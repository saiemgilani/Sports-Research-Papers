<!-- source: 2026 ELASTIC - Trajectory-Based Synchronization of Event and Tracking Data in Soccer - Kim et al.pdf -->
<!-- arxiv: https://arxiv.org/abs/2608.30227 -->

arXiv:2608.30227v1 [cs.DB] 31 Aug 2026

ELASTIC: Trajectory-Based Synchronization of Event and Tracking Data in Soccer Hyunsung Kim∗

Hoyoung Choi

Kunhee Lee

Sangwoo Seo

KAIST Daejeon, South Korea hyunsung.kim@kaist.ac.kr

KAIST Daejeon, South Korea chy3724@kaist.ac.kr

KAIST Daejeon, South Korea kunhee8@kaist.ac.kr

KAIST Daejeon, South Korea sangwooseo@kaist.ac.kr

Tom Boomstra

Jinsung Yoon

Chanyoung Park

AFC Ajax Amsterdam, Netherlands t.boomstra@ajax.nl

Fitogether Inc. Seoul, South Korea jinsung.yoon@fitogether.com

KAIST Daejeon, South Korea cy.park@kaist.ac.kr

Abstract Combining event and tracking data is fundamental to modern soccer analytics, yet the two sources are rarely well aligned: event timestamps recorded by human annotators often miss the true moment of the action, distorting the spatiotemporal context that downstream models rely on. Existing synchronization methods depend on noisy human-annotated event locations and fail to detect ball receptions, obscuring when each player gains ball possession. To address these limitations, we propose ELASTIC (Event-Location-AgnoSTIC synchronizer), a framework that infers the start and end timestamps of events solely from player and ball trajectories, without relying on annotated event locations. To recover ball receptions, ELASTIC enriches the event sequence by inserting virtual termination events between consecutive events, so that the end of each event is detected jointly with its start. It then extracts a sparse set of candidate frames where ball touches are physically plausible, and aligns the termination-inserted event sequence with the candidate-frame sequence using an extended Needleman-Wunsch algorithm. For reproducible evaluation, we construct a publicly available benchmark by annotating ground-truth timestamps on the Sportec Open DFL Dataset, on which ELASTIC substantially outperforms existing methods. Through downstream task evaluation, we further show that improved synchronization translates into measurable gains in soccer analytics. The source code and benchmark are available at https://github.com/hyunsungkim-ds/elastic.git.

CCS Concepts • Information systems → Data mining; Information integration; Spatial-temporal systems; • Theory of computation → Dynamic programming.

Keywords Sports Analytics; Data Quality; Multimodal Data Fusion; TimeSeries Synchronization; Sequence Alignment ∗ Also with Fitogether Inc..

This work is licensed under a Creative Commons Attribution 4.0 International License. CIKM ’26, Rome, Italy © 2026 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-2539-5/2026/11 https://doi.org/10.1145/3799682.3841035

ACM Reference Format: Hyunsung Kim, Hoyoung Choi, Kunhee Lee, Sangwoo Seo, Tom Boomstra, Jinsung Yoon, and Chanyoung Park. 2026. ELASTIC: Trajectory-Based Synchronization of Event and Tracking Data in Soccer. In Proceedings of the 35th ACM International Conference on Information and Knowledge Management (CIKM ’26), November 07–11, 2026, Rome, Italy. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/3799682.3841035

1

Introduction

The increasing availability of fine-grained in-game data has reshaped the landscape of soccer analytics. Among the various data modalities, two stand out as primary pillars: event data and tracking data. The former consists of manually annotated records of key on-ball actions such as passes, shots, and tackles, whereas the latter captures the positions of all players and the ball at every moment of the game through optical or wearable sensor-based systems. When properly combined, these two sources support a wide range of downstream tasks, such as quantifying the scoring probability of a shot [1, 6, 14, 15, 24], analyzing passing options in a given situation [2, 9, 10, 20–22, 26], and evaluating players’ abilities [8, 12, 23, 27, 28]. In practice, however, aligning these two sources is challenging. Event data is typically annotated by humans, meaning that the recorded timestamp often does not precisely correspond to the moment when the player actually performed the action. When such event records are naively combined with tracking data, the resulting player and ball configurations may be inaccurate, thereby distorting the spatiotemporal context used in downstream tasks. For this reason, synchronizing event and tracking data has become a central problem in soccer analytics [4, 19, 29]. More generally, the task belongs to a broader class of multimodal sequence alignment problems, in which sparse semantic records (i.e., event data) must be precisely aligned with dense temporal signals (i.e., tracking data). To address this issue, several methods have been proposed to synchronize soccer event and tracking data. Biermann et al. [4] introduced a learning-based approach that applies a sliding window over tracking data and uses aggregated window features to classify whether each window’s center frame corresponds to a pass. Anzer et al. [1] and Van Roy et al. [29] proposed distance-based methods that define a window around the annotated event timestamp and find the frame that minimizes the sum of distances between the annotated event location, ball location, and event player location.

CIKM ’26, November 07–11, 2026, Rome, Italy

Hyunsung Kim et al.

R

Event-ball distance (m)

25

(a) Snapshot

P

20 15 10 5 0

20

40

60

Frame ID

80

100

(b) Event-ball distance

Figure 1: A sample pass by player #12, where R and P mark the locations and moments of the ball reception (frame 38) and the pass (frame 79), respectively. (a) The white circle with a black tail shows the ball trajectory, and the star marks the annotated pass location, which deviates from the ball’s actual position at P. (b) The distance between the ball and the annotated pass location over time reaches its minimum near R rather than P, misleading distance-based synchronizers.

Oonk et al. [18, 19] used the Needleman-Wunsch algorithm [17] to find the globally optimal alignment between the two modalities while preserving the order of events. Meanwhile, another line of work detects events directly from tracking data without using event data at all [5, 16, 31], but such approaches recover only a limited set of event types defined by their own detection rules. We therefore focus on synchronizing the fine-grained event records that already exist, rather than regenerating them. Existing synchronization methods, however, share several limitations. First, they depend on manual annotations that are noisy and labor-intensive. Anzer et al. [1], Van Roy et al. [29], and Oonk et al. [18, 19] use the distance between the human-annotated event location and the ball as a primary scoring criterion, favoring frames with small event-ball distances. Since the annotated event locations are themselves spatially noisy, this criterion can select an incorrect frame. Fig. 1 illustrates such a failure: player #12 receives the ball at frame 38 (R) and passes it at frame 79 (P), but the annotated pass location (the star) lies closer to the reception point (R) than to the position where the pass is actually made (P), causing these methods to wrongly select the receiving moment as the estimated pass timestamp. Biermann et al. [4] instead rely solely on tracking features, but their method requires ground-truth labels to learn the feature distributions of pass and non-pass windows, and operates on coarse window-level features rather than fine frame-level cues, which limits its final accuracy. In addition, existing methods do not detect ball-receiving events. Anzer et al. [1] synchronize only shots, Biermann et al. [4] focus only on passes, and Oonk et al. [18, 19] extend coverage to passes, shots, tackles, and dribbles, but none of them detects the moment when a player receives the ball. This is partly because many data providers do not explicitly record ball-receiving events; as a result, even Van Roy et al. [29], whose method covers all recorded events, leave them unsynchronized. However, the absence of accurate ball-reception timing precludes downstream analyses such as reconstructing each player’s ball possession intervals [13] or analyzing passes conditioned on their destinations [9, 10, 26].

To overcome these challenges, we propose ELASTIC (EventLocation-AgnoSTIC synchronizer), a trajectory-based synchronization framework that detects both the start and end timestamps of events without relying on annotated event locations. To address the first limitation, ELASTIC infers event timings solely from player and ball trajectories, using features such as player-ball distance and ball acceleration to extract candidate frames that mark potential ball touches. To address the second, we explicitly recover ball receptions by enriching the event sequence with virtual termination events inserted between consecutive events, so that the end of each event is detected jointly with its start. We then find the optimal, order-preserving alignment between the termination-inserted event sequence and the candidate-frame sequence within each in-play segment using an extended Needleman-Wunsch algorithm [17]. Beyond the methodology, we make two practical contributions. First, we construct a reproducible benchmark by annotating true event timestamps on the Sportec Open DFL Dataset [3], enabling other researchers to reproduce our experiments and use the benchmark in other analyses. This is particularly important because prior studies have relied on proprietary data or indirect evaluation protocols. Second, we go beyond synchronization accuracy itself and evaluate how it affects downstream tasks including next action prediction and pass success prediction [12, 22, 27]. By doing so, we show that synchronization is not merely a technical alignment task but a practically consequential component that materially affects the quality of diverse soccer analytics. In summary, this paper makes the following contributions: • We propose ELASTIC, a framework for synchronizing event and tracking data in soccer that does not rely on humanannotated event locations, combining candidate frame extraction with an adapted sequence alignment algorithm. • We enable the framework to recover ball receptions by detecting the end of each event as well as its start, through virtual termination events inserted into the event sequence. • We construct a reproducible evaluation benchmark by annotating ground-truth timestamps on a publicly available dataset and show that ELASTIC achieves substantial improvements over existing baselines. • We further demonstrate through downstream task evaluation that improved synchronization leads to practically meaningful gains in soccer analytics.

2

Proposed Framework

Given a pair of event and tracking data from a soccer match, our objective is to infer the true start and end timestamps of each on-theball event. Formally, the event data is a sequence 𝐸 = (𝑒 1, . . . , 𝑒𝑀 ), where each event specifies its type (e.g., pass, shot, or tackle) and the involved player. The tracking data is a sequence of snapshots 𝑋 = (x1, . . . , x𝑇 ) recorded at 10 or 25 frames per second (FPS), where each snapshot contains the 2D position of all players, the 3D position of the ball, and a binary indicator of whether the frame is in play. Given 𝐸 and 𝑋 , our goal is to find a pair of tracking frames (i.e., snapshot indices) (𝑡𝑖start, 𝑡𝑖end ) corresponding to the true moments when each event 𝑒𝑖 was initiated and terminated, while preserving the event order as follows: start end 1 ≤ 𝑡 1start ≤ · · · ≤ 𝑡𝑖start ≤ 𝑡𝑖end ≤ 𝑡𝑖+1 ≤ · · · ≤ 𝑡𝑀 ≤𝑇.

(1)

ELASTIC: Trajectory-Based Synchronization of Event and Tracking Data in Soccer

ELASTIC finds these timestamps through five stages: data preprocessing (Section 2.1), selecting candidate frames representing possible ball touches (Section 2.2), calculating a compatibility score between every event and candidate frame in each episode (Section 2.3), aligning the event and the candidate-frame sequences using a “repeat-augmented” Needleman-Wunsch algorithm (Section 2.4), and postprocessing to refine the alignment (Section 2.5).

2.1

Data Preprocessing

First, following Oonk et al. [19], we split each match into segments of consecutive in-play frames, which we call episodes [11], and align each episode independently. While aligning 𝐸 = (𝑒 1, . . . , 𝑒𝑀 ) and 𝑋 = (x1, . . . , x𝑇 ) at once requires the quadratic time complexity of O (𝑀𝑇 ), this episode batching substantially reduces this cost to O (𝐾𝑀 ′𝑇 ′ ) where 𝐾 ≈ 100 is the number of episodes in a match and 𝑀 ′ ≪ 𝑀 and 𝑇 ′ ≪ 𝑇 are the number of events and tracking frames in the longest episode, respectively. Following prior work [29], we then convert the raw event data into the Soccer Player Action Description Language (SPADL) format [7] and group events into four categories that share behavior patterns in tracking signals: • Open-play outgoing: pass, cross, clearance, shot, shot_block, keeper_punch, bad_touch • Set-piece outgoing: throw_in, goal_kick, corner_short, corner_crossed, freekick_short, freekick_crossed, shot_freekick, shot_penalty • Incoming: interception, ball_recovery, keeper_save, keeper_claim, keeper_pickup • Minor: tackle, dispossessed A different scoring rule is applied to each category in Section 2.3. Lastly, to determine both the start and end timestamps of every event through a single alignment per episode, we explicitly insert virtual termination events between consecutive events. Specifically, we conditionally insert one of three virtual events between each pair of adjacent events (𝑒𝑖 , 𝑒𝑖+1 ) as follows: • When the current event 𝑒𝑖 is a successful shot followed by a kick-off pass, we insert a goal event. • When the next event 𝑒𝑖+1 is either a throw-in, a goal kick, or a corner kick, we insert an out event. • When 𝑒𝑖 and 𝑒𝑖+1 belong to the same episode and are executed by different players, we insert a control event indicating a ball reception by the next acting player. • Otherwise, we do not insert a virtual event. The resulting enriched sequence alternates as start (original) → end (inserted) → start (original) → end (inserted) → · · · , allowing every original event’s initiation and termination to be determined jointly by a single alignment per episode.

2.2

Candidate Frame Selection

Oonk et al. [19] first applied the Needleman-Wunsch algorithm [17] to align event and tracking sequences while treating every in-play frame as a potential match for each event. However, this exhaustive treatment has two drawbacks. First, as tracking data collected from a match at 25 FPS contains about 90,000 in-play frames (i.e., about 60 minutes), filling the dynamic programming (DP) table over all

CIKM ’26, November 07–11, 2026, Rome, Italy

in-play frames is computationally expensive even with dead-ball batching. Second, most in-play frames are not physically plausible candidates for on-the-ball events, since the ball is often not sufficiently close to any player or does not exhibit a meaningful change in motion at those moments. Including such frames as matching candidates therefore increases the likelihood of spurious alignments in situations where no event could realistically occur. To avoid these issues, we extract a sparse subset of candidate frames from each episode before the alignment in Section 2.4. Specifically, we consider the following frames as candidates: (a) local minima of the distance between the ball and a player, capturing the player’s potential ball touches; (b) local minima of the distance between the ball and a pitch boundary (i.e., a side line or an end line), capturing the moment the ball goes out of play for out and goal events; (c) local maxima of the ball acceleration, capturing a sudden change in the ball’s direction that may not coincide with a distance valley. Conditions (a) and (b) are evaluated independently for each player and each pitch boundary, and condition (c) is paired with the player closest to the ball at the acceleration peak. We discard any (frame, player) pair whose player-ball distance exceeds 3 m or whose ball height exceeds 4 m, retaining only those at which a ball touch is physically feasible. Section 3.4 empirically validates these choices, showing how candidate coverage and final accuracy change as we vary the two thresholds and ablate each detection condition. Finally, we group the remaining pairs by their frame index and represent each candidate as 𝑐 = (𝑡𝑐 , P𝑐 ), where 𝑡𝑐 is the frame and P𝑐 is the set of players and pitch lines associated with 𝑡𝑐 . Without this grouping, the order-preserving NW alignment in Section 2.4 would impose an arbitrary order on these simultaneous candidates, failing to match them with the corresponding co-occurring events whenever the two orderings conflict. See Fig. 2 that instantiates the player-ball distances marked with detected candidate frames.

2.3

Event-Candidate Pairwise Scoring

In this section, we assign a score in the range from 0 to 1 for every pair of event and candidate in each episode, where a higher score indicates that the event aligns better with the candidate. Without using the human-annotated event locations, we calculate a set of features informative for identifying on-the-ball events only from player and ball trajectories. We compute the score as a weighted sum of per-feature scores, where the features and their weights depend on the event category defined in Section 2.1. Calculating the score of every event-candidate pair yields a pairwise score matrix, which serves as the input to the alignment algorithm in Section 2.4. Specifically, we first define several per-feature scoring functions for a given candidate frame 𝑐 = (𝑡𝑐 , P𝑐 ). Each function takes the frame 𝑡𝑐 and optionally a target player (or a pitch line) 𝑝 ∈ P𝑐 as input, and returns a value between 0 and 1 based on a clipped linear mapping given by   0 if 𝑥 ≤ 𝑥 0,    𝑓 (𝑥; 𝑥 0, 𝑥 1 ) = 1 if 𝑥 ≥ 𝑥 1,    𝑥 −𝑥 0 if 𝑥 0 < 𝑥 < 𝑥 1 .  𝑥 1 −𝑥 0 The detailed definition of the scoring functions is as follows:

(2)

CIKM ’26, November 07–11, 2026, Rome, Italy

Hyunsung Kim et al.

𝑠 PBD (𝑡𝑐 , 𝑝) = 1 − 𝑓 (𝑑 (𝑡𝑐 , 𝑝); 0, 3 m).

(4)

Kick distance (KD) score. Since incoming or outgoing events involve the ball traveling a meaningful distance to or from the player, we score candidate 𝑐 by the maximum PBD over an interval before or after 𝑡𝑐 depending on the event category. Specifically, we define the pre-kick distance (Pre-KD) by the maximum PBD max𝑡𝑐− ≤𝑡 ≤𝑡𝑐 𝑑 (𝑡, 𝑝𝑐 ) in the interval between 𝑡𝑐 and the previous candidate 𝑐 − = (𝑡𝑐− , P𝑐− ) where 𝑝𝑐 ∈ P𝑐− , and the post-kick distance (Post-KD) by the maximum PBD max𝑡𝑐 ≤𝑡 ≤𝑡𝑐+ 𝑑 (𝑡, 𝑝𝑐 ) in the interval between 𝑐 and the next candidate 𝑐 + = (𝑡𝑐+, P𝑐+ ) where 𝑝𝑐 ∈ P𝑐+ . To distinguish actual ball receptions from subsequent minor touches, we assign a high score to a candidate with a large Pre-KD paired with an incoming event by:   − 𝑠 KD (𝑡𝑐 , 𝑝) = 𝑓 −max 𝑑 (𝑡, 𝑝); 0, 3 m . (5)

C

P

C

P

away_10 away_5

20 15 10 5 0 10600

10650

10700

10750 Frame ID

10800

10850

Figure 2: Player-ball distances for the two players in a sample interval. Black dashed vertical lines denote candidate frames, and red solid vertical lines indicate those matched to events by the NW alignment, with markers at the top indicating whether each event is a control (C) or a pass (P).

10 6 10 23 6 10 30 6 10 61 7 10 21 7 10 47 7 10 56 7 10 61 7 10 82 8 10 05 8 10 12 81 9

Player-ball distance (PBD) score. Since the acting player must be in contact with the ball at an event, a smaller PBD should yield a higher score. Thus, for the distance 𝑑 (𝑡, 𝑝) between player 𝑝 and the ball at time 𝑡, we define a decreasing scoring function as

25 Player-ball distance (m)

Ball acceleration (BA) score. Since the ball usually changes its direction when an event occurs, a larger BA should yield a higher score. Thus, for BA 𝑎(𝑡𝑐 ) at time 𝑡𝑐 , we define an increasing scoring function as 𝑠 BA (𝑡𝑐 ) = 𝑓 (𝑎(𝑡𝑐 ); 0, 30 m/s2 ). (3)

1.0

A10 control (11) .93 .61 .62 .80 .00 .00 .00 .00 .00 .00 .00 A10 pass (12) .70 .64 .64 .97 .00 .00 .00 .00 .00 .00 .00 A5 control (13) .00 .00 .00 .00 .89 .80 .63 .62 .67 .79 .77 A5 pass (14) .00 .00 .00 .00 .80 .80 .57 .62 .73 1.00 .52

0.8

𝑡𝑐 ≤𝑡 ≤𝑡𝑐

− or 𝑠 + in the total score defined in Eq. 10–12, We include either 𝑠 KD KD depending on the type of the paired event.

Player-ball distance slope (PBDS) score. Since the PBD typically exhibits a valley at the moment of an event, we penalize candidates that deviate from this V-shaped pattern using the pre-slope 𝑣 − (𝑡, 𝑝) and post-slope 𝑣 + (𝑡, 𝑝) of the PBD, defined as: 𝑑 (𝑡, 𝑝) − 𝑑 (𝑡 − ℎ, 𝑝) 𝑑 (𝑡 + ℎ, 𝑝) − 𝑑 (𝑡, 𝑝) , 𝑣 + (𝑡, 𝑝) = 𝑣 − (𝑡, 𝑝) = ℎ ℎ where ℎ = 0.2 s. A positive pre-slope indicates that the ball is already moving away from 𝑝 before 𝑡𝑐 , which is incompatible with an outgoing event. We therefore penalize candidate 𝑐 paired with an outgoing event by: − 𝑠 PBDS (𝑡𝑐 , 𝑝) = 1 − 𝑓 (𝑣 − (𝑡𝑐 , 𝑝); 0, 7 m/s).

A10 control (11) 0.00 A10 pass (12) 0.00 A5 control (13) 0.00 A5 pass (14) 0.00 diag-match

10 12 81 9

8

7 10 56 7 10 61 7 10 82 8 10 05

7 10 21 7 10 47

6

10 23 6 10 30 6 10 61

10 0.00

0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00

7.31 7.31 7.31 7.31 7.31 7.31 7.31 7.31 7.31 7.31 7.31 7.91 7.94 7.95 8.28 8.28 8.28 8.28 8.28 8.28 8.28 8.28 7.91 7.94 7.95 8.28 9.17 9.17 9.17 9.17 9.17 9.17 9.17 7.91 7.94 7.95 8.28 9.87 9.97 9.97 9.97 9.97 10.17 10.17

right-gap

down-gap

down-match

optimal path

(b) DP table 𝐹𝑖,𝑗 with backpointer moves 𝐵𝑖,𝑗

Figure 3: Components of the NW alignment for the four events of the interval shown in Fig. 2. The match moves (diag-match or down-match) along the yellow-highlighted optimal path in (b) correspond to the final event-frame pairs.

(7)

Likewise, a negative post-slope implies that the ball is still approaching 𝑝 after 𝑡𝑐 , which is incompatible with an incoming event. We thus penalize 𝑐 paired with an incoming event by: + 𝑠 PBDS (𝑡𝑐 , 𝑝) = 𝑓 (𝑣 + (𝑡𝑐 , 𝑝); −7 m/s, 0).

0.4

(a) Pairwise scores 𝑠 (𝑒𝑖 , 𝑐 𝑗 )

Symmetrically, to discriminate kicks against minor touches, we assign a high score to a candidate with a larger Post-KD paired with an outgoing event by:   + 𝑠 KD (𝑡𝑐 , 𝑝) = 𝑓 max + 𝑑 (𝑡, 𝑝); 0, 3 m . (6) 𝑡𝑐 ≤𝑡 ≤𝑡𝑐

0.6

(8)

− + We include either 𝑠 PBDS , 𝑠 PBDS , or 𝑠 OD defined below into the total

score as in Eq. 10–12, depending on the type of the paired event. Opponent distance (OD) score. Since two players contest the ball when a tackle or a dispossessed event occurs, the ball should be also close to the nearest opposing player as well as the acting

player. We thus assign a high score to such candidates by defining the scoring function as:   𝑠 OD (𝑡𝑐 , 𝑝) = 1 − 𝑓 min 𝑑 (𝑡𝑐 , 𝑞); 0, 3 m , (9) 𝑞 ∈𝑂 (𝑝 )

where 𝑂 (𝑝) is the set of players in the opposing team against 𝑝. Then, we compute the score 𝑠 (𝑒, 𝑐) between every pair of an event 𝑒 executed by player 𝑝𝑒 and a candidate 𝑐 = (𝑡𝑐 , P𝑐 ) per episode as a weighted sum of feature scores defined above. We require 𝑝𝑒 ∈ P𝑐 as a hard constraint, setting 𝑠 (𝑒, 𝑐) = 0 regardless

ELASTIC: Trajectory-Based Synchronization of Event and Tracking Data in Soccer

of the other features if 𝑝𝑒 ∉ P𝑐 . That is, the total score defined in Eq. 10–12 is evaluated only when 𝑝𝑒 ∈ P𝑐 . We include different component scores depending on the category of 𝑒 (defined in Section 2.1). If 𝑒 is an outgoing event in either an open play or a set piece, the ball should depart from the executing player and travel a meaningful distance after the event, so we + and the pre-slope score 𝑠 − use the post-KD score 𝑠 KD PBDS : 𝑠 (𝑒, 𝑐) = 𝜆BA𝑠 BA (𝑡𝑐 ) + 𝜆PBD𝑠 PBD (𝑡𝑐 , 𝑝𝑒 ) + − + 𝜆KD𝑠 KD (𝑡𝑐 , 𝑝𝑒 ) + 𝜆PBDS𝑠 PBDS (𝑡𝑐 , 𝑝𝑒 ).

(10)

In contrast, if 𝑒 is an incoming event, the ball should approach 𝑝𝑒 from a distant location before the event, so we use the pre-KD and − and 𝑠 + post-slope counterparts 𝑠 KD PBDS : 𝑠 (𝑒, 𝑐) = 𝜆BA𝑠 BA (𝑡𝑐 ) + 𝜆PBD𝑠 PBD (𝑡𝑐 , 𝑝𝑒 ) − + + 𝜆KD𝑠 KD (𝑡𝑐 , 𝑝𝑒 ) + 𝜆PBDS𝑠 PBDS (𝑡𝑐 , 𝑝𝑒 ).

(11)

When a minor event occurs, two players contest the ball at close range, so we use the OD score instead of the PBDS scores. For the − since the ball travels toward the tackling KD term, tackle uses 𝑠 KD + since the player before they touch it, while dispossessed uses 𝑠 KD executing player loses the ball after the event. The score is thus defined as: 𝑠 (𝑒, 𝑐) = 𝜆BA𝑠 BA (𝑡𝑐 ) + 𝜆PBD𝑠 PBD (𝑡𝑐 , 𝑝𝑒 ) + 𝜆KD𝑠 KD (𝑡𝑐 , 𝑝𝑒 ) + 𝜆OD𝑠 OD (𝑡𝑐 , 𝑝𝑒 ),

(12)

− for tackle and 𝑠 + where 𝑠 KD = 𝑠 KD KD = 𝑠 KD for dispossessed. We set all the weights to 𝜆BA = 𝜆PBD = 𝜆KD = 𝜆PBDS = 𝜆OD = 0.25, so

that each 𝑠 (𝑒, 𝑐) falls between 0 and 1. In Section 3.5, we examine the sensitivity of the final accuracy to these hyperparameters by varying each clipping threshold and weight of the per-feature scoring functions, and conduct an ablation study that confirms the necessity of each feature score by removing one term at a time. Fig. 3a illustrates the resulting score matrix for sample events, where each row corresponds to an event and each column corresponds to a candidate frame.

2.4

Repeat-Augmented Needleman-Wunsch Algorithm

Using the pairwise score matrix defined in Section 2.3, we align the event sequence and the candidate frame sequence within each episode while preserving their order. To this end, we adapt the Needleman-Wunsch (NW) algorithm [17], which was originally proposed in bioinformatics to find the globally optimal alignment between two amino-acid or DNA sequences. As the two sequences usually differ in length and cannot be matched one-to-one, NW introduces a gap penalty that controls which elements to leave as gaps on either side instead of forcing them into a match. In our framework, gaps on both sides naturally absorb ambiguous events that have no compatible candidate frame, as well as candidate frames at which no event actually occurs. Vanilla NW. For an episode 𝑘, let 𝐸𝑘 = (𝑒𝑘,1, . . . , 𝑒𝑘,𝑚𝑘 ) and 𝐶𝑘 = (𝑐𝑘,1, . . . , 𝑐𝑘,𝑛𝑘 ) denote the enriched event sequence and the candidate frame sequence, respectively. For notational simplicity, we drop the episode index 𝑘 and write 𝐸𝑘 = (𝑒 1, . . . , 𝑒𝑚 ) and 𝐶𝑘 = (𝑐 1, . . . , 𝑐𝑛 ) throughout this section. The vanilla NW initializes a

CIKM ’26, November 07–11, 2026, Rome, Italy

dynamic programming (DP) table 𝐹 ∈ R (𝑚+1) × (𝑛+1) as 𝐹 0,0 = 0, 𝐹𝑖,0 = 𝑖 · 𝑔𝑒 , and 𝐹 0,𝑗 = 𝑗 · 𝑔𝑐 , where 𝑔𝑒 and 𝑔𝑐 are the gap penalties for leaving an event unmatched and a candidate frame unused, respectively. The remaining entries are then filled recursively by taking the maximum over three possible moves at each cell:   𝐹 + 𝑠 (𝑒𝑖 , 𝑐 𝑗 ),   𝑖 −1,𝑗 −1  𝐹𝑖,𝑗 = max 𝐹𝑖,𝑗 −1 + 𝑔𝑐 ,    𝐹𝑖 −1,𝑗 + 𝑔𝑒 , 

(diag-match) (right-gap: 𝑐 𝑗 unmatched) (13) (down-gap: 𝑒𝑖 unmatched)

where 𝑠 (𝑒𝑖 , 𝑐 𝑗 ) is the pairwise score defined in Section 2.3, while recording the selected move in a backpointer table 𝐵 ∈ {diag-match, right-gap, down-gap} (𝑚+1) × (𝑛+1) . Once 𝐹 is completed, we trace back from the last position (𝑚, 𝑛) to the origin (0, 0) along the opposite directions stored in 𝐵, and the resulting path yields the optimal alignment between 𝐸𝑘 and 𝐶𝑘 . Extension with a down-match move. The threefold recurrence of this vanilla NW enforces a one-to-one correspondence in which each candidate frame can match at most one event. In soccer, however, two consecutive events frequently correspond to the same moment. For example, a loss of possession by one player and the gain of possession by an opposing player are separately recorded as dispossessed and tackle, but actually describe a single ball contest. Another typical example is a one-touch action such as a control followed by a pass or shot, in which the player makes a pass or a shot at their first contact with the ball. To accommodate such cases, we extend the NW recurrence in Eq. 13 with a downmatch option, which goes downward like a down-gap but matches the current event again to the previously matched candidate frame instead of leaving it as a gap:

𝐹𝑖,𝑗 = max

 𝐹𝑖 −1,𝑗 −1 + 𝑠 (𝑒𝑖 , 𝑐 𝑗 ),     𝐹  +𝑔 , 𝑖,𝑗 −1

𝑐

 𝐹𝑖 −1,𝑗 + 𝑔𝑒 ,    𝐹  𝑖 −1,𝑗 + 𝑠 (𝑒𝑖 , 𝑐 𝑗 ) + 𝑟,

(diag-match) (right-gap) (down-gap) (down-match)

(14)

where 𝑟 ≤ 0 is a constant repeat penalty. A down-match move duplicates the match of 𝑐 𝑗 , assigning it to both 𝑒𝑖 −1 and 𝑒𝑖 at the cost of 𝑟 , which indicates that the two events happen at the same moment. Like the vanilla NW algorithm, we record in the backpointer table 𝐵 ∈ {diag-match, right-gap, down-gap, down-match} (𝑚+1) × (𝑛+1) indicating which of the four moves attained the maximum. Penalty design. The gap and repeat penalties are designed based on domain-specific intuitions. First, we set the candidate frame gap penalty to 𝑔𝑐 = 0 so that the alignment is driven solely by the pairwise scores. This is because the number of candidate frames 𝑛 is generally larger than the number of events 𝑚, and at least 𝑛 − 𝑚 frames must remain unmatched in any alignment. By setting 𝑔𝑐 = 0, the algorithm determines which candidates to leave out only based on the pairwise score 𝑠 (·). Likewise, we set the event gap penalty to 𝑔𝑒 = 0 to allow an event to remain unmatched when no compatible candidate exists, deferring the rejection of low-confidence matches to the postprocessing threshold in Section 2.5. Lastly, we set the repeat penalty to 𝑟 = −0.1, so that two consecutive events are assigned to the same frame only when their scores are high enough

CIKM ’26, November 07–11, 2026, Rome, Italy

to outweigh the penalty. Section 3.5 shows that the alignment is insensitive to 𝑔𝑒 and validates the choices of 𝑔𝑐 and 𝑟 . Traceback. Once 𝐹 is fully populated, we obtain the optimal alignment by tracing back along 𝐵 from (𝑚, 𝑛) to (0, 0). Each move recorded in 𝐵𝑖,𝑗 shifts the indices in a different way: a diag-match shifts (𝑖, 𝑗) to (𝑖 − 1, 𝑗 − 1) while matching 𝑒𝑖 to 𝑐 𝑗 ; a right-gap shifts to (𝑖, 𝑗 − 1) while leaving 𝑐 𝑗 unmatched; and a down-gap shifts to (𝑖 − 1, 𝑗) while leaving 𝑒𝑖 unmatched. A down-match shifts in the same direction as a down-gap but matches 𝑒𝑖 to 𝑐 𝑗 rather than leaving 𝑒𝑖 as a gap. When the trace reaches (0, 0), every entry of the enriched event sequence is assigned either to a candidate frame or to a gap. Fig. 3b shows the resulting DP table and the optimal alignment for the sample events used in Fig. 3a.

2.5

Postprocessing

After obtaining the optimal alignment between the enriched event sequence and the candidate frame sequence, we apply three postprocessing steps to derive the final output. First, when an adjacent dispossessed-tackle pair is matched to different candidate frames, we unify them by snapping both events to the frame with the higher pairwise score, since the two events describe a single ball contest. Second, we reject any match whose pairwise score falls below 0.5 by marking it as unsynchronized, leaving low-confidence matches empty rather than contaminating downstream analyses. Finally, we fold the alignment over the enriched event sequence back into the original events, where each original event 𝑒𝑖 takes its start timestamp from its matched frame, and its end timestamp from the candidate frame matched to the virtual termination event inserted immediately after 𝑒𝑖 in Section 2.1.

3

Main Experiments

For rigorous evaluation, we first re-annotated the event timestamps in a public dataset to construct a reliable ground-truth benchmark, and validated its quality via a cross-annotator comparison (Section 3.1). We then compared the synchronization accuracy of ELASTIC on this benchmark (Section 3.3) against several baseline methods described in Section 3.2. To further examine our methodological design, we measured the coverage of the extracted candidate frames over the true event timestamps (Section 3.4), conducted a sensitivity study on the hyperparameters (Section 3.5), and analyzed the runtime of the methods (Section 3.6).

3.1

Ground-Truth Benchmark Construction

To construct a reproducible benchmark, we re-annotated the event timestamps in the Sportec Open DFL Dataset [3], a publicly available collection of event and tracking data from seven matches of the German Bundesliga’s first and second divisions. For effective annotation, we developed a JavaScript-based annotation tool that replays the match animation alongside the event records, allowing an annotator to inspect each event and correct its timestamp1 . Using this tool, three authors with expertise in soccer analytics independently re-labeled the event timestamps from three of the matches at 25 FPS (0.04 s resolution) to align with the tracking 1 The tool with the annotation results is available at https://elastic-annotator.com. The

annotator can jump the video to its recorded moment by clicking an event, and can reassign the event’s timestamp to the currently displayed frame with a single click.

Hyunsung Kim et al.

Table 1: Agreement statistics of event time labels across three annotators. “MD” denotes the mean pairwise absolute difference in frames between the labeled timestamps for each event. “Exact3” and “Exact2” indicate the number of events where at least three or two annotators, respectively, provided exactly the same timestamp. “Close3” and “Close2” indicate the number of events where at least three or two labels, respectively, fall within a two-frame (0.08 s) window. Category

Total MD

Exact3

Exact2

Close3

Close2

Outgoing-OP 2,690 0.279 2,615 (97.2%) 2,684 (99.8%) 2,647 (98.4%) 2,688 (99.9%) Outgoing-SP 282 0.021 279 (98.9%) 282 (100.0%) 280 (99.3%) 282 (100.0%) Incoming 295 1.530 266 (90.2%) 288 (97.6%) 274 (92.9%) 290 (98.3%) Minor 231 3.873 189 (81.8%) 223 (96.5%) 190 (82.3%) 227 (98.3%) Event start Event end

3,498 0.601 3,349 (95.7%) 3,477 (99.4%) 3,391 (96.9%) 3,487 (99.7%) 2,972 0.426 2,799 (94.2%) 2,911 (97.9%) 2,859 (96.2%) 2,938 (98.9%)

Total

6,470 0.521 6,148 (95.0%) 6,388 (98.7%) 6,250 (96.6%) 6,425 (99.3%)

data. Since the original dataset does not record event terminations, we further inserted control, out, and goal events with their true timestamps wherever they were missing. Table 1 reports the agreement statistics across the three annotators. All annotators assigned exactly the same timestamp for 95.0% of events, with a mean pairwise difference (MD) of 0.521 frames (0.0208 s). This high consistency stems from the meticulous re-annotation process, where each annotator paused the animation at every event to pinpoint its exact frame. Moreover, for 99.3% of events, at least two annotations fall within two frames (0.08 s) of each other. Assuming that such close agreement reflects reliability, this result implies that the median of the three timestamps provides a reliable estimate for 99.3% of events. Based on this observation, we adopt the median of the annotated timestamps for each event as the ground truth in the subsequent experiments.

3.2

Baselines and Evaluation Metrics

We compare ELASTIC against three baselines. ETSY [29] is a rulebased synchronizer that processes events in chronological order, assigning each event the frame that minimizes the sum of pairwise distances among the acting player, the ball, and the annotated event location. Biermann et al. [4] proposed a learning-based synchronizer, which slides a window over the tracking data and classifies whether each window’s center frame corresponds to an event based on aggregated window features. Since their method requires training data with ground-truth event timestamps, we evaluate it via leave-one-match-out cross-validation, training on two of the three benchmark matches and testing on the remaining match. As it detects only pass-like (outgoing) events, we leave incoming and minor events unsynchronized. DataBallPy [18, 19] finds a globally optimal alignment using the NW algorithm as our framework, but aligns events to all in-play frames without candidate frame selection. It synchronizes only pass, shot, and tackle events, so we map each outgoing event to a shot if its type is shot, shot_freekick, or shot_penalty (among all types listed in Section 2.1), and to a pass otherwise. Since DataBallPy does not handle ball receptions, it cannot synchronize incoming events. Among minor events, it covers only tackle, leaving dispossessed unsynchronized.

ELASTIC: Trajectory-Based Synchronization of Event and Tracking Data in Soccer

CIKM ’26, November 07–11, 2026, Rome, Italy

Table 2: Synchronization accuracy of three baselines and two ELASTIC variants across event categories. Category

Method

Total

MD

W2

W5

W25

W50

Valid

Open-play ETSY outgoing Biermann et al. DataBallPy ELASTIC-Greedy ELASTIC-NW

2,690 10.076 15.268 4.381 7.251 1.050

1,510 (56.1%) 1,853 (68.9%) 2,219 (82.5%) 2,365 (87.9%) 2,484 (92.3%) 2,103 (78.2%) 2,184 (81.2%) 2,278 (84.7%) 2,397 (89.1%) 2,690 (100.0%) 2,313 (86.0%) 2,533 (94.2%) 2,593 (96.4%) 2,641 (98.2%) 2,687 (99.9%) 2,315 (86.1%) 2,322 (86.3%) 2,349 (87.3%) 2,380 (88.5%) 2,525 (93.9%) 2,631 (97.8%) 2,642 (98.2%) 2,652 (98.6%) 2,666 (99.1%) 2,686 (99.9%)

Set-piece outgoing

ETSY Biermann et al. DataBallPy ELASTIC-Greedy ELASTIC-NW

282 28.560 3.915 3.280 3.594 0.060

183 (64.9%) 244 (86.5%) 264 (93.6%) 268 (95.0%) 276 (97.9%)

196 (69.5%) 259 (91.8%) 272 (96.5%) 272 (96.5%) 277 (98.2%)

198 (70.2%) 271 (96.1%) 273 (96.8%) 272 (96.5%) 277 (98.2%)

201 (71.3%) 274 (97.2%) 276 (97.9%) 273 (96.8%) 277 (98.2%)

230 (81.6%) 282 (100.0%) 282 (100.0%) 280 (99.3%) 277 (98.2%)

Incoming

ETSY Biermann et al. DataBallPy ELASTIC-Greedy ELASTIC-NW

295 23.287 — — 22.312 5.799

135 (45.8%) 0 (0.0%) 0 (0.0%) 214 (72.5%) 266 (90.2%)

165 (55.9%) 0 (0.0%) 0 (0.0%) 216 (73.2%) 268 (90.8%)

200 (67.8%) 0 (0.0%) 0 (0.0%) 222 (75.3%) 273 (92.5%)

221 (74.9%) 0 (0.0%) 0 (0.0%) 236 (80.0%) 283 (95.9%)

258 (87.5%) 0 (0.0%) 0 (0.0%) 270 (91.5%) 294 (99.7%)

Minor

ETSY Biermann et al. DataBallPy ELASTIC-Greedy ELASTIC-NW

231 18.370 — 15.284 13.322 2.883

76 (32.9%) 0 (0.0%) 39 (16.9%) 144 (62.3%) 203 (87.9%)

102 (44.2%) 0 (0.0%) 59 (25.5%) 154 (66.7%) 210 (90.9%)

165 (71.4%) 0 (0.0%) 95 (41.1%) 180 (77.9%) 222 (96.1%)

192 (83.1%) 0 (0.0%) 112 (48.5%) 194 (84.0%) 226 (97.8%)

215 (93.1%) 0 (0.0%) 120 (51.9%) 214 (92.6%) 231 (100.0%)

Event start ETSY Biermann et al. DataBallPy ELASTIC-Greedy ELASTIC-NW

3,498 13.030 14.201 4.703 8.572 1.495

1,904 (54.4%) 2,316 (66.2%) 2,782 (79.5%) 2,979 (85.2%) 2,347 (67.1%) 2,443 (69.8%) 2,549 (72.9%) 2,671 (76.4%) 2,616 (74.8%) 2,864 (81.9%) 2,961 (84.6%) 3,029 (86.6%) 2,941 (84.1%) 2,964 (84.7%) 3,023 (86.4%) 3,083 (88.1%) 3,376 (96.5%) 3,397 (97.1%) 3,424 (97.9%) 3,452 (98.7%)

3,187 (91.1%) 2,972 (85.0%) 3,089 (88.3%) 3,289 (94.0%) 3,488 (99.7%)

Event end

ELASTIC-Greedy ELASTIC-NW

2,972 13.092 1.937

2,313 (77.8%) 2,334 (78.5%) 2,381 (80.1%) 2,449 (82.4%) 2,782 (93.6%) 2,803 (94.3%) 2,853 (96.0%) 2,890 (97.2%)

2,622 (88.2%) 2,935 (98.8%)

Total

ELASTIC-Greedy ELASTIC-NW

6,470 10.577 1.697

5,254 (81.2%) 5,298 (81.9%) 5,404 (83.5%) 5,532 (85.5%) 6,158 (95.2%) 6,200 (95.8%) 6,277 (97.0%) 6,342 (98.0%)

5,911 (91.4%) 6,423 (99.3%)

In addition to the three baselines, we evaluate two variants of our framework: ELASTIC-NW, the full model using the NW alignment, and ELASTIC-Greedy, an ablated variant that shares the candidate frame selection (Section 2.2) and the pairwise scoring (Section 2.3) with ELASTIC-NW but replaces the NW alignment (Section 2.4) with greedy matching. Specifically, when an episode begins with a set piece, ELASTIC-Greedy first locates the restarting kick by selecting the first candidate frame that is paired with the kicker and whose post-slope exceeds 7 m/s. It then processes the remaining events in chronological order, assigning each event the highestscoring candidate between the frame assigned to the previous event and 5 s after the annotated timestamp of the current event. Once all original events are synchronized, each virtual termination event (i.e., goal, out, or control) is detected between the frames assigned to its two neighboring original events, and low-confidence matches are rejected by the same score threshold as in Section 2.5. We report the mean absolute difference (MD) in frames between the predicted and ground-truth timestamps, the number of events whose predicted frame falls within 2, 5, 25, and 50 frames of the ground truth (W2, W5, W25, W50), and the number of events to which the synchronizer successfully assigns a frame (Valid). Among these, we adopt W2 (a two-frame, 0.08 s tolerance) as our primary metric rather than exact alignment, so as not to penalize one- or two-frame discrepancies unrelated to actual synchronization accuracy. Such tiny differences typically arise from differing definitions of event moments across providers or annotators, or from local extrema shifted by one or two frames after the tracking data is smoothed. If only exact alignment were counted as correct, these

artifacts would be conflated with genuine synchronization errors. We therefore treat a prediction within two frames of the ground truth as accurate, which remains reliable since the annotators’ labels agree within two frames for 99.3% of events (Section 3.1).

3.3

Synchronization Accuracy

As shown in Table 2, ELASTIC-NW substantially outperforms the baselines across all event categories. For event starts (i.e., moments of the original events), it achieves 96.5% W2 accuracy, compared to 54.4% (ETSY), 67.1% (Biermann et al.), and 74.8% (DataBallPy). While this gap partly reflects that Biermann et al. and DataBallPy cover only a subset of event types, ELASTIC-NW remains the most accurate even on outgoing events in both open play (97.8% vs. 86.0% of DataBallPy) and set pieces (97.9% vs. 93.6% of DataBallPy), which all baselines are designed to cover. Moreover, it also detects event ends with 93.6% W2 accuracy, which are unrecorded ball receptions that prior methods leave unsynchronized. As a result, ELASTIC-NW synchronizes 95.2% of all events within two frames of the ground truth, with a mean difference of only 1.697 frames (0.068 s). The comparison between the two ELASTIC variants highlights the benefit of global alignment. Although ELASTIC-Greedy uses the same candidate frames, its sequential matching propagates early errors to later events, yielding markedly lower accuracy on event starts (84.1% vs. 96.5%). The gap is most pronounced for minor events (62.3% vs. 87.9%), whose behavior patterns are more ambiguous than those of other categories. The order-preserving NW alignment resolves such ambiguities jointly, preventing the local mistakes that accumulate under greedy matching. Overall,

CIKM ’26, November 07–11, 2026, Rome, Italy

Hyunsung Kim et al.

the precise and robust synchronization achieved by ELASTIC-NW makes it a reliable foundation for downstream tasks where accurate event timing is essential.

3.4

Candidate Frame Coverage

Since ELASTIC aligns events only to the extracted candidate frames, the candidate selection stage caps the achievable accuracy: if no candidate lies near the true frame of an event, no subsequent alignment can synchronize it correctly. To quantify this cap, we define the W2 coverage of a candidate set as the fraction of ground-truth event timestamps for which a candidate frame associated with the acting player exists within two frames. The W2 coverage equals the W2 accuracy of an oracle that always selects the correct candidate, and thus upper-bounds ELASTIC-NW and any other synchronizer operating on the same candidates. Table 3: W2 coverage of the extracted candidates over the true event frames and W2 accuracy of ELASTIC-NW under different detection conditions and thresholds, along with the number of candidates and the per-match runtime (mean ± std). ★ marks the default configuration, and cells are shaded by the size of the drop from the default setting: yellow for at least 1 pp, light red for 5 pp, or dark red for 15 pp. Event coverage Config.

#Cand.

Start

End

Total

Acc.

Time (s)

76.9% 90.7% 98.5%

77.5% 86.0% 98.2%

77.2% 88.5% 98.4%

75.4% 85.4% 95.2%

20.09 ± 1.38 35.30 ± 4.54 37.62 ± 5.25

Detection conditions (a)+(b) only (c) only (a)+(b)+(c)★

10,926 14,363 16,979

10,352 13,716 16,979 20,516 24,116 220,812

3.5

Feature weights. We first vary each feature weight in Eq. 10–12 to 0 (disabled) or 0.5 (emphasized) while keeping the others at the default of 0.25. Note that 𝜆BA , 𝜆PBD , and 𝜆KD apply to all event categories, whereas 𝜆PBDS and 𝜆OD apply only to major (outgoing and incoming) and minor events, respectively. Table 4: Sensitivity of the W2 accuracy to the feature weights for each event category, where each weight is varied to 0 (disabled) or 0.5 (emphasized) while the others remain at the default (★) of 0.25. Cells are shaded by the drop from the default as in Table 3.

93.1% 98.4% 98.5% 98.6% 98.6% 98.7%

95.1% 98.2% 98.2% 98.2% 98.2% 98.2%

94.0% 98.3% 98.4% 98.4% 98.4% 98.5%

89.4% 94.9% 95.2% 95.1% 95.2% 95.1%

33.85 ± 4.42 34.60 ± 5.29 37.62 ± 5.25 36.50 ± 5.23 37.46 ± 5.18 115.82 ± 24.40

14,306 15,685 16,639 16,979 17,202 17,726

83.9% 93.3% 98.5% 98.5% 98.5% 98.5%

84.5% 93.8% 98.2% 98.2% 98.2% 98.3%

84.2% 93.5% 98.4% 98.4% 98.4% 98.4%

77.2% 88.5% 95.1% 95.2% 95.2% 95.2%

32.80 ± 4.44 32.30 ± 5.55 33.90 ± 4.04 37.62 ± 5.25 32.61 ± 4.84 32.77 ± 4.44

Table 3 reports the W2 coverage and the W2 synchronization accuracy of ELASTIC-NW under different candidate selection settings. With the default configuration, the extracted candidates cover 98.4% of the ground-truth event timestamps, implying that nearly every event has a correct candidate to align with. The first block of the table shows that the detection conditions (a)–(c) defined in Section 2.2 are complementary: using only the distance conditions (a) and (b) or only the acceleration condition (c) drops the coverage to 77.2% and 88.5%, respectively. The former misses touches at which the player-ball distance forms no local minimum, while the latter misses soft touches without a sudden change in ball motion. The remaining blocks vary the two feasibility thresholds. Tight thresholds miss legitimate touches: a 1 m distance limit discards

Open-play Set-piece Incoming Minor outgoing outgoing

Event start

Event end

Default★ 0.25

97.8%

97.9%

90.2%

87.9%

96.5%

93.6%

𝜆BA

0.00 0.50

97.5% 97.7%

97.5% 97.9%

88.5% 86.8%

70.1% 86.1%

94.9% 96.0%

92.6% 90.6%

𝜆PBD

0.00 0.50

97.7% 97.2%

97.5% 97.9%

86.8% 87.5%

67.5% 84.0%

94.8% 95.6%

92.3% 92.9%

𝜆KD

0.00 0.50

91.7% 98.0%

94.7% 88.3%

76.6% 87.8%

71.4% 83.5%

89.4% 95.4%

79.6% 94.1%

𝜆PBDS

0.00 0.50

96.7% 97.1%

38.7% 95.7%

88.1% 89.5%

87.4% 87.9%

90.7% 95.7%

92.9% 91.9%

𝜆OD

0.00 0.50

97.8% 97.8%

97.9% 97.9%

89.5% 90.5%

74.9% 79.7%

95.6% 96.0%

93.5% 93.6%

Ball height threshold

1m 2m 3m 4 m★ 5m ∞

Hyperparameter Sensitivity

ELASTIC involves three groups of hyperparameters: the feature weights in Eq. 10–12, the clipping bounds of the per-feature scoring functions in Eq. 3–9, and the alignment penalties in Eq. 14. To justify our choice of the hyperparameters, we vary each of them while fixing the others to their defaults and measure the resulting W2 accuracy, as summarized in Tables 4 and 5.

Weight Value

Player-ball distance threshold

1m 2m 3 m★ 4m 5m ∞

true touches whose measured player-ball distance is inflated by trajectory noise, and a height limit below 3 m loses aerial touches, both collapsing the coverage to below 95%. Once both thresholds reach 3 m, the coverage and accuracy saturate, while removing the limits substantially increases the number of extracted candidates and thus the computation time. We therefore set the distance threshold to 3 m and the height threshold to 4 m, where the extraction stays efficient without performance drops and the retained candidates remain physically plausible for an actual ball touch.

As shown in Table 4, disabling any feature (𝜆 = 0) degrades accuracy in its corresponding categories, confirming that every feature contributes to the synchronization. Among them, 𝜆KD has the broadest impact: removing it lowers the accuracy across all categories, as the kick distance is the key signal for distinguishing kicks, receptions, and minor touches. Meanwhile, disabling 𝜆PBDS shows less effect on the other categories but collapses the set-piece accuracy to 38.7%. This is because a set piece usually launches the ball from rest at the start of an episode, where the framework detects spurious candidates around the true frame. These candidates appear nearly identical to the true one in all features except the pre-slope, so the alignment often picks a wrong candidate without the PBDS score, missing the W2 tolerance.

ELASTIC: Trajectory-Based Synchronization of Event and Tracking Data in Soccer

Emphasizing a single feature (𝜆 = 0.5) is also harmful, degrading the accuracy by overshadowing the other features. In particular, minor events are the most sensitive to these weight changes, as their inherently ambiguous motion patterns make the synchronization rely on the balance of all features. Across all categories, the default equal-weight setting yields the most consistent accuracy, justifying its use without further tuning. Scoring function bounds. Next, we sweep the clipping bound of each scoring function in Eq. 3–9 around its default value. As shown in the upper block of Table 5, the default value is the best or tied with the best for every bound, and the accuracy mostly varies within one percentage point across the swept ranges. The exceptions occur when a bound becomes too tight: clipping a feature at a small value saturates its score for most candidates, making large feature values indistinguishable from one another. Loosening the bounds instead mildly dilutes the resolution of the scores. Alignment penalties. Finally, we vary the candidate gap penalty 𝑔𝑐 , the event gap penalty 𝑔𝑒 , and the repeat penalty 𝑟 in Eq. 14. As reported in the lower block of Table 5, the accuracy is entirely insensitive to the event gap penalty, supporting our choice of 𝑔𝑒 = 0. In contrast, the candidate gap penalty degrades the accuracy in both directions, as a negative 𝑔𝑐 forces spurious matches by penalizing unmatched candidates, while a positive one rewards leaving true candidates unused. The repeat penalty behaves likewise: 𝑟 = 0 overmerges consecutive events into a single frame, whereas 𝑟 ≤ −0.3 blocks legitimate merges such as one-touch actions. Overall, the accuracy forms a wide plateau around the defaults, justifying our choice of hyperparameters.

in under a minute, and our ELASTIC-NW takes under 40 seconds per match on average. The method of Biermann et al. is the fastest (1.4 seconds on average), as its inference reduces to a single pass of a lightweight classifier over the sliding windows once trained. DataBallPy also synchronizes a match only within 4.0 seconds on average, since it skips candidate frame selection and directly performs the NW alignment. However, this speed comes at the cost of coverage and accuracy, as the two baselines synchronize only a subset of event types. In contrast, our framework additionally detects ball receptions and prunes physically implausible frames through candidate frame selection, achieving substantially higher accuracy across all event categories (Table 2). Moreover, since a 90-minute match is processed within a minute either way, such differences in runtime are practically irrelevant for post-match analysis. Table 6: Per-match runtime (in seconds) of each synchronizer on the three Sportec matches in the benchmark, along with the mean and standard deviation. Method ETSY Biermann et al. DataBallPy ELASTIC-Greedy ELASTIC-NW

4

Match 1

Match 2

Match 3

Mean ± Std

33.88 1.59 4.66 37.12 43.67

22.07 1.18 3.43 30.06 34.94

28.72 1.40 3.92 29.70 34.27

28.22 ± 5.92 1.39 ± 0.20 4.00 ± 0.62 32.29 ± 4.19 37.62 ± 5.25

Downstream Task Evaluation

BA bound (m/s2 )

10 94.7%

20 94.8%

30★ 95.2%

40 94.9%

50 94.7%

Beyond direct synchronization accuracy, we examine how it affects downstream analytics tasks that leverage the synchronized event and tracking data. Many soccer analytics models take the spatial configuration of players at each event (e.g., [1, 2, 9, 10, 12, 23, 26, 32]) as input, so an inaccurate event timestamp places the players at the wrong positions and feeds a distorted snapshot to the model. We therefore expect that more accurate synchronization leads to more reliable training and evaluation of such models. To demonstrate this, we measure the performance of two representative prediction tasks based on Graph Neural Networks (GNNs) when their input snapshots are synchronized by different methods.

PBD/OD bound (m)

1 92.4%

3★ 95.2%

5 95.1%

7 95.0%

9 94.7%

4.1

KD bound (m)

1 89.1%

3★ 95.2%

5 95.2%

7 95.0%

9 94.7%

PBDS bound (m/s)

1 91.7%

3 93.8%

5 94.7%

7★ 95.2%

9 95.2%

Candidate gap 𝑔𝑐

−0.3 93.9%

−0.1 94.7%

0★ 95.2%

+0.1 94.0%

+0.3 94.0%

Event gap 𝑔𝑒

−0.3 95.2%

−0.1 95.2%

0★ 95.2%

+0.1 95.2%

+0.3 95.2%

Repeat penalty 𝑟

0 94.0%

−0.1★ 95.2%

−0.2 94.7%

−0.3 94.4%

−0.4 93.9%

Table 5: Sensitivity of the total W2 accuracy to the clipping bounds of the per-feature scoring functions and to the alignment penalties, where each parameter is varied while the others remain at their defaults (★). Cells are shaded by the drop from the default as in Table 3. Scoring function bounds

Alignment penalties

3.6

CIKM ’26, November 07–11, 2026, Rome, Italy

Runtime Analysis

In this section, we measure the runtime of each synchronizer to verify that it does not introduce latency in practical analytics workflows. As reported in Table 6, all methods synchronize every match

Tasks and Setup

We consider the following two tasks that take the player and ball configuration at each event as a graph input and predict an attacking outcome. For both tasks, we follow the GNN architecture of Kim et al. [12], representing each game state as a fully connected graph of players and two goals and producing node embeddings with Graph Attention Network (GAT) [30] layers. • Next action prediction estimates which action the ball possessor will attempt next, namely a pass to one of the teammates, a dribble (treated as a pass to oneself), or a shot toward the opponent’s goal. We model it as a node selection task over the possessor’s teammates and the target goal, applying a softmax over their node embeddings to produce a probability distribution that sums to one. Since this task is a multi-class classification problem, we use accuracy, crossentropy (CE), and mean reciprocal rank (MRR) of the true node as performance metrics in Table 7.

CIKM ’26, November 07–11, 2026, Rome, Italy

Hyunsung Kim et al.

Table 7: Downstream task performance under different synchronization methods. Arrows indicate whether a higher (↑) or lower (↓) value is better. Next action prediction

Pass success prediction

Method

Acc. ↑

CE ↓

MRR ↑

F1 ↑

AUC ↑

Brier ↓

Unsynced ELASTIC-Greedy ELASTIC-NW

0.5796 0.6759 0.6863

1.2148 0.9114 0.8773

0.7354 0.8017 0.8087

0.9031 0.9072 0.9155

0.9028 0.9103 0.9172

0.1013 0.0966 0.0899

0.312 1

10

65

0.5

5 7 93 2 0.243 48

0.052 15130.222 215

03 13 12 8

0.4 0.3 11

0.1

1

(a) Next action probabilities

0.307 5 0.548 1 0.994 10

0.763 6

7 0.259 93

5

0.914 15130.722 215 0.476 0 0.616

2

0.322 48

0.2

11

3 13 12

1 0.344 8

(b) Pass success probabilities

0.0 1.0 0.9 0.8 0.7 0.6 0.5 0.4 0.3

Figure 4: Per-player outputs of the two downstream models for a sample pass, trained on data synchronized by ELASTICNW. Each value, shown both as text and by the circle’s color, indicates (a) the probability that the ball possessor selects each teammate as the target and (b) the probability that a pass to the teammate would succeed. • Pass success prediction estimates whether a pass to each teammate would succeed if attempted, applying a sigmoid to each node embedding to produce an independent success probability. Since this task is a binary classification task (whether the pass would succeed or fail), we use F1 score, AUC, and Brier score as performance metrics in Table 7. Fig. 4 illustrates the per-player outputs of the two models for a pass. Both tasks play a central role in understanding game situations [2, 10, 25] and evaluating players’ performance [8, 12, 23, 27]. Since the Sportec Open DFL Dataset contains only seven matches, we use a larger proprietary tracking dataset from the Dutch Eredivisie to train and evaluate the models, with 200 matches from the

2023–24 season for training, 50 matches from the same season for validation, and 157 matches from the 2024–25 season for testing. We train and evaluate each task independently on three versions of the data: the unsynchronized event data, and the data synchronized by ELASTIC-Greedy and ELASTIC-NW, respectively.

4.2

Results

As shown in Table 7, data synchronization consistently improves downstream performance. Compared to the unsynchronized data, even ELASTIC-Greedy raises accuracy on both tasks (especially the next-action prediction accuracy from 0.5796 to 0.6759), confirming that accurate synchronization is an essential preprocessing step for soccer analytics. Moreover, ELASTIC-NW further outperforms ELASTIC-Greedy across all metrics, demonstrating that the gains from its global alignment translate into measurable downstream benefits. This indirect comparison on a much larger set of matches thus corroborates the direct evaluation results reported in Section 3, confirming the benefit of ELASTIC-NW to practical analytics.

5

Conclusion

This paper revisits event-tracking synchronization in soccer from two angles that prior work has left open: removing the dependence on noisy human-annotated event locations, and recovering the ball receptions that mark when each event ends. ELASTIC addresses both by reasoning purely over player and ball trajectories, and our re-annotated public benchmark shows that this design not only achieves the most accurate synchronization to date but also uniquely recovers event endings. Crucially, our downstream evaluation reframes synchronization as more than a preprocessing detail: the quality of alignment directly shapes the reliability of the analytics built on top of it. We hope that both our method and the released benchmark lower the barrier to sports data analytics.

Acknowledgments This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (RS2024-00335098, RS-2024-00406985), and by the National Research Foundation of Korea (NRF) funded by Ministry of Science and ICT (RS-2022-NR068758).

GenAI Usage Disclosure We used generative AI tools in a limited and supportive manner during the preparation of this manuscript. Specifically, we used Claude to improve the clarity and readability of the writing through phrasing and grammar refinement. In addition, we used Claude Code to support data preprocessing, visualization, and debugging. All core research contributions, including the main ideas, methodology design, experiments, and analytical insights, were developed and validated entirely by the authors.

References [1] Gabriel Anzer and Pascal Bauer. 2021. A goal scoring probability model for shots based on synchronized positional and event data in football (soccer). Frontiers in Sports and Active Living 3 (2021). [2] Gabriel Anzer and Pascal Bauer. 2022. Expected passes: Determining the difficulty of a pass in football (soccer) using spatio-temporal data. Data Mining and Knowledge Discovery 36, 1 (2022), 295–317.

ELASTIC: Trajectory-Based Synchronization of Event and Tracking Data in Soccer

[3] Manuel Bassek, Robert Rein, Hendrik Weber, and Daniel Memmert. 2025. An integrated dataset of spatiotemporal and event data in elite soccer. Scientific Data 12, 195 (2025). [4] Henrik Biermann, Rumena Komitova, Dominik Raabe, Erik Müller-Budack, Ralph Ewerth, and Daniel Memmert. 2023. Synchronization of passes in event and spatiotemporal soccer data. Scientific Reports 13 (2023). [5] Jonas Bischofberger, Arnold Baca, and Erich Schikuta. 2024. Event detection in football: Improving the reliability of match analysis. PLOS ONE 19, 4 (2024). [6] Jesse Davis and Pieter Robberechts. 2024. Biases in expected goals models confound finishing ability. In MIT Sloan Sports Analytics Conference. [7] Tom Decroos, Lotte Bransen, Jan Van Haaren, and Jesse Davis. 2019. Actions speak louder than goals: Valuing player actions in soccer. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. [8] Gregory Everett, Ryan Beal, Tim Matthews, Timothy J. Norman, and Sarvapali D. Ramchurn. 2025. Evaluating defensive influence in multi-agent systems using graph attention networks. In Proceedings of the 12th IEEE International Conference on Data Science and Advanced Analytics. [9] Javier Fernández and Luke Bornn. 2020. SoccerMap: A deep learning architecture for visually-interpretable analysis in soccer. In European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases. [10] Javier Fernández, Luke Bornn, and Daniel Cervone. 2021. A framework for the fine-grained evaluation of the instantaneous expected value of soccer possessions. Machine Learning 110, 6 (2021), 1389–1427. [11] Hyunsung Kim, Han-Jun Choi, Chang Jo Kim, Jinsung Yoon, and Sang-Ki Ko. 2023. Ball trajectory inference from multi-agent sports contexts using set transformer and hierarchical bi-LSTM. In Proceedings of the 29th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. [12] Hyunsung Kim, Sangwoo Seo, Hoyoung Choi, Tom Boomstra, Jinsung Yoon, and Chanyoung Park. 2026. Better prevent than tackle: Valuing defense in soccer based on graph neural networks. In MIT Sloan Sports Analytics Conference. [13] Daniel Link and Martin Hoernig. 2017. Individual ball possession in soccer. PLOS ONE 12, 7 (2017). [14] Patrick Lucey, Alina Bialkowski, Mathew Monfort, Peter Carr, and Iain Matthews. 2015. “Quality vs quantity”: Improved shot prediction in soccer using strategic features from spatiotemporal data. In MIT Sloan Sports Analytics Conference. [15] James Mead, Anthony O’Hare, and Paul McMenemy. 2023. Expected goals in football: Improving model performance and demonstrating value. PLOS ONE 18, 4 (2023), e0282295. [16] Katie Mills, Henry Wang, Zachary Crang, Johsan Billingham, Grant Duthie, Richard Johnson, and Sam Robertson. 2026. Automatic event detection in association football using broadcast-derived tracking data. Sports Engineering 29 (2026). [17] Saul Needleman and Christian Wunsch. 1970. A general method applicable to the search for similarities in the amino acid sequence of two proteins. Journal of Molecular Biology 48, 3 (1970), 443–453. [18] Alexander Oonk, Daan Grob, and Matthias Kempe. 2026. DataBallPy: Load, synchronize, and analyse your soccer data. Journal of Open Source Software 11, 120 (2026), 10223. [19] Alexander Oonk, Matthias Kempe, and Daan Grob. 2025. The right way to synchronize tracking and event data: Using domain knowledge to optimize algorithms. In MathSports Conference. [20] Paul Power, Héctor Ruiz, Xinyu Wei, and Patrick Lucey. 2017. Not all passes are created equal: Objectively measuring the risk and reward of passes in soccer from tracking data. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. [21] Pegah Rahimian, Dayana Grayce da Silva Guerra Gomes, Fanni Berkovics, and László Toka. 2022. Let’s penetrate the defense: A machine learning model for prediction and valuation of penetrative passes. In ECML PKDD Workshop on Machine Learning and Data Mining for Sports Analytics. [22] Pegah Rahimian, Hyunsung Kim, Marc Schmid, and László Toka. 2023. Pass receiver and outcome prediction in soccer using temporal graph networks. In ECML PKDD Workshop on Machine Learning and Data Mining for Sports Analytics. [23] Pieter Robberechts, Maaike Van Roy, and Jesse Davis. 2023. un-xPass: Measuring soccer player’s creativity. In Proceedings of the 29th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. [24] Alexander Scholtes and Oktay Karakuş. 2024. Bayes-xG: Player and position correction on expected goals (xG) using Bayesian hierarchical approach. Frontiers in Sports and Active Living 6 (2024). [25] William Spearman. 2018. Beyond expected goals. In MIT Sloan Sports Analytics Conference. [26] William Spearman, Austin Basye, Greg Dick, Ryan Hotovy, and Paul Pop. 2017. Physics-based modeling of pass probabilities in soccer. In MIT Sloan Sports Analytics Conference. [27] Michael Stöckl, Thomas Seidl, Daniel Marley, and Paul Power. 2021. Making offensive play predictable - Using a graph convolutional network to understand defensive performance in soccer. In MIT Sloan Sports Analytics Conference.

CIKM ’26, November 07–11, 2026, Rome, Italy

[28] Masakiyo Teranishi, Kazushi Tsutsui, Kazuya Takeda, and Keisuke Fujii. 2023. Evaluation of creating scoring opportunities for teammates in soccer via trajectory prediction. In ECML PKDD Workshop on Machine Learning and Data Mining for Sports Analytics. [29] Maaike Van Roy, Lorenzo Cascioli, and Jesse Davis. 2023. ETSY: A rule-based approach to event and tracking data synchronization. In ECML PKDD Workshop on Machine Learning and Data Mining for Sports Analytics. [30] Petar Velickovic, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Liò, and Yoshua Bengio. 2018. Graph attention networks. In Proceedings of the 6th International Conference on Learning Representations. [31] Ferran Vidal-Codina, Nicolas Evans, Bahaeddine El Fakir, and Johsan Billingham. 2022. Automatic event detection in football using tracking data. Sports Engineering 25, 18 (2022). [32] Zhe Wang, Petar Velickovic, Daniel Hennes, Nenad Tomasev, Laurel Prince, Michael Kaisers, Yoram Bachrach, Romuald Elie, Li Kevin Wenliang, Federico Piccinini, William Spearman, Ian Graham, Jerome T. Connor, Yi Yang, Adrià Recasens, Mina Khan, Nathalie Beauguerlange, Pablo Sprechmann, Pol Moreno, Nicolas Heess, Michael Bowling, Demis Hassabis, and Karl Tuyls. 2024. TacticAI: An AI assistant for football tactics. Nature Communications 15, 1906 (2024).


