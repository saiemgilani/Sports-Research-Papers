<!-- source: library/preprints/arXiv/2026/2026 - Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection - Masillo et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.24801 -->
<!-- authors: Emanuele Masillo, Eva Pigi Viltanioti, Nina Deliu, Brunero Liseo -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-19; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection

                                               BAYESIAN C OMPUTATION OF C OPULA - BASED M ULTIVARIATE
                                                 M ODELS WITH AN A PPLICATION TO D OPING D ETECTION


                                                            Emanuele Masillo                                        Eva Pigi Vyltanioti
                                                  MEMOTEF, Sapienza Università di Roma (IT)                MEMOTEF, Sapienza Università di Roma (IT)
                                                     emanuele.masillo@uniroma1.it                                AUEB University of Athens
arXiv:2611.24801v1 [stat.CO] 18 Nov 2026




                                                                                                             pigieva.vyltanioti@uniroma1.it

                                                                      Nina Deliu                                           Brunero Liseo
                                                  MEMOTEF, Sapienza Università di Roma (IT)                    MEMOTEF, Sapienza Università di Roma (IT)
                                               MRC – Biostatistics Unit, University of Cambridge (UK)              brunero.liseo@uniroma1.it
                                                           nina.deliu@uniroma1.it


                                                                                               November 2026

                                                                                                A BSTRACT
                                                    The Athlete Biological Passport (ABP) monitors athletes for doping by comparing their biomarker
                                                    readings against personalized reference ranges. These are estimated via the Bayesian ADAPTIVE
                                                    model, which analyzes biomarkers separately and ignores their dependence. Building on a recently
                                                    proposed copula-based multivariate extension of ADAPTIVE, this paper focuses on its computational
                                                    aspects, introducing a fully joint MCMC algorithm and comparing it with a two-step Bayesian IFM
                                                    estimator. Simulations show the two procedures perform comparably under a correctly specified
                                                    copula, but exhibit a genuine trade-off under misspecification: the Bayesian IFM protects marginal
                                                    inference, while the joint MCMC yields better-calibrated dependence estimates and is markedly faster.
                                                    The two approaches are tested on a dataset containing ABP profiles of elite athletes, provided by
                                                    NADO Italia, and collected as part of the project Enhancing the methodological framework for doping
                                                    detection: from univariate to multivariate testing analysis on Athlete Biological Passport profiles.
                                                    Both approaches achieve consistent classification performance, providing anti-doping organizations
                                                    with two concrete inferential routes for adopting a multivariate ADAPTIVE model, along with
                                                    guidance on the trade-offs between them.

                                           Keywords Anomaly detection · Bayesian hierarchical modeling · Copula models · Highest-density regions · Posterior
                                           predictive density · Reference ranges

                                           1    Introduction
                                           Copula models are flexible tools for representing complex structures of dependence for random vectors. According
                                           to Sklar’s theorem [1], any multidimensional absolutely continuous distribution function can be uniquely represented
                                           as a copula, i.e. a joint cumulative distribution function on the unit hypercube with uniform marginals. The copula
                                           representation captures the dependence structure among the vector components, disentangling it from the marginal
                                           behaviour.
                                           From a statistical perspective, interest is typically focused on estimating the copula parameters, a task complicated
                                           by the dependence on the estimation of the marginal parameters. In the classical (frequentist) framework, this issue
                                           is commonly addressed using the so-called inference functions for margins (IFM) estimator [2]. More in detail, let
                                           Y = (Y1 , · · · , Yd ) be an absolutely continuous random vector with CDF FY (·; θ); following Sklar’s theorem, this can
                                           be represented as                                                                                         
                                                                         FY (y; θ) = C F1 (y (1) ; λ1 ), F2 (y (2) ; λ2 ), . . . , Fd (y (d) ; λd ); ψ ,         (1)
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


where C is a CDF, the parameter vector θ = (λ, ψ) is partitioned into the components associated with the marginals
λ = (λ1 , . . . , λd ) and those characterizing the copula, ψ. The two-step approach of [2] proposes to estimate each
marginal component of λ independently via maximum likelihood estimation (MLE) using only the marginal distributions
of the data, and then the dependence parameter ψ through a profile-likelihood-type approach. This is obtained by
re-expressing Eq. (1) with λ replaced by its conditional MLE, say λ̂ψ . While this approach yields consistent estimates
under general conditions, it is known to generate overly confident interval estimates by neglecting the standard error of
λ̂ψ .
Recently, [3] have proposed a Bayesian version of the IFM approach, similarly modulated through two steps. In the first
step, the marginal parameters λ are estimated in a Bayesian fashion, leading to a chain of posterior draws. In the second
step, for each posterior draw of the marginal parameters, posterior samples are also obtained for the copula parameter
ψ, fully propagating in this way uncertainty from the marginal to the copula estimation. It is interesting to note how this
approach can be considered a special case of the broader class of modular, or cut, Bayesian inference schemes [4, 5, 6].
The aim of this work is to propose, instead, an alternative to such two-step approaches, following a fully joint Markov
chain Monte Carlo algorithm (joint MCMC), which updates marginal and copula parameters jointly within a single
chain. By simultaneously exploring the λ− and ψ−components of the parameter space, with uncertainty allowed
to flow from and to each of the two components, this approach is expected to provide a more reliable measure of
uncertainty on the final inference. We are specifically interested in evaluating advantages and disadvantages of adopting
such a joint Bayesian approach compared with the Bayesian IFM in [3].
Our methodological contribution is not purely abstract: it is directly motivated by the problem of doping detection in
professional athletes. Doping control, or testing, stands at the cornerstone of anti-doping organizations to uphold the
integrity of clean sports competitions. Since its establishment in 1999, the World Anti-Doping Agency (WADA) has
spearheaded the global campaign to achieve doping-free sports competitions internationally and nationally, with the
support of national governments [7, 8]. In 2009, the Athlete Biological Passport (ABP) was introduced for monitoring
elite athletes in Olympic and Paralympic disciplines that require greater physical effort [9]. The main objective of the
ABP is to monitor the profiles of individual athletes over time with respect to selected biomarkers that are expected to
indirectly unveil the effects of doping. These include markers of the steroid module, which inform about any use of
anabolic androgenic steroids, and markers of the hematological module, which focus on identifying potential substances
used for the enhancement of oxygen transport or delivery. Within the hematological module of the ABP, WADA [8]
identifies two primary markers to detect atypical profiles. These markers, considered the most specific indicators of
blood doping [8], are hemoglobin concentration (Hgb) and the stimulation index OFF-score (OFFs). The latter is a
derived biomarker obtained by combining Hgb √     with the percentage of reticulocytes in blood (RET%) according to
the following formula: OF F s = 10 · Hgb − 60 RET %. If one of these primary markers takes on a value that falls
outside the intra-individual reference range constructed for that athlete at that time, the observation is classified as
atypical, indicating potential doping violations and prompting further investigation.
The methodological framework underlying ABP is called ADAPTIVE [10] and it is based on a Bayesian approach that
combines population and individual data to define personalized, time-updated reference ranges. However, ADAPTIVE
analyzes biomarkers separately, following a univariate approach and without considering their dependence structure. A
few works have investigated a multivariate extension to the problem, including [11] and [3]. While in [11] a multivariate
Gaussian model is investigated, [3] propose a more flexible model, capable of separately representing marginal
distributions and dependence structure via copulas [12]. This approach allows us to capture complex dependencies not
adequately described by multivariate Gaussian models. Furthermore, the method in [3] extends traditional univariate
reference ranges to multivariate highest-predictive regions (HPRs), addressing the challenges of multidimensional data
with complex structures. Such predictive reference regions account for previous historical readings of each individual
athlete in order to provide tailored tolerances that might flag for potential anomalies. Their construction is based on the
work of [13] and recent developments proposed by [14]. This paper builds on the same copula-based model and HPR
approach proposed in [3], contributing from a computational perspective with the proposal of a joint posterior sampling
scheme and an in-depth comparison to the Bayesian IFM.
The methodological developments of this work are then applied in our motivating application, using data consisting of
original ABP profiles collected by the National Anti-Doping Organisation Italy (NADO Italia). Data consider both
in-competition and out-of-competition samples, from national- and international-level athletes competing in various
sports disciplines. Only samples from athletes who provided explicit consent to the use of their personal data for
this specific research purpose are included. All data have been appropriately anonymized in compliance with privacy
disclosure requirements.
The remainder of this manuscript is structured as follows. In Section 2, we briefly formalize the doping-detection
problem within a statistical framework and review WADA’s state-of-the-art implementation. Focusing on the hemato-



                                                            2
        Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


logical module and its two primary markers, in Section 2.2.1 we describe our multivariate model, where the potential
dependence among biomarkers is explicitly accounted for using a copula representation. Section 3 is the core of this
paper, where we discuss in detail the Bayesian IFM approach (see Section 3.1) and then introduce, in Section 3.2, the
joint MCMC algorithm for producing a posterior sample for the two sets of parameters θ = (λ, ψ). The two approaches
are empirically compared both in terms of simulations (Section 4) and an application to the dataset provided by NADO
Italia (Section 5). These consist of n = 223 observations for a cohort of 23 elite athletes, including information on sport
and discipline, age, sex, altitude exposure, in- or out-of-competition status, and biomarker measurements. Section 6
presents conclusions and future research directions.

2     Problem formulation and existing approaches
In this section, we will briefly describe the problem of identifying anomalous behavior in the analysis of data from ABP
registers and formalize it from a statistical point of view.
The methods currently in use and some recent proposals appearing in the literature will be described.

2.1   State-of-the-art: the univariate ADAPTIVE
                                                                                                             (ℓ)
Consider n athletes indexed by i; for each athlete, ti repeated measurements are available. Let Yi,j ∈ R denote the
outcome of the bio-marker ℓ measured on subject i on occasion j (i = 1, . . . , n; j = 1, . . . , ti ). To accommodate
the problem of interest, we assume that the outcome is represented by the two continuous primary markers of the
ABP hematological module, with ℓ ∈ {Hgb, OFFs}. An athlete i may be flagged as suspected if the analysis of
                                                                  Hgb        OFFs
a new blood sample of these two markers, say Yi,ti +1 = (Yi,t       i +1
                                                                         , Yi,ti +1
                                                                                    ) reveals an atypical finding relative to
the historical readings Yi,ti = (Yi,1 , . . . , Yi,ti ). Often, Yi,j is accompanied by p ≥ 1 explanatory variables
            (1)        (p)
Xi,j = [Xi,j , . . . , Xi,j ]′ ; they represent potentially useful information known to influence Yi,j . In the hematological
case, for example, the analysis of elite athletes includes gender, age, ethnic origin, the altitude at which the competition
is scheduled, and sport discipline [15].
Given the historical path Yi,ti ∈ R2×ti and Xi,j ∈ Rp , the general problem is to provide a probabilistic framework
                                                                                       
to estimate the conditional probability distribution, say p yi,ti +1 |yi,t , xi,ti +1 , of a new test Yi,ti +1 ∈ R2 . This
                                                                              i
can then be used, combined with a decision rule, to define for each athlete a tolerance region of values for Yi,ti +1 :
for example, if a future observed reading yi,ti +1 falls outside a (1 − α)% percentile region, where α ∈ (0, 1) is a
predefined miscoverage level, then yi,ti +1 is considered atypical and athlete i may be excluded from the competition.
Note that this setting illustrates WADA’s paradigm of a no-start decision rule based on a future single measurement
Yi,ti +1 rather than the full sequence (Yi,1 , . . . , Yi,ti +1 ). The former will be the focus of this work, and we refer to
Section 2.2 of [16] for the complete sequence testing paradigm.
A Bayesian predictive technique has been introduced in [10] in order to quantify the chance of doping through the
use of a hierarchical linear model,
                                    where both intra- and inter-individual variability are accounted for. In that paper,
the conditional distribution p yi,ti +1 |yi,t , xi,ti +1 is obtained using a parametric Bayesian model where the prior
                                              i
distribution on the unknown model parameters is calibrated based on the information available on that portion of the
population most similar to athletes, i.e., "healthy" and young, and the updating step is performed using the continuously
observed individual data. In particular, a hierarchical model is considered separately for each primary biomarker ℓ,
assuming that: conditionally on the parameters, (i) an athlete’s readings j ≥ 1 are independent over time; (ii) outcomes
are independent across athletes i = 1, . . . , n. Also, for i = 1, . . . , n, the following assumptions are made for the
within-subject (intra-individual variability and the between-subject quantities:
                                              (ℓ)     (ℓ)      ind       (ℓ)
                                          Yi,j |µi , σ (ℓ) ∼ N (µi , σ (ℓ) ),             j≥1
                                           (ℓ)
                                          µi |µ̄(ℓ) , τ̄ (ℓ) ∼ N (µ̄(ℓ) , τ̄ (ℓ) )
                                           (ℓ) (ℓ)       (ℓ)               (ℓ)     (ℓ)
                                          σ     |ϕ̄     , ψ̄   ∼ LogN (ϕ̄      , ψ̄      ),
where N and LogN denote the Gaussian and the Log-Normal distributions, respectively. In the previous expressions,
                      (ℓ)
the individual mean µi and standard deviation σ (ℓ) are random and they are assumed to have a common distribution
with hyperparameters µ̄(ℓ) , τ̄ (ℓ) and ϕ̄(ℓ) , ψ̄ (ℓ) , respectively. These latter quantities are assumed to be known and are
selected based on historical information that can depend on the specific characteristics         of an athlete i.After collecting
                                                                                             (ℓ)
a series of reading ti for subject i, the (univariate) conditional distribution p yi,ti +1 |y (ℓ)     i,t
                                                                                                          , xi,ti +1 represents the
                                                                                                      i




                                                                     3
         Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


athlete-centred posterior predictive distribution:
                                                                                
                                                       (ℓ)
                                                    p yi,ti +1 |y (ℓ)
                                                                  i,t
                                                                      , xi,ti +1                                            (2)
                                                                      i


                                             (ℓ)
Notice that while prior knowledge of (µi , σ (ℓ) ) accounts for inter-individual variations only (estimated, e.g., from
                                                                                                      (ℓ)
historical control population data), updates progressively leverage the information from the athlete yi,j , j = 1, . . . , ti i
only (intra-individual variations) to capture his/her unique profile.

2.2     Multivariate ADAPTIVE extensions

2.2.1    A multivariate copula-based approach
Restricting attention, as per our application of interest, to a d = 2-dimensional outcome vector Y = (Y (1) , Y (2) ), we
now consider Sklar’s factorization result presented in Eq. (1). In the presence of a vector of explanatory variables X
(e.g., age, sex, altitude), Eq. (1) can be extended to a conditional copula representation [17]. Throughout, we adopt the
“simplifying assumption” commonly invoked in the vine-copula literature [18], whereby the copula linking Y (1) | X
and Y (2) | X does not itself depend on the specific value of X = x. For a continuous random vector Y this implies:
                         fY |X (y (1) , y (2) | x; θ) = f1|X (y (1) | x; λ1 )f2|X (y (2) | x; λ2 )                          (3)
                                                                  (1)                          (2)
                                                                                                                
                                                    × c F1|X (y           | x; λ1 ), F2|X (y         | x; λ2 ); ψ ,

where θ = (λ1 , λ2 , ψ), fℓ (·; λℓ ) and Fℓ (·; λℓ ) denote the marginal density and CDF of Y (ℓ) , respectively, and c(· ; ψ)
is the copula density, which absorbs the entire dependence structure. Under the “simplifying assumption”, conditioning
on X acts exclusively through the conditional margins. We refer the interested reader to [19], [18], [20], and [21] for a
thorough discussion of the simplifying assumption and its validity.
Compared to the standard multivariate parametric model (e.g., the multivariate ADAPTIVE is Section 2.2), this
representation has the key advantage of flexibly decoupling the marginal behavior of each biomarker from their
joint dependence structure. This considerably empowers model specification, since a wide range of parametric
or semiparametric families can be entertained for each margin independently, while possibly simplifying posterior
computation, as discussed in Section 3.1.
Using Eq. (3), we now generalize the Bayesian ADAPTIVE model described in Section 2.1 to a flexible multivariate
version as
                                        (ℓ)                 ind
                                     Yi,j | β (ℓ) , η (ℓ) ∼ D(ℓ) X′i,j β (ℓ) , η (ℓ) ,
                                                                                    

                                    β (ℓ) | β̄ (ℓ) , Σ̄β(ℓ) ∼ Np β̄ (ℓ) , Σ̄β(ℓ) ,
                                                                                
                                                                                                             (4)
                                              η (ℓ) ∼ πη̄(ℓ) ,
                                                                                              (ℓ) .
where D(ℓ) denotes a generic parametric family for margin ℓ, with mean parameter µi,j = X′i,j β (ℓ) , where β (ℓ)
are the population-level (fixed) effects, and remaining (family-specific) parameters η (ℓ) . Remaining parameters
β̄ (ℓ) , Σ̄β(ℓ) , η̄ (ℓ) represent prior hyperparameters and can be determined according to any historical population-level
information or kept weakly/non informative. The hierarchical model in (4) is completed by a parametric copula family
Cψ linking the conditional marginals
                                                           ind
                                                Ui,j | ψ ∼ Cψ ,       ψ ∼ πψ ,                                     (5)
           .  (1)         (2)            (ℓ) .       (ℓ)            
where Ui,j = Ui,j , Ui,j          , with Ui,j = Fℓ|X yi,j | xi,j ; λℓ by construction, and πψ is a prior on the copula
parameter.

3     Bayesian computation in copula-based models
Bayesian inference for copula-based models of the form described in Section 2.2.1 poses non-trivial computational
challenges, arising primarily from the need to jointly estimate the marginal parameters λ and the copula parameters
ψ while properly propagating the uncertainty between the two components of the model. As discussed in Section 1,
the classical solution to this problem is the IFM estimator of [2, 22], conceived under a frequentist framework. This
two-step strategy, whereby marginal parameters are estimated first and copula parameters are subsequently estimated


                                                                  4
        Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


conditional on these marginal estimates (all via MLE), has been adopted in applied financial contexts in [23] and [24].
A fully joint likelihood-based approach, optimizing simultaneously over θ = (λ, ψ), would be a valid alternative.
However, this approach may suffer from slow mixing and scalability issues as the dimension d grows, or when the
marginal or copula densities are complex. From a Bayesian standpoint, this issue translates into a joint posterior
distribution over θ whose full conditional distributions rarely admit closed-form expressions, owing to the composite
structure of the copula density underlying (1). Since the combination of different copula and marginal densities typically
lacks a standard form, the resulting posteriors are analytically intractable, so that tailored MCMC schemes, or more
sophisticated approaches are required to carry out inference.
Most of the existing literature has focused on the Bayesian estimation of the copula component alone, treating the
margins as fixed or pre-transformed; we refer to [25, 26] for a general treatment and to [27, 21] for more specific cases.
Silva and Lopes [28] were among the first to explicitly explore joint copula-marginal estimation, proposing a full slice-
sampling-based MCMC scheme for simple i.i.d. parametric families (no linear models). Through simulation studies,
they showed that this joint approach better captures the posterior dependence, which in turn improves copula-based
model selection. In a related direction, [29] extended joint Bayesian estimation to the conditional copula setting, where
the copula parameter itself varies with a covariate, and confirmed a better understanding of the parameter dependences
and improved model selection.
Subsequent work has extended this joint-estimation logic in several contexts. In [30] a joint MCMC strategy is adopted
for the specific skew-t copula, exploiting the conditionally Gaussian representation of the skew-t distribution. Building
on the Gaussian-copula data-augmentation scheme of [31], in [32] two data-augmentation MCMC schemes are proposed
for copulas with discrete or mixed margins. More recently, [33] develop a joint MCMC scheme for the joint sampling
of regression coefficients and copula correlation in a Gaussian-copula endogeneity-correction model, underscoring the
extended relevance of joint posterior estimation.
Building on this literature, and motivated by the trade-off it highlights between computational simplicity and full
uncertainty propagation, we outline and compare two computational solutions for the multivariate copula-based
ADAPTIVE model introduced in Section 2.2.1. The first, proposed in [3] extends the classical IFM logic to a Bayesian
framework: marginal and copula parameters are both estimated in a Bayesian fashion, through a two-step (rather than
integrated), but fully probabilistic, procedure. This is the object of Section 3.1. In Section 3.2, we instead present a novel
joint MCMC alternative, that updates marginal and copula parameters within a single Markov chain, tailored specifically
to our copula-based multivariate ADAPTIVE. The two approaches are then compared empirically in Sections 4-5.

3.1   Bayesian IFM

The classical IFM procedure adopt a frequentist approach to independently estimate the marginal parameters λ first
(Step 1), and then, keeping the estimates fixed, a frequentist procedure is used to estimate ψ. Such an approach is
therefore likely to produce overly confident interval estimates by neglecting the sampling variability of λ̂ (as hinted
in Section 1). To overcome this limitation, we proposed a Bayesian version of the IFM approach in [3]. Marginal
and copula parameters are estimated through the same two-step logic underlying the classical IFM procedure, but
full Bayesian principles are adopted at both steps, so that uncertainty is propagated from the marginal to the copula
estimation stage.
Formally, recall θ = (λ1 , λ2 , ψ), with λℓ the parameter vector of margin ℓ = 1, 2, and ψ the copula parameter(s).
Given a sample of size n, Fn = {xi , y i }i=1,...,n , the Bayesian IFM proceeds in two steps:
Step 1: Bayesian marginal estimation. For each margin ℓ = 1, 2, we obtain, independently of each other and of the
        copula component, a set of M posterior draws (λ̃ℓ,(1) , . . . , λ̃ℓ,(M ) ) approximating the marginal posterior
        π(λℓ | Fn ), obtained via posterior sampling, e.g., MCMC methods [34, 35].
Step 2: Bayesian copula estimation. For each posterior vector draw λ̃(m) = (λ̃1,(m) , λ̃2,(m) ), for m = 1, . . . , M ,
        obtained in Step 1, pseudo-observations are generated as
                                                                   
                                   ũiℓ,(m) = Fℓ yiℓ | xi , λ̃ℓ,(m) , ℓ = 1, 2; i = 1, . . . , n,                   (6)
        so that ũi,(m) = (ũi1,(m) , ũi2,(m) ) represents a pseudo-sample from the copula, conditional on the m-th
        marginal draws. Then, a chain of length M ′ of posterior draws is obtained for the copula parameter for each
                                                              .
        of the m-th marginal draws. The last draw ψ̃(m) = ψ̃(M ′ ,m) can be retained from the copula chain, assuming
                                            ′
        it has converged by iteration M .
Repeating Step 2 across       m = 1, . . . , M marginal draws yields a set of (pseudo-)joint posterior draws
 λ̃1,(m) , λ̃2,(m) , ψ̃(m) , m = 1, . . . , M , which approximate the joint uncertainty in θ = (λ1 , λ2 , ψ) and can be
used directly to derive the predictive distributions of interest. The pseudo-code is summarized in Algorithm 1.


                                                              5
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


Algorithm 1 Pseudo-code for the Bayesian IFM
  Input: Sample Fn = {xi , yi }i=1,...,n , yi ∈ R2 , xi ∈ Rp
         Marginal and copula models, with associated parameters (λ1 , λ2 , ψ)
         length of posterior draws M, M ′ ∈ R
         Priors on (λ1 , λ2 , ψ)                      
  Output: Posterior draws: { λ̃1,(m) , λ̃2,(m) , ψ̃(m) }m=1,...,M

  Step 1: marginal parameters
  for ℓ = 1, 2 do
      get M posterior draws (λ̃ℓ,(1) , . . . , λ̃ℓ,(M ) ) approximating the marginal posterior distributions π(λℓ | Fn )
      generate pseudo-data                            (ℓ)               (ℓ)
                                                                                
                                                         ũ1,(1) . . . ũ1,(M )
                                                      .                   .. 
                                                      .
                                                      .         ...        . ,
                                                                                
                                                           (ℓ)           (ℓ)
                                                        ũn,(1) . . . ũn,(M )
         (ℓ)   .                      
  with ũi,(m) = Fℓ yiℓ | λ̃ℓ,(m) , xi .
  end for

  Step 2: copula parameters
  for m = 1, . . . , M do
                                                                                              (1)       (2)
      fix the marginal parameters to (λ̃1,(m) , λ̃2,(m) ) and take associated pseudo-data {(ũi,(m) , ũi,(m) )}i=1,...,n
     get M ′ posterior draws (ψ̃(1,m) , . . . , ψ̃(M ′ ,m) ) approximating the copula posterior distribution
               .
     set ψ̃(m) = ψ̃(M ′ ,m) , assuming the copula chain has converged at step M ′
  end for
                                                         
  Return posterior draws: { λ̃1,(m) , λ̃2,(m) , ψ̃(m) }m=1,...,M


Compared to its frequentist counterpart [2], the Bayesian IFM allows uncertainty to flow from the marginal to the
copula parameters, providing a more reliable quantification of the overall estimation uncertainty, while retaining the
computational simplicity of a two-step procedure. It can be recognized as an instance of the broader class of modular,
or cut, Bayesian inference schemes [4, 5], in which a model is partitioned into sequentially estimated modules (here, the
marginal and copula components) with information deliberately prevented from flowing back from the second module
into the first. This modular perspective has recently been studied for copula models independently by [6]. Because our
Bayesian IFM coincides with the type-1 cut posterior (second module represented by the copula and first module given
by the marginals) of [6], it inherits their Lemma 1 (asymptotic equivalence to frequentist IFM), Lemma 2 (asymptotically
correct uncertainty quantification for the marginal parameters even under copula misspecification), and Lemma 3
(asymptotically correct uncertainty quantification for the copula parameter under correct specification of both marginals
and copula model). Nevertheless, since cutting discards the feedback from the copula to the marginal parameters, which
is exploited by a joint posterior sampling, the Bayesian IFM and joint MCMC scheme may differ in their efficiency and
shall coincide only when the marginal and copula parameters are asymptotically information-orthogonal. This can be
understood as a direct consequence of comparing Lemma 3’s variance expression (Bayesian IFM) to the block-inverse
decomposition of the joint information matrix (see Supplementary material of [6]). Since this may not be true in general,
the development and comparison with a fully joint alternative remain of interest and it helps assess the impact of model
misspecification in one of the modules.

3.2   Joint MCMC

We now illustrate the proposed fully joint Markov chain Monte Carlo (joint MCMC) algorithm that directly targets the
posterior:
                
                   n Y ti
                               (1)                    (2)
                  Y
  π(θ | Fn ) ∝           f1 (yi,j | Xi,j ; λ1 ) f2 (yi,j | Xi,j ; λ2 )
                  i=1 j=1
                                                                                                i
                                                     (1)                     (2)
                                            × c F1 (yi,j | Xi,j ; λ1 ), F2 (yi,j | Xi,j ; λ2 ); ψ π(λ1 ) π(λ2 ) π(ψ), (7)


                                                              6
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


with priors specified in (4)–(5). The composite structure of the likelihood prevents closed-form full conditionals,
necessitating a Metropolis–Hastings (MH) strategy, outlined below.
Recall from Section 3.1 that θ = (λ1 , λ2 , ψ). We design a blocked MH sampler of the form
                                                                      
                            θ(m+1) = λ1,(m+1) , λ2,(m+1) , ψ(m+1) , m = 1, . . . , M,
with M the length of the posterior chain. For each margin ℓ = 1, 2, the parameter vector λℓ may include regression
coefficients and scale parameters, while ψ relates to the copula parameters.
Marginal parameter updates. We use adaptive random-walk MH proposals of the form
                             λ∗ℓ = λℓ,(m) + ϵℓ,(m) ,     ϵℓ,(m) ∼ N (0, Σℓ,(m) ), ℓ = 1, 2.
       where Σℓ,(m) is updated sequentially using the empirical covariance of the chain. The acceptance probability
       is
                                               π(λ∗ℓ , λ−ℓ,(m) , ψ(m) | Fn )
                                                                             
                              αℓ = min 1,                                       , ℓ = 1, 2.
                                             π(λℓ,(m) , λ−ℓ,(m) , ψ(m) | Fn )
                                                                                       (ℓ)         (ℓ)
       Because the copula density depends on the transformed variables Ui,j = Fℓ (yi,j | Xi,j ; λℓ ), each proposed
       λ∗ℓ requires recomputing the pseudo-observations entering the copula likelihood. This ensures that depen-
       dence information influences the marginal updates, unlike in the Bayesian IFM, where Step 1 is performed
       independently of Step-2.
Copula parameter update. For the dependence parameter ψ, we use an adaptive MH step
                                     ψ ∗ = ψ(m) + η(m) , η(m) ∼ N (0, σψ,(m)
                                                                           2
                                                                                 ),
         with acceptance probability
                                                                                  
                                                            (1)    (2)   ∗
                                                                             π(ψ ∗ ) 
                                                  Q
                                                   i,j c Ui,j , Ui,j ; ψ
                                             
                                     αψ = min 1, Q                                   .
                                                         (1)    (2)
                                                   c U ,U ;ψ
                                                        i,j         i,j      π(ψ ) 
                                                                           i,j   (m)         (m)

         This update is computationally demanding because the copula must be evaluated for all observations at each
         iteration.
The pseudo-code is summarized in Algorithm 2.
Compared to the Bayesian IFM procedure of Section 3.1, the joint MCMC algorithm provides a coherent and fully
joint exploration of the posterior distribution of θ, thereby avoiding potential underestimation of uncertainty inherent to
two-stage approaches. By updating all components of θ within a single Markov chain, the method correctly propagates
dependence between marginal and copula parameters, yielding posterior intervals that appropriately reflect joint
variability.

4   Comparative Simulation Studies
Simulation studies are first conducted to assess the inferential performance of the joint MCMC and Bayesian IFM
approaches under controlled conditions. To provide a realistic benchmark for the subsequent real-world application,
the data-generating process is calibrated to reproduce the main distributional and dependence features observed in
the original data described in Section 5. Specifically, following the patterns shown in Figure 3 and Table 2, for each
simulated dataset, we use Gaussian marginals combined with a Gumbel copula. Gaussian marginals were chosen
to isolate the effects of copula specification and inferential methodology, while keeping the data-generating process
simple. The copula itself is selected from four candidates - Gaussian, Clayton, Gumbel, and Frank - using the Akaike
Information Criterion (AIC), see Table 2.
Among the available variables, sex and age are selected as the main covariates for the simulation study. The data-
generating process (i.e., the marginal parameters) is guided by fitting a linear model to the observed data for each
biomarker, with results reported in the Appendix B. The copula density is assumed to be covariate independent,
with the Gumbel dependence parameter estimated using the BiCopEst() [36] and resulting in a Kendall’s τ ≈ 0.55.
Specifically, for i = 1, . . . , n the generative process is given by
                                                                  (1)            (2)
                           YiHgb ∼ N (µi = 14.18 + 1.54 Xi              − 0.03 Xi , σ = 0.95),                          (8)
                                                                  (1) (2)
                           YiOFFs ∼ N (µi = 51.50 + 22.29 Xi + 0.22 Xi , σ = 12.99),
                           (UiHgb , UiOFFs ) ∼ CθGumbel (θ = 2.22),


                                                              7
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection




Algorithm 2 Pseudo-code for the joint MCMC
  Input: Sample Fn = {xi , yi }i=1,...,n , yi ∈ R2 , xi ∈ Rp
         Marginal and copula models, with associated parameters (λ1 , λ2 , ψ)
         length of posterior draws M ∈ R
         Priors on (λ1 , λ2 , ψ)                      
  Output: Posterior draws: { λ1,(m) , λ2,(m) , ψ(m) }m=1,...,M

  Initialize (λ1,(0) , λ2,(0) , ψ(0) )

  for m = 1, . . . , M do

      Step 1: update marginal parameters for Hgb
      Propose λ∗1 = λ1,(m−1) + ϵ1 , with ϵ1 ∼ N (0, Σ1 )
      Compute acceptance probability
                                                 π(λ∗1 , λ2,(m−1) , ψ(m−1) | Fn )
                                                                                   
                              α1 = min 1,
                                              π(λ1,(m−1) , λ2,(m−1) , ψ(m−1) | Fn )
      Set λ1,(m) = λ∗1 with probability α1 , otherwise λ1,(m) = λ1,(m−1)

      Step 2: update marginal parameters for OFFs
      Propose λ∗2 = λ2,(m−1) + ϵ2 , with ϵ2 ∼ N (0, Σ2 )
      Compute acceptance probability
                                                   π(λ1,(m) , λ∗2 , ψ(m−1) | Fn )
                                                                                  
                               α2 = min 1,
                                               π(λ1,(m) , λ2,(m−1) , ψ(m−1) | Fn )
      Set λ2,(m) = λ∗2 with probability α2 , otherwise λ2,(m) = λ2,(m−1)

      Step 3: update copula parameter
      Propose ψ ∗ = ψ(m−1) + η, with η ∼ N (0, σψ2 )
      Compute acceptance probability
                                                  π(λ1,(m) , λ2,(m) , ψ ∗ | Fn )
                                                                                
                                αψ = min 1,
                                               π(λ1,(m) , λ2,(m) , ψ(m−1) | Fn )
     Set ψ(m) = ψ ∗ with probability αψ , otherwise ψ(m) = ψ(m−1)
                                        
     Store draw: λ1,(m) , λ2,(m) , ψ(m)
  end for
                                                  
  Return posterior draws: { λ1,(m) , λ2,(m) , ψ(m) }m=1,...,M




                                                        8
         Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


          (1)                                            (2)
where Xi denotes the sex of athlete i, and Xi denotes the corresponding age. To mimic the true variability of the
covariates, rather than generating them ex-novo, we simulate them using a bootstrap resampling approach. We consider
a total sample size of n = 500.
Once the observations are generated on the uniform scale from the copula, they are transformed back to the original
scale using the inverse marginal CDF, with the marginal means evaluated conditionally on the corresponding covariate
          (ℓ)                    (ℓ)
values, Yi = Φ−1   (ℓ) (U
                          (ℓ)
                              ; µi , σ (ℓ) ). Because the two biomarkers are measured on different scales, the simulated
responses were standardized to improve numerical stability and facilitate prior specification. Since copulas are invariant
under strictly increasing marginal transformations, this approach does not alter the dependence structure. Weakly
                                                                                 (ℓ)     (ℓ)     (ℓ)  (1)    (ℓ)   (2)
informative priors are assigned to the marginal parameters. Specifically, given µi = β0 + β1 Xi + β2 Xi , we
set
                                                  (ℓ)
                                              βk ∼ N (0, 2.52 ),         ℓ = 1, 2;                                       (9)
                                                  (ℓ)
                                              σ         ∼ half − t3 (0, 2.5),   ℓ = 1, 2,
for all fixed coefficients k = 0, 1, 2.
Dependence is modeled directly through the parameter θ of the Gumbel copula, controlling the positive upper-tail
dependence between the two biomarkers. Since only positive dependence is considered, a weakly informative uniform
prior bounded in (1, 10) is assigned; that is,
                                                               ind
                                          (UiHgb , UiOFFs )|θ ∼ CθGumbel ,      θ ∼ U(1, 10).

All simulation studies are based on a number of 1,000 Monte Carlo (MC) replicas.

4.1     Software and computational details

The inference was carried out under identical computational settings for both approaches. For each method, 4
independent Markov chains were run, each consisting of M = 10,000 iterations. The first half was discarded as burn-in,
resulting in 5,000 iterations. A thinning factor of 5 was subsequently applied, yielding 1,000 posterior draws per chain
and 4,000 posterior draws overall. All analyses were performed in R version 4.5.1 (2025-06-13). Bayesian inference for
the marginal distributions was carried out using rstan [37] and the brms [38] package, an interface for fitting Bayesian
regression models with Stan. The joint MCMC approach was performed using user-defined functions implementing
random-walk Metropolis Hastings (RWMH) algorithms for the parameters of the two variables considered. Inference
for the copula component was conducted analogously. Specifically, for both approaches, a user-defined RWMH
function was used to sample from the posterior distribution of the dependence parameter of the selected copula family.
Copula selection was performed using the BiCopSelect function from the VineCopula [36] package. Finally, the
computational cost was assessed using Sys.time.

4.2     Comparative Results

Figure 1 shows the distribution of the parameter estimates obtained from the two approaches across the 1,000 Monte
Carlo replications under the Gumbel copula specification (well-specified copula model). Both estimators show small
bias across all parameters -as indicated by the deviation from the true value being close to zero- with β2 , associated with
the Age effect, showing the widest spread and correspondingly higher RM SE under both methods. The most notable
differences are observed for the parameters related to copula and Kendall’s τ , for which joint MCMC exhibits a lower
bias than Bayesian IFM, while the RMSE values remain essentially identical between the two approaches. Despite
this variability, the distributions remain centered around the true value, indicating that the greater dispersion is not
accompanied by a systematic bias. Substantial differences emerge in terms of computational efficiency. For a simulated
dataset with n = 500 observations, obtaining the posterior samples required approximately 17.04 seconds with the joint
MCMC, compared with approximately 159.03 seconds (2:39 minutes) with the Bayesian IFM. This corresponds to
approximately 3.52 and 0.38 complete runs per minute, respectively. Thus, the joint MCMC is computationally more
efficient, it completes approximately 9.33 times as many runs per minute as the Bayesian IFM.

4.2.1    Copula misspecification
To further evaluate the computational efficiency of the inferential methods under copula misspecification, three
alternative copula families (Gaussian, survival Clayton, and Frank) are also fitted to the simulated data. Each of these
copulas exhibits distinct shapes, capturing dependence in a different way. As we are interested in positive dependence,
weakly informative uniform priors are assigned to the respective dependence parameters, ensuring a support comparable


                                                                     9
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection




Figure 1: Boxplots show the percentage deviation of each simulation’s posterior mean from the true parameter value,
100 × (θ̂ − θ)/|θ|, across 1000 simulated datasets of size n = 500 under the Gumbel copula with covariates. Top: joint
MCMC estimator. Bottom: Bayesian IFM. The orange triangle marks the mean relative bias per parameter, and the
dashed line at zero marks an unbiased estimate.



                                                         10
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


to the same range of Kendall’s τ considered for the Gumbel copula, (0, 0.9). Parameter estimates are also reported
in terms of Kendall’s τ , which provides a copula-invariant measure of dependence and therefore a common scale for
comparison. This allows the analysis to focus on the effects of copula misspecification.




Figure 2: Points show the mean relative bias per parameter for the joint MCMC (green) and Bayesian IFM (red)
estimators, under the Gaussian (top-left), Surv. Clayton (top-right), Gumbel (bottom-left) and Frank (bottom-right)
copulas with covariates. Labels report relative bias (B), coverage of the 95% credible interval (C), and relative RMSE
(R).

Figure 2 shows the results obtained by applying the two approaches under the different copula models, reporting
the relative bias, RMSE, and coverage probabilities for all parameters. The copula dependence parameter and τ
show noticeably lower coverage under Frank than under Gumbel for both estimators, while the marginal parameters
remain comparable across the two copula families.These findings are consistent with the theoretical results of [6] on
cutting feedback in misspecified copula models. Under correct specification of the marginal models, they establish that
inference for the marginal parameters is asymptotically well-calibrated regardless of whether the copula function is
correctly specified or not, while the dependence parameter requires both the marginals and the copula to be correctly
specified. Our results reproduce this asymmetry. Coverage of the 95% confidence intervals for the marginal parameters
of Hgb and OFFs remained close to nominal across all four fitted copula families and under both the joint MCMC
and Bayesian IFM estimators (0.842-0.956), indicating that misspecification of the copula has negligible impact on
marginal inference when the margins themselves are correctly specified. In contrast, coverage for the dependence
parameters (θ and τ ) was strongly sensitive to whether the fitted copula matched the true dependence structure. When
the correctly specified copula was fit, coverage for θ and τ remained near nominal under both estimators (0.956/0.946,
joint MCMC/Bayesian IFM). When the copula was misspecified, it deteriorated substantially, most severely for the


                                                         11
        Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


Bayesian IFM estimator under the Clayton fit, where coverage for θ and τ fell to 0.145 and 0.144, respectively -
compared to 0.447 and 0.446 under the joint MCMC estimator. This pattern mirrors the degradation in τ coverage
reported by [6] (Table 2) under copula misspecification, and supports their theoretical result that two-step (IFM-style)
inference for the dependence parameter is particularly vulnerable to copula misspecification, since it does not propagate
the additional uncertainty that a jointly estimated model can partially absorb.

5     Application to NADO Italia data
The dataset used in the empirical analysis consists of longitudinal hematological measurements collected from athletes
monitored through the Athlete Biological Passport (ABP) program. The dataset was provided by NADO Italia
(https://www.nadoitalia.it), the sole authority responsible for implementing the anti-doping standards in Italy.


Table 1: Descriptive statistics of the study population by Age, Altitude, Test Type, and Sex, reported as absolute
frequencies and relative percentages.
               Age                          Altitude                         Test Type                 Sex
            Freq. Prop.                     Freq. Prop.                          Freq. Prop.              Freq. Prop.
20 ⊣ 35      188      85%      No            186     83%        Out-of-Comp       216     97%      M       113      51%
35 ⊣ 45       14       6%      Yes           31      14%        In-Comp            7       3%      F       110      49%
45 ⊣ 55       21       9%      Unknow         6       3%




5.1   Data description




Figure 3: Histograms (left) and scatterplot (right) of the Hgb and OFFs markers, illustrating the marginal distributions
and the presence of positive dependence.

The dataset comprises the ABP profiles of a cohort of n = 23 athletes, collected between 2019 and 2024, for a total of
223 repeated observations. For each athlete i = 1, . . . , n, demographic and athlete-level information is available, along
with all variables specified in the hematological module of the ABP used by WADA for the longitudinal monitoring of
athletes. Table 1 shows the distribution of the main covariates considered. The dataset is well balanced with respect
to sex, with 51% of the observations relating to male athletes and the remaining 49% relating to female athletes.
Measurements are also concentrated mainly among athletes at the peak of their competitive careers: approximately
85% of the observations relate to individuals aged between 20 and 35 years, while the remaining 15% are distributed
between 35 and 55 years of age. By contrast, the covariates related to high-altitude exposure and the type of test show a
highly imbalanced distribution. Only 24% of the observations were collected after exposure to high altitudes, while
the remainder of the sample comprises athletes who were not exposed or for whom no information is available. An
even more pronounced imbalance is observed for the variable related to sample collection type, with only 3% of the
measurements taken in-competition. Therefore, their contribution is not considered in the present study. The empirical


                                                           12
         Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


distributions of the two primary biomarkers are shown in Fig. 3. Hgb shows relatively low variability, with observed
values ranging approximately between 10 g/dL and 18 g/dL and its distribution exhibits slight negative skewness, with
observations concentrated towards the upper end of the distribution. The OFFs shows substantially greater variability,
with values ranging approximately between 20 and 100. Its distribution also exhibits negative skewness, with a greater
concentration of mass in the upper tail relative to Hgb.

5.2     Model formulation

Marginals Given the primary objective of comparing the joint MCMC and Bayesian IFM inferential procedures, and
consistent with the ADAPTIVE model [10], Gaussian marginal distributions are assumed for both biomarkers.
                                               (ℓ)                       (ℓ)
                                           Yi |β (ℓ) , σ (ℓ) ∼ N (µi , σ (ℓ) ),            ℓ = 1, 2,                  (10)
          (ℓ)     (ℓ)   (ℓ)    (1)       (ℓ)    (2)
where µi        = β0 + β1 Xi         + β2 Xi .
Before fitting the model, both biomarkers are standardized using their respective empirical means and standard
deviations. Relatively weakly informative priors are then assigned to the parameters of each marginal model
                                                     (ℓ)
                                                βk ∼ N (0, 2.52 ),             ℓ = 1, 2;                              (11)
                                                     (ℓ)
                                                σ          ∼ half − t3 (0, 2.5),     ℓ = 1, 2,

for all fixed coefficients k = 0, 1, 2.

Copula model The copula specification was selected based on the AIC criterion, reported in Table 2. The dependence
structure between the biomarkers is modeled using a Gumbel copula, assigning a weakly informative prior to its
dependence parameter
                                                                  ind
                                          (UiHgb , UiOFFs )|θ ∼ CθGumbel ,          θ ∼ U(1, 10)                      (12)

allowing a broad range of positive dependence, from independence to strong upper-tail dependence.

                           GAUSSIAN                                CLAYTON                             GUMBEL     FRANK

AIC                           -191.332                              -169.433                           -195.357   -174.045
BIC                           -187.924                              -166.026                           -191.950   -170.638
logLik                         96.666                                85.717                             98.679     88.023
Table 2: AIC, BIC, and log-likelihood values for the different copula specifications, evaluated on the NADO Italia
dataset. The Gumbel copula provides the best fit according to all three criteria.



5.2.1    Results and discussion
Table 3 reports the posterior point estimates and corresponding credible intervals obtained using the two approaches,
which show substantial overlap. The main difference arises for the parameter β2OFFs , for which the joint MCMC credible
interval includes zero, whereas the Bayesian IFM interval is entirely positive, suggesting stronger evidence for a positive
effect. Overall, both approaches yield similar results.



Figure 4 shows the estimated 95% HPRs for the NADO Italia dataset for both male and female athletes, with age fixed
at 24 years, using both inferential approaches. Male athletes exhibit higher values on average, resulting in a predictive
region shifted towards the upper-right portion of the plot, whereas for female athletes the region is shifted towards
the lower-left. However, the regions exhibit a substantial area of overlap, indicating the existence of a range values
compatible with both sexes. All observations for male athletes fall within the respective HPRs under both inferential
approaches, whereas a portion of the observations for female athletes falls outside. Specifically, 8.2% and 9.2% of
female observations fall outside the HPRs estimated using the joint MCMC and Bayesian IFM approaches, respectively.
These results are also summarized in Table 4.


                                                                        13
         Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection



Table 3: Posterior estimates and 95% credible intervals for the marginal regression coefficients, standard deviations, and
Gumbel copula dependence parameters obtained from the NADO Italia dataset using the joint MCMC and Bayesian
                                     (ℓ) (ℓ)        (ℓ)
IFM approaches. The parameters β0 , β1 , and β2 denote the intercept, sex effect, and age effect, respectively, for
biomarker ℓ.
                                joint MCMC                                               Bayesian IFM
               CI Upper           CI Lower            Estimate           Estimate           CI Lower            CI Upper
β0Hgb            14.789             13.816             14.320             14.180             13.721              14.646
β1Hgb            1.725              1.253              1.489               1.534             1.281               1.782
β2Hgb            -0.016             -0.046             -0.031             -0.028             -0.042              -0.014
  Hgb
σ                1.093              0.904              0.993               0.954             0.871               1.049
β0OFFs           61.265             48.794             55.153             51.562             45.292              57.833
β1OFFs           23.564             17.132             20.348             22.243             18.710              25.658
β2OFFs           0.335              -0.058             0.136               0.216             0.023               0.408
σ OFFs           14.687             12.233             13.376             13.065             11.905              14.361
θ                2.155               1.657              1.891              1.785              1.574               2.007
τ                0.536               0.396              0.469              0.437              0.365               0.502




Figure 4: Estimated 95% HPRs obtained with both the joint MCMC (dashed lines) and Bayesian IFM (solid lines)
approaches. Points represent observations from the NADO Italia dataset. Blue and pink regions correspond to male and
female athletes, respectively.


Doped athletes Figure 5 shows the same 95% HPRs together with observations from court rulings (TAS/CAS, UCI)
involving athletes convicted of anti-doping rule violations related to the hematological module of the ABP. For female
athletes, 89.7% of the observations are classified as atypical, while for male athletes, joint MCMC identifies 82.5% and
Bayesian IFM 84.2% as atypical. Overall, the two approaches classify 84.9% and 86% of the observations as atypical,
respectively, as shown in Table 5.



                                                           14
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


                                                                                 FPR
                                             Male                               Female                               Total
joint MCMC                                   0.000                               0.082                               0.040
Bayesian IFM                                 0.000                               0.091                               0.045
Table 4: Classification performance of the predictive regions obtained from the joint MCMC and Bayesian IFM
approaches in terms of false positive rate (FPR).



Notably, court rulings may report observations that are atypical with respect to the athlete’s individual reference range or
reflect suspicious variations in a biomarker over a specific time interval; not all reported observations are necessarily of
this kind. We attempted to select only those identified as atypical based on the evidence reported in the court decisions;
nevertheless, the sample may still contain observations that are not entirely relevant to the problem under investigation.




Figure 5: Estimated 95% HPRs obtained with both the joint MCMC (dashed lines) and Bayesian IFM (solid lines)
approaches. Points represent observations of athletes convicted of anti-doping rule violations. Blue and pink regions
correspond to male and female athletes, respectively.



                                                                                 TPR
                                             Male                               Female                               Total
joint MCMC                                   0.825                               0.897                               0.849
Bayesian IFM                                 0.842                               0.897                               0.860
Table 5: Classification performance of the predictive regions obtained from the joint MCMC and Bayesian IFM
approaches in terms of true positive rate (TPR).




                                                            15
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


6   Discussion and Conclusion

This work focuses on the Bayesian computational aspects of estimating multivariate copula-based models and was
directly motivated by an application to doping detection with two primary biomarkers of the Athlete Biological Passport.
Specifically, we introduced a fully joint MCMC alternative (Section 3.2), which updates marginal and copula parameters
within a single Markov chain, thereby allowing dependence information to flow in both directions. A side-by-side
comparison was then carried out with the two-step Bayesian IFM strategy proposed in [3] (Section 3.1).
The comparative simulation study of Section 4 showed that, under a correctly specified copula, both procedures recover
the true parameters with comparably low bias and RMSE, with the joint MCMC exhibiting a modest advantage for
the copula dependence parameter and Kendall’s τ . Under copula misspecification, by contrast, the two procedures
displayed an asymmetric pattern for the two parameter blocks. For the marginal parameters, the Bayesian IFM
performed markedly better than the joint MCMC, especially when the misspecified fitted copula was the Frank or
the survival Clayton. This is a direct consequence of the modular, cut-feedback structure of the Bayesian IFM: by
preventing information from flowing from the copula module back to the marginal module, it shields the marginal
parameters from copula misspecification. The joint MCMC’s marginal estimates, on the other hand, are updated jointly
with the copula parameters at every iteration, so that a misspecified copula can contaminate the marginal inference
through this shared estimation process. This result is consistent with the theoretical and empirical findings of [6]
for cut posteriors. For the dependence parameter (θ or τ ), both the Bayesian IFM and the joint MCMC deteriorated
substantially once the fitted copula departed from the true one, and did so far more severely for the Bayesian IFM than
for the joint MCMC. It is also worth noting that the two approaches showed some divergence in computational cost,
with the joint MCMC showing remarkable advantages over the Bayesian IFM counterpart.
The application to the NADO Italia dataset complemented the simulation findings in a real setting. Posterior estimates
of the marginal and copula parameters obtained under the two procedures were broadly consistent, with the only notable
discrepancy concerning the age effect on OFFs, for which the Bayesian IFM credible interval excluded zero while the
joint MCMC interval did not. Both approaches produced comparable classification performance: a false positive rate of
4.0–4.5% on the clean-athlete cohort, and a true positive rate of 85–86% on a set of court-documented anti-doping rule
violations, with no substantial advantage of one method over the other.
Taken together, these results point to a genuine trade-off rather than a uniformly preferable choice between the two
procedures. The joint MCMC is markedly faster and provides better-calibrated inference for the dependence parameter,
making it the natural default whenever computational cost is the binding constraint or when the copula family can be
trusted to be reasonably well specified. The Bayesian IFM offers a practically important advantage in settings where the
copula family is uncertain or difficult to validate. As emphasized throughout the anti-doping literature, false positives
carry serious consequences for clean athletes, and since the marginal parameters directly determine the reference ranges
against which an individual athlete’s biomarker values are judged, their robustness to copula misspecification is not a
secondary concern.
Several methodological extensions remain open for future work. First, the hierarchical marginal model of Section 2.2.1
(and related estimation) could be extended to accommodate individual random effects or temporal dependence within
an athlete’s longitudinal profile; while the assumption of time-independence may be reasonable for widely spaced
measurements, within-individual serial dependence is likely to arise in practice. Second, although the present analysis
focuses on the two primary hematological markers, the proposed framework extends naturally to a larger biomarker
panel through vine copula constructions [39], which represent high-dimensional dependence structures via bivariate
building blocks; extending the Bayesian IFM to this setting would require estimating additional marginals and a cascade
of conditional copulas, with a corresponding increase in computational complexity. In contrast, the joint MCMC would
require only a proportional increase in the number of blocks updated at each iteration. Third, we note that MCMC is
not the only computational route to joint Bayesian copula estimation. Variational inference has been proposed as a
faster, approximate alternative for vine-copula-structured likelihoods [40], and approximate Bayesian computation
has similarly been used to sidestep intractable copula likelihoods altogether [20]. We did not pursue either direction
here, given the moderate dimensionality of our application, but both represent natural avenues for scaling the proposed
framework to larger biomarker panels. Finally, the highest predictive regions used here to flag atypical profiles rely on
asymptotic justifications for their coverage properties; an interesting alternative would be to construct such uncertainty
regions using conformal inference methods (see [41] and [42] for a Bayesian treatment), which provide finite-sample
coverage guaranties under comparatively mild assumptions and could complement or substitute the approach adopted
here.
Beyond its methodological contribution, this work has direct practical relevance for anti-doping practice. Complement-
ing [3], who already showed the substantial advantage of the multivariate copula-based extension of ADAPTIVE, the
present paper provides the technical machinery and a concrete comparison between two viable inferential routes, needed


                                                           16
        Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


to actually implement this multivariate upgrade in practice. For international and national anti-doping organizations,
this means the improved discriminating power of the multivariate model is no longer only a theoretical prospect: it
comes with two fully specified, implementable estimation procedures, together with explicit guidance on the trade-offs
between them, so that the choice can be tailored to the operational constraints and priorities of a given laboratory. In a
setting where thousands of athlete profiles are screened routinely and the cost of a wrong decision is severe, having
both a more accurate strategy and a viable route is what makes the transition to the multivariate ADAPTIVE model
practically achievable.

Data Availability
The data that support the findings of this study are owned by NADO Italia (National Anti-Doping Organisation Italy)
and are not publicly available. They contain sensitive personal information on athletes and were provided exclusively for
this research, under the explicit consent of the athletes involved. Restrictions therefore apply to the availability of these
data, which were used under permission of NADO Italia for the current study. The observations of athletes convicted of
anti-doping rule violations used in Section 5 were retrieved from publicly available court rulings (TAS/CAS and UCI).

Acknowledgments
The authors would like to thank NADO Italia, the owner of the dataset used in this study, which was collected as part
of the project Enhancing the methodological framework for doping detection: from univariate to multivariate testing
analysis on Athlete Biological Passport profiles. The project particularly involved Dr. Michaela Procaccini and Prof.
Giuseppe D’Onofrio.

Financial Disclosure
This project has been carried out with the support of the World Anti-Doping Agency and the Partnership for Clean
Competition (WADA Grant 23D01BL). The funders had no role in the study design, data analysis, and interpretation of
the results.

Conflicts of Interest
The authors declare no conflicts of interest.

References
 [1] A. Sklar. Fonctions de répartition à N dimensions et leurs marges. Annales de l’ISUP, VIII(3):229–231, 1959.
 [2] H. Joe and J.J. Xu. The estimation method of inference functions for margins for multivariate models. Technical
     report, Technical Report No. 166, Department of Statistics, University of British Columbia, Vancouver., 1996.
 [3] N. Deliu and B. Liseo. A Copula-based Bayesian Framework for Doping Detection. Computational Statistics,
     40:1873–1898, 2025.
 [4] P.E. Jacob, L.M. Murray, C.C. Holmes, and C.P. Robert. Better together? statistical learning in models made of
     modules. arXiv preprint arXiv:1708.08719, 2017.
 [5] E. Pompe, M. Kasprzak, and P.E. Jacob. Asymptotics of Cut Distributions and Robust Modular Inference Using
     Posterior Bootstrap. arXiv preprint arXiv:2110.11149, 2025.
 [6] M.S. Smith, W. Yu, D.J. Nott, and D.T. Frazier. Cutting Feedback in Misspecified Copula Models. Journal of the
     American Statistical Association, 120(551):1975–1989, 2025.
 [7] B. Houlihan, D. Vidar Hanstad, S. Loland, and I. Waddington. The World Anti-Doping Agency at 20: progress
     and challenges. International Journal of Sport Policy and Politics, 11(2):193–201, April 2019.
 [8] WADA. The World Anti-Doping Code. Technical report, World Anti-Doping Agency, 2021.
 [9] P.E. Sottas, N. Robinson, O. Rabin, and M. Saugy. The athlete biological passport. Clinical Chemistry, 57(7):969–
     976, July 2011.
[10] P.-E. Sottas, N. Baume, C. Saudan, C. Schweizer, M. Kamber, and M. Saugy. Bayesian detection of abnormal
     values in longitudinal biomarkers with an application to T/E ratio. Biostatistics, 8(2):285–296, 2007.


                                                            17
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


[11] D. Eleftheriou, T. Piper, M. Thevis, and T. Neocleous. A multivariate Bayesian learning approach for improved
     detection of doping in athletes using urinary steroid profiles. The International Journal of Biostatistics, 21(1):165–
     181, 2025.
[12] R.B. Nelsen. An introduction to copulas. Springer Series in Statistics. Springer, New York, 2nd ed edition, 2006.
[13] R.J. Hyndman. Computing and Graphing Highest Density Regions. The American Statistician, 50(2):120, 1996.
[14] N. Deliu and B. Liseo. Alternative Approaches for Estimating Highest-Density Regions. International Statistical
     Review, 94(1):97–120, 2026.
[15] K. Sharpe, W. Hopkins, K.R. Emslie, and others. Development of reference ranges in elite athletes for markers of
     altered erythropoiesis. Haematologica, 87(12):1248–1257, December 2002.
[16] P.E. Sottas, N. Robinson, M. Saugy, and O. Niggli. A forensic approach to the interpretation of blood doping
     markers. Law, Probability and Risk, 7(3):191–210, 2008.
[17] A.J. Patton. Modelling Asymmetric Exchange Rate Dependence. International Economic Review, 47(2):527–556,
     2006.
[18] I. Gijbels, M. Omelka, and N. Veraverbeke. Estimation of a Copula when a Covariate Affects only Marginal
     Distributions. Scandinavian Journal of Statistics, 42(4):1109–1126, 2015.
[19] I.H. Haff, K. Aas, and A. Frigessi. On the simplified pair-copula construction — Simply useful or too simplistic?
     Journal of Multivariate Analysis, 101(5):1296–1310, May 2010.
[20] C. Grazian, L. Dalla Valle, and B. Liseo. Approximate Bayesian conditional copulas. Computational Statistics &
     Data Analysis, 169:107417, 2022.
[21] E. Levi and R.V. Craiu. Bayesian inference for conditional copulas using Gaussian Process single index models.
     Computational Statistics & Data Analysis, 122:115–134, June 2018.
[22] H. Joe. Asymptotic efficiency of the two-stage estimation method for copula-based models. Journal of Multivariate
     Analysis, 94(2):401–419, 2005.
[23] W. Hürlimann. Fitting bivariate cumulative returns with copulas. Computational Statistics & Data Analysis,
     45(2):355–372, 2004.
[24] O. Roch and A. Alegre. Testing the bivariate distribution of daily equity returns using copulas: An application to
     the Spanish stock market. Computational Statistics & Data Analysis, 51(2):1312–1329, 2006.
[25] M.S. Smith. Bayesian approaches to copula modelling. In P. Damien, P. Dellaportas, N.G. Polson, and D.A.
     Stephens, editors, Bayesian Theory and Applications, pages 336–358. Oxford University Press, 2013.
[26] A. Shemyakin and A. Kniazev. Introduction to Bayesian estimation and copula models of dependence. John
     Wiley & Sons, 2017.
[27] A. Min and C. Czado. Bayesian inference for multivariate copulas using pair-copula constructions. Journal of
     Financial Econometrics, 8(4):511–546, 2010.
[28] R. Silva and H.F Lopes. Copula, marginal distributions and model selection: a Bayesian note. Statistics and
     Computing, 18:313–320, 2008.
[29] R.V. Craiu and A. Sabeti. In mixed company: Bayesian inference for bivariate conditional copula models with
     discrete and continuous outcomes. Journal of Multivariate Analysis, 110:106–120, 2012.
[30] M.S. Smith, Q. Gan, and R.J. Kohn. Modelling dependence using skew t copulas: Bayesian inference and
     applications. Journal of Applied Econometrics, 27(3):500–522, 2012.
[31] M. Pitt, D. Chan, and R. Kohn. Efficient Bayesian inference for Gaussian copula regression models. Biometrika,
     93(3):537–554, 2006.
[32] M.S. Smith and M.A. Khaled. Estimation of Copula Models with Discrete Margins via Bayesian Data Augmenta-
     tion. Journal of the American Statistical Association, 107(497):290–303, 2012.
[33] R.E. Haschka. Bayesian Inference for Joint Estimation Models Using Copulas to Handle Endogenous Regressors.
     Oxford Bulletin of Economics and Statistics, 88(3):519–534, 2026.
[34] C.P. Robert and G. Casella. Monte Carlo Statistical Methods. Springer Texts in Statistics. Springer, New York,
     NY, 2004.
[35] M.D. Hoffman, A. Gelman, et al. The No-U-Turn sampler: adaptively setting path lengths in Hamiltonian Monte
     Carlo. Journal of Machine Learning Research, 15(1):1593–1623, 2014.
[36] T. Nagler, U. Schepsmeier, J. Stoeber, E.C. Brechmann, B. Graeler, and T. Erhardt. VineCopula: Statistical
     Inference of Vine Copulas, 2025. R package version 2.6.1.


                                                           18
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


[37] Stan Development Team. RStan: the R interface to Stan, 2025. R package version 2.32.7.
[38] P.C. Bürkner. brms: An R package for Bayesian multilevel models using Stan. Journal of Statistical Software,
     80(1):1–28, 2017.
[39] C. Czado. Analyzing Dependent Data with Vine Copulas: A Practical Guide With R, volume 222 of Lecture Notes
     in Statistics. Springer International Publishing, Cham, 2019.
[40] V. Kejzlar and T. Maiti. Variational inference with vine copulas: an efficient approach for Bayesian computer
     model calibration. Statistics and Computing, 33(1):18, 2023.
[41] V. Vovk, A. Gammerman, and G. Shafer. Algorithmic learning in a random world. Springer, 2005.
[42] N. Deliu and B. Liseo. The interplay between bayesian inference and conformal prediction. Philosophical
     Transactions of the Royal Society A, 384(2327), 2026.




                                                       19
        Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection


A     Model without covariates
In the model without covariates, the marginal parameters are estimated via maximum likelihood (MLE). We assume
Gaussian distributions for both marginals, with µ ≈ 14.14 and σ ≈ 1.24 for Hgb, and µ ≈ 69.20 and σ ≈ 17.15 for
OFFs. After transforming the observations to the unit interval, a Gumbel copula model is fitted to the data, yielding
Kendall’s τ = 0.55 and a corresponding dependence parameter θ ≈ 2.22. The resulting data-generating process is
defined as follows:
                                   YiHgb ∼ N (µ = 14.14, σ = 1.24),                 i = 1, . . . , n
                                   YiOFFs ∼ N (µ = 69.20, σ = 17.15)                                                      (13)
                                   (UiHgb , UiOFFs ) ∼ CθGumbel (θ = 2.22).
Subsequently, the simulated observations are transformed back to their original scale using the inverse of the marginal
        (ℓ)
CDF, Yi = Φ−1   (ℓ) (U
                       (ℓ)
                           ; µ(ℓ) , σ (ℓ) ). For each simulated dataset, a Gaussian marginal distribution is specified for both
variables. The data are then standardized, and weakly informative priors are assigned to the marginal parameters
                                                  µ(ℓ) ∼ N (0, 2.52 ),                                                    (14)
                                                      (ℓ)
                                                  σ         ∼ half − t3 (0, 2.5).

Dependence is modeled through a Gumbel copula, with a uniform prior assigned to the dependence parameter θ
                                                             ind
                                       (UiHgb , UiOFFs )|θ ∼ CθGumbel ,      θ ∼ U(1, 10).                                (15)
The prior is restricted to positive dependence, given the intrinsic association between Hgb and OFFs.

A.1   Results

The upper-right panel of Figure 6 shows the results obtained from the two approaches for the model without covariates.
For all parameters considered, the bias and RMSE values are relatively small, indicating a good ability of both approaches
to recover the true parameter values. The most notable differences arise for the copula dependence parameter and
Kendall’s τ . Joint MCMC exhibits a positive bias and a coverage probability of 90%, whereas Bayesian IFM shows
a negative bias and a coverage probability of 85%. These results suggest a slight overestimation of dependence for
the former and an underestimation for the latter, together with undercoverage for both approaches, which is more
pronounced for Bayesian IFM. In contrast, the coverage probabilities for the marginal parameters are close to or above
the nominal level.

A.2   Copula misspecification

Three different misspecified copula families are considered: Gaussian, Frank and survival Clayton. Dependence is
modeled through the parameter specific to each copula family, with the parameter space chosen to ensure coverage
of Kendall’s τ over the interval (0, 0.9). Figure 6 reports the results under copula misspecification, including the
corresponding bias, coverage probabilities, and RMSE. In all three cases, Bayesian IFM provides accurate estimates of
the marginal parameters, with coverage probabilities close to the nominal level. Joint MCMC performs well under the
Gaussian copula, whereas under Frank and survival Clayton it provides less accurate estimates, particularly for the
scale parameters, with coverage probabilities below the nominal level. For the copula parameters, Gaussian copula
performs well, and the Frank copula shows a slightly larger bias only for Joint MCMC. For the survival Clayton copula,
however, the bias increases substantially for both methods, with a marked decrease in coverage probability (45% for
Joint MCMC, 24% for Bayesian IFM). Overall, these results indicate greater stability of Bayesian IFM in estimating
the marginal parameters under copula misspecification, while inference on the dependence structure is more sensitive to
the assumed copula family.

B     Linear Model Fitting
Table 6 reports the results of the linear models fitted to Hgb and OFFs. The estimated coefficients are used to define the
marginal parameters of the data-generating process.




                                                                   20
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection




Figure 6: Points show the mean relative bias per parameter for the Joint MCMC (green) and Bayesian IFM (red)
estimators, under the Gaussian (top-left), Gumbel (top-right), and Frank (bottom-left) and Surv. Clayton (bottom-right)
copulas without covariates (n = 500, 100 simulations); The dashed line marks zero deviation and, labels give relative
bias (B), coverage of the 95% credible interval (C), and relative RMSE (R).




                                                          21
       Bayesian Computation of Copula-based Multivariate Models with an Application to Doping Detection




                                                               Dependent variable:
                                                              Hgb            OFFs
                        β0 – Constant                      14.178∗∗∗      51.503∗∗∗
                                                            (0.232)        (3.180)
                        β1 – Gender                           1.536∗∗∗      22.292∗∗∗
                                                               (0.127)       (1.740)
                        β2 – Age                          −0.028∗∗∗          0.217∗∗
                                                           (0.007)           (0.100)
                        Observations                          223              223
                        R2                                   0.421            0.435
                        Adjusted R2                          0.416            0.430
                        Residual Std. Error (df = 220)       0.949           12.987
                        F Statistic (df = 2; 220)          80.010∗∗∗        84.603∗∗∗
                                                        ∗
                          Note:                           p<0.1; ∗∗ p<0.05; ∗∗∗ p<0.01
Table 6: Linear model fits for Hgb and OFFs, reporting R , adjusted R2 , residual standard errors, F-statistics, and
                                                        2

significance levels for each covariate.




                                                         22
