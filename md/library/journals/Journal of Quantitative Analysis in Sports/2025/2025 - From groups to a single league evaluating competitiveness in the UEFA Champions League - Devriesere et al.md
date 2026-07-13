<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2025/2025 - From groups to a single league evaluating competitiveness in the UEFA Champions League - Devriesere et al.pdf -->

J. Quant. Anal. Sports 2026; aop 

### **Research Article** 

Karel Devriesere*, Dries Goossens and Frits Spieksma 

# **From groups to a single league: evaluating competitiveness in the UEFA Champions League** 

https://doi.org/10.1515/jqas-2025-0128 Received September 16, 2025; accepted April 14, 2026; published online May 8, 2026 

**Abstract:** Recently, UEFA changed the group stage of its international soccer competitions to an incomplete round robin tournament. Previously, teams were divided into groups, each playing a double round robin tournament with a resulting ranking table. In contrast, the new format has all teams competing in one league, producing a single ranking. We investigate the effect of the new format on the probability of competitive matches in the UEFA Champions League. A match is non-competitive if the prize for at least one opponent does not depend on the match outcome, or if there exists an opportunity for both opponents to collude; otherwise, we call a match competitive. Using Monte Carlo simulations and integer programming, we show that the new format results in proportionally more competitive matches than the old format, although it also results in a noticeable increase in the risk of collusion. 

**Keywords:** collusion; incomplete round robin; integer programming; OR in sports; simulation; UEFA Champions League 

## **1 Introduction** 

The UEFA Champions League – widely regarded as one of the most prestigious football club competitions – has recently undergone a significant change in the structure of its multi-stage format generating substantial academic 

***Corresponding author: Karel Devriesere** , Business Informatics and Operations Management, Ghent, Belgium, E-mail: Karel.Devriesere@UGent.be. https://orcid.org/0000-0002-6774-849X **Dries Goossens** , Business Informatics and Operations Management, Ghent, Belgium; and Core Lab CVAMO, FlandersMake@UGent, Belgium, E-mail: Dries.Goossens@UGent.be. https://orcid.org/0000-0003-0224-3412 **Frits Spieksma** , Department of Mathematics and Computer Science, Eindhoven University of Technology, The Netherlands, E-mail: f.c.r.spieksma@tue.nl. https://orcid.org/0000-0002-2547-3782 

interest (Csató et al. 2026; Csató and Gyimesi 2026b; Csató and Ilyin 2025; Guyon et al. 2025; Gyimesi 2024; Winkelmann et al. 2025). In the previous format, the competition began by partitioning teams into separate groups, each organized as a double round robin tournament (i.e., every team plays the others in its group twice), with its own ranking table. In contrast, the new format begins with a so-called incomplete round robin (iRR), in which each team plays against eight different opponents, and all teams are collectively ranked in a single unified table. A precise description of these formats is given in Section 2. According to UEFA (Union of European Football Associations), this revised format is intended to “result in more competitive matches” (UEFA 2024a). In this work, we examine whether UEFA’s claim is justified. 

A sports competition typically consists of a series of matches whose outcomes determine the allocation of specific prizes among competitors. The goal of the first stage of the UEFA Champions League is to determine the set of teams that qualify for the knockout stage. In the previous format, teams could qualify for the knockout stage by finishing as one of the top two teams in their respective group. In the new format, teams can qualify in two ways for the Round of 16: either by direct qualification (awarded to the top eight teams) or by qualification throughout a knockout phase (granted to teams ranked 9th to 24th), from which additional spots in the knockout stage are subsequently earned. The latter prize is evidently less desirable. We define a match as competitive if _a priori_ both teams have an incentive to exert full effort so as to increase their chances of securing the best possible prize. We identify three distinct types of non-competitive matches: (a) asymmetric matches, in which exactly one of the two teams is indifferent with respect to the match outcome (e.g., because it has already secured its prize); (b) stakeless matches, where the outcome has no impact on the prize allocation for either team; and (c) collusive matches, in which both teams still have something at stake, but where they can agree on a specific outcome that secures the desired prize for both. Thus, we classify the state of a match into one of these four categories: competitive, asymmetric, stakeless, or collusive (see Section 3 for 

Open Access. © 2026 the author(s), published by De Gruyter. 

This work is licensed under the Creative Commons Attribution 4.0 International License. 

> **2 —** K. Devriesere et al.: From groups to a single league 

examples). As far as we are aware, these three types of noncompetitive matches have not been considered before in the same framework. We emphasize that the competitiveness of a match is determined _a priori_ , and hence does not depend on its outcome or the margin by which it was decided (e.g. the 2024/25 Champions League final between PSG and Inter was definitely a competitive game, even though PSG obtained an overwhelming 5-0 victory). 

Ideally, the race for the prizes remains close, culminating in an exciting climax on the final day of the competition. According to the outcome uncertainty hypothesis proposed by Rottenberg (1956), if prizes are decided before the competition concludes, the remainder of the competition will not generate much interest. Indeed, both TV viewership and stadium attendance seem to be positively linked with outcome uncertainty (Cox 2018; Forrest and Simmons 2002; García and Rodríguez 2002; Pérez Carcedo et al. n.d.; Schreyer et al. 2018). Moreover, Buraimo et al. (2022) identify elevated interest for matches potentially significant for end-of-season outcomes in the English Premier League. In contrast, fan engagement is expected to decline significantly once their favorite team no longer has a chance of winning any of the prizes (Losak and Halpin 2024; Pawlowski and Nalbantis 2015; Villar et al. 2009). Moreover, a team’s level of effort is likely to decline once its prize outcome is determined, compared to when it is still in contention (Courty and Cisyk 2024; Page and Page 2009; Szymanski 2003). Finally, the integrity of the competition is another reason to avoid non-competitive matches (Vanwersch et al. 2025). Collusive matches provide both teams with an incentive for matchfixing. Asymmetric and stakeless matches have also repeatedly been linked to match-fixing (Caruso 2009; Duggan and Levitt 2002; Elaad et al. 2018; Feddersen et al. 2023; Jetter and Walker 2017). Indeed, if the cost of missing out on a prize exceeds the potential cost of corruption, the team still in the running for a prize might be tempted to try to bribe its indifferent opponent. 

The topic of non-competitive matches has been studied before for major football competitions. The 2026 FIFA World Cup was originally designed to contain a group stage with groups of three teams instead of four. Guyon (2020), Chater et al. (2021) and Stronka (2024) show that this switch from even-numbered groups to odd-numbered groups increases collusion opportunities and, together with Rennó-Costa (2023), Guajardo and Krumer (2024) and Csató and Gyimesi (2026a), propose remedies such as alternative designs and dynamic scheduling. Next to collusive matches, Chater et al. (2021) also estimate the sum of asymmetric and stakeless matches for the FIFA World Cup and find that the schedule in which the two strongest teams play against each other in the last round produces the lowest number of com- 

petitive games. Csató (2023) studies the effect of tie-breaking rules on collusion opportunities in the 2022/23 UEFA Nations League and finds that competitiveness can be promoted by preferring goal difference over head-to-head results as the primary tie-breaking rule. Csató et al. (2024) compare the expected number of asymmetric and stakeless matches over the 12 possible schedules for the previous Champions League format. They find that these types of matches are minimized if the strongest team plays at home in the last round against one of the middle teams. Recently, the number of non-competitive matches has been approximated for the new Champions League format by a simple heuristic (Gyimesi 2024). It was found that the new Champions League format reduces the number of asymmetric and stakeless games compared to the previous format. 

Most of the literature considering asymmetric, stakeless and/or collusive matches has focused on tournaments with a small number of teams, where these matches can be identified with a few rules of thumb (Devriesere et al. 2026). However, for a tournament the size of the new Champions League format, determining exactly whether a team’s prize is secured is computationally challenging. In this paper, we deal with this by using integer programming. Moreover, we study how to detect the opportunity for collusion for a large number of teams. Since we take into account collusion, use exact rather than heuristic methods, and consider multiple types of schedules, our work differs considerably from the work of Gyimesi (2024). To compare the number of competitive and non-competitive matches between the group stage format and the new iRR format of the UEFA Champions League, we use Monte Carlo simulation, which is one of the most popular methods to compare tournament formats (Devriesere et al. 2025). In this way, our paper contributes to the growing literature dealing with how tournament design impacts competitiveness. 

This paper is organized as follows. Section 2 discusses the reform of the Champions League format. In Section 3, we define (un)competitive matches and illustrate these concepts with examples. Section 4 discusses the methodology to perform a comparative analysis between the old and new Champions League format. Section 5 presents the results of our simulation study, building up to the conclusions in Section 6. 

## **2 The UEFA Champions League reform** 

Since 2003, the first stage of the UEFA Champions League has featured a group stage comprising 32 teams partitioned into 

> K. Devriesere et al.: From groups to a single league **— 3** 

eight groups of four. Each group followed a double round robin format, in which every team played each of the other three teams twice, once at home and once away. The top two teams from each group advanced to the knockout stage. Entry into the group stage was determined either by direct – qualification granted to e.g. champions of higher-ranked national associations - or by progression through one or more qualifying rounds (Csató 2022b). Beginning in 2009, these qualifying rounds were restructured into two separate tracks: one for league champions from lower-ranked associations, and another for non-champions from higher-ranked associations. In the remainder of this text, we label this “the group stage format”. 

Beginning with the 2024/25 season, UEFA implemented a new competition format for the Champions League, replacing the traditional group stage with an incomplete round robin (iRR) structure (see e.g. Li et al. (2025) and Devriesere and Goossens (2025)). Under this revised system, teams are no longer divided into groups but instead compete within a single league table. The number of participating clubs has been increased from 32 to 36, with the additional slots allocated as follows: one place each for the two highest-performing national associations from the previous season, one place for the third-ranked club from the fifthbest association, and one additional berth in the champions path. In this new iRR format, also known as the “league phase”, the teams are divided into fours pots (largely based on strength, as measured by the UEFA club coefficient) and each team plays against two distinct teams from each pot, without the need for transitive matchups (i.e., matches A vs. B, and B vs. C do not imply a match between A and C) (Guyon et al. 2025). 

Following this phase, a two-legged play-off round is contested between teams ranked 9th to 16th (seeded) and those ranked 17th to 24th (unseeded). The winners of these fixtures join the top eight teams from the league phase in the knockout stage, after which the competition resumes its traditional knockout format, including quarterfinals, semi-finals, and the final. Notably, similar structural reforms have also been applied to UEFA’s Europa League and Conference League competitions, which are UEFA’s second and third most prestigious club tournaments, respectively. 

Closely related to the incomplete round robin (iRR) format is the Swiss system (see e.g. Sauer et al. (2024)). Like the iRR format, the Swiss format involves teams playing a fixed number of matches against only a subset of all possible 

opponents. However, the key distinction lies in the scheduling methodology: whereas the iRR format establishes the entire match schedule prior to the start of the competition, the Swiss system schedules rounds dynamically. Pairings in each round are determined based on predefined rules that take into account prior results, typically matching teams with similar performance records as the tournament progresses. 

## **3 Competitive matches: definitions and examples** 

We distinguish three types of non-competitive matches in one framework: stakeless, asymmetric and collusive matches. In a stakeless match, both teams are indifferent about the match outcome: no outcome can have an impact on the prize that they collect at the end of the tournament. If exactly one of the opponents is indifferent, but the other can still lose the prize it currently holds or obtain a better one depending on the match outcome (and possibly the outcome of other matches), the match is said to be asymmetric. We note that stakeless and asymmetric matches have been called strongly and weakly stakeless, respectively, in the works of Csató et al. (2024) and Gyimesi (2024). A match is collusive if both teams have something at stake, and there exists an outcome such that both teams guarantee their best possible prizes. This does not imply that collusion necessarily occurs, but rather that both teams possess aligned incentives to facilitate such an outcome. In a competitive match, neither team is indifferent, and their objectives are incompatible, in the sense that collusion cannot help both teams achieve their best possible prizes. Hence, any game that is not asymetric, stakeless, or collusive is considered to be competitive. We emphasize that in our context the prize that a team can win depends only on its position in the final ranking. 

Table 1 illustrates each of the states a match can be in. It shows two hypothetical ranking tables of a double round robin tournament, as well as a table with the final round matches, indicating for each match its state under both ranking tables. Similar to the UEFA Champions League, teams are ranked using a point-based system where teams earn 3 points for a win, 1 point for a tie and no points for a loss; we call this a tournament with score vector (3,1,0). Goal difference (GD), i.e. the difference between the sum of the goals that a team scored over the matches minus the sum of the goals it conceded, is the primary tie-breaker, followed by 

> **4 —** K. Devriesere et al.: From groups to a single league 

**Table 1:** Examples of non-competitive matches. 

||**(a) Rankin**|**g table 1**||
|---|---|---|---|
|**Rank**|**Team**|**Pts**|**GD**|
|1|A|24|+5|
|2|B|23|+1|
|3|C|23|+1|
|4|D|23|+1|
|5|E|20|+1|
|6|F|16|−2|
|7|G|10|−2|
|8|H|9|−5|
||**(b) Rankin**<br>|**g table 2**<br>||
|**Rank**|**Team**|**Pts**|**GD**|
|1|A|23|+2|
|2|B|23|+1|
|3|C|23|+1|
|4|D|23|+1|
|5|E|15|+0|
|6|F|14|+0|
|7|G|10|−1|
|8|H|7|−4|



||**(c) Final round matches and their state**<br>**to the ranking tables**|**according**|
|---|---|---|
|**Match**|**Table 1**|**Table 2**|
|A-G|Collusive|Collusive|
|B-C|Competitive|Competitive|
|E-F|Asymmetric|Stakeless|
|D-H|Competitive|Competitive|



goals scored (not shown in the tables). There are two prizes: top 3 and top 7. It can be verified that both tables are possible outcomes of a double round robin tournament where the matches indicated in Table 1c still need to be played. 

Consider first the standing as in Table 1a. The game B-C is competitive, since both teams are still in the running for top 3, but could also drop to a top 7 ranking. For example, if B and C score the same number of goals, they can be overtaken by D and E, while a win guarantees a place in the top 3. Note that although their objectives are incompatible, there is a possibility that they both reach top 3 (in case of favorable outcomes in the matches D-H and E-F). Furthermore, we see that F is eliminated from the top 3 and guaranteed to finish at least in the top 7, while E can still reach top 3. Hence, match E-F is asymmetric. If we look at Table 1b, we see that the match E-F is stakeless, as both are eliminated from the top 3 but are guaranteed to finish in the top 7. The match 

A-G is in both cases collusive, but the outcome by which both teams guarantee their prize differs. In the ranking in Table 1a, a loss for A with a goal difference of less than 4 ensures that both A and G guarantee their prize (top 3 and top 7). Hence, in this scenario the match A-G is collusive. If we now consider the standing as in Table 1b, we see that a tie ensures that both A and G are guaranteed to finish in the top 3 and top 7, respectively. Hence, in this scenario the match A-G is collusive as well. In fact, in a tournament with outcomes win, draw and loss, a tie and a small loss are the only two outcomes which make a match prone to collusion. Note that in both outcomes, goal difference plays a crucial role as the primary tie-breaking rule. For actual examples of asymmetric and stakeless matches, we refer to Csató et al. (2024). 

We further note that there are other ways to express the competitiveness of matches. Schilling (1994), for example, quantifies the importance of a match with respect to a prize _x_ for team _i_ as the difference between the conditional probability of reaching prize _x_ if _i_ wins and reaching the prize if _i_ loses. This measure has extensively been used to compare tournament formats (e.g. Scarf et al. (2009)). Goossens et al. (2012) measure match importance on a continuous scale based on the number of teams that are eliminated for certain prizes. Next, Geenens (2014) and Corona et al. (2017) quantify the decisiveness of a match based on entropyrelated measures, while Goller and Heiniger (2024) consider event-importance. The recent working paper by Csató and Gyimesi (2026b) introduces a probabilistic match classification scheme and also applies it to the old and new formats of the UEFA Champions League. For example, a match is considered collusive if both teams are much better off by playing a draw than losing, while it does not make sense to take risks in order to win for neither of them. The important difference with the classification used in this paper is that the above-mentioned papers consider competitiveness as a probabilistic measure. Consequently, some matches found to be competitive in this paper may be classified as collusive (or non-competitive) in other frameworks. Even though these measures can be insightful, they require arbitrary cutoff points to classify matches as “sufficiently” competitive. In contrast, our definitions require no such assumptions, allowing a robust comparison between different formats. 

In order to determine whether a match is competitive, asymmetric, stakeless or collusive, we need to establish for both teams whether they have something at stake. If teams have nothing at stake, we say that the team’s prize is fixed. A team’s prize is said to be fixed if (i) the team has been 

> K. Devriesere et al.: From groups to a single league **— 5** 

eliminated from contention for any higher prize and (ii) it is guaranteed to receive the prize for which it currently qualifies. Determining whether the former condition holds is known as the _elimination problem_ (Bernholt et al. 1999), while the verifying the latter was termed the _guaranteed points placement problem_ (Christensen et al. 2015). 

If the score vector is (1,0), meaning matches cannot end in a tie and teams earn 1 point for a win and 0 for a loss, the so-called _magic number_ or _clinching number_ indicates the number of additional wins a team needs to secure winning the championship (Husted et al. 2021). In this case, deciding whether a team is eliminated for the first position can be solved in polynomial time (Adler et al. 2002; Gusfield and Martel 2002; Robinson 1991; Schwartz 1966; Wayne 2001). However, building on the results of Hoffman and Rivlin (1970), McCormick (1996) mentions that determining whether a team is eliminated from the top _k >_ 1 positions is already NP-complete even for this simple score vector. For a tournament with the (3,1,0)-score vector, the elimination problem was proven to be NP-complete by Bernholt et al. (1999), while the guaranteed points placement problem was proven to be coNPcomplete by Christensen et al. (2015), even when only considering the first and last position, respectively. However, depending on the remaining matches, algorithms exist that can solve these problems in polynomial time (Schlotter and Cechlárová 2018). In practice, however, both problems are usually solved with integer programming (Goossens et al. 2012; Gotzes and Hoppmann 2022; Raack et al. 2014; Ribeiro and Urrutia 2005). 

## **4 Methodology** 

In this section, we first show how we identify whether a match is asymmetric, stakeless, collusive or competitive 

(Section 4.1). Next, in order to simulate the Champions League under the previous and current format, we need to generate a feasible draw (Section 4.2) together with a schedule (Section 4.3). Moreover, for each match we need to simulate an outcome (Section 4.4). Finally, we need to make assumptions about the set of clubs, prizes and tie-breaking rules (Section 4.5). 

### **4.1 Identifying the state of a match** 

Here, we show how to identify the state of a match. We first show how solving both the elimination problem and the guaranteed points placement problem for a given team _t_ determines whether that team has something to play for. Thus, solving these two problems for all teams reveals whether or not a match is stakeless, or asymmetric. Second, we describe a procedure to identify whether a match is collusive. Throughout this section, we assume that goal difference is the primary tie-breaking rule, in accordance with the official tie-breaking rules in the iRR format (see Section 4.5). 

We first recall the formulation of the elimination problem proposed by Ribeiro and Urrutia (2005), which aims to determine the highest possible rank team _t_ can still achieve. Let _T_ be the set of teams and _M_ the set of matches that remain to be played. We define _yi_ as a binary variable that is 1 if team _i_ ∈ _T_ finishes with strictly more points than the given team _t_ . The binary variables _𝑤m, dm, lm_ are 1 if match _m_ = ( _i, j_ ), where _i_ is the home and _j_ is the away team, results in a win, tie or loss for _i_ , respectively. The sets _Mi_<sup>_h_and</sup><sup>_M_</sup> _i_<sup>_a_denotetheremaining</sup> home ( _h_ ) and away ( _a_ ) matches of team _i_ , respectively. The variable _pi_ represents the number of points of team _i_ after all matches are played. Let _Bi_ be the current points of team _i_ . Then, we can construct the following integer program: 



> **6 —** K. Devriesere et al.: From groups to a single league 

The objective function (1) minimizes the number of teams ranked above _t_ . Constraints (2) state that each match _m_ should result in exactly one of the three possible outcomes. Constraints (3) determine the points of each team after all matches are played. Finally, constraints (4) ensure that _yi_ is set to 1 if _i_ finishes with strictly more points than _t_ . Thus, team _t_ is eliminated from the top _k_ positions if and only if _z_ is at least _k_ . Observe that if _t_ has at least one remaining game, given that goal difference is the first tie-breaking rule in case of equal points, it is sufficient to minimize the 

number of teams that are strictly ranked above _t_ . Indeed, we can set the number of goals scored by _t_ in its remaining matches arbitrary large and the goals scored of other teams as small as possible, i.e. 0-0 for a tie and 1-0 or 0-1 for a home and away win, respectively. 

To model the guaranteed points placement problem, we replace constraints (4) with (8). By maximizing _z_ , we achieve the largest possible number of teams finishing with no more points than _t_ . Then, team _t_ is guaranteed to finish in the top _k_ if and only if _z_ is at most _k_ − 1. 







Observe that if _t_ has at least one remaining game, given that goal difference is the first tie-breaker in case of equal points, it is sufficient to maximize the number of teams that finish with the same number of points as _t_ . Indeed, we can assume _t_ loses its remaining games with an arbitrary large goal difference such that any other team that finishes with an equal number of points as _t_ ranks above _t_ . Solving both problems described above determines whether teams still have something at stake or not. This information is sufficient to identify asymmetric and stakeless matches. 

If a match is neither asymmetric nor stakeless, it may yet be collusive. To detect whether a match ( _i, j_ ) is prone to collusion, we distinguish two cases: when collusion is realized through a tie or a small loss. A further distinction can be made based on how many games are left. In order to identify whether a match is collusive through a tie, we solve the guaranteed points placement problem for both _i_ and _j_ , assuming the match ends in a tie. If after this match, _i_ and _j_ still have at least one other match (against different opponents), we do not have to take goal difference into account since both _i_ and _j_ may lose their last game with an arbitrary large goal difference. In case ( _i, j_ ) is the last game of _i_ and _j_ , we cannot neglect goal difference, as there can be teams that can finish with the same number of points as _i_ and/or _j_ by scoring the same number of goals, but with a worse goal difference. In case all teams have at most one remaining game left, we can simply iterate over all remaining matches to determine the maximum number of teams that can still finish above _i_ ( _j_ ). We first check, for each match other than ( _i, j_ ), whether both teams in that match can be ranked above _i_ ( _j_ ), taking into account the tie-breaking rules. If not, we 

check whether one of the teams finishes with at least the same number of points as _i_ ( _j_ ), given it wins that match. This way, we count the maximum number of teams that can finish above _i_ , and we do the same for _j_ . Finally, note that a collusion by a small loss is only possible for match ( _i, j_ ) if this match is the final match for the losing team. First, we determine whether _i_ or _j_ guarantees its prize when losing with only one goal conceded, while the other team guarantees its prize with a high number of goals scored. For practical purposes, we consider small losses up to a difference of five goals. This is in line with Chater et al. (2021), who check all possible goal differences between −5 and +5 to check collusion opportunities. If the answer is yes, we check whether one of the outcomes (1 _,_ 0) _,_ (2 _,_ 0) _,_ (3 _,_ 0) _,_ (4 _,_ 0) _,_ (5 _,_ 0), assuming here w.l.o.g. that _i_ is the team that must win, guarantees the best possible prize for both teams. If yes, the match is collusive by a small loss. 

### **4.2 Draw** 

#### **4.2.1 Group stage format** 

In the group stage format, 32 teams are drawn into eight groups of four teams each. Since the aim of the groups is to balance teams of similar strength over the groups, the 32 teams are first partitioned into 4 pots. Since the 2018/19 season, pot 1 contains the former Champions and Europa League winners, together with the champions of the six (or seven) countries with the highest UEFA association coefficients. Pots 2, 3 and 4 contain the other teams, seeded based on their UEFA club coefficients. Each group consists of one team from each pot. 

> K. Devriesere et al.: From groups to a single league **— 7** 

The draw procedure works as follows. First, clubs from pot 1 are randomly assigned to groups. Next, clubs from pot 2 are drawn. For each drawn team, “ _the computer indicates which groups are available for this club, and a bowl is prepared containing balls representing each of the groups into which the club could be drawn_ ” (UEFA 2023). This process is repeated for clubs of pot 3 and finally for clubs of pot 4. In order to simulate the group stage draw, we implement the official draw procedure: we randomly assign the teams to groups, in increasing order of the pots, and check if the draw can be completed in case the team is assigned to its drawn group. We propose to use an integer program to check the latter condition. If not, we remove the group from the team’s available groups and draw a new group, until we find a group such that the draw can be completed. For this purpose, let _T_ be the set of teams, _Ph_ be the teams of pot _h_ (with | _P_ | pots in total) and _C_ be the set of associations that are represented in the Champions League. Let _T c_ be the teams of association _c_ and _a_ ( _i_ ) be the association of team _i_ ∈ _T_ . Let _G_ be the set of groups. We use a binary variable _xig,_ ∀ _i_ ∈ _T, g_ ∈ _G_ that is 1 if team _i_ is assigned to group _g_ and 0 otherwise. Let _𝜓 ig_ be a parameter that is 1 if _i_ is allocated to group _g_ in the previous iterations, and 0 otherwise. 





Constraints (9) guarantee that each group contains at most one team from association _c_ ∈ _C_ . Constraints (10) assign each team to exactly one group, while constraints (11) ensure that each group consists of exactly one team from each pot. Previously drawn allocations are fixed by (12). 

In practice, prior to the draw, UEFA formed pairings of teams from the same association (one pairing for associations with two or three teams, two pairings for associations with four or five teams) based on television audiences, where one team would be drawn into Groups A–D and another team would be drawn into Groups E–H, so that the two teams would play on different days. These TV pairings seem to have a non-negligible impact on the draw probabilities (Guyon 2021). However, to correctly assess the impact of the change in tournament format rather than other specific rule changes, we decided to omit this draw constraint. 

#### **4.2.2 iRR format** 

For the draw of the iRR format, the following constraints need to be satisfied (UEFA 2024c): 

1. Each team faces exactly two different opponents from each pot, one at home and one away 

2. A team is never matched with a team from its domestic association 

3. A team faces at most two opponents from the same association 

With the expansion of 32 to 36 teams, one extra spot is granted to the fifth-ranked association. Moreover, one additional spot is given to each of the two associations with the best collective performance in the previous season of UEFA club competitions. Finally, the number of teams qualifying via the Champions Path has increased by one (Csató and Ilyin 2025). In addition to matching teams, also the home and away status is determined. Similarly to previous years, the draw is conducted iteratively. First, a team from pot 1 is drawn. Next, its eight opponents, two from each pot, are drawn, indicating for each opponent whether it is faced at home or away. This procedure is repeated for all remaining teams from pot 1. Next, a team from pot 2 is drawn, together with its 6 opponents from pots 2-4. This process is repeated for all teams from pot 2, next for pot 3 and finally for pot 4. 

Similarly to the group stage, we now present an integer program that checks whether the draw can be completed if a match is drawn. We use a binary variable _mij,_ ∀ _i, j_ ∈ _T_ that is 1 if _i_ plays home against _j_ and 0 otherwise. Let _𝜔ij_ be a parameter that is 1 if _i_ and _j_ were matched in a previous iteration, and 0 otherwise. Before committing to opponent _j_ being drawn for team _i_ , we check if the following set of constraints yield a feasible solution: 



> **8 —** K. Devriesere et al.: From groups to a single league 

Constraints (14) ensure that a team does not play against a team from the same association. Constraints (15) ensure that each team is matched with at most two teams from the same (but different than its own) association. Constraints (16) and (17) guarantee that a team faces exactly one team from each pot at home and one team from each pot away. Constraints (18) state that a team is not matched to the same opponent twice. Previously drawn matches are fixed by constraints (19). Naturally, a team does not face itself, which is stated by constraints (20). If the integer program is feasible, we pick the drawn team, update the value for the corresponding _𝜔_ parameter, and continue the draw. If not, then we remove team _j_ from the available opponents of _i_ and draw a new team. This approach mimics the official iterative procedure of UEFA, and guarantees that we will find a feasible draw, if one exists (see also Guyon et al. (2025)). 

Constraints (15)–(21) do not avoid the possibility of a draw that needs 9 matchdays to be completed. Such a scenario is possible, as is shown in Guyon et al. (2025). Since this only has an extremely small probability, however, we do not enforce this in the model presented above. Instead, if such a scenario arises, which would be detected by the integer program in the next Section, we simply perform another draw. 

### **4.3 Schedule** 

Given a draw, a feasible schedule needs to be constructed. We now introduce the following notation. Let _B_ = {1 _,_ … _,_ 8} be the set containing the indices of the rounds, and _S_ = {1 _,_ … _,_ | _S_ |} the set containing the indices of the time slots. Let _S_ be partitioned into subsets _Sb_ containing the indices of time slots of round _b_ ∈ _B_ . In each time slot _s_ ∈ _S_ , a certain number of matches _ms_ need to be played. Each team plays exactly one match in each round, in one of the available time slots. For example, the second round of the 2024/25 competition was played on Tuesday and Wednesday of the first week of October. Both Tuesday and Wednesday contain two time slots: 18:45 and 21:00. In the early time slot, two matches need to be planned while in the late time slot seven matches need to be planned, for a total of 18 matches in that round. It is important in this work to consider the specific time slots, and not only the rounds, because match outcomes of earlier slots in same round potentially impact the prize status of teams in the remaining matches. 

For both the group stage and the iRR format, UEFA gives surprisingly little information on how the matches 

are scheduled. The only additional scheduling requirement specific to the iRR format, beyond those implied by the published draw rules, is as follows: “A club does not play more than two home or two away matches in a row and each club plays one home match and one away match across the first two matchdays and across the last two matchdays” (UEFA 2024b, Article 17). The same requirement was also present in the previous format (Csató et al. 2024). 

#### **4.3.1 Group stage format** 

Csató et al. (2024) observe that from the 2021/22 season onwards, rounds 4/5/6 are the mirror image of rounds 3/2/1. Since in the group stage format non-competitive matches cannot occur before the fifth round, the order of the matches before the fifth round has no impact on competitiveness. Disregarding the order of the matches in the first four rounds, there remain 12 valid schedules, which can be characterized by the matches in the last two rounds (Csató et al. 2024). These schedules are listed in Table 2. The name of the 

**Table 2:** The final two rounds for each of the 12 valid schedules for the UEFA Champions League group stage (note that the order of the first four rounds does not affect competitiveness) (Csató et al. 2024, Table 9). 

|**Schedule**|**Round 5**|**Round 6**|
|---|---|---|
|1231|(1, 2)|(3, 1)|
||(4, 3)|(2, 4)|
|2113|(2, 1)|(1, 3)|
||(3, 4)|(4, 2)|
|1241|(1, 2)|(4, 1)|
||(3, 4)|(2, 3)|
|2114|(2, 1)|(1, 4)|
||(4, 3)|(3, 2)|
|1321|(1, 3)|(2, 1)|
||(4, 2)|(3, 4)|
|3112|(3, 1)|(1, 2)|
||(2, 4)|(4, 3)|
|1341|(1, 3)|(4, 1)|
||(2, 4)|(3, 2)|
|3114|(3, 1)|(1, 4)|
||(4, 2)|(2, 3)|
|1421|(1, 4)|(2, 1)|
||(3, 2)|(4, 3)|
|4112|(4, 1)|(1, 2)|
||(2, 3)|(3, 4)|
|1431|(1, 4)|(3, 1)|
||(2, 3)|(4, 2)|
|4113|(4, 1)|(1, 3)|
||(3, 2)|(2, 4)|



> K. Devriesere et al.: From groups to a single league **— 9** 

schedule reveals the matches of the team from pot 1, e.g. in schedule 1231, the team from pot 1 plays a home game against the team from pot 2 in round 5 and plays away against the opponent from pot 3 in round 6. Rounds can have up to 4 time slots, 2 on Tuesdays and 2 on Wednesdays, except for the last round where all matches of the same group are played at the same time. For round 5, in some groups one match was played at 18:45 and the other at 21:00, while in other groups both matches were played at 21:00. Since it is unclear why in some cases matches are played in separate time slots, we make the conservative assumption that in every round, all groups play their matches simultaneously. Hence, in the group stage the number of time slots coincide with the number of rounds. Note that this leads to a small underestimation of the number of non-competitive matches. 

In general, Csató et al. (2024) found that unattractive matches occur less frequently in schedules in which, in the last round, the strongest team plays at home against one of the two middle teams compared to other schedules. To assess the effect of the schedule on the group stage format, 

we iterate over all the options and schedule each group according to that option. Since in practice groups may be scheduled according to different options, we also include the option where each group is scheduled according to a randomly selected, hence possibly different, schedule. 

#### **4.3.2 iRR format** 

All matches of the last round of the iRR format take place at the same time, so there is only one time slot in the last round. In general, the first round is played in six time slots and rounds 2–7 are played in four time slots. Finding a feasible schedule for the iRR format is less straightforward but can be done by integer programming. Let _T_ again be the set of teams, _B_ be the set of rounds, _Sb_ be the set of time slots in round _b_ ∈ _B_ and _ms_ be the required number of matches in slots _s_ ∈ _Sb_ , _b_ ∈ _B_ . Let _Ni_<sup>_H_and</sup><sup>_N_</sup> _i_<sup>_A_be the sets</sup> of drawn opponents where team _i_ plays home and away against, respectively. Let _xijs_ be 1 if match ( _i, j_ ) is scheduled in slot _s_ , and 0 otherwise. A feasible schedule for the UEFA Champions League satisfies the following constraints: 



> **10 —** K. Devriesere et al.: From groups to a single league 

Constraints (22) and (23) ensure that each home and away opponent is seen exactly once over all time slots. Constraints (24) guarantee that each team plays exactly one game in each round, while constraints (25) guarantee that in each time slot, the required number of matches is played. Next, constraints (26) and (27) forbid consecutive home or away matches in the first and last two rounds. Finally, constraints (28) and (29) enforce that teams play at most two consecutive home or away games. We remark that a similar integer program is also proposed in Melkonian (2024). 

We now describe several possible objectives for the schedule. From a commercial perspective, an important objective of UEFA is to maximize its television audience. Hence, we extend the schedule by taking into account the number of teams of the same association playing in the same time slot, as well as the number of matches between teams from pot 1 that are scheduled in the same time slot. Ideally, these matches should be spread out as much as possible. Therefore, we create a binary variable _ycs_ that is 1 if a team from association _c_ plays in slot _s_ and a binary variable _zs_ that is 1 if a team from pot 1 plays in slot _s_ . 





Constraint (32) regulates that _ycs_ can only be 1 if at least one team from association _c_ plays a game in slot _s_ . Similarly, constraints (33) ensure that _zs_ can only be 1 if at least one team from pot 1 plays a game in slot _s_ . Adding constraints (22)–(30) to (31)–(35) gives the formulation 1. 

From a competitiveness perspective, it is worthwhile to compare schedules in which matches of teams with similar strength are scheduled as much as possible at either the beginning or end of the scheduling period. This can be done, for example, by making an ordinal ranking of the teams based on some criterion such as Elo rating. Let _ri_ be the position of team _i_ ∈ _T_ in this ranking. Let _b_<sup>_l_</sup> | _B_ |−2<sup>be the index</sup> of the last time slot in round | _B_ | − 2. Then, the formulation 

2 pushes matches of teams with similar strength to the later time slots in the last two rounds. 



Let _b_ 3<sup>_f_betheindexofthefirsttimeslotofthethird</sup> round. Then, formulation 3 pushes matches of teams of similar strength to the earlier time slots in the first two rounds. 



As a final type of schedule, instead of pushing matches between teams of similar strength all to the beginning or end of the scheduling period, formulation 4 has an additional constraint that guarantees that teams do not start or end with two games against teams from pots 1 and 2. Similarly, it also ensures that teams do not start or end with two games against teams from pots 3 and 4. The goal here is to ensure some degree of balance at the start and finish of the competition. 



Finally, for the season 2024/25, we run the simulations also with the schedule that was used in practice. This schedule will be denoted by 24−25. The main features of the schedules are summarized in Table 3. 

### **4.4 Simulating match outcomes** 

One of the most used statistical models for simulating football results is based on the Poisson distribution (Ley et al. 2019; Maher 1982). The probability that in match ( _i, j_ ), the home team _i_ scores _k_ goals against away team _j_ is given by: 

> K. Devriesere et al.: From groups to a single league **— 11** 

**Table 3:** Summary of schedules in the iRR format. 

|**Schedule **|**Main characteristic**|
|---|---|
|0|No objective|
|1|Spread (a) matches of teams from pot 1 and (b) matches of<br>teams from the same association|
|2|Schedule matches between teams of similar Elo strength to<br>the final matchdays|
|3|Schedule matches between teams of similar Elo strength to<br>the first matchdays|
|4|Teams do not start or end with two games against (a) two<br>teams from pots 1 and 2 and (b) two teams from pots 3 and 4|
|24−25|The actual schedule used for the season 2024/25|





where _𝜆_<sup>_h_</sup> _i j_<sup>denotes the expected number of goals scored by</sup> _i_ as the home team in match ( _i, j_ ). Similarly, the probability ℙ _a_ ( _k_ ) of the away team _j_ scoring _k_ goals against _i_ can be found by substituting _𝜆_<sup>_h_</sup> _i j_<sup>for</sup><sup>_𝜆a_</sup> _i j_<sup>,theexpectednumberof</sup> goals scored by the away team. Note that this model assumes that the results of matches are independent. 

It is common to model the _𝜆_<sup>_h_</sup> _i j_<sup>and</sup><sup>_𝜆a_</sup> _i j_<sup>parametersas</sup> a function of the difference in strength between the two teams. Using a polynomial regression, Gyimesi (2024) estimates the value of these lambdas as a function of the winning probability _𝑤i, j_ of team _i_ in a home game against team _j_ , based on their Elo ratings Elo _i_ and Elo _j_ , and given as. 



Dagaev and Rudyak (2019) use a generalized linear model (GLM) with a log-link function, using the UEFA club coefficients as a strength measure, while Corona et al. (2019) use a Bayesian Poisson model. In the context of estimating match outcomes between national teams, Football Rankings (2020) expresses _𝜆ij_ as a quartic polynomial defined in terms of _𝑤ij_ . This model has been used first in the scientific literature by Csató (2022a), and later by e.g. Stronka (2024). Although more advanced methods exist, since the goal here is to compare tournament formats rather than to predict individual matches, we stick to the more common models. 

For each season, we use the Elo rating of teams at the start of the first matchday in the Champions League of that season (without further updates). Similar to Gyimesi (2024), the ratings from the website elofootball.com are used. In order to derive a reasonable model, we estimate the parameters by maximum likelihood, investigate the effect of the degree of the polynomial regression and compare it to a 

generalized linear model. Data from the Champions League group stage in seasons 2005/06 till 2022/23 were used to estimate the model parameters, resulting in a training set of 1968 matches, while seasons 2023/24 and 2024/25 were used to validate the models. It should be noted that data from the 2020/21, and 2021/22 seasons may be biased because several matches were played behind closed doors. 



where parameter _r_ is the number of potential outcomes and _pm_ and _em_ are the predicted and observed outcomes of match _m_ , respectively. Intuitively, it measures how closely the predicted match outcome is to the observed outcome and is argued by Constantinou and Fenton (2012) to be a better football performance metric than other prevalent methods like the log loss and Brier score. Indeed, it has been used in many other works that compare football prediction models, see for example Groll et al. (2019), Ley et al. (2019) and Hubáček et al. (2022). A lower RPS value denotes a more accurate fit. In order to estimate the probabilities for a home win, draw and home loss for each match ( _i, j_ ), we define the joint probability matrix _M_ where element _Mgi,gj_ denotes the probability of the score ( _gi, g j_ ). We consider scores up to five goals. For the Poisson based models, _M_ is computed based on the fitted lambdas. Then, match outcome probabilities were derived via the summation of the joint probability mass functions across the respective regions of _M_ . The results are shown in Table 4. Next to the fitted models, we also 

**Table 4:** Comparison of predictive models across two seasons. 

|**Model**|**W (%)**|**T (%)**|**L (%)**|**RPS**|**Correct**<br>**(%)**|**Season**|
|---|---|---|---|---|---|---|
|Random guess|46.76|22.86|30.38|23.40|31.25|2023/24|
|Cubic polynomial|43.75|30.21|26.04|17.33|59.38|2023/24|
|Quartic polynomial|44.79|28.12|27.08|17.34|59.38|2023/24|
|Quintic polynomial|47.92|25.00|27.08|17.34|59.38|2023/24|
|GLM|48.96|27.08|23.963|17.54|58.3|2023/24|
|Actual|46.88|20.83|32.29|–|–|2023/24|
|Random guess|46.76|22.86|30.38|23.96|37.50|2024/25|
|Cubic polynomial|46.53|20.83|32.64|19.12|54.17|2024/25|
|Quartic polynomial|47.22|18.06|34.72|19.13|56.25|2024/25|
|Quintic polynomial|47.92|16.67|35.42|19.19|56.25|2024/25|
|GLM|50.00|18.75|31.25|19.23|58.33|2024/25|
|Actual|53.47|12.50|34.03|–|–|2024/25|



W, win; T, tie; L, loss; RPS, ranked probability score. 

> **12 —** K. Devriesere et al.: From groups to a single league 

computed the historical percentage of wins (46.76 %), ties (22.86 %) and losses (30.38 %) and used those probabilities to guess the match outcomes. 

For each model, we report the percentage of matches resulting in a home win (W), home loss (L) and tie (T), as well as the RPS values. As can be seen from the model, the Poisson-based models clearly outperform a random guess based on the historical average. There seems to be little difference, however, between the performance of the Poisson-based models. Moreover, the models appear to perform better on the 2023/24 data, which is unsurprising given that they were trained exclusively on data from groupstage matches rather than league-stage matches. Nevertheless, the RPS values closely resemble the values of those found in the literature (see e.g. Ley et al. (2019)). After performing a Nemenyi test for both RPS and the percentage of correct guesses, taking the two seasons together, the 4 Poisson-based models where not found to significantly differ (the lowest _p_ -value observed for RPS was 0.34 and for the percentage of correct guesses it was even 0.99). 

Therefore, we also consider the following simpler procedure to predict match outcomes: for each match ( _i, j_ ), we round _𝜆_<sup>_h_</sup> _i j_<sup>and</sup><sup>_𝜆a_</sup> _i j_<sup>tointegers.Theresultingvaluesrepre-</sup> sent a score that we use to determine whether the match results in a home win, draw, or home loss. This outcome is then compared to the real outcome. Using this approach, the number of correctly predicted match outcomes for the season 24/25 is the highest when using the lambdas from the GLM. We therefore opted to use this model in our computational experiments. The corresponding formulas of _𝜆_<sup>_h_</sup> _i, j_<sup>and</sup><sup>_𝜆a_</sup> _i, j_<sup>aregiveninequations(42)and(43),</sup> respectively. 



Table 5 shows the fitted lambdas for the matches involving the strongest and second strongest, as well as the strongest and weakest teams in the season 2024/2025, respectively (see Tables A.5 and A.6 for the Elo ratings of the teams). 

We note that since the model was trained only on group stage matches, the estimated model might be imprecise for the incomplete round robin format. In particular, Csató (2025a) argues that the incomplete round robin format encourages attacking play, which reduces the probability of draws. Our results – albeit based on a single season – seem 

**Table 5:** Lambdas for some selected matches of the season 2024/2025. 

|**_i_**|**_j_**|**_𝝀_**<sup>**_h_**</sup><br>**_i, j_**|**_𝝀_**<sup>**_a_**</sup><br>**_i, j_**|
|---|---|---|---|
|Manchester City|Real Madrid|1.92|1.24|
|Real Madrid|Manchester City|1.62|1.46|
|Manchester City|Slovan|5.20|0.35|
|Slovan|Manchester City|0.44|3.89|



to confirm a change in playing style. This, in turn, may have an impact on the thresholds for qualification (Winkelmann et al. 2025). It is likely that as more data becomes available, more accurate models that better reflect the dynamics of this new format can be developed. 

### **4.5 Experimental design** 

In order to adequately assess the impact of the format change, we compare the two formats based on the six seasons from 2019/20 to 2024/25. Taking multiple seasons into account reduces the bias caused by the Elo distribution of the competing teams in one particular season. However, since the iRR format features 36 instead of 32 teams as in the group stage format, we need to select four additional teams. The official UEFA rules allocate one extra spot for the 5th-ranked national association, one extra spot for a team from the so called champions qualifying path and two additional spots for the best-performing associations in the previous season. For each season played according to the old format, we follow these rules in the following way: 

- We add the best team (according to the domestic league) that was not yet present in the original 32 teams for the two associations with the highest UEFA association coefficient of the previous season. 

   - If the club that would have qualified as the 5th-ranked national association did already qualify, the additional spot is allocated to the best performing non-qualified team from the non-champions path. 



- For the additional team coming from the champions path, we select the best performing non-qualified team. Specifically, we selected the team that lost with the smallest goal difference, breaking ties randomly. 

The four added teams for each of the seasons 2019/20 till 2023/24 can be found in Csató et al. (2025, Table 1.). To construct the pots for the iRR format, the winner of the Champions League’s past season was placed in pot 1, while the other teams were allocated to pots based on their UEFA club coefficients of the past season. We note that these rules resulted in a feasible draw for the above mentioned seasons. For the 

> K. Devriesere et al.: From groups to a single league **— 13** 

season 2024/25, we delete four teams when simulating the group stage format according to a similar interpretation of these rules. 

After simulating match results, teams are ranked in both formats according to their points. However, the tiebreaking rules changed with the iRR format. In the seasons before 2024/25, ties were first broken based on head-to-head results. In contrast, in the iRR format, total goal difference is the first tie-breaking rule. It is known that tie-breaking rules affect the probability of asymmetric, collusive, and stakeless games as demonstrated in Csató (2023) and Csató (2025b). Moreover, recall that it is sufficient to use the integer programs in Section 4.1 to compute the prize status if the first tie-breaking rule is goal difference. If the first tie-breaking rule is head-to-head, additional checks are possibly needed. Since we want to distinguish the effect of the tie-breaking rules with that of the format, when simulating the group stage we rank teams based on the tie-breaking rules that are used in the season 2024/25. This includes breaking ties based on goal difference, goals scored, away goals scored, wins and away wins, in this order. In reality, the next tie-breaking rule would be based on the number of points obtained collectively by the teams’ league phase opponents. For the sake of simplicity, however, tie-breaking rules that go beyond away wins are replaced by a random draw. 

Finally, we consider the following prizes: 

- Group stage: Top 2 (qualified), 3rd (qualified for the Europa League), 4th (eliminated) 

- iRR: Top 8 (qualified for the knockout stage), 9–24 (qualified for the play-offs that determine qualification for the knockout stage), 25–36 (eliminated) 

It can be argued that the first and second place in the group stage are different prizes, since the first place is seeded while the second place is unseeded in the knockout stage. However, in contrast to the prizes defined above, seeding does not directly lead to elimination from the tournament. Moreover, accounting for these alternative prizes would require reporting twice as many results, which would considerably increase the length of the paper and potentially reduce its readability. Therefore, we chose to take into account only the set of prizes mentioned above. 

## **5 Results** 

For both the group stage and the iRR format, we perform 10,000 simulations for each type of schedule (12 for the group stage and 5 for the iRR format) and each of the six seasons. For the group stage format, we also include the option that each group is scheduled randomly according to 

each of the 12 possible schedules, while, for the iRR format, we also simulate the actual schedule used in the season 2024/2025. Hence, the total number of simulations is (12 + 1) × 6 × 10,000 = 780,000 for the group stage and (5 × 6 + 1) × 10,000 = 310,000 for the iRR format. In each simulation, we simulate the draw, which designates the set of matches that need to be played. Next, we sample match outcomes for each of these matches. Then, we use those match outcomes to evaluate competitiveness in the different types of schedules. 

In order to mitigate the computational burden of the experiments, we impose a time limit of 10 min for generating a schedule for the iRR format. If the gap between a model’s best found solution and its linear programming relaxation is at most 1 %, we accept the resulting schedule. Note that we want to compare schedule types based on the same draw and match outcomes. Hence, if for a certain draw, we cannot produce each of the schedule types, we discard this draw, generate a new one, and try to solve each of the scheduling models again. We do this until we obtain 10,000 simulations for each model. 

### **5.1 Comparison group stage and iRR format** 

To compare both formats, we compare the results when a random schedule is used. For the iRR format, a feasible schedule could be found in every simulation within 10 min. Table 6 shows the average percentage of stakeless, asymmetric, collusive and the total number of noncompetitive matches, respectively, for both formats. The difference between the iRR and the group stage format is shown in the row Δ. 

Table 6 reveals that the percentage of competitive matches increases from less than 87 % to nearly 94 % under the new format, confirming UEFA’s claim (UEFA 2024a). We further observe that the number of stakeless and asymmetric matches is much lower in the iRR format (which is in line with the results of Gyimesi (2024)), while the percentage of collusive matches is slightly higher (0.17 % instead of 0.11 %). The small percentage of collusive matches may give the impression that collusion is not an issue in both formats. However, the probability that a season in the group stage format contains at least one collusion opportunity is 1 − (1 − 0.0011)<sup>96</sup> × 100 % = 10.18 %, while for the iRR format, this probability is 1 − (1 − 0.0017)<sup>144</sup> × 100 % = 21.73 %. This indicates that collusion poses a non-negligible threat, and that the iRR format is associated with a noticeable increase in its probability. This finding is consistent with the results of Csató and Gyimesi (2026b), who, using a different measure, also report an increased probability of collusive matches in incomplete round-robin tournaments. 

> **14 —** K. Devriesere et al.: From groups to a single league 

**Table 6:** Observed percentage of each type of match, averaged over the seasons, for each format with random schedule. This corresponds to 0 for the iRR format and each group being randomly assigned to one of the 12 possible schedules for the group stage format. 

|**Format**|**Stakeless (%)**|**Asymmetric (%)**|**Collusive (%)**|**Competitive (%)**|
|---|---|---|---|---|
|iRR|0.75|5.14|0.17|93.94|
|Group stage|2.78|10.28|0.11|86.82|
|Δ|−2.03|−5.14|+0.06|+7.12|
|U (p)|2.8×10<sup>9 </sup>(_<_0.01)|2.7×10<sup>9 </sup>(_<_0.01)|1.6×10<sup>9 </sup>(_<_0.01)|5.4×10<sup>8 </sup>(_<_0.01)|
|_r_rb|−0.55|−0.49|+0.10|+0.70|



To test whether these values differ significantly, we perform a Mann-Whitney U test, which is a nonparametric test to evaluate whether two independent samples follow the same distribution. In this case, we test whether the values for stakeless and asymmetric matches are higher in the group stage compared to the iRR format. Similarly, we test whether the values for collusive and competitive matches are lower in the group stage compared to the iRR format. The resulting U-statistics (U) and corresponding p-values (p) are shown in Table 6. All values were found to significantly differ from each other ( _p <_ 0.01). Next, we compute the Rank-Biserial Correlation ( _r_ rb) to measure the strength of the association between the formats and the observed probability of non-competitive matches. A value of 0 indicates no correlation, while a value of +1 and −1 indicate a perfect positive and a perfect negative correlation, respectively. For example, we observe a strong positive effect (+0.70) of the iRR format on competitive matches. Based on Table 6, we conclude that the iRR format performs clearly better with respect to stakeless, asymmetric and competitive matches, 

while it seems to provoke a noticeable increase in collusive games. 

We now take a closer look at the distribution of the noncompetitive matches over the different time slots for the group stage format (Table 7a) and the iRR format (Table 7b). Recall that for the group stage format, we made the conservative assumption that the four teams from each group play their matches at the same time. Hence, the time slots coincide with the rounds and the number of matches in each time slot is 16. For the iRR format, round 7 consists of 4 time slots, while round 8 consists of a single time slot. As expected, non-competitive matches occur more frequently in later rounds. 

In Table 8, we decompose collusion in the iRR format based on the desired prize of the colluding teams. For example, Table 8 reveals that in 13.34 % of the observed collusion opportunities, a tie would guarantee the top 8 for both teams. Such a decomposition is not necessary for the group stage format, since the only collusion opportunity that is possible in this format is if two teams guarantee finishing in the top two positions by a tie. 

**Table 7:** Overview of each type of match per round/slot in the two formats. 

|||**(a) Overview of e**|**ach type of match match**|**per round/slot in the gro**|**up stage format**||
|---|---|---|---|---|---|---|
|**Round**|**Slot**|**#Matches**|**Stakeless (%)**|**Asymmetric (%)**|**Collusive (%)**|**Competitive (%)**|
|5|1|16|0.91|17.02|0.30|81.77|
|6|1|16|15.79|44.67|0.37|39.17|
|Total|–|96|2.78|10.28|0.11|86.82|
|||**(b) Overv**|**iew of each type of matc**|**h per round/slot in the iRR**|**format**||
|**Round**|**Slot**|**#Matches**|**Stakeless (%)**|**Asymmetric (%)**|**Collusive (%)**|**Competitive (%)**|
|7|1|2|0.06|4.15|0.0|95.79|
|7|2|7|0.16|5.87|0.0|93.97|
|7|3|2|0.60|12.22|0.0|87.18|
|7|4|7|0.80|13.78|0.0|85.42|
|8|1|18|5.55|31.69|1.34|61.42|
|Total|–|144|0.75|5.14|0.17|93.94|



> K. Devriesere et al.: From groups to a single league **— 15** 

**Table 8:** Observed percentage of the simulated seasons with a collusion opportunity occurring. 

|**Collusion type**|**Probability (%)**|
|---|---|
|T8<sup>a</sup>|13.34|
|T24<sup>b</sup>|32.73|
|T8-24<sup>c</sup>|35.21|
|SL<sup>d</sup>|18.72|



aT8, A tie guarantees top 8 for both teams; bT24, A tie guarantees top 24 for both teams;<sup>c</sup> T8-24, A tie guarantees top 8 for one and top 24 for the other team;<sup>d</sup> SL, Small loss. 

Finally, we show the observed probability of a team in a certain rank securing its prize before the last round for the group stage format (Table 9a) and the iRR format (Table 9b). It is straightforward to prove that in the group stage format, no team’s prize can be fixed before the last three rounds. While in the iRR format, it is theoretically possible that a team directly qualifies for the Round of 16 after 5 rounds (e.g. this team wins all its games, while all other games result in a tie), we have never observed this in our simulations. We observe that the strongest and weakest teams are typically able to secure their prize well before the tournament ends. By contrast, the middle-ranked teams are the least likely to know their prize in advance, as they must both be eliminated from the top 8 and guaranteed a place within the top 24. A similar analysis holds for the third strongest team in each group of the group stage format. Note that the numbers are lower in the odd time slots since only 2 instead of 7 games are played here, hence less information can be revealed in these time slots about which teams can be sure of which prizes. Further note that we cannot simply sum these numbers as the identity of the team in a certain position changes over the time slots. 

### **5.2 Effect of the schedule** 

Next, we analyze the effect of the schedule on the occurrence of the different types of matches. For the group stage format, the observed percentage of stakeless, asymmetric, collusive and competitive matches, averaged over the seasons, is shown in Table 10a. The best and worst schedules are indicated in bold. 

From Table 10a, we see that no schedule performs best or worst with respect to all types of non-competitive 

matches. However, if we look at competitive matches, schedule 3114 performs best, while schedule 2113 performs worst. The Friedman’s test reveals that there are significant differences between the schedules, for each type of match ( _p <_ 0.01). Moreover, according to the Nemenyi test, the best and worst schedules for each type of match significantly differ. However, regarding competitive matches, assigning schedules 1321 ( _p_ = 1.0), 1341 ( _p >_ 0.99) or 4112 ( _p >_ 0.98) to all groups does not yield significantly different results compared to randomly assigning a schedule to each group. The results per season can be found in the Appendix, in Tables A.1a-A.2. 

The results for the iRR format can be found in Table 10b. Because schedule 24−25 is only applicable for the season 2024/25, it is excluded from the Friedman’s and Nemenyi test when comparing the different types of schedules. The Friedman’s test reveals that the schedules significantly differ for each type of match ( _p <_ 0.01). Moreover, the Nemenyi test shows that, for each type of match, every pair of schedules differs significantly ( _p <_ 0.01). Table 10b shows that schedule 2, in which matches between teams of similar strength are scheduled in the last matchdays, performs worst. A possible explanation for this result is that with this scheduling strategy, the stronger teams play all their games against weaker teams in the beginning of the competition. As a result, the stronger teams are more likely to already have obtained enough points to secure their prize before the last matchdays. Analogously, weaker teams are more likely to have obtained few points, thus, they are already eliminated before the last matchdays. Table 10b further suggests that the opposite strategy performs best, i.e. scheduling matches between teams of similar strength in the beginning seems to have a positive effect on the number of competitive matches. Notably, the schedule which maximizes television audience yields the second best results. This is encouraging, as it suggests that attractiveness from a commercial as well as from a competitive viewpoint are not conflicting with each other. The results per season can be found in the Appendix. 

Finally, we see that the actual schedule for the season 2024/25 performs quite well for all types of matches. With respect to asymmetric, collusive and competitive matches in the season 2024/25, it even performs best among all types of schedules. This again reinforces the idea that stakeholder objectives and competitiveness need not conflict with each other. 

> **16 —** K. Devriesere et al.: From groups to a single league 

**Table 9:** Observed probability that a team’s prize was secured after a certain time slot in both formats. 

||**(a) Observe**|**d probability tha**|**t a team’s prize**|**was secured afte**|**r a certain time s**|**lot in the group s**|**tage format**||
|---|---|---|---|---|---|---|---|---|
||||||**Round**||||
|**Rank**||**3**|||**4**|||**5**|
|1<br>||0.0<br>|||31.92<br>|||49.46<br>|
|2<br>||0.0<br>|||2.57<br>|||25.17<br>|
|3<br>||0.0<br>|||0.0<br>|||6.44<br>|
|4||0.0|||1.97|||32.29|
||**(b) Obs**|**erved probabilit**|**y that a team’s p**|**rize was secured**<br>**Round**|**after a certain ti**<br>**(Time slot)**|**me slot in the iRR**|**format**||
|**Rank**|**6(1)**|**6(2)**|**6(3)**|**6(4)**|**7(1)**|**7(2)**|**7(3)**|**7(4)**|
|1|0.88|8.07|3.98|17.12|12.41|36.87|10.08|25.93|
|2|0.01|0.47|0.37|2.86|2.87|21.0|8.35|31.98|
|3|0.0|0.01|0.01|0.29|0.46|7.07|3.8|24.99|
|4|0.0|0.0|0.0|0.02|0.05|1.49|1.08|13.84|
|5|0.0|0.0|0.0|0.0|0.0|0.25|0.22|5.31|
|6|0.0|0.0|0.0|0.0|0.0|0.02|0.03|1.37|
|7|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.23|
|8|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.02|
|9|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.01|
|10|0.0|0.0|0.0|0.0|0.0|0.02|0.01|0.10|
|11|0.0|0.0|0.0|0.0|0.0|0.05|0.07|0.49|
|12|0.0|0.0|0.0|0.0|0.0|0.11|0.17|1.40|
|13|0.0|0.0|0.0|0.0|0.0|0.15|0.25|3.10|
|14|0.0|0.0|0.0|0.0|0.0|0.14|0.23|4.89|
|15|0.0|0.0|0.0|0.0|0.0|0.1|0.22|6.19|
|16|0.0|0.0|0.0|0.0|0.0|0.07|0.17|6.57|
|17|0.0|0.0|0.0|0.0|0.0|0.05|0.12|5.98|
|18|0.0|0.0|0.0|0.0|0.0|0.02|0.06|4.62|
|19|0.0|0.0|0.0|0.0|0.0|0.01|0.03|2.78|
|20|0.0|0.0|0.0|0.0|0.0|0.0|0.01|1.32|
|21|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.44|
|22|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.11|
|23|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.02|
|24|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|25|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|26|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.02|
|27|0.0|0.0|0.0|0.0|0.0|0.01|0.01|0.15|
|28|0.0|0.0|0.0|0.0|0.0|0.08|0.1|0.77|
|29|0.0|0.0|0.0|0.0|0.04|0.43|0.31|2.73|
|30|0.0|0.0|0.0|0.0|0.18|1.81|1.1|6.94|
|31|0.0|0.0|0.0|0.01|0.72|5.37|2.76|14.0|
|32|0.0|0.0|0.01|0.07|2.12|12.96|5.42|22.39|
|33|0.0|0.02|0.02|0.43|5.2|24.42|8.26|28.06|
|34|0.0|0.07|0.10|1.96|10.37|36.86|9.85|27.31|
|35|0.02|0.77|0.61|6.35|16.19|45.43|9.10|19.95|
|36|1.02|9.12|4.16|19.31|18.14|38.97|5.53|9.85|



> K. Devriesere et al.: From groups to a single league **— 17** 

**Table 10:** Observed percentage of each type of match for both formats, averaged over the seasons, for each schedule. For each type of match, the best and worst performing schedules are highlighted in bold. 

|**(a) Observed percentage of each type**|**of match in the group stage form**|**at, averaged over the seasons, for**|**each schedule**|
|---|---|---|---|
|**Schedule**<br>**Stakeless (%)**|**Asymmetric (%)**|**Collusive (%)**|**Competitive (%)**|
|Random<br>2.78|10.28|0.11|86.83|
|1231<br>2.55|10.64|**.**|86.67|
|2113<br>2.61|10.70|**.**|**.**|
|1241<br>2.63|10.58|**.**|86.65|
|2114<br>2.52|10.35|0.12|87.00|
|1321<br>3.32|9.76|0.10|86.82|
|3112<br>**.**|9.79|0.11|86.70|
|1341<br>2.44|10.65|**.**|86.83|
|3114<br>2.40|10.22|0.10|**.**|
|1421<br>3.34|9.91|0.10|86.65|
|1431<br>2.40|**.**|**.**|86.72|
|4112<br>3.38|**.**|0.11|86.84|
|4113<br>**.**|10.27|0.10|87.26|
|**(b) Observed percentage of each**|**type of match in the iRR format, f**|**or each schedule, averaged over t**|**he seasons**|
|**(except for sch**|**edule****24−25, which is based sol**|**ely on the 2024/25 season)**||
|**Schedule**<br>**Stakeless (%)**|**Asymmetric (%)**|**Collusive (%)**|**Competitive (%)**|
|0<br>0.75|5.15|0.17|93.93|
|1<br>0.72|5.08|0.16|94.04|
|2<br>**.**|**.**|**.**|**.**|
|3<br>**.**|5.10|0.16|**.**|
|4<br>0.72|5.13|0.16|93.98|
|24−25<br>0.77|**.**|**.**|94.02|



## **6 Conclusions** 

This paper compares the occurrence of different types of non-competitive matches in the former group stage and the newly introduced incomplete round robin format of the UEFA Champions League. Non-competitive matches are identified through a mathematically exact classification, and a simulation study is employed to evaluate the two formats. The findings indicate that, across a range of plausible scheduling scenarios, the iRR format substantially reduces the proportion of stakeless and asymmetric matches. Furthermore, appropriate scheduling strategies can further decrease the prevalence of non-competitive games. In particular, scheduling matches between teams of similar strength at the beginning of the tournament seems to enhance competitiveness. A likely explanation is that such a schedule keeps teams more closely aligned in terms of points before the final rounds. Notably, maximizing competitiveness and optimizing television audiences appear to be mutually compatible objectives. 

Conversely, scheduling late-stage matches between teams of similar strength seems to increase the number of noncompetitive outcomes and is therefore undesirable from a competitiveness perspective. 

Previous research on collusive matches has shown that opportunities for collusion are considerably more prevalent if the final games are not played simultaneously. In such cases, teams playing later gain perfect information about the minimum result required for qualification, making strategic outcomes such as small-loss collusion more likely. Conversely, scheduling all final-round matches at the same time reduces these opportunities but imposes costs in terms of television viewership. A promising direction for future research is to quantify this trade-off by examining how different scheduling configurations for the last round affect both the incidence of match manipulation and the associated commercial implications. 

We conclude that UEFA’s statement that the new format “results in more competitive matches” is grounded in facts. However, when distinguishing non-competitive matches as 

> **18 —** K. Devriesere et al.: From groups to a single league 

stakeless, asymmetric, and collusive, we find that while the number of stakeless and asymmetric matches decreases significantly in the new format, there is a noticeable increase in the probability of collusive matches. Whether this reform constitutes an improvement depends on the trade-off between the various types of non-competitive matches. 

**Acknowledgments:** The computational resources (Stevin Supercomputer Infrastructure) and services used in this work were provided by the VSC (Flemish Supercomputer Center), funded by Ghent University, FWO and the Flemish Government – department EWI. We also wish to thank András Gyimesi and Roel Lambers for fruitful discussions on the Champions League reform and László Csató in particular for his helpful suggestions on the writing of this paper. We also wish to thank two anonymous referees for their constructive feedback, which has significantly improved the quality of this paper. 

##### **Research ethics:** Not applicable. 

##### **Informed consent:** Not applicable. 

**Author contributions:** All authors have accepted responsibility for the entire content of this manuscript and approved its submission. 

**Use of Large Language Models, AI and Machine Learning Tools:** None declared. 

**Conflict of interest:** The authors state no conflict of interest. **Research funding:** The research was supported by the Research Foundation - Flanders under Grant S005521N. **Data availability:** Not applicable. 

## **Appendix** 

### **Results decomposed per season** 

See Tables A.1 and A.6. 

> K. Devriesere et al.: From groups to a single league **— 19** 

**Table A.1:** Non-competitive matches group stage format. 

||**(a) Percentage**|**of games that are**|**stakeless, for each**|**schedule for each**|**season in the grou**|**p stage format**||
|---|---|---|---|---|---|---|---|
|**Schedule**|**2019/20**|**2020/21**|**2021/22**|**2022/23**|**2023/24**|**2024/25**|**Average**|
|Random|2.6|2.88|3.07|2.72|2.61|2.81|2.78|
|1231|2.36|2.72|2.68|2.59|2.37|2.61|2.55|
|2113|2.42|2.81|2.8|2.7|2.34|2.59|2.61|
|1241|2.48|2.72|3.03|2.56|2.35|2.62|2.63|
|2114|2.36|2.59|2.88|2.43|2.27|2.6|2.52|
|1321|3.07|3.34|3.68|3.16|3.36|3.29|3.32|
|3112|**.**|**.**|3.73|**.**|**.**|3.35|**.**|
|1341|2.3|2.56|2.76|2.38|2.14|2.48|2.44|
|3114|2.27|**.**|2.73|**.**|**.**|2.46|2.4|
|1421|3.09|3.35|3.7|3.18|3.39|3.32|3.34|
|1431|**.**|2.58|2.56|2.48|2.13|2.44|2.4|
|4112|3.19|3.39|**.**|3.18|3.4|**.**|3.38|
|4113|2.24|2.54|**.**|2.47|**.**|**.**|**.**|
||**(b) Percentage o**|**f games that are a**|**symmetric, for eac**|**h schedule for eac**|**h season in the gr**|**oup stage format**||
|**Schedule**|**2019/20**|**2020/21**|**2021/22**|**2022/23**|**2023/24**|**2024/25**|**Average**|
|Random|10.3|10.34|10.28|10.27|10.18|10.31|10.28|
|1231|10.66|10.6|10.78|10.53|10.61|10.65|10.64|
|2113|10.72|10.79|10.8|10.56|10.73|10.56|10.7|
|1241|10.44|10.66|10.42|10.61|10.63|**.**|10.58|
|2114|10.3|10.44|10.2|10.36|10.36|10.46|10.35|
|1321|9.85|9.85|**.**|9.83|9.46|9.95|9.76|
|3112|9.8|9.94|9.87|9.98|9.45|**.**|9.79|
|1341|10.55|10.71|10.55|**.**|10.72|10.72|10.65|
|3114|10.15|10.31|10.05|10.23|10.25|10.3|10.22|
|1421|10.03|10.1|9.95|10.08|**.**|9.89|9.91|
|1431|**.**|**.**|**.**|**.**|**.**|10.69|**.**|
|4112|**.**|**.**|9.68|**.**|9.48|9.8|**.**|
|4113|10.26|10.31|10.36|10.16|10.21|10.29|10.27|
||**(c) Percentage**|**of games that are**|**collusive, for each**|**schedule for each**|**season in the grou**|**p stage format**||
|**Schedule**|**2019/20**|**2020/21**|**2021/22**|**2022/23**|**2023/24**|**2024/25**|**Average**|
|Random|0.11|0.11|0.11|0.12|0.11|0.11|0.11|
|1231|0.13|0.13|**.**|**.**|**.**|**.**|**.**|
|2113|**.**|**.**|**.**|**.**|0.14|**.**|**.**|
|1241|0.13|**.**|**.**|**.**|**.**|**.**|**.**|
|2114|0.12|0.12|0.12|0.12|0.14|**.**|0.12|
|1321|0.1|0.11|0.11|0.11|0.11|0.09|0.1|
|3112|0.12|0.11|0.1|0.11|0.1|0.1|0.11|
|1341|0.09|0.1|**.**|**.**|**.**|**.**|**.**|
|3114|0.1|0.1|**.**|0.11|0.09|0.09|0.1|
|1421|0.1|0.1|0.11|0.1|0.1|0.09|0.1|
|1431|**.**|**.**|**.**|**.**|0.09|**.**|**.**|
|4112|0.11|0.1|0.11|0.11|0.11|0.1|0.11|
|4113|0.1|0.1|0.1|0.1|0.1|0.09|0.1|



For each season, the best and worst performing schedules are highlighted in bold. 

> **20 —** K. Devriesere et al.: From groups to a single league 

**Table A.2:** Percentage of games that are competitive, for each schedule for each season in the group stage format. 

|**Schedule**|**2019/20**|**2020/21**|**2021/22**|**2022/23**|**2023/24**|**2024/25**|**Average**|
|---|---|---|---|---|---|---|---|
|Random|86.99|86.67|86.54|86.89|87.09|86.78|86.83|
|1231|86.84|86.55|86.41|86.75|86.88|86.62|86.67|
|2113|**.**|**.**|86.25|**.**|**.**|86.72|**.**|
|1241|86.94|86.49|86.41|86.69|86.87|**.**|86.65|
|2114|87.21|86.84|86.8|87.09|87.23|86.82|87.0|
|1321|86.97|86.71|86.6|86.9|87.07|86.67|86.82|
|3112|86.88|86.48|86.3|86.65|87.03|86.85|86.7|
|1341|87.06|86.63|86.6|86.88|87.06|86.72|86.83|
|3114|**.**|**.**|**.**|**.**|87.56|87.15|**.**|
|1421|86.78|86.45|**.**|86.65|87.09|86.7|86.65|
|1431|86.84|86.48|86.43|86.78|86.99|86.78|86.72|
|4112|87.05|86.79|86.47|86.99|87.02|86.72|86.84|
|4113|87.41|87.05|87.04|87.27|**.**|**.**|87.26|



For each season, the best and worst performing schedules are highlighted in bold. 

**Table A.3:** Non-competitive matches iRR format. 

||**(a) Percent**|**age of games that**|**are stakeless, for e**|**ach schedule for e**|**ach season in the i**|**RR format**||
|---|---|---|---|---|---|---|---|
|**Schedule**|**2019/20**|**2020/21**|**2021/22**|**2022/23**|**2023/24**|**2024/25**|**Average**|
|0|0.71|0.78|0.82|0.7|0.7|0.78|0.75|
|1|0.67|0.75|0.81|0.67|0.68|0.75|0.72|
|2|**.**|**.**|**.**|**.**|**.**|**.**|**.**|
|3|**.**|**.**|**.**|**.**|**.**|**.**|**.**|
|4|0.68|0.73|0.82|0.65|0.7|0.77|0.72|
|24−25|–|–|–|–|–|0.77|0.77|
||**(b) Percenta**|**ge of games that a**|**re asymmetric, for**|**each schedule for**|**each season in the**|**iRR format**||
|**Schedule**|**2019/20**|**2020/21**|**2021/22**|**2022/23**|**2023/24**|**2024/25**|**Average**|
|0|5.02|5.12|5.5|4.97|4.97|5.31|5.15|
|1|**.**|**.**|**.**|**.**|4.91|5.19|5.08|
|2|**.**|**.**|**.**|**.**|**.**|**.**|**.**|
|3|5.02|**.**|5.46|4.93|**.**|5.22|5.10|
|4|5.07|**.**|5.5|4.92|4.95|5.25|5.13|
|2425|–|–|–|–|–|**.**|**.**|
|−<br>|**(c) Percent**|**age of games that**|**are collusive, for e**|**ach schedule for e**|**ach season in the i**|**RR format**||
|**Schedule**|**2019/20**|**2020/21**|**2021/22**|**2022/23**|**2023/24**|**2024/25**|**Average**|
|0|0.16|0.19|0.18|0.16|0.16|0.17|0.17|
|1|**.**|0.17|0.18|0.16|**.**|**.**|0.16|
|2|**.**|**.**|**.**|**.**|**.**|**.**|**.**|
|3|**.**|**.**|**.**|0.16|**.**|0.16|0.16|
|4|0.16|0.17|0.18|**.**|0.16|0.17|0.16|
|24−25|–|–|–|–|–|**.**|**.**|



For each season, the best and worst performing schedules are highlighted in bold. 

> K. Devriesere et al.: From groups to a single league **— 21** 

**Table A.4:** Percentage of games that are competitive, for each schedule for each season in the iRR format. 

|**Schedule**|**2019/20**|**2020/21**|**2021/22**|**2022/23**|**2023/24**|**2024/25**|**Average**|
|---|---|---|---|---|---|---|---|
|0|94.11|93.91|**.**|94.17|94.16|93.74|93.93|
|1|94.2|94.0|93.6|**.**|94.26|93.91|94.04|
|2|**.**|**.**|**.**|**.**|**.**|**.**|**.**|
|3|**.**|**.**|93.63|94.27|**.**|93.94|**.**|
|4|94.1|94.01|**.**|94.27|94.2|93.82|93.98|
|24−25|–|–|–|–|–|**.**|94.02|



For each season, the best and worst performing schedules are highlighted in bold. 

> **22 —** K. Devriesere et al.: From groups to a single league 

**Table A.5:** First part of the clubs and their rating, for each season. A−1 indicates that the club was not present in the simulations of that season. 

|**Club**|**2019/20**|**2020/21**|**2021/22**|**2022/23**|**2023/24**|**2024/25**|
|---|---|---|---|---|---|---|
|Manchester City|2,321|2,242|2,313|2,322|2,399|2,398|
|Real Madrid|2,119|2,204|2,242|2,319|2,273|2,356|
|Paris Saint-Germain|2,172|2,262|2,229|2,210|2,121|2,212|
|Atletico Madrid|2,171|2,181|2,198|2,151|2,146|2,157|
|RB Leipzig|2,115|2,165|2,085|2,081|2,232|2,170|
|Shakhtar Donetsk|2,096|2,049|2,007|1,997|1,991|1,929|
|Bayern Munchen|2,257|2,391|2,377|2,303|2,261|2,215|
|FC Barcelona|2,291|2,229|2,219|2,185|2,198|2,226|
|Inter|2,071|2,173|2,228|2,210|2,241|2,277|
|Borussia Dortmund|2,126|2,137|2,174|2,098|2,153|2,185|
|RB Salzburg|2,104|2,106|2,091|2,083|2,082|1,922|
|Juventus|2,187|2,135|2,159|2,109|−1|2,149|
|Atalanta|2,095|2,158|2,119|−1|2,019|2,157|
|Liverpool FC|2,341|2,232|2,236|2,338|2,216|2,281|
|Chelsea FC|2,170|2,114|2,239|2,191|−1|−1|
|AFC Ajax|2,165|2,059|2,124|2,152|−1|−1|
|SL Benfica|2,102|−1|2,080|2,124|2,158|2,118|
|FC Porto|−1|2,043|2,115|2,136|2,169|−1|
|Arsenal|2,109|−1|−1|2,126|2,203|2,270|
|Sevilla FC|−1|2,150|2,148|2,053|2,021|−1|
|Bayer Leverkusen|2,057|2,098|−1|2,024|−1|2,254|
|Club Brugge KV|1,995|1,991|1,942|1,987|−1|1,983|
|Manchester United|−1|2,138|2,196|−1|2,125|−1|
|SSC Napoli|2,117|−1|−1|2,120|2,189|−1|
|AC Milan|−1|−1|2,131|2,176|2,110|2,065|
|Zenit St. Petersburg|1,969|2,068|2,031|−1|−1|−1|
|PSV Eindhoven|−1|−1|−1|2,053|2,114|2,124|
|Sporting CP|−1|−1|2,024|2,044|−1|2,169|
|Crvena Zvezda|1,938|−1|−1|1,997|1,941|1,952|
|Monaco|−1|−1|2,021|2,059|−1|2,099|
|Dinamo Zagreb|1,990|−1|−1|1,982|−1|1,930|
|Tottenham Hotspur|2,134|−1|−1|2,150|−1|−1|
|Villareal CF|−1|2,024|2,121|−1|−1|−1|
|Real Sociedad|−1|−1|2,045|−1|2,079|−1|
|Olympiakos Piraeus|2,049|2,066|−1|−1|−1|−1|
|Lazio Roma|−1|2,020|−1|−1|2,029|−1|
|BSC Young Boys|−1|−1|2,041|−1|1,989|−1|
|Olympique Marseille|−1|1,971|−1|2,041|−1|−1|
|Celtic FC|−1|−1|−1|2,013|1,999|2,006|
|Lille OSC|1,957|−1|2,041|−1|−1|2,064|
|Dinamo Kiev|−1|1,962|1,995|−1|−1|−1|
|Lokomotiv Moskva|1,967|1,929|−1|−1|−1|−1|



> K. Devriesere et al.: From groups to a single league **— 23** 

**Table A.6:** Second part of the clubs and their rating, for each season. A−1 indicates that the club was not present in the simulations of that season. 

|**Club**|**2019/20**|**2020/21**|**2021/22**|**2022/23**|**2023/24**|**2024/25**|
|---|---|---|---|---|---|---|
|Galatasaray|1,875|−1|−1|−1|1,983|−1|
|FC Kobenhavn|−1|−1|−1|1,887|1,930|−1|
|Feyenoord|−1|−1|−1|−1|2,021|2,067|
|Young Boys|2,016|−1|−1|−1|−1|1,847|
|Newcastle United|−1|−1|−1|−1|2,117|−1|
|Valencia CF|2,093|−1|−1|−1|−1|−1|
|VfL Wolfsburg|−1|−1|2,077|−1|−1|−1|
|Leicester City|−1|−1|2,076|−1|−1|−1|
|Slavia Praha|2,043|−1|−1|−1|−1|−1|
|Eintracht Frankfurt|−1|−1|−1|2,033|−1|−1|
|1. FC Union Berlin|−1|−1|−1|−1|2,033|−1|
|Olympique Lyon|2,032|−1|−1|−1|−1|−1|
|Getafe|2,027|−1|−1|−1|−1|−1|
|Bor. Monchengladbach|−1|2,019|−1|−1|−1|−1|
|Marseille|−1|−1|−1|−1|2,018|−1|
|Viktoria Plzen|−1|−1|−1|2,015|−1|−1|
|Rangers FC|−1|−1|−1|2,014|−1|−1|
|RC Lens|−1|−1|−1|−1|2,013|−1|
|PAOK|−1|2,001|−1|−1|−1|−1|
|Sporting Braga|−1|−1|−1|−1|1,979|−1|
|Stade Rennes|−1|1,977|−1|−1|−1|−1|
|Royal Antwerp FC|−1|−1|−1|−1|1,970|−1|
|KRC Genk|1,933|−1|−1|−1|−1|−1|
|FC Midtjylland|−1|1,925|−1|−1|−1|−1|
|Ferencvarosi TC|−1|1,920|−1|−1|−1|−1|
|FK Krasnodar|−1|1,914|−1|−1|−1|−1|
|Besiktas|−1|−1|1,884|−1|−1|−1|
|Rakow Czestochowa|−1|−1|−1|−1|1,882|−1|
|Molde|−1|1,880|−1|−1|−1|−1|
|Maccabi Haifa|−1|−1|−1|1,879|−1|−1|
|Malmo FF|−1|−1|1,876|−1|−1|−1|
|LASK|1,846|−1|−1|−1|−1|−1|
|Istanbul Basaksehir|−1|1,842|−1|−1|−1|−1|
|Ludogorets|−1|−1|1,814|−1|−1|−1|
|Girona|−1|−1|−1|−1|−1|2,042|
|VfB Stuttgart|−1|−1|−1|−1|−1|2,104|
|Aston Villa|−1|−1|−1|−1|−1|2,112|
|Bologna|−1|−1|−1|−1|−1|2,017|
|FC Sheriff|−1|−1|1,758|−1|−1|−1|
|Sparta Prague|−1|−1|−1|−1|−1|2,077|
|Brest|−1|−1|−1|−1|−1|1,985|
|Sturm Graz|−1|−1|−1|−1|−1|1,915|
|Slovan|−1|−1|−1|−1|−1|1,801|



> **24 —** K. Devriesere et al.: From groups to a single league 

## **References** 

- Adler, I., Erera, A.L., Hochbaum, D.S., and Olinick, E.V. (2002). Baseball, optimization, and the world wide web. _Interfaces_ 32: 12−22,. 

- Bernholt, T., Gülich, A., Hofmeister, T., and Schmitt, N. (1999). Football elimination is hard to decide under the 3-point-rule. In: _International symposium on mathematical foundations of computer science_ . Springer, Berlin, Heidelberg, pp. 410−418. 

- Buraimo, B., Forrest, D., McHale, I.G., and Tena, J.D. (2022). Armchair fans: modelling audience size for televised football matches. _Eur. J. Oper. Res._ 298: 644−655,. 

- Caruso, R. (2009). The basic economics of match fixing in sport tournaments. _Econ. Anal. Pol._ 39: 355−377,. 

- Chater, M., Arrondel, L., Gayant, J.P., and Laslier, J.F. (2021). Fixing match-fixing: optimal schedules to promote competitiveness. _Eur. J. Oper. Res._ 294: 673−683,. 

- Christensen, J., Knudsen, A.N., and Larsen, K.S. (2015). Soccer is harder than football. _Int. J. Found. Comput. Sci._ 26: 477−486,. 

- Constantinou, A.C. and Fenton, N.E. (2012). Solving the problem of 

   - inadequate scoring rules for assessing probabilistic football forecast models. _J. Quant. Anal. Sports_ 8, https://doi.org/10.1515/ 1559-0410.1418. 

- Corona, F., de Tena Horrillo, J.D., and Wiper, M.P. (2017). On the importance of the probabilistic model in identifying the most 

   - decisive games in a tournament. _J. Quant. Anal. Sports_ 13: 11−23,. 

- Corona, F., Forrest, D., Tena, J.D., and Wiper, M. (2019). Bayesian forecasting of UEFA Champions League under alternative seeding regimes. _Int. J. Forecast._ 35: 722−732,. 

- Courty, P. and Cisyk, J. (2024). Sports injuries and game stakes: concussions in the National Football League. _Econ. Inq._ 62: 430−448,. 

- Cox, A. (2018). Spectator demand, uncertainty of results, and public interest: evidence from the English Premier League. _J. Sports Econ._ 19: 3−30,. 

- Csató, L. (2022a). Quantifying incentive (in)compatibility: a case study from sports. _Eur. J. Oper. Res._ 302: 717−726,. 

Csató, L. (2022b). UEFA against the champions? An evaluation of the recent reform of the Champions League qualification. _J. Sports Econ._ 23: 991−1016,. 

- Csató, L. (2023). How to avoid uncompetitive games? The importance of tie-breaking rules. _Eur. J. Oper. Res._ 307: 1260−1269,. 

Csató, L. (2025a). A hidden benefit of incomplete round-robin tournaments: encouraging offensive play, _Manuscript_ . https://arxiv .org/abs/2509.13141. 

- Csató, L. (2025b). On head-to-head results as tie-breaker and consequent 

opportunities for collusion. _IMA J. Manag. Math._ 36: 215−230,. 

- Csató, L. and Gyimesi, A. (2026a). Increasing competitiveness by 

imbalanced groups: the example of the 48-team FIFA World Cup. _Eur. J. Oper. Res._ , In press. https://www.sciencedirect.com/science/ article/pii/S037722172500935X. 

- Csató, L. and Gyimesi, A. (2026b). A probabilistic match classification model for sports tournaments, _Manuscript_ . https://arxiv.org/abs/ 2601.09673. 

- Csató, L. and Ilyin, S. (2025). Misaligned incentives in sports: a mathematical analysis of the post-2024 UEFA Champions League qualification. _IMA J. Manag. Math._ 36: 579−591,. 

- Csató, L., Molontay, R., and Pintér, J. (2024). Tournament schedules and incentives in a double round-robin tournament with four teams. _Int. Trans. Oper. Res._ 31: 1486−1514,. 

- Csató, L., Gyimesi, A., Goossens, D., Devriesere, K., Lambers, R., and Spieksma, F. (2025). How to measure the uncertainty of a tournament draw: the case of European football’s Champions League, _Manuscript_ . https://arxiv.org/abs/ 2507.15320. 

- Csató, L., Devriesere, K., Goossens, D., Gyimesi, A., Lambers, R., and Spieksma, F. (2026). Ranking matters: does the new format select the best teams for the knockout phase in the UEFA Champions League? _Int. J. Sports Sci. Coach._ , In press. https://doi.org/10.1177/ 17479541251405330. 

- Dagaev, D. and Rudyak, V. (2019). Seeding the UEFA Champions League participants: evaluation of the reform. _J. Quant. Anal. Sports_ 15: 129−140,. 

- Devriesere, K. and Goossens, D. (2025). Redesigning Belgian youth field hockey competitions using an incomplete round-robin tournament. _INFORMS J. Appl. Anal._ 55: 437−505,. 

- Devriesere, K., Csató, L., and Goossens, D. (2025). Tournament design: a review from an operational research perspective. _Eur. J. Oper. Res._ 324: 1−21,. 

- Devriesere, K., Goossens, D., and Willem, A. (2026). Manipulation unraveled: a new framework to analyze the impact of tournament design on manipulation opportunities. _Int. J. Sports Sci. Coach._ 21: 638−652,. 

- Duggan, M. and Levitt, S.D. (2002). Winning isn’t everything: corruption in sumo wrestling. _Am. Econ. Rev._ 92: 1594−1605,. 

- Elaad, G., Krumer, A., and Kantor, J. (2018). Corruption and sensitive soccer games: cross-country evidence. _J. Law Econ. Organ._ 34: 364−394,. 

- Feddersen, A., Humphreys, B.R., and Soebbing, B.P. (2023). Contest incentives, team effort, and betting market outcomes in European football. _Eur. Sport Manag. Q._ 23: 605−621,. 

- Football Rankings (2020). Simulation of scheduled football matches. 28 December. http://www.football-rankings.info/2020/12/simulationof-scheduledfootball-matches.html. 

- Forrest, D. and Simmons, R. (2002). Outcome uncertainty and attendance demand in sport: the case of English soccer. _J. R. Stat. Soc. - Ser. D: Statistician_ 51: 229−241,. 

- García, J. and Rodríguez, P. (2002). The determinants of football match attendance revisited: empirical evidence from the Spanish football league. _J. Sports Econ._ 3: 18−38,. 

- Geenens, G. (2014). On the decisiveness of a game in a tournament. _Eur. J. Oper. Res._ 232: 156−168,. 

- Goller, D. and Heiniger, S. (2024). A general framework to quantify the event importance in multi-event contests. _Ann. Oper. Res._ 341: 71−93,. 

- Goossens, D., Beliën, J., and Spieksma, F.C.R. (2012). Comparing league formats with respect to match importance in Belgian football. _Ann. Oper. Res._ 194: 223−240,. 

- Gotzes, U. and Hoppmann, K. (2022). Bounding the final rank during a round robin tournament with integer programming. _Oper. Res._ 22: 123−131,. 

- Groll, A., Ley, C., Schauberger, G., and Van Eetvelde, H. (2019). A hybrid random forest to predict soccer matches in international tournaments. _J. Quant. Anal. Sports_ 15: 271−287,. 

- Guajardo, M. and Krumer, A. (2024). Tournament design for a FIFA World Cup with 12 four-team groups: every win matters. In: Breuer, M., and Forrest, D. (Eds.). _The palgrave handbook on the economics of manipulation in sport’_ . Palgrave Macmillan, Cham, Switzerland, pp. 207−230. 

> K. Devriesere et al.: From groups to a single league **— 25** 

- Gusfield and Martel (2002). The structure and complexity of sports elimination numbers. _Algorithmica_ 32: 73−86,. 

- Guyon, J. (2020). Risk of collusion: will groups of 3 ruin the FIFA world cup? _J. Sports Anal._ 6: 259−279,. 

- Guyon, G. (2021). Champions League group stage draw: who are the most likely opponents of Manchester City, Manchester United, Liverpool and Chelsea? 26 August. https://www.fourfourtwo.com/ us/features/champions-league-groupstage-draw-who-are-themost-likely-opponents-of-city-united-liverpooland-chelsea. 

- Guyon, J., Meunier, F., Ben Salem, A., Buchholtzer, T., and Tanré, M. (2025). Drawing and scheduling the UEFA Champions League league phase. https://ssrn.com/abstract=5413142. 

- Gyimesi, A. (2024). Competitive balance in the post-2024 Champions League and the European Super League: a simulation study. _J. Sports Econ._ 25: 707−734,. 

- Hoffman, A. and Rivlin, T.J. (1970). When is a team “mathematically” eliminated. In: _Proceedings of the Princeton symposium on mathematical programming’_ . Princeton University Press, Princeton, NJ, pp. 391−401. 

- Hubáček, O., Šourek, G., and Železn`y, F. (2022). Forty years of score-based soccer match outcome prediction: an experimental review. _IMA J. Manag. Math._ 33: 1−18,. 

- Husted, M.A., Olinick, E.V., and Newman, A.M. (2021). Improving sports media’s crystal ball for National Basketball Association playoff elimination. _INFORMS J. Appl. Anal._ 51: 119−135,. 

- Jetter, M. and Walker, J.K. (2017). Good girl, bad boy? Evidence consistent with collusion in professional tennis. _South. Econ. J._ 84: 155−180,. 

- Ley, C., Wiele, T.V.D., and Eetvelde, H.V. (2019). Ranking soccer teams on the basis of their current strength: a comparison of maximum likelihood approaches. _Stat. Model._ 19: 55−73,. 

- Li, M., Van Bulck, D., and Goossens, D. (2025). Beyond leagues: a single incomplete round robin tournament for multi-league sports timetabling. _Eur. J. Oper. Res._ 323: 208−223,. 

- Losak, J.M. and Halpin, S.A. (2024). Does every game matter? A new perspective on the league standing effect in Major League Baseball. _Sports Econ. Rev._ 5: 100028,. 

- Maher, M. (1982). Modelling association football scores. _Stat. Neerl._ 36: 109−118,. 

- McCormick, S.T. (1996). Fast algorithms for parametric scheduling come from extensions to parametric maximum flow. In: _Proceedings of the twenty-eighth annual ACM symposium on theory of computing_ , pp. 319−328. 

- Melkonian, V. (2024). An integer programming approach for scheduling a professional sports league. _Am. J. Comput. Math._ 14: 401−423,. 

- Page, L. and Page, K. (2009). Stakes and motivation in tournaments: playing when there is nothing to play for but pride. _Econ. Anal. Pol._ 39: 455−464,. 

- Pawlowski, T. and Nalbantis, G. (2015). Competition format, championship uncertainty and stadium attendance in European football − a small league perspective. _Appl. Econ._ 47: 4128−4139,. 

- Pérez Carcedo, L., Puente Robles, V., and Rodríguez Guerrero, P. (n.d.). Factors determining TV soccer viewing: does uncertainty of outcome really matter? _Int. J. Sport Finance_ 12: 124−139,. 

- Raack, C., Raymond, A., Schlechte, T., and Werner, A. (2014). Standings in sports competitions using integer programming. _J. Quant. Anal. Sports_ 10: 131−137,. 

- Rennó-Costa, C. (2023). A double-elimination format for a 48-team FIFA World Cup, Manuscript. https://arxiv.org/abs/2301.03411. 

- Ribeiro, C.C. and Urrutia, S. (2005). An application of integer 

   - programming to playoff elimination in football championships. _Int. Trans. Oper. Res._ 12: 375−386,. 

- Robinson, L.W. (1991). Baseball playoff eliminations: an application of linear programming. _Oper. Res. Lett._ 10: 67−74,. 

- Rottenberg, S. (1956). The baseball players’ labor market. _J. Polit. Econ._ 64: 242−258,. 

- Sauer, P., Cseh, Á., and Lenzner, P. (2024). Improving ranking quality and fairness in Swiss-system chess tournaments. _J. Quant. Anal. Sports_ 20: 127−146,. 

- Scarf, P., Yusof, M.M., and Bilbao, M. (2009). A numerical study of designs for sporting contests. _Eur. J. Oper. Res._ 198: 190−198,. 

- Schilling, M.F. (1994). The importance of a game. _Math. Mag._ 67: 282−288,. 

- Schlotter, I. and Cechlárová, K. (2018). A connection between sports and matroids: how many teams can we beat? _Algorithmica_ 80: 258−278,. 

- Schreyer, D., Schmidt, S.L., and Torgler, B. (2018). Game outcome uncertainty in the English Premier League: do German fans care? _J. Sports Econ._ 19: 625−644,. 

- Schwartz, B.L. (1966). Possible winners in partially completed 

   - tournaments. _SIAM Review_ 8: 302−308,. 

- Stronka, W. (2024). Demonstration of the collusion risk mitigation effect of random tie-breaking and dynamic scheduling. _Sports Econ. Rev._ 5: 100025,. 

- Szymanski, S. (2003). The economic design of sporting contests. _J. Econ. Lit._ 41: 1137−1187,. 

- UEFA (2023). UEFA Champions League group stage draw, 31 Augustus. https://www.uefa.com/uefachampionsleague/draws/2024/ 2001775/. 

- UEFA (2024a). New format for Champions League post-2024: Everything you need to know. 12 June. https://www.uefa.com/ uefachampionsleague/news/0268-12157d69ce2d-9f011c70f6fa- 

   - 1000−new-format-for-champions-league-post-2024-everythingyou-ne/. 

- UEFA (2024b). Regulations of the UEFA Champions League - Competition System. 2 September. https://documents.uefa.com/r/Regulationsof-the-UEFA-Champions-League-2024/25/II-Competition-SystemOnline. 

- UEFA (2024c). UEFA Champions League: League phase draw. 29 August. https://www.uefa.com/uefachampionsleague/draws/. 

- Vanwersch, L., Vandercruysse, L., Vermeersch, A., Vander Beken, T., Willem, A., Constandt, B., and Hardyns, W. (2025). The grayness of match-fixing: a study of the prevalence and sanctionability of non-betting-related match-fixing in football and tennis. _Deviant Behav._ 46: 709−730,. 

- Villar, J.G., and Guerrero, P.R. (2009). Sports attendance: a survey of the literature 1973-2007. _Rivista di Diritto e di Economia dello Sport_ 5: 112−151. 

- Wayne, K.D. (2001). A new property and a faster algorithm for baseball elimination. _SIAM J. Discrete Math._ 14: 223−229,. 

- Winkelmann, D., Michels, R., and Deutscher, C. (2025). Predicting 

   - qualification thresholds in UEFA’s incomplete round-robin tournaments, _Manuscript_ . https://arxiv.org/abs/2508.20075. 


