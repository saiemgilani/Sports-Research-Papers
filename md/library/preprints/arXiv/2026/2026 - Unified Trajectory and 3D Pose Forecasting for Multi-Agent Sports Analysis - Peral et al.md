<!-- source: 2026 - Unified Trajectory and 3D Pose Forecasting for Multi-Agent Sports Analysis - Peral et al.pdf -->
<!-- arXiv:2610.30519 · machine conversion (pdftotext -layout), equations/tables/figures not preserved; licence cc-by-nc-nd permits redistribution -->

# Unified Trajectory and 3D Pose Forecasting for Multi-Agent Sports Analysis

**Marc Peral, Guillem Capellera, Luis Ferraz, Antonio Rubio, Stella Graßhof, Dan Witzner Hansen, Antonio Agudo**

arXiv:[2610.30519](https://arxiv.org/abs/2610.30519) · 2026-10-27 ingest · licence: cc-by-nc-nd

## Analysis (N/P/R = 6/4/5 = 15/30)

Kognia-affiliated computer-vision work, tangential to a play-by-play stack but relevant to the broadcast-derived tracking thread already in this collection (Crang et al. concurrent validity, locomotor demands). The most transferable piece is the evaluation correction: overlapping-window sequence construction inflates scores for earlier joint-forecasting methods, so published comparisons are not apples to apples. Uses public WorldPose and 3DPW.

Summary: Joint trajectory + 3D pose forecaster (socio-temporal factorized attention, per-joint loss reweighting, frequency-domain smoothing); state of the art on WorldPose (World Cup broadcast) and 3DPW, and corrects an evaluation bias from overlapping sequences.

---

## Extracted text

```text
                                            Unified Trajectory and 3D Pose Forecasting for Multi-Agent Sports Analysis

                                                            Marc Peral1,2 Guillem Capellera1,2 Luis Ferraz2 Antonio Rubio2
                                                                 Stella Graßhof3 Dan Witzner Hansen3 Antonio Agudo1
                                                                   1
                                                                     Institut de Robòtica i Informàtica Industrial, CSIC-UPC
                                                                2
                                                                  Kognia Sports Intelligence 3 IT University of Copenhagen
arXiv:2610.30519v1 [cs.CV] 21 Oct 2026




                                                                  Abstract

                                         Forecasting future human motion requires jointly reasoning
                                         about an agent’s global trajectory and 3D body pose, which
                                         are tightly coupled, particularly in team sports where mul-
                                         tiple interacting players introduce complex social dynam-
                                         ics. We exploit a socio-temporal encoder that fuses trajec-
                                         tory and pose at the input level and models them jointly
                                         through shared factorized attention. The model is further
                                         enhanced by a per-joint loss reweighting scheme that em-
                                         phasizes dynamic joints and prevents degenerate solutions,
                                         and a frequency-domain trajectory smoothing term that im-
                                         proves trajectory prediction while indirectly benefiting pose
                                         forecasting. To ensure fair comparison with prior joint fore-
                                         casting methods, we identify and correct evaluation biases
                                         arising from overlapping sequence construction, adopting
                                         instead a non-overlapping protocol and a deterministic,
                                         oracle-free strategy for multi-future prediction. Our ap-
                                         proach improves over prior joint forecasting methods on
                                         both WorldPose and 3DPW, with the largest gains on pose
                                         accuracy, demonstrating that the proposed joint formula-
                                         tion generalizes beyond the densely interactive scenarios
                                         that motivate it.


                                         1. Introduction
                                         Anticipating how a person will move and how their body
                                         will be configured a few seconds into the future is a problem    Figure 1. Overview. Prior trajectories and poses are first projected
                                                                                                          independently into a shared latent space. The fused representation
                                         with direct consequences for robotics, autonomous driv-
                                                                                                          is processed by a socio-temporal encoder whose output is fed into
                                         ing, surveillance, and sports analytics. Two largely sepa-       two task-specific heads implemented as independent MLPs.
                                         rate lines of work have addressed pieces of this problem:
                                         one forecasts the trajectory that an agent will follow through
                                         space [4, 9–13, 15, 18, 24, 31, 35, 50], and the other fore-     informs technique and injury risk. Some works have begun
                                         casts how their articulated body will move independently         to forecast pose and trajectory jointly [1, 2, 30], but unfortu-
                                         of where it is [6, 7, 14, 16, 17, 23, 28, 37, 38, 46, 48, 54].   nately, they target settings with at most a couple of interact-
                                         However, in team sports, both quantities matter simultane-       ing people, where the social axis of motion is largely absent.
                                         ously and are far from independent: a player’s path across       Soccer offers a setting where this assumption breaks down
                                         the pitch and the way their limbs move at any instant are two    completely: with twenty-plus players continuously reacting
                                         views of the same underlying action, and practitioners care      to teammates, opponents, and the state of play.
                                         about both, trajectories inform tactical analysis, while pose       This work studies joint trajectory and pose forecast-
ing for interacting groups of players found in real soccer        tion toward the most informative body joints, with target
matches. As depicted in Fig. 1, we adopt a socio-temporal         joints selected based on directly measured per-joint error
transformer encoder, following the coarse-to-fine factorized      under uniform weighting rather than by assumption.
attention design proposed for unimodal trajectory forecast-     • A frequency-based trajectory smoothing term that sup-
ing [10], and apply it to a fused token stream that combines      presses unrealistic high oscillations in the predicted path,
both modalities at the input level, letting a single encoder      improving trajectory accuracy and, as an additional bene-
attend jointly over time and agents at once rather than pre-      fit, the stability of the accompanying pose forecasts.
dicting one and conditioning the other or processing the two    • State-of-the-art on WorldPose [32] and best among com-
streams through separate branches before merging. We fur-         pared methods on 3DPW [52], despite its markedly lower
ther contribute two loss-level improvements, validated with       agent density, demonstrating effectiveness both in the
targeted ablations: a per-joint rebalancing scheme with tar-      large-group setting it targets and beyond.
get joints selected via empirical per-joint error measure-
ment, and a frequency-domain trajectory smoothing term          2. Related Work
that indirectly stabilizes pose forecasts as well.
                                                                Forecasting how people move and how their bodies articu-
    Another aspect of this work concerns how we evalu-
                                                                late over time has been studied from several separate angles:
ate the results against existing methods. The most suitable
                                                                predicting the global trajectory of one or several agents, pre-
datasets for this task, WorldPose [32] and 3DPW [52], must
                                                                dicting the temporal evolution of an articulated skeleton,
be cut into short, fixed-length sequences before training and
                                                                and more recently predicting both jointly. We review each
evaluation. We find that the specific protocol used by the
                                                                direction below, paying particular attention to which set-
most recent methods with public implementations tackling
                                                                tings, datasets, and forecasting horizons each line of work
this same joint task, T2P [30] and SimpliHumon [2], ex-
                                                                targets, since these choices determine which methods con-
tract sequences with a stride of a single frame, introduc-
                                                                stitute a meaningful point of comparison for the soccer set-
ing avoidable biases: near-identical sequences are counted
                                                                ting addressed in this paper.
many times over, and longer source videos receive dispro-
                                                                Trajectory Forecasting has been extensively studied in dif-
portionate weight in the reported average simply by virtue
                                                                ferent types of agents moving through shared spaces [4, 15,
of their length. When re-evaluating these two methods for
                                                                24, 31, 35], with graph- and attention-based architectures
direct comparison, we instead construct sequences with a
                                                                now the dominant paradigm for modeling interactions be-
non-overlapping protocol, and additionally adopt a deter-
                                                                tween agents sharing a scene [5, 42, 45, 56]. Within sports
ministic single-future evaluation that does not require ora-
                                                                specifically, trajectory forecasting has been explored for
cle access to the ground truth at inference time, unlike the
                                                                American football [12, 50], basketball [11, 12, 18, 50], and
best-of-many selection used in their original papers.
                                                                soccer [10, 11, 25], taking advantage of the structured and
    We evaluate our approach on WorldPose [32], real broad-     rule-governed nature of team play to constrain the space of
cast footage from the 2022 FIFA World Cup featuring             plausible futures. However, none of these methods forecast
large groups of simultaneously interacting players, and on      body pose alongside trajectory as we do in this work.
3DPW [52], a general-purpose benchmark in which each            Human Pose Forecasting. A separate body of work fore-
sequence contains at most two people. WorldPose [32] is         casts the future articulation of a skeleton without reason-
the setting our socio-temporal design is most directly aimed    ing about its position in the world. Early approaches re-
at, and our model substantially improves over competing         lied on recurrent architectures [7, 16, 28, 54], later replaced
approaches across the majority of metrics. Notably, despite     by feed-forward graph- and transformer-based models that
3DPW [52] offering little of the social context our architec-   predict an entire future sequence directly and avoid autore-
ture is built to exploit, our model also matches or exceeds     gressive error accumulation [23, 37, 38, 48], as well as
both baselines on this benchmark, indicating that the gains     diffusion-based models that generate multiple plausible fu-
reported in this work do not depend on a densely populated      tures [6, 14, 17, 46]. A parallel line of work operates in
scene and that the underlying joint formulation generalizes     the frequency domain via the discrete cosine transform, de-
well beyond the team-sport setting that motivated it.           composing pose sequences into a small set of low-frequency
    The main contributions of this work are as follows:         components that capture smooth, periodic motion patterns
• A socio-temporal encoder that fuses trajectory and 3D         particularly well [19, 41, 44, 53].
   pose at the input level and processes them jointly through       Most of these methods, including representative recent
   shared factorized attention, at the scale of a full soccer   examples like MotionMixer [7] and BeLFusion [6], are for-
   scene, with a controlled comparison of fusion topologies     mulated for a single person and report results on bench-
   confirming that input-level fusion outperforms sequential    marks like Human3.6M [29] or AMASS [36], where no
   and late alternatives under a matched backbone.              inter-person interaction is modeled, typically over forecast-
• A per-joint loss rebalancing scheme that directs optimiza-    ing horizons of one second or less. Extensions to multi-
person settings instead design attention mechanisms that         on PoseTrack [3] and 3DPW [52] over a short forecast
operate jointly over agents and joints [49, 51], or combine      horizon of 900ms. Unfortunately, at the time of writing,
local per-person encoders with a global scene representa-        no official implementation has been released, which pre-
tion [53]. These models, however, are trained on substan-        cludes a direct experimental comparison. We instead com-
tially larger pose corpora than either of our target bench-      pare against T2P [30] and SimpliHumon [2], which, unlike
marks provides: [53], for instance, trains exclusively on        the methods discussed above, are trained directly on our
CMU-Mocap [33] before testing zero-shot on 3DPW [52]             target benchmarks without relying on larger external pre-
and MuPoTS-3D [39]. More importantly, none of these              training datasets, support forecasting horizons beyond one
multi-person methods output a global trajectory, so pre-         second, and tackle the same pair of tasks, pose and trajec-
dictions remain root-relative and the agent’s position in        tory forecasting, that we address. These properties make
the scene is never recovered. EqMotion [55] applies the          them the most directly comparable existing methods, and
same multi-agent reasoning machinery to both tasks, treat-       we adopt them as our primary baselines. However, we iden-
ing joints as interacting agents to forecast pose and pedes-     tify a methodological issue in how both construct sequences
trians as interacting agents to forecast trajectory. The issue   from 3DPW [52]: their official protocols use a stride of a
is that it evaluates the two as separate scenarios rather than   single frame across all splits, a choice we revisit and mod-
predicting, for the same set of people, how their bodies ar-     ify due to it introducing biases, and we propose instead a
ticulate and where they move at once, which is the setting       non-overlapping protocol. Our approach departs from the
we address here.                                                 methods discussed in this section by fusing trajectory and
Joint Pose and Trajectory Forecasting. A smaller body            pose at the input level and processing them through a shared
of work forecasts pose and trajectory together, motivated        socio-temporal encoder, without imposing a sequential or
by the observation that a person’s global movement and           branch-separated coupling between the two modalities.
the articulation of their limbs are tightly coupled, a run-
ner’s stride pattern is inseparable from their forward mo-       3. Methodology
tion, and a model that treats the two as independent dis-
cards information relevant to both. On that same premise, a      3.1. Problem Statement
complementary line of research treats body pose as an aux-       Given a set of N ∈ N agents observed over T frames, each
iliary input that sharpens future trajectory forecasting [20–    described by motion and body pose features, our goal is
22, 27, 43, 47]. Social-Transmotion [47] fuses pose-             to use the first t < T observations to predict the remain-
keypoint tokens with trajectory tokens at the input of a         ing frames, i.e., from t + 1 to T . For each observed time
shared social transformer, using masking to remain robust        step, the model receives two input streams: player trajec-
to unavailable modalities. Nonetheless, the method fore-         tories xt ∈ RN ×2 , given as 2D positions in global pitch
casts only trajectories. Multi-Transmotion [20] extends this     coordinates [26], and 3D body poses pt ∈ RN ×J×3 , where
into a large multimodal pre-trained model that also emits        J denotes the number of joints. Poses are represented as
3D pose keypoints. However, it forecasts the future motion       joint-wise offsets relative to a root joint fixed at the ori-
of a single ego agent while treating the remaining agents        gin, which isolates articulated motion from global position;
purely as social context, being trajectory and pose capabil-     the trajectory stream separately captures this positional in-
ities pre-trained on seven merged datasets and evaluated on      formation, making the two modalities complementary by
disjoint benchmarks, never providing the joint evaluation on     construction. The model operates under a strictly causal
a common testbench.                                              setting, relying exclusively on past observations to forecast
    Early architectures shared representations across the two    future ones, with no access to future context at inference
tasks through multi-branch designs [1, 8, 57], while later       time. Predicted trajectories and poses are expressed in the
work explored sequential pipelines in which a trajectory is      same coordinate systems as their respective inputs, ensuring
forecast first and used to condition pose generation [30, 40].   consistency between observation and prediction spaces.
More recent sequence-based methods operate directly on
structured pose inputs, separating and later fusing local and    3.2. Multi-Modal Input Encoding
global representations [58] or introducing learnable query       Soccer scenes contain a variable number of visible play-
tokens to represent candidate future motion states [2], with     ers due to occlusions and incomplete tracking. Instead of
both lines of work focused primarily on improving temporal       propagating attention masks throughout the encoder, we pad
reasoning within pose-centric representations.                   missing agent slots with a fixed out-of-range sentinel value
    Among methods that jointly forecast pose and trajectory      (e.g., −2000), which cannot overlap with valid normalized
for multiple interacting people, TRiPOD [1] is closely re-       trajectory or pose values. This architecture-agnostic strat-
lated to our setting, modeling human-human and human-            egy allows the model to process up to N agents without
object interactions through graph attention and evaluating       conditional logic. In practice, attention weights assigned
to padded slots converge close to zero, indicating that the       3.5. Loss
model implicitly learns to ignore absent agents. As shown         The model is trained end-to-end using a composite loss that
in Fig. 1, trajectory and pose inputs are first projected inde-
                                                                  jointly supervises trajectory and pose forecasting, together
pendently into a shared latent space of dimension d, produc-
                                                                  with a smoothness term applied to the predicted trajectory.
ing two t × N × d representations. These are concatenated,
                                                                  The forecasting terms are computed over every frame, in-
yielding a t × N × 2d tensor, and fused through a small           cluding the observed ones, training the model in a sequence-
MLP that compresses the representation back to d dimen-           to-sequence manner. Supervising the reconstruction of ob-
sions. This early fusion enables cross-modal interactions         served frames alongside future prediction regularizes the
from the first encoder layers while maintaining a consistent
                                                                  temporal dynamics learned by the encoder and encourages
embedding size, jointly encoding each agent’s position and
                                                                  consistent representations across the observation-prediction
body configuration at every timestep.
                                                                  boundary. The total loss is written as:
3.3. Socio-Temporal Encoder                                                  \mathcal {L}_\text {total} = \mathcal {L}_\text {traj} + \lambda _\text {pose} \mathcal {L}_\text {pose} + \lambda _\text {smooth} \mathcal {L}_\text {smooth}, \label {eq:loss}        (1)
To process the fused multimodal representation, we
                                                                  where λpose and λsmooth control the relative contribution of
adopt the coarse-to-fine socio-temporal encoder introduced
                                                                  each term. We set λpose = λsmooth = 10 throughout our
in [10] for trajectory forecasting, which we extend here to
                                                                  experiments. Each term is detailed below.
operate over our joint trajectory-pose tokens. The encoder
                                                                  Trajectory Loss. The trajectory term penalizes the mean
consists of two sequentially stacked stages, a coarse and
                                                                  Euclidean distance between predicted and ground-truth
a fine one, that share the same internal structure but act
                                                                  pitch positions across all agents and frames:
on progressively refined representations: the first builds a
global picture of the scene, while the second resolves finer-
grained dependencies on top of it (see Fig. 1). Before the                              \mathcal {L}_\text {traj} = \frac {1}{NT} \sum _{n=1}^N \sum _{t=1}^T \left \| \boldsymbol {\hat {x}}_{n,t} - \boldsymbol {x}_{n,t} \right \|_2 , \label {eq:losstraj}       (2)
first stage, a temporal positional encoding is added to the
token sequence to preserve frame ordering, while no posi-         where x̂n,t and xn,t are the predicted and ground-truth po-
tional encoding is applied along the agent dimension, which       sitions of player n at frame t, respectively.
enforces permutation equivariance with respect to player or-      Pose Loss. The pose term supervises the predicted root-
dering and lets the model generalize across different team        relative joint coordinates across all agents, frames, and
compositions. In our work each stage is composed of three         joints. For each j-th joint of player n at frame t, we first
Set Attention Blocks (SAB) [10, 34] arranged as two tem-          compute an absolute error as ϵn,t,j = |p̂xn,t,j − pxn,t,j | +
poral blocks, SABT , followed by one social block, SABS .         |p̂yn,t,j −pyn,t,j |+|p̂zn,t,j −pzn,t,j |, where p̂n,t,j and pn,t,j de-
Each SABT attends independently over the time dimension           note the predicted and ground-truth 3D coordinates, respec-
for a given agent, aggregating its individual motion history,     tively. We then take the l2 norm over the full set of joints,
while the subsequent SABS attends across all agents within        which acts as a regularizer that heavily penalizes large lo-
a single frame, capturing inter-player interactions and col-      calized errors, such as those arising from rapid limb move-
lective team behavior. We adopt this factorized design as         ments, that would otherwise be concealed by the accurate
an efficient and already validated way of scaling attention       prediction of more stable joints. A small subset of distal
to the large number of simultaneously interacting agents          joints, namely the elbows, wrists, ankles, and feet, exhibit
present in a soccer scene, and our contribution lies not in       a markedly higher error than the rest of the skeleton under
this backbone itself but in fusing trajectory and pose into a     uniform loss weighting, since their displacement in root-
shared token stream that this encoder then processes jointly.     relative coordinates is substantially larger and harder to pre-
                                                                  dict than that of proximal joints such as the hips or torso.
3.4. Prediction Heads
                                                                  Guided directly by that, we introduce a per-joint weight
The output of the fine encoder is passed to two task-specific     vector w ∈ RJ that up-weights precisely this set of high-
prediction heads, each implemented as an independent MLP          error distal joints, preventing them from being dominated in
operating on the shared spatio-temporal representation. The       the loss by the larger number of easier, low-error proximal
trajectory head maps the encoder output to a tensor of shape      joints, and explicitly encouraging the model to learn their
T × N × 2, the predicted 2D pitch-space position of each          fine-grained articulation. The pose loss is then written as:
agent at each timestep, while the pose head maps the same
representation to a tensor of shape T ×N ×3J, the predicted
                                                                                            \mathcal {L}_\text {pose} = \frac {1}{NT} \sum _{n=1}^N \sum _{t=1}^T \left \| \boldsymbol {w} \odot \boldsymbol {\epsilon }_{n,t} \right \|_2 , \label {eq:losspose}    (3)
3D root-relative joint coordinates for each player. In both
cases, only the forecast frames, from t + 1 to T , are retained
as the final output, discarding the reconstructions produced      where ϵn,t = (ϵn,t,1 , . . . , ϵn,t,J ) ∈ RJ collects the per-joint
for the observed frames at inference time.                        errors, and ⊙ denotes an element-wise product. This design
discourages degenerate solutions in which the model col-                                                                                                                               recordings into disjoint 3-second windows for training and
lapses toward static average poses, instead incentivizing the                                                                                                                          evaluation, without temporal overlap between extracted se-
learning of the high-intensity, fine-grained motion patterns                                                                                                                           quences. Unlike the original benchmark protocol, where
essential to realistic soccer dynamics. The relative strength                                                                                                                          train, validation, and test sequences can be drawn from the
of this rebalancing is controlled by a single scalar applied                                                                                                                           same match, we enforce a match-level split so that no eval-
to the weights of the selected joints, found empirically.                                                                                                                              uation sequence shares a video source with any training se-
Trajectory Smoothing Loss. Agent positions predicted                                                                                                                                   quence, removing incidental cues that would otherwise leak
independently at each frame can exhibit unrealistic high-                                                                                                                              across splits and give an overly optimistic picture of gen-
frequency oscillations, or zigzagging, between consecutive                                                                                                                             eralization to unseen games. We use the Morocco-Portugal
timesteps, even when their average displacement error is                                                                                                                               as validation, Netherlands-Argentina as test, and the other
low. To discourage this behavior, we introduce a smooth-                                                                                                                               6 games for training. On the other hand, 3DPW [52] is
ness term that penalizes high-frequency content in the pre-                                                                                                                            captured with a moving camera across diverse indoor and
dicted trajectory directly in the frequency domain, so that                                                                                                                            outdoor scenarios and typically involves at most two peo-
any systematic oscillation occurring anywhere within the                                                                                                                               ple per clip. The recordings are provided at 30 fps, so, to
forecasting horizon is captured, rather than only oscilla-                                                                                                                             match the 3-second duration used for WorldPose [32], we
tions between immediately adjacent frames. For each agent,                                                                                                                             extract sequences of 90 consecutive frames, and we keep
we take the real-valued fast Fourier transform of its pre-                                                                                                                             the per-video split of the original benchmark.
dicted trajectory over the Tpred forecast frames indepen-                                                                                                                                  Both datasets have served prior work on many pose-
dently along each coordinate axis, obtaining a complex                                                                                                                                 related tasks, but for the specific problem of forecasting
spectrum with F = ⌊Tpred /2⌋ + 1 frequency bins. We                                                                                                                                    future trajectory and pose, the protocol used by methods
then compute the power spectrum as the squared magnitude                                                                                                                               tackling it [2, 30] slides the extraction window forward
of each frequency coefficient and weight it by the square                                                                                                                              one frame at a time. Under this unit stride, adjacent win-
of its normalized frequency, so that the static component                                                                                                                              dows overlap almost completely, so each stretch of motion
receives zero weight and the highest representable Nyquist                                                                                                                             is scored many times, appearing both as a forecast target
frequency receives the maximum weight of one as:                                                                                                                                       and as observed context for numerous neighboring win-
                                                                                                                                                                                       dows. Longer recordings also yield proportionally more
          \mathcal {L}_\text {smooth} = \frac {1}{N F C} \sum _{n=1}^{N} \sum _{k=0}^{F-1} \sum _{c=1}^{C} f_k^2 \left | \hat {q}_{n,k,c} \right |^2 , \label {eq:losssmooth}    (4)   windows than shorter ones. Together, these effects let a
                                                                                                                                                                                       small number of recurring motions and the longest record-
                                                                                                                                                                                       ings dominate the reported average rather than the metric
where C = 2 is the number of spatial coordinates, q̂n,k,c is                                                                                                                           reflecting an even sample over the dataset’s diversity. For
the k-th Fourier coefficient of the c-th coordinate of agent                                                                                                                           both datasets we extract windows with a non-overlapping
n’s predicted trajectory, and fk = k/(F − 1) ∈ [0, 1] is                                                                                                                               stride, partitioning each split’s frames into disjoint, equal-
the normalized frequency of bin k. By penalizing high-                                                                                                                                 length sequences so that every frame contributes to exactly
frequency energy, this term suppresses zigzagging and other                                                                                                                            one, and discarding any trailing remainder shorter than a
trajectory artifacts while largely preserving physically plau-                                                                                                                         full window. Each sequence provides one second of ob-
sible motion. Moreover, it consistently improves pose fore-                                                                                                                            served context and is evaluated on the following two sec-
casting by providing a steadier trajectory context.                                                                                                                                    onds, the configuration used in all experiments.

4. Experimental Results                                                                                                                                                                Metrics and implementation details. We report five com-
                                                                                                                                                                                       plementary metrics, two per modality and a shared one,
We now present both quantitative and qualitative results in                                                                                                                            all in mm. For trajectories, Average Displacement Er-
terms of human pose and trajectory prediction. First, we                                                                                                                               ror (ADE) is the mean Euclidean distance between pre-
describe the datasets, evaluation protocol, metrics and im-                                                                                                                            dicted and ground-truth 2D root positions over all forecast
plementation details, followed by a series of ablation studies                                                                                                                         frames, while Final Displacement Error (FDE) measures the
assessing the contribution of each block. Finally, we com-                                                                                                                             same error only at the final frame, capturing end-of-horizon
pare our method with respect to two recent methods.                                                                                                                                    drift. For pose, Aligned mean per joint Pose Error (APE)
                                                                                                                                                                                       is the mean Euclidean joint error after expressing predic-
4.1. Datasets, Metrics and Implementation details                                                                                                                                      tions and ground truth in the root-joint coordinate system,
We evaluate our approach on two datasets: WorldPose [32]                                                                                                                               averaged over joints and frames, thus isolating articulation
and 3DPW [52]. On one side, WorldPose [32] provides                                                                                                                                    from global positioning. Procrustes-aligned mean per joint
precise 3D pose annotations from broadcast footage of the                                                                                                                              Pose Error (PPE) is computed analogously after full Pro-
2022 FIFA World Cup, spanning roughly 50 minutes of play                                                                                                                               crustes alignment, including rotation and scaling. Finally,
across multiple matches and venues, with every player vis-                                                                                                                             to score the joint task directly, we report the mean per-joint
ible on the pitch annotated simultaneously. We segment the                                                                                                                             error in world coordinates (JPE). We place each predicted
root-relative pose at the predicted pitch position, assuming        Input Modalities     APE ↓   PPE ↓     Input Modalities    ADE ↓   FDE ↓
                                                                       Pose only         123.0    90.7      Trajectory only    901.7   1901.5
the vertical coordinate as the trajectory head predicts only        Pose + Trajectory    121.8    88.9     Trajectory + Pose   704.1   1681.4
2D positions, and measure the mean Euclidean distance to
                                                                   Table 1. Effect of trajectory and pose as an auxiliary input on
the ground-truth joints in the global frame, averaged over
                                                                   pose/trajectory-only forecasting, evaluated on WorldPose [32].
all joints and forecast frames. Unlike ADE/FDE (which
                                                                   The model is trained to predict poses (left) / trajectories (right)
see only the root) and APE/PPE (which are root-relative            exclusively; only the input modalities are varied.
or Procrustes-aligned), JPE is invariant to neither modal-
ity and so reflects the coupled accuracy of trajectory and            Fusion            Params   ADE ↓    FDE ↓    JPE ↓       APE ↓   PPE ↓
pose together. Nevertheless, being an absolute world-frame           Sequential          2.58M   1074.6   2186.7   1131.9      116.3    85.3
                                                                     Cross Att           1.45M   951.4    1962.8   1012.7      115.1    84.1
distance, it is numerically dominated by the global-position        Late Halved          0.74M   850.9    1875.2    907.3      115.2    84.4
term. Our model is trained end-to-end for 100 epochs on                 Late             2.58M   810.7    1804.9    863.6      114.8    84.2
a single NVIDIA A40 GPU, using the AdamW optimizer                   Early Sum           1.31M   681.2    1663.4    736.8      113.0    83.9
                                                                    Early Concat         1.32M   670.8    1642.0    723.5      112.6    83.7
with a learning rate of 10−3 and ϵ = 10−4 , a batch size of
32, embedding dimension of d = 128, and gradient norm              Table 2. Fusion topology on WorldPose. All lines share back-
clipping at 5.                                                     bone, losses, protocol and training recipe, only the fusion point
                                                                   changes. Rebalancing/smoothing are disabled to isolate fusion.
4.2. Ablation Studies
Effect of Cross-Modal Inputs. We first isolate how much            tory first and conditions pose on it; a cross-attention block
each input modality contributes to the other’s forecasting         in which pose and trajectory tokens attend to one another
task, by training single-task variants of our model that pre-      before the encoders; two-branch late fusion, in which each
dict only trajectories or only poses, and feeding them ei-         modality is processed by its own encoders and merged only
ther their own matching modality alone or both modalities          before the output heads, at full width and at halved width to
jointly. Table 1 reports the pose/trajectory-only setting, re-     contrast the parameter budget; input-level fusion of the two
spectively. When predicting poses alone (left part in the          modalities into a single per-agent, per-frame token, either
table), supplying trajectory as an additional input improves       by element-wise sum or by concatenation followed by an
both pose metrics, even though no trajectory is being fore-        MLP (ours). Input-level fusion is clearly strongest, and the
cast in this configuration. This confirms that knowing where       separation between designs is concentrated in the trajectory-
a player is heading on the pitch is informative for anticipat-     coupled metrics while the root-relative pose metrics stay
ing how their body will be configured. However, the effect         nearly flat. The sequential prior is weakest by a wide mar-
is considerably larger when predicting trajectories alone:         gin, consistent with the cross-modal analysis in Table 1
adding pose as an input substantially reduces both ADE and         where pose→trajectory is the stronger direction, confirming
FDE, indicating that the articulation of a player’s limbs car-     that forecasting trajectories without access to pose modal-
ries strong cues about their imminent movement, such as the        ity is unfavorable. Finally, halved late fusion trails full late
pattern of an accelerating run, which a model can exploit to       fusion, while early concatenation surpasses it with roughly
forecast position more accurately. Beyond the benefit of           half the parameters, pointing to a topological rather than ca-
richer inputs, we also find that training the two tasks jointly,   pacity advantage. Concatenation slightly outperforms sum-
rather than training single-task variants, as in this ablation,    mation, so we use it throughout.
gives a further improvement over either single-task model.         Joint Balancing. We next study the effect of the joint
This is especially pronounced for pose forecasting: once           rebalancing weight (see Section 3.5), which consistently
the model is also tasked with predicting future trajectories,      up-weights the same set of high-motion joints previously
the representations it must learn to do so reflect a coherent      selected based on their measured error, varying only the
notion of where the player is going, and this improved tra-        strength of this rebalancing. Table 3-top reports trajec-
jectory context in turn sharpens pose forecasts beyond what        tory and pose metrics as the strength increases, with tra-
is achieved by simply observing trajectory as a static input.      jectory smoothing disabled throughout so that its effect is
The joint formulation used throughout the rest of this paper       isolated from the smoothing term studied next. By steering
therefore benefits from both the cross-modal input signal          the loss toward the most dynamic joints, this rebalancing
studied here and the additional supervision that comes from        helps the model escape the local minimum of predicting a
forecasting both modalities at once.                               near-static skeleton, a degenerate solution into which a uni-
Fusion Topology. Before studying our loss terms, we first          formly weighted loss can otherwise settle since low-motion
establish where the two modalities should be combined,             joints dominate the average error. Increasing the rebalanc-
holding the backbone, losses, protocol and training recipe         ing factor steadily improves pose metrics, confirming that
fixed and varying only the fusion point. Table 2 compares          directing more of the loss toward the most dynamic joints
five alternatives: a sequential design that forecasts trajec-      sharpens articulation. This comes at a cost to trajectory ac-
  Joints   Smoothing   ADE ↓   FDE ↓    JPE ↓   APE ↓    PPE ↓       4.3. Quantitative Results
     0        %        670.8   1642.0   723.5   112.6     83.7
   2.5        %        676.3   1651.1   720.2   105.9     81.4       We compare against two recent multi-person pose and
     5        %        683.3   1667.2   719.8   101.3     79.1       trajectory forecasting methods, T2P [30] and SimpliHu-
   7.5        %        714.6   1694.0   745.6    99.8     78.7       MoN [2], alongside a simple non-learned baseline. Both
    10        %        848.5   1832.5   874.7    98.7     78.5       methods report results on 3DPW [52] under the unit-stride
     0        !        611.7   1528.1   659.1   106.7     82.6       sequence construction discussed above. To make a fair
     5        !        623.0   1549.1   647.3    95.2     77.7       comparison, we instead re-run their official implementa-
Table 3. Ablation studies evaluated on WorldPose [32]. Joint re-     tions under our non-overlapping protocol and consistent
balancing factor in the top rows show that larger factors steadily   1s/2s observation-forecast split, on both WorldPose [32]
improve pose accuracy at the expense of trajectory accuracy. Tra-    and 3DPW [52]. T2P [30] and SimpliHumon [2] can sam-
jectory smoothing enabled for the last two rows improves trajec-     ple several plausible continuations per sequence: their orig-
tory accuracy directly, and pose accuracy indirectly, by removing    inal evaluation protocol retains the candidate closest to the
unrealistic high-frequency jitter in the predictions                 ground truth, which requires access to the future itself and
                                                                     is not realizable at deployment time. Since our goal is a
curacy, which degrades as the factor grows, since the tra-           deterministic, directly usable forecasting model we report
jectory term receives comparatively less effective weight as         these baselines under two settings that do not require ora-
optimization is increasingly steered toward pose. We select          cle selection: drawing a single future, and drawing multi-
a factor of 5 for the rest of our experiments, as it lies close      ple futures from which we select, without any access to the
to the point where further pose gains begin to come at a             ground truth, the one closest to their average, that is, the
disproportionate cost to trajectory accuracy. JPE, which ag-         most representative or central sample, and report its error
gregates both terms, happens to be minimized at this same            against the ground truth. We sample six futures in this set-
factor (with and without smoothing), rising for larger fac-          ting, matching the number of futures used in the original
tors as the growing trajectory error dominates the sum. We           source of both methods. Both settings reflect a selection
report this only as a consistency check rather than as the           strategy that would actually be available at inference time,
basis for the choice, since JPE is dominated by the global           in contrast to the best-of-many oracle selection used in the
position term and is correspondingly insensitive to the local        original evaluation protocol of these methods.
articulation that the rebalancing is meant to improve.                   We additionally report a non-parametric static baseline
Trajectory Smoothing. We then evaluate the frequency-                that holds the last observed pose fixed for every future
domain smoothing term (see Section 3.5), which penal-                frame, re-centering it at each timestep so that its root joint
izes high-frequency components of the predicted trajec-              matches the ground-truth root trajectory at that frame, since
tory to discourage unrealistic wiggling between consecu-             this baseline performs no trajectory prediction of its own.
tive frames. Last rows of Table 3 show models trained with           This isolates how much of the apparent forecasting diffi-
this term, to be compared with their analogs with the same           culty is solved trivially by assuming no further articulation,
joints balancing factor without smoothing in the top rows.           and gives a lower bound of difficulty against which learned
Enabling smoothing improves trajectory accuracy in both              methods should be judged. Our model used for comparison
cases, as expected given its direct effect on the trajectory         in this section incorporates the joint rebalancing factor and
loss. Notably, it also yields a consistent improvement in            trajectory smoothing term selected in Section 4.2. Table 4
both pose metrics: by discouraging zigzagging trajectory             reports the comparison across both datasets. On World-
predictions, the model produces a more physically coherent           Pose [32], our model remains competitive with T2P [30]
notion of where each player is heading, and this steadier tra-       on ADE and JPE while improving all other metrics, with
jectory context translates into more stable and realistic pose       a clear pose-metric margin over both benchmarks and the
forecasts, reinforcing the cross-modal dependency already            static reference. Unlike competing methods, whose tra-
observed in Table 1. Figure 2 left and central crops illus-          jectories increasingly drift from ground truth with hori-
trate this effect qualitatively. Without the smoothing term          zon, ours remain comparatively stable, yielding a smaller
(left), predicted trajectories exhibit visible jitter from frame     ADE–FDE gap. JPE closely follows global-position error,
to frame, deviating back and forth around the underlying             and T2P [30] retains a slight edge, mirroring its narrow
path rather than tracing it cleanly. With smoothing enabled          ADE advantage, while its larger pose errors are masked by
(central), the same trajectories become clearly steadier. This       JPE’s position-dominated scale. We therefore interpret JPE
added regularity is not merely cosmetic: by removing the             alongside the marginal metrics, which disentangle global
spurious oscillation, the predicted path is also better at fol-      localization from articulation. On 3DPW [52], despite the
lowing the true curvature of the trajectory, since a smoother        scene containing at most two agents and therefore offering
forecast can commit to a consistent direction of turning in-         little social context, our model still achieves the best re-
stead of having that signal masked by frame-to-frame noise.          sult on every metric. We also note that the static baseline
Figure 2. Effect of trajectory smoothing on predicted player paths. Left and central part: In each crop, the solid opaque line shows
the observed prior trajectory, the solid semi-transparent line shows the ground-truth future trajectory, and the dashed opaque line shows the
predicted path. Left and central representations are without and with the smoothing term enabled, respectively. Right part: Qualitative
pose forecasting on WorldPose [32] test set. Ground-truth poses are shown in blue and predicted poses in red. Each row shows a single
player action at five temporally equidistant frames within the 2-second forecasting horizon. Best viewed with zooming.
                                                     WorldPose [32]                                      3DPW [52]
           Method           Futures
                                       ADE ↓     FDE ↓ JPE ↓ APE ↓            PPE ↓     ADE ↓     FDE ↓ JPE ↓ APE ↓            PPE ↓
        StaticBaseline         –         –         –       –      169.8       124.3       –          –       –     108.5        79.5
      SimpliHuMoN [2]          1       757.0     1920.3 803.4     157.3       109.2     613.0     1155.5 693.4     191.6       139.4
      SimpliHuMoN [2]          6       763.0     1988.3 804.4     149.8       106.7     615.6     1161.5 702.2     202.2       174.8
           T2P [30]            1       584.6     1668.0 631.6     142.2        94.4     636.8     1156.9 667.5     109.7        80.5
           T2P [30]            6       564.1     1625.4 613.0     142.1        94.1     650.1     1165.5 682.4     109.1        80.2
             Ours              1       623.0     1549.1 647.3      95.2        77.7     551.2      763.8   580.7   101.2        76.2
Table 4. Quantitative comparison against T2P [30], SimpliHuMoN [2], and a static baseline on WorldPose [32] and 3DPW [52],
with 1 second of observed context and a 2 second forecasting horizon. Futures denotes the number of sampled continuations used at
inference for generative baselines, averaged when greater than one. Our model achieves competitive results on WorldPose [32] and, despite
the limited social context available, the best results on 3DPW [52].

lands remarkably close to the best solutions on this dataset,            ways with crossing legs, an unusual gait pattern that is likely
in contrast with the larger gap between them observed on                 underrepresented in the training data and that we consider
WorldPose [32]. This is consistent with the nature of the                a feasible source of model limitations. Even there the re-
two datasets: WorldPose [32] sequences are drawn from                    sulting prediction remains reasonable, suggesting that the
high-intensity match play where players are rarely station-              model degrades gracefully even on motion patterns it has
ary for long, so freezing the last pose is a poor predictor              seen comparatively rarely.
of the future, whereas 3DPW [52] contains a broader mix
of everyday, lower-intensity, and often near-static activities,          5. Conclusion
where holding the last observed pose is frequently a reason-
able approximation of what comes next, leaving compara-                  We presented a unified approach for joint trajectory and 3D
tively little room for a learned model to improve upon it.               pose forecasting in real soccer matches, fusing both modal-
                                                                         ities at the input through a shared socio-temporal encoder
4.4. Qualitative Evaluation                                              that learns their interaction directly. Per-joint loss reweight-
We further inspect our pose forecasts in Fig. 2-right, show-             ing and frequency-domain trajectory smoothing further im-
ing four sequences at five equidistant frames across the 2-              prove pose and trajectory accuracy respectively, the latter
second horizon (0.08s, 0.56s, 1.04s, 1.52s, and 2.00s af-                also stabilizing pose forecasts through steadier positional
ter the last observed frame). The first two sequences de-                context. Evaluated fairly with a non-overlapping, oracle-
pict players walking at a relaxed pace, completing roughly               free protocol, our model achieves state-of-the-art results
two steps over the displayed window. In both cases, pre-                 on WorldPose [32] and outperforms competing methods on
dictions stay close to ground truth, with residual error con-            3DPW [52] despite its lower social density, with qualita-
centrated in body orientation at the furthest frames rather              tive results confirming plausible forecasts under abrupt pace
than limb configuration. The last two sequences correspond               changes and graceful degradation on rare motions.
to substantially harder cases. In the third row, a player be-            Acknowledgment. This work has been partially sup-
gins a sprint abruptly at the observation boundary, a sud-               ported by the project GRAVATAR PID2023-151184OB-
den change in pace with no corresponding cue in the ob-                  I00 funded by MCIU/AEI/10.13039/501100011033 and by
served history, yet the forecast remains visually consistent             ERDF, UE and by the Government of Catalonia under 2020
and plausible. The fourth row shows a player walking side-               DI 00106.
References                                                             [16] Rohan Choudhury, Kris M Kitani, and László A Jeni.
                                                                            Tempo: Efficient multi-view pose estimation, tracking, and
 [1] Vida Adeli, Mahsa Ehsanpour, Ian Reid, Juan Car-                       forecasting. In ICCV, pages 14750–14760, 2023. 1, 2
     los Niebles, Silvio Savarese, Ehsan Adeli, and Hamid
                                                                       [17] Cecilia Curreli, Dominik Muhle, Abhishek Saroha, Zhen-
     Rezatofighi. Tripod: Human trajectory and pose dynamics
                                                                            zhang Ye, Riccardo Marin, and Daniel Cremers. Non-
     forecasting in the wild. In ICCV, pages 13390–13400, 2021.
                                                                            isotropic gaussian diffusion for realistic 3D human motion
     1, 3
                                                                            prediction. In CVPR, pages 1871–1882, 2025. 1, 2
 [2] Aadya Agrawal and Alexander Schwing. Simplihumon:
                                                                       [18] Zilin Fang, David Hsu, and Gim Hee Lee. Neuralized
     Simplifying human motion prediction.           arXiv preprint
                                                                            markov random field for interaction-aware stochastic human
     arXiv:2603.04399, 2026. 1, 2, 3, 5, 7, 8
                                                                            trajectory prediction. In ICLR, 2025. 1, 2
 [3] Mykhaylo Andriluka, Umar Iqbal, Eldar Insafutdinov,
                                                                       [19] Xuehao Gao, Shaoyi Du, Yang Wu, and Yang Yang. De-
     Leonid Pishchulin, Anton Milan, Juergen Gall, and Bernt
                                                                            compose more and aggregate better: Two closer looks at fre-
     Schiele. Posetrack: A benchmark for human pose estima-
                                                                            quency representation learning for human motion prediction.
     tion and tracking. In CVPR, pages 5167–5176, 2018. 3
                                                                            In CVPR, pages 6451–6460, 2023. 2
 [4] Görkay Aydemir, Adil Kaan Akan, and Fatma Güney. Adapt:
                                                                       [20] Yang Gao, Po-Chien Luan, and Alexandre Alahi. Multi-
     Efficient multi-agent trajectory prediction with adaptation. In
                                                                            transmotion: Pre-trained model for human motion predic-
     ICCV, pages 8295–8305, 2023. 1, 2
                                                                            tion. CoRL, 2024. 3
 [5] Inhwan Bae, Young-Jae Park, and Hae-Gon Jeon. Singu-
     lartrajectory: Universal trajectory predictor using diffusion     [21] Yang Gao, Po-Chien Luan, Kaouther Messaoud, Lan Feng,
     model. In CVPR, pages 17890–17901, 2024. 2                             and Alexandre Alahi. Omnitraj: Pre-training on heteroge-
                                                                            neous data for adaptive and zero-shot human trajectory pre-
 [6] German Barquero, Sergio Escalera, and Cristina Palmero.
                                                                            diction. arXiv preprint arXiv:2507.23657, 2025.
     Belfusion: Latent diffusion for behavior-driven human mo-
     tion prediction. In ICCV, pages 2317–2327, 2023. 1, 2             [22] Yang Gao, Saeed Saadatnejad, and Alexandre Alahi. Social-
                                                                            pose: Enhancing trajectory prediction with human body
 [7] Arij Bouazizi, Adrian Holzbock, Ulrich Kressel, Klaus Di-
                                                                            pose. TITS, 26(11):21309–21319, 2025. 3
     etmayer, and Vasileios Belagiannis. Motionmixer: Mlp-
     based 3D human body pose forecasting. arXiv preprint              [23] Colin Graber and Alexander G. Schwing. Dynamic neural
     arXiv:2207.00499, 2022. 1, 2                                           relational inference. In CVPR, 2020. 1, 2
 [8] Zhe Cao, Hang Gao, Karttikeya Mangalam, Qi-Zhi Cai,               [24] Junru Gu, Chen Sun, and Hang Zhao. Densetnt: End-to-end
     Minh Vo, and Jitendra Malik. Long-term human motion pre-               trajectory prediction from dense goal sets. In ICCV, pages
     diction with scene context. In ECCV, pages 387–404, 2020.              15303–15312, 2021. 1, 2
     3                                                                 [25] Marc Gutiérrez-Pérez and Antonio Agudo. Learning human
 [9] Guillem Capellera, Luis Ferraz, Antonio Rubio, Anto-                   sports motion feasibility via quantile regression on tracking
     nio Agudo, and Francesc Moreno-Noguer. Footbots: A                     data. In ACCV, 2026. 2
     transformer-based architecture for motion prediction in soc-      [26] Marc Gutiérrez-Pérez and Antonio Agudo. Pnlcalib: Sports
     cer. In ICIP, pages 2313–2319, 2024. 1                                 field registration via points and lines optimization. CVIU,
[10] Guillem Capellera, Luis Ferraz, Antonio Rubio, Antonio                 page 104712, 2026. 3
     Agudo, and Francesc Moreno-Noguer. Transportmer: A                [27] Marc Gutiérrez-Pérez, Calvin Yeung, Keisuke Fujii, and An-
     holistic approach to trajectory understanding in multi-agent           tonio Agudo. Once upon a goal: Towards orientation-based
     sports. In ACCV, pages 1652–1670, 2024. 2, 4                           shot metrics in football. CVIU, page 104732, 2026. 3
[11] Guillem Capellera, Antonio Rubio, Luis Ferraz, and Antonio        [28] Reyhaneh Hosseininejad, Megh Shukla, Saeed Saadatne-
     Agudo. Unified uncertainty-aware diffusion for multi-agent             jad, Mathieu Salzmann, and Alexandre Alahi. Motionmap:
     trajectory modeling. In CVPR, pages 22476–22486, 2025. 2               Representing multimodality in human pose forecasting. In
[12] Guillem Capellera, Luis Ferraz, Antonio Rubio, Alexandre               CVPR, pages 22680–22689, 2025. 1, 2
     Alahi, and Antonio Agudo. Jointdiff: Bridging continuous          [29] Catalin Ionescu, Dragos Papava, Vlad Olaru, and Cristian
     and discrete in multi-agent trajectory generation. In ICLR,            Sminchisescu. Human3.6m: Large scale datasets and predic-
     2026. 2                                                                tive methods for 3D human sensing in natural environments.
[13] Guillem Capellera, Antonio Rubio, Luis Ferraz, and Antonio             TPAMI, 36(7):1325–1339, 2014. 2
     Agudo. Heteroscedastic diffusion for multi-agent trajectory       [30] Jaewoo Jeong, Daehee Park, and Kuk-Jin Yoon. Multi-agent
     modeling. TPAMI, 48(10):11964–11977, 2026. 1                           long-term 3D human pose forecasting via interaction-aware
[14] Ling-Hao Chen, Jiawei Zhang, Yewen Li, Yiren Pang, Xi-                 trajectory conditioning. In CVPR, pages 1617–1628, 2024.
     aobo Xia, and Tongliang Liu. Humanmac: Masked motion                   1, 2, 3, 5, 7, 8
     completion for human motion prediction. In ICCV, pages            [31] Chiyu Jiang, Andre Cornman, Cheolho Park, Benjamin
     9544–9555, 2023. 1, 2                                                  Sapp, Yin Zhou, Dragomir Anguelov, et al. Motiondiffuser:
[15] Sehwan Choi, Jungho Kim, Junyong Yun, and Jun Won                      Controllable multi-agent motion prediction using diffusion.
     Choi. R-pred: Two-stage motion prediction via tube-query               In CVPR, pages 9644–9653, 2023. 1, 2
     attention-based trajectory refinement. In ICCV, pages 8525–       [32] Tianjian Jiang, Johsan Billingham, Sebastian Müksch, Juan
     8535, 2023. 1, 2                                                       Zarate, Nicolas Evans, Martin R Oswald, Marc Polleyfeys,
     Otmar Hilliges, Manuel Kaufmann, and Jie Song. World-         [47] Saeed Saadatnejad, Yang Gao, Kaouther Messaoud, and
     pose: A world cup dataset for global 3D human pose estima-         Alexandre Alahi. Social-transmotion: Promptable human
     tion. In ECCV, pages 343–362, 2024. 2, 5, 6, 7, 8                  trajectory prediction. ICLR, 2024. 3
[33] CMU Graphics Lab. Cmu graphics lab motion capture             [48] Jiarui Sun and Girish Chowdhary. Comusion: Towards con-
     database. http://mocap.cs.cmu.edu/, 2003. 3                        sistent stochastic human motion prediction via motion diffu-
[34] Juho Lee, Yoonho Lee, Jungtaek Kim, Adam Kosiorek, Se-             sion. In ECCV, pages 18–36, 2024. 1, 2
     ungjin Choi, and Yee Whye Teh. Set transformer: A frame-      [49] Julian Tanke, Linguang Zhang, Amy Zhao, Chengcheng
     work for attention-based permutation-invariant neural net-         Tang, Yujun Cai, Lezi Wang, Po-Chen Wu, Juergen Gall,
     works. In ICML, pages 3744–3753, 2019. 4                           and Cem Keskin. Social diffusion: Long-term multiple hu-
[35] Lihuan Li, Maurice Pagnucco, and Yang Song. Graph-                 man motion anticipation. In ICCV, pages 9601–9611, 2023.
     based spatial transformer with memory replay for multi-            3
     future pedestrian trajectory prediction. In CVPR, pages       [50] Wei Zhen Teoh. Coherent multi-agent trajectory forecasting
     2231–2241, 2022. 1, 2                                              in team sports with causaltraj. AAAIW, 2026. 1, 2
[36] Naureen Mahmood, Nima Ghorbani, Nikolaus F. Troje, Ger-       [51] Edward Vendrow, Satyajit Kumar, Ehsan Adeli, and Hamid
     ard Pons-Moll, and Michael J. Black. AMASS: Archive of             Rezatofighi. Somoformer: Multi-person pose forecasting
     motion capture as surface shapes. In ICCV, pages 5442–             with transformers. arXiv preprint arXiv:2208.14023, 2022.
     5451, 2019. 2                                                      3
[37] Angel Martı́nez-González, Michael Villamizar, and Jean-      [52] Timo von Marcard, Roberto Henschel, Michael Black, Bodo
     Marc Odobez. Pose transformers (potr): Human motion                Rosenhahn, and Gerard Pons-Moll. Recovering accurate 3D
     prediction with non-autoregressive transformers. In ICCV,          human pose in the wild using imus and a moving camera. In
     pages 2276–2284, 2021. 1, 2                                        ECCV, 2018. 2, 3, 5, 7, 8
                                                                   [53] Jiashun Wang, Huazhe Xu, Medhini Narasimhan, and Xiao-
[38] Omar Medjaouri and Kevin Desai. Hr-stan: High-resolution
                                                                        long Wang. Multi-person 3D motion prediction with multi-
     spatio-temporal attention network for 3D human motion pre-
                                                                        range transformers. NeurIPS, 34:6036–6049, 2021. 2, 3
     diction. In CVPR, pages 2540–2549, 2022. 1, 2
                                                                   [54] Chenxin Xu, Robby T Tan, Yuhong Tan, Siheng Chen, Xin-
[39] Dushyant Mehta, Oleksandr Sotnychenko, Franziska
                                                                        chao Wang, and Yanfeng Wang. Auxiliary tasks benefit 3D
     Mueller, Weipeng Xu, Srinath Sridhar, Gerard Pons-Moll,
                                                                        skeleton-based human motion prediction. In ICCV, pages
     and Christian Theobalt. Single-shot multi-person 3d pose
                                                                        9509–9520, 2023. 1, 2
     estimation from monocular rgb. In 3DV, pages 120–130,
                                                                   [55] Chenxin Xu, Robby T Tan, Yuhong Tan, Siheng Chen,
     2018. 3
                                                                        Yu Guang Wang, Xinchao Wang, and Yanfeng Wang. Eq-
[40] Behnam Parsaeifard, Saeed Saadatnejad, Yuejiang Liu, Tay-          motion: Equivariant multi-agent motion prediction with in-
     lor Mordan, and Alexandre Alahi. Learning decoupled repre-         variant interaction reasoning. In CVPR, pages 1410–1420,
     sentations for human pose forecasting. In ICCV, pages 2294–        2023. 3
     2303, 2021. 3
                                                                   [56] Pengfei Yao, Yinglong Zhu, Huikun Bi, Tianlu Mao, and
[41] Xiaogang Peng, Siyuan Mao, and Zizhao Wu. Trajectory-              Zhaoqi Wang. Trajclip: Pedestrian trajectory prediction
     aware body interaction transformer for multi-person pose           method using contrastive learning and idempotent networks.
     forecasting. In CVPR, pages 17121–17130, 2023. 2                   NeurIPS, 37:77023–77037, 2024. 2
[42] Marc Peral, Guillem Capellera, Luis Ferraz, Antonio Rubio,    [57] Mayssa Zaier, Hazem Wannous, Hassen Drira, and Jacques
     and Antonio Agudo. Multi-modal soccer scene analysis with          Boonaert. A dual perspective of human motion analysis-3D
     masked pre-training. In WACV, pages 3536–3545, 2026. 2             pose estimation and 2D trajectory prediction. In ICCV, pages
[43] Marc Peral, Guillem Capellera, Luis Ferraz, Antonio Rubio,         2189–2199, 2023. 3
     Stella Graßhof, Dan Witzner Hansen, and Antonio Agudo.        [58] Yuanhong Zheng, Ruixuan Yu, and Jian Sun. Efficient multi-
     Synergy between trajectories and human pose for soccer. In         person motion prediction by lightweight spatial and temporal
     ICIP, 2026. 3                                                      interactions. In ICCV, pages 10844–10853, 2025. 3
[44] Muhammad Rameez Ur Rahman, Luca Scofano, Edoardo
     De Matteis, Alessandro Flaborea, Alessio Sampieri, and
     Fabio Galasso. Best practices for 2-body pose forecasting.
     In CVPR, pages 3614–3624, 2023. 2
[45] Luke Rowe, Martin Ethier, Eli-Henry Dykhne, and
     Krzysztof Czarnecki. Fjmp: Factorized joint multi-agent
     motion prediction over learned directed acyclic interaction
     graphs. In CVPR, pages 13745–13755, 2023. 2
[46] Saeed Saadatnejad, Ali Rasekh, Mohammadreza Mofayezi,
     Yasamin Medghalchi, Sara Rajabzadeh, Taylor Mordan, and
     Alexandre Alahi. A generic diffusion-based approach for 3D
     human pose prediction in the wild. In ICRA, pages 8246–
     8253, 2023. 1, 2
   Unified Trajectory and 3D Pose Forecasting for Multi-Agent Sports Analysis
                         — Supplementary Material —
                   Marc Peral1,2 Guillem Capellera1,2 Luis Ferraz2 Antonio Rubio2
                        Stella Graßhof3 Dan Witzner Hansen3 Antonio Agudo1
                          1
                            Institut de Robòtica i Informàtica Industrial, CSIC-UPC
                       2
                         Kognia Sports Intelligence 3 IT University of Copenhagen

A. Joint Balancing Strategy
The target joints are identified by directly measuring per-
joint error under uniform weighting and selecting those with
consistently above-average error, rather than by assumption.
Under uniform weighting the distal joints (elbows, wrists,
ankles, and feet) carry markedly higher error than the rest of
the skeleton, while proximal joints such as the hips, spine,
and shoulders remain comparatively stable in root-relative
coordinates and dominate the averaged loss. Figure A1 vi-
sualizes per-joint error on a shared color scale before (left)
and after (right) rebalancing, so the two skeletons are di-
rectly comparable. The reduction is concentrated in the          Figure A1. Per-joint error under uniform loss weighting (left)
targeted distal joints, whose error visibly drops after rebal-   and with joint rebalancing (right). Each joint is colored by its
                                                                 mean absolute error on the test set, on a shared scale from 0 (light,
ancing. This directly prevents the degenerate static solu-
                                                                 low error) to 10 (dark, high error) across both skeletons, so the
tion into which a uniformly weighted loss could settle if the
                                                                 two panels are directly comparable. The targeted distal joints (el-
model minimizes average error by collapsing toward a near-       bows, wrists, ankles, and feet), outlined in cyan, are those with
motionless mean pose and leaving exactly these dynamic           consistently above-average error under uniform weighting, and re-
joints poorly predicted. By steering optimization toward the     balancing visibly reduces their error.
joints that carry the most discriminative information about
player actions, the rebalancing lowers their error and incen-
tivizes fine-grained articulation instead of collapse.           able part of the sequence was kept as absolute positions and
                                                                 only the frames to be forecast were expressed as displace-
B. Trajectory Smoothing Exploration                              ments. This reduced jitter and improved displacement error
                                                                 in the first forecast frames, but increased general ADE and
The frequency-domain smoothing term was the result of an         specially FDE as errors accumulated over the displacement
extended exploration of alternative strategies for suppress-     chain. Moreover, this representation fixed the boundary be-
ing the high-frequency oscillation that appears in absolute      tween the observed and forecast portions of the sequence at
pitch-coordinate trajectory predictions. The root cause of       a specific frame index, removing the model’s flexibility to
this jitter is that the model predicts absolute positions at     operate with different observation and forecast horizons.
each frame independently, with no explicit constraint on             A third alternative was a local smoothness penalty com-
temporal consistency between consecutive predictions.            puted in the time domain, penalizing second-order differ-
   The most natural alternative is to predict frame-to-frame     ences in position between consecutive frame triplets, which
displacements rather than absolute positions, converting the     correspond to sudden changes in velocity. This formula-
entire input sequence to a displacement representation so        tion operates only on pairs of adjacent frames and therefore
that the model reasons about changes in position rather than     misses oscillations that span more than two frames, which
positions themselves. This was implemented but produced          are the dominant artifact in practice.
a significant degradation of results. When all positions are         None of these alternatives matched the effective-
expressed as displacements, the model loses access to the        ness of the frequency-domain formulation ultimately
absolute spatial context of the scene: it can no longer di-      adopted, which penalizes the full-sequence power spec-
rectly represent where each player is on the pitch relative to   trum weighted by frequency, capturing all systematic high-
others, which is precisely the information the social atten-     frequency oscillations regardless of their temporal scale
tion block relies on to model inter-player interactions.         within the forecasting horizon.
   A second variant was then explored, where the observ-

```
