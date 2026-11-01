                      Digital Object Identifier




                      Does 3D Pose Improve Action Valuation
                      in Football? An Empirical Study of Pose
                      Representations and Learning
                      Objectives
                      RIKUHEI UMEMOTO1 , KENJIRO IDE1 , SOHAM MAJUMDER2 , ULF BREFELD2 , and KEISUKE
arXiv:2610.38308v1 [cs.CV] 28 Oct 2026




                      FUJII1,3 (Member, IEEE)
                      1
                           Graduate School of Informatics, Nagoya University, Furo-cho, Chikusa, Nagoya, Aichi, Japan
                      2
                           Institute of Computer Science, Leuphana University of Lüneburg, Lüneburg, Germany
                      3
                           Information Technology Center, Nagoya University, Furo-cho, Chikusa, Nagoya, Aichi, Japan
                      Corresponding author: Keisuke Fujii (email: fujii@i.nagoya-u.ac.jp)
                      This work was financially supported by JST SPRING Grant Number JPMJSP2125 and JSPS KAKENHI Grant Number 23H03282. R.
                      Umemoto would like to take this opportunity to thank the “THERS Make New Standards Program for the Next Generation Researchers”.




                                         ABSTRACT Football action valuation estimates players’ contributions to future scoring. Existing multi-
                                         agent deep reinforcement learning (MADRL) models use 2D positions and velocities, omitting posture
                                         information relevant to imminent actions. We investigate whether adding 3D pose to a SARSA-based
                                         model improves observed-action values relative to attack returns: goals, conceded goals or final expected
                                         possession value. Using UEFA Champions League 2022/23 event, tracking and 3D pose data, we compare
                                         six representations (no pose, raw joints, torso and head orientation, and spatial-temporal graph convolutional
                                         network (ST-GCN) embeddings) across five learning settings and three seeds. The settings vary temporal-
                                         difference targets and action-prediction loss, with Monte Carlo return regression as a reference. Across 50
                                         on-ball and off-ball comparisons, pose robustly improved return prediction in only three, all using torso and
                                         head orientation, while worsening it in twelve, mostly with ST-GCN. Training choices had greater effects:
                                         removing the action-prediction loss raised on-ball skill of position-only values from 0.003 to 0.040 and
                                         their correlation with expected goals from 0.23 to 0.60; the improvement in return prediction persisted at
                                         matched training length. Separately, pose improved prediction of the on-ball action 0.2 s ahead (macro AUC
                                         0.914 to 0.934 with raw joints), while the passer’s pose during execution improved pass-success prediction
                                         (AUC 0.844 to 0.856). Within this training protocol, pose informed imminent actions but rarely improved
                                         observed-action values.

                                         INDEX TERMS action valuation, deep reinforcement learning, multi-agent, 3D pose, graph convolutional
                                         network, sports analytics, football


                              This work has been submitted to the IEEE for possible publication.                        [7].
                            Copyright may be transferred without notice, after which this version may
                                                    no longer be accessible.
                                                                                                                           Action valuation estimates the contribution of each action
                                                                                                                        to future scoring opportunities. Value-based frameworks in-
                                                                                                                        clude expected possession value [8], [9] and reinforcement-
                        I. INTRODUCTION                                                                                 learning-based action valuation [10]–[13]. In particular,
                      Football analytics increasingly relies on event and tracking                                      MADRL formulates football as a sequential decision-making
                      data to model player behaviour and team tactics. Event data                                       problem with many interacting players and values both on-
                      describe discrete on-ball actions such as passes, shots and                                       ball and off-ball actions [11].
                      defensive events, while tracking data provide the continuous                                         These models describe the state by the positions and ve-
                      spatial configuration of the players and the ball. Together,                                      locities of the players and the ball. Position and velocity tell
                      these data have enabled models that estimate the value of                                         where a player is and how the player moves, but not how the
                      actions [1]–[3], possessions [4], [5] and tactical patterns [6],                                  player is prepared to act. Two players at similar locations and

                      VOLUME 4, 2016                                                                                                                                                  1
                                                                                    Umemoto et al.: 3D Pose and Action Valuation in Football



speeds may differ in body orientation, balance and readiness:           actions, also at matched training length, and that the
one may face the goal and be ready to receive or shoot, while           target of its public implementation can prevent learning.
the other may be turned away from the ball. Such differences          • We show that the same pose features improve the predic-
can change both the next action and its value, so an evaluation         tion of the on-ball action 0.2 s ahead and that the pose
that ignores them may assign the same value to situations that          of the passer at the pass is associated with its success,
are not equally promising.                                              so pose is informative about imminent actions and their
   Recent progress in player pose estimation makes 3D body-             execution although, in our data and settings, it rarely
joint information available in football [14]–[19], but its use          improves the values of the observed actions.
in value-based decision models remains limited. It is also
unclear how pose should be represented: raw joint coor-             II. RELATED WORK
dinates keep the full posture but enlarge the state, hand-          A. ACTION VALUATION IN FOOTBALL
crafted orientation features are compact and interpretable          Action valuation assigns to each action its contribution to
but discard most of the posture, and learned embeddings             future scoring. Event-based frameworks estimate how an
such as ST-GCN [20] compress short movements but may                action changes the probabilities of scoring and conceding
lose information relevant to valuation, especially when the         in the near future, as in VAEP [1], and expected possession
downstream reward is sparse.                                        value (EPV) models estimate the expected outcome of a
   This study asks whether adding 3D pose to an existing            possession from the full spatio-temporal configuration of the
MADRL action-valuation model [11] makes the values of               22 players and the ball [8], [22]. Reinforcement learning
the observed actions more valid. We keep the action space,          formulates the same problem as the estimation of action
reward and sequence model of the prior model and change             values in a sequential decision process: deep reinforcement
only the state representation, and we measure validity by           learning was first used to value actions in ice hockey and
comparing the values of the observed actions with the re-           football [10], [23], and multi-agent deep reinforcement learn-
alised returns of the attacks (a goal, a conceded goal or, other-   ing (MADRL) values both on-ball and off-ball actions of
wise, the expected possession value at the end of the attack),      all attacking players [11]. Subsequent studies extended this
separately for on-ball and off-ball time steps, and with an         line to richer decision-making states [24], to interpretable
expected-goals model for shots. A negative answer is hard to        valuation of all players with strategic multi-agent learning
interpret on its own: pose may carry no useful information, or      [13], and to the optimisation of decisions and tactics, such as
the information may not reach the values because of how they        player decisions in general [12], attacking strategies against
are learned. We therefore repeat the comparison under five          low-block defences with offline multi-agent reinforcement
learning settings, and we test separately, without the value        learning [25], and corner kicks with graph reinforcement
model, whether the same pose features carry information             learning [26]. These studies differ in the decision problem
about imminent actions and the outcome of a pass. We                and in the state, but, to our knowledge, none of them includes
found that pose robustly improved the values of the observed        the body pose of the players in the state. The present study
actions in only three of 50 comparisons, all with torso and         keeps the MADRL model of [11] and changes only its state
head orientation and in two of the five settings, that the          representation.
learning setting of the prior model limited the values far more        Action values have no ground truth, so their evaluation
than the state did, and that pose did improve the prediction of     is itself a design choice. Comparisons between valuation
the on-ball action 0.2 s ahead and the classification of pass       frameworks have shown that models that look similar can
success from the pose at the pass.                                  value the same actions differently [27]. The prior MADRL
                                                                    model [11] averaged the values of each player over a season
   The contributions of this paper are as follows.
                                                                    and compared the resulting ranking with season goals, expert
    • We extend a SARSA-based MADRL action-valuation                ratings, off-ball scoring opportunity (OBSO) [28] and its
      model [11] to 3D pose and compare raw joints, torso           extension C-OBSO [29], finding negative or no correlations,
      and head orientation [14], and ST-GCN embeddings              which were read as a different view of player contribution.
      [20] under the same protocol, evaluating the values of        Such comparisons position a new indicator against existing
      the observed actions against the realised returns and         ones, but they cannot show that one model is more valid than
      expected goals with match-level bootstrap confidence          another: the reference indicators rest on their own modelling
      intervals and the agreement of three seeds.                   assumptions and measure other quantities, a negative, null or
    • We show, across five learning settings and 50 compar-         positive correlation can each be explained after the fact, and
      isons, that pose robustly brings the action values closer     player-level rankings are confounded by playing position and
      to the realised returns in only three comparisons, all with   the number of attacks. The present study therefore evaluates
      torso and head orientation and none under Monte Carlo         the values against the realised returns of the same time
      return regression [21], and that ST-GCN embeddings            steps and uses an existing indicator, expected goals, only
      often make them worse.                                        as a reference for shots (Section V-C). Deep reinforcement
    • We show that the action-prediction loss of the prior          learning results are also known to vary strongly between
      model lowers the validity of the values of the observed       random seeds, so that conclusions from a single run or
2                                                                                                                            VOLUME 4, 2016
Umemoto et al.: 3D Pose and Action Valuation in Football



from confidence intervals that ignore this variation can be       The input is the state st seen from the target player, which
misleading [30], [31]; we therefore require differences to        consists of the 2D positions and velocities of the ball and all
agree across seeds.                                               22 players and, in the pose-aware conditions, a representation
                                                                  of the target player’s 3D pose. The output is the vector of
B. POSE IN SPORTS ANALYTICS                                       action values Q(st , ·).
Recent progress in pose estimation has made 3D body-joint             The reward follows the prior model [11]: it is zero except
information available in football, and pose has been used to      at the final time step T of a sequence, where it is 1 for a goal,
analyse particular actions. Body-orientation angles estimated     −1 if the team concedes in the opponent’s next attack, and
from broadcast video were associated with the strategies of       otherwise the expected score at the end of the sequence [8].
penalty takers and goalkeepers [15]. 3D body pose extracted       The EPV is read from the publicly available grid of 32 × 50
from broadcast footage was used to learn the save technique       pitch cells used by the OpenSTARLab implementation [36]1
of professional goalkeepers and to build an expected-saves        at the location of the last event of the sequence of a fixed
model [16], and 3D posture sequences of shots were collected      set of types (passes, crosses including crossed corners and
and embedded for posture analysis [18]. 3D player skeletons       free kicks, shots including direct free kicks, take-ons, in-
and body orientation reconstructed from broadcast video           terceptions, clearances, fouls, bad touches, and punches and
were used to estimate expected goals [17], [32], and head         pick-ups by the goalkeeper; the ball position if the event has
and shoulder angles from pose-enhanced tracking data were         no location), so it depends only on this location and is not
used to quantify the visual exploration of players [14]. Pass     fitted toPour data. With γ = 1, the return from step t is
success has been modelled from the positions and velocities                  T
                                                                  Gt =       k=t rk = rT . We call Gt the realised return; it is
in tracking data [33], [34], and the orientation of the passer    an observed goal or conceded goal for the sequences that end
and the receivers, combined with their locations, improved        with one, and otherwise this location-based estimate, not an
the estimation of which passes are feasible [35]. These stud-     observed number of goals.
ies target pose recovery or the analysis of single events such        As in the prior model, each outfield player of the attacking
as penalties, saves, shots, scanning and passes; they do not      team (the goalkeeper is excluded) is in turn the target player:
integrate pose into a sequential model that values the actions    a sequence gives one row per such player, which consists of
of all players over an attack. Their findings that pose informs   the states seen from this player and the actions of this player,
the next shot or pass motivate our analysis of imminent           and the model values the actions of the target player of the
outcomes (Section IV-E), which we perform with the same           row it is given. The network has no player identifier; the
features as the action-value model.                               target player is specified by its input slot and the relative-
   Skeleton-based action recognition represents a sequence        coordinate construction. All target players share the same
of body poses as a graph. ST-GCN [20] treats the joints as        network, and no joint policy or explicit coordination between
the vertices and the bones as the edges, and applies graph        players is optimised. We retain the term MADRL to remain
convolutions over the joints and temporal convolutions over       consistent with the prior model [11].
the frames, so that it learns spatial and temporal patterns
                                                                      An evaluation is valid when the value of the observed
of the skeleton jointly. We use ST-GCN to obtain a fixed-
                                                                  action agrees with what actually happened: Q(st , at ) should
length embedding of a five-frame window of the target
                                                                  be close to Gt , and the value of a shot should increase with
player’s pose. Unlike in action recognition, the embedding
                                                                  the probability that the shot is scored. This criterion concerns
is not trained to classify the movement itself; it is trained
                                                                  only the values of the observed actions. The return of an
jointly with the value model, only through the action-value
                                                                  action that was not taken is not observed, so the values of
objective.
                                                                  the other available actions, the ranking of the actions and the
                                                                  causal contribution of a player are not validated by it; values
III. PROBLEM STATEMENT
                                                                  learned from fixed data can be far from correct for actions
We consider attacking sequences of football matches sam-
                                                                  that are rare or absent in the data [37]. We regard pose as
pled at 5 Hz. At each time step t of a sequence, a target
                                                                  useful when it improves these properties over the same model
player of the attacking team takes an observed action at from
                                                                  without pose, trained in the same way. As a separate task, we
15 classes: idle and movement in eight directions for off-
                                                                  ask whether pose predicts imminent events from the same
ball players, shot, dribble, through pass, pass and cross for
                                                                  state: the on-ball action taken 0.2 s later and the success of a
the on-ball player, and a defensive action. As in the prior
                                                                  pass. We do not address pose estimation itself, counterfactual
model, a step is an on-ball step when its observed action is
                                                                  optimal actions, or changes of the reward.
one of the five on-ball actions, i.e., when the target player
plays the ball with one of these actions in that step; the
on-ball actions are masked at all other steps and the eight       IV. METHOD
movements and idle at on-ball steps, while the defensive
action is never masked. Between two on-ball events, the ball        1 The grid file of the OpenSTARLab implementation is identical to the
carrier is therefore labelled with a movement or idle, and only   EPV grid published at https://github.com/Friends-of-Tracking-Data-FoTD/
about 7% of the time steps are on-ball steps of some player.      LaurieOnTracking/blob/master/EPV_grid.csv.

VOLUME 4, 2016                                                                                                                         3
                                                                                                           Umemoto et al.: 3D Pose and Action Valuation in Football



                                                                              Action-value model (prior MADRL model; only 𝑢𝑡 differs)

                                                                                                                                         Validity: MSE against
        Tracking state                                                                                            𝑄 (𝑠𝑡 , 𝑎) for
                                                                                  FC +                                                   the realised return 𝐺𝑡
     𝑥𝑡 ∈ R92 : positions                                                                    GRU, 64 units,        15 actions,
                                                                                  ReLU                                                   on on- and off-ball
     and velocities of the                                                                   over the attack       masked by
                                                                                 64 units                                                steps; 𝜌(𝑄, xG) on
    ball and the 22 players                                                                                      on-/off-ball step
                                                                                                                                         shots
                                                                                 Training: SARSA TD loss + 𝜆 𝐴𝑆 L 𝐴𝑆 ;
                                                       𝑧𝑡 = [ 𝑥𝑡 ; 𝑢𝑡 ]
                                                                                 reward only at the end of the attack
                                                                          ⊕

                                  Pose representation 𝑢𝑡
                                                                               Imminent-outcome predictor (no value learning)
     3D pose of the target        none                     0
       𝑃𝑡 ∈ R5×29×3 : 29          raw joints              87
                                                                                   Gradient-boosted            on-ball action 0.2 s      Prediction: log loss,
    joints in the five 25 Hz      torso orientation        6
                                                                                   trees on 𝑥 and 𝑢            ahead;                    macro AUC and MCC;
     frames of a 5 Hz step        torso+head orientation 14
                                                                                  (without ST-GCN)             success of a pass         AUC for pass success
                                  ST-GCN 𝑔 𝜙 ( 𝑃𝑡 )      128
                                  ST-GCN+torso           134

FIGURE 1. Overview. The 92-dimensional position–velocity state of the ball and all players is concatenated with one of the pose representations of the target
player (dimensions on the right): none, raw joints, torso (and head) orientation features, or an ST-GCN embedding with or without torso features. In the action-value
model (top), the fused state is projected to 64 dimensions, encoded over the attacking sequence by a GRU, and mapped to action values; unavailable actions are
masked according to whether the observed action of the step is an on-ball action. The same state and pose features, except the ST-GCN embeddings, are given to
gradient-boosted trees for imminent events (bottom): the on-ball action 0.2 s ahead and, from the pose of the pass step, the success of a pass.



A. OVERVIEW                                                                           ht = GRUθ (ReLU(W zt ), ht−1 ), and mapped by a fully
Fig. 1 shows the two parts of the study. The action-value                             connected layer to qt = fθ (ht ), one value per action. As
model shares the action space, reward and sequence model                              in the implementation of the prior model, this layer has 16
of the prior model [11]; only the pose part of the state                              outputs: the 15 actions and a padding class, which is never an
differs between conditions. It is trained under several TD                            observed action and is not used in the evaluation.
settings (Section IV-C) and, as a reference, by Monte Carlo                              The prior model is trained with a SARSA [21], [39]
return regression [21] (Section V-B). The imminent-outcome                            temporal-difference (TD) loss and an action-prediction loss
predictor uses the same features without any value learning                           that uses the values as action scores:
(Section IV-E).
                                                                                                        yt = rt + γ mt+1 Q(st+1 , at+1 ),                         (1)
                                                                                                              1 X                    2
B. ACTION-VALUE MODEL                                                                                 LT D =         yt − Q(st , at ) ,                           (2)
                                                                                                             N t
Let xt ∈ R92 be the positions and velocities (px , py , vx , vy )                                               1 X                     
of the ball and the 22 players, in pitch coordinates with the                                         LAS = −         log softmax q̃t a ,                         (3)
                                                                                                                N t                       t
origin at the centre and the attacking team playing towards
positive x, divided by 52.5 m. The network has no player                                                 L = LT D + λAS LAS ,                                     (4)
identifier as input; instead, xt is built for each target player.
                                                                                      where mt+1 = 1 if step t + 1 belongs to the same sequence
Its first 84 dimensions are the other 21 players, with positions
                                                                                      and 0 at the end of the sequence, N is the number of real
relative to the target player and velocities in pitch coordi-
                                                                                      (non-padding) steps, and q̃t is qt with the values of the
nates, followed by the position and velocity of the ball and,
                                                                                      masked actions set to −99,999, so that the softmax runs over
in the last four dimensions, those of the target player in pitch
                                                                                      the available actions, the defensive action and the padding
coordinates. The 21 players are ordered by team (attacking
                                                                                      output, as in the implementation. We set γ = 1. The target
team first), then by the role label of the data (DF, FW, GK,
                                                                                      yt is computed from the values of the same network, without
MF) and then by the distance to the centre of the goal that
                                                                                      a separate target network, and is treated as a constant in the
the attacking team attacks; the order is computed at every
                                                                                      gradient computation. The prior model also has an L1 penalty
step, so a slot is not tied to one player. The target player is
                                                                                      on the weights; we set its weight to zero in all settings,
thus defined by the construction of the input rather than by
                                                                                      because with a positive weight the action prediction was not
an identity: it is the player in the last four dimensions, the
                                                                                      learned.
origin of the relative positions of the others and, in the pose-
aware conditions, the player whose pose is ut . Even without
pose, xt therefore differs between the target players of the                          C. LEARNING SETTINGS
same time step, and the GRU runs over the row of one target                           We train every pose condition under the following settings,
player, so its hidden state summarises the history seen from                          which differ in the TD target and the weight λAS of the action
that player. The fused state zt (Section IV-D) is projected                           supervision loss [11], [40].
by a fully connected layer with ReLU to 64 dimensions,                                  • Terminal TD: (1) with the standard terminal treatment
encoded by a one-layer GRU [38] with 64 hidden units,                                      (mT +1 = 0) over all real steps. With λAS = 0.01, the
4                                                                                                                                                     VOLUME 4, 2016
Umemoto et al.: 3D Pose and Action Valuation in Football



      weight of the prior model, this is the setting closest to     boosted trees on the same features. For the on-ball action,
      the prior model; we also train it with λAS = 0.               each on-ball step labelled shot, dribble, through pass, pass
   • Package TD: the target as computed by the public               or cross is predicted from the state xt−1 and pose features
      implementation of the prior model, over the padded            ut−1 of the previous step of the same sequence, i.e., 0.2 s
      length t = 0, . . . , Tmax − 2, so that the final reward of   before the step in which the action is taken; the five frames
      the longest sequence in a batch is not used and shorter       of step t − 1 all precede that step. We use the previous step
      sequences bootstrap from padded steps. We train it with       because the pose of the step itself shows the action being
      λAS = 0.01 and 0. This setting follows the public im-         executed, which would make the task recognition rather than
      plementation distributed through OpenSTARLab [36].            prediction. For pass success, each on-ball step labelled pass,
With λAS = 0, the model is trained without an auxiliary             through pass or cross is matched to the pass event of the
action-prediction objective. In all settings, our evaluation is     attacking team in the time window of the sequence, and the
restricted to observed-action values and does not validate the      success of that event is predicted from the state and the torso
ranking of alternative actions (Fig. 3).                            and head features of the passer at that step. Because the pass
                                                                    is played within this step, its pose can include the kick itself,
D. POSE REPRESENTATIONS                                             so this analysis relates the outcome of a pass to the posture
For each 5 Hz step, the target player’s 29 joints in the five       of its execution rather than predicting the outcome before the
25 Hz frames of the step are expressed relative to the mid-hip      pass. The ST-GCN embeddings are learned inside the value
joint and divided by 2.44 m, giving Pt ∈ R5×29×3 . The fused        model and are not used here.
state is zt = [xt ; ut ] with one of the following ut .
                                   92
   • None: ut is empty (zt ∈ R ).                                   F. TRAINING
   • Raw: the joint coordinates averaged over the valid             All action-value models are trained with Adam [41] (learning
      frames of the step, ut ∈ R87 .                                rate 10−4 , weight decay 10−5 ) and batches of 64 sequences,
   • Torso: the horizontal torso orientation, the unit vector       for at most 200 epochs with early stopping on the total val-
      perpendicular to the axis from the left to the right          idation loss L (patience 5, absolute minimum improvement
      shoulder and pointing to the front of the body, with its      10−4 ). As in the public implementation of the prior model,
      dot and cross products with the unit directions to the ball   which uses the same patience with a minimum improvement
      and to the centre of the opponent goal, ut ∈ R6 .             of 0.01, the test uses the weights at the end of training, i.e.,
   • Torso+head: the torso features plus the horizontal head        those of five epochs after the last improvement by more than
      orientation, perpendicular to the axis from the midpoint      the minimum. For TD, selecting instead the epoch with the
      of the left eye and ear to that of the right eye and ear,     lowest total validation loss would not select on the value
      with the sign chosen to agree with the neck-to-nose           error either, because this loss consists of the TD loss, which
      direction (or with the torso orientation when the nose        does not measure the distance to the true values [42], and,
      or neck is missing), and its dot and cross products with      with λAS = 0.01, the action-prediction loss. The gradient-
      the directions to the ball and to the goal and with the       boosted trees [43] (scikit-learn HistGradientBoostingClassi-
      torso orientation, ut ∈ R14 .                                 fier [44], at most 500 iterations, learning rate 0.05, internal
                                       128
   • ST-GCN: ut = gϕ (Pt ) ∈ R             , an ST-GCN embed-       early stopping on 15% of the training data) are fitted on the
      ding.                                                         training matches with five model seeds, and their predicted
                                           torso
   • ST-GCN+torso: ut = [gϕ (Pt ); ut            ] ∈ R134 .         probabilities are averaged.
The orientation features are computed in each frame with               The minimum improvement had different effects in the
the required joints and averaged over the frames of the step.       settings. Under terminal TD with λAS = 0.01, it was
Shoulder and head rotation angles of pose-enhanced tracking         about 0.5% of the total validation loss after the first epoch
data have been used in the same way as the orientation of the       (0.022), and the runs lasted 47 to 134 epochs; MC regression
body and of the gaze of players [14]. The encoder gϕ applies        (Section V-B) ran for 8 to 62 epochs with λAS = 0.01 and
two ST-GCN blocks [20] on the normalised adjacency matrix           6 to 12 with λAS = 0. Without the action loss, however,
of the 29-joint skeleton. Each block consists of a spatial graph    the validation loss of TD is the TD loss alone, which was
convolution followed by a temporal convolution with kernel          2.8 to 4.3 × 10−4 after the first epoch and decreased by at
size 3 and a residual connection; the first block maps the          most 0.47 × 10−4 over the next five epochs. No later epoch
3 coordinates to 64 channels and the second to 128. The             therefore counted as an improvement, and all 36 terminal and
output is averaged over the five frames and the 29 joints. The      package TD runs with λAS = 0 stopped after 1 + 5 = 6
encoder is initialised randomly and trained jointly with the        epochs regardless of their curves. In these runs, the validation
value model. The handling of missing joints and the details         loss fell by 2 to 12% from the first to the third epoch and
of the encoder are given in Appendices A and B.                     then varied within 6%, but it was lowest in the last epoch
                                                                    in 12 of the 36 runs, so a further slow decrease cannot be
E. IMMINENT-OUTCOME PREDICTION                                      excluded; the last weights were at most 5.1% above the
To test whether pose carries information about imminent             lowest validation loss of their run. These curves therefore do
events independently of value learning, we fit gradient-            not show that the values had converged, and the results of TD
VOLUME 4, 2016                                                                                                                     5
                                                                                    Umemoto et al.: 3D Pose and Action Valuation in Football



without the action loss are those after six epochs. They do        λAS = 0.01 and 0, package TD with λAS = 0, and MC
show that these values had been learned to some extent: after      regression with λAS = 0.01 and 0.
six epochs, they were closer to the returns than those with the
action loss after 47 to 134 epochs (Section VI-A).                 C. EVALUATION METRICS
                                                                   The primary metric is the mean squared error between the
V. EXPERIMENTAL SETUP                                              value                            and the realised return, MSE =
                                                                    1
                                                                      P of the observed action
                                                                                             2
A. DATASET                                                               t (Q(st , at )−G t )  , computed separately for on-ball and
                                                                   N
We used StatsPerform event data and Hawk-Eye tracking              off-ball steps of the test matches. Because the conditional
and 3D pose data (29 joints, 25 Hz) of UEFA Champions              mean of the return minimises the expected squared error,
League 2022/23 matches. Events were synchronised with the          the difference of the MSE of two models on the same steps
tracking data using ELASTIC [45], and the state–action–            estimates the difference of their mean squared distances from
reward data followed the OpenSTARLab format [36]. We               the true action values, without access to these values. The
removed stoppages, intervals affected by substitutions, dis-       TD loss does not have this property, because a small Bellman
missals or tracking errors, and sequences without usable           error does not imply values close to the true ones [42], so we
pose, aligned the attacking direction, and aggregated the data     do not use it to compare the models. We report it as the skill
to 5 Hz. Padding players that represent empty roster slots         1−MSE/Var(G), which compares the model with a constant
were excluded from event matching and from training. As            prediction of the mean return, and as the difference ∆ of the
in the prior model, the action-value model used the attacking      MSE of the seed-averaged values from that of the baseline
sequences in which at least two attackers entered the final        on the same steps, with 95% confidence intervals from 5,000
third (17.5 m beyond the centre line), about two thirds of the     bootstrap resamples of test matches [46]. These intervals
sequences. Each sequence was expanded into one row per             treat the seed-averaged values as fixed and do not include
attacking player; on-ball steps were counted only in the row       the variation between seeds. We therefore also computed the
of the ball carrier.                                               difference for each seed against the baseline of the same seed,
   The matches were split chronologically by competition           and call a difference robust only if its interval excludes zero
phase into training, validation and test sets, with no match in    and its sign is the same for all three seeds.
more than one set; a further set of matches reserved for pose-        We do not use correlations of season-averaged player
encoder pretraining was not used for the action-value models       values with existing indicators such as OBSO [28] or C-
or the imminent-outcome predictors; only the expected-goals        OBSO [29] as evidence of validity, for the reasons given in
model (Section V-C) was fitted on the shots of all matches         Section II. As a reference for on-ball values, we compared the
other than the test matches, including these. The training,        value of each observed shot, Q(st , shot), with the expected
validation and test sets contained 76, 15 and 12 matches           goals (xG) of the same shot. Because the event data contain
with 6,382, 1,202 and 971 attacking sequences and 616,731,         no xG, we fitted a logistic-regression xG model [47] on
117,097 and 97,100 time steps, respectively; expanded into         the 2,756 shots (own goals excluded) of the 107 non-test
the rows of the attacking players, they gave 43,812, 8,506 and     matches, with the distance and log-distance to the goal centre,
6,801 on-ball steps and 6,112,551, 1,160,946 and 962,800           the angle subtended by the posts, and indicators for headers,
off-ball steps. The training set was used to fit all models, the   penalties, direct free kicks, set pieces and fast breaks taken
validation set only for early stopping and for the selection of    from the event qualifiers. On the 299 test shots, its AUC for
one hyperparameter of the analysis in Section VII, and the         goals was 0.75 and its log loss 0.274, against 0.311 for a
test set only for the final evaluation.                            constant prediction. Each shot step of the action-value model
                                                                   was matched to the shot event of the same match inside the
B. COMPARED CONDITIONS                                             time window of its sequence, by order or, when the counts
We compared six conditions: none (baseline), raw, torso,           differed, by location within 10 m; all 250 shot steps were
torso+head, ST-GCN and ST-GCN+torso. Each condition                matched to 243 events with 27 goals. We use xG as an
was trained with three random seeds (42, 43, 44) under each        auxiliary reference for the scoring potential of observed shots
learning setting, and each pose condition was compared with        and, with a positive association specified in advance, report
the baseline of the same setting.                                  the Spearman correlation ρ(Q, xG) with match-bootstrap
   As a reference outside the proposed model, every condi-         confidence intervals. xG is not a ground truth for action
tion was also trained by Monte Carlo (MC) return regression        values and does not use pose.
(MC regression for short) [21], in which the bootstrapped             For imminent outcomes, the on-ball action prediction was
target yt is replaced by
                       Pthe observed return Gt (Section III),      evaluated by the log loss and the one-vs-rest macro AUC,
so that LM C = N1 t (Gt − Q(st , at ))2 replaces LT D ,            and, because passes dominate, also by the macro average
with λAS = 0.01 and 0. MC regression does not propagate            precision (PR-AUC), macro-F1 and the Matthews correlation
values through the model’s own estimates and thus serves to        coefficient (MCC) [48] of the class with the largest ratio of
test whether the results depend on bootstrapping. Package          predicted probability to its training share. Pass success was
TD with λAS = 0.01 did not learn (Section VI-A), which             evaluated by the AUC and the log loss. Differences from the
leaves five settings for the comparison: terminal TD with          state-only model are reported with 95% confidence intervals
6                                                                                                                            VOLUME 4, 2016
Umemoto et al.: 3D Pose and Action Valuation in Football



from 2,000 bootstrap resamples of test matches, together with       the constant prediction, and the difference was driven by one
the number of the five model seeds for which the difference         baseline seed: the off-ball MSE of the baseline was 3.365,
has the same sign.                                                  3.408 and 3.755 × 10−2 for seeds 42, 43 and 44, and the
   For the qualitative examples, the cases were selected by a       differences of raw and torso from the baseline seed with the
rule fixed before inspection. We compared the baseline with         same number changed sign across the seeds (+3.0, −5.7,
the pose condition that had the best on-ball primary metric         −37.7 and +19.5, +32.7, −24.4 × 10−4 ). The same seed
under terminal TD with λAS = 0.01. For each test step,              also reversed the sign of the differences of both ST-GCN
the values were averaged over the three seeds, and ∆t =             conditions. This is why we require the same sign for all seeds.
|Qpose (st , at ) − Gt | − |Qnone (st , at ) − Gt | was computed.      The learning setting changed the values far more than pose
Success cases were the steps with the smallest ∆t and failure       did. Under terminal TD with λAS = 0.01, the setting closest
cases those with the largest ∆t , taking at most one step per       to the prior model, the baseline was barely better than a
sequence within each of the four lists (success and failure,        constant prediction on on-ball steps (skill 0.003) and worse
on-ball and off-ball) and only steps without missing pose.          on off-ball steps (−0.057), and its shot values correlated
Because a single outcome is noisy, these cases illustrate how       only weakly with xG (0.23). Removing the action-prediction
pose changes the values; they are not evidence of validity.         loss raised the skill to 0.040 and 0.018 and the correlation
                                                                    with xG to 0.60; the MSE of the baseline decreased by
D. IMPLEMENTATION DETAILS                                           12.2 × 10−4 [8.4, 16.0] on on-ball and 12.1 × 10−4 [8.8,
Experiments were run with PyTorch 2.9.1 (CUDA 12.8) and             15.2] on off-ball steps, with the same sign for all seeds.
PyTorch Lightning 2.5.6 on NVIDIA A100-SXM4-80GB                    MC regression reached a similar level with either weight
GPUs, one GPU per run.                                              (on-ball skill 0.034 and 0.042, correlation with xG 0.64 and
                                                                    0.61). Package TD with λAS = 0.01 did not learn in any
VI. RESULTS                                                         of the 18 runs: from the first epoch, all action values moved
A. VALIDITY OF ACTION VALUES                                        together towards large negative values (mean value of the
Table 1 and Fig. 2 show the first main result. Across the five      observed action −7.7 after the first and −36 after the sixth
settings, five pose conditions and on-ball and off-ball steps,      epoch for the baseline, −11 to −26 at the end for the ST-
pose brought the values robustly closer to the realised returns     GCN conditions), and early stopping ended the runs after
in three of the 50 comparisons and made them robustly worse         six to 25 epochs. With λAS = 0, the same target stayed in
in twelve. All three improvements came from torso+head,             the range of the returns within the six epochs trained; like
on on-ball steps under terminal TD with λAS = 0.01                  every TD run without the action loss, these runs stopped
(∆ = −2.71 × 10−4 ) and on both kinds of steps under                after six epochs (Section IV-F), so whether their values would
package TD with λAS = 0 (−2.23 and −1.41 × 10−4 ).                  drift with longer training is untested. This limits the weight
The on-ball difference of torso+head was negative in all            of the two improvements of torso+head in this setting. Its
five settings, but under terminal TD with λAS = 0, which            improvement in the prior setting was about a fifth of the effect
differs from package TD only in the treatment of the end            of removing the action-prediction loss on the baseline (−2.71
of the sequences, its interval included zero (−1.08 [−2.60,         against −12.2 × 10−4 ), and its values there remained less
+0.59]), and under both MC settings its seeds also disagreed        skilful than the position-only values without that loss (0.010
in sign; its off-ball difference was negative in three settings     against 0.040). Thus pose improved the values only in a few
and positive in two. Nine of the twelve robust deteriorations       comparisons of two TD settings and in neither MC setting.
came from the ST-GCN embeddings: ST-GCN on both kinds
of steps under terminal and package TD with λAS = 0 (+4.4           B. POSE AND IMMINENT OUTCOMES
to +6.2×10−4 ), ST-GCN+torso on both kinds of steps under           Table 2 shows the second main result: the same pose features
terminal TD with λAS = 0 (+3.0 and +1.6) and on on-                 that did not robustly improve the action values improved the
ball steps under terminal TD with λAS = 0.01 (+2.7), and            prediction of the on-ball action 0.2 s ahead. The raw joints
both on off-ball steps under MC regression with λAS = 0.01          reduced the log loss by 0.038 and raised the macro AUC
(+13.1 and +16.6). The other three came from torso under            from 0.914 to 0.934 and the MCC from 0.424 to 0.512, for
MC regression (+1.05 to +1.58), and the raw joints were             all five model seeds; the torso and head orientation features
within the noise of the baseline in every comparison. On the        gave smaller improvements, with the same sign of the AUC
shots, no pose condition had a correlation with xG above the        and MCC differences for all five model seeds and intervals
interval of its baseline, and the ST-GCN conditions had the         excluding zero except for the MCC of torso. The gains also
lowest correlations under three settings.                           appeared in the metrics that weight the rare actions: with
   The confidence intervals over matches alone would have           the raw joints, the macro PR-AUC rose by +0.062 [+0.027,
suggested more effects. Under terminal TD with λAS =                +0.085] and the macro-F1 by +0.069 [+0.054, +0.085], and
0.01, the off-ball intervals of four pose conditions exclude        the PR-AUC of shots rose from 0.66 to 0.78 (base rate 0.04),
zero (raw −3.99, torso +5.93, ST-GCN +4.55 and ST-                  of dribbles from 0.28 to 0.40 and of crosses from 0.64 to 0.73.
GCN+torso +3.82 × 10−4 ), but every condition in this set-          Through passes, with 18 test cases, were hardly predicted
ting, including the baseline, had a larger off-ball error than      with any features.
VOLUME 4, 2016                                                                                                                    7
                                                                                                               Umemoto et al.: 3D Pose and Action Valuation in Football



TABLE 1. Validity of the action values on the test matches under five learning settings. Skill: 1 − MSE/Var(G), mean over three seeds; ∆: MSE of the
seed-averaged values minus that of the baseline of the same setting on the same steps (×10−4 , 95% CI from 5,000 bootstrap resamples of test matches);
ρ(Q, xG): Spearman correlation of the seed-averaged shot values with xG on the 250 test shots [95% CI]. Var(G) = 3.507 × 10−2 (on-ball) and 3.319 × 10−2
(off-ball). Negative ∆ means closer to the realised return; bold: best skill and ρ within each setting (ties at the shown precision all in bold); † : robust difference (CI
excludes zero and the same sign for all three seeds), in either direction. Package TD with λAS = 0.01 did not learn and is not shown.


                                              On-ball steps                                      Off-ball steps                        Shots
                     Condition         Skill        ∆ [95% CI]      Skill                              ∆ [95% CI]                ρ(Q, xG) [95% CI]
                     Terminal TD, λAS = 0.01 (prior model)
                     none (baseline) 0.003               –         −0.057                                 –                       0.23 [0.15, 0.32]
                     raw              0.000   +0.40 [−1.21, +1.94] −0.017                        −3.99 [−7.01, −0.91]             0.26 [0.16, 0.36]
                     torso            0.005   −0.89 [−1.98, +0.19] −0.085                        +5.93 [+2.90, +8.99]             0.25 [0.16, 0.35]
                     torso+head       0.010 −2.71† [−4.04, −1.49] −0.046                         −0.50 [−3.00, +2.40]             0.22 [0.14, 0.30]
                     ST-GCN           0.005   −1.17 [−3.16, +0.57] −0.043                        +4.55 [+1.77, +6.98]             0.17 [0.09, 0.25]
                     ST-GCN+torso −0.007 +2.69† [+1.09, +4.41] −0.047                            +3.82 [+0.65, +6.91]             0.13 [0.06, 0.22]
                     Terminal TD, λAS = 0
                     none (baseline) 0.040               –         0.018                                  –                       0.60 [0.48, 0.70]
                     raw              0.038   +0.46 [−0.08, +0.96] 0.018                         −0.27 [−0.70, +0.17]             0.57 [0.44, 0.69]
                     torso            0.038   +0.24 [−0.63, +1.09]  0.016                        +0.42 [−0.12, +0.97]             0.53 [0.39, 0.67]
                     torso+head       0.042 −1.08 [−2.60, +0.59]   0.018                         −0.29 [−1.05, +0.49]             0.53 [0.37, 0.67]
                     ST-GCN           0.021 +5.52† [+3.51, +7.93]   0.002                        +4.42† [+1.88, +7.17]            0.59 [0.43, 0.72]
                     ST-GCN+torso 0.028 +2.99† [+1.39, +4.68]       0.011                        +1.64† [+0.04, +3.17]            0.56 [0.40, 0.71]
                     Package TD, λAS = 0
                     none (baseline) 0.030               –          0.010                                 –                       0.56 [0.44, 0.67]
                     raw              0.026   +1.06 [+0.35, +1.65]  0.008                        +0.54 [−0.07, +1.07]             0.54 [0.40, 0.67]
                     torso            0.029   +0.02 [−0.80, +0.73]  0.008                        +0.58 [+0.03, +1.09]             0.52 [0.37, 0.65]
                     torso+head       0.036 −2.23† [−3.75, −0.74] 0.014                          −1.41† [−2.39, −0.41]            0.51 [0.36, 0.65]
                     ST-GCN           0.011 +5.31† [+3.58, +7.08] −0.012                         +6.17† [+3.73, +8.56]            0.58 [0.43, 0.71]
                     ST-GCN+torso 0.020       +2.33 [+0.90, +3.50]  0.003                        +1.83 [+0.34, +3.13]             0.56 [0.40, 0.71]
                     MC regression, λAS = 0.01
                     none (baseline) 0.034               –         0.014                                 –                        0.64 [0.54, 0.73]
                     raw              0.035   −0.27 [−1.40, +0.68]  0.011                      +0.96 [−0.05, +1.89]               0.57 [0.47, 0.67]
                     torso            0.031 +1.58† [+0.11, +3.07]   0.012                      +1.08 [−0.25, +2.44]               0.53 [0.42, 0.64]
                     torso+head       0.038 −1.32 [−3.42, +0.82]    0.012                      +0.52 [−1.31, +2.51]               0.56 [0.45, 0.67]
                     ST-GCN           0.027   +0.87 [−2.63, +4.07] −0.045                     +13.08† [+9.38, +16.59]             0.40 [0.31, 0.50]
                     ST-GCN+torso 0.021       +1.75 [−2.95, +6.00] −0.058                     +16.63† [+11.98, +20.84]            0.47 [0.38, 0.54]
                     MC regression, λAS = 0
                     none (baseline) 0.042               –          0.016                                 –                       0.61 [0.50, 0.70]
                     raw              0.040   +0.35 [−0.34, +1.04]  0.014                        +0.29 [−0.54, +1.01]             0.54 [0.44, 0.65]
                     torso                          †
                                      0.039 +1.05 [+0.08, +2.03]    0.013                             †
                                                                                                 +1.05 [+0.10, +1.93]             0.52 [0.40, 0.63]
                     torso+head       0.042   −0.23 [−1.69, +1.19]  0.016                        +0.26 [−1.16, +1.53]             0.47 [0.33, 0.61]
                     ST-GCN           0.039   +0.91 [−0.72, +2.63]  0.018                        −0.51 [−1.96, +0.90]             0.43 [0.28, 0.57]
                     ST-GCN+torso 0.044 −0.33 [−1.91, +1.21]       0.019                         −1.00 [−2.46, +0.40]             0.50 [0.38, 0.60]


TABLE 2. Prediction of the on-ball action 0.2 s ahead on the test matches                the kick (Section IV-E), to the 92-dimensional state raised the
(6,388 steps; pass 87%, cross 5%, dribble 4%, shot 4%, through pass 0.3%)
by gradient-boosted trees on the state and pose features of the previous step.           test AUC from 0.844 to 0.856 (difference +0.012 [+0.007,
Differences from the state-only model with 95% CIs over test matches; in                 +0.018], higher for each of the five model seeds); the log loss
parentheses, the number of the five model seeds with the same sign; bold:
best value of each column.
                                                                                         decreased from 0.305 to 0.298 (difference −0.007 [−0.011,
                                                                                         −0.004]; constant prediction 0.412).
 Features        Log loss        Macro AUC          MCC
 state only       0.304            0.914            0.424                                C. QUALITATIVE EXAMPLES
 +torso          −0.013         +0.009 (5/5)     +0.013 (5/5)
             [−0.017, −0.009] [+0.006, +0.013] [−0.001, +0.027]                          Fig. 3 shows the cases selected by the rule in Section V-C;
 +torso+head     −0.013         +0.010 (5/5)     +0.014 (5/5)                            torso+head had the best on-ball metric under terminal TD
             [−0.016, −0.009] [+0.007, +0.012] [+0.003, +0.024]                          with λAS = 0.01. In the success cases, torso+head moved the
 +raw            −0.038         +0.020 (5/5)     +0.089 (5/5)
             [−0.043, −0.032] [+0.011, +0.028] [+0.075, +0.101]                          values of the observed actions towards the realised returns:
                                                                                         it raised the value of a scored shot from 0.15 to 0.23 and
                                                                                         those of a through pass and of an off-ball movement that
                                                                                         the baseline valued below the return. In the on-ball failure,
   Pose was also associated with the outcome of the pass                                 it raised the value of an unscored shot in the same way, and
that it accompanies. For pass success, the matched sequences                             in the off-ball failure, the head of the target was below the
(1,845 of the 6,332 training and 390 of the 969 test sequences                           hips in all frames of the step, a fallen or misestimated pose,
that contain a pass, in which the numbers of passes and pass                             and the value of the observed movement fell from 0.04 to
events agreed) gave 10,034 training and 2,109 test passes,                               −0.80. The values of the unobserved off-ball actions, far
85% of them successful. Adding the 14 torso and head                                     below the range of the returns for both models, show that
features of the passer at the pass step, whose pose can include                          with λAS = 0.01 the action-prediction loss uses the values
8                                                                                                                                                           VOLUME 4, 2016
Umemoto et al.: 3D Pose and Action Valuation in Football



                                                     on-ball             off-ball           robust             not robust

                  Terminal, λAS = 0.01 (prior)       Terminal, λAS = 0              Package, λAS = 0                MC, λAS = 0.01                 MC, λAS = 0

           raw

          torso

    torso+head

      ST-GCN

ST-GCN+torso

                    −5       0        5               0            5                  0          5              0           10        20     −2         0          2


                                      ΔMSE from the baseline of the same setting (×10−4 ); negative: closer to the realised return

FIGURE 2. Difference in MSE between each pose condition and the baseline of the same setting on the test matches (×10−4 , values averaged over three seeds),
with 95% CIs from 5,000 bootstrap resamples of test matches. Filled markers: robust differences (CI excludes zero and the same sign for all three seeds). The
horizontal scales differ between panels. Package TD with λAS = 0.01 did not learn and is not shown.



as action scores (Section VII).                                                        TABLE 3. Action information in the values (probe on the five on-ball action
                                                                                       values, fitted on the training matches, tested on the 6,801 on-ball test steps):
                                                                                       macro AUC and MCC for terminal TD with λAS = 0.01 trained until early
                                                                                       stopping (47–134 epochs) or for six epochs, and with λAS = 0 (six epochs).
VII. DISCUSSION
                                                                                       Bold: best value of each column; † : robust difference from the baseline of the
A. WHY POSE DID NOT IMPROVE THE ACTION VALUES                                          same column, in either direction.

Pose carried information about the next action and about the
                                                                                                         λAS = 0.01 λAS = 0.01, 6 ep.    λAS = 0
outcome of a pass at its execution (Section VI-B), but not                                Condition     AUC    MCC AUC       MCC       AUC   MCC
in a form that improved the action values. We discuss two                                 none          0.735 0.131 0.853 0.270       0.871 0.266
factors that may explain this gap; the experiments support                                raw          0.792† 0.187 0.818† 0.234† 0.880 0.296†
                                                                                          torso         0.726 0.108 0.840   0.239†    0.873 0.265
the first, whereas the second is a hypothesis that we did not
                                                                                          torso+head    0.746 0.141 0.830   0.226     0.866 0.283†
test directly.                                                                            ST-GCN             †     †
                                                                                                       0.800 0.181 0.800 †  0.208 †   0.846† 0.258
   The first is the learning setting of the prior model. Auxil-                           ST-GCN+torso 0.801† 0.189 0.794† 0.183†     0.876 0.288
iary losses can help reinforcement learning when they shape
a shared representation [49], but the action-prediction loss
uses the values themselves as action scores, so it competes                            regression that predicts the observed on-ball action from
with value learning: under terminal TD with λAS = 0.01, the                            the five on-ball action values of the step (a probe [50]),
weighted gradient of the action loss was 0.43 to 0.96 times                            on the 76 training matches, with the inverse regularisation
that of the TD loss (median over epochs, mean over seeds),                             strength chosen from {10−3 , . . . , 102 } by the log loss on the
against 0.07 to 0.22 under MC regression. Because early                                validation matches, and evaluated it once on the test matches
stopping monitors the total validation loss, which includes                            (Table 3). After six epochs, the values of the baseline pre-
the action loss, training continued for 47 to 134 epochs                               dicted the action with a macro AUC of 0.853; after training to
(Fig. 4), although the validation TD loss rose after the first                         the end, only 0.735. With long training, raw, ST-GCN and ST-
epoch in every run and, in 14 of the 18 runs, never fell below                         GCN+torso had robustly higher AUC than the baseline (0.79
its first-epoch value (in the other four, it was at most 13%                           to 0.80), which could be read as pose information reaching
lower after 52 to 82 epochs). With λAS = 0, in contrast, ev-                           the values; at matched length, however, every pose condition
ery terminal-TD run stopped after six epochs (Section IV-F).                           was below the baseline, robustly so for raw, ST-GCN and ST-
To separate the action loss from the training length, we                               GCN+torso. The apparent advantage of the pose conditions
retrained terminal TD with λAS = 0.01 for exactly six                                  after longer training may partly reflect the decline in the
epochs. The baseline then had an on-ball skill of −0.039                               baseline during training, rather than solely information added
and an off-ball skill of −0.249, below the 0.040 and 0.018                             by pose. A similar pattern was observed with the probe fitted
reached without the action loss after the same six epochs;                             on the validation matches or on a subset of the training
the MSE without the action loss was lower by 24.2 × 10−4                               matches with a fixed regularisation strength, and with the four
[19.6, 28.5] on on-ball and 82.0 × 10−4 [76.4, 87.4] on off-                           on-ball actions other than the rare through pass.
ball steps, for every seed. The action loss therefore lowered                             The second factor may be the distance between the pos-
the validity of the values both at matched length and at the                           ture and the reward. In the settings without the action loss
length chosen by early stopping.                                                       and with MC regression, the baseline learned the position
   Training length did change how much information about                               information well enough for its shot values to agree with xG,
actions the values hold. We fitted a multinomial logistic                              and pose robustly improved the values only for torso+head
VOLUME 4, 2016                                                                                                                                                            9
                                                                                                                           Umemoto et al.: 3D Pose and Action Valuation in Football




                    attacking team          defending team          target player        ball                   Gt              none          torso+head

             (a) Success, on-ball: observed shot, Gt = 1.00, Δt = −0.081
                                                                                                               1.00

                                                                                                               0.75




                                                                                                   Q(st , a)
                                                                                                               0.50

                                                                                                               0.25

                                                                                                               0.00

                                                                                                                         shot     drib
                                                                                                                                       ble       pass   pass    cros
                                                                                                                                                                    s
                                                                                                                                             ugh
                                                                                                                                        thro

             (b) Success, on-ball: observed through pass, Gt = 0.01, Δt = −0.076

                                                                                                                0.1

                                                                                                                0.0




                                                                                                  Q(st , a)
                                                                                                              −0.1

                                                                                                              −0.2

                                                                                                                         shot     drib
                                                                                                                                       ble      pass    pass    cros
                                                                                                                                                                    s
                                                                                                                                            ugh
                                                                                                                                       thro

             (c) Success, off-ball: observed ←, Gt = 0.02, Δt = −0.384
                                                                                                                0.0

                                                                                                              −2.5
                                                                                                Q(st , a)




                                                                                                              −5.0

                                                                                                              −7.5

                                                                                                            −10.0
                                                                                                                         idle    →       ↗    ↑    ↖    ←   ↙   ↓       ↘



             (d) Failure, on-ball: observed shot, Gt = 0.09, Δt = +0.091
                                                                                                                0.2


                                                                                                                0.0
                                                                                                  Q(st , a)




                                                                                                              −0.2


                                                                                                              −0.4
                                                                                                                         shot     drib
                                                                                                                                       ble       pass   pass    cros
                                                                                                                                                                    s
                                                                                                                                             ugh
                                                                                                                                        thro

             (e) Failure, off-ball: observed ↖, Gt = 0.02, Δt = +0.787
                                                                                                                     0
                                                                                                    Q(st , a)




                                                                                                                −5



                                                                                                                −10

                                                                                                                         idle    →       ↗    ↑    ↖    ←   ↙   ↓       ↘

FIGURE 3. Qualitative cases selected by the rule in Section V-C (terminal TD, λAS = 0.01, torso+head against none, values averaged over three seeds): (a)–(c)
success cases with the smallest ∆t and (d), (e) failure cases with the largest ∆t . Left: players and ball, with the attacking team playing from left to right; middle:
front view of the target’s pose averaged over the frames of the step; right: values of the available actions, with the observed action in red, and the realised return Gt .
The share of test steps with ∆t < 0 was 0.61 on-ball and 0.47 off-ball.




10                                                                                                                                                                          VOLUME 4, 2016
Umemoto et al.: 3D Pose and Action Valuation in Football



            λAS = 0.01           λAS = 0         seed 42          seed 43           seed 44         the presence of missing or padded steps rather than on the
                                                                                                    posture itself, and both affect only the ST-GCN conditions,
             (a) validation TD loss                            (b) validation action loss
                                                                                                    which used the same joints as raw but, unlike raw, made the
0.003                                              2.0
                                                                                                    values robustly worse. We did not test these explanations;
                                                                                                    masking the missing joints and padded steps, normalising
                                                   1.5
0.002                                                                                               without them, or replacing batch normalisation by a per-
                                                   1.0
                                                                                                    sample normalisation would separate them from the effect
0.001
                                                                                                    of the sparse reward. Constraints on the embedding or a
                                                   0.5                                              pretraining objective related to value, such as the outcome
                                                                                                    of the next action, may be needed before learned embeddings
        1                10                100             1                10                100
                         epoch                                              epoch                   can help.

FIGURE 4. Validation losses of the baseline under terminal TD per epoch                             C. IMPLICATIONS FOR EVALUATING ACTION VALUES
(logarithmic scale). (a) TD loss with λAS = 0.01 and 0; (b) action-prediction
loss with λAS = 0.01. With λAS = 0.01, early stopping on the total validation                       Three aspects of the evaluation changed the conclusions.
loss ended the runs after 83 to 134 epochs, while the TD loss stayed above its                      Comparing the values with the realised returns and with xG
first-epoch value; with λAS = 0, all runs stopped after six epochs, because
the minimum improvement of early stopping exceeded the whole decrease of                            showed that the values of the prior setting were close to
the loss after the first epoch (Section IV-F). The levels of the two TD losses are                  a constant, which correlations of player-level values with
not comparable, because each is computed from the model’s own values.
                                                                                                    other indicators could not reveal. Requiring the same sign
                                                                                                    for all seeds removed off-ball differences, in both directions,
                                                                                                    that a bootstrap over matches alone would have declared
under package TD, whereas the same features improved the                                            significant. Matching the training length suggested that the
prediction of the next action and the classification of pass                                        apparent gain of pose in the action information of the values
success at the pass. Body orientation and preparation affect                                        may partly reflect the decline in the baseline during longer
the execution of the next action, but the end of an attack                                          training. Evaluations of action-value models should therefore
is several actions and several seconds later, and its outcome                                       report the error against realised returns, a reference such as
depends on many later decisions of both teams. A small effect                                       xG for shots, the results of several seeds, and the training
on the next action may therefore be diluted in a sparse and                                         length, and should select models on the value error rather
noisy return. Other explanations are not excluded, such as                                          than on a loss that includes action prediction or on the TD
errors and gaps in the estimated poses, the absence of the                                          loss [42].
poses of the other players, the capacity of the model and the
amount of data; comparing returns over horizons of different                                        D. LIMITATIONS
lengths would separate the distance to the reward from these.                                       The data come from one competition and season, and the
                                                                                                    test set contains 12 matches. The models were stopped on
B. LEARNED POSE EMBEDDINGS                                                                          the total validation loss and the test used the last weights,
The ST-GCN embeddings, trained from random initialisation                                           as in the public implementation of the prior model; without
jointly with the value model, accounted for nine of the twelve                                      the action loss, all TD runs stopped after six epochs because
robust deteriorations, in four of the five settings, and they                                       the minimum improvement of early stopping was larger than
lowered the correlation of the shot values with xG under three                                      the whole decrease of their validation loss after the first
settings. With λAS = 0.01, their seed-averaged values of                                            epoch, and in a third of these runs the validation loss was
the observed off-ball actions fell outside the range [−1, 1] of                                     still lowest in the last epoch (Section IV-F); in particular,
the returns at 82 and 124 test steps, which no such value of                                        the stability of package TD without the action loss was
the baseline did. A 128-dimensional embedding trained only                                          tested only over these six epochs. We did not test whether
through a sparse value signal can fit noise in the training re-                                     longer training, the selection of the weights with the lowest
turns: the encoder raised the number of trainable parameters                                        validation error of the values, or a different optimisation
from about 32,000 to 120,000 (Table 4).                                                             of the jointly trained ST-GCN encoder would change the
   Two properties of our encoder input may add to this                                              comparison, so the results hold for this training protocol. The
(Appendix A). First, the input has no mask: a missing joint                                         pose condition for the qualitative examples was chosen on the
is set to the position of the mid-hip, and a missing frame,                                         test results. The imminent-action analysis used the pose 0.2 s
a step without pose and a padded step are all zeros, so                                             before the action, which may already show the backswing
the encoder cannot tell absent pose from a posture with                                             of a kick, so it is short-range anticipation; the pass-success
joints at the hip. Second, batch normalisation [51] inside                                          analysis used the pose of the step of the pass, which can
the encoder computes its statistics over all steps of a batch,                                      include the kick, and only the sequences in which passes
including these zero inputs, whose share depends on the                                             and events could be matched one to one (29% of the training
lengths of the sequences in the batch, while the evaluation                                         and 40% of the test sequences), and our xG model uses only
uses the running statistics accumulated during training. Both                                       basic shot features. The off-ball values were compared only
can make the embedding of the same posture depend on                                                with the realised returns; a step-level comparison with an
VOLUME 4, 2016                                                                                                                                                  11
                                                                                   Umemoto et al.: 3D Pose and Action Valuation in Football



off-ball indicator such as OBSO, analogous to that with xG        kept; a frame without the mid-hip joint is treated as a frame
for shots, would give them an external reference, provided        without pose. The pose of a 5 Hz step consists of the at most
the indicator is first shown to predict the outcomes in the       five 25 Hz frames of the step.
same data. Only the pose of the target player and a 0.2-             The hand-crafted representations use only the available
second window were used, and no correction for multiple           joints. For the raw representation, each joint is averaged over
comparisons was applied; such a correction could remove           the frames in which it is present. For the orientation features,
some of the three robust improvements of the action values        the torso orientation of a frame requires both shoulders, and
but not add new ones, so it would not weaken the conclusion       the head orientation is computed only in frames with a torso
that pose rarely improved them. Conversely, the absence           orientation and requires at least one of the eye and the ear
of a robust improvement does not show that pose has no            on each side, the left and right points being the mean of
effect: the confidence intervals in Fig. 2 bound the effects      the available eye and ear; each feature is averaged over the
compatible with the data, and an equivalence test with a          frames in which it can be computed. A joint or feature that is
margin of practical relevance would be needed to conclude         not available in any frame of the step is set to zero.
that an effect is negligible. Finally, only the values of the        The ST-GCN input Pt is a fixed 5 × 29 × 3 array without
observed actions were validated (Section III); the values of      a mask. A missing joint is set to zero, i.e., placed at the mid-
the actions that were not taken, which can fall far outside the   hip; a missing frame and a step without pose are set to zero
range of the returns (Fig. 3) [37], were not.                     in all joints. The padded steps of a batch are also zero. The
                                                                  encoder is applied to all steps of the batch, including padded
VIII. CONCLUSIONS                                                 steps, and the batch-normalisation statistics are computed
We examined whether adding 3D pose to a SARSA-based               over all of them; the losses and metrics use only the real steps.
MADRL action-valuation model brings the values of the
observed actions closer to the realised returns of the attacks,   APPENDIX B ST-GCN ENCODER
which are an observed goal or conceded goal and otherwise         A spatial-temporal graph convolutional network (ST-GCN)
the expected possession value at the end of the attack. Across    [20] processes a sequence of skeletons as a graph whose
six representations, three seeds and five learning settings,      vertices are the joints of every frame. Spatial edges connect
pose robustly brought these values closer to the returns in       the joints linked by a bone within a frame, and temporal
only three of 50 comparisons, all with torso and head orien-      edges connect the same joint in consecutive frames. A spatial
tation and in two of the five settings, and learned ST-GCN        graph convolution updates the features of each joint from
embeddings often made them worse. The learning setting of         those of its neighbours in the skeleton, and a temporal convo-
the prior model limited the values far more than the state        lution then mixes the features of each joint over neighbouring
did: its action-prediction loss lowered their validity also at    frames; stacking such blocks lets the features cover larger
matched training length. The same pose features, in contrast,     parts of the body and longer intervals, and pooling over the
improved the prediction of the on-ball action 0.2 s ahead,        joints and frames gives a fixed-length vector. Because the
and the pose of the passer at the pass, which can include the     weights are shared over the joints and frames and the graph
kick, was associated with pass success. For our data from one     follows the skeleton, the network can represent coordinated
competition and season, the representations and the training      movements of body parts with few parameters. The original
protocol examined, with a reward given only at the end of         ST-GCN for action recognition stacks nine blocks with up
an attack, the improvement of the action values by pose was       to 256 channels and a temporal kernel of nine frames, parti-
thus limited. We validated only the values of the observed        tions the neighbours of each joint into subsets with separate
actions, not the values of the actions that were not taken or     weights, learns weights for the edges, and is trained with
the choice of an optimal action. Future work should train         a classification loss on labelled movements. Our encoder is
action values with outcomes closer in time, such as pass          a lightweight variant for a window of only five frames: it
success, ball retention or changes in expected goals, select      has two blocks, one normalised adjacency matrix without
models on the value error, predict the actions with a separate    partitions or learned edge weights, and a temporal kernel of
output head instead of the values themselves, pretrain the        three frames, and it is trained only through the losses of the
pose encoder, include the poses of surrounding players, and       value model.
verify the results on other competitions.                            The skeleton graph has the 29 joints as vertices and 28
                                                                  bones as undirected edges: nose–neck, nose–eyes, eyes–ears,
APPENDIX A POSE INPUT AND MISSING JOINTS                          neck–mid-hip, neck–shoulders, shoulders–elbows, elbows–
The 29 joints are the nose, neck and mid-hip, the left and        wrists, wrists–thumbs and wrists–little fingers, mid-hip–hips,
right shoulders, elbows, wrists, hips, knees, ankles, eyes and    hips–knees, knees–ankles, ankles–heels, and heels–big toes
ears, the big toes, small toes and heels of both feet, and the    and heels–small toes, on both sides. With A the adja-
thumbs and little fingers of both hands. In preprocessing, the    cency matrix including self-loops and D its degree matrix,
coordinates of every joint in a frame are expressed relative to   the encoder uses the normalised adjacency matrix Â =
the mid-hip joint of the same frame and divided by 2.44 m on      D−1/2 AD−1/2 of graph convolutional networks [52]. For
all three axes, so the proportions and angles of the body are     an input X ∈ RC×5×29 (channels, frames, joints), a block
12                                                                                                                          VOLUME 4, 2016
Umemoto et al.: 3D Pose and Action Valuation in Football



computes                                                                            [9] P. Rahimian, J. Van Haaren, and L. Toka, “Towards maximizing expected
                                                                                       possession outcome in soccer,” International Journal of Sports Science &
           H = ReLU BN(Ws XÂ) ,                                            (5)         Coaching, p. 17479541231154494, 2023.
                                                                                  [10] G. Liu, Y. Luo, O. Schulte, and T. Kharrat, “Deep soccer analytics:
           Y = ReLU BN(Conv3×1 (H)) + R(X) ,                                (6)         learning an action-value function for evaluating soccer players,” Data
                                                                                        Mining and Knowledge Discovery, vol. 34, pp. 1531–1559, 2020.
where Ws is a 1×1 convolution over the channels, Conv3×1                           [11] H. Nakahara, K. Tsutsui, K. Takeda, and K. Fujii, “Action valuation of
is a convolution over three consecutive frames with zero                                on- and off-ball soccer players based on multi-agent deep reinforcement
padding that keeps the five frames, BN is batch normalisation                           learning,” IEEE Access, vol. 11, pp. 131 237–131 244, 2023.
[51], and R is a 1 × 1 convolution with batch normalisation                        [12] P. Rahimian, J. Van Haaren, T. Abzhanova, and L. Toka, “Beyond action
                                                                                        valuation: A deep reinforcement learning framework for optimizing player
when the number of channels changes and the identity other-                             decisions in soccer,” in 16th Annual MIT Sloan Sports Analytics Confer-
wise. The convolutions have no bias, and no dropout is used.                            ence. Boston, MA, USA: MIT, 2022, p. 25.
The first block maps 3 to 64 channels and the second 64 to                         [13] K. Ide, T. Someya, K. Kawaguchi, and K. Fujii, “Strategic multi-agent
                                                                                        learning for interpretable action valuation of all players in football,” arXiv
128, and the embedding gϕ (Pt ) ∈ R128 is the mean of the                               preprint arXiv:2610.05961, 2026.
output over the five frames and the 29 joints. The encoder                         [14] J. Bekkers, “Wide open gazes: Quantifying visual exploratory be-
has 79,360 parameters.                                                                  havior in soccer with pose enhanced positional data,” arXiv preprint
                                                                                        arXiv:2602.18519, 2026.
   The encoder is initialised with the default initialisation of
                                                                                   [15] G. d. S. Pinheiro, X. Jin, V. T. Da Costa, and M. Lames, “Body pose
PyTorch and trained jointly with the value model by the same                            estimation integrated with notational analysis: A new approach to analyze
optimiser, learning rate and weight decay (Section IV); it is                           penalty kicks strategy in elite football,” Frontiers in Sports and Active
not pretrained, and no loss acts on it other than the losses                            Living, vol. 4, p. 818556, 2022.
                                                                                   [16] M. Wear, R. Beal, T. Matthews, T. Norman, and S. Ramchurn, “Learn-
of the value model. Table 4 lists the number of trainable                               ing from the pros: Extracting professional goalkeeper technique from
parameters of each condition.                                                           broadcast footage,” in MIT Sloan Sports Analytics Conference, 2022,
                                                                                        arXiv:2202.12259.
TABLE 4. Input dimension and number of trainable parameters of the                 [17] Y. Xu, L. Bretzner, T. Wang, and A. Maki, “Skor-xG: Skeleton-oriented
action-value model for each pose condition (input layer, GRU and output layer           expected goal estimation in soccer,” in Proceedings of the IEEE/CVF Con-
with 16 units for the 15 actions and the padding class, plus the ST-GCN                 ference on Computer Vision and Pattern Recognition (CVPR) Workshops,
encoder where used).                                                                    2025.
                                                                                   [18] C. Yeung, K. Ide, and K. Fujii, “AutoSoccerPose: Automated 3D posture
                 Condition          Input dim.       Parameters                         analysis of soccer shot movements,” in Proceedings of the IEEE/CVF Con-
                 none                       92           31,952                         ference on Computer Vision and Pattern Recognition (CVPR) Workshops,
                 raw                       179           37,520                         2024.
                 torso                      98           32,336                    [19] B. Liu and K. Fujii, “Data-driven pose-aware team-space evaluation in
                 torso+head                106           32,848                         soccer with 3D body orientation,” in International Conference on Sport
                 ST-GCN                    220          119,504                         Sciences Research and Technology Support (icSPORTS), 2026.
                 ST-GCN+torso              226          119,888                    [20] S. Yan, Y. Xiong, and D. Lin, “Spatial temporal graph convolutional
                                                                                        networks for skeleton-based action recognition,” in Proceedings of the
                                                                                        AAAI Conference on Artificial Intelligence, vol. 32, no. 1, 2018.
                                                                                   [21] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction,
REFERENCES                                                                              2nd ed. MIT Press, 2018.
 [1] T. Decroos, L. Bransen, J. Van Haaren, and J. Davis, “Actions speak louder    [22] J. Fernández, L. Bornn, and D. Cervone, “A framework for the fine-grained
     than goals: Valuing player actions in soccer,” in Proceedings of the 25th          evaluation of the instantaneous expected value of soccer possessions,”
     ACM SIGKDD international conference on knowledge discovery & data                  Machine Learning, vol. 110, no. 6, pp. 1389–1427, 2021.
     mining, 2019, pp. 1851–1861.                                                  [23] G. Liu and O. Schulte, “Deep reinforcement learning in ice hockey for
 [2] K. Toda, M. Teranishi, K. Kushiro, and K. Fujii, “Evaluation of soccer             context-aware player evaluation,” arXiv preprint arXiv:1805.11088, 2018.
     team defense based on prediction models of ball recovery and being            [24] K. Ide, T. Someya, K. Kawaguchi, and K. Fujii, “Expandable decision-
     attacked: A pilot study,” Plos one, vol. 17, no. 1, p. e0263051, 2022.             making states for multi-agent deep reinforcement learning in soccer tacti-
 [3] R. Umemoto, K. Tsutsui, and K. Fujii, “A generalized valuation method              cal analysis,” Journal of Big Data, 2026.
     for team defense by estimating probabilities in football games,” in Pro-
                                                                                   [25] Y. Pan, Z. Pu, M. Chen, W. Ren, Y. Li, and Z. Ming, “Offline multi-agent
     ceedings of the 13th International Conference on Sport Sciences Research
                                                                                        reinforcement learning for evaluating and optimizing football attacking
     and Technology Support (icSPORTS), vol. 1. SCITEPRESS, 2025, pp.
                                                                                        strategies against low-block defences,” Intelligent Sports and Health,
     79–89.
                                                                                        vol. 2, no. 2, pp. 74–87, 2026.
 [4] I. Simpson, R. J. Beal, D. Locke, and T. J. Norman, “Seq2event: Learning
                                                                                   [26] S. Groom, M. Groom, F. Belo, A. Rice, L. Anderson, V.-A. Darvariu, and
     the language of soccer using transformer-based match event prediction,”
                                                                                        S. Wang, “Maximising the set-piece return: Optimising football corner tac-
     in Proceedings of the 28th ACM SIGKDD Conference on Knowledge
                                                                                        tics with graph reinforcement learning,” arXiv preprint arXiv:2606.06353,
     Discovery and Data Mining, 2022, pp. 3898–3908.
                                                                                        2026.
 [5] C. Yeung, R. Bunker, and K. Fujii, “Unveiling multi-agent strategies: A
     data-driven approach for extracting and evaluating team tactics from foot-    [27] M. Van Roy, P. Robberechts, T. Decroos, and J. Davis, “Valuing on-the-
     ball event and freeze-frame data,” Journal of Robotics and Mechatronics,           ball actions in soccer: A critical comparison of xT and VAEP,” in AAAI-20
     vol. 36, no. 3, pp. 603–617, 2024.                                                 Workshop on Artificial Intelligence in Team Sports, 2020.
 [6] G. Anzer, P. Bauer, U. Brefeld, and D. Fassmeyer, “Detection of tactical      [28] W. Spearman, “Beyond expected goals,” in Proceedings of the 12th MIT
     patterns using semi-supervised graph neural networks,” in MIT Sloan                sloan sports analytics conference, 2018, pp. 1–17.
     Sports Analytics Conference, 2022.                                            [29] M. Teranishi, K. Tsutsui, K. Takeda, and K. Fujii, “Evaluation of creating
 [7] P. Rahimian and L. Toka, “Inferring the strategy of offensive and defensive        scoring opportunities for teammates in soccer via trajectory prediction,” in
     play in soccer with inverse reinforcement learning,” in Machine Learning           Machine Learning and Data Mining for Sports Analytics: 9th International
     and Data Mining for Sports Analytics (MLSA 2021), ser. Communications              Workshop, MLSA 2022, Grenoble, France, September 19, 2022, Revised
     in Computer and Information Science. Springer, 2022.                               Selected Papers. Springer, 2023, pp. 53–73.
 [8] J. Fernández, L. Bornn, and D. Cervone, “Decomposing the immeasurable         [30] P. Henderson, R. Islam, P. Bachman, J. Pineau, D. Precup, and D. Meger,
     sport: A deep learning expected possession value framework for soccer,”            “Deep reinforcement learning that matters,” in Proceedings of the AAAI
     in MIT Sloan Sports Analytics Conference, 2019.                                    Conference on Artificial Intelligence, vol. 32, no. 1, 2018.

VOLUME 4, 2016                                                                                                                                                     13
                                                                                                         Umemoto et al.: 3D Pose and Action Valuation in Football



[31] R. Agarwal, M. Schwarzer, P. S. Castro, A. Courville, and M. G. Belle-          [52] T. N. Kipf and M. Welling, “Semi-supervised classification with graph
     mare, “Deep reinforcement learning at the edge of the statistical precipice,”        convolutional networks,” in Proceedings of the 5th International Confer-
     in Advances in Neural Information Processing Systems, vol. 34, 2021.                 ence on Learning Representations (ICLR), 2017.
[32] M. Gutiérrez-Pérez, C. Yeung, K. Fujii, and A. Agudo, “Once upon a goal:
     Towards orientation-based shot metrics in football,” Computer Vision and
     Image Understanding, p. 104732, 2026.
[33] W. Spearman, A. Basye, G. Dick, R. Hotovy, and P. Pop, “Physics-based
     modeling of pass probabilities in soccer,” in Proceeding of the 11th MIT
     Sloan Sports Analytics Conference, 2017.
[34] P. Power, H. Ruiz, X. Wei, and P. Lucey, “Not all passes are created                                      RIKUHEI UMEMOTO received his B.E. degree
     equal: Objectively measuring the risk and reward of passes in soccer from                                 from Kyoto University, Kyoto, Japan, in 2022.
     tracking data,” in Proceedings of the 23rd ACM SIGKDD international                                       He also received his M.S. degree from Nagoya
     conference on knowledge discovery and data mining, 2017, pp. 1605–                                        University, Nagoya, Japan. His research interests
     1613.                                                                                                     include data analysis with computer vision and
[35] A. Arbués-Sangüesa, A. Martín, J. Fernández, C. Ballester, and G. Haro,                                   reinforcement learning in team sports such as foot-
     “Using player’s body-orientation to model pass feasibility in soccer,” in                                 ball.
     Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
     Recognition (CVPR) Workshops, 2020.
[36] C. Yeung, K. Ide, T. Someya, and K. Fujii, “OpenSTARLab: Open
     approach for spatio-temporal agent data analysis in soccer,” Complex &
     Intelligent Systems, vol. 11, 2025, art. no. 342.
[37] S. Fujimoto, D. Meger, and D. Precup, “Off-policy deep reinforcement
     learning without exploration,” in Proceedings of the 36th International
     Conference on Machine Learning, ser. Proceedings of Machine Learning
     Research, vol. 97, 2019, pp. 2052–2062.                                                                   KENJIRO IDE received his B.S. and M.S. de-
[38] K. Cho, B. van Merriënboer, C. Gulcehre, D. Bahdanau, F. Bougares,                                        grees from Nagoya University in 2024 and 2026,
     H. Schwenk, and Y. Bengio, “Learning phrase representations using RNN                                     respectively. His research interests are multi-agent
     encoder–decoder for statistical machine translation,” in Proceedings of the                               reinforcement learning and generative modeling
     2014 Conference on Empirical Methods in Natural Language Processing                                       for understanding and evaluating decision-making
     (EMNLP), 2014, pp. 1724–1734.                                                                             in team sports, particularly football.
[39] G. A. Rummery and M. Niranjan, “On-line Q-learning using connection-
     ist systems,” Cambridge University Engineering Department, Tech. Rep.
     CUED/F-INFENG/TR 166, 1994.
[40] K. Fujii, K. Tsutsui, A. Scott, H. Nakahara, N. Takeishi, and Y. Kawahara,
     “Adaptive action supervision in reinforcement learning from real-world
     multi-agent demonstrations,” International Conference on Agents and
     Artificial Intelligence (ICAART 2024), vol. 2, pp. 27–39, 2024.
[41] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” in
     International Conference on Learning Representations (ICLR), 2015.
[42] S. Fujimoto, D. Meger, D. Precup, O. Nachum, and S. S. Gu, “Why should                                    SOHAM MAJUMDER received his B.E. degree
     I trust you, Bellman? The Bellman error is a poor replacement for value                                   from St. Xavier’s College, Kolkata, India, in 2022.
     error,” in Proceedings of the 39th International Conference on Machine                                    He also received his M.S. degree from the In-
     Learning, ser. Proceedings of Machine Learning Research, vol. 162, 2022,                                  dian Statistical Institute, India, in 2023. His re-
     pp. 6918–6943.                                                                                            search interests include spatiotemporal data anal-
[43] J. H. Friedman, “Greedy function approximation: A gradient boosting                                       ysis, explainable machine learning, graph neural
     machine,” Annals of Statistics, vol. 29, no. 5, pp. 1189–1232, 2001.                                      networks, and their applications to football analyt-
[44] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel,                                ics.
     M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg et al., “Scikit-learn:
     Machine learning in Python,” Journal of Machine Learning Research,
     vol. 12, pp. 2825–2830, 2011.
[45] H. Kim, H. Choi, S. Seo, T. Boomstra, J. Yoon, and C. Park, “ELASTIC:
     Event-tracking data synchronization in soccer without annotated event
     locations,” in ECML PKDD Workshop on Machine Learning and Data
     Mining for Sports Analytics (MLSA), 2025, arXiv:2508.09238.
[46] B. Efron and R. J. Tibshirani, An Introduction to the Bootstrap. Chapman                                   ULF BREFELD received his Diploma degree in
     & Hall, 1993.                                                                                              Computer Science from Technische Universität
[47] H. Eggels, R. van Elk, and M. Pechenizkiy, “Expected goals in soccer:                                      Berlin, Germany, in 2003 and his Ph.D. degree
     Explaining match results using predictive analytics,” in The machine                                       from Humboldt-Universität zu Berlin, Germany,
     learning and data mining for sports analytics workshop, vol. 16, 2016.                                     in 2008. He previously worked on machine learn-
[48] B. W. Matthews, “Comparison of the predicted and observed secondary                                        ing at several academic and industrial research
     structure of T4 phage lysozyme,” Biochimica et Biophysica Acta (BBA) –                                     institutions, including Universität Bonn, Yahoo!
     Protein Structure, vol. 405, no. 2, pp. 442–451, 1975.                                                     Research Barcelona, and the Max Planck Institute
[49] M. Jaderberg, V. Mnih, W. M. Czarnecki, T. Schaul, J. Z. Leibo, D. Sil-                                    for Computer Science. He also led the Recom-
     ver, and K. Kavukcuoglu, “Reinforcement learning with unsupervised                                         mender Systems group at Zalando SE and served
     auxiliary tasks,” in International Conference on Learning Representations       as a joint professor of Knowledge Mining and Assessment at TU Darmstadt
     (ICLR), 2017.                                                                   and the Leibniz Institute for Research and Information in Education (DIPF).
[50] G. Alain and Y. Bengio, “Understanding intermediate layers using linear         He is currently a professor of Machine Learning at Leuphana Universität
     classifier probes,” arXiv preprint arXiv:1610.01644, 2016.                      Lüneburg, Germany. His research interests are statistical machine learning,
[51] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep network        data mining, spatiotemporal data analysis, recommender systems, and sports
     training by reducing internal covariate shift,” in Proceedings of the 32nd      analytics.
     International Conference on Machine Learning, ser. Proceedings of Ma-
     chine Learning Research, vol. 37, 2015, pp. 448–456.

14                                                                                                                                                 VOLUME 4, 2016
Umemoto et al.: 3D Pose and Action Valuation in Football



                          KEISUKE FUJII received his B.S., M.S., and
                          Ph.D. degrees from Kyoto University in 2009,
                          2011, and 2014, respectively. After his work as
                          a postdoctoral fellow and research scientist at
                          Nagoya University and RIKEN Center for Ad-
                          vanced Intelligence Project in Japan, he joined
                          Nagoya University. He is currently a professor at
                          the Information Technology Center and Graduate
                          School of Informatics. His research interests are
                          interdisciplinary studies among machine learning,
behavioral sciences, and sports sciences.




VOLUME 4, 2016                                                                15
