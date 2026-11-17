<!-- source: library/preprints/arXiv/2026/2026 - Who is who injury rates between players and within each player in professional team sports - Ricou et al.pdf -->
<!-- item: https://arxiv.org/abs/2608.11228 -->
<!-- authors: Gustavo Pedro Ricou, Nicholas Mahony -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-17; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Who is who: injury rates between players and within each player in professional team sports

                                            Who is who: injury rates between players and within each player
                                                              in professional team sports
                                                                   Gustavo Pedro Ricou1 and Nicholas Mahony2
                                                  1 School of Computer Science and Statistics, Trinity College Dublin, Dublin, Ireland
                                                  2 Discipline of Anatomy, School of Medicine, Trinity College Dublin, Dublin, Ireland




                                           Corresponding author Gustavo Pedro Ricou, School of Computer Science and Statistics, Trinity
                                           College Dublin, Dublin, Ireland. Email: pedrorig@tcd.ie.
                                           ORCID https://orcid.org/0009-0001-4196-7213
                                           Word count 3000 words of main text, headings included; abstract 250 words.
                                           Keywords (MeSH) Athletic Injuries; Incidence; Workload; Risk Factors; Recurrence; Team Sports;
arXiv:2608.11228v4 [stat.AP] 15 Nov 2026




                                           Soccer; Healthy Worker Effect




                                                                                           1
                                                 Abstract
     Objective Per-hour injury rates inform rest and match calendars. We measured how injury
     rates differ between players and with recent load.
     Methods Observational study of public match records in nine team sports. Injury records
     covered 22 573 players in six sports (748 women, in one league). In football, injuries were injury-
     coded substitutions. A heavy week had a full match or more within seven days; a longer-gap
     week followed an 8-to-13-day gap. We compared heavy weeks across players and within each
     player.
     Results As expected, players’ usual injury rates differed: between two players picked at random,
     the higher was typically 1.83 times the lower. As known, two or more injuries of 28 days or more
     in three years went with 1.3 to 1.7 times the rate in five sports. As expected, within the same
     player, playing time rose less after a heavy week than across players, whether or not a replaced
     player may return. As expected, simulations with no effect of load read heavy weeks as riskier
     within each player’s season in the usual comparisons, because injuries lower later load. Over
     whole seasons, they read them as 1.05 to 2.19 times as risky in all six sports.
     Conclusion Researchers and injury surveillance programmes who compare each player’s heavy
     weeks with the same player’s longer-gap weeks should check that comparison by simulation. Per-
     hour rates that compare players mix recent load with who carries it. So club medical staff can
     read lower injury rates among their most-used players as a sign of who plays.


What is already known on this topic
   • Players differ in injury risk beyond their load and their previous injuries; those who play most
     can look safer, because players at lower risk play more.

   • Per-hour injury rates assume that the hours a player records do not depend on the load under
     study.


What this study adds
   • In every sport with injury records, simulations with no effect of load read heavy weeks over
     whole seasons as 1.05 to 2.19 times as risky in the usual within-player comparisons.


How this study might affect research, practice or policy
   • Researchers and injury surveillance programmes should check by simulation any comparison
     of a player’s heavy weeks with the same player’s longer-gap weeks and, where they infer injury
     from team sheets, should not read a missed start in the next match as injury.

   • Club medical staff can read a lower injury rate among their most-used players as a sign of who
     plays, rather than of a safe load.


Introduction
Injury rates inform which players medical teams rest and how many matches players play.[1–3]
Both uses assume that recent load, meaning last week’s play, drives injury risk. Yet some players
are injured more often than others, beyond their load and their previous injuries.[4–6] A previous
injury, for example, is a strong risk factor for the next one.[7] Suppose those who play most are also
injured least. Then injury rates that compare players will make a heavy week, a full match or more
in the previous week, look safe.
    In football, injuries are counted per 1000 hours of play,[8–10] as in studies of fixture congestion
and recent load.[6, 11–15] These studies assume that the hours a player records stay the same,
whatever the load. But players play more minutes after a heavy week.[16, 17] We call this rise the
workload gradient.


                                                     2
   A per-hour rate divides injuries by the minutes played, called the denominator. After a heavy
week the minutes rise, for one of two reasons. A heavy week might change how long a player plays.
Or the players with a heavy week might be the regular starters, picked every week and kept on
the field. We call this choice team selection. Which reason holds decides whether a per-hour rate
compares loads or players.
   In medicine, comparing groups of people who were picked in some way can mislead.[18] Others
have asked how much recorded playing time comes from team selection.[1, 19]
   In nine team sports, we asked how much players differ in their usual injury rate. We then asked
whether comparing players makes heavy weeks look safer than comparing each player with their own
weeks.


Methods
Design and data
This observational study of public match records from nine team sports (Table 1) follows the
STROBE guideline.[20] The records of men’s football come from Transfermarkt, which we call the
provider (Supplementary Section S2). A league sample is one league’s seasons under one substitution
limit.[21]

Recent match load
Recent match load, or recent load, is a player’s league minutes in the previous seven days, in full
matches of 90 minutes. A player with a full match or more was loaded: a heavy week. A player with
no minutes was rested. A longer-gap week is a rested week: the club’s previous league match came 8
to 13 days earlier. Then the fixture list set the rest, rather than the coach or an injury (Figure 1C).

Injury records
A substitution is injury-coded when the match report gives injury as its reason (Supplementary
Section S3). We also counted confirmed injuries: injury-coded substitutions followed by an absence
in the provider’s public injury list. Such an absence is a sign of real injury. In the other sports, an
injury is each league’s own record of an absence (Supplementary Section S12).
    A statistical model gave each player their own usual injury rate, the baseline rate. It takes in
everything that stays the same about a player, such as position, usual load and how the club records
injuries (Supplementary Section S11). In five sports, the records also give each player’s injury history
(Supplementary Section S12).

The injury comparison
We counted injury-coded substitutions per 1000 starter hours, the hours played as a starter. We
compared heavy weeks with longer-gap weeks in two ways. Across starters, we compared different
starters’ weeks within each league-season (Mantel–Haenszel). Within each starter, we compared each
starter’s heavy weeks with the same starter’s longer-gap weeks in the same league-season (conditional
Poisson regression). We also made both comparisons against longer-gap weeks after a completed
match, in which the starter played all 90 recorded minutes.
    Last, we set starts two to three days after the club’s previous match in any competition, a short
gap, against those six to seven days after it. We repeated this after a completed match. The model
held other gaps and the starter’s minutes in that match (Supplementary Section S6).

Statistical analysis and pre-set criteria
The statistics follow the CHAMP statement.[22] We split the workload gradient exactly into two
parts: one comes from who starts, the other from starters and substitutes playing longer.[23] The


                                                   3
within-player slope is the gradient measured within each starter. We set two criteria before testing
them, on the within-player slope and on keeping loaded starters on (Supplementary Section S4).
Every other analysis, the injury comparison among them, is exploratory: it finds leads to check.
A simulation with the real calendars and appearances, and no effect of load, checked each injury
comparison (Supplementary Sections S6 and S9). Only comparisons that it read within two per cent
of one, with 95% intervals that held one at least 90% of the time, carry a sentence here. Comparisons
that missed this rule are printed beside their simulated values and read against them. We chose
the comparison within each starter and season after seeing the results of similar comparisons. We
added confirmed injuries, the reference after a completed match and its use for short gaps later,
after earlier runs had given their estimates. The simulation’s rule, fixed before it ran, judged each
one. Each result is read as if it were the only comparison. We wrote the analysis scripts with an AI
assistant and checked them against hand-worked tests.

How to read the results
Most results are ratios of two injury rates. Each ratio comes with a range, its 95% confidence interval
(95% CI). The true value is likely to be in this range. When the whole range lies above or below
one, the difference is clear: for heavy weeks, riskier or safer. When it includes one, there is no clear
difference: the two rates are similar. The range then shows how much higher or lower the rate may
still be.

Equity, diversity, and inclusion statement
The league samples include women’s football, Australian rules, basketball and cricket. The world-
wide survey of first-tier football leagues (Table 1) covers men’s leagues only. Women’s injury records
come from one league, the WNBA: 748 of the 22 573 players with injury records. The two authors
work at one European university, in statistics and medicine.

Patient and public involvement
Patients or the public were not involved in the design, conduct, reporting or dissemination plans of
this research.


Results
Players differed widely in their usual injury rate
As expected, players differed in their usual injury rate. Between two players picked at random from
one season, the higher baseline rate was typically 1.83 times the lower, over all 11 player groups
(Figure 1A). In football it was larger on confirmed injuries (1.94).
    As expected, injury history also marked higher risk. Players with two or more injuries of 28 days
or more in the previous three years had 1.3 to 1.7 times the injury rate of the others. This held in
every sport with injury histories (Figure 1B). Yet, as at one Australian football club,[4] most of the
difference between two players lay outside that history, as expected for a marker this modest or rare.
Even the fullest injury record made that difference at most 10.4% smaller (Supplementary Section
S12).

Compared like with like, a full match in the previous week carried similar injury
rates
In European men’s football, the standard comparison across starters made heavy weeks look 12%
safer than longer-gap weeks (0.88, 95% CI 0.82 to 0.94; Figure 2). On confirmed injuries it read 0.94
(0.85 to 1.05). With no effect of load, it read 0.97 to 0.99, and 0.92 for both counts when players at



                                                   4
Table 1: Which data answer which question. The nine sports are football, rugby union, Australian rules, basketball,
ice hockey, American football, rugby league, baseball and cricket. The eight European men’s leagues are those of
England, France, Germany, Italy, the Netherlands, Portugal, Spain and Turkey. League-seasons, players and sizes are
totals over the samples. In the first rows, the league samples are the 11 player groups. A player in two samples of
one question counts twice, unless the source gives each player one identifier: the NBA with the G League, and MLB’s
batters with its pitchers. The worldwide survey, the injury comparison and the next start count each player once.
The survey’s pooled results combine the 140 samples played with three or five substitutions allowed (Supplementary
Table S41). One start in 31 ended in an injury-coded substitution (Supplementary Section S3). The next start asks
how often a starter taken off early started the club’s next match (Supplementary Section S3). Outside football, an
injury is each league’s own record, counted once per absence (Supplementary Section S12). Median age is the range
of the samples’ median ages at appearance; a dash marks rows without one (Supplementary Table S2). The injury
comparison’s row includes goalkeepers, whom Figure 1C and Figure 2 leave out (19 231 starts).

                                           League League-         Of them, Median
Question          Sport and sex           samples seasons Players  women age, years             Size Unit of size
Players against   Football, men:                1        27      4591        0          –      6710 injury-coded
recent load       England, France,                                                                  substitutions,
(Figure 1A)       Germany, Italy and                                                                outfield
and injury        Spain, as one group                                                               starters
history (Figure
1B)
                  Australian rules,             1           9    1253        0          –      1824 absences
                  men                                                                                through
                                                                                                     injury
                  Basketball, men and           4        62      4252      748          –      3180 absences
                  women                                                                              through
                                                                                                     injury;
                                                                                                     injured-list
                                                                                                     placements in
                                                                                                     Japan
                  Ice hockey, men               2        13      1932        0          –      1946 absences
                                                                                                     through
                                                                                                     injury
                  Baseball, men,                2        32      3965        0          –      4743 injured-list
                  batters and pitchers                                                               placements
                  American football,            1        13      6580        0          –      4613 absences
                  men                                                                                through
                                                                                                     injury
Who starts        Football, 10 men’s            18       74     18 419    2104   24.5–28.7   685 148 appearances
(Figure S3A)      and 7 women’s;
                  rugby union, men
Within the        Football, men and             25       57     18 673    3265   24.4–28.5    14 963 players with
same player       women; rugby union,                                                                two or more
(Figure S3B)      men; Australian                                                                    starts
                  rules, women
Kept on,          Football, men’s first 140 of 162      538     72 208       0          – 2 089 384 starter
worldwide         tiers in 96 of 99                                                                 appearances
survey            competitions, the
                  eight European
                  men’s leagues fitted
                  apart
The injury        Football, men, the             5       27      5942        0   25.4–27.4   296 029 appearances,
comparison        same five leagues                                                                  goalkeepers
(Figures 1C                                                                                          included,
and 2) and one                                                                                       with 7158
start in 31                                                                                          injury-coded
                                                                                                     substitutions
The next start    Football, men, 14            14        82     13 202       0   24.8–28.7   490 125 starts
                  leagues, five                                                                      followed by
                  substitutions                                                                      another club
                                                                                                     match




                                                        5
 A Two players typically differ 1.83-fold,                                 B Injury history: higher rates
      from 1.59- to 4.16-fold by group                                         in every sport that records it
                                                                                                                  Injuries per
     Football, men, 5 leagues                                                                                     100, history
   Football, recorded absence                                                                                         v others
   Australian rules, AFL (men)                                                                       1.39             4.4 v 3.1
                                                                                     Football
               Basketball, NBA
         Basketball, G League                                           Australian rules, AFL              1.52       6.5 v 4.4
   Basketball, WNBA (women)
 Basketball, B.LEAGUE (Japan)                                         Ice hockey, Switzerland              1.44       2.2 v 1.6
           Ice hockey, Finland                                         Baseball, MLB batters          1.34            0.8 v 0.6
      Ice hockey, Switzerland
        Baseball, MLB batters                                         Baseball, MLB pitchers          1.31            3.4 v 2.5
       Baseball, MLB pitchers
                                                                      American football, NFL                   1.69   4.4 v 2.6
       American football, NFL

                                 1   1.5   2    3        5       7                              1   1.5    2
                 median rate ratio between two players (95% CI), log scale              rate ratio (95% CI), log scale:
                                                                                       two or more injuries of 28 days
                                                                                     or more in three years v the others



 C Plain rates across players: highest
      after part of a match or a missed one                       △ all players,            ■ starters,
                                                             per recorded hour         per starter hour
                     full match or more                                       22.3                  22.7
                        part of a match                                       26.4                  28.9
        absent from the previous match                                        27.8                  33.6
                rested by the calendar:
          longer-gap week, 8 to 13 days                                       24.8                  26.0
                break, 14 days or more                                        22.5                  23.8

                                           20       30           40
                                      injury-coded substitutions
                                       per 1000 hours (95% CI)

Figure 1: Players differed widely in their usual injury rate. (A) For each player group, the diamond shows how far
apart two players picked at random typically are: the median rate ratio, the higher rate over the lower. Lines show
95% CIs (Supplementary Table S50). On the log scale, doubling and halving sit the same distance from one. Football
counts outfield starts only, once for injury-coded substitutions and once for confirmed injuries. The G League leaves
out absences that were likely moves to the NBA. Japan’s B.LEAGUE, drawn lighter, had only 27 injuries. Finland’s
ice hockey league, the Liiga, has the highest ratio between players, because its teams record injuries in different ways
(Supplementary Section S12). Outside football, some injury lists record rest, or a move to another team, as an injury,
which would move its diamond to the right. (B) Players with two or more injuries of 28 days or more in the previous
three years, against the others. The panel gives the rate ratio, and beside it each group’s injuries per 100 starts or
appearances (Supplementary Table S52). (C) Plain injury rates, before any comparison within players: injury-coded
substitutions per 1000 hours among outfield players in the 27 league-seasons of the injury comparison, with 95% CIs.
Triangles count all players per hour played, and squares count starters per starter hour. Part of a match is some
minutes, but less than a full match. A player was rested by the calendar when the club had no league match that
week, and absent when they missed the club’s previous match.




                                                             6
lower risk carried more load (Supplementary Section S6). Starters with more heavy weeks in their
earlier starts had lower rates: 30 down to 14 injury-coded substitutions per 1000 starter hours.
    Comparisons within each player and season leaned the other way. With no effect of load, the
usual ones read heavy weeks as riskier. Over whole seasons they read 1.06 to 1.17 times as risky in
football, and 1.05 to 2.19 in the other sports with injury records (Supplementary Sections S6 and
S9). As expected, an injury lowers later load: the injured match ends early, and missed matches
add no minutes. So 24% of the first four starts after an injury-coded substitution were heavy weeks,
against 33% of all the same starters’ starts. With no effect of load, only football’s heavy-week
comparisons after a completed match read about one.
    Those comparisons set like with like. Of heavy weeks, 95% followed a match the starter com-
pleted, against 48% of longer-gap weeks. Longer-gap weeks after a match the starter did not complete
had more injury-coded substitutions (1.33, 95% CI 1.20 to 1.47), against 1.04 to 1.18 with no effect of
load. When both kinds of week followed a completed match, their injury rates were similar on both
counts (Figure 2). Within each starter and season they read 0.99 (0.91 to 1.09). With every club
match counted, on confirmed injuries, they read 1.16 (0.99 to 1.36) across starters and 1.08 (0.92
to 1.27) within each starter. One check left out each club’s first league match after an international
break. Across starters, on confirmed injuries with every club match counted, it read riskier: 1.18
(1.001 to 1.401), against 1.01 with no effect of load.
    In 64% of heavy weeks, the full match was the weekly one: the previous league match came
six or seven days earlier. Short gaps differed within each starter and season. Two to three days
after the club’s previous match in any competition carried 1.40 times the confirmed injuries of six to
seven days (95% CI 1.23 to 1.59). With no effect of load, this ratio read 1.04. When the starter had
completed that match, it read 1.41 (1.14 to 1.73), and the simulation read about one. On injury-
coded substitutions both ratios were smaller (Supplementary Section S6). As known, congestion
studies found more injuries after gaps of four days or less,[11] also within the same players at one
club.[12]

Heavy weeks fell to regular starters
As the first author’s nine-sport preprint reported,[24] the extra minutes after a heavy week came
mostly from who starts. By an exact split, who starts accounted for 73% to 92% of the workload
gradient in all 18 samples of football and rugby union (Supplementary Figure S3A). Within each
starter, recorded minutes changed little. In all 54 groups of 37 leagues in seven other sports, playing
time rose less within the same player than across players (Supplementary Section S9). This held
whether or not a replaced player may return.
    A summary of our key findings is presented in Figure 2.


Discussion
Comparing starters made football’s heavy weeks look safer. In the usual comparisons within each
player’s season, simulations with no effect of load read them as riskier, in every sport with injury
records. In football, compared like with like, a full match in the previous week carried similar rates.

Per-hour rates divide by who starts
As our earlier preprint argued, a per-hour rate compares players as well as loads.[16] Most heavy
weeks belong to regular starters. Workplace health research calls this the healthy worker effect:
those who do most of a job are those fit enough to stay in it.[25–27] A basketball preprint found it
for recent minutes.[28] In women’s football, non-starters’ higher injury rates were put down to too
little play.[29] They may instead show who plays.
     Other counts have been proposed: only the players fit to play,[30] or appearances rather than
hours.[31–35] Counting appearances keeps the selection among starters (Supplementary Section S6).



                                                  7
                               Players' usual injury rates differ widely

               Two players typically differ 1.83-fold

                                                                                                    Injury history:
   between two players                                                                         1.3 to 1.7 times the rate
                                                        B.LEAGUE         Liiga

                         1        1.5         2                3         4
                                 median rate ratio, log scale

                                Why: heavy weeks fall more often to regular starters.
                  In football and rugby union, 73–92% of the extra minutes come from who starts

          European men's football: heavy v longer-gap weeks, compared like with like
             ● injury-coded substitutions         □ those a recorded absence followed            × with no effect of load

                                                                                 ● 0.88: 12% lower, heavy weeks look safer
                          Across starters,
                   every longer-gap week
                                                                                 □ 0.94: 6% lower, no clear difference


                                                                                 ● 1.02: 2% higher (7% lower to 11% higher),
                           Across starters,                                        no clear difference
                 after a completed match                                         □ 0.96: 4% lower (16% lower to 10% higher),
                                                                                   no clear difference

                                                                                 ● 0.99: 1% lower (9% lower to 9% higher),
     Within each starter, same season,                                             no clear difference
              after a completed match                                            □ 0.95: 5% lower (17% lower to 10% higher),
                                                                                   no clear difference

                                                  0.8      1       1.2    1.4
                                  ratio after a heavy week (95% CI), log scale


        Researchers and surveillance programmes: compare each player's heavy weeks with the same
           player's longer-gap weeks after a completed match; check other designs by simulation



                Nine team sports, both sexes; injury records: 22 573 players (748 women), 23 016 injuries;
              in men's football, injury-coded substitutions in 27 league-seasons with near-complete reasons



Figure 2: Central Figure: players differ widely in their usual injury rate, and how to compare like with like. In the
top row, each dot is one of the 11 player groups and gives the median rate ratio between two players picked at random
(Supplementary Table S50). The dot at the far right is Finland’s Liiga. Its teams record injuries in different ways.
Japan’s B.LEAGUE, drawn lighter, had few injuries. The injury history’s ratios span the six groups that record it.
In the second row the symbols change meaning. A filled mark shows outfield starters’ injury-coded substitutions per
starter hour. An open mark shows their confirmed injuries. The first pair is the standard comparison, across starters
against every longer-gap week. A cross marks its value in a simulation with no effect of load. The other pairs use only
longer-gap weeks after a completed match: across starters, and within each starter (shaded) in the same league-season.
The words beside each interval give its reading: safer or riskier when it lies wholly below or above one, no clear
difference when it holds one. The arrow runs from the standard comparison to the comparisons after a completed
match. A heavy week had a full league match or more in the previous seven days. A longer-gap week followed a gap
of 8 to 13 days. The box gives this study’s own advice.




                                                                    8
How comparing players misleads
   • Heavy weeks look safe. Comparing starters credits the heavy week with the regular starters’
     lower risk, as a healthy worker effect would. Players picked for a World Cup showed the same
     pattern.[36] Regular match play could also protect over months.

   • As known, the denominator can flip the answer. Loaded players had 26% more injury-
     coded substitutions per appearance than rested players, but 9% fewer per hour. With no effect
     of load, a simulation read 1.34 and 0.97 (Supplementary Section S6). Youth American football
     showed the same flip.[37]

   • Comparing players by their load misses those at higher risk, such as players with
     repeated injuries of 28 days or more. That history marks a group, not the players who will be
     injured.[38] Clubs already rank previous injury among their main risk factors.[39] So it should
     not by itself change selection (Supplementary Section S12).

Other factors in resting a player
Besides recent load, a decision to rest a player can weigh:

   • previous injury, a strong risk factor;[7]

   • recovery time between matches, which congestion studies link to injury;[11, 13]

   • every match and the travel between them;[14]

   • training load, which match records never show;[15]

   • squad depth and rotation.[12, 40]

Implications for research
First, compare each player with themselves only in a design that a simulation with no effect of load
reads correctly. Self-controlled designs assume that an event does not change later exposure.[41]
Tests of this exist,[42] and one method allows for its failure with brief exposures and rare events
that happen once.[43] But injuries happen again, and load comes every week. In our simulation,
counting only first injuries, or leaving out the weeks after one, kept the bias (Supplementary Section
S6). We found no earlier measure of its size in sport. In football, the comparison after a completed
match passed this check. Outside football, no reference weeks that we tried passed (Supplementary
Section S9). Such designs were used at one club[12] and on public football records.[44] They suit
surveillance programmes and research that pool clubs. Report them beside the standard comparison
across players.
    Second, researchers who use public match records should count confirmed injuries and every
match played, as time-loss and congestion studies do.[8, 11]
    Third, as expected, starters taken off by the 60th minute started the next match less often. Even
without injury-coded substitutions, they started it 46% of the time, against 85% after a full match
(Supplementary Section S3). So researchers who infer injury from team sheets should not read a
missed start as injury.

Clinical implications
First, starters with the most heavy weeks had the lowest rates. So lower per-hour injury rates among
a club’s most-used players can show who plays, not that their load is safe.
    Second, in football, compared like with like, a full match in the previous week carried similar
rates (0.99). Its interval allows up to 9% more injury-coded substitutions: about one more per club
every 3.3 seasons. On confirmed injuries with every club match counted, the interval allows up to
27%: about one more per club every 2.4 seasons.

                                                  9
    Third, a full match two to three days earlier carried more confirmed injuries: about 4.2 more
per 1000 such league starts (1.8 to 6.1). At an average club, that is one more every 10.5 seasons.
So clubs can aim rest and rotation at short gaps after a full match, as many do.[40] Leagues and
players’ unions can weigh such gaps in match calendars: unions already count appearances less than
five days apart.[2]

Limitations
The most important limitation is how recent match load was measured.[45] The main analysis counts
league matches only. Matches in the international breaks are never counted. So an international
player’s load is understated in exactly the weeks that congestion research studies (Supplementary
Table S12).
    Second, the records are public match data, not surveillance data kept by club doctors.[46, 47]
The injury reason is a label from the match report, not a diagnosis. Public injury lists record long
injuries best.[46] The injury history counts only injuries of 28 days or more. Of the injury absences
after an injury-coded substitution, 41% lasted more than 28 days. No video audit of the study
seasons was feasible.
    Third, the design is observational: it records what happened and changes nothing.[48] A simula-
tion shows only that a comparison reads correctly under the paths it holds. Ours held the injury’s
effect on later load, a higher risk after a return, and team selection. A player may also carry a knock
through a completed match. Staff who rest players at rising risk[49] would then make heavy weeks
look safer. In the strongest knock simulated, with resting before league matches, the comparison
read 0.89: it could hide a rise of up to about 12%. Yet starters who completed a match started the
club’s next league match about as often within a week as after 8 to 13 days: 84% against 83%. So the
records show little such resting before league matches. At the club’s next match in any competition,
such starters started less often within a week: 80% against 85%. The records cannot tell rotation,
routine before a cup tie, from resting a player at rising risk. In football and rugby union, recorded
minutes stop at the full match. This sets the smallest within-player slope the design could detect
(Supplementary Section S6).
    Fourth, we saved the two pre-set criteria, with a date, to the project’s own files, not to a public
protocol. A public protocol is a plan published in advance. We saved both after our earlier preprint
had used the same records. The first passed narrowly and the second failed. On the first, the
within-player slope varied 0.48 times as much as the rise across starters, against a limit of one half.
The second failed because its link was too uncertain to tell either way (Supplementary Section S4).
A registered confirmation on the next complete seasons will not run: the study ends first.
    Finally, the samples differ in sport, sex, era and size. The only women’s injury record is one
basketball league. The injury comparison comes from European men’s football (Supplementary
Section S9).


Conclusion
Players’ usual injury rates differ, and heavy weeks fall more often to regular starters. So per-hour
rates that compare players mix recent load with who carries it. An injury lowers later load. This
biases comparisons within players. In football, compared like with like, a full match in the previous
week, usually the weekly one, carried similar rates. They may still be up to 9% higher in injury-
coded substitutions. Researchers and injury surveillance programmes should check comparisons
within players by simulation. In football, they can compare each player’s heavy weeks with the
same player’s longer-gap weeks after a completed match.


Declarations
Contributors GPR designed the study, collected and analysed the data and wrote the manuscript.
NM shaped the methods and the clinical framing of the earlier preprint that this manuscript extends.

                                                  10
Both authors approved the final version. GPR is the guarantor. Anthropic’s Claude, a generative
AI assistant, was used under GPR’s direction to write and check analysis code, search the literature
and edit the text. It was used because the first author could not otherwise build and check analyses
of this size. The study design, the claims and their interpretation are the authors’. Every reported
quantity is computed from the committed data by the archived code and was verified by GPR. Both
authors take full responsibility for the content.
Funding This research received no specific grant from any funding agency in the public, commercial
or not-for-profit sectors.
Competing interests None declared.
Prior dissemination This manuscript is posted on arXiv as the next version of our earlier
preprint.[16] That preprint raised the question this manuscript answers. Some of this manuscript’s
results were first posted in the first author’s nine-sport preprint.[24]
Ethics approval The study reused only public, pre-existing match records. There was no recruit-
ment, no contact with any individual, no intervention and no access to medical records or clinical
files, so informed consent did not apply. The records name professional athletes, and some reasons
for substitution are injuries. They were therefore treated as special-category personal data despite
being public. Processing was for scientific research under the research provisions of the General Data
Protection Regulation. Everything published, every table, figure and deposited file, is aggregated
to whole league samples, so none of it describes a single player. Ethical approval was not sought.
These published records were treated as archival data, which Trinity College Dublin’s research ethics
guidance excepts from approval.[50] The same guidance grants no approval retrospectively.
Data availability statement Data are available in a public, open access repository. The aggregated
results behind every table and figure, and the analysis scripts, are in the archived record at DOI
10.5281/zenodo.24243290. No player-level record is shared. The match records the scripts read
identify players, so they are not redistributed. Their reconstruction from the public providers, each
source’s terms of use as read and any permission held are documented in the archive. Statistics from
NBA.com are credited to NBA.com, as its terms ask.


References
 [1] FIFPRO. Excessive workload demands: player performance, recovery and health. FIFPRO
     Player Workload Monitoring men’s football report, 2023/24 season; 2024. With Football
     Benchmark; the core group of players, page 15. Accessed 28 September 2026. Available from:
     https://media.fifpro.org/media/1oxkdnt2/en_pwm_men-s-annual-report-2024.pdf.

 [2] den Hollander S, Kerkhoffs G, Gouttebarge V. The impact of match workload and in-
     ternational travel on injuries in professional men’s football. Sports (Basel) 2024;12:212.
     doi:10.3390/sports12080212.

 [3] den Hollander S, Burgess D, Kerkhoffs G, et al. The International Match Calendar in men’s
     professional football: an expert position statement. Scand J Med Sci Sports 2025;35:e70163.
     doi:10.1111/sms.70163.

 [4] Esmaeili A, Hopkins WG, Stewart AM, et al. The individual and combined effects of multiple
     factors on the risk of soft tissue non-contact injuries in elite team sport athletes. Front Physiol
     2018;9:1280. doi:10.3389/fphys.2018.01280.

 [5] Lewis M. It’s a hard-knock life: game load, fatigue, and injury risk in the National Basketball
     Association. J Athl Train 2018;53:503–9. doi:10.4085/1062-6050-243-17.

 [6] Hudson SJ, Williams S, Starling L, et al. Training-related concussions in men’s English Pre-
     miership Rugby Union: an eight-season prospective cohort study of 153 243 player-weeks. Br
     J Sports Med 2026;60:1394–400. doi:10.1136/bjsports-2026-111653.



                                                  11
 [7] Hägglund M, Waldén M, Ekstrand J. Previous injury as a risk factor for injury in elite foot-
     ball: a prospective study over two consecutive seasons. Br J Sports Med 2006;40:767–72.
     doi:10.1136/bjsm.2006.026609.

 [8] Bahr R, Clarsen B, Derman W, et al. International Olympic Committee consensus statement:
     methods for recording and reporting of epidemiological data on injury and illness in sport 2020
     (including STROBE Extension for Sport Injury and Illness Surveillance (STROBE-SIIS)). Br
     J Sports Med 2020;54:372–89. doi:10.1136/bjsports-2019-101969.

 [9] Waldén M, Mountjoy M, McCall A, et al. Football-specific extension of the IOC consensus
     statement: methods for recording and reporting of epidemiological data on injury and illness
     in sport 2020. Br J Sports Med 2023;57:1341–50. doi:10.1136/bjsports-2022-106405.

[10] Ekstrand J, Spreco A, Bengtsson H, et al. Injury rates decreased in men’s professional football:
     an 18-year prospective cohort study of almost 12 000 injuries sustained during 1.8 million hours
     of play. Br J Sports Med 2021;55:1084–91. doi:10.1136/bjsports-2020-103159.

[11] Bengtsson H, Ekstrand J, Hägglund M. Muscle injury rates in professional football increase
     with fixture congestion: an 11-year follow-up of the UEFA Champions League injury study. Br
     J Sports Med 2013;47:743–7. doi:10.1136/bjsports-2013-092383.

[12] Carling C, McCall A, Le Gall F, et al. The impact of short periods of match congestion on injury
     risk and patterns in an elite football club. Br J Sports Med 2016;50:764–8. doi:10.1136/bjsports-
     2015-095501.

[13] Page RM, Field A, Langley B, et al. The effects of fixture congestion on injury in professional
     male soccer: a systematic review. Sports Med 2023;53:667–85. doi:10.1007/s40279-022-01799-5.

[14] Allen T, Taberner M, Zhilkin M, et al. Evolving running load demands and fixture congestion
     in the English Premier League: a decade of insights from 2015/2016 to 2024/2025. Br J Sports
     Med 2025;59:1643–54. doi:10.1136/bjsports-2025-110430.

[15] Impellizzeri FM, Shrier I, McLaren SJ, et al. Understanding training load as exposure and dose.
     Sports Med 2023;53:1667–79. doi:10.1007/s40279-023-01833-0.

[16] Ricou GP, Mahony N. Playing time tracks recent exposure in fifteen men’s and women’s foot-
     ball leagues: the denominator gradient and what it does to per-minute injury rates; 2026.
     arXiv:2608.11228v3 [stat.AP]. Not peer reviewed.

[17] Mandorino M, Kavanagh R, Tessitore A, et al. “How many minutes does the player have in his
     legs?” Answering one of football’s oldest coaching questions through a mathematical model.
     Appl Sci 2026;16:2139. doi:10.3390/app16042139.

[18] Griffith GJ, Morris TT, Tudball MJ, et al. Collider bias undermines our understanding of
     COVID-19 disease risk and severity. Nat Commun 2020;11:5749. doi:10.1038/s41467-020-19478-
     2.

[19] McKay C, Cross M, Kemp S, et al. Strategies used by professional rugby union clubs to
     manage players for artificial turf exposure. S Afr J Sports Med 2020;32:1–7. doi:10.17159/2078-
     516x/2020/v32i1a8276.

[20] von Elm E, Altman DG, Egger M, et al. The Strengthening the Reporting of Observational
     Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies.
     Lancet 2007;370:1453–7. doi:10.1016/S0140-6736(07)61602-X.

[21] The IFAB. Five substitutes option temporarily allowed for competition organisers (8 May 2020);
     and The IFAB permanently approves five-substitute option in top-level competitions (13 June
     2022); 2022. The 2020 announcement: https://www.theifab.com/news/five-substit

                                                 12
    utes-option-temporarily-allowed-for-competition-organisers/. Both accessed 27
    September 2026. Available from: https://www.theifab.com/news/the-ifab-permanently
    -approves-five-substitute-option-in-top-level-competitions/.

[22] Mansournia MA, Collins GS, Nielsen RO, et al. A CHecklist for statistical Assessment of
     Medical Papers (the CHAMP statement): explanation and elaboration. Br J Sports Med
     2021;55:1009–17. doi:10.1136/bjsports-2020-103652.

[23] Kitagawa EM. Components of a difference between two rates. J Am Stat Assoc 1955;50:1168–94.
     doi:10.2307/2281213.

[24] Ricou GP. One equation allocates playing time in competitive team sports: the rulebook sets
     the arithmetic and the league sets the habit; 2026. arXiv:2609.05584v1 [physics.soc-ph]. Not
     peer reviewed.

[25] Li CY, Sung FC. A review of the healthy worker effect in occupational epidemiology. Occup
     Med (Lond) 1999;49:225–9. doi:10.1093/occmed/49.4.225.

[26] Steenland K, Deddens J, Salvan A, et al. Negative bias in exposure-response trends in occupa-
     tional studies: modeling the healthy worker survivor effect. Am J Epidemiol 1996;143:202–10.
     doi:10.1093/oxfordjournals.aje.a008730.

[27] Warren JR, Rumore G. The association between playing professional American football and
     longevity. Proc Natl Acad Sci U S A 2023;120:e2308867120. doi:10.1073/pnas.2308867120.

[28] Yu Y, Hu G. The load management paradox: correcting the healthy-worker survivor
     effect in NBA injury modeling; 2026. arXiv:2603.26935 [stat.AP]. Not peer reviewed.
     doi:10.48550/arXiv.2603.26935.

[29] Moreno-Pérez V, Carles Bové B, Courel-Ibáñez J, et al. Non-contact injury incidence in profes-
     sional women’s football depends on the starting status of the player. Biol Sport 2025;42:99–107.
     doi:10.5114/biolsport.2025.145916.

[30] El-Khoury J, Stovitz SD, Shrier I. Estimating unbiased sports injury rates: a compendium
     of injury rates calculated by athlete exposure and athlete at risk methods. Br J Sports Med
     2021;55:354–5. doi:10.1136/bjsports-2020-102456.

[31] Knowles SB, Marshall SW, Guskiewicz KM. Issues in estimating risks and rates in sports injury
     research. J Athl Train 2006;41:207–15. PMID: 16791309.

[32] Stovitz SD, Shrier I. Injury rates in team sport events: tackling challenges in assessing exposure
     time. Br J Sports Med 2012;46:960–3. doi:10.1136/bjsports-2011-090693.

[33] Hecksteden A, Berger J, Mazzolari R, et al. How to mitigate injury risk after return-to-play in
     elite football? Expert judgement meets data analytics. Sci Med Footb 2026:1–16. Published
     online ahead of print. doi:10.1080/24733938.2026.2642654.

[34] Stovitz SD, Shrier I. Determination of athlete-exposures in team sports: it depends on the
     research question. Br J Sports Med 2025;59:1107–9. doi:10.1136/bjsports-2025-109822.

[35] Danielsen AC, Gompers A, Bekker S, et al. Limitations of athlete-exposures as a construct for
     comparisons of injury rates by gender/sex: a narrative review. Br J Sports Med 2025;59:177–84.
     doi:10.1136/bjsports-2024-108812.

[36] Bengtsson H, Hägglund M, Ekstrand J, et al. No major changes in injury incidence in European
     club football during the 2022/23 FIFA World Cup season: a subanalysis of the UEFA Elite Club
     Injury Study. BMJ Open Sport Exerc Med 2025;11:e002772. doi:10.1136/bmjsem-2025-002772.



                                                  13
[37] Kerr ZY, Yeargin SW, Djoko A, et al. Examining play counts and measurements of injury
     incidence in youth football. J Athl Train 2017;52:955–65. doi:10.4085/1062-6050-52.7.06.

[38] Bahr R. Why screening tests to predict injury do not work—and probably never will. . . : a
     critical review. Br J Sports Med 2016;50:776–80. doi:10.1136/bjsports-2016-096256.

[39] McCall A, Carling C, Davison M, et al. Injury risk factors, screening tests and preventative
     strategies: a systematic review of the evidence that underpins the perceptions and practices
     of 44 football (soccer) teams from various premier leagues. Br J Sports Med 2015;49:583–9.
     doi:10.1136/bjsports-2014-094104.

[40] Carling C, McCall A, Le Gall F, et al.       What is the extent of exposure to peri-
     ods of match congestion in professional soccer players? J Sports Sci 2015;33:2116–24.
     doi:10.1080/02640414.2015.1091492.

[41] Petersen I, Douglas I, Whitaker H. Self controlled case series methods: an alternative to
     standard epidemiological study designs. BMJ 2016;354:i4515. doi:10.1136/bmj.i4515.

[42] Whitaker HJ, Ghebremichael-Weldeselassie Y, Douglas IJ, et al. Investigating the assumptions
     of the self-controlled case series method. Stat Med 2018;37:643–58. doi:10.1002/sim.7536.

[43] Farrington CP, Whitaker HJ, Hocine MN. Case series analysis for censored, perturbed, or
     curtailed post-event exposures. Biostatistics 2009;10:3–16. doi:10.1093/biostatistics/kxn013.

[44] Hampstead W, Pappas E, Whalan M, et al. Match exposure and estimated travel before
     ACL injury in professional women’s football: an exploratory within-player case-crossover study.
     Sports Med Open 2026;12:170. doi:10.1186/s40798-026-01144-4.

[45] Wang C, Kaufman JS, Shrier I. Exposure misclassification: an “immortal time” bias
     in observational studies of training load and injury. J Clin Epidemiol 2024;176:111581.
     doi:10.1016/j.jclinepi.2024.111581.

[46] Hoenig T, Edouard P, Krause M, et al. Analysis of more than 20,000 injuries in European pro-
     fessional football by using a citizen science-based approach: an opportunity for epidemiological
     research? J Sci Med Sport 2022;25:300–5. doi:10.1016/j.jsams.2021.11.038.

[47] Krutsch V, Grechenig S, Loose O, et al. Injury analysis in professional soccer by means of media
     reports: only severe injury types show high validity. Open Access J Sports Med 2020;11:123–31.
     doi:10.2147/OAJSM.S251081.

[48] Shrier I, Wang C, Stokes T, et al.    Causal effects, workload and injury risk: the
     importance of specifying the research question.     J Sci Med Sport 2022;25:574–8.
     doi:10.1016/j.jsams.2022.03.018.

[49] Krishna K, Lychagin S, McLean LS. Injury, workload, and the strategic response of
     coaches in the NBA. Cambridge, MA: National Bureau of Economic Research; 2026. 35803.
     doi:10.3386/w35803.

[50] Trinity College Dublin. Guidance for using the Research Ethics Application Management Sys-
     tem (REAMS): making an application; 2022. Institutional guidance, pages 5 and 27–28. Ac-
     cessed 25 September 2026. Available from: https://www.tcd.ie/research/support/assets
     /pdf/Top%20Guidance_Simplified-31st%20Oct.pdf.




                                                 14
