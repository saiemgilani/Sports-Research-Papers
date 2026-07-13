<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2025/2025 - The Adaptability Index An Information Theoretic Framework for Measuring Player Adaptability - Dubem.pdf -->

# **The Adaptability Index: An Information Theoretic Framework for Measuring Player Adaptability** Basketball 20251453 

## **1. Introduction** 

Since the “super team” era in the NBA started, understanding a basketball player’s offensive adaptability has been crucial to team construction. This holds true of all positions, skill levels, and usage rates. The best, highest usage players are expected to team up with other high usage players and must adapt to each other’s playstyles in a way that maximizes the output from all players. Power forwards and centers are not only expected to grab rebounds and score from in the paint, but also space the floor and score further away from the basket more than ever. The “3” or small forwards are increasingly taking advantage of all the space, running offenses and creating opportunities for others as well as creating their own shots from all areas of the court. Even point guards are getting bigger and stronger, not just shooting from the perimeter but also scoring in the paint when available. Without at least a couple players on the team that are adaptable, it seems that offenses can become stagnant and predictable and star players’ potentials can be wasted. 

Despite the importance of adaptability, there are very few metrics that measure offensive adaptability. Versatility[1], developed by John Hollinger and defined in equation (1) below, measures the ability for a player to score, rebound, and assist _all the time_ , but not selectively choose when to score, rebound, and assist _at any time_ given the personnel around them. Players can be versatile, while not adapting their playstyles. [(𝑃 )]<sup>1</sup> ⁄<sup>3</sup> (1) There exists another metric, portability, which is also crucial to team construction. Portability 𝑃𝑃) ∙(𝑅𝑅𝑃 ) ∙(𝐴𝐴𝑃 

hasn’t been rigorously defined by many however, craftedNBA[2] does have their own definition which is a weighted average of portable skills like low usage rates, high true shooting percentage, and high assisting. Portability is meant to measure the ability for a player to succeed regardless of who’s around them. Another interpretation is that portability is a measure of how easy it is for other players to adapt to the new player. Certainly, a valuable metric but doesn’t quite capture how adaptable the player is themselves. 

This work aims to define offensive adaptability and build a metric that adequately quantifies that definition. 

## **2. Methods** 

The existing metrics that are close to adaptability are missing the concept of _changing_ playstyle given the lineup. To adequately define adaptability, the metric must include the concept of changing playstyle. Secondly, the playstyle must be changing _predictably_ with lineup. A player cannot be adapting if the change in playstyle from lineup to lineup is random. 

A start for this metric is some sort of correlation. Correlations measure the relation of a change in one variable to the change in another. For example, Pearson’s correlation measures how linearly related one variable is to another, with a correlation of 1 representing that a change in one variable 



1 

perfectly predicts the change in another and a correlation of 0 representing a change in one variable having no predictive power for the change in another, assuming a linear relationship. So, adaptability could be defined as the correlation between lineup and playstyle where the higher the correlation, the more likely a change in lineup results in a change in playstyle and the lower the correlation, the less likely a change in lineup results in a change in playstyle. 

The natural selection at first thought might be Pearson’s correlation. However, using Pearson’s correlation presents some challenges. Lineup is a discrete, non-ordinal variable. Pearson’s correlation only properly relates linear relationships, which without even defining playstyle, one might think that there is not much “linear” about playstyle. Lastly, Pearson’s correlation can only relate two scalar variables. Playstyle most likely can’t get distilled down to a single scalar without losing too much information. 

There is a concept, mutual information, from information theory that correlates random variables. Mutual information makes no assumptions about the distributions of the random variables, the relationship of the random variables, whether they are discrete or continuous, or the dimensionality of the variables – making it a strong candidate for correlating lineup and playstyle. Adaptability will be defined as the mutual information between lineups that a player participates in and the player’s playstyle. 

### **2.1. Information Theory Primer** 

The following section is a brief introduction to information theory which will build intuition on the utility of mutual information and will provide the context for a more nuanced interpretation of future results that include information theoretic concepts. 

### **2.1.1. Entropy and Information Content** 

To get to the idea of shared information between lineup and playstyle, “information” must first be defined. The information theoretic definition of information called “entropy” is used. Entropy in information theory measures the spread of a probability mass or probability density function. In 

other words, how random the process is that follows the function. The definition is below: (2) 𝐻𝐻(𝑋𝑋) = −�𝑝𝑝(𝑥𝑥) log 𝑝𝑝(𝑥𝑥) Where: is a discrete random variable 𝑥𝑥∈𝒳𝒳 is the entropy of a discrete random variable 𝑋𝑋 is the probability mass function for a discrete random variable 𝐻𝐻(∙) is the set of values that can take on 𝑝𝑝(∙) is a realization of sampled from the set 𝒳𝒳 𝑋𝑋 To illustrate the utility of the equation, imagine a biased coin that has heads and tails. The 𝑥𝑥 𝑋𝑋 𝒳𝒳 probability of heads is 100% leaving the probability of tails as 0%. Substituting into equation (2), . In this context, the second term is defined as 0 or 0 ∙log 0 ≡0. The resulting entropy is 0. The function has no spread or randomness. Sometimes, entropy is described as the average information content of a distribution. 𝐻𝐻(𝑋𝑋) = −(1 ∙log 1) −(0 ∙log 0) is large when lower probabilities exist in the distribution and these low probability outcomes are considered “surprising” which can carry more information. Then entropy would be the average of all the events, which will be larger if −log 𝑝𝑝(𝑥𝑥) there are more surprising (low probability) events. There is an analog for continuous distributions 



2 

where the summation is substituted with integrals and the probability mass function is substituted with a probability density function. 



_Figure 1: Low and high entropy for discrete and continuous distributions_ 

### **2.1.2. Mutual Information** 

Now that there is a framework for getting the information content of a distribution, what does it mean for two distributions to share information? One could imagine that for two random variables, knowledge of the outcome of one variable might contain some information about the outcome of the other. This is analogous to Pearson’s correlation , where denotes how much variance in one variable can be explained by the variance in another. Another interpretation of two distributions sharing information is that knowledge about one variable reduces the average information content 𝑟𝑟 𝑟𝑟<sup>2</sup> in another. This is defined mathematically in equation (4): (4) Where: is the mutual information between two random variables 𝐼𝐼(𝑋𝑋; 𝑌𝑌) = 𝐻𝐻(𝑌𝑌) − 𝐻𝐻(𝑌𝑌|𝑋𝑋) is the conditional entropy – Entropy of first variable given knowledge of the second 𝐼𝐼(∙ ; ∙) This says that random process Y has some information content but knowledge about X reduces the 𝐻𝐻(∙| ∙) information Y contains. The amount of that reduction is the mutual information. This is illustrated in Figure 2 where is a continuous random variable and is a discrete random variable taking on two values. The marginal distribution, , is flatter and contains some amount of information. Knowing decreases the variance of 𝑌𝑌 on average. The information content of 𝑋𝑋 is reduced by the shared information between and . 𝑓𝑓(𝑌𝑌) 𝑋𝑋 𝑌𝑌 𝑌𝑌 𝑋𝑋 𝑌𝑌 



3 



<!-- Start of picture text -->
High entropy Reduced entropy Reduced entropy<br>2 1<br>𝐻𝐻 𝑌𝑌 𝐻𝐻 𝑌𝑌|𝑋𝑋= 𝑥𝑥 𝐻𝐻 𝑌𝑌|𝑋𝑋= 𝑥𝑥<br><!-- End of picture text -->



<!-- Start of picture text -->
High entropy Reduced entropy Reduced entropy<br>2 1<br>𝐻𝐻 𝑌𝑌 𝐻𝐻 𝑌𝑌|𝑋𝑋= 𝑥𝑥 𝐻𝐻 𝑌𝑌|𝑋𝑋= 𝑥𝑥<br>Entropyof marginaldistribution, no knowledge of X Entropyof conditional distributions given knowledge of X<br>Figure 2: Illustration of reducing information content (entropy) through shared (mutual) information<br>� (5)<br>𝐼𝐼(𝑋𝑋; 𝑌𝑌) ≡��𝑝𝑝(𝑥𝑥, 𝑦𝑦) log � 𝑝𝑝(𝑥𝑥, 𝑦𝑦)<br>𝑥𝑥∈𝒳𝒳 𝑦𝑦∈𝒴𝒴 𝑝𝑝(𝑥𝑥)𝑝𝑝(𝑦𝑦)<br><!-- End of picture text -->

_Figure 2: Illustration of reducing information content (entropy) through shared (mutual) information_ 

Mutual information can be written in terms of probability mass functions. 

This shows that if two random variables are independent, , then the mutual information is 0. Mutual information can also be written in the continuous case with integrals 𝑝𝑝(𝑥𝑥, 𝑦𝑦) = 𝑝𝑝(𝑥𝑥)𝑝𝑝(𝑦𝑦) (6) ~~�~~ 𝐼𝐼(𝑋𝑋; 𝑌𝑌) ≡� 𝑓𝑓(𝑥𝑥, 𝑦𝑦) log �<sup>𝑓𝑓(𝑥𝑥, 𝑦𝑦)</sup> 𝑑𝑑𝑦𝑦𝑑𝑑𝑥𝑥 𝑥𝑥∈𝒳𝒳,𝑦𝑦∈𝒴𝒴 **2.2. Estimating Mutual Information** 𝑓𝑓(𝑥𝑥)𝑓𝑓(𝑦𝑦) Although there is a clear definition of mutual information, computing its value still poses a challenge. For now, it’s assumed that “playstyle” contains some continuous component, requiring the integral form of mutual information to be used. However, is not known – only observations sampled from . could be estimated using a kernel density estimator, however computing the integral is still a challenge. A Markov Chain Monte Carlo (MCMC) estimator could be used, 𝑓𝑓(𝑥𝑥) however if “playstyle” is multi-dimensional, MCMC will also be challenging to compute.  𝑓𝑓(𝑥𝑥) 𝑓𝑓(𝑥𝑥) 

It is possible to directly estimate the entropy of a random variable using a k-nearest neighbor approach like the Kozachenko-Leonenko estimator[3] which is what’s used in this work. The derivation of the estimator is as follows: It is observed from equation (3) that entropy is an expectation of . An estimate of the expectation would be to forego the integral and directly calculate log 𝑓𝑓(𝑥𝑥) −<sup>1</sup> 𝑁𝑁 ) (7) 𝑖𝑖 �log 𝑓𝑓(𝑥𝑥 Where: is the number of samples 𝑁𝑁 𝑖𝑖=1 is a single data point 𝑁𝑁 𝑖𝑖 𝑥𝑥 



4 

That leaves estimating ). This estimation begins with the approximation that the probability mass around a point is equal to a sufficiently small volume centered at that point multiplied by a 𝑖𝑖 constant probability density throughout the volume. The sufficiently small volume is defined as the log 𝑓𝑓(𝑥𝑥 hypersphere around the point with a radius equal to the distance to that point’s 𝑘 ℎ nearest neighbor– more formally: ) (8) Where: is the distance from point to its 𝑃𝑃𝑖𝑖(𝜖𝜖) ≈𝑐𝑐th nearest neighbor 𝑑𝑑𝜖𝜖<sup>𝑑𝑑</sup> 𝑓𝑓(𝑥𝑥𝑖𝑖 is the probability mass of the volume around point to its 𝑘 ℎ nearest neighbor 𝜖𝜖 is the volume of a hypersphere in 𝑖𝑖 𝑘𝑘 -dimensional space with radius 1 𝑖𝑖 𝑃𝑃 (𝜖𝜖) 𝑖𝑖 𝑑𝑑 It then follows that: 𝑐𝑐 𝑑𝑑 ) (9) Focus is turned to estimating log 𝑃𝑃𝑖𝑖(𝜖𝜖) ≈log 𝑐𝑐. Consider a probability density function 𝑑𝑑 + 𝑑𝑑log 𝜖𝜖+ log 𝑓𝑓(𝑥𝑥𝑖𝑖 that is the probability density that is the distance to the th nearest 𝑖𝑖 𝑘𝑘 log 𝑃𝑃 (𝜖𝜖) neighbor of point . Then is the probability mass 𝑝𝑝 (𝜖𝜖) that one point, point ’s 𝑘𝜖𝜖 ℎ nearest neighbor, is contained in 𝑘𝑘 𝑘𝑘 the range 𝑖𝑖 . Then exactly 𝑝𝑝 (𝜖𝜖)𝑑𝑑𝜖𝜖 points are at distances less than the 𝑖𝑖 𝑘 ℎ nearest neighbor and points, the rest, are at distances farther than the [𝜖𝜖, 𝜖𝜖+ 𝑑𝑑𝜖𝜖] 𝑘𝑘−1 𝑘 ℎ nearest neighbor. This is a trinomial distribution where the 𝑁𝑁−𝑘𝑘−1 probability of success, exactly one point in the region is the probability mass from the incremental probability density multiplied by the width , the probability of being 𝑑𝑑𝜖𝜖 at a distance less than is , and the probability of being at a distance greater than is the remaining probability 𝑑𝑑𝜖𝜖 𝑖𝑖 _Figure 3: trinomial distribution_ mass. This takes the mathematical form of equation (10): 𝜖𝜖 𝑃𝑃 (𝜖𝜖) 𝜖𝜖 𝑘𝑘 𝑝𝑝 (𝜖𝜖)𝑑𝑑𝜖𝜖 ∙<sup>𝑑𝑑𝑃𝑃𝑖𝑖(𝜖𝜖)</sup> 𝑁𝑁−𝑘𝑘−1 𝑘𝑘 (𝑁𝑁−1)! 𝑖𝑖 𝑖𝑖 (10) 𝑝𝑝 (𝜖𝜖)𝑑𝑑𝜖𝜖= 𝑑𝑑𝜖𝜖∙𝑃𝑃 (𝜖𝜖)<sup>𝑘𝑘−1</sup> ∙�1 −𝑃𝑃 (𝜖𝜖)� 1! (𝑘𝑘−1)! (𝑁𝑁−𝑘𝑘−1)! 𝑑𝑑𝜖𝜖 �∙<sup>𝑑𝑑𝑃𝑃𝑖𝑖(𝜖𝜖)</sup> 𝑁𝑁−𝑘𝑘−1 𝑘𝑘 𝑖𝑖 𝑖𝑖 Then the expectation of the log of the probability mass around a point to its 𝑝𝑝 (𝜖𝜖)𝑑𝑑𝜖𝜖= 𝑘𝑘�<sup>𝑁𝑁−1</sup> 𝑘𝑘 𝑑𝑑𝜖𝜖 𝑑𝑑𝜖𝜖∙𝑃𝑃 (𝜖𝜖)<sup>𝑘𝑘−1</sup> ∙�1 −𝑃𝑃 (𝜖𝜖)� 𝑘 ℎ nearest neighbor ∞ (11) 0 𝑖𝑖 𝑘𝑘 𝑖𝑖 Ε[log 𝑃𝑃 (𝜖𝜖)] = �𝑝𝑝 (𝜖𝜖) log 𝑃𝑃 (𝜖𝜖) 𝑑𝑑𝜖𝜖 





5 

The details of evaluating the integral in equation (12) are left to Appendix A. Then substituting the right-hand side of equation (12) into equation (9) and rearranging terms: (13) 𝑖𝑖 𝑑𝑑 𝑖𝑖 And finally averaging over all log 𝑓𝑓(𝑥𝑥 ) ≈𝜓𝜓(𝑘𝑘) −𝜓𝜓(𝑁𝑁) −log 𝑐𝑐) −𝑑𝑑log 𝜖𝜖 





To deal with compounding errors that can occur from the estimation of conditional entropies in the summation term, the 𝑘 ℎ nearest neighbor for every point in the estimation of the marginal entropy ℎ<sup>�</sup> is selected such that it is the nearest neighbor in the associated conditional entropy estimator ℎ<sup>�</sup> . This approach is outlined by Ross[4]. Equation (15) with the Ross selection criterion for nearest neighbors in the marginal and conditional distributions is what is used to (𝑌𝑌) 𝑚𝑚𝑘𝑘ℎ estimate mutual information. (𝑌𝑌|𝑋𝑋= 𝑥𝑥) 

### **2.3. Final Problem Formulation** 

With the framework for defining adaptability and the machinery to compute mutual information specified, all that’s left is to formulate the variables for which mutual information will be computed between. 

As described in the beginning of section 2, the mutual information between “playstyle” and lineup will be used as the proxy for adaptability. Defining lineup is trivial – it’s a discrete random variable where each suitable lineup that a particular player was a part of is included in the set. Playstyle, for the purposes of this study, is simplified to the coordinates of the player on the court during a particular frame and a Boolean for whether the player has the ball during that frame. This will provide adequate information about how often the player has the ball and where they operate with the ball – a large portion of what defines offensive playstyle. Described later in section 4.3, it could be useful to update the ball possession variable to a discrete random variable sampled from the set of actions {𝑁 𝑁 𝑃 however this simplified version of ball possession captures plenty of information and can lead to interesting insights on its own. , 𝐷𝐷𝑟𝑟𝑖𝑖𝐷 𝐷𝐷𝑖𝑖𝑁𝑁𝐷𝐷, 𝑃 𝑖𝑖𝑁𝑁𝐷𝐷, 𝑆𝑆ℎ𝑁 𝑘𝑘𝑖𝑖𝑁𝑁𝐷𝐷, 𝑅𝑅𝑁𝑁𝐷𝐷𝑁𝑁𝑅𝑅𝑁𝑁𝑑𝑑𝑖𝑖𝑁𝑁𝐷𝐷} 

Mutual information is not well-defined for the mutual information between one variable and another joint random variable that is the joint of discrete and continuous variables, like in the case of the playstyle variable. The mutual information “chain-rule”, proven in Appendix B, can separate the effects of mutual information between the components of the playstyle joint random variable. The chain rule is: 







6 

This says that the mutual information between and a joint random variable is sum the of the mutual information between and and the incremental information gained about from after already knowing . 𝑋𝑋 𝑌𝑌, 𝑍𝑍 𝑋𝑋 𝑌𝑌 𝑋𝑋 𝑍𝑍 Substituting for lineup and 𝑌𝑌 𝑝𝑝𝐷𝐷𝑃𝑃𝑦𝑦𝑃𝑃𝑘𝑘𝑦𝑦𝐷𝐷𝑁𝑁= (𝐵𝐵𝑃𝑃𝐷 𝑃𝑃𝑁𝑁𝑃 𝑁𝑁𝑃 𝑖𝑖𝑁 , 𝑃𝑃𝐷𝐷𝑃𝑃𝑦𝑦𝑁𝑁𝑟𝑟 𝐶𝐶𝑁 𝑟𝑟𝑑𝑑𝑖𝑖𝑁𝑁𝑃𝑃𝑘𝑘𝑁𝑁𝑃𝑃) (17) 𝐼𝐼(𝐿𝐿; 𝐵𝐵, 𝐶𝐶) = 𝐼𝐼(𝐿𝐿; 𝐵𝐵) + 𝐼𝐼(𝐿𝐿; 𝐶𝐶 | 𝐵𝐵) = 𝐼𝐼(𝐿𝐿; 𝐵𝐵) + �𝑝𝑝(𝐷𝐷) ∙𝐼𝐼(𝐿𝐿; 𝐶𝐶|𝐵𝐵= 𝐷𝐷) 𝑏𝑏∈{0,1} Where: is the lineup random variable is the player-ball possession Boolean random variable 𝐿𝐿 is the player coordinates, random variable 𝐵𝐵 This says that the mutual information between lineup and playstyle, defined as the joint of player 𝐶𝐶 (𝑥𝑥, 𝑦𝑦) coordinates and the ball possession Boolean, is the sum of the mutual information between the lineup and ball possession variables and the mutual information between the lineup and player coordinates, given knowledge of if the player has the ball or not. Given the lineup variable and ball possession Boolean are discrete, computing their mutual information is trivial using equation (5). Finally, is computed using equation (15) twice, once for the datapoints where 𝐿𝐿 the player has the ball and once for when they don’t, with the result weight averaged together. 𝐵𝐵 𝐼𝐼(𝐿𝐿; 𝐵𝐵) 𝐼𝐼(𝐿𝐿; 𝐶𝐶) 

### **2.4. Data Preparation** 

Tracking data is required for the player coordinates and determining the ball possession Boolean. The 2016 SportVU dataset supplemented with play-by-play data is used. The merging of these two data sets is done by Donald Clayton and is publicly available on huggingface[5]. The SportVU dataset contains 631 games from the first half of the 2015-2016 season from the start of the season to January 23<sup>rd</sup> , 2016. 

The structure of the dataset is illustrated in Figure 4. The graph represents a series of “events” in a play-by-play context. Events are point-in-time actions like a shot attempt, a foul, or a turnover. Each game consists of many events and each event has relevant information to describe the event like who the home and away teams are, the players on the teams, what happened during the event, and which player(s) were involved in the event. Finally, the event also contains “moments” which include coordinates for all players on the court and the ball as well as what the clock reads for that moment. Each moment is a frame captured at a sampling rate of 25 frames per second. Given the structure of the dataset, there are several data processing steps outline in sections 2.4.1 and 2.4.2. 



7 



<!-- Start of picture text -->
Legend<br>Dictionary<br>List<br><!-- End of picture text -->

_Figure 4: SportVU Dataset Schema_ 

### **2.4.1. Deduplicating events** 

The moments, which capture frame-by-frame coordinates of the players and ball, are roughly grouped by possession, however the structure of the dataset maps groups of moments to events. Events are not an entire possession but rather a single moment in time. There may be multiple events in a possession. For example, a possession may consist of a shot attempt, an offensive rebound, and a foul. In this scenario, the shot attempt event, offensive rebound event, and the foul event will all contain the exact same set of moments from the possession that contains those events. Events need to be deduplicated such that each event in the dataset has a unique set of moments. To do so, events for a game are sorted in chronological order. Then starting with the first event, the following event’s beginning and ending moments are checked to see if they have the same start and end times as the event that came before it. If so, the event is logged in a set for the possession. The process continues until the next event does not contain the same moments as the current event – it is not in the same possession. Then the set of events in the possession are checked for a made or missed shot event. If no events in the possession contain a shot, the offensive possession is not used for this analysis, and it’s thrown out. If a shot event is contained in possession, the event labelled as the made or missed shot is retained to retain information about who had possession and the rest of the events in the possession are discarded. The algorithm is described in algorithm 1. 

- **<u>gorithm 1orithm 1</u>** Deduplicate events plicate events licate events 

- 1: Initialize clean deduped events list 2: Initialize Possession set 3: Sort uncleaned events list in ascending chronological order 𝑐𝑐 4: **for** each event in 𝒫𝒫 𝑁𝑁 

#### **Algorithm 1orithm 1** Deduplicate events plicate events licate events 

- 3: Sort uncleaned events list 4: **for** each event in 5: **if** 𝑖𝑖 

- 6: Add to 𝑁𝑁 𝑖𝑖= 1 𝑘𝑘𝑁𝑁 𝑖𝑖= |𝑁𝑁| −1 7: **end if** |𝒫𝒫| = 0 𝑖𝑖 

- 𝑁𝑁 𝒫𝒫 



8 

8: **if** and 𝑁 = 𝑁 9: Add to 𝑖𝑖 𝑖𝑖+1 𝑖𝑖 𝑖𝑖+1 10: **else** 𝑃𝑃𝑘𝑘𝑃𝑃𝑟𝑟𝑘𝑘 𝑘𝑘𝑖𝑖𝑚𝑚𝑁𝑁 𝑁𝑁𝑓𝑓 𝑁𝑁 = 𝑃𝑃𝑘𝑘𝑃𝑃𝑟𝑟𝑘𝑘 𝑘𝑘𝑖𝑖𝑚𝑚𝑁𝑁 𝑁𝑁𝑓𝑓 𝑁𝑁 𝑑𝑑 𝑘𝑘𝑖𝑖𝑚𝑚𝑁𝑁 𝑁𝑁𝑓𝑓 𝑁𝑁 𝑑𝑑 𝑘𝑘𝑖𝑖𝑚𝑚𝑁𝑁 𝑁𝑁𝑓𝑓 𝑁𝑁 𝑖𝑖+1 11: **if** 𝑁𝑁 𝒫𝒫 12: **if** shot made event in 13: |𝒫𝒫| > 1Append shot made event to 14: **else if** shot missed event in 𝒫𝒫 15: Append shot missed event to 𝑐𝑐 16: **end if** 𝒫𝒫 17: **else** 𝑐𝑐 18: **if** is a shot made or missed event 19: Append to 𝑖𝑖 20: **end if** 𝑁𝑁 𝑖𝑖 21: **end if** 𝑁𝑁 𝑐𝑐 22: Clear Posession set 23: **end if** 24: **end for** →𝒫𝒫= {} 

### **2.4.2. Removing event overlap** 

Even though events that contain the exact same set of moments have been deduped, it is still possible for a subset of moments from one event to exist in the next event. This is illustrated in Figure 5. Figure 5 tracks the ball location for two consecutive events during a Lakers vs. Celtics game. The two events are Julius Randle scores (on the right basket) followed by a David Lee missed jumper (on the left basket). In the top two visuals, the red oval highlights the same moments that exists in both events. Removing this overlap is trivial. Since only offensive possessions in the halfcourt are considered for this analysis, only frames where all 5 offensive players are on the offensive end of the court are retained. This fixes the overlap issue however some plays, like fast breaks, end up being completely removed given not all 5 offensive players are in the offensive halfcourt. This is okay as fastbreaks contain little information about change in offensive playstyle from lineup to lineup. The bottom two visuals in Figure 5 show which moments are removed using these rules. 



9 







<!-- Start of picture text -->
Julia.Randle.(LAL).scores.on.right. David.Lee.(BOS).missed.jumper.<br>side.before.removing overlap on.left.side.before.removing<br>overlap<br>Julia.Randle.(LAL).scores.on.right. David.Lee.(BOS).missed.jumper.<br>side.after.removing overlap on.left.side.after.removing<br>overlap<br><!-- End of picture text -->

_Figure 5: Location of the ball before and after removing overlap for two consecutive events_ 

### **2.4.3. Ball Possession** 

With completely deduplicated, frame-by-frame player coordinate and lineup data, the last step is to compute the ball possession Boolean for the player of interest. A simple heuristic is used.  For any frame, if the ball is within a 3-foot radius in the x-y plane and the ball is no higher than 3 feet above the player’s z-coordinates, then the player is in possession of the ball. These rules were selected because the average NBA player height is around 6’6” with an average ape index of 1.063 giving an average wingspan of around 83 inches or nearly 7 feet. Players rarely fully extend the ball parallel to the court so 3 feet should capture when a player is in possession of the ball. The ball must also be no higher the three feet above the player’s z-coordinate so that shots above a player’s head do not count as possession. 

## **3. Results** 

Equation (17) was computed for the top 8 players by minutes played for each of the 30 NBA teams. The samples used for computation came from the SportVU and play-by-play dataset which was cleaned using the process outlined in section 2.4. Only lineups that had sufficient data after cleaning were used in the adaptability computation, where sufficient is defined as 10,000 frames. 

Figure 6 shows a plot of mutual information vs. lineup entropy. Both mutual information and lineup entropy have been shifted and scaled such that the minimum and maximum values are 0 and 100 respectively. The scaling is for increased interpretability. The first item to notice is the relationship between lineup entropy and mutual information; as lineup entropy increases, so does mutual information. This is an expected outcome that is standard to information theory. The more information that a variable has, the more information that can be shared with another variable. From equation (2), lineup distributions that are uniform and have more lineups available will produce higher lineup entropies, allowing for more information to be shared. Translating this phenomenon to a basketball context – players that have more diverse lineups have more opportunity to adapt. Figure 7 shows the mean lineup entropy by number of lineups available to the player. 



10 



_Figure 6: Mutual Information vs Lineup Entropy_ 



_Figure 7: Mean Lineup Entropy by Unique Lineup Count_ 

It seems that there should be some accounting for the number of lineups a player participates in. It might be unfair that a player participates in only 3 valid lineups while another participates in 10. It could be that the player with fewer lineups has a less imaginative coach not willing to try different lineups. It could be that this player is on a team that isn’t as deep so there are fewer viable lineups. However, it also seems that players who have a higher mutual information regardless of number of lineups should not be penalized. It could be that these players are on so many lineups because they are so adaptable in the first place. On the low end of the lineup count scale, those players could be there because they are not very adaptable and only work in a couple lineups. 

A weighted average of raw mutual information and mutual information above expected is used to capture the effects of being on a certain number of lineups because the player is adaptable and being on a certain number of lineups due to outside factors. Mutual information above expected is the difference between the measured mutual information and the predicted mutual information 



11 

given lineup entropy from the regression in Figure 6. Both raw mutual information and mutual information above expected are scaled to a value between 0 and 100. This scaling is done so that mutual information and mutual information above expected have similar magnitude and have equal effects when changing the weight. The final weighted average is scaled as well. (18) Where: 𝐴𝐴𝑑𝑑𝑃𝑃𝑝𝑝𝑘𝑘𝑃𝑃𝐷𝐷𝑖𝑖𝐷𝐷𝑖𝑖𝑘𝑘𝑦𝑦= 𝑃𝑃𝑐𝑐𝑃𝑃𝐷𝐷𝑁𝑁𝑑𝑑�𝛼𝛼∙𝑃𝑃𝑐𝑐𝑃𝑃𝐷𝐷𝑁𝑁𝑑𝑑[𝐼𝐼(𝐿𝐿; 𝐵𝐵, 𝐶𝐶)] + (1 −𝛼𝛼) ∙𝑃𝑃𝑐𝑐𝑃𝑃𝐷𝐷𝑁𝑁𝑑𝑑[𝐼𝐼(𝐿𝐿; 𝐵𝐵, 𝐶𝐶) 𝑃𝑃𝐷𝐷𝑁𝑁𝑎𝑎𝑁𝑁 𝑁𝑁𝑥𝑥𝑝𝑝𝑁𝑁𝑐𝑐𝑘𝑘𝑁𝑁𝑑𝑑]� is the weighting factor For this study, an alpha of 0.5 is used as a fair point in the middle although there is no rigorous 𝛼𝛼 

testing for why it should be selected. It is up to the interpreter to select the weighting. 

### **3.1. Individual Results** 

Given an alpha of 0.5, Table 1 and Table 2 show the most and least adaptable players in the set. 

_Table 1: Most Adaptable Players_ 

_Table 2: Least Adaptable Players_ 

|**Name**|**Team **|**Position **|**Adaptability**|**Name**|**Team **|**Position **|**Adaptability**|
|---|---|---|---|---|---|---|---|
|Dennis<br>Schroeder|ATL|Guard|100.0|Ersan<br>Ilyasova|DET|Forward|0.0|
|Rajon<br>Rondo|SAC|Guard|98.6|Steven<br>Adams|OKC|Center|1.6|
|Evan<br>Turner|BOS|Guard|97.0|Andre<br>Drummond|DET|Center|3.5|
|James<br>Harden|HOU|Guard|95.4|Tim<br>Duncan|SAS|Center|6.3|
|LeBron<br>James|CLE|Forward|93.2|Robin<br>Lopez|NYK|Center|6.9|
|Jameer<br>Nelson|DEN|Guard|90.5|Hassan<br>Whiteside|MIA|Center|6.9|
|Darren<br>Collison|SAC|Guard|87.6|Marcin<br>Gortat|WAS|Center|8.3|
|Dion<br>Waiters|OKC|Guard|87.0|Tony Snell|CHI|Guard|8.9|
|Devin<br>Booker|PHX|Guard|85.7|Ian<br>Mahinmi|IND|Center|9.3|
|Jerryd<br>Bayless|MIL|Guard|85.0|Andre<br>Roberson|OKC|Guard|9.7|



Familiar faces show up on the most adaptable players list. LeBron James is known as a player that is certainly versatile and can do it all, however he is also known for elevating the players around him, no matter who they are. Rajon Rondo and James Harden during this time are also known to be floor generals, most likely adapting to players around them. The list of least adaptable players is full of bigs like Steven Adams, Tim Duncan, and Andre Drummond. 

The observation about bigs being less adaptable is supported by the entire dataset. Figure 8 shows the adaptability distributions by position. Centers are clumped near the lower end of adaptability 



12 

however, there seems to be some centers in the tail that are more adaptable than the bunch. These centers are Jahlil Okafor and Demarcus Cousins who were some of the premier centers during that time and who were asked to do a lot offensively. It now seems they were adapting to the players around them. Forwards and guards have a much more symmetric distribution while guards on the average are most adaptable. This makes sense as guards are typically the most skilled players and are asked to run their team’s offense. 



_Figure 8: Adaptability Distribution by Position_ 

Mutual information when defining playstyle as the joint of player coordinates and ball possession captures a complex relationship between player coordinates, ball possession, and lineup. Purely knowing the fraction of time that the player has the ball might give some information about which lineup the player is on. Knowledge of where the player is on the court regardless of if they have the ball or not may give some information about which lineup they’re on. Then finally, knowledge of where the player is when they have the ball and when they don’t have the ball will give some information about what lineup they’re on. To illustrate a player being adaptable, I’ve chosen just where the player is on the court regardless of when they have the ball as a clear visualization. 

Figure 9 shows a heatmap of LeBron James’ coordinates for different lineups. Generally, LeBron is quite versatile and plays on many areas of the court with some warm spots along the perimeter and near the blocks. In lineup 2 of Figure 9, LeBron plays many areas of the court. Kyrie Irving was injured during part of the 2015-2016 season so the number of frames available for this lineup is not significantly larger than others which implies variation in location is not due to a larger sample size. A hypothesis is that Kyrie is an offensive play maker who can get his own points at any location on the floor. This gives LeBron more freedom to roam the court. It might even be a necessity that he roams the court to allow Kyrie space for when he decides to score. Conversely, lineup 1 contains three other bigs, Tristan Thompson, Timofey Mozgov, and Kevin Love. LeBron is playing a guard on this lineup and clears from the paint by operating along the perimeter so the other bigs can operate where they’re comfortable. It’s clear that LeBron is adapting to the lineup on the court. 



13 





_Overall_ 













_Lineup 1 Lineup 2 Lineup 3_ 

_Figure 9: LeBron James Position Heatmaps_ 

Figure 10 shows a heatmap of Andre Drummonds’ coordinates for different lineups. Generally, Andre Drummond operates in the paint. Across the three lineups shown in the figure, Andre operated almost exclusively in the paint with very little variation in position across lineups. Andre is not adapting to his lineup. 



_Overall_ 



<!-- Start of picture text -->
Lineup 1<br><!-- End of picture text -->









_Lineup 1_ 





















_Lineup 2 Lineup 3_ 

_Figure 10: Andre Drummond Position Heatmaps_ 

### **3.2. Team Results** 

Adaptability is most important in the context of your team. The first analysis was to look at the mean adaptability index of the top 8 players by minutes on a team and see if that correlated with regular season wins. Figure 11 shows that there doesn’t seem to be much correlation. In fact, the Spurs, one of the best teams in the league that year, on average did not have very adaptable players. This could be interpreted as each player has a role that they play regardless of the lineup that 



14 

they’re on. The philosophy may be to know your role and excel at it. This is certainly easier on the players and the coach to execute, and it seems the Spurs do this extremely well. The Spurs are not without adaptable players though. Their most adaptable player is Manu Ginobili with an Adaptability Index slightly above average at 55.8. No other player on the team has an adaptability above 50. While most players on the Spurs during this time are tasked with executing their role, Manu is a “glue” person who comes off the bench and must play well with the second unit while also playing large minutes with the starting unit, where he must also perform as well. 



_Figure 11: Regular Season Wins vs Mean Adaptability_ 

It is interesting to investigate adaptability in the context of usage rate. Intuitively, it could be good for the highest usage player, the player most responsible for generating offense, to be adaptable for those who may not be as capable at generating offense. Figure 12 takes the usage rank for a particular player on their team and looks to see how high they rank in terms of adaptability on their team. For example, the first bar shows that for players who are the highest usage on their team tend to be the 4<sup>th</sup> most adaptable player on their team. Although, the error bars are wide (there are only 30 teams and thus 30 data points in each bar), the directional insight is interesting. Figure 12 says that the third highest usage player on the team, not the first, is often the most adaptable. This might be rationalized by the hypothesis that the highest usage player takes on the offensive load and must get points however they feel most comfortable, regardless of the other players on the court with them. However, the third option player must take the points as they come. They must adapt or risk being a lower scoring option on the team. 



15 



_Figure 12: Mean Adaptability Rank by Usage Ranks_ 

The third offensive option on the team might typically be the most adaptable, but is that the best strategy? Figure 13 takes the adaptability rank on the team for the highest usage player on that team and calculates the mean win rate for each bucket. For example, the first column is interpreted as teams for which their highest usage player is also the most adaptable player on the team, averaged 50 wins in 2015-2016. The second bar is read similarly, teams for which the highest usage player is the second most adaptable on the team averaged 40 wins for the season. The error bars are wide once again given only 30 datapoints total but directionally, it seems that it may be beneficial to have your highest usage player be your most adaptable. 



_Figure 13: Mean Team Win Count by Adaptability Rank of Highest Usage Player_ 

The teams in the first bar are the Cleveland Cavaliers, Houston Rockets, and Atlanta Hawks. Their highest usage and most adaptable players are LeBron James, James Harden, and Dennis Schroeder respectively. The strategy for these teams seems to be that their highest usage players are acting as floor generals fitting their teammates needs and making those around them better. Note that other high performing teams like the Golden State Warriors and the San Antonio Spurs are not in this list. Their most adaptable players are Andre Iguodala and Manu Ginobili who are the 7<sup>th</sup> most and 3<sup>rd</sup> 



16 

most used players on their team respectively. They fit the off the bench, glue-person role who provides value by fitting in where they can around stars that excel at their roles like Steph Curry and Klay Thompson for GSW and LaMarcus Aldridge and Kawhi Leonard for SAS. At first glance, it seems that if a team has a sufficient number of very strong offensive talent on the team, then lower usage players must be adaptable to provide value. Conversely, if there is not enough strong offensive talent on the team, the strongest offensive talent must be adaptable to lift their teammates up. 

It's interesting, yet expected, that there is not a one size fits all winning solution to bringing in adaptable players. The decision must be made in the context of the existing team, each player’s roles, and their excellence at their roles. 

## **4. Discussion** 

### **4.1. Caveats** 

Estimating mutual information using the slightly altered Kozachenko-Leonenko estimator is a strong choice for this application however, it is still an estimate that can have error. Nonparametric estimators, like this one, can be prone to errors if the data are high dimensional . These types of estimators can also have more error when the data are extremely correlated, given the assumption of constant density throughout the volume. For this analysis, the continuous vector was purposely kept to two dimensions to minimize this issue. 10,000 frames (𝑑𝑑≥10) were also used to have a sufficient sample size to reduce noise from the measurement. Lastly, the number of neighbors used in the computation at the conditional level (for each lineup) was 3. A higher number will increase the bias in the error and a lower number will increase the variance. 3 is a standard sweet spot. 

This metric measures how much a player has adapted in the past. It does not measure how much a player is able to adapt in the future. Possibly, in future studies, an analysis could be done to determine if the adaptability index has some autocorrelation with future values. The metric also does not measure how good a player is while adapting. A player can be adaptable but be poor at all the playstyles. This metric, like most metrics, must be used in totality with other metrics and the eye test to get the fullest insight. 

### **4.2. Use cases for the metric** 

At the highest level, the main use case for this metric is to understand the effect of roster changes; changes like bringing in a new player or the effect of bringing together several players who have not played with each other before. It could also be used to measure the effect of a player leaving – depending on the roster composition, players who are more adaptable may leave more of an offensive hole, all else being equal in terms of offensive capability. 

At the lower level, there seems to be two main use cases for this metric. The first is roster design for team front offices. This metric would be used to select which available players would have the highest impact on a new team, both in terms of lifting the existing players’ capabilities but also for the new player to be brought in. The second use case is for fantasy sports and sports betting where prediction of team/player performances after drafts, trades, and new signings is important. This metric could be used to help predict team/player performances before there is adequate data about how the team/player is performing in the new scenario. This early period is where sports bettors may find an edge and win money from the house. 



17 

### **4.3. Next Steps** 

The next steps are to improve the measurement of the metric and to continue to test for its usefulness in insight generation and future outcome prediction. 

The definition of the playstyle vector has room for improvement. As defined in this paper, it accounts for where the player is on the court and where they have the ball. While where the player is on the court and whether they have the ball encodes information about what the player is doing, it is not a full replacement for explicit categorization of what the player is doing. In future iterations of the metric, playstyle would be defined as a joint random variable where is a twodimensional vector containing the coordinates of the player, like it is defined in this paper, and is a discrete action vector extending the current ball possession Boolean definition. The (𝐶𝐶, 𝐴𝐴) 𝐶𝐶 values of A would be {𝑁 𝑁 (𝑥𝑥, 𝑦𝑦) 𝑃 . A machine learning model would be trained and implemented in the pipeline to determine if the player does not have 𝐴𝐴 𝐵𝐵 the ball or if they are dribbling, in the motion of passing, in the motion of shooting, or in the motion , 𝐷𝐷𝑟𝑟𝑖𝑖𝐷 𝐷𝐷𝑖𝑖𝑁𝑁𝐷𝐷, 𝑃 𝑖𝑖𝑁𝑁𝐷𝐷, 𝑆𝑆ℎ𝑁 𝑘𝑘𝑖𝑖𝑁𝑁𝐷𝐷, 𝑅𝑅𝑁𝑁𝐷𝐷𝑁𝑁𝑅𝑅𝑁𝑁𝑑𝑑𝑖𝑖𝑁𝑁𝐷𝐷} of rebounding. This new joint random variable would encode information that would nearly fully encompass playstyle. The downstream computation would all be the same. 

Unfortunately, there isn’t much publicly available NBA tracking data. While the metric has some interesting insights with half a season’s worth of data, gaining more confidence in those insights requires many seasons worth of data. With many seasons’ worth of data, auto correlation or metric stability studies could be run. The effect on team performance could properly be studied with regression techniques that include proper controls. The effect of moving players from one team to another, by nature, requires several seasons worth of data. All these studies can hopefully be done in the future upon the public release of more tracking data. 

## **5. Conclusion** 

In conclusion, mutual information is a powerful tool for measuring the adaptability of a player. While the Adaptability Index shows promise, the metric has room for improvement. Future iterations coupled with the public availability of more tracking data could generate even more interesting insights for roster development. 



18 

## **References** 

- [1] “Versatility Index in NBA Explained,” www.nbastuffer.com, May 08, 2017. - 

- <u>https://www.nbastuffer.com/analytics101/versatility index/</u> 

- [2] “NBA Stats & Analytics | CraftedNBA,” craftednba.com. https://craftednba.com/glossary 

- [3] L.F. Kozachenko, N.N. Leonenko, “A statistical estimate for the entropy of a random vector,” Problemy Peredachi Informatsii 23 (1987), 9–16. 

- [4] B. C. Ross, “Mutual Information between Discrete and Continuous Data Sets,” PLoS ONE, vol. 9, no. 2, p. e87357, Feb. 2014, doi: https://doi.org/10.1371/journal.pone.0087357. 

- [5] “dcayton/nba_tracking_data_15_16 · Datasets at Hugging Face,” huggingface.co. https://huggingface.co/datasets/dcayton/nba_tracking_data_15_16 



19 

## **Appendix A: Kozachenko-Leonenko Integral Evaluation** 

The goal is to simplify the integral in equation (12) also listed below: 







And also equals 

Where Γ(∙) is the gamma function. Then taking the derivative of the Beta function 



or 



Then using the definition of the digamma function: 

And rearranging 

Then 



Substituting into the partial derivative of the Beta function 



20 



And simplifying 





21 

## **Appendix B: Mutual Information Chain Rule** 

The chain rule stated in equation (16) is below: 𝐼𝐼(𝑋𝑋; 𝑌𝑌, 𝑍𝑍) = 𝐼𝐼(𝑋𝑋; 𝑌𝑌) + 𝐼𝐼(𝑋𝑋; 𝑍𝑍 | 𝑌𝑌) 

To derive the mutual information chain rule, mutual information is converted to its definition of reduction in the entropy of the joint variable after knowledge of 𝑌𝑌, 𝑍𝑍 𝑋𝑋 The next step is to rewrite the entropy of the joint variable 𝐼𝐼(𝑋𝑋; 𝑌𝑌, 𝑍𝑍) = 𝐻𝐻(𝑌𝑌, 𝑍𝑍) −𝐻𝐻(𝑌𝑌, 𝑍𝑍 | 𝑋𝑋) as the combination of singular and 

as the combination of singular and conditional entropies. To do this, the chain rule for entropy is used. The entropy chain rule is: 𝑌𝑌, 𝑍𝑍 This chain rule for entropy reads that the entropy of two variables is the entropy of one variable 𝐻𝐻(𝑋𝑋, 𝑌𝑌) = 𝐻𝐻(𝑋𝑋) + 𝐻𝐻(𝑌𝑌|𝑋𝑋) 

plus the entropy of the second variable given knowledge of the first. For completeness, the entropy chain rule will be derived. The proof for the entropy chain rule starts with converting entropy to the probability mass definition. 









22 

Then the term in the left-hand side is the definition for and the term on the right-hand side is 𝐻𝐻(𝑌𝑌|𝑋𝑋) 𝐻𝐻(𝑋𝑋). Using the entropy chain rule to reduce the entropy definition of mutual information to include only 𝐻𝐻(𝑋𝑋, 𝑌𝑌) = 𝐻𝐻(𝑌𝑌|𝑋𝑋) + 𝐻𝐻(𝑋𝑋) 

single variables, the following equation is achieved. Then rearranging terms. 𝐼𝐼(𝑋𝑋; 𝑌𝑌, 𝑍𝑍) = 𝐻𝐻(𝑌𝑌) + 𝐻𝐻(𝑍𝑍|𝑌𝑌) −[𝐻𝐻(𝑌𝑌|𝑋𝑋) + 𝐻𝐻(𝑍𝑍 | 𝑋𝑋, 𝑌𝑌)] And finally, the chain rule for mutual information. 𝐼𝐼(𝑋𝑋; 𝑌𝑌, 𝑍𝑍) = [𝐻𝐻(𝑌𝑌) −𝐻𝐻(𝑌𝑌|𝑋𝑋)] + [𝐻𝐻(𝑍𝑍|𝑌𝑌) −(𝑍𝑍 | 𝑋𝑋, 𝑌𝑌)] 𝐼𝐼(𝑋𝑋; 𝑌𝑌, 𝑍𝑍) = 𝐼𝐼(𝑋𝑋; 𝑌𝑌) + 𝐼𝐼(𝑋𝑋; 𝑍𝑍 | 𝑌𝑌) 



23 


