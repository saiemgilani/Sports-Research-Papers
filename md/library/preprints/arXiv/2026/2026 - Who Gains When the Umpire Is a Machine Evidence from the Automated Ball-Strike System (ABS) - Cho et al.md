<!-- source: 2026 - Who Gains When the Umpire Is a Machine Evidence from the Automated Ball-Strike System (AB - Cho, Lee.pdf -->
<!-- arXiv:2610.27576 · machine conversion (pdftotext -layout), equations/tables/figures not preserved; licence cc-by permits redistribution -->

# Who Gains When the Umpire Is a Machine? Evidence from the Automated Ball-Strike System (ABS)

**Seung Jin Cho, Jun Yeong Lee**

arXiv:[2610.27576](https://arxiv.org/abs/2610.27576) · 2026-10-27 ingest · licence: cc-by

## Analysis (N/P/R = 8/7/5 = 20/30)

Clean applied-economics read on algorithmic umpiring: the key move is decomposing the change into *removal of discretion* (rents worth a few runs per player-season) versus *new zone geometry* (height-scaled zone shifts strikes toward tall batters), and showing exposure is low so plate-appearance effects are near zero. Adaptation finding (pitchers throw higher, batters do not adjust) is the most actionable for MLB's own ABS challenge system. Data are public KBO pitch tracking but the source changed its reference point on 16 July 2026 (55 ft vs 50 ft), which the authors handle; replication needs that care. No code stated.

Summary: KBO 2024 automated ball-strike rollout, 1M+ pitches 2021-26: separates removed discretion (count effects, framing, star-batter edge, a few runs per player-season) from new zone geometry (more strikes for tall batters; PA effects near zero); pitchers adapted by throwing higher, batters did not.

---

## Extracted text

```text
                                                         Who Gains When the Umpire Is a Machine?

                                                Evidence from the Automated Ball-Strike System (ABS)

                                                                                 Seung Jin Cho
                                                                  Department of Economics, Dankook University
                                                                          ORCID: 0000-0003-1313-0296
arXiv:2610.27576v1 [econ.GN] 20 Oct 2026




                                                                                 Jun Yeong Lee
                                                                             Pusan National University
                                                                          ORCID: 0000-0002-8905-3760


                                           Contact information

                                           Seung Jin Cho
                                           Department of Economics, Dankook University
                                           152 Jukjeon-ro, Suji-gu, Yongin-si, Gyeonggi-do 16890, Republic of Korea
                                           Tel: +82-31-8005-3392 Email: seungjin.cho@dankook.ac.kr

                                           Jun Yeong Lee (corresponding author)
                                           Room 803, Economics and International Commerce Building, Pusan National University
                                           2 Busandaehak-ro 63beon-gil, Geumjeong-gu, Busan 46241, Republic of Korea
                                           Tel: +82-51-510-7054 Email: junyeonglee@pusan.ac.kr




                                           October 21, 2026
                     Who Gains When the Umpire Is a Machine?

             Evidence from the Automated Ball-Strike System (ABS)


Abstract

In 2024 the Korea Baseball Organization became the first top-tier league to replace the home-plate
umpire’s ball–strike judgment with an automated system. Using over a million pitches from 2021
to 2026, we separate the change into the removal of human discretion and the imposition of a
new zone geometry. The machine eliminated count-dependent calls, the value of catcher framing
and a small advantage for star batters, rents worth only a few runs per player-season. Because the
machine’s zone scales with height and treats every matchup alike, it redistributed strikes toward
tall batters and across matchups; but few pitches are exposed to these changes, and their effects on
plate-appearance outcomes are precisely estimated and close to zero. Pitchers re-optimized quickly
by throwing higher, with left-handers catching up to an existing trend, whereas we find no evidence
that batters adjusted. The results suggest that the incidence of replacing human judgment with a
rule depends on its geometry and on exposure.

Keywords: automated ball-strike system; algorithmic decision-making; evaluator bias; rents;
adaptation
JEL classification: Z22, J24, D83, O33




                                                 1
1    Introduction

Algorithms increasingly replace human judgment in decisions about people, from hiring and
lending to bail and grading. A large literature asks whether such algorithms decide better than the
humans they replace (Hoffman, Kahn, & Li, 2018; Kleinberg, Lakkaraju, Leskovec, Ludwig, &
Mullainathan, 2018). Less is known about what the replacement does to the people being evaluated.
Removing human discretion should eliminate the advantages that discretion created, but a rule also
has a shape. The shape determines who gains and who loses, and those affected may or may not
change their behavior in response. Answering these questions requires a setting in which every
decision is recorded, the rule that replaces human judgment is known, and the behavior of those
being evaluated can be observed before and after the change.
    Professional baseball offers such a setting. Every pitch is tracked, every ball–strike call (the
umpire’s ruling on a pitch the batter does not swing at) is recorded, and the call is the outcome
of a judgment that, until recently, was made by a human umpire. In 2024 the Korea Baseball
Organization (KBO) became the first top-tier professional league to hand that judgment entirely
to an automated ball-strike system (ABS). The ABS calls a strike whenever any part of the ball
passes through a rectangle defined by each batter’s registered height. We study this change using
every regular-season pitch thrown in the KBO from 2021 to 2026, more than a million pitches. We
combine the pitches with the tracking system’s trajectories, the umpires assigned to each game, and
the catcher on the field for each pitch.
    We organize the analysis around a simple decomposition. Relative to a human umpire, the
machine changes calls in two ways. It removes the discretionary component of human judgment,
that is, the part of the call that responds to context such as the count (the number of balls and
strikes so far in the plate appearance), the batter’s reputation or the catcher’s receiving skill. It also
imposes a new geometry, the difference between the zone the rule defines and the zone humans
actually called. The first component is a set of rents created by the evaluator; the second is a
redistribution chosen by the rule’s designers. To a first approximation, the economic incidence of
either component equals the number of calls it changes per plate appearance (a batter’s turn at bat)

                                                    2
times the value of a ball relative to a strike. Finally, those affected should adapt only when the gain
from adapting exceeds its cost.
   Three sets of findings emerge. First, the machine removed the rents created by human discretion.
On border pitches, those close to the edge of the zone, human umpires were 6.1 percentage points
more likely to call a strike when the batter was ahead in the count (2-0, 3-0 or 3-1) and 6.7 points
less likely with two strikes; neither adjustment is detectable under the ABS. Catcher framing, the
skill of receiving pitches so that umpires call them strikes, was persistent under human umpires,
with split-half reliabilities between 0.60 and 0.81, and it became indistinguishable from noise under
the machine. Human umpires also gave star batters slightly fewer called strikes on border pitches,
although the size of this effect depends on how finely location is held fixed. Valued at what a strike
costs the batting team in expected runs, these rents amounted to a few runs per catcher-season and
about one run per star batter-season.
   Second, the geometry of the rule redistributed strikes along two margins, but the redistribution
had little effect on outcomes. Because the human zone was anchored in absolute height while the
machine’s zone scales with registered height, the ABS moved strikes toward taller batters at the top
of the zone: relative to the human zone, each centimeter of height added 0.75 percentage points to
the share of a batter’s high pitches that were called strikes. Because human umpires treated pitcher–
batter matchups asymmetrically, the machine also moved strikes between handedness matchups at
the edges. Few pitches are exposed to these changes, however. The extra strikes amount to at most
one in every 23 plate appearances, and ten centimeters of height change the probability that a plate
appearance reaches two strikes or three balls, one call away from a strikeout or a walk, by less than
two percentage points.
   Third, pitchers adapted and batters did not. Using the change in each location’s value under the
machine as a measure of treatment intensity, we find that pitchers reallocated their pitches toward
locations the ABS favored, quickly and almost entirely through pitch height. The acceleration at
the time of the ABS comes from left-handed pitchers. Right-handed and side-arm pitchers (those
who throw with a low, sideways arm angle) had already been raising their pitches before 2024,


                                                  3
whereas left-handed pitchers had not, and they caught up within a season. For batters, by contrast,
we detect no change in swing decisions, either in response to the new geometry or to the end of
count-dependent calls. This asymmetry is consistent with a simple cost of re-optimization. A
pitcher’s plan is set in advance and applies to every batter, whereas a batter decides in real time,
and the stakes for any one batter are small.
   The paper contributes to four literatures. A body of work in economics and management
documents that human evaluators in sport are influenced by race (Hamrick & Rasp, 2015; Parsons,
Sulaeman, Yates, & Hamermesh, 2011; Price & Wolfers, 2010; Tainsky, Mills, & Winfree, 2015),
status (Kim & King, 2014; Mills, 2014), nationality (Zitzewitz, 2006), the sequence of past decisions
(Chen, Moskowitz, & Shue, 2016), the count (MacMahon & Starkes, 2008), and the home crowd
(Dohmen, 2008; Garicano, Palacios-Huerta, & Prendergast, 2005; Hsu, 2024; Sutter & Kocher,
2004), and that the quality of their judgment varies with working conditions (Fesselmeyer, 2021). A
related set of studies shows that these biases respond to the evaluator’s environment: favoritism fell
when referees became full-time professionals (Rickman & Witt, 2008) and when referees became
aware of their bias (Pope, Price, & Wolfers, 2018), and pitch-tracking technology changed how
umpires called the zone (Bradbury, 2019; Hunter, 2018; Mills, 2017). These studies observe human
evaluators under different incentives and degrees of scrutiny. We observe the complete replacement
of the evaluator, which allows us to measure the rents that discretion created and to test whether they
vanish. Our results also relate to the economics of algorithmic decision-making (Hoffman et al.,
2018; Kleinberg et al., 2018). That literature compares the quality of human and machine decisions.
We show that the distributional consequences of replacing humans with a rule are governed by the
rule’s geometry and by exposure, and that those evaluated by the rule may not adapt to it. Third,
we add to the evidence on how professional agents adjust their strategies when payoffs change.
Some studies find that professionals play close to optimally (Abramitzky, Einav, Kolkowitz, &
Mill, 2012; Chiappori, Levitt, & Groseclose, 2002; Palacios-Huerta, 2003; Walker & Wooders,
2001) and change their strategies as theory predicts when the rules change (Banerjee, Swinnen, &
Weersink, 2007), while others document persistent departures from optimal play (Kovash & Levitt,


                                                  4
2009; Romer, 2006). That pitchers adapted to the ABS while batters did not suggests that which
pattern prevails depends on how much an agent stands to gain from re-optimizing. Finally, we build
on recent studies of the ABS itself. Lee, Han, and Ko (2025) describe how the zone changed in the
first half of 2024, and Lee and Ko (2026) show that count-dependent calls disappeared, a result we
replicate. Song, Kang, and Paulsen (2026) attribute a decline in star batters’ performance after the
ABS to the loss of umpire favoritism. We find evidence of this favoritism at the level of individual
calls, but its value appears small, and much of the decline in outcomes appears to reflect the choice
of a single pre-ABS season as the baseline.
    The rest of the paper proceeds as follows. Section 2 develops the conceptual framework and the
hypotheses. Section 3 describes the institutional setting and the data, and Section 4 the empirical
strategy. Section 5 presents the results and their robustness, and Section 6 concludes.



2     Conceptual Framework and Hypotheses

2.1    Setup

Consider a pitch that the batter does not swing at, a taken pitch. It crosses the middle plane of
home plate at location ℓ (horizontal position and height), is thrown to a batter of registered height
ℎ, and arrives in a context 𝜃. The context comprises the count, the batter’s reputation, the catcher,
and the home-plate umpire. The evaluator calls a strike with probability 𝑆(ℓ, ℎ, 𝜃).
    Under a human umpire, 𝑆 𝐻 (ℓ, ℎ, 𝜃) is a smooth function of location. It may also depend on the
context, through count adjustments, deference to reputation, or the catcher’s receiving skill, and it
need not scale with the batter’s height. Under the ABS, the call is the indicator


                                     𝑆 𝑀 (ℓ, ℎ) = 1{ℓ ∈ 𝑍 (ℎ)}.                                  (1)


Here 𝑍 (ℎ) is the zone defined by the league’s rules (Korea Baseball Organization, 2026). Its
vertical bounds are fixed fractions of registered height, and its width is the plate (43.18 cm) plus


                                                 5
2 cm on each side; Section 3 gives the details. By construction, 𝜕𝑆 𝑀 /𝜕𝜃 = 0. The switch from 𝑆 𝐻
to 𝑆 𝑀 in 2024 is the shock we study.
   Let 𝑣 𝑠 (𝜃) and 𝑣 𝑏 (𝜃) be the batter’s expected plate-appearance value after a called strike and after
a called ball in count 𝜃, and let Δ𝑣(𝜃) = 𝑣 𝑏 (𝜃) − 𝑣 𝑠 (𝜃) > 0. We estimate 𝑣 from 2022–2023 plate
appearances, measuring the value of a plate appearance by weighted on-base average (wOBA),
which weights each outcome (walk, single, home run and so on) by its average contribution to run
scoring and gives outs a weight of zero. We call the weight of a plate appearance’s final outcome
its plate-appearance value; a player’s wOBA is the average of these values. On average, one strike
is worth 0.135 runs.


2.2    Two components of the shock

Let 𝑆¯ 𝐻 (ℓ, ℎ) be the human call probability averaged over contexts. The change in the call probability
for a given pitch decomposes into


           𝑆 𝑀 (ℓ, ℎ) − 𝑆 𝐻 (ℓ, ℎ, 𝜃) = 𝑆 𝑀 (ℓ, ℎ) − 𝑆¯ 𝐻 (ℓ, ℎ) − 𝑆 𝐻 (ℓ, ℎ, 𝜃) − 𝑆¯ 𝐻 (ℓ, ℎ) .
                                                                                           
                                                                                                      (2)
                                       |          {z            } |            {z             }
                                               geometric                   discretionary


The geometric component reflects the difference between the rule’s zone and the human zone. It
varies only with location, height and handedness, and it is a redistribution chosen by the rule’s
designers. The discretionary component is the part of human judgment that responds to context,
and the machine sets it to zero. It is a set of rents created by the human evaluator: deference to
stars, adjustments to the count, and the value of a catcher’s ability to influence calls.


2.3    Hypotheses

Our first hypothesis, H1, is that the machine removes discretion. Holding location fixed, called-
strike probabilities under the ABS do not depend on the count, the batter’s reputation or the catcher.
The pre-ABS size of each context effect measures a rent that the machine removes. Catcher framing



                                                    6
is a skill whose value comes from the evaluator’s errors, so it should be a persistent catcher attribute
before the ABS and indistinguishable from noise after it.
   The second hypothesis, H2, is that the geometric incidence of the change follows the rule’s
design. Because 𝑍 (ℎ) scales with registered height and is symmetric across handedness, the ABS
shifts strikes toward tall batters at the top of the zone. It also removes any handedness asymmetry
in the human zone.
   The third hypothesis, H3, is that the economic incidence of the change equals exposure times
price. To first order, the change in a batter’s expected plate-appearance value is

                                       ∑︁
                        Δ𝑉 ≈ −                     Δ𝑆(ℓ, ℎ, 𝜃) Δ𝑣(𝜃) = −𝐸 × Δ𝑣,                     (3)
                                   taken pitches


where 𝐸 is the number of calls per plate appearance that the shock flips. Large changes in call
probabilities therefore translate into small changes in outcomes when the affected pitches are rare.
Where we observe an outcome change for a group, the call channel in (3) bounds the part of that
change attributable to the ABS.
   The fourth hypothesis, H4, concerns pitchers, who should reallocate their pitches toward
locations whose value rose, with partial adjustment. We divide the plate into five vertical bands
(the three thirds of the ABS zone and the areas above and below it) and five horizontal bands (the
three thirds of its width and the areas beyond each side). A cell 𝑐 is a pitch type (fastball, slider,
curveball and so on) in one of the 25 resulting areas, and 𝑠𝑡 (𝑐) is the share of that pitch type’s
pitches thrown to the area in season 𝑡. The ABS changes the value of cell 𝑐 by its mechanical
shock 𝐺 (𝑐), the change in the cell’s value to the pitcher, in wOBA points per 1,000 pitches, when
its 2022–2023 called pitches are re-judged by the ABS rule with behavior held fixed. We model
usage as partial adjustment toward a target, the reduced form implied by convex adjustment costs
(Gould, 1968; Lucas, 1967):


                 Δ𝑠𝑡 (𝑐) = 𝜆 𝑠𝑡∗ (𝑐) − 𝑠𝑡−1 (𝑐) ,           ∗           ∗
                                              
                                                           𝑠2024 (𝑐) − 𝑠2023 (𝑐) = 𝜅 𝐺 (𝑐).         (4)



                                                       7
Three implications follow. First, the 2024 change in usage responds to 𝐺 over and above any
pre-existing trend: if 𝛽𝑡 denotes the slope of the usage change on 𝐺 in season 𝑡, the acceleration
𝐴 = 𝛽2024 − 𝛽2023 is positive. Second, the response fades once the new target is reached, so
𝛽2025 and 𝛽2026 are close to zero; a small negative value would indicate overshooting followed by
correction. Third, groups that were already moving toward the new target before 2024 show little
acceleration, whereas groups that had not moved catch up. These implications require only that
usage move in proportion to its distance from the target, not that it move slowly; they hold for any
adjustment speed 𝜆, including one close to one.
    The fifth hypothesis, H5, is that agents re-optimize only when the gain exceeds the cost. Even
professionals can leave sizable gains unexploited (Romer, 2006), which suggests that changing a
strategy is costly. Suppose that changing a decision rule carries a fixed cognitive or practice cost
in addition to the convex cost above, as in models that combine the two (Cooper & Haltiwanger,
2006). An agent then adjusts only when the expected gain exceeds the fixed cost, so that adjustment
is lumpy (Caballero & Engel, 1999), and the convex cost governs how quickly an agent that does
adjust approaches its target. The two sides of the plate face different gains. A pitcher’s location
plan is set in advance and applies to every batter, so its gain scales with the league-wide movement
of the zone. A batter’s swing decision is made in a fraction of a second, and its gain scales with
the batter’s own exposure 𝐸, which H3 implies is small. We therefore expect pitchers to adapt and
batters not to, even after the count stops affecting calls.



3     Institutional Setting and Data

3.1    The ABS in the KBO

Since the start of the 2024 season the KBO has used the ABS in every regular-season game. A
tracking system measures every pitch, and a strike-determination system relays the call to the
umpire through an earpiece. Calls cannot be challenged.
    The rule defines the zone relative to each batter’s registered height. In 2024 the bottom and

                                                   8
top of the zone were 27.64% and 56.35% of height. From 2025 both bounds moved down by 0.6
percentage points, to 27.04% and 55.75%, and they were unchanged in 2026. Horizontally, the
zone is the plate widened by 2 cm on each side, 47.18 cm in total. According to the league’s rules,
the horizontal bounds are checked at the middle plane of the plate, and a strike requires the pitch to
meet the vertical bounds at both the middle plane and the back plane (Korea Baseball Organization,
2026). The published rules do not say whether a pitch that only partly overlaps the zone is a strike.
    Three other rule changes overlap with our sample. In 2024 the league limited defensive shifts
(moving infielders toward the side of the field to which a batter tends to hit) and enlarged the bases;
a pitch clock (a time limit between pitches) was piloted in the same year, adopted in 2025 and
relaxed in 2026; and in 2022, two years before the ABS, the league instructed umpires to call a
wider zone. None of these changes enters the call function 𝑆, so tests based on calls are unaffected
by them. Tests based on behavior and outcomes rely on contrasts within the league, by height,
handedness, exposure and pitching arm, so that league-wide shocks are absorbed by season fixed
effects.


3.2    Pitch-level data

We collect every regular-season pitch from 2021 to 2026 from the play-by-play feed of Naver
Sports, the sports service of the Korean web portal Naver, which publishes the league’s tracking
data (Naver Sports, 2026). For each pitch we observe the call or batted-ball outcome, the pitch
type and velocity, and the nine parameters of the fitted trajectory. We also observe the batter’s
registered height and batting side (left or right), the pitcher’s throwing arm, and the result of the
plate appearance. We add the four umpires listed for each game and the catcher on the field for
each pitch, which we reconstruct from the starting lineup and the substitution log.
    We restrict the sample to April–September, so that each season covers the same months, and
drop the All-Star Game. The final sample contains 1,203,755 pitches, of which 657,201 were called,
and 308,959 plate appearances. Table 1 summarizes them by season. Among other statistics, it
reports the share of high pitches, those in the upper third of the ABS zone or above (the top two of


                                                  9
the five vertical bands defined in Section 2).

                                    Table 1: Summary statistics by season

                                                     Human umpire                         ABS
                                              2021       2022       2023       2024       2025       2026
       Games                                   596       687        648        680        674        665
       Pitches                               182,137   206,151    197,826    210,403    203,232    204,006
       Called pitches                        101,737   110,747    107,953    113,949    110,771    112,044
       Plate appearances                      46,287    53,252     50,698     54,074     52,261     52,387
       Called-strike rate (%)                  31.4      32.2       32.3       32.4       33.2       33.0
       Agreement with ABS rule (%)             89.8      91.4       91.6       98.6       98.6       98.6
       Strikes called outside the zone (%)      5.9       6.2        5.2        0.6        0.4        0.5
       Balls called inside the zone (%)        18.6      13.7       14.9        3.1        3.2        3.1
       High pitches (%)                        28.1      28.9       30.2       34.6       34.5       33.7
       Swing rate (%)                          43.8      45.9       44.9       45.5       45.1       44.7
       Walk rate (%)                           10.5       8.6        8.9        9.0        8.9        9.2
       Strikeout rate (%)                      18.0      18.6       17.7       18.8       19.6       19.4
       Notes:     Columns are regular seasons, April–September; 2021 is used only for pre-trend tests, 2022–
       2023 is the human-umpire baseline and 2024–2026 are ABS seasons. Agreement compares each call
       with our reconstruction of the ABS rule (Appendix Table A1), applying the 2024 zone through 2024
       and the 2025 zone thereafter, and high pitches are those in the upper third of the zone or above.



   The seasons play different roles. The two seasons 2022–2023 form the human-umpire baseline,
and every quantity defined relative to the human zone is estimated on them alone. The most
important is the human zone itself, 𝑆¯ 𝐻 (𝑥, 𝑧), the probability of a called strike at horizontal position
𝑥 and height above the ground 𝑧. We estimate it from 2022–2023 calls with a logit model in which
this probability is a smooth function of 𝑥 and 𝑧 (a generalized additive model with a tensor-product
spline). Because 𝑧 is measured in absolute terms, the estimated zone is free to ignore the batter’s
height. Treating the human zone as a smooth probability of a strike, rather than a sharp boundary,
follows the evidence that umpires’ calls behave like a psychophysical judgment that becomes less
certain near the edge (Flannagan, Mills, & Goldstone, 2024). The count values 𝑣 and the mechanical
shocks 𝐺 are also estimated on these two seasons. The seasons 2024–2026 are the ABS seasons.
We use 2021 only for pre-trend tests: it precedes the 2022 zone expansion, and the season was
interrupted by COVID-19 and resumed without extra innings (the additional innings played when
a game is tied after nine).




                                                        10
3.3    Reconstructing locations and the ABS rule

We compute the location at which each pitch crosses the plate from its fitted trajectory and express
its height as a fraction of the batter’s registered height, 𝑧/ℎ, the unit in which the ABS zone is
defined. Because the published rules leave some details open, Appendix Table A1 searches over
candidate definitions and compares each with the 2024–2026 ABS calls. Two features matter. Calls
match far better when a strike requires only that some part of the ball touch the zone, as Lee et al.
(2025) assume, than when the whole ball must be inside it (98.6% against 93.0%), and the 2 cm
widening adds two percentage points. The choice of plane matters little: checking the vertical
bounds at the middle plane alone or, as the rules state, at both the middle and the back plane gives
98.6% and 98.5%. We use the middle plane alone, which fits marginally better and gives each pitch
a single location. This rule reproduces 98.6% of calls using registered heights, and 99.1% using
the height list the system itself applies, which we back out from the tracking data’s zone bounds
(Appendix Tables A3 and A4). Applied to the human-umpire seasons, the same reconstruction
agrees with 91.4% and 91.6% of calls in 2022 and 2023; most of the disagreements are balls called
inside the zone.
   Two measurement issues require attention. The first is a change in the source format: from
games on 16 July 2026 the source data report trajectories relative to a reference point 55 ft from
the plate instead of 50 ft. Ignoring this would inflate plate-crossing heights by 12–19 cm. After the
correction, the replication rate is identical before and after the switch (Appendix Table A3).
   The second is the stability of the tracking calibration, since a recalibration of the vertical axis
could masquerade as pitchers throwing higher. Within a pitcher and pitch type, the height of the
ball 50 ft from the plate, close to the release point (where the ball leaves the pitcher’s hand), changes
by at most 1.8 cm across seasons (Appendix Table A2). This is small relative to the changes in
plate-crossing height that we attribute to behavior.




                                                   11
4     Empirical Strategy

The ABS was introduced in every game at once, so no part of the league remained under human
umpires after 2024. Our designs therefore exploit variation in how strongly the change in the call
function bears on different pitches, players and locations, and they lean on the fact that the call
function itself is untouched by the league’s other rule changes. This section describes each design
and the assumption under which it identifies the effect of the ABS. Regressions of binary outcomes
are linear probability models. Because we test many hypotheses, we also compute, within the family
of tests reported in each table, 𝑞-values adjusted for the false discovery rate with the procedure of
Benjamini and Hochberg (1995).


4.1    Calls

To locate the change in the call function, we divide called pitches into eight regions defined relative
to the 2024 ABS zone and the batter’s registered height: the three thirds of the zone; the high and
low edges, bands just above and below the zone; the inside and outside edges, bands just beyond
the side of the zone nearer to and farther from the batter; and everything farther out. For a called
pitch 𝑖 in region 𝑟, thrown by pitcher 𝑝 to batter 𝑏 in month 𝑚 of season 𝑡, we estimate


                            Strike𝑖 = 𝛼𝑟 + 𝛿𝑟 ABS𝑡 + 𝜇 𝑝 + 𝜇 𝑏 + 𝜇𝑚 + 𝜀𝑖 ,                         (5)


where Strike𝑖 indicates a called strike, ABS𝑡 indicates the 2024–2026 seasons, and 𝜇 𝑝 , 𝜇 𝑏 and 𝜇𝑚
are pitcher, batter and month fixed effects. The coefficient 𝛿𝑟 is the change in the probability that
a pitch in region 𝑟 is called a strike after the machine replaced the umpire, holding the pitcher and
the batter fixed. Standard errors in this and every other regression of calls are clustered by game,
because pitches in the same game share an umpire, a ballpark and conditions. This is a before–after
comparison within a region, and 𝛿𝑟 measures the effect of the ABS under the assumption that,
absent the machine, the probability that a pitch in region 𝑟 thrown by a given pitcher to a given
batter is called a strike would have stayed at its 2022–2023 level. Because the limits on defensive

                                                  12
shifts, the larger bases and the pitch clock do not enter the call, these other changes cannot violate
the assumption. It would fail if human umpires were already changing their calls, which we check
by replacing ABS𝑡 with indicators for each season from 2021 to 2026, with 2023 as the reference.
   The ABS rule treats every pitcher–batter matchup identically. To ask whether human umpires
did, we estimate equation (5) separately for each combination of pitching arm and batting side. Raw
call rates could differ across matchups simply because pitches land in different parts of an edge, so
we also modify equation (5) to compare pitches at the same location. For each side edge (inside and
outside) and each period (2022–2023 and 2024–2026), we replace the regressors of equation (5)
with indicators for three matchups, whose coefficients we denote 𝛾 𝑘 , and with fixed effects 𝜇ℓ
for the fine location bin ℓ of the pitch, 3 cm horizontally by 2% of the batter’s height vertically.
The three matchups are right-handed pitchers facing left-handed batters and left-handed pitchers
facing right- and left-handed batters, with right-handed pitchers facing right-handed batters as the
reference. Each 𝛾 𝑘 is then the difference in the called-strike probability between matchup 𝑘 and the
reference matchup at the same location, and a Wald 𝐹-test of 𝛾1 = 𝛾2 = 𝛾3 = 0 asks whether all
four matchups are called alike. A rule that is symmetric across handedness implies that this null
holds under the ABS.
   To measure how much the change in calls matters for plate appearances, we compute the
exposure 𝐸 in equation (3) directly. We re-judge every 2022–2023 called pitch with the ABS
rule, holding behavior fixed, and count for each plate appearance the strikes the ABS would have
added: pitches inside the ABS zone that umpires called balls, minus pitches outside it that umpires
called strikes. Averaging this count over the plate appearances of each matchup gives 𝐸. This is a
calculation rather than an estimate.
   The discretionary component is identified by difference-in-differences on border pitches, the
called pitches within 0.18 ft (5.5 cm, about one and a half ball widths) of the ABS zone boundary,
where context can plausibly sway a human call:


                          𝑌𝑖 = 𝛽1 𝑋𝑖 + 𝛽2 𝑋𝑖 × ABS𝑡 + 𝜇ℓ𝑡 + 𝜇 𝑝 + 𝜇𝑢 + 𝜀𝑖 ,                       (6)



                                                 13
where 𝑌𝑖 = Strike𝑖 , 𝑋𝑖 is a context variable, 𝜇ℓ𝑡 are fixed effects for location bins interacted with
season, and 𝜇𝑢 are fixed effects for the home-plate umpire 𝑢. We consider three contexts. Following
the evidence that status affects umpires’ calls (Kim & King, 2014), we define a star batter as one
whose on-base percentage (the share of plate appearances in which the batter reaches base by a hit,
a walk or being hit by a pitch) was in the top 20% among batters with at least 300 plate appearances
in the previous season. The second context is whether the batter plays for the home team. The third
is the count, grouped into hitter-ahead counts (2-0, 3-0 and 3-1), two-strike counts, and all other
counts as the reference. The specifications for the home team and the count add batter fixed effects
𝜇 𝑏 . For star status we report the estimate with and without them; with them, 𝛽2 is identified from
batters whose status changes. The coefficient 𝛽1 is the human umpires’ context effect at a given
location, and 𝛽2 is its change under the ABS. The identifying assumption is that, absent the ABS,
the gap in calls between contexts at the same location would have remained constant. We assess it
for star status by replacing 𝛽1 𝑋𝑖 + 𝛽2 𝑋𝑖 × ABS𝑡 with a separate coefficient on 𝑋𝑖 for each season,
which shows whether the gap was stable before 2024. Equation (6) also serves as the template for
several designs below, which change the outcome 𝑌𝑖 , the regressors and the fixed effects.
   To measure catcher framing, we adapt equation (6). For each season separately and on all called
pitches, we replace 𝛽1 𝑋𝑖 + 𝛽2 𝑋𝑖 × ABS𝑡 with a fixed effect 𝜙 𝑗 for the catcher 𝑗 who received the
pitch, and use fixed effects for location bin, pitcher, batter and home-plate umpire. Because catchers
on the same team share pitchers, 𝜙 𝑗 is identified only relative to teammates, so we normalize the
effects to have a pitch-weighted mean of zero within each team and keep catchers with at least
1,500 called pitches. We measure the persistence of framing in two ways: the split-half reliability,
the correlation between 𝜙 𝑗 estimated on alternating games of the same season, and the correlation
between a catcher’s 𝜙 𝑗 in consecutive seasons. Each correlation is tested against zero with the 𝑡-test
for a Pearson correlation, which has 𝑛 − 2 degrees of freedom for 𝑛 catchers. To value framing
in runs, we multiply each catcher’s effect by the catcher’s number of called pitches and by the run
value of a strike, and take the standard deviation across catchers.




                                                  14
4.2    Pitchers

For pitchers we cannot compare treated and untreated groups, because every pitcher faced the
machine. Instead we use the fact that the ABS changed the value of some locations much more
than others. For each cell 𝑐 defined in Section 2 (a pitch type in one of 25 areas of the plate) with
at least 150 pitches in 2022–2023, we compute its mechanical shock 𝐺 (𝑐) from 2022–2023 pitches
alone, and estimate for each season


                                 𝑠𝑡 (𝑐) − 𝑠𝑡−1 (𝑐) = 𝑎 𝑓 + 𝛽𝑡 𝐺 (𝑐) + 𝑒 𝑐,𝑡 ,                             (7)


where 𝑠𝑡 (𝑐) is the cell’s share, in percent, of its pitch type’s pitches, 𝑎 𝑓 are fixed effects for the pitch
type 𝑓 of cell 𝑐, and cells are weighted by their baseline pitches. This is a continuous-treatment
difference-in-differences across cells, with 𝐺 as the treatment intensity.
    A positive 𝛽2024 alone does not identify a response to the ABS, because usage may already
have been drifting toward cells that the ABS later favored. We therefore focus on the acceleration
𝐴 = 𝛽2024 − 𝛽2023 , which we estimate by regressing the difference between the 2024 and 2023
changes in usage on 𝐺 in the same way. It identifies the effect under the assumption that, absent
the ABS, the drift would have continued at its 2023 pace. Two checks support the assumption.
The slope for 2022 provides a placebo, and, for groups whose 2023 slope is zero, the acceleration
reduces to the 2024 slope. To ask whether pitchers did more than move their pitches up or down,
we also estimate 𝐴 with fixed effects for the five vertical bands, which compares cells at the same
height. We estimate these slopes for all pitchers, separately by pitching arm, and in a balanced
panel of pitchers with at least 300 pitches in at least three seasons. Because cells pool the pitches of
many pitchers, we compute standard errors from 999 bootstrap replications that resample pitchers
and test the slopes with 𝑧-tests.
    To compare the timing of the move toward high pitches across pitching arms, we regress each
pitcher’s share of high pitches in a season on pitcher fixed effects and season indicators, with 2023
as the reference. We estimate this regression in the balanced panel, separately for left-handed,


                                                     15
right-handed and side-arm pitchers, weighting by pitches and clustering standard errors by pitcher.
Each season coefficient 𝜃 𝑠 is the within-pitcher change in the high-pitch share between season 𝑠 and
2023. To ask whether human umpires treated high pitches differently by pitching arm before the
ABS, we adapt equation (6) once more, estimating it on called pitches in the upper third of the zone
and the high edge in 2022–2023. Its regressors are the interactions of indicators for left-handed
and side-arm pitchers with an indicator for 2022, with right-handed pitchers as the reference, and
its fixed effects are for location bin, season, pitching arm and batter. The coefficient 𝜆 𝑎 on each
interaction is the change in the called-strike probability from 2023 to 2022 for arm 𝑎 relative to
right-handed pitchers at the same location.


4.3    Batters

The ABS scales the zone with registered height, so height determines how strongly the geometric
shock bears on a batter. We measure the shock with each batter-season’s excess strike rate on high
pitches, 𝐷 𝑏𝑡 . For each high pitch within 1 ft of the center of the plate that batter 𝑏 took in season 𝑡,
we subtract from the actual call (one for a strike, zero for a ball) the probability that the 2022–2023
human zone would have called it a strike, and 𝐷 𝑏𝑡 is the average of these differences. For batters
observed both before and after the ABS, we estimate


                                                        ¯ × ABS𝑡 + 𝑢 𝑏𝑡 ,
                              𝐷 𝑏𝑡 = 𝛼𝑏 + 𝜏𝑡 + 𝜋 (ℎ 𝑏 − ℎ)                                            (8)


where ℎ 𝑏 is registered height, ℎ¯ = 182 cm, 𝛼𝑏 and 𝜏𝑡 are batter and season fixed effects, and
batter-seasons are weighted by their number of high pitches. This is the first stage. It is a
continuous-treatment difference-in-differences with height as the treatment intensity, and the iden-
tifying assumption is parallel trends across heights. We examine the assumption by replacing
       ¯ × ABS𝑡 with (ℎ 𝑏 − ℎ)
(ℎ 𝑏 − ℎ)                   ¯ interacted with each season from 2021 to 2026, relative to 2023.

Taller batters hit more home runs and strike out more (Appendix Table A6), but batter fixed effects
absorb such level differences, and the assumption requires only that their trends do not differ.


                                                   16
Standard errors in all regressions for batters are clustered by batter, except where noted.
   The reduced form replaces 𝐷 𝑏𝑡 in equation (8) with the batter’s behavior and plate-appearance
                                                                              ¯ × ABS𝑡 and batter
outcomes, at the level of the pitch or the plate appearance, keeping 𝜋 (ℎ 𝑏 − ℎ)
fixed effects. When the outcome is whether a pitch is high, we add fixed effects for pitcher by
season and for count by season. When it is whether the batter swings at a pitch in the area the ABS
added to the zone (above the top of the human zone, 3.35 ft, and inside the ABS zone), we add fixed
effects for absolute location bins (3 cm by 3 cm) by season, for count by season, and for pitcher.
When it is whether a plate appearance reaches two strikes or three balls, we add fixed effects for
pitcher by season.
   To test whether batters responded to the end of count-dependent calls, we extend equation (6)
to a triple difference, estimated on border pitches and pitches in the heart of the zone (inside the
zone and more than 0.18 ft from its boundary). The outcome 𝑌𝑖 is an indicator for a swing, and
the regressors are Border𝑖 × ABS𝑡 and its interactions with the hitter-ahead and two-strike count
groups, with other counts as the reference. The fixed effects are for location bin by season, count
group by season, count group by border, pitcher and batter, and standard errors are clustered by
game. The coefficient 𝜓𝑔 on the triple interaction for count group 𝑔 is the change under the ABS in
the difference in swing rates between border and heart pitches in that count group, relative to other
counts. Calls in the heart of the zone did not depend on the count even under human umpires, so
they absorb any change in swing behavior by count that is unrelated to the calls. As a placebo, we
estimate the same regression on 2022–2023 with 2023 treated as if it were the first ABS season.
   Finally, we estimate equation (6) at the plate-appearance level for star batters over 2022–2026.
The outcome 𝑌𝑖 indicates a walk, a strikeout or reaching base, or is the plate-appearance value; 𝑋𝑖
is star status; and the fixed effects are for batter and for pitcher by season. We denote its coefficients
𝜌1 and 𝜌2 , so that 𝜌2 is the change in star batters’ outcomes under the ABS. We compare 𝜌2 for
the plate-appearance value with the change that the call channel in equation (3) predicts. The
prediction multiplies the pre-ABS star coefficient 𝛽1 from the call regression by the value Δ𝑣 of
each border pitch that star batters took in 2022–2023, sums over these pitches, and divides by star


                                                   17
batters’ plate appearances in the same seasons. Treating the prediction as fixed, we test whether 𝜌2
equals it with a 𝑡-test. To express the call channel in runs per season, we multiply it by 550 plate
appearances and divide by the wOBA scale of 1.2. Because earlier work uses 2023 alone as the
pre-ABS season, we also estimate this regression with that baseline.



5     Results

We present the results in three steps. We first characterize what the machine changed in the call
function, separating its geometric and discretionary components (H1–H2). We then study how
pitchers reallocated their pitches (H4), and finally ask whether batters bore the incidence of the
change and whether they responded to it (H3, H5).


5.1    Calls: geometry and discretion

Our reconstruction of the ABS rule reproduces 98.6% of ABS calls in 2024 and 98.6% in 2026,
against 91.4% and 91.6% of human calls in 2022 and 2023 (Table 1). The overall called-strike
rate barely changed. The zone did not grow but moved (Appendix Figure A1), as Lee et al. (2025)
document for the first half of 2024.
    Table 2 asks where on the plate the calls changed and whether the change follows the rule’s
geometry. Panel A reports 𝛿𝑟 from equation (5) for each of the eight regions. Every 𝛿𝑟 is significantly
different from zero at the 1% level, and the signs follow the rule. A pitch in the upper third of the
zone became 13.9 percentage points more likely to be called a strike, because human umpires had
called a seventh of these pitches balls. A pitch in the band just below the zone became −15.2 points
less likely to be a strike, because human umpires had called a third of them strikes. Pitches in the
middle of the zone, already called strikes 95% of the time, changed little. The season-by-season
estimates of equation (5) in Appendix Table A9 show that the change at the top of the zone and on
the inside edge arrived in 2024, after two stable human-umpire seasons. On the outside edge and
below the zone, by contrast, human calls were already moving in the same direction between 2022


                                                  18
and 2023, so the before–after estimates overstate the effect of the machine there; relative to 2023
alone, the change is −3.2 points on the outside edge and −18.5 points below the zone.

                                    Table 2: The geometry of the change in calls

                                                                     Strike rate (%)          ABS effect (pp)
                                                                 Human             ABS        Change                 N
      Panel A. Location
        Zone, upper third                                          86.2           100.0       13.9∗∗∗     (0.3)    16,453
        Zone, middle third                                         94.5            98.4        4.0∗∗∗     (0.2)    20,059
        Zone, lower third                                          95.4           100.0        4.7∗∗∗     (0.2)    20,305
        High edge                                                  16.7            21.8        5.1∗∗∗     (0.5)    13,137
        Low edge                                                   33.1           17.8        -15.2∗∗∗    (0.5)    17,560
        Inside edge                                                33.0           39.7         6.7∗∗∗     (0.8)     7,422
        Outside edge                                               45.6           38.5         -7.0∗∗∗    (0.6)    14,541
        Far outside                                                0.9             0.0         -0.7∗∗∗    (0.1)   109,223
      Panel B. Horizontal edges by pitcher hand × batter side
        RHP vs RHB, inside edge                                  32.1              39.2        7.3∗∗∗     (1.4)    2,389
        RHP vs RHB, outside edge                                 50.4              38.9       -11.4∗∗∗    (1.0)    5,122
        RHP vs LHB, inside edge                                  32.3              39.2        6.9∗∗∗     (1.2)    2,942
        RHP vs LHB, outside edge                                 42.3              38.3        -3.9∗∗∗    (1.0)    5,491
        LHP vs RHB, inside edge                                  43.4              40.0         -3.2∗     (1.8)    1,287
        LHP vs RHB, outside edge                                 41.9              37.3        -4.3∗∗∗    (1.6)    1,678
        LHP vs LHB, inside edge                                  21.5              42.2       20.7∗∗∗     (2.1)     799
        LHP vs LHB, outside edge                                 45.1              39.2        -5.8∗∗∗    (1.5)    2,235
        Equal rates across matchups, inside edge: 𝐹 [𝑝]     25.8 [<0.001]       1.4 [0.227]
        Equal rates across matchups, outside edge: 𝐹 [𝑝] 11.7 [<0.001]          3.2 [0.021]
      Panel C. Mechanical exposure: extra strikes per plate appearance
        RHP vs RHB                                                                             0.007               37,814
        RHP vs LHB                                                                             0.024               38,792
        LHP vs RHB                                                                             0.019               14,197
        LHP vs LHB                                                                             0.043               13,060
       Notes:     The first two columns are raw called-strike rates under human umpires (2022–2023) and the ABS (2024–
      2026); Change is 𝛿𝑟 from equation (5) (a linear probability model with region, pitcher, batter and month fixed ef-
      fects), and N counts 2022–2023 called pitches (plate appearances in Panel C); pp denotes percentage points. Panel
      A covers every region of the plate, defined relative to the 2024 zone and registered height; Panel B re-estimates the
      model for the side edges by pitcher hand × batter side (RHP and LHP are right- and left-handed pitchers, RHB and
      LHB right- and left-handed batters), and its last two rows give Wald 𝐹-statistics [𝑝-values] for 𝛾1 = 𝛾2 = 𝛾3 = 0
      in the modified equation (5) of Section 4, that is, for equal call rates across matchups at the same location; Panel
      C re-judges 2022–2023 called pitches with the ABS rule and reports the extra strikes per plate appearance. ∗∗∗
      𝑝 < 0.01, ∗∗ 𝑝 < 0.05, ∗ 𝑝 < 0.1 in two-sided 𝑡-tests with standard errors clustered by game.



   The reason the top of the zone changed so much is that the human zone was anchored in absolute
height. Its top sat at about 102 cm for the shortest batters and 105 cm for the tallest (Figure 1). The
ABS scales the zone with height and lifts the top for the tallest group to 110 cm.




                                                              19
                                          100


               Height above ground (cm)

                                           80




                                           60




                                           40
                                                175 or less         176−180            181−185            186 or more
                                                                        Batter height (cm)

                                                              ABS (2024−2026)      Human umpire (2022−2023)



                                                Figure 1: Effective strike-zone height by batter height
  Notes: Called pitches within 0.4 ft of the center of the plate, 2022–2026. Bars span the heights at which a logit
  smooth of the called-strike probability exceeds 0.5.


   The ABS rule treats every pitcher–batter matchup identically, and Panel B asks whether human
umpires did. It reports 𝛿𝑟 from equation (5) for the inside and outside edges, estimated separately
for each combination of pitching arm and batting side. Two asymmetries stand out. On the outside
edge, umpires were generous when a right-handed pitcher faced a right-handed batter, calling 50.4%
of such pitches strikes against 42–45% in the other matchups; the ABS cut this rate by 11.4 points.
On the inside edge, they were stingy when a left-handed pitcher faced a left-handed batter, calling
21.5% of such pitches strikes against 32–43% elsewhere; the ABS raised this rate by 20.7 points.
After the ABS, edge strike rates lie between 37% and 42% in every matchup.
   The last two rows of Panel B compare the matchups at the same location: they report the Wald
𝐹-statistic for 𝛾1 = 𝛾2 = 𝛾3 = 0 in the modified equation (5). Under human umpires equality is
rejected, with 𝐹 = 25.8 on the inside edge and 𝐹 = 11.7 on the outside edge (both 𝑝 < 0.001).
Under the ABS it cannot be rejected on the inside edge (𝐹 = 1.4, 𝑝 = 0.23), and on the outside
edge the statistic falls to 𝐹 = 3.2 (𝑝 = 0.02), consistent with small differences in location within
bins. These results indicate that the human zone was asymmetric across handedness, whereas the

                                                                              20
machine’s is close to symmetric, as H2 predicts.
    Panel C reports the exposure 𝐸 by matchup. It ranges from 0.007 extra strikes per plate
appearance for right-handed pitchers facing right-handed batters to 0.043 for left-handed pitchers
facing left-handed batters. Large changes in call probabilities at the edges therefore amount to at
most one extra strike every 23 plate appearances, because few pitches land on the edges and fewer
still are taken. This is the first ingredient of H3.
    We turn from the geometry of the rule to the discretion it removed. Table 3 reports 𝛽1 and 𝛽2
from equation (6), which test H1. Before the ABS, star batters were 1.5 percentage points less likely
than other batters to receive a called strike on the same pitch (𝑝 < 0.01), and the ABS removed
most of this advantage (𝛽2 = 1.1, 𝑝 < 0.01). The same holds with batter fixed effects, comparing
seasons in which a batter does and does not hold star status (𝑝 < 0.05). Estimated season by season,
the advantage is present in both baseline seasons, at −1.15 points in 2022 (𝑝 < 0.05) and −1.75 in
2023 (𝑝 < 0.01), and it shrinks toward zero under the ABS, at −0.43, −0.35 and −0.17 points in
2024–2026; only the 2024 estimate is significant, and only at the 10% level. This pattern argues
against a pre-existing trend.
    There was no home-team bias to remove: neither 𝛽1 nor 𝛽2 for the home team is distinguishable
from zero (Appendix Table A12). The count, by contrast, mattered a great deal. Human umpires
expanded the zone in hitter-ahead counts by 6.1 points and contracted it with two strikes by −6.7
points (both 𝑝 < 0.01), and the estimates of 𝛽2 are of the opposite sign and similar size (both
𝑝 < 0.01), so that the adjustments essentially disappear under the ABS, replicating Lee and Ko
(2026) and consistent with experimental evidence that the count shapes ball–strike judgments
(MacMahon & Starkes, 2008).




                                                       21
                    Table 3: Context-dependent calls: status, home team and count

                                                        Estimate (pp)     SE          N
           Panel A. Batter status
             Star batter, pre-ABS                          -1.47∗∗∗      (0.35)     200,588
             Star batter × ABS                              1.15∗∗∗      (0.38)     200,588
             Star batter × ABS, batter fixed effects        1.02∗∗       (0.46)     200,568
             Star batter in 2022                            -1.15∗∗      (0.51)     200,588
             Star batter in 2023                           -1.75∗∗∗      (0.49)     200,588
             Star batter in 2024                             -0.43∗      (0.26)     200,588
             Star batter in 2025                              -0.35      (0.25)     200,588
             Star batter in 2026                              -0.17      (0.22)     200,588
           Panel B. Count
             Hitter-ahead count, pre-ABS                    6.14∗∗∗      (0.45)     200,568
             Hitter-ahead count × ABS                      -5.47∗∗∗      (0.48)     200,568
             Two-strike count, pre-ABS                     -6.74∗∗∗      (0.29)     200,568
             Two-strike count × ABS                         6.90∗∗∗      (0.31)     200,568
            Notes:     Columns report the coefficient in percentage points, its standard
           error and the number of border pitches (within 0.18 ft of the zone boundary),
           from linear probability models of a called strike with location-bin × season,
           pitcher and home-plate-umpire fixed effects. Panel A compares star batters
           (top 20% of on-base percentage among batters with 300+ plate appearances
           in the previous season) with other batters before and after the ABS, adding
           batter fixed effects in the third row and estimating the star coefficient season
           by season below; Panel B compares each count group with neutral counts,
           with batter fixed effects. ∗∗∗ 𝑝 < 0.01, ∗∗ 𝑝 < 0.05, ∗ 𝑝 < 0.1 in two-sided
           𝑡-tests with standard errors clustered by game.


   Catcher framing is a skill whose value derives from the evaluator’s errors, and a literature in
sports analytics measures it with catcher effects on the called-strike probability (Deshpande &
Wyner, 2017). H1 therefore predicts that it should be a persistent attribute of catchers under human
umpires and noise under the machine. Table 4 reports the dispersion and the reliability of the
catcher effects 𝜙 𝑗 defined in Section 4, and the estimates support both parts. Within team, the
dispersion of catcher effects falls from 0.93 to 0.14 percentage points. In every baseline season,
estimates from alternating halves of the season’s games are strongly correlated (0.60–0.81, all
𝑝 < 0.01 with 20–22 catchers), and a catcher’s estimate predicts the next season’s (𝑝 < 0.05). In
none of the ABS seasons is either correlation distinguishable from zero, even at the 10% level.


                                                 22
                           Table 4: Catcher framing before and after the ABS

                                   Dispersion            Reliability             Value
            Season     Catchers     SD (pp)     Split-half r   Prior-season r   SD (runs)
            2021          20          1.06        0.81∗∗∗                          4.9
            2022          22          0.94        0.65∗∗∗         0.56∗∗           4.1
            2023          20          0.78        0.60∗∗∗         0.67∗∗∗          4.6
            2024          21          0.09         -0.17           0.02            0.5
            2025          23          0.19         0.28            0.40            0.9
            2026          22          0.12         0.06            0.14            0.6
             Notes:     Columns report the number of catchers with 1,500+ called
            pitches, the standard deviation (SD) of their within-team effects on the
            called-strike probability in percentage points (pp), the correlation between
            estimates from alternating halves of the season’s games, the correlation
            with the same catcher’s estimate in the previous season, and the standard
            deviation in runs (one strike = 0.135 runs). Catcher effects come from
            season-by-season linear probability models with location-bin, pitcher, bat-
            ter and umpire fixed effects. ∗∗∗ 𝑝 < 0.01, ∗∗ 𝑝 < 0.05, ∗ 𝑝 < 0.1 in
            two-sided 𝑡-tests of zero correlation.


   Appendix Figure A2 shows the collapse. The rents involved were real but small. Valued at the
run value of a strike in the KBO (0.135 runs), one standard deviation of framing was worth about
4.5 runs per catcher-season before the ABS, against 0.7 after, and the star advantage in calls was
worth about 0.9 runs per star batter-season. Both effectively disappeared under the ABS, and both
are small relative to a team’s run total.


5.2    Pitchers: reallocation and catch-up

Pitchers moved their pitches up: the share of pitches in the upper third of the zone or above rose
for every pitch type in 2024 (Figure 2a). Table 5 asks whether this movement was a response to the
ABS rather than the continuation of a trend. It reports the slopes 𝛽𝑡 and the acceleration 𝐴 from
equation (7); a positive 𝐺 means that the machine made the cell more valuable to the pitcher.




                                                  23
          (a) Share of high pitches by pitch type                                                      (b) Within−pitcher change in high−pitch share


                                                                                                   5




                                                                           pp, relative to 2023
     40
 %




                                                                                                   0
     30



                                                                                                  −5
     20


          2021        2022           2023        2024   2025      2026                                  2021      2022       2023       2024       2025       2026


                 Changeup/splitter          Cutter      Sinker/two−seam
                                                                                                               Left−handed          Right−handed          Side−arm
                 Curveball                  Four−seam   Slider




                                             Figure 2: Pitch height before and after the ABS
  Notes: Panel (a): share of all pitches in the upper third of the ABS zone or above, by pitch type. Panel (b): season
  coefficients (2023 = 0) from regressions of a pitcher’s high-pitch share on season indicators with pitcher fixed
  effects, balanced panel, by pitching arm; 95% confidence intervals from standard errors clustered by pitcher; pp
  denotes percentage points.



     For all pitchers the response slope is zero in 2022 (𝛽2022 = 0.001, not significant), which serves
as a placebo: the ABS shock does not predict changes before the ABS was announced. The slope
is positive in 2023 (0.030, 𝑝 < 0.01), rises in 2024 (0.047, 𝑝 < 0.01), is close to zero in 2025, and
turns slightly negative in 2026 (−0.011, significant only at the 10% level), a partial unwinding of
the 2024 movement. The acceleration 𝐴 = 0.018 is positive but significant only at the 10% level,
and with vertical-band fixed effects it is no longer distinguishable from zero. Pitchers moved their
pitches up but did not otherwise re-sort them by pitch type or side of the plate. The adjustment was
quick and coarse, consistent with partial adjustment toward a new target that was reached within
one season (H4).




                                                                          24
                       Table 5: Pitchers’ reallocation toward locations favored by the ABS

                                                                    Response slope 𝛽𝑡                      Acceleration
                                                 2022        2023        2024        2025        2026            𝐴
        All pitchers                             0.001     0.030∗∗∗     0.047∗∗∗     -0.005     -0.011∗        0.018∗
                                                (0.006)    (0.006)      (0.006)     (0.005)     (0.006)       (0.010)
        Left-handed                              -0.007     0.003       0.060∗∗∗      0.002     -0.021∗       0.058∗∗∗
                                                (0.011)    (0.009)      (0.011)     (0.010)     (0.011)       (0.015)
        Right-handed                             0.001     0.034∗∗∗     0.039∗∗∗     -0.009      -0.009         0.005
                                                (0.007)    (0.008)      (0.007)     (0.006)     (0.007)       (0.012)
        Side-arm                                 0.020     0.052∗∗∗     0.045∗∗∗      0.030      -0.015        -0.007
                                                (0.019)    (0.020)      (0.017)     (0.020)     (0.032)       (0.031)
        Left-handed, balanced                    0.009      0.001       0.053∗∗∗      0.010    -0.031∗∗       0.052∗∗∗
                                                (0.010)    (0.010)      (0.011)     (0.011)     (0.015)       (0.018)
        Right-handed, balanced                   0.003     0.031∗∗∗     0.040∗∗∗   -0.015∗∗      -0.005         0.009
                                                (0.007)    (0.007)      (0.007)     (0.006)     (0.008)       (0.011)
        All, with vertical-band fixed effects                                                                  -0.012
                                                                                                              (0.009)
         Notes:     Each season column reports the slope 𝛽𝑡 from regressing the change in a cell’s usage share between
        𝑡 − 1 and 𝑡 on the cell’s mechanical shock 𝐺, with pitch-type fixed effects and baseline-pitch weights, and
        the last column is the acceleration 𝐴 = 𝛽2024 − 𝛽2023 . Cells are pitch type × five vertical × five horizontal
        bands with 150+ baseline pitches; rows split pitchers by arm, and the balanced panel keeps pitchers with 300+
        pitches in at least three seasons. ∗∗∗ 𝑝 < 0.01, ∗∗ 𝑝 < 0.05, ∗ 𝑝 < 0.1 in two-sided 𝑧-tests with standard errors
        from 999 bootstrap replications that resample pitchers.



   The pooled estimate masks sharp heterogeneity by pitching arm. Left-handed pitchers show
no response before 2024, a large response in 2024 (𝛽2024 = 0.060, 𝑝 < 0.01), none in 2025, and
a small reversal in 2026 (𝛽2026 = −0.021, significant only at the 10% level). Their acceleration
is 𝐴 = 0.058, and 0.052 in a balanced panel of the same pitchers (both 𝑝 < 0.01). Right-handed
pitchers who throw over-hand (with a conventional high arm angle), in contrast, were already
responding in 2023 (𝛽2023 = 0.034) and do not accelerate (𝐴 = 0.005, not significant).
   Appendix Table A11 examines why. Its timing rows report the within-pitcher season coefficients
𝜃 𝑠 ; its last row reports 𝜆 𝑎 , the difference by pitching arm in how human umpires called high pitches;
and the rows on the size of the shock, the mix of batters and the type of pitcher are descriptive
comparisons. Left-handed pitchers had somewhat more to gain from the ABS, but we find no
evidence that they faced a different mix of batters, threw differently, or changed in composition.
   What distinguishes them is timing. The within-pitcher coefficients 𝜃 𝑠 (Figure 2b) show that
right-handed and side-arm pitchers were already raising their pitches between 2021 and 2023,
whereas left-handed pitchers were flat until the ABS arrived. The 2021 and 2022 coefficients


                                                              25
relative to 2023 are negative and significant at the 1% level for right-handed and side-arm pitchers,
and indistinguishable from zero for left-handed pitchers. By 2025, all three groups had raised their
high-pitch share by similar amounts relative to 2023 (2.5–3.4 points; Appendix Table A11). For
side-arm pitchers, the earlier move coincides with a change in how human umpires called their high
pitches: relative to right-handed pitchers, their high pitches were less likely to be called strikes
in 2022 than in 2023 (𝜆 𝑎 significant at the 1% level). For right-handed pitchers there is no such
coincidence, and we treat their earlier move as a secular trend.
   The evidence is consistent with the third implication of H4: the ABS appears to have accelerated
reallocation mainly for the group that had not already moved toward the new target. Appendix
Figure A3 illustrates the contrast. The relationship between the shock and the change in usage
is flat for left-handed pitchers before the ABS and steep after it, but similar in both periods for
right-handed pitchers.


5.3    Batters: incidence without adaptation

Panel A of Table 6 reports 𝜋 from the first stage, equation (8), and its season-by-season version.
Each centimeter of height raises a batter’s excess strike rate on high pitches by 0.75 percentage
points after the ABS (𝑝 < 0.01; first-stage Wald 𝐹 = 49). The season-by-season estimates jump in
2024 and stay at that level. Before the ABS they are an order of magnitude smaller and move in
opposite directions in 2021 and 2022, around the league’s 2022 zone expansion. Height therefore
captures a large and stable change in the calls a batter receives.




                                                  26
Table 6: Batters: incidence by height, response to the end of count-dependent calls, and star batters’
outcomes

                                                                  Estimate      SE               N
               Panel A. First stage: excess high strikes (pp) per cm of height
                 Height × ABS, pooled 2022–2026                     0.75∗∗∗    (0.11)          1,026
                 Height × 2021                                      -0.16∗∗    (0.06)          1,183
                 Height × 2022                                      0.18∗∗∗    (0.06)          1,183
                 Height × 2024                                      0.78∗∗∗    (0.12)          1,183
                 Height × 2025                                      0.90∗∗∗    (0.10)          1,183
                 Height × 2026                                      0.83∗∗∗    (0.11)          1,183
               Panel B. Reduced form: effect of 10 cm of height after ABS (pp)
                 High pitch thrown                                  0.30     (0.24)           867,342
                 Swing at a newly created strike                   -1.25     (2.76)            16,244
                 Plate appearance reaches two strikes               0.57     (0.59)           222,828
                 Plate appearance reaches three balls              -0.34     (0.45)           222,828
               Panel C. Swing response to the removal of count-dependent calls (pp)
                 Two strikes × border × ABS                       0.77∗    (0.42)             691,755
                 Hitter ahead × border × ABS                       0.69    (0.86)             691,755
                 Two strikes × border × 2023 (placebo)            -0.85    (0.65)             274,154
                 Hitter ahead × border × 2023 (placebo)            0.79    (1.35)             274,154
               Panel D. Star batters’ outcomes after ABS (pp; wOBA points per 1,000 plate appearances)
                 Walk                                            -0.32     (0.44)         262,649
                 Strikeout                                       1.31∗∗    (0.59)         262,649
                 On base                                         -0.89     (0.66)         262,649
                 Plate-appearance value (wOBA points)            -5.68     (6.77)         262,649
                 Predicted by the call channel (wOBA points)     -1.92
                Notes:     Columns report the estimate, its standard error and the number of observations;
               pp denotes percentage points, and wOBA (weighted on-base average) values each plate-
               appearance outcome by its average contribution to scoring. Panel A regresses each batter-
               season’s excess called-strike rate on high pitches (relative to the 2022–2023 human zone)
               on height in cm × ABS with batter and season fixed effects, with season-by-season esti-
               mates relative to 2023; Panel B reports the reduced-form effect of 10 cm of height on pitch-
               or plate-appearance-level outcomes; Panel C is a triple difference in swing probability for
               border versus zone-interior pitches by count group, with 2023 as a placebo treatment; Panel
               D compares star and other batters before and after the ABS, and its last row is the change
               predicted by the call channel. ∗∗∗ 𝑝 < 0.01, ∗∗ 𝑝 < 0.05, ∗ 𝑝 < 0.1 in two-sided 𝑡-tests with
               standard errors clustered by batter (Panels A, B and D) or game (Panel C).



   Despite this, the reduced-form estimates of 𝜋 in Panel B show no detectable effect of height on
what happens in the plate appearance. Ten centimeters of height change the probability of reaching
two strikes by 0.57 points and of reaching three balls by −0.34 points. Neither is significantly
different from zero, and both 95% confidence intervals exclude effects larger than about 2 points.
Pitchers did not throw more high pitches to tall batters, and tall batters did not swing more at the
strikes the ABS created above the human zone. These estimates are reasonably precise, and the
absence of an effect is consistent with H3, given that a batter takes fewer than one high pitch every
two plate appearances.

                                                           27
   The removal of count-dependent calls changed the value of taking a border pitch by about seven
percentage points in the probability of a strike. Panel C reports the triple-difference coefficients
𝜓𝑔 , which ask whether batters adjusted their swings in response. Relative to pitches in the heart
of the zone, border swings with two strikes rose by 0.77 points. This estimate is significant only
at the 10% level, and the effect is an order of magnitude smaller than the change in calls. There is
no response in hitter-ahead counts, and the placebo estimates are flat. Batters did not re-optimize
while pitchers did, which is the asymmetry H5 predicts.
   Song et al. (2026) attribute a decline in star batters’ walks and on-base percentage after the
ABS to the loss of umpire favoritism. Our pitch-level evidence is consistent with such favoritism
(Table 3), but its value appears small. Panel D of Table 6 reports 𝜌2 , the change in star batters’ plate-
appearance outcomes under the ABS. Only the strikeout rate (the share of plate appearances ending
in three strikes) changes detectably, rising by 1.3 points (𝑝 < 0.05). The change in plate-appearance
value, −5.7 wOBA points per 1,000 plate appearances, is imprecise. It is not significantly different
from the −1.9 points that the call channel predicts (𝑡 ≈ −0.6). With a baseline consisting of 2023
alone, as in earlier work, the decline in plate-appearance value is about four times larger (−22.4
points) and significant at the 1% level (Appendix Table A10); adding 2022 to the baseline removes
most of it.


5.4    Robustness

Appendix Table A7 re-estimates the main coefficients under alternative specifications. For the
calls, we narrow or widen the border band to 0.12 or 0.25 ft, coarsen or refine the location bins to
6 or 1.5 cm, estimate a logit instead of a linear probability model, define star status by the top 10%
or 30% of on-base percentage or fix it at its 2021 value, and drop 2026. For pitchers, we require
100 or 300 instead of 150 baseline pitches per cell, and for batters we drop 2026. The removal of
count-dependent calls is robust to every change. The left-handed pitchers’ acceleration is equally
stable when we change the minimum number of baseline pitches per cell, and the first stage and the
null reduced form for batters are unchanged without 2026.


                                                   28
   The removal of the star advantage is less robust. It survives a narrower or wider border band,
finer location bins, a broader definition of star status (the top 30% of on-base percentage) and the
exclusion of 2026. It shrinks and loses significance, however, when location bins are coarsened to
6 cm, when the model is a logit, and when star status is restricted to the top 10%, and it is significant
only at the 10% level when status is fixed at its 2021 value. The logit is informative here: once the
ABS makes calls a deterministic function of location, many location bins are perfectly predicted
after 2024 and drop out of the logit, so it identifies the interaction from a different and smaller set
of pitches. We read the evidence as showing that human umpires favored star batters on border
pitches, but that the size of the effect depends on how finely location is held fixed.
   Appendix Table A8 reports the false-discovery-rate adjusted 𝑞-values. The removal of the star
advantage (𝑞 = 0.004), the removal of count-dependent calls (𝑞 < 0.001) and the acceleration
of left-handed pitchers (𝑞 < 0.001) survive the adjustment. The two marginal results for batters
do not: the increase in star batters’ strikeouts (𝑞 = 0.27) and the response of two-strike swings
(𝑞 = 0.33). This reinforces our reading that we cannot detect changes in batters’ behavior or
outcomes.


5.5    Summary

The machine removed three rents created by human judgment: deference to star batters, adjustments
to the count, and the value of catcher framing (H1). It also redistributed strikes along two geometric
margins chosen by its designers, height and handedness (H2). The redistribution was large in terms
of call probabilities but small in terms of plate-appearance outcomes, because few pitches are
exposed to it (H3). Pitchers re-optimized quickly and coarsely, and the group that had not already
moved caught up (H4). We find no detectable response by batters, either to the new geometry or to
the end of count-dependent calls (H5).




                                                   29
6    Conclusion

This paper studies what happens when an algorithm replaces human judgment in a setting where
every decision is recorded and the quality of each decision can be measured. In 2024 the KBO
replaced the home-plate umpire’s ball–strike judgment with an automated system, and we follow
more than a million pitches from 2021 to 2026 to trace the consequences for the evaluator’s calls,
for the pitchers who throw the pitches, and for the batters who face them. The machine changed
the call function in two distinct ways. It removed the discretionary component of human judgment.
Before 2024, umpires expanded the zone when the batter was ahead in the count and contracted it
with two strikes. Their calls depended on the catcher in a way that was stable within and across
seasons, and they gave star batters slightly more benefit of the doubt on border pitches, although
the size of this last effect depends on how finely location is held fixed. None of the three patterns is
detectable under the ABS. At the same time, the machine imposed a geometry chosen by the rule’s
designers. Because the human zone was anchored in absolute height and the machine’s zone scales
with registered height, strikes moved toward taller batters at the top of the zone. Because human
umpires treated matchups asymmetrically and the machine does not, strikes moved between right-
and left-handed matchups at the edges.
    These changes were large in terms of call probabilities but small in terms of outcomes. A pitch
in the upper third of the zone became 13.9 percentage points more likely to be called a strike. Yet
the extra strikes amount to at most one in every 23 plate appearances for the most exposed matchup,
and ten centimeters of height change the probability that a plate appearance reaches two strikes
or three balls by less than two percentage points. The value of catcher framing and of the star
advantage was real, but it amounted to a few runs per catcher-season and about one run per star
batter-season. This suggests that the incidence of a change in an evaluation rule may depend on
exposure as much as on the size of the change: a rule can move decisions sharply at the margin
while leaving the distribution of outcomes nearly intact, because few cases sit at the margin.
    The two sides of the plate responded very differently. Pitchers reallocated their pitches toward
the locations that the machine made more valuable, and they did so quickly and coarsely. The

                                                  30
response was concentrated in the first season, worked almost entirely through pitch height rather
than pitch type or side of the plate, and was partly unwound in the third season. Left-handed pitchers,
who had not taken part in the league’s earlier drift toward high pitches, account for the acceleration
at the time of the ABS and converged to the other groups within a season. Batters, by contrast,
show no detectable change in their swing decisions, either in response to the new geometry or to the
end of count-dependent calls, even though the value of taking a border pitch changed substantially
in some counts. This asymmetry is consistent with a simple cost of re-optimization. A pitcher’s
plan applies to every batter and is set in advance, so its gain scales with the league-wide shift in
the zone, whereas a batter’s decision is made in real time and its gain scales with the batter’s own
small exposure.
   The findings bear on the design of automated evaluation in sport and beyond. Leagues that
adopt automated calls, fully or through challenge systems such as those used in tennis and, since
2026, in Major League Baseball (Abramitzky et al., 2012; Lee, Han, Lee, & Ko, 2026), choose a
geometry when they write the rule, and that choice shapes who gains and who loses. Scaling the
zone with height, defining the plane at which the ball is judged, and widening the plate are design
parameters with distributional consequences, not technical details. More generally, our results
suggest that replacing a human evaluator with a rule can eliminate the rents that the evaluator’s
discretion created, including the value of skills whose purpose was to influence that discretion, but
need not by itself make outcomes more equal across agents. The incidence of the new rule is likely
to depend on its geometry and on how many cases it touches.
   Several limitations qualify these conclusions. We observe one league and three seasons after
the change, so we cannot say whether batters eventually adapt or whether the partial reversal in
pitchers’ behavior in 2026 persists. We do not observe salaries or contracts, so the labor-market
consequences of the rents we document remain open. Our measure of star status relies on past
on-base percentage, which captures reputation imperfectly. Our pitch locations come from the
league’s tracking data; we validate their stability within pitchers and against the system’s own calls,
but we cannot verify the pre-2024 coordinates independently. Finally, our analyses of behavior


                                                  31
and outcomes rely on contrasts within the league to absorb the other rule changes of 2024–2026,
an assumption that the calls themselves do not need. Comparisons with leagues that kept human
umpires, and with Major League Baseball’s challenge system, in which umpires still make every
call but players can ask the machine to overturn some of them (Lee et al., 2026), would sharpen
these results.



References

Abramitzky, R., Einav, L., Kolkowitz, S., & Mill, R. (2012). On the optimality of line call
      challenges in professional tennis. International Economic Review, 53(3), 939–964. doi:
      10.1111/j.1468-2354.2012.00706.x
Banerjee, A. N., Swinnen, J. F. M., & Weersink, A. (2007). Skating on thin ice: Rule changes
      and team strategies in the NHL. Canadian Journal of Economics, 40(2), 493–514. doi:
      10.1111/j.1540-5982.2007.00418.x
Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and
      powerful approach to multiple testing. Journal of the Royal Statistical Society: Series B
      (Methodological), 57(1), 289–300. doi: 10.1111/j.2517-6161.1995.tb02031.x
Bradbury, J. C. (2019). Monitoring and employee shirking: Evidence from MLB umpires. Journal
      of Sports Economics, 20(6), 850–872. doi: 10.1177/1527002518808350
Caballero, R. J., & Engel, E. M. R. A. (1999). Explaining investment dynamics in U.S.
      manufacturing: A generalized (S,s) approach.      Econometrica, 67(4), 783–826.      doi:
      10.1111/1468-0262.00053
Chen, D. L., Moskowitz, T. J., & Shue, K. (2016). Decision making under the gambler’s fallacy:
      Evidence from asylum judges, loan officers, and baseball umpires. Quarterly Journal of
      Economics, 131(3), 1181–1242. doi: 10.1093/qje/qjw017
Chiappori, P.-A., Levitt, S., & Groseclose, T. (2002). Testing mixed-strategy equilibria when
      players are heterogeneous: The case of penalty kicks in soccer. American Economic Review,



                                              32
      92(4), 1138–1151. doi: 10.1257/00028280260344678
Cooper, R. W., & Haltiwanger, J. C. (2006). On the nature of capital adjustment costs. Review of
      Economic Studies, 73(3), 611–633. doi: 10.1111/j.1467-937X.2006.00389.x
Deshpande, S. K., & Wyner, A. (2017). A hierarchical Bayesian model of pitch framing. Journal
      of Quantitative Analysis in Sports, 13(3), 95–112. doi: 10.1515/jqas-2017-0027
Dohmen, T. J. (2008). The influence of social forces: Evidence from the behavior of football
      referees. Economic Inquiry, 46(3), 411–424. doi: 10.1111/j.1465-7295.2007.00112.x
Fesselmeyer, E. (2021). The impact of temperature on labor quality: Umpire accuracy in Major
      League Baseball. Southern Economic Journal, 88(2), 545–567. doi: 10.1002/soej.12524
Flannagan, K. S., Mills, B. M., & Goldstone, R. L. (2024). The psychophysics of home plate
      umpire calls. Scientific Reports, 14, 2735. doi: 10.1038/s41598-024-52402-y
Garicano, L., Palacios-Huerta, I., & Prendergast, C. (2005). Favoritism under social pressure.
      Review of Economics and Statistics, 87(2), 208–216. doi: 10.1162/0034653053970267
Gould, J. P. (1968). Adjustment costs in the theory of investment of the firm. Review of Economic
      Studies, 35(1), 47–55. doi: 10.2307/2974406
Hamrick, J., & Rasp, J. (2015). The connection between race and called strikes and balls. Journal
      of Sports Economics, 16(7), 714–734. doi: 10.1177/1527002513509817
Hoffman, M., Kahn, L. B., & Li, D. (2018). Discretion in hiring. Quarterly Journal of Economics,
      133(2), 765–800. doi: 10.1093/qje/qjx042
Hsu, M. (2024). Umpire home bias in Major League Baseball. Journal of Sports Economics,
      25(4), 423–442. doi: 10.1177/15270025231222631
Hunter, D. J. (2018). New metrics for evaluating home plate umpire consistency and accuracy.
      Journal of Quantitative Analysis in Sports, 14(4), 159–172. doi: 10.1515/jqas-2018-0061
Kim, J. W., & King, B. G. (2014). Seeing stars: Matthew effects and status bias in Major League
      Baseball umpiring. Management Science, 60(11), 2619–2644. doi: 10.1287/mnsc.2014
      .1967
Kleinberg, J., Lakkaraju, H., Leskovec, J., Ludwig, J., & Mullainathan, S. (2018). Human


                                               33
      decisions and machine predictions. Quarterly Journal of Economics, 133(1), 237–293. doi:
      10.1093/qje/qjx032
Korea Baseball Organization. (2026). 2026 KBO league major regulations and rules. https://
      www.koreabaseball.com/Kbo/League/GameManage2026.aspx. (In Korean. Accessed
      14 October 2026)
Kovash, K., & Levitt, S. D. (2009). Professionals do not play minimax: Evidence from Major
      League Baseball and the National Football League (Working Paper No. 15347). Cambridge,
      MA: National Bureau of Economic Research.
Lee, K., Han, G., Lee, S., & Ko, J. (2026). When the strike zone becomes algorithmic: Umpire
      judgment and player challenge decisions under AI review. arXiv preprint 2609.25525.
Lee, K., Han, K., & Ko, J. (2025). Analyzing the impact of the automatic ball strike system
      in professional baseball through a case study on KBO league data. Scientific Reports, 15,
      44459. doi: 10.1038/s41598-025-28142-y
Lee, K., & Ko, J. (2026). Auditing contextual bias in human ball-strike calls using KBO’s automated
      umpiring transition. arXiv preprint 2609.03786.
Lucas, J., Robert E. (1967). Adjustment costs and the theory of supply. Journal of Political
      Economy, 75(4), 321–334. doi: 10.1086/259289
MacMahon, C., & Starkes, J. L. (2008). Contextual influences on baseball ball-strike decisions
      in umpires, players, and controls. Journal of Sports Sciences, 26, 751–760. doi: 10.1080/
      02640410701813050
Mills, B. M. (2014). Social pressure at the plate: Inequality aversion, status, and mere exposure.
      Managerial and Decision Economics, 35(6), 387–403. doi: 10.1002/mde.2630
Mills, B. M. (2017). Policy changes in Major League Baseball: Improved agent behavior and
      ancillary productivity outcomes. Economic Inquiry, 55(2), 1104–1118. doi: 10.1111/
      ecin.12396
Naver Sports. (2026). KBO league game schedules, box scores and pitch-by-pitch relay, 2021–2026.
      https://m.sports.naver.com/kbaseball. (In Korean. Accessed October 2026)


                                                34
Palacios-Huerta, I. (2003). Professionals play minimax. Review of Economic Studies, 70(2),
      395–415. doi: 10.1111/1467-937X.00249
Parsons, C. A., Sulaeman, J., Yates, M. C., & Hamermesh, D. S. (2011). Strike three: Discrim-
      ination, incentives, and evaluation. American Economic Review, 101(4), 1410–1435. doi:
      10.1257/aer.101.4.1410
Pope, D. G., Price, J., & Wolfers, J. (2018). Awareness reduces racial bias. Management Science,
      64(11), 4988–4995. doi: 10.1287/mnsc.2017.2901
Price, J., & Wolfers, J. (2010). Racial discrimination among NBA referees. Quarterly Journal of
      Economics, 125(4), 1859–1887. doi: 10.1162/qjec.2010.125.4.1859
Rickman, N., & Witt, R. (2008). Favouritism and financial incentives: A natural experiment.
      Economica, 75(298), 296–309. doi: 10.1111/j.1468-0335.2007.00605.x
Romer, D. (2006). Do firms maximize? Evidence from professional football. Journal of Political
      Economy, 114(2), 340–365. doi: 10.1086/501171
Song, J., Kang, J. H., & Paulsen, R. J. (2026). Technology adoption and bias in officiating: Auto-
      mated ball-strike system implementation in Korean baseball. European Sport Management
      Quarterly, 1–23. (Advance online publication) doi: 10.1080/16184742.2026.2681111
Sutter, M., & Kocher, M. G. (2004). Favoritism of agents—the case of referees’ home bias. Journal
      of Economic Psychology, 25(4), 461–469. doi: 10.1016/S0167-4870(03)00013-8
Tainsky, S., Mills, B. M., & Winfree, J. A. (2015). Further examination of potential dis-
      crimination among MLB umpires. Journal of Sports Economics, 16(4), 353–374. doi:
      10.1177/1527002513487740
Walker, M., & Wooders, J. (2001). Minimax play at Wimbledon. American Economic Review,
      91(5), 1521–1538. doi: 10.1257/aer.91.5.1521
Zitzewitz, E. (2006). Nationalism in winter sports judging and its lessons for organizational
      decision making. Journal of Economics & Management Strategy, 15(1), 67–99. doi: 10.1111/
      j.1530-9134.2006.00092.x




                                               35
A   Appendix: Measurement and Robustness

              Table A1: Reconstructing the ABS rule from 2024–2026 calls

        Zone width     Ball radius counts    Judging plane     Agreement (%)
        Plate + 2 cm   Yes                   Middle                98.61
        Plate + 2 cm   Yes                   Middle and back       98.49
        Plate + 2 cm   Yes                   Back                  98.00
        Plate          Yes                   Middle                96.61
        Plate          Yes                   Middle and back       96.31
        Plate          Yes                   Back                  96.13
        Plate + 2 cm   Yes                   Front                 95.67
        Plate          Yes                   Front                 94.80
        Plate + 2 cm   No                    Middle                93.00
        Plate + 2 cm   No                    Front                 92.84
        Plate + 2 cm   No                    Back                  92.34
        Plate + 2 cm   No                    Middle and back       91.29
        Plate          No                    Middle                90.85
        Plate          No                    Front                 90.68
        Plate          No                    Back                  90.20
        Plate          No                    Middle and back       89.22
         Notes:    Each row is a candidate definition of the ABS rule, and the
        last column is the share of 2024–2026 ABS calls it reproduces using
        registered heights.




                                            36
     Table A2: Measurement stability: within pitcher-by-pitch-type season effects

           Height at 50 ft (cm)      Plate-crossing height (cm)     Velocity (km/h)
   2021              -0.22                      -2.20∗∗∗                 -0.14
                    (0.33)                       (0.26)                 (0.18)
   2022            -0.70∗∗∗                     -1.29∗∗∗                0.46∗∗∗
                    (0.25)                       (0.25)                 (0.12)
   2024             0.73∗∗                       2.85∗∗∗               -0.51∗∗∗
                    (0.36)                       (0.26)                 (0.13)
   2025             1.76∗∗∗                      2.49∗∗∗                1.27∗∗∗
                    (0.55)                       (0.31)                 (0.19)
   2026              -0.32                       1.82∗∗∗                1.42∗∗∗
                    (0.55)                       (0.34)                 (0.21)
    Notes:     Columns report season coefficients (2023 omitted) from regres-
   sions with pitcher × pitch-type fixed effects; height at 50 ft approximates re-
   lease height, so a recalibration of the vertical axis would move both heights
   equally. ∗∗∗ 𝑝 < 0.01, ∗∗ 𝑝 < 0.05, ∗ 𝑝 < 0.1 in two-sided 𝑡-tests with stan-
   dard errors clustered by pitcher.


                     Table A3: Replication of ABS calls by period

Period                 Called pitches    Registered height (%)      ABS height list (%)
2024                      113,949                  98.59                  99.16
2025                      110,771                  98.62                  99.09
2026, from 16 July        43,121                   98.58                  99.09
2026, to 15 July          68,923                   98.66                  99.13
 Notes:   Columns report the number of called pitches and the share of ABS calls
reproduced using registered heights and using the system’s own height list. From
16 July 2026 the source data’s trajectory reference point moves from 50 to 55 ft,
which we correct.


            Table A4: Registered heights and the heights used by the ABS

  Season   Batters     Correlation    Slope     Median gap (cm)     Within 2 cm (%)
  2024       170          0.958       0.961            1.30               62.9
  2025       186          0.955       1.019            1.15               71.0
  2026       186          0.951       0.950            1.08               75.3
   Notes:    Columns compare registered heights with heights backed out from
  the tracking system’s zone bounds, for batters with 200+ pitches in a season.



                                           37
                     Table A5: Which listed umpire explains the calls?

Umpire position             Increase in adjusted R2 (×1000)      SD of umpire effects (pp)
First listed (home plate)                  1.50                              2.00
Second listed                              0.62                              1.41
Third listed                               0.75                              1.50
Fourth listed                              0.73                              1.51
 Notes:    Columns report the increase in adjusted 𝑅 2 from adding fixed effects for the
umpire in each listed position to a model with location-bin × season fixed effects, and
the standard deviation (SD) of those effects in percentage points (pp), for border pitches
in 2022–2023.


                      Table A6: Height and batters’ baseline profiles

      Variable                     Coefficient per 10 cm         SE       Correlation
      Home-run rate                       0.0100∗∗∗           (0.0016)        0.41
      Strikeout rate                      0.0409∗∗∗           (0.0090)        0.32
      Walk rate                            -0.0007            (0.0039)       -0.01
      Pulled ground-ball share            0.0454∗∗∗           (0.0120)        0.27
       Notes:     Columns report the coefficient on height (per 10 cm) and the
      correlation with height for baseline characteristics of the batters in Table 6,
      where a pulled ground ball is one hit in the direction of the batter’s swing
      (toward left field for a right-handed batter); batter fixed effects in that table
      absorb these level differences. ∗∗∗ 𝑝 < 0.01, ∗∗ 𝑝 < 0.05, ∗ 𝑝 < 0.1 in two-
      sided 𝑡-tests with heteroskedasticity-robust standard errors.




                                             38
                                      Table A7: Robustness of the main estimates

                                                    Calls (Table 3)                 Pitchers (Table 5)             Batters (Table 6)
Specification                            Star      Hitter ahead       Two strikes     Left-handed 𝐴        First stage    Reach two strikes

Baseline                                1.15∗∗∗      -5.47∗∗∗           6.90∗∗∗          0.058∗∗∗            0.75∗∗∗             0.57
                                        (0.38)        (0.48)            (0.31)            (0.015)            (0.11)             (0.59)
Border band 0.12 ft                     1.27∗∗∗      -5.21∗∗∗           7.40∗∗∗
                                        (0.48)        (0.61)            (0.38)
Border band 0.25 ft                     1.01∗∗∗      -5.12∗∗∗           6.21∗∗∗
                                        (0.31)        (0.40)            (0.26)
Coarser location bins (6 cm)             0.66        -5.21∗∗∗           6.16∗∗∗
                                        (0.43)        (0.56)            (0.35)
Finer location bins (1.5 cm)            1.17∗∗∗      -5.50∗∗∗           7.13∗∗∗
                                        (0.39)        (0.50)            (0.32)
Logit (log-odds coefficient)             0.02        -0.26∗∗∗           0.89∗∗∗
                                        (0.06)        (0.08)            (0.07)
Star: top 10%                            0.55
                                        (0.50)
Star: top 30%                           1.19∗∗∗
                                        (0.33)
Star: fixed 2021 status                  0.81∗
                                        (0.42)
Excluding 2026                          1.06∗∗∗      -5.52∗∗∗           6.94∗∗∗                              0.75∗∗∗             0.47
                                        (0.40)        (0.50)            (0.32)                               (0.11)             (0.56)
Cells with 100+ baseline pitches                                                         0.054∗∗∗
                                                                                         (0.015)
Cells with 300+ baseline pitches                                                         0.055∗∗∗
                                                                                         (0.018)

 Notes:     Each row re-estimates the main coefficients under one change to the baseline specification, and blank cells are not affected
by that change. The first three columns are the star, hitter-ahead and two-strike interactions with the ABS in Table 3, in percentage
points (log-odds in the logit row); the fourth is the acceleration 𝐴 of left-handed pitchers in Table 5; and the last two are the first stage
and the reduced-form effect of height on reaching two strikes in Table 6. Standard errors in parentheses below each estimate; ∗∗∗
𝑝 < 0.01, ∗∗ 𝑝 < 0.05, ∗ 𝑝 < 0.1 in two-sided tests with the same clustering as in the original tables.




                                                                      39
         Table A8: Multiple testing: false-discovery-rate adjusted 𝑞-values

   Family                 Test                                         Estimate         𝑝         𝑞
   Calls (Table 3)        Star × ABS                                    1.149        0.003      0.004
   Calls (Table 3)        Star × ABS, batter fixed effects              1.019        0.028      0.035
   Calls (Table 3)        Home × ABS                                    -0.123       0.634      0.634
   Calls (Table 3)        Hitter ahead × ABS                            -5.468      <0.001     <0.001
   Calls (Table 3)        Two strikes × ABS                             6.901       <0.001     <0.001
   Batters (Table 6)      High pitch thrown (reduced form)              0.295        0.225      0.518
   Batters (Table 6)      Swing at new strike (reduced form)            -1.248       0.652      0.652
   Batters (Table 6)      Reach two strikes (reduced form)              0.572        0.330      0.518
   Batters (Table 6)      Reach three balls (reduced form)              -0.345       0.449      0.518
   Batters (Table 6)      Two strikes, triple difference                0.773        0.065      0.327
   Batters (Table 6)      Hitter ahead, triple difference               0.693        0.420      0.518
   Batters (Table 6)      Star: walk                                    -0.324       0.466      0.518
   Batters (Table 6)      Star: strikeout                               1.311        0.027      0.274
   Batters (Table 6)      Star: on base                                 -0.886       0.179      0.518
   Batters (Table 6)      Star: plate-appearance value                  -5.682       0.401      0.518
   Pitchers (Table 5)     Acceleration, All pitchers                    0.018        0.072      0.143
   Pitchers (Table 5)     Acceleration, Left-handed                     0.058       <0.001     <0.001
   Pitchers (Table 5)     Acceleration, Right-handed                    0.005        0.667      0.800
   Pitchers (Table 5)     Acceleration, Side-arm                        -0.007       0.826      0.826
   Pitchers (Table 5)     Acceleration, Left-handed, balanced           0.052        0.003      0.009
   Pitchers (Table 5)     Acceleration, Right-handed, balanced          0.009        0.432      0.648
    Notes:     Columns report the estimate, its two-sided 𝑝-value from the original table, and the
   Benjamini–Hochberg 𝑞-value computed within each family of tests (the rows of one table).
   A 𝑞-value below 0.05 means that the expected share of false discoveries among tests at least
   as significant is below 5%.



    Table A9: Called-strike probability by region and season, relative to 2023

                              Human umpire                                       ABS
Region                     2021           2022             2024                  2025            2026
Zone, upper third    -16.1∗∗∗ (0.9)     -1.0 (0.7)     13.0∗∗∗ (0.5)      12.9∗∗∗ (0.5)       12.9∗∗∗ (0.5)
High edge            -14.8∗∗∗ (0.8)    -4.3∗∗∗ (0.8)    8.5∗∗∗ (0.8)        0.5 (0.9)           -0.2 (0.9)
Low edge                5.6∗∗∗ (1.1)   4.6∗∗∗ (1.0)    -18.5∗∗∗ (0.8)     -9.9∗∗∗ (0.9)      -10.4∗∗∗ (1.0)
Inside edge              2.3 (1.5)       1.8 (1.4)      8.2∗∗∗ (1.3)       9.8∗∗∗ (1.5)       9.5∗∗∗ (1.6)
Outside edge            5.0∗∗∗ (1.2)   9.8∗∗∗ (1.0)     -3.2∗∗∗ (1.0)      -2.7∗∗ (1.1)        -2.3∗∗ (1.1)
 Notes:      Columns report season coefficients relative to 2023, in percentage points, from linear
probability models of a called strike for pitches in each region, with pitcher, batter and month fixed
effects; regions are those of Table 2. The 2021 column precedes the KBO’s 2022 zone expansion.
∗∗∗ 𝑝 < 0.01, ∗∗ 𝑝 < 0.05, ∗ 𝑝 < 0.1 in two-sided 𝑡-tests with standard errors clustered by game.




                                                  40
                       Table A10: Star batters’ outcomes under alternative baselines

     Outcome                                                  Baseline 2022–2023             Baseline 2023 only
     Walk (pp)                                                     -0.32 (0.44)                  -0.59 (0.47)
     Strikeout (pp)                                                1.31∗∗ (0.59)                 1.89∗∗ (0.81)
     On base (pp)                                                  -0.89 (0.66)                 -2.03∗∗∗ (0.70)
     Plate-appearance value (wOBA points)                          -5.68 (6.77)                -22.35∗∗∗ (8.02)
      Notes:    Columns report the star × ABS coefficient from Panel D of Table 6, with
     the pre-ABS baseline defined as 2022–2023 (as in the paper) or as 2023 alone; pp
     denotes percentage points, and wOBA (weighted on-base average) values each plate-
     appearance outcome by its average contribution to scoring. ∗∗∗ 𝑝 < 0.01, ∗∗ 𝑝 < 0.05,
     ∗ 𝑝 < 0.1 in two-sided 𝑡-tests with standard errors clustered by batter.




                          Table A11: Why did only left-handed pitchers accelerate?

Explanation           Measure                                            Left-handed        Right-handed        Side-arm
Shock size            Mean gain from ABS re-judging (wOBA                    1.57               1.05               0.04
                      points per 1,000 pitches)
                      Share of pitches in gaining cells                      0.331              0.273             0.215
Timing                High-pitch share 2021 vs 2023 (pp)                 -1.21 (1.05)      -1.93∗∗∗ (0.51)    -5.44∗∗∗ (1.24)
                      High-pitch share 2022 vs 2023 (pp)                 -0.00 (0.76)      -1.52∗∗∗ (0.45)    -4.82∗∗∗ (1.11)
                      High-pitch share 2024 vs 2023 (pp)                2.80∗∗∗ (0.78)      3.93∗∗∗ (0.58)    3.53∗∗∗ (1.09)
                      High-pitch share 2025 vs 2023 (pp)                2.89∗∗∗ (0.79)      2.51∗∗∗ (0.65)     3.40∗ (1.93)
                      High-pitch share 2026 vs 2023 (pp)                  1.08 (0.90)       1.61∗∗∗ (0.57)    4.63∗∗∗ (1.51)
Matchup mix           Share of plate appearances against                     0.521              0.487             0.505
                      right-handed batters
Pitcher type          Four-seam fastball velocity (km/h)                    142.6               144.9             139.9
                      Share of border pitches                               0.348               0.349             0.351
Composition           Acceleration 𝐴, balanced panel                   0.052∗∗∗ (0.018)     0.009 (0.011)
Human calls           High-zone strike calls 2022 vs 2023,               -1.41 (0.90)            ref.         -3.74∗∗∗ (1.40)
                      relative to right-handed pitchers (pp)
 Notes:
 Columns compare left-handed, right-handed and side-arm pitchers using 2022–2023 pitches unless stated, and rows group
the measures by the candidate explanation they test; wOBA (weighted on-base average) values each plate-appearance out-
come by its average contribution to scoring, and pp denotes percentage points. The timing rows are within-pitcher season
coefficients of the high-pitch share (2023 omitted, standard errors clustered by pitcher), the acceleration row repeats Table
5 for the balanced panel, the last row compares human high-zone calls across pitcher hands at the same location (standard
errors clustered by game), and the remaining rows are descriptive. ∗∗∗ 𝑝 < 0.01, ∗∗ 𝑝 < 0.05, ∗ 𝑝 < 0.1 in two-sided tests.




                                                            41
                                                        Table A12: Home-team bias in calls

                                                                      Estimate (pp)        SE          N
                                         Home batter, pre-ABS               0.15          (0.24)     200,568
                                         Home batter × ABS                  -0.12         (0.26)     200,568
                                          Notes:      Columns report the coefficient in percentage
                                         points, its standard error and the number of border pitches,
                                         from a linear probability model of a called strike that com-
                                         pares home with away batters, with location-bin × season,
                                         pitcher, batter and home-plate-umpire fixed effects. ∗∗∗
                                         𝑝 < 0.01, ∗∗ 𝑝 < 0.05, ∗ 𝑝 < 0.1 in two-sided 𝑡-tests with
                                         standard errors clustered by game.




                                    2021                             2022                             2023




                         0.6



                         0.4


                                                                                                                         P(strike)
Height / batter height




                         0.2

                                                                                                                              0.75

                                    2024                             2025                             2026
                                                                                                                              0.50

                                                                                                                              0.25
                         0.6



                         0.4



                         0.2


                               −1    0         1              −1      0        1              −1       0       1
                                             Horizontal location (ft; positive = away from batter)



                                                   Figure A1: Called-strike probability by season
                  Notes: Predicted probability of a called strike from a tensor-product logit smooth of horizontal location and
                  height relative to the batter’s registered height, estimated separately by season. Black lines are 50% contours;
                  red dashed boxes are the ABS zone (2024 rule through 2024, 2025 rule thereafter). 2021 precedes the KBO’s
                  2022 official zone expansion.




                                                                          42
                                                           2




            Called−strike probability vs teammates (pp)
                                                           1




                                                           0




                                                          −1




                                                          −2


                                                               2021        2022        2023         2024          2025          2026


                                                                      Called pitches    2000       4000    6000          8000



                                                                      Figure A2: Catcher framing effects by season
Notes: Each point is a catcher-season estimate from Table 4, relative to teammates. Point size is the number of
called pitches. The dotted line marks the introduction of the ABS.




                                                                                              43
                                         2022 to 2023 (before ABS)                    2023 to 2024 (ABS introduced)
                                    3


                                    2


                                    1




                                                                                                                           Left−handed
                                    0
      Change in usage share (pp)




                                   −1


                                   −2


                                    3


                                    2




                                                                                                                           Right−handed
                                    1


                                    0


                                   −1


                                   −2


                                         0               20             40             0                20            40
                                        Mechanical value shock G (pitcher gain, wOBA points per 1,000 pitches)

                                                     Baseline pitches        2000   4000       6000



                                        Figure A3: Mechanical value shock and the change in usage
Notes: Each point is a cell (pitch type × vertical band × horizontal band). The horizontal axis is the cell’s
mechanical value shock 𝐺; the vertical axis is the change in its usage share. Lines are weighted least-squares
fits, and pp denotes percentage points. See Table 5.




                                                                         44

```
