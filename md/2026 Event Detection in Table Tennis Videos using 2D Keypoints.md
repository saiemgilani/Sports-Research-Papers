<!-- source: 2026 Event Detection in Table Tennis Videos using 2D Keypoints.pdf -->

# Event Detection in Table Tennis Videos using 2D Keypoints

- arXiv: https://arxiv.org/abs/2610.08286 (2026-10-06, cs.CV)
- Authors: Rainer Lienhart, Daniel Kienzle, Shin'ichi Satoh, Anastasiia Bilinska et al.
- Triage: N5/P3/R6 = 14/30 | data: public | code: yes

## Abstract

This paper addresses the challenge of automatic, frame-accurate event detection in table tennis videos. Current methods for estimating 3d ball trajectories and ball spin typically require that key events, such as ball-racket contacts, have already been identified in advance. This requirement makes it difficult to apply these methods to longer, unedited video recordings. To overcome this limitation, we propose EventNet, a two-stage pipeline to detect key events: (1) 2d keypoints are extracted of the upper-body poses for both players, table corners and ball center. A small keypoint transformer combines them into a compact representation that is robust to changes in viewpoint, lighting, and background clutter. (2) The temporal sequences of these frame-based representations are processed by a transformer encoder that predicts two time-to-event values for each frame, indicating how close the current frame is to the next and previous ball-racket contact. One novelty is a new, temporal cosine-like target signal. Furthermore, we introduce viewpoint augmentation via 3D reprojection and frame-rate augmentation to improve robustness and generalization. Our extensive ablation study gives deeper insights into the importance of various architectural and training aspects. Experimental results show that the proposed approach achieves an F1 score of 91.16% and a mean frame deviation between ground truth and predicted frame of 0.42 on the Latte-MV dataset and 73.08% / 1.16 on the challenging TTHQ dataset. Overall, our work demonstrates that 2d keypoint-based temporal modeling with our EventNet architecture is a promising and practical approach for automatic event detection in table tennis videos.

## Full text (pdftotext extraction)

```text
                                               Event Detection in Table Tennis Videos using 2D Keypoints
                                                                       Rainer Lienhart∗†                                                                   Daniel Kienzle∗
                                                                     University of Augsburg                                                          University of Augsburg
                                                                      Augsburg, Germany                                                                Augsburg, Germany
                                                                    Rainer.Lienhart@uni-a.de                                                         Daniel.Kienzle@uni-a.de

                                                                            Shin’ichi Satoh                                                          Anastasiia Bilinska∗
                                                               National Institute of Informatics                                                      University of Augsburg
                                                                    University of Tokyo                                                                Augsburg, Germany
                                                                         Tokyo, Japan
                                                                       satoh@nii.ac.jp
arXiv:2610.08286v1 [cs.CV] 6 Oct 2026




                                                                    Shape:          (𝑇, 𝑁, 2)                       (𝑇, 𝑁 + 1, 𝐷)                 (𝑇, 𝐷)                  (2,1)

                                                                 Sequence of                         Keypoints                    Extract CLS                                      𝑓" 𝑡 ! , 𝑏% 𝑡 !
                                                   t=0
                                                                 N keypoints                        Transformer                      token
                                                      .                 .                                  .                            .                     Time-to-                   at
                                                      .                 .                                  .                            .                       Event                         𝑇
                                                      .                 .                                  .                            .                                            𝑡! =
                                                                                                                                                            Transformer                       2
                                                   t=T-1         Sequence of                         Keypoints                    Extract CLS
                                                                 N keypoints                        Transformer                      token                                         with 𝑇 odd


                                        Figure 1: Overview of our EventNet: All keypoints per frame are individually condensed into a CLS token by the Keypoints
                                        Transformer, before the Time-to-Event Transformer determines the temporal distance to the previous and next event (𝑏 (𝑓 ′ ), 𝑓 (𝑡 ′ )).
                                        Abstract                                                                                    and 73.08% / 1.16 on the challenging TTHQ dataset. Overall, our
                                        This paper addresses the challenge of automatic, frame-accurate                             work demonstrates that 2d keypoint-based temporal modeling with
                                        event detection in table tennis videos. Current methods for esti-                           our EventNet architecture is a promising and practical approach
                                        mating 3d ball trajectories and ball spin typically require that key                        for automatic event detection in table tennis videos.
                                        events, such as ball-racket contacts, have already been identified in
                                        advance. This requirement makes it difficult to apply these methods                         CCS Concepts
                                        to longer, unedited video recordings. To overcome this limitation,                          • Computing methodologies → Activity recognition and un-
                                        we propose EventNet, a two-stage pipeline to detect key events: (1)                         derstanding; Visual content-based indexing and retrieval.
                                        2d keypoints are extracted of the upper-body poses for both players,
                                        table corners and ball center. A small keypoint transformer com-
                                        bines them into a compact representation that is robust to changes                          Keywords
                                        in viewpoint, lighting, and background clutter. (2) The temporal                            frame-accurate event detection, ball-racket event detection, event
                                        sequences of these frame-based representations are processed by a                           detection in table tennis, Transformer-based event detection
                                        transformer encoder that predicts two time-to-event values for each
                                        frame, indicating how close the current frame is to the next and pre-
                                        vious ball-racket contact. One novelty is a new, temporal cosine-like
                                        target signal. Furthermore, we introduce viewpoint augmentation                             1       Introduction
                                        via 3D reprojection and frame-rate augmentation to improve robust-                          In table tennis, recent works [4, 8, 9] on 3d reconstruction and ball
                                        ness and generalization. Our extensive ablation study gives deeper                          spin estimation have made it possible to analyze ball trajectories
                                        insights into the importance of various architectural and training                          with high precision. However, these approaches usually assume
                                        aspects. Experimental results show that the proposed approach                               that rallies are already segmented and timestamps of important
                                        achieves an F1 score of 91.16% and a mean frame deviation between                           events (such as ball-racket contacts or bounces on the table) are
                                        ground truth and predicted frame of 0.42 on the Latte-MV dataset                            known in advance. In practice, this assumption is rarely satisfied,
                                        ∗ All three authors contributed equally to this research.                                   especially for long, uncut broadcast videos. As a result, existing 3D
                                        † A significant portion of the overall work was carried out during the research stay at     trajectory and spin estimation pipelines cannot yet be applied fully
                                        the National Institute of Informatics, Toyko, Japan.                                        automatically to such unedited broadcast videos.
                                                                                                                                       To address this limitation, this work focuses on automatic frame-
                                                                                                                                    accurate event detection such as ball-racket contact in table tennis
                                        This work is licensed under a Creative Commons Attribution 4.0 International License.       videos using 2d keypoint representations instead of raw image data.
                                                                                      Rainer Lienhart, Daniel Kienzle, Shin’ichi Satoh, and Anastasiia Bilinska


We significantly extend and improve the work of [2] on frame-                 A different line of work uses 2d human pose sequences as a
accurate event detection of foot ground contact in long jump and           compact description of motion [2, 11, 21]. It has been shown that
triple jump using 2d keypoint sequences.                                   even noisy 2d keypoints can be used to estimate step frequency in
   Our proposed approach follows a two-step pipeline: First, 2d key-       sprinting, split athletic movements into phases, and detect sparse
points are extracted for the ball, the table, and the players’ pose. The   events in athletics videos with convolutional sequence models. [3]
motion states of both players are represented through their upper          proposes to first estimate 2d poses with Mask R-CNN and then apply
body pose keypoints, the ball’s motion through its location, and the       pose-based sequence models for event detection in swimming and
table keypoints provide geometric context. These keypoints in each         athletics. Their results show that pose sequences allow accurate and
frame are normalized and transformed by a keypoints transformer            data-efficient event detection and can be used in practical systems
into a compact temporal sequence. Second, a time-to-event trans-           for different sports.
former then models the temporal dependencies in these sequences               This work follows the same general idea of separating visual
and predicts two time-to-event values for each frame, namely, how          perception from temporal reasoning, but focuses on table tennis.
close a frame is to the previous and next event, which allows the          Compared to athletics and swimming, table tennis is more chal-
model to locate ball-racket contact events in time precisely.              lenging because the ball is small, often occluded, filmed from many
   Several extended and novel design choices beyond our base-              different viewpoints and moves fast.
line model [2] are introduced to improve robustness, prediction
performance, and generalization. Our key contributions are:                3     Approach
     • The proposed fps augmentation makes our models insensi-             Our goal is to perform frame-accurate event detection in video
       tive to varying, unknown frame rates of input videos.               recordings of table tennis matches. As a representative event, we
     • The proposed viewpoint augmentation through 3d reprojec-            choose the moment of ball-racket contact, i.e., we want to predict
       tion mitigates the effect of the limited diversity of camera        all frames showing the desired event in long, unedited broadcast
       angles in the training dataset and simulates the complexity         videos of table tennis matches. We assume that valid results of a 2d
       of real broadcast conditions.                                       ball, table tennis corner and net detector, as well as a human pose
       Both augmentations are possible due to our smart input              estimator are available, providing us most of the time throughout a
       representation as 2d keypoints without pixel information.           video with an estimate of the 2d pixel positions of the ball center,
     • We propose a relative linear and cosine-like time-to-event          the table and net corners, as well as the keypoints of the torsos and
       encoding, instead of the absolute linear event encoding of          upper limbs of both table tennis players1 .
       [2]. Both provide a smoother, more informative, and fps
       insensitive training signal.                                        3.1     Baseline Model
     • The TCN backbone of [2] is replaced with a transformer-             The work in [2] serves as our baseline model. It addresses frame-
       based architecture. This improves event detection perfor-           accurate event detection in long and triple jump videos. This method
       mance at reduced training time by a factor of 0.32 to 0.48.         relies purely on 2d pose sequences extracted from the athlete in each
     • An extensive ablation study gives deeper insights into the          frame to determine the beginning or end of foot ground contact.
       importance of various architectural and training aspects.           Pose sequences are a very compact and better suited representation
                                                                           for learning motion patterns over time than raw videos.
2    Related Work                                                             Adapted to our application scenario, each frame is described
                                                                           by a concatenated vector of 2d keypoints consisting of the pixel
Previous work on event detection in sports videos can be roughly
                                                                           positions of the ball center, the table and net corners as well as the
divided into three groups: methods that use (a) motion capture data,
                                                                           keypoints of the torsos and upper limbs of both table tennis players.
(b) work directly on raw video, or (c) rely on human poses and
                                                                           Keypoints without valid values for whatever reason (e.g., not in
other keypoints as an intermediate representation.
                                                                           the field-of-view or the detector missed it) are encoded as NaN
   Some early systems assume access to accurate 3D motion capture
                                                                           values. In [2] the sequence of keypoints is fed into a fully Temporal
data [5, 15]. With special sensor- or marker-based setups, they
                                                                           Convolutional Network (TCN [1]) that predicts the frame distance
detect key poses and split movements into actions, for example
                                                                           to the next and previous occurrence of the desired event type.
in martial arts or fitness exercises. These methods work well in
                                                                              A key contribution of [2] is its event detection formulation. In-
controlled lab environments but need expensive hardware and are
                                                                           stead of classifying each frame directly as event or non-event, it
not suitable for large amounts of broadcast-like sports videos.
                                                                           defines for every frame two target values for each event type: a
   If only standard monocular videos are available, many approaches
                                                                           forward and a backward time-to-event indicator value. The for-
work directly on image or motion features [10, 18]. Classical meth-
                                                                           ward/backward value tells the network how far the current frame
ods use silhouettes and motion-segmentation features for sports
                                                                           is away from the next/previous event. By predicting continuously
such as high diving or long jump, sometimes together with simple
                                                                           time-to-event values (i.e., for every frame) instead of classifying a
kinematic models. More recent deep learning methods train CNNs
                                                                           few rare events, a severe class imbalance at training time is avoided.
end-to-end on raw video frames to recognize actions or detect
                                                                              The TCN model [1] is based on temporal convolutional blocks.
sparse events, for example in soccer or swimming [6, 13, 16, 17].
                                                                           Each block uses dilated 1D convolutions over time, followed by
These models do not need explicit motion representations, but they
                                                                           batch normalization, ReLU, dropout, and residual connections. The
require a lot of annotated data and often generalize poorly when
camera viewpoints or recording conditions change.                          1 The source code and models are available at https://github.com/MLCVLab/EventNet
Event Detection in Table Tennis Videos using 2D Keypoints


network takes flattened keypoint locations as input, and outputs                       and 𝑏𝑐 (𝑡), that encode for each frame the distance to the next and
the forward and backward timing indicators for all event types                         from the previous event of type 𝑐. This concept is taken from [2].
at each time step. During training, the input length is set to the
                                                                                            Absolute Linear Time-to-Event Signal. In [2] the target temporal
model’s receptive field, and the prediction is made for the center
                                                                                       distances to the events are saturated normalized by a constant 𝑡 max
frame of the sequence. At inference time, the network processes the
                                                                                       to ensure that the target values lie within the range [0, 1] for 𝑓𝑐 (𝑡)
full pose sequence of a video and predicts time-to-event indicator
                                                                                       and [−1, 0] for 𝑏𝑐 (𝑡). In practice, parameter 𝑡 max proved difficult to
values for every frame. Event locations are detected at time steps
                                                                                       tune in our task due to different fps and highly variable ball speeds.
𝑡 where both indicator values simultaneously identify the same
                                                                                       If 𝑡 max is too small, only frames near events show meaningful values
frame as the next and previous event.
                                                                                       between 0 or 1, while distant frames at time 𝑡 saturate to the extreme
                                                                                       value of 𝑓𝑐 (𝑡) = 1 and 𝑏𝑐 (𝑡) = −1, respectively. If 𝑡 max is chosen too
3.2     Input: Sequence of 2d Keypoint Sequences
                                                                                       large, the signal becomes nearly flat. These issues made learning
As already said, we assume that we have for every frame 𝑖 (estimates                   challenging as clipped signals give no feedback during learning.
of) the 2d pixel positions of the ball center, the table and net corners,              The dashed lines in Fig. 2a show a target signal with flat regions.
as well as the keypoints of the torsos and upper limbs of both table
tennis players. Missing keypoint values (either not visible in the
frame or missed by the detectors) are encoded by NaN values. For
each frame 𝑖, we construct its feature tensor x𝑖 of shape 𝑁 × 2 by
concatenating the ball location with the six table keypoints (four
table corners and two net points) and a selected subset of 𝑏 body
keypoints of each player, resulting in 𝑁 = 1 + 6 + 2𝑏 keypoints per
frame (see Fig. 3). We construct two different, named keypoint sets
each with a different subset 𝑏 of upper body keypoints:                                    (a) Absolute linear time-to-event encoding (short "absLin")
     (1) UB = upper body = {ball, table, head, shoulders, elbows,
         wrists, hips}, 𝑁 = 25
     (2) NO = no body points = {ball, table}, 𝑁 = 7
We will evaluate experimentally in Section 4 which keypoint set is
more informative for the task at hand.
    Raw and Normalized Input Sequence . All raw2 input sequences x
of length 𝑇 are of shape 𝑇 × 𝑁 × 2. As the training will be conducted                       (b) Relative linear time-to-event encoding (short "relLin")
using the LATTE-MV dataset [4], all player keypoints as well as the
table and ball coordinates are annotated for each frame (including
NaN values for not available keypoints). However, the raw 2d key-
point coordinates vary widely in scale across different videos due to
differences in camera distance to the tennis table, viewpoint, scene
geometry, and video resolution. To make the representation of x
invariant to these factors, all keypoint coordinates in each input
sequence x are normalized to the range of [−1, 1] as follows:                                  (c) Cosine-like time-to-event encoding (short "cos")
      • Missing or failed detections (NaN values) in x are replaced
         by 0.0 in max or by 𝑤𝑖𝑑𝑡ℎ 𝑣𝑖𝑑𝑒𝑜 in min operations.                            Figure 2: Visualizations of our three variants of time-to-event
      • We compute the global minimum 𝑚 = min(x) and maxi-                             target signals: (a) absolute linear with 𝑡𝑚𝑎𝑥 = 35, (b) relative
         mum 𝑀 = max(x) over each complete 𝑇 × 𝑁 × 2 tensor.                           linear, and (c) cosine-like. Dashed lines show the target time-
      • Each keypoint is then scaled and shifted into the interval                     to-event signal: forward signal 𝑓𝑐 (𝑡) in orange, backward sig-
          [−1, 1] via x′′ = 2 · x′ − 1 with x′ = 𝑀x−𝑚
                                                   −𝑚 .                                nal 𝑏𝑐 (𝑡) in blue, summed signal 𝑟𝑐 (𝑡) in green. Solid lines
    This sequence-wise normalization ensures that all coordinates                      show the predictions of one of our trained models.
lie in a consistent bounded range.
                                                                                            Relative Linear and Cosine-Like Time-to-Event Encoding. To ad-
3.3     Target: Time-to-Event Indicator Signal
                                                                                       dress this shortcoming, we propose two new encodings. Both make
Each training and test video is fully annotated with a temporally                      sure that every event, regardless of the sequence’s fps or the ball’s
ordered set e = {𝑒 1, . . . , 𝑒𝐸 } of size 𝐸 of event occurrences of type              speed, is represented by the exact same mathematical pattern be-
𝑐, with 𝑐 = "ball-racket contact". Each 𝑒𝑖 ∈ {1, . . . ,𝑇 } specifies the              tween adjacent events. Instead of measuring the absolute distance
frame index of a ball-racket contact event by any player. 𝑇 is the                     to an event, the signal provides a relative temporal position between
temporal length of the input video in frames. Our task is now to                       adjacent events. For each time index 𝑡, the times of the closest pre-
construct two useful time-to-event indicator signals named 𝑓𝑐 (𝑡)                      vious and next event are defined as: 𝑡 prev (𝑡) = max{𝑒𝑖 ∈ e | 𝑒𝑖 ≤ 𝑡 },
2 The attribute raw indicates that all 2d coordinates are given in the unnormalized,   𝑡 next (𝑡) = min{𝑒𝑖 ∈ e | 𝑒𝑖 ≥ 𝑡 }. To ensure that the formulation
original pixel space of each video frame.                                              remains well-defined at the boundaries of a video sequence, we
                                                                                                                                            Rainer Lienhart, Daniel Kienzle, Shin’ichi Satoh, and Anastasiia Bilinska


                                                                                                                                              Shape:      (𝐵, 𝑇, 𝑁, 2)         (𝐵𝑇, 𝑁, 2)        (𝐵𝑇, 𝑁, 2)     (𝐵𝑇, 𝑁, 𝐷)     (𝐵𝑇, 𝑁 + 1, 𝐷)
apply the following rules: if no previous event exists (i.e., the cur-
                                                                                                                                            Sequence of
rent frame lies before the first annotated event), we set 𝑡 prev (𝑡) = 0.                                                           t=0
                                                                                                                                            N keypoints               Compute
                                                                                                                                                                                             Set                           Append
                                                                                                                                                                        NaN                                 Input
Similarly, if no future event exists (i.e., the current frame lies af-                                                                .
                                                                                                                                      .
                                                                                                                                                 .
                                                                                                                                                 .                    keypoint
                                                                                                                                                                                             NaN
                                                                                                                                                                                                             pro-
                                                                                                                                                                                                                            learn-
                                                                                                                                      .          .                                          values                           able
ter the last annotated event), 𝑡 next (𝑡) = 𝑡 + Δ, where Δ > 0 is a                                                                                                     Mask
                                                                                                                                                                          +
                                                                                                                                                                                              To
                                                                                                                                                                                                             ject-
                                                                                                                                                                                                              ion
                                                                                                                                                                                                                             CLS
                                                                                                                                            Sequence of                                      zero                          tokens
fixed constant. This avoids undefined operations when computing                                                                     t=T-1
                                                                                                                                            N keypoints
                                                                                                                                                                       flatten

distances to neighboring events and ensures stable and bounded                                                                                                             (𝐵𝑇, 𝑁)
                                                                                                                                                                                                                     (𝐵𝑇, 𝑁 + 1, 𝐷) 2×
timing indicators at the beginning and end of a sequence.                                                                                   Extract CLS               Keypoints +
                                                                                                                                    t=0                                                                                  Add & Norm
   Based on these neighboring events, we define relative linear                                                                                token                   CLS token
                                                                                                                                                                                                Output
                                                                                                                                      .          .                         .                                                 FFN
                                                                                                                                                 .                         .                   Projection
(relLin) and cosine-like (cos) time-to-event encodings:                                                                               .
                                                                                                                                      .          .                         .                       +
                                                                                                                                                                                               unflatten                 Add & Norm
                         𝑡 next (𝑡) − 𝑡                     𝑡 − 𝑡 prev (𝑡)                                                          t=T-1
                                                                                                                                            Extract CLS               Keypoints +
                                                                                                                                                                                                                             MSA
                   𝑓relLin (𝑡) =         , 𝑏 relLin (𝑡) = −                        (1)                                                         token                   CLS token
                         𝑡 next − 𝑡 prev                    𝑡 next − 𝑡 prev                                                                               (𝐵, 𝑇, 𝐷)               (𝐵, 𝑇, 𝑁 + 1, 𝐷)

                                                               𝜋 𝑡 − 𝑡 prev (𝑡)
                                                                              
                   𝜋 𝑡 next (𝑡) − 𝑡
  𝑓cos (𝑡) = sin                       , 𝑏 cos (𝑡) = − sin                         (2)                                         Figure 4: Overview of the Keypoints Transformer architec-
                   2 𝑡 next − 𝑡 prev                           2 𝑡 next − 𝑡 prev
                                                                                                                               ture. It shows how a sequence of keypoints per frame is
By construction both encodings satisfy 𝑓 (𝑒𝑖 )=𝑏 (𝑒𝑖 )=0 ∀𝑒𝑖 ∈ e, while
                                                                                                                               transformed into a CLS token and prepared as input for the
they take smooth, non-zero values between adjacent events. The
                                                                                                                               temporal Time-to-Event Transformer.
pair (𝑓 (𝑡), 𝑏 (𝑡)) thus forms a continuous encoding of the temporal
distance to the next event, with 𝑓 (𝑡) decreasing towards zero when
approaching the next event and 𝑏 (𝑡) increasing towards zero after
                                                                                                                                  Keypoints Transformer. Since some frames may have missing
the previous event. Unlike the relative linear encoding (dashed lines
                                                                                                                               keypoints, represented as NaN values, these coordinates are handled
in Fig. 2b), which does not consider that the prediction task gets
                                                                                                                               explicitly by the Keypoints Transformer as illustrated in Fig. 4
more difficult and uncertain the further the next/previous event
                                                                                                                               top. For each frame, a binary mask marks all keypoints with NaN
is away, the cosine-like signal (dashed lines in Fig. 2c) somehow
                                                                                                                               coordinates as missing. Then, each of the 𝑁 keypoints is projected
captures that by defining a more similar value the further it is away
                                                                                                                               linearly to a latent dimension 𝐷. The result is masked again so
from the next/previous event. We will evaluate experimentally in
                                                                                                                               that no missing keypoint can contribute to the representation. To
Section 4 which temporal time-to-event encoding works best.
                                                                                                                               obtain a fixed-size representation of the keypoints for each frame,
                                                                                                                               a learnable CLS token is appended to the keypoint sequence. The
3.4          EventNet Architecture
                                                                                                                               resulting sequence of 𝑁 + 1 keypoints is processed by a small stack
In our EventNet, we replace the TCN from the baseline model                                                                    of two transformer encoder blocks with multihead self-attention.
[2] with an encoder-only transformer architecture. It consists of a                                                            Again, the attention is masked to ensure that NaN keypoints do not
Keypoints Transformer which converts the sequence of 2d keypoints                                                              influence the self-attention at all. After the encoder, only the CLS
for each frame into a compact per-frame embedding, and a Time-                                                                 output token is retained for each frame as the compact descriptor of
to-Event Transformer which models the temporal evolution of these                                                              the entire keypoint set at time 𝑡. This results in an output sequence
embeddings to predict the values of the time-to-event indicators                                                               z = (z1, . . . , z𝑇 ) with z𝑡 ∈ R𝐷 of shape (𝑇 , 𝐷), which summarizes
𝑓 (𝑡) and 𝑏 (𝑡) for time instances 𝑡. Fig. 1 illustrates this architecture.                                                    the spatial relationships among all visible keypoints over time,
The input to EventNet is a tensor x ∈ R𝑇 ×𝑁 ×2 , where 𝑇 denotes                                                               while remaining robust to missing values.
the number of frames in the sequence, and 𝑁 the number of 2d                                                                      Alternatively, we also implement one variant of Keypoints Trans-
keypoints per frame (see Fig. 3), and the last dimension provides                                                              former where a mask token for each keypoint type is learned and
the normalized (𝑥, 𝑦) coordinates of each keypoint.                                                                            used if an associated keypoint contains NaN values. We will eval-
                                                                                                                               uate experimentally in Sec. 4 which approach of handling NaN
(a) Per-frame feature construction                (b) Build sequence tensor + Adding classification token
                                                                 Frames                                                        keypoints is superior.
   Input frame t


                                                                                                                                   Time-to-Event Transformer. The summarized representation of
                                                                                                                               2d keypoints, obtained as CLS token sequence z, is then passed to
                                                                                                                               the Time-to-Event Transformer, shown in Fig. 5. Here, a stack of
                                                                                            ∈ ℝ!×($%&)×( with 𝑁 = 1 + 6 + 2𝑏
                                                                                                                               three transformer encoder blocks models dependencies across time
                                                     Classification Token (1)

                                                     Player1 keypoints (b)
                                                                                Ball keypoints (1)
                                                                                Player2 keypoints (b)   Table keypoints (6)
                                                                                                                               using multi-head self-attention, residual connections, pre-norm
                                                                                                                               layer normalization, and a position-wise feed-forward network
Figure 3: Construction of the input representation. (a) Key-                                                                   with ReLU activation3 . In this stage, the model captures long-range
points from both players, the table, and the ball are extracted                                                                temporal context across the sequence of per-frame CLS tokens and
and concatenated. Here, 9 per player, 6 for the table, and 1 for                                                               maps them frame-wise to forward and backward time-to-event
the ball, resulting in 25 (𝑥, 𝑦) keypoint coordinates per frame.                                                               indicators. A final linear layer projects each temporal embedding
(b) EventNet input by assembling the pose sequence across                                                                      to the 2d output values corresponding to the predicted 𝑓 (𝑡) and
frames (projection each keypoint to size 𝐷) and adding the                                                                     𝑏 (𝑡) signals. As the prediction targets depend only on the nearest
CLS token of size 𝐷 to each frame.
                                                                                                                               3 In the experimental results section, we will also explore the effect of replacing ReLU
                                                                                                                               by GELU or the whole FFN-block by SwiGLUFFN.
Event Detection in Table Tennis Videos using 2D Keypoints


                                                               (𝐵, 𝑇, 𝑑𝑚𝑜𝑑𝑒𝑙 )
                     (𝐵, 𝑇, 𝐷)                 3×
                                                                          (𝐵, 𝑇, 2) 𝑓) 𝑡 = 0 , 0𝑏 𝑡 = 0
                                                                                                                     3.6     Viewpoint Augmentation
         Extracted                              Add & Norm
 t=0
         CLS token                                                                              .
                                                                                                .                    The LATTE-MV [4] dataset is limited to videos captured from a sin-
                                                    FFN         Output                          .
  .        .                   Input
  .
  .
           .
           .                 Projection                        Projection              𝑓) 𝑡 = 𝑇 − 1 ,                gle, side-view camera viewpoint. This results in a strong viewpoint
                                                Add & Norm                              𝑏, 𝑡 = 𝑇 − 1
         Extracted
                                                                                                                     bias, as real-world table tennis footage exhibits various camera
 t=T-1                                              MSA                                         (𝐵, 2,1)
         CLS token                                                                                                   angles and focal lengths. To improve generalization to unseen view-
                                                                                                           "
                             (𝐵, 𝑇, 𝑑𝑚𝑜𝑑𝑒𝑙 )                                       𝑓) 𝑡 ! , 𝑏, 𝑡 ! , 𝑡 ! =
                                                                                                           #
                                                                                                                     points, the training data is augmented by generating synthetic
                                                                                                                     cameras using the available 3D reconstructions. For each sequence,
Figure 5: Architecture of the Time-to-Event Transformer                                                              a realistic camera is created as follows: The intrinsic parameters are
that takes a CLS token sequence and produces time-to-event                                                           defined by randomly sampling focal lengths and the principal point
indicators 𝑓 (𝑡) and 𝑏 (𝑡).                                                                                          within realistic ranges to construct the intrinsic matrix 𝑀int . The
                                                                                                                     extrinsic parameters are obtained by sampling the camera position
                                                                                                                     in spherical coordinates, including the distance from the table as
neighboring events, the model is trained on fixed-length sequences                                                   well as azimuth and elevation angles, together with a look-at point
and predicts timing indicators for the central time step 𝑚 = ⌊𝑇 /2⌋.                                                 near the table center. From these parameters, the camera position c,
The model is optimized with Huber loss applied to the predicted                                                      forward direction f, right vector r, and up vector u are computed.
forward and backward indicators.                                                                                     The orientation is constrained such that the up vector has a positive
                                                                                                                     𝑧-component, ensuring a physically plausible configuration. These
                                                                                                                     components are then used to construct the extrinsic matrix 𝑀ext .
3.5       Event Extraction
                                                                                                                        Each generated camera is validated by projecting the full 3D
With perfect predictions, all events could be identified at time steps                                               sequence. A camera pose and position is accepted only if more
𝑡 where 𝑓 (𝑡) = 𝑏 (𝑡) = 0. In practice, however, it is challenging for                                               than 95% of all keypoints remain within the image bounds and
a model to perfectly reproduce the target signal, and thus 𝑓 (𝑡) and                                                 the projected scene spans a sufficient portion of the image area.
𝑏 (𝑡) rarely reach zero. Therefore, both indicators are combined into                                                Cameras that do not satisfy these criteria are discarded and resam-
a single discriminative event indicator 𝑟 (𝑡) defined as                                                             pled. Finally, all valid 3D keypoints (players, table, and ball) are
                                                                                                                     projected onto the synthetic camera’s 2d image plane using the
                                          𝑟 (𝑡) = 𝑓 (𝑡) + 𝑏 (𝑡).                                               (3)
                                                                                                                     standard projection equations
Events are then localized in 𝑟 (𝑡) in three steps:                                                                                       rcam = world2cam(rworld, 𝑀ext )                       (5)
       (1) Zero-crossings with a sufficiently positive slope: Can-                                                                        rimg = cam2img(rcam, 𝑀int ).                         (6)
           didate events are found at zero-crossings where 𝑟 (𝑡) sur-                                                These sequences with event annotations are used in training.
           passes upward a threshold of Δℎ. The threshold acts as a
           confidence gate: true events produce strong zero-crossings                                                3.7     Fps Augmentation
           in 𝑟 (𝑡) that reliably exceed Δℎ, while noise-related predic-
                                                                                                                     In the Latte-MV dataset, all videos are recorded at 30 fps. While
           tions remain below it and are filtered out.
                                                                                                                     this is convenient, in real-world scenarios, however, table tennis
       (2) Linear interpolation: The zero-crossing location of each
                                                                                                                     videos are captured at various frame rates. Thus, the training data
           candidate event at time 𝑡 is refined by linear interpolation.
                                                                                                                     was augmented with sequences at diverse fps.
           For consecutive frames where 𝑟 (𝑡) < 0 and 𝑟 (𝑡 + 1) > 0,
                                                                                                                          For every pose, ball, and table keypoint, the same interpolation
           the exact zero-crossing 𝑡 ∗ is computed as
                                                                                                                     scheme is applied. Given 𝑁𝑖𝑛 frames at an input frame rate 𝑓in
                                       (𝑡 + 1) − 𝑡                 𝑟 (𝑡)                                             sampled at time instances 𝑡𝑖in = 𝑓𝑖in , 𝑖 = 0, 1, . . . , 𝑁𝑖𝑛 − 1, a new
           𝑡 ∗ = 𝑡 − 𝑟 (𝑡) ·                          = 𝑡𝑖 −                   ,                               (4)   time grid at output frame rate 𝑓out is constructed at time instances
                                    𝑟 (𝑡 + 1) − 𝑟 (𝑡)        𝑟 (𝑡 + 1) − 𝑟 (𝑡)
                                                                                                                     𝑡 𝑗out = 𝑓out
                                                                                                                                𝑗
                                                                                                                                   , 𝑗 = 0, 1, . . . , 𝑁𝑜𝑢𝑡 − 1 by preserving the total duration T:
           then rounded to the nearest frame index, yielding a re-
                                                                                                                                                        𝑁𝑖𝑛 − 1 𝑁𝑜𝑢𝑡 − 1
           fined time of the event candidate with associated confidence                                                                 𝑇 = 𝑡 𝑁in−1 =          =         .                     (7)
           scores using 𝑠 = 𝑟 (𝑡 + 1) − 𝑟 (𝑡).                                                                                                            𝑓in     𝑓out
       (3) Non-maximum suppression (NMS): We apply NMS to                                                            Thus, 𝑁 out = ⌊𝑇 · 𝑓out ⌋ + 1. Each input dimension 𝑑 of the keypoints
           eliminate redundant event candidates by sorting all event                                                 is then interpolated independently using linear interpolation.
           candidates according to their score 𝑠 and then – starting                                                     The target values for the new sampling rate must be derived
           from the highest scoring – iteratively eliminating all event                                              from the event array 𝑒𝑣𝑒𝑛𝑡𝑐in ∈ {0, 1}𝑁𝑖𝑛 ×2 which encodes two types
           candidates that are within a temporal window of Δ𝑡. This                                                  of events: ball-racket contact of player 1 and player 2. However,
           eliminates redundant detections of the same event.                                                        linear interpolation is not possible with discrete events. It would
                                                                                                                     produce physically meaningless values. Instead, for each column 𝑐,
    Fig. 2c illustrates an example of the network output together with
                                                                                                                     the set E𝑐 of event frame indices where a contact with the racket
the combined event indicator 𝑟 (𝑡). Event occurrences are identified
                                                                                                                     occurs is first extracted. Each event index is then converted to an
at 𝑟𝑐 (𝑡) ≈ 0, where the signal changes sign from negative to positive.
                                                                                                                     absolute timestamp in seconds: 𝜏𝑒 = 𝑓𝑒in ∀𝑒 ∈ E𝑐 . The timestamp is
The first peak occurring around the 10𝑡ℎ frame does not reach the
predefined threshold of Δℎ = 0.5, thereby preventing a false positive                                                mapped to the nearest frame index in the new time grid:
prediction.                                                                                                                        𝑒 out = clip( round(𝜏𝑒 · 𝑓out ) , 0, 𝑁 out − 1) .           (8)
                                                                                        Rainer Lienhart, Daniel Kienzle, Shin’ichi Satoh, and Anastasiia Bilinska


The clipping ensures that the index remains within the valid range.
A new zero array 𝑒𝑣𝑒𝑛𝑡𝑐out ∈ {0, 1}𝑁out ×2 is then constructed, and
each remapped event is placed at its new position:
                           𝑒𝑣𝑒𝑛𝑡𝑐out [𝑒 out, 𝑐] = 1.                    (9)

4 Experimental Results
                                                                               Figure 6: Spatial player assignment logic using table geome-
4.1 Datasets                                                                   try. The net line is defined by the vector between the front-
    Latte-MV. All configurations of our approach were trained and              mid and back-mid keypoints. Player identities are assigned
evaluated on the Latte-MV dataset [4]. The dataset provides an-                by calculating the 2d cross product between this net vector
notations of racket-ball contacts as well as 2d and 3d keypoint                and the vector pointing to each player’s bounding box cen-
annotations for ball, tennis table, and human poses of both players.           ter. The sign of the resulting scalar determines the "left" as
It consists of 9,803 training, 2,099 validation, and 2,103 test videos.        Player 1 and "right" as Player 2, ensuring identity consistency
In case of viewpoint augmentation using 3D reprojection, the aug-              despite camera perspective or player movement.
mentation strategy was only applied to a subset of 2,328 training
and 498 validation videos, for which the 3d ball coordinates were
valid (i.e., not showing NaN values) at least 70% of all frames. The           in each frame using a SegFormer++ B0 model [7, 19], a lightweight
remaining training and validation videos were used without aug-                transformer-based segmentation model. It provides efficient and
mentations. For fps augmentation, the frame rates varied between               accurate per-frame segmentation, which makes it suitable for de-
30 and 60 fps. The test set was never unchanged. The keypoint                  tecting small objects such as the ball and for localizing the table
annotations were rescaled to a resolution of 1920 × 1080 before                tennis table consistently across video frames.
training. Models were trained on a sequence length of 𝑇 = 29, each
configuration 3 times with 3 different seeds.                                  4.2    Architecture details
                                                                               The temporal transformer was trained with a default batch size of
   TTHQ. The TTHQ dataset [8] was used to assess the model on
                                                                               200 for 30 epochs. The model parameters are optimized using the
real-world table tennis footage recorded from very diverse view-
                                                                               Adam optimizer. The initial learning rate is set to 5 · 10−4 , and a
points and a wide variety of scenes. All videos consist of stan-
                                                                               learning rate scheduler is used to improve convergence by reducing
dard or semi-broadcast YouTube content, captured at a resolu-
                                                                               the learning rate by a factor of 𝛾 = 0.3 after epoch 2, allowing
tion of 1920 × 1080 with a static camera setup per video. The
                                                                               the models to fine-tune their weights with smaller updates in later
frame rates range from 25 to 60 fps. From the TTHQ dataset,
                                                                               training stages. Formally, the learning rate at epoch 𝑡 is given by
we only select videos containing two players, as our models are
                                                                               lr𝑡 = 𝛾 𝑘 · lr, where 𝑘 is the number of milestones reached (in this
trained on two-player scenes. The final selection consists of six
                                                                               case, 𝑘 = 1 after epoch 2). This scheduling strategy helps to stabilize
long videos, which were split into shorter clips and recorded under
                                                                               training and improve overall performance.
varying camera viewpoints and frame rates, resulting in a total
                                                                                   In addition to the current state of the time-to-event transformer,
of 56 clips. TTHQ provides annotations of ball-racket contacts
                                                                               an exponential moving average (EMA) of its parameters is main-
and tennis table corners, but not for the 2d poses of the two play-
                                                                               tained during training, and all evaluations and inference exper-
ers and only some for ball positions. Therefore, the players were
                                                                               iments are performed using these EMA weights [14]. The EMA
first localized in each video frame using RT-DETRv2 [12] (model
                                                                               model tracks a smoothed version of the weights, updating accord-
rtdetr_r50vd_coco_o365 4 ). Then, since table tennis involves two
                                                                               ing to:
players in our setup, our algorithm selects the two largest detected
persons in each frame, followed by 2d pose estimation using a                                     𝜃 EMA ← 𝛼 𝜃 EMA + (1 − 𝛼) 𝜃 current,            (10)
ViT-Pose-B model [20] (model vitpose-base-simple 5 ). To en-                   where 𝜃 EMA are the EMA parameters, 𝜃 current the current model
sure consistent player assignment across a video, the two detected             parameters, and 𝛼 = 0.999 the decay factor. This approach stabi-
players are ordered in the input keypoints vector based on their               lizes training by reducing the effect of noisy gradient updates and
spatial position relative to the table net (see Fig. 6). First, the front-     improves evaluation and inference performance.
mid and back-mid table keypoints construct a line representing the                  Two encoder layers with a classification token of dimension 𝑑 =
table net. Next, the center point of each detected player is computed          128 were used to process keypoints. The time-to-event transformer
from his/her bounding box. The sign of the cross product between               uses three encoder layers, and the output consists of two predicted
the net direction vector and the vector from the front-mid net point           values per frame: 𝑓ˆ(𝑡) (predicted forward timing indicator) and
to each player determines whether a player is located on the “left”            𝑏ˆ (𝑡) (predicted backward timing indicator). The combined event
or “right” side of the table.                                                  indicator 𝑟ˆ (𝑡) was used for discrete event extraction as described
   From the full set of predicted pose keypoints, only a subset rele-          in Section 3.5, with non-maximum suppression applied using a
vant to the upper body is used. These are: head, left/right shoulder,          window size of 𝑤 = 7 frames and a minimal peak height of 0.5.
left/right elbow, left/right wrist, and left/right hip. Thus, each player is
represented by nine 2d keypoints. The table and ball were detected             4.3    Evaluation metrics
4 https://github.com/lyuwenyu/RT-DETR                                          For evaluation, we let a trained model process a complete test
5 https://github.com/ViTAE-Transformer/ViTPose                                 video set to predict all ball-racket contact events. We assign to each
Event Detection in Table Tennis Videos using 2D Keypoints


ground truth event in the test set the closest predicted event if and    the relative linear target signal performs overall best with an avg.
only if it is within an absolute temporal distance of Δ𝑡 frames. Thus,   F1-Score of 89.00/ 89.91 over the cosine-like with 88.39/ 89.69 and
a predicted event is considered correct if (a) its absolute temporal     absolute linear with 88.22 / 86.17 for masking / mask tokens for NaN
distance to the assigned ground truth does not exceed the maximum        values. However, its average mean L1 frame difference is minimally
allowed frame distance Δ𝑡 and (b) there is no other closer predicted     higher with a value of 0.42 / 0.41 versus 0.40 / 0.41 for cosine-like,
event. In our experiments, we have chosen a default threshold of         but much better than absolute linear with 0.46 / 0.43. This clearly
Δ𝑡 = 3 frames.                                                           shows the advantage of both relative target event signals. The effect
   Having defined what correct event detections are, we can now          is more pronounced on TTHQ, where both relative temporal target
compute precision, recall, and F1 score (in percentage) over a com-      signal encodings outperform absolute linear by about 3.5%.
plete test video dataset. The F1 score is the harmonic mean of
                                                                            FFN Variants. If we analyze the F1 test scores on the Latte-MV
precision and recall. Instead of a simple average, a harmonic mean
                                                                         dataset in Table 1 for our best configuration (NO, mask tokens for
punishes extreme failures. Thus, F1 will be our main performance
                                                                         NaN values), and average the three values for the different temporal
score. Additionally, the mean absolute frame deviation (short L1
                                                                         event encoding types, we observe that GELU performs best on Latte-
Diff ) of all correctly detected events (i.e., true positives) is also
                                                                         MV. It achieves an average F1 test score of 88.62, surpassing ReLU
reported. A value of, for instance, 0.5 means that on average the
                                                                         and SwiGLUFFN marginally with scores of 88.56 and 88.59. On the
error is 1/2 of a frame.
                                                                         challenging TTHQ dataset, the gap is a little bit larger with 69.68
                                                                         compared to 69.14 and 68.44 for GELU and SwiGLUFFN. Given
4.4     Experiments Results and Ablation Study
                                                                         that TTHQ serves as a reliable proxy for out-of-training-domain
In this section, we systematically evaluate each proposed compo-         performance (with variable frame rates and viewing angles), GELU
nent and its various implementation options. The experiments are         emerges as the most suitable training option here.
structured to validate our key design choices and demonstrate its
performance. We start from the following default configuration: All         Keypoint Set. In table tennis, the ball isn’t always easy to see
models are exclusively trained on Latte-MV with a sequence length        or visible. Therefore, one idea was to use the players’ upper-body
of 𝑇 = 29 using Adam as the optimizer and tested on Latte-MV’s           joints as reference keypoints to help determine the timing of the
and TTHQ’s test set. We further use fps and viewpoint augmenta-          ball-racket contact more reliably and, potentially, more accurately.
tion, a maximum allowed frame distance of Δ𝑡 = 3 and ReLUs. The          We tested therefore whether the keypoint set UB outperforms the
input keypoints consist of the ball center, the six table keypoints,     keypoints set NO. Table 1 gives here a clear answer. If the focus is
and 2 times the 9 upper body keypoints of both players.                  on the best performing configuration using mask tokens for NaN
                                                                         values and averaging over all time-to-event signal and FFN variants,
4.4.1 TCN-based Baseline vs. Our EventNet. We compare the per-           we see that NO outperforms UB by 2.31% (88.59 vs. 86.28) on Latte-
formance of the TCN baseline with our transformer-based EventNet         MV and by 2.12% (69.09 vs. 66.97) on TTHQ. Similar results can be
using the absolute linear time-to-event encoding ("absLin" for short)    determined for the choice of mask NaN values. Note also that the
introduced by the baseline and our novel cosine-like signal ("cos"       average L1 difference is slightly lower for keypoint set NO than UB.
for short) in the top two sections of Table 2. The first section shows   Thus, body pose does not help in our specific event detection task.
the results for the keypoint set without human poses (NO), while         Probably, the reversal of the ball’s direction provides the clearest
the second section with all keypoints of the upper bodies of both        signal for the example event detection task chosen.
players (UB). We can see that our EventNet on Latte-MV test set
outperforms the baseline on keypoint set NO by absolute +6.2%                FPS and Viewpoint Augmentation with Random Cameras. The
and +3.8% on "absLin" and "cos", respectively, while on keypoint set     third and last section of Table 2 shows the effect of our fps and
UB by +1.5% and −2.4%, respectively. The avg. L1 distance slightly       viewpoint augmentations on inference performance. Contrary to
improves from 0.4 to 0.5 for the baseline to a constant 0.4 with         expectations, fps augmentation does not consistently help. While it
EventNet. On the challenging TTHQ test set we see an increase in         is clear that it should slightly degrade the performance on Latte-MV
absolute F1 score by EventNet over the baseline between 22.1% and        with consistent 30 fps videos, it only shows its benefit on TTHQ
31.5%. Furthermore, the transformer-architecture significantly ac-       if combined with viewpoint augmentation. Here, the F1 score of
celerated training and inference by reducing the runtime between a       61.0% without any augmentation increases to 70.5% with viewpoint
factor of 0.32 and 0.48 on various GPU-platforms (e.g. with a single     augmentations and further absolute 3.2 points to 73.8% by adding
Nvidia RTX 3090, RTX 4090, A100, and Apple M4 Max).                      also fps augmentations. Thus, viewpoint augmentations are highly
                                                                         effective to adapt to different viewpoints, while fps augmentation
4.4.2 Ablation Study. Table 1 shows test results on Latte-MV and         needs viewpoint augmentations to show its benefit.
TTHQ using many variants of our EventNet architecture. In Table
1, all models are exclusively trained on Latte-MV using fps and          5   Conclusion
viewpoint augmentation, a sequence length of 𝑇 = 29, a maximum
                                                                         We have presented a practical approach to event detection in table
allowed frame distance of Δ𝑡 = 3, and Adam as optimizer.
                                                                         tennis that combines compact 2D keypoint representations with
   Temporal Event Encoding. If we look at the F1 test score on the       transformer-based temporal modeling. In contrast to relying on raw
Latte-MV dataset using the better performing keypoint set NO in          video input directly, 2D keypoints are very efficient and generalize
Table 1 and average within each temporal event encoding type             to diverse environmental settings very well. Therefore, EventNet is
the three scores for the different FFN incarnations, we see that         a modular solution for sports analysis in challenging video settings.
                                                                                   Rainer Lienhart, Daniel Kienzle, Shin’ichi Satoh, and Anastasiia Bilinska


Table 1: Test results on Latte-MV and TTHQ using our EventNet. The models are exclusively trained 3 times with Adam on
Latte-MV using fps and viewpoint augmentation, a sequence length of 𝑇 = 29 and a maximum allowed frame distance of Δ𝑡 = 3.
The temporal encoding and the non-linearity used in the FFN blocks of all transformer layers are set as specified for each
configuration. "L1 Diff" stands for mean absolute frame distance between predicted and ground truth event frames.


                                                   Mask all NaN Values                                   Mask Tokens for NaN Values
                                            Latte-MV                  TTHQ                            Latte-MV                  TTHQ
 Configuration                        F1 Score     L1 Diff     F1 Score    L1 Dff               F1 Score     L1 Diff     F1 Score    L1 Diff
 NO, relative linear, ReLU          89.51 ±0.67    0.42 ±0.02    69.25 ±2.75   1.14 ±0.05     89.58 ±1.00       0.38 ±0.01       73.08 ±3.92       1.16 ±0.01
 NO, relative linear, GELU          89.06 ±1.56    0.42 ±0.00    70.33 ±5.44   1.13 ±0.05     88.99 ±2.30       0.41 ±0.04       68.69 ±0.63       1.18 ±0.10
 NO, relative linear, SwiGLUFFN     88.44 ±1.32    0.43 ±0.02    68.72 ±4.34   1.05 ±0.09     91.16 ±1.28       0.42 ±0.02       70.61 ±2.11       1.25 ±0.09
 NO, cosine-like, ReLU              87.48 ±1.81    0.39 ±0.01    71.19 ±1.14   1.16 ±0.07     89.54 ±0.18       0.40 ±0.01       68.86 ±4.35       1.28 ±0.12
 NO, cosine-like, GELU              87.89 ±0.24    0.38 ±0.02    71.36 ±3.22   1.04 ±0.06     89.84 ±1.61       0.43 ±0.02       73.76 ±2.33       1.27 ±0.09
 NO, cosine-like, SwiGLUFFN         89.79 ±1.38    0.42 ±0.02    69.13 ±4.66   1.17 ±0.07     89.70 ±2.29       0.40 ±0.01       71.21 ±4.02       1.18 ±0.04
 NO, absolute linear, ReLU          88.20 ±0.56    0.46 ±0.03    68.25 ±3.40   1.02 ±0.05     86.55 ±0.95       0.43 ±0.04       65.49 ±2.12       1.13 ±0.11
 NO, absolute linear, GELU          88.82 ±1.02    0.48 ±0.02    66.01 ±3.18   1.06 ±0.07     87.04 ±2.13       0.43 ±0.02       66.59 ±5.01       1.12 ±0.11
 NO, absolute linear, SwiGLUFFN     87.63 ±2.42    0.44 ±0.03    67.11 ±3.67   1.11 ±0.07     84.92 ±1.56       0.43 ±0.01       63.50 ±2.79       1.12 ±0.10
 UB, relative linear, ReLU          88.40±1.32     0.40±0.04     64.34±3.66    1.08±0.13      85.35±2.05        0.37±0.02        66.96±3.12        1.18±0.08
 UB, relative linear, GELU          89.06±1.10     0.43±0.00     69.70±2.80    1.26±0.13      86.94±0.21        0.37±0.03        68.79±0.88        1.22±0.11
 UB, relative linear, SwiGLUFFN     87.20±4.98     0.39±0.02     67.74±7.17    1.09±0.15      87.36±1.32        0.38±0.04        70.18±1.84        1.24±0.05
 UB, cosine-like, ReLU              87.92±1.08     0.39±0.01     68.85±3.45    1.17±0.06      84.54±0.73        0.37±0.05        68.02±0.48        1.25±0.04
 UB, cosine-like, GELU              89.63±0.37     0.40±0.02     73.79±3.85    1.13±0.09      85.86±3.23        0.39±0.04        67.61±1.31        1.35±0.08
 UB, cosine-like, SwiGLUFFN         87.91±2.04     0.39±0.02     68.99±4.40    1.19±0.15      87.95±1.75        0.39±0.04        67.54±3.53        1.23±0.03
 UB, absolute linear, ReLU          86.98±1.99     0.46±0.02     62.98±0.75    1.14±0.10      84.70±4.27        0.43±0.02        64.64±1.86        1.23±0.08
 UB, absolute linear, GELU          86.35±0.47     0.46±0.01     62.56±5.20    1.06±0.07      86.53±2.16        0.43±0.02        63.76±1.08        1.07±0.02
 UB, absolute linear, SwiGLUFFN     87.79±0.74     0.44±0.03     65.49±3.42    1.02±0.03      87.27±1.57        0.44±0.04        65.20±4.51        1.05±0.05



                          Latte-MV                  TTHQ                 keypoint and a time-to-event encoder) outperforms (speed- and
 Model               F1 Score    L1 Diff      F1 Score  L1 Dff           performance-wise) a temporal convolutional network (TCN) sub-
                                                                         stantially. (2) If the training data set is recorded at a fixed fps, the
 NO Base cos        86.0±2.55     0.4±0.02    46.4±0.85    0.6±0.06
                                                                         proposed fps data augmentation and a relative temporal time-to-
 NO EN cos          89.8±1.61     0.4±0.02    73.8±2.33    1.3±0.09
                                                                         event indicator signal (either relative linear or cosine-like) can
 NO Base absLin     80.8±1.56     0.5±0.03    44.5±0.28    0.5±0.02
                                                                         transfer to variable fps rates of test videos. (3) If the training data
 NO EN absLin       87.0±2.13     0.4±0.02    66.6±5.01    1.1±0.11
                                                                         set is recorded from a fixed camera view, the proposed viewpoint
 UB Base cos        88.3±0.33     0.4±0.08    36.1±2.89    0.6±0.07      augmentation and a relative temporal time-to-event indicator signal
 UB EN cos          85.9±3.23     0.4±0.04    67.6±1.31    1.3±0.08      can transfer to variable viewpoints of test videos. However, there
 UB Base absLin     85.0±0.14     0.5±0.05    35.5±6.09    0.6±0.10      are viewpoint cases where the event is not visible and therefore the
 UB EN absLin       86.5±2.16     0.4±0.02    63.8±1.08    1.1±0.02      overall temporal precision suffers (e.g., frontal views in table tennis).
 NO EN cos 3d fps   89.8 ±1.61    0.4 ±0.02   73.8 ±2.33   1.3 ±0.09     (4) The upper body pose of the table tennis player did not help in
 NO EN cos 3d –     92.6 ±0.49    0.4 ±0.02   70.5 ±2.10   1.0 ±0.06     the case of ball-racket contact estimation, except in cases where the
 NO EN cos – fps    92.3 ±0.27    0.4 ±0.02   55.5 ±3.75   0.9 ±0.02     ball is not visible such as for frontal view recordings. In all other
 NO EN cos – –      94.0 ±0.09    0.4 ±0.00   61.0 ±3.72   0.9 ±0.22     cases, the upper body pose degraded the temporal precision in time
                                                                         as the ball - if visible - is the best indicator for identifying the point
Table 2: Performance comparison of the TCN baseline (Base)               of time when the ball changes its direction. Despite that we focus
with EventNet (EN, mask tokens for NaN values + fps and                  on racket-ball contact in this paper, our approach is transferable to
viewpoint augmentation) using the original absolute lin-                 all kinds of motion event detection.
ear (absLin) and our cosine-like (cos) time-to-event signal
(top/middle section using keypoint set NO/UB). Bottom sec-               Acknowledgments
tion shows the effect if we use or one of the two data aug-              The authors gratefully acknowledge the resources on the LiCCA
mentation strategies.                                                    HPC cluster of the University of Augsburg, co-funded by the Deutsche
                                                                         Forschungsgemeinschaft (DFG, German Research Foundation) –
                                                                         Project-ID 499211671. This work was partly supported by JSPS Invi-
  Several central findings were discovered in this work. (1) A           tational Fellowship for Research in Japan (Long-Term L26503) and
smartly designed small transformer-based architecture (using a           by JST ASPIRE JPMJAP2303.
Event Detection in Table Tennis Videos using 2D Keypoints


References                                                                                [19] Enze Xie, Wenhai Wang, Zhiding Yu, Anima Anandkumar, Jose M. Alvarez, and
 [1] Shaojie Bai, J. Zico Kolter, and Vladlen Koltun. 2018. An Empirical Evaluation of         Ping Luo. 2021. SegFormer: Simple and efficient design for semantic segmentation
     Generic Convolutional and Recurrent Networks for Sequence Modeling. doi:10.               with transformers. Advances in Neural Information Processing Systems 34 (2021),
     48550/arXiv.1803.01271 arXiv:1803.01271 [cs.LG].                                          12077–12090.
 [2] Moritz Einfalt, Charles Dampeyrou, Dan Zecha, and Rainer Lienhart. 2019.             [20] Yufei Xu, Jing Zhang, Qiming Zhang, and Dacheng Tao. 2022. ViTPose: Sim-
     Frame-Level Event Detection in Athletics Videos with Pose-Based Convo-                    ple Vision Transformer Baselines for Human Pose Estimation. arXiv preprint
     lutional Sequence Networks. In Proceedings Proceedings of the 2nd Interna-                arXiv:2204.12484 (2022). https://arxiv.org/abs/2204.12484
     tional Workshop on Multimedia Content Analysis in Sports (Nice, France) (MM-         [21] Kentaro Yagi, Kunihiro Hasegawa, Yuta Sugiura, and Hideo Saito. 2018. Esti-
     Sports ’19). Association for Computing Machinery, New York, NY, USA, 42–50.               mation of Runners’ Number of Steps, Stride Length and Speed Transition from
     doi:10.1145/3347318.3355525                                                               Video of a 100-Meter Race. In Proceedings of the 1st International Workshop on
 [3] Moritz Einfalt and Rainer Lienhart. 2020. Decoupling Video and Human Mo-                  Multimedia Content Analysis in Sports. ACM, Seoul Republic of Korea, 87–95.
     tion: Towards Practical Event Detection in Athlete Recordings. arXiv preprint             doi:10.1145/3265845.3265850
     arXiv:2004.09776 (2020). https://doi.org/10.48550/arXiv.2004.09776 Accepted
     at 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition
     Workshop (CVPRW).
 [4] Daniel Etaat, Dvij Kalaria, Nima Rahmanian, and S. Shankar Sastry. 2025. LATTE-
     MV: Learning to Anticipate Table Tennis Hits from Monocular Videos. In Pro-
     ceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition
     (CVPR). 7115–7124.
 [5] Pablo Fernández de Dios, Qinggang Meng, and Paul W. H. Chung. 2013. A
     Machine Learning Method for Identification of Key Body Poses in Cyclic Physical
     Exercises. In Proceedings of the 2013 IEEE International Conference on Systems,
     Man, and Cybernetics. IEEE, 1605–1610.
 [6] Silvio Giancola, Mohieddine Amine, Tarek Dghaily, and Bernard Ghanem. 2018.
     SoccerNet: A Scalable Dataset for Action Spotting in Soccer Videos. In Proceed-
     ings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
     Workshops. IEEE.
 [7] Daniel Kienzle, Marco Kantonis, Robin Schön, and Rainer Lienhart. 2024. Seg-
     former++: efficient token-merging strategies for high-resolution semantic seg-
     mentation. In IEEE International Conference on Multimedia Information Processing
     and Retrieval (MIPR) 2024, San Jose, CA, USA, August 7-9, 2024, Guan-Ming Su,
     Homer Chen, Ming-Ching Chang, Mohan Kankanhalli, Prabhakaran Balakrish-
     nan, and Dae Yeol Lee (Eds.). 75 – 81. doi:10.1109/MIPR62202.2024.00019
 [8] Daniel Kienzle, Katja Ludwig, Julian Lorenz, Shin’Ichi Satoh, and Rainer Lien-
     hart. 2026. Uplifting Table Tennis: A Robust, Real-World Application for 3D
     Trajectory and Spin Estimation. In Proceedings of the IEEE/CVF Winter Conference
     on Applications of Computer Vision (WACV). 7440–7449.
 [9] Daniel Kienzle, Robin Schön, Rainer Lienhart, and Shin’Ichi Satoh. 2025. Towards
     ball spin and trajectory analysis in table tennis broadcast videos via physically
     grounded synthetic-to-real transfer. In 2025 IEEE/CVF International Conference
     on Computer Vision and Pattern Recognition Workshops (CVPRW), 11-12 June 2025,
     Nashville, TN, USA. 5832 – 5841. doi:10.1109/CVPRW67362.2025.00582
[10] Haojie Li, Jinhui Tang, Si Wu, Yongdong Zhang, and Shouxun Lin. 2010. Auto-
     matic Detection and Analysis of Player Action in Moving Background Sports
     Video Sequences. IEEE Transactions on Circuits and Systems for Video Technology
     20, 3 (March 2010), 351–364.
[11] R. Lienhart, M. Einfalt, and D. Zecha. 2018. Mining Automatically Estimated
     Poses from Video Recordings of Top Athletes. International Journal of Computer
     Science in Sport 17, 2 (Dec. 2018), 94–112. doi:10.2478/ijcss-2018-0005
[12] Wenyu Lv, Yian Zhao, Qinyao Chang, Kui Huang, Guanzhong Wang, and Yi
     Liu. 2024. RT-DETRv2: Improved Baseline with Bag-of-Freebies for Real-Time
     Detection Transformer. arXiv:2407.17140 [cs.CV] https://arxiv.org/abs/2407.
     17140
[13] Long Sha, Patrick Lucey, Sridha Sridharan, Stuart Morgan, and Dave Pease. 2014.
     Understanding and Analyzing a Large Collection of Archived Swimming Videos.
     In Proceedings of the IEEE Winter Conference on Applications of Computer Vision
     (WACV). IEEE, 674–681.
[14] Antti Tarvainen and Harri Valpola. 2017. Mean teachers are better role models:
     Weight-averaged consistency targets improve semi-supervised deep learning
     results. In Proceedings of the 31st International Conference on Neural Information
     Processing Systems (Long Beach, California, USA) (NIPS’17). Curran Associates
     Inc., Red Hook, NY, USA, 1195–1204.
[15] Claudio Marcio de Souza Vicente, Erickson R. Nascimento, Luiz Eduardo C.
     Emery, Cristiano Arruda G. Flor, Thales Vieira, and Leonardo B. Oliveira. 2016.
     High Performance Moves Recognition and Sequence Segmentation Based on Key
     Poses Filtering. In Proceedings of the 2016 IEEE Winter Conference on Applications
     of Computer Vision (WACV). IEEE, 1–8.
[16] Brandon Victor, Zhen He, Stuart Morgan, and Dino Miniutti. 2017. Continuous
     Video to Simple Signals for Swimming Stroke Detection with Convolutional
     Neural Networks. In Proceedings of the IEEE Conference on Computer Vision and
     Pattern Recognition (CVPR) Workshops. IEEE.
[17] Timothy Woinoski, Alon Harell, and Ivan V. Bajic. 2020. Towards Auto-
     mated Swimming Analytics Using Deep Neural Networks. arXiv preprint
     arXiv:2001.04433 (2020).
[18] Chuan Wu, Yu-Fei Ma, Hong-Jiang Zhang, and Yu-Zhuo Zhong. 2002. Events
     Recognition by Semantic Inference for Sports Video. In Proceedings of the IEEE
     International Conference on Multimedia and Expo (ICME), Vol. 1. IEEE, 805–808.

```
