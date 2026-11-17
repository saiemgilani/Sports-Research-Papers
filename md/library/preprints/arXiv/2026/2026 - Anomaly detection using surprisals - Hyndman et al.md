<!-- source: library/preprints/arXiv/2026/2026 - Anomaly detection using surprisals - Hyndman et al.pdf -->
<!-- item: https://arxiv.org/abs/2603.09318 -->
<!-- authors: Rob J Hyndman, David T. Frazier -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-17; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Anomaly detection using surprisals

                                                       Anomaly detection using surprisals

                                                                    Rob J Hyndman
                                            Department of Econometrics & Business Statistics, Monash University
                                                                          and
                                                                    David T Frazier
arXiv:2603.09318v2 [stat.ME] 16 Nov 2026




                                            Department of Econometrics & Business Statistics, Monash University

                                                                             17 November 2026



                                                                                     Abstract

                                                    Anomaly detection methods are widely used but often rely on ad hoc rules or
                                                strong assumptions, and they often focus on tail events, missing “inlier” anomalies
                                                that occur in low-density gaps between modes. We propose a unified framework
                                                that defines an anomaly as an observation with unusually low probability under a
                                                (possibly mis-specified) model. For each observation we compute its surprisal (the
                                                negative log generalized density) and define an anomaly score as the probability
                                                of a surprisal at least as large as that observed. This reduces anomaly detection for
                                                complex univariate or multivariate data to estimating the upper tail of a univariate
                                                surprisal distribution. We develop two model-robust approximations to these tail
                                                probabilities: an empirical approximation based on the observed surprisal distribu-
                                                tion and a GPD approximation that fits a Generalized Pareto Distribution above a
                                                high threshold. For the empirical approximation we give conditions under which
                                                tail ordering is preserved and derive finite-sample confidence guarantees via the
                                                Dvoretzky–Kiefer–Wolfowitz inequality. For the GPD approximation we establish
                                                broad tail conditions ensuring classical extreme-value behavior. Simulations and
                                                applications to French mortality, Test-cricket and Old Faithful geyser data show the
                                                approach remains effective under substantial model mis-specification.

                                           Keywords: Extreme value theory, Generalized Pareto Distribution, Outlier detection, Tail
                                           bounds




                                                                                         1
1    Introduction

Anomaly detection methods are often rather ad hoc and lack a solid theoretical foun-

dation, or they make strong distributional assumptions that may not hold in practice.

We aim to address this by defining anomalies as observations of low probability under

a specified model, and proposing a general framework for anomaly detection that esti-

mates the probability mass associated with observations of equal or lower density (thus

more anomalous). The approach applies to any anomaly detection problem for which a

probability distribution can be defined on the space of observations, including univariate

and multivariate data, and unconditional and conditional distributions. Although it

requires a specified probability distribution, it is robust to substantial mis-specification of

that distribution.

The basic idea is to calculate the surprisal (equal to the negative log density) of each

observation, and then estimate the tail probability from the surprisal distribution. This

gives the probability of obtaining a surprisal at least as large as that of the observation,

and a threshold on these probabilities controls the false positive rate when flagging

anomalies.

Let y1 , . . . , yn be iid observations from a probability distribution F defined on an appro-

priate sample space, and let f be the generalized probability density function of F. That

is, f is defined using Dirac delta functions at jump points of F, so that it represents the

density function if F is continuous, the probability mass function if F is discrete, and a

combination of both if F is a mixture of continuous and discrete components.

The surprisal of observation yi is defined as (Stone 2022)


                                      si = − log f (yi ).                                   (1)


                                              2
While these are better known as “log scores” in statistics (Good 1952), in this context we

prefer the term “surprisal” (coined by Tribus 1961), as it captures the idea that observa-

tions with low density are more “surprising” (and therefore potentially anomalous) than

those with high density. A large value of si indicates that yi is an unlikely value, and so

is a potential anomaly. On the other hand, typical values will have low surprisals. In

information theory, the average surprisal is known as the entropy of a random variable

(Cover & Thomas 2006, Stone 2022) and provides a measure of uncertainty. If f is ob-

tained from a parametric model, then the sum of the surprisals is equal to minus the log

likelihood of the data.

Let G (s) = Pr{S ≤ s} be the distribution function of the surprisal values, where S =

− log f (Y ) and Y ∼ F. Then the probability of observing a value with surprisal at least

as large as s is given by Pr(S ≥ s) = 1 − G (s− ), where G (s− ) = limt↑s G (t). This leads to

a natural way of assigning an anomaly score to each observation yi :

                               pi = Pr(S ≥ si ) = 1 − G (si− ),                            (2)

where si is given by (1). We define anomalies as observations with pi ≤ α, giving a false

positive rate of α if all observations are from F. This is preferable to directly computing

the probabilities from the tail of F, as it allows for anomalies to occur anywhere in the

distribution of F, not just in its tails. For example, anomalies may lie between modes in a

multimodal distribution, or in otherwise low-density regions of the distribution F.

Distance-based approaches (e.g., Wilkinson 2018) instead flag observations that are far

from a centre, using a distance such as |yi − µ̂|/σ̂ or a Mahalanobis distance, ideally with

robust estimates of location and scale. When the density is unimodal and elliptically

symmetric, the surprisal is a monotone function of the Mahalanobis distance, so the two

approaches flag the same observations. They differ when the distribution is skewed or

                                              3
multimodal, as low density then no longer corresponds to large distance from a centre.

The surprisal approach converts the problem of working with F, a potentially multivariate

distribution (or even one on a manifold or some non-Euclidean space), to working with a

univariate distribution G defined on R. We can write


                     G (s) = Pr{− log f (Y ) ≤ s} = Pr{ f (Y ) ≥ e−s }.


This makes clear that the surprisal probability is related to the highest density regions of

the distribution (Hyndman 1996). In fact, every observation with pi ≤ α lies outside the

100(1 − α)% highest density region of F.

If F = N (µ, σ2 ), then pi = 2[1 − Φ(|yi − µ|/σ )], where Φ is the standard Normal

distribution function. In this case, identifying anomalies as observations with pi ≤ α is

equivalent to a z-score test with the threshold set to Φ−1 (1 − α/2). Hence, our approach

can be seen as a generalization of anomaly detection methods based on z-scores including

Grubbs’ test (Grubbs 1950).

It can also be seen as a generalization of other anomaly detection methods. For example,

the Hampel identifier (Hampel et al. 1986, p. 65) flags an observation as an anomaly if

|yi − m|/a > τ, where m is the median and a is the median absolute deviation (MAD)

of the data. The threshold τ is often set under the assumption of a Normal distribution.

When we take a surprisal perspective, this is equivalent to setting


                                F = N (m, a2 /Φ−2 (0.75)).                               (3)


The false anomaly rate is α = 2[1 − Φ(τ Φ−1 (0.75))]. The Hampel identifier is often

applied to time series using a moving window (Davies & Gather 1993), so that each




                                             4
observation is compared with its neighbours. Then m and a in (3) are replaced by


                               mt = median(yt−h , . . . , yt+h ),

                      and       at = median(|yt−h − mt |, . . . , |yt+h − mt |),


giving a different distribution at each time t.

We will usually not know F, and so we need to estimate it from data or from theory. Such

estimates are particularly fragile or uncertain in areas of low density, which is precisely

where we are looking for anomalies. Further, we are seeking a method that does not

make strong distributional assumptions.

                                                 e with generalized density f˜, which
Our approach begins with an assumed distribution F,

may be estimated from data, or obtained from theory. This distribution is used to compute

the surprisal values s̃i = − log f˜(yi ), i = 1, . . . , n.

If we also use the assumed distribution Fe to compute the tail probabilities, we obtain

p̂i = 1{ f˜(y) ≤ e−s̃i }d Fe(y), where 1 is the indicator function. However, this makes the
     R

strong assumption that Fe is an accurate representation of the data, and in practice it may

be poorly estimated or mis-specified.

So, instead, we estimate pi using one of the following two approximations:

   1. Empirical approximation: Use the empirical distribution function of the observed

      surprisals {s̃1 , . . . , s̃n }, so that p̂i is the proportion of surprisals at least as large as s̃i ;

   2. GPD approximation: Fit a Generalized Pareto Distribution (GPD) to the largest

      surprisal values, and use this to estimate the tail probabilities p̂i .

Both approximations allow for considerable mis-specification of the distribution used

to compute the surprisals. The empirical approximation requires only that the ordering


                                                     5
of the surprisals in the tail is similar to what would have been obtained under the

true distribution, while the GPD approximation also requires that extreme value theory

applies to the surprisal distribution.

In Section 2, we develop the necessary theory to support the use of empirical surprisal

probabilities, and identify the conditions under which this will give a good estimate

of the true surprisal probabilities. Similarly, Section 3 provides the theoretical results

needed to use a Generalized Pareto Distribution to approximate the tail of the surprisal

distribution. While we present the main results in terms of iid data, Section 4 shows that

the methods can be applied to conditional distributions as well. We demonstrate the

methods with several simulation experiments in Section 5, and in three applications in

Section 6. A discussion follows in Section 7. The appendix contains the proofs needed for

the results in Sections 2 and 3.




2    Empirical surprisal probabilities

Under the empirical approximation, we estimate pi in (2) by p̂i , the proportion of observed

surprisals s̃1 , . . . , s̃n at least as large as s̃i . The anomaly boundary for a threshold of α

corresponds to the 100(1 − α)% highest density region computed using the quantile

density approach of Hyndman (1996).

Let F (·) denote the true distribution function of Y, and suppose we use Fe to model Y.

For the empirical approximation to be accurate, the ordering of large surprisal values

under the fitted model, F,
                        e should match that under the true distribution, F. Thus, a

sufficient condition is that the true and fitted surprisals are related by a strictly increasing

transformation on the upper tail.



                                               6
Recall that the surprisal under the true distribution is defined as S = − log f (Y ), and

recall that G (s) = Pr(S ≤ s) denotes the CDF of S at s ∈ S ⊆ R, where S denotes the

support of the surprisals. Likewise, let Se = − log f˜(Y ) denote the surprisal under the

                             b n (s) := n−1 ∑n 1[Sei ≤ s] denote the empirical CDF of the
fitted distribution, and let P               i =1

fitted sample Se1 , . . . , Sen . Assumption 2.1 gives a sufficient condition for the empirical

estimator P
          b n (s) to provide an accurate estimate of the upper tail of G (s) in any given

sample.

Assumption 2.1. There exists an s⋆ ∈ R and a function h(·), strictly increasing on [s⋆ , ∞),

such that S = h(Se) almost surely for all Se ≥ s⋆ , and S ≤ h(s⋆ ) for Se < s⋆ .

Lemma 2.1. Let S1 , . . . , Sn be iid with distribution function G. If Assumption 2.1 is satisfied,
                                      p
then, for any δ ∈ (0, 1), and ϵ = log(2/δ)/(2n), with probability at least 1 − δ, for every

Sei ≥ s⋆

                              P
                              b n (Sei ) − ϵ ≤ G (Si ) ≤ P
                                                         b n (Sei ) + ϵ.


Lemma 2.1 implies that when the fitted distribution has tails that are similarly located to

the actual data distribution, then the fitted empirical surprisal probabilities are accurate

measures of the true surprisal probability, G (s). The tails of the fitted distribution need

not be the same as those of the data distribution; beyond a threshold value s⋆ , the two

need only be related through a monotone transformation. So the fitted distribution must

have its regions of low density in the same locations as the true data distribution.

Assumption 2.1 is not satisfied by all pairs of distributions: if the true data has skewness

but the fitted model assumes symmetry, or if there is bimodality in the observed data

that is not modeled, then Assumption 2.1 may not be satisfied.

In other cases Assumption 2.1 holds exactly. If the true and fitted densities are both


                                                  7
decreasing functions of the same distance from the same centre, the two sets of surprisals

are monotone functions of that distance, so h exists with s⋆ equal to the smallest surprisal.

For example, this is true when a Student’s t distribution with k degrees of freedom,

denoted t(k ), is fitted to N (0, 1) data, as in Section 5, or when a multivariate normal

distribution is fitted to data from an elliptical distribution with the same location and the

same scatter matrix up to scale. Because p̂i depends only on the ranks of the surprisals,

two fitted models that rank the largest surprisals in the same order give identical empirical

probabilities. This gives a simple practical check: compute the surprisals under two or

more plausible models (for example, a parametric model and a kernel density estimate)

and compare the observations with the largest surprisals. If they largely agree, the

ordering is unlikely to depend on the choice of model.

Lemma 2.1 also shows how large n must be to obtain a given level of accuracy. For

fixed δ, the half-width ϵ of the band shrinks to zero like n−1/2 and does not depend

on the tail probability of the true distribution. Hence, Lemma 2.1 is informative only

when ϵ is small compared with the tail probabilities of interest. With n = 1000, the 95%

bound gives ϵ ≈ 0.043, which is larger than a threshold of 0.01. A pointwise argument

is less conservative: at a true tail probability of α, p̂i is a binomial proportion with

relative standard error (1 − α)/(nα) ≈ (nα)−1/2 . So the accuracy of the empirical
                        p


approximation is governed by nα, the expected number of observations beyond the

threshold, rather than by n alone. As a rough guide, we suggest nα ≥ 10 (a relative

standard error of about 30%) for the empirical approximation. When nα is smaller, the

GPD approximation of Section 3 is preferable, because it uses the largest 100 × β% of the

surprisals rather than only those beyond the threshold.




                                             8
3    Extreme value theory for the surprisal distribution

The GPD approximation uses extreme value theory applied to the (univariate) surprisal

values. We will show that under weak conditions on the tail of the surprisal distribution,

the excesses of the surprisal over a high threshold converge to a GPD, with the surprisal

distribution in either the Gumbel or Fréchet domain of attraction. This justifies fitting

a Generalized Pareto Distribution (GPD) to the largest surprisal values, and using it to

estimate tail probabilities.

An important precursor to this work is Kandanaarachchi & Hyndman (2022) who pro-

posed estimating F by a leave-one-out kernel density estimate, and then fitting a Gener-

alized Pareto Distribution (GPD) to the most extreme surprisal values. The underlying

idea is that even if F is not particularly well-estimated, the tail of the surprisal distribu-

tion should still be well-approximated by a GPD. Hyndman et al. (2026) provide some

theoretical justification for this approach in the context of kernel density estimation.

Here we extend that idea to allow F to be any continuous distribution, including condi-

tional distributions; certain discrete distributions can be handled at the cost of additional

technicalities, while others would not deliver surprisals with a continuous GPD limit.

Specifically, we set the threshold u to be the 100(1 − β)% sample quantile of {s̃i }in=1 , and

fit a GPD to the excesses s̃i − u of the surprisals above u, obtaining estimates ω̂ and ξ̂ of

the scale and shape parameters. We then estimate the probability of a surprisal at least as

large as that of each observation by

                                      h                       i
                               p̂i = β 1 − Hξ̂ {(s̃i − u)/ω̂ } ,                           (4)


where Hξ is the GPD distribution function given in (5). Observations with s̃i ≤ u are

assigned p̂i = β.

                                              9
To justify this approach, specifically to ensure a Pickands–Balkema–de Haan theorem is

satisfied, we seek conditions on the distribution of the surprisal Se := − log f˜(Y ), where

Y ∼ F, and f˜ is the assumed or estimated density function, which may be distinct

from f . We formulate our results using moments of S,
                                                   e as well as additional regularity

conditions. We believe this formulation is helpful as the moment behavior of Se can

often be directly discerned at a glance and so does not require that the practitioner have

previous knowledge of EVT or any knowledge of the domain of attraction to which Se

belongs. For instance, if we know that Y ∼ N (0, 1) and f˜ = f , then it is immediately

obvious that Se is a shifted and scaled chi-squared random variable, and it is taught in

undergraduate statistics classes that chi-squared random variables have an exponential

moment.

To state our results, we thus maintain the following conditions. They are stated for a

generic random variable S, and we will apply them with S = S.
                                                           e


Assumption 3.1 (Exponential Moment Existence). The random variable S ∈ R is such

that µ = E[S] exists. For some parameters ν > 0 and σ2 > 0, and any λ ∈ R such that
                            2 2
|λ| ≤ 1/ν, E[eλ(S−µ) ] ≤ eλ σ /2 .

Assumption 3.2 (Polynomial Moment Existence). For some q > 1, E[|S − µ|q ] < ∞.

Assumption 3.1 ensures that S is a sub-exponential random variable, and is easy to check

for many distributions. For example, if Y ∼ t(k ), k ≥ 1, then S = − log f (Y ) has a

moment generating function, on a certain domain, which implies Assumption 3.1 is

satisfied: the quantities µ, σ2 and ν can be directly calculated from the MGF and are

functions of the degrees of freedom parameter k.

Assumption 3.2 will be satisfied in cases where S only admits a polynomial moment.


                                            10
For instance, if we compute the surprisals using a standard Gaussian density f˜, so that

Se = c + Y 2 /2, but in fact Y ∼ t(k), then Se will satisfy Assumption 3.2 so long as k > 2;

i.e., provided the observed data have a finite variance.

Define the GPD distribution function
                          
                           1 − (1 + ξy)−1/ξ , ξ ̸= 0, 1 + ξy > 0
                          
                 Hξ (y) =                                                                      (5)
                           1 − e−y ,
                          
                                               ξ = 0.


Theorem 3.1. Let Y1 , . . . , Yn be an iid sequence from F, and let Se = − log f˜(Y ), where Y ∼ F,

with µ = E[Se]. Let the regularity conditions in Assumption B.1 be satisfied with S = S.
                                                                                      e Then,

there exists a scale function ω (u) > 0 such that
                                                            !
                               (Se − µ) − u
               lim sup Pr                   ≤ y (Se − µ) > u − Hξ (y) = 0,
               u ↑ ∞ y ≥0          ω (u)

with ξ = 0 under Assumption 3.1 or 0 ≤ ξ ≤ 1/q under Assumption 3.2.

Theorem 3.1 shows that the conditional excess distribution function of the surprisal

converges to the GPD where the value of ξ is constrained by the number of finite moments

that Se possesses. If the surprisal distribution has at least an exponential moment and

full support, then the conditional excess distribution function of the surprisal behaves

like a shifted exponential distribution; if instead the surprisal only has a polynomial

moment, when ξ ̸= 0 the conditional excess distribution function converges to the Pareto

distribution. Theorem 3.1 therefore justifies the peaks-over-threshold approach: the fitted

GPD should give an accurate approximation to the true surprisal probability in large

samples, provided we can accurately estimate the parameters of the Generalized Pareto

Distribution (Coles 2001, Theorem 4.1).

It is possible to link Assumptions 3.1 and 3.2 to the domain of attraction conditions

usually considered in extreme value theory. For simplicity, let us assume that range of

                                                11
Se is R. Under technical conditions, Assumption 3.1 then implies that the distribution

of S,
   e denoted by G
                e herein, is in the Gumbel domain of attraction, i.e., H0 in Equation 5.

In contrast, under Assumption 3.2, G
                                   e can be in either the Gumbel or Fréchet domain

of attraction: where q denotes the number of assumed moments, we only have that

0 ≤ ξ ≤ 1/q and so cannot exclude the Gumbel domain of attraction; if, however, we

know that the (q + 1)-th moment of (Se − µ)+ is infinite, then under Assumption 3.2 we

          e is in the Fréchet domain of attraction and 0 < 1/(1 + q) ≤ ξ ≤ 1/q.
have that G

Assumptions 3.1 and 3.2 are convenient sufficient conditions, but they are not necessary

for the GPD approximation. The GPD limit for threshold excesses holds whenever G
                                                                               e is

in the domain of attraction of an extreme value distribution (Coles 2001, Theorem 4.1),

and this requires no moments. Because Assumption 3.2 needs q > 1, Theorem 3.1 only

allows ξ < 1, and so excludes surprisal distributions without a finite mean. These can

still be handled by the GPD approximation. For example, if the surprisals are computed

from a Gaussian density but Y ∼ t(1), then Se = c + Y 2 /2 has no finite mean, but
                          √
Pr(Se − c > s) = Pr(|Y | > 2s) is proportional to s−1/2 for large s, so G
                                                                        e is in the Fréchet

domain of attraction with ξ = 2. The cost of such heavy tails is statistical rather than

theoretical: ξ is harder to estimate, and extrapolation beyond the data is less reliable.




4    Applicability for conditional distributions

The theoretical results in Lemma 2.1 and Theorem 3.1 assume that the surprisal is based

on iid data Y generated from some unknown distribution. In this way, these results

are agnostic to the dimension of Y; the resulting surprisal Sei = − log f˜(Yi ) is always

univariate, and remains iid since any function of Y is also iid.



                                            12
However, there are many modeling situations, such as regression settings, where we

are not necessarily interested in measuring the surprisal that results from the joint

distribution of the data, but along a fixed vector of conditioning variables (e.g., age, or

gender). In such cases, we can think of our observed data being the variables Y = ( Z, X )

where Z is some outcome of interest and X are variables that are used to predict or

explain Z. In such cases, we can directly apply the surprisal approach with a conditional

model of the form f˜Z (z | X = x), and the surprisal Se = − log f˜Z ( Z | X = x) can be

thought of as being computed “conditional on a given X = x”.

For a fixed vector of the conditioning variables, it is not hard to see why our theoretical

results will remain valid: by fixing X = x, since we observe iid Y = ( Zi , Xi ), the

distribution of Z | X = x is also iid conditional on X = x, and the resulting theory

applies. That is, for example, if we wish to calculate surprisals at a fixed value of the

covariates x, then Lemma 2.1 and Theorem 3.1 can be applied conditional on this fixed

set of covariates.

However, if we wish to calculate surprisals across both the outcomes and covariates (i.e.,

when allowing both Z and X to vary), then what is a surprisal may change from instance

to instance. To see why, consider the simple example where we wish to detect surprisals

using a simple Gaussian regression model for Z | X, so that


                     Sei = − log f˜Z ( Zi | Xi ) = c + ( Zi − β 0 − β 1 Xi )2 /(2σZ2 ).


Now, Sei can be large for two distinct and interrelated reasons: either because Z itself is

large, relative to the observed values of β 0 + β 1 X, or because X is atypical, where the

assumed regression may be a poor approximation, so that Z − β 0 − β 1 X is large.

That is, in the general case, where we are searching for surprisals over the conditional


                                                    13
model without X being fixed, the behavior of Sei is determined by that of the joint

distribution:
                                Z
                Pr(Sei > s) =       1(− log f˜Z (z | x) > s) f Z (z | x) f X ( x) dz dx,


where f Z and f X denote the true conditional and marginal densities. This clarifies that

extreme behavior in Sei can result from extreme values of Z, X, or simply values of Z and

X where f˜Z ( Z | X ) is very small. The latter can occur even when Z and X take on values

that are typical for their marginal distribution, but which are not well-captured by the

assumed conditional model.

This determines which tail probability is estimated. When surprisals are pooled over

observations with different covariate values, as in the French mortality and cricket

applications, the empirical and GPD approximations estimate the marginal tail probability

Pr(Se ≥ s̃i ) given above, where ( Z, X ) varies over its joint distribution. This is an average

over x of the conditional tail probabilities Pr(Se ≥ s̃i | X = x). The two coincide when the

conditional distribution of Se given X = x does not depend on x. This holds when the

surprisal depends on the data only through a standardized residual whose distribution

does not depend on x. Examples are the Gaussian regression above when the model

is correct, where 2(Sei − c) has a χ21 distribution at every x, and the French mortality

application in Section 6, where the surprisal is computed from the standardized residual

of each series. When the conditional distribution of Se depends on x, as in the Binomial

model for the cricket data where the number of innings differs between batters, an

observation is flagged when its surprisal is unusual relative to all observations, not only

those with the same covariate values. Estimating the conditional tail at a fixed x requires

many observations at (or near) that value of x, or else computing the tail probability

directly from the conditional model, which relies on that model being correct.

                                                  14
5     Experiments

5.1   Standard univariate normal values

Although we need to assume some density function f when computing surprisals, we

want the resulting tail probabilities to be robust to a mis-specified distribution. Suppose

we generate 1000 observations from a N (0, 1) distribution f , but use a t(4) distribution fe

to compute the surprisal values. The empirical tail probabilities, and those obtained using

the GPD approximation, should still give reasonable estimates of the tail probabilities,

despite the incorrect distribution being used to compute the surprisals.

To study the effect of the assumed distribution, we generate 1000 observations from each

of the N (0, 1), t(4) and t(1) distributions, and compute the surprisal values using both a

standard Normal density and a t(4) density. Then, for each set of surprisal values, we

estimate the surprisal tail probabilities in three ways: (a) using the same distribution

used to compute the surprisal values; (b) using the empirical approximation; and (c)

using the GPD approximation fitted to the largest 100 surprisal values.

Figure 1 shows the estimates for observations greater than 2.5. In the left panel (N (0, 1)

data), the probabilities computed directly from the incorrect t(4) density are far too large,

but the empirical and GPD approximations are close to the truth under both assumed

densities. The middle panel (t(4) data) shows the converse: the probabilities computed

directly from the incorrect Normal density are far too small, but the empirical and

GPD approximations remain relatively accurate. In the right panel (t(1) data), neither

assumed density is correct. Gaussian surprisals do not have a finite mean in this case, so

Theorem 3.1 does not apply, but, as noted in Section 3, they are in the Fréchet domain

of attraction with ξ = 2, so the GPD approximation is still justified. The t(4) surprisals


                                             15
                                  Data: Normal                                 Data: t(4)                                Data: t(1)
              0.08


              0.06
Probability




              0.04


              0.02


              0.00
                     2.5   2.6   2.7   2.8   2.9   3.0      3.1          4      6       8       10      0          50         100         150
                                                                                    y

                                                            Assumed distribution f          Normal     t(4)



                                 Surprisal probability p^         True       Assumed distribution    Empirical distribution         GPD



Figure 1: Left: Observations are generated from a N (0, 1) distribution. Middle: Observations are

generated from a t(4) distribution. Right: Observations are generated from a t(1) distribution.

Assumed distribution fe indicates which distribution was used to compute the surprisal values.

Surprisal probability p̂ shows how the tail probabilities were computed. This demonstrates that

the surprisal probabilities computed using the empirical distribution or under the GPD are still

relatively accurate, even when the wrong distribution is used to compute the surprisal values.


satisfy Assumption 3.1. Nevertheless, the empirical and GPD approximations are again

close to the truth under both assumed densities, while the probabilities computed directly

from either density are far too small.

So even when we don’t know the distribution of the data, we can use an incorrect

assumed distribution to compute the surprisals, and then apply either the GPD or the

empirical approximation to obtain good estimates of the surprisal probabilities.




                                                                              16
5.2   Bivariate gamma values

The quality of the approximation used depends on the amount of data available, so

in this next experiment we compare the tail probabilities of the different approaches

across sample sizes. Let Y = (Yi,1 , Yi,2 )′ where Yi,j are independent Gamma(2,2) random

variables. We generate n observations from this bivariate distribution, and explore the

quality of the probability estimates as n increases from 100 to 10, 000. The surprisal values

are computed using the correct distribution, as well as three incorrect distributions, each

with independent components: a bivariate normal distribution with mean (1, 1)′ and

covariance matrix 0.5I; noncentral t(4) components with mean 1; and Exponential(1)

components (i.e., Gamma(1,1)). For each set of surprisal values, we estimate the tail

probabilities in two ways: (a) using the empirical approximation; and (b) using the GPD

approximation fitted to the largest 10% of surprisal values. We repeat this experiment

1000 times for each sample size. The anomaly rate shown is a loess smooth of the

proportion of anomalies detected when α = 0.01 for different sample sizes, along with

95% confidence intervals. The false anomaly rate under the true distribution is, of course,

0.01. The supplementary material repeats the experiment with the GPD fitted to the

largest 5% and 20% of surprisal values; at α = 0.01 the results are almost unchanged.

The empirical approximation always flags exactly ⌊nα⌋ observations, whatever distribu-

tion is used to compute the surprisals, so its false anomaly rate is ⌊nα⌋/n under all four

assumed distributions. This falls below α whenever nα is not an integer, which, rather

than estimation error, explains its shortfall at small n. The false anomaly rate does not

show whether the same observations are flagged. The Gamma and Normal surprisals are

not monotonically related, even in the tail, because the Gamma surprisal is unbounded

as either component approaches zero while the Normal surprisal is not. The GPD ap-


                                             17
               0.013




               0.012
                                                                                       Method
                                                                                          Empirical (Gamma11)
               0.011                                                                      Empirical (Gamma22)
Anomaly rate




                                                                                          Empirical (Normal)
                                                                                          Empirical (t)
               0.010                                                                      GPD (Gamma11)
                                                                                          GPD (Gamma22)
                                                                                          GPD (Normal)
               0.009                                                                      GPD (t)




               0.008




                        100                       1000                         10000
                                              Sample size n


                 Figure 2: Estimated false anomaly rate under different approximations when α = 0.01.


proximation flags slightly too many anomalies in small samples, but this bias disappears

as n increases. Among the GPD fits, using a Student-t reference distribution performs

nearly as well as using the true model, whereas using a Normal reference distribution

is noticeably worse even at large sample sizes. The reason is tail mismatch: the Normal

distribution is lighter-tailed than the true Gamma distribution, while the Student-t is

heavier-tailed. This suggests that it is safer to err on the side of assuming heavier tails,

as underestimating tail heaviness leads to slow convergence, while overestimating tail

heaviness incurs relatively little cost.



5.3                    Inlying anomalies in bimodal data

The previous experiments only involve anomalies in the tails of the distribution. The

surprisal approach also finds inlying anomalies, such as observations in the low-density

                                                              18
gap between the modes of a multimodal distribution. To demonstrate this, we generate

n = 1000 observations, of which 990 are drawn from the bimodal mixture 12 N (−4, 1) +
1                                                                          2
2 N (4, 1), and the remaining 10 are inlying anomalies drawn from N (0, 0.5 ), which lie in

the gap between the two modes.

We compare six methods. In each case the anomaly probability is estimated and an

observation is flagged as an anomaly if the probability is at most α = 0.01. The first

four use surprisals, computed from either the true mixture density or a two-component

Gaussian mixture fitted to the data by maximum likelihood (the fit includes the anomalies,

so it is itself slightly mis-specified), with tail probabilities estimated using either the

empirical approximation or the GPD approximation fitted to the largest 10% of surprisal

values. The fifth is the local outlier factor (LOF) of Breunig et al. (2000), a standard

density-based method that compares the local density around each observation to that

of its neighbours. We use k = 50 nearest neighbours (5% of n), and flag the 1% of

observations with the largest LOF scores, so that it can be compared with the other

methods at the same level. The sixth is the Hampel identifier, a robust distance-based

method, with pi computed from the Normal distribution in (3) using the median and

MAD of the data.

Figure 3 shows one simulated data set, and Table 1 summarizes 500 repetitions. LOF

finds only about half of the inlying anomalies. It is also sensitive to k: with small k the 10

anomalies are each other’s nearest neighbours, so they look like a small cluster rather

than anomalies, and in a preliminary run with k = 5 and k = 10 almost none were found.

The Hampel identifier finds none of the inlying anomalies, and flags no observations

at all. The inlying anomalies lie near the median, where the distance is smallest, and

the MAD of the bimodal data (about 6) is so large that even observations in the outer


                                             19
                                                   Empirical (true mixture)




                                                     GPD (true mixture)




                                               Empirical (fitted mixture)




                                                    GPD (fitted mixture)




                                                            LOF




                                                      Hampel identifier




                       −4                                   0                              4                 8
                                                                y

             Status     Flagged: inlying anomaly          Flagged: other      Missed anomaly   Not flagged



Figure 3: One simulated data set from the bimodal experiment, with 10 inlying anomalies between

the modes. Each panel shows the observations flagged as anomalies at α = 0.01 by one method.

Points are jittered vertically to reduce overplotting.


tails of the modes are not far enough from the median to be flagged. In contrast, all four

surprisal-based methods identify most of the inlying anomalies, because the density is

very low in the gap between the modes, and they do not depend on a neighbourhood

size. The few anomalies that are missed are those furthest from zero, which lie closer to

the modes and so are not truly unusual under the mixture. The empirical approximation

is limited by nα = 10: at most about 10 observations can be flagged, and some of these


                                                             20
Table 1: Average detection rate of the 10 inlying anomalies, and average false anomaly rate

among the 990 observations from the mixture, over 500 simulated data sets with α = 0.01.


            Method                        Detection rate    False anomaly rate

            Empirical (fitted mixture)              0.874                 0.001

            Empirical (true mixture)                0.881                 0.001

            GPD (fitted mixture)                    0.959                 0.003

            GPD (true mixture)                      0.964                 0.003

            Hampel identifier                       0.000                 0.000

            LOF                                     0.514                 0.005


are taken up by extreme observations in the tails of the modes. The GPD approximation

detects more of the inlying anomalies at the cost of a slightly higher false anomaly rate,

which remains well below α. The results using the fitted mixture are almost identical to

those using the true mixture, so the density need not be known.




6     Applications

6.1   French mortality rates

French mortality rates, disaggregated by age (single years) and sex, are available from

the Human Mortality Database (2025). We will consider male and female data from 1816

to 1999 over ages 0 to 85, giving 172 separate time series, each of length 184.

Figure 4 shows the data for both sexes and all ages. The mortality rates have improved

over time for all ages, especially since 1950. Infant mortality (age 0, shown as the top



                                             21
purple line) is much higher than the rest of childhood, with mortality rates at a minimum

at about age 10 in all years. The highest mortality rates are for the oldest age groups. The

effects of the two wars are particularly evident in the male mortality rates.

                            Female                                 Male




            0.1000


                                                                                        Age
                                                                                              80
Mortality




            0.0100
                                                                                              60

                                                                                              40

                                                                                              20
            0.0010
                                                                                              0




            0.0001

                     1850   1900     1950      2000        1850   1900    1950   2000
                                                 Year


Figure 4: French mortality rates by sex and age from 1816 to 1999. We use a log scale because

the rates are vastly different for different age groups.


We treat each age–sex series as a separate univariate time series, and use the moving-

window version of the Hampel model (3) with h = 7, so the running median mt and

MAD at are computed over a 15-year window. The first and last 7 years of each series

are not tested, as the window is incomplete. Because each MAD is computed from only

15 observations, the standardised residuals (yt − mt )/at have much heavier tails than a

Normal distribution. Following the advice in Section 5 to err on the side of heavier tails,

we replace the Normal distribution in (3) by a t(4) distribution with the same median and

MAD, and compute the surprisal of each standardised residual under this distribution.

Under the model, the standardised residuals have the same distribution in every series,

and so do their surprisals. So rather than estimating the surprisal tail probabilities

                                                  22
           French mortality anomalies
                                    Female                                                                    Male




                    1849                                                              1849      1870                        1914     1944
      75                                          1918   1919                 75
            1832           1871                                                    1832      1855      1871                        1940




      50                                                                      50
Age




                                                                        Age
      25                                                                      25




      0                                                                       0

             1840     1860        1880     1900      1920       1940                1840     1860      1880          1900   1920    1940
                                    Year                                                                  Year


Figure 5: Anomalies identified in the French mortality data by year and age. They coincide with

wars and epidemics in French history.


separately within each series, from only 170 values, we pool the surprisals from all

series, giving n = 29,240. We then compute the surprisal probabilities using the GPD

approximation fitted to the largest 10% of the surprisals, so nβ ≈ 2,924, with α = 0.01.

With so many observations, there is a high likelihood of many false positives (about 292

are expected), so we only retain anomalies when at least three age groups are anomalous

in the same year, and for the same sex. This results in 309 anomalies out of 31648

observations. Figure 5 shows these anomalies, which coincide with various wars and

epidemics that have occurred over French history (Bourdelais & Raulot 1987, Glei et al.

2025):

       • 1832, 1849: Cholera outbreaks

       • 1855: Crimean War (males aged 20–25)


                                                                       23
   • 1870: Franco–Prussian war

   • 1871: Repression of the ‘Commune de Paris’

   • 1914–1918: World War I

   • 1918–1919: Spanish flu outbreak

   • 1940, 1944: World War II

The empirical approximation gives almost the same result. With nα ≈ 292, it is well

within the guideline of Section 2. Using it instead of the GPD approximation, the same

filtering rule gives 287 anomalies rather than 309, all of which are also found by the GPD

approximation, and exactly the same years are identified. Supplementary material gives

extreme value diagnostics for the GPD fit, and shows that the anomalous years are the

same for thresholds between β = 0.03 and β = 0.1.

The theory in Sections 2 and 3 assumes independent observations, but these surprisals

are dependent. Within each series, the median lag-one autocorrelation of the surprisals is

0.21, and a surprisal above the 90% quantile is followed by another in the next year with

probability 0.25, rather than 0.1. The surprisals are also correlated across ages in the same

year, most strongly in years of war and epidemic. This dependence does not change what

is being estimated: pi is a marginal tail probability, and for an approximately stationary

sequence with weak serial dependence, the empirical distribution of the surprisals still

estimates the marginal distribution consistently, and the threshold excesses still have an

approximate GPD marginal distribution (Coles 2001, Ch. 5). It does reduce the precision.

The effective sample size is smaller than n, so the bound in Lemma 2.1 is optimistic, and

the GPD fit treats the exceedances as independent and so understates the uncertainty of

its parameters. Declustering or estimating the extremal index would be needed to model

the clusters themselves, for example to estimate the probability of an anomalous year,


                                             24
but not to estimate pi . The filtering rule above makes use of the dependence across ages:

a war or epidemic produces anomalies in many age groups in the same year, whereas

false positives are scattered.



6.2   Test cricket not outs

Career batting data for all men to have played Test cricket between 1877 and 6 October

2025 were obtained from Hyndman (2026). We will investigate if there are some batters

who have an unusually high proportion of innings where they have not been dismissed,

known as a “not out”. The data set contains results from 92646 innings, of which 11943

were not outs. So the overall proportion of not outs is 11943/92646 = 0.129.

Batters who bat early in the batting order are more likely to be dismissed than those who

bat last, but the data do not record batting position. However, the best batters tend to bat

early, leaving the least skilled batters (usually specialist bowlers) to bat last. A measure

of batting skill is the number of runs scored per innings (RPI), the uncensored batting

average. (Unlike the conventional batting average, RPI is not directly affected by the

number of not outs.) Figure 6 shows the proportion of not outs for each batter against

their RPI. The relationship is slightly U-shaped: weaker batters are disproportionately

likely to be the “last man standing”, while the very best batters are harder to dismiss.

The horizontal patterns in the grey points are due to the discrete nature of the data, as

batters with few innings can only have a small number of possible proportions.

The style of play and playing conditions have also changed considerably over almost 150

years of Test cricket. To account for these changes, and for the variation in batter skills,

we construct a generalized additive model (Wood 2017) for the number of not outs as

a function of RPI and the year in which the batter started playing. It is natural to use a

                                            25
                         1.00




                         0.75
Proportion of not outs




                                                                                       Innings >= 20
                         0.50                                                              FALSE
                                                                                           TRUE




                         0.25




                         0.00

                                0        30                60              90
                                                  Runs per innings


Figure 6: Proportion of not outs for each batter as a function of their runs per innings. Batters

with fewer than 20 innings are shown in grey.


Binomial distribution with a logit link function:

                                    NotOuts | RPI, Start ∼ Binomial(n = Innings, q),

where q denotes the probability of a batter not being dismissed in an innings,

                                         log(q/(1 − q)) = g1 (RPI) + g2 (Start),

and g1 () and g2 () are smooth functions estimated nonparametrically using penalized

regression splines in the mgcv package (Wood 2025).

Figure 7 shows the estimated functions. The probability of a not out decreases as RPI

increases to about 30, and then increases again for the very best batters, although the

confidence interval is very wide above about 50 as there are few batters with RPI that

high. The probability also increases with the year of debut until about 1975, and then

                                                             26
                      s(RPI)                                                      s(Start)
                                                                            0.2
                  2


                  1                                                         0.0
Partial effect




                                                          Partial effect
                  0
                                                                           −0.2


                 −1
                                                                           −0.4

                 −2
                                                                           −0.6
                       0       30    60   90                                      1880       1920      1960   2000
                                    RPI                                                             Start
                                           Basis: TPRS                                                         Basis: TPRS



Figure 7: Estimated smooth functions g1 and g2 in the model for not outs, with 95% confidence

intervals.


decreases. This is likely due to the introduction of limited-overs cricket in the 1970s, after

which batters in Test cricket became more aggressive.

Now we can use the fitted model to compute the surprisals from the Binomial distribution,

and find the most anomalous batters. While the Binomial distribution is probably a good

first approximation, it does assume that the probability of a batter being dismissed does

not change over their career, which is an unlikely assumption as it does not allow for the

development of skill, the value of experience, or the effect of aging. So we will use the

GPD approximation to compute the surprisal probabilities. With α = 0.01, 33 of the 3214

batters are flagged as anomalies; we discuss the two most anomalous.

The largest surprisal is for South African Shaun Pollock, who had 39 not outs in 156

innings, which is much higher than the expected number of not outs of 156 × 0.091 = 14.1.

Pollock was a bowling all-rounder and a capable lower-order batter, who often built

partnerships with the weakest batters.

The next most anomalous batter is New Zealander Trent Boult, a specialist bowler who


                                                         27
batted last and showed an unusual flair for entertaining batting. He had 46 not outs in 94

innings, compared to the expected number of 94 × 0.234 = 22.0.

Neither batter’s proportion of not outs is exceptional by itself (16 batters with at least 20

innings have a higher proportion than Boult), but they become anomalous once their RPI

and year of debut are taken into account. Because we have used a statistical model, we

have been able to account for the particular features of this data set, such as the discrete

nature of the data, and the changing variance, to identify observations that are anomalous

in the context of the model.

Here the choice of approximation makes almost no difference. With 3214 batters, the

empirical approximation gives the same ten most anomalous batters in the same order,

and the probabilities for Pollock and Boult are 0.0003 and 0.0006, compared with 0.0003

and 0.0004 from the GPD approximation. The sample is large enough that nα is not small,

so the empirical approximation is already accurate.



6.3   Old Faithful eruptions

Our third application is to the Old Faithful geyser in Yellowstone National Park. The

oldfaithful data set in the weird package (Hyndman 2026) contains the duration of each

of 2097 eruptions between 2017 and 2023, along with the waiting time until the following

eruption, both in seconds, compiled from observations recorded at GeyserTimes (https:

//geysertimes.org). The joint distribution of duration and waiting time is bimodal:

there is a cluster of short eruptions followed by short waits, and a larger cluster of

long eruptions followed by long waits, with a sparsely populated region between them.

Observations in that region are inlying anomalies, and none of them would be found

by a method that only looks for extreme values of each variable, or one that assumes a

                                             28
unimodal elliptical distribution.

We model the density with a Gaussian mixture model fitted using the mclust package

(Scrucca et al. 2016), which selects the number of components by BIC, and use it to

compute the surprisal of each eruption. We then estimate the surprisal probabilities using

both the empirical and the GPD approximations (the latter fitted to the largest 10% of

surprisals), and flag eruptions with probability at most α = 0.01. The fitted model is itself

only an approximation to the data-generating process, and is estimated from data that

include the anomalies, which is the situation the tail approximations are meant to handle.


                         7000
Waiting time (seconds)




                         6000




                         5000




                         4000




                         3000


                                0       100                          200             300
                                              Duration (seconds)

                                    Flagged   Neither    Empirical only    Both



Figure 8: Old Faithful eruption durations and waiting times. Grey contours show the 50%, 90%

and 99% highest density regions of the fitted Gaussian mixture model. Eruptions with surprisal

probability at most 0.01 are highlighted, according to whether they were flagged using the GPD

approximation, the empirical approximation, or both.


Figure 8 shows the results. The GPD approximation flags 12 eruptions and the empirical

approximation flags 20; all 12 of the former are also flagged by the latter. Some of the

                                                  29
anomalies are extreme in at least one variable, such as the eruption apparently lasting

one second, but several lie in the sparse region between the two clusters, and away from

both of them. For example, the three eruptions of 170 to 180 seconds that were followed

by waits of about an hour are not extreme in either variable on their own, but their

combination falls in a region of very low density. The empirical approximation flags

more observations, probably because its probabilities near the threshold are noisy, with

only about 21 observations below α = 0.01, whereas the GPD approximation smooths the

tail of the surprisal distribution. The two approximations agree on the most anomalous

eruptions.




7    Discussion

The surprisal of an observation measures how unusual it is under a specified distribu-

tional model, and our tail approximations remain accurate even when that model is

mis-specified. Methods that compute anomaly scores directly from the assumed distribu-

tion do not have this property, as Figure 1 shows. Converting a multivariate (or otherwise

complex) problem into estimating the upper tail of a univariate surprisal distribution lets

us use standard empirical and extreme-value methods.

Our theoretical results make clear what kind of mis-specification can be tolerated. Anoma-

lies are defined relative to regions of low density of F, but are identified using an assumed

distribution F.
             e For the empirical approximation to be reliable, the assumed model must

correctly identify the locations of these low-density regions, even if it does not accurately

capture the shape of the tail. Assumption 2.1 formalizes this requirement: the true and

fitted surprisals need only agree up to a strictly increasing transformation on the ex-

treme tail. When this condition holds, Lemma 2.1 guarantees that the empirical surprisal

                                             30
probabilities form a valid uniform confidence band for the true tail probabilities on the

upper tail. This does not require Fe to have the correct tail behavior or even the correct

distributional form, only the correct tail ordering. When the condition fails, such as

when the assumed model imposes symmetry where the data are skewed, or unimodality

where the data are multimodal, the empirical approximation no longer provides uniform

guarantees. In practice, such gross mis-specifications should be identifiable through

exploratory data analysis.

The GPD approximation offers a complementary route to estimating surprisal tail prob-

abilities. Our extreme-value results show that under broad moment conditions on the

surprisal (an exponential moment, or only a polynomial moment), together with mild

regularity conditions, the excesses of the surprisal over a high threshold converge to a

Generalized Pareto Distribution. These conditions encompass almost all common statis-

tical models. Thus, the GPD approximation can be expected to estimate the tail of the

distribution of Se well even when the assumed distribution is only loosely connected to

the true one. As with the empirical approximation, these are also accurate estimates of the

true tail probabilities pi provided the assumed and true distributions order the surprisals

in the same way above the threshold. This depends on the assumed distribution rather

than on the sample size.

The GPD approximation also requires a threshold. We have used β = 0.1 throughout.

In the bivariate Gamma experiment, the false anomaly rate at α = 0.01 was almost the

same for β between 0.05 and 0.2, but at α = 0.001 a threshold as low as β = 0.2 led to

too few anomalies when the assumed distribution was lighter-tailed than the data (see

the supplementary material). So we suggest β = 0.1 as a default, with smaller values

when n is large and very small tail probabilities are of interest. The choice can be checked


                                            31
with standard peaks-over-threshold diagnostics such as mean residual life and parameter

stability plots (Coles 2001, Ch. 4), which the supplementary material gives for each of

our applications. A systematic study of threshold selection for surprisal data is a topic

for future work.

In practice, the choice between the empirical and GPD approximations depends on the

sample size, n, and the desired level of significance, α. The empirical approximation

requires no tuning or model estimation, and provides finite-sample uniform error control,

but it can be noisy when nα is small; as discussed in Section 2, we suggest nα ≥ 10

as a rough minimum. The GPD approximation is most useful when nα is small, as it

can reduce variance and allow extrapolation beyond the observed maximum, but it

requires choosing a threshold and fitting a parametric model to the tail, which introduces

additional complexity and potential for mis-specification. For the GPD approximation,

what matters is the number of exceedances, nβ, rather than nα. In the bivariate Gamma

experiment, the false anomaly rate of the GPD approximation at α = 0.01 was 0.013

with nβ = 10 exceedances, but within 0.001 of the nominal rate once nβ ≥ 50 (that is,

n ≥ 500 with β = 0.1), so we suggest nβ ≥ 50 as a rough minimum. When the surprisal

distribution exhibits discreteness, spikes, or other non-smooth features that one may not

wish to smooth away with a parametric tail model, the empirical approximation may

be preferable. Often it is worth computing both, as a check on each other. While both

approaches can be expected to perform well under moderate model mis-specification,

neither approach is guaranteed if the mis-specification is severe enough that the tail

orderings of the true and fitted distributions differ substantially.

Surprisals are defined in the same way for discrete, continuous and mixed distributions,

and need no notion of distance or centre, which is hard to define for skewed, multi-modal,


                                             32
or high-dimensional data. The method is also cheap to compute: surprisal computation is

linear in the sample size, empirical tail estimation requires only sorting, and GPD fitting

is fast even for very large datasets.

Because anomalies are defined by low density rather than by distance from a centre, the

framework finds inlying anomalies between the modes of a multimodal distribution

as well as outlying anomalies in the tails. In the bimodal simulation in Section 5, the

surprisal-based methods find most of the inlying anomalies while the local outlier factor,

a standard density-based method, finds about half, and the Hampel identifier, a robust

distance-based method, finds none. In the Old Faithful application, several eruptions

are flagged because their combination of duration and waiting time falls between the

two clusters, although neither value is extreme on its own. In both cases the Gaussian

mixture was fitted to data that included the anomalies, and the empirical and GPD

approximations still worked.

Our theory assumes independent observations. With serially dependent data, such as

the French mortality series, both approximations still estimate the marginal tail probabili-

ties, but with less precision than the same number of independent observations would

give, and anomalies tend to occur in clusters. Extending the finite-sample guarantee

of Lemma 2.1 to dependent data, and using the extremal index to describe clusters of

anomalies, are topics for future work.

The surprisals depend on how the assumed distribution is estimated. If the data contain

anomalies, a non-robust estimate can be distorted by them, inflating the density near the

anomalies and so masking them. Robust estimation methods should therefore be used

where possible, and the surprisal framework allows any estimate of F,
                                                                   e including a robust

one. For example, the French mortality application uses a running median and MAD to

                                            33
define the conditional distribution for this reason.

The surprisal framework rests on a clear definition of an anomaly as an observation

of low probability, and gives both finite-sample and extreme-value guarantees for the

resulting anomaly scores, without requiring the model to be correct. The working model

is used only to compute the surprisals; the tail probabilities are then estimated from the

surprisals themselves, using either their empirical distribution or a fitted GPD. So the

model must rank the observations correctly in the tail, but need not get their probabilities

right. In the simulations and in all three applications this was enough. Using models

that were at best approximations, the approach found the wars and epidemics in two

centuries of French mortality data, the batters with unusually many not outs once their

skill and era were taken into account, and the Old Faithful eruptions whose duration and

waiting time are each unremarkable but rare in combination.

Our methods are implemented in the weird R package (Hyndman 2026), which com-

putes surprisals and estimates their tail probabilities using both the empirical and GPD

approximations.



Software and reproducibility

All results presented here can be reproduced using the data and code available at https:

//github.com/robjhyndman/Surprisal_Theory. The analysis was conducted using R

version 4.6.1 (R Core Team 2026), with the following R packages: weird (Hyndman 2026),

tsibble (Wang et al. 2026), targets (Landau 2026, 2021), ggplot2 (Wickham et al. 2026,

Wickham 2016), and other tidyverse (Wickham et al. 2019) packages.




                                            34
Funding

Both authors are funded by the Australian Research Council through Discovery Project

DP250100702. Rob Hyndman is a member of the Australian Research Council Industrial

Transformation Training Centre in Optimisation Technologies, Integrated Methodologies,

and Applications (OPTIMA), Project ID IC200100009.



Generative AI statement

The authors used Claude Code (Anthropic), with the Claude Opus 5.5 model, for copy-

editing to improve the clarity of the text, and for coding assistance to speed up writing

the R code. The authors checked and revised all AI-assisted text and code, and take full

responsibility for the content.



References

Bourdelais, P. & Raulot, J.-Y. (1987), Une peur bleue: Histoire du choléra en France, 1832–1854,

  Payot, Paris.

Breunig, M. M., Kriegel, H.-P., Ng, R. T. & Sander, J. (2000), LOF: Identifying density-based

  local outliers, in ‘Proceedings of the 2000 ACM SIGMOD International Conference on

  Management of Data’, ACM, pp. 93–104.

Coles, S. (2001), An introduction to statistical modeling of extreme values, Vol. 208 of Springer

  Series in Statistics, Springer, London UK.

Cover, T. M. & Thomas, J. A. (2006), Elements of information theory, 2nd edn, Wiley,

  Hoboken, NJ.




                                               35
Davies, L. & Gather, U. (1993), ‘The identification of multiple outliers’, Journal of the

  American Statistical Association 88, 782–792.

Glei, D., Wilmoth, J., Barbieri, M., Vallin, J. & Meslé, F. (2025), ‘About mortality data for

  France, total population’. Accessed 2026-04-29.

  URL: https://mortality.org/File/GetDocument/hmd.v6/FRATNP/Public/InputDB/

  FRATNPcom.pdf

Good, I. J. (1952), ‘Rational decisions’, Journal of the Royal Statistical Society. Series B,

  Statistical methodology 14, 107–114.

Grubbs, F. E. (1950), ‘Sample criteria for testing outlying observations’, Annals of Mathe-

  matical Statistics 21(1), 27–58.

Hampel, F. R., Ronchetti, E. M., Rousseeuw, P. J. & Stahel, W. A. (1986), Robust Statistics:

  The Approach based on Influence Functions, John Wiley & Sons, New York.

Human Mortality Database (2025), ‘University of California, Berkeley (USA); Max Planck

  Institute for Demographic Research (Germany)’. Accessed on 6 October 2025.

  URL: www.mortality.org

Hyndman, R. J. (1996), ‘Computing and graphing highest density regions’, The American

  Statistician 50(2), 120–126.

Hyndman, R. J. (2026), weird: Functions and Data Sets for "That’s Weird: Anomaly Detection

  Using R" by Rob J Hyndman. R package version 3.1.0.

  URL: https://pkg.robjhyndman.com/weird/

Hyndman, R. J., Kandanaarachchi, S. & Turner, K. (2026), When lookout sees crackle:




                                             36
  Anomaly detection via kernel density estimation.

  URL: https://robjhyndman.com/publications/lookout2.html

Kandanaarachchi, S. & Hyndman, R. J. (2022), ‘Leave-one-out kernel density estimates

  for outlier detection’, J Computational & Graphical Statistics 31, 586–599.

Landau, W. M. (2021), ‘The targets R package: a dynamic make-like function-oriented

  pipeline toolkit for reproducibility and high-performance computing’, Journal of Open

  Source Software 6(57), 2959.

Landau, W. M. (2026), targets: Dynamic Function-Oriented ‘Make’-Like Declarative Pipelines.

  R package version 1.12.0.

  URL: https://cran.r-project.org/package=targets

R Core Team (2026), R: A Language and Environment for Statistical Computing, R Foundation

  for Statistical Computing, Vienna, Austria. Version 4.6.1.

  URL: https://www.R-project.org/

Scrucca, L., Fop, M., Murphy, T. B. & Raftery, A. E. (2016), ‘mclust 5: Clustering, classi-

  fication and density estimation using Gaussian finite mixture models’, The R Journal

  8(1), 289–317.

Stone, J. V. (2022), Information theory: a tutorial introduction, Sebtel Press, Sheffield, England.

Tribus, M. (1961), Thermodynamics and thermostatics: An introduction to energy, information

  and states of matter, with engineering applications, D. Van Nostrand, New York, USA.

Wang, E., Cook, D., Hyndman, R. J., O’Hara-Wild, M., Smith, T. & Davis, W. (2026), tsibble:

  Tidy Temporal Data Frames and Tools. R package version 1.2.0.

  URL: https://tsibble.tidyverts.org



                                               37
Wickham, H. (2016), ggplot2: Elegant Graphics for Data Analysis, Springer-Verlag, New

  York, USA.

  URL: https://ggplot2-book.org/

Wickham, H., Averick, M., Bryan, J., Chang, W., McGowan, L. D., François, R., Grolemund,

  G., Hayes, A., Henry, L., Hester, J., Kuhn, M., Pedersen, T. L., Miller, E., Bache, S. M.,

  Müller, K., Ooms, J., Robinson, D., Seidel, D. P., Spinu, V., Takahashi, K., Vaughan,

  D., Wilke, C., Woo, K. & Yutani, H. (2019), ‘Welcome to the tidyverse’, Journal of Open

  Source Software 4(43), 1686.

Wickham, H., Chang, W., Henry, L., Pedersen, T. L., Takahashi, K., Wilke, C., Woo, K.,

  Yutani, H., Dunnington, D., van den Brand, T. & Posit, PBC (2026), ggplot2: Create

  Elegant Data Visualisations Using the Grammar of Graphics. R package version 4.0.3.

  URL: https://cran.r-project.org/package=ggplot2

Wilkinson, L. (2018), ‘Visualizing big data outliers through distributed aggregation’, IEEE

  Transactions on Visualization and Computer Graphics 24(1), 256–266.

Wood, S. N. (2017), Generalized additive models: An introduction with R, CRC press, Boca

  Raton, FL.

Wood, S. N. (2025), Mixed GAM Computation Vehicle with Automatic Smoothness Estimation.

  R package version 1.9-4.

  URL: https://cran.r-project.org/package=mgcv




                                            38
A     Proof of Lemma 2.1

Proof. Define Pn (s) = n−1 ∑in=1 1[Si ≤ s]. Fix an index i with Sei ≥ s⋆ . For any j, consider

the two possibilities. If Sej ≥ s⋆ , strict monotonicity gives

                                                  
                     Sej ≤ Sei   ⇐⇒       h Sej ≤ h Sei            ⇐⇒             S j ≤ Si .


If Sej < s⋆ , then both inequalities hold, because

                                                                
                           Sej < s⋆ ≤ Sei ,   S j ≤ h (s⋆ ) ≤ h Sei = Si .

               h         i           
Consequently, 1 Sej ≤ Sei = 1 S j ≤ Si for every j. Summing over j yields the exact

identity

                                         P
                                         b n (Sei ) = Pn (Si ) .


Therefore, simultaneously for all eligible indices,


                 P
                 b n (Sei ) − G (Si ) = |Pn (Si ) − G (Si )| ≤ sup |Pn (s) − G (s)| .
                                                                   s ∈R
           p
Take ϵ =       log(2/δ)/(2n). From the Dvoretzky-Kiefer-Wolfowitz theorem,
                                                                   (                           )
           n                                            o
                          b n (Sei ) − G (Si ) > ϵ ≤ Pr sup |Pn (s) − G (s)| > ϵ
       Pr ∃i : Sei ≥ s⋆ , P
                                                                       s ∈S

                                                                         2
                                                            ≤ 2e−2nϵ
                                                                                       
                                                                             log(2/δ)
                                                                   −2n          2n
                                                            = 2e

                                                            = 2e− log(2/δ)

                                                            = δ.


Re-arranging terms yields the stated inequality: for all Sei ≥ s⋆ , we have P
                                                                            b n (Sei ) − ϵ ≤

G ( Si ) ≤ P
           b n (Sei ) + ϵ with probability at least 1 − δ.




                                                   39
B      Proof of Theorem 3.1

We first state and prove two lemmas.



B.1      Lemmas

In this section, S denotes a generic random variable satisfying the stated conditions; in

                                e Let X = S − µ, and let X = supp( X ). In this appendix,
Theorem 3.1 it is the surprisal S.

redefine G as the distribution function of X, define Ḡ = 1 − G. Define the sequence bn by

the relation Ḡ (bn ) = 1/n, for all n large enough, and let an = 1/{n · g(bn )} > 0, where

g denotes the density of G. Define Mn = max{S1 − µ, . . . , Sn − µ}. We maintain the

following regularity conditions on X.

Assumption B.1 (Regularity Condition).

    (i) For some t0 < x+ := sup{ x ∈ X : G ( x ) < 1} = ∞, G is absolutely continuous

       on (t0 , x+ ) with a strictly positive and continuously differentiable density g. (ii)

       Ḡ (t) → 0 as t → x+ . (iii) The reciprocal hazard function r (t) = Ḡ (t)/g(t) satisfies

                                                   d
                                             lim      r (t) = ξ ∈ R.
                                             t↑ x+ dt


Define                        
                              
                              exp{−(1 + ξx )−1/ξ },          ξ ̸= 0,   1 + ξx > 0,
                              
                              
                Gξ ( x ) :=                                                           .
                              
                              exp{−e− x },
                              
                                                  ξ=0

Lemma B.1. Let Assumption B.1 be satisfied. If Assumption 3.1 is satisfied then, for every

x ∈ R,
                                           Mn − bn
                                                        
                                  Pr               ≤x        −→ G0 ( x ).
                                             an




                                                    40
If instead Assumption 3.2 is satisfied, then

                                   Mn − bn
                                               
                       Pr                  ≤x       −→ Gξ ( x ),           0 ≤ ξ ≤ 1/q.
                                     an

Proof. The proof proceeds in four steps.

Step 1: Upper tail threshold. For T > max(t0 , 0) and t ≥ T, the fundamental theorem of

calculus gives
                                                                Z t
                          r (t)      r ( T ) − ξT 1
                                −ξ =             +                      {r ′ (u) − ξ } du.
                             t              t      t                T

Given ε > 0, choose T so that |r ′ (u) − ξ | ≤ ε for all u ≥ T. The absolute value of

the integral term is then at most ε(t − T )/t, and the first term tends to zero. Since ε is

arbitrary,
                                                r (t)
                                                      −→ ξ.                                  (6)
                                                   t

As r (t) > 0 and t > 0 for all sufficiently large t, this implies ξ ≥ 0.

Fix x ∈ R such that 1 + ξx > 0; when ξ = 0, this permits every real x. Define


          Jx = [min(0, x ), max(0, x )],         c x = min(1 + ξv) = min(1, 1 + ξx ) > 0.
                                                           v ∈ Jx


By (6),
                               t + r (t)v                    r (t)
                      sup                 − (1 + ξv) ≤ | x |       − ξ −→ 0.
                      v ∈ Jx       t                            t

Consequently, for all sufficiently large t,

                                                              cx
                                      inf {t + r (t)v} ≥         t −→ ∞.                     (7)
                                      v ∈ Jx                  2

Thus the entire interval between t and t + r (t) x eventually lies in (t0 , ∞), and its smallest

point tends to infinity. This permits the use of Assumption B.1(iii) uniformly along that

interval, including when x < 0.



                                                      41
Step 2: Tail ratio. Set

                                        ηt = sup |r ′ (t + r (t)w) − ξ |.
                                              w ∈ Jx

Assumption B.1(iii) and equation (7) imply ηt → 0. For every v ∈ Jx , the fundamental

theorem of calculus gives

                                                       Z v
                              r (t + r (t)v)
                                             = 1+            r ′ (t + r (t)w) dw.
                                   r (t)                 0


All integrals with a negative upper limit are interpreted as oriented integrals. Hence

                                   r (t + r (t)v)
                          sup                     − (1 + ξv) ≤ | x |ηt −→ 0.              (8)
                          v ∈ Jx        r (t)

Since 1 + ξv ≥ c x > 0 on Jx , the ratios on the left are eventually bounded below by c x /2.

Taking reciprocals in (8) is therefore valid uniformly on Jx , yielding

                                                 r (t)        1
                                   sup                    −       −→ 0.                   (9)
                                   v ∈ Jx   r (t + r (t)v) 1 + ξv


On (t0 , ∞), positivity of G and g gives

                                      d                g(t)       1
                                         log G (t) = −       =−       .
                                      dt               G (t)    r (t)

Thus, for any u, v > t0 ,
                                                             Z v
                                                  G (v)          dw
                                            log         =−            .                 (10)
                                                  G (u)       u r (w)

We now evaluate this integral with endpoints t and t + r (t) x. These endpoints and the

interval between them are valid by (7). Substituting u = t + r (t)v and using the uniform




                                                       42
convergence in (9) on the fixed interval Jx gives
                                                  Z t +r ( t ) x
                          G (t + r (t) x )                          du
                      log                  =−
                               G (t)                t              r (u)
                                                  Z x
                                                                 r (t)
                                            =−                             dv
                                                    0       r (t + r (t)v)
                                                    x  dv
                                                        Z
                                            −→ −
                                                  0 1 + ξv
                                              
                                              
                                              −ξ −1 log(1 + ξx ), ξ > 0,
                                              
                                              
                                            =
                                              
                                              − x,
                                              
                                                                  ξ = 0.

In particular, the absolute difference between the two integrals over [0, x ] is bounded by

| x | times the supremum in (9). Exponentiating proves
                                             
                                             
                                             (1 + ξx )−1/ξ , ξ > 0,
                                             
                                             
             G (t + r (t) x )
                              −→ τξ ( x ) :=                                       1 + ξx > 0.   (11)
                  G (t)                      
                                             e− x ,
                                             
                                                             ξ = 0,


Step 3: Convert the tail ratio. The function G is continuous and strictly decreasing on

(t0 , ∞), and tends to zero as t → ∞. It is strictly positive at every finite t, because x+ = ∞.

Therefore G (bn ) = 1/n has a unique solution in (t0 , ∞) for all sufficiently large n, and

bn → ∞. With an = r (bn ), equation (11) gives

                                     G ( bn + r ( bn ) x )
                 nG (bn + an x ) =                         −→ τξ ( x ),         1 + ξx > 0.      (12)
                                           G ( bn )

Write qn = G (bn + an x ). Then qn → 0 and nqn → τξ ( x ), so


                        n log(1 − qn ) = −nqn {1 + o (1)} −→ −τξ ( x ).


Independence now yields

               Mn − bn
                           
      Pr               ≤x       = G (bn + an x )n = (1 − qn )n −→ exp{−τξ ( x )} = Gξ ( x ).
                 an



                                                    43
If ξ = 0, this proves the first part of the result for every x ∈ R. If ξ > 0 and x ≤ −1/ξ,

then for every z > −1/ξ, monotonicity gives

                                              Mn − bn
                                                               
                         0 ≤ lim sup Pr               ≤x            ≤ Gξ (z).
                                n→∞             an

Letting z ↓ −1/ξ makes the right-hand side tend to zero. Thus the result also holds at

and below the lower support boundary.

Step 4: Moment Implications. For every q > 0, Tonelli’s theorem gives the tail-integral

identity
                                               Z ∞
                                     q
                                 E[ X+ ] = q           tq−1 G (t) dt,                        (13)
                                                  0

with equality also when the expectation is infinite, and where X+ = max( X, 0).

Suppose first that ξ > 0. By (6), for any ε ∈ (0, ξ ) there is a T > max(t0 , 0) such that


                           (ξ − ε)t ≤ r (t) ≤ (ξ + ε)t,             t ≥ T.


Taking reciprocals and integrating gives
                                            Z t
                             log(t/T )           du     log(t/T )
                                       ≤              ≤           .
                               ξ+ε            T r (u)     ξ−ε

Using (10), we obtain


              G ( T )(t/T )−1/(ξ −ε) ≤ G (t) ≤ G ( T )(t/T )−1/(ξ +ε) ,         t ≥ T.       (14)


If q < 1/ξ, choose ε > 0 sufficiently small that q < 1/(ξ + ε). The upper bound in (14)

then makes the tail integral in (13) finite. If q > 1/ξ, choose ε > 0 sufficiently small that

q > 1/(ξ − ε). The lower bound makes that integral infinite. The integral over [0, T ] is

always at most T q . Consequently,
                             
                                   q
                             
                             E[ X+  ] < ∞,            0 < q < 1/ξ,
                             
                             
                                                                                             (15)
                                    q
                               
                               E[ X+ ] = ∞,
                               
                                                      q > 1/ξ.

                                                  44
These conclusions impose no restriction on whether the moment of order exactly 1/ξ is

finite.

Suppose next that ξ = 0. Equation (6) gives r (t) = o (t). For any A > 0, choose

T > max(t0 , 0) sufficiently large that r (t) ≤ t/A for t ≥ T. Equation (10) then implies
                                  Z t         
                                            du
              G (t) = G ( T ) exp −              ≤ G ( T )(t/T )− A ,  t ≥ T.
                                       T r (u)

For each q > 0, taking A > q in (13) proves

                           q
                       E[ X+ ] < ∞         for every q > 0   when ξ = 0.               (16)


Under Assumption 3.1,

                                   E[eλX+ ] ≤ 1 + E[eλX ] < ∞.

For every q > 0, the function uq e−λu is bounded on [0, ∞), so every positive-part moment

is finite. Equation (15) therefore excludes ξ > 0. Together with ξ ≥ 0, this gives ξ = 0.

Under Assumption 3.2, if ξ > 0, equation (15) requires q ≤ 1/ξ, or ξ ≤ 1/q. The same

upper bound holds when ξ = 0. If additionally E[ X+
                                                  r ] = ∞ for some r > q, equation (16)


excludes ξ = 0. Equation (15) then requires r ≥ 1/ξ, which gives ξ ≥ 1/r.

Let p∗ := sup{q > 0 : E max( X, 0)q < ∞}. Equation (16) gives p∗ = ∞ when ξ = 0,

whereas (15) gives p∗ = 1/ξ > 0 when ξ > 0, regardless of the finiteness of the boundary

moment. Thus a finite moment index satisfies ξ = 1/p∗ .


Recall, for y ≥ 0,
                                 
                                 
                                 1 − (1 + ξy)−1/ξ ,   ξ ̸= 0,   1 + ξy > 0
                                 
                                 
                     Hξ (y) :=
                                 
                                 1 − e − y ,
                                 
                                                      ξ = 0,

and Hξ (y) = 1 for y ≥ −1/ξ when ξ < 0. Recall that X = S − µ. Theorem 3.1 in the

main text follows from the following Lemma.

                                                45
Lemma B.2. Let Assumption B.1 be satisfied. If Assumption 3.1 is satisfied, then

                                        X − bn
                                                            
                               Pr              > y X > bn        −→ e−y .
                                          an

If Assumption 3.2 is satisfied, then

                        X − bn
                                             
               Pr              > y X > bn         −→ (1 + ξy)−1/ξ ,       (1 + ξy) > 0.
                          an

Proof. We prove a general form of the result and then specialize the result to the assumed

moment conditions.

Recall G (s) = Pr( X ≤ s). From Lemma B.1 and independence, we have that G (bn +

an x )n → Gξ ( x ) for any x such that 1 + ξx > 0. Let Ḡ = 1 − G. However,


                                    n Ḡ (bn + an x ) → − log Gξ ( x ),                        (17)


since log(1 − t) ∼ −t for t ↓ 0 and sufficiently small, and since Ḡ (bn + an x ) = Pr( X >

bn + an x ) → 0 as n → ∞. Let τξ ( x ) := − log Gξ ( x ).

For given u < x+ , but sufficiently close, let m(u) = ⌊1/ Ḡ (u)⌋. The result of Lemma B.1

excludes the case where an atom at a finite upper endpoint exists; hence, as u ↑ x+ ,


                           Ḡ (u) → 0,     m(u) → ∞,        m(u) Ḡ (u) → 1.                   (18)


We now show that,
                                               u − bm ( u ) u → x +
                                     z(u) =                 −−−→ 0.
                                                 am(u)

For any ε > 0, and sufficiently small, (17) implies that


          m(u) Ḡ {bm(u) − am(u) ε} → τξ (−ε);           m(u) Ḡ {bm(u) + am(u) ε} → τξ (ε).


From (18), and monotonicity of Ḡ, we have, for sufficiently large u,


                              bm(u) − am(u) ε < u < bm(u) + am(u) ε,

                                                    46
and so we have that z(u) → 0.

Fix x ≥ 0 with 1 + ξx > 0, and choose ε > 0 small enough so that eventually

                                         x − ε ≤ x + z(u) ≤ x + ε

Now, since am(u) > 0, for u = bm(u) + am(u) z(u), we have

                  bm ( u ) + a m ( u ) ( x − ε ) ≤ u + a m ( u ) x ≤ bm ( u ) + a m ( u ) ( x + ε ) .

However, Ḡ is decreasing so that

 m(u) Ḡ {bm(u) + am(u) ( x + ε)} ≤ m(u) Ḡ {u + am(u) x } ≤ m(u) Ḡ {bm(u) + am(u) ( x − ε)}

From (17), the outer-term in the above equation converge to τξ ( x + ε) and τξ ( x − ε),

respectively. Therefore, since τξ ( x ) is continuous, taking ε → 0 implies that
                                             h                         i
             m(u) Ḡ {u + am(u) x } = m(u) Ḡ bm(u) + am(u) {z(u) + x } → τξ ( x ).

Consequently, for ω (u) = am(u) ,

                 X−u                               m(u) Ḡ {u + am(u) x }
                                        
        Pr             >x|X>u                  =                               → τξ ( x ) = 1 − Hξ ( x ).
                 ω (u)                                  m(u) Ḡ (u)

Given the above convergence, a point-wise version of the stated result now follows by

the results in Lemma B.1.

The above convergence can be extended to uniform convergence directly. Define,

                                                        X−u
                                                                   
                                  Ku (y) = Pr                 ≤y X>u .
                                                        ω (u)

Clearly, the earlier argument implies, for every y ≥ 0, Ku (y) −→ Hξ (y). However, Ku

and Hξ are distribution functions and Hξ is continuous and proper, we have

                                        sup Ku (y) − Hξ (y) −→ 0
                                        y ≥0

as claimed.


                                                         47
