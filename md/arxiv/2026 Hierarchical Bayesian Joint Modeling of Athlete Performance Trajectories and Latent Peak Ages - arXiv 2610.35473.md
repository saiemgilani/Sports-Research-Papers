# Hierarchical Bayesian Joint Modeling of Athlete Performance Trajectories and Latent Peak Ages

- arXiv: https://arxiv.org/abs/2610.35473
- Published: 2026-10-26
- PDF: ../../library/preprints/arxiv/2026/2026 Hierarchical Bayesian Joint Modeling of Athlete Performance Trajectories and Latent Peak Ages - arXiv 2610.35473.pdf

## Abstract

Determining when athletes reach peak performance is a central question in sports science, with implications for talent identification, training design, and cross-discipline comparisons. Statistical inference is challenging because peak age is not directly observed: competition records are noisy and selective measurements of underlying performance capacity and are often limited to incomplete observation windows. We develop a hierarchical Bayesian joint modeling framework that links a longitudinal model for athlete-specific performance trajectories to a regression submodel for latent peak age. The longitudinal component models observed competition performances as noisy measurements of athlete-specific performance trajectories over age. The peak-age component then treats the maximizer of each trajectory as a latent response in a parametric accelerated failure time (AFT) model, allowing athlete-level covariates to explain earlier or later peak age. The hierarchical structure borrows information across athletes, while joint posterior inference propagates uncertainty from trajectory reconstruction to both individual peak-age estimates and population-level covariate effects. Simulation studies show that, as observation windows become less informative, the joint model preserves substantially smaller regression bias and reflects the information loss through wider uncertainty, whereas pseudo-peak and two-stage alternatives exhibit larger bias. An application to World Athletics ranking data illustrates how the joint model estimates discipline-specific peak-age patterns and covariate effects under incomplete and irregular observation windows. Beyond sports, the proposed framework applies broadly to problems that couple longitudinal trajectories with function-derived latent features.

## Full text (pdftotext)

                                                Hierarchical Bayesian Joint Modeling of Athlete Performance
                                                             Trajectories and Latent Peak Ages
                                                                 K. Ken Peng1,2           Tianyu Guan3             Xiong Zhao4,5
                                                  1
                                                    Department of Statistics and Actuarial Science, Simon Fraser University, Burnaby, British
                                                                                        Columbia, Canada
                                                        2
                                                          Department of Civil Engineering, University of Ottawa, Ottawa, Ontario, Canada
arXiv:2610.35473v1 [stat.AP] 26 Oct 2026




                                                     3
                                                       Department of Mathematics and Statistics, York University, Toronto, Ontario, Canada
                                                                         4
                                                                           AccMov Health Inc., Ottawa, Ontario, Canada
                                                   5
                                                     School of Kinesiology and Health Studies, Queen’s University, Kingston, Ontario, Canada


                                                                                             Abstract
                                                     Determining when athletes reach peak performance is a central question in sports science,
                                                 with implications for talent identification, training design, and cross-discipline comparisons. Sta-
                                                 tistical inference is challenging because peak age is not directly observed: competition records
                                                 are noisy and selective measurements of underlying performance capacity and are often limited
                                                 to incomplete observation windows. We develop a hierarchical Bayesian joint modeling frame-
                                                 work that links a longitudinal model for athlete-specific performance trajectories to a regression
                                                 submodel for latent peak age. The longitudinal component models observed competition per-
                                                 formances as noisy measurements of athlete-specific performance trajectories over age. The
                                                 peak-age component then treats the maximizer of each trajectory as a latent response in a
                                                 parametric accelerated failure time (AFT) model, allowing athlete-level covariates to explain
                                                 earlier or later peak age. The hierarchical structure borrows information across athletes, while
                                                 joint posterior inference propagates uncertainty from trajectory reconstruction to both individ-
                                                 ual peak-age estimates and population-level covariate effects. Simulation studies show that, as
                                                 observation windows become less informative, the joint model preserves substantially smaller
                                                 regression bias and reflects the information loss through wider uncertainty, whereas pseudo-peak
                                                 and two-stage alternatives exhibit larger bias. An application to World Athletics ranking data il-
                                                 lustrates how the joint model estimates discipline-specific peak-age patterns and covariate effects
                                                 under incomplete and irregular observation windows. Beyond sports, the proposed framework
                                                 applies broadly to problems that couple longitudinal trajectories with function-derived latent
                                                 features.

                                           Keywords: Accelerated failure time model; incomplete longitudinal data; latent event time; sports
                                           analytics; athlete performance monitoring.


                                           1    Introduction
                                           Managing and forecasting athletic performance over the course of a career is a central problem in
                                           sport science. A particularly important target is the age of peak performance (APP), because the
                                           timing of peak ability informs talent identification, training design, career planning, and health
                                           management (Allen and Hopkins, 2015). In high-performance sport, these questions also arise
                                           within broader development systems involving public investment, family costs, dual-career pres-
                                           sures, athlete transitions, and well-being concerns (Cakravastia and Setiawan, 2022; Hardy et al.,
                                           2010; Øydna et al., 2025; Pilkington et al., 2024; Spence et al., 2012; Tessitore et al., 2021; Houltberg

                                                                                                  1
and Scholefield, 2020; Soares and Carvalho, 2023; Subotnik et al., 2019). Our motivating application
uses track-and-field data, where events differ substantially in physiological and technical demands
and therefore provide a useful setting for studying discipline-specific peak-age patterns. Empirical
studies across sports suggest that peak performance often occurs in the mid-to-late twenties, but
with substantial variation across disciplines (Balatoni et al., 2020; Baker et al., 2017).
    Statistical inference on APP is difficult because the relevant object is not directly observed.
Conceptually, each athlete has an underlying age-specific performance capacity, denoted by Yi (t)
for athlete i at age t. The latent peak age is

                                         τi = arg max Yi (t),
                                                        t

the age at which the underlying performance trajectory reaches its maximum. In practice, however,
the full trajectory Yi (t) is unavailable. We observe only noisy competition records

                                          yij = Yi (tij ) + εij ,

at irregular ages tij , often over incomplete observation windows. Here εij represents residual varia-
tion between observed competition performance and latent performance capacity, including short-
term performance fluctuations and measurement noise. Because competition records are noisy,
sparse, and irregularly timed, the age of the best recorded performance may differ from the latent
APP of scientific interest. Thus, even when the scientific question is simple to state, the data
provide only a fragmented view of the career trajectory. These same features also complicate re-
gression analysis of how athlete-level characteristics shape both performance trajectories and peak
age.
     Most applied work in sport science therefore uses simplified summaries. One common approach
defines a pseudo peak age, such as the age of the best observed performance or the average age of
top-ranked athletes (Stiefel et al., 2013; Gorzi et al., 2022; Nikolaidis et al., 2017). Such summaries
are intuitive and easy to compute, but they can be biased or unstable when records are sparse, or
observed over only part of a career. A second approach first fits individual performance trajectories
and then regresses the resulting estimated peak ages on athlete-level covariates (Huebner and Per-
peroglou, 2019; Solberg et al., 2019; Haugen et al., 2018; Chen et al., 2025). Recent mixed-effects
and Bayesian longitudinal models improve trajectory estimation by borrowing information across
athletes (Griffin et al., 2022; Romann et al., 2024; Spyropoulou et al., 2024), but peak age is often
still extracted as a fitted-curve summary. In such two-stage analyses, the estimated peak ages are
treated as observed outcomes in the second stage, which can ignore first-stage uncertainty and lead
to understated uncertainty in regression inference (Murphy and Topel, 2002). Incomplete obser-
vation windows can also induce censoring- or truncation-like behavior, and heuristic treatments,
such as excluding athletes with few records or declaring the last observed age to be the peak, may
introduce additional bias (Brander et al., 2014).
     These limitations matter because APP is plausibly associated with multiple athlete-level and
contextual factors. Athlete development pathways, maturation timing, relative age effects, early
career milestones, specialization, training history, training load, recovery, and injury history may
all shape long-term performance dynamics (Parry et al., 2024; Barreira et al., 2021; Li et al., 2020;
McLellan et al., 2022; Exel and Dabnichki, 2024; Mian Darbandi and Zarei, 2023). This creates the
need for a statistical framework that can keep the trajectory, the peak age, and covariate effects in
the same inferential system.
     This paper develops a Bayesian joint modeling framework for longitudinal performance records
and latent peak ages. The proposed framework makes three main contributions. First, it recon-
structs athlete-specific latent performance trajectories from noisy, irregular, and partially observed

                                                    2
competition records. Second, it treats APP as a latent response defined by these trajectories, rather
than as an observed best-performance age or a plug-in estimate from a first-stage curve fit. Third,
it links latent peak age to athlete- and sport-specific covariates while propagating uncertainty from
trajectory reconstruction and peak-age estimation into regression inference. In simulations that
vary the informativeness of the observed age window and the trajectory specification, the proposed
joint formulation yields less biased covariate-effect estimates and reflects reduced peak-age infor-
mation through wider uncertainty intervals, whereas conventional alternatives tend to translate
the same information loss into attenuation bias. Together, these components provide a coherent
framework for estimating individual APPs, comparing peak-age patterns across sports and groups,
and quantifying the uncertainty in those comparisons. An accompanying R package implements
the proposed method.
     This formulation also has a natural connection to several areas of statistical methodology. In
failure-time settings, an event time may be right-, left-, or interval-censored (Klein and Moeschberger,
2003), and a large literature has developed regression methods for censored or interval-censored out-
comes (Turnbull, 1976; Finkelstein, 1986; Tian and Cai, 2006; Zhang and Sun, 2010). Standard
joint models link longitudinal biomarkers to externally observed clinical event times, such as death,
disease progression, or injury (Wulfsohn and Tsiatis, 1997; Wu et al., 2008; Brilleman et al., 2019;
Liu et al., 2026), and related ideas have also appeared in sports settings involving longitudinal
measurements and time-to-injury outcomes (Nielsen et al., 2019); see Wang and Zhong (2025) for
a recent overview. In contrast, APP is not an externally occurring event time observed through a
censoring mechanism. It is a latent functional, τi = arg maxt Yi (t), of an unobserved performance
trajectory. The proposed framework also shares features with multi-path or hierarchical change-
point models (Joseph and Wolfson, 1992), but the target here is not a structural breakpoint; it is
the timing of optimal performance defined by a smooth latent trajectory.
     The remainder of the paper is organized as follows. Section 2 introduces the World Athletics
data example that motivates the proposed framework. Section 3 presents the joint model, including
trajectory specifications, the peak-age submodel, and Bayesian inference. Section 4 applies the
model to the athletics data, Section 5 reports simulation studies comparing the proposed method
with conventional approaches, and Section 6 concludes with limitations and future directions.


2        Motivating Athletics Data Example
Before introducing the model, we first describe the athletics data example that motivates the
inferential problem. The purpose of this example is not only to provide the empirical setting for
the application, but also to make concrete the challenges described in the Introduction: performance
is observed at irregular competition ages, observation windows are often incomplete, and the age
of the best recorded performance need not coincide with the latent peak age of scientific interest.
    The motivating dataset consists of elite athletics performance records obtained from the World
Athletics all-time rankings database. The original records are publicly available from the official
World Athletics website1 , which compiles historical results from international competitions across
events. To facilitate data access and reproducibility, we used a curated dataset available on Kaggle2 ,
which was constructed by programmatically collecting the official rankings pages. Since the dataset
is a direct scrape of the World Athletics database without modification of the underlying records,
it provides a convenient and reproducible snapshot of the official data source used in this study.
Because all-time ranking lists include only performances that meet the ranking criteria, the observed
    1
        https://worldathletics.org/records/all-time-toplists
    2
        https://www.kaggle.com/datasets/jeannicolasduval/world-athletics-all-time-rankings


                                                     3
records primarily consist of high-level performances and may not capture every competition in an
athlete’s career.
    The dataset contains athlete-level performance records across multiple athletics disciplines.
Each entry corresponds to a competition result and includes the athlete name, date of birth, event,
performance score, and competition date. Performance in athletics events is measured using the
World Athletics scoring tables, which convert raw results, such as time or distance, into a standard-
ized performance score that allows comparisons across events (Spiriev and Spiriev, 2000). These
scoring tables are widely used in multi-event competitions such as the decathlon and heptathlon
to aggregate performances across disciplines. For each athlete, multiple observations are typically
available across different ages, forming an irregular longitudinal trajectory over the observed record
window of their career. To capture heterogeneity in age-related performance development across
athletics disciplines, we selected ten representative events spanning substantially different physio-
logical and technical demands: 100 metres, 400 metres, 1500 metres, marathon, long jump, shot put,
discus throw, javelin throw, decathlon (men), and heptathlon (women). To facilitate interpreta-
tion, these events are further grouped into six broader categories reflecting similar physiological and
technical characteristics: sprints (100 m and 400 m), middle-long distance (1500 m), road running
(marathon), jumps (long jump), throws (shot put, discus throw, and javelin throw), and combined
events (decathlon (men) and heptathlon (women)). Both men’s and women’s records were included
when available, with decathlon and heptathlon treated as sex-specific combined events.
    We applied minimal preprocessing to construct athlete-level longitudinal records for trajectory
modeling. Athlete identifiers were based on name and date of birth; duplicate records and two
likely linkage errors were removed. Athletes without a recorded date of birth were assumed to be
missing completely at random and excluded (0.03% of the dataset), and July 1 was used when only
birth year was available. We retained athletes with at least ten recorded competitions and focused
on those appearing in a single selected event. Among athletes meeting the ten-record threshold, 366
appeared in multiple selected events and were excluded. Such athletes raise important questions
about event-specific trajectories, within-athlete dependence, and event transitions, which we leave
to future work. After preprocessing, the analysis dataset contains 105,515 records from 3,229 single-
event athletes, with one longitudinal trajectory per athlete; event-level summaries are provided in
Supplementary Table S1.
    Figure 1 gives a more direct view of these challenges at the athlete level. The selected records
show that observed performances can be sparse and irregular over age, and that the best observed
performance may occur near the beginning or end of the observed record window. These patterns
visually reinforce the distinction made in the Introduction between an observed or pseudo peak age
and the latent peak age defined by the underlying performance trajectory.
    Taken together, the World Athletics records provide a rich but incomplete longitudinal view of
athlete development over age. They motivate a model that can borrow information across athletes
and sports, reconstruct smooth athlete-specific trajectories from irregular observations, and treat
peak age as a latent quantity rather than as a directly observed competition age. We now formalize
this modeling problem.


3     A Joint Modeling Framework
3.1   Notation and Modeling
Let i = 1, . . . , I index athletes and j = 1, . . . , ni index observed performance outcomes. Denote
by yij the observed performance score at age tij . We let xi denote athlete-level covariates (e.g.,
biological sex, sport, birth cohort) and zij denote competition-level covariates such as wind speed,

                                                  4
                                                                     Illustrative longitudinal performance records and inferential challenges
                                 Informative window                  Sparse records                                              Informative window                   Sparse records                                                Informative window                  Sparse records
                                       400 m                             100 m                                                         1500 m                            1500 m                                                           Discus                           Discus


                     1300                 Observed best                    Observed best                                                 Observed best                      Observed best                                                   Observed best                     Observed best
                                                                                                                                                                                                                        1300
                                                                                                                     1300
 Performance score




                                                                                                 Performance score




                                                                                                                                                                                                    Performance score
                     1200                                                                                                                                                                                               1200
                                                                                                                     1200




                     1100                                                                                                                                                                                               1100

                                                                                                                     1100




                                                                                                                                                                                                                        1000
                                 Best near boundary                 Late-entry window                                            Best near boundary                  Late-entry window                                              Best near boundary                 Late-entry window
                                       400 m                              100 m                                                        1500 m                              1500 m                                                        Shot put                            Discus


                     1300                      Observed best                     Observed best                                             Observed best                       Observed best                                                      Observed best                     Observed best
                                                                                                                                                                                                                        1300
                                                                                                                     1300
 Performance score




                                                                                                 Performance score




                                                                                                                                                                                                    Performance score
                     1200                                                                                                                                                                                               1200
                                                                                                                     1200




                     1100                                                                                                                                                                                               1100

                                                                                                                     1100




                                                                                                                                                                                                                        1000
                            20      25   30       35    40     20     25    30      35     40                               20      25      30     35      40   20     25      30     35       40                              20      25    30     35      40    20     25   30    35        40
                                         Age                               Age                                                             Age                                Age                                                           Age                               Age




Figure 1: Observed performance records for selected elite male athletes across event types. Each
panel shows one athlete. The examples illustrate sparse or irregular records, incomplete age win-
dows, and best recorded performances near the boundary of the observed age range. Dashed vertical
lines mark the age of the best recorded performance, which may differ from the latent peak age.

when available. Competition-level covariates zij adjust performance at a specific competition,
whereas athlete-level covariates xi enter the hierarchical distributions of athlete-specific trajectory
parameters and latent peak age.
    We model the longitudinal component of performance using a subject-specific smooth trajectory
with additive residual variation. In the notation introduced in Section 1, this latent age-performance
trajectory is parameterized as Yi (t) = µ(t; θ i , τi ). Conditional on latent trajectory parameters and
covariates, observed performances are assumed independent across competitions. Specifically,
                                                                        yij = µ(tij ; θ i , τi ) + δ ⊤ zij + εij ,                                                                   εij ∼ N (0, σy2 ),                                                                                       (1)
    In (1), εij denotes the remaining residual variation after adjusting for observed competition-level
covariates through δ ⊤ zij . µ(·) is a prespecified trajectory family, the random vector θ i governs the
shape of the individual performance curve (e.g., growth and decline rates), and τi represents the age
at which the trajectory attains its maximum. The vector δ captures fixed effects of competition-
level covariates zij .
    Between-athlete heterogeneity is modeled hierarchically through
                                                                                                                            θ i | xi ∼ Fθ (· | xi ; ψ θ ),                                                                                                                                    (2)
where Fθ is a conditional distribution for the athlete-specific trajectory parameters and ψ θ collects
the corresponding population-level parameters. This notation is intended to keep the framework

                                                                                                                                                           5
modular: the components of θ i and the distribution Fθ may be chosen to match a particular
trajectory parameterization. For example, a normal random-effects specification is

                             θ i = θ 0 + Bxi + bi ,       bi ∼ MVN(0, Σθ ),

where θ 0 represents baseline trajectory parameters, B links athlete-level covariates xi to trajectory
characteristics, and bi captures residual subject-specific deviations. Under this normal special case,
ψ θ = (θ 0 , B, Σθ ), and the covariance structure of Σθ can be specified to reflect dependence among
the components of θ i .
    A central scientific objective of this study is to understand how athlete-level characteristics are
associated with earlier or later peak performance development. To quantify covariate effects on
peak age, we specify a parametric submodel for the latent peak age τi . This submodel is embedded
within the joint longitudinal framework so that inference on τi and its covariate effects is based on
the full observed performance trajectory, rather than on the empirically observed best performance
alone. This distinction is especially important when the observed window provides only partial
information about the location of the peak. In particular, we adopt an accelerated failure time
(AFT) formulation
                               log(τi ) = β0 + β ⊤ xi + ei , ei ∼ N (0, στ2 ),                      (3)
so that τi | xi follows a lognormal distribution. Here, β0 represents a baseline peak age on the
log scale, while β captures how athlete-level covariates shift peak age multiplicatively. The vari-
ance parameter στ2 reflects residual heterogeneity in peak age that is not explained by observed
covariates. Notably, although we focus on the lognormal AFT model for concreteness, alternative
parametric specifications such as proportional hazard models can be incorporated within the same
joint framework.

3.2   Specification of the performance trajectory function
Because peak age is defined as the maximizer of an athlete-specific performance trajectory, we
use parametric longitudinal curves in which peak age can be represented directly as a trajectory
parameter. This provides an interpretable way to infer τi from irregular and noisy performance
records and to link it to athlete-level covariates. The proposed framework is modular with respect
to the choice of the trajectory function µ(·). We consider two parametric specifications that differ
in flexibility and interpretability.

Symmetric quadratic model           A simple and interpretable specification assumes a symmetric
quadratic trajectory,
                                     µ(t; α, ρ, τ ) = α − ρ(t − τ )2 ,                             (4)
where α represents the peak performance level, ρ > 0 controls the curvature of the trajectory and
implies how rapidly performance changes with age, and τ denotes the peak age. This formulation
is widely used in sports science (e.g. Guan and Swartz (2024)) due to its parsimony, interpretabil-
ity, and empirical adequacy in many applications. In particular, the quadratic form provides a
convenient summary of peak level, peak age, and overall curvature within a low-dimensional pa-
rameterization. However, it imposes symmetry around the peak, implicitly assuming that the rate
of performance improvement before the peak mirrors the rate of decline afterward. Such symme-
try may not hold in sports where developmental progression and post-peak aging follow different
dynamics.



                                                      6
Asymmetric quadratic model                To allow distinct rates of improvement and decline, we extend
the quadratic form to                                   (
                                                         α − ρL (τ − t)2 , t ≤ τ,
                                µ(t; α, ρL , ρR , τ ) =                                                          (5)
                                                         α − ρR (t − τ )2 , t > τ,
where ρL and ρR are positive parameters that govern the pre-peak and post-peak curvature, respec-
tively. This specification accommodates asymmetric developmental patterns commonly observed
in athletic performance. Although the trajectory is defined piecewise, it remains continuous and
differentiable at the peak age τ , while allowing the curvature to differ before and after the peak.
For example, in sprint events, athletes may experience rapid performance improvement during early
developmental years, whereas performance decline after the peak often occurs more gradually. In
the notation of the general model, the latent trajectory parameter vector is θ i = (αi , ρi )⊤ under
the symmetric quadratic specification and θ i = (αi , ρLi , ρRi )⊤ under the asymmetric quadratic
specification, with τi as the latent peak age in both cases.
    The parameters αi , ρLi , ρRi , and τi provide interpretable athlete-specific summaries of peak
level, pre-peak development, post-peak decline, and peak age, respectively. These quantities may
vary systematically across sports, since sprint, endurance, and technical events can involve dif-
ferent developmental patterns, peak ages, and aging dynamics. This consideration will guide the
application-specific model specification in later sections, where sport-specific effects are incorpo-
rated into multiple components of the joint model.

3.3    Joint likelihood formulation
We now make explicit the likelihood structure implied by the proposed model. For athlete i, let
yi = (yi1 , . . . , yini )⊤ denote the observed longitudinal outcomes, and zi = (zi1 , . . . , zini ) denote
the corresponding competition-level covariates. The conditional density of yi , given the latent
trajectory parameters θ i , latent peak age τi , and covariates, can be written as
                                                                                                             
                                                              1 X ni
                                                                                                            
                                                                                                            2
        fy (yi | θ i , τi , zi ; δ, σy ) = (2πσy2 )−ni /2 exp − 2      yij − µ(tij ; θ i , τi ) − δ ⊤ zij       . (6)
                                                              2σy                                            
                                                                   j=1

   The latent trajectory parameters (θ i , τi ) are assumed independent across athletes conditional
on covariates and global parameters (ψ θ , β0 , β, στ ). Given athlete-level covariates xi and shared
model parameters, let fθ and fτ denote the conditional densities of the latent trajectory parameters
and latent peak age, respectively. Under the normal random-effects specification in (2) and the
lognormal AFT specification in (3),

                           fθ (θ i | xi ; ψ θ ) = ϕMVN (θ i ; θ 0 + Bxi , Σθ ) ,                                 (7)
                                                                  (                           )
                                                       1             (log τi − β0 − β ⊤ xi )2
                    fτ (τi | xi ; β0 , β, στ ) =       √ exp −                                  .                (8)
                                                  τi στ 2π                       2στ2

More generally, fθ denotes the density induced by the chosen conditional distribution Fθ in (2). In
(7), ϕMVN (·; µ, Σ) denotes the multivariate normal density with mean µ and covariance matrix Σ.
     Let Θ = (δ, σy , ψ θ , β0 , β, στ ) collect all unknown global parameters. Under a concrete choice of
Fθ , ψ θ is replaced by the corresponding distributional parameters, such as (θ 0 , B, Σθ ) in the normal
special case. We assume that, conditional on covariates and Θ, the latent trajectory parameters are
independent across athletes according to fθ , the AFT errors {ei }Ii=1 are independent across athletes
according to (3), and the measurement errors {εij : i = 1, . . . , I; j = 1, . . . , ni } are independent

                                                         7
across observations; the trajectory and peak-age components are also conditionally independent
given the covariates and shared parameters. If the latent variables (θ i , τi ) were observed, the
complete-data likelihood contribution for athlete i would be
           (c)
         Li (Θ | yi , θ i , τi , xi , zi ) = fy (yi | θ i , τi , zi ; δ, σy ) fθ (θ i | xi ; ψ θ ) fτ (τi | xi ; β0 , β, στ ).    (9)

      However, the latent quantities (θ i , τi ) are not directly observed in practice. Assuming indepen-
dence across athletes, the observed-data likelihood based on D = {(yij , tij , zij , xi ) : i = 1, . . . , I; j =
1, . . . , ni } is therefore obtained by integrating out the latent trajectory parameters and latent peak
ages. For notational simplicity, we suppress the dependence of the component densities on shared
model parameters in the following expression.
                                       I Z
                                       Y          Z ∞                                                               
                     (o)
                 L         (Θ | D) =                    fy (yi | θ i , τi , zi ) fθ (θ i | xi ) fτ (τi | xi ) dτi dθ i ,         (10)
                                       i=1   Sθ   0

where Sθ denotes the support of the athlete-specific latent trajectory parameters. This likelihood
is not a standard survival likelihood for directly censored or truncated event times. Instead, incom-
plete observation windows affect inference through the longitudinal component fy , and uncertainty
about τi is propagated by integrating over the latent trajectory parameters and latent peak age.
    In general, the integrals in (10) do not admit closed-form expressions. We therefore adopt a
Bayesian estimation framework, which provides a coherent approach for inference in hierarchical
latent-variable models and yields full uncertainty quantification for both trajectory parameters and
peak ages. Bayesian methods are increasingly used in sports analytics, particularly in settings
involving multi-level performance data, partial career records, and complex dependency structures.
In addition, sports science applications often benefit from incorporating substantive prior knowl-
edge regarding performance development, physiological constraints, or sport-specific characteristics.
Some recent examples include Peng et al. (2024); Tea and Swartz (2023); Peng et al. (2022); D’Urso
et al. (2023); Dolmeta et al. (2023); Hecksteden et al. (2022).

3.4    Simultaneous Bayesian inference for parameter estimation
From a Bayesian perspective, the proposed framework constitutes a hierarchical latent-variable
model that jointly estimates population-level parameters, athlete-specific trajectory parameters,
and latent peak ages. This avoids a two-stage analysis in which individual peak ages are first
estimated from fitted performance curves and then treated as observed outcomes. The hierarchy
naturally reflects the data-generating mechanism described in the previous section. At the first
level, the longitudinal outcomes yi are modeled conditionally on athlete-specific latent trajectory
parameters, latent peak age, competition-level covariates, and observation-model parameters. At
the second level, the latent trajectory parameters are modeled through regression structures on
covariates xi , inducing trajectory-distribution parameters ψ θ (for example, (θ 0 , B, Σθ ) under the
normal special case) for θ i and (β0 , β, στ ) for τi .
    Specifically, the hierarchical structure can be summarized in compact form as

                                                  yi | θ i , τi , zi , δ, σy ∼ fy (·),

                                             θ i | xi ∼ fθ (·),         τi | xi ∼ fτ (·),
as defined in (6)–(8).



                                                                   8
    Under the Bayesian framework, inference proceeds by combining the likelihood with prior dis-
tributions on the global parameters Θ. Let π(Θ) denote the joint prior density. The joint posterior
distribution of all unknown quantities, including the latent variables, is proportional to
                                               " I                                  #
                                               Y (c)
                                     I
                     π Θ, {θ i , τi }i=1 | D ∝     Li (Θ | yi , θ i , τi , xi , zi ) π(Θ),     (11)
                                                i=1

        (c)
where Li (Θ | ·) is the complete-data likelihood defined in (9).
   Marginal posterior inference for Θ is obtained by integrating out the latent variables,
                                        Z                               I
                                                                       Y
                           π(Θ | D) =       π Θ, {θ i , τi }Ii=1 | D         dθ i dτi ,
                                                                       i=1

which mirrors the observed-data likelihood formulation in (10). In practice, direct evaluation of
these high-dimensional integrals is computationally infeasible. We therefore draw samples from
the joint posterior (11) using Markov chain Monte Carlo (MCMC) methods, treating the latent
variables (θ i , τi ) as additional unknowns.
     An important advantage of this simultaneous Bayesian inference is that it provides direct pos-
terior inference for the latent peak ages. In particular, for each athlete, the posterior distribution
π(τi | D) summarizes both the estimated peak age and its uncertainty, rather than reducing the
athlete’s longitudinal record to a single estimated peak age. This is especially useful for athletes
with sparse, noisy, or incomplete performance records, including cases in which the true peak may
lie outside the observed age range. The resulting posterior uncertainty for τi is propagated naturally
into inference on population-level peak-age effects, such as the regression coefficients β.
     In practical implementation, a joint prior distribution is assigned to the global parameters Θ
to complete the Bayesian specification. Since the proposed framework is intended to accommodate
a range of trajectory specifications and application contexts, we adopt weakly informative pri-
ors reflecting plausible ranges of athletic performance characteristics while maintaining sufficient
flexibility for the data to dominate inference.
     The specific prior choices and computational implementation used for the empirical analysis are
described in Section 4, where we apply a particular specification of the proposed framework to the
motivating athletics data introduced in Section 2.


4     Application to World Athletics Data
4.1   Model and prior specifications for the application
Using the World Athletics data described in Section 2, the model used in this application is a
specific instantiation of the general framework introduced in Section 3, with a parameterization
tailored to the structure of athletics performance data.
    In this application, the athlete-level covariates include sport category, biological sex, birth
year, and, for the peak-age submodel, sport-by-sex interactions. Because sprints, middle-long
distance, road running, jumps, throws, and combined events may differ in peak performance levels,
developmental rates, post-peak decline, and peak age, we allow sport-category effects to enter
multiple components of the model. In the notation of the general framework, this application
uses the asymmetric quadratic trajectory in (5) and takes the athlete-specific trajectory parameter
vector to be θ i = (αi , log ρLi , log ρRi )⊤ , corresponding to peak level, log pre-peak curvature, and


                                                      9
log post-peak curvature, respectively. Thus, the model below is a concrete special case of (1), (2),
and (3), with Fθ specified through the random effects for αi , log ρLi , and log ρRi .
    For athlete i and competition j, the observed performance score is modeled as

                                         yij = µ(tij ; αi , ρLi , ρRi , τi ) + εij ,    εij ∼N (0, σy2 ),
                                                (
                                                 αi − ρLi (τi − t)2 , t ≤ τi ,
                   µ(t; αi , ρLi , ρRi , τi ) =
                                                 αi − ρRi (t − τi )2 , t > τi ,
                                                        (α)          (α)
                                        αi = α0 + ηsport[i] + ui ,
                                                              (L)           (L)
                                  log ρLi = log ρL0 + ηsport[i] + ui ,
                                                                                                             (12)
                                                              (R)           (R)
                                  log ρRi = log ρR0 + ηsport[i] + ui ,
                                                       (τ )
                                  log(τi ) = β0 + ηsport[i] + βS Femalei + βY BirthYeari
                                                   (τ S)
                                               + ηsport[i] Femalei + ei ,
                                             (α)                      (L)
                                           ui ∼ N (0, σα2 ),        ui      ∼ N (0, σL2 ),
                                            (R)         2 ),
                                           ui ∼ N (0, σR                 ei ∼ N (0, στ2 ).

    As in the asymmetric trajectory specification in Section 3, αi denotes latent peak performance,
ρLi and ρRi denote pre- and post-peak curvature, and τi denotes latent peak age.
    The variable Femalei indicates female biological sex.
                           (α)    (L)        (R)
    The random effects ui , ui , and ui capture athlete-level heterogeneity in peak level and in
the two log-curvature components; the log-scale curvature parameterization enforces positivity and
                                                                                                (α) (L) (R)
improves numerical stability. More generally, the four athlete-level deviations (ui , ui , ui , ei )
could be modeled jointly using a multivariate normal distribution to account for residual correlations
among peak level, pre-peak curvature, post-peak curvature, and peak age.
    The sport-category terms are modeled as fixed effects relative to a reference category. The
six sport categories are sprints, middle-long distance, road running, jumps, throws, and combined
events, with middle-long distance used as the reference category. Sport category effects are incor-
                    (α)       (L)            (R)
porated through ηsport[i] , ηsport[i] , and ηsport[i] , while peak age is modeled through an accelerated
failure time structure with covariates including sport category, biological sex, birth year, and sport-
                                    (α)       (L)        (R)            (τ )
by-sex interactions. The terms ηsport[i] , ηsport[i] , ηsport[i] , and ηsport[i] are sport-category fixed effects,
           (τ S)
whereas ηsport[i] represents sport-by-sex interaction effects in the peak-age submodel.
    Competition-level covariates zij are not included in this application, since no such variables
are consistently available across all events considered here. However, the general framework allows
such covariates to be incorporated when appropriate data are available.
    This hierarchical specification allows information to be shared across athletes within sport
categories, helping stabilize inference for athletes with sparse or incomplete longitudinal records.
Weakly informative priors are assigned to all global parameters. The priors are chosen to encode
broad plausible ranges while allowing the likelihood to dominate when the data are informative;
for example, the baseline peak-age intercept is centered at log(28) with standard deviation 0.5,
reflecting a wide prior range for typical elite peak ages on the original age scale. Similarly, curvature
parameters are assigned priors on the log scale to enforce positivity while allowing substantial
variation in trajectory shape. The full prior specification is provided in the Supplementary Material.


                                                              10
4.2   Model fit and reconstructed performance trajectories
Posterior inference was carried out using MCMC implemented in Stan. We ran 4 parallel chains
with 1000 warm-up iterations followed by 2000 sampling iterations per chain. Table 1 provides an
overall summary of the posterior estimates for the key model parameters, including the baseline
trajectory parameters, covariate effects, and variance components.

Table 1: Posterior means and 95% credible intervals for key parameters in the application-specific
model. Male middle-long distance athletes are the reference group. Parameters are grouped by
peak level, curvature, peak age, and variance components.

                            Parameter                             Parameter
           Parameter Mean        95% CrI                Parameter Mean 95% CrI
           Peak-level submodel
                                                         (α)
           α0           1166.933 (1164.720, 1169.132)   ηcombined   0.823     (-9.648, 11.405)
             (α)                                         (α)
           ηsprint      0.254    (-2.591, 2.963)        ηthrows     -26.734 (-29.535, -23.948)
             (α)                                         (α)
           ηroad        13.010   (8.556, 17.348)        ηjumps      3.893     (-0.160, 8.018)
           Peak-age main effects                        Sport-by-sex interactions
                                                         (τ S)
           β0           3.185    (3.146, 3.224)         ηcombined   -0.029 (-0.154, 0.094)
                                                         (τ S)
           βS           0.082    (0.049, 0.117)         ηsprint     -0.044 (-0.084, -0.003)
                                                         (τ S)
           βY           0.049    (0.014, 0.083)         ηthrows     -0.035 (-0.076, 0.004)
             (τ )                                        (τ S)
           ηcombined    0.004    (-0.105, 0.106)        ηroad       -0.069 (-0.155, 0.018)
             (τ )                                        (τ S)
           ηsprint      -0.103   (-0.138, -0.067)       ηjumps      0.013     (-0.040, 0.067)
             (τ )
           ηthrows      0.044    (0.011, 0.079)
             (τ )
           ηroad        0.085    (0.009, 0.158)
             (τ )
           ηjumps       -0.088   (-0.135, -0.042)
           Curvature submodel
           log ρL0      -0.951   (-1.198, -0.715)       log ρR0     -2.704   (-3.093, -2.335)
             (L)                                          (R)
           ηcombined    0.619    (-0.026, 1.251)        ηcombined   0.187    (-0.723, 1.055)
             (L)                                          (R)
           ηsprint      1.098    (0.820, 1.379)         ηsprint     -0.347   (-0.765, 0.064)
             (L)                                          (R)
           ηthrows      0.719    (0.456, 0.980)         ηthrows     1.032    (0.650, 1.431)
             (L)                                          (R)
           ηroad        -0.458   (-1.058, 0.164)        ηroad       -0.534   (-1.164, 0.099)
             (L)                                          (R)
           ηjumps       0.735    (0.357, 1.112)         ηjumps      0.347    (-0.117, 0.817)
           Variance parameters
           σy           24.922   (24.814, 25.033)       στ          0.099    (0.093, 0.105)
           σα           27.852   (27.091, 28.609)       σL          0.804    (0.737, 0.876)
           σR           1.563    (1.420, 1.719)

    Overall, the posterior estimates are well identified and support meaningful statistical infer-
ence on both trajectory dynamics and peak-age effects. In particular, the variance components
associated with the athlete-specific random effects are clearly non-negligible. The estimated stan-
dard deviations for the random effects in peak level, pre-peak curvature, and post-peak curvature
are σα = 27.9 (95% credible interval (CrI): 27.1, 28.6), σL = 0.80 (95% CrI: 0.74, 0.88), and
σR = 1.56 (95% CrI: 1.42, 1.72), respectively, all clearly different from zero. These results indicate
substantial between-athlete heterogeneity in both overall performance level and the rates of perfor-
mance evolution, and provide strong empirical support for incorporating random effects to capture
individual-level variation in performance trajectories.
    To further illustrate model fit at the athlete level, Figure 2 displays observed performance scores

                                                  11
together with the posterior mean trajectory and the corresponding 95% posterior predictive interval
for a random sample of 16 male athletes across different disciplines. The vertical dashed line marks
the posterior mean estimate of the peak age τi for each athlete.

                                  Random athlete: 1                   Random athlete: 2                    Random athlete: 3                   Random athlete: 4
                                   Event: 1500 m                       Event: Shot put                      Event: Shot put                     Event: Javelin
                                     Sex: Men                            Sex: Men                             Sex: Men                            Sex: Men
 Performance score




                     1200



                     1100




                                  Random athlete: 5                   Random athlete: 6                    Random athlete: 7                   Random athlete: 8
                                   Event: 1500 m                       Event: Javelin                        Event: Discus                       Event: 400 m
                                     Sex: Men                            Sex: Men                              Sex: Men                           Sex: Men
 Performance score




                     1200



                     1100




                                  Random athlete: 9                   Random athlete: 10                   Random athlete: 11                  Random athlete: 12
                                   Event: 1500 m                       Event: Long jump                     Event: Long jump                     Event: 400 m
                                     Sex: Men                             Sex: Men                             Sex: Men                            Sex: Men
 Performance score




                     1200



                     1100




                                  Random athlete: 13                  Random athlete: 14                   Random athlete: 15                  Random athlete: 16
                                    Event: Discus                       Event: Discus                       Event: Marathon                      Event: 400 m
                                      Sex: Men                            Sex: Men                             Sex: Men                            Sex: Men
 Performance score




                     1200



                     1100




                             20     25         30      35   40   20     25         30      35    40   20     25         30      35   40   20     25         30      35   40
                                         Age                                 Age                                  Age                                 Age




Figure 2: Observed scores, posterior mean trajectories, and 95% posterior predictive intervals for
16 randomly selected male athletes. Solid curves show posterior mean latent trajectories, shaded
bands show posterior predictive intervals, and dashed vertical lines mark posterior mean peak ages.

    Across athletes with dense, sparse, or age-limited records, the fitted curves provide reasonable
reconstructions of performance trajectories and plausible peak-age estimates.

4.3                         Covariate effects on peak age
The regression structure in the peak-age submodel (3) allows direct statistical inference on factors
associated with the timing of peak performance. Table 1 summarizes posterior estimates for all
model parameters, while Figure 3 displays the posterior means and 95% credible intervals for
sport-category and biological-sex effects on log peak age, expressed relative to the male middle-
long distance reference group.
   Figure 3 shows two main patterns in the estimated sport-category and biological-sex effects
on peak age. First, estimated peak age varies systematically across sport categories. Sprint and
jumping events show clearly earlier peak ages compared with middle-long distance events, while
road running and throwing events tend to exhibit later peak ages, with the road-running effect
most clearly separated from the middle-long reference group among men. These patterns are
consistent with physiological differences across disciplines, where explosive power events typically


                                                                                                12
                                  Men       Women




                    Middle-long




                        Sprints




                        Throws




                  Road running




               Combined events




                        Jumps



                                    -0.1                     0.0               0.1
                                        Effect on log peak age relative to male middle-long


Figure 3: Posterior mean effects on log peak age from the accelerated failure time submodel by
sport category and biological sex, relative to male middle-long distance athletes. Points and hori-
zontal line segments show posterior means and 95% credible intervals. Negative and positive values
indicate earlier and later peak ages, respectively. The dashed vertical line marks zero effect.


favor earlier peak performance, whereas endurance- and technique-based events allow athletes to
remain competitive at older ages.
    Second, biological-sex differences in peak age are also evident. Across most sport categories,
female athletes tend to exhibit slightly later peak ages than male athletes, although the magnitude
of this difference varies by discipline.
    This pattern contrasts with the common expectation that female athletes peak earlier due to
earlier biological maturation. One possible explanation is that the present analysis focuses on
elite competition records, where peak performance reflects not only physiological development but
also career dynamics such as selection, participation pathways, and competitive longevity. For
instance, female athletes may maintain elite-level competitiveness over longer periods or achieve
their highest-ranked performances at slightly older ages due to differences in career progression and
competitive structure.
    In addition to the sport and biological-sex effects shown in the figure, the estimated birth-year
coefficient is modestly positive (βY = 0.049, 95% CrI: 0.014 to 0.083). Birth year is rescaled to the
unit interval using the minimum and maximum birth years in the analysis sample, so βY compares
athletes at the latest observed birth year with those at the earliest observed birth year rather
than representing a one-year effect. On the original age scale, the posterior mean corresponds to


                                                        13
a multiplicative effect of e0.049 ≈ 1.050, or about a 5.0% higher peak age for athletes at the latest
versus earliest observed birth year. This modest positive estimate may reflect possible cohort-
related changes in training, competition opportunities, or athlete development pathways.
    Supplementary Figure S1 provides a complementary boxplot summary of athlete-level posterior
mean peak ages on the original age scale, showing the distribution of estimated peak ages by sport
category and biological sex.

4.4                                        Sport differences in improvement and decline rates
The proposed framework also enables comparisons of how performance evolves before and after
the peak across different sport categories. Posterior summaries of the curvature-related parameters
are reported in Table 1, while Figure 4 provides a visual summary of the sport-specific curvature
estimates.
    Figure 4A displays the posterior mean average performance trajectory for each sport category,
providing a direct visualization of how the fitted age-performance curves differ in peak level and
shape across sports. In Figure 4B, the horizontal axis represents the rising-side curvature ρL , which
governs the rate of performance improvement before the peak, and the vertical axis represents the
declining-side curvature ρR , which governs the rate of performance decline after the peak. Larger
curvature values correspond to more rapid changes in performance. The dashed line indicates
equality between the two curvature parameters, corresponding to a symmetric quadratic trajectory.

 A                                                                                 B




                                        1150
                                                                                   Posterior mean declining-side curvature
  Average posterior performance score




                                                                                                                             1.0

                                                                                                                                                                             Sport category
                                                                                                                                                                                 Middle-long
                                        1100
                                                                                                                                                                                 Sprints
                                                                                                                                                                                 Throws
                                                                                                                                                                                 Road running
                                                                                                                                                                                 Combined events

                                        1050                                                                                 0.5                                                 Jumps




                                        1000



                                                                                                                             0.0
                                               15   20   25   30    35   40   45                                                0.0           0.5               1.0
                                                              Age                                                                     Posterior mean rising-side curvature


Figure 4: Sport-specific trajectory shapes. Panel A shows posterior mean average performance
trajectories by sport category. Panel B shows posterior mean rising- and declining-side curvatures,
ρL and ρR ; larger values indicate faster improvement or decline. Points and line segments show
posterior means and 95% credible intervals. The dashed diagonal marks ρL = ρR , corresponding
to a symmetric quadratic trajectory.

                            Figure 4A suggests that sprinting and jumping events have relatively similar average trajectory

                                                                                                                             14
shapes, with rapid improvement before the peak followed by a more gradual post-peak decline.
Figure 4B clarifies that this pattern is most pronounced for sprints: sprinting events have the
largest rising-side curvature and among the smallest declining-side curvature estimates. Jumping
events also show relatively large rising-side curvature, but their declining-side curvature is higher
than that of sprints, indicating somewhat sharper post-peak changes.
    Middle-long distance and road-running events have smaller curvature parameters overall, es-
pecially road running, consistent with more gradual performance evolution and longer sustained
periods of high-level performance. Throwing events have relatively high curvature on both sides,
and the largest declining-side curvature among the sport categories, indicating sharper post-peak
changes than in the other events. Combined events show greater uncertainty, reflecting their smaller
sample size and higher variability. In addition, the observed asymmetry between improvement
and decline rates across multiple sport categories provides empirical support for adopting a non-
symmetric performance trajectory specification.

4.5   Model diagnostics and software implementation
Convergence diagnostics for the MCMC algorithm, including trace plots and comparisons between
prior and posterior densities for key parameters, are provided in Section S4 of the Supplementary
Material. These results indicate stable sampling behavior and demonstrate that the data are
informative for the major model components. Additional checks on bias, uncertainty calibration,
incomplete observation windows, trajectory misspecification, and individual peak-age estimation
are provided in the simulation study in Section 5.
    To facilitate reproducibility and future applications, the proposed methodology has been im-
plemented in an R package supporting both symmetric and asymmetric trajectory specifications
considered in this study. The package provides functions for fitting the joint model, summarizing
posterior peak-age estimates, extracting athlete-level quantities, and visualizing fitted performance
trajectories. An anonymized version will be made available for review, and the public repository
will be released upon acceptance.


5     Simulation study
5.1   Simulation design
Our simulation study is designed to mirror the main challenges in the empirical application, in-
cluding noisy longitudinal measurements, irregular observation times, and incomplete observation
windows. We focus on three aspects of performance: (i) bias and variability of covariate effect esti-
mates in the peak-age model; (ii) the quality of uncertainty quantification, assessed by agreement
between Monte Carlo variability and reported standard errors or posterior uncertainty; and (iii)
sensitivity to incomplete observational windows, measured by how often the true peak age τi lies
within the observed age range. Here, Monte Carlo variability refers to the empirical variability of
estimates across repeated simulated datasets, whereas reported standard errors or posterior stan-
dard deviations quantify the uncertainty reported by the method within each dataset. Agreement
between these quantities provides a check on whether the method yields calibrated uncertainty
estimates.
    The data-generating procedure is summarized in Supplementary Algorithm S1. In each setting,
we generate datasets with I = 200 athletes and summarize results over 200 replications. Peak
ages are generated from a lognormal AFT model with true parameters β0 = 3.20, β1 = 0.01,
β2 = 0.05, and στ = 0.10, while athlete-specific performance trajectories are generated under


                                                 15
either a symmetric or asymmetric quadratic form. Unless otherwise stated, covariates, AFT errors,
trajectory parameters, observation windows, and measurement errors are generated independently
across athletes and observations. To assess sensitivity to incomplete observation, we consider
three observation-window settings in which the true peak age falls within the observed age range
with probability approximately 90%, 70%, or 50%. The asymmetric data-generating mechanism
uses smaller pre-peak curvature and larger post-peak curvature, corresponding to slower pre-peak
improvement and faster post-peak decline. This scenario is intended as a stress test of trajectory
misspecification rather than as a direct reproduction of the empirical pattern observed in the
athletics application.
    We compare the proposed joint model with two baseline approaches reflecting common practice.
The first is a pseudo-peak method (Naive 1), which defines peak age as the age at best observed
performance and uses it as the response in a lognormal AFT regression. The second is a two-stage
approach (Naive 2). In stage 1, we fit the trajectory model to the longitudinal observations and
extract the estimated peak age τ̂i for each athlete. In stage 2, these estimated peak ages are used as
responses in the same lognormal AFT regression as Naive 1. Thus, Naive 2 uses the same type of
trajectory information as the proposed method, but it first estimates peak ages from fitted trajec-
tories and then treats those estimates as observed outcomes in a separate regression. In contrast,
the proposed joint model estimates trajectories, latent peak ages, and AFT regression parame-
ters simultaneously, so uncertainty in τi is propagated into regression inference. We evaluate bias,
Monte Carlo standard deviation, and average reported standard errors or posterior standard devi-
ations for the regression coefficients. We also assess the accuracy of individual peak-age estimation
using interval coverage for τi , where applicable. Although inference is Bayesian, these metrics are
computed from a repeated-sampling perspective to examine frequentist operating properties of the
proposed method.

5.2   Simulation results
Before presenting the numerical results, we clarify the trajectory-specification labels used in Tables 2
and 3. For methods that explicitly model performance trajectories, namely the proposed method
and Naive 2, the rows labeled “Correct” correspond to data generated from the symmetric quadratic
trajectory and fitted with the symmetric trajectory model. The rows labeled “Wrong” correspond to
data generated from the asymmetric quadratic trajectory but fitted with the symmetric trajectory
model. Thus, “Wrong” refers specifically to fitting a symmetric trajectory model to asymmetric
trajectory data; other conceptually correct combinations, such as fitting the asymmetric model to
symmetric or asymmetric data, are not reported.
    Table 2 summarizes the simulation results across the three settings. For each parameter, entries
are reported as the Monte Carlo mean estimate across replications, with the Monte Carlo stan-
dard deviation in parentheses and the average posterior standard deviation in brackets. Results
are shown for both correctly specified and misspecified trajectory models under varying levels of
observational completeness.
    These two naive methods were implemented in R using standard procedures for AFT regression
and mixed-effects modeling. Naive 1 was implemented using survival::survreg() with a lognor-
mal AFT specification, whereas Naive 2 first fitted the mixed-effects quadratic trajectory model in
Stan via cmdstanr and then applied the same survival::survreg() lognormal AFT regression
to the estimated peak ages.
    Three main findings emerge. First, the proposed joint model gives less biased AFT regression
estimates across observation-window settings, especially for β1 and β2 . Naive 1 can perform reason-
ably when the observed window often contains the true peak, but its pseudo-peak response becomes


                                                  16
Table 2: Simulation summaries over 200 replications: Mean (SD) [Mean SE]. Mean and SD are
the Monte Carlo mean and standard deviation; Mean SE is the average reported standard error for
Naive 1 and Naive 2, and the posterior standard deviation for the proposed method.
                                                                               √      For the naive
AFT regressions, the model-based standard error of log στ is approximately 1/ 2I = 0.05 because
I = 200. Spec denotes the misspecification contrast in Section 5: Correct is symmetric data fitted
with the symmetric trajectory model, and Wrong is asymmetric data fitted with the symmetric
trajectory model. The dot for Naive 1 indicates that no trajectory model is fitted. True values are
β0 = 3.20, β1 = 0.01, β2 = 0.05, and log στ = −2.30.

Method     Spec               β0                          β1                            β2                        log στ

Setting 1: 90% peak coverage
Naive 1     ·       3.206 (0.0280) [0.0280]   0.00714 (0.00387) [0.00412]   0.03370 (0.03205) [0.03100]   -1.755 (0.0481) [0.0500]
Naive 2     Correct 3.221 (0.0154) [0.0123]   0.00557 (0.00200) [0.00183]   0.02808 (0.01440) [0.01375]   -2.572 (0.1065) [0.0500]
Naive 2     Wrong 3.160 (0.0133) [0.0099]     0.00417 (0.00162) [0.00147]   0.02107 (0.01178) [0.01109]   -2.791 (0.1300) [0.0500]
Proposed Correct 3.200 (0.0231) [0.0225]      0.00964 (0.00327) [0.00325]   0.04997 (0.02539) [0.02487]   -2.307 (0.0866) [0.0879]
Proposed Wrong 3.141 (0.0212) [0.0211]        0.00832 (0.00304) [0.00301]   0.04295 (0.02337) [0.02321]   -2.455 (0.0986) [0.0968]

Setting 2: 70% peak coverage
Naive 1     ·       3.167 (0.0257) [0.0259]   0.00400 (0.00380) [0.00384]   0.02063 (0.02812) [0.02895]   -1.823 (0.0473) [0.0500]
Naive 2     Correct 3.229 (0.0163) [0.0102]   0.00369 (0.00179) [0.00151]   0.01891 (0.01241) [0.01136]   -2.772 (0.1703) [0.0500]
Naive 2     Wrong 3.160 (0.0149) [0.0083]     0.00417 (0.00147) [0.00123]   0.01415 (0.01003) [0.00922]   -2.986 (0.2005) [0.0500]
Proposed Correct 3.199 (0.0290) [0.0282]      0.00973 (0.00439) [0.00411]   0.05139 (0.03180) [0.03126]   -2.307 (0.1265) [0.1247]
Proposed Wrong 3.138 (0.0276) [0.0283]        0.00832 (0.00428) [0.00406]   0.04295 (0.03027) [0.03102]   -2.455 (0.1491) [0.1409]

Setting 3: 50% peak coverage
Naive 1     ·       3.120 (0.0245) [0.0238]   0.00249 (0.00353) [0.00353]   0.01390 (0.02671) [0.02661]   -1.908 (0.0474) [0.0500]
Naive 2     Correct 3.238 (0.0189) [0.0086]   0.00266 (0.00163) [0.00128]   0.01351 (0.01084) [0.00959]   -2.963 (0.2810) [0.0500]
Naive 2     Wrong 3.169 (0.0187) [0.0075]     0.00204 (0.00143) [0.00112]   0.01036 (0.00932) [0.00840]   -3.117 (0.3710) [0.0500]
Proposed Correct 3.202 (0.0352) [0.0349]      0.01016 (0.00564) [0.00512]   0.05325 (0.03860) [0.03863]   -2.320 (0.2026) [0.1877]
Proposed Wrong 3.130 (0.0388) [0.0400]        0.00976 (0.00621) [0.00579]   0.05254 (0.04224) [0.04415]   -2.360 (0.2671) [0.2362]



increasingly boundary-driven as peak coverage decreases. Naive 2 uses fitted trajectories and is
less sensitive to this boundary effect, but it still treats first-stage peak-age estimates as observed
responses.
    Second, incomplete observation is reflected differently across methods. In the naive analyses,
weaker peak-age information mainly appears as increased bias, while reported standard errors
change little or even decrease. In the joint model, the same loss of information appears mainly as
larger posterior standard deviations, because uncertainty about latent peak ages is carried into the
AFT regression.
    Third, trajectory misspecification remains important. All methods deteriorate when asymmetric
trajectories are fitted with a symmetric model, but the proposed method retains smaller AFT
coefficient bias. As shown below, interval coverage for individual τi is still limited by trajectory-
model adequacy.
    We also examined the accuracy of individual peak age estimation. Table 3 summarizes these
results over all athletes within each observation-window setting. Across settings, the pseudo-peak
approach (Naive 1) has substantially larger RMSE than the trajectory-based methods, reflecting the
instability of using the observed best-performance age as a proxy for τi . Naive 2 and the proposed
method give similar individual peak-age estimates because both use the longitudinal performance
records to reconstruct athlete-specific trajectories; nevertheless, the proposed method has slightly
smaller RMSE across all settings. Under correct trajectory specification, empirical coverage of the
95% intervals remains close to the nominal level, whereas under trajectory misspecification coverage
deteriorates for both trajectory-based methods. The higher coverage in the 50% misspecified setting


                                                               17
likely occurs because weaker peak-age information leads to wider intervals. Thus, individual τi
estimation is ultimately limited by the amount of trajectory information available for each athlete
and by trajectory-model adequacy. The advantage of the proposed joint model compared with
Naive 2 is therefore not mainly a large improvement in individual peak-age point estimation, but
that it propagates uncertainty in the latent peak ages into the AFT regression, whereas Naive 2
treats first-stage peak-age estimates as observed responses.

Table 3: Individual latent peak-age estimation across observation-window settings, summarized
over all athletes. RMSE is the root mean squared error of posterior mean or point estimates of τi .
Cov. is the empirical coverage of 95% intervals for τi over 200 replications. Spec uses the same
misspecification contrast as Table 2. Coverage is not applicable for Naive 1 because it does not
produce individual peak-age intervals.

                                               Naive 1          Naive 2        Proposed
                        Window    Spec      RMSE      Cov.    RMSE    Cov.    RMSE    Cov.
                        Correct trajectory specification
                        90%       Correct 4.195         –     1.769   0.947   1.721   0.948
                        70%       Correct 4.410         –     2.164   0.946   2.096   0.946
                        50%       Correct 4.780         –     2.393   0.944   2.333   0.945
                        Misspecified trajectory specification
                        90%        Wrong      4.311     –     2.565   0.800   2.516   0.795
                        70%        Wrong      4.541     –     2.810   0.805   2.744   0.804
                        50%        Wrong      4.982     –     2.994   0.866   2.933   0.867




6    Discussion
This work develops a hierarchical Bayesian joint model for inferring latent peak ages and perfor-
mance trajectories from sparse, noisy, and irregular competition records. By treating peak age as a
latent event time defined by the underlying trajectory, the framework links performance dynamics
directly to covariate effects on earlier or later peak age.
    Methodologically, the main contribution is to connect longitudinal trajectory modeling with
event-time inference when the event, peak performance, is not observed directly but defined as a
functional of the latent trajectory. This formulation propagates trajectory uncertainty into peak-age
and covariate-effect inference, addressing a key limitation of pseudo-peak and two-stage analyses.
In simulations, as peak-age information weakens, pseudo-peak and two-stage analyses tend to at-
tenuate regression effects while reporting standard errors that change little or even decrease. The
joint model instead reflects weaker information through wider posterior uncertainty and compara-
tively stable regression estimates. This pattern echoes two familiar statistical issues: measurement
error in a latent response can bias covariate effects, and two-stage generated-response procedures
can make second-stage inference overconfident when first-stage uncertainty is ignored.
    In the athletics application, the framework gives coherent inference on peak age and on rates
of improvement and decline while accounting for heterogeneity across athletes and disciplines.
The results show systematic sport-category differences in peak age and trajectory shape, along
with biological-sex patterns that are not fully explained by conventional physiological arguments.
These findings show how statistical modeling can complement domain knowledge about biological
development, career structure, and selection processes.
    Beyond this application, the framework has broader use in sports analytics and related fields.
It can support athlete development analysis, forecasting from partial career data, and compar-

                                                         18
isons across sports or cohorts where peak age and performance dynamics may reflect structural or
environmental differences. More generally, the methodology applies when a latent event time is
directly defined by an underlying longitudinal process, such as growth curves, skill acquisition, or
productivity trajectories.
    Several extensions and data-related limitations suggest future work. The parametric AFT
submodel is one convenient specification for latent peak age; semi-parametric or nonparametric
alternatives could be developed within the same joint framework, although integration with the
latent trajectory model remains nontrivial. Similarly, quadratic trajectories are interpretable but
may not capture multi-phase or multi-peak career patterns, motivating smoother and more flexible
trajectory representations. Data-related limitations include the lack of explicit information on
injury, retirement, event transitions, competition-level changes, and competing career endpoints,
all of which may inform trajectories and peak age. Because the World Athletics analysis was
restricted to athletes in a single selected event, future work could model cross-event dependence
and event-transition processes for multi-discipline athletes. Extensions to multivariate performance
outcomes would further broaden the framework.
    For reproducibility, we provide an accompanying R package supporting symmetric and asym-
metric trajectory specifications. The software is available via an anonymized GitHub repository
and will be publicly released.


Funding
T. Guan’s work was supported by the Discovery Grant (RGPIN-2022-05140) from the Natural
Sciences and Engineering Research Council of Canada (NSERC).


Supplementary Material
Additional figures and tables, simulation details, prior specifications, and MCMC diagnostics are
provided in the accompanying supplementary material.

References
Sian V Allen and Will G Hopkins. Age of peak competitive performance of elite athletes: a systematic
   review. Sports Medicine, 45(10):1431–1441, 2015.

Joseph Baker, Bradley W Young, and David Mann. Advances in athlete development: understanding
  conditions of and constraints on optimal practice. Current Opinion in Psychology, 16:24–27, 2017.

Ildikó Balatoni, Ágnes Jenes, Nikolett Kosztin, and László Csernoch. Is there an ideal age to win an Olympic
   medal? Különleges Bánásmód-Interdiszciplináris folyóirat, 6(1):7–17, 2020.

Júlia Barreira, Bruno Bueno, and João Guilherme Cren Chiminazzo. Relative age effect and age of peak
   performance: an analysis of women’s football players in the Olympic Games (1996-2016). Motriz: Revista
   de Educação Fı́sica, 27:e1021006921, 2021.

James A Brander, Edward J Egan, and Louisa Yeung. Estimating the effects of age on NHL player perfor-
  mance. Journal of Quantitative Analysis in Sports, 10(2):241–259, 2014.

Samuel L Brilleman, Michael J Crowther, Margarita Moreno-Betancur, Jacqueline Buros Novik, James
  Dunyak, Nidal Al-Huniti, Robert Fox, Jeff Hammerbacher, and Rory Wolfe. Joint longitudinal and
  time-to-event models for multilevel hierarchical data. Statistical Methods in Medical Research, 28(12):
  3502–3515, 2019.


                                                      19
A. Cakravastia and M. Setiawan. Role of local club in developing value chain of high performance national
  tennis athlete. ITF Coaching & Sport Science Review, 30(87):63–71, 2022. doi: 10.52383/itfcoaching.
  v30i87.336.

Yuming Chen, Jiexing Chen, Yang Cao, and Liang Chen. Peak performance characteristics and key compe-
  tition factors of elite speed skaters based on longitudinal data. Scientific Reports, 15(1):33273, 2025.

Patric Dolmeta, Raffaele Argiento, and Silvia Montagna. Bayesian GARCH modeling of functional sports
  data. Statistical Methods & Applications, 32(2):401–423, 2023.

Pierpalo D’Urso, Livia De Giovanni, and Vincenzina Vitale. A Bayesian network to analyse basketball
  players’ performances: a multivariate copula-based approach. Annals of Operations Research, 325(1):
  419–440, 2023.

Juliana Exel and Peter Dabnichki. Precision sports science: what is next for data analytics for athlete
  performance and well-being optimization? Applied Sciences, 14(8):3361, 2024.

Dianne M. Finkelstein. A proportional hazards model for interval-censored failure time data. Biometrics,
  42(4):845–854, 1986. doi: 10.2307/2530698.

Ali Gorzi, Mina Khantan, Omid Khademnoe, and Roger Eston. Prediction of elite athletes’ performance
  by analysis of peak-performance age and age-related performance progression. European Journal of Sport
  Science, 22(2):146–159, 2022.

Jim E Griffin, Laurenţiu C Hinoveanu, and James G Hopker. Bayesian modelling of elite sporting performance
  with large databases. Journal of Quantitative Analysis in Sports, 18(4):253–268, 2022.

Tianyu Guan and Tim B Swartz. Acceleration and age in soccer. International Journal of Sports Science &
  Coaching, 19(3):1035–1041, 2024.

L. L. Hardy, B. Kelly, K. Chapman, L. King, and L. Farrell. Parental perceptions of barriers to children’s
   participation in organised sport in Australia. Journal of Paediatrics and Child Health, 46(4):197–203,
   2010. doi: 10.1111/j.1440-1754.2009.01661.x.

Thomas A Haugen, Paul A Solberg, Carl Foster, Ricardo Morán-Navarro, Felix Breitschädel, and Will G
  Hopkins. Peak age and performance progression in world-class track-and-field athletes. International
  Journal of Sports Physiology and Performance, 13(9):1122–1129, 2018.

Anne Hecksteden, Sabrina Forster, Florian Egger, Felix Buder, Ralf Kellner, and Tim Meyer. Dwarfs on the
  shoulders of giants: Bayesian analysis with informative priors in elite sports research and decision making.
  Frontiers in Sports and Active Living, 4:793603, 2022.

B. J. Houltberg and R. M. Scholefield. Developmental model of elite athletes: the integration of developmen-
  tal science and practitioner experience. Professional Psychology: Research and Practice, 51(6):550–559,
  2020. doi: 10.1037/pro0000316.

Marianne Huebner and Aris Perperoglou. Performance development from youth to senior and age of peak
 performance in Olympic weightlifting. Frontiers in Physiology, 10:1121, 2019.

Lawrence Joseph and David B Wolfson. Estimation in multi-path change-point problems. Communications
  in Statistics - Theory and Methods, 21(4):897–913, 1992.

John P. Klein and Melvin L. Moeschberger. Survival Analysis: Techniques for Censored and Truncated Data.
  Springer, New York, 2 edition, 2003. doi: 10.1007/b97377.

Pingwei Li, Juanita R Weissensteiner, Johan Pion, and Veerle De Bosscher. Predicting elite success: evidence
  comparing the career pathways of top 10 to 300 professional tennis players. International Journal of Sports
  Science & Coaching, 15(5-6):793–802, 2020.


                                                     20
Yixiu Liu, Depeng Jiang, Mahmoud Torabi, and Xuekui Zhang. A Bayesian multilevel joint modeling of
  longitudinal and survival outcomes in cluster randomized controlled trial studies. Statistics in Medicine,
  45(1-2):e70385, 2026.

Maddison McLellan, Sachin Allahabadi, and Nirav K Pandya. Youth sports specialization and its effect
 on professional, elite, and Olympic athlete performance, career longevity, and injury rates: a systematic
 review. Orthopaedic Journal of Sports Medicine, 10(11):23259671221129594, 2022.

Shirzad Mian Darbandi and Mostafa Zarei. Relationship between shoulder and knee muscles isokinetic
  strength and musculoskeletal injuries in Iranian national judo teams: a prospective cohort study. Physical
  Treatments: Specific Physical Therapy Journal, 13(4):225–234, 2023. doi: 10.32598/ptj.13.4.403.4.

Kevin M Murphy and Robert H Topel. Estimation and inference in two-step econometric models. Journal
  of Business & Economic Statistics, 20(1):88–97, 2002.

Rasmus Oestergaard Nielsen, Michael Lejbach Bertelsen, Daniel Ramskov, Merete Møller, Adam Hulme,
  Daniel Theisen, Caroline F Finch, Lauren Victoria Fortington, Mohammad Ali Mansournia, and
  Erik Thorlund Parner. Time-to-event analysis for sports injury research part 1: time-varying exposures.
  British Journal of Sports Medicine, 53(1):61–68, 2019.

P. T. Nikolaidis, M. A. Zingg, and B. Knechtle. Performance trends in age-group runners from 100 m to
   marathon—the World Championships from 1975 to 2015. Scandinavian Journal of Medicine & Science
   in Sports, 27(12):1588–1596, 2017.

M. L. Øydna, M. Saarinen, J. C. Nielsen, and C. T. Bjørndal. “you can definitely tell she’s truly committed”:
  student-athletes’ discursive construction of athletic commitment during transitions in secondary school.
  Frontiers in Sports and Active Living, 7:1658234, 2025. doi: 10.3389/fspor.2025.1658234.

Gemma N Parry, Sean Williams, Carly D McKay, David J Johnson, Michael F Bergeron, and Sean P Cum-
  ming. Associations between growth, maturation and injury in youth athletes engaged in elite pathways:
  a scoping review. British Journal of Sports Medicine, 58(17):1001–1010, 2024.

Kangyi Peng, Ryan T Brodie, Tim B Swartz, and David C Clarke. Bayesian inference of the impulse-response
  model of athlete training and performance. International Journal of Performance Analysis in Sport, 24
  (1):74–89, 2024.

Ken Peng, Dave C Clarke, and Tim B Swartz. Bayesian approaches for critical velocity modelling of data
  from intermittent efforts. International Journal of Sports Science & Coaching, 17(4):868–879, 2022.

V. Pilkington, S. Rice, L. Olive, C. C. Walton, and R. Purcell. Athlete mental health and wellbeing during
  the transition into elite sport: strategies to prepare the system. Sports Medicine - Open, 10(1):24, 2024.
  doi: 10.1186/s40798-024-00690-z.

Michael Romann, Marie Javet, Julia Hernandez, Louis Heyer, Severin Trösch, Stephen Cobley, and Dennis-
  Peter Born. Longitudinal performance trajectories of young female sprint runners: a new tool to predict
  performance progression. Frontiers in Sports and Active Living, 6:1491064, 2024.

A. L. A. Soares and H. M. Carvalho. Burnout and dropout associated with talent development in youth
  sports. Frontiers in Sports and Active Living, 5:1190453, 2023. doi: 10.3389/fspor.2023.1190453.

Paul A Solberg, Will G Hopkins, Gøran Paulsen, and Thomas A Haugen. Peak age and performance pro-
  gression in world-class weightlifting and powerlifting athletes. International Journal of Sports Physiology
  and Performance, 14(10):1357–1363, 2019.

J. C. Spence, N. L. Holt, C. J. Sprysak, N. Spencer-Cavaliere, and T. Caulfield. Non-refundable tax credits
   are an inequitable policy instrument for promoting physical activity among Canadian children. Canadian
   Journal of Public Health, 103(3):175–177, 2012. doi: 10.1007/BF03403808.


                                                     21
Bojidar Spiriev and Attila Spiriev. IAAF scoring tables of athletics. IAAF, 2000.

M. Spyropoulou, J. G. Hopker, and J. E. Griffin. Modelling between- and within-season trajectories in elite
  athletic performance data. arXiv preprint arXiv:2405.17214, 2024.

Michael Stiefel, Beat Knechtle, Christoph Alexander Rüst, Thomas Rosemann, and Romuald Lepers. The
  age of peak performance in Ironman triathlon: a cross-sectional and longitudinal data analysis. Extreme
  Physiology & Medicine, 2(1):27, 2013.

R. F. Subotnik, P. Olszewski-Kubilius, and F. C. Worrell. Environmental factors and personal characteristics
  interact to yield high performance in domains. Frontiers in Psychology, 10:2804, 2019. doi: 10.3389/fpsyg.
  2019.02804.

Peter Tea and Tim B Swartz. The analysis of serve decisions in tennis using Bayesian hierarchical models.
  Annals of Operations Research, 325(1):633–648, 2023.

A. Tessitore, L. Capranica, C. Pesce, Nadine De Bois, M. Gjaka, G. Warrington, C. MacDonncha, and
  M. Doupona. Parents about parenting dual career athletes: a systematic literature review. Psychology of
  Sport and Exercise, 53:101833, 2021. doi: 10.1016/j.psychsport.2020.101833.

Lu Tian and Tianxi Cai. On the accelerated failure time model for current status and interval censored data.
  Biometrika, 93(2):329–342, 2006. doi: 10.1093/biomet/93.2.329.

Bruce W. Turnbull. The empirical distribution function with arbitrarily grouped, censored and truncated
  data. Journal of the Royal Statistical Society. Series B (Methodological), 38(3):290–295, 1976. doi: 10.
  1111/j.2517-6161.1976.tb01597.x.

Jane-Ling Wang and Qixian Zhong. Joint modeling of longitudinal and survival data. Annual Review of
  Statistics and Its Application, 12(1):449–476, 2025.

Lang Wu, X Joan Hu, and Hulin Wu. Joint inference for nonlinear mixed-effects models and time to event
  at the presence of missing data. Biostatistics, 9(2):308–320, 2008.

Michael S Wulfsohn and Anastasios A Tsiatis. A joint model for survival and longitudinal data measured
  with error. Biometrics, 53(1):330–339, 1997. doi: 10.2307/2533118.

Zhigang Zhang and Jianguo Sun. Interval censoring. Statistical Methods in Medical Research, 19(1):53–70,
  2010. doi: 10.1177/0962280209105023.




                                                    22
      Supplementary Material: Hierarchical
       Bayesian Joint Modeling of Athlete
    Performance Trajectories and Latent Peak
                      Ages
              K. Ken Penga,b , Tianyu Guanc , and Xiong Zhaod,e
a
   Department of Statistics and Actuarial Science, Simon Fraser University,
                            Burnaby, BC, Canada
    b
      Department of Civil Engineering, University of Ottawa, Ottawa, ON,
                                   Canada
c
  Department of Mathematics and Statistics, York University, Toronto, ON,
                                   Canada
                 d
                   AccMov Health Inc., Ottawa, ON, Canada
  e
    School of Kinesiology and Health Studies, Queen’s University, Kingston,
                                ON, Canada



S1     Additional figures and tables
Table S1 provides the event-level summary of the World Athletics dataset after preprocess-
ing.




                                            1
Table S1: World Athletics dataset after preprocessing: 3,229 single-event athletes and
105,515 competition records. Observed window is the last observed age minus the first
observed age for each athlete. IQR denotes the interquartile range. Observed age range
reports the median first and last observed ages within each event.

Event         No. athletes No. records Records/athlete Observed window Observed age range
                                        median (IQR)      median (IQR)            median
100 m                 470       15,000 22 (14.0, 41.0)    6.9 (4.2, 10.0)       19.5–27.7
400 m                 606       18,537 22 (13.0, 39.0)     5.3 (3.3, 8.3)       20.9–27.0
1500 m                639       16,647 20 (13.0, 33.0)     6.4 (4.2, 9.0)       22.4–29.3
Marathon              238        3,039 12 (11.0, 14.0)    9.0 (7.0, 10.5)       24.7–34.0
Long jump             286        8,491 22 (14.0, 36.0)    7.4 (5.2, 10.1)       21.0–29.2
Shot put              379       17,932 30 (17.0, 59.5)     6.8 (4.4, 9.4)       22.8–30.1
Discus throw          213        9,189 26 (15.0, 49.0)    8.3 (6.0, 12.0)       23.0–32.0
Javelin throw         366       16,204 29 (17.0, 57.0)    7.7 (5.0, 10.7)       21.4–29.8
Decathlon               13         200 13 (11.0, 19.0)     7.2 (6.2, 8.2)       21.0–29.1
Heptathlon              19         276 14 (12.0, 17.0)     8.0 (7.0, 9.0)       22.5–30.6
Total               3,229      105,515               –                  –               –


    Figure S1 summarizes the athlete-level posterior mean peak ages on the original age
scale by sport category and biological sex.

                                                 Sex             Men    Women




                                            35
        Posterior mean estimated peak age




                                            30




                                            25




                                            20


                                                                    g                ts        s                     g                    nts       s
                                                                 lon              rin       row                  nin                     e        mp
                                                              le-               Sp        Th                  run                     ev        Ju
                                                            dd                                           ad                       d
                                                       Mi                                              Ro                     ine
                                                                                                                           mb
                                                                                                                         Co




Figure S1: Athlete-level posterior mean peak ages by sport category and biological sex.
Boxplots summarize posterior mean estimates of latent peak age τi within each sport–sex
group; points represent individual athletes.




                                                                                                   2
S2     Simulation data-generating procedure
Algorithm S1 gives the full data-generating procedure used in the simulation study.

Algorithm S1 Simulation data-generating procedure.
 1: Fix I = 200 athletes and repeat for M = 200 replications. Fix β0 = 3.20, β1 = 0.01,
    β2 = 0.05, στ = 0.10, α0 = 1150, σα = 50, ρ0 = 0.25, σρ = 0.8, and σy = 20.
 2: for i = 1, . . . , I do
 3:    Generate covariates x1i ∼ N (0, 32 ), x2i ∼ Bernoulli(0.8).
 4:    Generate peak age:

                       log(τi ) = β0 + β1 x1i + β2 x2i + ei ,     ei ∼ N (0, στ2 ).

 5:    Generate trajectory parameters:

                        αi ∼ N (α0 , σα2 ),      ρi ∼ Lognormal(log ρ0 , σρ2 ).

 6:    Construct the symmetric quadratic trajectory:

                                      Yi (t) = αi − ρi (t − τi )2 .

 7:    For the asymmetric data-generating mechanism, use
                                    {︄
                                      αi − 0.5ρi (t − τi )2 , t ≤ τi ,
                           Yi (t) =
                                      αi − 1.5ρi (t − τi )2 , t > τi .

 8:     Generate independent Ui , Vi ∼ Beta(2, 5). Let Li denote the start of the observed
    age window, Si its length, and Ri its endpoint. Set (Li , Si ) = (15 + 10Ui , 8 + 40Vi ),
    (15 + 15Ui , 40Vi ), or (15 + 15Ui , 25Vi ) for the approximately 90%, 70%, and 50% peak-
    coverage settings, respectively, and then set Ri = min(45, Li + Si ).
 9:     Draw ni = max{3, Poisson(20)}, set two observation times to Li and Ri , and sample
    the remaining ni − 2 times independently from Uniform(Li , Ri ).
10:     Generate observations:

                               yij = Yi (tij ) + εij ,   εij ∼ N (0, σy2 ).

11: end for



S3     Prior specification
Table S2 summarizes the prior distributions used for the athletics application. These priors
are weakly informative: they encode broad plausible ranges for elite athletics performance
while leaving substantial room for posterior updating by the data.




                                                  3
                  Table S2: Prior distributions for the athletics application.
Parameter block                                   Prior distribution Hyperparameters
Components of θ 0 corresponding to peak level     Normal             mean = 1200, sd = 200
Components of θ 0 corresponding to trajectory     Normal             mean = log(0.5), sd = 1
curvaturea
Sport-category coefficients in B for peak level   Normal             mean = 0, sd = 200
Sport-category coefficients in B for trajectory   Normal             mean = 0, sd = 0.5
curvature
β0                                                Normal             mean = log(28), sd = 0.5
Biological-sex coefficient in β                   Normal             mean = −0.1, sd = 0.1
Birth-year coefficient in β                       Normal             mean = 0, sd = 0.5
Sport-category coefficients in β for peak age     Normal             domain-informed meansb , sd = 0.1
Sport-by-sex interaction coefficients in β        Normal             mean = 0, sd = 0.3
Variance components in Σθ c                       Half-Normal        sd = 100
σy                                                Half-Normal        sd = 200
στ                                                Half-Normal        sd = 0.5
 a
   In the implementation, curvature parameters are modeled on the log scale to ensure positivity.
 b
   Domain-informed prior means for sport-category effects in the peak-age model are 0.10 (combined-
   events), −0.10 (sprints), 0.00 (throws), −0.10 (road running), and 0.00 (jumps), all specified relative
   to the baseline middle-long distance category.
 c
   In the present implementation, Σθ is assumed diagonal and parameterized through independent
   random-effect scale parameters for computational efficiency.


S4      MCMC diagnostics
Posterior inference for the athletics application was carried out using four parallel MCMC
chains. Figures S2–S5 show trace plots and prior-to-posterior comparisons for representa-
tive parameters. In the trace plots, the four chains overlap closely and fluctuate around
stable levels without visible long-term trends, indicating good mixing and stationarity for
both the peak-age AFT submodel and the longitudinal performance submodel. The re-
ported R ˆ︁ values are close to one for all displayed parameters. The R ˆ︁ diagnostic compares
between-chain and within-chain variability, with values near one indicating that the chains
are sampling from the same stationary posterior distribution (Vehtari et al., 2021). In these
diagnostics, the displayed R ˆ︁ values range from 1.001 to 1.007, providing no evidence of lack
of convergence.
    The prior-to-posterior comparisons show that the data provide substantial information
beyond the weakly informative priors. For the peak-age AFT parameters, the posterior den-
sities are generally much more concentrated than the corresponding priors. Several poste-
rior distributions also shift away from their prior centers, for example for the biological-sex
effect, the road-running sport-category effect, and selected sport-by-sex interaction terms.
For the trajectory-curvature parameters, the posterior densities are likewise narrower than
the priors and are centered differently across sport categories and between the pre-peak and
post-peak curvature components. These patterns indicate that the posterior summaries are
driven by the observed longitudinal performance records rather than being dominated by
the prior specification.




                                                   4
                      beta_S (Rhat=1.004)                                         beta_Y (Rhat=1.000)                                      eta^(tau)[Sprints] (Rhat=1.004)
                                                            0.12                                                           -0.04

                                                            0.08                                                           -0.08
0.10

                                                            0.04
                                                                                                                           -0.12
0.05
                                                            0.00
                                                                                                                           -0.16
        0       500          1000           1500     2000           0       500          1000           1500        2000           0        500         1000         1500        2000


               eta^(tau)[Throws] (Rhat=1.003)                            eta^(tau)[Road running] (Rhat=1.007)                          eta^(tau)[Combined events] (Rhat=1.001)
                                                                                                                            0.2
                                                             0.2
0.08                                                                                                                        0.1

                                                             0.1
0.04                                                                                                                        0.0


0.00                                                         0.0                                                            -0.1

                                                                                                                            -0.2
        0       500          1000           1500     2000           0       500          1000           1500        2000           0        500         1000         1500        2000


                eta^(tau)[Jumps] (Rhat=1.003)                              eta^(tau S)[Sprints] (Rhat=1.005)                              eta^(tau S)[Throws] (Rhat=1.002)
                                                                                                                           0.04

-0.05                                                       0.00
                                                                                                                           0.00

-0.10                                                       -0.05                                                          -0.04

-0.15                                                       -0.10                                                          -0.08


        0       500          1000           1500     2000           0       500          1000           1500        2000           0        500         1000         1500        2000


            eta^(tau S)[Road running] (Rhat=1.004)
 0.1


 0.0


 -0.1


 -0.2

        0       500          1000           1500     2000


                                                                        Chain        1       2          3       4




                          Figure S2: Trace plots for selected peak-age AFT parameters.




                                                                                         5
              log rho_L0 (Rhat=1.006)                                log rho_R0 (Rhat=1.007)                              eta^(L)[Sprints] (Rhat=1.006)
                                                  -2.0


-0.6                                                                                                           1.50
                                                  -2.4

-0.8                                                                                                           1.25

                                                  -2.8
-1.0                                                                                                           1.00

                                                  -3.2                                                         0.75
-1.2


-1.4                                              -3.6                                                         0.50
       0   500         1000         1500   2000          0       500          1000        1500          2000          0   500         1000         1500   2000


            eta^(L)[Throws] (Rhat=1.003)                       eta^(L)[Road running] (Rhat=1.007)                         eta^(R)[Sprints] (Rhat=1.005)
1.25


1.00                                                                                                            0.0
                                                    0

0.75
                                                                                                               -0.5

0.50                                               -1

                                                                                                               -1.0
0.25

       0   500         1000         1500   2000          0       500          1000        1500          2000          0   500         1000         1500   2000


           eta^(R)[Throws] (Rhat=1.008)                        eta^(R)[Road running] (Rhat=1.005)
 1.8


 1.5
                                                    0
 1.2


 0.9
                                                   -1

 0.6



       0   500         1000         1500   2000          0       500          1000        1500          2000


                                                             Chain        1          2     3        4




           Figure S3: Trace plots for selected longitudinal performance parameters.




                                                                              6
                                                                                                   Posterior       Prior



                                      beta_S                                                            beta_Y                                                 eta^(tau S)[Road running]

          20                                                                  20
                                                                                                                                          7.5
          15                                                                  15
                                                                                                                                          5.0
          10                                                                  10
          5                                                                     5                                                         2.5

          0                                                                     0                                                         0.0
                 -0.4       -0.2             0.0               0.2                         -1             0               1                             -1.0      -0.5      0.0         0.5     1.0

                                eta^(tau S)[Sprints]                                              eta^(tau S)[Throws]                                          eta^(tau)[Combined events]
          20                                                                  20

          15                                                                                                                               6
                                                                              15

          10                                                                  10                                                           4

          5                                                                     5                                                          2

          0                                                                     0                                                          0
Density




                  -1.0     -0.5           0.0            0.5           1.0          -1.0    -0.5          0.0           0.5         1.0          -0.4             -0.2            0.0         0.2

                                 eta^(tau)[Jumps]                                               eta^(tau)[Road running]                                            eta^(tau)[Sprints]
                                                                             10.0                                                         20
          15
                                                                              7.5                                                         15
          10
                                                                              5.0                                                         10
          5
                                                                              2.5                                                          5

          0                                                                   0.0                                                          0
               -0.4      -0.2          0.0             0.2           0.4         -0.4      -0.2             0.0               0.2               -0.25              0.00             0.25            0.50

                                eta^(tau)[Throws]

          20
          15
          10
          5
          0
                          -0.25                 0.00                 0.25



                Figure S4: Prior and posterior densities for selected peak-age AFT parameters.




                                                                                                      7
                                                                                        Posterior          Prior



                        eta^(L)[Road running]                                           eta^(L)[Sprints]                                            eta^(L)[Throws]
                                                                                                                                3
          1.2

                                                               2                                                                2
          0.8


          0.4                                                  1                                                                1


          0.0                                                  0                                                                0
                 -1            0            1         2                  -1                0               1           2             -2        -1             0           1

                        eta^(R)[Road running]                                           eta^(R)[Sprints]                                            eta^(R)[Throws]
          1.2                                                                                                                  2.0
                                                              1.5
                                                                                                                               1.5
Density




          0.8
                                                              1.0
                                                                                                                               1.0
          0.4
                                                              0.5                                                              0.5

          0.0                                                 0.0                                                              0.0
                 -1              0              1         2                   -1               0               1           2              -1              0           1

                             log rho_L0                                                   log rho_R0
           3                                                  2.0

                                                              1.5
           2
                                                              1.0
           1
                                                              0.5

           0                                                  0.0
                      -2.5            0.0           2.5             -4             -2               0              2



          Figure S5: Prior and posterior densities for selected trajectory-curvature parameters.


References
Vehtari, Aki, Gelman, Andrew, Simpson, Daniel, Carpenter, Bob and Bürkner, Paul-
                                                                               ˆ︁ for as-
  Christian (2021). Rank-normalization, folding, and localization: an improved R
  sessing convergence of MCMC (with discussion). Bayesian Analysis 16 667–718. doi:
  https://doi.org/10.1214/20-BA1221.




                                                                                          8

