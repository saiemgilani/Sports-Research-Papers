<!-- source: library/preprints/arXiv/2026/2026 - A Resource Allocation Tournament - Nathaniel et al.pdf -->
<!-- item: https://arxiv.org/abs/2610.31418 -->
<!-- authors: Adam Nathaniel, Refael Hassin -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-12; equations, tables and figures are NOT preserved - consult the PDF for those -->

# A Resource Allocation Tournament

                                                         A Resource Allocation Tournament∗
                                                                 Adam Nathaniel† and Refael Hassin‡
arXiv:2610.31418v1 [math.OC] 22 Oct 2026




                                                                                      2026


                                                                                   Abstract
                                                      We introduce and analyze a round-robin simultaneous resource alloca-
                                                  tion contest, motivated by sports leagues and other competitive environ-
                                                  ments where agents must distribute limited resources across multiple en-
                                                  counters. Players allocate resources in advance to matches against all op-
                                                  ponents, and match outcomes are determined by relative allocations. We
                                                  study two payoff schemes: total points, where players accumulate rewards
                                                  for each win, and winner-takes-all, where only the tournament winner is
                                                  rewarded. For three players, we provide complete equilibrium characteri-
                                                  zations under both schemes. For four or more players, we show that the
                                                  total points payoff admits Blotto-type equilibria, while the winner-takes-
                                                  all payoff requires numerical and algorithmic analysis. To address this, we
                                                  develop a best-response dynamics algorithm with stochastic inertia and
                                                  use it to approximate equilibria in games with four and five players.
                                           Keywords: Game Theory, Contest Theory, Sports Analytics, Colonel Blotto
                                           Game, Best Response Dynamics.


                                           1      Introduction
                                           We define and analyze a game motivated by sports leagues. We model a round-
                                           robin tournament as a contest in which teams compete for a prize by distributing
                                           costly resources, such as energy, across matches. The analysis examines how
                                           teams should optimally allocate their resources throughout the course of the
                                           competition.
                                               The scope of resource allocation competitions goes far beyond sports. Similar
                                           strategic problems arise in economics, where firms must decide how to allocate
                                           limited budgets across research and development projects or advertising cam-
                                           paigns. In political science, election campaigns can be viewed as contests in
                                           which parties distribute their resources over time to maximize electoral success.
                                               ∗ This work was supported by the Israel Science Foundation [Grant 2718/25].
                                             † Department of Statistics and Operations Research, School of Mathematical Sciences, Tel

                                           Aviv University. e-mail: adamnathaniel6@gmail.com.
                                             ‡ Department of Statistics and Operations Research, School of Mathematical Sciences, Tel

                                           Aviv University. e-mail: hassin@tauex.tau.ac.il.



                                                                                        1
Analogous dynamics also appear in international relations, for instance, in arms
races, where countries repeatedly allocate effort to maintain or gain advantage.
Thus, while sports provide natural and intuitive motivation, the underlying
allocation problem is relevant in a wide range of settings.
    In multi-stage contests, the resource allocation can be done either simul-
taneously, where players commit to their allocations for all stages in advance
without knowing the outcomes of earlier stages, or sequentially, where alloca-
tions are chosen stage by stage, with players observing the outcomes of previous
stages before making subsequent decisions. Although sequential contests are
more common, simultaneous resource allocation problems have many real-life
applications. In what follows, we discuss several such applications, before pre-
senting our simultaneous resource allocation framework.
    In sports, a clear example arises in pre-season planning, where teams de-
sign training-load or effort-allocation programs for the entire season in advance,
committing ex ante to a distribution of resources across competitions or time
periods, with only limited ability to adjust once the season begins. Similarly,
roster construction and budget allocation across positions before the season be-
gins can be viewed as a simultaneous resource allocation problem, since most
decisions are made prior to observing match outcomes.
    Simultaneous auctions have also been intensively studied. The literature in-
cludes theoretical analysis of equilibrium behavior and social welfare properties
in simultaneous auctions (Krishna and Rosenthal, 1996; Feldman et al., 2013),
as well as comparisons between simultaneous and sequential auctions from the
perspective of the auction designer (Hausch, 1986). In parallel, a substantial
body of work is devoted to the design and implementation of simultaneous
auctions for spectrum allocation (McAfee and McMillan, 1996; Milgrom, 2000;
Cramton, 2013). Algorithmic approaches to bidding in simultaneous auctions
have also been studied (Greenwald and Boyan, 2001).
    In contrast to our framework, in these auction settings, only winning bidders
incur payments, whereas unsuccessful bidders do not bear any cost. A notable
exception is the waiting-line auction (Holt and Sherman, 1982), which studies
the allocation of commodities on a first-come, first-served basis. Consumers
compete along a non-price dimension, time, closely resembling the non-price
dimension of effort in our framework.
    A sports-related simultaneous auction can be seen in the 2026 FIFA World
Cup ticketing process, where fans enter a simultaneous ballot, submitting bind-
ing purchase requests for all matches in which they are interested. While such
load management allocation problems can also be addressed through sequential
mechanisms in cyclic queueing games (Hassin and Nathaniel, 2021), the choice
of a simultaneous ballot introduces unique strategic complexities. Specifically,
fans may fear winning too many tickets, i.e., obtaining more tickets than they
can afford or wish to purchase, which may lead them to bid conservatively. A
closely related concern appears in McAfee and McMillan (1996), which shows
that in simultaneous auctions, budget-constrained bidders strategically shade
their bids due to the risk of winning more items than desired. Although our
model also incorporates a budget constraint, the fact that all players incur costs


                                        2
regardless of winning eliminates incentives to limit the number of wins.
    Additional simultaneous mechanisms in which players incur costs regard-
less of the outcome include rent seeking activities (Tullock, 1980; Congleton
et al., 2008; Fonseca, 2009). In the efficient rent seeking model, simultaneity
is imposed under the presumption that all players have an incentive to act as
first movers. Early work (Krueger, 1974) emphasizes the competitive nature of
rent seeking, demonstrating that the associated welfare losses may substantially
exceed those generated by traditional trade restrictions. Subsequent research
(Baye and Hoppe, 2003; Ahn et al., 2010) highlights the strategic equivalence
between rent seeking contests and tournament-style games, such as innovation
tournaments in which only the best entrepreneur can go to the market. Al-
though the literature predominantly adopts a simultaneous-move framework,
Glazer and Hassin (2000) study sequential rent seeking and show that early
movers do not necessarily earn higher profits and that aggregate profits may be
lower than under simultaneity.
    Another area close to simultaneous resource allocation contests is the course
bidding mechanism, where students use virtual points to bid for limited seats
in popular courses. Krishna et al. (2004) report a field experiment at the
University of Michigan Business School, comparing different course allocation
systems. Krishna and Unver (2008) complement this with laboratory evidence in
controlled settings. Sonmez and Unver (2010) highlight the conceptual problem
that bids used both for preference revelation and priority allocation can distort
outcomes. More recently, Juthamanee et al. (2021) and Laokondee et al. (2021)
applied deep learning models to optimize course allocation.
    Together, these applications illustrate the practical relevance of strategic re-
source allocation in simultaneous strategic interactions. Rent seeking activities
resemble our framework in settings where agents optimize tournament rank,
while course bidding mechanism resembles the setting where agents optimize
individual outcomes.
    At a formal level, such problems are naturally studied within the broader
framework of contest theory, to which we now turn.
    Contest theory (Glazer and Hassin, 1988; Moldovanu and Sela, 2001) is
a branch of game theory that studies situations where players expend costly
resources (effort, money, time, etc.) to compete for a prize. As in auctions, the
outcomes are determined by relative bids or efforts. The key difference from
auctions is that, in contests, all participants bear the cost of their actions, even
if they do not win the prize.
    Contests may differ in various aspects, such as the tournament format and
the mechanism used to determine match outcomes. In particular, in standard
profit-maximization contests, players aim to maximize their profit, typically de-
fined as the expected reward minus their chosen cost. In contrast, in resource
allocation contests, players are constrained to spend their entire resources (or
cost), and thus aim only to maximize their expected reward through the op-
timal allocation of that fixed budget. This distinction is especially relevant
in sports economics, where professional soccer clubs have been shown to fol-
low win-maximization strategies subject to budget constraints rather than pure


                                         3
profit-maximization (Garcia-del-Barrio and Szymanski, 2009).
    To the best of our knowledge, our model, formally presented in the next
section, has not previously been studied. In what follows, we review related
work.
    Resource allocation design has been studied in two-player contests with the
Tullock mechanism (Tullock, 1980), where if Player i allocates xi resources
in a match, their probability of winning the match is x1x+x   i
                                                                2
                                                                  . Sela and Erez
(2013) analyze contests in which the two players compete against each other in
n different stages, having winning values for each stage. Sela (2023) analyzes
the best-of-two and best-of-three tournaments, where only the winner of the
tournament receives a prize.
    The Colonel Blotto game (Borel, 1921) can be seen as a variation of the two-
player resource allocation contest with the all-pay mechanism, where if Player i
allocates xi resources in a match, they win the match against Player j if xi > xj .
The two players compete against each other in n simultaneous matches on n
battlefields, and their reward is equal to the total number of matches they win.
In its multiplayer version (Boix-Adsera et al., 2020), k players allocate resources
over n battlefields, where each player decides the amount of resources to allocate
to each battlefield.
    Round-robin tournaments with more than two players, where players do
not have resource budgets as in our model, have also been studied. Krumer
et al. (2017) analyze round-robin tournaments with three and four symmetric
players, where the matches are all-pay contests, and only the winner of the
tournament receives a prize. The matches are played sequentially, and it is
shown that asymmetry in the order of the matches leads to asymmetry in the
winning probability of the tournament among the players. Dagaev and Zubanov
(2022) consider a round-robin sequential resource allocation tournament with
three players and compare different distributions of prizes, some of them leading
to equal payoffs in equilibrium.
    In addition to theoretical work, Avrahami et al. (2013) conducted an exper-
imental study of resource allocation in a two-player contest over many fields,
comparing behavior in symmetric and asymmetric setups. They show that
weaker players often abandon some fields to focus resources and maintain a
chance of occasionally winning.
    In contrast to the models surveyed above, we consider a multiplayer round-
robin resource allocation tournament with simultaneous all-pay matches.
    The remainder of this paper is organized as follows. Section 2 presents
our model and suggests two payoff schemes: total points and winner-takes-all.
Sections 3-6 analyze each payoff scheme, first in the three-player game and then
in the game with four or more players. Section 7 concludes the paper.


2    Model
We consider a symmetric game with n players. The players compete in a round-
robin tournament, facing each of the other n − 1 players exactly once. Hence,


                                        4
each player participates in n − 1 matches.
    Each player is endowed with a total of one unit of resources to be allocated
across their matches. Formally, a strategy is an allocation vector (x1 , . . . , xn−1 )
      Pn−1
with i=1 xi = 1, where xi denotes the resources assigned to the i-th match.
    Players choose their allocation strategy simultaneously and in advance, with-
out knowing the identity of their opponents in each match or the order in which
the matches occur. In particular, since all strategies are determined before the
competition begins, players cannot observe the outcomes of any matches.
    The outcome of a match is determined by the relative resource allocations:
the player who allocates more resources wins the match and receives 1 point;
if both allocate the same amount, the match ends in a draw and each player
receives 0.5 point.
    The payoffs of the players in the tournament are based on their points. We
consider two payoff schemes:

    • Total points payoff : The payoff for each player equals the number of
      points accumulated throughout the tournament.
    • Winner-takes-all payoff : A reward of one unit is shared equally among
      all players with the highest total of points at the end of the tournament.

    Since the tournament schedule is random, we evaluate the expected payoffs
in all possible permutations of opponents and match orders. Thus, in the total
points payoff scheme we calculate each player’s expected total points, and in
the winner-takes-all payoff scheme we calculate the winning probability of each
player.
    We look for a symmetric Nash equilibrium strategy. Because the two-player
case is trivial, we begin with the three-player game for each payoff scheme.


3     Total points payoff: three players
In this section, we consider a three-player game in which each player faces the
other two exactly once and allocates their resources between the two matches.
The players aim to maximize their expected total number of points earned
throughout the tournament.
    Pure strategies are of the form (x, 1 − x). Since players must decide on their
allocation strategy without knowing the identity of their opponent in a given
match, we may, without loss of generality, restrict attention to x ∈ 12 , 1 to
                                                                              

avoid duplication of strategies.
Theorem    1. Any resource allocation strategy of the form (x, 1 − x), where
x ∈ 21 , 1 , is a symmetric equilibrium.
    

Proof. Denote my strategy by (y, 1 − y), where y ∈ 12 , 1 , and
                                                             
                                                                   1 denote
                                                                             the
strategy of each of the other two players by (x, 1 − x), where x ∈ 2 , 1 . Let P0
be my expected payoff and P1 be the expected payoff of each of the other two
players.


                                          5
    A total of three matches take place and, therefore, the sum of the players’
payoffs satisfies P0 +2P1 = 3. In a symmetric equilibrium, we have P0 = P1 = 1.
    We show that any response strategy (y, 1 − y) yields the same payoff P0 = 1
and therefore it is also a best response.
    In the case where x = y, it is straightforward that P0 = P1 = 1.
    A strategy with y < x satisfies x > y ≥ 1 − y > 1 − x, and I win the match
to which I allocate y units with probability 12 , since I win against 1 − x, lose
against x and encounter each of them with equal probability.
    Independently, as I play against a different player, I also win the match to
which I allocate 1 − y units with probability 21 , by the same reasoning: I win
against 1 − x, lose against x, and face each of them with equal probability.
    Similarly, strategy y > x satisfies y > x ≥ 1 − x > 1 − y, and I win the match
to which I allocate y units with probability 1, and I win the match to which I
allocate 1 − y units with probability 0.
    In conclusion, in the case y < x, my expected payoff is P0 = 21 + 21 = 1, and
in the case y > x, my expected payoff is P0 = 1 + 0 = 1 as well.
    Therefore, my strategy (y, 1 − y) is always a best response against (x, 1 − x).
Specifically, the strategy with y = x is a best response, and therefore (x, 1 − x)
is a symmetric equilibrium.
Remark 2. More generally, not only does any pure strategy constitute a sym-
metric equilibrium, but any profile of pure strategies constitutes an equilibrium,
and therefore any mixed strategy constitutes a symmetric equilibrium.

Proof. We have already shown that, in the case that two players play the same
pure strategy and one player plays a different pure strategy, the payoffs of all
players are equal. In the case of three players playing three different pure
strategies, there are eight equally likely configurations corresponding to each
player randomly allocating their resources between the two opponents. By a
calculation analogous to that in the proof of Theorem 1, it can be shown that
the payoffs of all players are equal in this case as well.


4    Total points payoff: four or more players
In this section, we consider a game with four or more players. The players
aim to maximize their expected total number of points earned throughout the
tournament.
    We begin the section with an analysis of the four-player game in which each
player faces the other three exactly once and allocates their resources over the
three matches.
    Pure strategies are of the form (x1 , x2 , x3 ), where x1 + x2 + x3 = 1. Since
players must decide on their allocation strategy without knowing the identity
of their opponent in a given match, we may, without loss of generality, restrict
attention to strategies satisfying x1 ≥ x2 ≥ x3 to avoid duplication.




                                        6
    Unlike the three-player variation, in the case of four players, not every strat-
egy of the form (x1 , x2 , x3 ) constitutes a symmetric equilibrium. In fact, none
of them does, and the game admits no pure symmetric equilibrium.
Lemma 3. In the four-player game, there does not exist a pure symmetric
equilibrium.

Proof. Let (x1 , x2 , x3 ) be the strategy played by each of the other three players,
where x1 ≥ x2 ≥ x3 and x1 + x2 + x3 = 1. Then, for sufficiently small ϵ > 0,
the strategy (x1 − 2ϵ, x2 + ϵ, x3 + ϵ) yields a strictly higher expected payoff for
me than the strategy (x1 , x2 , x3 ).
     Consider the case x1 > x2 > x3 . Let ϵ = 41 min(x1 − x2 , x2 − x3 ). Then the
following inequalities hold: x1 > x1 − 2ϵ > x2 + ϵ > x2 > x3 + ϵ > x3 .
     Denote my expected payoff by P0 , and denote the expected payoff of each
of the other three players by P1 . A total of six matches are played, so the sum
of all payoffs satisfies P0 + 3P1 = 6. Clearly, under my strategy (x1 , x2 , x3 ) we
have P0 = P1 = 1 12 .
     Now consider my strategy (x1 − 2ϵ, x2 + ϵ, x3 + ϵ). I win the match to
which I allocate x1 − 2ϵ, x2 + ϵ and x3 + ϵ units with probabilities 23 , 23 and 13 ,
respectively/
     Therefore, my expected payoff under this strategy is P0 = 32 + 23 + 13 = 1 32 >
  1
1 2 , as claimed.
     Similar arguments apply in the cases where x1 = x2 , x2 = x 3 , or x1 = x2 =
x3 = 13 . Against the strategy (x, x, 1 − 2x), where x ∈ 31 , 12 , I can respond
with (x + ϵ, x − 2ϵ, 1 − 2x + ϵ),and receive a payoff of 1 32 . Against the strategy
(1 − 2x, x, x), where x ∈ 0, 13 , I can respond with (1 − 2x − 2ϵ, x + ϵ, x + ϵ),
and receive a payoff of 2. Finally, against ( 31 , 13 , 31 ), I can respond, for example,
with ( 12 , 12 , 0), and receive a payoff of 2.


    The essence of the proof is that it is profitable to be better than the oppo-
nents in two out of the three coordinates and worse in the third coordinate. The
following example shows how the better response dynamics described above can
lead to cyclical behavior.
Example 4. Suppose that the other three players play (0.34, 0.33, 0.33). This is
not an equilibrium, as for me a better response is, for example, (0.43, 0.43, 0.14).
If they adopt this new strategy, my response becomes (0.53, 0.24, 0.23). They may
continue to follow, allowing me, in turn, to return to (0.34, 0.33, 0.33) and gain
an advantage once again.
   Therefore, we seek a mixed equilibrium strategy. Specifically, we define a
property, construct a distribution that satisfies this property, and prove that
the property constitutes a sufficient condition for equilibrium.
Definition 5. For a game with n+1-players, a mixed strategy (X1 , X2 , . . . , Xn )
is called Blotto if its joint probability distribution satisfies the following condi-
tions:


                                           7
        n
        X
   1.         Xi = 1,
        i=1

                    distribution is uniform on the interval 0, n2 ; that is, Xi ∼
                                                                
   2. Each
        2marginal
            
      U 0, n for all i ∈ {1, . . . , n}.
   A Blotto strategy was first presented by Borel and Ville (1938). In our
setup, this corresponds to an n + 1-player game, whereas the paper analyzes the
Colonel Blotto game, involves two players competing over n battlefields.
   Roberson (2006) and Weinstein (2012) provide an elegant construction of the
case n = 3. Consider a trivariate distribution that places a uniform probability
mass 12 on each of the following two line segments: from (0, 23 , 13 ) to ( 23 , 13 , 0),
and from (0, 13 , 32 ) to ( 23 , 0, 13 ). This defines a Blotto strategy for the case n = 3.
Weinstein (2012) further generalizes the construction to arbitrary n.
Theorem 6. For an n + 1-player game, any Blotto strategy constitutes a mixed
symmetric equilibrium.
Proof. Assume that the other n players use a common mixed Blotto strategy
and that I play the pure strategy (x1 , x2 , . . . , xn ), where x1 ≥ x2 ≥ · · · ≥ xn
and x1 + x2 + . . . + xn = 1. We will show that this strategy is a best response
if and only if x1 ≤ n2 .
    By the definition of a Blotto strategy, in each of my n matches, my oppo-
nent randomizes their allocation according to the uniform distribution over the
interval [0, n2 ]. Therefore, my expected payoff is
                                  n
                                  X
                           P0 =         Pr(Yi < xi | Yi ∼ U[0, n2 ]).
                                  i=1

   For any 0 ≤ x ≤ 1 and Y ∼ U[0, n2 ], we have:
                                 
                                  n x if 0 ≤ x ≤ 2 ,
                                      2                n
                     Pr(Y < x) =
                                 1        if n2 < x ≤ 1.

   Therefore, if x1 ≤ n2 , my expected payoff is
                           n     n            n      n
                             x1 + x2 + . . . + xn = ,
                           P0 =
                           2     2            2      2
               2
   and if xk > n ≥ xk+1 , then my expected payoff is
                         n                       n                          n
                P0 = k +   (xk+1 + . . . + xn ) < (x1 + . . . + xn ) = .
                         2                       2                          2
     Therefore, we conclude that a pure strategy (x1 , x2 , . . . , xn ) is a best response
if and only if x1 ≤ n2 . As a result, any mixed strategy that randomizes between
pure strategies, all of which have x1 ≤ n2 , is also a best response.
    The marginal distributions of the variables in the Blotto strategy are all
U 0, n2 , ensuring that no individual value exceeds n2 . Therefore, any Blotto
strategy constitutes a best response to itself, and thus forms an equilibrium.


                                                8
Remark 7. More generally, any strategy profile in which each player selects
a Blotto strategy (not necessarily identical for all players) constitutes a mixed
equilibrium.


5    Winner-takes-all payoff: three players
In this section, we consider a three-player game in which each player faces
each of the other two exactly once and allocates their resources between the two
matches. The players aim to maximize their chances of winning the tournament.
    Pure strategies are of the form (x, 1 − x). Since players must decide on their
allocation strategy without knowing the identity of their opponent        in a given
match, without loss of generality, we restrict attention to x ∈ 12 , 1 to avoid
                                                                      

duplication of strategies.
    Unlike the variation that maximizes expected points, in the case of maxi-
mizing the probability of winning, not every pure strategy of the form (x, 1 − x)
constitutes a symmetric equilibrium. In this section, we fully characterize the
payoff function, representing the player’s chance of finishing first, and prove that
the strategy ( 12 , 12 ) is the unique symmetric equilibrium.
Lemma 8. Assume that the three players play pure strategies (x, 1 − x), (y, 1 −
y), and (z, 1 − z). Without loss of generality, suppose that x ≥ y ≥ z ≥ 21 . The
payoffs of the players, which we denote as Px , Py , and Pz , satisfy Px +Py +Pz =
1 and are given in Table 1.


                           case           Px      Py       Pz
                        x>y>z            1/6     5/12     5/12
                        x=y>z            7/24    7/24     5/12
                     x > y = z > 1/2     1/12    11/24   11/24
                     x > y = z = 1/2         0    1/2     1/2
                        x=y=z            1/3      1/3     1/3


                   Table 1: Payoffs in the three-player game.


Proof. In each of the five cases, there are eight equally likely configurations
corresponding to each player randomly allocating their resources between the
two opponents. Specifically, Player 1 allocates x units of resources against Player
2 or against Player 3; Player 2 allocates y units of resources against Player 1 or
against Player 3; and Player 3 allocates z units of resources against Player 1 or
against Player 2.
   In each case-configuration combination, there are three matches, with deter-
ministic resource allocations and outcomes, leading to a deterministic payoff for


                                         9
each player. The expected payoff of a player in a given case is defined as the
average of their payoffs across all case-configuration combinations corresponding
to that case.
    For example, consider the case x > y > z and the configuration in which
Player 1 allocates x against Player 2, Player 2 allocates y against Player 1, and
Player 3 allocates z against Player 1.
    We have x > y > z ≥ 12 ≥ 1 − z > 1 − y > 1 − x. Therefore, Player
1 wins against Player 2, Player 3 wins against Player 1, and Player 3 wins
against Player 2. Consequently, in this case-configuration, Player 3 wins the
tournament, and the payoffs are Px = Py = 0 and Pz = 1.
    The other case-configuration combinations are analyzed similarly; the com-
plete analysis is provided in the appendix.
     Lemma 8 provides a complete characterization of the payoff function for pure
strategies. We can use it to find the unique symmetric equilibrium.
Theorem 9. The strategy 21 , 12 is the unique symmetric equilibrium.
                                      

                                               1 1
                                                    
Proof. First, we prove that the strategy       2 , 2 is an equilibrium. Assume that
the other two players play 12 , 12 , and that I play (x, 1 − x), where x ≥ 12 .
                                       

According to Lemma         8, if x = 12 my payoff is 13 and if x > 21 my payoff is 0.
                1 1
                    
Therefore, 2 , 2 is an equilibrium. We will prove that it is unique.
     Consider another strategy (X, 1 − X) of the other two players, where X is a
random variable over pure strategies and may be constant. We will prove that
(X, 1 − X) is not an equilibrium.
     If I play (X, 1 − X), my payoff is 13 . If I play 12 , 12 , my payoff is an
                                                                  

expectation of my payoffs over all realizations (x1 , 1 − x1 ) and (x2 , 1 − x2 ) of
the other two players, with x1 , x2 ≥ 12 .
     From Lemma 8, for any values of x1 and x2 , my profit from playing 12 , 12 ,
                                                                                    

denoted Pz in the lemma, is greater than or equal to 13 and is strictly greater
than 13 unless x1 = x2 = 12 .
     Since their strategy is not 12 , 12 , with positive probability we have x1 ̸= 12 .
                                         

Therefore,    with expectation over all realizations, my profit from the strategy
 1 1
       
   ,
 2 2     is strictly  greater than my profit from the strategy (X, 1 − X). Hence,
(X, 1−X) is not a best response against (X, 1−X), and thus not an equilibrium.


   Although mixed strategies such as (X, 1 − X), where X ∼ U [0, 1], may
appear as natural candidates for a symmetric equilibrium, we have shown that
none of them constitutes one. In addition, we provide a characterization of the
best responses to mixed strategies of this form.
Remark 10. Assume that the other two players allocate their resources inde-
pendently as (X, 1 − X), where X ∼ fX , a continuous density function over
[0, 1]. Assume that I choose my allocation deterministically as (y, 1 − y), where
y ∈ [ 12 , 1]. My payoff, denoted as P0 , is given by
                 1                                  1 − Pr(1 − y < X < y)
          P0 =     + ay (1 − ay )   where    ay =                         .
                 6                                            2

                                            10
My strategy (y, 1 − y) is a best response if and only if Pr(1 − y < X < y) = 0.
My strategy ( 12 , 12 ) is always a best response.
    The proof for Remark 10 is provided in the appendix.
Example 11. Assume that the other two players allocate their resources inde-
pendently as (X, 1 − X), where X ∼ U [0, 1]. Assume that I choose my allocation
deterministically as (y, 1 − y), where y ∈ [ 12 , 1]. My payoff, denoted as P0 , is
given by
                                     1
                               P0 = + y(1 − y).
                                     6
Since ay = 21 (1 − (y − (1 − y))) = 1 − y. My unique best response is ( 12 , 12 ).


6     Winner-takes-all payoff: four or more players
In this section, we consider a game with four or more players. The players aim
to maximize their chances of winning the tournament.
    We begin the section with an analysis of the four-player game in which each
player faces the other three exactly once and allocates their resources across the
three matches.
    Pure strategies are of the form (x1 , x2 , x3 ), where x1 + x2 + x3 = 1. Since
players must decide on their allocation strategy without knowing the identity of
their opponent in a given match, without loss of generality, we restrict attention
to strategies satisfying x1 ≥ x2 ≥ x3 to avoid duplication.
    An analytical solution for this variation may be challenging to derive, as
the payoff of one player also depends on the interactions among the other play-
ers, and the number of such interactions increases with the number of players.
Moreover, unlike the case with three players, the variation with four players has
no pure equilibrium.
    We solve this variation numerically. We present a geometric representation of
this game in Section 6.1 and its numerical discretization in Section 6.2. Then, we
prove that there is no pure equilibrium in Section 6.3 and discuss the analysis
of mixed strategies in Section 6.4. Finally, we use methods from algorithmic
game theory to find an ε-equilibrium in Section 6.5 and extend our solution to
the five-player game in Section 6.6.

6.1    Geometric representation
The possible strategies correspond to points satisfying the constraints x1 ≥ 0,
x2 ≥ 0, x3 ≥ 0, and x1 + x2 + x3 = 1, which define a two-dimensional triangle
bounded by the lines x1 = 0, x2 = 0, and 1 − x1 − x2 = 0. However, this triangle
contains strategies that are strategically equivalent. For example, the vertices
of this triangle are (1, 0), (0, 1), and (0, 0), corresponding to the equivalent
strategies (1, 0, 0), (0, 1, 0), and (0, 0, 1), respectively.
    To avoid redundant representations, we restrict attention to strategies sat-
isfying x1 ≥ x2 ≥ x3 . Under this restriction, the strategy space is the triangle


                                         11
defined by the lines x1 = x2 , x2 = 1 − x1 − x2 , and 1 − x1 − x2 = 0. The ver-
tices of this triangle are (1, 0), ( 12 , 12 ), and ( 13 , 31 ), corresponding to the strategies
(1, 0, 0), ( 12 , 12 , 0), and ( 13 , 13 , 13 ), respectively.
    In the following sections, we denote a general pure strategy by (x, y, z) in-
stead of (x1 , x2 , x3 ). The graphical representation of a pure strategy within the
triangle is shown in Figure 1.

                                    Triangle of Pure Strategies
    1.0
                     z=0
    0.8
           a



    0.6
                                                                                        x=y
                     y=z                                                                y=z
y




           c                                                                            z=0
    0.4
                                                  (a, b, c)



    0.2
           b

                     x=y
    0.0
                              a                           c                 b
               0.0         0.2             0.4                0.6        0.8             1.0
                                                      x

          Figure 1: The graphical representation of a pure strategy (a, b, c).



6.2       Numerical discretization
The infinite set of pure strategies in this game is defined as S = {(x, y, z) ∈ R3 :
x ≥ y ≥ z ≥ 0, x + y + z = 1}. To analyze the game numerically, we discretize
this strategy space.
    We define a two-dimensional grid with step size δ. The finite set of pure


                                                 12
strategies in the grid is

      Sδ = {(n1 δ, n2 δ) ∈ R2 : n1 δ ≥ n2 δ ≥ 1 − n1 δ − n2 δ ≥ 0, n1 , n2 ∈ Z}.

    The number of pure strategies in Sδ depends on δ and increases on the order
of δ12 . In the following sections, we analyze the grid with δ = 0.01, which
contains 884 pure strategies, and is shown in Figure 2.

                               Grid of Triangle of Pure Strategies
    1.0

                    z=0
    0.8



    0.6
                                                                           x=y
                                                                           y=z
                    y=z                                                    z=0
y




                                                                           Pure Strategies
    0.4



    0.2


                    x=y
    0.0
           0.0           0.2            0.4            0.6           0.8              1.0
                                                   x

                 Figure 2: The grid of pure strategies with δ = 0.01.


6.3       Pure strategies
As in the variation that maximizes expected total points, in the case of maxi-
mizing the winning probability, no pure strategy constitutes a symmetric equi-
librium. In particular, we claim that the specific example in Lemma 3 still
applies: let (x, y, z) denote the pure strategy adopted by each of the other three


                                              13
players. Then, the strategy (x − 2ϵ, y + ϵ, z + ϵ) yields a strictly higher expected
payoff for me than the strategy (x, y, z), which yields a payoff of 0.25.
    This claim can be proved analytically. However, since a player’s payoff in
this variation depends on the points earned by the other players, we would need
to consider up to 64 = 1296 possible cases (4 players, each with 3! = 6 equally
likely permutations of resource allocation). Although symmetry can reduce the
number of distinct cases, it may be easier - and equally exact - to perform a
complete enumeration using a simple computer program.
    The results for all common strategies (x, y, z) are shown in Table 2. In
each case, my payoff under a slightly modified strategy exceeds that of the
common strategy, demonstrating that no such strategy constitutes a symmetric
equilibrium.


          Their Strategy          My Strategy              My Payoff
         (x, y, z), x > y > z   (x − 2ϵ, y + ϵ, z + ϵ)   570/1296 = 0.440
            (x, x, y), x > y    (x + ϵ, x − 2ϵ, y + ϵ)   576/1296 = 0.444
            (x, y, y), x > y    (x − 2ϵ, y + ϵ, y + ϵ)   888/1296 = 0.685
            (1/3, 1/3, 1/3)         (1/2, 1/2, 0)        648/1296 = 0.500


                   Table 2: Strategies in the four-player game.

    Note that this result is independent of the numerical discretization and there-
fore remains valid in the original continuous setting.

6.4    Mixed strategies
We have shown that there is no pure symmetric equilibrium. Moreover, for any
pure strategy (x, y, z) played by the other three players, I have a response that
yields me a payoff of at least 0.440.
    In this section, we analyze mixed symmetric strategies. Given a mixed strat-
egy for the other three players, we compute my best response in the grid with
δ = 0.01. As a reminder, there is always a pure best response, and the grid con-
tains a finite number of pure strategies. In addition, a strategy constitutes an
equilibrium if and only if the best response against it yields a payoff of exactly
0.25.
    A mixed strategy on the P grid assigns probabilities 0 ≤ ps ≤ 1 to each pure
strategy s ∈ Sδ , such that s∈Sδ ps = 1. As noted in Section 6.2, for δ = 0.01 we
have |Sδ | = 884. Therefore, computing the best response requires evaluating 884
candidate pure strategies for me, each facing up to 8843 possible combinations
of pure strategies for the other three players.
    Due to computational constraints, an exact calculation is infeasible. Instead,
we employ a Monte Carlo approach in which, for each candidate response, we
simulate 10,000 realizations of the strategy combinations of the other players,


                                         14
sampled according to their mixed strategy, to approximate its expected payoff.
This yields estimates that are sufficiently stable for our purposes.
    Using this estimation procedure, we search for a mixed symmetric equilib-
rium.
    We test some natural candidates, motivated by the two-coordinate uniform
strategy (X, 1 − X) with X ∼ U [0, 1]. However, in analogy with the Bertrand
paradox (Bertrand, 1889), where the concept of a ”random chord” in a cir-
cle is not uniquely defined, the extension of the notion X ∼ U [0, 1] to three
coordinates lacks a unique interpretation.
Example 12. Consider the strategy that samples uniformly from the triangle
with vertices (1, 0, 0), (0, 1, 0), and (0, 0, 1). A similar strategy samples uni-
formly from the triangle with vertices (1, 0, 0), ( 12 , 21 , 0), and ( 13 , 13 , 13 ); in our
context, the two differ only on a set of measure zero. Its best-response payoff on
the grid is 0.362.
Example 13. Consider a Blotto strategy that assigns equal probability to the
two line segments from (0, 32 , 13 ) to ( 23 , 13 , 0) and from (0, 13 , 23 ) to ( 23 , 0, 13 ). Its
best-response payoff on the grid is 0.302.

            x       y       z
                                 that samples x, y, z ∼ U [0, 1] independently
Example 14. Consider the strategy
and plays x+y+z , x+y+z , x+y+z  . Its best-response payoff on the grid is 0.299.
    Although these strategies are closer to equilibrium than any pure strategy,
they are not sufficiently close. Consequently, a dedicated optimization algorithm
is required to identify an equilibrium strategy.

6.5     Algorithmic solution
We propose a variant of best-response dynamics (e.g., Roughgarden, 2016),
which we call approximate best-response dynamics with stochastic inertia. This
method combines elements from three established approaches: best-response
dynamics with inertia (e.g., Swenson et al., 2018), approximate best-response
dynamics (e.g., Bistritz and Leshem, 2017), and stochastic approximation (e.g.,
Lai, 2003).
    Best-response dynamics is an iterative procedure in which, at each step, a
player updates their strategy to the best response against the strategies played
in the previous round. Formally, if x(t) denotes the strategy profile at iteration
t, then the update rule is
                               x(t+1) = BR x(t) .
                                                

   In best-response dynamics with inertia, updates are smoothed through a
convex combination of the previous strategy and its best response:
              x(t+1) = (1 − α) x(t) + α BR x(t) ,
                                               
                                                     α ∈ (0, 1).
   In approximate best-response dynamics, updates are smoothed through a
uniform combination of all pure strategies within γ of the best-response payoff:
                               x(t+1) = d
                                        BR(x(t) ),          γ ≥ 0.


                                                15
   Finally, stochastic approximation algorithms form a general class of iterative
methods, commonly used in optimization. Their convergence typically requires
a decaying step-size sequence (αt ), satisfying:
                           ∞
                           X                      ∞
                                                  X
                                 αt = ∞,                αt2 < ∞.
                           t=0                    t=0

    We adopt this idea by replacing the fixed step size α with a decaying sequence
(αt ), thereby incorporating stochastic inertia into the dynamics.
    Our proposed dynamics synthesizes the strengths of these techniques in order
to improve performance and encourage convergence in the game.
Definition 15. Let G be the set of pure strategies in a symmetric n-player game,
and let ∆(G) denote the set of mixed strategies over G. For g1 , g2 ∈ ∆(G), define
u(g1 , g2 ) as the payoff to a player who plays g1 when each of the other n − 1
players plays g2 .
   Approximate Best-Response Dynamics with Stochastic Inertia is an iterative
procedure in which the mixed strategy x(t) ∈ ∆(G) is updated at each iteration
according to the rule:

                     x(t+1) = (1 − αt ) · x(t) + αt · d
                                                      BR(x(t) ),

where:
   • αt ∈ (0, 1) is a decaying step-size parameter,

   • d
     BR(x(t) ) is an approximate best-response distribution that assigns equal
     probability to all pure strategies g ∈ G satisfying

                 u(g, x(t) , . . . , x(t) ) ≥ max
                                               ′
                                                  u(g ′ , x(t) , . . . , x(t) ) − γ,
                                             g ∈G

      for some tolerance parameter γ ≥ 0.
   A strategy x is an ε-equilibrium if the maximum gain that a player can
obtain by unilaterally deviating from it is bounded by ε. Formally:

                             max u(g, x) − u(x, x) ≤ ε.
                              g∈G

    Returning to our game, we look for an 0.01-equilibrium, which corresponds
to a best-response payoff of less than 0.26, since the equilibrium payoff is 0.25.
We initialize the process with a decaying step-size αt = 1t , a tolerance γ = 0.01,
and an initial strategy x(0) that assigns equal probabilities to all pure strategies
s ∈ Sδ .
    We ran the Approximate Best-Response Dynamics with Stochastic Inertia
algorithm for 1000 iterations. A strategy achieving a best-response payoff be-
low 0.26 is first reached after approximately 200 iterations. The best strategy
obtained during the process achieves a best-response payoff of around 0.257.
The convergence of the best-response value over iterations is shown in Figure 3.


                                             16
                        Best Response Values Over Iterations
         0.38
         0.36
         0.34
Values




         0.32
         0.30
         0.28
         0.26
                0          200       400         600       800         1000
                                        Iterations

                    Figure 3: Convergence behavior of the algorithm.


    Our Monte Carlo approach with 10,000 simulations is sufficiently stable for
the update step of the algorithm. However, in order to better evaluate the best
returned strategy, we increased the number of simulations to 1,000,000, and find
that its best-response payoff is around 0.254.
    The returned strategy is characterized by the probabilities assigned to each
of the 884 pure strategies in Sδ . These probabilities are shown graphically in
Figure 4, normalized so that the highest probability assigned is scaled to 1. A
discretized version, in which the probability of each strategy is rounded to three
decimal places, thus creating six levels of positive probabilities, is provided in
the appendix.
    An additional interesting graphical characteristic of a strategy is given by its
marginal distribution: When Player A faces Player B (who plays the strategy),
what is the probability density over the resource that Player B allocates to
the match against Player A? The estimated marginal density for the returned
strategy is shown in Figure 5.
    The marginal density increases up to a very sharp drop to zero. This increase
is not linear; it is well described either by a quadratic function ax2 + bx + c with
explained variance R2 = 0.98, or by an exponential function exp(ax + b) + c
with explained variance R2 = 0.99.
    In addition, the strategy with a sharp drop to zero is better than a similar
strategy with an instantaneous drop to zero, in terms of its best-response payoff
being closer to the equilibrium payoff.



                                          17
                 Heatmap of Pure Strategies with Probabilities
        1.0                                                                  1.0

                 z=0

        0.8                                                                  0.8




        0.6                                                                  0.6
                                                                 x=y




                                                                                   Probability
                                                                 y=z
    y




                 y=z                                             z=0
        0.4                                                                  0.4




        0.2                                                                  0.2


                 x=y
        0.0                                                                  0.0
           0.0      0.2         0.4         0.6        0.8             1.0
                                       x



 Figure 4: Normalized probability weights assigned by the returned strategy.


6.6     Five players
The algorithmic solution presented in the previous section extends naturally
from the four-player case to any number of players, though with two main
limitations.
    First, while a geometric representation of strategies is feasible for four players
in two dimensions, it requires a three-dimensional representation for five players,
and becomes practically infeasible for six players or more.
    Second, the computational complexity increases rapidly with the number of
players. For instance, with a discretization step-size of δ = 0.01, the four-player
game involved 884 pure strategies, whereas the five-player game requires 8,037
pure strategies.
    Nevertheless, implementing the algorithm remains possible, and the marginal
density of the computed strategy can still be presented. We ran the algorithm


                                            18
                                    Strategy Distribution
           3.0
           2.5
           2.0
 Density




           1.5
           1.0
           0.5
           0.0
              0.0          0.2         0.4           0.6        0.8            1.0
                                             Value

                 Figure 5: Marginal distribution of returned strategy n = 4.


in the five-player game for approximately 1250 iterations until reaching a strat-
egy with a payoff below 0.21, noting that the equilibrium payoff is 0.20, and
a strategy with a payoff below 0.215 was first reached after approximately 250
iterations.
    The marginal density of the resulting strategy increases non-linearly before
exhibiting a sharp drop to zero, mirroring the behavior observed in the four-
player case. It is shown in Figure 6.


7          Conclusion
We defined a round-robin resource allocation contest and analyzed four varia-
tions. The resulting symmetric equilibrium strategies are summarized in Ta-
ble 3, with pure equilibrium strategies in the variations with three players and
mixed equilibrium strategies in the variations with four or more players. In
addition, we proposed a best-response dynamics algorithm and used it to solve
one of the variations.
    The table illustrates a key difference between the two payoff schemes. One
can think of the total points payoff as representing a tournament where players
receive a prize for every match win, while in the winner-takes-all payoff, players
receive a prize only for winning the entire tournament.
    The tension between maximizing the total score and maximizing the proba-
bility of outscoring the opponents also exists in the scoring-based games them-


                                             19
                                    Strategy Distribution
             6

             5

             4
   Density




             3

             2

             1

             0
              0.0          0.2         0.4           0.6        0.8            1.0
                                             Value

                 Figure 6: Marginal distribution of returned strategy n = 5.

                                   n = 3 players           n ≥ 4 players
                 Total points        (x, 1 − x)    Any Blotto strategy with
                                                                          2
                    payoff          ∀x ∈ 12 , 1      marginal dist. U[0, n−1 ]
             Winner-takes-all         ( 12 , 12 )     Solved numerically for
                 payoff           unique solution        n = 4 and n = 5

                          Table 3: Symmetric equilibrium results.


selves. Skinner (2011) modeled a game as a sequence of independent plays and
found that, in certain situations, it may be optimal for teams to select plays
with a lower expected score but a higher variance in scoring outcomes.
    Although we were able to find symmetric equilibrium strategies in all varia-
tions, some questions remain open.
    In the total points payoff with four or more players, we proved that any
Blotto strategy is a symmetric equilibrium. The equilibrium is not unique, as
there are many different Blotto strategies. However, it is unclear whether there
is another symmetric equilibrium strategy, distinct from a Blotto strategy.
    In the winner-takes-all payoff with three players, we proved that ( 12 , 12 ) is the
unique symmetric equilibrium. Interestingly, while it is a best response against
any common strategy of the other two players, it may not be a best response
in the general case. For example, in the settings of Lemma 8, consider the case
x > y > 0.5. In that case, it is more beneficial for the third player to play z = y


                                              20
and receive Pz = 11                                                    5
                    24 , rather than play z = 0.5 and receive Pz = 12 . Further
analysis may result in interesting insights.
    In the winner-takes-all payoff with four or more players, we proposed an algo-
rithm and implemented it in the game with four players. We presented a simple
version with fixed tolerance γ = 0.01, with which the process stabilized after
1000 iterations and returned a strategy that achieved a best-response payoff of
0.254. However, an improved version with a decreasing tolerance γt = 0.05  √ was
                                                                             t
able to return a strategy with a best-response payoff of 0.252, cutting 50% of the
gap toward the equilibrium payoff, after 5000 iterations. Further optimization
of the algorithm parameters may lead to even better results.
    In addition to these questions, there are more potential variations to explore.
A fundamental assumption in our model is that players allocate resources in ad-
vance, before the competition begins. Analyzing a game with dynamic strategies
that allocate resources to stage k only after knowing the results of stage k − 1
would enrich the model.
    Furthermore, one could define an alternative payoff scheme in which there is
a reward for winning the tournament (finishing first) and a penalty for losing it
(finishing last). Another variation may consider using the Tullock mechanism
to determine match outcomes, instead of the all-pay rule.
    Finally, one may also extend the analysis from a symmetric game to an
asymmetric game, where players have heterogeneous resource budgets. Apart
from our two payoff schemes, a natural framework in this case is to assign
players a common objective function that combines two components: a large
prize for winning the tournament and smaller prizes for each match victory. In
such a setting, it is plausible that stronger players would focus on maximizing
their probability of winning the tournament, while weaker players would instead
emphasize maximizing their expected total points.


A     Proof of Lemma 8
There are eight configurations, denoted A, B, C, D, E, F, G, and H. In configu-
rations A, B, C, and D, Player 1 allocates x against Player 2. In configurations
A, C, E, and G, Player 2 allocates y against Player 1. In configurations A, B, E,
and F, Player 3 allocates z against Player 1. The complete payoff table, contain-
ing all 32 case–configuration combinations (except the trivial case x = y = z),
is provided below.

               case          configuration      Px     Py         Pz
            x>y>z                   A            0     0          1
            x>y>z                   B           1/3   1/3        1/3
            x>y>z                   C            0     0          1
            x>y>z                   D           1/3   1/3        1/3
            x>y>z                   E           1/3   1/3        1/3


                                        21
        Table of case-configuration combinations (Continued)
              case         configuration     Px    Py         Pz
           x>y>z                  F           0     1         0
           x>y>z                  G          1/3   1/3       1/3
           x>y>z                  H           0     1         0
           x=y>z                  A           0     0         1
           x=y>z                  B          1/3   1/3       1/3
           x=y>z                  C           0     0         1
           x=y>z                  D          1/3   1/3       1/3
           x=y>z                  E          1/3   1/3       1/3
           x=y>z                  F          1/2   1/2        0
           x=y>z                  G          1/3   1/3       1/3
           x=y>z                  H          1/2   1/2        0
        x > y = z > 1/2           A           0     0         1
        x > y = z > 1/2           B          1/3   1/3       1/3
        x > y = z > 1/2           C           0     0         1
        x > y = z > 1/2           D           0     0         1
        x > y = z > 1/2           E           0     1         0
        x > y = z > 1/2           F           0     1         0
        x > y = z > 1/2           G          1/3   1/3       1/3
        x > y = z > 1/2           H           0     1         0
        x > y = z = 1/2           A           0     0         1
        x > y = z = 1/2           B           0     0         1
        x > y = z = 1/2           C           0     0         1
        x > y = z = 1/2           D           0     0         1
        x > y = z = 1/2           E           0     1         0
        x > y = z = 1/2           F           0     1         0
        x > y = z = 1/2           G           0     1         0
        x > y = z = 1/2           H           0     1         0


B     Proof of Remark 10
Assume that the other two players, denoted Opponent 1 and Opponent 2, allo-
cate their resources independently as (X, 1 − X), where X ∼ fX , a continuous
density function over [0, 1]. Assume that I choose my allocation deterministi-


                                      22
cally as (y, 1 − y), where y ∈ [ 12 , 1].
    We will prove that my payoff, denoted as P0 , is given by

                 1                                  1 − Pr(1 − y < X < y)
          P0 =     + ay (1 − ay )   where    ay =                         .
                 6                                            2
    Without loss of generality, assume that I allocate y against Opponent 1, and
1 − y against Opponent 2.
    The other two players allocate their resources independently as (X, 1 − X),
where X ∼ fX . Therefore, against each of them, I meet in probability 12 an
allocation X ∼ fX , and in probability 12 an allocation X ∼ f1−X .
    In other words, the allocation I face is X ∼ gX , where gX = fX +f2 1−X , and
gX is symmetric around 21 , as gX = g1−X . Therefore, Pr(X > y | X ∼ gX ) =
Pr(X < 1 − y | X ∼ gX ). We will mark Pr(X > y | X ∼ gX ) = Pr(X < 1 − y |
X ∼ gX ) = ay , and Pr(1 − y < X < y | X ∼ gX ) = 1 − 2ay .
    We will mark the two independent realizations of the allocations of the other
two players against me as x1 and x2 . Meaning, x1 , x2 ∼ gX .
    With probability 1, the values x1 , 1 − x1 , x2 , 1 − x2 , y, and 1 − y are all
distinct, so there are no draws in the matches. Either one player wins two
matches and, therefore, wins the tournament, or there is a triple draw in the
tournament, meaning that each player wins one match.
    I win the tournament if I win both matches. That is, if y > x1 and 1−y > x2 .
This happens in probability ay (1 − ay ).
    There is a triple draw if (A) I win against Opponent 2 who wins against
Opponent 1 who wins against me, or (B) I win against Opponent 1 who wins
against Opponent 2 who wins against me.
    (A) occurs with probability Pr(1 − y > x2 and 1 − x2 > 1 − x1 and x1 >
y) = Pr(x1 > y and x2 < 1 − y) = Pr(x1 > y) · Pr(x2 < 1 − y) = ay · ay = a2y
    (B) occurs with probability Pr(y > x1 and 1−x1 > 1−x2 and x2 > 1−y) =
Pr(0 < x1 < y and 1 − y < x2 < 1 and x1 < x2 ). The event can be decomposed
into a disjoint union of three sub-events:

   • The first sub-event is 0 < x1 < 1 − y and 1 − y < x2 < 1.
   • The second sub-event is 1 − y < x1 < y and 1 − y < x2 < y and x1 < x2 .

   • The third sub-event is 1 − y < x1 < y and y < x2 < 1.

    The first sub-event occurs in probability ay (1 − ay ), the second sub-event
occurs in probability 21 · (1 − 2ay )2 , and the third sub-event occurs in probability
(1 − 2ay )ay . The sum of the probability of all options is 12 − a2y .
    In conclusion, the probability of a triple draw (which results in a payoff of 31
for me) is 12 , and my payoff is P0 = 16 + ay (1 − ay ) for ay = Pr(X > y | X ∼ gX ).
Since gX = fX +f2 1−X , we have ay = 21 Pr(X > y | X ∼ fX ) + 12 Pr(1 − X > y |
X ∼ fX ) = 12 Pr(X < 1 − y or X > y | X ∼ fX ) = 21 (1 − Pr(1 − y < X < y |
X ∼ fX )).
                                                                                    □


                                            23
C     Discretized version of the returned strategy



                 Heatmap of Pure Strategies with Probabilities
        1.0                                                                  1.0

                 z=0

        0.8                                                                  0.8




        0.6                                                                  0.6
                                                                 x=y




                                                                                   Probability
                                                                 y=z
    y




                 y=z                                             z=0
        0.4                                                                  0.4




        0.2                                                                  0.2


                 x=y
        0.0                                                                  0.0
           0.0      0.2         0.4         0.6        0.8             1.0
                                       x



Figure 7: Normalized and discretized probability weights assigned by the re-
turned strategy.


References
 [1] Ahn, T. K., Isaac, R. M., and Salmon, T. C. (2011) “Rent seeking in
     groups.” International Journal of Industrial Organization, 29(1):116-125.
 [2] Anne, K. (1974) “The political economy of the rent-seeking society.” Amer-
     ican economic review, 64(3):291-303.
 [3] Avrahami, J., Kareev, Y., Todd, P. M., and Silverman, B. (2014) “Alloca-
     tion of resources in asymmetric competitions: How do the weak maintain
     a chance of winning?.” Journal of Economic Psychology, 42:161-174.


                                            24
 [4] Baye, M. R., and Hoppe, H. C. (2003) “The strategic equivalence of rent-
     seeking, innovation, and patent-race games.” Games and Economic Behav-
     ior, 44(2):217-226.
 [5] Bertrand, J. (1889). Calcul des Probabilités. Gauthier-Villars.

 [6] Bistritz, I., and Leshem, A. (2017) “Approximate best-response dynamics
     in random interference games.” IEEE Transactions on Automatic Control,
     63(6):1549-1562.
 [7] Borel, E. (1921) “La théorie du jeu et les équations intégralesa noyau
     symétrique.” Comptes rendus de l’Académie des Sciences, 173(1304-1308),
     58.
 [8] Borel, E., and Ville, J. (1938) “Application de la Théorie des Probabilités
     aux Jeux de Hasard.” Review of industrial organization, 42(2):161-190.
 [9] Boix-Adsera, E., Edelman, B. L., and Jayanti, S. (2020) “The multiplayer
     colonel blotto game.” Proceedings of the 21st ACM Conference on Eco-
     nomics and Computation.
[10] Congleton, R. D., Hillman, A. L., and Konrad, K. A. (2008) “Forty years of
     research on rent seeking: an overview.” The Theory of Rent Seeking: Forty
     Years of Research, 1:1-42.

[11] Cramton, P. (2013) “Spectrum auction design.” Gauthier-Villars, Paris.
[12] Dagaev, D., and Zubanov, A. (2022) “Round-robin tournaments with lim-
     ited resources.” Social Choice and Welfare, 59(3):525-583.
[13] Feldman, M., Fu, H., Gravin, N., and Lucier, B. (2013) “Simultaneous
     auctions are (almost) efficient.” Proceedings of the forty-fifth annual ACM
     symposium on Theory of computing.
[14] Fonseca, M. A. (2009) “An experimental investigation of asymmetric con-
     tests.” International Journal of Industrial Organization, 27(5):582-591.
[15] Garcia-del-Barrio, P., and Szymanski, S. (2009) “Goal! Profit maximiza-
     tion versus win maximization in soccer.” Review of Industrial Organization,
     34(1):45-68.
[16] Glazer, A., and Hassin, R. (1988) “Optimal contests.” Economic Inquiry,
     26(1):133-143.
[17] Glazer, A., and Hassin, R. (2000) “Sequential rent seeking.” Public Choice,
     102(3):219-228.
[18] Greenwald, A., and Boyan, J. (2001) “Bidding algorithms for simultaneous
     auctions.” Proceedings of the 3rd ACM Conference on Electronic Com-
     merce, 26(1):133-143.


                                       25
[19] Hassin, R., and Nathaniel, A. (2021) “Self-selected task allocation.” Man-
     ufacturing and Service Operations Management, 23(6):1669-1682.
[20] Hausch, D. B. (1986) “Multi-object auctions: Sequential vs. simultaneous
     sales.” Management Science, 32(12):1599-1610.

[21] Holt Jr, C. A., and Sherman, R. (1982) “Waiting-line auctions.” Journal
     of Political Economy, 90(2):280-294.
[22] Juthamanee, C., Piromsopa, K., and Chongstitvatana, P. (2021) “Token
     allocation for course bidding with machine learning method.” 18th In-
     ternational Conference on Electrical Engineering/Electronics, Computer,
     Telecommunications and Information Technology (ECTI-CON).
[23] Krishna, A., and Unver, M. U. (2008) “Research note—improving the effi-
     ciency of course bidding at business schools: Field and laboratory studies.”
     Marketing Science, 27(2):262-282.
[24] Krishna, A., Sonmez, T., and Unver, U. (2004) “Efficiency enhanced course
     bidding: Evidence from a field experiment at the University of Michigan
     Business School.” The Field Experiments Website.
[25] Krishna, V., and Rosenthal, R. W. (1996) “Simultaneous auctions with
     synergies.” Games and economic behavior, 17(1):1-31.

[26] Krumer, A., Megidish, R., and Sela, A. (2017) “First-mover advantage in
     round-robin tournaments.” Social Choice and Welfare, 48(3):633-658.
[27] Lai, T. L. (2003) “Stochastic approximation.” The Annals of Statistics,
     31(2):391-406.
[28] Laokondee, S., and Chongstitvatana, P. (2021) “Quantum Neural Network
     model for Token allocation for Course Bidding.” 25th International Com-
     puter Science and Engineering Conference (ICSEC).
[29] McAfee, R. P., and McMillan, J. (1996) “Analyzing the airwaves auction.”
     Journal of Economic perspectives, 10(1):159-175.

[30] Milgrom, P. (2000) “Putting auction theory to work: The simultaneous
     ascending auction.” Journal of political economy, 108(2):245-272.
[31] Moldovanu, B., and Sela, A. (2001). “The optimal allocation of prizes in
     contests.” American Economic Review, 91(3):542-558.
[32] Roberson, B. (2006) “The Colonel Blotto game.” Economic Theory, 29(1).

[33] Roughgarden, T. (2016) Twenty lectures on algorithmic game theory. Cam-
     bridge University Press.
[34] Sela, A. (2023) “Resource allocations in the best-of-k (k = 2, 3) contests.”
     Journal of Economics, 139(3):235-260.


                                       26
[35] Sela, A., and Erez, E. (2013) “Dynamic contests with resource constraints.”
     Social Choice and Welfare, 41(4):863-882.
[36] Skinner, B. (2011) “Scoring strategies for the underdog: A general, quanti-
     tative method for determining optimal sports strategies.” Journal of Quan-
     titative Analysis in Sports, 7(4).

[37] Sonmez, T., and Unver, M. U. (2010) “Course bidding at business schools.”
     International Economic Review, 51(1):99-123.
[38] Swenson, B., Eksin, C., Kar, S., and Ribeiro, A. (2018) “Distributed in-
     ertial best-response dynamics.” IEEE Transactions on Automatic Control,
     63(12):4294-4300.
[39] Tullock, G. (1980) “Efficient rent seeking.” Toward a theory of the rent-
     seeking society, 97, 112.
[40] Weinstein, J. (2012) “Two notes on the Blotto game.” The B.E. Journal
     of Theoretical Economics, 12(1).




                                      27
