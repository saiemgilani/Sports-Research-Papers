<!-- source: library/preprints/arXiv/2026/2026 - Inference in a generalized Bradley-Terry model for paired comparisons with covariates and a growing number of subjects - Yan.pdf -->
<!-- item: https://arxiv.org/abs/2507.22472 -->
<!-- authors: Ting Yan -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-18; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Inference in a generalized Bradley-Terry model for paired comparisons with covariates and a growing number of subjects

                                                   Inference in a generalized Bradley-Terry model for
                                                   paired comparisons with covariates and a growing
                                                                   number of subjects
arXiv:2507.22472v2 [stat.ME] 13 Nov 2026




                                                                                     Ting Yan∗
                                                                          Central China Normal University



                                                                                            Abstract

                                                        Motivated by the home-field advantage in sports, we propose a generalized
                                                    Bradley–Terry model that incorporates covariate information for paired compar-
                                                    isons. It has an n-dimensional merit parameter β and a p-dimensional regression
                                                    coefficient γ for covariates. When the number of subjects n approaches infinity and
                                                    the number of comparisons between any two subjects is fixed, we show the consis-
                                                    tency of the maximum likelihood estimator (MLE) (β,      b γb ) of (β, γ) in cases that p is
                                                    fixed or diverges with n. Furthermore, when p is fixed, we derive the asymptotic nor-
                                                    mal distribution of the MLE by characterizing its asymptotic representation. The
                                                    asymptotic distribution of γ b is biased, while that of βb is not. This phenomenon can
                                                    be attributed to the different convergence rates of γ  b and β. b The consistency result
                                                    is further extended to an Erdős–Rényi comparison graph. Numerical studies and a
                                                    real data analysis demonstrate our theoretical findings.
                                                    Key words: Asymptotic normality, Bradley-Terry model, Consistency, Covariate,
                                                    Growing number of parameters.

                                                    Mathematics Subject Classification: 60F05, 62J15, 62F12, 62E20.




                                           1        Introduction
                                           When it was difficult for subjects to rank simultaneously based on the judgment of one
                                           person, they were arranged as follows: repeatedly compared to each other in pairs. Paired
                                               ∗
                                               Department of Statistics, Central China Normal University, Wuhan, 430079, China.                Email:
                                           tingyanty@mail.ccnu.edu.cn.


                                                                                                 1
comparison data also arise in situations in which there are natural win-loss results between
two subjects without the presence of a judge. Subjects could be teams, players, beverages,
journals, and products. One of the fundamental problems in paired comparisons is the
production of a ranking for all subjects. Because global rankings are not easily obtained
for non round-robin tournaments, developing a statistical model to estimate rankings
is desirable. The Bradley–Terry model (Bradley and Terry, 1952) is one of the most
popular models for this purpose, dating back to at least 1929 (Zermelo, 1929). This is
occasionally referred to as the Bradley–Terry–Luce model (Luce, 1959). It assigns one
merit parameter βi to each subject and postulates that subject i beats subject j with a
probability eβi −βj /(1 + eβi −βj ), independent of other comparisons. The ranking of all the
subjects is determined by their maximum likelihood estimator (MLE). Since the work of
Bradley and Terry (1952), it has had numerous applications, ranging from rankings of
classical sports teams (Masarotto and Varin, 2012; Sire and Redner, 2008; Whelan and
Wodon, 2020) and scientific journals (Stigler, 1994; Varin et al., 2016) to the quality of
product brands (Radlinski and Joachims, 2007), such as two brands of wine of some type,
for multiclass classification (Hastie and Tibshirani, 1998; Clémençon and Vogel, 2020) and
crowdsourcing (Chen et al., 2016).
    Among many paired comparison models, the Bradley–Terry model is unique, satisfy-
ing the Bradley–Terry–Luce system (Colonius, 1980). Hajek et al. (2014) and Shah et al.
(2016) demonstrated that the MLE in the Bradley–Terry model is minimax-optimal for
estimating the merit parameters in terms of the mean squared error. A detailed investi-
gation of the Bradley–Terry model, including maximum likelihood estimation, hypothesis
testing and goodness-of-fit tests of the model can be found in Section 4 of David (1988).
To facilitate a wide range of applications, some generalized models have been proposed
(e.g. Luce, 1959; Rao and Kupper, 1967; Davidson, 1970; Huang et al., 2006). Algorithms
for solving MLEs in these models have been established (e.g. Ford, 1957; Hunter, 2003;
Vojnovic et al., 2019).
    As highlighted by Agresti (2012) (p. 455), most sports have home-field advantage:
A team is more likely to win when playing in its home city. He introduced a “home-
field advantage” model by assuming the logit of the probability of home i beating away
j is the merit difference βi − βj plus an effect parameter γ, where γ indicates a home-
field advantage if γ > 0. The home team of the two evenly matched teams has the
probability exp(γ)/(1 + exp(γ)) of winning. Except the home-field advantage, there exist
other covariates that have influences on the winning probabilities. For example, the
duration of athletes’ rest periods can influence competition results in sports competitions,
where athletes experiencing highly congested schedules may be particularly exposed to air
travel effects, circadian rhythm disruption, sleep deprivation, decline in physical capacity,
and injury risk (Esteves et al., 2021). Another example is that one can use a gambling


                                             2
company’s odds to predict the outcome of a game (Song et al., 2026), where a team with
low odds has a relatively stronger merit to win another team with large odds. In addition,
when a judge expresses a preference between two items, multiple covariates may affect the
outcome, including intrinsic covariates (e.g., the judge’s professional background, judging
experience, subjective predispositions, attention, and emotional state during assessment)
and extrinsic covariates (e.g., the evaluation environment, time constraints and stimulus
presentation order). We extend the “home-field advantage” model to a general form.
    Let zijk be a deterministic p-dimensional vector denoting covariate information as-
sociated with the kth comparison between subjects i and j. It is suitable to require
zijk = −zjik , because if something is advantageous to i then it is disadvantageous to j.
We incorporate the covariate information into the Bradley–Terry model by specifying the
winning probability of i against j as
                                                                      ⊤
                                                       exp(βi − βj + zijk γ)
                    P(i wins j|zijk , γ, βi , βj ) =                     ⊤
                                                                               ,                 (1)
                                                     1 + exp(βi − βj + zijk γ)

where γ is a p-dimensional regression coefficient of the covariates and βi is the merit pa-
rameter of i. Under the restriction zijk = −zjik , the probability above is well defined. We
call it the covariate-adjusted Bradley–Terry model (abbreviated as “CBTM”) hereafter.
    The covariate zijk can be formalized according to the situations of the teams or the
attributes of the subjects. If xik,j and xjk,i denote p-dimensional attributes of subjects
i and j in the kth comparison of i against j, respectively, they can be used to construct
vector zijk = g(xik,j , xjk,i ) for an asymmetric vector function, where g(xik,j , xjk,i ) =
−g(xjk,i , xik,j ). For instance, if we let g(xik,j , xjk,i ) be equal to xik,j − xjk,i , then we can
measure the dissimilarity between the two subjects. As an example, if the game is played
in the city of team i or subject i is listed first, then we let xik,j = 1 and Xjk,i = 0 (p = 1),
such that zijk = 1 and zjik = −1. In this case, the CBTM reduces to the home-field
advantage model in Agresti (2012).
    In several paired comparison situations, the number of subjects n is typically large,
whereas the number of comparisons mij for any pair (i, j) is relatively small (e.g. Simons
and Yao, 1999). Specifically, all mij are bounded by a fixed constant (e.g., each pair of
teams in the NBA plays at most four games in a regular season). Theoretical analysis of
the Bradley–Terry model with a diverse number of subjects has received wide attention
in recent years. We have elaborated on these after stating our main results. However, the
existing high-dimensional paired comparison literature has little involvement in additional
information (e.g., covariate), but for win-loss outcomes. As shown in Agresti (2012), this
can significantly influence the ranking.
    To determine how covariates influence the estimation of merit parameters in the high
dimension, we drew Figure 1 to evaluate the ℓ∞ -error ∥βb − β∥∞ via a simulation study

                                                 3
here, where βb was fitted using the maximum likelihood estimation in the original BTM
(shorthand of Bradley–Terry model) and the CBTM with the correct model specification
for comparison. The figure on the left shows that the error in the BTM increases rapidly
with γ whereas the error in the CBTM changes only slightly. The former became increas-
ingly larger than the latter for γ. From the right figure, we can see the following: the
error in the BTM is larger than that in the CBTM when n increases and γ is fixed. Even
when n increased to a sufficiently large value, the error in the BTM did not decrease.
This indicates that the CBTM has a significant improvement over the BTM when there
is covariate effect. This partly motivates the present study.
                     3.0




                                                                                      2.0
                                 CBTM                                                            CBTM
                                 BTM                                                             BTM
                     2.5




                                                                                      1.5
                     2.0
     || β − β || ∞




                                                                      || β − β || ∞
                     1.5




                                                                                      1.0
        ^




                                                                         ^
                     1.0




                                                                                      0.5
                     0.5




                           0.0   0.2    0.4     0.6   0.8   1.0                             50   100      150       200   250

                                         γ (n=100)                                                      n (γ=0.5)




Figure 1: The plots of the average values of ∥βb − β∥∞ changing with γ (when n is fixed)
in the left and changing with n (when γ is fixed) in the right. The red color indicates the
error with fitted values in the BTM without covariates while the black color indicates the
error in the CBTM. All βi s were independently generated from the uniform distribution
U (0, 1). Each pair had only one comparison. We set zijk = 1 when i < j and zijk = −1
when i > j. The win-loss outcomes were generated according to the CBTM. The average
value of ∥βb − β∥∞ was recorded out of 100 repetitions.

   The contributions of this study are as follows.

   • When n goes to infinity and all mij (> 0) are fixed, we establish the uniform consis-
     tency of the MLE when the dimension of covariates is fixed or increases with n. A
     key idea for the proof is that we use a two-stage method that first derives an error
     bound for the MLE γ   b of the regression coefficient γ of the covariates and then ob-
     tains the ℓ∞ -error between an estimator βbγ and β for a given γ via the convergence
     rate of a Newton’s iterative sequence. The proof in the first stage is delicate, where
     we derive the lower bound of the difference of the expected log-likelihood function
     between the true parameter and its neighboring point and a uniform lower bound
     of the averaged centered log-likelihood function between the true parameter and its
     its neighboring point, and connect it to the error bound of the true parameter.


                                                                  4
      • We derive the asymptotic normal distribution of the MLE by characterizing its
        asymptotic representation, when the dimension of covariates is fixed. This is proved
        by applying Taylor’s expansions to a series of functions constructed from likelihood
        equations and showing remainder terms in the expansions are asymptotically ne-
        glect. The asymptotic distribution of the MLE γ b contains a bias term while there is
        no bias for β.
                    b We propose a bias-corrected version of γ b for making valid inference.

      • We further extend the consistency result to an Erdős-Rényi random graph with a
        diverging number of pn , where the sampling probability is allowed to be close to the
        Erdős-Rényi lower bound (Erdős and Rényi, 1960). We also extend the results to a
        fixed sparse comparison graph in Yan et al. (2012).

   Simulation studies and a real data analysis are conducted to illustrate the theoretical
results.


1.1       Related work
Studies on the Bradley–Terry model in high-dimensional settings have recently attracted
significant interest. In a pioneering study, Simons and Yao (1999) proved the uniform
consistency and asymptotic normal distribution of the MLE when the number of sub-
jects approaches infinity and each pair has a fixed number of comparisons. To relax the
dense comparison assumption, Yan et al. (2012) extended their results to a fixed sparse
comparison graph by controlling the length from one subject to another subject. Han
et al. (2020) further extended Simons and Yao’s results to an Erdös–Rényi comparison
graph under a weak sparsity condition on qn , where qn is the probability that any two
subjects will be compared. Chen et al. (2019) established the ℓ∞ -error bounds for the
spectral estimator and regularized the MLE, which leads to sample complexity for the
top-K rankings. Chen et al. (2022) further studied the ℓ∞ -error of the MLE and obtained
the minimax rate for top-k ranking. However, covariate information was not considered
in these studies, which is the focus of this study.
    While revising this paper1 , a new related work appears. Fan et al. (2024) extend the
Bradley–Terry model to incorporate the covariate information, where the covariate term
is (Xi − Xj )⊤ γ and Xi denotes the individual-level attribute Xi of subject i. In contrast,
                                     ⊤
the covariate term in model (1) is Zijk γ, which contains the special case (Xi −Xj )⊤ γ. It is
clear that Fan et al. (2024) characterize only the individual level covariate information and
do not address such covariates associated with each paired comparision (e.g., home-field
advantage). In addition, our proof strategy is different from theirs, where Fan et al. (2024)
analyze the consistency of the MLE by using a constrained maximum likelihood technique
  1
      An original version was finished in 2020.


                                                  5
with a projected gradient descent algorithm and derive asymptotic distributions of the
MLE by approximating the MLE via the minimizer of the quadratic approximation of the
likelihood function. In this study, we use a two-stage technique that alternatively obtains
the ℓ∞ -error between an estimator βbγ and β and the ℓ∞ -error between an estimator γ     bβ
and γ, to show the consistency of the MLE and characterize asymptotic representations
to obtain its asymptotic distributions.
    Note that the CBTM can be recast into a logistic regression model. The “large N ,
diverging pN ” framework in generalized linear models (GLMs) has been explored, where
N is the sample size, and pN is the dimension of the parameter space. Portnoy (1988)
showed the asymptotic normality of the MLE in exponential family of distributions on
independent and identically distributed samples when p2N = o(N ). He and Shao (2000)
built the asymptotic normality of M -estimators when p2N log pN = o(N ). Wang (2011)
established the consistency of the generalized estimating equations estimator when p2N =
o(N ) and its asymptotic normality when p3N = o(N ). In our asymptotic framework for
the CBTM, p2N /N → 1/2, not 0, where pN = p + n and N = n(n + 1)/2 if each pair has
only one comparison. Therefore, these asymptotic results are not applicable in this case.
    A relevant work to GLMs is Liang and Du (2012), who study the asymptotic regime
pN = o(N ) in a logistic regression model. Let λmin (SN ) and λmax (SN ) denote the minimum
and maximum eigenvalues of SN , where SN = N                 ⊤
                                                  P
                                                     i=1 xi xi and xi is the pN -dimensional
covariate vector of individual i. Assuming that c1 N ≤ λmin (SN ) ≤ λmax (SN ) ≤ c2 N for
two constants c1 and c2 , they show the asymptotical normality of the MLE by extending
the proof strategy in Yin et al. (2006) for GLMs with fixed dimensions to an increasing
dimension. In CBTM, the first n diagonal entries of SN are of the order of n, because
of the special structure of the design matrix for the merit parameters β, whereas the
last p diagonal entries of SN are on the order of n2 . Because of the different orders of
the diagonal elements of SN , the ratio λmax (SN )/λmin (SN ) is not constant. In a broad
simulation study, we found the following: λmax (SN )/λmin (SN ) is of the order of O(N ),
far from the assumption that λmax (SN )/λmin (SN ) ≤ c2 /c1 , Therefore, the conditions in
Liang and Du (2012) cannot be applied to CBTM. Interestingly, a recent study reported
the following: Zhou et al. (2021) extended Yin et al.’s proof to GLMs with a diverging
number of covariates, which requires, except for the same conditions for SN as in Liang
and Du (2012), the condition p2N /N → 0 to guarantee asymptotic normality rather than
the weaker condition pN /N → 0. In addition, the asymptotic distribution of the MLE in
the aforementioned literature is not biased (e.g. Haberman, 1977; Portnoy, 1988; Wang,
2011; Liang and Du, 2012; Zhou et al., 2021). In sharp contrast to these studies, the
asymptotic distribution of MLE γ    b has a bias term, whereas that of the MLE βb does
not. This phenomenon is referred to as the incidental parameter problem in econometric
literature (e.g., Graham, 2017) which is caused by different convergence rates of γ b and β.
                                                                                          b


                                             6
    In the network setting, the degree heterogeneity and the homophily have been modelled
in a similar logistic regression form (e.g. Graham, 2017; Yan et al., 2019). However, their
focus are network features, which is different. In addition, the case with the increasing
dimension of covariates is not studied in their works. Model (1) can also be represented
as a log-linear model. Although the conditions for the existence of an MLE have been
established (Fienberg and Rinaldo, 2012), asymptotic theories remain lacking in high-
dimensional cases (e.g. Fienberg and Rinaldo, 2007, 2012).
    The remainder of this paper is organized as follows. In Section 2, we present the
maximum likelihood estimation. In Section 3, we present the consistency and asymptotic
normality of the MLE. In Section 4.1, we extend the consistency result to an Erdős–
Rényi comparison graph with a diverging number of covariates. In Section 5, we perform a
simulation and provide a real data analysis. We provide a summary and further discussion
in section 6. All proofs are presented on the supplementary material.


2    Maximum likelihood estimation
Consider a set of n + 1 subjects labelled by “0, . . . , n”. Let mij be the number of
comparisons between i and j and Aijk be the random outcome in the kth comparison,
k = 1, . . . , mij , where Aijk (∈ {0, 1}) is an indictor variable denoting whether i beats j
in the kth comparison. The lowercase letter aijk denotes its realized value. That is, if i
wins j, then aijk = 1; otherwise, aijk = 0. The win-loss results are recorded in a matrix:
A = (Aij )n×n , where Aij is the number of times that i beats j and the diagonal elements
                                                         P
Aii are set to zero by default, i.e., Aii = 0. Let di = j̸=i Aij be the total number of wins
for subject i and β = (β1 , . . . , βn )⊤ . We make the following assumptions.

Assumption 1. All mij are uniformly bounded above by a fixed positive constant m∗ .

Assumption 2. All the comparison outcomes Aijk over 0 ≤ i < j ≤ n, j = 1, . . . , mij ,
are mutually independent.

    When the number of subjects is large, Assumption 1 usually holds. For instance, two
teams play a maximum of four times in the NBA regular season. Assumption 2 requires
the independence of paired comparisons, which is widely used in literature (e.g. Simons
and Yao, 1999; Han et al., 2020; Fan et al., 2024).
    Because adding the same constant to all βi results in the invariance of probability (1),
we set β0 = 0 for model identification, as in Simons and Yao (1999). Other restrictions are
                       P
possible; for example, i βi = 0. Except for this restriction, some condition is needed
                                                                                  P
for the covariate matrix Z for guaranteeing the model identifiability. Let N = i<j mij
be the total number of comparisons and ei ∈ Rn denote the ith standard basis vector


                                             7
with its ith element being 1 and all other elements 0. Let x⊤      ⊤               ⊤       ⊤
                                                            ij = (xij,1 , . . . , xij,mij ) and


                   X = (x⊤             ⊤     ⊤             ⊤             ⊤      ⊤
                         01 , . . . , x0n , x12 , . . . , x1n , . . . , xn−1,n ) ∈ R
                                                                                    N ×n
                                                                                         ,    (2)

where x0j,k = −ej for j = 1, . . . , n and k = 1, . . . , m0j , and xkj,t = ek − ej for 1 ≤
k ≤ n − 1, j = k + 1, . . . , n and t = 1, . . . , mkj . It is clear that X is the design matrix
for the parameter vector (β1 , . . . , βn ). Recall that zij,k ∈ Rp denotes the p-dimensional
covariate vector associated with k-th comparison when subject i is compared with subject
j. Correspondingly, define z⊤          ⊤              ⊤       ⊤
                               ij = (zij,1 , . . . , zij,mij ) and


                    Z = (z⊤             ⊤     ⊤             ⊤             ⊤      ⊤
                          01 , . . . , z0n , z12 , . . . , z1n , . . . , zn−1,n ) ∈ R
                                                                                     N ×p
                                                                                          .   (3)

That is, Z is the design matrix for the p-dimensional regression parameter γ. Let (X, Z)
be the merged matrix of X and Z by column. The following proposition gives the iden-
tifiability of model, whose proof is in the supplementary material.

Proposition 1. If rank(X, Z) = n + p, then the covariate-adjusted Bradley–Terry model
is identical, subject to the restriction β0 = 0.

    We now provide some intuitive explanations on the condition rank(X, Z) = n+p. The
matrix X(X ⊤ X)−1 X ⊤ ∈ RN ×N is the projection matrix that project a vector onto the
linear subspace C(X ⊤ ) spanned by the column vectors of X ⊤ . Let IN denote the N × N
identity matrix. Then, we have

                     Z = X(X ⊤ X)−1 X ⊤ Z + (IN − X(X ⊤ X)−1 X ⊤ )Z,                          (4)

where the first term of the above right hand side represents the projection of Z ∈ RN ×p
onto the linear subspace C(X ⊤ ) and the second term is the residual vector. By the fact
(IN − X(X ⊤ X)−1 X ⊤ )X = 0, we have

                         Z ⊤ PX h = Z ⊤ PX (Xβ + Zγ) = (Z ⊤ PX Z)γ,                           (5)

where PX = IN −X(X ⊤ X)−1 X ⊤ and h is defined in (??) denoting the win-loss probability
vector. If rank(PX Z) < p, then the regression coefficient γ of the covariate is not identical.
A simple example is that zijk = xi − xj for all i, j, k, where xi denotes the attribute vector
of subject i. In this case, rank(PX Z) = 0. On the other hand, if rank(PX Z) = p, by (5),
then
                                 γ = (Z ⊤ PX Z)−1 Z ⊤ PX h.

That is, γ is identifiable. On the other hand, since rank(X ⊤ X) = n, if rank(PX Z) = p,
then all the parameters are identical.

                                                      8
   Under Assumption 2, the log-likelihood function in model (1), is
                                        m
                                        Pij                                        βi −βj +zijk γ    ⊤
                                              {Aijk (βi − βj + z⊤
                                P
     ℓ(β, γ) =                                                  ijk γ) − log(1 + e                )}
                        0≤i<j≤n k=1

                                                      Aijk (z⊤                        log(1 + exp(βi − βj + z⊤
                        P                     PP                              PP
                  =             βi Di +                      ijk γ) −                                        ijk γ)).
                            i                 i<j k                           i<j k


Write µijk (β, γ) as the expectation of aijk , where µijk (β, γ) is equal to the probability of
i winning j in the kth comparison given in (1). The maximum likelihood equation is as
follows:                                          m
                                           P n    Pij
                                   di =               µijk (β, γ), i = 1, . . . , n,
                                         j=0,j̸=i k=1
                   P m  Pij                 P m    Pij                                      (6)
                            Aijk zijk =                zijk µijk (β, γ).
                   0≤i<j≤n k=1                                0≤i<j≤n k=1

It should be noted that the above equations do not contain d0 . This is because ni=0 di =
                                                                               P
P
   i<j mij , The MLE of the parameter (β, γ), denoted as (β, γ
                                                            b b ), is the solution to the
above equations, where β̂0 = 0.
    Let K be the convex hull of set
                            XX
      {(d1 , . . . , dn ,               z⊤         ⊤
                                         ijk Aijk ) : Aijk ∈ {0, 1}, 0 ≤ i < j ≤ n, k = 1, . . . , mij }.
                            i<j     k


If rank(X, Z) = n + p, then, according to Theorem 1.13 in Brown (1986) (p. 19), the
normalizing function i<j k log(1 + exp(βi − βj + z⊤
                        P P
                                                         ijk γ)) is strictly convex. As this
normalizing function is steep and strictly convex, by the properties of exponential family
of distributions [e.g., Theorem 5.5 in Brown (1986) (p. 148)], we have the following result.

Proposition 2. If rank(X, Z) = n + p, the MLE (β,
                                               b γb ) exists if and only if
                                                                    XX
                                               (d1 , . . . , dn ,              z⊤
                                                                                ijk Aijk )
                                                                                          ⊤

                                                                    i<j   k


lies in the interior of K. Further, if the MLE exists, it is unique.

    If the vector (d1 , . . . , dn ) contains zero elements (corresponding to subjects without
wins), or values being equal to the total number of comparisons of some subjects (cor-
responding to subjects without losses), the MLE did not exist. If we do not consider
covariate information, then the condition in Proposition 2 can be explained in terms of
graph language. The win-loss matrix A can be represented in a directed graph Gn with
nodes denoting subjects and directed edges denote the number of wins for one subject
against another. The necessary and sufficient condition for the existence of βb is that the
directed graph Gn is strongly connected. That is, for every partition of subjects into two


                                                                      9
nonempty sets, a subject in the second set beats the subject in the first set at least once
[Ford (1957)].
    Note that there is a restriction on regression coefficient in semiparametric paired com-
parison models of Song et al. (2026). Song et al. (2026) treat the covariates as random
vectors while they are determined in this manuscript. Song et al. (2026) employ a special
regressor method to obtain explicit expressions for all unknown parameters, where one
element of the covariate vector is specially chosen to transform the original paired com-
parison data into the working data. Roughly speaking, the regression coefficient of that
special regressor is not needed to estimate in their method, which is different from the
maximum likelihood estimation here.
    We discuss computational issues. For moderate n, we can simply use the package
“glm” in the R language to solve the MLE, which implements an iteratively reweighted
least squares algorithm. The computational complexity of an iteratively reweighted least
squares algorithm is O(K(N (n + pn )2 + (n + pn )3 )), where K is the number of iterations
until the convergence condition is met. The memory requirements for this algorithm are
dominated by the storage of the N × (n + pn ) design matrix of the parameter vector
(β, γ), Its storage complexity is O(N pn ) because each row of the N × n design matrix of
the parameter vector β have only at most two nonzero elements. Its storage complexity
is O(N pn ) because each row of the N × n design matrix of the parameter vector β have
only at most two nonzero elements. Assuming that each pair is compared only once and
pn = 2, the memories for the design matrix take 4M b, 12.5M b, 49.5M b when n = 100,
500, 1000, respectively. When n = 200, the memories for the design matrix take 4M b,
12.5M b, 49.5M b when pn = 30, 50, 100, respectively. In this case, the corresponding
running times are 2.89, 3.35, 4.76 seconds in a computer with CPU Intel i9-10900 2.8GHz
and 64GB RAM when applying the “glm” package to solve the MLE on a data set. For
relatively large n, it might not have large enough memory to store the design matrix for
β required by the “glm.” In this case, we recommend using a two-step iterative algorithm
by alternating between solving the first equation in (6) using the fixed-point method in
Ford (1957) and solving the second equation in (6) using the Newton-Raphson method.
In the first stage, the iteration is
                                                    ⊤ γ     (k)
                 (k+1)
                                    X X mijk e−βj +zijk
                βi     = log di −                     (k)     (k) ⊤ γ
                                                                        , i = 1, . . . , n.
                                                     βi     −βj +zijk
                                    j̸=i   k   1+e

Its computational complexity is O(n2 pn ) in each iteration. Recall that we define the
function                        mij                         mij
                          X X                          X X
               Qβ (γ) =             zijk µijk (β, γ) −          aijk zijk .
                          0≤i<j≤n k=1                             0≤i<j≤n k=1




                                                10
The Newton-Raphson iteration is

                              γ (k+1) = γ (k) − [Qβ (γ)]−1 Qβ (γ).

Its computational complexity is O(p3n N ) in each iteration. The total computational com-
plexity is O(K(n2 pn + p3n N )), where K is the number of iterations.


3     Theoretical properties
In this section, we present the consistency and asymptotic normality of the MLE. First,
we introduce certain notation. For a subset C ⊂ Rn , let C 0 and C denote the interior
and closure of C, respectively. For a vector x = (x1 , . . . , xn )⊤ ∈ Rn , we denote ∥x∥∞ =
                          P
max1≤i≤n |xi | and ∥x∥1 = i |xi | by the ℓ∞ - and ℓ1 -norms of x, respectively. Let B(x, ϵ) =
{y : ∥x − y∥∞ ≤ ϵ} be the ϵ-neighborhood of x. For an n × n matrix J = (Jij ), let ∥J∥∞
denote the matrix norm induced by the ℓ∞ -norm on the vectors in Rn ; that is,
                                                              n
                                               ∥Jx∥∞         X
                            ∥J∥∞ = max               = max       |Jij |,
                                          x̸=0 ∥x∥∞    1≤i≤n
                                                             j=1


where ∥J∥ denotes a general matrix norm. Define the maximum absolute entry-wise
norm: ∥J∥max = maxi,j |Jij |. We use the superscript “*” to denote the true parameter
under which the data are generated. When there is no ambiguity, we omit the superscript
“*”. The notation i<j is a shorthand for ni=0 nj=i+1 . Define
                  P                       P P


                       ex
            µ(x) :=       x
                            , πijk := βi − βj + z⊤       ∗       ∗    ∗    ⊤    ∗
                                                 ijk γ, πijk := βi − βj + zijk γ .           (7)
                      1+e
                ∗
Note that µ(πijk   ) as the expectation of aijk . We will use the notations µ(πijk ) and
µijk (β, γ) interchangeably. c, c0 , c1 , C, C0 , C1 , . . ., refer to universal constants, whose
specific values may vary from place to place. When p diverges with n, we write pn .
    Let θ = (β ⊤ , γ ⊤ )⊤ and

                         Θ = {θ : ∥β − β ∗ ∥∞ ≤ 1, ∥γ − γ ∗ ∥∞ ≤ 1}.

When emphasizing πijk on its arguments, we write πijk (θ). We make the following as-
sumption on parameters.

Assumption 3. We assume that there exist two numbers κn and bn that may diverge
with n such that
                          sup ∥zijk ∥∞ ≤ κn ≤ log n,                        (8)
                                  i,j,k



                                                  11
and
                                            (1 + eπijk (θ) )2
                                  sup max                     ≤ bn .                         (9)
                                  θ∈Θ i,j,k    eπijk (θ)
   It is clear that bn ≥ 4 and

                                              eπijk (θ)
                                 inf min                     ≥ 1/bn .
                                 θ∈Θ i,j,k (1 + eπijk (θ) )2


When all covariates zijk are bounded by a constant, (8) automatically holds. This condi-
tion is presented in Graham (2017), Dzemski (2019) and Yan et al. (2019). Further, we
make the following assumption on covariates.

Assumption 4. Let Z̃ = (IN −X(X ⊤ X)−1 X ⊤ )Z. We assume that there exists a positive
fixed constant c0 such that Therefore,
                                                        !
                                              Z̃ ⊤ Z̃
                                    λmin                    ≥ c0 > 0.
                                                N

    In the above assumption, Z̃ could be viewed as the residual vector after projecting
Z into the column space C(X ⊤ ) as mentioned before, where X ∈ RN ×p is the design
matrix for the β parameter. Recall that Z = X(X ⊤ X)−1 X ⊤ Z + Z̃ in (4), where the
first and second terms are orthogonal. An intuitive explanation for Assumption 4 is that
the amount of information of the covariate matrix Z projected into C(X ⊤ )+ is linearly
proportional to the total amount of information, where C(X ⊤ )+ denotes the orthogonal
complementary space of C(X ⊤ )+ . A sufficient condition to guarantee Assumption 4 is
that zijt ’s are independently generated from a p-dimensional non-degenerated multivariate
symmetric distribution, whose proof is omitted. In practice, since Z̃ is observed, the
eigenvalues of Z̃ ⊤ Z̃ can be computed to judge whether Assumption 4 holds.
    To explore the asymptotic properties of the MLE, we introduce a system of score
functions based on the maximum likelihood equations:

                                    P         P
                  Hi (β, γ) =          j̸=i    k µijk (β, γ) − di ,     i = 0, . . . , n,
                                                                                            (10)
                   H(β, γ) = (H1 (β, γ), . . . , Hn (β, γ))⊤ .

Furthermore, we define Hγ,i (β) as the value of Hi (β, γ) for an arbitrarily fixed γ, and

                            Hγ (β) = (Hγ,1 (β), . . . , Hγ,n (β))⊤ .

Let βbγ be the solution to Hγ (β) = 0. Correspondingly, we define two additional score



                                                   12
functions:
                              X         X
                Q(β, γ) =                   zijk {µijk (β, γ) − aijk },                   (11)
                                  i<j   k
                              X         X
                  Qc (γ) =                  zijk {µ(βbγ,i − βbγ,j + z⊤
                                                                     ijk γ) − Aijk }.     (12)
                                  i<j   k


Qc (γ) can be viewed as a concentrated or profiled function of Q(β, γ), where the merit
parameter β was profiled. Clearly, if (β,
                                       b γb ) exist, then

             H(β,
               b γb ) = 0, H(βbγ , γ) = Hγ (βbγ ) = 0, Q(β,
                                                         b γb ) = 0, Qc (b
                                                                         γ ) = 0.


3.1    Consistency
Note that model (1) contains two sets of parameters: a merit vector parameter β with a
growing dimension, and regression coefficient γ of covariates with fixed dimensions. In the
absence of covariates, Simons and Yao (1999) proved the consistency of the MLE through
two key steps that first bound the probability that the strong connection condition in the
win-loss comparison graphs failed. Then, we find a set of common neighborhoods with
ratios close to the maximum ratio ûi0 /ui0 and the minimum ratio ûi1 /ui1 , where ûi = eβ̂i
and ui = eβi , i0 = arg maxi ûi /ui and i1 = arg mini ûi /ui . The first step establishes the
existence of an MLE with a high probability. In the presence of covariates, it is difficult to
verify the existence of the MLE. In addition, it is unclear how to find such neighborhoods
because the appearance of covariates will make some key inequalities in Simons and Yao
(1999) be difficult to generalize.
    We use a two-stage process to show consistency.           In the first stage, we establish
the existence of the MLE and obtain an error bound of γ          b . Its proofs proceed three
novel inequalities, including a lower bound of the difference in the expected log-likelihood
function Eℓ(θ) between θ and its true value θ ∗ , a uniform bound of the difference in
the centered log-likelihood function ℓ(θ) − Eℓ(θ) between θ and its true value θ ∗ , and
a relationship inequality that connects the lower bound of Eℓ(θ ∗ ) − Eℓ(θ) to the error
bounds of the MLE. In this stage, we only obtain a rough inequality for β.      b The second
stage is to improve this error bound. We use the convergence rate of the Newton iterative
algorithm to solve the equation F (x) = 0 for obtaining a much lower bound. Under the
well-known Newton-Kantorovich conditions [Kantorovich (1948)], the algorithm converges
and exhibits a high geometric convergence rate. As a result, a solution to the equation
exists, and an ℓp -error between the initial and limiting points is obtained.
    We now formally state the consistency. The proof of Theorem 1 is in the supplementary
material.
                                                                   1/2
Theorem 1. Suppose that Assumptions 1-4 hold. If b7n κn pn = o(n1/2 /(log n)1/2 ), then,

                                                13
with a probability of at least 1 − O(n−1 ), the MLE (β,
                                                     b γb ) exists, and satisfies
                                       r              !                          r              !
                 ∗                         pn log n                ∗                 pn log n
         ∥βb − β ∥∞ = O       b4n κn                      ,   ∥b
                                                               γ − γ ∥2 = O bn                      .       (13)
                                               n                                         n

Further, if the MLE exists, it is unique.
   We compared our ℓ∞ -error bound with Simons and Yao (1999) in the case of no
covariates. They show that ∥βb − β∥∞ = Op ((log n/n)1/2 ) when ∥β ∗ ∥∞ is bounded by
a constant, our result is consistent with their error bound in Simons and Yao (1999),
up to some constant factor. The error bound for γ      b is much slower than the optimal
convergence rate N −1/2 in classical large-sample theory, where N = n(n + 1)/2. The
asymptotic distribution result in Theorem 2 shows that the convergence rate of γ      b is in
the order of Op (1/n), achieving the optimal rate.
   We apply the consistency result to the top-K recovery problem, which identifies a set
of K subjects with the highest ranks. This problem has received considerable attention
in machine learning research; see Chen et al. (2019) and references therein. We assume
that there is a ground-truth order β0∗ > β1∗ > · · · > βn∗ . The aim is to find subjects with
K largest estimates in accordance with their true orders. It suffices to demonstrate that

                        βbi − βbj > 0, i = 0, . . . , K − 1; j = K, . . . , n.

                                                                ∗      ∗
As in Chen et al. (2019), we require a separation measure ∆K = βK−1 − βK to distinguish
between the (K − 1)th and Kth subjects. From the triangle inequality, we obtain:
                                                                                   r              !
                                                                                       pn log n
        βbi − βbj ≥ βi∗ − βj∗ − |βbi − βi∗ | − |βbj − βj∗ | ≥ ∆K − Op     b4n κn                        .
                                                                                           n

Therefore, we have the following corollary:
Corollary 1. Under the conditions in Theorem 1, if ∆K ≫ b4n κn (pn log n)1/2 /n1/2 , with a
probability of at least 1 − O(n−1 ), the set of top-K-ranked subjects can be recovered exactly
by using MLE.


3.2    Asymptotic normality of γ
                               b
Let ℓc (γ) be the concentrated log-likelihood function of ℓ(β, γ) by replacing β with βbγ .
It is easy to verify that the Hessian matrix of −ℓc (γ) (i.e., the Jacobian matrix Q′c (γ)) is
Σ(β,b γ), where

                                                    −1
                          ∂Q(β, γ) ∂Q(β, γ) ∂H(β, γ)     ∂H(β, γ)
               Σ(β, γ) :=      ⊤
                                  −     ⊤        ⊤
                                                                  .                                         (14)
                            ∂γ       ∂β       ∂β           ∂γ ⊤

                                                      14
Note that Q′c (γ) is the Fisher information on γ, which measures the amount of information
on γ provided by win-loss outcomes. Therefore, the asymptotic distribution of γ      b depends
               ′
crucially on Qc (γ).
    Note that (14) involves with the inverse of ∂H(β, γ)/∂β ⊤ , which is denoted as Hγ′ (β)
for convenience. In general, the inverse of Hγ′ (β) does not have a closed form. We use
a simple matrix to approximate it. The Jacobian matrix Hγ′ (β) has a special structure
that can be characterized in the form of a matrix class. Given b0 , b1 > 0, we say that
an n × n-matrix V = (vij )ni,j=1 belongs to the matrix class Ln (b0 , b1 ) if V is a diagonally
dominant matrix with negative nondiagonal elements bounded by b0 and b1 ; that is,

                                       Pn
                          b0 ≤ vii +     j=1,j̸=i vij ≤ b1 ,      i = 1, . . . , n,
                          b0 ≤ −vij ≤ b1 , i, j = 1, . . . , n; i ̸= j.

Define v0n = vn0 = nj=1,j̸=i vij −vii for i = 1, . . . , n and v00 = − ni=1 vin . Simons and Yao
                  P                                                   P

(1998) proposed to approximate the inverse of V , V −1 , by a simple matrix S = (sij )n×n ,
where
                                              δij        1
                                        sij =      +        .                                (15)
                                              vii v00
In the above equation, δij = 1 if i = j; otherwise, δij = 0. It is clear that Hγ′ (β) belongs
to this matrix class. Hereafter, we denote V = (vij ) by Hγ′ ∗ (β ∗ ).
                P
    Recall N = i<j mij . Let

                                                1
                                     Σ̄ := lim    Σ(β ∗ , γ ∗ ),
                                            n→∞ N


where Σ(β, γ) is defined in (14). We assume that the limit Σ̄ exists, which was considered
in Graham (2017). By using S in (15) to approximate V −1 , we have

            1                 1 XX                             1 X Z̄i Z̄i⊤
              Σ(β ∗ , γ ∗ ) =         zijk z⊤
                                            ijk µ ′
                                                    (π ∗
                                                       ijk ) −              + o(1),         (16)
            N                 N i<j k                          N i   vii

where                                       XX
                                    z̄i =              zijk µ′ (πijk
                                                                 ∗
                                                                     ).
                                            j̸=i   k

If zijk is independently draw from some multivariate distribution, then N −1 Σ(β ∗ , γ ∗ )
converges in probability to some non-random matrix.
    The idea of establishing the asymptotic normality of γ    b is briefly described as follows:
First, we use the mean-value expansion to derive the explicit expression of γ     b − γ ∗ , which
contains term Qc (γ ∗ ) multiplied by Σ̄−1 . Then, we apply a third-order Taylor expansion
to Qc (γ ∗ ) to characterize its limiting distribution. In the expansion, the first-order term


                                                   15
is asymptotically normal; the second-order term is the asymptotic bias term and the first-
order term is the remainder term. The asymptotic normality of γ b is described as follows,
whose proof is in the supplementary material.

Theorem 2. Suppose that the conditions in Theorem 1 hold and the dimension p is
fixed. If b12 κ4 = o(n1/2 /(log n)3/2 ), then for a nonzero constant vector c = (c1 , . . . , cp )⊤ ,
√ ⊤ n n
        γ − γ) converges in distribution to normal distribution with mean Σ̄−1 B∗ and
   N c (b
variance c⊤ Σ̄c,
                                              n P
                                         1 X j̸=i k zijk µ′′ (πijk    ∗
                                                        P
                                                                         )
                          B∗ = lim √               P P ′ ∗                 .                   (17)
                                n→∞ 2 N
                                             i=0     j̸ = i k µ (π ijk )

Remark 1. If λmin (Σ(β ∗ , γ ∗ )) ≥ c0 n2 , then γ   b has a convergence rate O(n−1 ). The
asymptotic distribution of γ b contains a bias term B∗ . This is because of the different con-
vergence rates of γ        b which roughly are Op (1/n) and Op (1/n1/2 ). This phenomenon
                    b and β,
is referred to as the incidental parameter problem; see econometric literature Graham
(2017) and the references therein. The bias term is bounded above by bn κn . This is due
to that µ′ (πijk
             ∗
                 ) ≥ 1/bn and |µ′′ (πijk
                                     ∗
                                         )| ≤ 1/4. If B∗ ̸= 0, then we can use the empirically
analytical bias-correction formula as in Dzemski (2019): γ       bbc = γ          b −1 (β,
                                                                       b − N −1/2 Σ     b γb )B̂,
                                                                             ∗       ∗
where B b and Σ b are the estimates of B∗ and Σ̄ obtained by replacing β and γ in their
expressions with the estimators βb and γ     b.


3.3     Asymptotic normality of βb
The idea of establishing an asymptotic distribution βb is briefly described as follows.
A second-order Taylor expansion is applied to Hγ (β)    b at β to derive the following ex-
plicit asymptotic expression for β.  b In the expansion, the first-order term is the sum of
[Hγ′ (β)]
      b −1 (βb − β) and Vγβ (b γ − γ), where Vγβ = ∂H(β, γ)/∂γ ⊤ . Because [Hγ′ (β)]−1 does
not have a closed form, we use S defined in (15) to approximate it. As discussed in
Remark 1, λmin (Σ(β ∗ , γ ∗ )) ≥ c0 n2 guarantees that γ
                                                       b has a convergence rate of Op (1/n).
This makes that the term Vγβ (b   γ − γ) is an asymptotically neglected remainder term. The
second-order term in the expansion is also asymptotically neglected. Then, we represent
βb − β as the sum of S(d − Ed) and remaining terms, where d = (d1 , . . . , dn )⊤ . Therefore,
the central limit theorem is proven by establishing the asymptotic normality of S(d − Ed)
and indicating that the remaining terms are negligible. We formally state the central
limit theorem below, whose proof is in the supplementary material.

Theorem 3. Suppose that the conditions in Theorem 1 hold, λmin (Σ(β ∗ , γ ∗ )) ≥ c0 n2
and the dimension p is fixed. If b12              4
                                               n κn = o(n
                                                         1/2
                                                             / log n), then, for a fixed k the vectors
((βb1 − β1∗ ), . . . , (βbk − βk∗ )) follows a k-dimensional multivariate normal distribution with a
covariance matrix given by the upper left k × k block of S defined in (15).

                                                 16
Remark 2. The asymptotic variance of βbi is 1/vii + 1/v00 , which is in the magnitudes of
O(n1/2 ). In case of no covariates, it is consistent with that in Simons and Yao (1999).


4     Extensions
4.1    Extension to an Erdős–Rényi comparison graph
All the preceding results concern dense comparisons, where each pair has at least one
comparison. We extended these to an Erdős–Rényi comparison graph G(n, qn ), where any
two subjects are compared with probability qn . If qn → 0, this implies a sparse comparison
design. We assume that if two subjects are compared, they are compared at most m∗
times with m∗ fixed, according to the aforementioned settings. In addition, we consider
the case of an increasing dimension of covariates, i.e., pn → ∞. The consistency result is
stated below, whose proof is in the supplementary material.

Theorem 4. Assume that ∥β ∗ ∥∞ and ∥γ ∗ ∥2 are bounded by a positive constant, κ =
supi,j,k ∥zijk ∥2 ≤ C for some constant C, and qn ≥ c log n/n for a sufficiently large con-
stant c. Under Assumptions 1, 2 and 4, if pn /qn = o(n/ log n) then, with a probability of
at least 1 − O(n−1 ), the MLE (β,b γ
                                   b ) exists and satisfies
                                 s           !                       s              !
                                     log n                               pn log n
              ∥βb − β ∗ ∥∞ = O                      γ − γ ∗ ∥2 = O
                                                 , ∥b                                   .
                                      nqn                                  nqn

    When sampling probability qn is less than log n/n, the realized comparison graph is
disconnected with a positive probability according to the theory of the Erdős–Rényi graph.
In this case, all subjects can be divided into two groups such that any subject in the first
group does not have comparisons with any subject in the second group, where it is not
possible to give a ranking of all subjects. Therefore, qn should be not smaller than log n/n,
up to a constant factor, which is a fundamental requirement to guarantee the connection
of the sampling graph. Condition pn /qn = o(n/ log n) restricts the increasing rate of pn .
When qn is a constant, it is weaker than that in Wang (2011), where p2n = o(n/ log n).


4.2    Extensions to a fixed sparse comparison graph with a dy-
       namic range of merit parameters
We extend them to a fixed sparse comparison graph in Yan et al. (2012) here. In some
applications such as sports, the comparison graph may be fixed, not be random. For
example, in the regular season of the National Football League (NFL), which teams
having games are scheduled in advance. More specially, there are 32 teams in the two


                                                  17
conferences of the NFL and are divided into eight divisions each consisting of four teams.
In the regular season, each team plays 16 matches, 6 within the division and 10 between the
divisions. Motivated by the design of the regular season of the National Football League,
they proposed a sparse condition to control the length from one subject to another subject
with 2 or 3 as in Yan et al. (2012):

                                               #{k : mik > 0, mjk > 0}
                                 τn := min                             .                                           (18)
                                       0≤i<j≤n            n

That is, τn is the minimum ratio of the total number of paths between any i and j with
length 2 or 3.
    We assume that if two subjects have comparisons, they are compared at most m∗ times
with m∗ fixed, in accordance with the aforementioned setting. The same proof technique
can be readily extended to the setting here. The main different places are the error bound
of using S to approximate V −1 , ∥V −1 − S∥max , and the number of comparisons of subject
i, mi , that will be replaced with b3n /(n2 τn3 ) and nτn in the sparse case. Here, V = Hγ′ ∗ (β ∗ ).
In this section, I redefine bn in Assumption 3 as
                                             ∗
                                   (1 + eπijk )2                ∗   ∗        ∗
                       bn := max       π ∗       == O(emaxi,j (βi −βj )+z∗ ∥γ ∥1 ),                                (19)
                             i,j,k    e ijk

where z∗ = maxi,j,k ∥Zijk ∥∞ . That says mini,j,k µ′ (πijk
                                                       ∗
                                                           ) ≥ 1/bn . It is easy to see bn ≥ 4.
  Let λmin (β) be the smallest eigenvalue of n Σ(β, γ ∗ ) and define
                                                 −2

                                                                  √
                                                                     2
                                        ρn :=        sup                 .                                         (20)
                                                 β∈B(β ∗ ,ϵn1 ) λmin (β)


Let ∥A∥2 be the ℓ2 -norm of a matrix A induced by Euclidean norm on vectors. By the
inequality of matrix norm, as in Golub and Van Loan (1996) (p. 56–57), we have
                                                                      √                           ρn
                   sup          ∥Σ−1 (β, γ ∗ )∥∞ ≤         sup            2∥Σ−1 (β, γ ∗ )∥2 ≤        .             (21)
               β∈Σ(β ∗ ,ϵn1 )                        β∈Σ(β ∗ ,ϵn1 )                               n2

Note that the dimension of the matrix Σ(β, γ) is fixed and every its entry is a sum of
n(n − 1)/2 terms. There it is suitable to have a factor n−2 in the above inequality. We
have the following theorem.
Theorem 5. Suppose that maxi,j,k ∥zijk ∥∞ ≤ c for a fixed constant c > 0. (1) If ρn b9n /τn9 =
o((n/ log n)1/2 ), then with probability at least 1 − O(n−1 ), the MLE (β,b γ
                                                                            b ) exists and
satisfies
                                                                                          r           !
                          ρn b9n log n                                              b3n
                                       
                                                                                              log n
  γ − γ ∗ ∥∞ = Op
 ∥b                                    ) = op (1), ∥βb − β ∗ ∥∞ = Op                                      = op (1). (22)
                              nτn9                                                  τn3         n

                                                       18
(2) If ρn b9n /τn9 = o(n1/2 /(log n)1/2 ), then for fixed k, the vector ((βb1 − β1∗ ), . . . , (βbk −
βk∗ )) follows a k-dimensional multivariate normal distribution with mean zero and the
covariance matrix given by the upper left k × k block of S defined at (15).
(3) If bn /τn = o(n1/24 /(log n)/24 ) and ρn b9n /τn9 = o((n/ log n)1/2 ), then for arbitrarily given
                                                  √
nonzero constant vector c = (c1 , . . . , cp )⊤ , N c⊤ (b γ − γ) converges in distribution to the
normal distribution with mean Σ̄ B∗ and variance c⊤ Σ̄c.
                                      −1


    The proof of claim (1) in Theorem 5 is in the supplementary material. The proofs
of claims (2) and (3) in Theorem 5 are respectively similar to the proofs of Theorem
2 and Theorem 3, and omitted. Note that in the proof of the consistency result in
Theorem 5, the independence assumption is only used to derive concentration inequalities
   P P                        P P
for j̸=i k (Aijk −EAijk ) and i<j k zijk (Aijk −EAijk ) in Lemma ??. This result holds,
regardless of the independence assumption, as long as the following event En holds with
high probability:
     n                                                                              o
 En = max |Hi (β ∗ , γ ∗ )| = O(mmax log mmax )1/2 ), ∥Q(β ∗ , γ ∗ )∥∞ = O(N log N ) . (23)
            i


Therefore, we have the following corollary.
Corollary 2. Under Assumption 1, if P(En ) → 1, maxi,j,k ∥zijk ∥∞ ≤ c, and ρn b9n /τn9 =
o((n/ log n)1/2 ), the MLE (β,
                            b γb ) exists and satisfies (22).



5       Numerical Studies
In this section, we evaluate the asymptotic results of the MLE using simulation studies
and a real-world data example.


5.1     Simulation studies
5.1.1    Setting: fixed p = 2, moderate n and mij = 1

We assume that each subject is compared with another subject only once, that is, mij = 1
for all i ̸= j. A comparison between i and j is associated with the two-dimensional
covariate vector zij1 = (zij1,1 , zij1,2 )⊤ . We consider two cases (Case I) and (Case II) for
the covariate settings:
    • (Case I). when i < j, zij1,1 took values −1 or 1 randomly with equal probability,
      and zij1,2 was generated using a standard normal distribution.

    • (Case II). when i < j, zij1,1 takes values −1 or 1 randomly with respective probability
      0.3 and 0.7, and zij1,2 takes values −1 or 1 randomly with respective probability 0.2
      and 0.8.

                                                 19
Note that zji1 = −zij1 . All covariates were generated independently. We set the coeffi-
cient regression of zij1 : γ ∗ = (0.3, 0.3)⊤ . The merit parameters took a linear form, i.e.,
βi∗ = ic log n/n for i = 0, . . . , n, where maxi,j (βi∗ − βj∗ ) = c log n. To assess asymptotic
properties under different asymptotic regimes, we considered four different values of c:
c = 0, 0.05, 0.1, 0.2 and two different values of n: n = 100, 200. Each simulation was
repeated 10, 000 times.
      From Theorem 3, both η̂i = (β̂i − βi∗ )/(1/v̂ii + 1/v̂00 )1/2 and ξˆi,j = [β̂i − β̂j − (βi∗ −
βj∗ )]/(1/v̂ii +1/v̂jj )1/2 converges in distribution to the standard normalities, where v̂i,i is the
estimate of vi,i by replacing (β ∗ , γ ∗ ) with (β, b γ
                                                      b ). Therefore, we assessed the asymptotic
                            ˆ
normalities of η̂i and ξi,j using the quantile-quantile (QQ) plot. The QQ plots for η̂i and
ξˆi,j under both cases (I) and (II) are similar. We only show the plots for η̂i in Figure
2 in case (II) when n = 100. From this figure, we can see that the QQ plots align
with the diagonal lines very well in each sub-figure, indicating the asymptotic normal
approximation is good.

Table 1: The reported values are the coverage frequency (×100%) for βi for a pair i,
denoted as “CF” and the length of the confidence interval “LCI”.
          n                c=0              c = 0.05           c = 0.1               c = 0.2

                        CF      LCI        CF      LCI        CF     LCI        CF        LCI

         100                   Case I: zijk,1 ∈ {−1, 1} with equal prob., zijk,2 ∼ N (0, 1)
                 1     94.99    1.14       94.71 1.15        94.88 1.15        95.15       1.18
                50     94.99    1.14       94.71 1.15        94.61 1.15        95.15       1.17
               100     94.5     1.14       94.59 1.15        94.69 1.15        94.85       1.18
         200    1      94.71    0.81       95.01 0.81        95.05 0.81        95.37       0.84
               100     94.69    0.81       95.08 0.81         95.2 0.81        95.12       0.83
               200     94.92    0.81       95.29 0.81        95.15 0.81        95.15       0.84

                       Case II: zijk,1 ∈ {−1, 1} with (0.3, 0.7), zijk,2 ∈ {−1, 1} with (0.2, 0.8)
         100    1      95.09 1.15         95.09 1.16        95.03 1.18         94.99      1.23
                50     94.96 1.15         94.92 1.16        95.06 1.17         95.09       1.2
               100     94.47 1.15         94.61 1.16        94.68 1.18         95.01      1.23
         200    1      95.07 0.81         95.16 0.82         95.2 0.83         95.09      0.87
               100     95.06 0.81         94.98 0.82        95.29 0.83          94.8      0.85
               200     94.92 0.81         94.88 0.82        94.98 0.83         94.59      0.87


    The MLE existed in all the simulations. Table 1 reports the 95% coverage frequencies
for βi∗ and the length of the confidence interval. As we can see, the length of the confidence
interval decreases as n increases, which qualitatively agrees with the theory. Because the
difference in the merit parameters between adjacent subjects was very small, the lengths
of the confidence intervals were very close across different pairs. This is consistent with
the theoretical length. All the simulated coverage frequencies are close to the nominal

                                                   20
                                     i=1                          i = n/2                              i=n
                      3




                                                       3




                                                                                        3
                      2




                                                       2




                                                                                        2
                      1




                                                       1




                                                                                        1
           c = 0.05

                      0




                                                       0




                                                                                        0
                      −1




                                                       −1




                                                                                        −1
                      −2




                                                       −2




                                                                                        −2
                      −3




                                                       −3




                                                                                        −3
                           −3   −1    0    1   2   3        −3   −1   0     1   2   3        −3   −1    0    1   2   3
                      3




                                                       3




                                                                                        3
                      2




                                                       2




                                                                                        2
                      1




                                                       1




                                                                                        1
           c = 0.1

                      0




                                                       0




                                                                                        0
                      −1




                                                       −1




                                                                                        −1
                      −2




                                                       −2




                                                                                        −2
                      −3




                                                       −3




                                                                                        −3


                           −3   −1    0    1   2   3        −3   −1   0     1   2   3        −3   −1    0    1   2   3
                      3




                                                       3




                                                                                        3
                      2




                                                       2




                                                                                        2
                      1




                                                       1




                                                                                        1
           c = 0.2

                      0




                                                       0




                                                                                        0
                      −1




                                                       −1




                                                                                        −1
                      −2




                                                       −2




                                                                                        −2
                      −3




                                                       −3




                                                                                        −3




                           −3   −1    0    1   2   3        −3   −1   0     1   2   3        −3   −1    0    1   2   3




Figure 2: The figures are the quantile-quatile plots of (β̂i − βi )/(1/v̂ii + 1/v̂00 )1/2 against
the standard normality under the setting Case II, where the horizontal and vertical coor-
dinates denote the theoretical and sample quantiles, respectively. The number of subjects
is n = 100. The first, second, third rows correspond to c = 0.05, c = 0.1 and c = 0.2
in the β-parameter settings. The plot under the case of c = 0 is similar to that under
c = 0.05 and is not shown to save space. The first and second columns correspond to
i = 1, i = n/2 and i = n, respectively.




                                                                 21
level 95%, indicating the asymptotic approximation performs well.
    We draw the QQ plots for the uncorrected estimator γ      b and its bias-corrected estimator
γ
bcorr . Since there are similar phenomena under two different covariate setting and two
different sizes n = 100 and n = 200, only the QQ plots under Case I and n = 100 is
shown in Figure 3 and other plots are not presented. From this figure, we can see that
the quantile-quatile plots of (γ̂1 − γ1 )/σ̂1 against the standard normality deviate obviously
upward from the diagonal line while the QQ plots for the bias-corrected estimator γ̂i,corr
agree with the diagonal lines well. Here, σ̂1 denotes the MLE of the standard error of γ̂1 .
There are similar phenomena in the QQ plots for γ̂2 , which are not shown to save space.
This shows that the bias-corrected estimator leads to more accurate statistical inference
than the uncorrected estimator for the regression coefficient γ.
    Table 2 reports the coverage frequency (×100%) for γ     b (CP) and the coverage frequency
(×100%) for γ  bbc (CPcorr ). From this table, we can see that (1) both values are close to the
target coverage frequency 95%; (2) the coverage frequency for the uncorrected estimator
is a littler lower than 95%; (3) the coverage frequencies for the corrected estimator are
closer to the target level than those for the uncorrected estimator.

Table 2: The reported values are the coverage frequency (×100%) for γ b (CP), the coverage
frequency (×100%) for γbbc (CPcorr ), and length of confidence interval (LCI).
                          c=0                          c = 0.05                       c = 0.1                       c = 0.2

  n     γ        CP       CPcorr     LCI         CP     CPcorr     LCI         CP      CPcorr    LCI         CP      CPcorr      LCI

                                                 Case I: zij1 ∈ {−1, 1} uniformly, zij2 ∼ N (0, 1)
 100    γ1      94.0       95.1      0.12      94.45     95.37    0.12       94.34    95.41    0.12         94.29     94.92      0.12
        γ2      93.94      94.9      0.12      93.95     95.05    0.12       93.66    94.73    0.12         94.27     95.05      0.12
 200    γ1      94.15      94.89     0.06      94.51     95.13    0.06       94.37    94.9     0.06         94.71     95.33      0.06
        γ2      94.84      95.31     0.06      94.33     94.91    0.06       94.62    95.23    0.06         94.56     95.24      0.06

                        Case II: zij1 ∈ {−1, 1} with probabilities 0.3 and 0.7, zij2 ∈ {−1, 1} with probabilities 0.2 and 0.8.
 100    γ1      94.4       95.11      0.12      94.44    95.09     0.12       94.44     95.16    0.12       94.33      95.01     0.12
        γ2      94.16      94.85      0.12      94.32    95.29     0.12       94.39     94.85    0.12       94.39      94.77     0.12
 200    γ1      93.83      94.54      0.06      94.54    95.16     0.06       94.85     95.39    0.06       94.52      95.03     0.06
        γ2      94.8       95.17      0.06      94.14    94.59     0.06        94.5     95.03    0.06       93.97      94.17     0.06




5.1.2        Setting: fixed p = 2, small n = 30 and mij = 4

Motivated by the schedule of the NBA regular season, where each team plays against
every other team 3 or 4 times in the regular season, we carried out simulations under a
small size n = 30 and the number of repeated comparisons mij = 4 for all i ̸= j. The
parameter and covariate settings are the same as those in section 5.1.1. Each simulation
was repeated 10, 000 times.
    All the QQ plots for η̂i and η̂ij , like those QQ plots in Figure 2, match the diagonal
lines very well. Thus, we do not show them here to save space. Because of the same

                                                             22
                                         γ1                                    γ1,corrected


                     3




                                                               3
                     2




                                                               2
                     1




                                                               1
          c = 0.05

                     0




                                                               0
                     −1




                                                               −1
                     −2




                                                               −2
                     −3




                                                               −3
                          −3   −2   −1   0    1   2   3             −3   −2   −1    0     1   2   3
                     3




                                                               3
                     2




                                                               2
                     1




                                                               1
          c = 0.1

                     0




                                                               0
                     −1




                                                               −1
                     −2




                                                               −2
                     −3




                                                               −3




                          −3   −2   −1   0    1   2   3             −3   −2   −1    0     1   2   3
                     3




                                                               3
                     2




                                                               2
                     1




                                                               1
          c = 0.2

                     0




                                                               0
                     −1




                                                               −1
                     −2




                                                               −2
                     −3




                                                               −3




                          −3   −2   −1   0    1   2   3             −3   −2   −1    0     1   2   3



Figure 3: The figures are the quantile-quatile plots of (γ̂1 − γ1 )/σ̂1 against the standard
normality under the setting Case I (zij,1 ∈ {−1, 1} uniformly, zij,2 ∼ N (0, 1)), where the
horizontal and vertical coordinates denote the theoretical and sample quantiles, respec-
tively. Here, the number of items is n = 100. The first, second, third rows correspond
to c = 0.05, c = 0.1 and c = 0.2 in the β-parameter settings. The plot under the case
of c = 0 is similar to that under c = 0.05 and is not shown to save space. The first and
second columns represent the uncorrected and corrected statistics for γ1 , where γ̂1 denotes
the MLE of the standard error of γ̂1 .




                                                          23
reason, I only show the QQ-plots for γ    b2 and γ
                                                 b2,corr under Case II in Figure 4. From this
figure, we can see that both quantile-quatile plots of (γ̂2 − γ2 )/σ̂2 and its corrected version
(γ̂2,corr −γ2 )/σ̂2 against the standard normality agree well with the diagonal line, although
there is a very small derivations for the uncorrected estimator. In contrast to Figure 3,
we find that increasing the number of comparisons in each pair can effectively reduce the
bias. These results indicate that the asymptotic normal approximation is good even if n
is small.
     The coverage frequencies and the confidence intervals with the target level 95% are in
Table 3 for β parameter and Table 4 for γ parameter, respectively. From these tables, we
can see that all simulated coverage frequencies are close to the target level.

Table 3: The reported values are the coverage frequency (×100%) for βi − βj for a pair
(i, j), denoted as “CF” and the length of the confidence interval “LCI”, where the number
of items is 30.
                        c=0              c = 0.05            c = 0.1               c = 0.2

                      CF     LCI        CF      LCI        CF      LCI        CF        LCI

                           Case I: zijk,1 ∈ {−1, 1} with equal prob., zijk,2 ∼ N (0, 1)
           (1, 2)    94.88 1.03        95.26 1.04        94.48 1.04        95.05       1.05
         (15, 16)    95.28 1.03        94.78 1.03        94.76 1.04        94.98       1.04
         (29, 30)    94.81 1.03        95.06 1.04        94.49 1.04        94.95       1.05
           (0, 1)    94.67 1.03        94.99 1.04        95.05 1.04        95.02       1.05
          (0, 15)     95.2 1.03        95.26 1.03        94.61 1.04        95.08       1.05
          (0, 30)    95.05 1.03        95.13 1.04        94.66 1.04        95.11       1.05

                     Case II: zijk,1 ∈ {−1, 1} with (0.3, 0.7), zijk,2 ∈ {−1, 1} with (0.2, 0.8)
           (1, 2)    94.37 1.04         95.01 1.05        94.76 1.06         94.94      1.08
         (15, 16)    95.05 1.04         94.89 1.04        94.96 1.05         94.91      1.06
         (29, 30)    95.18 1.04         94.99 1.05        94.83 1.06         94.76      1.08
           (0, 1)    94.98 1.04         95.12 1.05        94.82 1.06         95.03      1.08
          (0, 15)    94.61 1.04         94.86 1.05        94.85 1.05         94.75      1.07
          (0, 30)    94.03 1.04         93.93 1.05        94.26 1.06          93.5      1.08




5.1.3   Diverging pn = 30, moderate n = 100, and mij=1

Here, we consider a large pn . A pn -dimensional covariate vector zijk is generated as follows.
The first element of zijk takes one value of {−1, 1} with respective probabilities 0.3 and
0.7. The second to fourth elements of zij are generated from a 3-dimensional normal
distribution with mean zero and a covariance matrix, whose diagonal elements are 1’s and
non-diagonal elements are 0.3’s. The other elements are independently generated from
the standard normality. Set γ = (0.3, 0.3, 0.3, 0.3, 1/n, . . . , 1/n), n = 100 and pn = 30.
Other parameters are the same as those in section 5.1.1.

                                                  24
                                         γ2                                    γ2,corrected
                     3




                                                               3
                     2




                                                               2
                     1




                                                               1
          c = 0.05

                     0




                                                               0
                     −1




                                                               −1
                     −2




                                                               −2
                     −3




                                                               −3
                          −3   −2   −1   0    1   2   3             −3   −2   −1    0         1   2   3
                     3




                                                               3
                     2




                                                               2
                     1




                                                               1
          c = 0.1

                     0




                                                               0
                     −1




                                                               −1
                     −2




                                                               −2
                     −3




                                                               −3




                          −3   −2   −1   0    1   2   3             −3   −2   −1    0         1   2   3
                     3




                                                               3
                     2




                                                               2
                     1




                                                               1
          c = 0.2

                     0




                                                               0
                     −1




                                                               −1
                     −2




                                                               −2
                     −3




                                                               −3




                          −3   −2   −1   0    1   2   3             −3   −2   −1    0         1   2   3



Figure 4: The figures are the quantile-quatile plots of (γ̂2 − γ2 )/σ̂2 against the standard
normality under the setting Case II (zij1 ∈ {−1, 1} with probabilities 0.3 and 0.7, zij2 ∈
{−1, 1} with probabilities 0.2 and 0.8), where the horizontal and vertical coordinates
denote the theoretical and sample quantiles, respectively. Here, the number of items is
n = 30. The first, second, third rows correspond to c = 0.05, c = 0.1 and c = 0.2 in the
β-parameter settings. The plot under the case of c = 0 is similar to that under c = 0.05
and is not shown to save space. The first and second columns represent the uncorrected
and corrected statistics for γ2 , where γ̂2 denotes the MLE of the standard error of γ̂2 .




                                                          25
Table 4: The reported values are the coverage frequency (×100%) for γ     b , the coverage
frequency (×100%) for γbbc and the length of confidence interval, denoted as “CF”, CFcorr
and “LCI”, respectively.
                c=0                           c = 0.05                       c = 0.1                        c = 0.2

        CF      CFcorr    LCI         CF       CFcorr        LCI      CF      CFcorr     LCI        CF      CFcorr    LCI

                            Case I: zijk,1 ∈ {−1, 1} with equal probability, zijk,2 ∼ N (0, 1)
 γ1     94.1     94.1     0.19        94.3      93.7         0.19    92.9       93.8     0.19       94.1      94.9    0.19
 γ2     94.1     93.3     0.19        94.3      94.2         0.19    92.9        93      0.19       94.1      93.5    0.19

                         Case II: zijk,1 ∈ {−1, 1} with (0.3, 0.7), zijk,2 ∈ {−1, 1} with (0.2, 0.8)
 γ1     94.13   94.33     0.2         94.3     94.38         0.2     93.98      94.04    0.2        94.44    94.34    0.2
 γ2     94.43   94.55     0.2         94.28    94.25         0.2     94.77      94.67    0.2        94.46    94.32    0.2


   The 95% coverage frequency (×100%) for βi − βj is presented in Table 5. From this
table, we can see that all simulated coverage frequencies are close to the target level. The
QQ plots of η̂i against the standard normality are similar to those in Figure 2, where the
QQ curve aligns with the diagonal line. Therefore, they are not shown. There is similar
reason, the QQ plots for the γ parameters, which are similar to those in Figure 3, are also
not shown.

Table 5: The reported values are the coverage frequency (×100%) for βi − βj for a pair
(i, j), denoted as “CF” and the length of the confidence interval “LCI”, where the number
of items is 100.
                                c=0              c = 0.05             c = 0.1             c = 0.2

                           CF     LCI           CF       LCI         CF      LCI         CF     LCI
              (1, 2)      94.66   1.19         95.04     1.19       94.02    1.19       95.16   1.21
            (49, 50)      94.66   1.19          94.8     1.19       94.34    1.19       94.46   1.19
           (99, 100)      94.84   1.19         94.66     1.19       94.78    1.19       94.72   1.21
              (0, 1)      95.04   1.19         95.08     1.19       94.58    1.19       94.86   1.21
             (0, 50)      95.06   1.19         94.94     1.19       94.96    1.19       94.6    1.2
            (0, 100)       94.4   1.19         94.46     1.19       94.52    1.19        94.8   1.21


    Next, we consider Erdős–Rényi comparison graphs, where each pair is compared with
probability q. Set βi = (i − 1) ∗ 0.2 ∗ log n/(n − 1). Other settings are the same as those
in the above simulation. The 95% coverage frequencies for βi − βj are reported in Table
6. As expected, the estimation accuracy under sparse comparison designs is worse than
that under dense comparison designs. When q becomes smaller, the length of confidence
interval becomes larger. When q = 0.1, the coverage frequencies are far lower than the
target level 95%. There are similar phenomena for the MLE of the covariate parameter,
whose results are not shown.

                                                        26
Table 6: The reported values are the coverage frequency (×100%) for βi − βj for a pair
(i, j), denoted as “CF” and the length of the confidence interval “LCI”, where the number
of items is 100 under Erdős–Rényi comparison graph.
                          q = 0.1            q = 0.3         q = 0.5         q = 0.7

                         CF         LCI     CF     LCI      CF     LCI      CF     LCI
           (1, 2)    88.14(3.58)     4.7   92.92   2.31    95.16   1.74    94.82   1.45
         (49, 50)    87.93(2.88)    4.66   93.44   2.28    94.34   1.72    95.18   1.43
        (99, 100)    87.96(4.02)    4.73   93.86   2.31    94.46   1.74    94.44   1.46
           (0, 1)    88.75(3.46)    4.71   93.24   2.31    94.74   1.74    94.52   1.45
          (0, 50)    88.45(3.2)     4.68   93.86   2.29    94.92   1.73    94.52   1.44
         (0, 100)    86.89(3.46)    4.73   93.56   2.31     94.2   1.74     94.8   1.46


5.1.4   Influence of missing covariates

This section evaluates the influence of missing covariates on statistical inference. All
simulation situation settings are the same as those in section 5.1.1. Therefore, the correct
model has two covariates. To assess the influence of missing covariates on statistical
inference, we fitted the data under three different models: the correct model with two
covariates, the miss-specified model with only one covariate zijk,1 and the Bradley–Terry
model without covariates. Since there are similar phenomena under the covariate setting
(Case I) and (Case II), we only select some QQ-plots under Case II here. Consider the
covariate setting Case II in section 5.1.1
    The QQ-plots for (β̂i − βi )/σ̂i with three different indices i = 1, n/2, n against the
standard normality are in Figure 5. From this figure, we can see that (1) if βi ̸= 0, the
sample quantile agrees with the quantile of the standard normality only when the model
is correct; (2) the QQ-plots lie above the diagonal line under the miss-specified model
with only one covariate, and the Bradley–Terry model without covariates, indicating a
positive bias for the estimator, (3) by comparing the plots between the second row and the
third row, the straight-line distance between the QQ-curve and the diagonal line becomes
larger when the number of missed covariates increases; this phenomenon is also observed
by comparing the plots between the second and third columns in the same row, where
the values of βi increases. There are similar phenomena for the QQ-plots of γ̂1 , which are
not shown to save space.
    In order to compare which of two ranking models is better to fit the data, we further
propose a novel rank-goodness-of-fit measure to compare two models when applying them
                                      (model A)       (model B)
into paired comparison data. Let p̂ijk          and p̂ijk       denote the respective estimator
of the probability of item i winning item j in the k-th comparison under model A and




                                              27
                                    i=1                               i = n/2                              i=n
                     3




                                                      3




                                                                                            3
                     2




                                                      2




                                                                                            2
                     1




                                                      1




                                                                                            1
          c = 0.05

                     0




                                                      0




                                                                                            0
                     −1




                                                      −1




                                                                                            −1
                     −3




                                                      −3




                                                                                            −3
                          −3   −1    0    1   2   3        −3        −1   0     1   2   3        −3   −1    0    1   2   3


                                                                   correct model
                     3




                                                      3




                                                                                            3
                     2




                                                      2




                                                                                            2
                     1




                                                      1




                                                                                            1
          c = 0.05

                     0




                                                      0




                                                                                            0
                     −1




                                                      −1




                                                                                            −1
                     −3




                                                      −3




                                                                                            −3
                          −3   −1    0    1   2   3        −3        −1   0     1   2   3        −3   −1    0    1   2   3


                                                                missing one covariate
                     3




                                                      3




                                                                                            3
                     2




                                                      2




                                                                                            2
                     1




                                                      1




                                                                                            1
          c = 0.05

                     0




                                                      0




                                                                                            0
                     −1




                                                      −1




                                                                                            −1
                     −3




                                                      −3




                                                                                            −3




                          −3   −1    0    1   2   3        −3        −1   0     1   2   3        −3   −1    0    1   2   3


                                                                Bradley−Terry model




Figure 5: The figures are the quantile-quatile plots of (β̂i − βi )/σ̂i against the standard
normality under the setting Case II (zij1 ∈ {−1, 1} with probabilities 0.3 and 0.7, zij2 ∈
{−1, 1} with probabilities 0.2 and 0.8), where the horizontal and vertical coordinates
denote the theoretical and sample quantiles, respectively. Here, the number of items is
n = 100 and each pair is compared once. the β-parameter setting is βi = ci log n/n
for i = 0, . . . , n. Here, I only show the plots when c = 0.05, where there are similar
phenomena when c = 0, 0.1, 0.2. The first, second and third rows correspond to the
correct model with two covariates, the miss-specified model with only one covariate zij1 ,
and the original Bradley–Terry model without covariates.




                                                                    28
model B. The rank-goodness-of-fit measure is defined as
           1 XX               (model A)     (model B)                   (model A)     (model B)
                                                                                                  
RA,B =           1{aijk = 1, p̂ijk       > p̂ijk       } + 1{aijk = 0, p̂ijk       < p̂ijk       } ,
           N
              i<j   k
                                                                                                      (24)
 where 1{·} denotes an indicator function and N is the total number of paired comparisons.
This is motivated by the home-field effect, where the probability of a home team winning
an away team in the CBTM with the home/away covariate is higher than that in the
original Bradley–Terry model. For this measure, we have the relational expression RA,B +
RB,A = 1. The averaged rank-goodness-of-fit measure is reported in Table 7, where two
miss-specified models with only one covariate and no covariate are compared with the
correct model with two covariates. From this table, we can see the proposed measure is
much higher than 1/2 under the correct model.

Table 7: The average rank-goodness-of-fit measure (×100%). Rcorr,miss denotes the com-
parison between the correct model and the model with one missing covariate. Rcorr,BT
denotes the comparison between the correct model and the Bradley–Terry model with no
covariates.
           c=0                    c = 0.05                      c = 0.1                  c = 0.2

 Rcorr,miss   Rcorr,BT      Rcorr,miss   Rcorr,BT        Rcorr,miss   Rcorr,BT    Rcorr,miss   Rcorr,BT

   58.33         59.13        59.16       59.28            59.95          59.41     61.33          59.53




5.2     A real data example
The National Basketball Association (NBA) is the world’s premier men’s professional
basketball league and is one of the major professional sports leagues in North America. It
contains 30 teams equally divided into Eastern and Western conferences. In the regular
season, each team plays two, three, or four games against another, for a total of 82
games, of which 41 games were in their home arena, and 41 were played away. Thus,
there were 1, 230 games in the NBA regular season. We used the 2018-19 NBA regular
season data as an example, which is available from https://www.landofbasketball.
com/yearbyyear/2018_2019_teams.htm. We consider “home/away” as the covariate.
When team i interacts with team j in the kth comparison, we set zijk = 1 if i is at home;
otherwise zijk = −1. The fitted merits are given in Table 8, where we use “Washington
Wizards” as the baseline (βn = 0).
    The estimated home effect γ b and its standard errors are 0.45 and 0.065, respectively.
Under the null hypothesis of having no home effects, this gives a p-value 2.1 × 10−12 ,
indicating a significant home advantage. Since a natural way for the goodness-of-fit test
of the classical Bradley–Terry model is to embed it in a larger family of distributions–the

                                                    29
CBTM, where the corresponding task is to test the null γ = 0, the p-value indicates that
it rejects the Bradley–Terry model to fit this data set under the usual nominal level 0.05.
In addition, when applying the proposed rank-goodness-of-fit measure in (24) to compare
the CBTM and the Bradley–Terry model in this season data, it is 0.59, which is much
larger than 0.5. When applying this measure to the postseason data after the 2018-19
NBA regular season, where the fitted parameters from the regular season data are used,
the value is 0.56 out of 82 games, which is also larger than 0.5. This indicates that the
CBTM has a better fitness than the classical Bradley–Terry model.
    It would be interesting to compare the order of the eight playoff seeds at the two
conferences by the NBA rule, with ordering based on the merits obtained from fitting the
Bradley–Terry model. The order from high to low in the eight playoff seeds of the West-
ern conference is as follows: Warriors, Nuggets, Trailblazers, Rockets, Glasses, Thunder,
Spurs, and Clippers. The corresponding order at the Eastern Conference was: Bucks,
Raptors, 76ers, Celtics, Pacers, Nets, Magics, Pistons. From Table 8, we see that the
ordering of the merits of the Eastern Conference is consistent with that of the NBA rule.
In addition, at the Western conference, the order of seven and eight seeds was switched.

Table 8: The estimates of βi and their standard errors in 2018-19 NBA regular season.
    Order   Subject                   di      β̂i   σ̂i (×10)   Subject                 di     β̂i   σ̂i (×10)
                           Western conference                                 Eastern conference
    1       Golden State Warriors     57      1.5     3.52      Milwaukee Bucks         60     1.6     3.59
    2       Denver Nuggets            54     1.34     3.47      Toronto Raptors         58    1.48     3.54
    3       Portland Trail Blazers    53     1.28     3.46      Philadelphia 76ers      51    1.07     3.45
    4       Houston Rockets           53     1.27     3.46      Boston Celtics          49    0.95     3.43
    5       Utah Jazz                 50     1.09     3.43      Indiana Pacers          48    0.89     3.43
    6       Oklahoma City Thunder     49     1.04     3.43      Brooklyn Nets           42    0.57     3.41
    7       Los Angeles Clippers      48     0.98     3.41      Orlando Magic           42    0.57     3.41
    8       San Antonio Spurs         48     0.97     3.41      Detroit Pistons         41    0.52     3.41
    9       Sacramento Kings          39     0.49      3.4      Miami Heat              39    0.42     3.4
    10      Los Angeles Lakers        37      0.4     3.41      Charlotte Hornets       39    0.42     3.41
    11      Minnesota Timberwolves    36     0.36      3.4      Washington Wizards      32      0      3.45
    12      Memphis Grizzlies         33     0.19     3.43      Atlanta Hawks           29   −0.14     3.47
    13      Dallas Mavericks          33     0.18     3.43      Chicago Bulls           22   −0.56     3.6
    14      New Orleans Pelicans      33     0.15     3.43      Cleveland Cavaliers     19   −0.77     3.69
    15      Phoenix Suns              19    −0.69     3.68      New York Knicks         17    −0.9     3.76




6        Summary and discussion
We present the maximum likelihood estimation of the CBTM. Using a two-stage process,
we demonstrated the consistency of the MLE when the number of subjects approached
infinity. Furthermore, by applying a two/third-order Taylor expansion to score functions,
we establish the asymptotic normality of the MLE. The strategies for deriving the asymp-
totic properties of the MLE shed light on a principal approach to similar problems. These
principles should apply to a class of paired comparison models, in which the logistic dis-
tribution in the Bradley–Terry model is replaced by using other distributions such as

                                                       30
the probit distribution in the Thurstone model [Thurstone (1927)] even for generalized
Bradley–Terry models with ties [Davidson (1970); Rao and Kupper (1967)].
    There exist several issues that need to further investigate. First, the consistency
result in Theorem 1 restricts the diverging rate of the model parameters β and γ while the
asymptotic distributions in Theorems 2 and 3 require a stronger condition. The simulation
results indicate these conditions might be relaxed. Note that the asymptotic behavior of
the MLE depends on the configuration of all parameters. It would be interesting to
investigate whether these conditions could be relaxed. Second, we establish asymptotic
distributions of the MLE in Theorems 3 and 2 under the condition that the dimension of
covariates is fixed, and do not study the asymptotic distributions of the MLE when the
dimension of covariates diverge. In addition, this problem is also not studied in case of
Erdős–Rényi comparison graphs. In the latter, the dimension of covariates could influence
the convergence rate of the covaraite parameter estimator γ̂, which further affects the
remainder terms in the asymptotic representation of the MLE β̂ of the merit parameter.
The simulation results indicate that the asymptotic normal approximation of the MLE is
good. It would also be of interest to explore this problem. Third, although we introduce a
bias-corrected estimator for the regression parameter of covariates in Remark 1, we do not
give a formal result on its asymptotic distribution. To obtain its asymptotic distribution
of γ
   bbc , it faces two difficulties: (1) how to derive the asymptotic variance of B;
                                                                                 b (2) how
to analyze the correlation between γ    b and B.
                                               b It is beyond of the current manuscript to
study this problem. We would like to investigate it in the future work.


Acknowledgements
The supplementary material and simulation codes are available upon request by sending
an email to tingyanty@mail.ccnu.edu.cn.


References
Agresti, A. (2012). Categorical Data Analysis, 3rd Edition. Wiley, New York.
Bradley, R. A. and Terry, M. E. (1952). Rank analysis of incomplete block designs I. the
  method of paired comparisons. Biometrika, 39:324–345.
Brown, L. D. (1986). Fundamentals of Statistical Exponential Families with Applications
  in Statistical Decision Theory (Vol. 9). Lecture Notes-Monograph Series, Hayward,
  CA.
Chen, B., Escalera, S., Guyon, I., Ponce-López, V., Shah, N. B., and Simon, M. O.
  (2016). Overcoming calibration problems in pattern labeling with pairwise ratings:


                                            31
  Application to personality traits. In European Conference on Computer Vision (ECCV
  2016) Workshops, volume 9915, pages 419–432.
Chen, P., Gao, C., and Zhang, A. Y. (2022). Optimal full ranking from pairwise compar-
  isons. The Annals of Statistics, 50(3):1775–1805.
Chen, Y., Fan, J., Ma, C., and Wang, K. (2019). Spectral method and regularized MLE
  are both optimal for top-k ranking. Ann. Statist., 47(4):2204–2235.
Clémençon, S. and Vogel, R. (2020). A multiclass classification approach to label ranking.
  In International Conference on Artificial Intelligence and Statistics, pages 1421–1430.
Colonius, H. (1980). Representation and uniqueness of the Bradley-Terry-Luce model for
  pair comparisons. British Journal of Mathematical and Statistical Psychology, 33(1):99–
  103.
David, H. A. (1988). The Method of Paired Comparisons, 2nd ed. Oxford University
  Press, Oxford.
Davidson, R. R. (1970). On extending the Bradley-Terry model to accommodate ties
  in paired comparison experiments. Journal of the American Statistical Association,
  65(329):317–328.
Dzemski, A. (2019). An empirical model of dyadic link formation in a network with
  unobserved heterogeneity. The Review of Economics and Statistics, (To appear).
Erdős, P. and Rényi, A. (1960). On the evolution of random graphs. Publ. Math. Inst.
  Hungar. Acad. Sci, 5:17–61.
Esteves, P. T., Mikolajec, K., Schelling, X., and Sampaio, J. (2021). Basketball perfor-
  mance is affected by the schedule congestion: NBA back-to-backs under the microscope.
  European Journal of Sport Science, 21(1):26–35.
Fan, J., Hou, J., and Yu, M. (2024). Uncertainty quantification of mle for entity ranking
  with covariates. Journal of Machine Learning Research, 25(358):1–83.
Fienberg, S. E. and Rinaldo, A. (2007). Three centuries of categorical data analysis: Log-
  linear models and maximum likelihood estimation. Journal of Statistical Planning and
  Inference, 137:3430–3445.
Fienberg, S. E. and Rinaldo, A. (2012). Maximum likelihood estimation in log-linear
  models. Ann. Statist., 40(2):996–1023.
Ford, L. R. (1957). Solution of a ranking problem from binary comparisons. The American
  Mathematical Monthly, 64(8):28–33.
Golub, G. H. and Van Loan, C. F. (1996). Matrix Computations. 3rd Edition. Johns
  Hopkins University Press, Baltimore.
Graham, B. S. (2017). An econometric model of network formation with degree hetero-
  geneity. Econometrica, 85(4):1033–1063.
Haberman, S. J. (1977). Maximum likelihood estimates in exponential response models.
  Ann. Statist., 5(5):815–841.


                                            32
Hajek, B., Oh, S., and Xu, J. (2014). Minimax-optimal inference from partial rankings.
  In Advances in Neural Information Processing Systems 27, volume 2, pages 1475–1483.
Han, R., Ye, R., Tan, C., and Chen, K. (2020). Asymptotic theory of sparse bradley-terry
  model. Annals of Applied Probability, 30(5):2491–2515.
Hastie, T. and Tibshirani, R. (1998). Classification by pairwise coupling. Annals of
  Statistics, 26(2):451–471.
He, X. and Shao, Q.-M. (2000). On parameters of increasing dimensions. Journal of
  Multivariate Analysis, 73(1):120 – 135.
Huang, T.-K., Weng, R. C., and Lin, C.-J. (2006). Generalized Bradley-Terry models and
  multi-class probability estimates. Journal of Machine Learning Research, 7:85–115.
Hunter, D. R. (2003). MM algorithms for generalized Bradley-Terry models. Annals of
  Statistics, 32(1):384–406.
Kantorovich, L. V. (1948). Functional analysis and applied mathematics. Uspekhi Mat
  Nauk, pages 89–185.
Liang, H. and Du, P. (2012). Maximum likelihood estimation in logistic regression models
  with a diverging number of covariates. Electron. J. Statist., 6:1838–1846.
Luce, R. D. (1959). Individual choice behavior: A theoretical analysis. John Wiley &
  Sons, Inc., New York.
Masarotto, G. and Varin, C. (2012). The ranking lasso and its application to sport
  tournaments. The Annals of Applied Statistics, 6(4):1949–1970.
Portnoy, S. (1988). Asymptotic behavior of likelihood methods for exponential families
  when the number of parameters tends to infinity. Ann. Statist., 16(1):356–366.
Radlinski, F. and Joachims, T. (2007). Active exploration for learning rankings from
  clickthrough data. In Proceedings of the 13th ACM SIGKDD international conference
  on Knowledge discovery and data mining, pages 570–579.
Rao, P. V. and Kupper, L. L. (1967). Ties in paired-comparison experiments: A gener-
  alization of the Bradley-Terry model. Journal of the American Statistical Association,
  62(317):194–204.
Shah, N. B., Balakrishnan, S., Bradley, J., Parekh, A., Ramchandran, K., and Wain-
  wright, M. J. (2016). Estimation from pairwise comparisons: sharp minimax bounds
  with topology dependence. Journal of Machine Learning Research, 17(1):2049–2095.
Simons, G. and Yao, Y. C. (1998). Approximating the inverse of a symmetric positive
  definite matrix. Linear Algebra & Its Applications, 281(1):97–103.
Simons, G. and Yao, Y.-C. (1999). Asymptotics when the number of parameters tends to
  infinity in the Bradley-Terry model for paired comparisons. The Annals of Statistics,
  27(3):1041–1060.
Sire, C. and Redner, S. (2008). Understanding baseball team standings and streaks. The
  European Physical Journal B, 67(3):473–481.


                                          33
Song, H., Qu, L., Yan, T., and Chen, Y. (2026). Semiparametric analysis for paired
  comparisons with covariates. ArXiv:2603.29333.
Stigler, S. M. (1994). Citation patterns in the journals of statistics and probability.
  Statistical Science, 9(1):94–108.
Thurstone, L. L. (1927). A law of comparative judgment. Psychological Review, 34(4):273–
  286.
Varin, C., Cattelan, M., and Firth, D. (2016). Statistical modelling of citation exchange
  between statistics journals. Journal of The Royal Statistical Society Series A-statistics
  in Society, 179(1):1–63.
Vojnovic, M., Yun, S., and Zhou, K. (2019). Convergence rates of gradient descent and
  MM algorithms for generalized Bradley-Terry models. arXiv preprint arXiv:1901.00150.
Wang, L. (2011). GEE analysis of clustered binary data with diverging number of covari-
  ates. Ann. Statist., 39(1):389–417.
Whelan, J. T. and Wodon, A. (2020). Prediction and evaluation in college hockey using
  the Bradley-Terry-Zermelo model. Mathematics for Application, 8(2):131–149.
Yan, T., Jiang, B., Fienberg, S. E., and Leng, C. (2019). Statistical inference in a di-
  rected network model with covariates. Journal of the American Statistical Association,
  114(526):857–868.
Yan, T., Yang, Y., and Xu, J. (2012). Sparse paired comparisons in the bradley-terry
  model. Statistica Sinica, 22(3):1305–1318.
Yin, C., Zhao, L., and Wei, C. (2006). Asymptotic normality and strong consistency
  of maximum quasi-likelihood estimates in generalized linear models. Science China-
  mathematics, 49(2):145–157.
Zermelo, E. (1929). Die berechnung der turnier-ergebnisse als ein maximumproblem der
  wahrscheinlichkeitsrechnung. Mathematische Zeitschrift, 29(1):436–460.
Zhou, P., Yu, Z., Ma, J., Tian, M., and Fan, Y. (2021). Communication-efficient dis-
  tributed estimator for generalized linear models with a diverging number of covariates.
  Computational Statistics & Data Analysis, 157:107154.




                                            34
