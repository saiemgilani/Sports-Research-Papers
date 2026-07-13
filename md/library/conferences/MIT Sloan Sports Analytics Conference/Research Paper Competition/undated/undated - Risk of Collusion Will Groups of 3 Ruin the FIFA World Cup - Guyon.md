<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/undated/undated - Risk of Collusion Will Groups of 3 Ruin the FIFA World Cup - Guyon.pdf -->



# **Risk of Collusion: Will Groups of 3 Ruin the FIFA World Cup?** 

**Abstract** : In 2026, the FIFA World Cup will for the first time gather 48 men’s national teams. It will consist of a group stage made of 16 groups of three, with the best two teams in each group advancing to the knockout stage. Using groups of three raises several fairness issues, including the risk of match fixing and schedule imbalance. In this article we examine the risk of collusion. The two teams who play the last game in the group know exactly what results will let them advance to the knockout stage. Risk of match fixing occurs when a result qualifies both of them at the expense of the third team of the group, and can seriously tarnish the tournament. We quantify how often this is expected to happen and explain how to build the match schedule so as to minimize the risk of collusion. We also quantify how the risk of collusion depends on competitive balance. Moreover, we show that forbidding draws during the group stage (a rule considered by FIFA) does not eliminate the risk of match fixing, and that, surprisingly, the 3-2-1-0 point system does not do a better job at decreasing the risk of collusion than the 3-0 point system. Finally we describe alternate formats for a 48-team World Cup that would eliminate or strongly decrease the risk of collusion. A short version of this work has been published in The New York Times [25] and in Le Monde. The New York Times also published a follow-up article [26]. 

## **1. Introduction** 

The soccer World Cup is the most popular sporting event in the world together with the Olympic Games [52]. It is organized every four years by FIFA (Federation Internationale de Football Association), the sport's world governing body. Since 1998, 32 senior men's national teams participate in the final tournament, based on their results in the two-year qualification process--except for the host nation(s), who automatically qualify. First, the 32 teams are divided into eight groups of four; each group plays a single round-robin tournament. Then the best two teams in each group advance to the knockout stage, starting with the round of 16. 

On January 10, 2017, the FIFA council unanimously decided that starting with the 2026 edition, 48 teams will qualify to the World Cup finals. Interestingly, the press release by FIFA [19] does not motivate the decision. However, according to The New York Times [46] the decision to expand was both political and financial: ``FIFA's president, Gianni Infantino, had pressed for the change when he ran for the presidency [in 2016], as a way to invigorate the event and to include more countries. Expansion is sure to be popular in the vote-rich confederations of Africa and Asia that serve as any FIFA president's power base. And few dispute that a 48-team World Cup would be a bigger, richer tournament, producing, by FIFA's estimates, an additional USD1 billion in television, sponsorship and ticketing revenue in the first cycle alone.'' 

On the same day, FIFA decided that the final tournament will still consist of a group stage followed by a knockout stage, but that the group stage will use 16 groups of three instead of the traditional 



1 



groups of four that have been continuously used since 1950.<sup>1</sup> Like in the current format, each group will play a single round-robin tournament, and the winner and runner-up will advance to the knockout stage, which will now start with the round of 32. 

Using groups of three may look harmless, but it actually raises several fairness issues. The first obvious issue is schedule imbalance. Let us denote by A the team that will play the first two group games, B the team that will play the first and last group matches, and C the remaining team, which will play the last two group games (see Table 1). Team B will enjoy more rest days between their two group matches than Teams A and C; Team A, if they advance to the knockout round, will enjoy more rest days than the other advancing team; Team C will have none of these benefits. 

A more serious issue is the subject of this article: the risk of match fixing (or collusion). As soon as Match 2 is finished (see Table 1), Teams B and C will know what results of Match 3 will let them advance to the knockout stage. Those teams may be tempted to collude when a result lets both of them advance, at the expense of Team A. Suspicion of collusion can badly harm the tournament and the reputation of soccer in general, _whether the match is actually fixed or not_ , since outcome uncertainty is at the very root of sport's popularity. Not all teams would collude if given the opportunity, but even suspicion of coordination could damage the World Cup by casting doubt on the sincerity of the outcome. When collusion does occur, it need not be explicitly agreed upon before the match. It may simply take the form of two teams satisfied with the current score more or less late in a game and refusing or doing little to attack each other. 

The history of soccer is full of examples of such tacit coordination, including very recent ones. The ``disgrace of Gijon'' is certainly the most famous example of match fixing in the history of soccer (see, e.g., Section 3.9.1 in [28]). It refers to the match between West Germany and Austria who refused to attack each other during 80 minutes, satisfied by the 1-0 Germany win that would let both teams advance to the second round of the 1982 FIFA World Cup, at the expense of Algeria, who had played its last group game the day before. To prevent this to happen again, FIFA decided that all teams in a given group would play their last group match at the same time, which of course is not possible with groups that have an odd number of teams, in particular with groups of three. 

Even in traditional groups of four, playing the last two group games at the exact same time does not fully prevent collusion. Denmark-France (0-0 on June 26, 2018 during the 2018 FIFA World Cup) is a recent example of tacit collusion in this context: both teams knew that a draw would let them advance to the knockout stage whatever the result of the other game in the group, Australia-Peru. They did little effort to attack each other, which resulted in a boring game and the only goalless match of the 2018 World Cup. The crowd made its displeasure known, as well as football fans around the world on social media [47]. Denmark's manager Age Hareide said after the game: ``We just needed one point, we were up against one of the best teams in the world at counterattacks, so we would have been stupid to open up a lot of space. We stood back and got the result we needed, it was a 0-0 and we're very pleased with that'' [44]. 

The last 15 minutes of the 2018 World Cup match Japan-Poland provide another example of tacit collusion. Poland, already eliminated, was leading 1-0 and happy to leave the tournament on a win. When Senegal, which was playing at the same time against Colombia, conceded a goal at the 74th 

> 1 The 1982 World Cup used groups of three in the second round, where only the group winner advanced to the final knockout stage. 



2 



minute, Japan was perfectly even with Senegal in the group ranking on points, goal difference, and goals scored. The next tie-breaker was fair-play. With two yellow cards less than Senegal over the group stage, Japan would advance at the expense of Senegal. Even though Senegal could still score, Japan was happy with a 0-1 loss. Japan and Poland then suddenly stopped attacking each other, in scenes reminiscent of the disgrace of Gijon [7]. 

Peru and Colombia also colluded during the last minutes of their World Cup qualifying game (1-1) in October 2017. The current score saw both sides progress in World Cup qualifying. With results elsewhere going in their favor, Colombia knew a draw would see them finish in fourth place and qualify automatically, while Peru would advance to a play-off against New Zealand after finishing fifth. Both teams then refused to attack each other. The Independent [45] has reported that, following allegations of match fixing, Radamel Falcao, the Colombian striker and captain, admitted that he discussed playing for a draw with his opponents, as could clearly be seen on TV. 

Denmark-Sweden at UEFA Euro 2004 is another example of a tacit collusion situation [28, Section 3.9.3]: a 2-2 tie would qualify both teams at the expense of Italy, whatever the result of Italy against Bulgaria. The game indeed ended as a 2-2 draw, and even though Sweden and Denmark seemed to attack each other without restraint and try to win the game, the Italian team and fans, among others, raised complaints and suspected match fixing. 

Kendall and Lenten [28] provide other examples of tacit collusion in sports, and more generally examples where the rules of sports have led to unforeseen and/or unwanted consequences. Csato [11] also investigates an example of tacit collusion in soccer where, weirdly, two teams playing against each other are strictly better off by not winning. 

In this article, we quantify the risk of match fixing in groups of three, when two teams advance to the next phase. Section 2 describes the situations of possible collusion. In Section 3 we compute the probability of occurrence of those situations, first at the level of a group, then at the level of the tournament, which is made of 16 groups. Section 4 investigates the impact of the match schedule on the risk of collusion. In particular, we show that in order to minimize this risk, the team that plays the first two group games should be the _a priori_ strongest team in the group. In Section 5 we measure the impact of competitive balance on the risk of collusion. Section 6 and 7 quantify by how much the risk of collusion would decrease if FIFA does not use the traditional 3-1-0 point system but adopts alternate point systems that forbid draws, the 3-0 and 3-2-1-0 point systems. Finally, we discuss our results in Section 8 before suggesting alternate formats for a 48-team World Cup in Section 9 that would decrease or even eliminate the risk of collusion. Section 10 concludes. 

Note that two recent working papers by Chater et al. [9] and Truta [48] also conclude that, in order to maximize the number of competitive matches in groups of three, when two teams advance to the next phase, the _a priori_ best team should be passive in the last round. Very recently, Krumer et al. [31] argued that in the case of perfect competitive balance the team playing in the last two rounds has theoretically a higher probability of advancing, which reinforces the idea that the 2026 FIFA World Cup will violate fair-play principles. Note also that several approaches in the literature are connected to the subject of this article. For instance [1, 2, 4, 6, 16, 18, 20, 21, 22, 33, 34, 35, 39, 41, 42] assess and compare the efficacy of tournament designs, mainly via simulations. In particular, Glickman [20] assumes only partial information about competitors' relative rankings and develops 



3 



Bayesian locally-optimal design of adaptive knockout tournaments to maximize the probability that the best team advances to the next round. Glickman and Hennessy [21] have extended this approach in order to identify the overall best team in fixed knockout tournament brackets. Other utility functions are also considered. Scarf, Yusof, and Bilbao [41] propose tournament metrics that can be used to measure the success of a sporting tournament, and describe how these metrics may be evaluated for a particular tournament design. This allows them to compare competing designs, such as round robin, pure knockout and hybrids of these designs. They use the UEFA Champions League (soccer) to illustrate their methodology, while Scarf and Yusof [42] use the FIFA World Cup. Fair draws of round robin tournaments have been suggested and studied in [23, 24, 32]. Incentive incompatibility or lack of strategy-proofness, i.e., the possibility that a team is strictly better off with a weaker performance, has been investigated in [11, 14, 15, 50]. Another recent line of research is concerned with fixing a knockout tournament [5, 43, 49, 51]. 



## **2. Situations of possible collusion** 

We use the notation of Table 1. In a group of three, where the best two teams advance to the next stage, match fixing is possible when it is known after Match 2 that there exists a result of Match 3 (B vs C) which lets both Teams B and C advance at the expense of Team A. We then say that there is a _risk of match fixing_ . We assume that on paper teams have an incentive to finish first of the group. For instance, this happens when group winners play the runners-up of another group in the first round of the knockout stage, as it has been the case since the 1998 World Cup. FIFA is likely to continue to implement this rule.<sup>2</sup> We say that the risk of match fixing is _aggravated_ when Team B or C can win the group even after losing its last game. This win incentive could somewhat mitigate the risk of collusion. However, in practice, teams would rather secure qualification to the knockout round than take risks in order to win the group and perhaps lose and fail to advance (see Denmark's manager quote in the introduction). In practice, it might even happen that teams prefer to finish second in the group rather to win it, in order to end up in a preferred half of the knockout bracket. For instance, this seemed to be the case of England and Belgium during the 2018 FIFA World Cup. They were playing against each other in the last round of the group stage, and the winner could face a more difficult path to the final (Brazil in quarterfinals and France in semifinals) than the loser (England lost against Belgium and faced Sweden and Croatia instead). In the case of France-Denmark, it was not clear either whether winning the group was much of an advantage: the group winner could possibly face twice World Cup winners Argentina, while the runner-up would very likely face Croatia (all this indeed happened). 

> 2 Note that weirdly, among other oddities of the 1954 FIFA World Cup format, it had group winners playing against other group winners and runners-up playing against other runners-up in quarterfinals. 



4 



We assume that, like for the most recent World Cups, wins are worth 3 points, draws 1 point, losses 0 points, and that ties in the ranking table of the group are decided using the following ordered criteria: (1) overall goal difference, (2) overall goals scored; for the purpose of this study we only need to consider the further criterion (3): if exactly two teams are still even after Criteria 1 and 2 are applied, the winner (if any) of the match between these two teams is ranked higher. Note that the use of head-to-head results, promoted by UEFA, has no effect in groups of three. However, suspicion of collusion on the match Denmark-Sweden (UEFA Euro 2004, see introduction) was made possible only by the latter rule. 

The following proposition describes all the situations of possible collusion after Match 2. We denote by GDA the goal difference of Team A after Match 2. When A has one win and one loss, and GDA = 0, we denote by i the number of goals scored against A by the team that lost against A, and j the number of goals scored by A when it lost to the other team. For example, when A wins 1-0 against B and loses 2-1 against C, then i = 0 and j = 1. 

**Proposition 1.** Risk of match fixing occurs exactly in the following cases: 

1. Team A has one draw and one loss. 2. Team A has two draws. 3. Team A has one win and one loss and GDA ≤ 0. 

Aggravated risk of match fixing occurs if and only if Team A has one win and one loss and 

- GDA < 0, or 

- GDA = 0 and i < j. 

**Proof.** Let us review all the possible situations after Match 2: 

1. **Team A has two wins** . Then Team A has 6 points and advances to the knockout stage. No match fixing can eliminate them. 

2. **Team A has one win and one draw** . Then Team A has 4 points and advances to the knockout stage. No match fixing can eliminate them. 

3. **Team A has one win and one loss** . Then several cases must be looked at depending on the goal difference GDA of Team A: 

   - a) GDA > 0: Team A has won against, say, B with a margin of m goals, and lost to C with a margin of n goals, with GDA = m-n > 0. If B does not win against C, then it does not advance to the next round. If B wins against C, let p be the goal margin of this win. Then A, B, and C all have 3 points, B and C have goal differences p-m and n-p, one of which is strictly smaller than m-n (indeed, if p-m ≥ m-n and n-p  ≥ m-n then 2m-n ≤ p≤ 2n-m so m≤ n). The roles of B and C can of course be swapped. Eventually, no match fixing can eliminate A. 

   - b) GDA < 0: Team A has won against, say, B with a margin of m goals, and lost to C with a margin of n goals, with GDA = m-n < 0. If B wins m - 0 against C, then A, B, and C all have 3 points, B has goal difference 0, C has goal difference n-m > 0, both better than the goal difference of A, and the final group ranking is C > B > A. Therefore, by loosing m - 0 against B, C can eliminate A and still win the group. Again the roles of B and C can be swapped. Eventually, there is an _aggravated risk of match fixing_ . 



5 



   - c) GDA = 0: The situation is similar to the case GDA < 0. If B wins (m+k) - k against C with k large enough, then A, B, and C all have 3 points and goal difference 0, but B and C will finish ahead of A thanks to a larger number of goals scored. Let (m+i) - i be the score of A - B, and j - (m+j) be the score of A - C, with i,j≥ 0. If i > j, B is ahead of C due to a larger number of goals scored. If i = j, then B and C are perfectly even on points, goal difference, and goals scored, so Criterion 3 applies and in this case too the final group ranking is B > C > A. Finally, if i < j, C finishes ahead of B due to a larger number of goals scored. Again the roles of B and C can be swapped. Therefore, when GDA = 0, there is always a risk of match fixing, and this risk is aggravated if and only if the team that lost against A scored strictly less goals against A than A scored when it lost to the other team. 

4. **Team A has two draws** . Then if B and C draw k - k with k large enough, all teams will have 2 points, 0 goal difference, and B and C will eliminate A thanks to a larger number of goals scored. There is a risk of match fixing. 

5. **Team A has one draw and one loss** . Then if B and C draw they will have 2 and 4 points and will eliminate A (1 point). There is a risk of match fixing. 

6. **Team A has two losses** . Then Team A has zero point and is already eliminated. 

**Remark 2.** Note that the second case (Team A has one win and one draw) might lead to another weak form of collusion: Team A might have few incentives to win its second match after winning the first, which can be advantageous for Team C. This is especially probable if Team A is chosen to be the strongest team, which, as we will see in Section 4, will minimize the risk of collusion in the third match. 

## **3. Probability of possible collusion** 

Here we consider a simple model to estimate the probability of the situations of possible collusion. We assume that the result of Match 2 is independent of the result of Match 1. We denote by pXY the probability that Team X wins against Team Y (see Table 2) and by p<0 (resp. p0, p>0) the probability that Team A has negative (resp. null, positive) goal difference, i.e., GDA <  0 (resp. = 0, > 0), _given that Team A has one win and one loss in the group stage_ .<sup>3</sup> With obvious notations, we decompose p_0 into p0 = p0,i≥ j + p0,i<j. For simplicity, we denote by 

dXY = 1 - pXY - pYX 

the probability that Teams X and Y draw and by p≤0 = p<0 + p0. Table 3 summarizes all the possible situations of Team A after Match 2, their probabilities, and whether they lead to a risk of match fixing (RMF) and an aggravated risk of match fixing (RMF*). The following proposition gives the probability that there is a risk of match fixing for a given group of three in this model. It immediately follows from Proposition 1 and Table 3. 

3 A more complicated model could have the probabilities pXY depend on the match schedule. Note that, ignoring collusion issues, Krumer and Lechner [29] have examined the role of the schedule in round-robin tournaments with sequential games between three and four contestants empirically. Theoretical works on this topic include [30, 40]. 



6 







In the case of perfect competitive balance, 



and p≤0 > 1/2, typically close to 1/2. Then dAB = dAC = dBC = 1-2p and 



When p = 1/3, pRMF = 1/3 + 2/9*p≤0. Assuming p≤0 = 0.6, we get pRMF = 7/15. For a slightly more reasonable value p = 3/8, then pRMF = ¼ + 9/32*p≤0 = 67/160 ~ 42%. Both values are close to 50%. In the situation of perfect competitive balance, the risk of match fixing is very high. 



7 



The next two remarks, which are trivial consequences of Proposition 3, give sufficient conditions under which the risk of collusion is maximal or minimal. 

**Remark 4.** The probability that there is a risk of match fixing is maximal, equal to 1, in the case where dAB = dAC = 1. 

This remark somewhat explains why it has been reported that FIFA has considered banning draws during the group stage [17, 46, 53]. All group stage matches would have a winner and a loser, possibly decided by a penalty shootout in the case where two teams are tied after 90 minutes. The impact of banning draws will be thoroughly investigated in Sections 6 and 7. Note that forbidding draws does not eliminate the risk of collusion. For instance, the situations where Team A has one win and one loss and a nonpositive goal difference will still be prone to match fixing. 

**Remark 5.** The probability that there is a risk of match fixing is minimal, equal to 0, if one of the following conditions holds: 

- i. pAB = 1 and (pCA = 0 or p≤0 = 0): A surely wins against B, and it cannot lose against C, or if it loses against C its global goal difference GDA can only be positive. 

- ii. pAC = 1 and (pBA = 0 or p≤0 = 0): A surely wins against C, and it cannot lose against B, or if it loses against B its global goal difference GDA can only be positive. 

- iii. pBA = pCA = 1: A surely loses against B and C. 

This remark indicates that in order to minimize the risk of match fixing, Team A should be the _a priori_ strongest team in the group (so it is close to satisfy one of the first two conditions above) or the _a priori_ weakest team in the group, if very weak (so it is close to satisfy the last condition above). Team A should not be the middle team. However, conditions (i), (ii), or (iii) are never satisfied in practice: even when a soccer powerhouse meets an underdog, there is always a positive probability that the underdog draws or wins, even if it is small. This means that in practice the risk of match fixing cannot be avoided. In particular, we have: 

**Corollary 6.** Assume one of the following conditions: 

- i. All the probabilities pAB, pBA, pAC, pCA, p≤0 are strictly positive. 

- ii. The probabilities dAB and dAC are strictly positive. 

Then the risk of collusion cannot be avoided: pRMF > 0. 

Finally, the next proposition is also an immediate consequence of Proposition 3. It quantifies the probability that there will be a risk of collusion in at least one of the 16 groups. 



8 





For the numerical examples presented just after Proposition 3 we get pRMF(16) = 1-(1-7/15)^16 ~ 0.99996, or pRMF(16) = 1-(1-67/160}^16 ~ 0.99983. This shows that in the case of perfect balance, match fixing will almost surely be possible during the group stage. 

## **4. Impact of the match schedule on the risk of collusion** 

Let us consider a realistic example of a 2026 World Cup group given in Table 4, with a strong team S, a middle team M, and a weak team W. 

There are three possible choices for Team A: S, M, and W, corresponding to three possible match schedules. (The order of the first two games is irrelevant as regards the risk of collusion.) We naturally assume that the stronger Team A is, the smaller p≤0 and p<0 + p0,i<j are (see Table 5). The numerical values of the probabilities pSM, pSW, pMS, pMW, pWS, and pWM in Table 4, as well as those of the conditional probabilities p≤0 and p<0 + p0,i<j in Table 5, are made up but plausible. They mostly serve for illustration purposes, so that we can grasp the order of magnitude of the risk of collusion. Note that one cannot directly statistically estimate those probabilities from past World Cups as in 2026 many of the 16 new finalists (one per group) will likely be much weaker than recent World Cup finalists.<sup>4</sup> Another numerical example, corresponding to a more strongly imbalanced group, is investigated in Section 5 to illustrate the impact of the competitive balance on the risk of collusion. 

> 4 For this reason we disagree with the approaches based on the results of previous World Cups, such as [48]. 



9 





The corresponding values of pRMF and pRMF* are given in Table 5. For this plausible example, it is apparent that in order to minimize the risk of collusion, Team A (the team that plays the first two group games) should be the _a priori_ strongest team in the group: the risk of collusion is about 15% in any given group, if Team A is the _a priori_ strongest in the group, but it climbs to around 50% otherwise. Indeed, if Team A is the _a priori_ strongest in the group, it would likely be already qualified after Match 2 (first three lines of Table 3). However, arbitrarily deciding which team will play the first two games in a group is unfair, as it is the only team that may be the victim of collusion. 

Note that if this schedule (A = S) is implemented: 

- The _a priori_ strongest team in the group, if it is not already qualified after Match 2, might be the victim of a collusion between the two other teams. 

- The _a priori_ strongest team in the group, if it advances to the knockout stage, will enjoy more rest days than the other qualified team before the round of 32. 

- In all groups, the third match will oppose the two _a priori_ weakest teams in the group. 

The probabilities pRMF(16) (resp. pRMF*(16)) that there is a risk of match fixing (resp. an aggravated risk of match fixing) for at least one of the 16 groups, as well as the expected numbers of groups with a risk of match fixing, are also given in Table 5. Note how large pRMF(16) is, even in the most favorable case where in all groups Team A is the strongest team (more than 90%). It is almost certain that there will be a risk of collusion for at least one group. Even in this most favorable case, it is actually expected that risk of match fixing will occur in 2.3 groups. For the other schedules (A = M or W), match fixing will be possible in eight groups on average. The ``disgrace of Gijon'' will not 



10 



only be made possible again, the risk of its repetition will be very high, which is a terrible step back in the history of the World Cup. 

## **5. Impact of competitive balance on the risk of collusion}** 

Tables 6 and 7 compare three situations of competitive balance within a group: perfect balance (the three teams are equally skilled), imbalance (there is a strong team, a middle team, and a weak team), and strong imbalance (the strong team is much stronger than the weak team). Of course, only the last two cases are realistic for the World Cup, because of the seeding procedure used to build the groups [23, 24]. Note that the middle columns of Table 7 (Imbalance) coincide with Table 5. 



As can be seen from these tables, when Team A is the strongest team in the group, the stronger the imbalance, the smaller the risk of collusion. This is because A is more likely to be already qualified after Match 2. However, when Team A is the weakest team in the group, the risk of collusion is not a monotonic function of imbalance. 

Note that, even in the most favorable case where all groups are highly imbalanced and in all groups Team A is the strongest team, the risk of a collusion in at least one of the 16 groups is still larger than 60%, and match fixing will be possible in 0.9 group on average. 



11 



## **6. Impact of forbidding draws on the risk of collusion: the 3-0 point system** 

As mentioned after Remark 4, FIFA has considered banning draws during the group stage in order to limit the risk of collusion. In this section we investigate how efficient this ban would be. We assume a 3-0 point system: in the case of a draw, the winner of the penalty shootout earns 3 points, while the loser gets nothing. Another point system (3-2-1-0) will be investigated in Section 7. We also assume that the result of the penalty shootout does not impact the goal difference, and that both teams have equal chances to win the penalty shootout. 

**Remark 8.** The 3-0 point system has undesirable consequences. For instance, imagine that A wins against B and loses against C, in both cases after 90 minutes (no penalty shootouts). Then, in the traditional 3-1-0 system, a draw between B and C would eliminate B (C: 4 points, A: 3, B: 1). In the 3-0 point system, this draw between B and C must be resolved as a win/loss by a penalty shootout. By winning the penalty shootout, B could eliminate A or C, which seems unfair as, unlike B, Teams A and C got proper wins after 90 minutes. Worse, depending on goal differences, Team C could have secured the first place before the penalty shootout, and then _decide_ to eliminate Team A by deliberately losing the penalty shootout at no cost (aggravated risk of match fixing on penalties, see below). 

It is tempting to apply the results of Section 3 with the new values pXY<sup>30</sup> := pXY + ½*dXY. However, this is not correct as, unlike with the 3-1-0 point system, we cannot assume that, in the case where Team A has 3 points after Match 2, the sign of the goal difference of A is an independent random variable. For instance, when Team A has one win and one draw lost on penalties (it then has 3 points, corresponding to one win and one loss in the 3-1-0 point system), its goal difference can only be positive, since the result of the penalty shootout does not impact the goal difference. 

To ease comparisons with the 3-0 point system, we still speak of a draw for a match that is tied after 90 minutes and is decided by a penalty shootout, and of a win or a loss for games whose result is decided after 90 minutes. We recall that the risk of match fixing is _aggravated_ . when Team B or C can win the group even after losing its last game. When draws are banned, we introduce another notion of aggravated risk of match fixing: we say that there is an _aggravated risk of match fixing on penalties_ when Team B or C can win the group and eliminate Team A even after drawing its last game and losing on penalties. In such a case, Teams B and C may agree (explicitly or not) on a draw, and the team leading in the rankings can at no expense _decide_ to eliminate Team A by losing the penalty shootout---a situation that would certainly be described as scandalous by Team A, its fans, and the media, and that FIFA surely wants to avoid by all means. 

The next proposition compares the 3-0 point system with the 3-1-0 point system in terms of risk of collusion. It shows that forbidding draws indeed always decreases the risk of collusion, but it actually increases the probability of an aggravated risk of collusion. 



12 







**Proof.** Let us review all the possible situations after Match 2. If Team A has 6 points, it is already qualified and no match fixing can eliminate them. If Team A has 0 points, it is already eliminated. If Team A has 3 points, one must consider the sign of the goal difference GDA: 

1. GDA > 0: It is easy to check that, like in the 3-1-0 point system, Team A is already qualified and no match fixing can eliminate them. 



13 



2. GDA < 0: The situation slightly differs from the 3-1-0 point system due to the fact that A may have won its game on penalties, with a zero goal difference. Team A has won against, say, B with a margin of m ≥ 0 goals (m = 0 corresponds to a win on penalties), and lost to C with a margin of n ≥ 1 goals, with GDA = m-n < 0 (the roles of B and C can be swapped). 

   - a) There is an aggravated risk of match fixing on penalties if and only if 2m ≤ n. Indeed, if 2m < n, by drawing with B and losing on penalties, C would eliminate A and win the group. If 2m = n, B and C would need to draw k - k with k large enough so that B has the same goal difference as A but a larger number of goals scored. If 2m > n, then if B and C draw, A has a strictly better goal difference than B so it cannot be eliminated after B and C draw. 

   - b) If m ≥ 1, there is an aggravated risk of match fixing, like in the 3-1-0 point system. 

   - c) If m = 0, A and B have drawn and A has won on penalties. In some cases there can be an aggravated risk of match fixing: 

      - If n ≥ 3, or if n = 2 and A - B was a goalless draw, then C can afford to lose 1-0 against B and still eliminate A and win the group (aggravated risk of match fixing). 

      - If n = 2 and A - B was not a goalless draw, then there is an aggravated risk of match fixing if and only if C scored at least two more goals than B in their games against A (due to Criterion 3). 

      - If n = 1 there cannot be an aggravated risk of match fixing (of the first type), since if C loses against B after 90 minutes, it will be behind B in the rankings, due to a smaller goal difference. However, there is a risk of match fixing. 

3. GDA = 0: 

   - a) If Team A won one game (say, against B) and lost the other within 90 minutes, then the situation is similar to the 3-1-0 point system: there is a risk of collusion, which is aggravated (of the first type) if and only if i < j (defined before Proposition 1). There can be no aggravated risk of collusion on penalties as if B and C draw, A will finish ahead of B even if B wins the penalty shootout, due to a better goal difference. 

   - b) If Team A drew twice and won one penalty shootout (say, against B) and lost the other (say, against C), then by drawing k - k with k large enough both B and C would advance if B wins the penalty shootout. Team C would finish ahead of B only if it scored more goals (j) than B (i) when both teams tied with A (strictly more, due to Criterion 3, extended to win on penalties). Therefore there is a risk of match fixing, and there is an aggravated risk of match fixing on penalties if and only if i < j. There can be no aggravated risk of match fixing of the first type, since if C loses against B after 90 minutes, it will be behind both A and B in the rankings, due to a smaller goal difference. 



14 





Table 8 summarizes all the possible situations of Team A after Match 2 in the 3-0 point system, their probabilities, and whether they lead to a risk of match fixing (RMF), an aggravated risk of match fixing (RMF*), and an aggravated risk of match fixing on penalties (RMF*pen). Compared with the traditional 3-1-0 point system (Table 3) two situations that always led to risk of match fixing are now split into two: 

- **Team A has two draws** . There is no more risk of match fixing if A wins both penalty shootouts---in this case A is already qualified---or if it loses both penalty shootouts---in this case A is already eliminated. This decreases the probability that there is a risk of match fixing by 1/2 dABdAC. 

- **Team A has one draw and one loss.** There is no more risk of match fixing if A loses on penalties---in this case A is already eliminated. This decreases the probability that there is a risk of match fixing by ½*(pBAdAC + dABpCA). 

This explains why the risk of match fixing is decreased with the 3-0 point system. 

However, compared to the 3-1-0 point system, one new situation leads to an aggravated risk of match fixing: 

- **Team A has one draw and one loss** . There is now an aggravated risk of match fixing if A wins the penalty shootout and we are in Case 1. 

Therefore the 3-0 point system increases the probability of an aggravated risk of collusion. Not only that, it also creates a new type of aggravated risk of match fixing (on penalties), which may lead to extremely problematic situations. FIFA certainly needs to avoid by all means this situation where a team can decide to eliminate another team _at no cost_ by deliberately loosing a penalty shootout. 

Like in the previous section, Table 9 compares the three situations of competitive balance within a group, but now in the 3-0 point system. Let us compare Tables 7 and 9. Banning draws would indeed decrease the risk of collusion, but not much: for a reasonably unbalanced group, the risk of collusion would be around 10% (down from 15%) if the strongest team plays the first two group 



15 



games and around 33% (down from 50%) otherwise. For a strongly unbalanced group, the risk of collusion would decrease to 4.5% (down from 5.9%) if the strongest team plays the first two group games, to around 22% (down from 35%) if the weakest team plays the first two group games, and to around 40% (down from 50%) if the middle team plays the first two group games. The probability that at least one group faces risk of collusion would still be very high, at about 52% (down from 62%) in the most favorable case (strong imbalance, A = S), and close to 100% in many cases. Even in the most favorable case, it is more likely that match fixing will be possible in at least one group than not. 

As shown in Proposition 9, forbidding draws actually increases the probability of aggravated risk of collusion, the most dangerous form of match fixing. In the most favorable case (strong imbalance, A = S), the probability that at least one group faces aggravated risk of collusion increases to around 29% (up from 26%). For a reasonable unbalanced group, if A = S, it increases to 50% (up from 42%). In all other cases, it is larger than 96%. 

As for the new aggravated risk of collusion (on penalties), its probability is quite similar to that of the aggravated risk of collusion (after 90 minutes), which means that the total probability of an aggravated risk of collusion (after 90 minutes and on penalties) is roughly speaking doubled compared to the 3-1-0 point system. This higher aggravated risk of collusion is the main drawback of the 3-0 point system, together with the flaw described in Remark 8. 





16 



## **7. Impact of forbidding draws on the risk of collusion: the 3-21-0 point system** 

In this section we investigate another natural point system, the 3-2-1-0 point system, in the hope that it will do a better job at decreasing the risk of collusion. We still assume that draws are forbidden but now we assume that the winner of a tied game decided by a penalty shootout wins 2 points, instead of 3 points, while the loser wins 1 point, instead of 0 points. In this case, in all group matches, 3 points are distributed to the teams: either 3+0, if there is a winner at the end of the 90 minutes of play, or 2+1 if the game is tied and is decided by a penalty shootout. This 3-2-1-0 point system was used in the 1988-89 season of the Argentinian League [37, Chapter 10]. The 1994-95 National Soccer League season in Australia has applied a modified version: 4 points for a win, 2 for a win on penalties, 1 for a penalty loss and no points for a loss in regulation time [28, Section 3.9.7].<sup>5</sup> At first sight it seems that the 3-2-1-0 point system, which is natural and plausible, would significantly reduce the risk of collusion by increasing the number of possible point scenarios after Match 2. This was in particular argued by Ignacio Palacios-Huerta in [38] after we published two articles in The New York Times [25, 26] based on a first version of this work. Let us check to what extent this is true. To ease comparisons with the other point systems, we still speak of a draw for a match that is tied after 90 minutes and is decided by a penalty shootout, and of a win or a loss for games whose result is decided after 90 minutes. 

**Remark 10.** One benefit of the 3-2-1-0 point system is that it does not have the flaw of the 3-0 point system that was described in Remark 8: if A wins against, say, B and loses against C, in both cases after 90 minutes (no penalty shootouts), then, like in the traditional 3-1-0 system, a draw between B and C would automatically eliminate B, even if B wins the penalty shootout. 

The following proposition describes the situations of possible collusion in the 3-2-1-0 point system. 

> 5 Note that the extensive use of penalty shootouts for deciding draws may lead to the emergence of other fairness issues [3, 8, 36, 37]. 



17 







**Proof.** Let us review all the possible situations after Match 2: 

1. **Team A has two wins.** Then Team A has 6 points and advances to the knockout stage. No match fixing can eliminate them. 

2. **Team A has one win and one draw.** Then Team A has either 4 or 5 points and advances to the knockout stage. No match fixing can eliminate them. 

3. **Team A has one win and one loss.** The situation is similar to the 3-1-0 point system: match fixing will be possible if and only if GD_A≤ 0, and there is aggravated risk of match fixing if and only if GD_A < 0, or GD_A = 0 and i < j (see proof of Proposition 1). There can be no aggravated risk of match fixing on penalties. 



18 



4. **Team A has two draws.** If A wins the two penalty shootouts, then it has 4 points, advances to the knockout stage, and no match fixing can eliminate them. Otherwise there is a risk of match fixing: 

   - a) If A loses the two penalty shootouts, then all three teams have 2 points after Match 2. A draw between B and C, whoever wins the penalty shootout, will eliminate A. But there is no aggravated risk of match fixing (after 90 minutes or on penalties). 

   - b) If A wins exactly one of the two penalty shootouts, then it has 3 points, while B, say, has 1 point, and C 2 points. Then if B and C draw k - k with k large enough, and B wins the penalty shootout, all teams will have 3 points, 0 goal difference, and B and C will eliminate A thanks to a larger number of goals scored. There is an aggravated risk of match fixing on penalties if and only if the team who beat A on penalties (C in our example) scored strictly more goals against A than B did (strictly, because of tiebreaker Criterion 3, extended to wins on penalties). However, there is no aggravated risk of match fixing of the first type. 

5. **Team A has one draw and one loss.** If A loses the penalty shootout, it is already eliminated. Otherwise there is a risk of match fixing: A has 2 points, while B, say, has 1 point, and C 3 points; a win of B against C eliminates A; so does a draw, if B wins the penalty shootout. In this last case, C is already guaranteed to win the group after 90 minutes and has no interest in winning the penalty shootout. They may decide to lose the penalty shootout to eliminate A. There is an aggravated risk of match fixing on penalties. There is no aggravated risk of match fixing (after 90 minutes) though, since if C loses after 90 minutes it cannot win the group. 

6. **Team A has two losses.** Then Team A has zero point and is already eliminated. 



Table 10 summarizes all the possible situations of Team A after Match 2 in the 3-2-1-0 point system, their probabilities, and whether they lead to a risk of match fixing (RMF), an aggravated risk of match fixing (RMF*), and an aggravated risk of match fixing on penalties (RMF*pen). Compared with the traditional 3-1-0 point system (Table 3) two situations that always led to risk of match fixing are now split into two: 



19 



- **Team A has two draws.** There is no more risk of match fixing if A wins both penalty shootouts---in this case A is already qualified. This decreases the probability that there is a risk of match fixing by 1/4 dABdAC. 

- **Team A has one draw and one loss.** There is no more risk of match fixing if A loses on penalties---in this case A is already eliminated. This decreases the probability that there is a risk of match fixing by ½* (pBAdAC + dABpCA). 

This makes situations of possible match fixing less likely compared with the traditional 3-1-0 point system. However, there is no change regarding aggravated risk of match fixing: it occurs in the same situations for both point systems. But the 3-2-1-0 point system introduces a new, problematic aggravated risk of match fixing (on penalties), in which a team can decide to eliminate Team A at no cost by losing the penalty shootout if the last group game ends in a draw after 90 minutes. 

Note that the probabilities of an aggravated risk of match fixing (of the first or second types) are smaller in the 3-2-1-0 point system, compared to the 3-0 point system. This seems to indicate that, if FIFA wants to ban draws to reduce the risk of collusion, it should adopt the 3-2-1-0 point system, rather than the 3-0 point system. However, surprisingly, the global risk of collusion is _higher_ in the 3-2-1-0 point system than in the 3-0 point system: pRMF<sup>3210</sup> = pRMF<sup>30</sup> + ¼*dABdAC ≥ pRMF<sup>30</sup> . Indeed, compared with the 3-0 point system (Table 8) a situation now leads to risk of match fixing: 

- **Team A has two draws.** There is now a risk of match fixing if A loses both penalty shootouts---in this case A is already eliminated in the 3-0 point system, but may still qualify in the 3-2-1-0 point system, and is subject to possible collusion. This increases the probability that there is a risk of match fixing by 1/4 dABdAC. 

The various probabilities of risk of match fixing and average number of groups with a risk of match fixing in the 3-2-1-0 system are reported in Table 11, for the numerical example of Table 6. 



20 





## **8. Discussion** 

Figure 1 compares the probability of (a) risk of match fixing for a given group; (b) aggravated risk of match fixing for a given group; (c) risk of match fixing in at least one of the 16 groups; (d) aggravated risk of match fixing in at least one of the 16 groups, in the three different point systems 3-1-0, 3-0, 3-2-1-0, for the three competitive balance assumptions of Table 6 and the three schedules A = S, M, or W. It shows that: 

- Clearly the most important factor impacting the risk of match fixing is the schedule: the risk of match fixing is minimized when it is the _a priori_ strongest team that plays the first two games in the group. 

- Forbidding draws and adopting the 3-0 point system decreases the risk of collusion, but increases the probability of aggravated risk of match fixing. 

- Surprisingly, compared to the 3-0 point system, the risk of match fixing is slightly larger in the 3-2-1-0 point system; but, compared to the classical 3-1-0 point system, it is slightly smaller. 

The probability of aggravated risk of match fixing in the 3-2-1-0 point system is exactly the same as in the 3-1-0 point system. However, banning draws introduces problematic situations where a team may decide to eliminate another team by deliberately losing the penalty shootout (aggravated risk of match fixing on penalties). 



21 







22 





Eventually, it seems that, among the two alternative point systems considered here, the 3-2-1-0 point system would be the most efficient to decrease the risk of collusion. Indeed, it does significantly decrease the global risk of collusion compared to the classical 3-1-0 point system (almost as much as the 3-0 point system), and, unlike the 3-0 point system, it does not increase the aggravated risk of collusion. However, like the 3-0 point system, it introduces a very problematic kind of aggravated risk of collusion (on penalties). Figure 2 shows that in the 3-2-1-0 point system the probability of an aggravated risk of match fixing on penalties is almost as large that of an aggravated risk of match fixing (after 90 minutes) in most cases. (Note that there is a substantial difference between them in the case of strong imbalance.) 

## **9. Alternate formats** 

Assuming a 48-team World Cup, what alternate formats could FIFA use which would significantly decrease, or even eradicate, the risk of collusion? We have examined a few possible formats in [25, 26], which we summarize here. All the formats listed below take into account the requirement that the tournament should not last too long; the total number of matches should not exceed, say, 100. This precludes the classical round-robin format with eight groups of six---in this format the group stage only would feature 120 games. See however Format 6. Table 12 summarizes and compares the various formats. 



23 



**Format 1: 12 groups of four.** The 12 group winners, 12 runners-up, and eight best third-place teams would advance to the round of 32. However, with 72 group matches and a total of 104 games, the World Cup would then last at least one more week, assuming four group matches per day. Both the current format (1998-2018, 64 games) and the three-team group format (80 games) can be completed in 32 days. Since the number of groups would not be a power of two, the knockout bracket would be unbalanced, in the sense that some group winners would play against thirdplaced teams in the round of 32, while other group winners would play against runners-up, and some runners-up would play against each other, like it happened during the round of 16 of the 1986, 1990, and 1994 FIFA World Cups, and during the 2016 UEFA Euro, and like it will happen during the Euro 2020. See [27] for a detailed study of such unbalanced brackets. 

**Format 2: 12 groups of four, only 16 teams advance.** The 12 group winners and four best runners-up would advance to the round of 16. This would decrease the total number of matches to 88 from 104. Only a third of the teams would advance to the knockout stage. The knockout bracket would still be unbalanced, with some group winners facing each other in the first round of the knockout stage, while others would play against runners-up. 

**Format 3: 16 groups of three, only group winners advance.** This would eliminate the risk of collusion but has several serious pitfalls. First, the last group match may be a dead rubber (when Team A has two wins). Second, there is still a fairness issue. When Team A has one win and one draw (say, against B and C, respectively), Team B is already eliminated before the last group match and may not give its best effort to defeat C. If C wins the group after beating an unmotivated Team B, Team A may feel aggrieved. Third, this example shows that in this format a team (B in this case) can be eliminated after playing just one game. Finally, the winner would play only six matches, one less than in the current format (1998--2018). On the other hand, Vong [50] argues that to prevent strategic manipulation in tournament games, it is both necessary and sufficient to allow only the top-ranked player to qualify from each group. 

**Format 4: 16 groups of three, all teams advance** . Group winners would get a bye and directly advance to the round of 32, while runners-up and third-placed teams would advance to a playoff round, whose winner would qualify for the round of 32. This format would total 96 matches, which could fit in 38 days. It would indeed eliminate the risk of collusion. All teams would play a minimum of three games. The winner of the tournament would need to play seven or eight matches. Coaches, fans, TV networks and FIFA might not like the idea of group winners getting a bye, though. Those best teams would not be seen on TV in the playoff round. Also, if the group winner is Team A, they would have at least 12 rest days between their last group match and their first knockout game, which seems too long. 

**Format 5: 16 groups of three, seed knockout bracket based on performance across groups.** We have investigated the idea of seeding the knockout stage based on performance across groups in [27] where we illustrate how it would work for 24-team UEFA Euros. Group winners and runners-up would be ranked based on group stage performance (say for instance: points, goal differential, and number of goals scored, in that order). Then the best group winner would play against the lowest-ranked runner-up, the second best group winner against the second lowestranked runner-up, and so on, for example. This would incentivize all teams to perform at their best during the group stage, even if they know that a draw or even a 0-1 loss would be enough to advance to the knockout stage, thus significantly decreasing the risk of collusion. This format raises a logistics problem though: teams and fans could not plan ahead when and where they will be 



24 



playing during the knockout stage if they advance. They would have to wait until the last match of the last group to know when, where, and against who they will play in the round of 32. The teams that play this last match may be unfairly advantaged, as they would know who their opponent in the round of 32 would be, depending on the result of this last match. Also, more soccer-free days would be needed between the group stage and the round of 32 to ensure a minimum of rest days to all the teams that advance, which would lengthen the tournament. 

**Format 6: eight groups of six, but each team plays only three teams in their group** . Each group of six is divided into two balanced subgroups of three teams. All teams in Subgroup 1 play against all teams in Subgroup 2. The best two teams over all advance to the knockout stage (they could be both from the same subgroup). To enforce balance, six pots of eight teams could be formed based on the new FIFA rankings, from Pot 1 (the eight highest-ranked teams) to Pot 6 (the eight lowestranked teams). One subgroup would contain teams from Pots 1, 4 and 5 (or 6), while the other subgroup would contain teams from Pots 2, 3 and 5 (or 6). Like in the current system, in this format each team plays three group matches; all teams can play simultaneously on Match Day 3 to decrease the risk of collusion; and bracket routes could be predetermined. By splitting groups of six into two balanced subgroups of three, the number of group matches would decrease to 72 from 120. There would be a total of 88 games, which could fit in about 35 days. 

**Format 7: 16 groups of three, followed by eight groups of 4.** The 16 groups of three are paired, e.g., Group A is paired with Group B, Group C with Group D, etc. The best two teams in each group advance to a second group stage. Teams advancing from paired groups form a group of four, and the results of the matches played during the first group stage are carried over. For example, the winner (denoted A1) and runner-up (A2) of Group A form a group of four with the winner (B1) and runner-up (B2) of Group B, and the results of the games A1--A2 and B1--B2 are carried over, so the second group stage has only four games played over two match days (for example A1--B1 and A2-B2 on Match Day 1, and A1--B2 and A2--B1 on Match Day 2. The best two teams in each group of four advance to the round of 16. Since results of the first group stage are carried over, teams have no incentive to collude. There would be 48 games during the first group stage, 32 games during the second group stage, and 16 knockout games, for a total of 96 games. The winner would play eight games, one more than in the current format and the format suggested by FIFA. Since three match days are needed for the first group stage, and two match days for the second group stage, the tournament would last at least one more week. This format has been used in handball and has been analyzed in [12, 13].<sup>6</sup> 

> 6 The number of matches could be slightly decreased if only the eight group winners of the second group stage qualify for the quarterfinals. Then there would be only eight matches in the knockout stage, and the maximal number of matches per team would be reduced to eight from nine. The format G64, which was used in the 2003 World (Wo)Men's Handball Championship, contained groups of four teams such that only the first advanced to the knockout stage [13]. 



25 





**Remark.** Note that for three-team groups, when only the group winner advances to the next phase, a classical procedure to avoid that the last group game be a dead rubber, i.e., a match with nothing at stake between two teams that are already eliminated, consists of enforcing a flexible schedule where the team that loses the first game, if any, plays the second group game. As pointed out to me by Keith Willoughby (University of Saskatchewan), this flexible schedule was used in Canadian university hockey years ago. However, such flexibility in the schedule does not help decrease the risk of collusion when two teams advance to the next phase. 

## **10. Conclusion** 

We have quantified the risk of collusion in a group of three teams playing a single round-robin tournament, where two teams advance to the next phase. We have shown that the best way to minimize the risk of collusion is to enforce that the team that plays the first two group matches is the _a priori_ strongest team in the group, especially if the group is strongly imbalanced. However this may be deemed unfair to that team as it would be the only one vulnerable to collusion. This would also mean that Match Day 3 of the World Cup would feature none of the seeded teams. 

We have quantified how competitive imbalance within a group impacts the risk of collusion. We have also quantified by how much the risk of collusion would decrease if FIFA does not use the traditional 3-1-0 point system but adopts alternate point systems that forbid draws, the 3-0 and 3- 2-1-0 point systems. Even though it looks appealing on paper, the 3-2-1-0 point system does not do a better job at decreasing the risk of collusion than the 3-0 point system. Most important, when banning draws, FIFA would introduce new problematic situations of possible collusion where a team may decide to eliminate another team by deliberately losing the penalty shootout (these would be more likely with the 3-0 point system). 

The fact that there will be 16 groups of three makes the risk of collusion in at least one group very high, even in the most favorable case where all groups are strongly imbalanced and in every group Team A is the _a priori_ strongest team in the group. Our arguments shows that the introduction of groups of three is a terrible step back in the history of the World Cup. Not only it makes the ``disgrace of Gijon'' possible again, but it makes the risk of its repetition very high. Of course, not all teams would collude if given the opportunity, but even risk of match fixing may seriously tarnish 



26 



the World Cup, as unpredictability of the outcome is fundamental to its popularity, and to sport's popularity in general. 

Therefore, we have also described practical alternate formats for a 48-team World Cup that would eliminate or strongly decrease the risk of collusion, with groups of three, four, or six teams. 

Actually, whatever the rule that FIFA will use to rank the teams in a group of three, where only the group winner and the runner-up advance to the next phase, there will always be situations where Team A, the team that plays the first two group games, is neither qualified nor eliminated after Match 2, e.g., if A has one 1-0 win and one 2-0 loss. In these situations, some results of Match 3 will qualify Team A and others will eliminate it, raising the risk of collusion between Teams B and C to eliminate Team A. As a consequence, if FIFA wants to keep groups of three with the best two teams advancing, Format 5 of Section 9 seems the best solution to minimize the risk of collusion, where the knockout bracket is seeded based on performance across groups (see also [27]). 

It is FIFA's responsibility to build a fair World Cup. It is not too late for FIFA to review the format of the 2026 World Cup. Let us encourage the FIFA Council to realize the danger posed by groups of three, and, if it really wants a 48-team World Cup, opt for one of the formats described in Section 9. 



27 







28 







29 







30 


