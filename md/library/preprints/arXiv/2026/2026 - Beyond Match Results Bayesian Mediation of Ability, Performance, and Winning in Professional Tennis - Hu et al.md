# Beyond Match Results: Bayesian Mediation of Ability, Performance, and Winning in Professional Tennis

- arXiv: https://arxiv.org/abs/2610.21023
- Published: 2026-10-14
- PDF: ../../library/preprints/arxiv/2026/2026 Beyond Match Results Bayesian Mediation of Ability, Performance, and Winning in Professional Tennis - arXiv 2610.21023.pdf

## Abstract

Match results measure competitive ability, but they do not explain how ability is expressed during play. Match statistics offer a natural mediator, however performance is usually measured over the same match as the outcome: a full-match statistic uses events that help determine the winner, while a first-set statistic is earlier but rests on fewer service points and still contributes to the result. Comparing the two therefore mixes timing and precision. We develop a Bayesian mediation framework for this problem. Dynamic abilities on hard, clay, and grass courts are estimated from previous seasons only and are linked to both players' service performance, and a Bradley--Terry model relates ability and performance to the match result. A control mediator samples the first set's number of service points from the full match, separating the measurement window from the point count. In 3,820 men's matches, the hard-court mediated share rises from 0.52 with a first-set mediator to 0.95 with a full-match mediator; the point-count contrast accounts for 0.30 of this gap and the window contrast for 0.13. The pattern replicates on the women's tour. Simulations and sensitivity analyzes examine the decomposition and assumptions needed for a causal interpretation.

## Full text (pdftotext)

                                                     Beyond Match Results:
                                            Bayesian Mediation of Ability, Performance,
                                               and Winning in Professional Tennis
                                                                         Guanyu Hu
                                              Department of Statistics and Probability, Michigan State University
arXiv:2610.21023v1 [stat.AP] 14 Oct 2026




                                                                             and
                                                                          Xiao Wang
                                                        Department of Statistics, Purdue University



                                                                                       Abstract

                                                    Match results measure competitive ability, but they do not explain how ability is
                                                expressed during play. Match statistics offer a natural mediator, however performance
                                                is usually measured over the same match as the outcome: a full-match statistic uses
                                                events that help determine the winner, while a first-set statistic is earlier but rests on
                                                fewer service points and still contributes to the result. Comparing the two therefore
                                                mixes timing and precision. We develop a Bayesian mediation framework for this
                                                problem. Dynamic abilities on hard, clay, and grass courts are estimated from previous
                                                seasons only and are linked to both players’ service performance, and a Bradley–Terry
                                                model relates ability and performance to the match result. A control mediator samples
                                                the first set’s number of service points from the full match, separating the measurement
                                                window from the point count. In 3,820 men’s matches, the hard-court mediated share
                                                rises from 0.52 with a first-set mediator to 0.95 with a full-match mediator; the
                                                point-count contrast accounts for 0.30 of this gap and the window contrast for 0.13.
                                                The pattern replicates on the women’s tour. Simulations and sensitivity analyzes
                                                examine the decomposition and assumptions needed for a causal interpretation.

                                           Keywords: Bradley–Terry model; measurement error; pathway decomposition; sports
                                           analytics




                                                                                            1
1     Introduction
The match results reveal differences in competitive ability, but they say little about how

those differences are expressed during play. A player may win through a persistent advantage

in ability because that advantage produces better serving or returning, or because both

pathways operate together. Mediation analysis (Baron & Kenny 1986, Imai, Keele &

Tingley 2010) organizes such questions, and paired-comparison models such as Bradley–

Terry (Bradley & Terry 1952) have long measured player strength in tennis and other

sports (Glickman & Stern 1998, Kovalchik 2020, Radicchi 2011). Both frameworks are well

established, but combining them in tennis raises a measurement problem that neither one

addresses on its own.

    Professional tennis is a useful setting for this question (Reid et al. 2010, Blackburn 2013,

Bozóki et al. 2016). The serve is the most scrutinized part of the game: in Grand Slam play

the server wins about 69–75% of first-serve points and roughly 55% of second-serve points,

and first-serve points are won about 69% of the time on clay against 75% on grass and hard

courts (Prieto-Lage et al. 2023); point outcomes also carry information beyond independent

coin flips (Klaassen & Magnus 2001). Match-level summaries of serve performance are

widely used in broadcasts, betting markets and player evaluation, but they are computed

over the completed match, so a full-match measure of service points won is built from events

that also help determine the winner. We call this outcome overlap.

    One apparent remedy is to shorten the measurement window, but restricting the mediator

to the first set changes more than the timing: fewer service points enter the statistic, so it

is measured less precisely, and classical measurement error attenuates its coefficient and

shrinks the estimated indirect effect (Carroll et al. 2006). Comparing full-match and first-set

mediators therefore mixes a change in window with a change in precision, a trade-off easy

to overlook because within-match statistics feel like a direct read on how a match was won.


                                               2
Diagnosing it requires varying the two separately, which is what we develop below.

   Existing methods stop short of such a diagnosis. The Bradley–Terry model relates the

probability that one player defeats another to the difference in their latent abilities (Bradley

& Terry 1952), in the paired-comparison tradition initiated by Zermelo (1929) and developed

for computation and dynamic ability by Hunter (2004), Glickman (1999), Glickman & Stern

(1998), Cattelan et al. (2013); the distinction between observed results and underlying

strength matters in sports because outcomes carry substantial contest-to-contest variation

(Lopez et al. 2018). In tennis, Klaassen & Magnus (2001) show that points are neither

independent nor identically distributed, Barnett & Clarke (2005) use service statistics for

forecasting, and Ingram (2019) develops a hierarchical point-level model. Ranking and Elo

procedures remain strong predictive benchmarks (Kovalchik 2016), and Dong et al. (2026)

let player strength depend on comparison-specific covariates in a Plackett–Luce model. None

of this work examines how a pre-match ability advantage is expressed through performance

measured during the match, or how the construction of that measure affects the estimated

pathway.

   The mediation literature supplies the causal vocabulary but not the fix. Direct and

indirect pathways run from the regression formulation of Baron & Kenny (1986) to the

counterfactual definitions of Robins & Greenland (1992) and Pearl (2001); identification,

estimation and sensitivity analysis are studied by Imai, Keele & Tingley (2010), Imai, Keele

& Yamamoto (2010), VanderWeele (2015), with particular attention to unmeasured mediator–

outcome confounding (VanderWeele 2010, Cinelli & Hazlett 2020). Timing is central to

time-varying exposures (Robins et al. 2000), and using information collected during an

outcome period is close to the logic of immortal time bias (Suissa 2008). Measurement error

in a mediator is equally well understood, but timing and precision are usually treated as

separate concerns. In tennis they change together, and that is the gap we address. Because

latent ability is not a manipulable treatment and the required mediator and outcome


                                               3
assumptions cannot be verified from these data, we report direct and indirect effects as

model-based pathway summaries rather than unconditional causal claims.

   We make two methodological contributions. The first is a modular ability model in

which service performance cannot contaminate the ability assigned before a match: a

dynamic Bradley–Terry model pools player strength across hard, clay and grass courts,

ability entering a season-t match is learned only from results through season t − 1, so the

match under analysis never contributes to its own pre-match estimate, and the performance

and outcome models are fitted conditional on draws from it (Bayarri et al. 2009, Plummer

2015), which prevents information from flowing backward from within-match performance

into pre-match ability.

   The second is a point-count-matched design that separates what a shorter window

changes. The control mediator samples without replacement from all of a player’s service

points, keeping the number served in the first set, so it covers the full match at the first-set

sample size. Comparing it with the full-match statistic defines a point-count component;

comparing it with the first-set statistic defines the remaining window-construction compo-

nent, which may combine outcome overlap with genuine changes in performance across sets.

We therefore add a second outcome: first-set performance lies inside the match outcome’s

window but entirely before the second-set outcome. These contrasts distinguish point

count from the remaining change in construction; they do not separately identify overlap

and performance change. Uncertainty in constructing the control is propagated through

a design-integrated posterior mixture, analogous to multiple imputation (Rubin 1987),

and the diagnostic makes the distinction explicit without claiming that either contrast is

automatically a causal effect.

   The application contributes on its own terms. It asks not how to rank players but

how an ability advantage established before a match reaches the result through service

performance. Statistics such as service points won drive broadcasts, betting lines and player


                                               4
evaluation, and the conclusions drawn from them depend on two choices analysts usually

make by default: the measurement window and the number of points behind the statistic.

The reliability analysis extends the same logic to settings where only an aggregate statistic

and its denominator are observed, which covers most sports without point-level records.

    Section 2 describes the linked match and point-level data. Section 3 introduces the

surface-specific ability model, defines the pathway estimands, states the identification

conditions, describes computation and reports the simulation evidence. Section 4 presents

the ATP and WTA analyses with the reliability analysis for settings without point-level

data, and Section 5 concludes the paper with detailed discussions. Further simulations,

computational detail, diagnostics and posterior predictive checks are in the supplementary

material.



2     Motivating data

2.1    Data sources and study samples

We combine tour-level match records with point-level charting data. The men’s and women’s

archives maintained by Jeff Sackmann provide main-draw singles results, match dates, court

surfaces, tournament rounds, rankings and match-level service statistics (Sackmann 2026a,c);

we retain matches played on hard, clay and grass courts from 2015 through 2026. The Match

Charting Project supplies the point-level records needed to reconstruct service performance

over different portions of a match (Sackmann 2026b). Records are linked on normalized

player names, match dates and surfaces, with a small date discrepancy permitted only when

the player pair and surface agree.

    The men’s charting archive contains 6,575 records, of which 1,628 precede the study

period and 184 belong to the 2026 holdout season. Among the 4,763 records from 2015

through 2025, 4,138 link to a tour-level match. Most of the remaining 625 could not link



                                             5
under any rule: 256 involve a player outside the 485-player core used for ability estimation,

54 are qualifying-round matches (20 of them in both groups) and 204 are Challenger

matches, and the main-draw tour files contain neither qualifying nor Challenger matches.

Section S1 of the supplementary material gives the linkage rules and the disposition of every

record. The women’s replication is constructed independently under the same definitions;

the descriptive figures in this section use the ATP samples only.

   Table 1 summarizes the three ATP samples. The ability sample is the broad set of tour

matches used to estimate how player strength changes across seasons and surfaces. The

pathway sample is smaller because it requires a link to the point-level archive, complete

service information for both competitors, a valid point-count-matched mediator and a prior

ability history. Matches from 2026 are reserved for forecast evaluation.
                      Table 1: Samples used in the primary ATP analysis.
Sample    Seasons                             Size   Inclusion and use
Ability   2015–2025    28,658 matches; 485 players   Main-draw singles matches on hard, clay
                                                     or grass, with both players appearing in
                                                     at least ten matches; used to estimate the
                                                     dynamic surface-specific ability model.
Pathway   2016–2025                 3,820 matches    Linked matches with complete first-set and
                                                     full-match service records, a valid point-
                                                     count-matched mediator and prior ability
                                                     information for both players: 2,484 hard-
                                                     court, 940 clay-court and 396 grass-court
                                                     matches.
Holdout   2026                      1,178 matches    Matches reserved for forecast evaluation
                                                     and excluded from estimation.


   Figure 1 describes the ability sample. The annual match counts show how sharply the

available information varies across seasons and surfaces, and the player heatmap shows the

same from the player side, comparing raw surface-specific win rates for frequently observed

players. These rates do not adjust for opponent strength, but they make the central point:

a single rating can conceal large differences between hard, clay and grass courts.

   Before constructing the outcome we randomly assign the competitors in each match to



                                              6
                                       (a) Match counts by season and surface                           (b) Raw win rate by surface, 15 most-observed players
                                1750                                     Hard alexander zverev            0.69 (443)   0.75 (220)   0.66 (67)
                                                                         Clay        novak djokovic       0.86 (400)   0.82 (184)   0.92 (72)    1.0
                                1500                                     Grass daniil medvedev            0.73 (443)   0.57 (81)    0.67 (75)
Matches in the ability sample
                                                                              roberto bautista agut       0.61 (371)   0.55 (149)   0.65 (72)
                                                                                                                                                 0.8
                                1250                                                  andrey rublev       0.63 (406)   0.66 (134)   0.66 (35)
                                                                                  stefanos tsitsipas      0.64 (344)   0.75 (163)   0.54 (41)




                                                                                                                                                   Raw win rate
                                1000                                                grigor dimitrov       0.64 (378)   0.58 (123)   0.57 (46)    0.6
                                                                                 adrian mannarino         0.49 (380)   0.22 (59)    0.59 (103)

                                 750                                                     taylor fritz     0.61 (378)   0.56 (93)    0.63 (68)    0.4
                                                                                  karen khachanov         0.57 (343)   0.58 (132)   0.64 (50)
                                                                                        david goffin      0.56 (339)   0.59 (138)   0.59 (44)
                                 500                                                                                                             0.2
                                                                                     dominic thiem        0.59 (256)   0.70 (214)   0.48 (31)
                                                                                    alex de minaur        0.65 (354)   0.52 (77)    0.64 (56)
                                 250                                                     marin cilic      0.59 (307)   0.59 (102)   0.75 (64)    0.0
                                                                                        rafael nadal      0.76 (246)   0.85 (193)   0.79 (29)
                                   0                                                                       Hard         Clay         Grass
                                     15
                                     16
                                     17
                                     18
                                     19
                                     20
                                     21
                                     22
                                     23
                                     24
                                     25
                                   20
                                   20
                                   20
                                   20
                                   20
                                   20
                                   20
                                   20
                                   20
                                   20
                                   20                  Season
        Figure 1: Structure of the ATP ability sample. Panel (a) reports the number of matches observed
        in each season on hard, clay, and grass courts. Panel (b) reports raw surface-specific win rates for
        frequently observed players represented on all three surfaces, with the corresponding match counts
        shown in parentheses. The win rates are descriptive and do not adjust for opponent strength.

        positions a(m) and b(m) using a fixed seed, removing the winner-first ordering inherited

        from the source files; after randomization player a(m) wins 49.9% of matches, as expected

        under an assignment unrelated to the result. For player i in match m, service performance

        over a window W is


                                                                first-serve points won + second-serve points won
                                                Xim (W) =                                                        .                                                (1)
                                                                               service points played


       This is the proportion of all points won while serving, not the percentage of first serves

        placed in play, and it can be reconstructed from the point-level records over any window.

                                 Table S2 defines the outcomes, exposure and mediator constructions used in the pathway

        analysis. The full-match mediator uses every service point a player played; the first-set

        mediator uses only points from the opening set; the point-count-matched control draws

       without replacement from the complete match record while retaining that player’s first-set

        service-point count. All three come from the same point-level source and are standardized

       within surface before fitting.

                                 Figure 2 is built from the exact ATP matches in the pathway analysis: its panels compare

                                                                                            7
         the service-point counts behind the first-set and full-match mediators, the player differences

         from the two windows, and the relation of each difference to the observed probability of

        winning. The first-set statistic uses only about forty percent as many service points, and

        while the two measures are positively associated, the full-match difference aligns far more

         closely with the winner.
                                        (a) Service points behind each mediator                                                                                                                                           (c) Performance difference and match outcome
                                                                                                                                                                                                                    1.0
                                              First set                                                                              (b) Agreement between windows                                                              First set

                                                                                 Full-match difference, Rfull, a − Rfull, b
                                  175         Full match                                                                                                                                                                        Full match
Service points per player-match




                                                                                                                               0.4    r = 0.78                               50                                     0.8




                                                                                                                                                                                        Observed P(player a wins)
                                  150                                                                                                 n = 3,820
                                                                                                                                                                             40
                                  125                                                                                          0.2
                                                                                                                                                                                                                    0.6




                                                                                                                                                                              Matches
                                                                                                                                                                             30
                                  100                                                                                          0.0
                                                                            89
                                  75               74          73                                                                                                            20                                     0.4
                                                                                                                              −0.2
                                  50                                                                                                                                         10
                                              30                      30
                                                                                                                              −0.4                                                                                  0.2
                                                         29
                                  25
                                   0
                                                                                                                                 −0.50 −0.25 0.00 0.25 0.50                                                         0.0
                                           Hard         Clay        Grass                                                        First-set difference, Rset1, a − Rset1, b                                  −2         0          2
                                                                                                                                                                                                 Standardised performance difference (bin mean)
     Figure 2: Service-performance measurement in the ATP pathway sample. Panel (a) compares
     the numbers of service points used to construct the first-set and full-match mediators. Panel
     (b) compares the corresponding player performance differences. Panel (c) reports the observed
     probability that player a(m) wins across binned values of the standardized performance difference.
     All panels use the same matches included in the primary pathway analysis.


                                   The second fact is why a mediation analysis of these data cannot proceed in the usual

        way. The full-match mediator is assembled from the very points through which the result

         is realized, so part of its association with winning is mechanical rather than behavioral.

        The first-set statistic moves measurement before most of the outcome, but discards more

         than half of the service points, so comparing the two confounds a change in window with

         a change in precision, and more matches cannot resolve a confound built into how the

         statistics are defined. The point-count-matched control reproduces the loss of precision

        while keeping the full-match window, so the two changes can be estimated separately. It is

         sampled without replacement because sampling with replacement would add variation from

         repeatedly drawing the same observed record.




                                                                                                                                                         8
2.2    Empirical motivation

Each feature of the ATP data rules out a simpler analysis. Players appear repeatedly

and their level changes over time, so a static rating is insufficient. Their information

differs sharply across surfaces, with long hard-court histories and a short grass season, so

three independent ratings would be noisy where data are scarce while one pooled rating

would suppress the specialization the heatmap in Figure 1 suggests. The ability model is

therefore dynamic and hierarchical, letting overall strength evolve while partial pooling

carries information from well-observed surfaces to sparse ones.

   Service performance imposes a different requirement. A service-point percentage reflects

the server’s quality and the returner’s at once, so it is not a player attribute in isolation,

and the performance model conditions on the pre-match abilities of both competitors. Its

output enters the outcome model, where Figure 2 shows a tight descriptive relationship

between the full-match performance difference and winning. That tightness is the problem:

it reflects outcome overlap as much as any behavioral pathway, while shortening the window

confounds timing with precision. The three mediator constructions exist because the data

offer no mediator that is at once early, precise and free of overlap.

   Temporal ordering creates one more constraint. An ability read off a model fitted to

the full study period would let current and future results leak into the exposure assigned

to earlier matches, so we estimate ability from expanding windows of prior seasons and

keep the performance model from feeding information back. The design follows from what

these data can and cannot identify: repeated comparisons argue for a dynamic ability

model, sparse grass-court histories for partial pooling, opponent-dependent performance

for a two-competitor mediator, and the joint movement of timing and precision for the

point-count-matched control and the second-set comparison.




                                              9
3     Method

3.1    Dynamic surface-specific ability

Let i = 1, . . . , N index players, m = 1, . . . , M index matches, and t index seasons. The

surface of match m is sm ∈ S = {H, C, G}, corresponding to hard, clay, and grass courts,

while a(m) and b(m) denote the two participating players. We define Ym = 1 when player

a(m) wins and Ym = 0 otherwise. The Bradley–Terry model represents this outcome through

the difference between the players’ latent abilities (Bradley & Terry 1952). It belongs to

the paired-comparison tradition initiated by Zermelo (1929) and has been extended to

more general comparison structures, computational procedures and abilities that evolve

over time (Hunter 2004, Glickman 1999, Cattelan et al. 2013). The last extension matters

here, because the set of active players changes from season to season and the information

available on each surface is highly uneven.

    A single rating is too restrictive here. Players develop persistent strengths on particular

surfaces, but an unrelated trajectory per surface would be unstable, especially on grass,

so we separate ability into an overall component that evolves by season and a surface

specialization shared across seasons:


                θi,s,t = µi,t + δi,s ,     µi,t = µi,t−1 + ωit ,       ωit ∼ N (0, σω2 ).   (2)


Here µi,t is the player’s competitive level in season t and δi,s the amount by which surface s

raises or lowers it. Unobserved annual innovations are integrated out over an absence, so

for consecutive active seasons t′ < t,


                                                                     
                                  µi,t | µi,t′ ∼ N µi,t′ , (t − t′ )σω2 .




                                                    10
This is the transition implied by the unconstrained annual increments, not an assumption

that ability is fixed during an absence. Because the zero-sum restrictions below couple the

players’ coordinates, it is a building block of the constrained Gaussian prior rather than the

conditional distribution of one constrained coordinate.

   Conditional on the latent abilities, match results follow the surface-specific Bradley–Terry

model


                                                                                        
          Ym | θ, a ∼ Bernoulli(pm ),        logit(pm ) = asm θa(m),sm ,tm − θb(m),sm ,tm ,       (3)


where as > 0 is a surface-specific discrimination parameter. The ability difference determines

which player is favored; as how sharply latent separation translates into a difference in win

probability. Letting it vary by surface avoids forcing the same latent gap to carry the same

predictive consequence on every court.

   The likelihood in (3) depends only on ability differences, and the decomposition in (2)

introduces an additional invariance between overall ability and surface specialization. We

remove these invariances by imposing


   X                               N
                                   X                                X
         µi,t = 0 for every t,           δi,s = 0 for every s,            δi,s = 0 for every i,   (4)
  i∈At                             i=1                              s∈S



where At is the set of players active in season t. The first restriction defines each season

relative to its active player population; the others separate general ability from surface

specialization, since surface effects average to zero across players and each player’s across

the three court types. The restrictions are imposed through orthonormal Helmert bases:

with Ht the basis for the players active in season t and HN and H3 the player and surface

bases,

                 µt = Ht zt ,    δ = σδ HN Draw H3⊤ ,        vec(Draw ) ∼ N (0, I).



                                                 11
This parameterization is one-to-one on the constrained space and avoids the redundant

direction left by centering unrestricted coordinates after sampling. The noncentred repre-

sentation of δ also reduces posterior dependence between the surface effects and their scale

σδ .

       The zero-sum restriction changes the normalizing term of the random-walk prior, which

depends on σω and is retained when that variance is estimated (Section S5.2 of the sup-

plementary material gives the expression). The scale is anchored through µi,tmin
                                                                             i
                                                                                 ∼ N (0, 1),

with tmin
      i   player i’s first season: rescaling every ability and dividing as by the same constant

leaves (3) unchanged, so as is read relative to this reference scale.

       The pathway analysis requires ability to be determined before the match under study.

A trajectory fitted to all seasons fails this, because the random walk smooths an earlier

state using later results. For every target season T we therefore refit (2) and (3) using only

matches played before T . Let t∗i (T ) < T be the most recent season in that window in which

player i was active and gi (T ) = (T − 1) − t∗i (T ). The exposure is the latent state at the end

of the historical window, season T − 1, not an unobserved season-T state. Propagating the

fitted transition model to that boundary gives

                                                       q
                      −
                    θei,s (T ) = µi,t∗i (T ) + δi,s + σω gi (T ) Zi ,   Zi ∼ N (0, 1).        (5)


The extra innovation term vanishes for a player observed in the preceding season, whose

posterior draw already carries that season’s uncertainty, and propagates the unobserved

transitions through season T − 1 for a player returning after an absence; a one-step forecast

of the season-T state would use T − t∗i (T ) instead, which is not the exposure here. Players

without earlier match history are excluded rather than assigned an exposure determined

almost entirely by the prior.

       Because each expanding-window fit has its own anchored scale, the abilities passed to


                                                       12
the pathway model are standardized within their window:

                                  −
                     −          θei,s (T )                h   n
                                                               −
                                                                                oi
                    θi,s (T ) =            ,    ςT = sdi,s E θei,s (T ) | D<T        ,       (6)
                                    ςT


where the standard deviation is taken over players with prior history and the three surfaces,

so one unit of θ− is one window-specific standard deviation in the historical ability field. The

eligible player population is defined using the complete study period, so sample membership

stays retrospective even though no current or future outcome enters θ− . That does not

affect comparisons among mediator constructions, which share the same ability draws, but

it limits the standardized unit to the population the study represents.


3.2    Observed performance and match outcomes

The second stage describes how pre-match ability is expressed through observed service

performance and how both quantities are associated with the match result. Let w ∈ W =
                                                                     (w)
{set1, ctrl, full} index the mediator construction, and let Rim denote the proportion of

service points won by player i in match m. The three constructions use the first set, a

point-count-matched subsample of the full match, and the full match, respectively. Because

the marginal distribution of service performance differs across surfaces, each version is

centered and scaled within surface, pooling the observations from both players:

                                                 (w)     (w)
                                           (w)  Rim − Rsm
                                          Xim =      (w)
                                                             .                               (7)
                                                   Ssm


For a resampled control the standardization is repeated within each imputation, using the

control realization supplied to that fit. We suppress w when describing one construction,

but all pathway parameters are construction-specific, with c(w)  (w)
                                                            s , λs   and gs(w) estimated in

separate fits: the three constructions are alternative measurements of the mediator, not

repeated observations governed by a common coefficient.


                                                   13
   Service performance depends on both players: a strong server wins more points on serve,

but fewer of them against a stronger opponent. We represent both features jointly as


                                           −                 −
                     Xa(m)m = αsm + βsown
                                       m
                                          θa(m),s m
                                                    + βsopp
                                                         m
                                                            θb(m),s m
                                                                      + εam ,              (8)

                                           −                 −
                     Xb(m)m = αsm + βsown
                                       m
                                          θb(m),s m
                                                    + βsopp
                                                         m
                                                            θa(m),s m
                                                                      + εbm ,              (9)
                                                     
                     εam      0       1          ρ
                          ∼ N   , σ 2                 .                           (10)
                                X                    
                         εbm          0              ρ 1


The restrictions βsown > 0 and βsopp < 0 orient the model so that own ability improves service

performance and opponent ability suppresses it. The correlation ρ is unrestricted: match

conditions may move the two residuals together, while momentum or other within-match

dynamics may move them apart, and the bivariate distribution allows either pattern rather

than treating the two player-match observations as conditionally independent.

   Equations (8)–(10) are a working model for the surface-standardized proportion; they

do not use the service-point count as a binomial denominator, which enters instead through

the control mediator below. Reliability and simulation analyses assess departures from the

assumptions that make that control comparable to the first-set measure.

   The outcome layer extends the Bradley–Terry model by allowing realized service perfor-

mance to enter alongside the pre-match ability difference:


                                                                −
                 Ym ∼ Bernoulli(pm ),        logit(pm ) = csm ∆θm + λsm ∆Xm ,             (11)


where
                   −    −           −
                 ∆θm = θa(m),s m
                                 − θb(m),s m
                                             ,        ∆Xm = Xa(m)m − Xb(m)m .


The surface-specific coefficient cs > 0 measures the part of the ability association remaining

after conditioning on observed performance, and λs > 0 the association between the service-


                                                 14
performance advantage and the outcome at a fixed ability difference. Equation (11) is fitted

separately for each mediator construction and each outcome. With the match winner, the

first-set mediator occurs earlier but remains part of the outcome-generating period; with the

second-set winner, first-set performance is measured entirely before the outcome window.

   The positivity restrictions orient the decomposition and imply a mediated share between

zero and one. They are substantive rather than identification conditions and exclude

inconsistent mediation, so we also report an unrestricted refit of the direct coefficient and

read near-boundary shares against it.

   The two stages are kept modular, because a joint posterior would let the within-match

mediator and outcome revise the latent ability assigned to that match, weakening the

pre-match interpretation the expanding-window construction establishes. With DA the

historical results used to estimate ability, DP the pathway data and ψ the performance and

outcome parameters, we target the cut distribution


                                                                      
                   pcut ψ, θ − | DA , DP = p ψ | θ − , DP p θ − | DA ,                   (12)


whose marginal pathway distribution is

                                    Z                         
                       pcut (ψ) =       p ψ | θ − , DP p θ − | DA dθ − .                 (13)


The first-stage posterior acts as an imputation distribution for pre-match ability, and the

second stage is refitted conditionally on draws from it (Rubin 1987), propagating ability

uncertainty without feedback from the pathway data. The result is a modular, or cut,

posterior rather than an ordinary joint posterior (Plummer 2015, Jacob et al. 2017).

   Contrasts among mediator constructions require a joint convention for the otherwise




                                                 15
separate fits. We use the comparison distribution


                                                                                 
                                                                              (w)
               qcmp θ − , {ψ (w) }w∈W = p(θ − | DA )          p ψ (w) | θ − , DP
                                                        Y
                                                                                        .   (14)
                                                        w∈W



Figure S1 of the supplementary material shows the resulting temporal structure, with an

unobserved match-level shock that may act on both mediator and outcome. All constructions

share the same draw of pre-match ability, while their pathway parameters are conditionally

independent given that draw. This is a comparison distribution, not a generative joint

posterior: the same match outcome appears in each alternative analysis and is not generated

three times. Equation (14) states the dependence used for posterior contrasts without

suggesting that the data identify residual cross-model covariances that were never estimated.


3.3    Pathway estimands and identification

A pathway contrast must specify how the abilities of both competitors change. We use a

symmetric intervention that changes their difference while holding their mean fixed:


                                d                  d
                        θa (d) = ,       θb (d) = − ,         ∆θ(d) = d.                    (15)
                                2                  2


This avoids reading the contrast as a change in the general standard of the match. Under

(8) and (9), the expected performance difference responds to d through


                                 ∂
                          gs =      E{∆Xm (d) | s} = βsown − βsopp .                        (16)
                                 ∂d


Since βsown > 0 and βsopp < 0, the gradient gs is positive: raising one player’s ability while

lowering the opponent’s widens the expected performance difference through both sides of

the match.




                                              16
   For construction w and the reference contrast d0 = 0 and d1 = 1, write


                                                                 h                         i
                (w)                                                      (w)
              ∆Xm   (d) = gs(w) d + e(w) ,           e(w) ∼ N 0, 2{σX }2 {1 − ρ(w) } .


The surface intercept drops out of the difference and the common part of the two residuals

cancels. Using the same realization of e(w) under both ability levels, the direct, indirect and

total pathway summaries on the win-probability scale are


                         h                                                     i
         DE(w)
           s   = Ee(w) expit{c(w)
                              s   + λ(w)
                                     s e
                                         (w)
                                             } − expit{λ(w)
                                                        s e
                                                            (w)
                                                                } ,                                (17)
                         h       h                               i                             i
          IE(w)
            s   = Ee(w) expit c(w)
                               s   + λ(w) (w)
                                      s {gs   + e(w) } − expit{c(w)
                                                                s   + λ(w)
                                                                       s e
                                                                           (w)
                                                                               } ,                 (18)
                         h       h                               i                     i
          TE(w)
            s   = Ee(w) expit c(w)
                               s   + λ(w) (w)
                                      s {gs   + e(w) } − expit{λ(w)
                                                                s e
                                                                    (w)
                                                                        } .                        (19)


The direct effect changes ability with the mediator held at its d0 distribution; the indirect

effect moves the mediator from its d0 to its d1 distribution with the ability contrast held at

d1 ; the total effect changes both. These definitions give


                                      TE(w)
                                        s   = DE(w)   (w)
                                                s + IEs ,




and the construction-specific mediated share Ss(w) = IE(w)   (w)
                                                       s / TEs , both evaluated within

each posterior draw. Numerical verification of the identity is a coding check, not evidence

for the model.

   The decomposition reported in the application is now explicit. For each surface, define


                       Gs = Ss(full) − Ss(set1) ,

                        Ps = Ss(full) − Ss(ctrl) ,        Ws = Ss(ctrl) − Ss(set1) .               (20)


Here Gs is the conventional full-match versus first-set gap, Ps the point-count component


                                                     17
and Ws the remaining window-construction component, with Gs = Ps + Ws by definition.

These are contrasts among three fitted constructions for a centered pair separated by one

standard deviation of historical ability, not population average treatment effects; the labels

do not by themselves supply a causal interpretation.

   The control separates the number of service points from the part of the match over

which they are observed. With Rim = (Wim1 , . . . , WimNim ) the service-point outcomes of

player i in match m, write
                                     full      1 NXim

                                    Rim   =           Wimk .
                                              Nim k=1

If the player serves nim points in the first set, the control mediator is the mean of nim

entries drawn uniformly without replacement from Rim , independently of their values.

Proposition 1 (Common target of the full and control mediators). Conditional on the

complete service record,
                                                    
                                      ctrl          full
                                   E Rim   | Rim = Rim   .

                    full
Consequently, if E(Rim   | πim ) = πim for a latent match-specific service rate πim , then


                                        ctrl
                                     E(Rim   | πim ) = πim .


The full-match and control mediators therefore target the same performance quantity. Their

difference concerns measurement rather than the underlying construct.

   The result follows because every service point has inclusion probability nim /Nim in

the control sample. It establishes a common finite-record target, but not a pure precision

effect: differences between nonlinear fitted shares depend on the mediators’ full conditional

distributions, not only their variances.

   Matching the precision of the first-set mediator requires more. Suppose the service

points are exchangeable given a latent rate π, with conditional variance v and common

                                                18
pairwise covariance q, and the number n of first-set service points is fixed given π and does

not depend on their values.


Proposition 2 (Matched conditional variance). Under these conditions, the first-set medi-

ator and a without-replacement control containing n points have the same conditional error

variance:
                                                              v     1
                                                                       
                             set 1                 ctrl
                     Var R           | π = Var R          |π = + 1−   q.
                                                              n     n

If the points are conditionally independent Bernoulli observations, this reduces to π(1 − π)/n.


   This is why the control is sampled without replacement: a with-replacement sample

adds variation from repeatedly drawing the observed full-match pool, making it noisier

than the statistic it is meant to match (Section S2 of the supplementary material gives the

derivation). The conditions of Proposition 2 should not be taken for granted in tennis, since a

set ends when one player wins it, making the number of service points an outcome-dependent

stopping time; matching the observed count does not establish that the two statistics have

the same conditional error distribution. We therefore call the primary construction point-

count-matched. Its contrast with the full-match mediator has a design-based interpretation

conditional on the observed service record, and is a contrast in measurement precision about

a latent rate only under the exchangeability and stopping assumptions of the proposition,

whose failure modes the reliability analysis and simulation examine.

   Measurement error describes the direction in which an imperfect match can matter.

With κs the conditional reliability of a mediator contrast, the classical linear attenuation

approximation gives


                                                                      Var(∆Xtrue | ∆θ)
            b =κ λ ,
            λ s s s          cbs = cs + λs gs (1 − κs ),       κs =                    .   (21)
                                                                      Var(∆Xobs | ∆θ)


The first relation attenuates the estimated mediator coefficient; the second transfers the


                                                  19
omitted part of the pathway to the ability coefficient, so


                                     cbs + λ
                                           b g =c +λ g ,
                                            s s  s  s s




and the total coefficient is preserved along this attenuation path. For a linear outcome, lower

reliability necessarily reduces the mediated effect and its share. For the logistic outcome

the result is local, because both the residual scale and the curvature of the link affect

probability-scale estimands, so we evaluate the direction over the fitted posterior rather

than treating it as a general property of logistic mediation models.

   When the conditional reliabilities of the first-set and control mediators differ, a reliability-

matched control multiplies the control’s point count by the factor equating the two reliabili-

ties under an inverse-variance relation; Section S2 of the supplementary material gives the

factor and its derivation. With dependent points the covariance term creates a variance

floor, so the target reliability need not be attainable at any count. That analysis is therefore

a sensitivity to the matching criterion, not a corrected primary estimate.

   The fitted summaries become causal mediation effects only under stronger conditions:

consistency, no interference, positivity, exchangeability for the exposure and mediator

relations, no unmeasured mediator–outcome confounding after conditioning on ability and

baseline variables, no exposure-induced mediator–outcome confounder, and the required

temporal ordering (Robins & Greenland 1992, Pearl 2001, Imai, Keele & Tingley 2010,

VanderWeele 2015). The expanding-window construction ensures that θ− uses only earlier

seasons. A first-set mediator is earlier than the final result but still belongs to that

outcome window; only the second-set analysis places it entirely before the modeled outcome.

Neither rules out an unobserved match-level shock, such as injury, fatigue or changing court

conditions, affecting both performance and outcome, which we examine through sensitivity

analysis rather than treat as identified. Latent ability is also a model-defined exposure


                                               20
rather than a manipulable treatment. Absent those conditions and a defensible intervention

interpretation, (17)–(19) are surface-specific structural pathway summaries.

   Leaving one match out of the ability analysis would not resolve this. It would keep that

match from contributing to its own ability estimate, but gives neither independence from

persistent form, health, scheduling and opponent selection nor an exclusion restriction, and

past results may act on later ones through seeding, confidence and preparation. Expanding-

window estimation preserves temporal ordering; it does not create an instrument. Proofs,

the stopping-time counterexample and the reliability calculations are in Sections S2 and S14

of the supplementary material.


3.4    Posterior computation

Both stages are sampled with a purpose-written Hamiltonian Monte Carlo implementation

using analytic gradients (Neal 2011, Betancourt 2017) and unconstrained parameters: the

zero-sum restrictions in (4) are imposed through orthonormal Helmert bases, the surface

specialization has a noncentred representation avoiding the funnel geometry induced by its

hierarchical scale, and the sign-restricted coefficients are sampled on the log scale with the

required Jacobian terms. The step size is adapted by dual averaging and a diagonal metric

is estimated over expanding warmup windows (Hoffman & Gelman 2014); all adaptation

ends with warmup, so the retained iterations come from a fixed kernel with a Metropolis

correction.

   Computation follows the modular structure in (13). For each target season the ability

model is fitted to earlier seasons only, and the cut posterior for the pathway parameters is

approximated by refitting the pathway model conditional on each of K retained ability draws

and pooling the conditional samples. In the point-count-matched arm a different control

realization is paired with each ability draw and standardized within surface before fitting,

so the pooled sample propagates uncertainty in pre-match ability and in the points drawn


                                             21
to build the mediator. At no stage can the pathway data update the ability distribution.

   Pathway summaries are computed by g-computation: residual mediator contrasts are

drawn once and reused across ability interventions, (17)–(19) are evaluated by Monte Carlo,

and the mediated share is formed within each draw rather than as a ratio of posterior means.

Contrasts among constructions use (14), with the same ability draw and g-computation

random numbers in each arm but conditionally independent pathway draws. The coupling

propagates common ability uncertainty without estimating the residual covariance induced

by reusing the same outcomes; repeated-sampling calibration is examined in simulation

instead. The full parameterization, leapfrog and adaptation settings, priors and prior

predictive checks, gradient verification and convergence diagnostics are in Sections S4–S6 of

the supplementary material.


3.5    Simulation evidence

We simulate from each stage to check parameter recovery, and from the point level to check

that the decomposition responds to the two mechanisms it separates. The ability model

recovers the identified match-level predictor, with fitted log odds correlating 0.968 with the

truth at a calibration slope of 0.920, and the performance model recovers its coefficients

within Monte Carlo error. The point-level experiment builds the three mediators as the

pipeline builds them and varies two dials: γ, the weight of realized points in the outcome

equation, which is outcome overlap, and ς, a segment-level shock giving the opening set

its own latent rate, which is construct change. With both off, the window-construction

components cover zero under both outcomes. Construct change alone produces a positive

match-outcome component with no overlap present. Overlap alone moves the component

only when the outcome follows the first set, because with conditionally independent points

the opening set and the control coincide under the match outcome, a property of the

generator rather than a finding. Over four repeated-sampling cells the estimator is close to


                                             22
unbiased with conservative 90% intervals: where the truth is zero, an interval excludes it in

0–2% of datasets against a nominal 10%. Section S7 of the supplementary material gives

the design, the full grid (Table S3) and the calibration study (Table S4).



4     Real data analysis
This section applies the methodology of Sections 3 to eleven seasons of professional tennis.

The application serves two purposes. First, it is a case study in the practical question

that motivates the paper: when an analyst decomposes the effect of pre-match ability

into a pathway through in-match performance, how much of the answer is driven by

how the performance mediator is constructed rather than by the sport itself? Second,

it demonstrates that the proposed control construction, the comparison distribution in

(14), and the reliability diagnostics can all be computed from data that national tours,

broadcasters, and analytics departments already collect, and that they yield findings with

direct consequences for how performance statistics are used in the sport.


4.1    Ability estimates and predictive performance

Figure 3 shows how the leading surface-specific abilities evolved. The leading players are

similar across surfaces but the ordering is not identical, which quantifies, with posterior

uncertainty, how far “the best player” is a surface-dependent statement. Partial pooling is

most visible on grass, where the shorter calendar carries less information. The five highest

posterior means on each surface, with intervals and match counts, are in Table S8 of the

supplementary material.

    The pathway analysis conditions on pre-match abilities, so those abilities must be

demonstrably competitive as forecasts, though they need not be the best available forecaster.

Scored on the untouched portion of the 2026 season, the model attains the lowest log

loss and Brier score and the highest accuracy among seven comparators (Table S7 of


                                             23
the supplementary material). Paired per-match t-statistics separate it clearly from the

frozen Elo, the surface-blended Elo and the static Bradley–Terry model (t = 3.80, 2.62

and 3.53), but not from either ranking baseline (t = 1.06 frozen, 0.32 with live ranks) or

the prequentially updated Elo (t = 1.24). The hold-out also runs only to late spring and

contains no grass-court matches, so the grass ratings are not tested out of sample, and

two comparators read the hold-out season while the model is frozen at the end of 2025;

Section S9 of the supplementary material gives both features in full. We therefore report

this as evidence that the pre-match abilities are credible, not as a forecasting claim. Its

practical reading is that one hierarchical model, frozen at the season boundary and refit

annually, matches the day-to-day accuracy of ratings updated after every match. The

calibration slope of 0.857 indicates mild overconfidence, consistent with updating ability

between seasons rather than within them; Figure S2 of the supplementary material shows

the reliability curve.
                              Hard                           Clay                             Grass
                                                Sinner                           Alcaraz
                          5                                                                                       Alcaraz
                                                Alcaraz                          Sinner                           Sinner
 posterior mean ability




                          4                     Djokovic                         Djokovic                         Djokovic
                                                Minaur                           Zverev
                          3                                                                                       Draper
                                                Zverev                           Ruud                             Fritz
                          2
                          1
                          0
                          2015 2018 2021 2024              2015 2018 2021 2024              2015 2018 2021 2024
Figure 3: Posterior mean ability trajectories from 2015 to 2025 for the five highest-rated players
on each surface at the end of the study period.


               Two posterior predictive checks and an outlier scan appear in full in Section S8 of the

supplementary material. The model reproduces the upset rate, 0.3128 observed against

0.3122 replicated with a posterior predictive p-value of 0.440, and the fitted probabilities

are pulled inward in both tails (Table S5), the signature of hierarchical shrinkage. Ranking



                                                                    24
matches by predictive surprise returns recognisable upsets, and it surfaced a data issue rather

than a sporting one: several high-surprise results end in retirement, where the outcome is

not produced by the play the mediator measures. Section S12 of the supplementary material

refits the decomposition without them.


4.2    Pathway effects and measurement windows

Posterior summaries of the second-stage coefficients are in Table S9 of the supplementary

material. For the first-set mediator, own ability is positively and opponent ability negatively

associated with service performance, and |βsopp | is of the same order as βsown on every surface,

so both players contribute materially to the mediator. Whether the opponent term is larger

is less clear: the posterior probability that |βsopp | > βsown is 0.83 on hard, 0.87 on clay and

0.07 on grass, and the priors in Section S4 of the supplementary material place β own at

a larger location. We therefore read service performance as a property of the matchup

rather than of the server alone: a player’s serve statistics are largely a statement about who

that player has faced. That matters whenever they are compared across players who faced

opponents of different quality, and Section 4.5 develops the implication for leaderboards,

scouting and contract evaluation.

   Table 2 compares the three constructions, all fitted to the same matches with the same

pre-match abilities and outcome model and differing only in the period the mediator covers

and the number of service points behind it.

   For the temporally ordered first-set mediator the two pathways are of similar size: on

hard courts a one-standard-deviation ability advantage raises the win probability by 0.104,

of which 0.054 passes through first-set service performance and 0.050 remains direct, a

mediated share of 0.52. The full-match mediator gives a share of 0.95 and a direct effect of

0.005. Since the same service points enter the mediator and the result, that reads more

naturally as outcome overlap than as evidence that serving is the only route from ability to


                                               25
Table 2: Model-implied changes in win probability for a one-unit standardized pre-match ability
contrast, by mediator. The first two blocks are the comparison the literature would make; the
control block holds the window at the whole match while reducing the sample size to the first
set’s. Entries are posterior means with 90% credible intervals; the final column is the mediated
share of the total, with its own 90% interval.
  Surface                 Direct                Mediated                    Total   Mediated share
  First set (set-1 window, set-1 sample size)
    Hard 0.050 [0.040, 0.060] 0.054 [0.048, 0.060]           0.104 [0.092, 0.116]   0.52 [0.47, 0.58]
    Clay     0.065 [0.050, 0.080] 0.044 [0.036, 0.052]       0.109 [0.093, 0.125]   0.41 [0.33, 0.48]
    Grass 0.055 [0.033, 0.080] 0.048 [0.037, 0.060]          0.104 [0.079, 0.129]   0.47 [0.35, 0.60]
  Control (full-match window, set-1 sample size)
    Hard 0.036 [0.027, 0.045] 0.067 [0.060, 0.074]           0.103 [0.092, 0.114]   0.65 [0.59, 0.71]
    Clay    0.044 [0.030, 0.058] 0.061 [0.051, 0.071]        0.105 [0.089, 0.120]   0.58 [0.49, 0.68]
    Grass 0.047 [0.027, 0.069] 0.057 [0.042, 0.073]          0.104 [0.080, 0.128]   0.55 [0.42, 0.69]
  Full match (full-match window, full sample size)
    Hard 0.005 [0.003, 0.008] 0.101 [0.092, 0.110]           0.106 [0.096, 0.116]   0.95 [0.92, 0.97]
    Clay    0.010 [0.005, 0.017] 0.092 [0.081, 0.104]        0.103 [0.090, 0.115]   0.90 [0.84, 0.95]
    Grass 0.013 [0.006, 0.023] 0.089 [0.072, 0.107]          0.103 [0.083, 0.122]   0.87 [0.79, 0.94]

winning. The main empirical finding is therefore negative: the near-complete mediation a

full-match analysis reports, which a practitioner would read as “winning is almost entirely

serving”, reflects how the mediator is constructed rather than a property of tennis.

   The control arm splits the conventional gap into a point-count and a window-construction

component.
Table 3: Decomposition of the gap between the first-set and full-match mediators into a window-
construction component (first set → control, the window widens at fixed sample size) and a
point-count component (control → full match, the sample size grows at fixed window), with the
outcome being the match. The three share columns are posterior means; the two component
columns are posterior means with 90% credible intervals, all on the mediated-share scale. The
final column is the window-construction component as a share of the two-arm gap, formed from
posterior means; it is not an overlap share because it combines overlap with the change in the
measured construct.
   Surface      Mediated share                          Window           Point count     Window %
             set 1   control       full            component              component          of gap
   Hard      0.522    0.649    0.950       0.127 [0.053, 0.203]   0.301 [0.236, 0.364]         30%
   Clay      0.405    0.582    0.899       0.177 [0.066, 0.288]   0.317 [0.213, 0.420]         36%
   Grass     0.473    0.553    0.872      0.080 [-0.090, 0.247]   0.319 [0.173, 0.464]         20%


   The control spans the whole match, so it carries whatever outcome overlap the conven-

tional mediator carries, but is computed from the opening set’s number of service points;

                                                   26
under Proposition 2 it also has the first-set mediator’s conditional error variance. On

hard courts its mediated share is 0.65, between the other two, with a window-construction

component of 0.127 [0.053, 0.203] and a point-count component of 0.301 [0.236, 0.364]. The

window-construction component is the smaller part of what the conventional comparison

reports, between 20% and 36% of the gap depending on surface, so most of the apparent

difference between an early-window and a full-match analysis is the arithmetic of counting

more points. How much of it is outcome overlap this design does not say, since the compo-

nent combines overlap with a change in the measured construct. Clay shows the largest

component and grass the least precise estimate, as the sample sizes lead one to expect.

   Intervals for these contrasts use the comparison distribution in (14), so they quantify

uncertainty under that stated coupling rather than estimating a covariance identified by

a joint model for the three mediators. Repeated-sampling behavior under the simulation

generator and the pooling construction are in Sections S7.3 and S11 of the supplementary

material.

   Conditional on the complete point record the control is an unbiased subsample of the

raw full-match proportion with binomial sampling variance close to the first-set statistic’s,

which supports the point-count comparison without identifying a pure measurement-error

effect. We therefore report both quantities as construction contrasts.

   The window-construction component is smaller than the overlap intuition suggests, for

a reason that transfers beyond tennis. The outcome is who won the match and the first set

is part of that match, so a first-set mediator is earlier than the end of the outcome but not

outside it: its points are among those that decide the thing being explained. Widening the

window moves the mediator from one region inside the outcome to a larger region inside the

same outcome, adding overlap to a baseline that was never overlap-free. Temporal ordering

and freedom from outcome overlap are therefore distinct properties of a mediator, and an

analysis can have the first without the second.


                                             27
4.3    Temporal ordering, robustness, and replication

Because a first-set mediator is observed earlier than the match result but remains part

of it, we repeat the decomposition with the outcome defined as winning the second set.

The mediator is then entirely prior to the modeled outcome, while the control still samples

the full match, including second-set points. This is a positive-control analysis for outcome

overlap, not an estimate of how much overlap occurs naturally.

   The window-construction component grows when the outcome moves outside the first-set

window. On hard courts it rises from 0.127 [0.053, 0.203] for the match outcome to 0.311

[0.229, 0.396] for the second-set outcome, about two-and-a-half-fold, and the clay-court

estimate is 0.328 [0.217, 0.442]. The pattern is consistent with outcome overlap, though it

does not identify overlap separately from changes in performance across sets. It shows how

far the placement of the outcome window can move a mediated share.

   The conclusion is similar after splitting matches by tournament round, excluding re-

tirements and walkovers, replacing the expanding-window exposure with a retrospective

ability estimate, and perturbing the mediator–outcome association with an unmeasured

match-level shock; permuting outcomes within surface removes both components. These

checks cannot remove selection into the charted sample or establish the causal assumptions

of Section 3.3; Section S12 of the supplementary material gives every estimate.

   The analysis was repeated independently for the WTA tour with 26,591 ability matches

and 2,332 linked pathway matches. Against the match outcome the hard-court window-

construction component is 0.109 [−0.004, 0.223], against 0.127 [0.053, 0.203] for the ATP

sample; against the second-set outcome it rises to 0.316 [0.192, 0.436]. The replication

reproduces both the direction of the decomposition and its dependence on whether the

mediator lies inside the modeled outcome window. The tours differ in playing style, calendar

and match format at the largest events, so the agreement suggests these construction effects



                                            28
belong to the analytic design rather than to one tour.

   Historical ability is thus associated with subsequent service performance, and both with

match results. The much larger mediated share from full-match performance is not evidence

that serving is the only route from ability to winning; it reflects a mediator measured

with more points and over a period overlapping the outcome, and the control construction

diagnoses both changes without assigning a causal share to either.


4.4    Reliability analysis without point-level data

When only an aggregate performance statistic and its denominator are available, the errors-

in-variables approximation in (21) is a diagnostic rather than a generally valid correction.

We estimate the sampling variance by p(1 − p)/n and compare it with the residual mediator
           2
variance 2σX (1 − ρ), which assumes conditionally independent Bernoulli points and a fixed

count, though tennis points are dependent and the number played is outcome-dependent.

   Table S18 of the supplementary material shows why equal point counts should not be

called equal reliability, which matters because matching on sample size is the default fairness

criterion in applied work. The control has nearly the first-set mediator’s plug-in sampling

variance but lower conditional reliability on every surface, because the two constructions

differ in signal variation. Equal n does not imply equal information, so the point-count

component is not an identified measurement-error effect. Matching reliability instead moves

the hard-court window-construction component from 0.127 to 0.215 and the clay-court

component from 0.177 to 0.329, which we report as sensitivity to the matching criterion,

not as a corrected decomposition.

   The regression-calibration diagnostic is


                                               λ
                                               b
                                                 s
                                  Ds = cbs −       gs (1 − κs ),                          (22)
                                               κs


the implied direct coefficient after attenuation correction. It is negative in 10 of the 12

                                               29
mediator-by-surface cells, so the approximation is incompatible with the positive-direct-effect

restriction in most fitted configurations. An unrestricted hard-court refit reinforces the

warning: the full-match direct coefficient is −0.091 [−0.175, −0.009] and the mediated share

is 1.07, while the first-set estimate is essentially unchanged. A share above one signals that

the restricted model is at its boundary, so the near-boundary full-match share is sensitive

to the restriction and prior rather than evidence of complete mediation.

   Section S14 of the supplementary material gives the reliability derivation, correction

validation, unrestricted fits, reliability-matched decompositions and fixed-point calculations.

Across all reported configurations the maximum rank-normalized split-R
                                                                     b is 1.012, the

minimum bulk effective sample size is 720, and no divergent transitions occur among

retained draws (Section S6 of the supplementary material).


4.5    Implications for the sports industry

Four consequences follow from the results rather than from sporting intuition. First,

because |βsopp | is of the same order as βsown (Section 4.2), a serve percentage is partly a

statement about the opponent, so leaderboards quoting it without opponent adjustment

let schedule imbalance confound any comparison or performance clause built on them; the

fitted coefficients supply the adjustment, with posterior uncertainty, from abilities the model

already produces. Second, ranking matches by predictive surprise (Section 4.1) screens a

data-quality or integrity pipeline, and here it surfaced retirements, which are censoring

events rather than sporting anomalies. Third, the decomposition of Section 4.2 cautions any

mediation-style analysis whose mediator is measured on a window overlapping the outcome:

the mediated share rose by a factor of 1.6 to 2.2 between the first-set and full-match

constructions across both tours and all surfaces, and matching on sample size does not

fix it, since equal counts are not equal reliability (Table S18). The diagnostic needs only

the same data, re-windowed, and the ATP–WTA agreement suggests it transfers to other


                                              30
sports recorded as sequences of within-contest events. Fourth, the hold-out comparison of

Section 4.1 shows a pooled rating frozen at the season boundary to be indistinguishable in

accuracy from ratings updated after every match, which matters where continuous updating

is an operational liability.



5     Discussion
When a mediator is measured cannot be separated from how precisely it is measured. Full-

match service performance rests on more points than first-set performance, so comparing

the two confounds timing with precision. The point-count-matched control pulls them apart:

against the full-match mediator it isolates a point-count component, and against the first-set

mediator it holds the count fixed and isolates the remaining window-construction component.

Reading the first contrast as pure measurement precision requires the assumptions of

Section 3.3. In our data the point-count component is the larger, but the window component

still matters and its meaning is ambiguous, mixing mediator–outcome overlap with real

changes in performance across sets. The second-set analysis makes that concrete: a mediator

recorded earlier in a match is not necessarily measured before the outcome. Timing and

precision are distinct design choices, and both shape the pathway an analyst will attribute

to performance.

    These conclusions come with limits. The Match Charting Project is a volunteer archive

that over-covers prominent players and marquee matches, so the linked sample is not

representative of professional tennis, and cross-round comparisons cannot rule out selection

because every match comes from the same archive. The simulation reproduces the expected

behavior of the decomposition but simplifies outcome-dependent match length, dependence

among points and the imputation procedure. Unmeasured match-level shocks remain

possible; the sensitivity analysis probes them but the data do not identify them. The model

holds surface specialization fixed and lets ability move only between seasons. Finally, the


                                             31
modular procedure targets a cut posterior, which protects the pre-match meaning of ability

but whose frequentist calibration need not match a joint posterior’s.

    Point-level records would let mediators be built over progressively longer stretches of a

match, tracing the pathway as the window widens; serving, returning and pressure-point

performance could be separate mediators; ability and specialization could evolve within a

season. More broadly, studies using temporally aggregated mediators should treat their

construction as part of the inferential design: report the number of contributing observations,

compare windows at a common precision, and measure the mediator outside the outcome

window when a temporal interpretation is intended. Without these safeguards, a change

in the mediated effect may come from measurement error, temporal overlap, a shifting

construct, or all three at once.



6     Data Availability Statement
The match results and point-level charting records analysed here are publicly available from

the archives maintained by Jeff Sackmann under a CC BY-NC-SA 4.0 licence (Sackmann

2026a,c,b). The code that downloads the data, records their provenance, fits both stages and

generates every reported table, figure and value accompanies the supplementary material.


                       SUPPLEMENTARY MATERIAL

Supplementary material: Sections S1–S14: data linkage, proofs, the control mediator,

priors, posterior computation and diagnostics, simulation details, model checking, the

forecast comparison, additional empirical results, interval construction, robustness and

sensitivity checks, and the reliability analysis.

Reproduction archive: Python code for data preparation, both model stages, the sim-

ulations and every table and figure; the fitted result archives; and a provenance manifest

with the URL, retrieval date and SHA-256 digest of every downloaded file. (zip)

                                              32
References
Barnett, T. & Clarke, S. R. (2005), ‘Combining player statistics to predict outcomes of
  tennis matches’, IMA Journal of Management Mathematics 16(2), 113–120.

Baron, R. M. & Kenny, D. A. (1986), ‘The moderator–mediator variable distinction in social
  psychological research: Conceptual, strategic, and statistical considerations’, Journal of
  Personality and Social Psychology 51(6), 1173–1182.

Bayarri, M. J., Berger, J. O. & Liu, F. (2009), ‘Modularization in Bayesian analysis, with
  emphasis on analysis of computer models’, Bayesian Analysis 4(1), 119–150.

Betancourt, M. (2017), ‘A conceptual introduction to Hamiltonian Monte Carlo’, arXiv
  preprint arXiv:1701.02434 .

Blackburn, M. L. (2013), ‘Ranking the performance of tennis players: an application to
  women’s professional tennis’, Journal of Quantitative Analysis in Sports 9(4), 367–378.

Bozóki, S., Csató, L. & Temesi, J. (2016), ‘An application of incomplete pairwise comparison
  matrices for ranking top tennis players’, European Journal of Operational Research
  248(1), 211–218.

Bradley, R. A. & Terry, M. E. (1952), ‘Rank analysis of incomplete block designs: I. the
  method of paired comparisons’, Biometrika 39(3/4), 324–345.

Carroll, R. J., Ruppert, D., Stefanski, L. A. & Crainiceanu, C. M. (2006), Measurement
 Error in Nonlinear Models: A Modern Perspective, 2 edn, Chapman & Hall/CRC, Boca
  Raton.

Cattelan, M., Varin, C. & Firth, D. (2013), ‘Dynamic Bradley–Terry modelling of sports
  tournaments’, Journal of the Royal Statistical Society: Series C (Applied Statistics)
  62(1), 135–150.

Cinelli, C. & Hazlett, C. (2020), ‘Making sense of sensitivity: Extending omitted variable
  bias’, Journal of the Royal Statistical Society: Series B 82(1), 39–67.

Dong, P., Han, R., Jiang, B. & Xu, Y. (2026), ‘Statistical ranking with dynamic covariates’,
 Journal of the Royal Statistical Society Series B: Statistical Methodology 88(1), 221–238.

Glickman, M. E. (1999), ‘Parameter estimation in large dynamic paired comparison experi-
  ments’, Journal of the Royal Statistical Society: Series C 48(3), 377–394.

Glickman, M. E. & Stern, H. S. (1998), ‘A state-space model for national football league
  scores’, Journal of the American Statistical Association 93(441), 25–35.


                                            33
Hoffman, M. D. & Gelman, A. (2014), ‘The no-U-turn sampler: Adaptively setting path
 lengths in Hamiltonian Monte Carlo’, Journal of Machine Learning Research 15, 1593–
 1623.

Hunter, D. R. (2004), ‘MM algorithms for generalized Bradley–Terry models’, The Annals
 of Statistics 32(1), 384–406.

Imai, K., Keele, L. & Tingley, D. (2010), ‘A general approach to causal mediation analysis’,
  Psychological Methods 15(4), 309–334.

Imai, K., Keele, L. & Yamamoto, T. (2010), ‘Identification, inference and sensitivity analysis
  for causal mediation effects’, Statistical Science 25(1), 51–71.

Ingram, M. (2019), ‘A point-based Bayesian hierarchical model to predict the outcome of
  tennis matches’, Journal of Quantitative Analysis in Sports 15(4), 313–325.

Jacob, P. E., Murray, L. M., Holmes, C. C. & Robert, C. P. (2017), ‘Better together?
  Statistical learning in models made of modules’, arXiv preprint arXiv:1708.08719 .

Klaassen, F. J. G. M. & Magnus, J. R. (2001), ‘Are points in tennis independent and
  identically distributed? Evidence from a dynamic binary panel data model’, Journal of
 the American Statistical Association 96(454), 500–509.

Kovalchik, S. A. (2016), ‘Searching for the GOAT of tennis win prediction’, Journal of
 Quantitative Analysis in Sports 12(3).

Kovalchik, S. A. (2020), ‘Extension of the Elo rating system to margin of victory’, Interna-
 tional Journal of Forecasting 36(4), 1329–1341.

Lopez, M. J., Matthews, G. J. & Baumer, B. S. (2018), ‘How often does the best team win?
  A unified approach to understanding randomness in North American sport’, The Annals
  of Applied Statistics 12(4), 2483–2516.

Neal, R. M. (2011), MCMC using hamiltonian dynamics, in S. Brooks, A. Gelman, G. L.
 Jones & X.-L. Meng, eds, ‘Handbook of Markov Chain Monte Carlo’, Chapman and
  Hall/CRC, Boca Raton, FL, pp. 113–162.

Pearl, J. (2001), Direct and indirect effects, in ‘Proceedings of the Seventeenth Conference on
  Uncertainty in Artificial Intelligence’, Morgan Kaufmann, San Francisco, CA, pp. 411–420.

Plummer, M. (2015), ‘Cuts in Bayesian graphical models’, Statistics and Computing
  25(1), 37–43.

Prieto-Lage, I., Paramés-González, A., Torres-Santos, D., Argibay-González, J. C., Reguera-


                                              34
  López-de-la Osa, X. & Gutiérrez-Santiago, A. (2023), ‘Match analysis and probability of
  winning a point in elite men’s singles tennis’, PLOS ONE 18(9), e0286076.

Radicchi, F. (2011), ‘Who is the best player ever? A complex network analysis of the history
  of professional tennis’, PLoS ONE 6(2), e17249.

Reid, M., McMurtrie, D. & Crespo, M. (2010), ‘The relationship between match statistics
  and top 100 ranking in professional men’s tennis’, International Journal of Performance
 Analysis in Sport 10(2), 131–138.

Robins, J. M. & Greenland, S. (1992), ‘Identifiability and exchangeability for direct and
 indirect effects’, Epidemiology 3(2), 143–155.

Robins, J. M., Hernán, M. Á. & Brumback, B. (2000), ‘Marginal structural models and
 causal inference in epidemiology’, Epidemiology 11(5), 550–560.

Rubin, D. B. (1987), Multiple Imputation for Nonresponse in Surveys, John Wiley & Sons,
  New York.

Sackmann, J. (2026a), ‘ATP tennis rankings, results, and stats’, Data set. Archival
  mirror, https://github.com/Aneeshers/tennis-sackmann-archive; originally https:
  //github.com/JeffSackmann/tennis_atp. CC BY-NC-SA 4.0. Retrieved 2026-09-10.

Sackmann, J. (2026b), ‘The match charting project’, Data set, https://github.com/
  JeffSackmann/tennis_MatchChartingProject. CC BY-NC-SA 4.0. Retrieved 2026-09-
  10.

Sackmann, J. (2026c), ‘WTA tennis rankings, results, and stats’, Data set. Archival
  mirror, https://github.com/Aneeshers/tennis-sackmann-archive; originally https:
  //github.com/JeffSackmann/tennis_wta. CC BY-NC-SA 4.0. Retrieved 2026-09-10.

Suissa, S. (2008), ‘Immortal time bias in pharmacoepidemiology’, American Journal of
  Epidemiology 167(4), 492–499.

VanderWeele, T. J. (2010), ‘Bias formulas for sensitivity analysis for direct and indirect
  effects’, Epidemiology 21(4), 540–551.

VanderWeele, T. J. (2015), Explanation in Causal Inference: Methods for Mediation and
  Interaction, Oxford University Press, New York.

Zermelo, E. (1929), ‘Die berechnung der turnier-ergebnisse als ein maximumproblem der
  wahrscheinlichkeitsrechnung’, Mathematische Zeitschrift 29(1), 436–460.




                                            35

