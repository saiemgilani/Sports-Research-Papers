<!-- source: 2016 Complementary Skills NBA.pdf -->



# **Accounting for Complementary Skill Sets When Evaluating NBA Players’ Values to a Speci�ic Team** 

Joseph Kuehn CSU East Bay Email: joseph.kuehn@csueastbay.edu 

#### **Abstract** 

This paper develops a player evaluation framework that stresses the importance of accounting for complementarities between teammates when evaluating players. This is done by developing a probabilistic model of a basketball possession as a progression of events, where the probability of each event’s occurrence is determined by the offensive players’ skills, the defensive players’ skills, and the complementarities between the skills of teammates. Evaluating players using this framework allows me to assess the substitutability between different game actions, the lineup-speci�ic value a player brings to a team, and the players that are the best and worst teammates. It also allows me to separately identify the individual effect from the effect teammates have on a player’s statistical production, and to evaluate whether player complementarities are valued in the market for NBA players in terms of higher salaries. I �ind that complementarities are under-valued, and that players are instead paid mainly for their individual statistical production. 

## **1 Introduction** 

A key element to constructing any NBA team lineup is understanding how well the skills of the players in that lineup complement each other. Like in any team setting, an NBA lineup can be better, or it can be worse, than the sum of its parts. Teams that have a good understanding of what player types complement each other, can use complementarities between teammates to overcome de�iciencies in talent, and win games against more skilled opponents. The effect of teammates is also important when evaluating player talent at the individual level. It is not uncommon to see below average players produce at an above average level when put in a lineup that accentuates their strengths, or conversely see a highly skilled player with below average numbers when playing with teammates with higher usage rates. This can make it dif�icult to distinguish between the ability of the individual player and the extent to which his performance has been in�luenced by his teammates. 

In this paper I develop a player evaluation framework that stresses the importance of accounting for complementarities between teammates when evaluating players. What separates this player evaluation scheme from previous ones¹ is the focus here on identifying the substitutability between different game actions, and then using that to quantify the complementary effect teammates have on one another. This framework allows me to compute the value a player brings to a _particular_ lineup taking teammate spillovers into account, and allows me to assess which players help and hurt their teammates’ production the most. It also allows me to separate out how much of a player’s statistical 

¹These include papers by Maymin, Maymin, and Shen[4], and Oh, Keshri, and Iyengar[5], whose modeling approaches are conceptually similar to mine, but differ in their focus and implementation, and by using game simulations to get expected outcomes. 



2016 Research Papers Competition Presented by: 



1 



production can be attributed to the player individually (and thus will translate to a new team) and how much is due to the team he is currently playing on (in which case you wouldn’t see the same statistical output if the player moved teams). Finally this framework allows me to assess how much value current GMs place on the spillover bene�its a player has on his teammates, by looking at whether NBA salaries re�lect these potential spillovers or are based solely on individual production.² 

## **2 Data** 

The data I use is play-by-play data from SI.com[3] for the 2014-2015 NBA season. With this data I record the 10 players on the court for each possession and the detailed result of the possession. To avoid trying to calculate ratings for players with few possessions, I only look at the 250 players with the most possessions during the 2014-2015 season. All the rest of the players are considered ”replacement” players. I also use data on player salaries for the 2015-2016 NBA season from ESPN.com[2]. 

## **3 Model** 

I model a basketball game as a series of possessions where each possession is a sequence of events that have the potential to generate value (i.e. points) for the offensive team. The probabilities with which each of these events occur determine the number of points a team receives in expectation per possession according to the model outlined in Section 3.1. The probabilities that certain events occur during a possession are then determined by the skills of the players on the court, and importantly the _interaction_ between those players and their teammates. The model determining these probabilities is outlined in Section 3.2. 

### **3.1 Event Tree Model** 

Each possession is modeled as a sequence of actions represented graphically by the tree structure in Figure 2 of the Appendix. On a given possession each of the �ive offensive players can either shoot from a number of locations on the court, turn the ball over in a number of ways (i.e. bad pass, offensive foul, etc.), or be fouled without shooting. If the player receives a non-shooting foul then the offensive possession starts over, while if they turn the ball over then the possession ends. If they shoot, then at each location there are 4 possibilities: they make the shot, they miss the shot, they make the shot and are fouled, or they miss the shot and are fouled. If the shot is made the team gets 2 or 3 points depending on the shot location, and if the player is fouled then the expected number of points depends on their free throw percentage. If the player misses the shot then there are 2 possibilities: an offensive rebound by one of the offensive players, which results in the possession starting over, or a defensive rebound which ends the possession. 

The probabilities with which each of these events occurs is determined by the individual player model in section 3.2. Given probabilities for each action for each of the �ive offensive players on the court, I can solve the event tree model for the expected number of points associated with each action and the expected number of points per possession. Thus the model is used to determine how the probabilities of particular actions being executed by a team of �ive players against �ive opposing players, affects the expected number of points per possession for the offensive team. 

²Arcidiacono, Kinsler, and Price[1] do a similar analysis in a setting with a more general model of player complementarities. 





2016 Research Papers Competition Presented by: 

2 



To evaluate the model I classify shots into 7 shooting locations and classify turnovers as either forced or unforced. I calculated the average probability of each event occurring during the 2014-2015 season, and then using those probabilities solved for the expected value of each event and the overall expected points per possession for the ”average” lineup of players. The results are in Table 1 below. 

Table 1: Probabilities of each event and the associated expected points, for a lineup of ”average” players during the 2014-2015 NBA season 

|Event|Average<br>Probability|Expected<br>Points|
|---|---|---|
|Possession||1.0765|
|2FGA: 0ft-3ft|24.1%|1.4626|
|2FGA: 4ft-8ft|11.0%|1.1569|
|2FGA: 9ft-15ft|9.1%|1.0539|
|2FGA: 16ft+|12.8%|0.9661|
|3FGA: 22ft-23ft|4.4%|1.3478|
|3FGA: 24ft-25ft|10.3%|1.2605|
|3FGA: 26ft+|6.7%|1.2032|
|TO Unforced|4.9%|0|
|TO Forced|7.0%|0|
|Non-ShootingFoul|9.7%|1.1055|



The results in the table indicate that for a lineup with 5 average players, the possession outcome with the highest expected point total is shooting from inside 3 feet. For this lineup, a possession that results in a shot from inside 3 feet will increase the team’s expected points per possession by 0.386 points over the average expected points per possession of 1.077 points. The worst outcome is a turnover as this drops the expected points on the possession to zero. These expected values take into account the probability that a player is fouled on a given shot, and the probability that an offensive rebound off a missed shot (or missed free throw) gives the offensive team another possession. 

### **3.2 Individual Player Model** 

I next model how individual player skills coalesce with the skills of teammates (and are counteracted by the defensive skills of opponents) to affect the probabilities that the events outlined above occur. Players create value for their team either directly through the probabilities that they themselves commit certain actions during a possession, or indirectly by affecting their teammates’ probabilities of committing certain actions. By affecting these probabilities, a player brings value to the team through the effect these changing probabilities have on the team’s expected points per possession. 

For each potential game event outlined above (e.g. taking a 2pt shot from inside 3 feet), I model the conditional probability of a particular offensive player, _j_ 1, with teammates _j_ 2 _, j_ 3 _, j_ 4 _, j_ 5, and opposing players _k_ 1 _, k_ 2 _, k_ 3 _, k_ 4 _, k_ 5, executing the particular event _E_<sup>_i_</sup> as: 





where _γj_<sup>_x_is the propensity of player</sup><sup>_j_1to commit action</sup><sup>_x_(and</sup><sup>_γ_</sup> _k_<sup>_x,def_</sup> is a defensive player’s ability to affect his opponent’s propensity to commit action _x_ ), and **X** ( **E**<sup>**i**</sup> ) is the set of actions with the same 



2016 Research Papers Competition Presented by: 



3 



parent node as action _E_<sup>_i_</sup> , in the tree in Figure 2. The parameter _βx_ measures the own-substitutability of action _x_ (e.g. how much the propensity of _j_ 1’s teammates to shoot a 2pt shot from inside 3 feet affects _j_ 1’s probability of doing so) and the parameter _δx,y_ measures the cross-substitutability of action _y_ on action _x_ (e.g. how much the propensity of _j_ 1’s teammate to shoot a 3pt shot from 24-25 feet out affects _j_ 1’s probability of shooting from inside 3 feet). Equation (2) shows that a player’s probability of executing a particular action during a possession (such as shooting a 3pt shot from 24-25 feet out), depends on their own propensity to commit the action, their teammate’s propensity to commit the action, the player and his teammates propensity to commit other actions during the possession (such as turning the ball over or shooting from another location), and the defensive players’ abilities to affect the probability of the event occurring. 

The individual player model is estimated using a 2-step approach where in the �irst step maximum likelihood is used to map observed probabilities into 3 player scores which measure, respectively, the player’s propensity to execute an event, the player’s effect on teammates’ propensities to execute an event, and the player’s defensive effect on opponents’ probabilities of executing an event. In the second stage I then use a least-squares approach to match these scores with the parameters ( _β_ and _δ_ ) and player ratings ( _γj_<sup>_x_and</sup><sup>_γ_</sup> _k_<sup>_x,def_</sup> ) of the above model. 

### **3.2.1 Substitution Parameters** 

Estimation of the model parameters tells us how substitutable certain player actions are. For example we can see how substituting in a player who is 10% more likely to shoot a 3pt �ield goal from 24-25 feet out, affects his teammates’ probabilities of shooting the same shot, and their probabilities of executing other events such as shooting from within 3 feet or committing a turnover. The estimated parameters are displayed in the table in Figure 1, and are interpreted as the effect a 1% increase in a player’s propensity to commit the column event during a possession, affects their teammates’ propensities to commit the row event. For example the entry in column 1, row 1 of -0.086, means that if you substitute in a player that is 10% more likely to shoot from within 3 feet, then all else equal this will decrease the probability that each teammate shoots from within 3 feet by 0.86%. 

Figure 1: Substitution Parameters: The estimated effect of a 1% increase in the probability a player executes the column action on the probabilities that his teammates execute the row action for a team of average players 

||**2FGA:    0ft-3ft**<br>**2FGA**<br>|**:    4ft-8ft**<br>**2F**<br>|**GA:    9ft-15ft 2F**<br>|**GA:    16ft+**<br>**3F**|**GA:    22ft-23ft 3F**|**GA:    24ft-25ft 3F**<br>|**GA:    26ft+**<br>|**TO    Unforced**<br>**T**|**O    Forced**|**Non-Shooting    Foul**<br>|
|---|---|---|---|---|---|---|---|---|---|---|
|**2FGA:    0ft-3ft**<br>|-0.08575<br>|-0.02014<br>|-0.07731|0.00696<br>|0.03133|-0.02421|-0.01671<br>|0.00547<br>|0.02333|-0.06957<br>|
|**2FGA:    4ft-8ft**<br>|-0.02979|-0.09915<br>|0.00857<br>|-0.00226|0.02151<br>|0.01117<br>|-0.01911<br>|-0.04382<br>|0.01722|-0.02027<br>|
|**2FGA:    9ft-15ft**<br>|0.02589<br>|-0.01043|-0.06482<br>|0.03572<br>|-0.06091<br>|-0.01012<br>|-0.01694|-0.01760|0.00331<br>|-0.05658<br>|
|**2FGA:    16ft+**<br>|-0.09587<br>|0.04233<br>|-0.02997<br>|-0.10692<br>|-0.08022<br>|-0.06114<br>|0.03038<br>|0.00511|-0.02927|-0.08281|
|**3FGA:    22ft-23ft**<br>|-0.00646<br>|-0.01485<br>|-0.06495|-0.02028<br>|-0.17842<br>|-0.01348<br>|-0.00136<br>|0.02654|0.00855|0.01333<br>|
|**3FGA:    24ft-25ft**<br>|-0.04388<br>|-0.04148<br>|0.01244<br>|-0.01496<br>|-0.00328|-0.11104<br>|-0.04846<br>|0.02827<br>|0.00761<br>|-0.01015|
|**3FGA:    26ft+**<br>|-0.01051<br>|-0.00891<br>|-0.00947|-0.04178<br>|0.00458|-0.05316|-0.14089|-0.05438<br>|-0.05666|0.12967<br>|
|**TO    Unforced**<br>|-0.00972<br>|-0.01017<br>|0.00435<br>|-0.01246<br>|0.01596|0.01117|0.01637<br>|-0.08693<br>|0.01311<br>|-0.00296|
|**TO    Forced**<br>|-0.00156<br>|-0.05478<br>|-0.00276|-0.01025<br>|0.01805<br>|0.01297|-0.00858<br>|-0.03656<br>|-0.22084<br>|0.01175<br>|
|**Non-Shooting    Fou**<br>|**l**<br>0.04050<br>|-0.00224|0.01097|-0.05517|-0.00427|0.01565|-0.02288|-0.04346|-0.01054|-0.14053|
|<br>|**Off    Reb Def    Reb**<br><br>||||||||||
|**Off    Reb**<br>|-0.1499<br>-0.0801<br><br>||||||||||
|**Def    Reb**|-0.0580<br>-0.1775||||||||||



The tables indicate that getting rebounds are the most substitutable action for teammates, in that a player who gets 10% more offensive rebounds really only helps his team get 4% more offensive rebounds in total because he is taking some rebounds away from his teammates. Defensive rebounds are 



2016 Research Papers Competition Presented by: 



4 



even more substitutable in that a player who gets 10% more defensive rebounds only helps his team get a little less than 3% more defensive rebounds in total, again because he is taking some rebounds away from teammates. Taking 3pt shots is also highly substitutable in that substituting in a player who takes 10% more 3pt shots from 22-23 feet out, will only increase the overall team’s probability of taking that shot during a possession by 2.9%, again since he is taking this shot away from teammates. This is contrasted with taking 2pt shots from within 3 feet, where substituting in a player who takes 10% more of these shots increases the overall team’s probability of taking that shot during a possession by 6.6%. This is because putting in a player with a propensity to take close-range shots doesn’t take as many close-range shots away from teammates, and instead leads to a lower probability of other events, such as the team taking 2pt �ield goals from outside 16 feet. 

The parameter results also indicate the substitutability between _different_ events. For example, the entry in column 1, row 2 of -0.0298, means that if you substitute in a player that is 10% more likely to shoot from within 3 feet, then this will decrease the probability that each teammate shoots at a location between 4-8 feet by 0.298%. Thus if you look at the �irst column you can see that a player who takes more close range shots from within 3 feet, decreases the probability that teammates take 2pt shots from outside 16 feet and 3pt shots between 24-25 feet, but also that there is a positive correlation between shooting close-range shots and getting non-shooting fouls. This positive correlation is most likely a result of players getting fouled as they drive to the basket for the close-range shot. 

### **3.2.2 Player Ratings** 

Estimation of the player model also leads to player ratings that tell us the propensity for players to commit certain actions during a possession (e.g. shoot from particular locations, turn the ball over, or be fouled), the probability they make or miss a shot (and the probability they are fouled during a shot) from a particular location, and the probability they get an offensive rebound off a missed shot from a particular location. I also get defensive player ratings which tell us how defensive players affect the probability that their opponent commits a particular action during a possession, makes a shot from a particular location, and gets a rebound off a missed shot. These ratings are estimated simultaneously with the substitution parameters above, and thus take into account the substitutability and complementarity between different actions. For example, a player who gets a lot of rebounds in a lineup where no one else gets rebounds will get a lower rebounding rating compared to a player who has similar rebounding statistics, but is in a lineup with other strong rebounders. The top 5 players for each rating are displayed in Tables 11 and 12 in the Appendix. 

## **4 Player Evaluations** 

With the estimated model I can then evaluate the value a player has to a lineup through their own offensiveoutput, theeffecttheyhaveonteammates’offensiveoutputs, andtheirdefensiveeffect. These player evaluations do not require simulation, but are instead based on how a player’s skills affect their own, _and their teammates_ , propensities to commit certain actions during a basketball possession, and the associated values of those actions based on the expected points they will produce, derived from the event model of section 3.1. These player valuations are lineup-speci�ic in that certain players’ skills coalesce better with particular teammates rather than others. For example the additional value Andre Drummond brings to a lineup that already contains Greg Monroe is less than the value he would provide to a lineup without another solid rebounder, particularly because Drummond’s biggest skill is his rebounding ( _γAD_<sup>_OR_= 0</sup><sup>_._167) and rebounding is highly substitutable (</sup><sup>_δOR,OR_=</sup><sup>_−_0</sup><sup>_._1499).</sup> 



2016 Research Papers Competition Presented by: 



5 



### **4.1 Lineup-Speci�ic Player Valuations** 

To illustrate how this model can generate lineup-speci�ic player valuations, I �irst look at the value players brought to the lineups they were a part of during the 2014-2015 NBA season. I do this by comparing the lineup’s expected points per possession with the player in the lineup versus the same lineup’s expected points per possession if the player were instead replaced by a ”replacement” player.³ This takes into account both the player’s direct contribution and his spillover contribution to teammates. 

Table 2: Players who caused the largest increase in their lineup’s expected points per possession 

|Player|Lineup|Increase in EVP|
|---|---|---|
|Anthony Davis|Tyreke Evans, Eric Gordon, Dante Cunningham, Omer Asik, Anthony Davis|0.0614|
|Al Horford|Kent Bazemore, Dennis Schroeder, Kyle Korver, Mike Scott, Al Horford|0.0610|
|Stephen Curry|Stephen Curry, Klay Thompson, Andre Iguodala, Draymond Green, Andrew Bogut|0.0609|
|Pau Gasol|Kirk Hinrich, Jimmy Butler, Mike Dunleavy, Pau Gasol, Joakim Noah|0.0575|
|LaMarcus Aldridge|Steve Blake, Damian Lillard, Nicolas Batum, LaMarcus Aldridge, Chris Kaman|0.0553|



Table 3: Players who caused the largest decrease in their opponent’s expected points per possession 

|Player|Lineup|OppChange in EVP|
|---|---|---|
|Zaza Pachulia|Brandon Knight, Khris Middleton, Giannis Antetokounmpo, Jared Dudley, Zaza Pachulia|-0.0648|
|Marc Gasol|Mike Conley, Courtney Lee, Tony Allen, Zach Randolph, Marc Gasol|-0.0506|
|John Wall|John Wall, Bradley Beal, Paul Pierce, Nene Hilario, Marcin Gortat|-0.0477|
|Andrew Bogut|Stephen Curry, Klay Thompson, Andre Iguodala, Draymond Green, Andrew Bogut|-0.0464|
|Kyle Lowry|Kyle Lowry, Lou Williams, DeMar DeRozan, Pattrick Patterson,Jonas Valanciunas|-0.0455|



Table 4: Players who caused the largest increase to the difference between their lineup’s offensive expected points per possession and expected points per possession given up on defense 

|Player|Lineup|Increase in EVP|
|---|---|---|
|Marc Gasol|Mike Conley, Courtney Lee, Tony Allen, Zach Randolph, Marc Gasol|0.0818|
|LaMarcus Aldridge|Damian Lillard, Wesley Matthews, Nicolas Batum, LaMarcus Aldridge, Robin Lopez|0.0721|
|Tyson Chandler|Devin Harris, Monta Ellis, Chandler Parsons, Al-Farouq Aminu, Tyson Chandler|0.0721|
|DeMarcus Cousins|Darren Collison, Ben McLemore, Rudy Gay, Jason Thompson, DeMarcus Cousins|0.0718|
|AnthonyDavis|Tyreke Evans, Eric Gordon, Dante Cunningham, Omer Asik, AnthonyDavis|0.0701|



Table 2 lists the 5 players that increased their respective lineup’s offensive expected points per possession by the largest amount. Table 3 lists the 5 players that decreased their respective lineup’s opponent’s expected points per possession by the largest amount. Table 4 then lists the 5 players that increased their respective lineup’s difference between expected points per possession on offense and expected points given up on defense, by the largest amount. As an example, the way to interpret the �irst number in Table 2 is that on offense Anthony Davis provides 0.065 more expected points per possession (or 6.5 more expected points per 100 possessions) than a replacement player to that lineup. 

### **4.2 Best Teammates** 

I can also evaluate which players were good or bad teammates by looking at which players increased or decreased _their teammates’_ expected points per possession by the largest amount, after subtracting 

³A replacement player has skills equal to the average skills of a player during the 2014-2015 NBA season that fell _outside_ of the top 250 players in terms of possessions. 



2016 Research Papers Competition Presented by: 



6 



out the player’s individual production. Table 5 lists the 3 players that increased (and decreased) their teammatesproduction by the most upon entering the respective lineup. These are then the playersthat had the largest positive (and negative) spillover effect on the offensive production of their teammates. 

Table 5: List of 3 players whom increased their teammates’ expected points per possession by the most and 3 players who decreased their teammates’ expected points per possession by the most 

||Best Teammates||
|---|---|---|
|Player|Lineup|Increase in<br>Teammate EVP|
|Wesley Johnson|Jeremy Lin, Wesley Johnson, Wayne Ellington, Jordan Hill, Ed Davis|0.0668|
|Joe Ingles<br>Kirk Hinrich|Dante Exum, Gordan Hayward, Joe Ingles, Derrick Favors, Rudy Gobert<br>Kirk Hinrich,JimmyButler, Mike Dunleavy, Pau Gasol,Joakim Noah|0.0579<br>0.0571|
||Worst Teammates||
|Player|Lineup|Increase in<br>Teammate EVP|
|Russell Westbrok|Russell Westbrook, Dion Waiters, Andre Roberson, Enes Kanter, Steven Adams|-0.1414|
|DeMarcus Cousins|Darren Collison, Ben McLemore, Rudy Gay, Jason Thompson, DeMarcus Cousins|-0.1356|
|Derrick Rose|Derrick Rose, Kirk Hinrich,JimmyButler, Pau Gasol,Joakim Noah|-0.1342|



### **4.3 Players Whose Teammates Helped Improve Their Stats by the Most (Least)** 

This player evaluation framework also allows me to look at which players saw the biggest increase in their individual production due to the lineups they were in. This is important because if a player is putting up good numbers because they are on a bad team, you would not expect these numbers to translate if the player goes to a better team, and if the player is putting up not as good numbers because they are on a good team, then they might have a higher production on a lesser team. I thus compared the individual expected points per possession that a player received in the lineup they appeared in the most during the 2014-2015 season, with the individual points per possession they would expect to receive on a team full of replacement players. The 5 players with the largest positive (and negative) change in expected points per possession due to the lineup they played in, are displayed in Table 6. 

Table 6: Players with the largest positive and largest negative change in expected points per possession due to the lineup they played the most time in during the 2014-2015 season 

|Largest positi<br>teammate eff|ve<br>ect|Largest n<br>teammat|egative<br>e effect|
|---|---|---|---|
|Player|Lineup Effect<br>on EVP|Player|Lineup Effect<br>on EVP|
|Jeremy Lin|0.0562|Rudy Gay|-0.0955|
|Jordan Clarkson|0.0556|Kyrie Irving|-0.0879|
|Gordon Hayward|0.0492|Lou Williams|-0.0843|
|Jordan Hill|0.0463|Anthony Davis|-0.0841|
|Michael Carter-Williams|0.0413|Kevin Love|-0.0839|



## **5 Does the NBA Player Market Take Into Account Complementarities?** 

To assess whether player salaries take into account the spillover bene�it a player provides to a team, I regress the log annual salary for each player for the 2015-2016 season, on the player’s own contribution to the expected points per possession for a lineup of average players, the player’s spillover 



2016 Research Papers Competition Presented by: 



7 



contribution to the expected points per possession for that lineup, and his defensive contribution to the lineup. I also include �ixed effects for the player’s position. The results are in Table 7. 

Table 7: Salary Regression 

|DepVaria|ble: ln(yearly|salary)|
|---|---|---|
|Variable|Coef�icient|SE|
|Own|16.373*|3.535|
|Team|-4.615|21.806|
|Def|2.037|11.621|
|SG|-0.109|0.170|
|SF|-0.232|0.185|
|PF|0.302|0.222|
|C|0.395|0.272|
|Const|15.169*|0.148|
|Obs|250||
|_R_<sup>2</sup>|0.12|9|



The results indicate that players are largely paid for their individual statistical output on offense. The coef�icient on teammate contribution is negative (but not statistically signi�icant at the 5% level) indicating that the market does not place a great enough value on a player’s potential spillover bene�it to teammates. The coef�icient on defense (which also is not signi�icant at the 5% level,) shows that defensive contributions are also undervalued compared to offensive output. These results indicate that NBA teams are not doing a good job of identifying the value a player brings to a team through his complementarities with existing players, and are largely paying players based on their individual offensive contributions. 

### **5.1 Free Agent Acquisitions** 

To illustrate how this paper’s player evaluation model could be used to take team complementarities into account when evaluating free agents, I look at the case of LaMarcus Aldridge during the 2015 NBA offseason. For the �ive teams he was most interested in joining (San Antonio, Portland, New York, Los Angeles, and Dallas), I look at the additional expected points per possession he would of brought to the lineup with the most possessions on each team, above the player he most likely would have replaced in the lineup. The results are in Table 8, and they indicate that the New York Knicks would have had the highest value for Aldridge. This is not surprising since they were one of the worst teams in 20142015. What is a little surprising is that the Spurs had a higher value for him than both the Lakers and Mavericks, two teams with much weaker lineups. If complementarities were not taken into account, Aldridge would have provided much more value to the Lakers than the Spurs because the Lakers had a weaker existing lineup. Once complementarities are taken into account, Aldridge is shown to be of greater value to the Spurs. This quanti�ies the conventional wisdom during the offseason that Aldridge was a good ”�it” with the Spurs. 

Table 8: Lineups that have the most value for LaMarcus Aldridge 

|Player|Rest of|Player|Increase in|Increase in|Increase in|
|---|---|---|---|---|---|
|In|Lineup|Replaced|Off Team EVP|Def Team EVP|Tot Team EVP|
|LaMarcus Aldridge|Jose Calderon, Langston Galloway, Carmelo Anthony, Cole Aldrich|Jason Smith|+0.0439|+0.0398|+0.0837|
|LaMarcus Aldridge|Steve Blake, Damian Lillard, Nicolas Batum, Chris Kaman|”Replacement”|+0.0553|+0.0242|+0.0795|
|LaMarcus Aldridge|Tony Parker, Danny Green, Kawhi Leonard, Tim Duncan|Boris Diaw|+0.0351|+0.0302|+0.0653|
|LaMarcus Aldridge|Jeremy Lin, Wesley Johnson, Kobe Bryant, Jordan Hill|Carlos Boozer|+0.0127|+0.0377|+0.0504|
|LaMarcus Aldridge|Devin Harris, Monta Ellis, Chandler Parsons, Dirk Nowitzki|Tyson Chandler|+0.0236|+0.0099|+0.0335|





2016 Research Papers Competition Presented by: 



8 



I also look at which team would provide Aldridge the best opportunity to showcase his skills. Table 9 lists the increase in Aldridge’s individual expected points per possession from joining each of the �ive teams. If Aldridge was solely interested in increasing his own points per possession than the best team for him to join would have been the Lakers since the lack of talent on their current roster would have meant Aldridge would not have had to ”compete” as much with teammates for statistical output. 

Table 9: Lineups that provide the most value to LaMarcus Aldridge 

|Player<br>In|Rest of<br>Lineup|Individual<br>EVP|
|---|---|---|
|LaMarcus Aldridge|Jeremy Lin, Wesley Johnson, Kobe Bryant, Jordan Hill|0.3699|
|LaMarcus Aldridge|Jose Calderon, Langston Galloway, Carmelo Anthony, Cole Aldrich|0..2850|
|LaMarcus Aldridge|Devin Harris, Monta Ellis, Chandler Parsons, Dirk Nowitzki|0.2833|
|LaMarcus Aldridge|Tony Parker, Danny Green, Kawhi Leonard, Tim Duncan|0.2680|
|LaMarcus Aldridge|Steve Blake, Damian Lillard, Nicolas Batum, Chris Kaman|0.2578|



### **5.2 Lineups That Took the Most Advantage of Complementarities** 

To conclude I look at what lineups during the 2014-2015 NBA season were the most successful at taking advantage of complementarities between teammates. I do this by comparing the expected points per possession for each lineup if complementarities are taken into account, with their expected points per possession if complementarities are ignored. The �ive teams that most took advantage of teammate complementarities are listed in Table 10. The lineups that were the most successful at taking advantage of complementarities were the lineups where low percentage shooters did not take shots away from high percentage shooters, and there was less shooting from locations with low expected point values that reduced the probability of shots coming from locations with high expected point values. 

Table 10: 2014-2015 lineups that took the most advantage of player complementarities 

|Lineup|Diff in EVP<br>from Comps|
|---|---|
|Andre Miller, Bradley Beal, Rasual Butler, Kevin Seraphin, Nene Hilario|0.1089|
|Kyle Lowry, DeMar DeRozan, Terrence Ross, Patrick Patterson, Jonas Valanciunas|0.1195|
|Kemba Walker, Gerald Henderson, Lance Stephenson, Cody Zeller, Al Jefferson|0.1259|
|Kirk Hinrich, Jimmy Butler, Mike Dunleavy, Pau Gasol, Joakim Noah|0.1308|
|TonyParker, Manu Ginobili, Kawhi Leonard, Tim Duncan, Boris Diaw|0.1323|



## **6 Conclusion** 

This paper introduces a framework for identifying the substitutability between player actions during a NBA game, and using that to derive player evaluations that take into account the complementarities between teammates in manufacturing production. I showed how this can be used to identify which players are good and bad teammates, and also to separate out how much of a player’s statistical output is due to their individual skills and how much is due to the team they play on. I also showed that current NBA salaries indicate that player complementarities are undervalued in the market for NBA talent, and that many teams could improve their rosters by better identifying spillovers between players, possibly with a framework similar to the one developed in this paper. One limitation of the current paper is that player actions are broadly de�ined, and so future work should adapt the current model to take advantage of more detailed player action data such as exact shot locations and defensive player positions. 



2016 Research Papers Competition Presented by: 



9 



## **References** 

- [1] Peter Arcidiacono, Josh Kinsler, and Joseph Price. Productivity spillovers in team production: Evidence from professional basketball, 2014. 

- [2] ESPN. Espn nba player salaries, 2015. URL `http://www.espn.go.com/nba/salaries` . 

- [3] Sports Illustrated. Sports illustrated nba play-by-play, 2015. URL `http://www.si.com` . 

- [4] Allan Maymin, Philip Maymin, and Eugene Shen. Nba chemistry: Positive and negative synergies in basketball. In _2012 MIT Sloan Sports Analytics Conference_ , 2012. 

- [5] Min-hwan Oh, Suraj Keshri, and Garud Iyengar. Graphical model for basketball match simulation. In _2015 MIT Sloan Sports Analytics Conference_ , 2015. 





2016 Research Papers Competition Presented by: 

10 



## **Appendix** 

Figure 2: Event Tree 



<!-- Start of picture text -->
Possession<br><!-- End of picture text -->



<!-- Start of picture text -->
2   pt.   FGA<br><!-- End of picture text -->



<!-- Start of picture text -->
3   pt.   FGA<br><!-- End of picture text -->



<!-- Start of picture text -->
Def   Non-­‐<br>Shooting   Foul<br>TO<br><!-- End of picture text -->



<!-- Start of picture text -->
FG   Missed<br><!-- End of picture text -->



<!-- Start of picture text -->
FG   Made<br>+   2<br><!-- End of picture text -->



<!-- Start of picture text -->
FG   Missed<br><!-- End of picture text -->



<!-- Start of picture text -->
FG   Made<br>+   3<br><!-- End of picture text -->



<!-- Start of picture text -->
Possession<br>Defensive<br>Possession<br><!-- End of picture text -->



<!-- Start of picture text -->
Fouled<br><!-- End of picture text -->



<!-- Start of picture text -->
Not   Fouled<br><!-- End of picture text -->



<!-- Start of picture text -->
Fouled<br><!-- End of picture text -->



<!-- Start of picture text -->
Not   Fouled<br><!-- End of picture text -->



<!-- Start of picture text -->
Not   Fouled<br><!-- End of picture text -->



<!-- Start of picture text -->
Fouled<br><!-- End of picture text -->



<!-- Start of picture text -->
Not   Fouled<br><!-- End of picture text -->



<!-- Start of picture text -->
Off   Reb<br><!-- End of picture text -->



<!-- Start of picture text -->
Make-­‐Miss<br>+1<br>Miss-­‐Make<br><!-- End of picture text -->



<!-- Start of picture text -->
2   Free<br>Throws<br><!-- End of picture text -->



<!-- Start of picture text -->
Off   Reb<br><!-- End of picture text -->



<!-- Start of picture text -->
Miss-­‐Miss<br><!-- End of picture text -->



<!-- Start of picture text -->
Off   Reb<br><!-- End of picture text -->



<!-- Start of picture text -->
Possession<br><!-- End of picture text -->



<!-- Start of picture text -->
Def   Reb<br>Defensive<br>Possesssion<br><!-- End of picture text -->



<!-- Start of picture text -->
FT   Made<br>+1<br><!-- End of picture text -->



<!-- Start of picture text -->
3   Free<br>Throws<br><!-- End of picture text -->



<!-- Start of picture text -->
...<br><!-- End of picture text -->



<!-- Start of picture text -->
Def   Reb<br><!-- End of picture text -->



<!-- Start of picture text -->
Defensive<br>Possession<br><!-- End of picture text -->



<!-- Start of picture text -->
Def   Reb<br>Defensive<br>Possesssion<br><!-- End of picture text -->



<!-- Start of picture text -->
FT   Made<br>+1<br>Defensive<br>Possession<br><!-- End of picture text -->



<!-- Start of picture text -->
Possession<br><!-- End of picture text -->



<!-- Start of picture text -->
Possession<br>Defensive<br>Possession<br><!-- End of picture text -->



<!-- Start of picture text -->
Possession<br>Defensive<br>Possession<br><!-- End of picture text -->



<!-- Start of picture text -->
Possession<br>Defensive<br>Possession<br><!-- End of picture text -->

Table 11: Top 5 Players in Possession Ratings 

||||||Offense||||||
|---|---|---|---|---|---|---|---|---|---|---|
|Rank|2FGA: 0ft-3ft|2FGA: 4ft-8ft|2FGA: 9ft-15ft|2FGA: 16ft+|3FGA: 22ft-23ft|3FGA: 24ft-25ft|3FGA: 26ft+|TO Unforced|TO Forced|Non-ShootingFoul|
|1<br> <br>2<br>3<br> <br>4<br>5<br>|DeMarcus Cousins<br>Tyreke Evans<br>Russell Westbrook<br>Enes Kanter<br>Andre Drummond|DeMarcus Cousins<br>Brook Lopez<br>Al Jefferson<br>Greg Monroe<br>Dwight Howard|Dwayne Wade<br>Chris Bosh<br>DeMar DeRozan<br>Al Jefferson<br>RudyGay|Marreese Speights<br>DeMar DeRozan<br>Dwayne Wade<br>LaMarcus Aldridge<br>Blake Grif�in|Anthony Morrow<br>Lou Williams<br>O.J. Mayo<br>Terrence Ross<br>AveryBradley<br>Defense|Lou Williams<br>Gerald Green<br>Greivis Vasquez<br>Terrence Ross<br>WesleyMatthews|Stephen Curry<br>Lou Williams<br>C.J. Miles<br>Jamal Crawford<br>KlayThompson|DeMarcus Cousins<br>Kevin Seraphin<br>Nene Hilario<br>Amir Johnson<br>Dwight Howard|Russell Westbrook<br>Derrick Rose<br>John Wall<br>LeBron James<br>Aaron Brooks|DeMarcus Cousins<br>Dirk Nowitzki<br>Chris Paul<br>DeAndre Jordan<br>Dwight Howard|
|Rank|2FGA: 0ft-3ft|2FGA: 4ft-8ft|2FGA: 9ft-15ft|2FGA: 16ft+|3FGA: 22ft-23ft|3FGA: 24ft-25ft|3FGA: 26ft+|TO Unforced|TO Forced|Non-ShootingFoul|
|1<br>2<br>3<br>4<br>5|Kris Humphries<br>Carl Landry<br>Miles Plumlee<br>J.J. Hickson<br>Serge Ibaka|Anthony Tolliver<br>Jonas Valanciunas<br>Robin Lopez<br>J.J. Barea<br>Shaun Livingston|Kyle Korver<br>Robin Lopez<br>Roy Hibbert<br>LaMarcus Aldridge<br>Tyler Zeller|Andrew Bogut<br>Marcin Gortat<br>Chris Kaman<br>Robin Lopez<br>Omer Asik|Marc Gasol<br>Chris Bosh<br>Al Horford<br>Chase Budinger<br>Kobe Bryant|Kent Basemore<br>Andre Roberson<br>Wesley Matthews<br>Reggie Jackson<br>Paul Millsap|Patrick Patterson<br>C.J. Miles<br>Amir Johnson<br>Andre Iguodala<br>Jamal Crawford|Marcus Smart<br>Dennis Schroder<br>Mario Chalmers<br>Manu Ginobili<br>Zaza Pachulia|Kyle Lowry<br>Tony Allen<br>Zaza Pachulia<br>Ty Lawson<br>Draymond Green|Otto Porter<br>Paul Pierce<br>O.J. Mayo<br>Marco Bellinelli<br>Andre Drummond|



Table 12: Top 5 Players in Rebound Ratings 

|Rank|Off Reb|Def Reb|
|---|---|---|
|1|Andre Drummond|DeAndre Jordan|
|2|DeAndre Jordan|Dwight Howard|
|3|Enes Kanter|Andre Drummond|
|4|Rudy Gobert|Pau Gasol|
|5|Ed Davis|Jordan Hill|





2016 Research Papers Competition Presented by: 



11 


