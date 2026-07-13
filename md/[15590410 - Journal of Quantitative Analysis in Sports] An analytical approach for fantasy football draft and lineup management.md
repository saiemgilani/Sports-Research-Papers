<!-- source: [15590410 - Journal of Quantitative Analysis in Sports] An analytical approach for fantasy football draft and lineup management.pdf -->

J. Quant. Anal. Sports 2016; 12(1): 17–30 

### Adrian Becker and Xu Andy Sun* 

# **An analytical approach for fantasy football draft and lineup management** 

##### DOI 10.1515/jqas-2013-0009 

**Abstract:** In this paper, we consider fantasy football, an increasingly-popular online game based on the actual, on-the-field performances of players in the National Football League. It is estimated by the Fantasy Sports Trade Association that in 2011 there were 35 million people in the US and Canada playing fantasy sports online. About 85 percent of all fantasy sports participants play fantasy football, most of whom have their games set up in major media websites such as Yahoo!, ESPN, MSN, and NFL.  Numerous websites specialize in reporting NFL games, providing preseason rankings, fantasy points projections, team and player statistics, and expert draft opinions. However, despite the vast popularity of the game, the intensive analysis by experts, and various online tools that offer prediction for the values of players, to the best of our knowledge, there is no method that provides a comprehensive optimization strategy for the entire Fantasy Football season. We set out to develop such a methodology that predicts team and player performance based on the rich historical data, and builds a mixed-integer optimization model using such predictions for the draft selection as well as weekly line-up management that incorporates the entire objective of winning a fantasy football season. Numerical tests of our model show promising performance. 

**Keywords:** fantasy sports; mixed integer optimization; performance prediction; sports draft. 

playing fantasy sports online.<sup>1</sup> This number has risen significantly from a 2006 survey of 19.4 million online players in North America.<sup>2</sup> Its annual economic impact across the sports industry in 2006 is estimated to be $3–4 billion.<sup>3</sup> About 85 percent of all fantasy sports participants play fantasy football, most of whom have their games set up in major media websites such as Yahoo!, ESPN, MSN, and NFL.<sup>4</sup> Numerous websites have specialized in reporting NFL games, providing preseason rankings, fantasy point projections, team and player statistics, and expert draft opinions. However, despite the vast popularity of the game, the intensive analysis by experts, and various online tools that offer prediction for the values of players, to the best of our knowledge, there is no method that provides a comprehensive strategy for the entire fantasy football season. Thus, winning a league is, by and large, still more of an art than a science. 

We set out to develop such an approach that predicts team and player performance based on the rich historical data, and builds a mixed integer programming (MIP) model using such predictions for the draft selection as well as weekly lineup management, incorporating the entire objective of winning a fantasy football season. Due to the special structure of our model, the MIP formulation can be solved very efficiently, which is crucial for an on-line environment as the fantasy football draft process. We train our model using the data of 2004–2006 seasons and simulate the 2007 season and the 2008 season. The result is encouraging and shows an edge of our method over the conventional strategy. 

## **1  Introduction** 

In this paper, we consider fantasy football, which, as one of the fantasy sports, has become increasingly popular. It is estimated by the Fantasy Sports Trade Association that in 2011 there were 35 million people in the US and Canada 

***Corresponding author: Xu Andy Sun,** Georgia Institute of Technology – Industrial and Systems Engineering, 755 Ferst Drive, Atlanta, GA 30332, USA, e-mail: andy.sun@isye.gatech.edu **Adrian Becker:** Dynamic Ideas LLC, 465 Waverley Oaks Road, Suite 315, Waltham, MA 02452, USA 

**1** See Fantasy Sports Trade Association’s official website http://www. fsta.org/. 

**2** See report “Fantasy Sports Conference Demographic Survey Shows Continued Growth” at http://www.prweb.com/releases/2007/08/ prweb543818.htm. 

**3** See report “The fantasy football phenomenon” at http://www. theacorn.com/news/2006-08-03/Sports/076.html. 

**4** See websites at http://football.fantasysports.yahoo.com/, http:// games.espn.go.com/frontpage/football, http://msn.foxsports.com/ fantasy/football/commissioner/, http://www.nfl.com/fantasyfootball, and report “CNN Money: Fantasy football...real money” at http://money.cnn.com/2006/08/11/news/companies/fantasyfootball/. 

**18** A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management 

Two core methodologies are presented in this paper: 

1. A holistic optimization model which manages a team through draft construction and weekly management. 

2. The analysis of a player’s historical statistical performance on a weekly basis in the context of the player’s opponents; and the ability to make predictions on this analysis. 

While we apply these methodologies to fantasy football, they have potential use to general managers in the real world outside the realm of fantasy sports. Often general managers with a positional need will need to evaluate another team’s reserve players in the off season for a potential trade. Since these reserve players’ experience at the professional level is typically limited, it is crucial that it be evaluated in the context of their opponents. Furthermore, like fantasy managers, real world general managers must build and manage a team to win weekly matchups against known opponents and advance through the playoffs to be successful. We also acknowledge that the real world general managers have to consider several factors that are not present in the fantasy games, such as salary cap, multi-year contracts, player characters, team chemistry, etc; however, we believe understanding the trade-offs in the “stylized” fantasy sports settings could potentially factor into the realworld decision-making process. 

The paper is organized as follows. Section 2 reviews and analyzes some related work in sports drafting and prediction. Section 3 introduces background knowledge of fantasy football and the dynamics of a fantasy football season. Section 4 discusses in detail our integer optimization model for draft selection. Section 5 proposes a new estimation methodology for NFL player performance prediction, which plays an essential role in the draft selection model. Section 6 discusses available data and simulation procedure, presents the calibration and model evaluation results, and provides detailed analysis on several aspects of the proposed model. Section 7 concludes the paper with a discussion on possible extensions of our model. 

## **2  Literature review** 

Fantasy sports drafting and lineup management is a relatively new area of sports analytics. The related area of real-world sports drafting is also relatively unexplored. We are not aware of any existing work that proposes similar methods for fantasy sports drafting as 

presented in this paper. In the following, we review previous work in both real-world sports drafting and fantasy sports drafting and provide detailed comparison with our proposal. 

The paper by Summers, Swartz, and Lockhart (2007) considers the problem of optimal drafting in hockey pools, which is similar to the drafting process in fantasy football. The authors take a statistical approach and estimate, at each stage of the drafting, the probability that a lineup drafted by a player beats one of other lineups. The optimal drafting is to choose an available hockey player that maximizes this probability. 

Fry, Lundberg, and Ohlmann (2007) propose a stochastic dynamic programming (DP) model for the player selection draft of a single real-world NFL franchise, where the best choice of drafting at each round is determined by the DP recursion that maximizes the sum of the value added by the drafted player and the total expected value added to the team in the future rounds. To produce a  computationally tractable model, some simplifying assumptions are introduced to remove stochasticity from the model (mainly the uncertainty in opponent teams’ behavior) and reduce the size of the state space. The resulting deterministic DP can be efficiently solved as linear programs. 

Gibson, Ohlmann, and Fry (2010) extend the above work of Fry et al. (2007) to a more general situation where the decision maker (DM) executes a sequence of resource allocation decisions under the uncertainty of resource availability due to actions of competitors. The paper introduces a new type of stochastic knapsack problem with sequential competition and proposes a stochastic ruler approach and agent-based modeling framework. The numerical test compares favorably with the deterministic DP approach proposed in Fry et al. (2007). 

Among these three papers, the work of Summers et al. (2007) concerns hockey drafting in a fantasy environment, which is also potentially applicable to other fantasy sports drafting. However, the model and methodology proposed in Summers et al. (2007) mainly use statistical analysis tools, which is fundamentally different from our approach. Gibson et al. (2010) extend the work in Fry et al. (2007) to general situations of sequential resource allocation problems. The stochastic optimization framework and agent-based simulation approach are also qualitatively different from our proposal. Comparing to Fry et al. (2007), our proposed model uses a forward-looking approach, which avoids the computational difficulty of the DP model; the proposed model has a mixed-integer optimization formulation that incorporates a comprehensive objective of winning the entire season; and our model 

A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management **19** 

also considers the uncertainty in opponent owners’ drafting behavior and model it through robust optimization. 

In addition to the optimization model for drafting, we propose a prediction methodology that estimates player and team performance using historical data augmented by expert opinions. There is a rather extensive literature on sports game outcome prediction. For example, linear regression Markov chain models proposed by Kvam and Sokol (2006) and Brown and Sokol (2010) have proved to be successful for NCAA basketball prediction. The task for our model is more fine-grained in that it needs to predict fantasy points of each player and team in each game as well as the points needed for a team to win a game against a specific opponent. The distinctive feature of our model is that it introduces the notion of innate abilities of a player or a team in various statistics, and makes prediction based on them. 

The artificial neural network model proposed in David et al. (2011) has a component that uses statistical differentials to compare teams, such as the offensive passing yards gained by a team versus the defensive passing yard allowed by an opposing team. This is similar in spirit to our notion of opponent specific comparison. However, both the prediction methodology and the way the model is constructed are qualitatively different. The work by Berri and Simmons (2011) investigates the relationship between the draft position of a quaterback (QB) and his subsequent performance in the NFL. Their study focuses on predicting the overall value of a QB, independent of the opponent faced in each game, whereas our method offers prediction of players performance at all positions, in the context of competing against the opponent teams. Massey and Thaler (2013) finds similar conclusions as in Berri and Simmons (2011) that top draft picks in the real-world NFL drafting are significantly overvalued in a manner that is inconsistent with the notion of rational expectation and efficient markets. Again, their work focuses on estimating the market values or surplus values of players, rather than game-by-game performance. The doctoral thesis of Young (2010) develops a hybridintelligent decision support system for determining the expected contribution value of a potential NFL candidate. The model is based on machine learning and statistical methodologies. Works by Harville (1980) and Reid (2003) on predicting team scores and game margins have a similar principle to our work in that they account for the intricacies of a particular matchup including the offensive and defensive characteristics of opposing teams. Our work can be seen as an extension of this principle to the prediction of the individual player’s statistics rather than the overall team score. 

## **3  The dynamics of fantasy football** 

Fantasy football is an online game where 10–20 individuals (called “owners”) create and manage teams composed of real-life NFL players. Each week, owners are paired against each other and score points based on the actual performance of players on their teams. The owner with the highest total point for a week records a win. A fantasy football season is typically divided into three phases: draft, weekly play, and playoffs. There are many variations on the specifics of a fantasy football league, such as the number of owners participating in the league, the maximum size of the team roster, the number of slots for starting positions, how many points are rewarded for an NFL player’s specific real-world accomplishments, the length and dynamics of the playoff phase, and so on. To facilitate exposition, we develop and evaluate our methodology using the default rules of the Yahoo public fantasy league.<sup>5</sup> The proposed methodology is generally applicable to other variations of these rules. Throughout the paper, we assume the perspective of a team owner, and call it the DM, while other owners are called the opponents. 

### **3.1  Draft phase** 

The draft phase occurs before the NFL season officially starts. Owners are randomly assigned a pick order and then, according to this order, select real-world NFL players to be placed on their respective fantasy teams. Each NFL player can only be drafted on at most one owner’s team, so if a player is drafted, it precludes all other owners from including that player on their teams. The draft continues according to the pick order until each owner has filled his or her roster. As a side note, the draft typically follows a snaking order. For example, in a league of 20 owners, if the DM is assigned pick number 19, the DM makes the 19th pick, and the next owner makes the 20th and the 21st picks, then it wraps back and the DM makes the 22nd pick, then the 59th and the 62nd picks of the draft and so on. 

### **3.2  Weekly play phase** 

The regular NFL season consists of 17 weeks. Each NFL team plays 16 games with one per week and also has 

> **5** For details, see http://help.yahoo.com/l/us/yahoo/sports/fantasysports/football/rules/. 

**20** A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management 

one bye week, i.e. the week they do not play. Typically the first 15 weeks are devoted to the weekly play phase. For each week in this phase, owners are matched head to head. Each owner must select players from his or her roster to start that week. For each position, there is a limit to the number of players that can start. For the analysis, it is assumed that each owner can start with up to 1 quarterback, 2 running backs, 3 wide receivers, 1 tight end, 1 kicker, and 1 team defense. Owners then score points for that week according to the actual performance of their starting lineup. For example, according to the Yahoo league’s rule, an owner would score 6 points for each touchdown and 1 point for each 25 yards that the owner’s starting quarterback achieves in his game that week. For each head to head pairing, the owner with the highest total points records a win. It is important to note that players on NFL teams which have a bye week score no points and that any particular NFL team may be facing a strong or weak opponent in any given week. Therefore, an owner will likely want to adjust his or her starting lineup from week to week. 

value of players for a fantasy football season. However, we do not know any methodologies that plan a comprehensive strategy for the entire fantasy football season. Our model for draft selection as well as weekly and playoff management offers such a methodology. 

In particular, we believe that draft selections should fully incorporate the dynamics of the weekly play and playoff phases. Moreover, during the draft phase, owners typically have a very limited time frame of one to three minutes in which they must make their draft picks. So any methodology developed should incorporate a computationally tractable model which can be solved quickly. The proposed integer optimization model is quickly solvable to accomplish this task. As a preface, we introduce the parameters and decision variables used in the integer program. 

### **4.1  Parameters and decision variables** 

#### 1. Parameters: 

N: The set of NFL players and defensive teams. 

### **3.3  Playoff phase** 

The playoff phase typically consists of the last 2 weeks of the regular season. The four owners with the highest winning records during the weekly play phase enter the playoff phase. The playoff phase proceeds in a similar manner as the weekly phase: in the first week, the 1st and 4th as well as the 2nd and 3rd ranked owners are matched head to head. The two winners are matched head to head in the second week to determine the ultimate winner. In the event of a tie, the owner who has scored the most total points throughout the season is declared the winner. Again, bye weeks and NFL team matchups influence the starting lineup for owners in the playoff phase. Owners ranked 5th–8th also compete in a consolation playoff. Public fantasy football league challenges often charge an entry fee and offer cash prizes to winners, and private leagues are often operated by groups of individuals who place entry fees in a “pot” which is paid out to the top two owners in the end of the season. 

M: The set of positions M = {QB, RB, WR, TE, K, Def}. T: The set of weeks in the NFL regular and playoff seasons. Pos( _i_ ): The position of player _i_ , e.g. Pos(PeytonManning) = QB. 

PosLimit( _j_ ): The upper bound on the number of starting players for position _j_ ∈ M during the weekly play and playoff phases, e.g. PosLimit(QB)  = 1. 

_nk_ : The overall pick number of the DM’s _k_ -th draft pick. 

DMPlayer( _k_ ): The set of players that the DM has drafted by her _k_ -th pick. 

OppPlayer( _k_ ): The set of players that the opponents have drafted by the DM’s _k_ -th pick. 

_Rk_ ( _i_ ): Anticipated ranking of unselected player _i_ at the DM’s _k_ -th draft pick. 

_f_ ( _i_ , _t_ ): An estimate of the number of fantasy points player _i_ will score in week _t_ of the NFL regular season. 

β( _t_ ): The predicted amount of fantasy points the DM needs so to be reasonably confident to win in week _t_ ∈ T against the DM’s matchup opponent. 

γ _j_ : The number of players the DM must draft at position _j_ . 

#### 2. Decision variables: 

## **4   An integer optimization model for draft selection** 

As we have mentioned, there are many tools available on the internet that offer a prediction methodology for the 

The optimization model has two sets of binary decision variables for picking players in the draft phase and starting drafted players in each week, respectively. In particular, 

- _yi_ ∈ {0, 1}: _yi_ = 1 if the DM picks player _i_ in the draft phase, and _yi_ = 0 otherwise. 

- _xit_ ∈{0, 1} : _xit_ = 1 if the DM starts player _i_ in week _t_ , and<sup>_x_</sup> _it_ = 0 otherwise. 

A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management **21** 

- _zt_ ∈ {0, 1}: _zt_ = 1 if the total estimated fantasy points of the DM’s line-up in week _t_ is greater than β( _t_ ) (i.e. ∑ _i_ ∈N _f_ ( _i_ , ) _t xit_ > β( _t_ )), and _zt_ = 0 otherwise. 

There are roughly 590 offensive players and 32 defensive teams in the NFL, which determines the size of N. In a league of 20 owners, if the DM is assigned pick number 19, the overall pick number of her first draft pick _n_ 1 = 19, her second draft pick _n_ 2 = 22, her third draft pick _n_ 3 = 59 and so on, following a snaking draft order as mentioned earlier. DMPlayer( _k_ ) and OppPlayer( _k_ ) are updated after each draft pick. Using various online expert articles and preseason predictions, we create an initial player ranking _R_ 0( _i_ ) for each player _i_ . In particular, _R_ 0( _i_ ) is calculated by ordering the average ranking of available expert data sources. If a particular source does not rank a particular player, that player’s rank is taken to be one greater than the number of players ranked by the source. After each draft pick _k_ , the selected players are eliminated from the set _Rk_ , and the ranking of the remaining players are adjusted and form _Rk_ + 1. More will be discussed in the following subsection on modeling the opponent owners’ behavior. Quantities _f_ ( _i_ , _t_ ) and β( _t_ ) are derived from an estimation methodology proposed in Section 5. 

### **4.2   Modeling the drafting strategy of the opponent owners** 

Requisite in developing an optimization model for the draft selection is anticipating how opponent owners will draft players. In this paper, we propose a simple model for opponents’ drafting behavior using the media prediction and opinions. The media publishes numerous expert articles and websites during the NFL preseason that indicate a measure of players’ value and a suggested draft order.<sup>6</sup> Using these suggested draft orders we can assign each player _i_ an initial anticipated draft ranking _R_ 0( _i_ ). This ranking indicates the expected overall pick number for player _i_ . In other words, when the opponent owners pick their draft, they pick players according to a probability distribution whose expectation is equal to _R_ 0( _i_ ) for each player _i_ . In terms of model development, we feel that it is reasonable to assume that opponent owners will approximately adhere to this probability distribution for drafting. 

To account for the uncertainty in the opponents’ drafting behavior, we propose a simple model, which can 

> **6** See for example http://sports.yahoo.com/fantasy, http://www. rotosource.com, http://games.espn.go.com/frontpage/football, and http://fantasyfootball.com. 

be viewed as the _uncertainty set_ in the robust optimization framework. In particular, suppose that it is currently time for the DM to make her _k_ -th pick in the draft. Several players will have already been drafted by owners, imposing the constraints _yj_ = 0 for players already picked by opponents and _yj_ = 1 for players already picked by the DM. Using the draft order, we can create a new ranking for the remaining players, denoted as _Rk_ . After the DM picks her _k_ -th player, _nk_ + 1 − _nk_ − 1 players will be selected by opponents before the DM’s next pick. If we assume that these picks will come from the top α · ( _nk_ + 1 – _nk_ − 1) ranked players in _Rk_ for some parameter α ≥ 1, then for the DM’s next pick, she can pick at most one player from the top α · ( _nk_ + 1 − _nk_ ) ranked players in the current ranking _Rk_ , and for the DM’s next two picks, she can pick at most two players from the top α · ( _nk_ + 2 − _nk_ ) ranked players in the current ranking _Rk_ , and so on for all her remaining picks. Note that this uncertainty set imposes constraints on the DM’s drafting, not on the opponent owners’ drafting. As an example, the uncertainty set for the DM’s ( _k_ + 1)-th pick does not impose a rigid rule that the opponent owners must draft players ranked at the top α · ( _nk_ + 1 − _nk_ − 1), but rather it prohibits the DM from drafting these top α · ( _nk_ + 1 − _nk_ − 1) players at her ( _k_ + 1)-th round, regardless if these players have been drafted by the opponents. The opponent owners still draft according to the probability distribution mentioned in the previous paragraph. 

### **4.3  The draft selection model and algorithm** 

At each round of the DM’s draft pick, the DM makes the draft decision by solving the following optimization problem that incorporates the objective of maximizing the total number of winning games in the entire season as well as the total points scored by her team, subject to the constraints describing the fantasy football dynamics, opponents’ drafting behavior, and logic relationship between drafting decisions. In particular, we propose the following integer optimization model, denoted as (Draft _k_ ), solved at the DM’s _k_ -th draft pick: 



**22** A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management 



In the following, we explain in details each component of this integer optimization model. 

- The objective function aims to win as many head-tohead matchups as possible during the weekly play and playoff phases [the terms associated with λ1 and λ2 in (1a)], as well as to maximize the total number of fantasy points scored throughout the season (the term associated with λ0), where _zt_ ’s are indicator variables modeled in constraint (1f). The weights λ0, λ1, λ2 will be obtained from the calibration phase discussed in Section 6. Briefly speaking, the available evaluation data is divided into a training period and a validation period. The training period is used to search the parameter space and select the parameter values. The final parameter choice is then used in the validation period. 

- Constraint (1b) restricts that, up to the _k_ ̅-th pick, the DM can only pick no more than _k_ ̅ − _k_ players from the top α · ( _nk_ − _nk_ ) players ranked in the list _Rk_ . This essentially defines an uncertainty set for the opponents’ possible draft selections between the DM’s _k_ -th and the _k_ ̅-th picks, and makes the DM’s future drafts robust to any variation of the opponents’ picks within this uncertainty set. The parameter α ≥ 1 can be used to control the conservativeness of the DM’s drafting decision, with larger α implying a more risk-averse attitude on the DM’s side. 

- Constraint (1c) requires that the DM drafts a certain number of players γ _j_ in position _j_ . For example, the DM may want to draft at least five wide receivers to prepare for bye weeks and possible injuries, although only three wide receivers can be started at any given week. 

- – Constraint (1d) enforces the upper bound on the number of players of a given position _j_ that the DM’s team can start in any week _t_ . 

- Constraint (1e) imposes the logic relation that the DM can only start a player in week _t_ who has been drafted on her roster. 

- Constraints (1g)–(1h) specify the existing drafting results of which players have already been taken by the opponents and by the DM’s team. 

It is important to note that due to the special structure of this IP, we can relax the binary constraints on the variables<sup>_x_</sup> _it_<sup>and assume without loss of generality that</sup><sup>_x_</sup> _it_<sup>are</sup> continuous between 0 and 1. This leads to a mixed-integer program (MIP). Since there are in total approximately 620 offensive players and defensive teams in the NFL and 17 weeks in a season, this MIP formulation has about 640 integer variables (without relaxation on<sup>_x_</sup> _it_ , there would be more than 11,000 binary variables), 10,550 continuous variables, and 10,700 linear constraints. Also notice that, as the draft progresses, the number of fixed _yj_ increases, therefore the number of unknown variables decreases. As shown in our computational experiments, this MIP can be solved very fast within a minute on a normal laptop, and accelerates as the draft progresses. 

Using the above MIP model, the draft selection algorithm works as follows. At the DM’s _k_ -th draft pick, the DM solves the above MIP problem (Draft _k_ ). Denote _k_ the optimal solution _yi_ as<sup>_y_</sup> _i_<sup>for each</sup><sup>_i_∈N. Define</sup> _Pk_ = { _i_ : _yik_ = 1, _i_ ∉DMPlayer( _k_ )} as the set of players that (Draft _k_ ) recommends that the DM should select as its _k_ -th draft pick, ( _k_ + 1)-th draft pick, …, _nD_ -th draft pick, where _nD_ denotes the total number of draft picks allowed for each owner. Of course, the DM only executes the selection for the current ( _k_ -th) draft pick (the other picks are modeled to help evaluate the impact of the choice at the current draft pick). Specifically, the DM selects the player _i_ ∈ _Pk_ with the highest ranking _Rk_ ( _i_ ) as her _k_ -th draft pick. The draft then moves on to the DM’s ( _k_ + 1)-th pick and repeats the same procedure. The draft selection algorithm is summarized in Algorithm 1. 

Note that the _f_ ( _i_ , _t_ ) is an internal metric that the estimation algorithm generates, while _Rk_ is a public signal; there is incidental correlation between the two but it is not direct. The above optimization model uses _f_ ( _i_ , _t_ ) in the objective. Once the optimal _y_<sup>_k_</sup> is found, the players are selected based on _Rk_ . The reason for such a procedure is 

**Algorithm 1:** Draft selection algorithm. 

|1:**for** _k_ =1, 2, ...,_nD_ **do**|
|---|
|2:   Solve the draft model (Draft_k_). Denote the optimal solution by<br>_k_<br>_i_<sup>_y_ for all</sup><sup>_i_ ∈ N</sup>|
|3:   Draft the newly selected player_ik_with the highest rank, that|
|is,_ik_ =arg max_i_ ∈ _Pk_ _Rk_(_i_).|
|4:  Update DMPlayer(_k_ +1)=DMPlayer(_k_)∪{_ik_}.|
|5:**end for**|



A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management **23** 

the following. The presumption of the model is that opponent owners are making their decision based on the public _Rk_ , and this is the behavior that the optimization model is robust to, by constraints (1b). Note that the DM only makes one pick each round. Picking based on _Rk_ ensures that, if the assumption on the uncertainty sets holds, the ultimate team the DM ends up with will be no worse than the anticipated team calculated in the _k_ -th round optimization. However, picking based on _f_ ( _i_ , _t_ ) would not ensure this. As an example, assume that the player with the highest _f_ ( _i_ , _t_ ) has a poor ranking in _Rk_ and the player best ranked in _Rk_ has the second highest _f_ ( _i_ , _t_ ). The _k_ -th round draft optimization (Draft _k_ ) anticipates that the DM can get both players by picking the player with high ranking in _Rk_ now and the other player with high _f_ ( _i_ , _t_ ) in a later round. However, if the DM picks based on _f_ ( _i_ , _t_ ), the player with high ranking in _Rk_ will certainly be drafted by opponent owners by the time the DM picks again. 

### **4.4   Weekly play and playoff phases: greedy algorithm** 

During the weekly play and playoff phases, we use a simple greedy algorithm to select the starting lineups. In particular, since we know which opponents the DM’s players and defensive teams face during that week, we select the starting lineup from the DM’s roster with the highest _f_ ( _i_ , _t_ ) by position. Throughout the season, we keep _f_ ( _i_ , _t_ ) updated using the new data available up to week _t_ . 

## **5  Estimating** **_f_ (** **_i_ ,** **_t_ ) and** β **(** **_t_ )** 

In this section, we propose a prediction method to estimate the weekly fantasy points _f_ ( _i_ , _t_ ) of a player or a defensive team _i_ in week _t_ , and fantasy points β( _t_ ) needed by the DM’s team to reasonably ensure a victory in week _t_ . 

Various websites publish expert opinions on players’ and teams’ performance. Such expert predictions incorporate valuable information about rookie players and roster changes, which is impossible to anticipate by historical data. However, a drawback of the expert prediction is that they are usually given in the form of total season points of a player or a team.<sup>7</sup> Since the objective of fantasy football 

> **7** Some websites provide weekly performance predictions at the start of a season, such as Yahoo! and www.accuscore.com. These data can be used in place of _f_ ̅( _i_ , _t_ ). However, they may not be easy to access and process. Furthermore, their accuracy may not be vetted. 

is to win weekly matchups, it is important to provide a methodology that estimates fantasy points of players and teams scored on a weekly basis. 

Since individual players and defensive teams all have relative strengths and weaknesses, and any particular player or defensive team will face a different opposing team from week to week, we propose an index _f_ ̅( _i_ , _t_ ) to capture the notion of innate ability of a player or defensive team, and use this index to allocate experts’ projections of fantasy points for the entire season to each week. Eventually, the weekly fantasy points _f_ ( _i_ , _t_ ) is given as 



where _g_ ( _i_ ) is the expert prediction of player _i_ ’s total fantasy points over an entire season. The index _f_ ̅( _i_ , _t_ ) can also be viewed as the prediction of “when” the player _i_ will score. In the following, we discuss in details the algorithm for estimating the index _f_ ̅( _i_ , _t_ ) and the procedure to obtain β( _t_ ). 

### **5.1  An algorithm for estimating** **_f_ (** **_i_ ,** **_t_ )** 

To estimate a player’s weekly performance, we assume that each offensive player _i_ has an innate talent for achieving each relevant fantasy statistic independent of his opponent, and we measure this as<sup>_u_</sup> _is_<sup>for each sta-</sup> tistic _s_ , such as passing/rushing touchdowns, passing/ rushing yards, fumbles, field goals, etc. Table 1 summarizes the offensive and defensive statistics used in the prediction. 

Similarly, we assume that every defensive team _j_ has an innate ability to defend against these statistics, _Ds_ denoted as _w j_ where _Ds_ stands for defense against statistic _s_ . The projection for the level of each statistic achieved by a player in a given week is the product of his innate ability and his opponent’s ability to defend. We use the product of the two competing statistics as a simple model to capture the first order interaction between the two matched up agents. For instance, if 

**Table 1:** Offensive and defensive statistics. 

|QB|Passing/rushing yards, passing/rushing touchdowns<br>interceptions, fumbles, 2-point conversions|
|---|---|
|RB/WR/TE|Receiving/rushing yards, receiving/rushing<br>touchdowns fumbles, 2-point conversions|
|Kicker|XPM, FGM by distance|
|Def team|Points allowed, sacks, turnovers, safeties, blocked<br>kicks|



**24** A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management 

Peyton Manning, the QB for the Indianapolis Colts, plays against the New York Jets in week 4, we would project him to pass for _u_ PeytonManningpassYards × _w_ JetsDpassYards yards in week 4. Then, _f_ (PeytonManning, 4) is calculated by adding the projected points for each statistic. 

Following the above idea, we use a two-step procedure to derive _f_ ̅( _i_ , _t_ ). In the first step, we estimate the offensive and defensive strength of each team for each _s Ds_ fantasy statistic, i.e. _uk_ and _wk_ for each team _k_ . To do this, we use a weighted average of historical performance with recent performance weighted more heavily as our data, and a least squares estimation as the methodology. In the second step, we compute the innate abilities of each offensive player for each fantasy statistic, i.e. _uks_ for each player _k_ . 

For each statistic, we know the aggregate achievement in each historical season. For example, the  Minnesota Vikings gave up 986 rushing yards in 2006. We also know which opponents each team faced in each season. To estimate the innate offensive and defensive abilities of each team _k_ , we would therefore like to solve the following systems in the least squares sense: 



where Oppτ( _k_ ) is the set of opponents that team _k_ faced in a historical season τ, and HS is the index set of the historical seasons, where, for example, τ = 0 indexes the season 1 year ago from the current season, τ = −1 for the season 2 years ago, etc. The quantity _HTks_ is the weighted historical total points that team _k_ achieved for statistic _s_ , calculated as _HTks_ = ∑ τ∈HS 2 τ _HTks_ ,τ , where _HTks_ ,τ is the total points that team _k_ achieved for statistic _s_ in the specific historical season τ. In a similarly way, we calculate _HTkDs_ for the weighted historical total points that team _k_ achieved for defensive statistic _Ds_ . 

Formally, we want to solve the following optimization problem: 



**Algorithm 2:** Alternating minimization algorithm. 

|1:**Initialization**:_t_ =0 and set<br>0<br>(<br>)<br>1<br>_Ds_<br>_j_<br>_w_<br>=for each defensive team_j_<br>and statistic_Ds_|
|---|
|2:**repeat**|
|3:   Solve the linear least-squares problem (4) over<br>_s_<br>_k_<br>_u_with fixed<br>(<br>) ,<br>_Ds_<br>_j_<br>_t_<br>_w_<br>using the Singular Value Decomposition (SVD).<br>Denote the solution as<br>+1<br>(<br>)<br>.<br>_s_<br>_k t_<br>_u_|
|4:   Solve the linear least-squares problem (4) over<br>_Ds_<br>_j_<br>_w_<br>with<br>fixed<br>+1<br>(<br>)<br>,<br>_s_<br>_k t_<br>_u_<br>using SVD. Denote the solution as<br>+1<br>(<br>)<br>.<br>_Ds_<br>_j_<br>_t_<br>_w_<br>|
|5:_t_←_t_ +1|
|6:**until**convergence criterion is met.|



This is a nonlinear least squares problem. However, we notice that the system of (2) and (3) is composed of bilinear terms in _u_ and _w_ . Therefore, for a fixed defensive _Ds_ multipliers _w j_ , (2) becomes a linear system in the offensive multipliers _uks_ and vice versa. Using this observation, we implement an alternating minimization algorithm for solving the nonlinear least squares problem (4), as outlined in Algorithm 2. 

The principle of alternating optimization has a long history, dating back to the early work of alternating projection methods for solving linear systems by Agmon (1954) and Motzkin and Schoenberg (1954). Our proposed method is also closely related to the hill-climbing method for solving bilinear optimization problems, which is used as the first-step in a cutting problem algorithm proposed by Konno (1976). Note that with one set of variables _Ds_ fixed (e.g. _w j_ ), the nonlinear least squares problem (4) becomes convex quadratic over the other set of variables (e.g. _uks_ ). 

The following argument shows that the proposed algorithm converges. Denote the objective function in (4) as _h_ ( _u_ , _w_ ). Then, the iterations indexed by _t_ of the algorithm generate a sequence of decreasing objective values as _h_ ( _u_<sup>_t_</sup> , _w_<sup>_t_</sup> )  ≥ _h_ ( _u_<sup>_t_</sup> , _w_<sup>_t_+ 1</sup> )  ≥ _h_ ( _u_<sup>_t_+ 1</sup> , _w_<sup>_t_+ 1</sup> ), due to the alternating minimization procedure. Since _h_ ( _u_ , _w_ )  ≥ 0, this decreasing sequence _h_ ( _u_<sup>_t_</sup> , _w_<sup>_t_</sup> ) is bounded from below. Therefore, by the monotone convergence theorem (see e.g. Rudin (1976)), { _h_ ( _u_<sup>_t_</sup> , _w_<sup>_t_</sup> )} converges. 

Of course, due to the nonconvex nature of the above optimization problem, we cannot guarantee global optimality of the convergent solution. However, for our data set, convergence is typically achieved within two or three iterations of the above algorithm, and _R_<sup>2</sup> values for the goodness-of-fit are very high around 0.999 across all estimation entries. Therefore, we believe the above simple algorithm is sufficient. 

Once we have obtained offensive and defensive multipliers for each team, we must estimate the innate ability 

A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management **25** 

of offensive players whom we could potentially draft. Again, for each historical season, we have aggregate data for every fantasy statistic as well as knowledge of what opposing teams each player faced. The multipliers for player _i_ ’s statistic _s_ are then given by: 



where _HTis_ is the weighted historical total points of statistic _s_ obtained by player _i_ , Oppτ( _i_ ) is the set of defensive teams that player _i_ played against in the historical season _Ds_ τ, and _w j_ is the defensive team _j_ ’s multiplier for defending against statistic _s_ , computed from the first step. 

Finally, the estimate of how much total fantasy points player _i_ will achieve in week _t_ is then 



where Opp( _i_ , _t_ ) is the opponent defensive team that player _i_ meets in week _t_ of the current season. 

### **5.2  Estimating** β **(** **_t_ )** 

The quantity β( _t_ ) represents the number of points that are needed by the DM’s team to reasonably assure a victory against its opponent owner in week _t_ . At the DM’s pick in each round _k_ , β( _t_ ) is re-estimated in the following way. We distinguish between the weekly play phase (Week 1 to Week 15) and the playoff season (Weeks 16, 17). For each week _t_ in the weekly play phase, the DM knows which opponent owner she will face before she solves the (Draft _k_ ) problem. She also has the current ranking of players _Rk_ . With this knowledge, we simulate the remaining draft from the current round by assigning players to each team according to the rank order _Rk_ . In this process, we skip over a pick for a particular opponent if one of the following holds: 1) that pick of position _j_ would put the opponent’s roster over PosLimit( _j_ ); 2) that pick would cause the opponent to reach PosLimit( _j_ ) and that player’s bye week is shared with assigned picks of that position, leaving the opponent without enough starters. Then, we calculate the sum of the _f_ ( _i_ , _t_ ) values over the starting lineup of the week _t_ opponent’s team with the highest ranking by _Rk_ . For the playoff phase, because we do not know in advance which opponent owner the DM’s team will play, to be robust, we calculate the projected fantasy points for each opposing owner in Weeks 16 and 17, then take the maximum point projection for any possible opponent. 

## **6  Model calibration and evaluation** 

To evaluate the MIP draft model and the estimation methodology, we conduct extensive numerical simulation using historical data. In the following, we discuss the data sources, the simulation engine that we created to simulate fantasy football seasons, and calibration techniques to deal with limited data for rookie players. Then, we present simulation results for 2007 and 2008 seasons. The performance of our model is very promising for both seasons. 

### **6.1  Data** 

There are numerous internet websites that provide extensive data on career statistics of nearly every player in professional football history, game-by-game statistics of each player going back to early or middle 1990’s, preseason ranking of each position, and many rankings for fantasy football. For the purpose of predicting players and defense team performance, we obtained data corresponding to the overall performance of individual players and NFL teams for the 2004–2007 NFL seasons, as well as performance for the 2008 season from Yahoo!<sup>8</sup> and NFL.<sup>9</sup> We also obtained preseason fantasy draft rankings for each position from expert articles. Furthermore, we obtained summary reports of actual owner draft behavior for several public fantasy contests for the 2007 and 2008 seasons. For simulation purposes, we obtained more detailed game-by-game box scores for each player of the 2007 and 2008 season. 

### **6.2  The simulation engine** 

To calibrate the model parameters and assess performance, we develop a simulation engine for the fantasy football problem. This engine simulates the draft, weekly play, and playoff phase on data available for the current or a historical season. We incorporate three aspects of variability: 

- (a) The DM’s draft order, 

- (b) Weekly head-to-head match-up schedule during the weekly play phase, 

- (c) Opposing owners’ draft picks. 

The first two aspects are known at the start of the draft phase, while the third is realized as the draft progresses. 

- **8** Data extracted from http://sports.yahoo.com/nfl/stats. 

> **9** Data extracted from http://www.nfl.com/stats/player. 

**26** A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management 

For each simulation trial, we assign the DM a uniform random order number between 1 and 10 to simulate a league of 10 owners. We then select one match-up schedule uniformly from all possible regular season phase schedules with the following characteristics: 

1. Each owner plays all other owners at least once, 

parameters: α = 1, γ _j_ = PosLimit( _j_ ) + 1, λ0 = 1, λ1 = 100, and λ2 = 150. In Section 6.5.1, we will study the performance of the model with an alternative choice of γ _j_ . In general, γ _j_ ’s are a parameter setting that can be calibrated according to the DM’s preference for buffering injury risk and accumulating tradeable assets. 

2. No owner plays another more than twice. 

The draft then proceeds as follows: 

- (1) When it is the DM’s turn to pick, use the Draft Selection Algorithm outlined in the Section 4.3. For this phase, we calculate _f_ ( _i_ , _t_ ) based on historical data available at the beginning of the simulation season. 

- (2) When it is an opponent’s turn to draft, examine each remaining player _i_ in order of descending rank in _Rk_ : 

   - If opponent already has enough players with the same position as _i_ to fill a starting lineup as well as a backup player for that position to cover bye week, opponent rejects player _i_ . 

   - Otherwise, accept or reject player _i_ based on the empirical probability that player _i_ was selected with a similar pick number in mock draft data. 

We also note that the γ _j_ values used in the DM’s model do not apply to the opposing teams in step (2). 

For each week in the weekly play phase, the DM starts the player on her roster with the highest _f_ ( _i_ , _t_ ). Opponents start the players playing this week whom the opponents drafted first for each position. Scores for the starting lineups are then given according to the actual historical performance of that week during the simulation season. At the end of the weekly play phase, the playoff phase schedule is constructed and simulated using the same dynamics. 

Each simulation trial was performed on a 1.5GHZ Pentium M 2GB RAM machine running AMPL-CPLEX 11.2, the first and second round of the draft consumed the most time, taking on average 42 seconds with the longest time observed being 75 seconds. The 13 subsequent draft rounds took under 30 seconds a piece on average. Data processing, weekly play, and playoff phases took in aggregate 10 seconds on average. 

### **6.3  Model calibration** 

For model calibration, we derived _f_ ( _i_ , _t_ ) from the 2004 to 2006 season data, the anticipated draft rankings _Rk_ ( _i_ ) using expert websites with 2007 draft ranking and then simulated performance on the 2007 season. This calibration allowed us to select the following values for 

### **6.4  Model evaluation** 

#### **6.4.1  2007 Simulation results** 

Simulating 300 trials with the final model construction, we obtained the following results shown in Figure 1. Recall that the top two owners are typically financially compensated with the first place owner receiving the largest reward. Thus, for 2007 our approach won its fantasy football league 16.7% of the time, coming in at least the second best at nearly 27.3% of the time. The average rank achieved was 4.60 whereas a uniform approach, using the same drafting methodology as our baseline opponents would be expected to yield an average rank of 5.5, achieving each rank 10% of the time. Therefore, this study finds that the probability of winning money using the IP drafting approach is statistically significantly higher than the baseline approach at the 99.75% confidence level. 

As an example, Table 2 shows the draft result of the DM’s team in a trial run and its performance in the 2007 season. In each pair of scores, the first one is the DM’s team’s fantasy points, and the second one is the opposing owner’s points. Again, this shows a specific example of using γ _j_ = PosLimit( _j_ ) + 1 in the model. Other γ _j_ values can be chosen according to the DM’s preferences. 

To assess the value added by considering each player’s ability to score points in a given week (projecting _f_ ( _i_ , _t_ )) rather than simply their overall point scoring ability (projecting _f_ ( _i_ )), we also simulated 300 trials in which 



<!-- Start of picture text -->
2007 Season performance<br>18%<br>16%<br>14%<br>12%<br>10%<br>8%<br>6%<br>4%<br>2%<br>0%<br><!-- End of picture text -->

**Figure 1:** The empirical distribution of the final ranks achieved by our model in 2007 season. 

A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management **27** 

**Table 2:** An example of the DM’s draft and its performance in the 2007 season (score format: DM – opponent) for weeks 1–17. 

|1|Peyton Manning|2||Chad Johnson||3|Marsh|awn Lynch|
|---|---|---|---|---|---|---|---|---|
|4|Donald Driver|5||Laveranues Coles||6|Warric|k Dunn|
|7|Denver Broncos|8||Alge Crumpler||9|Brando|n Jackson|
|10|Nate Kaeding|11||Jeff Wilkins||13|Derrick|Mason|
|13|New York Giants|14||Heath Miller||15|Brady|Quinn|
|Week|1<br>2|3|4|5|6|7|8|9|
|Score|104–84<br>110–100|107–91|112–45|79–28|32–75|131–64|47–116|87–75|
|Week|10<br>11|12|13|14|15|16|17||
|Score|65–73<br>60–90|99–84|64–72|66–62|76–40|109–95|102–90||



_f_ ( _i_ , _t_ ) was simply set to _g_ ( _i_ )/16 during non-bye weeks, where _g_ ( _i_ ) is the third-party expert prediction. Using this uniform method of calculating _f_ ( _i_ , _t_ ), we placed first or second only 15% of the time, see Figure 2. This study finds that using a weekly allocation increases our probability of winning money by a statistically significant amount at the 97.8% confidence level. 



#### **6.4.2  2008 Simulation results** 

For the 2008 season, we derived _f_ ( _i_ , _t_ ) from the 2004–2007 season data, the anticipated draft rankings _Rk_ ( _i_ ) using expert websites with 2008 draft ranking and then simulated performance on the 2008 season. The results are shown in Figure 3. Here we place first or second 20.7% of the time. The average rank achieved was 5.14, beating the baseline approach by a statistically significant amount at the 99.25% confidence level. 

#### **6.4.3  Distribution of projection accuracy** 

For the 2007 and 2008 seasons, the distribution of prediction error ( _f_ ( _i_ , _t_ ) − _f_<sup>*</sup> ( _i_ , _t_ )), excluding each player’s 

**Figure 3:** The empirical distribution of the final ranks achieved by our model in 2008 season. 

bye-week, is plotted in Figure 4, where _f_<sup>*</sup> ( _i_ , _t_ ) is the actual fantasy points obtained by player _i_ at week _t_ . 

On average, a player’s fantasy point score for each week is overestimated by 4.5 with _f_ ( _i_ , _t_ ). Recall that each _f_ ( _i_ , _t_ ) has been reweighed by the expert total season projections, so this suggests that experts tend to over predict players’ fantasy scoring abilities. The spread of the empirical distribution indicates that there is room to improve on the prediction method for _f_ ( _i_ , _t_ ). 

From Figure 4, we can see that much of the prediction error is driven by over-optimism in predicting points for skill position players. While predicting Kicker and 





<!-- Start of picture text -->
Prediction error<br>7%<br>6%<br>5%<br>4%<br>3%<br>2%<br>1%<br>0%<br><!-- End of picture text -->

**Figure 2:** The empirical distribution of the final ranks achieved by our model with just the 3rd party projection. 

**Figure 4:** The empirical distribution of prediction error _f_ ( _i_ , _t_ ) − _f_<sup>*</sup> ( _i_ , _t_ ) for the 2007 and 2008 seasons. 

**28** A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management 

**Table 3:** The average actual fantasy points (Avg points), i.e. average of _f_<sup>*</sup> ( _i_ , _t_ ) for each position, the mean absolute error (MAE) of prediction, i.e. average of | _f_ ( _i_ , _t_ ) − _f_<sup>*</sup> ( _i_ , _t_ )|, and the sample standard deviation (Std Dev) of the absolute error of prediction over the 2007 and 2008 seasons. 

||**QB**|**RB**|**WR**|**TE**|**K**|**DEF**|
|---|---|---|---|---|---|---|
|Avg points|10.92|7.46|6.56|4.72|7.18|8.00|
|MAE|8.18|6.77|5.70|4.61|3.64|5.18|
|Std Dev|5.67|9.32|4.22|3.39|2.66|3.91|



Defensive scoring is generally thought of as a more challenging endeavor, Table 3 shows that prediction errors for Kicker and Defensive scoring are actually smaller than QB, RB, and WR. This demonstrates that expert bias in wanting to predict the next breakout skill position player may be an overwhelming influence in prediction error. Based on the average actual fantasy points for each position as shown in the first row of Table 3, we can see that the relative prediction error for QB is in fact lower than RB, TE, and WR, and higher than Defensive and Kicker. 

### **6.5  Further discussions** 

In this subsection, we present further discussions on three relevant questions. The first one is to study the effect of the lower bounds on the number of drafted players for each position, i.e. γ _j_ in constraint (1c). The second one is a sensitivity analysis of the model performance with respect to the parameter α. The third one is to test the hypothetical case where all the owners have access to the actual performance data of that season, i.e. owners have perfect information. This would give an indication on how the performance of the proposed model is affected by the errors in the _f_ ( _i_ , _t_ ) forecast. All the following experiments have 300 simulation trials. 

#### **6.5.1  Choice of** γ _j_ 

In the proposed model (Draft _k_ ), constraints (1c) set the requirement that the DM at least drafts a certain number of players (or defensive teams) γ _j_ for each position _j_ . The actual values of the parameters in the (Draft _k_ ) model, including γ _j_ ’s, are calibrated using the 2004–2006 season data to achieve an optimized performance. The calibration selects γ _j_ = PosLimit( _j_ ) + 1 for all _j_ , which means that, for each position, the model will draft at least one more player than the number at that position required to fill the starting lineup. We would like to emphasize that other 

values of γ _j_ ’s can be chosen according to the DM’s preferences. For example, the following strategy also seems reasonable: select γ _j_ = PosLimit( _j_ ) + 1 for QB, RB, and WR, and select γ _j_ = PosLimit( _j_ ) for TE, Kicker, and Defense team. Figures 5 and 6 show the performance of the strategy of choosing γ _j_ for the years 2007 and 2008, respectively. For 2007, the new strategy achieves the first or second place with probability 28% and average ranking 4.53; for 2008, the new strategy achieves the first or second place with probability 20.3% and average ranking 5.11, both of which are close to the performance of the original strategy of γ _j_ = PosLimit( _j_ ) + 1 for all position _j_ . 

#### **6.5.2  Sensitivity on** α 

As explained in Section 4.3, the constraint (1b) for each draft round ensures the robustness of the DM’s draft selection against the uncertainty in the opponent owners’ drafting. The parameter α controls the degree of conservativeness of the DM’s assumption on how much the 



<!-- Start of picture text -->
2007 Season performance<br>20%<br>18%<br>16%<br>14%<br>12%<br>10%<br>8%<br>6%<br>4%<br>2%<br>0%<br>1 2 3 4 5 6 7 8 9 10<br>Ranking<br>Figure 5:  The empirical distribution of the final ranks achieved by<br>our model in 2007 season using γγ j = PosLimit( PosLimit( j ) + 1 for QB, RB, and + 1 for QB, RB, and  1 for QB, RB, and<br>WR, and γγ j = PosLimit( PosLimit( j ) for TE, K, and Def.<br>2008 Season performance<br>18%<br>16%<br>14%<br>12%<br>10%<br>8%<br>6%<br>4%<br>2%<br>0%<br>1 2 3 4 5 6 7 8 9 10<br>Ranking<br>Empirical probability<br>Empirical probability<br><!-- End of picture text -->

**Figure 5:** The empirical distribution of the final ranks achieved by our model in 2007 season using γγ _j_ = PosLimit( PosLimit( _j_ ) + 1 for QB, RB, and + 1 for QB, RB, and  1 for QB, RB, and WR, and γγ _j_ = PosLimit( PosLimit( _j_ ) for TE, K, and Def. 

**Figure 6:** The empirical distribution of the final ranks achieved by our model in 2008 season using γ _j_ = PosLimit( _j_ ) + 1 for QB, RB, and WR, and γ _j_ = PosLimit( _j_ ) for TE, K, and Def. 

A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management **29** 

**Table 4:** Sensitivity of α. 

|α|**Avg**|**Place 1st (%)**|**Place 1st or 2nd (%)**|**Place top half (%)**|
|---|---|---|---|---|
|1.0|4.60|16.7|27.3|64.7|
|1.1|4.76|15.3|23.0|62.7|
|1.2|5.06|10.0|19.7|58.3|
|1.3|5.07|12.0|24.7|55.7|
|1.4|5.09|12.7|20.3|57.3|
|1.5|5.38|12.0|21.7|52.7|



opponents could deviate from the publically available ranking _Rk_ at each round _k_ . The calibrated model has α = 1, which means the DM’s drafting model will assume the opponents draft according to _Rk_ in expectation. Here we provide a sensitive analysis on the performance of the model for different α’s. 

In Table 4, the second to the fifth columns are, respectively, the average rank achieved by the proposed model for different α’s, the empirical probability of coming in the 1st place, the empirical probability of placing in the first two places, and the probability of placing in the top half (top 5 in a league of 10 owners). Again, 300 simulation trials are conducted for each value of α. For α ≤  1.4, the probability of placing in the top half beats the baseline approach (50%) by a statistically significant amount above the 97.5% confidence level. 

From this figure, we can see that as α increases, the model behaves more conservatively, which results to a worse average achieved rank, and lower probability of winning top places. 

#### **6.5.3  Impact of perfect information** 

We have also tested the case where the owners have access to perfect information about the players and teams performance. In this case, the opponents draft according to a ranking list using the perfect information of the players’ performance. In particular, we use the 3rd party ranking as the overall ranking of players, and then the relative rankings for each position within the overall ranking list are ordered using the actual points. 

Even with perfect information on player performance, a fantasy sports draft still remains a challenging optimization problem due to the positional requirements of the roster and the varying week-to-week point production and opponent matchups. The simulation results are the following: Average achieved rank is 3.32, 24.7% of the time coming in the 1st place, and 15.0% the time coming in the 2nd place, therefore winning the league with 39.7% of the time. This represents a significant 

improvement in our model’s draft performance emphasizing both the ability of our model to improve drafting decisions and the challenge that forecast error creates in this problem. 

## **7   Conclusion and possible extensions** 

The proposed mixed-integer programming based method for draft selection outperforms the baseline strategy of using publicly available expert rankings by a statistically significant margin under simulation. Planning for the weekly matchups that NFL players will face rather than their overall fantasy point scoring ability was also found to increase the likelihood of winning. We feel that this method would perform well in fantasy football league play against real-life opponents by providing a quantitative edge; however there are still several aspects of the model that could be improved through future research. Future work directions could include the following extensions: 

1. As seen in the Section 6.4.3, it may be possible to improve upon the prediction methodology used or to improve results buy purchasing expert 3rd party weekly predictions for players’ fantasy points. Grouping players’ forecast points into tiers and assigning all players in the same tier the cluster average may highlight the significant differences in forecast points and help improve the performance of the model. 

2. Given a methodology for projecting _f_ ( _i_ , _t_ ), we can observe the distribution of historical prediction error for players in various classes. This empirical distribution could be used to create an uncertainty set around _f_ ( _i_ , _t_ ). Stochastic or robust optimization counterparts to our model could then be evaluated. 

3. A significant source of uncertainty in fantasy football is player injuries. If the DM drafts a player that is subsequently injured, the DM would receive no points for starting that player on a week in which they are sitting out due to injury. We could incorporate a robust formulation where an adversary is allowed to pick one or more of our players to injure for the season, ensuring that we do not rely too heavily on the point contributions of a few key players that may be injured. 

4. The calculation of β( _t_ ) may be improved. In particular, there is room for a possible model extension by solving an auxiliary optimization problem to maximize β( _t_ ) for the opposing owner’s team in round _t_ over the same pick uncertainty set described in Sections 4.3, or 

**30** A. Becker and X.A. Sun: An analytical approach for fantasy football draft and lineup management 

   - to incorporate such β( _t_ ) maximization into our model using robust optimization techniques. 

5. Mid-season free agency and trades: During the weekly play phase, it is also often permitted to trade players with opposing owners, drop players from our roster, and add players to our roster who are not currently on any other owner’s roster. The existing model can be easily extended to reoptimize our roster in each week incorporating to-date performance. To evaluate this strategy, simulation rules for free agency for opposing owners would have to be developed. 

- Fry, M. J., A. W. Lundberg, and J. W. Ohlmann. 2007. “A Player Selection Heuristic for a Sports League Draft.” _Journal of Quantitative Analysis in Sports_ 3. 

- Gibson, M. R., J. W. Ohlmann, and M. J. Fry. 2010. “An Agent-based Stochastic Ruler Approach for a Stochastic Knapsack Problem with Sequential Competition.” _Computers & Operations Research_ 37:598–609. 

- Harville, D. 1980. “Predictions for National Football League Games via Linear-model Methodology.” _Journal of the American Statistical Association_ 75:516–524. 

- Konno, H. 1976. “A Cutting Plane Algorithm for Solving Bilinear Programs.” _Mathematical Programming_ 11:14–27. 

Kvam, P. and J. Sokol. 2006. “A Logistic Regression/Markov 

- Chain Model for NCAA Basketball.” _Naval Research Logistics_ 53:778–803. 

## **References** 

Agmon, S. 1954. “The Relaxation Method for Linear Inequalities.” _Canadian Journal of Mathematics_ 6:383–392. 

- Berri, D. J. and R. Simmons. 2011. “Catching a Draft: On the Process of Selecting Quarterbacks in the National Football League  amateur draft.” _Journal of Productivity Analysis_ 35:37–49. 

- Brown, M. and J. Sokol. 2010. “An Improved LRMC Method for NCAA Basketball Prediction.” _Journal of Quantitative Analytics in Sports_ 6:1–23. 

- David, J. A., R. D. Pasteur, M. S. Ahmad, and M. C. Janning. 2011. “NFL Prediction Using Committees of Artificial Neural Networks.” _Journal of Quantitative Analysis in Sports_ 7. 

- Massey, C. and R. H. Thaler. 2013. “The Loser’s Curse: Decision Making and Market Efficiency in the National Football League Draft.” _Management Science_ 59:1479–1495. 

- Motzkin, T. and I. J. Schoenberg. 1954. “The Relaxation Method for Linear Inequalities.” _Canadian Journal of Mathematics_ 6:393–402. 

- Reid, M. 2003. _Least Squares Model for Predicting College Football Scores_ . Master’s thesis, University of Utah. 

- Rudin, W. 1976. _Principles of Mathematical Analysis_ . McGraw-Hill Higher Education. 

- Summers, A. E., T. B. Swartz, and R. A. Lockhart. 2007. _Statistical Thinking in Sports_ . Chapman and Hall/CRC, chapter Optimal Drafting in Hockey Pools. 

- Young, W. A. 2010. _A Team-Compatibility Decision Support System to Model the NFL Knapsack Problem: An Introduction to HEART_ . Ph.D. thesis, Ohio University. 


