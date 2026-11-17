<!-- source: library/preprints/arXiv/2026/2026 - Subarchetypal Analysis A Semi-Supervised Framework for Archetypal Analysis - Bol s et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.19930 -->
<!-- authors: Vicente J. Bolós, Mireia Mollar-Gumbau, Aleix Alcacer, Irene Epifanio -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-17; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Subarchetypal Analysis: A Semi-Supervised Framework for Archetypal Analysis

                                               Subarchetypal Analysis: A Semi-Supervised
                                                  Framework for Archetypal Analysis
                                                     Vicente J. Bolós1 , Mireia Mollar-Gumbau2 , Aleix Alcacer2 ,
                                                                           Irene Epifanio2,3,∗
                                                 1
                                                     Dept. Business Mathematics, Universitat de València, Av. Naranjos s/n, València, 46022, Spain.
                                                  2
                                                      Dept. Mathematics, Universitat Jaume I, Campus Riu Sec, 12071, Castelló de la Plana, Spain.
arXiv:2611.19930v1 [stat.ME] 15 Nov 2026




                                                        3
                                                            ValgrAI - Valencian Graduate School and Research Network of Artiﬁcial Intelligence.
                                                             e-mail: vicente.bolos@uv.es (V. J. Bolós), mollarm@uji.es (M. Mollar-Gumbau),

                                                                        aalcacer@uji.es (A. Alcacer), epifanio@uji.es (I. Epifanio)




                                                                                        Abstract
                                                    In this work, we introduce subarchetypal analysis, a new semi-supervised framework
                                                for Archetype Analysis (AA) and Archetypoid Analysis (ADA) based on subsets of ob-
                                                servations from which archetypal proﬁles are generated. To the best of our knowledge,
                                                this is the ﬁrst subset-constrained framework for archetypal analysis. Classical AA and
                                                ADA are recovered as special cases, and the location result for archetypes is extended
                                                to the proposed framework. The generating subsets may be deﬁned a priori by the
                                                user to incorporate external knowledge, or determined from intrinsic properties of the
                                                data or the underlying problem structure. As an illustration of the latter, we consider
                                                eﬃcient subarchetypes within Data Envelopment Analysis, where the subsets are deter-
                                                mined by the geometry of the eﬃcient frontier. We develop and implement algorithms
                                                for subarchetypal analysis in both multivariate and functional settings, available in an R
                                                package. The proposed methods are compared with constrained clustering, group-wise
                                                archetypal analysis, and classical unconstrained AA and ADA, and their practical use-
                                                fulness is demonstrated through applications to business, sports analytics, and human
                                                development data.
                                              Keywords: archetypal analysis; data envelopment analysis; eﬃciency; functional data
                                           analysis; semi-supervised learning; sports analytics


                                           1    Introduction
                                           Archetype Analysis (AA) (Cutler and Breiman, 1994) is an unsupervised learning technique
                                           that seeks to identify extremal patterns in datasets. In AA, each observation is approximated
                                           as a convex combination of a set of archetypes, which are themselves convex combinations
                                           of the observed data points. As a result, archetypes constitute representative proﬁles that
                                           allow us to interpret the variability of the dataset. This formulation provides a powerful
                                           framework for dimensionality reduction and feature extraction, as comprehensively reviewed
                                           by Alcacer et al. (2026). Archetypoid Analysis (ADA) (Vinué et al., 2015) extends AA by
                                           restricting the representatives to observed data points rather than convex combinations of
                                           observations, while preserving the convex representation of the observations. This makes the
                                           resulting representatives easier to interpret in applications where actual data instances are
                                           preferred. Although AA and ADA were originally developed for multivariate numerical data,
                                           they have been successfully extended to functional data (Epifanio, 2016).
                                               Throughout the paper, the term “archetypal analysis” is used to refer to the family
                                           of archetype-based methods, including AA, ADA, and their extensions, such as the corre-
                                           sponding functional methodologies. Archetypal analysis lies conceptually between principal

                                                                                                    1
component analysis and clustering techniques, providing a low-dimensional representation
of the data while retaining an interpretation in terms of representative archetypal proﬁles
(Mørup and Hansen, 2012).
    To date, archetypal analysis has been developed exclusively in an unsupervised setting,
with no established semi-supervised framework for exploiting expert knowledge through con-
straints on the archetypal construction process. As in semi-supervised clustering (González-Almagro et al.,
2025), archetypal analysis can beneﬁt from the incorporation of expert-deﬁned constraints
when prior knowledge is available, thereby guiding the identiﬁcation of archetypal proﬁles
toward more meaningful and interpretable representations. To address this gap, we intro-
duce, for the ﬁrst time, a semi-supervised archetypal analysis framework based on subset
constraints on the construction of archetypal proﬁles, which we refer to as subarchetypal
analysis.
    Semi-supervised learning is the branch of machine learning that focuses on using both la-
belled and unlabelled data to perform speciﬁc learning tasks (Van Engelen and Hoos, 2020).
While the vast majority of studies on semi-supervised learning concentrate on semi-supervised
classiﬁcation, the present work diverges from this standard task. Our approach shares a
conceptual aﬃnity with semi-supervised clustering (Jones et al., 2022), as prior labelled in-
formation is embedded directly into the data organizing process rather than used to learn
a mapping function. However, unlike traditional semi-supervised clustering (which strictly
focuses on utilizing group labels to partition the entire dataset), our framework applies these
labels speciﬁcally to ﬁnd the extreme representatives of the data. Speciﬁcally, this framework
operates by injecting known labels as structural constraints to govern subarchetypal analysis,
leveraging the prior group information to explicitly restrict and dictate the admissible subsets
within which the archetypes themselves can be constructed.
    Possible applications of this semi-supervised archetypal analysis arise in settings where
partial expert knowledge is available and can be encoded as constraints on the archetypal
structure. For instance, in biomedical data analysis, clinicians may impose constraints reﬂect-
ing known phenotypes or disease subgroups to guide the discovery of meaningful archetypal
patient proﬁles. In market segmentation, partial labelling of customer types can be used
to steer archetypal proﬁles toward interpretable consumer archetypes consistent with busi-
ness knowledge. Similarly, in remote sensing and environmental science, expert knowledge
about land-cover classes or ecological regions can be incorporated to ensure that the ex-
tracted archetypes respect known physical or geographical structures. In sports analytics,
prior information about player roles or tactical positions can be used to constrain the learning
process so that the resulting archetypes correspond to interpretable playing styles or strate-
gic proﬁles. In human development studies, socio-economic or demographic constraints can
be incorporated to ensure that the resulting archetypal representatives reﬂect meaningful
population proﬁles consistent with known development patterns and inequalities.
    In some applications, such constraints may arise from the intrinsic structural properties
of the problem rather than from expert knowledge, yielding a data-driven setting. A notable
example is provided by Data Envelopment Analysis (DEA) (Charnes et al., 1978), where the
geometry of the eﬃcient frontier naturally induces restrictions on the admissible archetypes
by requiring them to be eﬃcient. The motivation for the present work is rooted precisely in
the computation of such eﬃcient subarchetypes.
    The main contributions of this work are as follows: (i) we introduce, to the best of our
knowledge, the ﬁrst subset-constrained framework for AA and ADA, in which archetypal pro-
ﬁles are generated from user-deﬁned or data-driven subsets. This framework includes classical
AA and ADA as special cases and extends the location result for archetypes; (ii) we develop
algorithms for both the multivariate and functional settings and implement them in the
subarchetypes package for R (R Core Team, 2026); (iii) we show that the proposed frame-
work naturally accommodates the computation of eﬃcient subarchetypes in DEA, where
the generating subsets are determined by the facets of the eﬃcient frontier; and (iv) we
demonstrate its practical usefulness through comparisons with alternative approaches and


                                              2
applications to multivariate and functional human development data.
    The remainder of the paper is organized as follows. Section 2 provides the necessary
mathematical background. In particular, Section 2.1 reviews the fundamentals of archetypal
analysis, whereas Section 2.2 introduces the basic concepts of DEA. Section 3 introduces the
proposed semi-supervised archetypal analysis framework and extends the location result for
archetypes. Section 4 develops the corresponding algorithms, including a simulation study
of their computational cost and heuristic strategies for screening candidate conﬁgurations.
Section 5 presents motivating applications of the proposed methodology, including eﬃcient
subarchetypes in DEA and multivariate and functional applications to human development
data. Finally, Section 6 concludes the paper and outlines directions for future research. The
proofs are provided in Appendix A. Additional illustrative comparisons with constrained
clustering (a form of semi-supervised clustering), group-wise archetypal analysis, and classical
unconstrained archetypal analysis are reported in Appendix B.


2       Mathematical background
2.1     Archetypal analysis
This section provides the basic background on archetypal analysis required for the remainder
of the paper. We ﬁrst review the concepts of archetypes and archetypoids for multivariate
observations and then present their extension to functional observations through functional
archetypal analysis.

2.1.1    Archetypes and archetypoids
         n
Let {xi }i=1 denote a sample of m-dimensional observations. In Archetype Analysis (AA),
                      k
the k archetypes {zj }j=1 are deﬁned as convex combinations of the observations:
                                          n
                                          X
                                   zj =         βjl xl ,         j = 1, . . . , k,                      (1)
                                          l=1
                  Pn
with βjl ≥ 0 and l=1 βjl = 1. In matrix form, (1) is expressed as Zk×m = βk×n Xn×m .
Each observation is then approximated as a convex combination of the archetypes:
                                            k
                                            X
                             xi ≈ x̂i =              αij zj ,        i = 1, . . . , n,                  (2)
                                            j=1

                  Pk
with αij ≥ 0 and j=1 αij = 1, which in matrix form is given by X̂n×m = αn×k Zk×m .
Under these constraints, we minimize the residual sum of squares
                                                                                                    2
                             n                          n                k           n
                                                 2
                             X                          X                X           X
                    RSS =          kxi − x̂i k =                 xi −          αij         βjl xl
                             i=1                        i=1              j=1         l=1
                                                                               !2                     (3)
                             X m
                             n X                     k
                                                     X            n
                                                                  X
                         =             xig −              αij           βjl xlg  ,
                             i=1 g=1                 j=1           l=1

where k · k represents the Euclidean norm. In certain cases, when the variables corresponding
to each observation diﬀer in nature and are expressed in diﬀerent units of measurement, the
data should be brought to a common scale prior to analysis, for example by standardization,
normalization, or rank transformation.
    In summary, parameters βjl deﬁne archetypes from observations, while αij describe how
each observation is approximated as a mixture of these archetypes.

                                                           3
                                                                                      k
    In Archetypoid Analysis (ADA) (Vinué et al., 2015), the k archetypoids {zj }j=1 are de-
ﬁned as single observations. So, they are given by (1) with βjl ∈ {0, 1} and nl=1 βjl = 1.
                                                                              P
Each observation is also approximated as a convex combination of the archetypoids in the
same way as (2), and the residual sum of squares given by (3) is minimized.
    The number of archetypes or archetypoids k may be chosen by a domain expert based on
prior knowledge or determined using an elbow-type criterion, the most widely used approach
in practice, selecting the value of k at which the RSS curve ﬂattens (Cutler and Breiman,
1994; Eugster and Leisch, 2009; Vinué et al., 2015). Alternatively, other criteria may be
adopted, such as the model consistency criterion proposed by Hinrich et al. (2016).

2.1.2   Functional archetypal analysis
Let {xi (t)}ni=1 be a set of univariate observed functions deﬁned on the interval [a, b]. Through-
out this work, we assume that the functions satisfy suitable smoothness conditions and be-
long to the Hilbert space L2 [a, b] of square-integrable functions. The objectives of Functional
Archetype Analysis (FAA) and Functional Archetypoid Analysis (FADA) are the same as in
the multivariate case, replacing vectors by functions and the Euclidean norm by the L2 -norm.
   Using a basis representation, each function is expressed as xi (t) = b′i B, where bi is the
vector of basis coeﬃcients of the i-th observed function, B is the vector of basis functions,
and ′ denotes transpose. The RSS can then be written as (Epifanio, 2016)
                                              n
                                              X
                                      RSS =         a′i W ai ,                                (4)
                                              i=1

                 Pk      Pn
where a′i = b′i − j=1 αij l=1 βjl b′l , and W is the matrix of inner products between basis
functions. For an orthonormal basis, W is the identity matrix, reducing FAA (FADA) to
AA (ADA) applied to the basis coeﬃcients.

2.2     Data envelopment analysis
In this section, we review the theoretical framework and fundamental concepts of Data En-
velopment Analysis (DEA) that are required to develop the notion of eﬃcient subarchetypes
in Section 3.3. To provide the necessary context, DEA is a non-parametric methodology
for assessing the relative eﬃciency of a homogeneous set of Decision-Making Units (DMUs)
that transform multiple inputs into multiple outputs (Cooper et al., 2007). Through math-
ematical programming models, DEA identiﬁes the best-performing DMUs and constructs
the corresponding eﬃcient frontier. Units located on this frontier are classiﬁed as eﬃcient,
whereas those outside it are deemed ineﬃcient.

2.2.1   Eﬃcient frontier
Let D = {DMU1 , . . . , DMUn } be a set of n DMUs with m1 inputs and m2 outputs. Let
us denote by xig1 and yig2 the g1 -th input and g2 -th output, respectively, of the i-th DMU.
We also assume that xig1 and yig2 are all positive, i.e. greater than 0. In this framework,
                                                                                m1           m2
we call activity to any pair of positive vectors (x, y) ∈ Rm  >0 , where x ∈ R>0 and y ∈ R>0 .
Any DMUi ∈ D has its associated activity (xi , yi ), where xi = (xi1 , . . . , xim1 ) and yi =
(yi1 , . . . , yim2 ). Therefore, we can identify a DMU with its activity in the same way that a
point is identiﬁed with its coordinates.
    We say that an activity (x, y) dominates another activity (x′ , y ′ ) if x ≤ x′ and y ≥ y ′ .
In this case, (x, y) is considered to be more (or equally) eﬃcient than (x′ , y ′ ), because it
consumes less (or equal) inputs and produces more (or equal) outputs. The relation “to be
dominated by” is a partial order on the set of activities.




                                                4
    The production possibility set is the set of feasible activities deﬁned by D. Assuming
strong disposability of inputs and outputs, and variable returns to scale (VRS), it is formed
by all the activities dominated by convex combinations of DMUs in D. Hence, it is given by
                                    Pn                                             
                   
                                      i=1 λi xig1 ≤ xg1 ,     g1 = 1, . . . , m1  
                                     Pn
             P = (x, y) ∈ Rm   >0          λ  y
                                            i ig2  ≥ y g2 ,    g 2 = 1, . . . , m 2   .    (5)
                                    Pi=1
                                       n                                            
                                       i=1 λi = 1,    λi ≥ 0, i = 1, . . . , n
                                                                                   

Constant
Pn         returns to scale (CRS) can also be considered by removing the convexity condition
       λ
   i=1 i  = 1 from (5). However, this convexity condition (and thus the assumption of VRS)
is essential for conducting archetypal analysis.
    A DMU (or an activity, in general) is eﬃcient if and only if there is no (x, y) ∈ P ,
diﬀerent from the DMU, that dominates the DMU (Koopmans, 1951). Hence, a DMU is
eﬃcient if and only if there is not another feasible activity in the production possibility set
“better than” the DMU, in the sense that consumes less (or equal) inputs and produces
more (or equal) outputs, with at least one strict inequality. Otherwise, we say that it is
ineﬃcient. The set of eﬃcient activities in P is called the eﬃcient frontier (also known as
strongly eﬃcient frontier or Pareto-Koopmans frontier ) of P , and we denote it by ∂ S (P ). It
is clear that ∂ S (P ) is in the frontier of P , but it does not cover all the frontier (see Figure 1).




Figure 1: Eﬃcient frontier (solid line) and the rest of the frontier (dashed line) of the pro-
duction possibility set (shaded in grey) for a set of DMUs with one input and one output
under VRS. The eﬃcient DMUs are named A, B, C, and D.


2.2.2    Maximal friends sets
Given a subset of DMUs, F ⊆ D, it is called friends if any convex combination of DMUs in F
is eﬃcient. In Tone (2010) it is proved that F is friends if and only if a convex combination
of all DMUs in F is eﬃcient.
    A friends set F is said to be maximal if it is not contained in any other friends set.
Each maximal friends set determines a facet of the eﬃcient frontier. In particular, under
the assumption of VRS, a maximal friends set consists of the vertices that deﬁne a facet of
the eﬃcient frontier. Consequently, the eﬃcient frontier can be fully characterized by the
collection of all maximal friends sets (i.e. the vertices of its facets), denoted by F . It follows
that, under VRS, any eﬃcient activity in P can be represented as a convex combination of
the DMUs belonging to a maximal friends set.




                                                  5
3     Methodology
We now present our semi-supervised archetypal analysis framework, comprising subarchetypes,
subarchetypoids, and several important special cases, including partitioned archetypes and ef-
ﬁcient subarchetypes. Throughout this paper, we use the term “semi-supervised” to refer
to archetypal analysis in which the construction of archetypal proﬁles is constrained by a
prescribed family of generating subsets. These generating subsets may be speciﬁed a priori
by the user, for example to incorporate external knowledge or structural requirements, or
they may be determined from intrinsic properties of the data or the underlying problem, as
for computing eﬃcient subarchetypes in Section 3.3.
    Illustrative toy examples of the proposed methodology are provided in Appendix B.

3.1    Subarchetypes and subarchetypoids
               r                                                                             n
Let S = {Sp }p=1 be a family of r nonempty subsets of the set of observations {xi }i=1 ,
referred to as generating subsets. We note that the union of the generating subsets need
not cover the entire set of observations, thereby allowing the framework to accommodate
partially labelled datasets. Moreover, the generating subsets are not required to be pairwise
disjoint.
               k                                                 n
    Let {zj }j=1 be the set of k subarchetypes of {xi }i=1 with respect to S. Each zj is
deﬁned as a convex combination of observations in some generating subset Sp(j) ⊆ S, where
p(j)
Pn ∈ {1, . . . , r} for j = 1, . . . , k. Subarchetypes can be written as (1) with βjl ≥ 0 and
   l=1 βjl = 1, where βjl = 0 if xl ∈     / Sp(j) .
    Each observation is then approximated as a convex combination of the subarchetypes in
the same way as (2). Finally, the residual sum of squares given by (3) is minimized. We will
refer to Subarchetype Analysis as subAA.
    Note that p(j) speciﬁes the generating subset used to construct the j-th subarchetype.
Speciﬁcally, the j-th subarchetype is generated as a convex combination of the elements in
the p(j)-th generating subset. In the absence of any prior preference,     all possible conﬁgura-
tions of p(j) must be considered. In general, this results in k+r−1     k  distinct conﬁgurations,
which represents the number of combinations with repetition when distributing k identical
elements (subarchetypes) into r distinct categories (generating subsets). Alternatively, prior
preferences can be incorporated through p(j) by restricting the set of admissible conﬁgura-
tions. For instance, one may impose the constraint that each generating subset generates
at most one subarchetype (see Section 4.4). This excludes all conﬁgurations for which there
exist j1 , j2 ∈ {1, . . . , k} with j1 6= j2 such that p(j1 ) = p(j2 ).
Remark 3.1 (AA versus subAA). The distinction between AA and subAA lies in the
additional constraints βjl = 0 imposed on the deﬁnition of the subarchetypes zj in (1)
whenever xl ∈ / Sp(j) . No additional constraints are imposed on the coeﬃcients αij . Since
the residual sum of squares to be minimized is given by (3), all observations contribute to
the optimization process. Another distinctive feature of subAA is that user-deﬁned lower
and/or upper bounds may be imposed on the number of subarchetypes associated with each
generating subset.
Remark 3.2 (Subarchetypes as a Generalization of Archetypes and Archetypoids).
Subarchetypes generalize both archetypes and archetypoids. Speciﬁcally, archetypes arise as
a special case of subarchetypes when r = 1 and S1 = {xi }ni=1 . Conversely, archetypoids
correspond to the case r = n, with Sp = {xp } for p = 1, . . . , n. Thus, the subarchetype
framework encompasses archetypes and archetypoids as two extreme cases.
    Analogously, subarchetypoids are deﬁned as archetypoids under subset
                                                                       Pn constraints. In
this case, a subarchetypoid zj is given by (1) with βjl ∈ {0, 1} and l=1 βjl = 1, where
βjl = 0 if xl ∈
              / Sp(j) , and p(j) specifying the generating subset used to construct the j-th
subarchetypoid. Each observation is approximated by (2), and the residual sum of squares

                                                6
(3) is minimized. As in the case of archetypoids, each subarchetypoid corresponds to a single
                                                                                         n
observation. Moreover, they also generalize archetypoids in the case r = 1 and S1 = {xi }i=1 .
We will refer to Subarchetypoid Analysis as subADA.
Remark 3.3 (ADA versus subADA). The distinction between ADA and subADA lies
solely in the user-deﬁned lower and/or upper bounds that may be imposed on the number of
subarchetypoids associated with each generating subset, provided that every observation be-
longs to at least one generating subset. If no such bounds are speciﬁed, subADA is equivalent
to ADA, and the resulting subarchetypoids coincide with the archetypoids.
    An intuitive interpretation of subarchetypes and subarchetypoids is to regard the obser-
vations as animals and each generating subset as a group of genetically compatible animals.
Subarchetypes can then be interpreted as feasible hybrids within each generating subset,
thereby excluding unrealistic combinations analogous to chimeras or crosses between ge-
netically incompatible animals. In contrast, subarchetypoids correspond to actual animals
belonging to groups of genetically compatible animals. If no constraints are imposed on the
number of subarchetypoids associated with each generating subset, subarchetypoids coincide
with archetypoids.
    As with AA and ADA, subAA and subADA can be extended to datasets consisting of
samples of univariate observed functions (see Section 2.1.2), giving rise to Functional Sub-
archetype Analysis (subFAA) and Functional Subarchetypoid Analysis (subFADA), respec-
tively.
    Finally, the number of subarchetypes or subarchetypoids can be selected using criteria
analogous to those described in Section 2.1.1 for AA and ADA. The user may specify a priori
the desired number of representatives generated from each subset, thereby ﬁxing the total
number k. Otherwise, the elbow criterion can be used to determine k, selecting, for each
value of k, the combination of representatives generated from the subsets that minimizes the
RSS.

3.2    Location of subarchetypes and subarchetypoids
The following result about the location of a set of archetypes {zj }kj=1 can be found in
Cutler and Breiman (1994):
                                                     n
Proposition 3.1. Let C be the convex hull of {xi }i=1 . Let B be the set of data points on
∂C (the boundary of C), and let N be the cardinality of B.
  1. If k = 1, choosing z1 to be the sample mean minimizes RSS.
                                                     k
  2. If 1 < k < N , there is a set of archetypes {zj }j=1 on ∂C that minimizes RSS.
                              k
  3. If k = N , choosing {zj }j=1 = B results in RSS = 0.
    The following proposition extends Proposition 3.1 to subarchetypes with respect to a
                                          r
collection of generating subsets S = {Sp }p=1 , considering all possible conﬁgurations:
Proposition 3.2. Let CS be the convex hull of ∪rp=1 Sp . Let BS be the set of data points on
∂CS , and let NS be the cardinality of BS . Moreover, let Cp be the convex hull of the p-th
generating subset Sp , for p = 1, . . . , r.
  1. If k = 1,
      (a) and the sample mean x̄ belongs to ∪rp=1 Cp , choosing z1 = x̄ minimizes RSS.
      (b) and the sample mean x̄ does not belong to ∪rp=1 Cp , there is a subarchetype z1 on
          ∂ ∪rp=1 Cp that minimizes RSS.



                                              7
                                                            k
  2. If 1 < k < NS , there is a set of subarchetypes {zj }j=1 on ∂ ∪rp=1 Cp that minimizes
     RSS.
                                  k
  3. If k = NS , choosing {zj }j=1 = BS yields a minimum of the RSS. Moreover, if
                     n
     ∪rp=1 Sp = {xi }i=1 then RSS = 0.
                                                                        n
Remark 3.4. In the case k = NS , the condition ∪rp=1 Sp = {xi }i=1 can be relaxed to
B ⊆ ∪rp=1 Sp , where B is deﬁned in Proposition 3.1. Since every observation belongs to the
convex hull of B, this weaker condition is suﬃcient to ensure that RSS = 0.
Remark 3.5. Proposition 3.2 generalizes the original result by Cutler and Breiman (1994)
given in Proposition 3.1. Indeed, Proposition 3.1 is recovered by taking r = 1 and S1 =
{xi }ni=1 , that is, when subarchetypes coincide with archetypes (see Remark 3.2). In this
                              n
special case, ∪rp=1 Sp = {xi }i=1 , CS = C, BS = B, NS = N , and ∪rp=1 Cp = C.
    Finally, it is worth noting that the location result of Proposition 3.2 does not extend to
subarchetypoids. Indeed, just as archetypoids are not necessarily located on the boundary
of the convex hull of the observations, subarchetypoids are not necessarily located on the
boundary of ∪rp=1 Cp . Several counterexamples for archetypoids are given in Vinué et al.
(2015); the same examples immediately extend to the subarchetypoid setting.

3.3    Eﬃcient subarchetypes
Given a set of DMUs, computing archetypes from the set of eﬃcient DMUs does not nec-
essarily produce eﬃcient archetypes. This is because unconstrained convex combinations of
eﬃcient DMUs are not guaranteed to remain on the eﬃcient frontier.
    The occurrence of ineﬃcient archetypes computed from eﬃcient DMUs is not merely a
theoretical possibility, but also arises frequently in practice. For example, in simulations
based on 200 DMUs with three inputs and three outputs generated independently from a
normal distribution, approximately 30 DMUs are eﬃcient on average. In each simulation,
ﬁve archetypes were computed from the eﬃcient DMUs. Over 100 simulation runs (500
archetypes in total), about 35% of the resulting archetypes were ineﬃcient. Although this
percentage naturally depends on the characteristics of the problem and the data-generating
distribution, it shows that obtaining ineﬃcient archetypes from eﬃcient DMUs is not an
exceptional situation.
    The following proposition provides a suﬃcient condition for guaranteeing that every sub-
archetype lies on the eﬃcient frontier.
Proposition 3.3. Let D be a set of DMUs, and let E denote the corresponding set of eﬃcient
DMUs. If the generating subsets are friends sets, then every subarchetype of E is both feasible
and eﬃcient, and therefore lies on the eﬃcient frontier.
    Assuming VRS, the eﬃcient frontier of D is composed of facets whose vertex sets are
the maximal friends sets, all of which are subsets of E. In this setting, a feasible activity
is eﬃcient if and only if it lies on one of these facets, or equivalently, if and only if it can
be expressed as a convex combination of the corresponding maximal friends set. Within the
subAA framework, taking maximal friends sets as generating subsets guarantees that the
resulting subarchetypes of E are feasible activities lying on the eﬃcient frontier. Moreover,
every point of the eﬃcient frontier belongs to the convex hull of some generating subset, so no
region of the eﬃcient frontier is excluded from containing a subarchetype. Such subarchetypes
will be referred to as eﬃcient subarchetypes.
    As an illustration, in Figure 1, the set of eﬃcient activities is {A, B, C, D}, and the
generating subsets are the vertex sets of the facets of the eﬃcient frontier: S1 = {A, B}, S2 =
{B, C}, and S3 = {C, D}. Consequently, every region of the eﬃcient frontier is represented
by at least one generating subset, allowing subarchetypes to be located anywhere on the
eﬃcient frontier.

                                               8
3.4    Partitioned archetypes
A particular case of subarchetypes with a wide range of applications arises when the gener-
ating subsets form a partition of the set of observations.
                    r                                                           n
    Let P = {Pp }p=1 be a partition of the set of observations {xi }i=1 , that is, a collection
of nonempty pairwise disjoint subsets whose union is the entire set of observations. The
corresponding subarchetypes with respect to P are also referred to as partitioned archetypes.
    Typically, it is desirable that {p(j)}kj=1 = {1, . . . , r}, i.e., each element of P generates at
least one
         partitioned archetype. In this case, the number of possible             conﬁgurations of p(j)
is k−1
    r−1  . For ﬁxed   r, this quantity is asymptotically     of order   k r−1
                                                                              . However, this condition
may be relaxed in the general case without the need to impose any additional restrictions,
thereby allowing some elements of the partition not to generate any partitioned archetypes.
    Analogously, partitioned archetypoids can be deﬁned when subarchetypoids are considered
instead of subarchetypes. It is also possible to construct subarchetypoids and subarchetypes
from collections of subsets contained within each element of P. In this case, we can name
them partitioned subarchetypoids and partitioned subarchetypes, respectively.
    For example, we could consider an analogy in which observations represent vertebrate an-
imals and the partition elements correspond to major taxonomic groups (mammals, reptiles,
birds, ﬁsh, and amphibians). Partitioned archetypes within each group identify the most
distinctive representatives relative to the rest of the vertebrates. By further considering
subsets of genetically compatible animals within each group, the corresponding partitioned
subarchetypes avoid unrealistic combinations, in the same way that biological constraints
preclude the existence of chimeras. Another example is given in Section 5.1.2 for NBA
players.
    It may also be of interest to apply partitioned archetypal analysis to country-level data,
where the partition elements represent groups of countries, such as continents or associations.
Similarly, the methodology could be applied to ﬁrm-level economic data, with partition ele-
ments corresponding, for example, to economic sectors.


4     Algorithms
This section describes the algorithms underlying the proposed methodology. Sections 4.1 and
4.2 present the procedures for computing subarchetypes and subarchetypoids, respectively,
for a given subset conﬁguration. As in the classical AA and ADA frameworks, these algo-
rithms extend naturally to the functional setting, giving rise to subFAA and subFADA by
simply replacing the objective function with the corresponding functional RSS. Section 4.3
analyses the computational cost when all subset conﬁgurations are considered and presents
a simulation study. Finally, Section 4.4 introduces heuristic screening strategies for reducing
the number of candidate subset conﬁgurations to be evaluated.
    We implemented the algorithms for computing subarchetypes and subarchetypoids in
the subarchetypes package for R (R Core Team, 2026). The package allows users either
to specify lower and upper bounds on the number of subarchetypal proﬁles generated by
each subset or to provide only the total number of proﬁles, k, in which case the algorithm
automatically selects the subset allocation that minimizes the RSS. The computation of
maximal friends sets is implemented in the deaR R package (Bolós et al., 2025) available at
CRAN (https://cran.r-project.org/package=deaR). The package subarchetypes and
the scripts required to reproduce all experimental results in Section 5 and Appendix B and
are available at https://www.uv.es/vbolos/investigacion/subarchetypes.zip.

4.1    Subarchetype computation
Given a candidate conﬁguration specifying how many subarchetypes have to be generated
from each generating subset, the subarchetypes are computed as follows.


                                                  9
    We have modiﬁed the original alternating minimization algorithm proposed by Cutler and Breiman
(1994). This algorithm alternates between two constrained optimization steps. First, with
the archetypes ﬁxed, each observation is expressed as a convex combination of the archetypes
by estimating non-negative coeﬃcients that sum to one. Second, with these coeﬃcients ﬁxed,
each archetype is updated as a convex combination of the observed data, again subject to
non-negativity and sum-to-one constraints.
    In subAA, this step is modiﬁed so that each subarchetype is updated as a convex combi-
nation of only the observations assigned to its corresponding generating subset, rather than
all observed data. Accordingly, the initialization is also modiﬁed. Instead of randomly select-
ing the initial archetypes, as in the original algorithm, one observation is selected from each
predeﬁned generating subset. When these subsets overlap, observations are chosen without
replacement so that the same observation is not used to initialize multiple subarchetypes.
    These two steps are repeated iteratively until the RSS converges, yielding a set of sub-
archetypes that best represent the extreme patterns in the data while providing a convex
reconstruction of every observation. The same algorithm applies to both the multivariate
and functional settings by simply using the appropriate RSS.
    The convergence properties of the proposed algorithm are inherited from those of the
alternating optimization algorithm of Cutler and Breiman (1994). The only modiﬁcation
consists of restricting each archetype to be a convex combination of the observations be-
longing to its prescribed generating subset. Consequently, each optimization step remains a
convex least-squares problem over a compact convex feasible set. As in the classical algo-
rithm, every iteration decreases (or leaves unchanged) the residual sum of squares, which is
bounded below by zero. Therefore, the sequence of objective values is monotone and conver-
gent. The same arguments as those of Cutler and Breiman (1994) establish convergence of
each inner loop to the minimizer of the corresponding restricted convex least-squares prob-
lem. As in classical archetypal analysis, however, the alternating optimization procedure is
not guaranteed to attain the global minimum, and diﬀerent initializations may converge to
diﬀerent local minima.
    As in k-means clustering, AA and subAA are initialized multiple times from diﬀerent
starting points to reduce the risk of becoming trapped in local minima, retaining the solution
with the smallest RSS.

4.2    Subarchetypoid computation
Given a candidate conﬁguration specifying how many subarchetypoids have to be generated
from each generating subset, the subarchetypoids are computed as follows.
    The algorithm for subADA is identical to that of ADA (see Vinué et al. (2015) for details),
except that the subset constraints are enforced throughout the optimization. In the BUILD
phase, the required number of subarchetypoids is selected within each generating subset,
without replacement, according to the corresponding restrictions. In the SWAP phase, each
subarchetypoid is allowed to swap only with observations belonging to the same generating
subset. The algorithm iterates until a suﬃciently small value of the RSS while preserving the
prescribed number of subarchetypoids in each subset. As before, the same algorithm applies
to both the multivariate and functional settings by simply using the corresponding RSS.
    The proposed modiﬁcations preserve the main properties of the original ADA algorithm,
while reducing the size of the search space. Since each swap is restricted to observations
within the corresponding generating subset, the number of candidate exchanges evaluated at
each iteration is reduced, potentially leading to faster convergence in practice.
    As in subAA, subADA is initialized multiple times from diﬀerent starting points, and the
solution with the smallest RSS is retained.
    Like ADA, subADA can be scaled to large datasets by extending the scalable optimization
strategy proposed by Vinué and Epifanio (2021). The only modiﬁcations required are to
enforce the subset constraints during the BUILD and SWAP phases.


                                              10
4.3     Computational cost
The computational cost of subAA (and, analogously, of subADA) diﬀers from that of classi-
cal AA (and ADA, respectively) mainly because several candidate conﬁgurations may have
to be evaluated. Throughout this section, the discussion is presented for subAA and AA,
but the same arguments apply directly to subADA and ADA. It is therefore useful to distin-
guish between the cost of solving a single optimization problem and the cost of exploring all
candidate conﬁgurations.
    For a ﬁxed candidate conﬁguration, the computational cost of subAA is essentially the
same as that of classical AA. Indeed, once the generating subset assigned to each subarchetype
has been ﬁxed, the optimization algorithm is identical to that of AA, except that the coef-
ﬁcients deﬁning each subarchetype are constrained to observations belonging to the corre-
sponding generating subset. Consequently, the computational complexity of one execution
of subAA is of the same order as that of AA.
    The additional computational eﬀort arises from the need to evaluate multiple candidate
conﬁgurations. As shown in Section 3.1, in the absence of any prior preference,       the total
number of candidate conﬁgurations for computing subarchetypes is k+r−1
                                                                            
                                                                         k    . For ﬁxed k, this
quantity grows asymptotically as O(rk ). More generally, if TAA denotes the computational
cost of a single execution of the AA algorithm, then the overall computational cost of subAA
is proportional to Nconf TAA , where Nconf is the number of candidate conﬁgurations evaluated.
    Therefore, the computational bottleneck of subAA is generally not the optimization itself,
but the combinatorial growth in the number of candidate conﬁgurations. This motivates
the screening procedures proposed in Section 4.4, whose objective is to discard unlikely
conﬁgurations before running the optimization algorithm.
    Another important feature is that the candidate conﬁgurations are completely indepen-
dent. Consequently, each conﬁguration can be evaluated separately, making the proposed
methodology embarrassingly parallel and particularly suitable for multi-core and distributed
computing environments. This allows substantial reductions in execution time through par-
allel implementation.

4.3.1   Simulation study
To illustrate the computational behaviour of the proposed methodology, we conducted a
simulation study focusing on the eﬀect of the number of generating subsets. The remaining
parameters (number of observations, dimension of the observations, and number of sub-
archetypes) were kept ﬁxed, as their inﬂuence on the computational cost of AA has already
been studied by Eugster and Leisch (2009).
    We generated datasets consisting of n = 128 observations in dimension m = 5, using a
multivariate standard normal distribution. We computed k = 4 subarchetypes with respect
to diﬀerent numbers of generating subsets, namely r ∈ {1, 2, 4, 8, 16}. For each value of r,
the observations were partitioned into generating subsets of the same size.
    For each scenario, 50 independent datasets were generated. The complete subAA proce-
dure was then applied to each dataset, evaluating all candidate conﬁgurations ﬁve times from
diﬀerent initial conditions. For each dataset, the lowest RSS obtained across all candidate
conﬁgurations and initial conditions was recorded, together with the total elapsed computa-
tion time required for the ﬁve runs. All computations were performed using R version 4.5.1
on a computer equipped with an Intel® Core™ i9-10900KF CPU @ 3.70 GHz and 64 GB of
RAM, running Ubuntu 24.04.4 LTS (Linux kernel 6.8.0-117-generic).
    Figure 2 shows the computational results for the diﬀerent values of the number of gener-
ating subsets r. The three panels report the total computation time, the computation time
per candidate conﬁguration (ﬁve runs), and the resulting RSS, respectively. As expected, the
total computation time increases substantially with r, reﬂecting the growth in the number
of candidate conﬁgurations. In contrast, the computation time per conﬁguration decreases
as r increases. This behaviour can be attributed to the fact that, for larger values of r,


                                              11
each subarchetype is constructed from a more restricted subset of observations, leaving fewer
alternatives within each optimization problem and thus facilitating convergence. The de-
crease in the standard deviation of the computation time per conﬁguration indicates that
the computation times become less dispersed as r increases. Regarding the RSS, its increase
relative to the classical AA case (r = 1) is relatively small, and the values tend to stabilize for
larger numbers of generating subsets. Thus, in this simulation setting, increasing the num-
ber of generating subsets has a comparatively limited eﬀect on the quality of the resulting
subarchetypal representation.




Figure 2: Computational performance of subAA for diﬀerent numbers of generating subsets r.
The panels show, from left to right, the total computation time (in seconds, on a logarithmic
scale), the computation time per candidate conﬁguration, and the resulting RSS. Each point
represents the mean over the simulated datasets, with error bars indicating ±1 standard
deviation. The computation times include the ﬁve runs from diﬀerent initial conditions,
while the reported RSS is the lowest value obtained across all candidate conﬁgurations and
initial conditions.


4.4    Screening candidate conﬁgurations
Computing subarchetypes requires considering a potentially large number of candidate con-
ﬁgurations involving k subarchetypes and r generating subsets, and the same holds for sub-
archetypoids.   As shown in Section 3.1, the total number of candidate conﬁgurations is
 k+r−1
       
    k   , which grows as O(rk ) for ﬁxed k. Consequently, exhaustive evaluation may become
computationally prohibitive even for moderate values of r.
    When the number of candidate conﬁgurations becomes prohibitively large, several screen-
ing approaches may be used to reduce the number of candidate conﬁgurations that need to
be evaluated. It should be emphasized, however, that these approaches are heuristic and
therefore do not guarantee that the optimal solution will be retained. Nevertheless, they
can substantially reduce the computational eﬀort while often yielding solutions with only a
small increase in RSS. Examples illustrating the following screening methods are presented
in Section 5.1.

   • If the number of generating subsets r is large relative to k, we may restrict the search
     to conﬁgurations containing at most one subarchetype pergenerating subset. Although
     this reduces the number of candidate conﬁgurations to kr , the asymptotic complexity
     remains O(rk ) for ﬁxed k.
   • Retain only those generating subsets containing observations that contribute to the
     classical archetypes or correspond to the classical archetypoids. More generally, addi-
     tional conﬁgurations involving subsets associated with solutions having a low RSS in
     the classical archetypal analysis may also be retained, whereas conﬁgurations associated
     with high RSS values may be discarded.
   • Compute archetypoids using the midpoints of the generating subsets and retain conﬁg-
     urations involving those subsets whose midpoints are selected as archetypoids. When


                                                12
        seeking eﬃcient subarchetypes, where the generating subsets are maximal friends sets
        (i.e., the vertex sets of the facets of the eﬃcient frontier), conﬁgurations involving ad-
        jacent facets (namely, facets sharing two or more vertices) may also be considered.
        The archetypoid analysis may be performed by considering only the midpoints or by
        considering both the midpoints and the observations (vertices). In the latter case, a
        partitioned subarchetypoid analysis can be applied to the combined set of midpoints
        and observations, while constraining the subarchetypoids to be selected from the set of
        midpoints.
    In practice, combining several of these strategies often yields substantial reductions in
computational eﬀort with only a small increase in the resulting RSS.
    Finally, although not strictly a screening strategy, it is worth mentioning a practical
technique that can drastically reduce the number of evaluated conﬁgurations when comput-
ing eﬃcient subarchetypes within partition elements. As discussed in Section 3.3, although
archetypes computed from eﬃcient DMUs may be ineﬃcient, this situation is relatively un-
common in practice. Consequently, it is often suﬃcient to introduce the corresponding max-
imal friends sets as generating subsets only for those partition elements whose subarchetypes
are found to be ineﬃcient, while leaving the remaining partition elements undivided. If the
resulting subarchetypes are then eﬃcient in all partition elements, there is no need to fur-
ther reﬁne the remaining partition elements, since doing so would only impose additional
constraints and therefore cannot decrease the minimum attainable RSS.
    An application of this strategy is presented in Section 5.1.2. In that example, only one
partition element produces an ineﬃcient subarchetype. In this case, it is suﬃcient to evalu-
ate only the six candidate conﬁgurations associated with the six maximal friends sets of that
partition element for all resulting subarchetypes to be eﬃcient. In contrast, introducing the
maximal friends sets as generating subsets in every partition element would require evaluat-
ing 23 760 candidate conﬁgurations. This illustrates the substantial computational savings
that can be achieved when only a small number of partition elements contain ineﬃcient
subarchetypes.


5       Results and discussion
5.1      Motivating applications: eﬃcient subarchetypes
In this section, we introduce the application that motivates subAA, namely the computation
of eﬃcient subarchetypes within the framework of DEA (see Section 3.3). It is worth em-
phasizing that, in this application, the constraints imposed on the subarchetypes arise from
the intrinsic geometric structure of the eﬃcient frontier rather than from external expert
knowledge.

5.1.1     Eﬃcient subarchetypes in business data
To illustrate the proposed methodology, we consider a dataset of 55 decision-making units
(DMUs) corresponding to commercial ﬁrms from the Valencian Community, recovered from
the SABI ﬁnancial database SABI (2025). The ﬁrms are medium-sized (employing between
50 and 200 workers) and operated in the wholesale and retail trade sector (Sector G) during
2022. The input variables considered are “Total Assets”, “Staﬀ Costs”, and “Other Costs”,
while “Operating Revenues” is treated as the output variable. Within this framework, the
“Number of Employees” is regarded as a non-controllable variable. After conducting DEA
under constant returns to scale (CRS), 12 DMUs were found to be eﬃcient. Note that we
assume CRS because any proportional multiple of a feasible activity can also be considered
feasible.
    Our goal is to ﬁnd eﬃcient subarchetypes from these 12 eﬃcient DMUs. The problem is
that the implementation of subAA requires the assumption of variable returns to scale (VRS).

                                                13
However, by virtue of the Theorem of Equivalence for Ratio Variables (Bolós et al., 2026),
the above eﬃciency analysis under CRS is equivalent to an eﬃciency analysis under VRS but
expressing all variables as ratios with respect to the non-controllable variable. Speciﬁcally,
each input and output is normalized by the “Number of Employees”, thereby allowing the
assumption of VRS while preserving the underlying eﬃciency analysis.
    Moreover, to ensure that all variables contribute with comparable relative importance
in the computation of archetypes, each ratio variable was normalized by dividing it by its
maximum value. This normalization does not aﬀect the eﬃciency status of the DMUs, as
eﬃciency is invariant to changes
                              √     in the units of measurement. Subsequently, the output
variable was multiplied by 3 to compensate for the imbalance between the number of
inputs and outputs. Speciﬁcally, this adjustment prevents the RSS used in the computation
of archetypes from disproportionately emphasizing the inputs relative to the output, given
that the model includes three inputs and only one output. The resulting normalized dataset
is presented in Table 1.

                       DMU        Input 1    Input 2    Input 3    Output
                       1            0.419      0.581      0.926     1.665
                       2            1.000      1.000      0.792     1.622
                       3            0.336      0.447      1.000     1.732
                       4            0.152      0.616      0.839     1.502
                       5            0.099      0.326      0.101     0.271
                       6            0.429      0.643      0.261     0.657
                       7            0.352      0.388      0.385     0.809
                       8            0.354      0.653      0.391     0.897
                       9            0.064      0.651      0.170     0.380
                       10           0.048      0.456      0.255     0.511
                       11           0.220      0.688      0.157     0.422
                       12           0.141      0.289      0.063     0.183

Table 1: Inputs and output considered in the example. All of them are ratio variables,
dividing “Total Assets”, “Staﬀ Costs”, “Other Costs” and “Operating Revenues” by the
“Number of Employees”.√Moreover, each variable has been divided by its maximum, and the
output is multiplied by 3 to compensate with respect to the inputs.

    Before computing the eﬃcient subarchetypes, we ﬁrst calculate the classical archetypes to
illustrate that the resulting archetypes are not necessarily eﬃcient. A good choice, according
to the elbow-type criterion, is to compute k = 3 archetypes. The archetypes obtained are
DMU2 , 0.796 · DMU3 + 0.204 · DMU4 , and 0.375 · DMU9 + 0.625 · DMU12 with RSS = 0.0172
(see Table 3). The ﬁrst two archetypes are eﬃcient, but the third is ineﬃcient with an
ineﬃciency score of 0.935, computed by the input-oriented radial BCC model (values below
1 indicate ineﬃciency) (Banker et al., 1984). Note that DMU9 and DMU12 do not appear
together on any facet, see Table 2.

          Facet   1   2   3   4     5    6    7     8   9   10    11   12   13   14   15
                  1   1   1   2     3    3    3     3   4    4     5    5    5    5    5
                  2   2   3   3     4    4    4     5   5    5     6    6    6    8    8
         DMUs
                  3   4   4   7     5    5    7     7   7    8     7    8   11    9    9
                  8   8   8   8     7   10    8    12   8   10     8   11   12   10   11

Table 2: Facets of the eﬃcient frontier and their corresponding vertex DMUs. Each facet is
deﬁned by four vertex DMUs, which constitute a maximal friends set.

   Using the maximal friends sets reported in Table 2 as generating subsets, the eﬃcient

                                                  14
subarchetypes are DMU2 , 0.801 · DMU3 + 0.199 · DMU4 , and 0.716 · DMU5 + 0.284 · DMU9 ,
with an RSS of 0.0186 (see Table 3). All of them are in at least one facet and hence, they
are eﬃcient. Speciﬁcally, the ﬁrst eﬃcient subarchetype is in facets 1, 2, and 3; the second
eﬃcient subarchetype is in facets 3, 5, 6, and 7; and the third eﬃcient subarchetype is in
facets 14 and 15. As can be seen in Table 3, the eﬃcient subarchetypes closely resemble the
archetypes, while achieving only a slightly higher RSS.
    In the above computation of eﬃcient subarchetypes, all 680 candidate conﬁgurations were
considered. Although this does not pose a computational challenge in the present example,
the number of candidate conﬁgurations may become computationally intractable in more
general settings. Several methods for screening candidate conﬁgurations can be employed to
alleviate this issue (see Section 4.4). A simple way to reduce the computational burden is to
limit the maximum number of subarchetypes per facet to one, which reduces the number of
candidate conﬁgurations from 680 to 455.
    Another of the proposed screening methods requires ﬁrst computing the archetypoids,
motivated by the fact that they tend to be the main contributors to the construction of the
eﬃcient subarchetypes. Computing k = 3 archetypoids yields DMU2 , DMU3 , and DMU5 ,
with RSS = 0.0240 (see Table 3). Thus, we can select candidate conﬁgurations involving
facets that contain these DMUs. In this case, however, this screening criterion is not eﬀective,
since every facet contains at least one of DMU2 , DMU3 , and DMU5 .
    On the other hand, the observations contributing to the archetypes are DMU2 , DMU3 ,
DMU4 , DMU9 , and DMU12 . In this case, two facets do not have any of these DMUs as
vertices. Discarding these facets reduces the number of candidate conﬁgurations to 455. If,
in addition, we impose that each facet generates at most one subarchetype, the number of
candidate conﬁgurations is further reduced to 286.

                                                      Input 1    Input 2   Input 3    Output
   Archetypes      DMU2                                 1.000      1.000     0.792     1.622
                   0.796 · DMU3 + 0.204 · DMU4          0.298      0.482     0.967     1.685
 RSS = 0.0172      0.375 · DMU9 + 0.625 · DMU12         0.112      0.425     0.103     0.257
   Eﬃcient         DMU2                                 1.000      1.000     0.792     1.622
 Subarchetypes     0.801 · DMU3 + 0.199 · DMU4          0.299      0.481     0.968     1.686
 RSS = 0.0186      0.716 · DMU5 + 0.284 · DMU9          0.089      0.418     0.121     0.301
 Archetypoids      DMU2                                 1.000      1.000     0.792     1.622
                   DMU3                                 0.336      0.447     1.000     1.732
  RSS = 0.0240     DMU5                                 0.099      0.326     0.101     0.271

Table 3: Results of computing three archetypes, three eﬃcient subarchetypes, and three
archetypoids, together with a comparison of their goodness of ﬁt and the coordinates of the
obtained representatives.

    A further screening method proposed in Section 4.4 consists of taking the “mean activity”
(midpoint) of each facet and performing an archetypoid computation. In this case, the
archetypoids correspond to the mean activities of facets 1, 6, and 13.
    However, it is also advisable to take the observations into account when identifying the
archetypoids among the set of mean activities. To this end, we perform partitioned archety-
poid analysis on the union of the mean activities and the observations, using two partition
elements: P1 , consisting of the mean activities, and P2 , consisting of the observations. The
partitioned archetypoids are constrained to be selected from P1 . In this case, a similar result
is obtained, with the selected mean activities corresponding to facets 1, 3, and 13.
    It can be observed that the ﬁrst eﬃcient subarchetype lies on facets 1 and 3, and the
second on facets 3 and 6. Although the third eﬃcient subarchetype does not lie on facet
13, it lies on facet 15, which is adjacent to facet 13 (i.e., the two facets share at least two
vertices). These results suggest that ﬁltering candidate conﬁgurations using archetypoids

                                              15
computed from the mean activities of the facets can be an eﬀective strategy.
    Restricting the candidate conﬁgurations to those involving facets 1, 3, or 13, or facets
adjacent to them, eliminates only facet 14. This results in 580 candidate conﬁgurations, or
364 when the maximum number of subarchetypes per facet is restricted to 1. We may instead
focus on conﬁgurations containing facets 1, 3, or 13. However, this still leaves a large number
of candidate conﬁgurations. A more restrictive criterion is to consider the combination of
facets 1, 3, and 13 and allow at most one of these facets to be replaced by an adjacent
facet, while leaving the remaining facets unchanged. This reduces the number of candidate
conﬁgurations to 17, among which is the combination with the minimum RSS (facets 1, 3,
and 15).
    Nevertheless, if a suﬃciently good solution is acceptable, even if it is not the optimal one,
the conﬁguration formed by facets 1, 3, and 13 is the one to select. In this case, restricting the
subarchetypes to the combination of facets 1, 3, and 13 yields an RSS of 0.0193, which may
be regarded as satisfactory, since it is close to the minimum value of 0.0186. Moreover, using
the combination of facets 1, 6, and 13 yields exactly the same solution as the combination of
facets 1, 3, and 13, resulting in identical subarchetypes.

5.1.2   Partitioned eﬃcient subarchetypes in basketball
In this example, our aim is to identify the ideal eﬃcient archetypal basketball player for
each position. To this end, we compute partitioned subarchetypes from the set of eﬃcient
players in each position, with the partition deﬁned according to player position. Within each
partition element, the corresponding maximal friends sets are used as generating subsets to
ensure that the resulting archetypal players are eﬃcient with respect to players in the same
position. The analysis is based on data for all NBA players from the 2025–26 NBA regular
season, obtained from Basketball-Reference.com (2026).
    The outputs considered are the totals of oﬀensive rebounds (ORB), defensive rebounds
(DRB), assists (AST), steals (STL), and points (PTS), while the input is minutes played
(MP). In addition, only players with at least 30 games played and averaged at least 10
minutes per game are included in the analysis (the same sample selection as made by Lutz
(2012); Vinué and Epifanio (2017)), i.e. 428 players in total. Since MP is a non-controllable
variable, the Theorem of Equivalence for Ratio Variables (Bolós et al., 2026) allows us to
assume VRS by replacing the original volume variables with the corresponding output-to-
MP ratios together with a single input consisting entirely of ones.
    There are ﬁve diﬀerent positions: center (C), power forward (PF), point guard (PG), small
forward (SF), and shooting guard (SG). After performing DEA separately for each position
(applying a radial output-oriented model under VRS), we construct a dataset consisting of
the 53 players identiﬁed as eﬃcient in their respective positions: 8 C, 10 PF, 13 PG, 8 SF,
and 14 SG.
    To perform archetypal analysis on the outputs, we normalize each variable by dividing
it by its maximum value and multiplying the result by 100, thereby expressing all variables
as percentages. Since this is merely a linear rescaling, the original values can be recovered
at any stage using the maximum values of the ratio variables: 0.214 (ORB), 0.325 (DRB),
0.308 (AST), 0.125 (STL), and 0.956 (PTS). As in the previous example, this rescaling does
not aﬀect the DEA results. With ﬁve player positions, we set k = 5 for all analyses.
    If we compute ﬁve archetypes without considering player positions, the resulting archety-
pal proﬁles combine players from diﬀerent positions and are therefore not suitable for charac-
terizing players in a speciﬁc position. The resulting RSS of 300.7 constitutes a lower bound
for the RSS achievable by the subarchetypal analyses considered below, since the subset
constraints can only reduce the feasible solution space.
    On the other hand, if we deﬁne a partition P according to player position and compute one
archetype within each partition element independently (group-wise archetypes), we obtain the
centroids of the corresponding partition elements. Although this produces a diﬀerent proﬁle



                                               16
for each position, each proﬁle is computed independently from the others, taking into account
only the players in the corresponding position. As a consequence, the resulting proﬁles are
very similar in some variables, such as STL and PTS, and therefore do not adequately capture
the diﬀerences between playing positions (see Table 4, Group-wise archetypes). Moreover,
they are not eﬃcient, with ineﬃciency scores of 1.03 (C), 1.07 (PF), 1.06 (PG), 1.04 (SF),
and 1.05 (SG), computed using the output-oriented radial BCC model (values greater than
1 indicate ineﬃciency) (Banker et al., 1984). Although these values are close to 1, they still
indicate that the centroid proﬁles are ineﬃcient.

                Group-wise archetypes                   Group-wise eﬃcient subarchetypes
        ORB      DRB AST        STL PTS                 ORB DRB AST           STL PTS
  C      61.5     78.3 40.1     35.2 57.5           C    62.2  79.8 40.2      37.7 58.0
 PF      34.0     54.3 37.1     32.6 48.8          PF    34.0  54.0 37.3      36.7 49.7
 PG      19.1     42.4 67.2     41.8 57.3          PG    22.8  43.2 68.9      44.0 58.4
 SF      25.8     50.8 50.9     35.8 66.1          SF    28.3  51.7 51.6      36.9 67.4
 SG      20.8     40.2 45.3     42.7 49.8          SG    21.1  43.5 46.4      44.5 50.8

                Partitioned archetypes                  Partitioned eﬃcient subarchetypes
        ORB      DRB AST         STL PTS                ORB DRB AST            STL PTS
  C      90.7     75.9 17.0      33.2 32.1          C    90.2   76.2 17.1      32.7 31.9
 PF      16.6     52.2 59.2      28.1 31.7         PF    13.7   52.7 65.4      26.1 31.9
 PG      13.2     47.5 94.4      32.2 70.1         PG    12.7   45.1 94.6      33.0 71.8
 SF      15.5     51.6 46.8      26.8 87.8         SF    15.5   51.6 46.9      26.5 87.7
 SG      16.5     26.9 18.3 100.0 37.9             SG    16.5   26.9 18.3 100.0 37.9

Table 4: Comparison of the proﬁles obtained for diﬀerent player positions using four archety-
pal analysis approaches: group-wise archetypes, group-wise eﬃcient subarchetypes, parti-
tioned archetypes, and partitioned eﬃcient subarchetypes. All values are expressed as ratios
per minute played (MP) and normalized as percentages of the maximum value of the corre-
sponding variable.

    To obtain eﬃcient group-wise archetypes, we compute group-wise eﬃcient subarchetypes.
Speciﬁcally, within each partition element, we take the corresponding maximal friends sets
as generating subsets, namely 4 for C, 6 for PF, 11 for PG, 5 for SF, and 18 for SG, and com-
pute one eﬃcient subarchetype independently of the other partition elements. The resulting
proﬁles are very similar to the group-wise archetypes, while guaranteeing eﬃciency in every
position (see Table 4 Group-wise eﬃcient subarchetypes). However, as in the previous case,
each position is analysed independently, without taking into account the players in the other
positions. Consequently, the resulting proﬁles also fail to adequately capture the diﬀerences
between playing positions, particularly in variables such as STL and PTS.
    If we compute partitioned archetypes with respect to P, we obtain an RSS of 364.7. Com-
pared with the previous group-wise proﬁles, partitioned archetypes yield extreme proﬁles that
better characterize the distinctive features of each playing position, since they are computed
by jointly considering players from all positions. As a consequence, the resulting proﬁles are,
in a sense, complementary to one another and are therefore more suitable for representing a
balanced basketball team (see Table 4, Partitioned archetypes). However, the PF proﬁle re-
sults ineﬃcient, with an ineﬃciency score of 1.04, computed using the output-oriented radial
BCC model.
    To overcome this ineﬃciency, we use the maximal friends sets associated with the eﬃcient
frontier of each position as generating subsets within the corresponding partition elements,
and partitioned subarchetypes are computed. Consequently, the resulting archetypal players
are guaranteed to be eﬃcient with respect to players in their respective positions. These
proﬁles will be referred to as partitioned eﬃcient subarchetypes (see Table 4, Partitioned


                                              17
eﬃcient subarchetypes).
    The partitioned eﬃcient subarchetypes yield an RSS of 364.9, which is only slightly larger
than that of the partitioned archetypes. Moreover, the resulting proﬁles are remarkably
similar, with only subtle diﬀerences (mainly in the PF proﬁle) that are suﬃcient to guarantee
eﬃciency in every position. Overall, this example illustrates that enforcing eﬃciency has only
a limited impact on the RSS while guaranteeing that each proﬁle lies on the corresponding
eﬃcient frontier.
    Finally, it is worth noting that, in this example, it was not necessary to compute par-
titioned eﬃcient subarchetypes for all 23 760 candidate conﬁgurations. Since only the PF
archetypal proﬁle was ineﬃcient, we considered the maximal friends sets as generating subsets
only within the PF partition element. For the remaining positions, the corresponding parti-
tion elements were left undivided and therefore acted as single generating subsets. This was
suﬃcient to obtain eﬃcient proﬁles while requiring the evaluation of only six candidate con-
ﬁgurations, corresponding to the six facets of the PF eﬃcient frontier. This illustrates that,
in practice, it is often suﬃcient to reﬁne only those partition elements whose subarchetypes
are ineﬃcient. When only a small number of partition elements contain ineﬃcient proﬁles,
this strategy can substantially reduce the computational eﬀort needed to obtain eﬃcient
subarchetypes.

5.2     Applications in human development
To illustrate the practical utility of subADA, we consider two applications based on pub-
licly available data from Our World in Data (2026). In both cases, countries are grouped
according to the oﬃcial Human Development Index (HDI) (United Nations, 2023) classiﬁca-
tion (Very High, High, Medium, and Low Human Development), and the aim is to identify
archetypal countries while preserving this grouping structure. The ﬁrst application considers
multivariate societal indicators, whereas the second analyses total fertility rate trajectories as
functional data. Together, these examples demonstrate the ﬂexibility of subADA in selecting
representative observations from grouped multivariate and functional datasets.

5.2.1   Societal indicators data
The ﬁrst application considers a multivariate dataset of 166 countries described by four
societal indicators. Countries with complete information for the latest available year of each
variable were retained, resulting in 65 Very High, 38 High, 39 Medium, and 24 Low HDI
countries. The variables are the Human Rights Index (2025) (HRI), Life Expectancy at birth
(2023) (LE), Labour Force Participation Rate (2025) (LP), and Scientiﬁc and Technical
Journal Articles Published per Million People (2022) (SP). All data were obtained from
Our World in Data (2026).
    Because the four indicators are expressed in diﬀerent units and scales, the analysis was
performed using the ranks of each variable rather than their original values. Besides ensur-
ing comparability across variables, this transformation facilitates interpretation, as country
performance in these indicators is often communicated through rankings. If there are tied
values, we assign them the average of the ranks they would have shared.
    Table 5 compares the representatives selected by classical ADA (i.e. without considering
the labels) for k = 4 and subADA by constraining the solution to include one subarchetypoid
from each of the four groups. As expected, ADA achieves a lower reconstruction error
(RSS = 1 125.24) than subADA (RSS = 1 229.74), since it is not constrained by the HDI
grouping. However, ADA selects representatives exclusively from the Very High and Low
HDI categories, leaving the High and Medium HDI groups unrepresented. In contrast, since
subADA selects one representative from each HDI category, it provides a balanced summary
of countries across all levels of human development. In policy applications such as human
development, ensuring that all HDI categories are represented is often more valuable for



                                               18
decision-making than achieving a marginal reduction in reconstruction error by concentrating
the representatives in only a subset of the groups.

                Method      Country    HDI group     HRI    LE     LP    SP
                            Sweden     Very high      2     11     61      7
                            China        High        157    48     62    44
                subADA
                            Angola      Medium       107    142    17    166
                            Djibouti     Low         130    137    165   134
                            Finland    Very high     10.5   25     98     6
                            Qatar      Very high     135    17      1     33
                ADA
                            Djibouti     Low         130    137    165   134
                            Niger        Low         102    157     8    161

Table 5: Representatives selected by subADA (with one subarchetypoid per group) and
classical ADA with k = 4 for societal indicators data. The variables are expressed as ranks,
with tied observations assigned the average of the ranks they would otherwise occupy.

    Table 6 reports the representatives selected when k = 8 using ADA and subADA, with
subADA constrained to select two subarchetypoids from each of the four groups. Again,
ADA attains a lower reconstruction error (RSS = 268.63 versus 329.32 for subADA), but the
resulting allocation is unbalanced, with three representatives from the Very High HDI group,
three from the Low HDI group, two from the High HDI group, and none from the Medium
HDI group. In contrast, as subADA allocates exactly two representatives to each HDI cate-
gory, it ensures a balanced representation of countries across all development levels. These
results illustrate that subADA can preserve meaningful group representation while incurring
only a moderate increase in reconstruction error relative to the unconstrained solution. No-
tably, even when the number of representatives is doubled from four to eight, ADA still fails
to select any representative from the Medium HDI category. In contrast, subADA guarantees
balanced representation across all HDI levels while maintaining a competitive reconstruction
error. This is particularly appealing in policy applications, where expressing each country
as a combination of representatives from all HDI categories provides a more interpretable
description than relying on representatives drawn from only a subset of the development
levels.

5.2.2   Functional data: total fertility rate time series
The second application considers functional data comprising the total fertility rate trajecto-
ries of the same 166 countries analysed in the previous application. The total fertility rate
measures the average number of children that a woman would have if she experienced the age-
speciﬁc fertility rates observed in a given year throughout her reproductive life. The dataset
consists of annual observations from 1950 to 2023 and was obtained from Our World in Data
(2026). As before, the countries are grouped into 65 Very High, 38 High, 39 Medium, and
24 Low HDI countries according to their HDI category.
    All functions were expressed using 32 B-spline basis functions of order 4 (cubic splines)
over the period 1950–2023, with equally spaced knots, following the same basis speciﬁcation
adopted by Epifanio (2016) in a similar application.
    For k = 4, subFADA (with one subarchetypoid per group) selects Serbia, Thailand,
Syria, and Somalia as representatives of the Very High, High, Medium, and Low HDI groups,
respectively (RSS = 8.32). By contrast, classical FADA (without considering labels) achieves
a slightly lower reconstruction error (RSS = 7.04) by selecting Latvia, Singapore, Libya,
and Afghanistan, resulting in two Very High, one High, one Low, and no Medium HDI
representative.


                                             19
        Method      Country                         HDI group   HRI    LE    LP    SP
                    Sweden                          Very high     2     11    61     7
                    Qatar                           Very high   135     17    1     33
                    Iran                              High      151     53   155    43
                    Nicaragua                         High      164     76    48   147
        subADA
                    Nigeria                          Medium      98    166    5    104
                    Sao Tome and Principe            Medium      35    112   166   127
                    Afghanistan                       Low       166    136   161   155
                    Niger                             Low       102    157    8    161
                    Iceland                         Very high   6.5     13   16     8
                    Italy                           Very high    32     6    145    19
                    Qatar                           Very high   135     17    1     33
                    Dominican Republic                High      46.5   85    57    142
        ADA
                    Egypt                             High      152    101   151    67
                    Afghanistan                       Low       166    136   161   155
                    Central African Republic          Low       127    163   18    156
                    Gambia                            Low        42    138   149   115

Table 6: Representatives selected by subADA (with two subarchetypoids per group) and
classical ADA with k = 8 for societal indicators data. The variables are expressed as ranks,
with tied observations assigned the average of the ranks they would otherwise occupy.



    Figure 3 shows the fertility trajectories of the selected representatives. Although FADA
achieves a slightly lower reconstruction error, two of its representatives exhibit patterns
that are similar to those selected by adjacent HDI groups in subFADA. In particular, the
trajectory of Singapore (Very High HDI) closely resembles that of Thailand (High HDI), while
the trajectory of Libya (High HDI) is similar to that of Syria (Medium HDI). Consequently,
FADA allocates two representatives to the Very High HDI group while omitting the Medium
HDI group, whereas subFADA preserves one representative for each development level and
provides a more balanced characterization of fertility dynamics across HDI categories. From
a policy perspective, this is particularly appealing because each country’s fertility trajectory
is interpreted as a combination of representatives from all HDI categories, rather than from
only those groups favoured by the unconstrained optimization.


6    Conclusions
This paper introduces, to the best of our knowledge, the ﬁrst semi-supervised framework for
archetypal analysis. The proposed methodology extends classical AA and ADA by incorpo-
rating constraints into the construction of archetypal proﬁles through subsets of observations.
It further generalizes these frameworks and extends the location result for archetypes given
by Cutler and Breiman (1994). The framework accommodates both user-deﬁned and data-
driven generating subsets, allowing external knowledge or intrinsic structural properties of
the problem to be incorporated into the analysis, as illustrated by the computation of eﬃcient
subarchetypes within the framework of DEA. The methodology has been developed for both
multivariate and functional data, and the corresponding algorithms have been implemented
in the subarchetypes R package.
    The experimental results illustrate the ﬂexibility of the proposed framework across both
user-deﬁned and data-driven settings. In the DEA applications, the methodology provides
a natural way to compute eﬃcient subarchetypes by restricting the admissible subsets to
the vertex sets of the eﬃcient frontier facets, called maximal friends sets. In the human
development applications, the subgroup-constrained approaches produce balanced and in-


                                               20
Figure 3: Fertility rate trajectories of the representatives selected by a) subFADA with one
subarchetypoid per group, and b) classical FADA for k = 4. Colours indicate the HDI groups:
black (Very High), red (High), green (Medium), and blue (Low).


terpretable representatives, ensuring that all predeﬁned groups are represented while jointly
minimizing the global reconstruction error. Comparisons with constrained clustering, group-
wise archetypal analysis, and the classical unconstrained approach further highlight the ad-
vantages of optimizing the global reconstruction error under subset constraints rather than
analysing each group independently or ignoring the available prior information.
    Several directions for future research remain open. An immediate extension concerns the
computation of eﬃcient subarchetypes under alternative DEA technologies, including con-
stant (CRS), non-increasing (NIRS), non-decreasing (NDRS), and generalized (GRS) returns
to scale (Cooper et al., 2007). Since these technologies modify the admissible combinations of
observations through diﬀerent returns-to-scale assumptions, extending the proposed frame-
work would require new optimization procedures.
    Another important line of research is the development of scalable implementations for
large datasets by adapting the computational strategies proposed for scalable AA and ADA
Alcacer et al. (2026). Moreover, an algorithm for computing subarchetypes could be devel-
oped without requiring the exploration of all candidate conﬁgurations, following an approach
similar to that of the current archetypoid algorithm. Starting from an initial conﬁguration,
the algorithm could iteratively move to “nearby” conﬁgurations that improve the RSS until
a suﬃciently good solution is obtained.
    Furthermore, methodological extensions for subarchetypal analysis can be carried out.
These include robust formulations based on alternative loss functions (Moliner and Epifanio,
2019), kernel formulations to capture nonlinear relationships in the data (Mørup and Hansen,
2012), as well as subarchetypal analysis for other data types, including shapes (Epifanio et al.,
2018; Alcacer et al., 2020; Epifanio et al., 2023), binary data (Cabero and Epifanio, 2020),
ordinal data (Fernández et al., 2021), datasets with missing values (Epifanio et al., 2020),
asymmetric dissimilarity data (Vinué and Epifanio, 2017; Alcacer et al., 2025), and extend-
ing to biarchetypes (Alcacer et al., 2024), where subsets of both observations and variables
will be considered. Another promising direction is the incorporation of fairness into sub-
archetypal analysis. While fairness has recently been addressed in AA through constraints
on the representation coeﬃcients (Alcacer and Epifanio, 2025), its integration with subset-
constrained archetypal analysis remains an open research question.
    Finally, we expect the proposed framework to ﬁnd useful applications in many domains


                                               21
where prior structural information is naturally available.


Declaration of generative AI and AI-assisted technologies
in the writing process
During the preparation of this work the authors used OpenAI’s ChatGPT in order to improve
language and readability. After using this tool, the authors reviewed and edited the content
as needed and take full responsibility for the content of the published article.


Acknowledgments
We thank Morten Mørup for his constructive feedback and insightful suggestions.


Funding
This work was partially supported by the Spanish Ministry of Science and Innovation PID2023-
153128NB-I00, PID2022-141699NB-I00 and PID2020-118763GA-I00 and Generalitat Valen-
ciana CIPROM/2023/66.


Declaration of competing interest
The authors have declared that no competing interests exist.


Data and code availability
The package subarchetypes and the scripts with data required to reproduce all experimental
results in Section 5 and Appendix B are available at https://www.uv.es/vbolos/investigacion/subarchetypes.z


A     Proofs
Proof of Proposition 3.2. In each case, the proposed subarchetypes satisfy the subset con-
straints, since each of them can be expressed as a convex combination of observations be-
longing to a common generating subset. It therefore remains to prove their optimality with
respect to the RSS.
  1. k = 1.
      (a) The sample mean x̄ is the unconstrained minimizer of the RSS.
      (b) It is clear that the subarchetype z1 belongs to ∪rp=1 Cp since it belongs to one of
          the sets Cp . Moreover, an optimal subarchetype exists because ∪rp=1 Cp is compact
          and the RSS is continuous.
          Suppose that z1 is an interior point of ∪rp=1 Cp . Let

                                  z(t) = x̄ + t(z1 − x̄),        0 < t < 1,

           and deﬁne                               n
                                                   X
                                       RSS(t) =          kxi − z(t)k2 .
                                                   i=1




                                              22
            Since z1 is an interior point of ∪rp=1 Cp , there exists ε > 0 such that z(t) ∈ ∪rp=1 Cp
            for all 1 − ε < t < 1. Moreover, a direct calculation shows that
                                        RSS(t) = RSS(0) + nt2 kz1 − x̄k2 ,
            and hence RSS(t) is strictly increasing for 0 < t < 1 because z1 6= x̄. Therefore,
            z(t) is feasible and RSS(t) < RSS(1) for all 1 − ε < t < 1, contradicting the
            optimality of z1 .
    2. 1 < k < NS . It is clear that each subarchetype belongs to ∪rp=1 Cp since it belongs to
       one of the sets Cp . Moreover, an optimal set of subarchetypes exists because ∪rp=1 Cp
       is compact and the RSS is continuous.
      Suppose without loss of generality that z1 is an interior point of ∪rp=1 Cp . Let
                                   z(t) = zj + t(z1 − zj ),       t > 1,
      for some j 6= 1, and choose t > 1 such that z(t) ∈ ∂ ∪rp=1 Cp . Such a value of t
      exists because ∪rp=1 Cp is compact and z1 is an interior point. For z1 , . . . , zk ﬁxed,
      RSS is minimized with respect to the coeﬃcients αij by choosing kj=1 αij zj to be the
                                                                              P
      point in the convex hull of {z1 , . . . , zk } closest (in the Euclidean metric) to xi , for all
      i = 1, . . . , n.
      Since the convex hull of {z(t), z2 , . . . , zk } contains the convex hull of {z1 , . . . , zk },
      minimizing the RSS with respect to the coeﬃcients αij over the former cannot yield a
      larger value than minimizing it over the latter. If the new RSS is strictly smaller, we
                                        k
      contradict the optimality of {zj }j=1 . Otherwise, the same minimum is attained with
                                      r
      z(t) lying on the boundary of ∪p=1 Cp . Hence, there always exists an optimal solution
      in which z1 belongs to ∂ ∪rp=1 Cp .
    3. k = NS . We may choose the subarchetypes to be precisely the vertices of CS , that is,
            k                                          k
       {zj }j=1 = BS . Hence, the convex hull of {zj }j=1 is CS , which is the largest feasible
       convex set obtainable under the generating-subset constraints. Therefore, no other
       feasible choice of subarchetypes can generate a larger feasible region, and consequently
       no smaller value of the RSS can be achieved.
                                    n
      Moreover, if ∪rp=1 Sp = {xi }i=1 then every observation belongs to CS . So, each observa-
      tion is represented exactly by a convex combination of the subarchetypes, and therefore
      RSS = 0.


Proof of Proposition 3.3. Every subarchetype of E is a convex combination of DMUs belong-
ing to a generating subset, which is a friends set. Since any convex combination of DMUs
in a friends set is eﬃcient (see Section 2.2.2), every subarchetype of E is eﬃcient. Moreover,
regardless of the returns to scale, any convex combination of DMUs is feasible. Hence, every
subarchetype of E is also feasible.


B      Illustrative comparisons
To illustrate the behaviour of the proposed subAA and subADA, we consider several toy
examples. We compare the new methodologies with three alternative approaches. Firstly,
we consider constrained clustering. Secondly, we compare subADA with a group-wise ADA
approach, which serves as an alternative baseline where archetypoids are estimated inde-
pendently within each generating subset. Thirdly, we compare the proposed subADA with
classical ADA, which ignores group labels. These qualitative examples highlight the concep-
tual diﬀerences between these methods and provide intuition about the eﬀect of incorporating
group information into the archetypal estimation process.

                                                  23
B.1    Constrained clustering versus subAA
To the best of our knowledge, there is no method in the literature that is directly compa-
rable to semi-supervised archetypal analysis. The closest related approaches are found in
constrained clustering (González-Almagro et al., 2025), which are semi-supervised clustering
methods, where partial label information or pairwise constraints are used to guide the parti-
tioning of the data. However, semi-supervised clustering techniques do not retain the convex
geometric structure that characterizes archetypal representations, since they primarily focus
on cluster assignment rather than on learning interpretable extremal representations of the
data space, as in subAA. In other words, whereas constrained clustering focuses on restricting
how observations are assigned to clusters, subAA constrains how archetypal representatives
are constructed.
    If we express k-means in a matrix factorization framework as AA was deﬁned in Sec-
tion 2.1.1, the matrix Zk×m = (α′ α)−1 α′ Xn×m contains the centroids of each of the k
groups that partition the data set, while the constraints are kj=1 αij = 1 with αij ∈ {0, 1}
                                                                 P
for i = 1, . . . , n. In constrained clustering, the restrictions are imposed on the α values.
However, in subAA, the restrictions are not placed on the α values, but on the β values, and
consequently on Zk×m (see Remark 3.1).
    The distinction between these two approaches is illustrated using data from the World
Happiness Report dataset (Helliwell et al., 2019). In this example, we consider two variables,
GDP.per.capita and Healthy.life.expectancy, together with the happiness score, which
ranges from 0 to 10. To provide partial class information, we label 10% of the countries based
on their happiness scores, assigning the 5% with the highest scores to the happy class and
the 5% with the lowest scores to the unhappy class. This strategy ensures a clear distinction
between the two classes while avoiding the arbitrary choice of a threshold for converting the
continuous happiness score into categorical labels (Hand, 2006). The remaining 90% of the
countries are left unlabelled.
    In Figure 4, we visualize the distribution of happy, unhappy and unlabelled countries in
the space deﬁned by the two selected variables. Additionally, the ﬁgure shows the centroids
obtained from constrained k-means (Hiep and Duc, 2016; Wagstaﬀ et al., 2001) and the sub-
archetypes identiﬁed with k = 2, considering as generating subsets the two sets of happy
and unhappy countries and computing one subarchetype per class. These subarchetypes rep-
resent extreme prototypes of the data distribution, corresponding here to Utopia (highest
happiness) and Dystopia (lowest happiness), commonly used in sociology as a benchmark.
In contrast, clustering centroids represent average proﬁles located near the centre of the data
cloud, resulting in less distinctive characteristics.
    Another diﬀerence is that constrained k-means only provides group membership, whereas
subAA expresses each observation as a convex combination of the identiﬁed subarchetypes,
thereby revealing its relative proximity to Utopia and Dystopia. For example, constrained
clustering assigns both a country with GDP per capita and healthy life expectancy values of
0.657 and 0.672, respectively, and another country with corresponding values of 0.204 and
0.390 to the cluster of unhappy countries. Moreover, both countries are equidistant from their
corresponding cluster centroid. Despite this, subAA provides a more informative represen-
tation. Speciﬁcally, the ﬁrst country is expressed as 44% Utopia and 56% Dystopia, whereas
the second is represented as 10% Utopia and 90% Dystopia. Hence, subAA distinguishes
the proﬁles of these two countries, whereas constrained clustering provides the same cluster
assignment for both.
    Furthermore, unlike constrained k-means, subAA allows the user to specify an arbitrary
number of subarchetypes for each group. In contrast, constrained k-means is limited to a
single representative (centroid) per group.




                                              24
                                                             Happy
                                                             Unhappy
                                                             Unlabelled                              A1




                                                 1.0
                                                             Centroids
                                                             Subarchetypes




                                                 0.8
                       Healthy life expectancy

                                                 0.6
                                                 0.4



                                                              A2
                                                 0.2
                                                 0.0




                                                       0.0                   0.5              1.0   1.5

                                                                                   GDP per capita




Figure 4: World Happiness Dataset with centroids of constrained k-means and subarchetypes.



B.2    Group-wise ADA versus subADA
To illustrate the diﬀerence between group-wise ADA and subADA, we consider a simple two-
dimensional toy example. Here, group-wise ADA serves as an alternative baseline in which
archetypoids are estimated separately for each generating subset, with each optimization
minimizing the RSS corresponding exclusively to the observations within that subset.
    The dataset consists of ten observations representing cities from two countries A and B,
described by average annual temperature and annual precipitation. A partition P = {Pp }2p=1
is deﬁned, where P1 contains cities from country A and P2 contains cities from country B.
The two countries partially overlap in the feature space, with one city from each country
sharing the same coordinates (15, 700). We compare the representatives selected by applying
ADA independently within each country (and two archetypoids per country) with those
obtained by subADA using P1 and P2 as the generating subsets (and two subarchetypoids
per subset).
    Figure 5 compares the representatives selected by the two approaches. Because two coun-
tries overlap in the feature space, group-wise ADA selects two archetypoids located at the
same point, leading to redundant representatives. By jointly minimizing the global recon-
struction error while enforcing two archetypoids per country, subADA avoids this redundancy
and selects a more informative set of representatives that better captures the overall distri-
bution of the data.
    The advantage of subADA is even more apparent when only one representative is selected
per country. While group-wise ADA independently selects the medoid of each country, lo-
cated at (10, 950) and (18, 560), subADA selects the cities at (5, 1200) and (24, 300), which
represent the two extremes of the complete dataset. As a result, subADA achieves a more
informative representation of the global data structure, whereas the group-wise solution is
optimal only within each individual country.

B.3    ADA versus subADA
To illustrate the diﬀerences between classical ADA (without considering groups) and sub-
ADA, we consider a simple two-dimensional toy example (see Figure 6). The dataset consists
of ten observations representing cities from two countries, described by two variables: aver-
age annual temperature and annual precipitation. As in the previous example, a partition

                                                                                     25
                   Annual precipitation (mm)
                                               1000                                            Country
                                                                                                    A
                                                                                                    B

                                               750

                                                                                               Method
                                                                                                    Group−wise ADA
                                               500                                                  subADA




                                                      5         10       15         20
                                                          Average annual temperature (°C)


Figure 5: Toy example illustrating the diﬀerence between group-wise ADA and subADA.
Two cities, one from each country, share the same coordinates. They are displayed with a
slight oﬀset for visualization purposes.



P = {Pp }2p=1 is deﬁned, where P1 contains cities from country A and P2 contains cities
from country B. Country A exhibits substantially greater variability than country B, whose
observations are concentrated within a relatively small region of the feature space.
    We compare the representatives selected by ADA with k = 4 archetypoids, with those
obtained by subADA using P1 and P2 as the generating subsets (and two subarchetypoids per
subset). This example demonstrates that, although both approaches use the same number
of representatives, the global solution given by ADA tends to allocate more archetypoids to
the more heterogeneous country, whereas the subgroup-based approach given by subADA
guarantees balanced representation of both countries while still capturing within-group vari-
ability.
                                               1250
                   Annual precipitation (mm)




                                               1000
                                                                                                        Country
                                                                                                             A
                                                                                                             B
                                               750


                                                                                                        Method
                                               500                                                           ADA
                                                                                                             subADA


                                               250


                                                               10              20              30
                                                             Average annual temperature (°C)


       Figure 6: Toy example illustrating the diﬀerence between ADA and subADA.



References
A. Alcacer and I. Epifanio. Incorporating fairness constraints into archetypal analysis, 2025.
  URL https://arxiv.org/abs/2507.12021.


                                                                              26
A. Alcacer, I. Epifanio, M. V. Ibáñez, A. Simó, and A. Ballester. A data-driven classiﬁcation
  of 3D foot types by archetypal shapes based on landmarks. PLoS One, 15(1):e0228016,
  2020.
A. Alcacer, I. Epifanio, and X. Gual-Arnau. Biarchetype analysis: Simultaneous learning of
  observations and features based on extremes. IEEE Transactions on Pattern Analysis and
  Machine Intelligence, 46(12):8228–8239, 2024.
A. Alcacer, R. Benı́tez, V. J. Bolós, and I. Epifanio. Multidimensional scaling of two-mode
  three-way asymmetric dissimilarities: ﬁnding archetypal proﬁles and clustering, 2025. URL
  https://arxiv.org/abs/2511.15813.
A. Alcacer, I. Epifanio, S. Mair, and M. Mørup. A survey on archetypal analysis. IEEE
  Transactions on Pattern Analysis and Machine Intelligence, pages 1–20, 2026. doi: 10.
  1109/TPAMI.2026.3740133.
R. D. Banker, A. Charnes, and W. W. Cooper. Some models for estimating technical and
  scale ineﬃciencies in data envelopment analysis. Management Science, 30(9):1078–1092,
  1984. doi: 10.1287/mnsc.30.9.1078.
Basketball-Reference.com. 2025–26 NBA Totals. https://www.basketball-reference.com/leagues/NBA_2026_t
  2026. Accessed: 2026-08-02.
V. J. Bolós, R. Benı́tez, and V. Coll-Serrano. deaR: Conventional and fuzzy DEA models
  with R. SoftwareX, 31:102266, 1–6, 2025. doi: 10.1016/j.softx.2025.102266.
V. J. Bolós, V. J. España, R. Benı́tez, and V. Coll-Serrano. On the suitability of ratio
  variables in data envelopment analysis: An application to education with methodological
  extensions, 2026. URL https://arxiv.org/abs/2607.17193.
I. Cabero and I. Epifanio. Finding archetypal patterns for binary questionnaires. SORT, 44
   (1):39–66, 2020.
A. Charnes, W. W. Cooper, and E. Rhodes. Measuring the eﬃciency of decision making units.
  European Journal of Operational Research, 2(6):429–444, 1978. doi: 10.1016/0377-2217(78)
  90138-8.
W. W. Cooper, L. M. Seiford, and K. Tone. Data Envelopment Analysis. A Comprehen-
 sive Text with Models, Applications, References and DEA-Solver Software. Springer, 2nd
 edition, 2007.
A. Cutler and L. Breiman. Archetypal Analysis. Technometrics, 36(4):338–347, 1994.
I. Epifanio. Functional archetype and archetypoid analysis. Computational Statistics & Data
   Analysis, 104:24 – 34, 2016.
I. Epifanio, M. V. Ibáñez, and A. Simó. Archetypal shapes based on landmarks and extension
   to handle missing data. Advances in Data Analysis and Classiﬁcation, 12(3):705–735, 2018.
I. Epifanio, M. V. Ibáñez, and A. Simó. Archetypal analysis with missing data: see all
   samples by looking at a few based on extreme proﬁles. The American Statistician, 74(2):
   169–183, 2020.
I. Epifanio, V. Gimeno, X. Gual-Arnau, and M. V. Ibáñez-Gual. Archetypal curves in the
   shape and size space: Discovering the salient features of curved big data by representative
   extremes. La Matematica, 2(3):635–658, 2023.
M. J. A. Eugster and F. Leisch. From Spider-man to hero — archetypal analysis in R. Journal
 of Statistical Software, 30(8):1–23, 2009.

                                              27
D. Fernández, I. Epifanio, and L. F. McMillan. Archetypal analysis for ordinal data. Infor-
  mation Sciences, 579:281–292, 2021.
G. González-Almagro, D. Peralta, E. De Poorter, et al. Semi-supervised constrained clus-
  tering: an in-depth overview, ranked taxonomy and future research directions. Artiﬁcial
  Intelligence Review, 58:157, 2025.
D. J. Hand. Classiﬁer technology and the illusion of progress. Statistical Science, 21(1):1–14,
  2006.
J.     F. Helliwell, R. Layard, and J. D. Sachs.                    World happiness re-
     port    2019   dataset.        Available    through     Kaggle,    2019.          URL
     https://www.kaggle.com/datasets/unsdsn/world-happiness.             Dataset accompa-
     nying the World Happiness Report 2019. File used: 2019.csv. Accessed: 2026-07-07.
T. K. Hiep and N. M. Duc. conclust: Pairwise Constraints Clustering, 2016.               URL
  https://CRAN.R-project.org/package=conclust. R package version 1.1.
J. L. Hinrich, S. E. Bardenﬂeth, R. E. Røge, N. W. Churchill, K. H. Madsen, and M. Mørup.
   Archetypal analysis for modeling multisubject fMRI data. IEEE Journal of Selected Topics
   in Signal Processing, 10(7):1160–1171, 2016.
C. Jones, V. Roulet, and Z. Harchaoui. Discriminative clustering with representation learning
  with any ratio of labeled to unlabeled data. Statistics and Computing, 32(1):17, 2022.
T. C. Koopmans. Analysis of production as an eﬃcient combination of activities. In T. C.
  Koopmans, editor, Activity Analysis of Production and Allocation, 13, pages 33–97. Cowles
  Commission for Research in Economics, 1951.
D. Lutz. A cluster analysis of NBA players. In Proceedings of the MIT Sloan Sports Analytics
  Conference, 2012.
J. Moliner and I. Epifanio. Robust multivariate and functional archetypal analysis with
  application to ﬁnancial time series analysis. Physica A: Statistical Mechanics and its Ap-
  plications, 519:195 – 208, 2019.
M. Mørup and L. K. Hansen. Archetypal analysis for machine learning and data mining.
 Neurocomputing, 80:54–63, 2012.
Our World in Data. Our world in data. https://ourworldindata.org, 2026. Accessed: 14
 July 2026.
R Core Team. R: A Language and Environment for Statistical Computing. R Foundation for
  Statistical Computing, Vienna, Austria, 2026. URL https://www.R-project.org/.
SABI.        Información ﬁnanciera de      empresas españolas              y   portuguesas.
  https://sabi.bvdinfo.com, 2025. Accessed 2025-05-15.
K. Tone. Variations on the theme of slacks-based measure of eﬃciency in DEA. European
  Journal of Operational Research, 200(3):901–907, 2010.
United Nations. Human development index.           https://hdr.undp.org/data-center/human-
 development-index, 2023.
J. E. Van Engelen and H. H. Hoos. A survey on semi-supervised learning. Machine learning,
   109(2):373–440, 2020.
G. Vinué and I. Epifanio. Archetypoid analysis for sports analytics. Data Mining and
  Knowledge Discovery, 31(6):1643–1677, 2017.


                                              28
G. Vinué and I. Epifanio. Robust archetypoids for anomaly detection in big functional data.
  Advances in Data Analysis and Classiﬁcation, 15(2):437–462, 2021.
G. Vinué, I. Epifanio, and S. Alemany. Archetypoids: A new approach to deﬁne representative
  archetypal data. Computational Statistics & Data Analysis, 87:102–115, 2015.
K. Wagstaﬀ, C. Cardie, S. Rogers, S. Schrödl, et al. Constrained k-means clustering with
  background knowledge. In Proceedings of 18th International Conference on Machine Learn-
  ing, volume 1, pages 577–584, 2001.




                                            29
