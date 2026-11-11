<!-- source: library/preprints/arXiv/2026/2026 - Detecting Common Golfing Faults Using AI and Video-Derived Biomechanical Features - Martin et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.11515 -->
<!-- authors: Oliver Martin, Jeff Clark, Nawid Keshtmand -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-11; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Detecting Common Golfing Faults Using AI and Video-Derived Biomechanical Features

  MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI                                                                    1



  Detecting Common Golfing Faults Using AI
  and Video-Derived Biomechanical Features
  Oliver Martin                                                                         School of Engineering Mathematics
                                                                                        and Technology
  Jeff Clark                                                                            University of Bristol
                                                                                        Bristol, UK
arXiv:2611.11515v1 [cs.LG] 8 Nov 2026




  Nawid Keshtmand
  nawid.keshtmand@bristol.ac.uk




                                                                                 Abstract
                                            Understanding how an athlete moves can improve both technique and safety, yet
                                        outside the laboratory technique is still assessed by eye. We present a pipeline that detects
                                        named golf swing faults from ordinary video, without markers or calibration. Instead
                                        of learning end to end, it tracks body pose and the clubhead in a body-centred frame,
                                        and classifies the biomechanical quantities a coach would measure, such as the height
                                        of the clubhead above the swing plane, with shallow boosted trees. We demonstrate
                                        the approach on two common faults, coming over-the-top (OTT) and early-extension
                                        (EE). On 160 swings and 143 swings from public sources it detects OTT and EE with
                                        a cross-validated ROC-AUC of 0.975 and 0.911 respectively. Because every feature
                                        is a biomechanical quantity a coach already uses, measured at a known phase of the
                                        downswing, each decision can be traced to the signals and the moments of the swing
                                        that drove it. The signals the model relies on most are the same ones a coach checks
                                        when diagnosing these faults. The pipeline processes phone video on a consumer laptop
                                        in seconds, so it could feasibly be developed into an app for golfers of all abilities and
                                        extended to other sports in which technique is judged against a biomechanical reference.


  1                                     Introduction
  How an athlete moves determines how well they perform, how likely they are to be injured,
  and in some sports whether their technique is legal at all. In golf, swing kinematics can differ
  between professionals and amateurs [33], and the mechanics of the swing are implicated in
  low back pain, among the most common injuries in the sport [4, 15, 16]. Most of what is
  known about the technique comes from marker-based motion capture in the laboratory [2],
  which is precise but requires a capture volume, markers, and an operator, and may not be
  representative of typical outdoor golfing conditions. Outside the laboratory, coaches assess
  technique by eye against a small set of key swing parameters [22], and golfers without a
  coach are left to assess their own technique by filming themselves on a phone. A tool that
  serves professionals and amateurs alike must therefore work from a single ordinary video,
  with no markers, calibration, or special equipment.
© 2026. The copyright of this document resides with its authors.
It may be distributed unchanged freely in print or electronic forms.
2    MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI

    Computer vision and machine learning are increasingly used in sports analytics, from
player and ball tracking to motion analysis [24, 27], and markerless pose estimators [1] now
return body landmarks from phone video in real time. In golf, video has already been used for
swing sequencing, self-training, and skill assessment [10, 14, 17], yet academic studies and
consumer apps typically do not explicitly detect faults. In this paper we develop a pipeline
to detect two named faults in golf technique:
    1. Coming “over-the-top” (OTT): the club is thrown outward at the start of the down-
       swing, so the clubhead travels above the swing plane. Perhaps the most common fault
       among high-handicap golfers, it typically produces a pull or a slice [26]. Coaches
       diagnose it from the down-the-line view; so do we, from body pose and a tracked
       clubhead (Figure 1). It is a demanding test case: the decisive evidence is the club path,
       invisible to a pose estimator, judged over time against a biomechanical construct, the
       swing plane [5, 13].
    2. Early-extension (EE): the hips thrust toward the ball during the downswing, so the
       torso stands up out of its address posture (Figure 2). It typically produces a two-way
       miss, a block or a hook [25]. Coaches diagnose it from the same view, by whether the
       hips keep their distance from the ball; so do we.
    Our contributions are:
     • A golf fault detection pipeline for ordinary monocular video, combining MediaPipe
       pose estimation with a YOLO11 clubhead detector fine-tuned on 700 hand-labelled
       frames and a gated Kalman/RTS tracker that bridges detection dropouts, utilising di-
       rectly interpretable biomechanical features (Sec. 3).
     • A biomechanics-guided, phase-normalised trajectory representation of the downswing,
       demonstrated on 160 and 143 swing videos, on which it detects OTT with a cross-
       validated ROC-AUC of 0.975 (Table 1) and EE with 0.911 (Table 3).
     • Error and feature importance analyses for both faults; for OTT the single most infor-
       mative signal is clubhead height above the swing plane (Table 2).


2     Related work
Technique assessment from pose estimation. Action quality assessment regresses judges’
scores from whole-clip features, first from pose [20] and later from spatio-temporal RGB
networks [19]; it yields a global score rather than a decision about a named fault, and its
benchmarks are broadcast footage of judged sports such as diving. Pose-based coaching sys-
tems compare a user’s keypoints with exemplars and return corrective feedback [29]. Closer
to our task, named execution faults have been detected from monocular video with key-
point time series and compact classifiers: squat form classes from distance matrices [18],
aberrant executions of the military press from time-series classifiers [21], and race-walking
faults using pose estimation and machine learning models trained based on the judgements
of multiple qualified judges [23]. These studies share our regime of small, expert-labelled
datasets and interpretable features, but in each of them the fault is visible in the body alone,
whereas OTT is a fault of the club path. Skeleton-based recognisers [32] learn from key-
point sequences end to end but need far more than 160 clips, and pose inputs have the further
advantage of transferring to out-of-context actions where RGB models fail [30].
MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI                            3

Golf swing analysis from video. Monocular golf analysis has a long history in computer
vision research. In 2003 Gehrig et al. [7] recovered the clubhead trajectory from ordinary
swing video by fitting curves to club detections, and in 2005 Urtasun et al. [28] tracked the
golfer’s 3D pose through a swing with a learned motion model. Modern pipelines start from
a learned body-pose estimator. GolfDB [17] provides 1,400 professional swings annotated
with eight event frames and the SwingNet event detector; we draw our negative class cases
from it, and our top and impact detection plays the same role as its event detection, but from
pose and clubhead tracks rather than RGB frames. Pose-based coaching tools synchronise a
learner’s swing with an expert’s and visualise where the two diverge [14], estimate a golfer’s
handicap from video [10], or separate proficiency-related differences from individual style
using 2D pose and club detection in a single camera view [31]. 3D pose estimation from
monocular video has been found too inaccurate for golf kinematics [9]. Closest in task
to ours, Feng et al. [6] classify common swing errors from MediaPipe landmarks with an
attention-augmented LSTM, on 160 swings recorded under controlled conditions, and Kim
et al. [12] derive posture and tempo metrics and a projected club path from down-the-line
footage, without a labelled fault to detect. Because body-pose estimators do not see the
club, recent work fuses club and body keypoints to predict ball flight [11]; we also treat
the club as a first-class signal, with a dedicated detector and tracker, but use it to measure a
named fault against a swing-plane line. To our knowledge no prior work detects OTT and
EE automatically from monocular video.


3     Method
Our representation is guided by interpretable biomechanical signals rather than learned end
to end: we track the quantities a coach would measure and let a shallow classifier use them.
The downswing lasts a fraction of a second, and both faults are defined by sequential move-
ments, so features that summarise the whole swing discard most of the evidence. The
pipeline therefore runs per-frame body pose and clubhead detection (Sec. 3.1), maps the
coordinates into a body-centred, aspect-corrected frame (Sec. 3.2), detects the top of the
backswing and impact (Sec. 3.3), and resamples the downswing between them to a fixed
number of phase steps, as gait cycles are time-normalised in biomechanics [8]. Within that
window it tracks a small set of signals a coach would look at, including the height of the club-
head above a swing-plane line (Sec. 3.4.1), and classifies their trajectories with boosted trees
whose feature importance can be read off by signal and by phase (Sec. 3.4). EE detection
reuses every stage except the clubhead detector.


3.1    Body pose and clubhead detection
Body landmarks are generated with MediaPipe Pose (33 landmarks per frame, video mode,
model complexity 1) and are used by both fault models. The clubhead comes from a
YOLO11-L detector (25.3M parameters) fine-tuned for three classes (ball, handle, club-
head) on 700 hand-labelled frames (560 train, 140 validation) for 80 epochs at 1280 px.
Inference runs at 640 px with a confidence threshold of 0.10, followed by a recovery pass
that re-detects missed clubheads in a zoomed crop around the predicted position; this raises
the median fraction of frames with a detected clubhead from ∼62% to ∼86%. The raw
clubhead track is then cleaned and smoothed. Detections more than 6.0 robust deviations
(MAD) from the local median path, or more than 1.2 body heights from the lead wrist, are
4   MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI




           OTT
           non-OTT




Figure 1: Progression of an over-the-top (OTT) swing (top) and a non-OTT swing (bottom),
shown at the top of the backswing, one-third and two-thirds of the way through the down-
swing, and impact. Orange: tracked clubhead path so far (red dot: current position). Cyan:
the swing-plane line from the clubhead at address to the trail elbow. The OTT clubhead
loops outward and stays above the line, while the non-OTT clubhead drops onto the line
before impact.
           EE
           non-EE




Figure 2: Progression of an early-extension (EE) swing (top) and a non-EE swing (bottom),
shown at the top of the backswing, one-third and two-thirds of the way through the down-
swing, and impact. Orange: tracked hip path (red dot: start position). Cyan: the start line
from the back of the foot. The hips of the amateur (top) start slightly right and extend far
further than those of the experienced player (bottom).
MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI                             5

rejected. A constant-acceleration Kalman filter with confidence-scaled measurement noise
(measurement and process noise variances 4×10−4 and 5×10−3 ) and a 3.5σ innovation gate
is followed by a Rauch–Tung–Striebel (RTS) smoother, which bridges gaps of up to 15
frames. These settings are fixed across all OTT experiments. Figure 1 shows an OTT and
a non-OTT swing with the tracked clubhead path and the swing-plane line. The clubhead
detector and tracker serve the OTT model only: EE is a fault of the body rather than the club,
so its model works from the body landmarks alone.

3.2     Body-frame normalisation
Pose and detector coordinates arrive as fractions of frame width and height, which are differ-
ent units on any non-square frame. Let (x, y) be a keypoint’s horizontal and vertical image
position. We first multiply x by the frame aspect ratio W /H so that both axes are in frame
heights, which removes the angle distortion of portrait frames. Each keypoint is then mapped
to
                                      s (x − xhip )          yhip − y
                                 x̃ =               ,   ỹ =          ,                       (1)
                                           B                    B
where (xhip , yhip ) is the mid-hip, B is body height (the median shoulder-to-ankle distance over
the clip), and s = ±1 orients the horizontal axis by the backswing direction. This decouples
frame resolution, camera distance and the golfer’s size, and makes the signals invariant to
handedness and camera side.

3.3     Swing phases
Both faults are faults of the downswing, so both models work on the window from the top of
the backswing to impact, and both events must be located in every clip. Impact is the frame
at which the clubhead returns to its address height (the ball) and turns upward; anchoring
impact to the ball prevents a high finish, which comes after impact, from being mistaken for
the top. The top is defined as the lead wrist’s last up-to-down reversal before impact. It is
anchored to the wrist rather than the clubhead because the clubhead’s highest point is itself
shifted by the OTT move: with a clubhead-defined top, the top fell at a different phase in
each class. When the clubhead is tracked on fewer than half the frames, both events default
to the wrist trajectory, and the EE model, which does not track the clubhead, locates both
events from the wrist throughout.

3.4     Classifier and features
Biomechanical signals are extracted from each clip, as positions and as their frame-to-frame
differences, and classified with XGBoost.

3.4.1   Absolute position and change in position
The downswing is resampled to N=30 phase steps, and at each step we record a set of
signals a coach would look at, in the body frame (Sec. 3.2); their frame-to-frame differences
∆st = st − st−1 double the feature count. For OTT the eleven signals are lead wrist x, y; trail
elbow x, y; horizontal shoulder and hip separation; shoulder tilt; clubhead x, y; shaft angle;
and the signed height of the clubhead above the swing-plane line (Sec. 3.4.2), giving 330
position and 330 delta features. The last of these measures the defining sign of OTT directly,
6    MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI

a clubhead that stays above the swing plane through the downswing [26], but not decisively.
The other signals describe the hands, arms, club and torso around it and separate the classes
at different moments.
    For EE, a fault of the body rather than the club, the fifteen signals are the horizontal and
vertical displacement of the hips and of the shoulders from address, measured relative to
the mid-ankle; the head’s rise from address; horizontal hip separation; the x, y of both knees
and both ankles; and the spine angle, the forward tilt of the mid-hip to mid-shoulder line,
giving 450 position and 450 delta features. The hips’ horizontal displacement measures the
defining sign of EE directly, a pelvis that moves toward the ball during the downswing [25].
The other signals describe what the hip thrust does to the torso, head and legs, and where the
hips sit over the feet.

3.4.2    Swing plane
The plane line runs from the ball to the trail elbow, both taken at address in the first 0.5 s of
the clip, and is held fixed through the downswing (Figure 1). At address the clubhead rests
on the ball, so its tracked position there gives the ball point, avoiding the ball detector, which
on a driving range can jump between stray balls. Every swing begins the downswing well
above this line, so its early frames carry little information.

3.4.3    Trajectories rather than summaries
To assess the importance of temporal trajectories, we compare a model trained on the 30
separate phase steps with a baseline trained on scalar summaries of the whole downswing,
taken from the coaching definition of each fault (Sec. 4). The same eleven signals (fifteen
for EE) enter the trajectory model as positions alone, as frame-to-frame deltas alone, and as
both together (Sec. 5.1.1 and Sec. 5.2.1).


4       Experimental setup
Data. A dataset of 169 video clips was assembled for OTT detection. Positives, which
display the OTT fault, total 68 clips: 62 are amateur clips sourced from Reddit, 4 from
YouTube and 2 from other sources. Negatives (non-OTT, 101 clips) are 83 professional clips
from GolfDB (160×160 px, cropped to the annotated swing plus 15 frames either side), 13
amateur clips from TikTok, 4 from Reddit and 1 from YouTube. All clips share the down-
the-line camera angle and were checked for a consistent view and adequate lighting. Nine
clips (5 OTT, 4 non-OTT) whose detected downswing window (Sec. 3.3) does not actually
descend (cut off or flat) are discarded, since their phase-normalised features would describe
no real downswing, leaving 160 clips for all OTT experiments.
    For EE detection, 143 video clips were used, consisting of 60 amateur clips from the
OTT dataset graded independently for EE, 28 extra Reddit clips posted about EE, and 55
GolfDB professional clips, assumed free of it. In total 46 clips were positive for EE. These
143 clips remain after excluding 56 clips whose hip movement is not tracked effectively.

Classifier. Both fault models use the position and delta trajectory features of Sec. 3.4.1
(660 for OTT, 900 for EE), classified with XGBoost: depth-2 trees, 400 estimators,
                                                                       √           learning
rate 0.05, L2 regularisation λ =3, and column subsampling of min(1, 8/ d) for d features.
MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI                             7

Shallow trees keep the feature importance readable by signal and by phase. The same settings
are used for OTT and EE.

Scalar baseline. For comparison, baseline models for both faults were trained on a small
number of scalar features from the coaching definition of each fault. For OTT the baseline
scalar model utilises four features: the horizontal gap between the lead hand’s downswing
and backswing paths; how far the hand moves outward relative to how far it drops early in the
downswing; the early change in shaft angle; and the clubhead’s height above the swing plane,
weighted toward mid-downswing (Sec. 3.4.2). The EE scalar baseline uses three features:
how far the hips move toward the ball from top to impact; how far they sit past the ankles at
impact compared with address; and the loss of forward spine tilt from address to impact. For
both, an XGBoost classifier was trained with 200 trees of depth 3 and learning rate 0.1.

Evaluation protocol. Repeated stratified 5-fold cross-validation (3 repeats, seed 42), re-
porting mean ± s.d. of ROC-AUC over the 15 folds, and F1, precision and recall at a fixed
0.5 threshold. All results in Sec. 5 use this protocol unless stated otherwise; the ‘full model’
for OTT or EE is the one using both the positions and the deltas of the trajectory.


5       Results and discussion
5.1     Over-the-top (OTT)
5.1.1    Classification of “over-the-top” (OTT)
Table 1 summarises detection performance on the 160 swings. The full trajectory model (po-
sitions and deltas, 660 features) achieves the best performance and reaches a cross-validated
ROC-AUC of 0.975 ± 0.019. In practical terms, at the default 0.5 decision threshold, when
the model flags a swing as OTT it is correct in ∼93% of cases, and it detects ∼89% of the
OTT swings in the dataset. The four scalar features that summarise the whole downswing
reach only 0.874 ± 0.046, so resolving the downswing in time accounts for most of the im-
provement. Positions and deltas each perform well alone (AUC of 0.962 and 0.969) and are
complementary when combined.

             Features                Dim.       AUC           F1     Prec.    Rec.
             Scalar baseline            4   0.874 ± 0.046    0.760   0.813    0.740
             Trajectory: positions    330   0.962 ± 0.031    0.884   0.931    0.847
             Trajectory: deltas       330   0.969 ± 0.020    0.840   0.881    0.821
             Trajectory: pos+delta    660   0.975 ± 0.019    0.908   0.931    0.894
Table 1: OTT fault detection across 160 swings, 63 of them positive for OTT; ROC-AUC is
mean ± s.d. over 15 folds. F1, precision (“Prec.”) and recall (“Rec.”) are at the 0.5 decision
threshold; “Dim.” is the number of features.

    Figure 5 (Appendix A) shows the class-mean trajectory of each signal over the down-
swing. Clubhead height above the plane separates the classes most clearly, and the other
club signals separate over most of the downswing. The body signals separate at their own
moments: the lead wrist’s horizontal position differs from the start, and shoulder tilt and hip
separation differ slightly in the first half. The evidence is thus confined to particular phases,
8   MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI

which the phase-resolved representation preserves and a whole-swing summary would aver-
age away.

5.1.2   Feature importance by signal and phase
We examine which signals and which moments of the downswing the OTT model relies on
in two ways. The first trains the classifier on a single signal, its 30 positions and 30 deltas,
and reports the AUC that signal reaches alone (Table 2), a measure of how informative each
signal is regardless of the others. The second lays out a trained model’s feature importance,
the share of XGBoost’s gain attributed to each feature, as a map of signal against downswing
phase, for the full model and for a model trained on the body signals alone (Figure 3).

Single-signal models. The ranking in Table 2 follows the definition of the fault. Clubhead
height above the swing plane, the quantity a coach judges OTT by, is the strongest single
signal with an AUC of 0.940, within 0.035 of the full model (Table 1), and the other three
club signals follow: the clubhead’s horizontal and vertical position (0.875 and 0.867) and
the shaft angle (0.833). The body signals are weaker but far from uninformative. The lead
wrist’s horizontal position (0.820) outranks its height (0.689): in the down-the-line view the
horizontal axis runs across the target line, the direction in which an OTT move throws the
hands and club outward. Hip separation reaches 0.789 although it barely differs between
the classes in any third of the downswing; the trail elbow (0.693 and 0.687) and shoulder
tilt (0.650) add little alone, and the horizontal shoulder separation (0.571) is close to chance.
The body alone thus carries a usable signal of a fault defined by the club, and the full model’s
0.975 exceeds the strongest club and body signals, so the two are partly complementary.

             Signal                  AUC           Signal                AUC
             Head above plane    0.940 ± 0.026     Trail elbow x     0.693 ± 0.067
             Clubhead x          0.875 ± 0.057     Lead wrist y      0.689 ± 0.107
             Clubhead y          0.867 ± 0.043     Trail elbow y     0.687 ± 0.088
             Shaft angle         0.833 ± 0.073     Shoulder tilt     0.650 ± 0.083
             Lead wrist x        0.820 ± 0.071     Shoulder sep. x   0.571 ± 0.063
             Hip sep. x          0.789 ± 0.077
Table 2: Per-signal cross-validated ROC-AUC (mean ± s.d. over 15 folds, 160 swings) of
the OTT classifier trained on each signal individually, i.e. its 30 phase-step positions and 30
deltas (60 features), under the protocol of Sec. 4. “Head above plane” is the signed height of
the clubhead above the swing-plane line (Sec. 3.4.2); x and y are horizontal and vertical body-
frame coordinates (Sec. 3.2) and “sep.” the horizontal separation of the shoulders or hips.
Signals are sorted by AUC; the full model using all eleven signals reaches 0.975 (Table 1).



Importance maps. For the full model the importance map is sparse (Figure 3a): almost
all of the importance sits in clubhead height above the swing plane between about 65% and
80% of the downswing, with smaller contributions from the same signal in the last 20%
and from the clubhead’s and lead wrist’s horizontal position near impact. Contributions in
the first half are minimal: every swing starts the downswing well above the plane line, and
the classes diverge in the middle third and are furthest apart in the last. The body rows, by
contrast, are nearly empty, which appears to contradict Table 2, where the same body signals
MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI                                              9
                          Where the signal lives: 30-frame normalised downswing
      lead_wrist_x                                                                        0.10
      lead_wrist_y
     trail_elbow_x                                                                        0.08




                                                                                                 XGBoost gain importance
     trail_elbow_y
   shoulder_sep_x                                                                         0.06
         hip_sep_x
      shoulder_tilt                                                                       0.04
       clubhead_x
       clubhead_y
                                                                                          0.02
       shaft_angle
head_above_plane
                                                                                          0.00
                      0        20             40              60            80     100
                                    downswing progress (%) top -> impact
                                             (a) Full model


      Lead wrist x                                                                        0.0175
      Lead wrist y                                                                        0.0150




                                                                                                 Share of gain importance
     Trail elbow x                                                                        0.0125

     Trail elbow y                                                                        0.0100

  Shoulder sep. x                                                                         0.0075

                                                                                          0.0050
        Hip sep. x
                                                                                          0.0025
      Shoulder tilt
                      0        20             40              60            80     100
                                    Downswing progress (%), top to impact
                                           (b) Body pose only


Figure 3: Feature importance of the OTT classifier by signal (rows) and downswing phase
(columns; 0% is the top of the backswing, 100% impact), with each signal’s position and
delta features at a phase step combined into one cell. (a) Full model. (b) Body-pose-only
model (AUC 0.883). Colour scales differ between the panels.


reach AUCs between 0.57 and 0.82 on their own. The two views measure different things.
A single-signal AUC measures how much a signal carries by itself, whereas importance
measures how much the training loss fell when the trees split on a feature, and boosting
chooses at each split the feature that reduces the loss most. Clubhead height above the plane
separates the classes better than any body signal, so the trees split on it almost every time, and
the body signals, which see the same outward move from the body’s side and are correlated
with it, are rarely needed once it has been used. Their low importance means the club signal
carries their information more directly, not that they carry none: the table shows what each
signal knows, and the map what the model uses.
    Removing the club signals makes this visible. A body-only model trained on the seven
10    MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI

body signals (AUC 0.883) spreads its importance across signals and across the downswing
(Figure 3b): the lead wrist’s horizontal position from about 20% to 55% of the downswing
and again near impact, shoulder tilt between about 30% and 50%, hip separation at the very
start, and the wrist and trail-elbow heights in the second half. In both maps the evidence
is confined to particular phases rather than spread evenly, which is what a whole-swing
summary discards, and in both the signals and moments the model relies on are those a
coach looks for.

5.2     Early-extension (EE)
5.2.1   Classification of early-extension (EE)
The EE experiments test whether the same recipe transfers to a fault of the body rather than
the club. Table 3 presents detection of EE on the 143 clips. With position and delta features
the model reaches a cross-validated ROC-AUC of 0.911 ± 0.065 and, at the 0.5 threshold, an
F1 of 0.706 with precision 0.852 and recall 0.619: a swing flagged as EE is correct in ∼85%
of cases, but only ∼62% of EE swings are detected. As with OTT, precision exceeds recall,
but the gap is wider. The classes are more imbalanced (46 of 143 clips, against 63 of 160 for
OTT), which leaves the fixed 0.5 threshold on the conservative side; the AUC shows that the
ranking of swings is better than the thresholded figures suggest, and a lower threshold would
trade precision for recall. The fold-to-fold spread of AUC is also more than three times that
of OTT (±0.065 against ±0.019), as expected with ∼nine positives per test fold. As for
OTT, a trajectory beats scalar summaries of the same movement.

            Features                Dim.        AUC           F1     Prec.    Rec.
            Scalar baseline            3    0.726 ± 0.079    0.536   0.619    0.491
            Trajectory: positions    450    0.824 ± 0.061    0.539   0.672    0.465
            Trajectory: deltas       450    0.883 ± 0.080    0.727   0.853    0.649
            Trajectory: pos+delta    900    0.911 ± 0.065    0.706   0.852    0.619
Table 3: EE fault detection across 143 swings, 46 of them positive for EE; ROC-AUC is
mean ± s.d. over 15 folds. Trajectory rows use 15 hip, leg and torso signals. The 143 swings
exclude 56 clips whose hip movement was not tracked effectively (Sec. 4), so these results
are an upper bound. F1, precision (“Prec.”) and recall (“Rec.”) are at the 0.5 decision
threshold; “Dim.” is the number of features.

5.2.2   Feature importance by signal and phase
We examine which signals and moments of the downswing the EE model relies on in the
same two ways as for OTT (Sec. 5.1.2): the AUC each signal reaches alone (Table 4), and
the trained model’s share of gain by signal and downswing phase (Figure 4). As the EE
model works from body landmarks alone, there is one map rather than two.

Single-signal models. The ranking in Table 4 again follows the definition of the fault. The
hips’ horizontal displacement from address, the quantity a coach judges EE by (Sec. 1), is
the strongest signal at 0.910, as high as the full model’s 0.911 (Table 3), so the other fourteen
signals add nothing measurable to the ranking of swings. Those that follow are consequences
of the same movement: the spine angle (0.834) is the torso standing up out of its address tilt,
and since the body frame is centred on the mid-hip (Sec. 3.2), the trail and lead ankle x
MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI                            11

(0.826 and 0.727) are the horizontal offset between hips and feet, that is, how far the hips
have moved out over the ankles. The head’s rise (0.687) and three knee coordinates (0.605
to 0.641) carry less, and the remaining seven signals are close to chance (0.516 to 0.584),
among them the vertical displacement of the hips and shoulders, the shoulders’ horizontal
displacement and hip separation, which reached 0.789 for OTT. EE is therefore visible as the
hips moving toward the ball under the shoulders and over the feet, and as the posture change
that follows.

      Signal                      AUC           Signal                          AUC
      Hip ∆x from address     0.910 ± 0.057     Hip ∆y from address         0.584 ± 0.098
      Spine angle             0.834 ± 0.090     Shoulder ∆x from address    0.563 ± 0.113
      Trail ankle x           0.826 ± 0.045     Lead ankle y                0.559 ± 0.083
      Lead ankle x            0.727 ± 0.113     Hip sep. x                  0.552 ± 0.105
      Head ∆y from address    0.687 ± 0.102     Shoulder ∆y from address    0.531 ± 0.073
      Trail knee x            0.641 ± 0.079     Lead knee x                 0.530 ± 0.109
      Trail knee y            0.611 ± 0.103     Trail ankle y               0.516 ± 0.091
      Lead knee y             0.605 ± 0.064
Table 4: Per-signal cross-validated ROC-AUC (mean ± s.d. over 15 folds, 143 swings) of
the EE classifier trained on each signal individually, i.e. its 30 phase-step positions and 30
deltas (60 features), under the protocol of Sec. 4. “∆x” and “∆y” are horizontal and vertical
displacement from the address position, relative to the mid-ankle; “Spine angle” is the for-
ward tilt of the mid-hip to mid-shoulder line; the other x and y are horizontal and vertical
body-frame coordinates (Sec. 3.2) and “sep.” the horizontal separation of the hips. Signals
are sorted by AUC; the full model using all fifteen signals reaches 0.911 (Table 3).


Importance maps. Figure 4 shows what the EE model relies on. Through the first three
quarters of the downswing importance is low and scattered, with only hip separation and the
knees carrying weak, isolated importance in its middle. Importance concentrates at 80–100%
of the downswing in the hips’ horizontal displacement from address, the spine angle and the
rise of the head, with the horizontal position of the trail ankle alongside. This is the fault as
a coach defines it (Sec. 1) [25]: the hips move toward the ball and the torso stands up out of
its address posture, and the evidence appears in the approach to impact rather than at the top.
As for OTT, the decisive signals are confined to one part of the downswing, here its last fifth,
which the phase-resolved representation keeps separate and a whole-swing summary would
average away. The two views agree: the signals that carry the importance in the last fifth are
four of the five strongest single signals in Table 4, and the rows that stay dark throughout are
the signals near chance. That the gain is spread over the spine, ankle and head rows while
the full model is no better than the hips’ displacement alone follows the reading of gain in
Sec. 5.1.2: correlated views of one movement share it.

5.3    Why OTT is detected better than EE
EE is harder to detect than OTT for three reasons. First, its defining movement is small
and overlaps between classes: at impact, the median EE swing has moved its hips 0.033
body heights toward the ball against 0.003 for non-EE amateurs, but a quarter of EE swings
move less than a quarter of non-EE swings, whereas clubhead height above the plane differs
by 0.32 body heights in the last third of the downswing. Second, the clubhead is tracked
12     MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI

      Hip Δx from address
      Hip Δy from address                                                                0.0175

                Hip sep. x
              Lead knee x                                                                0.0150

              Lead knee y
                                                                                         0.0125
              Trail knee x




                                                                                              Share of gain importance
              Trail knee y
                                                                                         0.0100
             Lead ankle x
             Lead ankle y
                                                                                         0.0075
             Trail ankle x
             Trail ankle y
                                                                                         0.0050
Shoulder Δx from address
Shoulder Δy from address
                                                                                         0.0025
              Spine angle
     Head Δy from address
                                                                                         0.0000
                             0   20             40            60              80   100
                                      Downswing progress (%), top to impact


Figure 4: Feature importance of the EE classifier of Table 3 (143 clips, AUC 0.911) by signal
(rows) and downswing phase (columns; 0% is the top of the backswing, 100% impact), with
each signal’s position and delta features at a phase step combined into one cell. The model
sees body landmarks only; the fifteen signals are defined in Table 4. Importance concentrates
at 80–100% of the downswing in the hips’ horizontal displacement from address, the spine
angle and the rise of the head.



directly, while the hip is a joint centre inferred by the pose estimator. Third, EE is graded on
a continuum and has fewer positives.




5.4       Runtime

Run time was assessed on an Apple M2 laptop (Table 5). With the YOLO11-L detector
used throughout, the forward pass takes 281 ms/frame, and full clubhead tracking of a 104-
frame clip, including video decoding and the recovery pass, takes 12.7 s (42.3 s on the CPU).
A phone clip can therefore be scored locally on consumer hardware within seconds of the
swing, while it is still fresh; because OTT and EE are properties of the whole downswing,
feedback is per swing rather than per frame. The smaller YOLO11-S and YOLO11-N vari-
ants run at 38 and 56 frames per second, which would allow near-instantaneous feedback
once their detection accuracy has been validated.
MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI                          13

                  Detector       Device         ms/frame    fps   3 s clip (s)
                  YOLO11-L†      CPU                1374    0.7        123.7
                  YOLO11-L†      GPU (MPS)           281    3.6         25.3
                  YOLO11-S       GPU (MPS)            26    38            2.3
                  YOLO11-N       GPU (MPS)            18    56            1.6
Table 5: Detector forward-pass time per frame on an Apple M2 laptop for a synthetic
640×640 input. “fps” is frames processed per second (1000/ms); typical video is 30 fps.
“3 s clip” is the processing time for 90 frames. † The detector used in all experiments; the
smaller S (“small”) and N (“nano”) variants were timed only and their detection accuracy is
untested.


6    Conclusion
We have presented a pipeline that detects named golf swing faults from a single ordinary
video, with no markers, calibration or special equipment, and applied it to OTT and EE.
Rather than learning end to end, it tracks the biomechanical quantities a coach would mea-
sure, including the height of the clubhead above a swing-plane line, in a body-centred frame,
and shallow boosted trees on these trajectories detect OTT and EE with a cross-validated
ROC-AUC of 0.975 and 0.911 respectively. What the models rely on agrees with coaching
practice: for OTT the most informative signals are the clubhead’s height above the swing
plane and its position, and the classes separate at distinct moments of the downswing that a
whole-swing summary averages away, while for EE the movement of the hips is the driving
factor. Because the signals are the ones a coach uses, a detection can be explained to the
golfer in the same terms, which is what a coaching or injury-prevention tool needs. The
study has several limitations. The dataset is small, only two faults are covered, and the clips
come from a single down-the-line view in which hip rotation is foreshortened. Fault labels
are partly confounded with skill level: most non-faulty clips are professional swings from
GolfDB, while nearly all positives are amateurs, so the model may partly learn differences
between professional and amateur swings rather than the fault itself. The static-frame probe
(Appendix B) suggests it does not rely heavily on pre-fault cues, but does not rule the con-
found out. No qualified coach selected or graded the clips, so some labels are likely to be
noisy, particularly for EE, which is graded on a continuum. Future work will expand the
dataset from public sources, with more non-faulty amateur swings so the skill-level con-
found can be tested directly, have multiple qualified coaches grade the clips and report their
inter-rater agreement, and assess further faults. Single-image 3D body reconstruction such as
SAM 3D [3] may recover the rotations that a 2D view hides. Clubhead tracking already runs
in about 13 s per clip on an Apple M2, so an app that returns fault feedback from a phone
recording is within reach, and the same recipe of coach-defined signals, phase-normalised
over a detected movement window, applies to other sports in which technique is judged
against a biomechanical reference.

Acknowledgments OM was funded by the University of Bristol Faculty of Science and
Engineering Summer Internship Scheme 2026.
14   MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI

References
 [1] Valentin Bazarevsky, Ivan Grishchenko, Karthik Raveendran, Tyler Zhu, Fan Zhang,
     and Matthias Grundmann. BlazePose: On-device real-time body pose tracking. arXiv
     preprint arXiv:2006.10204, 2020.

 [2] Maxime Bourgain, Philippe Rouch, Olivier Rouillon, Patricia Thoreux, and Christophe
     Sauret. Golf swing biomechanics: A systematic review and methodological recom-
     mendations for kinematics. Sports, 10(6):91, 2022.

 [3] Xingyu Chen, Fu-Jen Chu, Pierre Gleize, Kevin J Liang, Alexander Sax, Hao Tang,
     Weiyao Wang, Michelle Guo, Thibaut Hardin, Xiang Li, et al. SAM 3D: 3Dfy any-
     thing in images. In Proceedings of the IEEE/CVF Conference on Computer Vision and
     Pattern Recognition, pages 7220–7232, 2026.

 [4] Michael H Cole and Paul N Grimshaw. The biomechanics of the modern golf swing:
     implications for lower back injuries. Sports Medicine, 46(3):339–351, 2016.

 [5] Simon GS Coleman and Andrew J Rankin. A three-dimensional examination of the
     planar nature of the golf swing. Journal of Sports Sciences, 23(3):227–234, 2005.

 [6] Chengwei Feng, Boris Bačić, and Weihua Li. SCA-LSTM: A deep learning approach
     to golf swing analysis and performance enhancement. In International Conference on
     Neural Information Processing, pages 72–86. Springer, 2024.

 [7] Nicolas Gehrig, Vincent Lepetit, and Pascal Fua. Visual golf club tracking for enhanced
     swing analysis. In Proceedings of the British Machine Vision Conference 2003, 2003.

 [8] Nathaniel E Helwig, Sungjin Hong, Elizabeth T Hsiao-Wecksler, and John D Polk.
     Methods to temporally align gait cycle data. Journal of Biomechanics, 44(3):561–566,
     2011.

 [9] Christian Keilstrup Ingwersen, Janus Nørtoft Jensen, Morten Rieger Hannemose, and
     Anders Bjorholm Dahl. Evaluating current state of monocular 3D pose models for golf.
     In Northern Lights Deep Learning Workshop 2023. Septentrio Academic Publishing,
     2023.

[10] Christian Keilstrup Ingwersen, Artur Xarles, Albert Clapés, Meysam Madadi,
     Janus Nørtoft Jensen, Morten Rieger Hannemose, Anders Bjorholm Dahl, and Sergio
     Escalera. Video-based skill assessment for golf: Estimating golf handicap. In Pro-
     ceedings of the 6th International Workshop on Multimedia Content Analysis in Sports,
     pages 31–39, 2023.

[11] Seunghyeon Jung, Minseok Kim, Hyeonjin Kim, Seungwon Jeong, Yunseok Lee, Yunji
     Kim, Hyunse Lee, Seoyoung Hong, Gyumin Choi, Jaerim Choi, et al. Explainable
     graph-based golf swing analysis integrating club and body keypoints for ball flight
     outcome prediction. Applied Sciences, 16(8):3813, 2026.

[12] Theodore T Kim, Mohamed A Zohdy, and Michael P Barker. Applying pose estimation
     to predict amateur golf swing performance using edge processing. IEEE Access, 8:
     143769–143776, 2020.
MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI                       15

[13] Young-Hoo Kwon, Christopher S Como, Kunal Singhal, Sangwoo Lee, and Ki Hoon
     Han. Assessment of planarity of the golf swing based on the functional swing plane
     of the clubhead and motion planes of the body points. Sports Biomechanics, 11(2):
     127–148, 2012.
[14] Chen-Chieh Liao, Dong-Hyun Hwang, and Hideki Koike. AI Golf: Golf swing analysis
     tool for self-training. IEEE Access, 10:106286–106295, 2022.
[15] David M Lindsay and Anthony A Vandervoort. Golf-related low back pain: a review
     of causative factors and prevention strategies. Asian Journal of Sports Medicine, 5(4):
     e24289, 2014.
[16] Andrew McHardy, Henry Pollard, and Kehui Luo. Golf injuries: a review of the litera-
     ture. Sports Medicine, 36(2):171–187, 2006.
[17] William McNally, Kanav Vats, Tyler Pinto, Chris Dulhanty, John McPhee, and Alexan-
     der Wong. GolfDB: A video database for golf swing sequencing. In 2019 IEEE/CVF
     Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), pages
     2553–2562. IEEE, 2019.
[18] Ryoji Ogata, Edgar Simo-Serra, Satoshi Iizuka, and Hiroshi Ishikawa. Temporal dis-
     tance matrices for squat classification. In 2019 IEEE/CVF Conference on Computer
     Vision and Pattern Recognition Workshops (CVPRW), pages 2533–2542. IEEE, 2019.
[19] Paritosh Parmar and Brendan Tran Morris. What and how well you performed? a mul-
     titask learning approach to action quality assessment. In 2019 IEEE/CVF Conference
     on Computer Vision and Pattern Recognition (CVPR), pages 304–313. IEEE, 2019.
[20] Hamed Pirsiavash, Carl Vondrick, and Antonio Torralba. Assessing the quality of ac-
     tions. In European Conference on Computer Vision, pages 556–571. Springer, 2014.
[21] Ashish Singh, Antonio Bevilacqua, Thach Le Nguyen, Feiyan Hu, Kevin McGuinness,
     Martin O’Reilly, Darragh Whelan, Brian Caulfield, and Georgiana Ifrim. Fast and
     robust video-based exercise classification via body pose tracking and scalable multi-
     variate time series classifiers. Data Mining and Knowledge Discovery, 37(2):873–912,
     2023.
[22] Aimée Smith, Jonathan Roberts, Eric Wallace, Pui Wah Kong, and Steph Forrester.
     Golf coaches’ perceptions of key technical swing parameters compared to biomechan-
     ical literature. International Journal of Sports Science & Coaching, 10(4):739–755,
     2015.
[23] Tomohiro Suzuki, Kazuya Takeda, and Keisuke Fujii. Automatic detection of faults
     in simulated race walking from a fixed smartphone camera. International Journal of
     Computer Science in Sport, 23(1):22–36, 2024.
[24] Graham Thomas, Rikke Gade, Thomas B Moeslund, Peter Carr, and Adrian Hilton.
     Computer vision for sports: Current applications and research topics. Computer Vision
     and Image Understanding, 159:3–18, 2017.
[25] Titleist Performance Institute. Early extension. https://www.mytpi.com/
     improve-my-game/swing-characteristics/early-extension,
     2026. Accessed 21 October 2026.
16   MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI

[26] Titleist Performance Institute. Over the top. https://www.mytpi.com/
     improve-my-game/swing-characteristics/over-the-top,             2026.
     Accessed 21 October 2026.

[27] Joseph Turner, Jeff Clark, and Nawid Keshtmand. Markerless pose estimation for re-
     sistance training technique assessment. arXiv preprint arXiv:2608.24384, 2026.
[28] Raquel Urtasun, David J Fleet, and Pascal Fua. Monocular 3D tracking of the golf
     swing. In 2005 IEEE Computer Society Conference on Computer Vision and Pattern
     Recognition (CVPR’05), volume 2, pages 932–938. IEEE, 2005.

[29] Jianbo Wang, Kai Qiu, Houwen Peng, Jianlong Fu, and Jianke Zhu. AI Coach: Deep
     human pose estimation and analysis for personalized athletic training assistance. In
     Proceedings of the 27th ACM International Conference on Multimedia, pages 374–
     382, 2019.
[30] Philippe Weinzaepfel and Grégory Rogez. Mimetics: Towards understanding human
     actions out of context. International Journal of Computer Vision, 129(5):1675–1690,
     2021.
[31] Kota Yamamoto, Yumiko Hasegawa, Tomohiro Suzuki, Hiroo Suzuki, Hiroko Tanabe,
     and Keisuke Fujii. Extracting proficiency differences and individual characteristics in
     golfers’ swing using single-video markerless motion analysis. Frontiers in Sports and
     Active Living, 5:1272038, 2023.
[32] Sijie Yan, Yuanjun Xiong, and Dahua Lin. Spatial temporal graph convolutional net-
     works for skeleton-based action recognition. In Proceedings of the AAAI Conference
     on Artificial Intelligence, volume 32, 2018.

[33] N Zheng, SW Barrentine, GS Fleisig, and JR Andrews. Kinematic analysis of swing
     in pro and amateur golfers. International Journal of Sports Medicine, 29(6):487–493,
     2008.
MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI                       17

A     Class-mean trajectories for OTT




Figure 5: Class-mean trajectories of the eleven OTT signals over the downswing (0% is the
top of the backswing, 100% impact), OTT (red) against non-OTT (blue), with shaded bands
around each mean showing the standard deviation. Positions are body-frame coordinates in
body heights (Sec. 3.2), the shaft angle is in degrees, and “head_above_plane” is the signed
height of the clubhead above the swing-plane line (Sec. 3.4.2).
18   MARTIN, CLARK, KESHTMAND: DETECTING COMMON GOLFING FAULTS USING AI

B     Comparison of our model to a learned video model
Another alternative to tracking is a learned video model. We tested a Kinetics-pretrained
R3D-18 as a frozen feature extractor on each downswing. It reaches AUC 0.967, close to
the XGBoost model. To test what each model relies on, we freeze every test swing at the
top of the backswing, before the fault occurs, and re-score with each model. The R3D-18
still scores 0.946, separating the classes from appearance. Our model falls to 0.547, close
to chance. Frame differences of the RGB video do not remove the shortcut either (0.951).
On an earlier version of the data, Grad-CAM on the same backbone fed rendered skeleton
frames placed its attention on the torso rather than the club or arms.

     Model                                Normal             Frozen at top of backswing
                                                          re-scored      single-frame model
     R3D-18 (frozen) + log. reg., RGB   0.967 ± 0.028   0.946 ± 0.040     0.960 ± 0.034
     Ours (XGBoost, pos+delta)          0.975 ± 0.019   0.547 ± 0.077     0.752 ± 0.055
Table 6: Static-frame probe (CV ROC-AUC, 160 swings, 15 folds). “Re-scored”: trained
on real swings, tested on swings frozen at the top of the backswing. “Single-frame model”:
trained and tested on that frame alone.
