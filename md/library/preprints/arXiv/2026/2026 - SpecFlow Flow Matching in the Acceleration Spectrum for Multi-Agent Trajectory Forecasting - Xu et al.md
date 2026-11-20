<!-- source: library/preprints/arXiv/2026/2026 - SpecFlow Flow Matching in the Acceleration Spectrum for Multi-Agent Trajectory Forecasting - Xu et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.26390 -->
<!-- authors: Ziyang Xu, Peng Han, Hai Zhou -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-20; equations, tables and figures are NOT preserved - consult the PDF for those -->

# SpecFlow: Flow Matching in the Acceleration Spectrum for Multi-Agent Trajectory Forecasting

                                                    SpecFlow: Flow Matching in the Acceleration Spectrum for Multi-Agent
                                                                          Trajectory Forecasting
                                                                                       Ziyang Xu1,2 , Peng Han1∗ , Hai Zhou1
                                                                1
                                                                    National Space Science Center, Chinese Academy of Sciences, Beijing 100190, China
                                                                           2
                                                                             University of Chinese Academy of Sciences, Beijing 101408, China
                                                                         xuziyang23@mails.ucas.ac.cn, hanpeng@nssc.ac.cn, zhouhai@nssc.ac.cn


                                                                        Abstract                                             Past Trajectories
arXiv:2611.26390v1 [cs.RO] 19 Nov 2026




                                                                                                                                                              Gaussian Noise

                                           Multimodal trajectory forecasting must cover diverse future
                                           behaviors without sacrificing dynamical coherence. Most gen-
                                           erative forecasters evolve frame-wise positions directly, leav-
                                           ing the relationships among position, velocity, and accel-
                                           eration implicit. We present SpecFlow, a conditional flow-
                                           matching framework that treats the Discrete Cosine Trans-
                                           form (DCT) coefficients of future accelerations as its gener-
                                                                                                                                                                            k (2n + 1) 
                                                                                                                                                           Dk ,n = k cos               
                                           ative state. SpecFlow learns a transport from Gaussian noise                                                                         2T      
                                           to acceleration spectra and reconstructs velocity and posi-                                                        Discrete Cosine
                                                                                                                                                              Transform (DCT)
                                           tion through fixed analytical integration initialized by the last
                                           observed state. A joint phase-space objective supervises all
                                           three kinematic levels. To represent destination uncertainty
                                                                                                                                           Acceleration-Spectrum
                                           without future information, an endpoint predictor produces                                         Flow Matching
                                           candidate destinations and confidence scores solely from ob-
                                           served context, and the highest-confidence candidate condi-
                                                                                                                                                    Inverse DCT
                                           tions the spectral denoiser. Alternating attention over trajec-
                                           tory hypotheses and agents captures multimodality and inter-
                                           action. Under best-of-20 evaluation, SpecFlow achieves aver-                                       Double Integration
                                           age minADE/minFDE of 0.15/0.22 on ETH/UCY, 0.69/0.86 at
                                           four seconds on NBA, and 7.38/11.57 on SDD. It establishes
                                           state-of-the-art results across all five ETH/UCY scenes and
                                           achieves the lowest four-second ADE on NBA with a tied-best
                                           FDE, while remaining competitive on SDD. Together, these
                                           results demonstrate that acceleration-spectrum flow matching
                                           provides an effective structured generative state across smooth                                 Future Trajectories
                                           pedestrian motion, coordinated multi-agent sports dynamics,                          Past Trajectories          Prediction                 Endpoint

                                           and heterogeneous outdoor trajectories. Code will be made
                                           publicly available.
                                                                                                               Figure 1: SpecFlow generates acceleration spectra and re-
                                                                                                               constructs future trajectories.
                                                                     Introduction
                                         Trajectory forecasting estimates plausible future motion from            We define the generative state in the acceleration spec-
                                         observed multi-agent histories. Futures depend on scene ge-           trum. The DCT provides a fixed orthonormal temporal basis
                                         ometry and other agents. Recurrent, graph-based, adversar-            ordered from low to high frequency (Ahmed, Natarajan, and
                                         ial, variational, and diffusion models address this uncertainty       Rao 1974; Mao et al. 2019). A network transports Gaus-
                                         through interaction modeling and diverse sampling (Alahi              sian noise to acceleration coefficients. Two fixed cumulative
                                         et al. 2016; Gupta et al. 2018; Salzmann et al. 2020; Yuan            operators then recover velocity and position from the last ob-
                                         et al. 2021; Gu et al. 2022; Mao et al. 2023). Flow-matching          served state. Each acceleration sample determines all three
                                         models learn a continuous transport from simple noise to the          kinematic quantities. Retaining part of the basis sets the tem-
                                         trajectory distribution (Lipman et al. 2022; Fu et al. 2025).         poral bandwidth directly.
                                         Most methods generate frame-wise positions and learn their               The acceleration representation does not by itself resolve
                                         kinematic relations implicitly.                                       destination uncertainty or agent interaction. SpecFlow pre-
                                                                                                               dicts endpoints from observed context and uses the selected
                                                                                                               proposal to condition the denoiser. Its backbone alternates
                                            ∗
                                                Corresponding author.                                          attention along the hypothesis and agent axes. The first op-
eration exchanges information among modes. The second             human motion (Ahmed, Natarajan, and Rao 1974; Mao
models interaction within each joint forecast.                    et al. 2019; Mao, Liu, and Salzmann 2020). EigenTrajec-
   Under best-of-20 evaluation, SpecFlow averages 0.15/0.22       tory learns low-rank trajectory descriptors for multimodal
on ETH/UCY and ranks first in every scene. It reaches             forecasting (Bae, Oh, and Jeon 2023). Other models address
0.69/0.86 at four seconds on NBA and 7.38/11.57 on SDD            dynamic feasibility through heterogeneous dynamics, equiv-
without scene inputs.                                             ariance, or explicit control points (Salzmann et al. 2020; Xu
   The contributions are as follows:                              et al. 2023; Bae and Jeon 2023). SpecFlow applies the DCT
 • We formulate conditional flow matching in the DCT ac-          to acceleration and learns the flow in the resulting coefficient
   celeration spectrum. Fixed analytical operators recon-         space. Fixed integration recovers velocity and position.
   struct velocity and position from the observed state.
 • We train with a joint position–velocity–acceleration ob-
                                                                                              Method
   jective. Endpoint conditioning and alternating attention       Problem Formulation
   model destination uncertainty and agent interaction.           Let Xo ∈ RA×P ×2 denote P observed positions for A
 • SpecFlow leads all ETH/UCY scenes and four-second              agents, and let Xf ∈ RA×T ×2 denote their future positions.
   NBA ADE, ties the best NBA FDE, and remains compet-            Coordinates are relative to the final observation. A context
   itive on SDD. Ablations examine the main components            encoder maps absolute position, relative position, and finite-
   and sampling cost.                                             difference velocity to agent tokens H ∈ RA×d . The model
                                                                  generates M joint hypotheses {X b f,m }M . Each hypothesis
                                                                                                         m=1
                      Related Work                                forecasts all A agents. We use M = 20 in every experiment.
Trajectory Prediction. Classical crowd models encode
interaction through hand-crafted dynamics such as social          Acceleration Spectrum
forces (Helbing and Molnar 1998). Social LSTM and Social          Finite differences of the future sequence give velocity Vf
GAN introduced recurrent pooling and adversarial sampling         and acceleration Af . At the temporal boundary, we replicate
for pedestrian interaction (Alahi et al. 2016; Gupta et al.       the last valid difference as in the implementation. For horizon
2018). Graph and transformer models represent time-varying        T , the orthonormal DCT-II basis D ∈ RT ×T is
neighborhoods, group structure, and joint agent dependen-                                                  
                                                                                                 πk(2n + 1)
cies (Mohamed et al. 2020; Huang et al. 2019; Ivanovic and                   Dk,n = αk cos                    ,
Pavone 2019; Salzmann et al. 2020; Yuan et al. 2021; Xu et al.                                        2T                       (1)
2022; Shi et al. 2023, 2022; Xu et al. 2023; Kim et al. 2024).                           −1/2                      1/2
                                                                                α0 = T        ,      αk>0 = (2/T ) .
Other work makes long-term intent explicit through anchors,
endpoints, waypoints, or control points (Kothari, Sifringer,      We retain the first K rows, DK ∈ RK×T , and define the
and Alahi 2021; Mangalam et al. 2020, 2021; Chiara et al.         generative target
2022; Bae and Jeon 2023; Lin et al. 2024). IAD combines
endpoint proposals with short-term polar intentions and re-                        CA = DK Af ∈ RA×K×2 .                        (2)
finement (Liu et al. 2026). SpecFlow also predicts endpoints,     The basis is fixed. The value of K controls temporal
but uses them as observed-context conditions for a generative     bandwidth, and the learned transport operates in a 2K-
acceleration spectrum.                                            dimensional state per agent.
Diffusion and Flow Models. Latent-variable and adversar-
ial predictors learn distributions over plausible futures (Lee    Conditional Spectral Flow Matching
et al. 2017; Gupta et al. 2018; Sadeghian et al. 2019; Xu,        For each hypothesis, we sample Z ∼ N (0, I) and t ∈ (0, 1).
Hayet, and Karamouzas 2022). PCCSNet separates cluster-           A linear conditional path connects noise and data,
ing, classification, and synthesis (Sun et al. 2021). Diffu-
sion models learn iterative denoising transports from Gaus-                            Ct = (1 − t)Z + tCA .                    (3)
sian noise (Ho, Jain, and Abbeel 2020). Trajectory variants
use purposive hypotheses, motion-indeterminacy diffusion,         The denoiser predicts the clean spectral endpoint C
                                                                                                                    b A,θ from
leapfrog initialization, or compact descriptors (Bae, Park,       (Ct , t, H, e), where e is an endpoint embedding. This pre-
and Jeon 2022; Gu et al. 2022; Mao et al. 2023; Bae, Park,        diction induces the velocity
and Jeon 2024). Flow matching regresses a continuous prob-                                            b A,θ − Ct
                                                                                                      C
ability path and samples by integrating an ordinary differ-                           uθ (Ct , t) =              .              (4)
ential equation (Lipman et al. 2022; Liu, Gong, and Liu                                                  1−t
2023). MoFlow applies flow matching to multi-agent trajec-        For the linear conditional path, the target vector field is
tories and distills the transport into a one-step predictor (Fu
et al. 2025). SpecFlow retains an ODE sampler but trans-                              dCt            CA − Ct
                                                                              u⋆t =       = CA − Z =         ,                  (5)
ports acceleration-spectrum coefficients rather than frame-                            dt             1−t
wise coordinates.                                                 and the standard conditional flow-matching (CFM) objective
Spectral and Kinematic Structure. DCT bases provide               is                         h                    i
                                                                                                                2
compact representations of long temporal dependencies in                    LCFM = ECA ,Z,t ∥uθ (Ct , t) − u⋆t ∥F .      (6)
                                                          Gaussian Noise
        Observed                                         (M Joint Samples)
       Trajectories

 Agent 1

 Agent 2
                                Agent Context          Acceleration-Spectrum               M Joint Acceleration-
                                           ⋯
                                                          Flow Matching                    Spectrum Hypotheses
   ⋯




 Agent N
                                                                                                                       M Joint Multi-Agent
                                  Endpoint
           time                                                                                                             Forecasts
                                  Predictor

                                                                                                Kinematic
                                                                                              Reconstruction
                              Selected Endpoint
                                  Condition                                                Inverse DCT + Double
                                                                                                 Integration
                              Training: nearest GT
                            Inference: highest score
 Ground-Truth Future
     Trajectories
 Agent 1
                            Acceleration-Spectrum
 Agent 2
                                    Target             Training Only
                                  First K DCT
   ⋯




                                  Coefficients
 Agent N


           time


Figure 2: Observed trajectories and Gaussian noise enter the endpoint predictor and acceleration-spectrum flow model. Fixed
reconstruction maps M joint acceleration hypotheses to future trajectories. Ground-truth futures select the endpoint condition
and spectral target only during training.


Under the clean-endpoint parameterization,                                   Fixed Kinematic Reconstruction
                                        2 
                                                                             Let S ∈ RT ×T be the strict lower-triangular cumulative-sum
                       
                           b A,θ − CA
                           C
                                        F                                   matrix, and define
             LCFM = E                     ,                  (7)
                       
                             (1 − t)2                                                   Wint = DK SD⊤
                                                                                                    K,             d1 = DK 1.                (8)
so spectral data prediction and CFM field regression param-                  Given the last observed relative position x0 and velocity v0 ,
eterize the same conditional transport. At inference, Euler                  spectral velocity and position are reconstructed as
integration starts from Gaussian noise and advances the ve-                                              b A + d1 v ⊤ ,
                                                                                              C
                                                                                              b V = Wint C
                                                                                                                   0                         (9)
locity field from t = 0 to t = 1. During training, t follows a
logit-normal distribution that places fewer samples near the                                  CX = Wint CV + d1 x⊤ .
                                                                                              b          b
                                                                                                                       0                 (10)
path endpoints.
                                                                             The time-domain outputs are A b = D⊤ C               ⊤ b
   Each noisy spectrum is combined with a sinusoidal time                                                           K A , V = DK CV ,
                                                                                                                      b    b
code, observed context, a hypothesis embedding, and an                                   ⊤
                                                                             and Xb =D C
                                                                                         K X . All matrices are precomputed and frozen.
                                                                                           b
agent embedding. A decoder block first applies self-attention                Position and velocity follow deterministically from the ac-
across the M hypotheses for each agent. It then attends across               celeration sample and observed initial state.
the A agents within each hypothesis. A classification head
scores the generated hypotheses.                                             Joint Phase-Space Objective
                                                                             For each training example, we select the nearest hypothesis
Observed-Context Endpoint Conditioning                                       in position space and supervise it at all kinematic levels:
For each agent, L = 20 learned queries cross-attend to
its context token. Two multilayer perceptrons produce can-                                   Lphase = λx Lx + λv Lv + λa La ,
                                                                                                                                         (11)
didate endpoints {gℓ }L                                    L
                         ℓ=1 and confidence logits {sℓ }ℓ=1 .
                                                                                       (λx , λv , λa ) = (1, 0.5, 0.1).
During training, the ground-truth destination is assigned to                 Each term is the mean Euclidean error over valid agents and
the nearest candidate. Endpoint regression and confidence                    frames. Let Ra , Rv , and Rx denote the fixed linear maps
classification supervise the predictor, and the nearest pro-                 from an acceleration spectrum to acceleration, velocity, and
posal conditions the denoiser. At inference, the model selects               position. Observed-state offsets cancel in prediction errors.
garg maxℓ sℓ . Future positions and oracle goals are never used              For every phase-space level q,
at test time. The endpoint objective is the same on all three
datasets.                                                                                 b A − CA ) = (1 − t)Rq (uθ − u⋆ ).
                                                                                      Rq (C                                              (12)
                                                                                                                        t
                      (a) ETH_UCY                                                                         (b) SDD
                                        Past Trajectory           Prediction           Ground Truth



Figure 3: Observed ETH/UCY and SDD trajectories are input to SpecFlow. The model outputs multiple forecasts, shown with
the ground-truth futures.


Thus Lphase is a clean-data CFM objective under a fixed                   The improvement is not concentrated in one unusually easy
kinematic task metric and logit-normal time weighting. Its             split. Using the rounded entries in Table 1, SpecFlow lowers
numerical value differs from the isotropic squared norm in             the second-best FDE by 0.06 on ETH, 0.03 on HOTEL, 0.11
Eq. (6). The zero-error vector field is unchanged because              on UNIV, 0.06 on ZARA1, and 0.04 on ZARA2. The relative
λa > 0 and Ra = D⊤   K is injective on the retained spectrum.          reductions are approximately 11.8%, 20.0%, 33.3%, 25.0%,
The implementation uses this structured surrogate without a            and 20.0%. UNIV combines the largest absolute and relative
separate isotropic spectral loss. The complete objective is            gains, while HOTEL has the smallest absolute scale and still
                                                                       improves. This scene-wise consistency is stronger evidence
            Ltotal = Lphase + λc Lcls + λe Lend .         (13)         for the representation than the average alone, because leave-
All losses act on the same acceleration–velocity–position              one-scene-out evaluation changes both training composition
reconstruction.                                                        and test geometry in every row.
                                                                       NBA. Table 2 places SpecFlow among the best two entries
                      Experiments                                      for all eight NBA metrics. It ties the best ADE and FDE
Experimental Setup                                                     at one second. At two seconds, IAD is lower by 0.01 on
We evaluate on ETH/UCY (Pellegrini et al. 2009; Lerner,                both measures. At three seconds, SpecFlow has a 0.01 lower
Chrysanthou, and Lischinski 2007), NBA SportVU (Yue                    FDE, while IAD has a 0.02 lower ADE. At four seconds,
et al. 2014), and Stanford Drone Dataset (SDD) (Robicquet              SpecFlow reaches 0.69/0.86 while forecasting all 11 entities
et al. 2016). ETH/UCY uses leave-one-scene-out evaluation              jointly. This is the lowest ADE and a tied-best FDE. The
with eight observed and twelve predicted frames. NBA uses              ranking changes across horizons rather than showing uniform
ten observed frames and predicts twenty frames, or four sec-           dominance.
onds, for ten players and the ball. SDD contains 2,829 test               The horizon-wise pattern distinguishes short-term fit from
windows with eight observed and twelve predicted frames.               long-term stability. At one second, SpecFlow, MoFlow, and
We report best-of-20 minADE20 / minFDE20 in meters for                 MoFlow-IMLE are indistinguishable after rounding. By four
ETH/UCY and NBA and in pixels for SDD. Baseline values                 seconds, SpecFlow lowers ADE from 0.71 to 0.69 relative
retain their published precision.                                      to both MoFlow variants and matches the best FDE of 0.86.
                                                                       IAD is strongest at two-second ADE/FDE, whereas its FDE
Main Results                                                           rises from 0.45 to 0.99 over the remaining two seconds. The
                                                                       corresponding increase for SpecFlow is from 0.46 to 0.86.
ETH/UCY. Table 1 reports the lowest minADE/minFDE                      These results suggest that the spectral acceleration state is
pair for SpecFlow in all five scenes. Its average is 0.15/0.22,        most useful as errors accumulate over a longer rollout, rather
compared with second-best values of 0.19 and 0.30. UNIV                than as a uniform gain at every intermediate horizon.
has the largest FDE margin, at 0.22 versus 0.33 for High-
Graph. On ETH, SpecFlow gives 0.45 FDE versus 0.51 for                 SDD. SpecFlow obtains 7.38/11.57 on SDD. It ranks third
PPT. The FDE margins are larger than the ADE margins,                  in minADE and fourth in minFDE. The gaps to the best
placing most of the difference near the end of the prediction          entries are 0.53 and 0.92 pixels. SpecFlow uses trajectories
horizon.                                                               without scene images or semantic maps. Its result remains
Method                              ETH                     HOTEL                  UNIV            ZARA1                ZARA2                   AVG
Social-GAN                      0.87/1.62                  0.67/1.37           0.76/1.52           0.35/0.68            0.42/0.84             0.61/1.21
Social-STGCNN                   0.64/1.11                  0.49/0.85           0.44/0.79           0.34/0.53            0.30/0.48             0.44/0.75
Social-VAE                      0.41/0.58                  0.13/0.19           0.21/0.36           0.17/0.29            0.13/0.22             0.21/0.33
MID                             0.39/0.66                  0.13/0.22           0.22/0.45           0.17/0.30            0.13/0.27             0.21/0.38
LED                             0.39/0.58                  0.11/0.17           0.26/0.43           0.18/0.26            0.13/0.22             0.21/0.33
EigenTrajectory                 0.36/0.53                  0.12/0.19           0.24/0.43           0.19/0.33            0.14/0.24             0.21/0.34
TUTR                            0.40/0.61                  0.11/0.18           0.23/0.42           0.18/0.34            0.13/0.25             0.21/0.36
HighGraph                       0.40/0.55                  0.13/0.17           0.20/0.33           0.17/0.27            0.11/0.21             0.20/0.30
PPT                             0.36/0.51                  0.11/0.15           0.22/0.40           0.17/0.30            0.12/0.21             0.20/0.31
MoFlow                          0.40/0.57                  0.11/0.17           0.23/0.39           0.15/0.26            0.12/0.22             0.20/0.32
IAD                             0.34/0.52                  0.15/0.24           0.20/0.36           0.15/0.24            0.11/0.20             0.19/0.31
SpecFlow                        0.29/0.45                  0.10/0.12           0.14/0.22           0.12/0.18            0.10/0.16             0.15/0.22

Table 1: Best-of-20 ETH/UCY results in meters. AVG is the scene mean. Baselines follow MoFlow and IAD (Fu et al. 2025;
Liu et al. 2026). Bold and underlined values rank first and second.

                                           1s                                 2s                          3s                           Total (4 s)
Method                         ADE                FDE                  ADE          FDE           ADE            FDE                ADE              FDE
Social-GAN                      0.41               0.62                0.81          1.32         1.19           1.94               1.59             2.41
Social-STGCNN                   0.34               0.48                0.71          0.94         1.09           1.77               1.53             2.26
PECNet                          0.40               0.71                0.83          1.61         1.27           2.44               1.69             2.95
NPSN                            0.35               0.58                0.68          1.23         1.01           1.76               1.31             1.79
GroupNet                        0.26               0.34                0.49          0.70         0.73           1.02               0.96             1.30
MID                             0.28               0.37                0.51          0.72         0.71           0.98               0.96             1.27
LED                             0.18               0.27                0.37          0.56         0.58           0.84               0.81             1.10
MoFlow                          0.18               0.25                0.34          0.47         0.52           0.67               0.71             0.87
MoFlow-IMLE                     0.18               0.25                0.34          0.47         0.52           0.67               0.71             0.86
IAD                             0.21               0.25                0.32          0.45         0.48           0.75               0.79             0.99
SpecFlow                        0.18               0.25                0.33          0.46         0.50           0.66               0.69             0.86

Table 2: Best-of-20 NBA results in meters at cumulative horizons. Baselines follow MoFlow and IAD (Fu et al. 2025; Liu et al.
2026). Bold and underlined values rank first and second.


                                                                                    tent with a dataset in which curbs, entrances, and walkable
                                                                                    regions provide information that cannot always be inferred
                                                                                    from eight observed positions. This comparison motivates
                                                                                    adding scene semantics as a complementary condition rather
                                                                                    than changing the acceleration-spectrum representation.

                                                                                    Qualitative Results
                                                                                    Figures 3 and 4 show forecasts on the three datasets. The
                  Past Trajectory    Prediction   Ground Truth                      ETH/UCY and SDD samples continue the observed heading
                                                                                    and include curved paths. Each NBA sample contains all ten
Figure 4: Observed trajectories for ten players and the ball                        players and the ball, rather than independently selected agent
are input to SpecFlow. The model outputs a joint forecast.                          paths. The examples show forecast geometry and grouping.
Ground-truth futures are shown for comparison.                                      They do not measure diversity, calibration, or likelihood.

                                                                                    Ablation Studies
competitive, but visual context can still help resolve scene-                       Table 4 isolates the main choices in the representation, objec-
dependent destinations.                                                             tive, and architecture. The acceleration DCT spectrum gives
   The SDD ranking also clarifies the boundary of motion-                           lower error than either time-domain acceleration or the po-
only conditioning. Relative to the best entries, the ADE and                        sition DCT spectrum on all three benchmarks. Position, ve-
FDE gaps are approximately 7.7% and 8.6%, respectively.                             locity, and acceleration supervision perform best when used
In contrast, SpecFlow improves over MoFlow by 0.12 ADE                              together. Removing either attention axis increases error, and
and 0.39 FDE under the same trajectory-only input type. The                         removing both produces the largest change within that block.
remaining difference to PPT and IAD is therefore consis-                            A separately trained model without endpoint prediction and
Method                 Year         minADE           minFDE      short-horizon dynamics provide additional constraints.
Social-GAN             2018           27.23            41.44     Sampling efficiency. The supplement reports represen-
SoPhie                 2019           16.27            29.38     tation, bandwidth, classification, sample-count, endpoint-
PECNet                 2020            9.96            15.88     query, input-feature, and solver experiments, and separates
PCCSNet                2021            8.62            16.16
Social-VAE             2022            8.10            11.72
                                                                 a retrained endpoint ablation from an inference-time inter-
MID                    2022            7.61            14.30     vention. Reducing Euler integration from 100 to 20 steps
LED                    2023           8.48             11.66     preserves all three headline results at two-decimal precision.
TUTR                   2023            7.76            12.69     On NBA, latency falls from 17.55 to 3.68 ms per scene,
ET+HighGraph           2024           7.81             11.09     or to approximately 21% of the 100-step cost. Higher-order
PPT                    2024            7.03            10.65     solvers yield only small raw-error changes while increasing
MoFlow                 2025           7.50             11.96     runtime. The main tables retain the conservative 100-step
IAD                    2026           6.85             11.22     setting for comparability, but the step ablation indicates that
SpecFlow               2027           7.38             11.57     the learned vector field is smooth enough for substantially
                                                                 cheaper deployment.
Table 3: Best-of-20 SDD results in pixels. Values follow IAD,
with ET+HighGraph added from MoFlow (Fu et al. 2025;             Design Trade-offs
Liu et al. 2026).                                                Spectral bandwidth. The bandwidth sweep retains one
                                                                 quarter, one half, three quarters, or all DCT coefficients.
                                                                 The half-spectrum setting used by the full model is best
conditioning also performs worse than the full model.            on every dataset: 0.15/0.22 on ETH/UCY, 0.6976/0.8694 on
                                                                 NBA, and 7.38/11.57 on SDD. A quarter spectrum raises
Representation and supervision. Replacing frame-wise             FDE to 0.29, 0.9090, and 12.62, indicating that aggressive
position generation with the full acceleration-spectrum          truncation removes trajectory changes needed for accurate
model reduces ETH/UCY ADE/FDE from 0.18/0.28 to                  endpoints. Retaining the full spectrum also degrades FDE
0.15/0.22, reductions of 16.7% and 21.4%. The corre-             to 0.24, 0.8820, and 11.78. The consistent U-shaped pattern
sponding relative reductions are 4.6%/5.3% on NBA and            supports a bias–variance interpretation: low frequencies cap-
6.8%/7.1% on SDD. Time-domain acceleration is consis-            ture the dominant motion, whereas some higher-frequency
tently better than frame-wise position, but remains worse        coefficients model turns and interaction responses; retain-
than its DCT counterpart. The gain is therefore not explained    ing every coefficient also exposes the flow to high-frequency
by differentiation alone: concentrating motion in a truncated    variation that contributes less to displacement accuracy.
low-frequency basis also matters. Position DCT improves
over frame-wise positions, yet acceleration DCT is better on     Hypothesis and endpoint budgets. Increasing the number
every dataset, supporting the choice to place the generative     of joint hypotheses from 1 to 5, 10, and 20 monotonically
state at the highest explicitly supervised kinematic order.      improves all three benchmarks. On NBA, ADE/FDE falls
   The phase-space rows show complementary supervision           from 0.9210/1.3210 to 0.7620/0.9840, 0.7210/0.9050, and
rather than three interchangeable losses. Adding velocity to     0.6976/0.8694, while measured runtime grows from 1.0×
position-only training reduces FDE from 0.25 to 0.23 on          to 1.3×, 1.6×, and 2.0×. The largest gain occurs between
ETH/UCY, from 0.8970 to 0.8810 on NBA, and from 12.06            one and five hypotheses, but the remaining increments are
to 11.81 on SDD. Position plus acceleration is also better       material under best-of-20 evaluation. Endpoint queries show
than position alone, but is slightly weaker than position plus   clearer saturation. Increasing L from 5 to 10 and 20 improves
velocity. The full objective improves again to 0.22, 0.8694,     NBA FDE from 0.8970 to 0.8830 and 0.8694, whereas 40
and 11.57 FDE. Velocity supplies a direct constraint on lo-      queries gives 0.8700. ETH/UCY likewise stays at 0.15/0.22
cal displacement, while acceleration penalizes changes in        for 20 and 40 queries, and SDD changes from 7.38/11.57
that displacement; their combination is consistent with the      to 7.40/11.61. We therefore use 20 endpoint candidates: it
deterministic two-stage reconstruction.                          captures the measurable gain without doubling a proposal
                                                                 set that already saturates.
Interaction, modes, and endpoints. Removing both at-
tention axes produces the largest architectural degradation:     Observed context. The observed-input sweep separates
relative to the full model, FDE rises by 36.4% on ETH/UCY,       geometry from dynamics. Absolute positions alone ob-
8.9% on NBA, and 10.0% on SDD. Retaining only agent-             tain 0.19/0.31 on ETH/UCY, 0.7510/0.9540 on NBA, and
axis attention is better on NBA and SDD than retaining           8.21/13.04 on SDD. Adding coordinates relative to the last
only hypothesis-axis attention, which is expected for joint      observation improves all three; adding finite-difference ve-
forecasts containing interacting entities. On ETH/UCY, the       locity produces the full-model results. The same ordering
two single-axis variants are close, indicating that mode co-     across coordinate systems indicates that the gain is not tied to
ordination and social interaction both contribute. The end-      a benchmark-specific unit. Relative positions remove global
point ablation raises FDE from 0.22 to 0.26, from 0.8694         offsets, while velocity exposes the local trend that must be
to 0.8950, and from 11.57 to 12.39. Its larger relative effect   continued or changed by the predicted acceleration. The
on ETH/UCY and SDD is consistent with destination ambi-          hypothesis-classification head provides a smaller but consis-
guity in pedestrian scenes; on NBA, player interactions and      tent improvement: removing it changes the three FDE values
Variant                                            ETH/UCY                           NBA                                  SDD
Representation
Frame-wise position                                0.18/0.28                     0.7310/0.9180                         7.92/12.45
Position DCT spectrum                              0.16/0.25                     0.7160/0.8980                         7.66/12.03
Time-domain acceleration                           0.16/0.24                     0.7110/0.8910                         7.61/11.94
Phase-space supervision
Position only                                      0.17/0.25                     0.7160/0.8970                         7.71/12.06
Position + velocity                                0.16/0.23                     0.7050/0.8810                         7.52/11.81
Position + acceleration                            0.16/0.24                     0.7080/0.8860                         7.58/11.90
Attention and endpoint conditioning
No hypothesis-axis attention                       0.17/0.26                     0.7290/0.9150                         7.81/12.31
No agent-axis attention                            0.17/0.27                     0.7180/0.8990                         7.76/12.22
No attention on either axis                        0.19/0.30                     0.7480/0.9470                         8.04/12.73
No endpoint module                                 0.17/0.26                     0.7120/0.8950                         7.86/12.39
Full SpecFlow                                      0.15/0.22                     0.6976/0.8694                         7.38/11.57

                Table 4: Component ablations reported as minADE/minFDE. All variants use best-of-20 sampling.


from 0.22, 0.8694, and 11.57 to 0.24, 0.8860, and 11.88. This        Taken together, the experiments support three distinct
head does not create additional samples; it helps organize and    claims. The main tables establish competitive sample cov-
select the existing joint hypotheses during training.             erage across pedestrian, sports, and aerial-view benchmarks.
                                                                  The representation and objective ablations attribute the gain
Endpoint diagnostic. Separately trained models without            to acceleration-spectrum generation with joint kinematic su-
endpoint conditioning obtain 0.17/0.26, 0.7120/0.8950, and        pervision. The solver study shows that the result is not de-
7.86/12.39, while replacing predicted endpoints with ground-      pendent on a finely discretized 100-step trajectory. They do
truth endpoints yields diagnostic upper bounds of 0.13/0.18,      not establish calibrated probabilities, robustness across train-
0.6650/0.8110, and 6.92/10.54. The gap between predicted          ing seeds, or the contribution of visual semantics. Those
and oracle conditioning shows that endpoint estimation re-        questions require likelihood- or calibration-aware metrics,
mains a meaningful error source, especially on SDD. A             repeated training, and controlled scene-feature experiments.
fixed-checkpoint NBA intervention is more conservative:
bypassing the predicted endpoint changes 0.6976/0.8694 to                                 Conclusion
0.7052/0.8903. Together, the retraining and intervention tests
separate two effects. Endpoint supervision shapes the learned     SpecFlow applies conditional flow matching to DCT co-
representation over training, and the endpoint embedding          efficients of future acceleration. Fixed reconstruction links
also contributes directly at inference. The oracle row is not a   acceleration, velocity, and position to the observed initial
test-time result and is used only to estimate remaining head-     state. Endpoint conditioning represents destination uncer-
room.                                                             tainty. Alternating attention exchanges information among
                                                                  hypotheses and agents. The model gives the best reported
                                                                  results on ETH/UCY and four-second NBA ADE, ties the
Cross-Dataset Analysis                                            best NBA FDE, and remains competitive on SDD.
The three benchmarks use the same acceleration-spectrum              Despite its strong performance across diverse motion
target and reconstruction but differ in horizon, coordinate       regimes, SpecFlow remains a motion-only forecaster: it does
system, scene content, and number of agents. Their raw er-        not incorporate scene imagery, walkable-region priors, or se-
rors are therefore not directly comparable. On ETH/UCY,           mantic destination cues. The comparatively smaller gains on
SpecFlow improves both metrics in every scene, with larger        SDD therefore highlight the complementary role of scene
margins in FDE. On NBA, it is not best at every interme-          context in resolving destination ambiguity, rather than a
diate horizon, but gives the lowest four-second ADE and a         limitation of the acceleration-spectrum representation itself.
tied-best FDE. Its smaller ranking advantage on SDD is con-       Moreover, best-of-20 displacement metrics evaluate sample-
sistent with the absence of visual scene cues, although the       set coverage but do not characterize probability calibration,
benchmark does not isolate that factor.                           likelihood quality, or the distribution of generated modes. Ex-
   Best-of-20 metrics measure whether the sample set con-         tending the proposed structured generative state with scene-
tains a trajectory near the ground truth. They do not measure     aware conditioning and calibration-sensitive evaluation con-
calibration or likelihood. Results that become equal after        stitutes a natural direction for future work.
rounding are treated as ties. The main experiments use one
seed, so they do not quantify variation across training runs.
The ablations compare controlled variants of SpecFlow, but
four-decimal values should not be compared with baseline
values reported at lower precision.
                        References                                 Kim, S.; Chi, H.-g.; Lim, H.; Ramani, K.; Kim, J.; and Kim,
Ahmed, N.; Natarajan, T.; and Rao, K. R. 1974. Discrete            S. 2024. Higher-order relational reasoning for pedestrian tra-
cosine transform. IEEE transactions on Computers, 100(1):          jectory prediction. In Proceedings of the IEEE/CVF Confer-
90–93.                                                             ence on Computer Vision and Pattern Recognition, 15251–
Alahi, A.; Goel, K.; Ramanathan, V.; Robicquet, A.; Fei-Fei,       15260.
L.; and Savarese, S. 2016. Social lstm: Human trajectory           Kothari, P.; Sifringer, B.; and Alahi, A. 2021. Interpretable
prediction in crowded spaces. In Proceedings of the IEEE           social anchors for human trajectory forecasting in crowds.
conference on computer vision and pattern recognition, 961–        In Proceedings of the IEEE/CVF Conference on Computer
971.                                                               Vision and Pattern Recognition, 15556–15566.
Bae, I.; and Jeon, H.-G. 2023. A set of control points con-        Lee, N.; Choi, W.; Vernaza, P.; Choy, C. B.; Torr, P. H.; and
ditioned pedestrian trajectory prediction. In Proceedings of       Chandraker, M. 2017. Desire: Distant future prediction in
the AAAI Conference on Artificial Intelligence, volume 37,         dynamic scenes with interacting agents. In Proceedings of the
6155–6165.                                                         IEEE conference on computer vision and pattern recognition,
Bae, I.; Oh, J.; and Jeon, H.-G. 2023. Eigentrajectory: Low-       336–345.
rank descriptors for multi-modal trajectory forecasting. In        Lerner, A.; Chrysanthou, Y.; and Lischinski, D. 2007.
Proceedings of the IEEE/CVF International Conference on            Crowds by example. In Computer graphics forum, vol-
Computer Vision, 10017–10029.                                      ume 26, 655–664. Wiley Online Library.
Bae, I.; Park, J.-H.; and Jeon, H.-G. 2022. Non-probability        Lin, X.; Liang, T.; Lai, J.; and Hu, J.-F. 2024. Progressive
sampling network for stochastic human trajectory prediction.       pretext task learning for human trajectory prediction. In Eu-
In Proceedings of the IEEE/CVF Conference on Computer              ropean Conference on Computer Vision, 197–214. Springer.
Vision and Pattern Recognition, 6477–6487.                         Lipman, Y.; Chen, R. T.; Ben-Hamu, H.; Nickel, M.; and
Bae, I.; Park, Y.-J.; and Jeon, H.-G. 2024. Singulartrajectory:    Le, M. 2022. Flow matching for generative modeling. In
Universal trajectory predictor using diffusion model. In Pro-      The eleventh international conference on learning represen-
ceedings of the IEEE/CVF Conference on Computer Vision             tations.
and Pattern Recognition, 17890–17901.
                                                                   Liu, X.; Gong, C.; and Liu, Q. 2023. Flow straight and
Chiara, L. F.; Coscia, P.; Das, S.; Calderara, S.; Cucchiara,      fast: Learning to generate and transfer data with rectified
R.; and Ballan, L. 2022. Goal-driven self-attentive recur-         flow. In International conference on learning representations
rent networks for trajectory prediction. In Proceedings of         (ICLR).
the IEEE/CVF conference on computer vision and pattern
recognition, 2518–2527.                                            Liu, Y.; Liu, Z.; Ren, X.; Li, Y.; and Kong, H. 2026. Intention-
                                                                   aware diffusion model for pedestrian trajectory prediction.
Fu, Y.; Yan, Q.; Wang, L.; Li, K.; and Liao, R. 2025. Moflow:      In Proceedings of the AAAI Conference on Artificial Intelli-
One-step flow matching for human trajectory forecasting via        gence, volume 40, 18469–18477.
implicit maximum likelihood estimation based distillation. In
Proceedings of the Computer Vision and Pattern Recognition         Mangalam, K.; An, Y.; Girase, H.; and Malik, J. 2021. From
Conference, 17282–17293.                                           goals, waypoints & paths to long term human trajectory fore-
                                                                   casting. In Proceedings of the IEEE/CVF international con-
Gu, T.; Chen, G.; Li, J.; Lin, C.; Rao, Y.; Zhou, J.; and Lu, J.
                                                                   ference on computer vision, 15233–15242.
2022. Stochastic trajectory prediction via motion indetermi-
nacy diffusion. In Proceedings of the IEEE/CVF conference          Mangalam, K.; Girase, H.; Agarwal, S.; Lee, K.-H.; Adeli, E.;
on computer vision and pattern recognition, 17113–17122.           Malik, J.; and Gaidon, A. 2020. It is not the journey but the
Gupta, A.; Johnson, J.; Fei-Fei, L.; Savarese, S.; and Alahi, A.   destination: Endpoint conditioned trajectory prediction. In
2018. Social gan: Socially acceptable trajectories with gener-     European conference on computer vision, 759–776. Springer.
ative adversarial networks. In Proceedings of the IEEE con-        Mao, W.; Liu, M.; and Salzmann, M. 2020. History repeats
ference on computer vision and pattern recognition, 2255–          itself: Human motion prediction via motion attention. In Eu-
2264.                                                              ropean Conference on Computer Vision, 474–489. Springer.
Helbing, D.; and Molnar, P. 1998. Social force model for           Mao, W.; Liu, M.; Salzmann, M.; and Li, H. 2019. Learning
pedestrian dynamics. arXiv preprint cond-mat/9805244.              trajectory dependencies for human motion prediction. In
Ho, J.; Jain, A.; and Abbeel, P. 2020. Denoising diffusion         Proceedings of the IEEE/CVF international conference on
probabilistic models. Advances in neural information pro-          computer vision, 9489–9497.
cessing systems, 33: 6840–6851.                                    Mao, W.; Xu, C.; Zhu, Q.; Chen, S.; and Wang, Y. 2023.
Huang, Y.; Bi, H.; Li, Z.; Mao, T.; and Wang, Z. 2019. Stgat:      Leapfrog diffusion model for stochastic trajectory prediction.
Modeling spatial-temporal interactions for human trajectory        In Proceedings of the IEEE/CVF conference on computer
prediction. In Proceedings of the IEEE/CVF international           vision and pattern recognition, 5517–5526.
conference on computer vision, 6272–6281.                          Mohamed, A.; Qian, K.; Elhoseiny, M.; and Claudel, C. 2020.
Ivanovic, B.; and Pavone, M. 2019. The trajectron: Proba-          Social-stgcnn: A social spatio-temporal graph convolutional
bilistic multi-agent trajectory modeling with dynamic spa-         neural network for human trajectory prediction. In Proceed-
tiotemporal graphs. In Proceedings of the IEEE/CVF inter-          ings of the IEEE/CVF conference on computer vision and
national conference on computer vision, 2375–2384.                 pattern recognition, 14424–14432.
Pellegrini, S.; Ess, A.; Schindler, K.; and Van Gool, L. 2009.
You’ll never walk alone: Modeling social behavior for multi-
target tracking. In 2009 IEEE 12th international conference
on computer vision, 261–268. IEEE.
Robicquet, A.; Sadeghian, A.; Alahi, A.; and Savarese, S.
2016. Learning social etiquette: Human trajectory under-
standing in crowded scenes. In European conference on
computer vision, 549–565. Springer.
Sadeghian, A.; Kosaraju, V.; Sadeghian, A.; Hirose, N.;
Rezatofighi, H.; and Savarese, S. 2019. Sophie: An atten-
tive gan for predicting paths compliant to social and physical
constraints. In Proceedings of the IEEE/CVF conference on
computer vision and pattern recognition, 1349–1358.
Salzmann, T.; Ivanovic, B.; Chakravarty, P.; and Pavone, M.
2020. Trajectron++: Dynamically-feasible trajectory fore-
casting with heterogeneous data. In European conference on
computer vision, 683–700. Springer.
Shi, L.; Wang, L.; Zhou, S.; and Hua, G. 2023. Trajectory
unified transformer for pedestrian trajectory prediction. In
Proceedings of the IEEE/CVF International Conference on
Computer Vision, 9675–9684.
Shi, S.; Jiang, L.; Dai, D.; and Schiele, B. 2022. Motion trans-
former with global intention localization and local movement
refinement. Advances in Neural Information Processing Sys-
tems, 35: 6531–6543.
Sun, J.; Li, Y.; Fang, H.-S.; and Lu, C. 2021. Three steps to
multimodal trajectory prediction: Modality clustering, clas-
sification and synthesis. In Proceedings of the IEEE/CVF In-
ternational Conference on Computer Vision, 13250–13259.
Xu, C.; Li, M.; Ni, Z.; Zhang, Y.; and Chen, S. 2022. Group-
net: Multiscale hypergraph neural networks for trajectory
prediction with relational reasoning. In Proceedings of the
IEEE/CVF conference on computer vision and pattern recog-
nition, 6498–6507.
Xu, C.; Tan, R. T.; Tan, Y.; Chen, S.; Wang, Y. G.; Wang,
X.; and Wang, Y. 2023. Eqmotion: Equivariant multi-agent
motion prediction with invariant interaction reasoning. In
Proceedings of the IEEE/CVF conference on computer vision
and pattern recognition, 1410–1420.
Xu, P.; Hayet, J.-B.; and Karamouzas, I. 2022. Socialvae:
Human trajectory prediction using timewise latents. In Eu-
ropean Conference on Computer Vision, 511–528. Springer.
Yuan, Y.; Weng, X.; Ou, Y.; and Kitani, K. 2021. Agent-
former: Agent-aware transformers for socio-temporal multi-
agent forecasting. In 2021 IEEE/CVF International Confer-
ence on Computer Vision (ICCV), 9793–9803. IEEE.
Yue, Y.; Lucey, P.; Carr, P.; Bialkowski, A.; and Matthews,
I. 2014. Learning fine-grained spatial models for dynamic
sports play prediction. In 2014 IEEE international confer-
ence on data mining, 670–679. IEEE.
