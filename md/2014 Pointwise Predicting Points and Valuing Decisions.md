<!-- source: 2014 Pointwise Predicting Points and Valuing Decisions.pdf -->



# **POINTWISE:** 

# **Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data** 

Dan Cervone<sup>†</sup> , Alexander D’Amour<sup>†</sup> , Luke Bornn<sup>†</sup> , and Kirk Goldsberry<sup>‡</sup> Department of Statistics<sup>†</sup> and Institute for Quantitative Social Science<sup>‡</sup> Harvard University Cambridge, MA, USA, 02138 Email: dcervone@fas.harvard.edu 

## **Abstract** 

Basketball is a game of decisions; at any moment, a player can change the character of a possession by choosing to pass, dribble, or shoot. The current state of basketball analytics, however, provides no way to quantitatively evaluate the vast majority of decisions that players make, as most metrics are driven by events that occur at or near the end of a possession, such as points, turnovers, and assists. We propose a framework for using player-tracking data to assign a point value to each moment of a possession by computing how many points the offense is expected to score by the end of the possession, a quantity we call expected possession value (EPV). EPV allows analysts to evaluate every decision made during a basketball game – whether it is to pass, dribble, or shoot – opening the door for a multitude of new metrics and analyses of basketball that quantify value in terms of points. In this paper, we propose a modeling framework for estimating EPV, present results of EPV computations performed using playertracking data from the 2012-13 season, and provide several examples of EPV-derived metrics that answer real basketball questions. 

## **A new microeconomics for the NBA** 

Basketball players, coaches, and fans often compare a possession to a high-speed chess match, where teams employ tactics that do not necessarily generate points immediately, but can yield higher-value opportunities several “moves” down the line. Watching the game in this way can reveal that the decisive moment in a given possession may not have been the open shot at the end, but the pass that led to the open shot, or even the preceding drive that collapsed the defense. These ideas lie at the heart of offensive strategies and the decisions that players make over the course of a possession. 

Unfortunately, contemporary basketball analytics fail to account for this core idea. Despite many recent innovations, most advanced metrics (PER [1] and +/- variations [2], for example) remain based on simple tallies relating to the terminal states of possessions like points, rebounds, and turnovers. While these have shed light on the game, they are akin to analyzing a chess match based only on the move that resulted in checkmate, leaving unexplored the possibility that the key move occurred several turns before. This leaves a major gap to be filled, as an understanding of how players contribute to the whole possession – not just the events that end it – can be critical in evaluating players, assessing the quality of their decision-making, and predicting the success of particular in-game tactics. The major obstacle to closing this gap is the current inability to evaluate the individual tactical decisions that form the substructure of every possession of every basketball game. For example, there is no current method to estimate the value of a dribble penetration or to compare the option of taking a contested shot to the option of passing to an open teammate. 

In this paper, we propose and implement a framework that removes this obstacle. Using player-tracking data, we develop a coherent, quantitative representation of a whole possession that summarizes each moment of the possession in terms of the number of points the offense is expected to score – a quantity we call _expected possession value_ , or EPV (see Figure 1 for an illustration of EPV). We accomplish this by specifying and fitting a probabilistic model that encodes how ball handlers make decisions based on the spatial configuration of the players on the court. 



2014 Research Paper Competition Presented by: 







**Figure 1.** Diagram of EPV as a weighted average of the values of the ballcarrier's (Leonard's) decisions and the probability of making each decision. We also consider the possibility of Leonard dribbling to a different area or driving toward the basket, as well as turning the ball over, but these are omitted from the above diagram for conceptual clarity. 

EPV assigns a point value to every tactical option available to a player at each moment of a possession, allowing analysts to evaluate each decision that a player makes. For example, passing to a wide open shooter in the corner or near the basket is worth more expected points than to a covered player in a similar place. EPV thus opens up new avenues of basketball analysis that focus on decision-making, opportunity creation and prevention, and optimal responses that were not possible before. Just as the notion of utility made quantitative analysis of everyday decisions possible in microeconomics, we believe EPV lays the foundation for quantitative decision analysis in the NBA. 

This paper has four parts<sup>1</sup> . In Part 1, we give a brief overview of the possession model we use to compute EPV. Part 2 showcases the raw results of our EPV computations using our current specification of the possession model, showing how EPV changes in real time as a possession unfolds. Part 3 introduces several examples of how EPV can be used to answer real basketball questions. These examples are in no way an exhaustive list, but should be instructive of how wide-reaching EPV can be as a framework for basketball analytics. Finally, in Part 4, we discuss how EPV-based analysis can be extended in future work. 

## **1   Computing EPV with a possession model: What happens next?** 

EPV is a conditional expectation – the expected number of points the offense will score, given the spatial configuration of the players and ball at time during the possession ): 

#### [ ] 

By definition, the current EPV of a possession is the weighted average of the outcomes of all future paths that the possession could take. Calculating this requires a model that defines a probability distribution over what the ballhandler is likely to do next, given the spatial configuration of the players on the court, as we need to understand what future paths the possession can take and how likely they are given the present state. We call this model the 

> 1 Because optical tracking data has been presented several times at the Sloan conference, we have placed a description of the data in the appendix. 





2014 Research Paper Competition Presented by: 

2 



_possession model_ . Using a Markovian assumption<sup>2</sup> , the possession model allows us to estimate both (a) the probability that a player will make a particular decision in a given situation and (b) the resulting EPV of the possession after the player makes that decision. Taken together, we learn both how valuable any moment in a possession is, as well as the features of the offense's configuration that produce this value. For an illustration of this breakdown of EPV, see Figure 1. 

Our possession model breaks down a player's options into discrete actions that may take several seconds to complete (e.g., passing or shooting) or continuous actions that evolve instantaneously (e.g., moving to the left or right). We call the former actions _macrotransitions_ and the latter actions _microtransitions_ . Using this breakdown, we can rewrite EPV at time during a possession by conditioning on the ballhandler's next action during a small time window ( ): 

#### )  [ ]  [                      ] ]                 ] ) ) [                      ] ]                 ] ) 

In our current implementation, we define passes, shots, and turnovers as macrotransitions, and all movements that players make with the ball as microtransitions. However, if one were able to identify additional spatiotemporal motifs, either by algorithmic sophistication or the input of coaches or players, it would be possible to incorporate other actions such as drives to the hoop as additional macrotransitions. 

The macro/microtransition dichotomy facilitates calculating components of (1) using statistical models. The macrotransition probabilities                  ] ) (e.g., the instantaneous probability that a player will pass or shoot the ball) respond to the full-resolution spatial configuration of the players, and are therefore the most nuanced components. We compute these using competing risks, a statistical framework for modeling the occurrence of discrete events in continuous time [3, 4], incorporating situational covariates (e.g., presence of defender between player and teammate), and spatially-smoothed random effects that capture individual players' tendencies [5]. We compute [                       ] ] by modeling a coarsened version of the court space as a homogeneous Markov chain (a common technique in baseball [6] and football [7]). We compute the final components in (1), based on microtransitions, from the macrotransition components and some basic mathematical assumptions of local space-time smoothness. 

The exact specification and technical details for fitting our possession model for each player in the NBA are beyond the scope of the paper, and are the subject of a forthcoming statistical article. Indeed, one major challenge of using data sets as large and rich as optical tracking data is implementing statistical models that are flexible enough to incorporate subtle spatial patterns in players' tendencies while being robust enough to avoid overfitting the occasional abnormal behavior we observe – the Dwight Howard corner 3, for instance. Standard techniques such as regression, analysis of variance, and generalized linear models are ill-suited to these problems. The competing risk models we use to estimate decision probabilities in different situations respond to small but meaningful changes in the data space, such as the ball carrier's exact location on the court and the positions of the defenders relative to his passing options. However, the sophistication of such models carries a heavy computational cost – using cutting-edge algorithms [8, 9], our possession model still requires several hours to fit using hundreds of processors and over 4 terabytes of memory. 

For simplicity, in the analyses that follow, we focus on half-court possessions and ignore fouls. 

## **2   Summarizing possessions with EPV: The possession stock ticker.** 

Because EPV is calculated continuously throughout the possession and depends on the full-resolution spatial data, it is in constant motion as the possession unfolds. Much like the share price of a publicly traded company, EPV represents the value or stock of a possession and may respond dramatically to major events (an unexpected pass or a shot attempt), while remaining more steady the rest of the time. 

> 2 We assume that the decision the ballhandler makes depends only on the current spatial configuration of the possession. Markovian models for the purposes of computing win probabilities or run values have been proposed in American football and baseball analytics, but our application of these ideas to basketball, and indeed any continuous-time continuous-space sport, is novel. 





2014 Research Paper Competition Presented by: 

3 





**Figure 2.** EPV throughout the Spurs' final possession, with annotations of major events. 

In fact, plotting out the EPV graph of a particular possession reveals the moments that move EPV most drastically. Consider the following possession from the Spurs/Cavaliers game on February 13, 2013. Down by 2 with less than 10 seconds left, the Spurs inbounded to Tony Parker, who drove to the basket, drawing defenders into the paint and leaving Kawhi Leonard wide open in the corner. Instead of attempting the tightly contested layup that would tie the game, Parker dished to a wide-open Leonard, who promptly sank the game-winning 3-pointer, almost unchallenged by the defense. While Leonard's 3-pointer was this possession's (and game's) “checkmate”, we see from Figure 2 how valuable Parker was in setting it up. Parker actually dramatically increased the value of the possession twice – first by driving towards the basket, and then by passing to Leonard. 

Contrast this curve to the boxscore summary of the play. Parker would be credited with an assist but not with the preceding drive, and worse yet, if Leonard were to miss the shot, the whole play would go unrecorded. The EPV view, on the other hand, gives a continuous summary of the whole possession, and is unaffected by the noise in downstream events – in this case, if Leonard were to miss the shot, Parker would still be credited with the same EPV contributions. In this way, the EPV curve in Figure 2 acts like a stock ticker in providing an instantaneous snapshot of the offense's value (and perhaps also the spirits of Spurs fans watching the game). Much as financial economists analyze the movement of stock prices to gain insight on the strategy and behaviors of firms and investors, basketball analysts can use the EPV framework to learn and evaluate players' actions throughout the entirety of their court time. 

## **3   Answering questions with EPV: Introducing EPVmetrics.** 

In addition to providing a quantitative lens through which we can analyze entire possessions, metrics derived from EPV can provide precise answers to a number of fundamental basketball questions. We list several questions and the EPV-derived metrics that can be used to answer them in this section. 

### **3.1   EPV-Added: Does Chris Paul make better decisions than the league-average player?** 

The clearest application of EPV is quantifying a player's overall offensive value, taking into account every action he has performed with the ball. We can use EPV to collapse all of a player's actions onto a single interpretable scale (in this case, points) while placing the player's value in context (namely, the offensive role he fills on his team). One way to compute a player's value is to ask how much EPV he adds in the situations where he handles the ball compared to a hypothetical player that could replace him<sup>3</sup> . 

> 3 It is tempting to aggregate the change in EPV every time a player makes a decision with the ball as a measure of a player's value, as we did when analyzing Parker's contribution to the possession discussed earlier. However, much like residuals in a linear regression, the sum of EPV changes that a player makes is zero by definition; we can't expect the team to score points if we know later in the possession we'll expect them to score more than points. 





2014 Research Paper Competition Presented by: 

4 



In this case, we compare the player of interest to the league-average player formed by combining every other player's decision tendencies given the same situations. This allows us to track a player's _replacement-level EPV_ ( ) alongside the player of interest's EPV, and difference these two quantities to obtain the player's instantaneous EPV over replacement at any point in time (     ) )). When ) )  , we predict he will make higher-value decisions than the league-average player in the same situation faced at time . Combining these differences in      ) ) across that player's touches for an entire season, we measure the extent to which he systematically outperforms a league-average player in terms of the value of his decisions given his options – a quantity we call _EPV-added over replacement_ (EPVA)<sup>4</sup> : 

#### ) ) { } ∑ 

Of all NBA players in 2012-13, Chris Paul had the highest EPVA at +3.48 per game. Figure 3 illustrates a particular play during which Paul accrues high EPVA. When Paul first touches the ball, he is at the top of the arc without any noteworthy passing options. The EPV at this instant is slightly higher than the assuming a league-average player in Paul's shoes; Paul is more valuable in this situation because he is an above-average shooter from this range and has the ability to penetrate the defense and drive toward the basket. Paul does indeed drive to the basket on this play, and at the end of this possession when Paul shoots, the EPV is very high (1.59) and well above (1.28) since Paul is very efficient near the basket. Of course, the hypothetical league-average player may not have driven to the basket the same way Paul did during this possession, so to compute the contribution to Paul's EPVA from this play we compare the EPV at the end of the play to the at the start of the touch, netting Paul about +0.65. 

Ricky Rubio had the lowest EPVA during 2012-13 at -3.33 points per game. Figure 4 illustrates a possession that contributes negatively to Rubio's EPVA. Rubio gains possession of the ball in the restricted area, closer to the basket than to any defender. This is a high situation (1.57) because the league-average player is likely to take a shot in this situation and make it, but for Rubio, this is a low EPV situation (0.84) because he, too, has a strong propensity to take this shot but his shooting percentage in this situation (restricted area, unguarded) is much worse. In this possession, Rubio wisely decides to pass the ball to Derrick Williams, yielding a slight increase in EPV, but compared to the high-percentage shot that most players would have taken in this situation, the pass to Williams resulted in a far less valuable opportunity. As a result, Rubio accrues a negative EPVA (-0.66) for this play. 

In Table 1 in the appendix, we provide a list of the top and bottom 10 EPVA players in the league, according to our current implementation of the possession model. Generally, players with high EPVA are able to take advantage of the situations they face better than the rest of the league by fully utilizing the court space that they occupy and taking advantage of the characteristics of their teammates. Players with low (negative) EPVA are not necessarily “bad” players in any conventional sense; their actions simply tend to lead to fewer points than other players given the same options – negative EPVA is most easily accrued by taking low-probability 2-point shots and by turning the ball over. 

### **3.2   Shot Satisfaction: Is Carmelo Anthony a selfish shooter?** 

Players who take a large proportion of their team's shots or pass infrequently are often labeled “selfish” shooters. The implication is that selfish shooters care more about their personal point totals than the team's point total; however, some players might generally face fewer passing options during their shot opportunities, or passing options not as valuable as a shot attempt. Before we label somebody a selfish shooter due to his shot and pass tallies, we should consider his options when deciding to shoot or pass – it may very well be the case that his decisions were best for the team (as well as for his own stat-padding). 

We can quantify the value of shot attempts relative to passing options by calculating players' _shot satisfaction_<sup>_5_</sup> . To do this, at every time a certain player takes a shot, we subtract the EPV conditional on a pass having happened instead at time from the realized      ), which assumes the shot: 

> 4 The notion of contrasting a player's contributions against a meaningful baseline is central to the metric Wins Against Replacement (WAR), most fully developed in baseball [10]. Like baseball's WAR, EPVA is also useful in collapsing all of a player's actions to an interpretable scale (points for EPVA, wins for WAR). Note, however, that the definition of a replacement player in the construction of WAR is different from our usage here, where we consider a league-average player. 

> 5 When talking about the utilities (costs) of various decisions, it's customary to define the _regret_ of a realized decision versus the various alternatives. We take a more optimistic approach by considering satisfaction instead. 





2014 Research Paper Competition Presented by: 

5 



#### )  [                      ] ] ∑ 

The rightmost term in the above equation is a byproduct of the macrotransition model used in computing EPV. Averaged over their full seasons, the vast majority of NBA players have positive shot satisfaction, which makes sense as players are taught to shoot only when they think it gives their team the best chance to score on that possession. Carmelo Anthony, often labeled as a selfish shooter, averages +0.053, meaning that we expect the team to score 0.053 more points for an Anthony shot attempt than had he passed the ball instead. Carmelo's shot satisfaction is at the 22% quantile of player scores, meaning more than 1 in 5 players are objectively more “selfish” in their shot selections. 

The players with the top and bottom 10 mean shot satisfaction scores over the course of the season are given in Table 2 in the appendix. Generally, players register high shot satisfaction when they take shots in areas in which they are effective shooters, and when they are not being contested by the defense. If a player's teammates are not good scorers, it is easier for him to accrue shot satisfaction, all else being equal. Similarly, players with low or negative shot satisfaction take low-probability shots (either tightly contested or in a disadvantageous area of the court) or frequently ignore teammates with open looks at the basket. 

### **3.3   Other EPV-derived metrics** 

EPVA and shot satisfaction are just two examples of question-driven metrics that can be derived from EPV. Other questions that EPV-derived metrics can answer include: (a) what value we might expect to get by replacing one player with another, for example through a trade, by computing EPVA with respect to a particular player rather than the league average, (b) whether a player is a “selfish assister” by computing pass satisfaction analogously to the shot satisfaction discussed above, (c) how to identify the player who best set up a basket by developing analogs to the assist, and (d) how to design a defense that consistently shuts off the highest EPV options to systematically lower an opponent's EPV. 

## **4   Discussion and the future of EPV** 

In this paper, we proposed the EPV framework as a novel paradigm for basketball analytics that is congruent with the flowing nature of the sport and overcomes many shortcomings of the conventional boxscore approaches to analyzing the game. We have shown that emerging forms of player-tracking data not only allow us to expand upon conventional approaches to analyzing the game (e.g. tallying touches, dribbles etc.), but when combined with contemporary statistical modeling and computation, afford an exciting opportunity to develop new modes of analysis to answer questions that have been inherent to basketball since its inception, but would have been impossible to answer even a few years ago. 

The implementation of EPV estimation we have laid out in this paper can be extended with future work. For instance, additional macrotransitions such as pick-and-rolls or drives to the basket could be added to make estimates more responsive to set plays that an offense runs. More generally, coaches and team managers can tweak the EPV model to reflect particular schemes their players and team run – in theory, our model loses efficiency in estimating EPV by regarding players' decisions as Markovian when their actions in fact execute a carefully designed sequence. However, because we have specified EPV in terms of a probability model, the procedure to implement these extensions is clear. 

Because player-tracking cameras were only installed in half of the league's arenas in 2012-13, we observe only away games for roughly half of the players, and primarily home games for the others.  The resulting biases in our player comparisons will disappear in the future as player-tracking data is now available for all arenas in the current season. 

Despite these limitations, we assert that most questions that coaches, players, and fans have about basketball, particularly those that involve the offense, can be phrased and answered in terms of EPV. Indeed, we believe that EPV is not only useful for providing answers, but that it also helps us form questions that are well-posed in terms of the game's most fundamental quantity – points. More generally, we believe that this question-driven approach to analytics, which prioritizes coherence and interpretability over analytical ease, provides a template for growing the footprint of the sports analytics community and turning next-generation sports data into next-generation sports intelligence. 





2014 Research Paper Competition Presented by: 

6 



## **Acknowledgements** 

The authors would like to thank STATS LLC for providing us with the optical tracking data, as well as Edo Airoldi, Carl Morris, Alex Franks, Andy Miller, and Natesh Pillai for extremely valuable input throughout the course of this project. 

## **References** 

[1] J. Hollinger. _Pro basketball forecast 2004-05_ . Brassey’s, Washington, 2004. [2] D. Omidiran. A new look at adjusted plus/minus for basketball analysis. _MIT Sloan Sports Analytics Conference 2011_ , 2011. 

[3] D. Cox. The analysis of exponentially distributed life-times with two types of failure. _Journal of the Royal Statistical Society, Series B_ , 21(2):411–421, 1959. 

[4] R. Prentice, J. Kalbfleisch, A. Peterson Jr., and N. Flournoy. The analysis of failure times in the presence of competing risks. _Biometrics_ , 34(4):541–554, 1978. 

[5] Brian D Ripley. _Spatial statistics_ , volume 575. Wiley. com, 2005. 

[6] T. Tango. _The Book: playing the percentages in baseball_ . Potomac Books, Washington. 

[7] K. Goldner. A Markov model of football: Using stochastic processes to model a football drive. _Journal of Quantitative Analysis in Sports_ , 8(1), 2012. 

[8] H. Rue, S. Martino, and N. Chopin. Approximate Bayesian inference for latent Gaussian models by using integrated nested Laplace approximations. _Journal of the Royal Statistical Society, Series B_ , 71(2):319–392, 2009. [9] F. Lindgren, H. Rue, and J. Lindström. An explicit link between Gaussian fields and Gaussian Markov random fields: the stochastic partial differential equation approach. _Journal of the Royal Statistical Society, Series B_ , 73(4):423–498, 2011. 

[10] S. Smith. WAR  explained. http://www.baseball-reference.com/about/war_explained.shtml. 

[11] A. Miller, L. Bornn, R. Adams, and K. Goldsberry. Factorized point process intensities:  A spatial analysis of professional basketball. Forthcoming in _Proceedings of the 31_<sup>_st_</sup> _International Conference on Machine Learning_ , 2013. 

[12] K. Goldsberry and E. Weiss. The Dwight effect: A new ensemble of interior defense analytics for the NBA. _MIT Sloan Sports Analytics Conference 2013_ , 2013. 

## **Appendix** 

### **SportVU Optical Tracking Data** 

Optical tracking data for this project were provided by STATS LLC from their SportVU product. The data are composed X- and Y- coordinates for each of the ten players and three referees on the court, in addition to X-, Y-, and Z-coordinates for the ball. The data also include annotations for moments where players take possession of the ball, and events like dribbles, passes, shots, and fouls. In recent years, SportVU data have been used to perform spatial analyses of basketball [11, 12], although these have focused on shot events. 

We performed the example analyses in this paper with data from the 2012-13 NBA regular season. During this time, data were only available from 13 arenas in the NBA: Cleveland, Milwaukee, New York, Orlando, Philadelphia, Toronto, and Washington in the East, and Dallas, Golden State, Houston, Minnesota, Phoenix, and San Antonio in the West. Because of uneven SportVU coverage, some teams were only observed in a small number of games. This sampling bias is a major concern for the example analyses performed in this paper. However, beginning with the 2013-14 season the NBA installed SportVU cameras in every team's arena, making thse concerns about sampling bias irrelevant for analyses in future seasons. 





2014 Research Paper Competition Presented by: 

7 



### **Additional Figures** 





**Figure 3.** A high EPVA play for Chris Paul. On each plot, the black dot on the EPV scale represents the current EPV and the gray dot is the EPV with league average player in place of Chris Paul ( ). The horizontal lines are proportional to the probability of each of the 4 possible pass events, a made/missed shot event, or a turnover occurring in the next time window. Black/solid lines represent Paul's probabilities, and grey/pastel lines represent the league average player's probabilities. Paul's EPVA for this play is +0.65, which is obtained by subtracting the at the beginning of the touch (gray dot on the left figure) from the (player-specific) EPV at the end of the touch (the black dot in the right figure). 





**Figure 4.** A low EPVA play for Ricky Rubio. EPV actually increases during this play, yet EPVA is still negative (-0.66) since the higher EPV at the end of the play is still much lower than the at the start of the play. We estimate a league-average player to be considerably more valuable than Rubio when placed in Rubio's shoes at the start of this touch due to the fact that Rubio is a below-average shooter near the basket. 





2014 Research Paper Competition Presented by: 

8 



## **Tables** 

**Table 1.** Top 10 and bottom 10 players by EPV-added (EPVA) in 2012-13 (per game, minimum 100 touches during season). Because of limited SportVU coverage in the 2012-13 season, some players in these tables were only observed for a small number of games despite having enough touches to be included. For example, Chris Paul (ranked 1st) and LeBron James (ranked 23rd, not shown) were only observed in away games, for 11 and 17 games, respectively. In these games Paul shot 54% compared to his season average 48%, while James shot for 50% in our data compares to his season average 57%. This sampling bias accounts for some anomalies in this ranking, which could be eliminated by considering the 2013-14 season's complete data. 

|**Player**|**EPVA**|**Player**|**EPVA**|
|---|---|---|---|
|Chris Paul|3.48|Ricky Rubio|-3.33|
|Dirk Nowitzki|2.60|Kevin Love|-2.38|
|Deron Williams|2.52|Russell Westbrook|-2.07|
|Stephen Curry|2.50|Evan Turner|-1.90|
|Jamal Crawford|2.50|Austin Rivers|-1.84|
|Greivis Vasquez|2.46|Rudy Gay|-1.75|
|LaMarcus Aldridge|2.40|Jrue Holiday|-1.51|
|Steve Nash|2.09|Paul George|-1.49|
|Wesley Matthews|2.06|Chris Singleton|-1.48|
|Damian Lillard|1.95|RoyHibbert|-1.44|



**Table 2.** Top 10 and bottom 10 players by average shot satisfaction in 2012-13 (per shot attempt, minimum 500 touches during season). The sampling bias concerns noted in Table 1 apply to these results as well. 

|**Player**|**Shot Satisfaction**|<br>**Player**|**Shot Satisfaction**|
|---|---|---|---|
|Lance Stephenson|0.362|Alonzo Gee|-0.098|
|Steve Nash|0.340|Daniel Gibson|-0.082|
|Pablo Prigioni|0.335|Ricky Rubio|-0.067|
|Chris Paul|0.334|Patrick Beverley|-0.046|
|Jamal Crawford|0.310|Michael Beasley|-0.033|
|Jared Dudley|0.286|Andre Miller|-0.005|
|Martell Webster|0.283|Luc Richard Mbah a Moute|-0.005|
|Stephen Curry|0.258|George Hill|0.001|
|Amir Johnson|0.256|Evan Turner|0.001|
|Patrick Mills|0.255|Glen Davis|0.010|







2014 Research Paper Competition Presented by: 

9 


