<!-- source: library/preprints/arXiv/2026/2026 - Who Fills the Gap Role Similarity and Teammates' Minutes When NBA Players Are Ruled Out - Guan et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.34688 -->
<!-- authors: Tianyu Guan, Yang Zhou -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-26; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Who Fills the Gap? Role Similarity and Teammates' Minutes When NBA Players Are Ruled Out

                                           Who Fills the Gap? Role Similarity and Teammates’ Minutes When
                                                             NBA Players Are Ruled Out

                                                                               Tianyu Guan1,2,∗          Yang Zhou2
                                                           1 Department of Mathematics and Statistics, York University, Toronto, Canada
                                                                                 2 TY Sports Analytics Inc., Canada
arXiv:2611.34688v1 [stat.AP] 25 Nov 2026




                                                                              ∗ Corresponding author: tguan@yorku.ca




                                                                                              Abstract

                                              When a core player is ruled out before an NBA game, do teammates whose statistical role resembles that
                                              of the removed set (every rotation player ruled out, about three per case) play more? Using injury reports
                                              stamped at least six hours before tip-off and rosters reconstructed after the season, we study 2,441 team-
                                              games from 2023–24 to 2025–26 in which a core player was ruled out for a medical reason. Among
                                              teammates in the same game, one within-case standard deviation more similarity in role profile (three-
                                              point attempts, assists and rebounds per minute) goes with about 0.63 more minutes, holding reference
                                              minutes and headroom fixed (p < 0.0001); this compares teammates within a game, not the minutes
                                              gained because of the absence. The pattern holds in two earlier seasons and in exploratory within-
                                              player and without-and-with comparisons. Whether similarity adds to listed position is not settled. The
                                              association is small and yielded no statistically detectable reduction in the error of the retrospective
                                              minute forecasts we tested. Role coverage, how much of the missing minutes and roles the remaining
                                              rotation could restore, showed no consistent incremental association with team role output or the final
                                              margin.

                                              Keywords: injury reports; playing time; substitution; listed position; team production; basketball




                                                                                                  1
1    Introduction

From 2023–24 to 2025–26, the league’s official pregame injury report ruled out at least one of a team’s three

core players (those with the most reference minutes; Section 3.1) for a medical reason in more than a third

of team-games (2,441 of the 6,722 with a report filed by our cutoff). The coach then decides who plays the

missing minutes. This paper asks whether the allocation follows statistical role: whether teammates whose

profile resembles the absent players’ play more. The absent players are the removed set, every rotation

player ruled out for any reason (3.0 per case on average; Section 3.3), not only the core player who makes

the team-game a case, and similarity is to their combined profile. Which teammate replaces the core player

himself is a different question, which this design does not answer; the pair comparison of Section 5.2 comes

closest.

    Absences matter. Teams that lose more games to injury win less often (Podlog et al., 2015), the in-game

exit of a player who is both captain and All-Star lowers teammates’ plus-minus (Kocsoy, 2024), and betting

prices move when injury news arrives (Sauer, 2002; Dare et al., 2015). Teammates adjust. In the NHL,

the absence of a substitutable co-worker raises established teammates’ working time (Hoey et al., 2023).

In baseball, same-position replacements gain opportunity after star injuries (Nishihata, 2026), and in the

NBA, after in-game injuries of high performers teammates keep their division of tasks but produce less, and

relatively skilled players step in (Wegelin et al., 2022). These designs group teammates by task, by listed

position or by overall quality, and data-driven classifications have already moved beyond the five positions

(Muniz and Flamand, 2022). What has not been measured is, first, whether in games with a known pregame

absence a teammate plays more the more closely his statistical profile resembles that of the absent players

and, second, whether that carries information beyond listed position and past substitution.

    For every team-game of those three seasons we take the last official injury report whose header time

is at least six hours before tip-off, each player’s recent games, and the roster, which we reconstruct after

the season where the league’s records are incomplete (Section 2.2). We call a team-game a case when that

report rules out, for a medical reason, at least one of the team’s three core players. Reference minutes divide

the game’s 240 minutes among the roster according to each player’s recent games (Section 3.1). Two earlier

seasons (2021–22 and 2022–23), in which our role measures had never been related to any outcome, serve

as a second sample. We planned three tests.

    • Allocation. In cases, do teammates whose statistical role is closer to that of the absent players play


                                                      2
        more minutes relative to their reference minutes?

      • Role output. When the retained roster can cover less of a missing role, does the team produce less of

        that role in the game?

      • Margin. Does the roster’s ability to cover the missing roles explain the final margin, beyond the value

        of the players who are missing?

      The first test uses role similarity, the cosine between a teammate’s standardised per-minute rates of three-

point attempts, assists and rebounds and those of the absent players (Section 3.3). The other two use role

coverage, the share the retained rotation could restore: of each role for the role-output test (ck ), and jointly,

of the absent players’ minutes and every role at once under one budget of extra minutes, for the margin test;

no player may exceed his 90th percentile of minutes (at most 40).

      The main finding is that minutes tilt toward similar teammates: within a case, a teammate one within-

case standard deviation more similar to the removed set plays about 0.63 more minutes than a teammate

with the same reference minutes and headroom. This is a difference between teammates of one game,

not the minutes a teammate gains because of the absence, which only the exploratory comparisons of a

teammate’s games without and with a given core player approach, and less precisely (Section 5.2). The

association recurs in two earlier seasons; it is small and did not yield a statistically detectable reduction in

the error of the retrospective forecasts we tested. Whether it carries information beyond listed position is left

open: part of it survives position controls over all cases, but in cases whose absent players share one listed

position and in pairs with both players’ effects the estimates fall to 0.20 and −0.02 minutes per unit and

are imprecise. The second finding is negative: the planned role-output test misses its threshold (p = 0.070),

and role coverage adds no stable information about team role output beyond the absent players’ share of

each role, or about the final margin beyond the value of the missing players (Section 9.3). Both rest on a

point-in-time reconstruction of the injury reports that this paper shares with a companion paper (Section 2).


1.1     Related work

Absences, teammates and substitutes. An injured second-tier star lowers a European football team’s

goal difference (Jedelhauser et al., 2023), and on NBA teams with a single star, losing a star who is a

generalist across play types costs more than losing a specialist (Nalbantis et al., 2026). Who replaces whom

has been studied mostly by position: when COVID-19 kept foreign players out of the Chinese Basketball

                                                         3
Association, domestic players at the affected positions gained minutes (Jin et al., 2026). Outside sport,

coworkers in the same occupation earn more after a worker dies, evidence of substitution between workers

and of its cost (Jäger and Heining, 2022), and in Danish small firms parental leave costs firms little except

where no coworker in the same occupation can cover (Brenøe et al., 2024); both point to the availability of

close substitutes, which our coverage measure quantifies for a roster. Absences also change how teams work

together (Chen and Garg, 2018; Stuart, 2017), and give rookies playing time that affects their later contracts

(Hoey, 2026). A recent NBA study, Krishna et al. (2026), uses the number of a player’s absent teammates

in the games of 2017–18 to 2022–23 as an instrument for his minutes, finds that workload raises injury risk

and that coaches rest players after shocks to that risk; it counts absent teammates without regard to who

they are and does not ask which teammates absorb the minutes. Here the absence is fixed by the pregame

report, and the question is how the freed minutes are divided among the retained players according to their

role similarity to the absent ones. Absences are not random: whether NBA stars miss a game depends on

injuries, back-to-backs, the point in the season and the opponent (Reilly et al., 2023). Betting markets react

to injury and illness news, though not always at once (Fischer and Schmal, 2025).

    Roles beyond listed position. Data-driven roles replace the five positions in many studies: clustering

yields thirteen (Alagappan, 2012), self-organising maps with fuzzy clustering five (Bianchi et al., 2017),

weighted networks eight (Muniz and Flamand, 2022), and principal components with k-means five in 2025–

26 (Rodriguez-Idiazabal et al., 2026); cosine distance has been used to cluster lineup-based playing styles

(Guo et al., 2025). Listed position nonetheless stays informative: it still accounts for about a quarter of

the variation in players’ statistical profiles, although dispersion within positions has grown (Durmuş et al.,

2026), and archetypes add only modest gains over positions in models of team defence (South, 2025).

Similarity on components of tracking statistics has been proposed to find cheaper replacements (Bruce,

2016). A critical integrative review of NBA analytics proposes a framework for judging whether evidence

is ready to inform decisions and discusses role substitution and player availability (Zhou and Guan, 2026).

We ask instead whether, after a pregame absence, teammates’ minutes are associated with their continuous

role similarity to the absent players, and whether that association goes beyond listed position.

    Allocation of playing time. Whether draft position affects minutes beyond performance is disputed

(Staw and Hoang, 1995; Camerer and Weber, 1999); adjusting for the games a player was available and

using a discontinuity at draft-position thresholds, Leeds et al. (2015) find no evidence that highly drafted

players receive extra time. How evenly a team spreads minutes over a season is associated with its wins

                                                      4
(Cardazzi et al., 2024). Team points have been related to the ice time given to data-driven NHL player types,

with a tool that projects reallocations (Chan et al., 2012), and NBA rosters have been chosen by mixed-

integer nonlinear programming that values synergies between archetypes (Muniz and Flamand, 2023). Our

coverage program asks a narrower question in each game: how far the retained rotation could restore the

absent players’ minutes and roles under one budget and each player’s capacity. Shot allocation has been

evaluated for efficiency (Goldman and Rao, 2011; Sandholtz et al., 2020), and inverse optimisation recovers

decision-makers’ objectives (Chan et al., 2025; Sandholtz et al., 2024). Skill sets complement one another

(Kuehn, 2017; Maymin et al., 2013), productivity spillovers matter for team output (Arcidiacono et al.,

2017), and efficiency is expected to fall as a player’s usage rises (Skinner and Goldman, 2017); coverage

holds role rates fixed and so describes a scenario, not what the remaining players would produce.



2     Data and information timing

We study the 2023–24 to 2025–26 NBA seasons: 3,690 regular-season games and the three NBA Cup finals,

which ESPN lists with them but which count in no standings. The finals contain no case but, like all games,

enter player histories and ten-game baselines. The two preceding seasons (2,460 team-games each) form the

second sample (Section 7); their reports were parsed with the same parser, adapted to the older layout. They

list COVID-19 absences under the league’s health and safety protocols, which our reason classes count as

medical. Seasons from 2019–20 enter only as player history. The data construction is shared with a separate

paper by the same authors on a different question (Guan and Zhou, 2026); the two papers share nothing else.


2.1    Sources

      • Games and box scores. ESPN game summaries (8,292 games, 2019–20 to 2025–26): start time, final

       score and every listed player with minutes and box statistics. The summaries also embed an injury

       block that is updated after the game; we do not use it.

      • Official injury reports. Every PDF injury report the league’s server holds for the game days of

       October 2021 to April 2026 from midnight (US Eastern) to 90 minutes before the day’s last tip-off

       (23,485 reports), hourly and, from 22 December 2025, every 15 minutes. Collection stopped at that

       endpoint, not publication: the server also holds 1,787 later reports of those days, which we did not

       use. None of them can meet a cutoff six hours or 90 minutes before a game’s own tip-off, so they

                                                       5
        change no selected report and nothing in this paper. Our parser, which assigns each word to a column

        by its position, parsed every report. On an earlier version of the data (about five reports per game day),

        its Out list agreed with a parse from our earlier work in 99.8% of the 5,978 team-games both covered.

        We time each report by the time printed in its header, the earliest time it can have been public; until 22

        December 2025 file names carry only the hour and are 30 minutes earlier (45 minutes for 57 reports

        of 19 to 22 December 2025), an offset that the examples of Abramson (2021) also show.

      • Transactions and attributes. The league’s player-movement log (6,716 signings, waivers and trades)

        and season-level listed position and height from Basketball-Reference roster rows, matched to players

        by team and season (one removed player of the earlier seasons has no roster row), used for position

        and forecasts.

      • Play-by-play and betting lines. The ESPN summaries also hold the play-by-play, from which we

        reconstruct lineup stints (the stretches between substitutions) for the substitution-partner share and a

        plus-minus measure, and closing spreads for 2021–22, 2022–23 and 2025–26. The stints reproduce

        the final score exactly in 57.8% of games (92.3% within four points for each team); recomputed from

        the games whose stints pass our validation checks (44% of the games before 2024–25), both measures

        give similar estimates and the same conclusions (Supplementary Tables S45 and S47).


2.2    The pregame information set

The information cutoff is six hours before scheduled tip-off. A player belongs to a team if his most recent

event before the cutoff (a box-score listing, a signing, a trade or a claim) ties him to that team and he has

not since been waived; a player listed on the team’s injury report is added unless he is known to belong to

another team. The movement log has no contract expirations, so a player whose last tie to a team is from an

earlier season stays on it only if his first record of the new season (a box-score row, a listing, a signing, a

trade or a waiver) is a box-score row or listing for that team, or a waiver (a re-signing does not count); this

uses records after the cutoff and reconstructs the roster after the fact. A ten-day contract ends after ten days

or three team games, whichever is longer, unless renewed, and transactions, dated by day, count from the

end of their day (Section 8). Each player’s status (Out, Doubtful, Questionable, Probable, Available) and

reason come from the last official report whose header time is at or before the cutoff (equal to it in 51% of

cases; Section 8) in which the team’s block (its section of the report) was submitted; ruled Out below means


                                                         6
this status. Reasons are kept distinct (medical, G League assignment, personal, suspension, rest, trade

pending, ineligible, unknown). These classes count “Coach’s Decision” as medical (25 of 26,554 medical

Out rows) and a bare “Not With Team” as personal (688 rows); a correction written after the analyses were

frozen separates both. It changes no case or removed set and none of the estimates, only one descriptive

count in the Supplementary Material, so the tables were not rebuilt with it (Section S4). Player history is

each player’s last 20 regular-season games (counting the NBA Cup finals) with positive minutes that ended

before the cutoff, within 365 days, for any team. Besides this roster rule, two preprocessing steps use

information from after the cutoff. Role rates are standardised with the moments of the analysed seasons,

so we repeat the allocation test with the previous season’s moments (Supplementary Tables S43 and S45).

Listed positions and heights are season-level values. Apart from the holdover rule, whose first record of the

season can be the case game itself, and the end of ten-day contracts, which can depend on the following

days, actual participation, minutes and scores from the same game enter only as outcomes. The rosters and

these two steps are thus not as known at the cutoff: the analysis is retrospective, not a simulation of forecasts

made at the time.


2.3     Missing report blocks and the number of cases

At the six-hour cutoff, 664 team-games (9.0%) have no submitted block for the team in any report stamped

by then. Under the 2025–26 rules most game-day reports are due between 11 a.m. and 1 p.m. local time

(National Basketball Association, 2025), close to a 1 p.m. cutoff for a 7 p.m. tip-off. A core player sat out

in 50.6% of team-games with missing blocks and in 47.6% of the rest, so selective missingness cannot be

ruled out. Team-games without a block are left out of case identification rather than treated as healthy. A

hybrid sample, added after the first results, fills them with the last report stamped 90 minutes or more before

tip-off and serves as a sensitivity analysis.

      The 2025–26 season has 1,058 cases (43.0% of team-games), against 630 (25.6%) in 2023–24 and 753

(30.6%) in 2024–25. Three things rose together: more blocks had been filed by the cutoff, core players

missed more games according to the box scores, and a core player who sat out was more often already listed

Out, for any reason, at the cutoff (Supplementary Table S53).




                                                       7
2.4     Validation and hand checks

The authors made two hand checks. First, for 184 team-games of four teams in 2023–24 they reconstructed

rosters, report statuses and participation by hand from official transactions and reports, split between the

authors. Table 1 compares the automated pipeline with this subset. Of the 89 cases the pipeline finds in

these team-games, 74 are cases in the audit. The other 15 fall in team-games whose rosters the audit could

not verify; a separate check of their source records confirms 14, and the authors, checking all 15, agree

and class the fifteenth, a return-to-competition reconditioning after a non-medical absence, as not medical,

although our reason rule counts it; without it the tests barely change (Supplementary Table S3). Second, for

80 team-games from all five seasons, 28 of them from the two earlier seasons, they compared the report the

pipeline selected, its Out list, and its statuses and reasons with the source reports. The selected report and

the Out list agreed in all 80. Statuses and reasons agreed in 78, and the two disagreements, reasons that ran

across a page break, led to a correction of the parser. A further 40 team-games of the two earlier seasons,

half of them cases, were then checked in the same way and agreed on every item. A check that needs no

hand work: a core player listed Out at the cutoff played in only 8 of 5,171 instances (Supplementary Table

S53). Every disagreement, in either sample, is a player listed Out in the report the pipeline selected; the 31

at six hours (28 with no report for the team at the cutoff in the reconstruction) are all in reports stamped

exactly at the cutoff and disappear with reports stamped strictly before it (Supplementary Tables S3 and

S72).

Table 1: Pipeline versus the hand-reconstructed subset of 184 team-games (six-hour cutoff). The remaining
Out disagreements are players the pipeline lists as Out and the audit does not (31 of 734). Ties in reference
minutes at the third place (about 1% of team-games) are broken by player identifier, here as in the pipeline.

              Check                                                  Agreement         n

              Rotation players in audited roster found by pipeline   99.9%             2,544
              Pipeline rotation players in audited roster            98.8%             2,573
              Pregame Out status agreement                           99.1%             3,431
              Out recall / precision                                 100.0% / 95.8%    703 / 734
              Identical three-player reference core                  98.9%             184
              Audited cases recovered                                100% (74 of 74)   74
              Coverage absolute error, median / 90th percentile      0.000 / 0.001     74




                                                            8
3     Measures

3.1   Reference rotation

A roster member is supported if his history has at least 5 games and 100 minutes and no more than 20 of

the team’s scheduled games have passed since his last appearance. For supported player j, let m̄ j be his

mean minutes and u j = min(40, q j ) his minutes capacity, where q j is the 90th percentile of his minutes. The

reference rotation, which we also call the reference allocation, divides the 240 minutes of a regulation game

among the supported players in three steps; the resulting b j are reference minutes. First, the minutes are

shared in proportion to m̄ j . Second, every player whose share exceeds u j is set to u j and leaves the pool

together with those minutes. Third, the first two steps are repeated on the remaining players and minutes

until no share exceeds a capacity (algorithm in Supplementary Section S1). The rotation uses only games

that ended before the cutoff and includes every supported player, whether or not he is ruled Out. It is a

full-roster baseline, not an estimate of what each player would play with nobody absent. The three players

with the largest b j form the reference core.


3.2   Role rates

For each role k (three-point attempts, assists and total rebounds per minute) a player’s rate r jk is shrunk, with

a weight of 100 pseudo-minutes, toward the pooled rate of his teammates (the player himself excluded):

                                                         n jk + 100 r̄− j,k
                                                r jk =                                                        (1)
                                                             M j + 100

where n jk is his count, M j his minutes in the history window and r̄− j,k that pooled rate.


3.3   Role similarity

Role similarity compares a teammate’s profile with that of the absent players. Each rate is standardised over

the player rows of all team-games with a core player ruled Out in the seasons analysed, z jk = (r jk − µk )/σk :

the three main seasons, the two earlier ones (Section 7), all five in five-season pools, and the two training

seasons for the forecasts (Section 5.5; Supplementary Section S1). Let R be the supported players ruled

Out at the cutoff for any reason, the removed set: 3.0 per case on average (median 3), the medically absent

core players and any others. Its profile is the reference-minute-weighted mean of its members’ standardised


                                                             9
rates, and similarity is the cosine between the two profiles:


                                              ∑a∈R ba zak                    ∑k z jk z̄Rk
                                     z̄Rk =               ,        sim j =                 .                (2)
                                               ∑a∈R ba                       ∥z j ∥ ∥z̄R ∥

      Similarity lies between −1 and 1, and its within-case standard deviation (the root mean square deviation

from the case mean) is 0.58. It is high when a teammate is above or below average in the same roles as the

removed set, whatever his minutes. The removed set’s profile is never zero (minimum norm 0.06, median

1.00); without the 29 cases below 0.2 the coefficient of Section 5.1 is almost unchanged (1.10 against 1.09;

Supplementary Table S64). An example: when Philadelphia hosted Milwaukee on 25 February 2024, the

removed set was the starting centre, Joel Embiid, and one reserve (30.7 reference minutes together). Its

profile had few three-point attempts, above-average assists and many rebounds (standardised rates −0.71,

0.77 and 1.65). The two reserve big men had the highest similarity (0.76 and 0.65), and one of them, Paul

Reed, played 27 minutes against 16.4 reference minutes (Table S55).


3.4     Role coverage

The removed set (the supported players ruled Out; Section 4) leaves L = ∑a∈R ba reference minutes and role

demands Dk = ∑a∈R ba rak . Each retained player j (any other supported player) keeps his reference minutes

and can add x j ≤ h j = max(u j − b j , 0), his headroom. Coverage is the largest fraction θ of the removed

minutes and of every role demand that one set of extra minutes can restore at the same time:


                 coverage = max θ
                              θ,x

                        subject to    ∑ j x j ≤ L,          ∑ j x j ≥ θ L,
                                                                                                            (3)
                                      ∑ j r jk x j ≥ θ Dk     for every role k,

                                      0 ≤ xj ≤ hj       for every retained player j,           0 ≤ θ ≤ 1.

      The same minute counts toward every role, so a player cannot cover rebounds and assists with separate

minutes. The model describes a scenario and is not an upper bound on real substitutability: it keeps every

retained player at least at his reference minutes, lets no one exceed his capacity and holds role rates fixed.

In the games themselves, 29.5% of retained players played fewer minutes than their reference minutes

(15.5% did not play), 15.4% more than their capacity, and players outside the reference rotation played


                                                              10
minutes equal to 16% of the removed reference minutes (Supplementary Table S46). The shared budget

lowers coverage below the smallest separate bound (minutes or one role) by 0.014 on average (median 0;

Supplementary Table S46).

    For the role-output test we also compute coverage for each role separately, ck = min(1, Sk /Dk ), where Sk

is the largest amount of role k that the retained players can supply with at most L extra minutes within their

headroom (Supplementary Section S1). Among the 2,441 primary cases, median joint coverage is 0.951;

39.2% reach 1.



4      Empirical design

Cases. A case is a team-game in which at least one reference-core player is ruled Out for a medical reason

at the cutoff. The primary six-hour sample has 2,441 cases in 2,013 games, covering all 30 teams and 348

distinct combinations of team and absent core players. The removed set contains every supported player

ruled Out for any reason, on average 3.0 per case; the other supported players are the retained players.

Most cases lie inside longer absences: in 59.2% the same core players were also out in the team’s previous

game, and in only 3.9% of cases had every removed player played in that game (Supplementary Table S40).

Supplementary Section S1 defines every variable.

    Planned tests. Three tests were planned: their specifications, samples, three sensitivity analyses (Sec-

tion 8) and pass rules were recorded in our version history before any relationship between a role measure

and an outcome was computed. That history is our own record; these plans were not registered externally

(Nosek et al., 2018), unlike the 2026–27 replication (Section 9.2). In earlier work on these data we had seen

the final scores of all five seasons, fitted models of player value and team production, and compared scores

with betting lines; we had not related role similarity or coverage to any outcome (Supplementary Section

S4).

    Allocation test. The unit is retained player j in case i, and the outcome is his extra minutes, his actual

minutes (zero if he did not play) minus his reference minutes:


                                 ∆mini j = β simi j + γ1 bi j + γ2 hi j + αi + εi j ,                      (4)


where bi j and hi j are his reference minutes and headroom in that case and αi is a case fixed effect. Because



                                                         11
bi j is a regressor, β is also the coefficient of the same model with actual minutes as the outcome: it compares

teammates with equal reference minutes and headroom in one case, not a teammate’s minutes with and

without the absence, which Section 5.2 compares.

    Role-output test. The unit is a case and role, and the outcome is role output: the team’s in-game total of

the role over its mean in the previous ten games, minus one. The regressors are single-dimension coverage

ck , the removed minute share (removed reference minutes divided by 240) and role dummies.

    Margin test. The unit is the case and the outcome is the final margin. The regressors are cover-

age, the removed minute share, lost value, strength difference, a home indicator and rest difference. Lost

value weights each removed player’s reference minutes by his box-score efficiency per minute in his history

games; absence value is the same quantity for every team-game with a report block. Strength difference is

the difference between the two teams’ mean margins over their previous ten games, and rest difference the

difference in days since each team’s previous game, each capped at three (Supplementary Section S1).

    Pass rule and inference. Each test passes if its key coefficient is positive with two-sided p < 0.05;

it is called robust to measurement if it also passes in at least 8 of 10 alternative definitions, a rule written

after the first results (Section 8). Standard errors (SE) are clustered by team (30 clusters, CR1 correc-

tion, t-tests with 29 degrees of freedom; fewer clusters in some pair comparisons). Adjusted for the three

planned tests (Holm), the role-output p is 0.14; the exploratory analyses are not corrected for multiplicity.

Because 30 clusters are few (MacKinnon et al., 2023), we also report wild cluster restricted bootstrap p-

values (Cameron et al., 2008) with 9,999 draws and Webb weights (Webb, 2023); some later checks use

Rademacher weights. With absorbed fixed effects, all nested within teams, the small-sample factor counts

only the explicit regressors (Correia, 2015; see Cameron and Miller, 2015); counting the absorbed effects

too would widen the standard errors we report by 4% to 13%, or 18% to 60% with teammate or removed-set

effects (Supplementary Table S58).

    Exploratory analyses. Everything else is exploratory; a few later analyses had a pass rule written before

they were run, and most were added after the main results were known. Supplementary Section S4 and Table

S71 give the planned tests, their verdicts and the deviations that bear on them; the analysis record released

with the code gives each plan, its timing and every deviation. A replication of the allocation test, without

and with listed position and height, on the 2026–27 season was registered on the Open Science Framework

on 30 September 2026, before the season began, and will be judged once, at the end of the regular season.

A final exploratory analysis (Sections 5.3 and 6.3), decided after all other results were known, was specified

                                                      12
before it was run in a working log, not in the version history (Supplementary Section S4).



5      Results: role similarity and minutes

Table 2 gives the planned tests and their verdicts; this section and the next discuss the allocation test and the

coverage tests in turn, and Section 7 the earlier seasons.


5.1    Minutes tilt toward similar teammates

Within a case, teammates whose role profile is closer to that of the absent players play more minutes than

teammates with the same reference minutes and headroom. In the primary sample, a one-unit increase in

role similarity is associated with 1.09 more minutes (SE 0.18; p < 0.0001; wild bootstrap p ≤ 0.0001;

28,118 player-cases), holding reference minutes and headroom fixed. One within-case standard deviation

of similarity (0.58) thus corresponds to about 0.63 minutes more than such a teammate receives. Figure 1

shows the relationship net of the case, reference minutes and headroom. With splines, deciles or decile-

by-quintile cells for reference minutes and headroom, the coefficient changes by at most 5% (1.14; earlier

seasons 8%, 1.29; exploratory; Supplementary Table S65).

Table 2: The planned tests, six-hour cutoff: coefficient and 95% interval (team-clustered; for the margin test,
coverage per 0.1 with the 90% interval of the equivalence test), in the main seasons (2023–24 to 2025–26,
2,441 cases), the earlier seasons (2021–22, 2022–23, 1,466 cases) and all five seasons (3,907 cases). The
verdict applies the pass rule of Section 4 to the main seasons; the position-and-height row (P3 addendum A)
was specified after the first results of the other rows and before its own. Details in Supplementary Tables S5
to S8, S21, S23, S30 and S71.

Test                          Main seasons             Earlier seasons         Five seasons             Verdict (main)

Allocation: role similarity   1.09 [0.72, 1.46]        1.20 [0.67, 1.72]       1.14 [0.85, 1.43]        passes
and extra minutes                                                                                       (p < 0.0001)
Allocation, with position     0.89 [0.51, 1.28]        0.91 [0.40, 1.41]       0.92 [0.62, 1.22]        passes
and height                                                                                              (p < 0.0001)
Role output:                  0.054 [−0.005, 0.114]    0.100 [0.047, 0.153]    0.070 [0.029, 0.112]     does not pass
single-dimension coverage                                                                               (p = 0.070)
Role output, with the         −0.053 [−0.126, 0.021]   0.068 [−0.009, 0.144]   −0.002 [−0.064, 0.060]   –
benchmark (exploratory)
Margin: coverage per 0.1,     −0.10 [−0.58, +0.39]     +0.24 [−0.31, +0.80]    +0.05 [−0.32, +0.42]     does not pass
90% interval                                                                                            (p = 0.73)



                                                          13
    Because reference minutes enter both the outcome and the regressors (Section 4), this is a conditional

difference between teammates of one game: it says who plays longer in that game, not who gains minutes

because of the absence. The comparisons of Section 5.2 come closer to the second question: 1.54 minutes

per unit of similarity between a teammate’s games without and with a given core player, but 0.77 (95%

interval −0.09 to 1.62) in the 168 spells whose windows remove a linear drift.


                                                    1.5
                        Extra minutes (residual)




                                                    1.0

                                                    0.5

                                                    0.0

                                                   −0.5

                                                   −1.0


                                                     −1.00 −0.75 −0.50 −0.25 0.00 0.25 0.50       0.75   1.00
                                                                     Role similarity (residual)


Figure 1: Partial relation between role similarity and extra minutes, net of case fixed effects, reference
minutes and headroom (primary sample, 28,118 player-cases). Points are means within deciles of residual
similarity; bars are 95% team-cluster bootstrap intervals; the dashed line is the regression slope (1.09 min-
utes per unit).


    The association is small. The partial R-squared of similarity is 0.45%, against 3.4% for reference min-

utes and headroom together, and extra minutes have a within-case standard deviation of 9.6 minutes (Sup-

plementary Table S52). The pattern describes allocation and is not evidence of how coaches decide. Because

the profiles come from recent games that often include the current absence (Section 4), similarity describes

current roles, possibly already adapted to the absence. Two checks point the other way: Section 5.3 also

measures similarity before the absence (1.01 in the pair comparison without position terms), and the gradi-

ent is larger in the first game of a run of absences than in the games that follow (Section 5.4). Split into parts

(exploratory; Supplementary Table S64), it reflects both whether a teammate plays (1.1 percentage points

per standard deviation; 85% play) and his minutes when he does (0.50 minutes per standard deviation).

The coefficient barely moves when the teammate’s own pregame status is added (1.00) or teammates listed

Questionable or Doubtful are left out (1.08; exploratory; Supplementary Table S61).




                                                                            14
5.2     Games without and with the absent player

Extra minutes are measured against reference minutes, and reference minutes come from a history in which

the absent players are often already absent (Section 4). The coefficient above is therefore a deviation from

a mixed baseline, not the difference between a teammate’s minutes without and with a given player. An

exploratory analysis makes that comparison directly, with an outcome that does not use the reference alloca-

tion (Supplementary Table S49). The unit is a pair. One member is a core player who, within a team-season,

was ruled Out for a medical reason in at least five cases and played in at least five of the team’s other games

with a report block. The other is a teammate observed in at least three games of each kind. The outcome

is the teammate’s mean minutes in the games without the core player minus his mean minutes in the games

with him, where a game in which the teammate did not play counts as zero and a game for which he was

himself ruled Out is left out. We regress this difference on the similarity of the two players (the cosine

of their standardised rates, averaged over the games without the core player), with a fixed effect for each

absent player in each team-season. The teammate’s mean reference minutes and headroom in those games

are controls; the reference rotation still defines who is a core player and which teammates enter.

      The primary sample gives 2,653 such pairs, built around 199 combinations of absent player, team and

season. Teammates play 2.9 minutes more on average in the games without the absent player, and 1.54

minutes more per unit of similarity to him (SE 0.19; 95% interval 1.15 to 1.93; wild bootstrap p ≤ 0.0001).

The estimate is 1.30 (SE 0.26) when the absent player is the only core player out and no core player is out

in the comparison games, and 1.41 (SE 0.29) in the two earlier seasons.

      Without a teammate effect, a teammate who gains minutes whenever any core player is absent would

contribute to this estimate. With a fixed effect for each teammate in each team-season, each teammate is

compared only with himself across the absent players he is paired with, in the 2,168 pairs in which the

teammate (828 teammate-seasons) is paired with two or more absent players. The estimate is 1.23 (SE 0.25,

or 0.33 with the absorbed effects counted; 95% interval 0.73 to 1.73; wild bootstrap p = 0.0003), against

1.52 on the same pairs without teammate effects, and 1.62 (SE 0.42) in the earlier seasons (Supplementary

Table S56).

      The comparison is still observational: games without and with a player differ in date and opponent,

and a teammate’s place in the rotation can change over a season. Windows of three games on each side of

the start and of the end of a spell of absence cancel a drift linear in the team’s game number, though not



                                                      15
necessarily one linear in calendar time (Supplementary Table S60). In the 168 spells with both windows the

gradient is 0.77 (SE 0.42; −0.09 to 1.62), too imprecise to tell. In the games before a spell, which involve

no change of status, no gradient is detected; in the earlier seasons the windows give 2.43 (1.72 to 3.15).


5.3     Position, height, past substitution and player effects

Similarity might simply recode listed position or the absent players’ usual backups. Two kinds of evidence

bear on this: how the coefficient changes when position controls are added within one sample, and whether

what remains is the same across designs (Table 3; Supplementary Section S6 gives the full account). Three

position groups (guard, forward, centre) and the height gap leave 82% of the coefficient (Supplementary

Table S6). On one common sample (Table 3, rows 1 to 7), adding a substitution-partner share, how often

the teammate was on court during an absent player’s bench possessions in his recent games, leaves 72%;

indicators for every pairing of the teammate’s five listed positions with the removed set’s main position (the

one holding most of its reference minutes) leave 63%; and the share of the removed reference minutes at

each listed position, interacted with the teammate’s position, leaves 45%, or 53% with player effects.

      Two designs describe listed position completely, although listed position is not actual role. In the 455

cases whose removed players share one listed position, the pairings and the height gap take the coefficient

from 1.05 to 0.37 (−0.44 to 1.18), and adding the partner share to 0.20 (row 9). In the pair comparison of

Section 5.2, on the 1,278 pairs with a game before the absence (1.30 there without position terms, against

1.23 on all pairs), with the 25 pairings of the two players’ listed positions, their height gap, absent-player

and teammate effects and similarity measured before the absence, it falls from 1.01 to −0.02 (−0.72 to 0.67;

rows 10 and 11). No association beyond position is detected in these designs, but one of 0.54 minutes per

unit of similarity, the size the plan of the pair analysis called meaningful (0.3 minutes per standard deviation,

about half the 0.63 of Section 5.1), cannot be excluded (one-position minus other cases: −0.56, p = 0.22);

with absent-player effects only the pair estimate is 0.60 (−0.05 to 1.25), or 0.72 (0.19 to 1.25) on all 1,788

pairs with similarity before the absence, and in the earlier seasons the pair model gives 0.85 (row 13). The

cases and the pairs differ in more than the position control (unit, sample, outcome, timing of similarity, fixed

effects), so the gap between them is not the effect of a more complete control alone.




                                                       16
Table 3: Role similarity with position, height, substitution and player controls, in three designs that differ
in more than the controls. Panel A, rows 1 to 7: the allocation test on one common sample (27,896 player-
cases in 2,423 cases with every teammate control available); player effects are player-by-team-by-season
fixed effects; share kept is relative to the similarity-only model with the same fixed effects. Panel B, rows
8 and 9: the 455 of these cases (5,775 player-cases) in which every removed player has the same listed
position. Panel C, rows 10 to 13: the comparison of games without and with the absent player (Section 5.2).
All rows are exploratory. Other models and the earlier seasons are in Supplementary Tables S45, S50, S56,
S57, S58, S59 and S63.

 Model (all with reference minutes and headroom)                     Similarity (SE)   95% interval    Share kept

 A. All cases (2,423), case effects
 (1) Similarity only                                                 1.10 (0.18)       0.73 to 1.47
 (2) Three position groups, height gap, partner share                0.79 (0.19)       0.41 to 1.17    72%
 (3) Every position pairing, height gap, partner share               0.69 (0.17)       0.35 to 1.04    63%
 (4) Positions of all removed players, height gap, partner share     0.49 (0.17)       0.15 to 0.84    45%
 A, continued: case and player effects
 (5) Similarity only                                                 1.40 (0.20)       0.98 to 1.82
 (6) Every position pairing, height gap, partner share               0.93 (0.23)       0.47 to 1.39    66%
 (7) Positions of all removed players, height gap, partner share     0.75 (0.22)       0.30 to 1.19    53%
 B. One-position cases (455), case effects
 (8) Similarity only                                                 1.05 (0.32)       0.40 to 1.70
 (9) Every position pairing, height gap, partner share               0.20 (0.41)       −0.64 to 1.04
 C. Pairs (1,278; row 13: 914), similarity before the absence
 (10) Absent-player and teammate effects                             1.01 (0.32)       0.36 to 1.66
 (11) Both effects, position pairings and height gap                 −0.02 (0.34)      −0.72 to 0.67
 (12) Absent-player effects only, position pairings and height gap   0.60 (0.32)       −0.05 to 1.25
 (13) Earlier seasons (914), as row 11                               0.85 (0.58)       −0.34 to 2.04



    Case fixed effects absorb who is absent, but not a teammate’s place in the rotation. With player-by-

team-by-season fixed effects the coefficient rests on changes in the same player’s similarity across his cases,

almost all between cases with different removed sets: it is 1.38 (0.95 to 1.81) on all primary cases and 0.93

with every position pairing, the height gap and the partner share (row 6), so a place in the rotation that is the

same in all of a player’s cases in a season does not account for the association; player effects do not absorb

his being the regular replacement of one particular teammate, which the partner share addresses only in part.

    Two exploratory analyses ask which roles carry the gradient and what happens when position and role


                                                         17
disagree (Supplementary Tables S66 to S68). Entered jointly as separate regressors, with the teammate’s

own scaled rates as controls, the three role components of similarity give 0.75 minutes per unit for three-

point attempts, 1.01 for assists and 1.76 for rebounds, and their equality is not rejected (p = 0.070); with

the controls of Table 3, row 3, and own status the rebound component remains positive (1.03; 0.52 to 1.55),

and it and the assist component come from absences of players who rebound much and pass little, mostly

forwards and centres. In the 280 cases with one removed player that contain both a teammate of his position

group with low similarity and one of another group with high similarity, the second plays 0.15 minutes more

(−0.83 to 1.13), an interval too wide to tell which criterion the allocation follows.


5.4     Placebo and subsamples

Figure 2 collects the main estimates of this section and of the earlier seasons (Section 7). Every real-absence

row without the position pairings of Section 5.3 has a positive coefficient whose 95% interval excludes zero,

and both placebo intervals include zero.

      In a placebo with the 3,522 team-games in which all three core players took part, treating each in

turn as absent, the similarity gradient is slightly negative (−0.16 per unit, SE 0.09; −0.21, p = 0.026,

with one pseudo-absent core player drawn at random), as expected if similar teammates compete for the

same minutes when the core player plays or if reference minutes already reflect earlier absences, and the

real-minus-placebo difference is 1.25 (SE 0.20, p < 0.0001; Supplementary Table S18). Because placebo

similarity refers to one player, a closer contrast takes the 353 cases with one removed player (0.98, p =

0.007) and the 846 placebo team-games in which no supported player was ruled Out (−0.07, SE 0.10): the

difference is 1.05 (SE 0.35, p = 0.005; wild bootstrap p = 0.007; exploratory; Supplementary Table S48).

      The association also holds with Euclidean distance and in the 406 cases in which only core players were

removed, and it is larger in the first game of a run of absences (1.32) than in the games that follow, where it

remains positive (Supplementary Tables S35, S40 and S54).


5.5     Forecasts

In the retrospective allocation models we tested, similarity did not yield a statistically detectable reduction

in the mean absolute error of minute forecasts. Regressions fitted to the hybrid cases of 2023–24 and

2024–25, with role rates standardised on those two seasons alone, and evaluated on the 1,139 of 2025–



                                                      18
      Primary sample, 2023–24 to 2025–26
        Planned allocation test                                                                    1.09 [0.72, 1.46]
        + position (three groups) and height                                                       0.89 [0.51, 1.28]
        + every position pairing, height, partner share                                            0.69 [0.35, 1.04]
        + all removed positions, height, partner share                                             0.49 [0.15, 0.84]
        Planned test + player × team × season effects                                              1.38 [0.95, 1.81]
        Same + position pairings, height, partner share                                            0.93 [0.47, 1.39]
        Same + all removed positions, height, partner share                                        0.75 [0.30, 1.19]
        Cases with one removed player (353)                                                        0.98 [0.29, 1.67]
      One listed position removed (455 cases)
        Similarity only                                                                            1.05 [0.40, 1.70]
        + every position pairing, height, partner share                                           0.20 [−0.64, 1.04]
      Games without and with the absent player
        Pairs, absent-player effects (2,653 pairs)                                                 1.54 [1.15, 1.93]
        + teammate effects (2,168 pairs)                                                           1.23 [0.73, 1.73]
        Both effects, similarity before absence (1,278)                                            1.01 [0.36, 1.66]
        Same + position pairings and height gap                                                 −0.02 [−0.72, 0.67]
        Same, absent-player effects only                                                          0.60 [−0.05, 1.25]
      Earlier seasons, 2021–22 and 2022–23
        Allocation test                                                                            1.20 [0.67, 1.72]
        + position (three groups) and height                                                       0.91 [0.40, 1.41]
        + every position pairing, height, partner share                                            0.92 [0.43, 1.41]
        Allocation test + player × team × season effects                                           1.77 [1.27, 2.28]
        Pairs, absent-player effects (1,661 pairs)                                                 1.41 [0.82, 2.01]
        Pairs, before absence + position pairings (914)                                           0.85 [−0.34, 2.04]
      Placebo: no core player absent
        Each core treated as absent (3,522 team-games)                                          −0.16 [−0.33, 0.02]
        No supported player ruled Out (846 team-games)                                          −0.07 [−0.27, 0.13]

                                                             −1        0 0.5 1 1.5 2
                                                     Minutes per unit of role similarity (95% interval)

Figure 2: The similarity coefficient across specifications and samples: minutes per unit of role similarity,
with 95% intervals (coefficient ± 2.045 team-clustered standard errors; for the pair comparisons with fewer
than 30 teams, the t(G − 1) quantile for their number of teams G). Filled circle: the planned allocation test;
filled squares: tests whose pass rule was written before they were run; open circles: exploratory checks. Pair
rows: outcome a difference of mean minutes, similarity to that player alone (Section 5.2); other rows: extra
minutes, similarity to the whole removed set. Rows use different samples; Table 3 provides same-sample
comparisons. Sources: Sections 5 and 7 and Supplementary Tables S6, S18, S23, S48 to S50, S56, S57, S59
and S63.


26 (a season whose outcomes we had seen, though not used in fitting) had mean absolute errors of 7.175

minutes with similarity, 7.166 with listed position (three groups) and height, and 7.201 for allocation in

proportion to reference minutes, with no difference distinguishable from zero, and adding similarity to the

model with the five listed positions changes the error by −0.004 minutes (95% interval −0.017 to 0.011;

Supplementary Table S51); an inverse-optimisation model did not meet the pass rule set for it in advance

(7.178; Supplementary Tables S14 and S71). None can place a retained player below his reference minutes,

although 29.5% played less (Section 3.4). The comparison is thus limited to models of this kind, fitted and


                                                           19
evaluated on the hybrid sample with rosters that use later records (Section 2.2): it shows no advantage for

similarity, not that similarity has no predictive value.



6      Results: role coverage

6.1     Team role output: coverage adds nothing detectable beyond the role share

Single-dimension coverage varies little: it equals its cap of 1 in 77% of case-roles, and at the estimated

slope moving from its 10th percentile (0.85) to 1 corresponds to role output higher by 0.8% of the ten-game

baseline, against an outcome standard deviation of 18%. Whatever its sign, the association is therefore

small. The role-output test does not meet its threshold (Table 2): a one-unit increase in coverage goes with

a team role total 5.4% higher relative to its baseline (SE 2.9%; p = 0.070; wild bootstrap p = 0.071). It is

significant in 2 of the 10 measurement definitions, short of the 8 of 10 that the plan’s robustness rule requires

(Supplementary Table S71); of its three planned sensitivity samples one passes (core players ruled Out for

any reason: 0.058, p = 0.045; Supplementary Table S8).

Table 4: Exploratory versions of the role-output test, main seasons, six-hour cutoff: coefficient of ck (p).
The planned test and its five-season and earlier-season versions are in Table 2; the benchmark is defined in
the text and in Supplementary Section S1. Supplementary Tables S30, S34 and S43.

                   Specification                                          Coefficient of ck (p)

                   With the benchmark (95% interval −0.126 to 0.021)      −0.053 (0.15)
                   With the absent players’ share of the role instead     −0.048 (0.15)
                   With the benchmark capped at each player’s headroom    −0.044 (0.24)
                   Healthy baseline, with the benchmark                   −0.074 (0.071)
                   First game of each episode, with the benchmark         −0.042 (0.41)
                   Placebo (all core players took part), planned inputs   0.033 (0.021)



      When the absent players carried much of a role, ck is low, but their teammates would also supply less

of that role if the freed minutes were simply shared out. As a benchmark we computed, for each case and

role, the proportional change in role output if the removed minutes went to the retained players in proportion

to their reference minutes, each at his historical rate. Given the removed minute share, the benchmark is

almost a linear function of the absent players’ share of the role (partial correlation −0.98), so we read it as

that share. It predicts role output (0.21 per unit, p < 0.0001), and with it as a control the coefficient of ck

                                                         20
is −0.053 (p = 0.15); the same holds with the role share itself, with the benchmark capped at each player’s

headroom, and over five seasons (Tables 2 and 4; Supplementary Table S30). The ten-game baseline is itself

partly adapted: in 98.5% of cases it includes a game without a removed player (Supplementary Table S40),

which pulls role output toward zero in continuing absences; with a healthy baseline the coefficient with the

benchmark is −0.074 (p = 0.071), and in the first game of each episode −0.042 (Supplementary Tables S30

and S34). A placebo in the 3,522 team-games in which all three core players took part gives a same-signed

slope with the planned inputs (0.033, p = 0.021), and the difference between real cases and placebo is not

significantly positive in any version we compared; in one it is significantly negative (Supplementary Tables

S43 and S44).


6.2     The final margin: no consistent association

Absences coincide with lower margins: team-games with a core player ruled Out for a medical reason have

a margin 2.26 points lower than the same team’s other games in that season. The margin test asks whether

coverage adds to the value of the players who are missing.

      In the primary sample, conditional on the removed minute share, lost value, strength, home and rest, the

coverage coefficient is −0.10 points per 0.1 of coverage with a 95% interval of [−0.68, +0.49]: the interval

still includes a negative association of half a point per 0.1, and the 90% interval does not fall within the

equivalence bounds of ±0.5 (see below). Per unit of coverage this is −0.99 points (SE 2.86; p = 0.73; wild

bootstrap p = 0.74). In the hybrid sample it is −0.01 [−0.53, +0.51]. No sample, baseline or measurement

variant of the planned model yields p < 0.05 for coverage (Supplementary Figure S1); of the exploratory

versions we tried, a few do, none of them planned: a five-season hybrid version with a lineup-based value

measure (p = 0.043; wild bootstrap 0.055), the 37 cases whose removed players had played each of the

team’s last ten games (p = 0.039) and the 2021–22 slope of a model with season-specific slopes (p = 0.045;

Supplementary Tables S40 and S33). The partial relationship over all five seasons has no clear gradient

(Supplementary Figure S2).

      How precise is this null? At its standard error, the test had 80% power only for effects of at least 0.83

points per 0.1 of coverage, about 1.4 points across the interquartile range of coverage (0.17). Two one-sided

tests (Schuirmann, 1987; Lakens, 2017) against ±0.5 points per 0.1, a bound set after the main estimate was

known, do not establish equivalence in the primary sample (90% interval [−0.58, +0.39] per 0.1); over five

seasons they do so in the planned specification and in some variants (the hybrid sample; RAPM beside the

                                                       21
box-score value), but not with the opponent’s absence value controlled (Section 7; Supplementary Tables

S21 and S26).

      Further checks leave this unchanged: other controls, fixed effects and measures of absence value (p =

0.06 to 0.93 in the six-hour models of Supplementary Tables S12, S20, S26, S35 and S42), and other

treatments of teammates listed Questionable or Doubtful (exploratory; Supplementary Table S62). A follow-

up model with a pass rule written in advance passed (in the hybrid sample the value the retained rotation

could supply predicts the margin, p = 0.007), but that measure correlates 0.98 with removed minutes and

adds nothing against the closing spread in 2025–26 (Supplementary Tables S15 and S16).


6.3     Coverage when teammates’ minutes may be cut

Coverage keeps every retained player at or above his reference minutes (Section 3.4), although 29.5% of

retained players played fewer. In an exploratory extension (Section 4; Supplementary Section S6 and Tables

S69 and S70) we let retained players’ minutes fall below their reference minutes within a budget of total

cuts and ask what share of the absent players’ minutes and roles can then be restored at once. Given the

retained players, their capacities and fixed role rates, 39.2% of cases are fully covered without cuts, 23.4%

once cuts are allowed (median smallest total cut 9.3 minutes) and 37.4% not even with unrestricted cuts;

allowing cuts closes 43% of the summed shortfall, 27% to 60% under other cut floors, capacity rules and rate

shrinkage. Whether the required cut tracks actual rotations is not established: of two planned comparisons

one is positive and the other imprecise and based on a baseline that is not comparable in structure, so the

criterion fixed in advance (both positive and the baseline comparison’s interval excluding zero) is not met.



7      The same tests in two earlier seasons

We built the seasons 2021–22 and 2022–23, in which coverage and role similarity had never been related to

any outcome, with the same code and ran the planned tests (Table 2) under a rule written down in advance:

a test replicates if its coefficient has the original sign and p < 0.05. This is a second sample from the same

pipeline and the same authors, not an independent replication.

      The allocation test replicates with a similar point estimate in the two seasons pooled, and most of it

again survives position (three groups) and height; it is significant in each of the two seasons alone (2022–

23: 1.06, p = 0.001; Supplementary Table S38). The exploratory checks of Section 5 agree (1.41 and 1.62


                                                     22
in the without-and-with comparison, 1.77 with player-by-team-by-season effects), and the position results

are mixed as in the main seasons: 0.92 (0.43 to 1.41) with every pairing on cases, 0.85 (−0.34 to 2.04) in

the pair comparison (Section 5.3; Supplementary Tables S48 to S50, S56, S57 and S63).

    In the earlier seasons the role-output test meets its planned threshold, also without the 177 six-hour cases

that involve a COVID-19 protocol absence (0.089, p = 0.009; the allocation test 1.13; Supplementary Table

S33), but with the benchmark the estimate is 0.068 and its interval includes zero. The margin test remains

null: over five seasons the planned specification meets the ±0.5 bound of Section 6.2 (Table 2), and with

the opponent’s absence value controlled it does not (+0.18; −0.24 to +0.59).



8    Robustness and data quality

Measurement definitions. We reran every step for ten alternative definitions on the hybrid sample (Sup-

plementary Table S10 and Figure S1). The similarity coefficient ranges from 0.81 to 1.12 and is significant

in all ten; the coefficient of ck ranges from 0.028 to 0.064 and is significant in two. The three sensitivity

analyses fixed with the plan (without previous-day reports, which removes no case; core players ruled Out

for any reason; without full coverage) leave the allocation test unchanged or larger (1.09 to 1.35) and give

role output 0.049 to 0.058 (p = 0.045 to 0.093; Supplementary Tables S5 and S8).

    Inference and seasons. Wild bootstrap p-values are within 0.03 of the clustered t-test p-values for every

planned test (Supplementary Table S9), and clustering by team and game (Cameron et al., 2011) changes

no verdict, while clustering by game alone gives role output p = 0.046 (Supplementary Table S32). The

allocation test is significant in each main season, with a falling coefficient (1.56, 1.13 and 0.80), but the

linear trend is not (−0.36 per season, p = 0.060), nor over five seasons (−0.11, p = 0.31; Supplementary

Table S38).

    Data corrections. After the planned tests had been run and the 2026–27 test registered, an audit of

the code and a later review found three defects in the rosters of that build: ended contracts, and unrenewed

ten-day contracts, were not ended (a player who signed nowhere else kept reference minutes on his old team

for about 20 games of the next season; 380 of that build’s 2,440 cases), and transactions were dated at noon

UTC, before most cutoffs. We specified the corrections (Section 2.2), reran every analysis and, with both

sets of results known, made the corrected data the paper’s data, although this took the role-output test below

its threshold (p = 0.038 on the earlier build); every result here and in the supplement uses them unless a


                                                      23
supplementary table compares data versions. Seven other significance judgements differ between the two

builds, and on the final data, unlike on the earlier build, clustering by game alone changes the verdict of

the role-output test (Supplementary Table S72). In 51% of cases the selected report’s header time, a lower

bound on publication, equals the cutoff; with reports strictly before it the tests give 1.01, 0.052 (p = 0.085)

and −0.08 per 0.1.



9      Discussion and conclusions

9.1     What the evidence shows

Minutes tilt modestly toward teammates whose statistical role resembles that of the absent players, in the

main and the earlier seasons; the placebo gradient is slightly negative.

      What the evidence does not settle is whether role similarity carries information beyond listed position.

Over all cases 45% to 72% of the coefficient remains after position, height-gap and partner-share controls

and is distinguishable from zero (Section 5.3). In the one-position cases and the pair model with both

players’ effects, no additional association is detected in the main or the earlier seasons (Sections 5.3 and 7;

Supplementary Table S56), but the intervals are wide, all 1,788 pairs with absent-player effects only give

0.72 (0.19 to 1.25), and these designs differ from the case model in more than the control. The evidence

supports a small, repeatable gradient, not that role describes the allocation better than listed position.

      Coverage adds nothing detectable to team role output beyond the absent players’ share of each role, and

nothing consistent to the margin (Section 6). The measure is generous (39.2% of cases at full coverage) and

correlated with the removed minute share and absence value; other dimensions or lineups may matter. Split-

ting similarity by role and letting coverage cut minutes (Sections 5.3 and 6.3) do not change these readings:

the role components do not differ clearly once the teammate’s own rates are controlled; the rebound com-

ponent stays positive with the position controls of Table 3, row 3, but comes from frontcourt absences, so

these exploratory analyses do not settle whether role adds to listed position; and how much of the coverage

shortfall cuts close depends on capacity and cut-floor assumptions.


9.2     Limitations

      • Not causal. Absences are not random: core players listed Questionable or Doubtful sat somewhat

        more often when the proportional benchmark said more of their role could be absorbed (p = 0.04;

                                                       24
        Supplementary Table S42), and neither player nor teammate effects remove a change of place in the

        rotation that coincides with who is absent (Sections 5.2 and 5.3). Profiles may already reflect the

        absence (Section 5.1).

      • Seen outcomes. Every result comes from seasons whose outcomes we had seen. The registered 2026–

        27 allocation test (amended before its first game to make the corrected code of Section 8 primary) has,

        at a true effect of 0.78 minutes per unit (its smallest effect of interest), power 0.48, 0.81 or 0.99 if that

        season is as precise as 2023–24, 2024–25 or 2025–26 (SE 0.40, 0.27, 0.18), and the effects it detects

        with 80% power at those precisions are 1.15, 0.77 and 0.52 (Supplementary Table S43); its position

        rule, three groups and height, cannot settle whether similarity adds to listed position.

      • Sample. Only supported players (Section 3.1) enter, so long-term absentees, newcomers and players

        outside the rotation are partly missing.

      • Measurement. Three box-score dimensions miss usage, defensive assignments, ball handling and

        spacing. A report’s header time only bounds when it became public (Section 8). Coverage, also with

        cuts, holds role rates fixed.

      • Post-hoc checks. Only three tests were planned; most checks were specified after related results had

        been seen. With so many models, isolated p-values near 0.05 should be read accordingly (Gelman

        and Loken, 2014).


9.3     What it means

The paper makes two contributions. First, in pregame absences it measures a small gradient of minutes

along a continuous role-similarity measure, which recurs in a second sample, and asks whether it adds to

listed position and past substitution. Same-position gains after absences are known (Nishihata, 2026); new

here are the pregame-report timing and the continuous role measure, which extend the question of how an

absence shifts co-workers’ working time (Hoey et al., 2023). Whether role adds to listed position depends on

how position is controlled and on the design (Section 5.3): an analysis that stopped at coarse controls would

claim more than these data support. Second, Glazer et al. (2025) note that their NFL injury-burden measure

treats every backup as replacement level and leave team-specific replacement level to future work; coverage

is one such attempt, built from box scores, and in the models we tested it shows no stable incremental

association, an answer for this measure, not for the question.

                                                         25
Data and code availability

Code, tests, analysis plans and a reproduction guide will be made public upon publication. The sources’

terms of use restrict redistribution, so we will release derived tables, with a script that reproduces Tables

2 and 3 from them, the main seasons’ game identifiers and the SHA-256 hash of every injury report. The

2026–27 replication is registered at https://osf.io/kzfyu (under embargo).



Declarations

Funding. This research received no specific grant from any funding agency in the public, commercial or

not-for-profit sectors.

    Competing interests. The authors declare no competing interests.

    Author contributions (CRediT). Tianyu Guan: Conceptualization; Methodology; Software; Valida-

tion; Formal analysis; Writing – original draft; Writing – review & editing; Project administration. Yang

Zhou: Conceptualization; Methodology; Software; Validation; Data curation; Writing – review & editing.

Both authors read and approved the final manuscript.

    Supplementary Material. The Supplementary Material follows the references.



References

Abramson, J. (2021).        NBA injury report sports analytics project (part 1).            Blog post, 25

  July 2021, https://jeremyabramson.github.io/blog/sports%20analytics/nba/

  python/research/projects/injuries/2021/07/25/nba-injuries.html.

Alagappan, M. (2012). From 5 to 13: Redefining the positions in basketball. In MIT Sloan Sports Analytics

  Conference.

Arcidiacono, P., Kinsler, J., and Price, J. (2017). Productivity spillovers in team production: Evidence from

  professional basketball. Journal of Labor Economics, 35(1):191–225.

Bianchi, F., Facchinetti, T., and Zuccolotto, P. (2017). Role revolution: towards a new meaning of positions

  in basketball. Electronic Journal of Applied Statistical Analysis, 10(3):712–734.

Brenøe, A. A., Canaan, S., Harmon, N. A., and Royer, H. N. (2024). Is parental leave costly for firms and

  coworkers? Journal of Labor Economics, 42(4):1135–1174.


                                                     26
Bruce, S. (2016). A scalable framework for NBA player and team comparisons using player tracking data.

  Journal of Sports Analytics, 2(2):107–119.

Camerer, C. F. and Weber, R. A. (1999). The econometrics and behavioral economics of escalation of

  commitment: a re-examination of Staw and Hoang’s NBA data. Journal of Economic Behavior & Orga-

  nization, 39(1):59–82.

Cameron, A. C., Gelbach, J. B., and Miller, D. L. (2008). Bootstrap-based improvements for inference with

  clustered errors. The Review of Economics and Statistics, 90(3):414–427.

Cameron, A. C., Gelbach, J. B., and Miller, D. L. (2011). Robust inference with multiway clustering.

  Journal of Business & Economic Statistics, 29(2):238–249.

Cameron, A. C. and Miller, D. L. (2015). A practitioner’s guide to cluster-robust inference. Journal of

  Human Resources, 50(2):317–372.

Cardazzi, A., Humphreys, B. R., and Reddig, K. (2024). Sports team success and managerial decisions:

  the role of playing-time concentration. International Journal of Sports Marketing and Sponsorship,

  25(2):266–287.

Chan, T. C. Y., Cho, J. A., and Novati, D. C. (2012). Quantifying the contribution of NHL player types to

  team performance. Interfaces, 42(2):131–145.

Chan, T. C. Y., Mahmood, R., and Zhu, I. Y. (2025). Inverse optimization: Theory and applications. Oper-

  ations Research, 73(2):1046–1074.

Chen, J. S. and Garg, P. (2018). Dancing with the stars: Benefits of a star employee’s temporary absence for

  organizational performance. Strategic Management Journal, 39(5):1239–1267.

Correia, S. (2015). Singletons, cluster-robust standard errors and fixed effects: A bad mix. Technical note,

  Duke University.

Dare, W. H., Dennis, S. A., and Paul, R. J. (2015). Player absence and betting lines in the NBA. Finance

  Research Letters, 13:130–136.

Durmuş, T., Sansone, P., and Zhang, S. (2026). From fixed positions to role diversity: positional evolution in

  the National Basketball Association. International Journal of Performance Analysis in Sport. Published

  online 16 July 2026.

Fischer, K. and Schmal, W. B. (2025). Pricing in response to new information: The case of betting markets.

  Economic Inquiry, 63(1):236–264.

Gelman, A. and Loken, E. (2014). The statistical crisis in science. American Scientist, 102(6):460–465.

                                                      27
Glazer, A., Binney, Z., and Seth, T. (2025). Weighted approaches to assessing injury burden in team sports.

  Journal of Sports Analytics, 11:22150218241304941.

Goldman, M. and Rao, J. M. (2011). Allocative and dynamic efficiency in NBA decision making. In MIT

  Sloan Sports Analytics Conference, Boston, MA.

Guan, T. and Zhou, Y. (2026). Who was really out? A point-in-time NBA availability benchmark, and what

  it says about hindsight. Submitted.

Guo, T., Ley, C., Cui, Y., Shen, Y., Zhang, C., and Mi, J. (2025). Quantifying player versatility through

  lineup-based playing styles in elite basketball. International Journal of Sports Science & Coaching,

  20(2):688–697.

Hoey, S. (2026). One’s pain is another’s gain: Early career exposure and later labor market outcomes. The

  Journal of Law, Economics, and Organization. Advance article ewag008.

Hoey, S., Peeters, T., and van Ours, J. C. (2023). The impact of absent co-workers on productivity in teams.

  Labour Economics, 83:102400.

Jäger, S. and Heining, J. (2022). How substitutable are workers? Evidence from worker deaths. Working

  Paper 30629, National Bureau of Economic Research.

Jedelhauser, F., Flepp, R., and Franck, E. (2023). Overshadowed by popularity: The value of second-tier

  stars in European football. Journal of Sports Economics, 24(8):1026–1054.

Jin, J., Yang, D., Liu, Y., and He, L. (2026). Does playing time impact player performance? A COVID-19

  natural experiment. International Journal of Sport Finance, 21(2):87–100.

Kocsoy, A. (2024). Captains vs. All-Stars: Who makes better leaders? PLOS ONE, 19(11):e0309374.

Krishna, K., Lychagin, S., and McLean, L. S. (2026). Injury, workload, and the strategic response of coaches

  in the NBA. Working Paper 35803, National Bureau of Economic Research.

Kuehn, J. (2017). Accounting for complementary skill sets: Evaluating individual marginal value to a team

  in the National Basketball Association. Economic Inquiry, 55(3):1556–1578.

Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. Social

  Psychological and Personality Science, 8(4):355–362.

Leeds, D. M., Leeds, M. A., and Motomura, A. (2015). Are sunk costs irrelevant? Evidence from playing

  time in the National Basketball Association. Economic Inquiry, 53(2):1305–1316.

MacKinnon, J. G., Nielsen, M. Ø., and Webb, M. D. (2023). Cluster-robust inference: A guide to empirical

  practice. Journal of Econometrics, 232(2):272–299.

                                                     28
Maymin, A. Z., Maymin, P. Z., and Shen, E. (2013). NBA chemistry: Positive and negative synergies in

  basketball. International Journal of Computer Science in Sport, 12(2):4–23.

Muniz, M. and Flamand, T. (2022). A weighted network clustering approach in the NBA. Journal of Sports

  Analytics, 8(4):251–275.

Muniz, M. and Flamand, T. (2023). Sports analytics for balanced team-building decisions. Journal of the

  Operational Research Society, 74(8):1892–1909.

Nalbantis, G., Manger, C., Pawlowski, T., and Yang, P. (2026). Exploring the impact of specialist and

  generalist stars on organizational performance. PLOS ONE, 21(5):e0349682.

National Basketball Association (2025). NBA injury report: 2025–26 season. https://official.

  nba.com/nba-injury-report-2025-26-season/. Accessed 21 September 2026.

Nishihata, M. (2026). The value of a chance: Task concentration and talent discovery in team production.

  Preprint, arXiv:2511.07218v2 (first posted November 2025).

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. (2018). The preregistration revolution.

  Proceedings of the National Academy of Sciences, 115(11):2600–2606.

Podlog, L., Buhler, C. F., Pollack, H., Hopkins, P. N., and Burgess, P. R. (2015). Time trends for injuries

  and illness, and their relation to performance in the National Basketball Association. Journal of Science

  and Medicine in Sport, 18(3):278–282.

Reilly, P., Solow, J. L., and von Allmen, P. (2023). When the stars are out: The impact of missed games on

  NBA television audiences. Journal of Sports Economics, 24(7):877–902.

Rodriguez-Idiazabal, L., Casals, M., Moreno-Doutres, D., Barrio, I., and Sanz, P. (2026). Data-driven

  role identification and role-specific performance evaluation in the NBA. International Journal of Sports

  Science & Coaching. Published online 10 August 2026.

Sandholtz, N., Mortensen, J., and Bornn, L. (2020). Measuring spatial allocative efficiency in basketball.

  Journal of Quantitative Analysis in Sports, 16(4):271–289.

Sandholtz, N., Wu, L., Puterman, M., and Chan, T. C. Y. (2024). Learning risk preferences in Markov

  decision processes: An application to the fourth down decision in the National Football League. Annals

  of Applied Statistics, 18(4):3205–3228.

Sauer, R. D. (2002). Player injuries and price responses in the point spread wagering market. In Vaughan-

  Williams, L., editor, The Economics of Gambling, pages 145–164.

Schuirmann, D. J. (1987). A comparison of the two one-sided tests procedure and the power approach for

                                                    29
  assessing the equivalence of average bioavailability. Journal of Pharmacokinetics and Biopharmaceutics,

  15(6):657–680.

Skinner, B. and Goldman, M. (2017). Optimal strategy in basketball. In Albert, J., Glickman, M. E., Swartz,

  T. B., and Koning, R. H., editors, Handbook of Statistical Methods and Analyses in Sports, chapter 11.

  Chapman & Hall/CRC, Boca Raton, FL.

South, C. (2025). A basketball paradox: exploring NBA team defensive efficiency in a positionless game.

  Journal of Quantitative Analysis in Sports, 21(4):345–359.

Staw, B. M. and Hoang, H. (1995). Sunk costs in the NBA: Why draft order affects playing time and survival

  in professional basketball. Administrative Science Quarterly, 40(3):474–494.

Stuart, H. C. (2017). Structural disruption, relational experimentation, and performance in professional

  hockey teams: A network perspective on member change. Organization Science, 28(2):283–300.

Webb, M. D. (2023). Reworking wild bootstrap-based inference for clustered errors. Canadian Journal of

  Economics, 56(3):839–858.

Wegelin, P., Orlowski, J., and Dietl, H. M. (2022). The importance of high performing team members in

  complex team work: Results from quasi-experiments in professional team sports. Economic Inquiry,

  60(3):1296–1310.

Zhou, Y. and Guan, T. (2026). From metrics to decisions in NBA analytics: A critical integrative review and

  decision-readiness framework. Preprint, arXiv:2609.27245.




                                                    30
                     Supplementary Material for
     “Who Fills the Gap? Role Similarity and Teammates’ Minutes
                  When NBA Players Are Ruled Out”
                                         Tianyu Guan        Yang Zhou


This supplement gives what the paper has no room for: the definition of every variable (Section S1), the
full results of the planned tests and their sensitivity analyses (Section S2), the tables of the later, exploratory
analyses that the paper cites (Section S3), the planned tests with their verdicts, the data corrections and
the deviations that bear on the planned tests (Section S4), how to reproduce the results (Section S5), and
the full account of two analyses that the paper reports in brief (Section S6). Every table and figure uses
the final data, with corrections R, T, D and M (Section S4), unless its caption names another build. The
numbers in the tables are generated by the table-building script from the result files of the repository; the list
of planned tests (Table S71) is typed. Some terms differ from the paper. The allocation, margin and role-
output tests of the paper are tests (1), (2) and (3) here (the paper presents role output before the margin); the
two earlier seasons are the replication seasons; the supported players of the paper are also called reference
players, and the retained players remaining players; the hand-reconstructed subset of 184 team-games is
the gold standard or hand-audited subset; a plan, a test or its code is frozen once it was committed and no
longer changed, and the frozen rows of a test are the rows of its planned sample; an episode is a run of
consecutive games with the same core players ruled Out; and a player’s standing is his place in the rotation.
A separate check is a check made without having written the code or the text it checked; such checks are not
independent verification. The history of the analysis (each plan with its commit time, every addendum and
every deviation, and the reproduction checks of earlier builds) is kept in a separate analysis record released
with the code.
The tables cited by each section of the paper are: Section 2, Tables S3, S43, S45, S47, S53, S72; Section 3,
Tables S46, S55, S64; Section 4, Tables S40, S58, S71; Section 5, Tables S5, S6, S7, S8, S14, S18, S21,
S23, S30, S35, S40, S45, S48, S49, S50, S51, S52, S54, S56, S57, S58, S59, S60, S61, S63, S64, S65, S66,
S67, S68, S71; Section 6, Tables S8, S12, S15, S16, S20, S21, S26, S30, S33, S34, S35, S40, S42, S43,
S44, S62, S69, S70, S71; Section 7, Tables S33, S38, S48, S49, S50, S56, S57, S63; Section 8, Tables S5,
S8, S9, S10, S32, S38, S72; Section 9, Tables S42, S43, S56.


S1     Variable definitions
Cutoff
     Scheduled tip-off minus six hours (primary) or minus 90 minutes (hybrid and 90-minute samples).
Report at cutoff
     The last official injury report whose printed header time is at or before the cutoff and in which the
     team’s block was submitted. Team-games with no such report are left out of case identification and,
     as opponents, have a missing absence value. The header time only bounds publication from below,
     and in 51% of primary cases it equals the cutoff; addenda P44 and P47 use only reports strictly before
     the cutoff as a sensitivity analysis (Table S72).


                                                        1
Roster at cutoff
     Players whose latest event before the cutoff (box-score listing, signing, trade or claim) ties them to the
     team and who have not since been waived; plus players on the team’s report unless known to belong
     to another team. The player-movement log has no contract expirations, and the earlier build dated
     transactions at 12:00 UTC; the final data correct this (Table S72). Transactions count from 23:59 US
     Eastern time on their date (correction T). A player whose last tie to a team is from an earlier season
     stays on it only if his first record of the new season (box-score row, report listing, signing, trade or
     waiver) is a box-score row or a report listing for that team, or a waiver (R); a signing, even a re-signing
     with the same team after the cutoff, does not continue the earlier tie. A ten-day contract ends on the
     later of the signing date plus ten days and the date of the team’s third game of the same season after
     the signing; unless the player has another transaction or plays for another team by the day after that
     date, he leaves the team at 23:59 US Eastern time on it and stays off its roster until his next record (D;
     318 contracts in 2019–20 to 2025–26). R and D use records after the cutoff (a later transaction, listing
     or appearance), so the rosters are a retrospective reconstruction, not a rule a forecaster could apply in
     real time; for 2026–27 a dated amendment to the registration, filed and approved on 19 October 2026
     (17:26 UTC), before the season’s first game (20 October 2026), makes the corrected code (R, T, D
     and the position correction M) the primary analysis and reports the registered code beside it (addenda
     P46 to P48).
Listed position and height
      A player’s listed position (PG, SG, SF, PF or C; grouped as guard, forward and centre) and height in a
      season, from the Basketball-Reference team-season roster rows (correction M, addendum P48; source
      file in Section S5). Each roster row is matched to an ESPN player who appears in the box scores of
      the same team and season, by the full name key, else the key without a suffix (Jr., II, III), else last
      name and first initial, and only where the key identifies exactly one roster row and one ESPN player
      in that team-season; a Basketball-Reference player matched to more than one ESPN identifier, or the
      reverse, is dropped (2 pairs). A player who played for several teams in a season takes the row of the
      team for which he played the most minutes. Player-seasons left unmatched keep the value of the bio
      pipeline’s player-season table, which supplied every position before correction M and had dropped
      players whose names it could not resolve (among them names with Jr., II or III); where both sources
      give a position for a player-season (2,616) they agree. A player without a value in the season takes
      that of an adjacent season. Every removed player of the primary cases has a listed position; in the
      earlier seasons one player, absent from the roster rows, has none (8 cases; Table S65).
History
      A player’s last 20 regular-season games with positive minutes ending before the cutoff, within 365
      days, for any team. The NBA Cup finals, which ESPN lists with the regular season but which count
      in no standings, are included.
Supported
     At least 5 history games, 100 minutes, and no more than 20 of the team’s scheduled games since the
     last appearance.
Capacity u j
     min(40, 90th percentile of history minutes).
Reference minutes b j
     240 minutes allocated to supported players in proportion to mean minutes, capped at capacity, excess
     redistributed.



                                                       2
Reference core
     The three players with the largest reference minutes.
Case
       A team-game in which at least one core player is ruled Out for a medical reason (including injury
       management) at the cutoff.
Reason classes
     The reason printed on the report is classed as G League, suspension, trade pending, ineligible, personal
     (also a bare “not with team”), rest (a reason that begins with “Rest” and does not mention injury) or
     unknown (empty); every other non-empty reason is medical. This residual rule is needed because
     reasons are often split across lines of the PDF, leaving fragments such as “Strain” or “Surgery”; it
     also makes medical a reason such as “Return to Competition Reconditioning”, which names no injury
     (Table S3). “Coach’s Decision” falls under this rule and is medical in every table (25 Out rows;
     correction C, Section S4, would separate it and a bare “not with team”; it changes no case, and its
     effect on the tables is listed there).
Role rates r jk
      Three-point attempts, assists and total rebounds per minute, shrunk toward the pooled rate of the roster
      teammates with history (leaving the player out) with 100 pseudo-minutes.
Role similarity
      Cosine similarity between a player’s standardised role-rate vector and the reference-minute-weighted
      mean of the removed players’ standardised vectors (Equation 2 of the paper; Table S55 works through
      one case). Each role rate is standardised with the mean and standard deviation over the reference
      players of every team-game of the analysed seasons in which a core player is ruled Out for any reason
      (a wider set than the cases, which need a medical reason; removed players included, one row per
      player and team-game); the removed players’ vectors are standardised first and then averaged. The
      forecasts and the models built on them (P4.1 to P4.3 with their sensitivity analyses, P34 part Bh and
      P43; Tables S14, S15, S16 and S51) use means and standard deviations from the two training seasons
      (2023–24 and 2024–25) only (addenda P46 and P47). Every other analysis standardises over the
      seasons of the sample it analyses: the three main seasons (2023–24 to 2025–26) for the primary and
      hybrid samples, the two earlier seasons (2021–22 and 2022–23) for the replication seasons, and all
      five seasons for the five-season samples (so the five-season coefficients for 2023–24 to 2025–26 differ
      slightly from the three-season ones, Table S38). Because similarity is a cosine of centred and scaled
      rates, a different set of means and standard deviations changes the profiles’ directions and not only
      the scale of the coefficient. No vector in the primary sample has a zero norm; the smallest norm of a
      removed set’s mean vector is 0.06 (addendum P32).
Headroom h j
     max(u j − b j , 0).
Coverage
     Largest θ ∈ [0, 1] such that one set of extra minutes within headroom, totalling at most the removed
     minutes L, restores the share θ of L and of every role demand (linear program, Section 3.4 of the
     paper).
Single-dimension coverage ck
      min(1, Sk /Dk ), where Sk is the most of role k the remaining players can supply with at most L extra
      minutes within their headroom (a fractional knapsack, solved exactly by giving the extra minutes to
      the players with the highest rate of the role first).


                                                      3
Lost value
      ∑a∈R ba ea , with ea the pre-cutoff efficiency per minute (PTS + REB + AST + STL + BLK − TOV −
      missed FG − missed FT).
Strength difference
     Difference between the two teams’ mean margins over their previous ten games.
Rest difference
      Difference in days since each team’s previous game, capped at three.
Role output
      Team’s in-game total of a role divided by its mean over the previous ten games, minus one.
Absence value
     Lost value computed for every team-game with a report block (zero when no reference player is Out);
     used in Section 6.2 of the paper and, for the opponent, as a control.
Benchmark
     benchk = [(Bk − Dk )/Bk ] · 240/(240 − L) − 1, with Bk = ∑ j b j r jk over the full reference rotation: the
     proportional change in role output if the removed minutes went to the remaining reference players in
     proportion to their reference minutes, each at his historical rate.
Role pressure
      Dk divided by the remaining reference players’ expected output of role k at reference minutes,
      ∑ j∈R
         / b j r jk ; the rate response (Table S4; the paper mentions it only in words) is estimated on
      remaining players who played, one row per player and role (71,289 = 3 × 23,763).
Rate change
      For a retained reference player who played, his in-game count of role k divided by his actual minutes,
      minus his historical rate r jk (per minute); regressed on role pressure with role dummies and team-
      clustered errors, pooled over cases (the rate response of Table S4).
Measurement definitions
    Capacity quantile 0.75 or 1.0 (instead of 0.9); unshrunk rates (no pseudo-minutes); current-team
    history only; low history threshold (supported with 1 game and 30 minutes instead of 5 and 100);
    recency 40 (no more than 40 instead of 20 team games since the last appearance); 24-hour latency
    (history games must have ended 24 hours before the cutoff); six coverage dimensions (field-goal
    attempts, three-point attempts, assists, offensive rebounds, defensive rebounds and blocks, used for
    coverage only; role similarity keeps the three primary roles); last 10 or last 40 games of history instead
    of 20.
Managed absence
    Core player listed Out for a medical reason whose text mentions injury management, maintenance,
    reconditioning or rest. A reason that begins with “Rest” and does not mention injury is classed as rest
    rather than medical and never makes a case; where a managed absence mentions rest, the reason also
    names an injury.
Removed set R
    All reference players ruled Out at the cutoff, for any reason (a case needs at least one core player ruled
    Out for a medical reason). Similarity, demands Dk and the removed minutes L refer to the whole set,
    not to one absent player.
Suppliers
     The supported (reference) players not ruled Out. The same set supplies extra minutes in the coverage

                                                       4
       linear program, in Sk and ck , in the benchmark and in the capped benchmark; unsupported roster
       players never supply. The shrinkage prior of the role rates uses every roster player with history.
Extra minutes ∆mini j
     Actual minutes minus reference minutes b j . A retained reference player who did not play has actual
     minutes 0, so ∆mini j = −b j (checked by a unit test, addendum P30).
Position and height with several absences
      The removed set’s position is the position group (guard, forward, centre) with the largest total ref-
      erence minutes among the removed players, and its height is their reference-minute-weighted mean
      height; same position = 1 if the retained player’s group equals it, and height gap = |H j − H̄R |. Ad-
      dendum P34 also uses the five listed positions (PG, SG, SF, PF, C): same position with five positions,
      the position distance (absolute difference between the player’s position, numbered 0 to 4, and the
      reference-minute-weighted mean of the removed set) and indicators for every pairing of the player’s
      position with the removed set’s. Positions and heights are season-level values (see Listed position and
      height).
Substitution-partner share
     For each removed player a and retained player j, the share of possessions with a on the bench in
     which j was on court, over those of the team’s last 20 games before the cutoff in which a played, from
     the stint data; averaged over removed players with weights ba .
Shared-budget gap
     G = U − θ with U = min{1, H/L, mink ck }, H the retained players’ total headroom: how much the
     requirement that one set of extra minutes restore every role at once lowers coverage below the separate
     bounds (Table S46).
Inputs from games 11–30 (P28)
     Numerical inputs recomputed from each player’s positive-minute games 11 to 30 before the cutoff:
     mean minutes, capacities (hence reference minutes), the support thresholds and role rates. The sample
     construction is kept frozen: support flags, core identities, removal flags and the case and placebo
     samples come from the tables of the primary definition, whose history is the last 20 games.
Allocation model (P4.1)
      Predicted minutes are b j + x j , with x solving minx ∑k wk (Dk − ∑ j r jk x j )2 /D̄2k + λ ∑ j x2j /u j subject to
      ∑ j x j = L and 0 ≤ x j ≤ h j (headroom scaled up proportionally when it totals less than L), where
      D̄k is the mean demand in the training cases. The weights w (on the simplex) and λ minimise the
      squared error against observed minutes rescaled to a 240-minute game, in the 1,574 hybrid cases
      of 2023–24 and 2024–25 (Nelder–Mead from two starting points); 2025–26 (1,139 cases, 13,168
      player-cases) is held out. Baselines: proportional (x j = L b j / ∑ b), capacity only (w = 0, λ = 1),
      and linear regressions of extra minutes on similarity, reference minutes and headroom, or on same
      position, height gap, reference minutes and headroom (negative predictions set to zero and rescaled to
      L). Rule: the model passes if its holdout mean absolute error beats the proportional and capacity-only
      baselines with team-cluster bootstrap intervals (2,000 draws) that exclude zero.
Replacement-quality model (P4.2)
     Uses the extra minutes x̂ j predicted by the allocation model P4.1 (weights and λ estimated on the
     training seasons) for the remaining reference players. Replaced value is ∑ j x̂ j e j , the predicted extra
     minutes only, each at the player’s historical efficiency per minute e j (the rate behind lost value, last
     20 games; a missing rate     is replaced by the median of the case’s remaining players). Usage gap
     is ∑a∈R ba ga − ∑ j x̂ j g j / ∑ j (b j + x̂ j ), where g is historical usage per minute, (FGA +0.44 FTA +
     TOV)/minutes, over the same games (a missing rate counts as zero for removed players): the usage

                                                           5
      the removed players carried at reference minutes minus the usage the predicted extra minutes supply,
      per minute of the remaining rotation. Healthy-baseline strength of a team is its mean margin over
      those of its previous ten games (those that started more than three hours before the cutoff) in which
      every core player now ruled Out played; if fewer than three such games exist, the mean over all
      ten is used. The healthy-baseline strength difference is the team’s value minus the opponent’s, each
      computed with its own absent core players. The margin model regresses the final margin on lost value,
      replaced value, usage gap, removed minute share, healthy-baseline strength difference, home and rest
      difference, in the hybrid cases of all three seasons with team-clustered errors (Table S15).

Algorithm S1: reference rotation of a team-game. Input: the roster at the cutoff and each roster mem-
ber’s history. Players ruled Out for the game are included; a player’s status in the injury report does not enter
the algorithm.
    1. P ← the supported roster members. For each j ∈ P: m̄ j ← his mean minutes over his history, and
       u j ← min(40, q0.9 ), with q0.9 the 90th percentile of his history minutes (linear interpolation).
    2. If ∑ j∈P u j < 240, no reference rotation is defined. This occurs in none of the 12,306 team-games of
       the five seasons.
    3. T ← 240 and A ← P.
    4. λ ← T / ∑ j∈A m̄ j and C ← { j ∈ A : λ m̄ j > u j }.
    5. If C is empty, set b j ← λ m̄ j for every j ∈ A and stop. Otherwise set b j ← u j for every j ∈ C,
       T ← T − ∑ j∈C u j and A ← A \C, and return to step 4.
The b j sum to 240 minutes. The reference core is the three players with the largest b j . The removed set R
is the reference players ruled Out at the cutoff; the removed minutes are L = ∑a∈R ba , and the headroom of
every other reference player is h j = max(u j − b j , 0).


S2     Full results
Wild cluster restricted (WCR) bootstrap p-values are computed with 9,999 draws and Webb weights; ad-
denda P33 to P36, P38 to P40, P42 and P45 (Tables S48, S49, S50, S56, S57, S59, S60, S61, S63 and S64)
use Rademacher weights. Each analysis script uses its own seed, so the bootstrap p-value of the same co-
efficient can differ by about 0.01 between runs: the value in each table is the one produced by the run that
table reports (the main tests, Table S9; the post-hoc checks, Table S12; the season checks, Table S13; the
replication, Table S23). Table S58 gives the standard errors of the models with absorbed fixed effects when
those effects are also counted in the small-sample factor.

Table S1: The three tests, the equivalence tests and the stint-level models under the earlier version of the
data (about five reports per game day) and the complete report series. ∗: the judgement at the 0.05 level
differs. Coefficients with team-clustered p-values; equivalence: two one-sided tests at ±0.5 points per 0.1 of
coverage and the minimum detectable effect (80% power) per 0.1. Neither column has the roster corrections
R, T and D (addenda P44 and P47; Table S72); the right-hand column is the earlier build.

   Test                                              Earlier data                 Complete series
                                                 n     Coef.           p         n     Coef.            p
   Three seasons, six hours (primary)
   (1) similarity                          26,511      1.020    <0.0001    28,884      1.104    <0.0001
   (2) coverage                             2,230     −2.61       0.431     2,440     −1.51       0.622
   (3) ck                                   6,690     0.0659      0.062     7,320     0.0648      0.038     ∗
   Three seasons, hybrid

                                                        6
(1) similarity                        31,539    1.113    <0.0001   31,957    1.123    <0.0001
(2) coverage                           2,672 −0.41         0.877    2,711   −0.52       0.847
(3) ck                                 8,016 0.0664        0.024    8,133   0.0592      0.047
Three seasons, 90 minutes
(1) similarity                        33,979    1.165    <0.0001   34,000    1.166    <0.0001
(2) coverage                           2,926 −0.36         0.884    2,928   −0.32       0.897
(3) ck                                 8,778 0.0767       0.0021    8,784   0.0768     0.0022
Five seasons, six hours
(1) similarity                        42,493    1.030    <0.0001   45,883    1.077    <0.0001
(2) coverage                           3,604      0.12     0.963    3,905      0.35     0.877
(3) ck                                10,812 0.0741       0.0040   11,715   0.0675     0.0026
Five seasons, hybrid
(1) similarity                        50,291    1.083    <0.0001   50,954    1.092    <0.0001
(2) coverage                           4,294      1.31     0.505    4,355      1.27     0.530
(3) ck                                12,882 0.0762       0.0010   13,065   0.0712     0.0015
Replication seasons, six hours
(1) similarity                        15,982    1.007     0.0028   16,999    1.018     0.0040
(2) coverage                           1,374      2.92     0.327    1,465      2.62     0.420
(3) ck                                 4,122 0.0935       0.0035    4,395   0.0827     0.0057
Replication seasons, hybrid
(1) similarity                        18,752    0.999     0.0020   18,997    1.021     0.0018
(2) coverage                           1,622      2.78     0.241    1,644      2.90     0.236
(3) ck                                 4,866 0.0980       0.0014    4,932   0.0955     0.0017
Three seasons, six hours, current-season baseline
(1) similarity                        26,511    1.020    <0.0001   28,884    1.104    <0.0001
(2) coverage                           2,204 −1.74         0.610    2,414   −0.87       0.784
(3) ck                                 6,615 0.0500        0.186    7,245   0.0499      0.127
Three seasons, hybrid, current-season baseline
(1) similarity                        31,539    1.113    <0.0001   31,957    1.123    <0.0001
(2) coverage                           2,646      0.36     0.897    2,685      0.12     0.966
(3) ck                                 7,941 0.0495        0.092    8,058   0.0426      0.134
Equivalence (±0.5), test (2)
                                          n     pTOST      MDE          n   pTOST       MDE
three seasons six hours frozen        2,230     0.235       0.95    2,440   0.130        0.88
three seasons six hours with oppo-    1,966     0.094       1.05    2,254   0.122        0.99
nent
three seasons hybrid frozen           2,672     0.045       0.76    2,711    0.052       0.77   ∗
three seasons hybrid with opponent    2,654     0.059       0.81    2,693    0.056       0.85
replication six hours frozen          1,374     0.243       0.85    1,465    0.231       0.93
replication six hours with opponent   1,239     0.554       0.89    1,367    0.538       0.85
replication hybrid frozen             1,622     0.173       0.67    1,644    0.195       0.70
replication hybrid with opponent      1,604     0.388       0.69    1,627    0.391       0.70
five seasons six hours frozen         3,604     0.029       0.72    3,905    0.023       0.65
five seasons six hours with oppo-     3,205     0.195       0.80    3,621    0.105       0.74
nent
five seasons hybrid frozen            4,294     0.033       0.56    4,355    0.036       0.58


                                                 7
five seasons hybrid with opponent        4,258     0.064       0.61   4,320   0.078    0.64
Stint-level value measure, coverage coefficient in test (2)
three seasons; stint-level RAPM re-    2,230        0.66      0.808   2,440    1.47   0.573
places box-score value
three seasons; stint-level RAPM        2,230 −2.56            0.444   2,440   −1.50   0.628
added
three seasons; stint-level RAPM re-    1,966        3.02      0.289   2,254    1.48   0.558
places box-score value with oppo-
nent
five seasons; stint-level RAPM re-     3,604        2.52      0.258   3,905    2.67   0.177
places box-score value
five seasons; stint-level RAPM         3,604        0.10      0.966   3,905    0.31   0.887
added
five seasons; stint-level RAPM re-     3,205        4.51      0.046   3,621    3.66   0.073   ∗
places box-score value with oppo-
nent
three seasons, hybrid; stint-level     2,672        2.76      0.238   2,711    2.64   0.262
RAPM replaces box-score value
three seasons, hybrid; stint-level     2,672 −0.38            0.885   2,711   −0.50   0.853
RAPM added
three seasons, hybrid; stint-level     2,654        2.54      0.279   2,693    2.54   0.287
RAPM replaces box-score value
with opponent
five seasons, hybrid; stint-level      4,294        3.48      0.053   4,355    3.48   0.055
RAPM replaces box-score value
five seasons, hybrid; stint-level      4,294        1.34      0.477   4,355    1.30   0.502
RAPM added
five seasons, hybrid; stint-level      4,258        3.74      0.049   4,320    3.79   0.047
RAPM replaces box-score value
with opponent




                                                    8
                                                                (1) Role similarity                   (2) Coverage (per 0.1)           (3) Single-dimension coverage
                                                                → extra minutes                       → margin (points)                → team role output


           6-hour cutoff (primary)

                   Hybrid sample

                 90-minute cutoff

   6-hour, current-season baseline

   Hybrid, current-season baseline

    Hybrid: Capacity quantile 0.75

     Hybrid: Capacity quantile 1.0

           Hybrid: Unshrunk rates

 Hybrid: Current-team history only

     Hybrid: Low history threshold

 Hybrid: Recency 40 opportunities

   Hybrid: 24-hour history latency

  Hybrid: Six coverage dimensions

            Hybrid: Last 10 games

            Hybrid: Last 40 games

                                                                0.0      0.5          1.0   1.5           −0.5      0.0        0.5           0.00   0.05   0.10



Figure S1: Key coefficients across cutoffs, baselines and measurement definitions (final data). Points and
95% intervals (team-clustered, 30 clusters). Blue: p < 0.05; grey: not significant. Shaded rows: cutoff
and baseline definitions; other rows: measurement variants on the hybrid sample. The ten measurement
definitions are correlated variants built from the same data, and the six-dimension variant changes only the
coverage terms, so its rows for tests (1) and (3) repeat the hybrid estimate.


                                                                2
                             Final margin (residual, points)




                                                                1


                                                                0


                                                               −1


                                                               −2



                                                                    −0.25 −0.20 −0.15 −0.10 −0.05 0.00 0.05                    0.10   0.15
                                                                                   Role coverage (residual)


Figure S2: Partial relation between coverage and the final margin (final data), both net of the removed
minute share, lost value, strength difference, home and rest difference; five seasons, six-hour cutoff (3,907
cases). Points are means within deciles of residual coverage; bars are 95% team-cluster bootstrap intervals;
the dashed line is the regression slope. There is no clear gradient.


                                                                                                  9
                           Table S2: Sample description (reports timed by header).

Quantity                                                                          Value
Games / team-games                                                                3,693 / 7,386
Team-games with no report block at six hours                                      664 (9.0%)
   by season (2023–24, 2024–25, 2025–26)                                          9.5%, 11.4%, 6.1%
   by venue time zone (Eastern, Central, Mountain, Pacific)                       7.0%, 10.1%, 10.7%, 11.2%
   games tipping 9 p.m. ET or later: share of team-games / of missing             25.2% / 29.5%
blocks
Hybrid: team-games falling back to the 90-minute cutoff / still without           664 / 54 (0.7%)
a report
Core player sat out: team-games with / without a missing block                    50.6% / 47.6%
Primary cases (six-hour)                                                          2,441 in 2,013 games
   by season                                                                      630, 753, 1,058
   teams / team–core identities                                                   30 / 348
   mean reference players removed                                                 3.03
   median coverage / share reaching 1                                             0.951 / 39.2%
   median removed reference minutes                                               53.2
Hybrid cases                                                                      2,713
Six-dimension coverage: share of hybrid cases reaching 1                          18.2%
Supported roster members per team-game (mean)                                     14.3
Case rate before / after 20 December, 2023–24                                     25.4% / 29.6%
Case rate before / after 20 December, 2024–25                                     33.6% / 35.0%
Case rate before / after 20 December, 2025–26                                     50.9% / 43.3%
Case rate: share of team-games with a report block in which a core player is ruled Out for a medical reason.




                                                            10
     Table S3: Pipeline versus the hand-audited subset (184 team-games of four teams, 2023–24).

          Check                                                             Six-hour          n    Hybrid          n
          Rotation players in audited roster found                            0.9988     2,544     0.9988     2,544
          All audited roster members found                                    0.9966     3,236     0.9972     3,236
          Pipeline rotation players in audited roster                         0.9876     2,573     0.9876     2,573
          Pregame Out status agreement                                        0.9910     3,431     0.9732     3,433
          Out recall                                                          1.0000       703     1.0000       703
          Out precision                                                       0.9578       734     0.8843       795
          Identical three-player reference core                               0.9891       184     0.9891       184
          Mean core overlap                                                   0.9964       184     0.9964       184
          Audited cases recovered                                             1.0000        74     1.0000        74
          Pipeline cases that are audited cases                               0.8315        89     0.7789        95
          Coverage absolute error, median                                     0.0000        74     0.0000        74
          Coverage absolute error, 90th percentile                            0.0010        74     0.0010        74
          Coverage correlation                                                0.9814        74     0.9814        74
          Removed-minute-share correlation                                    0.9921        74     0.9921        74
Proportions. Planned thresholds (rotation recall and Out agreement at least 0.95; median coverage error at most 0.05) are
met in both samples. The reconstruction records report statuses at the six-hour cutoff only. Every disagreement on Out
status (31 six-hour, 92 hybrid) is a player whom the report selected by the pipeline lists Out (31 and 92); in 28 and 89 of
them the reconstruction had no report for the team at the six-hour cutoff, and in the other 3 it records the player as not
listed. The lower hybrid precision therefore reflects the later report, not parsing. The 15 six-hour pipeline cases that are not
audited cases are team-games whose personnel the reconstruction could not verify (in 5 of them it also records no reference
core player ruled Out for a medical reason); in all of them the selected report lists every removed core player (23 of 23)
Out, so the pipeline’s case status agrees with the source reports there, but the reconstruction cannot confirm the rosters;
the hybrid sample adds 6 such team-games. Disagreements were checked against the report PDFs by a separate check
(check_gold_case_disagreements.py). A separate check of the source records (addendum P48; not a check by
the authors) classified the 15 pipeline cases that the reconstruction could not verify: 14 confirmed (every removed core player
listed Out for a medical reason in the selected report, on the team’s roster at the cutoff by the transaction log and the box
scores, and the reference core recomputed independently from the box scores equals the pipeline’s), 0 denied and 1 not
confirmable (a player listed Out with Return to Competition Reconditioning, a reason that names no injury and is medical
only under the residual rule of the reason classification). The lead author then checked all 15 against the source records
(addendum P49): the 14 are cases, and the lead author classes the fifteenth, a reconditioning after an absence listed as not
with the team, as not medical, a judgement the reason rule of the final data does not make; without it the three planned tests
barely change (1.093; 0.056, p = 0.062; −0.08 per 0.1 of coverage), and so do those of the earlier seasons without one such
case (1.196; 0.100, p = 0.0006; +0.24 per 0.1).




                                                              11
                       Table S4: Full coefficient estimates, six-hour primary sample.

      Term                                                              Coef.        SE             p         n
      Test (1), extra minutes (case fixed effects)
      Role similarity                                            1.092            0.180     <0.0001     28,118
      Reference minutes                                          0.287            0.023     <0.0001     28,118
      Headroom                                                   0.081            0.057       0.166     28,118
      Test (2), final margin
      Constant                                                   2.469            2.803       0.386       2,441
      Coverage                                                  −0.990            2.860       0.732       2,441
      Removed minute share                                       1.586           12.557       0.900       2,441
      Lost value                                                −0.143            0.094       0.138       2,441
      Strength difference                                        0.612            0.033     <0.0001       2,441
      Home                                                       2.968            0.593     <0.0001       2,441
      Rest difference                                            0.884            0.306       0.007       2,441
      Coverage (team–core clusters)                             −0.990            2.696       0.714       2,441
      Lost value (team–core clusters)                           −0.143            0.064       0.027       2,441
      Test (3), role output
      Single-dimension coverage                                  0.054            0.029        0.070      7,323
      Removed minute share                                      −0.008            0.020        0.696      7,323
      Role: three-point attempts                                −0.045            0.028        0.122      7,323
      Role: assists                                             −0.048            0.028        0.090      7,323
      Role: rebounds                                            −0.049            0.027        0.082      7,323
      Per-minute rate change (descriptive; deviation from plan)
      Role pressure                                              0.010            0.002      0.0001     71,289
      Role: three-point attempts                                −0.002            0.001       0.021     71,289
      Role: assists                                             −0.005            0.001     <0.0001     71,289
      Role: rebounds                                            −0.004            0.001       0.006     71,289
Team-clustered CR1 standard errors unless stated. Test (3) and the rate-change model have no constant; the role dummies
are their intercepts.




                                                          12
Table S5: Test (1): role similarity and extra minutes (minutes per unit of similarity), by cutoff, baseline and
sample.

            Sample                                                         Coef.       SE             p          n
            Six-hour (primary)
            Core ruled Out, medical (main)                                 1.092    0.180     <0.0001      28,118
            (a) Excluding previous-day reports                             1.092    0.180     <0.0001      28,118
            (b) Core ruled Out for any reason                              1.095    0.175     <0.0001      29,311
            (c) Excluding coverage = 1                                     1.353    0.224     <0.0001      16,580
            Hybrid
            Core ruled Out, medical (main)                                 1.113    0.172     <0.0001      31,117
            (a) Excluding previous-day reports                             1.113    0.172     <0.0001      31,117
            (b) Core ruled Out for any reason                              1.115    0.168     <0.0001      32,549
            (c) Excluding coverage = 1                                     1.402    0.202     <0.0001      18,578
            90-minute
            Core ruled Out, medical (main)                                 1.163    0.163     <0.0001      33,121
            (a) Excluding previous-day reports                             1.163    0.163     <0.0001      33,121
            (b) Core ruled Out for any reason                              1.165    0.162     <0.0001      34,657
            (c) Excluding coverage = 1                                     1.562    0.197     <0.0001      20,016
            Six-hour, current-season baseline
            Core ruled Out, medical (main)                                 1.092    0.180     <0.0001      28,118
            (a) Excluding previous-day reports                             1.092    0.180     <0.0001      28,118
            (b) Core ruled Out for any reason                              1.095    0.175     <0.0001      29,311
            (c) Excluding coverage = 1                                     1.353    0.224     <0.0001      16,580
            Hybrid, current-season baseline
            Core ruled Out, medical (main)                                 1.113    0.172     <0.0001      31,117
            (a) Excluding previous-day reports                             1.113    0.172     <0.0001      31,117
            (b) Core ruled Out for any reason                              1.115    0.168     <0.0001      32,549
            (c) Excluding coverage = 1                                     1.402    0.202     <0.0001      18,578
  Team-clustered CR1 standard errors, 30 clusters, t(29). Planned pass rule: coefficient positive and p < 0.05 in the six-hour
  main sample. Sensitivity samples (a)–(c) were fixed in the plan; the hybrid, 90-minute and current-season-baseline rows
  were added later and are reported as sensitivity analyses. Sensitivity analysis (a), excluding previous-day reports, removes
  no case in any of these samples, so its rows equal the main rows.


                 Table S6: Position and height controls for test (1). Cells: coefficient (SE), p.

      Model                                   Role similarity           Same position           Height gap (per inch)
      Six-hour primary (n = 28,117 player-cases with position and height)
      Similarity only                     1.09 (0.18), <0.0001 –                                –
      Position and height only            –                     0.54 (0.22), 0.020              −0.22 (0.04), <0.0001
      Both                                0.89 (0.19), <0.0001 0.34 (0.22), 0.131               −0.19 (0.04), 0.0002
      Share of similarity coefficient re- 82%
      tained
      Hybrid (n = 31,116 player-cases with position and height)
      Similarity only                     1.11 (0.17), <0.0001 –                                –
      Position and height only            –                     0.59 (0.20), 0.007              −0.22 (0.04), <0.0001
      Both                                0.91 (0.18), <0.0001 0.39 (0.20), 0.069               −0.18 (0.04), 0.0002
      Share of similarity coefficient re- 82%
      tained
  Case fixed effects; reference minutes and headroom included; team-clustered errors. The controls were written down before
  estimation (P3 addendum A).



                                                              13
Table S7: Test (2): coverage and final margin (points per unit of coverage), by cutoff, baseline and sample.

              Sample                                                          Coef.        SE         p         n
              Six-hour (primary)
              Core ruled Out, medical (main)                                −0.990      2.860    0.732     2,441
              (a) Excluding previous-day reports                            −0.990      2.860    0.732     2,441
              (b) Core ruled Out for any reason                             −1.384      2.951    0.643     2,545
              (c) Excluding coverage = 1                                     0.621      3.373    0.855     1,483
              Hybrid
              Core ruled Out, medical (main)                                −0.077      2.550    0.976     2,713
              (a) Excluding previous-day reports                            −0.077      2.550    0.976     2,713
              (b) Core ruled Out for any reason                             −0.408      2.581    0.876     2,838
              (c) Excluding coverage = 1                                     0.265      2.853    0.927     1,670
              90-minute
              Core ruled Out, medical (main)                                 0.059      2.334    0.980     2,929
              (a) Excluding previous-day reports                             0.059      2.334    0.980     2,929
              (b) Core ruled Out for any reason                             −0.180      2.365    0.940     3,064
              (c) Excluding coverage = 1                                     0.219      2.636    0.934     1,829
              Six-hour, current-season baseline
              Core ruled Out, medical (main)                                −0.846      3.132    0.789     2,415
              (a) Excluding previous-day reports                            −0.846      3.132    0.789     2,415
              (b) Core ruled Out for any reason                             −1.361      3.192    0.673     2,517
              (c) Excluding coverage = 1                                     0.210      3.497    0.953     1,465
              Hybrid, current-season baseline
              Core ruled Out, medical (main)                                 0.093      2.799    0.974     2,687
              (a) Excluding previous-day reports                             0.093      2.799    0.974     2,687
              (b) Core ruled Out for any reason                             −0.345      2.806    0.903     2,810
              (c) Excluding coverage = 1                                    −0.189      2.989    0.950     1,652
  Team-clustered CR1 standard errors, 30 clusters, t(29). Planned pass rule: coefficient positive and p < 0.05 in the six-hour
  main sample. Sensitivity samples (a)–(c) were fixed in the plan; the hybrid, 90-minute and current-season-baseline rows
  were added later and are reported as sensitivity analyses. Sensitivity analysis (a), excluding previous-day reports, removes
  no case in any of these samples, so its rows equal the main rows.




                                                              14
Table S8: Test (3): single-dimension coverage and team role output (proportion of ten-game baseline), by
cutoff, baseline and sample.

               Sample                                                        Coef.        SE         p         n
               Six-hour (primary)
               Core ruled Out, medical (main)                                0.054     0.029    0.070     7,323
               (a) Excluding previous-day reports                            0.054     0.029    0.070     7,323
               (b) Core ruled Out for any reason                             0.058     0.028    0.045     7,635
               (c) Excluding coverage = 1                                    0.049     0.028    0.093     4,449
               Hybrid
               Core ruled Out, medical (main)                                0.050     0.028    0.086     8,139
               (a) Excluding previous-day reports                            0.050     0.028    0.086     8,139
               (b) Core ruled Out for any reason                             0.052     0.027    0.059     8,514
               (c) Excluding coverage = 1                                    0.046     0.028    0.110     5,010
               90-minute
               Core ruled Out, medical (main)                                0.069     0.023    0.005     8,787
               (a) Excluding previous-day reports                            0.069     0.023    0.005     8,787
               (b) Core ruled Out for any reason                             0.073     0.022    0.002     9,192
               (c) Excluding coverage = 1                                    0.067     0.022    0.005     5,487
               Six-hour, current-season baseline
               Core ruled Out, medical (main)                                0.041     0.032    0.203     7,248
               (a) Excluding previous-day reports                            0.041     0.032    0.203     7,248
               (b) Core ruled Out for any reason                             0.043     0.031    0.172     7,554
               (c) Excluding coverage = 1                                    0.037     0.030    0.217     4,395
               Hybrid, current-season baseline
               Core ruled Out, medical (main)                                0.035     0.028    0.216     8,064
               (a) Excluding previous-day reports                            0.035     0.028    0.216     8,064
               (b) Core ruled Out for any reason                             0.037     0.027    0.183     8,433
               (c) Excluding coverage = 1                                    0.032     0.026    0.218     4,956
  Team-clustered CR1 standard errors, 30 clusters, t(29). Planned pass rule: coefficient positive and p < 0.05 in the six-hour
  main sample. Sensitivity samples (a)–(c) were fixed in the plan; the hybrid, 90-minute and current-season-baseline rows
  were added later and are reported as sensitivity analyses. Sensitivity analysis (a), excluding previous-day reports, removes
  no case in any of these samples, so its rows equal the main rows.




         Table S9: Wild cluster restricted bootstrap (Webb weights, 9,999 draws, 30 team clusters).

         Coefficient                                                   t (CR1)       p (CR1)     p (WCR)            n
         Six-hour, test (1) role similarity                             6.055      <0.0001         0.0001     28,118
         Six-hour, test (2) coverage                                   −0.346        0.732         0.7380      2,441
         Six-hour, test (3) single-dimension coverage                   1.880        0.070         0.0711      7,323
         Hybrid, test (1) role similarity                               6.472      <0.0001         0.0001     31,117
         Hybrid, test (2) coverage                                     −0.030        0.976         0.9786      2,713
         Hybrid, test (3) single-dimension coverage                     1.776        0.086         0.0891      8,139
         Hybrid, replaced value (P4.2)                                  2.884        0.007         0.0125      2,713




                                                              15
           Table S10: Measurement definitions, hybrid sample: key coefficients of tests (1)–(3).

           Definition                               Sim.             p   Coverage         p       ck      p
           Primary definition                       1.11    <0.0001          −0.08     0.976   0.050   0.086
           Capacity quantile 0.75                   1.12    <0.0001          −0.90     0.704   0.028   0.150
           Capacity quantile 1.0                    1.11    <0.0001           0.93     0.757   0.064   0.057
           Unshrunk rates                           1.11    <0.0001          −0.06     0.982   0.052   0.042
           Current-team history only                1.11    <0.0001          −0.49     0.814   0.030   0.129
           Low history threshold                    1.04    <0.0001          −0.37     0.903   0.060   0.090
           Recency: 40 team games                   1.00    <0.0001           0.49     0.838   0.054   0.061
           24-hour history latency                  1.11    <0.0001          −0.13     0.960   0.047   0.094
           Six coverage dimensions                  1.11    <0.0001          −0.69     0.780   0.050   0.086
           Last 10 games                            0.81     0.0006          −3.29     0.149   0.041   0.060
           Last 40 games                            1.11    <0.0001          −0.83     0.756   0.064   0.030
Each definition rebuilds every table from the raw inputs. Team-clustered CR1 errors.




                        Table S11: Descriptive cost of an absence (points of final margin).

Quantity                                                                      Value
Six-hour primary
Core absence vs other games, same team-season (simple / weighted              −2.26 / −2.03
mean)
Team-seasons                                                                  90
Margin vs team-season mean, 0 / 1 / 2+ cores out (team-games)                 0.66 (4,281) / −0.82 (1,940) / −2.47
                                                                              (501)
All team-games: margin per unit of own absence value (n = 6,204)              −0.116 (SE 0.014), p <0.0001
Implied cost at the median / upper-quartile case                              −3.62 / −4.87
Opponent ten-game margin, core-absence vs other games                         0.13 / −0.02
Hybrid
Core absence vs other games, same team-season (simple / weighted              −2.17 / −1.99
mean)
Team-seasons                                                                  90
Margin vs team-season mean, 0 / 1 / 2+ cores out (team-games)                 0.63 (4,619) / −0.66 (2,132) / −2.60
                                                                              (581)
All team-games: margin per unit of own absence value (n = 7,280)              −0.113 (SE 0.011), p <0.0001
Implied cost at the median / upper-quartile case                              −3.60 / −4.82
Opponent ten-game margin, core-absence vs other games                         0.10 / −0.07
Descriptive comparison, not a causal estimate. The all-team-games model uses games in which both teams have a report
block.




                                                           16
  Table S12: Post-hoc checks, specified in writing after the main results were known (exploratory).

   Model                                                               Coef.       SE            p   p (WCR)
   Six-hour primary
   Coverage, frozen model (n = 2,441)                                 −0.990    2.860      0.732        0.7375
   Coverage, with opponent absence value (n = 2,255)                  −0.485    3.135      0.878        0.8805
     opponent absence value                                            0.124    0.016    <0.0001             –
   Coverage × lost value (n = 2,255)                                   0.081    0.108      0.460        0.4722
   Unmanaged absences only (2,212 of 2,441 cases): test (1)            1.145    0.177    <0.0001        0.0001
     test (2) coverage, with opponent absence value (n = 2,045)        0.256    2.931      0.931        0.9325
     test (3) ck                                                       0.066    0.029      0.029        0.0343
   Hybrid
   Coverage, frozen model (n = 2,713)                                 −0.077    2.550      0.976        0.9782
   Coverage, with opponent absence value (n = 2,695)                   0.158    2.728      0.954        0.9574
     opponent absence value                                            0.122    0.015    <0.0001             –
   Coverage × lost value (n = 2,695)                                   0.076    0.089      0.399        0.4083
   Unmanaged absences only (2,436 of 2,713 cases): test (1)            1.164    0.166    <0.0001        0.0001
     test (2) coverage, with opponent absence value (n = 2,420)        0.851    2.600      0.746        0.7535
     test (3) ck                                                       0.065    0.027      0.021        0.0258
Managed absences: a core player listed Out for a medical reason whose text mentions injury management, maintenance,
reconditioning or rest. Opponents without a report block are dropped, not treated as healthy.




            Table S13: Season composition checks (addendum P9, written before running).

      Model                                                   Coef.       SE         p   p (WCR)          n
      Six-hour primary
      Test (2), frozen                                       −0.990    2.860    0.732       0.7464    2,441
      Test (2) + season FE                                   −1.003    2.796    0.722       0.7297    2,441
      Test (2) + opponent absence                            −0.485    3.135    0.878       0.8852    2,255
      Test (2) + opponent absence + season FE                −0.468    3.123    0.882       0.8868    2,255
      Test (2), excluding 2025–26 before 20 Dec              −1.276    2.660    0.635       0.6480    2,064
      Test (3), frozen                                        0.054    0.029    0.070       0.0722    7,323
      Test (3) + season FE                                    0.053    0.029    0.077       0.0861    7,323
      Test (3) + season × role FE                             0.055    0.028    0.064       0.0710    7,323
      Test (3), excluding 2025–26 before 20 Dec               0.063    0.032    0.055       0.0639    6,192
      Hybrid
      Test (2), frozen                                       −0.077    2.550    0.976       0.9763    2,713
      Test (2) + season FE                                   −0.115    2.484    0.963       0.9657    2,713
      Test (2) + opponent absence                             0.158    2.728    0.954       0.9613    2,695
      Test (2) + opponent absence + season FE                 0.218    2.702    0.936       0.9377    2,695
      Test (2), excluding 2025–26 before 20 Dec               0.286    2.501    0.910       0.9119    2,296
      Test (3), frozen                                        0.050    0.028    0.086       0.0909    8,139
      Test (3) + season FE                                    0.049    0.028    0.091       0.1030    8,139
      Test (3) + season × role FE                             0.050    0.028    0.079       0.0863    8,139
      Test (3), excluding 2025–26 before 20 Dec               0.053    0.029    0.080       0.0830    6,888




                                                        17
Table S14: Out-of-sample minute prediction (P4.1). Training: 1,574 hybrid cases (2023–24, 2024–25);
holdout: 1,139 cases, 13,168 player-cases (2025–26).

         Model                                                      MAE (min)        Difference vs model [95% CI]
         Inverse-optimisation model                                        7.178     –
         Proportional to reference minutes                                 7.201     0.023 [−0.037, 0.081]
         Capacity only (no role term)                                      7.190     0.011 [−0.020, 0.045]
         Regression on role similarity                                     7.175     −0.004 [−0.039, 0.035]
         Regression on position and height                                 7.166     −0.012 [−0.056, 0.031]
  Estimated role weights: three-point attempts 0.39, assists 0.29, rebounds 0.32; λ = 0.0198. A positive difference favours
  the model; team-cluster bootstrap, 2,000 draws. Planned test: the model must beat both the proportional and the capacity-
  only baseline, each with an interval excluding zero. It does neither: against proportional allocation the difference is 0.023
  [−0.037, 0.081], and against the capacity-only baseline 0.011 [−0.020, 0.045], an interval that includes zero.




                            Table S15: Replacement quality and the skill curve (P4.2).

       Term                                                                               Coef.         SE              p
       Margin model, hybrid sample (n = 2,713)
       Constant                                                                          0.985       0.778       0.215
       Lost value                                                                       −0.166       0.070       0.025
       Replaced value                                                                    0.521       0.181       0.007
       Usage gap                                                                        11.778      13.483       0.390
       Removed minute share                                                            −57.406      22.381       0.016
       Healthy-baseline strength difference                                              0.532       0.029     <0.0001
       Home                                                                              2.945       0.566     <0.0001
       Rest difference                                                                   0.690       0.329       0.045
       Coverage, added to the model                                                     −0.989           –       0.749
       Replaced value, dropping the 18 cases whose opponent had no report                0.485       0.183       0.013
       Fragility (post-hoc)
       Correlation of replaced value with removed minute share                            0.977
       Correlation with the proportional-allocation version                               0.996
       Proportional-allocation version in place of replaced value                         0.509          –        0.002
       Remaining rotation mean efficiency in place of replaced value                     34.567          –        0.002
       By season, 2023–24 (n = 706)                                                       0.988          –       0.0004
       By season, 2024–25 (n = 868)                                                       0.428          –        0.024
       By season, 2025–26 (n = 1,139)                                                     0.300          –        0.289
       Holdout RMSE: base / + replaced value and usage gap / + coverage                  15.040     15.022       15.043
       (n = 1,139)
       Skill curve: true-shooting change per unit load change (n = 19,942,              −0.011       0.010         0.287
       player FE)
  Team-clustered CR1 errors. By-season models omit the usage gap; on the earlier build this specification reproduced the
  by-season p-values of the original P4 report.




                                                              18
Table S16: Margin against the closing spread, 2025–26 hybrid cases (75.8% of 1,139 cases have a spread;
mean −0.15, SD 14.12).

                    Term                                                                   Coef.         p
                    Lost value and replaced value (n = 863)
                    Constant                                                              1.903      0.070
                    Lost value                                                           −0.016      0.832
                    Replaced value                                                       −0.050      0.551
                    Adding removed minute share (n = 863)
                    Constant                                                              1.952      0.042
                    Lost value                                                           −0.025      0.776
                    Replaced value                                                       −0.082      0.643
                    Removed minute share                                                  4.976      0.850
  Team-clustered CR1 errors. Descriptive; no threshold was set.




Table S17: Earlier data with reports timed by file name, against the final data (header times, complete report
series). Cells: coefficient (p), n.

    Result                                                 File-name timing, earlier data       Final data
    Six-hour (primary), test (1)                           1.037 (<0.0001), 27,655              1.092 (<0.0001), 28,118
    Six-hour (primary), test (2)                           −2.508 (0.433), 2,330                −0.990 (0.732), 2,441
    Six-hour (primary), test (3)                           0.071 (0.054), 6,990                 0.054 (0.070), 7,323
    Hybrid, test (1)                                       1.073 (<0.0001), 31,610              1.113 (<0.0001), 31,117
    Hybrid, test (2)                                       0.812 (0.769), 2,683                 −0.077 (0.976), 2,713
    Hybrid, test (3)                                       0.070 (0.021), 8,049                 0.050 (0.086), 8,139
    90-minute, test (1)                                    1.141 (<0.0001), 34,952              1.163 (<0.0001), 33,121
    90-minute, test (2)                                    0.573 (0.816), 3,030                 0.059 (0.980), 2,929
    90-minute, test (3)                                    0.072 (0.004), 9,090                 0.069 (0.005), 8,787
    Gold standard: Out agreement / coverage cor-           0.9816 / 0.946                       0.9910 / 0.981
    relation
    P4.1 holdout MAE: model / proportional                 7.469 / 7.456                        7.178 / 7.201
    P4.2 replaced value                                    0.490 (0.015)                        0.521 (0.007)
  The right-hand column combines three changes: header timing (addendum P10), the complete report series (addendum P19)
  and the roster corrections R, T and D (addenda P44 and P47). Header timing alone changed no planned verdict: test (3) had
  p = 0.062 with header times on the earlier data, against 0.054 with file-name times. The complete series then moved test (3)
  below 0.05 on the earlier build (Table S1), and the roster corrections moved it back above (Table S72).




                                                              19
Table S18: Placebo for test (1): role similarity and extra minutes when the core player is present (six-hour
sample; addenda P11 and P15).

  Sample                                          Coef.       SE              p    p (WCR)      Player-cases / pseudo-cases
  Actual absences (test (1), main sample)        1.092     0.180     <0.0001         0.0001     28,118 / 2,441
  Placebo A1: every core player of a            −0.156     0.087       0.084         0.0815     123,306 / 10,566
  team-game with all three cores play-
  ing, in turn
  Placebo A2: pseudo-absent player re-          −0.158     0.090         0.089       0.0826     113,393 / 9,697
  stricted to cores who do miss games in
  the sample
  Actual minus placebo A1 (stacked in-            1.248    0.204     <0.0001         0.0001     151,424
  teraction)
  Actual minus placebo A2 (stacked in-            1.250    0.204     <0.0001         0.0001     141,511
  teraction)
  Sensitivity: one pseudo-absent core           −0.209     0.089         0.026       0.0262     –
  drawn at random (seed 20260922)
  Case fixed effects (team-game × pseudo-absent player), reference minutes and headroom; team-clustered errors. Role rates
  are standardised with the means and standard deviations over the reference players of the cases of the main sample (the
  standardisation of test (1) also includes team-games with a core player ruled Out for a non-medical reason, Section S1; the
  moments differ only in the fourth decimal), and similarity is the cosine of the standardised rate vectors. As in a real case,
  players listed Out are removed from the placebo sample; P11 had kept them, which made the placebo coefficient spuriously
  negative (addendum P15). Over 20 random draws (seeds 20260922–20260941) the A1 coefficient ranges from −0.234 to
  −0.097 (p 0.023–0.363), which is why every core player is used in turn.




Table S19: Alternative measures of absence value: margin on own and opponent absence value, strength,
home and rest, all team-games in which both teams have a report block (addendum P11).

           Measure                                                        Own coef.             t       R2         n
           Six-hour primary: predictive power across all team-games
           Box-score efficiency (used in the paper)               −0.1157                 −8.25      0.206    6,204
           Regularised plus-minus, two previous seasons           −0.0061                 −1.43      0.183    6,204
           Shrunk on-court plus-minus                               0.2603                 3.30      0.186    6,204
           Shrunk team-relative plus-minus (amendment)            −0.5307                 −2.51      0.184    6,204
           Hybrid: predictive power across all team-games
           Box-score efficiency (used in the paper)               −0.1128                −10.01      0.206    7,280
           Regularised plus-minus, two previous seasons           −0.0040                 −1.18      0.183    7,280
           Shrunk on-court plus-minus                               0.2929                 4.52      0.187    7,280
           Shrunk team-relative plus-minus (amendment)            −0.4461                 −2.27      0.184    7,280
  The own and opponent coefficients are equal and opposite by construction because every game appears once from each side.




                                                              20
Table S20: Test (2) with alternative measures of absence value: coverage coefficient (addendum P11).

    Model                                                Coef.     SE       p    p (WCR)      n
    Six-hour primary
    Regularised plus-minus replaces lost value           1.882   2.469   0.452    0.4691   2,441
    Regularised plus-minus added                        −1.015   2.845   0.724    0.7296   2,441
    Regularised plus-minus, with opponent                1.787   2.199   0.423    0.4313   2,255
    On-court plus-minus replaces lost value              2.636   2.462   0.293    0.3111   2,441
    On-court plus-minus added                           −0.914   2.883   0.754    0.7611   2,441
    On-court plus-minus, with opponent                   2.589   2.366   0.283    0.2907   2,255
    Team-relative plus-minus replaces lost value         1.622   2.308   0.488    0.5077   2,441
    Team-relative plus-minus added                      −0.985   2.845   0.732    0.7397   2,441
    Team-relative plus-minus, with opponent              1.641   2.142   0.450    0.4623   2,255
    Hybrid
    Regularised plus-minus replaces lost value           2.925   2.311   0.216    0.2252   2,713
    Regularised plus-minus added                        −0.121   2.541   0.962    0.9625   2,713
    Regularised plus-minus, with opponent                2.529   2.269   0.274    0.2752   2,695
    On-court plus-minus replaces lost value              3.533   2.276   0.132    0.1420   2,713
    On-court plus-minus added                           −0.038   2.539   0.988    0.9889   2,713
    On-court plus-minus, with opponent                   3.138   2.333   0.189    0.1941   2,695
    Team-relative plus-minus replaces lost value         2.428   2.166   0.271    0.2820   2,713
    Team-relative plus-minus added                      −0.083   2.533   0.974    0.9747   2,713
    Team-relative plus-minus, with opponent              2.135   2.153   0.330    0.3350   2,695




                                                   21
Table S21: Equivalence tests and minimum detectable effects for test (2), per 0.1 of coverage (addenda P11
and P12).

      Sample and model                          Estimate     90% interval       TOST ±0.5        TOST ±0.25          MDE
      Three seasons, six-hour, frozen              −0.10     [−0.58, 0.39]             0.086            0.301        0.83
      Three seasons, six-hour, with oppo-          −0.05     [−0.58, 0.48]             0.080            0.263        0.91
      nent
      Three seasons, hybrid, frozen                −0.01     [−0.44, 0.43]             0.032            0.175        0.74
      Three seasons, hybrid, with oppo-             0.02     [−0.45, 0.48]             0.043            0.199        0.79
      nent
      Replication seasons, six-hour,                 0.24    [−0.31, 0.80]             0.219            0.491        0.95
      frozen
      Replication seasons, six-hour, with            0.50    [−0.01, 1.02]             0.500            0.792        0.88
      opponent
      Replication seasons, hybrid, frozen            0.26    [−0.15, 0.67]             0.167            0.518        0.71
      Replication seasons, hybrid, with              0.40    [−0.02, 0.81]             0.337            0.720        0.71
      opponent
      Five seasons, six-hour, frozen                 0.05    [−0.32, 0.42]             0.023            0.181        0.63
      Five seasons, six-hour, with oppo-             0.18    [−0.24, 0.59]             0.099            0.382        0.71
      nent
      Five seasons, hybrid, frozen                   0.13    [−0.20, 0.46]             0.035            0.279        0.56
      Five seasons, hybrid, with oppo-               0.18    [−0.18, 0.54]             0.071            0.372        0.61
      nent
      Three seasons, six-hour, net rating          −0.09     [−0.56, 0.39]             0.079                 –       0.81
      per 100 possessions
      Three seasons, six-hour, net rating,         −0.03     [−0.55, 0.48]             0.071                 –         –
      with opponent
  Two one-sided tests against ±0.5 and ±0.25 points per 0.1 of coverage (for net rating, the equivalent in net-rating units;
  the ±0.25 bound and the with-opponent rows for the replication and five-season samples come from addendum P15; the
  net-rating rows have neither); t(29). TOST columns give the p-value of the two one-sided tests. MDE: minimum detectable
  effect at 80% power, (t0.975 + t0.80 )×SE.



                   Table S22: First game of an absence versus later games (addendum P11).

              Term                                                                  Coef.        SE              p
              Six-hour primary: first game of an absence in 459 cases (19%)
              Test (1): similarity, later games                             1.017              0.173   <0.0001
              Test (2): coverage, later games                             −0.966               3.340     0.774
              Test (3): ck , later games                                    0.041              0.033     0.226
              Test (1): similarity × first game                             0.423              0.294     0.160
              Test (2): coverage × first game                             −1.277               6.345     0.842
              Test (3): ck × first game                                     0.038              0.064     0.558
              Hybrid: first game of an absence in 554 cases (20%)
              Test (1): similarity, later games                             1.025              0.170   <0.0001
              Test (2): coverage, later games                             −0.450               2.833     0.875
              Test (3): ck , later games                                    0.035              0.036     0.335
              Test (1): similarity × first game                             0.456              0.275     0.109
              Test (2): coverage × first game                               0.142              5.427     0.979
              Test (3): ck × first game                                     0.032              0.060     0.594
  First game: the absent core player took part in the team’s previous game. Heterogeneity by head coach is in Table S28.



                                                              22
         Table S23: Frozen tests in the replication seasons and in all five seasons (addendum P12).

       Test                                                     Coef.        SE              p         p (WCR)             n
       Replication seasons (2021–22, 2022–23), six-hour (cases: 764, 702)
       Test (1) role similarity                          1.196 0.256 <0.0001                           0.0001       16,583
       Test (2) coverage                                 2.423 3.275       0.465                       0.4755        1,466
       Test (3) single-dimension coverage                0.100 0.026      0.0006                       0.0012        4,398
       Test (1) with position and height                 0.908 0.246      0.0009                  76% retained      16,574
       Replication seasons, hybrid (cases: 852, 793)
       Test (1) role similarity                          1.193 0.237 <0.0001                           0.0001       18,526
       Test (2) coverage                                 2.608 2.432       0.292                       0.3093        1,645
       Test (3) single-dimension coverage                0.118 0.027      0.0001                       0.0004        4,935
       Test (1) with position and height                 0.917 0.231      0.0004                  77% retained      18,517
       Five seasons, six-hour (cases: 764, 702, 630, 753, 1,058)
       Test (1) role similarity                          1.140 0.141 <0.0001                           0.0001       44,701
       Test (2) coverage                                 0.502 2.161       0.818                       0.8186        3,907
       Test (3) single-dimension coverage                0.070 0.020       0.002                       0.0022       11,721
       Test (1) with position and height                 0.918 0.145 <0.0001                      80% retained      44,691
       Five seasons, hybrid (cases: 852, 793, 706, 868, 1,139)
       Test (1) role similarity                          1.154 0.131 <0.0001                           0.0001       49,643
       Test (2) coverage                                 1.347 1.941       0.493                       0.4949        4,358
       Test (3) single-dimension coverage                0.076 0.021      0.0009                       0.0010       13,074
       Test (1) with position and height                 0.929 0.136 <0.0001                      80% retained      49,633
  Rule written before running: a test replicates if its coefficient has the original sign and p < 0.05 in the replication seasons.
  Tests (1) and (3) replicate; test (3) also without COVID-19 protocol cases in the six-hour sample (Table S33), but not once
  the benchmark is controlled (Table S30); test (2) is null.

       Table S24: Stint-level regularised adjusted plus-minus: estimation samples (addendum P16).

     Season analysed                     Stints (two previous seasons)        Players         λ    Possessions per minute
     2021–22                                                      61,786          635     3,200                          2.03
     2022–23                                                      67,138          697     3,200                          2.07
     2023–24                                                      71,719          711     3,200                          2.07
     2024–25                                                      70,996          661     3,200                          2.08
     2025–26                                                      71,269          694     3,200                          2.07
  Lineups are reconstructed from the cached play-by-play: 241,913 stints in 8,259 of 8,292 games, with all four periods usable
  in 96.0% of games (319 periods dropped, 0.96%). Summing each game’s stint points reproduces the final score exactly in
  57.8% of games and within four points in 89.9%, counting the two teams’ score errors together; the validation of addendum
  P30 allows four points for each team separately and gives 92.3% on the same stints (Table S47). λ is chosen by five-fold
  cross-validation grouped by game over 25–51,200; the selected value is interior in every season.

Table S25: Margin on two measures of absence value, same sample of team-games in which both teams
have a report block (addenda P16 and P17).

                    Measure                                             Coef.            t        R2          n
                    Box-score efficiency                             −0.105       −10.49     0.174     10,362
                    Stint-level RAPM                                 −0.405        −2.64     0.155     10,362
  Own and opponent absence value, strength difference, home and rest difference; five seasons. The own and opponent
  coefficients are equal and opposite by construction, because every game enters once from each side. The regularised, on-
  court and team-relative plus-minus measures of Table S19 (t −1.43, +3.30, −2.51) were estimated on the three original
  seasons only and are not comparable with these. Between 7.0% and 10.4% of the reference players listed Out have no
  RAPM (rookies and new arrivals) and enter with a value of zero; they hold 5.2–7.9% of the lost reference minutes.


                                                                23
               Table S26: Test (2) with the RAPM measure of absence value (addendum P16).
   Model                          Coverage       SE           p    p (WCR)      90% interval per 0.1       TOST ±0.5       n
   Three seasons, six-hour
   RAPM replaces the box-            1.788    2.526       0.485      0.4930     [−0.25, 0.61]                  0.107   2,441
   score value
   RAPM added beside it             −0.985    2.871       0.734      0.7442     [−0.59, 0.39]                  0.086   2,441
   RAPM replaces it, with op-        1.843    2.346       0.439      0.4430     [−0.21, 0.58]                  0.094   2,255
   ponent
   Five seasons, six-hour
   RAPM replaces the box-            2.777    1.919       0.159      0.1624     [−0.05, 0.60]                  0.128   3,907
   score value
   RAPM added beside it              0.481    2.094       0.820      0.8242     [−0.31, 0.40]                  0.020   3,907
   RAPM replaces it, with op-        3.770    1.932       0.061      0.0715     [0.05, 0.71]                   0.265   3,623
   ponent
   Three seasons, hybrid
   RAPM replaces the box-            2.895    2.305       0.219      0.2338     [−0.10, 0.68]                  0.184   2,713
   score value
   RAPM added beside it             −0.077    2.538       0.976      0.9772     [−0.44, 0.42]                  0.031   2,713
   RAPM replaces it, with op-        2.779    2.279       0.233      0.2405     [−0.11, 0.67]                  0.169   2,695
   ponent
   Five seasons, hybrid
   RAPM replaces the box-            3.531    1.730    0.05037       0.0629     [0.06, 0.65]                   0.201   4,358
   score value
   RAPM added beside it              1.392    1.850       0.458      0.4699     [−0.18, 0.45]                  0.030   4,358
   RAPM replaces it, with op-        3.836    1.808       0.043      0.0546     [0.08, 0.69]                   0.262   4,323
   ponent
  Exploratory. None of the six six-hour models gives a coverage coefficient with p < 0.05 (smallest p = 0.061); that model
  is decomposed in Table S27. Of the six hybrid models, one has p < 0.05 (smallest 0.043, WCR 0.0546). Added beside the
  box-score value, the RAPM term itself takes the wrong sign, so it partly tracks team strength.




Table S27: Where the six-hour stint-level coverage coefficient with the smallest p comes from (addendum
P17).

               Model                                                     Coverage         SE           p        n
               Five seasons, RAPM replaces the box-score value                2.777    1.919    0.159        3,907
               Same, restricted to team-games whose opponent                  3.549    1.957    0.080        3,623
               filed a report
               Same, adding the opponent’s RAPM absence                       3.770    1.932    0.061        3,623
               value
               Same, adding both of the opponent’s absence-                   4.093    2.044    0.055        3,623
               value measures
               With the opponent term, dropping 2021–22                       1.590    2.558    0.539        2,907
               With the opponent term, keeping the box-score                  1.523    2.262    0.506        3,623
               value as well
  Dropping the 284 team-games whose opponent filed no report moves the coefficient by 0.77; the opponent term itself moves
  it by 0.22. Corrected for the six models of Table S26, the smallest p is 0.36 (Bonferroni). Clustered t-tests; no bootstrap.




                                                              24
                               Table S28: Test (1) by head coach (addendum P16).

 Quantity                                                       Coef.            SE                          p        Sample
 Pooled similarity slope (all coaches)                        1.092          0.180                   <0.0001           2,441
 Coach-specific slopes: median (quar-          1.187 (0.442, 1.713)       SD 1.229                         –      40 coaches
 tiles)
 Coach-specific slopes: range                      −0.829 to 5.116                –                         –               –
 Pooled group of five short spells                         −2.056                 –                         –               –
 Similarity slope, teams that changed                        1.462            0.505                     0.012           1,295
 coach
 Change in that slope after the change                        −0.338          0.446     0.461 (WCR 0.473)            15 teams
Head-coach spells were compiled from public encyclopaedia pages (not derived by the pipeline), each row with its source
and the date it was read; every case in the primary sample matched a spell. Coaches with fewer than 15 cases are pooled
into one group, shown separately and excluded from the quartiles and the range. Per-coach standard errors are not reported:
a coach sits almost entirely inside one team, so team-clustered errors for his slope are degenerate, and for the same reason a
joint test across coaches is not possible (30 clusters, 40 contrasts). The last two rows are the only comparison that separates
coach from team, and they use the 15 teams that changed coach inside the sample.




   Table S29: Further checks of the three tests (addendum P23; exploratory). Cells: coefficient (p).

Sample                              Frozen / share              Check                                Extra term          Cases
Test (3) with the removed share of each role’s baseline output as a control
Three seasons, six-hour         0.054 (0.070)              0.078 (0.040); WCR 0.0467    0.057 (0.219)                     2,441
Three seasons, hybrid           0.050 (0.086)              0.077 (0.031); WCR 0.0359    0.068 (0.109)                     2,713
Five seasons, six-hour          0.070 (0.002)              0.099 (0.001); WCR 0.0013    0.078 (0.062)                     3,907
Five seasons, hybrid            0.076 (0.0009)             0.106 (0.0005); WCR 0.0008 0.081 (0.035)                       4,358
Ten-game baseline crossing a season boundary: share of cases; test (3) without those cases
Three seasons, six-hour         288 of 2,441 (11.8%) 0.061 (0.077); WCR 0.0805          –                                 2,153
Three seasons, hybrid           312 of 2,713 (11.5%) 0.054 (0.084); WCR 0.0898          –                                 2,401
Five seasons, six-hour          427 of 3,907 (10.9%) 0.075 (0.0005); WCR 0.0007 –                                         3,480
Five seasons, hybrid            470 of 4,358 (10.8%) 0.079 (0.0005); WCR 0.0005 –                                         3,888
Current-season baselines: test (1) similarity, test (2) coverage, test (3) ck
Three seasons, six-hour         1.092 (<0.0001)            −0.846 (0.789)               0.041 (0.203)                     2,415
Three seasons, hybrid           1.113 (<0.0001)            0.093 (0.974)                0.035 (0.216)                     2,687
Replication seasons, six-hour 1.196 (<0.0001)              3.095 (0.365)                0.097 (0.001)                     1,453
Replication seasons, hybrid     1.193 (<0.0001)            3.282 (0.220)                0.116 (0.0003)                    1,632
Five seasons, six-hour          1.140 (<0.0001)            0.657 (0.781)                0.062 (0.005)                     3,868
Five seasons, hybrid            1.154 (<0.0001)            1.561 (0.478)                0.068 (0.002)                     4,319
Removed role share: removed reference output in the role divided by the team’s ten-game baseline in that role; its correlation
with ck is −0.53 (three seasons, six-hour). Current-season rows: columns 2–4 are tests (1), (2) and (3); test (1) does not use
the ten-game baseline, so its values repeat the frozen estimates, and Cases counts the test (2) sample, which, unlike test (3),
also needs the opponent’s current-season baseline and so loses the cases whose opponent was playing its first game of the
season. Scale of the coverage null (six-hour cases): standard deviation 0.123 (five seasons 0.132), interquartile range 0.172
(0.182), so ±0.5 points per 0.1 of coverage is ±0.86 (±0.91) points across the interquartile range; coverage correlates −0.28
with the removed minute share and −0.42 with absence value, which correlate 0.93. Role similarity: standard deviation 0.61
(0.58 within cases), so the test (1) coefficient is 0.66 minutes per standard deviation (0.63 per within-case standard deviation
in the paper). NBA Cup finals: 3 games, 6 team-games, 0 cases.




                                                              25
Table S30: Test (3) against the proportional-reallocation benchmark (addendum P24; exploratory).
Columns: ck without the benchmark; ck and the benchmark from one model; ck with the capped bench-
mark. Cells: coefficient (p).

      Sample                      ck alone            ck                   Benchmark              ck , capped           Cases
        Ten-game baseline
      Three seasons, six- 0.054 (0.070)          −0.053 (0.152) 0.207 (<0.0001)                   −0.044 (0.244)        2,441
      hour
      Three seasons, hy- 0.050 (0.086)           −0.050 (0.174) 0.195 (<0.0001)                   −0.047 (0.218)        2,713
      brid
      Five seasons, six- 0.070 (0.002)           −0.002 (0.954) 0.154 (0.0005)                    −0.006 (0.868)        3,907
      hour
      Replication seasons, 0.100 (0.0006) 0.068 (0.082)           0.077 (0.165)                   0.062 (0.178)         1,466
      six-hour
        Healthy baseline: recent games in which the absent core players took part
      Three seasons, six- 0.070 (0.048)          −0.074 (0.071) 0.279 (<0.0001)                   −0.073 (0.090)        2,441
      hour
      Three seasons, hy- 0.065 (0.060)           −0.067 (0.093) 0.262 (<0.0001)                   −0.072 (0.085)        2,713
      brid
      Five seasons, six- 0.091 (0.0007) −0.003 (0.932) 0.201 (<0.0001)                            −0.012 (0.754)        3,907
      hour
        Healthy baseline, cases in which it could be built only
      Three seasons, six- 0.121 (0.034)          −0.105 (0.069) 0.451 (<0.0001)                   −0.109 (0.075)        1,366
      hour
      Three seasons, hy- 0.119 (0.038)           −0.076 (0.182) 0.406 (<0.0001)                   −0.089 (0.111)        1,519
      brid
      Five seasons, six- 0.140 (0.002)           −0.011 (0.819) 0.326 (<0.0001)                   −0.027 (0.590)        2,255
      hour
  Benchmark: the change in the team’s output of the role expected if the absent players’ reference minutes were shared
  among the remaining reference players in proportion to their reference minutes, each at his historical rate, relative to the full
  reference rotation’s output. Capped benchmark: the same with each player’s extra minutes capped at his headroom and the
  excess redistributed. Correlation of ck with the benchmark 0.62 (capped 0.74). Wild bootstrap p for ck with the benchmark,
  three seasons six-hour: 0.170 (ten-game baseline), 0.094 (healthy baseline). The healthy baseline needs at least three such
  games among the last ten; it could be built for 56% of cases (three seasons, six-hour), and the others keep the ten-game
  baseline. With the benchmark’s coefficient fixed at 1 (outcome minus benchmark), ck is −0.462 (p <0.0001): actual role
  output falls far less than the benchmark, most of all where the benchmark predicts large losses, partly because the ten-game
  baseline already includes games without the absent players, whereas the benchmark is measured against the full rotation.
  95% intervals for ck with the benchmark: three seasons, six-hour [−0.126, 0.021]; five seasons, six-hour [−0.064, 0.060];
  replication seasons, six-hour [−0.009, 0.144]. Amendment 2: with the absent players’ share of the role in the reference
  rotation’s output as the control instead, ck is −0.048 (0.153) (three seasons, six-hour, share −0.287 (<0.0001)); −0.001
  (0.980) (five seasons, six-hour, share −0.220 (0.0003)); 0.065 (0.077) (replication seasons, six-hour, share −0.121 (0.106)).
  The P23 control, the same share measured against the ten-game baseline (correlation 0.99), shares its denominator with the
  outcome; with it ck is 0.078 (0.040), and with it and the benchmark together −0.051 (0.219) (three seasons, six-hour).




                                                                26
Table S31: Test (3) by role, and the distribution of ck (addendum P24; exploratory). Slopes of ck by role in
the stacked model. Cells: coefficient (p).

Role            Three seasons      + bench.             Five seasons      + bench.             Replication       + bench.
Three-point     0.053 (0.570)      −0.049 (0.614)       0.089 (0.094)     0.023 (0.696)        0.139 (0.010)     0.109 (0.074)
attempts
Assists         0.065 (0.039)      −0.043 (0.252)       0.072 (0.010)     −0.005 (0.868)       0.089 (0.017)     0.050 (0.217)
Rebounds        0.031 (0.431)      −0.078 (0.073)       0.048 (0.215)     −0.018 (0.682)       0.089 (0.167)     0.064 (0.370)
Equal           0.772              0.745                0.703             0.701                0.592             0.523
slopes, F
test p
  Six-hour samples. Separate regressions by role with the benchmark: three seasons, six-hour: three-point attempts −0.065
  (0.519), assists −0.005 (0.916), rebounds −0.074 (0.171); five seasons, six-hour: three-point attempts −0.001 (0.985),
  assists 0.053 (0.180), rebounds −0.018 (0.737); replication seasons, six-hour: three-point attempts 0.072 (0.194), assists
  0.147 (0.017), rebounds 0.048 (0.545). Share of cases with ck = 1 (three seasons): three-point attempts 80%, assists 69%,
  rebounds 82%. Pooled over roles, ck equals 1 in 77.3% of case-roles; its standard deviation is 0.088 and its 10th percentile
  0.850, so moving from the 10th percentile to 1 changes role output by 0.8% of the baseline (five seasons 1.2%, replication
  2.0%); the outcome’s standard deviation is 18%. Holm-adjusted p for test (3) across the three frozen tests: 0.140 (three
  seasons, six-hour), 0.172 (hybrid), 0.001 (replication), 0.003 (five seasons); the plan required no correction.




Table S32: Clustering by team, by game, and by team and game (addendum P24; exploratory). Cells:
coefficient, standard error (p).

 Test                         Team (30)                        Game                              Team and game
 Clustering, three seasons, six-hour (2,441 cases in 2,013 games; both teams are cases in 428 games)
 Test (1) similarity        1.092, SE 0.180 (<0.0001) 1.092, SE 0.096 (<0.0001) 1.092, SE 0.181 (<0.0001)
 Test (2) coverage          −0.990, SE 2.860 (0.732)      −0.990, SE 2.748 (0.719)     −0.990, SE 2.864 (0.732)
 Test (3) ck                0.054, SE 0.029 (0.070)       0.054, SE 0.027 (0.046)      0.054, SE 0.028 (0.060)
  Two-way clustering follows Cameron, Gelbach and Miller: the team and game covariances minus their intersection, each
  with the CR1 correction; t tests with the number of clusters minus one as degrees of freedom (29 for team and for two-way
  clustering). Five seasons, six-hour: test (2) p 0.818, 0.796, 0.815; test (3) p 0.002, 0.0003, 0.001.




                                                              27
Table S33: Replication without cases involving COVID-19 health and safety protocols, 2021–22 and 2022–
23 (addendum P24; exploratory). Cells: coefficient (p).

     Sample                                            Test (1)              Test (2)             Test (3)             Cases
     Replication seasons, six-hour, all cases          1.196 (<0.0001)       2.423 (0.465)        0.100 (0.0006)       1,466
     Replication seasons, six-hour, without            1.128 (0.0002)        −1.436 (0.758)       0.089 (0.009)        1,289
     protocol cases
     Replication seasons, hybrid, all cases            1.193 (<0.0001)       2.608 (0.292)        0.118 (0.0001)       1,645
     Replication seasons, hybrid, without              1.120 (<0.0001)       −0.508 (0.888)       0.113 (0.001)        1,454
     protocol cases
     Five seasons, six-hour, all cases                 1.140 (<0.0001)       0.502 (0.818)        0.070 (0.002)        3,907
     Five seasons, six-hour, without protocol          1.109 (<0.0001)       −1.240 (0.639)       0.065 (0.011)        3,730
     cases
     Five seasons, hybrid, all cases                   1.154 (<0.0001)       1.347 (0.493)        0.076 (0.0009)       4,358
     Five seasons, hybrid, without protocol            1.123 (<0.0001)       −0.064 (0.979)       0.072 (0.005)        4,167
     cases
  Protocol cases: at least one absent core player listed under “Health and Safety Protocols”, which the parser classes as medical:
  162 (2021–22) and 15 (2022–23) six-hour cases, 139 of them with no other medical absence of a core player; none in 2023–
  24 to 2025–26. Season heterogeneity of test (2), five seasons, six-hour: coverage × replication period 1.262 (0.722), with
  opponent absence value 2.811 (0.387); five season-specific slopes equal: F(4, 29) = 0.96 (p 0.442), with opponent absence
  value 0.84 (p 0.511). Season-specific slopes of test (2) with opponent absence value: 2022 9.036 (0.045), 2023 −3.528
  (0.559), 2024 −0.122 (0.976), 2025 −0.867 (0.827), 2026 1.618 (0.698) (seasons by end year). Test (3): ck × replication
  period 0.009 (0.789); five season-specific slopes equal, p 0.541. Test (2) with healthy baselines (strength measured over
  recent games in which the absent core players took part): −2.195 (0.516) (three seasons, six-hour); cases with a built
  baseline only −6.930 (0.158), 1,366 cases; five seasons 0.152 (0.953). The P3 market regression (margin against the closing
  spread on coverage, 2025–26): −1.284 (0.772), 808 six-hour cases; hybrid −0.446 (0.922).




                                                                  28
Table S34: Test (3): placebo, ceiling, pace, form of the benchmark, joint coverage and absence episodes
(addendum P25; exploratory). Three seasons, six-hour, unless stated. Cells: coefficient (p).

  Specification                                                ck alone             ck with benchmark        Benchmark
   Planned model, real cases (2,441 cases)
  Real absences                                         0.054 (0.070)      −0.053 (0.152)                    0.207 (<0.0001)
   Placebo: all three core players played, each in turn treated as absent (3,522 team-games)
  Placebo                                               0.033 (0.021)      0.023 (0.139)                     0.019 (0.432)
  Real minus placebo (stacked)                          0.022 (0.534)      −0.076 (0.062)                    0.188 (0.0002)
   Ceiling at ck = 1
  Adding 1[ck < 1]                                      0.011 (0.769)      −0.043 (0.291)                    0.215 (<0.0001)
  Case-roles with ck < 1 only (1,661)                   0.027 (0.537)      −0.049 (0.313)                    0.311 (0.003)
  Shortfall (Dk − Sk )+ /Bk instead of ck               −0.069 (0.306) 0.133 (0.077)                         0.209 (<0.0001)
   Outcome normalised for pace and overtime (5.2% of team-games go to overtime)
  Per 240 player minutes                                0.059 (0.046)      −0.047 (0.189)                    0.204 (<0.0001)
  Per 100 possessions; rebounds as share of all re- 0.067 (0.015)          −0.021 (0.539)                    0.170 (0.0007)
  bounds
   Form of the benchmark and measurement error
  Restricted cubic spline of the benchmark              –                  −0.048 (0.227)                    (spline)
  OLS, benchmark from odd-numbered history –                               −0.052 (0.145)                    0.231 (<0.0001)
  games
  IV: odd-game benchmark, even-game instrument          –                  −0.057 (0.139)                    0.242 (0.0001)
  IV: even-game benchmark, odd-game instrument          –                  −0.066 (0.079)                    0.260 (<0.0001)
   Joint coverage θ in place of ck (coefficient of θ )
  Three seasons                                         0.032 (0.129)      0.004 (0.829)                     0.166 (<0.0001)
  Five seasons                                          0.033 (0.073)      0.008 (0.675)                     0.148 (<0.0001)
   Absence episodes (996 episodes; mean length 2.45 cases, median 1)
  Weighted by 1 / episode length                        0.078 (0.038)      −0.045 (0.336)                    0.249 (<0.0001)
  First game of each episode (2,988 case-roles)         0.095 (0.04995) −0.042 (0.411)                       0.282 (<0.0001)
  Team-clustered CR1 errors, t(29). Benchmark as in Table S30. Wild bootstrap p for ck alone: placebo 0.024; per 240 minutes
  0.047; per 100 possessions 0.0146; with the spline 0.246. Placebo: ck equals 1 in 79% of pseudo-case-roles; the removed
  minute share has median 0.19 (real cases 0.22). Real-case slope in the stacked model 0.054 (SE 0.029). Outcome mean
  and, after regressing on the benchmark, removed minute share and role dummies, residual mean by ck : <0.8 (502) −0.011,
  0.008; 0.8–0.9 (487) −0.014, −0.003; 0.9–0.95 (300) −0.003, 0.004; 0.95–1 (372) −0.000, 0.006; = 1 (5,662) 0.007,
  −0.001. Shortfall: Sk is the greedy supply, Bk the full reference rotation’s expected output; its 90th and 99th percentiles are
  0.049 and 0.204. R2 with removed minute share and role dummies: controls only 0.0003, adding ck 0.0010, the benchmark
  0.0047, both 0.0051, the spline 0.0050. Split halves: history games of each player in odd and even positions, rates shrunk
  with 100 pseudo-minutes toward the case mean; correlation of the two benchmarks 0.92, first-stage R2 0.85. θ correlates
  0.62 with ck and equals 1 in 39% of case-roles. Episode: consecutive team games with the same set of absent core players.




                                                               29
Table S35: Tests (1) and (2): substitution partners, distance, overtime, late scratches, all team-games and
fixed effects (addendum P25; exploratory). Three seasons, six-hour. Cells: coefficient (p).

  Specification                                           Key coefficient                Other
    Test (1): minutes per unit [per within-case SD]; 27,897 player-cases with the partner measure
  Similarity alone                                   1.102 (<0.0001) [0.64] –
  Substitution-partner share alone                   –                         7.357 (<0.0001) [1.59]
  Both                                               0.953 (<0.0001) [0.55] 7.126 (<0.0001) [1.54]
  Negative Euclidean distance instead of cosine      0.827 (<0.0001) [0.69] –
  Cases with one removed reference player (353) 0.981 (0.007)                  –
  Minutes scaled to 240 per game                     1.085 (<0.0001)           –
  Without 503 retained player-cases who sat for 1.039 (<0.0001)                –
  a non-coaching reason
  First game of each absence episode (11,283 1.323 (<0.0001)                   –
  player-cases)
    Test (2): final margin; 6,204 team-games in 3,102 games with both report blocks, or 2,441 cases
  All team-games: own absence value × (1 − −0.055 (0.316)                      home rows only −0.026 (0.752)
  coverage)
  All team-games: own absence value                  −0.105 (<0.0001)          home rows only −0.133 (<0.0001)
  Effect of coverage across the case IQR at the 0.30 points                    95% [−0.30, 0.90]
  median case absence value
  Cases, 89 team-season fixed effects                −2.457 (0.423)            lost value −0.277 (0.002)
  Cases, weighted by 1 / episode length              −0.963 (0.802)            –
  Cases, first game of each episode (996)            −5.640 (0.198)            –
  Substitution-partner share: for each removed reference player i and retained player j, the share of possessions with i on
  the bench in which j was on court, over those of the team’s last 20 games before the cutoff in which i played (stint data
  of addendum P16), averaged over removed players with weights bi ; available for 99.2% of player-cases; correlation with
  similarity 0.07. Late scratches: retained players listed in the box score as not playing for a reason other than a coach’s
  decision. All team-games: margin on own and opponent absence value, each interacted with one minus coverage (coverage
  set to 1 when no reference player is Out), strength difference, home and rest difference; each game enters twice, so errors are
  clustered by team and by game. Median absence value of a case 31.1; case interquartile range of coverage 0.175.




Table S36: The three frozen tests by season, removed reference minutes, Doubtful core players and the
construct validity of coverage (addendum P25; exploratory). Six-hour cutoff. Cells: coefficient (p).

     Season        Test (1)              Test (2)             Test (3)           Cases     Removed min., median (IQR)
     2023–24       1.557 (0.0004)        4.237 (0.387)        0.103 (0.082)      630                      51.7 (40.6–71.9)
     2024–25       1.134 (0.0002)        −3.471 (0.459)       0.047 (0.364)      753                      55.6 (42.1–74.8)
     2025–26       0.800 (<0.0001)       −2.153 (0.652)       0.032 (0.403)      1,058                    52.5 (38.6–69.0)
  Single-season test (1) uses the three-season standardisation of role rates. Doubtful: 211 core-player entries listed Doubtful
  at the cutoff in 199 team-games; 97.6% of these players did not play; treating Doubtful as Out would add 138 cases (134
  in which the player sat). Construct validity: the share of the absent players’ expected output of a role Dk that the retained
  players actually added (their in-game output minus reference minutes times historical rate) has median 0.85 (interquartile
  range 0.36 to 1.39); winsorised at 1% and 99% and regressed with role dummies on ck 0.916 (<0.0001), correlation 0.08;
  on θ 0.656 (0.0002), correlation 0.08; on the benchmark 1.857 (<0.0001), correlation 0.13. Decomposition, all roles: the
  retained players’ added output equals 85% of ∑ Dk ; extra minutes at historical rates contribute 81% and changes in per-
  minute rates 4% (three-point attempts 89%, 83% and 6%; assists 82%, 75% and 7%; rebounds 84%, 85% and −1%).




                                                               30
Table S37: Test (3) with role rates that do not overlap the ten-game baseline (addendum P26; exploratory).
Six-hour cutoff. Cells: coefficient (p).

   Specification                                              ck alone            ck with benchmark         Benchmark
    Three seasons, six-hour (2,441 cases, 7,323 case-roles)
   Rates from the last 20 games (frozen)                0.054 (0.070)  −0.053 (0.152)                       0.207 (<0.0001)
   Rates from games 11–30                               0.061 (0.054)  −0.057 (0.138)                       0.231 (<0.0001)
   Rates from games 11–30, frozen benchmark             –              −0.033 (0.379)                       0.193 (<0.0001)
    Five seasons, six-hour (3,907 cases, 11,721 case-roles)
   Rates from the last 20 games (frozen)                0.070 (0.002)  −0.002 (0.954)                       0.154 (0.0005)
   Rates from games 11–30                               0.065 (0.002)  −0.016 (0.568)                       0.172 (0.0001)
   Rates from games 11–30, frozen benchmark             –              −0.004 (0.885)                       0.155 (0.0002)
    Replication seasons, six-hour (1,466 cases, 4,398 case-roles)
   Rates from the last 20 games (frozen)                0.100 (0.0006) 0.068 (0.082)                        0.077 (0.165)
   Rates from games 11–30                               0.080 (0.005)  0.042 (0.267)                        0.086 (0.107)
   Rates from games 11–30, frozen benchmark             –              0.041 (0.266)                        0.098 (0.063)
    Placebo, rates from games 11–30 (3,522 team-games, 31,698 pseudo-case-roles)
   Placebo                                              0.037 (0.012)  0.022 (0.192)                        0.028 (0.280)
   Real minus placebo (stacked)                         0.025 (0.486)  −0.079 (0.057)                       0.202 (0.0002)
  Role rates from each player’s games 11 to 30 with positive minutes before the cutoff (365 days, any team), shrunk with 100
  pseudo-minutes toward the leave-one-out rate of roster players with games in the same window; players without such games
  take that rate (11.5% of roster players, three seasons). Reference minutes, capacity, the removed players and the outcome
  (role total over the team’s mean in its last ten games, minus one) are unchanged; ck and the benchmark are recomputed.
  Team-clustered CR1 errors, t(29). Wild bootstrap p, three seasons: frozen 0.079 (a different seed from Table S9); games
  11–30 0.058, with the benchmark 0.153; placebo 0.016. Correlation of old and new ck 0.93, of the benchmarks 0.96;
  ck = 1 in 75.4% of case-roles (frozen 77.3%). Recent (games 1–10) minus older (games 11–30) raw per-minute rates, mean
  (SE): retained players (27,598) three-point attempts 0.0030 (SE 0.0002); assists 0.0027 (SE 0.0002); rebounds −0.0005 (SE
  0.0003); removed players (7,312) three-point attempts 0.0015 (SE 0.0004); assists 0.0019 (SE 0.0004); rebounds −0.0004
  (SE 0.0005). Joint coverage θ with rates from games 11–30 correlates 0.92 with the frozen θ and equals 1 in 36.1% of cases;
  test (2) with it −1.539 (0.593), frozen on the same cases −0.990 (0.732).




Table S38: Test (1) by season and its linear trend (addendum P26; exploratory). Six-hour cutoff. Cells:
coefficient (p) unless stated.

             Season                 3 seasons             5 seasons             SD     Removed       Core     Min.
             2021–22                –                     1.366 (0.002)       0.56          3.28     1.26     55.1
             2022–23                –                     1.060 (0.001)       0.56          2.65     1.22     49.1
             2023–24                1.557 (0.0004)        1.621 (0.0003)      0.57          2.96     1.19     51.7
             2024–25                1.134 (0.0002)        1.164 (0.0001)      0.59          3.23     1.30     55.6
             2025–26                0.800 (<0.0001)       0.781 (0.0002)      0.58          2.94     1.21     52.5
             Trend per season       −0.357 (0.060)        −0.112 (0.309)         –             –        –        –
  Case fixed effects with similarity × season (linear, centred), reference minutes and headroom; 28,118 player-cases in three
  seasons and 44,701 in five. The five-season build standardises role rates over five seasons, so its coefficients for 2023–24
  to 2025–26 differ slightly from the three-season build; cases and minutes are identical. 3 seasons, 5 seasons: coefficient of
  similarity in the three- and five-season builds. SD: within-case standard deviation of similarity. Composition columns (five-
  season build): removed reference players per case (Removed), core players ruled Out per case (Core) and median removed
  reference minutes (Min.).




                                                              31
Table S39: Power of a single-season prospective test at the standard errors of single past seasons (addendum
P26). Six-hour cutoff.

        Season      H3-B SE       Power      MDE       MDE/SESOI         Test (2) SE     Power      MDE       MDE/SESOI
        2023–24         0.081       12%      0.235                3.6            0.48      17%       1.40                2.8
        2024–25         0.071       14%      0.206                3.2            0.46      18%       1.34                2.7
        2025–26         0.045       29%      0.130                2.0            0.47      18%       1.37                2.7
  H3-B: ck with the benchmark as a control; smallest effect size of interest (SESOI) 0.065. Test (2): coverage and margin,
  SE and MDE in points per 0.1 of coverage; SESOI 0.5 points per 0.1. Two-sided 5% tests with t(29); power from the
  noncentral t distribution; minimum detectable effect (MDE) at 80% power, (t0.975 + t0.80 )×SE. Standard errors from the
  frozen specifications fitted to each season alone (role rates from the last 20 games).




Table S40: The frozen tests by the composition of the removed set (addendum P27; exploratory). Three
seasons, six-hour. Cells: coefficient (p).

Cases                   n    Test (1)                Test (2)           Test (3)           ck with bench.        Benchmark
All                2,441     1.092 (<0.0001)         −0.990 (0.732)     0.054 (0.070)      −0.053 (0.152)        0.207 (<0.0001)
Core only            406     0.963 (0.011)           −3.807 (0.469)     0.092 (0.263)      −0.067 (0.558)        0.364 (0.029)
New                   94     1.917 (<0.0001)         −0.741 (0.956)     0.183 (0.056)      −0.118 (0.421)        0.651 (0.003)
Core    only,         67     1.528 (0.002)           4.057 (0.813)      0.190 (0.144)      −0.054 (0.791)        0.595 (0.185)
new
Clean base-           37     1.573 (0.033)           31.972 (0.039)     0.319 (0.022)      −0.011 (0.970)        0.786 (0.161)
line
  Rows: all cases; only core players removed; every removed player had played the team’s previous game (new); both; every
  removed player had played each of the team’s last ten games (clean baseline). Removed players are the reference players
  ruled Out at the cutoff (on average 3.0 per case), including players still supported after weeks out. Shares of cases: only core
  players removed 16.6%; every removed player had positive minutes in the team’s previous game 3.9%; every removed player
  had positive minutes in each of the team’s last ten games 1.5%, so in 98.5% of cases the ten-game baseline includes a game
  in which a removed player did not play. In 59.2% of cases the same set of core players was also out in the team’s previous
  game (episode definition of addendum P25). Test (1): minutes per unit of similarity, case fixed effects; test (2): margin per
  unit of coverage; test (3): role output per unit of ck , and with the benchmark.




                                                                32
Table S41: Test (3) per opportunity and with both regressors instrumented; team efficiency (addendum P27;
exploratory). Three seasons, six-hour. Cells: coefficient (p).

     Specification                                         ck alone            ck with benchmark        Benchmark
       Outcome per opportunity (3PA/FGA, AST/FGM, rebound share) relative to the ten-game mean
     All roles                                       0.038 (0.126)    −0.042 (0.183)   0.156 (0.0002)
     Three-point attempts per field-goal attempt     0.140 (0.094)    0.008 (0.921)    0.266 (0.0004)
     Assists per made field goal                     −0.004 (0.874) 0.011 (0.781)      −0.030 (0.568)
     Share of all rebounds                           0.040 (0.348)    −0.066 (0.234)   0.197 (0.0001)
     Volume outcome, same rows (frozen defini- –                      −0.053 (0.152)   0.207 (<0.0001)
     tion)
       Split halves: ck and the benchmark both instrumented (7,323 case-roles)
     2SLS: odd-game ck and benchmark, even- –                         −0.059 (0.182)   0.239 (<0.0001)
     game instruments
     OLS with odd-game measures                      –                −0.064 (0.091)   0.240 (<0.0001)
     2SLS: even-game ck and benchmark, odd- –                         −0.073 (0.102)   0.260 (<0.0001)
     game instruments
     OLS with even-game measures                     –                −0.049 (0.199)   0.211 (<0.0001)
  Team-clustered CR1 errors, t(29); wild bootstrap p for ck alone per opportunity 0.127. By role: one role at a time with a
  constant. Split halves as in Table S34, with Sk and ck also computed from each half; first-stage R2 for ck and the benchmark
  0.78 and 0.84; correlations of the halves 0.88 (ck ) and 0.92 (benchmark). Team efficiency (cases): change from the ten-game
  mean regressed on coverage, removed minute share, lost value, strength, home and rest; coverage coefficient for true shooting
  0.016 (0.160), three-point percentage 0.015 (0.323), turnovers per possession −0.002 (0.801).




                                                              33
Table S42: Test (2) intervals and the closing spread, selection into absence, and the construct validity of
coverage in levels (addendum P27; exploratory). Six-hour cutoff. Cells: coefficient (p) unless stated.

  Specification                                 Key estimate                              Other
   Test (2): 90% intervals per 0.1 of coverage, CR1 and by inverting the wild bootstrap
  Three seasons, frozen                     −0.10; CR1 [−0.58, 0.39]           [−0.60, 0.41]; ±0.5 not met,
                                                                               ±0.25 not met
  Three seasons, with opponent ab- −0.05; CR1 [−0.58, 0.48]                    [−0.60, 0.53]; ±0.5 not met,
  sence value                                                                  ±0.25 not met
  Five seasons, frozen                      0.05; CR1 [−0.32, 0.42]            [−0.33, 0.43]; ±0.5 met, ±0.25
                                                                               not met
  Five seasons, with opponent absence 0.18; CR1 [−0.24, 0.59]                  [−0.26, 0.62]; ±0.5 not met,
  value                                                                        ±0.25 not met
   Test (2) with the closing spread (seasons with lines: 2021–22 764, 2022–23 702, 2025–26 808 cases)
  Frozen model, same cases                  0.787 (0.793)                      lost value −0.104 (0.105)
  Spread in place of the strength differ- −1.091 (0.700)                       spread −1.003 (<0.0001)
  ence
  Margin against the spread as outcome −1.086 (0.701)                          lost value −0.045 (0.510)
   Selection: core players listed Questionable or Doubtful (1,886 entries, 89% Questionable); outcome: sat out
  Coverage without the player               0.143 (0.120); 1.9 pp per SD       Questionable only 0.151 (0.129)
  Mean ck without the player                0.350 (0.114); 2.0 pp per SD       Questionable only 0.396 (0.117)
  Mean benchmark without the player         0.698 (0.040); 2.4 pp per SD       Questionable only 0.703 (0.054)
   Construct validity in levels: retained players’ added output of a role
  On Sk and Dk                              Sk 0.300 (<0.0001)                 Dk 0.454 (<0.0001); R2 0.194
  On min(Sk , Dk ) and Dk                   0.334 (0.004)                      Dk 0.365 (0.001); R2 0.187
  On Dk only                                –                                  Dk 0.633 (<0.0001); R2 0.183
  Wild bootstrap intervals: the set of values β0 on a grid of 0.01 per 0.1 for which the restricted wild bootstrap (Webb weights,
  9,999 draws) does not reject β = β0 at 10%. Closing spread: the team’s closing line (negative for favourites), available
  for 2021–22, 2022–23 and most of 2025–26 only. Selection: linear probability model with Doubtful status, the player’s
  reference minutes, the minutes already removed, strength, home, rest and season dummies; the key variable is computed as
  if the player were ruled Out (with any reference players actually Out); sat-out rates 38% (Questionable) and 98% (Doubtful).
  Construct validity: added output as in Table S36 (actual output minus reference minutes times historical rate, summed over
  retained players), Sk the greedy supply, Dk the demand; role dummies, team-clustered errors, 7,323 case-roles.




                                                               34
Table S43: The placebo slope of test (3), and test (1) standardisation and power (addendum P28; ex-
ploratory). Three seasons, six-hour. Cells: coefficient (p) unless stated.

Specification                                  Real cases                              Placebo
  Test (3), ck alone: numerical inputs from games 11–30, frozen sample (P28-A), against the frozen inputs
Frozen inputs                                   0.054 (0.070)                           0.033 (0.021)
Inputs from games 11–30                         0.040 (0.085; wild 0.087)               0.018 (0.153; wild 0.170)
Inputs from games 11–30, unchanged ro- 0.080 (0.083)                                    0.011 (0.504)
tation / unchanged top three (different re-
strictions, not comparable; see Table S44)
Inputs from games 11–30, five seasons           0.047 (0.003)                           –
Real minus placebo, inputs from games 0.023 (SE 0.027; 0.416)                           –
11–30
  ck with the benchmark (benchmark coefficient in brackets)
Frozen inputs                                   −0.053 (0.152) [0.207]                  0.023 (0.139) [0.019]
Inputs from games 11–30                         −0.039 (0.149) [0.194]                  −0.000 (0.977) [0.045]
Inputs from games 11–30, benchmark −0.066 (0.053) [0.180]                               −0.001 (0.962) [0.038]
capped at headroom
  Decomposition of ck (frozen inputs; ck coefficient unless stated)
D1: qk = Dk /Bk ; sk = Sk /Bk ; ceiling indi- −0.303 (<0.0001);             −0.079 0.009 (0.768); 0.048 (0.390);
cator (no ck )                                  (0.151); −0.006 (0.412)                 0.007 (0.015)
D2: with qk                                     −0.048 (0.153)                          0.027 (0.082)
D3: with baseline exposure of retained 0.048 (0.106); 0.067 (0.038)                     0.024 (0.092); 0.068 (0.012)
players eret (its coefficient second)
D4: with the team’s baseline dip by role        0.079 (0.019)                           0.039 (0.022)
D5: D3 and D4 together                          0.073 (0.026)                           0.029 (0.073)
Correlation of ck with eret / with the base- 0.18 / 0.06                                0.15 / 0.02
line dip
  Analysis of covariance: log role total on ck with the log ten-game baseline by role
Frozen inputs; with benchmark                   0.060 (0.053); −0.085 (0.025)           0.028 (0.115); 0.001 (0.952)
Inputs from games 11–30; with bench- 0.048 (0.043); −0.052 (0.048)                      0.022 (0.122); −0.001 (0.964)
mark
  Benchmark and the absent players’ role share qk : partial correlation given the removed minute share and role
Frozen / games 11–30 inputs                     −0.982 / −0.978                         −0.994 / −0.992
  Test (1): standardisation of the role rates (three seasons, six-hour; similarity coefficient)
Moments of the three seasons (frozen)           1.092 (<0.0001)                         –
Moments of the previous season                  1.168 (<0.0001)                         corr. with frozen similarity 0.984
Moments of the replication seasons              1.142 (<0.0001)                         corr. with frozen similarity 0.951
  Test (1) in one season: power at the season’s standard error (two-sided 5%, t(29))
2021–22 (SE 0.39)                               power 0.77 at 1.10; 0.48 at 0.78        MDE (80%) 1.14
2022–23 (SE 0.29)                               power 0.95 at 1.10; 0.73 at 0.78        MDE (80%) 0.85
2023–24 (SE 0.40)                               power 0.77 at 1.10; 0.48 at 0.78        MDE (80%) 1.15
2024–25 (SE 0.27)                               power 0.98 at 1.10; 0.81 at 0.78        MDE (80%) 0.77
2025–26 (SE 0.18)                               power 1.00 at 1.10; 0.99 at 0.78        MDE (80%) 0.52




                                                            35
Note to Table S43. Inputs from games 11–30: mean minutes, capacities (90th percentile of per-game minutes, at most 40),
the support thresholds (5 games, 100 minutes) and role rates from each player’s positive-minute games 11 to 30 before the
cutoff (within 365 days, any team); reference minutes recomputed under the 240-minute budget; frozen support flags, core
identities, removal flags and outcome. With games 1–20 the construction reproduces the frozen reference minutes, capacities
and rates (largest difference 7e-15). Placebo: the 3,522 team-games in which all three core players played, each core player
treated in turn as absent (10,508 pseudo-absences with the new inputs); unchanged top three: the three players with the
largest new mean minutes are the frozen core (1,847 team-games). Unchanged rotation: every frozen reference player meets
the new thresholds (852 cases). eret : expected role output of retained reference players weighted by the share of the team’s
last ten games each missed, relative to Bk ; baseline dip: log of the ten-game mean over the mean of the team’s games 11 to
30. Wild bootstrap: Webb weights, 9,999 draws. Test (1) power: noncentral t at the clustered standard error of the season’s
estimate in Table S38 (standard errors as listed here), for true coefficients 1.10 (three seasons pooled) and 0.78 (2025–26),
the estimates on the earlier build fixed in the plan (final data: 1.09 and 0.80).




                                                            36
Table S44: Test (3) and its placebo under the same restrictions, and test (1) by the composition of the
removed set (addendum P29; exploratory). Six-hour cutoff. Cells: coefficient (p) unless stated.

Specification                             Real cases                     Placebo                         Real minus placebo
  Rotation unchanged (852 cases; 1,352 placebo team-games)
Inputs from games 11–30: ck alone 0.080 (0.083;        wild              0.048 (0.011;       wild        0.033  (SE         0.049;
                                     0.086)                              0.009)                          0.516)
Inputs from games 11–30: ck with −0.021 (0.747) [0.213]                  0.014 (0.549) [0.068]           −0.035 (SE         0.065;
the benchmark                                                                                            0.591)
Frozen inputs: ck alone              0.083 (0.058)                       0.047 (0.010)                   0.036  (SE         0.049;
                                                                                                         0.466)
Frozen inputs: ck with the bench- −0.021 (0.727) [0.207]      0.018 (0.359) [0.055]                      −0.039 (SE         0.058;
mark                                                                                                     0.503)
  Top three unchanged (1,372 cases; 1,847 placebo team-games)
Inputs from games 11–30: ck alone 0.047 (0.136)               0.011 (0.504)                              0.036  (SE         0.035;
                                                                                                         0.316)
Inputs from games 11–30: ck with          −0.030 (0.416) [0.188]         −0.015 (0.518) [0.066]          −0.015 (SE         0.042;
the benchmark                                                                                            0.733)
Frozen inputs: ck alone                   0.023 (0.538)                  0.038 (0.013)                   −0.015 (SE         0.040;
                                                                                                         0.712)
Frozen inputs: ck with the bench- −0.105 (0.032) [0.255]                 0.020 (0.333) [0.035]           −0.125 (SE         0.046;
mark                                                                                                     0.011)
  Both (487 cases; 725 placebo team-games)
Inputs from games 11–30: ck alone 0.055 (0.320)                          0.042 (0.036)           0.014   (SE  0.059;
                                                                                                 0.821)
Inputs from games 11–30: ck with −0.060 (0.499) [0.243]              −0.030 (0.277) [0.149]      −0.031 (SE 0.088;
the benchmark                                                                                    0.728)
Frozen inputs: ck alone                 0.041 (0.419)                0.058 (0.003)               −0.017 (SE 0.055;
                                                                                                 0.752)
Frozen inputs: ck with the bench- −0.085 (0.255) [0.248]             −0.001 (0.978) [0.116]      −0.084 (SE 0.068;
mark                                                                                             0.224)
  Test (1): similarity slope interacted with the composition of the removed set (frozen, three seasons)
New absences (every removed other                 cases    1.061 in group 1.876 (SE interaction                0.815
player played the previous game) (<0.0001)                           0.368)                      (0.012)
(94 cases)
Only core players removed (406 other              cases    1.124 in group 0.945 (SE interaction              −0.179
cases)                                  (<0.0001)                    0.356)                      (0.645)
  In the last panel the cells are the slope in the other cases, the slope in the group and the interaction, not the quantities of
  the column heads. Rotation unchanged: every frozen reference player meets the support thresholds in games 11–30, so
  the reference rotation has the same members as in the frozen build. Top three unchanged: the three reference players with
  the largest mean minutes in games 11–30 are the frozen core. The same restriction is applied to real cases and to placebo
  team-games; inputs as in Table S43. Real minus placebo: interaction of ck with a real-case indicator in the stacked regression
  of Table S34 (separate role intercepts and removed minute share slopes); with the benchmark, the difference is that of the
  ck coefficients, and the benchmark coefficient is in brackets. Test (1): case fixed effects, reference minutes and headroom
  as controls; the interaction is the difference between the slope in the group and in the other cases. Wild bootstrap: Webb
  weights, 9,999 draws.




                                                               37
Table S45: Test (1) with position, height and substitution-partner share controlled jointly on a common
sample (addenda P30 to P32; exploratory). Three seasons, six-hour. Cells: coefficient (p).

Model                                   Similarity           Same position         Height gap            Sub.-partner
                                                                                                         share
  Common sample: 27,896 player-cases with all controls (99% of the frozen sample)
Similarity only                     1.102               –                –                  –
                                    (<0.0001)
Similarity, same position, height 0.793 (0.0002)        0.318 (0.163)    −0.148 (0.002)     6.952
gap and substitution-partner                                                                (<0.0001)
share
Similarity only; previous-season 1.177                  –                –                  –
standardisation                     (<0.0001)
Joint controls; previous-season 0.868 (0.0001)          0.291 (0.204)    −0.147 (0.002)     6.930
standardisation                                                                             (<0.0001)
  Substitution-partner share from validated stint games only (addendum P31): 27,750 player-cases in 2,411 cases
Similarity only                     1.108               –                –                  –
                                    (<0.0001)
Similarity, same position, height 0.789 (0.0002)        0.317 (0.168)    −0.155 (0.001)     6.641
gap and substitution-partner                                                                (<0.0001)
share
Similarity only; previous-season 1.182                  –                –                  –
standardisation                     (<0.0001)
Joint controls; previous-season 0.862 (0.0001)          0.289 (0.209)    −0.154 (0.001)     6.618
standardisation                                                                             (<0.0001)
  Case fixed effects; reference minutes and headroom as controls; team-clustered errors, t(29). Share of the similarity coef-
  ficient retained with the joint controls: 72% (analysed-season standardisation) and 74% (previous-season standardisation);
  with the validated-game share, 71% and 73%. Size (addendum P32): one within-case standard deviation of similarity (0.58)
  goes with 0.64 [0.42, 0.86] more minutes with similarity alone and 0.46 [0.24, 0.68] with the joint controls (95% intervals);
  with the validated-game share, 0.64 [0.43, 0.86] and 0.46 [0.24, 0.68]. Same position: the player’s position group equals
  the position group with the largest total reference minutes among the removed players; height gap: absolute difference from
  the removed players’ reference-minute-weighted mean height; substitution-partner share as in Table S35. Previous-season
  standardisation: role rates standardised with the mean and standard deviation of the previous season’s case players.




                                                              38
Table S46: What the shared minutes budget adds, how the scenario compares with the actual rotation, and
the dates of the P28 inputs (addendum P30; descriptive). Three seasons, six-hour.

Quantity                                                        Value
  Shared-budget gap G = U − θ , U = min{1, H/L, mink ck } (2,441 cases; violations θ > U: 0)
Mean; median; 90th, 95th, 99th percentile; maximum 0.014; 0.000; 0.055, 0.082, 0.136; 0.199
Share of cases with G > 10−6 / > 0.01 / > 0.05            36.9% / 26.5% / 11.6%
Among cases with θ < 1: share with G > 0.01               43.6% (of 60.8% of cases)
U set by: assists / rebounds / three-point attempts / 25.9 / 13.1 / 11.1 / 0.1 / 49.8%
minutes / U = 1
Example: PHI, 2024-02-25 (2 removed)                      θ 0.75; U 0.95; c (3PA, AST, REB) 1.00, 1.00, 0.95; H/L
                                                          5.7
Example: PHI, 2024-02-27 (2 removed)                      θ 0.76; U 0.94; c (3PA, AST, REB) 1.00, 1.00, 0.94; H/L
                                                          5.7
  The scenario against the actual rotation (retained reference players in cases)
Played fewer minutes than reference / more than ca- 29.5% / 15.4% / 15.5% of 28,118
pacity / did not play
Minutes of players outside the reference rotation: 9.3; 4.6 (medians 0 and 0)
mean per case; per team-game with no core player
ruled Out (4,177)
The same, pooled over cases, as a share of the removed 16.2%
reference minutes
  Dates of the inputs from games 11–30 (Table S43)
Real cases: latest input game not earlier than the earli- 23 of 32,866 player-team-games (0.07%); all involve
est baseline game                                         games for another team
Placebo team-games: latest input game not earlier than 20 of 46,541 player-team-games (0.04%); all involve
the earliest baseline game                                games for another team
  H: total headroom of the retained reference players; L: removed reference minutes; ck : single-dimension coverage; θ :
  coverage. Because one set of extra minutes that restores the share θ of every demand also satisfies each constraint separately,
  θ ≤ U; G measures how much the shared budget lowers coverage below the separate bounds. Here θ < 1 means below 1
  by more than 10−9 ; Table S2 counts a case as reaching 1 when coverage is at least 0.9999, so the two shares do not sum
  exactly to 100%. Baseline games: the team’s previous ten games, which define the outcome baseline of test (3); games for
  another team: the player changed teams within the window, so his input games are not games of the team whose baseline
  they overlap in time.




                                                               39
Table S47: Validation of the stint data and the analyses that use it; construct check with a free coefficient
(addendum P30; exploratory).

Season                                     Score exact      Within 4 points (each team)         Minutes consistent       All checks
 Validation of the stint reconstruction, by season (share of games)
2019–20 (1,059 games)                        44.7%                                   82.3%                    79.4%           38.1%
2020–21 (1,080 games)                        47.3%                                   91.5%                    98.8%           46.8%
2021–22 (1,230 games)                        40.6%                                   90.3%                    99.2%           40.4%
2022–23 (1,230 games)                        44.4%                                   92.8%                    98.8%           44.1%
2023–24 (1,231 games)                        50.4%                                   90.6%                    98.5%           50.2%
2024–25 (1,231 games)                        88.5%                                   98.8%                    99.1%           88.0%
2025–26 (1,198 games)                        86.1%                                   98.7%                    99.0%           85.8%
All seasons                                  57.8%                                   92.3%                    96.4%           56.6%
  All seasons: shares of the 8,259 games of the season rows, those with reconstructed stints (8,292 games in all; note to
  Table S24). Score: sum of stint points against each team’s final score (within 4 points: both teams’ errors at most four
  points); minutes consistent: every player with at least 10 box-score minutes has an on-court possession share within 0.10 of
  his share of the game’s minutes, and no player without box-score minutes appears in 3 or more possessions; every stint has
  five players per side in all games. On the validated games: test (1) with similarity and substitution-partner share, similarity
  0.955 (<0.0001), SE 0.178, share 6.795 (<0.0001), SE 0.581 (all games 0.953 (<0.0001), SE 0.178, and 7.126 (<0.0001),
  SE 0.547); 27,751 player-cases in 2,411 cases (all games 27,897 in 2,423). The share keeps its window, the team’s last
  20 games before the cutoff; games that fail validation are dropped from the window, not replaced by earlier games; the
  filter applies only to the games from which the share is computed, not to the cases explained, and a retained player whose
  absent teammates have no validated game left in the window has no share and leaves the sample. Stint-level RAPM refitted
  on validated games only (correlation with the full fit 0.78 to 0.93); test (2) with it in place of lost value: coverage 1.835
  (0.452) over three seasons and 2.523 (0.197) over five (full fit 1.788 (0.485) and 2.777 (0.159)). Construct check with a
  free coefficient on reference output (uses no stint data): retained players’ role output regressed on their reference output Ek ,
  demand Dk and supply, with role dummies. Without supply, R2 0.5582; with min(Sk , Dk ): coefficient 0.346 (0.002), Ek
  0.692, R2 0.5603; with Sk : coefficient 0.298 (<0.0001), Ek 0.695, R2 0.5641.




                                                                40
S3     Further results
The tables below report the exploratory analyses added after the main results were known (addenda P33
to P50) and the worked example of Section 3 of the paper. Each caption names its addendum and states
whether its reading was fixed in a plan before it was run.

Table S48: Test (1) with player fixed effects, and single-absence cases against a like-for-like placebo (ad-
dendum P33; exploratory). Six-hour cutoff. Cells: coefficient of similarity (SE), p.

Model                                         Similarity                     95% interval       p (WCR)         Rows       Cases
 Primary sample, 2023–24 to 2025–26
Case fixed effects (the planned test)  1.092 (0.180), <0.0001 [0.72, 1.46]                     –               28,118      2,441
+ player × team × season fixed effects 1.383 (0.211), <0.0001 [0.95, 1.81]                     ≤0.0001         28,118      2,441
+ player × team fixed effects          1.256 (0.197), <0.0001 [0.85, 1.66]                     –               28,118      2,441
 Replication seasons, 2021–22 and 2022–23
Case fixed effects (the planned test)  1.196 (0.256), <0.0001 [0.67, 1.72]                     –               16,583      1,466
+ player × team × season fixed effects 1.773 (0.247), <0.0001 [1.27, 2.28]                     ≤0.0001         16,583      1,466
+ player × team fixed effects          1.675 (0.243), <0.0001 [1.18, 2.17]                     –               16,583      1,466
 Cases with one removed reference player against the single-core placebo
Real cases                             0.981 (0.337), 0.007        [0.29, 1.67]                –               4,524         353
Placebo, all 3,522 team-games          −0.156 (0.087), 0.084       [−0.33, 0.02]               –             123,306      10,566
   real minus placebo                  1.137 (0.367), 0.004        [0.39, 1.89]                0.0059        127,830      10,919
Placebo, 846 team-games, no reference −0.071 (0.097), 0.468        [−0.27, 0.13]               –              31,893       2,538
player ruled Out
   real minus placebo                  1.052 (0.349), 0.005        [0.34, 1.77]                0.0067          36,417      2,891
  Outcome, similarity, reference minutes and headroom as in test (1); team-clustered CR1 errors, t(29); the fixed effects are
  removed by alternating projections and, being nested in the team clusters, are not counted in the small-sample factor. Primary
  sample: 1,677 player-team-seasons of 678 players, with a median of 14 cases each (79 appear once and do not contribute);
  the standard deviation of similarity net of case effects and controls is 0.58, and 0.42 net of player-team-season effects as
  well (53% of the variance). Replication seasons: 1,092 player-team-seasons, 0.56 and 0.40 (50%). One within-case standard
  deviation of similarity goes with 0.63 minutes under case effects and 0.80 with player-team-season effects in the primary
  sample. WCR: wild cluster restricted bootstrap with Rademacher weights, 9,999 draws. Placebo: team-games with a report
  block in which no core player was ruled Out and all three played; each core player in turn is treated as absent, so a placebo
  case is a team-game and a pseudo-absent player. Real minus placebo: stacked model with case fixed effects in which
  similarity, reference minutes and headroom are each interacted with an indicator for real cases. Minutes are freed in real
  cases and not in the placebo, and the games differ.




                                                               41
Table S49: Games without and with the absent player (addendum P34, part A; exploratory). Cells: coeffi-
cient of similarity (SE), p.

  Model                                                                  Similarity                                 95% interval                p (WCR)              Pairs / rows
   Primary sample, 2023–24 to 2025–26: pairs of a teammate and an absent core player
  Unweighted, with the two controls (main) 1.542 (0.190), <0.0001 [1.15, 1.93]       ≤0.0001                                                                                   2,653
  Weighted by the number of games           1.418 (0.209), <0.0001 [0.99, 1.84]      –                                                                                         2,653
  Without the controls                      1.461 (0.204), <0.0001 [1.04, 1.88]      –                                                                                         2,653
  He is the only core player out; no core 1.301 (0.261), <0.0001 [0.77, 1.83]        –                                                                                         1,757
  player out in the games with him
   Primary sample, 2023–24 to 2025–26: team-games, team-game and player effects
  Similarity × case                         1.385 (0.215), <0.0001 [0.95, 1.82]      ≤0.0001                                                                                 81,178
  + case × usual minutes                    1.406 (0.210), <0.0001 [0.98, 1.84]      –                                                                                       80,064
  + reference minutes, case × reference 1.403 (0.201), <0.0001 [0.99, 1.81]          –                                                                                       81,178
  minutes, case × headroom
  Player’s mean similarity over his cases × 1.339 (0.384), 0.002     [0.55, 2.12]    –                                                                                       81,178
  case
  Deviation from that mean × case           1.405 (0.216), <0.0001 [0.96, 1.85]      –                                                                                       81,178
   Replication seasons, 2021–22 and 2022–23: pairs of a teammate and an absent core player
  Unweighted, with the two controls (main) 1.413 (0.292), <0.0001 [0.82, 2.01]       ≤0.0001                                                                                   1,661
  Weighted by the number of games           1.415 (0.254), <0.0001 [0.90, 1.93]      –                                                                                         1,661
  Without the controls                      1.420 (0.348), 0.0003    [0.71, 2.13]    –                                                                                         1,661
  He is the only core player out; no core 1.391 (0.328), 0.0002      [0.72, 2.06]    –                                                                                         1,078
  player out in the games with him
   Replication seasons, 2021–22 and 2022–23: team-games, team-game and player effects
  Similarity × case                         1.654 (0.261), <0.0001 [1.12, 2.19]      ≤0.0001                                                                                 52,980
  + case × usual minutes                    1.728 (0.234), <0.0001 [1.25, 2.21]      –                                                                                       52,487
  + reference minutes, case × reference 1.703 (0.227), <0.0001 [1.24, 2.17]          –                                                                                       52,980
  minutes, case × headroom
  Player’s mean similarity over his cases × 1.443 (0.460), 0.004     [0.50, 2.38]    –                                                                                       52,980
  case
  Deviation from that mean × case           1.771 (0.260), <0.0001 [1.24, 2.30]      –                                                                                       52,980




                             A2: components + own-coordinate main effects                                           A3: A2 + position pairings, height gap, partner share, status
                             equal-coefficient test, WCR p: main 0.08, earlier 0.20                                 equal-coefficient test, WCR p: main 0.17, earlier 0.67

           3PA per minute                                                                         3PA per minute


        Assists per minute                                                                     Assists per minute


      Rebounds per minute                                                                  Rebounds per minute

                             0.5      0.0      0.5     1.0     1.5       2.0     2.5                                0.5      0.0      0.5     1.0     1.5      2.0     2.5
                                   Extra minutes per unit of component (95% interval)                                     Extra minutes per unit of component (95% interval)
                                                                     2023-24 to 2025-26         2021-22 and 2022-23


Figure S3: The three role components of similarity, models A2 and A3 of Table S66, in the main and the
earlier seasons: minutes per unit with 95% intervals (addendum P50; exploratory).



                                                                                          42
  Note to Table S49. Pairs: the unit is a core player ruled Out for a medical reason in at least 5 cases of a team-season who
  played in at least 5 of that team’s other team-games with a report block (a game for which he was listed Out for any reason
  is not a game with him). A teammate enters with at least 3 games on each side: without him, as a retained player of the
  frozen sample of test (1); with him, as a supported roster player not listed Out. Outcome: the teammate’s mean minutes
  from the box scores in the games without him minus his mean in the games with him (0 if he did not play). Regressor:
  the cosine of the two players’ standardised role rates, averaged over the games without him; controls: the teammate’s mean
  reference minutes and headroom in those games; fixed effects for the absent player by team and season. Team-games: rows
  are the frozen rows of test (1) and, for the other team-games, every supported roster player not listed Out; outcome: minutes
  played; similarity is that of test (1) in cases and 0 elsewhere; usual minutes are the player’s mean minutes in his non-case
  rows (at least 3). The first team-game row is not mainly a contrast of cases with other games: 70% of its identifying variance
  (64% in the replication seasons) is the deviation of a player’s similarity from his own mean over his cases, the variation
  used in Table S48; the row with the player’s mean isolates the contrast of cases with other games. Primary sample: 199
  absent players by team and season (127 players, 30 teams); a pair has a median of 9 games without him and 35 with him;
  teammates play 2.93 minutes more on average without him (SD 6.59); similarity has a standard deviation of 0.56 among
  the teammates of one absent player, so the main estimate is 0.87 minutes per standard deviation; 137 absent players in the
  fourth row; team-games: 2,441 cases and 4,177 team-games with a report block, a reference rotation and no core player
  ruled Out (1,758 player-team-seasons). Replication seasons: 131 absent players by team and season (93 players, 30 teams);
  a pair has a median of 8 games without him and 39 with him; teammates play 3.20 minutes more on average without him
  (SD 6.72); similarity has a standard deviation of 0.56 among the teammates of one absent player, so the main estimate is 0.79
  minutes per standard deviation; 87 absent players in the fourth row; team-games: 1,466 cases and 2,921 team-games with
  a report block, a reference rotation and no core player ruled Out (1,161 player-team-seasons). Team-clustered CR1 errors;
  intervals with t(29), except the fourth pairs row of the replication seasons (29 teams, t(28)); WCR with Rademacher weights,
  9,999 draws. With the outcome permuted within team-games (the dry run), the first pairs row is 0.11 (SE 0.17) and the first
  team-game row −0.06 (SE 0.13).




                                       kappa(rho) in the 1,484 cases with original coverage < 1 (main specification)                    Classes of the 2,441 cases under each variant (one setting changed at a time)
                                 1.0
                                                                                                Main (q90, 100 pseudo-min., alpha 0)             39%                   23%             37%

                                 0.9                                                                            Cut floor alpha = 0.5            39%                  19%             42%
     Coverage reachable, kappa




                                                                                                              Cut floor alpha = 0.75             39%                14%             47%
                                 0.8
                                                                                                                       Capacity q95               43%                     25%             33%
                                 0.7
                                                                                                            Capacity: pre-cutoff max               46%                        28%           26%

                                 0.6                                                                               No rate shrinkage              41%                   23%            36%

                                                                                                                300 pseudo-minutes               38%                  23%             39%
                                 0.5                                  25th to 75th percentile
                                                                      median                     Questionable/Doubtful may not add              36%                 22%              42%
                                                                      mean
                                 0.4
                                       0.0         0.5         1.0          1.5           2.0                                           0           25%               50%           75%            100%
                                  Budget for cuts, as a share of the removed minutes (rho / L)                         Covered without cuts            Full coverage needs cuts     Not fully covered even with cuts


Figure S4: Coverage when teammates’ minutes may be cut (addendum P50; exploratory): the median,
mean and interquartile band of κ(ρ) against the cut budget ρ/L in the 1,484 cases below full coverage
(main specification), and the share of cases in each class under each variant of Table S69.




                                                                                                                        43
Table S50: Test (1) with five listed positions, every position pairing, and player fixed effects together with
the joint controls (addendum P34, part B; exploratory). Cells: coefficient (SE), for the position variables
also p; share of the similarity-only coefficient kept.

Model                                                    Primary sample                Kept     Replication seasons           Kept
  Case fixed effects: coefficient of similarity
Similarity only                                      1.102 (0.181)                –             1.201 (0.255)                   –
Three position groups, height gap, partner 0.793 (0.186)                        72%             0.901 (0.235)                 75%
share (second row of Table 3 of the paper)
Five positions (same position), height gap, part- 0.781 (0.176)                 71%             0.921 (0.221)                 77%
ner share
Five positions, position distance, height gap, 0.679 (0.178)                    62%             0.815 (0.205)                 68%
partner share
Every position pairing, height gap                   0.790 (0.169)              72%             0.881 (0.244)                 73%
Every position pairing, height gap, partner 0.691 (0.169)                       63%             0.916 (0.239)                 76%
share (main)
  Case and player × team × season fixed effects: coefficient of similarity
Similarity only                                      1.402 (0.205)                –             1.767 (0.246)                   –
Three position groups, height gap, partner 0.999 (0.219)                        71%             1.281 (0.261)                 72%
share
Five positions, position distance, height gap, 0.885 (0.213)                    63%             1.191 (0.253)                 67%
partner share
Every position pairing, height gap, partner 0.927 (0.225)                       66%             1.250 (0.273)                 71%
share (main)
  Position variables without similarity (case fixed effects; with the height gap)
Same position, three groups                          0.552 (0.213), 0.015         –             1.264 (0.331), 0.0007                –
Same position, five positions                        0.949 (0.298), 0.003         –             1.731 (0.402), 0.0002                –
Same position, five positions, with position dis- 0.568 (0.318), 0.084            –             1.279 (0.436), 0.006                 –
tance in the model
Position distance (per position step)                −0.625 (0.155), 0.0004       –             −0.640 (0.244), 0.014                –
  Partial R2 of similarity / partner share / position and height
Case effects, three position groups                  0.23% / 1.55% / 0.16%        –             0.26% / 1.02% / 0.27%                –
Case effects, every position pairing                 0.16% / 1.50% / 0.52%        –             0.24% / 1.00% / 0.61%                –
Case and player effects, every position pairing 0.20% / 0.18% / 0.54%             –             0.31% / 0.00% / 0.75%                –
  All models include reference minutes and headroom. Every similarity coefficient has p < 0.002. Sample: frozen rows of
  test (1) with position, height, the removed set’s position and height, and the substitution-partner share: 27,896 player-cases
  in 2,423 cases (99% of the frozen rows; the sample of Table S45) and 16,535 in 1,463 cases in the replication seasons. The
  removed set’s position is the position group with the most removed reference minutes. Position distance is the absolute
  difference between the player’s position, numbered from point guard (0) to centre (4), and the reference-minute-weighted
  mean of the removed set. Every position pairing: indicators for the player’s five positions crossed with the removed set’s five
  positions (25 cells; 20 are identified with case effects and 16 with player effects as well). In the primary sample the retained
  player has the removed set’s position in 36% of rows with three groups and 17% with five positions; similarity correlates
  0.21 with same position (three groups), 0.17 (five), −0.29 with position distance, −0.19 with the height gap and 0.07 with
  the partner share. 95% intervals of the two main rows: primary [0.35, 1.04] and [0.47, 1.39], replication [0.43, 1.41] and
  [0.69, 1.81]; WCR p (Rademacher weights, 9,999 draws): primary 0.0005 and 0.0003, replication 0.0008 and 0.0004. One
  within-case standard deviation of similarity on this sample is 0.58, so the main case-effects row is 0.40 minutes per standard
  deviation. Partial R2 : the share of the residual sum of squares of the model without a variable (or group) that it removes, net
  of the fixed effects.




                                                                44
Table S51: Holdout prediction of minutes with five listed positions (addendum P34, part B; descriptive).
Mean absolute error in minutes on 2025–26.

 Model                                                            MAE     Minus the similarity regression [95% interval]
 Allocation in proportion to reference minutes                 7.2012     0.027 [−0.013, 0.064]
 Regression on similarity                                      7.1746     –
 Regression on same position (three groups) and height         7.1660     −0.009 [−0.041, 0.019]
 gap
 Regression on same position (five), position distance         7.1656     −0.009 [−0.043, 0.019]
 and height gap
 Similarity, same position (three groups), height gap          7.1606     −0.014 [−0.034, 0.005]
 Similarity, same position (five), position distance,          7.1620     −0.013 [−0.038, 0.010]
 height gap
  The procedure and data table of the allocation model of Table S14 (hybrid sample): regressions with reference minutes
  and headroom fitted on 2023–24 and 2024–25 (1,574 cases) and evaluated on 2025–26 (1,139 cases, 13,168 player-cases);
  predictions rescaled to the removed minutes of each case. Intervals: team-cluster bootstrap, 2,000 draws. Regressions with
  position are fitted on the training rows that have a position. The first three rows reproduce Table S14. Adding similarity
  to position (addendum P43; descriptive), with the same draws: five positions, distance and height gap −0.0036 [−0.0170,
  0.0109] minutes; three groups and height gap −0.0054 [−0.0233, 0.0132]; the model with similarity has the smaller error
  for 50.3% of player-cases.




                                                             45
Table S52: Why the coefficient of test (1) rises with player fixed effects, and how much variance similarity
accounts for (addendum P34, parts C and F; exploratory).

                                          Pooled Within                Between           Difference           p        Within share
 Primary sample, with the two con-          1.092 1.453 (0.206) 0.663 (0.258) −0.789 (0.311) 0.017                               54%
 trols
 Primary sample, without controls           1.164 1.396 (0.205) 0.890 (0.328) −0.506 (0.369) 0.181                               54%
 Replication seasons, with the two          1.196 1.855 (0.276) 0.506 (0.372) −1.349 (0.386) 0.002                               51%
 controls
 Replication seasons, without con-          1.319 1.781 (0.263) 0.842 (0.419) −0.939 (0.461) 0.051                               51%
 trols

                                                                      R2 Similarity Controls Std. coefficient
              Primary sample, case effects                        3.86%         0.45%       3.39%                 0.066
              Primary sample, case and player effects             1.98%         0.50%       1.49%                 0.070
              Replication seasons, case effects                   3.65%         0.49%       3.08%                 0.069
              Replication seasons, case and player ef-            2.69%         0.71%       2.00%                 0.083
              fects
  Upper panel: outcome and similarity are first taken net of case fixed effects (and of reference minutes and headroom); the
  residual similarity is split into its mean by player, team and season (between) and the deviation from that mean (within). The
  two parts are orthogonal, so the pooled coefficient equals the within coefficient times the within share of the variance plus
  the between coefficient times the rest, exactly. The within column is not the two-way fixed-effects estimate of Table S48
  (1.38 and 1.77), which removes the player effects from all variables jointly; for the same reason the within share here differs
  slightly from the share of variance left by the player effects in that table (53% and 50%). Test of the difference: Wald, t(29),
  team-clustered. In the primary sample the between component correlates 0.005 with the player’s mean reference minutes,
  0.028 with his mean headroom and 0.074 with the share of his cases in which he is in the reference core, so none of these
  explains the difference. Upper panel, columns: coefficient (SE); the difference is between minus within. Lower panel:
  test (1) with case fixed effects, and with player-by-team-by-season fixed effects added; the columns are the R2 net of the
  fixed effects, the partial R2 of similarity, the partial R2 of reference minutes and headroom together, and the standardised
  coefficient of similarity; partial R2 is the share of the residual sum of squares of the model without a variable that the variable
  removes. Extra minutes have a standard deviation of 9.63 minutes within cases in the primary sample (9.73 in the replication
  seasons). The coefficient of reference minutes in test (1) is 0.29 in cases (Table S4) and 0.52 (SE 0.02) in the placebo sample
  of Table S18, where no core player is absent and which does not print this coefficient (headroom: −0.35, SE 0.04): it reflects
  the construction of the reference rotation and not who takes the freed minutes.




                                                                 46
Table S53: Cases and core players who did not play, by season (addendum P34, part D; descriptive). The
last column is 2025–26 divided by the mean of 2023–24 and 2024–25.

                                                        2021–22       2022–23       2023–24      2024–25       2025–26       Ratio
     Report blocks and cases
   Team-games                                     2,460        2,460        2,462       2,462      2,462                         –
   With a report block at the cutoff             92.1%        90.9%        90.5%       88.6%      93.9%                       1.05
   Cases                                            764          702          630         753      1,058                         –
   Cases, share of all team-games                31.1%        28.5%        25.6%       30.6%      43.0%                       1.53
   Cases, share of team-games with a block       33.7%        31.4%        28.3%       34.5%      45.7%                       1.46
     From the box scores: team-games in which at least one of the three core players did not play
   Share of all team-games                       48.7%        44.1%        40.9%       47.9%      54.8%                       1.23
   Share of team-games with a block              47.9%        43.2%        40.5%       47.6%      54.4%                       1.24
   Cases per 100 such team-games with a            70.4          72.7        69.8        72.5       84.0                      1.18
   block
   Season core instead of reference core, all    35.8%        35.6%        32.3%       30.0%      38.3%                       1.23
   team-games
     Core players in team-games with a block: report status at the cutoff against the box score
   Listed Out, did not play                       1,064          915          793       1,059      1,332                          –
   Listed Out, played                                  4            2           0           0          2                          –
   Not listed Out, did not play                     361          352          358         358        318                          –
   Not listed Out, played                         5,366        5,442        5,530       5,129      5,287                          –
   Of those who did not play, listed Out by      74.7%        72.2%        68.9%       74.7%      80.7%                           –
   the cutoff
  Reference core: the three players with the most reference minutes. Season core: for each team and season, the three players
  with the most minutes per game among those with at least 20 games for the team, each counted between his first and last
  appearance; it uses no part of the reference rotation. The case rate over all team-games is the product of three shares: team-
  games with a block; of those, team-games in which a core player did not play; and cases per such team-game. Their ratios
  are 1.05, 1.24 and 1.18; the ratio of the case rate is 1.53. The plan’s statistic, the excess of the box-score ratio over 1 divided
  by the excess of the case-rate ratio over 1, is 0.44 with the reference core and 0.43 with the season core. Over the five seasons
  a core player was listed Out at the cutoff 5,171 times in team-games with a block and played in 8 of them.




                                                                 47
Table S54: Test (1) in new and continuing absences under three definitions of a new absence (addendum
P34, part E; exploratory). Cells: coefficient of similarity (SE); for the differences, also p.

  Definition of a new ab-           Cases Continuing         New              New minus continuing With player effects
  sence
    Primary sample, 2023–24 to 2025–26
  First case of a run of con-    996 0.949 (0.181) 1.307 (0.224) 0.358 (0.166), 0.039                     0.358 (0.143), 0.018
  secutive team-games with
  the same core players out
  At least one removed core      459 1.017 (0.173) 1.440 (0.342) 0.423 (0.294), 0.160                     0.367 (0.274), 0.191
  player played the team’s
  previous game
  Every removed player            94 1.061 (0.179) 1.876 (0.368) 0.815 (0.303), 0.012                     0.299 (0.441), 0.503
  played the team’s previous
  game
    Replication seasons, 2021–22 and 2022–23
  First case of a run of con-    602 0.994 (0.292) 1.495 (0.265) 0.500 (0.248), 0.053                     0.439 (0.228), 0.063
  secutive team-games with
  the same core players out
  At least one removed core      294 1.008 (0.263) 2.018 (0.370) 1.009 (0.344), 0.006                     0.739 (0.268), 0.010
  player played the team’s
  previous game
  Every removed player            57 1.169 (0.260) 1.875 (0.540) 0.706 (0.531), 0.194                     0.524 (0.506), 0.309
  played the team’s previous
  game
  Test (1) with similarity interacted with an indicator for a new absence (case fixed effects; the last column adds player-by-
  team-by-season fixed effects). The definitions are those of addenda P25, P11 and P27 and are nested: every case of the third
  is a case of the second, and every case of the second a case of the first (in the primary sample all 459 cases of the second are
  among the 996 of the first, and all 94 of the third among those of the second). The second definition is implemented as in
  P11: a case in the team’s first game of the sample seasons counts as new, and a removed core player counts as having played
  the previous game if he played in it for any team. Estimates on the new cases alone: primary 1.32, 1.49, 1.92; replication
  1.52, 2.07, 1.98.




                                                                48
Table S55: The case used as an example in the paper: Philadelphia, at home to Milwaukee, 25 February
2024 (six-hour cutoff).

         Player                                     Ref. min.         3PA      AST       REB      Similarity     Played
          Removed set
         Joel Embiid                                      24.3     −0.74      1.00        2.00              –          –
         Kenneth Lofton Jr.                                6.4     −0.59     −0.12        0.30              –          –
         Reference-minute-weighted profile                30.7     −0.71      0.77        1.65              –          –
          Retained players, by similarity
         Mo Bamba                                          9.8     −0.96     −0.55       1.60           0.76          11
         Paul Reed                                        16.4     −1.52     −0.97       1.71           0.65          27
         Tobias Harris                                    24.2     −0.69      0.29      −0.08           0.39          31
         KJ Martin                                        12.3     −1.40     −0.77      −0.07           0.09           0
         Ricky Council IV                                  7.2     −0.47     −0.93       0.27           0.03           7
         Nicolas Batum                                    17.9     −0.60     −0.11      −0.36          −0.19          17
         Tyrese Maxey                                     27.0      0.81      1.15      −1.09          −0.43          38
         Cameron Payne                                    11.2      0.63      0.90      −0.87          −0.44           8
         Kyle Lowry                                       19.3     −0.10      0.53      −0.87          −0.48          21
         Kelly Oubre Jr.                                  22.9     −0.28     −1.32      −0.43          −0.55          29
         Buddy Hield                                      21.1      1.10      0.61      −0.87          −0.59          28
         De’Anthony Melton                                20.0      1.00     −0.14      −0.55          −0.77          18
  Ref. min.: reference minutes; 3PA, AST, REB: standardised per-minute rates of three-point attempts, assists and rebounds;
  Played: minutes played. The second removed player was listed Out for a G League assignment; the case arises from the first,
  a core player listed Out for a medical reason. Coverage in this case is 0.75; single-dimension coverage is 1.00 for three-point
  attempts, 1.00 for assists and 0.95 for rebounds.




                                                                 49
Table S56: Three further checks (addendum P35; exploratory): the comparison of games without and with
the absent player with teammate effects; position pairings where they describe every removed player’s listed
position; where the within-player variation of similarity comes from. Cells: coefficient of similarity (SE),
p; 95% interval.
    Model                                 Primary sample                         Replication seasons
      A. Games without and with the absent player: pairs of a teammate and an absent core player
    Unit effects, all pairs (first row of Ta- 1.542 (0.190), <0.0001 [1.15, 1.93]  1.413 (0.292), <0.0001 [0.82, 2.01]
    ble S49)
    Unit effects, teammates in two or 1.517 (0.206), <0.0001 [1.09, 1.94]          1.429 (0.328), 0.0002 [0.76, 2.10]
    more pairs
    Unit and teammate effects (main)          1.231 (0.245), <0.0001 [0.73, 1.73]  1.620 (0.423), 0.0007 [0.75, 2.49]
    Unit and teammate effects, without 1.254 (0.239), <0.0001 [0.76, 1.74]         1.681 (0.410), 0.0003 [0.84, 2.52]
    the controls
    Unit and teammate effects, weighted 1.295 (0.228), <0.0001 [0.83, 1.76]        1.769 (0.374), <0.0001 [1.00, 2.54]
    by the number of games
      B. Position pairings, cases with one removed reference player (340 and 257 cases)
    Similarity only                           0.961 (0.340), 0.008   [0.27, 1.66]  0.681 (0.524), 0.204   [−0.39, 1.75]
    Three position groups, height gap, 0.493 (0.344), 0.162          [−0.21, 1.20] 0.432 (0.465), 0.361   [−0.52, 1.39]
    partner share
    Every position pairing, height gap        0.402 (0.446), 0.375   [−0.51, 1.31] 0.307 (0.441), 0.493   [−0.60, 1.21]
    Every position pairing, height gap, 0.190 (0.450), 0.675         [−0.73, 1.11] 0.219 (0.443), 0.624   [−0.69, 1.13]
    partner share (main)
    The main model in the other cases         0.765 (0.186), 0.0003 [0.38, 1.15]   1.065 (0.261), 0.0003 [0.53, 1.60]
    Difference from the other cases           −0.574 (0.479), 0.240 [−1.55, 0.41] −0.845 (0.510), 0.108 [−1.89, 0.20]
      B. One listed position among the removed reference players (455 and 291 cases)
    Similarity only                           1.050 (0.316), 0.002   [0.40, 1.70]  0.730 (0.504), 0.158   [−0.30, 1.76]
    Three position groups, height gap, 0.575 (0.329), 0.091          [−0.10, 1.25] 0.488 (0.449), 0.286   [−0.43, 1.41]
    partner share
    Every position pairing, height gap        0.369 (0.398), 0.361   [−0.44, 1.18] 0.324 (0.438), 0.465   [−0.57, 1.22]
    Every position pairing, height gap, 0.201 (0.409), 0.628         [−0.64, 1.04] 0.241 (0.437), 0.586   [−0.65, 1.13]
    partner share (main)
    The main model in the other cases         0.763 (0.190), 0.0004 [0.38, 1.15]   1.059 (0.264), 0.0004 [0.52, 1.60]
    Difference from the other cases           −0.563 (0.446), 0.217 [−1.48, 0.35] −0.818 (0.518), 0.125 [−1.88, 0.24]
      C. Player effects: a player’s cases grouped by identical removed set
    Case and player effects (Table S48)       1.383 (0.211), <0.0001 [0.95, 1.81]  1.773 (0.247), <0.0001 [1.27, 2.28]
    Case and player-by-group effects: 0.222 (0.877), 0.802           [−1.57, 2.02] −1.492 (1.461), 0.316 [−4.48, 1.50]
    removed set unchanged
    Group mean of similarity: differ- 1.410 (0.210), <0.0001 [0.98, 1.84]          1.834 (0.247), <0.0001 [1.33, 2.34]
    ences between groups
    Deviation from the group mean: 0.075 (0.898), 0.934              [−1.76, 1.91] −1.036 (1.411), 0.469 [−3.92, 1.85]
    within a group
    Group mean minus deviation                1.335 (0.890), 0.145   –             2.869 (1.418), 0.052   –
      C. A player’s cases grouped by identical set of removed core players
    Case and player-by-group effects: 1.066 (0.278), 0.0006 [0.50, 1.64]           1.540 (0.294), <0.0001 [0.94, 2.14]
    removed set unchanged
    Group mean of similarity: differ- 1.582 (0.294), <0.0001 [0.98, 2.18]          1.857 (0.325), <0.0001 [1.19, 2.52]
    ences between groups
    Deviation from the group mean: 1.059 (0.263), 0.0004 [0.52, 1.60]              1.590 (0.283), <0.0001 [1.01, 2.17]
    within a group
    Group mean minus deviation                0.522 (0.387), 0.188   –             0.267 (0.412), 0.522   –




                                                            50
Note to Table S56. Team-clustered CR1 errors, t with the number of teams in the regression minus one. Part A: the pairs
of Table S49; a teammate (by team and season) enters when he is paired with two or more absent players: 2,168 of 2,653
pairs, 828 teammates, 180 absent players by team and season, 29 teams (1,308 of 1,661, 530, 116 and 28 in the replication
seasons). Teammate effects leave 58% of the variance of similarity among the teammates of one absent player (standard
deviation 0.43; 51% and 0.39), so the main row is 0.53 minutes per standard deviation (0.64); it is 81% of the row above it
(113%). WCR p of the main row: 0.0003 and 0.0010. Part B: the sample and the models of Table S50, restricted to cases
with one removed reference player (4,362 and 3,264 player-cases; other players without reference minutes may be listed
Out) or to cases in which every removed reference player has a listed position and all have the same one (5,775 and 3,676;
these include the former). The difference from the other cases is the coefficient of similarity interacted with the group in a
model in which every regressor and every position pairing is interacted with the group. Similarity keeps 20% and 19% of
its coefficient in the two groups (32% and 33%); the plan reports these ratios without reading them. WCR p of the main
rows: 0.7025 and 0.6511 (0.6639 and 0.6298). Part C: the frozen rows of test (1) with reference minutes and headroom.
Share of the within-player variance of similarity left inside groups: 2.1% and 2.1% for identical removed sets, 37.9% and
31.5% for identical sets of removed core players. Net of case and player-by-team-by-season effects similarity has a standard
deviation of 0.42 (0.40); inside groups of a player’s cases with the identical removed set it is 0.06 (0.06). A player has a
median of 8 different removed sets in a team-season (7); 17,668 of 28,118 rows are in groups with two or more cases. The
group mean is the player’s mean similarity over his cases with that removed set; differences between groups include changes
of the measured profiles between those cases. WCR p: removed set unchanged 0.8052 and 0.3979; group mean ≤0.0001
and ≤0.0001. WCR with Rademacher weights, 9,999 draws.




                                                             51
Table S57: The comparison of games without and with the absent player, with the pairings of the two listed
positions and similarity measured before the absence (addendum P36; exploratory, with the reading of the
main coefficient fixed in the plan). Cells: coefficient of similarity (SE), p; 95% interval.
        Model                                                               Similarity                 95% interval
          Main seasons: similarity before the first absence (1,278 pairs; 139 absent players; 27 teams)
        Both effects, no position terms                                       1.009 (0.316), 0.004      [0.36, 1.66]
        Both effects, position pairings and height gap (the model the read- −0.022 (0.338), 0.949       [−0.72, 0.67]
        ing applies to)
           the same without the two controls                                  −0.029 (0.325), 0.929     [−0.70, 0.64]
           the same, weighted by the number of games                          0.172 (0.303), 0.576      [−0.45, 0.80]
           the same with absent-player effects only                           0.598 (0.315), 0.069      [−0.05, 1.25]
        Both effects, same-position indicator and height gap                  0.402 (0.331), 0.235      [−0.28, 1.08]
          The same pairs: similarity as in Table S49
        Both effects, no position terms                                       1.303 (0.302), 0.0002     [0.68, 1.92]
        Both effects, position pairings and height gap                        0.261 (0.359), 0.473      [−0.48, 1.00]
           the same without the two controls                                  0.219 (0.352), 0.539      [−0.50, 0.94]
           the same, weighted by the number of games                          0.406 (0.367), 0.279      [−0.35, 1.16]
           the same with absent-player effects only                           0.864 (0.286), 0.006      [0.28, 1.45]
        Both effects, same-position indicator and height gap                  0.680 (0.345), 0.059      [−0.03, 1.39]
          The same pairs: mean similarity over the games before the first absence
        Both effects, no position terms                                       1.149 (0.331), 0.002      [0.47, 1.83]
        Both effects, position pairings and height gap                        0.087 (0.346), 0.804      [−0.62, 0.80]
           the same without the two controls                                  0.052 (0.322), 0.873      [−0.61, 0.71]
           the same, weighted by the number of games                          0.257 (0.302), 0.404      [−0.37, 0.88]
           the same with absent-player effects only                           0.588 (0.329), 0.086      [−0.09, 1.26]
        Both effects, same-position indicator and height gap                  0.526 (0.347), 0.142      [−0.19, 1.24]
          Only that core player out, none out in the comparison games (664 pairs; 79 absent players; 23 teams)
        Both effects, no position terms                                       1.003 (0.614), 0.116      [−0.27, 2.28]
        Both effects, position pairings and height gap                        0.037 (0.597), 0.952      [−1.20, 1.27]
           the same without the two controls                                  0.133 (0.607), 0.829      [−1.13, 1.39]
           the same, weighted by the number of games                          0.241 (0.565), 0.673      [−0.93, 1.41]
           the same with absent-player effects only                           0.284 (0.519), 0.590      [−0.79, 1.36]
        Both effects, same-position indicator and height gap                  0.267 (0.562), 0.639      [−0.90, 1.43]
          No earlier-season game he missed in the teammate’s profile (546 pairs; 113 absent players; 26 teams)
        Both effects, no position terms                                       1.850 (0.677), 0.011      [0.46, 3.24]
        Both effects, position pairings and height gap                        0.741 (0.883), 0.409      [−1.08, 2.56]
           the same without the two controls                                  0.694 (0.867), 0.431      [−1.09, 2.48]
           the same, weighted by the number of games                          0.389 (0.911), 0.673      [−1.49, 2.26]
           the same with absent-player effects only                           0.799 (0.636), 0.221      [−0.51, 2.11]
        Both effects, same-position indicator and height gap                  1.219 (0.889), 0.182      [−0.61, 3.05]
          All pairs with the data (1,788 pairs; 165 absent players; 30 teams)
        Absent-player effects only, no position terms                         1.454 (0.242), <0.0001 [0.96, 1.95]
        Absent-player effects only, position pairings and height gap          0.722 (0.258), 0.009      [0.19, 1.25]
          Replication seasons: similarity as in Table S49 (1,306 pairs; 116 absent players; 28 teams)
        Both effects, no position terms                                       1.617 (0.424), 0.0007     [0.75, 2.49]
        Both effects, position pairings and height gap                        0.742 (0.506), 0.154      [−0.30, 1.78]
           the same without the two controls                                  0.697 (0.501), 0.175      [−0.33, 1.73]
           the same, weighted by the number of games                          1.012 (0.469), 0.040      [0.05, 1.97]
           the same with absent-player effects only                           0.542 (0.363), 0.147      [−0.20, 1.29]
        Both effects, same-position indicator and height gap                  0.897 (0.461), 0.062      [−0.05, 1.84]
          Replication seasons: all pairs with the data (1,659 pairs; 131 absent players; 30 teams)
        Absent-player effects only, no position terms                         1.421 (0.293), <0.0001 [0.82, 2.02]
        Absent-player effects only, position pairings and height gap          0.681 (0.303), 0.032      [0.06, 1.30]




                                                            52
Note to Table S57. Outcome: the teammate’s mean minutes in the games without the absent player minus his mean minutes in
the games with him (Table S49); both effects: absent player by team and season, and teammate by team and season; controls:
the teammate’s mean reference minutes and headroom in the games without the absent player. Position pairings: indicators
for the 25 pairings of the two players’ five listed positions (25 occur, 16 columns are identified net of the effects); height
gap: the absolute difference of their heights. Similarity before the first absence: the cosine of the two players’ standardised
rates at the cutoff of the last game, before the absent player’s first absence with that team in that season, in which he played
and both players had a profile. The first absence is the first team-game in which he was on the team’s roster at the cutoff and
did not play, or which is one of his cases; no game he missed for that team in that season enters either profile. Of the 2,653
pairs, 1,788 have this similarity (165 of 199 absent players have such a game), 1,788 also have both positions and heights,
and 1,278 of these belong to teammates paired with two or more absent players (541 teammates by team and season; 1,306
pairs of 529 teammates in the replication seasons). Absent players are counted by team and season. The profiles use each
player’s last 20 games and reach into the previous season: in 557 of the 1,278 pairs (44%) the teammate’s profile holds at
least one earlier-season game of the same team that the absent player missed (2.2 games per pair on average). Correlation of
the similarity before the absence with that of Table S49: 0.86. Standard deviation of similarity net of both effects: 0.44; net
also of the position terms and controls: 0.38 (0.39 and 0.33 in the replication seasons). Reading fixed in the plan: the 95%
interval of the main coefficient is compared with zero and with ±0.54 minutes per unit of similarity (0.30 minutes per 0.56,
the standard deviation of similarity among the teammates of one absent player in Table S49). Outcome: no clear additional
association is detected, but one of the size set in advance cannot be excluded, so it cannot be judged whether what remains
is small (−0.01 minutes per 0.56; 95% interval −0.40 to 0.38). WCR p of the main coefficient (Rademacher weights, 9,999
draws): 0.9474; its height-gap coefficient is −0.13 (SE 0.14) minutes per inch. Share of the coefficient without position terms
that remains with them, reported without a reading: -2% in the main block, 20% and 8% with the other two similarities, 50%
in all pairs with the data, and 46% and 48% in the replication seasons. In P36 the replication seasons had no table of every
reference player’s profile in every game, so similarity before the absence was not computed there; addendum P42 later built
those profiles (Table S63). Team-clustered CR1 errors, t with the number of teams in the regression minus one; the small-
sample factor counts the explicit regressors and not the absorbed effects (Table S58 gives the standard errors that count them).
Only the main row is read by the rule; the other rows are the sensitivity analyses fixed in the plan.




                                                              53
Table S58: Standard errors with the absorbed fixed effects also counted in the small-sample factor (ad-
dendum P37; a check of the inference convention made after all other results were known). a: absorbed
parameters; SE∗ and interval∗ : with them counted; player effects: player by team and season; both effects:
absent player and teammate, each by team and season.
Model                                                        a        Factor Coef. (SE)    95% interval SE∗ Interval∗
  Every model of addenda P33 to P36, by its fixed effects (number of coefficients; rows n)
Case (92; 3,264–127,830)                              257–10,919 1.041–1.048
Case; player by team and season (34; 16,535–         2,494–4,028 1.080–1.085
28,118)
Case; player by team (2; 16,583–28,118)              2,240–3,494 1.069–1.075
Case; player by removed set (4; 16,583–28,118) 4,853–17,095 1.183–1.597
Team-game; player by team and season (18;            5,440–8,286 1.055–1.056
52,487–81,178)
Pairs: absent player (24; 546–2,653)                      79–199 1.040–1.130
Pairs: absent player; teammate (48; 546–2,168)           306–946 1.332–1.546
  Main seasons: models whose coefficients the paper reports
Test (1), case effects                                      2,441         1.046 1.09 (0.18) [0.72, 1.46] 0.19 [0.71, 1.48]
   and player effects                                       4,028         1.080 1.38 (0.21) [0.95, 1.81] 0.23 [0.92, 1.85]
Table 3 of the paper: row 1, similarity only                2,423         1.046 1.10 (0.18) [0.73, 1.47] 0.19 [0.71, 1.49]
   row 2: three groups, height gap, partner share           2,423         1.046 0.79 (0.19) [0.41, 1.17] 0.20 [0.39, 1.19]
   row 3: every pairing, height gap, partner share          2,423         1.047 0.69 (0.17) [0.35, 1.04] 0.18 [0.33, 1.05]
   row 5: player effects, similarity only                   4,008         1.081 1.40 (0.20) [0.98, 1.82] 0.22 [0.95, 1.85]
   row 6: player effects and the controls of row 3          4,008         1.081 0.93 (0.23) [0.47, 1.39] 0.24 [0.43, 1.43]
   row 8: one position removed, similarity only               455         1.042 1.05 (0.32) [0.40, 1.70] 0.33 [0.38, 1.72]
   row 9: one position removed, controls of row               455         1.042 0.20 (0.41) [−0.64, 1.04] 0.43 [−0.67, 1.07]
3
   row 10: pairs (1,278), both effects                        625         1.401 1.01 (0.32) [0.36, 1.66] 0.44 [0.10, 1.92]
   row 11: the same with position terms                       625         1.410 −0.02 (0.34) [−0.72, 0.67] 0.48 [−1.00, 0.96]
   row 12: absent-player effects, position terms              139         1.061 0.60 (0.32) [−0.05, 1.25] 0.33 [−0.09, 1.28]
Placebo: real minus placebo gradient                       10,919         1.046 1.14 (0.37) [0.39, 1.89] 0.38 [0.35, 1.92]
Pairs (2,653), absent-player effects                          199         1.040 1.54 (0.19) [1.15, 1.93] 0.20 [1.14, 1.95]
   only that core player out                                  137         1.042 1.30 (0.26) [0.77, 1.83] 0.27 [0.75, 1.86]
Pairs (2,168), both effects                                   946         1.333 1.23 (0.25) [0.73, 1.73] 0.33 [0.56, 1.90]
Pairs (1,278), both effects, similarity of Ta-                625         1.401 1.30 (0.30) [0.68, 1.92] 0.42 [0.43, 2.17]
ble S49
   the same with position terms                               625         1.410 0.26 (0.36) [−0.48, 1.00] 0.51 [−0.78, 1.30]
Pairs (1,788), absent-player effects, position                165         1.050 0.72 (0.26) [0.19, 1.25] 0.27 [0.17, 1.28]
terms
Pairs (664), only that core player out, row 11                355         1.493 0.04 (0.60) [−1.20, 1.27] 0.89 [−1.81, 1.88]
model
Pairs (546), no earlier-season game missed, row               306         1.546 0.74 (0.88) [−1.08, 2.56] 1.37 [−2.07, 3.55]
11 model
  Replication seasons
Test (1), case effects                                      1,466         1.047 1.20 (0.26) [0.67, 1.72] 0.27 [0.65, 1.74]
   and player effects                                       2,498         1.085 1.77 (0.25) [1.27, 2.28] 0.27 [1.22, 2.32]
Every pairing, height gap, partner share                    1,463         1.047 0.92 (0.24) [0.43, 1.41] 0.25 [0.40, 1.43]
   one position removed                                       291         1.042 0.24 (0.44) [−0.65, 1.13] 0.46 [−0.69, 1.17]
Pairs (1,661), absent-player effects                          131         1.042 1.41 (0.29) [0.82, 2.01] 0.30 [0.79, 2.03]
Pairs (1,308), both effects                                   604         1.364 1.62 (0.42) [0.75, 2.49] 0.58 [0.43, 2.80]
Pairs (1,306), both effects, positions (P36; for              603         1.372 0.74 (0.51) [−0.30, 1.78] 0.69 [−0.68, 2.17]
P42 see Table S63)
   the same with absent-player effects only                   116         1.049 0.54 (0.36) [−0.20, 1.29] 0.38 [−0.24, 1.32]




                                                             54
  Note to Table S58. In the paper and in this supplement, the small-sample factor G/(G − 1) · (n − 1)/(n − k) of the team-
  clustered CR1 errors counts the k explicit regressors and not the absorbed fixed effects, which in the models of this table
  are all nested within teams; this is the usual convention when the effects are nested within the clusters (Cameron and Miller,
  2015, Section III.B, for effects at the level of the cluster; Correia, 2015; both in the references of the paper). The more
  conservative count adds the rank a of the absorbed effects (one set: its number of levels; two sets: the levels of both minus
  the connected
             p components of the graph in which each row joins its two levels), which multiplies the standard error by
  the factor (n − k)/(n − k − a); the interval∗ uses the same t quantile as the original interval. Wild bootstrap p-values do
  not change, because the factor cancels from every bootstrap t statistic. Every model estimated by the shared estimation
  functions of addenda P33 to P36 was re-estimated; its coefficient and standard error agree with the committed result files
  (246 coefficient records, largest difference 0). The within/between splits of P34 part C and P35 part C are computed outside
  those functions and are compared but not annotated; the planned allocation test and its variants (Tables S9 to S23) have case
  effects only, whose factor is 1.04 to 1.05 in every model here, and are not recomputed one by one. Of the 222 coefficients,
  6 have a 95% interval that excludes zero under the usual count and includes it under the conservative one: P34 part B, main
  seasons: height gap, every position pairing with partner share (row 3 of Table 3 of the paper) (−0.12; [−0.24, 0.00]); height
  gap, five positions and position distance with player effects (−0.22; [−0.45, 0.01]); P34 part B, replication seasons: height
  gap, five positions with partner share (−0.13; [−0.27, 0.00]); P36, main seasons: similarity, pairs with no earlier-season
  game he missed in the teammate’s profile, both effects, no position terms (1.85; [−0.26, 3.96]); P36, replication seasons:
  height gap, both effects, position terms (row 13 of Table 3 of the paper until addendum P42 replaced it) (−0.25; [−0.53,
  0.03]); similarity in the same model weighted (1.01; [−0.31, 2.33]). No verdict of a planned test depends on this choice.
  The paper keeps the usual count and gives the range of the factor in its Section 4; the conservative interval of the row of
  addendum P42 that replaced row 13 is in the note to Table S63.




Table S59: The allocation model of Table 3 of the paper with the listed positions of all removed players
(addendum P38; exploratory, with the reading fixed in the plan). Coefficient of similarity (SE) and the share
of the similarity-only coefficient with the same fixed effects that it keeps.
  Model                                                                Primary sample     Kept     Replication seasons     Kept
   All cases of the common sample: case effects
  Similarity only                                                     1.10 (0.18)           – 1.20 (0.25)                  –
  Main position of the removed set (Table 3 of the paper, row 3)      0.69 (0.17)        63% 0.92 (0.24)               76%
  Positions of all removed players (Table 3 of the paper, row 4)      0.49 (0.17)        45% 0.83 (0.22)               69%
  Both position descriptions                                          0.48 (0.17)        44% 0.82 (0.22)               68%
   All cases of the common sample: case and player-by-team-by-season effects
  Similarity only                                                     1.40 (0.20)           – 1.77 (0.25)                  –
  Main position of the removed set (Table 3 of the paper, row 6)      0.93 (0.23)        66% 1.25 (0.27)               71%
  Positions of all removed players (Table 3 of the paper, row 7)      0.75 (0.22)        53% 1.16 (0.26)               66%
  Both position descriptions                                          0.77 (0.22)        55% 1.14 (0.26)               65%
   Without the cases in which every removed player has the same listed position: case effects
  Similarity only                                                     1.10 (0.21)           – 1.35 (0.28)                  –
  Main position of the removed set                                    0.76 (0.19)        69% 1.06 (0.26)               79%
  Positions of all removed players                                    0.52 (0.20)        47% 0.87 (0.26)               65%
   Without the cases in which every removed player has the same listed position: case and player-by-team-by-season effects
  Similarity only                                                     1.55 (0.21)           – 1.93 (0.28)                  –
  Main position of the removed set                                    1.09 (0.21)        71% 1.43 (0.28)               74%
  Positions of all removed players                                    0.81 (0.21)        52% 1.31 (0.27)               68%
   Cases in which every removed player has a listed position: case effects
  Similarity only                                                     1.10 (0.18)           – 1.21 (0.26)                  –
  Main position of the removed set                                    0.69 (0.17)        63% 0.94 (0.24)               77%
  Positions of all removed players                                    0.49 (0.17)        45% 0.85 (0.22)               70%
   Cases in which every removed player has a listed position: case and player-by-team-by-season effects
  Similarity only                                                     1.40 (0.20)           – 1.79 (0.25)                  –
  Main position of the removed set                                    0.93 (0.23)        66% 1.29 (0.27)               72%
  Positions of all removed players                                    0.75 (0.22)        53% 1.19 (0.26)               66%




                                                               55
  Note to Table S59. Every model also has the height gap, the substitution-partner share, reference minutes and headroom.
  Main position of the removed set: the 25 indicators of the pairing of the teammate’s five listed positions with the position
  that has the most removed reference minutes (rows 3 and 6 of Table 3 of the paper). Positions of all removed players:
  the 25 products of an indicator of the teammate’s position and the share of the removed reference minutes at each of the
  five positions, the share taken over all removed reference minutes (a removed player without a listed position adds to the
  denominator only); where every removed player has the same listed position the two descriptions coincide. Sample: the
  common sample of Table 3 of the paper (27,896 player-cases in 2,423 cases; replication seasons 16,535 in 1,463); 455 and
  291 cases in which every removed player has the same listed position, 0 and 8 cases with a removed player without a listed
  position; players with a listed position hold 100% and 100% of the removed reference minutes on average over all cases,
  and – and 75% within the cases with a removed player without a listed position (derived from the mean over all cases, since
  the share is 1 in the other cases: one minus the product of one minus that mean and the ratio of all cases to these cases).
  Positions of all removed players, all cases: 95% interval 0.15 to 0.84 (case effects; WCR p 0.0059, Rademacher weights,
  9,999 draws) and 0.30 to 1.19 (player effects); replication seasons 0.38 to 1.29 (WCR p 0.0011) and 0.63 to 1.70. With the
  absorbed effects counted in the small-sample factor (Table S58): 0.13 to 0.86 and 0.27 to 1.23; 0.35 to 1.31 and 0.58 to 1.74.
  The case-effects row of all cases is the model that the separate check of P35 computed outside its plan on the earlier build
  (analysis record); on the final data it gives 0.494 (0.169) and 0.832 (0.224). Team-clustered CR1 errors, t with the number
  of teams in the regression minus one.




Table S60: The comparison of games without and with the absent player in windows around the start and the
end of his absence (addendum P39; exploratory, with the reading of the main coefficient fixed in the plan).
Coefficient of similarity (SE); 95% interval; spells.
   Outcome                                           Primary sample              Spells   Replication seasons           Spells
    Windows of 3 games (the main reading: first row)
   Both sides (mean of start and end)              0.77 (0.42); −0.09 to 1.62      168    2.43 (0.35); 1.72 to 3.15       128
   Start of the spell, every valid spell           1.04 (0.31); 0.41 to 1.67       283    2.03 (0.45); 1.10 to 2.95       197
   End of the spell, every valid spell             0.69 (0.34); −0.00 to 1.38      235    2.60 (0.36); 1.86 to 3.34       151
   Start, on the spells with both sides            0.63 (0.45); −0.29 to 1.56      168    2.39 (0.50); 1.38 to 3.41       128
   End, on the spells with both sides              0.90 (0.49); −0.09 to 1.90      168    2.47 (0.45); 1.56 to 3.39       128
   Before the spell (no change of his status)      0.32 (0.23); −0.15 to 0.79      198    −0.33 (0.29); −0.93 to 0.27     144
   Both sides, other core players playing in every 0.79 (0.60); −0.44 to 2.03       52    1.79 (0.55); 0.64 to 2.94        36
   window game
    Windows of 2 games
   Both sides (mean of start and end)              0.93 (0.28); 0.36 to 1.49       269    2.00 (0.41); 1.15 to 2.84       193
   Start of the spell, every valid spell           1.04 (0.26); 0.51 to 1.56       403    1.78 (0.45); 0.86 to 2.69       264
   End of the spell, every valid spell             1.10 (0.25); 0.60 to 1.60       336    2.40 (0.39); 1.60 to 3.20       220
   Before the spell (no change of his status)      0.29 (0.23); −0.17 to 0.75      310    0.21 (0.29); −0.38 to 0.79      230
    Windows of 5 games
   Both sides (mean of start and end)              0.82 (0.56); −0.35 to 1.99       56    2.62 (0.63); 1.33 to 3.91        58
   Start of the spell, every valid spell           1.28 (0.48); 0.30 to 2.27       138    1.88 (0.46); 0.93 to 2.83       108
   End of the spell, every valid spell             0.92 (0.41); 0.07 to 1.77       108    2.67 (0.43); 1.78 to 3.56        81
   Before the spell (no change of his status)      0.16 (0.28); −0.42 to 0.75       86    −0.85 (0.41); −1.70 to 0.00      64




                                                               56
  Note to Table S60. Team-games of a team-season are ordered by scheduled start. A spell is a maximal run of consecutive
  team-games in which the absent core player is on the roster and does not play, containing at least one game in which he
  is ruled Out for a medical reason at the cutoff as a core player of a case (the games without him of Table S49). Start: the
  teammate’s mean minutes in the first W games of the spell minus those in the W games before it, in which the absent player
  played; end: the last W games of the spell minus the W games after it, in which he played again; both sides: the mean of the
  two, in which a drift of the teammate’s minutes that is linear in the team’s game number cancels (a drift linear in calendar
  time need not, because the games are not evenly spaced); before the spell: games −W to −1 minus games −2W to −W − 1.
  A teammate is a supported player on the roster and not listed Out in every game of the windows (minutes 0 if he did not play)
  and a retained player of at least one of the first W case games of the spell; similarity and the controls (reference minutes,
  headroom) are his means over those case games. Every model has a fixed effect per spell; team-clustered CR1 errors. Spells:
  702 and 445; with W = 3, 283 and 197 have a valid start, 235 and 151 a valid end, 168 and 128 both. Main reading (primary
  sample, W = 3, both sides), fixed in the plan against zero and ±0.54 minutes per unit of similarity (the size of Table S57):
  the window comparison is too imprecise to tell; WCR p 0.0779 (Rademacher weights, 9,999 draws); with the absorbed spell
  effects counted (Table S58) −0.14 to 1.68. Replication seasons: detected, and at least the size set in advance as meaningful
  (WCR p ≤0.0001). The windows may understate the gradient of the full comparison, because the absent player often leaves
  his last game injured and returns on limited minutes. Short spells make the windows of the two sides overlap.




Table S61: The allocation test with the retained teammate’s own pregame status (addendum P40; ex-
ploratory, with the reading fixed in the plan).
                                                       Primary sample 95% interval       Replication seasons 95% interval
       Coefficient of similarity (SE); 95% interval
     Test (1) as planned                                1.09 (0.18)      0.72 to 1.46    1.20 (0.26)          0.67 to 1.72
     With the teammate’s pregame status                 1.00 (0.18)      0.62 to 1.38    1.14 (0.25)          0.62 to 1.65
     With his status, without teammates listed Ques- 1.08 (0.19)         0.70 to 1.46    1.21 (0.26)          0.69 to 1.74
     tionable or Doubtful
       Teammate’s status in the model with his status (minutes, against not listed)
     Available                                          −0.37 (0.44)                     −1.68 (1.57)
     Probable                                           −1.39 (0.53)                     −1.04 (0.99)
     Questionable                                       −12.69 (0.63)                    −12.58 (0.69)
     Doubtful                                           −24.69 (0.85)                    −26.69 (1.88)
       Rows
     Player-cases (cases)                               28,118 (2,441)                   16,583 (1,466)
        without teammates listed Questionable or 26,097                                  15,575
     Doubtful
  Rows: the frozen sample of test (1). The teammate’s status is the one on the last official report whose header time is at or
  before the six-hour cutoff in which the team’s block was submitted; teammates listed Out are removed players and never
  retained. Core players, reference minutes, headroom, the removed set and similarity are unchanged; leaving teammates
  out only drops their rows. Every model has similarity, reference minutes, headroom and case effects; team-clustered CR1
  errors, t with 29 degrees of freedom. WCR p (Rademacher weights, 9,999 draws): ≤0.0001 and ≤0.0001 in the primary
  sample, 0.0002 and ≤0.0001 in the replication seasons. With the absorbed case effects counted in the small-sample factor
  (Table S58): 0.61 to 1.40 and 0.68 to 1.48; 0.59 to 1.68 and 0.66 to 1.76. Relative to test (1): 92% and 99% in the primary
  sample, 95% and 101% in the replication seasons. Per within-case standard deviation of similarity in the frozen sample
  (0.58): 0.63, 0.58 and 0.63 minutes. A listed status is mostly medical; a few teammates are listed for a G League assignment,
  rest or other reasons.




                                                              57
Table S62: Role coverage with teammates listed Doubtful or Questionable not counted as available (adden-
dum P41; exploratory, with the reading fixed in the plan). Coefficient [95% interval].
  Version                                     Role output: ck         ck with the benchmark      Margin, per 0.1 of coverage
    Primary sample (2,441 cases)
  As in the paper                             0.054 [−0.005, 0.114]   −0.053 [−0.126, 0.021]     −0.10 [−0.68, 0.49]
  Teammates listed Doubtful supply noth-      0.050 [−0.009, 0.108]   −0.061 [−0.134, 0.011]     −0.09 [−0.68, 0.51]
  ing
  Teammates listed Doubtful or Question-      0.052 [−0.002, 0.105]   −0.057 [−0.126, 0.012]     −0.05 [−0.58, 0.48]
  able supply nothing
  Players listed Doubtful treated as absent   0.051 [−0.005, 0.106]   −0.059 [−0.125, 0.006]     −0.05 [−0.63, 0.53]
    Replication seasons (1,466 cases)
  As in the paper                             0.100 [0.047, 0.153]    0.068 [−0.009, 0.144]      0.24 [−0.43, 0.91]
  Teammates listed Doubtful supply noth-      0.100 [0.048, 0.153]    0.068 [−0.007, 0.143]      0.27 [−0.40, 0.94]
  ing
  Teammates listed Doubtful or Question-      0.089 [0.037, 0.140]    0.049 [−0.029, 0.127]      0.21 [−0.43, 0.86]
  able supply nothing
  Players listed Doubtful treated as absent   0.101 [0.050, 0.153]    0.067 [−0.007, 0.142]      0.26 [−0.39, 0.91]
  Cases, reference rotations, reference minutes, role rates and the removed set are those of the paper; the case sample never
  changes. Coverage counts as suppliers all reference players not ruled Out, with their full headroom. In the versions where
  they supply nothing, teammates listed Doubtful (or Questionable) keep their reference minutes and the demand is unchanged;
  treated as absent, players listed Doubtful join the removed set, so the demand, the removed minutes, the removed minute
  share, the lost value and the supply are recomputed (team-games that would become cases are not added). The benchmark
  is computed over the players who can supply. The first row reproduces the coefficients and intervals of the paper (Table 2
  and Section 6.2); its bootstrap p-values are redrawn and can differ from the published ones in the second decimal. Retained
  player-cases listed Doubtful / Questionable: 285 / 1,736 of 28,118 (primary), 129 / 879 of 16,583 (replication); cases with
  such a teammate: 227 (Doubtful) and 1,245 (either), 7.4% of the retained headroom. Coverage changes in 3.3%, 23.6% and
  7.3% of primary cases. Team-clustered CR1 errors, t with 29 degrees of freedom; WCR p (Webb weights, 9,999 draws, the
  same seeds in every version) for the benchmark model 0.171, 0.110, 0.121, 0.087 and for the margin 0.746, 0.785, 0.845,
  0.859 (primary).




                                                                58
Table S63: The comparison of games without and with the absent player in the replication seasons, with
similarity measured before the absence and listed position controlled between the two players of each pair
(addendum P42; exploratory, with the reading fixed in the plan). Coefficient of similarity (SE).
            Model (absent-player and teammate effects)                                 Coefficient (SE)     95% interval
             Similarity before the absence
            Without position terms                                                     1.57 (0.43)          0.69 to 2.45
            With position pairings and height gap                                      0.85 (0.58)          −0.34 to 2.04
            Same, without the controls                                                 0.68 (0.61)          −0.59 to 1.94
            Same, weighted                                                             1.04 (0.53)          −0.05 to 2.12
            Same, absent-player effects only                                           0.86 (0.37)          0.10 to 1.63
            Same-position indicator instead of the pairings                            0.95 (0.48)          −0.04 to 1.95
             Similarity of Section 5.2 of the paper
            Without position terms                                                     1.56 (0.37)          0.79 to 2.33
            With position pairings and height gap                                      0.96 (0.54)          −0.15 to 2.08
            Same, without the controls                                                 0.91 (0.59)          −0.30 to 2.12
            Same, weighted                                                             1.11 (0.49)          0.11 to 2.11
            Same, absent-player effects only                                           0.87 (0.40)          0.06 to 1.69
            Same-position indicator instead of the pairings                            0.96 (0.44)          0.06 to 1.86
             Mean similarity before the absence
            Without position terms                                                     1.56 (0.49)          0.55 to 2.56
            With position pairings and height gap                                      0.82 (0.66)          −0.53 to 2.17
            Same, without the controls                                                 0.80 (0.71)          −0.66 to 2.27
            Same, weighted                                                             1.09 (0.62)          −0.19 to 2.37
            Same, absent-player effects only                                           0.87 (0.43)          −0.02 to 1.76
            Same-position indicator instead of the pairings                            0.91 (0.55)          −0.23 to 2.05
  The specification of Table S57 for the primary sample, applied to the replication seasons: 914 pairs of 389 teammates and
  103 absent players (by team and season) of 26 teams, with similarity before the absence, both players’ positions and heights,
  and a teammate in two or more pairs; the 1,306 pairs of the replication seasons in Table S57 use the similarity of Section 5.2
  only. Every player’s profile at every team-game of these seasons (needed for the similarity before the absence) was built with
  the code of the final build; the other tables written in the same run are identical to those of the final build. Correlation of the
  similarity before the absence with that of Section 5.2: 0.88. Reading of the main model (fixed in the plan, as for Table S57):
  no additional association detected, a size of 0.54 minutes per unit not excluded; WCR p (Rademacher weights, 9,999 draws)
  0.2178; with the absorbed effects counted in the small-sample factor: −0.84 to 2.54. Difference from the primary sample’s
  main model (Table S57): 0.87; no standard error is given, because the two periods share teams and the two estimates are not
  independent under team clustering. Team-clustered CR1 errors, t with 25 degrees of freedom. The count of earlier-season
  games missed by the absent player in the teammate’s profile, and the models without such pairs, are not computed: the rosters
  of 2020–21 are not built.




                                                                 59
Table S64: The allocation test split into whether a retained teammate plays and his minutes when he plays,
and without the cases whose removed-set profile is closest to zero (addendum P45; exploratory, with the
reading fixed in the plan). Coefficient of similarity per unit (SE) and 95% interval.
                                                        Primary sample 95% interval       Replication seasons 95% interval
     Test (1): extra minutes                            1.09 (0.18)       0.72 to 1.46    1.20 (0.26)           0.67 to 1.72
     Plays at all (percentage points)                   2.0 (0.6)         0.7 to 3.2      1.0 (0.7)             −0.4 to 2.5
     Extra minutes, players who played (descrip-        0.86 (0.13)       0.59 to 1.14    1.18 (0.20)           0.78 to 1.58
     tive)
     Test (1) without cases whose profile norm is be-   1.10 (0.18)       0.72 to 1.48    1.19 (0.26)           0.65 to 1.72
     low 0.2
     Test (1) without cases whose profile norm is be-   1.12 (0.18)       0.74 to 1.50    1.20 (0.26)           0.66 to 1.74
     low 0.3
  Rows: the frozen sample of test (1); every model has similarity, reference minutes, headroom and case effects; team-clustered
  CR1 errors, t with 29 degrees of freedom. 84.5% of retained player-cases played (85.3% in the replication seasons), for 23.8
  minutes on average; every case has at least two who played. The second row is a linear probability model; the third conditions
  on playing, which similarity may itself affect, and is descriptive. The two do not add up to the first, which counts a teammate
  who did not play as minus his reference minutes. Per within-case standard deviation of similarity (0.58): 0.63 minutes, 1.1
  percentage points (about 0.27 minutes at the mean minutes of those who played) and 0.50 minutes in the primary sample;
  0.67, 0.6 and 0.66 in the replication seasons. WCR p (Rademacher weights, 9,999 draws): 0.0046 and ≤0.0001 (primary),
  0.1601 and ≤0.0001 (replication); with the absorbed case effects counted (Table S58): 0.7 to 3.3 and 0.57 to 1.15 (primary).
  Norm of the removed set’s mean standardised profile (Equation 2 of the paper): minimum 0.057 (0.073 in the replication
  seasons), with 1st and 50th percentiles 0.19 and 1.00; below 0.2 in 29 primary cases (297 player-cases) and below 0.3 in 86;
  24 and 62 in the replication seasons.




Table S65: Test (1) with non-linear controls for reference minutes and headroom (addendum P48; ex-
ploratory, with the reading fixed in the plan). Coefficient of similarity (team-clustered SE), case fixed ef-
fects.

    Controls                                                                     Similarity              p   Ratio to linear
    Main seasons, 2023–24 to 2025–26 (28,118 player-cases)
    Linear reference minutes and headroom (test (1))                         1.092 (0.180)      <0.0001                1.000
    Restricted cubic splines, 5 knots each                                   1.137 (0.184)      <0.0001                1.041
    Decile indicators of each                                                1.132 (0.176)      <0.0001                1.036
    Reference-minute deciles × headroom quintiles (50 cells)                 1.143 (0.183)      <0.0001                1.046
    Earlier seasons, 2021–22 and 2022–23 (16,583 player-cases)
    Linear reference minutes and headroom (test (1))                         1.196 (0.256)      <0.0001                1.000
    Restricted cubic splines, 5 knots each                                   1.291 (0.259)      <0.0001                1.080
    Decile indicators of each                                                1.264 (0.256)      <0.0001                1.057
    Reference-minute deciles × headroom quintiles (50 cells)                 1.289 (0.254)      <0.0001                1.078
  Knots of the splines at the 5th, 27.5th, 50th, 72.5th and 95th percentiles. Reading of the plan: within ±10% of the linear
  coefficient in every row, so the coefficient is insensitive to the non-linear controls examined (largest change 8.0%). Position
  coverage after correction M (listed positions matched from the roster rows by team and season): 0 of 2,441 primary cases
  and 8 of 1,466 cases of the earlier seasons have a removed player without a listed position (1 player, absent from the roster
  rows); before the correction 486 primary cases had one. Matching: 3,294 player-team-seasons matched (3,240 by the full
  name, 48 without the suffix, 8 by last name and initial), 2 conflicting pairs dropped.




                                                               60
Table S66: Role similarity split into its three role components (addendum P50, part A; exploratory). Minutes
per unit of each component (95% interval), case fixed effects, reference minutes and headroom in every
model; test of equal coefficients of the three components.
Model                                    Three-point attempts    Assists                 Rebounds              Equal: F, p (WCR p)             n
  Main seasons, 2023–24 to 2025–26
A0: similarity (test (1))              1.092 (0.723 to 1.461)                                                                           28,118
A1: three components                   0.82 (0.14 to 1.50)       0.75 (0.06 to 1.45)     1.75 (1.17 to 2.34)   4.35, 0.022 (0.024)      28,118
A2: A1 and the teammate’s own scaled 0.75 (0.02 to 1.47)         1.01 (0.26 to 1.75)     1.76 (1.12 to 2.40)   2.92, 0.070 (0.079)      28,118
rates (main)
A3: A2, every position pairing, height 0.33 (−0.37 to 1.02)      0.62 (−0.04 to 1.28)    1.03 (0.52 to 1.55)   1.99, 0.155 (0.172)      27,896
gap, partner share, own status
  Earlier seasons, 2021–22 and 2022–23
A0: similarity (test (1))              1.196 (0.672 to 1.720)                                                                           16,583
A1: three components                   0.99 (0.14 to 1.84)       1.01 (0.26 to 1.76)     1.75 (0.84 to 2.66)   1.56, 0.227 (0.244)      16,583
A2: A1 and the teammate’s own scaled 0.84 (−0.17 to 1.85)        1.16 (0.34 to 1.99)     1.82 (0.92 to 2.71)   1.97, 0.158 (0.201)      16,583
rates (main)
A3: A2, every position pairing, height 0.65 (−0.23 to 1.53)      0.76 (−0.01 to 1.52)    1.16 (0.24 to 2.08)   0.48, 0.621 (0.669)      16,535
gap, partner share, own status
   With v jk = z jk /∥z j ∥ and wk = z̄Rk /∥z̄R ∥, similarity is ∑k wk v jk ; component k is wk v jk (the sum of the three equals similarity
   to within 10−14 ). A1 with the three coefficients constrained equal returns test (1) (1.0923). A2 adds the v jk as controls,
   A3 the controls of Table 3 of the paper, row 3, and the teammate’s own pregame status, on its common sample; with the
   controls of that row alone the similarity coefficient is 0.6906, as in the paper. Team-clustered CR1 errors, t(29); equality:
   Wald F(2, 29) and wild cluster restricted bootstrap (Webb weights, 9,999 draws). Within-case standard deviations of the
   components in the main seasons: 0.31, 0.34, 0.30 (similarity 0.58). Cases with |wk | > 0.3: 1,763, 1,842, 1,744 of 2,441. The
   ordering of the three estimates is descriptive: equality is not rejected in A2 or A3 in either period.




Table S67: Model A2 of Table S66 with each component split by the sign of the removed set’s scaled rate
wk (addendum P50, part A; the split was specified with the plan, the tests of the differences were added
afterwards, at a co-author’s review; exploratory, no correction for multiple comparisons). Minutes per unit
(95% interval).
            Component                 wk > 0                     wk < 0                    Difference                     WCR p
             Main seasons (28,118 player-cases)
            Three-point attempts 0.72 (−0.38 to 1.81)            0.75 (−0.74 to 2.23)      −0.03 (−2.17 to 2.11)          0.976
            Assists                0.07 (−1.03 to 1.16)          2.36 (1.08 to 3.65)       −2.30 (−4.22 to −0.37)         0.026
            Rebounds               2.89 (1.82 to 3.96)           0.57 (−0.45 to 1.59)      2.32 (0.66 to 3.98)            0.0097
             Earlier seasons (16,583 player-cases)
            Three-point attempts 0.65 (−0.70 to 1.99)            1.06 (−1.56 to 3.67)      −0.41 (−3.90 to 3.08)          0.824
            Assists                0.54 (−1.26 to 2.33)          2.02 (0.13 to 3.91)       −1.48 (−4.82 to 1.85)          0.381
            Rebounds               3.01 (1.04 to 4.99)           0.64 (−1.42 to 2.70)      2.37 (−1.23 to 5.98)           0.195
   Of the six differences only two, both in the main seasons, have intervals that exclude zero; none does in the earlier seasons.
   The two groups of cases overlap: in the main seasons 973 cases have wreb > 0 and 797 have wast < 0, 355 both (36% and
   45% of the two groups, 25% of their union; correlation of the two w −0.08); the main position group of the removed set
   is forward in 48% and 58% of them and centre in 22% and 12%, against 40% and 9% in all cases. The assist and rebound
   contrasts therefore cannot be read as two independent confirmations, although the two groups are far from the same cases.
   Main-season sample as in Table S66; team-clustered CR1 errors.




                                                                     61
Table S68: Teammates for whom position and role point in different directions (addendum P50, part B;
exploratory, with the balance gate fixed before the outcome was read). Cases with one removed player in
the main seasons.
           Diagnostic (retrospectively constructed pregame co-       Three position groups    Five listed positions
           variates only)
           Cases with one removed player                                               353                     353
           Cases with both kinds of teammate                                           280                     176
           Teams; absent players                                                    29; 78                  27; 51
           Teammate rows L; R                                                    544; 986                264; 908
           Standardised difference in reference minutes (R − L);                0.14; 0.15              0.30; 0.34
           within quintiles
           Gate (≥100 cases, ≥20 teams, difference <0.25)                              met                 not met
           Contrast R − L (three groups)                            Minutes (95% interval)                WCR p
           Main specification (3,594 rows)                            0.15 (−0.83 to 1.13)                   0.754
           With the partner share (3,460 rows)                        0.06 (−1.01 to 1.13)                   0.916
           With the height gap (3,594 rows)                           0.18 (−0.86 to 1.23)                   0.722
  L: a teammate of the absent player’s position group whose similarity is below the case median; R: a teammate of another
  group whose similarity is above it; the other teammates are the reference group. Extra minutes on the L and R indicators,
  reference minutes, headroom and own pregame status, case fixed effects, team-clustered CR1 errors and WCR bootstrap
  (Webb weights, 9,999 draws). Other standardised differences with three groups (R − L): capacity 0.11, headroom −0.04,
  listed Questionable or Doubtful 0.16, partner share 0.07, height gap 0.78. The five-position contrast was not estimated
  because the gate was not met. Raw mean extra minutes: L 1.31, R 1.30, other teammates 1.71.




                                                             62
Table S69: Coverage when teammates’ minutes may be cut (addendum P50, part C; exploratory; from the
retrospectively constructed reference rotations and pregame covariates). Cases by class, the share of the
summed shortfall that cuts close, and the smallest total cut that gives full coverage, in the main specification
and in one-at-a-time variants. Main seasons, 2,441 cases.
                                              Full         Full       Not full    Below   Share         Median share     C(1): median minutes
Variant                                   without cuts   with cuts   (capacity)    full   closed          (IQR)                (IQR); /L
Main specification                                957         571      913 (63)   1,484   0.432    0.61 (0.21 to 1.00)    9.3 (4.0 to 19.7); 0.20
Cut floor m j ≥ 0.5 b j                           957         470    1,014 (63)   1,484   0.359    0.45 (0.15 to 1.00)    6.8 (3.0 to 14.6); 0.16
Cut floor m j ≥ 0.75 b j                          957         340    1,144 (63)   1,484   0.273    0.29 (0.10 to 0.89)     4.9 (2.2 to 9.1); 0.11
Capacity: 95th percentile                       1,039         606      796 (36)   1,402   0.512    0.78 (0.30 to 1.00)   10.8 (4.3 to 20.8); 0.23
Capacity: most minutes before the cut-          1,111         687      643 (19)   1,330   0.604    1.00 (0.44 to 1.00)   11.4 (4.5 to 21.4); 0.24
off
Role rates not shrunk                           1,000         553     888 (63)    1,441   0.431    0.66 (0.20 to 1.00)    8.6 (3.4 to 17.5); 0.17
Role rates shrunk with 300 pseudo-                916         569     956 (63)    1,525   0.442    0.61 (0.22 to 1.00)    9.6 (4.6 to 20.2); 0.22
minutes
Questionable or Doubtful: not above b j           871         535    1,035 (63)   1,570   0.385    0.52 (0.14 to 1.00)   10.2 (4.4 to 19.2); 0.22

   κ(ρ) is the largest τ such that one allocation m of the retained players, with 0 ≤ m j ≤ u j , total minutes between B + τL
   and 240, every role k at least the retained players’ reference output plus τDk and a total cut ∑ j max(0, b j − m j ) ≤ ρ, exists;
   C(1) is the smallest total cut with τ = 1. κ(0) equals coverage (largest difference over the 2,441 cases 4.5×10−11 ); κ
   is non-decreasing and concave in ρ in every case and variant (no case violates either on the grid). Classes, given the
   retained players, their capacities and fixed role rates: full without cuts (coverage ≥ 1 − 10−7 ), full with cuts (coverage
   < 1 − 10−7 and κmax ≥ 1 − 10−7 ), not full even with unrestricted cuts (coverage and κmax both < 1 − 10−7 ; in parentheses:
   retained capacities summing to less than 240). Share closed: ∑(κmax − coverage)/ ∑(1 − coverage) over the cases below
   full coverage, recomputed in each variant (numerator and denominator). Median share: median over the same cases of
   (κmax − coverage)/(1 − coverage). C(1): in the cases full with cuts of that row, so the medians of different rows rest on
   different sets of cases (the fall from 9.3 to 6.8 and 4.9 minutes as the floor rises reflects which cases remain feasible, not a
   smaller cut for the same cases). Variants: the cases, the removed sets, b j , L and B are the same in every row. The floor rows
   set m j ≥ αb j ; the capacity rows replace the 90th percentile in u j = min(40, ·) by the 95th percentile or the maximum of
   the same history (at most the player’s last 20 games in the 365 days before the cutoff), keeping the cap of 40; the shrinkage
   rows set the prior weight of the role rates to 0 or 300 minutes instead of 100, which changes the rates and hence Dk and the
   retained players’ reference output; the last row bars teammates listed Questionable or Doubtful from playing more than b j .
   Mean κ in the cases below full coverage of the main specification: 0.836 at ρ/L = 0, 0.858 at ρ/L = 0.1, 0.894 at ρ/L = 0.5,
   0.904 at ρ/L = 1, 0.907 with unrestricted cuts. LPs solved with HiGHS (SciPy).




                                                                       63
Table S70: Does the required cut track actual rotations? (Addendum P50, part C, validation; specified before
it was run, with a reading fixed in advance.) Coefficient of C(1)/L (95% interval).
Outcome                                                  Unit, n                           C(1)/L                   WCR p        Specified
(a) Retained players’ cut minus the team-season          cases, 1,876                      4.44 (−1.65 to 10.53)    0.163          planned
baseline
(b) Teammates’ total loss of minutes, games without      absent-player team-seasons, 199   24.06 (14.66 to 33.45)   0.0008         planned
minus with the absent player
(a′ ) Retained players’ cut, team-season fixed effects   cases, 2,441                      5.44 (1.63 to 9.26)      0.0065         after (a)
(a′ ) the same, cases with a baseline                    cases, 1,876                      5.42 (0.46 to 10.37)     0.031          after (a)
(b) with team fixed effects                              199                               21.37 (12.34 to 30.41)   0.0011   after a review
(b) with season fixed effects                            199                               23.93 (14.74 to 33.11)   0.0007   after a review
   Key variable: C(1)/L in the cases full with cuts, 0 in the cases full without cuts, and 0 with an indicator in the cases not
   full even with cuts; controls L/240, the retained players’ summed headroom and their number; team-clustered CR1 errors,
   WCR bootstrap (Webb weights, 9,999 draws). (a): the outcome is ∑ j max(0, b j − mobs     j ) minus the team-season mean of
   the same quantity in games in which all three core players played, no supported player was listed Out and the team’s report
   block exists (the last condition added at run time); 846 such games in 77 team-seasons, 565 cases without one. The baseline
   spreads 240 reference minutes, the cases 240 − L, so the two are not comparable in structure (mean cut 46.9 and 27.9
   minutes). (b): the unit is an absent player in a team-season of the pair comparison of Section 5.2 of the paper; the outcome
   is ∑teammates max(0, −y), y the teammate’s mean minutes in games without minus with the absent player, and C(1)/L is
   averaged over the unit’s cases; it still rests on reference minutes, and units weigh equally whatever their number of cases.
   Reading fixed in advance: both coefficients positive and the interval of (a) excluding zero; not met. Incremental R2 of
   C(1)/L: 0.004 in (a′ ) within team-seasons, 0.045 in (b); the two are not directly comparable (the level of aggregation and the
   unit of analysis differ, and C(1)/L is non-zero in 571 cases only).




                                                                        64
S4    Planned tests, data corrections and deviations
The three tests of the paper, with their samples, fixed sensitivity analyses and pass rules (plan P3), were
committed to the project’s version-control repository on 21 September 2026, before any role measure was
related to an outcome. Position and height controls (P3 addendum A) and the hybrid sample (addendum
B) were added after the first P3 results, and the rule that a test is robust to measurement if it passes in
at least 8 of 10 alternative definitions (P6) was written after them. Table S71 lists every test with a pass
rule written before it was run, and its verdict on the final data. Everything else is exploratory. Most later
analyses were added as numbered addenda after the main results were known, each with its reading fixed
in a plan committed before it was run; the plans of the last addendum (P50, decided on 20 October 2026
after all other results were known) were written before each run in a working log with their SHA-256 hashes
and committed afterwards. The prospective replication on the 2026–27 season was registered on the Open
Science Framework on 30 September 2026, with a dated amendment on 19 October 2026.

Prior exposure. Final scores for all five seasons used here (2021–22 to 2025–26) had been read in an
earlier project by the same authors that used the same data sources (games from 2019–20 onwards) and
fitted models of player value and team production, and a separate study by the same authors compared
final scores with betting lines in these seasons, so the relationship between player value and results had
been examined. No relationship between role coverage (or role similarity) and any game outcome, in-game
behaviour or minutes had been computed before the plan for the three tests was frozen. An earlier pilot on
four teams (the hand-audited subset of Table S3) built the measure but fitted no outcome model.

Data corrections. A pre-submission audit found that the reconstructed rosters kept players whose con-
tracts had ended (correction R), counted transactions before same-day cutoffs (T) and kept ten-day contracts
that had ended without renewal (D); listed positions and heights are matched directly from the roster rows
of the reference site (M). Every result uses the final data, with R, T, D and M. Table S72 gives the planned
tests with the corrections one by one; the analysis record lists every number of the paper that differs between
the build on which the plans were run and the final data. A review after the analyses were frozen found
that the reason classes call “Coach’s Decision” medical and merge a bare “Not With Team” into personal.
Correction C gives both their own class (in the code, off by default, with a regression test on the report of 7
February 2023, 1 pm). In the selected six-hour reports of the five seasons it moves 25 of the 26,554 medical
Out rows to coach’s decision and 688 of the 1,160 personal Out rows to not with team (with the last report
stamped 90 minutes or more before tip-off, which fills the hybrid sample: 56 of 31,392 and 797 of 1,368). Of
the reclassified rows, 44 belong to core players at the six-hour cutoff and 53 at 90 minutes; all but one move
from personal to not with team, non-medical either way. One medically classified core-player row leaves
the medical class: Dinwiddie of Brooklyn on 7 February 2023, in an earlier-season case that stays a case
because Durant was ruled Out with a knee injury. No case or removed set changes, so the planned tests and
the estimates computed on cases and removed sets are unchanged. Analyses that take the medically absent
core players one at a time could see that row. The pair comparisons (Table S49 and those built on it) need at
least three games without the absent player, and Dinwiddie has one with Brooklyn, so they are unchanged.
In the spell windows (Table S60) his Brooklyn spell is that single game, which enters no window (W of 2, 3
or 5), so the estimates are unchanged, but the count of earlier-season spells in the table note would fall from
445 to 444. The tables were not rebuilt with C.




                                                      65
Table S71: Every planned test of a hypothesis with a pass rule, and its verdict (six-hour cutoff unless stated).
Coefficient (team-clustered SE) and two-sided p (for the last row, an exploratory validation, coefficient and
95% interval) on the final data (corrections R, T and D; positions with correction M); where the verdict on
the earlier build, on which the plans were run, was different, the last column gives it.
   Test                        Plan           Rule                              Result                           Verdict
   (1) Role similarity → ex-   P3             positive, p < 0.05                1.09 (0.18), p < 0.0001          passes
   tra minutes
   (2) Coverage → margin       P3             positive, p < 0.05                −0.99 (2.86), p = 0.73           does not pass
   (3) ck → role output        P3             positive, p < 0.05                0.054 (0.029), p = 0.070         does not pass;
                                                                                (WCR 0.071)                      earlier    build:
                                                                                                                 passed (0.065,
                                                                                                                 p = 0.038)
   Gate                        P3             continue if any test passes       through test (1)                 passed
   (1) with position and       P3 add. A      similarity positive, p < 0.05     0.89 (0.19), p < 0.0001;         passes
   height                                                                       82% retained
   Hybrid rule                 P3 add. B      hybrid verdict prevails if it     gate unchanged                   no change
                                              changes the gate
   Minute-allocation model     P4.1           beats    proportional    and      0.023 [−0.037,       0.081]      does not pass
                                              capacity-only MAE, interval       against proportional; 0.011
                                              excluding 0                       [−0.020, 0.045] against
                                                                                capacity-only
   Skill curve                 P4.2           slope negative, p < 0.05          −0.011, p = 0.29                 does not pass
   Replaced value → mar-       P4.2           positive, p < 0.05                0.52, p = 0.007 (bootstrap       passes; fragile
   gin (hybrid)                                                                 0.013)                           (Section 6.2 of
                                                                                                                 the paper)
   Robustness to measure-      P6             same sign and p < 0.05 in ≥       (1) 10 of 10; (2) 0 of 10; (3)   (1) robust; (3)
   ment                                       8 of 10 definitions               2 of 10                          not robust
   Wild bootstrap              P6             prevails if it crosses 0.05       crosses for no planned test      no change
   Replication (2021–22,       P12            original sign and p < 0.05        (1) 1.20, p < 0.0001; (2)        (1), (3) replicate,
   2022–23)                                                                     2.42, p = 0.47; (3) 0.100,       (3) also without
                                                                                p = 0.0006                       protocol cases;
                                                                                                                 (2) does not;
                                                                                                                 earlier     build:
                                                                                                                 (3) not without
                                                                                                                 protocol cases
                                                                                                                 (p = 0.073)
   Rebuild on the complete     P18            rebuild if ≥ 10% blocks re-       5.1% and 3.9% (data before       rebuild required
   series                                     covered or ≥ 2% Out lists         the complete series)
                                              changed
   Prospective 2026–27 test    P13,           test (1): registered rules,       prospective analysis pending     pending
                               amend-         primary with the corrected
                               ments 1–5;     code, secondary with the
                               registered     registered code, sensitivity
                               30      Sep    with reports strictly before
                               2026; dated    the cutoff; tests (2), (3): de-
                               amendment      scriptive only
                               (P48) filed
                               19       Oct
                               2026
   Validation of coverage      P50            both coefficients of C(1)/L       (a) 4.44 [−1.65, 10.53]; (b)     criterion not met
   with cuts (exploratory)                    positive and the interval of      24.1 [14.7, 33.5] (Table S70)
                                              (a) excluding zero


Typed from the tables of this supplement, not generated by the script. MAE: holdout mean absolute error in minutes, the im-
provement of the model over each baseline with a team-cluster bootstrap interval. Data checks with thresholds, the gold-standard
validation of P2 (Table S3) and the rebuild checks of P19, all passed. Every other analysis in the paper and this supplement is



                                                                66
exploratory or descriptive, with no pass rule; several later addenda fix the reading of a result in their plan, and the exploratory vali-
dation of addendum P50 has a criterion written before it was run, listed in the last row. The verdict of test (3) has a history: judged
on the six-hour sample, as the plan requires, rather than on the hybrid sample, it failed before the complete series and passed on the
complete series, the earlier build (Section S4, deviations 5 and 8); with the rosters corrected it does not pass, on the intermediate
build of addendum P46 (0.055, p = 0.071) or on the final data (addendum P47; Table S72).


Deviations that bear on the planned tests.
   1. Data repair after the first P3 run. The first P3 results used a parse of the injury reports from the
      authors’ earlier work that had lost Charlotte’s blocks from 2023–24 onward and some other blocks.
      We re-parsed every report with our own parser and reran all tests with unchanged specifications. The
      first run gave the same gate verdict (test (1) passed; tests (2) and (3) did not).
   2. Hybrid sample (addendum B) was added after the first P3 results were known, to fill team-games
      whose report had not been filed at the six-hour cutoff.
   3. Per-minute rate response. P3 specified, for each role separately, the model of test (1) (case fixed
      effects, reference minutes, headroom) with a retained player’s change in his per-minute rate of that
      role as the outcome and the role pressure of the removed set as the key variable. Role pressure varies
      by case and role but not across the players of a case, so within each role’s regression it is absorbed by
      the case effects and the planned coefficient is not identified. A regression stacked over the three roles
      with case and role effects would be identified, but it was not specified and was not run; the pooled
      specification with role indicators and no case effects (Table S4) is reported instead, as descriptive
      evidence.
   4. P4.2 amendment. Before any P4.2 result, the efficiency measure in the skill curve was changed to
      true shooting, because per-minute efficiency rises mechanically with shot volume, and the quality-
      adjusted replacement value was replaced by replaced value plus a usage gap.
   5. Verdict on test (3). We first judged test (3) on the hybrid sample. A separate check pointed out that
      addendum B keeps the six-hour sample primary when the gate verdict agrees, so test (3) is judged
      on the six-hour sample. On the version of the data before the complete series it did not pass there
      (p = 0.062); on the complete series, the earlier build, it passed (p = 0.038); on the final data it does
      not (p = 0.070; addendum P47).
   6. P4.4 not reported. Probabilistic availability was computed as a descriptive exercise. Its availabil-
      ity rates were estimated from whole seasons, including games after the prediction date, so they are
      unsuitable as predictors; they enter no model, test or reported result.
   7. Sample size. The P3 plan quoted 2,174 cases from the preliminary build. The repaired, header-
      timed build had 2,230 six-hour cases; the complete-series build (P19), the earlier build, 2,440; the
      intermediate build of P46 2,439; and the final data (P47) have 2,441.
   8. Complete report series (P18, P19). The version of the data before the complete series used about five
      reports per game day (2,632 reports over three seasons). The complete series recovers a report block
      for 5.1% of team-games (missing blocks fall from 14.1% to 9.0%), replaces the selected report with
      a later pre-cutoff one in 59% of the others (a median of three hours later) and changes the pregame
      Out list in 3.9% of team-games. Every table and test was rebuilt. Three verdicts at the 0.05 level
      changed: test (3) in the primary sample (p = 0.062 to 0.038; wild bootstrap 0.063 to 0.040); the ±0.5
      equivalence test in the three-season hybrid sample (0.045 to 0.052); and the stint-level model with
      opponent absences over five seasons (0.046 to 0.073). Among the checks, the number of measurement
      definitions in which test (3) is significant fell from 8 to 6 of 10, so test (3) no longer meets the
      robustness rule of plan P6; the season checks of test (3) in the six-hour sample moved from p between

                                                                  67
Table S72: The planned tests with the data corrections (addenda P44 and P47; data corrections and a sen-
sitivity analysis made after all other results were known, with the reading fixed in the plans). Coefficient
[95% interval] unless stated.
    Data                Cases Allocation       Role output: ck     p (WCR     ck with the   Margin, per 0.1 Coverage:
                                                                   p)         benchmark     of coverage     median;
                                                                              (p)                           share at 1
      Primary sample, six-hour cutoff, 2023–24 to 2025–26 (margin: 95% interval)
    Earlier build         2,440 1.10           0.065                 0.038      −0.040      −0.15             0.961;
                                [0.74, 1.46]   [0.004, 0.126]        (0.040)    (0.282)     [−0.77, 0.47] 41.8%
    R: rosters            2,440 1.06           0.055                 0.071      −0.053      −0.15             0.954;
                                [0.69, 1.44]   [−0.005, 0.114] (0.072)          (0.147)     [−0.74, 0.44] 39.7%
    T: transaction dates 2,439 1.11            0.065                 0.038      −0.040      −0.15             0.961;
                                [0.75, 1.47]   [0.004, 0.126]        (0.040)    (0.289)     [−0.77, 0.48] 41.7%
    R and T               2,439 1.07           0.055                 0.071      −0.053      −0.14             0.954;
    (addendum P46)              [0.70, 1.45]   [−0.005, 0.114] (0.071)          (0.152)     [−0.73, 0.45] 39.6%
    S: reports strictly   2,302 1.04           0.064                 0.042      −0.047      −0.13             0.963;
    before the cutoff           [0.68, 1.39]   [0.003, 0.126]        (0.043)    (0.211)     [−0.79, 0.53] 42.0%
    R, S and T            2,301 0.99           0.053                 0.083      −0.063      −0.13             0.955;
                                [0.63, 1.36]   [−0.007, 0.113] (0.084)          (0.090)     [−0.77, 0.51] 39.8%
    R, T and D: final     2,441 1.09           0.054                 0.070      −0.053      −0.10             0.951;
    data                        [0.72, 1.46]   [−0.005, 0.114] (0.071)          (0.152)     [−0.68, 0.49] 39.2%
    R, S, T and D         2,302 1.01           0.052                 0.085      −0.064      −0.08             0.953;
                                [0.65, 1.37]   [−0.008, 0.112] (0.086)          (0.087)     [−0.71, 0.55] 39.5%
      Hybrid sample, 2023–24 to 2025–26 (margin: 90% interval, as in the equivalence test)
    Earlier build         2,711 1.12           0.059                 0.047      −0.037      −0.05             0.957;
                                [0.78, 1.46]   [0.001, 0.118]        (0.046)    (0.305)     [−0.51, 0.40] 40.8%
    R and T               2,711 1.09           0.050                 0.085      −0.050      −0.05             0.951;
                                [0.73, 1.45]   [−0.007, 0.107] (0.089)          (0.173)     [−0.49, 0.38] 38.8%
    R, T and D: final     2,713 1.11           0.050                 0.086      −0.050      −0.01             0.949;
    data                        [0.76, 1.47]   [−0.008, 0.107] (0.089)          (0.174)     [−0.44, 0.43] 38.4%
    R, S, T and D         2,684 1.08           0.057                 0.053      −0.050      −0.02             0.950;
                                [0.73, 1.43]   [−0.001, 0.115] (0.058)          (0.187)     [−0.48, 0.45] 38.8%
      Earlier seasons, 2021–22 and 2022–23, six-hour cutoff (margin: 90% interval, as in the equivalence test)
    Earlier build         1,465 1.02           0.083                 0.006      0.044       0.26              0.937;
                                [0.35, 1.69]   [0.026, 0.139]        (0.007)    (0.254)     [−0.28, 0.80] 36.1%
    R and T               1,466 1.17           0.097                 0.0010     0.063       0.21              0.924;
                                [0.63, 1.70]   [0.043, 0.151]        (0.002)    (0.103)     [−0.35, 0.77] 35.5%
    R, T and D: final     1,466 1.20           0.100                 0.0006     0.068       0.24              0.920;
    data                        [0.67, 1.72]   [0.047, 0.153]        (0.001)    (0.082)     [−0.31, 0.80] 34.4%
    R, S, T and D         1,401 1.20           0.098                 0.001      0.073       0.20              0.923;
                                [0.68, 1.73]   [0.042, 0.153]        (0.002)    (0.072)     [−0.37, 0.77] 34.8%
      Five seasons, six-hour cutoff (margin: 90% interval, as in the equivalence test)
    Earlier build         3,905 1.08           0.068                 0.003      −0.006      0.03              0.952;
                                [0.75, 1.40]   [0.026, 0.109]        (0.003)    (0.839)     [−0.34, 0.41] 39.6%
    R and T               3,905 1.11           0.069                 0.002      −0.004      0.01              0.944;
                                [0.83, 1.40]   [0.027, 0.112]        (0.003)    (0.906)     [−0.36, 0.38] 38.1%
    R, T and D: final     3,907 1.14           0.070                 0.002      −0.002      0.05              0.942;
    data                        [0.85, 1.43]   [0.029, 0.112]        (0.002)    (0.954)     [−0.32, 0.42] 37.4%
    R, S, T and D         3,703 1.10           0.067                 0.004      −0.007      0.06              0.943;
                                [0.81, 1.38]   [0.023, 0.111]        (0.005)    (0.836)     [−0.33, 0.44] 37.7%




                                                             68
Note to Table S72. Each variant rebuilds the analysis tables with the stated corrections (a switch in the build code, off in the
earlier build) and reruns the three planned tests as specified in P3 and test (3) with the proportional-reallocation benchmark
as in Table S30. R, rosters: the player-movement log has no contract expirations, so a player whose last tie to a team came
from an earlier season (seasons change on 1 July) stayed on its roster. With R he stays on it only if his first record of the
current season (a box-score row, a listing on a selected injury report, a signing or trade into a team, or a waiver) is a box-score
row or a listing for that team, or a waiver; if that record joins him to a team (also re-signing with the same team after the
cutoff) or is a record for another team, or if the season has no record of him, his contract did not carry over. Records after the
cutoff are used: they supply contract information that the teams had before tip-off and the log lacks. Ten-day contracts are
handled by D. T, transaction dates: transactions are stamped at 23:59 US Eastern time on their date instead of 12:00 UTC, so
a transaction of the game day is not known before a same-day cutoff and a box-score row of the same day no longer follows
a waiver or a trade. S, reports strictly before the cutoff: only reports whose header time is strictly before the cutoff are used
(at the six-hour and the 90-minute cutoff), reselected from the complete series; the header time only bounds publication from
below. D, ten-day contracts (addendum P47): a ten-day contract ends ten days after the signing or after the team’s third game
of the same season, whichever is later; unless the player has another transaction or plays for another team before the day after
that, he leaves the team at 23:59 US Eastern time on that day. R, T and D, all corrections of data errors, are the final data that
the paper and this supplement use; S and the variants with S are sensitivity analyses of the time definition. R and T alone
were the corrected build of addendum P46. R removes 1,609 roster rows with reference minutes in 1,040 team-games of the
primary seasons, 87 player-team-seasons with a median of 21 team-games each; 380 of the 2,440 primary cases are affected
(on average 15.3 reference minutes removed per affected case), and 168 of the 1,465 cases of the earlier seasons. In 1,257
of the 2,441 primary cases of the final data (51.5%) the selected report’s header time equals the cutoff. Hand-audited subset
(Table S3; six-hour, 2023–24): with R and T, pipeline rotation players in the audited roster 97.9% of 2,596, against 97.5% of
2,609 in the earlier build, and audited rotation players found by the pipeline 99.88% of 2,544, against 99.96% of 2,544 (final
data: 98.8% of 2,573 and 99.88% of 2,544, Table S3); with S, Out precision 100.00% of 701, against 95.8% of 732: the 31
Out disagreements of the earlier build disappear (with R, S, T and D: 100.00% of 703; final data: 95.8% of 734). The row
on an identical three-player reference core is not reported for R and T: the validation script (validate_gold.py) then
broke ties in reference minutes with an unstable sort; addendum P46 made it break them by player identifier, as the pipeline
does, which leaves the earlier build unchanged and gives 98.9% for R and T and 98.9% of 184 on the final data (Table 1 of
the paper). The row of the earlier build reproduces the planned tests as run on it, and the row of the final data reproduces the
paper. Allocation: p < 0.0001 and WCR p ≤0.0001 in every row of the primary sample. WCR p of ck with the benchmark
in the primary sample, in the order of the rows: 0.297, 0.163, 0.307, 0.171, 0.227, 0.110, 0.170, 0.107. Team-clustered CR1
errors, t with 29 degrees of freedom; WCR p with Webb weights, 9,999 draws, with the seeds of addenda P6 and P12 (of
P24 for the benchmark model). The paper and the other tables of this supplement use the final data (R, T and D). Besides the
planned role-output test, seven significance judgements of the paper differ between the earlier build and the final data (earlier;
final): the role-output sensitivity sample without full coverage (0.062, p = 0.047; 0.049, p = 0.093); the real-minus-placebo
coverage slope with unchanged top three, the planned inputs and the benchmark (−0.092, p = 0.055; −0.125, p = 0.011);
the pair model with absent-player effects, position pairings and the height gap (Table 3 of the paper, row 12: 0.79, p = 0.031;
0.60, p = 0.069); the earlier seasons’ pairs with the similarity of Section 5.2 of the paper (1.34, p = 0.019; 0.96, p = 0.087);
the allocation test in 2022–23 alone (0.73, p = 0.114; 1.06, p = 0.001); role output in the earlier seasons without the 177
COVID-19 protocol cases (0.065, p = 0.073; 0.089, p = 0.009); and role output with reports strictly before the cutoff (0.064,
p = 0.042; 0.052, p = 0.085). With standard errors clustered by game the role-output test is significant on both builds
(p = 0.025 and 0.046), so on the final data, unlike on the earlier build, clustering by game changes its verdict.




                                                               69
      0.052 and 0.069 to below 0.05; and in the hybrid sample the bootstrap p of test (3) with season fixed
      effects moved from 0.029 to 0.057. Table S1 lists the tests, equivalence tests and stint-level models
      under both versions.
   9. P3 market regression not reported. P3 specified a descriptive regression of the margin against the
      closing spread on coverage for 2025–26. The frozen code computed it from the start, but drafts before
      addendum P24 did not report it; it is reported in the note to Table S33 (−1.28, p = 0.77, 808 six-hour
      cases).


S5     Reproduction and data availability
The repository contains the code for every stage, the unit tests, the analysis plans with their commit history,
and a step-by-step guide that rebuilds every table and figure from the raw inputs. The raw inputs are the
official NBA injury-report PDFs, which remain public at the league’s address; ESPN game summaries
(scores, box scores and closing spreads); and the league’s player-movement log.
    The terms of use of these sources restrict redistribution of their data. We therefore release: all code; a
manifest of every source file with its identifier and SHA-256 hash, so that users can verify that the files they
download match ours; and four derived tables of our own measures, on the final data: by case, by retained
player and case, by pair of a teammate and an absent core player, and by case and role (contents below).
Other player-level tables are rebuilt by the user from the public sources with the released code. This is not
legal advice; users are responsible for complying with the sources’ terms.

What has been reproduced on the final data. Three levels are distinct. (i) From the released derived
tables, reproduce_tables.py reproduces Tables 2 and 3 of the paper and the main estimates (172
of 172 values within 10−6 ) on the lead author’s machine and from the released code package; this checks
the regressions, not how the tables were built. (ii) From the same cached raw inputs on a second machine,
the six-hour analysis tables of 2021–22 to 2025–26 rebuilt on the lead author’s machine are byte for byte
identical to those of the cloud build (addendum P47), and P33 part A, P45 (P47) and P34 part B (P48) rerun
there give identical values; this checks that the build is deterministic given the cache, not the cache itself.
(iii) A rebuild from the raw sources in a clean directory was made for earlier versions of the data only (P30,
and P44 from the inputs of the earlier build; table below), not for the final data. The agreement of 172 of 172
values therefore does not mean that the chain from the raw sources to the final data has been independently
rebuilt.

Counts quoted in Section 2.1 of the paper. The complete series holds 23,485 report files, from 18 Octo-
ber 2021 to 12 April 2026, all parsed without error and each with a printed header time; reports are hourly
and, from 22 December 2025, every 15 minutes. It covers each game day from midnight (US Eastern) to 90
minutes before the day’s last tip-off, where collection stopped; the 1,787 later reports of those days held on
the league’s server cannot meet a cutoff six hours or 90 minutes before a game’s own tip-off and were not
used. Hour-only file names are 30 minutes earlier than the printed time (14,891 files), 45 minutes earlier for
57 files from 19 to 22 December 2025, and equal to it for one file of a daylight-saving change day; of the
8,536 names with minutes, 8,535 agree with the printed time. The comparison with a separate parse from
the authors’ earlier work, made with other code (the same Out list in 99.8% of the 5,978 team-games both
covered) was made on the earlier version of the data, for the three main seasons. The game summaries cover
8,292 games from 2019–20 to 2025–26, and the player-movement log has 6,716 entries.




                                                      70
External data. One table is not derived from the sources above: the head-coach spells used in Table S28
were compiled by the authors from public encyclopaedia pages (not derived by the pipeline), one row per
spell with its source and the date it was read. It is released with the code.

Public derived tables. The four released tables (league/public/) are on the final data, with the listed
positions of correction M. The case table holds, for every case of the six-hour and hybrid samples and of the
replication seasons (2,441, 2,713 and 1,466 rows), the game and team identifiers, season, home indicator,
coverage, removed minute share, lost value, strength and rest differences and the final margin. The player-
case table holds the frozen rows of test (1) in the primary and replication seasons (28,118 and 16,583 rows),
with the three-group and five-position listed positions, the pairing of the player’s position with the removed
set’s, the shares of the removed reference minutes at each listed position, the height gap, the substitution-
partner share, an indicator of cases in which one listed position is removed, and the flags of the samples of
Table 3 of the paper. The pair table holds the 2,653 pairs of Section 5.2 of the paper and the 1,661 of the
replication seasons, with similarity before the absence; the case-role table the 11,721 case-roles of test (3)
(7,323 primary and 4,398 replication), with ck , the benchmark, role output and its ten-game baseline, the
removed minute share and the role. The script league/public/reproduce_tables.py (numpy
and pandas only) reproduces from these tables alone Tables 2 and 3 of the paper and the main estimates
of the allocation test (1.092), Section 5.2 (1.542) and the margin test (−0.990, p = 0.732; hybrid −0.077,
p = 0.976); with -check results/final it compares 172 values with the result files, and all 172
agree to within 10−6 .

Running addendum P50. The scripts are in league/scripts/p50/, whose README gives the
order and arguments. Step 0 rebuilds, from the cache of the final build, the six-hour tables of 2021–22 to
2025–26 and the variants with the 95th percentile and the maximum of recent minutes as capacity and with
prior weights of 0 and 300 for the role rates (MEASURE_VARIANTS in league/src/build.py), and
checks them against the released tables; parts A and B then need these tables and the released player-case
table, part C and its validation the tables, the variants and, for the validation only, actual minutes; the last
step writes Tables S66 to S70 from the stored results (results/final/p50/). The released derived
tables alone do not suffice: they hold neither the retained players’ reference minutes, capacities and rates
nor the variants.

Inputs not built by the released code. Listed position and height come from files com-
piled, outside the released code, from Basketball-Reference team-season roster pages (run identifier
580c44bb...): the roster rows of those pages (player_bio_bref_source_rows.csv, SHA-
256 97a844de...260f44d), which correction M matches to ESPN players by team and season with
the released code (league/src/bref_positions.py; Section S1), and, for the player-seasons it
leaves unmatched, the player-by-season table of the same run (player_bio_player_season.csv,
330458c8...f558234, with player_bio_latest_snapshot.csv, 6b77fe71...2fee74),
the only source before correction M; the code reads only the listed position and height of each player in
each season. The positions and the height gap are columns of the released player-case table, so the position
controls of Table 3 of the paper can be reproduced from the release, although the source files are compiled
outside the released code. The lineup stints (241,913 rows; SHA-256 b883b616...e097) are built by
the released code from the play-by-play of the game summaries (addendum P16); they do not depend on the
rosters and are the same on every build.




                                                      71
S6     Further detail on Sections 5.3 and 6.3 of the paper
The paper reports these analyses in brief; this section gives the full account it was shortened from.

Position, height, past substitution and player effects (Section 5.3 of the paper). Similarity might sim-
ply recode listed position or the absent players’ usual backups. Two kinds of evidence bear on this: how the
coefficient changes when position controls are added within one sample, and whether what remains is the
same across designs. In the allocation test, three position groups (guard, forward, centre; the removed set’s
position is the group holding most of its reference minutes) and the height gap leave 82% of the coefficient
(Table S6), and on the common sample of Table 3 of the paper (rows 1 to 7) 72% with a substitution-partner
share added: how often the teammate was on court during an absent player’s bench possessions in his recent
games, which predicts extra minutes strongly (1.59 minutes per within-case standard deviation, against 0.64
for similarity; Table S35) but is nearly uncorrelated with similarity (0.07). Indicators for every pairing of
the teammate’s five listed positions with the removed set’s main position (the one with most of its reference
minutes) leave 63% (0.69, SE 0.17; 95% interval 0.35 to 1.04); the share of the removed reference minutes at
each listed position, interacted with the teammate’s position, which also describes the other removed players
(3.0 per case on average), leaves 45% (0.49, SE 0.17; 0.15 to 0.84), or 53% with player effects (Table S59).
In the 455 cases whose removed players share one listed position (340 with a single removed player; Table
S56), the pairings and the height gap take the coefficient from 1.05 (SE 0.32) to 0.37 (SE 0.40; −0.44 to
1.18), and adding the partner share to 0.20 (SE 0.41; −0.64 to 1.04), and in the 1,278 pairs described next
from 1.01 (SE 0.32) to −0.02 (SE 0.34; −0.72 to 0.67).
     In the pair comparison of Section 5.2 of the paper each pair has one absent player and one teammate, so
the 25 pairings of the two players’ listed positions and their height gap describe listed position completely;
we added them to the model with absent-player and teammate effects, with similarity from the two players’
profiles at the last game before the absent player’s first absence with that team in that season (Table S57).
This uses 1,278 pairs of 541 teammates with such a game, both players’ positions and heights and two or
more pairs each, a selected subset (34 of the 199 absent-player team-seasons have no such game); on them
the model of Section 5.2 of the paper gives 1.30 (SE 0.30), against 1.23 on its 2,168 pairs.
     Across designs the answer is not stable. Over all cases a distinguishable part remains with every descrip-
tion of position; in the one-position cases and in the pair model with absent-player and teammate effects,
where listed position is described completely, no additional association is detected (similarity coefficient in
one-position cases minus that in the others: −0.56, SE 0.45, p = 0.22), but one of 0.54 minutes per unit
of similarity (0.3 minutes per standard deviation, about half the 0.63 of Section 5.1 of the paper; the size
the plan of the pair analysis called meaningful) cannot be excluded. Other pair specifications differ: with
absent-player effects only, 0.60 (SE 0.32; −0.05 to 1.25) on these pairs and 0.72 (SE 0.26; 0.19 to 1.25) on
all 1,788 pairs with similarity before the absence; with one same-position indicator in place of the pairings,
0.40 (SE 0.33); 0.04 (SE 0.60) in the 664 pairs in which that core player was the only one out; 0.26 (SE
0.36) with the similarity of Section 5.2 of the paper. In the earlier seasons the pair model gives 0.85 (Table 3
of the paper, row 13), and 0.96 (SE 0.54) with the similarity of Section 5.2 of the paper (Table S63). The
cases and the pairs differ in more than the position control (unit, sample, outcome, timing of similarity, fixed
effects), so the gap between them is not the effect of a more complete control alone; within the pairs, too,
the fixed effects and the sample matter. Every share is approximate (controls and similarity are measured
with error), and listed position is not actual role; in 44% of the pairs the teammate’s profile also includes
earlier-season games that the absent player missed (Table S57).
     Case fixed effects absorb who is absent, but not a teammate’s place in the rotation: a player may be the
usual stand-in and also resemble the players he stands in for. With player-by-team-by-season fixed effects
the coefficient rests on changes in the same player’s similarity across his cases; 98% of that variation lies
between cases with different removed sets (Table S56). With the controls of the allocation test it is 1.38 (SE

                                                      72
0.21; 95% interval 0.95 to 1.81) on all primary cases (Table S48; 1.40 on the common sample of Table 3
of the paper), and 0.93 (SE 0.23) with every position pairing, the height gap and the partner share (Table 3
of the paper, row 6). A place in the rotation that is the same in all of a player’s cases in a season therefore
does not account for the association. Player effects do not absorb his being the regular replacement of one
particular teammate, which the partner share addresses only in part, or a change of place that coincides with
a change in who is absent.
    Which roles carry the gradient? Similarity (Section 3.3 of the paper) is a sum over the three roles of
the product of the teammate’s and the removed set’s standardised rates, each divided by the norm of its
profile. Entered jointly as separate regressors, with the teammate’s own scaled rates as controls, the three
products give 0.75 minutes per unit for three-point attempts (95% interval 0.02 to 1.47), 1.01 for assists
(0.26 to 1.75) and 1.76 for rebounds (1.12 to 2.40); equality of the three is not rejected (F(2, 29) = 2.92,
p = 0.070; wild bootstrap p = 0.079; earlier seasons p = 0.16), so the ordering is descriptive. Split by the
sign of the absent players’ rates (exploratory, uncorrected), the rebound and assist components come from
absences of players who rebound much and pass little, mostly forwards and centres (Table S67). With every
position pairing, the height gap, the partner share and own status they are 0.33, 0.62 and 1.03 (0.52 to 1.55).
A direct comparison asks which criterion the allocation follows when the two disagree. In the 280 cases
with one removed player that contain both a teammate of his position group with below-median similarity
and one of another group with above-median similarity, the second plays 0.15 minutes more than the first
(−0.83 to 1.13). The interval is compatible with differences in either direction as large as the 0.63 minutes
per standard deviation of Section 5.1 of the paper, so this design cannot tell which criterion the allocation
follows when they disagree; with five listed positions the two kinds of teammate were not balanced and the
comparison was not estimated. Both analyses are exploratory (Tables S66 and S68).

Coverage when teammates’ minutes may be cut (Section 6.3 of the paper). Coverage keeps every
retained player at or above his reference minutes (Section 3.4 of the paper), although 29.5% of retained
players played fewer. In an exploratory extension (Section 4 of the paper) we let a retained player’s minutes
m j fall below b j , with 0 ≤ m j ≤ u j , and bound the total cut ∑ j max(0, b j − m j ) by a budget ρ; to restore
a fraction τ of the removed minutes and roles, total minutes must lie between B + τL and 240, where B is
the retained players’ reference minutes, and each role must reach the retained players’ reference output plus
τDk . Let κ(ρ) be the largest attainable τ, and C(1) the smallest total cut that gives full coverage. κ(0)
equals coverage, and κ is non-decreasing and concave in ρ. Given the retained players, their capacities and
fixed role rates, 39.2% of cases are fully covered without cuts, 23.4% become fully covered once cuts are
allowed, and 37.4% are not fully covered even with unrestricted cuts, mostly because no allocation restores
every role at once. Of the summed shortfall ∑(1 − coverage) over the 1,484 cases below full coverage, 43%
is closed by allowing cuts. Recomputed under one-at-a-time changes of the cut floor, the capacity rule, rate
shrinkage and the treatment of teammates listed Questionable or Doubtful, this share ranges from 27% to
60%; it is most sensitive to capacity and to how deep the cuts may go (Table S69 and Figure S4). In the 571
cases fully covered only with cuts, the smallest total cut has a median of 9.3 minutes, and its ratio to the
removed minutes a median of 20%. Whether the required cut tracks actual rotations is not settled. Of two
planned comparisons, the one whose outcome does not use reference minutes is positive (the teammates’
total loss of minutes in games without versus with a given absent player, 24.1 minutes per unit of C(1)/L,
14.7 to 33.5; 21.4 and 23.9 with team or season effects; C(1)/L itself rests on reference minutes). The other,
the retained players’ cut against a team-season baseline, is imprecise (4.44, −1.65 to 10.53), so the criterion
fixed in advance (both positive and the baseline comparison’s interval excluding zero) is not met; its baseline
is moreover not comparable in structure, since in the baseline games the retained players’ reference minutes
sum to 240 and in the cases to 240 − L. A behavioural counterpart of the cut is therefore not established
(exploratory; Table S70).


                                                       73
