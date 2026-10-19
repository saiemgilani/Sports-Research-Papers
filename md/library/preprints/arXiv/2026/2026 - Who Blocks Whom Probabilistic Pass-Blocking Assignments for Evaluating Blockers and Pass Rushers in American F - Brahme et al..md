<!-- source: library/preprints/arXiv/2026/2026 - Who Blocks Whom Probabilistic Pass-Blocking Assignments for Evaluating Blockers and Pass Rushers in American F - Brahme et al..pdf -->
<!-- arXiv:2609.33664 | https://arxiv.org/abs/2609.33664 | filed 2026-10-19 -->

# Who Blocks Whom? Probabilistic Pass-Blocking Assignments for Evaluating Blockers and Pass Rushers in American Football

                                               Who blocks whom? Probabilistic pass-blocking assignments for
                                                evaluating blockers and pass rushers in American football
                                                     Abhijit Brahme∗1 , Ishan Mehta2 , Gregory J. Matthews3 , and Alexander Franks4
                                                         1
                                                           University of California Santa Barbara, Probability and Statistics, e-mail:
                                                                                    abhijitbrahme@ucsb.edu
arXiv:2609.33664v2 [stat.AP] 29 Sep 2026




                                                                              2
                                                                                e-mail: ishanumehta13@gmail.com
                                                      3
                                                        Loyola University Chicago, Department of Mathematics and Statistics, e-mail:
                                                                                       gmatthews1@luc.edu
                                                         4
                                                           University of California Santa Barbara, Probability and Statistics, e-mail:
                                                                                        amfranks@ucsb.edu




                                                                                                Abstract
                                                         Historically, statistical analysis of offensive lineman has been hindered by the lack of eas-
                                                     ily measurable quantities. More recently, with the introduction of player tracking data new
                                                     methodological advances are now possible. Using high-dimensional spatio-temporal data, we
                                                     adapt the defensive-matchup hidden Markov model of Franks et al. (2015) from basketball to
                                                     football pass protection, producing frame-by-frame probabilistic assignments of each pass blocker
                                                     to the rushers. We show how this probabilistic assignment is a usable modeling artifact that
                                                     augments existing player-evaluation frameworks. We directly quantify the attention a rusher
                                                     commands, upgrade adjusted plus-minus (Macdonald, 2012) from all-or-nothing stints to partial,
                                                     continuous blocking credit in continuous time, yield block-shedding survival metrics, and measure
                                                     the space a rusher generates for his teammates. Fit to the first eight weeks of the 2021 NFL
                                                     season, the resulting metrics recover widely-recognized elite rushers and pass protectors and
                                                     align with independent charting.

                                           Keywords: hidden Markov model, Kalman filter, Hierarchical modeling, National Football League,
                                           offensive linemen, player tracking data


                                           1        Introduction
                                           American football is a complex game that consists of many different positions, each given a high
                                           specialized role: while there are only eleven athletes per team on the field at a time, there are over
                                           two dozen distinct positions. As such, measuring individual performance requires different metrics
                                           for each position, each of which targets the tasks assigned to that role. Historically, statistics were
                                           mainly kept for players in the so-called “skill positions" (i.e., quarterback, running backs, wide
                                           receivers, with tight ends often also included in this group). Running backs and wide receivers
                                           are evaluated based on yards gained, and quarterbacks are evaluated based on statistics such as
                                           completion percentage, yards per attempt, and quarterback rating. Defensive players are judged
                                           on statistics such as sacks, pressures, tackles, and interceptions, but these are relatively recent
                                               ∗
                                                   Corresponding author.


                                                                                                    1
additions to the collected statistics, with sacks not being officially recorded by the NFL until 1982
(Treacy, 2026), for example. Kickers and punters are measured by their field goal percentage and
average hang time, respectively. One can see that with the extreme specialization that is inherent to
American football, the statistics to measure the performance of each of these positions follow suit.
    While many of these statistics have been collected since the inception of the game, for much of
the game’s history there have been positions where collection of statistical performance measures
have been scant or even non existent. Defensive linemen, and even more so for offensive linemen,
have almost no historical statistical data collected for their performance as their contribution to any
given play is difficult to quantify in a simple manner. With the advent of advance tracking data,
however, we propose a novel method for analyzing the performance of both offensive and defensive
linemen performance.
    On passing plays, the role of the defensive line (and other players who are “rushers” on a
particular play) is ultimately to get to the quarterback as quickly as possible with the ideal outcome
from a defensive rusher’s perspective being a sack (i.e., tackling the quarterback for a loss before
they are able to throw the ball).
    On the other side of the ball, the goal of the offensive lineman is to block the defensive rushers
to allow their quarterback time to throw the ball unimpeded. However, offensive linemen, one of the
most important and highest paid position groups (Atienza-Romero, 2026), lack reliable measures of
their performance. Commonly, the offensive linemen are typically noticed when they err (i.e., they
allow a sack or miss a block), events which are relatively rare. Metrics based on counts of these rare
events tend to be unreliable estimates of ability. Metrics, such as the one we present here, which
better quantify the performance of offensive linemen would be invaluable for coaches and fans alike.
    While there are some metrics for quantifying the performance of offensive linemen, most of these
measures, focus on the offensive line as a unit rather than individual performance. For instance,
Football Outsiders measures the ability of pass blockers with adjusted sack rate (Football Outsiders,
2023). Burke (2018) proposes pass block win rate (PBWR), which measures the proportion of time
that a pass blocker is able to hold their block for at least 2.5 seconds. Unlike adjusted sack rate, this
measure evaluates individual linemen rather than the entire offensive line as a unit. However, this
method may not account for the ability of the rusher, or changing blocking assignments over the
course of the play. For example, a blocker may stunt, or pass off a rusher to a teammate, disrupting
the metric by incorrectly distributing credit among the blockers responsible for the block.
    Existing work analyzing the performance of offensive linemen involves hand-collecting data on
whether a blocker held their block long enough for the QB to throw the football. Alamar and
Weinstein-Gould (2008) used a three-game sample of data from the 2007 season to establish a
relationship between the amount of time a lineman can hold a block and pass completion. Later,
Alamar and Goldner (2011) looked at passing plays in the 2010 season and estimated the number of
yards each lineman contributed on offense. Ultimately, Alamar and Weinstein-Gould (2008) noted
the “absence of publicly available data that is needed in order to track the performance of a specific
lineman”, leading to the lack of research on this topic. Fortunately, with publicly-available player
tracking data NFL Football Operations (2023a), it is now possible to evaluate and better understand
the offensive line positions in football at a fine-grained level.

1.1    Contributions
Franks et al. (2015) used a Hidden Markov Model (HMM) to assign each defensive player to offensive
players in professional basketball. Their work demonstrated how player tracking data could be used
to study defensive performance, an aspect of basketball that has historically received less attention
than offensive performance. We apply a similar approach to football, where we use player tracking


                                                   2
data to identify which defensive player each offensive lineman is blocking. In doing so, we seek to
extend this type of analysis to another comparatively under-analyzed aspect of sports: offensive line
performance in American football.
    For each offensive lineman, the model produces probabilistic blocking assignments associated with
each frame of the tracking data. To our knowledge, no prior work generates blocking responsibilities
as a frame-by-frame probabilistic quantity in continuous time. We show that these assignments
offer useful summaries that can enhance existing analytical frameworks. Specifically, the assignment
probabilities let us (i) measure the attention a rusher commands; (ii) augment adjusted plus-minus
metrics (Macdonald, 2012) by assigning each blocker partial, continuous credit for the STRAIN
(Nguyen et al., 2023) of the rushers they engage in proportional to their assignment; (iii) read block
shedding and disengagement directly off the assignment dynamics; and (iv) quantify how much
space a rusher generates for their teammates. Further, we show that our methods are able to recover
per-position blocker positioning, identify top pass rusher and blocker talent in accordance with
scouting consensus, as well as recover hand-labeled pass-blocking assignments without the reliance
on hand-labeled data. In the next Section, we describe the player tracking data and other derived
metrics in detail. In Section 3, we provide an overview of our methodology and present the main
results. Finally, we discuss potential future work and limitations in Section 7.


2    Data
We use the player tracking data provided by the 2023 NFL Big Data Bowl (Howard et al., 2022) in
the analysis that follows. This data comes from the NFL’s Next Gen Stats system (NFL Football
Operations, 2023b), which returns the spatial coordinates of all 22 players on the field and the
location of the football at a frequency of 10 Hz (i.e., 10 frames per second). The data also includes
player speed, acceleration, orientation, and event annotations associated with each time frame within
a play. Event annotations include time-stamped demarcations of actions that occurred during the
play including, ball snap, quarterback throw, run, sack, etc.
    In total, the data contain 698 distinct pass rushers and 534 distinct pass blockers (i.e., offensive
linemen, backs, and TEs in blocking roles) are analyzed across 8,530 plays during the first eight
weeks of the 2021 season. (Appendix A describes the offensive position groups these blockers are
drawn from and how much each of them actually blocks on a pass play.) Throughout the paper,
we index quantities by play i, pass rusher j, pass blocker b, and frame (time step) t, with frames
sampled at 10 Hz. In order to assess pass blockers and pass rushers, we limit our analysis to the
individuals tagged by Pro Football Focus (an independent NFL contractor providing additional data
augmentation that relies on domain knowledge annotators) with a “Pass Block” or “Pass Rush” role.
Furthermore, we focus on the time-frames between the snap and the quarterback event (i.e. pass
attempt, run attempt, sack), again using the event annotations to filter our data. Before beginning
our analysis, we smooth the raw positional data using a Kalman filter, the details of which are
located in Appendix B.
    In addition to the raw data, we generate a derived pass-rush metric called STRAIN (Nguyen
et al., 2023), which is closely related to the concept of strain rate in materials science (Callister
and Rethwisch, 2018). Let dijt be the Euclidean distance between rusher j and the quarterback at
frame t of play i, and let vijt = ddijt /dt be its rate of change. With this notation, Nguyen et al.
(2023) define
                                                          vijt
                                          STRAINijt = −        ,                                     (1)
                                                          dijt
as a per-frame measure of each rusher’s pressure on the quarterback, so that a rusher’s STRAIN is


                                                   3
large when they are both close to and rapidly reducing their distance to the quarterback. Whereas
Nguyen et al. (2023) estimate vijt by a forward difference, we use the central difference method
with second-order accuracy for a more numerically stable derivative, and likewise approximate the
closing acceleration aijt = dvijt /dt with a second-order central difference.


3     A Hidden Markov Model (HMM) for Pass Blocking
A Hidden Markov Model consists of a series of latent states that evolve in time and probabilistically
“emit” observed data depending on the value of the latent state. In our application, the latent states
we seek to infer correspond to the identities of the rushers that a given offensive linemen could be
blocking. The conditional distribution of the location and orientation of the offensive linemen given
the latent defensive matchup is called the “emission distribution”. The blocking assignments evolve
in time, as linemen can switch to block different rushers as the play progresses. This probability of
switching latent states (i.e., switching pass-blocking assignments) is called the “transition probability".
Due to substantial differences in blocking technique and responsibility across offensive positions,
the model is fit independently for each blocking position group g ∈ {G, T, C, TE, RB, WR, FB}. We
write g(b) for the position group of blocker b and mark every group-specific parameter with the
superscript (g).

3.1    Modeling Blocker Positioning
The core assumption of our model is that the pass-blocker maintain their position such that they
are between their pass-rusher assignment and their quarterback. Let Rtj denote the location of
rusher j and Qt the quarterback position, and define Otb as the location of blocker b at time t. Let
Itbj be an indicator variable equal to 1 if blocker b is assigned to rusher j at frame t. Then, we posit
a model for Otb given that they are matched up against rusher j as
                                              (g)
                                             µtj = γr(g) Rtj + γq(g) Qt                                (2)
                                                           (g(b))     2(g(b))        
                                 Otb | Itbj = 1 ∼ N2 µtj            , σD        I2                     (3)

where Otb , Rtj , Qt ∈ R2 are x-y field coordinates. The emission is a bivariate normal whose mean
 (g)
µtj is a point on the segment joining the pass rusher to the quarterback, with an isotropic covariance
               2(g)
governed by σD .
   We also model the orientation of blocker b at time t given that they are blocking rusher j. Since
pass blockers typically face the pass rusher and attempt to stay square to the rusher during pass
blocking events, we propose a model for the orientation of blocker b based on the expectation that
their orientation should be roughly opposite of that of his assigned rusher. Specifically, let ηtj
and ηtb denote the orientation (in radians) of rusher j and blocker b at time t; the expectation
that the blocker faces the rusher corresponds to ηtb ≈ ηtj + π. Because orientation is a circular
(angular) quantity, we model it directly with a von Mises distribution, the circular analogue of the
Gaussian distribution. Given that they are guarding rusher j, we assume blocker b’s orientation is
vonMises(ηtj + π, κ) with density

                                      exp{κ cos(ηtb − ηtj − π)}   exp{−κ cos(ηtb − ηtj )}
                p(ηtb | Itbj = 1) =                             =                         ,
                                              2πI0 (κ)                  2πI0 (κ)
where I0 is the modified Bessel function of the first kind of order zero. The mean direction ηtj + π
encodes the blocker facing opposite the rusher, so the density is maximized when ηtb = ηtj + π.

                                                       4
The fixed concentration κ > 0 controls how strongly orientation informs the assignment. We fix
κ = 1. Because the positional and orientation emissions are conditionally independent given the
assignment, we model the joint conditional emission density as the product of the two individual
densities. In plain terms, the emission distribution encodes the idea that we expect a blocker to be
facing their assignment as well as in between the assignment and the quarterback.

3.2   Modeling Switches
In American football, offensive lineman may "pass off" rushers to their teammates, which results in
a switch in assignment during the course of the play. Lineman may also "stunt" (feint as if they
are going towards a rusher, then recover back to their original assignment), which also constitutes
a change in assignment. Our model must encode this frame to frame transition, or "stickiness" of
a blocker to his assignment. We let ni denote the number of pass rushers on play i, and we fit a
separate ρ(g) for each blocking position group g (Appendix A):

                                     P (Itbj = 1|I(t−1)bj = 1) = ρ(g(b)) ,

                                                           1 − ρ(g(b))                  ′
                        P (Itbj = 1|I(t−1)bj ′ = 1) =                  ,   for j ̸= j
                                                             ni − 1
Each ρ(g) is estimated via maximum likelihood within the EM algorithm, where it reduces to the
expected fraction of retained assignments; the derivation is given in Appendix C.2.
    The transition above treats every blocker in a position group as equally likely to switch at
each frame. In practice, this transition probability varies by player: an elite tackle anchored on an
edge rusher rarely switches, whereas an interior lineman routinely passes off twists and stunts. We
therefore let each blocker’s b transition parameter ρb vary by position and place a common Beta
prior over the player-level transition probability parameter within each position group,

                                         ρb ∼ Beta αρ(g(b)) , βρ(g(b)) .
                                                                      


                         (g)   (g)
The hyperparameters (αρ , βρ ) are themselves estimated from the data via an empirical Bayes
strategy, so that the player-level estimates are partially pooled. A blocker seen on many snaps is
governed by his own transitions, while one seen rarely is shrunk toward the position-level mean
  (g)    (g)    (g)
αρ /(αρ + βρ ) (See Appendix C.2 for full details). This yields a regularized measure of how
                                                                                              (g)  (g)
readily each individual blocker switches or passes off assignments. Estimation of ρb and (αρ , βρ )
within the EM algorithm is detailed in the appendix.
     We also incorporate pre-snap information to strategically inform the prior distribution of
assignments. Before the snap, a blocker’s responsibility is largely dictated by the protection scheme
and the defensive alignment. For instance, a left tackle is a-priori likely to be responsible for the
edge rusher aligned to its side, modulated by down, distance, and formation. Rather than initializing
the hidden Markov chain with a uniform distribution over rushers, we encode this pre-snap belief
with a multinomial-logistic model. Let Xibj denote a vector of pre-snap covariates for the (blocker b,
rusher j) pair on play i — the relative alignment at the snap (e.g. lateral and longitudinal offset,
whether the rusher is on the blocker’s side and whether it is the outermost rusher on that side),
the rusher’s lined-up alignment, and interactions of these with down, distance, and formation. The
initial distribution, omitting the play level subscript i for notational brevity, is then

                                                     exp{β (g(b))⊤ X0bj }
                               P (I0bj = 1) = P                (g(b))⊤ X ′ }
                                                                             ,
                                                     j ′ exp{β          0bj


                                                       5
with coefficients β (g) that are shared across plays but estimated separately for each blocking position
group. Each position has their own learned mapping from pre-snap alignment to likely assignment,
reflecting role-specific heterogeneity. The coefficients are fit within the EM algorithm (Appendix).
    To appropriately account for the fact that not every pass-blocker needs to be assigned a rusher,
we augment an (ni + 1)-th “disengaged state” to each blocker’s latent state space. Because the
disengaged state does not correspond to a rusher, it has a different emission distribution. We assume
that if a blocker is disengaged, their positional density is uniform over position and orientation
on the field, so the disengaged state is assigned to blocker for a frame when no rusher’s position-
and-orientation density clears the background level. Transitions to and from the disengaged state
are asymmetric, reflecting the fact that once a block is shed (denoted with parameter pfail ) or
                                                                 (g)
lost, it is difficult to re-engage (denoted with parameter ρnull ). As with ρb , the hazard pfail,b is
                            (g)
estimated per blocker, ρnull is pooled per position group, and the background level cbg is a single
fixed constant shared across groups (See Appendix C.2 for details). The engaged-to-disengaged
transition parameter is used in Section 3.3.2 to measure how long blockers sustain their blocks and
how quickly rushers shed them.
                                                                            (g) (g)                 2(g)
    To summarize the scope of each parameter: the emission weights (γr , γq ) and variance σD ,
the pre-snap matchup coefficients β (g) , the Dirichlet concentration α(g) of the stay/switch/fail
                                   (g)
prior, and the null persistence ρnull are estimated separately for each blocking position group g; the
stickiness ρb and block-failure hazard pfail,b are per blocker, partially pooled toward their position
group; and the orientation concentration κ and background level cbg are fixed constants common to
all position groups. Each position group is fit on its own data. The assignment probabilities are
recovered from the Expectation step of the forward-backward EM algorithm used to estimate the
relevant parameters. A full treatment of algorithm details are given in the appendix, and code for
the implementation can be found on Github.

3.3   Results of the HMM fits
                                                        2
                              Position       γr   γ q σD    ρ pfail ρnull
                              Tackle        0.82 0.18 1.41 0.97 0.02 1.00
                              Guard         0.84 0.16 1.21 0.97 0.01 1.00
                              Center        0.84 0.16 1.05 0.98 0.01 0.97
                              Tight End     0.89 0.11 2.29 0.96 0.02 1.00
                              Fullback      0.79 0.21 4.57 0.70 0.27 1.00
                              Running Back 0.55 0.45 5.91 0.39 0.58 1.00
                              Wide Receiver 0.99 0.01 4.61 0.45 0.55 1.00

Table 1: HMM parameter estimates by blocking position: the emission position weights γr , γq
                                                                                 2 ; the per-player
(blocker location along the rusher–quarterback segment) and positional variance σD
stickiness ρ (probability of staying on the engaged rusher); the block-failure pfail (engaged →
disengaged); and the disengaged-state persistence ρnull .

    We run the HMM for each position group and recover the emission weights γr , γq which locate a
blocker along the segment from his engaged rusher to the quarterback. Consistent with common
protection designs, we find that offensive linemen and tight ends position themselves close to the
rusher they engage with (γr ≈ 0.82–0.89), whereas running backs position themselves closer to the
quarterback (γq ≈ 0.45). The positional variance σD 2 is tightest for the interior line (≈ 1.0–1.4) and

largest for running backs, wide receivers, and fullbacks (≈ 4.6–5.9), who are typically not anchored
to a fixed rusher.


                                                   6
     The transition parameter, ρ, is very high for linemen and tight ends (ρ ≈ 0.96–0.98) indicating
these positions rarely switch. It is far lower for running backs and wide receivers (ρ ≈ 0.4), who
are known to release into routes rather than sustaining a block over the course of the play. The
structured disengaged state separates that release from a genuine switch through the block-failure
parameter pfail , the per-frame rate of transitioning from blocking to the disengaged state. It is
negligible for the interior line and tight ends (pfail ≈ 0.01–0.02) and large for backs and receivers
(pfail ≈ 0.55–0.58). Finally, the disengaged-state persistence ρnull ≈ 0.97–1.00 is near-absorbing at
every position. Once a blocker is beaten or has released, he rarely re-engages within the same play.
These estimates align closely with football intuition, supporting the model construction.

3.3.1     Rusher Attention and Blocker Entropy
In this Section, we describe simple metrics derived from the results of the HMM. First, we derive a
metric that quantifies the effective number of blockers a rusher faces at a given instant. Specifically,
we define “attention” as the sum of the assignment probabilities assigned to a rusher at a given
                        P
time-step, neff (j, t) = b θ(b, j, t). Aggregated over a play or a season, it is the number of “effective”
blockers a rusher faces over that time period. Because the number of effective blockers depends partly
on the blocking scheme a defense faces, we normalize each rusher’s attention within every play-frame
relative to the average rusher on the field such that the resulting figures are comparable across
three-, four-, and five-man fronts. Table 2 reports the rushers who draw the most front-normalized
attention by position, which generate about 1.5 times as many blockers per play as the average
rusher does. The five who draw the least by position can be found in Appendix Table 8.

   Name              Att.                 Name                 Att.               Name                  Att.
   Adam Butler       1.55                 Marlon Davidson      1.53               Brandon Williams      1.55
   Ta’Quon Graham    1.49                 Malcom Brown         1.53               Johnathan Hankins     1.52
   Calais Campbell   1.47                 Folorunso Fatukasi   1.52               Christian Covington   1.51
   Dre’Mont Jones    1.47                 Naquan Jones         1.51               John Jenkins          1.50
   Shelby Harris     1.46                 Sheldon Richardson   1.50               Greg Gaines           1.46

          (a) Edge                               (b) DT                                   (c) NT

        Table 2: Top 5 pass rushers by front-normalized attention, by position (min 50 snaps).

    Just as attention summarizes the load a rusher draws, the assignment probabilities also charac-
terize how a blocker distributes their responsibility. A blocker who stays attached to a single rusher
concentrates all of their assignment mass on one rusher, whereas a blocker who passes off rushers,
picks up stunts, or works in combination blocks spreads that mass across several. We quantify
this with the entropy of a blocker’s marginal assignment distribution over the rushers on a play,
normalized by log of the number of rushers in the front so that it is comparable across fronts of
different sizes. Table 3 ranks blockers by this front-normalized assignment entropy. The "stickiest"
blockers (lowest entropy) are almost exclusively offensive tackles, who tend to man up on a single
edge rusher; the one exception is a fullback, who blocks on too few snaps to spread his assignment.
The most variable (highest entropy) are predominantly interior linemen, consistent with their role
in passing off twists, stunts, and looping rushers.

3.3.2     Disengagement and Block Shedding
There are three distinct situations that can lead to blockers who will transition to a disengaged state:
1) a blocker can been be beaten, i.e. the the rusher has crossed to the quarterback side of him, 2) a
blocker can win his matchup by driving the rusher away from the pocket or 3) a blocker can simply

                                                    7
     Name                  Pos Norm. Entropy               Name               Pos Norm. Entropy
     Ben Cleveland       G          0.368                  Patrick Ricard   FB          0.042
     Netane Muti         G          0.336                  Dion Dawkins     T           0.134
     Elijah Wilkinson    T          0.308                  Isaiah Wynn      T           0.140
     Michael Deiter      C          0.307                  Yosuah Nijman    T           0.147
     Calvin Throckmorton T          0.304                  Rashawn Slater   T           0.152
     Jamarco Jones       T          0.303                  Andrew Thomas    T           0.154
     Justin Britt        C          0.302                  Donovan Smith    T           0.158
     Wes Schweitzer      G          0.300                  Dan Moore        T           0.158
     Ben Bartch          T          0.295                  Andrew Whitworth T           0.160
     Tyler Shatley       G          0.292                  Samuel Cosmi     T           0.163

            (a) Highest (most switching)                           (b) Lowest (stickiest)

      Table 3: Pass blockers ranked by front-normalized assignment entropy (min 50 snaps).


release the rusher with no other rusher to engage. In order to distinguish these different situations,
we use geometric features together with STRAIN. We assume a blocker in a disengaged state is
beaten only when the "assigned" rusher (i.e. the rusher whose assignment probability is highest
amongst all possible rushers) is on quarterback-side of him. Specifically, the blocker is considered
beaten when (d(rusher, QB) < d(blocker, QB)), and that rusher’s STRAIN is rising. Conversely, we
assume the blocker has won his matchup when in a disengaged state and the "assigned" rusher is
moving away with low or negative STRAIN. Finally, if neither of the previous two conditions are
met, the frame is classified as a release.
    For each play and blocker, we take the time from the snap to the first time beaten by a rusher as
a survival outcome, right-censored at the throw for the majority of blocks that are never beaten, and
summarize it with the Kaplan–Meier restricted mean survival time RMSTb alongside the per-block
beat rate BRb . Computing the same two quantities for a rusher rather than a blocker gives RMSTj
and the shed rate BRj , which measure how quickly and how often he beats the blocks he faces.
Table 9a ranks tackles by engagement. Because most blocks survive to the throw, the RMST sits
near the ∼ 4 s play horizon for nearly everyone. Elite pass protectors such as Rashawn Slater,
Andrew Thomas, Trent Williams, and Lane Johnson are beaten on only 3–6% of their blocks.
Conversely, Table 9b ranks rushers by how quickly they beat their blocks (shortest survival): Dont’a
Hightower, Jonathan Greenard, Nick Bosa, and A.J. Epenesa beat blocks both fastest and most
often, consistent with their reputations as disruptive rushers.
    Since elite tackles also face the best rushers, we additionally report an opponent-adjusted
quantity. We model the per-frame block-failure hazard directly as a discrete-time logistic survival
on the beaten events,
                             logit hb,t = α + g1 t̃ + g2 t̃2 + βopp Rj(b) + ub ,
where t̃ is (standardized) frames since engagement, Rj is the engaged rusher’s peak-STRAIN plus-
minus effect from the play-level model of Appendix D, entered at its posterior mean (standardized)
as a fixed opponent-quality covariate, and ub is a regularized per-blocker hold frailty with scale σu .
This model is also fit by NUTS with four chains (1,000 warmup and 1,000 retained iterations each).
The dwell coefficient is positive (ĝ1 > 0) suggesting that blocks fail more readily the longer they are
asked to last. The opponent coefficient is positive too (β̂opp > 0), confirming that facing a better
rusher raises the failure hazard. The resulting hold rating −ub (now adjusted for opponent quality)
moves Trent Williams from 15th to 3rd among the 93 tackles with at least 40 blocks (Figure 4).
The implied per-play beat probabilities run from ∼ 3% for the best protectors to ∼ 20% for the
most-beaten, rising a point or two against an elite edge rusher.


                                                   8
4     Extending Plus Minus Models
In this section, we describe how we can utilize partial blocking responsibilities from the HMM
assignment probabilities to quantify the moderated effect of a pass blocker on a rusher’s STRAIN
towards the quarterback. We introduce the continuous generalization which operates on a frame-
by-frame basis. The continuous generalization allows us to model the change in STRAIN over
time-steps attributed to a rusher and his blocking counterparts. We rank the rushers and blockers
according to expected STRAIN generated (or prevented), and find that our measures identifies
talent that correlates with PFF’s hand tagged rusher and blocker grades. Our model presented here
is Bayesian, allowing us to quantify the uncertainty of the estimates of our parameters of interest.

4.1    Continuous Time Blocker Plus-Minus
We extend the play-level plus-minus model of Appendix D to continuous time by resolving it to
the (play i, rusher j, frame t) level, so that every rusher-frame is a distinct observation rather
than a single play-level summary. We take the one-frame change in STRAIN as the response,
∆STRAINijt = STRAINi,j,t+1 − STRAINijt . The regressor is the blocking effect a rusher receives
at t, weighted by the blocking responsibility θ(b, j, t). Because the response looks one frame ahead,
θ(b, j, t, i) is the filtered assignment posterior, which uses the tracking data only up to frame t. The
blocker effect Bb∆ reflects how much blocker b’s engagement decelerates the rusher over the next
frame.                                               X                                       
                ∆STRAINijt ∼ N µ + Rj∆ + Q∆      qi −    Bb∆ θ(b, j, t, i) + ϕ STRAINijt , σ∆
                                                                                            2
                                                                                                .
                                                    b∈Xi

Equivalently, the model is a first-order autoregression of the next-frame STRAIN with coefficient
1 + ϕ. Rj∆ and Q∆qi are constant rusher and quarterback random intercepts that capture a rusher’s
own drive and a quarterback’s pocket behaviour. The rusher, blocker, and quarterback effects are
drawn around a linear function of player attributes z = [position, height, weight], which shrinks each
player toward their positional/size archetype,
                       ∆ R                       ∆ B                      ∆ Q
      Rj∆ = αR
             ∆⊤
                zj + σ R εj ,   Bb∆ = αB
                                       ∆⊤
                                          zb + σ B εb ,     Q∆    ∆⊤
                                                             q = αQ zq + σQ εq ,          ε ∼ N (0, 1),

with their own scales and residual σ∆ . The scales are given half-normal priors, σB       ∆ ∼ N + (0, 0.052 )

and σR ∆ , σ ∆ ∼ N + (0, 0.022 ); σ ∼ N + (0, 0.52 ). The intercept µ, the coefficient ϕ, and the attribute
            Q                      ∆
coefficients αR ∆ , α∆ , α∆ receive N (0, 1) priors.
                     B    Q
    The continuous-time model gives rusher, blocker, and quarterback ratings derived from STRAIN
dynamics. We fit it by NUTS on the 1.1M rusher-frames over eight weeks, again with four chains (800
warmup and 800 retained iterations each, 3,200 draws); the mean-reversion coefficient is ϕ̂ = −0.059.
On the common set of 207 linemen with at least 50 PFF pass-block snaps, the per-blocker effect Bb∆ ,
for which higher values mean better protection, correlates negatively with independent PFF charting
on both pressures allowed (Pearson −0.32) and the beaten rate (−0.25), and it also separates
protection skill within position (Pearson −0.29). The rankings (Figure 1) are led by interior linemen
Matt Skura, Quenton Nelson, and Michael Onwenu alongside tackles Marcus Cannon, Olisaemeka
Udoh, Bobby Massie, and Jordan Mailata. The rusher effect Rj∆ in turn tracks charted pass-rush
production closely (Section 6).
    Combining the attention metric of Section 3.3.1 with the continuous-time rusher effect, we can
plot how quickly a rusher builds STRAIN against how much blocking attention he receives. We
quantify attention in front-normalized terms: for each snap we divide a rusher’s effective-blocker
       P
count b θ(b, j, i) by the average over the rushers active on that snap, then average over the rusher’s


                                                     9
                                       Continuous−Time Blocker Rating

                        Matt Skura

                    Marcus Cannon

                  Olisaemeka Udoh

                   Quenton Nelson

                   Michael Onwenu




                                                                                                           All (Top)
                     Bobby Massie

                     Jordan Mailata

                      Ryan Jensen

               Jermaine Eluemunor

                   Jackson Carman

                    Will Hernandez

                 Andrew Whitworth

                     Michael Deiter

                      Blake Hance

                  Alex Leatherwood

                   Julien Davenport

                      Charles Leno




                                                                                                           All (Bottom)
                        Alex Cappa

                David Quessenberry

                    Kendrick Green

                       Jack Driscoll

                      Justin Herron

                    Daniel Brunskill

                    Austin Jackson
                                                 −0.01                   0.00             0.01
                                         B∆b   (per−frame STRAIN deceleration, centred on position mean)


                                                                     C          G   T



Figure 1: Posterior distributions of the continuous-time blocker rating Bb∆ for the top and bottom
twelve pass blockers (≥ 100 snaps), coloured by position. Vertical lines mark the 2.5, 50 and 97.5
percentiles. Zero is the average player at the position. Like the play-level coefficient, this is an effect
per unit of assignment.


snaps, so a value of 1 is an average share and values above 1 mean the rusher draws more than his
teammates. Figure 2 plots the two dimensions for every rusher with at least fifty pass-rush snaps.
The two are strongly negatively related (Pearson −0.78), and the plot splits positionally. Edge
rushers, who typically face fewer blockers, command less attention and sit in the upper left, led by
T.J. Watt, Odafe Oweh, Alex Highsmith, and Kyler Fackrell. Interior linemen draw more blockers
but build STRAIN more slowly and sit in the lower right (e.g. Brandon Williams, Malcom Brown,
and Naquan Jones). The few rushers in the upper right, who draw extra attention and still build
STRAIN quickly, include Jihad Ward, Kerry Hyder, Arik Armstead, and Dre’Mont Jones, along
with Cameron Heyward among interior linemen.


                                                                10
Figure 2: The two dimensions of pass-rush value for every rusher with ≥ 50 snaps (n = 250). The
horizontal axis is front-normalized attention commanded; the vertical axis is the continuous-time
rusher effect Rj∆ (per-frame STRAIN acceleration, adjusted for the blocking faced).


5    Pocket Space Ownership
Our final application incorporates the assignment probabilities into a space-control model of the
pass-protection pocket. We borrow heavily from Fernández and Bornn (2018) a space control
approach application in soccer and utilize the fitted blocking probabilities to measure the space a
rusher generates for his teammates. Each player k is assigned a bivariate influence Ik (p, t) ∈ (0, 1]
over field locations p. A location is controlled by whichever side’s influence is greater. Writing Bt
for the blockers (including the quarterback) and Rt for the rushers on the field at time t, the pocket
control (PC) at location p is the probability the offense owns that space,
                                             P                                     
                        PC(p, t) = logit−1      b∈Bt Ib (p, t) −
                                                                   P
                                                                       j∈Rt Ij (p, t)                (4)

visualized in Figure 3. Figure 3 shows the field across a collapsing pocket: at the snap the quarterback
sits in a protected area, which shrinks as a rusher wins. Quantitatively, the minimum over a play
of the quarterback’s own controlled area predicts charted pressure and sacks. To attribute that
control to individual players rather than to a side, we also define each player’s control share as
                      P
wk (p, t) = Ik (p, t)/ k′ Ik′ (p, t). Since space near the quarterback is more important, we value
it with weight V (p) = e−∥p−QBt ∥/λ , which decays exponentially with distance λ = 3 yd from the
quarterback. Integrating the two over a disk Dt of radius 5 yd centred on the quarterback gives



                                                  11
each k a value-weighted owned-space quality
                                                     X
                                   Qk (t) =                  wk (p, t) V (p) ∆a,                       (5)
                                                     p∈Dt

evaluated on a quarterback-centred grid, where ∆a is grid partition’s area. Table 11 lists rushers
who have gained valuable access to the pocket.
    While ownership is valuable in identifying who is gaining ground near the quarterback, pass
rushers rarely work in isolation. Typically, space generation occurs when a rusher pulls a blocker off
a teammate, freeing that teammate to win valuable near-QB ground. Our HMM reports, as a fitted
probability θ(b, r, t) ∈ [0, 1], whether the blocker is blocking him. Over a short window [t, t+w] we
therefore weight the event “blocker b leaves teammate i′ for the generator i” by the probabilities
directly,
                 Wb (i′ → i) = θ(b, i′ ; t) 1 − θ(b, i′ ; t+w) θ(b, i; t+w) 1 − θ(b, i; t) ,
                                                                                         
                              |   {z   }|               {z          }|     {z       }|     {z      }
                              was on i′               left i′            now on i    not on i before
and credit the generator with that fraction of the value-weighted space his freed teammate then
wins,
                                           Wb (i′ → i) Qi′ (t+w) − Qi′ (t) .
                                   XX                                     
                        SGGi +=
                                          b i′ ̸=i
   This recovers a dimension of pass rushing that personal-pressure metrics miss. The leading
space generators (Appendix Table 12) are primarily interior linemen who command double teams
and, in doing so, free their teammates. They rank high in attention but low in personal pressure
and plus-minus. Fernández and Bornn (2018) pair generation with its mirror image, space received.
Summing the directed flow over each generator–receiver pair of teammates (Table 4) recovers
recognizable synergies — Aaron Donald drawing the double and freeing his nose tackle, Dalvin
Tomlinson springing Danielle Hunter off the edge, Maxx Crosby opening the interior.

                    Unit Generator                           Receiver                     Space
                    IND Grover Stewart (DT)     DeForest Buckner (DT)                      98.4
                    GB Kingsley Keke (Edge)     Kenny Clark (NT)                           73.1
                    MIN Dalvin Tomlinson (DT) Danielle Hunter (Edge)                       69.9
                    LA  Aaron Donald (DT)       Sebastian Joseph (NT)                      59.7
                    NYJ Folorunso Fatukasi (DT) John Franklin-Myers (Edge)                 51.4
                    LV  Maxx Crosby (Edge)      Quinton Jefferson (DT)                     51.3
                    DEN Von Miller (Edge)       DreMont Jones (Edge)                       51.0
                    DEN Malik Reed (Edge)       DreMont Jones (Edge)                       47.8
                    NYG Austin Johnson (NT)     Leonard Williams (DT)                      46.2
                    WAS Jonathan Allen (DT)     Daron Payne (DT)                           46.2
                    IND DeForest Buckner (DT) Grover Stewart (DT)                          46.0
                    MIA Adam Butler (Edge)      Christian Wilkins (DT)                     45.5

Table 4: The strongest within-front space-generation flows: for each pair of teammates, the value-
weighted near-QB space one rusher (the generator) frees for the other (the receiver) by drawing a
blocker’s assignment away, summed over eight weeks.



6    External Validation against PFF Charting
Our assignments and metrics are derived purely from tracking geometry and STRAIN, so the
independently hand-charted pass-block / pass-rush data from Pro Football Focus provides an
external check.

                                                             12
Figure 3: Pocket space control across a collapsing play (snap to sack, left to right). Color is the
probability that the offense (blockers) controls each location; the quarterback (⋆) sits in a protected
blue pocket early and is exposed as a rusher wins control. Green: blockers; black: rushers; arrows:
velocity.


    First, the HMM assignments recover the charted blocker responsibilities. PFF tags, for each play
and blocker, the single rusher that blocker was responsible for. Over the 44,037 charted blocker-plays
we are able to match, our smoothed assignment places a mean of 0.77 of its engaged probability
mass on exactly that rusher and the model’s most-assigned rusher agrees with PFF’s designation on
87.5% of blocker-plays.
    Second, the block-shedding survival rates (Section 3.3.2) and the continuous-time rusher and
blocker effects (Section 4.1) also correlate with charted pressure outcomes in the expected directions
(Table 5). The table orients every correlation so that agreement in the expected direction is positive.
On the rusher side the agreement is strong: a rusher’s continuous-time effect Rj∆ tracks his PFF
pressure rate (Pearson 0.57) and sack rate (0.46), and his shed rate tracks his pressure rate as
well (0.37). On the blocker side the survival correlations are modest, but statistically significant
and directionally correct: blockers who sustain their blocks longer allow fewer pressures (0.19 after
orientation), and blockers who are beaten more often allow more (0.17). The continuous-time blocker
rating Bb∆ is the strongest blocker-side metric, with an oriented correlation of 0.32 with pressures
allowed. In conclusion, the rush-side metrics validate strongly against independent charting and the
block-side metrics validate directionally, providing confidence that our methodology is picking up
relevant signal.




                                                  13
             Model metric             Symbol PFF outcome Sign s Pearson ×s Spearman ×s
             Pass rushers (pressures obtained)
               Continuous-time effect Rj∆         pressures     +1   +0.57    +0.58
               Continuous-time effect Rj∆           sacks       +1   +0.46    +0.46
               Shed rate               BRj        pressures     +1   +0.37    +0.36
               Engagement RMST         RMSTj      pressures     −1   +0.31    +0.36
             Pass blockers (pressures allowed)
               Continuous-time effect Bb∆      pressures all.   −1   +0.32    +0.32
               Beat rate                BRb    pressures all.   +1   +0.17    +0.31
               Engagement RMST          RMSTb pressures all.    −1   +0.19    +0.33

Table 5: Correlation of tracking-derived model metrics with independent PFF pass-pressure charting
(players with ≥ 50 PFF snaps; rushers n = 250, blockers n = 207). The Symbol column gives the
quantity being correlated: the continuous-time rusher and blocker effects Rj∆ and Bb∆ of Section 4.1,
and the survival summaries RMST and beat rate BR of Section 3.3.2, subscripted j for a rusher and
b for a blocker. PFF outcomes are per-snap rates, where a pressure is a sack, hit, or hurry. Each
correlation is multiplied by the sign s, so that a positive value means agreement with PFF in the
expected direction. s = −1 for metrics that should move against the PFF outcome: a rusher whose
blocks last longer (larger RMSTj ) should generate less pressure, and a blocker who decelerates the
rush more (larger Bb∆ ) or sustains his blocks longer (larger RMSTb ) should allow less.




                                                     14
7    Discussion
We adapted the defensive-matchup hidden Markov model of Franks et al. (2015) from basketball to
football pass protection. The recovered assignments reproduce independently, hand-charted blocker
responsibilities. Beyond individual evaluation, the assignment probabilities reveal which rushers
draw the most interference and how protection schemes resolve over the course of a play, information
that can inform opponent scouting and the design of blocking schemes. We show that integrating
the probabilistic assignments into existing analytical frameworks yields insight into identifying top
rusher and blocker talent across a wide array of metrics ranging from space conceded / generated
to STRAIN allowed / prevented. Our implementation itself provides closed form updates where
applicable, providing scalable inference and a framework for incorporating more complex modeling
decisions.
    Although our methods are promising, there is certainly room for improvement. First, additional
information could sharpen the HMM assignments. We rely primarily on positioning, yet a blocker’s
direction of velocity carry complementary signal. We also do not fully separate a blocker who is
actively impeding a rusher from one who merely happens to be in the right place (i.e. a missed
block while nominally “assigned”). The disengaged state is a first step toward this distinction, but a
two-layer HMM in the spirit of Kabir et al. (2016) could, conditional on the assignment, additionally
infer the engagement status. Second, blocker evaluation remains the hardest open problem. Our
continuous time model is a step in the right direction; however, it is nonetheless an associational
estimate. Reformulating the problem from a causal perspective could potentially provide more
actionable insight for coaching and front office perspectives. Finally, other response variables are
worth exploring. Rather than STRAIN, one could rate rushers by acceleration projected along the
quarterback’s escape direction, foregrounding pursuit ability, or model the time-to-pressure hazard
directly. More broadly, the probabilistic instrument is agnostic to the outcome, so any frame-level
measure of pressure or disruption could be substituted for STRAIN without changing the evaluation
machinery.




                                                 15
Appendices
Appendix A            Offensive Position Groups
Our models are fit separately for each of the seven offensive position groups that appear in a blocking
role: guard (G), tackle (T), center (C), tight end (TE), running back (RB), wide receiver (WR), and
fullback (FB). These groups differ both in how often they block on a pass play and how they block.
    The offensive linemen (tackles, guards, and centers) are the primary pass blockers. They start
on the line of scrimmage on every snap and block on essentially every dropback. The center and the
guards form the interior of the line and typically engage interior rushers, who attack on the short,
direct path to the quarterback. The two tackles align at the outside edges of the line and usually
handle edge rushers, who take the widest and longest path to the quarterback.
    Tight ends occupy an intermediate role. A tight end may align at the end of the line or in
the backfield, and on a given pass play he may either stay in to block or release into a route as a
receiver.
    Running backs, wide receivers, and fullbacks are primarily receivers on pass plays; They do block
on occasion. A running back or fullback may stay in to protect the quarterback, chip an edge rusher
on his way into a route, or pick up an unblocked blitzing defender, and, in maximum-protection
schemes, additional players are kept in to block. However, on most dropbacks these players release
downfield rather than engage a rusher.

               Position group       Dropbacks with ≥ 1 blocking Mean blockers per dropback
               Tackle (T)                 8,530 (100.0%)                   2.09
               Guard (G)                   8,471 (99.3%)                   1.93
               Center (C)                  7,820 (91.7%)                   0.98
               Running back (RB)          1,541 (18.1%)                    0.18
               Tight end (TE)             1,195 (14.0%)                    0.17
               Fullback (FB)                146 (1.7%)                     0.02
               Wide receiver (WR)            44 (0.5%)                     0.01

Table 6: How much each offensive position group actually pass-blocks, over the 8,530 dropbacks
in the sample. A player counts as blocking on a play when the HMM places non-zero engaged
assignment mass on him.



Appendix B            Smoothing Positional Data
Before beginning our analysis using raw (x,y) tracking data, we smooth the observations. It is
known that RFID sensors are noisy, and thus analysis of raw values are subject to error. More
importantly, since our analysis heavily utilizes numerical differentiation techniques which rely on
smooth function assumptions, de-noising the presented data is of significant importance. In order
to achieve this, we apply a Kalman filter to the positional data, using the reported velocity and
acceleration only to initialize the latent state, as described below.
    Noting that movement in the x and y direction can be calculated independently, we present the
method for the x direction of motion and note that the same method follows for the y component.




                                                   16
B.1    Kalman Filter Implementation
A Kalman Filter is a specific instance of general state space models where both the emission and
latent state distributions are assumed to be normally distributed. The general formulation is as
follows:
                                          yt ∼ N (F θt , V )
                                                  θt ∼ N (Gθt−1 , W )
                                                    x0 ∼ N (m0 , C0 )
Note that F and G are known matrices, and V and W represent the error associated with the
observation vector yt and the latent state θt respectively. Similarly, m0 and C0 are initial parameters
defining the distribution of the initial latent state x0 .
    In our case the latent state collects the player’s true position, velocity, and acceleration in one
coordinate,                                          
                                                      zt
                                               θt = żt  ,
                                                     
                                                      z̈t
with zt the latent position. The dynamics follow a constant-acceleration model over the frame
interval δ = 0.1 s,

        zt = zt−1 + δ żt−1 + 12 δ 2 z̈t−1 + 16 δ 3 jt ,       żt = żt−1 + δz̈t−1 + 21 δ 2 jt ,       z̈t = z̈t−1 + δjt ,

that is θt = G θt−1 + jt with                                               
                                                                       1 2
                                                       1 δ             2δ
                                                  G = 0 1              δ .
                                                                            
                                                       0 0              1
The jerk jt is an unknown continuous white-noise input of spectral density q, which induces the
standard full-rank process covariance
                                                                                 
                                                  δ 5 /20 δ 4 /8 δ 3 /6
                                           W = q  δ /8 δ 3 /3 δ 2 /2 .
                                                  4                   
                                                   δ 3 /6 δ 2 /2    δ

   We treat position as the only observation and let the filter infer velocity and acceleration:
                                                                                      h             i
                            yt = zt + εt ,         εt ∼ N (0, σp2 ),             F = 1 0 0 .

The tracking feed reports a speed ∥vt ∥, an acceleration magnitude ∥at ∥, and a direction of motion
ηt . We use those derived kinematics to seed the initial state mean θ0 , with a tight prior on position
and a loose one on the inferred velocity and acceleration, C0 = diag(0.01, 1, 4).
     We set the process  spectral density q = 1 yd2 /s5 and the observation variance σp2 = 10−3 yd2
  ≈ (0.03 yd)2 . Finally, we apply the Kalman smoother, as derived in Kalman (1960) and
                

implemented in Duckworth (Duckworth), to every player, play trajectory, and use the smoothed
position, velocity, and acceleration in all subsequent analysis.




                                                                17
Appendix C             HMM Parameter Estimation
C.1    Model Formulation
We model the evolution of pass blocking assignments, as given by the matrix of matchups, Ii , over
the course of a play i using a hidden Markov model. Because the model is fit independently for
each blocking position group, the derivation below describes a single group, and we suppress the
group superscript (g) throughout this appendix, reserving the superscript (s) for the EM iteration.
Every parameter estimated here is understood to be that group’s own.
    Each blocker b on play i is associated with ni + 1 hidden states: the ni rushers on the play, and
a (ni + 1)-th disengaged state. We write Itbj = 1 when blocker b occupies state j ∈ {1, . . . , ni + 1}
at frame t, and reserve the index j ≤ ni for engaged states.

Emission Distribution Removing the subscript i for clarity, an engaged state emits the blocker’s
position and orientation as the product of the two following densities
                                             2                        2     
                  Dtb | Itbj = 1, γq , γr , σD ∼ N2 γr Rtj + γq Qt , σD I2 ,       j ≤ ni ,
                                                                     
                          ηtb |Itbj = 1, ηtj ∼ vonMises ηtj + π, κ ,        j ≤ ni ,
where κ is a fixed hyper-parameter and the emission weights are constrained to the simplex,
γr + γq = 1. The disengaged state has no rusher to correspond to, so we assign it an emission of a
flat positional background and a uniform orientation,
                                                                                          1
                   p(Dtb | Itb,ni +1 = 1) = exp(cbg ),        p(ηtb | Itb,ni +1 = 1) =      ,
                                                                                         2π
with cbg a fixed constant (von Mises with κ = 0 for the orientation). The value of cbg is chosen by
identifying the elbow of the implied mean disengaged probability curve (about 8% of blocker-frames)
on one week of data.

Transition Dynamics The transition is structured so that disengaging is a distinct event from
switching rushers. From an engaged state, blocker b stays with probability ρb , moves to one of the
other rushers with total probability 1 − ρb − pfail,b , disengages with the block-failure hazard pfail,b .
Once in the disengaged state, a blocker stays in the disengaged state with probability ρnull and
re-engages a rusher with 1 − ρnull :

                     P (Itbj = 1 | I(t−1)bj = 1) = ρb ,                                    j ≤ ni ,
                                                    1 − ρb − pfail,b
                    P (Itbj = 1 | I(t−1)bj ′ = 1) =                  ,              j ̸= j ′ ≤ ni ,
                                                          ni − 1
                 P (Itb,ni +1 = 1 | I(t−1)bj = 1) = pfail,b ,                              j ≤ ni ,
             P (Itb,ni +1 = 1 | I(t−1)b,ni +1 = 1) = ρnull ,
                                                     1 − ρnull
                 P (Itbj = 1 | I(t−1)b,ni +1 = 1) =            ,                           j ≤ ni .
                                                        ni
Here ni is the number of rushers on play i, constant within a play; ρb and pfail,b are per blocker and
ρnull is shared across the position group.




                                                      18
Initial Assignments At the snap the engaged states share the conditional-logit matchup prior of
Section 3 and the disengaged state receives a fixed mass ν,

                                                     exp{β ⊤ X0bj }
            P (I0bj = 1) = (1 − ν) P                          ⊤
                                                                        ,        j ≤ ni ,            P (I0b,ni +1 = 1) = ν,
                                                 j ′ ≤ni exp{β X0bj ′ }

with ν = 0.05. We omit the subscript for the play i for notational brevity.

Likelihood Writing I for the matrix of assignments, D for the blocker positions, and η for the
blocker orientations over a play, the complete-data likelihood over all plays in the group is
        N Y nY
             i +1
        Y                                                                                                                       It b j
L=                             P (Dti bi | Iti bi ji ) P (ηti bi | Iti bi ji ) P (Iti bi ji | I(ti −1)bi · )                            i i i   ,
        i=1 t,b j=1

so that the complete-data log-likelihood is
           N X nX
           X    i +1                h                                                                                               i
      l=                     Iti bi ji log P (Dti bi | Iti bi ji ) + log P (ηti bi | Iti bi ji ) + log P (Iti bi ji | I(ti −1)bi · ) ,
           i=1 ti bi ji =1

where for an engaged state ji ≤ ni the positional term expands to − 2σ12 ∥Dti bi − γr Rti ji − γq Qti ∥2 −
                                                                                                     D
log σD 2 up to a constant, and for the disengaged state the two emission terms are the constants c
                                                                                                      bg
and − log 2π.
     We group the parameters into two blocks: the emission and matchup-prior block Θ1 =
            2 , β), and the transition block Θ = ({ρ , p
(γr , γq , σD                                 2      b fail,b }b , ρnull ). The constants κ, cbg , and ν
are fixed.

C.2     Inference
The two blocks are estimated by a two-stage approach rather than a single joint EM. Stage 1
fits Θ1 by EM on the engaged-only model, obtained by deleting the disengaged state. As such,
each chain has ni states, the transition reduces to the stay/switch form P (Itbj | I(t−1)bj ) = ρ,
P (Itbj | I(t−1)bj ′ ) = (1 − ρ)/(ni − 1), and the initial distribution is the conditional-logit prior
over rushers alone (ν = 0). Stage 1 also produces a preliminary per-blocker stickiness under a
Beta-Binomial prior. Stage 2 then holds Θ̂1 fixed, restores the disengaged state, and fits Θ2 by
EM on the full (ni + 1)-state model. Each stage runs a fixed 15 EM iterations.
    We hold Θ1 fixed during estimation of Θ2 since this allows the model to be identified. Under
the augmented model, the background density cbg and the emission distribution variance σD       2 can

both be used for explaining poorly-fit frames. For example, a smaller variance would increase the
prevalence of disengaged states, and vice versa.

C.2.1      Stage 1: EM on the Engaged-Only Model
Utilizing the Expectation Maximization (EM) algorithm, we estimate the unknown Iti bi ji ∀i = 1 . . . N
                  2 , γ , γ and ρ. At each iteration s of the algorithm, we perform the E-step
(with ji ≤ ni ), σD    r   q
                                                                          ˆ
                                                            |D , ρˆ(s) , σ , Γˆ(s) ] and A
                                             (s)        (s)               2(s)
and M-step. For the E-step, we compute E          = E[I          ti bi ji         ti bi ji   ti bi ′ =
                                                                                                          D                      ti bi ji ji
                                              ˆ
E[Iti bi ji I(ti −1)bi j ′ |Dti bi , ρˆ(s) , σD , Γˆ(s) ] ∀i = 1 . . . N where Γ = [γr , γq ]. Using the forward-backward
                                              2(s)
                        i
algorithm, we can compute these expectations by each bi since we assume the pass blocking

                                                                     19
assignments are independent across blockers. In the M-step, we update the maximum likelihood
              2 , Γ, and ρ given the current expectations. Letting X = [R, Q] be the design matrix
estimates of σD
corresponding to the rusher location and quarterback location. Then Xti ji = [Rti ji , Qti ] be the
design matrix corresponding to rusher j during play i at time ti . In the sth iteration of the M-step
we first update estimates of Γ and σD 2


                                                        N X                        h 1
                      ˆ
            (Γˆ(s) , σD ) ←
                                                                                                                                           i
                      2(s)                              X                (s)                                               2          2
                           −     argmax             −                  Eti bi ji      2 ∥Dti bi − ΓXti ji ∥                    + log(σD )
                                            2
                               Γ : 1⊤ Γ=1, σD           i=1 ti bi ji
                                                                                    2σD

The estimator of Γ is the responsibility-weighted generalized least-squares solution projected onto
the constraint γr + γq = 1, as in Franks et al. (2015). Note that the estimated pass blocker variation
                  2 , is the weighted residual sum of squares at the updated Γ̂ divided by the total
at time step s, σ̂D
responsibility mass,
                                     PN                  T
                                                                           
                                 2     i=1 tr (Di − Γ̂Xi ) Ei (Di − Γ̂Xi )
                               σ̂D =
                                                 2 N
                                                  P
                                                    i=1 tr(Ei )
                      (s)
where Ei = diag(Eti bi ji ) over the rows of Xi and the residual Di − Γ̂Xi has one column per field
dimension. Because the emission is isotropic, the residuals from both dimensions are pooled into
this single variance. Next, we update our estimate of the transition parameter, ρ, in iteration s:
                                N X
                               X                                              N X X
                                                                               X                                                1−ρ 
            ρ̂(s) ←
                  − argmax                      Ati bi ji ji log(ρ) +                                        Ati bi ji j ′ log
                        ρ
                                 i=1 ti bi ji                                      i=1 ti bi ji ji ̸=j ′
                                                                                                                       i          ni − 1
                                                                                                         i


Since the log(ni − 1) term does not depend on ρ, the maximum likelihood estimate is the pooled
fraction of retained assignments,

                                                     S      Q̂                                         S
                                     ρ̂(s) =            =        ,                         Q̂ =          ,
                                                    S+W   1 + Q̂                                       W

where S = N                                      N
            P     P                                      P        P            P
             i=1   ti bi ji Ati bi ji ji and W = i=1 ti bi ji       ′ A         ′ are the total expected numbers
                                                              ji ̸=ji ti bi ji ji
of retained and switched assignments, respectively, and ni is the number of rushers in play i. Every
frame-to-frame transition contributes equally to the estimate.

Transition Heterogeneity By Blocker The pooled estimate above assigns one parameter to
an entire position group. We instead give each blocker b his own ρb with a shared conjugate prior
ρb ∼ Beta(αρ , βρ ), and produce the analogous sufficient statistics in the pooled case from A into
per-blocker expected transition counts
                                         X                                           X X
                                Sb =               Ati bji ji ,         Wb =                           Ati bji j ′ ,
                                                                                                                 i
                                        i,ti ,ji                                   i,ti ,ji ji ̸=j ′
                                                                                                  i


. Setting αρ = ρ0 c and βρ = (1 − ρ0 )c to a fixed weakly informative prior recovers an ordinary
conjugate-Bayes update in which the per-blocker step is fully closed form. Conditional on ρb , each
frame-to-frame transition is a Bernoulli “stay versus switch” trial. The posterior is ρb | Sb , Wb ∼
Beta(αρ + Sb , βρ + Wb ), and the maximization occurs at the mean

                                                                 Sb + αρ
                                                   ρ̂b =                      .
                                                            Sb + Wb + αρ + βρ


                                                                       20
This allows a blocker with many transitions to be influenced primarily by his own counts Sb , Wb ,
while one with few is shrunk toward the prior mean αρ /(αρ + βρ ).
    Each EM iteration thus updates every ρb in closed form, after which the expected counts Sb , Wb
are recomputed at the next E-step. Within Stage 1 the per-blocker ρb replaces the shared ρ when
forming the transition matrix in the E-step. They are re-estimated in Stage 2 under the structured
transition, for which the Stage-1 ρ̂b and prior mean ρ0 = αρ /(αρ + βρ ) serve as the starting point.

Matchup Prior The conditional-logit coefficients β of the initial distribution have no closed-
form update. In the M-step we maximize the corresponding term of the expected complete-data
log-likelihood,
                               N XX                exp{β ⊤ X
                                                               0bi ji }
                                                                           
                              X         (s)
                      Q(β) =           E0bi ji log P                         ,
                                                      ′ exp{β ⊤ X       ′}
                              i=1 b j         i     ji            0bi j   i               i

         (s)
where E0bi ji are the snap-frame (t = 0) responsibilities used as soft targets. This is a soft-label
multinomial-logistic regression with gradient
                                          N XX
                                          X                    (s)                  
                              ∇β Q =                       E0bi ji − P (I0bi ji = 1) X0bi ji ;
                                          i=1 bi      ji

we maximize it with a small number of Newton steps warm-started from the previous iterate. The
pre-snap features X0bi ji are standardized and β is shared across plays but estimated separately per
blocking position.

C.2.2    Stage 2: Disengaged Transition Estimation
Stage 2 restores the (ni + 1)-th disengaged state and its structured transition (Model Formulation
above) and estimates Θ2 = ({ρb , pfail,b }b , ρnull ), holding the Stage-1 emission weights, variance,
matchup-prior coefficients, and feature standardization fixed. The transition is initialized at the
Stage-1 per-blocker ρ̂b , with pfail,b = 0.01 and ρnull = 0.99.
    Each iteration runs the forward–backward algorithm over the ni + 1 states, with the engaged
emissions evaluated at Θ̂1 , the disengaged emission at cbg , and the initial distribution with fixed dis-
engaged probability ν. The posteriors yield expected counts per blocker, with the following sufficient
statistics: Sb (stay on the same rusher), Wb (switch to another rusher), Fb (engaged→disengaged),
and disengaged-row counts N stay (disengaged→disengaged) and N re (disengaged→rusher) pooled
over the position group. The sufficient statistics (Sb , Wb , Fb ) are multinomial, so we place a shared
Dirichlet(α1 , α2 , α3 ) prior over their three outcomes as α = (20ρ0 , 18(1 − ρ0 ), 2(1 − ρ0 )). The
per-blocker M-step is then closed form,
                      Sb + α1                                       Fb + α3
         ρ̂b =                        ,           p̂fail,b =                        ,         α0 = α1 + α2 + α3 ,
                 Sb + W b + F b + α 0                          Sb + W b + F b + α 0
and the disengaged persistence is the pooled fraction, ρ̂null = (N stay + 1)/(N stay + N re + 2). These
Stage-2 estimates form the transition matrix used to produce every assignment posterior, both the
smoothed forward–backward posterior and the filtered posterior of the continuous-time model.


Appendix D               Play-Level Plus-Minus Model
The opponent-quality covariate Rj in the block-hold hazard of Section 3.3.2 is the rusher effect of a
play-level plus-minus model, which the continuous-time model of Section 4.1 extends to the frame

                                                                 21
level. The model quantifies the maximum pressure a rusher generates on a play, while leveraging
the partial responsibilities of the pass-blockers generated from the HMM. For each rusher j on play
i, we take yij = maxt STRAINijt , the maximum STRAIN that rusher exerts over the frames of the
play. We model a rusher’s peak STRAIN as that rusher’s effect Rj , subtracted by the contribution
of the blockers Bb assigned to him, weighted by the average attention θ(b, j, i) that blocker b devotes
to rusher j on play i. Because of this formulation we capture the partial contributions of all blockers
on a play, and a more engaged blocker (larger Bb ) reduces the STRAIN its rusher can generate.
                                                                                                     
                            Bb θ(b, j, i) + Qqi + Ooi + Ddi + Dni + Qti + OFi + DCi + γ ⊤ si , σy2
                        X
    yij ∼ N µ + Rj −
                        b∈Xi

where Dni , Qti , OFi , DCi are random intercepts for the down, quarter, offensive formation, and
defensive coverage type of play i, Qqi , Ooi , Ddi are random intercepts for the quarterback, offensive
team, and defensive team, and si denotes covariates of score differential, game time remaining, and
field position.
    The rusher, blocker, and quarterback effects are drawn around a linear function of player
attributes z = [position, height, weight], which shrinks each player toward their positional/size
archetype, while the team and game-situation intercepts are zero-centered:
                        ⊤                        ⊤                        ⊤
                  Rj = αR z j + σ R εR
                                     j ,   Bb = αB z b + σ B εB
                                                              b ,   Qq = αQ z q + σ Q εQ
                                                                                       q ,

  Oo = σOff εO
             o,    Dd = σDef εD
                              d ,    Dni = σDn εDn
                                                dn(i) ,    and likewise Qt, OF, DC,          ε ∼ N (0, 1).
The intercept µ, the attribute-coefficient vectors αR , αB , αQ , and the game context effects γ are given
N (0, 1) priors, and every scale parameter — the residual σy together with σR , σB , σQ , σOff , σDef
and the four game context scales σDn , σQt , σOF , σDC — is given an Inverse-Gamma(2, 1) prior. All
continuous covariates are standardized.
    In contrast to previous plus/minus metrics which incorporate every on-field participant, we
include only the rusher of interest, excluding the other rushers. We argue instead that the blocking
assignment θ(·, j, i) is a sufficient conditioning variable for the influence of the remaining rushers.
The only way another rusher k can affect j’s STRAIN is by competing for the finite blocking
                                                                                          P
resource and drawing assignment mass away from j. Recall that for each blocker j θ(b, j, i) = 1
and that the reallocation is fully observed in the θ(b, j, i) that j receives. Conditional on θ(·, j, i),
the identities and abilities of the other rushers therefore carry no additional information about j’s
STRAIN.
    We fit the play-level model on all eight weeks of data (8,530 plays, 36,254 rusher observations)
with the No-U-Turn sampler (Hoffman and Gelman, 2014) implemented using NumPyro (Phan
et al., 2019), running four chains of 1,000 warmup and 2,000 retained iterations each (8,000 posterior
draws). Convergence diagnostics are reported in Appendix E.


Appendix E             Posterior Sampling Diagnostics
Three of the models in this paper are fit by the No-U-Turn sampler: the play-level plus-minus
model of Appendix D, the continuous-time blocker rating of Section 4.1, and the opponent-adjusted
block-hold hazard of Section 3.3.2. Each was run as four chains from dispersed initializations —
1,000 warmup and 2,000 retained iterations per chain for the play-level model, 800 and 800 for the
continuous-time model, and 1,000 and 1,000 for the block-hold model. Table 7 reports R  b and the
bulk and tail effective sample sizes for the parameters of interest.


                                                    22
                    Parameter                   Components    R
                                                              b      ESS (bulk) ESS (tail)
                    Play-level plus-minus (4 chains)
                    µ (intercept)                   1        1.002      3,107     3,827
                    Rj (rusher effects)            698       1.002      4,076     3,952
                    Bb (blocker effects)           534       1.003     9,853      4,796
                    Qq (quarterback effects)       60        1.002      6,683     4,552
                    αR , αB , αQ (attributes)       22       1.002      2,583     3,908
                    σR , σB , σQ                    3        1.002     2,816      4,470
                    σOff , σDef                     2        1.001     3,848      5,263
                    σDn , σQt , σOF , σDC           4        1.001     3,549      4,539
                    γ (situation slopes)            3        1.001     11,456     4,851
                    σy (residual)                   1        1.000     12,877     4,944
                    Continuous-time (4 chains)
                    µ (intercept)                   1        1.000     2,311      2,574
                    Bb∆ (blocker effects)          534       1.007     2,333      1,601
                    αB (blocker attributes)         8        1.001     2,331      2,336
                     ∆
                    σB                              1        1.003     1,318      2,021
                    Rj∆ (rusher effects)           698       1.006     1,610      1,591
                    αR (rusher attributes)         13        1.002     3,055      2,236
                     ∆
                    σR                              1        1.003     1,054      1,266
                    Q∆q (QB effects)               60        1.005     2,219      1,888
                    αQ (QB attributes)              2        1.003     1,700      1,866
                     ∆
                    σQ                              1        1.000     1,224      1,734
                    ϕ (STRAINt control)             1        1.002     3,120      2,158
                    σ∆ (residual)                   1        1.003     3,470      2,110
                    Block hold (4 chains)
                    α (baseline hazard)             1        1.004      944       1,579
                    g1 , g2 (dwell)                 2        1.002     5,664      3,074
                    βopp (opponent quality)         1        1.000     6,719      2,443
                    σu (frailty scale)              1        1.001      978       1,926
                    −ub (hold ratings)             534       1.006     3,220      1,871

Table 7: Convergence diagnostics for the three models fit by the No-U-Turn sampler, each run as
four chains. For vector parameters, Components gives the number of scalar components and the
table reports the worst value over them (largest R,
                                                  b smallest effective sample size). All parameters
        b ≤ 1.007, with bulk and tail effective sample sizes of at least 944.
satisfy R




                                                       23
Appendix F                          Supplementary Tables
These supplementary tables illustrate the variety of metric rankings derived from our models.

F.1        Attention Metrics

   Name                      Att.                         Name                        Att.                                Name                Att.
   K’Lavon Chaisson          0.72                         Chris Jones                 1.22                                Josh Tupou          1.29
   Justin Hollins            0.75                         Zach Sieler                 1.23                                Poona Ford          1.31
   Von Miller                0.77                         Dalvin Tomlinson            1.23                                Danny Shelton       1.31
   Dont’a Hightower          0.79                         Michael Hoecht              1.23                                Steve McLendon      1.35
   Terrell Lewis             0.80                         Ross Blacklock              1.24                                Eddie Goldman       1.35

             (a) Edge                                                 (b) DT                                                     (c) NT

     Table 8: Bottom 5 pass rushers by front-normalized attention, by position (min 50 snaps).



F.2        Disengagement Metrics

                   Opponent−Adjusted Block Hold
                             C (Top)                                           G (Top)                                            T (Top)


                                              Michael Onwenu
  Matt Paradis                                                                                            Taylor Moton

    J.C. Tretter                                   Alex Cappa
                                                                                                       Germain Ifedi

   Evan Brown                                     Dennis Daley                                        Trent Williams

 Aaron Brewer                                        Ali Marpet                                       Lane Johnson

  Trey Hopkins                                     Ben Powers                                             Trenton Scott
                            C (Bottom)                                        G (Bottom)                                         T (Bottom)

                                                                                                     Jamarco Jones
    Ryan Kelly                               Alijah Vera−Tucker

                                                                                                    Julien Davenport
   Greg Mancz                                  Andrew Norwell

                                                                                                          Jason Peters
 Michael Deiter                                  Damien Lewis

James Ferentz                                  Brandon Scherff                                         Duane Brown


 Justin McCray                                  Quinn Meinerz                                        Morgan Moses
                        0       2        4                               0        2          4                               0       2        4
                                                       − ub       (opponent−adjusted block−hold rating)


Figure 4: Posterior distributions of the opponent-adjusted block-hold rating −ub for the top and
bottom five pass blockers by position (min 40 blocks). Higher values indicate a blocker who sustains
his block longer.




                                                                         24
   Name                         RMST (s) Beat rate Adj resid (s)                                    Name                     Pos        RMST (s) Beat rate
   Joe Haeg                       4.000              0.014            -1.451                        Dont’a Hightower        Edge          3.663         0.161
   Germain Ifedi                  3.966              0.031            -0.708                        Jonathan Greenard       Edge          3.671         0.140
   Lane Johnson                   3.965              0.061            -0.340                        Michael Hoecht           DT           3.674         0.150
   Cornelius Lucas                3.961              0.054            -0.616                        Alton Robinson          Edge          3.682         0.172
   Braden Smith                   3.961              0.068            -0.706                        Yetur Gross-Matos       Edge          3.685         0.143
   Lucas Niang                    3.956              0.061            -0.583                        Zach Sieler              DT           3.706         0.122
   Rashawn Slater                 3.956              0.040            -0.983                        Chauncey Golston        Edge          3.721         0.155
   Trenton Scott                  3.956              0.023            -0.798                        Andrew Van Ginkel       Edge          3.733         0.113
   Dan Moore                      3.954              0.030            -1.279                        Nick Bosa               Edge          3.737         0.113
   Marcus Cannon                  3.953              0.057            -0.829                        Lawrence Guy             DT           3.744         0.141
   Olisaemeka Udoh                3.946              0.035            -0.968                        A.J. Epenesa            Edge          3.748         0.160
   Andrew Thomas                  3.945              0.030            -0.947                        Danny Shelton            NT           3.749         0.135
   Taylor Moton                   3.944              0.031            -0.748                        Steven Means            Edge          3.750         0.147
   Matt Nelson                    3.943              0.049            -0.885                        Carl Davis               NT           3.754         0.095
   Trent Williams                 3.942              0.040            -0.874                        Chase Winovich          Edge          3.756         0.122

(a) Tackle pass-block engagement (longer survival-to-                                       (b) Pass rushers that beat blocks fastest (shortest
beat = better)                                                                              survival-to-beat)

Table 9: Two sides of the same block-failure survival outcome: tackles ranked by how long they
sustain a block (a) and pass rushers by how quickly they beat one (b); min 40 blocks.


F.3       Plus Minus Metrics

                      Continuous−Time Plus−Minus: Pass Blockers
                                  C (Top)                                                       G (Top)                                             T (Top)


       Matt Skura                                                    Ben Cleveland                                   Marcus Cannon


     Ryan Jensen                                                   Quenton Nelson                                  Olisaemeka Udoh


        Billy Price                                                Michael Onwenu                                      Bobby Massie


    Frank Ragnow                                             Jermaine Eluemunor                                       Jordan Mailata


 Connor McGovern                                                   Jackson Carman                                  Andrew Whitworth
                                 C (Bottom)                                                    G (Bottom)                                          T (Bottom)


 Bradley Bozeman                                                      Blake Hance                                      Charles Leno

   Matt Hennessy                                                     Ben Bredeson                                       Jack Driscoll

    Michael Deiter                                                      Alex Cappa                                     Justin Herron

   Kendrick Green                                            David Quessenberry                                    Brady Christensen

     Austin Reiter                                                  Daniel Brunskill                                  Austin Jackson
                        −0.01      0.00       0.01                                     −0.01     0.00       0.01                           −0.01     0.00       0.01
                                                             B∆b    (per−frame STRAIN deceleration, centred on position mean)


Figure 5: Posterior distributions of the continuous-time blocker effect Bb∆ for the top and bottom
five pass blockers by position (min 50 pass-block snaps). Higher values indicate a blocker whose
engagement decelerates the rush more. Zero is the average player at the position.



F.4       Quarterback STRAIN Metrics
Because the quarterback intercept Q∆
                                   qi enters the continuous-time predictor of Section 4.1 additively,
the model yields a by-product ranking of quarterbacks by how quickly STRAIN builds on their


                                                                                       25
dropbacks. Reporting this as a suppression score −Q∆ q , Figure 6 lists the most and least STRAIN-
suppressing passers. Those who suppress the most (Kyler Murray, Aaron Rodgers, and Jalen Hurts)
are known for their mobility, whereas STRAIN builds fastest on the dropbacks of the less mobile
Ben Roethlisberger and Tom Brady. We note that this score reflects STRAIN rather than sacks,
so it measures how quickly pressure develops rather than whether it is converted. The posterior
distributions are wide and overlap, so only the extremes of the ranking are clearly separated.

                                   Continuous−Time Quarterback STRAIN Suppression

                    Kyler Murray

                 Aaron Rodgers

                     Jalen Hurts

                  Baker Mayfield




                                                                                                 All (Top)
                     Trey Lance

                 Taylor Heinicke

                  Russell Wilson

                    Zach Wilson

               Patrick Mahomes

                   Dak Prescott

                      Jared Goff

                Matthew Stafford

                  Carson Wentz

                  Ryan Tannehill




                                                                                                 All (Bottom)
                      Matt Ryan

                   Sam Darnold

                     Mike White

                   Daniel Jones

                     Tom Brady

              Ben Roethlisberger
                               −0.015      −0.010       −0.005       0.000       0.005   0.010
                                                − Q∆q   (per−frame STRAIN suppression)


                                                                    QB



Figure 6: Posterior distributions of continuous-time quarterback STRAIN suppression −Q∆    q for
the ten most and ten least suppressing passers (min 50 dropbacks). Higher values indicate slower
per-frame STRAIN growth on that quarterback’s dropbacks.


F.5   Pocket Space Control Metrics
The pocket space-control tables of Section 5 follow: the per-rusher space-won ranking and the
assignment-weighted space-generation-gain table.




                                                            26
   Name                   Space won        95% CI            Name                   Space won           95% CI
   Preston Smith             12.30     [11.80, 12.89]        Broderick Washington         9.61        [8.73, 10.68]
   Isaac Rochell             12.17     [10.64, 14.07]        Michael Hoecht               9.33         [8.80, 9.80]
   Darrell Taylor            12.17     [11.57, 12.93]        AShawn Robinson              9.14         [8.69, 9.63]
   Genard Avery              12.16     [11.00, 13.42]        Chris Jones                  9.10         [8.65, 9.57]
   John Franklin-Myers       12.13     [11.59, 12.77]        Leonard Williams             9.07         [8.71, 9.33]

                    (a) Edge                                                    (b) DT

      Name                Space won      95% CI               Name               Space won           95% CI
      Josh Tupou             8.80      [8.31, 9.24]           David Long            11.80         [10.82, 12.82]
      Raekwon Davis          8.69      [7.75, 9.65]           Elandon Roberts       11.57         [10.13, 13.11]
      Eddie Goldman          8.45      [7.94, 8.94]           Roquan Smith          11.48         [10.25, 12.64]
      Sebastian Joseph       8.41      [8.11, 8.70]           Kenny Young           11.42         [10.68, 12.19]
      Damion Square          8.41      [7.93, 8.88]           Deion Jones           11.35         [10.29, 12.48]

                        (c) NT                                                  (d) ILB




    Name                  Space won       95% CI              Name               Space won           95% CI
    Jamin Davis             11.47      [10.14, 12.86]         Jabrill Peppers       11.59         [10.02, 13.58]
    Azeez Al-Shaair         10.48       [8.78, 12.33]         Jamal Adams           11.34         [10.21, 12.79]
    Tremaine Edmunds        10.13       [8.97, 11.44]         Malcolm Jenkins       9.97           [9.01, 10.89]
    Myles Jack              10.13       [8.80, 11.40]         Chuck Clark           8.64            [7.66, 9.47]
    Shaquille Leonard       9.93        [8.96, 10.97]         Brandon Jones         8.61            [7.87, 9.42]

                    (a) MLB                                                      (b) SS

      Name               Space won      95% CI
                                                                Name            Space won           95% CI
      Jeremy Chinn         10.98      [9.37, 12.76]
      Jayron Kearse        10.79      [9.16, 12.59]             Mike Hilton       12.76          [11.06, 14.54]
      Daniel Sorensen      9.16       [8.12, 10.24]             LJarius Sneed     11.63          [10.69, 12.72]

                         (c) FS                                                 (d) CB


Table 11: Per-rusher pocket space-won (control share over the QB danger region, yd2 ; higher =
collapses more of the QB’s space), by position, bootstrap 95% CI over plays.




                                                        27
                        Name              Pos   SGG Att. PFF press +/−
                        Grover Stewart    DT 1.129 1.30     0.07   -0.17
                        Danny Shelton     NT 1.117 1.23     0.08   -0.17
                        Alim McNeill      NT 0.913 1.25     0.05   -0.19
                        Austin Johnson    NT 0.896 1.22     0.10   -0.12
                        Bryan Mone        NT 0.854 1.28     0.04   -0.24
                        Robert Nkemdiche DT 0.841 1.26      0.05   -0.12
                        Sheldon Rankins   DT 0.830 1.31     0.08   -0.11
                        Kingsley Keke     Edge 0.750 1.24   0.06   -0.19
                        Justin Hollins    Edge 0.741 0.62   0.04   -0.13
                        Dalvin Tomlinson  DT 0.723 1.11     0.12   -0.14
                        Romeo Okwara      Edge 0.713 0.76   0.21   -0.07
                        Teair Tart        DT 0.709 1.36     0.05   -0.15
                        Dorance Armstrong Edge 0.705 0.96   0.12   -0.09
                        Wyatt Ray         Edge 0.703 0.88   0.10   -0.15
                        Davon Godchaux    NT 0.700 1.26     0.04   -0.15

Table 12: Top pass rushers by Space Generation Gain (SGG). Att. is the rusher’s front-normalized
blocking attention, PFF press his own pressure rate, and +/− his plus-minus effect. The leading
generators are interior linemen.




                                                28
Acknowledgements
Big Data Bowl for publicly-available data


References
Alamar, B. and K. Goldner (2011). The blindside project: Measuring the impact of individual
  offensive linemen. Chance 24, 25–29.

Alamar, B. C. and J. Weinstein-Gould (2008). Isolating the effect of individual linemen on the
  passing game in the national football league. Journal of Quantitative Analysis in Sports 4 (2).

Atienza-Romero, A. (2026). Highest paid NFL players by position. The Big Lead. [Accessed
  24-Sep-2026].

Burke, B. (2018). We created better pass-rusher and pass-blocker stats: How they work. ESPN.com.
  [Accessed 16-May-2023].

Callister, W. D. and D. G. Rethwisch (2018). Materials science and engineering: an introduction
 (10 ed.). Hoboken, NJ: John Wiley & Sons, Inc.

Duckworth, D. pykalman 0.9.2 documentation. https://pykalman.github.io/. [Accessed 27-11-
 2023].

Fernández, J. and L. Bornn (2018). Wide open spaces: A statistical technique for measuring space
  creation in professional soccer. In Proceedings of the 12th MIT Sloan Sports Analytics Conference.

Football Outsiders (2023). Football Outsiders Glossary. footballoutsiders.com. [Accessed 21-May-
  2023].

Franks, A., A. Miller, L. Bornn, and K. Goldsberry (2015). Characterizing the spatial structure of
  defensive skill in professional basketball. The Annals of Applied Statistics 9 (1).

Hoffman, M. D. and A. Gelman (2014). The no-u-turn sampler: Adaptively setting path lengths in
  hamiltonian monte carlo. Journal of Machine Learning Research 15 (47), 1593–1623.

Howard, A., A. Blake, A. Patton, M. Lopez, T. Bliss, and W. Cukierski (2022). NFL Big Data Bowl
  2023.

Kabir, M. H., M. R. Hoque, K. Thapa, and S.-H. Yang (2016). Two-layer hidden markov model for
 human activity recognition in home environments. International Journal of Distributed Sensor
 Networks 12 (1), 4560365.

Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. Transactions of
 the ASME–Journal of Basic Engineering 82 (Series D), 35–45.

Macdonald, B. (2012). Adjusted plus-minus for nhl players using ridge regression with goals, shots,
 fenwick, and corsi. Journal of Quantitative Analysis in Sports 8 (3).

NFL Football Operations (2023a). Big Data Bowl. NFL.com. [Accessed 16-May-2023].

NFL Football Operations (2023b). NFL Next Gen Stats. NFL.com. [Accessed 16-May-2023].


                                                29
Nguyen, Q., R. Yurko, and G. J. Matthews (2023). Here Comes the STRAIN: Analyzing Defensive
  Pass Rush in American Football with Player Tracking Data. arXiv preprint arXiv:2305.10262 .

Phan, D., N. Pradhan, and M. Jankowiak (2019). Composable effects for flexible and accelerated
  probabilistic programming in NumPyro. arXiv preprint arXiv:1912.11554 .

Treacy, D. (2026). NFL sack records: Most sacks in a game, season and career in NFL history. The
  Sporting News, via Yahoo Sports. [Accessed 24-Sep-2026].




                                              30
