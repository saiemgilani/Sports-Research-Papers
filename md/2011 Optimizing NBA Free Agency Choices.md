<!-- source: 2011 Optimizing NBA Free Agency Choices.pdf -->

MIT  Sloan  Sports  Analytics  Conference  2011 March  4-­‐5,  2011,  Boston,  MA,  USA 



# **Optim���������������������������������������������������� Multiple-Choice Knapsack Model** 

Sam Kirshner ������������������ Kingston, ON, Canada, K7L 3N6 Email: skirshner@business.queensu.ca 

## **Abstract** 

���������������������������������������������������������������������������������������������for which the available free agents comprise the items that can be placed into the knapsack, �������������������������� corresponds to the size of the knapsack.  The salary cap presents teams with the problem of how to maximize the value of a fixed expenditure in a dynamic market. As free agents are signed, the talent pool ��������������������������������������������������������������������������������������������������������������� the amount required to sign a given player also decreases. Thus, teams are faced with the dilemma of when to offer a contract and how much money to offer.  The optimal strategy for solving this problem must consider the trade-off between losing a player to a competitor and acquiring the player at a price that preserves as much cap space as possible for additional players.  This trade-off can be solved by a dynamic program based on the multiple-choice knapsack problem, which optimizes the benefit of signing a player at any particular point in the free agency period in comparison to the opportunity costs of the cap space required to do so. 

## **1  Introduction** 

Professional sports provide a unique setting to test labor market theories because of the extensive available data regarding salaries, worker-employer relationships, and detailed work performance statistics.  Economists have used sports to test various theories on subjects such as monopsony [1, 2], bargaining power [3], the structure of salaries [4] and the impact of supervision and incentives [5].  Sport labor markets can also be used to assess how the availability of ��������������������������������������������������������������������������������������������������������������������� 

��������������������������������������������������������������, in particular, offers an interesting setting since much of the information pertaining to the market valuation of the employees and the available resources of the employers are known to all participants.  At the end of every NBA season there are a number of established players with expiring contracts who become unrestricted free agents.  These players have the right to sign a new contract with any team interested in acquiring their services.  The NBA has a salary cap restricting the total amount that the teams can spend on salaries.  All participants know the amount of money each team has available to sign free agents, because the details of the existing contracts are published.  Although the NBA does not use a hard salary cap since teams can raise their salary ceilings by taking advantage of the salary cap exceptions, the amount of additional cap space available to each team can be treated as part of the total available salary cap [6].  There is also consensus information available on the market valuation of free agents based on the extensive amount of data related to their skills sets.  Unlike the salary cap, the exact valuation that each team places on these players is not publicly known.  Generally, teams have relatively good information on how many teams may be interested in acquiring specific players based on how well �������������skill sets match the needs of teams with cap space.  Furthermore, players often signal how many teams are interested in their services at the start of free agency since it is in their interest to generate multiple offers. 

MIT  Sloan  Sports  Analytics  Conference  2011 March  4-­‐5,  2011,  Boston,  MA,  USA 



Teams approach free agency with a variety of strategies.  Often several teams will target the same players and engage in a competitive auction in an attempt to sign these free agents.  Some teams use a pre-emptive strategy to offer a contract towards the high end of ������������������������������������������������������������������������������������. Once a team offers a contract, the player must either accept or reject it.  If he rejects the offer, then there is a strong probability that the team will offer a contract to an alternative choice.  Other teams use a wait-and-see approach to gauge how many teams are interested in a player before bidding on their services, especially if they have limited cap space compared to the other teams that they are likely to be competing against.  Finally, teams may delay signing players until the final stages of the off season in order to sign those who represent relatively good value.  It is unclear which strategic approach is optimal.  On the one hand, as free agents are signed th���������������������������������������������������������� on the other hand, as the amount of available money in the market decreases the amount required to sign a given player also decreases, since ���������������������������������������������������������e of the teams that are interested in signing them.  The optimal strategy for deciding on when to offer a contract must consider the trade-off between losing the player to a competitor and acquiring the player at a cheaper price to preserve cap space to sign additional players. 

Although the above trade-off should be the primary determinant of acquiring free agents, it is unclear which criteria general managers (GMs) of NBA teams should use in deciding when and how much to offer players in the free agency period.  The question is far from trivial in view of the following: NBA players are the highest paid professional athletes as a group with the average contract in the 2010 season amounting to $5.854 million [6, 7], ���������������������� is directly related to how successful the team is in a given season, and the strategic signing of free agents is the primary means whereby a team can improve their performance from year to year. 

## **2  Overview of the Problem** 

Free agency is often viewed as an independent private value auction problem, since the teams have independent assessment ����������������talents from a distribution that is common knowledge [8].  Although the GMs have common information re������������������������������� and statistics, the precise valuation that GMs place on a free agent will ������������������������������������������������������������������������������������������������������.  Free agents do not have access to this private information, and therefore, they must auction off their services.  If more than one GM ��������������������������������������������������������������������������������������������������������������������� presumption that the player will sign with the team that bids the highest. 

There are two unique aspects to the NBA free agency problem which differentiate it from the competitive auction models.  The first is the extent of the common information available to all participants.  The availability of this information affects both the GMs' strategies on when and how much to offer players and the players' strategies regarding which contract offers to accept and reject.  All participants are aware of the amount of salary cap space available to each team.  There are also five distinct positions on a team, and there are relatively good assessments by pundits on the skill sets required by each team based on the number and performance of the incumbent players.  There are also detailed performance statistics available on each player, which helps to establish a benchmark for how a free agent may be valued at the start of the free agency period.  Therefore, both teams and players have relatively good information regarding the amount of interest in each free agent and their value in the marketplace.  The analogous situation in terms of auctions would be an ascending auction where a bidder has knowledge on which items the other participants in the game will bid on and the amount of money they have available to make these bids.  Although bidders do not know the valuation assigned to each item by the competing bidders, they are aware of the maximum amount of money each participant can bid.  This amount of common information has a significant impact on the strategies of both GMs and players and makes the free agency problem distinct from competitive auction problems. 

The second unique factor of the free agency market is that teams and players are competing with one another and each contract decision changes the state of free agency.  Given the constraint of a salary cap, players are essentially competing with one another to maximize their share of a common pie.  Thus, their reserve value at the start of the free agency period represents the relative demand for their services compared to the other free agents given the amount of available salary cap.  As players are signed and the salary cap shrinks, generally, players expected salaries will fall. 

2 

MIT  Sloan  Sports  Analytics  Conference  2011 March  4-­‐5,  2011,  Boston,  MA,  USA 



However, it is possible, especially during the early stages of the free agency, that this value could rise, ���������������������� set is in high demand and there are fewer players available with these skills.  This explains why players may reject contract offers below what they perceive to be their relative value in the marketplace even though the amount of the available pie may subsequently shrink.  However, as the available salary cap continues to shrink, it will ultimately become the predominant influence on their reserve wage irrespective of how their skills are valued relative to the remaining free agents.  Likewise, the salary cap presents teams with the dilemma of how to maximize the value of this fixed expenditure relative to the other NBA teams that they compete against.  Optimizing the performance of the team is then not necessarily accomplished by winning a competitive auction if the remaining salary cap shrinks relative to the value of the remaining players.  ��������������������������������������������������������������������������������������������������� ����������������������������������������������free agents is sufficiently high that the value of the remaining players will shrink relative to the remaining salary cap.  Teams may also be motivated to make relatively high pre-emptive bids to players who may be more in demand once the marquee players pursued by multiple teams are signed to contacts in anticipation that their market value will rise.  Therefore, unlike auction theory where participants are trying to maximize profit or surplus in an absolute sense, the GMs and players are trying to improve their position relative to their competitors.  Thus, the strategies of both GMs and players will be fundamentally different than the strategies of buyers and sellers in auctions. 

Given that teams are constrained by the salary cap, the GMs face a competitive resource allocation problem which is best modelled by a 0-1 knapsack problem.  A 0-1 knapsack problem is a combinational optimization problem where items with various weights and benefits are selected to fill a weight constrained knapsack.  The objective of the problem is to maximize the value of the knapsack by selecting the most valuable items such that the sum of the items �������������������������������������������������.  ���������������������������������������������������������������������ts ��������������������������������������������������������������������������������. 

The knapsack problem confronting GMs is complicated by three factors.  First, although each team covets a unique combination of skills, better players� skill sets will likely encompass increased combinations and will be desired by more teams.  Second, the cost of each player������������������ is constantly changing over time, since a ������������������� function of the remaining cap space of the teams interested in signing him.  Third, the teams participating in the competition for a given player can change with each new signing.  Consequently, GMs face a multidimensional multiplechoice knapsack problem.  They have to determine whether to sign individual players they value highly immediately or to wait in the hope that they can improve the overall value of their knapsack by acquiring the player they value at reduced wages preserving salary to sign additional players. 

Independent work by Gibson et al. [9] uses a knapsack approach for modeling sport league drafts.  They consider a similar knapsack problem with sequential selection.  In their knapsack game, at time � a GM has to pick a player based on the available pool of players.  The stochastic nature of the draft is that the GM has to make a decision on which player to draft with incomplete knowledge of which players will be selected and which players will be available at future decision points.  Gibson et al. develop several algorithms to help solve the GMs problem.  The crucial difference between the draft model and the free agency model presented in this paper is that GMs do not make their decision sequentially without competition.  Thus the decision making process of the knapsack problem associated with free agency is more dynamic and difficult to model than the one associated with the draft.  This helps to explain why the outcomes associated with free agency are nearly impossible to predict while the draft can be predicted with a high degree of accuracy by pundits. 

## **3  Modeling Free Agency** 

Under the assumption that the revenue earned by a franchise is entirely related to success of its basketball team, the objective of GMs in free agency is to add players that will give their team the greatest chance of winning.  A model of free agency can be described by a game with three stages.  The first stage of the game occurs before GMs are allowed to start signing free agents.  In this stage, each team evaluates the available players and makes a list of the free agents they would be interested in pursuing.  The second stage is the free agency period indexed by �����������, where the 

3 

MIT  Sloan  Sports  Analytics  Conference  2011 March  4-­‐5,  2011,  Boston,  MA,  USA 



free agents can be signed by a team with available salary.  Using the expected wages of the players and the knowledge of the other teams, GMs decide whether they want to offer a contract to a targeted player from their list or whether they should wait.  The period ends when a player is signed to a contract, because both teams and players must update their strategies to account for changes in the market related to the amount of available money and the relative value of the remaining players.  The final stage of the game is at time��, where all remaining free agents exit the market receiving a wage ��.  The wage �� corresponds to the salary of playing in the development league or overseas. 

### **3.1  Free Agents** 

At the start of free agency there are � players who are not under contract with any team, but would be hired by at least one team for an amount equal to or greater than the league minimum wage ����.  Each player ��������� can be uniquely described by a vector � of � attributes.  The value ����, which is player �����������������������ent of attribute ��������� is based on past performance.  The availability of any player � at time � can be expressed by the binary vector ���� which equals 1 at index � if player � has yet to be signed by a team and � if the player is off the market. 

### **3.2  Teams** 

At the start of the free agency period there are � teams with cap space.  Each team ��������� has a specific amount of cap space determined by how many players are currently under contract with the team and the league's salary cap. The remaining salary space that team � has under the cap at time � is given by the �<sup>��</sup> element of vector ����.  Any team � with sufficient salary space to sign any player at time ��belongs to the set�����.  To identify potential players to pursue at each time �, each team � places a weight ������ on each attribute ���������.  Thus, the value of each player � to team � during period ��is given by ������, where 



The value of a player can change over time as a result of trades and other free agents signing.  Although team � does not have full information on how other teams value each player �, the knowledge of rosters and players provides GMs with some insight regarding the other teams' needs.  Using ������������������������������������������������������ teams rosters and cap space, GMs can estimate an expected minimum wage ������� that player � will be offered if more than one team is interested in his services. 

Using the values of ������� each team makes a list ����� of the available players that they may be interested in signing.  A GM can surmise the probability that team � will sign player ��at time �, ������������������ by considering each ������������������������������������������players� expected wages ��������.  Due to the presence of the league minimum wage, ���� (where ���� ���) a player � will only be on team �'s list ����� if ������� �����.  At the start of time � each team ������ updates their list ����� so that only the available players given by �������������� ����� remain on the list.  If a player is only on one team�s list, then the team will only offer the player ����� since there are no other ������������������������������������������������������.  However, a player may refuse ���� if he believes that his market value may improve as free agency progresses.  If there are two or more teams interested in a player, then to contract a player � the GM of team �� will have to offer a wage 



Therefore, at anytime ����������� the GM of team � is trying to solve the knapsack problem: 

4 

MIT  Sloan  Sports  Analytics  Conference  2011 March  4-­‐5,  2011,  Boston,  MA,  USA 





where ������ equals 1 if player � is contracted to the team at wage ������ during time � and � otherwise.  Treating free agency as a knapsack problem implicitly assumes that teams will spend all of their available cap space on players who are free agents.  This assumption is consistent with what typically occurs in practice, although it is not absolute and may fluctuate from year to year. 

Although the knapsack problem is relatively straightforward, the dynamic nature of wages complicates the problem.  As free agents are signed there are two conflicting forces affecting the ������������������������.  If the relative benefit of a player increases as free agents are signed, then ������������������������������������������������������������ ��������������������������������������������������.  On the other hand, as the amount of available money in the market ���������������������������������������s decrease.  Thus, the strategy for deciding on when to offer a contract must consider the trade-offs between losing the player to a competitor and acquiring the player at a lower price to preserve cap space to sign additional players, as well as being forced into offering higher than anticipated contracts because of a limited pool of desirable players. 

If the set �<sup>�</sup> ��� represents the set of available players at a certain position, �, and �<sup>�</sup> ��� is the set of teams with cap space interested in acquiring a player at the position at time �, then signing player ����<sup>�</sup> ��� will be valuable if ����<sup>�</sup> ��� ������ ����<sup>�</sup> ����� ������ � � ����<sup>�</sup> ��� ����� ����<sup>�</sup> ����� ������� 

The ratio considers the tradeoff �������������������������������������������������ture ability to use cap space, providing reasonable criterion for offering contracts to targeted players.  The value of the signing relative to the opportunity cost of the utilized cap space also increases with the difference between the two ratios.  If the team is trying to fill several positions and there is a high probability that the team can optimize the value of the remaining cap space, then the team will place a premium on acquisitions which maximize value.  If teams are playoff or championship contenders and believe they only need to add one player, then the team will place less emphasis on their opportunity costs to acquire additional players. 

### **3.3  Optimal Solution and Control Strategy** 

The strategic ��������������������offer player � a contract at wage ������ ���������������������������������������������� periods and obtain more players at lower costs.  Therefore, at any period � the knapsack problem for the GM of team �� can be solved using the dynamic program: 



where �� is a column vector of length � that is all zeros except for the �<sup>��</sup> component which has a value of �, �� is a column vector of length � that is all zeros except for the �<sup>��</sup> element which has a value of �, and 



The boundary conditions for the dynamic program are as follows: 





The dynamic program has the assumption that only one player can be signed in any given time period, which is fairly 

consistent with what occurs in practice.  As a result the player that offers the greatest value to team �� is player �<sup>�</sup> defined by 



5 

MIT  Sloan  Sports  Analytics  Conference  2011 March  4-­‐5,  2011,  Boston,  MA,  USA 



An examination of the dynamic program reveals that the �����control policy should have the threshold form: 

> <sup>����������������������</sup> �� ���� ��<sup>������</sup> ������������������������������������������������������������������������������������������������������������������������������������������������<sup>�������������������������������������������������</sup> 

The policy implies that a GM should offer a contract to player ��if the value of the player added to the team is greater than the opportunity cost of the cap space being utilized by the player.  Although the state-space of the dynamic problem will scale exponentially with the addition of each player to the model, in reality teams are generally interested in a small group of players who are considered to be a good match for their teams and can scale the model down accordingly.  In situations where the model is more computationally complex due to a large number of players under consideration, there is a rich literature of algorithms and heuristics that can be applied to the knapsack formulation of the free agency problem to give approximate solutions [10, 11, 12, 13, 14]. 

## **4  Conclusion** 

Modeling free agency as a multidimensional multiple-choice knapsack problem explains the motivations behind most free agent signings and incorporates the various phenomena related to the dynamics of player wages.  For example, due to the limit on the maximum salary that teams can offer, the value of marquee free agents for most teams will exceed the opportunity costs of the cap space required to sign them.  Consequently, these players will receive multiple offers of similar value, and their choice on which team to sign with will be based on their personal preferences. After the top marquee free agents are signed, teams revalue the remaining free agents based on the uniqueness of their skill sets and the available cap space of the teams who require these skills.  Most economic models of employment and contracts include a rationality constraint preventing wages from surpassing the value added by the worker.  However, NBA contracts often exceed the (players� and pundits�) predicted salaries relative to the value added by the player, because GMs are only concerned with maximizing the talent of their team subject to the sole constraint of the salary cap.  GMs who are purely myopic will solve the knapsack problem at each time � by offering contracts to the top targeted players that they can sign given sufficient cap space.  Strategic GMs will use information to predict how a potential signing of player � at time � will impact their opportunity costs to add value to their team as free agency progresses.  Typically, free agents are signed in clusters throughout the duration of the free agency period.  This is consistent with the model since the signing of one free agent will inevitably change the dynamics of the market conditions for both teams and players.  A signing may give greater incentive for a team to contract a player when they lacked sufficient strategic motivation to do so in prior stages of the free agency period.  Thus, the model would assume that each signing would trigger a number of strategic responses by reducing the degree of uncertainty related to the number of available roster spots, salary cap, and opportunity costs associated with the remaining players. 

The properties of the multidimensional multiple-choice knapsack problem presented in this paper seem to adequately ������������������������������������������������������������������������������������������������������� contracts. The extensive availability of common information associated with this market combined with the competitive dynamics between the participants gives rise to a strategic problem, which can be solved by a dynamic program. Future research on this problem should focus on heuristic approaches to solving the dynamic program and exploring whether aspects of this model can be applied to other labor markets with similar features. 

## **5  References** 

[1] S.  Rottenberg, ������������������������������������� Journal of Political Economy, 64, 242-258, 1956. 

[2] Gerald W.  ���������Pay and performance in major league baseball���American Economic Review,Vol.  64(6), pp. 915-930, 1974. 

[3] Lawrence M.  Kahn, �Free Agency, Long-term Contracts and Compensation in Major League Baseball: Estimates ����������������� The Review of Economics and Statistics, 75(1), pp.  157-64, 1993. 

6 

MIT  Sloan  Sports  Analytics  Conference  2011 March  4-­‐5,  2011,  Boston,  MA,  USA 



[4] D.  G.  Richards and R.  C.  Guell��������������������������������������������������� Applied Economics Letters, 5, pp.  291-6, 1998. 

[5] Lawrence M.  Kahn, ������������������������� ��������������������������������������������������������� Perspectives, 14 (3), pp.  75-94, 2000. 

[6] Larry Coon, NBA salary cap FAQ, 2010, retrieved January 2011, from http://www.cbafaq.com. 

��������������������������������������������������������������������������������������������������������������������������� January 2011 from http://www.businessinsider.com/average-major-league-salary-tops-3-million-for-the-first-time-201012. 

[8] K.  T.  Talluri and G.  J.  Van Ryzin������������� Chapter 6 in the Theory and Practice of Revenue Management, Norwall, MA: Kluwer Academic Publishers, pp.  241 -297, 2004. 

[9] Matthew R.  Gibson et al., ���������-based stochastic ruler approach for a stochastic knapsack problem with sequential competition�� Computers and Operations Research, 37 (3) pp.  598-609, 2010. 

[10������������������������������������������-1 knapsack ������������������������������������������������������� Research, 155 (1) pp. 1-21, 2004. 

[11�������������������������������������������������������������������������������������������������������������� and Network Economics 5385, pp. 566-576, 2008. 

[12] Md ����������������������������������������������������������-choice multi-����������������������������� Proceedings of the International Conference on Computational Science-Part II, p.659-668, May 28-30, 2001. 

[13�������������������Heuristic algorithms for the multiple-choice multidimensional knapsack problem������������������ Operational Research Society 55, pp. 1323-1332, 2004. 

[14] Hans Kellerer et al., Knapsack Problems, Springer, Berlin, Germany, 2004. 

7 


