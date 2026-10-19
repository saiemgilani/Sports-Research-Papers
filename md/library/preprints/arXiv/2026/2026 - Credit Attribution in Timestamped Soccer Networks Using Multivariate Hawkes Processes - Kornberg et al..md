<!-- source: library/preprints/arXiv/2026/2026 - Credit Attribution in Timestamped Soccer Networks Using Multivariate Hawkes Processes - Kornberg et al..pdf -->
<!-- arXiv:2610.12775 | https://arxiv.org/abs/2610.12775 | filed 2026-10-19 -->

# Credit Attribution in Timestamped Soccer Networks Using Multivariate Hawkes Processes

                                           Credit Attribution in Timestamped Soccer
                                         Networks Using Multivariate Hawkes Processes

                                                             Phillip W. Kornberg and Kevin S. Xu

                                                                 Case Western Reserve University
                                                       10900 Euclid Avenue, Cleveland, OH 44106-7071, USA
                                                                     {pwk9,ksx2}@case.edu
arXiv:2610.12775v1 [cs.SI] 8 Oct 2026




                                              Abstract. The two main traditional player statistics used in soccer are
                                              goals scored and assists, with an assist credited when a player’s pass im-
                                              mediately leads to a teammate scoring. Attributing credit solely to the
                                              player who makes the final pass before a goal fails to account for the con-
                                              tributions of multiple players in the buildup to the goal. Consequently,
                                              traditional statistics provide only a limited view of player involvement.
                                              In this paper, we use multivariate Hawkes processes (MHPs) to model
                                              timestamped sequences of passes and shots, which form continuous-time
                                              networks. MHPs provide a branching mechanism where an event (a pass
                                              or shot) can be generated as a child of a previous event, which allows us
                                              to quantify each pass’s contribution to a subsequent pass or shot. This
                                              approach distributes credit across multiple passes within an attacking
                                              sequence, making it applicable across a wide range of situations. Build-
                                              ing on this framework, we propose expected goal involvements (xGI),
                                              a metric that measures a player’s involvement in creating goal scoring
                                              opportunities based on their passes. This metric identifies players who
                                              play key roles in creating goal scoring opportunities even if they do not
                                              make the final pass, offering a more comprehensive measure of attacking
                                              involvement and player performance.

                                              Keywords: continuous-time network, Hawkes process, soccer analytics,
                                              player evaluation, expected assists, expected goal involvements


                                        1   Introduction
                                        Passing the ball between players on the same team is a crucial part of the sport of
                                        association football, also known as soccer. The collection of passes during a soccer
                                        match is naturally modeled as a continuous-time network with nodes denoting
                                        players and timestamped directed edges denoting passes from one player to a
                                        teammate at a specific time during the match. Such passing networks have been
                                        the topic of many prior studies [3,4,8], often with the goal of better understanding
                                        collective team performance and tactics. Shots on goal can also be modeled by
                                        treating the opposing team’s goal as an additional node and adding an edge from
                                        the player taking the shot to the goal node.
                                            In this paper, we consider the problem of credit attribution in soccer passing
                                        networks: for a given action in a soccer match, such as a specific pass or shot,
2       Phillip W. Kornberg and Kevin S. Xu

what past actions contributed most to the given action? This is especially im-
portant when we want to assign credit for shots on goal. Traditionally, credit for
a shot is given to two players, the player who shoots the ball (the shooter), and
the player who passed the ball to the shooter (the passer). If the shot goes into
the opposing team’s goal, then the shooter is awarded a goal, and the passer is
awarded an assist, recognizing the important contribution of the passer. If the
shot does not go into the goal, then the passer does not receive an assist, despite
the outcome of the shot being mostly out of the passer’s control.
    Recent developments in soccer analytics have moved to separate the outcome
of a shot from the actions leading up to the shot, resulting in the creation of the
expected goals (xG) and expected assists (xA) metrics. The xA metric allows
the player who passed the ball to the shooter to still receive credit for creating
a goal scoring opportunity regardless of the outcome of the shot. However, no
credit is passed further back, to the players who made the passes leading up to
the final pass. These previous passes could still be very important contributions
to the shot and should also receive some credit.


Key Contributions We make three main contributions in this paper. First,
we propose to use multivariate Hawkes processes (MHPs) to model timestamped
networks of passes and shots, providing a mechanism that can be used to esti-
mate the responsibility of each prior pass leading up to a pass or shot. Next, we
use these responsibilities to create a new statistic, the expected goal involvements
(xGI), that measures a player’s involvement in creating goal scoring opportuni-
ties beyond the final pass based on their passing history. Finally, we apply these
methods to analyze data from the 2015/2016 La Liga season at the team and
league level.


2     Background and Related Work

2.1   Soccer Analytics Metrics

In recent years, soccer analytics has progressed significantly, moving away from
simple cumulative statistics such as shots and total passes to more sophisticated
metrics like expected goals (xG) along with expected assists (xA). Expected goals
(xG) is a metric that assigns each shot a value between 0 and 1, representing the
likelihood that a shot will result in a goal based on factors such as shot location
and defensive pressure [11]. Closely related to expected goals is expected assists
(xA), which assigns the expected goals value of the resulting shot to the player
who made the final pass [16]. For example, if a player passes to a teammate who
shoots, the xG value of that shot is credited to the passer in the form of an xA.
    While traditional xA provide a measure of a player’s ability to create goal
scoring opportunities, it is limited in scope because it only considers the pass
immediately preceding a shot. This approach works well in situations where a
single pass leads directly to a shot, but it becomes less effective in scenarios
 Credit Attribution in Soccer Networks Using Multivariate Hawkes Processes       3

involving multiple passes in the buildup to a shot, which occur far more fre-
quently in soccer. To address this limitation, metrics such as Opta’s expected
assists (xA) [18] estimate the likelihood that a pass will become an assist re-
gardless of whether the receiver takes a shot. Another approach is to give credit
equally to every player who participated in a possession. This is the approach
taken by xGChain [10], which assigns the xG of a shot in the possession to all
of the players involved. A downside is that a player who makes the first pass
in a long passing sequence receives equal credit to the player who makes the
last pass, even though these events may be separated by multiple minutes and
dozens of passes and may contribute unequally to the shot.

2.2   Analyzing Passing Networks in Team Sports
The study of soccer passing networks, where players are represented as nodes
and passes as edges, has been widely used to identify key players within teams
and characterize a team’s play style [4]. Gyarmati and Kwak [8] use motifs in
the passing networks to characterize a team’s play style. Clemente et al. [6] use
traditional network metrics, such as degree centrality, betweenness centrality,
and closeness centrality, to identify key players and quantify their contributions.
While these metrics provide insights into player involvement, they often fail to
account for the quality or context of individual passes.
   Another line of work focuses on building probabilistic models for timestamped
event sequences in sports, including passing networks. Xin et al. [19] propose
a continuous-time network model for events in basketball, including passes.
Grieshop et al. [7] propose a continuous-time stochastic process designed to
model different aspects of a soccer match, including ball control, passing, and
pace. These models have been used for exploratory analysis of different sports
teams but have not been used for credit attribution.

2.3   Multivariate Hawkes Processes and Credit Attribution
Temporal point processes (TPPs) are often used to model timestamped events
that are observed at irregular time intervals. TPPs serve as a natural model for
events, such as passes and shots, in soccer and other sports. A TPP is character-
ized by its intensity function, which represents the instantaneous rate at which
events occur over time. A Hawkes process [9] is a self-exciting TPP where the
occurrence of an event may influence the occurrence of additional events shortly
thereafter. The influence then decays over time according to a kernel function
that is typically chosen to be an exponential function βe−β(t) .
    A multivariate Hawkes process (MHP) models multiple variables that can
mutually excite each other. This provides an interesting model for soccer events,
as the occurrence of one pass can increase the intensity of a future pass or shot.
An exponential MHP is characterized by its conditional intensity function
                                       d
                                       X       X
                   λi (t|Ht ) = µi +                       αij βe−β(t−tl ) ,
                                       j=1 tl ∈Tj ,tl <t
4       Phillip W. Kornberg and Kevin S. Xu

where Ht denotes the history (all events up to time t), µi denotes a baseline rate
at which events in variable i occur, d denotes the number of variables in the MHP
(the dimension), Tj denotes the set of times that an event in variable j occurs,
β denotes the rate of exponential decay of the influence of past events, and αij
denotes the normalized jump size such that the product αij β corresponds to the
increase in the intensity of variable i triggered by an event in variable j.
    In our proposed MHP model for soccer action sequences (see Section 4.1 for
details), each variable i corresponds to a specific pair of players: a sender is who
initiates the pass and a receiver ir . Therefore, αij measures the influence of a
pass from js → jr on a future pass from is → ir .
    An MHP can be used to compute the probability that an event l is the parent
of event k, often called the responsibility of event l for event k:

                                                     k −tl )]
                   
                    µ +Pαv(k)v(l)αβ exp[−β(t                         , 0 < l < k,
                      v(k)    t ′ <tk  v(k)v(l′ ) β exp[−β(tk −tl′ )]
             zkl =             l
                                         µv(k)                                     (1)
                    µ +P
                      v(k)            α       ′ β exp[−β(tk −t ′ )]
                                                                      , l = 0,
                             t ′ <tk   v(k)v(l )        l
                              l


where v(k) denotes the variable in the MHP for event k, and l = 0 denotes that
the event occurred from the baseline rate and is not a child of a previous event.
These responsibilities can be used to attribute how much credit event l should
be given for event k.


Credit Attribution in Event Sequences The problem of attributing credit
to multiple prior events is also encountered in online advertising, where the last
ad that a user clicks on is often assigned all of the credit if the user then makes
a purchase. This is often referred to as “last-touch attribution,” which is similar
to the attribution provided by giving an assist to the player making the final
pass before a goal. Attributing credit to multiple prior events is often referred
to as multi-touch attribution, and different data-driven algorithms have been
proposed for online advertising [13, 20].
    Recent approaches have used MHPs to model soccer action sequences in
order to assign different amounts of credit to different players. FeatHawkes [17]
represents each player as a dimension of an MHP. There is also a dimension for
shots. Last-touch credit is computed using the branching matrix, equivalent to
the excitation matrix α for an exponential MHP, which captures how strongly
one player’s actions directly trigger another player’s actions or a shot. To provide
credit for previous touches, multi-touch credit is computed using the descendant
matrix D = α(I − α)−1 , which adds up both direct and indirect chains of
influence to give each player’s overall expected contribution.
    Another MHP-based approach is proposed by Baouan et al. [2], who build
a 12-dimensional MHP representation with 11 dimensions denoting the players’
positions and a 12th dimension denoting a ball touch in a predefined danger area
around the opponent’s goal. They similarly use the branching matrix α and
descendant matrix D for last-touch and multi-touch attribution, respectively,
and use them to create direct and indirect generation of threat indices for players.
 Credit Attribution in Soccer Networks Using Multivariate Hawkes Processes     5

3     Dataset Description and Preprocessing
We use publicly available data from StatsBomb [15] and consider data from all
of the teams in La Liga over the 2015/2016 season. To construct timestamped
passing networks, we extract all pass and shot events from the raw JSON files
separately for each half and team. Separating halves avoids complications from
overlapping timestamps caused by stoppage time.
    For passes, we record the sender, receiver, time- Time Sender Receiver
stamp, and location using player IDs. For shots, we 10:00           4        0
record the shooting player and expected goals (xG). 10:02           0        2
The receiver for a shot is represented by a new goal 10:05          2        8
node rather than the opposing goalkeeper, allowing 10:07            8        1
shots to be treated as terminal actions rather than 10:09           1        0
events that could influence future passes. Fig. 1 dis-
plays a subset of one data frame and the correspond-                           4
ing directed graph.                                             2
    After constructing data frames for each half, we                     0
combine events from all matches in a season and store
each half separately. A global player index is used to     8
maintain consistent player mapping across matches.                  1
The data is then transformed from data frames into
arrays, where each key represents a sender-receiver
                                                         Fig. 1: A sequence of
pair and the corresponding value is a list of times-
                                                         passes beginning with
tamps when passes occurred between them. We add
                                                         player 4 represented as
600 seconds to the times of all events in the second
                                                         a relational event table
half to avoid the overlap with stoppage time events in
                                                         and directed graph.
the first half. This process is repeated for each match,
so the full dataset becomes a list of these arrays across the entire season.
    One challenge in transforming the data in this way was making sure that
every game uses the same set of player pairs. This is important because the
MHP compares interaction patterns across matches, so the input structure must
be consistent for each match. In our model, each team typically had around 25
players, which resulted in roughly 500 sender-receiver pairs. However, many of
these pairs either occurred very rarely, as shown in Fig. 2, or did not appear
at all in certain matches. This creates both computational and statistical issues
as rare interactions produce unstable alpha estimates. To address this issue, we
only select the 100 most frequent pairs, which represent the most common and
consistent passing interactions for each team.


4     Methods
4.1   Multivariate Hawkes Process Model of Passing Networks
We model timestamped passing networks using an exponential multivariate
Hawkes process (MHP), where each variable or dimension in the MHP corre-
sponds not to a single player, unlike in [2, 17], but to a pair of players, which
6       Phillip W. Kornberg and Kevin S. Xu




                         102



             Frequency
                         101


                         100
                               100   101                102
                                           Pair Count

Fig. 2: Frequency of passes for sender-receiver pair in Barcelona’s 2015/2016 La
Liga season, sorted in decreasing order.


we denote as a sender-receiver pair. As discussed previously, we include only
the 100 most frequent sender-receiver pairs as well as pairs where the receiver
is the goal node, so that all shots on goal are captured. Events involving other
sender-receiver pairs are excluded from training.
    We use the HawkesTorch [12] library, which allows for fast fitting of exponen-
tial MHPs using maximum likelihood. The model learns a full excitation matrix
α, where entry αij captures how a pass between sender-receiver pair j influences
a pass between sender-receiver pair i in the near future. Another model param-
eter is the vector of baseline rates µ, where µi models how frequently passes
between sender-receiver pair i occur in isolation when not caused by a prior
pass. Finally, the scalar β denotes the rate of exponential decay. To capture the
fast paced nature of a soccer match where passes occur rapidly, we choose the
decay parameter β = 0.2. With this choice, about 98% of the influence of a pass
on a future pass is gone after 20 seconds.
    Since fitting the MHP requires estimating a full excitation matrix, we eval-
uate several regularization techniques to prevent overfitting: ℓ1 , ℓ2 , and nuclear
norm. We use Optuna [1] to select optimal penalty hyperparameters, which we
compare using negative log-likelihood (NLL) on validation data. We normal-
ize by the number of events to allow for comparison across matches and use a
70/15/15 train/validation/test split. We set the range from 10−8 to 103 and run
1,000 trials. We find that the different penalty configurations have only small
effects on the test NLL, with the unregularized model achieving the lowest value.
Thus, we select the unregularized MHP model, which is the maximum-likelihood
estimate (MLE). We train for 1,000 epochs, beyond which the NLL plateaus.


Differences from Prior MHPs for Soccer Actions Rather than using play-
ers as dimensions or variables of the MHP as in [2, 17], we use pairs of players.
This helps preserve more structure than treating each player as one dimension,
as it can capture patterns at the level of the passing network, not just individ-
ual player sequences. Furthermore, it allows us to directly perform multi-touch
 Credit Attribution in Soccer Networks Using Multivariate Hawkes Processes         7

attribution through the estimated branching matrix α. This is unlike in [2, 17],
where α provides only last-touch attribution, and the descendant matrix D is
required to compute multi-touch attribution.

Smoothing Estimates A problem with the MLE is that αij = 0 if sender-
receiver pair j never occurs shortly before a sender-receiver pair i in the training
data. This would result in j receiving no credit for i, even if j occurs one second
before i in the test data. Additionally, we may observe sender-receiver pairs
that are not one of the 100 most frequent pairs and are thus not part of the
model. These pairs would also receive no credit. From a soccer perspective, this
is not realistic, as nearly any pass has at least some potential to contribute to a
subsequent shot. To address this issue, we smooth the estimated α by taking a
convex combination of the MLE and a scaled all-ones matrix:
                                                       
                                                    0.5
                            α = (1 − ϵ)αMLE + ϵ           ,
                                                    M
where M is the total number of sender-receiver pairs. We choose ϵ = 0.3 so that
the final αij value is 70% based on the MLE and 30% based on a small non-zero
value 0.5/M . The 0.5/M scaling is used to ensure the largest eigenvalue of the
scaled all-ones is less than one, ensuring a stable MHP. Smoothing using a scaled
all-ones matrix can be viewed as a uniform prior distribution and is similar to
additive smoothing techniques commonly used in language modeling [5]. The
smoothing makes the effective floor of the matrix ≈ 0.001 and ensures that an
event involving pair j occurring immediately before an event involving pair i
receives some credit, even if it is not observed in the training data. Additionally,
if the sender-receiver pair i or j is not one of the 100 most frequent pairs, its αij
                                                      MLE
value is the minimum value of α, the same as if αij        = 0.

4.2   Shot Responsibilities
Using the value of β along with the estimated α, µ, we can measure how much
a pass contributed to a subsequent shot by computing the responsibility of the
pass for the shot using (1). For each shot, we examine the 6 preceding passes
and calculate the probability that each pass contributed to the shot, along with
the probability that the shot occurred independently of any pass, i.e., l = 0 in
(1). Independently created or spontaneous shots are often a result of free kicks
and penalty kicks, where there is a large time gap between passes and the shot.
    Importantly, the model does not assign responsibility solely based on the
time gap between a pass and a shot. While the exponential decay with rate β
gives greater weight to more recent passes, the learned αij values also influence
attribution. This allows passes that historically lead to subsequent shots more
often to receive greater responsibility than more recent passes with lower αij
values. Thus, the model accounts for both temporal proximity and the learned
influence of each sender-receiver pair, providing a more nuanced attribution of
credit than a fixed global α shared across all sender-receiver pairs, which would
assign credit primarily on the time between events.
                          8              Phillip W. Kornberg and Kevin S. Xu

                          4.3       Expected Goal Involvements (xGI)
                          The shot responsibility values form the basis of a new metric we propose called
                          expected goal involvements (xGI), which measures a player’s involvement in
                          creating goal scoring opportunities based on their passes. Rather than treating
                          passes as independent actions or assigning all credit to the final pass, xGI dis-
                          tributes the expected goal (xG) value of a shot, which is part of the StatsBomb
                          data [15], among all players who contributed to the attacking sequence:
                                                                                     m
                                                                                     X
                                                                    xGIls =                   (xG)k · zkl ,
                                                                                     k=1

                          where m denotes the number of shots in a game, and ls denotes the sender of
                          pass l. This allows players who initiate or advance dangerous plays, but do not
                          provide the final pass, to receive credit for their involvement.


                          5       Results
                          5.1       Barcelona 2015/2016 Analysis
                          Model Fitting After filtering the data to include only the 100 most frequent
                          pairs, we fit the MHP on a total of 17,645 pass and shot events. Fig. 3 de-
                          picts a subset of the estimated α matrix, which shows the impact of passes on
                          future shots by Luis Suárez. Pairs such as (Neymar → Suárez) and (Messi →
                          Suárez) have the largest αij values, which is expected since passes received by
                          Suárez are more likely to directly contribute to shots taken by Suárez. However,
                          the model assigns nonzero αij values to several pairs where the receiver is not
                          Suárez, such as (Messi → Busquets). This indicates that passes not directly in-
                          volving Suárez can still contribute indirectly to future shots by Suárez through
                          subsequent passes, which allows for multi-touch attribution.

                          Shot Responsibilities Using the entire α matrix, we compute shot responsi-
                          bilities for each individual match. Table 1 shows two passing sequences alongside
                          the responsibility values produced by our model. Notice that the differences in
                          shot responsibilities depend both on the αij value and the time gaps between
                          passes. For the shot in Table 1a, the responsibilities are distributed relatively

                                                                    Goal Alpha Values for Suárez Goal (Barcelona)
Goal Pair




            Suárez Goal              0.076              0.035                           0.046                             0.039           0.049
                               Neymar Suárez         Alves Suárez                Busquets Suárez                       Alba Suárez    Iniesta Suárez
                                                                    Goal Alpha Values forPass Pairs
                                                                                           Suárez   Goal (Barcelona)
Goal Pair




            Suárez Goal              0.033              0.004                           0.013                             0.090           0.002
                                Rakiti    Suárez    Messi Neymar                  Messi Busquets                       Messi Suárez   Messi Rakiti
                                                                                        Pass Pairs

                              Fig. 3: Subset of αij values for passes leading up to a shot by Luis Suárez.
 Credit Attribution in Soccer Networks Using Multivariate Hawkes Processes            9


Table 1: Examples of shots with (a) widely distributed and (b) concentrated
responsibilities from our proposed MHP model. Responsibilities from a temporal
decay (TD) baseline model do not show much difference between the two shots.

              (a) Widely distributed shot responsibility (xG = 0.55)
                                          Responsibilities
 Time    Event                       TD Baseline MHP Model           xGI      αij
 0:35    Munir Shot                      -               -             -
 0:34    Neymar Pass to Munir          0.473           0.329        0.1810   0.0013
 0:30    Suárez Pass to Neymar        0.213           0.268        0.1474   0.0023
 0:29    Neymar Pass to Suárez        0.174           0.136        0.0748   0.0014
 0:26    Roberto Pass to Neymar        0.096           0.086        0.0473   0.0016
 0:20    Mathieu Pass to Roberto       0.029           0.020        0.0110   0.0013
 0:17    Bravo Pass to Mathieu         0.015           0.011        0.0061   0.0013
   -     Spontaneous Shot                -             0.150           -        -


                 (b) Concentrated shot responsibility (xG = 0.12)
                                          Responsibilities
 Time    Event                       TD Baseline MHP Model           xGI      αij
 82:57   Messi Shot                      -                -            -
 82:56   Piqué Pass to Messi          0.559           0.649        0.0779   0.0057
 82:52   Rakitić Pass to Piqué       0.251           0.075        0.0090   0.0015
 82:48   Busquets Pass to Rakitić     0.112           0.031        0.0037   0.0014
 82:45   Alba Pass to Busquets         0.062           0.018        0.0022   0.0014
 82:36   Messi Pass to Piqué          0.010           0.003        0.0004   0.0013
 82:33   Rakitić Pass to Messi        0.006           0.029        0.0035   0.0249
   -     Spontaneous Shot                -             0.195           -        -


evenly between the two passes leading up to the shot by Munir, as the penul-
timate pass (Suárez → Neymar) has the higher αij value than the final pass
(Neymar → Munir). For the shot in Table 1b, the pass (Piqué → Messi) is given
by far the highest responsibility due to having both a much higher αij value
compared to the other passes and being the final pass.

Comparison with Temporal Decay Baseline To test whether the learned
excitation matrix α provides meaningful attribution beyond temporal proximity
alone, we compare our proposed MHP model with a simple temporal decay
(TD) baseline. The baseline considers the same six passes preceding each shot
and computes responsibilities purely based on an exponential temporal decay
e−β(t−tl ) . The responsibilities for the TD baseline are normalized to sum to 1
so that they are directly comparable to the MHP model, except that it does
not have a baseline µ. Notice from Table 1 that the TD model’s responsibilities
between the two shots are very similar, as it considers only the time gaps between
the passes and the shot, unlike our proposed MHP model.
10             Phillip W. Kornberg and Kevin S. Xu


                         Table 2: Top 5 La Liga players by average xGI per game
     Player                                              Team                              xGI                 Games Played                               xGI Per Game
     Neymar Junior                                       Barcelona                         15.5                    34                                         0.457
     Lionel Messi                                        Barcelona                         12.4                    33                                         0.376
     Jorge Resurrección                                 Atlético Madrid                  11.1                    35                                         0.316
     Luis Suárez                                        Barcelona                         11.1                    35                                         0.316
     Manuel Nolito                                       Celta Vigo                        8.39                    29                                         0.289
                        Barcelona 2015/2016 Passing Network                                                               Levante UD 2015/2016 Passing Network

                                               Neymar                                                                                              Morales
                        Adriano                                                                                           Joan Verdú                           Ghilas
                                                                   Muñoz
                                                                                                                Rossi                                                    Deyverson
                                                                                        Alpha Influence                                                                                             Alpha Influence
                                                                                                    1.2                                                                                                         1.2
                                                                                                                                              Feddal                               Casadesús
                           Iniesta
                                              Rakitic                                              1.0                                                                                                         1.0
                                                                              Suarez                                    Camarasa
                Dani                                                                             Juanfran                                                             Verza
                Alves                                                                              0.8                                                                                                         0.8
                                                        Busquets
  Aleix                                                                                            0.6                                                                                      Pedro              0.6
  Vidal                                                                                           Iván                                                                                      López
                                                                                 Arda            López                                                                  Antonio
                                                                                                   0.4                                                                  García                                 0.4
                                                     Javier                                          José
     Mathieu                         Messi                                                         0.2María                                                                                                    0.2
                                                                            Sergi                                                  Lerma
                                                                           Roberto                 0.0                                                                            Medjani                      0.0
                                                                                                               David
                                                                                                              Navarro
               Alba                          Pique                                                                                                                        Simao
                                                                                                                                    Rubén                    Rubén
                                                         Mohamed                                                                   Martínez      Mariño      García



                             (a) Barcelona                                                                                    (b) Levante UD

Fig. 4: 2015/2016 La Liga influence networks for the 100 most frequent passing
pairs. Edge width and color denote the total influence that a pass from the
sender has on the receiver playing a pass shortly thereafter.


5.2        La Liga 2015/2016 Analysis

We can look at the xGI of each player across the entire season to understand their
expected involvement in creating goal scoring opportunities. Many of the players
appearing in Table 2 are well known for their ability to create chances. Lionel
Messi and Neymar Junior, who have the highest xGI per game, consistently lead
players in xA and key passes.
    Out of the 20 teams in La Liga, Barcelona has the highest mean αij value of
0.0050, while Levante UD has one of the lowest at 0.0040. Fig. 4 shows the in-
fluence networks for different players on Barcelona and Levante UD. The weight
of the edge for a sender-receiver pair (s, r) is given by the sum of all αij en-
tries for all j corresponding to sender-receiver pairs (s, :) and i corresponding to
sender-receiver pairs (r, :), where the : notation denotes all of the nodes. Unlike
a passing network, where the edge weight measures the number of passes from a
sender to a receiver, the influence network measures the total influence that the
sender has on the receiver playing a pass in the future.
    From Fig. 4, Barcelona shows overall stronger influences between players
compared to Levante UD. In particular, Barcelona’s network has a stronger
 Credit Attribution in Soccer Networks Using Multivariate Hawkes Processes        11

core, while Levante UD’s network has more players on the periphery with only
weak influences. This is consistent with the parameter estimates for the model.


6   Conclusion
This paper outlines a new approach to better characterize player involvement in
creating goal scoring opportunities in soccer. Instead of attributing credit only
to the final pass before a shot, our method distributes credit across multiple
passes in the buildup. We accomplish this by modeling passing networks using
an MHP and using a branching probabilities equation to compute shot responsi-
bilities. Then, we introduce the expected goal involvements (xGI) statistic, which
distributes xG based on player’s level of responsibility for creating the shot.

Limitations Our model for credit attribution has several limitations. The first
is the basic assumption—a pass (s → r) that frequently leads to a pass (s′ → r′ )
shortly thereafter should be given more credit than a pass (u → v) that infre-
quently leads to (s′ → r′ ). This method of attributing credit based on frequent
occurrences from the training data may not be applicable to all application set-
tings, and furthermore, the training data may not be sufficiently long to observe
many such occurrences. Additionally, infrequent passes that are not among the
top 100 most frequent pairs are currently excluded from the MHP model and are
assigned the minimum αij ≈ 0.001. Both of these problems could potentially be
alleviated by developing MHP-based network models that can group together dif-
ferent nodes, such as the multivariate community Hawkes (MULCH) model [14].
Unfortunately, the MULCH model is not flexible enough in its current form for
multi-touch attribution and can only perform last-touch attribution.
    Another limitation of our analysis is the manual selection of β. Different β
values will result in a different α matrix, and in turn, different shot responsibili-
ties. Our analysis used β = 0.2, which we felt was a reasonable choice because it
leads to 98% of the influence of a pass on future passes being gone after 20 sec-
onds, which is a long time in a soccer match. However, β could also reasonably
be set to other values such as 0.1 or 0.5 to reflect different time scales.


7   Acknowledgments
This material is based upon work supported by the National Science Foundation
grant IIS-2318751. This work was also supported by a summer research award
provided by the CWRU Undergraduate Research Office.


References
 1. Akiba, T., Sano, S., Yanase, T., Ohta, T., Koyama, M.: Optuna: A next-generation
    hyperparameter optimization framework. In: Proc. 25th ACM SIGKDD Int. Conf.
    Knowl. Disc. Data Min., pp. 2623–2631 (2019)
12      Phillip W. Kornberg and Kevin S. Xu

 2. Baouan, A., Coustou, S., Lacome, M., Pulido, S., Rosenbaum, M.: Generation of
    threat: crediting football players for creating dangerous actions in an unbiased way.
    J. Quant. Anal. Sports (2025)
 3. Buldú, J.M., Busquets, J., Martı́nez, J.H., Herrera-Diestra, J.L., Echegoyen, I.,
    Galeano, J., Luque, J.: Using network science to analyse football passing networks:
    Dynamics, space, time, and the multilayer nature of the game. Front. Psychol. 9,
    1900 (2018)
 4. Caicedo-Parada, S., Lago-Peñas, C., Ortega-Toro, E.: Passing networks and tactical
    action in football: A systematic review. Int. J. Enviro. Res. Public Health 17(18),
    6649 (2020)
 5. Chen, S.F., Goodman, J.: An empirical study of smoothing techniques for language
    modeling. Comput. Speech Lang. 13(4), 359–394 (1999)
 6. Clemente, F.M., Sarmento, H., Aquino, R.: Player position relationships with cen-
    trality in the passing network of world cup soccer teams: Win/loss match compar-
    isons. Chaos, Solitons & Fractals 133, 109,625 (2020)
 7. Grieshop, N., Feng, Y., Hu, G., Schweinberger, M.: A continuous-time stochastic
    process for high-resolution network data in sports. arXiv preprint arXiv:2303.01318
    (2023). URL https://arxiv.org/abs/2303.01318
 8. Gyarmati, L., Kwak, H., Rodriguez, P.: Searching for a unique style in soccer.
    arXiv preprint arXiv:1409.0308 (2014). URL https://arxiv.org/abs/1409.0308
 9. Laub, P.J., Lee, Y., Taimre, T.: The Elements of Hawkes Processes. Springer
    International Publishing, Cham (2021)
10. Lawrence, T.: Introducing xGChain and xGBuildup (2018). URL https://www.
    hudl.com/blog/introducing-xgchain-and-xgbuildup
11. Lucey, P., Bialkowski, A., Monfort, M., Carr, P., Matthews, I.: Quality vs quantity:
    Improved shot prediction in soccer using strategic features from spatiotemporal
    data. In: Proc. 9th Annu. MIT Sloan Sports Anal. Conf. (2015)
12. Raza, A., Smith, H.: Massively parallel exact inference for Hawkes processes. arXiv
    preprint arXiv:2604.01342 (2026). URL https://arxiv.org/abs/2604.01342
13. Shao, X., Li, L.: Data-driven multi-touch attribution models. In: Proc. 17th ACM
    SIGKDD Int. Conf. Knowl. Discov. Data Min., pp. 258–264 (2011)
14. Soliman, H., Zhao, L., Huang, Z., Paul, S., Xu, K.S.: The Multivariate Community
    Hawkes model for dependent relational events in continuous-time networks. In:
    Proc. 39th Int. Conf. Mach. Learn., pp. 20,329–20,346 (2022)
15. StatsBomb: StatsBomb open data (2026). URL https://github.com/hudl/open-
    data
16. The Football Analyst: Expected assists (xA) – football statistics ex-
    plained (2025).        URL https://the-footballanalyst.com/expected-assists-xa-
    football-statistics-explained/
17. Verronneau, R., Croissant, L., Vieille, B., Perchet, V.: The path to the goal:
    Feature-augmented Hawkes processes for event-level attribution (2026). URL
    https://hal.science/hal-05284437. Preprint
18. Whitmore, J.: What are expected assists (xA)? https://theanalyst.com/articles/
    what-are-expected-assists-xa (2021)
19. Xin, L., Zhu, M., Chipman, H.: A continuous-time stochastic block model for bas-
    ketball networks. Ann. Appl Stat. pp. 553–597 (2017)
20. Xue, T., Zhai, P., Yang, Y., Li, Y.: Deep learning for multi-touch attribution in
    online advertising: A comparative study. Inf. Syst. Front. pp. 1–35 (2026)
