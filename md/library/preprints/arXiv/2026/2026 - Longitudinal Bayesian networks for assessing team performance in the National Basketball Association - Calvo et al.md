<!-- source: library/preprints/arXiv/2026/2026 - Longitudinal Bayesian networks for assessing team performance in the National Basketball Association - Calvo et al.pdf -->
<!-- item: https://arxiv.org/abs/2608.09824 -->
<!-- authors: Gabriel Calvo, Francisco Palmí-Perales, Carmen Armero, Virgilio Gómez-Rubio -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-05; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Longitudinal Bayesian networks for assessing team performance in the National Basketball Association

                                                Longitudinal Bayesian networks for assessing
                                                team performance in the National Basketball
                                                               Association
                                               Gabriel Calvo1 , Francisco Palmı́-Perales1 , Carmen Armero1 , and
                                                                    Virgilio Gómez-Rubio 2
                                                                            11th August 2026
arXiv:2608.09824v1 [stat.AP] 10 Aug 2026




                                           1
                                             Department of Statistics and Operations Research, Faculty of Mathematics,
                                           Universitat de València, Spain. gabriel.calvo@uv.es, carmen.armero@uv.es,
                                           francisco.palmi@uv.es
                                           2
                                             Department of Mathematics, School of Industrial Engineering-Albacete, Uni-
                                           versidad Castilla-La Mancha, Spain. virgilio.gomez@uclm.es

                                                                                  Abstract
                                                      Assessing the performance of a basketball team requires the consid-
                                                  eration of multiple sources of information. In recent years, the volume
                                                  and the quality of data generated in sport has increased considerably,
                                                  particularly in basketball. In this work, we propose a Bayesian graphical
                                                  modelling framework for the longitudinal analysis of basketball team per-
                                                  formance. The framework is based on Bayesian networks that explicitly
                                                  represent the nodes, that is, the random variables of interest, as longitud-
                                                  inal stochastic processes. We propose three baseline longitudinal models:
                                                  a static Bayesian network, a dynamic Bayesian network with an autore-
                                                  gressive structure between successive games, and a dynamic Bayesian net-
                                                  work based on a hidden Markov structure. We illustrate the proposed
                                                  framework through a real-world sports analytics case study involving the
                                                  Philadelphia 76ers of the National Basketball Association (NBA) during
                                                  the 2005–06 season. The analysis includes player participation, minutes
                                                  played, fouls drawn, and one-, two-, and three-point shots attempted and
                                                  made.


                                           1      Introduction
                                           The analysis of team and player performance in team sports generally requires
                                           the joint study of multiple interrelated variables. Bayesian networks (BNs) are
                                           particularly well suited to this task because they provide a multivariate mod-
                                           elling framework in which the probabilistic dependencies among the variables


                                                                                       1
can be represented explicitly through a graphical structure. This representation
also facilitates the interpretation of the relationships captured by the model.
    Sports analytics can be defined as the use of statistical, mathematical, and
computational methods to analyse sports data and support decision-making
concerning player and team performance, strategy, and sports management
(Alamar, 2013; Baumer et al., 2023). Basketball is one of the most popular
team sports in the entire world both at the professional, amateur and collegiate
levels. The National Basketball Association (NBA) is an American professional
basketball league and the premier professional basketball league in the world.
    In recent decades, the quality of sport-derived data has increased substan-
tially, particularly in basketball (Gudmundsson and Horton, 2017; Terner and
Franks, 2021). Such data are well suited to repeated-measures and longitudinal
modelling. In repeated-measures designs, multiple observations are obtained
from the same experimental units under varying conditions (Diggle, 2002).
    Bayesian Networks (BNs) are probabilistic models whose structure can be
represented graphically through directed acyclic graphs (DAGs). Nodes in BNs
are random variables. Edges are probabilistic relationships between nodes that
involve real causal relationships. More specifically, DAGs are directed graphs
that contain no directed cycles (Diestel, 2017). Within this graphical framework,
BNs provide a general approach to assessing model uncertainty by combining
the world of probability and graph theory (Holmes and Jain, 2008). As high-
lighted by Pearl and Russell (1995), the most relevant feature of BNs is that
they are “direct representations of the world, not of reasoning processes”. The
history of BNs is recent and dates back to the pioneering work of Pearl (1988),
who introduced the probabilistic approach to artificial intelligence and expert
systems. Since then, BN have become an indispensable tool in mastering AI in
uncertain environments (Wiegerinck et al., 2013).
    In addition, dynamic Bayesian Networks (DBNs) are BNs designed to rep-
resent temporal processes (Ghahramani, 1997). The random variables in these
type of networks are indexed by time, and the dependencies are modelled with
directed arcs from past to future, usually under a first-order Markov assump-
tion (i.e., each state depends only on the immediately preceding state) or under
autoregressive relationships. This framework generalises classical models such
as hidden Markov models (Kulkarni, 2011), allowing the representation of richer
temporal structures with both latent and observable variables.
    Although BNs have attracted increasing attention in sports analytics, the
applied literature remains sparse. Among the existing contributions, a copula-
based Bayesian network jointly models multivariate indicators of players’ per-
formances, capturing non-linear dependencies for interpretable probabilistic com-
parison of profiles (D’Urso et al., 2023). From a team perspective, structure
learning has been used to discriminate ‘winning’ from ‘losing’ team formations
and to identify influential variables along the path to victory (Zhang et al.,
2020). Regarding temporal scoring patterns, the hot-hand phenomenon has
been examined with hidden Markov models, which are particular instances of
dynamic BNs, with latent temporal states and observable nodes, thus enabling
inference on state-dependent efficiencies and streakiness over time (Sun, 2004;


                                       2
Sandri et al., 2020; Ötting and Andreas, 2022; Calvo et al., 2025). Applications
of BNs can also be found in the prediction of the outcomes of football matches
(Constantinou et al., 2012; Owramipur et al., 2013; Razali et al., 2017).
    In this context, this article focuses on the analysis of longitudinal basketball
data using BNs. We present three foundational models for evaluating basket-
ball player performance over the course of a season through the joint analysis
of minutes played, fouls drawn, and shots attempted and made. Utilising lon-
gitudinal Bayesian networks, specifically static, dynamic, and dynamic with
hidden states, these models are examined through a Bayesian inferential and
predictive framework. We illustrate our methodology using a case study of the
Philadelphia 76ers (NBA, 2005–06 season), though the modelling is broadly ap-
plicable to any team, league, or season. One of the objectives of the study is to
predict the number of points scored by each player in each game. Both model
estimation and prediction are carried out within a fully Bayesian framework.
    The remainder of the paper is organised as follows. Section 2 outlines the
performance data for the Philadelphia 76ers during the 2005–2006 NBA season,
which serves as the empirical basis for the analysis conducted in Section 5. Sec-
tion 3 presents the general Bayesian framework for estimation and prediction in
longitudinal Bayesian networks. Section 4 describes the three specific modelling
approaches proposed for analysing basketball data. Section 5 reports the results
obtained from applying the three models to the Philadelphia 76ers 2005-2006
NBA season. Finally, Section 6 discusses the main findings and limitations of
the study, presents some conclusions, and outlines directions for future research.


2    The Philadelphia 76ers
The Philadelphia 76ers are a professional basketball franchise based in the Phil-
adelphia metropolitan area, competing in the Atlantic Division of the Eastern
Conference within the National Basketball Association (NBA) in the USA. Dur-
ing the 2005–2006 NBA season, this team played a total of 82 games (the com-
plete regular-season schedule), with 38 wins and 44 losses. The team played
no additional postseason games, as they finished 9th in the Eastern Conference
and failed to qualify for the playoffs.
    The play-by-play data were obtained from NBAstuffer (NBAstuffer, 2022)
and were accessed on 3 May 2022. The study dataset contains information
on the performance of 13 players of the Philadelphia 76ers team who most
frequently participated during the 2005-2006 regular season, each identified by
their playing position (Pos), guard (PG, SG), forward (SF, PF) and center (C).
    Table 1 presents a summary of individual player statistics for the team during
that regular season. It includes the total minutes played (MP), number of per-
sonal fouls received, free throw attempts (FT Att), two-point field goal attempts
(2PT Att), and three-point field goal attempts (3PT Att), as well as successful
free throws (FT Made), two-point field goals (2PT Made), and three-point field
goals (3PT Made). These performance metrics provide the foundational data
for our Bayesian statistical modelling and analysis of shooting efficiency and


                                         3
player behaviour. Is it worth mentioning that the information in the table is
aggregated, with the total for the entire season reported for each player. In
this study, however, we analyse the data at the player-game level and adopt a
longitudinal modelling structure to account for changes in player performance
over the course of the season.

Table 1: Player performance summary of the 2005–2006 NBA regular season
of the Philadelphia 76ers team: position (Pos), minutes played (MP), fouls
received (FR), and free throws, two-pointers and three-pointers attempted and
made shooting statistics.


 Player              Pos    MP       FR        FT Att/Made   2PT Att/Made   3PT Att/Made
 Allen Iverson       PG    3103.35   672         829/675       1599/743       223/72
 Andre Iguodala      PG    3085.30   258         349/263       530/ 288       158/56
 Chris Webber        PF    2892.90   255         348/263       1345/596        77/21
 John Salmons        SG    2059.35   175         200/155       434/193         87/26
 Kevin Ollie         SG    1069.02    56           49/41        171/74          3/1
 Kyle Korver         SF    2562.80   124         119/101       323/143        438/184
 Lee Nailon          PF     237.50    13           15/13         80/40          0/0
 Lou Williams        PG     144.97     9           13/8          43/21          9/2
 Matt Barnes         PF     538.35    33          43/29          99/57         11/2
 Michael Bradley     PF     368.03    9             3/2          74/31          5/1
 Samuel Dalembert     C    1761.70   114         132/93         368/196         1/0
 Shavlik Randolph    PF    486.38    58            71/43         97/44          0/0
 Steven Hunter        C    1310.62   107          138/71       291/175          0/0


   A wide variety of performance profiles can be observed, ranging from high-
volume shooters such as Allen Iverson to lower-usage players. In particular,
Allen Iverson and Andre Iguodala were the most active players in terms of
minutes played, contributing significantly to the offensive output of the team,
as evidenced by their high number of attempts at shots in all categories. In
contrast, players like Lou Williams and Lee Nailon had limited playing time
and shot volume, representing more marginal roles. The table also highlights
positional diversity, offering insight into how shooting responsibilities and foul
patterns vary by position.


3    Bayesian framework for longitudinal Bayesian
     networks
Let (Y , Z) = {(Y j , Z j ), j = 1, . . . , J} be a longitudinal random vector whose
component relating to occasion or time j is in turn a random vector determined
by V observable random variables and W hidden random variables, (Y j , Z j ) =
   (1)          (V ) (1)         (W )
(Yj , . . . , Yj , Zj , . . . , Zj ). We assume that ϕ is a set of random effects
and θ is a set of parameters and hyperparameters that governs the stochastic
behaviour of (Y , Z).



                                           4
   A longitudinal Bayesian network (LBN) with nodes (Y , Z, ϕ, θ) is a joint
probability distribution for this random vector as follows:
                    p(y, z, ϕ, θ) = p(y, z | ϕ, θ) p(ϕ | θ) π(θ),                    (1)
where p(y, z | ϕ, θ) is the joint conditional probability distribution for Y and Z
given ϕ and θ that represents the LBN sampling model, p(ϕ | θ) the conditional
distribution of the vector of random effects ϕ given θ, and π(θ) a prior distri-
bution for the vector of parameters and hyperparameters θ. Note that we are
using lowercase letters as variables of a function, in this case, density functions.
Later, we will also use lowercase letters to denote the data, without making a
distinction, as the context is sufficiently clear to avoid ambiguities.
    LBNs have some important features that should be highlighted. Define the
              (v)        (w)                              (v)   (w)
parents pa(Yj ) (pa(Zj )) of the random variable Yj (Zj ) in the network
                                                                      (v)     (w)
as the set of nodes in (Y , Z) whose directed edges point towards Yj        (Zj     ). If
            (v)  (w)
the node Yj (Zj ) has no parents in (Y , Z), its random behaviour is described
                                    (v)            (w)
by the conditional distribution, p(yj | ϕ, θ) (p(zj | ϕ, θ)). For the sake of
                                             (w)
simplicity, we assume that the parents pa(Zj ) of a latent random variable
  (w)                                                                      (w)
Zj include only hidden nodes from Z. This is not the case for pa(Yj )
nodes, which can have observable or latent parents.
    Although formally, θ and ϕ are generally parents of the variables in (Y , Z),
we will not include them as members in the subsequent set pa(·) in order to
clearly distinguish the nature of the conditional probability distributions with
which we will address in each part of the paper. Note that our approach nat-
urally allows for the inclusion of shared random effects and shared paramet-
ers across longitudinal nodes. This induces an additional association structure
between longitudinal nodes that is not encoded by the conditional independence
relations of the DAG alone.
    The global semantics property of the BNs (Pearl and Russel, 2003) allows
the joint distribution p(y, z | ϕ, θ) to be expressed through the product of
conditional distributions on the parents:
      p(y,z | ϕ, θ) =
          QJ QV QW              (v)       (v)           (w)     (w)
             j=1   v=1   w=1 p(yj   | pa(yj ), ϕ, θ) p(zj | pa(zj ), ϕ, θ).          (2)
                                                            (v)      (v)
In this context, each local conditional distribution, p(yj | pa(yj ), ϕ, θ), as-
sociated with a node and its parent set in the BN can be interpreted as a
longitudinal submodel incorporating all relevant components, including covari-
ates.
                  (v)       (w)
   For a node Yj (or Zj ) in measurement or time j, if any of its parent
nodes include nodes from previous measurements or times j − 1, j − 2, . . . , 1,
then the model falls within the framework of dynamic BNs, and, in particular,
within longitudinal dynamic BNs (LDBNs). In the case of dynamic BNs, the
probabilistic relationship between a node and its parents can be modelled in
several ways, for instance, through Markovian or autoregressives relationships.


                                         5
    Bayesian learning in LBNs can be performed following the general Bayesian
inferential protocol. We always start by eliciting a prior distribution π(θ) on θ.
This distribution can be very informative if we have a lot of expert information
on θ or very vague if we do not have it or have it but do not want to include it in
the statistical analysis. A common choice for the distribution of random effects
ϕ given the hyperparameters is a multivariate normal distribution centered on
zero, with a more or less complex structure in the associated variance-covariance
matrix.
    Statistics’ favourite food is data. In the case of LBNs, we considered balanced
data from N individuals from paired observations of the observable random vari-
                                    (v)
ables Y of the network, D = {yij , i = 1, . . . , N, j = 1, . . . , J, v = 1, . . . , V },
        (v)                              (v)
where yij is the observed value of Yj for individual i. Prior and experimental
information are combined through Bayes’ theorem to obtain the posterior dis-
tribution of (ϕ, θ),

                        π(ϕ, θ | D) ∝ L(ϕ, θ) p(ϕ | θ) π(θ),                          (3)

where L(ϕ, θ) is the likelihood function of (ϕ, θ) for the data D.
    The posterior distribution π(ϕ, θ | D) is usually not analytical, so computa-
tional methods must be used to obtain approximate samples from it. Although
the field of Bayesian computation has experienced great growth in recent times,
MCMC and importance sampling procedures continue to be the ones most pop-
ular and widely used (Chib, 2001). The computation of π(ϕ, θ | D) via sim-
ulation allows one to approximate the posterior distribution of any relevant
(ϕ, θ)-dependent output as well as the joint posterior predictive distribution
of the possible outcomes Y ∗ of the network’s observable variables for a new
individual
                       R
           p(y ∗ | D) = p(y ∗ , z, ϕ, θ | D) d(z, ϕ, θ)
                       R
                      = p(y ∗ | z, ϕ, θ) p(z | ϕ, θ) π(ϕ, θ | D) d(z, ϕ, θ),

from which any posterior predictive marginal distribution or posterior predictive
conditional of interest associated with observable nodes can be approximated.


4     Bayesian LBNs for assessing the effectiveness
      of players on a basketball team
We propose three modelling approaches tailored to analyse the evolution of
player performance across successive league matches. The first one consists of
a static Bayesian network in which each node is treated as a longitudinal vari-
able. In the second approach, we additionally incorporate temporal depend-
encies between the observable nodes, leading to a dynamic LBN. Finally, we
introduce latent nodes in the network that follow a first-order Markov structure
over time, thereby defining a hidden dynamic LBN.



                                               6
4.1      A static LBN
Consider a set of i = 1, . . . , N basketball players from a team participating in a
J-game league for which we observe the following random variables:
                                               (F )
   • Number of personal fouls, Yij , received by player i in game j, j =
     1, . . . , J.
                                                           (T )                              (T )
   • Number of free throw attempts, Yij 1 , field goals attempts, Yij 2 , and
                                                          (T )
        three point field goals attempts, Yij 3 , made by player i in game j.
                                           (C )                     (C )
   • Number of free throws, Yij 1 , field goals, Yij 2 , and three point field
                (C )
        goals, Yij 3 , scored by player i in game j.

All the random variables defined above depend on the number of minutes played
                                           (M )
by player i in match j, denoted by Yij . Since not all players participate in
every game, we introduce an indicator random variable to represent whether or
not player i takes part in match j during the season. In particular, we define
                         (A)
the random variable Yij as 1 or 0 depending on whether or nor the player
i participates in the match j. Obviously, if player i does not play in match
                  (M )       (F )               (C )      (T )
j we will have Yij      = Yij = 0 and Yij k = Yij k = 0, with k = 1, 2, 3.
In addition, we included a covariate Hj in the modelling that indicates if the
match j is played at home (IH (j) = 1) or away (IH (j) = 0), and a set of
indicator covariates that inform about the position of each player on the field.
In particular, ICE (i), IP F (i), ISF (i), IP G (i), and ISG (i) will be equal to 1 if
player i occupies the center (CE), the power forward (P F ), the small forward
(SF ), the point guard (P G), and the shooting guard (SG) position on the field,
respectively, and 0 otherwise.

4.1.1     Structure
We begin by simplifying the notation in order to clarify the structure of the
probabilistic models presented in this paper. Let Y (C) = (Y (C1 ) , Y (C2 ) , Y (C3 ) )
and Y (T ) = (Y (T1 ) , Y (T2 ) , Y (T3 ) ) be the random vector with element Y (Ck ) =
    (C )                                                        (T )
{Yij k , i = 1, . . . , N, j = 1, . . . , J} and Y (Tk ) = {Yij k , i = 1, . . . , N, j =
1, . . . , J}, k = 1, 2, 3, respectively. We proposed a Bayesian LBN for the joint
distribution of all the above random quantities as follows,

             p(y (C) , y (T ) , y (F ) , y (M ) , y (A) , θ, ϕ) =
                       p(y (C) | y (T ) , θ, ϕ) p(y (T ) | y (F ) , y (M ) , y (A) , θ, ϕ)
                                                                                                    (4)
                        p(y (F ) | y (M ) , y (A) , θ, ϕ) p(y (M ) | y (A) , θ, ϕ)
                        p(y (A) | θ, ϕ) p(ϕ | θ) π(θ),

where ϕ will include all the random effects of the modelling and θ will be the set
of parameters and hyperparameters of the model. The joint distribution in (4)


                                                      7
factorizes as the product of the conditional joint distribution p(y (C) | y (T ) , θ, ϕ)
of the vector associated with the baskets scored given the shots attempted, θ
and ϕ; the conditional joint distribution p(y (T ) | y (F ) , y (M ) , y (A) , θ, ϕ) of the
shots attempted given the fouls received, the minutes played by each player in
each game, the presence of the player in each game, θ and ϕ; the joint condi-
tional distribution of p(y (F ) | y (M ) , y (A) , θ, ϕ) of fouls received in relation to
minutes played, the presence of the player in each game, θ and ϕ; the con-
ditional distribution p(y (M ) | y (A) , θ, ϕ) of the minutes played with regard to
the participation of the player in the match given θ and ϕ; the conditional dis-
tribution p(y (A) | θ, ϕ) indicating whether or not each player has participated
in each game given θ and ϕ; and the conditional distribution p(ϕ | θ) of the
random effects given their hyperparameters in θ and the prior distribution π(θ)
for θ.
                                                                             (A)
    The DAG for a player i that participates in match j (i.e. Yij = 1) as-
sociated with this LBN is shown in Figure (1). The knowledge of θ and ϕ
assumed by the conditional distributions of the observables in (4) allows the
assumption of conditional independence hypotheses that greatly simplify their
complete specification. Below we present the proposed modelling for each of
these conditional distributions.




Figure 1: DAG for the scoring LBN of basketball player i-th in the j-th basket-
ball match. For simplicity and better visualisation, the variable describing each
player’s possible participation in a match, the vector of parameters, hyperpara-
meters, and random effects have been omitted from the DAG.


4.1.2    Conditional distributions
The conditional distributions for the respective network nodes corresponding to
games played, minutes played, fouls drawn, shots attempted and shots made
are outlined below.



                                            8
Games played
Let Y (A) be the random vector describing the participation of all players in all
matches. Its conditional distribution is defined as:
                                    QJ QN          (A)
                   p(y (A) | θ, ϕ) = j=1 i=1 p(yij | θ, ϕ).                  (5)
                   (A)                                                            (A)
   Recall that Yij       is a binary variable, with probabilities P (Yij                = 1 | θ, ϕ)
         (A)
and P (Yij = 0 | θ, ϕ), associated with whether the player i plays or does not
                                              (A)                  (A)
play in match j-th of the season. That is, (Yij | θ, ϕ) ∼ Bern(pi ), where
 (A)
pi denotes the probability that the player i plays in a given match. Note
that, although it could depend on other factors, we are making the simplifying
assumption that the probability of playing or not depends only on the player.

Minutes played
The random vector Y (M ) representing the minutes played by the basketball
players of the team depends directly on Y (A) and (θ, ϕ):
                                        QJ QN       (M )  (A)
              p(y (M ) | y (A) , θ, ϕ) = j=1 i=1 p(yij | yij , θ, ϕ).  (6)

    We assume a conditional zero-inflated Poisson model (Lambert, 1992) (ZIP)
                                      (M )      (A)
for the conditional distribution of Yij given Yij and (θ, ϕ):
                                (M )          (A)
                          (Yij         | Yij        = 0, θ, ϕ) ∼ 0,
                                (M )          (A)                     (M )
                          (Yij         | Yij        = 1, θ, ϕ) ∼ Po(µi       ),                (7)
            (M )         (M )          (M )                 (M )
where log(µi ) = µ0 + bi , being µ0 a common mean among all players
                      (M )                2
in all matches, and (bi    | σM ) ∼ N(0, σM ) a random effect associated with
player i.

Fouls drawn
The personal fouls received by each player in a game depend on whether the
player participated in the match and, if so, on the number of minutes played.
The conditional distribution of the number Y (F ) personal fouls received by all
players in all games is as follows:
                                           QJ QN       (F )  (M ) (A)
        p(y (F ) | y (M ) , y (A) , θ, ϕ) = j=1 i=1 p(yij | yij , yij , θ, ϕ). (8)

In this case, we also chose a ZIP distribution to model the conditional distri-
bution in (8). When a basketball player does not play a game, the number of
fouls drawn is zero. Therefore,
                          (F )          (A)
                     (Yij        | Yij        = 0, θ, ϕ) ∼ 0,
                        (F ) (M )   (A)                (F )
                     (Yij | yij , Yij = 1, θ, ϕ) ∼ Po(µij ),


                                                        9
              (F )          (F )          (F )   (M )      (F )            (F )
being log(µij ) = µ0               + βM yij             + bi      , where µ0      is a common parameter
                                                      (F )
associated with all basket players in all matches, (bi | σF ) ∼ N(0, σF2 ) is a
                                                 (F )
random effect associated with the player i, and βM is the regression coefficient
associated with the minutes played by each player in each match.

Shots attempted
The shots taken by each basketball player depend on their presence in the match
and, if positive, on the number of minutes played. The exception is for free
throws, which depend on the fouls received or assigned to each player. In this
way, the conditional distribution for the number of shots thrown for al players
in all games is

p(y (T ) | y (F ) , y (M ) , y (A) , θ, ϕ) = p((y (T1 ) , y (T2 ) , y (T3 ) ) | y (F ) , y (M ) , y (A) , θ, ϕ)
      QJ QN                  (T )     (F ) (A)          Q3             (T )      (M ) (A)
  = j=1 i=1 p(yij 1 | yij , yij , θ, ϕ) k=2 p(yij k | yij , yij , θ, ϕ). (9)

We assume a ZIP distribution for each player’s throws in each match. In the
case of free throw attempts,
                              (T )          (A)
                         (Yij 1 | Yij             = 0, θ, ϕ) ∼ 0,
                            (T )   (F )   (A)                (T )
                         (Yij 1 | yij , Yij = 1, θ, ϕ) ∼ Po(µij 1 ).

  Assuming the center (C) position of a player as the reference category, the
mean of the free throws for each payer and match is expressed as
                     (T )           (T )          (T ) (F )        (T )              (T )
             log(µij 1 ) = β0 1 + βF 1 yij + βP F1 IP F (i) + βSF1 ISF (i)
                                       (T )                    (T )               (T )
                                   + βP G1 IP G (i) + βSG1 ISG (i) + bi 1 ,                              (10)
          (T )
where β0 1 is the regression coefficient associated with the center position of
               (T )
the player, βF 1 a slope associated with the faults received by each player
in each game, IQ (i) is an indicator function that takes the value 1 if player
                                                      (T )    (T ) (T )  (T )
i has characteristic Q and zero otherwise, and βP F1 , βSF1 , βP G1 , βSG1 are
the regression coefficients associated with each of the player’s position on the
field with regard to the center position: point guard (P G), the shooting guard
(SG), the small forward (SF ), and the power forward (P F ). The random effect
                                  (T )
associated with the player i is (bi 1 | σT1 ) ∼ N(0, σT2 1 ).
    Similarly, the numbers of two-point and three-point baskets attempted de-
pend on the minutes played and the unknown parameter vectors (θ, ϕ) according
to the ZIP distribution
                      (T )          (A)
                  (Yij k | Yij            = 0, θ, ϕ) ∼ 0,
                     (T )   (M )   (A)                (T )
                  (Yij k | yij , Yij = 1, θ, ϕ) ∼ Po(µij k ),                      k = 2, 3,




                                                          10
with
               (T )       (T )      (T ) (M )      (T )               (T )
          log(µij k ) = β0 k + βM k yij         + βP Fk IP F (i) + βSFk ISF (i)
                             (T )               (T )           (T )
                         + βP Gk IP G (i) + αSGk ISG (i) + bi k ,

where the β’s parameters have the same meaning as those defined in (10) except
     (T )
for βM k , which is now the coefficient associated with the minutes played by
                              (T )
each player and match, and (bi k | σTk ) ∼ N(0, σT2 k ) is a normally distributed
random effect associated with player i.

Shots scored
Finally, the conditional joint distribution of the random vector that represents
the basket scores is given by the attempted shots, θ and ϕ as follows:
                                    QJ QN Q3          (C )  (T )
          p(y (C) | y (T ) , θ, ϕ) = j=1 i=1 k=1 p(yij k | yij k , θ, ϕ).   (11)

Each shot that a player throws in a game can generate a basket or not, so the
number of baskets scored will be a binomial-type variable with a probability
that depends on the characteristics of the player, the match and the position
the player occupies on the court. Consequently,
                  (C )    (T )                  (T )    (C )
               (Yij k | yij k , θ, ϕ) ∼ Bi(yij k , pij k ), k = 1, 2, 3,

with
               (C )       (C )      (C )               (C )            (C )
         logit(pij k ) = β0 k + βH k IH (j) + βP Fk IP F (i) + βSFk ISF (i)
                             (C )               (C )           (C )
                         + βP Gk IP G (i) + βSGk ISG (i) + bi k ,                 (12)
        (C )
where β0 k is a common baseline parameter associated with each player in the
                                                             (C )
center position and match played away from home, bi k is a random effect
                                   (Ck )                 2                    (C )
associated with player i, where (bi      | σCk ) ∼ N(0, σC k
                                                             ). Furthermore, βH k is
the coefficient associated with the indicator IH (j), which takes the value 1 when
                                                                         (C )   (C )
the game j is played at home and 0 when it is played away. Finally, βP Fk , βSFk ,
 (Ck )        (Ck )
βP G , and βSG are the coefficients associated with the indicator variables for
the player’s court position. The center position is used as the reference category.

4.1.3   Prior distribution
We assume prior independence among the parameters and hyperparameters of
the model and consider a scenario of poor prior information. We elicit minimally
informative normal distributions with mean 0 and standard deviation 10 for all
regression coefficients of all conditional distributions of the DAG and uniform
distribution on the interval (0, 100) for all standard deviation hyperparameters.
Additionally, the prior distribution for binomial and zero-inflation probabilities
are considered as uniformly distributed between 0 and 1.


                                           11
4.2    A dynamic LBN
In the previous network, we did not consider any temporal probabilistic rela-
tionship between a node and its parents. In the event that this relationship is
to be included, one way to construct a dynamic LBN is, as mentioned above,
to assume an autoregressive relationship between nodes so that the parents of
a node at time (match) j can include nodes from the previous time (match)
j − 1.
    In our basketball study, we have represented each match’s play through the
static network in Figure 1, so a first-order auto-regressive structure can be added
by connecting the networks corresponding to two consecutive matches. Figure 2
shows a dynamic network that connects the networks of two consecutive matches
through the minutes played by each player. Also, in this DAG, we have omitted
the node describing the possible participation of player i in match j, and all the
parameters, hyperparameters, and random effects of the model.




Figure 2: DAG for the random variables of the Dynamic LBN of a basketball
player i who has participated in match j.


    All probabilistic relationships between nodes in this network remain the same
as those presented for the static network in the previous section, except for the
distribution of the node describing the minutes played by each player in each
match. In this case, the conditional distribution of Y (M ) is defined as
      p(y (M ) | y (A) , θ, ϕ) =
               QN          (M )    (A)       QJ      (M )  (M )     (A)
                 i=1 p(yi1      | yi1 , θ, ϕ) j=2 p(yij | yi j−1 , yij , θ, ϕ).   (13)
   For the case j = 1, this conditional model is the same as in the static
network, that is,
                           (M )      (A)
                        (Yi1      | Yi1    = 0, θ, ϕ) ∼ 0,
                           (M )  (A)                (M )
                        (Yi1 | Yi1 = 1, θ, ϕ) ∼ Po(µi ),


                                              12
               (M )       (M )       (M )
with log(µi ) = µ0 + bi . The dynamic structure for j > 1 is introduced
following the approach by Fokianos and Tjøstheim (2011) for log-linear autore-
gressive time series models:
                            (M )      (A)
                        (Yij       | Yij     = 0, θ, ϕ) ∼ 0,
                           (M ) (M )      (A)                (M )
                        (Yij | yi j−1 , Yij = 1, θ, ϕ) ∼ Po(µij ),

where
                            (M )           (M )      (+)          (M )     (M )
                      log(µij ) = µ0              + βM log(1 + yi j−1 ) + bi      .   (14)

        (M )                                                   (M )
Now µ0       also represents an overall mean, bi     a random effect associated
                                   2           (+)
with player i, (bi | σM ) ∼ N(0, σM ), and βM is the coefficient associated with
                                          (M )                            (+)
the autoregressive information from yi j−1 with prior distribution π(βM ) =
N(0, 102 ), following the same elicitation scheme as the previous model.

4.3     A hidden Markov LBN
We propose an alternative dynamic model, this time including certain latent
nodes. Specifically, we will construct a dynamic Bayesian network with a hidden
Markov model based on the ‘hot hand’ effect (Calvo et al., 2025) which will affect
the success of baskets scored.
    We first define a stochastic process that will invisibly govern the behaviour
of the network. Let {Zj , j = 1, . . . , J} be a hidden Markov chain (HMC) rep-
resenting the latent state of the team in game j, where Zj ∈ {C, H} indicates
whether the team is in a cold (C) or a hot (H) state. The latent process is
assumed to satisfy the Markov property,

                      P (Zj | Z1 , . . . , Zj−1 , θ, ϕ) = P (Zj | Zj−1 , θ, ϕ).

   The transition probability matrix of the chain is defined as
                                  CC
                                          q CH
                                               
                                   q
                             Ω = HC              ,                                    (15)
                                   q      q HH

where q CH = P (Zj = H | Zj−1 = C, θ, ϕ) denotes the transition probabil-
ity from the cold state C to the hot state H in game j, conditional on the
model parameters θ and ϕ. Finally, consider that Ω is a stochastic matrix, con-
sequently each row of the transition matrix sums to one, that is, q CC + q CH = 1
and q HC + q HH = 1.
    The structure of the hidden Markov LBN is shown in Figure 3. As we can
observe, the probabilistic relationships between player participation and minutes
played in successive matches, fouls drawn and shots taken will be the same as
those presented for the static network and will not be affected by the hidden
process. The baskets scored during a match will depend not only on the shots



                                                      13
attempted but also on the latent state of the team in the match as follows:
                                          J Y
                                            N Y
                                              3
                                                                 (C )      (T )
                                          Y
          p(y (C) | y (T ) , z, θ, ϕ) =                      p(yij k | yij k , zj , θ, ϕ).
                                          j=1 i=1 k=1

                                                 (C )
    The number of baskets scored Yij k , k = 1, 2, 3, will follow a binomial
distribution depending on the baskets thrown and the current state of the team.
In particular, a higher success probability when Zj = H, or a lower one when
Zj = C:
                      (C )                (T )                      (T )     (C )
                 (Yij k | Zj = C, yij k , θ, ϕ) ∼ Bi(yij k , pCijk ),
                      (C )                (T )                      (T )     (C )
                 (Yij k | Zj = H, yij k , θ, ϕ) ∼ Bi(yij k , pHijk ),
where
               (C )           (C )      (C )                 (C )                 (C )
        logit(pCijk ) = βC0k + βH k IH (j) + βP Fk IP F (i) + βSFk ISF (i)
                                 (C )                 (C )                 (C )
                             + βP Gk IP G (i) + βSGk ISG (i) + bi k ,
               (C )           (C )      (C )                 (C )                 (C )
        logit(pHijk ) = βH0k + βH k IH (j) + βP Fk IP F (i) + βSFk ISF (i)
                                 (C )                 (C )                 (C )
                             + βP Gk IP G (i) + βSGk ISG (i) + bi k .




Figure 3: DAG for the hidden Markov dynamic LBN of a basketball player i
                                           (A)
in a team basketball match team j, when Yij = 1. Nodes for parameters,
hyperparameters, and random effects have omitted in the DAG.


    Prior independence, wide normal distribution centered at 0, N(0, 102 ) are
elicited for the regression coefficients and beta prior distribution for the two
transition probabilities q CH and q HC , p(q CH ) = p(q HC ) = Beta(1, 1). It is


                                                 14
                                     (C )     (C )
worth noting that the restriction βC0k < βH0k is imposed, ensuring that the
team’s overall success probability is always higher in the hot state. Moreover,
this constraint ensures that we avoid the identifiability problem caused by label
switching, which is inherent in models with latent variables.


5     Philadelphia 76ers Player Performance
Inference across all three models for the Philadelphia 76ers performance dataset
is based on the joint posterior distribution of the parameters, hyperparameters,
and random effects. To obtain an approximation of the corresponding posterior
distribution we used the version 1.3.0 of the NIMBLE R package (de Valpine
et al., 2017), which relies on algorithms based on MCMC methods (Tanner,
1993). It is important to highlight the flexibility of NIMBLE, which does not
rely on a single MCMC algorithm. Instead, it implements a modular system
that combines several samplers, which are automatically selected according to
the structure of the model, while always allowing the user to modify them if
required.
    For each model, we ran three parallel chains with a total of 1,000,000 itera-
tions per chain, including a burn-in period of 500,000 iterations for each chain.
To reduce autocorrelation in the samples, the chains were thinned by retaining
every 500th iteration. All computations were performed on a computer equipped
with an Intel i9 processor, 32 GB of RAM, and running Windows 10 Enterprise
LTSC. All code required to reproduce the results in this paper is available at
https://github.com/gcalvobayarri/Longitudinal_BNs.

5.1    Model selection
We compare the three modelling approaches using the default implementation
of the Watanabe Akaike Information Criterion (WAIC) in the NIMBLE envir-
onment. The WAIC, introduced by Watanabe (2010), is a metric employed
for Bayesian model comparison that makes use of the information of the full
posterior distribution via the MCMC sample from it. It provides an estimate
of the out-of-sample predictive error. The underlying idea, shared with other
information criteria, is that the model with the smallest value is preferred, as it
indicates better expected predictive performance.
    Table 2 reports the WAIC values computed for the three LBNs. Based on
this criterion, the dynamic LBN is the preferred model, as it attains a lower
WAIC value than the remaining alternatives. Consequently, from this point
forward, we present the results for the dynamic network with an autoregressive
structure in the minutes played variable, namely the dynamic LBN.




                                        15
            Table 2: WAIC values for the three modelling approaches.

                             Model                         WAIC
                             Static LBN                   21274.69
                             Dynamic LBN                  21194.13
                             Hidden Markov LBN            21274.60


5.2       Estimation
Due to the large number of parameters and hyperparameters involved in the
selected dynamic LBN, the posterior distribution of all of them is presented
following the ordering of the joint distribution in expression (4). We begin with
the conditional model for the successful shots and conclude with the indicator
random variable that assesses the participation of a player in a game.
    Table 3 shows a summary of the approximate posterior distribution for the
parameters and hyperparameters of the logistic regression models that assess
the success of one-, two- and three-point shots by players in the same basketball
match. Although in many cases we observe rather wide credibility intervals,
particularly in the approximate posterior distribution of the parameters asso-
ciated with the three-point shooting variable, relevant information can still be
extracted from the data. For instance, when comparing the standard devi-
ation parameter associated with the players’ random effects, we observe that
the standard deviation associated with the probability of success on a 2-point
shot for each player, σC2 , exhibits smaller values whilst the variability in free
throws associated with the different players is much greater, slightly more than
double on average. This could be interpreted as indicating different variabil-
ity in field goal success probabilities among different players. In addition, the
                                                                      (C )   (C )
effect of playing at home, as reflected in the credible intervals of βH 1 , βH 2 ,
       (C )
and βH 3 , appears to be around zero for one-point and three-point shots, but
slightly positive for made two-point field goals.

Table 3: Summary of the approximated posterior distribution of the parameters
and hyperparameters of the 1PT, 2PT and 3PT shots scored submodels.

                   1PT Made (k = 1)                    2PT Made (k = 2)                     3PT Made (k = 3)
           Mean       Sd        0.95CI        Mean        Sd         0.95CI        Mean        Sd        0.95CI
  (C )
 β0 k      0.457     0.428   (-0.333,1.329)   0.233      0.172   (-0.115,0.559)    -3.434     2.892   (-9.657,1.683)
  (Ck )
 βH        0.045     0.099   (-0.148,0.246)   0.067      0.056   (-0.041,0.175)    -0.060     0.132   (-0.321,0.202)
  (C )
 βP Fk     0.452     0.518   (-0.587,1.517)   -0.386     0.214   (-0.798,0.029)     2.323     2.910   (-2.876,8.598)
  (Ck )
 βP G      0.699     0.541   (-0.431,1.674)   -0.274     0.229   (-0.712,0.168)     2.726     2.904   (-2.421,8.999)
  (C )
 βSFk      1.271     0.730   (-0.300,2.663)   -0.493     0.300   (-1.072,0.123)     3.145     2.923   (-2.109,9.595)
  (Ck )
 βSG       0.924     0.585   (-0.240,2.079)   -0.507     0.249   (-0.998,-0.004)   2.578      2.931   (-2.578,8.952)
  σCk      0.475     0.239   (0.175,1.053)    0.190      0.093    (0.059,0.416)    0.302      0.351   (0.012,1.163)




                                              16
    Furthermore, bearing in mind that the player’s position associated with the
reference category is the center, there appears to be a relationship between the
probability of scoring and certain player positions on the pitch. The shots made
by the center players (in the early 2000s) were mainly two-point shots scored
from a close position to the basket. This fact makes that the percentage of
success was higher to the ones that are tried from a further positions, which are
the most common shots of power forward and shooting forward players. That
explains why the credible intervals of the two point shots of these players com-
                                                           (C )       (C )
pared with the center players are mostly negative (βP F2 and βSF2 ). On the
other hand, shooting guards are generally among the shortest players on the
team. They usually attempt shots beyond the three-point line and tend not to
play close to the basket, as they can be more easily blocked by opposing play-
ers. This is reflected in the credible intervals for shooting guards compared with
           (C )       (C )
centers (βSG2 and βSG3 ). Moreover, Table 4, which presents the posterior prob-
ability that each parameter is greater than zero, supports the interpretations
discussed above.

Table 4: Posterior probability that each parameter is greater than zero for the
1PT, 2PT and 3PT shots made submodels.


                        1PT Made (k = 1)    2PT Made (k = 2)   3PT Made (k = 3)
        (C )
    Pr(β0 k > 0 | D)         0.896               0.933              0.102
        (C )
    Pr(βH k > 0 | D)         0.667               0.884              0.319
        (C )
    Pr(βP Fk > 0 | D)        0.849               0.032              0.780
        (C )
    Pr(βP Gk > 0 | D)        0.927               0.087              0.830
        (C )
    Pr(βSFk > 0 | D)         0.961               0.043              0.873
        (C )
    Pr(βSGk > 0 | D)         0.951               0.024              0.812


    It should also be noted that we have a sample from the posterior distribution
of the random effects associated with each player. By combining all the available
information, we can estimate the probability of making any of the three types
of shots for any player in a game, according to expression (12). Specifically,
we visualise the success probabilities of two outstanding players: Allen Iverson
and Kyle Korver. Figure 4 shows the approximate posterior distributions of the
success probabilities for 1PT, 2PT, and 3PT shots for these two players. We
observe that, for both players, the free throw is the easiest shot, exhibiting the
highest probability of success. This is followed by field goals, with a success
probability of around 0.5 in both cases. Finally, the three-point shot appears,
as expected, to have the lowest probability of success. However, at this point, a
notable difference emerges between the two players. Kyle Korver clearly shows
a much higher probability of successfully making a three-point shot than Allen
Iverson.




                                           17
          30                                                                                   30




          20                                                                                   20
                                                                 Shots scored                                                                             Shots scored
Density




                                                                                     Density
                                                                   1PT                                                                                      1PT
                                                                   2PT                                                                                      2PT
                                                                   3PT                                                                                      3PT
          10                                                                                   10




           0                                                                                    0
               0.00   0.25        0.50        0.75        1.00                                      0.00           0.25        0.50       0.75    1.00
                               Probability                                                                                  Probability


                         (a) Allen Iverson.                                                                               (b) Kyle Korver.

Figure 4: Approximate posterior distributions of the success probabilities for
1PT, 2PT, and 3PT shots by Allen Iverson and Kyle Korver.

    Table 5 presents a summary of the posterior distribution of the different
types of shots attempted. We observe that the credible interval for the three-
                                       (T )
point attempts of center players, β0 3 , is negative. As this position typically
operates inside the three-point line, players in this role have fewer opportunities
                                                                    (T )  (T )
to attempt shots from long range. In addition, the parameters βF 1 , βF 2 , and
  (T )
βF 3 have approximated posterior distributions with positive values. This in-
dicates that the number of fouls received influences the number of free throws,
and that the minutes played also affect the volume of field-goal attempts. In
            (T )
contrast, βP G3 is entirely positive, meaning that point guards generally attempt
more three-point shots than other positions. In addition, the 95% credible in-
                                                                   (T )
terval for the small forward position in three-point attempts, (βSF3 ), is entirely
positive. This is mainly because the most efficient three-point shooters in those
years played mainly as point guards or small forwards.

Table 5: Summary of the approximated posterior distribution of the parameters
and hyperparameters of the 1PT, 2PT and 3PT shots attempted submodels.

                             1PT Attempted (k = 1)                                   2PT Attempted (k = 2)                                               3PT Attempted (k = 3)
                      Mean               Sd             0.95CI                  Mean                        Sd                0.95CI             Mean              Sd         0.95CI
           (T )
          β0 k         0.246        0.830            (-1.268,2.110)             0.591                      0.398          (-0.196,1.340)         -5.900           1.703   (-9.587,-2.810)
           (Tk )
          βF           0.227        0.009            (0.208,0.245)              0.040                      0.002          (0.036,0.044)           0.030           0.005    (0.021,0.039)
           (T )
          βP Fk       -0.811        1.050            (-3.061,1.046)             -0.064                     0.486          (-1.016,0.919)          2.471           2.076   (-1.758,6.590)
           (Tk )
          βSF         -0.305        1.383            (-3.275,2.262)             -0.546                     0.743          (-1.997,0.904)          6.659           2.748   (1.357,12.635)
           (T )
          βP Gk       -0.333        1.085            (-2.873,1.616)             0.009                      0.533          (-1.061,1.032)         5.135            2.100    (1.148,9.665)
           (Tk )
          βSG         -0.330        1.153            (-2.823,1.873)             -0.182                     0.592          (-1.369,0.999)          3.705           2.327   (-0.919,8.593)
           σTk         1.124        0.409            (0.605,2.112)              0.598                      0.185          (0.342,1.062)           2.194           1.003    (0.947,4.593)


   Table 6 refers to the minutes played by each player in a game and reports
the posterior distribution of a common mean of the participation of each player
               (M )                    (+)
in a match, µ0 , the autoregressive βM regression coefficient associated to
the minutes played by each player in the previous game, and the standard
deviation σM of the random effect associated to each player. We observe that


                                                                                18
the autoregressive coefficient responsible for turning this LBN into a dynamic
LBN takes relatively small values. However, the 95% credible interval of the
approximated posterior distribution is entirely positive.

Table 6: Summary of the approximate posterior distribution of the parameters
and hyperparameters of the minutes played submodels.



                                  Mean       Sd            0.95CI
                           (M )
                          µ0      2.616    0.223    (2.172, 3.004)
                            (+)
                          βM      0.097    0.011    (0.076, 0.119)
                           σM     0.688    0.177    (0.451, 1.089)


    Finally, Table 7 displays a summary of the posterior distribution of the
individual probabilities of playing a match. High values can be seen almost all
the players which are even higher for the stars of the team (Iverson, Iguodala
and Webber). Less dominance can be seen in the centers (Dalmebert, Randolph
and Hunter) which had the same probability of playing. It is also interesting to
see that Korver and Salmons have a high probability, that is because they were
seen as the young promises of the team.

Table 7: Summary of the approximated posterior distribution of the individual
probabilities of playing.



                 Player                   Mean      Sd              0.95CI
                 Allen Iverson            0.870    0.036     (0.792, 0.932)
                 Andre Iguodala           0.988    0.012     (0.958, 1.000)
                 Chris Webber             0.905    0.031     (0.835, 0.957)
                 John Salmons             0.988    0.012     (0.958, 1.000)
                 Kevin Ollie              0.845    0.039     (0.764, 0.914)
                 Kyle Korver              0.988    0.012     (0.959, 1.000)
                 Lee Nailon               0.273    0.047     (0.188, 0.372)
                 Lou Williams             0.369    0.054     (0.272, 0.483)
                 Matt Barnes              0.606    0.053     (0.501, 0.706)
                 Michael Bradley          0.561    0.053     (0.454, 0.664)
                 Samuel Dalembert         0.797    0.044     (0.709, 0.878)
                 Shavlik Randolph         0.690    0.051     (0.585, 0.788)
                 Steven Hunter            0.833    0.040     (0.750, 0.906)




5.3    Prediction
A powerful feature of BNs is their capacity to compute predictions by systemat-
ically applying the total law of probability within their structured probabilistic
framework. This architecture allows not only the prediction of variables con-
ditioned by others that influence them probabilistically, but also flexible pre-


                                            19
dictions of any variables given new evidence about anothers. This versatility,
in turn, facilitates multidirectional reasoning, allowing prediction from causes
to effects and from effects back to causes. In the Bayesian framework, we use
                                                                             (A)
the joint posterior predictive distribution of the possible participation, y ∗ ,
               (M )                                   (F )
the number y ∗ of minutes played, the number y ∗ of fouls drawn, and the
                                        (T )      (C)
number of shots thrown and scored, y ∗ and y ∗ , respectively, of each player
of the team in a new hypothetical match defined as
           (C)   (T )   (F )   (M )   (A)
     f (y ∗ , y ∗ , y ∗ , y ∗ , y ∗ | D) =
             R       (C)   (T )  (F )  (M )  (A)
                f (y ∗ , y ∗ , y ∗ , y ∗ , y ∗ | θ, ϕ) π(θ, ϕ | D) d(θ, ϕ).           (16)

From the complete posterior predictive distribution, it is possible to compute
different types of posterior predictive marginals and conditionals outputs. The
analysis may focus on those predictions that are of particular interest for the
model. For instance, one may predict how many points in total, counting those
scored from free throws, two-point shots and three-point shots, will the player
score in the next match in the case the player would play more or less than a
given number of minutes. Figure 5 presents an approximation of this predictive
distribution for Allen Iverson and Kyle Korver in the event that they played for
more than 30 minutes. The results show clearly that the predicted points for
Allen Iverson are higher than those for Kyle Korver.




    0.10

                                                                   Player
                                                                      Allen Iverson
                                                                      Kyle Korver
    0.05




    0.00
            0                  20                   40       60
                                      Points

Figure 5: Approximate predictive distribution of the total number of points
scored (1PT + 2PT+ 3PT) by the players Allen Iverson and Kyle Korver in a
new match, assuming they play more than 30 minutes.

    We can also approach the problem the other way round. That is, knowing
that a particular player has scored more or less than a certain number of points,
we could predict how many minutes he has played during the match. Figure 6
shows the approximate posterior predictive distribution of the minutes played
given that the player, Allen Iverson or Kyle Korver, has scored 10 points or fewer


                                               20
in a match. It can be observed that the posterior predictive distribution of the
minutes played, given the points scored, is a mixture probability distribution,
as a consequence of how the model is defined in expression (7). In this sense, it
can be observed in Figure 6 that if Allen Iverson scores fewer than 10 points in
a game, this is likely because he did not play or played very few minutes. This
does not occur with Kyle Korver, as can be seen in Figure 6.


    0.6




    0.4
                                                                Player
                                                                   Allen Iverson
                                                                   Kyle Korver

    0.2




    0.0
          0          10           20          30          40
                               Minutes

Figure 6: Approximate predictive distribution of the total number of minutes
played by Allen Iverson and Kyle Korver in a new match assuming they score
a total of 10 points or fewer.


6    Conclusions, limitations and future research
     lines
The main contribution of this work is to develop a longitudinal analysis of bas-
ketball team performance within a Bayesian graphical modelling framework. In
particular, we discuss three basic, generic longitudinal models for evaluating the
performance and effectiveness of players in a basketball team over the course of
an entire league season: a static longitudinal Bayesian network, a dynamic lon-
gitudinal Bayesian network incorporating an autoregressive dependence struc-
ture between succesive matches, and a dynamic longitudinal Bayesian network
based on a hidden Markov structure. The proposed models can easily be adap-
ted to other leagues beyond the NBA and to updated schedules, while allowing
for the straightforward integration of additional relevant nodes and covariates.
    In the specific case of the Philadelphia 76ers, the results showed that the
autoregressive model, referred to as the dynamic LBN model, provided the
best predictive performance, as indicated by its lowest WAIC value. Among
other findings, the proposed framework enabled us to predict both the points
scored and the minutes played by all the players of the team. At the player
level, the posterior predictive distributions for Allen Iverson and Kyle Korver
indicate that, when Iverson plays more than 30 minutes, he is expected to score


                                         21
considerably more points than Korver. They also suggest that Iverson points
total below 10 is associated with a high posterior predictive probability of him
not having played in that game. This pattern is not observed for Kyle Korver.
    Given that automatic graph structure learning constitutes a highly complex
combinatorial problem, particularly in the presence of latent nodes, its investig-
ation has been deliberately placed beyond the scope of this study. Accordingly,
the network structure is assumed to be specified by the researcher or treated as
known.
    This modelling perspective naturally suggests several directions for future
research. A first extension would be to allow for multivariate nodes, enabling
a single node to represent a set of correlated variables that evolve jointly over
time, such as the numbers of free throws, two-point field goals, and three-point
field goals made in each match. An especially promising line of work concerns
the incorporation of spatial or spatio-temporal nodes, which would make it pos-
sible to capture spatial dependencies and their interaction with longitudinal
dynamics. In addition, further research should address approximate approaches
to structural learning, as well as extensions of the framework to unbalanced data
and irregular measurement times. Altogether, these developments would com-
plement the framework proposed here and considerably broaden its applicability
to a wider range of complex longitudinal phenomena.


Acknowledgements
This work is part of the project PID2022-136455NB-I00, funded by Ministerio de
Ciencia, Innovación y Universidades of Spain (MCIN/AEI/10.13039/501100011033/
FEDER, UE) and the European Regional Development Fund.


References
Alamar, B. C. (2013). Sports analytics: A guide for coaches, managers, and
  other decision makers. Columbia University Press.
Baumer, B. S., Matthews, G. J., and Nguyen, Q. (2023). Big ideas in sports
  analytics and statistical tools for their investigation. Wiley Interdisciplinary
  Reviews: Computational Statistics, 15(6):e1612.
Calvo, G., Armero, C., and Spezia, L. (2025). Can the hot hand phenomenon be
  modelled? A Bayesian hidden Markov approach. Computational Statistics,
  40(4):2195–2222.
Chib, S. (2001). Chapter 57 - Markov Chain Monte Carlo Methods: Computa-
  tion and inference. volume 5 of Handbook of Econometrics, pages 3569–3649.
  Elsevier.




                                       22
Constantinou, A. C., Constantinou, A., Fenton, N., Fenton, N., Neil, M., and
  Neil, M. (2012). Pi-football: A Bayesian network model for forecasting Asso-
  ciation Football match outcomes. Knowledge Based Systems.
de Valpine, P., Turek, D., Paciorek, C. J., Anderson-Bergman, C., Lang,
  D. T., and Bodik, R. (2017). Programming with models: writing stat-
  istical algorithms for general model structures with NIMBLE. Journal of
  Computational and Graphical Statistics, 26(2):403–413.
Diestel, R. (2017). Graph Theory: 5th edition. Springer Graduate Texts in
  Mathematics. Springer.
Diggle, P. (2002). Analysis of longitudinal data. Oxford university press.

D’Urso, P., De Giovanni, L., and Vitale, V. (2023). A Bayesian network to ana-
  lyse basketball players’ performances: a multivariate copula-based approach.
  Annals of Operations Research, 325(1):419–440.
Fokianos, K. and Tjøstheim, D. (2011). Log-linear Poisson autoregression.
  Journal of multivariate analysis, 102(3):563–578.
Ghahramani, Z. (1997). Learning dynamic Bayesian networks. In International
 School on Neural Networks, Initiated by IIASS and EMFCSC, pages 168–197.
 Springer.
Gudmundsson, J. and Horton, M. (2017). Spatio-temporal analysis of team
 sports. ACM Computing Surveys (CSUR), 50(2):1–34.
Holmes, D. E. and Jain, L. C. (2008). Introduction to bayesian net-
  works. In Holmes, D. E. and Jain, L. C., editors, Innovations in Bayesian
  Networks: Theory and Applications, volume 156 of Studies in Computational
  Intelligence. Springer.

Kulkarni, V. G. (2011). Introduction to Modeling and Analysis of Stochastic
 Systems, volume 1. Springer.
Lambert, D. (1992). Zero-inflated Poisson regression, with an application to
  defects in manufacturing. Technometrics, 34(1):1–14.

NBAstuffer (2022). Nba play-by-play data. https://www.nbastuffer.com/
 analytics101/playbyplay-data/. Accessed 3 May 2022.
Ötting, M. and Andreas, G. (2022). A regularized hidden Markov model for
   analyzing the ‘hot shoe’in football. Statistical Modelling, 22(6):546–565.
Owramipur, F., Owramipur, F., Eskandarian, P., Eskandarian, P., Mozneb,
 F. S., and Mozneb, F. S. (2013). Football result prediction with bayesian
 network in spanish league-barcelona team. International Journal of Computer
 Theory and Engineering.



                                      23
Pearl, J. (1988). Probabilistic Reasoning in Intelligent Systems: Networks of
  Plausible Inference. Morgan Kaufmann.
Pearl, J. and Russell, S. (1995). Bayesian networks. arbib, m. In Arbib, M. A.,
  editor, Handbook of Brain Theory and Neural Networks. MIT Press.

Razali, N., Razali, N., Mustapha, A., Mustapha, A., Yatim, F. A., Yatim, F. A.,
  Aziz, R., and Aziz, R. A. (2017). Predicting football matches results using
  bayesian networks for english premier league (epl). null.
Sandri, M., Zuccolotto, P., and Manisera, M. (2020). Markov switching mod-
  elling of shooting performance variability and teammate interactions in bas-
  ketball. Journal of the Royal Statistical Society Series C: Applied Statistics,
  69(5):1337–1356.
Sun, Y. (2004). Detecting the hot hand: An alternative model. In Proceedings
  of the annual meeting of the cognitive science society, volume 26.
Tanner, M. A. (1993). Tools for statistical inference, volume 3. Springer.

Terner, Z. and Franks, A. (2021). Modeling player and team performance in
  basketball. Annual Review of Statistics and Its Application, 8(1):1–23.
Watanabe, S. (2010). Asymptotic equivalence of Bayes cross validation and
 widely applicable information criterion in singular learning theory. Journal
 of machine learning research, 11(12).

Wiegerinck, W., Burgers, W., and Kappen, B. (2013). Bayesian Networks,
 Introduction and Practical Applications, pages 401–431. Springer Berlin
 Heidelberg, Berlin, Heidelberg.
Zhang, Z., Zhang, L., Wang, C., and Wei, Z. (2020). Bayesian network
  learning for winning structure and losing structure in basketball games. In
  2020 International Conference on Image, Video Processing and Artificial
  Intelligence, volume 11584, pages 348–353. SPIE.




                                       24
