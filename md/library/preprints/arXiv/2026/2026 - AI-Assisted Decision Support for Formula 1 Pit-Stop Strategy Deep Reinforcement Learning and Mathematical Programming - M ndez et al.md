<!-- source: library/preprints/arXiv/2026/2026 - AI-Assisted Decision Support for Formula 1 Pit-Stop Strategy Deep Reinforcement Learning and Mathematical Programming - M ndez et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.26909 -->
<!-- authors: Felipe Méndez, Charles Thraves -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-24; equations, tables and figures are NOT preserved - consult the PDF for those -->

# AI-Assisted Decision Support for Formula 1 Pit-Stop Strategy: Deep Reinforcement Learning and Mathematical Programming

                                             AI-Assisted Decision Support for Formula 1
                                           Pit-Stop Strategy: Deep Reinforcement Learning
                                                   and Mathematical Programming

                                                            Felipe Méndez1 and Charles Thraves1*
arXiv:2611.26909v1 [math.OC] 19 Nov 2026




                                           1*
                                                Department of Industrial Engineering, University of Chile, Beauchef
                                                                     851, Santiago, Chile.


                                                   *Corresponding author(s). E-mail(s): cthraves@dii.uchile.cl;
                                                      Contributing authors: felipe.mendez.p@ug.uchile.cl;


                                                                                Abstract
                                            Pit-stop strategy in Formula 1 is a sequential decision problem under uncer-
                                            tainty, in which strategists decide at each lap whether to pit and which tire
                                            compound to fit. We develop a data-driven simulator, calibrated with historical
                                            race data, that captures tire degradation, drivers’ recent performance, overtaking,
                                            yellow flag events, and rivals’ pit-stop decisions. We train agents with five Deep
                                            Reinforcement Learning (DRL) algorithms and compare them with a Quadratic
                                            Mixed-Integer Programming (QMIP) formulation that is optimal in determinis-
                                            tic single-driver settings. Without uncertainty or competition, all DRL methods
                                            except TRPO achieve near-optimal performance. With a full grid of competitors
                                            and stochastic race events, the ranking of DRL methods depends on the eval-
                                            uation setting: Proximal Policy Optimization (PPO) and its recurrent variant
                                            are the only methods that improve on the QMIP both in fully simulated races
                                            and when the actual 2024 races are replayed. Averaged over eight circuits, PPO
                                            improves on the QMIP by 0.33 and 0.49 positions in the two settings and Recur-
                                            rent PPO by less, and in the replay PPO finishes 0.66 positions ahead of the
                                            drivers’ actual strategies simulated in the same races. The QMIP performs sim-
                                            ilarly to the other methods, even though it cannot anticipate yellow flag events.
                                            Finally, we use the trained PPO policy as a look-ahead decision-support tool
                                            that shows the strategist the distribution of race outcomes under each candidate
                                            pit-stop action. Applied retrospectively to eight 2024 races, the look-ahead iden-
                                            tifies the laps where the actual decision, the recommendation, or a third action
                                            was preferable.

                                            Keywords: Decision Support, Human–AI Collaboration, Deep Reinforcement
                                            Learning, Pit-Stop Strategy, Mixed-Integer Programming, OR in Sports


                                                                                    1
1 Introduction
Many operational systems require high-stakes sequential decisions to be made under
uncertainty, strategic interaction, and severe time pressure. In such settings, human
decision-makers increasingly rely on AI-based decision-support systems, but fully
autonomous policies are often difficult to trust, interpret, and validate. This paper
studies this challenge in the context of Formula 1 pit-stop strategy, where teams
must decide under tire degradation, traffic, competitors’ actions, and stochastic race
interruptions.
    Although Formula 1 is a motorsport application, the underlying decision structure
is shared by many operational settings in which human decision-makers must act
under uncertainty, strategic interaction, and limited time, such as dynamic vehicle
dispatching (Pillac et al. 2013), disruption management in transportation networks
(Clausen et al. 2010), and real-time resource allocation (Powell 2016).
    Pit-stop strategy is a key determinant of performance in Formula 1 racing. At each
lap, a driver must decide whether to remain on track or perform a pit stop, trading
off the immediate time loss associated with pitting against the potential performance
gains from fresher tires. This decision is further complicated by the availability of
different tire compounds, namely soft, medium, and hard, which exhibit distinct trade-
offs between speed and degradation. Softer compounds provide faster lap times but
deteriorate more rapidly, while harder compounds are more durable but slower. In
addition, race regulations require drivers to use at least two different tire compounds
under dry conditions, further constraining feasible strategies.
    Stochastic race events also affect these decisions. In particular, yellow-flag periods,
including Safety Car (SC) and Virtual Safety Car (VSC) events, can substantially
alter the relative cost of pit stops. During these periods, cars are forced to reduce
speed and overtaking on track is restricted, which reduces the relative time lost in the
pit lane and can create strategic opportunities. Effective decisions therefore depend
on the current race state and on the possibility of future disruptions.
    Incorporating competition against rival cars further complicates the problem
through both physical interactions and strategic behavior. From a physical stand-
point, traffic conditions affect lap times, as overtaking is often difficult and inherently
stochastic, even when relative pace differences are known. From a strategic perspec-
tive, each driver’s decision influences and is influenced by the actions of others, leading
to a high-dimensional dynamic game. With approximately 20 drivers making pit-
stop and tire-compound decisions over the course of a race, the joint decision space
grows rapidly with the number of laps and drivers, making exact modeling approaches
computationally challenging.
    The combination of stochastic race dynamics, operational constraints, and strate-
gic interactions makes pit-stop optimization difficult. This difficulty is particularly
relevant for AI-assisted decision support: exact optimization can provide high-quality
solutions and structural insight, but becomes computationally impractical in realistic
multi-driver settings, while learning-based policies can generate fast recommendations
once trained but require careful validation and interpretation. This paper addresses
this trade-off by studying deep reinforcement learning (DRL) methods for Formula 1
pit-stop strategy and evaluating them against an exact mathematical programming


                                            2
benchmark. From this perspective, learning-based policies are not intended to replace
human strategists, but to support them with fast recommendations and interpretable
summaries of alternative actions.
    Existing approaches to pit-stop strategy include simulation-based methods,
supervised learning models trained on historical race decisions, exact optimization
approaches based on dynamic programming or mathematical programming, and, more
recently, reinforcement learning methods. Simulation and supervised learning can
capture realistic race features and generate fast recommendations, but they do not nec-
essarily identify optimal strategies. Exact optimization methods provide benchmarks
and structural insight, but their scalability is limited in realistic multi-driver settings.
Learning-based policies scale to high-dimensional sequential decision problems, but
their use as decision-support tools raises questions of reliability and interpretability
that motivate our study. Section 2 reviews these streams in detail.
    Three challenges remain open for AI-assisted decision support in pit-stop strategy.
First, learning-based policies should be validated against exact optimization bench-
marks whenever such benchmarks are available. Second, their performance under
competition and stochastic race events should be checked against the realizations of
actual races, which, to our knowledge, has not been done for DRL. Third, recommen-
dations should be translated into interpretable summaries that allow human strategists
to compare alternative actions and assess their associated risks.
    To address these challenges, we investigate the following three research questions:
(i) To what extent can DRL-based pit-stop policies reproduce optimal decisions in
settings where exact solutions are available? (ii) How reliable are learning-based rec-
ommendations under competition and multiple sources of uncertainty, in simulated
races and in replays of the actual 2024 races? (iii) How can the outcomes of alternative
pit-stop actions be evaluated and visualized to help human strategists understand the
risks and expected outcomes of competing race decisions?
    The main contributions of this paper are as follows:
• We develop a data-driven race simulation environment calibrated with public histori-
  cal race data from 2021 to 2024. The environment captures key sources of operational
  uncertainty, including lap-time variability, driver interactions, overtaking dynam-
  ics, and yellow-flag events. It also incorporates predictive models of rivals’ pit-stop
  behavior and updates driver-specific performance estimates using only information
  available prior to each race, so that the whole procedure can be run before a Grand
  Prix.
• We evaluate five DRL methods against an exact QMIP benchmark. In simplified
  deterministic settings, where optimal solutions can be computed, this comparison
  allows us to quantify the optimality gap of learning-based policies. In realistic full-
  grid scenarios with competition and multiple sources of uncertainty, we compare
  learning-based recommendations with an exact optimization benchmark that uses
  a simplified race representation. The evaluation covers eight circuits of the 2024
  season, in both fully simulated races and replays of the actual races. Performance
  relative to the QMIP varies across DRL methods, so the choice of algorithm matters.
• We show how the resulting policies can support human race strategists through
  look-ahead simulations of alternative pit-stop decisions. For selected race states,


                                             3
  the framework evaluates and visualizes the distribution of final outcomes under
  each feasible action, allowing decision-makers to compare expected performance,
  downside risk, and outcome variability. We also apply it retrospectively to review
  the pit-stop decisions taken in the 2024 races.
    The remainder of the paper is organized as follows. Section 2 reviews the rele-
vant literature. Section 3 describes the race simulation environment and its calibration
based on historical race data. Section 4 formulates the pit-stop decision problem,
including the state and action spaces, rivals’ behavior, and the reward function.
Section 5 introduces an exact quadratic mixed-integer programming (QMIP) formula-
tion for simplified instances. Section 6 validates the learned policies against the QMIP
and in full-grid race scenarios. Section 7 presents the look-ahead decision-support
analysis, and Section 8 concludes. The appendices follow the references.

2 Related Literature
2.1 Race Strategy and Pit-Stop Optimization
Different approaches have been proposed to address the pit-stop optimization prob-
lem, ranging from exact methods to simulation-based and learning-based techniques.
Exact approaches, such as mathematical programming and dynamic programming
(DP), provide optimal solutions but are typically limited to simplified settings due
to the exponential growth of the state space. Prior to the development of such meth-
ods, simulation was widely used to evaluate candidate strategies by modeling race
dynamics that involve uncertainty, including overtaking, tire degradation, lap time
variability, safety car deployments, Drag Reduction System (DRS),1 and driver inter-
actions (Bekker and Lotz 2009; Phillips 2014; Heilmeier et al. 2018; Sulsters 2018;
Heilmeier et al. 2020). While simulation enables the incorporation of realistic and
complex racing events, it is computationally intensive and requires evaluating a large
number of scenarios to identify high-performing strategies.
    Machine learning approaches have also been explored as decision-support tools.
Supervised methods such as Random Forests, Support Vector Machines, and LASSO
have been trained on historical race data to emulate pit-stop decisions (Tulabandhula
and Rudin 2014; Choo 2015; Fatima and Johrendt 2023). More recently, Sasikumar
et al. (2025) propose a supervised deep learning framework using Bi-LSTM and related
architectures to predict pit stop timing from telemetry data, achieving strong classi-
fication performance. These approaches can provide real-time recommendations but
are inherently limited by the quality of historical decisions, as they tend to replicate
past strategies rather than identify optimal ones. Hybrid approaches combining opti-
mization and learning have also been proposed; for instance, Heilmeier et al. (2020)
integrate neural networks with optimization models to guide decision-making.
    Exact solution methods based on dynamic programming (DP) have recently been
proposed for pit-stop optimization problems. In a single-driver setting, Carrasco Heine
and Thraves (2023) formulate the problem as a stochastic DP in which, at each lap, the

  1
    The Drag Reduction System, introduced in 2011, is a car feature that allows a driver to open the rear
wing to reduce air resistance on certain straights when trailing another car within one second.



                                                   4
driver decides whether to change tires based on the current race state. Despite incor-
porating stochastic elements such as yellow flag events, the absence of competition
allows for the practical enumeration of all relevant states. Extensions to multi-driver
settings have been explored using game-theoretic formulations. In particular, Aguad
and Thraves (2024) model the interaction between two drivers as a feedback Stack-
elberg game, showing that the problem remains computationally tractable despite a
state space on the order of billions. However, these approaches do not scale to realistic
race settings involving more than two drivers, as the state space grows exponentially
with the number of agents. This limitation motivates the use of approximate meth-
ods, such as DRL, which can handle large state spaces while maintaining a relatively
small action space.

2.2 Learning-Based Methods for Race Strategy
The comparison between DRL and classical optimization approaches has attracted
growing interest across multiple operations research domains. In inventory manage-
ment, Gijsbrechts et al. (2022) provide a rigorous evaluation of DRL against optimal
and near-optimal analytical policies in classic intractable inventory problems, while
Dehaybe et al. (2024) evaluate DRL under non-stationary uncertain demand. In power
systems scheduling, O’Malley et al. (2023) conduct a head-to-head comparison of
MIP and reinforcement learning for unit commitment, finding that MIP consistently
produces lower-cost schedules, though RL’s key advantage lies in generating solu-
tions practically instantly regardless of problem size. These results suggest that the
relative performance of DRL and classical optimization methods is highly problem-
dependent. However, comparable evaluations against exact optimization benchmarks
remain limited in the context of pit-stop strategy optimization.
    DRL has recently been applied to high-dimensional sequential decision problems.
In motorsports, DRL has been applied to trajectory optimization, energy management,
and refueling strategies (Remonda et al. 2021; Hoeppke 2022; Liu et al. 2023; Evans
et al. 2023; Liu et al. 2021; Boettinger and Klotz 2023).
    In the context of pit-stop strategies, Piccinotti et al. (2021) simulate lap times
calibrated with XGBoost and evaluate different implementations of Monte Carlo
Tree Search (MCTS) to identify optimal sequences of actions. Among the methods
considered, an open-loop Q-learning approach achieves the best performance. More
recent work has focused on DRL methods. Using Deep Q-Networks (DQN), Marinaro
(2023) compares single-agent, multi-agent, and hybrid learning approaches, showing
that the hybrid setting achieves strong performance with reduced data requirements.
Rebé Martı́n (2024) evaluates DQN, QR-DQN, and A2C under different reward
specifications based on positions and final outcomes, finding that A2C consistently
outperforms the alternatives. Similarly, Thomas et al. (2025) propose a recurrent DRL
architecture that integrates simulation and live-race data, using reward functions based
primarily on championship points. In the first author’s Master’s thesis (Méndez Pérez
2025), which this paper extends with a revised simulator, five DRL algorithms were
compared with the QMIP in the single-driver deterministic case. Fieni et al. (2025),
in work independent of ours, formulate a single-driver problem at the Bahrain circuit



                                           5
that also allocates energy, solve it as a mixed-integer nonlinear program, and com-
pare the solution with a Soft Actor-Critic agent. Their setting has no competitors
and no stochastic race events. More recently, Fieni et al. (2026) propose a multi-
agent reinforcement learning framework that jointly optimizes energy management,
pit stop timing, and tire selection using a self-play training scheme, demonstrating
that agents adapt their strategies in response to competitors’ actions. However, the
framework is evaluated in pairwise duels between its own agents at a single circuit,
without stochastic race events.

2.3 AI-Assisted Decision Support and Learning-Based
    Optimization
The use of learning-based policies as decision-support tools connects this work to the
broader literature on human–AI decision-making. In AI-assisted decisions, a recom-
mendation should also help the decision-maker judge when to follow, question, or
override it. A recurring theme in this literature is appropriate reliance: users should
defer to correct recommendations and rely on their own judgment when the model
is likely to err (Schemmer et al. 2022), and reliance and decision quality are dis-
tinct outcomes that explanations and additional decision-support information can help
align (Schoeffer et al. 2025; Leichtmann et al. 2023). A complementary line of work
frames decision support as the visualization and exploration of trade-offs and outcome
uncertainty across a set of candidate solutions, rather than the delivery of a single
recommendation; in the context of multi-objective optimization, Osika et al. (2023)
survey such methods and identify visualization, uncertainty exploration, and inter-
activity as core mechanisms for helping a decision-maker choose among alternatives.
These ideas have also been instantiated in real-time, safety-critical operations: Abbas
et al. (2025) integrate deep reinforcement learning into a human-in-the-loop decision-
support system for industrial control rooms, providing operators with intervention
strategies adapted to the state of both the process and the operator under information
overload. Pit-stop strategy shares the defining features of these settings: recommen-
dations must be interpreted under severe time pressure, alongside information not
fully encoded in the simulator, and with limited opportunity to revise a decision once
made. Our look-ahead visualization builds directly on this perspective, presenting the
strategist not with a single prescribed action but with the full distribution of outcomes
under each feasible alternative, so that expected performance and downside risk can
be weighed jointly.
    Taken together, this body of work shows that learning-based methods are promising
for race strategy, yet no existing study brings together the three elements needed for
reliable decision support: benchmarking against an exact optimum, evaluation against
actual race realizations, and interpretable comparison of the actions available at each
lap.

3 Race Simulation Environment
We begin by describing the problem setting. Consider a given driver racing in a For-
mula 1 Grand Prix at a specific circuit. Let N denote the number of laps, D the set


                                           6
of drivers, C = {C0, C1, C2, C3, C4, C5} the set of tire compounds2 , and Y the set of
past seasons for which lap-time data are available for each driver, Grand Prix, and lap,
as well as from previous races in the current season. The objective is to construct a
simulation environment that generates realistic lap times and captures race dynamics,
enabling the optimization of pit-stop strategies via DRL.
    To train the reinforcement learning agent, it is essential to accurately model lap
times, as they determine both the state transitions and the reward signal. To this
end, we calibrate a regression model for each circuit using historical lap-time data. We
consider two scenarios: one under clear track conditions and another under VSC or SC
periods, to account for the differences in lap times across these settings. In addition,
we incorporate data from previous races in the same season to update driver-specific
effects and capture recent performance. Finally, we use a logit model to simulate
overtaking events.
    We use race data from the Python library FastF1 (Schaefer 2024), which provides
detailed information for the 2021–2024 seasons. We use OpenF1 (2026) for tire data
that are missing from or inconsistent with FastF1. The data and code supporting this
study are publicly available at Méndez and Thraves (2026). The dataset includes lap
times, telemetry, car positions, tire usage, weather conditions, event schedules, and
session results. In the lap-time models, we exclude race editions in which more than
10% of the laps were run on intermediate or wet tires, as well as laps on these tires
in the remaining editions. The overtaking and rivals’ models exclude only the laps on
these tires. As a result, the Emilia Romagna GP, whose 2021 and 2022 editions were
wet and whose 2023 edition was cancelled, is not considered. Tire construction changed
with the 2022 technical regulations, so a given tire age in 2021 does not correspond to
the same wear as in later seasons. In all models that use tire age, we multiply the 2021
tire age by a factor f = 0.78, common to all compounds and estimated from lap times
and pit-stop decisions (see Appendix A). Tire age does not count laps under SC, VSC
or red flag, and the age of a set used earlier in the weekend counts only its push laps,
within 10% of the driver’s best lap of the session. In addition, we construct variables
capturing the time gaps between consecutive cars, which are critical for modeling race
dynamics, as both following closely behind another car and having a car directly ahead
can lead to time losses.

3.1 Lap-Time Model under Clear-Track Conditions (RegLTC)
3.1.1 Base model:
We use a linear regression model to predict lap times using historical data from pre-
vious races at the same circuit. A separate model is estimated for each circuit, as
circuits exhibit substantial heterogeneity, particularly in how tire degradation affects

 2
     For each GP, a set of three compounds is selected from these.




                                                     7
lap-time performance. The regression model is specified as follows:
                                                                    X               X
                       2
y = β0 + β1 XLap + β2 XLap + β3 XPitIn + β4 XPitOut +                     βd Xd +         βy Xy + βDRS XDRS
                                                                    d∈D             y∈Y
        X                 X
    +         βc,1 Xc +         βc,2 Xc XTireLife + β∆1 e−X∆1 + β∆2 e−X∆2 + β1pos X1pos ,
        c∈C               c∈C
                                                                                       (1)
where each observation corresponds to a driver–year–lap triplet for the circuit under
analysis. The intercept represents the lap time of a reference driver and tire com-
                                                                           2
pound on fresh tires with initial fuel load. The terms β1 XLap and β2 XLap     capture the
effect of fuel consumption over the race, allowing for non-linear improvements in lap
times as the car becomes lighter. Pit-related time losses are modeled through β3 XPitIn
and β4 XPitOut . Driver- and year-specific heterogeneity are captured via fixed effects
{βd }d∈D and {βy }y∈Y , respectively. The effect of DRS availability is represented by
βDRS XDRS . Tire effects are modeled through a compound-specific intercept βc,1 and
an interaction term βc,2 Xc XTireLife , capturing both baseline performance and degra-
dation. As tire usage increases, lap times are expected to increase, implying positive
slope coefficients, with softer compounds exhibiting faster degradation than harder
ones. Conversely, softer compounds are expected to have lower intercepts due to their
superior initial grip. The terms β∆1 e−X∆1 and β∆2 e−X∆2 capture the impact of nearby
cars, where the exponential specification ensures a decreasing effect as the time gap
increases. Finally, β1pos X1pos accounts for additional time associated with the start-
ing position in the first lap. Table 1 provides a detailed description of the independent
variables. At some circuits the compound coefficients βc,1 and βc,2 are poorly identi-
fied, either because a compound was rarely used or because tire age is highly correlated
with the lap number. We therefore replace them with the estimates of a model fitted
jointly across circuits, in which softer compounds are faster when new and degrade
faster, and each circuit’s degradation level is shrunk toward the common mean (see
Appendix B).


   Variable           Values            Description
    XLap            {1, . . . , N }     Lap number
   XPitIn             {0, 1}            1 if the car is entering the pit lane in the lap, 0 otherwise
   XPitOut            {0, 1}            1 if the car is exiting the pit lane in the lap, 0 otherwise
  {Xd }d∈D            {0, 1}            1 if the driver is d, 0 otherwise
  {Xy }y∈Y            {0, 1}            1 if the year is y, 0 otherwise
   XDRS               {0, 1}            1 if the car ahead is within one second, 0 otherwise
  {Xc }c∈C            {0, 1}            1 if tire compound c is being used, 0 otherwise
  XTireLife         {1, . . . , N }     Tire age (in laps)
    X∆1                  R+             Time gap (seconds) to the car behind
    X∆2                  R+             Time gap (seconds) to the car ahead
    X1pos           {1, . . . , 20}     Starting position in the first lap (0 otherwise)
    XVSC              {0, 1}            1 if there is a VSC during the lap, 0 otherwise
    XSC               {0, 1}            1 if there is a SC during the lap, 0 otherwise

Table 1 Description of the independent variables in the regression model




                                                      8
3.1.2 Removing outliers
In some cases, observed lap times may differ considerably from the values predicted
by the linear regression model. This can be explained by factors not captured in the
model, many of which are unobserved. For instance, a driver may make a mistake in
a corner, resulting in a loss of more than one second and a large residual. To mitigate
the impact of such events, we remove these observations from the dataset to prevent
them from biasing the estimation of the model coefficients. This step is particularly
important for the tire compound coefficients, as inaccurate estimates would distort
the agent’s understanding of tire performance and may lead to unrealistic strategies.
    We first discard the laps that are at least 15 seconds slower than the median lap
time of their race, except for in-laps, out-laps and the first lap. We then adopt an iter-
ative procedure to remove outliers. First, we estimate the linear regression model and
identify observations whose residuals lie more than three interquartile ranges (IQR)
below the first quartile or above the third quartile of the residual distribution. If any
such observations are found, they are removed from the dataset and the regression is
re-estimated. This process is repeated until no additional outliers are detected (at most
ten iterations). The procedure is summarized in Algorithm 1. It is important to note


Algorithm 1 Outlier elimination with IQR
Require: I ← D × Y × {1, . . . , N } and covariates-laptimes {x(i) , y (i) }i∈I
 1: while true do                     
                      (i) (i) 
 2:   ŷi ← LinReg      x ,y       i∈I
                                         using Equation (1)
 3:   êi ← yi − ŷi ∀i ∈ I
 4:   Q3 ← 75% percentile of {êi }i∈I
 5:   Q1 ← 25% percentile of {êi }i∈I
 6:   IQR ← Q3 − Q1
 7:   J ← {i ∈ I | êi ∈
                       / [Q1 − 3 · IQR, Q3 + 3 · IQR]}
 8:   I ←I \J
 9:   if |J | = 0 then
10:       break


that this procedure does not directly remove outliers in lap times, but instead excludes
observations with large residuals. The iterative nature of the algorithm ensures that
such observations are progressively identified, including those that may initially be
masked by other extreme values. The primary objective of this procedure is to prevent
parameter estimates from being biased, with any improvement in model fit arising as
a secondary effect.

3.1.3 Updating drivers’ coefficients based on recent performance
Up to this point, the performance of each driver at the target circuit, captured by βd in
Equation (1), is estimated using lap-time data from previous years of the same circuit.
However, driver performance varies over time, both across seasons and across races
within the same season. This variability can be explained by factors such as changes


                                            9
in regulations, updates in car components, and drivers adjusting to their cars, among
others. Figure 1 illustrates how a driver’s performance can vary across different years.
Therefore, recent races in the current season provide valuable information to better
capture these dynamics in the model.

                                                2021–2023 seasons                                   2024 season

                       25             Norris (McLaren)
 Championship Points



                                      Hamilton (Mercedes)
                       20
                       15
                       10
                        5
                        0




                                                                                                      Ch an




                                                                                              re u in



                                                                                              N e ary
                                                                                                  he ium



                                                                                             U Sin aij y
                                                                                              ni g an
                                                                                                     St e
                                 21




                                                            2




                                                                                   23




                                                                                                  A rab n
                                                                                                    us ia
                                                                                                      Ja lia

                                                                                                     M ina
                                                                                                     E mi
                                                                                                      on ia
                                                                                                        na o
                                                                                                       S da

                                                                                                     B tria
                                                                                                     un in




                                                                                                  ze Ita s




                                                                                                       ex s
                                                                                                             o
                                                                                                  d or
                                                                                                     rb l
                                                                                                          nd




                                                                                                    M ate
                                                             2




                                                                                                    Ca ac




                                                                                                          ic
                                                                                                   i A rai




                                                                                             G A pa
                                                                                                   M mil




                                                                                                   H rita
                                                                                                          p
                                                                                                         a
                                20




                                                          20




                                                                                20




                                                                                                        ia




                                                                                                         g




                                                                                                te ap
                                                                                                      rla
                                                                                                 at s
                                                                                                       tr




                                                                                                et lg
                                                                                                ud ah
                            o




                                                     o




                                                                           o




                                                                                             Sa B




                                                                                                   B
                           ic




                                                     ic




                                                                           ic
                        ex




                                                    ex




                                                                         ex




                                                                                                A
                       M




                                                 M




                                                                        M



Fig. 1 Race points of Hamilton and Norris at the Mexican Grand Prix in 2021–2023 and in the 2024
races up to that Grand Prix. Red markers show the 2024 Mexican Grand Prix.


   To account for these dynamics, we predict each driver’s coefficient for the target
race from information available before it, and use these predictions in place of the
coefficients {βd }d∈D of Equation (1). The prediction model is estimated with all drivers
and races of 2021–2024 that precede the target race:

                                                                 3
                                                z                X
                                                pole
                                                     = α0 +            αPrevi XPrevi + αFP XFP + αQ XQ ,          (2)
                                            T                    i=1

where each observation is a driver–race pair, z is the driver’s coefficient estimated with
Equation (1) using only that race, and T pole is the pole lap time of that race weekend.
The variables XPrevi are the driver’s coefficients in their three most recent races, each
divided by the pole lap time of its race, and XFP and XQ are the relative differences
between the driver’s best lap time in the free practice and qualifying sessions of the
same weekend and that of the reference driver. The prediction is multiplied by the
pole lap time of the target race. The treatment of missing sessions, drivers with few
previous races and races with few clean laps, as well as alternative specifications, are
in Appendix C.
    The resulting linear regression used to generate lap times under clear-track con-
ditions, denoted by RegLTC, is obtained by iteratively applying Equation (1) as
described in Algorithm 1, followed by updating the driver-specific coefficients using
Equation (2).
    To incorporate stochasticity, lap times are sampled from a Normal distribution
with mean equal to the predicted value and variance σ̂ 2 (1 + X0T (X T X )−1 X0 ), the


                                                                                        10
predictive variance of the regression model, where σ̂ 2 is the estimated residual variance,
X0 is the feature vector of the new observation, and X is the design matrix used for
estimation. Since the driver coefficient predicted by Equation (2) is also imperfect, in
each simulated race it is perturbed by a draw from a zero-mean normal distribution,
kept fixed during the race. Its standard deviation is that of the prediction error in the
eight 2024 races of Section 6.3, net of the sampling error of the coefficient estimated
with each race.

3.2 Lap-Time Model under Safety Car and Virtual Safety Car
    (RegLTSC)
Under VSC or SC conditions, lap times are mainly determined by the imposed speed
limit, and tire age and compound have little effect. We therefore model them as a
multiple of the reference clear-track lap time of circuit g , L(g) , and the pit-lane time
loss as a fraction of the corresponding clear-track loss:
                                                 ′               ′
       y = L(g) (ρVSC XVSC + (ρSC + ug )XSC ) + βPitIn XPitIn + βPitOut XPitOut ,      (3)

       ′           (g)       ′                    (g)         (g)        (g)
with βPitIn  = κin Gin and βPitOut = κout Gout , where Gin and Gout are the clear-track
time losses of the in-lap and out-lap at circuit g , and ug is a circuit effect under SC.
The model is estimated jointly over all circuits using the 2021–2023 laps run entirely
under VSC or SC, so it does not require yellow flag events to be observed at every
circuit (see Appendix D). Under SC, the field regroups progressively: in the second
lap the gaps between consecutive cars are halved, and from the third lap the cars run
in line, 1.5 seconds apart. Pit stops under SC are only allowed in its first lap.
    The resulting regression model used to generate lap times under yellow flag
conditions is denoted as RegLTYF.

3.3 Overtaking Model (LogitOvertake)
The components introduced in the previous sections allow us to simulate lap times.
However, in practice, executing an overtaking maneuver requires more than a trailing
car being sufficiently fast to close the gap with the car ahead; it must also be able
to complete the pass. In other words, overtakes may not occur even when lap-time
predictions suggest they should. To model overtaking behavior more realistically and
consistently with observed data, we estimate the following logistic regression model:
                                       
                                   p
                         ln                 = γ0 + γPredGap XPredGap ,                 (4)
                                  1−p

where p denotes the probability that an overtake occurs for a given car and lap. The
model is estimated per Grand Prix on pairs of consecutive cars, on laps without SC,
VSC or red flag. The dependent variable is binary, taking value 1 if the trailing car
finishes the lap ahead of the car it was following and 0 otherwise. The explanatory
variable XPredGap represents the predicted time gap between two consecutive cars at
the end of the lap. Specifically, it is computed as the current time gap at the beginning


                                                 11
of the lap, plus the predicted lap time of the trailing car, minus the predicted lap time
of the leading car. Predicted lap times are obtained from RegLTC.
    It is worth noting that Equation (4) does not guarantee an overtake even when
the predicted gap is negative (i.e., when the trailing car would theoretically pass the
leading car), since p < 1. To ensure physically consistent simulations, we impose
that, following an overtake, the resulting time gap between consecutive cars is at least
tmin gap .
    Finally, overtaking on track is not permitted under SC or VSC conditions. Accord-
ingly, the LogitOvertake model is applied only under clear-track conditions; during
yellow flag periods, position changes occur solely as a consequence of pit stops and
are resolved deterministically from the resulting time gaps.
    This model is referred to as LogitOvertake.

4 Pit-Stop Decision Model
Near the end of each lap, the agent decides, based on the current race state, whether
to stay on track or perform a pit stop, selecting one of the available tire compounds.
When the decision is made, the agent already knows whether the next lap will be
run under clear track, VSC or SC, as rivals do. In this section, we formally define
the agent’s action space, state representation, reward function, and state transition
dynamics.

4.1 Action Space
The agent’s action space consists of four possible actions: staying on track or chang-
ing tires to one of the three compounds available for the Grand Prix g , denoted by
C (g,2024) ⊆ C . The coefficients of compounds rarely used at a circuit are obtained from
the joint model described in Section 3.1.1, so all three compounds are available, and
we write C r = C (g,2024) . The action space is then defined as {0}∪C r , where 0 represents
the action of staying on track (i.e., not performing a pit stop). At the initial lap, the
agent must select the starting tire compound, and action 0 is penalized (Section 4.4).
Each driver starts the race with the dry tire sets available to them in the 2024 race,
some of which were already used in practice or qualifying. Under the 2024 Sporting
Regulations, a driver receives 13 dry sets per weekend (12 in sprint weekends) and
returns some of them after each practice and qualifying session, which leaves about
seven sets at the start of the race, including at least one hard and one medium set.
Since the returned sets are not reported, we infer them from the sets used in each
session (Appendix E). A pit stop fits the least-worn set of the chosen compound, and
the tire age of the new stint starts at the age of that set. The set taken off returns to
the driver’s sets with its age and can be fitted again, so a set of every compound is
always available. Rivals fit their sets in the same way.

4.2 State Space
The state space consists of features that describe relevant information about the agent
and its opponents. These include: the current lap, the number of remaining laps, the


                                            12
tire compound of each car, the tire age of each car, the age of the set of each compound
that a pit stop would fit, the time gap between the agent and each opponent, an
indicator of whether each car has used at least two different tire compounds, the
number of remaining laps under VSC or SC conditions, the agent’s action in the
previous lap, and the position of each car. A summary of the state variables is provided
in Table 2.

      Variable               Values                                Description
                                    r
      STire,d                   C                   Tire compound in use of each driver d ∈ D
                                                 Age in laps of the tire set in use of each driver
    STireLife,d                Z≥0
                                                                        d∈D
                                                Age of the set of compound c ∈ C r that the agent
     SSetAge,c                 Z≥0
                                                      would fit by stopping in the current lap
       SLap                {1, . . . , N }                      Current lap number
     SLaps Left            {1, . . . , N }             Number of remaining laps in the race
                                                 1 if at least two different compounds have been
     SChange,d                {0, 1}
                                                         used by driver d ∈ D, 0 otherwise
        SSC              {0, 1, 2, 3, 4}                Number of remaining laps under SC
       SVSC                 {0, 1, 2}                  Number of remaining laps under VSC
    SPrevAction             {0} ∪ C r             Action taken by the agent in the previous lap
    SPosition,d         {1, 2, 3, . . . , 20}              Current position of car d ∈ D
                                                  Time difference in seconds between car d ∈ D
      SGap,d                     R
                                                       and the agent, negative if d is ahead

 Table 2 Description of state variables for the agent.




4.3 Rivals’ Strategy
A key component of the environment is how the agent’s rivals make their decisions.
On the one hand, rivals could act randomly by assigning probabilities to each possible
action. On the other hand, they can follow more structured strategies, for instance by
emulating decisions observed in real race data. The former approach may lead to unre-
alistic or suboptimal rival behavior, which can negatively affect the learning process.
Therefore, we adopt the latter approach. Specifically, we use two predictive models to
determine each rival’s action at every lap: the first model predicts whether the rival
performs a pit stop or stays on track, and the second model selects the tire com-
pound (from those available for the Grand Prix) if a pit stop is made. During training,
each rival may also retire from the race, with the probability and lap of retirement
estimated from 2021–2023 races. When rivals’ decisions are simulated, their starting
compounds are drawn for each race from a common distribution p ∼ Dirichlet(α, α, α)
over the three available compounds, with α = 0.437 estimated by maximum likelihood
from the starting compounds of 19 races held at the same circuits in 2021–2023, which
reproduces the tendency of most drivers to start on the same compound.




                                                 13
4.3.1 Pit Stop Decision (LogitStop)
We use a logistic regression model to estimate the probability that a driver performs
a pit stop, as described by
              
          q
ln                 = δ0 + δSC XSC + δVSC XVSC + δChange XChange + δEarly XEarly + δLate XLate
         1−q
                       X
                     +     δTireLife,c XTireLife Xc + δpos Xpos + δGP XGP .
                       c∈C
                                                                                        (5)
Here, q denotes the probability of performing a pit stop. The variables XSC = 1{SSC >0}
and XVSC = 1{SVSC >0} indicate whether the current lap is under SC or VSC condi-
tions, respectively. The variable XChange = SChange indicates whether the driver has
already used two compounds, while XEarly = 1{SLaps ≤10} and XLate = 1{SLaps ≥N −10}
indicate the first and last ten laps of the race. The variable Xpos denotes the driver’s
position, and XGP corresponds to a set of Grand Prix indicator variables. The vari-
ables Xc and XTireLife are defined in Table 1. This model captures how race conditions
and strategic context influence pit-stop decisions, and is referred to as LogitStop. In
the simulation, rivals do not stop in the first five laps and, under green flag conditions,
neither with seven or fewer laps to go nor before completing eight laps on the current
set; under SC or VSC, they may only stop on the first lap of the period. If a rival
that has not yet used two compounds would fit the same compound again, a different
compound is drawn at random. Consistently with this rule, the model is estimated
with one observation per driver and SC or VSC period, placed on the first lap of the
period and equal to one if the driver stopped at any lap of it.

4.3.2 Tire Compound Choice (CondLogitCompound)
Once a pit-stop decision is made, the driver must choose the tire compound for the
next stint. To model this decision, we use a conditional logistic regression calibrated
using data from previous years. A conditional model is appropriate since the set of
available compounds varies across year–Grand Prix combinations, allowing the model
to account for the specific choice set at each pit stop. More specifically, the utility
associated with selecting compound c is specified as

                      Uc = νc + νc,LapsLeft Xc XLapsLeft + νNoChange XNoChange ,         (6)

where c denotes the compound being evaluated, and XNoChange equals 1 if c is the
only compound that has been used so far. XLapsLeft = N − SLaps is the number of
remaining laps, and compound C3 is the base alternative. Grand Prix indicators are
not included, since they are common to all alternatives and cancel out in a conditional
logit. This conditional logistic model is denoted as CondLogitCompound.




                                                 14
4.4 Reward Function
The reward in the Formula 1 simulation environment is defined as a combination of
three components: (i) race time, (ii) race points, and (iii) penalties. The first com-
ponent is given by the negative lap time (in seconds), computed using the regression
models in Equations (1) and (3). This encourages the agent to minimize lap time and
make decisions that improve race performance. The second component accounts for
the points awarded based on the final race position. Points are assigned as 25, 18, 15,
12, 10, 8, 6, 4, 2, and 1 for the top ten positions, and 0 otherwise. To align the scale
of this component with lap times, the points are multiplied by a factor of 300 before
being incorporated into the reward. In addition, 150 (21 − p) is added, where p is the
final position, so that the reward also distinguishes positions outside the top ten. The
third component is a penalty applied if the agent completes the race without using
two different tire compounds. In this case (i.e., SChange,d = 0), a penalty of 1000 sec-
onds is subtracted and no points or position terms are added. This ensures that the
agent accounts for mandatory tire compound change rule. Smaller penalties discour-
age stops that are rarely sensible in practice: 200 for stopping in two consecutive laps,
100 for stopping in laps 1 to 5, and 150 for stopping in the final lap. Choosing action
0 at the initial lap, when a starting compound must be selected, assigns the medium
compound and incurs a penalty of 1000.
    The inclusion of both race time and points reflects the trade-off between interme-
diate performance and final outcomes. While points determine the ultimate objective,
race time and the position term provide a more informative signal in situations where
positions result in identical points (e.g., positions 11 and 20). Reward normalization
is applied for PPO and Recurrent PPO to improve training stability and convergence.

4.5 State Transition Function
The state transition function in the Formula 1 simulation environment specifies how
the state evolves as a result of the agent’s action a ∈ {0} ∪ C r for driver d ∈ D. In
particular, it defines the update rules for each relevant state variable, as detailed below.

             STire,d ← STire,d · 1{a=0} + a · 1{a̸=0}
          STireLife,d ← (STireLife,d + 1{SSC +SVSC =0} ) · 1{a=0} + Wd,a · 1{a̸=0}
               SLap ← SLap + 1
          SLaps Left ← SLaps Left − 1
          SChange,d ← min{SChange,d + 1{a̸∈{0,STire,d }} , 1}
                SSC ← 4 · 1{SC begins} + max{SSC − 1, 0}
              SVSC ← 2 · 1{VSC begins} + max{SVSC − 1, 0}
         SPrevAction ← a
                        X
          SPosition,d ←    1{SGap,d +yd ≤SGap,d′ +yd′ }
                         d′ ∈D
              SGap,d ← SGap,d + yd − yagent



                                            15
where Wd,a is the age of the least-worn set of compound a among the sets of driver
d, including the one just taken off. The set ages SSetAge,c are updated accordingly.
This set of rules fully specifies the evolution of the state variables as a function of
the agent’s actions and race events, thereby defining the transition dynamics of the
simulation environment.

4.6 Stochastic Race Events
Besides the uncertainty incorporated in lap times and overtaking maneuvers, we also
model the stochastic occurrence of VSC and SC events. Specifically, for each lap, we
assume that a VSC or SC may be triggered with a certain probability. As noted in
Aguad and Thraves (2024), these probabilities depend on the circuit characteristics. In
particular, street circuits, which allow less margin for driver error, are more prone to
yellow flag events, whereas more open circuits tend to exhibit lower probabilities. For
each circuit, we estimate the probabilities of SC and VSC occurrences using empirical
frequencies from previous seasons, see Appendix F for more details.

4.7 Simulation Overview
Figure 2 provides an overview of the complete simulation procedure. The predictive
models are calibrated using historical data prior to the target Grand Prix, including
past races as well as free-practice and qualifying sessions. These models, together with
the reward function and rival behavior models, define the simulation environment used
to train the agent. A detailed description of the lap-by-lap race evolution is provided
in Algorithm G.1 in Appendix G.

                                                           Simulation environment
                                  RegLTC
   Current GP
    qualifying                                                    Lap time
                                                                 simulation
                                  RegLTYF


    Current GP
                                LogitOvertake                 Reward function            Agent
   free practice


                                 LogitStop
     Previous                                                 Rivals’ strategies
    race data
                                 CondLogit
                                 Compound



                 Data sources          Predictive models            Sim. components        Agent

Fig. 2 Overview of the data sources, predictive models, and simulation components used to construct
the environment.


   One agent is trained for each circuit, for a specific driver who starts from their
actual 2024 grid position. Each training episode is a full race of N laps in which lap
times, overtaking maneuvers, rivals’ decisions and retirements, and SC and VSC events


                                                  16
are sampled as described above, and the agent chooses its starting compound. For
each algorithm, several seeds are trained and one is selected on independent validation
races. The hyperparameters, network architectures and selection rule for each DRL
algorithm are reported in Appendix H.

5 Exact Optimization Benchmark
This section describes an exact formulation for the pit-stop optimization problem in
a deterministic single-driver setting. The formulation is based on quadratic mixed-
integer programming (QMIP) and obtains optimal solutions when tire performance
and pit stop time losses are known with certainty and no competition is present.
     We adopt two simplifying assumptions consistent with the DRL setting. First, each
tire compound c exhibits a linear degradation rate, so that the lap time penalty grows
linearly with tire usage. Under this assumption, the total lap time accumulated during
a stint of j laps with a set of compound c of age w equals (βc,1 + (w − 1/2)βc,2 ) j +
(βc,2 /2) j 2 . Second, pit stop time losses depend on track conditions: βPitIn + βPitOut
                                       ′       ′
under clear track conditions, and βPitIn    + βPitOut under a VSC or a SC. Although the
driver cannot anticipate future yellow flag events, it is assumed to be aware of the
current track status, denoted by (SVSC , SSC ) ∈ {(0, 0), (1, 0), (0, 1)}.
     We define a stint as a sequence of consecutive laps on the same tire compound.
Consider that there are n ≤ N laps remaining, the current tire compound in use is
c(0) with age w0 , and C (used) denotes the set of compounds used in previous laps. The
driver can complete at most K additional stints. Let w1c ≤ w2c ≤ . . . be the ages
of the sets of compound c left, of which at most K are considered, and let Jc index
them. The decision variables are x0 ≥ 0, the laps remaining in the current stint, and
xjc ≥ 0, the laps run on the j -th least-worn set of compound c, with binary indicator
yjc . Following Quiroga (2024), the problem is formulated as:
                                       
                              1                   βc(0) ,2 2
    min     βc(0) ,1 + w0 −       βc(0) ,2 x0 +           x0
                              2                     2
            X X                
                                           1
                                                  
                                                             βc,2 2
                                                                             
          +              βc,1 + wjc −          βc,2 xjc +        xjc + a yjc           (7a)
                                           2                  2
            c∈C r j∈Jc
                X X
     s.t. x0 +           xjc = n                                                       (7b)
                 c∈C r j∈Jc

          xjc ≥ yjc                                        ∀c ∈ C r , ∀j ∈ Jc          (7c)
          xjc ≤ n · yjc                                    ∀c ∈ C r , ∀j ∈ Jc          (7d)
              X        X
                                  yjc ≥ 1                     if C (used) = 1          (7e)
           c∈C r \C (used) j∈Jc
           X X
                        yjc ≤ K                                                        (7f)
           c∈C r j∈Jc

          yjc ≥ yj+1,c                                     ∀c ∈ C r , ∀j, j + 1 ∈ Jc   (7g)
          x0 , xjc ∈ Z≥0                                   ∀c ∈ C r , ∀j ∈ Jc          (7h)


                                             17
           yjc ∈ {0, 1}                                  ∀c ∈ C r , ∀j ∈ Jc            (7i)

                                                     ′        ′
where a1 = (βPitIn + βPitOut )1{SSC +SVSC =0} + (βPitIn    + βPitOut )1{SSC +SVSC >0} and
a = βPitIn + βPitOut denote the time loss incurred during a pit stop under current
and normal track conditions, respectively. The reduced loss a1 replaces a in one stop
if the driver stops in the current lap (x0 = 0), which is modeled with an auxiliary
binary variable; under SC, this is only possible in its first lap. The objective func-
tion (7a) minimizes the total remaining race time. Constraint (7b) ensures that the
number of laps assigned across all stints equals the remaining laps. Constraints (7c)
and (7d) enforce the logical relationship between the integer and binary decision vari-
ables. Constraint (7e) guarantees that at least two different tire compounds are used
throughout the race, as required by regulations. Since the order of the stints after the
current one does not affect the objective, they are indexed by tire set rather than by
position, which removes equivalent permutations: each set is fitted at most once, at
most K sets are fitted (Constraint (7f)), and the sets of a compound are fitted from
the least worn (Constraint (7g)). Two further constraints remove equivalent solutions
for the current stint: at the start of the race at least one lap is run on the starting
compound and, without a yellow flag, the least-worn set of the current compound is
not run for more laps than the current set will have completed.
    The formulation can be readily adapted to optimize pit-stop strategies from the
start of the race by setting the initial tire compound as an additional decision variable,
which starts on the least-worn set of that compound. In deterministic instances without
yellow flag events, the QMIP (7) is solved once at the start of the race to obtain the full
strategy. In stochastic instances where SC or VSC events may occur, the QMIP (7) is
solved at each lap, allowing the strategy to be updated in response to the current track
status. The QMIP does not refit a set taken off during the race. In the deterministic
instances of Section 6, an exact dynamic program over stints gives the same optimal
race time with and without refitting sets.

6 Validation of Learning-Based Pit-Stop Policies
Before using the learned policies as decision-support tools, we first evaluate their reli-
ability in settings of increasing complexity. This section is organized into three parts.
First, we present the calibration of the simulation environment, including the esti-
mated models for lap times, driver coefficients, and overtaking behavior. Second, we
benchmark the DRL methods against the optimal solution obtained via the QMIP
formulation in simplified settings without uncertainty or competition. Finally, we eval-
uate the performance of the DRL methods and the QMIP in realistic race scenarios
with a full grid of competitors, considering both fully simulated instances and instances
based on real race realizations.




                                            18
6.1 Calibration of the Simulation Environment
6.1.1 Clear-Track Lap-Time Model
The regression model in Equation (1) is estimated separately for each circuit, following
the outlier removal procedure described in Algorithm 1, which removes between 0.7%
and 3.0% of the laps in the circuits considered. Figure 3 shows the resulting tire
compound coefficients for the 2024 United States Grand Prix. With all laps, the soft
compound becomes faster as it ages. Removing outliers restores a positive degradation,
but the soft compound remains slower than the hard one when new and degrades more
slowly than the other two, since it was used in only five stints in 2021–2023. The joint
model of Appendix B recovers the expected pattern, in which softer compounds are
faster when new but degrade faster.

                                        With outliers                  Without outliers                   Joint model

                          2
Additional Lap Time [s]




                          1                                                                                                      Compound
                                                                                                                                    Hard
                                                                                                                                    Medium
                          0                                                                                                         Soft

                          1
                              0   5     10 15 20          25   0   5     10 15 20          25   0   5     10 15 20          25
                                      Tire Usage [laps]                Tire Usage [laps]                Tire Usage [laps]


Fig. 3 Tire performance at the 2024 United States GP. Left: Equation (1) estimated with all laps.
Center: Equation (1) estimated after removing outliers with Algorithm 1. Right: coefficients of the
joint model (Appendix B). Additional lap time is relative to a new hard tire.



    Table I.1 in Appendix I reports the full set of estimated coefficients before and
after removing outliers for the 2024 United States Grand Prix, and Figure J.1 in
Appendix J shows the removed lap times.
    The estimated coefficients of the yellow flag lap time model (RegLTYF) are
reported in Appendix D. A lap under VSC is about 34% slower than a clear-track
lap, and a pit stop under yellow flag conditions costs between 59% and 69% of the
clear-track pit-lane loss across the eight circuits.

6.1.2 Driver Coefficient Correction
Figure 4 shows the prediction accuracy of the driver coefficients with and without the
correction of Equation (2). Incorporating recent races and the practice and qualifying
sessions of the same weekend reduces the error in all circuits except the Qatar GP. An
example of the estimated coefficients of Equation (2) is shown in Appendix K.




                                                                                  19
                            3
                                                                               With correction




   Driver coefficient MSE
                                                                               Without correction

                            2



                            1



                            0


                                          se




                                        ish




                                           n

                                         an




                               ng n

                                           e



                                          ty

                                           s

                                          ar
                            i A in

                             Ja an




                                           i

                               Sp o



                             un n




                                         ch


                             ze an




                                         es




                                         bi
                                        m




                                       ga
                                       or
                                      ria




                                       ja
                                      ac




                                       ia




                                      Ci




                                      at
                                     ne
                                      ra




                                     ha
                                     at
                                     gi

                                    ut
                                     bi




                                      li
                                     ia



                                   an




                                    ai

                                   ap
                                    tr




                                  Ve
                                  on




                                  ga




                                 Ita
                                 ah




                                  Q
                                  el




                                 St
                                pa
                                 ra




                                 M




                                 D
                                 D



                                rb




                                  o
                                us



                               B




                               ic
                              M
                              B




                               s



                            bu
                             A




                             d



                           La
                            ex
                            Si

                           te
                           H




                          A
                        ud




                         A
                        M
                        ni
                      Sa




                      U
Fig. 4 MSE between predicted and ground-truth driver coefficients for each 2024 Grand Prix, where
the ground truth is estimated with Equation (1) using only that race. Without correction: Equation (1)
on the 2021–2023 editions of the same circuit; With correction: Equation (2), which adds the driver’s
three most recent 2024 races plus practice and qualifying sessions of the same weekend. Circuits
without dry editions in 2024 or before are omitted, as is the Australian GP, where the reference driver
retired on the fourth lap.


6.1.3 Overtaking Model
The logistic regression in Equation (4) is estimated using data from previous years.
Table L.1 in Appendix L reports the estimated coefficients for each circuit. In all cases,
the intercept is negative, indicating that closing the gap to the car ahead does not
necessarily lead to an overtake. The coefficient on the predicted time gap is negative
and significant at all circuits, indicating that smaller gaps are associated with higher
overtaking probabilities. The coefficients vary across circuits, reflecting differences in
overtaking opportunities: overtaking is more frequent at permanent circuits such as
Belgium or Bahrain, and less frequent at street circuits such as Singapore or Saudi
Arabia.

6.1.4 Rivals’ Strategy Models
The logistic regression for the pit-stop decision (LogitStop) and the conditional logistic
regression for tire compound selection (CondLogitCompound) are estimated using
historical race data as described in Section 4.3. For space considerations, the estimated
coefficients are reported in Appendix M.

6.2 Optimality Gap of DRL Methods in Simplified Settings
To measure how close each DRL method comes to the optimum, we evaluate the
agent on instances simple enough so that the optimal pit-stop strategy can be com-
puted. More specifically, we consider the agent for a specific GP under no competition
in a deterministic setting where tires’ performance and pit-stop additional lap time
are obtained from the regression in Equation (1). The agent has the tire sets of the
driver considered at the same circuit in Section 6.3. Then, the estimated coefficients
({βc,1 , βc,2 }c∈C , βPitIn and βPitOut ) are used as inputs to the QMIP in Equation (7)
of Section 5 to obtain the optimal solution. Each DRL method is trained with five


                                                  20
seeds for each circuit, and we report the seed with the smallest gap among those that
satisfy the two-compound rule.
    Figure 5 shows, for each GP, the optimal strategy, obtained with the QMIP, and
the agent’s strategy with all DRL methods. In general, the pit-stop solutions obtained
with all methods, except with TRPO, are very similar to the optimal solution. With
the selected seed, Recurrent PPO attains the optimal race time in seven of the eight
circuits and Double DQN in five. Since different strategies can have the same race
time, we also report the race time suboptimality gap in Table N.1 in Appendix N.
Averaged across circuits, the gap of the selected seed is below one second for Recurrent
PPO, Double DQN and PPO, about one and a half seconds for A2C, and larger for
TRPO. With the median over seeds, the gaps increase for all methods: they remain
below one second for Double DQN and Recurrent PPO, rise to between two and three
seconds for A2C and PPO, and exceed five seconds for TRPO.

                                    Bahrain Grand Prix                                Saudi Arabian Grand Prix                                           Miami Grand Prix                                       Hungarian Grand Prix
         QMIP Optimal     C2 (18)         C1 (20)          C1 (19)                       C4 (25)                        C3 (25)                      C4 (29)                       C3 (28)                 C5 (23)          C5 (23)              C4 (24)
        Recurrent PPO     C2 (18)         C1 (20)          C1 (19)                       C4 (25)                        C3 (25)                    C4 (26)                       C3 (31)                   C5 (23)          C5 (23)              C4 (24)
                  PPO
Model




                          C2 (19)          C1 (19)         C1 (19)                       C4 (25)                        C3 (25)                         C4 (35)                       C3 (22)             C5 (19)          C5 (27)               C4 (24)
                TRPO      C2 (18)             C1 (26)          C1 (13)             C2 (15)                        C3 (35)                             C2 (32)                       C3 (25)                     C3 (35)                     C4 (35)
                  A2C     C2 (19)          C1 (20)          C1 (18)                           C4 (34)                        C2 (16)             C4 (22)                       C3 (35)                     C5 (23)          C5 (24)              C4 (23)
          Double DQN      C2 (18)         C1 (19)          C1 (20)                       C4 (25)                        C3 (25)                        C4 (33)                       C3 (24)               C5 (23)          C5 (23)              C4 (24)
                                    Belgian Grand Prix                                       Dutch Grand Prix                                        Singapore Grand Prix                                     United States Grand Prix
         QMIP Optimal C4 (14)            C4 (14)           C2 (16)                 C3 (23)              C3 (23)              C2 (26)               C5 (30)                       C4 (32)                  C4 (18)           C3 (19)              C3 (19)
        Recurrent PPO C4 (14)            C4 (14)           C2 (16)                 C3 (23)              C3 (23)              C2 (26)               C5 (30)                       C4 (32)                  C4 (18)           C3 (19)              C3 (19)
                  PPO C4 (14)
Model




                                         C4 (14)           C2 (16)                       C1 (37)                         C2 (35)                   C5 (31)                       C4 (31)                   C4 (19)           C3 (20)              C3 (17)
                TRPO C3 (14)               C2 (17)           C2 (13)                    C1 (35)                         C2 (37)                     C3 (32)                       C4 (30)                       C2 (28)                     C3 (28)
                  A2C    C4 (15)          C4 (14)           C3 (15)                      C1 (37)                         C2 (35)                   C3 (31)                       C4 (31)                  C4 (17)          C3 (19)              C3 (20)
          Double DQN     C4 (15)          C4 (14)           C3 (15)                C3 (23)              C3 (23)              C2 (26)               C5 (30)                       C4 (32)                   C4 (19)          C3 (18)              C3 (19)
                     0.0     0.2        0.4          0.6   0.8           1.0 0.0       0.2         0.4            0.6        0.8       1.0 0.0     0.2            0.4      0.6         0.8      1.0 0.0        0.2        0.4         0.6       0.8         1.0
                                     Normalized Laps                                          Normalized Laps                                             Normalized Laps                                            Normalized Laps
                                                                                        QMIP Optimal                         Hard            Medium                     Soft



Fig. 5 Pit-stop strategies for five DRL models and the optimal solution, in a deterministic setting
with no competition.



6.3 Benchmarking DRL and QMIP under Competition
This section analyzes the performance of the DRL methods and the QMIP on eight
circuits of the 2024 season, considering that the agent competes in a full grid of twenty
drivers. For each GP, we consider a specific driver starting between sixth and thirteenth
on the grid, so that there is room for both improvement and deterioration in the final
result. Once the agent has been trained for a particular GP in a simulator calibrated
with data from previous races, using the seed selected on validation races (Figure H.1
in Appendix H shows all seeds), we evaluate its performance over 500 simulated races
under two settings: one in which rivals’ decisions and yellow flag events are randomly
generated (as described in Sections 4.3 and 4.6, respectively), and one in which they
are taken from the actual 2024 race, including the age of the set fitted in each stint. In
both settings, rivals that retired in the actual race retire on the same lap (Table O.1
in Appendix O). The QMIP uses the same tire coefficients as the DRL methods,
estimated with 2021–2023 data, and is re-optimized at each lap given the current track
status. In both settings, the clear-track lap times of the evaluation races are simulated
with tire coefficients re-estimated with the 2021–2024 races, so the agents and the
QMIP are evaluated in a simulator that differs from the one used to train the agents.


                                                                                                                              21
  6.3.1 Fully Simulated Race Scenarios
  Figure 6 shows the distribution of final positions across 500 simulations for each solu-
  tion method and circuit in the 2024 season. In terms of the median, PPO and Recurrent
  PPO are never worse than the QMIP and are better in two and three circuits, respec-
  tively. The dispersion of final positions is similar across methods. Mean final positions
  with 95% confidence intervals are reported in the top part of Table P.1 in Appendix P.
  Averaged over the eight circuits, PPO and Recurrent PPO attain the best mean final
  positions, with no appreciable difference between them, improving on the QMIP by
  0.33 and 0.28 positions, respectively, followed by the QMIP, then Double DQN and
  A2C, and finally TRPO.

                              Bahrain GP (ALO)                   Saudi Arabian GP (NOR)                              Miami GP (OCO)                    Hungarian GP (TSU)
                  2
                  4
                  6
Final Position




                  8
                 10
                 12
                 14
                 16
                 18
                 20
                              Belgian GP (GAS)                         Dutch GP (STR)                           Singapore GP (HUL)                    United States GP (MAG)
                  2
                  4
                  6
Final Position




                  8
                 10
                 12
                 14
                 16
                 18
                 20
                      DQN   A2C   TRPO   PPO   RPPO QMIP   DQN   A2C     TRPO   PPO    RPPO QMIP      DQN      A2C     TRPO   PPO   RPPO QMIP   DQN   A2C   TRPO   PPO   RPPO QMIP
                                                                    Actual Starting Position       Actual Final Position       Mean



  Fig. 6 Distribution of final positions over 500 fully simulated races per circuit, 2024 season.



  6.3.2 Real Race Realizations
  Figure 7 shows the distribution of final positions for each solution method under
  real race scenarios for the 2024 season. Compared to the fully simulated setting, the
  distributions are somewhat narrower on average, although not in every circuit, given
  that rivals’ decisions and yellow flag events are fixed to those observed in the actual
  race. From the bottom part of Table P.1 in Appendix P, we observe that PPO and A2C
  obtain the best average final positions, 0.49 and 0.44 positions ahead of the QMIP,
  followed by Recurrent PPO and the QMIP, and finally TRPO and Double DQN.
  As a reference, the box labeled “Replay” in Figure 7 reproduces the driver’s actual
  2024 starting compound and pit stops in the same simulated races. Averaged over the
  eight circuits, every method except Double DQN improves on the final position of this
  replay, by 0.66 positions for PPO and 0.61 for A2C. The replay, however, outperforms
  every method in the Belgian GP. The replay also provides a check of the simulator: the
  driver’s actual final position (dashed line) lies within the box of the replayed positions
  in six of the eight races, and within their central 90% interval in all of them. On
  average, however, the replay places the driver 0.94 positions ahead of the actual final
  position, which is why the methods are compared with the replay rather than with
  the actual final position.


                                                                                               22
                               Bahrain GP (ALO)                 Saudi Arabian GP (NOR)                         Miami GP (OCO)                 Hungarian GP (TSU)
                  2
                  4
                  6
Final Position
                  8
                 10
                 12
                 14
                 16
                 18
                 20
                               Belgian GP (GAS)                     Dutch GP (STR)                          Singapore GP (HUL)               United States GP (MAG)
                  2
                  4
                  6
Final Position




                  8
                 10
                 12
                 14
                 16
                 18
                 20
                      Replay DQN A2C TRPO PPO RPPO QMIP   Replay DQN A2C TRPO PPO RPPO QMIP        Replay DQN A2C TRPO PPO RPPO QMIP   Replay DQN A2C TRPO PPO RPPO QMIP
                                                                   Actual Starting Position    Actual Final Position     Mean



  Fig. 7 Distribution of final positions over 500 simulations per circuit with rivals’ decisions and yellow
  flags fixed to those of the actual 2024 race. The leftmost box, “Replay”, reproduces the driver’s actual
  2024 starting compound and pit stops.


      Across the eight circuits, PPO and Recurrent PPO are the only methods that
  improve on the QMIP in both settings, PPO by a larger margin. The differences are
  statistically significant (Table P.1). These margins are per race: half a position in each
  of the 24 races of a season adds up to twelve positions. In the 2024 Constructors’
  Championship, Alpine finished sixth, seven points ahead of Haas (Formula 1 2024),
  and in 2023 sixth place was worth an estimated 8 million dollars more in prize money
  than seventh (Hardy 2023). We therefore adopt PPO for the look-ahead analysis,
  whose rollouts sample yellow flag events, the same uncertainty under which the agent
  was trained.

  7 AI-Assisted Look-Ahead Decision Support
  While the previous sections evaluate decision policies in terms of their average perfor-
  mance over many races, in practice a race strategist must make a single, irreversible
  choice on each lap, with limited time for deliberation. In this setting, a point rec-
  ommendation from the DRL agent, such as “pit for medium tires now”, offers little
  visibility into the underlying trade-offs, into how confident the policy is in that action,
  or into what would have happened under alternative choices. For example, if the race
  engineer believes that the best action is to “continue on track” rather than stop-
  ping for medium tires, it would be useful to visualize and compare the race outcomes
  implied by the DRL recommendation and by the engineer’s own preferred action. We
  therefore propose a visualization tool that turns the trained DRL policy into a for-
  ward look-ahead simulator over alternative actions, providing the strategist with an
  interpretable view of the distribution of possible outcomes under each available action.
       For a fixed race, lap n, and driver, the procedure is as follows. For each candidate
  action a ∈ {Hard, Medium, Soft, No pit} available at lap n, we run M Monte Carlo
  simulations in which the action at lap n is forced to a and the actions in laps n +
  1, . . . , N are those that the trained PPO policy π would take, that is, its most likely
  action, excluding stops for the same compound before the two-compound rule is met.


                                                                                              23
Each rollout draws independent realizations of the stochastic race events described in
Section 4.6 (yellow flag occurrences, lap time noise, and overtakes), as well as of the
rivals’ pit stop decisions through the predictive model of Section 4.3. The final position
and championship points of each rollout give an empirical distribution of outcomes for
each action at lap n. The state sn is obtained by replaying the actual 2024 race up
to lap n, with rivals’ decisions and yellow flags fixed to those observed and the driver
following π . A yellow flag period already active at lap n keeps its actual duration,
and later events are sampled. Since the policy is followed deterministically, the spread
of outcomes reflects only race uncertainty and not randomness in the policy’s own
actions. The procedure is summarized in Algorithm 2. It is a one-step rollout with the
PPO policy as the base policy (Bertsekas et al. 1997).

Algorithm 2 Look-ahead rollouts for decision support visualization
Require: Trained policy π , current race state sn , candidate actions {0} ∪ C r , number
    of simulations M , set of feasible actions A(s)
                                    r
 1: for each action a ∈ {0} ∪ C do
 2:     for m = 1, . . . , M do
 3:        Set an ← a
 4:        Sample stochastic race events and rivals’ actions; update state sn+1
 5:        for n′ = n + 1, . . . , N do
 6:            an′ ← arg maxa′ ∈A(sn′ ) π (a′ | sn′ )
 7:            Sample stochastic race events and rivals’ actions
 8:            Update state sn′ +1
                                      (a)
 9:        Record final outcome ym (final position and championship points)
                                          (a) M                     r
10: return Empirical distributions {ym }m=1 for each a ∈ {0} ∪ C



     Figure 8 illustrates the resulting visualization for a representative decision point:
lap n = 7 of the 2024 Saudi Arabian Grand Prix (N = 50 laps), in a race driven by the
PPO policy from Lando Norris’s starting position. The policy started on soft tires and
is running in position 6, with seven laps of use on them, on the lap in which a safety
car is deployed. The DRL policy recommends switching to medium tires, which attains
the best average final position (4.18) and the highest average points (12.13)3 . Fitting
hard tires comes closest, with 0.54 ± 0.33 fewer points, so the strategist may prefer
it at a small expected cost on the basis of information not encoded in the simulator,
such as weather forecasts, mechanical concerns, or tactical instructions from the team
principal. Staying on track loses 2.23 ± 0.46 points. A stop under the safety car costs
less time than under green flag conditions and is only possible on the first lap of the
period (Appendix G), so if the driver stays out, the policy itself postpones the stop
to the second half of the race in about 70% of the rollouts. Fitting soft tires again
costs about as much (2.05 ± 0.40 fewer points), because a second soft stint would
still require a later stop on the medium or hard compound. Hard and medium tires
complete the race with the stop at lap 7, whereas fitting softs again or staying on track

 3
     Only drivers finishing in the top ten positions receive championship points.



                                                     24
lead to a further stop (see Figure Q.1 in Appendix Q). The strategist can thus tell
near-equivalent options from clearly dominated ones. The actual race differs: Norris
started on medium tires and stayed out under the safety car, and the policy would
have recommended a stop for soft tires at that lap (Figure R.1 in Appendix R).

                                                     Hard (C2)                                           Medium (C3) DRL recommendation
                           0.3
 Fraction of simulations




                                                                     Average position = 4.40                                        Average position = 4.18
                                                                     Average points = 11.58                                         Average points = 12.13
                                                               DRL wins head-to-head = 55%
                           0.2                                  points vs rec. = -0.54 ± 0.33

                           0.1

                           0.0
                                                      Soft (C4)                                                      Stay out
                           0.3
 Fraction of simulations




                                                                     Average position = 5.09                                        Average position = 5.18
                                                                     Average points = 10.08                                           Average points = 9.89
                                                               DRL wins head-to-head = 65%                                    DRL wins head-to-head = 66%
                           0.2                                  points vs rec. = -2.05 ± 0.40                                  points vs rec. = -2.23 ± 0.46

                           0.1

                           0.0
                                 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20             1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
                                                    Final position                                                 Final position

Fig. 8 Final position over M = 500 rollouts of each candidate action at lap 7 of the 2024 Saudi
Arabian Grand Prix, with the PPO policy driving in place of Lando Norris. Head-to-head wins and
∆ points compare paired rollouts with the recommended action (±2 standard errors, SE).



    Figure 9 shows the average championship points of each candidate action at every
lap of the race, with a band of ±2 SE. The “stay out” action defers to the policy from
lap n + 1 onward, so it already includes the stop that the policy itself would make: at
each lap the comparison is between stopping now and letting the policy choose when
to stop. The top strip reports the action recommended by the policy at each lap.
    During the first six laps, pitting for any compound earns fewer expected points than
staying on track, since the driver would abandon the initial soft-tire stint prematurely;
consistent with this, the DRL policy recommends “no pit” throughout the opening
phase. On lap 7, when the safety car is deployed, pitting for medium tires becomes
preferable to staying on track, with hard tires close behind, and this is the lap in which
the policy prescribes its stop. On laps 8 and 9 the four actions coincide, since no stop
is possible on them. From lap 10 onward any further stop would be a second one, and
staying on track remains the preferred continuation over the rest of the race.




                                                                                           25
  DRL action


                     12

                     10




    Average points
                      8

                      6

                      4

                      2

                          0    10                       20                      30                 40      50
                                                             Current lap

                              Hard (C2)   Medium (C3)        Soft (C4)     Stay out   Safety car   ±2 SE

Fig. 9 Average championship points by lap for each candidate action over M = 500 rollouts. 2024
Saudi Arabian Grand Prix, PPO policy driving in place of Lando Norris.


    The look-ahead can also be applied retrospectively to review the decisions taken in
2024. For every lap n of the eight races, the state sn replays the driver’s actual starting
compound and pit stops up to lap n − 1, and the recommended action is compared
with the actual one through the paired difference in points over the M = 500 rollouts.
Since the actual starting compound often differs from the one the policy would choose,
the analysis uses the PPO policy further trained with a randomly drawn starting
compound (Appendix R). The recommendation coincides with the actual decision in
94% of the laps, most of them laps in which neither stops. Of the 28 laps where the
two differ, the difference exceeds two standard errors in 12, 7 of them in favor of the
recommendation (mean difference of 0.73 points) and 5 in favor of the actual decision
(0.23 points) (Figure R.1 in Appendix R).
    The look-ahead evaluates all four actions, so it can be used to check the recommen-
dation. Figure 10 shows the laps of the Bahrain Grand Prix where the recommendation
for Alonso differs from his actual decision, together with the best of the four actions at
each of them. At lap 15 Alonso stopped and the policy recommends staying out, but
the rollouts show no clear difference between the two. Alonso’s next stop was at lap
41, whereas from lap 35 on the policy recommends stopping for hard tires. At laps 35
and 36 the rollouts favor staying out, at laps 37 and 38 they show no clear difference,
and at laps 39 and 40 they favor the recommendation, although at lap 40 medium
tires would be even better. The tire sets available at each decision point are reported
in Table E.1 of Appendix E.
    The rankings of the four actions inherit the biases of the policy used to roll out the
remaining laps: where it is suboptimal, they may be distorted. PPO, one of the best-
performing methods in our evaluation, mitigates this concern but does not eliminate
it. Computation times, including those of the look-ahead, are reported in Appendix S.
    The trained policy is used as a simulator rather than as an autonomous agent: the
strategist sees the outcomes of each action and decides how to combine them with
information the model does not have.




                                                             26
                                                                        DRL actual           Best of the four actual
 Actual      14                      26                        17
 Lap 15       16                    20                    21            No pit: +0.1 ± 0.3   Medium: -0.2 ± 0.2
 Lap 35      14                20                        23             Hard: -0.2 ± 0.2*    No pit: 0.0 ± 0.0
 Lap 36      14                21                        22             Hard: -0.3 ± 0.2*    No pit: 0.0 ± 0.0
 Lap 37      14                 22                        21            Hard: 0.0 ± 0.2      Same as DRL
 Lap 38      14                 23                        20            Hard: +0.1 ± 0.1     Same as DRL
 Lap 39      14                     24                        19        Hard: +0.6 ± 0.2*    Same as DRL
 Lap 40      14                     25                        18        Hard: +0.6 ± 0.2*    Medium: +0.8 ± 0.2*
                  10    20                30      40               50
                                         Lap
                        Hard             Medium   Soft


Fig. 10 Actual 2024 tire stints of Alonso in the Bahrain Grand Prix and stints implied by the DRL
recommendation at every lap where it differs from the actual decision. Each lower bar replays the
race up to the lap marked by the triangle and shows one representative continuation under the PPO
policy, without further yellow flags. On the right, the mean paired difference in points against the
actual decision for the recommended action and for the best of the four actions, ±2 SE over M = 500
rollouts with simulated yellow flags; positive values favor the recommended action (or the best of the
four) over the actual decision, and ∗ marks differences larger than 2 SE. The best action is selected
with a separate set of 500 rollouts, so its difference is not biased upward by the selection.


8 Conclusions
This paper studied Formula 1 pit-stop strategy as a sequential decision problem under
uncertainty and competition, with the aim of supporting rather than replacing human
strategists. We trained five DRL methods in a race simulation environment calibrated
with historical data, which models lap times, drivers’ recent performance, overtaking,
rivals’ pit-stop decisions, and yellow flag events, and benchmarked them against a
QMIP formulation that is optimal in deterministic single-driver settings, where all
DRL methods except TRPO achieve near-optimal performance.
    With a full grid of competitors, PPO and Recurrent PPO attain the best average
final positions in fully simulated races, and A2C and PPO when races are replayed
with the rivals’ decisions and yellow flags observed in 2024. PPO and Recurrent PPO
are the only methods that significantly improve on the QMIP, on average over the eight
circuits, in both settings, PPO by 0.33 and 0.49 positions in each setting and Recurrent
PPO by less, while the QMIP, which cannot anticipate yellow flag events, remains
competitive with the other DRL methods. TRPO is among the weakest methods in
every setting considered, so the choice of algorithm still matters.
    We then used the trained PPO policy as a look-ahead simulator that reports the
distribution of final positions and championship points under each candidate action.
In an illustrative case from the 2024 Saudi Arabian Grand Prix, on the lap in which
a safety car is deployed, it shows that stopping for medium or hard tires is preferable
to both staying out and a second soft-tire stint, and it identifies the laps at which
deviating from the policy is costly. Applied retrospectively to eight 2024 races, the
look-ahead identifies the laps where the actual decision, the recommendation, or a
third action was preferable, so it can be used to check the recommendation itself. A
strategist can weigh the recommendation against information the model lacks.


                                                         27
    Model parameters are estimated from pre-race information only; with live data, the
QMIP could be re-solved with updated parameters during the race, whereas the DRL
policies would need retraining. Rivals follow data-driven behavioral models rather than
responding strategically to the agent, a limitation that multi-agent formulations could
address, also allowing for coordination between teammates. The tire sets available at
the start of the race are inferred from the sets used in each session and the 2024
Sporting Regulations, since the returned sets are not reported, so the availability of
tires at each decision point is approximate. Finally, evaluating the look-ahead tool
with practicing strategists would show how it affects their reliance on the policy and
the quality of their decisions.
Acknowledgements. This work was supported by the Agencia Nacional de Inves-
tigación y Desarrollo (ANID), Fondecyt Iniciación 11241531. Powered@NLHPC: This
research was partially supported by the supercomputing infrastructure of the NLHPC
(ECM-02).
Use of AI tools. The authors used Claude (Anthropic) to assist with code develop-
ment, data analysis and drafting of parts of the text. The authors reviewed all outputs
and take full responsibility for the content of this article.
Statements and Declarations. Funding. This work was funded by the Agencia
Nacional de Investigación y Desarrollo (ANID), Fondecyt Iniciación 11241531.
Competing interests. The authors declare no competing interests.
Ethics approval and consent to participate. Not applicable.
Consent for publication. Not applicable.
Data availability. Race data were obtained from the public Formula 1 timing feeds
through FastF1 (Schaefer 2024) and OpenF1 (2026). The processed data are available
at Méndez and Thraves (2026).
Materials availability. Not applicable.
Code availability. The code and trained models are available at Méndez and Thraves
(2026).
Author contribution. F.M. contributed to data curation, formal analysis, investi-
gation, methodology, software, visualization, and writing (review and editing). C.T.
contributed to conceptualization, formal analysis, funding acquisition, methodology,
software, supervision, and writing (original draft).


References
Abbas, A.N., Amazu, C.W., Mietkiewicz, J., Briwa, H., Perez, A.A., Baldissone, G.,
 Demichela, M., Chasparis, G.C., Kelleher, J.D., Leva, M.C.: Analyzing operator
 states and the impact of AI-enhanced decision support in control rooms: a human-
 in-the-loop specialized reinforcement learning framework for intervention strategies.
 International Journal of Human–Computer Interaction 41(12), 7218–7252 (2025)

Aguad, F., Thraves, C.: Optimizing pit stop strategies in Formula 1 with dynamic
 programming and game theory. European Journal of Operational Research (2024)
 https://doi.org/10.1016/j.ejor.2024.07.011


                                          28
Boettinger, M., Klotz, D.: Mastering Nordschleife: A comprehensive race simulation
  for AI strategy decision-making in motorsports (2023)

Bekker, J., Lotz, W.: Planning Formula One race strategies using discrete-event sim-
  ulation. Journal of the Operational Research Society 60 (2009) https://doi.org/10.
  1057/palgrave.jors.2602626

Bertsekas, D.P., Tsitsiklis, J.N., Wu, C.: Rollout algorithms for combinatorial opti-
  mization. Journal of Heuristics 3(3), 245–262 (1997) https://doi.org/10.1023/A:
  1009635226865

Choo, C.L.W.: Real-time decision making in motorsports: analytics for improving
  professional car race strategy. Master’s thesis, Massachusetts Institute of Technology
  (2015). https://dspace.mit.edu/handle/1721.1/100310

Carrasco Heine, O.F., Thraves, C.: On the optimization of pit stop strategies via
  dynamic programming. Central European Journal of Operations Research 31(1),
  239–268 (2023) https://doi.org/10.1007/s10100-022-00806-4

Clausen, J., Larsen, A., Larsen, J., Rezanova, N.J.: Disruption management in the
  airline industry—concepts, models and methods. Computers & Operations Research
  37(5), 809–821 (2010)

Dehaybe, H., Catanzaro, D., Chevalier, P.: Deep reinforcement learning for inven-
  tory optimization with non-stationary uncertain demand. European Journal of
  Operational Research 314(2), 433–445 (2024) https://doi.org/10.1016/j.ejor.2023.
  10.007

Evans, B.D., Jordaan, H.W., Engelbrecht, H.A.: Safe reinforcement learning for high-
  speed autonomous racing. Cognitive Robotics 3, 107–126 (2023) https://doi.org/
  10.1016/j.cogr.2023.04.002

Fatima, S.S.W., Johrendt, J.: Deep-racing: An embedded deep neural network (ednn)
  model to predict the winning strategy in Formula One racing. International Jour-
  nal of Machine Learning and Computing 13(3), 97–103 (2023) https://doi.org/10.
  18178/ijml.2023.13.3.1135

Formula 1: 2024 Team Standings. https://www.formula1.com/en/results/2024/team.
  accessed November 2026 (2024)

Fieni, G., Wüthrich, J., Neumann, M.-P., Moradi, M.H., Onder, C.H.: Benchmarking
  Learning-Based Formula 1 Race Strategies (2025)

Fieni, G., Wüthrich, J., Neumann, M.-P., Onder, C.H.: Learning-based Multi-agent
  Race Strategies in Formula 1 (2026)

Gijsbrechts, J., Boute, R.N., Van Mieghem, J.A., Zhang, D.J.: Can deep reinforcement



                                          29
  learning improve inventory management? Performance on lost sales, dual-sourcing,
  and multi-echelon problems. Manufacturing & Service Operations Management
  24(3), 1349–1368 (2022) https://doi.org/10.1287/msom.2021.1064

Hardy, E.: F1 prize money: How much teams earned in the 2023
 season.         Motorsport.com,        https://www.motorsport.com/f1/news/
 f1-prize-money-how-teams-earned/10553551/. accessed November 2026 (2023)

Heilmeier, A., Graf, M., Betz, J., Lienkamp, M.: Application of Monte Carlo methods
  to consider probabilistic effects in a race simulation for circuit motorsport. Applied
  Sciences 10(12), 4229 (2020) https://doi.org/10.3390/app10124229

Heilmeier, A., Graf, M., Lienkamp, M.: A race simulation for strategy decisions in
  circuit motorsports. In: 2018 21st International Conference on Intelligent Trans-
  portation Systems (ITSC), pp. 2986–2993 (2018). https://doi.org/10.1109/ITSC.
  2018.8570012 . IEEE

Hoeppke, C.: Optimal control and reinforcement learning for Formula One lap simu-
 lation. PhD thesis, University of Oxford (2022). https://ora.ox.ac.uk/objects/uuid:
 491a5bb1-db1b-4cf6-b6f2-0ec06097ac9d

Heilmeier, A., Thomaser, A., Graf, M., Betz, J.: Virtual strategy engineer: Using
  artificial neural networks for making race strategy decisions in circuit motorsport.
  Applied Sciences 10(21), 7805 (2020) https://doi.org/10.3390/app10217805

Liu, X., Fotouhi, A., Auger, D.J.: Formula-E race strategy development using dis-
  tributed policy gradient reinforcement learning. Knowledge-Based Systems 216,
  106781 (2021) https://doi.org/10.1016/j.knosys.2021.106781

Leichtmann, B., Humer, C., Hinterreiter, A., Streit, M., Mara, M.: Effects of explain-
  able artificial intelligence on trust and human behavior in a high-risk decision task.
  Computers in Human Behavior 139, 107539 (2023)

Liu, R., Zhuang, W., Tong, F., Yin, G.: Learn to race: Sequential actor-critic rein-
  forcement learning for autonomous racing. In: 2023 IEEE International Automated
  Vehicle Validation Conference (IAVVC), pp. 1–6 (2023). https://doi.org/10.1109/
  IAVVC57316.2023.10328086 . IEEE

Marinaro, D.: S-MARL: An algorithm for single-to-multi-agent reinforcement learning:
 Case study: Formula 1 race strategies. Master’s thesis, KTH Royal Institute of
 Technology (2023)

Méndez Pérez, F.: Aprendizaje por refuerzo profundo para la optimización de estrate-
 gias de paradas en boxes en la Fórmula 1. Master’s thesis, Universidad de Chile
 (2025)

Méndez, F., Thraves, C.: Data and Code for: AI-Assisted Decision Support for Formula


                                          30
  1 Pit-Stop Strategy: Deep Reinforcement Learning and Mathematical Programming.
  Zenodo. [dataset] (2026). https://doi.org/10.5281/zenodo.24361704

O’Malley, C., Mars, P., Badesa, L., Strbac, G.: Reinforcement learning and mixed-
  integer programming for power plant scheduling in low carbon systems: Comparison
  and hybridisation. Applied Energy 349, 121659 (2023) https://doi.org/10.1016/j.
  apenergy.2023.121659

OpenF1: OpenF1 API: Real-time and historical Formula 1 data. https://openf1.org.
 accessed October 2026 (2026)

Osika, Z., Salazar, J.Z., Roijers, D.M., Oliehoek, F.A., Murukannaiah, P.K.: What lies
  beyond the Pareto front? a survey on decision-support methods for multi-objective
  optimization. arXiv preprint arXiv:2311.11288 (2023)

Pillac, V., Gendreau, M., Guéret, C., Medaglia, A.L.: A review of dynamic vehicle
  routing problems. European Journal of Operational Research 225(1), 1–11 (2013)

Phillips, A.: Building a race simulator. https://f1metrics.wordpress.com/2014/10/03/
  building-a-race-simulator/. accessed December, 2022 (2014)

Piccinotti, D., Likmeta, A., Brunello, N., Restelli, M.: Online planning for F1
  race strategy identification. In: Proceedings of the AAAI Conference on Artificial
  Intelligence, pp. 12624–12632 (2021)

Powell, W.B.: Perspectives of approximate dynamic programming. Annals of Opera-
  tions Research 241(1), 319–356 (2016)

Quiroga, M.: Optimization of pit stop strategies in Formula 1 racing: A data-driven
 approach. Master’s thesis, Universidad de Chile (2024)

Remonda, A., Krebs, S., Veas, E., Luzhnica, G., Kern, R.: Formula RL: Deep Rein-
  forcement Learning for Autonomous Racing using Telemetry Data (2021). https:
  //doi.org/10.48550/arXiv.2104.11106

Rebé Martı́n, J.: Toma de decisiones de estrategia durante las carreras de fórmula 1
  utilizando deep reinforcement learning. Master’s thesis, Universidad de Valladolid
  (2024)

Schaefer, P.: FastF1: Python package for Formula 1 data analysis. https://github.com/
  theOehrly/Fast-F1. accessed October 2026 (2024)

Schemmer, M., Hemmer, P., Kühl, N., Benz, C., Satzger, G.: Should I follow AI-
  based advice? measuring appropriate reliance in human-AI decision-making. arXiv
  preprint arXiv:2204.06916 (2022)

Schoeffer, J., Jakubik, J., Vössing, M., Kühl, N., Satzger, G.: AI reliance and decision
  quality: Fundamentals, interdependence, and the effects of interventions. Journal of


                                           31
  Artificial Intelligence Research 82, 471–501 (2025)

Sasikumar, A., Leema, A.A., Balakrishnan, P.: Data-driven pit stop decision support
  for Formula 1 using deep learning models. Frontiers in Artificial Intelligence 8 (2025)
  https://doi.org/10.3389/frai.2025.1673148

Sulsters, C.: Simulating Formula One race strategies. Research paper, msc business
  analytics, Vrije Universiteit Amsterdam (2018)

Thomas, D., Jiang, J., Kori, A., Russo, A., Winkler, S., Sale, S., McMillan, J.,
 Belardinelli, F., Rago, A.: Explainable reinforcement learning for Formula One
 race strategy. In: Proceedings of the 40th ACM/SIGAPP Symposium on Applied
 Computing, pp. 1090–1097 (2025). https://doi.org/10.1145/3672608.3707766

Tulabandhula, T., Rudin, C.: Tire changes, fresh air, and yellow flags: challenges in
  predictive analytics for professional racing. Big Data 2(2), 97–112 (2014) https:
  //doi.org/10.1089/big.2014.0018




                                           32
Appendix A              Rescaling of tire age in 2021
The tires used from 2022 onward have a different construction from those of 2021, so
the lap-time loss per lap of tire age differs between the two periods. We express the
2021 tire age in equivalent laps of 2022–2023 by multiplying it by a factor f , common
to all compounds and circuits, and estimate f in two ways.
    The first estimate uses lap times. We estimate Equation (1) for each circuit with
2021–2023 data, imposing that the 2021 tire age slope of each compound equals f
times its 2022–2023 slope, with f common to all circuits. Since fuel consumption and
track evolution shape the lap-time trend over the race differently across seasons, the
lap number terms are specific to each year. Using the 15 circuits with laps in both
periods (15,524 laps in 2021), we obtain f = 0.69, with a standard error of 0.069
clustered by race.
    The second estimate uses pit-stop decisions. We estimate a logit model of the
decision to pit on 2021–2023 laps, with indicators for SC and VSC and for having
used two compounds, compound-specific tire age slopes, the driver’s position, circuit
effects, a 2021 effect, and a function of the fraction of the race completed, specific to
2021 (a B-spline with five degrees of freedom). As in the rivals’ model (Section 4.3),
each SC or VSC period contributes one observation per driver, on its first lap, equal
to one if the driver stopped at any lap of the period. With the 2021 tire age multiplied
by f , the likelihood is maximized at f = 0.87, with a standard error of 0.074 clustered
by race.
    The two estimates are compatible (p = 0.08). Treating them as independent, since
they rely on different data, we combine them by a precision-weighted average, which
gives f = 0.78 (95% confidence interval 0.68–0.88).

Appendix B              Joint model for tire coefficients
Estimating Equation (1) separately for each circuit yields compound coefficients that
are often imprecise and frequently violate the expected ordering of compounds. This
occurs when a compound was used in few stints at a circuit, when it was not used at
all in 2021–2023, or when tire age is highly correlated with the lap number, as in the
Saudi Arabian GP, where pit stops were synchronized by a red flag and SC periods
in 2021, and by an SC period in 2022 and 2023. We therefore replace the compound
coefficients of Equation (1) by those of a model fitted jointly across circuits.
    Let ogc = βc,1 and sgc = βc,2 denote the intercept and degradation coefficients of
compound c at circuit g . The joint model is

                                          sgc = exp θg + λ′g bc ,
                                                               
                        ogc = λg ac ,

where ac and bc are compound profiles common to all circuits, with ac decreasing and bc
increasing in the softness of the compound, λg , λ′g > 0 are circuit-specific scale factors,
and θg is the degradation level of circuit g . The ordering is imposed by writing each
profile as a cumulative sum of positive steps between consecutive compounds; since
the 2021–2023 data are not informative about the step between C4 and C5, it is set
equal to the step between C3 and C4. The level θg is a random effect, θg ∼ N (µ, τ 2 ),


                                            33
with τ = 0.768 estimated by maximum likelihood, which shrinks the degradation level
of circuits with poorly identified slopes toward the common mean. The scale factors
are penalized toward one (log λg and log λ′g with standard deviation 0.3). The model is
fitted by generalized least squares to the per-circuit estimates of Equation (1) for the
21 circuits of the 2024 calendar with 2021–2023 data, each weighted by the inverse of
its estimated covariance matrix. Since the intercepts of Equation (1) are relative to a
reference compound, only their differences within each circuit enter the fit. Table B.1
reports the resulting coefficients for the eight circuits considered.


              Grand Prix       Compound      Stints 2021–2023    βc,1      βc,2
              Bahrain          C1                   33            0.000   0.1171
                               C2                   45           -0.206   0.1388
                               C3                  109           -0.415   0.1674
              Belgian          C2                   16           0.000    0.1574
                               C3                   60           -0.145   0.1780
                               C4                   33           -0.256   0.1919
              Dutch            C1                    0           0.000    0.0408
                               C2                   41           -0.188   0.0486
                               C3                   50           -0.378   0.0589
              Hungarian        C3                   75            0.000   0.0574
                               C4                   45           -0.178   0.0661
                               C5                    3           -0.356   0.0761
              Miami            C2                   39            0.000   0.0163
                               C3                   40           -0.123   0.0198
                               C4                    5           -0.217   0.0224
              Saudi Arabian    C2                   50           0.000    0.0111
                               C3                   62           -0.167   0.0161
                               C4                    5           -0.295   0.0202
              Singapore        C3                   18            0.000   0.0405
                               C4                   21           -0.204   0.0465
                               C5                    3           -0.409   0.0535
              United States    C2                   79            0.000   0.0782
                               C3                   86           -0.156   0.0885
                               C4                    5           -0.275   0.0955
            Table B.1 Tire coefficients of the joint model for each Grand Prix
            and compound. βc,1 is expressed relative to the hardest compound of
            the Grand Prix (seconds) and βc,2 is the lap-time increase per lap of
            tire age (seconds per lap). The number of stints run with each
            compound in 2021–2023 indicates how much each coefficient relies on
            the circuit’s own data.




                                             34
Appendix C               Specifications for updating driver
                         coefficients
We compare four specifications of Equation (2) that differ in how lap times are
expressed: (i) in seconds, with the pole lap time as a proxy for circuit length; (ii) as
differences to the reference driver; (iii) as differences to the session median; and (iv)
relative to lap time, as in Equation (2). Each specification is estimated using only the
races prior to the target race, and evaluated on every race of 2023 and 2024 against the
coefficient estimated with Equation (1) on that race alone. Two benchmarks without
correction are included: the driver’s coefficient in the previous race, and the coeffi-
cient estimated with Equation (1) on previous editions of the same circuit. Table C.1
reports the mean squared errors. All specifications substantially reduce the error rela-
tive to both benchmarks, and the relative specification attains the lowest error in both
seasons. Dropping XQ (the driver’s best qualifying lap time relative to that of the ref-
erence driver) changes the error by at most 0.02, whereas using fewer previous races
increases it, up to about 0.35 when none is available. Accordingly, XQ is dropped when
the qualifying session is missing or was run in wet conditions, and drivers with fewer
than three previous races use the available ones. Races in which a driver, or the ref-
erence driver, completes fewer than 15 clean laps are not used, either as observations
or as previous races.


                               Specification                     No correction
            Season     (i)     (ii)     (iii)    (iv)    Previous race    Same circuit
            2023      0.136   0.153    0.166    0.135        0.249            0.538
            2024      0.221   0.195    0.210    0.191        0.322            0.618
          Table C.1 Out-of-sample mean squared error, in (seconds per lap)2 , of
          the predicted driver coefficients for the races of 2023 (189 driver–race pairs)
          and 2024 (276), by specification of Equation (2) and for the two
          benchmarks without correction.




Appendix D               Lap times under yellow flag conditions
Equation (3) is estimated with a linear mixed model on lap times divided by L(g) ,
using the 2021–2023 laps that a driver ran entirely under VSC or SC (1117 laps from
34 races). Laps in which a car went through the pit lane without changing tires, as
when the field is led through the pit lane behind the SC, are excluded, also from the
excess times below. The reference lap time L(g) is the median clear-track lap without
                              (g)       (g)
pit stops at circuit g , and Gin and Gout are the median excess times of in-laps and
out-laps over the cars that did not pit in the same lap. We exclude the lap in which a
SC is deployed, since each car runs it only partially under SC, and pit stops made once
the field is queued, whose duration mixes the regrouping modeled in Algorithm G.1.



                                                35
The model includes a random effect common to all cars in each race lap and the circuit
effect ug under SC.
    Table D.1 reports the common coefficients. A lap under VSC is about 34% slower
than a clear-track lap, and a lap under SC about 42% slower before the circuit effect.
The pace of the first SC lap, before the field is queued, does not differ significantly
(1.432, s.e. 0.027), so a single SC coefficient is used. The pit-lane factors κin and
κout are common to SC and VSC. Table D.2 reports the circuit-level quantities and
the resulting lap times and pit-lane losses. Across the eight circuits, a pit stop under
yellow flag conditions costs between 59% and 69% of the clear-track loss, which saves
between 6.3 and 12.3 seconds.

                              Coefficient       Estimate     Std. Err.
                              ρVSC                1.337       (0.023)
                              ρSC                 1.420       (0.026)
                              κin                 0.366       (0.227)
                              κout                0.702       (0.092)
                              Std. dev. of ug     0.087
                            Table D.1 Common coefficients of the
                            yellow flag lap time model (Equation (3)),
                            estimated with 2021–2023 data.




                               (g)      (g)
 Grand Prix         L(g)     Gin      Gout      ug    VSC lap SC lap Pit (YF) Pit (clear)
 Bahrain       98.315 3.227 20.841 -0.129                 131.5    127.0       15.8        24.1
 Saudi Arabian 95.170 3.347 19.085 0.033                  127.3    138.3       14.6        22.4
 Miami          92.768 5.034 14.860 -0.076                124.1    124.7       12.3        19.9
 Hungarian      84.573 3.069 18.674 0.000                 113.1    120.1       14.2        21.7
 Belgian       112.776 5.122 13.653 0.000                 150.8    160.2       11.5        18.8
 Dutch          76.390 3.681 18.703 -0.092                102.2    101.5       14.5        22.4
 Singapore     100.414 9.947 19.977 -0.023                134.3    140.4       17.7        29.9
 United States 102.338 0.678 19.619 -0.026                136.9    142.7       14.0        20.3
Table D.2 Circuit-level quantities of the yellow flag lap time model and resulting lap times and
                                                             (g)         (g)
pit-lane losses, in seconds. Pit (YF) is the pit-lane loss κin Gin + κout Gout and Pit (clear) is
  (g)     (g)
Gin + Gout . No SC laps remain in the estimation sample at the Hungarian and Belgian GPs in
2021–2023, so their circuit effect is set to zero.




Appendix E                 Tire Sets Available at the Start of the
                           Race
The tire sets used in each session of the 2024 weekends (practice, sprint qualifying,
sprint and qualifying) and their ages are taken from FastF1 and OpenF1 (https://


                                                36
openf1.org). Under Article 30.2 of the 2024 Sporting Regulations, a driver receives 13
dry sets in a regular weekend and returns two after each practice session and, if they
reach Q3, one soft set after qualifying; in sprint weekends, 12 sets are allocated and
one is returned after FP1, one after the sprint and three after qualifying. One hard
and one medium set, the race specifications at the eight circuits, cannot be returned.
Which set is returned is not reported; we assume that, among the sets not used later
in the weekend, teams return the one with the most laps, preferring soft sets. The
resulting inventory has 6.73 sets per driver on average, 55% of them new (counting
only push laps). In 2024, 17% of the race stints started on a used set (15% of the starts
and 19% of the stints after a pit stop), and 192 of these 196 stints match a set of the
inferred inventory. Table E.1 reports the sets available to each driver at the decision
points reviewed in Figure R.1, which bound the length of the stints shown there.

                                             Laps        On car           Sets available (age in laps)
 GP (driver)                   Lap           left        (age)    Hard         Medium         Soft
 Bahrain (Alonso)              15             43     C3 (15)      C1: 0, 0     C2: 0          C3: 1, 1
                               35–40 (39)     19     C1 (23)      C1: 0        C2: 0          C3: 1, 1, 16
 Saudi Arabian (Norris)        7              44     C3 (6)       C2: 0        C3: 0          C4: 1, 3, 3
                               29             22     C3 (25)      C2: 0        C3: 0          C4: 1, 3, 3
                               31–36 (34)     17     C3 (30)      C2: 0        C3: 0          C4: 1, 3, 3
 Miami (Ocon)                  22             36     C3 (21)      C2: 0        C3: 2, 2       C4: 1, 1, 1
 Hungarian (Tsunoda)           29             42     C4 (28)      C3: 0, 0     C4: –          C5: 1, 1, 2
 Belgian (Gasly)               9              36     C3 (8)       C2: 0, 0     C3: –          C4: 0, 0, 0, 0
                               25             20     C2 (15)      C2: 0        C3: 9          C4: 0, 0, 0, 0
                               26–28 (26)     19     C2 (16)      C2: 0        C3: 9          C4: 0, 0, 0, 0
 Dutch (Stroll)                30             43     C2 (29)      C1: 0        C2: –          C3: 1, 1, 1, 2
 Singapore (Hülkenberg)       29             34     C4 (28)      C3: 0        C4: –          C5: 1, 1, 1, 1
 United States (Magnussen)     3              54     C3 (2)       C2: 0        C3: 0, 2       C4: 1, 1, 1
                               17             40     C3 (13)      C2: 0        C3: 0, 2       C4: 1, 1, 1
                               36–37 (36)     21     C2 (18)      C2: –        C3: 0, 2, 14   C4: 1, 1, 1
Table E.1 Tire sets available to the driver at each decision point of Figure R.1, with the age in
laps of every set of each compound and of the set on the car. For a group of consecutive laps, the
lap of the largest difference is given in parentheses and the state refers to that lap. A pit stop fits
the least-worn set of the chosen compound. A dash means that no spare set of that compound is
left; the set taken off returns to the driver’s sets with its age, so the set on the car can always be
refitted, with the age it has at that lap. Ages follow Section 3: laps under SC, VSC or red flag, and
the non-push laps of earlier sessions, do not count.




Appendix F                 Safety Car and Virtual Safety Car
                           Event Data
Table F.1 reports, for each circuit, the estimated probability that at least one SC or at
least one VSC occurs during a race. In the simulation, the probability of an event in


                                                    37
each lap is 1 − (1 − P )1/N , where P is the probability in the table and N is the number
of laps of the race. The SC probability of the Saudi Arabian GP is capped at 0.70,
since a probability of one would imply a SC in every lap of the simulation. The last
two columns give the laps with SC or VSC conditions in the actual 2024 race, where
a dash means that none occurred; these laps are used when the yellow flag events are
taken from the real race.

                               Estimated Probability    Actual Laps (2024 GP)
               Grand Prix       SC         VSC           SC          VSC
               Bahrain         0.37        0.22           —           —
               Saudi Arabian   0.70        0.67          7–9          —
               Miami           0.50        0.50         28–32       22–23
               Hungarian       0.25        0.33           —           —
               Belgian         0.64        0.11           —           —
               Dutch           0.67        0.67          —            —
               Singapore       0.93        0.43           —           —
               United States   0.36        0.38          3–5          —
             Table F.1 Estimated probability of at least one SC or VSC event
             per race, taken from Aguad and Thraves (2024) except for Miami,
             which is not included there and is estimated from its 2022–2023
             races, and lap ranges during which SC or VSC conditions were active
             in the corresponding 2024 race.




Appendix G              Race Evolution
Algorithm G.1 describes the evolution of one lap of the simulation, given the state at
its beginning and the agent’s action.
    Three remarks complement Algorithm G.1. First, during a SC period the field is
regrouped progressively: gaps are halved on the second lap of the period and, from
the third lap on, drivers queue behind the leader at tSC gap = 1.5 s (the median gap
observed in real SC queues), with track positions frozen; pit stops are only possible on
the first lap of the period, when teams react to the deployment. This is a simplification,
since the pit lane remains open during the whole period; in practice, however, most
stops under a safety car are made on its first lap (about two thirds in the dry races
of 2021–2024), and in a sensitivity check that also allows the agent to stop on the
second lap, such a stop yields a similar expected outcome to one on the first lap, so
the recommendation to stop under the safety car in Figure 8 is unchanged. The same
restriction applies under VSC, to the agent and to the rivals: a stop is only possible on
the first lap of a VSC period. Second, the following gap of a car that fails to overtake
is not a constant: it is drawn as tmin gap + ε with tmin gap = 0.4 s and ε exponential
with mean 0.26 s, so that the mean following gap matches the 0.66 s observed for
cars that are faster than the car ahead but fail to pass it. A constant gap would keep
groups of cars at a fixed spacing. Third, a pit stop on the final lap is charged the full



                                             38
Algorithm G.1 System evolution for a lap
Require: Lap n, state at the beginning of the lap S , agent’s action
 1: ℓ ← number of consecutive laps (including n) with SSC ≥ 1; ℓ = 0 if SSC = 0
 2: Sample rivals’ pit-stop decisions using LogitStop (pit stops are only allowed on
    clear-track laps and on the first lap of an SC or VSC period; otherwise the agent’s
    pit action is a no-op)
 3: For rival drivers who stop, get the new tire compound with CondLogitCompound
 4: if SSC + SV SC = 0 then                                                    ▷ Clear track lap
 5:       Compute {ŷd }d∈D with RegLTC                   ▷ Preliminary lap times; each driver’s
    coefficient includes the prediction error drawn at the start of the race
 6: else                                                                 ▷ There is a SC or VSC
 7:       Compute {ŷd }d∈D with RegLTYF                  ▷ Preliminary lap times; the SC/VSC
    coefficient is used from the first lap of the period
 8: if n is the final lap and driver d pits then charge both PitIn and PitOut to ŷd ▷
    No out-lap exists after the final lap
 9: if SSC ≥ 1 and ℓ ≥ 3 then
10:       Queue the field behind the leader, with gaps of tSC gap between consecutive
    cars; positions are frozen; return                                          ▷ No overtaking
      (i)
11: d      ← driver in i-th position at the beginning of lap n
12: for h = 2 to 20 do
13:       d(h) ← driver in the hth position at the beginning of lap n
14:       for k = h to 2 do
15:           d(k−1) ← driver (partially) in the k − 1th position
                 (k,k−1)
16:           X∆2         ← time gap at the beginning of lap n between drivers d(k) and
    d(k−1)
                              (k,k−1)
17:           XPredGap ← X∆2            + ŷd(k) − ŷd(k−1)
18:           if SSC + SV SC = 0 then                                          ▷ Clear track lap
19:                Get τ ← LogitOvertake                                      ▷ Probability that
    d(k) overtakes d(k−1) , evaluated with the mean lap times, since the logit already
    contains their uncertainty
20:                Overtake ← Uniform(0, 1) < τ
21:           else                                                       ▷ There is a SC or VSC
22:                Overtake ← XPredGap < 0
23:           if Overtake then                                 ▷ Overtake is predicted to occur
                                                      (k,k−2)
24:                ŷd(k) ← max{ŷd(k) , ŷd(k−2) − X∆2       + tmin gap }
                                                    (k,k−1)
25:            ŷd(k−1) ← max{ŷd(k−1) , ŷd(k) + X∆2      + tmin gap }
                        (k)     (k−1)
26:            Swap d and d
27:        else                                                   ▷ Overtake does not occur
28:            ε ∼ Exp(0.26), with mean 0.26 s ▷ Following gap: tmin gap + ε seconds,
    resampled per pair and lap
                                                  (k,k−1)
29:            ŷd(k) ← max{ŷd(k) , ŷd(k−1) − X∆2       + tmin gap + ε}
30:            break
31: if SSC ≥ 1 and ℓ = 2 then
32:     Scale the gaps to the leader by 12 , after applying the lap times ▷ Progressive
    regrouping behind the SC

                                              39
pit-lane time (PitIn and PitOut) within that lap, since no out-lap exists; otherwise
such a stop would cost only the pit-entry component.




                                        40
Appendix H                Models Architecture and Seed
                          Selection
H.1     Hyperparameters
Tables H.1 and H.2 report the hyperparameters of the five DRL algorithms in the
simplified setting without competition and in the setting with a full grid of competitors,
respectively. The algorithms are those of Stable-Baselines3 and its contrib package
(TRPO and Recurrent PPO), and the parameters that are not listed take their default
values. Without competition, each configuration is trained with five seeds.

    Hyperparameter         Double DQN       A2C         TRPO          PPO         Recurrent PPO
                                    −4          −4           −3           −4
    Learning rate            1×10          3×10        1×10          3×10            5×10−4
    Discount factor (γ)                                   0.99
    LSTM layers × units           –           –            –             –            1 × 32
    Hidden layers           [64, 64, 64]   [64, 64]   [64, 64, 64] [64, 64, 64]      [32, 32]
    nsteps                      –            nl           nl           2nl             nl
    Batch size                2nl ne          –          nl ne        nl ne           nl ne
    Entropy coefficient         –           0.05           –          0.01            0.10
    GAE λ                       –           0.95         0.95         0.95            0.95
    Clip range                  –             –            –          0.20            0.30
    Update epochs               –            –             –           10              10
   Table H.1 Hyperparameters of each RL algorithm without competition. nl : laps per
   circuit; ne = 10: parallel environments. All use ReLU activation, reward normalization and
   5M timesteps. Double DQN uses a replay buffer of 3 × 106 ; A2C uses RMSProp with
   normalized advantages; PPO uses target KL = 0.015; the LSTM of Recurrent PPO is used
   by the actor only.




                                                41
   Hyperparameter           Double DQN         A2C        TRPO         PPO       Recurrent PPO
                 †                  −4             −4          −4          −4
   Learning rate               3×10          5×10        5×10        3×10            5×10−4
   Discount factor (γ)                                    0.995
   Reward normalization           No            No         No           Yes            Yes
   LSTM layers × units             –            –          –          –               1 × 64
   Hidden layers            [256, 256, 256] [256, 128] [256, 128] [256, 128]           [128]
   nsteps                         –             2nl         2nl         2nl            2nl
   Batch size                    256              –        2nl ne      2nl ne         2nl ne
   Entropy coefficient‡           –             0.01         –          0.05           0.05
   VF coefficient                 –             0.50         –          0.01           0.01
   GAE λ                          –             1.00        0.95        0.98           0.95
   Clip range                     –               –          –          0.20           0.25
   Update epochs                  –              –           –            3             4
   Target KL                      –              –          0.02          –              –
  Table H.2 Hyperparameters of each RL algorithm with competition. nl : laps per circuit;
  ne = 10: parallel environments. All use ReLU activation and 5M timesteps with early
  stopping (patience of 25 evaluations, 50 episodes each). Double DQN uses a replay buffer of
  1.5×106 , learning starts after 30,000 steps, exploration fraction 0.30 with ϵfinal = 0.02, and
  target network updates every 1,500 steps. † Double DQN anneals the learning rate linearly
  from 3×10−4 to 1×10−5 ; the other algorithms use a constant rate. ‡ With 0.02, PPO and
  Recurrent PPO collapsed their entropy early in training and kept stopping on the sixth lap
  of the Miami Grand Prix.




H.2     Seed Selection
With competition, each agent is trained with ten seeds, and each seed is evaluated
on 200 simulated races independent of those of Figure 6. A race is valid if the agent
makes one to four pit stops, the first after lap 5 unless a safety car or virtual safety
car has already been deployed, and, except on safety car or virtual safety car laps,
none with seven or fewer laps to go and none fewer than eight laps after the previous
stop. Among the seeds with at least 95% valid races and no race disqualified for not
using two compounds, the one with the best average final position is kept; if no seed
meets both conditions, the one with the most valid races is kept. Only TRPO needs
this fallback, in four of the eight circuits, where the selected seed reaches the share of
valid races but leaves up to 3.5% of them disqualified. Figure H.1 shows the mean final
position of every seed in these validation races. The ten seeds of PPO and Recurrent
PPO lie close together in every circuit. Double DQN and A2C vary more across seeds
in some circuits, and TRPO is the most sensitive, with seeds far from the rest in several
circuits. The agent evaluated in Section 6.3 is the selected seed, which by construction
is among the best of its method.




                                                42
                                     Bahrain GP                 Saudi Arabian GP                        Miami GP                    Hungarian GP

                                                                                          14                               10
      Mean final position
                            6
                                                         6
                                                                                          13                                9
                            5                            5
                                                                                          12                                8
                            4                            4
                                                                                          11                                7

                                     Belgian GP                     Dutch GP                         Singapore GP                  United States GP
                                                        20
                                                                                          12                               18
 Mean final position




                       10                               16
                                                                                          10                               15
                                                        12
                                                                                           8                               12
                            9                            8                                                                  9
                                                                                           6
                                DQN A2C TRPO PPO RPPO        DQN A2C TRPO PPO RPPO             DQN A2C TRPO PPO RPPO            DQN A2C TRPO PPO RPPO
                                                        Each dot is one of the 10 training seeds; the bar is the median.


Fig. H.1 Mean final position of the ten training seeds of each algorithm, by circuit, in the validation
races used for seed selection.


Appendix I                                         Estimated Coefficients for the
                                                   Clear-Track Lap Time Model
Table I.1 reports the estimated coefficients of Equation (1) for the 2024 United States
Grand Prix, estimated with the 2021–2023 clear-track laps, before and after removing
outliers, that is, laps at least 15 seconds slower than the median lap of their race (except
in-laps, out-laps and the first lap) and the observations excluded by Algorithm 1. In the
table, Interval behind and Interval front are e−X∆1 and e−X∆2 , FirstLap pos is X1pos ,
and TireLife is the effective tire age, with the 2021 laps rescaled as in Appendix A.
Removing 1.7% of the laps increases the coefficient of determination from 0.877 to
0.966 and roughly halves the standard errors. Some coefficients also take the expected
sign. For example, starting further back increases the first lap time, which holds only
after the removal of outliers. Similarly, the tire life coefficient of the softest compound
(C4) is negative before the removal and positive after, although it is estimated from
fewer than 30 laps and is not significant in either case. Even after removing outliers,
the degradation rate of C3 is slightly lower than that of the harder C2, which motivates
the joint model of Appendix B.




                                                                                     43
                                                Model
                           With outliers                Without outliers
 Variable                Coef.           Std. Err.      Coef.           Std. Err.
 Intercept           102.3083***          (0.191)    101.8442***         (0.089)
 DRS                  -0.3834***          (0.137)     -0.3765***         (0.064)
 FirstLap pos         -0.1156***          (0.030)      0.3717***         (0.061)
 Interval behind       0.4954***          (0.172)      0.6740***         (0.081)
 Interval front        1.8054***          (0.274)      1.9258***         (0.129)
 LapNumber            -0.0913***          (0.009)     -0.0664***         (0.004)
 LapNumber2            0.0006***          (0.000)      0.0001            (0.000)
 PitIn                 1.6267***          (0.155)      0.3997***         (0.075)
 PitOut               20.4048***          (0.162)     20.2851***         (0.079)
 C3 (ref. C2)         -0.2258*            (0.122)     -0.1544***         (0.057)
 C4 (ref. C2)          1.1898*            (0.672)      0.8043**          (0.332)
 Year 2022             0.3556***          (0.082)      0.4237***         (0.039)
 Year 2023            -0.0637             (0.082)     -0.0685*           (0.038)
 TireLife · C2         0.0611***          (0.008)      0.0857***         (0.004)
 TireLife · C3         0.0602***          (0.009)      0.0787***         (0.004)
 TireLife · C4        -0.1045             (0.123)      0.0398            (0.060)
 Albon                 1.9023***          (0.198)      1.7684***         (0.092)
 Alonso                1.3695***          (0.177)      1.3088***         (0.083)
 Bottas                1.3130***          (0.186)      1.2742***         (0.087)
 Gasly                 1.9389***          (0.188)      1.4930***         (0.088)
 Giovinazzi            1.9019***          (0.249)      1.9433***         (0.116)
 Hamilton              0.0843             (0.172)      0.1482*           (0.080)
 Hülkenberg           1.5815***          (0.242)      1.7902***         (0.113)
 Latifi                2.9836***          (0.199)      2.7591***         (0.093)
 Leclerc               0.6149***          (0.172)      0.5937***         (0.080)
 Magnussen             2.1983***          (0.197)      2.2395***         (0.092)
 Mazepin               4.6397***          (0.250)      4.3056***         (0.120)
 Norris                0.9059***          (0.173)      0.9570***         (0.080)
 Ocon                  2.7198***          (0.204)      2.1169***         (0.097)
 Pérez                0.4450**           (0.173)      0.4811***         (0.080)
 Piastri               3.5756***          (0.500)      1.0198***         (0.246)
 Räikkönen           1.9776***          (0.249)      1.8211***         (0.117)
 Ricciardo             1.7759***          (0.174)      1.7124***         (0.081)
 Russell               1.2953***          (0.173)      1.2940***         (0.080)
 Sainz                 0.6347***          (0.194)      0.6588***         (0.090)
 Sargeant              1.7842***          (0.244)      1.6352***         (0.114)
 Schumacher            2.7114***          (0.199)      2.6256***         (0.093)
 Stroll                1.5572***          (0.184)      1.6824***         (0.086)
 Tsunoda               1.6039***          (0.174)      1.6050***         (0.081)
 Vettel                1.8525***          (0.198)      1.7463***         (0.092)
 Zhou                  2.1083***          (0.199)      1.9340***         (0.093)
 Observations                    2812                           2764
 R2                              0.877                          0.966
Table I.1 Regression coefficients under clear-track conditions for the 2024
United States Grand Prix, estimated with 2021–2023 data. Left: estimated
with all data points; Right: estimated after removing outliers. The reference
driver is Verstappen. Notes: *** p < 0.01, ** p < 0.05, * p < 0.1.
                                         44
 Appendix J                        Outlier lap times of the United States
                                   GP
 Figure J.1 shows the clear-track lap times of the 2021–2023 United States GP used to
 estimate the 2024 coefficients, where outliers are marked with a different color. Most
 outliers are lap times considerably higher than those of other drivers, and many of
 them occur in the first lap, when cars are still very close. These laps include driver
 errors, minor collisions and other incidents that add time. Unusually fast laps do not
 deviate enough from the rest to be classified as outliers. Laps in which a car enters or
 leaves the pit lane are also much slower, but they are not outliers, since Equation (1)
 accounts for them through PitIn and PitOut.

                            2021                2022                         2023
                150
                                                                                    Non-outlier
                140                                                                 Outlier
Lap Times [s]




                130
                120
                110
                100
                      0   20       40    0    20       40          0       20       40
                          Lap Number          Lap Number                   Lap Number

 Fig. J.1 Clear-track lap times of the United States GP in 2021, 2022 and 2023. Laps removed by
 Algorithm 1 are shown in orange.




 Appendix K                        Correction of drivers’ estimated
                                   coefficients for Belgian GP 2024
 Table K.1 reports the coefficients of Equation (2) estimated with the races prior to
 the 2024 Belgian GP. Since its qualifying session was run in wet conditions, the spec-
 ification without XQ is used for this race; the full specification is shown for reference.
 The three previous races and the free practice sessions carry most of the weight, and
 all coefficients are statistically significant.




                                               45
                                    Full specification            Without XQ (used)
                Variable            Coef.       Std. Err.           Coef.       Std. Err.
                Intercept        0.0018***          (0.0004)      0.0016***         (0.0004)
                XPrev1            0.202***           (0.027)       0.213***          (0.029)
                XPrev2            0.213***           (0.027)       0.201***          (0.028)
                XPrev3            0.202***           (0.028)       0.224***          (0.029)
                XFP               0.275***           (0.027)       0.271***          (0.028)
                XQ                0.039***           (0.009)
                Observations                 929                            1022
                R2                          0.578                           0.516
               Table K.1 Coefficients of Equation (2) estimated with the races
               prior to the 2024 Belgian GP. The specification without XQ is the
               one used for this race. Notes: *** p < 0.01, ** p < 0.05, * p < 0.1.




Appendix L              Overtaking estimated coefficients
The overtaking logit is estimated per Grand Prix on 2021–2023 pairs of consecutive
cars with a predicted gap between −30 and 5 s, excluding laps 1 to 4 and laps with
SC, VSC or red flag. In the simulation the logit decides every battle under clear-track
conditions, whatever the gap; the fitted probability τ is used directly as the success
probability of an overtaking attempt (Algorithm G.1); no decision threshold is applied.
The last column of Table L.1 reports the empirical overtaking rate in the estimation
sample.


                        Estimated Coefficients           Training data [observations]          Overtake
                                                                                                 rate
      Grand Prix            γ0        γPredGap           Overtakes            Total
      Bahrain          -1.1439***    -1.8735***             235               1475              0.159
      Belgian          -0.7949***    -2.6221***             183                964              0.190
      Dutch            -1.9121***    -1.8383***             130               1551              0.084
      Hungarian        -1.6567***    -2.4366***             206               1969              0.105
      Miami            -0.8381***    -2.4429***             133               1302              0.102
      Saudi Arabian    -1.3699***    -1.5285***             110               1377              0.080
      Singapore        -1.9813***    -2.0974***              44                844              0.052
      United States    -0.6854***    -2.2913***             199               1641              0.121
    Table L.1 Overtake logistic regression coefficients for selected GPs, laps with overtake
    in training data, and empirical overtaking rate in the estimation sample. Notes: ***
    p < 0.01, ** p < 0.05, * p < 0.1.




   Figure L.1 shows the probability of overtaking implied by the coefficients of
Table L.1 as a function of the predicted gap XPredGap , where a negative gap means
that the trailing car is predicted to finish the lap ahead. At a predicted gap of zero,
the probability ranges from 12% (Singapore) to 34% (United States). The trailing car
must be predicted to finish ahead by between 0.3 and 1.0 s for the probability to reach
50%, and by about 3 s for it to exceed 95% at every circuit.


                                                    46
                                  1
                                                                               United States
                                                                               Belgian
                                 0.8                                           Miami

     Probability of overtaking
                                                                               Bahrain
                                                                               Saudi Arabian
                                 0.6
                                                                               Hungarian
                                                                               Dutch
                                 0.4                                           Singapore


                                 0.2


                                  0
                                   −3   −2        −1           0           1   2               3
                                                       Predicted gap (s)

Fig. L.1 Probability of overtaking as a function of the predicted gap, from the coefficients of
Table L.1. Circuits are listed in decreasing order of the probability at a gap of zero.


Appendix M                                   Rivals’ Pit-Stop Decision-Making
Table M.1 reports the estimated coefficients of the logistic regression in Equation (5).
Laps under a safety car (SC) or virtual safety car (VSC) and a worse track position
are all associated with a higher likelihood of making a pit stop, whereas stops are less
likely in the first ten laps and much less likely in the last ten. If a driver has already
used two different tire compounds, the odds of making a stop decrease. In general, the
softer the tire compound, the more likely a driver is to stop earlier. In the simulation,
the logit is evaluated only on laps in which a pit stop is admissible, i.e., clear-track
laps and the first lap of a SC or VSC period (Algorithm G.1). The model is estimated
with one observation per driver and SC or VSC period, and stops are identified by a
change of tire set, since the timing data also flag laps in which the whole field was led
through the pit lane behind the SC.
    Table M.2 shows the estimated coefficients of the conditional logistic regression in
Equation (6). The negative sign of the last coefficient indicates that when the driver
has used one compound only, it is more likely that a different compound is selected,
all else equal.




                                                          47
       Variable                     Coef.        Std. Err.
       Intercept                 -5.6162***          (0.152)
       Bahrain GP                 1.5180***          (0.149)
       Belgian GP                 1.6129***          (0.170)
       Dutch GP                   0.4334***          (0.150)
       Hungarian GP               0.0325             (0.154)
       Miami GP                  -0.7288***          (0.214)
       Saudi Arabian GP           0.1041             (0.198)
       Singapore GP              -1.4500***          (0.257)
       United States GP           1.3122***          (0.155)
       SC                         3.5309***          (0.115)
       VSC                        3.1374***          (0.144)
       Used two compounds        -1.0413***          (0.065)
       Early laps                -0.4136***          (0.097)
       Late laps                 -2.0614***          (0.115)
       TireLife · C1              0.1380***          (0.009)
       TireLife · C2              0.1180***          (0.005)
       TireLife · C3              0.1461***          (0.004)
       TireLife · C4              0.1893***          (0.006)
       TireLife · C5              0.3002***          (0.014)
       Position                   0.0490***          (0.005)
       Observations                         60,433
       Pseudo R2                             0.216
      Table M.1 Logit regression results for pit stop
      decision. Each SC or VSC period contributes one
      observation per driver, on its first lap. Notes: ***
      p < 0.01, ** p < 0.05, * p < 0.1. Reference
      categories and the indicators of the circuits not
      considered omitted.




 Variable                                   Coef.        Std. Err.
 Alt: C0                               -1.3493**             (0.540)
 Alt: C1                               -0.0278               (0.610)
 Alt: C2                               -1.0243**             (0.406)
 Alt: C4                                1.2418***            (0.443)
 Alt: C5                                3.4327***            (1.044)
 Alt: C0 · LapsLeft                     0.0265*              (0.015)
 Alt: C1 · LapsLeft                     0.0054               (0.019)
 Alt: C2 · LapsLeft                     0.0278*              (0.015)
 Alt: C4 · LapsLeft                    -0.0793***            (0.017)
 Alt: C5 · LapsLeft                    -0.2823***            (0.063)
 Alt: Same & only one comp. used       -1.5111***            (0.296)
 Observations                                        1,742
 Pseudo R2                                           0.311
Table M.2 Conditional logit results for tire compound
choice conditional on pit stop. Notes: *** p < 0.01, **
p < 0.05, * p < 0.1. Base alternative (C3) omitted. Clustered
standard errors at race level (63 races).




                               48
Appendix N               DRL Performance in Simplified
                         Deterministic Instances
Table N.1 reports, for the simplified setting with one driver and no uncertainty, how
much slower the full-race strategy of each DRL agent is than the optimal strategy
of the QMIP. The gap is in seconds, and a zero means that the agent reaches the
optimal race time. Since different strategies can have the same race time, the table
complements the stints shown in Figure 5. The first eight rows give, for each circuit,
the seed with the smallest gap among the five trained that satisfy the two-compound
rule, and the row “Mean” averages them over circuits. The last row gives the median
over the five seeds, averaged over circuits. It is larger than the mean of the selected
seeds for every method, so the result depends on the training run.


        Grand Prix           Double DQN       A2C     TRPO     PPO      Recurrent PPO
        Bahrain                  0.000       0.185    4.919    0.068         0.000
        Belgian                  0.057       0.057    1.217    0.000         0.000
        Dutch                    0.000       1.231    1.408    1.231         0.000
        Hungarian                0.000       0.128    5.374    1.217         0.000
        Miami                    0.421       0.889    3.438    0.885         0.128
        Saudi Arabian            0.000       3.471    5.068    0.000         0.000
        Singapore                0.000       4.971    5.034    0.012         0.000
        United States            0.102       0.082    2.237    0.279         0.000
        Mean                     0.072       1.377    3.587    0.461         0.016
        Median over seeds        0.596       2.214    6.893    2.503         0.903
       Table N.1 Time difference (in seconds) between each DRL model strategy and the
       global optimal race strategy computed via the QMIP model. Positive values indicate
       how much slower the agent’s full-race strategy is compared to the QMIP optimum.
       Each entry corresponds to the seed with the smallest gap among five. Median over
       seeds: median gap across the five seeds of each circuit, averaged over circuits.




Appendix O               Drivers Who Did Not Finish (DNF)
                         per Race
Table O.1 lists the drivers who did not finish each of the eight 2024 races. In the
simulations, rivals that retired in the real race retire on the same lap (Section 6.3).
The second column counts all the retirements of the race, and the third counts those
of drivers who started ahead of the agent. In these races, every retirement is of a driver
who started behind the agent.




                                              49
                                                   DNF
                         Grand Prix       Total   Ahead of Agent
                         Bahrain           0             0
                         Belgian           1             0
                         Dutch             0             0
                         Hungarian         1             0
                         Miami             1             0
                         Saudi Arabian     2             0
                         Singapore         2             0
                         United States     1             0
                        Table O.1 Number of drivers who did not
                        finish (DNF) per race in the 2024 season.
                        DNF Ahead of Agent: number of DNFs
                        among drivers who started ahead of the
                        agent’s grid position.




Appendix P             Mean Final Positions with Confidence
                       Intervals
Table P.1 reports the mean final position of each method in the eight circuits, in the
fully simulated races (top) and in the races with the real realizations (bottom). A lower
position is better. The row “Average” is the mean over the circuits, and “Difference
with QMIP” is the mean paired difference averaged over the circuits, so a negative
value means that the method finishes ahead of the QMIP. The marks are not corrected
for multiple comparisons. The intervals do not include the variability across training
seeds, so the differences with the QMIP refer to the selected agent of each method.




                                           50
 GP                        Double DQN         A2C            TRPO             PPO          Rec. PPO          QMIP
 Fully simulated races (Figure 6)
 Bahrain                   5.34 ± 0.24†    4.69 ± 0.23†   4.91 ± 0.24†    4.04 ± 0.19∗    4.13 ± 0.19∗     4.34 ± 0.20
 Belgian                  10.74 ± 0.25∗   10.71 ± 0.24∗   11.79 ± 0.29†   10.77 ± 0.25∗   10.80 ± 0.25∗   11.18 ± 0.25
 Dutch                      7.67 ± 0.26    7.98 ± 0.26†    7.83 ± 0.30    6.79 ± 0.22∗    6.70 ± 0.22∗     7.72 ± 0.25
 Hungarian                 8.47 ± 0.25†    8.37 ± 0.24†   8.28 ± 0.24†    7.73 ± 0.22∗      7.84 ± 0.23    8.02 ± 0.25
 Miami                     12.98 ± 0.29   13.85 ± 0.29†   14.50 ± 0.28†   12.76 ± 0.28∗    13.06 ± 0.28   12.99 ± 0.27
 Saudi Arabian              4.61 ± 0.18    4.45 ± 0.19     4.71 ± 0.17†    4.41 ± 0.16     4.26 ± 0.16∗    4.51 ± 0.16
 Singapore                 6.65 ± 0.22∗    6.74 ± 0.22     8.62 ± 0.33†   6.42 ± 0.21∗    6.40 ± 0.21∗     6.93 ± 0.21
 United States             9.20 ± 0.23†    9.07 ± 0.23†   9.06 ± 0.25†     8.89 ± 0.23     9.00 ± 0.23†    8.74 ± 0.23
 Average                   8.21 ± 0.09†   8.23 ± 0.08†    8.71 ± 0.09†    7.73 ± 0.08∗    7.77 ± 0.08∗    8.05 ± 0.08
 Difference with QMIP      +0.16 ± 0.08   +0.18 ± 0.08    +0.66 ± 0.09    −0.33 ± 0.07    −0.28 ± 0.07         –
 Real race realizations (Figure 7)
 Bahrain                   5.77 ± 0.22†   4.60 ± 0.22∗     4.95 ± 0.23    4.77 ± 0.22∗    4.83 ± 0.23∗    5.00 ± 0.23
 Belgian                   12.19 ± 0.27    12.19 ± 0.23   12.37 ± 0.27     12.30 ± 0.25   12.89 ± 0.27†   12.31 ± 0.25
 Dutch                    11.06 ± 0.24†   9.59 ± 0.21∗    9.65 ± 0.21∗    9.61 ± 0.20∗    9.83 ± 0.21∗    10.73 ± 0.22
 Hungarian                 8.55 ± 0.18∗   8.46 ± 0.16∗    8.45 ± 0.16∗    8.45 ± 0.15∗     9.54 ± 0.25†   9.35 ± 0.23
 Miami                    10.58 ± 0.30∗   11.01 ± 0.35∗   12.62 ± 0.35†   11.07 ± 0.33∗   12.57 ± 0.29†   12.27 ± 0.28
 Saudi Arabian             7.20 ± 0.20†     5.34 ± 0.14    5.66 ± 0.18†    5.25 ± 0.14     5.25 ± 0.14     5.26 ± 0.14
 Singapore                 9.30 ± 0.16†    8.31 ± 0.18†    9.04 ± 0.20†    8.41 ± 0.17†    7.92 ± 0.16     7.96 ± 0.17
 United States            9.74 ± 0.21∗     10.13 ± 0.21   10.78 ± 0.25†   9.39 ± 0.19∗    9.49 ± 0.20∗    10.27 ± 0.22
 Average                   9.30 ± 0.08†   8.70 ± 0.08∗    9.19 ± 0.08     8.66 ± 0.08∗    9.04 ± 0.08∗    9.14 ± 0.08
 Difference with QMIP      +0.16 ± 0.06   −0.44 ± 0.06    +0.05 ± 0.07    −0.49 ± 0.06    −0.10 ± 0.05         –

Table P.1 Mean final position by solution method and circuit, 2024 season, over 500 simulations
per circuit, with 95% confidence intervals. Since all methods are evaluated on the same 500 random
seeds, the difference with the QMIP is computed race by race. The intervals reflect the variability
across simulated races for the trained agent of each method, and not the variability across training
seeds or circuits. ∗ /† Better/worse than the QMIP at the 5% level (paired t-test, i.e., the 95%
confidence interval of the paired difference excludes zero).




Appendix Q                           Tire Stints of the Candidate Actions
Figure Q.1 shows the tire stints that follow each of the four candidate actions at the
decision point of Figure 8. In every bar, the first segment is the stint on soft tires run
before the decision, the dashed line marks the decision lap, the shaded band is the
safety car period, and the triangles mark the pit stops. Fitting hard or medium tires
at lap 7 is enough to finish the race, since the new set runs the remaining 44 laps.
Fitting soft tires again requires a second stop, to medium tires, after a stint of 25
laps. If the driver stays out, the soft stint ends after 22 laps in a stop to medium tires.
These second stops are why the two actions lose points in Figure 8. Each bar is one
continuation under the PPO policy, with the same race events in the four of them, so
the bars show strategies, not average outcomes.




                                                          51
                                     decision lap 7

                    Hard (C2)    C4 (6)                                                               C2 (44)



Action in lap 7
                  Medium (C3)    C4 (6)                                                               C3 (44)

                     Soft (C4)   C4 (6)                                      C4 (25)                                               C3 (19)

                     Stay out                          C4 (22)                                                        C3 (28)

                                                      10                          20                        30                     40        50
                                                                                                Lap
                                                                 Hard (C2)             Medium (C3)        Soft (C4)   Safety car



Fig. Q.1 Tire stints implied by each candidate action at lap 7 of the 2024 Saudi Arabian Grand
Prix, with the PPO policy driving in place of Lando Norris. Each bar shows one representative
continuation under the PPO policy, with the same realization of race events across actions. Numbers
in parentheses give stint lengths in laps.


Appendix R                                            Review of the 2024 Decisions: Further
                                                      Training and Results for All Races
The policies evaluated in Section 6.3 choose their own starting compound and, in most
races, always start on the same one. When the race history fixes a different starting
compound, as for Norris in the 2024 Saudi Arabian Grand Prix, the look-ahead rollouts
reach states rarely visited during training, in which the policy may propose a second
stint on the starting compound before the two-compound rule is met, so that the
restriction to feasible actions in Algorithm 2 has to override it.
    For the analysis of Figure R.1, training resumes from the selected PPO policy of
each race, including its observation and reward normalization statistics, in the same
environment and with the hyperparameters of Table H.2, except for the following. In
half of the episodes, the starting compound is drawn uniformly among the available
ones, and it is chosen by the policy otherwise; the same mixture is used in the periodic
evaluation episodes. The learning rate is kept constant at 10−4 , and each run lasts at
most 1.5 million steps, with an evaluation every 5,000 steps per environment and the
same early stopping as in the original training, keeping the best checkpoint. We train
ten seeds per race and select one with the validation rule of Appendix H, among the
runs that also meet the two-compound rule in all of 200 validation races when forced
to start on the driver’s actual 2024 compound.
    Over the eight races, the further training changes the mean final position in the
two scenarios of Figures 6 and 7 by less than 0.05 positions; the policy remains ahead
of the QMIP and meets the two-compound rule in all the simulated races, compared
with up to 0.2% of failures for the original policy.
    Figure R.1 shows the stints implied by the recommendation at every lap where it
differs from the actual decision in the eight races. In Singapore, Hülkenberg started
on medium tires and stopped on lap 29 for hard tires (28 and 34 laps). At that lap the
recommendation is to stay out, with a gain of 0.2 ± 0.2 points, just above two standard
errors. Under the policy the driver also makes one stop, from medium to hard tires,
but five laps later (33 and 29 laps), so the difference is small. In the Saudi Arabian



                                                                                         52
Grand Prix, Norris started on medium tires, stayed out under the safety car on lap
7, and stopped on lap 37 for soft tires (36 and 14 laps). At lap 7 the recommendation
is to fit soft tires, which gains 2.9 ± 0.4 points over staying out, and the policy runs
them to the end (6 and 44 laps). In Figure 8 the policy recommends medium tires
instead, since in that race it started on softs. In the later laps the recommendation is
again soft tires, but the differences are −0.1 ± 0.2 (lap 29) and −0.2 ± 0.1 (laps 31 to
36), so they do not support stopping earlier than Norris did.

              Bahrain GP (ALO)                                                                                        Saudi Arabian GP (NOR)
     Actual      14                        26                          17                                   Actual                           36                                  14
    Lap 15          16                     20                         21              No pit: +0.1 ± 0.4     Lap 7     6                                     44                                Soft: +2.9 ± 0.4*
Laps 35 40       14                        24                          19             Hard: +0.8 ± 0.2* Lap 29                         28                                  22                  Soft: -0.1 ± 0.2
                                                                                      (lap 39)
                                                                                                       Laps 31 36                           33                                  17             Soft: -0.2 ± 0.1*
                                                                                                                                                                                               (lap 34)
                    10           20             30          40             50                                                   10               20              30        40             50

              Miami GP (OCO)                                                                                          Hungarian GP (TSU)
    Actual            21                                36                                                   Actual              28                                   42
    Lap 22            21                                36                            Soft: 0.0 ± 0.0        Lap 29               31                                  39                       No pit: +0.1 ± 0.2
                    10           20             30          40             50                                              10          20         30         40       50        60        70

              Belgian GP (GAS)                                                                                        Dutch GP (STR)
     Actual     8                     19                           17                                        Actual              29                                   43
      Lap 9           15                       14                      15             No pit: -0.1 ± 0.1     Lap 30               32                                  40                       No pit: +0.1 ± 0.1
    Lap 25      8                16                               20                  Hard: +0.1 ± 0.2
Laps 26 28      8                    17                           19                  Soft: -0.3 ± 0.2*
                                                                                      (lap 26)
                         10               20            30                  40                                                        20                    40              60

              Singapore GP (HUL)                                                                                      United States GP (MAG)
    Actual                 28                                34                                             Actual          16                         21                       19
    Lap 29                  33                                   29                   No pit: +0.2 ± 0.2* Lap 3 2                20                         15                  19             Medium: +0.1 ± 0.1*
                                                                                                           Lap 17               21                         16                   19             No pit: +0.1 ± 0.1*
                                                                                                       Laps 36 37           16                        19                    21                 Medium: 0.0 ± 0.0
                                                                                                                                                                                               (lap 36)
                    10          20         30          40         50             60                                          10             20           30           40             50
                                           Lap                                                                                                         Lap

                                                Hard                   Medium                   Soft           Safety car                    Virtual SC


Fig. R.1 Actual 2024 tire stints of each driver and stints implied by the DRL recommendation at
every lap where it differs from the actual decision. Each lower bar replays the race up to the lap
marked by the triangle and shows one representative continuation under the PPO policy, without
further yellow flags. Consecutive laps with the same recommendation share a bar, drawn from the
lap with the largest difference. The annotation on the right reports the recommended action and
the mean paired difference in points against the actual decision at that lap (given in parentheses for
grouped bars), over M = 500 rollouts with simulated yellow flags, ±2 SE; positive values favor the
DRL recommendation and negative values favor the driver’s actual decision, and ∗ marks differences
larger than 2 SE. The differences come from the rollouts used to select the best action in Figure 10,
so they differ slightly from those reported there.




                                                                                                        53
Appendix S              Computation Times
Table S.1 reports the median wall-clock time, in hours, needed to train one policy for
one circuit, with at most 5M timesteps. Policies are trained on an AMD EPYC 9224,
with four CPU cores in the setting with competition and two without it. Once trained,
a PPO decision takes about 0.1 ms and a QMIP solve at most about 20 ms, or about
0.2 s for a whole race, on one core of an Apple M4. A look-ahead recommendation is
more demanding, since its cost grows with M and with the remaining laps: at lap 7
of the case in Figure 8, it takes about 50 s with M = 500 and 11 s with M = 100
in a single process. Since rollouts are independent, they can be distributed across
processes with identical results: the look-ahead takes about 13 s for M = 500 with
eight processes and about 6 s for M = 100 with four.


       Setting                Double DQN      A2C     TRPO     PPO     Recurrent PPO
       With competition            1.65       1.48     1.67     1.50         1.86
       Without competition         0.37       0.16     0.28     0.25         0.83
      Table S.1 Median wall-clock training time per policy and circuit, in hours, by DRL
      method.




                                             54
