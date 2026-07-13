<!-- source: 2017 PageRank Model for Player Performance Assessment.pdf -->



# **A PageRank Model for Player Performance Assessment in Basketball, Soccer and Hockey** 

### Shael Brown 

### Basketball Paper #1494 

#### **Abstract** 

In the sports of soccer, hockey and basketball the most commonly used statistics for player performance assessment are divided into two categories: offensive statistics and defensive statistics. However, qualitative assessments of playmaking (for example, making “smart” passes) are difficult to quantify. It would be advantageous to have available a single statistic that can emphasize the flow of a game, rewarding those players who initiate and contribute to successful plays more. In this paper we will examine a model based on Google's PageRank. Other papers have explored ranking teams, coaches, and captains but here we construct ratings and rankings for individual members on both teams in a game that emphasize initiating and partaking in successful plays and forcing defensive turnovers. 

For a soccer/hockey/basketball game, our model assigns a node for each of the _n_ players who play in the game and a “goal node”. Arcs between player nodes indicate a pass in the _reverse_ order (turnovers are dealt with separately). Every sport-specific situation (fouls, out-of-bounds, playstoppages, turnovers, missed shots, defensive plays) is addressed, tailored for each sport. As well, some additional arcs are added in to ensure that the associated Markov chain transition matrix is primitive (some power of the matrix has all positive entries) and hence there is a unique PageRank vector, which is used to rate and rank the players of the game. 

To illustrate the model, data was taken from nine NBA games played between 2014 and 2016. The application shows that this model does indeed provide the type of comprehensive statistic described in the introductory paragraph. Many of the top-ranked players (in the model) in a given game have some of the most impressive traditional stat-lines. However, from the model there are surprises where some players who have impressive stat-lines have lower ranks, and others, who have less impressive stat-lines have higher ranks. 

Overall, the model provides an alternate tool for player assessment in soccer, basketball and hockey. The model's ranking and ratings reflect more the flow of the game compared to traditional sports statistics. 





2017 Research Papers Competition Presented by: 

1 



## **1. Background** 

Google PageRank was created as the backbone to what is now the most influential search engine ever created [7]. Its purpose is to rank the importance of web pages when a user makes a query. The foundations of PageRank lie in Markov chain theory (see, for example [9]): given a finite set of states 𝑆= 𝑠$, ⋯, 𝑠' , let 𝑡),* be the probability of moving from state 𝑠) to state 𝑠* from time _k_ to 𝑘+ 1 (note that 𝑡),* is independent of _k_ ). Let 𝑇= [𝑡),*] denote the _transition matrix_ of the Markov chain. Provided that the matrix _T_ is _primitive_ (i.e. 𝑇<sup>1</sup> > 0 for some positive integer _m_ ), there is a unique _stationary vector_ **_v_** , such that 𝒗<sup>6</sup> 𝟏= 1 and  𝑻<sup>6</sup> 𝒗= 𝒗, where 𝟏 is the vector in ℝ<sup>'</sup> consisting of all 1's (that is, **_v_** is an eigenvector of  𝑻<sup>6</sup> with eigenvalue 1 whose nonnegative entries sum to 1). We call such a vector the _PageRank vector_ of the Markov chain. The lack of primitivity in Google's Markov model in general requires some alteration to the transition matrix in that case. Each component of the PageRank vector is thought of as the _rank_ of that state (and an ordering of the states is derived from these values). 

There is a natural way to construct a Markov chain from a (finite) directed graph and its adjacency matrix. The states of the chain are the nodes of the graph. If there are 𝑛),* (= 𝐴),*) arcs from node _i_ to node _j_ and node _i_ has a total of 𝑛) outgoing arcs, then 𝑇),* = ''<<,= ~~.~~ For a Markov chain derived from 

a directed graph, primitivity of the Markov chain corresponds to the existence of a positive integer _k_ such that there is a walk of length _k_ between any two nodes. In such a case there is a unique stationary vector for the associated Markov chain, which can be calculated from a linear system (see [7] for more details). We remark that it has been observed that the PageRank vector is fairly insensitive to small changes in the network involving only lowly ranked nodes [4, 5]. 

Previous applications of PageRank to sports metrics usually address ranking either teams [1, 2, 10], coaches [8], or individual players on various teams [10, 11]. A number of models have relied on underlying graph networks of games in their respective sports. In [12] a directed graph representing the passes between the starting players on an individual soccer team was constructed and a PageRank vector was computed to highlight who were the most important players on the team based on ball reception; the network as well was analyzed to determine the strategies and weak points of each team. In [6] every team has a corresponding weighted directed graph representing passes and two additional nodes representing the other team's goal and missed shots. Cricket batsmen and bowlers that face each other on separate teams are compared using a basic model much like the one that compares teams in the ``win-loss'' PageRank method for ranking teams [11]. A weighted directed graph for players across many basketball teams is created in [13] where arcs exist only between players who played on the court together on the same team at some point and the weight of these arcs corresponds to how effective they were in playing together. Finally, in [3] a PageRank network is created for each individual soccer team, where arcs indicate passes between players. 

None of these models allow for the effective comparison of any two players playing in the same game together (or even in different games), possibly of different positions or teams, using a PageRank method. More significantly, they do not emphasize playmaking ability, as opposed to pure offensive statistics, and that is exactly what we plan to do. 



2017 Research Papers Competition Presented by: 



2 



## **2. The Model** 

We create a directed graph (which we abbreviate as a _digraph_ ) representing the progression of play during a particular game – whether soccer, basketball or hockey. For each of the _n_ players in the game there is a node, and the digraph contains one additional _goal node_ (while our implementation of a goal node is not unique, the use of a “missed shot” node in [6] is redundant when we have both teams that are competing against each other in a game represented on the same digraph). Since we desire a model that values playmaking, we must reverse the direction of most arcs that would result from a straightforward progression of play (such an idea was raised but not deeply pursued in a multi-team setting in [3]). For player _i_ and player _j_ (represented by node _i_ and node _j_ , respectively) on the same team, whenever player _i_ passes to player _j_ we draw an arc from node _j_ to node _i_ . However, if players _i_ and _j_ are on separate teams and player _i_ loses the ball/puck to player _j_ we draw an arc from node _i_ to node _j_ . If player _i_ scores, the sport specific value of the score will be the number of arcs drawn from the goal node to node _i_ (for example an NBA 3-pointer would result in three arcs). All of our choices for arc direction ensures the flow of rank rewards playmaking. There will be more game specific arcs, to be discussed below. 

We initialize the digraph for a given game as follows. We draw arcs in both directions between each player node and the goal node, and in addition, we draw a loop from the goal node to itself. Outside of goal scoring, no other arcs will be added to or from the goal node. If team 1 has 𝑛$ players and team 2 has 𝑛> players (𝑛$ + 𝑛> = 𝑛), then in the corresponding game adjacency matrix, _A_ , 𝐴∈ 𝑀'A$,'A$(ℝ), the first 𝑛$ columns (and rows) of _T_ represent players on team 1, columns (and rows) 𝑛> + 1 to _n_ representing players on team 2, and the (𝑛+ 1)th column and row representing the goal node. Thus, before the game starts, 𝐴'A$,* = 𝐴),'A$ = 1 for 1 ≤𝑖, 𝑗≤ 𝑛+ 1 and 𝐴),* = 0 otherwise. The method of construction of the initial digraph ensures that any two nodes are connected by a path of length exactly two, and hence the corresponding Markov chain transition matrix, _T_ , will have each entry of 𝑇<sup>></sup> nonnegative, making _T_ primitive, and therefore the Markov chain associated with the digraph has a unique PageRank vector. 

We let 𝒓 = (𝑟$, ⋯, 𝑟', 𝑟I) be the PageRank vector of the game transition matrix. For a number of reasons, to be listed, we shall rescale the values in the PageRank vector (such a process does not change the induced ordering of the players’ ranks). One immediate issue with the model is the fact that the goal node may have different rank in each game depending on the number of players in the game, thus making the comparison of ranks of players in different games dependent on the rank of the goal node. We can scale the computed rank vector **_r_** by any scalar, as **_r_** is an eigenvector of 𝑇<sup>6</sup> . We standardize _r_ by defining the relative rank of player _i_ in the game by 



The choice of scaling is as follows: the denominator removes the effect of the goal node’s rank, and the numerator ensures (a) that the relative rank is insensitive to the number of players in the game and (b) provides values on a reasonable scale, between 0 and 50𝑛 (it is not hard to see that the average relative ranks of all players in a game is 50). The relative ranks can thus be used for meaningful comparison of players in different games. 

We now return to how the digraph itself is built up in the three sport specific situations. We 



2017 Research Papers Competition Presented by: 



3 



illustrate the process with basketball (the rules for soccer and hockey can be found in the Appendix). Each bullet point is a play “event”, with its subsequent descriptor the corresponding arc(s) to add to the digraph. 

Basketball rules of implementation: 

- Pass from player _i_ to player _j_ . 

   - an arc from node _j_ to node _i_ 

- Player _i_ dispossesses player _j_ . [This could include cases where player _i_ does not gain possession of the ball after dispossessing player _j_ – for example a defensive touch leading to the ball being out of play or deflecting a pass still into play but away from its intended target.] 

   - an arc from node _j_ to node _I_ 

- Player _I_ scores _n_ points where 1 ≤𝑛≤4. 

   - _n_ arcs from the goal node to node _I_ 

- Player _I_ shoots when being contested and defended by player _j_ and misses the net. [Same as player _j_ dispossessing player _I_ , play resuming with the rebounding/inbounding player. This case includes the situation where player _j_ blocks player _i_ .] 

   - an arc from node _i_ to node _j_ 

- Player _i_ shoots and misses the net under no pressure and the ball is rebounded by player _j_ . [Same as player _j_ dispossessing player _i_ .] 

   - an arc from node _i_ to player _j_ 

- Player _i_ fouls player _j_ and player _j_ makes at least one free throw. 

   - if player _j_ makes _n_ > 0 free throws then _n_ arcs are created from the goal node to node _j_ 

- Player _i_ fouls player _j_ and player _j_ makes zero free throws. [Same as player _j_ dispossessing player _i_ – it was a “smart” foul.] 

   - an arc from node _j_ to node _i_ 

- Any stoppage of play that does not have to do with the game (i.e. a technical foul, fan interference, injury, altercation etc.). [Play is dead.] 

   - no arc drawn 





2017 Research Papers Competition Presented by: 

4 



- Player _i_ intercepts a pass from player _j_ . [Same as player _i_ dispossessing player _j_ .] 

   - an arc from node _j_ to node _i_ 

- Player _i_ touches the ball without having possession (for example the ball hits player _i_ , or a “pinball” play). 

   - no arc drawn 

- Any unforced turnover by player _i_ . 

   - no arcs drawn 

We illustrate the process with a small example. Suppose that two basketball teams, the Reds and the Blues, are playing against each other in a “3-on-3” match (where all baskets are worth one point). We will denote the players on the Reds by A, B and C, and those on the Blues by D, E and F. Before the game begins we have the setup of the digraph shown in Figure 1 (where G stands for the goal node). In this and subsequent diagrams of digraphs, if there exists more than one arc from node _x_ to node _y_ we will draw one arc from node _x_ to node _y_ but label it with the number of arcs that exist between the two nodes. 



<!-- Start of picture text -->
A F<br>G<br>B E<br>C D<br><!-- End of picture text -->

Figure 1: Small example’s initial digraph (before play). 

Now suppose we have the following sequence of plays in the game: (where “→” represents the movement of the ball between nodes, and “0” is the end of play sequence symbol): 



2017 Research Papers Competition Presented by: 



5 



A→B→A→F→G 

D→F→E→F→D→C→B→C→A→C→B→A→G 

D→C→A→C→B→A→G 

D→F→0→B→C→A→G 

D→F→E→F→D→G 

###### A→B→F→G 

After these sequences of plays our updated network becomes: 



<!-- Start of picture text -->
A F<br>3 2<br>3<br>2<br>G 2<br>B E<br>2<br>2 3<br>3<br>C D<br>2<br><!-- End of picture text -->

Figure 2: Small example updated 

The adjacency matrix of the digraph (whose (𝑖, 𝑗)–th entry is the number of arcs in the digraph from node _i_ to node _j_ ) is 





2017 Research Papers Competition Presented by: 

6 





and so the transition matrix for this game is 



The calculated relative ranks of the players in the system are as follows: 

|Player|Team|Relative Rank|
|---|---|---|
|C|Reds|64.66|
|F|Blues|60.38|
|A|Reds|58.79|
|B|Reds|52.39|
|D|Blues|39.17|
|E|Blues|24.61|



While player A scored the most goals in the game and player F had the same number of total goals and assists, we see that in fact player C, who had only 1 assist and no goals, has the highest rank. However, a cursory examination of the plays clearly shows how integral player C was in the game as a playmaker. The example shows how a player whose contribution to the game might be ignored under the usual stat lines receives their well-deserved acknowledgement under the proposed model. 

Before we continue with some experimental results it is natural to ask how this model fits with our intuition of evaluating the performance of athletes. We observe first that the lowest possible 



2017 Research Papers Competition Presented by: 



7 



relative rank of any player in a game of _n_ players is no more than 50, since if the smallest relative rank of any player in the game is more than 50, since if the relative rank of every player were larger than 50, we would contradict the fact that the average relative rank of all players in the game is 50. The following propositions consider the spacing of relative ranks in a game. 

_Proposition 2.1_ . If there are _k_ starters (out of _n_ players) in a given game with a cumulative starter '(QRSTU) relative rank of _R,_ then there must exist a bench player with a rank that is at most distance U('RU) from the rank of some starter. 

ST'RQ _Proof._ We first note that the average bench player relative rank must be as there are 𝑛 − 𝑘 'RU bench players and the total sum of all the relative ranks is 50𝑛. Clearly the worst-case scenario Q ST'RQ occurs if all starters have a rank of and all bench players have a rank of (as otherwise there U 'RU ST'RQ would have to be one bench player with relative rank greater than or one starter with rank 'RU 

Q less than ). Thus, in this worst-case scenario the distance between any starter and any bench U player is Q − ST'RQ = Q'RQURST'UAQU = '(QRSTU) ~~.~~ n U 'RU U 'RU U('RU) 

_Proposition 2.2._ If there are _n_ players in a game then there must exist at least two players who have >S' relative ranks within of each other. 'R> 

_Proof._ Clearly 0 is a lower bound on the relative rank of a player in a given game and an upper bound is 50𝑛 (the sum of all the relative ranks). Thus, we may partition this range into 𝑛 − 2 equal ST' length intervals, each of length using 𝑛 − 1 of the _n_ total players. We must have that at least 'R> three players must be within (or on the boundary of) one of the 𝑛 − 2 intervals, meaning that two of their relative ranks must be in the same half interval, making the difference of their relative >S' ranks no more than .     n 'R> 

The above two results show that there has to be some bench player of non-negligible importance to the game, and that some players have to have ranks that are “somewhat” close to each other. The first result fits with the widely accepted notion that bench play is a component to the success of a basketball team. 

Finally, we may be interested in how the number of goals scored by players on different teams affects their relative ranks. As an illustration, suppose we have only two players, 𝑃$ and 𝑃>, in the system, each on separate teams, with no interaction between them and 𝑃$ scores 𝑔$ goals and 𝑃$ scores 𝑔> goals. Then if 𝑔$ < 𝑔> then the relative rank of 𝑃$ is greater than that of 𝑃>. This follows as it is clear that the relative rank of 𝑃$ is ST'Z[(I\A$) and the relative rank of 𝑃> is (I\AI]A>)($RZ[) 

ST'Z[(I]A$) (I\AI]A>)($RZ[) ~~w~~ here 𝑟I is the rank of the goal node. 





2017 Research Papers Competition Presented by: 

8 



## **3. Sample Data Analysis** 

We now apply our model to some real-life basketball games. The specific games used were 

- Chicago Bulls vs. San Antonio Spurs (November 30th 2015), 

- Golden State Warriors vs. Cleveland Cavaliers (January 18th 2016), 

- San Antonio Spurs vs. Brooklyn Nets (December 3rd 2014), 

- Chicago Bulls vs. Charlotte Hornets (December 3rd 2014), 

- Los Angeles Lakers vs. Golden State Warriors (November 1st 2014), 

- Toronto Raptors vs. Cleveland Cavaliers (December 9th 2014), 

- Golden State Warriors vs. Cleveland Cavaliers (December 25th 2015), 

- Chicago Bulls vs. Oklahoma City Thunder (December 25th 2015), and 

- Washington Wizards vs. Cleveland Cavaliers (November 26th 2014). 

The games are identified by the teams playing, date, score and winning team. In each game, plays were manually analyzed and transcribed, and the resulting transition matrices and PageRank vectors were calculated. The nine tables, in decreasing order, the relative ranks of each of the players (rounded to the nearest hundredth) in all nine NBA basketball games from which data was taken, followed by each players points (P), assists (A), rebounds (R), steals (S), turnovers (T) and field goal percentage (FG%), rounded to the nearest whole number, (in that order) all accessed from nba.com. 

Chicago Bulls vs. San Antonio Spurs, November 30th 2015 (Bulls win 92-89) 

|Player name|Team|Relative Rank|P|A|R|S|T|FG%|
|---|---|---|---|---|---|---|---|---|
|Parker|Spurs|103.66|13|9|1|0|0|50|
|Rose|Bulls|83.68|11|6|4|1|1|29|
|Duncan|Spurs|74.05|6|3|12|0|2|43|
|Gasol|Bulls|72.30|18|4|13|1|1|33|
|Leonard|Spurs|63.62|25|3|8|2|2|77|
|Aldridge|Spurs|59.99|21|0|12|0|2|55|
|Noah|Bulls|58.32|8|7|11|0|0|67|
|Green|Spurs|57.69|9|1|4|2|1|30|
|Butler|Bulls|49.23|14|3|3|1|5|55|
|Mirotic|Bulls|46.55|8|2|5|0|2|38|
|Ginobli|Spurs|44.89|4|2|1|1|1|25|
|Diaw|Spurs|44.82|5|0|6|0|1|40|
|Mills|Spurs|40.31|4|1|0|0|0|25|
|Moore|Bulls|33.42|6|1|2|0|1|50|
|West|Spurs|31.02|2|1|3|0|0|20|
|Snell|Bulls|27.48|11|1|6|0|0|80|
|McDermott|Bulls|24.97|12|0|3|0|0|42|
|Gibson|Bulls|20.86|4|1|4|1|0|40|
|Anderson|Spurs|13.13|0|0|0|0|0|0|





2017 Research Papers Competition Presented by: 



9 



Golden State Warriors vs. Cleveland Cavaliers, January 18th 2016 (Warriors win 132-98) 

|Player name|Team|Relative Rank|P|A|R|S|T|FG%|
|---|---|---|---|---|---|---|---|---|
|Curry|Warriors|122.91|35|4|5|3|1|67|
|Green|Warriors|109.34|16|10|7|0|1|50|
|Dellavedova|Cavaliers|109.26|11|6|1|0|1|50|
|James|Cavaliers|91.43|16|5|5|1|3|44|
|Irving|Cavaliers|78.75|8|3|5|0|2|27|
|Barnes|Warriors|66.94|12|0|2|0|2|50|
|Livingston|Warriors|62.80|4|0|2|0|2|67|
|Love|Cavaliers|60.54|3|2|6|0|1|20|
|Iguodala|Warriors|60.24|20|5|3|0|1|88|
|Bogut|Warriors|58.61|4|0|6|0|0|67|
|Varejao|Cavaliers|50.63|5|3|4|1|1|50|
|Shumpert|Cavaliers|39.84|10|0|2|0|3|67|
|Barbosa|Warriors|39.52|8|4|1|2|0|50|
|Thompson|Warriors|39.05|15|2|1|1|1|45|
|Clark|Warriors|38.24|6|2|2|0|0|29|
|Ezeli|Warriors|29.79|4|0|2|0|2|67|
|Mozgov|Cavaliers|28.84|6|3|0|0|1|50|
|Smith|Cavaliers|26.99|14|1|2|1|1|67|
|Thompson|Cavaliers|23.73|2|0|2|0|0|0|
|JThompson|Warriors|21.89|1|1|3|0|0|1|
|Cunningham|Cavaliers|20.39|9|1|3|0|0|60|
|Jefferson|Cavaliers|18.47|6|0|3|0|1|100|
|Jones|Cavaliers|17.43|8|1|0|0|1|60|
|Speights|Warriors|17.22|4|0|1|0|0|25|
|Rush|Warriors|17.17|3|1|3|0|0|33|







2017 Research Papers Competition Presented by: 

10 



San Antonio Spurs vs. Brooklyn Nets, December 3rd 2014 (Nets win 95-93) 

|Player name|Team|Relative Rank|P|A|R|S|T|FG%|
|---|---|---|---|---|---|---|---|---|
|Williams|Nets|111.40|17|9|3|0|2|40|
|Teletovic|Nets|90.99|26|2|15|0|0|69|
|Duncan|Spurs|81.11|14|1|17|0|2|28|
|Parker|Spurs|79.92|9|6|1|0|3|50|
|Ginobli|Spurs|68.23|15|5|6|1|0|46|
|Green|Spurs|65.77|20|2|10|2|0|50|
|Lopez|Nets|62.01|16|3|16|0|0|35|
|Leonard|Spurs|56.59|12|1|13|1|0|25|
|Joseph|Spurs|55.32|7|3|3|0|0|38|
|Johnson|Nets|53.48|8|2|5|1|1|25|
|Jack|Nets|47.11|8|3|1|0|2|40|
|Diaw|Spurs|45.72|0|3|2|0|2|0|
|Bonner|Spurs|35.93|7|0|1|0|0|30|
|Bogdanovic|Nets|32.72|14|0|8|0|2|50|
|Baynes|Spurs|17.78|4|1|4|1|0|40|
|Anderson|Nets|14.49|2|1|1|0|2|20|
|Belinelli|Spurs|11.89|5|1|1|0|1|67|
|Jordan|Nets|9.83|2|0|2|1|0|100|
|Plumlee|Nets|9.73|2|0|3|0|1|33|



Chicago Bulls vs. Charlotte Hornets, December 3rd 2014 (Bulls win 102-95) 

|Player name|Team|Relative Rank|P|A|R|S|T|FG%|
|---|---|---|---|---|---|---|---|---|
|Walker|Hornets|110.08|23|4|5|1|0|39|
|Rose|Bulls|85.77|15|5|2|0|2|42|
|Gasol|Bulls|84.94|19|3|15|0|2|37|
|Noah|Bulls|77.80|14|7|10|1|2|67|
|Mirotic|Bulls|73.59|11|1|2|0|1|50|
|Stephenson|Hornets|64.26|20|4|8|1|4|50|
|Zeller|Hornets|63.21|12|2|8|0|0|45|
|Williams|Hornets|59.65|6|0|3|1|0|40|
|Butler|Bulls|52.88|15|5|2|2|1|45|
|Brooks|Bulls|51.90|7|3|3|0|2|43|
|Hinrich|Bulls|48.90|12|2|3|0|1|44|
|Roberts|Hornets|37.93|3|3|1|0|0|13|
|Jefferson|Hornets|35.36|13|2|7|0|0|38|
|Dunleavy|Bulls|32.20|9|0|1|1|0|60|
|Henderson|Hornets|30.55|10|1|4|0|1|50|
|Hairston|Hornets|14.67|4|1|2|2|0|14|
|Snell|Bulls|13.54|0|1|1|0|0|0|
|Biyombo|Hornets|12.64|4|0|4|0|0|50|





2017 Research Papers Competition Presented by: 



11 



|Pargo|Hornets|0.14|0<br>0<br>0<br>0|0|<br>0|
|---|---|---|---|---|---|



Los Angeles Lakers vs. Golden State Warriors, November 1st 2014 (Warriors win 127-104) 

|Player name|Team|Relative Rank|P|A|R|S  T|FG%|
|---|---|---|---|---|---|---|---|
|Curry|Warriors|132.74|31|10|5|3  2|53|
|Lin|Lakers|94.24|6|6|4|1  5|0|
|Green|Warriors|89.61|9|1|5|1  1|33|
|Iguodala|Warriors|84.83|9|6|4|2  4|50|
|Bogut|Warriors|79.29|6|3|10|1  5|30|
|Bryant|Lakes|76.87|28|1|6|2  7|43|
|Hill|Lakers|74.27|23|4|5|0  2|71|
|Price|Lakers|64.48|1|6|4|2  2|0|
|Davis|Lakers|59.39|13|2|6|1  1|71|
|Barnes|Warriors|53.12|15|3|4|1  1|83|
|Thompson|Warriors|50.27|41|2|5|0  1|78|
|Livingston|Warriors|42.72|2|1|2|1  1|50|
|Boozer|Lakers|38.93|9|1|4|0  0|44|
|Ezeli|Warriors|37.05|3|1|4|0  2|100|
|Barbosa|Warriors|34.37|9|3|1|1  3|50|
|Johnson|Lakers|33.40|15|0|4|0  1|67|
|Ellington|Lakers|20.53|2|1|4|1  1|50|
|Speights|Warriors|14.58|2|0|3|0  0|50|
|Sacre|Lakers|7.69|4|0|1|0  2|50|
|Clarkson|Lakers|5.52|3|0|1|2  1|20|
|Henry|Lakers|4.95|0|0|0|0  0|0|
|Holiday|Warriors|1.18|0|0|0|0  0|0|







2017 Research Papers Competition Presented by: 

12 



Toronto Raptors vs. Cleveland Cavaliers, December 9th 2014 (Cavaliers win 105-101) 

|Player name|Team|Relative Rank|P|A|R|S  T|FG%|
|---|---|---|---|---|---|---|---|
|Lowry|Raptors|123.55|16|14|4|1  0|33|
|Irving|Cavaliers|118.30|13|10|1|2  2|42|
|James|Cavaliers|95.39|35|4|2|2  2|57|
|Love|Cavaliers|70.70|17|4|9|0  3|40|
|Valanciunas|Raptors|65.34|18|0|15|0  3|86|
|Dellavedova|Cavaliers|59.32|6|5|3|0  0|50|
|Patterson|Raptors|47.36|12|1|4|0  1|71|
|Thompson|Cavaliers|44.27|8|0|8|0  1|60|
|Williams|Raptors|43.97|6|4|1|0  1|25|
|A.Johnson|Raptors|41.76|10|2|2|0  2|50|
|Ross|Raptors|37.68|18|1|3|0  5|62|
|Vasquez|Raptors|33.11|3|2|0|0  1|33|
|Fields|Raptors|32.38|4|2|1|2  1|100|
|Varejao|Cavaliers|32.15|8|1|6|0  1|40|
|Waiters|Cavaliers|29.92|18|2|1|0  1|70|
|J.Johnson|Raptors|24.98|12|0|4|1  1|46|
|Marion|Cavaliers|23.12|0|0|1|0  1|0|
|Jones|Cavaliers|20.41|0|1|0|0  0|0|
|Hayes|Raptors|6.30|2|0|1|0  0|100|







2017 Research Papers Competition Presented by: 

13 



Golden State Warriors vs. Cleveland Cavaliers, December 25th 2015 (Warriors win 89-83) 

|Player name|Team|Relative Rank|P|A|R|S|T|FG%|
|---|---|---|---|---|---|---|---|---|
|Green|Warriors|140.89|22|7|15|0|4|47|
|Curry|Warriors|117.29|19|7|7|2|3|40|
|Love|Cavaliers|106.85|10|4|18|0|1|31|
|Dellavedova|Cavaliers|98.70|10|1|5|1|1|36|
|James|Cavaliers|97.45|25|2|9|1|4|38|
|Iguodala|Warriors|74.47|7|3|2|1|0|17|
|Irving|Cavaliers|65.18|13|2|3|1|2|27|
|Thompson|Cavaliers|57.09|8|1|10|1|0|50|
|Livingston|Warriors|54.35|16|2|3|1|4|89|
|Thompson|Warriors|47.08|18|1|6|0|1|38|
|Bogut|Warriors|47.03|4|1|7|0|0|100|
|Ezeli|Warriors|36.77|3|0|4|0|2|25|
|Shumpert|Cavaliers|30.38|0|1|4|1|0|0|
|Smith|Cavaliers|28.77|14|0|1|1|2|44|
|Rush|Warriors|18.84|0|0|3|1|1|0|
|Mozgov|Cavaliers|15.40|0|0|3|0|1|0|
|Clark|Warriors|14.20|0|0|0|1|0|0|
|Barbosa|Warriors|14.04|0|0|1|0|0|0|
|McAdoo|Warriors|13.33|0|0|1|0|0|0|
|Speights|Warriors|10.75|0|0|0|1|1|0|
|Jones|Cavaliers|5.78|0|0|2|0|0|0|
|Williams|Cavaliers|5.35|3|1|0|0|0|0|







2017 Research Papers Competition Presented by: 

14 



Chicago Bulls vs. Oklahoma City Thunder, December 25th 2015 (Bulls win 105-96) *last 36.4 seconds of second quarter and first 17 seconds of 3rd quarter were not able to be seen from the source. 

|Player name|Team|Relative Rank|P|A|R|S|T|FG%|
|---|---|---|---|---|---|---|---|---|
|Westbrook|Thunder|125.96|26|8|7|6|6|39|
|Gasol|Bulls|104.06|21|6|13|0|4|50|
|Butler|Bulls|94.85|23|4|6|4|3|45|
|Durant|Thunder|79.36|29|7|9|1|2|52|
|Rose|Bulls|79.34|19|1|4|0|4|39|
|Kanter|Thunder|70.19|14|1|13|0|0|50|
|Gibson|Bulls|62.38|13|2|10|1|1|75|
|Ibaka|Thunder|58.25|6|0|7|2|2|25|
|Portis|Bulls|49.98|7|3|5|1|1|38|
|Hinrich|Bulls|41.15|2|2|0|0|0|50|
|Adams|Thunder|38.62|3|0|4|0|0|25|
|Brooks|Bulls|35.67|6|1|4|0|0|50|
|Mirotic|Bulls|32.04|6|2|7|1|1|20|
|Augustin|Thunder|28.25|3|1|1|1|2|25|
|Roberson|Thunder|23.22|2|1|4|0|0|17|
|McDermott|Bulls|19.31|5|1|3|1|1|29|
|Morrow|Thunder|18.27|9|0|1|1|0|50|
|Snell|Bulls|17.27|3|0|1|0|1|25|
|Waiters|Thunder|12.41|2|2|0|1|1|17|
|Collison|Thunder|9.42|2|0|2|0|0|50|







2017 Research Papers Competition Presented by: 

15 



Washington Wizards vs. Cleveland Cavaliers, November 26th 2014 (Cavaliers win 113-87) 

|Player name|Team|Relative Rank|P|A|R|S|T|FG%|
|---|---|---|---|---|---|---|---|---|
|James|Cavaliers|117.45|29|8|10|3|4|50|
|Irving|Cavaliers|117.00|18|5|1|3|1|47|
|Wall|Wizards|113.96|6|7|4|0|5|33|
|Beal|Wizards|62.07|10|2|2|3|1|40|
|Love|Cavaliers|61.40|21|0|5|0|2|70|
|Gortat|Wizards|52.63|12|1|2|1|3|50|
|Thompson|Cavliers|50.89|10|0|1|0|0|100|
|Waiters|Cavaliers|49.51|15|6|3|2|1|35|
|Miller|Wizards|48.21|7|6|2|0|0|75|
|Seraphin|Wizards|47.26|7|3|3|0|2|38|
|Varejao|Cavaliers|47.03|10|0|7|0|1|100|
|Humphries|Wizards|45.24|3|1|3|0|1|14|
|Pierce|Wizards|42.62|15|3|3|0|3|80|
|Marion|Cavaliers|40.00|6|2|4|2|0|25|
|PorterJr.|Wizards|30.72|2|1|2|0|0|25|
|Cherry|Cavaliers|28.63|2|0|0|2|0|0|
|Blair|Wizards|23.79|0|0|1|0|1|0|
|Butler|Wizards|23.11|23|0|1|1|2|60|
|Amundson|Cavaliers|20.52|0|1|1|0|0|0|
|Gooden|Wizards|16.66|2|0|3|0|0|50|
|Harris|Cavaliers|11.30|2|0|2|0|0|50|



We observe several general trends from the data that intuitively match what we would expect. For ^_ example, out of all the players with relative ranks under 30, ≈87% of them have their sum of SS points, assists, rebounds and steals no greater than 10, corresponding to a “small” stat line. On the >_ other hand, out of all players who have relative ranks greater than 70, ≈64% have their sum of ^^ points, assists, rebounds and steals be at least 25, corresponding to a “large” stat line. In terms of highest ranked positions, seven of the games had a point guard ranked the highest; however, a forward was ranked in the top five ranks in all nine games as well. On average, the starters of both teams owned approximately 7 out of the first 10 highest relative ranks, which fits with our knowledge that at least one bench player must have some significant importance to the game. Out of the nine games sampled, the highest ranked player was on the losing team four times. 

Now let us consider some basic trends in certain averages of the relative ranks in the nine games. In the table below all values were rounded to the nearest hundredth, WT stands for winning team, LT stands for losing team and ARR stands for average relative rank. 





2017 Research Papers Competition Presented by: 

16 



|Game|WT ARR|LT ARR|WT starter ARR|LT starter ARR|
|---|---|---|---|---|
|1|46.31|53.32|55.85|71.80|
|2|52.59|47.19|79.37|57.31|
|3|47.97|51.82|70.11|65.82|
|4|57.95|42.85|66.72|60.69|
|5|56.34|43.66|81.00|63.54|
|6|54.84|45.64|67.93|60.14|
|7|49.09|51.10|74.23|62.73|
|8|53.60|46.40|74.53|65.08|
|9|54.37|46.03|76.58|63.31|



Out of the nine games sampled, the winning team had a higher average relative rank than that of the losing team six times. However, the average ranks of starters on the winning team was greater than that for the losing team in eight out of the nine games. 

In many cases our intuition of how a strong overall performance by a player should be ranked agreed with the generated relative ranks. For example, consider the cases of LeBron James (Cleveland Cavaliers), Stephen Curry (Golden State Warriors) and Pau Gasol (Chicago Bulls). Each are recognized as being very talented players in the NBA and in each game surveyed in which they played they each had a “strong” stat line, and also a very high relative rank (corresponding to them being excellent playmakers as well). However, there were certainly also some surprises where players with “strong” stat lines did not have large relative ranks. In the Lakers vs. Warriors game, Klay Thompson scored 41 points yet had a very average relative rank of 50.27. In the Wizards vs. Cavaliers game, Butler had 23 points and a rank of about 23. 

A general trend that we observe is that out of all the players who had at least 15 points and have a relative rank less than 50, 89% had the sum of their assists, rebounds and steals be under 10, i.e. scoring alone was not generally highly valued by the model. In contrast, out of the 30 players in all games who had at least 5 assists, 28 of them had a relative rank of at least 50 (about 93%), showing a general trend of rewarding passing compared to scoring. There were of course also some overachievers in the sample data; of the top 10 ranks in each game, on average 40% had a sum of their points, assists, rebounds and steals be at most 20, corresponding to what one could call an at most “standard/average” stat line. Specific examples of high ranking players with low stat lines in this model were John Wall (Wizards vs. Cavaliers), Ronnie Price (Lakers vs. Warriors), Jeremy Lin (Lakers vs. Warriors), Tony Parker (Spurs vs. Nets) and Matthew Dellavedova (Cavaliers vs. Warriors and Cavaliers vs. Raptors). 

## **4. Conclusion** 

While the relative ranks of players are comparable between games, in future work we may consider, over a whole season in one sports league, having all players and teams represented by one large digraph with one goal node. This large-scale model could be used as another measure of performance between any athletes in the same league. Note that 





2017 Research Papers Competition Presented by: 

17 



adjusting this model for dealing with events such as player trades would not be difficult. In any case, automating the processing of input is a necessary step in scaling the model. Moreover, adjusting the model to encompass more sports that follow similar models to soccer, basketball and hockey, for instance volleyball or water polo, could find useful applications as well. 

The PageRank-based model, which we have constructed, appears to be the first of its kind to give a quantifiable measure in which players on different teams and even different games can be ranked and compared, inclusive of their offensive and defensive skills. While the model could serve as a useful mainstream statistic for scouts, coaches, managers and fans, more data analysis is required to see if the model can provide accurate outcome predictions for games (for example, comparing the average relative rank of the starters of each team, prior to that game). The statistics from our proposed model could be used in conjunction with the standard player performance metrics in each sport to help deepen our understanding of who is really influencing the game the most. 





2017 Research Papers Competition Presented by: 

18 



## **References** 

[1] Balreira, Eduardo C., Brain K. Miceli, and Thomas Tegtmeyer. "An Oracle Method to Predict NFL Games." _Journal of Quantitative Analysis in Sports_ 10 (2014): 183-196. [2] Barrow, Daniel, Ian Drayer, Peter Elliott, Garren Gaut, and Braxton Osting. ”Ranking rankings: an empirical comparison of the predictive power of sports ranking methods.” _Journal of Quantitative Analysis in Sports_ 9 (2013): 187-202. 

[3] Brandt, Markus, and Ulf Brefeld. ”Graph-based Approaches for Analyzing Team Interaction on the Example of Soccer.” _Proceedings of the ECML/PKDD Workshop on Machine Learning and Data Mining for Sports Analytics_ 8 (2015). 

[4] Chartier, Timothy P., Erich Kreutzer, Amy N. Langville, and Kathryn E. Pedings. ”Sensitivity and stability of ranking vectors.” _Siam Journal of Scientific Computing_ 33 (2011): 1077-1102. 

[5] de Kerchove, Cristobald, Laura Ninove, and Paul Van Dooren. ”Maximizing PageRank via outlinks.” _Linear Algebra and its Applications_ 429 (2008): 1254-1276. 

[6] Duch, Jordi, Joshua S. Waitzman, and Luis A. Nunes Amaral. ”Quantifying the Performance of Individual Players in a Team Activity.” _PLoS ONE_ 5 (2010). 

[7] Glelch, David F. ”PageRank Beyond the Web.” _SIAM Review_ 57 (2015): 321-363. 

[8] Hu, Zhi, Jing Zhou, Meng Zhang, and Yang Zhao. ”Methods for ranking college sports coaches based on data envelopment analysis and PageRank.” _The Journal of Knowledge Engineering_ 32 (2015): 652-73. 

[9] Langville, Amy N., and Carl D. Meyer. _Google’s PageRank and Beyond: The Science of Search Engine Rankings_ . N.p.: Princeton University Press, 2011. 

[10] Mukherjee, Satyam. ”Identifying the greatest team and captain - A complex network approach to cricket matches.” _Physica A: Statistical Mechanics and its Application_ 391 (2012): 6066-6076. 

[11] Mukherjee, Satyam. ”Quantifying individual performance in Cricket - A network analysis of batsmen and bowlers.” _Physica A: Statistical Mechanics and its Application_ 393 (2013): 624-637. 

[12] Pea, Javier L., and Hugo Touchette. ”A network theory analysis of football strategies.” _Proc. 2012 Euromech Phsycis of Sports Conference_ (2013) 517-528. 

[13] Piette, James, Lisa Pham, and Sathyanarayan Anand. ”Evaluating Basketball Player Performance via Statistical Network Modeling.” _MIT Sloan Sports Conference_ (2011). 





2017 Research Papers Competition Presented by: 

19 



### **Appendix** 

##### **Soccer rules of implementation:** 

- Pass from player _i_ to player _j_ . 

   - an arc from node _j_ to node _i_ 

- Player _i_ dispossesses player _j_ . [This could include cases where player _i_ does not gain possession of the ball after dispossessing player _j_ ; for example a defensive tackle leading to the ball being out of play or deflecting a pass still into play but away from its intended target.] 

– an arc from node _j_ to node _i_ 

- Player _i_ scores. 

   - an arc from the goal node to node _i_ 

- Player _i_ shoots when being pressured by player _j_ and misses the net. [Same as player _j_ dispossessing player _i_ . This case includes the situation where player _j_ blocks player _i_ 

   - an arc from node _i_ to node _j_ 

- Player _i_ shoots and misses the net under no pressure. [Play is dead.] 

– no arcs drawn 

- Player _i_ shoots and shot is saved by the goalkeeper, player _j_ . [Same as player _j_ dispossessing player _i_ .] 

– an arc from node _i_ to node _j_ 

- Player _i_ fouls player _j_ , not resulting in a goal. [Play is dead.] 

– no arcs drawn 

- Player _i_ fouls player _j_ , resulting in a penalty or a goal from a free kick. [Smart drawing of a foul by player _j_ ; scoring from a free kick could include a direct shot, a header or volley from the free kick or a rebound inside the box following the free kick.] 

##### – an arc from node _i_ to node _j_ 





2017 Research Papers Competition Presented by: 

20 



- Any stoppage of play that does not have to do with the game (i.e. weather, fan interference, injury, altercation etc.). [Play is dead.] 

– no arcs drawn 

- Player _i_ intercepts a pass from player _j_ . [Same as player _i_ dispossessing player _j_ .] 

   - an arc from node _j_ to node _i_ 

- Player _i_ touches the ball without having possession, for example, the ball hits player _i_ , or a “pinball” play. [Player _i_ did not have possession.] 

– no arcs drawn 

- Any unforced turnover by player _i_ . 

   - no arcs drawn 

- Player _i_ is offside when player _j_ passes the ball. [Player _j_ passes the ball to player _i_ who is in an offside position, so the play ends at player _i_ .] 

   - an arc from node _i_ to node _j_ 

###### **Hockey rules of implementation:** 

- Pass from player _i_ to player _j_ . 

##### – an arc from node _j_ to node _i_ 

- Player _i_ dispossesses player _j_ . [This could include cases where player _i_ does not gain possession of the puck after dispossessing player _j_ , for example a defensive touch leading to the puck being out of play or deflecting a pass still into play but away from its intended target.] 

##### – an arc from node _j_ to node _i_ 

- Player _i_ scores. 

   - an arc from the goal node to node _i_ 

- Player _i_ shoots when being defended by player _j_ and misses the net. [Same as player _j_ dispossessing player _i_ ; play resumes with the player that collects the puck after the shot. This case includes the situation where player _j_ blocks the shot of player _i_ .] 

   - an arc from node _i_ to node _j_ 





2017 Research Papers Competition Presented by: 

21 



- Player _i_ shoots and the shot is saved by the goalkeeper, player _j_ . [Same as player _j_ dispossessing player _i_ .] 

##### – an arc from node _i_ to node _j_ 

- Player _i_ shoots and misses the net under no pressure. [Play is dead.] 

##### – no arcs drawn 

- Player _i_ draws a penalty from player _j_ during which no power-play goal is scored. [A “smart” penalty.] 

##### – an arc from node _i_ to node _j_ 

- Player _i_ draws a penalty from player _j_ during which a power-play goal is scored. [A “smart” drawing of a penalty.] 

##### – an arc from node _j_ to node _i_ 

- Any stoppage of play that does not have to do with the game (i.e. a penalty, fan interference, injury, altercation etc.). [Play is dead.] 

##### – no arcs drawn 

- Player _i_ intercepts a pass from player _j_ . [Same as player _i_ dispossessing player _j_ .] 

##### – an arc from node _j_ to node _i_ 

- Player _i_ touches the puck without having possession (for example the puck hits player _i_ , or a “pinball” play). [Player _i_ did not have possession.] 

##### – no arcs drawn 

- Any unforced turnover by player _i_ . 

##### – no arcs drawn 

- Player _i_ is offside when player _j_ passes the puck. [Player _j_ still passed player _i_ the puck, the play ended by player _i_ being in an offside position.] 

##### – an arc from node _i_ to node _j_ 

- Player _i_ ices the puck which is touched by player _j_ . [Same as player _i_ turning the puck over to player _j_ .] 

##### – an arc from node _i_ to node _j_ 





2017 Research Papers Competition Presented by: 

22 


