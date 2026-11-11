<!-- source: library/preprints/arXiv/2026/2026 - The maximum concentration of results in incomplete round-robin tournaments - Cs ji et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.01750 -->
<!-- authors: Gergely Csáji, László Csató -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-11; equations, tables and figures are NOT preserved - consult the PDF for those -->

# The maximum concentration of results in incomplete round-robin tournaments

                                                                The maximum concentration of results
                                                               in incomplete round-robin tournaments
                                                                         Gergely Csájia                László Csatób


                                                                                    3rd November 2026
arXiv:2611.01750v1 [math.OC] 1 Nov 2026




                                          “The arguments above make it clear that the varying upper and lower bounds of HHI need to be
                                          taken into account to obtain a measure of competitive balance that is generally applicable for
                                          comparisons over time or across different leagues” (Owen et al., 2007, p. 293).


                                                                                           Abstract
                                                The Herfindahl–Hirschman Index (HHI), a standard measure of market concentration, is
                                                widely used to quantify competitive balance in sports tournaments. To enable comparisons
                                                over time or across leagues, both its minimum and maximum should be known. The minimum
                                                is usually trivial. Our paper provides results on the maximum HHI in incomplete round-robin
                                                tournaments, where the set of matches is represented by a regular but not complete undirected
                                                graph. We prove that the lower bound of maximum HHI is reached when the tournament
                                                consists of independent round-robin groups, while the upper bound of maximum HHI is
                                                reached when the set of matches is represented by a bipartite graph. Maximising HHI is
                                                computationally difficult even for highly structured graph types corresponding to real-world
                                                tournaments, where the teams are partitioned into pots and play the same number of matches
                                                against opponents from every pot. The complexity of the problem does not depend on the
                                                scoring system or the number of opponents from a pot.
                                                Keywords: graph theory; Herfindahl–Hirschman index; incomplete round-robin tournament;
                                                OR in sports; sports economics
                                                MSC class: 62P20, 90-08, 91-08
                                                JEL classification number: C44, D63, L83, Z20




                                             a
                                                Email: csajigergely@sztaki.hu
                                          Institute for Computer Science and Control (SZTAKI), Hungarian Research Network (HUN-REN), Laboratory on
                                          Engineering and Management Intelligence, Budapest, Hungary
                                          Budapest University of Technology and Economics, Department of Computer Science and Information Theory,
                                          Faculty of Electrical Engineering and Informatics, Hungary
                                             b
                                                Corresponding author. Email: laszlo.csato@sztaki.hun-ren.hu
                                          Institute for Computer Science and Control (SZTAKI), Hungarian Research Network (HUN-REN), Laboratory
                                          on Engineering and Management Intelligence, Research Group of Operations Research and Decision Systems,
                                          Budapest, Hungary
                                          Corvinus University of Budapest (BCE), Institute of Operations and Decision Sciences, Department of Operations
                                          Research and Actuarial Sciences, Budapest, Hungary
1    Introduction
Competitive balance, the inequality observed in match outcomes in a tournament, is a funda-
mental concept of sports economics (Szymanski, 2003). Sports have a unique economic structure
where, besides competing against each other, multiple teams jointly create another “product”,
the overall league competition. Therefore, in order to keep fans engaged and maximise the
entertainment value of the league, it is essential in all leagues to maintain balance and prevent
the long-term domination of some teams.
    There are two basic tournament formats: the knockout and round-robin competitions. In a
knockout competition, a loser is immediately eliminated; thus, competitive balance is always
perfect. In a round-robin competition, every team plays the same number of matches against
any other team, and competitive balance becomes a crucial issue.
    Obviously, competitive balance has many dimensions, which implies the existence of various
competitive balance measures (Humphreys, 2002; Fort and Maxcy, 2003; Csató and Petróczy,
2025). Since competitive balance is closely related to the inequality of match outcomes, standard
concentration measures from the literature on income distribution and industrial organisation,
such as the Gini coefficient (Schmidt and Berri, 2001) and relative entropy (Horowitz, 1997), are
widely used to measure competitive balance. Another well-known measure from this category
is the Herfindahl–Hirschman index (HHI ) (Herfindahl, 1950; Hirschman, 1945, 1964). As a
measure of competitive balance, HHI is the sum of the squares of teams’ shares from the total
points allocated in a league (Depken, 1999). The number of teams in a round-robin tournament
affects both the lower (Depken, 1999) and upper bounds (Owen et al., 2007; Avila-Cano et al.,
2021) of the Herfindahl–Hirschman index; hence, it is usually normalised based on these two
extremes to lie in the [0, 1] unit interval (Owen and Owen, 2022; Avila-Cano et al., 2023).
    In recent years, another tournament format, the incomplete round-robin, has also become
popular in the world of sports. The Union of European Football Associations (UEFA) has
changed the design of its club competitions to an incomplete round-robin from the 2024/25
season, and will organise its national team competitions in this format from 2028 (UEFA, 2026).
    In an incomplete round-robin tournament, each team plays the same number of matches,
but they play only against a subset of the other teams (Cochran, 1971; Devriesere et al., 2025).
In contrast to the Swiss-system (Csató, 2017; Sauer et al., 2024), the schedule of matches is
fixed in advance. The incomplete round-robin tournament is effective in reducing travel distance
and capacity violations (Devriesere and Goossens, 2025; Li et al., 2025), as well as in avoiding
non-competitive matches (Csató and Gyimesi, 2026; Devriesere et al., 2026).
    If the teams play the same number of matches, the minimum HHI is the reciprocal of the
number of teams when all matches result in a draw. However, regarding the other extreme, several
interesting questions arise for incomplete round-robin tournaments: What is the maximum value
of HHI ? What is the computational complexity of finding this upper bound? Can reasonable
restrictions simplify the problem? The current paper attempts to answer these questions.

Our contributions      First, we characterise tournaments with the highest and lowest maximum
HHI values. The highest attainable HHI in an incomplete round-robin tournament with 𝑁
teams, under either the (2, 1, 0) or (3, 1, 0) scoring system, is 2/𝑁 , with equality precisely when


                                                 2
the set of matches is represented by a bipartite graph (Theorem 1). Intuitively, bipartite graphs
allow half of the teams to win all their matches, concentrating points as much as possible. At
the opposite extreme, the lowest maximum HHI is attained when the tournament consists of
disjoint round-robin groups (Theorem 3), as such a structure restricts the concentration of
wins by confining them to small groups. If the number of teams does not allow creating such
equal groups, the lower bound breaks down (Proposition 1). Our proof uses equitable graph
colouring and majorisation to show that any other match schedule allows an at least as unequal
distribution of points. Theorem 2 also provides a formula for computing this extremal value.
    We then investigate the computational complexity of maximising HHI for a given tournament
graph. Although the objective involves squared scores, the main difficulty resides in the
combinatorial dependencies between match outcomes. We prove 𝒩 𝒫-hardness even for highly
structured graph types corresponding to real-world tournaments, where the teams are partitioned
into pots and play the same number of matches against opponents from every pot. In particular,
Theorem 5 shows this for the (𝜔, 1, 0) scoring system with 𝜔 ≥ 3, while Theorem 7 proves
hardness for the (2, 1, 0) scoring system. If the total number of points is fixed (draws are
prohibited or the (2, 1, 0) scoring system is applied), maximising HHI amounts to maximising the
sum of squared wins, which we relate to the minimum odd-cycle transversal problem through a
reduction from Not-All-Equal 3-SAT. The (3, 1, 0) scoring system is more challenging to analyse,
since draws change both the numerator and denominator of HHI . Our reduction encodes a
satisfiability instance using variable cycles and clause triangles: alternating winning patterns
represent truth assignments, and clause gadgets enforce satisfaction. Finally, carefully chosen
auxiliary graphs are used to translate this combinatorial structure into the fractional HHI
objective.

    Our study is not the first to examine incomplete round-robin tournaments from the perspective
of graph theory. Li et al. (2025) provide theoretical results on the complexity of constructing an
incomplete round-robin tournament. de Werra et al. (2026) consider the problem of minimising
the number of breaks (two consecutive home or two consecutive away games); Devriesere et al.
(2027) aim to find break-free timetables that minimise venue capacity violations. Wessel and
Spieksma (2026) establish the complexity of determining whether there exists a fair draw where
the strengths of the opponent sets are equal for each team. However, none of these previous
works involves finding match outcomes to optimise an objective function, which we will do.
    The paper is organised as follows. Section 2 introduces the problem. Section 3 derives strict
lower and upper bounds on the maximum HHI in incomplete round-robin tournaments. Section 4
deals with the complexity of computing the maximum HHI . Finally, Section 5 concludes.


2    Preliminaries
Let 𝐺 = (𝑉, 𝐸) be a 𝑑-regular undirected graph representing the set of matches played in an
incomplete round-robin tournament, where the vertices are the teams and the edges are the
matches. Each match between teams 𝑣 and 𝑢 has three possible outcomes: team 𝑣 wins, team 𝑣
loses, or the result is a draw. Denote the number of teams by |𝑉 | = 𝑁 .
    For each vertex 𝑣 ∈ 𝑉 , let 𝑤𝑣 , 𝑑𝑣 , ℓ𝑣 denote the number of wins, draws, and losses, respectively,

                                                   3
     Figure 1: The graph corresponding to the group stage of the Romanian football cup


such that 𝑤𝑣 + 𝑑𝑣 + ℓ𝑣 = deg(𝑣). If scoring system (𝜔, 1, 0) is used to rank the teams, the score
of vertex 𝑣 is given by 𝑝𝑣 = 𝜔𝑤𝑣 + 𝑑𝑣 , where 𝜔 is the value of a win.
   We aim to find a valid orientation of outcomes on 𝐸 that maximises competitive imbalance,
measured by the Herfindahl–Hirschman index (HHI 𝜔 ) of the tournament. HHI 𝜔 is the sum of
squared scores divided by the square of total points:
                                                   ∑︀    2
                                                    𝑣∈𝑉 𝑝𝑣
                                     HHI 𝜔 (𝐺) =           ,
                                                     𝑃2
            ∑︀
where 𝑃 =     𝑣∈𝑉 𝑝𝑣 is the total number of points awarded in the tournament.
   The lower bound of HHI 𝜔 , associated with perfect competitive balance, is 1/𝑁 in any graph
𝐺 and for any scoring system (𝜔, 1, 0). It can be easily achieved if all teams collect the same
number of points by playing only draws. The upper bound of HHI 𝜔 is denoted by HHI *𝜔 .
   Let Max-HHI denote the optimisation problem that aims to find the maximum attainable
HHI 𝜔 of a given input graph 𝐺 and scoring system (𝜔, 1, 0).
   Regularity is a natural requirement for a tournament graph, since ranking would be challenging
if the number of matches played by the teams differs (Leiva Bertrán, 2025). However, the
organisers usually impose other constraints in order to avoid high differences between the
strengths of opponents for two teams. This can be achieved by creating pots based on the
strengths of the teams, and drawing the matches such that each team plays the same number of
matches against teams from each pot, possibly without playing against teams from its own pot.
   For example, the Romanian football cup (Cupa României) contains a “group stage” since the
2022/23 season. Each of the four groups contains two teams from Pots 1–3, respectively. Every
team plays one match against one team from each of the three pots in their group. Figure 1
shows the graph associated with a group in this tournament, which is unique if the identities of
the teams are ignored. The maximum of the Herfindahl–Hirschman index is reached under the
point distribution (9,9,9,0,0,0), when half of the teams win all their matches.
   Let 𝐺 = (𝑉, 𝐸) and 𝑉 = 𝑉1 ∪˙ · · · ∪˙ 𝑉𝑘 be a partition into classes of equal size. Denote the
neighbours of 𝑣 by 𝑁 (𝑣) for all 𝑣 ∈ 𝑉 .

      1. The graph (and the partition) is fully balanced with parameter 𝑟 if for all 𝑣 ∈ 𝑉 and
         1 ≤ 𝑗 ≤ 𝑘:
                                             |𝑁 (𝑣) ∩ 𝑉𝑗 | = 𝑟

      2. The graph (and the partition) is externally balanced with parameter 𝑟 if for all 𝑣 ∈ 𝑉𝑖


                                               4
         and 𝑗 ̸= 𝑖:
                                                |𝑁 (𝑣) ∩ 𝑉𝑗 | = 𝑟

    Fully balanced graphs represent tournaments where each team plays exactly 𝑟 matches with
teams from every pot, including its own. Externally balanced graphs differ only in that teams
do not play against other teams from their own pot, but play exactly 𝑟 matches with teams from
every other pot.
    Both structures arise naturally in major European sports competitions since the 2023/24
season. In the league phase of the UEFA Champions League and Europa League, the 36
participating clubs are divided into four seeding pots of nine clubs each, and every club plays
against two opponents from each pot, including its own. Thus, the set of matches yields a fully
balanced graph with 𝑟 = 2. The UEFA Conference League employs six pots of six clubs, with
each club facing exactly one opponent from each pot, giving a fully balanced graph with 𝑟 = 1.
In the Champions Hockey League, the 24 participating teams are divided into four seeding pots
of six teams each, and every team faces exactly two opponents from each of the other three pots.
Thus, the set of matches is represented by an externally balanced graph with parameter 𝑟 = 2.


3      Bounds on the maximum Herfindahl–Hirschman index
In this section, we study HHI in incomplete round-robin tournaments, and show that it has a
strict, structurally bounded global maximum. In particular, Section 3.1 establishes an upper
bound on HHI *𝜔 , Section 3.2 computes HHI *𝜔 in disjoint round-robin tournaments, and Section 3.3
establishes a lower bound on HHI *𝜔 . Recent results about the maximum HHI in round-robin
tournaments are summarised in Appendix A.
    Throughout this section, 𝜔 ≥ 2 is assumed to be an exogenous integer. The case 𝜔 = 3,
which corresponds to the standard football scoring system, is stated explicitly whenever the
general formula is less transparent.

3.1     Upper bound and characterisation
The following result provides a strict upper bound on the maximum Herfindahl–Hirschman index
for incomplete round-robin tournaments.

Theorem 1. Let 𝐺 be a 𝑑-regular graph representing an incomplete round-robin tournament.
Then
                                                         𝐶𝜔
                                          HHI *𝜔 (𝐺) ≤      ,
                                                         𝑁
where                              ⎧
                                   ⎨2,
                                   ⎪
                                   ⎪                            𝜔 ∈ {2, 3},
                            𝐶𝜔 =          (𝜔 2 − 2)2
                                   ⎪
                                   ⎪                    ,       𝜔 ≥ 4.
                                       4𝜔(𝜔 − 1)(𝜔 − 2)
                                   ⎩

For 𝜔 ∈ {2, 3}, equality holds if and only if 𝐺 is bipartite. For 𝜔 ≥ 4, put

                                               2(𝜔 2 − 2𝜔 + 2)
                                       𝜌𝜔 :=                    .
                                               (𝜔 2 − 2)(𝜔 − 2)

                                                   5
Equality holds if and only if 𝐺 is the disjoint union of a 𝑑-regular bipartite graph on 𝜌𝜔 𝑁 vertices
and a 𝑑-regular graph on the remaining vertices; no match in the first graph is a draw and all
matches in the second graph are draws.

Proof. Let 𝑊 be the total number of wins in the tournament. Because 𝐺 is 𝑑-regular, the
number of edges is 𝑁 𝑑/2. The total sum of draw-degrees is 𝑁 𝑑 − 2𝑊 . Thus, the sum of points is

                            𝑃 = 𝜔𝑊 + (𝑁 𝑑 − 2𝑊 ) = 𝑁 𝑑 + (𝜔 − 2)𝑊.                                     (1)

   Using 𝑤𝑣 + 𝑑𝑣 + ℓ𝑣 = 𝑑, we get 𝑤𝑣2 = 𝑑𝑤𝑣 − 𝑤𝑣 𝑑𝑣 − 𝑤𝑣 ℓ𝑣 and 𝑑2𝑣 = 𝑑𝑑𝑣 − 𝑤𝑣 𝑑𝑣 − ℓ𝑣 𝑑𝑣 .
Expanding the squared points (𝜔𝑤𝑣 + 𝑑𝑣 )2 and using                                𝑣 𝑑𝑣 = 𝑁 𝑑 − 2𝑊 :
                                                               ∑︀                 ∑︀
                                                                   𝑣 𝑤𝑣 = 𝑊 and


                                    𝑆 = 𝑁 𝑑2 + 𝑑(𝜔 2 − 2)𝑊 − Γ𝜔 ,                                      (2)

where
                                 ∑︁ (︁                                    )︁
                         Γ𝜔 :=           𝜔 2 𝑤𝑣 ℓ𝑣 + (𝜔 − 1)2 𝑤𝑣 𝑑𝑣 + 𝑑𝑣 ℓ𝑣 ≥ 0.
                                 𝑣∈𝑉

   Put 𝑥 := 𝑊/(𝑁 𝑑). Since 0 ≤ 𝑊 ≤ 𝑁 𝑑/2, we have 0 ≤ 𝑥 ≤ 1/2, and consequently

                                                    1 1 + (𝜔 2 − 2)𝑥
                                  HHI 𝜔 (𝐺) ≤                         .                                (3)
                                                    𝑁 (1 + (𝜔 − 2)𝑥)2

   The derivative of this fraction as a function of 𝑥 has the same sign as

                                  𝜔 2 − 2𝜔 + 2 − (𝜔 2 − 2)(𝜔 − 2)𝑥.

For 𝜔 ∈ {2, 3}, the expression in (3) is increasing on [0, 1/2], and its value at 𝑥 = 1/2 is 2/𝑁 . In
particular, for 𝜔 ∈ {2, 3} we get
                                                             2
                                             HHI *𝜔 (𝐺) ≤      .
                                                             𝑁
For 𝜔 ≥ 4, the unique maximum is attained at

                                                    𝜔 2 − 2𝜔 + 2
                                          𝑥*𝜔 =                    ,
                                                  (𝜔 2 − 2)(𝜔 − 2)

and substituting this value into (3) gives 𝐶𝜔 /𝑁 .
   Equality in the envelope requires Γ𝜔 = 0. Hence every vertex is a pure winner, a pure
drawer, or a pure loser. For 𝜔 ∈ {2, 3}, equality also requires 𝑥 = 1/2, so there are no draws; the
pure winners and pure losers form the two sides of a bipartition. Conversely, a pure bipartite
orientation attains 2/𝑁 .
   For 𝜔 ≥ 4, equality requires 𝑊 = 𝑥*𝜔 𝑁 𝑑. The pure winners and pure losers therefore form a
𝑑-regular bipartite union on 2𝑊/𝑑 = 𝜌𝜔 𝑁 vertices, while the pure drawers induce a 𝑑-regular
union on the remaining vertices. There can be no edges between these two parts. Conversely,
orienting the first part bipartitely and making every match a draw in the second part attains
the maximum.

Corollary 1. Letting each match be a draw gives a 𝐶𝜔 -approximation to Max-HHI, since this


                                                       6
configuration has HHI 𝜔 = 1/𝑁 . In particular, it is a 2-approximation for 𝜔 ∈ {2, 3}.

   Theorem 1 is not only a theoretical curiosity, as there exist incomplete round-robin tour-
naments where the matches are given by a bipartite graph. We have already discussed the
Romanian football cup in Section 2. The Leagues Cup is an international football competition
for Major League Soccer (MLS) and Mexican clubs. It starts with a league phase since 2025,
contested by 18-18 MLS and Mexican clubs, which are divided into six groups of three teams
each, determined by three tiers based on historical performances and two geographical regions.
In the groups, each team plays against the three teams from the other country; thus, each match
is played by one club from MLS and one from Mexico.

3.2   The maximum HHI in disjoint round-robin tournaments
                               ⋃︀
In this section, we consider        𝐾𝑑+1 . For 𝜔 = 3, the relevant component states are precisely the
truncated cascade distributions studied by Avila-Cano et al. (2021), and their HHI is given by
the formula stated in Section 2. The same score pattern extends to general 𝜔. Since different
components of a disjoint union may be in two adjacent states, we need their total points and
sums of squares separately.
   Starting from the all-draw configuration, an upgrade of a vertex means replacing its draws
against the current bottom tier of its component by wins, one after another. A greedy win
allocation always chooses a vertex having the minimum possible number of losses, completes its
upgrade, and then continues with another such vertex.
   The following lemma gives the complete structural reduction that we need.

Lemma 1 (Structure of an optimal configuration). There exists a configuration maximising
                      ⋃︀
the HHI on 𝐺worst =        𝐾𝑑+1 that is a greedy win allocation in which every started upgrade is
completed. Consequently, every component is in a truncated cascade state: it has singleton upper
tiers and one bottom draw tier. Moreover, the number of fully upgraded vertices in any two
components differs by at most one.

Proof. For 𝜔 = 2, the total number of points is fixed. If a highest-scoring vertex draws against
another vertex, changing that draw into a win of the highest-scoring vertex transfers one point
from the latter vertex to the former and strictly increases the sum of squared scores. Repeating
this argument for second highest scorers, etc., gives the complete cascade in every component.
Hence, all assertions are immediate for 𝜔 = 2.
   Assume from now on that 𝜔 ≥ 3, and put

                                               𝑐𝜔 := 𝜔 − 2.

We use the upper-bound constant 𝐶𝜔 from Theorem 1. In particular, every configuration on the
whole 𝑁 -vertex graph satisfies
                                                             𝐶𝜔
                                                        {︂        }︂
                                          HHI 𝜔 ≤ min 1,               .                          (4)
                                                             𝑁
   We first prove a saturation claim. Divide the vertices into tiers based on their scores: 𝑢, 𝑣
belong to the same tier if and only if 𝑝𝑢 = 𝑝𝑣 . Fix a component and suppose that some vertices


                                                    7
of this component (possibly 0) have already been fixed as singleton upper tiers. Let 𝑅 be the set
of remaining vertices and write
                                                    |𝑅| = 𝑚 + 1.

Among the HHI -maximising configurations respecting the already fixed upper tiers, choose one
that minimises the number of decisive matches inside 𝑅. Let 𝑣 be a highest-scoring vertex of 𝑅.

Step 1: The highest remaining vertex has no loss.
     Suppose that 𝑣 loses to some 𝑢 ∈ 𝑅. Reverse this result, so that 𝑣 defeats 𝑢. The total
number of points remains unchanged, while the score of 𝑣 increases by 𝜔 and the score of 𝑢
decreases by 𝜔. Since 𝑝𝑣 ≥ 𝑝𝑢 , the corresponding change in the sum of squared scores is

                           (𝑝𝑣 + 𝜔)2 + (𝑝𝑢 − 𝜔)2 − 𝑝2𝑣 − 𝑝2𝑢 = 2𝜔(𝑝𝑣 − 𝑝𝑢 ) + 2𝜔 2 > 0.

This contradicts optimality. Hence, 𝑣 has only wins and draws against the other 𝑚 vertices of 𝑅.
    Temporarily replace all these matches by draws. Let

                                               𝑟1 ≤ 𝑟2 ≤ · · · ≤ 𝑟𝑚

be the resulting scores of the other vertices. If 𝑣 defeats a vertex with baseline score 𝑟𝑗 but
draws with a vertex having baseline score 𝑟𝑖 < 𝑟𝑗 , exchange these two results. The score of 𝑣
and the total points remain unchanged, while the change in the sum of squared scores is

                                (𝑟𝑖 − 1)2 + 𝑟𝑗2 − 𝑟𝑖2 − (𝑟𝑗 − 1)2 = 2(𝑟𝑗 − 𝑟𝑖 ) > 0.

Therefore, if 𝑣 has exactly 𝑤 wins, we may assume that it defeats the vertices with baseline
scores 𝑟1 , . . . , 𝑟𝑤 .

Step 2: A highest remaining vertex either draws every match or wins every match.
    The proof of Step 2 is intuitive but technical; thus it is provided in Appendix B.

Step 3: Recursive construction of a truncated cascade.
     Recall that, subject to the already fixed singleton upper tiers, we chose an HHI -maximising
configuration having the minimum number of decisive matches inside 𝑅. If 0 < 𝑤 < 𝑚, the
all-draw boundary has fewer decisive matches. Consequently, it cannot have the same HHI , by
the tie-breaking choice. The all-win boundary must therefore attain the same maximum HHI .
Hence, there exists an optimal configuration in which 𝑣 defeats every other vertex of 𝑅. We fix
𝑣 as the next singleton upper tier and repeat the argument on 𝑅 ∖ {𝑣}.
    The recursion may instead reach a stage at which a highest-scoring remaining vertex 𝑣
already has 𝑤 = 0. Then 𝑣 has score 𝑚. Every other remaining vertex has score at most 𝑚,
and, since it draws with 𝑣, its score from matches inside 𝑅 ∖ {𝑣} is at most 𝑚 − 1. On the other
                                               (︀𝑚)︀
hand, the 𝑚 vertices of 𝑅 ∖ {𝑣} play            2      matches, each awarding at least two points, so their
total score from these matches is at least 𝑚(𝑚 − 1). Hence, every one of them has score exactly
𝑚 − 1 from the induced subtournament, and every match in that subtournament awards exactly
two points. Since 𝜔 ≥ 3, all those matches are draws. Thus, the whole remaining set is one
bottom draw tier.


                                                           8
   Applying this argument independently to every component gives a HHI -maximising config-
uration in which every component is a truncated cascade.

Step 4: The cascade depths of different components differ by at most one.
   Suppose, to the contrary, that two components have bottom draw tiers of sizes 𝑥 ≥ 1 and 𝑦,
where𝑦 ≥ 𝑥 + 2. In the component with bottom size 𝑥, undo the last completed upgrade. This
removes the 𝑥 wins by which one vertex was separated from a bottom tier of size 𝑥 + 1. In the
component with bottom size 𝑦, use these 𝑥 wins to start upgrading one vertex against exactly 𝑥
of its 𝑦 − 1 bottom-tier opponents. The total number of decisive matches, and hence the total
number of points, remains unchanged.
   For a bottom tier of size 𝑧, giving one vertex 𝑤 wins against its peers changes the sum of
squared scores by
                                                                    [︁                       ]︁
             Δ𝑆(𝑧, 𝑤) = [𝑧 − 1 + (𝜔 − 1)𝑤]2 − (𝑧 − 1)2 + 𝑤 (𝑧 − 2)2 − (𝑧 − 1)2
                         = [2𝑐𝜔 (𝑧 − 1) + 1] 𝑤 + (𝜔 − 1)2 𝑤2 .                                            (5)

Therefore, the loss caused by undoing the completed upgrade is Δ𝑆(𝑥 + 1, 𝑥), while the gain in
the other component is Δ𝑆(𝑦, 𝑥). Their difference is

                        Δ𝑆(𝑦, 𝑥) − Δ𝑆(𝑥 + 1, 𝑥) = 2𝑐𝜔 𝑥(𝑦 − 𝑥 − 1) > 0.

We have obtained a configuration with the same total points and a strictly larger sum of squared
scores, contradicting optimality. Hence, the bottom tier sizes of any two components differ by at
most one; equivalently, their number of fully upgraded vertices differs by at most one.

   We are ready to give a formula for the maximum HHI of disjoint round-robin tournaments.
                               ⋃︀𝑁/(𝑑+1)
Theorem 2. Let 𝐺worst =          𝑖=1       𝐾𝑑+1 and put 𝑐 = 𝑁/(𝑑 + 1). Then

                              𝑑+1                                𝛼𝑆𝑐𝜔 (𝑥 − 1) + (1 − 𝛼)𝑆𝑐𝜔 (𝑥)
         HHI *𝜔 (𝐺worst ) =         max           max                                           ,
                               𝑁 𝑥∈{1,...,𝑑+1} 𝛼∈{0,1/𝑐,...,1} [𝛼𝑃𝑐𝜔 (𝑥 − 1) + (1 − 𝛼)𝑃𝑐𝜔 (𝑥)]2

where

                         𝜔𝑑(𝑑 + 1) − (𝜔 − 2)𝑥(𝑥 − 1)
                𝑃𝑐𝜔 (𝑥) =                            ,                                                    (6)
                                      2
                           2 𝑑(𝑑 + 1)(2𝑑 + 1)   (𝑥 − 1)𝑥(2𝑥 − 1)
                            [︂                                   ]︂
                 𝜔
                𝑆𝑐 (𝑥) = 𝜔                    −                     + 𝑥(𝑥 − 1)2 .                         (7)
                                    6                   6

Here 𝑥 is the baseline number of bottom vertices in a component and 𝛼 is the fraction of
components upgraded to 𝑥 − 1 bottom vertices.

Proof. By Lemma 1, an optimal configuration consists of truncated cascade components whose
numbers of bottom vertices differ by at most one. Let 𝑘 components have 𝑥 − 1 bottom vertices
and the remaining 𝑐 − 𝑘 components have 𝑥 bottom vertices; put 𝛼 = 𝑘/𝑐.
                                                                                        (︀𝑥)︀
   A component with 𝑥 bottom vertices has all matches decisive except for the            2        draws among
the bottom vertices. Since a decisive match awards 𝜔 points in total and a draw awards two



                                                     9
points, its total number of points 𝑃𝑐𝜔 (𝑥) is
    [︃(︃       )︃     (︃ )︃]︃        (︃ )︃
           𝑑+1   𝑥                     𝑥         𝜔𝑑(𝑑 + 1) 𝜔𝑥(𝑥 − 1)              𝜔𝑑(𝑑 + 1) − (𝜔 − 2)𝑥(𝑥 − 1)
𝜔              −                +2           =            −          + 𝑥(𝑥 − 1) =                             ,
            2    2                     2             2        2                                2

which gives (6).
      Its top vertices have scores 𝜔𝑥, 𝜔(𝑥 + 1), . . . , 𝜔𝑑, while every bottom vertex has score 𝑥 − 1.
Using
                                                   𝑛
                                                  ∑︁           𝑛(𝑛 + 1)(2𝑛 + 1)
                                                        𝑗2 =                    ,
                                                  𝑗=1
                                                                      6

we obtain
                                                                                    ⎛                        ⎞
                 𝑑
                ∑︁               𝑥
                                ∑︁                        𝑑
                                                         ∑︁                               𝑑
                                                                                         ∑︁          𝑥−1
                                                                                                     ∑︁
    𝑆𝑐𝜔 (𝑥) =        (𝜔𝑗)2 +          (𝑥 − 1)2 = 𝜔 2           𝑗 2 + 𝑥(𝑥 − 1)2 = 𝜔 2 ⎝        𝑗2 −         𝑗 2 ⎠ + 𝑥(𝑥 − 1)2
                𝑗=𝑥             𝑖=1                      𝑗=𝑥                            𝑗=1          𝑗=1
                         𝑑(𝑑 + 1)(2𝑑 + 1) (𝑥 − 1)𝑥(2𝑥 − 1)
                    [︂                                                 ]︂
             = 𝜔2                        −                 + 𝑥(𝑥 − 1)2 ,
                                6                 6

which gives (7). This is exactly the truncated cascade distribution of Avila-Cano et al. (2021).
      The total sum of squares and total points are

            𝑆(𝛼) = 𝑐 [𝛼𝑆𝑐𝜔 (𝑥 − 1) + (1 − 𝛼)𝑆𝑐𝜔 (𝑥)] ,              𝑃 (𝛼) = 𝑐 [𝛼𝑃𝑐𝜔 (𝑥 − 1) + (1 − 𝛼)𝑃𝑐𝜔 (𝑥)] .

Substitution into HHI 𝜔 = 𝑆/𝑃 2 proves the formula. Since the objective is a ratio of a linear
function and the square of a linear function in 𝛼, its continuous maximum may lie in the interior;
the discrete maximum is obtained by checking all displayed values of 𝑥 and 𝛼.

3.3        Lower bound and characterisation
The following result provides a strict lower bound on the maximum Herfindahl–Hirschman index
for incomplete round-robin tournaments by the HHI *𝜔 of independent round-robin tournaments,
computed in Theorem 2.

Theorem 3. Let 𝐺 be a simple 𝑑-regular graph on 𝑁 vertices representing an incomplete
round-robin tournament, where 𝑑 ≥ 1 and 𝑑 + 1 divides 𝑁 . Put
                                                                                         𝑐
                                        𝑁                                               ⋃︁
                                𝑐 :=       ,            𝐾 := 𝐾𝑑+1 ,         𝐺worst :=         𝐾𝑑+1 .
                                       𝑑+1                                              𝑖=1

Then, we have that
                                                                            𝑑+1
                                     HHI *𝜔 (𝐺) ≥ HHI *𝜔 (𝐺worst ) ≥            HHI *𝜔 (𝐾).                                (8)
                                                                             𝑁
                                                                          ∼ 𝐺worst . For larger 𝜔,
The first inequality is an equality for 𝜔 ∈ {2, 3, 4, 5} if and only if 𝐺 =
equality may also hold for other graphs.

Proof. Put 𝑐 = 𝑁/(𝑑 + 1). We first choose a reference configuration on 𝐺worst and construct
a configuration of 𝐺 whose score vector majorises the reference score vector. We then prove
strictness for 𝜔 ∈ {2, 3, 4, 5} when 𝐺 ∼
                                       ̸ 𝐺worst .
                                       =


                                                                  10
   Choose an optimal configuration of the entire graph 𝐺worst . By Lemma 1, the reference may
be chosen so that every component has 𝑟 fully upgraded winners, while 𝑡 components have one
additional fully upgraded winner, for some 0 ≤ 𝑟 ≤ 𝑑 and 0 ≤ 𝑡 < 𝑐. We take 𝑡 = 0 if 𝑟 = 𝑑,
since no further nontrivial upgrade is possible.
   Let 𝑥 := 𝑑 + 1 − 𝑟. The decreasing reference score vector p = (𝑝1 , . . . , 𝑝𝑁 ) consists of 𝑐 copies
of each of
                                 𝜔𝑑, 𝜔(𝑑 − 1), . . . , 𝜔(𝑑 − 𝑟 + 1),

followed, when 𝑡 > 0, by 𝑡 scores equal to 𝜔(𝑑 − 𝑟). All remaining scores are 𝑥 − 1 or 𝑥 − 2 (only
𝑥 − 1 when 𝑡 = 0). The total number of decisive matches in this configuration is
                                          (︃         (︃ )︃)︃
                                                       𝑟
                                  𝑊 = 𝑐 𝑟𝑑 −                   + 𝑡(𝑑 − 𝑟).                           (9)
                                                       2


Step 1: Equitable colouring. By the Hajnal–Szemerédi theorem (Hajnal and Szemerédi, 1970;
Kierstead and Kostochka, 2008), 𝐺 has a proper equitable (𝑑 + 1)-colouring, i.e. a colouring
with independent colour classes 𝐴0 , . . . , 𝐴𝑑 of size 𝑐. Order these classes greedily: choose 𝐴0
arbitrarily and, after choosing the first 𝑗 classes, select 𝐴𝑗 among the remaining classes such
that it minimises its number of neighbours in their union. Write

                               𝑈𝑗 := 𝐴0 ∪ · · · ∪ 𝐴𝑗−1            (𝑈0 = ∅).


Step 2: A bound on the internal edges. We claim that
                                           (︃ )︃
                                               𝑗
                               𝑒𝐺 (𝑈𝑗 ) ≤ 𝑐                (0 ≤ 𝑗 ≤ 𝑑 + 1).                        (10)
                                               2

It is convenient to measure the difference by
                                                   (︃ )︃
                                                    𝑗
                                       𝛿𝑗 := 𝑐        − 𝑒𝐺 (𝑈𝑗 ).
                                                    2

Thus 𝛿1 = 0. Suppose 𝛿𝑗 ≥ 0 and 1 ≤ 𝑗 ≤ 𝑑 − 1. Since 𝐺 is 𝑑-regular, the number of edges from
𝑈𝑗 to the remaining 𝑑 + 1 − 𝑗 colour classes is

                               𝑗𝑐𝑑 − 2𝑒𝐺 (𝑈𝑗 ) = 𝑗𝑐(𝑑 + 1 − 𝑗) + 2𝛿𝑗 .

The greedy choice of 𝐴𝑗 therefore gives

                                                                 2𝛿𝑗
                                   𝑒𝐺 (𝐴𝑗 , 𝑈𝑗 ) ≤ 𝑗𝑐 +              .
                                                               𝑑+1−𝑗

Consequently,
                                                      2
                                          (︂                     )︂
                                  𝛿𝑗+1 ≥ 1 −                          𝛿𝑗 ≥ 0.                      (11)
                                                    𝑑+1−𝑗
This proves (10) for 𝑗 ≤ 𝑑. The same bound at 𝑗 = 𝑑 + 1 is an equality, because 𝐺 has
𝑁 𝑑/2 = 𝑐 𝑑+1
             (︀   )︀
           2  edges.


                                                      11
   If 𝑡 > 0, one additional, partial class is needed. Choose 𝐵 ⊆ 𝐴𝑟 with |𝐵| = 𝑡, consisting
of the 𝑡 vertices with fewest neighbours in 𝑈𝑟 , and put 𝑈 := 𝑈𝑟 ∪ 𝐵. Since 𝐴𝑟 is independent,
averaging the degrees into 𝑈𝑟 gives
                                                                 (︃ )︃
                                  𝑡                  𝑟        𝑡        2𝛿𝑟
                                                                                          (︂                         )︂
              𝑒𝐺 (𝑈 ) ≤ 𝑒𝐺 (𝑈𝑟 ) + 𝑒𝐺 (𝐴𝑟 , 𝑈𝑟 ) ≤ 𝑐   − 𝛿𝑟 +   𝑟𝑐 +
                                  𝑐                  2        𝑐      𝑑+1−𝑟
                            (︃ )︃                                                        (︃ )︃
                          𝑟                 2𝑡             𝑟
                                          (︂                                  )︂
                       =𝑐   + 𝑟𝑡 − 1 −              𝛿𝑟 ≤ 𝑐   + 𝑟𝑡.
                          2            𝑐(𝑑 + 1 − 𝑟)        2

The last step follows from 𝑡 < 𝑐 and 𝑑 + 1 − 𝑟 ≥ 2 whenever 𝑡 > 0.

Step 3: Constructing a majorising score vector. For an edge between 𝐴𝑖 and 𝐴𝑗 , 𝑖 < 𝑗,
call 𝑖 its leading index. List the edges by nondecreasing leading index. If 𝑡 > 0, list edges led by
vertices of 𝐵 first among those whose leading index is 𝑟. Select the first 𝑊 edges, make their
lower-indexed endpoint the winner, and declare all other matches draws. Let q = (𝑞1 , . . . , 𝑞𝑁 )
be the resulting decreasing score vector.
   Fix 1 ≤ 𝑗 ≤ 𝑟. The number of edges incident with 𝑈𝑗 is
                                                                 (︃            (︃ )︃)︃
                                                                                   𝑗
                              𝐹𝑗 = 𝑗𝑐𝑑 − 𝑒𝐺 (𝑈𝑗 ) ≥ 𝑐 𝑗𝑑 −                               =: 𝑊𝑗 .
                                                                                   2

All these edges precede edges with leading index at least 𝑗. Since 𝑊 ≥ 𝑊𝑗 , at least 𝑊𝑗 selected
edges have their winner in 𝑈𝑗 . At most 𝑒𝐺 (𝑈𝑗 ) ≤ 𝑐 2𝑗 selected edges have both endpoints in 𝑈𝑗 .
                                                                      (︀ )︀

   Initially, if all matches were draws, the teams in 𝑈𝑗 would have 𝑗𝑐𝑑 points. Changing a
crossing draw into a win by a team in 𝑈𝑗 adds 𝜔 − 1 points to 𝑈𝑗 , whereas changing an internal
draw adds 𝜔 − 2 points. Hence
                                                                                                    (︃ )︃
           ∑︁                                                                                            𝑗
                  𝑞𝑣 ≥ 𝑗𝑐𝑑 + (𝜔 − 1)𝑊𝑗 − 𝑒𝐺 (𝑈𝑗 ) ≥ 𝑗𝑐𝑑 + (𝜔 − 1)𝑊𝑗 − 𝑐                                          = 𝜔𝑊𝑗 .
           𝑣∈𝑈𝑗
                                                                                                         2

The first 𝑗𝑐 entries of p are exactly the first 𝑗 upper tiers of the 𝑐 reference cliques, whose sum
is 𝜔𝑊𝑗 . The largest 𝑗𝑐 entries of q have a sum at least that of 𝑈𝑗 . Thus

                                    𝑗𝑐
                                    ∑︁           𝑗𝑐
                                                 ∑︁
                                          𝑞𝑖 ≥         𝑝𝑖             (1 ≤ 𝑗 ≤ 𝑟).                                         (12)
                                    𝑖=1          𝑖=1

   If 𝑡 > 0, the partial-class bound gives
                                                                                   (︃       (︃ )︃)︃
                                                                                               𝑟
        |{𝑒 ∈ 𝐸(𝐺) : 𝑒 ∩ 𝑈 ̸= ∅}| = 𝑑(𝑟𝑐 + 𝑡) − 𝑒𝐺 (𝑈 ) ≥ 𝑐 𝑟𝑑 −                                         + 𝑡(𝑑 − 𝑟) = 𝑊.
                                                                                               2

All edges incident with 𝑈 precede the other edges in our ordering, so all 𝑊 selected matches
have their winners in 𝑈 . At most 𝑒𝐺 (𝑈 ) selected matches are internal to 𝑈 ; consequently,

                     ∑︁                                                                            𝑟𝑐+𝑡
                                                                                                   ∑︁
                           𝑞𝑣 ≥ 𝑑(𝑟𝑐 + 𝑡) + (𝜔 − 1)𝑊 − 𝑒𝐺 (𝑈 ) ≥ 𝜔𝑊 =                                     𝑝𝑖 .
                     𝑣∈𝑈                                                                           𝑖=1




                                                            12
This gives the additional prefix inequality at 𝑟𝑐 + 𝑡.
   We now verify the remaining prefixes. For a decreasing vector, its interpolated prefix sums
form a concave function. The prefix sums of p are linear between consecutive indices among
0, 𝑐, 2𝑐, . . . , 𝑟𝑐, and between 𝑟𝑐 and 𝑟𝑐 + 𝑡 when 𝑡 > 0. Concavity and the established endpoint
inequalities therefore give
                                  𝑠
                                 ∑︁            𝑠
                                              ∑︁
                                       𝑞𝑖 ≥         𝑝𝑖       (0 ≤ 𝑠 ≤ 𝑟𝑐 + 𝑡).
                                 𝑖=1          𝑖=1

Both configurations have the same number 𝑊 of decisive matches and therefore the same total
number of points:
                                  𝑁
                                  ∑︁           𝑁
                                               ∑︁
                                        𝑞𝑖 =         𝑝𝑖 = 𝑁 𝑑 + (𝜔 − 2)𝑊.                         (13)
                                  𝑖=1          𝑖=1

If 𝑡 = 0, the remaining reference scores are all 𝑥 − 1, so the same concavity argument proves the
inequalities for all later prefixes. If 𝑡 > 0, the remaining reference scores are in {𝑥 − 1, 𝑥 − 2}.
Suppose that 𝑠 > 𝑟𝑐 + 𝑡 is the first position at which the prefix inequality fails. It must then
be that 𝑞𝑠 < 𝑝𝑠 . Since scores are integers, 𝑞𝑠 ≤ 𝑝𝑠 − 1; and, since q is decreasing and all later
reference scores are at least 𝑝𝑠 − 1, we have 𝑞𝑖 ≤ 𝑝𝑖 for every 𝑖 ≥ 𝑠. The strict prefix deficit could
never be recovered at 𝑁 , contradicting (13).
   Thus q majorises p. By the convexity of 𝑧 ↦→ 𝑧 2 and equality of their total points,

                           HHI *𝜔 (𝐺) ≥ HHI 𝜔 (𝐺, q) ≥ HHI 𝜔 (𝐺worst , p).

Since p is an optimal score vector of 𝐺worst , this proves the first inequality in (8) for every 𝜔 ≥ 2.
For the second inequality, take any optimal configuration of 𝐾 and repeat it on all 𝑐 components.
If its total points and sum of squared scores are 𝑃𝐾 and 𝑆𝐾 , the resulting configuration on
𝐺worst has
                                    𝑐𝑆𝐾     1             𝑑+1
                        HHI 𝜔 =          2
                                           = HHI *𝜔 (𝐾) =     HHI *𝜔 (𝐾).
                                  (𝑐𝑃𝐾 )    𝑐              𝑁
The optimum on 𝐺worst is at least this value, giving the second inequality in (8).

Step 4: Uniqueness for 𝜔 ∈ {2, 3, 4, 5}. We may assume 𝑑, 𝑐 ≥ 2; otherwise, any possible 𝑑-
regular graph is of the form 𝑐𝐾𝑑+1 . Write 𝐻 = 𝑐𝐾𝑑+1 and choose the optimal truncated-cascade
configuration on 𝐻 used above, with parameters 𝑟, 𝑡 and 𝑊 decisive matches.
   First, this configuration has at least two fully upgraded vertices. Indeed, the all-draw
configuration (that has the unique worst possible HHI of 𝑁1 ) cannot be optimal. If it had exactly
one fully upgraded vertex, then 𝑟 = 0, 𝑡 = 1. Let 𝐹 (𝑠) denote the HHI of the configuration with
one fully upgraded vertex in each of 𝑠 cliques and only draws elsewhere. Then by (1)-(2)

                               𝑁 𝑑 + 𝑠𝐴
                    𝐹 (𝑠) =              ,               𝐴 = (𝜔 2 − 3)𝑑 + 1,     𝑏 = 𝜔 − 2.
                              𝑑(𝑁 + 𝑏𝑠)2

A direct calculation gives

                                                                𝐴   𝑏(2 + 3𝑏/𝑁 )
                              𝐹 (2) > 𝐹 (1)          ⇐⇒           >              .
                                                                𝑑   1 − 2𝑏2 /𝑁 2


                                                           13
Since 𝑁 = 𝑐(𝑑 + 1) ≥ 6 and 𝑏 ∈ {0, 1, 2, 3}, the right-hand side is at most 0, 45/17, 54/7, 21,
respectively, whereas 𝐴/𝑑 is greater than 1, 6, 13, 22, respectively (using the bound 𝐴/𝑑 ≥
𝑏2 + 4𝑏 + 1). Hence 𝐹 (2) > 𝐹 (1), ruling out 𝑟 = 0, 𝑡 = 1. In particular, if 𝑟 = 0, then 𝑡 ≥ 2.
   We use the following elementary colouring observation. If 𝐺 is not a union of 𝐾𝑑+1 ’s, it has
a proper equitable (𝑑 + 1)-colouring with classes 𝐴0 , 𝐴1 , . . . , 𝐴𝑑 such that

                      𝑒𝐺 (𝐴0 , 𝐴1 ) ≤ 𝑐,     𝑁𝐺 (𝑣) ∩ 𝐴0 = ∅ for some 𝑣 ∈ 𝐴1 .                               (†)

To see this, start from any equitable colouring. The average number of edges between two
classes is 𝑐. Any pair with fewer than 𝑐 edges, or with exactly 𝑐 edges but not forming a perfect
matching, gives the claim (interchanging its classes if necessary). Otherwise, all pairs are joined
by perfect matchings. Since 𝐺 is not a clique union, there is an induced path 𝑢 − 𝑣 − 𝑤; its three
vertices have distinct colours. Swapping the colours of 𝑣, 𝑤 preserves properness and equitability,
but 𝑢 now has no neighbour of 𝑣’s original colour. By the same averaging argument, the resulting
colouring has a pair satisfying (†).
   Fix this colouring, order the remaining classes greedily as in Steps 1–3, and distinguish two
cases.
   If 𝑊 > 𝑐𝑑: We then have 𝑟 ≥ 2 or 𝑟 = 1 and 𝑡 ≥ 1; and by (9), 𝑊 − 𝑐𝑑 ≥ 𝑑 − 1, so the
reference has 𝑝𝑐+1 = 𝜔(𝑑 − 1). In the edge ordering of Step 3, put the 𝑑 edges incident with 𝑣
first among the edges led by 𝐴1 ; if a partial class 𝐵 ⊆ 𝐴1 is used, choose it to contain 𝑣, which
is possible because 𝑣 has no neighbour in 𝐴0 . All 𝑐𝑑 edges incident with 𝐴0 are selected first. At
least 𝑑 − 1 of 𝑣’s edges are therefore selected, making its score at least 𝜔(𝑑 − 1) + 1. Meanwhile,
all 𝑐 vertices of 𝐴0 score 𝜔𝑑. Thus the sorted constructed score vector q satisfies 𝑞𝑐+1 > 𝑝𝑐+1 ;
by Steps 1–3 it majorizes p, and strict convexity of the square yields a strict HHI inequality.
   If 𝑊 ≤ 𝑐𝑑: The reference either has (𝑟, 𝑡) = (1, 0) or 𝑟 = 0, 𝑡 ≥ 2. Put ℎ = 𝑐 in the first
case and ℎ = 𝑡 in the second, so that 𝑊 = ℎ𝑑. Because 𝐴0 is independent, it sends exactly 𝑐𝑑
edges to the 𝑐𝑑 vertices outside it. By (†), at least one outside vertex has no neighbour in 𝐴0 ;
hence another has at least two neighbours there. Choose 𝑇 ⊆ 𝐴0 of size ℎ ≥ 2 containing two
such neighbours. Make every vertex of 𝑇 win all its matches and declare all remaining matches
draws. For 𝑣 ∈
             / 𝑇 put 𝑎𝑣 = |𝑁𝐺 (𝑣) ∩ 𝑇 |, then
                                                     ∑︀
                                                          / 𝑎𝑣 = ℎ𝑑.
                                                        𝑣 ∈𝑇                The total number of wins and
points equal those in the reference (𝑊 = ℎ𝑑). Furthermore, in the reference, each non-winner
has 0 or 1 losses. Therefore, for the difference in the sums of squared scores, we have
                           ∑︁                                                            ∑︁ (︀
𝑆(𝐺)−𝑆(𝐻) = ℎ(𝜔𝑑)2 +             (𝑑−𝑎𝑣 )2 −(ℎ(𝜔𝑑)2 +ℎ𝑑(𝑑−1)2 +(𝑁 −ℎ𝑑−ℎ)𝑑2 ) =                    𝑎2𝑣 −𝑎𝑣 > 0,
                                                                                                       )︀

                          𝑣 ∈𝑇
                            /                                                           𝑣 ∈𝑇
                                                                                          /

since some 𝑎𝑣 ≥ 2. This again gives a strict HHI inequality.
    Thus HHI* (𝐺) > HHI* (𝑐𝐾𝑑+1 ) for every 𝐺 ∼
              𝜔             𝜔                  ̸ 𝑐𝐾𝑑+1 and 𝜔 ∈ {2, 3, 4, 5}.
                                               =

Example 1 (The clique union need not be the unique minimiser). Let 𝑑 = 2, 𝑁 = 6, and 𝜔 = 6.
The graphs 𝐺worst = 2𝐾3 and 𝐺 = 𝐶6 are nonisomorphic, but

                                                                     79
                                   HHI *6 (2𝐾3 ) = HHI *6 (𝐶6 ) =       .                                   (14)
                                                                    200

Indeed, on either graph, let one vertex win both its matches and make every other match a

                                                   14
draw. The resulting score vector is (12, 2, 2, 2, 1, 1), giving HHI 6 = 158/400 = 79/200.
    To see that no configuration on either graph has a higher HHI, let 𝑊 ∈ {0, . . . , 6} be the
number of decisive matches. By the general identities for total points and squared scores in (1)
and (2), we have
                                 𝑃 = 12 + 4𝑊,           𝑆 = 24 + 68𝑊 − Γ6 ,

where
                                       ∑︁ (︀                            )︀
                                Γ6 =           36𝑤𝑣 ℓ𝑣 + 25𝑤𝑣 𝑑𝑣 + 𝑑𝑣 ℓ𝑣 ≥ 0.
                                       𝑣∈𝑉

If 𝑊 = 2, either a single vertex wins both matches, yielding Γ6 = 2, or two vertices win one
match each, giving Γ6 ≥ 50. Hence 𝑆 ≤ 158. If 𝑊 = 3, at least one vertex has exactly one win,
so Γ6 ≥ 25 and 𝑆 ≤ 203. For the remaining values 𝑊 ∈ {0, 1, 4, 5, 6}, the bound Γ6 ≥ 0 suffices.
Consequently,
                      {︃                                         }︃
                           158 203               24 + 68𝑊                          79 203 37             79
                                                                              {︂                }︂
        HHI 6 ≤ max            ,   , max                              = max           ,   ,          =       .
                           20 24 𝑊 ∈{0,1,4,5,6} (12 + 4𝑊 )2
                             2   2                                                 200 576 98            200

Thus equality in the minimum-HHI comparison does not characterise 𝐺worst when 𝜔 ≥ 6.

    The lower bounds break down if 𝑑 + 1 does not divide 𝑁 , that is, when the teams cannot be
partitioned into full round-robin tournament groups, as shown in the next proposition.

Proposition 1 (The divisibility assumption is necessary). The conclusion of Theorem 3 does
not hold for arbitrary 𝑁 . In particular, let 𝜔 = 5, let 𝐺 = 𝐾3,3 , and let 𝐾 = 𝐾4 . Then

                                                    77  4               158
                                HHI *5 (𝐾3,3 ) =       < HHI *5 (𝐾4 ) =     .                                    (15)
                                                   216  6               441

    The proof of Proposition 1 just calculates the HHI* values of each graph, and is deferred to
Appendix C.

    At first sight, it may be unclear why Theorem 3 is relevant in practice, since we do not
know about any tournament where the teams playing in independent round-robin groups are
ranked globally in a single table. However, the third-placed teams of all groups are ranked in the
recent FIFA World Cup and UEFA European Championships. Furthermore, the competitive
balance of a group stage consisting of round-robin groups is usually computed as the average
Herfindahl–Hirschman index of the groups in a season (see, for example, Triguero-Ruiz and
Avila-Cano (2023)), which is related to considering the group stage as an incomplete round-robin
tournament.


4    Complexity results
We now turn to the computational complexity of maximising the Herfindahl–Hirschman index
in an incomplete round-robin tournament. Section 4.1 proves the 𝒩 𝒫-hardness for every fixed
integer 𝜔 ≥ 3, even under strongly balanced schedules. Section 4.2 addresses the case of fixed
total points, where the reduction is an easier odd-cycle-transversal encoding.


                                                       15
4.1     Arbitrary win values under balanced schedules
Throughout this section, a win is worth a fixed integer 𝜔 ≥ 3, a draw is worth one point, and a
loss is worth zero points. We prove hardness under two strong restrictions on the schedule.
Map of the proof: The reduction has four layers. First, we rewrite the nonlinear objective
as a linear potential once the total numbers of decisive matches and mixed local outcomes are
recorded. Second, variable cycles and clause triangles encode a truth assignment: alternating
pure winners select one sign of each variable, while a clause winner must correspond to a true
literal. Third, fixed class-compatible padding gadgets make maximising the HHI equivalent to
maximising this potential on the core. Finally, a complete 𝑘-fold blow-up turns parameter one
into parameter 𝑘; and a quantitative gap ensures that asymmetric configurations of the blow-up
cannot erase the separation. Figures 2–4 illustrate the main building blocks.

4.1.1    A potential for cubic (3-regular) graphs

Let Φ be a configuration on a cubic graph. For a vertex 𝑣, let 𝑤𝑣 , 𝑑𝑣 , ℓ𝑣 be its numbers of wins,
draws, and losses, and let 𝑊 be the number of decisive matches. Define
                                        ∑︁ (︁                                         )︁
                           Γ𝜔 (Φ) :=            𝜔 2 𝑤𝑣 ℓ𝑣 + (𝜔 − 1)2 𝑤𝑣 𝑑𝑣 + 𝑑𝑣 ℓ𝑣 ,                (16)
                                         𝑣

                           Ψ𝜔𝑞 (Φ) := 𝑞𝑊 − Γ𝜔 (Φ).                                                  (17)

If the graph has 𝑁 vertices, then

                                 𝑃 (Φ) = 3𝑁 + (𝜔 − 2)𝑊,                                             (18)
                                  𝑆(Φ) = 9𝑁 + 3(𝜔 2 − 2)𝑊 − Γ𝜔 (Φ).                                 (19)

Indeed, 𝑤𝑣 + 𝑑𝑣 + ℓ𝑣 = 3 gives

                     𝑤𝑣2 = 3𝑤𝑣 − 𝑤𝑣 𝑑𝑣 − 𝑤𝑣 ℓ𝑣 ,               𝑑2𝑣 = 3𝑑𝑣 − 𝑤𝑣 𝑑𝑣 − 𝑑𝑣 ℓ𝑣 ,

and summing (𝜔𝑤𝑣 + 𝑑𝑣 )2 yields (19). Consequently, for every real number 𝜆,

            𝑆(Φ) − 𝜆𝑃 (Φ) = 3𝑁 (3 − 𝜆) + Ψ𝜔𝑞𝜆 (Φ),                   𝑞𝜆 := 3(𝜔 2 − 2) − 𝜆(𝜔 − 2).   (20)

   The following elementary normal form is the only local argument needed in the section.

Lemma 2. Let 2 ≤ 𝑞 < 2(𝜔 − 1). On every cubic graph, a configuration maximising Ψ𝜔𝑞 can be
chosen so that every vertex is one of the following:

                           (3, 0, 0),        (0, 0, 3),        (0, 2, 1),      (0, 1, 2).

Furthermore, if 𝜔 ≥ 4, then a configuration maximising Ψ𝜔1 can be chosen such that every vertex
is one of the following:

                  (3, 0, 0),       (0, 0, 3),        (0, 2, 1),        (0, 1, 2),      (0, 3, 0).


                                                          16
Thus, every vertex having a win is a pure winner. If 𝐼 is the set of pure winners and 𝑅 is the
number of mixed vertices, then
                                         Ψ𝜔𝑞 = 3𝑞|𝐼| − 2𝑅,                                       (21)

and 𝐼 is an independent set.

Proof. The contribution of a vertex 𝑣 to Ψ𝜔𝑞 is
                                         (︁                               )︁
                        𝜓𝑞𝜔 (𝑣) = 𝑞𝑤𝑣 − 𝜔 2 𝑤𝑣 ℓ𝑣 + (𝜔 − 1)2 𝑤𝑣 𝑑𝑣 + 𝑑𝑣 ℓ𝑣 .

   First, let 2 ≤ 𝑞 < 2(𝜔 − 1).

Step 1: eliminating vertices with exactly one win. Suppose that 𝑣 has exactly one win,
against 𝑢, and replace this decisive match with a draw. Write the state of 𝑣 as (1, 𝑑𝑣 , ℓ𝑣 ), where
𝑑𝑣 + ℓ𝑣 = 2. At 𝑣, the change in the potential is

                       Δ𝑣 = (𝜔 − 1)2 𝑑𝑣 + (𝜔 2 − 1)ℓ𝑣 − 𝑞 ≥ 2(𝜔 − 1)2 − 𝑞.

At 𝑢, one loss is replaced by one draw. The change is

                 Δ𝑢 = (2𝜔 − 1)𝑤𝑢 + 𝑑𝑢 − ℓ𝑢 + 1 = (2𝜔 − 2)𝑤𝑢 + 4 − 2ℓ𝑢 ≥ −2,

where the last inequality follows from 𝑤𝑢 + 𝑑𝑢 + ℓ𝑢 = 3. Hence,

                                     Δ𝑣 + Δ𝑢 ≥ 2𝜔 2 − 4𝜔 − 𝑞.                                    (22)

If 2 ≤ 𝑞 < 2(𝜔 − 1), then it is strictly larger than 2𝜔 2 − 6𝜔 + 2, which is positive for every 𝜔 ≥ 3.
Thus, a maximiser has no vertex with exactly one win.

Step 2: eliminating a vertex with two wins and one draw. Suppose that 𝑣 has state
(2, 1, 0) and draws against 𝑢. Let 𝑣 win this match. At 𝑣, the change is Δ𝑣 = 𝑞 + 2(𝜔 − 1)2 .
   At 𝑢, one draw is replaced with one loss. Since Step 1 has eliminated vertices with exactly
one win, the smallest possible change at 𝑢 is attained when 𝑢 has state (2, 1, 0), and equals
Δ𝑢 = −4𝜔 + 2. Therefore,
                                   Δ𝑣 + Δ𝑢 ≥ 2𝜔 2 − 8𝜔 + 𝑞 + 4.                                  (23)

This quantity is positive whenever 𝑞 > 2, 𝜔 ≥ 3. For 𝑞 = 2, it is nonnegative for every 𝜔 ≥ 3,
with equality only when 𝜔 = 3.

Step 3: eliminating a vertex with two wins and one loss. Suppose that 𝑣 has state
(2, 0, 1). Replace both wins by draws. At 𝑣, the change is 2(𝜔 2 − 𝑞 − 1). At either defeated
neighbour, replacing one loss by one draw decreases the potential by at most 2, as calculated in
Step 1. Hence, the total change is at least

                                              2(𝜔 2 − 𝑞 − 3).                                    (24)

If 2 ≤ 𝑞 < 2(𝜔 − 1), then 𝜔 2 − 𝑞 − 3 > 𝜔 2 − 2𝜔 − 1 > 0 for every 𝜔 ≥ 3.
   Steps 1–3 show that, when 𝑞 > 2, every vertex having a win is a pure winner. The same

                                                    17
conclusion holds for 𝑞 = 2: among all maximisers, choose one having the largest possible number
of pure winners, and apply the non-decreasing operation of Step 2 whenever necessary.
Step 4: eliminating a vertex playing three draws. Suppose that 𝑣 draws all three matches.
Since every winner is pure, none of its neighbours has a win. Let 𝑣 win all three matches. Its
contribution increases by 3𝑞. At each neighbour, replacing one draw by one loss changes the
contribution by at least −2. Thus, the total change is at least

                                          3𝑞 − 6 = 3(𝑞 − 2).                                   (25)

This is positive for 𝑞 > 2. For 𝑞 = 2, it is zero; our tie-breaking rule again allows us to perform
the operation because it increases the number of pure winners.
   Now, assume 𝜔 ≥ 4 and consider the potential Ψ𝜔1 . Then, all three modifications in steps 1-3
are strictly improving, since

                   2𝜔 2 − 4𝜔 − 1 > 0,       2𝜔 2 − 8𝜔 + 5 > 0,     2(𝜔 2 − 4) > 0.

Consequently, in a configuration maximising Ψ𝜔𝑞 or Ψ𝜔1 for 𝜔 ≥ 4, every winner is pure. Thus,
we also get (21) from (17).

Corollary 2. If 𝐼 denotes the set of pure winners, then every edge not incident with 𝐼 is a draw,
and the contribution of a vertex 𝑣 is
                                ⎧
                                ⎪
                                ⎪
                                ⎪
                                ⎪ 3𝑞,   𝑣 ∈ 𝐼,
                                ⎨
                                 −2,    𝑣∈
                                         / 𝐼 and |𝑁 (𝑣) ∩ 𝐼| ∈ {1, 2},                         (26)
                                ⎪
                                ⎪
                                ⎪
                                ⎩0,     𝑣∈
                                         / 𝐼 and |𝑁 (𝑣) ∩ 𝐼| ∈ {0, 3}.
                                ⎪


4.1.2      Two balanced satisfiability cores

We reduce from Monotone 3-Sat in which every clause contains three distinct literals and
every variable occurs exactly three times positively and exactly three times negatively. This
problem is 𝒩 𝒫-complete (Darmann and Döcker, 2021). Let the formula 𝜙 have 𝑚 clauses and 𝑧
variables. Counting literal occurrences gives

                                                             𝑚
                                        6𝑧 = 3𝑚,        𝑧=     .                               (27)
                                                             2

Consider the bipartite incidence graph between the clauses and the two signed literals 𝑥+ , 𝑥−
of every variable. It is cubic on both sides. By Kőnig’s line-colouring theorem, its edges can
be coloured with {1, 2, 3} so that every clause and every signed literal is incident with all three
colours.

The fully balanced core. For every clause, create a triangle, putting the vertex of an
occurrence of colour 𝑗 into class 𝑉𝑗 . For every variable 𝑥, denote its positive and negative
                                   −
occurrences of colour 𝑗 by 𝑥+
                            𝑗 and 𝑥𝑗 and create the six-cycle

                                            − + − + − +
                                        𝑥+
                                         1 𝑥2 𝑥3 𝑥1 𝑥2 𝑥3 𝑥1 .                                 (28)

                                                   18
                                   𝑥+
                                    1
                                                                                       𝑐1
                       𝑥−
                        3                         𝑥−
                                                   2




                                                                            𝑐2                 𝑐3
                       𝑥+
                        2                         𝑥+
                                                   3


                                   𝑥−
                                    1


                            Variable six-cycle                                   Clause triangle

                        Figure 2: Building blocks of the fully balanced core 𝐹𝜙
Note: The three shades indicate the classes 𝑉1 , 𝑉2 , 𝑉3 ; every short external edge is continued to the corresponding
occurrence vertex in the other type of block.


            −
Put 𝑥+
     𝑗 and 𝑥𝑗 into 𝑉𝑗 and join every occurrence vertex to its clause vertex. Call the resulting
graph 𝐹𝜙 .
    Every vertex has one neighbour in each of the three classes. Every clause contributes one
vertex to each class, and every variable contributes two, so (27) gives |𝑉𝑗 | = 𝑚 + 2𝑧 = 2𝑚. Thus,
𝐹𝜙 is cubic and fully balanced with parameter one.

Lemma 3. For 2 ≤ 𝑞 < 2(𝜔 − 1),

                                                                   15𝑞
                                                              (︂            )︂
                                         max      Ψ𝜔𝑞 (Φ) ≤            − 5 𝑚.                                    (29)
                                        Φ on 𝐹𝜙                     2

Equality holds if and only if 𝜙 is satisfiable. If 𝜙 is unsatisfiable, the right-hand side can be
decreased by 3𝑞.
    For 𝜔 ≥ 4, we also have
                                                                     5𝑚
                                                 max Ψ𝜔1 (Φ) ≤          ,                                        (30)
                                              Φ on 𝐹𝜙                 2
with equality if and only if 𝜙 is satisfiable; otherwise, the maximum is at most 5𝑚/2 − 1.

Proof. For the first assertion, apply Lemma 2. Every clause triangle contains at most one pure
winner and every variable six-cycle at most three, so

                                                                     5𝑚
                                              |𝐼| ≤ 𝑚 + 3𝑧 =            .
                                                                      2

Every clause triangle contains at least two mixed vertices. If it contains a pure winner, the
other two clause vertices lose against it and draw with each other. If it contains no pure winner,
all three internal matches are draws; Step 4 implies that every clause vertex must then lose its
occurrence match.
    Among the 3𝑚 variable vertices, at most 3𝑧 = 3𝑚/2 are pure winners, and at most 𝑚 are
pure losers: every pure-loser occurrence vertex is adjacent to the unique pure winner of its clause




                                                         19
triangle. Hence at least 𝑚/2 variable vertices are mixed and

                                                     𝑚   5𝑚
                                        𝑅 ≥ 2𝑚 +       =    .
                                                     2    2

Equation (21) proves (29).
   Equality forces an alternating set of three pure winners in every variable cycle and one pure
winner in every clause triangle. Interpret the selected occurrence vertices as false literals. The
selected clause vertex is not adjacent to a selected occurrence vertex and therefore represents
a true literal. This gives a satisfying assignment. Conversely, a satisfying assignment selects
the three false-literal vertices of each variable cycle and one true-literal vertex of every clause
triangle, attaining equality. An unsatisfiable formula therefore loses at least one pure winner,
and hence at least 3𝑞 on Ψ𝜔𝑞 .
   Now let 𝑞 = 1 and 𝜔 ≥ 4. By Lemma 2, every winner is pure.
   We first record a bound that will also be used for the externally balanced core. Consider a
variable cycle of length 2𝑟, and let 𝑥 be the number of pure winners on the cycle. For 𝑗 ∈ {0, 1, 2},
let 𝑛𝑗 be the number of non-winners having exactly 𝑗 winning cycle neighbours. Since the
winners form an independent set,

                                     𝑥 ≤ 𝑟,        𝑛1 + 2𝑛2 = 2𝑥.

Before taking the losses towards clause neighbours into account (assuming they are draws), by
(26) the contribution of the cycle is

                                 3𝑥 − 2(𝑛1 + 𝑛2 ) = 2𝑛2 − 𝑥 ≤ 𝑥 ≤ 𝑟.

By (26), each adjacent pure winner clause vertex can increase this contribution by at most two,
and therefore, if there are 𝑦 such clause vertices, the cycle contributes at most 𝑟 + 2𝑦. Equality
forces 𝑥 = 𝑛2 = 𝑟, so the winners form one of the two alternating independent sets.
   Applying this estimate with 𝑟 = 3, the variable cycles contribute at most 3𝑧 + 2𝑌 , where 𝑌
is the total number of pure winner clause vertices. A clause triangle contributes at most zero if
it has no winner and at most 3 − 2 − 2 = −1 if it has a pure winner. Hence,

                                                        3𝑚      5𝑚
                              Ψ𝜔1 ≤ 3𝑧 + 2𝑌 − 𝑌 =          +𝑌 ≤    .
                                                         2       2

Equality requires an alternating set of three pure winners in every variable cycle and one pure
winner in every clause triangle. As before, interpreting the selected occurrence vertices as false
literals and the selected clause vertex as a true literal gives a satisfying assignment, and every
satisfying assignment attains equality. Since Ψ𝜔1 is integer-valued, an unsatisfiable instance loses
at least one.

The externally balanced core.           Let

                      𝜎1 = (12)(34),          𝜎2 = (13)(24),    𝜎3 = (14)(23).



                                                   20
For every clause 𝐶 and every 𝑡 ∈ [4], create a triangle 𝐶 𝑡 . If an occurrence has colour 𝑗, put its
vertex in 𝐶 𝑡 into class 𝑉𝜎𝑗 (𝑡) and join it to a variable vertex in class 𝑉𝑡 .
    This already guarantees external balancedness at every clause vertex.
    It remains to arrange the variable vertices. A variable vertex is described by an ordered pair
                                                                                     ̸ 𝑏, there are
(𝑎, 𝑏), where 𝑎 is its own class and 𝑏 is the class of its clause neighbour. Since 𝑎 =
twelve possible ordered pairs. For every variable, we create one positive and one negative vertex
for each such pair, giving 24 vertices in total.
    The availability of these vertices agrees exactly with the clause construction. For fixed 𝑡, the
three occurrence colours require the pairs

                                    (𝑡, 𝜎1 (𝑡)),        (𝑡, 𝜎2 (𝑡)),       (𝑡, 𝜎3 (𝑡)),

                                                          ̸ 𝑡. Thus, as 𝑡 ranges over [4], every
which are precisely the three ordered pairs (𝑡, 𝑏) with 𝑏 =
ordered pair (𝑎, 𝑏) with 𝑎 ̸= 𝑏 is required exactly once for the positive occurrences and exactly
once for the negative occurrences.
    Arrange the 24 variable vertices on a cycle, placing positive vertices at odd positions and
negative vertices at even positions. Let their own classes be

               (𝑎1 , . . . , 𝑎24 ) = (1, 4, 3, 1, 2, 4, 3, 2, 4, 1, 2, 3, 1, 4, 2, 3, 4, 1, 3, 2, 1, 3, 4, 2).   (31)

For every 𝑖 ∈ Z24 , define 𝑏𝑖 as the unique class not contained in 𝑎𝑖−1 , 𝑎𝑖 , 𝑎𝑖+1 . The sequence in
(31) has the following two properties:

      1. 𝑎𝑖−1 , 𝑎𝑖 , 𝑎𝑖+1 , 𝑏𝑖 = [4]       (𝑖 ∈ Z24 );

      2. among the odd positions, and separately among the even positions, the pairs (𝑎𝑖 , 𝑏𝑖 )
         are exactly the twelve ordered pairs (𝑎, 𝑏) with 𝑎 ̸= 𝑏 (counted in a cyclic way).

We assign to position 𝑖 the positive or negative variable vertex corresponding to the pair (𝑎𝑖 , 𝑏𝑖 )
and connect it to its clause neighbour in class 𝑉𝑏𝑖 .
    We can now verify external balancedness at a variable vertex in position 𝑖. The vertex itself
lies in 𝑉𝑎𝑖 , its clause neighbour lies in 𝑉𝑏𝑖 , and its two cycle neighbours lie in 𝑉𝑎𝑖−1 and 𝑉𝑎𝑖+1 .
Since 𝑎𝑖−1 , 𝑎𝑖 , 𝑎𝑖+1 , 𝑏𝑖 = [4], these three neighbours lie, one each, in the three classes different
from 𝑉𝑎𝑖 .
    Consequently, every vertex of the resulting graph 𝐸𝜙 has exactly one neighbour in each
class different from its own and no neighbour in its own class. In particular, all four classes are
independent and 𝐸𝜙 is cubic.
    Finally, every clause contributes three vertices to each class: class 𝑉𝑠 occurs once in each
triangle 𝐶 𝑡 with 𝑡 =
                    ̸ 𝑠. Moreover, the sequence (31) contains every class six times, so every
variable contributes six vertices to each class. Thus, all four classes have the same size.

Lemma 4. For 2 ≤ 𝑞 < 2(𝜔 − 1),

                                           max Ψ𝜔𝑞 (Φ) ≤ (30𝑞 − 20)𝑚.                                            (32)
                                         Φ on 𝐸𝜙




                                                            21
                                                                             𝐶1




                                                                             𝐶2
                                24-cycle for 𝑥
                              odd: 𝑥+ , even: 𝑥−

                                                                             𝐶3




                                                                             𝐶4


                   Figure 3: Schematic view of the externally balanced core 𝐸𝜙


Equality holds if and only if 𝜙 is satisfiable. In an unsatisfiable instance, the right-hand side can
be decreased by 3𝑞.
    For 𝜔 ≥ 4, we also have
                                          max Ψ𝜔1 (Φ) ≤ 10𝑚,                                    (33)
                                        Φ on 𝐸𝜙

with equality if and only if 𝜙 is satisfiable; otherwise, the maximum is at most 10𝑚 − 1.

Proof. By Lemma 2, Ψ𝜔𝑞 = 3𝑞|𝐼| − 2𝑅. The 4𝑚 clause triangles contain at most 4𝑚 pure winners,
and the 𝑧 = 𝑚/2 variable cycles contain at most 12𝑧 = 6𝑚. Thus |𝐼| ≤ 10𝑚.
    Every clause triangle contains at least two mixed vertices, giving 8𝑚. Among the 12𝑚
variable vertices, at most 6𝑚 are pure winners and at most 4𝑚 are pure losers, because every
pure-loser vertex is adjacent to the unique pure winner of one clause triangle. Therefore, at least
2𝑚 variable vertices are mixed and 𝑅 ≥ 10𝑚. This proves the bound (32).
    Equality forces an alternating independent set in every variable cycle and one pure winner in
every clause copy. Odd and even positions represent the positive and negative occurrences, so
the alternating set determines a truth value. The selected clause vertex represents a true literal.
Conversely, a satisfying assignment attains equality by selecting all false-literal vertices and one
true-literal vertex in each clause copy. Unsatisfiability loses at least one pure winner and hence
at least 3𝑞 in Ψ𝜔𝑞 .
    Now let 𝑞 = 1 and 𝜔 ≥ 4. By Lemma 2, every winner is pure. Apply the cycle estimate from
the proof of Lemma 3 with 𝑟 = 12. If 𝑌 is the total number of pure winner clause vertices, the
variable cycles contribute at most

                                        12𝑧 + 2𝑌 = 6𝑚 + 2𝑌.

As in Lemma 3, the clause triangles contribute at most −𝑌 . Since 𝑌 ≤ 4𝑚,

                                        Ψ𝜔1 ≤ 6𝑚 + 𝑌 ≤ 10𝑚.

Equality forces an alternating independent set in every variable cycle and one pure winner in
every clause copy, and is therefore equivalent to a satisfying assignment. Since the potential is


                                                   22
integer-valued, an unsatisfiable instance loses at least one.

4.1.3     Class-compatible padding

We use the following standard tangent argument.

Lemma 5 (Tangent padding). Let 𝑅 be a fixed regular graph. Suppose that 𝑅 has a distinguished
configuration whose total number of points and sum of squared scores are 𝑃0 > 0 and 𝑆0 ,
respectively. Define 𝜆 := 2𝑆
                          𝑃0 . Assume that every configuration of 𝑅, with corresponding values
                            0


(𝑃𝑅 , 𝑆𝑅 ), satisfies
                                       𝑆𝑅 − 𝜆𝑃𝑅 ≤ 𝑆0 − 𝜆𝑃0 ,                                      (34)

and equality in (34) is possible only if (𝑃𝑅 , 𝑆𝑅 ) = (𝑃0 , 𝑆0 ). Let 𝐻 be an arbitrary core graph, and
add 𝑡 disjoint copies of 𝑅 to 𝐻. For all sufficiently large polynomially bounded 𝑡, the following
statements hold.

        1. Every configuration maximising the HHI of the resulting disjoint union uses a configur-
          ation with values (𝑃0 , 𝑆0 ) on every copy of 𝑅.

        2. Suppose that every copy of 𝑅 uses such a distinguished configuration. Let Φ1 and Φ2 be
          two configurations of 𝐻, with values (𝑃1 , 𝑆1 ) and (𝑃2 , 𝑆2 ), respectively. If

                                             𝑆1 − 𝜆𝑃1 > 𝑆2 − 𝜆𝑃2 ,

          then the padded configuration obtained from Φ1 has strictly larger HHI than the padded
          configuration obtained from Φ2 .

The same value of 𝑡, polynomial in |𝑉 (𝐻)|, can be chosen simultaneously for all configurations
of 𝐻.

The proof of Lemma 5 is provided in Appendix D.1.

Padding gadgets construction.           We shall use the following cubic padding gadgets. Partition
both 𝐾3,3 and the triangular prism Π (see Figure 4) into the three edges of a perfect matching.
Let 𝑄3 be 𝐾4,4 with a perfect matching removed, with the two nonadjacent vertices 𝑎𝑖 , 𝑏𝑖 placed
in class 𝑖. In the externally balanced construction, each vertex of 𝐾4 forms a singleton class.
    For 𝜔 ≥ 4, put
                          𝐴𝜔 := 3𝜔 2 − 6𝜔 + 5,          𝐵𝜔 := 3𝜔 2 − 12𝜔 + 7.

Both numbers are positive. Define the fixed cubic padding graphs

                        𝑅F := 2𝐴𝜔 𝐾3,3 ∪˙ 𝜔𝐵𝜔 Π,         𝑅E := 𝐴𝜔 𝑄3 ∪˙ 𝜔𝐵𝜔 𝐾4 .

In the distinguished configuration of 𝑅F , every 𝐾3,3 is oriented bipartitely, and every prism
plays only draws. In the distinguished configuration of 𝑅E , every 𝑄3 is oriented bipartitely, and
every 𝐾4 plays only draws.



                                                   23
                                                                𝑎2


                                             𝑎1                               𝑎3



                                                                𝑏2


                                             𝑏1                                𝑏3

                    Figure 4: The triangular prism Π and its fully balanced partition
Note: The three thick (vertical) matching edges form the three classes.




 Structure             𝜔    Padding graph and configuration             𝑃0                    𝑆0                     𝜆

 fully balanced        3    𝐾3,3 , pure bipartite orientation           27                    243                   18
 externally balanced   3    𝑄3 , pure bipartite orientation             36                    324                   18
 fully balanced        ≥4   𝑅F as above                          108𝜔(𝜔 − 1)(𝜔 − 2)   54𝜔(𝜔 − 1)(3𝜔 2 − 7)   (3𝜔 2 − 7)/(𝜔 − 2)
 externally balanced   ≥4   𝑅E as above                          72𝜔(𝜔 − 1)(𝜔 − 2)    36𝜔(𝜔 − 1)(3𝜔 2 − 7)   (3𝜔 2 − 7)/(𝜔 − 2)

    We verify the hypotheses of Lemma 5. For 𝜔 = 3, the pure bipartite configurations maximise
Ψ𝜔3 on 𝐾3,3 and 𝑄3 , with respective values 27 and 36. For 𝜔 ≥ 4, Lemma 2 gives

             max Ψ𝜔1 (𝐾3,3 ) = 9,         max Ψ𝜔1 (𝑄3 ) = 12,             max Ψ𝜔1 (Π) = max Ψ𝜔1 (𝐾4 ) = 0.

The first two maxima are attained only by a pure bipartite orientation, up to reversing the two
sides, while the last two are attained only by the all-draw configuration. Indeed, in 𝐾3,3 a set of
two pure winners leaves three mixed vertices, while three pure winners form one bipartition side
and leave no mixed vertex. In 𝑄3 , an independent set of four vertices must be one bipartition
side. In Π, one pure winner creates three mixed vertices and two pure winners create four; in 𝐾4 ,
one pure winner creates three mixed vertices. Thus, equality fixes the displayed pair (𝑃0 , 𝑆0 ) in
every row.
    For the last two rows, a direct calculation gives

                                    2𝑆0   3𝜔 2 − 7
                                        =                       and hence           𝑞𝜆 = 1.
                                    𝑃0     𝜔−2

For the first two rows, 𝜆 = 18 and 𝑞𝜆 = 3. Consequently, (20) shows that the distinguished
configuration satisfies the strict tangent condition, and Lemma 5 applies.

Theorem 4 (Parameter one). For every fixed integer 𝜔 ≥ 3, computing the maximum HHI is
𝒩 𝒫-hard on each of the following graph classes:

       1. Cubic graphs with a fully balanced partition into three equal-size classes with parameter
             one;

       2. Cubic graphs with an externally balanced partition into four equal-size independent
             classes with parameter one.

                                                                24
Proof. For 𝜔 = 3, use the first or second row of the tangent-padding table and the 𝑞 = 3 part
of Lemma 3 or Lemma 4. For 𝜔 ≥ 4, use the corresponding 𝑅F or 𝑅E row and the 𝑞 = 1
part of the relevant core lemma. Equation (20) and Lemma 5 reduce maximising HHI to the
corresponding core potential, which is 𝒩 𝒫-hard. Every core and every padding component have
equal class sizes and the required parameter-one partition, so their disjoint union preserves the
restriction.

    We need one quantitative observation to pass from parameter one to parameter two. Replacing
the satisfiability core by a fixed number 𝐿 of disjoint copies multiplies its strict potential gap
by 𝐿 and preserves all class conditions. The preceding padding calculations therefore give the
following.
Lemma 6 (Amplified gap). For every fixed integer 𝜔 ≥ 3 and every constant 𝐴 > 0, either
reduction in Theorem 4 can be arranged to produce a graph 𝐻 on 𝑛 vertices and a threshold 𝜏
such that
                                                                             𝐴
                         YES: HHI *𝜔 (𝐻) ≥ 𝜏,         NO: HHI *𝜔 (𝐻) ≤ 𝜏 −      .
                                                                             𝑛2
The proof of Lemma 6 is provided in Appendix D.2.
Definition 1 (Complete 𝑘-fold blow-up). Let 𝐺 = (𝑉, 𝐸) be a graph and let 𝑘 ≥ 1 be an
integer. The complete 𝑘-fold blow-up 𝐵𝑘 (𝐺) is obtained by replacing each vertex 𝑣 ∈ 𝑉 with
an independent set of 𝑘 clones 𝑣 1 , . . . , 𝑣 𝑘 , and each edge 𝑢𝑣 ∈ 𝐸 with all 𝑘 2 edges between the
clones of 𝑢 and 𝑣. Formally,
                                                      {︀                                     }︀
               𝑉 (𝐵𝑘 (𝐺)) = 𝑉 × [𝑘],     𝐸(𝐵𝑘 (𝐺)) = {(𝑢, 𝑖), (𝑣, 𝑗)} : 𝑢𝑣 ∈ 𝐸, 𝑖, 𝑗 ∈ [𝑘] .

In particular, if 𝐺 is 𝑑-regular on 𝑁 vertices, then 𝐵𝑘 (𝐺) is 𝑘𝑑-regular on 𝑘𝑁 vertices and has
𝑘 2 |𝐸| edges.
Lemma 7. Let 𝐻 be a 𝑑-regular graph on 𝑛 vertices and let ℎ* = HHI *𝜔 (𝐻). Then

                               ℎ*                     ℎ* 𝜔(𝜔 − 2)2
                                  ≤ HHI *𝜔 (𝐵𝑘 (𝐻)) ≤   +          .                              (35)
                               𝑘                      𝑘    4𝑛2 𝑘

Proof. The symmetric lift of an optimal configuration of 𝐻 has 𝑘 2 times the total points and 𝑘 3
times the sum of squared scores, proving the lower bound.
                                                         ̂︀ of 𝐵 (𝐻). Independently choose one
    For the upper bound, take an arbitrary configuration Φ      𝑘
clone of every original vertex and project the selected clone edges to a random configuration Φ
of 𝐻. Then
                                  𝑊
                                  ̂︁                       𝑃 (Φ)
                                                              ̂︀                    Γ
                                                                                    ̂︀ 𝜔
                     E[𝑊 (Φ)] =      ,      E[𝑃 (Φ)] =           ,   E[Γ𝜔 (Φ)] ≤         .        (36)
                                  𝑘2                        𝑘2                      𝑘3
The third inequality follows by expanding each product 𝑤𝑣 ℓ𝑣 , 𝑤𝑣 𝑑𝑣 , 𝑑𝑣 ℓ𝑣 : a projected ordered
pair of distinct original edges is sampled with probability 1/𝑘 3 , while the corresponding clone
product may contain additional nonnegative pairs arising from the same original edge.
    Put 𝑎 := 𝜔 2 − 2. Since 𝐻 has 𝑛 vertices and degree 𝑑,

                                                                             𝑊
                                                                             ̂︁   Γ
                                                                                  ̂︀ 𝜔
                    E[𝑆(Φ)] = 𝑛𝑑2 + 𝑑𝑎 E[𝑊 (Φ)] − E[Γ𝜔 (Φ)] ≥ 𝑛𝑑2 + 𝑑𝑎          −      .
                                                                             𝑘2   𝑘3

                                                    25
On the other hand, 𝐵𝑘 (𝐻) has 𝑛𝑘 vertices and degree 𝑑𝑘, so

                       𝑆(Φ)
                         ̂︀   (𝑛𝑘)(𝑑𝑘)2 + (𝑑𝑘)𝑎𝑊
                                               ̂︁ − Γ
                                                    ̂︀ 𝜔
                                                             2      𝑊
                                                                    ̂︁   Γ
                                                                         ̂︀ 𝜔
                            =                            = 𝑛𝑑  + 𝑑𝑎    −      .
                        𝑘3               𝑘3                         𝑘2   𝑘3

Taking expectations,
                                           𝑆(Φ)
                                             ̂︀
                                                ≤ ℎ* E[𝑃 (Φ)2 ].                             (37)
                                            𝑘3
From (37) and E[𝑃 (Φ)2 ] = E[𝑃 (Φ)]2 + Var(𝑃 (Φ)), we obtain
                                                  [︃                           ]︃
                                  𝑆(Φ)         ̂︀ 2
                                          * 𝑃 (Φ)
                                    ̂︀
                                       ≤ ℎ          + Var(𝑃 (Φ)) .
                                   𝑘3         𝑘4

Since 𝑆(Φ) ≤ ℎ* 𝑃 (Φ)2 for every projection,

                                    𝑆(Φ)
                                      ̂︀          ℎ* 𝑘 3 ℎ* Var(𝑃 (Φ))
                                              ≤     +                  .
                                       ̂︀ 2
                                    𝑃 (Φ)         𝑘           ̂︀ 2
                                                           𝑃 (Φ)

Now 𝑃 = 𝑑𝑛 + (𝜔 − 2)𝑊 , so
                                      Var(𝑃 ) = (𝜔 − 2)2 Var(𝑊 ).

Writing 𝑊 as the sum of the decisiveness indicators of the 𝑛𝑑/2 edges, vertex-disjoint indicators
are independent, while every variance and every absolute covariance is at most 1/4. Since there
are 𝑛 𝑑2 adjacent edge pairs,
     (︀ )︀


                                                  𝑛𝑑 𝑛𝑑(𝑑 − 1)   𝑛𝑑2
                                  Var(𝑊 ) ≤          +         ≤     .
                                                   8     4        4

Furthermore, ℎ* ≤ 𝜔/𝑛, because 𝑆 ≤ (𝜔𝑑)𝑃 and 𝑃 ≥ 𝑛𝑑, and 𝑃 (Φ)
                                                            ̂︀ ≥ 𝑘 2 𝑛𝑑. Substitution gives
the stated error term.

Theorem 5 (Parameter 𝑟). For every fixed integer 𝜔 ≥ 3 and 𝑟 ≥ 1, computing the maximum
HHI is 𝒩 𝒫-hard on each of the following graph classes:

      1. 3𝑟-regular graphs with a fully balanced partition into three equal-size classes with
             parameter 𝑟;

      2. 3𝑟-regular graphs with an externally balanced partition into four equal-size independent
             classes with parameter 𝑟.

Proof. Use Lemma 6 with 𝐴 > 𝜔(𝜔 − 2)2 /4𝑟 and construct 𝐵𝑟 (𝐻). Put all clones of a vertex
into its original class. Every original neighbour in a class creates 𝑟 clone neighbours in that
class, so the parameter becomes 𝑟; independent classes remain independent. In a YES-instance,
the symmetric lift has HHI at least 𝜏 /𝑟. In a NO-instance,

                                              1        𝐴                  𝜔(𝜔 − 2)2  𝜏
                                                       (︂        )︂
                            HHI *𝜔 (𝐵𝑟 (𝐻)) ≤       𝜏− 2              +             < .
                                                  𝑟   𝑛                     4𝑛2 𝑟    𝑟

Thus 𝜏 /𝑟 separates the two cases.



                                                            26
4.2    Fixed total points
We now move to the case when the total number of points is fixed: either draws are prohibited
and a win is worth any fixed 𝜔 > 0 points, or draws are allowed under the (2, 1, 0) rule. In the
latter case, an optimum contains no draws. Indeed, if a draw 𝑢𝑣 gives the teams 𝑥 + 1 and
𝑦 + 1 points with 𝑥 ≥ 𝑦 from their other matches, replacing it by a win of 𝑢 changes the sum of
squared scores by

                     (𝑥 + 2)2 + 𝑦 2 − (𝑥 + 1)2 − (𝑦 + 1)2 = 2(𝑥 − 𝑦 + 1) > 0.

Thus, in both settings we may orient every edge and maximise

                                     ∑︁                              𝐴(Φ)
                           𝐴(Φ) :=         𝑤𝑣2 ,      HHI 𝜔 (Φ) =           .
                                     𝑣∈𝑉
                                                                    |𝐸(𝐺)|2

Theorem 6 (Fixed total points, parameter one). In either fixed-total-points setting, computing
the maximum HHI is 𝒩 𝒫-hard on each of the following classes:

       1. Cubic graphs with a fully balanced partition into three classes with parameter one;

       2. Cubic graphs with an externally balanced partition into four independent classes with
          parameter one.

Proof. For a cubic graph on 𝑁 vertices, let ℓ𝑣 be the indegree of 𝑣. Since 𝑤𝑣 + ℓ𝑣 = 3 and
∑︀
  𝑣 𝑤𝑣 = 3𝑁/2,
                                                   9𝑁 ∑︁
                                      𝐴(Φ) =          −   𝑤𝑣 ℓ𝑣 .
                                                    2   𝑣

A vertex contributes two to the last sum exactly when it has both an incoming and an outgoing
edge. If 𝑀 (Φ) is the set of such mixed vertices, then

                                                   9𝑁
                                     𝐴(Φ) =           − 2|𝑀 (Φ)|.
                                                    2

The pure winners and pure losers form two independent sets, so 𝑀 (Φ) is an odd cycle transversal.
Conversely, from any odd cycle transversal 𝑋, orient the bipartite graph 𝐺 − 𝑋 with bipartition
(𝐿, 𝑅) from 𝐿 to 𝑅, orient the edges between 𝐿 and 𝑋 towards 𝑋 and the ones between 𝑋 and
𝑅 towards 𝑅. Finally, orient the remaining edges within 𝑋 arbitrarily. Hence

                                                    9𝑁
                                      𝐴* (𝐺) =         − 2𝜏 (𝐺),                                (38)
                                                     2

where 𝜏 (𝐺) is the minimum odd cycle transversal size.
     We reduce from Linear Nae-3-Sat in which every clause has three distinct literals and
every variable occurs exactly three times positively and three times negatively; this problem is
𝒩 𝒫-complete (Darmann et al., 2024). Use the two balanced cubic cores 𝐹𝜙 and 𝐸𝜙 defined in
Section 4.1.2; the construction itself is independent of the scoring system.
     Every clause triangle forces at least one vertex into an odd cycle transversal. If 𝜙 is NAE-
satisfiable, colour each variable cycle by literal truth values and, in every clause triangle, delete
the vertex of one literal while retaining two literals of different truth values. Colour the two

                                                     27
surviving clause vertices opposite to their occurrence neighbours. The remaining graph is
bipartite. Conversely, a transversal meeting the lower bound deletes exactly one vertex from
every clause triangle and no variable vertex; each intact alternating variable cycle determines a
truth value, and the two surviving adjacent clause vertices force two literals of the clause to
have different truth values. Therefore,

                             𝜏 (𝐹𝜙 ) = 𝑚    ⇐⇒     𝜙 is NAE-satisfiable,

and, since there are four clause triangles per clause in 𝐸𝜙 ,

                            𝜏 (𝐸𝜙 ) = 4𝑚     ⇐⇒     𝜙 is NAE-satisfiable.

The first graph has 6𝑚 vertices and the second has 24𝑚 vertices. By (38), their orientation
thresholds are 25𝑚 and 100𝑚, respectively. Dividing by |𝐸(𝐺)|2 gives the corresponding HHI
thresholds.

   We now extend this result to parameter 𝑟.
Lemma 8. For every regular graph 𝐺, 𝐴* (𝐵𝑘 (𝐺)) = 𝑘 3 𝐴* (𝐺).
Proof. Lifting an orientation of 𝐺 symmetrically gives the lower bound. For the reverse inequality,
                                            ∑︀
suppose 𝐺 is 𝑑-regular and put 𝐶(Φ) :=        𝑣 𝑤𝑣 ℓ𝑣 . Since 𝑤𝑣 + ℓ𝑣 = 𝑑,


                                      𝐴(Φ) = 𝑑|𝐸(𝐺)| − 𝐶(Φ).

                     ̂︀ of 𝐵 (𝐺), independently choose one clone of every original vertex, and
Take any orientation Φ      𝑘
project to an orientation Φ of 𝐺. Expanding 𝑤𝑣 ℓ𝑣 into ordered pairs of distinct incident edges
gives
                                                       𝐶(Φ)
                                                         ̂︀
                                           E[𝐶(Φ)] ≤        ;
                                                        𝑘3
the clone product may additionally count two clone edges corresponding to the same original
              ̂︀ ≥ 𝑘 3 minΦ 𝐶(Φ). Since 𝐵 (𝐺) has degree 𝑘𝑑 and 𝑘 2 |𝐸(𝐺)| edges,
edge. Hence 𝐶(Φ)                         𝑘


                             ̂︀ ≤ 𝑘 3 𝑑|𝐸(𝐺)| − 𝑘 3 min 𝐶(Φ) = 𝑘 3 𝐴* (𝐺).
                           𝐴(Φ)
                                                       Φ




Theorem 7 (Fixed total points, parameter 𝑟). In either fixed-total-points setting, computing
the maximum HHI is 𝒩 𝒫-hard on each of the following classes:
        1. 3𝑟-regular graphs with a fully balanced partition into three classes with parameter 𝑟 ≥ 1;

        2. 3𝑟-regular graphs with an externally balanced partition into four independent classes
          with parameter 𝑟 ≥ 1.
Proof. Apply the complete 𝑟-fold blow-up to either graph in Theorem 6 and put all clones of a
vertex into its original class. The class parameter gets multiplied by 𝑟 and independent classes
remain independent. By Lemma 8, the orientation threshold is multiplied by 𝑟3 , while the
number of edges is multiplied by 𝑟2 ; thus, the HHI threshold is divided by 𝑟.

                                                  28
    Finally, the total number of points is also fixed under the (3,2,1,0) scoring system; this case
is discussed in Appendix E.


5    Conclusions
Our paper has focused on computing the maximum Herfindahl–Hirschman index in incomplete
round-robin tournaments, represented by regular graphs. We have derived sharp lower (The-
orem 3) and upper (Theorem 1) bounds for it. The former is reached when the tournament
consists of round-robin groups, while the latter is reached – under the (2, 1, 0) and (3, 1, 0) scoring
systems – when the set of matches forms a bipartite graph. These bounds are important because
determining the maximum HHI is 𝒩 𝒫-hard even if the teams are divided into pots, and each
team plays the same number of matches 𝑟 against teams from any pot. In particular, finding
the maximum is computationally difficult for all parameters 𝑟 ≥ 1 if the value of a win is at
least three points (Theorem 5). This is a highly relevant case in practice, because the (3,1,0)
scoring system is used in football, and the number of opponents from a given pot is either 𝑟 = 1
(UEFA Conference League) or 𝑟 = 2 (UEFA Champions League) in some major tournaments.
Even though fixing the denominator of HHI by prohibiting draws or using the (2,1,0) scoring
system simplifies the problem, computing the maximum HHI remains 𝒩 𝒫-hard for all 𝑟 ≥ 1
(Theorem 7). Both Theorems 5 and 7 remain valid if the teams do not play against teams from
their own pot, as in the Champions Hockey League.
    Several questions remain open. First, despite the 𝒩 𝒫-hardness results, it would be interesting
to develop approximation algorithms with stronger guarantees, particularly for balanced tourna-
ment graphs. Practical methods, such as integer programming formulations and local-search
heuristics, could also be valuable for computing or approximating the maximum HHI of actual
tournament schedules. A related issue is the range of maximum HHI in a given tournament.
For example, in the UEFA Champions League, there are nine teams in each of four pots, and
each team faces exactly two opponents from every pot. Hence, the set of matches could not form
a bipartite graph, and the lower and upper bounds derived in Section 3 can be improved.
    Typical tournament structures might be more interesting than extremal cases. For instance,
how close is the maximum HHI of a randomly generated balanced tournament to the theoretical
upper and lower bounds? Studying its expected value and concentration, especially as the
number of teams grows, could reveal whether highly unequal outcomes are mainly a consequence
of exceptional schedules or occur frequently even in randomly designed competitions. Further
extensions could consider unequal numbers of matches and repeated encounters between teams.


Acknowledgements
The research was supported by the National Research, Development and Innovation Office under
Grants Advanced 152220 and FK 145838, and the János Bolyai Research Scholarship of the
Hungarian Academy of Sciences.




                                                  29
References
Avila-Cano, A., Owen, P. D., and Triguero-Ruiz, F. (2023). Measuring competitive balance in
  sports leagues that award bonus points, with an application to rugby union. European Journal
  of Operational Research, 309(2):939–952.

Avila-Cano, A., Ruiz-Sepulveda, A., and Triguero-Ruiz, F. (2021). Identifying the maximum
  concentration of results in bilateral sports competitions. Mathematics, 9(11):1293.

Cochran, R. S. (1971). Designs with redeeming social aspects for evenings of social bridge. The
  American Statistician, 25(2):12–15.

Csató, L. (2017). On the ranking of a Swiss system chess team tournament. Annals of Operations
  Research, 254(1-2):17–36.

Csató, L. and Gyimesi, A. (2026). A probabilistic match classification model for low-scoring
  sports. Manuscript. DOI: 10.48550/arXiv.2601.09673.

Csató, L. and Petróczy, D. G. (2025). Competitive balance in the UEFA Champions League
  group stage: Novel measures show no evidence of decline. Annals of Operations Research,
  352(1-2):105–120.

Darmann, A. and Döcker, J. (2021). On simplified NP-complete variants of Monotone 3-Sat.
  Discrete Applied Mathematics, 292:45–58.

Darmann, A., Döcker, J., and Dorn, B. (2024). An even simpler hard variant of Not-All-Equal
  3-SAT. Manuscript. DOI: 10.48550/arXiv.2412.03395.

de Werra, D., Urrutia, S., and Assunção, L. (2026). Break minimization in incomplete round-robin
  tournaments. Discrete Applied Mathematics, 387:6–14.

Depken, C. A. (1999). Free-agency and the competitiveness of Major League Baseball. Review
  of Industrial Organization, 14(3):205–217.

Devriesere, K., Csató, L., and Goossens, D. (2025). Tournament design: A review from an
  operational research perspective. European Journal of Operational Research, 324(1):1–21.

Devriesere, K. and Goossens, D. (2025). Redesigning Belgian youth field hockey competitions
  using an incomplete round-robin tournament. INFORMS Journal on Applied Analytics,
  55(6):457–468.

Devriesere, K., Goossens, D., and Spieksma, F. (2026). From groups to a single league: Evaluating
  competitiveness in the UEFA Champions League. Journal of Quantitative Analysis in Sports,
  in press. DOI: 10.1515/jqas-2025-0128.

Devriesere, K., Goossens, D., and Spieksma, F. (2027). Finding breakfree timetables for
  incomplete round robin tournaments. Operations Research Letters, 70:107528.

Fort, R. and Maxcy, J. (2003). Competitive balance in sports leagues: An introduction. Journal
  of Sports Economics, 4(2):154–160.

                                               30
Hajnal, A. and Szemerédi, E. (1970). Proof of a conjecture of Erdős. In Erdős, P., Rényi, A.,
  and T. Sós, V., editors, Combinatorial Theory and its Application, volume 2, pages 601–623.
  North-Holland, London, United Kingdom.

Herfindahl, O. C. (1950). Concentration in the Steel Industry. PhD thesis, Columbia University,
  New York.

Hirschman, A. O. (1945). National Power and the Structure of Foreign Trade. University of
  California Press, Berkeley and Los Angeles, California, USA.

Hirschman, A. O. (1964). The paternity of an index. American Economic Review, 54(5):761–762.

Horowitz, I. (1997). The increasing competitive balance in major league baseball. Review of
  industrial Organization, 12(3):373–387.

Humphreys, B. R. (2002). Alternative measures of competitive balance in sports leagues. Journal
  of Sports Economics, 3(2):133–148.

Kierstead, H. A. and Kostochka, A. V. (2008). A short proof of the Hajnal–Szemerédi theorem
  on equitable colouring. Combinatorics, Probability and Computing, 17(2):265–270.

Leiva Bertrán, F. (2025). Ranking in incomplete tournaments: The generalized win percentage
  method, efficiency, and NCAA football. Journal of Sports Economics, 26(1):3–34.

Li, M., Van Bulck, D., and Goossens, D. (2025). Beyond leagues: A single incomplete round robin
  tournament for multi-league sports timetabling. European Journal of Operational Research,
  323(1):208–223.

Owen, P. D. and Owen, C. A. (2022). Simulation evidence on Herfindahl-Hirschman measures
  of competitive balance in professional sports leagues. Journal of the Operational Research
  Society, 73(2):285–300.

Owen, P. D., Ryan, M., and Weatherston, C. R. (2007). Measuring competitive balance
  in professional team sports using the Herfindahl-Hirschman index. Review of Industrial
  Organization, 31(4):289–302.

Sauer, P., Cseh, Á., and Lenzner, P. (2024). Improving ranking quality and fairness in Swiss-
  system chess tournaments. Journal of Quantitative Analysis in Sports, 20(2):127–146.

Schmidt, M. B. and Berri, D. J. (2001). Competitive balance and attendance: The case of Major
  League Baseball. Journal of Sports Economics, 2(2):145–167.

Szymanski, S. (2003). The economic design of sporting contests. Journal of Economic Literature,
  41(4):1137–1187.

Triguero-Ruiz, F. and Avila-Cano, A. (2023). On competitive balance in the group stage of the
  UEFA Champions League. Scottish Journal of Political Economy, 70(3):231–248.




                                              31
UEFA (2026). New concept for men’s national team competitions as of 2028 approved today.
  20 May. https://www.uefa.com/news-media/news/02a5-20aba2a6e7e9-38897428c81f-
  1000--new-concept-for-men-s-national-team-competitions-as-of-2028/.

Wessel, S. and Spieksma, F. (2026). Finding fair draws for incomplete round robin tournaments.
  Manuscript. DOI: 10.48550/arXiv.2607.17901.




                                             32
Appendix

A     HHI *𝜔 in round-robin tournaments
A single round-robin tournament is a special incomplete round-robin tournament, where 𝑑 = 𝑁 −1
and 𝐺 = 𝐾𝑁 = 𝐾𝑑+1 . As discussed in the following, the maximum Herfindahl–Hirschman index
is known in this case, even if two teams play more than one match against each other.
    If 𝜔 = 2, that is, two points are awarded for a win and one point for a draw, HHI *2 occurs
when one team wins all of its matches, the second team defeats all teams except for the first
team, and so on, down to the weakest team that always loses (Owen et al., 2007). As shown in
Owen et al. (2007, Appendix):
                                                                        2(2𝑁 − 1)
                                                     HHI *2 =                      .
                                                                        3𝑁 (𝑁 − 1)
    However, this upper bound is invalid for sports with 𝜔 = 3, such as in (association) football.
Consider a (single) round-robin tournament with 𝑛 = 4 teams. The previous logic suggests that
the most unequal point distribution is (9, 6, 3, 0), which gives
                                          )︂2                 )︂2                 )︂2                 )︂2
                                      9                   6                  3                   0               1 1  1  7
                                (︂                  (︂                  (︂                  (︂
              HHI 3 (𝑞 = 0) =                   +                   +                   +                   =     + +   = .
                                     18                  18                  18                  18              4 9 36  18

But, if 𝑞 (0 ≤ 𝑞 ≤ 𝑁 − 1) teams play only draws against each other, then the total number
of points 𝑃 is reduced, which might increase HHI 3 . Returning to the example, the possible
point distribution (9, 6, 1, 1) leads to HHI 3 (𝑞 = 2) = 81/289 + 36/289 + 2 · 1/289 = 7/17, while
the point distribution (9, 2, 2, 2) results in HHI 3 (𝑞 = 3) = 9/25 + 3 · 4/225 = 31/75. Clearly,
HHI 3 (𝑞 = 3) > HHI 3 (𝑞 = 2) > HHI 3 (𝑞 = 0).
    According to Avila-Cano et al. (2021, Proposition 1):

                           2𝑞 3 + (−6𝑁 + 5/2) 𝑞 2 + 6𝑁 2 − 5𝑛 + 1/2 𝑞 + 𝑁 (𝑁 − 1)2
                                                                             (︀                                 )︀
               HHI 3 (𝑞) =                                                         .
                                      [−𝑞 2 + (2𝑁 − 1)𝑞 + 2𝑁 (𝑁 − 1)]2 /4

    HHI 3 (𝑞) has a unique maximum for a particular 0 ≤ 𝑞 ≤ 𝑁 − 1 (Avila-Cano et al., 2021,
Theorem 1), and the upper bound of HHI 3 is given by HHI *3 = HHI 3 (𝑞 * ), where 𝑞 * is the smallest
integer satisfying the following fifth-degree inequality (Avila-Cano et al., 2021, Theorem 2):

            1  5      9 4                       7 3                          9 2
         [︂          (︂              )︂         (︂                                      )︂             (︂                     )︂
  0 >      − 𝑞5 +𝑁+     𝑞 + −8𝑁 2 + 12𝑁 −          𝑞 + 11𝑁 3 + 27𝑁 2 + 18𝑁 −   𝑞
            2  2      4                         2                            4
                             15 1
       (︂                          )︂                                    ]︂
      + 8𝑁 4 − 6𝑁 3 − 9𝑁 2 +   −      𝑞 − 4𝑁 5 + 12𝑁 4 − 13𝑁 3 + 6𝑁 2 − 𝑁 .
                             2   2

    It is worth noting that Avila-Cano et al. (2021) only compare win distributions where the first
set of teams win all their matches played against the second set of teams, and all matches played
by teams from the second set are draws. Consequently, finding the 𝑞 optimising HHI 3 (𝑞) does
not necessarily maximise HHI 3 globally. According to Lemma 1, there does exist an optimum
based on a win distribution of this form for multiple independent round-robin tournaments.




                                                                        33
B     Proof of Step 2 in Lemma 1
Let 𝑃0 and 𝑆0 be the global total points and sum of squared scores, respectively, when 𝑣 draws
all its 𝑚 matches in 𝑅. Define
                                      𝑤
                                     ∑︁                                 𝑚
                                                                        ∑︁
                             𝑅𝑤 :=         𝑟𝑖    and         𝑅𝑚 :=            𝑟𝑖 .
                                     𝑖=1                                𝑖=1

If 𝑣 defeats precisely the first 𝑤 vertices, then its score changes from 𝑚 to

                                            𝑚 + (𝜔 − 1)𝑤,

while each defeated vertex loses one point. Consequently,

                                           𝑃 (𝑤) = 𝑃0 + 𝑐𝜔 𝑤                                     (39)

and
                                                                   𝑤 [︁                     ]︁
                     𝑆(𝑤) = 𝑆0 + [𝑚 + (𝜔 − 1)𝑤]2 − 𝑚2 +
                                                                  ∑︁
                                                                          (𝑟𝑖 − 1)2 − 𝑟𝑖2
                                                                  𝑖=1

                          = 𝑆0 + 2𝑚(𝜔 − 1)𝑤 + (𝜔 − 1) 𝑤2 − 2𝑅𝑤 + 𝑤.
                                                             2
                                                                                                 (40)

    We compare this value with the two boundary configurations 𝑤 = 0 and 𝑤 = 𝑚. Put

                                                       𝑤
                                                𝑡 :=     .
                                                       𝑚

By (40),

                         (1 − 𝑡)𝑆(0) + 𝑡𝑆(𝑚) − 𝑆(𝑤)
                                                                  𝑤
                                                             (︂                      )︂
                              = (𝜔 − 1)2 𝑤(𝑚 − 𝑤) − 2               𝑅𝑚 − 𝑅𝑤 .                    (41)
                                                                  𝑚

    We now bound the term in parentheses. Let 𝑠𝑖 := 𝑟𝑖 − 1 be the score of vertex 𝑖 from matches
played entirely inside 𝑅 ∖ {𝑣}. The added one point cancels because the coefficients below sum
to zero, and hence
                                            𝑚               𝑤
                            𝑤           𝑤 ∑︁         𝑚 − 𝑤 ∑︁
                              𝑅𝑚 − 𝑅𝑤 =         𝑠𝑖 −          𝑠𝑖 .                               (42)
                            𝑚           𝑚 𝑖=𝑤+1       𝑚 𝑖=1

Regard the first 𝑤 vertices as a bottom set 𝐵 and the remaining 𝑚 − 𝑤 vertices as a top set 𝑇 .
We maximise the right-hand side of (42) match by match.
    A match inside 𝑇 has coefficient 𝑤/𝑚 at both endpoints, so its contribution is at most 𝜔𝑤/𝑚.
A match inside 𝐵 has coefficient −(𝑚 − 𝑤)/𝑚 at both endpoints, so its contribution is at most
−2(𝑚 − 𝑤)/𝑚. Finally, a match between 𝑇 and 𝐵 contributes the most when the vertex in 𝑇




                                                  34
wins, in which case its contribution is 𝜔𝑤/𝑚. Therefore,
                                     [︃(︃         )︃                 ]︃       (︃ )︃
                 𝑤            𝜔𝑤            𝑚−𝑤              2(𝑚 − 𝑤) 𝑤
                   𝑅𝑚 − 𝑅 𝑤 ≤                   + 𝑤(𝑚 − 𝑤) −
                 𝑚            𝑚              2                  𝑚     2
                                  𝑤(𝑚 − 𝑤)
                              =            [𝜔(𝑚 + 𝑤 − 1) − 2𝑤 + 2] .                  (43)
                                    2𝑚

Combining (41) and (43) gives

                         (1 − 𝑡)𝑆(0) + 𝑡𝑆(𝑚) − 𝑆(𝑤) ≥ 𝜅𝜔,𝑚,𝑤 𝑤(𝑚 − 𝑤),                (44)

where

                                                𝜔(𝑚 + 𝑤 − 1) − 2𝑤 + 2
                          𝜅𝜔,𝑚,𝑤 := (𝜔 − 1)2 −
                                                          𝑚
                                                   𝑐𝜔 (𝑤 − 1)
                                  = (𝜔 − 1)2 − 𝜔 −            .                       (45)
                                                       𝑚

   Let
                                            𝑆(0) 𝑆(𝑚)
                                                {︂                   }︂
                                   𝑀 := max       ,                       .
                                            𝑃 (0)2 𝑃 (𝑚)2
Since both boundary configurations are configurations of the original 𝑁 -vertex graph and
𝑁 ≥ 𝑚 + 1, (4) implies
                                                           𝐶𝜔
                                                     {︂         }︂
                                      𝑀 ≤ min 1,              .                       (46)
                                                          𝑚+1
We claim that for 𝑤 ∈
                    / {0, 𝑚}
                                             𝜅𝜔,𝑚,𝑤 ≥ 𝑀 𝑐2𝜔 .                         (47)

   First suppose that 𝜔 = 3. Then 𝑐𝜔 = 1, 𝐶𝜔 = 2, and

                                    𝑤−1   𝑚−𝑤+1   2    2
                     𝜅3,𝑚,𝑤 = 1 −       =       ≥   >     ≥ 𝑀.
                                     𝑚      𝑚     𝑚   𝑚+1

   Now suppose that 𝜔 ≥ 4, so 𝑐𝜔 ≥ 2. Since 𝜔 = 𝑐𝜔 + 2 and 𝑤 − 1 ≤ 𝑚 − 2, we get
(𝜔 − 1)2 − 𝜔 = 𝑐2𝜔 + 𝑐𝜔 − 1 and

                                    −𝑐𝜔 (𝑤 − 1)         2𝑐𝜔
                                                ≥ −𝑐𝜔 +     .
                                         𝑚               𝑚

Thus,

                                                             2𝑐𝜔
                                     𝜅𝜔,𝑚,𝑤 ≥ 𝑐2𝜔 − 1 +          .                    (48)
                                                              𝑚

If 𝑚 ≤ 2𝑐𝜔 , the right-hand side is at least 𝑐2𝜔 , and (47) follows from 𝑀 ≤ 1.
   If 𝑚 > 2𝑐𝜔 , then
                                               𝐶𝜔     𝐶𝜔
                                     𝑀≤           <         .
                                              𝑚+1   2𝑐𝜔 + 1
Furthermore,
                                              𝐶𝜔 ≤ 𝑐𝜔 + 1.                            (49)




                                                     35
Indeed, 𝑐𝜔 = 𝜔 − 2, and hence 𝑐𝜔 + 1 = 𝜔 − 1. Since 𝜔 ≥ 4,

                                                    (𝜔 2 − 2)2
                      𝐶𝜔 ≤ 𝑐𝜔 + 1 ⇐⇒                              ≤𝜔−1
                                                 4𝜔(𝜔 − 1)(𝜔 − 2)
                                            ⇐⇒ (𝜔 2 − 2)2 ≤ 4𝜔(𝜔 − 1)2 (𝜔 − 2).

Substituting 𝜔 = 𝑐𝜔 + 2, the difference between the right-hand side and the left-hand side
becomes

                        4𝜔(𝜔 − 1)2 (𝜔 − 2) − (𝜔 2 − 2)2
                                = 4(𝑐𝜔 + 2)(𝑐𝜔 + 1)2 𝑐𝜔 − (𝑐2𝜔 + 4𝑐𝜔 + 2)2
                                  (︁                                 )︁
                                = 4𝑐4𝜔 + 16𝑐3𝜔 + 20𝑐2𝜔 + 8𝑐𝜔
                                       (︁                                  )︁
                                  − 𝑐4𝜔 + 8𝑐3𝜔 + 20𝑐2𝜔 + 16𝑐𝜔 + 4
                                = 3𝑐4𝜔 + 8𝑐3𝜔 − 8𝑐𝜔 − 4
                                = (3𝑐4𝜔 − 4) + 8𝑐𝜔 (𝑐2𝜔 − 1) > 0,

where the final inequality follows from 𝑐𝜔 ≥ 2. Therefore, 𝐶𝜔 < 𝑐𝜔 + 1, which proves (49). Since

                                  (𝑐𝜔 + 1)𝑐2𝜔 ≤ (2𝑐𝜔 + 1)(𝑐2𝜔 − 1),

where the difference between the right- and left-hand sides is 𝑐3𝜔 − 2𝑐𝜔 − 1 ≥ 0, we obtain

                                            (𝑐𝜔 + 1)𝑐2𝜔
                               𝑀 𝑐2𝜔 <                  ≤ 𝑐2𝜔 − 1 < 𝜅𝜔,𝑚,𝑤 .
                                              2𝑐𝜔 + 1

This proves (47).
   By (39),
                                   𝑃 (𝑤) = (1 − 𝑡)𝑃 (0) + 𝑡𝑃 (𝑚),

and a direct expansion gives

                        (1 − 𝑡)𝑃 (0)2 + 𝑡𝑃 (𝑚)2 = 𝑃 (𝑤)2 + 𝑐2𝜔 𝑤(𝑚 − 𝑤).                      (50)

Using the definition of 𝑀 , followed by (44), (47), and (50), we obtain

                     𝑆(𝑤) ≤ (1 − 𝑡)𝑆(0) + 𝑡𝑆(𝑚) − 𝜅𝜔,𝑚,𝑤 𝑤(𝑚 − 𝑤)
                                  [︁                            ]︁
                           ≤ 𝑀 (1 − 𝑡)𝑃 (0)2 + 𝑡𝑃 (𝑚)2 − 𝑀 𝑐2𝜔 𝑤(𝑚 − 𝑤)
                           = 𝑀 𝑃 (𝑤)2 .

Therefore,
                                 𝑆(𝑤)         𝑆(0) 𝑆(𝑚)
                                                     {︂                   }︂
                                        ≤ max       ,                          .
                                 𝑃 (𝑤)2       𝑃 (0)2 𝑃 (𝑚)2
Thus, a highest remaining vertex with both wins and draws is dominated by one of the two
boundary configurations: it may be made to draw every match or to win every match.



                                                      36
C       Proof of Proposition 1
Proof. We first calculate the optimum on 𝐾4 . By Lemma 1, an optimal configuration is a
truncated cascade. For 𝜔 = 5, the four possible bottom-tier sizes 𝑥 ∈ {1, 2, 3, 4} give the
following score vectors:

                                    𝑥      Score vector           HHI 𝜔

                                       1     (15, 10, 5, 0)        7/18
                                       2     (15, 10, 1, 1)      109/243
                                       3       (15, 2, 2, 2)     79/147
                                       4       (3, 3, 3, 3)        1/4

Consequently,
                                                                79
                                             HHI *5 (𝐾4 ) =         .                          (51)
                                                                147
    It remains to determine the optimum on 𝐾3,3 . Let 𝑊 be the number of decisive matches.
Since 𝑁 = 6, 𝑑 = 3, and 𝜔 = 5, the identities for the number of points and sum of squares in (1)
and (2) become

                                           𝑃 = 18 + 3𝑊,                                        (52)
                                           𝑆 = 54 + 69𝑊 − Γ5 ,                                 (53)

where
                                       ∑︁
                                Γ5 =           (25𝑤𝑣 ℓ𝑣 + 16𝑤𝑣 𝑑𝑣 + 𝑑𝑣 ℓ𝑣 ) .                  (54)
                                       𝑣∈𝑉

    We show that
                                                   𝑆     77
                                                     2
                                                       ≤     .                                 (55)
                                                   𝑃     216
Equivalently, by (52) and (53), it is enough to prove

                                                             77
                                 Γ5 ≥ 54 + 69𝑊 −                 (18 + 3𝑊 )2 .                 (56)
                                                             216

The right-hand side of (56) is nonpositive for

                                           𝑊 ∈ {0, 1, 2, 7, 8, 9},

so these cases follow immediately from Γ5 ≥ 0. For the remaining values, it equals

                                           𝑊                       3      4      5   6
                                                                   9     55   259
                           Required lower bound on Γ5                                6
                                                                   8     6    24
    If a vertex has exactly one or two wins, then its contribution to Γ5 is at least 32. Indeed, if
𝑤𝑣 = 1, then 𝑑𝑣 + ℓ𝑣 = 2, and
                                       25ℓ𝑣 + 16𝑑𝑣 + 𝑑𝑣 ℓ𝑣 ≥ 32;

if 𝑤𝑣 = 2, then 𝑑𝑣 + ℓ𝑣 = 1, and its contribution is either 32 or 50.


                                                        37
     Suppose first that 𝑊 = 3. If some winning vertex is not a pure winner, then Γ5 ≥ 32.
Otherwise, there is exactly one pure winner. Its three opponents each have state (0, 2, 1), while
all remaining matches are draws. Thus, these three opponents contribute two each to Γ5 , and

                                                      9
                                              Γ5 ≥ 6 > .
                                                      8

     If 𝑊 ∈ {4, 5}, the wins cannot all belong to pure winners because every pure winner
contributes exactly three wins. Hence, some vertex has one or two wins, and

                                                              55 259
                                                         {︂        }︂
                                   Γ5 ≥ 32 > max                ,    .
                                                               6 24

     Finally, let 𝑊 = 6. If some winning vertex is not pure, then again Γ5 ≥ 32. Otherwise,
there are exactly two pure winners. Pure winners form an independent set, so in 𝐾3,3 they must
belong to the same bipartition class. Each vertex in the opposite class then has state (0, 1, 2)
and contributes two to Γ5 . Therefore,
                                                Γ5 ≥ 6.

This proves (55) in every case.
     Equality is attained when two vertices in the same bipartition class win all their matches
and the third vertex in that class draws all its matches. The score vector is

                                           (15, 15, 3, 1, 1, 1),

so
                                         152 + 152 + 32 + 12 + 12 + 12   77
                      HHI *5 (𝐾3,3 ) =                  2
                                                                       =     .               (57)
                                                      36                 216
Finally,
                                  4               2 79    158
                                    HHI *5 (𝐾4 ) = ·    =     ,
                                  6               3 147   441
and
                                     158   77     19
                                         −    =       > 0.
                                     441 216    10584
Hence, the claimed lower bound fails when 𝑑 + 1 does not divide 𝑁 .




                                                    38
D       Technical proofs for the arbitrary-𝜔 hardness reduction
D.1     Proof of the tangent-padding lemma (Lemma 5)
Proof. We refer to the 𝑡 copies of 𝑅 as the padding gadgets. The role of these gadgets is to make
the nonlinear HHI objective behave, on the core graph 𝐻, like the linear objective

                                           𝑆𝐻 − 𝜆𝑃𝐻 .

Since 𝑅 is fixed, it has only finitely many possible pairs (𝑃𝑅 , 𝑆𝑅 ). By the strictness assumption
in (34), there exists a constant 𝛿 > 0, depending only on 𝑅, such that every non-distinguished
configuration of 𝑅 satisfies
                                 (𝑆0 − 𝜆𝑃0 ) − (𝑆𝑅 − 𝜆𝑃𝑅 ) ≥ 𝛿.                                (58)

We prove the two statements separately.

Step 1: every padding gadget is distinguished. Fix an arbitrary configuration of the
core 𝐻, and denote its total points and sum of squared scores by 𝑃𝐻 and 𝑆𝐻 . Suppose that the
𝑡 padding gadgets together have total points and sum of squared scores

                                        𝑃pad     and     𝑆pad .

Write
                               𝑃pad = 𝑡𝑃0 + 𝑥,         𝑆pad = 𝑡𝑆0 + 𝑦.

Thus, 𝑥 and 𝑦 measure the change from using the distinguished configuration on every padding
gadget. Let 𝑏 be the number of padding gadgets that are not distinguished. Summing (58) over
the 𝑡 copies gives
                               𝑒 := 𝑡(𝑆0 − 𝜆𝑃0 ) − (𝑆pad − 𝜆𝑃pad )
                                 = 𝜆𝑥 − 𝑦 ≥ 𝑏𝛿.
Equivalently,
                                     𝑦 = 𝜆𝑥 − 𝑒,          𝑒 ≥ 𝑏𝛿.                              (59)

Because 𝑅 is fixed, there is also a constant 𝐶 > 0 such that changing one padding gadget from
its distinguished configuration changes its number of points by at most 𝐶. Therefore,

                                              |𝑥| ≤ 𝐶𝑏.                                        (60)

We compare the given configuration with the configuration having the same core configuration
but using the distinguished configuration on all 𝑡 padding gadgets. Their HHI values are,
respectively,
                             𝑡𝑆0 + 𝑦 + 𝑆𝐻                       𝑡𝑆0 + 𝑆𝐻
                                                   and                     .
                           (𝑡𝑃0 + 𝑥 + 𝑃𝐻 )2                   (𝑡𝑃0 + 𝑃𝐻 )2
Put
                                         𝐴 := 𝑡𝑃0 + 𝑃𝐻 .



                                                 39
After cross-multiplication, the distinguished padding is better exactly when

                        𝐷 := (𝑡𝑆0 + 𝑆𝐻 )(𝐴 + 𝑥)2 − (𝑡𝑆0 + 𝑦 + 𝑆𝐻 )𝐴2 > 0.

Expanding the first square gives

                               𝐷 = (𝑡𝑆0 + 𝑆𝐻 )(2𝐴𝑥 + 𝑥2 ) − 𝑦𝐴2 .

Using (59), we obtain

                        𝐷 = (𝑡𝑆0 + 𝑆𝐻 )(2𝐴𝑥 + 𝑥2 ) − (𝜆𝑥 − 𝑒)𝐴2
                          = 𝑒𝐴2 + 𝑥𝐴 2(𝑡𝑆0 + 𝑆𝐻 ) − 𝜆𝐴 + 𝑥2 (𝑡𝑆0 + 𝑆𝐻 ).
                                       (︀                       )︀


The definition 𝜆 = 2𝑆0 /𝑃0 implies
                                            2𝑡𝑆0 − 𝜆𝑡𝑃0 = 0.

Consequently,
                                2(𝑡𝑆0 + 𝑆𝐻 ) − 𝜆𝐴 = 2𝑆𝐻 − 𝜆𝑃𝐻 ,

and therefore
                           𝐷 = 𝑒𝐴2 + 𝑥𝐴(2𝑆𝐻 − 𝜆𝑃𝐻 ) + 𝑥2 (𝑡𝑆0 + 𝑆𝐻 ).                          (61)

The last term in (61) is nonnegative. Using 𝑒 ≥ 𝑏𝛿 and |𝑥| ≤ 𝐶𝑏, we get

                                 𝐷 ≥ 𝑏𝛿𝐴2 − 𝐶𝑏𝐴 |2𝑆𝐻 − 𝜆𝑃𝐻 |
                                     = 𝑏𝐴 (𝛿𝐴 − 𝐶|2𝑆𝐻 − 𝜆𝑃𝐻 |) .

The quantities 𝑃𝐻 and 𝑆𝐻 are polynomially bounded in |𝑉 (𝐻)|. Hence, by choosing 𝑡 polynomi-
ally large, we can guarantee

                                   𝛿(𝑡𝑃0 + 𝑃𝐻 ) > 𝐶|2𝑆𝐻 − 𝜆𝑃𝐻 |

for every possible configuration of 𝐻. It follows that 𝐷 > 0 whenever 𝑏 ≥ 1. Thus, if even
one padding gadget is non-distinguished, replacing all padding gadgets by distinguished ones
strictly increases the HHI while leaving the core unchanged. Therefore, every HHI -maximising
configuration uses (𝑃0 , 𝑆0 ) on every padding gadget.

Step 2: ordering the core configurations.                 Assume now that all 𝑡 padding gadgets are
distinguished. A core configuration with values (𝑃𝑖 , 𝑆𝑖 ) gives the padded HHI

                                                          𝑡𝑆0 + 𝑆𝑖
                                     𝐹𝑡 (𝑃𝑖 , 𝑆𝑖 ) :=                .
                                                        (𝑡𝑃0 + 𝑃𝑖 )2

Consider two core configurations with values (𝑃1 , 𝑆1 ) and (𝑃2 , 𝑆2 ). Since all denominators are
positive,
                                      𝐹𝑡 (𝑃1 , 𝑆1 ) > 𝐹𝑡 (𝑃2 , 𝑆2 )



                                                   40
is equivalent to

                   𝑁𝑡 := (𝑡𝑆0 + 𝑆1 )(𝑡𝑃0 + 𝑃2 )2 − (𝑡𝑆0 + 𝑆2 )(𝑡𝑃0 + 𝑃1 )2 > 0.                (62)

Expanding (62) according to the powers of 𝑡 gives

                          𝑁𝑡 = 𝑡2 𝑃02 [(𝑆1 − 𝜆𝑃1 ) − (𝑆2 − 𝜆𝑃2 )]
                                    [︁                                       ]︁
                                + 𝑡 𝑆0 (𝑃22 − 𝑃12 ) + 2𝑃0 (𝑆1 𝑃2 − 𝑆2 𝑃1 )
                                   (︁                   )︁
                                + 𝑆1 𝑃22 − 𝑆2 𝑃12 .                                            (63)

The coefficient of 𝑡2 is positive precisely when

                                          𝑆1 − 𝜆𝑃1 > 𝑆2 − 𝜆𝑃2 .

All remaining terms in (63) grow at most linearly with 𝑡. Therefore, whenever the above strict
inequality holds, the positive quadratic term dominates for all sufficiently large 𝑡, and hence

                                         𝐹𝑡 (𝑃1 , 𝑆1 ) > 𝐹𝑡 (𝑃2 , 𝑆2 ).

It remains to verify that one polynomially bounded value of 𝑡 works for every pair of core
configurations. Since
                                                        2𝑆0
                                                  𝜆=
                                                        𝑃0
and 𝑃0 , 𝑆0 are fixed integers, every value 𝑆𝐻 − 𝜆𝑃𝐻 is a rational number whose denominator
divides 𝑃0 . Therefore, two distinct such values differ by at least 1/𝑃0 . In particular, whenever
the coefficient of 𝑡2 in (63) is nonzero, its absolute value is at least 𝑃0 . On the other hand, all
quantities 𝑃𝑖 and 𝑆𝑖 are polynomially bounded in |𝑉 (𝐻)|. Hence, the coefficients of 𝑡 and 𝑡0 in
(63) are also polynomially bounded. A polynomially large value of 𝑡 consequently makes the
quadratic term dominate simultaneously for every pair of core configurations. This proves both
statements.

D.2    Proof of the amplified-gap lemma (Lemma 6)
Proof. Apply the construction in Theorem 4 to the conjunction of 𝐿 variable-disjoint renamed
copies of 𝜙, where 𝐿 is a sufficiently large constant depending only on 𝐴 and 𝜔. Let 𝑁 denote
the number of vertices in the resulting unpadded core, and let (𝑃0 , 𝑆0 ) be the distinguished pair
of the corresponding padding graph from the table above. Put

                                                        2𝑆0
                                                 𝜆 :=       .
                                                        𝑃0

For one copy of the formula, let Δ𝜔 > 0 denote the strict gap in the relevant core potential: we
may take Δ3 = 9 and Δ𝜔 = 1 for 𝜔 ≥ 4. By (20), a canonical YES-core configuration (𝑃1 , 𝑆1 )
and any NO-core configuration (𝑃2 , 𝑆2 ) therefore satisfy

                                (𝑆1 − 𝜆𝑃1 ) − (𝑆2 − 𝜆𝑃2 ) ≥ 𝐿Δ𝜔 .

                                                      41
    Add 𝑡 copies of the padding graph. The difference between the HHI of the padded YES-
configuration and that of the padded NO-configuration is

                                                      𝐷𝑡
                                                                     ,
                                           (𝑡𝑃0 + 𝑃1 )2 (𝑡𝑃0 + 𝑃2 )2

where

                           𝐷𝑡 = 𝑡2 𝑃02 [(𝑆1 − 𝜆𝑃1 ) − (𝑆2 − 𝜆𝑃2 )]
                                      [︁                                       ]︁
                                  + 𝑡 𝑆0 (𝑃22 − 𝑃12 ) + 2𝑃0 (𝑆1 𝑃2 − 𝑆2 𝑃1 )
                                  + 𝑆1 𝑃22 − 𝑆2 𝑃12 .

Since the core is cubic and 𝜔 is fixed, 𝑃𝑖 , 𝑆𝑖 = 𝑂𝜔 (𝑁 ). Hence, the last two lines have absolute
value 𝑂𝜔 (𝑡𝑁 2 + 𝑁 3 ), while the first line is at least

                                                  𝐿Δ𝜔 𝑃02 𝑡2 .

Choose 𝑡 = 𝐾𝜔 𝑁 2 , where 𝐾𝜔 is sufficiently large that Lemma 5 applies and the leading term
dominates the remaining terms. Then

                                                 𝐷𝑡 ≥ 𝐶𝜔 𝐿𝑡2

for some constant 𝐶𝜔 > 0 independent of 𝐿 and of the input formula. Moreover, 𝑡𝑃0 +𝑃𝑖 = Θ𝜔 (𝑡),
so the HHI gap is at least
                                                     𝐶𝜔′ 𝐿
                                                           .
                                                      𝑡2
The total number of vertices in the padded graph is 𝑛 = Θ𝜔 (𝑡); therefore, the gap is at least

                                                     𝐶𝜔′′ 𝐿
                                                      𝑛2

for a constant 𝐶𝜔′′ > 0.
    Let 𝜏 be the HHI of the padded canonical YES-configuration. The estimate holds uni-
formly against every NO-core configuration, and Lemma 5 ensures that an optimum uses the
distinguished configuration on every padding copy. Thus every NO-instance has optimum at
most
                                                       𝐶𝜔′′ 𝐿
                                                  𝜏−          .
                                                        𝑛2
Choosing 𝐿 so that 𝐶𝜔′′ 𝐿 ≥ 𝐴 proves the claim. Since 𝐿 is a constant independent of the input
formula, the reduction remains polynomial.




                                                       42
E     Maximum HHI under the (3,2,1,0) scoring system
Draws are followed by penalty shootouts in some incomplete round-robin competitions, such as
the Champions Hockey League (Section 2) or the Leagues Cup (Section 3.1), with the following
scoring system: three points for a regular win, two points for a shootout win, one point for a
shootout loss, and zero points for a regular loss. Consequently, the total number of points is
three times the number of matches. Maximising HHI under this scoring system is equivalent to
the (2, 1, 0) case, which we have investigated thoroughly in Section 4.2.

Proposition 2. For every graph 𝐺 with at least one edge,

                                    HHI *(3,2,1,0) (𝐺) = HHI *2 (𝐺).

Moreover, every configuration maximising HHI under the (3, 2, 1, 0) scoring system contains
only regular wins and losses.

Proof. Every match awards exactly three points, regardless of its outcome. Hence, the total
number of points is fixed at 3|𝐸(𝐺)|, and maximising HHI is equivalent to maximising the sum
of squared scores.
    Consider a match between two teams whose scores from their other matches are 𝑎 and 𝑏. If
the first team receives 𝑥 points, the sum of their squared scores is

                                  𝑔(𝑥) = (𝑎 + 𝑥)2 + (𝑏 + 3 − 𝑥)2 .

Since 𝑔 is strictly convex, for 𝑥 ∈ {1, 2} we have 𝑔(𝑥) < max{𝑔(0), 𝑔(3)}. Therefore, replacing
any shootout result by a regular victory strictly increases HHI . Consequently, every optimal
configuration contains only regular wins and losses.
    Let 𝑤𝑣 denote the number of wins of team 𝑣. Its score is then 3𝑤𝑣 , and thus
                                                 ∑︀         2       ∑︀      2
                                                  𝑣∈𝑉 (3𝑤𝑣 )           𝑣∈𝑉 𝑤𝑣
                      HHI *(3,2,1,0) (𝐺) = max                = max           ,
                                            Φ    (3|𝐸(𝐺)|)2      Φ   |𝐸(𝐺)|2

where Φ ranges over all orientations of 𝐺. The last expression is precisely HHI *2 (𝐺), since an
optimum under the (2, 1, 0) scoring system also contains no draws.

    Hence, all extremal characterisations and computational hardness results established for the
(2, 1, 0) scoring system extend directly to the (3, 2, 1, 0) scoring system.




                                                      43
