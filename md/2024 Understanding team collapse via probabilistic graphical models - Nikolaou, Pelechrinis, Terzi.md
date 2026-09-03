<!-- source: 2024 Understanding team collapse via probabilistic graphical models - Nikolaou, Pelechrinis, Terzi.pdf -->
<!-- arXiv:2402.10243v1 [physics.soc-ph], 2024-02-14 (v1); this file converted from the arXiv PDF via pdftotext + scripted reflow, 2026-09-02 -->
<!-- machine conversion: equations, tables and figures are NOT preserved - consult the PDF for those -->

Understanding team collapse via probabilistic graphical models Iasonas Nikolaou

Konstantinos Pelechrinis

Evimaria Terzi

Boston University Boston, USA nikolaou@bu.edu

University of Pittsburgh Pittsburgh, USA kpele@pitt.edu

Boston University Boston, USA evimaria@bu.edu

## Abstract

In this work, we develop a graphical model to capture team dynamics. We analyze the model and show how to learn its parameters from data. Using our model we study the phenomenon of team collapse from a computational perspective. We use simulations and real-world experiments to find the main causes of team collapse. We also provide the principles of building resilient teams, i.e., teams that avoid collapsing. Finally, we use our model to analyze the structure of NBA teams and dive deeper into games of interest.

CCS CONCEPTS • Information systems → Data mining; • Computing methodologies → Learning in probabilistic graphical models; • Theory of computation → Social networks.

KEYWORDS team collapse, team dynamics, probabilistic graphical models ACM Reference Format: Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi. 2023. Understanding team collapse via probabilistic graphical models. In Proceedings of ACM KDD Conference 2024 (KDD ’24). ACM, New York, NY, USA, 25 pages. https://doi.org/XXXXXXX.XXXXXXX

## Introduction

What are the reasons that a (sports) team severely under-performs and eventually collapses? Are some teams more prone to collapse than others? Are there some guiding principles for building resilient teams? In this paper, we make a significant step towards addressing these questions. We achieve this by introducing a probabilistic graphical model that assumes the following: at any time 𝑡 a player’s hidden (mental) state depends on the player’s own hidden state at 𝑡 − 1 and the observed performances of all team members at 𝑡 − 1. Consequently, a team collapse happens at time 𝑡 if more than a certain percentage of the team’s players are in a “low" hidden (mental) state at 𝑡. Our model parameters enable us to encode different types of dependencies among team members. For example, there may be players whose performance is only affected by their own hidden/observed state and is unaffected by the performance of others. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. KDD ’24, August 25-29, 2024, Barcelona, Spain © 2023 Association for Computing Machinery. ACM ISBN 978-1-4503-XXXX-X/18/06. . . $15.00 https://doi.org/XXXXXXX.XXXXXXX

We call such players pillars. On the other hand, non-pillar players are more susceptible to be influenced by their teammates’ observed performance. An interesting question we explore is to what extend having more or less pillars affects the resilience of a team and influences its collapse probability. Moreover, is it just the number of pillars important or their dependency patterns as well? We believe that being able to answer questions like this can inform roaster-building decisions. From the computational point of view, we show that we can use the Expectation-Maximization (EM) framework to learn the parameters of our model. In particular, we borrow several ideas from probabilistic graphical models [15] and Hidden Markov Models (HMMs) [3] in order to implement the expectation and the maximization steps of EM. In practice, we show that despite the large number of parameters of our model, EM can learn those parameters effectively in a small number of iterations. Using real data from National Basketball Association (NBA) games (season 2021-22), we deploy our EM algorithm to learn the parameters of our model for all NBA teams. We identify some interesting dependencies among players and demonstrate that pillar players do not always coincide with players widely acknowledged as “stars". Moreover, our framework allows us to identify team collapses in various games and further analyze them in order to find the reasons for which these collapses happened. We believe that these results provide useful insights on team dynamics and can be used from team psychologists and General Managers in order to safeguard teams from collapses. Overall, our model allows us to capture complex team dynamics and can be used as a tool by experts in team sports to analyze their teams’ compositions, simulate the performance of different compositions and use these insights to create teams that are more resilient to team collapses. Although related to other probabilistic models proposed in the literature (see related work for an extended discussion), the exact details of our model and the corresponding computational problem associated with the learning of its parameters are novel. This is because, to the best of our knowledge, our model is the first probabilistic graphical model that is tailored to capture how teammate dependencies give rise to team collapses. Related work: During the last decade, the ability to collect multiple player-tracking data has led to a growth of computational approaches for evaluating players, teams and team strategies in a variety of sports [6, 9–11, 17, 19, 20, 28, 29, 35, 36]. From the application point of view, our work falls into this general area and it relates to work on sport analytics and athlete choking. From the computational point of view, our work is related to existing work on probabilistic models and interconnected Hidden Markov Models (HMMs). We summarize these connections below.

KDD ’24, August 25-29, 2024, Barcelona, Spain

Team and player performance ratings: One of the main tasks that the field of sports analytics has dealt with is that of team and player performance evaluation. This typically is achieved through models that learn team and player ratings, which are then used in match prediction and gambling or to help teams identify players to acquire. The simplest team ratings are based on regression methods [4, 16, 32, 34]. More sophisticated ones use network analysis of the “whowins-whom” network [22, 25], while others use latent space models to learn an embedding for each team that will help obtain a team ranking [7, 8, 24]. Similarly, for evaluating players the traditional approach for obtaining player ratings is using regression based approaches [18, 27, 31] to model the score differential during a game possession as a function of the players on the court/pitch. These ratings ignore dependencies between the players and make the implicit assumptions that player ratings are additive, i.e., a team is the sum of the individual players. As such, it is hard for these type of models to help us understand and explain situations where a team significantly over or under performs its expectation within a game. In our work, we explicitly consider the dependencies between players and we develop a framework that can explain how these dependencies can lead to a team collapsing. Athlete’s “choking”. : The common belief is that super-star athletes shine when the stakes are high, while athletes in lower tiers severely under perform under pressure, i.e., they “choke” or collapse. While there has been some literature on players performance and decision-making under pressure, this has traditionally been in the field of sports psychology [1, 23, 26]. The vast majority of the literature has been on the complementary phenomenon of “clutch” players, i.e., players that deliver when the stakes are high. The majority of this literature indicates that individual clutch performance is highly noisy [2, 30, 33]. One of the few computational studies on player performance under pressure is that from Bransen et al. [5] who develop metrics to evaluate the performance of individual soccer players under situations with high mental pressure. In a similar direction, Dohmen [12] focused on studying penalty shootouts and found that players of the home team are more likely to choke; the same study identified no evidence in their data that high stakes induce choking. A detailed overview of mechanisms and potential moderators of choking in sport is further provided by Hill et al. [14]. All the above work considers individual players’ choking. Our work enhances this literature by studying the team effects of individual performance, as well as, the possible influence they exert on the performance of their teammates and how this translates to a team’s ability to withstand, or not, periods of subpar performance of individual players. Computational work on interacting HMMs. Our model is inspired by HMMs [15] and in particular work on “coupled" HMMs [13, 21] where the nodes of a network are HMMs themselves influenced by the other nodes via the edges of the network. The most related to ours is the work of Pan et al. [21]. Motivated by applications of influence in social media and disease propagation, Pan et al. propose a model very similar to ours, where the hidden state of every individual at time step 𝑡 depends on their own hidden state at 𝑡 − 1 and the others’ hidden states at 𝑡 − 1. Contrary to this, our model assumes that an individual’s hidden state at 𝑡 depends on their own hidden state at 𝑡 − 1 and the others’ observed states at

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

𝐻 11

𝐻 31

𝐻 21 𝑂 11 𝑂 12

𝐻 12

𝑂 31

𝑂 21

𝑂 32

𝑂 22 𝐻 22

𝐻 32

Figure 1: Graphical model representation of our model for 𝑛 = 2 entities and 𝑇 = 3 timesteps 𝑡 − 1. From the application point of view this difference is important: players in a team don’t know the hidden state of their teammates; they only know their teammates’ observed performance. Thus, our model is better suited for our application. The computational consequences of this difference are also important: we are able to compute (and sample) from the posterior probability distribution during the E-step of our EM algorithm, while they cannot as they have to deploy variational inference techniques.

THE MODEL

We start this section by giving some notational conventions we follow throughout the paper. Then, we give a high-level description of our model, and provide example instantiations that enable us to better convey its expressivity.

2.1

Notational conventions

For the rest of the paper, we establish the following notation: we use uppercase letters to denote random variables, e.g. 𝑋 , 𝑂, 𝐻 and lowercase letters to denote non-random quantities, e.g. 𝑥, 𝑜, ℎ. When the random variables are vectors we denote them with bold uppercase letters X, O and H and the corresponding vector non-random quantities x, o and h. For a vector random (resp. nonrandom) variable X (resp. x), we denote its 𝑖-th coordinate with 𝑋 𝑖 (resp. 𝑥 𝑖 ). We also use uppercase calligraphic letters to denote (non-random) matrices, e.g. M, N . All matrices in this paper are non-random quantities. In some cases, we abuse notation, and we also use use uppercase calligraphic letters to denote sets, e.g. H , and | · | to denote their cardinality. We use Pr(𝑋 = 𝑥) to denote the probability of random variable 𝑋 taking the value 𝑥. For brevity, when clear from context, we abuse the notation and use Pr(𝑋 ) instead of Pr(𝑋 = 𝑥).

2.2

Model description

Our team model aims to capture the influence that the team entities/players have on each other. The model is inspired by Hidden Markov Models and their interaction as described by Pan et al.[21]. Despite this initial inspiration, our model deviates from the aforementioned work in some key ways which have significant application and computational consequences, discussed in the last paragraph of the Related work. Entities: The model assumes of 𝑛 entities. At time step 𝑡 = 1, . . . ,𝑇 , each entity 𝑖 is associated with a hidden (not observed) state 𝐻𝑡𝑖 ∈ H , where H is a discrete finite set of hidden states with cardinality 𝑛ℎ . At 𝑡, entity 𝑖 emits an observed signal 𝑂𝑡𝑖 ∈ O, where O is a discrete

Understanding team collapse via probabilistic graphical models

KDD ’24, August 25-29, 2024, Barcelona, Spain

finite set of observed states with cardinality 𝑛𝑜 . We assume that we have observations for 𝑇 timesteps. In our case, the entities correspond to the players, members of a team. Since we consider basketball teams we have 𝑛 = 5. The hidden states can be thought of as the psychological/mental states of each player. In our experiments, we define 3 hidden states H = {−1, 0, 1} where −1 is the lowest (worst), 0 is the average and 3 is the highest (best) possible mental state of a player. The observed states capture the performance of each player during a game. We again experiment with 3 observed states O = {−1, 0, 1}; 0 corresponds to a player performing within their average performance, 1 (resp. −1) corresponds to a player’s performance above (resp. below) his/her expected performance. We give the details of how we set those in real data in Section 5. Model parameters: The key assumption of our model is that the hidden state 𝐻𝑡𝑖 of an entity 𝑖 at time 𝑡 depends on the observed states of all entities at time 𝑡 − 1, denoted by O𝑡 −1 , as well as 𝐻𝑡𝑖 −1 (i.e., the hidden state of 𝑖 at time 𝑡 − 1). Figure 1 shows the graphical model representation of our model for 𝑛 = 3 and 𝑇 = 3. Central for our model is the computation of the conditional probability Pr(𝐻𝑡𝑖 | O𝑡 −1, 𝐻𝑡𝑖 −1 ). In general, computing this probability is hard due to the exponential state space. Thus, we adopt the following simplifying assumption: Pr(𝐻𝑡𝑖 | O𝑡 −1, 𝐻𝑡𝑖 −1 ) = 𝑛 ∑︁ 𝑗 𝑅𝑖 𝑗 × Infl(𝐻𝑡𝑖 | 𝑂𝑡 −1 ) + |{z} | {z } 𝑗=1 tie strength

influence 𝑗→𝑖

(1) 𝑟𝑖 × Infl(𝐻𝑡𝑖 | 𝐻𝑡𝑖 −1 ) | {z }

,

previous hidden state influence

Í where 𝑅𝑖 𝑗 ’s and 𝑟𝑖 are convex coefficients; i.e., 𝑛𝑗=1 𝑅𝑖 𝑗 + 𝑟𝑖 = 1 and 𝑅𝑖 𝑗 , 𝑟𝑖 ≥ 0. For brevity, we also use vector R𝑖 = (𝑟𝑖 | 𝑅𝑖1, . . . , 𝑅𝑖𝑛 ) to store the convex coefficients that appear in Eq. (1). Finally, we use R to denote the 𝑛 × (𝑛 + 1) matrix that contains all 𝑛 R𝑖 vectors as its rows. Note that R is an important parameter as it encodes the structure of influence within the team. In Section 5 this is the matrix we are inspecting in order to analyze the structure of the teams we consider. We refer to R as the team structure. 𝑗 Infl(𝐻𝑡𝑖 = ℎ | 𝑂𝑡 −1 = 𝑜) corresponds to the influence that 𝑗 𝑂𝑡 −1 = 𝑜 has on 𝐻𝑡𝑖 = ℎ. We store these influence values in 𝑛𝑜 × 𝑛ℎ 𝑗 matrices M𝑖 𝑗 = Infl(𝐻𝑡𝑖 | 𝑂𝑡 −1 ). Similarly, Infl(𝐻𝑡𝑖 = ℎ | 𝐻𝑡𝑖 −1 = ′ ℎ ) corresponds to the influence that 𝐻𝑡𝑖 −1 = ℎ ′ has on 𝐻𝑡𝑖 = ℎ. For notational convenience, we define an 𝑛ℎ × 𝑛ℎ matrix N 𝑖 storing these influence values; i.e., N 𝑖 = Infl(𝐻𝑡𝑖 | 𝐻𝑡𝑖 −1 ). We assume that both matrices M𝑖 𝑗 and N 𝑖 are row-stochastic. One may be tempted to interpret these influence values as prob𝑗 𝑗 abilities and assume that Infl(𝐻𝑡𝑖 | 𝑂𝑡 −1 ) = Pr(𝐻𝑡𝑖 | 𝑂𝑡 −1 ) and 𝑖 𝑖 𝑖 𝑖 Infl(𝐻𝑡 | 𝐻𝑡 −1 ) = Pr(𝐻𝑡 | 𝐻𝑡 −1 ). In Appendix A.2 we show that this is not true and that the Infl(·) values are not necessarily probabilities. In order to establish that our model is well-defined we show the following lemma, with proof in Appendix A.1: Lemma 1. Pr(· | O𝑡 −1, 𝐻𝑡𝑖 −1 ) induces a probability law.

Finally, we need to specify the emission probabilities Pr(𝑂𝑡𝑖 |𝐻𝑡𝑖 ) that connect the hidden state of an entity to its observed state. We store those in matrix: E𝑖 = Pr(𝑂𝑡𝑖 |𝐻𝑡𝑖 ). Matrices M𝑖 𝑗 , N 𝑖 , R and E𝑖 are the parameters of our model denoted by 𝚯 = {M𝑖 𝑗 , N 𝑖 , R, E𝑖 | 𝑖, 𝑗 ∈ [𝑛]}. These parameters fully describe our model and each instantiation of the parameters corresponds to a different team profile. In many practical applications it is reasonable to assume that matrices M𝑖 𝑗 are the same for all 𝑗 ∈ [𝑛]. In such cases we write M𝑖 , instead of M𝑖 𝑗 . Simplifying the model even further we may have all entities to share the same M matrix. In practice, it is also reasonable to assume that there is a single N , and E shared among all entities. In our experiments we make such simplifying assumptions assuming that its parameters are 𝚯 = {M, N, R, E}.

2.3

Team collapse

Given the above model, we can now formally define the hidden and the observed team states and the notions of player choking and team collapse. Definition 1. The hidden (resp. observed) team state is the average hidden (resp. observed) state of the team’s players. Definition 2. A player 𝑖 is in a chocking state at time 𝑡, if 𝐻𝑡𝑖 = −1, i.e., the player is in the lowest possible hidden state. Definition 3. A team is in an 𝛼-collapse state at time 𝑡, if 𝛼 fraction of the team’s players are in a chocking state at time 𝑡; for 𝛼 ∈ [0, 1]. We use these definitions of player choking and team collapse when analysing the expressivity of our model in Section 3 and when doing experiments with data from NBA teams in Section 5.

EXPLORING TEAM PROFILES

In this section, we experimentally evaluate how prone are different team profiles to team collapse. For this, we focus on a few basic team profiles, i.e., different instantiations of the model parameters Θ = {M, N, R, E}1 . Then, we generate data using the instances of Θ we consider and study different properties of the corresponding team profile. These properties include the average hidden (resp. observed) team state (Def. 1) and the probability that a team gets into a collapse state (Def. 3). The goal of this section is not only to study the properties of the particular profiles we are considering, but also demonstrate how our model can be used by experts in team sports to analyze different team compositions and their robustness to team collapses.

3.1

Team profiles

Below we describe the design principles for the team profiles we experiment with in the main body of the paper; a more extensive list of team profiles as well as some specific instances of the parameters are also shown in Appendix B. Setting M: Matrix M captures the influence of everyone’s observed states to the hidden state of a player. When designing M, we assume that M (𝑜 = ℓ, ℎ = ℓ) > M (𝑜 = ℓ, ℎ = ℓ ′ ) for all ℓ ≠ ℓ ′ and ℓ, ℓ ′ ∈ {−1, 0, 1}. That is, when observing a state that is similar 1We

focus on the simplified version of the model.

KDD ’24, August 25-29, 2024, Barcelona, Spain

Team collapse probability vs Team profile

Setting R: Parameters R𝑖 = (𝑟𝑖 | 𝑅𝑖1, · · · , 𝑅𝑖𝑛 ) for all 𝑖 ∈ [𝑛] assign weights to the influence matrices M and N (see Eq. (1)). We consider different scenarios for R𝑖 :

Team collapse probability

0.06

• Rh : All players depend on their previous hidden state. That is, 𝑟𝑖 = 1, ∀𝑖 ∈ [𝑛] and 𝑅𝑖 𝑗 = 0, ∀𝑖, 𝑗 ∈ [𝑛]. We denote the profile that corresponds to this R with H.

• R kH : There are 𝑘 pillar players 𝑃 that affect all others, but all non-pillar players are also affected by their hidden states. That is, 𝑟𝑖 = 1 for all 𝑖 ∈ 𝑃, 𝑟𝑖 > 0 for all 𝑖 ∉ 𝑃 and 𝑅𝑖 𝑗 = (1 − 𝑟𝑖 )1/|𝑃 | for all 𝑖 ∉ 𝑃 and 𝑗 ∈ 𝑃. In our experiments we set 𝑟𝑖 = 0.5 for all 𝑖 ∉ 𝑃. • R kD : In this case, there are again 𝑘 pillar players 𝑃 (as in R𝑘 , but this time they depend on each other. That is, for every 𝑖 ∈ 𝑃 0 < 𝑟𝑖 < 1 and 𝑅𝑖 𝑗 = (1 − 𝑟𝑖 )1/|𝑃 | for every 𝑖, 𝑗 ∈ 𝑃. In our experiments we again set 𝑟𝑖 = 0.5. Setting E: Matrix E controls the emission probabilities. We assume that the observed states are strongly correlated with hidden states. That is, E (𝑜 = ℓ, ℎ = ℓ) > E (𝑜 = ℓ, ℎ = ℓ ′ ) all ℓ, ℓ ′ ∈ {−1, 0, 1} and ℓ ≠ ℓ ′ . For example, if a player is in a poor mental state, we expect their performance (observed state) to also be poor low. Since we do not vary M, N and E, the instantiations of R give rise to different team profiles. Thus, we have the following mappings between the R instances and team-profile names: Rh → H, Rho → HO, R𝑘 → kPillars(kP), R kH → kPillars+H(kP + H) and R kD → kPillars+D(kP + D).

3.2

Simulations

In order to better understand our models we create data that correspond to 7 distinct team profiles; for a larger set of team profiles see Appendix B.2. Using these profiles we generate 1000 datasets for each profile, where each dataset has 𝑛 = 5, 𝑇 = 100 and every player 𝑖 ∈ [𝑛] starts from hidden state 𝐻 1𝑖 = 0.

0.04 0.03 0.02 0.01

• Rho : All players depend only on their previous hidden and observed states. That is, 𝑟𝑖 > 𝑅𝑖𝑖 > 0, ∀𝑖 ∈ [𝑛] and 𝑅𝑖 𝑗 = 0, ∀𝑖, 𝑗 ∈ [𝑛]. For our experiments we use 𝑟𝑖 = 0.7 and 𝑅𝑖𝑖 = 0.3, for all 𝑖 ∈ [𝑛]. • R𝑘 : There are 𝑘 pillar players 𝑃 that affect all others; i.e., 𝑟𝑖 = 𝑅𝑖𝑖 = 0 and 𝑅𝑖 𝑗 = 1/|𝑃 | for all 𝑖 ∉ 𝑃 and 𝑗 ∈ 𝑃 and 𝑟𝑖 = 1 for 𝑖 ∈ 𝑃.

0.05

Team profiles

3P

2P + D

2P

1P + H

H

0.00

1P

Setting N : Matrix N captures the influence of a player’s hidden state at 𝑡 − 1 to their own hidden state at 𝑡. Our assumption is that each player is inclined to stay in the same hidden state; i.e., N (ℎ, ℎ) > N (ℎ, ℎ ′ ), for all ℎ ≠ ℎ ′ and ℎ, ℎ ′ ∈ H .

In Appendix B.3 we show the hidden and observed team states for the profiles we mention above and others we consider in the appendix. The summary of the results is the following: in almost all cases the hidden and the observed team states follow closely one another. All teams’ states converge to the expected performance (0). Some differences are observed between profiles with respect to the 25-75 percentiles of the values we get in the simulations. Probability of team collapse. In order to empirically estimate the probability of a team collapse for a given team, we count all the times the team collapsed in the simulations and divide by the total number of samples (1000 × 100 = 105 ). In these experiments, we consider that 𝛼 = 1 (see Dfn. 3); i.e. a team collapses if all its players have choked. In Fig. 10 we show the team-collapse probability for the different team profiles we considered.

HO

to their hidden state, the players do not change their hidden state. Moreover, M (𝑜 = ℓ, ℎ = ℓ ′ ) is monotonically decreasing with the difference |ℓ − ℓ ′ |. Intuitively, this means that a player’s hidden state gets affected less by observed states that are very different from his/hers current hidden state. For the experiments we show here we assume that M (𝑜 = ℓ, ℎ = ℓ) is the same for all values of ℓ ∈ {−1, 0, 1}. In this scenario any observed state of any player influences the others to stay in the corresponding hidden state. The particular matrix we used for our simulations in shown in Appendix B.1.

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

Figure 2: Team collapse probability vs team profile First, we observe that when all players are completely unaffected by other players (profiles H and HO), then the team rarely collapses. In this case, the only way for a collapse to occur is all players independently under-performing at the same time. In general, adding dependence on the hidden state of the players, i.e., making the players more self-dependent results in a more resilient team. We also observe that the when there is one pillar in the team (profiles 1Pillar and 1Pillar+H), the team has a single point of failure. That is, when the pillar happens to under-perform, the rest of the players are negatively affected and transition to their lowest mental (hidden) state. Subsequently, these players also under-perform until the performance of the pillar player improves. Naturally, adding more pillars (profiles kPillars, ) makes the team more resilient to collapse since not all pillars under-perform at the same time. Furthermore, dependence between pillar players (e.g., profile 2Pillars+D) results in less resilient teams. This is because, dependent pillar players have a tendency to under-perform at the same time. Once this happens, the rest of the players transition to hidden state −1 and start under-performing. Finally, we emphasize that a team that doesn’t under-perform isn’t necessarily a good team. Observed performance is measured relatively to the average performance of the team. Thus, a consistently bad team might never under-perform, but still perform poorly relatively to other teams.

3.3

Remarks on team profiles

We summarize here our observations and state some principles we experimentally found to be true and can provide useful insights to

Understanding team collapse via probabilistic graphical models

experts reasoning about team composition and resilience of teams to collapses. Remark 1. (Self-dependence.) Self-dependent players, i.e., players that primarily depend on their own hidden and observed states, improve the resilience of teams. We say that a player is a pillar if other players heavily depend on him/her, while he/she is self-dependent. For example, a player 𝑖 is a pillar player if 𝑟𝑖 ≈ 1 and 𝑅 𝑗𝑖 ≈ 1, ∀𝑗 ∈ [𝑛]. Remark 2. (Pillars.) More pillars are better than less pillars. Remark 3. (Dependence between pillars.) Dependence between pillars makes teams more vulnerable to team collapse.

KDD ’24, August 25-29, 2024, Barcelona, Spain

4.1

Learning the parameters of the model

We learn the parameters of the model by applying the ExpectationMaximization (EM) algorithm. EM alternates between two steps: the expectation step (E-step) and the maximization step (M-step). In our case, these steps are: E-step: In this step, we need to calculate the expected complete log-likelihood: 𝑄 (𝚯 | 𝚯old ) = EH∼Pr(H|O,𝚯old ) [log Pr(H, O | 𝚯)] ,

(2)

Usually, we approximate the above expectation by drawing samples from the posterior distribution Pr(H | O, 𝚯) and calculating the average of the function. M-step: In this step, we need to maximize the expected complete log-likelihood w.r.t. the parameters of the model. EM alternates between the E and the M steps until convergence.

These observations have several implications in terms of team and roster construction. More specifically, self-dependent players are also typically players that can do several things at a high level. This is in contrast to “specialists” that bring to the team a very welldelineated skillset (e.g., individual defense and three point shooting) and depend on their teammates for other aspects of the game (e.g., shot generation). While lately there are many teams that prioritize the acquisition of specialists who possess specific skillset at an elite level, our observations indicate that having more self-dependent players makes a team more resilient to a possible collapse. Furthermore, as one might have expected, a team with selfdependent players that can also influence/help their teammates’ performance (i.e., pillar players) is in general more resilient. However, the choice of these pillar players should take into consideration their dependence. According to our third remark, if a team includes pillars that are dependent, the resiliency to team collapse reduces. This dependency can be related to the position the two pillars cover on the team. For instance, if a team’s pillar A is a center and its other pillar B is a guard there can be directional dependency from the B to A, just because B controls the ball more and is the one responsible for distributing it to other players. This dependency does not have to be strong, but its effects can trickle down to the rest of the players. Hence, from a roster-construction perspective, assuming a team already has one pillar, understanding the dependency that will be introduced when adding a second one is crucial. Going back to the example above, the best pillar pairing for player B might be another guard instead of a center.

4.1.1 E-step. In the E-step we need to sample from the posterior distribution Pr(H | O, 𝚯), assuming that the model parameters 𝚯 are known. Since it is clear from the context that all probabilities will be conditioned on 𝚯, we omit the parameters in the condition and write the posterior as Pr(H | O) The key idea for being able to sample from the posterior is that we need to write Pr(H | O) as a product where each random variable H𝑡 is only conditioned on observed quantities or on random variables H𝑡 ′ with 𝑡 ′ < 𝑡. This is summarized in the following Lemma, which is the main result of this section:

Pr(H, O) = Pr(H1 )

LEARNING THE MODEL

In this section, we describe a learning algorithm. Given the observed states of the players of a team over a period of time, it estimates the parameters of our model and the corresponding hidden states of the players. Throughout the description we follow the following notation: we use O to denote the sequence of observations O1, · · · , O𝑇 , where O𝑡 = (𝑂𝑡1, . . . , 𝑂𝑡𝑛 ) are the observed signals of all entities at time 𝑡. Accordingly, we use H to denote the sequence of hidden states H1, · · · , H𝑡 , where H𝑡 = (𝐻𝑡1, . . . , 𝐻𝑡𝑛 ) are the hidden states of all entities at time 𝑡. Finally, we use O1:𝑡 to denote O1, . . . , O𝑡 . Thus, given O, we want to learn the parameters 𝚯 = {M𝑖 𝑗 , N 𝑖 , R, E𝑖 | 𝑖, 𝑗 ∈ [𝑛]} of the model and the sequence of hidden states H.

Lemma 2. It holds that Pr(H | O) =

𝑛 Ö 𝑇 Ö Pr(𝐻𝑡𝑖 | O1:𝑡 ) Pr(𝐻𝑡𝑖 | 𝐻𝑡𝑖 −1, O1:𝑡 −1 ) 𝑖 𝑖=1 𝑡 =1 Pr(𝐻𝑡 | O1:𝑡 −1 )

(3)

The proof of the lemma is based on a set of observations and it is quite lengthy, so it is given in Appendix D.1. This lemma allows us to sample 𝐻𝑡𝑖 from a distribution that is proportional to Pr(𝐻𝑡𝑖 = ℎ | O1:𝑡 )Pr(𝐻𝑡𝑖 = ℎ | 𝐻𝑡𝑖 −1, O𝑡 −1 )

,

Pr(𝐻𝑡𝑖 = ℎ | O1:𝑡 −1 ) as dictated by Lemma 2. 4.1.2 M-step. In the M-step we want to maximize the the expected complete log-likelihood w.r.t. the parameters of the model. To see how this can be approached we first write the complete likelihood:

= Pr(H1 )

𝑇 Ö

Pr(H𝑡 | H𝑡 −1, O𝑡 −1 )

𝑡 =2 𝑇 Ö 𝑛 Ö

𝑇 Ö

Pr(O𝑡 | H𝑡 )

𝑡 =1

Pr(𝐻𝑡𝑖 | 𝐻𝑡𝑖 −1, O𝑡 −1 )

𝑡 =2 𝑖=1

𝑇 Ö 𝑛 Ö

Pr(𝑂𝑡𝑖 | 𝐻𝑡𝑖 )

𝑡 =1 𝑖=1

Taking the logarithm on both sides we get the complete log-likelihood: log Pr(H, O) = log Pr(H1 ) +

+

𝑇 ∑︁ 𝑛 ∑︁ 𝑡 =2 𝑖=1 𝑇 ∑︁ 𝑛 ∑︁ 𝑡 =1 𝑖=1

log Pr(𝐻𝑡𝑖 | 𝐻𝑡𝑖 −1, O𝑡 −1 ) log Pr(𝑂𝑡𝑖 | 𝐻𝑡𝑖 ).

(4)

KDD ’24, August 25-29, 2024, Barcelona, Spain

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

The base case is

Thus in the M-step we have to solve the following problem: 𝚯new = arg max 𝑄 (𝚯 | 𝚯old ), 𝚯

where 𝑄 () is given by Eq. (2) and the complete log-likelihood is computed by Eq. 4. Note that 𝑄 (𝚯 | 𝚯old ) is not a concave function in the parameters 𝚯 and thus finding a global maximum it not easy. Specifically, the problem stems from the terms Pr(𝐻𝑡𝑖 | 𝐻𝑡𝑖 −1, O𝑡 −1 ) which contain products of variables. Thus, we opted for a roundrobin heuristic algorithm. This heuristic iteratively optimizes one parameter from 𝚯 = {M, N, R𝑖 , E | 𝑖 ∈ [𝑛]} per iteration, while keeping the other parameters fixed; in all cases fixing all but one of the parameters results in a concave function. Hence, we can use standard convex-optimization tools to optimize for each parameter separately. In practice, we found that 1-2 iterations of the round robin heuristic are adequate.

4.2

Likelihood calculation

Given the model parameters 𝚯, we can calculate the likelihood of the data Pr(O), based on the results of the previous section:

=

𝑇 ∑︁ 𝑛 ∑︁ 𝑡 =1 𝑖=1 𝑇 ∑︁ 𝑛 ∑︁

log Pr(𝑂𝑡𝑖 | O𝑡 −1 )

Once all 𝛿𝑖 (𝑡, ℎ) values are computed one can trace back the solutions starting from 𝛿𝑖 (𝑇 , ℎ), where ℎ = arg maxℎ ′ ∈ H 𝛿𝑖 (𝑇 , ℎ ′ ).

4.4

Evaluating the learning algorithm on synthetic data

We evaluated our implementation of the EM algorithm on synthetic data as follows. We created a 1Pillar team profile and generated samples that correspond to 𝑇 = 100 timesteps. We then ran the EM algorithm and found that it correctly identifies the structure of the team. Figure 3 shows the Negative Evidence Lower Bound (N-ELBO) as a function of the iterations of EM. The figure shows the average and the standard deviation of N-ELBO over 10 different initializations. As expected, N-ELBO decreases with iterations until it stabilizes to a low value. The negative likelihood of the (best) learned model is 416, while the negative likelihood of the true model is 417 (slightly larger). That is, EM finds a model that has even better likelihood than the model used to generate the data. Average Standard Deviation

(6)

" log

𝑡 =1 𝑖=1

# ∑︁

Pr(𝑂𝑡𝑖 | 𝐻𝑡𝑖 = ℎ) Pr(𝐻𝑡𝑖 = ℎ | O1:𝑡 −1 ) .

N-ELBO

log Pr(O) =

𝛿𝑖 (1, ℎ) = Pr(𝐻 1𝑖 = ℎ)Pr(𝑂 𝑖1 | 𝐻 1𝑖 = ℎ), ∀ℎ ∈ H .

(5)

ℎ∈ H

(7)

4.3

Decoding the hidden states

In decoding , we find the most likely hidden variables path H1, . . . , H𝑇 , given the model parameters 𝚯 (evaluated by EM) and the observed variables O = O1:𝑇 . Formally, this problem can be expressed as h = arg max Pr(H = h | O).

(8)

h

We solve the problem expressed in Eq. (8) via a dynamic-programming algorithm, which is very similar to the Viterbi algorithm used for standard HMMs [3]. To this end, first we decouple the chains Pr(H = h | O) =

𝑛 Ö

𝑖

𝑖

Pr(H = h | O),

𝑖=1

using the independence of H𝑖 and H 𝑗 given O. For each entity 𝑖, we define 𝛿𝑖 (𝑡, ℎ) to be the probability of the maximum-probability path ending at 𝐻𝑡𝑖 = ℎ; formally: 𝛿𝑖 (𝑡, ℎ) =

max

ℎ 1 ,...,ℎ𝑡 −1 ∈ H𝑡 −1 Pr(𝐻 1𝑖 = ℎ 1, · · · , 𝐻𝑡𝑖 −1

= ℎ𝑡 −1, 𝐻𝑡𝑖 = ℎ | 𝑂 𝑖1, · · · 𝑂𝑡𝑖 ).

That is, 𝛿𝑡 (ℎ) is the probability of the most probable path ending at 𝐻𝑡𝑖 = ℎ. Now the values of 𝛿𝑖 (𝑡, ℎ) can be computed using the following dynamic-programming recursion: 𝛿𝑖 (𝑡, ℎ) = Pr(𝑂𝑡𝑖 | 𝐻𝑡𝑖 = ℎ)×   max 𝛿𝑖 (𝑡 − 1, ℎ ′ )Pr(𝐻𝑡𝑖 = ℎ | 𝐻𝑡𝑖 −1 = ℎ ′, O𝑡 −1 ) , ℎ′ ∈ H ∀ℎ ∈ H and 𝑡 ∈ {1, . . . ,𝑇 }.

Iterations

Figure 3: Negative Evidence Lower Bound (N-ELBO) vs iterations of EM; average and standard deviation over 10 random initializations.

REAL-WORLD EXPERIMENTS

In this section, we validate the practical utility of our model by using it to identify the structure of all NBA teams for the season 2021-2022. We also show how our model can be used to analyze and obtain significant insights for specific games.

5.1

## Data

For each NBA team of the 2021-2022 season we selected their starting lineup players. That is, the players that played the most minutes in each position (Point Guard, Shooting Guard, Small Forward, Power Forward, Center)2 . For our experiment,s we used a Play-by-Play dataset (PBP) that contains a detailed record of events for all NBA games of the season. Using PBP, for each player, we computed his average PIE metric3 across all quarters (each game has four 12min quarters) of all games.

## 2. The

starting lineups are obtained from the basketball reference website. For example, for Boston Celtics the starting lineup is here: https://www.basketballreference.com/teams/BOS/2022_depth.html 3 See https://www.nba.com/stats/help/faq

Understanding team collapse via probabilistic graphical models

KDD ’24, August 25-29, 2024, Barcelona, Spain

1.0

1.0 L. Doncic

D. Garland

0.8

J. Brunson

L. Markanen

0.4

0.6 Players

D. Finney-Smith

## I. Okoro

0.4 E. Mobley

0.2

D. Powell

0.2

(a) Dallas Mavericks

n

y

lle J. A

ble

Players

(b) Cleveland Cavaliers 1.0

1.0 M. Smart

K. PorterJr.

0.8

J. Brown

0.8

J. Green 0.6

J. Tatum 0.4

0.6 Players

G. Williams

K. Martin 0.4 J. Tate

0.2

d Wo o

0.0

C.

J. T ate

rtin K.

Ma

n ree

Po rt K.

(c) Boston Celtics

J. G

r.

r_i

for d

0.0

ord

ms Wi llia

0.2

C. Wood

A. H

Players

G.

J. T atu

m

n row J. B

art M.

Sm

r_i

A. Hordford

erJ

Players

0.0

E.

Mo

n

ko ro

I. O

Ma rka ne

D.

Ga

rla nd

r_i

D.

ith Po we ll

ck

Fin ne y-S m

ull o

Players

0.0

D.

son

R. B

run

J. B

Do nc ic L.

r_i

J. Allen

L.

Players

0.6 R. Bullock

0.8

Players

(d) Houston Rockets

Figure 4: Team structure (R) for the Dallas Mavericks, Cleveland Cavaliers, Boston Celtics and Houston Rockets. At a high level, the PIE metric of a player for a given time window, captures the percentage of events (points, assists, rebounds, etc) that the player achieved in the given window. Finally, we labeled the performance of every player for every quarter he played as average (𝑂𝑡𝑖 = 0), if his PIE metric was within ±𝜖 of his average PIE, where 𝜖 = 0.05. If his performance was above this region, we labeled his performance as over-performance 𝑂𝑡𝑖 = 1. Accordingly, if his performance was below the average region we labels his performance as under-performance 𝑂𝑡𝑖 = −1. If the player didn’t play in a quarter we used his latest PIE measurement in the game, or if there was no previous measurement we assumed average performance 𝑂𝑡𝑖 = 1. We name the resulting dataset NBAseason. For section 5.4, we created the NBAgames dataset. This dataset contains a few selected games of interest. We divided each of these games into 3 minute time windows so as to have more fine-grained measurements. As before, for each player we computed his average PIE metric in each 3 minute window and labeled his performance.

5.2

Implementation details

In order to apply EM in real data, we created a collection of approximately 10000 team profiles, i.e., instantiations of our model. These profiles were, to a large extent, informed by our findings

in Section 4.4. Then, we found the profile from the collection that best matches each team by calculating the likelihood of the profile. Finally, for each team we ran the EM algorithm initialized with the aforementioned profile. The implementation of our algorithms, along with the datasets we used in our experiments are publicly available at https://github. com/jasonNikolaou/Team-collapse.git.

5.3

Team structure in NBA teams

Using dataset NBAseason, we applied the EM algorithm to find the maximum-likelihood estimates of the parameters of our model as described in Section 5.2. Thus, for every one of the 30 NBA teams we obtained an estimate of its team structure R. While of course each team has a different structure, there are two main team-structure types that emerge. In Figure 4 we present four representative teams of these team structures (two for each), while we present the rest of the team structures in Appendix E.1. The team structures correspond to the matrix R of the team profile and therefore, they are presented as a 5 × 6 heatmap. The first column in the heatmap corresponds to the dependency of each row player 𝑖 to its hidden state (i.e., 𝑟𝑖 ), and the rest 5 × 5 matrix

0.2

PTS +/-

0.4

0.0

team state 7.5 PTS +/-

0.4

team state 7.5 PTS +/-

0.0

5.0

0.2

5.0

0.1

2.5

0.0

0.2

0.0

0.1

Team state

Team state

0.2

0.3

0.2

0.4

0.5

0.4

0.6

Window

(a) Nets vs Knicks game (16 Feb 2022)

PTS +/-

team state

PTS +/-

0.6

2.5

Window

Team state

0.8

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

2.5 0.0

0.2

5.0

0.4

7.5

0.6

(b) Celtics vs Knicks game (6 Jan 2022)

2.5

PTS +/-

KDD ’24, August 25-29, 2024, Barcelona, Spain

5.0 7.5 10.0

Window

(c) Lakers vs Thunder (27 Oct 2021)

Figure 5: Team (hidden) state and points difference (PTS +/-) per 3 minute window for different games. represents the dependency between the hidden state of the row player 𝑖 and the observed state of the column player 𝑗. The first two team structures, shown in Figures 4a and 4b correspond to the structures of Dallas Mavericks and Cleveland Cavaliers respectively. For the Mavericks, we see that the state of every player is mainly dependent on their own hidden state (first column of the matrix), while they do not depend on their own observations. Simply put, these teams consist of players that typically can showcase “short memory” with respect to their observed performance/state and their state only depends on their own hidden (mental) state. The Cavaliers’ team structure is very similar. The other two team structures shown in Figures 4c and 4d correspond to Boston Celtics and Houston Rockets respectively. For Celtics, we see a smaller dependency of their players’ on their own hidden state and a larger dependency for some of them on their observed state. However, there is also a dependency on another player’s observed state (last column in Figure 4c). In this particular case , this player is Al Horford, who is the most experienced player on the team and his teammates can be thought of as “feeding off” his observed state/performance. The Rockets team structure (Figure 4d) is very similar. Interestingly, while both the Dallas Mavericks and Boston Celtics have very different structures, they both reached the conference finals and finals respectively. On the other hand, the Houston Rockets, which have structure similar to Boston Celtics, had a record of 20 wins and 62 loses and finished last in the Western conference. This demonstrates that there are many ways to succeed (or fail) in a team sport. The team structure is just one characteristic of a team, among others that create different vulnerabilities and strengths.

5.4

Diving deeper into specific games

For the results we report here, we use the NBAgames dataset described in section 5.1. Using the parameters learned in the previous section, we decode the most probable hidden states of players by applying the decoding algorithm described in Section 4.3. We now analyze three games in detail. In all these games, one of the teams managed to comeback and win the game despite trailing behind in score for the most part of the game. More analyzed games can be found in the Appendix E.2. Figure 5 visualizes the hidden team state we obtained from our model over the 3 minute windows, and overlays the actual point

differential for the game during these states. In these games, a team was performing well to start the game (Knicks, Celtics and Lakers respectively in the figure order), but later in the game there was a “transition” and they surrendered the lead and ultimately lost the game (i.e., collapsed). As we can see the inferences on the team state made by our model follow closely the point differential, and hence the status, of the game. These results indicate that our model captures the underlying hidden states of the players to a great extent and can explain what one observes at the game.

## Conclusions

In this paper, we proposed a probabilistic graphical model that allowed us to formalize the dependencies between team players’ hidden/mental states and the observed performance of themselves and their teammates. Then, we used this model to identify, analyze and explain team collapses, i.e., events where a team severely underperformed. We also showed that we can learn the parameters of this model using an EM algorithm. Furthermore, we used our model to analyze real-world team data from NBA games in 2021-22 season. As a result, we found some interesting team structures and identified games where according to our model a team collapsed. One shortcoming of our model is the assumption that players in the team do not change over time. Considering a dynamic version of the model, where players can get substituted is an interesting direction of future work. In our experiments with real-world data, we relied on the use of the PIE metric to measure the observed performance of players. In the future, we plan to explore other metrics as well as make use of machine learning methods in order to classify the observed performance. Finally, we can potentially use our model to calculate collapse probabilities, as predictors of future collapses. In such a scenario, our model can guide coaching decisions, e.g., substitutions, time-out, etc. Reproducibility. We make the code and the data we used in our experiments publicly available at https://github.com/jasonNikolaou/ Team-collapse.git.

Understanding team collapse via probabilistic graphical models

## References

[1] Roy F Baumeister and Carolin J Showers. 1986. A review of paradoxical performance effects: Choking under pressure in sports and mental tests. European Journal of Social Psychology 16, 4 (1986), 361–383. [2] Phil Birnbaum. 2008. Clutch hitting and the cramer test. The Baseball Research Journal 37 (2008), 71–76. [3] Christopher M. Bishop. 2006. Pattern recognition and machine learning. Springer. [4] Ralph Allan Bradley and Milton E Terry. 1952. Rank analysis of incomplete block designs: I. The method of paired comparisons. Biometrika 39, 3/4 (1952), 324–345. [5] Lotte Bransen, Pieter Robberechts, Jan Van Haaren, and Jesse Davis. 2019. Choke or shine? Quantifying soccer players’ abilities to perform under mental pressure. In Proceedings of the 13th MIT sloan sports analytics conference. 1–25. [6] Daniel Cervone, Alex D’Amour, Luke Bornn, and Kirk Goldsberry. 2016. A multiresolution stochastic process model for predicting basketball possession outcomes. J. Amer. Statist. Assoc. 111, 514 (2016), 585–599. [7] Shuo Chen and Thorsten Joachims. 2016. Modeling intransitivity in matchup and comparison data. In Proceedings of the ninth acm international conference on web search and data mining. 227–236. [8] Shuo Chen and Thorsten Joachims. 2016. Predicting matchups and preferences in context. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. 775–784. [9] Wen-Cheng Chen, Wan-Lun Tsai, Huan-Hua Chang, Min-Chun Hu, and Wei-Ta Chu. 2021. Instant basketball defensive trajectory generation. ACM Transactions on Intelligent Systems and Technology (TIST) 13, 1 (2021), 1–20. [10] Alexander D’Amour, Daniel Cervone, Luke Bornn, and Kirk Goldsberry. 2015. Move or Die: How Ball Movement Creates Open Shots in the NBA. [11] Tom Decroos, Lotte Bransen, Jan Van Haaren, and Jesse Davis. 2019. Actions speak louder than goals: Valuing player actions in soccer. In Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining. 1851–1861. [12] Thomas J Dohmen. 2008. Do professionals choke under pressure? Journal of economic behavior & organization 65, 3-4 (2008), 636–653. [13] Wen Dong, Alex Pentland, and Katherine A. Heller. 2012. Graph-Coupled HMMs for Modeling the Spread of Infection. In Proceedings of the Twenty-Eighth Conference on Uncertainty in Artificial Intelligence, Catalina Island, CA, USA, August 14-18, 2012, Nando de Freitas and Kevin P. Murphy (Eds.). AUAI Press, 227–236. [14] Denise M Hill, Sheldon Hanton, Nic Matthews, and Scott Fleming. 2010. Choking in sport: A review. International Review of Sport and Exercise Psychology 3, 1 (2010), 24–39. [15] Daphne Koller and Nir Friedman. 2009. Probabilistic graphical models: principles and techniques. MIT press. [16] Amy N Langville and Carl D Meyer. 2012. Who’s# 1? The science of rating and ranking. Princeton University Press. [17] Patrick Lucey, Alina Bialkowski, Mathew Monfort, Peter Carr, and Iain Matthews. 2016. quality vs quantity: Improved shot prediction in soccer using strategic features from spatiotemporal data. In 8th MIT Sloan Sports Analytics Conference. [18] Brian Macdonald. 2011. A regression-based adjusted plus-minus statistic for NHL players. Journal of Quantitative Analysis in Sports 7, 3 (2011). [19] Andrew Miller, Luke Bornn, Ryan Adams, and Kirk Goldsberry. 2014. Factorized Point Process Intensities: A Spatial Analysis of Professional. In ICML. [20] Quang Nguyen, Ronald Yurko, and Gregory J Matthews. 2023. Here Comes the STRAIN: Analyzing Defensive Pass Rush in American Football with Player Tracking Data. arXiv preprint arXiv:2305.10262 (2023). [21] Wei Pan, Wen Dong, Manuel Cebrian, Taemie Kim, James H Fowler, and Alex Sandy Pentland. 2012. Modeling dynamical influence in human interaction: Using data to make better inferences about influence within social systems. IEEE Signal Processing Magazine 29, 2 (2012), 77–86. [22] Juyong Park and Mark EJ Newman. 2005. A network-based ranking system for US college football. Journal of Statistical Mechanics: Theory and Experiment 2005, 10 (2005), P10014. [23] Beth L Parkin and Vincent Walsh. 2017. Gunslingers, poker players, and chickens 2: Decision-making under physical performance pressure in subelite athletes. Progress in Brain Research 234 (2017), 317–338. [24] Konstantinos Pelechrinis. 2018. Linnet: Probabilistic lineup evaluation through network embedding. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases. Springer, 20–36. [25] Konstantinos Pelechrinis, Evangelos Papalexakis, and Christos Faloutsos. 2016. Sportsnetrank: Network-based sports team ranking. ACM KDD Workshop on Large-Scale Sports Analytics (2016). [26] Sònia Pineda-Hernández. 2022. How to play under pressure: EEG monitoring of mental activation training in a professional tennis player. Physiology & Behavior 250 (2022), 113784. [27] R Paul Sabin. 2021. Estimating player value in American football using plus– minus models. Journal of Quantitative Analysis in Sports 17, 4 (2021), 313–364. [28] Thomas Seidl, Aditya Cherukumudi, Andrew Hartnett, Peter Carr, and Patrick Lucey. 2018. Bhostgusters: Realtime interactive play sketching with synthesized NBA defenses. In Proceeding of the 12th MIT Sloan Sports Analytics Conference,

KDD ’24, August 25-29, 2024, Barcelona, Spain

Boston, MA. Boston: MIT. [29] Anthony Sicilia, Konstantinos Pelechrinis, and Kirk Goldsberry. 2019. Deephoops: Evaluating micro-actions in basketball using deep feature representations of spatio-temporal data. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. 2096–2104. [30] Yosef Solomonov, Simcha Avugos, and Michael Bar-Eli. 2015. Do clutch players win the game? Testing the validity of the clutch player’s reputation in basketball. Psychology of Sport and Exercise 16 (2015), 130–138. [31] AC Thomas, Samuel L Ventura, Shane T Jensen, and Stephen Ma. 2013. Competing process hazard function models for player ratings in ice hockey. The Annals of Applied Statistics (2013), 1497–1524. [32] Gilbert W Bassett. 2007. Quantile regression for rating teams. Statistical Modelling 7, 4 (2007), 301–313. [33] Scott Wallace, Steven B Caudill, and Franklin G Mixon Jr. 2013. Homo certus in professional basketball? Empirical evidence from the 2011 NBA Playoffs. Applied Economics Letters 20, 7 (2013), 642–648. [34] Wayne L Winston, Scott Nestler, and Konstantinos Pelechrinis. 2022. Mathletics: How gamblers, managers, and fans use mathematics in sports. Princeton University Press. [35] Yisong Yue, Patrick Lucey, Peter Carr, Alina Bialkowski, and Ian Matthews. 2014. Learning fine-grained spatial models for dynamic sports play prediction. In ICDM. [36] Ronald Yurko, Francesca Matano, Lee F Richardson, Nicholas Granered, Taylor Pospisil, Konstantinos Pelechrinis, and Samuel L Ventura. 2020. Going deep: models for continuous-time within-play valuation of game outcomes in American football with tracking data. Journal of Quantitative Analysis in Sports 16, 2 (2020), 163–182.

KDD ’24, August 25-29, 2024, Barcelona, Spain

A

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

APPENDIX FOR SECTION 2

A.1

Proof of Lemma 1

Proof. ∑︁

(𝐻𝑡𝑖 = ℎ | O𝑡 −1, 𝐻𝑡𝑖 −1 )

ℎ∈ H 𝑛 ∑︁ ©∑︁ ª 𝑗 ­ 𝑅𝑖 𝑗 Infl(𝐻𝑡𝑖 = ℎ | 𝑂𝑡 −1 ) + 𝑅𝑖 Infl(𝐻𝑡𝑖 = ℎ | 𝐻𝑡𝑖 −1 ) ® ℎ∈ H « 𝑗=1 ¬ 𝑛 ∑︁ ∑︁ ∑︁ 𝑗 = 𝑅𝑖 𝑗 Infl(𝐻𝑡𝑖 = ℎ | 𝑂𝑡 −1 ) + 𝑅𝑖 Infl(𝐻𝑡𝑖 = ℎ | 𝐻𝑡𝑖 −1 )

=

𝑗=1

=

𝑛 ∑︁

ℎ∈ H

ℎ∈ H

𝑅𝑖 𝑗 + 𝑅𝑖

𝑗=1

= 1. □

A.2

On the influence matrices

In this section, we answer the following question: why isn’t M the same as the probability distributions Pr(𝐻𝑡𝑖 | 𝑂𝑡𝑖 −1 ). Consider the following proof by contradiction. Let 𝑛 = 1 and 𝑟 1 = 0, 𝑅11 = 1. We define the following parameters: 0 0 1 1 0 0  0.7 0.2 0.1       N = 0 1 0 , N = 0 1 0 , E = 0.2 0.6 0.2 , (9) 1 0 0 0 0 1  0.1 0.2 0.7       Assume that: Pr(𝐻𝑡𝑖 = ℎ | 𝑂𝑡𝑖 −1 = 𝑜) = M [ℎ, 𝑜]

(10)

Pr(𝐻𝑡1 = 0 | 𝐻𝑡1−1 = 1, 𝑂𝑡1−1 = 2) = 𝑟 1 N [1, 0] + 𝑅11 M [2, 0]

(11)

We have

=0+1×1

(12)

=1

(13)

and Pr(𝐻𝑡1 = 0 | 𝐻𝑡1−1 = 1) = N [1, 0] = 0.

(14)

We also have Pr(𝐻𝑡1 = 0 | 𝐻𝑡1−1 = 1) =

∑︁

Pr(𝐻𝑡1 = 0 | 𝐻𝑡1−1 = 1, 𝑂𝑡1−1 = 𝑜)Pr(𝑂𝑡1−1 = 𝑜 | 𝐻𝑡1−1 = 1)

(15)

𝑜

≥ Pr(𝐻𝑡1 = 0 | 𝐻𝑡1−1 = 1, 𝑂𝑡1−1 = 2)Pr(𝑂𝑡1−1 = 2 | 𝐻𝑡1−1 = 1)

(16)

≥ 1 × 0.2

(17)

= 0.2,

(18)

which is a contradiction. In the same way, we can prove that N isn’t the same as the probability distributions Pr(𝐻𝑡𝑖 | 𝐻𝑡𝑖 −1 ).

Bappendix FOR SECTION 3 B.1 Examples of model parameters used in our experiments N instance used in the experiments presented in Section 3: 0.7  N = 0.2 0.1 

0.2 0.6 0.2

0.1 0.2 0.7

(19)

Understanding team collapse via probabilistic graphical models

KDD ’24, August 25-29, 2024, Barcelona, Spain

E instance used in our experiments: 0.8  E = 0.2 0 

0.2 0.8 0.2

0  0.2 0.8

(20)

0.8  M = 0.2 0 

0.2 0.8 0.2

0  0.2 , 0.8

(21)

0.9  M = 0.2 0.2 

0.1 0.6 0.3

0  0.2 0.5

(22)

M instances used in our experiments in Section 3

Additional M instances we considered:

and  0 0.2 0.8   Manti = 0.1 0.8 0.1 . (23) 0.8 0.2 0    Additional R instances we considered In addition to the R instances we described in Section 3, we also experimented with a few more R instances. We describe the full set of those instances here: • Rh : All players depend on their previous hidden state. That is, 𝑟𝑖 = 1, ∀𝑖 ∈ [𝑛] and 𝑅𝑖 𝑗 = 0, ∀𝑖, 𝑗 ∈ [𝑛]. We denote the profile that corresponds to this R with H. • Rho : All players depend only on their previous hidden and observed states. That is, 𝑟𝑖 > 𝑅𝑖𝑖 > 0, ∀𝑖 ∈ [𝑛] and 𝑅𝑖 𝑗 = 0, ∀𝑖, 𝑗 ∈ [𝑛]. For our experiments we use 𝑟𝑖 = 0.7 and 𝑅𝑖𝑖 = 0.3, for all 𝑖 ∈ [𝑛]. • R𝑘 : There are 𝑘 pillar players 𝑃 that affect all others; i.e., 𝑟𝑖 = 𝑅𝑖𝑖 = 0 and 𝑅𝑖 𝑗 = 1/|𝑃 | for all 𝑖 ∉ 𝑃 and 𝑗 ∈ 𝑃 and 𝑟𝑖 = 1 for 𝑖 ∈ 𝑃. • R kH : There are 𝑘 pillar players 𝑃 that affect all others, but all non-pillar players are also affected by their hidden states. That is, 𝑟𝑖 = 1 for all 𝑖 ∈ 𝑃, 𝑟𝑖 > 0 for all 𝑖 ∉ 𝑃 and 𝑅𝑖 𝑗 = (1 − 𝑟𝑖 )1/|𝑃 | for all 𝑖 ∉ 𝑃 and 𝑗 ∈ 𝑃. In our experiments we set 𝑟𝑖 = 0.5 for all 𝑖 ∉ 𝑃. • R kD : In this case, there are again 𝑘 pillar players 𝑃 (as in R𝑘 , but this time they depend on each other. That is, for every 𝑖 ∈ 𝑃 0 < 𝑟𝑖 < 1 and 𝑅𝑖 𝑗 = (1 − 𝑟𝑖 )1/|𝑃 | for every 𝑖, 𝑗 ∈ 𝑃. In our experiments we again set 𝑟𝑖 = 0.5. • R kDH : This is a combination of R𝐻 and R𝑘𝐷 where all pillar players are set as in R𝑘𝐷 and all non-pillar players are set as in R kH . • R uniform : In this case we assume that for every player 𝑖, 𝑟𝑖 = 𝑅𝑖 𝑗 = 1/(𝑛 + 1).

B.2

Team profiles

We create the following extended sets of profiles: H: M as above and R𝑖 = R𝐻 . HO. M as above and R𝑖 = Rho . 1Pillar (1P). M as above and R𝑖 = R 1 . 1Pillar + Hidden (1P + H). M as above and R𝑖 = R 1H . 2Pillars (2P). M as above and R𝑖 = R 2 . 2Pillars + Dependence (2P + D). M as above and R𝑖 = R 2D . 2Pillars + Hidden (2P + H). M as above and R𝑖 = R 2H . 2Pillars + Hidden + Dependence (2P + H + D). M as above and R𝑖 = R 2DH . 3Pillars (3P). M as above and R𝑖 = R 3 . 3Pillars + Dependence (3P + D). M as above and R𝑖 = R 3D . 3Pillars + Hidden (3P + H). M as above and R𝑖 = R 2H . 3Pillars + Hidden + Dependence (3P + H + D). M as above and R𝑖 = R 2DH . Uniform. Players equally depend on their hidden states and other players, i.e. 𝑅𝑖 = 1/6, 𝑅𝑖 𝑗 = 1/6, ∀𝑖, 𝑗 ∈ [𝑛]. 1Pillar Bad Teammate (BT1P). Same as the 1Pillar profile, but we change the M matrix to the following: 0.9  M = 0.2 0.2 

0.1 0.6 0.3

0  0.2 . 0.5

(24)

KDD ’24, August 25-29, 2024, Barcelona, Spain

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

We are trying to capture a pillar who has significantly negative impact when his/her observed state is −1 (i.e. below-average performance), and weakly positive impact when their observed state is 1 (i.e. above-average performance). 1Pillar Bad Teammate + Hidden (BT1P). Same as the 1Pillar + Hidden profile, but with the M matrix of the BT1P profile. 1Pillar Great Teammate (GT1S). Same as the 1Pillar profile, but we change the M matrix to the following:

0.5  M = 0.1 0 

0.3 0.8 0.1

0.2 0.1 . 0.9

(25)

This profile captures a pillar who has significantly positive impact when their observed state is 1 (i.e. above-average performance), and weakly negative impact when their observed state is −1 (i.e. below-average performance). 1Pillar Great Teammate + Hidden (GT1P). Same as the 1Pillar + Hidden profile, but with the M matrix of the 1-Pillar Great Teammate profile. Finally, we create two profiles to capture anti-dependence. That is, when one player’s performance improves, another player’s performance drops. We define the anti-dependence M matrix as:

0  M antiD = 0.1 0.8 

0.2 0.8 0.2

0.8 0.1 . 0 

(26)

1Pillar + anti-Dependence (1Pillar + antiD). Same as the 1Pillar profile, but we change the M to M antiD . 2Pillars + anti-Dependence (2Pillars + antiD). Same as the 2Pillar profile, but we change the M matrix of both pillars to M antiD . In this way, the two pillars are anti-dependent on each other. Note that the pillars don’t depend at all on non-pillar players.

B.3

Team state over time

In order to better understand our models we experiment with the 19 profiles described in Appendix B.2. For each profile we types of teams and then run 1000 simulations. Each simulation consists of 100 samples. We assume that every player 𝑖 ∈ [𝑛] starts from hidden state 𝐻 1𝑖 = 0. In our experiments, we use 19 different team profiles, which correspond to different combinations of R and M pairs. We define the hidden team state (resp. observed team state) at each timestep as the average of the hidden (resp. observed) states of the individuals in the team at this timestep; values close to 0 correspond to average team performance, values close to −1 (resp. 1) correspond to an under-performing (resp. over-performing) team. The team (hidden) state of the different teams over time is shown in Figures 6 - 9. In these plots the thick green region corresponds to the 25-th and 75-th percentiles of the team state across simulations. The light green region corresponds to the min and max values of the team state across simulations. Depending on the team profile, the thick green band might vary its width. Teams with a narrow green band, are more stable, since in 50% of the time they are close to their average mental state. Furthermore, its worth noticing that for some profiles the green band is shifted either upwards (e.g. GT1P) or downwards (e.g BT1P). This shift reveals an inclination of a team towards higher (or lower) mental states.

Understanding team collapse via probabilistic graphical models

1.00

1.00

Average Hidden Average Observed

0.75 0.50

0.50

0.25

0.25

0.00 0.25

0.00 0.25

0.50

0.50

0.75

0.75

1.00

1.00

Time

Average Hidden Average Observed

0.75

Team state

Team state

KDD ’24, August 25-29, 2024, Barcelona, Spain

(a) 1Pillar

1.00

Average Hidden Average Observed

0.75

0.50

0.50

0.25

0.25

0.00 0.25

Average Hidden Average Observed

0.75

Team state

Team state

Time

(b) 1Pillar + H

1.00

0.00 0.25

0.50

0.50

0.75

0.75

1.00

1.00

Time

(c) 1Pillar + H + antiD

1.00

Time

(d) 2Pillars

1.00

Average Hidden Average Observed

0.75 0.50

0.50

0.25

0.25

0.00 0.25

0.00 0.25

0.50

0.50

0.75

0.75

1.00

Average Hidden Average Observed

0.75

Team state

Team state

1.00

Time

(e) 2Pillars + H

Time

(f) 2Pillars + D

Figure 6: Average hidden and observed states for each team profile

KDD ’24, August 25-29, 2024, Barcelona, Spain

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

1.00 0.75 0.50

0.50

0.25

0.25

0.00 0.25

0.00 0.25

0.50

0.50

0.75

0.75

1.00

1.00

Time

Average Hidden Average Observed

0.75

Team state

Team state

1.00

Average Hidden Average Observed

(a) 2Pillars + H + D

1.00

0.50

0.50

0.25

0.25

0.00 0.25

Average Hidden Average Observed

0.75

Team state

Team state

1.00

0.00 0.25

0.50

0.50

0.75

0.75

1.00

1.00

Time

(c) 3Pillars

Time

(d) 3Pillars + H

1.00

1.00

Average Hidden Average Observed

0.75 0.50

0.50

0.25

0.25

0.00 0.25

0.00 0.25

0.50

0.50

0.75

0.75

1.00

Average Hidden Average Observed

0.75

Team state

Team state

Time

(b) 2Pillars + antiD

Average Hidden Average Observed

0.75

1.00

Time

(e) 3Pillars + D

Time

(f) 3Pillars + H + D

Figure 7: Average hidden and observed states for each team profile

Understanding team collapse via probabilistic graphical models

1.00

1.00

Average Hidden Average Observed

0.75 0.50

0.50

0.25

0.25

0.00 0.25

0.00 0.25

0.50

0.50

0.75

0.75

1.00

1.00

Time

Average Hidden Average Observed

0.75

Team state

Team state

KDD ’24, August 25-29, 2024, Barcelona, Spain

(a) 1Pillar Bad Teammate (BT1P)

1.00

0.50

0.50

0.25

0.25

0.00 0.25

Average Hidden Average Observed

0.75

Team state

Team state

Time

1.00

0.00 0.25

0.50

0.50

0.75

0.75

1.00

1.00

Time

(c) 1Pillar Great Teammate (GT1T)

1.00

Time

(d) 1Pillar Great Teammate (GT1T) + H

1.00

Average Hidden Average Observed

0.75 0.50

0.50

0.25

0.25

0.00 0.25

0.00 0.25

0.50

0.50

0.75

0.75

1.00

Average Hidden Average Observed

0.75

Team state

Team state

(b) 1Pillar Bad Teammate (BT1P) + H

Average Hidden Average Observed

0.75

1.00

Time

(e) H

Time

(f) HO

Figure 8: Average hidden and observed states for each team profile

KDD ’24, August 25-29, 2024, Barcelona, Spain

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

1.00

Average Hidden Average Observed

0.75

Team state

0.50 0.25 0.00 0.25 0.50 0.75 1.00

Time

(a) Balanced

Figure 9: Average hidden and observed team states for each team profile; average is taken over different simulations

B.4

Team collapse probability vs Team profile

Team collapse probability vs Team profile

Team collapse probability

0.08 0.06 0.04 0.02

H HO 1P 1P + H 1P + H + antiD BT1P BT1P + H GT1P GT1P + H 2P 2P + 2P + a D ntiD 2P + H 2P + H +D 3P 3P + D 3P + 3P + Hh + Balanc D ed

0.00

Team profiles

Figure 10: Team collapse probability vs Team profile

B.5

Maximum and average time in collapse state

In figure 11 (a), we observe that the more pillars a team has, the longer the maximum window of team collapse is. In general adding self-dependence, i.e. dependence on the hidden states, doesn’t always make the team more resilient. However, adding self-dependence in the 3Pillars profile resulted in higher maximum collapse time. Moreover, we observe that having a Great Teammate player on whom all other players depend (1Pillar Great Teammate (GT1T) profile), significantly reduces the length of the maximum time collapse window. This is because when the pillar player under-performs, he/she only mildly affects non-pillar players. On the contrary, if the pillar player over-performs, non-pillar players are greatly affected in a positive way.

Understanding team collapse via probabilistic graphical models

KDD ’24, August 25-29, 2024, Barcelona, Spain

Max collapse time vs Team profile

Avg collapse time vs Team profile 1.6 1.4

1.2 Avg collapse time

1.0 0.8 0.6 0.4 0.2

H HO 1P 1P + H 1P + H + antiD BT1P BT1P + H GT1P GT1P + H 2P 2P + 2P + a D ntiD 2P + 2P + Hh +D 3P 3P + D 3P + 3P + Hh + Balanc D ed

Team profiles

0.0

H HO 1P 1P + H 1P + H + antiD BT1P BT1P + H GT1P GT1P + H 2P 2P + D 2P + a ntiD 2P + H 2P + H +D 3P 3P + D 3P + H 3P + H +D Balanc ed

Max collapse time

Team profiles

(a) Maximum time in team collapse

(b) Average time in collapse

Figure 11: Maximum and average time team team collapse

In Figure 11 (b), we observe that the average collapse time doesn’t significantly vary among team profiles. That said, it is clear that when the players only depend on their hidden state, i.e.H profile, the average duration of the collapse is longer. This is because, in the rare case that all players choke, it is very difficult to get out of the choke. For example, this is not the case for the 1Pillar profile. When the pillar of the team chokes, non-pillar players are likely to choke. But, once the pillar player gets out of the choke, non-pillar players are likely to do the same.

C

INDEPENDENCE

In graphical models, independence between random variables is defined using the concept of 𝑑-separation. For a definition and analysis of 𝑑-separation see [15]. We use 𝑋 ⊥ 𝑌 | 𝑍 to denote that 𝑋 is independent of 𝑌 given 𝑍 . In our proofs we used the following independence relationships: • • • • • •

𝑗

𝐻𝑡𝑖 ⊥ 𝐻𝑡 | O1:𝑡 𝑂𝑡𝑖 ⊥ O𝑡−𝑖 | 𝐻𝑡𝑖 𝐻𝑡𝑖 ⊥ O𝑡−𝑖 | O1:𝑡 −1 𝑂𝑡𝑖 ⊥ O𝑡1:𝑡 −1 | 𝐻𝑡𝑖 𝑗 𝑗 (𝐻𝑡𝑖 , 𝑂𝑡𝑖 ) ⊥ (𝐻𝑡 , 𝑂𝑡 ) | O1:𝑡 −1 𝑖 𝑗 H ⊥H |O

Apart from checking the above relationships using the rules of 𝑑-separation, we also checked them using independence checker programs that are freely available online.

Dappendix FOR SECTION 4 D.1 Expectation step Calculating the posterior. Using the definition of conditional probability we have that the posterior can be written as Pr(H | O) =

Pr(H, O) . Pr(O)

(27)

KDD ’24, August 25-29, 2024, Barcelona, Spain

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

Now, using the structure of the graphical model (see Fig. 1), we can decompose the joint probability of the variables as a product of probabilities where each variable is conditioned on its parent nodes [15]. Thus, we have Pr(H, O) = Pr(H1 )

𝑇 Ö 𝑛 Ö

Pr(𝑂𝑡𝑖 | 𝐻𝑡𝑖 )

𝑡 =1 𝑖=1

𝑇 Ö 𝑛 Ö

Pr(𝐻𝑡𝑖 | 𝐻𝑡𝑖 −1, O𝑡 −1 )

(28)

𝑡 =2 𝑖=2

Thus, the difficulty of sampling from the posterior stems from the denominator Pr(O) which can be written as Ö Pr(O) = Pr(O1 ) Pr(O𝑡 | O1:𝑡 −1 ).

(29)

In general, calculating Pr(O) is difficult, however in our model it can be done efficiently by calculating Pr(O𝑡 | O1:𝑡 −1 ). We do this as follows. First, we define the forward parameters 𝑛 Ö Pr(H𝑡 | O1:𝑡 ) = Pr(𝐻𝑡𝑖 | O1:𝑡 ), (30) 𝑖=1

where we used the independence

𝑗 and 𝐻𝑡 given O1:𝑡 . Pr(𝐻𝑡𝑖 | O1:𝑡 ) = Pr(𝐻𝑡𝑖 |

of 𝐻𝑡𝑖

= = =

Pr(O𝑡 |

We now calculate Pr(𝐻𝑡𝑖 |O1:𝑡 −1 ). O1:𝑡 −1, O𝑡 )

(31)

𝐻𝑡𝑖 , O1:𝑡 −1 )Pr(𝐻𝑡𝑖

(32)

| O1:𝑡 −1 ) Pr(O𝑡 | O1:𝑡 −1 ) Pr(O𝑡−𝑖 | O1:𝑡 −1 )Pr(𝑂𝑡𝑖 | 𝐻𝑡𝑖 , O1:𝑡 −1 )Pr(𝐻𝑡𝑖 | O1:𝑡 −1 ) Pr(𝑂𝑡𝑖 | O1:𝑡 −1 )Pr(O𝑡−𝑖 | O1:𝑡 −1 ) Pr(𝑂𝑡𝑖 | 𝐻𝑡𝑖 )Pr(𝐻𝑡𝑖 | O1:𝑡 −1 ) , Pr(𝑂𝑡𝑖 | O1:𝑡 −1 )

(33)

(34)

where in the second equation we used Bayes’ rule, in the third equation we used the independence between 𝑂𝑡𝑖 and O𝑡−𝑖 given O1:𝑡 −1 and the independence of O𝑡−𝑖 and 𝐻𝑡𝑖 given O1:𝑡 −1 , and in the last equation we used the independence of 𝑂𝑡𝑖 and O1:𝑡 −1 given 𝐻𝑡𝑖 . Furthermore, we have ∑︁ Pr(𝐻𝑡𝑖 | O1:𝑡 −1 ) = Pr(𝐻𝑡𝑖 | 𝐻𝑡𝑖 −1 = ℎ, O1:𝑡 −1 )Pr(𝐻𝑡𝑖 −1 | O1:𝑡 −1 ), (35) ℎ∈ H

Pr(𝐻𝑡𝑖 −1

where | O1:𝑡 −1 ) can be calculated recursively. We also have Pr(H𝑡 , O𝑡 | O1:𝑡 −1 ) = =

=

𝑛 Ö 𝑖=1 𝑛 Ö 𝑖=1 𝑛 Ö

Pr(𝐻𝑡𝑖 , 𝑂𝑡𝑖 | O1:𝑡 −1 )

(36)

Pr(𝑂𝑡𝑖 | 𝐻𝑡𝑖 , O1:𝑡 −1 )Pr(𝐻𝑡𝑖 | O1:𝑡 −1 )

(37)

Pr(𝑂𝑡𝑖 | 𝐻𝑡𝑖 )Pr(𝐻𝑡𝑖 | O1:𝑡 −1 ),

(38)

𝑖=1 𝑗

𝑗

where in the first equation we used the independence of (𝐻𝑡𝑖 , 𝑂𝑡𝑖 ) and (𝐻𝑡 , 𝑂𝑡 ) given O1:𝑡 −1 , and in the third equation we used the independence of 𝑂𝑡𝑖 and O1:𝑡 −1 given 𝐻𝑡𝑖 . Moreover, we have Pr(H𝑡 , O𝑡 | O1:𝑡 −1 ) Pr(H𝑡 | O1:𝑡 ) = (39) Pr(O𝑡 | O1:𝑡 −1 ) Having computed Pr(H𝑡 | O1:𝑡 ) and Pr(H𝑡 , O𝑡 | O1:𝑡 −1 ) we can calculate Pr(O𝑡 | O1:𝑡 −1 ) using the above equation. Thus, we can compute Pr(O) and the posterior distribution. The E-step concludes by defining 𝑄 (𝚯 | 𝚯old ) as the expected value of the log likelihood function of 𝚯, with respect to the current conditional distribution of H given O and the current estimates of the parameters: 𝑄 (𝚯 | 𝚯old ) = EH∼Pr(H|O,𝚯old ) [log Pr(H, O | 𝚯)]

(40)

In practice, we estimate the expectation by drawing samples from the posterior distribution Pr(H | O, 𝚯old ), and using the empirical mean. To this end, we next show how to generate samples from the posterior distribution. Sampling from the posterior. We are now ready to prove Lemma 2 that allows us to decompose the posterior distribution into products of simpler distributions.

Understanding team collapse via probabilistic graphical models

KDD ’24, August 25-29, 2024, Barcelona, Spain

Proof. First, based on the previous analysis, we have Pr(O𝑡 | O1:𝑡 −1 ) = =

=

Pr(H𝑡 , O𝑡 | O1:𝑡 −1 ) Pr(H𝑡 | O1:𝑡 ) 𝑛 Ö Pr(𝐻 𝑖 , 𝑂 𝑖 | O1:𝑡 −1 ) 𝑡

(41)

𝑡

(42)

Pr(𝐻𝑡𝑖 | O1:𝑡 )

𝑖=1 𝑛 Ö

Pr(𝑂𝑡𝑖 | 𝐻𝑡𝑖 )Pr(𝐻𝑡𝑖 | O1:𝑡 −1 ) . Pr(𝐻𝑡𝑖 | O1:𝑡 ) 𝑖=1

(43)

Hence, the evidence becomes Pr(O) =

=

=

𝑇 Ö

Pr(O𝑡 | O1:𝑡 −1 )

(44)

𝑡 =1 𝑇 Ö 𝑛 Ö

Pr(𝐻𝑡𝑖 , 𝑂𝑡𝑖 | O1:𝑡 −1 ) Pr(𝐻𝑡𝑖 | O1:𝑡 ) 𝑡 =1 𝑖=1 𝑇 Ö 𝑛 Ö Pr(𝑂 𝑖 | 𝐻 𝑖 )Pr(𝐻 𝑖 | O1:𝑡 −1 ) 𝑡

𝑡 =1 𝑖=1

𝑡

(45)

𝑡

.

Finally, substituting the above into the definition of the posterior distribution and combining with the joint distribution, we have Pr(H, O) 𝑃𝑟 (H | O) = Pr(O) 𝑇 Ö 𝑛 Ö Pr(𝑂𝑡𝑖 | 𝐻𝑡𝑖 )Pr(𝐻𝑡𝑖 | 𝐻𝑡𝑖 −1, O𝑡 −1 ) = 𝑖 𝑖 𝑖 𝑖 𝑡 =1 𝑖=1 Pr(𝑂 𝑡 | 𝐻𝑡 )Pr(𝐻𝑡 | O1:𝑡 −1 )/Pr(𝐻𝑡 | O1:𝑡 ) =

(46)

Pr(𝐻𝑡𝑖 | O1:𝑡 )

𝑇 Ö 𝑛 Pr(𝐻 𝑖 | O )Pr(𝐻 𝑖 | 𝐻 𝑖 , O Ö 1:𝑡 𝑡 𝑡 𝑡 −1 𝑡 −1 ) 𝑖 |O Pr(𝐻 1:𝑡 −1 ) 𝑡 𝑡 =1 𝑖=1

(47)

(48)

(49) □

. Thus, we

sample 𝐻𝑡𝑖

from a propability distribution that is proportional to Pr(𝐻𝑡𝑖 = ℎ | O1:𝑡 )Pr(𝐻𝑡𝑖 = ℎ | 𝐻𝑡𝑖 −1, O𝑡 −1 ) . Pr(𝐻𝑡𝑖 = ℎ | O1:𝑡 −1 )

(50)

Ereal-WORLD EXPERIMENTS E.1 Team structures Figure 12 presents the structure matrix for all 30 NBA teams in our dataset. As discussed in Section 5 there are two main profiles and each team can be thought of as falling closer to one of them. For example the Cleveland Cavaliers, fall closer to the profile we saw for the Dallas Mavericks, but with the added difference that two of their players also depend slightly to their own observed state (not only their hidden state). At the same time, Houston Rockets are closer to the profile we saw for the Boston Celtics, where the observed state of Martin seems to impact the state of his teammates.

E.2

Additional examples of specific games

The following figure provides some additional examples of games with the inferred from our model team state. As we can see here also, the team states inferred from our model follows closely in the vast majority of the cases the observed score differential at the game. All in all, the expressivity of our model is very good and can explain well the observed output of the game.

KDD ’24, August 25-29, 2024, Barcelona, Spain

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

1.0 M. Smart

1.0 S. Dinwiddie

0.8

C. Thomas

J. Brown

0.4 0.2

0.2

D.

(b) Brooklyn Nets

1.0

1.0

## I. Quickley

T. Maxey

0.8

E. Fournier

0.8

M. Thybulle

R. Barrett 0.4

0.6 Players

J. Randle

D. Green 0.4 T. Harris

0.2

(c) New York Knicks

mb iid

arr is

0.0

J. E

T. H

D.

Gr ee n

e ull

M.

Th

T. M

M.

Players

yb

0.0

r_i

on

0.2

J. Embiid

Ro b

ins

dle

J. R an

arr ett

Fo urn

E.

R. B

ier

y kle I. Q

uic

r_i

M. Robinson

ax ey

Players

0.6

Players

(d) Philadelphia 76ers

1.0

1.0 F. VanVleet

C. White

0.8

0.8

Z. LaVine

G. TrentJr.

0.6

O. Anunoby 0.4

Players

0.6 J. Green

0.4 D. DeRozan

(e) Toronto Raptors

ev ic

N.

Vu c

n De

(f) Chicago Bulls

Figure 12: Team structure R

Ro za

n ree J. G

La Vin e Z.

Players

D.

Players

ite

0.0

Wh

a

P. A ch iuw

S.

Ba

rne s

by nu no

O. A

Tre ntJ r.

G.

et Vle F. V an

0.2

N. Vucevic

C.

0.2

P. Achiuwa

r_i

S. Barnes

r_i

Players

0.0

Fin n

M. Players

(a) Boston Celtics

ey -Sm ith N. Cla xto n

es Bri

dg

as om Th

C.

S.

ord

Din

0.0

ie

r_i

N. Claxton

A. H

Wi llia G.

J. B

M.

for d

ms

n J. T atu m

row

art Sm

r_i

Players

0.4 D. Finney-Smith

G. Williams A. Hordford

M. Bridges

wid d

J. Tatum

0.6 Players

0.6 Players

0.8

0.0

Understanding team collapse via probabilistic graphical models

KDD ’24, August 25-29, 2024, Barcelona, Spain

1.0 D. Garland

1.0 K. Hayes

0.8

C. Cunningham

L. Markanen

0.4 0.2

I. S

J. G

tew

ran

art

t

y

m

Be

S.

ha

C.

E. Players

(a) Cleveland Cavaliers

Players

(b) Detroit Pistons

1.0 M. Brogdon

1.0 J. Holiday

0.8

0.4

0.4 G. Antetokounmpo

D. Sabonis 0.2

0.2

Po rt

is

o

B.

An

K.

tet

Mid

ok ou

dle

nm p

en All

y da oli

0.0

Players

Players

(c) Indiana Pacers

G.

D.

M.

Sa

J. H

Tur ne r

nis bo

set ris

O. B

C.

M.

t

e Du

art

on Bro

gd

r_i

0.0

ton

B. Portis

r_i

M. Turner

K. Middleton

G.

O. Brissett

0.6 Players

0.6 Players

0.8

G. Allen

C. Duarte

(d) Milwaukee Bucks

1.0

1.0 T. Young

L. Ball

0.8

B. Bogdanovic

0.4 D. Gallinari

0.6 Players

K. Huerter

0.8

T. Rozier

0.6

K. OubreJr. 0.4 M. Bridges

0.2

C. Capela

0.2

(e) Atlanta Hawks

(f) Charlotte Hornets

Figure 13: Team structure R

ee ml

M.

Plu

dg es Bri

Jr.

Players

Players

M.

bre

K.

Ou

er

Ba ll

T. R ozi

C.

L.

r_i

ela

0.0

Ca p

ari

D.

Ga

llin

r

Hu ert e

K.

no gd a

B.

Bo

T. Y o

un

g

vic

M. Plumlee r_i

Players

0.0

Cu

nn

K.

Mo

es

r_i

0.0

ing

n

0.2

## I. Stewart

J. A

lle

ble

y

ko ro

I. O

rka n

L.

D.

Ma

Ga

rla n

en

d

r_i

0.4 J. Grant

E. Mobley J. Allen

S. Bey

Ha y

## I. Okoro

0.6 Players

0.6 Players

0.8

0.0

KDD ’24, August 25-29, 2024, Barcelona, Spain

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

1.0

1.0 K. Lowry

C. Anthony

0.8

T. Herro

0.8

G. Harris

J. Butler 0.4

0.6 Players

P. Tucker

F. Wagner 0.4 W. CarterJr.

0.2

(a) Miami Heat

a mb

M.

(b) Orlando Magic

1.0

1.0 R. Neto

M. Morris

0.8

K. Caldwell-Pope

0.4

0.6 Players

K. Kuzma

J. Green 0.4 A. Gordon

0.2

D. Gafford

0.2

(c) Washington Wizards

Jok

ic

0.0

N.

n

Players

A. Go rdo n

Mo

Players

J. G ree

art on

r_i

D.

M.

K.

W. B

rd Ga

ffo

ma K.

Ku z

pe Av dij a D.

0.0

Ca

ldw

ell

R. N

-Po

eto

r_i

N. Jokic

rris

Players

D. Avdija

0.8

W. Barton

0.6

(d) Denver Nuggets

1.0 D. Russell

1.0 S. Gilgeous-Alexander

0.8

0.8

L. Dort

A. Edwards

0.4

(e) Minnesota Timberwolves

Players

(f) Oklahoma City Thunder

Figure 14: Team structure R

rl

y

-Ea on ins

J. R ob

an d L. er Do rt

lex s-A ou Gil

ge

Tow ns

K.

rbi lt

0.0 S.

Players

J. V an de

aro lm

L.

Bo

ard s

l

A. E

dw

sel Ru s D.

r_i

r_i

0.2

zle

J. Robinson-Earl

Ba

0.2

D.

D. Bazley

ey

0.4 J. Vanderbilt K. Towns

J. Giddey

J. G idd

L. Bolmaro

0.6 Players

0.6 Players

0.0

Ba

art e

rJr.

r

Players

W. C

C.

ne

rris

F. W ag

An

Ad e B.

Players

Ha

0.0

G.

ba

0.2

M. Bamba

r_i

yo

r cke P. T u

J. B utl er

K.

T. H

err o

Lo wr y

r_i

B. Adebayo

tho ny

Players

0.6

0.0

Understanding team collapse via probabilistic graphical models

KDD ’24, August 25-29, 2024, Barcelona, Spain

1.0 D. Lillard

1.0 M. Conley

0.8

D. Mitchell

A. Simons

0.2

gd Bo

ert ob

B.

(b) Utah Jazz

1.0

1.0 S. Curry

E. Bledsoe

0.8

J. Poole

0.8

R. Jackson

A. Wiggins 0.4

0.6 Players

O. PorterJr.

T. Mann 0.4 M. Morris

0.2

ac ub

0.0

I. Z

rris M.

Mo

an n T. M

R. Ja

cks

ds Ble

Lo o

K.

(c) Golden State Warriors

on

0.0

r_i

ne y

r. erJ

0.2

## I. Zubac

E.

Players

O. Po rt

A. Wi gg

ins

le J. P oo

rry S.

Cu

r_i

K. Looney

oe

Players

0.6

Players

(d) LA Clippers

1.0

1.0 R. Westbrook

T. Maxey

0.8

M. Monk

0.8

M. Thybulle 0.6 0.4

C. Anthony

0.6 Players

L. James

D. Green 0.4 T. Harris

0.2

A. Davis

0.2

Players

(e) Los Angeles Lakers

Players

(f) Phoenix Suns

Figure 15: Team structure R

iid J. E mb

is arr T. H

n

D.

Gr ee

ull e yb Th

M.

T. M ax ey

r_i

is

A. Da v

tho ny

0.0

C.

An

es Jam L.

Mo nk

M.

R. We st

bro

ok

J. Embiid r_i

Players

0.0

R. G

an

'Ne

D.

Players

(a) Portland Trail Blazers

ov ic

ale

ell ch Mit

Co M.

R. O

r_i

ic

0.0

J. N

ov ing

urk

ton

ell

0.2

R. Gobert

R. C

N.

Po w

s on im

A. S

D.

Lill

ard

r_i

Players

0.4 B. Bogdanovic

R. Covington J. Nurkic

R. O'Neale

y

0.4

nle

N. Powell

0.6 Players

0.6 Players

0.8

0.0

KDD ’24, August 25-29, 2024, Barcelona, Spain

Iasonas Nikolaou, Konstantinos Pelechrinis, and Evimaria Terzi

1.0 D. Fox'

1.0 L. Doncic

0.8

J. Brunson

T. Haliburton

0.4 0.2

0.2

(a) Sacramento Kings

ey -Sm it D. h Po we ll

oc

Players

Fin n

(b) Dallas Mavericks

1.0 K. PorterJr.

1.0 J. Morant

0.8

K. Martin 0.4

0.6 Players

0.6

Z. Williams 0.4 J. JacksonJr.

J. Tate 0.2

Players (c) Houston Rockets

ms Ad a

0.0

S.

ac

kso nJr .

ms

Players

J. J

Z.

D.

J. M

Wi llia

Ba n

e

nt

0.0

r_i

d

0.2

S. Adams

C.

Wo o

J. T ate

J. G ree n K. Ma rtin

K.

Po rt

erJ

r.

r_i

C. Wood

ora

Players

0.8

D. Bane

J. Green

(d) Memphis Grizzlies

1.0 D. Graham

1.0 D. Murray

0.8

0.8

L. WalkerIV

J. Hart

0.6

B. Ingram 0.4

Players

0.6 K. Johnson

0.4 D. McDermott

ltl

J. P oe

De Mc

(f) San Antonio Spurs

Figure 16: Team structure R

rm ott

ns on

Players

D.

K.

Joh

V Wa lke rI

rra y

L.

J. V ala n

(e) New Orleans Pelicans

Mu

s na

0.0

ciu

s ne H. Jo

ram B.

Ing

art J. H

am Gr ah D.

Players

0.2

J. Poeltl

D.

0.2

J. Valanciunas

r_i

H. Jones

r_i

Players

0.0

D.

Players

ull

R. B

run J. B

Do

C.

son

ic

r_i

0.0

k

D. Powell

L.

Me

tu

s arn e

ess

H. B

on

Ha rkl

urt

M.

T. H ali b

D.

Fox '

r_i

0.4 D. Finney-Smith

H. Barnes C. Metu

R. Bullock

nc

M. Harkless

0.6 Players

0.6 Players

0.8

0.0

0.8

KDD ’24, August 25-29, 2024, Barcelona, Spain

team state 6 PTS +/4

0.6

0.6

0.2

PTS +/-

Team state

0.4

0.0

Team state

0.4

team state 7.5 PTS +/5.0

0.2

2.5

0.0

0.0

2.5

0.2

0.4

7.5

Window

0.6

(a) Denver Nuggets vs Los Angeles Lakers(11 Jan 2022)

team state PTS +/-

0.6

0.8

Window

(c) Miami Heat vs Boston Celtics (23 May 2022)

Team state

Team state

0.4

Window

team state 4 PTS +/2

0.0

0.2

0.2

0.0

(b) Dallas Mavericks vs Golden State Warriors (20 May 2022)

PTS +/-

0.2

5.0

0.4

0.2

PTS +/-

0.2

PTS +/-

Understanding team collapse via probabilistic graphical models

0.4

0.6

0.8

Window

(d) Milwaukee Bucks vs Boston Celtics (15 May 2022)

Figure 17: Team collapse games
