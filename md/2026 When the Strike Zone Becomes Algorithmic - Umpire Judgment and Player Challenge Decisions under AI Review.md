<!-- source: 2026 When the Strike Zone Becomes Algorithmic - Umpire Judgment and Player Challenge Decisions under AI Review.pdf -->

# When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review

- arXiv: https://arxiv.org/abs/2609.25525 (2026-09-22, cs.HC)
- Authors: Kichang Lee, Gyeongmin Han, Sungmin Lee, JeongGil Ko et al.
- Triage: N6/P7/R9 = 22/30 | data: public | code: no

## Abstract

The Automated Ball-Strike challenge system that Major League Baseball adopted in 2026 offers a distinctive setting for studying human AI interaction in which umpires make every ball and strike call, while players can selectively ask an automated system to publicly overturn those decisions. We analyze 4,114,256 called pitches from 2015 through 2026 and 8,447 challenges from the 2026 season to examine how algorithmic review reshapes umpire judgment and player behavior. We study where umpires placed the effective strike zone boundary, how consistently they applied that boundary, how they responded to overturned calls, and which calls players chose to challenge. In 2026, the effective called boundary shifted toward the automated strike zone beyond the trajectory observed in prior seasons, while the consistency of that boundary largely continued its existing trend. Following an overturned call, umpires temporarily adjusted subsequent decisions near the corrected boundary, although these effects did not consistently persist into the next game. Count dependent variation in calling remained, while differences associated with player status narrowed. Players, meanwhile, left many overturnable calls unchallenged and appeared to base challenge decisions more strongly on immediately observable evidence than on the precise geometry of the automated zone. Together, these findings show that selective AI review does more than correct individual errors. It reshapes human judgment, adaptation, and strategic behavior around an algorithmic authority.

## Full text (pdftotext extraction)

```text
                                         When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player
                                         Challenge Decisions under AI Review

                                         KICHANG LEE∗ , KAIST, Republic of Korea and Yonsei University, Republic of Korea
                                         GYEONGMIN HAN∗ , Yonsei University, Republic of Korea
                                         SUNGMIN LEE, KAIST, Republic of Korea and Yonsei University, Republic of Korea
                                         JEONGGIL KO† , Yonsei University, Republic of Korea
                                         The Automated Ball-Strike challenge system that Major League Baseball adopted in 2026 offers a distinctive setting for studying human
                                         AI interaction in which umpires make every ball and strike call, while players can selectively ask an automated system to publicly
arXiv:2609.25525v1 [cs.HC] 22 Sep 2026




                                         overturn those decisions. We analyze 4,114,256 called pitches from 2015 through 2026 and 8,447 challenges from the 2026 season to
                                         examine how algorithmic review reshapes umpire judgment and player behavior. We study where umpires placed the effective strike
                                         zone boundary, how consistently they applied that boundary, how they responded to overturned calls, and which calls players chose
                                         to challenge. In 2026, the effective called boundary shifted toward the automated strike zone beyond the trajectory observed in prior
                                         seasons, while the consistency of that boundary largely continued its existing trend. Following an overturned call, umpires temporarily
                                         adjusted subsequent decisions near the corrected boundary, although these effects did not consistently persist into the next game.
                                         Count dependent variation in calling remained, while differences associated with player status narrowed. Players, meanwhile, left
                                         many overturnable calls unchallenged and appeared to base challenge decisions more strongly on immediately observable evidence
                                         than on the precise geometry of the automated zone. Together, these findings show that selective AI review does more than correct
                                         individual errors. It reshapes human judgment, adaptation, and strategic behavior around an algorithmic authority.

                                         CCS Concepts: • Human-centered computing → Human computer interaction (HCI).

                                         Additional Key Words and Phrases: AI oversight, human-AI interaction, expert decision making, signal detection theory, perceptual
                                         learning, sports officiating


                                         1   Introduction
                                         For more than a century, ball-strike calls in baseball relied almost entirely on human umpires’ judgment. The introduction
                                         of the Automated Ball-Strike system (ABS) has begun to change this practice. In 2024, the Korea Baseball Organization
                                         (KBO) introduced ABS to automate ball-strike calls throughout the league[33]. Major League Baseball (MLB), in
                                         contrast, adopted a challenge-based ABS in 2026. The home-plate umpire makes the initial call, but a batter, pitcher, or
                                         catcher may immediately challenge it. ABS then uses camera-based pitch tracking to uphold or overturn the call. This
                                         arrangement preserves human responsibility for the initial judgment while giving an automated system final authority
                                         over challenged decisions.
                                             From a human-computer interaction (HCI) perspective, this arrangement raises a question about how automated
                                         review shapes human judgment [10, 32, 39, 44]. Prior research has examined systems that advise humans while leaving
                                         the final decision to them [3, 20, 31, 37, 46], as well as algorithmic management systems that assign tasks and evaluate
                                         workers’ performance [27, 28, 36, 52, 54]. Challenge-based ABS, however, introduces a distinctive setting in which one
                                         person makes a decision, another chooses whether to contest it, and a system delivers a binding ruling. Understanding
                                         ∗ These authors contributed equally to this work.
                                         † Corresponding author.


                                         Authors’ Contact Information: Kichang Lee, kichang.lee@kaist.ac.kr, KAIST, Daejeon, Republic of Korea and Yonsei University, Seoul, Republic of Korea;
                                         Gyeongmin Han, sd061123@yonsei.ac.kr, Yonsei University, Seoul, Republic of Korea; Sungmin Lee, i.am.sungmin.lee@kaist.ac.kr, KAIST, Daejeon,
                                         Republic of Korea and Yonsei University, Seoul, Republic of Korea; JeongGil Ko, jeonggil.ko@yonsei.ac.kr, Yonsei University, Seoul, Republic of Korea.
                                         Manuscript submitted to ACM                                                                                                                         1
2                                                                                                                           Lee et al.




Fig. 1. Overview of the MLB ABS challenge procedure. (a) The umpire makes the initial call; (b) the pitcher, catcher, or batter may
challenge it; (c) ABS publicly displays the measured pitch location; and (d) the call is upheld or overturned. The lower schematic
highlights the resulting asymmetry: umpires judge every pitch but receive correction only for challenged calls, while players determine
which calls receive review.



this interaction requires examining both how decision-makers respond to automated review and how the people entitled
to request that review exercise their authority.
    Automated review may influence umpire judgment in two ways: (i) through the possibility of review before a
challenge is made and (ii) through the corrective feedback that follows an overturned call. These effects may change
how willing an umpire is to call a strike or how accurately the umpire separates pitches near the zone boundary.
Signal detection theory provides a framework for separating shifts in decision criterion from changes in perceptual
sensitivity [18, 23]. Corrective feedback may also lead to immediate conscious adjustments or, through repeated
exposure, gradual perceptual recalibration [51, 62, 65]. We therefore examine changes associated with the availability
of automated review together with changes after individual overturns, without assuming that either pathway affects
only criterion or sensitivity.
    Figure 1 summarizes how an ABS challenge proceeds. Figure 1 (a) shows the umpire making the initial ball-strike
call, after which the pitcher, catcher, or batter may contest it by tapping their helmet (see Figure 1 (b)). ABS then
displays the measured pitch location (see Figure 1 (c)) and either upholds or overturns the call (c.f., Figure 1 (d)). This
workflow creates two features central to our analysis. First, feedback is public and explicit: an overturn directly reveals
a discrepancy between the umpire’s judgment and the system’s ruling to the umpire, players, and spectators. Second,
review is selective: each team begins with two challenges and retains a challenge when successful, so players determine
which eligible calls receive review. As summarized by the lower schematic, umpires judge every pitch but receive
explicit correction only for calls that players choose to challenge. Across the 1,974 games played from Opening Day
through August 24, 2026, players initiated 8,447 challenges (4.28 per game), with at least one challenge in 98.7% of
games; 4,525 (53.6%) were overturned.
    Prior research has studied systematic errors and contextual biases in human ball-strike judgments [9, 25, 26, 35, 40, 67],
including associations with pitcher status [29, 42, 59], the count [57], and race [22, 45, 61]. Such patterns raise a distinction
Manuscript submitted to ACM
When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review                   3


between perceptual limitations and the criteria used to translate perception into a call. Flannagan et al. [13] reported
improvements in umpires’ perceptual precision across seasons alongside persistent biases, suggesting that greater
precision need not eliminate systematic decision tendencies. Evidence from tennis further suggests that automated
review can accompany changes in officials’ decision tendencies. Almog et al. [2] reported a shift toward calling balls in
after the introduction of Hawk-Eye.
  Taken together, however, prior work leaves several questions about challenge-based review unresolved. Baseball
studies have documented broad patterns in umpire calls, and research on automated review has shown that judgments
can change after such systems are introduced. These findings do not show how umpires respond to a specific overturn
or whether any resulting adjustment persists beyond the immediate call. At the same time, studies of challenge behavior
have generally treated the decision to request review as a separate problem, rather than as part of a feedback process that
also involves the original decision-maker. Challenge-based ABS brings these elements together, allowing us to examine
broader changes in umpire judgment, responses to individual overturns, and the calls players choose to challenge
within the same system.
  We investigate these questions using twelve seasons of MLB data from 2015 through 2026, comprising 4,114,256
regular-season called pitches from 141 home-plate umpires and 8,447 challenge events recorded in 2026. Crucially,
changes in 2026 must be interpreted with caution, since the introduction of challenge-based ABS also brought a new
operational definition of the strike zone. A change in umpire calling patterns could therefore be associated with the
new review system, the change in the zone used to evaluate pitches, or both.
  To keep the change in strike-zone definition from being mistaken for a change in umpire judgment, we place all
twelve seasons on the same spatial reference. We define a fixed reference zone based on batter height, independently
of observed umpire calls, and account separately for how the strike zone used in each era differs from that reference.
On this common scale, we estimate where umpires tend to switch from ball to strike at each edge of the zone and
how sharply that switch occurs. These measures capture changes in strike-calling tendency and response precision,
which we interpret in relation to decision criterion and sensitivity under our response model. We use them to examine
both broader changes across seasons and changes following individual overturns, while analyzing players’ challenge
decisions separately.
  Specifically, we focus on and address three research questions (RQ):


RQ1. How do umpires’ judgments change after an individual overturn, in which direction and at which zone boundaries,
       and do these changes persist into the next game?
RQ2. How do decision criteria, sensitivity, and condition-specific biases differ before and after the introduction of
       challenge-based ABS?
RQ3. Which characteristics of a pitch and its game context are associated with players’ decisions to challenge a call?


  These questions frame challenge-based ABS as a system in which umpire judgment, automated feedback, and players’
use of review are closely connected. By comparing broader changes across seasons with responses following individual
overturns, we characterize how umpire calls vary under automated review across different timescales. From another
perspective, we examine which calls players choose to challenge, since those choices determine when automated
review and corrective feedback occur. Viewed together, these analyses show why understanding challenge-based review
requires considering both how umpires respond to automated rulings and how players decide when to invoke them.

                                                                                                  Manuscript submitted to ACM
4                                                                                                                    Lee et al.


2     Background and Related Work
2.1    The ABS Challenge System
Understanding the Automated Ball-Strike System (ABS) first requires understanding how ball-strike calls shape play.
When a batter does not swing at a pitch, the home-plate umpire calls it a strike or a ball based on whether it passes
through the strike zone. Each call updates the count, which records the number of balls and strikes accumulated during
the current plate appearance. A fourth ball awards the batter first base, whereas a third strike results in a strikeout. A call
therefore affects either the outcome of the plate appearance or the count under which play continues. The traditional
rulebook defines the strike zone as a three-dimensional region above home plate, with vertical boundaries determined
by the batter’s stance. However, as Wang et al. [64] explain, the written definition, umpires’ calling practices, and
technological representations of the zone have not always aligned.
    MLB introduced challenge-based ABS in the 2026 season. Under this system, the umpire makes the initial call, and
only the batter, pitcher, or catcher involved in the pitch may request review. Each team starts with two challenges
and retains a challenge when it succeeds while losing one after an unsuccessful attempt. A team that enters an extra
inning without a remaining challenge receives one. As illustrated in Figure 1, a player must request review immediately
after the call. The system then displays its ruling publicly before the call is upheld or overturned [64]. As a result, a
successful challenge changes the ruling while preserving the team’s opportunity to request another review.
    ABS applies a specific operational definition of the strike zone. Its zone is a 17-inch-wide rectangle at the midpoint
of home plate, with its lower and upper boundaries set at 27% and 53.5% of the batter’s measured standing height,
respectively. Wang et al. [64] trace how this implementation emerged through seven years of experimentation. Their
study shows that both the geometry of the zone and the choice to use challenges were shaped by technical feasibility,
economic considerations, continuity with established calling practices, and the preservation of gamesmanship. In
particular, the challenge format preserves opportunities for players to influence and contest human judgments while
making the decision to invoke automated review part of the game itself.
    This arrangement distributes authority across three roles. The umpire makes the initial judgment, an eligible player
decides whether to challenge it, and ABS determines the binding outcome of the review. Technological evaluation
of umpires predates ABS through camera-based monitoring and public analyses of pitch-tracking data [4, 26, 43, 64].
Challenge-based ABS adds immediate, player-initiated review that can reverse a call during the game. Umpire judgments
are therefore subject to public correction, while whether that correction occurs depends on players’ decisions to
challenge.



2.2    Automated Review and Human Authority
Research on AI-assisted decision-making has examined how people accept or reject algorithmic advice [11, 17, 47, 68, 69].
Bansal et al. [3] found that explanations increased acceptance of AI recommendations regardless of their correctness,
without further improving complementary team performance. Buccinca et al. [5] showed that interventions encouraging
deliberate engagement reduced overreliance compared with explanation-based interfaces. Together, these findings show
that people’s responses to AI depend partly on how they engage with algorithmic recommendations. Challenge-based
ABS expands this into a distinctive settings where automated review can overturn the human decision rather than merely
inform it. This shift in authority raises a related question about how people exercise judgment when an automated
system can issue the final ruling.

Manuscript submitted to ACM
When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review                      5


   Research on evaluation and accountability helps explain why such authority may influence judgment [14, 21, 49, 50].
Rahman [48] found that workers responded to opaque algorithmic evaluations by experimenting with ways to improve
their scores or by restricting their platform activity. Their behavior changed even when the criteria behind the evaluation
were difficult to understand. Lerner and Tetlock [38] likewise show that accountability can reduce or amplify biases
depending on the conditions under which people expect to justify their decisions. These findings motivate examining
how judgment changes under evaluative authority without assuming that evaluation necessarily improves it.
   Sports officiating provides evidence of these responses under technological monitoring and review. Bradbury [4]
examined QuesTec monitoring in baseball, finding some evidence of reduced shirking while emphasizing umpires’
responsiveness to existing league directives. Studies of VAR in football similarly report partial reductions in home
bias rather than its elimination [6, 15, 24]. These findings establish that technological oversight can accompany
uneven changes in officiating, although monitoring and human-led video review differ from systems that issue binding
automated rulings.
   Hawk-Eye in tennis provides a closer example of this form of review. More directly, Almog et al. [2] found that
Hawk-Eye review in tennis reduced overall errors on close calls while shifting judgments toward calling balls in. Their
structural model interprets this shift in terms of the psychological cost of being overruled. The findings show that
improved aggregate accuracy can coexist with a change in the kinds of errors officials make. They therefore motivate
examining not only whether judgment becomes more accurate under automated review but also how calling patterns
change.
   Within baseball, Wang et al. [64] explain how ABS emerged through negotiations over technological rule enforcement,
preserving human participation while granting the system final authority over challenged calls. Their account of
the system’s design complements the behavioral evidence from other sports. Together, these perspectives motivate
examining broader patterns in umpire judgment, responses following individual overturns, and the conditions under
which players request review. This allows automated review to be studied through both the judgments subject to it and
the human choices that determine when it occurs.

2.3   Umpire Judgment: Bias, Feedback, and Measurement
Umpires are directly exposed to automated review given that their judgments are the decisions being evaluated and
potentially overturned. Understanding their responses requires examining both the factors that shape their calls and
the forms of change that may follow the corrective feedback. Prior research shows that ball-strike judgments depend
on more than pitch location [7, 25, 34, 40, 42, 61]. Green and Daniels [19] documented count-dependent variation in
the called strike zone, while Kim and King [29] identified an association between pitcher status and favorable calls.
Deshpande and Wyner [9] examined catcher framing, through which the presentation of a pitch influences its evaluation.
These findings establish that the observed strike zone reflects contextual influences as well as the physical location of
the ball.
   Signal detection theory provides a framework for distinguishing two aspects of such judgments: (i) sensitivity, the
ability to distinguish between alternatives, and (ii) criterion, the threshold used to select a response under uncertainty [18,
23]. An umpire may become less willing to call a borderline pitch a strike without becoming better at distinguishing
pitches inside and outside the zone. Conversely, improved discrimination need not eliminate a systematic tendency to
favor one response. Flannagan et al. [13] illustrate this distinction by reporting improvements in perceptual precision
across seasons alongside persistent biases. Their findings motivate examining the location and precision of the decision
boundary separately, rather than treating changes in aggregate accuracy as a complete description of umpire behavior.
                                                                                                     Manuscript submitted to ACM
6                                                                                                               Lee et al.


    Corrective feedback introduces a further question: how does a particular overturn relate to subsequent judgments?
Perceptual learning research describes how experience can alter the processing and differentiation of task-relevant
information [12, 51, 53, 55, 65]. Related work on sensorimotor adaptation distinguishes explicit adjustments from
implicit learning [62] and identifies adaptation processes operating at different rates [58]. These accounts motivate
examining the time course and generalization of responses to correction. In baseball, a response may be concentrated
near the corrected boundary, extend to other boundaries, or persist into later games. Such patterns provide evidence
about the scope and duration of adjustment, although they do not uniquely identify an underlying cognitive mechanism.
    Observing these changes requires an interpretable representation of the called strike zone. Existing approaches
include geometric measures of accuracy and consistency [26], hierarchical models of contextual influences [9], and
psychophysical models that distinguish boundary location from the width of the transition between ball and strike
responses [13]. Boundary location describes where the response changes, whereas transition width describes how
gradually it changes with pitch position. Under the assumptions of the response model, these quantities support
interpretations in terms of criterion and sensitivity. Longitudinal comparisons must additionally account for differences
in the reference zone: Wang et al. [64] show that the rulebook definition, established calling practices, and the zone
implemented by ABS are not interchangeable. This distinction motivates using a common spatial reference across our
twelve-season dataset while accounting separately for era-specific zone definitions.




2.4   Player Decisions to Challenge
Players determine when automated review is invoked and, consequently, which umpire judgments receive public
confirmation or correction. A challenge decision involves both uncertainty about the call and the value of requesting
review in the current game situation [16, 63]. Disagreement with the umpire may favor a challenge, but the possibility
of losing a remaining opportunity for review may favor restraint. Understanding challenge behavior therefore requires
considering perceptual judgment alongside the incentives created by the review procedure.
    Research in tennis demonstrates the relevance of both factors. Mather [41] analyzed line-call challenges using a
psychophysical model of uncertainty in players’ and officials’ judgments. The model accounted for the concentration
of challenges and errors near court boundaries, showing how perceptual uncertainty can explain observed challenge
patterns. From a decision-theoretic perspective, Abramitzky et al. [1] modeled challenges as a trade-off between the
immediate benefit of overturning a call and the value of retaining opportunities for later use. They found that players’
behavior was close to the optimal strategy prescribed by their model. Together, these studies suggest that challenge
decisions reflect both whether a player believes a call is incorrect and whether contesting it is worthwhile.
    In baseball, Wang et al. [64] identify selective enforcement as a design choice that preserves gamesmanship and
makes the use of automation part of player strategy. This perspective motivates examining how challenge requests
vary with pitch characteristics, the count, and the broader game context. However, an unchallenged call does not
reveal whether the player accepted the ruling, failed to recognize a discrepancy, or deliberately preserved a challenge.
Similarly, the pitch location measured by ABS does not directly reveal what the player perceived. We therefore examine
observable conditions associated with review requests without treating challenge rates alone as evidence of perceptual
ability or strategic intent. These choices also define the set of calls on which umpires receive automated feedback,
connecting players’ use of the system to the study of umpire responses.

Manuscript submitted to ACM
When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review                   7


2.5    Positioning the Present Study
Prior research has examined technological officiating as a broader class of decision-aid systems, including questions of
authority, accuracy, and standards of review [8, 30], and documented how technological monitoring and review alter
officials’ decisions in baseball, football, and tennis [2, 4, 6, 24, 43, 60] and modeled challenge behavior as a combination
of perceptual uncertainty and the strategic use of limited review opportunities [1, 41, 66]. In MLB specifically, recent
work has traced how ABS developed from a technological aid into a system of selective, binding rule enforcement,
showing that the operational strike zone reflects design choices rather than a straightforward translation of the written
rule [64].
    Our study brings these perspectives together in MLB’s challenge-based ABS by examining umpire judgments and
players’ requests for review within the same setting. Using twelve seasons of pitch data and challenge records from 2026,
we characterize longer-term judgment patterns, the spatial specificity and persistence of changes following overturns,
and the conditions associated with challenge requests. Building on psychophysical approaches that model the called
strike zone in terms of boundary location and response precision [13], we use a common spatial reference to compare
judgments across seasons while separately accounting for changes in the operational definition of the zone [64]. This
approach examines both how judgments vary under automated review and how participants selectively invoke that
review, without assuming that observed behavioral patterns uniquely identify cognitive mechanisms or strategic intent.


3     Data and Measurement Framework
3.1    Dataset Construction and Measurement Harmonization

Sample construction. Our dataset draws on MLB pitch-tracking data from Baseball Savant covering twelve regular
seasons from 2015 through 2026, with the 2026 data available through August 24. The analysis is restricted to balls
and called strikes to focus on pitches that require a ball-strike decision by the home-plate umpire. Extra innings are
excluded to keep the number of available challenge opportunities comparable across games, as MLB provides each team
with an additional challenge in every extra inning. For each pitch, the dataset includes its tracked location, strike-zone
boundaries, home-plate umpire, batter, and ball-strike count. After applying these criteria, the final sample contains
4,114,256 called pitches, including 8,283 challenged pitches, adjudicated by 141 home-plate umpires. We note that before
comparing these pitches across seasons two changes in the 2026 data must be addressed.
Original umpire calls. The first change concerns the recorded outcome of challenged pitches. In 2026, this outcome
reflects the final ruling after ABS review and may differ from the umpire’s original call. For each overturned challenge,
the recorded outcome is reversed to recover the call initially made by the umpire. We denote this original call by 𝑦𝑖 ,
where 𝑦𝑖 = 1 indicates a called strike and 𝑦𝑖 = 0 indicates a called ball.
Common measurement plane. The second change concerns where pitch location is measured. Through 2025, pitch
coordinates were reported at the front plane of home plate, whereas the 2026 season coordinates are reported at the
midpoint plane used by ABS. As a result, the same pitch would have different reported coordinates depending on
which plane is used for measurement. The size and direction of this difference depend on the trajectory of the pitch.
Consequently, comparing the reported coordinates directly could make a change in measurement convention appear as
a change in umpire judgment.
    To make the coordinates comparable across seasons, we reconstruct each pre-2026 season pitch at the midpoint plane
of home plate. For each pitch, velocity and acceleration parameters from the tracking data are used to determine when
                                                                                                  Manuscript submitted to ACM
8                                                                                                                                    Lee et al.


it reaches the front and midpoint planes. Propagating its trajectory between these two points yields the horizontal
and vertical coordinates at the midpoint. Coordinates from 2026 are already reported at this plane and require no
reconstruction. This procedure places pitch locations from all twelve seasons on the same measurement plane. We
next define a common spatial reference on this plane so that changes in the operational strike-zone definition are not
mistaken for changes in umpire judgment.



3.2     Spatial Reference and Edge-Specific Samples
Comparing umpire judgment across seasons requires a spatial reference that remains fixed over time. This is especially
important in 2026, when challenge-based ABS was introduced together with a new operational definition of the strike
zone. If each season were measured relative to its own operational zone, movement in the reference boundary could
offset or exaggerate movement in the called boundary. For this, we measure every season relative to a single fixed
reference and account separately for differences in the official strike-zone definition.
    We use the following 2026 ABS zone geometry as a fixed reference for all seasons.
                                 top
                               𝑅𝑏 = 0.535 ℎ𝑏 ,         𝑅𝑏bot = 0.270 ℎ𝑏 ,            𝑅 side = 𝑊 ,      𝑊 = 8.5 in,                          (1)

where, ℎ𝑏 is the height of batter 𝑏. The top and bottom edges vary with batter height, while the two side edges are
located at ±𝑊 . Applying this geometry to all twelve seasons provides a common measurement reference. Note that we
use this geometry only as a common measurement reference and do not assume that it was the strike zone applied
before 2026.
    The choice of the 2026 geometry also reflects how the automated zone was developed. Wang et al. [64] describe how
earlier implementations based more directly on the three-dimensional rulebook zone produced calls that players found
unfamiliar. MLB subsequently calibrated a two-dimensional zone, including its placement at the midpoint of home plate,
to better align automated rulings with established calling practices [64]. The resulting geometry differs from earlier
rule definitions in physical space but was developed with reference to the ball-strike boundary experienced by players
and umpires. It therefore provides a meaningful fixed reference without requiring us to treat it as the historical rule.
    A pitch is ruled a strike when any part of the ball intersects the zone. Accordingly, we expand each geometric edge
by the radius of the baseball, 𝜌 = 1.45 inches.
                                         top  top
                                       𝑅˜𝑏 = 𝑅𝑏 + 𝜌,           𝑅˜𝑏bot = 𝑅𝑏bot − 𝜌,         𝑅˜ side = 𝑅 side + 𝜌.                            (2)

    With the reference boundary defined, each pitch can be represented by its signed distance from a particular edge. We
set 𝑑 = 0 at the reference boundary, with positive values toward the interior of the zone and negative values outside.
                    top        top
                  𝑑𝑖      = 𝑅˜𝑏 (𝑖 ) − 𝑧𝑖 ,   𝑑𝑖bot = 𝑧𝑖 − 𝑅˜𝑏bot
                                                               (𝑖 ) ,     𝑑𝑖ins = 𝑅˜ side − 𝑠𝑖 𝑥𝑖 ,      𝑑𝑖out = 𝑅˜ side + 𝑠𝑖 𝑥𝑖 ,          (3)

where 𝑠𝑖 = −1 for right-handed hitters and 𝑠𝑖 = +1 for left-handed hitters. This transformation gives the inside and
outside edges the same orientation for both batter sides. Under this representation, 𝑑𝑖𝑒 = 1 means that the center of the
ball lies one inch inside reference edge 𝑒, while 𝑑𝑖𝑒 = −1 means that it lies one inch outside.
    Pitches closest to an edge provide the most information about where calls change from ball to strike and how sharply
that change occurs. We estimate each edge using pitches within 𝑏 = 3.0 inches of its reference boundary. Across the
observed season-edge cells, this band spans 2.34 to 4.26 estimated transition widths 𝜎 defined below, with a median of
2.95.

Manuscript submitted to ACM
When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review                      9


  Pitches near a corner require an additional restriction because two boundaries may influence the call. For a target
edge 𝑒, we retain pitches that lie within 𝑏 inches of that edge while remaining sufficiently far inside both orthogonal
edges. The quantity |𝑑𝑖𝑒 | gives the absolute distance from the target edge regardless of whether the pitch lies inside
or outside the zone. For each orthogonal edge 𝑜, a larger positive 𝑑𝑖𝑜 indicates that the pitch lies farther inside that
boundary. The resulting edge sample is
                                                 n                             o
                                             𝐵𝑒 = 𝑖 : |𝑑𝑖𝑒 | ≤ 𝑏,   min 𝑑𝑖𝑜 > 𝑐 .                                            (4)
                                                                    𝑜⊥𝑒

The first condition keeps pitches near the target edge, while the second removes pitches close to corners where another
boundary may also influence the call. For consistency across seasons and edges, we use a single corner threshold 𝑐. We
choose this threshold so that pitches retained for a target edge have a fitted strike probability of at least 0.95 with respect
to each orthogonal edge across all observed season-edge cells. A threshold of 𝑐 = 3.7 inches satisfies this requirement,
while the corresponding cell-specific thresholds range from 1.13 to 3.66 inches. Applying these conditions leaves 842,456
pitches, which we refer to as the band sample. The four edge samples are mutually disjoint, so each pitch is assigned to
at most one edge and each edge is estimated from pitches for which it is the primary spatial constraint on the call.


3.3   Estimating Criterion and Sensitivity
Within each edge sample, the two-dimensional strike zone reduces to a one-dimensional decision problem. Each pitch
is represented by its signed distance 𝑑𝑖𝑒 from the reference edge and the umpire’s original call 𝑦𝑖 . As 𝑑𝑖𝑒 increases from
outside the zone toward its interior, the probability of a strike call increases.
  Following the psychophysical model of umpire judgment proposed by Flannagan et al. [13] and Lee et al. [33], we
adapt their logistic formulation to our edge-specific signed-distance representation:
                                                                  𝑑 +𝛼
                                                                  𝑒     
                                            Pr(𝑦𝑖 = 1) = logit−1 𝑖         .                                                 (5)
                                                                     𝜎
Whereas Flannagan et al. model pitch location using distance from the center of the strike zone, our formulation
measures signed distance from each individual edge. This allows us to interpret the two parameters directly in terms of
boundary judgment: 𝛼 captures the location of the called boundary relative to the common reference, while 𝜎 captures
the width of the transition from ball to strike calls.
  The two parameters describe different aspects of umpire judgment. The parameter 𝛼 determines the location of the
transition. The fitted strike probability equals 0.5 at 𝑑𝑖𝑒 = −𝛼, so 𝛼 > 0 indicates that the called boundary lies outside
the common reference, while 𝛼 < 0 indicates that it lies inside. We therefore interpret 𝛼 as the outward displacement of
the umpire’s decision criterion, measured in inches.
  The parameter 𝜎 determines the width of the transition. Smaller values produce a steeper change from ball to strike
calls around the boundary, while larger values produce a more gradual transition. For example, moving from −𝜎 to
+𝜎 around the 50-percent point changes the fitted strike probability from approximately 0.27 to 0.73. Thus, smaller 𝜎
indicates greater spatial sensitivity to changes in pitch location.
  Figure 2 shows how 𝛼 and 𝜎 capture distinct aspects of umpire judgment. Figure 2 (a) shows the four disjoint edge
bands used to estimate each boundary. Figure 2 (b) defines 𝛼 as the displacement between the fixed reference edge and
the estimated called boundary, capturing where the boundary is placed. Figure 2 (c) illustrates 𝜎: a small 𝜎 indicates a
sharp and consistent transition between ball and strike calls, whereas a large 𝜎 indicates greater ambiguity around the
boundary. Thus, 𝛼 measures where the boundary lies, while 𝜎 measures how sharply it is applied.
                                                                                                     Manuscript submitted to ACM
10                                                                                                                         Lee et al.




Fig. 2. Illustration of the two quantities used to characterize umpire decision boundaries. (a) A fixed reference zone defines four
disjoint edge bands used for estimation. (b) The per-edge displacement 𝛼 measures how far the estimated called boundary lies from
the reference edge. (c) The transition width 𝜎 captures how sharply the boundary is applied: smaller 𝜎 indicates a sharper transition,
whereas larger 𝜎 indicates a broader region in which similar pitch locations receive both calls.




Adjustment variables. Equation (5) captures the core relationship between pitch location and the probability of a
strike call. In the observed data, however, calls may also vary with the official strike-zone definition, batter geometry,
game context, and other factors. If these differences are ignored, they could shift the fitted psychometric curve and be
incorrectly attributed to changes in criterion or sensitivity. Given this, we add an adjustment term 𝐴𝑖 :
                                                                  𝑑 +𝛼
                                                                 𝑒           
                                          Pr(𝑦𝑖 = 1) = logit−1 𝑖         + 𝐴𝑖 .                                                   (6)
                                                                    𝜎
     The adjustment term collects four types of factors that we want to account for separately from the spatial transition:

                                            𝐴𝑖 = 𝜆 Δ𝑍𝑏 (𝑖 ) + 𝜌 𝑅 Rc𝑖 + 𝜸 ⊤ X̃𝑖 + 𝝉 ⊤ T𝑖 .                                        (7)

     The first term, Δ𝑍𝑏 (𝑖 ) , accounts for differences between the official strike-zone edge applicable to batter 𝑏 (𝑖) and the
fixed spatial reference used in our analysis. Recall that we measure every season using the same reference geometry so
that criterion is expressed on a common scale. However, the official zone itself can differ from this reference and can
change across seasons. Including Δ𝑍𝑏 (𝑖 ) allows the model to account for these differences rather than absorbing them
into the estimated umpire criterion.
     For the top and bottom edges, we additionally include Rc𝑖 to account for batter geometry. While our reference zone
already scales with batter height, umpires may not adjust the vertical boundary perfectly in proportion to that geometry.
Rc𝑖 measures how far the batter-specific reference edge differs from the corresponding seasonal average. We center this
variable within each season, so Rc𝑖 = 0 represents the average batter geometry for that season.
     The covariate block X̃𝑖 accounts for other characteristics that may systematically affect ball-strike calls. Following
the psychophysical specification of Flannagan et al. [13], it includes eleven count indicators, three batter-by-pitcher
handedness indicators, inning half, and umpire indicators. We center each covariate by its mean in the estimation
Manuscript submitted to ACM
When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review 11


sample. Consequently, X̃𝑖 = 0 represents the average composition of pitches in that sample rather than an arbitrary
combination of reference categories.
  Finally, T𝑖 contains variables specific to the analysis being conducted. For example, later analyses may use these terms
to distinguish pitches before and after a particular feedback event or between treatment and comparison conditions. We
leave these variables uncentered so that T𝑖 = 0 corresponds to the relevant baseline condition. The specific treatment
terms and their interpretation are introduced when each analysis is presented.
  With these adjustments, 𝛼 can be interpreted under a common reference condition in which the covariates and batter
geometry are centered at their mean values, the official zone edge coincides with the fixed spatial reference, and the
treatment is set to the baseline condition. Thus, 𝐴𝑖 captures systematic variation unrelated to the spatial judgment of
interest, allowing 𝛼 and 𝜎 to characterize the location and sharpness of the umpire’s ball strike transition.
Estimation and inference. For estimation, Equation (6) is fit in the equivalent linear logistic form

                                           logit Pr(𝑦𝑖 = 1) = 𝛽 0 + 𝛽𝑑 𝑑𝑖𝑒 + 𝐴𝑖 .                                        (8)

The psychophysical parameters are then recovered as
                                                       𝛽0              1
                                                 𝛼=       ,     𝜎=       .                                               (9)
                                                       𝛽𝑑             𝛽𝑑
  We estimate the model separately for each season and edge using Newton’s method. Because calls may be correlated
within both umpires and batters, we use a two-way cluster sandwich estimator with clustering by umpire and batter.
Standard errors (se) for 𝛼 and 𝜎 are obtained using the delta method, and all reported regression-based intervals use
1.96 × se.



3.4   Benchmarking 2026 Against the Pre-Adoption Trend
A direct comparison between 2025 and 2026 is insufficient because criterion and sensitivity were already changing before
challenge-based ABS was introduced. We therefore evaluate whether the 2026 estimates depart from the longer-term
trajectory observed before adoption. For each edge-specific 𝛼 and 𝜎 series, we fit a linear trend using the 11 seasons
from 2015 through 2025 and project that trend one year forward. We then compare the observed 2026 estimate with the
value predicted from the pre-adoption trajectory.
  We give the 11 annual observations equal weight. The residual year-to-year variation in these series is substantially
larger than the estimation error of the individual seasonal estimates. Weighting seasons by their estimation precision
would give seasons with larger within-season samples greater influence over the temporal slope even though they
are not necessarily more representative of the underlying year-to-year trajectory. Our inferential target is a new
annual observation rather than the mean fitted trend. Therefore, we evaluate the 2026 season data using the predictive
distribution for a new observation from the pre-adoption regression, which incorporates both uncertainty in the fitted
trend and residual year-to-year variation around it.
  For each series, we report the percentile of the observed 2026 value within this predictive distribution together with
its 50 and 95 percent prediction intervals. The 95 percent interval provides a conventional benchmark for identifying
observations outside the range implied by the pre-adoption trajectory, while the 50 percent interval provides a narrower
reference for the distance from its center. These comparisons indicate whether the 2026 criterion and sensitivity
estimates continue the historical trajectory or depart from it following the introduction of challenge-based ABS.

                                                                                                 Manuscript submitted to ACM
12                                                                                                                  Lee et al.


4     RQ1. How Do Umpire Calls Change Under Challenge-Based ABS?
4.1     Analytical Overview
Challenge-based ABS creates two levels at which changes in umpire calls may appear. At the system level, every call
becomes eligible for review once the challenge system is introduced, even when no challenge is made. At the event
level, an overturn provides explicit feedback that a particular call disagreed with the automated ruling. We first examine
the system level by asking whether the called boundary 𝛼 or transition width 𝜎 in 2026 departed from the 2015–2025
trajectory estimated in Section 3.3. Since all umpires entered the challenge system at the same time, this comparison
identifies a departure from the pre-adoption pattern rather than a causal effect of reviewability.
     We then turn to individual challenge rulings. Here, the question is more specific. “After an umpire receives an
overturn, does the called boundary move in the direction of the correction, does that response remain concentrated on
the reviewed edge, and is it still detectable in the umpire’s next game?” Answering these questions requires comparisons
both within the same game and across consecutive games.


4.2     Method
4.2.1 Identifying the Immediate Feedback Response. To identify the response associated specifically with corrective
feedback, we compare overturned challenges with upheld challenges. While both expose the umpire to automated
review, only an overturn indicates that the original call disagreed with the automated ruling. The contrast therefore
separates responses following corrective feedback from those following an upheld review. It is not randomized, however,
since overturned and upheld challenges may differ in pitch location and in the circumstances that led players to
challenge. Accordingly, we interpret the contrast as a differential response following corrective versus non-corrective
review rather than as an isolated causal effect of feedback.
     Beyond asking whether calls change after an overturn, we also ask whether the response remains specific to the
reviewed boundary. We compare subsequent pitches on the reviewed edge with those on the other three edges. A
response concentrated on the reviewed edge would indicate a local adjustment, whereas movement on the other edges
would suggest a broader change in the called zone. These two comparisons determine how challenge exposure is
represented in the model.
     For each pitch 𝑖, let 𝑒𝑖 denote its edge and 𝑜𝑖 its order within game 𝑔𝑖 . We classify challenges by verdict 𝑣 ∈ {ov, up}
and by the direction implied by the original call 𝑠 ∈ {tight, wide}. The direction of the correction depends on the
original call. A challenged ball corresponds to a potentially too-tight zone, while a challenged strike corresponds to
                                  𝑣,𝑠
a potentially too-wide zone. Let 𝐹𝑔,𝑒 be the pitch order of the first challenge of type (𝑣, 𝑠) on edge 𝑒 in game 𝑔, with
 𝑣,𝑠
𝐹𝑔,𝑒 = ∞ when no such event occurs. We then define
                                                                                                   
                                 𝐴𝑖own,𝑣,𝑠 = 1 𝑜𝑖 > 𝐹𝑔𝑣,𝑠          𝐴𝑖oth,𝑣,𝑠 = 1 𝑜𝑖 > min 𝐹𝑔𝑣,𝑠
                                                            
                                                       𝑖 ,𝑒𝑖
                                                               ,                             𝑖 ,𝑒
                                                                                                        .                 (10)
                                                                                      𝑒≠𝑒 𝑖

     The first indicator marks pitches after a ruling of type (𝑣, 𝑠) on the same edge, while the second marks pitches after
such a ruling on another edge. Once activated, each remains on for the rest of the game. The analysis therefore measures
how calls change after the first relevant ruling of each type rather than treating every repeated challenge as a separate
exposure.
     With challenge exposure defined in this way, we first estimate changes in boundary position. Let 𝑚 ∈ {own, oth}
denote whether exposure occurred on the pitch’s own edge or another edge. We fit
Manuscript submitted to ACM
When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review 13


                                                                       ∑︁
                                        𝜂𝑖 = 𝑎𝑐𝑖 + 𝛽𝑑 𝑑𝑖 + x𝑖⊤𝜸 +              𝜏𝑚,𝑣,𝑠 𝐴𝑚,𝑣,𝑠
                                                                                       𝑖     ,                            (11)
                                                                       𝑚,𝑣,𝑠
  where 𝑐𝑖 is the game-by-edge cell, 𝑑𝑖 is the signed distance from the relevant reference edge defined in Section 3.2,
and x𝑖 contains covariates that vary within a cell. The coefficient 𝜏𝑚,𝑣,𝑠 shifts the calling curve after the corresponding
exposure begins, representing a change in where the called boundary lies.
  We also examine whether a ruling changes the sharpness of the ball-strike transition. To do so, we allow challenge
exposure to modify the distance slope

                                                             ∑︁
                                 𝜂𝑖 = 𝑎𝑐𝑖 + 𝛽𝑑 𝑑𝑖 + x𝑖⊤𝜸 +
                                                                                              
                                                                     𝐴𝑚,𝑣,𝑠
                                                                      𝑖     𝜏𝑚,𝑣,𝑠 + 𝛿𝑚,𝑣,𝑠 𝑑𝑖 .                          (12)
                                                             𝑚,𝑣,𝑠
  When an exposure is active, the distance slope becomes 𝛽𝑑 + 𝛿𝑚,𝑣,𝑠 . Thus, 𝜏, which shifts the calling curve, captures
where the called boundary moves, while 𝛿, which changes the distance slope, captures whether calls around that
boundary become sharper or more gradual.


4.2.2 Controlling for Game-Level Conditions. To separate changes following a challenge ruling from conditions shared
within the same game, we compare pitches within game-by-edge cells. Ballpark characteristics, environmental conditions,
and other factors shared within a cell may affect umpire calls while also being related to when challenges occur. A
conditional logistic model keeps the comparison within the same game and edge while accounting for these shared
conditions.
  An ordinary fixed-effect logistic model would require a separate intercept 𝑎𝑐 for every game-by-edge cell. Each cell
contains fewer than eight calls on average, making direct estimation of thousands of cell-specific intercepts prone to
small-cell estimation problems. Conditional logistic estimation instead conditions on the number of strike calls within
each cell and removes 𝑎𝑐 from the likelihood. The exposure coefficients are therefore identified from variation among
pitches on the same edge within the same game. Umpire indicators are also constant within these cells and drop out of
the conditional likelihood.
  Removing the cell intercept prevents us from recovering the absolute level of 𝛼, which describes where the called
boundary lies relative to the common reference. The event-level analysis does not require this absolute position. Instead,
the exposure coefficients identify how far the called boundary moves after a ruling within the same game.


4.2.3 Estimating Boundary-Specific Effects. We next translate the exposure coefficients into the spatial contrasts
reported in the results. For each edge membership 𝑚 and ruling direction 𝑠, we compare the post-ruling shift after an
overturn with the corresponding shift after an upheld challenge


                                                 𝐶𝑚,𝑠 = 𝜏𝑚,ov,𝑠 − 𝜏𝑚,up,𝑠 .                                               (13)
  Here, 𝐶𝑚,𝑠 captures the additional shift in the calling curve following an overturn relative to an upheld review. Since
this contrast remains on the logistic scale, we convert it to the distance scale from Section 3.3

                                         𝐶 own,𝑠                     𝐶 own,𝑠 − 𝐶 oth,𝑠
                                  Δown (𝑠) =     ,   Δtargeted (𝑠) =                   .                       (14)
                                           𝛽𝑑                               𝛽𝑑
  The quantity Δown measures how far the reviewed boundary moves after an overturn relative to an upheld challenge.
The quantity Δtargeted compares that movement with the other three edges and therefore indicates how strongly the
                                                                                                    Manuscript submitted to ACM
14                                                                                                              Lee et al.


response is concentrated on the reviewed boundary. Under our sign convention, a positive Δown means that the called
boundary moves outward.
     We apply the same overturn-versus-upheld comparison to transition width. Since 𝜎 is the reciprocal of the distance
slope, its value under each exposure state is

                                              1
                                   𝜎𝑚,𝑣,𝑠 =           ,   Δ𝜎,𝑚 (𝑠) = 𝜎𝑚,ov,𝑠 − 𝜎𝑚,up,𝑠 .                         (15)
                                          𝛽𝑑 + 𝛿𝑚,𝑣,𝑠
     The quantity Δ𝜎,𝑚 therefore measures whether the ball-strike transition becomes sharper or more gradual after an
overturn relative to an upheld challenge. No additional conversion is needed since 𝜎 is already expressed in inches.
Standard errors for these nonlinear contrasts are computed using the delta method.

4.2.4 Testing Persistence across Consecutive Games. The within-game analysis identifies the immediate response
following a challenge ruling, but persistence requires examining the umpire’s subsequent game. Since previous-game
exposure is constant within the current game, a current-game fixed effect would absorb it. We therefore return to the
model from Section 3.3 with umpire indicators and restrict the sample to pitches before the first overturn of the new
game. This opening window allows us to examine whether the post-ruling pattern remains detectable before any new
corrective feedback is received.
     Comparing these estimates with the within-game response provides a behavioral measure of how long the adjustment
lasts. We use this comparison to characterize its time course without assigning the observed pattern to a particular
cognitive mechanism.

4.2.5    Samples. The season-level analysis uses the full band sample described in Section 3.2. Event-level analyses use
2026, the only season in which challenge rulings are observed. The within-game sample contains 59,076 pitches across
7,040 game-by-edge cells, while the next-game analysis contains 25,938 pitches from the opening windows. Standard
errors for both event-level analyses are clustered by umpire.


4.3     Results
4.3.1 Season-Level Change under Reviewability. We first ask whether challenge-based ABS coincided with a system-level
change in umpire judgment beyond the changes already underway before 2026, focusing on boundary position 𝛼 and
transition width 𝜎. A departure in 𝛼 would indicate that the effective calling boundary moved, whereas a departure in 𝜎
would indicate a change in boundary sharpness. Since both quantities had already evolved over preceding seasons, we
compare the 2026 observations with forecasts from the 2015–2025 trajectory rather than treating 2025 as a stationary
baseline.
     Figure 3 shows that the two quantities behave differently in 2026. Panels (a) and (b) show the longer-term evolution
and forecast comparison for 𝛼. The whole-zone, bottom, inside, and outside estimates fall below their pre-adoption
forecasts with 𝑝 < 0.05, while the top edge remains within its predicted range with 𝑝 > 0.05. The largest departures
occur at the bottom and outside edges, where the called boundary had historically extended farther outside the common
reference. In contrast, panels (c) and (d) show that the 2026 𝜎 estimates remain close to their forecasts across the whole
zone and all four edges, with 𝑝 > 0.05 throughout.
     Taken together, these results indicate that umpire calls changed primarily in where the boundary was
placed, while the sharpness of that boundary remained consistent with its pre-adoption trajectory.

Manuscript submitted to ACM
  When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review 15

                                                                                                95% PI      Trend forecast
                      Whole zone    Top      Bottom      Inside       Outside                   50% PI      Observed 2026
                                                             ABS introduction
            2
(inches)




            1
            0 Rulebook boundary
            1
                   2016      2018         2020        2022        2024          2026   Whole     Top Bottom Inside Outside
                                          Season                                       2015 25 forecast vs. 2026 observed
                                            (a)                                                       (b)
                                                                                                95% PI      Trend forecast
                      Whole zone    Top      Bottom      Inside       Outside                   50% PI      Observed 2026
           1.4                                               ABS introduction

           1.2
(inches)




           1.0
           0.8
           0.6
                   2016      2018         2020        2022        2024          2026   Whole     Top Bottom Inside Outside
                                          Season                                       2015 25 forecast vs. 2026 observed
                                            (c)                                                       (d)
  Fig. 3. Seasonal changes in boundary position 𝛼 and transition width 𝜎 before and after challenge-based ABS. Figure 3 (a, c) show
  annual estimates from 2015–2026, with the dashed line marking ABS introduction. Figure 3 (b, d) compare the observed 2026 estimates
  (◦) with forecasts extrapolated from the 2015–2025 trend (⋄); shaded regions show the 50% and 95% prediction intervals. The 2026
  boundary positions shift toward the common reference, particularly at the bottom and outside edges, whereas transition widths
  remain close to their pre-2026 trends.

  4.3.2 Immediate Response to Challenge Feedback. The season-level analysis shows that boundary position departed
  from its previous trajectory in 2026, but it cannot reveal whether a particular automated correction is followed by a
  corresponding change in subsequent calls. At the event level, this leads to two expectations. A ball overturned to a
  strike indicates that the called boundary was too tight and should move outward, whereas a strike overturned to a ball
  indicates that it was too wide and should move inward. If this response is specific to the corrected spatial judgment, it
  should also be concentrated on the reviewed edge. We test these expectations by comparing overturned with upheld
  challenges and then the reviewed edge with the remaining edges. Since overturned and upheld challenges are not
  randomly assigned, we interpret these estimates as differential responses following corrective versus non-corrective
  review rather than as an isolated causal effect of feedback.
       Figure 4 shows both the directional and spatial patterns in boundary position. In panel (a), reviewed-edge estimates
  generally move outward after a “too tight” ruling, while panel (b) shows a tendency toward inward movement after a
 “too wide” ruling. The outward pattern is most visible at the bottom and outside boundaries. Estimates for the other
  three edges remain much closer to zero under both ruling directions, and none reaches statistical significance with
  𝑝 ≥ 0.086. Most reviewed-edge confidence intervals still include zero, so the data provide clearer evidence about the
                                                                                                          Manuscript submitted to ACM
  16                                                                                                                      Lee et al.

                                         Ruled edge (filled)    Same game, other edges (open)

             Whole
               Top
Zone edge


            Bottom
             Inside
            Outside
                      0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00               0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00
                             after a too tight ruling (inches)                       after a too wide ruling (inches)
                                           (a)                                                    (b)

             Whole
               Top
Zone edge




            Bottom
             Inside
            Outside
                       0.4       0.2      0.0         0.2       0.4            0.4        0.2        0.0        0.2         0.4
                             after a too tight ruling (inches)                       after a too wide ruling (inches)
                                           (c)                                                    (d)
  Fig. 4. Within-game changes after challenge rulings. (a) and (b) show changes in boundary position Δ𝛼; (c) and (d) show changes in
  transition width Δ𝜎. Filled markers indicate changes on the reviewed edge, while open markers indicate changes on the other three
  edges in the same game; the horizontal bars show 95% confidence intervals. After a “too tight” ruling, positive Δ𝛼 corresponds to
  expanding the called zone, whereas after a “too wide” ruling, negative Δ𝛼 corresponds to contracting it. Boundary-position changes
  are directionally concentrated on the reviewed edge, while changes in 𝜎 show no consistent pattern.

  direction and spatial concentration of the response than its precise magnitude at any single edge. This uncertainty
  reflects the relatively few pitches within each game-by-edge cell.
        Panels (c) and (d) examine whether the same rulings are followed by a change in boundary sharpness rather than
  boundary position. Here, Δ𝜎 varies in sign across edges and ruling directions, and most confidence intervals overlap
  zero. We therefore find no consistent evidence that an overturn is followed by either a sharper or a more gradual
  ball-strike transition around the affected boundary.
        Taken together, these results indicate that the clearest immediate post-overturn pattern is a directionally
  appropriate change in boundary position localized to the reviewed edge, with no comparable evidence of
  spillover to the other edges or a systematic change in transition width.

  4.3.3 Persistence across Consecutive Games. The preceding analysis shows that an overturn can be followed by a
  localized directional change within the same game, but RQ1 further asks whether that response persists beyond the
  immediate feedback context. A short-lived adjustment should be visible after the ruling but weaken by the next game,
  whereas a more persistent change should remain detectable when the umpire returns to call pitches later. We examine
  Manuscript submitted to ACM
When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review 17

                                     Within the same game        Next game, opening window


    Too tight

    Too wide
                 0.4        0.2         0.0         0.2          0.4        0.4          0.2        0.0           0.2          0.4
                        , overturned upheld (inches)                                 , overturned upheld (inches)
                                    (a)                                                          (b)
Fig. 5. Persistence of post-challenge changes across games. (a) Changes in boundary position Δ𝛼 and (b) changes in transition width
Δ𝜎. Filled markers indicate the remainder of the same game, while open markers indicate the opening window of the umpire’s next
game; the horizontal bars show 95% confidence intervals. The directional change in boundary position observed within the same
game largely disappears by the next game, while 𝜎 remains close to zero at both time horizons.


these alternatives by comparing the within-game estimates with those from the opening window of the umpire’s next
game, before another overturn can provide new corrective feedback.
     Figure 5 (a) shows a clear difference between these two time horizons for boundary position. Within the same game, a
“too tight” ruling is followed by an outward movement of the called boundary with 𝑝 = 0.014 < 0.05. A “too wide” ruling
is followed by movement in the opposite direction, although this estimate is less precise and does not reach statistical
significance with 𝑝 = 0.145 > 0.05. In the opening window of the next game, however, neither directional response
remains detectable. Both estimates lie near zero, with 𝑝 = 0.996 > 0.05 after a “too tight” ruling and 𝑝 = 0.670 > 0.05
after a “too wide” ruling. Panel (b) shows a similar lack of persistence in transition width, with Δ𝜎 remaining close to
zero at both time horizons.
     The contrast across games is therefore more consistent with an adjustment that is strongest shortly after corrective
feedback than with one that clearly persists into later judgments. This time course resembles the distinction in perceptual-
learning and motor-learning research between rapidly adjustable responses and more persistent recalibration [51, 62],
although the behavioral data do not identify the underlying mechanism. The next-game confidence intervals remain
wide enough that smaller carryover effects cannot be ruled out.
     The results show that the directional change in boundary position is detectable primarily within the
game in which the correction occurs and is not detectably preserved at the beginning of the next game.

     Key takeaway of RQ1. The clearest changes under challenge-based ABS appear in boundary position rather than
     transition width. Individual overturns are followed by localized directional adjustments within the same game, but
     these responses are not detectably preserved into the next game.


5     RQ2. How Did Systematic Variation in Umpire Calls Change Under Challenge-Based ABS?
5.1     Analytical Overview
RQ1 examined how the called strike zone changed under challenge-based ABS and how umpires responded to individual
overturns. Those broader changes need not imply that previously documented variation across conditions changed in
the same way. We therefore ask whether systematic variation associated with ball-strike count, player status, and pitch
type also changed in 2026.
                                                                                                          Manuscript submitted to ACM
18                                                                                                                Lee et al.


     For count and player status, we distinguish differences in boundary position 𝛼 from differences in transition width 𝜎.
Unlike count and player status, pitch type is a property of the pitch itself and may affect how difficult it is to judge. We
therefore characterize pitch-type differences using transition width and miscall rates rather than criterion bias. This
distinction also carries into the historical comparison. Count and player status are evaluated against their pre-adoption
trajectories, while pitch type is summarized against the 2015–2025 average, with statistical departures evaluated against
the pre-adoption trend.

5.2    Method
5.2.1 Condition-Specific Criterion and Transition Width. To measure how umpire calls vary across conditions, we
extend the regression from Section 3.3. For a categorical factor with reference group 𝑔0 , let 𝐺𝑖𝑔 indicate that pitch 𝑖
belongs to group 𝑔. Suppressing the adjustment terms already defined in Section 3.3, the model becomes

                                                              ∑︁
                                               𝜂𝑖 = 𝜂𝑖(0) +
                                                                                  
                                                                     𝐺𝑖𝑔 𝜏𝑔 + 𝛿𝑔𝑑𝑖 ,                                    (16)
                                                              𝑔≠𝑔0

     where 𝜂𝑖(0) is the baseline linear predictor and 𝑑𝑖 is the signed distance from the relevant zone boundary. The
coefficient 𝜏𝑔 shifts the calling curve relative to the reference group, capturing a difference in boundary position, while
𝛿𝑔 changes the distance slope and captures a difference in boundary sharpness.
     We convert the shift associated with 𝜏𝑔 to the condition-specific criterion 𝛼𝑔 using the transformation in Section 3.3.
The corresponding transition width is
                                                             1
                                                        𝜎𝑔 =      .                                               (17)
                                                          𝛽𝑑 + 𝛿𝑔
     This decomposition lets us distinguish two forms of systematic variation. 𝛼𝑔 describes where the called boundary
lies for condition 𝑔, while 𝜎𝑔 describes how sharply calls change around that boundary.
5.2.2 Count and Player Status. Count is represented by the twelve possible ball-strike counts, with 0-0 as the reference
category, and uses the full band sample from Section 3.2. Since count is the focal factor in this analysis, the count terms
included as adjustment covariates in the baseline model are omitted.
     To represent career status using information established before each season, we use the cumulative number of
All-Star selections. Moreover, different cut points are used by role to avoid sparse pitcher categories. Batters are grouped
into no previous selections, one to three selections, and four or more selections, whereas pitchers are grouped into no
previous selections, one selection, and two or more selections. Since each pitch involves both a batter and a pitcher,
both status variables enter the model simultaneously. We treat these groups as indicators of career status rather than as
causal effects of receiving an All-Star selection.
5.2.3 Pitch-Type Miscall Rates. We analyze six Statcast pitch types, including four-seam fastballs, sinkers, cutters,
sliders, curveballs, and changeups, using four-seam fastballs as the reference category and retaining only cells with at
least 209 pitches. Transition width 𝜎 describes how sharply calls change around the boundary, but it does not show the
direction in which calls disagree with the reference zone. We therefore separate miscalls into two directions

                         𝑁 (outside-zone pitch called strike)               𝑁 (inside-zone pitch called ball)
                𝑟 wide =                                      ,   𝑟 tight =                                   .         (18)
                              𝑁 (outside-zone pitches)                          𝑁 (inside-zone pitches)
     Here, 𝑟 wide measures how often pitches outside the reference zone are called strikes, while 𝑟 tight measures how often
pitches inside the zone are called balls. We also report the overall miscall rate, defined as the proportion of pitches in
the analysis band for which the umpire’s call disagrees with the reference zone, together with Wilson intervals.
Manuscript submitted to ACM
  When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review 19

                                                                                                    95% PI      Trend forecast
                                      3-0    0-0     3-2      0-2                                   50% PI      Observed 2026
                                                              ABS introduction
              2.0
              1.5
(inches)




              1.0
              0.5
              0.0 Rulebook boundary
              0.5
                        2016     2018       2020       2022         2024         2026        3-0        0-0         3-2        0-2
                                            Season                                      2015 25 forecast vs. 2026 observed
                                              (a)                                                      (b)
                                                                                                    95% PI      Trend forecast
                                      3-0    0-0     3-2      0-2                                   50% PI      Observed 2026
                                                              ABS introduction
              1.4
   (inches)




              1.2
              1.0
              0.8
              0.6
                        2016     2018       2020       2022         2024         2026        3-0        0-0         3-2        0-2
                                            Season                                      2015 25 forecast vs. 2026 observed
                                              (c)                                                      (d)
  Fig. 6. Count-dependent changes in boundary position 𝛼 and transition width 𝜎. (a, c) Seasonal estimates for four representative
  counts from 2015–2026. (b, d) Observed 2026 estimates compared with forecasts from the 2015–2025 trend, with 50% and 95%
  prediction intervals. In 2026, 𝛼 shifts below the pre-adoption forecasts across all four counts, with several estimates falling outside
  the 95% prediction intervals, while 𝜎 remains comparatively stable.

       Taken together, these measures help distinguish boundary movement from changes in boundary sharpness. Holding
  the pitch-location distribution fixed, an inward boundary shift should reduce wide-side errors while tending to increase
  tight-side errors. A sharper transition, by contrast, can reduce disagreement on both sides. The combination of 𝑟 wide ,
  𝑟 tight , and 𝜎 therefore shows whether changes in miscall rates are more consistent with a shift in the called boundary or
  with sharper calls around it.

  5.3         Results
  5.3.1 Count-Dependent Calling. RQ1 showed that boundary position shifted inward in 2026, but this system-level
  change does not tell us whether established differences across ball-strike counts changed with it. We therefore ask
  whether count-dependent calling became less pronounced or whether the familiar ordering remained while the
  boundaries shifted together. We estimate boundary position 𝛼, which captures where the called boundary lies, and
  transition width 𝜎, our measure of boundary sharpness, across all 12 counts and compare the 2026 estimates with their
  2015–2025 trajectories. Figure 6 shows four representative counts spanning the observed range.
       Figure 6 (a) shows that the established ordering in boundary position remains visible in 2026. The called boundary is
  still widest at 3–0 and tightest at 0–2, with 0–0 and 3–2 between them. Against their pre-adoption trajectories, however,
                                                                                                              Manuscript submitted to ACM
    20                                                                                                                             Lee et al.

                                                                                                        95% PI      Trend forecast
                                       level: none     level: 1-3     level: 4+                         50% PI      Observed 2026
                                                                      ABS introduction
                  1.5
Batter (inches)

                  1.0
                  0.5
                        Rulebook boundary
                  0.0
                           2016        2018          2020      2022        2024          2026       none          1-3            4+
                                                     Season                                     2015 25 forecast vs. 2026 observed
                                                       (a)                                                     (b)
                                                                                                        95% PI      Trend forecast
                                       level: none     level: 1-3     level: 4+                         50% PI      Observed 2026
                                                                      ABS introduction
                  1.2
Batter (inches)




                  1.0

                  0.8
                           2016        2018          2020      2022        2024          2026       none          1-3            4+
                                                     Season                                     2015 25 forecast vs. 2026 observed
                                                       (c)                                                     (d)
    Fig. 7. Boundary position 𝛼 and transition width 𝜎 by batter All-Star status. (a, c) Seasonal estimates for batters with no prior All-Star
    selections, one to three selections, and four or more selections. (b, d) Observed 2026 estimates compared with forecasts from the
    2015–2025 pre-adoption trend, with 50% and 95% prediction intervals. In 2026, 𝛼 falls below its pre-adoption forecast across all three
    status groups and the differences between groups narrow, while 𝜎 remains close to its predicted values.

    all four displayed counts shift inward. Panel (b) places the 3–0, 0–0, and 3–2 estimates beyond their 95% prediction
    intervals, while 0–2 lies near the lower bound. The broader shift observed in RQ1 therefore extends across counts
    without removing their relative ordering.
              A comparable departure does not appear in boundary sharpness. Figure 6 (c, d) shows the 2026 transition-width
    estimates 𝜎 remaining close to their predicted trajectories, with 𝑝 > 0.05 for all four displayed counts. Since the counts
    begin from different boundary positions, the same inward movement has different consequences. At 3–0, where the
    called boundary had historically been wider than the common reference, the shift brings it closer to that reference,
    while at 0–2 it can move an already tighter boundary farther inside.
              Taken together, these results show that the broader 2026 shift changes the absolute position of the
    called boundary across counts without removing the established count-dependent ordering, while boundary
    sharpness remains consistent with its pre-adoption trajectory.

    5.3.2 Player Status. The count analysis shows that established differences across game situations remain visible in
    2026, but player-status differences need not be equally stable. We therefore compare boundary position 𝛼 and transition
    width 𝜎 across batter and pitcher All-Star status groups. Before 2026, higher-status batters generally received tighter
    called boundaries, whereas higher-status pitchers tended to receive wider ones, although some group estimates overlap.
    Manuscript submitted to ACM
    When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review 21

                                                                                                           95% PI     Trend forecast
                                         level: none      level: 1      level: 2+                          50% PI     Observed 2026
                                                                         ABS introduction
                   1.5
Pitcher (inches)




                   1.0
                   0.5
                         Rulebook boundary
                   0.0
                            2016        2018           2020      2022         2024          2026       none          1            2+
                                                       Season                                      2015 25 forecast vs. 2026 observed
                                                         (a)                                                      (b)
                                                                                                           95% PI     Trend forecast
                                         level: none      level: 1      level: 2+                          50% PI     Observed 2026
                                                                         ABS introduction
Pitcher (inches)




                   1.2

                   1.0

                   0.8
                            2016        2018           2020      2022         2024          2026       none          1            2+
                                                       Season                                      2015 25 forecast vs. 2026 observed
                                                         (c)                                                      (d)
    Fig. 8. Boundary position 𝛼 and transition width 𝜎 by pitcher All-Star status. (a, c) Seasonal estimates for pitchers with no prior
    All-Star selections, one selection, and two or more selections. (b, d) Observed 2026 estimates compared with forecasts from the
    2015–2025 pre-adoption trend, with 50% and 95% prediction intervals. In 2026, 𝛼 falls below its pre-adoption forecast across all three
    status groups and the differences between groups narrow, while 𝜎 remains close to its predicted values.



               Figure 7 (a) shows that the batter-status groups move substantially closer together in 2026 after remaining separated
    through much of the pre-adoption period. Figure 7 (b) further shows that all three 2026 𝛼 estimates fall below their
    pre-adoption forecasts, with each departure significant at 𝑝 < 0.05. In contrast, Figure 7 (c, d) shows that 𝜎 remains
    close to its predicted trajectory, with 𝑝 > 0.05 for all three groups. Thus, the narrowing occurs primarily in where the
    boundary is placed rather than in how sharply it is applied.
               A similar pattern appears for pitchers. Figure 8 (a, b) shows that the three status groups converge to similarly lower
    boundary positions in 2026, with all observed 𝛼 estimates well below their pre-adoption forecasts. Figure 8 (c, d) again
    shows little evidence of a status-specific change in 𝜎, with 𝑝 > 0.05 across all three groups. Overall, challenge-based ABS
    coincides with a broad contraction of the called boundary and a narrowing of previously observed status differences,
    while leaving transition width comparatively unchanged.
               Taken together, these results show that status-associated differences narrow most clearly for batters in
    2026, unlike the count-dependent ordering that remains clearly visible, while the evidence is weaker for
    pitchers and boundary sharpness remains broadly consistent with its pre-adoption trajectory.

                                                                                                                    Manuscript submitted to ACM
22                                                                                                                    Lee et al.

Table 1. Miscall rates and transition width 𝜎 by pitch type within the boundary band, comparing the 2015–2025 average with 2026.
Stars mark a departure from the pre-adoption trend of Section 3.4 (∗ 𝑝 < 0.05, ∗∗ 𝑝 < 0.01).


                                                                    Miscall rate (%)                 𝜎 (in)
                   Pitch                Type         𝑛    2015–25    2026    Relative change     2015–25       2026
                   Four-seam fastball   all     319,326      27.1     19.9             −26.4*       1.00      0.82
                                        wide    142,034      41.9     25.0             −40.3**
                                        tight   177,292      15.3     15.4              +0.5
                   Sinker               all     179,968      27.5     19.5             −29.0**      1.05      0.83
                                        wide     79,619      43.7     25.6             −41.5**
                                        tight   100,349      14.7     14.5              −1.3
                   Cutter               all      55,688      28.2     20.6             −26.8        1.05      0.82
                                        wide     24,566      44.1     26.8             −39.2**
                                        tight    31,122      15.5     14.8              −4.4
                   Slider               all     106,188      27.7     21.0             −24.3*       1.03      0.87
                                        wide     45,313      45.1     27.8             −38.4**
                                        tight    60,875      14.9     15.1              +1.4
                   Curveball            all      63,024      26.1     21.9             −16.2        1.00      0.94*
                                        wide     25,729      43.5     29.2             −32.8*
                                        tight    37,295      14.3     15.5              +8.1
                   Changeup             all      58,454      26.9     19.2             −28.6**      0.95      0.85
                                        wide     29,228      40.8     20.2             −50.5**
                                        tight    29,226      13.3     18.1             +36.1*



5.3.3 Pitch-Type Differences. The count and status analyses ask whether established differences in boundary position
persisted across game situations and players. Pitch type raises a different question. Since pitches may differ in how
difficult they are to judge, we examine whether reduced disagreement with the reference zone appears across pitch
types and which side of the boundary accounts for it. Table 1 separates wide-side errors, where an outside pitch is called
a strike, from tight-side errors, where an inside pitch is called a ball, together with transition width 𝜎, our measure of
boundary sharpness. An inward boundary shift should primarily reduce wide-side errors, whereas a sharper boundary
should reduce errors on both sides.
     Overall miscall rates are lower in 2026 for all six pitch types, with reductions from 16.2% for curveballs to 29.0% for
sinkers. Relative to the pre-adoption trend, these reductions are significant for four-seam fastballs and sliders with
𝑝 < 0.05 and for sinkers and changeups with 𝑝 < 0.01. Cutters and curveballs also decline, but not significantly. The
more consistent pattern appears on the wide side. For every pitch type, outside-zone pitches are substantially less likely
to be called strikes in 2026, with reductions from 32.8% to 50.5%. All six depart significantly from their pre-adoption
trends with 𝑝 < 0.05.
     In contrast, tight-side errors do not show a common direction. They remain nearly unchanged for four-seam fastballs
and sliders, decline slightly for sinkers and cutters, and increase for curveballs and changeups. Only the changeup
increase is significant, rising by 36.1% with 𝑝 < 0.05. This wide-side concentration is consistent with the inward
boundary shift observed in RQ1, indicating that the overall decline in miscalls comes mainly from fewer outside-zone
pitches being called strikes.
     Boundary sharpness provides a complementary view of the pitch-type results. Although the 2026 transition-width
estimates 𝜎 are numerically lower than their 2015–2025 averages for all six pitch types, only the curveball departs
Manuscript submitted to ACM
When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review 23


significantly from its pre-adoption trajectory with 𝑝 < 0.05. Curveballs nevertheless retain the largest transition width
in 2026 and the smallest descriptive reduction in overall miscalls. Prior work has associated curveballs with distinctive
motion-perception effects [56], which may help explain this residual difference, although the present analysis cannot
distinguish that account from other pitch-specific factors.
    Taken together, these results show that the reduction in pitch-type miscalls is concentrated on wide-side
errors across pitch types, which is more consistent with the broader inward shift in boundary position than
with a uniform sharpening of calls around the boundary.

    Key takeaway of RQ2. Systematic variation in umpire calls changes unevenly in 2026. Count-dependent ordering
    remains visible, status-associated differences narrow most clearly for batters, and pitch-type miscall reductions
    come mainly from fewer wide-side errors.


6     RQ3. How Do Players Decide When to Challenge?
6.1    Analytical Overview
RQ1 and RQ2 examined how umpire calls changed under challenge-based ABS. We now turn to the other side of the
system, where players decide which calls receive automated review. Since only challenged calls are reviewed, which
errors ABS ultimately corrects depends partly on how players use their limited challenge opportunities.
    To study this choice, we define a challenge opportunity as a called pitch for which the eligible side still has at least
one challenge remaining. Using these opportunities, we first ask whether challenge use increases as the geometric
disagreement between the original call and the automated ruling grows. Exact pitch geometry is not available to players,
however, which leads to a second question of whether challenge behavior aligns more closely with overturn probability
based on that geometry or with probability inferred from information available at decision time. Finally, since an
unsuccessful challenge reduces the team’s remaining opportunities, we examine whether players become more selective
when only one challenge remains.


6.2    Method
6.2.1 Challenge Opportunities and Geometric Error. We first measure how far each pitch lies from a ruling that would
favor the side eligible to challenge. Using the official zone that determines the ABS ruling, we compute the signed
margin to the nearest boundary


                           𝑑𝑖 = min 𝑊 ′ + 𝑥𝑖 , 𝑊 ′ − 𝑥𝑖 , top𝑖 − 𝑧𝑖 , 𝑧𝑖 − bot𝑖 ,    𝑊 ′ = 𝑊 + 𝜌.
                                   
                                                                                                                          (19)
    The margin 𝑑𝑖 is positive inside the official zone and negative outside it. To put ball and strike calls on the same scale
from the perspective of the eligible side, we orient this margin according to the original call

                                           −𝑑𝑖 , if the original call was a strike,
                                          
                                          
                                          
                                    𝑚𝑖 =                                                                          (20)
                                           +𝑑𝑖 , if the original call was a ball.
                                          
                                          
    Under this convention, 𝑚𝑖 > 0 indicates a call that automated review would overturn in favor of the eligible side,
while 𝑚𝑖 < 0 indicates a call that would be upheld. The magnitude |𝑚𝑖 | gives the geometric distance from the relevant
boundary.
                                                                                                    Manuscript submitted to ACM
24                                                                                                                  Lee et al.


     Since 𝑚𝑖 is derived from tracked pitch location, it is available to the analyst but not directly to the player making the
challenge decision. We therefore use it as a geometric benchmark for how challenge use changes with distance into
or away from the overturnable region. We bin 𝑚𝑖 in 0.3-inch intervals over [−4.2, 4.2] inches and compute challenge
rates separately for the batting and fielding sides, excluding bins with fewer than 50 opportunities. Challenge rates for
𝑚𝑖 > 0 therefore show how often geometrically overturnable calls receive review, although unchallenged calls do not
by themselves indicate poor decisions because players do not observe the exact geometry represented by 𝑚𝑖 .

6.2.2 Geometry-Aware and Observable-Information Predictions. While the geometric benchmark identifies which calls
favor an overturn, players must decide without observing that exact geometry. To distinguish overturn probability
implied by exact geometry from what players can infer at decision time, we estimate two models. The geometry-aware
model includes the pitch’s signed position relative to the automated zone

                                             𝑝b𝑖𝐺 = 𝑃 (overturn𝑖 = 1 | geometry),

     so 𝑝b𝑖𝐺 represents overturn probability when exact spatial information is available. By contrast, the observable-
information model excludes exact zone-relative geometry and uses only information available when the challenge
decision is made


                                      𝑝b𝑖𝑂 = 𝑃 (overturn𝑖 = 1 | observable information).
  Thus, 𝑝b𝑖𝑂 represents overturn probability based on information that could inform the player’s decision. We compare
challenge rates against both predictions to ask which better tracks actual challenge use. Stronger alignment with 𝑝b𝑖𝑂
would be consistent with an information constraint, although it would not establish perceptual uncertainty as the only
reason that overturnable calls go unchallenged.
     To avoid comparing behavior with predictions fitted to the same observations, both probabilities are generated out
of sample using a walk-forward procedure. For each month, the models are trained only on earlier opportunities and
then applied to the subsequent month.

6.2.3 Remaining Challenge Inventory. Even when the available evidence favors an overturn, players may still conserve
a challenge because an unsuccessful attempt reduces the team’s remaining opportunities. We therefore ask whether
the same predicted overturn probability leads to different challenge use depending on whether one or two challenges
remain. Specifically, we compare challenge rates across predicted overturn probabilities for the two inventory states.
A lower rate with one challenge remaining would indicate more conservative use of the final opportunity, whereas
similar rates would suggest that remaining inventory plays a smaller role in the decision.

6.2.4 Sample. Across these analyses, the sample contains 146,725 challenge opportunities and 7,381 actual challenges,
corresponding to an overall usage rate of 5.03%.

6.3     Results
6.3.1 Challenge Rate by Geometric Error. We first ask whether challenge rates rise with the geometric severity of calls
that ABS would reverse. The oriented distance defined in Section 6.2 places batting- and fielding-side opportunities on
the same scale. Positive values indicate calls that automated review would overturn for the eligible side, and larger
values indicate greater disagreement with the original call. If players respond to this disagreement, challenge rates
should rise farther into the overturnable region.
Manuscript submitted to ACM
  When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review 25


                    Batting   Fielding   Miscall rate                                           Two challenges left   One challenge left
              1.0                                                        0.3
              0.8




                                                        Challenge rate
Probability




              0.6                                                        0.2
              0.4
                                                                         0.1
              0.2
              0.0                                                        0.0
                    4 3 2 1 0 1 2 3                                            0.0           0.5            1.0       0.0            0.5            1.0
                      Oriented distance from                                            Unobservable                            Observable
                     the official zone (inches)                                      overturn probability                   overturn probability
                                  (a)                                                        (b)                                    (c)
   Fig. 9. Challenge use as a function of call geometry and predicted overturn probability. (a) Challenge probability for the batting
   and fielding sides by oriented distance from the official zone; positive distance indicates calls that ABS would overturn, while the
   dashed line shows the corresponding miscall probability. (b, c) Challenge rates by predicted overturn probability using unobservable
   geometric information and observable information, respectively, separated by the number of challenges remaining. Challenge use
   rises more clearly with observable overturn probability, while having one versus two challenges remaining produces only modest
   differences.




          Figure 9(a) shows this increase, but challenge rates remain well below one even when the geometry strongly favors
   an overturn. Between one and three inches into the overturnable region, batting-side rates range from approximately
   0.19 to 0.30, while fielding-side rates range from approximately 0.31 to 0.65. Thus, many calls that ABS would overturn
   remain unchallenged despite an available opportunity to request review.
          The fielding side also challenges more frequently than the batting side across much of the observed range. This
   separation may reflect differences in what the two sides can observe, when they consider a challenge, or the value of
   reversing the call. Since oriented distance captures the underlying geometry rather than information available to the
   player, this comparison cannot distinguish among these explanations.
          Taken together, these results show that challenge use increases with the geometric severity of an over-
   turnable call, but many calls that ABS would reverse still receive no challenge.

   6.3.2 Challenge Decisions by Available Information. The geometric pattern leaves an important question unresolved:
   exact pitch geometry determines whether ABS will overturn a call, but players do not observe it directly. We therefore
   compare two estimates of overturn probability. The geometry-aware probability 𝑝b𝐺 uses the pitch’s exact position
   relative to the automated zone, whereas the observable-information probability 𝑝b𝑂 uses only information available at
   decision time. This comparison tests whether challenge decisions more closely follow the underlying geometry used by
   ABS or the information available to players.
          Figure 9 (b) shows only a weak relationship between challenge use and 𝑝b𝐺 . Across much of the middle range,
   substantially different geometry-based overturn probabilities correspond to similar challenge rates, spanning only about
   0.06. By contrast, Figure 9 (c) shows a much clearer increase with 𝑝b𝑂 , with challenge rates spanning approximately 0.21
   over the corresponding range. Challenge rates nevertheless remain well below one even when 𝑝b𝑂 is high, indicating
   that observable information alone does not explain every unchallenged error.
                                                                                                                             Manuscript submitted to ACM
26                                                                                                                       Lee et al.




Fig. 10. Illustrative examples of relaying ABS pitch-location information from the dugout. The numbered 3 × 3 zone board (left) and
compact hand signal (right) translate pitch-location information into cues that players can interpret during play. These examples
illustrate possible team-created feedback.




     Taken together, these results indicate that challenge decisions track information available to players at
decision time more closely than the exact geometry used by ABS, although observable information does not
fully explain why overturnable calls go unchallenged.


6.3.3 Challenge Decisions by Remaining Inventory. Even when observable evidence favors an overturn, players may
preserve a challenge because an unsuccessful attempt reduces future review opportunities. We therefore ask whether
remaining inventory changes how players respond to the same observable evidence. Holding 𝑝b𝑂 fixed, stronger
conservation would appear as lower challenge rates when only one challenge remains.
     Figure 9 (c) shows little separation between the two inventory states across most of the probability range. At low and
moderate values of 𝑝b𝑂 , teams with one and two challenges remaining challenge at similar rates. The curves separate
more clearly only at the upper end, where teams with two challenges remaining challenge somewhat more often. This
pattern is consistent with modest conservation of the final challenge, but the inventory effect is small relative to the
overall increase in challenge use with observable overturn probability.
     Taken together, these results suggest that remaining challenge inventory plays a secondary role in
challenge use, with clearer inventory differences appearing mainly when an overturn already appears likely.

     Key takeaway of RQ3. Players’ challenge decisions align more closely with information available at decision
     time than with exact ABS geometry. Many overturnable calls remain unchallenged, while remaining challenge
     inventory has a comparatively smaller relationship with challenge use.


Manuscript submitted to ACM
When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review 27


7     Discussion
7.1    Real-Time Feedback and Player Calibration
Our results suggest that access to information matters on both sides of the challenge system. In Section 4.3.2, an
overturn was followed by a short-lived change in an umpire’s subsequent calls. In RQ3, challenge decisions were more
closely associated with information available to players than with the exact pitch geometry used by ABS. Together,
these findings raise a broader question: what happens when automated officiating information becomes available to
participants during play?
    The KBO provides illustrative examples of how such feedback can emerge around full ABS. Because the system
produces a ruling on every pitch, teams can potentially use its output as a continuing source of information about the
automated zone. Figure 10 illustrates two communication practices observed in actual KBO games and redrawn here
for clarity: a numbered 3 × 3 grid identifying a region of the zone and a compact hand signal conveying pitch location.
These examples are not intended as standardized KBO practices; rather, they show how teams can build their own
communication layer around automated officiating.
    This possibility is relevant to MLB’s challenge format. Our RQ3 results show that many overturnable calls still go
unchallenged and that challenge use more closely tracks information players can infer than exact pitch geometry.
Additional feedback about previous pitches could therefore help players calibrate their estimate of the ABS boundary,
the umpire’s departures from it, and which borderline calls are worth contesting.
    MLB’s challenge system, however, provides a much thinner feedback stream than full ABS: only contested pitches
reveal an ABS ruling, and those pitches are already selected because someone suspected an error. The resulting feedback
is therefore sparse and potentially unrepresentative. This raises a broader Sports HCI design question: how much
algorithmic feedback should participants receive, in what form, and at what point in play? Figure 10 illustrates that
when system output is available, participants may create such feedback channels themselves.


7.2    Fans as Stakeholders in Automated Officiating
Our analysis has been confined to the two parties who act inside the challenge system, the umpire whose call is reviewed
and the player who requests the review. When a challenge is raised, however, the output of the system reaches not only
these two but also the people watching the game, whether in the ballpark or on a broadcast. Fans neither make the call
nor request the review, yet they are party to the process, and what it leaves them with is an experience of watching.
What, then, has this system added to that experience?
    To get a sense of this, we asked 32 viewers of a league in which the system rules on every pitch. What the challenge
arrangement adds to the experience of watching is more visible to viewers who have watched baseball without challenges.
They named two merits of the arrangement. The first is that established skills such as catcher framing—the catcher’s
technique of receiving borderline pitches in ways that increase the chance of a strike call—retain their value. The second
is watching the new ability of players to judge whether to contest a call. This suggests that when a change to the rules
opens a new angle on player ability, fans may take that angle up as a source of enjoyment.
    These responses also suggest that fans should be considered as an important stakeholder in the design of challenge-
based officiating systems. The information shown to viewers—what is revealed, when it is revealed, and how it is
represented—may shape how they interpret player judgment, uncertainty, and the role of automation in the game. For
example, selectively exposing pitch-location or overturn information could create new forms of anticipation around
whether a player chooses to challenge, while other designs may better preserve uncertainty or highlight traditional
                                                                                                 Manuscript submitted to ACM
28                                                                                                               Lee et al.


baseball skills. This makes spectators not merely observers of the system, but stakeholders whose experience depends
on how algorithmic information is disclosed. Future work should examine how the content, timing, and representation
of such feedback shape spectators’ understanding, enjoyment, and trust in automated officiating.
     The survey items, respondent characteristics, and full response distributions are given in the supplementary material.

7.3    Beyond the Ball Park
While our study is grounded in professional baseball, challenge-based ABS illustrates a broader form of human–AI
interaction in which automated judgment is selectively introduced into an otherwise human decision process. The
umpire remains responsible for the initial call, while players decide when algorithmic review should be invoked. This
creates two distinct interactions with automation: humans act under the possibility of later review, and others decide
when that review is worth requesting.
     Our findings suggest that the effects of such systems extend beyond whether the automated decision is more accurate.
Review provides localized feedback about human judgment, but because it is selectively invoked, participants see only
a subset of human–AI disagreements. What they learn from automation therefore depends not only on model outputs,
but also on when those outputs become visible and who can request them.
     This perspective applies to other human–AI systems that preserve human authority while providing selective
algorithmic oversight. Designers may therefore need to consider the frequency, timing, and granularity of automated
feedback alongside predictive accuracy. Challenge-based ABS provides a clear example of how these choices can shape
both the person being reviewed and those who decide when automation enters the interaction.

8     Conclusion
Challenge-based ABS creates a distinctive form of selective human–AI review because umpires make every initial call,
while players determine when ABS can intervene and issue the final ruling. This structure allows us to examine not
only how umpire judgment changes under automated review, but also how players decide which judgments receive that
review. Across twelve MLB seasons, we find that changes in umpire calls are most evident in boundary position rather
than transition width. Individual overturns are followed by localized directional adjustments within the same game,
although these responses are not detectably preserved into the next game. Systematic variation also changes unevenly,
with count-dependent ordering remaining visible, status-associated differences narrowing most clearly for batters, and
pitch-type miscall reductions coming mainly from fewer wide-side errors. On the player side, many overturnable calls
remain unchallenged, and challenge decisions align more closely with information available at decision time than with
exact pitch geometry. Together, these findings show that selective automated review depends both on how people
respond when automation corrects them and on whether other participants choose to invoke that correction in the first
place.

Ethics and Privacy Statement
This work draws on two public sources and one small survey. Pitch-level tracking data come from the Statcast records
that MLB publishes through Baseball Savant, and items absent from those records, namely umpire assignments, challenge
rulings, and All-Star selections, were supplemented from MLB’s public Stats API. No privileged access or non-public
information was used. The umpires and players in the data act in professional capacities, and the calls in question are
already public through broadcasts and official records, so no question of personal privacy arises. Because the analysis
nonetheless concerns individual patterns of judgment, umpires are handled only as anonymous identifiers and every
Manuscript submitted to ACM
When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review 29


quantity we report is an estimate across the population of umpires. Observation covers part of a single season under a
newly introduced system, so these results cannot serve as an assessment of any individual’s competence.
   The survey reported in the supplementary material was determined to be exempt from review by our institutional
review board. Thirty-two adults completed it online, recruited by convenience from the personal networks of the
research team. Participation was voluntary and uncompensated, respondents were informed of the purpose of the
survey and told they could stop at any time, and no identifying information was collected.


References
 [1] Ran Abramitzky, Liran Einav, Shimon Kolkowitz, and Roy Mill. 2012. On the optimality of line call challenges in professional tennis. International
     Economic Review 53, 3 (2012), 939–964.
 [2] David Almog, Romain Gauriot, Lionel Page, and Daniel Martin. 2024. AI oversight and human mistakes: evidence from centre court. In Proceedings
     of the 25th ACM Conference on Economics and Computation. 103–105.
 [3] Gagan Bansal, Tongshuang Wu, Joyce Zhou, Raymond Fok, Besmira Nushi, Ece Kamar, Marco Tulio Ribeiro, and Daniel Weld. 2021. Does the whole
     exceed its parts? the effect of ai explanations on complementary team performance. In Proceedings of the 2021 CHI conference on human factors in
     computing systems. 1–16.
 [4] John Charles Bradbury. 2019. Monitoring and employee shirking: Evidence from MLB umpires. Journal of Sports Economics 20, 6 (2019), 850–872.
 [5] Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z Gajos. 2021. To trust or to think: cognitive forcing functions can reduce overreliance on AI in
     AI-assisted decision-making. Proceedings of the ACM on Human-computer Interaction 5, CSCW1 (2021), 1–21.
 [6] Lago-Peñas Carlos, Rey Ezequiel, and Kalén Anton. 2019. How does Video Assistant Referee (VAR) modify the game in elite soccer? International
     journal of performance analysis in sport 19, 4 (2019), 646–653.
 [7] Daniel L Chen, Tobias J Moskowitz, and Kelly Shue. 2016. Decision making under the gambler’s fallacy: Evidence from asylum judges, loan officers,
     and baseball umpires. The Quarterly Journal of Economics 131, 3 (2016), 1181–1242.
 [8] Harry Collins. 2010. The philosophy of umpiring and the introduction of decision-aid technology. Journal of the Philosophy of Sport 37, 2 (2010),
     135–146.
 [9] Sameer K Deshpande and Abraham Wyner. 2017. A hierarchical Bayesian model of pitch framing. Journal of Quantitative Analysis in Sports 13, 3
     (2017), 95–112.
[10] Berkeley J Dietvorst, Joseph P Simmons, and Cade Massey. 2015. Algorithm aversion: people erroneously avoid algorithms after seeing them err.
     Journal of experimental psychology: General 144, 1 (2015), 114.
[11] Mary T Dzindolet, Linda G Pierce, Hall P Beck, and Lloyd A Dawe. 2002. The perceived utility of human and automated aids in a visual detection
     task. Human factors 44, 1 (2002), 79–94.
[12] Manfred Fahle. 2005. Perceptual learning: specificity versus generalization. Current opinion in neurobiology 15, 2 (2005), 154–160.
[13] Kevin S Flannagan, Brian M Mills, and Robert L Goldstone. 2024. The psychophysics of home plate umpire calls. Scientific Reports 14, 1 (2024), 2735.
[14] Dwight D Frink and Richard J Klimoski. 2004. Advancing accountability theory and practice: Introduction to the human resource management
     review special edition. Human resource management review 14, 1 (2004), 1–17.
[15] Thadeu Gasparetto and Kirill Loktionov. 2023. Does the Video Assistant Referee (VAR) mitigate referee bias on professional football? Plos one 18, 11
     (2023), e0294507.
[16] Gerd Gigerenzer and Daniel G Goldstein. 1996. Reasoning the fast and frugal way: models of bounded rationality. Psychological review 103, 4 (1996),
     650.
[17] Ben Green and Yiling Chen. 2019. The principles and limits of algorithm-in-the-loop decision making. Proceedings of the ACM on human-computer
     interaction 3, CSCW (2019), 1–24.
[18] David Marvin Green, John A Swets, et al. 1966. Signal detection theory and psychophysics. Vol. 1. Wiley New York.
[19] Etan Green and David P Daniels. 2014. What does it take to call a strike? Three biases in umpire decision making. In 8th annual Sloan-MIT sports
     analytics conference proceedings.
[20] Nina Grgić-Hlača, Christoph Engel, and Krishna P Gummadi. 2019. Human decision making with machine assistance: An experiment on bailing and
     jailing. Proceedings of the ACM on human-computer interaction 3, CSCW (2019), 1–25.
[21] Angela T Hall, Dwight D Frink, and M Ronald Buckley. 2017. An accountability account: A review and synthesis of the theoretical and empirical
     research on felt accountability. Journal of organizational behavior 38, 2 (2017), 204–224.
[22] Jeff Hamrick and John Rasp. 2015. The connection between race and called strikes and balls. Journal of Sports Economics 16, 7 (2015), 714–734.
[23] Michael J Hautus, Neil A Macmillan, and C Douglas Creelman. 2021. Detection theory: A user’s guide. Routledge.
[24] Ulrike Holder, Thomas Ehrmann, and Arne König. 2022. Monitoring experts: insights from the introduction of video assistant referee (VAR) in elite
     football. Journal of Business Economics 92, 2 (2022), 285–308.
[25] Mike Hsu. 2024. Umpire home bias in major league baseball. Journal of Sports Economics 25, 4 (2024), 423–442.

                                                                                                                         Manuscript submitted to ACM
30                                                                                                                                           Lee et al.


[26] David J Hunter. 2018. New metrics for evaluating home plate umpire consistency and accuracy. Journal of Quantitative Analysis in Sports 14, 4
     (2018), 159–172.
[27] Mohammad Hossein Jarrahi. 2018. Artificial intelligence and the future of work: Human-AI symbiosis in organizational decision making. Business
     horizons 61, 4 (2018), 577–586.
[28] Katherine C Kellogg, Melissa A Valentine, and Angele Christin. 2020. Algorithms at work: The new contested terrain of control. Academy of
     management annals 14, 1 (2020), 366–410.
[29] Jerry W Kim and Brayden G King. 2014. Seeing stars: Matthew effects and status bias in major league baseball umpiring. Management Science 60, 11
     (2014), 2619–2644.
[30] Otto Kolbinger and Martin Lames. 2017. Scientific approaches to technological officiating aids in game sports. Current Issues in Sport Science (CISS)
     (2017).
[31] Vivian Lai, Samuel Carton, Rajat Bhatnagar, Q Vera Liao, Yunfeng Zhang, and Chenhao Tan. 2022. Human-ai collaboration via conditional delegation:
     A case study of content moderation. In Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems. 1–18.
[32] John D Lee and Katrina A See. 2004. Trust in automation: Designing for appropriate reliance. Human factors 46, 1 (2004), 50–80.
[33] Kichang Lee, Kyungsik Han, and JeongGil Ko. 2025. Analyzing the impact of the automatic ball strike system in professional baseball through a case
     study on KBO league data. Scientific reports 15, 1 (2025), 44459.
[34] Kichang Lee and JeongGil Ko. 2026. Auditing Contextual Bias in Human Ball-Strike Calls Using KBO’s Automated Umpiring Transition. arXiv
     preprint arXiv:2609.03786 (2026).
[35] Kichang Lee and JeongGil Ko. 2026. Unified Pitch Graphs for Diagnosing Pitching Strategy. arXiv preprint arXiv:2609.03810 (2026).
[36] Min Kyung Lee, Daniel Kusbit, Evan Metsky, and Laura Dabbish. 2015. Working with Machines: The Impact of Algorithmic and Data-Driven
     Management on Human Workers. In Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems. 1603–1612.
[37] Sungmin Lee, Joonhee Lee, Minju Kang, Seungyong Lee, Dongju Kim, Jingi Hong, Jun Shin, Pei Zhang, and JeongGil Ko. 2026. JARVIS for HVAC:
     LLM-based Question-Answer Framework for Sensor-driven HVAC System Interaction. Proceedings of the ACM on Interactive, Mobile, Wearable and
     Ubiquitous Technologies 10, 2 (2026), 1–36.
[38] Jennifer S Lerner and Philip E Tetlock. 1999. Accounting for the effects of accountability. Psychological bulletin 125, 2 (1999), 255.
[39] Jennifer M Logg, Julia A Minson, and Don A Moore. 2019. Algorithm appreciation: People prefer algorithmic to human judgment. Organizational
     behavior and human decision processes 151 (2019), 90–103.
[40] Clare MacMahon and Janet L Starkes. 2008. Contextual influences on baseball ball-strike decisions in umpires, players, and controls. Journal of
     sports sciences 26, 7 (2008), 751–760.
[41] George Mather. 2008. Perceptual uncertainty and line-call challenges in professional tennis. Proceedings of the Royal Society B: Biological Sciences
     275, 1643 (2008), 1645.
[42] Brian M Mills. 2014. Social pressure at the plate: Inequality aversion, status, and mere exposure. Managerial and Decision Economics 35, 6 (2014),
     387–403.
[43] Brian M Mills. 2017. Technological innovations in monitoring and evaluation: Evidence of performance impacts among Major League Baseball
     umpires. Labour Economics 46 (2017), 189–199.
[44] Raja Parasuraman and Victor Riley. 1997. Humans and automation: Use, misuse, disuse, abuse. Human factors 39, 2 (1997), 230–253.
[45] Christopher A Parsons, Johan Sulaeman, Michael C Yates, and Daniel S Hamermesh. 2011. Strike three: Discrimination, incentives, and evaluation.
     American economic review 101, 4 (2011), 1410–1435.
[46] Samir Passi and Mihaela Vorvoreanu. 2022. Overreliance on AI literature review. Microsoft Research 339 (2022), 340.
[47] Forough Poursabzi-Sangdeh, Daniel G Goldstein, Jake M Hofman, Jennifer Wortman Wortman Vaughan, and Hanna Wallach. 2021. Manipulating
     and measuring model interpretability. In Proceedings of the 2021 CHI conference on human factors in computing systems. 1–52.
[48] Hatim A Rahman. 2021. The invisible cage: Workers’ reactivity to opaque algorithmic evaluations. Administrative science quarterly 66, 4 (2021),
     945–988.
[49] Daniel M Ravid, David L Tomczak, Jerod C White, and Tara S Behrend. 2020. EPM 20/20: A review, framework, and research agenda for electronic
     performance monitoring. Journal of Management 46, 1 (2020), 100–126.
[50] Daniel M Ravid, Jerod C White, David L Tomczak, Ahleah F Miles, and Tara S Behrend. 2023. A meta-analysis of the effects of electronic performance
     monitoring on work outcomes. Personnel Psychology 76, 1 (2023), 5–40.
[51] L Robert. 1998. Goldstone. Perceptual learning. Annual review of psychology 49, 1 (1998), 585–612.
[52] Alex Rosenblat and Luke Stark. 2016. Algorithmic labor and information asymmetries: A case study of Uber’s drivers. International journal of
     communication 10 (2016), 27–27.
[53] Dov Sagi. 2011. Perceptual learning in vision research. Vision research 51, 13 (2011), 1552–1566.
[54] Henri Schildt. 2017. Big data and organizational design–the brave new world of algorithmic management and computer augmented transparency.
     Innovation 19, 1 (2017), 23–30.
[55] Aaron Seitz and Takeo Watanabe. 2005. A unified model for perceptual learning. Trends in cognitive sciences 9, 7 (2005), 329–334.
[56] Arthur Shapiro, Zhong-Lin Lu, Chang-Bing Huang, Emily Knight, and Robert Ennis. 2010. Transitions between central and peripheral vision create
     spatial/temporal distortions: A hypothesis concerning the perceived break of the curveball. PloS one 5, 10 (2010), e13296.
[57] Masahiro Shinya and Mitsuto Tomomura. 2026. Bayesian sensory integration explains ball-count bias in Major League Baseball umpires. (2026).
Manuscript submitted to ACM
When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review 31


[58] Maurice A Smith, Ali Ghazizadeh, and Reza Shadmehr. 2006. Interacting adaptive processes with different timescales underlie short-term motor
     learning. PLoS biology 4, 6 (2006), e179.
[59] Jimin Song, Ji Hyuk Kang, and Richard J Paulsen. 2026. Technology adoption and bias in officiating: automated Ball-Strike System implementation
     in Korean Baseball. European Sport Management Quarterly (2026), 1–23.
[60] Jochim Spitz, Johan Wagemans, Daniel Memmert, A Mark Williams, and Werner F Helsen. 2021. Video assistant referees (VAR): The impact of
     technology on decision making in association football referees. Journal of sports sciences 39, 2 (2021), 147–153.
[61] Scott Tainsky, Brian M Mills, and Jason A Winfree. 2015. Further examination of potential discrimination among MLB umpires. Journal of Sports
     Economics 16, 4 (2015), 353–374.
[62] Jordan A Taylor, John W Krakauer, and Richard B Ivry. 2014. Explicit and implicit contributions to learning in a sensorimotor adaptation task. The
     Journal of neuroscience 34, 8 (2014), 3023–3032.
[63] Amos Tversky and Daniel Kahneman. 1974. Judgment under Uncertainty: Heuristics and Biases: Biases in judgments reveal some heuristics of
     thinking under uncertainty. science 185, 4157 (1974), 1124–1131.
[64] Andrea Wen-Yi Wang, Waki Kamino, David Mimno, Karen Levy, and Malte F Jung. 2026. Inside Baseball: The Automated Ball-Strike System as an
     Object Lesson in Technological Rule Enforcement. In The 2026 ACM Conference on Fairness, Accountability, and Transparency. 5828–5845.
[65] Takeo Watanabe and Yuka Sasaki. 2015. Perceptual learning: toward a comprehensive theory. Annual review of psychology 66, 1 (2015), 197–221.
[66] David Whitney, Nicole Wurnitsch, Byron Hontiveros, and Elizabeth Louie. 2008. Perceptual mislocalization of bouncing balls by professional tennis
     referees. Current Biology 18, 20 (2008), R947–R949.
[67] M Williams. 2019. MLB umpires missed 34,294 ball-strike calls in 2018. Bring on robot-umps. BU Today (2019).
[68] Ming Yin, Jennifer Wortman Vaughan, and Hanna Wallach. 2019. Understanding the effect of accuracy on trust in machine learning models. In
     Proceedings of the 2019 chi conference on human factors in computing systems. 1–12.
[69] Yunfeng Zhang, Q Vera Liao, and Rachel KE Bellamy. 2020. Effect of confidence and explanation on accuracy and trust calibration in AI-assisted
     decision making. In Proceedings of the 2020 conference on fairness, accountability, and transparency. 295–305.




                                                                                                                        Manuscript submitted to ACM

```
