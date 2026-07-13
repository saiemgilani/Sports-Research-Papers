<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2024/2024 - Risks and rewards of executing transition events from settled possession - Unknown Authors.pdf -->



# **Risks and rewards of executing transition events from settled possession.** 

All the safety of De la Fuente’s Spain with the excitement of Allardyce’s transitional Bolton; what is the catch? Daniel A. Pritchard 

## **Introduction** 

Tactics change as different teams choose to set up according to how they evaluate one simple trade-off, the risk of conceding versus the reward of creating goalscoring opportunities. Over the last 10 years resource dominant teams have largely, though with a few exceptions, employed positional play principles to maximise this trade off. Those sides seek to reduce conceding risk by keeping possession, even adopting more aggressive pressing principles, peaking before crowdless pandemic football<sup>1–3</sup> , to reduce opposition opportunities further. The tendency to recycle possession after a turnover for more pure positional sides has often allowed an opponent time to set up an organised block to reduce goalscoring opportunities. The top sides with the attacking talent to break these organised blocks down accepted that trade-off; positional play creating a spacing framework to break low blocks down with passing diamonds, triangles and fluid movement while maintaining said spacing. 

The success by counter strategies like Jürgen Klopp’s gegenpressing Dortmund was, as previously stated, adopted by the likes of positional play ‘high priest’ Pep Guardiola, more players have become involved in build up to increase passing options and thus the effectiveness of pressing reduced<sup>4</sup> , leaving few pure gegenpressing teams left outside of the tactic’s native Germany. Reaction to positional play dominance has been, ‘if you cannot beat them-join them” Klopp’s Liverpool slowly adopted principles of it after facing more low blocks in the English Premier League than he did in the German Bundesliga<sup>5,6</sup> . This has, by the end of the 2023/24 season left the tactical landscape of football in a state of dominance by what football analytics podcast ‘The Double Pivot’ has called FiveGuys tactics<sup>7</sup> ; having a rest defence and buildup unit of 5 or sometimes more players which has proliferated down to less resource rich sides<sup>7,8</sup> . 

In the last few seasons, a growing number of these lower talent teams have struggled to see success following the trade offs that high talent positional play teams have accepted, namely facing down and breaking low blocks. To use some examples from the Premier League Brenden Roger’s Leicester failed to reach the Champions League with such an approach and high net spend, and while Graham Potter’s Brighton side were impressive given their resources, they did not reach European places under him<sup>9</sup> . Continuing to follow Brighton, it was under their next coach that they saw their highest modern league 

**1** 



finish and finally European football, employing the tactics which shall be the focus of my research. 

### **1.1 Torero and Transition Events** 

Brighton and a growing number of teams below the elite level are seeking to mitigate the typical low block trade-off of positional play by create artificial transition-like attacks from settled possession in both women’s and men’s games<sup>10–13</sup> . The tactic which hereafter I shall call Torero – Italian and other Latin language’s word for bullfighter, and satisfyingly containing Tor the German word for goal, is trading the risk of losing possession in potentially dangerous areas to attack in space further up the pitch. While this is not a counter to the Five-Guys trend, Roberto De Zerbi often built up with 6 players at Brighton, it does seek to use the proliferation of positional play and its pressing evolution to draw the opposition out of a block<sup>12,13</sup> . 

Key to this strategy is the event of transition itself, hereafter referred to as a Transition event (TE), when the opposition have ideally been drawn out and it is time to attack. There has been little analysis of how this part of the strategy plays out, if it is often passes or carries, when the ideal conditions are, and how much, in terms of chance creation, are these transition-like attacks resembling counterattacks from turnovers. On the other hand there has been some analysis on successful counter strategies like sitting off and denying transition space for example<sup>14</sup> , but is this ideal or can teams exact a higher reward trade-off for risking more TEs, questions like where TEs are being initiated and how to effectively stop them are yet to be addressed in the public space. 

### **1.2 Aims** 

There has been plenty of public tactical analysis of Torero, and even some dives into existing statistics<sup>14,15</sup> , but little that looks to address TEs, their risks and upsides. My aim then is to use Statsbomb’s extensive event and 360 data to address TEs both descriptively and prescriptively. I want to explore how to find TEs in event data and create an event statistic for analytical use. I aimed use it to describe where teams are transitioning, by what means, and identify players capable of carrying out TEs. Additionally, I will use the insights provided by 360 level data to understand their topology and find prescriptive insights to what until now has been hypothesis. What is the risk of Torero are and whether TEs are the most vulnerable link in the chain, as well as how they can be best leveraged. 

**2** 



## **Methodology** 

The dataset I used for this analysis was comprised of 10 English Premier League sides for the full 2022/23-2023/24 seasons. I chose these sides to have a mixture of tactical styles; amongst the recognisable Torero teams of Aston Villa, Brighton, and Tottenham, I have chosen ‘block & counter’ sides Everton and West Ham, positional play sides Manchester City and Arsenal, and ‘press & posses’ sides Chelsea and Liverpool. As well as the more difficult to pigeonhole Manchester United, who’s coach Erik Ten Haag previously deployed Torero like tactics at Ajax. 

### **2.1 Discovery Phase** 

My first challenge was to find TEs in the event data, which meant defining them from the build-up phase. I decided to define the TE as the event that first progresses the ball into the transition-like attack, excluding events that may unlock the possibility to transition, e.g. a pass into a player in space who then executes a progressive pass. The latter example, while important to a Torero style, both only creates the opportunity to launch a transition-like attack and would present far more difficulty finding. 

As I could not make the same assumptions as other methods of identifying transitions after turnovers<sup>16,17</sup> , I tried to find transition events from settled possession by identifying changes of tempo in event data. My method for doing so was to calculate a progression per second (ΔTempo) statistic for every event within a given possession, utilising the match timestamp and X axis coordinate of events (e.g. Pass end location X – Pass event X). This unfortunately did not work, the short timeframe of one touch passes, in which ball receipt and pass share the same timestamp or receiving and carrying the ball on the run made dividing by seconds impossible. Adding an insignificant duration of 0.01 seconds to any event meant even small amounts of progression were awarded high progression/second if the event was a bounce pass or running carry. Furthermore, this approach highly awarded long passes, particularly clearances from goalkeepers; while goalkeepers can be an important avenue for launching transition like attacks, it was not what I was searching for. 

For the successful approach I made use of Statsbomb’s 360 frames to visualise the area of the pitch around the actor (player executing the event) at the time of an event. As the key aspects of Torero are pulling an opposition block out of position then exploiting the space left by this, I first looked for players being pulled out of their defensive position. As 360 frames are blind to the name of any player other than the actor, I calculated maximum (x = closest to opposition goal, y = right side edge of pitch) and minimum (x = closest to possession goal, y = left side edge of pitch) x and y positions of opposition players for each event. When averaged across a 45-minute half these values provided a reasonable idea of the average area of the defensive block of the opposition side<sup>18</sup> , players outside of that block could then be identified as ‘pulled’ (for pulled out of position). After experimentation as well as match footage I identified 3 pulled players as a potential opportunity for a TE as it struck a balance between the 1 or 2 players who may 

**3** 



be tasked with pressuring the possession team at any given time, and not losing too many potential TEs. When 3 or more players were pulled out of position, I could then identify TEs by finding events which ‘packed’ players behind the ball, therefore being behind the play, using the number of defenders goalside of the actor, a stat provided in the 360 data. After much experimentation with match footage, I found that packing 3 or more players, reducing a possible 10 outfield players to 7 in front of the ball, provided a significant move into space to carry out and transition-like attack. Having identified TEs as events packing 3 or more players while 3 or more players have been pulled, I further separated TE events into types of progression by passes (TEpass), which included line breaking passes as according to Statsbomb’s model, and carries, which also included dribbles (TEcarry). 

### **2.2 Definition Phase** 

To further refine TEs I added a number of filters after watching match footage of events discovered in the first phase, these included the play pattern coming from regular play (as defined in Statsbomb’s event data) as well as the stipulation that the possession side must have played at least 3 passes or a ‘Pausa’ (no event for greater than 1.5 seconds) after regaining the ball to ensure a settled possession state. Furthermore, I filtered for events taking part in the defensive 60% of the pitch of the possession team, ensuring events took place after an attempt to draw an opposition press. 

As I also aimed to study the risks of Torero, I also had to find unsuccessful attempts at executing a TE using 360 data. To begin I started with the definitions already laid out. Unsuccessful TE attempts must take place in settled possession (3 passes after possession regain or Pausa) and in the defensive 60% of the field, while 3 or more defending players have been pulled. An unsuccessful attempt therefore was any time possession was lost during this play state, in the event data this was any time a new possession was started e.g., a blocked pass goes out for a throw in for the possession team, starting a new possession for the same team. 

**4** 



## **Applications** 

The scope of this paper is unfortunately due to time constraints, limited to applications of the TE statistic itself, downstream trade-offs of the Torero approach, and its optimisation in the public space are therefore left to a later publication (hopefully) or other researchers. 

### **3.1 Scouting** 

For sides looking to implement Torero tactic, finding players who can execute TEs well should be a priority. Defining a TE statistic can help find players already executing a high volume of TEs. It should be said however that the situational nature of TEs, both with regard to pulling defenders out of position and licence to execute risky passes or carries to pack players, is dependent on tactical context. More research is needed to identify player who could execute high value TEs but are limited in doing so for tactical reasons. 

For players in my dataset of 10 premier league clubs I hypothesised a list of top TE executors to be limited to defenders, goalkeepers and pivot midfielders, particularly from clubs playing a Torero style. 



This hypothesis largely held up, many of the players within the figure and falling just below the high median set for it were players from deeper positions tasked with pulling defenders out of position and playing the ball into attacker with more space to operate as a result. Several goalkeepers, particularly Jason Steele of Brighton, feature highly in the list. However, the above figure contains a couple of surprises, the first being that it heavily features players from Sean Dyche’s Everton side. It is not clear (without watching a lot more match footage than I have time for) if Everton are deliberately trying to draw the opposition press or simply on the receiving end of high pressing game plans, but as 

**5** 



TEs have been filtered to settled possession it would seem to indicate that this may well be deliberate; another feather to add to the cap of the Dyche-pilled among us. This also serves to demonstrate that not all ‘defend and transition’ sides are built in the same way, by comparison the West Ham side coached by David Moyes played far fewer TEs, with only one player featured on the list of the top 10, though that player, Mohammed Kudus presents another surprise. Several attacking and wide midfield players feature highly on this list, Harry Kane a forward, who at Tottenham would regularly drop into midfield positions, also falls just outside of it. After reviewing this in match footage it appears that another successful way of first drawing the opposition press and packing them is a dropping attacking midfielder, winger, or even forward. This could be particularly effective against man to man pressing systems, drawing at least one defender deeper with an attacking player and creating a one vs one opportunity that favours the attacker. The overloads, more attacking players in an area of the pitch than defenders, created by dropping an attacker into the build-up phase are thought of more often as a late attacking stage method for entering the defending box. In a Torero style, however, there is little reason an overload needs to occur immediately outside the defending box if an overload in a build-up phase can create a transition-like attack with a higher likelihood of getting into the opposition box. 

### **3.2 Opposition Analysis** 

The second immediate application of creating a TE statistic is where they are being executed, it is not hard to see that knowing where a side commonly wants to execute TEs, or where that want to play them into could help a defending team. A tactic we have seen adopted against the Torero style is to play a static defence and refusing to be pulled out of position, I believe that this approach, while effective, may be leaving attacking upside on the table. My hypothesis that pressuring the attacking side’s regular TE outlets, may lead to more regularly dangerous turnovers as well and not surrendering possession to side’s built for and more comfortable on the ball, this however requires more downstream analysis to confirm. 

**6** 





Regardless with just the TE statistic identified, the information could be used to Coach game specific pressing or backline dropping triggers and defend ball receiving space effectively. Above I have tried to show this for the 10 sides in the dataset, so as not to overload the figure with two season worth of passes, and to demonstrate a set or TEs from an average match, the median number of TEs for each side was calculated, I then filtered for the matches (n) in which a median number of TEs were executed. Several insights can be quickly gleaned even in this general approach on several teams rather than an in-depth approach to one, as is the case in opposition analysis. Some of these are Brighton’s right side dominate TE execution, vice versa Aston Villa’s left side bias. Others like Everton are more balances but limited almost entirely to the wings. This analysis also reveals that few TEpass are directly entering the final third revealing that there should be more opportunity to recover the ball before a dangerous attack can develop. 

### **<mark>3.3 Where next?</mark>** 

As I have already described throughout this insight section any prescriptive tactical insights are yet to be researched & follow up studies are needed that can leverage this approach further or provide counters to it. Questions on the downstream results of TEs like how to reduce probability of unsuccessful TEs & vice versa, and could the trade-off scale up to sides with more possession are obvious starting places from valuable research that could impact decision making at clubs. Similarly, there are on pitch tactical questions like when the optimal time is to execute a TE in which data departments are only just starting to impact. 

Torero has proven somewhat successful for clubs just outside the elite; Aston Villa achieved Champions League football for the first time in over 40 years and have risen from midtable xGoal Difference to top 8. Brighton achieved their first taste of European football under a Torero style, while Tottenham look like dangerous challengers again after 

**7** 



a several year decline from their Champions League regular peak. In the Bundesliga Bayer Leverkusen ended 11 years of Bayern Munich’s domestic dominance against the odds adopting Torero principles. Using data to maximise the approach or to counter a potentially growing number of Torero teams is, to me at least, the next big tactical landscape shift for teams below the elite and may well be the answer to the style evolving on its way into the elite. 

**8** 



## **References** 

1. Desmond, R. Pressing from the Front – Tactical Trends in 2020. _TheMastermindSite_ https://themastermindsite.com/2021/01/16/pressing-from-the-fronttactical-trends-in-2020/ (2021). 

2. McKeever, P. English Premier League 2021-22 Stats. _Opta Analyst_ https://theanalyst.com/eu/2022/08/premier-league-stats-2022-23/ (2022). 

3. McKeever, P. Premier League Stats: 2023-24 Season. _Opta Analyst_ 

https://theanalyst.com/2023/08/premier-league-stats-2023-24 (2023). 

4. Football Tactics: Build-up Play in the Face of Pressing | Coachbetter Blog: News and Case related topics. https://www.coachbetter.com/blog/soccer-tactics-build-upplay-in-the-face-of-pressing. 

5. Wizard, T. From Rangnick to Klopp: The Rise of Gegenpressing. _Medium_ https://medium.com/@tacticalwizard/from-rangnick-to-klopp-the-rise-ofgegenpressing-5dee25907ca4 (2024). 

6. The evolution of Jürgen Klopp’s tactics at Liverpool. _The Coaches’ Voice_ https://www.coachesvoice.com/cv/jurgen-klopp-tactics-liverpool/. 

7. Fullbacks and the Rise of Five Guys Tactics. _Apple Podcasts_ https://podcasts.apple.com/ch/podcast/fullbacks-and-the-rise-of-five-guystactics/id1121866859?i=1000656301811. 

8. MG. The Practical Guide to Actually Understanding Positional Play. _Touchline Theory_ https://touchlinetheory.com/the-practical-guide-to-actually-understandingpositional-play/ (2021). 

9. FC, A. Data in Context: How Did Graham Potter’s Brighton Achieve a ‘Big Six’ Style of Play with a Bottom Six Budget? _Analytics FC_ 

https://analyticsfc.co.uk/blog/2022/09/20/data-in-context-how-did-graham-pottersbrighton-achieve-a-big-six-style-of-play-with-a-bottom-six-budget/ (2022). 

10. _Pep Guardiola: Roberto De Zerbi Is One of the Most Influential Managers of the Last 20 Years_ . (2023). 

11. FC, A. Is Transition-Attacking the NWSL’s New Meta? _Analytics FC_ 

https://analyticsfc.co.uk/blog/2024/08/14/is-transition-attacking-the-nwsls-new-meta/ (2024). 

12. A year under Emery: How he’s transformed Aston Villa. https://www.premierleague.com/news/3750635. 

13. Nils. Tactical Masterclass: How Xabi Alonso’s Ingenious Strategies Revitalized Bayer Leverkusen. _Soccer-Coaches_ https://soccer-coaches.com/tactical-masterclassxabi-alonsos-bayer-leverkusen/ (2024). 

14. FC, A. Should you sit deep against Brighton? _Analytics FC_ 

https://analyticsfc.co.uk/blog/2023/10/16/should-you-sit-deep-against-brighton/ (2023). 

**9** 



15. FC, A. St Pauli’s year of Hürzeler – now also playing the best football in the 2. Bundesliga. _Analytics FC_ https://analyticsfc.co.uk/blog/2023/11/10/st-paulis-year-ofhurzeler-now-also-playing-the-best-football-in-the-2-bundesliga/ (2023). 

16. Eusebio, P., Prieto-González, P. & Marcelino, R. Decoding the complexities of transitions in football: a comprehensive narrative review. _Ger. J. Exerc. Sport Res._ (2024) doi:10.1007/s12662-024-00951-9. 

17. Stewart, A. New Metrics: Transition Pass Data Added to TransferLab. _Analytics FC_ https://analyticsfc.co.uk/blog/2022/11/13/new-metrics-transition-pass-data-added-totransferlab/ (2022). 

18. Carey, M. Why Liverpool’s compact defence is Arne Slot’s first big win. _The New York Times_ . 

**10** 


