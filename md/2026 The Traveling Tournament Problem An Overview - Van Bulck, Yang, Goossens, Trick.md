<!-- source: 2026 The Traveling Tournament Problem An Overview - Van Bulck, Yang, Goossens, Trick.pdf -->
<!-- arxiv: https://arxiv.org/abs/2609.03612 -->

This paper is dedicated to Dr. Kelly Easton who was instrumental in defining the Traveling Tournament Problem, in providing early results on the problem, and in using those results in real-world sports schedules. Her tragically early passing in February 2026 was a tremendous loss both personally and for the sports scheduling field.

The Traveling Tournament Problem: An Overview

arXiv:2609.03612v1 [math.OC] 3 Sep 2026

David Van Bulcka,b , Fan Yangc,∗, Dries Goossensa,b , Michael Trickd a

Faculty of Economics and Business Administration, Ghent University, Ghent, Belgium b FlandersMake@UGent – core lab CVAMO, Ghent, Belgium c School of Finance and Business, Shanghai Normal University, Shanghai, China d Carnegie Mellon University in Qatar

Abstract Over the past 25 years, the Traveling Tournament Problem (TTP) has become one of the most extensively studied optimization problems in sports scheduling. At its core, the TTP seeks to minimize the total travel distance incurred by teams that travel directly between opponents’ venues during consecutive away games. The problem originated from the scheduling challenges faced by Major League Baseball, where it was identified as the central computational difficulty. This paper provides a comprehensive overview of the literature on the TTP. We review the principal problem variants and benchmark instances, and summarize the current state of the art in lower bounds, approximation guarantees, and exact and heuristic optimization algorithms. Moreover, we contribute to the continued development of the field by tracking and validating lower and upper bounds, while succeeding the repository originally established by Prof. Michael Trick as part of the RobinX sports timetabling project. Finally, we identify several open questions and outline promising directions for future research. Keywords: sports timetabling, travelling tournament problem, travel, lower bound, approximation, open problem

1. Introduction In 1995, a seemingly simple question emerged from Major League Baseball (MLB): could operations research techniques be used to create a timetable for its league? What followed was a decade-long struggle that did not result in a schedule for MLB (that would come later), but did give rise to one of the most extensively studied optimization problems in sports scheduling: the Traveling Tournament Problem (TTP). The TTP, formally introduced in the seminal paper of Easton et al. (2001), asks for a compact double round-robin tournament that minimizes the overall ∗

Corresponding author Email addresses: david.vanbulck@ugent.be (David Van Bulck), fan_yang@shnu.edu.cn (Fan Yang), dries.goossens@ugent.be (Dries Goossens), trick@cmu.edu (Michael Trick)

mo

mi

mo

mi

ny pi

ch

ny pi

ch

ph

ci

ph

ci

st

st

at

at

fl

fl

(a) Input. Pairwise travel distances between the teams, here visualized by the distances between the teams’ home locations

(c) Visualization of the road trips for team CI in the timetable provided below

(b) An optimal timetable. The first team in parentheses is the home team, the second the away team. The away games of team CI are typeset in bold. The maximal sequence of home and away games is limited to three. R1

R2

R3

R4

R5

R6

R7

R8

R9

1 (AT,CH) (AT,MI) (AT,FL) (NY,ST) (NY,MO) (NY,CI) (AT,PH) (AT,NY) (AT,PI) 2 (MO,PH) (MO,ST) (PH,ST) (PH,MO) (PH,CI) (FL,PH) (MO,CI) (FL,PI) (PH,NY) 3 (FL,MI) (FL,CH) (MO,NY) (CI,FL) (CH,PI) (PI,MO) (FL,NY) (CI,PH) (CI,ST) 4 (PI,CI) (PI,PH) (PI,CH) (CH,AT) (ST,FL) (ST,AT) (PI,MI) (CH,MO) (CH,FL) 5 (ST,NY) (CI,NY) (CI,MI) (MI,PI) (MI,AT) (MI,CH) (CH,ST) (MI,ST) (MI,MO)

R10

R11

R12

R13

(NY,AT) (PH,CH) (CI,MO) (ST,PI) (MI,FL)

(NY,CH) (PH,MI) (MO,AT) (PI,FL) (ST,CI)

(NY,MI) (MO,CH) (FL,CI) (PI,AT) (ST,PH)

(AT,CI) (MO,MI) (FL,ST) (PI,NY) (CH,PH)

R14

R15

R16

R17

R18

(AT,ST) (AT,MO) (NY,FL) (NY,PI) (NY,PH) (FL,MO) (PH,FL) (PH,PI) (PH,AT) (MO,PI) (CI,PI) (PI,ST) (CI,AT) (MO,FL) (FL,AT) (CH,NY) (CI,CH) (CH,MI) (CH,CI) (ST,CH) (MI,PH) (MI,NY) (ST,MO) (ST,MI) (MI,CI)

Figure 1: Example of a problem instance with 10 teams (NL10) together with an optimal solution and a visualization of the road trips for one particular team

distance traveled by the teams. That is, over the course of the season, each of an even number of teams plays every other team once at home and once away, and it plays exactly one game per round. In order to minimize travel, teams are allowed to group away games into a road trips: when consecutively playing away, teams move directly between the opponent’s venues, without returning home. Two additional constraints make the problem realistic. First, to avoid excessive travel fatigue, long periods without home games for the fans, and too many consecutive home games, no team is allowed to play more than a given number of consecutive home or away games. Second, for reasons of game attractiveness and fairness, no two teams may play each other in consecutive rounds. For an example of the input of the problem, a round-robin timetable solution, and the individual road trips of a particular team, we refer to Figure 1. Although the problem is deceptively simple to describe, it is notoriously difficult to solve. To understand part of its difficulty, observe that each team in itself solves a vehicle routing problem: using its own venue as the ‘depot’, it visits every other team in road trips with a given maximal length (the ‘capacity’ of the vehicles), while minimizing travel distance. Yet the teams individual routing problems cannot be solved separately, because every team plays a game in every round, so the trips of one team dictate which other teams have to be home and thus cannot be on a road trip themselves. And as schedulers discovered the hard way, timetables are inherently fragile: even a minor modification in one game triggers a cascade of changes that may ultimately compromise the quality or even the feasibility of the resulting schedule. As a result, the largest TTP real-distance instance solved to optimality contains merely 10 teams. This is a surprisingly small number, especially in light of the vehicle routing problem where instances involving hundreds of customers are now routinely solved to optimality. The TTP continues to attract a steady stream of research: over the past 25 years, it has 2

281

258 223

184

81 51 2000-2004 2005-2009 2010-2014 2015-2019 2020-2024

2025-

Figure 2: Number of Google Scholar hits for ‘"Traveling Tournament Problem" OR "Travelling Tournament Problem"’, per five-year periods

accumulated more than a thousand Google Scholar hits (Figure 2 gives the evolution per five-year period). In our view, the literature on the TTP can be organized into three broad research waves. During a first wave, roughly spanning the first decade of research (2000-2009), the focus was mostly on metaheuristics. This wave resulted in the first dedicated non-trivial neighborhoods for sports scheduling, respecting the elementary round-robin structure of the timetable and applicable more broadly than for the TTP alone. Successful applications include simulated annealing, GRASP, and tabu search (see e.g., Anagnostopoulos et al. (2006), Di Gaspero & Schaerf (2007), Ribeiro & Urrutia (2007)). In a second wave, roughly spanning 2008 to 2012, the emphasis shifted towards exact methods. Building on earlier branch-and-price ideas by Easton et al. (2003), in 2008 Irnich (2010) succeeded to prove optimality for the eight-team NL8 instance. One year later, a provenly optimal solution to the NL10 instance was found by Uthus et al. (2009, 2012) employing deptfirst and best-first search algorithms. A third and ongoing wave, starting around 2010, concerns the theoretical analysis of the problem, including the first complexity proofs for the unconstrained variant by Bhattacharyya (2009, 2016) and a growing body of results on approximation algorithms (e.g., Miyashiro et al. (2012), Westphal & Noparlik (2014), Zhao et al. (2025)) and inapproximability (e.g., Bendayan et al. (2023), Zhao & Xiao (2025b)). With this growing body of literature, we believe an overview of the field is timely. Indeed, to the best of our knowledge, no comprehensive overview on the TTP exists. The aim of this paper is to fill this gap and to provide a guide for researchers who wish to start working on the TTP. The remainder of this paper is organized as follows. Section 2 recounts how the TTP came into existence. Section 3 introduces the formal problem definition, reviews the principal problem variants, and presents the benchmark instances that are commonly used in the literature. Section 4 surveys the lower bounds that have been proposed for the TTP, followed by an overview of the approximation results in Section 5. Section 6 gives an overview of the exact and heuristic optimization algorithms that have been developed. Finally, Section 7 concludes and discusses directions for future research. Throughout the paper, we identify seven open problems, drawn either from the literature or from questions that we believe deserve attention in the years to come. Beyond the survey itself, this paper contributes to the community in a concrete way: it brings together all commonly used TTP instances and their best-known solutions, including previously lost instance classes as well as full solutions rather than merely objective values, and computes lower bounds for instances for which none or only weaker ones existed. Moreover, it takes over the maintenance of the repository started by Prof. Michael Trick, which now officially lives on as part of the RobinX sports timetabling project (see www.robinxval.ugent.be/RobinX/travelRepo.php). 3

2. Origins of the traveling tournament problem Although some earlier papers address travel minimization for teams undertaking road trips inspired by real-world sports tournaments, e.g., Campbell & Chen (1976) (basketball) and Russell & Leung (1994) (baseball), the TTP is first formally defined by Easton et al. (2001). The authors were inspired by a request to schedule the Major League Baseball (MLB), which Prof. Michael Trick received from Doug Bureman, an executive with a local MLB team, in 1995. In Trick’s own words, the Traveling Tournament Problem originated as follows. When Doug approached me in 1995, I was full of confidence that I could schedule Major League Baseball. I figured I could put together a quick greedy algorithm followed by local search, perhaps with simulated annealing (then about 10 years old) that would clearly get good answers reasonably quickly. I knew that Henry and Holly Stephenson, baseball’s schedulers, used computers to count aspects of the schedule, but the bulk of the work was based on hand-generated patterns that they laboriously put together. Thus, I was certain that my vast array of operations research techniques could create better schedules, faster. But it was not the case. Very quickly, I realized that it was not straightforward to create a local search algorithm. Given a schedule, simply exchanging the opponents on two games led to a cascading set of necessary changes that might not result in a feasible schedule. And even creating a greedy heuristic seemed difficult: when scheduling week-by-week, it didn’t take long to reach a point where the schedule could not be completed. Stymied on the heuristic front, I returned to an integer programming approach. And here I received another shock: the integer programs I formulated not only could not be solved to optimality, but the software never even came back with feasible integer solutions. When I created the integer programs, I included everything Major League Baseball required in a schedule. In addition to scheduling the 2,430 games, there were many, many additional requirements, including that every team must play half their weekends at home, that stadiums are sometimes unavailable for home games, and that teams do not want to travel too far. I did learn some key aspects that made things a bit simpler. In baseball, teams typically played 2 to 4 games against a single opponent (a series) before moving on to the next opponent. So instead of 2,430 games, I was really trying to schedule 780 series. Better, initially MLB had 2 leagues that did not play each other, so I was really trying to schedule a 14 team league and a 16 team league (with weak interaction due to the two team cities), not a 30 team league. I also learned that I had to have variables that represented “trips” that teams took, rather than individual series. So if team A went to team B, then C, then D before returning home, then that road trip could be represented by a single integer variable. But, despite all I had learned, and continuing improvements in the underlying solver, I still got nowhere in solving the integer programs. The solver would branch and branch and branch without improving the lower bound (where the objective was primarily to minimize distance traveled) and without finding a feasible solution for an upper bound. Of course, being an academic, this failure to find anything approaching a useful approach didn’t stop me from presenting the work at various conferences and workshops. More importantly, I began working with George Nemhauser, a famous person in integer programming circles, and Kelly Easton (then a doctoral student) on scheduling other leagues. It turned out that while MLB was out of reach, 4

integer programming methods could work wonders for smaller leagues, and we began scheduling college sports leagues. The schedules we created were much better than the hand-schedules being used, and quickly multiple college leagues played our schedules. But Major League Baseball continued to haunt us. In 1999, I did what I should have done much earlier: I started to explore why my integer programs were hard to solve. I decided to start removing constraints until I got down to a solvable problem. I took away the weekend constraints, and then the team requests, and so on and so on. Surprisingly, I realized I could take away almost everything and still end up with an unsolvable problem. In fact, even when I reduced the problem to a double round-robin (instead of the quadruple round-robin that then made up the MLB schedule), as long as I tried to find a schedule with minimum distance traveled, I could not even solve a six team instance to optimality! The problem was not with all the “complicating” constraints: the difficulty was with the underlying basic problem of finding minimum distance roundrobins. So the Traveling Tournament Problem was born: how to create such minimum distance round robins. We first formally presented this work as a short paper at the Constraint Programming Conference in 2001 (Easton et al., 2001). I was very worried that someone would quickly find a way to solve this problem, making the TTP irrelevant. As history would show, despite dozens of papers, no one has found a quick way to solve the instances we presented, and even finding provably optimal solutions to 12 team round robins remains beyond current capabilities. Twenty-five years after the TTP was first developed, it remains a rich source of inspiration for research in heuristic and optimization approaches. For Major League Baseball, ten years after my initial forays into the problem, our group finally created schedules that MLB would play. We would do so for almost all the next 12 years, before being supplanted by firms that continued to develop optimization approaches for this problem. 3. The TTP, problem variants, and instances 3.1. Preliminaries Let T be the set of teams, where |T | = n ≥ 4 is even, and R the set of rounds (often corresponding to weekends; also called time slots). During each round, a team can play at most one game. Furthermore, we define with D an n × n symmetric distance matrix, where element di,j ∈ D reflects the non-negative integer distance between the home venue of team i and team j. It is common in the TTP literature on lower bounds and approximation ratio’s to assume that D respects the triangle inequality (i.e., di,j + dj,k ≥ di,k ∀i, j, k ∈ T ), and that di,i = 0 for all i ∈ T . Nonetheless, there are benchmark instances that violate this assumption. A game is an ordered pair of teams (i, j) in which i ∈ T is the home team providing the venue where the game is played, and j ∈ T \ {i} is the away team. If a team plays two or more away games in a row, it has a road trip and travels directly from the venue of one opponent to the venue of the next opponent. We define a leg of a road trip as a single direct journey between two venues. For instance, the road trip of team CI to teams CH and MI in Figure 1c consists of legs CI-CH, CH-MI, and MI-CI. Similarly, a team has a home stand when it plays two or more consecutive games at home. It is assumed that all teams are initially at home, and that teams need to return home after playing their last away game. A double round-robin tournament (2RR) is a collection of games in which every team plays every other team exactly once at home and once away, and is called compact if it uses the minimum 5

number of rounds needed (i.e., 2n − 2 since we assume n even). Finally, the complete graph on n vertices is denoted by Kn . 3.2. Classic version of the problem The classic version of the TTP is defined as follows. Traveling Tournament with Maximal Trip Length k (TTP(k)) Input: Teams T and rounds R with |R| = 2n − 2, distance matrix D, and a non-negative integer k. Output: A compact 2RR timetable minimizing the sum of the distances travelled by all teams such that: C1 The length of home stands and road trips is at most k, and C2 No game (i, j) is immediately followed by game (j, i). Constraints C1 and C2 are referred to as the ‘at-most’ and ‘no-repeater’ constraints, respectively. Unless otherwise specified, this paper assumes that k = 3, which is by far the most studied case in the literature. Since no compact timetable exists that perfectly alternates between home and away games for all teams (see e.g., de Werra (1981)), it is clear that k must be greater than 1. The version of the problem without the at-most constraint (i.e., k = n − 1) is referred to as the unconstrained traveling tournament problem (UTTP). We note that the original description of the TTP by Easton et al. (2001) also includes a parameter to regulate the minimal length of home stands and road trips. However, this constraint has been ignored in the literature so far. With regard to the complexity status of TTP(k), the following results are known (for an overview of results, see Table 1). The first complexity proof is provided by Bhattacharyya (2009, 2016), who show that the UTTP is N P-hard by providing a reduction from the (1,2)-Traveling Salesman Problem (TSP). Thielen & Westphal (2011) provide a reduction from 3-SAT to TTP(3), showing that the TTP remains N P-hard for k = 3. Chatterjee (2021) generalizes this result for any fixed k > 3. The complexity status of TTP(2), though, is still open. Open Problem 1. Determine the computational complexity status of TTP(2), i.e., TTP(2)∈ P? On the positive side, several approximation algorithms are known for TTP(2) with an approximation ratio which goes to 1 as n increases to infinity (the earliest of which is due to Thielen & Westphal (2012)). This implies that TTP(2) has a PTAS (see Zhao & Xiao (2025b)). In contrast, Bendayan et al. (2023) show that the UTTP is APX-hard, thus no PTAS exists unless P = N P, solving an open problem raised by Imahori et al. (2014). This result has later been generalized to arbitrary k > 2 by Zhao & Xiao (2025b). 3.3. Problem variants There are several variants of the TTP that consider alternative constraints and tournament formats. One variant that has been particularly researched is the mirrored TTP (m-TTP), introduced by Ribeiro & Urrutia (2007). In this variant, the 2RR is divided into two phases, where the second phase is identical to the first except that the home and away teams are swapped for every match. The bipartite traveling tournament problem extends the TTP to competitions consisting of two leagues with dedicated and consecutive time slots for interleague games, where the interleague play is represented by a bipartite tournament (see Hoshino & Kawarabayashi (2011b)). Hoshino 6

Publications

TTP(2)

TTP(3)

TTP(k > 3)

UTTP (k = n − 1)

P vs. NP-hard ? Thielen & Westphal (2011) Chatterjee (2021) Bhattacharyya (2016) PTAS vs. APX-hard Thielen & Westphal (2012) Zhao & Xiao (2025b) Bendayan et al. (2023)

NP-hard NP-hard NP-hard PTAS APX-hard

APX-hard APX-hard

Table 1: Overview of complexity results.

& Kawarabayashi (2011a) propose the multi-round TTP which generalizes the TTP to l-RR tournaments where teams meet each other exactly l > 2 times (in the TTP, l = 2). Long before the introduction of the TTP, Russell & Leung (1994) already consider a variant that can now be seen as the TTP(2), however, focusing on a 1RR (i.e., l = 1) and additionally enforcing that each team plays approximately half of its games at home. Devriesere et al. (2026) introduce the TTP in the context of incomplete round-robin tournaments, in which fewer than n − 1 time slots are available and, consequently, not all teams can play each other; they term this variant the incomplete TTP. In contrast, Bao & Trick (2010) assume that there are more than 2n−2 time slots, meaning that teams no longer play on every time slot. This variant is known as the time-relaxed TTP (RTTP). Several other variants of the TTP assume that part of the timetable has already been fixed. For instance, the TTP with predefined-venues (TTP-PV) requires constructing a travel-minimal 1RR schedule for the second half of a phased tournament, where each pair of teams must play at the other team’s venue compared to their first match (see Melo et al. (2009)). The timetable constrained distance TTP seeks an optimal home-away assignment when the opponents of each team in each time slot are given (see Rasmussen & Trick (2008)). The TTP with trip preferences (TP-TTP) aims to create a travel-minimal timetable while ensuring that all road trips belong to a predefined set of trips. A real-life application of the TP-TTP in the context of Argentina’s professional basketball league is discussed in Durán et al. (2019). Osicka & Guajardo (2023) introduce fairness objectives to the TTP: rather than solely minimizing the overall distance traveled, they use a cooperative game theory approach to fairly distribute the travel distance over the teams. Finally, there is a large strand of literature that focuses on the Traveling Umpire Problem (TUP), which aims to assign umpires to games, given a timetable for the tournament. The goal is to minimize umpire travel while ensuring that no umpire handles the game of a particular team too frequently (see Trick et al. (2012)). Bender & Westphal (2016) propose an integration of the TTP with the TUP. 3.4. Common problem instances The popularity of the TTP is partly attributable to the availability of several well-known benchmark instances (see Table 2). Perhaps most known are the National League (NLx) problem instances proposed by Easton et al. (2001), which are based on the actual locations of Major League Baseball teams in the National League. Other instance classes that are based on real-life tournaments include the National Football League (NFLx, see Uthus et al. (2009)), Super 14 Rugby League (SUPx, see Uthus et al. (2009)), and Brazilian soccer championship (BRAx, Ribeiro & Urrutia (2007)). In addition, the Galaxy instances (GALx, see Uthus et al. (2012)) embed the team locations in a 7

Table 2: Overview of existing traveling tournament instance classes Abbreviation CONx CIRCx LINEx INCRx GALx NLx NFLx SUPx BRAx 1 1

Full name Constant distance instances Circular distance instances Linear distance instances Increasing distance instances Galaxy instances National League instances National Football League instances Super 14 Rugby League instances Brazilian soccer championship instances

1 1

4

1

2

1

3

1

Type

No. teams

Artificial Artificial Artificial Artificial Artificial Real-life Real-life Real-life Real-life

[4,40] [4,40] [4,40] [4,40] [4,40] [4,16] [4,32] [4,14] [4,24]

3 4

1

2 1

1

1 3

1

1

2

(a) CIRC4

2

3

3

(b) LINE4 and INCR4

4

1

1

4 1

1 1

2

(c) CON4

Figure 3: Graph representation of artificial TTP problem instances for which the associated TSP is trivial. Distance di,j is equal to the shortest path length between node i and j in the graph.

3D-coordinate space, where the distance matrix is based on the number of light-years between stars in the universe. The above instance classes pose significant challenges: the largest instance solved to proven optimality contains only ten teams. What if we add some topological structure to the instances, such that the associated TSP becomes trivial? In this light, Easton et al. (2001) introduce the circular distance instances (CIRCx) where teams are positioned on a circle and travel to other teams by moving along it (see also Figure 3). Following a similar idea, Hoshino & Kawarabayashi (2012) propose linear (LINEx) and incremental (INCRx) distance instances, where all teams are located on a straight line. In LINEx the distance between adjacent teams is always 1, whereas in INCRx the distance between adjacent teams increases by one unit at each step. However, even with this simplified structure, none of the instances with more than 10 teams has been solved to optimality so far. What if we completely ignore the distance matrix, by having a distance of 1 between any pair of teams? The resulting instances are known as the constant distance instances (CONx, see Urrutia & Ribeiro (2006)), and all optimal solutions are known for up to 16 teams. We refer to the TTP with constant distances as the CD-TTP. For more than twenty years, the website maintained by Prof. Michael Trick1 has tracked the best-known solutions for several of the above problem instances. As part of this project, this website has been transferred to RobinX2 (see Van Bulck et al. (2020)). RobinX offers many advantages over a plain-text only website, including XML-based storage of the problem instances and solutions (rather than just their objective values), and an online validator for checking solution feasibility. Moreover, missing instances have been included and several solutions and lower bounds have been 1 2

See https://mat.tepper.cmu.edu/TOURN/. See www.robinxval.ugent.be/RobinX/.

8

mo

mi ch st

pi

ny ph

ci

mi ch st

at

pi

ny ph

ci

fl

pi

mi ch st

ny ph

ci

at

at

(a) ILB(2) = matching

mo

mo

fl (b) ILB(3) = VRP

fl (c) ILB(n − 1)=TSP

Figure 4: Illustration of computation for the Independent Lower Bounds (ILB) for team CI

restored or even improved. For instance, we have included the LINEx and INCRx instance classes and in collaboration with Melo et al. we have retrieved several TTP-PV problem instances that had been lost and were therefore not available on Trick’s website. Moreover, lower bounds have been computed for the first time for several larger problem instances that had previously been considered computationally too demanding (see the next section). 4. Lower Bounds Independent lower bounds. Perhaps the most commonly used technique to obtain lower bounds in TTP is to sum over the minimum distance that each team needs to travel to visit every other team, while taking into account the maximum length of road trips but ignoring all other scheduling constraints. This approach results in the ‘independent lower bound’ (ILB), so named because it breaks down the TTP instance into n sub-problems that can be solved independently. Campbell & Chen (1976) and Ball & Webster (1977) independently observe that a maximum trip length of two (k = 2) requires every team to travel between their own venue and their opponent’s venue at least once (see the dotted edges in Figure 4a). In other words, summing over all teams, the total distance covered to move to the first opponent of each road trip P of length one or two and to return home at the end of each road trip of length two is given by ∆ = i,j∈T :i̸=j di,j . Disregarding the dotted edges, it becomes clear that a lower bound on the sum of travel from the first to the second opponent in each road trip of length two and returning home from a road trip of length one is given by a minimum cost matching, which can be found in polynomial time. Proposition 1 (ILB(2), Campbell & Chen (1976)). Denote by γ the minimum weight of a perfect matching in Kn . Every solution of the TTP(2) has a total length of at least ∆ + nγ. In contrast, for k > 2, Easton (2003) proves that computing the ILB is N P-complete in the strong sense for any constant k by providing a reduction from the N P-complete problem of partitioning a graph into isomorphic subgraphs restricted to paths. As noted in Urrutia et al. (2007), the ILB can be computed by solving n independent vehicle routing problems (VRP). More in particular, in the VRP of team i ∈ T , the venue of team i serves as the depot, all other teams act as customers with a demand of one, and each vehicle has a capacity of k (see Figure 4b). 9

Proposition 2 (ILB(k), Easton et al. (2003)). Let πi be the optimal solution value P for the VRP associated with team i. Every solution of the TTP(k) has a total length of at least i∈T πi . Considering the UTTP, computing the ILB becomes equivalent to solving a TSP (see Figure 4c). This results in the following lower bound, which is obviously also valid for TTP(k) as the UTTP is a relaxation. Proposition 3 (ILB(n − 1), Yamaguchi et al. (2011)). Let ρ be the length of an optimal TSP tour in Kn . Every solution of the UTTP has a total length of at least nρ. An interesting conjecture by Bao & Trick (2010) that, to the best of our knowledge, is still open is whether ILB(3) becomes tight when there are sufficiently more time slots than games per team. Open Problem 2. Determine whether there exists an α such that the ILB(k) is tight for RTTP(k) with 2n − 2 + α time slots, where α may depend on n and k. We have found the following results in the literature that are related to Open Problem 2. Using at most two byes per team, Campbell & Chen (1976) and Ball & Webster (1977) show how to construct a schedule for RTTP(3) that attains ILB(2). In contrast, computational experiments by Brandão & Pedroso (2014) show that there exist instances for which two byes per team do not suffice for RTTP(3) to attain ILB(3). Despite the fact that the independent lower bound can be quite strong in practice (for ILB(3) within 5% of the optimal value, according to Miyashiro et al. (2012)), it is generally not tight. This is due to cases where the individual teams’ road trips cannot be combined into a feasible timetable. For instance, with regard to TTP(2), Thielen & Westphal (2012) prove that ILB(2) cannot be attained if the perfect matching used to compute the bound is unique. Minimum number of legs. A special type of problem instances for which stronger lower bounds are known is the constant distance instances of the CD-TTP. In these instances, minimizing the overall travel distance is equivalent to minimizing the overall number of legs teams undertake during road trips. While Russell & Leung (1994) already show a relation between travel minimization and break maximization (a team is said to have a break if it plays two consecutive home games or two consecutive away games), Urrutia et al. (2007) are the first to prove break maximization is equivalent to travel leg minimization. Proposition 4 (Urrutia & Ribeiro (2006)). Denote by β and τ the total number of breaks and travel legs in a 2RR timetable, respectively. It holds that τ = n(2n − 2) − β/2. As a consequence, any upper bound on the maximum number of breaks in a 2RR timetable can be transformed into a lower bound on the minimum number of legs in the timetable. Indeed, a team can have at most 2n − 4 breaks in a 2RR schedule, which occurs when the team plays all its home games before playing all its away games (or vice versa). Moreover, since no two teams can play according to the same home-away pattern (see de Werra (1981)), the maximal number of breaks in a 2RR timetable is 2(2n − 4) + (n − 2)(2n − 5) = 2n2 − 5n + 2, which gives rise to the following proposition. Proposition 5 (Urrutia & Ribeiro (2006)). Every solution of the TTP(k) contains at least n2 + n/2 − 1 legs. 10

Urrutia & Ribeiro (2006) provide a constructive proof to show that this bound is tight for the UTTP, implying that the UTTP restricted to constant distance instances is solvable in polynomial time. Stronger bounds on the number of legs for TTP(3) are given by Fujiwara et al. (2007). Proposition 6 (Fujiwara et al. (2007)). Every solution of the TTP(3) has at least (4/3)n2 − n legs if n ≡ 0 mod 3, (4/3)n2 − 5/6n − 1 legs if n ≡ 1 mod 3, and (4/3)n2 − 2/3n legs if n ≡ 2 mod 3. These bounds are tight for all instances of n ≡ 1 mod 3, n ⩽ 50. For similar lower bounds for the mirrored CD-TTP, we refer to Urrutia & Ribeiro (2006). We note that Rasmussen & Trick (2007) and Van Bulck & Goossens (2023) further improve upon these bounds by considering logicbased and traditional Benders’ cuts. Moreover, when minimizing travel legs, Van Bulck & Goossens (2023) conjecture that it suffices to consider timetables where every team is paired with another that plays the exact opposite sequence of home and away games (referred to as a complementary Home/Away Pattern (HAP) set). Open Problem 3. Determine whether there always exists an optimal solution to CD-TTP(3) that has a complementary HAP set. Minimum number of legs lower bound. Urrutia et al. (2007) use optimal solution values (or lower bounds thereof) for the CD-TTP to strengthen the ILB. In particular, they propose to simultaneously compute the ILB for all teams, with the additional constraint that the overall number of legs made by all teams is at least equal to the optimal value in the associated CD-TTP instance. Even though its computation is considerably more challenging, the resulting bound, called the Minimum Number of Legs Lower Bound (MNLLB), often improves upon the ILB by several percentage points. Proposition 7. Let µn be a lower bound on the minimum number of legs in a 2RR timetable with n teams, and let τi be the total numberP of legs made by team i. Every solution of the TTP(k) has a  P total length of at least min i∈T τi ≥µn i∈T πi . The MNLLB is further enhanced by Cheung (2009), who add the requirement that a set of logicbased Benders’ cuts must be satisfied. Nevertheless, this complicates the computation even further, limiting the author to compute bounds only for m-TTP(3). During computational experiments with this code, however, we observe that the alternative IP formulation to compute the MNLLB provided by Cheung (2009) is substantially faster than the IP model provided by Urrutia et al. (2007). Together with the author, this enabled us to compute the MNLLB for several problem instances for which it was not computed before, resulting in several new best lower bounds, all of which have been added to the RobinX website. Other lower bounds. Several other lower bounds have been proposed in the literature on approximation algorithms, which are typically easier to compute. Although these bounds often perform worse than the ILB in practice, evaluating the worst-case behavior of an algorithm based on these bounds can still provide useful insights. As an overview of these bounds is currently missing, we provide it here. As each team needs to travel to the venue of every other team, a trivial lower bound on the total travel distance per team is the minimum spanning tree σ in Kn . Recalling that γ denotes the minimum weight of a perfect matching in Kn , Imahori (2021) shows that nσ + nγ is also a valid bound for TTP(2), but this bound is weaker than Proposition 1. Intuitively, spanning trees are cycle-free and thus ignore the fact that teams need to return home. Yamaguchi et al. (2011) exploit this to provide the bound in Proposition 8 (for a variant, see Zhao et al. (2025)). 11

Proposition 8 (Yamaguchi et al. (2011)). Let σ be the length of a minimum spanning tree in Kn and, given a solution, denote by dhome the total distances covered by team i to leave and return to i its home before and after P every road trip, respectively. Every solution of the TTP(k) has a total length of at least nσ + i dhome /2. i Alternatively, considering again the distances covered by the teams to leave and return to their home venues, Yamaguchi et al. (2011) propose the following bound (recall ∆ denotes the sum of all pairwise distances). Proposition 9P(Yamaguchi et al. (2011)). Every solution of the TTP(k) has a total length of at 2 least k−2 (∆ − i dhome ). i Miyashiro et al. (2012) prove that the optimal value of TTP(3) is larger than or equal to (2/3)∆. Westphal & Noparlik (2014) generalize this result for arbitrary k. Proposition 10 (Westphal & Noparlik (2014)). Every solution of the TTP(k) has a total length of at least 2∆ k . For completeness, we note that several techniques have been proposed for deriving lower bounds for specific distance matrices. Among them, the branch-and-price algorithm developed by Irnich (2010) and the depth-first search (DFS*) algorithm proposed by Uthus et al. (2009) have resulted in some of the best instance-specific lower bounds known to date. 5. Approximation Results The previous section focusses on the minimal travel distance in a P TTP instance. At the same P time, observe that no solution for the TTP has a distance longer than i∈T j∈T \{i} (di,j + dj,i ) = 2∆ (i.e., each team visits every other team during a road trip of length 1). Combining this with Proposition 10, we obtain the following result. Corollary 1 (Miyashiro et al. (2012)). Any algorithm for the TTP(k) is a k-approximation algorithm. Theoretical work on the TTP has mainly focused on improving this bound. Since a clear overview of the best known bounds for the different variants of the TTP is currently missing in the literature, we provide it here. For an overview of the approximation ratios, see Tables 3 and 4. 5.1. TTP(2) From an approximation point of view, TTP(2) is by far the most studied variant. Thielen & Westphal (2012) provide an algorithm with approximation ratio 1.5 + O(1/n), which is the first algorithm to achieve a ratio better than the trivial ratio of 2 from Corollary 1. Assuming n/2 is even, they provide an improved algorithm with ratio 1+16/n. This ratio has later been improved to about 1 + 4/n by Xiao & Kou (2016); when n ⩽ 32, a slightly better ratio is provided by Chatterjee & Roy (2021). For the case when n/2 is odd, Imahori (2021) introduce the first 1 + O(1/n) algorithm, achieving a ratio of 1 + 24/n. Current best results are by Zhao & Xiao (2025e), who attain an approximation ratio of less than 1 + 3/n and 1 + 5/n for instances where n/2 is even and odd, respectively. Kanaya & Takazawa (2025) provide a 1 + 9/n approximation algorithm, which is slightly worse than the best known one, yet it runs in O(n3 ) rather than O(n4 ) as required by Zhao & Xiao (2025e). 12

5.2. TTP(3) While TTP(3) poses APX-hardness, indicating the impossibility of achieving a 1 + O(1/n) approximation ratio (unless P = N P), Fujiwara et al. (2007) demonstrate the existence of such an algorithm when restricting the problem to constant distances (i.e., CD-TTP(3)). Their algorithm is referred to as the modified circle method. We note that Fujiwara et al. (2007) also provide a second algorithm for CD-TTP(3), yielding optimal solutions when n is a multiple of 6 minus 2 and n ⩽ 50. However, this heuristic assumes the availability of a break minimum 1RR with no breaks on some pre-defined time slots (generated with IP), rendering it non-polynomial. By randomly permuting team names and employing derandomization techniques, Miyashiro et al. (2012) transform the modified circle method into an approximation algorithm with a ratio of 2 + O(1/n) for the more general TTP(3). Similarly, permuting teams based on a solution to the associated TSP instance, Yamaguchi et al. (2011) achieve a ratio of 1.667 + O(1/n). Zhao et al. (2025) utilize a 3-cycle packing to improve the ratio to 1.598 + ϵ, for any ϵ > 0. 5.3. TTP(k > 3) The algorithm from the previous section by Yamaguchi et al. (2011) extends to any value of k: for k > 5, the approximation ratio is (5k − 7)/(2k) + O(k/n), improving to (2k − 1)/k + O(k/n) when k ≤ 5. In fact, the schedules provided by Yamaguchi et al. (2011) also satisfy the mirroring constraint, implying that these approximation ratios are also valid for the m-TTP(k). The first constant-factor approximation algorithm for TTP(k), independent of both n and k, is presented by Westphal & Noparlik (2014), claiming a bound of 5.875. However, Zhao & Xiao (2025a) point out that the algorithm by Westphal & Noparlik (2014) may violate the at-most constraint and identify flaws in the analysis of the approximation ratio, suggesting the correct ratio is 6.667 rather than 5.875. By rectifying these errors and refining certain lower bounds, Zhao & Xiao (2025a) achieve a constant approximation ratio of 5, which further improves to 4 when k ⩾ n/2. Imahori et al. (2014) achieve a ratio of 2.75 when k = n − 1 (i.e., the UTTP). 5.4. Other special variants Regarding the linear-distance TTP, Hoshino & Kawarabayashi (2012) provide an expander construction method, transforming a 1RR with n teams into a 2RR with 3n − 2 teams, achieving a ratio of 1.333. For multiples of 6, Zhao et al. (2022) improve the ratio to 1.2 + ϵ, for any ϵ > 0. Zhao & Xiao (2023) present an EPTAS for LD-TTP(k) with k ⩾ 3, theoretically providing solutions arbitrarily close to the optimum. Hoshino & Kawarabayashi (2012) extend their approximation algorithm to a heuristic for TTP(3) by mapping teams on a straight line and solving the associated LD-TTP(3) instance. Rasmussen & Trick (2009) propose a similar approach, mapping teams circularly and reusing the best-known solution of the associated CD-TTP(3) instance. However, no approximation ratios are provided. Finally, Hoshino & Kawarabayashi (2013) provide a 2 + O(1/n) approximation algorithm for B-TTP(3) when n is a multiple of 3, which can be slightly improved further for special distance metrics like the Euclidean one. Zhao & Xiao (2025c) further improve this ratio to 1.5 + ϵ, for any ϵ > 0 and any n. Approximation results for a generalization of B-TTP(3) to the three-partite case can be found in Zhao et al. (2026).

13

Table 3: Approximation ratios for the regular TTP Publications

TTP(2)

Thielen & Westphal (2012)

1.5 + 6/(n − 4)a 1.5 + 5/(n − 1)b 1 + 16/n b,c

TTP(3)

Xiao & Kou (2016) Imahori (2021) Chatterjee & Roy (2021) Zhao & Xiao (2025e)

1 + 2/(n − 2) + 2/nb 1 + 24/na 1 + (⌈log2 n/4⌉ + 4)/(2(n − 2))b 1 + 5/n − 10/(n(n − 2))a 1 + 3/n − 10/(n(n − 2))b 2 + 2.25/(n − 1) 1.667 + O(1/n) 1.598 + ϵ

Miyashiro et al. (2012) Yamaguchi et al. (2011) Zhao et al. (2025) Zhao & Xiao (2025d)

Westphal & Noparlik (2014) Zhao & Xiao (2025a)

1.7 + ϵ 1.625 + ϵ

e

k ≥ 6, also valid for m-TTP(k). Zhao et al. (2025) show how to improve the ratio slightly further. f k ≥ 4 and n ≥ 6. Zhao & Xiao (2025a) claim the correct ratio is 6.667. g k ≥ n/2.

n/2 is odd.

b n/2 is even. c d

TTP(k)

(2k − 1)/k + O(k/n)d (5k − 7)/2k + O(k/n)e 5.875f 5.0 4.0g

Yamaguchi et al. (2011)

a

TTP(4)

n ≥ 12. k ≤ 5, also valid for m-TTP(k).

Table 4: Approximation ratios for special variants of the TTP Publications Fujiwara et al. (2007)

CD-TTP(3)

LD-TTP(3)

1/3(n−1) a 1+ 4/3n2 −n 1/3n−1/3 1+ 4/3n2 −5/6n−1 5/6n−5/3 c 1+ 4/3n2 −2/3n

UTTP

b

1.333d 1.2 + ϵe EPTASf

Hoshino & Kawarabayashi (2012) Zhao et al. (2022) Zhao & Xiao (2023) Hoshino & Kawarabayashi (2013) Zhao & Xiao (2025c) Imahori et al. (2014)

B-TTP(3)

2 + O(1/n)a 1.5 + ϵ 2.75

a

d n ≡ 4 (mod 6). e

n ≡ 0 (mod 3). b n ≡ 1 (mod 3). c n ≡ 2 (mod 3).

f

n ≡ 0 (mod 6). valid for any k ≥ 3

6. Optimization Algorithms Dozens of algorithms have been proposed to solve TTP instances either optimally or heuristically. Since there are far too many algorithms to enumerate them all, this section only focuses on a selection of them. 6.1. Exact Methods The first (unsuccessful) attempt reported in the literature to solve the NL8 instance with a more sophisticated method than basic IP or CP models is by Benoist et al. (2001), who introduce a hybrid algorithm combining Lagrangian relaxation with constraint programming. Shortly after, Easton et al. (2003) succeed in solving NL8 using a branch-and-price method, requiring approximately four days of computation time on 20 processors. They use CP to generate columns representing the venues at which each team plays in each round. Later, Irnich (2010) reformulate the pricing problem as a shortest path problem over an expanded network, significantly accelerating the algorithm and improving several best lower bounds at that time. Building upon this, Uthus et al. (2009) utilize some symmetry reductions proposed by Irnich (2010) along with depth-first branch-and-bound 14

(DFS*) to solve NL8 using only 4 processors and 100 seconds of computation time. In a follow-up work, Uthus et al. (2012) propose an iterative-deepening algorithm (A*), achieving optimality for problem instances with up to 10 teams for the first time. However, attempts to solve larger instances encounter memory issues. A polyhedral study for an IP formulation for the UTTP together with a new class of valid inequalities is given in Siemann & Walter (2022). Regarding the time-relaxed TTP, Brandão & Pedroso (2014) propose an exact approach based on combinatorial branch-and-bound combined with dynamic programming to efficiently compute the ILB. A related idea for the regular TTP is introduced by Frohner et al. (2023), who propose a beam search heuristic that explores the most promising nodes at each level of the search tree, guided by either the ILB or a heuristic approximation thereof. This approach results in several of the currently best known solutions. For over a decade, apart from the constant distance instances, there has been no advancement in optimally solving instances with more than 10 teams. The current best upper bound for NL12 is 110,729, with the best lower bound being 108,629, leaving a gap of approximately 2%. Consequently, we propose the following open problem, whose solution would constitute a significant milestone in the study of the TTP. Open Problem 4. Determine a proven optimal solution for the NL12 instance. 6.2. Heuristic Methods The success of the TTP may at least be partially explained by the fact that it provided one of the first optimization problems in sports timetabling that was both challenging and sufficiently simple for the application of metaheuristics, at a time when these methods were still gaining popularity. Indeed, before the introduction of the TTP, metaheuristics for sports scheduling were almost nonexisting and neighborhood structures for altering round-robin timetables were largely unexplored. This is reflected in the early heuristics applied to this problem, which often avoided the need for neighborhood structures by combining IP or CP solvers as subroutines within a heuristic framework for achieving large moves in the search space. For instance, Henz (2004) suggests a fix-and-optimize heuristic based on CP, where different submodels are solved that focus on the optimization for only a subset of teams or time slots, while fixing the part of the timetable that is not optimized for. Alternatively, they fix the home-away statuses for the teams while optimizing the opponents in each round, or vice versa. Another example is Crauwels & Van Oudheusden (2003) and Adriaen et al. (2003), who use Ant Colony Optimization (ACO) based techniques, in which n ants traverse a network to construct each team’s schedule, backtracking whenever infeasibilities occur. As such, rather than relying on dedicated neighborhoods, problem-specific information is encoded in the network structure. While the initial performance of these early ACO heuristics was somewhat disappointing, at least when viewed retrospectively compared to current state-of-the-art methods, Uthus et al. (2009) later show how the performance of this heuristic can be drastically improved by incorporating more sophisticated techniques for handling the problem constraints. A major breakthrough comes with the introduction of two novel neighborhoods that preserve the round-robin structure, proposed by Anagnostopoulos et al. (2006) using Simulated Annealing (SA) and Ribeiro & Urrutia (2007) using GRASP and iterated local search. The first neighborhood, PartialRoundSwap (PRS) exchanges a subset of the games between two rounds. The second, PartialTeamSwap (PTS) swaps the opponents of two teams in a given round. Both use a deterministic ejection or repair chain to restore feasibility (see Ribeiro et al. (2025) for details). Several follow-up works have emerged from these two pioneering papers. For instance, Van Hentenryck & Vergados 15

(2006) adapt the SA algorithm to solve the mirrored TTP, Lim et al. (2006) divide the search space into a timetable and a team assignment phase, and Van Hentenryck & Vergados (2007) propose a massively parallelized version of the SA algorithm. Di Gaspero & Schaerf (2007) incorporate the neighborhoods into a tabu search framework, while Goerigk & Westphal (2016) combine tabu search with integer-programming–based neighborhoods. Neighborhoods dedicated to RTTP are proposed in Montero & Riff (2015). Many of today’s best-known solutions stem from these approaches. In the very beginning, little was known regarding PRS and PTS and often only restricted variants of the moves were used. For instance, Ribeiro & Urrutia (2007) only apply PTS moves involving 4 games, however, as shown by Di Gaspero & Schaerf (2007) PTS is equivalent to PRS in this case. Costa et al. (2012) later observe experimentally that under some circumstances none of the moves above are able to escape a given solution, and thus that the search space is disconnected (disproving a conjecture by Di Gaspero & Schaerf (2007)). These results are later formalized and proved for a wider family of timetables in Januario & Urrutia (2015) and Januario et al. (2016a). A paper by Langford (2010), which to our surprise is majorly overlooked in the literature, shows how PTS in the context of 2RR tournaments can be improved through a careful selection of the SwapHomes neighborhood swapping the assignment of rounds to games (i, j) and (j, i). This considerably reduces the number of opponents involved in the repair chain. Moreover, while PRS is commonly attributed to Anagnostopoulos et al. (2006) and Ribeiro & Urrutia (2007), we note that it is in fact proposed more than ten years earlier by Russell & Leung (1994) who apply it to a sports scheduling problem that can be considered a variant of TTP(2). Ever since the introduction of PRS and PTS, only one new neighborhood has been proposed for time-constrained round-robin scheduling, known as TARS and its generalized variant GPTS (see Januario et al. (2016b) and Ribeiro et al. (2025)). These neighborhoods have resulted in several new best-found solutions for the TTP-PV, but have not been applied yet to the classic TTP(3). Even with the inclusion of GPTS to the neighborhood structure, it is unknown whether the search space of round-robin tournament scheduling is connected (see Ribeiro et al. (2025)). This leads to the following open question. Open Problem 5. Does there exist a polynomial-time neighborhood that fully connects the roundrobin timetable search space, while preserving the 2RR structure among consecutive moves? To achieve the next major breakthrough in metaheuristic development for the TTP, we believe it would be beneficial to come up with new neighborhoods that explicitly take into account the travel cost or ensure feasibility of the no-repeater and at-most constraints (see also Cáceres & Riff (2012) and Loyen et al. (2025)). Open Problem 6. Do there exist polynomial-time neighborhoods that explicitly optimize for travel distance and/or are guaranteed to respect the no-repeater and/or the at-most constraint? We believe that a good candidate for Open Problem 6 is a neighborhood that focuses solely on the home-away assignment of the teams. A first attempt in this direction has been made by Cáceres & Riff (2012) who favor SwapHomes moves that result in longer yet still valid road trips. As for the mirrored version of the problem, we believe the neighborhoods proposed in Knust & von Thaden (2006) to modify home-away patterns in single round-robin tournaments are a good candidate. On the negative side, Loyen et al. (2025) claim that connected neighborhoods that operate in the feasible space only, may very well not exist. They argue that valid TTP solutions are almost maximally different from each other and thus that moving from one solution to another 16

implies that almost all games have to be rescheduled. We note, though, that their observations are based on a relatively small sample of timetables and that random valid solutions are almost maximally different on average. While this indeed suggests it is unlikely to be able to move from one feasible solution to any other in just a single (or a few) moves, it does not rule out the possibility for longer chains of moves via interconnecting solutions. For connectivity, analyzing the number of differences to its closest neighbor could therefore be of interest. Nakahatta et al. (2026) observe that the successful application of population-based algorithms to the TTP remains largely unexplored. They partially attribute this to the lack of a construction algorithm capable of generating many diverse and feasible starting solutions, ideally sampling the entire feasible solution space without bias. The absence of such an approach is somewhat surprising, given the existence of an algorithm that results in any possible (single) round-robin tournament (see Costa et al. (2012)) and the myriad of approximation algorithms that also provide initial feasible solutions. Moreover, Costa et al. (2012) highlights the importance of starting from solutions that differ from the canonical construction, which remains the most commonly used starting solution to date. This brings us to the following open problem. Open Problem 7. Does there exist an algorithm for uniformly sampling feasible solutions to TTP(3) at random? 7. Conclusion and future research directions Over the past 25 years, the Traveling Tournament Problem has established itself as one of the central benchmark problems in sports scheduling. Its relatively simple formulation has made it an attractive testbed for a wide range of optimization techniques, while its computational complexity continues to motivate methodological advances. As this survey has shown, substantial progress has been made both theoretically and computationally. Theoretical advances are reflected in computational complexity results and approximation guarantees, while computational progress has been driven by the development of exact and heuristic algorithms that have produced increasingly high-quality solutions for many benchmark instances. Nevertheless, besides the 7 open problems mentioned in this paper, several promising research directions remain. First, there is a need for new benchmark instances and a more standardized framework for computational evaluation. For many values of the number of teams, only a limited set of less than 10 benchmark instances is available, with most of them having a simple topological structure. Moreover, problem instances of different sizes are very similar to each other as smaller instances are contained within larger ones. All of this restricts opportunities for parameter tuning, algorithm comparison, and robustness analysis. Expanding the benchmark library and establishing more consistent standards for reporting computational performance (e.g., resources used) would facilitate fairer and more reproducible comparisons between solution approaches. Second, the relationship between the Traveling Tournament Problem (TTP) and the Traveling Umpire Problem (TUP) deserves further investigation. We believe that a meaningful trade-off may exist between the travel distances of teams and umpires, where a modest increase in the TTP objective could yield a substantial reduction in umpire travel. To the best of our knowledge, only Bender & Westphal (2016) consider this integrated setting, and the trade-off between these competing objectives remains largely unexplored. Finally, while the TTP is intentionally a simplified abstraction of real-world scheduling, this simplicity is arguably one of its greatest strengths, as it has enabled the development of a rich body 17

of algorithmic research. Rather than replacing the TTP with increasingly complex variants, we advocate investigating how the insights and techniques developed for the TTP can be transferred to practical scheduling applications. Despite 25 years of research, only a single documented realworld application is known to us (Durán et al., 2019). Bridging the gap between theoretical advances and practical deployment therefore represents an important opportunity for future work. We hope that this survey provides both a comprehensive overview of the existing literature and a useful starting point for researchers entering the field. We also encourage researchers to share and validate their results on the RobinX website3 (see Van Bulck et al. (2020)), with which we continue to track the best-known solutions and bounds. Given the continued methodological developments in combinatorial optimization and the growing availability of computational resources, the Traveling Tournament Problem is likely to remain an important benchmark and source of challenging research problems for years to come. Acknowledgements Fan Yang is supported by the Young Scientists Fund of the National Natural Science Foundation of China (grant number 72301177) and the Shanghai Pujiang Program (grant number 22PJC091). David Van Bulck is supported by the Research Foundation Flanders (FWO) [23AXE35N].

References Adriaen, M., Custers, N., & Vanden Berghe, G. (2003). An agent based metaheuristic for the traveling tournament problem. In Workshop on real-life applications of Metaheuristics, Antwerpen. Anagnostopoulos, A., Michel, L., Van Hentenryck, P., & Vergados, Y. (2006). A simulated annealing approach to the traveling tournament problem. J. Sched., 9 , 177–193. Ball, B. C., & Webster, D. B. (1977). Optimal scheduling for even-numbered team athletic conferences. AIIE Transactions, 9 , 161–169. Bao, R., & Trick, M. (2010). The relaxed traveling tournament problem. In B. McCollum, E. Burke, & G. White (Eds.), Proc. 8th Int. Conf. Pract. Theory Autom. Timetabling (pp. 472–476). Belfast: PATAT. Bendayan, S., Cheriyan, J., & Cheung, K. K. (2023). Unconstrained traveling tournament problem is APX-complete. Operations Research Letters, 51 , 456–460. Bender, M., & Westphal, S. (2016). A combined approximation for the traveling tournament problem and the traveling umpire problem. Journal of Quantitative Analysis in Sports, 12 , 139–149. Benoist, T., Laburthe, F., & Rottembourg, B. (2001). Lagrange relaxation and constraint programming collaborative schemes for travelling tournament problems. In Proc. CPAIOR (pp. 15–26). volume 1. Bhattacharyya, R. (2009). A note on complexity of traveling tournament problem. Technical Report Optimization Online. Bhattacharyya, R. (2016). Complexity of the unconstrained traveling tournament problem. Oper. Res. Lett., 44 , 649 – 654. Brandão, F., & Pedroso, J. P. (2014). A complete search method for the relaxed traveling tournament problem. EURO Journal on Computational Optimization, 2 , 77–86. Cáceres, L. P., & Riff, M. C. (2012). AISTTP: An artificial immune algorithm to solve traveling tournament problems. Int. J. Comput. Intell. Appl., 11 . 3

www.robinxval.ugent.be/RobinX/

18

Campbell, R., & Chen, D. (1976). Management science in sports. Chapter: A minimum distance basketball scheduling problem. (pp. 15–25). North-Holland. Chatterjee, D. (2021). Complexity of traveling tournament problem with trip length more than three. arXiv preprint arXiv:2110.02300 , . Chatterjee, D., & Roy, B. K. (2021). An improved scheduling algorithm for traveling tournament problem with maximum trip length two. In M. Müller-Hannemann, & F. Perea (Eds.), 21st Symposium on Algorithmic Approaches for Transportation Modelling, Optimization, and Systems (ATMOS 2021) (pp. 16:1–16:15). Schloss Dagstuhl – Leibniz-Zentrum für Informatik volume 96 of Open Access Series in Informatics (OASIcs). doi:10.4230/OASIcs.ATMOS.2021.16. Cheung, K. (2009). A Benders approach for computing lower bounds for the mirrored traveling tournament problem. Discrete Optim., 6 , 189 – 196. Costa, F. N., Urrutia, S., & Ribeiro, C. C. (2012). An ILS heuristic for the traveling tournament problem with predefined venues. Ann. Oper. Res., 194 , 137–150. Crauwels, H., & Van Oudheusden, D. (2003). Ant colony optimization and local improvement. In Workshop of Real-Life Applications of Metaheuristics, Antwerp, Belgium. Devriesere, K., Van Bulck, D., & Goossens, D. (2026). The incomplete traveling tournament problem. Di Gaspero, L., & Schaerf, A. (2007). A composite-neighborhood tabu search approach to the traveling tournament problem. J. Heuristics, 13 , 189–207. Durán, G., Durán, S., Marenco, J., Mascialino, F., & Rey, P. A. (2019). Scheduling Argentina’s professional basketball leagues: A variation on the travelling tournament problem. Eur. J. Oper. Res., 275 , 1126 – 1138. Easton, K. (2003). Using integer programming and constraint programming to solve sports scheduling problems. Ph.D. thesis Georgia Institute of Technology USA. Easton, K., Nemhauser, G., & Trick, M. (2001). The traveling tournament problem description and benchmarks. In T. Walsh (Ed.), Principles and Practice of Constraint Programming — CP 2001 (pp. 580–584). Berlin, Heidelberg: Springer. Easton, K., Nemhauser, G., Trick, M., Easton, K., Nemhauser, G., & Trick, M. (2003). Solving the travelling tournament problem: A combined integer programming and constraint programming approach. In E. Burke, & P. De Causmaecker (Eds.), Pract. Theory Autom. Timetabling IV: 4th International Conference, PATAT 2002, Gent, Belgium, August 21-23, 2002. Selected Revised Papers (pp. 100–109). Berlin, Heidelberg: Springer. Frohner, N., Neumann, B., Pace, G., & Raidl, G. R. (2023). Approaching the Traveling Tournament Problem with Randomized Beam Search. Evolutionary Computation, 31 , 233–257. Fujiwara, N., Imahori, S., Matsui, T., & Miyashiro, R. (2007). Constructive algorithms for the constant distance traveling tournament problem. In E. K. Burke, & H. Rudová (Eds.), Practice and Theory of Automated Timetabling VI (pp. 135–146). Berlin, Heidelberg: Springer. Goerigk, M., & Westphal, S. (2016). A combined local search and integer programming approach to the traveling tournament problem. Ann. Oper. Res., 239 , 343–354. Henz, M. (2004). Playing with constraint programming and large neighborhood search for traveling tournaments. In E. K. Burke, & M. Trick (Eds.), Proc. PATAT (pp. 23–32). volume 2004. Hoshino, R., & Kawarabayashi, K. (2011a). A multi-round generalization of the traveling tournament problem and its application to Japanese baseball. Eur. J. Oper. Res., 215 , 481 – 497. Hoshino, R., & Kawarabayashi, K. (2011b). Scheduling bipartite tournaments to minimize total travel distance. J. Artif. Intell. Res., 42 , 91–124. Hoshino, R., & Kawarabayashi, K. (2012). Generating approximate solutions to the traveling tournament problem using a linear distance relaxation. J. Artif. Intell. Res., 45 , 257–286. Hoshino, R., & Kawarabayashi, K. (2013). An approximation algorithm for the bipartite traveling tournament problem. Math. Oper. Res., 38 , 720–728.

19

Imahori, S. (2021). A 1+ o (1/n) approximation algorithm for TTP(2). arXiv preprint arXiv:2108.08444 , . Imahori, S., Matsui, T., & Miyashiro, R. (2014). A 2.75-approximation algorithm for the unconstrained traveling tournament problem. Ann. Oper. Res., 218 , 237–247. Irnich, S. (2010). A new branch-and-price algorithm for the traveling tournament problem. Eur. J. Oper. Res., 204 , 218 – 228. Januario, S., Urrutia, S., & de Werra, D. (2016a). Sports scheduling search space connectivity: A riffle shuffle driven approach. Discrete Appl. Math., 211 , 113 – 120. Januario, T., & Urrutia, S. (2015). An analytical study in connectivity of neighborhoods for single round robin tournaments. Operations research and computing: algorithms and software for analytics, 1st ed. Richmond, VI: INFORMS , . Januario, T., Urrutia, S., Celso, C. R., & de Werra, D. (2016b). Edge coloring: A natural model for sports scheduling. Eur. J. Oper. Res., 254 , 1 – 8. Kanaya, Y., & Takazawa, K. (2025). A faster deterministic approximation algorithm for TTP-2. Journal of the Operations Research Society of Japan, 68 , 99–123. Knust, S., & von Thaden, M. (2006). Balanced home–away assignments. Discrete Optim., 3 , 354–365. Langford, G. (2010). An improved neighbourhood for the traveling tournament problem. URL: https: //arxiv.org/abs/1007.0501. Lim, A., Rodrigues, B., & Zhang, X. (2006). A simulated annealing and hill-climbing algorithm for the traveling tournament problem. Eur. J. Oper. Res., 174 , 1459 – 1478. Loyen, B., Duncan, B., Richoux, F., & van den Berg, D. (2025). The traveling tournament problem: Valid solutions are different across instance sizes. In International Joint Conference on Computational Intelligence (pp. 491–503). Springer. Melo, R. A., Urrutia, S., & Ribeiro, C. C. (2009). The traveling tournament problem with predefined venues. J. Sched., 12 , 607. Miyashiro, R., Matsui, T., & Imahori, S. (2012). An approximation algorithm for the traveling tournament problem. Ann. Oper. Res., 194 , 317–324. Montero, E., & Riff, M.-C. (2015). RAISTTP revisited to solve relaxed travel tournament problem. In Proc. of the 2015 Annual Conference on Genetic and Evolutionary Computation GECCO ’15 (pp. 121–128). New York, NY, USA: ACM. Nakahatta, G., Richoux, F., van den Berg, D., & Aranha, C. (2026). A constructive method to build many valid initial solutions for the traveling tournament problem. In evoapplications. Osicka, O., & Guajardo, M. (2023). Fair travel distances in tournament schedules: A cooperative game theory approach. Sports Economics Review , 2 , 100011. Rasmussen, R. V., & Trick, M. A. (2007). A Benders approach for the constrained minimum break problem. Eur. J. Oper. Res., 177 , 198 – 213. Rasmussen, R. V., & Trick, M. A. (2008). Round robin scheduling–a survey. Eur. J. Oper. Res., 188 , 617–636. Rasmussen, R. V., & Trick, M. A. (2009). The timetable constrained distance minimization problem. Ann. Oper. Res., 171 , 45–59. Ribeiro, C. C., & Urrutia, S. (2007). Heuristics for the mirrored traveling tournament problem. Eur. J. Oper. Res., 179 , 775–787. Ribeiro, C. C., Urrutia, S., & de Werra, D. (2025). Metaheuristics for problems in sports scheduling. In R. Martí, P. M. Pardalos, & M. G. Resende (Eds.), Handbook of Heuristics (pp. 1493–1522). Cham: Springer Nature Switzerland. doi:10.1007/978-3-032-00385-0_62. Russell, R. A., & Leung, J. M. Y. (1994). Devising a cost effective schedule for a baseball league. Oper. Res., 42 , 614–625. Siemann, M. R., & Walter, M. (2022). A polyhedral study for the cubic formulation of the unconstrained traveling tournament problem. Discrete Optim., 46 , 100741.

20

Thielen, C., & Westphal, S. (2011). Complexity of the traveling tournament problem. Theor. Comput. Sci., 412 , 345 – 351. Thielen, C., & Westphal, S. (2012). Approximation algorithms for TTP(2). Mathematical Methods of Operations Research, 76 , 1–20. Trick, M. A., Yildiz, H., & Yunes, T. (2012). Scheduling major league baseball umpires and the traveling umpire problem. Interfaces, 42 , 232–244. Urrutia, S., & Ribeiro, C. C. (2006). Maximizing breaks and bounding solutions to the mirrored traveling tournament problem. Discrete Appl. Math., 154 , 1932–1938. Urrutia, S., Ribeiro, C. C., & Melo, R. A. (2007). A new lower bound to the traveling tournament problem. In Computational Intelligence in Scheduling, 2007. SCIS’07. IEEE Symposium on (pp. 15–18). IEEE. Uthus, D. C., Riddle, P. J., & Guesgen, H. W. (2009). DFS* and the traveling tournament problem. In W.-J. van Hoeve, & J. N. Hooker (Eds.), Integration of AI and OR Techniques in Constraint Programming for Combinatorial Optimization Problems (pp. 279–293). Berlin, Heidelberg: Springer. Uthus, D. C., Riddle, P. J., & Guesgen, H. W. (2012). Solving the traveling tournament problem with iterative-deepening A*. J. Sched., 15 , 601–614. Van Bulck, D., & Goossens, D. (2023). A traditional Benders’ approach to sports timetabling. Eur. J. Oper. Res., 307 , 813–826. Van Bulck, D., Goossens, D., Schönberger, J., & Guajardo, M. (2020). RobinX: A three-field classification and unified data format for round-robin sports timetabling. Eur. J. Oper. Res., 280 , 568 – 580. Van Hentenryck, P., & Vergados, Y. (2006). Traveling tournament scheduling: A systematic evaluation of simulated annealling. In J. C. Beck, & B. M. Smith (Eds.), Integration of AI and OR Techniques in Constraint Programming for Combinatorial Optimization Problems (pp. 228–243). Berlin, Heidelberg: Springer. Van Hentenryck, P., & Vergados, Y. (2007). Population-based simulated annealing for traveling tournaments. In oc. of the 22nd National Conf. on Artificial Intelligence (p. 267). AAAIPress volume 22. de Werra, D. (1981). Scheduling in sports. In P. Hansen (Ed.), Studies on graphs and discrete programming (pp. 381–395). Amsterdam: North-Holland. Westphal, S., & Noparlik, K. (2014). A 5.875-approximation for the traveling tournament problem. Ann. Oper. Res., 218 , 347–360. Xiao, M., & Kou, S. (2016). An Improved Approximation Algorithm for the Traveling Tournament Problem with Maximum Trip Length Two. In P. Faliszewski, A. Muscholl, & R. Niedermeier (Eds.), 41st International Symposium on Mathematical Foundations of Computer Science (MFCS 2016) (pp. 89:1– 89:14). Dagstuhl, Germany: Schloss Dagstuhl–Leibniz-Zentrum fuer Informatik volume 58 of Leibniz International Proc. in Informatics (LIPIcs). Yamaguchi, D., Imahori, S., Miyashiro, R., & Matsui, T. (2011). An improved approximation algorithm for the traveling tournament problem. Algorithmica, 61 , 1077. Zhao, J., & Xiao, M. (2023). The linear distance traveling tournament problem allows an EPTAS. Proceedings of the AAAI Conference on Artificial Intelligence, 37 , 12155–12162. Zhao, J., & Xiao, M. (2025a). A 5-approximation algorithm for the traveling tournament problem. Annals of Operations Research, 346 , 2287–2305. Zhao, J., & Xiao, M. (2025b). The APX-hardness of the traveling tournament problem. Operations Research Letters, 62 , 107311. Zhao, J., & Xiao, M. (2025c). An improved algorithm for a bipartite traveling tournament in interleague sports scheduling. Mathematics of Operations Research, (p. In press). Zhao, J., & Xiao, M. (2025d). A matching-based approximation algorithm for the traveling tournament problem. Theoretical Computer Science, (p. 115485). Zhao, J., & Xiao, M. (2025e). Practical algorithms with guaranteed approximation ratio for traveling tournament problem with maximum tour length 2. Mathematics of Operations Research, 50 , 910–934.

21

Zhao, J., Xiao, M., & Kawarabayashi, K. (2026). A TSP-based algorithm for multi-league traveling tournament. Proceedings of the AAAI Conference on Artificial Intelligence, 40 , 36547–36555. doi:10.1609/aaai.v40i43.40977. Zhao, J., Xiao, M., & Xu, C. (2022). Improved approximation algorithms for the traveling tournament problem. In 47th International Symposium on Mathematical Foundations of Computer Science (MFCS 2022). Schloss Dagstuhl-Leibniz-Zentrum für Informatik. Zhao, J., Xiao, M., & Xu, C. (2025). The traveling tournament problem: Improved algorithms based on cycle packing. Theoretical Computer Science, 1056 , 115519.

22


