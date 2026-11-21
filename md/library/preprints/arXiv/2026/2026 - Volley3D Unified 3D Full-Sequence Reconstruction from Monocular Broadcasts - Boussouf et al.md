<!-- source: library/preprints/arXiv/2026/2026 - Volley3D Unified 3D Full-Sequence Reconstruction from Monocular Broadcasts - Boussouf et al.pdf -->
<!-- item: https://arxiv.org/abs/2610.38358 -->
<!-- authors: Noâm Boussouf, Adrien Maglo, Mohamed Chaouch, Hideo Saito -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-21; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Volley3D: Unified 3D Full-Sequence Reconstruction from Monocular Broadcasts

                                         Volley3D: Unified 3D Full-Sequence Reconstruction from Monocular Broadcasts

                                                            Noâm Boussouf1,2 * Adrien Maglo3                    Mohamed Chaouch3             Hideo Saito1
                                                                     1
                                                                        Keio University, Japan 2 École Centrale de Nantes, France
                                                                    3
                                                                        Université Paris-Saclay, CEA-LIST, F-91120, Palaiseau, France
                                                                                              noam.boussouf@keio.jp
arXiv:2610.38358v1 [cs.CV] 28 Oct 2026




                                                  (a) Input 2D Broadcast View            (b) Reconstructed 3D Scene (Broadcast POV)      (c) Reconstructed 3D Scene (Other POV)

                                         Figure 1. Monocular 3D collective reconstruction from broadcast volleyball video. From a single uncalibrated broadcast sequence
                                         (a), our framework recovers 3D player poses, jump dynamics, and physical ball trajectories in global court coordinates, enabling realistic
                                         novel-view synthesis from multiple vantage points (b, c).

                                                                   Abstract                                      1. Introduction
                                                                                                                 In recent years, computer vision has revolutionized sports
                                         3D reconstruction from single-view sports broadcast is a                analysis, enabling automated data extraction for tactical in-
                                         pivotal capability for automated analytics and immersive                sights and performance optimization. Within this domain,
                                         AR/VR replays, yet notoriously ill-posed due to difficult-              3D reconstruction has emerged as a pivotal task. While
                                         to-calibrate moving cameras and depth ambiguity. Unlike                 multi-camera setups currently power elite-level tools like
                                         widely studied racket sports, team sports such as volleyball            semi-automated offside technology, their reliance on ex-
                                         feature unpredictable multi-contact sequences and high-                 pensive, synchronized infrastructure renders them inappli-
                                         altitude jumps. These dynamics categorically invalidate                 cable for universally accessible broadcast footage. Shift-
                                         the standard planar projection assumptions relied upon                  ing to a monocular paradigm is therefore essential. Not
                                         by existing methods. To resolve these limitations without               only to democratize sports analytics but also to unlock next-
                                         3D training supervision, we propose a complete, physics-                generation immersive applications. Specifically, lifting a
                                         grounded pipeline tailored to monocular broadcast volley-               standard 2D broadcast feed into 3D space enables view-
                                         ball. First, we include a correction module to the perspec-             ers to experience historical matches through Virtual Reality
                                         tive drift induced by ground-plane projection by coupling               (VR) and synthesizes novel camera angles for augmented
                                         temporal jump spotting with Newtonian interpolation for                 reality (AR) broadcasting. However, recovering depth from
                                         3D player placement. Second, for 3D ball trajectory es-                 a single uncalibrated viewpoint transforms 3D reconstruc-
                                         timation, we design a dedicated sub-trajectory segmenta-                tion into a highly ill-posed inverse problem. While recent
                                         tion architecture alongside a collision-matching algorithm.             monocular frameworks show promising results in sports
                                         By anchoring physical equations to reconstructed 3D hand                with constrained, ground-bound movements (e.g., table ten-
                                         vertices, we lift noisy ball 2D detections into a spatiotem-            nis [11] or badminton [20]), collective sports featuring un-
                                         porally coherent 3D scene. Evaluations on multi-camera                  predictable aerial gameplay remain under-explored.
                                         benchmarks demonstrate our approach significantly re-                       Volleyball stands out as a highly challenging yet under-
                                         duces 3D spatial drift compared to 2D-reprojection base-                researched domain. Due to its unique physical and spa-
                                         lines. Project Webpage : noambsf.github.io/Volley3D                     tial dynamics, it serves as a rigorous testing ground for
                                                                                                                 monocular 3D vision; a framework capable of accurately re-


                                                                                                             1
constructing a volleyball match possesses the versatility to              The second stage reconstructs the 3D ball trajectory
adapt to various other sports. Unlike racket sports character-        by exploiting these player-anchored mechanics. First, we
ized by strictly alternating turns, volleyball features unpre-        introduce a temporal sub-trajectory segmentation archi-
dictable, intra-team multi-contact sequences. Chief among             tecture that outperforms existing state-of-the-art models
its challenges is the omnipresence of high-amplitude verti-           in isolating ball deflection events. Next, a training-free,
cal jumps, which completely invalidates the static ground-            heuristic-based collision matching algorithm identifies the
contact assumptions relied upon by current state-of-the-art           specific agent and the exact hand responsible for the con-
pipelines. Furthermore, reconstructing this 3D space from             tact, utilizing the spatial features extracted in the first stage.
broadcast feeds is severely hindered by the lack of reliable          These identified 3D hand coordinates serve as precise sub-
3D calibration cues. The court provides almost no known               trajectory boundary conditions. Finally, we employ an opti-
3D reference points above the ground plane. While the net             mization algorithm governed by aerodynamic physics to lift
features standardized dimensions, its reference antennas are          the 2D ball detections into a coherent 3D trajectory. To rig-
visually ambiguous from distant broadcast angles. Conse-              orously validate our physics-grounded lifting against state-
quently, while pseudo-3D calibration might be acceptable              of-the-art methods, we conduct extensive ablation stud-
near the net, it degrades toward the backcourt, making tra-           ies on a 4 corner cameras, multi-view, semi-professional
ditional reprojection heuristics highly unstable. Finally, this       dataset for which we extract ground-truth 3D ball trajec-
depth ambiguity is exacerbated by moving cameras, low                 tories. Our evaluations demonstrate that anchoring physical
broadcast angles, and severe mutual players occlusions.               equations to player kinematics outperforms existing monoc-
   Compounding these physical and visual hurdles is se-               ular methods [21], which rely on 2D reprojection for initial
vere data scarcity. Unlike major sports such as football              conditions estimation and consequently suffer from impor-
or basketball, volleyball lacks large-scale datasets provid-          tant 3D spatial drift.
ing 3D ground-truth for both player and ball trajectories.               In summary, our main contributions are as follows:
This deficiency renders the training of massive, end-to-end           • A comprehensive monocular 3D reconstruction
deep learning architectures for direct 2D-to-3D mapping                 framework tailored to broadcast volleyball, which uni-
unfeasible. Consequently, we propose a modular pipeline                 fies player and 3D ball tracking into a spatiotemporally
that decomposes the overarching problem into specialized                coherent scene without relying on 3D training datasets.
computer vision sub-tasks. Importantly, instead of treating           • A physics-informed jump handling method that re-
ball trajectory estimation independently of human motion,               solves the depth drift caused by ground-plane projection
our framework explicitly addresses the lack of 3D ball data             models. By combining event spotting with Newtonian in-
by mathematically coupling them. By anchoring the ball’s                terpolation, our approach yields visually and physically
physical trajectory to detected player interactions, we en-             accurate 3D airborne player localizations.
force strict spatiotemporal consistency, establishing a co-           • A context-aware 3D ball trajectory lifting pipeline, in-
herent 3D reconstruction from a single video stream with-               troducing a sub-trajectory segmentation architecture, a
out requiring 3D training supervision.                                  training-free collision matching algorithm, and a player-
    Specifically, we propose a two-stage framework for                  anchored aerodynamic solver. Evaluations across a cal-
monocular 3D volleyball reconstruction (Fig. 2). The first              ibrated multi-view benchmark validate that grounding
stage focuses on player reconstruction, leveraging court                physical equations in player kinematics reduces 3D spa-
keypoint detection, 2D tracking, and camera-space 3D pose               tial drift compared to 2D-reprojection baselines.
extraction, followed by player position temporal smoothing.           2. Related Work
Building upon this foundation, the core innovation of this
stage lies in handling jumping players. Because monocu-               3D Multi-View Reconstruction in Sports. The 3D re-
lar depth recovery is inherently ill-posed, standard pipelines        construction of sports matches has been a prominent com-
rely on a strict ground-contact assumption to anchor players          puter vision research vector for over two decades. Early ex-
onto the court plane [11, 20, 28, 40]. However, this sim-             ploratory works in the 2000s primarily focused on virtual-
plifying constraint categorically fails during vertical exten-        izing soccer broadcast scenes [2, 24, 40]. Since then, multi-
sions. When a player jumps, their vertical elevation in the           camera architectures have achieved high-fidelity results
2D image plane is misinterpreted by the homography matrix             leveraging advanced stereo segmentation [14] and multi-
as a retreat in depth, causing severe spatial drift. To over-         person triangulation [1, 4]. While highly accurate, these
come this, we integrate a pose-based event spotting mod-              systems require meticulously calibrated and synchronized
ule tailored for precise takeoff and landing localization. We         camera networks, limiting their applicability to standard,
then apply Newtonian equations of motion to interpolate the           single-feed volleyball broadcast footage. Consequently, re-
player’s true 3D trajectory in world space, yielding visually         cent efforts have shifted toward monocular reconstruction,
and physically accurate airborne localizations.                       which fundamentally relies on strong spatial priors to re-

                                                                  2
solve the ill-posed nature of single-view depth estimation.          anism strictly requires an accurate 3D camera calibration
    Monocular 3D Reconstruction in Sports. To mitigate               matrix. MonoTrack [21] achieves this by relying on the ex-
single-view ambiguities, recent monocular frameworks tar-            plicit detection of the four court corners and two specific
geted constrained environments like badminton [20] and ta-           reference points on the net (from a corner view). In pro-
ble tennis [11]. These sports offer strict spatial separation        file broadcast volleyball, net reference points are frequently
between players, static cameras, and alternating turns. Such         visually ambiguous, occluded, or completely out of frame,
structured settings allow methods to leverage fixed view-            making stable 3D calibration exceedingly difficult and in-
points and strict planar ground assumptions, effectively by-         evitably leading to sub-optimal trajectory lifting. Addition-
passing mutual occlusions and simplifying 3D projectile              ally, MonoTrack [21] relies heavily on the inherent simplifi-
tracking. However, these systems rely heavily on domain-             cations of badminton dynamics, where the hitting player al-
specific heuristics (e.g., the MonoTrack [21] method for             ternates deterministically across the net, entirely bypassing
shuttlecocks) and fail to handle jump phases, as they strictly       the challenge of identifying which specific athlete is respon-
anchor players to the ground plane.                                  sible for the ball deflection. It also presumes a static cam-
    Monocular 3D Reconstruction in Collective Sports.                era and assumes the projectile never contacts the ground.
Transitioning to collective sports exposes the vulnerabilities       Similarly, while Grad et al. [13] introduce robust aerody-
of classical monocular pipelines due to continuous mutual            namic fitting pipelines over 2D projections, their methodol-
occlusions and unpredictably moving broadcast cameras.               ogy requires manual temporal segmentation, enforces rigid
Pioneering works like Soccer on Your Tabletop [28] bridged           ground-verticality heuristics that fail during aerial rallies,
this gap using 2D poses and massive synthetic datasets to            and remains highly sensitive to monocular calibration noise.
generate individual depth maps, though the resulting vol-                Parallel to explicit physical modeling, alternative frame-
umetric approximations often suffer from topological arti-           works explore geometric and deep learning methods to di-
facts such as disappearing player body parts. Similar frame-         rectly lift 2D ball detections into 3D space [18, 27, 35].
works for American football [30] face operational bottle-            While Zandycke et al. [35] propose an ingenious scale-
necks, requiring manual tracking initialization and relying          based ray projection framework, its reconstruction accuracy
on frame-by-frame NLF [29] reconstructions that lack tem-            remains sub-optimal as it processes frames independently
poral consistency. Crucially, these collective sport pipelines       without leveraging temporal video dynamics while still re-
do not support two major requirements for accurate volley-           quiring a fully calibrated camera. Alternatively, learning-
ball 3D reconstruction: they entirely ignore the ball’s 3D           based methods directly map pixel tracks to 3D coordi-
trajectory, losing essential tactical context, and they remain       nates [18, 27]. However, due to the severe scarcity of real-
rigidly bound to the planar ground assumption, failing to            world 3D ball annotations, their heavy reliance on synthetic
capture high-amplitude jumps.                                        training data introduces a pronounced domain gap that hin-
    To resolve these ambiguities, recent state-of-the-art            ders generalization on broadcast footage.
methods have reverted to multi-view setups. For instance,                To overcome these limitations, we propose a comprehen-
LiveSplats [16] applies 3D Gaussian Splatting across syn-            sive, modular framework for the holistic 3D reconstruction
chronized streams for basketball reconstruction. However,            of volleyball broadcast sequences. Unlike existing collec-
such dense camera networks preclude applicability to stan-           tive sports pipelines that strictly rely on planar ground as-
dard broadcast footage, underscoring the need for monoc-             sumptions and ignore ball dynamics, our approach intro-
ular frameworks capable of holistically capturing high-              duces a physics-informed jump handling module to correct
amplitude jumps and ball-player dynamics.                            jump-induced perspective drift. By coupling temporal event
    Monocular 3D Ball Trajectory Estimation. To recon-               spotting with Newtonian interpolation, we natively resolve
struct the 3D trajectory of a fast-moving projectile from a          the breakdown of projective models during high-amplitude
single camera feed, classical frameworks heavily leverage            aerial phases, yielding physically accurate 3D player local-
physics-based optimization by fitting aerodynamic equa-              izations. Furthermore, to circumvent the lack of 3D ball su-
tions to 2D image observations. These methods typically              pervision and the spatial drift caused by 2D-reprojection op-
segment the continuous video into discrete sub-trajectories,         timizations, we propose a context-aware 3D ball trajectory
subsequently optimizing the initial 3D position and veloc-           lifting pipeline. After introducing a temporal sub-trajectory
ity for each interval [5, 9, 13, 21, 31]. Recent frameworks          segmentation architecture and a heuristic collision match-
like MonoTrack [21] and Grad et al.’s [13] attempt to bound          ing algorithm, we anchor the ball’s aerodynamic optimiza-
this non-linear optimization by minimizing a 2D reprojec-            tion solver to the reconstructed 3D hand vertices. By using
tion loss to estimate these initial conditions. However, rely-       player kinematics as precise boundary conditions, our ap-
ing on 2D reprojection is fundamentally flawed for depth             proach completely bypasses the reliance on noise-sensitive
estimation, as it inherently yields severe spatial drift on          3D camera calibration, unifying athlete and ball dynamics
real-world datasets. Furthermore, this reprojection mech-            into a spatiotemporally coherent 3D scene.

                                                                 3
Figure 2. Overview of our proposed two-stage monocular 3D reconstruction pipeline. In the first stage, we extract and position the athletes
in 3D world-space, combining smoothed homographic projections with a pose-based jump spotting module to handle aerial phases. In the
second stage, we segment 2D ball tracks and explicitly anchor them to the reconstructed athletes, using the predicted 3D collision points
to physically constrain the final 3D ballistic trajectory. The blue modules highlight the contributions introduced in this paper.

3. Global Pipeline Overview                                             full-body 3D kinematics of the athletes using WHAM [32]
                                                                        to generate camera-space 3D poses.
The proposed end-to-end framework, illustrated in Figure 2,
                                                                           Fundamentally, the ground-plane projection of the player
is designed to map raw monocular broadcast videos onto a
                                                                        feet structurally fails during high-amplitude jumps. To re-
pre-modeled 3D volleyball court. To circumvent the severe
                                                                        solve this, we introduce a physics-informed jump handling
lack of multi-agent 3D ground truth, our framework is de-
                                                                        module. Because raw pixel-based event spotting strug-
coupled into two interconnected stages. Stage 1 establishes
                                                                        gles to isolate individual actions within a densely populated
the structural foundation by extracting and positioning the
                                                                        scene, we opt for PoseConvSpot [3] a pose-based architec-
athletes in 3D space, explicitly handling the transition be-
                                                                        ture. This discrete temporal isolation allows the pipeline
tween ground-contact and aerial phases. Building upon this,
                                                                        to explicitly override the planar projection. By applying
Stage 2 leverages the reconstructed players kinematics to
                                                                        Newtonian equations of motion between the homography-
constrain and estimate the 3D trajectory of the ball.
                                                                        derived takeoff and landing positions, we ensure physically
3.1. Player Reconstruction                                              accurate 3D mesh positioning during these aerial phases.
To establish the global spatial context, athletes must first be
                                                                        3.2. Context-Aware Ball 3D Trajectory Estimation
localized and tracked across the temporal sequence. We em-
ploy YOLOX [10] coupled with Deep-EIoU [15] for multi-                  The second stage reconstructs the projectile dynamics,
object tracking.                                                        abandoning standalone 3D trajectory optimizations in favor
    To register these tracked 2D bounding boxes within the              of a context-aware anchoring approach. Initially, 2D ball
global 3D court space, we continuously compute the ho-                  tracking is performed using TrackNetV3 [6], which proved
mography matrix between the 2D image plane and the court                to be highly accurate for localizing small, high-velocity,
ground plane. This is achieved utilizing the court keypoint             and motion-blurred projectiles in sports feeds. Given the
detection architecture proposed by Maglo et al. [22]. As-               discontinuous nature of volleyball trajectories, these global
suming a strict ground-contact constraint, players’ 2D foot             2D tracks are subsequently segmented into discrete sub-
coordinates are projected through this homography to ob-                trajectories with our introduced architecture.
tain absolute world-space positions. However, extracting                    Instead of relying on unstable calibration-based 2D-
coordinates via 2D homographic projections from a moving                reprojection optimizations to lift these tracklets, we explic-
camera introduces high-frequency spatial noise. To enforce              itly anchor the ball to the reconstructed environment. A
temporal stability prior to 3D lifting, we introduce a filtering        training-free, heuristic-based collision matching algorithm
module applying a Butterworth low-pass filter to the pro-               is deployed to identify the agent, either a player or the court
jected 2D ground-plane trajectories, mitigating projection              surface (assuming no net contacts in this study), and the ex-
jitter (as shown on Fig. 3). Simultaneously, we extract the             act hand responsible for initiating each sub-trajectory. By


                                                                    4
retrieving the corrected 3D kinematics generated in the first                                               Drift                   Drift
                                                                                                 6        (0.84 m)                (0.20 m)                        Drift
                                                                                                                                                                (1.42 m)




                                                                      Court Depth - Y Axis (m)
stage, these identified 3D hand vertices establish precise
                                                                                                 5
boundary conditions. Finally, we employ an aerodynamic
                                                                                                 4
optimization solver to lift the 2D detections into a contin-
                                                                                                 3
uous 3D trajectory. By natively bounding these physical
equations between the verified player interaction points, our                                    2
                                                                                                                                              Airborne Phase
                                                                                                 1                                            Raw Homography (2D Projection)
approach completely bypasses the need for explicit 3D cam-                                                                                    Filtered (Ground Plane)
                                                                                                 0                                            Ours (Physics-Corrected Jump)
era calibration, seamlessly unifying the athletes and the ball
into a single, spatiotemporally coherent representation.                                             50              100    150              200               250
                                                                                                                           Time (Frames)

4. Jump-Aware 3D Player Reconstruction                                  Figure 3. ButterWorth Filtering and Perspective Drift Correc-
                                                                        tion . The raw 2D homographic projection of a player’s position
As highlighted in Section 3, standard monocular 3D po-                  during a sequence (grey) exhibits high-frequency jitter. While
sitioning heavily relies on a strict ground-contact assump-             temporal filtering (blue dashed line) stabilizes ground locomo-
tion. However, volleyball is defined by frequent, high-                 tion, it fails during airborne phases (yellow zones). Our physics-
amplitude jumps. During these airborne phases, the 2D ho-               informed interpolation (solid red line) overrides the ground-plane.
mographic projection fundamentally breaks down. When
a player jumps, their elevation in the 2D image plane is                5. Scene-Constrained Ball Trajectory Lifting
misinterpreted by the homography matrix as a retreat in
                                                                        Unlike racquet sports where projectile dynamics are strictly
depth, causing severe perspective drift along the court’s
                                                                        alternating and highly predictable, a volleyball rally is char-
plane. To resolve this, we propose to decouple the prob-
                                                                        acterized by various possible trajectories such as intra-team
lem into two tasks: precisely isolating the temporal interval
                                                                        passes, spikes, and bumps, which are often discontinuous.
of each jump, and physically correcting the 3D trajectory
                                                                        To reconstruct this complex 3D ball motion without relying
during this interval.
                                                                        on 3D training data or noise-sensitive 2D reprojection, we
    Precise Jump Spotting. Extracting frame-accurate
                                                                        introduce a scene-constrained lifting approach that anchors
micro-events in unconstrained broadcast footage is highly
                                                                        the ball’s physical equations to the reconstructed athletes.
challenging. Traditional RGB-based pipelines struggle with
dense multi-player scenarios, where spatial overlaps and
mutual occlusions severely degrade pixel-level feature ex-              5.1. 2D Ball Sub-Trajectory Segmentation
traction. To circumvent this, we utilize PoseConvSpot [3],              The first step requires isolating the global 2D ball track, ex-
a purely pose-based temporal event spotting architecture.               tracted continuously via TrackNetV3 [6], into discrete bal-
Relying exclusively on 2D joint coordinates, already ex-                listic sub-trajectories separated by deflection points (e.g.,
tracted during our initial tracking phase, makes this ap-               hits, passes, or bounces). To extract these frame-accurate
proach computationally efficient and robust to visual over-             micro-events, we propose a lightweight Temporal Convolu-
laps that plague crowded broadcast sports while being more              tional Network (TCN).
robust to domain shifts [3]. This module allows us to reli-
                                                                            For a given temporal window of length T , the network
ably identify the exact discrete takeoff (t = 0) and landing
                                                                        takes a 4-channel input sequence consisting of the ball’s 2D
(t = tf ) frames for each jumping athlete.
                                                                        image coordinates and their first-order temporal derivatives:
    Airborne Trajectory Correction. Once the exact tem-
                                                                        Xt = [xt , yt , dxt , dyt ]T , and outputs a probability vector
poral boundaries of a jump are isolated, we reconstruct
                                                                        of length T , where each element represents the likelihood
the player’s true 3D trajectory by overriding the flawed
                                                                        of the corresponding frame containing a deflection point.
homographic projection. The corresponding world-space
                                                                        The architecture processes this sequence through an initial
boundary coordinates at takeoff, (x0 , y0 , 0), and landing,
                                                                        1D convolution, followed by a series of TCN blocks lever-
(xf , yf , 0), are obtained from the ground-plane homogra-
                                                                        aging dilated convolutions. These dilated residual blocks
phy . Integrating the acceleration twice over the interval
                                                                        efficiently expand the network’s receptive field to capture
t ∈ [0, tf ] with our ground-contact boundary conditions
                                                                        broad spatiotemporal context. More details of the architec-
yields the corrected spatiotemporal trajectory:
                                                                        ture in Supplementary.
                    t                         g                             We formulate sub-trajectory segmentation as continuous
  pxy (t) = p0 +      (pf − p0 ),    z(t) =     t(tf − t)   (1)         per-frame regression rather than frame-wise classification,
                   tf                         2
                                                                        adopting the formulation and Soft-Gamma Loss of PoseC-
where g is the gravitational acceleration (9.81 m/s2 ). Fig-            onvSpot [3] for human event spotting, we frame deflection
ure 3 shows the effect of Butterworth filtering and jumping             detection as a regression task over Gaussian-smoothed tem-
player position correction during jumps.                                poral labels.


                                                                  5
5.2. Heuristics-Based Collision Agent Matching                         is the initial velocity vector vi for this specific segment.
Once the 2D track is segmented into discrete sub-                      Rather than relying on 2D reprojection heuristics, we di-
trajectories, each deflection point must be associated with            rectly solve for the exact vi that satisfies these physical con-
its physical source. Bypassing data-hungry networks that               straints. We define an optimization problem to minimize the
                                                                       Euclidean endpoint error:
lack annotated training data, we propose a training-free
heuristic matching algorithm.                                                                                            2
    At every identified hit frame thit , the algorithm evaluates                   vi∗ = arg min P̂i+1 (vi ) − Pi+1                (4)
                                                                                               vi
the spatial and kinematic relationship between the 2D ball
detection and the skeletal joints of tracked athletes. Specifi-        where P̂i+1 (vi ) is the simulated final position obtained by
cally, we compute a collision score Sj,k for joint j of player         numerically integrating the differential equation over ∆t.
k, combining spatial proximity and localized joint velocity:           The optimization is efficiently solved using the Nelder-
                                       !                               Mead algorithm. The solver is initialized with the closed-
                                 d2j,k
               Sj,k = β exp − 2 + λVj,k                      (2)       form pure ballistic velocity (assuming zero drag, Cd = 0).
                                  2σ                                      Once vi∗ is optimized, the 3D position of the ball at any
                                                                       intermediate frame t ∈ [ti , ti+1 ] is computed using Semi-
where dj,k is the Euclidean pixel distance between the ball            Implicit Euler Method. We rigorously validate the superior-
and wrist node j of player k, σ controls the Gaussian prox-            ity of this physics-grounded lifting approach over standard
imity decay, and Vj,k is the wrist velocity computed via fi-           2D-reprojection optimizations in Sec. 5.3.
nite differences over a temporal window (thit ± τ ).
    The athlete with the highest wrist score is identified as          6. Experiments and Results
the collision agent, with the left/right score margin deter-
mining the contacting hand(s). If an ankle-to-wrist proxim-            While qualitative assessment of our pipeline can be per-
ity ratio indicates the ball is closer to the ground than player       formed through visual inspection of the reconstructions
wrists, the event is classified as a court bounce.                     (see Sec. 7), obtaining a quantitative evaluation is more
                                                                       challenging due to the lack of broadcast video recordings
5.3. Physics-Informed 3D Trajectory Estimation                         with calibrated cameras, synchronized human motion cap-
Existing monocular lifting methods attempt to resolve depth            ture and 3D ball tracking. Therefore, we evaluate the indi-
by incorporating 2D reprojection losses into non-linear tra-           vidual components of our pipeline to the best of our ability.
jectory optimizations. However, this assumes pristine 3D
camera calibration matrices and 2D Ball Tracking. Thus,                6.1. Experimental Setup
it suffers from severe spatial drift in difficult-to-calibrate         To train and evaluate our modules, we leverage established
broadcast scenarios. Our framework bypasses this depth                 sports benchmarks and extensive novel manual annotations.
ambiguity by framing 3D trajectory lifting as a strictly               Broadcast Volleyball Dataset. Because our pipeline is
bounded Boundary Value Problem (BVP).                                  specifically designed for unconstrained broadcast environ-
    For any identified sub-trajectory spanning between con-            ments, we substantially extend the Volleyball dataset by
secutive deflection frames ti and ti+1 , the collision agents          Saad et al. [17]. We manually annotated multiple subsets
provide the 3D interaction points. By retrieving the precise           while maintaining the original cross-match splits:
world-space coordinates of the hitting hand at ti (denoted             • Court Calibration: We manually annotated 4 to 9 vis-
Pi = (xi , yi , zi )) and the receiving hand or court ground              ible court keypoints in 1,500 diverse frames to robustly
at ti+1 (denoted Pi+1 ), we establish rigid initial and final             evaluate homography estimation.
boundary conditions.                                                   • Perspective Drift: 50 challenging aerial phases were an-
    The flight of a volleyball is governed by gravity and aero-           notated with takeoff/landing foot coordinates and human
dynamic drag. Neglecting the Magnus effect, the velocity                  estimation of their orthogonal ground projections to eval-
vector v(t) = [vx (t), vy (t), vz (t)]T is governed by the fol-           uate spatial drift mitigation.
lowing first-order differential equation:                              • Trajectory Segmentation and Agent Collision Match-
                dv(t)                                                     ing: We labeled over 1,600 trajectory-change events
                      = g − Cd ∥v(t)∥v(t)                   (3)           across various arenas to train, evaluate and compare seg-
                 dt
                                                                          mentation modules. We also included SportsMOT [8]
                                                     ρAC
where g = [0, 0, −9.81]T m/s2 and Cd =            2m
                                                    drag
                                                         is               videos to have a wider range of courts.
                                                 −1
the drag-to-mass coefficient (computed to 0.035 m using                For 2D ball tracking, we utilized the existing annotations
standard volley ball measurements).                                    provided by Perez et al. [26] to train TrackNetV3 [6]. To
   Since the trajectory must connect Pi and Pi+1 over the              foster future research in volleyball analytics, all our annota-
time interval ∆t = ti+1 − ti , the only unknown variable               tions will be made publicly available.


                                                                   6
 Backbone          Mean IoU (%)      Proj. Err (m)     Reproj. Err (px)       Method              3D RMSE (m) X/Y/Z RMSE (m) 2D Reproj. (px)
 ViT-Tiny [38]         96.03              0.181               0.009           MonoTrack [21]           1.56      1.42 / 0.62 / 0.12    3.89
 PVTv2 [36]            96.67              0.144               0.007
                                                                                       Theoretical Bounds (Using 3D GT Start/End Points)
        (a) Performance of court keypoint detection backbones.
                                                                              Pure Ballistics          0.38      0.28 / 0.10 / 0.23    19.2
   Method                             MAE (m)             RMSE (m)
                                                                              With Drag                0.29      0.14 / 0.09 / 0.24    17.9
   Standard Homography                  1.050                1.431
   Ours (Physics-Informed)              0.230                0.412                              Our Pipeline (Using 3D Hand Bounds)

      (b) Perspective drift mitigation along court depth (Y -axis).           Pure Ballistics          0.38      0.31 / 0.14 / 0.18    19.4
                                                                              With Drag                0.27      0.15 / 0.13 / 0.18    17.2
Table 1. Quantitative Evaluation of 3D Player Reconstruction
Components.
                                                                              Table 3. 3D Ball Trajectory Estimation on VolliQ. Evaluation
   Method                                 δ=1        δ=2       δ=3            of 3D spatial accuracy and 2D reprojection error. Our holis-
                  Using Oracle 2D Ball Trajectory                             tic physics-informed approach drastically reduces 3D spatial drift
                                                                              compared to reprojection-based optimization.
   Baseline 1 (Y (t))                     0.801      0.840     0.843
   Baseline 2 (X(t) + Y (t))              0.794      0.872     0.884
   TT3D (Poly. only) [11]                 0.713      0.751     0.764
   TT3D (Poly. + PCA Blur) [11]           0.762      0.807     0.810
   HitNet (MonoTrack) [21]                0.836      0.874     0.877
   Ours (TCN + Soft-Focal)                0.929      0.945     0.950
                 Using Predicted 2D Ball Trajectory
   Heuristic Y (t)                        0.759      0.802     0.812
   Heuristic X(t) + Y (t)                 0.714      0.794     0.813
   TT3D (Poly. only) [11]                 0.689      0.725     0.736
   TT3D (Poly. + PCA Blur) [11]           0.702      0.751     0.770          Figure 4. Qualitative comparison of 3D trajectory reconstruc-
   HitNet (MonoTrack) [21]                0.815      0.858     0.866          tion on a short rally from Volliq [37]. Our drag model (green,
   Ours (TCN + Soft-Focal)                0.898      0.914     0.925          err: 0.19 m, 12.7 px) accurately follows the ground truth (red)
                                                                              compared to MonoTrack [21] (purple, err: 1.69 m, 4.32 px).
Table 2. 2D Ball Trajectory Segmentation (F1-Score). Perfor-
mance across temporal tolerances δ ∈ {1, 2, 3} frames.                        (PVTv2) [36]. As shown in Tab. 1a, PVTv2 achieves higher
VolliQ 3D Validation Dataset. While our pipeline is de-                       spatial precision at the expense of increased inference time.
signed for uncalibrated moving broadcast cameras, rig-                        Jump-Aware Trajectory Correction. We evaluate aerial
orously evaluating the core 3D physics-informed lifting                       perspective drift mitigation along court depth (Y -axis)
mechanism against existing 2D-reprojection baselines re-                      across 50 annotated jumps (> 800 airborne frames). As
quires 3D ground truth. As none exists as far as we know,                     shown in Tab. 1b, our physics-informed correction signif-
to avoid the domain gap introduced by synthetic datasets,                     icantly reduces drift compared to standard homography.
we utilized VolliQ [37], a semi-professional dataset fea-                     Qualitative results show that remaining residual errors stem
turing four synchronized, static cameras positioned at the                    primarily from human annotation ambiguity in estimat-
court corners. We semi-manually annotated the exact 2D                        ing orthogonal ground projections from monocular profile
ball coordinates across 10 continuous, fully active rallies                   views, rather than algorithmic failure.
(yielding over 12,000 bounding boxes across 3,000 multi-
view frames). These views were triangulated, after cameras                    6.3. 3D Ball Trajectory Estimation
3D calibration, to establish a real-world 3D ballistic ground
truth for our ablation studies.                                               2D Ball Tracking and Trajectory Segmentation. We
                                                                              benchmark our segmentation module against heuristic and
Implementation Details. Extensive training protocols, hy-                     learned baselines using the F1-Score across three temporal
perparameter configurations for all tasks and dataset details                 tolerances (δ ∈ {1, 2, 3} frames). To decouple segmenta-
are deferred to the Supplementary Material.                                   tion from upstream 2D detection errors, we evaluate on both
                                                                              Oracle and TrackNetV3 predicted trajectories.
6.2. 3D Player Reconstruction
                                                                                 We compare our module to four baselines. Heuristics
Court Calibration. To compute the continuous image-to-                        Y(t) and X(t) + Y(t) geometrically detect deflections via
court homography, we adapt the keypoint detection pipeline                    gradient sign changes in the ball’s 2D pixel coordinates. We
of Maglo et al. [23] to volleyball. Following the metrics in                  also adapt TT3D Piecewise Polynomials [11] in two vari-
Chu et al. [7], we compare the lightweight ViT-Tiny [38]                      ants: a standard solver and one augmented with PCA-based
(original backbone) against a Pyramid Vision Transformer                      motion blur, bypassing its native BlurBall [12] module due


                                                                          7
Figure 5. Qualitative 3D reconstruction results across diverse game scenarios. Top: 2D input broadcast frames from different rallies.
Bottom: corresponding unified 3D scene reconstruction.

to the lack of a volleyball-specific blur dataset. Finally, we       hands) against theoretical “GT Bounds” (GT start/end 3D
evaluate HitNet (MonoTrack) [21], a data-driven racquet              ball coordinates). Surprisingly, anchoring to 3D hands out-
sports model. Because HitNet requires the hitter’s pose, an          performs GT ball bounds (0.272m vs. 0.293m). We at-
ambiguous input in volleyball before collision matching, we          tribute this to multi-frame contacts: because we assume in-
restrict its inputs to 2D ball tracks and court corners.             stantaneous hits, exact GT ball positions cause simulated
    As demonstrated in Tab. 2, our TCN architecture signif-          trajectories to depart prematurely. Anchoring to hand ver-
icantly outperforms all baselines. Moreover, Tab. 2 reveals          tices, which sit lower than the ball during contact, geometri-
that standard heuristics are highly sensitive to 2D tracking         cally compensates for this temporal mismatch, as confirmed
noise, whereas our network maintains a robust 0.898 F1-              by the vertical Z-axis error drop (0.182m vs. 0.242m).
Score (δ = 1) even on raw TrackNetV3 predictions.
                                                                     7. Qualitative experiments
Heuristic Collision Agent Matching. We evaluate our spa-
                                                                     Figures 1 and 5 showcase our pipeline across dynamic plays
tial proximity matching (Sec. 5.2) using three metrics: (1)
                                                                     (spikes, sets, blocks). Despite the depth ambiguity inherent
Agent Identification (player ID or ground); (2) Strict Hand
                                                                     to monocular broadcast feeds, our framework reliably re-
Assignment (left, right, or both hands); and (3) a relaxed
                                                                     covers the global 3D layout of most players, with physics-
Functional Hand Assignment. In volleyball, two-handed
                                                                     informed jump spotting lifting jumping actors to plausible
contacts (e.g., setting, bump, block) bring the hands to-
                                                                     heights. While extreme 2D overlap from rare camera align-
gether. Because our 3D solver anchors two-handed hits to
                                                                     ments can occasionally conceal players (e.g., the missed
a single reference hand vertex (right) without physical bias,
                                                                     blocker in the rightmost column), the reconstructed ball re-
the functional metric only penalizes strictly lateral hand as-
                                                                     mains consistent with game dynamics, demonstrating ro-
signment errors. On Oracle 2D trajectories, our algorithm
                                                                     bust spatiotemporal coherence. More examples are in Sup-
achieves 85.3% agent identification accuracy, with 98.8%
                                                                     plementary Materials.
functional and 75.8% strict hand assignment. On noisy ball
predictions, performance remains remarkably robust, with             8. Conclusion and Future Work
agent identification dropping only slightly to 83.3%.
                                                                     We presented Volley3D, a unified framework for lifting un-
In-The-Lab Validation: Physics-Based Lifting. We val-                calibrated monocular broadcast volleyball footage into a
idate our holistic lifting methodology using our triangu-            spatiotemporally coherent 3D scene. Our pipeline first cor-
lated ball 3D ground truth of the multi-camera VolliQ                rects ground-plane projection flaws by coupling pose-based
dataset [37]. While VolliQ’s static cameras do not assess our        jump spotting with Newtonian interpolation, yielding phys-
broadcast-specific tracking algorithms, they isolate and val-        ically accurate 3D localizations for airborne players. Then,
idate the physical coherence of our 3D formulation against           by introducing a TCN-based trajectory segmentation archi-
state-of-the-art 2D-reprojection methods.                            tecture with a collision matching algorithm, our method an-
   As shown in Tab. 3 and Fig. 4, MonoTrack [21] overfits            chors the ball’s aerodynamic equations directly to the ath-
to the image plane: achieving minimal 2D reprojection er-            letes’ reconstructed 3D hands, resulting in physically plau-
ror (3.9px) but severe depth ambiguity (1.56m 3D RMSE).              sible 3D reconstructions of complex rallies.
Conversely, our aerodynamic pipeline prioritizes spatial co-            Future work includes an end-to-end evaluation of the
herence, slashing the 3D RMSE to 0.272m and ensuring                 complete pipeline using a new dataset pairing broadcast
physically sound trajectories consistent with ball dynamics.         camera views with synchronized 3D ground truth, as well
We ablate our predicted “GT Hand Bounds” (triangulated               as adapting the pipeline for real-time processing.


                                                                 8
References                                                               [13] Lukasz Grad, Krzysztof M Czajkowski, and Aliaksandr
                                                                              Varashylau. Physics-based 3d ball trajectory reconstruction
 [1] Islam Amar, Abdalla Elsana, and Jihad El-Sana. Live free-                from monocular soccer video: A multi-model benchmark.
     view video for soccer games. In Proceedings of the 28th                  In Proceedings of the IEEE/CVF Conference on Computer
     International ACM Conference on 3D Web Technology, New                   Vision and Pattern Recognition (CVPR) Workshops, pages
     York, NY, USA, 2023. Association for Computing Machin-                   9940–9948, 2026. 3
     ery. 2                                                              [14] Jean-Yves Guillemaut and Adrian Hilton. Joint multi-layer
 [2] T. Bebie and Hanspeter Bieri.           A video-based 3d-                segmentation and reconstruction for free-viewpoint video
     reconstruction of soccer games. Computer Graphics Forum,                 applications. International Journal of Computer Vision, 93:
     19:391 – 400, 2000. 2                                                    73–100, 2011. 2
 [3] Noâm Boussouf, Adrien Maglo, Mohamed Chaouch, Paul                 [15] Hsiang-Wei Huang, Cheng-Yen Yang, Jiacheng Sun, Pyong-
     Pham Dang, and Hideo Saito. Poseconvspot: Overcoming                     Kun Kim, Kwang-Ju Kim, Kyoungoh Lee, Chung-I Huang,
     domain shifts in precise event spotting for sports videos via            and Jenq-Neng Hwang. Iterative scale-up expansioniou
     pose-only spatio-temporal regression. In Proceedings of the              and deep features association for multi-object tracking in
     ACM International Workshop on Multimedia Content Anal-                   sports. In 2024 IEEE/CVF Winter Conference on Applica-
     ysis in Sports (MMSports), 2026. 4, 5, 11, 13                            tions of Computer Vision Workshops (WACVW), pages 163–
 [4] Lewis Bridgeman, Marco Volino, Jean-Yves Guillemaut,                     172. IEEE, 2024. 4, 11, 13
     and Adrian Hilton. Multi-person 3d pose estimation and              [16] Junkai Huang, Saswat Subhajyoti Mallick, Alejandro Amat,
     tracking in sports. In Proceedings of the IEEE/CVF Confer-               Marc Ruiz Olle, Albert Mosella-Montoro, Bernhard Kerbl,
     ence on Computer Vision and Pattern Recognition (CVPR)                   Francisco Vicente Carrasco, and Fernando De la Torre.
     Workshops, 2019. 2                                                       Echoes of the coliseum: Towards 3d live streaming of sports
 [5] Hua-Tsung Chen, Wen-Jiin Tsai, Suh-Yin Lee, and Jen-Yu                   events. ACM Trans. Graph., 44(4), 2025. 3
     Yu. Ball tracking and 3d trajectory approximation with ap-          [17] Mostafa S. Ibrahim, Srikanth Muralidharan, Zhiwei Deng,
     plications to tactics analysis from single-camera volleyball             Arash Vahdat, and Greg Mori. A hierarchical deep temporal
     sequences. Multimedia Tools Appl., 60(3):641–667, 2012. 3                model for group activity recognition. In 2016 IEEE Confer-
 [6] Yu-Jou Chen and Yu-Shuen Wang. Tracknetv3: Enhancing                     ence on Computer Vision and Pattern Recognition (CVPR),
     shuttlecock tracking with augmentations and trajectory rec-              2016. 6, 11, 13
     tification. In Proceedings of the 5th ACM International Con-        [18] Daniel Kienzle, Katja Ludwig, Julian Lorenz, Shin’ichi
     ference on Multimedia in Asia, New York, NY, USA, 2024.                  Satoh, and Rainer Lienhart. Uplifting table tennis: A robust,
     Association for Computing Machinery. 4, 5, 6, 11, 13                     real-world application for 3d trajectory and spin estimation.
                                                                              In Proceedings of the IEEE/CVF Winter Conference on Ap-
 [7] Yen-Jui Chu, Jheng-Wei Su, Kai-Wen Hsiao, Chi-Yu Lien,
                                                                              plications of Computer Vision (WACV), 2026. 3
     Shu-Ho Fan, Min-Chun Hu, Ruen-Rone Lee, Chih-Yuan
     Yao, and Hung-Kuo Chu. Sports field registration via                [19] Colin Lea, Rene Vidal, Austin Reiter, and Gregory D. Hager.
     keypoints-aware label condition. In 2022 IEEE/CVF Con-                   Temporal convolutional networks: A unified approach to ac-
     ference on Computer Vision and Pattern Recognition Work-                 tion segmentation, 2016. 14
     shops (CVPRW), pages 3522–3529, 2022. 7                             [20] Tica Lin, Alexandre Aouididi, Chen Zhu-Tian, Johanna
                                                                              Beyer, Hanspeter Pfister, and Jui-Hsien Wang. Vird: Immer-
 [8] Yutao Cui, Chenkai Zeng, Xiaoyu Zhao, Yichun Yang,
                                                                              sive match video analysis for high-performance badminton
     Gangshan Wu, and Limin Wang. Sportsmot: A large multi-
                                                                              coaching. IEEE transactions on visualization and computer
     object tracking dataset in multiple sports scenes. arXiv
                                                                              graphics, 30(1):458–468, 2023. 1, 2, 3
     preprint arXiv:2304.05170, 2023. 6, 11
                                                                         [21] Paul Liu and Jui-Hsien Wang. Monotrack: Shuttle trajec-
 [9] Jiaxu Dong, Xina Cheng, and Takeshi Ikenaga. Multi-                      tory reconstruction from monocular badminton video. In
     physical and temporal feature based self-correcting approxi-             2022 IEEE/CVF Conference on Computer Vision and Pat-
     mation model for monocular 3d volleyball trajectory analy-               tern Recognition Workshops (CVPRW), pages 3512–3521.
     sis. In 2021 17th International Conference on Machine Vi-                IEEE, 2022. 2, 3, 7, 8, 12, 16, 17
     sion and Applications (MVA), pages 1–4, 2021. 3                     [22] Adrien Maglo, Astrid Orcesi, Julien Denize, and
[10] Zheng Ge, Songtao Liu, Feng Wang, Zeming Li, and Jian                    Quoc Cuong Pham. Individual locating of soccer players
     Sun. Yolox: Exceeding yolo series in 2021. arXiv preprint                from a single moving view. Sensors, 23(18), 2023. 4
     arXiv:2107.08430, 2021. 4, 11, 13                                   [23] Adrien Maglo, Astrid Orcesi, Julien Denize, and
[11] Thomas Gossard, Andreas Ziegler, and Andreas Zell. Tt3d:                 Quoc Cuong Pham. Individual locating of soccer players
     Table tennis 3d reconstruction. In 2025 IEEE/CVF Con-                    from a single moving view. Sensors, 23(18), 2023. 7, 13
     ference on Computer Vision and Pattern Recognition Work-            [24] Cornelius Malerczyk. 3d-reconstruction of soccer scenes.
     shops (CVPRW), pages 5821–5831. IEEE, 2025. 1, 2, 3, 7                   pages 1 – 4, 2007. 2
[12] Thomas Gossard, Filip Radovic, Andreas Ziegler, and An-             [25] Yin May Oo, Ankhzaya Jamsrandorj, Vanyi Chao,
     dreas Zell. Blurball: Joint ball and motion blur estimation              Hoang Quoc Nguyen, Yewon Hwang, Kyung-Ryoul Mun,
     for table tennis ball tracking. Proceedings of the IEEE/CVF              and Jinwook Kim. Jump-aware: Player position rectification
     Conference on Computer Vision and Pattern Recognition                    and identification in dynamic sports using jump event spot-
     (CVPR) Workshops, 2026. 7                                                ting. In Proceedings of the Computer Vision and Pattern


                                                                     9
     Recognition Conference (CVPR) Workshops, pages 5935–                 [40] Xinguo Yu, Xin Yan, Tze Sen Hay, and Hon Wai Leong.
     5944, 2025. 11                                                            3d reconstruction and enrichment of broadcast soccer video.
[26] Mauricio Perez, Jun Liu, and Alex C. Kot. Skeleton-based                  page 260–263, New York, NY, USA, 2004. Association for
     relational reasoning for group activity analysis. Pattern                 Computing Machinery. 2
     Recognition, 122:108360, 2022. 6, 11, 13
[27] Puntawat Ponglertnapakorn and Supasorn Suwajanakorn.
     Where is the ball: 3d ball trajectory estimation from 2d
     monocular tracking. In Proceedings of the IEEE/CVF Con-
     ference on Computer Vision and Pattern Recognition (CVPR)
     Workshops, pages 6168–6177, 2025. 3
[28] Konstantinos Rematas, Ira Kemelmacher-Shlizerman, Brian
     Curless, and Steve Seitz. Soccer on your tabletop. In
     2018 IEEE/CVF Conference on Computer Vision and Pat-
     tern Recognition, pages 4738–4747. IEEE, 2018. 2, 3
[29] István Sárándi and Gerard Pons-Moll. Neural localizer
     fields for continuous 3d human pose and shape estimation.
     Advances in Neural Information Processing Systems, 37:
     140032–140065, 2024. 3
[30] Kanta Sawafuji, Rintaro Otsubo, Dan Mikami, and Hideo
     Saito. 3d reconstruction of american football game situa-
     tions from handheld monocular video. In Proceedings of
     the IEEE/CVF Conference on Computer Vision and Pattern
     Recognition (CVPR) Workshops, pages 10048–10057, 2026.
     3
[31] Lejun Shen, Qing Liu, Lin Li, and Haipeng Yue. 3d recon-
     struction of ball trajectory from a single camera in the ball
     game. In Proceedings of the 10th International Symposium
     on Computer Science in Sports (ISCSS), pages 33–39, Cham,
     2016. Springer International Publishing. 3
[32] Soyong Shin, Juyong Kim, Eni Halilaj, and Michael J Black.
     Wham: Reconstructing world-grounded humans with accu-
     rate 3d motion. In 2024 IEEE/CVF Conference on Computer
     Vision and Pattern Recognition (CVPR), pages 2070–2080.
     IEEE, 2024. 4, 11, 13
[33] Shuhei Tarashima, Muhammad Abdul Haq, Yushan Wang,
     and Norio Tagawa. Widely applicable strong baseline for
     sports ball detection and tracking. In BMVC, 2023. 15, 16
[34] Shuhei Tarashima, Muhammad Abdul Haq, Yushan Wang,
     and Norio Tagawa. Widely applicable strong baseline for
     sports ball detection and tracking, 2023. 11
[35] Gabriel Van Zandycke and Christophe De Vleeschouwer.
     3d ball localization from a single calibrated image. In
     2022 IEEE/CVF Conference on Computer Vision and Pat-
     tern Recognition Workshops (CVPRW), pages 3471–3479.
     IEEE, 2022. 3
[36] Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao
     Song, Ding Liang, Tong Lu, Ping Luo, and Ling Shao. Pvt
     v2: Improved baselines with pyramid vision transformer.
     Computational Visual Media, 8(3):415–424, 2022. 7, 13
[37] N.H. Wanigasingha, M.K.A. Ariyaratne, and R.M. Silva.
     Volliq - multiangle volleyball dataset, 2026. 7, 8, 12, 16
[38] Kan Wu, Jinnian Zhang, Houwen Peng, Mengchen Liu, Bin
     Xiao, Jianlong Fu, and Lu Yuan. Tinyvit: Fast pretraining
     distillation for small vision transformers, 2022. 7
[39] Yufei Xu, Jing Zhang, Qiming Zhang, and Dacheng Tao.
     ViTPose: Simple vision transformer baselines for human
     pose estimation. In Advances in Neural Information Pro-
     cessing Systems, 2022. 11, 13


                                                                     10
Volley3D: Unified 3D Full-Sequence Reconstruction from Monocular Broadcasts
                                                  Supplementary Material
A. Datasets Details                                                       dataset [25], ensuring accurate temporal localization of
                                                                          aerial phases without any further adaptation.
This section provides comprehensive details regarding the
datasets used for training and evaluating each module of our              A.2. Ball Lifting
pipeline, as well as our custom annotation procedures.
                                                                          2D Ball Tracking. We train TrackNetV3’s full
A.1. Players Reconstruction Modules                                       pipeline [6] (TrackNet and InPaintNet) using the an-
                                                                          notations provided by Perez et al. [26] on the Volleyball
Detection and Tracking For 2D multi-object detection                      dataset originally introduced by Saad et al. [17]. We
and tracking, we directly employ the YOLOX [10] detec-                    adapted the training configuration as detailed in Sec. B. A
tion model and the Deep-EIoU [15] re-identification tracker               comparison of our 2D tracking performance against the
pre-trained on the SportsMOT dataset [8]. No further fine-                state-of-the-art results reported directly by Tarashima et
tuning was performed for these modules.                                   al. [34] on this same dataset (marked with †) is provided in
                                                                          Sec. C.
Court Calibration Despite prior works addressing court
calibration, there is, to the best of our knowledge, no pub-              Trajectory Segmentation and Agent Collision. The
licly available annotated dataset dedicated to volleyball. To             original dataset from Saad et al. [17] consists of short, over-
train our keypoints detection network (from which we ob-                  lapping, 41-frame video clips. Because our temporal con-
tain homography estimation between the 2D image space                     volutional network (TCN) requires a receptive field of 17
and court plane), we manually annotated broadcast vol-                    frames, applying it to such short clips introduces severe
leyball frames from the Volleyball Dataset [17]. For each                 boundary effects. To mitigate this, we merged consecutive
frame, we annotated 4 to 9 keypoints of the court to ob-                  clips belonging to the same rally into continuous sequences.
tain a robust GT homography. As fish-eye limitations can                  To further increase visual diversity, we also incorporated
cause the homography to fail, we restrained from annotat-                 several volleyball rallies from SportsMOT [8], for which we
ing points at the extreme limit of the image. The anno-                   added semi-automatically the 2D ball positions. We then
tated frames details are summarized in Tab. S1. For split-                manually annotated some of these combined sequences for
ting matches, we strictly follow the original dataset split-              both sub-trajectory temporal boundaries and collision agent
ting [17].                                                                matching. More precisely, we annotate deflection frames,
                                                                          Player ID (or ’ground’/’net’) and used hands. Table S3 de-
        Split         # Frames     Avg. Points / Frame                    tails the dataset statistics before and after the merging pro-
        Train            923               5.64                           cess, alongside the total number of annotations.
        Validation       350               5.32
        Test             164               4.53                                             Original [17]              Merged (Ours)

Table S1. Court Calibration Dataset. We report the number of               Split    Clips      Frames       Avg.   Clips   Frames    Avg.
annotated frames per split and the average number of visible court         Train    2,152      88,232       41.0   805     69,320      86.1
keypoints annotated per frame.                                             Val      1,341      54,981       41.0   541     43,331      80.1
                                                                           Test     1,337      54,817       41.0   548     43,628      79.6
                                                                           Total    4,830      198,030      41.0   1,894   156,279     82.5
Human Mesh Recovery (WHAM) For 3D human pose
                                                                          Table S2. Trajectory Dataset Merging Statistics. Comparison
and shape estimation, we utilize the WHAM codebase,                       between the original 41-frame video clips from Saad et al. [17]
2D body joints are extracted using the ViTPose-Base                       and our continuous merged rally sequences.
model [39] and are subsequently processed by the official
WHAM [32] model, using the official checkpoint trained
                                                                             The collision agent annotations are distributed among
on the BEDLAM dataset provided by the authors.
                                                                          four categories: Left Hand, Right Hand and Both Hands for
                                                                          Player assignment and Ground or Net. In volleyball, actions
Jump Detection Our jump spotting module relies on                         such as setting naturally involve a symmetrical, two-handed
the PoseConvSpot architecture [3]. We utilize the offi-                   contact (Both Hands). To simplify our heuristic 3D solver
cial model checkpoint trained on the SportsJumpMotion                     without sacrificing physical realism, we explicitly anchor


                                                                     11
  Split   Annotated Clips     Sub-trajectories    Collisions              era feeds, followed by exhaustive manual inspection and
                                                                          per-frame refinement to ensure zero tracking artifacts.
  Train          135                 613               0
  Val             87                 353               0                • 3D Ground-Truth Trajectories: Using our refined
  Test           155                 655              654                 multi-view 2D annotations and static calibrations, we re-
                                                                          constructed metric 3D ball coordinates via robust multi-
  Total          377                1,621             654
                                                                          view triangulation providing a rigorous benchmark for
Table S3. Manual Trajectory and Collision Annotations. Statis-            monocular trajectory lifting.
tics of our custom annotations across the subset of merged rally        • Trajectory Segmentation: For each rally, we localized
sequences.                                                                the exact deflection frames marking physical contacts.
                                                                        • 3D Hand Ground Bounds: At each deflection frame, we
                                                                          annotated the contacting 2D hand position (or ball bounce
                                                                          on the ground) across all four views, tracking the approx-
                                                                          imate vertex location defined in our hand mesh model.
                                                                          Triangulating these points yields the metric 3D “GT Hand
                                                                          Bounds” anchoring each sub-trajectory.
                                                                        • MonoTrack Adaptation: Following MonoTrack [21],
                                                                          we annotated the hitting players’ 2D foot contacts at de-
                                                                          flection instants, projected them onto the court surface via
                                                                          homography, and assigned an empirical 3D contact height
                                                                          of 2.0 m. These positions supervise MonoTrack’s court-
                                                                          bounded optimization alongside its reprojection loss.

                                                                          Dataset    Rallies   Frames per View       Sub-trajectories
Figure S1. Agent Collision Distribution. Frequency of each                VolliQ       10             3066                 101
physical source across our annotated dataset.
                                                                        Table S4. VolliQ 3D Benchmark Statistics. Overview of the syn-
                                                                        chronized four-camera evaluation dataset, reporting the number of
these two-handed contacts to the right hand vertex of the               rallies, duration in frames per viewpoint, total multi-view frame
player’s 3D mesh. This design choice is functionally sound              count, and evaluated sub-trajectories.
because both hands often converge for a two-hands move-
ment (e.g. they form a tight diamond shape during a set),
meaning the spatial offset between the left and right hand is
negligible relative to the ball’s radius and overall trajectory
scale.

A.3. VolliQ Evaluation Dataset
To benchmark our full 3D physics-informed pipeline
against multi-view ground truth, we leverage VolliQ [37],
a synchronized four-camera semi-professional volleyball
dataset. Because the raw data presents temporal offsets and
lacks explicit 3D annotations, we established a rigorous an-
notation protocol:
• Temporal Synchronization:            We manually re-
  synchronized the multi-view streams, correcting minor
  frame-level discrepancies present in the original dataset.
• Multi-View Camera Calibration: Static court and net
  keypoints were annotated across all four views to get in-
  trinsic and extrinsic camera matrices. This calibration
  serves both as the foundation for multi-view triangulation
  and as the reference projection for the MonoTrack [21]
  baseline.
• 2D Ball Tracking: We employed a semi-automatic
  pipeline to detect 2D ball positions across all four cam-


                                                                   12
B. Implementation Details
In this section, we provide the architectural and training de-
tails for each module of our pipeline to ensure full repro-
ducibility.

B.1. Tracking and Human Mesh Recovery
For 2D multi-object detection and tracking, we strictly fol-
low the default configurations of YOLOX [10] and Deep-
EIoU [15], utilizing their official pre-trained weights with-
out any further fine-tuning.
   For 3D human pose and shape recovery, we adopt the
official codebase of WHAM [32]. Following their stan-                 Figure S2. 2D Court Template with Keypoint IDs. Distribution
dard pipeline, we extract 2D body joints using a ViTPose-             of the 65 annotated semantic keypoints defined across the metric
Base model [39] and apply SMPLify for mesh smoothing.                 court space (1800 cm×900 cm). The non-linear distribution along
The WHAM model processes video inputs using the official              the Y -axis increases keypoint density near the foreground to coun-
                                                                      teract broadcast perspective foreshortening.
checkpoint pre-trained on the BEDLAM dataset.

B.2. Jump Spotting                                                    a factor of 10 at two-thirds of the total training epochs via a
                                                                      StepLR scheduler. To handle the class imbalance between
The jump detection module uses the PoseConvSpot [3] ar-               the sparse keypoints and the vast background, we use a
chitecture with its default hyper-parameters. During infer-           weighted Cross-Entropy loss where keypoint pixels are as-
ence, we apply a probability threshold of 0.35 to consider            signed a weight 1, 000 times greater than the background
an event as successfully detected. Furthermore, we apply              pixels.
a bi-causal temporal consistency filtering strategy: a take-
off event is only retained if a corresponding landing event
                                                                      Inference. During inference, after extracting the 2D key-
is detected within a physically plausible temporal window,
                                                                      point coordinates from the predicted heatmaps, we estimate
and vice-versa.
                                                                      the homography matrix using the RANSAC algorithm. We
B.3. Continuous Court Calibration                                     set the maximum number of RANSAC iterations to 2, 000
                                                                      and the reprojection error threshold to 8 pixels.
Because the original implementation of Maglo et al. [23]
is not publicly available, we fully re-implemented their ap-
                                                                      Trajectory Smoothing. Due to independent per-frame
proach and adapted it to volleyball court dimensions.
                                                                      keypoint detections and homography estimates, raw 2D
                                                                      player foot locations projected onto the metric court sur-
Grid Definition. Unlike soccer, which uses 91 keypoints               face can exhibit high-frequency jitter. To ensure smooth
in the original paper, we define a grid of 65 semantic key-           and physically coherent trajectories across time, we apply
points across the volleyball court (yielding 66 classes, in-          a continuous temporal filtering step. First, missing track-
cluding the background), as illustrated in Fig. S2. Follow-           let frames are linearly interpolated. Second, to eliminate
ing their geometric progression logic, the grid divides the           edge transient artifacts, trajectories are padded by repeat-
court length (18 m) into 13 equal segments. Along the court           ing boundary values by 20 frames. Finally, we apply a 5th -
width (9 m), we distribute 5 rows of points using a geo-              order zero-phase low-pass Butterworth filter (fs = 25 Hz)
metric progression (initial step u0 = 150 cm, increment               independently to the projected X and Y spatial coordinates.
r = 50 cm). This allocates a higher density of keypoints              After filtering, the artificial padding is discarded to restore
near the baseline/lower edge of the camera view, where per-           the original sequence length.
spective distortion from the broadcast camera is the most
pronounced.                                                           B.4. 2D Ball Tracking
                                                                      We adopt the TrackNetV3 [6] framework composed of
Training Details. The backbone network is PVTv2 [36],                 TrackNet (detection) and InpaintNet (temporal trajectory
taking standard ImageNet-normalized inputs resized to                 inpainting). Unlike the badminton baseline which concate-
1280 × 720 pixels. Ground-truth heatmaps are generated by             nates a static background frame to the input, we omit back-
drawing constant-value circles with a 3-pixel radius around           ground subtraction because of broadcast volleyball cam-
each visible keypoint. We train the model for 1, 000 epochs           eras continuous movement. Both sub-networks are trained
with a batch size of 8. We optimize the network using                 on the annotations from Perez et al. [26] derived from the
AdamW with an initial learning rate of 10−4 , decayed by              dataset by Saad et al. [17], with a random seed set to 26.


                                                                 13
TrackNet Details. TrackNet is trained for 30 epochs with               frames and a batch size of 64. Optimization is performed
a batch size of 16 and an input temporal window of 8 con-              using Adam with a learning rate of 10−3 and a cosine sched-
secutive frames. We optimize the network using the Adam                uler. The Soft-Focal Loss is defined with a focusing param-
optimizer with a learning rate of 10−3 and no weight de-               eter γ = 2.0 and weighting factor α = 0.25.
cay. We employ Mixup augmentation (α = 0.5) applied                       To improve model robustness, we apply four spatial and
batch-wise across both input frames and target heatmaps (as            temporal augmentations during training:
formulated in the original codebase):
                                                                       • Horizontal Flipping (p = 0.5): The court is mirrored
    x̃ = λx + (1 − λ)xπ ,     ỹ = λy + (1 − λ)yπ ,       (S1)           (X ← 1.0 − X and dX ← −dX).
                                                                       • Spatial Shifting (p = 0.5): A random global shift ∆ ∼
where λ = max(λ′ , 1 − λ′ ) with λ′ ∼ Beta(α, α), and π is               U(−0.08, 0.08) is applied to both X and Y coordinates.
a random batch permutation. During validation and evalu-               • Physical Noise (p = 0.5): Additive Gaussian noise
ation, a predicted ball center is considered a true positive if          N (0, 0.006) is injected independently into the coordi-
its Euclidean distance to the ground truth is strictly within 4          nates.
pixels.                                                                • Temporal Cutout (p = 0.3): 1 or 2 consecutive frames
                                                                         are randomly zero-masked within the input window to
InpaintNet Details. InpaintNet is trained for 400 epochs                 force the network to rely on global trajectory dynamics
with a batch size of 128. It processes input sequences of                rather than overfitting to exact local peaks.
16 consecutive 2D coordinates. During training, we apply a
random masking ratio of 30% (p = 0.3) over the coordinate
sequence to simulate tracking failures and occlusions.
   All remaining architectural parameters follow the origi-            Inference. During inference, the model processes the full
nal TrackNetV3 configuration.                                          rally sequence using a sliding window approach with a re-
                                                                       ceptive field of 17 frames and a strict stride of 3 frames. The
B.5. Sub-trajectory Segmentation                                       frame-wise predictions are aggregated, and peaks exceeding
The trajectory segmentation module relies on a 1D Tem-                 a probability threshold of 0.35 are successfully extracted as
poral Convolutional Network (TCN) to temporally localize               sub-trajectory boundaries.
ball deflection events (e.g., hits, bounces) from the raw 2D
tracking sequence.
                                                                       B.6. Collision Agent Matching
Input Format and Network Architecture Extracted 2D                     To identify the striking player, we evaluate the spatial prox-
ball coordinates are converted into sequences of 4D feature            imity and kinematics of wrist nodes, parameterized with a
vectors containing normalized spatial positions and frame-             Gaussian proximity decay σ = 55 px, proximity weight
to-frame velocities: (X, Y, dX, dY ). Normalization is ap-             β = 0.9, and velocity weight λ = 0.1. The instan-
plied according to the input broadcast resolution.                     taneous wrist velocity Vj,k is computed via finite differ-
    The TCN architecture begins with an initial 1D convo-              ences as the maximum frame-to-frame Euclidean pixel dis-
lution (kernel size 5) projecting the 4-channel input to 128           placement over a temporal window of τ = 1 frame (i.e.,
channels, followed by 1D Batch Normalization, ReLU acti-               [thit − 1, thit + 1]). Both proximity and velocity values are
vation, and Dropout (p = 0.5). The core temporal modeling              independently normalized by their respective maximums
is handled by two residual TCN blocks [19] (kernel size 5).            across all detected athletes in the frame prior to computing
The first block maintains 128 channels with a dilation factor          the composite collision score Sj,k . The athlete maximizing
of 2, while the second expands the feature dimension to 256            this score is selected as the active agent. For contact-type
channels with a dilation factor of 4. Each TCN block con-              attribution, we evaluate the score margin between the des-
tains two dilated convolutional layers with Batch Normal-              ignated athlete’s wrists: if |Sleft − Sright | < 0.05, the impact
ization and ReLU, supplemented by a residual connection.               is classified as Both Hands (associated with setting or over-
Finally, a 1 × 1 convolution collapses the features into a sin-        head passes); otherwise, the higher-scoring wrist is desig-
gle channel, passed through a Sigmoid function to output a             nated as the sole contact source. Finally, ground bounces
frame-wise probability.                                                are detected by computing the proximity of player ankle
                                                                       keypoints with the same Gaussian decay parameter σ; if the
Training Details. Ground truth labels are smoothed into                ratio between the maximum ankle proximity score and the
1D Gaussian distributions (σ = 1.0, bounded by a radius                maximum wrist proximity score across all candidates satis-
of 3 frames) centered on the exact contact frames. We train            fies ≥ 1.0, the event is redirected to a court bounce rather
the network for 60 epochs using an input window size of 17             than a player interaction.


                                                                  14
B.7. Physics-Based Optimization for 3D Trajectory                     vertices (SMPL vertex indices 3447 and 6770) and com-
      Estimation                                                      pute a continuous blending weight using a Softmax func-
                                                                      tion (k = 20) over their local Z-coordinates. This smoothly
To solve the bounded trajectory optimization problem for-
                                                                      assigns a higher spatial weight to the lowest foot, aiming
mulated in Eq. (4) of the main paper, we employ the Nelder-
                                                                      to mitigate step-transition jitter. The entire mesh is then
Mead simplex algorithm with an absolute coordinate pa-
                                                                      translated such that this hybrid reference point matches the
rameter tolerance set to 10−5 .
                                                                      filtered metric court coordinates at Z = 0. For temporal
                                                                      windows classified as aerial jump phases, the trajectory is
Initial Velocity Guess. We initialize the initial velocity            corrected as explained in main paper’s Section 4.
vector v0 = (v0,x , v0,y , v0,z )⊤ using the closed-form bal-
listic solution (neglecting aerodynamic drag). Given the
                                                                      Ball Export. From the continuous 3D ball coordinates
initial 3D contact boundary p0 = (x0 , y0 , z0 )⊤ , the termi-
                                                                      generated by the Ball Lifting module, a reference volley-
nal boundary pT = (xT , yT , zT )⊤ , and the total trajectory
                                                                      ball mesh is automatically translated to these coordinates
duration ∆t = T /fps, the closed-form initial velocity com-
                                                                      and exported synchronously with the player meshes.
ponents are:
                        xT − x 0                                      B.9. Blender Animation
                 v0,x =           ,                      (S2)
                          ∆t                                          Rendering Setup. To generate multi-view visualizations
                        yT − y 0                                      of the reconstructed rallies, we orchestrate a fully auto-
                 v0,y =          ,                       (S3)
                          ∆t                                          mated rendering pipeline using Blender’s EEVEE engine.
                        zT − z0 + 12 g∆t2                             We enable Ground Truth Ambient Occlusion (GTAO) for
                 v0,z =                                  (S4)         volumetric depth, soft shadows, and Screen Space Reflec-
                               ∆t
                                                                      tions (SSR) to simulate the glossy finish of indoor volley-
where g = 9.81 m/s2 denotes gravitational acceleration.               ball courts.

Forward Numerical Integration. Once the optimal ini-                  Scene Customization and Camera Control. Within the
tial launch velocity v̂0 is recovered by minimizing the ob-           3D environment, players are automatically clustered into
jective function, we integrate the full 3D trajectory under           their respective teams based on their spatial coordinates rel-
quadratic aerodynamic drag (adrag = −Cd ∥v∥v) using the               ative to the net, allowing for distinct, customizable material
semi-implicit Euler scheme:                                           assignments for each team and the ball. To better analyze
                                                                      the temporal stability of the 3D reconstruction from novel
             vt+δt = vt + (g − Cd ∥vt ∥vt ) δt,          (S5)         vantage points, a virtual camera is programmatically ani-
            pt+δt = pt + vt+δt δt,                       (S6)         mated to revolve around the court, with an adjustable angu-
                                                                      lar velocity per time step. Furthermore, the pipeline adapts
where δt = 1/fps, g = [0, 0, −9.81]⊤ m/s2 , and Cd =                  to the specific match category: when processing female ral-
ρACdrag
  2m    ≈ 0.035 m−1 denotes the effective drag-to-mass co-            lies (if specified by the user), the net height is automatically
efficient computed using standard volleyball specifications           lowered from the standard men’s regulation height (2.43 m)
(m = 0.27 kg, r = 0.105 m, A = πr2 , ρ = 1.225 kg/m3 ,                to the women’s regulation height (2.24 m).
and Cdrag ≈ 0.45). We confirmed empirically that this Cd
value achieves top-results.                                           C. 2D Ball Tracking Evaluation
B.8. Mesh Export (Players and Ball)                                   We evaluate our 2D ball tracking module against existing
                                                                      small ball tracking methods on the public Volleyball dataset.
To construct the final 3D scene, we translate and export the          Following the standard evaluation protocol, a predicted ball
estimated SMPL vertices and the ball object into per-frame            center is counted as a True Positive if its Euclidean distance
Wavefront .obj files.                                                 to the ground-truth center is within a tolerance threshold of
                                                                      τ = 4 pixels. We report the results of multiple methods on
Player Grounding and Jump Handling. We first project                  the exact same dataset from WASB [33].
the 2D pixel coordinates of the players’ feet onto the met-               We compare the performance of TrackNetV3 (composed
ric court surface via the estimated inverse homography, fol-          of TrackNet alongside InPaintNet) against baseline meth-
lowed by a low-pass Butterworth filter (fc = 1.3 Hz) to               ods. Our implementation achieves a substantial perfor-
eliminate high-frequency projection jitter. To robustly an-           mance improvement, reaching an Accuracy of 94.19% and
chor the 3D SMPL meshes to the court, we introduce a Soft-            an F1-Score of 96.78%, surpassing WASB (80.0% Acc.,
Pitch grounding heuristic. We isolate the left and right foot         88.0% F1) and TrackNetV2 (73.8% Acc., 83.6% F1). This


                                                                 15
  Method                     Accuracy (%) ↑     F1-Score (%) ↑              rather than moving broadcast footage, we do not deploy
            †                                                               our 2D broadcast vision modules directly on these feeds.
  DeepBall                        50.7                64.4
  DeepBall-Large†                 57.5                70.4
                                                                            Instead, to perform a fair evaluation, all methods share
  BallSeg†                        17.5                19.5                  ground-truth trajectory deflection frames. MonoTrack [21]
  TrackNetV2†                     73.8                83.6                  is provided with ground-truth camera calibration and trian-
  ResTrackNetV2†                  74.7                84.2                  gulated 3D foot contacts, optimizing its trajectory via 2D
  MonoTrack†                      75.9                85.1                  reprojection on a single camera view. We benchmarked
                                                                            MonoTrack across all four viewpoints, finding that camera
  WASB† (Step = 3)                77.9                86.5
                                                                            AN02 yielded its best overall 3D RMSE. In contrast, our
  WASB† (Step = 1)                80.0                88.0
                                                                            physics-informed approach operates directly in metric 3D
  TrackNetV3 (Ours)              94.19                96.78                 space using triangulated 3D hand contact boundaries with-
Table S5. 2D Ball Tracking Performance on the Volleyball
                                                                            out any 2D reprojection optimization.
Dataset. Evaluation with a distance threshold τ = 4 px. Methods                 As reported in Tab. S6, MonoTrack minimizes 2D re-
marked with († ) are directly reported from WASB [33]. Track-               projection error exceptionally well on its reference camera
NetV3 integrates both TrackNet and InPaintNet.                              (AN02: 3.89 px). However, this represents a degenerate
                                                                            projective solution: when reprojection is evaluated on the
                                                                            remaining views, the error explodes to 90.6 px on AN01,
high precision and recall (98.28%) ensure dependable 2D                     131.0 px on AN03, and 53.7 px on AN04, resulting in se-
candidate trajectories for the downstream 3D physics lift-                  vere 3D drift (1.55 m 3D RMSE). Conversely, our direct
ing. We found out that the significant performance improve-                 3D physical estimation produces balanced cross-view re-
ment over existing methods is largely due to InPaintNet.                    projections (≈ 17–23 px across all views) and achieves a
                                                                            precise metric fit (0.272 m 3D RMSE), demonstrating that
D. Trajectory Lifting Ablation on VolliQ                                    while single-view 2D reprojection loss can succeed in con-
While Section 6.3 of the main paper quantitatively demon-                   fined sports such as table tennis or badminton, it is flawed
strates the superiority of our physics-informed lifting for-                to resolve depth ambiguity in sports containing rapid aerial
mulation over classical 2D reprojection baselines, we                       ball trajectories such as volleyball.
provide further qualitative comparisons and error anal-                         This phenomenon is further visualized in Fig. S3.
ysis against MonoTrack [21] on the multi-view VolliQ
dataset [37].                                                               E. Step-by-Step Pipeline Modules Visualiza-
                                                                               tion
                     2D Reproj. RMSE (px) ↓ 3D RMSE (m) ↓                   To illustrate the monocular lifting workflow, Fig. S4 pro-
Method               AN01 AN02 AN03 AN04             VolliQ (3D)            vides a step-by-step visual inspection of intermediate out-
MonoTrack [21]        90.6    3.89 131.0 53.7            1.55               puts generated by each module on the representative rally
                                                                            frame presented in the teaser figure of the main paper.
          Theoretical Bounds (Using 3D GT Start/End Points)

Pure Ballistics       26.3    19.2   26.6   29.1         0.380              F. Full Reconstruction Visual Examples
With Drag             24.9    17.9   24.5   26.9         0.293
                                                                            To fully illustrate our pipeline reconstruction results, we
        Our 3D Pipeline (Using Triangulated 3D Hand Bounds)
                                                                            provide extensive reconstruction results along with the cor-
Pure Ballistics  22.4         19.3   23.5   27.6         0.384              responding input broadcast frame in Fig. S5 and Fig. S6.
With Drag (Ours) 19.7         17.2   19.9   23.1         0.272

Table S6. Cross-View Reprojection vs. Metric 3D Accuracy on
VolliQ. MonoTrack [21] optimizes its trajectory via 2D reprojec-
tion on camera AN02 (its best-performing viewpoint among all 4
views) using GT triangulated foot positions and GT camera cali-
bration. Our physics-informed methods operate purely in metric
3D space using 3D boundary constraints. The resulting 3D tra-
jectories are reprojected onto all four views to diagnose projective
overfitting and showcase reprojection methods flaws.



Analysis of Cross-View Reprojection and 3D Overfit-
ting. Because VolliQ features static multi-view cameras


                                                                       16
            (a) 3D Trajectory (rally1)                     (b) 3D Trajectory (rally2)                     (c) 3D Trajectory (rally3)




             (d) 2D Reproj. (rally1)                        (e) 2D Reproj. (rally2)                        (f) 2D Reproj. (rally3)




            (g) 3D Trajectory (rally4)                     (h) 3D Trajectory (rally5)                     (i) 3D Trajectory (rally6)




             (j) 2D Reproj. (rally4)                        (k) 2D Reproj. (rally5)                         (l) 2D Reproj. (rally6)

Figure S3. Qualitative 2D Reprojection and 3D Trajectory Comparisons on VolliQ. Visual comparison between MonoTrack [21] (pur-
ple), our physics-informed lifting formulation with aerodynamic drag (green), and Ground Truth (red) across two distinct rally sequences.




                                                                   17
                                                              (a) Raw Broadcast Frame                                              (b) Player Detection & Tracking




                                                             (c) Court Calibration Overlay                                       (d) WHAM Human Mesh Recovery




                                                  (e) Jump Spotting (Grounded/Aerial)                                                   (f) 2D Ball Detection
                                                               Sub-trajectory Deflection Probability Over Time
                       1.0       Deflection Probability
                                 Threshold (0.35)
                                 Detected Deflection Peaks
                                 Query Frame (256)
                       0.8


                       0.6
         Probability




                       0.4


                       0.2


                       0.0
                             0                    50                 100              150              200       250
                                                                                 Frame Index

                                             (g) Sub-trajectory TCN Deflection Score                                                (h) Collision Agent Matching




                                                       (i) Final 3D Scene Reconstruction                                    (j) Final 3D Scene Reconstruction (Other POV)

Figure S4. Step-by-Step Visualization of Intermediate Pipeline Stages. Visual walkthrough on the teaser rally frame: (a) raw input
feed; (b) 2D bounding boxes and tracklet IDs; (c) homography estimation and projected court grid; (d) SMPL body mesh recovery; (e)
jump event spotting; (f) localized 2D ball position; (g) temporal TCN deflection probabilities across the rally (pink vertical bar indicates
the query frame); (h) heuristic wrist proximity and velocity scoring attributing the collision; (i, j) final 3D scene reconstructed in Blender.

                                                                                                                       18
                        (a) Input Broadcast Frame 1                           (b) Reconstructed 3D Scene 1




                        (c) Input Broadcast Frame 2                           (d) Reconstructed 3D Scene 2




                        (e) Input Broadcast Frame 3                           (f) Reconstructed 3D Scene 3




                        (g) Input Broadcast Frame 4                           (h) Reconstructed 3D Scene 4




                        (i) Input Broadcast Frame 5                           (j) Reconstructed 3D Scene 5

Figure S5. Qualitative 3D Reconstruction Visualizations (Part 1/2). Paired comparisons between monocular broadcast input frames
(left) and the complete metric 3D scene reconstructed in Blender (right).
                                                                    19
                         (a) Input Broadcast Frame 6                             (b) Reconstructed 3D Scene 6




                         (c) Input Broadcast Frame 7                             (d) Reconstructed 3D Scene 7




                         (e) Input Broadcast Frame 8                             (f) Reconstructed 3D Scene 8




                         (g) Input Broadcast Frame 9                             (h) Reconstructed 3D Scene 9




                        (i) Input Broadcast Frame 10                             (j) Reconstructed 3D Scene 10

Figure S6. Qualitative 3D Reconstruction Visualizations (Part 2/2). Additional paired comparisons demonstrating cross-camera stabil-
ity, player grounding, and aerial spike reconstructions from uncalibrated
                                                                     20 monocular broadcast feeds.
