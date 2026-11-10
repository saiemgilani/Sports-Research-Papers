# When Should AI Overturn a Human Decision? Controversy at the 2026 World Cup and a $\sqrt{2/π}$ Solution

- arXiv: https://arxiv.org/abs/2611.11819
- Authors: Amir Ali Ahmadi, Parsa Alavi, Radeen Alavi
- Sport: Soccer; N/P/R 7/5/6 = 18/30

ML rule for when a VAR measurement should overturn a referee's offside call: reversal threshold sqrt(2/pi)*sigma_AI^2/sigma_H under Gaussian errors; closed-form, calibratable, generalizes to any human-call + AI-measurement setting.

---

                                                       When Should AI Overturn a Human
                                                                                    q  Decision?
                                                           Controversy at the 2026 World Cup and a               2/π Solution

                                            Amir Ali Ahmadi                     Parsa Alavi                            Radeen Alavi
                                            Princeton University       Algonquin Regional High School         Algonquin Regional High School
                                            aaa@princeton.edu              parsialavi@gmail.com                  radeenalavi@gmail.com


                                                                                        Abstract
arXiv:2611.11819v1 [cs.AI] 9 Nov 2026




                                                 We study how to combine a human binary call (a referee’s offside or onside decision) with an
                                             AI numerical measurement (VAR’s estimate of an attacker’s position relative to the offside line).
                                             We derive an explicit maximum-likelihood rule that determines when the referee’s call should
                                             stand and when a conflicting VAR measurement should overturn it. Our model treats the true
                                             offside margin as fixed and unknown and assumes independent additive Gaussian errors in the
                                             human’s perception and the AI measurement. When both errors have         pzero means    and known
                                                                                                                              2
                                             standard deviations σH and σAI , respectively, the reversal threshold is 2/π σAI   /σH . An onside
                                             call is overturned precisely when VAR’s measured offside margin exceeds this threshold—not
                                             merely because VAR places the attacker beyond the offside line. We also derive the rule when
                                             either source has a systematic bias. We prove that the maximum-likelihood estimate of the true
                                             margin exists and is unique, while the final binary decision requires only a threshold comparison,
                                             without computing that estimate numerically. We illustrate the rule through numerical examples
                                             and show how to estimate the error parameters from calibration data. The same analysis applies
                                             beyond soccer to binary classification problems in which a human call and an AI measurement
                                             satisfy the stated model. This paper is intended for educational purposes: we aim to illustrate
                                             how undergraduate students and advanced high school students familiar with basic probability
                                             and calculus can investigate research questions in AI and its applications.

                                        Keywords. Human–AI decision fusion, maximum likelihood, Gaussian measurement error, binary
                                        classification, probit regression, video assistant referee technology, sports analytics.


                                        1    Introduction
                                        The 2026 FIFA World Cup, unprecedented in scale, was
                                        marked by both extraordinary excitement and considerable
                                        controversy. Entire nations were lifted to their feet with last-
                                        minute goals, only for the video assistant referee (VAR) to be
                                        the bearer of disappointment at an agonizingly inconvenient
                                        time.
                                           On June 26, 2026, in the final round of group-stage matches,
                                        Iran faced Egypt in what was the most important match either
                                        of these sides had played in years. It was a simple scenario;
                                        Iran needed a win to guarantee their qualification to the Round Figure 1: The 3D reconstruction of
                                        of 32, while a tie would leave their fate up to other results Khalilzadeh’s late winner. According
                                        the next day. Egypt had already qualified to the Round of 32, to VAR, the tip of his foot was in an
                                        but a loss against Iran would put them up against a European offside position, disallowing the goal.
                                        giant as opposed to a weaker side such as Australia. In a
                                        packed Seattle Stadium, with the authors among those in attendance, both teams traded early goals

                                                                                             1
Combining a human decision and an AI measurement                                                                       2


in the first half. The game remained deadlocked into the final twenty minutes, when momentum
began to shift. Iran launched a sustained attack that forced the Pharaohs to sit in a low block
for the remainder of the game. In the 93rd minute, Iran seemed to have finally found the winner.
A free-kick from star full-back Ramin Rezaeian led to a scuffle in the box, resulting in a Shoja
Khalilzadeh goal that lifted the spirits of an entire nation. Celebrations erupted, as Iran appeared
to have made history. Yet the joy soon gave way to disappointment. After minutes of deliberation
amid Egyptian protest, the referee turned to VAR and disallowed the goal for an alleged offside1
offense [4]. Although the on-field refereeing team initially ruled the goal onside, the decision was
overturned after VAR claimed that a small part of Khalilzadeh’s foot was in an offside position at
the relevant moment. Figure 1 shows the reconstruction displayed during the review.
   This VAR decision proved costly for Iran. Their fate was now up to matches the next day, their
Round of 32 dreams dependent on at least one of the following outcomes occurring: Ghana beating
Croatia, Uzbekistan not losing to Congo, and the bout between Austria and Algeria having a winner.
According to The Athletic, “Team Melli” had a 92% chance of qualifying for the knockouts despite
their seemingly unjust draw with Egypt [5]. This probability dropped all the way down to 0% as
none of the three subsequent results went Iran’s way. One can argue that Iran’s woes could be
traced back to that decisive goal disallowance by VAR. This raises a natural question: should a
very small offside margin reported by VAR be sufficient to overturn the on-field referee’s call?
   The Iran–Egypt incident was by no means the
only VAR controversy at the 2026 World Cup.
During the Portugal-Croatia game, there were
multiple disallowed goals, the most notable of
which came in the last minutes of stoppage time.
In the 90+13th minute, Joško Gvardiol scored
to equalize for his country and force the match
into extra time. However, after lengthy delibera-
tion, Croatian player Mario Pašalić was deemed
offside during the build-up and thus the goal was
disallowed. The sequence consisted of an Ivan
                                                      Figure 2: The signal used by VAR to support
Perišić cross into the box followed by a deflection
                                                      its claim that the ball touched Matanović’s hair.
off Portuguese player Renato Veiga. The ball fell The Croatian federation filed a complaint with FIFA
to Pašalić, who failed to control it, but it bounced challenging VAR’s decision to overturn the human
off him to Gvardiol, who tapped it in. However, ruling.
before Veiga’s deflection, there was a purported
touch from Igor Matanović. At the time of this perceived touch, Pašalić was in an offside position
and subsequently became involved in the play that led to the goal. Although the alleged contact was
nearly imperceptible to viewers watching on television, the sensor within the Trionda ball registered
a signal that VAR interpreted as indicating contact with Matanović’s hair [6]. Figure 2 shows the
sensor trace displayed for this incident. More generally, such incidents illustrate that even highly
precise spatial reconstructions need not imply equally precise offside margins: in video recorded
at 30 frames per second for example, an athlete moving at 5 m/s travels about 17 cm between
consecutive frames, so even small uncertainty in the relevant contact time can be consequential.
   Disputes over whether technology presumed to be more accurate should take precedence over
human judgment are not confined to soccer. In tennis, for instance, electronic line calling has also
sparked much controversy. A recent example involved Alexander Zverev, then ranked No. 2 in the
   1
     Law 11 of the International Football Association defines an offside position by the conditions that any part of the
head, body, or feet is in the opponents’ half (excluding the halfway line) and is nearer to the opponents’ goal line than
both the ball and the second-last opponent. The hands and arms of players are not considered [3].
Combining a human decision and an AI measurement                                                           3


world. During his match against Alejandro Davidovich Fokina at the 2025 Madrid Open, Zverev
disputed an electronic line call in the second set. He pointed to the ball mark on the clay, arguing
that the line-calling technology had made an error of four to five centimeters. Umpire Mohamed
Lahyani refused to inspect the ball mark on the court because, under the electronic line-calling
rules, the electronic call took precedence. Out of frustration, Zverev retrieved his phone from his
bag and took a picture of the mark, later posting it on social media. This incident further fueled
the ongoing debate over how to resolve conflicts between human and machine refereeing systems [7].
Figure 3 shows two images associated with this incident.




Figure 3: Left: Alexander Zverev photographs a ball mark with his phone during the match to challenge an
electronic line call that ruled Davidovich Fokina’s shot in. Right: the photograph, which Zverev later posted
on Instagram to support his claim that the ball had landed out.

   The tension between human judgment and technology extends beyond sports to various other
applications of artificial intelligence (AI). In many such settings, the human provides a binary
judgment, while the AI provides a numerical measurement that can be converted into a binary
decision by comparison with a threshold. In medical diagnosis, for example, a physician may
classify a lesion as benign or malignant, while an AI system assigns it a numerical malignancy
score. In aircraft inspection, a maintenance engineer may classify a component as safe or requiring
maintenance, while an AI system produces a numerical defect-severity score. In finance, a hedge
fund manager may be bullish or bearish on a stock based on experience and judgment, while an
AI model produces a numerical estimate of its expected return. These examples share the same
information structure: a human binary judgment and an AI numerical measurement concerning the
same underlying decision.
   In this paper, we develop a maximum-likelihood model for combining human judgment and AI
measurements to estimate an unknown quantity of interest and make a final binary decision. We
assume that the correct decision is determined by the sign of a fixed, unknown scalar. The human
and AI receive noisy information about this scalar through independent additive Gaussian errors,
but only the sign of the human’s internal observation is available. We prove existence and uniqueness
of the maximum-likelihood estimate of the unknown scalar and derive an explicit rule for its sign.
The resulting decision rule combines the human binary call and the AI numerical measurement and
requires only a threshold comparison once the error parameters have been calibrated. We also show
how maximum likelihood can be used to estimate these parameters from data.
   The model applies to any binary classification problem in which the human and AI receive
noisy information about the same underlying scalar quantity and the stated error assumptions
hold. We present the model in the context of offside calls, which provided our original motivation;
the translation to other applications satisfying these assumptions is immediate. In Section 2, we
review the required probability and optimization concepts. In Section 3, we derive the model and
Combining a human decision and an AI measurement                                                            4


decision rule. In Section 4, we present numerical examples and illustrations of decision boundaries.
In Section 5, we derive the calibration procedures, and in Section 6, we summarize our conclusions.


2     Preliminaries for maximum likelihood
In this section, we review the probability and optimization concepts needed to develop the maximum-
likelihood model in the sections that follow.

2.1    The Gaussian distribution
A real-valued random variable X has a Gaussian distribution with mean m ∈ R and standard
deviation σ > 0, written X ∼ N (m, σ 2 ), if its probability density function is
                                                                !
                                       1      (x − m)2
                             fX (x) = √ exp −                       ,         x ∈ R.                     (2.1)
                                     σ 2π        2σ 2
                                                                              Rb
The density determines interval probabilities by P(a ≤ X ≤ b) =                a fX (x) dx for a ≤ b. Its mean
and variance satisfy
                       Z ∞                                     Z ∞
              E[X] =         xfX (x) dx = m,        Var(X) =            (x − m)2 fX (x) dx = σ 2 .
                       −∞                                       −∞

The standard deviation σ is the square root of the variance and has the same units as X.
  We denote the density and cumulative distribution function of N (0, 1) as
                                                                Z u
                                      1   2
                              ϕ(u) = √ e−u /2 ,        Φ(u) =             ϕ(t) dt.                       (2.2)
                                      2π                            −∞

The cumulative distribution function of X ∼ N (m, σ 2 ) is therefore
                                                         x−m
                                                                         
                                  FX (x) := P(X ≤ x) = Φ     .                                           (2.3)
                                                          σ
We will use the identities Φ(−u) = 1 − Φ(u), Φ′ (u) = ϕ(u), and ϕ′ (u) = −uϕ(u).
   Gaussian distributions are widely used in statistics and probability theory to model additive
measurement error. The central limit theorem (see, e.g., [1, Section 5.4]) provides a useful justification
for this choice. Roughly speaking, when an error is the sum of many small independent sources of
error, its distribution can often be well approximated by a Gaussian distribution. This motivates
the error model used in this paper.

2.2    Likelihood and log-likelihood
Let X denote data generated by a probability model with an unknown fixed parameter ϑ ∈ Θ,
where Θ is the parameter space. If X is discrete, let pϑ (x) = Pϑ (X = x) be its probability mass
function. If X has a probability density function, denote that function by fϑ . For an observed value
x, the likelihood function is
                                          (
                                          pϑ (x),   in the discrete case,
                              L(ϑ; x) =
                                          fϑ (x),   in the continuous case.

We hold the data x fixed and regard L(ϑ; x) as a function of ϑ. When the data points come
from independent observations, the joint likelihood is the product of their probability masses or
Combining a human decision and an AI measurement                                                           5


probability densities, as appropriate for each observation. A maximum-likelihood estimate (see,
e.g., [2, Chap. 7]) is any parameter value satisfying

                                           ϑb ∈ arg max L(ϑ; x).                                       (2.4)
                                                  ϑ∈Θ

Here arg max denotes the set of maximizers. For discrete data, maximum likelihood selects a
parameter value that assigns the largest probability to the observed data. For continuous data,
the probability of any particular observed value is zero. We instead maximize the density at that
value. When the density is continuous at the observation, the probability of a small neighborhood
is approximately the density there times the neighborhood’s volume. Thus the maximum likelihood
approach focuses on the local concentration of probability around the observed data.
   Note that the likelihood function is nonnegative. We define the log-likelihood function by
ℓ(ϑ; x) = log L(ϑ; x) when L(ϑ; x) > 0, with the convention log 0 = −∞. Since the logarithm
is strictly increasing on (0, ∞), maximizing the likelihood and maximizing the log-likelihood are
equivalent. Taking logarithms turns products into sums, which is convenient for some calculations.
All likelihoods considered below are finite and strictly positive at every admissible parameter value.

2.3    Concavity and maximization
A set C ⊆ Rn is convex if it contains the line segment between any two of its points; that is,

                        (1 − t)x + ty ∈ C       for every x, y ∈ C and t ∈ [0, 1].

A function f : C → R on a convex set C is concave if

                f ((1 − t)x + ty) ≥ (1 − t)f (x) + tf (y)   for all x, y ∈ C and t ∈ [0, 1].           (2.5)

It is strictly concave if the inequality is strict whenever x ̸= y and t ∈ (0, 1).

Proposition 2.1. A strictly concave function on a convex set has at most one maximizer.

Proof. If distinct points x and y both attained the maximum value M , strict concavity at their
midpoint would give f ((x + y)/2) > (f (x) + f (y))/2 = M , a contradiction.

   Let f be twice continuously differentiable on an open interval I. If f ′′ (x) < 0 for every x ∈ I,
then f is strictly concave [2, Section 3.1.4], and f ′ is strictly decreasing. Consequently, if f ′ (x⋆ ) = 0
at some x⋆ ∈ I, then f ′ > 0 to its left and f ′ < 0 to its right, so x⋆ is the unique maximizer on
I. Note that a strictly concave function does not necessarily have a maximizer (consider, e.g.,
f (x) = −e−x for x ∈ R). The claim is that if it has one, then the maximizer must be unique.


3     Combining the referee’s call and the AI measurement
In this section, we formulate a model for combining a human binary call with an AI numerical
measurement and derive the corresponding maximum-likelihood decision. The model applies to any
binary classification problem in which the two observations satisfy the Gaussian error assumptions
stated below. We present the derivation in the context of offside calls as a concrete example.
Combining a human decision and an AI measurement                                                                 6


3.1    The observation model
For an attacker in the opponents’ half, let θ ∈ R be the fixed, unknown true margin: the signed
longitudinal distance of the attacker’s foremost eligible body part beyond the offside line at the
relevant teammate contact. We use “offside” and “onside” for this positional classification. Positive
margins indicate offside; nonpositive margins indicate onside. Define the binary decision function
                                                (
                                                    +1,   t > 0,
                                      T (t) =                          t ∈ R.                                (3.1)
                                                    −1,   t ≤ 0,

The correct decision is T (θ); the challenge is that the exact value of θ is unknown.
   We model the referee’s perception of the true margin by an unobserved random variable XH .
Specifically, XH equals the true margin θ plus Gaussian noise with mean mH and standard deviation
σH . The referee does not explicitly compute a numerical distance; rather, XH represents the referee’s
latent internal assessment in our model. The observed human call is only the binary decision
H = T (XH ). Specifically,
                                                              2
                          XH = θ + εH ,         εH ∼ N (mH , σH ),         H = T (XH ),                      (3.2)
and only H, i.e. the referee offside/onside call, is observed.
   The AI measurement is also modeled based on additive Gaussian noise, but with a possibly
different mean and standard deviation:
                                                                          2
                                   Y = θ + εAI ,          εAI ∼ N (mAI , σAI ).                              (3.3)
We assume that the human measurement error εH and the AI measurement error εAI are indepen-
dent.2 We also assume that mH , mAI ∈ R and σH , σAI > 0 are known. Section 5 explains how these
parameters can be estimated from data. The means represent bias, and the standard deviations
represent the variability of the measurement errors. The means and standard deviations have the
same distance units as θ.
   We observe H = h ∈ {−1, +1} and Y = y ∈ R, but not XH . We refer to Y as the AI measurement
and to y as its observed value.3 Define the bias-corrected AI measurement by
                                      Z = Y − mAI ,           z = y − mAI .                                  (3.4)
                2 ), and z is the observed bias-corrected AI measurement.
Then Z ∼ N (θ, σAI

3.2    The joint likelihood
We first derive the probability mass function of the human call H. Recall that θ is the fixed true
margin. For any event A involving the random human call or AI measurement, let Pθ (A) denote the
probability that A occurs under the model when the true margin is θ. For example, Pθ (H = +1) is
the probability that the referee calls offside when the true margin is θ. From (3.2), an offside call
occurs when εH > −θ. The symmetry of the Gaussian distribution gives
                                                −θ − mH                   θ + mH
                                                                                
                            Pθ (H = +1) = 1 − Φ                        =Φ        .
                                                   σH                       σH
   2
     This assumption is reasonable when the two errors arise primarily from distinct sources, such as human visual
perception and the AI system’s sensing, modelling, and computation.
   3
     Beyond the soccer example, many AI-based binary classifiers first produce a real-valued score and then compare
that score with a threshold to make a binary decision. Examples include the output score of a neural network or the
signed distance to the separating hyperplane in a support vector machine. In such cases, the underlying numerical
score is available.
Combining a human decision and an AI measurement                                                                                      7


The complementary probability gives the onside case. Thus, for h ∈ {−1, +1},

                                                                                  h(θ + mH )
                                                                                              
                                                             Pθ (H = h) = Φ                  .                                     (3.5)
                                                                                      σH

In Figure 4, we plot the offside-call probability from (3.5) for several human error parameters.
Increasing σH makes the transition between predominantly onside and predominantly offside calls
more gradual. A nonzero mH shifts the true-margin value at which the referee is equally likely to
call onside or offside from θ = 0 to θ = −mH .
   We next consider the AI measurement. By (3.3), Y has a Gaussian distribution with mean
θ + mAI and standard deviation σAI . In view of (2.1) and (2.2), the probability density function of
Y , evaluated at the observed value y, is given by
                                                                         1    y − θ − mAI
                                                                                               
                                                             fY (y) =       ϕ             .
                                                                        σAI       σAI

   Because the measurement errors εH and εAI are independent, the human call H = T (θ + εH ) and
the AI measurement Y = θ + εAI are independent for each fixed θ. Multiplying the probability mass
of H = h by the probability density of Y at y therefore gives the joint likelihood

                                                                   h(θ + mH )        1    y − mAI − θ
                                                                                                         
                                                    L(θ; h, y) = Φ                      ϕ             .                            (3.6)
                                                                       σH           σAI       σAI
Here ϕ and Φ are the standard Gaussian probability density function and cumulative distribution
function defined in (2.2). The human factor uses Φ because only a sign is observed: we integrate the
density of XH over the half-line corresponding to the reported call. The AI factor uses ϕ because
the numerical value y itself is observed. Thus the first factor is a probability mass and the second is
a probability density. In particular, for real a ≤ b,
                                                                                     Z b
                                                        Pθ (H = h, a ≤ Y ≤ b) =            L(θ; h, y) dy.
                                                                                      a



                                            1.0
           Probability of an offside call




                                            0.8


                                            0.6


                                            0.4


                                            0.2                                                       mH = 0 cm, σH = 5 cm
                                                                                                      mH = 0 cm, σH = 10 cm
                                                                                                      mH = 5 cm, σH = 10 cm
                                            0.0
                                              −30     −20        −10            0               10              20            30
                                                                        True margin θ (cm)


Figure 4: Human offside-call probabilities from (3.5). A larger σH makes the transition more gradual. A
nonzero mH shifts the 50% crossover point from θ = 0 to θ = −mH . The parameters are illustrative.
Combining a human decision and an AI measurement                                                     8


3.3   The maximum-likelihood estimate
We now maximize the joint likelihood L(θ; h, y) in (3.6) over the true margin θ ∈ R, holding the
observed human call h and AI measurement y fixed. Recall from (3.4) that z = y − mAI is the
observed bias-corrected AI measurement. By taking the logarithm of the likelihood function in (3.6),
we can write down the log-likelihood function as
                                          √      (z − θ)2
                                                                 
                                                                   h(θ + mH )
                                                                              
                    ℓ(θ; h, y) = − log(σAI 2π) −     2    + log Φ               .                (3.7)
                                                   2σAI                σH
Our goal is to show that this function attains a unique maximum and to characterize its maximizer.
We first establish a strict-concavity property of the Gaussian cumulative distribution function that
will be useful here and again in the calibration analysis of Section 5. With ϕ(·) and Φ(·) as in (2.2),
define
                                               ϕ(u)
                                       λ(u) =       ,     u ∈ R.                                  (3.8)
                                               Φ(u)
This function is positive and finite because Φ(u) ∈ (0, 1) for every u ∈ R. The following lemma is
standard; we include a proof for completeness.
Lemma 3.1. Let Φ be the cumulative distribution function in (2.2). The function u 7→ log Φ(u) is
strictly concave on R.
Proof. Let g(u) = log Φ(u). To prove that g is strictly concave, it suffices to show that g ′′ (u) < 0
for every u ∈ R. Using the fact that Φ′ (u) = ϕ(u) and the definition of λ in (3.8), we have
          ϕ(u)
g ′ (u) = Φ(u) = λ(u). Hence, g ′′ (u) = λ′ (u). Since ϕ′ (u) = −uϕ(u),

                                   ϕ′ (u)Φ(u) − ϕ(u)Φ′ (u)
                        λ′ (u) =
                                                                            
                                                           = −λ(u) u + λ(u)   .
                                            Φ(u)2
We have λ(u) > 0, so it remains to show that u + λ(u) > 0. Since ϕ′ (t) = −tϕ(t) and ϕ(t) → 0 as
t → −∞, we have                             Z      u
                                  uΦ(u) + ϕ(u) =        (u − t)ϕ(t) dt > 0.
                                                   −∞
As Φ(u) > 0, division by Φ(u) gives u + λ(u) > 0.

Theorem 3.2 (Existence and uniqueness of the maximum-likelihood estimate). Consider the
observation model (3.2)–(3.3) with independent measurement errors εH and εAI , given means
mH , mAI ∈ R, and standard deviations σH , σAI > 0. For every observed pair (h, y) ∈ {−1, +1} × R,
there is a unique maximum-likelihood estimate θbML of the true margin θ. It is the unique solution
of the equation                                                  !
                          y − mAI − θbML      h    h(θbML + mH )
                                 2         +    λ                  = 0,                       (3.9)
                                σAI          σH         σH
where λ(·) is as in (3.8).
Proof. Let z = y − mAI . For fixed observations (h, y), differentiation of the log-likelihood function
with respect to θ gives
                                             z−θ    h    h(θ + mH )
                                                                     
                              ′
                              ℓ (θ; h, y) = 2 +       λ               ,                         (3.10)
                                              σAI  σH        σH
                                                1   1     h(θ + mH )
                                                                    
                             ℓ′′ (θ; h, y) = − 2 + 2 λ′                 < 0.                    (3.11)
                                               σAI σH         σH
Combining a human decision and an AI measurement                                                                                   9


The expression for the second derivative uses the fact that h2 = 1, and the last inequality follows
from the proof of Lemma 3.1 keeping in mind that λ′ (u) = (log Φ)′′ (u). We can therefore conclude
from (3.11) that the log-likelihood function is strictly concave.
   To prove existence of a maximizer, observe that since log Φ ≤ 0, we have
                                                                          √      (z − θ)2
                                                    ℓ(θ; h, y) ≤ − log(σAI 2π) −     2    −→ −∞              as |θ| → ∞.
                                                                                   2σAI
Choose a closed bounded interval containing zero outside which ℓ(θ; h, y) < ℓ(0; h, y). Since ℓ is
a continuous function, by the extreme value theorem, it must have a maximizer on this interval,
which is also a maximizer on R. Strict concavity of ℓ and Proposition 2.1 imply that this maximizer
must be unique. Lastly, the maximizer is the solution to ℓ′ = 0, which in view of (3.10) gives the
equation in (3.9).

  Rearranging (3.9), we have
                                                                                                         !
                                                                            2
                                                                          hσAI   h(θbML + mH )
                                                                θb
                                                                 ML = z +      λ               .                               (3.12)
                                                                           σH         σH

Since λ is positive (see (3.8)), an offside call increases the maximum likelihood estimate relative
to the bias-corrected AI measurement z, and an onside call decreases it. The quantity θbML can be
computed, e.g., by bisection [8, Lecture 7] on the strictly decreasing derivative (3.10). Note that
ℓ′ (θ) → +∞ as θ → −∞ and ℓ′ (θ) → −∞ as θ → +∞, so two points with opposite derivative signs
can always be found to serve as the initial bracket for the bisection algorithm.
    In Figure 5, we fix the observed AI measurement y and the four error parameters and plot the
log-likelihood for each human call. In this example, changing the human call changes the sign of the
unique maximizer. In the two cases, the maximum-likelihood estimate lies to the right or left of
the observed AI measurement by unequal amounts. The intuition is that an agreeing human call
provides relatively little additional information because such a call was already likely at values near
the AI measurement. By contrast, a disagreeing human call is more informative because it is less
likely under those same values, causing the likelihood to shift farther to accommodate it.

                                                                      ̂                  ̂
                                                                     θML = −0.37       θML = 1.70
            Log-likelihood minus its maximum




                                                0



                                               −2



                                               −4



                                               −6
                                                                                   Human call: onside
                                                                                   Human call: offside

                                                −4             −2              0               2               4           6
                                                                          Candidate true margin θ (cm)


Figure 5: Log-likelihoods for y = 1 cm, mH = mAI = 0, and σH = σAI = 2 cm. Each curve has been shifted
to have maximum zero. Changing the human call changes the sign of θbML even though the observed AI
measurement is unchanged.
Combining a human decision and an AI measurement                                                       10


3.4   The maximum-likelihood decision
Recall that θbML is the unique maximum-likelihood estimate of the true margin θ, and is characterized
by (3.9). We define the maximum-likelihood decision to be T (θbML ), where T is the binary decision
function in (3.1). This will be our final decision obtained by combining the referee’s call with the
AI measurement: our call will be offside if T (θbML ) = 1, and onside if T (θbML ) = −1. We next show
that this decision can be obtained without computing the numerical value of θbML .
   In the following proposition, h ∈ {−1, 1} is the observed human call, y ∈ R is the observed AI
measurement, and mH , mAI , σH , σAI are the error parameters in (3.2)–(3.3). The functions ϕ(·) and
Φ(·) are defined in (2.2).
Proposition 3.3 (Maximum-likelihood decision rule). Under the assumptions of Theorem 3.2, the
maximum-likelihood decision is offside if and only if
                                                   2 ϕ(hm /σ )
                                                 hσAI    H   H
                                     y − mAI +                   > 0.                              (3.13)
                                                  σH Φ(hmH /σH )

Proof. The maximum-likelihood decision is offside if θbML > 0 and onside if θbML ≤ 0. For the
log-likelihood ℓ(θ; h, y) in (3.7), the derivative with respect to θ is given by (3.10). From the proof
of Theorem 3.2, we see that ℓ′ is strictly decreasing and vanishes at θbML . Hence,

                                     θbML > 0     ⇐⇒        ℓ′ (0; h, y) > 0.
                                              2 gives (3.13).
Evaluating (3.10) at zero and multiplying by σAI

   For h ∈ {−1, +1}, define the positive, referee-call-dependent threshold

                                                σ2    hmH
                                                                 
                                            ch = AI λ     ,                                        (3.14)
                                                 σH    σH
where λ(·) is as in (3.8). Recall that z = y − mAI is the observed bias-corrected AI measurement.
The maximum-likelihood decision rule declares offside when z + hch > 0. Thus, following a human
offside call, the final decision is offside if z > −c+1 , whereas following a human onside call, the final
decision is offside if z > c−1 . The two thresholds c+1 and c−1 can be computed offline.
   As a sanity check, consider the case where mH > 0, which corresponds to a referee who may be
somewhat biased to call offside. Then, m              mH
                                               σH > − σH . Since λ is strictly decreasing (see the proof
                                                 H
                                              
of Lemma 3.1), we have λ m    H
                             σH   < λ −m σH , and therefore c+1 < c−1 . Hence, when the referee is
                                          H


biased toward offside, the AI evidence required to overturn a human onside call in favor of offside is
stronger than the AI evidence required to overturn a human offside call in favor of onside.

3.5   The special case of zero means
We now specialize the referee-call-dependent thresholds c+1 and c−1 from (3.14) to the prominent
case where mH = mAI = 0. The observed bias-corrected AI p  measurement z = y − mAI then equals
the observed AI measurement y. Since λ(0) = ϕ(0)/Φ(0) = 2/π, the two thresholds reduce to
                                                               2
                                                        r
                                                            2 σAI
                                                cML =             .                                (3.15)
                                                            π σH
Therefore, the maximum-likelihood decision is offside if and only if

                                                z + hcML > 0.                                      (3.16)
Combining a human decision and an AI measurement                                                    11


Note that both z and cML have units of distance. If hz ≥ 0, the human call is retained. If hz < 0,
the human call and AI measurement disagree, and we proceed as follows:

                            |z| > cML    =⇒     overturn the human call,
                                                                                                 (3.17)
                            |z| < cML    =⇒     retain the human call.

At |z| = cML in a disagreement, the final decision is onside. This retains an onside call and overturns
an offside call.
   It is intuitive that increasing σAI raises the threshold cML , since a noisier AI requires stronger
evidence to overturn the human call, whereas increasing σH lowers cML because a noisier human
call should be easier to overturn. The different powers of σAI and σH in cML come from the two
likelihood terms: differentiating the Gaussian log-density for the AI measurement introduces a
factor 1/σAI2 , whereas differentiating the log Gaussian tail probability for the human call introduces

a factor 1/σH , as seen in (3.10).

Decision error probabilities. Recall the definition of the binary decision function T (·) from (3.1).
We now compare, under our model, the probabilities that the maximum-likelihood decision rule
T (θbML ), the human call H, and the AI decision T (Y ) make an incorrect decision, i.e., a decision
different from T (θ).
    Let us continue with the case mH = mAI = 0. For a fixed true margin θ > 0, an erroneous
maximum-likelihood onside decision occurs when H = +1 and Z ≤ −cML , or when H = −1 and
Z ≤ cML . Here, Z (which equals Y since mAI = 0) is the bias-corrected AI measurement in (3.4)
and cML is the threshold in (3.15). Independence of the human and AI measurement errors, ϵH and
ϵAI , gives
                                                     θ      −θ − cML
                                                                  
                                              
                          Pθ T (θML ) ̸= T (θ) = Φ
                                b                        Φ
                                                    σH        σ
                                                             AI
                                                         θ     cML − θ
                                                                      
                                                 +Φ −       Φ            .
                                                        σH       σAI
For θ < 0, by symmetry, we get the same expression with θ replaced by |θ|. Lastly, at θ = 0, the
error probability is 1/2.
   The human call and AI decision separately have error probabilities Φ(−|θ|/σH ) and Φ(−|θ|/σAI ).
Figure 6 compares these probabilities when σH = σAI = 2 cm. At |θ| = 2 cm, the maximum-
likelihood decision has error probability approximately 9.70%, compared with 15.87% for either
source alone. These probabilities average over all observations at a fixed true margin, not only
disagreements.
Combining a human decision and an AI measurement                                                                             12



                                 50                                                 Human call H or AI decision T(Y)
                                                                                    Maximum-likelihood decision T( ML)
                                 40
         Error probability (%)
                                 30

                                 20

                                 10

                                 0
                                      0             1            2           3             4             5               6
                                                               True margin magnitude | | (cm)
Figure 6: Decision error probabilities for mH = mAI = 0 and σH = σAI = 2 cm. The human call H and the
AI decision T (Y ) have the same error probability.


4     Numerical examples and decision boundaries
In this section, we illustrate the maximum-likelihood decision rule with a few numerical examples
and describe the boundaries between retaining and overturning the human call.

4.1   Examples with zero and nonzero means
                                                                            2 /σ from (3.15). Let
                                                                                                   p
Example 1 (Zero means). Recall the zero-mean threshold cML = 2/π σAI            H
mH = mAI = 0, σH = 10 cm, and σAI = 2 cm. Then cML ≈ 0.3192 cm. The observed bias-corrected
AI measurement z = y − mAI equals y in this case. Table 1 shows that a conflicting measurement
of magnitude 0.20 cm retains the human call, whereas a magnitude of 0.50 cm overturns it. The
estimates are computed from (3.9); their signs follow directly from (3.16).

Table 1: Maximum-likelihood decisions for mH = mAI = 0, σH = 10 cm, and σAI = 2 cm. Numerical
estimates are rounded to four decimal places.

                                          Human call       z (cm)   θbML (cm)     Final decision    Action
                                          Offside          −0.20      0.1162      Offside           Retain
                                          Offside          −0.50     −0.1763      Onside            Overturn
                                          Onside            0.20     −0.1162      Onside            Retain
                                          Onside            0.50      0.1763      Offside           Overturn



Example 2 (Unequal means). We next show how unequal error means affect the maximum-
likelihood decision. In the human model, a negative mH can represent a reluctance to call offside in
a tense situation, whereas a positive mH represents a tendency to call offside. Keep σH = 10 cm
and σAI = 2 cm, but set mH = 5 cm and mAI = 0. The thresholds (3.14) become

                                                        c+1 ≈ 0.2037 cm,        c−1 ≈ 0.4564 cm.
Combining a human decision and an AI measurement                                                                                  13


An offside call with y = −0.30 cm is overturned, but an onside call with y = 0.30 cm is retained.
Equal conflicting magnitudes have different effects because the human bias makes the thresholds
asymmetric.
   To isolate the effect of AI bias, instead set mH = 0 and mAI = 1 cm, keeping the same standard
deviations. Since mH = 0, the two thresholds in (3.14) are equal to cML in (3.15). For h = +1 and
y = 0.50 cm,
                             z + cML = y − mAI + cML ≈ −0.1808 cm < 0.
The maximum-likelihood decision is onside. Omitting the known AI bias would produce an offside
decision for the same observations.

4.2   Decision boundaries
We next visualize the boundary between retaining and overturning the human call. Suppose that
both means are zero and that the observed bias-corrected AI measurement z = y conflicts with
the human call, so hz < 0. Let cML be the threshold in (3.15). For a fixed magnitude |z| > 0, the
boundary |z| = cML can be written as
                                                                              1/4 q
                                                                              π
                                                                     σAI =                |z|σH .                               (4.1)
                                                                              2
Figure 7 plots this boundary in the (σH , σAI ) plane for four magnitudes of the conflicting AI
measurement: |z| = 0.05, 0.10, 0.20, and 0.40 cm. For a given curve, a point below it satisfies
|z| > cML and therefore overturns the human call. A point above it retains the call. Increasing |z|
raises the boundary and enlarges the overturning region.

                                          4.0       |z| = 0.05 cm                      Retain above the selected curve
                                                    |z| = 0.10 cm
         AI standard deviation σAI (cm)




                                          3.5
                                                    |z| = 0.20 cm

                                          3.0       |z| = 0.40 cm


                                          2.5

                                          2.0

                                          1.5

                                          1.0

                                          0.5                                          Overturn below the selected curve

                                          0.0
                                                0         5           10          15           20                 25       30
                                                                    Human standard deviation σH (cm)


Figure 7: Decision boundaries for |z| = 0.05, 0.10, 0.20, and 0.40 cm, with both means zero and hz < 0.
For each curve, we overturn the human decision below the curve and retain it above.

  Allowing the conflicting AI measurement magnitude |z| to vary gives the surface
                                                                                         2
                                                                                  r
                                                                                      2 σAI
                                                                          |z| =                                                 (4.2)
                                                                                      π σH
in Figure 8. Points above the surface overturn the human call; points below retain it. A horizontal
slice at a fixed |z| gives the corresponding two-dimensional boundary (4.1).
Combining a human decision and an AI measurement                                                        14




                                                                                     16


                                                                                     12




                                                                                            |z| (cm)
                                                                                     8


                                                                                     4


                                                                                  0
                                                                                 10
              5                                                           8

                          10                                        6
                                                                                 )
                                                                4            m
                            σH (         15                              I
                                                                           (c
                                   cm)                      2       σA
                                                     20

Figure 8: The decision boundary in (4.2). Both means are zero, and hz < 0. Above the surface, we overturn
the human decision; below it, we retain it. On the surface, the estimated true margin is zero and the final
decision is onside.


5    Maximum-likelihood calibration
The observation model (3.2)–(3.3) depends on four parameters: the human error mean mH and
standard deviation σH , and the AI error mean mAI and standard deviation σAI . In this section,
we show how to estimate these parameters from calibration data. The same maximum-likelihood
framework used above can also be used for this purpose once reference margins are available.
   For our running offside example, calibration data could be obtained from controlled plays or
reconstructed incidents for which the player positions and contact times are known. The human
calibration sample would record the referee’s binary call at each known true margin, while the AI
calibration sample would record the corresponding numerical measurement. The two procedures
need not use the same observations or the same sample size. More generally, depending on the
application, the true margin may become observable after the relevant outcome is realized, or it
may be measured during calibration using a higher-fidelity and more costly reference technology
that need not be deployed in routine operation.
   The first situation arises naturally in finance. For example, a hedge fund manager may predict
whether a stock will outperform or underperform a benchmark over a specified horizon, while an AI
model produces a numerical prediction of the stock’s excess return. Once the horizon has elapsed,
the realized excess return provides the true margin: its sign determines the correct binary decision,
while its magnitude measures the extent of outperformance or underperformance. Repeating this
process across stocks and time periods provides calibration data for estimating the human and AI
error parameters.
Combining a human decision and an AI measurement                                                         15


5.1    AI parameters
We collect n ≥ 2 calibration records

                                          (θi , yi ),          i = 1, . . . , n,                       (5.1)

where θi is a fixed, known reference margin and yi is the observed AI measurement. We assume
that the AI measurement errors yi − θi , i = 1, . . . , n, are independent and identically distributed
                       2 ). The following derivation is standard; we include it for completeness.
according to N (mAI , σAI
   Define the observed AI residuals by ei = yi − θi , for i = 1, . . . , n. The likelihood of the observed
residual sample, as a function of mAI and σAI , and its log-likelihood are
                                        n
                                          1    ei − mAI
                                        Y                              
                   LAI (mAI , σAI ) =        ϕ          ,                                              (5.2)
                                         σ
                                      i=1 AI
                                                  σAI
                                                                   n
                                                   n          1 X
                    ℓAI (mAI , σAI ) = −n log σAI − log(2π) − 2       (ei − mAI )2 .                   (5.3)
                                                   2         2σAI i=1

Our goal is to find values for mAI ∈ R and σAI > 0 that maximize ℓAI (or equivalently LAI ). Let
e = n1 ni=1 ei . The identity
      P

                             n
                             X                          n
                                                        X
                                               2
                                    (ei − mAI ) =             (ei − e)2 + n(mAI − e)2
                              i=1                       i=1

shows that, for every fixed σAI > 0, the unique maximizing mean is mAI = e. Let S = ni=1 (ei − e)2 ,
                                                                                              P

and note that S > 0 when not all sample errors are identical. It is straightforward to verify that
                                         d                         2
                                                             S − nσAI
                                             ℓAI (e, σAI ) =     3    .                                (5.4)
                                        dσAI                   σAI
                                          p                                            p
This derivative is positive for σAI < S/n and negative for σAI > S/n. Hence, with S > 0, the
unique maximum-likelihood estimates are the following intuitive quantities:
                                                                    n
                                                                                   !1/2
                                                                 1X
                               m
                               b AI = e,           σ
                                                   bAI =               (ei − e)2          .            (5.5)
                                                                 n i=1

The estimated mean is the average difference between the AI measurement and the reference margin,
so it measures the AI’s systematic bias. The estimated standard deviation is the root mean squared
deviation of these residuals from their average, so it measures their variability after removing the
estimated bias.

5.2    Human parameters
We collect n ≥ 2 calibration records (θi , hi ), for i = 1, . . . , n, where θi is a fixed, known reference
margin and hi ∈ {−1, +1} is the observed human call. For reliable estimation, the calibration sample
should include reference margins near the transition region, where both onside and offside calls
occur. We assume that the underlying human measurement errors in these records are independent
and identically distributed according to N (mH , σH   2 ). The internal human measurements X
                                                                                                     H,i are
unobserved. By (3.5), the likelihood of the observed human calls is
                                                         n
                                                                       hi (θi + mH )
                                                         Y                        
                                    LH (mH , σH ) =            Φ                     .                 (5.6)
                                                         i=1
                                                                             σH
Combining a human decision and an AI measurement                                                                    16


The maximum-likelihood problem of interest is therefore
                                                                 n
                                                                                    hi (θi + mH )
                                                                 X                              
                             maximize        ℓH (mH , σH ) :=          log Φ                      .              (5.7)
                            mH ∈R, σH >0
                                                                 i=1
                                                                                          σH

It is convenient to introduce the one-to-one reparameterization:
                                   mH                1                              α            1
                             α=       ,        β=      > 0,            mH =           ,   σH =     .             (5.8)
                                   σH               σH                              β            β
The equivalent problem becomes
                                                                n
                                                                X                            
                                 maximize ℓeH (α, β) :=               log Φ hi (α + βθi ) .                      (5.9)
                                  α∈R, β>0
                                                                i=1

In this parameterization, the probability of an offside call at the known reference margin θi is
Φ(α + βθi ). A binary-response model of this form is called probit regression. Problem (5.9) estimates
its two coefficients by maximum likelihood, with β > 0 required by the fact that σH > 0.
   Unlike the AI calibration problem, the human calibration problem does not generally admit
closed-form maximum-likelihood estimates. Nevertheless, its optimization structure is particularly
simple. It follows from Lemma 3.1 that log Φ is a concave function. Each summand in (5.9) is log Φ
composed with an affine function and is therefore concave [2, Chapter 3]. Hence, ℓeH is concave on
R × (0, ∞). If the calibration sample contains at least two distinct reference margins, then ℓeH is
strictly concave. Indeed, for two distinct parameter pairs (α1 , β1 ) and (α2 , β2 ), the affine values
α1 + β1 θi and α2 + β2 θi cannot agree at two distinct values of θi unless the two parameter pairs
coincide. Thus, at least one summand satisfies a strict concavity inequality, while all satisfy a
nonstrict one. Proposition 2.1 then implies that any maximizer of (5.9) must be unique.4
   The requirement of distinct reference margins is important for identifying both parameters. If
every reference margin equals θ0 , then the likelihood depends on (α, β) only through α + βθ0 , or
equivalently on (θ0 + mH )/σH , and the two human error parameters cannot be identified separately.
   Problem (5.9) is a two-dimensional convex optimization problem and can be solved numerically
using standard algorithms for convex optimization [2, Chapters 9–11]. Since the feasible set R×(0, ∞)
is open, any maximizer (α,b β)
                            b must satisfy the first-order conditions

                                                  n
                                          ∂ ℓeH X                      
                                               =     hi λ hi (α
                                                              b + βθ
                                                                  b i ) = 0,                                    (5.10)
                                          ∂α     i=1
                                                  n
                                          ∂ ℓeH X                         
                                               =     hi θi λ hi (α
                                                                 b + βθ
                                                                     b i ) = 0,                                 (5.11)
                                          ∂β     i=1

where λ(·) is as in (3.8). Therefore, one can also solve these two nonlinear equations in the two
unknowns α b and βb directly. Under the distinct-margin condition above, any solution (α,
                                                                                        b β)
                                                                                          b with
β > 0 is the unique maximizer of (5.9). We then recover the human error parameters as
b

                                                       α
                                                       b                   1
                                                m
                                                bH =        ,     σ
                                                                  bH =          .                               (5.12)
                                                       βb                  βb
   4
                                                                                              P I+ = {i :
    One can show that under reasonable assumptions, existence of a maximizer is guaranteed. Let
hi = +1} and I− = {i : hi = −1}, and suppose that both sets are nonempty. Define θ̄+ = |I+ |−1 i∈I+ θi and
θ̄− = |I− |−1
                P
                i∈I−
                       θi . A sufficient condition for the existence of a maximizer of (5.9) is mini∈I+ θi < maxi∈I− θi
and θ̄+ > θ̄− . This means that there should be some overlap between the two types of calls, but offside calls should
nevertheless occur at larger reference margins on average than onside calls.
Combining a human decision and an AI measurement                                                           17


6    Summary and conclusions
We have developed a maximum-likelihood model for combining a human binary call with an AI
numerical measurement under independent Gaussian measurement errors. We showed that the
log-likelihood has a unique maximizer and that its derivative at zero determines the sign of this
maximizer. The resulting decision therefore requires a threshold comparison rather thanp numerical
optimization for each incident. When both error means are zero, the threshold is 2/π σAI      2 /σ ;
                                                                                                   H
nonzero means give call-dependent thresholds and an explicit correction to the AI measurement.
   We also derived maximum-likelihood calibration procedures for the four error parameters. The
AI parameters have closed-form estimates, while the human parameters are obtained from a two-
dimensional concave maximization problem. These procedures require numerical reference margins,
but they do not require access to the human’s internal measurements. Although we used offside
calls to present the analysis throughout the paper, the same derivation applies whenever the human
reports a binary decision about an underlying scalar quantity and the AI provides a numerical
measurement of that same quantity. A promising direction for future work is to quantify the empirical
impact of the proposed maximum-likelihood procedure on decision accuracy in applications where
the model can be readily calibrated, such as finance, medical imaging, and prediction markets.


Acknowledgments
Parsa and Radeen Alavi are grateful to their grandmother, Maryam Dara, for her support and
encouragement throughout this project. The authors acknowledge the use ofpChatGPT for generating
figures, additional proofreading, and sanity checks, while following their 2/π rule to ensure that
AI did not overturn their human judgment. They take full responsibility for the content.


References
 [1] D. P. Bertsekas and J. N. Tsitsiklis, Introduction to Probability, 2nd ed., Athena Scientific, Belmont,
     MA, 2008. https://www.mit.edu/~dimitrib/probbook.html.
 [2] S. Boyd and L. Vandenberghe, Convex Optimization, Cambridge University Press, Cambridge, 2004.
     https://web.stanford.edu/~boyd/cvxbook/.
 [3] The International Football Association Board, Laws of the Game, Law 11: Offside, online edition,
     accessed October 25, 2026. https://www.theifab.com/laws/latest/offside/.
 [4] S. Tobin, Iran wait on World Cup progress after late goal disallowed in Egypt draw, Reuters, June 27,
     2026. Online report.
 [5] The Athletic, 2026 FIFA Men’s World Cup third-place tracker. https://www.nytimes.com/athletic
     /interactive/fifa-mens-world-cup-2026-tracker/third-place-tracker/.
 [6] Y. Arya, FIFA defend VAR decision to disallow Croatia’s stoppage time equaliser for hair flick as
     Portugal go through, Goal, July 3, 2026. https://www.goal.com/en/lists/fifa-defend-var-croat
     ia-goal-disallowed-portugal-world-cup/bltc7118fa3e7cbdffb.
 [7] Reuters, The camera never lies: Electronic line calls in focus again as Zverev takes photo of ball mark,
     Malay Mail, April 28, 2025.
     https://www.malaymail.com/news/sports/2025/04/28/the-camera-never-lies-electronic-l
     ine-calls-in-focus-again-as-zverev-takes-photo-of-ball-mark/174771.
 [8] A. A. Ahmadi, Lecture notes on computing and optimization, Princeton University, Fall 2025.
     https://aaa.princeton.edu/orf363.
