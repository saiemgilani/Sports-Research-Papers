<!-- source: 2011 Player Eval Techniques - NBA.pdf -->



MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 

A new player evaluation technique for players of the National Basketball Association (NBA) 

Jeremias Engelmann Karlsruhe Institute of Technology Karlsruhe, Germany jeremias.engelmann@googlemail.com 

February 14, 2011 

## Abstract 

I present a combination of player evaluation techniques that signifcantly outperforms regularized adjusted +/- in prediction accuracy. This approach models a basketball game as a finite state machine, which is a behavior model composed of a finite number of states, transitions between those states, and actions. This state machine consists of four states, a ’normal’ and an ’extra possession’-state for each of the two teams. The ’extra possession’-state can be reached through forcing opponent turnovers or offensive rebounds. Players get positive and negative credit assigned to them for executing certain actions or failure to do so. Variables that determine how credit gets split between players get optimized by minimizing the sum of squared residuals in the training data. NBA games from October through February were used to train each model. All models were evaluated in terms of their ability to predict the outcome of the remaining regular season games, which are not included in each models’ training set. Squared error of predicted vs. actual margin of victory was used as a measure of accuracy. 

# 1 The States 

In the context of this method we define four different states for a basketball game, a ’normal’ possession and an ’extra’ possession for each of the two teams. The winner of the initial jump ball starts in its ’normal’ state. This team stays in that state as long as the ball is not turned over or thrown at the basket. In case of a shot at the basket a team can enter the ’extra’ state through offensive rebounding. In that case it will then stay in that ’extra’ state as long as it is in possession of the ball. In case the shot was made or the opponent team grabbed the defensive rebound, the opponent will enter its ’normal’ state. An additional way of entering a teams’ ’extra’ state is by forcing the opponent team into a turnover while it is currently in its ’normal’ state. The team that forced the turnover will then, as before, stay in this ’extra’ state as long as is it in possession of the ball. Forcing a turnover when the opponent is currently in its’ ’extra’ state will simply result in the ’normal’ state for the teamed that forced the turnover. The different types of turnovers get treated equally. Blocks with ensuing defensive rebounds have the same effect as forcing turnovers. Which actions lead to which state is shown in Fig.1. Play by play files taken from [3] were used to determine the states. 

# 2 Assignment of credit 

Players get credit for actions they do on the court. How much credit they earn for a specific action depends on what state the game was in when the action was executed and on specific parameters, which will be explained in the next section. In the ’normal’ state players of the attacking team can get positive credit through either making a shot, making multiple free throws, assisting a made shot or just being on the court during a made shot. They can get negative credit either through missing a shot, missing free throws or just being on the court while a shot was missed by a teammate. Players of the defending team get positive credit if an opponent misses a shot and they get negative credit if the opponent makes a shot. In the ’normal’ state, before we distribute credit, we subtract the average amount of points that get scored league wide in a ’normal’ state possession, usually around 1 _._ 05 from the amount of points that were just scored. Because of this, making just a single free throw in a ’normal’ possession actually leads to negative credit being distributed between players of the attacking team (1 _−_ 1.05= _−_ 0 _._ 05 _<_ 0). Whenever the state transitions from a ’normal’ to an ’extra’ state the system keeps track on who was listed as responsible for the state transition. In most cases one player from each team is listed as responsible. The responsible player that is on the team which is now in ball possessions will be referred to as P-EP, players from the other team, the one that lost the ball, will be referred to as P-EN. If points were scored during the ’extra’ state, the positive credit gets split between the player who scored, the player who assisted on the score (if there is an assist) and P-EP. The negative credit gets assigned to P-EN. In those cases in which no specific player was listed as responsible for the turnover, e.g. in a 24-second violation, the entire 5-man unit which was oncourt during the turnover gets the credit split between them. Allowing the opponent to enter its’ ’extra’ state by letting the opponent grab an offensive rebound gets handled in the same way. If the 

2 

’extra’ state ends with no points scored during that state no credit, positive or negative, gets assigned to any player. That way, the quality of the steal, block and offensive rebound gets built into the system. 

# 3 Optimizing parameters in the state machine model 

In almost all cases where credit gets assigned it gets split between several players. How the credit gets split is determined by multiple variables. In case there were points scored in a ’normal’ possession the credit gets split between the shooter, the person giving the assist (if listed in the PBP file) and all other attackers on the court. In case there were points scored in an ’extra’ possession the credit gets split between the players responsible for the possession, the player who scored and the person who assisted. As was described above, in a ’normal’ possession, circa 1 _._ 05 points get subtracted from the amount of points scored. In an ’extra’ possession the full amount of scored points gets split. Before we split the credit between players, we split it between the two teams: Half of the resulting figure gets added as credit to players of the team who scored, the other half gets subtracted from the credit of the players of the team which was scored on. 

To give an example: P1 shoots an assisted 3-pointer in a ’normal’ possession. The assist was given by P2. 3 _−_ 1 _._ 05 = 1 _._ 95 gets split between both teams. 1 _._ 95 _/_ 2 = 0 _._ 975 and thus _−_ 0 _._ 975 gets distributed over all defenders, _−_ 0 _._ 195 for each. Our (in this scenario fictional) parameter for making an assisted 3- pointer is 0 _._ 6, the parameter for assisting it is 0 _._ 2 and the parameter for being an attacker and not being directly involved in an assisted made 3-pointer is also 0 _._ 2. P1 then gets 0 _._ 975 _∗_ 0 _._ 6 = 0 _._ 585 of credit, P2 would get 0 _._ 195, the remaining attackers would split 0 _._ 2 _∗_ 0 _._ 975 = 0 _._ 195 between them. The sum of parameters which are linked to the same action always have to add up to 1 _._ 0 To create a final player rating the sum of credit of each player has to be divided by the amount of possessions that player played in. The final model consists of over 40 parameters, each depending on state, amount of points scored, whether the made shot was assisted or not, whether free throws were made and which kind of action led to the ’extra’-state. Parameters were optimized the following way: Of the games between October and February each game was removed from the dataset once. Then, all player actions from all other games in the dataset were recorded, the game was put back into the dataset and another one was taken out and so forth. For the games that were taken out of the dataset the amount of possessions each player played were recorded. Using the parameters, the possession data from a game _Gi_ and the recorded actions from all other games that were not _Gi_ the squared differences between the actual outcome of that game and the outcome forecasted by the model was calculated. This was done for all games and the squared errors were summed up. The optimal parameters were chosen to be those which minimized the sum of those squared differences between actual and predicted outcome. 

3 

# 4 Team point differential as a forecasting method 

The average point differential of each team has long served as a rough forecasting method for future games. For this method the average point differential a team has collected from October through February, adjusted by its’ amount of home and road games, serves as a forecast for games in March and later. This method is equivalent to assigning each player 1 _/_ 5 of the average point differential of his team. The resulting number would have to be divided by the average amount of possessions of each game, circa 190, to get a possession based rating for each player. The state machine model (SM) was optimized to produce minimal error when combined with the forecast from this method. Optimal weighing of both methods was found using the technique described in the last section. The best weights turned to be 0 _._ 4 for SM and 0 _._ 6 for the point differential method (PD). 

# 5 Regularized adjusted plus minus (RAPM) 

Readers unfamiliar with this technique are advised to read [1]. To find the optimal value for _λ_ crossvalidation was done on the data from October through February for each year. _λ_ = 2000 was found to be the optimal value. Data from [2] was used for all computations. 

# 6 Comparison of accuracy 

To ensure fairness, all games that didn’t exist in both datasets from [2] and [3] were removed from the set in which it existed before any kind of training or testing was done. For the pure PD model, the PD+SM model and the RAPM model the squared difference between predicted and actual outcome of NBA games of March and April of all seasons were recorded. Root mean square error for the single seasons can be found in Table 1. A one-tailed paired t-test was performed on the data pairs to test for statistical significance. March and April contained 342 games in 2007, 350 in 2008, 337 in 2009 and 334 in 2010. Thus there were 1363 data pairs. The combination of the PD and the SM methods significantly outperformed RAPM (p _<_ 0 _._ 01) and the combination of PD and SM significantly outperformed pure PD (p _<_ 0 _._ 02). 

||2007|2008|2009|2010|
|---|---|---|---|---|
|RAPM|13.00|12.55|11.59|12.12|
|PD|13.02|11.79|11.55|11.81|
|PD+SM|12.88|11.70|11.50|11.65|



Table 1: RMSE for all methods and years 

# 7 Conclusions 

A new player evaluation technique, which uses a finite state machine to model basketball games has been shown to significantly improve prediction accuracy of 

4 

a point differential based forecasting method. The combination of both methods significantly outperforms regularized adjusted +/- (RAPM). 

# 8 Outlook 

Additional work will be done to see how a pure BoxScore based metric compares to these methods. Also, how much each method gains by using multiple years of data will be evaluated. Some initial work to include the coaches of NBA teams into RAPM was done but needs to be expanded. Different lambda values for coaches and players, offense and defense, and player position need to be evaluated. Whether the state machine model produces similar results with a smaller set of parameters will also be researched. Strength of schedule will be added to the state machine model. Finally, some work will be done to find a better predictor of NBA games using a combination of all methods described above. 

# 9 Acknowledgements 

I would like to thank the owners of the web pages [3] and [2] for making their data publicly available. 

# References 

- [1] Joe Sill, ”‘Improved NBA Adjusted +/- Using Regularization and Out-ofSample Testing”’; MIT Sloan Sports Analytics Conference, March 6, 2010 

- [2] `http://basketballvalue.com/downloads.php` 

- [3] `http://www.basketballgeek.com/data/` 

5 



<!-- Start of picture text -->
Turnover(A),<br>Made<br>Shot(A),<br>Missed<br>Shot(A)+Defensive<br>Reb(H)<br>Home- Away-<br>Normal Extra<br>Turnover(H)<br>Made<br>Shot(A), Missed<br>Missed Shot(A)+Offensive<br>Made Shot(H),<br>Reb(A)<br>Shot(A)+Defensive Missed<br>Reb(H)<br>Shot(H)+Defensive Missed<br>Reb(A)<br>Shot(H)+Offensive<br>Reb(H)<br>Turnover(H),<br>Made<br>Shot(H),<br>Missed<br>Shot(H)+Defensive<br>Reb(A)<br>Away- Home-<br>Normal Extra<br>Turnover(A)<br><!-- End of picture text -->

Figure 1: States and transitions 

6 


