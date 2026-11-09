# Competitive Balance Beyond Standings: Bayesian Inference for Latent Tiers and Structural Heterogeneity

- arXiv: https://arxiv.org/abs/2611.08856
- Authors: Guanyu Hu

---

                                              Competitive Balance Beyond Standings: Bayesian Inference for
                                                       Latent Tiers and Structural Heterogeneity
                                                                                    Guanyu Hu
                                                                       Department of Statistics and Probability
                                                                             Michigan State University
                                                                                huguanyu@msu.edu
arXiv:2611.08856v1 [stat.ME] 6 Nov 2026




                                                                                          Abstract
                                                   Competitive balance has long been a central concern in sports economics, tied to outcome
                                               uncertainty, fan engagement, and the way leagues design their policies. Most existing measures of
                                               competitive balance are built from standings or winning percentages, which say little about how
                                               overall parity relates to the way teams sort into latent competitive tiers. We propose a Bayesian
                                               framework based on the Bradley–Terry model that jointly estimates the number of competitive
                                               tiers and team memberships. To capture the overall degree of competitive heterogeneity, we
                                               introduce a structural balance parameter defined on the unit interval within a hierarchical
                                               model, and we establish theoretical results giving this parameter a clear interpretation: it is
                                               directly tied to the separation between tiers, and overall heterogeneity depends on both the
                                               size and frequency of cross-tier differences. Importantly, structural balance is distinct from the
                                               information content of the schedule itself, so leagues with different numbers of teams and games
                                               can be compared on equal footing. Inference is carried out with an efficient posterior sampling
                                               algorithm that jointly handles team abilities, tier structure, home advantage, and structural
                                               balance. Simulation studies validate the proposed method, showing accurate recovery of the
                                               latent competitive structure and correct performance of the structural-balance testing procedure.
                                               Applied to the NBA and NFL, it reveals that the two leagues exhibit similar global structural
                                               balance despite very different competitive organizations: the NBA has three latent tiers, while
                                               the NFL has two broader ones, and the NFL’s sparser schedule produces considerably more
                                               posterior uncertainty. Overall parity, it turns out, can mask quite different forms of competitive
                                               stratification—something standings-based measures alone cannot detect.

                                          Keywords: Bayesian nonparametrics; Bradley–Terry model; pairwise comparison; sports analyt-
                                          ics.


                                          1    Introduction
                                          Competitive balance sits at the heart of professional sports leagues and has long occupied sports
                                          economists and league managers. Teams closely matched in underlying strength make for less
                                          predictable outcomes and seasons that stay meaningful into their final weeks, and that unpre-
                                          dictability is a large part of what keeps fans engaged — engagement that, in turn, underwrites
                                          much of a league’s commercial value. Persistent gaps in team quality work the opposite way: they
                                          harden into a hierarchical structure where a handful of clubs dominate and the uncertainty of
                                          outcome that draws fans in the first place starts to erode. That’s why competitive balance comes
                                          up so often in debates over league governance, talent allocation, revenue sharing, and the long-run
                                          sustainability of competition. Leagues have responded with an array of parity-promoting poli-
                                          cies, including player drafts, salary caps, luxury taxes, revenue sharing, and schedule design, and

                                                                                               1
much of the classical literature in sports economics examines these instruments in exactly this light
(Vrooman, 1995; Fort and Quirk, 1995; Szymanski, 2001, 2003; Zimbalist, 2002; Fort and Maxcy,
2003). Measuring competitive balance well matters for a reason beyond description: it’s how we tell
whether these policies are actually delivering the parity they’re designed to produce. The standard
toolkit for measuring competitive balance, which includes the dispersion of winning percentages,
concentration indices, and related measures (Utt and Fort, 2002; Owen et al., 2007; Manasis et al.,
2013; Manasis and Ntzoufras, 2014; Manasis et al., 2022), summarizes realized outcomes well. But
it has two real limitations. It mixes persistent differences in underlying team strength with plain
game-level noise, and it says almost nothing about how teams sort into latent competitive groups
or how uncertain that grouping itself is. As a result, two leagues can look equally balanced on
paper while their underlying competitive organization differs substantially, and what looks like a
difference in standings may just reflect how much schedule information each league happens to
provide.
    A related but distinct feature of league competition is the presence of competitive tiers. Teams
need not fall into clearly distinguishable positions along a complete ranking — several clubs may
simply be of comparable latent strength and together form a common competitive level. That
means competitive balance and competitive stratification capture different things: two leagues can
show similar overall heterogeneity while organizing teams into very different numbers of tiers, and
two leagues with the same number of tiers can still differ sharply in how far apart those tiers sit.
We treat these as separate inferential problems.
    Basini et al. (2023) make the value of latent grouping concrete, using a Bayesian stochastic block
model to trace more than four decades of English football and showing how shifts in the number,
sizes, and interaction patterns of latent groups surface features of competition that conventional
balance indices miss. The natural home for this kind of question is the Bradley–Terry–Luce model
(Bradley and Terry, 1952; Luce, 1959), which represents game outcomes through differences in
latent ability and underlies a large literature on sports ranking, forecasting, Bayesian inference,
and scalable computation (Davidson, 1970; Glickman, 1999; Hunter, 2004; Caron and Doucet,
2012; Mollica and Tardella, 2021; Tian et al., 2024; Pearce and Erosheva, 2025b). But the standard
version of that model assigns every competitor a continuous latent ability, so no two competitors
ever share a strength level with positive probability — every team is distinguishable from every
other whether or not that distinction means anything.
    Several lines of work relax this. The ranking lasso groups Bradley–Terry effects through pe-
nalized fusion (Masarotto and Varin, 2012); a separate body of Bayesian and mixture-based work
handles clustered rankings, partial orders, and related structures more generally (Marden, 1996;
Murphy and Martin, 2003; Busse et al., 2007; Dunson and Peddada, 2008; Deng et al., 2014; Li
et al., 2022). Two recent papers push this further by inferring latent rank groups directly: Pearce
and Erosheva (2025a) propose a rank-clustering Bradley–Terry–Luce model that jointly estimates
the number and memberships of latent rank clusters, and Santi and Friel (2026) combine paired-
comparison ranking with latent block structure to recover tied competitive levels.
    What none of this tells you is how far apart the tiers actually are. A league could have three
tightly bunched tiers and a league could have two tiers separated by a canyon, and a method
built to answer ”who belongs together” has no way to distinguish those two situations — yet they
represent very different competitive environments. That’s the gap we’re after: we infer the tiers,
but we also put a number on how much separation exists between them, on a scale that lets you
compare that separation across leagues regardless of how many tiers or teams each one has.
    We develop a Bayesian extension of the Bradley–Terry model that studies competitive tier
structure and global structural balance jointly. A mixture of finite mixtures prior (Miller and Har-
rison, 2018) is placed on team abilities, so the number of occupied tiers and their memberships

                                                  2
are both learned from the observed games. Our work builds on recent approaches that char-
acterize competitive structure through latent groups: Bayesian stochastic block models describe
competition through the number, composition, and interaction patterns of latent blocks (Basini
et al., 2023), spike and slab fusion priors identify competitors with tied latent ranks (Pearce and
Erosheva, 2025a), and Bradley–Terry stochastic block models jointly infer tied rank groups, their
strengths, and their memberships (Santi and Friel, 2026). These methods describe how competitors
are grouped, but the grouping alone does not say how strongly the resulting competitive levels are
separated. A league with several closely spaced tiers can be more balanced than one with only two
tiers sitting far apart. We therefore introduce a global structural balance parameter that measures
the dispersion of tier-specific abilities separately from the latent partition. The partition cap-
tures competitive stratification, while the balance parameter quantifies how large the heterogeneity
among tiers actually is, which gives a common scale for comparing leagues with very different com-
petitive structures. Our theoretical development makes this distinction precise. We characterize
the balance parameter through the exact distribution of average between-tier separation, and we
show that team-level heterogeneity decomposes into the magnitude of between-tier differences and
the prevalence of cross-tier pairs. Greater structural balance, we further show, corresponds to fewer
practically distinguishable competitive levels at a fixed resolution, which clarifies why tier count
by itself is not an adequate measure of balance. The common scale also lets us move beyond de-
scriptive comparison. We develop Bayesian procedures for comparing structural balance between
systems directly, including directional posterior probabilities and practical-equivalence assessments,
even when the systems differ in their numbers of teams and comparison designs. Since leagues also
differ markedly in their schedules, we study identification under incomplete comparison graphs and
separate the underlying structural quantity from the amount of information available to estimate
it. Posterior computation combines the MFM representation with Pólya–Gamma augmentation
(Polson et al., 2013) and jointly propagates uncertainty in team abilities, tier memberships, home
advantage, structural balance, and cross-league comparisons. Our application to the NBA and
NFL shows why both the measure and the comparison procedure matter. Despite very different
observed standings and schedule densities, the posterior analysis offers little directional evidence
that either league is globally more balanced, which points to similar levels of structural balance.
The latent competitive organizations are nonetheless quite different: the NBA has three compet-
itive tiers, while the NFL has two broader ones. The NFL’s much sparser schedule also leads to
greater posterior uncertainty, both in league-specific inference and in the cross-league comparison.
Similar overall parity, it turns out, can coexist with different forms of competitive stratification,
and formal uncertainty quantification can separate genuine differences in structural balance from
differences that merely reflect schedule information.
    The remainder of the paper is organized as follows. Section 2 introduces the mixture of finite
mixtures model for team abilities, defines the balance parameter B, and describes the MCMC
algorithm used for posterior sampling and post MCMC inference procedure. Section 3 develops
the theoretical results behind B, and Section 4 turns that interpretation into a practical procedure
for comparing balance across two systems. Section 5 reports extensive simulations that check
recovery and the comparison procedure under schedules of varying density, and Section 6 applies
the framework to the NBA and NFL. We conclude in Section 7 with a summary of the findings
and directions for future work.




                                                  3
2     Methodology
2.1    Paired comparisons and latent tier structure
Let i = 1, . . . , n index observational units and e = 1, . . . , M index paired comparisons. For com-
parison e, let ae and be denote the two participating units, and let Ye = 1 if unit ae is preferred to
unit be and Ye = 0 otherwise. We assume the Bradley–Terry model (Bradley and Terry, 1952)

                       Ye | θ, h ∼ Bernoulli(pe ),         logit(pe ) = θae − θbe + h,              (1)

where θi is the latent ability of unit i. The parameter h represents a systematic first-position effect,
with h ∼ N (0, σh2 ) when estimated and h = 0 under a symmetric comparison design.
   The comparison structure can be represented by an oriented incidence matrix. Let qe ∈ Rn
contain a 1 in position ae , a −1 in position be , and zeros elsewhere, and define

                                           QM = (q1 , . . . , qM )⊤ .

Then the linear predictor is qe⊤ θ + h. This representation connects identifiability of the latent
effects to the comparison graph and its incidence matrix (Dong et al., 2026).
    We assume that units with comparable latent abilities may share a common tier. Let K denote
the nominal number of mixture components and assign the mixture-of-finite-mixtures prior (Miller
and Harrison, 2018)
                                   K ∼ 1 + Poisson(λK ),
                                 π | K ∼ Dirichlet(γ, . . . , γ),                                   (2)
                              zi | π, K ∼ Categorical(π),               θi = µzi .
    Conditional on a global precision parameter ϕ,

                                              τ02
                                                 
                                      iid
                            µk | ϕ, K ∼ N 0,        ,            k = 1, . . . , K,                  (3)
                                               ϕ

where τ0 > 0 is a fixed reference scale.
   Let
                                             P = {C1 , . . . , CT }
denote the occupied partition after empty mixture components are removed, with T = |P|. Thus
T is the number of occupied tiers and P determines their memberships. Mixture labels have no
substantive meaning and no ordering constraint is imposed during posterior sampling.
   For a fixed partition, let ZP be the n × T membership matrix and define

                                               DP = QM ZP .

Then
                                  θ = ZP µ,           ψ = DP µ + h1M .
For a connected comparison graph, rank(DP ) = T − 1, so the occupied tier effects are identifiable
up to a common location. A precise rank condition is given in Section 3.1.




                                                       4
2.2    Structural balance
We assign
                                        ϕ ∼ Gamma(aϕ , bϕ ),
using the shape-rate parameterization, and define
                                 ϕ                 B
                           B=       ,       ϕ=        ,           0 < B < 1.                    (4)
                                1+ϕ               1−B
The parameter B measures the global magnitude of structural balance. Larger values of B imply
greater precision and hence smaller separation among the latent tier effects.
   For two distinct tiers c and d,
                                                             
                                                      21 − B
                                 µc − µd | B ∼ N 0, 2τ0         ,
                                                          B

and therefore
                                                         1−B
                                E (µc − µd )2 | B = 2τ02
                                   
                                                             .
                                                          B
   For T ≥ 2, define the average squared separation
                                             2     X
                                  DT =              (µc − µd )2 .                               (5)
                                         T (T − 1)
                                                      c<d

Then
                                                        1−B
                                    E(DT | B, T ) = 2τ02      ,                                 (6)
                                                          B
which does not depend on T . Thus the latent partition (T, P) describes the tier structure, whereas
B measures the magnitude of between-tier heterogeneity.
    The interpretation also carries to the paired-comparison scale. In the absence of a position
effect,
                                       pcd = expit(µc − µd ).
As B → 1, the tier contrasts shrink toward zero and pcd → 1/2. Hence larger values of B correspond
to greater structural balance.

2.3    Posterior computation
We develop a semi-collapsed Gibbs sampler (Neal, 2000) that combines the MFM partition repre-
sentation with Pólya–Gamma augmentation (Polson et al., 2013). The mixture weights and nominal
component count are integrated out when updating the occupied partition, while the effect of a
proposed new tier is integrated analytically. The sampler therefore avoids reversible-jump moves
and does not require the number of occupied tiers to be fixed in advance. Full derivations of the
sampling updates are provided in the Supporting Materials.
   For the current partition, define
                                                                 1
                                 ψe = d⊤
                                       e µ + h,         κe = Ye − ,
                                                                 2
where d⊤
       e is row e of DP . Introduce the Pólya–Gamma latent variables

                              ωe | ψe ∼ PG(1, ψe ),         e = 1, . . . , M.                   (7)

                                                  5
Let
                              Ω = diag(ω1 , . . . , ωM ),                 κ = (κ1 , . . . , κM )⊤ .
      Conditional on ω,                 
                                        µ
                                           rest ∼ N Q−1 b, Q−1 ,
                                                              
                                                                                                                (8)
                                        h
where
                                   DP ΩDP + ϕτ0−2 IT
                                   ⊤                                           ⊤ Ω1
                                                                                        
                                                                               DP   M
                               Q=                                                     −2 ,
                                       1⊤
                                        M ΩDP                               1⊤
                                                                             M Ω1M + σh
and                                                        ⊤ 
                                                           DP κ
                                                       b=       .
                                                           1⊤
                                                            Mκ
When h = 0, the last row and column are omitted.
  Integrating out (K, π) gives
                                           T                                     ∞
                                           Y
                                                     (nc )
                                                                                 X          k[T ]
                          p(P) = Vn (T )         γ           ,     Vn (T ) =                         pK (k),    (9)
                                           c=1                                   k=T
                                                                                           (γk)(n)

where nc = |Cc |, x(r) denotes a rising factorial, and x[r] denotes a falling factorial.
   To update zi , remove unit i from its current tier and let t denote the number of remaining
occupied tiers. For an existing tier c,
                                        Wic = (n−i,c + γ) exp{ℓi (c)},                                         (10)
where ℓi (c) is the Pólya–Gamma augmented log-likelihood contribution from comparisons involving
unit i.
   For a proposed new tier, define
                                 ϕ   X                X
                            Ai = 2 +   ωe ,     Ci =     sie (κe − ωe rie ),
                                τ0
                                           e∈Ei                           e∈Ei

and                                                   X                    ωe 2 
                                           Hi =                  κe rie −     r .
                                                                            2 ie
                                                      e∈Ei
The integrated contribution of the proposed tier is
                                                     1/2
                                               ϕ/τ02
                                                              2
                              new                              Ci
                            mi = exp(Hi )                 exp      ,
                                                Ai             2Ai
giving
                                                                 Vn (t + 1) new
                                           Winew = γ                       mi .                                (11)
                                                                   Vn (t)
If a new tier is selected,                                                       
                                                                          Ci 1
                                           µnew | rest ∼ N                  ,          .                       (12)
                                                                          Ai Ai
      Conditional on the occupied tier effects,
                                                                                             T
                                                                                                     !
                                                  T       1 X 2
                             ϕ | µ, T ∼ Gamma aϕ + , bϕ + 2  µc                                          ,     (13)
                                                  2      2τ0                                c=1

after which B = ϕ/(1 + ϕ).
    Algorithm 1 summarizes the sampler.

                                                                  6
Algorithm 1 Semi-collapsed Gibbs sampler
 1: Initialize P (0) , µ(0) , h(0) , and ϕ(0) .
 2: for s = 1, . . . , S do
 3:    Compute ψe = d⊤      e µ + h and sample ωe according to (7).
 4:    for i = 1, . . . , n do
 5:       Remove unit i from its current tier and delete the tier if it becomes empty.
 6:       Compute the existing-tier weights in (10) and the new-tier weight in (11).
 7:       Sample zi from the normalized allocation weights.
 8:       if a new tier is selected then
 9:           Sample µnew from (12).
10:       end if
11:    end for
12:    Construct the updated tier design matrix DP .
13:    Sample (µ, h) from (8).
14:    Sample ϕ from (13) and set B = ϕ/(1 + ϕ).
15:    Store P, T , µ, h, ϕ, and B.
16: end for


2.4    Posterior summaries
The MCMC output supports inference on everything the model estimates: the number of occupied
tiers, their memberships, the tier effects, and the structural balance parameter. The posterior
distribution of the occupied tier count is estimated by
                                                                S
                                      c =t|Y)= 1
                                                                X
                                      Pr(T                            1{T (s) = t}.
                                               S
                                                                s=1

   Because any single draw of the partition can be misleading, we summarize partition uncertainty
through the posterior similarity matrix
                                                      S
                                                  1   X  n
                                                           (s)  (s)
                                                                    o
                                           Pbij =       1 zi = zj     ,
                                                  S
                                                      s=1

so that Pbij is the posterior probability that units i and j belong to the same tier.
    When a single representative partition is needed, we use the least-squares criterion of Dahl
(2006). Let                                       n            o
                                           (s)       (s)   (s)
                                         Aij = 1 zi = zj
be the co-clustering matrix from posterior draw s. The Dahl partition is
                                                       X  (s)         2
                       bDahl = P (s∗ ) ,
                       P                  s∗ = arg min      A − Pbij .                           (14)
                                                                               ij
                                                                1≤s≤S
                                                                        i<j

Since the criterion involves only pairwise co-clustering indicators, it is invariant to mixture labels
and no post-processing for label switching is required.
    For interpretation, the tiers in PbDahl are ordered by their posterior tier effects. Structural
balance is summarized by the posterior distribution of B, with its posterior median and credible
interval as the primary summaries. When several paired-comparison populations are analyzed
together, the posterior draws of B feed directly into the Bayesian comparisons of Section 4.

                                                            7
3     Theoretical Properties
This section studies two theoretical properties of the proposed framework. We first consider iden-
tifiability under incomplete comparison designs and then provide a structural interpretation of the
balance parameter. These results clarify when the model can learn team differences from an in-
complete schedule and how the balance parameter can be interpreted in practical comparisons of
competitive structure. Proofs of all results are provided in the Supporting Materials.

3.1    Identification under incomplete comparison designs
The Bradley–Terry likelihood involves the latent abilities only through pairwise differences. There-
fore, shifting all tier effects by a common constant leaves the likelihood unchanged. The common
location is not identified, but under a connected comparison design all contrasts among occupied
tiers are identifiable.
Proposition 1 (Graph identification of tier contrasts). Suppose the observed comparison graph is
connected and P = {C1 , . . . , CT } contains T nonempty blocks. Then
                                          rank(DP ) = T − 1,
or equivalently,
                                         null(DP ) = span{1T }.
Thus all contrasts among the occupied tier effects are identifiable.
   If the first-position effect h is included, let HP be a T × (T − 1) contrast matrix satisfying
                                  HP⊤ 1T = 0,       HP⊤ HP = IT −1 .
Then (βP , h) is identifiable whenever
                                         rank [DP HP , 1M ] = T.
    Proposition 1 distinguishes identifiability from estimation precision. Connectivity ensures that
occupied tier contrasts are identifiable, whereas the number and distribution of observed compar-
isons determine how precisely these contrasts can be estimated.
    To characterize estimation under increasing comparison information, suppose the true occupied
partition is P ∗ and consider a fixed-n regime with M → ∞. Assume that the limiting comparison
graph is connected, the true comparison probabilities are bounded away from zero and one, and
                                    1 ⊤
                                     X ∗ W ∗ XP ∗ ,M −→ I ∗ ,                                       (15)
                                    M P ,M M
where I ∗ is positive definite.
Proposition 2 (Conditional posterior concentration). Suppose the prior density for the identifiable
tier contrasts and h is positive and continuous in a neighborhood of the true parameter. Conditional
on P = P ∗ , for any sequence rM → ∞,
                                                                 
                                          ∗     rM      (M )    ∗
                                Π ∥ϑ − ϑ ∥ > √        Y      , P −→ 0
                                                  M
in P ∗ -probability.
    Proposition 2 shows that, conditional on the occupied partition, increasing the number of infor-
mative comparisons improves estimation of the tier contrasts at the usual parametric rate. Thus
the amount of schedule information affects estimation precision but does not change the definition
of structural balance.

                                                   8
3.2   Structural interpretation of competitive balance
From (4),
                                              B
                                        ϕ=       ,          0 < B < 1,
                                             1−B
and the occupied tier effects satisfy
                                                                
                                               iid           1−B
                                        µc | B ∼ N    0, τ02       .
                                                              B
Therefore, for two distinct tiers,
                                                                         
                                                                    1−B
                                     µc − µ d | B ∼ N       0, 2τ02           .
                                                                    B
   Recall the average squared separation DT defined in (5).
Theorem 1 (Exact distribution of tier dispersion). Conditional on B and T ≥ 2,
                                           (T − 1)B
                                                       DT ∼ χ2T −1 .                         (16)
                                          2τ02 (1 − B)
Consequently,
                                                                1−B
                                        E(DT | B, T ) = 2τ02        ,
                                                                 B
and                                                                       2
                                                   8τ04
                                                                
                                                                    1−B
                                Var(DT | B, T ) =                                 .
                                                  T −1               B
   Moreover, if 0 < B2 < B1 < 1, then

                                     |µc − µd | | B1 ≤st |µc − µd | | B2 .

   Theorem 1 provides a direct interpretation of B. The expected average between-tier separation
does not depend on the number of occupied tiers, the number of competitors, or the number of
observed comparisons. Therefore, B provides a common measure of between-tier heterogeneity
across different competitive systems.
   To connect this quantity with team-level heterogeneity, define
                                             2     X
                                 Dnunit =               (θi − θj )2
                                          n(n − 1)
                                                        1≤i<j≤n

and                                                  PT
                                                        c=1 nc (nc − 1)
                                      q(P) = 1 −                          .
                                                          n(n − 1)
Corollary 1 (Population-level dispersion decomposition). Conditional on B and P,
                                                             1−B
                                 E Dnunit | B, P = q(P) 2τ02
                                                
                                                                 .
                                                              B
    Corollary 1 shows that overall team-level heterogeneity depends on two features: the magnitude
of separation between occupied tiers, measured by 2τ02 (1 − B)/B, and the proportion of team pairs
belonging to different tiers, measured by q(P). Therefore, two systems may have similar structural
balance while exhibiting different levels of overall heterogeneity because their tier compositions
differ.

                                                      9
3.3    Structural balance and effective tier complexity
The occupied tier count T is learned from the posterior partition and is not determined by B.
However, B is related to the number of competitive levels that remain distinguishable at a given
practical resolution.
   Fix δ > 0 and define a threshold graph on the occupied tiers by connecting c and d whenever

                                              |µc − µd | ≤ δ.

Let Tδ (B) denote the number of connected components of this graph.

Proposition 3 (Balance and effective tier complexity). Fix T ≥ 2 and δ > 0, and write
                                                  1/2
                                             1−B                      iid
                           µc (B) = τ0                    Zc ,     Zc ∼ N (0, 1).
                                              B

Under this common-Z coupling, if B1 > B2 , then

                                Tδ (B1 ) ≤ Tδ (B2 )           almost surely,

and consequently
                                  E{Tδ (B1 ) | T } ≤ E{Tδ (B2 ) | T }.
    For any two distinct occupied tiers,
                                                          "                   1/2 #
                                                         δ                B
                        Pr (|µc − µd | > δ | B) = 2Φ − √                                ,
                                                         2τ0             1−B

which is strictly decreasing in B.

    Proposition 3 shows that greater structural balance leads to smaller differences among occupied
tiers and therefore fewer practically distinguishable competitive levels at a fixed resolution δ. This
result concerns effective tier complexity and does not imply that the raw occupied MFM tier count
T must decrease monotonically with B in every finite data set.
    Finally, for a neutral comparison between tiers c and d, let

                                         pcd = expit(µc − µd ).

Then                              h                 i       1−B
                                E {logit(pcd )}2 | B = 2τ02        ,
                                                              B
so larger values of B correspond to smaller variation in pairwise log-odds contrasts.


4     Bayesian Comparison of Structural Balance Across Systems
The results in Section 3.2 provide a common scale for comparing competitive balance across paired-
comparison systems. Consider two systems indexed by ℓ = 1, 2, with balance parameters B1 and B2 .
The systems may differ in the number of competitors, occupied tiers, and observed comparisons,
but are analyzed using the same reference scale τ0 .
   By Theorem 1, define
                                                             1−B
                                 d(B) = E(DT | B, T ) = 2τ02     .
                                                              B

                                                     10
Because d(B) is strictly decreasing on (0, 1), larger values of B correspond to smaller between-tier
separation and therefore greater structural balance. Importantly, d(B) does not depend on the
number of competitors, the number of occupied tiers, or the number of observed comparisons.
These features affect posterior uncertainty and the realized competitive structure, but not the
interpretation of structural balance. Therefore, the same scale can be used to compare systems
with different competitive structures and schedules.

4.1      Directional comparison of structural balance
Define
                                             ∆B = B1 − B2 .
Because d(B) is strictly decreasing,

                                 ∆B > 0         ⇐⇒        d(B1 ) < d(B2 ).

Thus ∆B > 0 indicates greater structural balance in system 1, whereas ∆B < 0 indicates greater
structural balance in system 2.
    Given posterior draws,
                                       (s)     (s)    (s)
                                     ∆B = B1 − B2 .
We summarize the posterior distribution of ∆B using its median, credible interval, and the direc-
tional probability
                                  P12 = Pr(B1 > B2 | Y1 , Y2 ).
Values near one provide evidence that system 1 is more balanced, values near zero favor system 2,
and values near one half indicate little directional evidence.

4.2      Practical differences in structural balance
A directional comparison does not indicate whether the difference in structural balance is practically
meaningful. We therefore define
                                       ∆d = d(B2 ) − d(B1 ),
so that
                                       ∆d > 0     ⇐⇒        B1 > B2 .
   For a prespecified practical margin ϵd > 0, consider

                      H− : ∆d < −ϵd ,          H0 : |∆d | ≤ ϵd ,        H+ : ∆d > ϵd .

Here, H− represents meaningfully greater balance in system 2, H0 represents practical similarity,
and H+ represents meaningfully greater balance in system 1.
   The corresponding posterior probabilities are

                                    π− = Pr(∆d < −ϵd | Y1 , Y2 ),
                                       π0 = Pr(|∆d | ≤ ϵd | Y1 , Y2 ),
                                    π+ = Pr(∆d > ϵd | Y1 , Y2 ),

where
                                           π− + π0 + π+ = 1.



                                                     11
The vector (π− , π0 , π+ ) distinguishes evidence for a meaningful difference from evidence for practical
similarity. In particular, a directional probability near one half does not imply practical equivalence.
   For posterior draws,                        (                         )
                                                        (s)          (s)
                                     (s)     2   1 − B2       1 − B1
                                   ∆d = 2τ0          (s)
                                                            −     (s)
                                                                           .
                                                   B2           B1
    For calibration, the root mean squared tier separation is
                                                                                 1/2
                                                             √
                                                                       
                                                   1/2                     1−B
                                 s(B) = {d(B)}           =       2τ0                    ,
                                                                            B

which is expressed on the latent Bradley–Terry log-odds scale. This provides a direct way to specify
ϵd in terms of a practically meaningful difference in tier separation.
    Evidence for practical similarity can also be summarized using the interval Bayes factor

                        (ϵ)     Pr(H0 | Y1 , Y2 )/ Pr(H1 | Y1 , Y2 )
                    BF01 =                                           ,            H1 : |∆d | > ϵd .
                                       Pr(H0 )/ Pr(H1 )

Values greater than one indicate increased support for practical similarity relative to the prior,
whereas values below one favor a meaningful difference. We report this quantity as a complementary
posterior summary together with (π− , π0 , π+ ).


5     Simulation study
We conducted a factorial simulation study to evaluate the proposed framework under comparison
structures and competitive configurations motivated by professional sports applications. The sim-
ulations address two related questions. First, we examine how accurately the model recovers latent
team abilities, competitive tiers, and structural balance under schedules with different amounts of
comparison information. Second, we evaluate whether the proposed posterior comparison of struc-
tural balance remains informative when two systems differ substantially in their numbers of teams
and observed comparisons.

5.1   Estimation and latent-tier recovery
The simulations use n = 30 teams under three comparison-graph designs. The first is the observed
NBA regular-season schedule with 1,230 games. To see what happens as comparison information
is stripped away while keeping the graph connected, we add a complete double round-robin with
870 games and a complete single round robin with 435 games. The three designs step down in
informativeness, which lets us watch how schedule density affects recovery of the latent competitive
structure.
    Each design is crossed with two structural settings,

                              (B, T ) = (0.2, 4)         and           (B, T ) = (0.5, 3),

a less balanced system with four tiers and a more balanced one with three. The second setting is
deliberately the harder one for tier recovery: since larger B means smaller between-tier separation,
its tiers sit closer together even though there are fewer of them. Within each setting we try both
balanced and unbalanced tier allocations,

                                    (8, 8, 7, 7)     and           (3, 12, 12, 3)

                                                         12
for four tiers, and
                                  (10, 10, 10)       and        (5, 20, 5)
for three. The unbalanced layouts test whether recovery suffers when most teams pile into one or
two levels instead of spreading across tiers.
    Team labels are randomly assigned to tiers in each replicate. With τ0 = 1, the tier abilities are
scaled so that the implied structural balance matches the target exactly, and games are generated
from
                       Pr(Yij = 1 | θ, h) = logit−1 (θi − θj + h), h = 0.35.
   We ran 100 independent replicates for each of the 12 simulation settings. For each replicate,
the MFM–BT model was fitted using two independently initialized MCMC chains. Each chain
consisted of 6,000 iterations, with the first 1,500 iterations discarded as burn-in and every third
subsequent iteration retained, yielding 1,500 posterior draws per chain. We used λK = 1, τ0 = 1,
and γ = 1 throughout the simulation study. The number of occupied tiers is inferred from the data
rather than fixed at the truth. Clustering accuracy is measured by the adjusted Rand index (ARI)
(Hubert and Arabie, 1985) of the Dahl representative partition, and tier-count recovery by
                                                   R
                                                   X
                                              −1
                                       100R              I(Tbr = T ).
                                                   r=1

Ability estimation is judged by mean squared error (MSE), ranking by the Spearman correlation
between estimated and true ability ranks, and the system-level parameters by B-MSE and h-
MSE from their posterior means. These criteria deliberately separate recovery of the discrete tier
structure from estimation of the continuous balance parameter.
    We compare MFM–BT with three two-stage benchmark procedures: BT–GMM, which clusters
ordinary Bradley–Terry ability estimates using a Gaussian mixture model (McLachlan and Peel,
2000); BT–DP, which applies a DP-means clustering procedure to the Bradley–Terry estimates
(Kulis and Jordan, 2012); and BT–pairwise-fusion, which uses an all-pairs L1 fusion penalty mo-
tivated by the ranking-lasso method (Masarotto and Varin, 2012), all fitted to exactly the same
graphs and outcomes. Each benchmark selects its own number of clusters from its fitted model,
since in practice neither the number nor the composition of competitive tiers is known in advance.
    Figure 1 summarizes clustering recovery across the 12 simulation settings. The upper row
reports the adjusted Rand index (ARI), and the lower row reports the percentage of replicates that
recover the true number of tiers. Within each graph design, the four bars correspond to the two
(B, T ) settings under balanced and unbalanced tier allocations. For MFM–BT and BT–DP, the
reported partitions are obtained from the Dahl-selected posterior representative partition.
    MFM–BT achieves the best clustering performance across nearly all settings. Its advantage
is especially clear for the sparse single-round-robin design and the more difficult (B, T ) = (0.5, 3)
setting, where the tier differences are smaller. BT–DP is generally the strongest benchmark in terms
of ARI, but it tends to overestimate the number of tiers. On average, it estimates approximately 5.13
tiers when the true number is either 3 or 4, which explains its relatively low true-tier recovery rate.
BT–GMM performs moderately well under the denser designs but loses accuracy as comparison
information decreases. It tends to merge some of the true tiers, leading to fewer estimated tiers than
the truth. BT–pairwise-fusion has the lowest ARI and consistently underestimates the number of
tiers, recovering the true tier count in none of the simulation replicates.
    Table 1 summarizes performance across the 12 simulation settings, with 100 replicates for each
setting. MFM–BT achieves the highest average ARI, 0.858, and recovers the true number of tiers
in 81.8% of replicates. The genuine Bayesian BT–DP benchmark performs second, with an average

                                                    13
                                                                     Clustering performance across simulation settings
                                                                                Genuine Bayesian DP−−BT; BT−kmeans excluded
                          NBA schedule (1230)                                               Double round robin (870)                                              Single round robin (435)
1.00



0.75




                                                                                                                                                                                                              ARI
0.50



0.25



0.00
100



 75




                                                                                                                                                                                                              True T selected (%)
 50



 25



  0
       B=0.2, T=4   B=0.2, T=4           B=0.5, T=3   B=0.5, T=3   B=0.2, T=4           B=0.2, T=4            B=0.5, T=3           B=0.5, T=3   B=0.2, T=4   B=0.2, T=4             B=0.5, T=3   B=0.5, T=3
        balanced    unbalanced            balanced    unbalanced    balanced            unbalanced             balanced            unbalanced    balanced    unbalanced              balanced    unbalanced


                                                                   Method          MFM−BT      BT−GMM          BT−DP       BT−pairwise−fusion




                             Figure 1: Clustering performance across the 12 simulation designs.

ARI of 0.774 and a true-tier recovery rate of 26.2%. BT–GMM recovers the true tier count in
29.7% of replicates, while BT–pairwise-fusion never recovers the true count. MFM–BT also has
the smallest ability MSE and the highest rank correlation. Thus, its advantage is not limited to
partition recovery: jointly modeling tier memberships and abilities also improves continuous ability
estimation and the induced team ranking.

Table 1: Average performance over the 12 simulation settings and 100 replicates per setting. Entries
are means with standard deviations in parentheses.
       Method                        ARI True T (%) Ability MSE Rank correlation
       MFM–BT              0.858 (0.182) 81.8 (38.6) 0.137 (0.162)            0.959 (0.067)
       BT–GMM              0.610 (0.290) 29.7 (45.7) 0.378 (1.811)            0.915 (0.054)
       BT–DP               0.774 (0.250) 26.2 (44.0) 0.144 (0.164)            0.952 (0.069)
       BT–pairwise-fusion 0.433 (0.168)        0.0 (0.0) 1.597 (1.136)        0.913 (0.059)

    This gap between methods matters for the application we have in mind. A competitive-balance
study needs more than a ranking of teams; it needs a stable account of which teams are practically
indistinguishable in latent strength, and the much higher ARI of MFM-BT says its posterior parti-
tion captures that organization far more faithfully. At the same time, the strong rank correlations
across several methods remind us that producing a ranking is much easier than recovering the tier
structure beneath it, so high ranking accuracy on its own says little about stratification.
    Table 2 shows the MFM-BT estimation results by design. Under the NBA schedule recovery
is excellent, with ARI between 0.948 and 0.991 and true tier counts recovered in 79% to 97% of
replicates. Performance slips moderately under the double round robin and more sharply under the
single round robin, worst of all at (B, T ) = (0.5, 3), where ARI falls to 0.577–0.614. The pattern is
exactly what the structure predicts: B = 0.5 puts the tiers closer together, and with fewer games
it becomes harder to say which side of a boundary a team belongs on.
    The balance parameter is far more stable than individual tier memberships. B-MSE stays small
in nearly every design even where ARI drops substantially: under the single-round-robin settings
with (B, T ) = (0.5, 3), ARI sits below 0.62 while B-MSE remains between 0.003 and 0.006. B
summarizes the overall scale of heterogeneity rather than the fate of any one team, so it doesn’t
need every team to land in its exact true tier to stay well estimated.

                                                                                                     14
     Table 2: MFM-BT performance by graph design, structural setting, and tier allocation.
 Graph design (B, T ) Allocation     ARI True T (%) Ability MSE B-MSE h-MSE
 NBA            (0.2,4) Balanced    0.990             97           0.058      0.002     0.007
 NBA            (0.2,4) Unbalanced 0.991              96           0.036      0.003     0.004
 NBA            (0.5,3) Balanced    0.948             79           0.032      0.005     0.004
 NBA            (0.5,3) Unbalanced 0.955              81           0.026      0.004     0.004
 Double RR      (0.2,4) Balanced    0.951             85           0.104      0.003     0.012
 Double RR      (0.2,4) Unbalanced 0.964              86           0.082      0.004     0.009
 Double RR      (0.5,3) Balanced    0.891             76           0.064      0.005     0.007
 Double RR      (0.5,3) Unbalanced 0.898              82           0.050      0.004     0.006
 Single RR      (0.2,4) Balanced    0.752             73           0.425      0.003     0.025
 Single RR      (0.2,4) Unbalanced 0.768              67           0.329      0.010     0.015
 Single RR      (0.5,3) Balanced    0.614             85           0.229      0.006     0.014
 Single RR      (0.5,3) Unbalanced 0.577              74           0.209      0.003     0.010


    Losing games mainly hurts local structure. Ability MSE rises noticeably as schedules thin out,
and tier assignments near close levels become ambiguous, while the global balance signal survives
because it pools information across the whole league – exactly the separation between partition
uncertainty and B-uncertainty the framework is built around.
    Unbalanced tier sizes cause no systematic damage, either. In several settings the unbalanced
allocation does as well as, or slightly better than, the balanced one, so the method does not rely
on roughly equal groups – a good sign for sports data, where tiers routinely contain very different
numbers of teams.
    Taken together, the simulations bear out the separate roles of the partition and the balance pa-
rameter. With an informative schedule, MFM-BT recovers abilities, rankings, and tiers accurately;
as comparisons grow scarce, uncertainty about individual abilities and memberships rises, especially
when tiers sit close together, while B remains comparatively steady. B tracks the magnitude of
structural heterogeneity; the comparison graph only governs how precisely that structure can be
learned from the games at hand – which is exactly the division of labor the theory predicts.

5.2   Validation of structural-balance comparisons
We separately evaluated the proposed posterior procedure for comparing structural balance across
two systems. The purpose of this experiment is to determine whether comparisons on the common
B-scale remain meaningful when the systems being compared differ substantially in both population
size and schedule density.
    The first design was a matched comparison in which both systems contained 30 teams and used
the same NBA schedule with 1,230 comparisons. The second was a heterogeneous comparison in
which system 1 used the NBA design (n1 = 30, M1 = 1230), while system 2 used the NFL design
(n2 = 32, M2 = 272). The heterogeneous setting is particularly relevant to the empirical analysis
because it separates differences in the underlying balance parameter from differences in the amount
of information available to estimate it.
    For every replicate, system 1 was generated with (B1 , T1 ) = (0.5, 3), while system 2 was gener-
ated with (B2 , T2 ) = (0.2, 4). Because B1 > B2 , system 1 is more structurally balanced under the
data-generating model. We generated 100 replicates for each design and fitted the same MFM-BT




                                                 15
model independently to the two systems. Posterior draws were used to calculate
                                                                                1−B
                 ∆B = B1 − B2 ,        ∆d = d(B2 ) − d(B1 ),      d(B) = 2τ02       .
                                                                                 B
Positive values of either contrast favor system 1. We summarized the directional probability
Pr(B1 > B2 | Y ), the corresponding probability on the dispersion scale, and the three practical-
testing probabilities (π− , π0 , π+ ). The practical-equivalence margin was set to ϵd = 0.4 on the
dispersion scale.
    The results are summarized in Table 3. For the matched design, the average posterior probability
that system 1 was more balanced was 0.864, compared with 0.829 for the heterogeneous NBA–NFL
comparison. The corresponding probabilities that system 1 was more balanced by more than the
practical-equivalence margin were 0.836 and 0.795. The posterior median dispersion contrasts were
3.46 and 3.15, respectively. Hence, the procedure identifies the correct direction of the balance
difference under both comparison designs.

      Table 3: Validation of the Bayesian structural-balance comparison over 100 replicates.
                                                                                 (ϵ)
 Design                      Pr(B1 > B2 ) Pr(∆d > 0)      π−     π0     π+ BF01 Median ∆d
 Matched NBA–NBA                   0.864         0.864 0.113 0.050 0.836 0.317               3.46
 Heterogeneous NBA–NFL             0.829         0.829 0.143 0.062 0.795 0.397               3.15

    The contrast between the two designs is itself informative. Swapping the NBA schedule for
the much sparser NFL schedule does not flip the inferred ordering of the two systems, but it does
weaken the posterior evidence. The average probability assigned to the correct practical direction
falls from 0.836 to 0.795, while the mass given to the opposite direction and to the equivalence
region grows. Schedule density, in other words, changes how confident the comparison is, not what
it concludes on the common structural-balance scale.
    The interval Bayes factors average 0.317 under the matched design and 0.397 under the hetero-
geneous one. Both sit below one, so the posterior does not favor practical equivalence relative to
the prior in this directionally separated experiment, though neither comes close to certainty. That
is about what one should expect from a single season, especially when one system supplies only
272 comparisons. It also explains why posterior probabilities serve the purpose better than a flat
declaration that one league is or is not more balanced.
    In sum, the second simulation supports the framework’s main comparative claim. Structural
balance can be compared across systems with different numbers of teams, tier configurations, and
comparison graphs, because B is defined independently of all of these. Schedule differences surface
instead through posterior uncertainty. This is precisely the situation the sports application presents:
two leagues can be placed on the same structural scale even though one of them offers far more
information about its latent competitive structure.


6    Comparing Competitive Balance and Tier Structure in the NBA
     and NFL
We apply the proposed MFM–BT model to the 2025–2026 National Basketball Association (NBA)
regular season and the 2025 National Football League (NFL) regular season. Each game enters
the analysis as a paired comparison between the home and away teams, and each league has its
own home-advantage parameter on the common reference scale τ0 = 1. NFL postseason games are
excluded, as is the additional Knicks–Spurs special event in the NBA.

                                                  16
    For each league, we run two independently initialized MCMC chains. Each chain contains
4,000 iterations, with the first 1,000 iterations discarded as burn-in and every third subsequent
iteration retained. This yields 1,000 posterior draws for posterior summaries. We use λK = 1 and
γ = 0.4 for the MFM prior, and assess convergence using trace plots, running posterior means, and
Gelman–Rubin diagnostics for B and the home-advantage parameter.
    The two schedules differ sharply in density. The NBA season has each of its 30 teams play 82
games, giving 1,230 regular-season comparisons in total. The NFL, with 32 teams, plays only 17
games apiece, for 272 comparisons. The NBA therefore provides more than four times as many
pairwise observations on relative team strength, while the NFL season is short enough that a single
game carries considerable weight. This contrast between a long, dense schedule and a short, sparse
one makes the pairing well suited to studying how schedule information affects what can be learned
about competitive structure.

6.1   Structural balance and cross-league comparison
Posterior summaries for the two leagues appear in Table 4. The posterior mean of B is 0.482 for
the NBA and 0.473 for the NFL. The NBA estimate is nominally higher, but the difference is small
relative to posterior uncertainty: the 90% credible intervals are [0.240, 0.681] and [0.205, 0.693],
respectively. The posterior mean of the home-advantage parameter is 0.274 for the NBA and 0.196
for the NFL. The corresponding 90% credible intervals are [0.172, 0.381] and [−0.030, 0.423]. Thus,
the NBA shows a larger estimated home advantage, although the intervals overlap substantially
and the NFL interval includes zero.

Table 4: Posterior summaries of structural balance, home advantage, and latent tier structure for
the NBA and NFL.
      League n         M E(B | Y ) 90% CrI for B E(h | Y ) 90% CrI for h Dahl T
      NBA       30 1,230       0.482    [0.240, 0.681]    0.274 [0.172, 0.381]           3
      NFL       32    272      0.473    [0.205, 0.693]    0.196 [-0.030, 0.423]          2

   To compare the leagues formally, we use the dispersion-scale procedure from Section 4. Define

                                     ∆d = d(BNFL ) − d(BNBA ),

so positive values indicate greater structural balance in the NBA. We calibrate the practical margin
by allowing a 0.25-unit difference in the RMS tier separation
                                                    p
                                            s(B) = d(B)

around B0 = 0.5, which with τ0 = 1 gives the conservative dispersion-scale margin ϵd = 0.77.
   The posterior median of ∆d is 0.04, with a 90% credible interval of [−3.91, 5.49]. The posterior
probability that the NBA is more structurally balanced is

                                       Pr(∆d > 0 | Y ) = 0.510,

essentially a coin flip. Posterior mass spreads across all three practical regions,

                                 (π− , π0 , π+ ) = (0.315, 0.340, 0.345),

rather than concentrating on a meaningful difference in either direction, and the interval Bayes
factor BF01 = 1.42 offers only modest evidence for practical similarity relative to the prior. The

                                                   17
   Table 5: Bayesian comparison of NBA and NFL structural balance on the dispersion scale.
             Median ∆d       90% CrI Pr(∆d > 0)     π−       π0    π+ BF01
             0.04         [-3.91,5.49]     0.510 0.315 0.340 0.345        1.42


data, in other words, support neither a directional difference in structural balance nor strong
practical equivalence; one season simply does not contain enough information for the latter.
    The comparison also highlights a useful property of the balance measure. The NBA supplies
more than four times as many regular-season comparisons as the NFL, yet this does not change
what B means, only how well it is estimated. The NFL interval is noticeably wider at a similar
posterior mean, which is exactly what one expects when less data are available to separate persistent
strength differences from game-level noise. A league should therefore not be called more or less
balanced merely because its schedule happens to produce a sharper or noisier standings table.

6.2   Comparison with traditional competitive-balance measures
For context, we also compute conventional competitive-balance measures used in sports economics
from regular-season win percentages, including the standard deviation, top-to-bottom range, Herfindahl–
Hirschman index (HHI), and Gini coefficient (Fort and Maxcy, 2003; Utt and Fort, 2002; Owen
et al., 2007; Manasis et al., 2013). Lower values indicate greater observed balance. These measures
summarize realized standings and therefore address a different question from the structural balance
parameter. In particular, they do not separate persistent differences in underlying team strength
from game-level variation, and they do not quantify uncertainty in the latent tier structure.

  Table 6: Traditional competitive-balance measures calculated from regular-season standings.
                    League SD of win percentage Range          HHI Gini
                    NBA                     0.169    0.573 0.0370 0.188
                    NFL                     0.204    0.647 0.0363 0.230

    The conventional measures mostly point toward greater observed parity in the NBA (Table 6).
The standard deviation of win percentages is 0.169 in the NBA against 0.204 in the NFL, and the
ranges are 0.573 and 0.647. The Gini coefficients, 0.188 and 0.230, tell the same story. Only the
HHI departs slightly, at 0.0370 for the NBA and 0.0363 for the NFL. The conventional toolkit thus
does not even agree with itself about the ranking, though most of its members see more dispersion
in the NFL standings.
    The model-based analysis cuts across this. Despite the wider spread of observed NFL win
percentages under most conventional measures, the posterior distributions of B give little reason
to think the leagues differ in underlying structural balance. Some of what the standings show as an
NFL disadvantage is plausibly the product of a much shorter schedule and the game-level variation
that comes with it, rather than genuinely larger persistent heterogeneity. Observed parity and
latent structural balance, it seems, need not tell the same story.

6.3   Latent competitive tiers and team rankings
The structural balance parameter measures overall heterogeneity, but it does not describe how
teams are organized within a league. We therefore also examine the estimated competitive tiers.
Because mixture labels are arbitrary, we order the tiers according to the Dahl-selected tier abilities,
with Tier 1 denoting the strongest competitive tier. The Dahl representative partition identifies

                                                  18
three tiers in the NBA with 6, 14, and 10 teams, respectively, and two tiers in the NFL with 16
teams each (Table 7).

Table 7: MFM–BT Dahl representative tier composition for the NBA and NFL. Tier 1 denotes the
strongest competitive tier.
 League and tier         Teams
 NBA Tier 1 (higher) Boston Celtics; Denver Nuggets; Detroit Pistons; New York Knicks; Ok-
                         lahoma City Thunder; San Antonio Spurs.
 NBA Tier 2 (middle) Atlanta Hawks; Charlotte Hornets; Cleveland Cavaliers; Golden State
                         Warriors; Houston Rockets; LA Clippers; Los Angeles Lakers; Miami
                         Heat; Minnesota Timberwolves; Orlando Magic; Philadelphia 76ers;
                         Phoenix Suns; Portland Trail Blazers; Toronto Raptors.
 NBA Tier 3 (lower)      Brooklyn Nets; Chicago Bulls; Dallas Mavericks; Indiana Pacers; Mem-
                         phis Grizzlies; Milwaukee Bucks; New Orleans Pelicans; Sacramento
                         Kings; Utah Jazz; Washington Wizards.
 NFL Tier 1 (higher) Buffalo Bills; Chicago Bears; Denver Broncos; Detroit Lions; Green Bay
                         Packers; Houston Texans; Indianapolis Colts; Jacksonville Jaguars; Los
                         Angeles Chargers; Los Angeles Rams; Minnesota Vikings; New England
                         Patriots; Philadelphia Eagles; Pittsburgh Steelers; San Francisco 49ers;
                         Seattle Seahawks.
 NFL Tier 2 (lower)      Arizona Cardinals; Atlanta Falcons; Baltimore Ravens; Carolina Pan-
                         thers; Cincinnati Bengals; Cleveland Browns; Dallas Cowboys; Kansas
                         City Chiefs; Las Vegas Raiders; Miami Dolphins; New Orleans Saints;
                         New York Giants; New York Jets; Tampa Bay Buccaneers; Tennessee
                         Titans; Washington Commanders.

    The NBA shows a more differentiated competitive structure. Six teams make up Tier 1, a
large middle group of 14 sits in Tier 2, and 10 teams fall to Tier 3. Much of the league, in other
words, is packed into the middle, with a relatively small group pulling away at the top. This is also
where the tier structure and the global balance parameter part company: a league can be highly
balanced overall and still contain a recognizable group of leading teams. The tier compositions also
say things the raw standings do not. Tier 1 puts the defending champion Oklahoma City Thunder
and the usual contenders, Boston and Denver, alongside two teams a standings-only reading would
overlook. Detroit spent much of the season playing better than its win total suggested, and San
Antonio belonged to the elite group on latent strength well before its record caught up. The Knicks
sit in that group too, which shows the model looking past short streaks to how teams actually
compare. Working the other way, a few famous names, the Lakers and Warriors among them,
land in the broad middle tier rather than the elite one, and a win-percentage table flattens that
distinction into one long ranking. The practical reading for a front office is simple: about half the
league is a middle band where games are close to a coin flip, and a six-team group forms the realistic
championship tier. That distinction shapes how a season should be judged, and no standings table
makes it visible.
    The NFL partition is coarser, splitting the league evenly into two tiers of 16. That should not
be read as a simpler competitive structure. With only 272 regular-season games against the NBA’s
1,230, the data simply carry far less information about teams of similar ability. The broad NFL tiers
reflect both the organization the data support and the heavier uncertainty that a sparse schedule
brings. The NFL tiers carry the same kind of information. Tier 1 contains the eventual Super


                                                 19
Bowl champion Seattle and the AFC champion New England, along with teams whose seasons
ended earlier than their strength deserved, Buffalo and the Chargers being the clearest cases. It
also holds the season’s surprise division winners, including Chicago, whose arrival in the top group
the model caught even though the franchise had spent years near the bottom. Tier 2, meanwhile,
collects teams whose reputations run ahead of their present strength. Kansas City and Baltimore
both fall below the midpoint on latent ability despite championship pedigrees that say otherwise.
In a seventeen-game season, a couple of close losses or one injury at the wrong time can push a
team like that out of January, and the tiers capture the fact that they never separated from the
league’s middle. The honest summary of an NFL season, it turns out, is a large top group of
broadly comparable clubs, a handful of genuine stragglers, and a lot of doubt in between, not the
clean thirty-two-step ordering the standings imply.
    The comparison also shows why the number of tiers should not be used as a measure of over-
all competitive balance. The NBA has three estimated tiers and the NFL has two, while their
posterior estimates of B are very similar. The tier structure describes how teams are organized
into competitive levels, whereas B measures the magnitude of heterogeneity among those levels.
Therefore, more tiers do not necessarily imply less competitive balance.
    Figure 2 provides a more detailed view of the posterior ranking and clustering results. The
rank intervals describe uncertainty in the relative positions of individual teams, while the posterior
mean co-clustering matrices summarize uncertainty in whether pairs of teams belong to the same
latent competitive tier.
    The posterior mean co-clustering matrices provide information that is not available from a
single representative partition. Teams near a tier boundary may have lower posterior co-clustering
probabilities with teams in their assigned tier and nonnegligible probabilities of clustering with
teams in a neighboring tier. The Dahl tiers should therefore be interpreted as representative
summaries of posterior clustering uncertainty rather than as fixed classifications of team quality.

6.4   Agreement with observed standings and practical implications
As a descriptive check, we compare posterior median ranks with observed regular-season ranks
based on winning percentage, using point differential as a transparent tie-breaker. Since both
rankings come from the same games, this measures agreement with the observed season rather
than out-of-sample prediction.

   Table 8: Agreement between MFM–BT posterior ranks and observed regular-season ranks.
  League Spearman ρ Kendall τ Pearson r Mean absolute rank error Top-five overlap
  NBA            0.978      0.924    0.949                       2.35               5/5
  NFL            0.990      0.944    0.959                       2.38               4/5

    The model ranks teams much the way the standings do. The Spearman correlation is 0.978 for
the NBA and 0.990 for the NFL, and the Kendall correlations are 0.924 and 0.944. The model’s
top five also matches the observed NBA top five exactly, and four of the observed NFL top five.
So the model keeps the ordering we see in the season results, but adds something the standings
cannot: uncertainty intervals and information about which teams belong to the same competitive
group.
    The results leave us with a few observations. First, the usual measures cannot even settle
which league is more balanced. Most of the dispersion measures point to the NBA, the HHI points
slightly to the NFL, and our model finds no meaningful difference in structural balance. Much
depends on what one chooses to look at: the results on the court and field, or the strength of the

                                                 20
teams underneath them. It also becomes clear that equal balance does not mean the same kind of
competition. The NBA breaks into three tiers, with most clubs crowded into a broad middle and
a small elite group above them, while the NFL settles into two wide groups. A policy aimed at
parity might close the gaps between teams without changing how they bunch together, or it might
reshuffle the groups without narrowing the gaps, and it is worth knowing which of the two a given
policy actually does. Finally, the schedule puts a ceiling on what any of this can tell us. An NBA
season simply contains far more information about how teams compare, whereas an NFL season
leaves real doubt about teams of similar strength and about where one tier gives way to the next. A
comparison built only on standings risks mistaking that doubt for a genuine difference in balance.
On the whole, the NBA and NFL look much alike in global structural balance but quite different
in how their competition is organized, and in how confidently that organization can be described.
Balance, tier structure, and schedule information are separate features of a league. Treating them
as such makes for better comparisons than leaning on standings, conventional indices, or tier counts
alone.


7    Discussion and Conclusion
We have developed a Bayesian paired-comparison framework for studying competitive balance that
separates global structural heterogeneity from latent competitive tier structure. The MFM prior
learns the number and membership of occupied tiers, while the balance parameter B quantifies how
strongly those tiers are separated. Our theoretical results give B a direct interpretation in terms of
between-tier dispersion and show how overall team-level heterogeneity depends jointly on the size of
tier separation and the prevalence of cross-tier comparisons. Because the framework separates the
underlying competitive structure from the information contained in the observed schedule, balance
can be compared across systems with different numbers of teams and games. The simulations show
that the method recovers latent competitive structure accurately when the comparison design is
informative enough, and that estimates of structural balance remain comparatively stable even
as schedules thin out. The NBA and NFL application reinforces the distinction between global
balance and competitive stratification. Conventional standings-based measures generally suggest
greater observed parity in the NBA, yet the posterior analysis finds little evidence of a meaningful
difference in underlying structural balance. The two leagues are organized differently all the same:
the NBA splits into three latent competitive tiers, while the NFL falls into two broader ones, and
the greater uncertainty in the NFL reflects its much sparser schedule.
    Several extensions are worth exploring. A longitudinal version of the model could let B, team
abilities, and tier memberships drift across seasons, which would make it possible to characterize
changes in parity, movement between competitive tiers, and the effects of league policies on com-
petitive structure. On the theory side, it would be useful to understand how the topology of the
comparison graph shapes estimation. Beyond plain connectivity, properties such as graph density,
degree heterogeneity, spectral connectivity, and bottlenecks may govern how precisely abilities,
tiers, and structural balance can be learned, and could inform the design of schedules that carry
more information. One further direction is to relax the transitive structure of the Bradley–Terry
model. Sports competitions often show systematic matchup patterns: team A tends to beat team
B, team B tends to beat team C, but team C tends to beat team A. A one-dimensional latent ability
cannot represent such cycles. A natural next step is to augment the global ability component with
structured matchup effects that capture nontransitive patterns while keeping measures of overall
strength and balance interpretable. That would give a richer account of both hierarchical and cyclic
structure in competitive systems.


                                                 21
References
Basini, F., Tsouli, V., Ntzoufras, I., and Friel, N. (2023). Assessing competitive balance in the
  English Premier League for over forty seasons using a stochastic block model. Journal of the
  Royal Statistical Society Series A: Statistics in Society, 186(3):530–556.

Bradley, R. A. and Terry, M. E. (1952). Rank analysis of incomplete block designs: I. the method
  of paired comparisons. Biometrika, 39(3/4):324–345.

Busse, L. M., Orbanz, P., and Buhmann, J. M. (2007). Cluster analysis of heterogeneous rank
  data. In Proceedings of the 24th international conference on Machine learning, pages 113–120.

Caron, F. and Doucet, A. (2012). Efficient bayesian inference for generalized bradley–terry models.
  Journal of Computational and Graphical Statistics, 21(1):174–196.

Dahl, D. B. (2006). Model-based clustering for expression data via a dirichlet process mixture model.
 In Do, K.-A., Müller, P., and Vannucci, M., editors, Bayesian Inference for Gene Expression and
 Proteomics, pages 201–218. Cambridge University Press.

Davidson, R. R. (1970). On extending the bradley-terry model to accommodate ties in paired
  comparison experiments. Journal of the American Statistical Association, 65(329):317–328.

Deng, K., Han, S., Li, K. J., and Liu, J. S. (2014). Bayesian aggregation of order-based rank data.
  Journal of the American Statistical Association, 109(507):1023–1039.

Dong, P., Han, R., Jiang, B., and Xu, Y. (2026). Statistical ranking with dynamic covariates.
 Journal of the Royal Statistical Society Series B: Statistical Methodology, 88(1):221–238.

Dunson, D. B. and Peddada, S. D. (2008). Bayesian nonparametric inference on stochastic ordering.
 Biometrika, 95(4):859–874.

Fort, R. and Maxcy, J. (2003). Competitive balance in sports leagues: An introduction. Journal
  of Sports Economics, 4(2):154–160.

Fort, R. and Quirk, J. (1995). Cross-subsidization, incentives, and outcomes in professional team
  sports leagues. Journal of Economic Literature, 33(3):1265–1299.

Glickman, M. E. (1999). Parameter estimation in large dynamic paired comparison experiments.
  Journal of the Royal Statistical Society Series C: Applied Statistics, 48(3):377–394.

Hubert, L. and Arabie, P. (1985). Comparing partitions. Journal of Classification, 2(1):193–218.

Hunter, D. R. (2004). MM algorithms for generalized Bradley-Terry models. The Annals of
 Statistics, 32(1):384–406.

Kulis, B. and Jordan, M. I. (2012). Revisiting K-means: New algorithms via bayesian nonparamet-
 rics. In Proceedings of the 29th International Conference on Machine Learning, pages 1131–1138.

Li, X., Yi, D., and Liu, J. S. (2022). Bayesian analysis of rank data with covariates and heteroge-
  neous rankers. Statistical Science, 37(1):1–23.

Luce, R. D. (1959). Individual Choice Behavior: A Theoretical Analysis. Wiley.



                                                 22
Manasis, V., Avgerinou, V., Ntzoufras, I., and Reade, J. J. (2013). Quantification of competi-
 tive balance in European football: Development of specially designed indices. IMA Journal of
 Management Mathematics, 24(3):363–375.

Manasis, V. and Ntzoufras, I. (2014). Between-seasons competitive balance in European foot-
 ball: Review of existing and development of specially designed indices. Journal of Quantitative
 Analysis in Sports, 10(2):139–152.

Manasis, V., Ntzoufras, I., and Reade, J. J. (2022). Competitive balance measures and the uncer-
 tainty of outcome hypothesis in european football. IMA Journal of Management Mathematics,
 33(1):19–52.

Marden, J. I. (1996). Analyzing and modeling rank data. CRC Press.

Masarotto, G. and Varin, C. (2012). The ranking lasso and its application to sport tournaments.
 The Annals of Applied Statistics, 6(4):1949–1970.

McLachlan, G. J. and Peel, D. (2000). Finite Mixture Models. Wiley Series in Probability and
 Statistics. John Wiley & Sons, New York.

Miller, J. W. and Harrison, M. T. (2018). Mixture models with a prior on the number of components.
 Journal of the American Statistical Association, 113(521):340–356.

Mollica, C. and Tardella, L. (2021). Bayesian analysis of ranking data with the extended plackett–
 luce model. Statistical Methods & Applications, 30(1):175–194.

Murphy, T. B. and Martin, D. (2003). Mixtures of distance-based models for ranking data. Com-
 putational statistics & data analysis, 41(3-4):645–655.

Neal, R. M. (2000). Markov chain sampling methods for Dirichlet process mixture models. Journal
  of Computational and Graphical Statistics, 9(2):249–265.

Owen, P. D., Ryan, M., and Weatherston, C. R. (2007). Measuring competitive balance in pro-
 fessional team sports using the herfindahl–hirschman index. Review of Industrial Organization,
 31(4):289–302.

Pearce, M. and Erosheva, E. A. (2025a). Bayesian rank-clustering. Psychometrika, 90(3):904–931.

Pearce, M. and Erosheva, E. A. (2025b). Modeling preferences: A bayesian mixture of finite mix-
  tures for rankings and ratings. Journal of the American Statistical Association, 120(551):1621–
  1632.

Polson, N. G., Scott, J. G., and Windle, J. (2013). Bayesian inference for logistic models using
  pólya–gamma latent variables. Journal of the American Statistical Association, 108(504):1339–
  1349.

Santi, L. and Friel, N. (2026). The bradley–terry stochastic block model. The Annals of Applied
  Statistics, 20(2):1766–1787.

Szymanski, S. (2001). Income inequality, competitive balance and the attractiveness of team sports.
  Economic Journal, 111(469):69–84.

Szymanski, S. (2003). The economic design of sporting contests. Journal of Economic Literature,
  41(4):1137–1187.

                                                23
Tian, X., Shi, J., Shen, X., and Song, K. (2024). A spectral approach for the dynamic bradley–terry
  model. Stat, 13(3):e722.

Utt, J. and Fort, R. (2002). Pitfalls to measuring competitive balance with gini coefficients. Journal
  of Sports Economics, 3(4):367–373.

Vrooman, J. (1995). A general theory of professional sports leagues. Southern Economic Journal,
  61(4):971–990.

Zimbalist, A. (2002). Competitive balance in sports leagues: An introduction. Journal of Sports
  Economics, 3(2):111–121.




                                                 24
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Posterior team ranks and latent tiers
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Bars: 90% posterior rank intervals
                                                                                                                                                                                                                                                                                                                             NBA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       NFL

  Oklahoma City Thunder                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Seattle Seahawks

        San Antonio Spurs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Denver Broncos

              Detroit Pistons                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Houston Texans

               Boston Celtics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Jacksonville Jaguars
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Los Angeles Rams
            Denver Nuggets
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             New England Patriots
           New York Knicks
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              San Francisco 49ers
       Los Angeles Lakers
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Buffalo Bills
       Cleveland Cavaliers
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Chicago Bears
           Houston Rockets
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Los Angeles Chargers
               Atlanta Hawks
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Philadelphia Eagles
 Minnesota Timberwolves
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Pittsburgh Steelers
            Toronto Raptors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Green Bay Packers
          Charlotte Hornets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Minnesota Vikings
                   Miami Heat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Detroit Lions
              Orlando Magic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Indianapolis Colts
         Philadelphia 76ers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Tampa Bay Buccaneers
               Phoenix Suns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Baltimore Ravens

                  LA Clippers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Carolina Panthers

     Portland Trail Blazers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Atlanta Falcons
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Dallas Cowboys
    Golden State Warriors
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Miami Dolphins
               Brooklyn Nets
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Cincinnati Bengals
               Chicago Bulls
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Kansas City Chiefs
           Dallas Mavericks
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               New Orleans Saints
              Indiana Pacers
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Cleveland Browns
         Memphis Grizzlies
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Washington Commanders
          Milwaukee Bucks
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Arizona Cardinals
    New Orleans Pelicans                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Las Vegas Raiders
         Sacramento Kings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           New York Giants
                     Utah Jazz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         New York Jets
      Washington Wizards                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Tennessee Titans

                                                                          31                                                                            26                                                                                             21                                                                          16                                                                                             11                                                                              6                                                                                  1                                                                                      31                                                                                                       26                                                                                      21                                                                                          16                                                                                                11                                                                                                 6                                                                                                 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Rank (1 = strongest)

                                                                                                                                                                                                                                                                                                                                                                                                                                                   Dahl tier                                                                1                                        2                               3                     Point estimate                                    Dahl−selected                                                                                                           Posterior median


                             NBA posterior tier−clustering                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             NFL posterior tier−clustering
    Washington Wizards                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Tennessee Titans

               Utah Jazz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            New York Jets

      Sacramento Kings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            New York Giants

   New Orleans Pelicans                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Las Vegas Raiders
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Arizona Cardinals
        Milwaukee Bucks
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Washington Commanders
      Memphis Grizzlies
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Cleveland Browns
          Indiana Pacers
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               New Orleans Saints
        Dallas Mavericks
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Kansas City Chiefs
           Chicago Bulls
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Cincinnati Bengals
           Brooklyn Nets
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Miami Dolphins
   Golden State Warriors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Dallas Cowboys
    Portland Trail Blazers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Atlanta Falcons
             LA Clippers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Carolina Panthers
           Phoenix Suns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Baltimore Ravens

      Philadelphia 76ers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Tampa Bay Buccaneers

          Orlando Magic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Indianapolis Colts

              Miami Heat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Detroit Lions
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Minnesota Vikings
       Charlotte Hornets
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Green Bay Packers
         Toronto Raptors
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Pittsburgh Steelers
 Minnesota Timberwolves
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Philadelphia Eagles
           Atlanta Hawks
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Los Angeles Chargers
        Houston Rockets
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Chicago Bears
     Cleveland Cavaliers
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Buffalo Bills
     Los Angeles Lakers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       San Francisco 49ers
        New York Knicks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      New England Patriots
         Denver Nuggets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Los Angeles Rams
           Boston Celtics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Jacksonville Jaguars
          Detroit Pistons                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Houston Texans

      San Antonio Spurs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Denver Broncos

 Oklahoma City Thunder                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Seattle Seahawks
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Seattle Seahawks

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Denver Broncos

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Houston Texans

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Jacksonville Jaguars

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Los Angeles Rams

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        New England Patriots

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               San Francisco 49ers

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Buffalo Bills

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Chicago Bears

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Los Angeles Chargers

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Philadelphia Eagles

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Pittsburgh Steelers

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Green Bay Packers

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Minnesota Vikings

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Detroit Lions

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Indianapolis Colts

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Tampa Bay Buccaneers

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Baltimore Ravens

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Carolina Panthers

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Atlanta Falcons

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Dallas Cowboys

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Miami Dolphins

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Cincinnati Bengals

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Kansas City Chiefs

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      New Orleans Saints

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Cleveland Browns

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Washington Commanders

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Arizona Cardinals

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Las Vegas Raiders

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              New York Giants

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                New York Jets

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Tennessee Titans
                              Oklahoma City Thunder

                                                      San Antonio Spurs

                                                                           Detroit Pistons

                                                                                             Boston Celtics

                                                                                                              Denver Nuggets

                                                                                                                               New York Knicks

                                                                                                                                                 Los Angeles Lakers

                                                                                                                                                                      Cleveland Cavaliers

                                                                                                                                                                                            Houston Rockets

                                                                                                                                                                                                              Atlanta Hawks

                                                                                                                                                                                                                              Minnesota Timberwolves

                                                                                                                                                                                                                                                        Toronto Raptors

                                                                                                                                                                                                                                                                          Charlotte Hornets

                                                                                                                                                                                                                                                                                              Miami Heat

                                                                                                                                                                                                                                                                                                           Orlando Magic

                                                                                                                                                                                                                                                                                                                              Philadelphia 76ers

                                                                                                                                                                                                                                                                                                                                                   Phoenix Suns

                                                                                                                                                                                                                                                                                                                                                                  LA Clippers

                                                                                                                                                                                                                                                                                                                                                                                Portland Trail Blazers

                                                                                                                                                                                                                                                                                                                                                                                                          Golden State Warriors

                                                                                                                                                                                                                                                                                                                                                                                                                                   Brooklyn Nets

                                                                                                                                                                                                                                                                                                                                                                                                                                                    Chicago Bulls

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Dallas Mavericks

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Indiana Pacers

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Memphis Grizzlies

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Milwaukee Bucks

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              New Orleans Pelicans

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Sacramento Kings

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Utah Jazz

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Washington Wizards




                                                                                                                                                                                                                                              P(same tier)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         P(same tier)
                                                                                                                                                                                                                                                                                              0.00                         0.25                    0.50                 0.75                             1.00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    0.00                                 0.25                     0.50                                   0.75                1.00




Figure 2: Posterior team rankings, Dahl representative tiers, and posterior mean co-clustering
matrices for the NBA and NFL. Circles denote posterior median ranks, triangles denote ranks from
the Dahl representative partition, and horizontal bars represent 90% posterior credible intervals for
team ranks. Team colors indicate the Dahl representative tiers, with Tier 1 denoting the strongest
competitive tier. The heatmaps display the posterior mean co-clustering matrices, where each entry
is the posterior mean of the indicator that two teams belong to the same latent tier. Rank 1 denotes
the strongest team.




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             25
