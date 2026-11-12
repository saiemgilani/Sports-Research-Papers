<!-- source: library/preprints/arXiv/2026/2026 - The Athlete as a Scientist of One Agentic Bayesian Experimental Design for Individualized Physiology from Consumer Wearables - Moradi.pdf -->
<!-- item: https://arxiv.org/abs/2610.40370 -->
<!-- authors: Behnam Moradi -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-12; equations, tables and figures are NOT preserved - consult the PDF for those -->

# The Athlete as a Scientist of One: Agentic Bayesian Experimental Design for Individualized Physiology from Consumer Wearables

                                                                                                                                                                                 1




                                                        The Athlete as a Scientist of One:
                                                     Agentic Bayesian Experimental Design for
                                                             Individualized Physiology
                                                             from Consumer Wearables
                                                                                                    Behnam Moradi
                                                                                              Software Department, KavAI
                                                                                                    California, USA
                                                                                               behnam.moradi@kavai.com
arXiv:2610.40370v1 [cs.RO] 29 Oct 2026




                                            Abstract—Large language model (LLM) agents for personal                  Recent personal-health agents are impressive readers of
                                         health read wearable data and recommend, but do not learn                wearable data. PH-LLM fine-tunes Gemini to produce expert-
                                         about the individual in a way that can be audited or falsified. We       rated coaching from thirty-day summaries [1]; PHIA answers
                                         present E PI C OACH, an agentic system that treats one athlete,
                                         a cross-country mountain biker, as the subject of accountable            open-ended numerical questions over wearable time series
                                         N-of-1 science. Claims about the athlete live in an evidence-gated       by generating and running code [2]; the Personal Health
                                         hypothesis registry: each must issue a probabilistic prediction about    Agent orchestrates data-scientist, domain-expert and coach sub-
                                         a future session before it occurs, and its belief moves only through     agents [3]; SePA grounds advice in personalized risk models
                                         computed evidence from a logged statistical fit. Predictions come        and trusted retrieval [4]; LLM-SPTRec generates training plans
                                         from a mechanistic digital twin inferred from heart rate, GPS and
                                         barometric altitude: a lagged heart-rate response model, a fitness–      from a sports-science knowledge graph [5]. All of them share
                                         fatigue model with learned time constants, and a latent technical-       a direction of information flow: data in, recommendation out,
                                         descending skill state, measured on discovered trail segments.           population knowledge applied to an individual. None maintains
                                         The agent prescribes the next training week as a constrained             a body of claims about this particular person that is explicit,
                                         experiment maximizing information gain subject to load and               probabilistic, revised by evidence, and exposed to falsification.
                                         safety constraints, around two instrument rides. We evaluate the
                                         system two ways over eighteen months of data. A rolling-origin           If such a system tells the athlete that her heart rate drifts in
                                         replay benchmark shows the twin beats standard forecasters on            the heat, nothing records whether that claim was ever tested,
                                         heart rate but not segment time, and the agentic loop matches a          what it would take to overturn it, or whether it was quietly
                                         static model. A live prospective phase runs the weekly cycle: in its     abandoned.
                                         first three weeks the ledger sealed 20 predictions, scored 14, the
                                         descent forecast calibrated after one correction, the climb forecast        We argue that the missing object is not a better recommender
                                         pessimistic as the athlete improved, and the safety officer vetoed       but an epistemic loop, and that building one for a single human
                                         the agent twice. Every correction is preserved in the registry, a        raises problems that automated-science systems in chemistry
                                         template for auditable, falsifiable personalization in digital health.   or biology [6]–[8] do not face. The subject cannot be reset;
                                         We release the registry, benchmark and protocol.
                                                                                                                  every observation costs a training session that also changes the
                                            Index Terms—Digital twin, N-of-1 trial, Bayesian experimental         system being studied; the measurements are noisy wrist sensors
                                         design, large language model agents, hypothesis registry, wearable       rather than assays; and the designer has a second objective,
                                         sensors, mountain biking, personalized health.
                                                                                                                  making the athlete better, that competes with learning about her.
                                                                                                                  We call the resulting problem epistemic coaching and make
                                                                 I. I NTRODUCTION                                 four design commitments:

                                            A coach who has worked with the same athlete for years                1) A prediction ledger, not a chat log. Every hypothesis in
                                         knows things about that athlete that no textbook contains: that             the registry must emit a probabilistic prediction about a
                                         her heart rate climbs by six beats per hour once the temperature            specific future ride, timestamped before the ride. Beliefs
                                         passes 28◦ C, that two short nights cost her more on technical              move only through a tool that requires a logged statistical
                                         descents than on climbs, that she holds fitness longer than                 fit. This is what makes N =1 science defensible: it closes
                                         the forty-two-day constant assumed by every training platform.              the garden of forking paths [9], [10] that would otherwise
                                         This knowledge is individual, it was acquired by watching                   let a fluent language model explain any outcome after the
                                         many sessions, and, crucially, it was tested: the coach predicted,          fact.
                                         observed, and revised. Consumer wearables now record the                 2) A mechanistic twin from a watch alone. We infer, from
                                         raw material for this kind of knowledge continuously, and                   optical heart rate, GPS and barometric altitude only, a
                                         LLM agents can reason over it. Yet the systems built so far                 lagged heart-rate response with drift and heat interactions,
                                         do something quite different from what the experienced coach                a fitness–fatigue model whose time constants are estimated
                                         does.                                                                       rather than assumed, and a latent technical-skill state that
                                                                                                                                      2



    is deliberately separated from aerobic fitness because heart BoxingGym [18] benchmarks LLM agents on information-gain-
    rate stops measuring mechanical work on descents [11], driven design in simulated environments and finds them weak
    [12].                                                          at it. Our setting is BoxingGym’s real-world counterpart with
3) Workouts as experiments, with safety as a hard con- a living subject, irreversible state and a dual objective.
    straint. The next ride is chosen from a menu by a utility            c) Training-load modelling and digital twins.: The
    that trades expected information gain against expected per- Banister impulse-response model [19], [20] and the Busso
    formance improvement, subject to acute:chronic workload variable-dose variant [21] relate training load to performance
    bounds, heart-rate caps and readiness gates enforced in through fitness and fatigue filters; they are known to be ill-
    code rather than by the language model. Repeated trail seg- conditioned [22], [23] and sensitive to the load metric [24].
    ments, discovered automatically, serve as the measurement Kalman-filter variants track parameters online [25]; optimal-
    instrument.                                                    control and reinforcement-learning methods optimize load
4) Evaluation by prediction, not by plausibility. We score schedules given fitted parameters. We treat parameter uncer-
    the system by rolling-origin replay over eighteen months tainty as the object to be reduced by design, and we use only
    of history and by a live prospective phase in which every wrist-derived load and segment-based performance rather than
    prediction is sealed before the ride it concerns, using proper power meters or laboratory tests.
    scoring rules and forecast-comparison tests designed for a           d) N-of-1 trials and self-experimentation.: Within-person
    single long time series.                                       crossover trials have a mature design and analysis litera-
      a) Contributions.: (i) A formalization of coaching as ture [26]–[29]. CASEbot [30] uses an LLM to help users design
sequential, safety-constrained Bayesian experimental design such experiments. In our system the agent generates candidate
over an evidence-gated hypothesis registry with a pre-registered experiments from model residuals, selects them by expected
prediction ledger (Section III). (ii) A wrist-only digital twin information gain, executes them through the athlete’s device,
for mountain biking with explicit identifiability analysis of and analyses them with randomization-respecting estimators.
its fitness–fatigue component (Section IV). (iii) An agent               e) Mountain-bike physiology.: Cross-country mountain
architecture, implemented in Google ADK, whose protocol,           biking  is characterized by sustained high heart rates that remain
not its prompts, guarantees that LLMs propose, select and          elevated   on descents despite low power output, attributed
explain while deterministic tools fit, score and gate (Section V). to  isometric    load and arousal [11], [12]; performance is
(iv) A public rolling-origin replay benchmark for individualized   multidimensional      and course-specific [31]; rolling resistance
physiological forecasting with retrospective results on eighteen   varies two-  to three-fold   with surface [32]. These facts shape the
months of data, and the first three weeks of a live, pre-          twin:  heart  rate is a  fitness signal only on climbs, descending
registered prospective N =1 phase with its complete audit          is a  separate   skill, and   rolling resistance is a segment-level
trail (Section VI).                                                nuisance.


                     II. R ELATED W ORK                                    III. C OACHING AS ACCOUNTABLE S EQUENTIAL
                                                                                        E XPERIMENTATION
      a) LLMs and agents over wearable data.: PH-LLM [1]
                                                                     A. Setting
fine-tunes a frontier model on expert case studies built from
thirty-day aggregates and reasons in-model. PHIA [2] is a               An athlete produces a stream of rides r = 1, 2, . . . and
ReAct agent [13] with a Python runtime and web search,               daily wellness records. Each ride yields a time series xr =
evaluated on thousands of insight questions. The Personal            {(t, HRt , gt , at , Tt )} of heart rate, GPS position, barometric
Health Agent [3] adds orchestration across specialist sub-           altitude and temperature, plus device-level summaries. Let
agents; PhysioLLM [14] adds a statistical-correlation layer;         θ ∈ Θ denote the parameters of a generative model of the
SePA [4] adds personalized predictive models and whitelisted         athlete (Section IV) and pt (θ) the posterior given all data
retrieval. These systems answer questions and give advice.           observed up to time t. A workout d ∈ D is a specification
None keeps a persistent, probabilistic, falsifiable model of the     the athlete can execute (archetype, duration, heart-rate target,
user, none chooses what data to collect next, and none writes        segment, day), and y ∼ p(y | θ, d) is the vector of outcomes
an intervention back to the device. We use PHIA-style agents         the twin predicts for it.
as a baseline and PHA-style orchestration as a point of contrast.
      b) AI scientists and hypothesis management.: End-to-           B. Hypothesis registry and prediction ledger
end automated research systems [6], [7] close a hypothesize–
                                                                     Definition 1 (Hypothesis). A hypothesis H = (text, ϕH , πH )
experiment–analyze loop in silico or in the wet lab, where
                                                                     consists of a natural-language claim; a formal predicate
replicates are cheap and the system under study is stationary.
                                                                     ϕH : Θ → {0, 1} or a sub-model MH ; a belief πH ∈ (0, 1);
The Hypothesis Evolution Protocol [8] externalizes hypothe-
                                                                     together with a lifecycle state in { PROPOSED, UNDER _ TEST,
ses as registry objects with evidence-gated beliefs, lineage
                                                                     SUPPORTED , REFUTED , UNDETERMINED , RETIRED } and
and lifecycle; we adopt this discipline and add the ledger
                                                                     parent pointers recording refinement and merging.
requirement that every hypothesis issues a dated prediction
about an unobserved outcome. Box’s loop with language                  Two rules distinguish our registry from a free-form notebook.
models [15], [16] and the Automatic Statistician [17] use LLMs       Evidence gating (inherited from [8]): πH changes only through
to propose and criticize probabilistic programs on fixed data;       record_evidence(H, log BF, fit_id), where log BF is
                                                                                                                                      3



a log Bayes factor or an equivalent evidence score computed physiological reading. All models are fit by Hamiltonian Monte
by a deterministic fit whose identifier exists in the statistician’s Carlo [38] in NumPyro [39]; cheap Kalman-form updates run
store, and the update is logit πH ← logit πH + log BF [33]. weekly and full refits monthly. Appendix B gives priors and
The language model has no tool that sets πH directly. Ledger full specifications.
requirement (ours): a hypothesis may enter UNDER _ TEST
only after predict(H, r∗ , qH ) has registered a predictive A. Signal quality and derived quantities
distribution qH for a specified future ride r∗ , and the registry
                                                                        Optical wrist heart rate fails in characteristic ways: it locks
refuses the call if its timestamp is later than the ride’s start.
                                                                     onto pedalling cadence or arm-shake frequency, drops out
Ledger predictions are scored with proper scoring rules [34]
                                                                     on rough descents, and lags true heart rate by 20–45 s [40],
when r∗ is observed, and the scores are the only admissible
                                                                     [41]. We compute a per-sample quality flag (cadence-lock
evidence for hypotheses about predictive claims. Identifiability
                                                                     when |HRt − cadencet | < 4 bpm for ≥ 30 s with collapsed
gate (ours): for a directional claim about a parameter, a
                                                                     variance; implausible jumps |∆HR| > 8 bpm/s), use a Student-
Savage–Dickey-style log BF is admitted only if the posterior
                                                                     t likelihood on heart rate, and expose the fraction of good
standard deviation has shrunk by at least 10% relative to the
                                                                     samples as a covariate so that instrument failure is itself
prior; otherwise the evidence is recorded as zero (the test
                                                                     something the registry can reason about. Altitude is taken
still consumes budget). Without this rule a bounded prior
                                                                     from the barometer, never from GPS. The device used here
that is merely re-shaped by weak data can masquerade as
                                                                     records no cadence, temperature or power in its FIT records,
evidence; it did so for the fitness time constant in our own data
                                                                     so cadence lock is detected indirectly through its flatline-and-
(Section IV-E). The verdict UNDETERMINED is reachable: a
                                                                     release signature; ambient temperature, humidity and conditions
hypothesis whose evidence has not left | log BF| < log 3 after
                                                                     come from the activity’s weather record (reported in Fahrenheit
a pre-set budget of tests is closed as unresolved rather than
                                                                     by the vendor API and converted).
left open indefinitely.
                                                                        Without a power meter we recover virtual power on climbs
C. The design problem                                                from  the standard road-cycling power balance [42],
                                                                                           h
   At each decision point the agent chooses the next workout.                      VPt = mgvt (sin θt + Crr cos θt )
Let π = (πH )H∈H be current registry beliefs and θ the twin                                                          i               (3)
parameters. The expected information gain of a design about                                  + 12 ρCd A vt3 + mat vt /η,
θ is the mutual information [35], [36]
                                                                     with total mass m, grade θt , speed vt and acceleration at .
  EIGθ (d) = Ept (θ) p(y|θ,d) [log p(y | θ, d) − log p(y | d)] ,     On climbs of grade ≥ 4% below 15 km/h the gravitational
                                                                 (1) term dominates and the aerodynamic term is negligible; the
                Z
    p(y | d) = p(y | θ, d) pt (θ) dθ,
                                                                     rolling coefficient Crr , which varies two- to three-fold with
and the analogous quantity for the discrete hypothesis set is the surface [32], is absorbed as a segment-level random effect.
expected reduction in registry entropy, EIGH (d) = H(π) − Virtual power is used only on climb segments and only as
Ey|d [H(π | y, d)], computed by Bayesian model averaging over an input to the heart-rate response; it is never reported as an
the sub-models MH . Because the athlete is not a laboratory, we estimate of mechanical power.
do not maximize information alone. With ∆p(d) denoting the
twin’s predicted change in performance over a fixed horizon if B. Repeated segments as instruments
d is executed, the agent solves                                         Repeated terrain converts an uncontrolled ride into a repeated-
            d⋆t = arg max λt EIG(d)d                                 measures design. We build the athlete’s trail network from
                      d∈Dtfeas                                   (2) OpenStreetMap: all named ways tagged as paths, tracks or
                                + (1 − λt ) Ept [∆p(d)],             service roads within each riding area are fetched, ways sharing
where λt ∈ [0, 1] decays over a training block (explore early, a name are joined end-to-end into a chain, and each chain is
exploit late) and Dtfeas ⊂ D is the set of designs that satisfy hard densified to 5 m points carrying an along-trail coordinate s.
constraints: acute:chronic workload ratio ACWR ∈ [0.8, 1.3] Every GPS sample is snapped to the nearest chain point within
computed on 7:28-day rolling loads [37], weekly load within 20 m, which gives it a trail name and a scalar position; a run
±15% of the block plan, at least one rest day per week, a is a contiguous stretch of samples on one chain with monotone
heart-rate cap, no prescription when device-reported training s, and its sign gives the direction (the same trail ridden up
readiness falls below a threshold or the athlete reports illness, and down is two segments). Because riders enter and leave a
and calendar availability. Constraints are evaluated by code; the trail at different points, timing the whole trail would inflate
language model may argue for a design but cannot admit an variance. We therefore define a segment by consensus gates:
infeasible one. We call the resulting policy information-directed the longest stretch of s covered by at least 60% of the rides
training.                                                            that touch the chain (and by at least five rides). A traversal
                                                                     is a pass from the entry gate to the exit gate with monotone
 IV. A W RIST-O NLY M ECHANISTIC T WIN FOR M OUNTAIN progress and no stop longer than 90 s; entry and exit times
                               B IKING                               are interpolated at the gate crossings. Each traversal records
   The twin is deliberately minimal: each component exists moving time (the primary timing outcome; wall-clock time is
because a hypothesis class needs it, and each parameter has a inflated by trail-side stops), heart-rate summary and quality,
                                                                                                                                      4



mean virtual power, ambient temperature, elapsed ride time,          (dry, habitual sleep, median elapsed ride time). A “stop-free”
recent precipitation and gear. Appendix A gives thresholds and       traversal is one whose clock starts when the rider rolls out
failure modes; Appendix G lists the discovered segments.             of the entry gate, so a pause at the gate (lap press, regroup)
                                                                     does not disqualify it; before this rule only 5 of 25 instrument
C. Heart-rate response on climbs                                     descents entered the fit.
  For climb traversals we model the steady-state heart rate the
body is approaching and the lag with which it approaches it:         E. Fitness–fatigue with learned time constants
                       ∆t                                               Daily load wd is computed from heart rate alone, using
                            HRss
                                        
    HRt+1 = HRt +               t − HRt + εt ,
                       τhr                                           Banister’s exponential TRIMP [20] as the primary metric and
                εt ∼ tν (0, σhr ),                          (4)      Edwards zone-TRIMP [44] and the device’s proprietary load
      HRss                                       t
        t = αr + βw(r) VPt + γT (Tr − 20) + γd 3600
                                                                     as sensitivity inputs, since load metrics are known not to be
                               t
             + γdT (Tr − 20) 3600 + us(t) .                    (5)   interchangeable [24]. Fitness and fatigue are exponential filters
                                                                     of load,
Here αr is a ride-level intercept (day-to-day arousal and resting
heart rate), us a segment random effect that absorbs Crr and           Fd = e−1/τ1 Fd−1 + wd ,            Gd = e−1/τ2 Gd−1 + wd ,
                                                                                                                                     (6)
surface, γT the heat offset, γd the cardiac-drift slope in bpm per     pd = p0 + k1 Fd − k2 Gd ,
hour [43], and γdT its interaction with temperature. The slope
βw follows a Gaussian random walk over weeks w, so that a with the Busso variable-gain extension [21] available when
contrast βw2 − βw1 is the formal content of the hypothesis “my posterior checks demand it. Because there is no laboratory
climbing response has improved”. The pair (γd , γdT ) is the test, performance pd is measured as heart-rate-adjusted speed
formal content of “my heart rate drifts X bpm/h above Y ◦ C”. on climb segments (log speed regressed on segment, heart
A segment-aggregate version regresses traversal-mean heart rate, temperature, elapsed time and pd , i.e. the external
rate on traversal-mean virtual power with the same covariates output at matched internal cost), with the device’s reported
and fits in seconds; the sample-level recursion is reserved for VO2 max available as an optional noisy auxiliary channel.
the final analysis.                                                Priors are informative but wide, τ1 ∼ LogNormal(ln 42, 0.3),
      a) Retrospective fit.: On 188 climb traversals over 9 seg- τ2 ∼ LogNormal(ln 7, 0.4), k2 /k1 ∼ LogNormal(ln 2, 0.3).
ments the aggregate model (NUTS, no divergences, R̂ ≤ 1.003)              a) Identifiability is a result, not a nuisance.: The fitness–
gives β = 19 ± 3 bpm per 50 W, cardiac drift γd = 6.0 bpm/h        fatigue   model is ill-conditioned even with weekly laboratory
(90% interval 2.1–9.6), a heat offset γT = 0.34 ± 0.23 bpm/ C   ◦  tests   [22], [23]: τ1 , τ2 , k1 , k2 trade off along ridges of the
and a heat–drift interaction indistinguishable from zero (γdT =    likelihood.   Our  data reproduce this. With weakly informative
                                               ◦
−0.27 ± 0.38; only 17 rides exceeded 25 C). Heart rate at          log-normal    priors  the posterior escapes to τ1 ≈ 180 days and
reference power changed by +4±4 bpm from the first to the last     τ 2 ≈  145  days:  a slow  trend, not a training response. Bounding
week, so the claim “aerobic response improved” has posterior       τ 1  ∈ [15, 90], requiring    τ2 < τ1 and k2 > k1 , and adding an
                                                       2
probability 0.16. Residual scale is 6.9 bpm with R = 0.65.         annual    harmonic   for trail conditions returns a posterior that is
                                                                   essentially the prior: Bhattacharyya overlap 0.89 for τ1 , 0.95
                                                                   for τ2 , 0.99 for k2 /k1 ; the 90% interval of k1 includes zero;
D. Technical descending as a latent skill
                                                                   the implied performance swing over eighteen months is 1.9%;
   On descents heart rate decouples from mechanical work [11], and leave-one-out comparison cannot separate the full model
so we do not model it as a fitness signal. Instead, descent time from a fitness-only model (|∆elpd| < 4). Without the seasonal
at matched conditions measures a latent skill:                     term the model absorbs a 14% seasonal swing into “fitness”;
            log Tr,s = µs + λs Sw(r) + δwet wetr                   load and season are confounded because the athlete rides more
                                           ⊤
                       + δlight lightr + δ cr + ηr,s ,             in summer. A synthetic check that simulates speeds from a
                                                                   true τ1 = 35 days on the athlete’s actual load history and
                 Sw ∼ N (Sw−1 , σS2 ),                             observation schedule recovers the latent performance trajectory
where λs is a segment loading (technical segments load more well (r = 0.95–0.99) but returns τ1 intervals of roughly [28, 65]
on skill), cr holds candidate covariates such as prior-night sleep days, biased upward (Appendix F). The observational design,
duration and elapsed ride time, and Sw is a weekly random not the model, is the bottleneck.
walk. “Sleep below 6.5 h slows my technical descents by Y %”           Three consequences follow. First, the registry reports “τ1 <
is a coefficient in δ and is testable only on segments with 42 days” as unresolved: the identifiability gate (Section III)
sufficient λs . Descent heart rate is retained as an exploratory refused the raw log BF of +1.45 because the posterior had
“arousal cost” outcome. On 104 stop-free descents over 8 widened relative to the prior. Second, this is precisely where
segments the fit gives δsleep = −0.022±0.015 per hour, i.e. one information-directed design earns its keep: the design that most
hour less sleep slows a descent by 2.2% (90% interval −0.2 to reduces uncertainty about τ2 is a planned deload followed by
+4.7%); wet conditions show no effect; the log-timing residual a standardized test climb, and about τ1 a sustained block; a
is 7.9%. The ledger prediction for the instrument descent is conventional schedule may never produce either contrast. Third,
drawn from this posterior: segment level, skill state advanced no real posterior is interpreted before its recovery has been
one random-walk step, and covariates at protocol conditions verified on synthetic athletes (Section VI-D).
                                                                                                                                                         5



                                                                                                  refit candidate sub-models


                                     Ingest                        Statistician                                                       Modeler ↔ Critic
  Garmin Connect                                                                      residuals    Hypothesizer    claims
                                  sync, HR QC,                       fit twin,                                                         template spec,
   rides, wellness                                                                              anomalies → claims
                                    segments                     residuals, LOO                                                         ≤ 3 rounds

                                                              posteriors      record_evidence                     register, predict



rides, wellness                                              Fit store                   Hypothesis Registry                            Scribe
                                                        posteriors, fit_id               beliefs, lineage, ledger                     weekly report
                                                                                                                                       to athlete

                                                                                                   π, pt (θ)


                                                                 Safety Officer                                                         Experiment
                                Workout Pusher           d⋆                            ranked        EIG scorer                Dt        Designer
   Athlete + watch                                                ACWR, HR
                               JSON → calendar                                                    nested MC, Eq. (2)                     menu Dt ,
                                                                 cap, readiness
                                                                                                                                        constraints
Fig. 1: The weekly E PI C OACH cycle. Purple nodes are LLM agents; teal nodes are deterministic tools; the red node is the safety gate; gold nodes are
persistent stores. LLMs may register hypotheses and predict, but only the Statistician’s record_evidence, keyed by a stored fit_id, can move a
belief. The Safety Officer’s constraints are code and cannot be argued around.



                    V. T HE E PI C OACH AGENT                       fits the twin and candidate sub-models, computes residual
                                                                    reports, leave-one-out comparisons [46] and Bayes factors, and
   E PI C OACH is a weekly cycle implemented as a Google stores every fit under a fit_id. The EIG scorer evaluates
ADK SequentialAgent with one inner LoopAgent [45] Eq. (2) over Dt by nested Monte Carlo [47] with N =M =500
(Figure 1). The architecture is not novel for being multi-agent; posterior draws (variational estimators [48] are a drop-in if
orchestrated specialist agents already exist for wearables [3]. cost demands). The Safety Officer evaluates the feasibility set
What we claim is the allocation: every operation that produces Dfeas and vetoes; an LLM explains the veto to the athlete but
                                                                       t
a number the system will act on is performed by a deterministic cannot lift it. The Workout Pusher serializes d⋆ as a cycling
tool, and the language model is confined to the operations where workout with heart-rate-target steps and writes it to the athlete’s
its strengths are real and its failure modes are survivable.        calendar, from which the watch receives it on the next sync
      a) What the LLM does.: The Hypothesizer receives (Appendix E).
structured residual diagnostics from the Statistician (e.g. “heart-
rate residual +6 bpm on rides with ambient temperature
> 27◦ C, n=14”; “descent times on segment 7 bimodal since                 c) Information-directed design in practice.: Scoring the
week 61”), retrieves candidate mechanisms from the literature, menu against the retrospective posterior ranks an overload week
and proposes hypotheses with a formal predicate, a prior followed by full rest with three repeated test efforts highest
log-odds and a test plan. This is mechanism retrieval and (0.17 nats), ahead of a three-week block-and-taper (0.16) and
analogical reasoning, a genuine language-model capability. all conventional weeks (≤ 0.06): the contrast in which fatigue
The Modeler translates an accepted hypothesis into a model dissipates while fitness persists is what separates τ2 from τ1 ,
specification drawn from a unit-tested template library (add as anticipated in Section IV-E. Absolute gains per cycle are
covariate, add interaction, add changepoint, add random walk, small because the posterior on k1 is near zero; information
split a parameter by condition); it cannot emit free-form model accrues over cycles. In a live run on the athlete’s current state
code, which keeps it from inventing unidentifiable structures. A (acute load 1.26× chronic) the Safety Officer vetoed ten of
Critic reviews the specification against identifiability red flags the top-ranked plans for ACWR, and the Designer settled on
and registry lineage, and the pair iterate at most three times. The a back-loaded conventional week with one test: an instance of
Experiment Designer proposes the candidate workout menu safety constraints overriding information gain by construction.
Dt (20–40 designs: long aerobic rides, climb repeats on segment
s at heart-rate target h, descent laps, deloads, a standardized
eight-minute test climb; crossed with duration, day and time              d) Registry protocol.: The registry is a relational
of day), negotiates calendar and wellness constraints with the store with seven tools: register, predict,
athlete in natural language, and explains the final choice. The record_evidence, refine, merge, retire, list.
Scribe writes the weekly report, including counterfactuals such Refinement and merging are permitted only for parents that
as “had you slept 7 h, the twin predicts climb 3 would have have reached a verdict or carry at least one piece of evidence,
been 4% faster” (computed by the twin as a posterior predictive so untested proposals cannot spawn descendants. Every call
under do(sleep = 7) and merely narrated by the model).              is logged with its caller, so the audit trail distinguishes an
      b) What tools do.: Ingest synchronizes rides and wellness, LLM proposal from a tool verdict. Schema and prompts are
runs quality control and segment matching. The Statistician in Appendix D.
                                                                                                                                               6



                                                                                check (≥ 80% of samples within 25 m of the trail). Seventy-
                                                                                nine historical traversals (April 2025–September 2026, every
                                                                                month of the record; 90 including the prospective phase) take
                                                                                12–21 min moving (median 17.3, robust CV 7.4%) at mean
                                                                                heart rates of 130–176 bpm; across those rides each +1 bpm of
                                                                                mean heart rate buys about 3.6 s, i.e. the between-ride spread
                                                                                is dominated by effort (Fig. 4), which is precisely what the
                                                                                fixed-heart-rate protocol removes. The descent instrument is
                                                                                Nicoles Trail, entered from the summit via Poplar Trail and
                                                                                timed from the Poplar–Nicoles junction to the exit (1.16 km,
                                                                                −158 m, −13.6%, 23 traversals, median 5.6 min, robust CV
                                                                                9.2%). A longer declared climb on a second network (5.9 km,
                                                                                +425 m, 47 min) was considered first and rejected before any
                                                                                prospective ride: it had six traversals against seventy-nine, and
                                                                                an instrument the athlete will ride twice a week has to be near
Fig. 2: The instrument ride on Burnaby Mountain (one recording, coloured home. The change is logged in the registry (the two ledger
by heart-rate zone; satellite view from the vendor’s app). From the car park at
lower left the athlete warms up along the Power Line Trail, climbs the Trans    predictions registered against the earlier instrument are marked
Canada Trail (a wide, steady-gradient gravel track under canopy) to University withdrawn, not deleted) and no prospective data is affected.
Drive, traverses the campus ring road, and descends Nicoles Trail, a narrow
technical singletrack, back to the start. The climb is held at 160 ± 5 bpm; the
descent is ridden at self-selected effort. Lap presses at the four gates mark the   B. Retrospective replay benchmark
two timed segments.
                                                                       The replay asks a single question: at each point in the past
                                                                    eighteen months, would the system’s beliefs have predicted the
                        VI. E VALUATION                             following week’s rides better than the alternatives? We step
                                                                    a rolling origin t weekly after a four-month warm-up. Every
A. Data                                                             method sees data ≤ t only, including language-model calls
   The subject is one recreational cross-country mountain biker (frozen model version, temperature 0, responses cached per
(an author) whose Garmin record begins with the purchase of a origin, three seeds). Each issues predictive distributions for the
Forerunner 965 on 2 April 2025 and runs to 30 September 2026 next seven days of realized rides: (a) traversal time on each
(eighteen months). It holds 653 activities, of which 223 are rides matched segment; (b) mean climb heart rate conditional on real-
(296 hours; median ride 79 min, 11 km, 340 m of climbing), ized virtual power and temperature; (c) within-ride drift slope;
recorded with optical wrist heart rate, GPS and a barometric (d) sign of the weekly change in device VO2 max. Registry
altimeter; no power meter or chest strap was used. Rides are hypotheses additionally issue binary ledger predictions.
fetched as native FIT files at 1 Hz (the vendor’s chart endpoint,        a) Metrics.: Continuous ranked probability score and log
which downsamples to 2,000 points, is not used); heart-rate score for (a)–(c) [34]; probability integral transform histograms
coverage within rides is 99.5% and GPS coverage 95.7%. Daily and expected calibration error for calibration; Brier score and
wellness records (556 days) include sleep stages and overnight calibration error for binary ledger predictions; and the posterior
heart-rate variability (77% of nights), resting heart rate, stress, entropy of θ over time as an information-accrual curve.
body battery and device-computed training metrics (readiness,            b) Baselines.: (1) Persistence and exponentially weighted
acute and chronic load, VO2 max; 98–99% of days). Ambient moving averages of segment times; (2) the device’s own
temperature on rides spans 1–32◦ C with 17 rides at or above VO2 max, race-time predictor and training-status outputs, which
25◦ C. Segment discovery yields 24 segments (11 climbs, 8 see identical sensor data; (3) a Banister model with population
descents, 5 rolling) with 458 traversals; 15 segments have at constants (τ1 , τ2 ) = (42, 7); (4) a Gaussian-process regression
least ten traversing rides. Three riding areas dominate: a home on calendar time and covariates with no mechanism; (5) a
hill with 153 rides, and two mountain networks with 29 and sequence model for heart-rate forecasting in the style of
26 rides. The non-ride activities (265 strength sessions, hiking, personalized workout models; (6) a PHIA-style ReAct agent
running) contribute to daily load but not to segment outcomes. with a code runtime asked for the same forecasts; (7) a static,
      a) Instrument ride.: Automatic discovery keys on named non-agentic twin: our model stack with fixed structure, no
OSM trails and therefore fragments long climbs (the home registry, no hypothesis-driven refinement.
hill’s main gravel ascent is mapped as 22 OSM ways and does              c) Ablations.: Run: no identifiability gate (every Savage–
not survive discovery as a single piece). The instrument climb Dickey result admitted); no registry (the twin refit at every
was instead declared with the athlete as a gate-to-gate route origin with fixed structure). The language-model-only forecaster
on the home hill (Fig. 2; close-ups in Fig. 9; GPS traces of is the ReAct baseline. Not run: no segment instruments (whole-
every traversal in Fig. 3): the Trans Canada Trail from its ride outcomes only) and no heart-rate quality control. The
lower gate to the point where the gravel meets the summit active component cannot be ablated in replay, since history is
road, 2.06 km, +148 m, 7.2%, a wide, smooth, steady-gradient fixed; we say so and evaluate it prospectively.
surface with no technical content, 10 minutes from the athlete’s         d) Statistical comparison.: Everything is one long de-
door. Traversals are extracted by gate passage with a corridor pendent series, so we use forecast-comparison tests built for
                                                                                                                                                            7




                                                                                                        Nicoles descent via Poplar (n = 31)
                                                                                                    49.273



                                            Trans Canada Trail climb (n = 90)                       49.272
               49.284
                                                                                                    49.271

               49.282
                                                                                                    49.270

               49.280
                                                                                                    49.269


                                 -122.920     -122.915   -122.910   -122.905   -122.900
                                                                                                    49.268


                                                                                                    49.267
                                                                                                         -122.910 -122.908 -122.906 -122.904 -122.902


Fig. 3: Instrument segments on Burnaby Mountain, all traversals to 22 October 2026. Left: 90 GPS traces on the Trans Canada Trail climb (blue), start gate
(circle) and end gate (square) where the gravel meets University Drive. Right: 31 traces on the Nicoles descent via Poplar Trail (red); the start gate is the
athlete’s lap-press point, not the OSM junction node, which sat 49 m off the ridden line. Grey dots: OSM corridor geometry used for the corridor check.


                                        Climb: effort dominates time                                    Fixing HR removes effort spread
                            22                                                                16
                            20                                                                14
                                                                                              12
        Moving time (min)




                            18                                                                10                                 Uncontrolled (n=79)
                                                                                                                                 CV=9%
                                                                                      Count




                                                                                               8                                 Protocol prediction
                            16                                                                                                     (17.7, 1.25²) min
                                                                                               6
                            14         Historical traversal                                    4
                                       OLS slope=-3.6 s/bpm
                                       r 2=0.17                                                2
                            12         Protocol target 160 bpm
                                                                                               0
                                  80         100 120 140 160                    180                12        14    16      18     20             22
                                              Mean heart rate (bpm)                                               Moving time (min)
Fig. 4: Justification for the fixed-heart-rate protocol. Left: moving time vs mean heart rate across 79 historical TCT traversals; the −3.6 s/bpm slope shows
effort explains most between-ride spread. The red band marks the 160 ± 5 bpm target. Right: uncontrolled time distribution (CV 9%) and the protocol prediction
N (17.7, 1.252 ) min; fixing heart rate is expected to collapse the spread to the model’s residual uncertainty.



that case: Diebold–Mariano tests on per-origin score differ-                              or three-week load patterns (conventional, front/back-loaded,
ences with heteroskedasticity- and autocorrelation-consistent                             deload 50/25/0%, overload 115/130% and their sequences),
variance (lag four weeks) [49]; moving-block bootstrap with                               chosen by Eq. (2) and checked by the safety officer. Before
14-day blocks for intervals on aggregate differences [50];                                every instrument ride the ledger holds a sealed prediction for
and Giacomini–White tests of conditional predictive ability                               it; a ride is scored by the first traversal after sealing, one
to characterize when the agent helps [51].                                                traversal scores at most one prediction, and a ride through
                                                                                          the gates without the lap protocol is training data and never
C. Prospective phase                                                                      scores. The twin is refit once per week, after all of that week’s
                                                                                          predictions have been scored and before the next are sealed,
   Since 3 October 2026 the weekly cycle has run live on the                              so no prediction is ever made by a model that has seen the
athlete. Each week contains two instrument rides that never                               ride it predicts. Two further pre-registered components begin
change: the Trans Canada Trail climb held at 160 ± 5 bpm                                  once the baseline is established: randomization of weeks to
and the Nicoles descent at self-selected effort, each bracketed                           information-directed versus conventional (λt =0) design, with
by lap presses at the gates, on day 1 (fresh, after a rest day)                           realized information per ride as the outcome; and short-washout
and day 5 (loaded, after the week’s training). What the agent                             within-person interventions (sleep extension, time of day, heat,
designs is the training between them: one of fifteen one-, two-
                                                                                                                                                           8



TABLE I: Rolling-origin replay, 60 weekly origins, one-week horizon. CRPS (lower is better) with 95% moving-block bootstrap intervals; 90%-interval
coverage; Diebold–Mariano p against the twin row of the same target (HAC variance, lag 4). Segment time is scored in log-seconds. The “no segment
instruments” and “no HR quality control” ablations listed in Section VI-B were not run.

                                                               Segment time (n=81)                 Conditional climb HR [bpm] (n=106)
                      Method                                    CRPS               Cov90 DM p           CRPS           Cov90    DM p
                      Persistence                        0.052 [0.047, 0.060]      0.96      0.93 9.25 [7.50, 11.06]   0.88     <0.001
                      EWMA                               0.046 [0.040, 0.055]      0.96     0.31 7.87 [6.48, 9.19]     0.89     0.003
                      Ridge on covariates                0.109 [0.081, 0.134]      0.83     0.004 8.06 [6.69, 10.07]   0.83      0.13
                      GP on time + covariates            0.097 [0.070, 0.126]      0.75     0.026 8.06 [6.88, 9.46]    0.70     0.004
                      Banister, population τ             0.056 [0.049, 0.064]      0.91     0.21          —             —         —
                      Static twin (FFM / HR model)       0.048 [0.041, 0.063]      0.91       —    7.03 [6.13, 7.81]   0.87       —
                      E PI C OACH agentic twin (gated)   0.050 [0.042, 0.065]      0.91     0.007 7.00 [6.07, 7.82]    0.88     0.627
                         no identifiability gate         0.050 [0.042, 0.065]      0.91     0.007 7.00 [6.07, 7.82]    0.88     0.627
                         no registry (static refit)      0.050 [0.042, 0.065]      0.91     0.005 6.89 [5.98, 7.67]    0.88     0.313
                      ReAct agent (PHIA-style)           0.144 [0.085, 0.213]      0.84     0.014 8.91 [7.58, 10.26]   0.73     <0.001



                                        Rolling-origin replay CRPS (lower = better)
                                                Climb HR                                                                       Segment time
        Agentic twin (gated)                                     n.s.                      Agentic twin (gated)                  **

      Agentic twin (no gate)                                     n.s.                     Agentic twin (no gate)                 **

  Agentic twin (no registry)                                     n.s.               Agentic twin (no registry)                   **

     Static twin (reference)                                                          Static FFM (reference)

                         EWMA                                           **                                 EWMA                 n.s.

               ReAct baseline                                                ***                  ReAct baseline                                       *

                                  0                5                    10                                         0.0             0.1          0.2
                                                CRPS (bpm)                                                                     CRPS (log-speed)
Fig. 5: Rolling-origin replay CRPS (lower is better) with 95% moving-block bootstrap CIs; DM test significance vs the static twin reference (green dashed
line). The agentic system matches the static twin on both targets (n.s. on HR, p=0.007 on segment time); the ReAct baseline is significantly worse on both.



caffeine) in counterbalanced one-week blocks. Design details                       once it has three prior traversals. The corresponding twin
and power are in Appendix C.                                                       posteriors are in Figure 6.
                                                                                         a) Conditional heart rate.: The twin’s heart-rate response
D. Synthetic recovery check                                                        model attains CRPS 7.03 bpm (95% block-bootstrap interval
                                                                                   6.13–7.81) against 7.87 for an exponentially weighted average,
   A single subject cannot establish generality, and a posterior
                                                                                   8.06 for the Gaussian process, 8.06 for ridge regression on the
should not be interpreted before the model has been shown to
                                                                                   same covariates and 9.25 for persistence; Diebold–Mariano
recover known parameters. We therefore simulate athletes from
                                                                                   tests on per-origin losses give p = 0.003, 0.004, 0.13 and <
the fitted twin under the athlete’s actual training history and
                                                                                   0.001 respectively. Its 90% intervals cover 86.8% of outcomes
refit; with the real design the fitness–fatigue model recovers
                                                                                   (ECE 0.15); the model is slightly overconfident, which we
the daily performance state (r=0.996) and the load scale
                                                                                   attribute to ride-level variation that a one-week-ahead forecast
k1 and ratio k2 /k1 within their 90% intervals, but not the
                                                                                   cannot condition on.
time constants, whose posteriors remain close to their priors
                                                                                         b) Agentic replay.: With the fixed registry (invariants I7–
(Appendix F). A multi-athlete simulator for information-accrual
                                                                                   I8), the hypothesis loop runs causally at every origin: base
experiments is future work.
                                                                                   twin refit, Hypothesizer + Modeler/Critic against a frozen-clock
                                                                                   registry, Statistician evaluates open hypotheses (directional
E. Results                                                                         claims by Savage–Dickey on the stored fit; structural specs
   Table I and Figure 5 report the replay over 60 weekly origins                   by compiling a linear term and refitting), working model
after a 120-day warm-up; a segment becomes a forecast target                       = base + admitted structural specs (belief ≥ 0.5). Three
                                                                                                                                                                9




              τ1 fitness (d)                                         τ2 fatigue (d)                                                k2/k1
                                 prior
                                 posterior




         20       40       60       80      100            0        10        20         30        40                       2            4             6


Fig. 6: Posterior distributions from the retrospective twin. Left: cardiac drift γd is clearly positive (H1, belief 95%). Centre: fitness time constant τ1 remains
wide despite 79 instrument traversals (H4, belief 80%); the prospective fresh/loaded pair is designed to resolve this. Right: switching from 6 Mountain
Highway rides to 79 TCT rides tightened HR model noise from 6.5 to 5.3 bpm.



ablations share the same base fits and differ only in admission:       e) Prospective phase: three weeks.: Figure 8 shows
gated (identifiability gate on), no-gate, no-registry (static    every sealed prediction and every instrument ride from 3 to
twin). Across 60 origins the agentic system matches the static   22 October 2026: 20 predictions sealed, 14 scored, 4 withdrawn
twin on HR forecasting (CRPS 7.00 vs 7.03, p = 0.63)             before their outcome existed (I9), 2 open. The athlete rode 9
and segment time (0.050 vs 0.048, p = 0.007, marginally          protocol climbs at 160–164 bpm (one at 170) and 8 protocol
worse). The no-registry ablation is indistinguishable. I7 reduceddescents (one while no descent prediction was open); two
the hypothesis count from 62 to 40 by blocking duplicate         further climbs through the gates without laps were training and
registrations; I8 demoted 5 premature “supported” verdicts       were not scored.
when later data disagreed (belief trajectories in Figure 7). The    Descent. The first two descent predictions were sealed against
honest interpretation: 18 months of observational data, with     a gate that sat on the OSM junction node, 49 m from the
the current segment network, does not give the hypothesis loop   line the athlete rides; both outcomes fell 1.9 and 2.4σ below
enough contrast to improve forecasts. The designed experiments   the forecast (CRPS 0.155, 0.218 log-s). They were scored as
in the prospective phase (particularly the fresh/loaded pair and sealed, the gate was moved to the athlete’s lap-press point, the
the overload–rest contrast) are what the loop needs.             correction was logged as a registry event, and the forecast was
                                                                 changed from a historical median to the skill-model posterior.
     c) ReAct baseline.: A PHIA-style agent (the same lan-
                                                                 The five predictions since score CRPS 0.040 log-s (4.0%) with
guage model with a read-only SQL tool over the same
                                                                 all standardized residuals inside ±0.9: the descent instrument
history, asked to reason and return a Gaussian forecast) scores
                                                                 is calibrated.
8.91 bpm on conditional heart rate and 0.144 on segment
                                                                    Climb. Seven climb predictions scored a mean CRPS of 40 s
time, significantly worse than the twin on both (p < 0.001,
                                                                 (3.9% of the 17-minute climb) with 90%-interval coverage
p = 0.014) and worse than persistence on segment time. Free-
                                                                 6/7, but the athlete was faster than the forecast in six of seven,
form reasoning over the raw table does not recover what the
                                                                 mean standardized residual −0.71. Across the three weeks the
mechanistic model and even a moving average extract; this is
                                                                 protocol climb time fell from 1046 s (first three) to 1003 s (last
the gap the architecture is designed around.
                                                                 three) at matched heart rate, a slope of −4.8 s/day; the twin’s
     d) Segment time.: No method beats a simple exponentially forecast moved from 1060 to 1054 s. An exponentially weighted
weighted average of past traversal times (CRPS 0.046 in log- average of past climbs at 155–167 bpm, sealed at the same
seconds, i.e. ∼4.6%): the fitness–fatigue twin with learned moments, would have scored 31.5 s. This is the live counterpart
time constants scores 0.048, persistence 0.052 and a Banister of the replay’s segment-time result: the fitted fitness–fatigue
model with population constants 0.056, none significantly state is too slow to track a real training response, and the
different from one another, while the Gaussian process and pre-specified standard for the twin (match or beat the moving
ridge baselines are clearly worse (0.097, 0.109). This is the average) was not met.
forecasting face of the identifiability result of Section IV-E:     Pre-registered contrasts. Both live cycles sealed a fresh and
in this athlete’s observational record, training load carries a loaded climb prediction and stated the falsifier in advance:
no predictive information about segment time beyond recent a loaded test not slower than the fresh one counts against the
performance. We regard this as a finding, not a failure, and as modelled fatigue penalty. In week 1 the fresh test took 975 s
the strongest available motivation for the designed contrasts of and the loaded test 926 s; in week 2, 1031 s (6.0 h sleep) and
the prospective phase.                                           968 s. The falsifier fired twice. The refit that followed moved
                                                                                                                                                                   10




                                                Registry belief trajectories (agentic replay, 60 origins)
                                 H22: Subjective readiness score modulates techn                   H36: Submaximal climb heart rate exhibits marke
                           1.0                                                               1.0

                  Belief




                                                                                    Belief
                           0.5                                                               0.5


                           0.0                                                               0.0
                                 H2: Prior night sleep duration modulates subma                    H5: Ambient relative humidity increases submax
                           1.0                                                               1.0
                  Belief




                                                                                    Belief
                           0.5                                                               0.5


                           0.0                                                               0.0
                                 H7: Submaximal climb heart rate increases with                    H12: Time of day (hour_local) modulates submaxi
                           1.0                                                               1.0
                  Belief




                                                                                    Belief
                           0.5                                                               0.5


                           0.0                                                               0.0
                                 H13: Cumulative ride duration reduces descent s                     H15: Prior night heart rate variability (hrv_la
                           1.0                                                               1.0
                  Belief




                                                                                    Belief




                           0.5                                                               0.5


                           0.0                                                                0.0
                                c 2 5      2 6 r 26      2 6 g 26     t 2 6    c 2 6     2 7        25 eb 26 pr 26 n 26 ug 26 ct 26 ec 26 eb 27
                             De       Fe b          Ju n
                                              Ap proposed   Au     Oc
                                                                  under_testDe         b        Dec
                                                                                     Fe supported             A
                                                                                                       F refuted   Ju undetermined
                                                                                                                         A      O   D     F


Fig. 7: Belief trajectories for the eight most-tested hypotheses in the agentic replay (60 rolling origins). Colour encodes state: grey = proposed, blue = under
test, green = supported, red/orange = refuted/undetermined. Flat segments show hypotheses that reached a verdict; invariant I8 (no permanent verdicts) would
reopen them if later evidence disagreed.

TABLE II: Registry state on 22 October 2026 after three live cycles. Beliefs start at 0.5 and move only through Savage–Dickey evidence from stored fits,
subject to the identifiability gate. H1–H5 were pre-specified; H6–H11 were registered by the agent during the live cycles. Ledger: predictions scored / sealed
per hypothesis, with mean CRPS (climb in seconds, descent in log-seconds).

 Hypothesis                                           Formal object            Belief                 State           Ledger
 H1 Cardiac drift > 0                                 γd > 0                      0.95            under test          3/3 scored, CRPS 21.9 s
 H2 Drift larger in heat                              γdT > 0                     0.21             proposed           —
 H3 Less sleep slows descents                         δsleep < 0                  0.94            under test          7/7 scored, CRPS 0.082 (0.040 post-correction)
 H4 Fitness constant < 42 d                           τ1 < 42                     0.50         under test (gated)     4/4 scored, CRPS 54.1 s; falsifier fired 2/2
 H5 Aerobic response improved                         cwlast − cwfirst < 0        0.14             proposed           —
 H6 Climb HR rises with temperature                   γT > 0                      0.43             proposed           —
 H7 Wet trail slows descents                          δwet > 0                    0.65             proposed           —
 H8 Climb HR varies with time of day                  δhour ̸= 0                  0.62             proposed           —
 H9 Descent slows with elapsed ride time              δelapsed > 0                0.49             proposed           —
 H10 Fatigue constant < 7 d                           τ2 < 7                      0.55             proposed           —
 H11 Sleep affects climbing HR                         HR ̸= 0
                                                      δsleep                      0.36             proposed           —



the fitness–fatigue posterior to τ1 = 27 d [17, 59], P (τ1 <                             design ranked first by expected information gain was an
42) = 0.80, and τ2 = 3.7 d [0.7, 15.9]; the identifiability gate                         overload week (130% of the four-week mean); the safety officer
still refuses to move H4’s belief from 0.5 because the prior–                            vetoed it both times (ACWR 1.35 > 1.3; weekly load outside
posterior overlap is 0.84. Two weeks of designed contrast have                           ±15%) and the agent took the second-ranked two-week plan.
not resolved what eighteen months of observation could not,                              The ±15% tolerance made the pre-registered overload design
and the registry says so.                                                                logically infeasible. With the athlete’s written consent the cap
   The agent and the safety officer. In both live cycles the                             was raised to ACWR 1.5 and ±35% and a no-consecutive-
                                                                                                                                                             11



  Climb moving time at 160 ± 5 bpm (s)
                                                     gate + forecast                refit +                   refit +
                                         1150          correction                   cycle 1                   cycle 2


                                         1100

                                         1050

                                         1000

                                          950
                                                     instrument ride (laps)
                                          900        training ride through gates




                                          375
  Descent moving time (s)




                                          350

                                          325

                                          300

                                          275

                                          250

                                          225
                                                Oct 02       Oct 05        Oct 08   Oct 11    Oct 14         Oct 17             Oct 20            Oct 23

Fig. 8: The prospective ledger, 1–23 October 2026. Horizontal bars are sealed predictions (mean; shaded 90% interval) drawn from the moment of sealing to
the ride that scored them; dotted bars are predictions withdrawn before any outcome (I9). Filled circles are instrument rides (lap protocol), open circles the
outcome as scored, crosses training rides through the gates (not scored). Dashed verticals: the descent-gate and forecast correction (4 Oct) and the two live
refit-and-cycle events. Top: the climb forecast barely moves while the athlete’s time at 160 bpm falls by ∼ 80 s. Bottom: descent forecasts before and after the
instrument correction.



overload rule added, effective from the fourth cycle; the change physiology. Replay evaluates only the passive component of
is a protocol_change event in the registry and is not the system; the active component is evaluated prospectively
retroactive. The agent also registered six new hypotheses (heat, over a short horizon with limited power for small effects, and
time of day, wet surface, elapsed time, τ2 < 7 d, sleep on we state in advance which effects are detectable.
climbing heart rate); all remain proposed with | log BF| < 0.8.       b) Sensors.: Wrist optical heart rate and forest GPS are
   Audit trail. The registry holds 4 score_correction noisy; the quality-control and Student-t likelihoods mitigate
events from this period: three cases in which an ad-hoc but do not remove this. Virtual power is a modelling input, not
scorer matched the wrong ride (date-level instead of timestamp a measurement. Several device metrics used as baselines are
comparison; one traversal claiming two predictions; a training proprietary; the retrospective twin does not use them as inputs,
ride claiming a test prediction), each reversed with the wrong and if the auxiliary VO2 max channel is enabled we will report
value preserved, and the rules that now prevent them (first results with and without it.
traversal strictly after sealing; invariant I10, one observation      c) Identifiability.: The fitness–fatigue component is poorly
scores one prediction; lap protocol required). We report these identified after eighteen months of observational data (Sec-
because a system whose record is clean on first contact with tion IV-E) and may remain so after a short prospective block.
reality is a system whose record is not being kept. Full The system is designed to say so.
registry state, including the six agent-proposed hypotheses,          d) Self-experimentation and safety.: The prospective
is in Table II.                                                  phase is self-experimentation by a healthy adult with hard
                                                                 caps on heart rate and load, readiness and illness gates, and
                VII. L IMITATIONS AND E THICS                    interventions restricted to sleep, timing, heat exposure and
      a) One subject.: The empirical study is N =1 by de- caffeine within ordinary ranges. E PI C OACH is a research
sign, and the subject is an author. We argue generality on prototype and not medical advice; nothing in the design should
methodological grounds (the formalization, the benchmark, be read as safe for individuals with cardiovascular or other
the simulator and a pipeline that admits a second athlete conditions without clinical oversight. Garmin’s Connect API
without code changes), not on the basis of the single subject’s is unofficial; raw responses are snapshotted so that the study
                                                                                                                                                               12



is reproducible against API drift.                                                 [7] A. E. Ghareeb, B. Chang, L. Mitchener, A. Yiu, C. J. Szostkiewicz, J. M.
     e) Three weeks.: The prospective results are three weeks                          Laurent, M. T. Razzak, A. D. White, M. M. Hinks, and S. G. Rodriques,
                                                                                       “Robin: A multi-agent system for automating scientific discovery,” arXiv
of one athlete: 14 scored predictions and two fresh/loaded                             preprint arXiv:2505.13400, 2025.
contrasts. They are enough to show the ledger working,                             [8] I. Takahara and T. Mizoguchi, “Toward auditable AI scientists: A hypothe-
including against the twin, and not enough to estimate a                               sis evolution protocol for LLM agents,” arXiv preprint arXiv:2607.09195,
                                                                                       2026.
time constant. The randomized information-directed versus                          [9] A. Gelman and E. Loken, “The garden of forking paths: Why multiple
conventional comparison has not yet begun; every live week so                          comparisons can be a problem, even when there is no “fishing expedition”
far was information-directed. We also changed the instrument                           or “p-hacking” and the research hypothesis was posited ahead of time,”
                                                                                       Department of Statistics, Columbia University, 2013.
(gate position), the descent forecast method and the safety                       [10] B. A. Nosek, C. R. Ebersole, A. C. DeHaven, and D. T. Mellor, “The
thresholds during the phase. Each change is dated and logged,                          preregistration revolution,” Proceedings of the National Academy of
predictions sealed before a change were scored under the rules                         Sciences, vol. 115, no. 11, pp. 2600–2606, 2018.
                                                                                  [11] J. Gregory, D. P. Johns, and J. T. Walls, “Relationship between
in force when sealed, and none was retroactive; but a reader                           physiological and performance variables during cross-country mountain
should weigh the first three weeks as a shakedown of the                               bike racing,” Journal of Strength and Conditioning Research, vol. 21,
protocol as much as a test of the athlete.                                             no. 1, pp. 17–22, 2007.
                                                                                  [12] F. M. Impellizzeri and S. M. Marcora, “The physiology of mountain
     f) Language-model nondeterminism.: Model versions are                             biking,” Sports Medicine, vol. 37, no. 1, pp. 59–71, 2007.
frozen, temperature is zero, every call is cached per origin, and                 [13] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao,
spread over three seeds is reported.                                                   “ReAct: Synergizing reasoning and acting in language models,” in
                                                                                       International Conference on Learning Representations (ICLR), 2023.
                                                                                  [14] C. M. Fang, V. Danry, N. Whitmore, A. Bao, A. Hutchison, C. Pierce,
                         VIII. C ONCLUSION                                             and P. Maes, “PhysioLLM: Supporting personalized health insights with
                                                                                       wearables and large language models,” arXiv preprint arXiv:2406.19283,
   Personal-health agents have learned to read wearable data                           2024.
and to speak about it well. We have argued that the next step                     [15] M. Y. Li, E. B. Fox, and N. D. Goodman, “Automated statistical model
is not better speech but accountable learning: a system that                           discovery with language models,” in International Conference on Machine
                                                                                       Learning (ICML), 2024.
holds explicit, probabilistic claims about one person, commits                    [16] G. E. P. Box, “Science and statistics,” Journal of the American Statistical
to predictions before seeing outcomes, chooses what to observe                         Association, vol. 71, no. 356, pp. 791–799, 1976.
next, and is judged by whether it was right. E PI C OACH realizes                 [17] J. R. Lloyd, D. Duvenaud, R. Grosse, J. B. Tenenbaum, and Z. Ghahra-
                                                                                       mani, “Automatic construction and natural-language description of
this loop for a mountain biker with nothing but a watch, with                          nonparametric regression models,” in Proceedings of the AAAI Conference
a protocol that lets language models do what they are good                             on Artificial Intelligence, 2014.
at (propose mechanisms, choose instruments, negotiate with a                      [18] K. Gandhi, M. Y. Li, L. Goodyear, A. Bhatia, L. Li, A. Bhaskar,
human, explain) while deterministic tools fit, score, gate and                         M. Zaman, and N. D. Goodman, “BoxingGym: Benchmarking progress
                                                                                       in automated experimental design and model discovery,” arXiv preprint
record. Eighteen months of wrist data did not resolve a fitness                        arXiv:2501.01540, 2025.
time constant, and three weeks of designed rides have so far                      [19] E. W. Banister, T. W. Calvert, M. V. Savage, and T. Bach, “A systems
shown the twin to be too slow to follow the athlete it models;                         model of training for athletic performance,” Australian Journal of Sports
                                                                                       Medicine, vol. 7, no. 3, pp. 57–61, 1975.
a system that writes that down, keeps the wrong scores next                       [20] E. W. Banister, “Modeling elite athletic performance,” in Physiological
to the corrected ones, and can answer “not yet, and here is the                        Testing of the High-Performance Athlete, J. D. MacDougall, H. A. Wenger,
week that would help” is, we think, the right kind of coach.                           and H. J. Green, Eds. Human Kinetics, 1991, pp. 403–424.
                                                                                  [21] T. Busso, “Variable dose-response relationship between exercise training
                                                                                       and performance,” Medicine & Science in Sports & Exercise, vol. 35,
                 C ODE AND DATA AVAILABILITY                                           no. 7, pp. 1188–1195, 2003.
                                                                                  [22] P. Hellard, M. Avalos, L. Lacoste, F. Barale, J.-C. Chatard, and G. P.
   The E PI C OACH implementation, the full hypothesis registry                        Millet, “Assessing the limitations of the Banister model in monitoring
and prediction ledger, the replay benchmark, and the opera-                            training,” Journal of Sports Sciences, vol. 24, no. 5, pp. 509–520, 2006.
tional protocol are released at https://github.com/Bmoradi93/                     [23] K. Vermeire, M. Ghijs, J. G. Bourgois, and J. Boone, “The fitness–
                                                                                       fatigue model: What’s in the numbers?” International Journal of Sports
epicoach-agent.                                                                        Physiology and Performance, vol. 17, no. 5, pp. 810–813, 2022.
                                                                                  [24] K. M. Vermeire, F. Van de Casteele, M. Gosseries, J. G. Bourgois,
                                                                                       M. Ghijs, and J. Boone, “The influence of different training load
                              R EFERENCES                                              quantification methods on the fitness–fatigue model,” International
 [1] J. Cosentino, A. Belyaeva, X. Liu, N. A. Furlotte, Z. Yang, C. Lee,               Journal of Sports Physiology and Performance, vol. 16, no. 9, pp. 1261–
     E. Schenck, Y. Patel, J. Cui, L. D. Schneider et al., “A personal health          1269, 2021.
     large language model for sleep and fitness coaching,” Nature Medicine,       [25] D. Kolossa, M. A. Bin Azhar, C. Rasche, S. Endler, F. Hanakam,
     vol. 31, 2025.                                                                    A. Ferrauti, and M. Pfeiffer, “Performance estimation using the fitness-
 [2] M. A. Merrill, A. Paruchuri, N. Rezaei, G. Kovacs, J. Perez, Y. Liu,              fatigue model with Kalman filter feedback,” International Journal of
     E. Schenck, N. Hammerquist, J. Sunshine, S. Tailor et al., “Transforming          Computer Science in Sport, vol. 16, no. 2, pp. 117–129, 2017.
     wearable data into personal health insights using large language model       [26] R. L. Kravitz, N. Duan, and the DEcIDE Methods Center N-of-1 Guidance
     agents,” Nature Communications, vol. 17, 2026.                                    Panel, “Design and implementation of N-of-1 trials: A user’s guide,”
 [3] A. A. Heydari, K. Gu, V. Srinivasan, S. Tailor et al., “The anatomy of a          AHRQ Publication No. 13(14)-EHC122-EF, 2014.
     personal health agent,” arXiv preprint arXiv:2508.20148, 2025.               [27] N. Duan, D. Norman, C. Schmid, I. Sim, and R. L. Kravitz, “Personalized
 [4] M. Ozolcer and S. W. Bae, “SePA: A search-enhanced predictive agent for           data science and personalized (N-of-1) trials: Promising paradigms for
     personalized health coaching,” arXiv preprint arXiv:2509.04752, 2025.             individualized health care,” Harvard Data Science Review, 2022, special
 [5] Z. He, J. Wang, B. Zhang, and Y. Li, “Knowledge-grounded large lan-               Issue 3.
     guage model for personalized sports training plan generation,” Scientific    [28] E. J. Daza and L. Schenk, “Causal inference for N-of-1 trials,” arXiv
     Reports, vol. 16, p. 6793, 2026.                                                  preprint arXiv:2406.10360, 2024.
 [6] C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, and D. Ha, “The AI         [29] E. J. Daza and L. Schneider, “MoTR and PSTn: Building a causal
     scientist: Towards fully automated open-ended scientific discovery,” arXiv        engine for estimating the within-individual average treatment effect using
     preprint arXiv:2408.06292, 2024.                                                  wearable sensors,” arXiv preprint arXiv:2208.00739, 2022.
                                                                                                                                                     13



[30] S. Z. Ishita, S. Kaliappan, M. Rashik, D. A. Epstein, and R. Karkar,           joined when endpoints lie within 15 m, then densified to
     “CASEbot: A conversational agent for structuring and personalizing the         5 m. Chains shorter than 100 m are dropped. Paved roads
      design of self-experiments in personal health,” in Proceedings of the
      2026 CHI Conference on Human Factors in Computing Systems (CHI                (unclassified) are retained for segment discovery but
     ’26), 2026.                                                                    excluded from the heart-rate and fitness–fatigue models, where
[31] A. R. Novak, K. J. M. Bennett, J. Fransen, and B. J. Dascombe, “A              virtual power is unreliable at road speeds.
      multidimensional approach to performance prediction in Olympic distance
      cross-country mountain bikers,” Journal of Sports Sciences, vol. 36, no. 1,         b) Snapping and runs.: A KD-tree over all chain points
      pp. 71–78, 2018.                                                              returns, for each GPS sample, the nearest chain and its along-
[32] W. M. Bertucci, S. Rogier, and R. F. Reiser, “Effects of mountain bike
      tyre pressure and tread, cycling speed and terrain on rolling resistance
                                                                                    trail coordinate s, accepted if within 20 m. Gaps of up to 30 s
      and aerodynamic drag,” Journal of Sports Sciences, vol. 31, no. 14, pp.       on a chain are bridged. A run needs ≥ 30 samples, ≥ 20
      1–8, 2013.                                                                    snapped, and a robust slope |ds/dt| ≥ 0.3 m/s (otherwise the
[33] R. E. Kass and A. E. Raftery, “Bayes factors,” Journal of the American
      Statistical Association, vol. 90, no. 430, pp. 773–795, 1995.
                                                                                    rider is dithering at a junction).
[34] T. Gneiting and A. E. Raftery, “Strictly proper scoring rules, prediction,           c) Consensus gates.: Chain length is binned at 10 m; each
      and estimation,” Journal of the American Statistical Association, vol.        ride’s coverage interval [min s, max s] increments the bins it
      102, no. 477, pp. 359–378, 2007.
[35] D. V. Lindley, “On a measure of the information provided by an                 spans; the segment is the longest contiguous bin range with
      experiment,” The Annals of Mathematical Statistics, vol. 27, no. 4, pp.       count ≥ max(5, 0.6 × rides touching the chain) and length
      986–1005, 1956.                                                               ≥ 250 m. Segments are typed by the median altitude change
[36] K. Chaloner and I. Verdinelli, “Bayesian experimental design: A review,”
      Statistical Science, vol. 10, no. 3, pp. 273–304, 1995.                       over traversals (climb > 15 m, descent < −15 m, otherwise
[37] T. J. Gabbett, “The training—injury prevention paradox: should athletes        rolling).
      be training smarter and harder?” British Journal of Sports Medicine,                d) Traversals.: Within a run, entry is the first crossing
      vol. 50, no. 5, pp. 273–280, 2016.
[38] M. D. Hoffman and A. Gelman, “The No-U-Turn sampler: Adaptively                of the entry gate (a run that starts more than 30 m inside the
      setting path lengths in Hamiltonian Monte Carlo,” Journal of Machine          segment is not a full traversal), exit the first subsequent crossing
      Learning Research, vol. 15, no. 1, pp. 1593–1623, 2014.                       of the exit gate. Accepted if ≥ 85% of samples lie within the
[39] D. Phan, N. Pradhan, and M. Jankowiak, “Composable effects for flexible
      and accelerated probabilistic programming in NumPyro,” arXiv preprint         gates ±15 m, no inter-sample gap exceeds 90 s, progress is
      arXiv:1912.11554, 2019.                                                       monotone for ≥ 90% of steps, and duration ≥ 60 s. Laps yield
[40] B. Bent, B. A. Goldstein, W. A. Kibbe, and J. P. Dunn, “Investigating          multiple traversals per run.
      sources of inaccuracy in wearable optical heart rate sensors,” npj Digital
      Medicine, vol. 3, p. 18, 2020.                                                      e) Known failure modes.: GPS error under canopy of 10–
[41] J. W. Navalta, J. Montes, N. G. Bodell, R. W. Salatto, J. W. Manning,          25 m can place a sample on a parallel trail; the 20 m snap radius
      and M. DeBeliso, “Concurrent heart rate validity of wearable technology
      devices during trail running,” PLoS ONE, vol. 15, no. 8, p. e0238569,         and the monotone-progress test suppress most such errors.
      2020.                                                                         Trails absent from OpenStreetMap, or unnamed, produce no
[42] J. C. Martin, D. L. Milliken, J. E. Cobb, K. L. McFadden, and A. R.            segments; in this study 20% of ride samples in the main area
      Coggan, “Validation of a mathematical model for road cycling power,”
      Journal of Applied Biomechanics, vol. 14, no. 3, pp. 276–291, 1998.           were unmatched, mostly unsanctioned connectors. Entry/exit
[43] E. F. Coyle and J. González-Alonso, “Cardiovascular drift during               jitter of ∼1 s is 2% of a 60 s descent, so we prefer segments
      prolonged exercise: new perspectives,” Exercise and Sport Sciences            of several minutes for hypothesis testing and report duration
      Reviews, vol. 29, no. 2, pp. 88–92, 2001.
[44] S. Edwards, The Heart Rate Monitor Book. Sacramento, CA: Fleet                 alongside every estimate.
      Feet Press, 1993.                                                             f) Per-traversal record.: segment_id, activity_id,
[45] Google, “Agent development kit (ADK),” https://google.github.io/               t_entry, t_exit, duration_s, moving_s,
      adk-docs/, 2025.
[46] A. Vehtari, A. Gelman, and J. Gabry, “Practical Bayesian model                 has_stop, cover, hr_mean, hr_max,
      evaluation using leave-one-out cross-validation and WAIC,” Statistics         hr_ok_frac, d_alt, dist_m,
      and Computing, vol. 27, no. 5, pp. 1413–1432, 2017.                           elapsed_at_entry_s, vp_mean_w, grade_mean,
[47] T. Rainforth, R. Cornish, H. Yang, A. Warrington, and F. Wood, “On
      nesting Monte Carlo estimators,” in International Conference on Machine       wx_temp_c, wx_humidity, wet_now, sleep_h,
      Learning (ICML), 2018.                                                        hrv_last_night, readiness_score, week,
[48] A. Foster, M. Jankowiak, E. Bingham, P. Horsfall, Y. W. Teh, T. Rainforth,     day_index.
      and N. Goodman, “Variational Bayesian optimal experimental design,”
      in Advances in Neural Information Processing Systems (NeurIPS), 2019.
[49] F. X. Diebold and R. S. Mariano, “Comparing predictive accuracy,”
      Journal of Business & Economic Statistics, vol. 13, no. 3, pp. 253–263,                              A PPENDIX B
      1995.                                                                                     M ODEL S PECIFICATIONS AND P RIORS
[50] H. R. Künsch, “The jackknife and the bootstrap for general stationary
      observations,” The Annals of Statistics, vol. 17, no. 3, pp. 1217–1241,
      1989.                                                                              a) Heart-rate      response       (Eqs.      4–5).:
[51] R. Giacomini and H. White, “Tests of conditional predictive ability,”          τhr ∼ LogNormal(ln 30, 0.3) s; αr ∼ N (µα , σα2 )
      Econometrica, vol. 74, no. 6, pp. 1545–1578, 2006.                            with µα ∼ N (120, 152 ), σα ∼ HalfNormal(8);
                                                                                    βw ∼ N (βw−1 , σβ2 ), β0 ∼ N (0.25, 0.12 ) bpm/W,
                             A PPENDIX A                                            σβ ∼ HalfNormal(0.01); γT ∼ N (0.5, 0.52 ) bpm/◦ C;
                         S EGMENT D ISCOVERY                                        γd ∼ N (4, 32 ) bpm/h; γdT ∼ N (0, 0.52 ); us ∼ N (0, σu2 ),
     a) Trail network.: For each riding area (a bounding box                        σu ∼ HalfNormal(6); ν ∼ Gamma(2, 0.1) truncated below at
around a cluster of ride start points) we query OpenStreetMap                       2; σhr ∼ HalfNormal(3). The recursion is implemented with
for ways with a highway tag in {path, track, cycleway,                              jax.lax.scan on 5 s-downsampled series. The segment-
footway, bridleway, service, unclassified, steps} and a name;                       aggregate variant replaces Eq. (4) by HRr,s = HRss    r,s + ϵr,s
responses are cached. Ways sharing a name are greedily                              with the same linear predictor evaluated at traversal means.
                                                                                                                                                        14




Fig. 9: The two instruments in relief (satellite view, one ride, track coloured by heart-rate zone). Left: the Trans Canada Trail climb, 2.06 km at 7.2% on
wide compacted gravel with no technical features: heart rate is a clean function of mechanical work here, which is why it serves as the fitness instrument.
Right: Nicoles Trail, 1.16 km and −158 m of tight, rooted singletrack: heart rate decouples from work and time is governed by skill, which is why it is
modelled separately (Section IV).



      b) Skill state (Eq. 6).: µs ∼ N (log medians , 0.22 ); λs ∼             we report the rank stability under M ∈ {250, 500, 1000}. For
HalfNormal(0.1); S0 = 0, σS ∼ HalfNormal(0.02); δ· ∼                          the hypothesis-level quantity, y is scored under each sub-model
N (0, 0.052 ); η ∼ tν (0, ση ), ση ∼ HalfNormal(0.05).                        MH and π | y follows from Bayes’ rule over the registry.
      c) Fitness–fatigue    (Eq. 6).: Load: Banister exponential                     f) Menu Dt .: Archetypes: (i) long low-intensity ride, 90–
                                          r
TRIMP w = t ∆t·HRrt ·0.64 e1.92 HRt with heart-rate reserve
               P
                                                                              180 min, heart rate below a zone-2 cap; (ii) climb repeats
fraction HRrt = (HRt − HRrest )/(HRmax − HRrest ); HRmax                      on segment s at heart-rate target h ∈ {Z3, Z4}, 3–5 repeats;
from the 99.5th percentile over all rides, HRrest from the de-                (iii) descent laps on segment s′ , 4–8 laps, easy climbs between;
vice’s nightly value. Priors: τ1 ∼ LogNormal(ln 42, 0.3), τ2 ∼                (iv) deload: ≤ 50% of mean weekly load; (v) standardized
LogNormal(ln 7, 0.4), k1 ∼ HalfNormal(0.05), k2 /k1 ∼                         test: eight-minute climb on a designated segment at a fixed
LogNormal(ln 2, 0.3), p0 ∼ N (0, 1) on standardized perfor-                   heart-rate target preceded by a fixed warm-up; (vi) rest. Each
mance. Measurement: log vr,s | HR-matched = as + b pd(r) +                    archetype is crossed with day-of-week and time-of-day options
δ ⊤ cr + ϵ, and VO2 maxdev d   = c0 + c1 pd + ϵ′ with ϵ′ allowed to           drawn from the athlete’s stated availability and the weather
be heavy-tailed because device VO2 max updates are discrete.                  forecast; the Experiment Designer prunes to 20–40 candidates
Model comparison between τ hypotheses uses bridge-sampling                    before scoring.
Bayes factors and PSIS-LOO [46]; we report prior–posterior                                                   P t = w7 /w28 ∈ [0.8, 1.3] after
                                                                                     g) Feasibility set.: ACWR
overlap (Bhattacharyya coefficient) for every parameter.                      the candidate is appended;         week w ∈ [0.85, 1.15]× block
      d) Weekly updates.: The twin is refit by NUTS once per                  target; ≥ 1 rest day in any 7-day window; heart-rate target
week, after all predictions for the week are scored and before                ≤ 0.92 HRmax ; device readiness ≥ 30; no athlete-reported
new ones are sealed; between refits the stored posterior is used              illness or injury in the daily check-in; candidate day marked
as is. Ledger predictions are drawn from it: the climb from                   available.
the fitness–fatigue posterior at 160 bpm (segment level, last
daily state, heart-rate slope, season), the descent from the skill                                    A PPENDIX C
posterior with the skill state advanced one random-walk step                             P ROSPECTIVE N- OF -1 D ESIGN AND P OWER
and covariates at protocol conditions.                                              a) Randomization.: Weeks are the unit for the
      e) Nested Monte Carlo.: With θ(n) ∼ pt (θ), n = 1..N ,                   information-accrual comparison, randomized in pairs so that
and y (n) ∼ p(y | θ(n) , d),                                                   each fortnight contains one information-directed and one
                  N h                                                          conventional week. Within each week, two instrument rides are
     d θ (d) = 1
                 X
     EIG              log p(y (n) | θ(n) , d)                                  scheduled on non-adjacent days; the intervention order (AB
               N n=1                                                           or BA) is randomized with counterbalancing across weeks.
                                         M                                     Sleep extension requires a 1-day washout; caffeine a 48-
                                      1 X                      i
                              − log         p(y (n) | θ(m) , d) ,              hour abstinence baseline; time-of-day/heat manipulations are
                                      M m=1
                                                                               constrained by forecast.
with N = M = 500 and the inner samples shared across de-                            b) Instrument ride.: Two instrument rides per week on
signs [47]. The estimator is biased upward at finite M ; because               the declared climb, at a fixed heart-rate target of 160 ± 5 bpm
we only rank designs within a menu, the bias is tolerable, and                 chosen by the athlete as sustainable for the ∼ 17 min effort
                                                                                                                                                          15



TABLE III: Discovered segments. Area A is the home hill (instrument network), B and C two mountain networks. Declared routes are gate-to-gate
instruments; the rest are discovered. Moving time is the median over traversals; CV is the coefficient of variation of moving time.

               Trail (OSM name)                                           Area     Kind     Length [m]   ∆alt [m]   Rides   Moving [min]   CV [%]   HR
               TCT, lower gate → summit road (declared)                   A        climb         2061       +148      90            17.2      9.1   150
               Nicoles via Poplar (declared)                              A      descent         1159       -158      31             4.8     14.8   123
               Dead Moped Trail                                           A        climb          692        +28      86             4.6     11.5   140
               Upper Cut Trail                                            A      descent          353        -51      38             1.2     25.8   120
               Arts Road                                                  A       rolling         339        +12      31             1.6     18.5   141
               North Road Trail                                           A       rolling         430        -13      30             1.9     18.3   127
               Sidewinder South                                           A        climb         1074        +96      29            10.9      8.6   147
               North Road                                                 A        climb          365        +19      27             2.4     35.3   140
               Sidewinder                                                 A        climb          971        +81      27             9.9      6.2   146
               Sidewinder                                                 A      descent          971        -76      24             3.0     11.9   133
               Sidewinder South                                           A      descent         1070        -92      18             2.7     15.6   117
               Mountain Air Trail                                         A       rolling        1349         +9      18             7.0      9.4   156
               Cougar Creek Trail                                         A       rolling         430        +11      18             2.1     12.5   149
               North Road Trail                                           A      descent          487        -49      16             2.5      8.7   124
               North Road                                                 A        climb          755        +20      14             4.4     12.9   124
               Pipeline Trail                                             A        climb          650        +26      11             4.8      8.8   146
               Lower Snake Trail                                          A      descent          519        -72       7             2.2      8.0   128
               North Road Trail                                           A        climb          487        +47       5             5.1      3.7   144
               Grouse Mountain Highway                                    B        climb          840        +61      10             7.7      6.3   152
               Access road, lot → 7th switchback (declared, superseded)   B        climb         5896       +425       6            47.3      8.9   157
               Skid Road Ascent                                           B        climb          469        +49       9             4.8      6.5   152
               Ramble On                                                  B       rolling         402         +6       8             3.4      9.8   150
               Seventh Secret                                             B      descent         1028       -160       7             7.5      6.2   103
               Executioner Ascent                                         B        climb          362        +46       7             5.0      3.3   160
               For the Kids                                               B        climb          519        +60       7             6.1     10.3   141
               Expresso                                                   B      descent         1490       -207       5             6.9      3.7   100
               Empress Bypass                                             C      descent          510        -62       6             1.7      2.4   128




(watch alert on the band; lap press where the gravel meets the                        distribution_json, registered_at,
summit road ends the step), followed by one traversal of the                          scored_at, crps, logscore, brier);
designated descent at self-selected effort. The two rides occupy                      evidence(id, hypothesis_id, fit_id,
fixed positions: a fresh test on the first day after the weekly                       log_bf, method, recorded_at); fits(fit_id,
rest day and a loaded test on day 5, after the week’s training.                       model_spec_hash, data_cutoff,
The pair is the within-week fatigue contrast the fitness–fatigue                      posterior_path, loo, created_at);
model needs to separate τ2 from τ1 without special weeks; with                        events(id, hypothesis_id, kind, payload,
one ride a week that contrast is unavailable. Everything between                      actor, at).
the tests is the athlete’s normal training (rides, football, strength                       b) Invariants      enforced    by      the     store.:
work; all enter the load series, with the caveat that heart-rate-                     (i) logit_belief is written only by record_evidence;
based load under-counts strength sessions). Outcomes: moving                          (ii) record_evidence rejects a fit_id absent from
time on the climb at the protocol heart rate, descent moving                          fits or with data_cutoff later than the target ride;
time. Each instrument ride carries ≈ 60 exp-TRIMP, about                              (iii) predict rejects registered_at > ride start;
12% of the athlete’s weekly load, so the plans in the design                          (iv) transition to SUPPORTED requires πH ≥ 0.8, to REFUTED
menu differ only in the remaining training.                                           πH ≤ 0.2, to UNDETERMINED a test budget exhausted
      c) Estimand and analysis.: ψ = E[log v (1) − log v (0) ]                        with | log BFcum | < log 3; (v) refine/merge require a
within person. Primary analysis: Bayesian regression of log v                         parent with a verdict or evidence; (vi) every call is logged
on treatment, block effects, a linear trend and AR(1) residuals;                      with its actor; (vii) a single piece of evidence is capped at
secondary: randomization test permuting treatment labels                              | log BF| ≤ 10; (viii) directional evidence from a parameter
within blocks; sensitivity: time-varying g-formula with one-step                      posterior is admitted only if the posterior standard deviation
carryover [28].                                                                       shrank by ≥ 10% relative to the prior (identifiability gate);
      d) Power.: With traversal-speed CV ≈ 3% (to be verified                         (ix) a prediction is never deleted: if its target can no longer
     p retrospective data) and n = 12 per arm, SE(ψ̂) ≈
on the                                                                                be observed it is marked withdrawn with a reason, and
0.03 2/12 ≈ 0.012; a 4% effect gives z ≈ 3.3 (power ≈ 0.9                             a prediction whose outcome exists cannot be withdrawn;
at α = 0.05), a 2% effect gives power ≈ 0.4. Hypotheses                               (x) an observation (outcome_ref: activity and segment)
whose plausible effect is below 3% are declared untestable in                         scores at most one prediction. Each invariant has a unit test;
the prospective window and remain in the replay-only track.                           record_evidence additionally rejects any caller other
                                                                                      than the statistician tool.
                      A PPENDIX D                                                           c) Hypothesizer prompt (abridged).:
   R EGISTRY S CHEMA , T OOL P ROTOCOL AND P ROMPTS                                          You are a sports physiologist reviewing
                                                                                             diagnostics for ONE athlete. You will
a) Tables.: hypotheses(id, text, formal_spec,                                                receive structured residual reports from
state, logit_belief, created_by,                                                             fitted models and a list of open
                                                                                             hypotheses. Propose at most 3 new
created_at, parent_ids); predictions(id,                                                     hypotheses. For each:
hypothesis_id, target_ride,                                                                    - claim: one sentence, specific to
                                                                                                                               16



         this athlete, falsifiable;                               (two of three covering the truth); τ2 and k2 /k1 were recovered
       - mechanism: 1-2 sentences with a                          in all three; the latent performance trajectory correlated 0.95–
         literature pointer;
       - formal: a predicate over named model                     0.99 with the truth. The design identifies performance but not
         parameters OR a model-template                           the time constants.
         change from the allowed list
         (add_covariate, add_interaction,
         add_changepoint, add_random_walk,                                                A PPENDIX G
         split_by_condition);                                                           DATA I NVENTORY
       - prior_logodds: a number in [-2, 2]
         with one line of justification;                             Activities by type: 265 strength sessions (274 h), 222
       - test: which segment(s), which                            mountain-bike rides (295 h), 45 walks, 22 mountaineering
         outcome, how many traversals needed.
     You cannot set beliefs, compute
                                                                  days, 19 treadmill runs, 15 overland trips, 13 trail runs and
     evidence, or approve workouts. Do not                        52 others; all 653 have FIT files. Monthly ride counts range
     restate hypotheses already in the                            from 1 (February 2026) to 22 (August 2026), with a winter
     registry; refine or merge instead.
                                                                  trough from December to March. One device (Forerunner 965,
     d) Critic prompt (abridged).:                                firmware 22.24–29.05) recorded every activity. Weather records
     Review the proposed model-template
     change. Reject if: it introduces a
                                                                  exist for every ride.
     parameter not separable from an                                 Daily wellness completeness over 556 days: readiness 98%,
     existing one given the listed                                acute/chronic load 98%, resting heart rate, stress and body
     instruments; it uses descent heart
     rate as a fitness signal; it
                                                                  battery 99%, sleep and overnight HRV 77% (the watch was
     conditions on post-outcome                                   not worn on some nights). Daily load: mean exponential TRIMP
     information; or an equivalent                                55 per day with 116 rest days; the vendor’s proprietary load
     hypothesis exists in lineage.
     Return accept|revise|reject with
                                                                  correlates with exponential TRIMP at r = 0.87.
     one paragraph.

                       A PPENDIX E
                  W ORKOUT W RITE -BACK
   The pusher serializes d⋆ as a cycling workout with ordered
steps, each with a duration or distance end condition and a
heart-rate-zone or custom heart-rate target, creates it through
the workout service and schedules it on the target date; the
watch receives it after the phone application syncs, which the
athlete is prompted to do. Because the endpoint is unofficial,
the payload schema is validated against a workout created in
the vendor’s own interface and retrieved through the same API,
and a file-based fallback (FIT workout copied to the device
over USB) is maintained. All requests are paced and retried
with exponential backoff; raw responses are archived.

                      A PPENDIX F
              S YNTHETIC R ECOVERY C HECK
   Each simulated athlete draws τ1 ∼ U(25, 60), τ2 ∼ U(4, 12),
k2 /k1 ∼ U (1.2, 3), γd ∼ U (1, 8), γdT ∼ U (0, 1), a segment
network subsampled from the real one, a ride-frequency process
matched to the real athlete’s calendar, heart-rate noise and
dropout rates matched to measured quality statistics, and a
weather series bootstrapped from the real archive. We simulate
(a) the historical load history for replay-pipeline calibration
and (b) prospective seasons under information-directed versus
conventional policies. Reported: parameter-recovery coverage
of 90% intervals; information accrual curves; CRPS/ECE of
the full pipeline on simulated held-out weeks.
     a) Recovery under the athlete’s actual design.: As a first
check we simulated HR-adjusted climb speeds from τ1 = 35,
τ2 = 7, k2 /k1 = 2 and a 6% Student-t noise on the real load
history and the real 188 observation times, segments and heart
rates (a 21% latent performance swing), then refit the bounded
model. Over three seeds the posterior median of τ1 was 45, 58
and 46 days with 90% intervals [28, 65], [41, 76] and [30, 66]
