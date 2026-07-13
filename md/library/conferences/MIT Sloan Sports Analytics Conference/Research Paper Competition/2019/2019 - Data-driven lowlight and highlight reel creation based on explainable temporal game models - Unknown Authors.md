<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2019/2019 - Data-driven lowlight and highlight reel creation based on explainable temporal game models - Unknown Authors.pdf -->



# **Data-driven lowlight and highlight reel creation based on explainable temporal game models** 

Evin Keane, Philippe Desaulniers, Luke Bornn and Mehrsan Javan SPORTLOGiQ <u>evin@sportlogiq.com</u> 

### **Abstract** 

We describe a framework for automatic highlight reel extraction based on game event data. The framework can be applied to most team sports given the output of any in-game state valuation model, of which there are many. We adjust the valuation of events based on their impact on the game's result, a highly relevant factor in terms of fan interest. We demonstrate the usefulness of our approach for extracting both highlights and lowlights, the latter of which has proven difficult with previous approaches. We apply a minimum entropy threshold to avoid monotony in highlight reels. We introduce Event Interest, treating the interest of an event as a continuous function across time rather than a discrete instant. We introduce Cumulative Event Interest, the output of which provides a simple means of extracting game highlights. We demonstrate that this output can be easily modified depending on the type of highlights required by adjusting a limited, intuitive number of parameters of the Cumulative Event Interest function. We provide examples of the output in the form of graphical game summaries and their corresponding highlight videos. 

## **1. Introduction** 

Consumption of sports is trending towards fragmented content on mobile devices. To quote a recent McKinsey & Co study, “We aren’t losing fans, we are fighting shorter attention spans.” In contrast to live television, highlights are visual and short: perfect content for social media. Highlight reels are currently generated manually. This can be time-intensive, particularly in cases where up to ten games can begin and end around the same time, for example in the English Premier League. We propose an automated, data-driven methodology for sports networks and franchises to extract highlights rapidly and automatically and explain why such segments are selected and the underlying data-driven story behind them. 

State-of-the-art highlight generation in sports mostly relies on recognizing audio and visual cues such as visual abnormalities, crowd cheers and fist pumps. In team invasion sports, this approach often points to obvious highlight events such as shots and goals. We propose a method of highlight generation for team invasion sports based on a stochastic model-derived impact metric. The approach allows for highlight and “lowlight” generation, pointing to plays that are most beneficial or detrimental to a team’s performance, not just shots and goals. We demonstrate the framework’s application to hockey, automatically extracting highlight reel video for high-impact actions including shots and goals but also passes, checks, and loose puck recoveries. We demonstrate the flexibility of the framework to extract not only short clip sequences of no more than several seconds, but also shortened games such as the popular "90 in 30" soccer format. 





2019 Research Papers Competition Presented by: 

1 



This is the first attempt in this space to take advantage of the explainable spatio-temporal game models. 

## **2. In-Game Value Models** 

The first requirement of a successful highlight-lowlight extraction framework is a method of game evaluation that updates over time, whether by evaluating game states, game events, or both. Thankfully, such models are becoming more and more ubiquitous. 

The variety of approaches is great. In [5], distinctions are made between the values of events such as goals based on their importance given the game context in which they occur, a concept which is applicable here in highlight extraction as much as player performance evaluation. In [7, 6], the game is described as a Markov chain with rewards in goal states, with k-nearest-neighbors clustering used to define states based on event location. This allows each state to be assigned a value based on its likelihood of leading to a goal for or against each team. In [4], this approach is advanced to incorporate continuous signals using a possession-based LSTM. [3] applies a probabilistic model to optical tracking data in basketball to evaluate every instant in a possession in basketball in terms of the number of points each possession is likely to generate. This model accounts for the locations of all players. The data required for such models is becoming more granular and more widely available, particularly with the advent of optical tracking data. In NFL, LOESS has been used to evaluate the game state based on down-distance-field position in [2]. [1] evaluates a player's contribution to goals based on a goal-scoring prediction model, moving beyond the marginal effect measured by popular plus-minus statistics to a more useful partial effect measurement. This same prediction model can be used to evaluate either team's state. 

## **3. Methods** 

### **3.1 The Impact Score** 

After a game's individual events have been evaluated using a Markov Model or any other evaluation model such as mentioned above, the next step is to determine which events resulted in large changes in value for either team, here referred to as the base and opposing teams. 

The impact score for the base team, _I_ ( _a_ ), previously discussed in [7], is the difference between the change of values resulted from the action taken by the base and the opposing teams. 



where _V b_ ( _e_ ) and _V o_ ( _e_ ) indicate the value of the action or the game event, _e_ , taken by the base and opposing teams, respectively. If a team's impact is positive, the likelihood of that team scoring before the end of the play sequence has increased relative to that of their opponent. The opposite is true when a team's impact is negative. 

### **3.2 Game Context Adjustment** 

Typically, the value of an event is tied in some way to the likelihood of each team scoring next, or the number of points a team is expected to score. In other words, the impact metric captures the effect that an event has on a team's likelihood of scoring next. However, depending on a game's context, the impact of an event may not have any effect on a game's outcome. For this 





2019 Research Papers Competition Presented by: 

2 



reason, it's likely to be of far less interest to fans. The importance of an event's effect on a game's outcome is somewhat important in player evaluation and in the past, adjustments have been made to some evaluation models to account for the importance of a score, for example in [5]. Often, however, the difficulty of executing a particular skill or making a certain decision may not increase much as the game's score changes. From the point of view of the fan, however, the importance of events becomes far greater the greater the effect it has on the game's outcome. The impact must therefore be adjusted to account for its likelihood of changing the game's ultimate result. 

A simple in-game win probability model allows us to adjust the impact to reflect an action's performance given the context. Our in-game model uses league-wide even-strength zero score differential scoring rate combined with a game's remaining time in minutes to generate a Poisson distribution of score count for each team. These distributions, combined with a game's current score differential, are used to calculate win probabilities for each team. 

For each event, the current win probability for each team is calculated. Two further win probabilities are then calculated: one for if the base team is to score immediately, and another for if the opposing team is to score immediately. The difference between each of these and the actual current win probability represent the effect that scoring a goal would have for each team. This value increases when the game is tight, especially near the end of the game, reflecting the contexts in which high and low quality events tend to be most exciting to fans. 

The weighting of this effect is applied to the event impact as follows: 



The first term on the right represents the increase in home team win probability that results from the action. The second term on the right represents the increase in visitor team win probability that results from the action. 

In addition to weighting more heavily towards events that occur in tense contexts, this adjustment also assigns higher rewards to players for making riskier plays near the end of the game when their team needs to score. For example, if the home team is losing by a goal with thirty seconds remaining, it may make a risky play that increases the opposing team's likelihood of scoring next more than its own. This would result in a negative _I_ . However, the effect it has on the game's win probability may actually result in a positive _I adj_ ( _e_ ), because a goal for the home team in this context has a far greater effect on the win probability than a goal for the away team. 

### **3.3 Aggregating Impact Values for Highlights** 

We now have a value assigned to each individual event in a game that reflects its potential interest to viewers. However, a highlight package consisting simply of the highest and lowest value events according to the _I adj_<sup>(</sup> _e_<sup>)</sup> would have several problems. 

First, many sports consist of a wide variety of events, many of which require great skill to execute successfully, but some of which result in far higher impacts than others. In particular, a 





2019 Research Papers Competition Presented by: 

3 



goal in soccer has a far higher impact than any other event in the game. But many other events, which have relatively less impact, require a similar amount of skill and are often of equal interest to fans. Excellent passes, tackles and take-ons all tend to have lower impact than goals and shots. To correct for this, a good highlight extraction framework should account not only for an event's _I adj_ , but should also make variety of event types a priority. 

Second, a compelling highlight does not always consist only of a single event. Often, several valuable events build on one another to result in a particularly valuable sequence of play. A highlight may consist of one very high impact event, or it may consist of several reasonably high impact events in succession. Therefore, a methodology is required to determine what succession of event impacts within a timeframe merits inclusion in a highlight reel. The length of the clip itself should also be a function of the distribution of event impacts with respect to time, rather than each event impact being treated as discrete and independent of others that occur around the same time. 

This section describes solutions to both these problems in turn - one suited to single-event-based highlights, and one suited to aggregating several successive events as highlight sequences. 

### **3.3.1 Variety - Value Tradeoff** 

To avoid producing a monotonous list of highlights that are all of high value but all broadly similar, we apply a condition to the set of results produced whereby a minimum amount of variety is required. We use a user-set minimum entropy value to achieve this. 



where _n_ is the number of distinct event types,<sup>_p_</sup> _i_ is the probability that any event selected randomly from the set of events is event type _i_ , and is equal to the number of events of type _i_ in the list divided by the total number of events in the list. 

Initially, the events with highest adjusted impact are included in the list of highlights. If the entropy for the event types in this list fall below the threshold, the event with next-highest adjusted impact that has not been included in the list is inserted. It replaces whichever event gives the resulting list maximum entropy. This process is repeated until the entropy condition is met, ensuring a certain amount of clip variety as specified by the user. Appendix A shows a coded example of how this can be implemented for a 10-clip highlight reel with a minimum _H_ threshold of 1.0. 

### **3.3.2 Event Interest** 

Typically, in sports analytics each event is recorded with a single timestamp, resulting in a description of a game that consists of a sequence of discrete instants in time. The interest that an event holds for a fan is not only in a single snapshot in time. Instead of assigning the entirety of the impact of an event to a discrete instant, we smooth the distribution of each impact to give the Event of Interest, _EI_ , a continuous function of both _I adj_ ( _e_ ) and time, _EI_ ( _I adj_<sup>(</sup> _e_<sup>)</sup> _,t_ ). 





2019 Research Papers Competition Presented by: 

4 



The exact nature of this function may vary depending on the sport or the event. For example, when a great goal is scored in soccer, the interest for a fan is to see the instant of the goal, and the action that preceded the goal. An _EI_ with a long left tail would accommodate this. Conversely, for a great hit in baseball, we only need to see a second or two of the action that precedes the hit; most of the interest lies in the moments that follow the ball being hit. Here, a function with a longer right tail would be preferable. 

### **3.3.3 Clip Length** 

In many sports, a highlight package based only on individual events would not be effective: often, several events with varying amounts of interest to the viewer happen within a very short space of time. A single high-interest event may not merit fan interest; several medium-interest events in quick succession may be of more interest overall. We may want to vary the length of the clip depending on how many events of interest occur near to one another in time. 

Now that we can represent the event interest as a continuous function in time, we consider the occurrence of several events whose _EI_ distributions overlap in time. We take the sum of every event's _EI_ at each moment: 



We call the resulting value the Cumulative Event Interest, or _CEI_ , where _n_ is the total number of events and _I adj_<sup>(</sup> _e_<sup>)</sup> is the adjusted impact of the game event _e_ . This function represents the cumulative interest of a game's events at every point in time and is a flexible tool for extracting highlights. 

Figure 1 shows the _CEI_ of events with respect to time across a few minutes of an NHL hockey game.  The height of the black lines represents the magnitude of each individual event's impact. The cyan curves represent the _EI_ of each event. The function may vary depending on the usecase; in this case we use a Gaussian function whose height is directly proportional to the absolute impact value. The red curve is the sum of all _EI_ , or the _CEI_ , normalized to appear on the same scale as impact and individual _EI_ . 

Note that the maximum of the _CEI_ occurs at a different location from the maximum _EI_ . This illustrates the fact that _CEI_ relies on several high-impact events; a single high-impact event does not always merit a fan's interest. 

Now that we have a function representing the level of interest at every moment in time, the process of highlight extraction is as simple as setting a minimum threshold for _CEI_ . Any timeframe within which the minimum threshold is met is included in the highlight reel. The length of each clip is the difference between the time when the curve passes above the threshold, and the time when the curve passes back below the threshold. In other words, rather than each clip having the same length, clip length is dictated by the length of time a period of high interest is sustained without interruption. Alternatively, a user may require a fixed number of highlight clips or fixed amount of highlight time. Both cases can be automated by lowering the highlight 





2019 Research Papers Competition Presented by: 

5 



reel threshold until it's reached the height at which the required number of clips or length of time passes above the threshold. 



**Figure 1** : Cumulative Event Interest of game events 

The Gaussian function used in Figure 1 demonstrates another flexible component of the _CEI_ : adjusting the standard distribution used to calculate event _EI_ allows the user to control the tradeoff between importance of individual events and importance of a sequence of events. As the standard deviation approaches zero, _CEI_ approaches an identical representation to the noncontinuous representations given by the discrete _I_ values. On the other hand, a very large standard deviation spreads the interest of each event impact widely across the game, in which case the tool becomes better suited to extended highlights. Alternative (non-Gaussian) distributions are also possible if one prefers asymmetric tails or other features tailored to the sport in question. 

### **3.3.4 Adjustment for breaks in continuous play** 

The _CEI_ is effective in most cases during a continuous sport. One issue arises whenever a break in play occurs. Since a break in play is of no interest to a fan, it does not make sense for the _EI_ of an event to carry across breaks in play. For example, if a goal occurs in the final second of the first half in a soccer game, this does not mean we wish to see the events that occur in the first second of the second half. The same is true for period breaks in hockey and breaks between plays in football. 

The solution is first to limit the _EI_ to the sequence of continuous play in which the event occurs. 



where _s_ is the sequence of play in which the event _e_ occurs. _t_ refers to game time rather than actual clock time, so that breaks in play are ignored. 





2019 Research Papers Competition Presented by: 

6 



Now that there is no spillover of _EI_ from one sequence to another, a second problem arises. At the beginning and end of each play sequence, several high-impact events may occur that are underrepresented by the _CEI_ , simply because it occurs near a cutoff point limiting the _EI_ of nearby events. 



**Figure 2:** _CEI_ after removing _EI_ spillover across breaks in play 

Figure 2 demonstrates the issue with limiting _EI_ spillover across breaks in play. The example is of a hockey game with two breaks in play: one between period 1 and period 2, and another between period 2 and period 3. Around 1200 and 2400 seconds, the _CEI_ drops severely. The same occurs at the start and end of the games. 

To correct for this, we calculate the average per-second _EI_ for the game of interest. We imagine each play sequence extending indefinitely into the past and future beyond its actual start and end times, with perfectly average _EI_ throughout. We calculate the resulting _CEI_ and allow this to spill over into the play sequence. The result is a boost to _EI_ that increases the closer the play is to the beginning or end of a play sequence. Because this boost is proportional to the average impact of the game, it does not unfairly affect the _CEI_ at the beginning and end of play sequences one way or the other. The additional _CEI_ generated using this method is shown in Figure 3. The resulting _CEI_ for the same game as Figure 2 is shown in Figure 4. 





2019 Research Papers Competition Presented by: 

7 





**Figure 3** : _CEI_ from imaginary average _EI_ events before and after each play sequence 

## **4. Sport Dataset** 

The highlight extraction technique can be applied to any sport. We demonstrate the technique by applying it to NHL hockey. We rely on a proprietary SPORTLOGiQ dataset built from computer vision that extracts key information from hockey games. The dataset used to evaluate game states consists of 8,810,580 events recorded in the NHL during the 2016-17 and 2017-18 regular seasons and playoffs. Each event represents an action taken by a player in the game. Each entry in the dataset lists game, team, and player associated with the event, timestamp, event name and type, x-y coordinates of the event, and outcome. This play-by-play data records 13 general action types. Each general action is itself given a more specific type and outcome, of which there are 108 unique values. The locations of events are stated using a coordinate system whose origin is at the ice center, and all locations are oriented such that the possession team is attacking the goal lying on the positive _x_ -axis. The unit of measure is feet. Adjusted X-coordinates run from -100 to +100, and Y-coordinates from -42.5 at the bottom to 42.5 at the top, and the origin is at the ice center. 

In addition to the information specific to each event, we also rely on the following contextual information provided by SPORTLOGiQ: home team; current score; number of skaters on the ice for each team; and whether or not each team's goalie is on the ice. 

### **4.1 Event Valuation Model** 

The highlight-reel extraction process is designed to be independent of the technique used to evaluate a game's actions.  Here, we use a Markov model to evaluate each game state. The Markov model has been applied widely in sports analytics, and has been applied specifically to the NHL by SPORTLOGiQ and its collaborators [7]. 

Following the Markov Game Models in [7,6], the game is described by a finite set of states, defined by the event type, location, outcome and team. A set of contexts are described, defined by game period, score differential, manpower differential and which team's goalies are on the ice. The contexts are chosen with the help of hockey experts, based on which contextual 





2019 Research Papers Competition Presented by: 

8 



information tends to have the greatest effect on players' behavior. The goal in defining contexts is to allow the model to distinguish between contexts that most affect the value of events within those contexts. Each state is assigned a probability distribution representing the likelihood that the play will transition from that state into another. This probability distribution is equal to the count of transitions from the state into each successive state. Value iteration is applied, first to the home team and then to the away team. In the case of the home team, reward is set to 1.0 for a home goal state and 0.0 for all other states. In the case of the away team, reward is set to 1.0 for an away goal state and 0.0 for all other states. Goal and neutral zone faceoff are terminal states. This results in two values for each state, each value representing the probability that either the home team or the away team will score before the end of the current play sequence, where each play sequence begins with a faceoff and terminates with either a faceoff or a goal. 



**Figure 4:** _CEI_ after removing _EI_ spillover across breaks in play and boosting near the beginning and end of each period 

## **5. Results** 

### **5.1 Single Event Highlights** 

First of all, setting aside the results of _EI_ and _CEI_ and evaluating events based only on their<sup>_I_</sup> _adj_ , we find useful results. Applying<sup>_I_</sup> _adj_ to hockey, in order to demonstrate the usefulness of the measure we exclude shots and goals, events whose interest in a highlight reel are self-evident. Instead, we look at events whose impact can vary greatly and can be either positive or negative depending on the context: passes and blocks. We rank these events by their impacts. See the appendix B for the clips that correspond to Table 1 and Table 2. 





2019 Research Papers Competition Presented by: 

9 



**Table 1:** _I adj_ of most negative impact passes and blocks 



**Table 2:** _I adj_ of highest positive impact passes and blocks 



### **5.2 Positive, negative and combined impacts** 

After testing several smoothing functions, we find that for hockey highlights, the Gaussian function produces the most interesting results. Next, we examine the effect of smoothing over a) the absolute impact of all events, b) the impact of positive impact events only, and c) the absolute impact negative impact events only. 

- Events with Positive and Negative Impact. This results in a highlight reel with plenty of swings in puck possession, such as when several shots occur near the net and the defending team is scrambling to win possession of the puck without success. 

- Only Events with Positive Impact. Limiting the sequence to positive impact events only produces the most exciting highlight reel with plenty of high danger chances and shots. 

- Only Events with Negative Impact. Limiting the sequence to negative impact events only, the result is a set of clips that feature moments that could have been big scoring opportunities but for an error - a player misses a reception, loses the puck in a dangerous position, etc. 

The url to view the output of each approach is listed in the appendix B. 

### **5.3 Auto-Generated Mini-Game** 

Mini-games are popular formats for fans to re-watch games. Typically, the games are shortened to about a third of their usual length, as in the popular "90 in 30" soccer format. The techniques described here can be modified to produce this format, simply by setting a high number of highlight seconds and a wide _EI_ tail parameter. In this case, we treat every whistle as a break in play, rather than only treating intermissions between periods as such. We also increase the standard deviation of the Gaussian _EI_ function to accommodate longer play sequences. We ignore any play sequences with less than 10 events. These result in a more fragmented-looking vizualisation as seen in Figure 5. The resulting set of clips can be viewed at the corresponding link in Appendix B. 

2019 Research Papers Competition Presented by: 





10 





**Figure 5:** _CEI_ for mini-game with goal _I_ included 

### **5.4 Graphical Game Summary** 

The graphical display of _CEI_ is a useful tool for deciding what parameters to set for extracting game highlights, giving a sense of the most dramatic moments in a game. Another use-case for this graphical representation is worth noting. Instead of producing a single _CEI_ function over the course of a game, we can produce two: one for each team. The greater the _EI_ , the more dominant a team. Plotting both against each other produces a graph that acts as a simple, clear visual representation of the ebb and flow of a game over time. 

While visual game summaries do already exist, they tend to rely on an aggregate of no more than a handful of basic measures, such as shots or goals. _CEI_ allows us to plot a representation that accounts for all events in a game, while also removing the noise that would result from simply plotting discrete event values for each team. An example is shown in Figure 6. 

## **6. Discussion** 

We have introduced a framework for automatic highlight and lowlight generation that can be applied to many sports. This framework can accommodate a host of requirements, from the case of single-second social media clip reels to shortened mini-games. We have shown that the same approach can produce interesting visual narratives of a game. 

The nature of sports as entertainment is such that interesting events often occur whose interest will not be reflected in the events' value: near-events that don't quite materialize; events executed in particularly unusual ways; even celebrations can be of much interest that will never be captured with this approach. On the other hand, as in-game valuation models continue to improve in major sports, the highlight framework's output will become more and more compelling. 

This approach is generalized to the greatest extent possible. In producing results from Ice Hockey data, modifications were inevitably made to best accommodate the nature of the game. 





2019 Research Papers Competition Presented by: 

11 



Further work can be done on the specific needs within each sport and how best to integrate this framework given those needs. 



**Figure 6:** Graphical summary of VGK vs WSH, Game 5 of 17/18 NHL Stanley Cup final 

Ultimately, the correspondence between _EI_ and fan interest remains an assumption. It would be worthwhile to explore viewer responses to various parameterizations of the techniques described here using A/B testing or a similar approach. 

The use-cases of isolating high and low-impact events need not be limited to media. The same clips could also be used to highlight a player's strengths and weaknesses to coaching staff in game reviews and in scouting. 

## **Acknowledgements** 

The authors wish to reiterate the usefulness of Oliver Schulte’s past work on Markov game models to this research. Thanks to Jesus Servin who gave the highlight reels their edge. Nick Czuzoj-Shulman and Matt Perri were a great help in studying the early output of these techniques. David Yu and Sam Gregory kept gave useful feedback along the way. 





2019 Research Papers Competition Presented by: 

12 



## **References** 

[1] Robert B. Gramacy, Matt Taddy, and Sen Tian. Estimating player contribution in hockey with regularized logistic regression. Journal of Quantitative Analysis in Sports, 9(1). 

[2] Brian Burke. Expected point values, 2009. URL <u>htp://archive.advancedfootballanalytcs.com/2009/12/expected-point-values.html.</u> 

[3] Dan Cervone, Alexander D’Amour, Luke Bornn, and Kirk Goldsberry. Pointwise: Predicting points and valuing decisions in real time with NBA optical tracking data. _Sloan Sports Analytics Conference_ , 2014. 

[4] Guiliang Liu and Oliver Schulte. Deep reinforcement learning in ice hockey for context-aware player evaluation. _IJCAI-ECAI-18_ , 2018. 

[5] Stephen Pettigrew. Assessing the offensive productivity of NHL players using in-game win probabilities. 

[6] Oliver Schulte, Mahmoud Khademi, Sajjad Gholami, Zeyu Zhao, Mehrsan Javan, and Philippe Desaulniers. A Markov game model for valuing actions, locations, and team performance in ice hockey. _Data Mining and Knowledge Discovery_ , 31(6):1735–1757, 2017. 

[7] Oliver Schulte, Zeyu Zhao, Mehrsan Javan, and Philippe Desaulniers. Apples-to-apples: Clustering and ranking NHL players using location information and scoring impact. _Sloan Sports Analytics Conference_ , 2017. 





2019 Research Papers Competition Presented by: 

13 



## **Appendix** 

## **A** 

## **Code for minimum entropy requirement** 







2019 Research Papers Competition Presented by: 

14 



## **B** 

## **Video playlist urls** 

Playlist url for Table 1: <u>https://www.youtube.com/playlist?list=PL93Hzatf7cllaMlcuLyrdGssUmYWl_zcz</u> Playlist url for Table 2: <u>https://www.youtube.com/playlist?list=PL93Hzatf7clnwX5lcxcY8Aqe_9OLCfasp</u> Playlist url for 60-second highlight reels - positive impact, negative impact and both <u>https://www.youtube.com/playlist?list=PL93Hzatf7clmdCNbUHEJE0BuTnUbo870m</u> url for 20-minute minigame <u>https://www.youtube.com/playlist?list=PL93Hzatf7clnYQUY_sVrU7zEcGWmXHoha</u> 





2019 Research Papers Competition Presented by: 

15 


