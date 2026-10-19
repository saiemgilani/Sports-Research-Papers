<!-- source: library/preprints/arXiv/2026/2026 - From Metrics to Decisions in NBA Analytics - Zhou et al..pdf -->
<!-- arXiv:2609.27245 | https://arxiv.org/abs/2609.27245 | filed 2026-10-19 -->

# From Metrics to Decisions in NBA Analytics: A Critical Integrative Review and Decision-Readiness Framework

                                               From Metrics to Decisions in NBA Analytics: A
                                              Critical Integrative Review and Decision-Readiness
                                                                   Framework
                                                                                   Yang Zhou1       Tianyu Guan2,1,∗
                                                                               1
                                                                                   TY SPORTS ANALYTICS INC., Canada
                                                                  2
                                                                      Department of Mathematics and Statistics, York University,
arXiv:2609.27245v1 [stat.AP] 23 Sep 2026




                                                                                            Toronto, Canada

                                                                              Yang Zhou: yangzhou@tysportsanalytics.com
                                                                       ∗
                                                                           Corresponding author: Tianyu Guan, tguan@yorku.ca


                                                                                                Abstract
                                                     National Basketball Association (NBA) teams have increasingly detailed metrics, but better
                                                 predictions do not necessarily improve decisions. This critical integrative review draws on prior
                                                 reviews, citation tracing, and topic searches across seven research streams: on-court action,
                                                 player value, role, lineup synergy, availability, draft and development, and contracts and roster
                                                 construction. An observation–state–action–decision–evaluation chain organizes the synthesis.
                                                 Six decision-readiness gates guide our assessment: point-in-time validity, uncertainty, context
                                                 portability, action feasibility, opportunity-set observability, and evaluation, with requirements
                                                 matched to each claim. The reviewed literature is strongest in measuring and predicting individ-
                                                 ual components of a decision. Evidence is less developed at interfaces that combine components,
                                                 transfer them across settings, and compare feasible actions. We outline a proposed deployment
                                                 workflow, a reporting contract, and a research agenda covering player transport, role substitu-
                                                 tion, roster fragility, legal action generation, and asset valuation. The 2023 collective bargaining
                                                 agreement and forthcoming 3-2-1 Draft Lottery illustrate how institutional changes generate re-
                                                 search questions. Models should inform evaluable comparisons of feasible choices. While its
                                                 effect on organizational decision quality remains an empirical question, the framework provides
                                                 a diagnostic and reporting structure for matching decision claims to evidence requirements.

                                           Keywords: NBA; basketball analytics; decision readiness; basketball operations; roster construc-
                                           tion


                                           1 Introduction
                                           NBA analytics now reaches well beyond box-score comparisons. Play-by-play records support
                                           possession-level analysis, lineup data describe combinations of players, and optical tracking records
                                           movement on and off the ball. Schedules, injury reports, contracts, transactions, and prospect
                                           records extend this work to decisions about participation and team building. Researchers have used
                                           these sources to estimate player contribution, value possessions, describe roles, forecast injuries and
                                           draft outcomes, and construct rosters. Prior reviews and foundational work document the statistical
                                           foundations, performance measures, and data sources on which these applications depend (Chen

                                                                                                   1
From Metrics to Decisions in NBA Analytics                                               Critical integrative review


et al., 2025; Huyghe et al., 2022; Kovalchik, 2023; Kubatko et al., 2007; Sarlis and Tjortjis, 2020;
Terner and Franks, 2021; Zhou and Li, 2024).
   These works approach the field from several directions. Kubatko et al. establish possession-
based statistical foundations; Sarlis and Tjortjis survey player and team evaluation; and Terner
and Franks examine models of game play, strategy, and performance, identifying causal inference
as a major research need. Huyghe et al. focus on the player and contextual constraints affecting
NBA game play. Kovalchik covers tracking methods and action valuation across sports, while Zhou
and Li organize basketball research by dimension, granularity, task, and stakeholder question. Chen
et al. assess data–method alignment across 206 performance-analysis studies. Table 1 sets out how
our review builds on this work. We take a particular decision—who acts, when, and with which
alternatives—as the starting point, then ask whether the available estimates can support it. This
perspective connects on-court research with availability, development, draft, contract, transaction,
and roster decisions.

   Table 1: Positioning this review relative to prior reviews and foundational basketball work.
 Source                Primary                 Boundary addressed by the present review
                       organizing lens
 Kubatko et al.        Possession accounting   Connects statistical measurement to specific coaching and
 (2007)                and foundational        personnel actions
                       basketball statistics
 Sarlis and Tjortjis   Methods and metrics     Separates observed performance, portable ability, price, and
 (2020)                for player and team     team-specific decision value
                       evaluation
 Terner and Franks     Statistical models of   Extends from estimators to action feasibility, organizational
 (2021)                player and team         context, and deployment evaluation
                       performance
 Huyghe et al.         Player and contextual   Extends beyond game-play determinants to development, draft,
 (2022)                constraints             contracts, and roster choices
                       underpinning NBA
                       game play
 Kovalchik (2023)      Player-tracking data    Examines whether tracking outputs support interventions and
                       and methods across      evaluated NBA decisions
                       sports
 Zhou and Li           Dimensions,             Adds a decision timestamp, feasible and plausibly available
 (2024)                granularity, tasks,     actions, coupled cross-stream states, and explicit evaluation
                       and stakeholder
                       questions in
                       professional
                       basketball
 Chen et al. (2025)    Data–method             Shifts to claim-specific time validity, uncertainty, transport,
                       alignment in            feasible and available actions, and evaluation
                       basketball
                       performance analysis
 Present review        Observation–state–      Connects seven operations streams and sets out research and
                       action–decision–        reporting priorities
                       evaluation chain


   The difficulty becomes clear when a model leaves the setting in which it was estimated. A plus-
minus coefficient may summarize contribution alongside observed teammates yet say little about
performance in a new role. A lineup forecast may rank five-player units without accounting for
fatigue or the bench minutes needed to complete a rotation. Similarly, predicting injury risk does


                                                         2
From Metrics to Decisions in NBA Analytics                                          Critical integrative review


not identify the effect of resting a player, and predicting salary does not establish what a contract
is worth to a particular team. These are gaps between the question a model answers and the choice
its user faces. More granular data or a more complex algorithm may help, but neither resolves the
mismatch on its own.
   Our concern is how estimates enter basketball-operations decisions. Such decisions concern a
specific team at a specific time, use incomplete information, and draw on alternatives that may be
difficult to observe. A player’s projected contribution matters alongside the role available to that
player, the price of acquiring the contract, and the team’s tolerance for risk. The analytical target
is the value of an action under those conditions, over an appropriate horizon.
   We organize the review around the evidence needed for these choices. Contribution, role, syn-
ergy, and availability describe related aspects of a player’s value: what the player can produce, in
which setting, alongside whom, and at what workload. Contracts, draft rights, and the collective
bargaining agreement (CBA) shape the cost and feasibility of acting on those estimates. Figure 1
shows the links from observations to an evaluated decision.
                                                          legal and market       counterfactual
             time validity          portability               feasibility          evaluation
 Observations
                          State                Candidate
 events, lineups,                                                      Decision rule         Evaluation
                        estimates                 actions
    tracking,                                                            objective,          wins, health,
                      value, role, fit,         play, rest,
     health,                                                           risk, horizon,        development,
                       availability,          develop, draft,
    contracts,                                                          constraints            flexibility
                           price                sign, trade
      assets

         Information environment: public                          Decision environment: team
           and private access, provenance,                        context, contracts, CBA, draft
             missingness, revision history                      rights, competition and bargaining

                                          learning and regime change


Figure 1: The NBA analytics data-to-decision pipeline. Model performance at one stage does not
validate the next interface. Decision-ready evidence must preserve the information available at the
decision time, transport estimates to the intended context, generate feasible actions, and evaluate
choices against credible alternatives.

   The review makes three connected contributions. It synthesizes evidence across seven NBA
research streams to identify where well-studied components remain weakly connected to decisions.
It integrates established methodological requirements into six decision-readiness gates, using the
dated team decision as the organizing unit and matching the requirements to each claim level.
It then translates these diagnoses into a reporting contract and proposed deployment workflow
(Section 7). The contribution lies in this integration and operationalization, rather than in a new
statistical estimator. The 2023 CBA and the 3-2-1 Draft Lottery approved in 2026 illustrate how
changes in constraints and incentives generate research questions.
   The scope covers competitive basketball operations: on-court action, player evaluation and devel-
opment, availability, draft, contracts, transactions, and roster construction. Betting, fan sentiment,
ticket demand, media value, and officiating fall outside it unless they directly affect one of these



                                                      3
From Metrics to Decisions in NBA Analytics                                   Critical integrative review


decisions. Throughout, we assess a study against the claim it makes. Descriptive research has value
in its own right; the additional requirements arise when its findings are used to support a choice.


2 Review Purpose, Scope, and Analytical Lens

2.1 The questions that organize the review

The review is organized around three questions.

1. What decision-relevant states does NBA research estimate? This includes player con-
   tribution, role and capability, lineup synergy, availability and workload capacity, development,
   market value, and contract value.
2. How far does each research stream travel from observation to action? We distinguish
   measurement, prediction, causal or counterfactual estimation, constrained prescription, and
   prospective evaluation.
3. Which interfaces must be built next? We examine connections among player states, team
   context, legal constraints, market opportunities, uncertainty, and evaluation, with particular
   attention to the new CBA and lottery regimes.

   These questions guide the selection and comparison of studies. We give particular attention
to work that changes the target of analysis, strengthens validation, measures a previously unob-
served state, or makes a decision amenable to evaluation. Small differences in model performance
receive less attention when they leave the underlying decision claim unchanged. Selection priori-
tizes evidence that directly informs the decision interfaces under review, rather than comprehensive
coverage of each field.

2.2 Review approach and evidence selection

A critical integrative review suits this purpose because the relevant studies differ in their units of
analysis, terminology, data access, and publication format. We use the evidence map, available
as a machine-readable CSV on GitHub, to examine how their findings connect and how far their
claims extend. The review is not an exhaustive census or a PRISMA-style systematic review, and
its study counts cannot be used to estimate the prevalence of methods or findings in NBA research.
   The evidence cutoff was 1 September 2026. We began with the terminology and seed references
in Table 1, then followed backward and forward citations into statistics, computer science, sports
medicine, economics, operations research, and management. Targeted searches supplemented this
process. Sources included scholarly web search and publisher or DOI pages; PubMed/MEDLINE
and PubMed Central for health and availability; arXiv, PMLR, SSRN, MIT Sloan proceedings,
institutional repositories, and author pages for methodological work; and official NBA and NBA
Players Association archives for rule states. Search terms combined basketball or NBA with per-
formance and plus-minus; tracking, spacing, defense, and action value; role, lineup, rotation, and
network; injury, workload, and participation; or draft, development, salary, contract, trade, and
roster optimization. We followed further leads when a paper introduced a relevant estimand, data
layer, validation design, or decision interface. Search functions differed across sources, so the

                                                  4
From Metrics to Decisions in NBA Analytics                                  Critical integrative review


searches cannot be treated as equivalent database runs. The companion materials record the query
families, access status, and retained evidence.
   Eligible sources included primary empirical studies, methodological papers demonstrated on
NBA data, and full conference papers. A source had to estimate a decision-relevant state, examine
transport or uncertainty, model an intervention or constrained action, or document a relevant data
or institutional limitation. Broader basketball and multisport studies were included where they
directly informed an NBA decision interface. Reviews supplied context and terminology. Official
NBA and NBA Players Association documents established legal and policy states; they were not
used as evidence of a rule’s effects.
    Five discovery workstreams produced 132 records. These were search-management categories;
the synthesis subsequently grouped the evidence into seven substantive research streams. Recon-
ciliation by DOI, normalized title, and report version left 127 unique reports, of which 51 were
retained. Seven prior-review and NBA foundations brought the NBA synthesis corpus to 58 re-
ports: 50 inspected in full text, five available through abstracts or verified metadata and used only
for positioning or scope claims, and three official rule documents. Eight non-NBA methodological
works support the framework separately and do not enter the NBA evidence counts or maturity
judgments. The supplementary search-and-synthesis record documents eligibility, deduplication,
counts, and the rationale for every cell of Figure 4. A 66-row evidence map, available as a machine-
readable CSV on GitHub, links all cited sources to their roles in the review. Supplementary Table S4
provides the report-level crosswalk of claim levels, decision interfaces, and principal limitations.
   For each retained report, we extracted the observation unit, data access, target or estimand, val-
idation or identification design, uncertainty output, and claimed decision. We then assessed what
further evidence would be needed to use the estimate in that decision. The extracted evidence di-
mensions were assessed separately rather than combined into a quality score. Public reproducibility,
for example, says little on its own about a model’s relevance to a trade, while restricted medical
data may support an operationally useful study. Figure 4 compares the maturity of research in-
terfaces on this basis; it does not rank papers or count publications. Both authors worked jointly
on screening, extraction, and coding. During manuscript preparation, both authors independently
cross-checked the source claims and the extracted information for all 66 records included in Ta-
ble S4, as well as all Figure 4 cell ratings. Discrepancies were resolved through joint review, and
the final coding was confirmed by both authors. No formal estimate of inter-rater agreement is
reported.


2.3 Claim levels and decision readiness

We distinguish five claim levels:

1. Measurement: What happened, and how should observed contribution or behavior be sum-
   marized?
2. Prediction: What outcomes can be predicted in a declared future or held-out sample, using a
   specified information set?
3. Causal or counterfactual estimation: What would change under a specified intervention
   or alternative context?


                                                 5
From Metrics to Decisions in NBA Analytics                                                      Critical integrative review


4. Constrained prescription: Which action is preferred under an explicit objective, information
   set, and feasible action set?
5. Prospective evaluation: Did an implemented decision rule improve outcomes under deploy-
   ment against a credible comparator?

   Retrospective replay can support a decision claim under stated identification and support as-
sumptions, but does not constitute prospective deployment evaluation. Scientific credibility con-
cerns whether a study answers its stated question; decision readiness concerns whether its output
can inform a choice. We assess the latter through six decision-readiness gates: point-in-time valid-
ity, uncertainty, context portability, action feasibility, opportunity-set observability, and evaluation.
The requirements depend on the claim. A descriptive paper has no obligation to enumerate legal
trades, but a trade recommendation must address both legality and counterpart acceptance. Con-
strained prescription names a claim level; action feasibility names one gate used to assess it. Public
reproducibility and organizational auditability are recorded separately, including for studies based
on protected data.


3 A Decision-Readiness Framework for NBA Analytics

3.1 Specifying the decision

Let It be the information available to a team at date t, Rt the relevant rule and contract state, Mt
a specified scenario for the partly observed market opportunity set, and A(It , Rt , Mt ) the actions
admissible in that scenario. Let Yt:t+h (a) denote the multidimensional consequences of action a
over a common declared horizon h, and let Vt:t+h (a) = U (Yt:t+h (a)) be their scalar organizational
value under a declared objective. Define the corresponding scalar loss as Lt:t+h (a) = −Vt:t+h (a).
For transactions, Mt depends jointly on each required party’s reservation value, outside option,
and latent willingness to transact; legal admissibility is therefore necessary but not sufficient for a
transaction to be treated as plausibly available. A generic mean–risk decision is

          a∗t (Mt ) = arg        max           {E[Vt:t+h (a) | It , Rt , Mt ] − λ ρ(Lt:t+h (a) | It , Rt , Mt )} .     (1)
                            a∈A(It ,Rt ,Mt )

   The dependence on It and Rt , held fixed in each scenario comparison, is suppressed on the
left-hand side.
   The outcome vector can include wins, playoff advancement, player development, health, payroll,
asset value, and future flexibility. The mapping U converts those outcomes to a scalar value; it
does not by itself specify the organization’s full risk preference. Downside aversion is represented
by λ ≥ 0 and the risk functional ρ, applied to the conditional loss distribution. Examples include
expected excess loss above a specified threshold and conditional value-at-risk under an explicit loss
convention. CVaR at the 95th percentile, for instance, can summarize mean loss in the worst five
percent of joint availability, playoff, and asset-value scenarios.
   For decisions spanning several seasons, U must specify how outcomes at different dates are
discounted or weighted. Those weights may reflect the team’s competitive timeline and mandate.
The objective, time weights, and risk preferences are organizational inputs to be declared or elicited;


                                                               6
From Metrics to Decisions in NBA Analytics                                                 Critical integrative review


predictive fit alone does not determine them. Transaction flexibility is included in Y , avoiding
a second risk penalty for the same consequence. This formulation follows the distinction among
actions, uncertain consequences, values, and losses in decision analysis and incorporates constraints
in the feasible set (Berger, 1985; Boyd and Vandenberghe, 2004).
   For a causal or prescriptive claim, Y (a) denotes an action-specific potential outcome. It cannot
generally be recovered by averaging observed outcomes among cases that selected a. If Itobs is the
information observed by the researcher and Dt the realized action, then E[Y | Itobs , Dt = a] need
not equal E[Y (a) | Itobs ]. Unrecorded coaching, player, or organizational information may affect
both selection and outcomes.
   Equation 1 compares actions within a stated market scenario. A team may know terms that the
researcher cannot observe. If acceptance is uncertain to the team itself, the controllable action is to
submit an offer; acceptance, rejection, and negotiation costs then enter Y (a). Beliefs about those
outcomes must carry through expected value and downside risk. A recommendation to complete a
transaction remains conditional on attainable terms. Many studies estimate contribution or injury
risk; fewer identify action effects, reconstruct available opportunities, or evaluate the resulting
choice.
   Each part of the decision object motivates a readiness gate. The time index on It establishes the
need for point-in-time validity. Value and loss distributions, together with ρ, require uncertainty
to be represented in the choice. Applying an outcome model to a new team, role, opponent,
or rule regime raises the question of context portability. Membership in A requires legal and
operational feasibility, while Mt makes explicit the need to observe, reconstruct, or bound the
available opportunities. Finally, comparing U (Y ) across actions calls for an evaluation design suited
to the claim. The six decision-readiness gates thus identify different ways an otherwise credible
estimate can fail to support a choice. Reproducibility and organizational auditability allow others
to inspect that assessment.
   Consider two models that rank all realistically available players in the same order. The more
accurate model may leave a team’s choice unchanged while improving its assessment of uncertainty
or downside. An estimate of role portability or joint availability could be more useful if it changes
which alternatives the team should consider. Value-of-information analysis formalizes this link
between information, choice, and outcome (Howard, 1966). It helps explain why improvements in
average predictive error can have limited operational value.


3.2 Player value is a coupled state

A single rating is convenient for comparing players, but a team needs to know how that value
depends on the intended use. For player p at time t in decision context d, we write

                           Vp,t,d = f (Ap,t , Rp,t,d , Sp,t,d , Hp,t , Cp,t,d , Zt,d ) ,                          (2)

   where A is ability or expected contribution, R is role, S is synergy with teammates and system,
H is availability or workload capacity, C is cost and contractual control, and Z describes the
team’s competitive and institutional context. Relevant elements of Zt,d include playoff position,
roster depth, competitive timeline, apron or hard-cap status, and the rules in force. We impose
no additive or linear form on f . The value of a player’s ability may depend on role, health, and

                                                        7
From Metrics to Decisions in NBA Analytics                                              Critical integrative review


contractual rights, with institutional thresholds changing the value of the same component across
teams. Figure 2 depicts these dependencies.
   For example, a deep contender may be able to absorb a player’s absences and offer a com-
plementary role, whereas a shallow roster may face expensive replacement needs. The baseline
contribution estimate alone would miss that difference. Cost, rights, and the team’s competitive
timeline determine whether the projected contribution justifies acquiring or retaining the player.

                 Ability                                     Synergy
                                        Role                                       Availability
                 expected                                    teammate
                                 capability bundle                               workload capacity
               contribution                                and system fit
                                  What function                                   Can the player
              What can the                                  With whom
                                    is assigned?                                   participate?
             player produce?                                 and how?

                         coupled player-state vector (Ap,t , Rp,t,d , Sp,t,d , Hp,t )



                Cost and rights                 team-date                    Team context
                  salary, years,              decision value                  needs, depth,
                 options, assets                   Vp,t,d                     timeline, risk



                                   supported, dated and feasible choice


                                                             acquire              allocate
                 deploy / rest          develop
                                                             / retain              assets


Figure 2: An integrated player-state model. Ability, role, synergy, and availability form a coupled
player-state vector; cost, rights, and team context determine whether and how that state creates
value for a particular team and dated decision. Arrows indicate dependencies, not a claim that one
universal functional form is correct.


Illustrative decision trace. Consider two general managers assessing the same high-impact
wing at a hypothetical trade deadline t. One leads a deep contender; the other leads a top-heavy
team near an apron threshold. Both use the same baseline contribution estimate, absence scenarios,
and outcome horizon h. The candidate actions are the wing acquisition package (A), an alternative
capability bundle (B), and retaining the current roster (C). Suppose baseline contribution favors
A. Table 2 illustrates how a legal screen can change that comparison before role, risk, and market
terms determine a recommendation.




                                                      8
From Metrics to Decisions in NBA Analytics                                            Critical integrative review



                     Table 2: Illustrative decision trace for two team contexts.
  Readiness         Deep contender                                  Top-heavy apron team
  gate

  Point-in-time     Freeze It , contracts, rights, objective, and   Use the same cutoff and horizon, but freeze
  validity          horizon before comparing actions                this team’s own roster and rule state
  Uncertainty       Assess whether replacement depth buffers        Estimate downside under the same absence
                    lost minutes under the stated absence           scenarios using this team’s replacement
                    scenarios                                       capacity
  Context           Assess whether projected contribution           Assess role overlap and test contribution
  portability       transports to the complementary role;           across plausible role and minutes
                    require evidence for that deployment            assignments
  Action            In this hypothetical screen, A, B, and C are    Package A requires a transaction tool
  feasibility       legal; assess their rights and future-tool      unavailable to this team at t; exclude A and
                    costs                                           compare legal actions B and C
  Opportunity-set   Counterpart acceptance is unknown;              Apply the same acceptance check to this
  observability     condition acquisition on acceptable,            team’s affordable package set; legality alone
                    attainable terms                                is insufficient
  Evaluation        Archive the action, forecast, and baseline;     Preserve the same outcome definitions, but
                    assess contribution, depth, and flexibility     declare this team’s weights and downside
                    over h                                          tolerance in advance


   The screen leaves the contender comparing A, B, and C, while the apron team compares B with
C, despite the shared baseline ranking. The contender could prefer A if its role-adjusted contribu-
tion outweighs cost and downside; the apron team could prefer B only if the bundle improves on
retention under its own objective. These are hypothetical comparisons, conditional on acceptable,
attainable terms. Changes in price, absence risk, or replacement quality warrant reassessment.
Evaluating either choice requires a credible comparator and design, since the unchosen outcome is
unobserved.

3.3 What the data measure

Each data source reveals some aspects of a player’s or team’s state and leaves others uncertain.
Table 3 summarizes these measurement limits.
   Tracking data reveal off-ball movement, although tactical intent and portability remain difficult
to infer. League medical surveillance can improve injury ascertainment, but public injury reports
cannot reproduce it. Transaction records reveal agreed prices while omitting failed offers and
opportunities that never reached negotiation. These examples make the observation process part
of the decision problem: what was measured, for whom, and when it became available all affect the
claim the data can support. Section 7.2 returns to these questions in the reporting requirements.


4 Evidence Across Seven Research Streams

4.1 On-court action and possession value

Decision question. Given the ball, score, clock, player locations, matchup, and opponent re-
sponse, which action should a player or lineup take?

                                                       9
From Metrics to Decisions in NBA Analytics                                     Critical integrative review



Table 3: Major NBA data layers, their decision-relevant contribution, and their principal boundary.
 Data layer         What it makes more observable             What remains unresolved
 Box score and      Outcomes, usage, basic efficiency,        Teammate and opponent context, off-ball
 game logs          participation, career trajectories        contribution, role, and causal attribution
 Play-by-play       On/off context, events, substitutions,    Within-possession movement, defensive
 and possessions    score and clock states                    assignment, strategy selection, and
                                                              hidden coaching information
 Lineups and        Realized combinations, stint outcomes,    Untried combinations, why lineups were
 rotations          substitution patterns                     chosen, fatigue, feasibility of alternative
                                                              rotations
 Shot and           Spatial behavior, contest, movement,      Proprietary access, cross-vendor
 tracking data      action sequences, role features           definitions, tactical intent, transfer to a
                                                              new team or role
 Injury and         Reported status, games missed, return     Clinical state, workload dose, reporting
 participation      dates, schedule and travel exposure       changes, medical intervention and
 records                                                      selection
 Prospect and       Pre-draft performance, measurements,      Team boards, interviews, workout
 draft data         market beliefs, selection and career      selection, opportunity after selection,
                    outcomes                                  class-specific priors
 Contract,          Salary, years, options, reported terms,   Complete clauses, rejected offers,
 transaction and    completed moves, pick ownership           counterpart preferences, precise
 asset data                                                   historical legal action sets


   Possession-based accounting made it possible to separate pace from efficiency and compare events
on a common basis (Kubatko et al., 2007). Shot-selection models built on this foundation by weigh-
ing shot quality against the opportunity cost of continuing a possession (Skinner, 2012). Spatial
and tracking studies brought shooting locations, defensive regions, movement, and individual ac-
tions into the analysis (Franks et al., 2015; Kovalchik, 2023; Miller et al., 2014). Multiresolution
possession and transition models estimate how expected value changes as play unfolds (Cervone et
al., 2016; Sandholtz and Bornn, 2020). Jutamulia and Hosoi restrict the comparison to immediate
pass and shot alternatives. Their approach compares realized actions with modeled opportunities
and helps distinguish the creation of opportunities from their execution (Jutamulia and Hosoi,
2025).
   These studies connect observations to choices at the timescale of play, bringing them close to
an action-value framework. Their estimates nevertheless depend on the actions that players and
coaches selected and on how the defense responded. Uncommon actions may have little support
in the data. A high modeled value gives no assurance that a play can be taught, executed, or
sustained against an adapting opponent. Held-out possessions can test predictive performance, but
evaluating a coaching intervention requires an identification strategy, credible off-policy evaluation,
or prospective implementation. For propensity-weighted evaluation, action probabilities must be
logged or defensibly estimated and overlap must be adequate. Rare actions increase variance; un-
observed coaching information can undermine the assignment model (Swaminathan and Joachims,
2015).
   Personnel and lineup composition offer a useful next step. A pass may have high expected
value because a particular receiver or screener is on the floor, or because the spacing permits it.
Estimating action values conditional on those capabilities and on defensive response would make


                                                    10
From Metrics to Decisions in NBA Analytics                                    Critical integrative review


the results more informative for coaches. It would also clarify which recommendations are likely to
survive changes in personnel or opponent strategy.


4.2 Player value across teams and roles

Decision question. How much would a player contribute over a future horizon for a particular
team, role, and set of teammates?
   Adjusted plus-minus methods confront the difficulty of attributing jointly produced outcomes
to individual players. Substitutions overlap, minutes are selected, and some players rarely ap-
pear apart. Regularization reduces instability from collinearity and limited lineup overlap, while
Bayesian models express uncertainty in contributions and rankings (Barrientos et al., 2023; Fearn-
head and Taylor, 2011). In held-out games, Sill (2010) reduced game-margin RMSE from 12.01 to
11.47 points with regularization, conditional on the games’ realized lineups and possessions. This
is predictive evidence, but not a forecast using only pregame information. By contrast, Deshpande
and Jensen (2016) estimate retrospective, context-dependent contributions to winning; they ex-
plicitly caution against interpreting those estimates as future player performance. Meta-analytic
work further shows that plausible metrics can differ in discrimination, stability, and independence
(Franks et al., 2016). Labor-economics research questions whether regularized adjusted plus-minus
isolates individual productivity when teammates’ contributions are complementary (Ghimire et al.,
2020).
   The resulting estimates describe contribution after adjustment for the context represented in
the model. Using them for recruitment requires an additional inference: that the contribution
will persist with different teammates, coaching, or responsibilities. Shrinkage addresses sampling
variability, but it cannot establish that inference. Validation needs to reflect the target, whether
that is retrospective contribution, near-term performance in the same setting, portable skill, or
contribution under a specified team change.
   Team and role changes provide opportunities to test transport. A model can be fitted using
only information available before a switch, then assessed against subsequent minutes, role, lineup
context, and contribution. The assumptions linking the two settings need to be stated explicitly
(Pearl and Bareinboim, 2014). Calibration and uncertainty coverage matter alongside ranking
accuracy: a team needs to know both the contribution projected for its intended deployment and
how uncertain that projection is.


4.3 Roles, capabilities, and assignments

Decision question. Which functions can a player perform, which role will be assigned, and how
will that role change in a new system?
  Traditional positions group players with quite different responsibilities. Tracking features, spatial
measures, networks, and clustering describe shooting, creation, screening, passing, rebounding, rim
protection, and defensive movement in more detail (Muniz and Flamand, 2022; Skinner and Guy,
2015). Such representations help compare players, identify hybrid roles, describe roster composition,
and provide inputs to performance and acquisition models. The tracking-oriented model of Skinner
and Guy (2015), for example, was demonstrated on 780 hand-coded sequences from three 2011



                                                  11
From Metrics to Decisions in NBA Analytics                                  Critical integrative review


playoff games. Its limited cross-lineup checks provide evidence about skill transfer within that
setting, rather than broad validation after team or coaching changes.
   Interpreting those representations requires care. An observed role partly reflects what an organi-
zation asks a player to do. A cluster summarizes similarities in measured features, so membership
alone does not establish that two players are interchangeable. Roles also change within games and
across seasons, teammates, and coaches. A fixed label can obscure the adaptability a team hopes
to acquire.
   It is useful to distinguish capability, the actions a player can perform at an acceptable level;
assignment, the functions the team asks the player to undertake; and execution, what the player
does in a particular setting. Longitudinal and multi-view representations could help estimate
transitions among these states. Tests on unseen teams and roles would then provide evidence
about whether the representation supports the intended use. For roster construction, this means
estimating degrees of substitutability among capability bundles, beyond assigning each player a
single archetype.


4.4 Synergy, lineups, and rotation choice

Decision question. Which combinations of players create value beyond the sum of individual
contributions, and what rotation should be used against a given opponent?
   Research on synergy examines interaction effects, productivity spillovers, complementary skills,
networks, and lineup performance (Arcidiacono et al., 2017; Devlin and Uminsky, 2020; Kuehn,
2017; Maymin et al., 2013). Structural production and possession models also compare hypothetical
teammate configurations and trades. These comparisons are substantive counterfactual exercises,
but their interpretation depends on assumptions about production and selection; they do not
identify the effect of deploying a new lineup without those assumptions. Predictive work uses
player features and related representations to estimate the performance of units with little or no
shared playing time (Martonosi et al., 2023). Strategic-network studies offer another perspective
by describing team process and the concentration of ball movement (Fewell et al., 2012).
   Lineup selection complicates all of these approaches. Coaches use information about practice,
playbook knowledge, health, matchups, development, and interpersonal considerations that re-
searchers may not observe. A lineup absent from the data could be infeasible, unsuitable, or simply
unnecessary in the games played. Even units that appear regularly do so against selected opponents
and in selected score states. These features limit what can be learned by comparing their observed
outcomes.
   The distinction between observed interaction, predicted lineup performance, and interventional
lineup value helps specify the problem. Observed interaction describes departures from an additive
benchmark among players who shared the court. Predicted lineup performance concerns a specified
unit, including one that has not played. Interventional lineup value concerns the change caused
by deploying one feasible lineup rather than another. Isolating synergy additionally requires an
explicit benchmark for additive individual contributions. Temporal holdouts can assess prediction;
intervention effects also require support checks and an identification strategy addressing coaching
selection and opponent context. The rotation also matters. A strong five-player unit may be a
poor choice if it leaves the team unable to cover the remaining minutes.


                                                 12
From Metrics to Decisions in NBA Analytics                                     Critical integrative review


4.5 Availability and workload decisions

Decision question. Should a player play, rest, reduce workload, or follow a return-to-play pro-
gression, and what is the roster consequence of each choice?
   NBA injury studies cover long-run epidemiology, schedule associations, forecasting, and workload
measurement (Cohan et al., 2021; Drakos et al., 2010; Lewis, 2018; Mack et al., 2019; Russell et
al., 2021; Teramoto et al., 2017). Public analyses commonly draw on missed games, reports,
transactions, news, and box-score measures of load. The league’s player injury and illness database
offers more structured ascertainment, although the data are unavailable for public replication (Mack
et al., 2019). Studies of schedules, travel, and time zones add information about environmental
exposures (Charest et al., 2021).
  These sources measure different aspects of availability. An official designation, a missed game,
a minutes restriction, and a clinical diagnosis are not interchangeable. A player may be fit to
participate but rested, cleared for limited minutes, or classified under a reporting rule that changed
during the sample. Public labels thus reflect both health and organizational reporting decisions.
Any model intended to guide participation needs to account for that observation process.
   The intervention question is harder. An association between recent load and injury does not
establish whether reducing minutes would improve health or how replacement minutes would af-
fect team performance and risk. Research on rest and playoff performance, along with emerging
heterogeneous-treatment approaches, begins to address this question (Belk et al., 2017; Nakamura-
Sakai et al., 2024). Using internal surveillance data, Herzog et al. (2026) found no statistically
significant differences in subsequent regular-season injury risk across rest/load-management groups;
the outcome was an in-game injury causing at least two consecutive missed games. The estimates
concern that outcome and study population. Rest remained nonrandom, so the result does not
establish that an individual rest intervention is ineffective. Participation decisions call for a defined
intervention and attention to time-varying confounding, competing risks, recurrent events, and in-
dividual uncertainty. For team decisions, the useful output is a joint distribution over participation,
workload capacity, performance, recurrence, and replacement quality.
   The same issues carry into roster construction. For a team with concentrated salary commit-
ments and limited replacement tools, correlated absences can create substantial downside. Linking
availability forecasts to lineup and contract models would allow a team to compare that exposure
with the costs and benefits of greater depth. The reviewed literature offers limited validation of
this connection.


4.6 Drafting and development opportunities

Decision question. Which prospect should a team select or acquire, at what pick price, and
how should that player be developed after selection?
   Draft studies use college production, measurements, combine results, and mock drafts to predict
selection, early performance, career outcomes, and market consensus (Berger and Daumann, 2021;
Berri et al., 2011; Fisher and Montague, 2025; Ichniowski and Preston, 2017). These targets capture
different processes. Draft order reflects team evaluations and broader market expectations; early
minutes depend partly on the opportunity a team provides; and career contribution combines
ability with health, coaching, development, and survival in the league. A model can predict draft

                                                   13
From Metrics to Decisions in NBA Analytics                                   Critical integrative review


position accurately while reproducing biases embedded in historical team selection decisions. The
studies also differ in validation: Berri et al. (2011) report retrospective regressions without held-
out predictive evaluation, whereas Fisher and Montague (2025) evaluate dated mock drafts against
actual selection order.
   Associations between draft order, later playing time, and career survival illustrate the difficulty
of separating prospect quality from organizational opportunity (Staw and Hoang, 1995). If realized
career production is the sole outcome, a model may receive credit for anticipating the selection
process rather than improving on it. Draft evaluation should trace pre-draft signals through mar-
ket beliefs, the team’s choice, development opportunities, and subsequent contribution. Missing
combine tests, workouts, and interviews also require interpretation as selection states, rather than
being entered as zeroes.
    The pick itself changes the decision. Selecting a prospect fourth and selecting that prospect
twenty-fourth involve different opportunity costs, contracts, alternative boards, and trade possibil-
ities. A useful evaluation would preserve the information available at the pick and compare player
outcomes together with asset cost. Archived consensus boards and validation across draft classes
are especially valuable because both class strength and the information available to teams change
over time. The retained literature is stronger on prospect selection and post-selection opportunity
than on evaluations of development interventions; the stream label should not imply equal coverage
of both.


4.7 Contracts, acquisition, and roster construction

Decision question. Should a team sign, extend, trade, waive, or retain a player, and which
legally and commercially feasible portfolio best serves its objectives?
   Salary research examines compensation, discrimination, offensive and defensive returns, and pre-
contract performance (Ehrlich et al., 2019; Kaplan, 2024; Wen et al., 2023). Return-on-investment
measures combine performance and salary to estimate apparent surplus (Lautier, 2025). These
results describe how the labor market rewards players, but a team deciding whether to offer a
contract faces a different question: what would the player be worth in its roster? Bargaining,
maximum and minimum salary rules, service, timing, cap conditions, and scarce alternatives all
influence the observed price. Salary is therefore an outcome to be explained as well as a cost to be
paid.
   Acquisition and roster models approach this choice more directly, combining player metrics with
role balance, network fit, or optimization (Brill et al., 2023; Ke et al., 2024; Maymin, 2017; Muniz
and Flamand, 2023). Work on risk and uncertainty places team building in a dynamic setting
(Schmidt, 2021); a recent preprint develops a rolling-horizon stochastic formulation (Zhang et al.,
2026). The practical difficulty is defining the actions a team can take. A payroll constraint captures
only part of the CBA. Transactions also depend on roster slots, contract types, rights, exceptions,
salary matching, hard caps, aprons, draft assets, timing, and counterpart willingness. Bringing
these conditions into the candidate generator would allow optimization to address a more realistic
set of choices.
  Legal permission and market availability remain separate even in a detailed rule model. A
permitted trade may have no willing counterparty. Observed trades are selected agreements, while


                                                 14
From Metrics to Decisions in NBA Analytics                                   Critical integrative review


a non-trade could represent rejection, lack of availability, a dominated option, or a proposal never
considered. Roster models need some account of these possibilities, whether through probabilities,
bounds, or clearly labeled assumptions. They also need to carry uncertainty in player states and
the value of future options into the comparison.


4.8 Cross-stream synthesis

Across the seven streams, research tends to provide stronger support when the target stays close
to the observation unit: a possession, stint, game, draft selection, or contract. More assumptions
are needed as an estimate is transferred to a new role, used to choose a workload, or combined
with other estimates in an acquisition decision. Selection and feasibility then become prominent.
Coaches, medical staff, teams, prospects, and counterparties influence which actions appear in the
data and which alternatives were available. The following section examines these shared difficulties.


5 Connecting Estimates to Decisions:
  Strong States, Weak Interfaces
Figure 3 maps the relationships between measurement, player states, and decisions. Tracking and
spatial-defense data inform contribution and synergy as well as role. Possession models contribute
to player evaluation and tactical choice; lineup and passing networks describe roles and comple-
mentarity; and schedule and participation records inform availability (Cervone et al., 2016; Fewell
et al., 2012; Franks et al., 2015; Mack et al., 2019; Muniz and Flamand, 2022; Skinner and Guy,
2015). The less established links involve combining these estimates, applying them to a different
setting, and comparing actions subject to the rules and opportunities at the time.


5.1 Aligning observation and decision units

The observation unit often differs from the decision unit. Studies analyze player-seasons, stints,
possessions, games, or contracts; a team chooses an action concerning a player in a particular setting
and at a particular date. Bridging the two takes additional work. A player-season prediction needs
a deployment assumption, a lineup-stint prediction needs a rotation, and a salary prediction needs
the alternatives available in negotiation. Specifying the decision owner, timestamp, candidate
actions, and outcome horizon helps identify which links the analysis must supply.
   The interpretation of the target matters just as much. Observed contribution, future perfor-
mance, treatment response, and the value of information are different estimands. A recommenda-
tion cannot be justified by moving between them implicitly. Where causal identification is unavail-
able, scenario analysis or partial identification can establish the conditions under which an action
would be preferred.




                                                 15
From Metrics to Decisions in NBA Analytics                                                 Critical integrative review




                      Selected measurements −→ decision-relevant states

                                         player          role /       synergy / availability / market value /
                                      contribution     capability        fit      capacity      development

   box score and plus-minus

   tracking, spacing and defense

   possession and action value

   lineup and passing networks
   schedule, injury and
   participation records

                 Decision-relevant states −→ basketball-operations decisions

                                        lineup /        rest /          draft /  contract / dynamic roster
                                         tactics       workload      development   trade     construction

   player contribution

   role and capability

   synergy and lineup fit

   availability and capacity

   market value and development


           primary or direct use                                    supporting or contextual use
     Blank cells indicate no standard direct interface in the reviewed literature, not a claim of impossibility.


Figure 3: Relationships among major NBA analytics research streams. The upper matrix records
how selected measurement streams inform decision-relevant player states; the lower matrix records
how those states enter basketball-operations decisions. Filled markers denote primary or direct
uses in representative studies, outlined markers denote supporting or contextual uses, and blank
cells indicate that the review did not identify a standard direct interface. The map is conceptual
rather than a citation network, maturity score, or paper count.




                                                         16
From Metrics to Decisions in NBA Analytics                                  Critical integrative review


5.2 Reconstructing the opportunity set

Researchers generally observe selected actions: the lineup a coach used, the prospect a team drafted,
the player rested, or the contract both sides signed. The alternatives are much less visible. Coding
every unrealized action as a negative observation obscures the difference between an option that
was rejected and one that was never available.
   Some alternatives can be reconstructed from dated rules and public information. Selection
can also be studied using observed decision variables, instruments, quasi-experiments, or explicit
structural assumptions. When the opportunity set remains uncertain, partial identification and
sensitivity bounds can show how much the conclusion depends on it (Manski, 2003). The choice of
method should reflect what is known about availability, rather than assume that every player-team
pair or hypothetical trade was possible.


5.3 Information available at the decision date

Information changes between an event and the date a researcher retrieves the data. Injury desig-
nations may be updated several times before tip-off; contract terms may become public after an
agreement; and a consensus draft board may incorporate news released after a selection. Replaying
a decision with a later file can give the model information the team did not have. Retrospective
analyses therefore need versioned snapshots that distinguish event, release, and retrieval times from
the model cutoff. Rolling-origin evaluation is appropriate for this temporal forecasting task; random
folds spanning seasons may allow later information into earlier predictions (Tashman, 2000).
   Changes in tracking definitions, reporting practices, participation policies, the CBA, and lottery
rules can also alter what the data mean. A model spanning several regimes needs to represent
those differences and assess how well its estimates transfer across them. Treating the sample as
stationary would leave this part of the claim untested.
  Table 4 summarizes the six decision-readiness gates and their diagnostic questions.


5.4 Carrying uncertainty into the choice

Uncertainty can materially alter an otherwise attractive choice. A low-probability absence may be
costly for a shallow roster; a risk of role failure may matter over a long contract; and correlated
injuries can undermine apparent depth. Draft-pick protections introduce further asymmetry. Re-
porting uncertainty at the estimation stage is insufficient if the recommendation then treats the
forecast as certain.
   The comparison of actions can use posterior distributions, calibrated probabilities, intervals, or
scenarios, depending on the uncertainty at issue. Conformal methods, scenario trees, robust opti-
mization (Bertsimas et al., 2011), and value-of-information analysis (Howard, 1966) offer different
ways to examine it. The useful test is whether the analysis identifies conditions that change the
preferred action or establishes its robustness across plausible conditions. Elaborate uncertainty
modeling contributes little when the candidate set is unrealistic, whereas simple scenarios may
reveal a consequential weakness.




                                                 17
From Metrics to Decisions in NBA Analytics                                               Critical integrative review



                  Table 4: Six decision-readiness gates and their diagnostic questions.
 Gate                  Diagnostic question                             Common failure
 Point-in-time         Were inputs and definitions available at        Later injury status, corrected data, or
 validity              the decision time?                              post-draft information leaks into
                                                                       training or replay
 Uncertainty           Does the decision rule use calibrated           A recommendation is based on a noisy
                       distributions, intervals, or scenarios?         point estimate without propagating
                                                                       decision-relevant uncertainty
 Context               Is transfer to the intended team, role,         Observed contribution is treated as
 portability           lineup, opponent, or regime tested?             intrinsic and invariant ability
 Action feasibility    Are actions legal and operationally             An optimizer uses only a payroll cap or
                       possible at that date?                          ignores the full rotation and contract
                                                                       rights
 Opportunity-set       Are available alternatives observed,            Untried lineups, undrafted players, and
 observability         reconstructed, or bounded?                      non-trades are treated as ordinary
                                                                       negatives
 Evaluation            Is the selected action evaluated against        Predictive accuracy or a realized
                       credible alternatives under conditions          retrospective outcome is treated as
                       appropriate to the decision claim?              evidence that the recommended action
                                                                       improved the decision
Accountability note. Public reproducibility and organizational auditability are separate reporting requirements rather
than a seventh decision-readiness gate: they determine whether the evidence and handoffs can be inspected, not
whether an action improved a decision.


5.5 Research with public and restricted data

Much of the information used inside teams is private: raw tracking, medical surveillance, workload
sensors, scouting, practice records, team boards, contract clauses, negotiations, and rejected offers.
Public research can still test benchmarks and biases, compare reduced public-data models, and
release definitions and code. For a decision that depends on inaccessible information, researchers
can reconstruct the legal and publicly visible options, specify plausible ranges for missing health or
market states, and report how the preferred action changes across those ranges. The claim should
be limited to the region supported by the analysis.
   For internal research, provenance, versioning, and independent audit provide ways to scrutinize
findings that cannot be publicly replicated. Public reproducibility and internal auditability answer
different questions about access and accountability. Neither, on its own, establishes that the model
supports the proposed decision.
   Figure 4 summarizes the maturity of these interfaces in the retained literature. Measurement
interfaces are developed in several streams. Predictive modeling is present across all seven streams,
but prediction is rated Developed only for on-court action and Emerging elsewhere, reflecting
limited accumulation or validation for the specified targets. Causal and model-based counterfactual
work is developing unevenly and retains substantial identification limits. Constrained prescription
has a smaller evidence base, and no retained study prospectively evaluates an implemented NBA
organizational decision rule against a credible alternative. These findings concern the reviewed
evidence; they cannot establish the extent of private team practice or of research outside the
corpus.



                                                         18
From Metrics to Decisions in NBA Analytics                                           Critical integrative review


                                                             Causal /    Constrained         Prospective
                           Measurement      Prediction
                                                          counterfactual prescription        evaluation

        On-court action      developed       developed        emerging         emerging           thin

           Player value      developed       emerging         emerging           thin             thin

       Role / capability     developed       emerging           thin             thin             thin

       Synergy / lineup      developed       emerging         emerging         emerging           thin

            Availability     emerging        emerging         emerging           thin             thin

   Draft / development       emerging        emerging         emerging           thin             thin

      Contract / roster      emerging        emerging         emerging         emerging           thin


                            Interpretation: maturity of specified interfaces in the retained public liter-
                             ature. Model-based counterfactuals need not identify causal effects. The re-
                            curring gap is the move to dated, feasible and prospectively evaluated action.


Figure 4: Qualitative evidence-gap map. Labels characterize each specified interface within the re-
tained public literature, not the domain as a whole, study quality, or publication volume. Developed
denotes an established research line with validation appropriate to its claim level; emerging denotes
substantive direct work with limited accumulation or validation; thin denotes mainly isolated, indi-
rect, or conceptual evidence. The causal/counterfactual column includes model-based comparisons
whose identification assumptions remain unverified. Coding rules and cell-level targets, evidence,
and boundaries appear in Supplementary Section S3 and Table S3; report-level mappings appear
in Table S4.


6 Research Opportunities Under Changing NBA Rules
Applying the framework to recent CBA and Draft Lottery changes shows how it generates research
questions from a changing decision environment. Both affect the rule state Rt , the feasible set
A, and the incentives represented in Equation 1. They also change how historical data should be
interpreted. For effects that have yet to occur, researchers have an opportunity to preserve data
and specify hypotheses before observing outcomes.


6.1 The 2023 CBA and the value of transaction options

The CBA took effect on 1 July 2023 and runs through the 2029–30 season, with either side able
to opt out after 2028–29 (NBA, 2024; NBA and NBPA, 2023). Its apron rules restrict transaction
tools in specified team states, including salary aggregation, exceptions, and the use of future draft
assets. The Frozen Pick rule illustrates the longer-term consequences. Beginning in 2024–25,
Second-Apron status at the start of a team’s final regular-season game can freeze its first-round
pick in the seventh Draft after the end of that Salary Cap Year. Exposure at that measurement
point in at least two of the next four cap years can move the pick to the end of the first round and


                                                     19
From Metrics to Decisions in NBA Analytics                                   Critical integrative review


keep it untradeable (NBA, 2024). An acquisition can therefore change a team’s future options as
well as its payroll and playing strength. Its value depends on the restrictions the team would face.
  Four related lines of research follow from these constraints.

1. Team-specific player decision value. Replace league-wide player-surplus rankings with
   a player-by-team-by-date distribution that combines contribution, role fit, joint availability,
   contract cash flows, rights, and the shadow price of lost transaction flexibility.
2. Role-bundle substitution. Test whether combinations of lower-cost capabilities can replace a
   scarce, expensive function under apron constraints. The target is not similarity between player
   archetypes but the ability of a feasible bundle to reproduce lineup functions over a full rotation.
3. Availability-adjusted roster fragility. Compare star concentration and depth strategies
   using correlated participation and workload-capacity scenarios, replacement quality, legal mid-
   season tools, and downside-risk measures. Mean projected wins are insufficient when the dis-
   tribution is asymmetric.
4. The causal value of transaction rights. Reconstruct exact team-date apron and contract
   states and estimate how losing particular transaction tools changes signings, trades, roster
   continuity, depth, and performance. Payroll above a threshold is an exposure, not the causal
   mechanism; the target is the restriction or option whose loss changes behavior.

   These programs overlap with the broader priorities in Table 5, since the same apron restriction
can affect player transport, substitution, roster risk, acquisition options, and rights valuation.
A versioned representation of the CBA would make those connections easier to study. Causal
evaluation remains difficult, however. Teams may adjust contracts before a restriction binds, and
exposure varies with team quality, ownership spending, and competitive timeline. Difference-in-
differences designs need treatment-timing diagnostics; matched team-date comparisons and event
studies need to address anticipation. Structural or simulation models offer another route, provided
they make the assumptions used to value flexibility explicit.


6.2 Prospective research on the 3-2-1 Lottery

On 28 May 2026, the NBA approved a 3-2-1 Draft Lottery for the 2027, 2028, and 2029 drafts
(NBA, 2026), with the stated aim of reducing incentives to prioritize draft position over winning.
The lottery expands to 16 teams. Non-playoff and non-Play-In teams generally receive three balls,
except the bottom three teams, which receive two. The No. 9 and No. 10 Play-In seeds in each
conference receive two, and the losers of the No. 7-versus-No. 8 Play-In games receive one. The
drawing orders all first 16 picks. The bottom three teams cannot fall below pick 12, while the other
lottery teams can fall as far as pick 16. Additional provisions limit repeated high own-pick outcomes,
restrict certain new pick protections, and expand disciplinary authority. These are changes to the
rules. Their effects on the value of moving up or down the standings remain questions for empirical
research.
   No regular season or draft had been conducted under the new system by the evidence cutoff of
1 September 2026. Game-level analyses can therefore be planned before the first affected season.
Historical work documents responses to draft incentives and the difficulty of attributing behavior to


                                                 20
From Metrics to Decisions in NBA Analytics                                       Critical integrative review


lottery changes (Price et al., 2010; Schmidt, 2024; Taylor and Trogdon, 2002). For the new system,
a binary “tanking” measure would discard much of the relevant variation. One possible treatment is
the rule-induced change in the expected value of a team’s own or economically exposed draft asset
from an additional loss at a given date. Calculating it requires standings, schedules, ownership,
swaps, protections, and an estimate of prospect-class value, together with the full rank-conditioned
pick distribution incorporating pick floors and repeated-pick restrictions.
   Availability-adjusted lineup strength, veteran shutdowns, young-player minutes, transactions,
and late-game choices are possible outcomes, although none directly reveals intent. A credible
design would specify these measures in advance and examine placebo ranking boundaries where
the lottery rule does not change, alternative pick-value curves, simulated schedules, injuries, and
playoff incentives. The two-ball allocation for the bottom three teams and the inclusion of Play-
In teams introduce incentive kinks. Because ranks can be influenced by team behavior and local
samples are small, analyses should examine difference-in-discontinuities or simulated, synthetic,
and matched comparisons before relying on local randomization.
   The relevant exposure date is outcome-specific: asset-market responses may begin at announce-
ment, whereas game-level responses should be examined during the first affected season. Baseline
periods should also be checked for anticipation before the announcement. A drawing that orders
all 16 picks changes the distribution of pick outcomes, while protection limits and repeated-pick
restrictions affect value across years. Trades usually bundle players, picks, swaps, and protec-
tions, making the price of any one component difficult to isolate. Interval-valued hedonic models
and matched-package comparisons, supported by structural sensitivity analysis, could express that
uncertainty more faithfully than a single estimated pick price.
  Figure 5 summarizes the timing of these institutional changes and the corresponding research
opportunities.

                                             3-2-1 Lottery
       2023 CBA                                                                        three treated
                                               approved
      takes effect                                                                         drafts
                                             asset-market
       new apron                                                                    first multi-season
                                               responses
      architecture                                                                       synthesis
                                              may begin
                           2024–26                                 2026–27

        July 2023                            28 May 2026                              through 2029

                           phased
                         transaction
                                                                first affected
                       and future-pick
                                                               playing season
                        consequences
                                                               and 2027 Draft
                           become
                         observable

                          Align baseline data with outcome-specific exposure
                       dates; preregister analyses of outcomes not yet observed.


Figure 5: Institutional research timeline. The CBA already produces observable team exposure.
The 3-2-1 Lottery applies from the 2027 Draft, with the 2026–27 season the first affected playing
season. Asset-market responses may begin at the May 2026 announcement, so baseline periods
must be defined separately for each outcome.


                                                  21
From Metrics to Decisions in NBA Analytics                                                    Critical integrative review


6.3 Priorities for linked research

Table 5 brings the proposed studies together. For each, it identifies the estimand, minimum linked
data, and an evaluation design, so that the proposal can be assessed against the information it
would actually require.

          Table 5: Priority research programs generated by the decision-centered synthesis.
 Program              Decision estimand                  Minimum linked data                Credible design or
                                                                                            evaluation
 Player-team          Future contribution                Point-in-time player features,     Team-switch and role-switch
 transport            distribution under a declared      role, tracking where available,    holdouts; calibration; support
                      team, role, lineup and minutes     lineups, availability, team        checks; uncertainty coverage
                      horizon                            changes
 Role-bundle          Value of a feasible capability     Capability features, role          Out-of-team validation plus
 substitution         bundle relative to the best        assignments, full rotations,       constrained roster replay;
                      accessible alternative             salaries, contracts, legal         ablation of role and synergy
                                                         acquisition state                  interfaces
 Roster fragility     Tail loss from correlated          Participation, minutes capacity,   Model: joint scenarios and a
                      unavailability under a roster      performance, depth, contracts,     declared downside objective.
                      and replacement policy             CBA replacement tools              Checks: calibration, coverage,
                                                                                            stress sensitivity, and replay
                                                                                            under stated assumptions
 Legal and market     Expected value of the best legal   Versioned CBA state,               Rule-engine tests; candidate-set
 action generation    and plausibly available            contracts, rights, assets, team    audit; bounds on market
                      personnel action (signing,         needs, transactions and            availability; prospectively
                      trade, waiver, or contract         reported offers                    logged shadow-mode
                      extension)                                                            comparisons
 CBA restriction      Effect and shadow value of         Team-date apron state,             Event study or matched panel
 effects              losing a specified transaction     contract structure, hard-cap       with anticipation checks;
                      right                              triggers, transactions, roster     structural sensitivity for option
                                                         and performance outcomes           value
 Continuous           Behavioral response per            Pregame standings, schedule,       Pre-registered continuous
 lottery incentives   marginal expected team asset       roster health, lineup strength,    treatment; alternative pick
                      value of a loss                    asset exposure, and                curves; placebo dates and
                                                         rule-encoded pick distributions    ranking boundaries without
                                                         including floors                   rule changes
 Pick portfolio       Joint option value of picks,       Complete asset graph, dated        Interval-valued hedonic or
 valuation            swaps, protections and             trade packages, rule state,        structural model; interference
                      repeated-pick restrictions         prospect-class priors and later    and equilibrium sensitivity
                                                         outcomes


   In shadow-mode comparisons, candidate sets and recommendations are frozen and logged before
outcomes, without requiring the recommended action to be executed. This permits prospective
checks of forecasts and action-set records; it does not identify effects of unchosen actions or demon-
strate gains from deployment. Several of these studies would supply inputs for others. Estimates
that transport across teams could support role-bundle and roster comparisons. Joint availability
scenarios could inform contract risk, while a dated legal action generator could help identify expo-
sure to CBA restrictions. An asset graph and rule encoder would serve both lottery-incentive and
pick-valuation research. Shared definitions and compatible timestamps would make these connec-
tions more useful than a collection of independent model rankings.


7 Using the Framework in Team Decisions
In a team setting, an estimate usually passes through several people before it affects a decision.
An analyst’s contribution forecast needs to specify the role and minutes assumed. A coach us-

                                                             22
From Metrics to Decisions in NBA Analytics                                             Critical integrative review


ing an availability forecast needs alternatives for workload and replacement minutes. Basketball-
operations staff need to assess a proposed roster move against legality, price, market access, risk,
and lost flexibility. Table 6 describes the information needed at these handoffs.

                Table 6: Practitioner interfaces for decision-ready NBA analytics.
 Primary       Decision question        Minimum analytical output              Required handoff
 user
 Coach and     Who should play, in      Conditional action or lineup           Assumptions that can be
 performance   which role and           values; availability and               translated into a rotation, tactical
 staff         lineup, at what          minutes-capacity scenarios;            instruction, or rest plan and
               workload, against        uncertainty and opponent response      observed after implementation
               this opponent?
 General       Which feasible           Player–team value distribution;        A dated decision memo that
 manager and   acquisition,             contract and rights state; legal and   separates model value, market
 basketball    retention,               plausible alternatives; multi-period   price, legal feasibility, and
 operations    development, or          risk and flexibility                   unobserved counterpart willingness
               asset action best
               advances the team’s
               timeline?
 Analyst and   Is the output valid      Versioned inputs; target and           Reproducible model card, scenario
 data          for the decision date,   estimand; calibration; transport       output, data lineage, and a record
 engineer      population, and          and support diagnostics; action-set    of what information was actually
               context?                 audit                                  delivered




7.1 A proposed deployment workflow

The framework can be used without building an end-to-end optimizer. The following proposed
deployment workflow records the information needed to make and subsequently examine a decision.

1. Freeze the decision. Record the owner, timestamp, objective, horizon, and information that
   was available.
2. Estimate coupled states. Produce distributions for the components that could change the
   choice—contribution, role, synergy, availability, cost, or development—and expose their depen-
   dencies.
3. Construct candidate actions. Apply roster, contract, CBA, timing, and basketball con-
   straints; label market availability as observed, assumed, or bounded.
4. Stress-test the ranking. Vary the assumptions that matter to the user, including minutes,
   role, opponent, availability, price, and competitive timeline.
5. Issue a decision record. Report the recommended action, credible alternatives, uncertainty,
   assumptions, veto conditions, and information that would change the recommendation.
6. Evaluate after the decision. Preserve the selected action and contemporaneous forecast,
   then evaluate calibration, process, and outcomes without redefining the target after results are
   known.




                                                       23
From Metrics to Decisions in NBA Analytics                                  Critical integrative review


   Keeping this record would make it easier to investigate a poor outcome: the cause might lie in
the forecast, an unavailable alternative, a failed transport assumption, or an incorrectly encoded
rule. The outcome might also have been plausible under a well-calibrated forecast.


7.2 A reporting contract for decision claims

A reporting contract makes the assumptions behind a decision claim available to its readers and
users. Its detail should be proportionate to the claim: a descriptive spatial study needs a clear
sample and interpretation, while a recommendation needs evidence about the alternatives and their
consequences. For work that supports or implies a decision, we propose the following minimum
information.

 1. Decision owner and action. Identify who acts and what choice is compared: deploy, rest,
    develop, draft, sign, trade, retain, or allocate an asset.
 2. Decision timestamp and information set. Freeze the latest permissible input, report event
    and release times, and audit later corrections or labels.
 3. Target and estimand. Distinguish observed contribution, future prediction, causal effect,
    treatment response, market price, and team-specific decision value.
 4. Unit and horizon. Align the observation unit with the action and outcome horizon. Explain
    how possession, game, stint, player-season, contract, and team-date units are connected.
 5. Uncertainty and calibration. Report the distributional information that could change a
    choice, including interval coverage, calibration, scenarios, and correlated risks where relevant.
 6. Context and transport. Declare team, role, lineup, opponent, coaching, data-vendor, and
    policy regimes; validate transport to the claimed context.
 7. Feasible action set. Reconstruct legal actions at the date and distinguish them from actions
    assumed to be commercially available.
 8. Opportunity and selection. Explain how realized lineups, rests, picks, contracts, and trades
    were selected; use identification, support checks, or sensitivity bounds.
 9. Evaluation. Match retrospective fit, temporal prediction, causal identification, policy simula-
    tion, constrained replay, or prospective trial to the claim being made.
10. Provenance and auditability. Report source, access, version, transformations, code, and
    model cutoff. When data are private, state the public replication boundary and the internal
    audit mechanism.

   Targeted replication can resolve disagreements about definitions, leakage, or transport, and can
give researchers a common benchmark. Reproducing every model is not necessary for the conceptual
synthesis presented here. The case for a particular reproduction is strongest when it could change
the interpretation of an important finding or settle a consequential uncertainty about its use.




                                                 24
From Metrics to Decisions in NBA Analytics                                    Critical integrative review



8 Limitations
The review draws together work from disciplines with different terminology and publication prac-
tices. Its iterative selection process helps connect those literatures but cannot establish that every
relevant method paper has been found. Counts describe the retained corpus, and the qualitative
map in Figure 4 should be read within that scope.
   Publications also provide only a partial view of organizational practice. Teams have access
to tracking, health, scouting, practice, negotiation, and internal objective-function information
that researchers may never see. Limited public evidence for an integrated decision system does
not establish that no team uses one. The review’s conclusions concern published and publicly
inspectable work.
   Applying the six decision-readiness gates involves judgment about the claim a study actually
makes. A sound descriptive study may have no reason to construct trades or estimate an interven-
tion effect. The gates are intended to identify the evidence needed for a particular use, rather than
produce a ranking of studies.
   We assess the framework as a claim-matching and diagnostic structure by asking whether its
gates follow from a decision made at a specified time, identify distinct failure modes, and yield
coherent diagnoses across research streams. It has not been validated as a numerical scale or shown
to improve team outcomes. Reliability as a scored instrument and prospective effects on decision
quality require separate empirical investigation.
   No game-level or draft outcomes under the new lottery were available at the cutoff. Asset-market
analyses, however, require outcome-specific exposure dates and checks for anticipation around the
announcement. CBA effects also remain difficult to isolate because restrictions phase in, teams
anticipate exposure, and other changes affect payroll, participation, and competition at the same
time. The suggested designs would need to address these sources of confounding.
   Generalization beyond the NBA requires further work. Its small number of teams, concentrated
talent, negotiated rules, and visible transactions make it a distinctive labor market. The framework
may be useful in other leagues or workplaces, but its empirical conclusions cannot be assumed to
transfer with it.


9 Conclusion
The reviewed literature provides substantial knowledge about player performance and several other
components of basketball-operations decisions. The harder step is using that knowledge when the
team, role, available alternatives, or rules differ from the setting in which an estimate was obtained.
A forecast becomes more useful when those conditions are explicit and its uncertainty is carried
into the comparison of actions.
   The priority research agenda identified by this review is to test the links among these components.
Contribution forecasts need evidence of role and team transport; lineup comparisons need workable
rotations and availability assumptions; and acquisition models need realistic costs, rights, and
alternatives. The six decision-readiness gates provide a way to specify what is missing in each case.




                                                  25
From Metrics to Decisions in NBA Analytics                                   Critical integrative review


   The 2023 CBA and the 3-2-1 Draft Lottery give this work practical urgency. They alter trans-
action options and draft incentives, creating settings in which researchers can preserve information
before decisions and evaluate outcomes afterward. Progress will depend on whether the proposed
links improve an actual comparison of feasible choices, as well as on the accuracy of the underlying
estimates.
   For studies that make a decision claim, the useful questions are specific: how could this estimate
alter the comparison among feasible choices, what alternatives were available, and how would
that comparison be evaluated? The framework is intended to help researchers answer them. Its
usefulness in other constrained roster markets, and its effect on decisions within teams, remain
open to empirical testing.


Data and materials availability
This review synthesizes published research and publicly available official rule documents. The Sup-
plementary Evidence Appendix accompanying this preprint documents the search and synthesis.
The machine-readable retained-evidence map (nba-decision-readiness-evidence-map.csv) is
openly available as a CSV on GitHub. No player-level private health, tracking, scouting, or nego-
tiation data were used, and ethical approval was not required.


Funding and competing interests
The authors received no financial support for the research, authorship, or publication of this article
and declare no competing interests.




                                                 26
Supplementary Evidence Appendix                                        From Metrics to Decisions in NBA Analytics



                        Supplementary Evidence Appendix
                          From Metrics to Decisions in NBA Analytics:
                    A Critical Integrative Review and Decision-Readiness Framework
                                             Yang Zhou and Tianyu Guan
                                           Evidence cutoff: 1 September 2026



S1. Purpose and review design
This appendix records how evidence was selected and synthesized for the accompanying critical integrative review. It
documents the links between NBA research streams, the limits of the claims drawn from them, and the judgments
behind the qualitative evidence-gap map. The search was iterative rather than exhaustive. Counts describe the
review’s records; they are not estimates of research prevalence or study quality.
   The evidence-discovery cutoff was 1 September 2026. Records were assembled from prior reviews, backward and
forward citation tracing, targeted topic searches, publisher and DOI verification, and official NBA and NBA Players
Association sources for rule states. Search functions and export capabilities differed across platforms, so searches were
adapted to each source rather than represented as equivalent database runs. Bibliographic verification and targeted
source and coding checks were completed through 17 September 2026. These did not expand the retained corpus or
change the evidence cutoff of 1 September 2026.


S1.1 Discovery sources
Sources searched or used for verification included scholarly web search; publisher and DOI pages; PubMed/MEDLINE
and PubMed Central; arXiv, PMLR, SSRN, and MIT Sloan Sports Analytics Conference proceedings; NBER/IZA
and institutional or author repositories; public code repositories linked to reports; and official NBA and NBA Players
Association pages.
  Where a platform supported structured fielded Boolean search, NBA or basketball terms were AND-combined with
parenthesized OR synonyms in title, abstract, or keyword fields. Scholarly-web, venue, and repository searches used
the same query families as broader keyword strings, followed by backward and forward citation chaining and title,
DOI, and report-version verification. Field syntax was adapted to each platform rather than treated as identical
across sources.
  Representative query families were:
• NBA (adjusted plus-minus OR RAPM OR player value) offense defense
• NBA (player role OR archetype OR profile) clustering longitudinal tracking
• NBA (shot selection OR shot quality OR shot making OR expected possession value)
• NBA lineup synergy interaction unseen lineup prediction network complementarity
• NBA substitution rotation minutes optimization fatigue lineup
• NBA injury availability workload prediction rest load management travel
• NBA draft prospect college combine scouting prediction mock consensus
• NBA draft position minutes retention survival sunk cost lottery tanking
• NBA salary contract compensation free agent valuation wage
• NBA trade acquisition roster team building optimization risk set candidate set
• site:nbpa.com/cba
• site:nba.com CBA 101 Second Apron
• NBA 3-2-1 Draft Lottery 2026 official


                                                      27
Supplementary Evidence Appendix                                         From Metrics to Decisions in NBA Analytics



  Title, author, DOI, cited-by, and version-of-record searches reconciled preprints, working papers, conference papers,
and journal versions. When a publisher page was restricted, a lawful author manuscript or preprint was used when
available.


S1.2 Eligibility and evidence roles
Primary empirical studies, methodological studies demonstrated on NBA data, and full conference papers were eligible
when they did at least one of the following:

1. estimated a decision-relevant state;
2. evaluated uncertainty or transport;
3. modeled an intervention, candidate action, or constrained choice; or
4. exposed a material data, selection, market, or institutional boundary for basketball operations.

  Reviews were retained for prior-coverage comparison and terminology. Official NBA and NBA–NBPA documents
were retained only to define rule and policy states, not as outcome evidence. Broader basketball or multisport work
was retained only when its method or evidence directly informed an NBA decision interface.
   Records were excluded when they were duplicates or superseded versions, had no NBA empirical or direct decision-
interface contribution, repeated a sample without adding a distinct estimand, addressed betting/fan/media topics
outside the stated scope, focused on a clinical treatment without an availability or operations interface, or remained
an abstract-only lead not required to delimit the manuscript’s scope. Retained abstract-only records are marked and
do not carry decisive field-level findings.


S1.3 Record accounting and deduplication
The five discovery workstreams organized the search and extraction process. Their reports were subsequently grouped
into seven research streams for the synthesis.


                             Table S1: Discovery records by source evidence workstream.
                                  Source evidence workstream                        Rows
                                  Player value, role, and on-court action              21
                                  Synergy and lineup decisions                         27
                                  Availability, injury, and workload                   30
                                  Draft, development, and lottery                      25
                                  Contracts, acquisition, and roster construction      29
                                  Total discovery rows                                132

   Deduplication used, in order, a normalized DOI; a normalized title when no DOI was available; and manual
inspection of authors, year, and report/version identity. Working-paper and journal manifestations of the same study
were treated as one report. Five duplicate report pairs were reconciled across workstreams, leaving 127 unique
workstream reports.
   The right-hand categories are mutually exclusive coding categories for manuscript accounting, not a universal
publication taxonomy. When a source could carry multiple labels, it is counted under the category that describes how
it enters this review.
   Of the 127 unique workstream reports, 51 were retained and the remaining 76 remain discovery or background
records. Seven additional foundations bring the cited NBA synthesis corpus to 58 reports: the six prior reviews
retained for scope comparison (Sarlis and Tjortjis, 2020; Terner and Franks, 2021; Huyghe et al., 2022; Kovalchik,
2023; Zhou and Li, 2024; Chen et al., 2025) and Kubatko et al. (2007) as the NBA statistical foundation. Eight non-
NBA methodological sources ground the decision-readiness framework and are excluded from NBA evidence counts
and Figure 4 maturity judgments.


                                                         28
Supplementary Evidence Appendix                                           From Metrics to Decisions in NBA Analytics




                                        Table S2: Retained evidence accounting.
                NBA synthesis status Reports                  Manuscript evidence category Reports
                Full text inspected                 50        Primary empirical study                     21
                Abstract/metadata only               5        Methodological study                        24
                Official rule document               3        Full conference paper                        2
                                                              Preprint                                     2
                                                              Review                                       6
                                                              Official rule                                3
                NBA synthesis corpus                58        NBA synthesis corpus                        58
                Framework foundations                8        Combined citation map                       66


S2. Extraction and synthesis
The workstream tables record each report’s bibliographic identity, publication and access status, seasons, data sources,
observation unit, estimand, method, and validation. They also distinguish findings supported by the source from
inferences made in this review, and record uncertainty, limitations, decision tasks, action and opportunity boundaries,
provenance, and public replication feasibility.
   The harmonized evidence map records the furthest claim level directly used by the manuscript: measurement, pre-
diction, causal or counterfactual estimation, constrained prescription, or prospective evaluation. It separately records
point-in-time validity, uncertainty, context portability, action feasibility, opportunity-set observability, evaluation, and
reproducibility or auditability. Fields use yes, partial, no, not applicable, or not reported; they are not summed into
a score. In the GitHub-hosted CSV, the source_table field identifies an internal discovery workstream rather than
a separate evidence source. Its evidence_id and citation_key fields link retained records to Section S4 and the
reference list; the remaining fields record evidence role, access, claim level, diagnostic assessments, manuscript use,
and interpretive notes.
  The combined reproducibility_auditability field is interpreted alongside access status and the evidence notes.
For AV01, AV02, AV06, and AV10, no denotes restricted public reproducibility, not the absence of internal auditability.
AV02 describes an internally audited record system.
   We recorded the furthest analytical claim implemented and used in this review, and assessed its validation and
decision readiness separately. We then considered the readiness gates relevant to its claim and the evidence still
needed for the proposed use. Descriptive work was assessed on its own terms. Abstract-only records established the
presence of a topic or method, but were not used to support numerical effects or mature interfaces. Official documents
established rules and dates, without establishing policy effectiveness.
   Both authors worked jointly on screening, extraction, and coding. During manuscript preparation, both authors
independently cross-checked the source claims and the extracted information for all 66 records included in Table S4, as
well as all Figure 4 cell ratings. Discrepancies were resolved through joint review, and the final coding was confirmed
by both authors. Evidence extraction was domain-specific and then harmonized for this review. No formal estimate
of inter-rater agreement is reported. No paper reproduction or PRISMA flow is claimed.


S3. Figure 4 maturity definitions and audit trail
The unit of classification is a specified research interface at one claim level. Table S3 states the target of each cell
and the evidence or boundary supporting its rating. Measurement concerns the stated representation or construct;
prediction concerns outcomes in a declared future or held-out sample; causal/counterfactual estimation concerns
intervention effects or model-based alternative outcomes; constrained prescription concerns comparison of candidate
actions under an objective and explicit constraints; prospective evaluation concerns an implemented decision rule and
a credible comparator. Model-based counterfactuals are not treated as identified causal effects.
   Coding first distinguishes direct implementations from adjacent evidence, then considers the accumulation of dis-
tinct full-text contributions and validation appropriate to the target. Report versions of one study do not provide


                                                         29
Supplementary Evidence Appendix                                           From Metrics to Decisions in NBA Analytics



independent support; distinct contributions can share NBA data and do not automatically constitute external repli-
cation. Measurement is assessed through construct, measurement, or robustness evidence; prediction through relevant
held-out or temporal evaluation; causal/counterfactual work through its identification or structural assumptions and
sensitivity; action models through candidate comparisons and constraint coverage; and deployment through the im-
plemented comparison. Requirements from later claim levels are not imposed on earlier ones.

• Developed: Multiple distinct full-text contributions form an identifiable research line, with established implemen-
  tations and repeated empirical support appropriate to the specified target and claim level. Remaining limitations
  do not reduce the evidence to isolated demonstrations. Developed does not mean free of bias or decision-ready.
• Emerging: Substantive direct implementation extends beyond an isolated illustrative proof of concept, but accu-
  mulation or claim-appropriate validation remains too limited for Developed. Identification, transport, calibration,
  or constraint coverage may remain unresolved; their relevance depends on the target.
• Thin: Direct evidence is absent or confined to isolated illustrations; other anchors are adjacent, diagnostic, or
  conceptual. Later-stage gaps alone do not imply Thin at an earlier claim level.

   The rules are applied in that order: an interface that does not meet Developed is assessed for substantive direct
work before being assigned Emerging or Thin. Boundary rationales identify the limiting evidence rather than require
a universal end-to-end system. No numerical score or fixed publication-count threshold is used. Public literature
includes inspectable reports based on restricted data; lack of access to raw data is recorded separately and is not by
itself a reason to lower maturity. Abstract-only reports establish topic presence, and official rules establish legal states,
but neither establishes a mature empirical interface. Evidence IDs resolve to Section S4. An anchor may document
a limitation rather than supply positive evidence at the cell’s claim level; such use does not upgrade the report’s own
claim.


Targeted source checks.        The following checks clarify important boundaries in Tables S3 and S4:
• PV02, Sill (2010), pp. 3–6: the March–April 2009 holdout uses coefficients fitted earlier, but predictions condition
  on realized lineups and possessions. PV03, Deshpande and Jensen (2016), Sections 1 and 7: player impact is
  explicitly retrospective, not a forecast. PV03 therefore supports measurement; the retained direct prediction
  evidence is insufficient for Developed.
• RO01, Skinner and Guy (2015), Section 5 and Methods: the demonstration uses 780 hand-coded sequences from
  three playoff games, with limited cross-lineup checks. A tracking-oriented method is not itself evidence of large-scale
  tracking validation.
• SY03, Kuehn (2017): the retained extraction record and publisher description support model-based candidate
  trades. The opportunity_set code is partial, because the retained record does not establish actual market
  availability.
• AV01/AV02 support injury and participation ascertainment. The Availability measurement rating also covers
  workload representation (AV06); its limited validation as an indicator of capacity should not be read as a judgment
  that injury surveillance is immature.
• AV10, Herzog et al. (2026), Sections 2.3 and 3.1: no statistically significant regular-season injury-risk differences
  were found across rest/load-management groups for in-game injuries causing at least two consecutive missed games.
  This observational result does not establish an individual causal effect.
• DR01, Berri et al. (2011), Sections 3–4 and Tables 3 and 5–6: retrospective regressions relate pre-draft character-
  istics to selection and later production; no held-out predictive evaluation is reported. DR03, Fisher and Montague
  (2025), evaluates dated selection-order forecasts. This supports Emerging for draft-order/consensus prediction,
  without establishing prediction of player productivity or development effects.
• CR05, Brill et al. (2023), Sections 2–3: a modeled lineup outcome is used to rank acquisition candidates under a
  salary filter, without reported held-out forecast or recommendation validation. CR02/CR04 supply compensation
  and accounting context. Emerging denotes direct modeling with limited validation.




                                                        30
Supplementary Evidence Appendix                                          From Metrics to Decisions in NBA Analytics



                          Table S3: Audit trail for the seven-by-five qualitative maturity map in
                          Figure 4. Each rationale specifies the target, supporting evidence, and
                          relevant boundary. Evidence IDs are representative anchors rather than
                          citation counts.

          Stream           Claim level     Rating       Evidence IDs       Target, evidence, and boundary
          On-court action Measurement      Developed    OA01, OA03,        Observed possession, spatial behavior,
                                                        OA04, OA07         and action value: accounting,
                                                                           defensive attribution, and
                                                                           action-value representations form
                                                                           established measurement lines.
          On-court action Prediction       Developed    OA05, OA06         Downstream possession value:
                                                                           possession and transition models
                                                                           provide empirical prediction and
                                                                           validation with explicit state
                                                                           dynamics.
          On-court action Causal /         Emerging     OA02, OA06,        Alternative micro-action outcomes:
                          counterfac-                   OA07               explicit modeled comparisons extend
                          tual                                             beyond conceptual proposals, but
                                                                           unchosen-action support and strategic
                                                                           response limit causal interpretation.
          On-court action Constrained      Emerging     OA02, OA06,        Pass and shot choice: models
                          prescription                  OA07               enumerate and compare actions;
                                                                           capability, teachability, and opponent
                                                                           adaptation remain incompletely
                                                                           represented.
          On-court action Prospective      Thin         OA05, OA06,        Implemented coaching rules: the
                          evaluation                    OA07               retained anchors evaluate models, not
                                                                           a prospectively deployed coaching
                                                                           decision against a credible
                                                                           comparator.
          Player value     Measurement     Developed    PV01, PV03,        Observed-context contribution:
                                                        PV04, PV05,        multiple impact estimators and metric
                                                        PV06               audits examine attribution, stability,
                                                                           and ranking uncertainty. This target
                                                                           does not require team-switch
                                                                           validation.
          Player value     Prediction      Emerging     PV02, PV03         Held-out game margins: PV02
                                                                           validates conditional predictions using
                                                                           realized lineups and possessions;
                                                                           PV03 is retrospective measurement.
                                                                           Direct predictive accumulation in the
                                                                           retained corpus is insufficient for
                                                                           Developed.
          Player value     Causal /        Emerging     PV05, PV06         Teammate effects on impact metrics:
                           counterfac-                                     PV06 implements FE/IV analyses;
                           tual                                            PV05 supplies a diagnostic audit, not
                                                                           causal evidence. Identification
                                                                           assumptions and portable player
                                                                           effects remain unresolved.
          Player value     Constrained     Thin         PV01, PV03,        Deployment or acquisition choice: the
                           prescription                 PV06               anchors estimate or audit player
                                                                           contribution without comparing
                                                                           implementable actions under an
                                                                           objective and constraints.
                                                                                            Continued on next page




                                                       31
Supplementary Evidence Appendix                                         From Metrics to Decisions in NBA Analytics



          Table S3 continued from previous page
          Stream            Claim level      Rating      Evidence IDs     Target, evidence, and boundary
          Player value      Prospective      Thin        PV02, PV03       Implemented player-value rules: PV02
                            evaluation                                    supplies conditional predictive testing
                                                                          and PV03 retrospective measurement;
                                                                          neither prospectively evaluates their
                                                                          use in team decisions.
          Role /            Measurement      Developed   RO01, RO02       Role representation: skill features and
          capability                                                      multi-season archetypes provide
                                                                          empirically studied representations
                                                                          and stability checks beyond nominal
                                                                          positions.
          Role /            Prediction       Emerging    RO01, RO02       Performance from role features: RO01
          capability                                                      tests limited cross-lineup skill transfer
                                                                          using hand-coded games; RO02
                                                                          supplies representation stability.
                                                                          Validation after team or role changes
                                                                          is sparse.
          Role /            Causal /         Thin        RO01, RO02       Role-reassignment outcomes: neither
          capability        counterfac-                                   representation anchor directly
                            tual                                          estimates an intervention or models
                                                                          outcomes under alternative
                                                                          assignments.
          Role /            Constrained      Thin        RO01, RO02       Role or minutes assignment:
          capability        prescription                                  representations suggest applications
                                                                          but do not compare implementable
                                                                          assignments under a declared
                                                                          objective and constraints.
          Role /            Prospective      Thin        RO01, RO02       Representation-guided reassignment:
          capability        evaluation                                    no retained study prospectively
                                                                          evaluates an implemented
                                                                          role-assignment rule.
          Synergy /         Measurement      Developed   SY01, SY02,      Observed teammate interaction: pair
          lineup                                         SY03, SY04,      effects, spillovers, higher-order
                                                         SY06             decompositions, and networks
                                                                          constitute an established
                                                                          measurement literature.
          Synergy /         Prediction       Emerging    SY05, RO01       Unseen-lineup performance: SY05
          lineup                                                          uses time-ordered prediction; RO01
                                                                          provides limited within-series
                                                                          cross-lineup checks. Validation
                                                                          remains sparse and conditioned on
                                                                          lineups coaches used.
          Synergy /         Causal /         Emerging    SY01, SY02,      Alternative teammate configurations:
          lineup            counterfac-                  SY03             structural production and possession
                            tual                                          models provide counterfactual
                                                                          comparisons. Strategic selection and
                                                                          structural assumptions prevent
                                                                          treating these as identified
                                                                          deployment effects.
          Synergy /         Constrained      Emerging    SY01, SY03,      Lineup or roster choice: simulated
          lineup            prescription                 SY05             trades and candidate screening
                                                                          compare actions, unlike
                                                                          representation alone; complete
                                                                          rotation constraints and market
                                                                          access remain unvalidated.
                                                                                           Continued on next page



                                                         32
Supplementary Evidence Appendix                                        From Metrics to Decisions in NBA Analytics



          Table S3 continued from previous page
          Stream            Claim level      Rating     Evidence IDs     Target, evidence, and boundary
          Synergy /         Prospective      Thin       SY01, SY05       Implemented lineup policies: no
          lineup            evaluation                                   retained system prospectively
                                                                         evaluates a substitution, minutes, or
                                                                         lineup rule against a credible
                                                                         alternative.
          Availability      Measurement      Emerging   AV01, AV02,      Participation and workload
                                                        AV06             representation: AV01/AV02 support
                                                                         injury and participation
                                                                         ascertainment. Emerging concerns
                                                                         limited validation of workload
                                                                         measures as capacity indicators
                                                                         (AV06), not event surveillance or
                                                                         restricted data access itself.
          Availability      Prediction       Emerging   AV04, AV05       Future injury or absence risk: direct
                                                                         risk models exist, but label validity,
                                                                         temporal validation, and calibration
                                                                         remain limited.
          Availability      Causal /         Emerging   AV08, AV09,      Rest effects on health or performance:
                            counterfac-                 AV10             empirical intervention contrasts and
                            tual                                         heterogeneity analyses exist, but
                                                                         confounding by indication and
                                                                         interference remain unresolved.
          Availability      Constrained      Thin       AV06, AV09,      Workload or rest choice: monitoring
                            prescription                AV10             and effect estimates do not directly
                                                                         compare feasible policies under an
                                                                         objective incorporating health,
                                                                         replacement performance, and
                                                                         competitive cost.
          Availability      Prospective      Thin       AV04, AV10       Implemented availability rules: risk
                            evaluation                                   prediction and retrospective rest
                                                                         analysis do not prospectively compare
                                                                         a deployed policy with a credible
                                                                         alternative.
          Draft /           Measurement      Emerging   DR02, DR03,      Prospect signals: athletic tests, public
          development                                   DR05             ranks, and allocated opportunity are
                                                                         measured, but construct validation
                                                                         separating ability, belief, and
                                                                         development opportunity remains
                                                                         limited.
          Draft /           Prediction       Emerging   DR01, DR03       Draft-order/consensus prediction:
          development                                                    DR03 evaluates dated forecasts
                                                                         against actual selections; DR01
                                                                         reports retrospective regressions
                                                                         without held-out evaluation.
                                                                         Repeated direct predictive validation
                                                                         is insufficient for Developed; future
                                                                         productivity and development effects
                                                                         remain outside this target.
          Draft /           Causal /         Emerging   DR04, DR06,      Information and lottery-incentive
          development       counterfac-                 DR07, DR08       effects: quasi-experimental and
                            tual                                         regime comparisons address
                                                                         alternatives, but concurrent changes,
                                                                         opportunity, and behavioral
                                                                         interpretation limit identification.
                                                                                          Continued on next page



                                                        33
Supplementary Evidence Appendix                                         From Metrics to Decisions in NBA Analytics



          Table S3 continued from previous page
          Stream            Claim level      Rating     Evidence IDs      Target, evidence, and boundary
          Draft /           Constrained      Thin       DR01, DR03,       Pick or prospect acquisition:
          development       prescription                DR09              prediction and rule anchors inform a
                                                                          choice but do not directly compare
                                                                          priced, team-specific candidate
                                                                          actions under constraints.
          Draft /           Prospective      Thin       DR08, DR09        Implemented draft rules: no retained
          development       evaluation                                    study evaluates a prospectively
                                                                          deployed team decision rule; the new
                                                                          lottery also had no treated season by
                                                                          the cutoff.
          Contract /        Measurement      Emerging   CR02, CR03,       Performance-to-compensation value:
          roster                                        CR04              contract outcomes, consumer value,
                                                                          and realized ROI have direct
                                                                          empirical measures, but different
                                                                          targets and limited validation of value
                                                                          conversion prevent an established
                                                                          common interface.
          Contract /        Prediction       Emerging   CR02, CR04,       Prediction-based acquisition ranking:
          roster                                        CR05              CR05 ranks candidates using modeled
                                                                          lineup outcomes, but reports no
                                                                          held-out forecast or recommendation
                                                                          validation. CR02/CR04 provide
                                                                          compensation and accounting context,
                                                                          not forecast validation.
          Contract /        Causal /         Emerging   CR02, CR03        Compensation under alternative rules:
          roster            counterfac-                                   CR03 models a pay counterfactual;
                            tual                                          CR02 supplies observed-contract
                                                                          context. Assumptions about valuation
                                                                          and selection limit interpretation.
          Contract /        Constrained      Emerging   CR05, CR06,       Acquisition or roster choice: models
          roster            prescription                CR10, CR11,       compare candidates under explicit
                                                        CR12              objectives and simplified constraints.
                                                                          Rule documents define missing legal
                                                                          requirements; full CBA and market
                                                                          coverage remain unvalidated.
          Contract /        Prospective      Thin       CR06, CR10        Implemented roster rules:
          roster            evaluation                                    retrospective cases and stylized
                                                                          simulations do not establish
                                                                          prospective NBA execution or
                                                                          decision improvement.



S4. Retained-evidence crosswalk
The table links each citation to its role in the review and the main limitation on its use in a decision. It distinguishes
the 58 NBA reports from the eight general framework sources. The furthest claim level describes the implemented
analysis used here, not its overall quality or validation status. A prediction-oriented model is distinguished from held-
out predictive validation in the evidence notes and maturity rationales. A descriptive study can be sound without
constructing a trade; a prescriptive claim needs evidence about feasibility, opportunity, uncertainty, and evaluation.




                                                        34
Supplementary Evidence Appendix                                                     From Metrics to Decisions in NBA Analytics



                           Table S4: Retained-evidence crosswalk. The 58 NBA synthesis reports and eight
                           framework-foundation sources are shown separately by the Stream/type column.
                           “Furthest claim” records the highest analytical reach used in the manuscript, not
                           an overall quality rating.

           ID       Source                   Stream / type           Furthest claim      Decision interface and principal
                                                                                         boundary

           REV01    Sarlis and Tjortjis      cross-stream            not applicable      prior-review positioning. Reviews
                    (2020)                   review; review                              player and team evaluation; used for
                                                                                         scope comparison, not outcome
                                                                                         evidence.
           REV02    Terner and Franks        cross-stream            not applicable      prior-review positioning.
                    (2021)                   review; review                              Methodological review of basketball
                                                                                         player and team performance.
           REV03    Huyghe et al. (2022)     cross-stream            not applicable      prior-review positioning. NBA
                                             review; review                              gameplay-performance systematic
                                                                                         review; salaries and health/injury are
                                                                                         outside its stated scope.
           REV04    Kovalchik (2023)         cross-stream            not applicable      prior-review positioning and
                                             review; review                              data-access boundary. Cross-sport
                                                                                         tracking-data review used for method
                                                                                         and access framing.
           REV05    Chen et al. (2025)       cross-stream            not applicable      prior-review positioning. Only
                                             review; review;                             high-level abstract-supported coverage
                                             abstract/metadata                           claims are retained; not used for
                                             only                                        detailed findings.
           REV06    Zhou and Li (2024)       cross-stream            not applicable      prior-review positioning. Full text
                                             review; review                              supports the reported dimension–
                                                                                         granularity–task–stakeholder-question
                                                                                         organizing structure and its
                                                                                         32-question agenda.
           OA01     Kubatko et al. (2007)    on-court action;        measurement         observation-to-state. Foundational
                                             cross-stream                                possession accounting and basketball
                                             foundation;                                 statistics; not a modern
                                             methodological                              decision-support validation.
                                             study
           OA02     Skinner (2012)           on-court action;        constrained         state-to-action. Formalizes
                                             methodological          prescription        shot-selection tradeoffs; empirical
                                             study                                       intervention and opponent-response
                                                                                         validation remain limited.
           OA03     Miller et al. (2014)     on-court action; full   measurement         observation-to-state. Spatial
                                             conference paper                            shot-intensity model using
                                                                                         tracking-era data; measurement rather
                                                                                         than a tested coaching intervention.
           OA04     Franks et al. (2015)     on-court action;        measurement         observation-to-state. Measures
                                             methodological                              defensive spatial responsibility and
                                             study                                       skill; role and assignment transport
                                                                                         are not prospectively tested.
           OA05     Cervone et al. (2016)    on-court action;        prediction          state-to-outcome. Possession-value
                                             methodological                              prediction supports action comparison
                                             study                                       but does not identify unchosen-action
                                                                                         effects.
           OA06     Sandholtz and Bornn      on-court action;        constrained         state-to-action. Transition model
                    (2020)                   methodological          prescription        evaluates observed on-court decisions;
                                             study                                       uncommon or unchosen actions and
                                                                                         deployment remain bounded.
           OA07     Jutamulia and Hosoi      on-court action;        measurement         state-to-action. Expected action value
                    (2025)                   methodological                              enumerates immediate pass and shot
                                             study                                       alternatives and measures decision
                                                                                         skill; the comparisons are predictive
                                                                                         rather than causal or prospectively
                                                                                         evaluated.
           PV01     Fearnhead and Taylor     player value;           measurement         observation-to-state. Posterior
                    (2011)                   methodological                              offense/defense contribution in
                                             study                                       observed lineups; future team-switch
                                                                                         portability is not tested.
           PV02     Sill (2010)              player value; full      prediction          state-to-outcome. Conditional
                                             conference paper                            held-out game-margin prediction;
                                                                                         coefficients fitted before the
                                                                                         March-April 2009 test games, but
                                                                                         realized lineups and possession counts
                                                                                         enter predictions (pp. 3-6). No
                                                                                         prospective decision evaluation.

                                                                                                      Continued on next page




                                                              35
Supplementary Evidence Appendix                                                     From Metrics to Decisions in NBA Analytics



           Table S4 continued from previous page
           ID       Source                     Stream / type         Furthest claim      Decision interface and principal
                                                                                         boundary

           PV03     Deshpande and Jensen       player value;         measurement         observation-to-state. Retrospective,
                    (2016)                     methodological                            context-dependent contribution to
                                               study                                     winning, explicitly not future player
                                                                                         performance (Sections 1 and 7).
                                                                                         Internal win-probability estimation
                                                                                         does not validate a player-contribution
                                                                                         forecast.
           PV04     Barrientos et al. (2023)   player value;         measurement         state-to-ranking. Makes uncertainty in
                                               methodological                            rankings explicit; not a team-specific
                                               study                                     choice evaluation.
           PV05     Franks et al. (2016)       player value;         measurement         metric-to-state audit. Assesses
                                               methodological                            discrimination, stability, and
                                               study                                     independence of sports metrics;
                                                                                         supplies diagnostic context rather
                                                                                         than direct causal evidence.
           PV06     Ghimire et al. (2020)      player value;         causal or           teammate context-to-impact metric.
                                               primary empirical     counterfactual      FE/IV specifications examine
                                               study                 estimation          teammate effects on RPM; instrument
                                                                                         validity and selection remain
                                                                                         assumptions, and a portable player
                                                                                         effect is not identified.
           RO01     Skinner and Guy            role / capability;    prediction          observation-to-state.
                    (2015)                     methodological                            Tracking-oriented skill model
                                               study                                     demonstrated on 780 hand-coded
                                                                                         sequences from three 2011 playoff
                                                                                         games; limited cross-lineup checks, not
                                                                                         broad team-switch validation (Section
                                                                                         5 and Methods).
           RO02     Muniz and Flamand          role / capability;    measurement         observation-to-state. Recovers stable
                    (2022)                     methodological                            player archetypes across seasons;
                                               study                                     clusters do not identify causal role
                                                                                         assignments.
           SY01     Maymin et al. (2013)       synergy / lineup;     constrained         state-to-action. Pairwise chemistry
                                               methodological        prescription        and simulated trades; lineup selection
                                               study                                     and market availability are not
                                                                                         identified.
           SY02     Arcidiacono et al.         synergy / lineup;     causal or           teammate configuration-to-production.
                    (2017)                     primary empirical     counterfactual      Structural spillover estimates and
                                               study                 estimation          alternative-team comparisons depend
                                                                                         on conditional exogeneity; substitution
                                                                                         robustness does not identify a
                                                                                         deployed lineup effect.
           SY03     Kuehn (2017)               synergy / lineup;     constrained         state-to-action. Lineup-specific
                                               methodological        prescription        marginal values and model-based
                                               study                                     trade comparisons depend on the
                                                                                         possession model; one-season fit,
                                                                                         selection, and unclear provenance
                                                                                         restrict deployment claims. Candidate
                                                                                         alternatives are enumerated within the
                                                                                         model; the retained evidence record
                                                                                         does not establish actual market
                                                                                         availability.
           SY04     Devlin and Uminsky         synergy / lineup;     measurement         observation-to-state. Decomposes
                    (2020)                     methodological                            observed lineup performance; no
                                               study                                     predictive or intervention validation.
           SY05     Martonosi et al. (2023)    synergy / lineup;     prediction          state-to-outcome. Time-ordered
                                               methodological                            unseen-lineup prediction, but
                                               study                                     evaluation is conditioned on lineups
                                                                                         coaches later used.
           SY06     Fewell et al. (2012)       synergy / lineup;     measurement         observation-to-state. Strategic passing
                                               primary empirical                         networks describe team process; they
                                               study                                     do not validate a lineup or tactical
                                                                                         intervention.
           AV01     Drakos et al. (2010)       availability;         measurement         observation-to-state. Internal
                                               primary empirical                         surveillance measures diagnosed injury
                                               study                                     burden and participation loss; it does
                                                                                         not measure complete workload
                                                                                         capacity. The no code concerns
                                                                                         restricted public reproducibility; it
                                                                                         does not establish the absence of
                                                                                         internal auditability.

                                                                                                      Continued on next page




                                                                36
Supplementary Evidence Appendix                                                  From Metrics to Decisions in NBA Analytics



           Table S4 continued from previous page
           ID       Source                   Stream / type         Furthest claim     Decision interface and principal
                                                                                      boundary

           AV02     Mack et al. (2019)       availability;         measurement        data-to-state governance.
                                             methodological                           Standardizes internal injury, illness,
                                             study                                    and participation records; raw-data
                                                                                      access is a replication boundary, not
                                                                                      itself a maturity penalty. The no code
                                                                                      concerns restricted public
                                                                                      reproducibility; the source describes
                                                                                      an internally audited record system.
           AV03     Teramoto et al. (2017)   availability;         measurement        exposure-to-state. Associates schedule
                                             primary empirical                        context with in-game injury frequency;
                                             study                                    not a causal rest effect.
           AV04     Lewis (2018)             availability;         prediction         state-to-outcome. Pregame
                                             primary empirical                        public-data risk model; no temporal
                                             study                                    external validation, intervention
                                                                                      model, or calibrated decision utility.
           AV05     Cohan et al. (2021)      availability;         prediction         state-to-outcome. Random-split injury
                                             methodological                           classifier with extreme imbalance;
                                             study                                    temporal and decision validation are
                                                                                      absent.
           AV06     Russell et al. (2021)    availability;         measurement        observation-to-state. Single-team
                                             primary empirical                        workload study compares practice and
                                             study                                    game load; cross-team validation and
                                                                                      physiological-capacity measurement
                                                                                      remain limited. The no code concerns
                                                                                      restricted public reproducibility; it
                                                                                      does not establish the absence of
                                                                                      internal auditability.
           AV07     Charest et al. (2021)    availability;         measurement        exposure-to-state. Travel and
                                             primary empirical                        time-zone associations are
                                             study                                    reproducible proxies, not player-level
                                                                                      health effects.
           AV08     Belk et al. (2017)       availability;         causal or          action-to-outcome. Matched
                                             primary empirical     counterfactual     retrospective rest study; small sample
                                             study                 estimation         and selection prevent a strong causal
                                                                                      conclusion.
           AV09     Nakamura-Sakai et al.    availability;         causal or          action-to-outcome. Heterogeneous
                    (2024)                   preprint              counterfactual     rest-effect model; causal interpretation
                                                                   estimation         depends on unconfoundedness and no
                                                                                      interference, and external validation
                                                                                      remains unresolved.
           AV10     Herzog et al. (2026)     availability;         causal or          action-to-outcome. No statistically
                                             primary empirical     counterfactual     significant regular-season injury-risk
                                             study                 estimation         differences across
                                                                                      rest/load-management groups for
                                                                                      in-game injuries causing at least two
                                                                                      consecutive missed games (Sections 2.3
                                                                                      and 3.1); observational comparison,
                                                                                      not an identified individual rest effect.
                                                                                      The no code concerns restricted public
                                                                                      reproducibility; it does not establish
                                                                                      the absence of internal auditability.
           DR01     Berri et al. (2011)      draft /               prediction         state-to-outcome. Retrospective
                                             development;                             regressions relate pre-draft
                                             primary empirical                        characteristics to draft position and
                                             study                                    later NBA production; no held-out
                                                                                      predictive evaluation is reported
                                                                                      (Sections 3-4, Tables 3 and 5-6). The
                                                                                      prediction label records the modeling
                                                                                      target, not validated forecast
                                                                                      performance.
           DR02     Berger and Daumann       draft /               measurement        signal-to-market belief. Combine
                    (2021)                   development;                             athleticism predicts selection more
                                             primary empirical                        than later observed performance;
                                             study                                    missing tests and opportunity are
                                                                                      selected.
           DR03     Fisher and Montague      draft /               prediction         public belief-to-selection.
                    (2025)                   development;                             Date-indexed public mock aggregation
                                             methodological                           evaluates draft-order forecasts, not
                                             study                                    future NBA productivity or
                                                                                      development effects; the historical
                                                                                      corpus is not released (Sections 5-6).
           DR04     Ichniowski and           draft /               causal or          information-to-market belief. Uses
                    Preston (2017)           development;          counterfactual     pre-tournament mock rank as a dated
                                             primary empirical     estimation         prior; private boards and later
                                             study                                    opportunity remain unobserved.

                                                                                                    Continued on next page


                                                              37
Supplementary Evidence Appendix                                                 From Metrics to Decisions in NBA Analytics



           Table S4 continued from previous page
           ID       Source                  Stream / type        Furthest claim      Decision interface and principal
                                                                                     boundary

           DR05     Staw and Hoang          draft /              measurement         selection-to-opportunity. Shows draft
                    (1995)                  development;                             order is associated with later
                                            primary empirical                        opportunity and survival; does not
                                            study                                    cleanly identify a sunk-cost
                                                                                     mechanism.
           DR06     Taylor and Trogdon      draft /              causal or           rule-to-behavior. Three-regime
                    (2002)                  development;         counterfactual      comparison supports incentive
                                            primary empirical    estimation          response but not directly observed
                                            study                                    intent.
           DR07     Price et al. (2010)     draft /              causal or           rule-to-behavior. Long-panel extension
                                            development;         counterfactual      strengthens historical generalization
                                            primary empirical    estimation          while team intent and mechanism
                                            study                                    remain latent.
           DR08     Schmidt (2024)          draft /              causal or           rule-to-roster-use.
                                            development;         counterfactual      One-season-before/one-season-after
                                            primary empirical    estimation          portfolio analysis is informative but
                                            study                                    insufficient for a standalone causal
                                                                                     policy claim.
           DR09     NBA (2026)              draft /              not applicable      rule-state definition. Authoritative
                                            development;                             treatment definition only; zero
                                            official rule                            completed treated seasons at the
                                                                                     evidence cutoff.
           CR01     Ehrlich et al. (2019)   contract / roster;   measurement         performance-to-market price.
                                            primary empirical                        Abstract-level evidence only; used to
                                            study;                                   identify the offense-defense wage
                                            abstract/metadata                        question, not a decisive effect
                                            only                                     estimate.
           CR02     Wen et al. (2023)       contract / roster;   measurement         performance-to-contract outcome.
                                            primary empirical                        Observed contract salary, duration,
                                            study                                    and performance have specification
                                                                                     checks but no predictive holdout;
                                                                                     rejected terms and causal contract
                                                                                     effects are not observed.
           CR03     Kaplan (2024)           contract / roster;   causal or           rule-to-compensation distribution.
                                            primary empirical    counterfactual      Counterfactual pay distribution under
                                            study                estimation          min/max constraints; league-wide
                                                                                     consumer value is not team-specific
                                                                                     contract value.
           CR04     Lautier (2025)          contract / roster;   measurement         performance-and-salary-to-ROI.
                                            methodological                           Realized salary ROI is an accounting
                                            study                                    allocation with internal checks, not a
                                                                                     signing-time forecast or independently
                                                                                     validated marginal contract value.
           CR05     Brill et al. (2023)     contract / roster;   constrained         state-to-acquisition candidate.
                                            methodological       prescription        Prediction-based candidate ranking
                                            study                                    uses modeled lineup outcomes and a
                                                                                     simplified salary filter; no held-out
                                                                                     forecast or recommendation validation
                                                                                     is reported (Sections 2-3). Legal and
                                                                                     market availability remain unverified.
           CR06     Muniz and Flamand       contract / roster;   constrained         state-to-roster action. Mixed-integer
                    (2023)                  methodological       prescription        roster construction demonstrates
                                            study                                    budget-feasible alternatives but omits
                                                                                     the full CBA and counterpart choice.
           CR07     Ke et al. (2024)        contract / roster;   constrained         state-to-roster action. Abstract-only
                                            methodological       prescription        record; does not carry a decisive
                                            study;                                   field-level maturity judgment.
                                            abstract/metadata
                                            only
           CR08     Maymin (2017)           contract / roster;   constrained         state-to-personnel action.
                                            methodological       prescription        Abstract-only record; draft, trade, and
                                            study;                                   free-agency system is noted without
                                            abstract/metadata                        treating reported performance as
                                            only                                     validated deployment.
           CR09     Schmidt (2021)          contract / roster;   measurement         market state-to-team-building risk.
                                            primary empirical                        Abstract-only record; supports the
                                            study;                                   existence of a risk/uncertainty
                                            abstract/metadata                        question, not a decision-readiness
                                            only                                     conclusion.
           CR10     Zhang et al. (2026)     contract / roster;   constrained         state-to-dynamic roster action.
                                            preprint             prescription        Rolling-horizon stochastic
                                                                                     optimization is evaluated in a stylized
                                                                                     simulation, not an audited NBA
                                                                                     transaction environment.

                                                                                                  Continued on next page



                                                            38
Supplementary Evidence Appendix                                                  From Metrics to Decisions in NBA Analytics



           Table S4 continued from previous page
           ID       Source                    Stream / type         Furthest claim    Decision interface and principal
                                                                                      boundary

           CR11     NBA and NBPA              contract / roster;    not applicable    rule-state definition. Authoritative
                    (2023)                    official rule                           agreement defines legal states; it is not
                                                                                      evidence that a provision caused an
                                                                                      outcome.
           CR12     NBA (2024)                contract / roster;    not applicable    rule-state explainer. Official explainer
                                              official rule                           supplements but does not replace the
                                                                                      signed CBA.
           FF01     Tashman (2000)            framework             not applicable    point-in-time and rolling-origin
                                              foundation; review                      validation foundation.
                                                                                      Forecast-evaluation foundation;
                                                                                      excluded from the NBA synthesis
                                                                                      corpus and Figure 4 ratings.
           FF02     Pearl and Bareinboim      framework             not applicable    transportability and external-validity
                    (2014)                    foundation;                             foundation. Transportability
                                              methodological                          foundation; excluded from the NBA
                                              study                                   synthesis corpus and Figure 4 ratings.
           FF03     Manski (2003)             framework             not applicable    partial-identification foundation.
                                              foundation;                             Partial-identification foundation for
                                              methodological                          hidden opportunity sets; excluded
                                              study                                   from the NBA synthesis corpus and
                                                                                      Figure 4 ratings.
           FF04     Swaminathan and           framework             not applicable    off-policy evaluation foundation.
                    Joachims (2015)           foundation; full                        Logged-bandit and counterfactual-risk
                                              conference paper                        foundation; excluded from the NBA
                                                                                      synthesis corpus and Figure 4 ratings.
           FF05     Berger (1985)             framework             not applicable    statistical decision-theory foundation.
                                              foundation;                             Decision-theory foundation for
                                              methodological                          actions, uncertainty, utilities, and
                                              study                                   losses; excluded from the NBA
                                                                                      synthesis corpus and Figure 4 ratings.
           FF06     Howard (1966)             framework             not applicable    value-of-information foundation.
                                              foundation;                             Value-of-information foundation;
                                              methodological                          excluded from the NBA synthesis
                                              study                                   corpus and Figure 4 ratings.
           FF07     Bertsimas et al. (2011)   framework             not applicable    robust-optimization foundation.
                                              foundation; review                      Robust-optimization foundation;
                                                                                      excluded from the NBA synthesis
                                                                                      corpus and Figure 4 ratings.
           FF08     Boyd and                  framework             not applicable    constrained-optimization foundation.
                    Vandenberghe (2004)       foundation;                             Constrained-optimization foundation;
                                              methodological                          excluded from the NBA synthesis
                                              study                                   corpus and Figure 4 ratings.




S5. Limitations of the evidence record
1. Discovery was iterative and source capabilities were unequal; the corpus is not an exhaustive enumeration of NBA
   analytics.
2. The five domain tables used different native schemas. Harmonization improves comparability but cannot recover
   information a source workstream did not record, including a complete set of individual exclusion reasons for the
   76 non-retained reports.
3. Five retained records are abstract/metadata only and are restricted to positioning or scope claims.
4. Some studies use commercial tracking, internal medical data, unreleased historical collections, or unobserved
   bargaining and opportunity sets. Access to the paper does not imply that its analysis can be publicly replicated.
5. The maturity map is a structured qualitative synthesis, not a validated numerical scale. Ratings concern public
   research interfaces rather than individual paper quality.
6. The review applies the framework across research streams. It does not test whether adopting the framework
   improves team outcomes.

  The machine-readable companion file (nba-decision-readiness-evidence-map.csv) is openly available as a CSV
on GitHub. Domain-level evidence tables preserve the more detailed extraction fields used to produce this appendix.



                                                               39
From Metrics to Decisions in NBA Analytics                                      Critical integrative review



References
Arcidiacono P, Kinsler J and Price J (2017) Productivity spillovers in team production: Evidence from
  professional basketball. Journal of Labor Economics 35(1): 191–225.
  https://doi.org/10.1086/687529.

Barrientos AF, Sen D, Page GL et al. (2023) Bayesian inferences on uncertain ranks and orderings:
  Application to ranking players and lineups. Bayesian Analysis 18(3): 777–806.
  https://doi.org/10.1214/22-BA1324.

Belk JW, Marshall HA, McCarty EC et al. (2017) The effect of regular-season rest on playoff performance
  among players in the National Basketball Association. Orthopaedic Journal of Sports Medicine 5(10):
  2325967117729798. https://doi.org/10.1177/2325967117729798.

Berger JO (1985) Statistical decision theory and Bayesian analysis, 2nd ed. New York: Springer.
  https://doi.org/10.1007/978-1-4757-4286-2.

Berger T and Daumann F (2021) Jumping to conclusions: An analysis of the NBA Draft Combine
  athleticism data and its influence on managerial decision-making. Sport, Business and Management: An
  International Journal 11(5): 515–534. https://doi.org/10.1108/SBM-11-2020-0117.

Berri DJ, Brook SL and Fenn AJ (2011) From college to the pros: Predicting the NBA amateur player
  draft. Journal of Productivity Analysis 35: 25–35. https://doi.org/10.1007/s11123-010-0187-x.

Bertsimas D, Brown DB and Caramanis C (2011) Theory and applications of robust optimization. SIAM
  Review 53(3): 464–501. https://doi.org/10.1137/080734510.

Boyd S and Vandenberghe L (2004) Convex optimization. Cambridge: Cambridge University Press.
  https://doi.org/10.1017/CBO9780511804441.

Brill RS, Hughes J and Waldbaum N (2023) Algorithmic NBA player acquisition. Wharton Sports Research
  Journal, Fall 2023. Available at:
  https://wsb.wharton.upenn.edu/wp-content/uploads/2023/12/Brill_2023_Q.pdf (accessed 14
  September 2026).

Cervone D, D’Amour A, Bornn L et al. (2016) A multiresolution stochastic process model for predicting
  basketball possession outcomes. Journal of the American Statistical Association 111(514): 585–599.
  https://doi.org/10.1080/01621459.2016.1141685.

Charest J, Samuels CH, Bastien CH et al. (2021) Impacts of travel distance and travel direction on
  back-to-back games in the National Basketball Association. Journal of Clinical Sleep Medicine 17(11):
  2269–2274. https://doi.org/10.5664/jcsm.9446.

Chen K, Rein R, Memmert D et al. (2025) A critical evaluation of data utilization and analytical
  techniques in basketball performance analysis: A systematic review. International Journal of Sports
  Science and Coaching 20(5): 2286–2303. https://doi.org/10.1177/17479541251347142.

Cohan A, Schuster J and Fernandez J (2021) A deep learning approach to injury forecasting in NBA
  basketball. Journal of Sports Analytics 7(4): 277–289. https://doi.org/10.3233/JSA-200529.

Deshpande SK and Jensen ST (2016) Estimating an NBA player’s impact on his team’s chances of winning.
  Journal of Quantitative Analysis in Sports 12(2): 51–72. https://doi.org/10.1515/jqas-2015-0027.

Devlin S and Uminsky D (2020) Identifying group contributions in NBA lineups with spectral analysis.
  Journal of Sports Analytics 6(3): 215–234. https://doi.org/10.3233/JSA-200407.


                                                   40
From Metrics to Decisions in NBA Analytics                                        Critical integrative review


Drakos MC, Domb B, Starkey C et al. (2010) Injury in the National Basketball Association: A 17-year
  overview. Sports Health 2(4): 284–290. https://doi.org/10.1177/1941738109357303.

Ehrlich J, Sanders S and Boudreaux CJ (2019) The relative wages of offense and defense in the NBA: A
  setting for win-maximization arbitrage? Journal of Quantitative Analysis in Sports 15(3): 213–224.
  https://doi.org/10.1515/jqas-2018-0095.

Fearnhead P and Taylor BM (2011) On estimating the ability of NBA players. Journal of Quantitative
  Analysis in Sports 7(3): Article 11. https://doi.org/10.2202/1559-0410.1298.

Fewell JH, Armbruster D, Ingraham J et al. (2012) Basketball teams as strategic networks. PLOS ONE
  7(11): e47445. https://doi.org/10.1371/journal.pone.0047445.

Fisher JD and Montague C (2025) Improving the aggregation and evaluation of NBA mock drafts. Journal
  of Quantitative Analysis in Sports 21(4): 327–343. https://doi.org/10.1515/jqas-2023-0100.

Franks A, Miller A, Bornn L et al. (2015) Characterizing the spatial structure of defensive skill in
  professional basketball. The Annals of Applied Statistics 9(1): 94–121.
  https://doi.org/10.1214/14-AOAS799.

Franks AM, D’Amour A, Cervone D et al. (2016) Meta-analytics: Tools for understanding the statistical
  properties of sports metrics. Journal of Quantitative Analysis in Sports 12(4): 151–165.
  https://doi.org/10.1515/jqas-2016-0098.

Ghimire S, Ehrlich JA and Sanders SD (2020) Measuring individual worker output in a complementary
  team setting: Does regularized adjusted plus minus isolate individual NBA player contributions? PLOS
  ONE 15(8): e0237920. https://doi.org/10.1371/journal.pone.0237920.

Herzog MM, Brink A, Gondalia R et al. (2026) The relationship between games missed for rest or load
  management and injury in the National Basketball Association, 2014–15 through 2022–23. Sports
  Medicine 56(9): 2313–2323. https://doi.org/10.1007/s40279-026-02457-w.

Howard RA (1966) Information value theory. IEEE Transactions on Systems Science and Cybernetics 2(1):
  22–26. https://doi.org/10.1109/TSSC.1966.300074.

Huyghe T, Alcaraz PE, Calleja-González J et al. (2022) The underpinning factors of NBA game-play
  performance: A systematic review (2001–2020). The Physician and Sportsmedicine 50(2): 94–122.
  https://doi.org/10.1080/00913847.2021.1896957.

Ichniowski C and Preston A (2017) Does March Madness lead to irrational exuberance in the NBA draft?
   High-value employee selection decisions and decision-making bias. Journal of Economic Behavior and
   Organization 142: 105–119. https://doi.org/10.1016/j.jebo.2017.07.015.

Jutamulia I and Hosoi AE (2025) Leveraging expected action value to measure on-court decision-making
  skills in basketball. Journal of Sports Analytics 11: 1–15.
  https://doi.org/10.1177/22150218251325018.

Kaplan SM (2024) Leveling the playing field: The distributional impact of maximum- and minimum-level
  contracts on player compensation. Contemporary Economic Policy 42(2): 375–391.
  https://doi.org/10.1111/coep.12621.

Ke Y, Bian R and Chandra R (2024) A unified machine learning framework for basketball team roster
  construction: NBA and WNBA. Applied Soft Computing 153: 111298.
  https://doi.org/10.1016/j.asoc.2024.111298.


                                                     41
From Metrics to Decisions in NBA Analytics                                        Critical integrative review


Kovalchik SA (2023) Player tracking data in sports. Annual Review of Statistics and Its Application 10:
  677–697. https://doi.org/10.1146/annurev-statistics-033021-110117.

Kubatko J, Oliver D, Pelton K et al. (2007) A starting point for analyzing basketball statistics. Journal of
  Quantitative Analysis in Sports 3(3): Article 1. https://doi.org/10.2202/1559-0410.1070.

Kuehn J (2017) Accounting for complementary skill sets: Evaluating individual marginal value to a team
  in the National Basketball Association. Economic Inquiry 55(3): 1556–1578.
  https://doi.org/10.1111/ecin.12451.

Lautier JP (2025) A new framework to estimate return on investment for player salaries in the National
  Basketball Association. Applied Stochastic Models in Business and Industry 41(3): e70020.
  https://doi.org/10.1002/asmb.70020.

Lewis M (2018) It’s a hard-knock life: Game load, fatigue, and injury risk in the National Basketball
  Association. Journal of Athletic Training 53(5): 503–509.
  https://doi.org/10.4085/1062-6050-243-17.

Mack CD, Meisel P, Herzog MM et al. (2019) The establishment and refinement of the National Basketball
 Association Player Injury and Illness Database. Journal of Athletic Training 54(5): 466–471.
 https://doi.org/10.4085/1062-6050-18-19.

Manski CF (2003) Partial identification of probability distributions. New York: Springer.
 https://doi.org/10.1007/b97478.

Martonosi SE, Gonzalez M and Oshiro N (2023) Predicting elite NBA lineups using individual player order
 statistics. Journal of Quantitative Analysis in Sports 19(2): 51–71.
 https://doi.org/10.1515/jqas-2022-0039.

Maymin A, Maymin PZ and Shen E (2013) NBA chemistry: Positive and negative synergies in basketball.
 International Journal of Computer Science in Sport 12(2): 4–23. Author manuscript:
 https://doi.org/10.2139/ssrn.1935972.

Maymin PZ (2017) The automated general manager: Can an algorithmic system for drafts, trades, and free
 agency outperform human front offices? Journal of Global Sport Management 2(4): 234–249.
 https://doi.org/10.1080/24704067.2017.1389248.

Miller A, Bornn L, Adams RP et al. (2014) Factorized point process intensities: A spatial analysis of
  professional basketball. In: Proceedings of the 31st International Conference on Machine Learning, vol.
  32, pp.235–243. PMLR. Available at: https://proceedings.mlr.press/v32/miller14.html (accessed
  9 September 2026).

Muniz M and Flamand T (2022) A weighted network clustering approach in the NBA. Journal of Sports
 Analytics 8(4): 251–275. https://doi.org/10.3233/JSA-220584.

Muniz M and Flamand T (2023) Sports analytics for balanced team-building decisions. Journal of the
 Operational Research Society 74(8): 1892–1909. https://doi.org/10.1080/01605682.2022.2118634.

Nakamura-Sakai S, Forastiere L and Macdonald B (2024) Estimating the age-conditioned average
  treatment effects curves: An application for assessing load-management strategies in the NBA.
  arXiv:2402.12400. https://doi.org/10.48550/arXiv.2402.12400.

National Basketball Association (2024) 2024–25 CBA 101: Highlights of the NBA Collective Bargaining
  Agreement. Available at:
  https://cms.nba.com/wp-content/uploads/sites/4/2024/11/2024-25-CBA-101.pdf (accessed 1
  September 2026).


                                                     42
From Metrics to Decisions in NBA Analytics                                      Critical integrative review


National Basketball Association (2026) NBA Board of Governors approves new Draft Lottery system to
  address tanking. Official release, 28 May 2026. Available at:
  https://www.nba.com/news/nba-board-governors-approve-new-draft-lottery-system (accessed
  1 September 2026).

National Basketball Association and National Basketball Players Association (2023) Collective Bargaining
  Agreement, effective July 1, 2023. Available at: https://nbpa.com/cba (accessed 1 September 2026).

Pearl J and Bareinboim E (2014) External validity: From do-calculus to transportability across
  populations. Statistical Science 29(4): 579–595. https://doi.org/10.1214/14-STS486.

Price J, Soebbing BP, Berri D et al. (2010) Tournament incentives, league policy, and NBA team
  performance revisited. Journal of Sports Economics 11(2): 117–135.
  https://doi.org/10.1177/1527002510363103.

Russell JL, McLean BD, Stolp S et al. (2021) Quantifying training and game demands of a National
  Basketball Association season. Frontiers in Psychology 12: 793216.
  https://doi.org/10.3389/fpsyg.2021.793216.

Sandholtz N and Bornn L (2020) Markov decision processes with dynamic transition probabilities: An
  analysis of shooting strategies in basketball. The Annals of Applied Statistics 14(3): 1122–1145.
  https://doi.org/10.1214/20-AOAS1348.

Sarlis V and Tjortjis C (2020) Sports analytics: Evaluation of basketball players and team performance.
  Information Systems 93: 101562. https://doi.org/10.1016/j.is.2020.101562.

Schmidt MB (2021) Risk and uncertainty in team building: Evidence from a professional basketball
  market. Journal of Economic Behavior and Organization 186: 735–753.
  https://doi.org/10.1016/j.jebo.2020.11.001.

Schmidt MB (2024) On the incentive structure of tournaments: Evidence from the National Basketball
  Association’s Draft Lottery. Eastern Economic Journal 50(3): 400–429.
  https://doi.org/10.1057/s41302-024-00272-7.

Sill J (2010) Improved NBA adjusted plus-minus using regularization and out-of-sample testing. MIT Sloan
   Sports Analytics Conference. Available at: https://www.sloansportsconference.com/
   research-papers/improved-nba-adjusted-using-regularization-and-out-of-sample-testing
   (accessed 9 September 2026).

Skinner B (2012) The problem of shot selection in basketball. PLOS ONE 7(1): e30776.
  https://doi.org/10.1371/journal.pone.0030776.

Skinner B and Guy SJ (2015) A method for using player tracking data in basketball to learn player skills
  and predict team performance. PLOS ONE 10(9): e0136393.
  https://doi.org/10.1371/journal.pone.0136393.

Staw BM and Hoang H (1995) Sunk costs in the NBA: Why draft order affects playing time and survival in
  professional basketball. Administrative Science Quarterly 40(3): 474–494.
  https://doi.org/10.2307/2393794.

Swaminathan A and Joachims T (2015) Counterfactual risk minimization: Learning from logged bandit
  feedback. In: Proceedings of the 32nd International Conference on Machine Learning, vol. 37,
  pp.814–823. PMLR. Available at: https://proceedings.mlr.press/v37/swaminathan15.html
  (accessed 9 September 2026).


                                                   43
From Metrics to Decisions in NBA Analytics                                      Critical integrative review


Tashman LJ (2000) Out-of-sample tests of forecasting accuracy: An analysis and review. International
  Journal of Forecasting 16(4): 437–450. https://doi.org/10.1016/S0169-2070(00)00065-0.

Taylor BA and Trogdon JG (2002) Losing to win: Tournament incentives in the National Basketball
  Association. Journal of Labor Economics 20(1): 23–41. https://doi.org/10.1086/323930.

Teramoto M, Cross CL, Cushman DM et al. (2017) Game injuries in relation to game schedules in the
  National Basketball Association. Journal of Science and Medicine in Sport 20(3): 230–235.
  https://doi.org/10.1016/j.jsams.2016.08.020.

Terner Z and Franks A (2021) Modeling player and team performance in basketball. Annual Review of
  Statistics and Its Application 8: 1–23.
  https://doi.org/10.1146/annurev-statistics-040720-015536.

Wen R, Cao Q and Wang H (2023) Are pay decisions based on pre-contract efficiency necessarily correct?
 Evidence from players contracts of National Basketball Association. SAGE Open 13(4):
 21582440231204149. https://doi.org/10.1177/21582440231204149.

Zhang S, Shen Z, Chen S et al. (2026) A rolling-horizon stochastic optimization framework for NBA
  franchise management with distributionally robust risk constraints. arXiv:2604.06548. Available at:
  https://arxiv.org/abs/2604.06548 (accessed 9 September 2026).

Zhou Y and Li T (2024) Quantitative analysis of professional basketball: A qualitative discussion. Journal
  of Sports Analytics 9(4): 273–287. https://doi.org/10.3233/JSA-220713.




                                                    44
