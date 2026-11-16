<!-- source: library/preprints/arXiv/2026/2026 - Match classification in the last round of four-team round-robin tournaments - Csat et al.pdf -->
<!-- item: https://arxiv.org/abs/2605.25610 -->
<!-- authors: László Csató, András Gyimesi -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-16; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Match classification in the last round of four-team round-robin tournaments

                                                                 Match classification in the last round
                                                                 of four-team round-robin tournaments
                                                                         László Csatóa                  András Gyimesib

                                                                                      16th November 2026
arXiv:2605.25610v3 [physics.soc-ph] 13 Nov 2026




                                                  “The FIFA Council has unanimously decided in favour of expanding the FIFA World CupTM
                                                  to a 48-team competition as of the 2026 edition. [. . . ] The decision was taken following
                                                  a thorough analysis, based on a report that included four different format options. The
                                                  study took into account such factors as sporting balance, competition quality, impact on
                                                  football development, infrastructure, projections on financial position and the consequences
                                                  for event delivery.”

                                                                                                (Third meeting of the FIFA Council (FIFA, 2017))



                                                                                               Abstract
                                                         Classification of matches played in the last rounds of sports competitions is a
                                                         well-established tool for evaluating tournament designs. Our paper offers the first
                                                         comparison of deterministic and probabilistic match classification models by analysing
                                                         the most prominent example of four-team round-robin competitions, the group stage
                                                         of the FIFA World Cup. We show that both models are highly relevant in practice:
                                                         all (four) deterministic and (six) probabilistic match types occurred in the 2014
                                                         and 2018 FIFA World Cups, respectively. The probabilistic model, which accounts
                                                         for the relative benefits of attacking and defending, provides a deeper insight; for
                                                         instance, the competitive matches from the deterministic approach can be of any of
                                                         the six probabilistic types. Therefore, the probabilistic model is used to decompose
                                                         the impact of three reforms introduced in the 2026 FIFA World Cup: the expansion
                                                         to 48 teams, the modified qualification rules, and head-to-head tie-breakers.
                                                         Keywords: FIFA World Cup; incentives; match classification; simulation; tournament
                                                         design
                                                         MSC class: 62P20, 90-10, 90B90, 91B14
                                                         JEL classification number: C44, C53, D71, Z20
                                                     a
                                                       Corresponding author. Email: laszlo.csato@sztaki.hun-ren.hu
                                                  Institute for Computer Science and Control (SZTAKI), Hungarian Research Network (HUN-REN),
                                                  Laboratory on Engineering and Management Intelligence, Research Group of Operations Research and
                                                  Decision Systems, Budapest, Hungary
                                                  Corvinus University of Budapest (BCE), Institute of Operations and Decision Sciences, Department of
                                                  Operations Research and Actuarial Sciences, Budapest, Hungary
                                                     b
                                                       Email: gyimesi.andras@ktk.pte.hu
                                                  University of Pécs, Faculty of Business and Economics, Pécs, Hungary
                                                  Institute for Computer Science and Control (SZTAKI), Hungarian Research Network (HUN-REN),
                                                  Laboratory on Engineering and Management Intelligence, Research Group of Operations Research and
                                                  Decision Systems, Budapest, Hungary
1     Introduction
Various methods of operational research are increasingly used to examine sports rules. Indeed,
as clearly shown by the justification of the Fédération Internationale de Football Association
(FIFA) for the expansion of the 2026 FIFA World Cup, quoted at the beginning of the paper, the
evaluation of a tournament format requires an appropriate choice of the objective function and a
well-designed quantification of several, often conflicting factors. Inspired by the fundamental
changes in the 2026 FIFA World Cup, the flagship tournament of the most popular sport in the
world, our paper offers such an in-depth analysis.
    In the history of football, there are several examples of tacit coordination (Guyon, 2020) and
matches where one team or even both teams had few incentives to win. The last round of the
group stage is particularly prone to these anomalies (Guyon, 2022; Csató, 2025b). Let us see
some examples from the FIFA World Cup:

      • In 2018, Denmark and France played a boring goalless draw, which secured the qual-
        ification of Denmark and the first position of France. The Danish coach said that
        “we just needed one point, we were up against one of the best teams in the world at
        counterattacks, so we would have been stupid to open up a lot of space”, and “the last
        15 minutes was a neutral match” according to the French manager (Stuart, 2018).

      • In 2018, Belgium and England played against each other for the first place after both
        teams had already qualified. England made eight changes from the winning squad
        against Panama, lost the game, and the coach admitted “our objective was to qualify
        from the group and we have done that” (BBC, 2018).

      • In 2022, Brazil qualified before the last round and completely shuffled the squad by
        10 changes. They lost to Cameroon, and finished as the group winner only because
        Switzerland failed to score one more goal against Serbia in the parallel match (BBC,
        2022).

      • In 2026, France and Norway played against each other for the first place after both
        teams had already qualified. Norway opted to make 10 changes, the “goal machine”
        Haaland started on the bench for the first time since 2024, and the coach clarified that
        “I could not care too much about that game now” (Johnston, 2026).

The academic literature has already devoted serious effort to classifying these matches according
to their competitiveness. Inspired by the matches above, we adopt the common assumption of
this research field that teams only focus on qualifying for the next stage, and do not care about
the knockout bracket where they land.
    However, there exist two different match classification approaches. Deterministic models
(Ribeiro and Urrutia, 2005; Chater et al., 2021; Csató et al., 2024; Devriesere et al., 2026a) focus
on mathematical (im)possibility and do not take the relative payoffs from winning and losing into
account. A recently developed probabilistic model (Csató and Gyimesi, 2026b) is based on two
premises: (1) teams do not consider events with a small probability of occurring; and (2) their
offensive or defensive tactic is chosen based on the incentives provided by the tournament rules.
    Our first contribution resides in the comparison of the deterministic and probabilistic match
classification models. This is carried out for four-team single round-robin tournaments where
the top two teams qualify, a widely used format in major sports, including the FIFA World Cup
group stage until 2022. Both approaches are found to be highly relevant for historic FIFA World
Cups, but the probabilistic model is shown to give an enhanced picture, especially by breaking
down the broad category of competitive matches in the deterministic model.

                                                 2
    Consequently, the probabilistic model of Csató and Gyimesi (2026b) is adopted to analyse
the fundamental change in the design of the 2026 FIFA World Cup, which provides our second
contribution. We decompose the overall effect of the reform, which is important because three
independent rules have been modified at the same time: (1) the number of participating teams
has increased from 32 to 48; (2) a higher proportion of teams (2/3 instead of 1/2) qualify from
the groups since, besides the group winners and the runners-up, two-thirds of the third-placed
teams advance to the knockout stage, too; and (3) head-to-head records have replaced goal
difference as the primary tie-breaking criteria in the groups.
    The current study extends and refines the results of the pioneering work Chater et al. (2021),
on the competitiveness of the games played in the last round of the FIFA World Cup group stage,
from several aspects. First, we use a more sophisticated, probabilistic categorisation of matches.
In addition, the higher strength differences are explicitly accounted for in the simulation model,
and the effect of the tie-breaking rules is also considered. Crucially, our attention is not restricted
to the last group to play; averages are reported across all groups, addressing the challenge that
the third-placed teams in the groups finishing earlier do not necessarily know the exact target of
qualification. Finally, the decomposition procedure presented here helps in understanding the
impact of each component in the 2026 reform of the FIFA World Cup.
    The structure of the paper is as follows. Section 2 gives a concise overview of connected studies.
The methodology is presented in Section 3. The deterministic and probabilistic classification
models are compared in Section 4. Section 5 uses the latter model to explore the effects of the
recent comprehensive reform on the design of the FIFA World Cup. Section 6 concludes.


2     Related literature
Applications of operational research to sports have grown rapidly in recent decades due to the
huge amount of publicly available data, as well as the continuous development of computing
techniques and statistical methods. This literature is surveyed by Wright (2009, 2014); Kendall
and Lenten (2017); Csató (2021); Lenten and Kendall (2022); Devriesere et al. (2025, 2026b),
among others. Here, we give an overview of two sets of studies that are relevant to our topic:
works on the clustering of games with respect to the incentives of opposing teams, and research
on the expansion of the FIFA World Cup.
     Match classification is an increasingly popular topic in tournament design. Ribeiro and
Urrutia (2005) present integer programming models that give necessary and sufficient conditions
to ensure the qualification of a team in the first 𝑚 positions. Their technique can be used to
detect in advance when a team has already qualified or been eliminated. Chater et al. (2021)
divide the matches played in the last round of the FIFA World Cup group stage into three
distinct classes: (a) competitive game if no team is indifferent and at least one outcome of the
simultaneously played games threatens the qualification of one of them; (b) collusive game if
a particular outcome ensures the qualification of both teams; (c) stakeless game if at least one
team is indifferent because it is already qualified or eliminated. The probabilities are computed
via simulations for several reasonable formats with 32 teams (8 groups of four, top two qualify),
40 teams (8 groups of five, top two qualify), 48 teams (16 groups of three, top two qualify; 12
groups of four, top two plus the eight best third-placed teams qualify), and 60 teams (12 groups
of five, top two plus the eight best third-placed teams qualify) under all possible schedules of the
matches.
     Csató et al. (2024) conduct a similar simulation for the UEFA Champions League groups,
where four teams played a double round-robin tournament. However, the three categories of
games are (a) weakly stakeless if exactly one team is indifferent; (b) strongly stakeless if both


                                                  3
teams are indifferent; (c) competitive otherwise. Their probabilities are computed for both the
penultimate and the last matchdays under the 12 valid schedules. The same classification is
used by Gyimesi (2024) to compare the group and incomplete round-robin league formats of the
UEFA Champions League, as well as the planned format of the European Super League.
     Devriesere et al. (2026a) unify the classification models of Chater et al. (2021) and Csató
et al. (2024) by considering competitive, asymmetric (weakly stakeless), (strongly) stakeless, and
collusive games. Analogous to Gyimesi (2024), the group and incomplete round-robin formats of
the UEFA Champions League are analysed, but not only random schedules are studied: the 12
valid schedules are examined for the group stage, and five reasonable schedules are generated for
the incomplete round-robin league.
     Csató and Gyimesi (2026a) refine the concept of stakeless games by taking into account their
expected outcome. In particular, the organiser is assumed to face higher reputational costs if
the indifferent team is more likely to win if it exerts full effort. A novel format with imbalanced
groups is proposed for the 2026 FIFA World Cup to substantially decrease the probability that
the 16 strongest teams become indifferent in the last round of the group stage.
     Compared with these traditional models that use binary concepts, Csató and Gyimesi (2026b)
propose a probabilistic classification model based on a risk-benefit analysis. First, a team is
called indifferent if its payoff is fixed with a sufficiently high probability, rather than in any
mathematically possible scenario. Second, a team is assumed to play more offensively/defensively
if its expected gain from scoring goals is higher/lower than its expected loss from conceding goals.
This implies six different types of matches, as will be detailed in Section 3.1.2.
     It is known that multi-stage tournaments can always lead to strategic manipulation if more
than one team qualifies from a group (Vong, 2017). However, allowing only one team to qualify
makes teams indifferent with a high probability towards the end of the tournament, resulting in
a number of asymmetric and stakeless games, which threatens the attractiveness and even the
integrity of sports. Thus, the investigation of trade-offs between desirable factors in tournament
design calls for a probabilistic approach (Vong, 2017), as will be done here.
     Another line of literature considers and uses measures of match importance. Based on the
idea of Schilling (1994), Scarf and Shi (2008) compute the impact of a match on the finishing
positions, given the results of all other matches, some of them already played, some of them
simulated. Buraimo et al. (2022) find that matches potentially significant for end-of-season
outcomes attract a higher audience in the English Premier League. Compared to these studies,
the main novelty of our match classification model is the focus on the two opposing teams, rather
than on the match itself, which allows for quantifying team incentives.
     This paper is also strongly connected to studies on various issues of the 2026 FIFA World
Cup. Guyon (2020) quantifies the risk of match fixing if the tournament is played in 16 groups
of three, as was originally planned (FIFA, 2017). Forcing the strongest team to play the first two
matches minimises the risk of collusion, but this remains unacceptably high even in the most
favourable case when all groups are strongly imbalanced. The problem cannot be avoided by
forbidding draws. However, according to Stronka (2024), using random tie-breaking and dynamic
scheduling can be effective: the expected number of games with a collusive outcome is reduced
from 5.5 to 0.26. These results have probably inspired FIFA to reconsider the design of the 2026
FIFA World Cup, and choose to organise it in 12 groups of four teams each, where the top two
teams from each group and the eight best third-placed teams qualify for the Round of 32 (FIFA,
2023). As we have seen, the competitiveness of matches in this format is analysed by Chater
et al. (2021) and Csató and Gyimesi (2026a).
     The closest study is a parallel, not peer-reviewed work. Medina (2026) builds a Monte
Carlo simulation model for the FIFA World Cup, which reveals that uncompetitive final group


                                                 4
games nearly doubled between 2022 and 2026, mainly due to head-to-head tiebreakers and the
qualification of third-laced teams. It is shown that teams assigned to later finishing have a
stronger temptation to play for an advancing result. Crucially, the incentives are reinforced by
empirical observations: teams for which a draw is beneficial indeed play a draw more frequently,
in contrast to zero-sum final group games. Finally, an alternative 48-team format is suggested,
where only the group winners and runners-up qualify for the knockout stage, and the best group
winners directly qualify for the Round of 16.
    Di Mattia and Krumer (2026) examine the effects of reducing the number of matches in
groups of four teams. They exploit a structural change in professional beach volleyball, where the
number of rounds has been reduced to two in 2017. The reform impacts neither the probability
of a favourite team winning a single match nor the efficacy of the tournament.
    The expansion to 48 teams has received attention from the perspective of slot allocation, too.
The FIFA World Cup qualification is organised by the six confederations of FIFA, whose national
teams compete for a given number of berths; only two slots are available in an intercontinental
playoff tournament. Therefore, ensuring a balanced allocation of slots across the confederations
is crucial for the fairness of the qualification (Stone and Rod, 2016; Csató, 2023c). Krumer and
Moreno-Ternero (2023) explore the problem by using the standard tools of the fair allocation
literature. The claims are determined by the strengths of the confederations. 10 different
allocations are considered based on various assumptions on the measure of strength and the
status quo. UEFA (Union of European Football Associations) is found to deserve more slots than
assigned by FIFA. Csató et al. (2025) develop an Elo-based method inspired by the FIFA World
Ranking to quantify the performance of five confederations in previous FIFA World Cups. Their
results show that more European and South American teams need to play in the competition
than allowed by the official policy.


3       Methodology
Section 3.1 presents the two existing approaches for match classification. The pre-2026 and
post-2026 formats of the FIFA World Cup are described in Section 3.2, and our simulation
framework is discussed in Section 3.3.


3.1      Match classification models
As we have outlined in Sections 1 and 2, two different frameworks have been suggested for
clustering games played in the last rounds of sports tournaments. They are presented in
Sections 3.1 and 3.2, respectively, assuming that only one prize—qualification to the next stage—
exists, which is realistic in the case of the FIFA World Cup (Chater et al., 2021; Guyon, 2022;
Csató and Gyimesi, 2026a).

3.1.1     Deterministic model
The evolution of the deterministic approach for match classification has already been discussed
in Section 2. Currently, Devriesere et al. (2026a) consider the most refined categorisation, by
unifying the models introduced by Chater et al. (2021) and Csató et al. (2024). We will use this
model, which contains the following four distinct categories:

        • Stakeless match: the prizes of both teams do not depend on the outcomes of matches
          played simultaneously or later;



                                                5
        • Asymmetric match: the prize of exactly one team does not depend on the outcomes of
          matches played simultaneously or later;

        • Collusive match: the prizes of both teams depend on the outcomes of matches played
          simultaneously or later, but a particular result guarantees the prize for both teams;

        • Competitive match: none of the above, that is, the prizes of both teams depend on the
          outcomes of matches played simultaneously or later, and no particular result guarantees
          the prize for both teams.

Illustrative examples from historic FIFA World Cups will be given in Section 4.3.

3.1.2     Probabilistic model
According to our knowledge, the only probabilistic match classification model has been introduced
                                      (ℎ)
by Csató and Gyimesi (2026b). Let 𝑃𝑖 be the probability that team 𝑖 obtains the prize if the
result of its match is ℎ.
    Compared to the benchmark of 0-0, the potential gain from playing offensively is
                                               (𝑚-0)          (0-0)
                                        𝒢𝑖 = 𝑃𝑖        − 𝑃𝑖,𝑘 ,

as the attacking team scores 𝑚 goals if its tactic is successful.
    Compared to the benchmark of 0-0, the potential loss from playing offensively is
                                               (0-0)      (0-𝑚)
                                       ℒ𝑖 = 𝑃𝑖,𝑘       − 𝑃𝑖           ,

as the attacking team concedes 𝑚 goals if its tactic is unsuccessful.
    The classification is based on comparing the values 𝒢𝑖 and ℒ𝑖 for the two opponents. Naturally,
𝒢𝑖 and ℒ𝑖 are computed by simulating the results of all matches played simultaneously or later.
The value of 𝑚 is also determined by the simulation model, which ensures that a weaker (stronger)
team is less (more) likely to win by more goals.
    An indifference threshold ℐ is used to ignore events with a small probability of occurring:
a team is said to be indifferent if both 𝒢𝑖 and ℒ𝑖 remain below ℐ. Teams play offensively by
default, and shift to a defensive tactic only if the payoff from avoiding a loss (ℒ𝑖 ) is higher than
the payoff from winning (𝒢𝑖 ).
    Csató and Gyimesi (2026b) have adopted the probabilistic model to analyse the UEFA
Champions League, where two prizes are available. Consequently, 𝒢𝑖 = ℒ𝑖 if a win certainly
provides the first prize for team 𝑖, while a loss leads to no prize. The probability of such an event
is non-marginal in the group stage used until the 2023/24 season, since the first prize is the top
two positions, and the second prize is the third position in a group of four. Therefore, in order
to avoid the uncertain classification when 𝒢𝑖 = ℒ𝑖 , Csató and Gyimesi (2026b) have assumed
that teams play defensively only if ℒ𝑖 exceeds 𝒢𝑖 by the “margin of error” ℐ. In the case of the
FIFA World Cup, this technical adjustment is unnecessary due to the existence of only one prize.
Hence, we can choose the natural direct comparison of 𝒢𝑖 and ℒ𝑖 .
    These assumptions imply six distinct categories of games:

        • Unimportant match: both teams are indifferent if max {𝒢𝑖 ; ℒ𝑖 ; 𝒢𝑗 ; ℒ𝑗 } ≤ ℐ;

        • Defensive asymmetric match: team 𝑖 is indifferent and team 𝑗 should play defensively if
          max {𝒢𝑖 ; ℒ𝑖 } ≤ ℐ and max {𝒢𝑗 ; ℒ𝑗 } > ℐ such that 𝒢𝑗 < ℒ𝑗 ;

        • Offensive asymmetric match: team 𝑖 is indifferent and team 𝑗 should play offensively if
          max {𝒢𝑖 ; ℒ𝑖 } ≤ ℐ and max {𝒢𝑗 ; ℒ𝑗 } > ℐ such that 𝒢𝑗 ≥ ℒ𝑗 ;

                                                   6
      • Antagonistic match: neither team is indifferent, team 𝑖 should play offensively and team
        𝑗 should play defensively if max {𝒢𝑖 ; ℒ𝑖 } > ℐ and max {𝒢𝑗 ; ℒ𝑗 } > ℐ such that 𝒢𝑖 ≥ ℒ𝑖
        and 𝒢𝑗 < ℒ𝑗 ;

      • Defensive match: neither team is indifferent, both teams 𝑖 and 𝑗 should play defensively
        if max {𝒢𝑖 ; ℒ𝑖 } > ℐ and max {𝒢𝑗 ; ℒ𝑗 } > ℐ such that 𝒢𝑖 < ℒ𝑖 and 𝒢𝑗 < ℒ𝑗 ;

      • Offensive match: neither team is indifferent, both teams 𝑖 and 𝑗 should play offensively
        if max {𝒢𝑖 ; ℒ𝑖 } > ℐ and max {𝒢𝑗 ; ℒ𝑗 } > ℐ such that 𝒢𝑖 ≥ ℒ𝑖 and 𝒢𝑗 ≥ ℒ𝑗 .

We set ℐ = 0.02, that is, teams become indifferent if the difference in the probability of
qualification with a loss and a win remains below 2%. Illustrative examples from historic FIFA
World Cups will be given in Section 4.3.
    This framework even allows quantifying the strength of incentives for each match. Let 𝜔𝑖
be 0 if team 𝑖 is indifferent, and 𝜔𝑖 = |𝒢𝑖 − ℒ𝑖 | if max {𝒢𝑖 , ℒ𝑖 } > ℐ. The strength of incentives
equals (a) 𝜅 = 0 in an unimportant game; (b) 𝜅 = 100 · max{𝜔𝑖 ; 𝜔𝑗 } in a defensive or offensive
asymmetric game; and (c) 𝜅 = 100 · min {𝜔𝑖 ; 𝜔𝑗 } in an antagonistic/defensive/offensive game.
Hence, 0 ≤ 𝜅 ≤ 100, and a higher value indicates that more powerful incentives are created for
the non-indifferent team(s).
    To define intensity, we deliberately use the maximum for asymmetric matches and the
minimum if no team is indifferent. If exactly one team is indifferent, it does not care about the
outcome, and everything depends on what the other team wants to do. On the other hand, if no
team is indifferent, the conservative assumption is that the behaviour of the team with weaker
incentives will decide what happens on the field.


3.2     Tournament designs of the FIFA World Cup
The FIFA World Cup was organised in essentially the same format between 1998 and 2022. The
32 participants were allocated into eight groups of four teams by maximising inter-confederation
games played in the group stage (Csató, 2025a). While the groups were intended to be balanced
in order to ensure fairness, this was usually not achieved due to the misaligned seeding policies
(Guyon, 2015; Cea et al., 2020; Csató, 2023a; Lapré and Palazzolo, 2023). In the groups, single
round-robin tournaments were played, with three matches for each team. The first two teams
advanced to the Round of 16, the last two were eliminated. The final group standings were
determined according to the following criteria:

      1. Points obtained in all group matches;

      2. Goal difference in all group matches;

      3. Number of goals scored in all group matches;

      4. Points obtained in the matches played between the teams in question;

      5. Goal difference in the matches played between the teams in question;

      6. Number of goals scored in the matches played between the teams in question;

      7. Fair play points in all group matches;

      8. Drawing of lots.




                                                  7
    The 2026 edition of the FIFA World Cup has seen several changes to the group stage. First,
the number of teams increased from 32 to 48, divided into 12 groups of four. Second, the knockout
stage starts with the Round of 32, contested by the 12 group winners, the 12 runners-up, and the
eight best third-placed teams. The third-placed teams are ranked by the relevant tie-breaking
criteria of the 32-team format in the given order (1, 2, 3, 7, 8). Third, in the 2026 edition,
head-to-head results are preferred to goal difference; the order of tie-breaking criteria is 1, 4, 5,
6, 2, 3, 7, with the 8th replaced by position in the official FIFA World Rankings.


3.3     The simulation model
As usual in the literature of tournament design (Scarf et al., 2009), we use simulations since
historical data reflect only a single realisation of several uncertain parameters, and the probabilistic
match classification model calls for computing the probability of qualification. In particular, the
group stages of the five FIFA World Cups between 2010 and 2026 are simulated using the actual
participants and group allocations. Hence, four instances of the 32-team format and one example
of the 48-team format are considered.
    Individual match outcomes—the number of goals scored by the two teams—are simulated
by a Poisson model (Maher, 1982), which was estimated by Football rankings (2020) based on
thousands of matches between national teams. This is a well-established simulation method in
the academic literature, used by Csató (2022, 2023a,b,c, 2025c); Csató and Gyimesi (2026a);
Stronka (2024). The strengths of the teams are measured by their World Football Elo Ratings
(https://www.eloratings.net/). In particular, ratings on 1 April 2026 are employed for
the 48-team format, and 1 June of the given year for the 32-team format, downloaded from
https://www.international-football.net/. The model distinguishes between matches
played on neutral and non-neutral grounds. Naturally, only the host countries play at home.
Following World Football Elo Ratings and in line with the regression of Football rankings (2020),
the Elo ratings of the host(s) are increased by 100 to reflect home advantage.
    The simulations are conducted at two levels. First, we generate results for all matches played
simultaneously or later than the given match 1000 times. This is the set of matches whose
outcomes remain unknown to the opposing teams at the start of their match, but could affect
their qualification from the group. The 1000 simulated sets of results are used to quantify the
probability of qualification under 1000 wins of 𝑚-0, 1000 draws of 0-0, and 1000 losses of 0-𝑚.
The value of 𝑚 comes directly from a probability distribution, analogous to Csató and Gyimesi
(2026b): the number of goals scored by the loser is set to 0, and the number of goals scored by
the winner is generated by the Poisson model (if it would be 0, a new value is drawn). Thus, it
is not fixed for a given match but varies across the simulations such that the expected value of
𝑚 is a monotonic function of Elo rating difference. This simple procedure will be followed in
Section 4.3 to classify the 16-16 matches played in the last round of the group stage in the FIFA
World Cups between 2014 and 2022.
    However, in order to reliably compare the two classification models (Section 4.4) and examine
the effects of the 2026 reform (Section 5), we need to generate larger and more representative
samples for both the 32-team and the 48-team formats, without fixing the results of the first two
rounds in the group stage to the actual outcomes. Therefore, the second level refers to simulating
past results, too. Again, 1000 sets of results are generated for these earlier matches, yielding
1000 hypothetical scenarios for each FIFA World Cup between 2010 and 2026.
    Tournament organisers should make decisions based on this representative set of outcomes,
rather than the observed results of the first two rounds in historic competitions. For instance, it
would be a serious mistake to assume that the champion of 2022, Argentina, is always defeated


                                                   8
by Saudi Arabia in the group stage.
     Finally, as it will turn out in Section 4.1, the deterministic model requires only simulating the
first two rounds of the group stage in the pre-2026 format, when the top two teams qualify from
each group. However, this simplification does not hold for the post-2026 format since only some
third-placed teams qualify, making the groups interdependent: in any given group, the results in
the other groups could affect qualification. Hence, for example, Chater et al. (2021) focus on
the last group to play, where the third-ranked team exactly knows its target to qualify—but
this worst-case analysis is disadvantageous to the post-2026 format of the FIFA World Cup.
Fortunately, the unequal treatment of third-placed teams does not cause any difficulty for the
probabilistic match classification model because the results of groups finishing earlier can be
simulated accordingly. To conclude, using the deterministic approach would be either complicated
or biased for the 2026 FIFA World Cup, which provides an additional argument for considering
the probabilistic approach to analyse the effects of the reform package.


4     Which match classification model is better for the
      FIFA World Cup?
Section 4.1 classifies matches according to the deterministic model for single round-robin tourna-
ments with four teams if the top two teams qualify. The differences between the deterministic
and probabilistic approaches are illustrated in Section 4.2. The 48 games played in the last
round of the FIFA World Cup group stages from 2014 to 2022 are classified by both models in
Section 4.3. Finally, Section 4.4 compares the deterministic and probabilistic match classification
models through the example of the four FIFA World Cups organised between 2010 and 2022.


4.1     Identification of deterministic match types
Table 1 presents all possible scenarios in a single round-robin tournament with four teams before
the last round. The classification of matches in the deterministic model is also provided for the
rules of the 2022 FIFA World Cup, when the top two teams qualify, and the primary tie-breaking
criterion is goal difference.
    Regarding the distribution of points, 13 cases may occur when two rounds are finished. If
the points are 6-3-3-0 or 4-4-1-1, two different scenarios exist with respect to the matches played
in the last round. It is important to distinguish these scenarios for the deterministic match
classification model. If the points are 6-3-3-0 such that the top team A with 6 points plays
against the bottom team D with 0 points, their game is stakeless: team A is already qualified,
and team D is eliminated. However, in the other case under points 6-3-3-0, both last round
games are competitive. Analogously, if the points are 4-4-1-1 such that the top teams A and
B with 4 points play against each other in the last round, their game is collusive: both teams
are guaranteed to qualify with a (goalless) draw. On the other hand, both last-round games are
competitive if a team with 4 points plays against a team with 1 point.
    Among the 15 possible scenarios, only one (scenario 7 in Table 1) involves a collusive
game. The number of asymmetric games is two in one scenario (14), and one in four scenarios
(8–11). There exists one scenario (15) with two stakeless games, and another one (12) with
one stakeless game. Finally, there is no scenario with two different types of uncompetitive
(collusive/asymmetric/stakeless) games, and both last round matches are competitive in six
scenarios (1–6 and 13).




                                                  9
     Table 1: Deterministic match classification in a four-team single round-robin
  tournament if two teams qualify and the primary tie-breaking rule is goal difference

 Scenario         1               2               3               4              5           6
 A                2               3               4               4              4           4
 B                2               3               2               3              3           4
 C                2               3               2               2              3           1
 D                2               3               1               1              1           1
 Draws            4               0               3               2              1           2
                 A-B             A-B             A-B             A-D         A-B           A-C
 Games
                 C-D             C-D             C-D             B-C         C-D           B-D

 Scenario             7      8          9        10        11          12    13       14         15
 A                    4      4          4        6         6            6     6        6          6
 B                    4      4          4         2        3           3      3       4           6
 C                    1      2          3        1         1            3     3        1          0
 D                    1      0          0        1         1            0    0         0          0
 Draws                2      2          1        2         1            0     0        1          0
                  A-B       A-B        A-C       A-B       A-C        A-D    A-B     A-B      A-B
 Games
                  C-D       C-D        B-D       C-D       B-D        B-C    C-D     C-D      C-D
 Collusive        A-B       —          —         —         —           —     —        —          —
                                                                                     A-B
 Asymmetric        —        C-D        B-D       A-B       A-C         —     —                   —
                                                                                     C-D
                                                                                              A-B
 Stakeless         —        —          —         —         —          A-D    —        —
                                                                                              C-D
   The rows A–D indicate the number of points scored by the four teams after two rounds, respectively.
   The row Draws presents the number of draws played in the first two rounds.
   The row Games shows the matches to be played in the last round.

         Table 2: 2022 FIFA World Cup, Group C: Standing before the last round

   Pos       Team                W           D         L         GF         GA       GD       Pts
    1        Poland              1           1         0          2          0       +2        4
    2        Argentina           1           0         1          3          2       +1        3
    3        Saudi Arabia        1           0         1          2          3       −1        3
    4        Mexico              0           1         1          0          2       −2        1
   Pos = Position; W = Won; D = Drawn; L = Lost; GF = Goals for; GA = Goals against; GD = Goal
   difference; Pts = Points. All teams played two matches.
   The top two teams qualify for the Round of 16, and the bottom two teams are eliminated.
   Matches in the last round: Argentina vs Poland, Saudi Arabia vs Mexico.


4.2      Importance of distinguishing competitive matches
Table 2 shows the standing of Group C in the 2022 FIFA World Cup before the last (third)
round, where Argentina plays against Poland and Saudi Arabia plays against Mexico. Obviously,
any team can still qualify or be eliminated; hence, none of these matches is asymmetric or
stakeless. In addition, Argentina and Poland have no collusive strategy since a win by Saudi


                                                  10
                         Table 3: Classification of matches played in the last
                          round of the 2022 FIFA World Cup group stage

                                                                                               Model
Group   Team 1           Team 2            ℒ1 (%)    𝒢1 (%)   ℒ2 (%)    𝒢2 (%)      𝜅
                                                                                            Det.  Prob.
 A      Ecuador          Senegal           91.94       0        2.39     97.61    91.94      C     AN
 A      Qatar            Netherlands         0         0       25.57       0      25.57     AS     DAS
 B      England          Wales             1.66        0         0       27.70    27.70      C     OAS
 B      Iran             United States     85.24     14.76       0        100     70.48      C     AN
 C      Argentina        Poland            71.67     28.33     68.80       0      43.34      C       D
 C      Saudi Arabia     Mexico            25.67     74.33       0       57.59    48.66      C       O
 D      Australia        Denmark           98.34      1.66       0       99.62    96.68      C     AN
 D      France           Tunisia             0          0        0       23.56    23.56     AS     OAS
 E      Costa Rica       Germany           68.90     31.10       0       83.63    37.80      C     AN
 E      Spain            Japan             15.51        0      19.53     80.47    15.51      C     AN
 F      Belgium          Croatia           2.72      97.28     67.56       0      67.56      C     AN
 F      Canada           Morocco             0          0      55.20       0      55.20     AS     DAS
 G      Brazil           Cameroon            0         0         0       42.91    42.91     AS     OAS
 G      Serbia           Switzerland         0       99.37     98.98      1.02    97.96      C     AN
 H      Ghana            Uruguay           93.50      6.50       0       90.62    87.00      C     AN
 H      Portugal         South Korea         0         0          0      50.50    50.50     AS     OAS
 Models: Det. stands for Deterministic, Prob. stands for Probabilistic.
 Deterministic match types: AS = asymmetric; C = competitive; COL = collusive; S = stakeless.
 Probabilistic match types: AN = antagonistic; D = defensive; DAS = defensive asymmetric; O = offensive; OAS =
 offensive asymmetric; U = unimportant.


     Arabia eliminates one of them. Therefore, both matches played in the last round are competitive.
         Nonetheless, both Argentina and Poland qualify by playing a goalless draw if Mexico does
     not lose or does not win by at least three goals against Saudi Arabia. This has a relatively
     high probability since Mexico is a stronger team than Saudi Arabia: in the FIFA Men’s World
     Rankings of 31 March 2022, used for seeding the 2022 FIFA World Cup, Mexico was ranked 9th,
     while Saudi Arabia was ranked 49th. On the other hand, Argentina is certainly eliminated if it
     loses. Poland is also eliminated if it loses and either Saudi Arabia wins in the other match, or
     Saudi Arabia plays a draw and Argentina wins by a high margin, or both Mexico and Argentina
     win by a cumulated margin of five goals. Consequently, neither Argentina nor Poland should
     accept a substantial risk in order to win their last game.
         The incentives in the other match are quite different. Mexico needs to win in order to have
     any chance to qualify. Even though Saudi Arabia may qualify by playing a draw if Poland wins,
     this is unlikely, as Argentina is stronger than Poland. Thus, both Saudi Arabia and Mexico have
     to take a high risk in order to win their last game and have a decent chance of qualification.
         Thus, both matches played in the last round are in the same (competitive) category according
     to the standard deterministic match classification model. However, both teams have strong
     incentives to defend the result of 0-0 in the first match, and both teams have powerful incentives
     to attack in the second match.




                                                    11
4.3     Classification of historic FIFA World Cup games
Table 3 classifies the 16 matches played in the last round of the 2022 FIFA World Cup group
stage based on both approaches presented in Section 3.1.
     We have argued in Section 4.2 that the two matches played in Group C significantly differ
with respect to the incentives of the teams, which is not reflected by the deterministic model,
but is captured by the probabilistic model. Indeed, according to our simulations, Argentina and
Poland qualify with probabilities of more than 70% and 100%, respectively, even by playing
a goalless draw. However, if they lose, Argentina is certainly eliminated, and Poland is also
eliminated with a probability of more than 65%. Therefore, this match is categorised as defensive
in the probabilistic model. The strength of incentives 𝜅 is remarkably high; the difference between
the loss from losing and the gain from winning exceeds 40 percentage points for both teams.
     On the other hand, Mexico cannot qualify by playing a draw, and Saudi Arabia has a chance
of less than 30% to qualify if it plays a goalless draw. Hence, they face strong incentives to
attack, implying an offensive match. The strength of incentives 𝜅 is also quite high; the difference
between the gain from winning and the loss from losing almost reaches 50 percentage points for
both teams.
     In the deterministic model, there are five asymmetric matches, either because one team is
already qualified (France, Brazil, Portugal) or eliminated (Qatar, Canada) after two rounds,
and 11 competitive matches. Naturally, in the probabilistic model, the asymmetric games are
either defensive or offensive asymmetric, depending on whether the non-indifferent team prefers
avoiding a loss to winning (e.g. the Netherlands certainly qualifies by playing a goalless draw),
or winning to avoiding a loss (e.g. Tunisia is certainly eliminated by playing a goalless draw).
Among the competitive matches, there is also one offensive asymmetric match: in Group B,
England can still be eliminated if it loses, but this has only a marginal probability of less than
2%, below the indifference threshold ℐ. Hence, the probabilistic framework identifies England
as an indifferent team. The remaining 10 competitive matches are all antagonistic, except for
the one defensive and the one offensive match in Group C, discussed above. Nevertheless, the
strength of incentives varies from about 15 percentage points (Spain qualifies with a probability
of more than 84% even if it loses against Japan) to almost 98 percentage points.
     The matches played in the last round of the 2014 and 2018 FIFA World Cup group stages,
respectively, are classified in Tables A.1 and A.2 in the Appendix. Two stakeless/unimportant
matches appear in Group B in 2014 and in two groups (Groups A and G) in 2018, corresponding
to scenario 15 in Table 1. Group D in the 2014 FIFA World Cup has one stakeless/unimportant
and one competitive/antagonistic match. Indeed, Costa Rica with 6 points is already qualified,
while its opponent, England, is certainly eliminated. In the game Uruguay vs Italy, two teams
with 3 points play against each other, but their goal differences are −1 and 0, favouring Italy in
the case of a draw. Thus, the strength of incentives 𝜅 reaches its theoretical maximum because
Italy qualifies at the expense of Uruguay if the result is a draw, while Uruguay qualifies at the
expense of Italy if it wins. Finally, there is one collusive match in the 2014 FIFA World Cup,
as Group G corresponds to scenario 7 in Table 1: two teams with 4 points, Germany and the
United States, play against each other, while the two remaining teams have only 1 point each.
     To conclude, all four deterministic match types occurred in the 2014 FIFA World Cup, and
all six probabilistic match types occurred in the 2018 FIFA World Cup. Thus, both classifications
presented in Section 3.1 have a high practical relevance; they are not only theoretical curiosities.




                                                12
                                    (a) Deterministic model
 2-2-2-2 (1)
 3-3-3-3 (2)
 4-2-2-1 (3)
 4-3-2-1 (4)
 4-3-3-1 (5)
 4-4-1-1 (6)
 4-4-1-1 (7)
 4-4-2-0 (8)
 4-4-3-0 (9)
6-2-1-1 (10)
6-3-1-1 (11)
6-3-3-0 (12)
6-3-3-0 (13)
6-4-1-0 (14)
6-6-0-0 (15)
               0      2       4      6      8        10       12       14      16      18    20
                                                Probability (%)
                      Stakeless      Asymmetric           Collusive         Competitive


                                    (b) Probabilistic model
 2-2-2-2 (1)
 3-3-3-3 (2)
 4-2-2-1 (3)
 4-3-2-1 (4)
 4-3-3-1 (5)
 4-4-1-1 (6)
 4-4-1-1 (7)
 4-4-2-0 (8)
 4-4-3-0 (9)
6-2-1-1 (10)
6-3-1-1 (11)
6-3-3-0 (12)
6-3-3-0 (13)
6-4-1-0 (14)
6-6-0-0 (15)
               0      2       4      6      8        10       12       14      16      18    20
                                                Probability (%)
                   Unimportant       Defensive asymmetric             Offensive asymmetric
                   Defensive         Offensive                        Antagonistic

                       Figure 1: Match classification in the last round of
                      simulated 2010–2022 FIFA World Cup group stages




                                                13
           Table 4: Frequency of deterministic and probabilistic match types in
           the last round of simulated 2010–2022 FIFA World Cup group stages

                                              Deterministic model
 Probabilistic model                                                                        Total
                            Asymmetric        Collusive   Competitive         Stakeless
 Antagonistic                                                44.16%                        44.16%
 Defensive                                     1.02%         2.11%                         3.13%
 Offensive                                                    4.86%                         4.86%
 Defensive asymmetric          9.89%           0.10%          3.68%                        13.67%
 Offensive asymmetric          13.93%                         3.46%                        17.38%
 Unimportant                    2.98%          0.01%         0.24%             13.58%      16.80%
 Total                         26.80%           1.13%           58.50%         13.58%       100%


4.4      Comparison of the alternative match classification models
Figure 1 plots the probability of each match type in the last round of the FIFA World Cup group
stages from 2010 to 2022. All games played in the eight groups have been simulated 1000 times
each, implying a sample of 4 × 8 × 2 × 1000 = 64,000. Points 6-3-3-0 occur in about a third of
simulated groups; the chances of scenarios 12 (when the two runners-up play against each other)
and 13 (when the first team plays against a runner-up) are about 11.7% and 18.6%, respectively.
The probability of three other cases (points 4-4-3-0, 6-3-1-1, and 6-4-1-0) approximates or exceeds
10%, while it remains below 7% in the further nine cases. Scenario 1, with four draws in the first
two rounds, is almost impossible with a probability of merely 0.175%.
    Figure 1.a for the deterministic model adds little to Table 1. Competitive becomes far
the most frequent category, but the proportion of asymmetric and stakeless matches is also
substantial. On the other hand, collusive matches occur with a probability of less than 1.2%.
Given the standing after two rounds, at most two types of matches may emerge, as the last
round contains two games.
    Regarding the probabilistic model (Figure 1.b), since a stakeless match is always unimportant,
only unimportant games appear in scenario 15, but the picture is quite diverse in the majority of
scenarios. All the six different types have a positive chance of occurring under points 4-4-1-1 and
6-3-3-0, which have two corresponding scenarios each. Antagonistic matches are dominant in five
scenarios (1–5) when the group has a high competitive balance after two rounds. In line with the
historical examples discussed in Section 4.3, offensive and, especially, defensive matches occur only
occasionally, with probabilities of 4.9% and 3.1%, respectively. Naturally, asymmetric matches
mainly occur in imbalanced groups. Finally, besides scenario 15, a one-to-one correspondence
exists between the deterministic and probabilistic models in scenario 12, where the competitive
match played by the two teams with 3 points is always antagonistic.
    Table 4 compares the two match classification approaches for a characteristic FIFA World
Cup with 32 teams, based on the average of the four tournaments played between 2010 and 2022.
Crucially, even though competitive matches have a probability of almost 60%, they can be of
any type in the probabilistic model, even though a majority of them are antagonistic. Stakeless
matches are always unimportant, but some asymmetric matches become unimportant, too, if the
non-indifferent team is almost certainly qualified or eliminated. The remaining asymmetric games
are either defensive or offensive asymmetric. The joint probability of defensive and offensive
asymmetric matches is higher than the probability of asymmetric matches in the deterministic
model, because some competitive matches have an essentially guaranteed outcome for one of the



                                                 14
opposing teams. Even a collusive match may be unimportant if the two teams with 4 points have
a sufficiently high goal difference after two rounds. While most collusive games are defensive,
the majority of defensive matches come from competitive matches. Finally, antagonistic and
offensive matches are always competitive.
    To summarise, the two match classification models do differ to a substantial extent, as
illustrated by Table 4. The probabilistic model does not only refine the categories in the
deterministic approach, but also gives an important insight into the incentives of the opposing
teams.


5     The effects of the 2026 reform package
Now we evaluate the impact of the three main changes in the format of the 2026 FIFA World Cup
group stage: a) increasing the number of teams from 32 to 48 (Expansion effect); b) allowing the
qualification of two-thirds of the third-placed teams besides the group winners and the runners-up
(Qualification effect); and (c) preferring head-to-head results to goal difference in breaking ties
(Tie-breaking effect). The analysis is conducted by computing the probability of each type of
game according to the recently developed, more sophisticated probabilistic match classification
model.
    All of these rule changes are expected to influence the distribution of matches. First, the
higher number of participants directly increases the differences between the strengths of the
teams in all groups, especially because the allocation of slots among the FIFA confederations
does not ensure the qualification of the best teams (Stone and Rod, 2016; Csató, 2023c), and this
problem has been aggravated with 48 teams (Krumer and Moreno-Ternero, 2023). Second, when
more teams qualify from a group, they are more (less) likely to qualify (be eliminated) before the
last round—and the interplay of these opposite tendencies needs to be explored. Third, favouring
head-to-head records over goal difference may have non-negligible consequences with respect to
the set of possible outcomes in the final group ranking (Csató, 2023b, 2025c).
    Figure 2 presents the frequencies of the six match categories for the five FIFA World Cups
between 2010 and 2026. The proportion of unimportant games is doubled, from less than 20% to
almost 40%, which might be worrying since both teams have few incentives to exert full effort in
these games. In contrast, the ratio of defensive asymmetric matches appears to be similar in all
editions of the FIFA World Cup. There is also a notable decrease in the frequency of offensive
asymmetric games, where one team is indifferent, and the other has to focus on attacking.
    Defensive matches have the lowest probability of occurrence in each case. Nonetheless, their
current chance of around 4.7% implies that at least one game out of the 24 played in the last
round will be defensive with a probability of more than 70%. A defensive match is expected to
be boring as both opponents should defend rather than attack, and might threaten fairness by
raising the suspicion of collusive behaviour, especially if a draw finally results in the qualification
of both teams at the expense of a third one (Guyon, 2020).
    In contrast, the changes in the proportion of attractive offensive and antagonistic games
are favourable. The former is at least tripled compared to the 32-team format, while the latter
decreases from at least 40% to less than 20%. Note that offensive games are probably even more
attractive than antagonistic games since both teams need to play offensively.
    Figure 3 details these changes by clustering the groups according to their standing before the
last round (Table 1), and reporting the results for four different formats:

      • Standard 32-team format, used in the FIFA World Cup group stage until 2022 (top
        two teams qualify from each group, the primary tie-breaking rule is goal difference);


                                                  15
         Unimportant




 Defensive asymmetric




 Offensive asymmetric




             Defensive




             Offensive




          Antagonistic


                         0    5     10     15     20       25    30     35     40     45     50
                                                       Proportion (%)
          2026 FIFA World Cup             2022 FIFA World Cup            2018 FIFA World Cup
          2014 FIFA World Cup             2010 FIFA World Cup

                   Figure 2: Probabilistic match classification in the last
                     round of simulated FIFA World Cup group stages


      • Expanded 48-team format (top two teams qualify from each group, the primary tie-
        breaking rule is goal difference);

      • Expanded 48-team format with new qualification rules (top two teams qualify from
        each group together with the eight best third-placed teams, the primary tie-breaking
        rule is goal difference);

      • Expanded 48-team format with new qualification and tie-breaking rules, used in the
        2026 FIFA World Cup group stage (top two teams qualify from each group together
        with the eight best third-placed teams, the primary tie-breaking rule is head-to-head
        result).

     The probability of the 15 cases is independent of the qualification and tie-breaking rules, but
it is hugely influenced by the composition of teams. Increasing the number of teams to 48 strongly
worsens competitive balance; for example, the chance that two teams win their first two matches
(scenario 15) increases from 7.8% to 20%, which is mainly responsible for the higher frequency of
unimportant matches. However, the post-2026 qualification rules make most matches between
the two teams with two losses each offensive or offensive asymmetric, since the winner can qualify
among the best third-placed teams. The tie-breaking rules have a non-negligible effect, too: they


                                                16
                   32 teams, top two teams qualify,                             48 teams, top two teams qualify,
                           goal difference                                              goal difference

 2-2-2-2 (1)                                                  2-2-2-2 (1)
 3-3-3-3 (2)                                                  3-3-3-3 (2)
 4-2-2-1 (3)                                                  4-2-2-1 (3)
 4-3-2-1 (4)                                                  4-3-2-1 (4)
 4-3-3-1 (5)                                                  4-3-3-1 (5)
 4-4-1-1 (6)                                                  4-4-1-1 (6)
 4-4-1-1 (7)                                                  4-4-1-1 (7)
 4-4-2-0 (8)                                                  4-4-2-0 (8)
 4-4-3-0 (9)                                                  4-4-3-0 (9)
6-2-1-1 (10)                                                 6-2-1-1 (10)
6-3-1-1 (11)                                                 6-3-1-1 (11)
6-3-3-0 (12)                                                 6-3-3-0 (12)
6-3-3-0 (13)                                                 6-3-3-0 (13)
6-4-1-0 (14)                                                 6-4-1-0 (14)
6-6-0-0 (15)                                                 6-6-0-0 (15)
               0         5        10      15       20                       0         5        10      15     20
                             Probability (%)                                              Probability (%)


                48 teams, the best third-placed                                  48 teams, the best third-placed
               teams also qualify, goal difference                              teams also qualify, head-to-head

 2-2-2-2 (1)                                                  2-2-2-2 (1)
 3-3-3-3 (2)                                                  3-3-3-3 (2)
 4-2-2-1 (3)                                                  4-2-2-1 (3)
 4-3-2-1 (4)                                                  4-3-2-1 (4)
 4-3-3-1 (5)                                                  4-3-3-1 (5)
 4-4-1-1 (6)                                                  4-4-1-1 (6)
 4-4-1-1 (7)                                                  4-4-1-1 (7)
 4-4-2-0 (8)                                                  4-4-2-0 (8)
 4-4-3-0 (9)                                                  4-4-3-0 (9)
6-2-1-1 (10)                                                 6-2-1-1 (10)
6-3-1-1 (11)                                                 6-3-1-1 (11)
6-3-3-0 (12)                                                 6-3-3-0 (12)
6-3-3-0 (13)                                                 6-3-3-0 (13)
6-4-1-0 (14)                                                 6-4-1-0 (14)
6-6-0-0 (15)                                                 6-6-0-0 (15)
               0         5        10      15       20                       0         5        10      15     20
                             Probability (%)                                              Probability (%)
                        Unimportant            Defensive asymmetric                    Offensive asymmetric
                        Defensive              Offensive                               Antagonistic

                          Figure 3: Probabilistic match classification in the
                       last round of different formats for the FIFA World Cup


turn the majority of offensive asymmetric matches into unimportant ones in scenarios 9 and 12.
    Finally, Figure 4 aggregates the detailed results reported in Figure 3 and decomposes the
changes in the distribution of match types in order to explore the implications of the three
main effects separately. First, the expansion to 48 teams essentially shifts one-eighth of all
games played in the last round from antagonistic to unimportant, which is clearly detrimental to
attractiveness. The easing of qualification reduces the proportion of antagonistic matches by


                                                        17
         Unimportant


 Defensive asymmetric


 Offensive asymmetric


            Defensive


             Offensive

         Antagonistic

                          −30    −25   −20    −15     −10   −5         0   5    10     15        20
                            Difference in the probability of match category (percentage points)
                         Expansion effect       Qualification effect       Tie-breaking effect

         Figure 4: Decomposition of changes in the distribution of probabilistic
       match categories in the last round of the 2026 FIFA World Cup group stage


even more, exceeding 15 percentage points. But the balance seems to be beneficial: the increase
in the frequency of offensive matches greatly exceeds that of defensive matches. About 2-3% of
all last-round games are also moved from offensive asymmetric to defensive asymmetric, which is
not welcome from the perspective of attractiveness. Last but not least, tie-breaking rules affect
mainly unimportant and offensive asymmetric matches, with an increase in the former category
of about 5.6 percentage points. This is in line with previous results; preferring head-to-head
results has been demonstrated to lead to more stakeless (Csató, 2023b) and collusive (Csató,
2025c) games in the deterministic model applied to round-robin contests among four teams.


6     Concluding remarks
The current paper has attempted to achieve two aims. Our first, theoretical goal has been a
better understanding of a recently developed probabilistic match classification model (Csató
and Gyimesi, 2026b) by comparing it with the traditional deterministic approach (Ribeiro and
Urrutia, 2005; Chater et al., 2021; Csató et al., 2024; Devriesere et al., 2026a). For this purpose,
the format of a single round-robin group with four teams, where the first two teams qualify, has
been chosen. In this simple but extensively used case, the number of possible scenarios before the
last round remains manageable, and allows the identification of the deterministic match types
without using integer programming. By classifying the matches played in three historic FIFA
World Cups, we have demonstrated the usefulness of the sophisticated probabilistic classification
model, as all the six possible types of games have occurred in the 2018 competition. Furthermore,
the probabilistic model has been shown to be fundamentally different from the deterministic
model considered in the previous literature; for example, competitive matches can be of any type
in our probabilistic framework.
    Inspired by this promising clustering method, our second, practical goal has been exploring how
the recent reform of the FIFA World Cup in 2026 has changed the distribution of matches. Since
this has been a comprehensive package consisting of three main elements, we have decomposed


                                                 18
the consequences of the increase in the number of teams, as well as the implications of the
modified qualification and tie-breaking rules. Even though the participation of 16 weaker teams
undeniably reduces the attractiveness of the last round played in the group stage by worsening
competitive balance, allowing the qualification of the best third-placed teams is favourable for
attractiveness due to exchanging antagonistic matches with offensive matches, where a draw is
no longer advantageous for any team. In contrast, using head-to-head results as the primary
criteria for breaking ties does not support competition due to restricting the set of possible group
rankings after the first two rounds.
    Our findings can be interesting for any tournament organiser planning to change the number of
participants, the qualification system, or the tie-breaking principles, especially if the competition
contains single round-robin groups of four teams. This format often appears in major sports,
such as in the FIBA Basketball World Cup, the FIFA World Cup and the UEFA European
Championship (in association football), the IHF World Handball Championship, or the FIVB
Volleyball World Championship. We encourage governing bodies to carry out similar investigations
in the future, even before similar reforms are introduced, and discuss with all stakeholders whether
they can accept the expected consequences.
    To summarise, this paper reinforces the validity of a recently proposed probabilistic approach
to match classification and will probably inspire further studies that analyse the effects of rule
changes in the design of sports competitions. Hopefully, it can also contribute to stronger
collaboration between the academic community and decision-makers in sports.


Acknowledgements
We are grateful to two anonymous colleagues for useful remarks.
The research was supported by the National Research, Development and Innovation Office under
Grants Advanced 152220 and FK 145838, and the János Bolyai Research Scholarship of the
Hungarian Academy of Sciences.


References
BBC (2018). World Cup: England’s game v Colombia ‘biggest knockout game for decade’. 28
 June. https://www.bbc.com/sport/football/44650417.

BBC (2022). World Cup 2022 - Cameroon 1-0 Brazil: Cameroon out despite win over Brazil. 2
  December. https://www.bbc.com/sport/football/63752145.

Buraimo, B., Forrest, D., McHale, I. G., and Tena, J. D. (2022). Armchair fans: Modelling
  audience size for televised football matches. European Journal of Operational Research,
  298(2):644–655.

Cea, S., Durán, G., Guajardo, M., Sauré, D., Siebert, J., and Zamorano, G. (2020). An analytics
  approach to the FIFA ranking procedure and the World Cup final draw. Annals of Operations
  Research, 286(1-2):119–146.

Chater, M., Arrondel, L., Gayant, J.-P., and Laslier, J.-F. (2021). Fixing match-fixing: Optimal
  schedules to promote competitiveness. European Journal of Operational Research, 294(2):673–
  683.

Csató, L. (2021). Tournament Design: How Operations Research Can Improve Sports Rules.
  Palgrave Pivots in Sports Economics. Palgrave Macmillan, Cham, Switzerland.

                                                 19
Csató, L. (2022). Quantifying incentive (in)compatibility: A case study from sports. European
  Journal of Operational Research, 302(2):717–726.

Csató, L. (2023a). Group draw with unknown qualified teams: A lesson from the 2022 FIFA
  World Cup. International Journal of Sports Science & Coaching, 18(2):539–551.

Csató, L. (2023b). How to avoid uncompetitive games? The importance of tie-breaking rules.
  European Journal of Operational Research, 307(3):1260–1269.

Csató, L. (2023c). Quantifying the unfairness of the 2018 FIFA World Cup qualification.
  International Journal of Sports Science & Coaching, 18(1):183–196.

Csató, L. (2025a). The fairness of the group draw for the FIFA World Cup. International Journal
  of Sports Science & Coaching, 20(2):554–567.

Csató, L. (2025b). Mitigating the risk of tanking in multi-stage tournaments. Annals of Operations
  Research, 344(1):135–151.

Csató, L. (2025c). On head-to-head results as tie-breaker and consequent opportunities for
  collusion. IMA Journal of Management Mathematics, 36(2):215–230.

Csató, L. and Gyimesi, A. (2026a). Increasing competitiveness by imbalanced groups: The ex-
  ample of the 48-team FIFA World Cup. European Journal of Operational Research, 332(3):868–
  879.

Csató, L. and Gyimesi, A. (2026b). A probabilistic match classification model for low-scoring
  sports. Manuscript. DOI: 10.48550/arXiv.2601.09673.

Csató, L., Kiss, L. M., and Szádoczki, Zs. (2025). The allocation of FIFA World Cup slots based
  on the ranking of confederations. Annals of Operations Research, 344(1):153–173.

Csató, L., Molontay, R., and Pintér, J. (2024). Tournament schedules and incentives in a double
  round-robin tournament with four teams. International Transactions in Operational Research,
  31(3):1486–1514.

Devriesere, K., Csató, L., and Goossens, D. (2025). Tournament design: A review from an
  operational research perspective. European Journal of Operational Research, 324(1):1–21.

Devriesere, K., Goossens, D., and Spieksma, F. (2026a). From groups to a single league:
  Evaluating competitiveness in the UEFA Champions League. Journal of Quantitative Analysis
  in Sports, in press. DOI: 10.1515/jqas-2025-0128.

Devriesere, K., Goossens, D., and Willem, A. (2026b). Manipulation unraveled: A new framework
  to analyze the impact of tournament design on manipulation opportunities. International
  Journal of Sports Science & Coaching, 21(1):638–652.

Di Mattia, A. and Krumer, A. (2026). The effect of reducing the number of matches in round-
  robin tournaments with four teams: Evidence from beach volleyball. Annals of Operations
  Research, 360(2-3):951–977.

FIFA (2017). Unanimous decision expands FIFA World CupTM to 48 teams from 2026. 10
  January. https://web.archive.org/web/20170110231324/http://www.fifa.com/about-
  fifa/news/y=2017/m=1/news=fifa-council-unanimously-decides-on-expansion-of-
  the-fifa-world-cuptm--2863100.html.

                                               20
FIFA (2023). FIFA Council approves international match calendars. 14 March. https://ww
  w.fifa.com/about-fifa/organisation/fifa-council/media-releases/fifa-council-
  approves-international-match-calendars.

Football rankings (2020). Simulation of scheduled football matches. 28 December. https:
  //web.archive.org/web/20260607105217/http://www.football-rankings.info/2020/1
  2/simulation-of-scheduled-football-matches.html.

Guyon, J. (2015). Rethinking the FIFA World CupTM final draw. Journal of Quantitative
 Analysis in Sports, 11(3):169–182.

Guyon, J. (2020). Risk of collusion: Will groups of 3 ruin the FIFA World Cup? Journal of
 Sports Analytics, 6(4):259–279.

Guyon, J. (2022). “Choose your opponent”: A new knockout design for hybrid tournaments.
 Journal of Sports Analytics, 8(1):9–29.

Gyimesi, A. (2024). Competitive balance in the post-2024 Champions League and the European
  Super League: A simulation study. Journal of Sports Economics, 25(6):707–734.

Johnston, N. (2026). Rest your best or go strong? Norway face questions as Haaland left out. 27
  June. https://www.bbc.com/sport/football/articles/cp3xd37np9po.

Kendall, G. and Lenten, L. J. A. (2017). When sports rules go awry. European Journal of
 Operational Research, 257(2):377–394.

Krumer, A. and Moreno-Ternero, J. (2023). The allocation of additional slots for the FIFA
  World Cup. Journal of Sports Economics, 24(7):831–850.

Lapré, M. A. and Palazzolo, E. M. (2023). The evolution of seeding systems and the impact of
  imbalanced groups in FIFA Men’s World Cup tournaments 1954–2022. Journal of Quantitative
  Analysis in Sports, 19(4):317–332.

Lenten, L. J. A. and Kendall, G. (2022). Scholarly sports: Influence of social science academe on
  sports rules and policy. Journal of the Operational Research Society, 73(12):2591–2601.

Maher, M. J. (1982). Modelling association football scores. Statistica Neerlandica, 36(3):109–118.

Medina, J. (2026). Formats shape incentives: A quantitative evaluation of the 2026 FIFA World
 Cup and alternative designs. Manuscript. DOI: 10.2139/ssrn.7107799.

Ribeiro, C. C. and Urrutia, S. (2005). An application of integer programming to playoff elimination
  in football championships. International Transactions in Operational Research, 12(4):375–386.

Scarf, P., Yusof, M. M., and Bilbao, M. (2009). A numerical study of designs for sporting contests.
  European Journal of Operational Research, 198(1):190–198.

Scarf, P. A. and Shi, X. (2008). The importance of a match in a tournament. Computers &
  Operations Research, 35(7):2406–2418.

Schilling, M. F. (1994). The importance of a game. Mathematics Magazine, 67(4):282–288.

Stone, C. and Rod, M. (2016). Unfair play in World Cup qualification? An analysis of the
  1998–2010 FIFA World Cup performances and the bias in the allocation of tournament berths.
  Soccer & Society, 17(1):40–57.

                                               21
Stronka, W. (2024). Demonstration of the collusion risk mitigation effect of random tie-breaking
  and dynamic scheduling. Sports Economics Review, 5:100025.

Stuart, J. (2018). Denmark join France in last 16 after first goalless draw of World Cup. The
  Guardian. 26 June. https://www.theguardian.com/football/2018/jun/26/denmark-
  france-world-cup-group-c-match-report.

Vong, A. I. K. (2017). Strategic manipulation in tournament games. Games and Economic
  Behavior, 102:562–567.

Wright, M. (2009). 50 years of OR in sport. Journal of the Operational Research Society,
 60(Supplement 1):S161–S168.

Wright, M. (2014). OR analysis of sporting rules – A survey. European Journal of Operational
 Research, 232(1):1–8.




                                              22
     Appendix

                       Table A.1: Classification of matches played in the last
                         round of the 2014 FIFA World Cup group stage

                                                                                                Model
Group   Team 1            Team 2            ℒ1 (%)    𝒢1 (%)   ℒ2 (%)    𝒢2 (%)      𝜅
                                                                                            Det.   Prob.
 A      Brazil            Cameroon          26.10       0         0        0       26.10     AS     DAS
 A      Croatia           Mexico             0.79     99.21      100       0       98.42     C      AN
 B      Netherlands       Chile               0         0         0        0          0       S       U
 B      Spain             Australia            0        0         0         0        0        S       U
 C      Colombia          Japan               0         0         0      48.61     48.61     AS     OAS
 C      Greece            Ivory Coast         0       82.03     90.49     9.51     80.98     C      AN
 D      Costa Rica        England             0         0         0        0          0       S       U
 D      Uruguay           Italy               0        100       100       0        100      C      AN
 E      Ecuador           France            27.34     49.66      0.34      0        0.34     C      OAS
 E      Switzerland       Honduras          38.32     34.51        0      6.38      3.81     C      AN
 F      Argentina         Nigeria             0         0       28.05      0       28.05     AS     DAS
 F      Bosnia and H.     Iran                 0        0          0     65.24     65.24     AS     OAS
 G      Germany           United States      1.72       0       41.48      0       41.48    COL     DAS
 G      Portugal          Ghana               0       26.61       0      51.37     26.61     C        O
 H      Algeria           Russia            98.16      1.84       0      97.45     96.32     C      AN
 H      Belgium           South Korea         0          0        0      13.56     13.56     AS     OAS
 Teams: Bosnia and H. stands for Bosnia and Herzegovina.
 Models: Det. stands for Deterministic, Prob. stands for Probabilistic.
 Deterministic match types: AS = asymmetric; C = competitive; COL = collusive; S = stakeless.
 Probabilistic match types: AN = antagonistic; D = defensive; DAS = defensive asymmetric; O = offensive; OAS =
 offensive asymmetric; U = unimportant.




                                                     23
                       Table A.2: Classification of matches played in the last
                         round of the 2018 FIFA World Cup group stage

                                                                                               Model
Group   Team 1           Team 2          ℒ1 (%)     𝒢1 (%)   ℒ2 (%)    𝒢2 (%)       𝜅
                                                                                            Det.  Prob.
 A      Russia           Uruguay            0         0         0         0         0        S       U
 A      Saudi Arabia     Egypt              0         0          0        0         0        S       U
 B      Portugal         Iran             98.01       0        1.86     98.14     96.28      C     AN
 B      Spain            Morocco          18.51       0          0        0       18.51     AS     DAS
 C      Australia        Peru               0       51.21       0         0       51.21     AS     OAS
 C      France           Denmark            0         0       17.91       0       17.91     AS     DAS
 D      Argentina        Nigeria            0       86.48     88.13     11.87     76.26      C     AN
 D      Iceland          Croatia            0       39.63       0         0       39.63     AS     OAS
 E      Brazil           Serbia           81.38       0        8.47     91.53     81.38      C     AN
 E      Switzerland      Costa Rica       12.96       0         0         0       12.96     AS     DAS
 F      Germany          South Korea      48.17     46.58       0       28.34      1.59      C       O
 F      Mexico           Sweden           81.94       0       5.71      93.90     81.94      C     AN
 G      Belgium          England            0         0         0         0         0        S       U
 G      Panama           Tunisia            0         0          0        0          0       S       U
 H      Poland           Japan              0         0       59.03       0       59.03     AS     DAS
 H      Senegal          Colombia         78.91       0       58.02     41.98     16.04      C       D
 Models: Det. stands for Deterministic, Prob. stands for Probabilistic.
 Deterministic match types: AS = asymmetric; C = competitive; COL = collusive; S = stakeless.
 Probabilistic match types: AN = antagonistic; D = defensive; DAS = defensive asymmetric; O = offensive; OAS =
 offensive asymmetric; U = unimportant.




                                                    24
