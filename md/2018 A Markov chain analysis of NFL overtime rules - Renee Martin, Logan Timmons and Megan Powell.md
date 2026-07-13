<!-- source: 2018 A Markov chain analysis of NFL overtime rules - Renee Martin, Logan Timmons and Megan Powell.pdf -->

95 

Journal of Sports Analytics 4 (2018) 95–105 DOI 10.3233/JSA-170198 IOS Press 

# A Markov chain analysis of NFL overtime rules 

Renee Martin, Logan Timmons and Megan Powell<sup>∗</sup> _University of St. Francis, Joliet, IL, USA_ 

**Abstract** . In this paper, we consider the National Football League’s rules for overtime. We use Markov chain models to represent sudden death, modified sudden death 15-minute overtime, the newly changed modified sudden death 10-minute overtime, and our theoretical alternative modified sudden death. Through our model analysis, we find the average length of overtime and the probability of the team possessing the ball first during overtime winning the game. Our analysis shows that the modified sudden death rule change increased the average overtime from 7 minutes 1 second to 7 minutes 37 seconds and that the probability of the team possessing the ball first winning decreased from 59.9% to 55.4%. Furthermore, we predict the 10-minute overtime change will result in the team possessing the ball first winning 54.1% of the time and the probability of a game ending in a tie increasing to 11.2% from under 2% in the current 15-minute overtime. Finally, we propose a system where both teams are required to possess the ball at least once before the game ends and conclude this system would increase the average overtime length to 7 minutes 57 seconds and the probability of the team possessing the ball first winning would be 54.7%. 

Keywords: Markov chains, NFL, overtime, football, national football league, sudden death, modified sudden death 

## **1. Introduction** 

Prior to the 2010-2011 season, the NFL overtime rules stated that the first team to score a touchdown (TD), field goal (FG), or safety won the game whether or not both teams had received an opportunity to score. After the 2010-2011 season, the NFL slightly modified the overtime rules, in only playoff games, due to an abundance of criticism that had been circulating throughout the league that a coin toss was having too significant a role in the outcome of the game. The new rule does not allow the initial receiving team to win with a FG on their first possession, only with a TD. If the initial receiving team does not score a TD, the game returns to the old NFL overtime sudden death rules. In 2012, the NFL owners voted to extend the new overtime rules to regular season games. The only difference was that regular season games can end in a tie if the score remains tied after 

> ∗Corresponding author: Megan Powell, PhD, University of St. Francis, 500 Wilcox St., Joliet, IL 60435, USA. Tel.: +1 815 740 3458; Fax: +1 815 740 4285; E-mail: mpowell@stfrancis.edu. 

one standard 15-minute period, while playoff games continued to play standard 15-minute periods until one team wins. Then in 2017, the league changed the length of an overtime period from 15 minutes to 10 minutes. 

During the Divisional Round of the 2016 playoffs, the Arizona Cardinals beat the Green Bay Packers by scoring a TD on the first possession of overtime. The Packers never got a chance to possess the ball and lost their opportunity to advance to the NFC Championship (Brady, 2016). After the Cardinals scored on just three plays, there was much discussion on the fairness of the overtime rules including by Jim Buzinski, writer for SB Nation and co-founder of outsports.com (Buzinski, 2016). Buzinski strongly believes that the NFL needs to change the overtime rules in the playoffs stating, “Give each team at least one possession, no matter what happens on the first one.” In this paper, we create and analyze Markov chain models to represent the old sudden death (SD) rules, new modified sudden death (MSD) rules, the new MSD in 10 minutes rule (MSD-10) and a theoretical alternative modified sudden death (AMSD) 

2215-020X/18/$35.00 © 2018 – IOS Press and the authors. All rights reserved 

This article is published online with Open Access and distributed under the terms of the Creative Commons Attribution Non-Commercial License (CC BY-NC 4.0). 

96 

_R. Martin et al. / A Markov chain analysis of NFL overtime rules_ 

addressing Buzinski’s proposal where each team has at least one possession during overtime. We will use overtime data from NFL regular season games ending in 2010–2012 and 2013–2015 for SD and MSD models, respectively. We use the 2013–2105 overtime regular season data with modifications for the MSD-10 and AMSD. 

## **2. Literature review** 

## _2.1. Prior models_ 

Markov chain models have been previously used to model NFL overtime, and we improve upon these models as more data has become available for NFL overtime play. Our model is based on that proposed by Chris Jones (Jones, 2012), but insufficient overtime data under the MSD rules was available at that time. Because of the limited data, C. Jones used 2008 regulation time data and estimated how some of the probabilities would change during overtime. He concluded that with the SD rules, Team A (the initial receiving team) wins 64% of the time within 6 possessions and with MSD rules, Team A wins 52% of the time. We were able to limit our data search to overtime drives only since the MSD has been in place for a number of years now. However, we limited our model to only represent regular season overtime because insufficient playoff games have gone into overtime since the MSD rule update for analysis. Michael Jones (Jones, 2004) used a Markov chain model to represent the SD rules prior to the change, using 2002 regulation time drive data. As overtime data has become more readily accessible, we were able to include end of game ties and safeties, simplifying assumptions M. Jones neglected in his model. 

## _2.2. Alternative overtime format suggestions_ 

There have been a myriad of suggestions on how to improve the fairness of overtime, many of which were compiled by Carl Bialik (Bialik, 2003). Many suggest some version of bidding or divide and choose where to start the drive are more fair than the SD or MSD rules and gives neither team an advantage at the beginning of overtime (Che & Che, 2006; Che & Hendershott, 2007; Jones, 2012; Brams & Sanderson, 2012). In both scenarios, coaches determine a yardage from the end zone at which a team should start a possession. In auctioning, the team with the lower bid gains possession of the ball first, and in 

divide-and-choose, a coin flip decides which teams picks a yardage and which teams chooses if they want to have possession of the ball first. Che and Hendershott (2007) conclude that auctioning is better than divide-and-choose which is better than sudden death with the added corollary that the more capable team is more likely to win in the auctioning method. In his book Mathletics, Wayne Winston (2009) suggests moving the kickoff 5 yards to give the receiving team worse field position when starting their drive and predicts this would decrease Team A’s chances of winning in the SD format from 60% to 55%. 

M. Jones considered a first to six points scenario and suggested limiting time by restricting overtime to 6 possessions, the average number of possessions per quarter. He concludes that this method would have win probabilities of 0.491 for Team A and 0.393 for Team B, bringing the probability of ending in a tie up to 0.116 (Jones, 2004). We propose an alternative modified sudden death (AMSD) model where both teams are guaranteed possession of the ball at least once before the rules revert to SD with a result of Team A winning 54.7% of the time, higher than Jones’ 49.1%. 

## **3. NFL overtime analysis** 

## _3.1. Models_ 

In all NFL games that have gone into overtime, there have only been fourteen instances where teams who have won the coin toss have chosen not to receive the ball. Eight of the fourteen games resulted in the team choosing not to receive winning, three games ended with the team who chose to not receive never possessing the ball, and the others ended in a tie. In our model, we assume Team A to be the initial receiving team and Team B to be the initial kicking team and, since the game has made it to overtime, both teams are of equivalent strength. We use the Drive Finder tool at pro-football-reference.com (Finder, 2017) for all of the data including the number of FGs, TDs, safeties, defensive TDs, no scores, end of games, total possessions, length of possession, and length of overtime. Summaries of the data used in all the analyses can be found in the Appendix. 

## _3.1.1. Sudden death_ 

Table 1 shows the transition matrix for the possible outcomes for regular season games during overtime in the 2010–2012 seasons (See Table 17 in the 

_R. Martin et al. / A Markov chain analysis of NFL overtime rules_ 

97 

Appendix for Drive Results Data). For all transition matrices, the first column indicates the current state and the matrix gives the probabilities of entering the other states in the next possession. The sudden death rules state that whichever team scored first in any way wins, thus, the transition states for sudden death are only Team A possessing the ball (A Pos) and Team B possessing the ball (B Pos). 

Absorbing states are states that cannot be left once they are entered. In our model the absorbing states are defined as the game ending. The game ends when Team A or Team B scores or an end of game tie occurs (A Wins, B Wins, EOG Tie). In Table 1, the probabilities of 1 represent not being able to leave an absorbing state, while the probabilities of 0 represent states you cannot go back to. For example, in the first row when Team A possesses the ball (A Pos), it is not possible for Team A to transition to possessing the ball again (A Pos, A Pos). During the 2010–2012 seasons Team B would get the ball if Team A did not score (NS), this is shown in (A Pos, B Pos). Team A could win if they scored a FG or TD, as shown in (A Pos, A Wins). Next, (A Pos, B Wins) shows that the only way Team B can win when Team A has possession of the ball is on a safety (S). Lastly, (A Pos, EOG Tie) shows when the game ends in a tie because the game clock ran out while Team A has possession of the ball. The second row shows that when B subsequently possesses the ball and the results are symmetric to the first row. The game will continue on until one of the absorbing states are reached. 

## _3.1.2. Modified sudden death_ 

Table 2 shows the transition matrix for possible outcomes for modified sudden death rules. As in the sudden death model above, the number of FGs, TDs, safeties, defensive TD, no scores, end of games, and total possessions were used in the analyses (See Table 18 of the Appendix). The MSD rules state that both teams have the opportunity to possess the ball, unless the receiving team scores a TD on their first possession. After both teams have earned a possession the game returns to the SD rules. This change was implemented in order to create more fairness for each team, no matter who started with the ball. The transition states for MSD are Team A having the ball on the first possession (A First Pos), Team A scoring a FG on their first possession and Team B receiving the ball (B down by 3), Team A not scoring on first possession and Team B possessing the ball (B Pos), or ending in a tie because time ran out (EOG Tie). These rules allow Team B an opportunity to possess as long as they stop Team A from scoring a TD on the first possession. 

The absorbing states are again end of game situations. The differences between this model and the SD model relate to the first two possessions, which have unique rules relative to subsequent possessions. The first is that A may score but not end the game with a FG, and the second is that B can subsequently lose possession without scoring yet lose the game, since they are down by 3 points. Therefore, because it is highly unlikely a game will end in a tie in the first 

Table 1 

|||Sudden death|transition matrix|||
|---|---|---|---|---|---|
||A Pos|B Pos|A Wins|B Wins|EOG Tie|
|A Pos|0|NS|FG+TD|S|EOG|
|B Pos|NS|0|S|FG+TD|EOG|
|A Wins|0|0|1|0|0|
|B Wins|0|0|0|1|0|
|EOG Tie|0|0|0|0|1|



NS: No Score, FG: Field Goal, TD: Touchdown, S: Safety, EOG: End of Game. Each cell represents the probability of transition from the current state (first column) to a subsequent state (first row). 

Table 2 

||A First Pos|B down by3|A Pos|B Pos|A Wins|B Wins|EOG Tie|
|---|---|---|---|---|---|---|---|
|A First Pos|0|FG|0|NS+EOG|TD|S|0|
|B down by 3|0|0|FG|0|NS+EOG|TD|0|
|A Pos|0|0|0|NS|FG+TD|S|EOG|
|B Pos|0|0|NS|0|S|FG+TD|EOG|
|A Wins|0|0|0|0|1|0|0|
|B Wins|0|0|0|0|0|1|0|
|EOG Tie|0|0|0|0|0|0|1|



NS: No Score, FG: Field Goal, TD: Touch- down, S: Safety, EOG: End of Game Tie. 

_R. Martin et al. / A Markov chain analysis of NFL overtime rules_ 

98 

Table 3 

|A|First Pos|B down by3|B down by6|B down by7|B down by8|<br>A Pos|B Pos|A Wins|B Wins|EOG Tie|
|---|---|---|---|---|---|---|---|---|---|---|
|A First Pos|0|FG|TD+0PT|TD+1PT|TD+2PT|0|NS+EOG|0|S|0|
|B down by 3|0|0|0|0|0|FG|0|NS+EOG|TD|0|
|B down by 6|0|0|0|0|0|TD+0PT|0|1 - (TD+0/1 PT)|TD+1PT|0|
|B down by 7|0|0|0|0|0|TD+1PT|0|1 - (TD+1/2 PT)|TD+2PT|0|
|B down by 8|0|0|0|0|0|TD+2PT|0|1 - (TD+ 2PT)|0|0|
|A Pos|0|0|0|0|0|0|NS|FG+TD|S|EOG|
|B Pos|0|0|0|0|0|NS|0|S|FG+TD|EOG|
|A Wins|0|0|0|0|0|0|0|1|0|0|
|B Wins|0|0|0|0|0|0|0|0|1|0|
|EOG Tie|0|0|0|0|0|0|0|0|0|1|



NS: No Score, FG: Field Goal, TD+0PT: Touchdown with missed extra point(s), TD+1PT: Touchdown with extra kick, TD+2PT: Touchdown with two-point conversion, S: Safety, EOG: End of Game Tie. 

two possessions, we consider the probability of transitioning into EOG Tie in the first two possessions to be zero. The rows must still add to one, so we moved the probability of EOG Tie in the first possession to B Pos indicating A has not scored and B now has the ball. In the second row, we have moved the EOG probability to A Wins indicating B did not score and B loses by 3. 

## _3.1.3. Alternative modified sudden death_ 

Table 3 shows the Alternative Modified Sudden Death transition matrix. In this model we are proposing that both teams receive an opportunity to possess even if Team A scores a TD on their first possession. This allows Team B to be down by 0, 3, 6, 7, or 8 depending on what Team A did on their first possession. If Team B is down by 3, then Team A scored a FG. If they are down by 6, then Team A scored a TD and missed the extra point, whether they went for a one point or two-point conversion. Team B will be down by 7 or 8 if Team A scores a TD and makes the extra point(s). If Team B is down by 6, 7, or 8, it makes no sense to attempt a FG because they would still lose the game. In the rare event that Team B recovers an onside kick and scores, we consider this to end the game, since Team A had a chance to possess the ball and failed as is the case in the current MSD rules. 

## _3.2. Analysis_ 

under that ruleset by using the average length of a possession (2 minutes, 38 seconds). For each model we show the ending absorbing state matrix which gives the probability of ending in a given absorbing state if a team starts in a particular transition state. For our model analyses, we are mainly interested in the first row of this matrix which represents starting in the transition state of Team A’s first possession of the ball. Our model considers the beginning of overtime to be when A first possesses the ball, neglecting the time for the kickoff to Team A receiving the ball. See the Appendix Section 6.3 for the transition matrices with the overtime data. 

## _3.2.1. Sudden death (SD)_ 

From the Fundamental Matrix (Table 4) for the SD transition matrix, we have that the average number of possessions during overtime is the sum of the first row which represents how many times we expect each team to possess the ball. We take this sum and multiply by the average length of possession (2 minutes 38 seconds) to find the average length of overtime to be 7 minutes and 1 second. The actual average length of overtime from 2010–2012 was 7 minutes and 2 seconds. 

Table 5 shows our model’s results of the estimated probabilities of each team winning from the sudden death rules. In row one, we see Team A wins the game, on average 59.9% of the time, Team B wins 

For each model we show the transition matrix for the given rule set using the regular season overtime data for the years given. We then provide the Fundamental Matrix for each model which gives the total numberoftimesweexpectateamtobeinagivenstate (first row) after starting in a given state (first column) before absorption (game ending). From the Fundamental Matrix, we estimate the length of overtime 

Table 4 

Sudden death fundamental matrix 

||A Pos|B Pos|
|---|---|---|
|A Pos|1.685|0.974|
|B Pos|0.974|1.685|



This gives the number of times we expect A and B to possess the ball (first row) if A or B starts with the ball (first column). 

_R. Martin et al. / A Markov chain analysis of NFL overtime rules_ 

99 

Table 5 

Sudden death probability of ending in absorbing state matrix 

||A Wins|B Wins|EOG Tie|
|---|---|---|---|
|A Pos|0.599|0.389|0.017|
|B Pos|0.389|0.599|0.017|



This gives the probability of winning (first row) if A or B starts with the ball (first column). 

Table 6 

||A First Pos|B down by3|A Pos|B Pos|
|---|---|---|---|---|
|A First Pos|1|0.322|0.636|0.937|
|B down by 3|0|1|0.475|0.270|
|A Pos|0|0|1.476|0.838|
|B Pos|0|0|0.838|1.476|



First row gives the number of times A and B would possess the ball starting with A first possessing the ball. 

Table 7 

Modified sudden death probability of ending in absorbing state matrix 

||A Wins|B Wins|EOG Tie|
|---|---|---|---|
|A First Pos|0.554|0.433|0.013|
|B down by 3|0.784|0.209|0.006|
|A Pos|0.620|0.360|0.020|
|B Pos|0.360|0.620|0.020|



This gives the probability of game results (first row) based on the current state (first column). 

38.9% of the time, and the game ends in a tie 1.7% of the time. Using the same data to represent playoff games, where a tie is not an option, we have Team A winning 60.8% of the time in an average 7 minute 4 second OT. 

## _3.2.2. Modified sudden death model (MSD)_ 

Similar to SD, we find the average length of overtime to be the sum of the first row of the Fundamental Matrix (Table 6) multiplied by the average length of possessions, which gives 7 minutes 37 seconds. The actual average overtime length from 2013–2015 was 7 minutes 21 seconds. 

Table 7 shows the probabilities of each team winning from the modified sudden death rules. The first row shows that Team A wins the game, on average 55.4% of the time, Team B wins 43.3% of the time, and the game ends in a tie 1.3% of the time. In addition, if Team B is down by 3 then Team A will win 78.4% of the time. We also include the results of our analysis based on where the drive starts in Table 25 in Section 6.4 of the Appendix. 

Table 8 

Drive results for first OT possession and last 7 minutes of OT from 2013–2016 

|Drive Result|First Possession|Last 7 Minutes|
|---|---|---|
|Punt|0.377|0.200|
|Field Goal|0.213|0.320|
|Touchdown|0.180|0.040|
|Downs|0.066|0.080|
|Fumble|0.082|0.040|
|Missed FG|0.033|0.200|
|Interception|0.049|0.000|
|Safety|0.000|0.040|
|End of Game|0.000|0.080|



We then consider the model without an end of game tie option to represent playoff games. Using the same data, but no tie option, we find Team would win 56.1% of the time with an average overtime length of 7 minutes and 42 seconds. In comparison, the 32 playoff games that have gone into overtime since 1958, 53.1% have been won by the team that possessed the ball first with an average overtime length of 8 minutes, 35 seconds, which includes games played under both the SD and MSD rules. 

## _3.2.3. Modified sudden death in 10 minutes (MSD-10)_ 

With the May 2017 overtime rule change from 15 minute periods to 10 minute periods, we attempt to predict how this may change the outcome of overtime games in upcoming seasons. We estimate a 10 minute OT by using drive data from the first possession of MSD OT with an average length of 3 minutes to estimate Team A’s first possession (A First Pos in Table 2). Then we use data from the last 7 minutes of MSD OT to estimate what teams would do in a shortened amount of time to continue play for the rest of the transition matrix (data shown in Table 8). This does not directly account for if Team B would play differently when down by 3 then in SD, but rarely does Team B make a TD when down by 3, so it is reasonable to assume they would still only go for a FG to tie the game as they would during SD to win the game. Games with OT lasting more than 8 minutes is a small data set, but gives us an understanding of how teams play closer to the end of OT, and future years of the 10 minutes OT can give us data to strengthen the analysis. 

One aspect of OT that may change that we do not consider, is Team A intentionally increasing the length of their first possession to limit the time Team B has to score on their first possession. We repeat the MSD analysis with this data in the transition matrix 

_R. Martin et al. / A Markov chain analysis of NFL overtime rules_ 

100 

Table 9 

Modified sudden death-10 minutes probability of ending in absorbing state matrix 

||A Wins|B Wins|EOG Tie|
|---|---|---|---|
|A First Pos|0.541|0.346|0.112|
|B down by 3|0.807|0.140|0.053|
|A Pos|0.522|0.311|0.167|
|B Pos(game tied)|0.311|0.522|0.167|



This gives the probability of game results (first row) based on the current state (first column). 

and find the average length of OT to be 6 minutes 54 seconds with Team A winning 54.1% of the time and Team B winning 34.6% of the time shown in Table 9. It is expected that more games will end in a tie in upcoming seasons with a shorter OT and our model predicts that probability of the game ending in a tie increasing from under 2% to over 11%. For playoff games, when ending in a tie is not an option, we find the probability of Team A winning to be 59.5% with an OT length of 8 minutes 8 seconds. 

## _3.2.4. Alternative modified sudden death model_ 

## _(AMSD)_ 

For our analysis of the theoretical model, we consider a few assumptions and determine the sensitivity of the result to some of those assumptions. In the first possession, there is minimal advantage for Team A to be up by 8 if they score a TD, therefore we assume they will always elect to kick the extra point and not attempt a 2-point conversion, making B down by 8 an unachievable state. Additionally, while Team A is not guaranteed the win if they score a TD on their first possession, their probability of winning is greatly increased, therefore, we assume the same value as the MSD model for TDs for both teams in any possession. 

If Team A scores a TD on their first possession, we needed to consider how Team B would respond since a FG would still lose them the game. Using regular season, regulation time data on Drive Finder, we find that when teams have the ball and are down by 4 to 11 points in the last 3 minutes of the fourth quarter, the drive ends in a TD 17% of the time. Therefore, we assume 17% as the probability Team B will score a TD when down by 6-7 points. 

Additionally,whendownby7,weconsiderifTeam B will elect an extra kick to tie the game or two-point conversion to win the game after a TD. We assume Team B would always go for the extra kick in this scenario to tie the game based on team choice when down by 7 in the last 2-3 minutes of the game. Using 

Table 10 Alternative modified sudden death probability of ending in absorbing state matrix 

||A Win|B Win|EOG Tie|
|---|---|---|---|
|A First Pos|0.547|0.439|0.014|
|B Down by 3|0.784|0.209|0.006|
|B Down by 6|0.835|0.165|0.2|
|B Down by 7|0.939|0.058|0.0032|
|A Pos|0.62|0.361|0.0196|
|B Pos|0.36|0.62|0.0196|



the regular season data on Drive Finder, we found when teams are down by 7 near the end of the fourth quarter, they almost always choose the extra kick over the two-point conversion after a TD. 

Table10showtheprobabilityofeachteamwinning or the game tying with the base assumptions of: 

- Team A will never elect to try for a 2-point conversion on their first possession after scoring a TD. 

- Team B will score a TD 17% of the time when down by 6, 7, or 8. 

- Team B will always elect for the extra kick after a TD when down by 7. 

The result is that Team A wins 54.7% of the time, Team B wins 43.9% of the time, and the game ending in a tie 1.4% of the time with an average of 7 minutes 57 seconds of overtime. Table 10 also shows us the probability of Team A winning based on their performance in their first possession. Notable is that if Team A scores a TD, they have a minimum of 83.6% chance of winning the game and up to a 93.9% chance of winning the game if the extra kick is successful. We include the results of our analysis based on where the drive starts in Table 25 in Section 6.4 of the Appendix. Table 11 gives the sensitivity of the results based on data on Team B’s probability of scoring a TD on their first possession, based on what teams do in the last few minutes of the game in regulation time. 

Finally, we consider a playoff model where an end of game tie is not an option. We eliminate EOG Tie as a potential state and consider any drives that ended in an EOG tie as a change in possession. We note there were very few ties in the regular season between 2013-2015 so this change will minimally impact the model. Using the same assumptions for the regular season AMSD model, our analysis predicts Team A would win 55.4% of the time with an overtime length of 8 minutes and 2 seconds. 

_R. Martin et al. / A Markov chain analysis of NFL overtime rules_ 

101 

Table 11 

Sensitivity of results to Team B TD probability 

|Minutes left|Number of|%FG|%TD|Team A|Team B|EOG Tie|OT Length|
|---|---|---|---|---|---|---|---|
|ingame|Drives|||Win|Win||(minutes)|
|2|915|0.030|0.113|0.549|0.437|0.014|7.927|
|3|1401|0.034|0.171|0.547|0.439|0.014|7.956|
|4|1843|0.036|0.198|0.546|0.440|0.014|7.970|
|5|2196|0.036|0.214|0.546|0.441|0.013|7.978|



From 1999 to 2016 in the regular season, probabilities of a drive ending in a FG or TD when a team is down by 4–11 points with 2–5 minutes remaining in the fourth quarter (Drive Finder) and resulting winning probabilities and game time. 

Table 12 

Onside kick probability descriptions and calculations 

|Probability|Description|Calculation|
|---|---|---|
|P(B Wins, reg kick)<br>|Probability B wins with regular kickoff|SD, MSD, MSD-10, AMSD results|
|P(Wins|Recover)<br>|Probability B wins after recovering an onside<br>kick|Probability of TD or FG after onside kick + probability of<br>winning in SD (winning despite not scoring with onside kick<br>recovery when game goes into sudden death)|
|P(Wins|Do not recover)|Probability B wins after not recovering an<br>onside kick|Probability from SD, MSD, MSD-10, AMSD transition matrix<br>analyses with probabilities of A scoring after starting their<br>frst possession near the center of the feld (see Table 13)|
|P(Recover)|Probability of B recovering the ball needed to<br>make probability of winning with onside|P (B Wins, regkick)−P(B ins|Do not recover)<br>|
||kick at least asgood as winningwithout it.|P (B Wins|Recover)−P(B Wins|Do not recover)|



## _3.3. Onside kicks_ 

Onside kicks are an uncommon event but may be an advantage during overtime. If Team B recovers an onside kick, they greatly increase their chances of winning the game, but if they do not recover the onside kick, they have given Team A much better field position and potential to score a TD on their first possession. We consider the break-even onside kick recovery probability, that is, what probability of recovering an onside kick is necessary to make Team B’s probability of winning at least as good had they executed a regular kickoff. Consider Team B choosing an onside kick and either recovering or not recovering the ball and subsequently winning the game. The probability of Team B winning after an onside kick must be at least as high as with a regular kick to make the onside kick a reasonable choice. Therefore, we find the probabilities that Team B wins withandwithoutrecoveringanonsidekickandsetthe sum of those probabilities equal to the probability of TeamBwinningwitharegularkickoff. Thuswehave, 



## = _P_ ( _Recover_ ) _P_ ( _Win_ | _Recover_ ) _,_ 

## _P_ ( _Do not Recover and Win_ ) 

## = _P_ ( _Do not recover_ ) _P_ ( _Win_ | _Do not recover_ ) _,_ 

where we sum these probabilities, set equal to the probability B wins with a regular kickoff, _P_ ( _B Wins, reg kick_ ). Therefore our equation is 

## _P_ ( _Recover and Win_ ) + _P_ ( _Do not recover and Win_ ) = _P_ ( _B Wins, reg kick_ ) 

and solve for the probability of recovering the ball, _P_ ( _Recover_ ). A summary of terms, data used in calculations, and the equation used for calculating the break-even recovery probability is provided in Table 12. 

If Team B recovers an onside kick, Team A is considered as having had a chance to possess the ball so, in all OT formats, the game will be operating under sudden death rules. Therefore, Team B will immediately win if they score a FG or TD and, if they do not score on their first possession, they have the same probability of winning as in the SD format. To find the probability of Team B winning after recovering the ball, we sum the probability of scoring after an onside kick recovery with the probability of winning in sudden death. To find the probability of scoring, we look at the results of drives after recovery of an onside kick between 2010 and 2016, expanding the years due to the rare nature of recovered onside kicks. From profootball-reference.com, we find that recovered onside kicks results in a FG 19.3% of the time and a TD 

_R. Martin et al. / A Markov chain analysis of NFL overtime rules_ 

102 

Table 13 

Team A scoring after onside kick data from pro-football-reference.com 

||2010–2012|2013–2015|
|---|---|---|
|Average recovery location|Own 47.3|Opponent 49|
|Team A FG probability after Team B not recovering onside kick|0.2<sup>∗</sup>|0.27<sup>∗∗</sup>|
|Team A TDprobabilityafter Team B not recoveringonside kick|0.26<sup>∗</sup>|0.25<sup>∗∗</sup>|



> ∗Computed as average of regulation time scoring from drives starting at Own 46 to Own 49 (based on average recovery location of Own 47.3).<sup>∗∗</sup> Computed as the average of regulation time scoring from drives starting at Opponent 48 to Own 48 (based on average recovery location of Opp 49). 

Table 14 

Values used in computation and solutions for onside kick break-even recovery probabilities for the different OT formats 

|Overtime|P(B Wins,|P(Win|Recover)|P(Win|Do Not|Break Even|
|---|---|---|---|---|
|Format|RegKick)||Recover)|RecoveryP(Recover)|
|SD|0.389|0.895|0.280|0.177|
|MSD|0.433|0.895|0.360|0.137|
|MSD-10|0.409|0.895|0.330|0.140|
|AMSD|0.439|0.895|0.376|0.121|



28.1% of the time. In addition, we consider teams going for long field goals during OT where they had a turnover on downs during regulation time. Recovered onside kicks resulted in a turnover on downs 10.5% of the time with an average line of scrimmage at the 42-yard line. Since Team B would win with just a FG during OT, we assume they would have gone for a FG and find approximately 30.2% of the FGs would be made. Thus we estimate the probability of Team B scoring after recovering an onside kick to be 0.193 + 0.281 + (0.105)(0.302) = 0.506. 

If Team B does not recover an onside kick, Team A hasanadvantageinopeningdrivefieldposition.Team B is not considered as having had a chance to possess the ball, therefore, Team A can only win on their first possession in the MSD and MSD-10 formats when they score a TD. We compute the probability of Team B still winning, despite not recovering their onside kick, by using the probabilities of Team A scoring a FG or TD on their first drive from their advanced field position in the transition matrices in the various OT formats. The onside kick probability values are summarized in Table 13. 

Table 14 summarizes the values used in Equation 1 in the different OT formats and gives the break-even onside kick recovery values. The break-even recovery probabilities are all higher than the league onside kick recovery averages of 13% in 2010–2012 and 5.2% in 2013–2015. This indicates onside kicks are unlikely to be used in OT, but if successful, can give Team B a significant advantage. 

Teams must take into account is the amount of time they spend practicing 2-minute drills. The preparation to recover an onside kick in the last 

2 minutes of a game has become an increasingly important part of an NFL game. If a team has yet to have received an onside kick in the last 2 minutes of a crunch time game, then the probability of recovering the kick for the kicking team could be slightly higher. As a result, if the kicking team has practiced kicking onside kicks in crunch time and has done so before in the season then it might be in their best interest to attempt the onside kick in overtime. Also, if the team kicking off first in overtime has staged a worthwhile comeback in regulation and seems to have control of the momentum then this could be another opportune time to try the onside kick. Based on the recent rule change to a 10-minute overtime the probability of recovery for onside kicks in our model have increased by just under 4%. Leading us to believe that onside kicks could become more attractive for teams. However, in the last 5 years no team has ever attempted an onside kick during overtime. If the NFL were to utilize the AMSD format along with the 10-minute overtime rule, then teams might consider attempting an onside kick even more because the average number of drives in the last 10 minutes of overtime in 2013–2015 was around 2. If the kicking team chooses to kick an onside kick under AMSD rules with the 10-minute time limit, then they are giving themselves a chance to win the game on the second possession of the game without the receiving team possessing the ball. Even if the kicking team does not recover, they set up the receiving team in good field position allowing their drive time to potentially decrease because the average recovery spot in 2013–2015 was the opponent’s 49-yard line. This allows the kicking team that did not recover the 

_R. Martin et al. / A Markov chain analysis of NFL overtime rules_ 

103 

Table 15 

||Summary|of overtime formats||||
|---|---|---|---|---|---|
|Overtime<br>Format|Regular<br>Season<br>Overtime<br>Length|Regular Season<br>Probability<br>of Team A<br>Winning|Regular<br>Season<br>Probability<br>of Team B<br>Winning|Playoff<br>Overtime<br>Length|Playoff<br>Probability<br>of Team A<br>Winning|
|Sudden Death|7 min 1 sec|59.9%|38.9%|7 min 4 sec|60.8%|
|Modifed Sudden Death|7 min 37 sec|55.4%|43.3%|7 min 42 sec|56.1%|
|Modifed Sudden Death 10 Minutes|6 min 54 sec|54.1%|34.6%|8 min 8 sec|59.5%|
|Alternative Modifed Sudden Death|7 min 57 sec|54.7%|43.9%|8 min 2 sec|55.4%|



ball a chance to possess it for a longer period of time regardless of the scoring or non-scoring outcome of the receiving team’s first drive; under AMSD rules with a 10-minute time limit. 

## **4. Conclusion** 

Table 15 shows a summary of what our models estimate the average overtime length to be and the probabilities of Team A and Team B winning. We can conclude that, while the MSD format does seem togettheprobabilitiescloserto50-50foreachteamto win, it still can be improved. As expected, our model predicts that shortening the OT length to 10 minutes will increase the number of games ending in ties. In the AMSD format, where both teams are required to possess the ball at least once, the game length is not greatly extended and seems slightly more fair to both teams, but the probability of Team A winning (54.7%) is still better than simply home field advantage during overtime (54.2%). While our alternative provides a possibility that would make the game feel more fair, the outcomes, based on our assumptions, does not indicate an equal chance of winning for both teams. 

## **5. Future work** 

As more data becomes available, modeling playoff games directly from playoff data would be more indicative of potential playoff results. Our current analysis estimates using regular season data, that may not accurately reflect how teams play during the playoffs. The MSD-10 and AMSD model analyses are based on estimated data, better estimation techniques would strengthen the model analysis. Teams may modify their strategy during a 10 minute OT, so we can also consider how different strategies may influence the outcome of the game. In all of the models, we 

assume team strength is equivalent and use averages for the entire league for our analyses. If sufficient data is available, differences in how team strengths can influence overtime outcomes, regardless of the coin toss can also be considered. Finally, under what circumstances (if any) electing not to receive after winning the coin toss is recommended can be investigated. 

## **Acknowledgments** 

This work was partially supported by the University of St. Francis Summer Research Experience (SURE) program. Thank you to Charles Powell for his support of data collection for this work. 

## **References** 

- Bialik, C., 2003, Should the Outcome of a Coin Flip Mean So Much in NFL Overtime? pp. 1-5. 

- Brady, J., 2016, Super Bowl overtime rules 2016: League ready for extra play if required. SB Nation. Available at: http://www. sbnation.com/nfl/2016/2/7/10817840/super-bowl-2016-nflovertime-rules 

- Brams, S. & Sanderson, Z., 2012, Overtime Rules in Football: Bidding Is Fairer Than Coin Tossing. 

- Buzinski, J., 2016, The NFL needs to change its overtime rules for the playoffs. SB Nation. Available at: http://www. sbnation.com/nfl/2016/1/17/10781862/nfl-needs-to-changepostseason-overtime-rule-cardinals-packers 

- Che, Y. & Che, Y., 2006, Department of Economics Discussion PaperSeriesAuctioningtheNFLOvertimePossession(May). 

- Che, Y.K. & Hendershott, T., 2007, How to divide the possession of a football? _Economics Letters_ , _99_ (3), 561-565. 

- Finder, D., 2017, Pro-Football-Reference.com. Available at: http:// www.pro-football-reference.com/play-index/drive finder.cgi 

- Jones, C., 2012, The new rules for NFL overtime, _Mathematics Magazine_ , _85_ (4), 277-283. 

- Jones, M.A., 2004, Jones.pdf, _The College Mathematics Journal_ , _35_ (5), 330-336. 

- Winston, W., 2009, Mathletics, Princeton University Press. 

_R. Martin et al. / A Markov chain analysis of NFL overtime rules_ 

104 

## **6. Appendix** 

Table 19 

Drive results for games tied after 5 minutes of OT 2013–2016 

## _6.1. List of abbreviations_ 

Table 16 

||Abbreviations|
|---|---|
|Abbreviation|Meaning|
|FG|Field Goal|
|TD|Touchdown|
|TD+0PT|TD with no extra points scored|
|TD+1PT|TD with 1 extra point scored|
|TD+2PT|TD with 2 extra points scored|
|S|Safety|
|EOG|End of Game|
|NS|No Score|



|Abbreviation|Result|Number|Probability|
|---|---|---|---|
|No Score and|Punt|9|0.243|
|Game Continues|Downs|1|0.027|
|(NS)|Fumble|2|0.054|
||Missed FG|6|0.162|
||Interception|1|0.027|
||Blocked FG|0|0.000|
|FG|Field Goal|13|0.351|
|TD|Touchdown|2|0.054|
|S|Safety|1|0.027|
|EOG|End of Game|2|0.054|



37 drives in 20 games. 

Table 20 

Number of OT games, drives and length by year 

## _6.2. Overtime Data from_ 

_pro-football-reference.com_ 

Table 17 

|Year|Number|Number of|Length of Overtime|
|---|---|---|---|
||of OT’s|Drives|(minutes)|
|2010|19|59|7 : 38|
|2011|13|29|6 : 10|
|2012|22|61|7 : 24|
|2013|16|45|9 : 11|
|2014|11|22|6 : 05|
|2015|21|51|7 : 36|



2010–2012 overtime data 

|Abbreviation|Result|Number|Probability|
|---|---|---|---|
|No Score and|Punt|60|0.403|
|Game Continues|Downs|4|0.027|
|(NS)|Fumble|7|0.047|
||Missed FG|13|0.087|
||Interception|11|0.074|
||Blocked FG|0|0|
|FG|Field Goal|46|0.309|
|TD|Touchdown|7|0.047|
|S|Safety|0|0.00|
|EOG|End of Game|1|0.0067|



Total of 149 drives in 54 games. 

## _6.3. Transition matrices with overtime data_ 

Table 21 

Sudden death transition matrix with 2010–2012 regular season overtime data 

||A Pos|B Pos|A Wins|B Wins|Tie|
|---|---|---|---|---|---|
|A Pos|0|0.638|0.356|0|0.007|
|B Pos|0.638|0|0|0.356|0.007|
|A Wins|0|0|1|0|0|
|B Wins|0|0|0|1|0|
|Tie|0|0|0|0|1|



Table 18 

2013–2015 overtime data 

|Abbreviation|Result|Number|Probability|
|---|---|---|---|
|No Score and|Punt|42|0.356|
|Game Continues|Downs|8|0.068|
|(NS)|Fumble|7|0.059|
||Missed FG|5|0.042|
||Interception|4|0.034|
||Blocked FG|1|0.0085|
|FG|Field Goal|38|0.322|
|TD|Touchdown|11|0.093|
|S|Safety|1|0.008|
|EOG|End of Game|1|0.008|



Table 22 

Modified sudden death transition matrix with 2013–2015 overtime data 

||A First<br>Pos|B down<br>by3|A Pos|B Pos|A Wins|B Wins|EOG<br>Tie|
|---|---|---|---|---|---|---|---|
|A First Pos|0|0.322|0|0.576|0.093|0.008|0|
|B Down by|3<br>0|0|0.322|0|0.585|0.093|0|
|A Pos|0|0|0|0.568|0.415|0.008|0.008|
|B Pos|0|0|0.568|0|0.008|0.415|0.008|
|A Wins|0|0|0|0|1|0|0|
|B Wins|0|0|0|0|0|1|0|
|E0G Tie|0|0|0|0|0|0|1|



Total of 118 drives in 48 games. 

105 

_R. Martin et al. / A Markov chain analysis of NFL overtime rules_ 

Table 23 

Modified sudden death-10 minutes transition matrix with 2013–2016 first possession data for first row (a first pos) and last 7 minutes of 2013–2106 ot for remaining rows 

||A First Pos|B down by3|A Pos|B Pos|A Wins|B Wins|EOG Tie|
|---|---|---|---|---|---|---|---|
|A First Pos|0.000|0.213|0.000|0.607|0.180|0.000|0.000|
|B down by 3|0.000|0.000|0.320|0.000|0.640|0.040|0.000|
|A Pos|0.000|0.000|0.000|0.52|0.360|0.040|0.080|
|B Pos (game tied)|0.000|0.000|0.520|0.000|0.040|0.360|0.080|
|A Wins|0.000|0.000|0.000|0.000|1.000|0.000|0.000|
|B Wins|0.000|0.000|0.000|0.000|0.000|1.000|0.000|
|EOG Tie|0.000|0.000|0.000|0.000|0.000|0.000|1.000|



Table 24 

Alternative modified sudden death transition matrix with 2013–2015 regular season overtime data with modifications 

||A First Pos|B Down by3|B Down by6|B Down by7|B down by8|A Pos|B Pos|A Wins|B Wins|EOG Tie|
|---|---|---|---|---|---|---|---|---|---|---|
|A First Pos|0|0.322|0.008|0.083|0|0|0.576|0|0.008|0|
|B Down by 3|0|0|0|0|0|0.322|0|0.585|0.093|0|
|B Down by 6|0|0|0|0|0|0.010|0|0.830|0.160|0|
|B Down by 7|0|0|0|0|0|0.160|0|0.840|0|0|
|B Down by 8|0|0|0|0|0|0.085|0|0.915|0|0|
|A Pos|0|0|0|0|0|0|0.568|0.415|0.008|0.008|
|B Pos|0|0|0|0|0|0.568|0|0.008|0.415|0.008|
|A Wins|0|0|0|0|0|0|0|1|0|0|
|B Wins|0|0|0|0|0|0|0|0|1|0|
|EOG Tie|0|0|0|0|0|0|0|0|0|1|



## _6.4. Results by drive_ 

Table 25 

Percent of drives ending in FG or TD and results of MSD analysis by drive starting position 

|StartingPosition|%FG|%TD|Overtime Length|A Wins|B Wins|EOG Tie|
|---|---|---|---|---|---|---|
|Own 20|0.210|0.113|8.714|0.543|0.439|0.018|
|Own 25|0.216|0.122|8.400|0.546|0.437|0.017|
|Own 30|0.226|0.119|8.299|0.547|0.437|0.016|
|Own 35|0.242|0.110|8.258|0.547|0.437|0.016|
|Own 40|0.260|0.100|8.201|0.547|0.437|0.016|
|Own 45|0.274|0.100|8.024|0.549|0.436|0.015|
|Opp 45|0.833|0|7.467|0.753|0.238|0.008|
|Opp 40|0.833|0|7.467|0.753|0.238|0.008|
|Opp35|1.000|0|7.833|1.000|0|0|




