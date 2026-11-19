<!-- source: library/preprints/arXiv/2026/2026 - Training-free motion statistics match self-supervised behavior encoders - Chen.pdf -->
<!-- item: https://arxiv.org/abs/2611.24792 -->
<!-- authors: Ziwen Chen -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-19; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Training-free motion statistics match self-supervised behavior encoders

                                           Training-free motion statistics match self-supervised behavior encoders
                                                                                              Ziwen Chen
                                                                                  University of Illinois Urbana-Champaign
                                                                                          ziwenc3@illinois.edu



                                         Abstract                                                          rectly. Do these encoders beat the hand-built ingredients
                                                                                                           they are built from, when both get the same classifier
                                         Self-supervised encoders for animal behavior are often            and the same budget of numbers per frame?
arXiv:2611.24792v1 [cs.CV] 18 Nov 2026




                                         trained on, or fed, hand-built movement features. We                 We answer it with a deliberately plain baseline. For
                                         ask whether they beat those ingredients when compared             each frame we compute a few dozen generic measure-
                                         fairly. A training-free representation, made of generic           ments of position, speed, turning, body shape and the
                                         per-frame measurements summarized over fixed time win-            relation between animals. Each is summarized over fixed
                                         dows and reduced with PCA, is compared with retrained             time windows from half a second to the whole clip, and
                                         and released encoders (BAMS, hBehaveMAE) under a                  PCA reduces the result to the benchmark’s budget. Noth-
                                         preregistered protocol: frozen representations of equal           ing is trained by gradient descent, and no label is used
                                         size and one shared classifier. On CalMS21 it reaches 85.8        to build the representation.
                                         macro F1 against 82.4 for the best encoder, ties with four           We compare it with retrained and released self-
                                         labelled videos, and leads when the annotator changes             supervised encoders under a frozen-representation pro-
                                         or new behaviors must be learned from a few videos; the           tocol. Every method gives the same number of values
                                         reading holds for encoders retrained with three seeds.            per frame, and the same small classifier is trained on
                                         On the MABe22 mouse triplets it scores 83.7 against 80.3          top. To keep the comparison honest we preregistered it:
                                         for the released hBehaveMAE (gap +3.4, 95% interval               before any test score existed, each test’s design and the
                                         +2.1 to +4.7). On a second species, the MABe22 fly                rule for reading it were written down and hashed, and
                                         groups, the same recipe scores 51.6 mean F1 over 50               every later choice was made on training data only.
                                         tasks against 48.2 for BAMS, the best published method.              The training-free features match or beat the encoders
                                         On Shot7M2, the synthetic basketball benchmark built              in every test, on mice, on flies and on a simulated human:
                                         by hBehaveMAE’s authors, it scores 68.8 against 64.7 for           • CalMS21 Task 1. 85.8 macro F1 with all labels,
                                         hBehaveMAE, the best method in that paper, though                     against 82.4 for hBehaveMAE and 78.3 for BAMS,
                                         hBehaveMAE remains better on the shortest movements.                  and a tie with BAMS at 5% of labels (61.1 against
                                         Short time windows carry most of the result. Raw key-                 63.4). Two further training runs of each encoder give
                                         points in each body’s own frame, summarized over the                  the same picture.
                                         same windows, already match or beat the encoders on                • CalMS21 Tasks 2 and 3. With a new annotator,
                                         both mouse datasets and on Shot7M2; on the fly groups                 or a new behavior learned from one to four labelled
                                         they fall short, and the measurements add 5.3 points.                 videos, the features lead both encoders (77.9 against
                                         On these benchmarks, current behavior encoders have                   71.7, and 37.6 against 33.9).
                                         yet to beat the hand-built features they learn from, and           • MABe22 mouse triplets. 83.7 on the clip-level
                                         such baselines should be reported alongside them.                     tasks, against 80.3 for the authors’ released hBe-
                                                                                                               haveMAE (gap +3.4 [+2.1, +4.7]) and above every
                                                                                                               method in that paper’s table.
                                         1     Introduction                                                 • MABe22 fly groups. On a second species, 51.6
                                                                                                               mean F1 over 50 tasks, against 48.2 for BAMS, the
                                         Machine learning for animal behavior has moved from                   best published method.
                                         hand-built features to representations learned without la-         • Shot7M2. On a simulated basketball player, 68.8
                                         bels. Recent self-supervised encoders such as BAMS [1],               against 64.7 for hBehaveMAE on its own benchmark;
                                         hBehaveMAE [11] and MICE [12] learn from tracked                      the lead comes from episode-level activities, while
                                         poses and report gains on the standard mouse bench-                   hBehaveMAE is better on the shortest movements.
                                         marks. Several of them are trained on, or fed, hand-built          • What carries it. Short time windows do most of
                                         movement features: BAMS learns to predict histograms                  the work, and 19 of the 23 measurements already
                                         of future movement features, and its mouse recipe takes               beat both encoders with all labels.
                                         hand-built pose features as input.                                 • Raw keypoints. In each body’s own frame and
                                            This raises a question the literature has not tested di-           summarized the same way, raw keypoints match or


                                                                                                       1
    beat the encoders on both mouse datasets and on
                                                                   Table 1: The 23 CalMS21 measurements, in seven groups.
    Shot7M2, 1.0 to 2.8 points below the measurements
    with all labels. On the fly groups the measurements            Group       Measurements
    add 5.3 points, and they are what puts the recipe              Distance    distance between the two body centres; one
    above BAMS.                                                                minus that distance; contact (below one body
   Our contributions are: (1) a training-free represen-                        length)
tation that matches or beats published self-supervised             Speeds      each mouse’s centre speed
encoders on the standard mouse benchmarks; (2) a pre-              Approach    closing speed; each mouse’s speed toward the
registered, frozen-representation protocol for comparing                       other
                                                                   Activity    per mouse, the share of still frames (below 0.25
behavior representations fairly; (3) an analysis of which
                                                                               body lengths per second) and the rate of switch-
ingredients carry the result, including raw keypoints in
                                                                               ing between still and moving, over 0.5 s; the
place of the measurements on four benchmarks; and                              correlation of the two speeds over 0.5 s
(4) evidence that the recipe carries over to a second              Nose        each mouse’s nose to the nearest keypoint of the
species and to a simulated human, where it beats the                           other
best published encoders on the MABe22 fly groups and               Heading     whether each mouse’s head points at the other
on Shot7M2.                                                                    (cosine); how fast each head turns
                                                                   Posture     each mouse’s body length relative to its median;
                                                                               nose speed minus body speed
2    Related work
Self-supervised behavior representations. Several                  nine datasets [17]. Random convolutional kernels with a
methods learn frame-level embeddings from tracked poses            linear classifier matched state-of-the-art time-series clas-
without behavior labels and evaluate them with small               sification at a small fraction of the cost (ROCKET [2]),
classifiers on frozen features. TREBA [14] trains tra-             and 22 canonical features summarize a series at a modest
jectory embeddings with self-supervised tasks that do-             cost in accuracy (catch22 [7]). In deep metric learning,
main experts write as programs (“task programming”).               reported gains shrank to marginal ones under careful
BAMS [1] uses two temporal convolutional networks for              evaluation [9]. Our study does the same for behavior
short- and long-term dynamics, trained to predict his-             representations, with the comparison preregistered.
tograms of future actions and to stay consistent across
                                                                   Benchmarks. CalMS21 [13] and MABe22 [15] de-
time, and it ranked first on both MABe 2022 trajec-
                                                                   fine the tasks and splits we use for mice and flies,
tory leaderboards. hBehaveMAE [11] learns a hierar-
                                                                   and Shot7M2 [11] for a simulated basketball player.
chy of masked-autoencoder representations from pose.
                                                                   MABe22’s own evaluator trains linear models on frozen
MICE [12] is a hierarchical foundation model for mouse
                                                                   embeddings, the protocol we use throughout.
behavior pretrained on six mouse datasets; on CalMS21
it reports 83.28 macro F1 with a probe on frozen features,
and 84.56 with multi-dataset pretraining. Unsupervised             3      Method: a training-free repre-
methods such as B-SOiD [4], VAME [8] and Keypoint-
MoSeq [16] instead segment behavior into discrete motifs.                 sentation
Hand-built behavior features. Supervised behavior                  The representation has three steps: per-frame measure-
classifiers have long used hand-built features of pose and         ments, statistics of each measurement over fixed time
of the relations between animals. JAABA [5] turns a few            windows, and a linear reduction fitted without labels.
labelled frames into classifiers for flies, mice and larvae.
MARS [10] classifies mouse social behavior with random             Per-frame measurements. For CalMS21 (two mice,
forests on hand-designed pose features, and SimBA [3]              seven keypoints each, 30 Hz) we use 23 measurements
builds explainable classifiers from features such as move-         (Table 1). Keypoints are first smoothed with a three-
ment, posture and proximity. CalMS21’s poses come                  frame median filter. Distances are in body lengths, the
from MARS, and its Task 1 training and test videos                 clip’s median nose-to-tail distance, and speeds in body
match those of MARS’s classifiers. In a study of visual            lengths per second, so camera scale drops out. No mea-
context, Li et al. [6] found MARS’s hand-engineered fea-           surement uses the arena’s position or axes.
tures ahead of BAMS and hBehaveMAE on CalMS21,                     Window statistics. For each measurement we keep
and treated this as an exception owed to features en-              its value at the frame and, over centred windows of 0.5,
gineered for two-mouse recordings. Our representation              2, 8 and 30 seconds, its mean, its standard deviation and
follows this tradition, but its measurements are generic,          an 8-bin histogram. The bin edges are quantiles of that
it defines no behavior, and it uses no labels.                     measurement on training data.
Simple baselines that hold up. One-layer linear                    Reduction. The statistics are standardized and re-
models beat Transformer-based long-term forecasters on             duced with PCA to the benchmark’s budget of numbers


                                                               2
per frame (128 on CalMS21 and the MABe22 mice). Mo-
                                                                 Table 2: CalMS21 Task 1, macro F1 on the 19 test videos,
ments and PCA are fitted on unlabelled and training
                                                                 with 95% intervals, for encoders trained with seed 0 and
videos without labels, then frozen.
                                                                 averaged over three training seeds. BAMS is the version
Layout. Four layouts were defined before any scoring:            fed our measurements, its best on training videos; the
one PCA or two (short and long windows apart), each              authors’ mouse recipe is adapted to CalMS21’s seven
with or without the histograms. The layout is chosen by          keypoints.
cross-validation on training data only. CalMS21 chose            Method                             All labels       5% of labels
two PCAs with histograms: 64 numbers from the frame
                                                                 Training-free features (ours)   85.8 [82.4, 88.5] 61.1 [57.0, 64.1]
value and the two short windows, and 64 from the two             hBehaveMAE                      82.4 [78.2, 85.3] 45.5 [41.1, 49.1]
long windows.                                                    BAMS                            78.3 [73.9, 81.3] 63.4 [58.4, 64.9]
                                                                 BAMS, authors’ mouse recipe     54.6 [47.5, 56.9] 28.4 [25.3, 29.3]
MABe22 mouse triplets. The same recipe uses 89
measurements written for three mice: per-mouse speeds,           hBehaveMAE, mean of 3 seeds           82.4              45.4
                                                                 BAMS, mean of 3 seeds                 77.8              63.1
body lengths, turning and position in the arena, plus
pairwise distances, closing speeds, facing and approach.
Per-mouse and pairwise values are sorted across animals,
                                                                 an NVIDIA GeForce RTX 4080 SUPER GPU (16 GB).
so the representation does not depend on mouse order.
The windows add the whole 60-second clip, because the            Fixed before scoring. The 23 CalMS21 measurements
benchmark’s clip-level labels are defined per clip. Every-       were fixed on 11 November 2026, with a file hash, before
thing is fitted on the 1,600 user-train clips, and cross-        any CalMS21 score had been computed. Every test used
validation there chose two PCAs without histograms in            the file with that same hash. The fly and Shot7M2
the short half.                                                  measurements were written for their tests and hashed
                                                                 before any score on those datasets existed.
MABe22 fly groups. For groups of up to 11 flies at
150 Hz we wrote 24 generic measurements per fly (speeds,
turning, body and wing posture, leg reach, and relations         4     Evaluation protocol
to the nearest fly), pooled over flies by mean, spread,
minimum and maximum, plus four group measurements:               Frozen representations, one classifier. Every
100 numbers per frame. Windows run from 0.5 s to the             method gives the same number of values per frame, and
whole 30 s clip, and PCA reduces to the benchmark’s              the encoders stay frozen. On CalMS21 the same classifier
limit of 256. Everything is fitted on the 426 user-train         is trained on top of each method: a linear layer or a one-
clips, and cross-validation there chose one PCA of means         hidden-layer MLP with 512 units, with or without class
and spreads.                                                     balancing, over a fixed grid of L2 penalties (14 settings).
Shot7M2. For one simulated 3D body (26 joints, 30 Hz)            Each method’s setting, and its own variant (for example
we wrote 40 measurements: body size; pelvis and head             which hBehaveMAE level), is chosen by cross-validation
height; for each wrist and ankle, its position in the            on the 70 training videos only. Each method is then
body’s frame, its speed and its vertical speed; elbow and        scored once on the 19 official test videos, as macro F1
knee angles and their rates; trunk lean and twist; signed        over attack, investigation and mount.
turning speed; hand and foot gaps; and stillness. Left           Label budgets. We use all 70 training videos, and a
and right limbs are kept apart. The windows are those            5% budget: ten fixed sets of four training videos, with
of the MABe22 mice, PCA reduces to the benchmark’s               the scores averaged.
64 numbers, and cross-validation on the 1,280 user-train
episodes chose two PCAs of means and spreads.                    Encoders. BAMS and hBehaveMAE were retrained
                                                                 with their authors’ code and recipes on CalMS21’s unla-
How much is hand-built. Each measurement set is a                belled and training videos: hBehaveMAE for 200 epochs,
few dozen ordinary kinematic quantities computed from            BAMS for 500. BAMS was trained twice, once on key-
the tracked points: positions, speeds, distances, angles         points with the authors’ template and once fed our
and heights, of the kind found in any behavior-analysis          23 measurements; the second scored higher on train-
toolkit. None of them defines a behavior, and none uses          ing videos and is the one reported. hBehaveMAE is
a label. Each dataset’s per-frame measurement function           read at each of its three levels, and the best on training
is under 100 lines of Python (46 for CalMS21, 82 for             videos is used. On MABe22 we used the authors’ released
the MABe22 mice, 78 for the flies, 43 for Shot7M2).              hBehaveMAE checkpoint and the benchmark’s own eval-
Fitting the window statistics and PCA takes minutes on           uator, which trains ridge classifiers with three seeds and
a CPU; training BAMS on CalMS21 alone took us 5 to               takes a majority vote. There we report clip-level F1
6 hours on a GPU. Section 6 measures how much the                (mouse strain, lights on or off) and frame-level F1. On
measurements add over raw keypoints summarized the               the fly groups we used the MABe 2022 public evaluator
same way. All runs used one workstation with an Intel            and compare with BAMS’s published score. On Shot7M2
Core i9-12900KF CPU (16 cores), 64 GB of RAM and


                                                             3
Table 3: CalMS21 Tasks 2 and 3 with the Task 1 encoders, frozen. Task 2: macro F1 per annotator, averaged over
annotators. Task 3: F1 per new behavior, averaged over behaviors.
                                                  Task 2: new annotators                                     Task 3: new behaviors
Encoder seed                            0                   1                    2                    0                1                 2
Training-free features (ours)         77.9                77.9                 77.9                37.6               37.6              37.6
hBehaveMAE                            71.7                72.6                 70.2                28.2               29.1              30.6
BAMS                                  66.1                66.4                 66.8                33.9               34.3              33.9
Ours minus hBehaveMAE            +6.2 [+2.6, +8.8]   +5.3 [+1.9, +7.8]   +7.7 [+3.3, +9.3] +9.3 [+5.8, +12.8] +8.5 [+5.0, +12.1] +7.0 [+3.3, +10.7]
Ours minus BAMS                 +11.8 [+7.4, +14.6] +11.5 [+7.6, +14.1] +11.1 [+6.7, +13.7] +3.7 [+1.2, +6.4] +3.2 [+1.0, +5.5] +3.7 [+1.5, +5.8]



Table 4: MABe22 mouse triplets, benchmark evaluator. Clip-level F1 is the mean of strain and lights; brackets are 95%
intervals from resampling test clips. Published rows are from the hBehaveMAE paper [11], Table 2 (“transductive”:
pretrained on the test clips too).
                           Method                                                     Clip-level F1       Frame-level F1
                           Training-free features (ours)                             83.7 [81.9, 85.3]        24.5
                           hBehaveMAE, released, best level (our run)                80.3 [78.7, 81.8]        22.3
                           hBehaveMAE, published, transductive                             80.3                22.3
                           BehaveMAE, published, transductive                              81.0                21.5
                           BAMS, published, transductive                                   80.1                19.8
                           hBehaveMAE, published, inductive                                78.5                20.1


we used the released hBehaveMAE checkpoint and the
                                                                               Table 5: MABe22 fly groups, mean F1 over 50 tasks,
authors’ evaluator.
                                                                               benchmark scorer. Published rows are from the BAMS
CalMS21 Tasks 2 and 3. The encoders trained for                                paper [1], Table 4.
Task 1 are reused frozen, with the variant and classifier                                  Method                            Mean F1
setting each method chose for the 5% budget. Task 2
trains on each annotator’s six training videos and tests                                   Training-free features (ours)        51.6
on that annotator’s test videos. Task 3 trains on one to                                   BAMS                                 48.2
                                                                                           T-GPT                                45.8
four videos per new behavior. Each classifier is trained
                                                                                           T-Perceiver                          44.8
with five seeds and the scores averaged.                                                   PCA                                  42.5
Uncertainty. Intervals are 95% intervals from 10,000                                       TVAE                                 37.0
resamples of the test videos (or clips), paired between
methods when we report a gap. To cover training luck,
each CalMS21 encoder was trained three times with                              haveMAE, by 3.4 points (paired interval +2.7 to +4.5).
different seeds, and each comparison is read for every                         With four labelled videos they tie BAMS: BAMS is 2.2
seed.                                                                          points higher, but the interval on the gap includes zero
                                                                               (−5.0 to +2.6), so the preregistered rule reads CON-
Preregistration. Before any test score existed, each
                                                                               FIRMED. hBehaveMAE, the stronger encoder with all
test’s design and its reading rule were written down
                                                                               labels, falls far behind with few labels. The reading does
and hashed, and the run scripts refuse to start if any file
                                                                               not depend on the encoders’ training seed: with each of
differs (Appendix A). For CalMS21 Task 1 the rule reads:
                                                                               the two further seeds the features lead with all labels
the claim holds if, at both label amounts, the features
                                                                               and tie BAMS with 5% (Appendix B). The lead with
are at or above the best encoder, or the 95% interval on
                                                                               all labels comes from attack and investigation; mount is
their gap includes zero. Deviations were recorded with
                                                                               easy for every method, and with 5% of labels no method
a timestamp before the scores they affect existed. For
                                                                               finds attack well (Appendix B). BAMS in its authors’
example, the reproduction target for hBehaveMAE on
                                                                               own mouse recipe scores far below every other method,
MABe22 was corrected from the paper’s inductive score
                                                                               so the version fed our measurements remains the BAMS
to its transductive one, which is what the released model
                                                                               entry.
is; our run matches that score to the decimal.
                                                                               CalMS21 Tasks 2 and 3. Both transfer settings favor
                                                                               the features over both encoders, with every paired inter-
5      Results                                                                 val above zero for every encoder seed (Table 3). With
                                                                               a new annotator, where hBehaveMAE is the closer en-
CalMS21 Task 1. With all labels the training-free                              coder, the features lead for each of the five annotators
features beat both encoders, and the better one, hBe-


                                                                           4
Table 6: Shot7M2, the benchmark’s evaluator. All F1 is the mean of the three scale scores. hBehaveMAE’s scale
columns in its paper are each the best of its levels; its All F1 is one level. Published rows are from the hBehaveMAE
paper [11], Table 3.
                                      Method                                                            All F1   Activities    Actions     Movemes
                                      Training-free features (ours)                                     68.8        92.6         55.2          58.7
                                      hBehaveMAE, released, best level (our run)                        64.7        76.4         54.8          62.9
                                      hBehaveMAE, best level for each scale (our run)                               80.9         58.5          67.3
                                      hBehaveMAE, published                                              64.7       80.9         58.5          67.3
                                      BehaveMAE, published                                               64.3       76.7         55.1          61.0
                                      PCA-30, published                                                  61.9       68.3         50.8          66.7
                                      PCA, published                                                     60.8       69.5         51.0          61.8
                                      TS2Vec, published                                                  59.6       68.6         50.0          60.2
                                      BAMS, published                                                    53.7       67.1         45.3          48.6
                                      TVAE, published                                                    51.2       65.5         47.0          41.0


                                                  All training labels (70 videos)                                    5% of labels (4 videos)
                                                                                                   70
                                     90
           Macro F1 on test videos




                                                                                hBehaveMAE         65
                                                                                                                                               BAMS
                                     80                                         BAMS
                                                                                                   60
                                     70
                                                                                                   55

                                     60                                                            50

                                                                                                   45                                          hBehaveMAE
                                     50                              step picked by the rule
                                                                     hand-built features           40
                                     40
                                           3 5    8      13 15    19    23                                3 5    8      13 15    19    23
                                          Measurements used (groups added left to right)                 Measurements used (groups added left to right)



Figure 1: CalMS21 Task 1 on the test videos as measurement groups are added (seed 0 encoders, each step with the
full set’s classifier settings). Whiskers and bands are 95% intervals. The circled step was picked by the preregistered
rule on training videos; the other steps describe the method rather than test it.


with every seed. With new behaviors learned from one                                               53.3; the published 48.2 has no interval of its own, so this
to four videos, where BAMS is the closer encoder, they                                             comparison is not paired. The rule was locked before
are best on five of the seven behaviors.                                                           any fly score existed, and before any of our scores the
                                                                                                   benchmark’s public scorer reproduced its own published
MABe22 mouse triplets. Against the authors’ re-
                                                                                                   scores for the sample submission. The score comes mostly
leased hBehaveMAE, scored with the benchmark’s own
                                                                                                   from the clip-level tasks (Appendix C; genotype 50.6
evaluator, the features lead by 3.4 points of clip-level F1;
                                                                                                   and line category 68.7, against 14.5 and 28.4 for the
resampling the 1,068 test clips puts the paired interval at
                                                                                                   random sample submission). The per-fly behavior tasks
+2.1 to +4.7 (Table 4). They are ahead on all 11 binary
                                                                                                   stay below the random submission (17.0 against 21.0),
tasks: strain (92.9 against 87.1), lights (74.4 against 73.4)
                                                                                                   because the representation pools over flies. A layout that
and each of the nine frame-level behaviors. The released
                                                                                                   keeps the flies apart, added after this result (16 numbers
model was pretrained on the test clips without labels,
                                                                                                   per fly plus 80 for the group), lifts the per-fly tasks to
while our statistics were fitted on the training clips only.
                                                                                                   24.8 and sex to 97.6 but lowers the group tasks, for 48.8
83.7 is also above every method in the hBehaveMAE
                                                                                                   overall; so pooling explains the weak per-fly scores.
paper’s table. We do not count the frame-level tasks
as evidence, because their labels were partly computed                                             Shot7M2. On a simulated basketball player, the bench-
from the poses.                                                                                    mark hBehaveMAE’s authors built to show what a hier-
                                                                                                   archical encoder learns, the features lead hBehaveMAE,
MABe22 fly groups. On a second species, from a
                                                                                                   the best method in that paper, by 4.2 points of All
different laboratory, the recipe scores 51.6 mean F1 over
                                                                                                   F1 (paired interval over the 680 test episodes +3.7 to
the benchmark’s 50 fly tasks, against 48.2 for BAMS,
                                                                                                   +4.6; Table 6). By the rule locked before any basketball
the best published method (Table 5). Resampling the
                                                                                                   score existed, the features are at or above hBehaveMAE.
326 test clips gives our score a 95% interval of 48.4 to


                                                                                               5
Before our features were scored, the authors’ released
                                                                  Table 7: Raw keypoints and their velocities in place of
model, run with their test settings and scored by their
                                                                  the measurements (“Ours”), everything else unchanged.
evaluator, reproduced its published All F1 and per-scale
                                                                  Body frame: centred on each animal or player and turned
bests. The lead comes from activities, the episode-level
                                                                  to its heading. World frame: camera, arena or dish coor-
labels. Actions are about level, with hBehaveMAE bet-
                                                                  dinates (Shot7M2’s are already centred on the pelvis hor-
ter on spins and turns and the features better on sprint.
                                                                  izontally). Best encoder: hBehaveMAE, except BAMS
hBehaveMAE is ahead on movemes, the shortest scale:
                                                                  for CalMS21 with 5% of labels and for the flies (published
foot and hand contacts, the ball, and elbow flexing and
                                                                  score). Each benchmark keeps its own score (clip-level
extending. So on the shortest movements the learned
                                                                  F1 for the mouse triplets).
encoder earns its keep. Because the generator defines
movemes from the motion itself, the rule also reads the                                             Raw keypoints     Best
activity and action scales without them: 73.9 against               Benchmark                Ours body     world    encoder
65.6, the same reading.
                                                                    CalMS21, all labels      85.8   84.8    77.7      82.4
                                                                    CalMS21, 5% of labels    61.1   64.7    38.4      63.4
                                                                    MABe22 mouse triplets    83.7   82.5    76.0      80.3
6    What carries the result                                        Shot7M2                  68.8   66.0    65.7      64.7
                                                                    MABe22 fly groups        51.6   46.3    41.8      48.2
To see which ingredients matter, a second preregistered
test strips the representation down. It adds the mea-
surement groups back one at a time, scores each step on
                                                                  and the same classifier or scorer (Table 7). In each
training videos, and picks the smallest step within one
                                                                  body’s own frame, raw keypoints beat hBehaveMAE on
point of the full set. The rule picked 19 measurements, ev-
                                                                  CalMS21 with all labels (+2.4 [+1.2, +3.8]), tie BAMS
erything except posture. On the test videos that version
                                                                  with 5% (+1.3 [−1.0, +4.4]), and beat hBehaveMAE on
beats hBehaveMAE with all labels (+2.6 [+1.6, +3.8])
                                                                  the MABe22 mouse triplets (clip-level F1 82.5 against
and ties BAMS with 5% (−1.4 [−4.7, +4.1]). The full
                                                                  80.3, +2.2 [+0.8, +3.5]) and on Shot7M2 (+1.4 [+0.8,
23 are +0.8 [+0.2, +1.5] points better with all labels,
                                                                  +1.8]). On the triplets’ frame-level tasks, which we
so they remain the method. Against encoders retrained
                                                                  do not count as evidence, they score 18.4 against 22.3.
with two further seeds, the 19-measurement version keeps
                                                                  The measurements add 1.0 point on CalMS21 with all
its reading: ahead of both with all labels in all three
                                                                  labels (+1.0 [+0.1, +2.0]) and 2.8 points on Shot7M2
passes (mean gaps +7.2 over BAMS and +2.6 over hBe-
                                                                  (+2.8 [+2.5, +3.1]), mostly on movemes (58.7 against
haveMAE) and level with BAMS at 5% (mean −1.0).
                                                                  52.2). Two differences have intervals that include zero:
   The other versions were read off the test videos, so
                                                                  the measurements’ 1.2-point lead on the mouse triplets
they describe the method rather than test it:
                                                                  (+1.2 [−0.2, +2.6]), and their 3.5-point deficit to raw
 • Time windows matter more than the choice
                                                                  keypoints on CalMS21 with 5% (−3.5 [−6.1, +0.1]). On
    of measurements. The frame value with the 0.5 s
                                                                  the fly groups raw keypoints fall short of BAMS (46.3, in-
    and 2 s windows alone scores 84.8 with all labels, 1.0
                                                                  terval 43.3 to 48.1, against 48.2), and the measurements
    below the full set. The 8 s and 30 s windows alone
                                                                  add 5.3 points (+5.3 [+2.7, +7.7]); one likely reason is
    score 69.6, and frame values without any window
                                                                  that pooling raw keypoints over up to 11 flies loses the re-
    76.3.
                                                                  lations between flies, which several measurements encode.
 • No single group is essential with all labels.
                                                                  In camera, arena or dish coordinates raw keypoints do
    Dropping any one group costs at most 0.8 points
                                                                  worse on every benchmark. So on both mouse datasets
    (posture). With 5% of labels, heading matters most
                                                                  and on Shot7M2 a body-centred frame and the window
    (4.5 points), then distance (2.3) and nose (2.1).
                                                                  statistics carry most of the result; with all labels the
 • One point per animal goes far. The 13 measure-
                                                                  measurements add 1.0 to 5.3 points, most on the flies.
    ments that need only each mouse’s centre score 81.2
                                                                     Together these point to a simple account: most of what
    with all labels, ahead of BAMS (+3.0 [+0.8, +5.1])
                                                                  the encoders capture about these behaviors is already in
    and level with hBehaveMAE (−1.2 [−2.8, +0.1]).
                                                                  a few kinematic signals summarized over short windows.
    With 5% of labels they trail BAMS by 10.4.
                                                                  BAMS shows the same from the other side: it is only
 • Histograms matter with few labels. Without
                                                                  as good as its input. Fed our 23 measurements as input
    them the 5% score falls by 7.0 to 10.7 points, while
                                                                  and targets it reaches 78.3 on the test videos; in its
    with all labels they are worth about one point.
                                                                  authors’ mouse recipe (adapted to CalMS21’s keypoints)
Raw keypoints. Three further preregistered tests,                 54.6; and on raw keypoints with its authors’ generic
locked before any raw-keypoint score existed and read             template it reached 54.8 on the training videos, where
descriptively, replace the measurements by raw keypoints          it was not selected. Even at its best it stays below the
and their velocities. Everything else is unchanged: the           measurements it was fed (78.3 against 85.8).
windows and statistics, fitting on training data only, the
layout and budget each benchmark’s own test chose,


                                                              6
7    Limitations                                                keypoints in the body’s own frame, summarized the
                                                                same way, match or beat the encoders, while on flies
• Scope. The evidence is two mouse datasets, one fly            the measurements are needed. We suggest that new
  dataset and one synthetic human dataset. CalMS21’s            behavior encoders report such a baseline next to their
  three tasks come from one laboratory and setup, so            results, and we will release ours with its frozen fits, with
  Tasks 2 and 3 are not independent of Task 1. On               the conference version, so that it costs nothing to run.
  flies the comparison is with BAMS’s published score           Code and data. The code will be released with the
  from a single submission, and the per-fly behavior            conference version of this paper. The release will contain
  tasks are not solved by a representation that pools           the measurement code for each dataset, the frozen fits,
  over flies.                                                   the preregistration files with their hashes, and the scripts
• Home ground. CalMS21’s poses come from MARS,                  that score them with each benchmark’s own evaluator.
  and Task 1’s videos match the training and test sets          The datasets are not redistributed; they are available
  of MARS’s classifiers, which use hand-designed fea-           from their original sources.
  tures. The benchmark paper [13] reports 79.3 for
  a supervised 1D convolutional network, 82.9 when
  that network is given TREBA’s self-supervised fea-            References
  tures, and 86.4 for the 2021 challenge winner, a semi-
  supervised model trained with the labels; our 85.8             [1] Mehdi Azabou, Michael Mendelson, Nauman Ahad,
  uses a much smaller classifier.                                    Maks Sorokin, Shantanu Thakoor, Carolina Urzay,
• Retrained opponents. On CalMS21 we retrained                       and Eva L. Dyer. Relax, it doesn’t matter how you
  both encoders ourselves. They score above the                      get there: A new self-supervised approach for multi-
  numbers MICE reports for them (hBehaveMAE                          timescale behavior analysis. In Advances in Neural
  82.4 against 76.05, BAMS 78.3 against 74.98), but                  Information Processing Systems 36 (NeurIPS 2023),
  BAMS’s keypoint template was weak in our hands,                    2023. arXiv:2303.08811.
  and its authors’ own mouse recipe, adapted to
  CalMS21’s seven keypoints (42 of its 66 input features         [2] Angus Dempster, François Petitjean, and Geof-
  remain), did worse still: 54.6 with all labels and 28.4            frey I. Webb. ROCKET: exceptionally fast and
  with 5%, below the 0.70 training-video floor, so the               accurate time series classification using random con-
  version fed our measurements stays the BAMS entry.                 volutional kernels. Data Mining and Knowledge
• Few labels. With four labelled videos the compari-                 Discovery, 34(5):1454–1495, 2020. doi: 10.1007/
  son with BAMS is a tie, not a win.                                 s10618-020-00701-z.
• MICE. It is the newest encoder and was not run,                [3] Nastacia L. Goodwin, Jia J. Choong, Sophia Hwang,
  because its code was not released (its repository held             Kayla Pitts, Liana Bloom, Aasiya Islam, Yizhe Y.
  only a placeholder README on 17 November 2026).                    Zhang, Eric R. Szelenyi, Xiaoyu Tong, Emily L.
  Its reported CalMS21 score (83.3) comes from a setup               Newman, Klaus Miczek, Hayden R. Wright, Ryan J.
  that scores every method lower than ours, so it cannot             McLaughlin, Zane C. Norville, Neir Eshel, Mitra
  be compared directly.                                              Heshmati, Simon R. O. Nilsson, and Sam A. Golden.
• Frozen representations. We test frozen embed-                      Simple behavioral analysis (SimBA) as a platform
  dings with a small classifier. Fine-tuned encoders,                for explainable machine learning in behavioral neu-
  or learned features at much larger scale with full                 roscience. Nature Neuroscience, 27(7):1411–1424,
  supervision, may behave differently.                               2024. doi: 10.1038/s41593-024-01649-9.
• Uncertainty. Intervals cover the sampling of test
  videos. Training luck is covered by repeating each             [4] Alexander I. Hsu and Eric A. Yttri. B-SOiD,
  encoder’s training with three seeds, not by the inter-             an open-source unsupervised algorithm for iden-
  vals.                                                              tification and fast prediction of behaviors. Na-
                                                                     ture Communications, 12(1), 2021. doi: 10.1038/
                                                                     s41467-021-25420-x.
8    Conclusion
                                                                 [5] Mayank Kabra, Alice A. Robie, Marta Rivera-Alba,
Under one fair protocol, a training-free representation              Steven Branson, and Kristin Branson. JAABA: in-
built from generic measurements and window statistics                teractive machine learning for automatic annotation
matches or beats two published self-supervised behavior              of animal behavior. Nature Methods, 10(1):64–67,
encoders on the standard mouse benchmarks, on a second               2013. doi: 10.1038/nmeth.2281.
species and on a simulated human, where the learned
                                                                 [6] Weihan Li, Jingyang Ke, Qinheng Pu, Yule Wang,
encoder still wins on the shortest movements. Most of the
                                                                     Chengrui Li, and Anqi Wu. Learning when visual
result comes from a few kinematic signals summarized
                                                                     context matters for mouse behavior analysis, 2026.
over short windows; on mice and basketball, even raw
                                                                     arXiv:2603.07279.


                                                            7
 [7] Carl H. Lubba, Sarab S. Sethi, Philip Knaute, Si-              Oleszko, Zachary Partridge, Milan Peelman, Al-
     mon R. Schultz, Ben D. Fulcher, and Nick S. Jones.             ice Robie, Catherine E. Schretter, Keith Sheppard,
     catch22: CAnonical Time-series CHaracteristics: Se-            Chao Sun, Param Uttarwar, Julian Morgan Wagner,
     lected through highly comparative time-series anal-            Erik Werner, Joseph Parker, Pietro Perona, Yisong
     ysis. Data Mining and Knowledge Discovery, 33(6):              Yue, Kristin Branson, and Ann Kennedy. MABe22:
     1821–1852, 2019. doi: 10.1007/s10618-019-00647-x.              A multi-species multi-task benchmark for learned
                                                                    representations of behavior. In Proceedings of the
 [8] Kevin Luxem, Petra Mocellin, Falko Fuhrmann, Jo-
                                                                    40th International Conference on Machine Learn-
     hannes Kürsch, Stephanie R. Miller, Jorge J. Palop,
                                                                    ing, volume 202 of Proceedings of Machine Learning
     Stefan Remy, and Pavol Bauer. Identifying behav-
                                                                    Research, pages 32936–32990. PMLR, 2023.
     ioral structure from deep variational embeddings
     of animal motion. Communications Biology, 5(1),            [16] Caleb Weinreb, Jonah E. Pearl, Sherry Lin, Mo-
     2022. doi: 10.1038/s42003-022-04080-7.                          hammed Abdal Monium Osman, Libby Zhang, Sid-
                                                                     harth Annapragada, Eli Conlin, Red Hoffmann,
 [9] Kevin Musgrave, Serge Belongie, and Ser-Nam Lim.
                                                                     Sofia Makowska, Winthrop F. Gillis, Maya Jay,
     A metric learning reality check. In Computer Vision
                                                                     Shaokai Ye, Alexander Mathis, Mackenzie W.
    – ECCV 2020, Lecture Notes in Computer Science,
                                                                     Mathis, Talmo Pereira, Scott W. Linderman, and
     pages 681–699. Springer International Publishing,
                                                                     Sandeep Robert Datta. Keypoint-MoSeq: parsing
     2020. doi: 10.1007/978-3-030-58595-2_41.
                                                                     behavior by linking point tracking to pose dynam-
[10] Cristina Segalin, Jalani Williams, Tomomi Karigo,               ics. Nature Methods, 21(7):1329–1339, 2024. doi:
     May Hui, Moriel Zelikowsky, Jennifer J. Sun, Pietro             10.1038/s41592-024-02318-2.
     Perona, David J. Anderson, and Ann Kennedy. The
     mouse action recognition system (MARS) software            [17] Ailing Zeng, Muxi Chen, Lei Zhang, and Qiang Xu.
     pipeline for automated analysis of social behaviors             Are transformers effective for time series forecasting?
     in mice. eLife, 10, 2021. doi: 10.7554/eLife.63720.             Proceedings of the AAAI Conference on Artificial
                                                                     Intelligence, 37(9):11121–11128, 2023. doi: 10.1609/
[11] Lucas Stoffl, Andy Bonnetto, Stéphane d’Ascoli,                 aaai.v37i9.26317.
     and Alexander Mathis. Elucidating the hierar-
     chical nature of behavior with masked autoen-
     coders. In Computer Vision – ECCV 2024, Lec-
     ture Notes in Computer Science, pages 106–125.
     Springer Nature Switzerland, 2024. doi: 10.1007/
     978-3-031-73039-9_7.
[12] Yen-Shuo Su, Weihan Li, and Anqi Wu. MICE:
     Multi-animal interaction context encoder – a hierar-
     chical foundation model for mouse behavior, 2026.
     NeurIPS 2026 (per the arXiv comment).
[13] Jennifer J. Sun, Tomomi Karigo, Dipam
     Chakraborty, Sharada P. Mohanty, Benjamin
     Wild, Quan Sun, Chen Chen, David J. Anderson,
     Pietro Perona, Yisong Yue, and Ann Kennedy.
     The multi-agent behavior dataset: Mouse dyadic
     social interactions. In Proceedings of the Neu-
     ral Information Processing Systems Track on
     Datasets and Benchmarks (NeurIPS 2021), 2021.
     arXiv:2104.02710.
[14] Jennifer J. Sun, Ann Kennedy, Eric Zhan, David J.
     Anderson, Yisong Yue, and Pietro Perona. Task
     programming: Learning data efficient behavior rep-
     resentations. In 2021 IEEE/CVF Conference on
     Computer Vision and Pattern Recognition (CVPR),
     pages 2875–2884. IEEE, 2021. doi: 10.1109/
     CVPR46437.2021.00290.
[15] Jennifer J. Sun, Markus Marks, Andrew Wesley
     Ulmer, Dipam Chakraborty, Brian Geuther, Ed-
     ward Hayes, Heng Jia, Vivek Kumar, Sebastian


                                                            8
A       Preregistration record
Each test, and each later addition to it, was written down and locked before any of its test scores existed; the run
scripts check the SHA-256 hash of every locked file before they start. All dates are in 2026.

 Test                                  What was locked                                                         Locked (UTC)
 CalMS21 Task 1                        design, opponents and reading rule                                      15 Nov, 01:10
                                       remaining details; running the parts side by side                       15 Nov, 03:30–06:35
                                       repeat with two further encoder seeds                                   16 Nov, 18:15
                                       BAMS with its authors’ mouse recipe                                     16 Nov, 19:10
 CalMS21 Tasks 2 and 3                 design and reading rule                                                 16 Nov, 19:30
 What carries the result               stripped-down versions (Section 6)                                      16 Nov, 21:00
 MABe22 mouse triplets                 design, opponents and reading rule                                      15 Nov, 01:10
                                       layout chosen on user-train clips; frozen files                         15 Nov, 01:20
                                       reproduction check of the released hBehaveMAE                           16 Nov, 18:40
                                       intervals                                                               17 Nov, 17:15
 MABe22 fly groups                     design and reading rule                                                 17 Nov, 15:10
                                       layout that keeps the flies apart                                       17 Nov, 17:20
                                       intervals                                                               17 Nov, 18:05
 Shot7M2                               design and reading rule                                                 17 Nov, 17:30
                                       intervals                                                               17 Nov, 17:58
 Raw keypoints, CalMS21 Task 1         design and descriptive reading (Section 6)                              18 Nov, 06:14
 Raw keypoints, Shot7M2 and flies      design and descriptive reading (Section 6)                              18 Nov, 14:39
 Raw keypoints, MABe22 mice            design and descriptive reading (Section 6)                              18 Nov, 16:41



B       CalMS21 Task 1: encoder seeds and per-behavior scores
Gaps are the features minus the best encoder at each label budget, with paired 95% intervals.

                                                    All labels                         5% of labels
                     Encoder seed      hBehaveMAE          Features minus it    BAMS       Features minus it
                     0                      82.4           +3.4 [+2.7, +4.5]    63.4       −2.2 [−5.0, +2.6]
                     1                      83.1           +2.7 [+2.0, +3.6]    61.9       −0.7 [−3.8, +4.1]
                     2                      81.6           +4.2 [+2.9, +5.6]    63.9       −2.8 [−5.5, +1.9]


  Per-behavior F1 with seed 0 encoders:

                           Method                            Labels    Attack   Investigation    Mount
                           Training-free features (ours)     all        79.9        84.6           93.0
                           hBehaveMAE                        all        76.4        79.6           91.2
                           BAMS                              all        60.7        82.8           91.4
                           Training-free features (ours)     5%         38.2        70.9           74.3
                           hBehaveMAE                        5%         30.8        56.4           49.2
                           BAMS                              5%         39.3        73.7           77.2




                                                                   9
C   MABe22 fly groups by task category

      Category                        Tasks   Ours, pooled    Ours, flies apart   Random sample submission
      Fly type (genotype)              11         50.6              41.2                    14.5
      Stimulation, control lines       10         52.8              47.7                    48.4
      Stimulation, aggression lines    15         55.0              56.0                    49.6
      Line category                     7         68.7              60.5                    28.4
      Female vs male                    1         88.0              97.6                    72.1
      Manual behaviors (per fly)       6          17.0              24.8                    21.0
      All 50 tasks                     50        51.6               48.8




                                                         10
