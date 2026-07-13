<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2010/2010 - Did the Best Team Win Analysis of the 2010 Major League Baseball Postseason Using Monte Carlo Simulation - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1344 

Did the Best Team Win? Analysis of the 2010 Major League Baseball Postseason Using Monte Carlo Simulation 

**Thomas W. Rudelius,** _Cornell University_ 

©2012 American Statistical Association. All rights reserved. DOI: 10.1515/1559-0410.1344 

## Did the Best Team Win? Analysis of the 2010 Major League Baseball Postseason Using Monte Carlo Simulation 

##### Thomas W. Rudelius 

##### **Abstract** 

The San Francisco Giants were crowned champions of Major League Baseball in 2010 after defeating the Texas Rangers in the World Series. The World Series matchup may have come as a surprise to many baseball fanatics; the Rangers ended the regular season with the worst record of any of the eight playoff teams, and the Giants ended with the fourth worst. Did these two teams simply catch fire at the right time? Or were they better than their regular season records showed? To answer these questions, the regular season statistics of individual players on each team were used to simulate the postseason. These simulations determined the probability with which each playoff team could have been expected to win the 2010 World Series. 

**KEYWORDS:** baseball, Monte Carlo, simulation, 2010, postseason 

Rudelius: Did the Best Team Win? 

### **1 Introduction** 

The objective of the Major League Baseball postseason is to determine the best team from a pool of eight. Naively, one might expect that the team with the best regular season record would have the greatest chance of success in the postseason. Figure 1 shows the number of regular season wins out of 162 for each of the eight teams in the 2010 Major League Baseball postseason. 

|Team|Wins|
|---|---|
|Rangers|90|
|Yankees|95|
|Rays|96|
|Twins|94|
|Giants|92|
|Braves|91|
|Phillies|97|
|Reds|91|



Figure 1: Regular Season Wins. 

A 2006 Baseball Prospectus study of postseson success found a .22 correlation between postseason success points and actual winning percentage. In the regression model used by the study, the most reliable predictor of postseason success was opponents’ batting average, managing a correlation of .23<sup>[2]</sup> . It would appear that postseason success is inherently difficult to predict. 

However, there are problems with using a linear regression model to predict which teams will succeed in the Major League Baseball postseason. First of all, as noted by the study’s authors, run-scoring is not linear in nature. Secondly, postseason baseball differs from regular season baseball, which makes it difficult to predict postseason success based solely on regular season success. Most prominently, the majority of teams use a five-man starting pitching roation in the regular season but drop to a four-man for the postseason. This means that a team with four very good starting pitchers and one poor starting pitcher would be expected to excel in the postseason, while a team with five decent starting pitchers might not fare as well. 

Thirdly, a team only needs to win postseason series against three other teams to win the championship. If one team happens to match up well against three others, they may succeed by simple luck of the draw. Conversely, the best team may be faced with a tougher postseason schedule and lose in one of the earlier rounds. 

1 

_Submission to Journal of Quantitative Analysis in Sports_ 

The goal of this project was to simulate the 2010 Major League Baseball postseason. Specifically, I addressed two questions: 

- Did the best team in the 2010 Major League Baseball postseason win? 

- To what extent can the best team in the postseason be expected to win? 

### **2 The Simulation** 

The monte carlo simulation featured batting lineups and pitching rotations of each of the eight teams in the 2010 Major League Baseball postseason. Four-man pitching rotations were used for each team, with the number one pitcher on each team serving as the game one starter in each series. The statistics of the five most prolific relief pitchers on each team were averaged together to yield a fifth pitcher. It was assumed that this compilation pitcher entered every game in the seventh inning, and remained until the game was over. 

For each batter, the probabilities of a single (1B), double (2B), triple (3B), home run (HR), and walk (BB) in a given plate appearance were calculated from the batter’s 2010 regular season statistics. For each pitcher, the relative probabilities of a single, double or triple, home run, and walk in a given plate appearance were calculated likewise. It was assumed that the difference between a double and triple was dependent mainly on the batter’s speed and was therefore out of control of the pitcher. Instead, the pitcher’s combined number of doubles and triples was considered, and the conditional probability of a double given a double or triple was taken as a constant, dependent on the league average. All statistics were found at BaseballReference.com. 

Defense was not explicitly incorporated into the model. It has been suggested that errors are not a good indication of team’s defensive ability<sup>[3]</sup> . Instead, the conditional probability of an error given that the batter did not single, double, triple, homer, or walk was taken as a constant. This probability was approximated by dividing the number of errors by the number of put-outs in the 2010 regular season. Fielding may be implicitly taken into account, however, as it is likely correlated with the statistics that were incorporated into the model. For instance, if a team’s defensive range is generally poor, it will probably lead to an increase in the number of hits allowed by the team’s pitchers. 

Stolen bases and sacrifice bunts were also left out of the model. One study found that stolen bases do not typically have great impact on a team’s chance of winning a game<sup>[4]</sup> . Sacrifice bunts have been shown to be advantageous only in very rare situations<sup>[5]</sup> . It would be very difficult to determine when a specific team 

http://www.bepress.com/jqas 

2 

Rudelius: Did the Best Team Win? 

would decide to attempt a stolen base or sacrifice bunt. For this reason, they were neglected from the model entirely. 

As in real life, the first round of playoffs was a best-of-five series, and the next two rounds were best-of-seven. Each possible series matchup was simulated 2,000,000 times to ensure precision. Then, the probability of any particular team advancing past any particular round was determined by multiplying the probability of the team advancing to that round by the probability of the team beating their next opponent, weighted differently for the different possible opponents. For instance, the probability that the Texas Rangers would advance to the World Series was computed via the formula, P(Texas in WS) = P(Texas in ALCS) _·_ [P(Texas beats New York) _·_ P(New York in ALCS) + P(Texas beats Minnesota) _·_ P(Minnesota in ALCS)]. 

Designated hitters were used only in games at American League stadiums, with the pitchers batting in their place at National League stadiums. Rather than use the batting statistics for each of the pitchers, which compose a small sample size, the overall National League average of batters in the ninth spot in the batting order was used. All pitchers were treated as equally-skilled batters, therefore. 

When computing the league average probability of a single, double, triple, home run, or walk, only the American League statistics were used. The National League statistics are somewhat tainted due to the lack of a designated hitter. This may have skewed the results of the National League series simulations slightly, but the American and National Leagues are similar enough that the League chosen should not matter greatly. Furthermore, no team should gain a significant advantage. 

#### **2.1 Testing the Simulation** 

Before developing any meaningful results, it was necessary to ensure that the simulation itself was a realistic simulation of a Major League Baseball game. To accomplish this, league average statistics were used to simulate 10,000,000 innings. The mean number of runs per inning could be compared to the observed mean number of runs scored per inning. This process was repeated for innings beginning with runners in any of the eight possible situations (first, second, third, first and second, first and third, second and third, and bases loaded) and with any of the three possible number of outs (zero, one, or two). Thus, twenty-four expected runs values were calculated, which could be compared to those published by Baseball Prospectus for the 2010 Major League Baseball regular season<sup>[6]</sup> . 

3 

_Submission to Journal of Quantitative Analysis in Sports_ 

|Runners|0 ou|ts|1 ou|t|2 ou|ts|
|---|---|---|---|---|---|---|
||Prospectus|Model|Prospectus|Model|Prospectus|Model|
|—|.49154|.50157|.26151|.27248|.10374|.10425|
|1–|.85877|.86987|.50512|.5164|.2282|.22422|
|-2-|1.01113|1.03678|.67765|.65667|.3215|.32065|
|–3|1.35798|1.26174|.93308|.85929|.34192|.3874|
|12-|1.42099|1.51017|.88181|.96901|.45503|.45896|
|1-3|1.80042|1.57111|1.0982|1.04182|.46571|.51915|
|-23|1.96584|1.81419|1.38849|1.25753|.58205|.60902|
|123|2.36061|2.26705|1.51185|1.59502|.77712|.811302|



Figure 2: Expected Runs Matrix. 



Figure 3: Regression of Model Expected Runs by Baseball Prospectus Expected Runs. 

Were the model a perfect simulation of a Major League Baseball game, regression analysis would yield a correlation coefficient of 1.0, a slope of 1.0, and an intercept of 0. In reality, the correlation was .993, the slope was .928, and the intercept was .051. Thus, the model used was not a perfect simulation of a Major League Baseball game, but it was similar enough to generate potentially meaningful results. Furthermore, there was no reason to believe that any one team would gain an advantage from the error introduced by the simulation. 

http://www.bepress.com/jqas 

4 

Rudelius: Did the Best Team Win? 

#### **2.2 The Log5 Method** 

The log5 formula, a variant of Bayes’ formula, was the crux of the simulation. First developed by Bill James and published in his _1981 Baseball Abstract_ , the log5 method can be used to calculate the probability with which a given batter will single, double, triple, homer, or walk against a given pitcher<sup>[7]</sup> . The specific formula (e.g. for a single) is 

_P_ <u>(</u> _Single_ <u>)</u> _<u>Batter·P</u>_ <u>(</u> _Single_ <u>)</u> _<u>P itcher</u>_ 



where _P_ ( _Single_ ) _Batter_ is the probability that the batter singles, _P_ ( _Single_ ) _Pitcher_ is the probability that the pitcher allows a single, and _P_ ( _Single_ ) _LgAvg_ is the average probability of single across the entire league. The probability of a double, triple, home run, or walk can be calculated from the same formula, simply replacing the word “single” with the event in question. 

As an example, consider the batter-pitcher matchup between Alex Rodriguez of the New York Yankees and Cliff Lee of the Texas Rangers. The probabilities associated with each of the possible outcomes of an Alex Rodriguez plate appearance are: 

|Player|1B|2B|3B|HR|BB|
|---|---|---|---|---|---|
|Alex Rodriguez|.13445|.04874|.00336|.05042|.10420|



Likewise, the probabilities associated with each possible outcome when Cliff Lee is pitching are: 

|Pitcher|1B|2B|3B|HR|BB|
|---|---|---|---|---|---|
|Cliff Lee|.15402|.05265|.00482|.02529|.02989|



So, using league average probabilities given by: 

|Player|1B|2B|3B|HR|BB|
|---|---|---|---|---|---|
|League Average|.15610|.04631|.00424|.02547|.09333|



And using the log5 formula, one arrives at the following probabilities for the outcomes of the matchup between Alex Rodriguez and Cliff Lee: 

|Matchup|1B|2B|3B|HR|BB|
|---|---|---|---|---|---|
|Rodriguez v. Lee|.13261|.05539|.00382|.05007|.03365|



5 

_Submission to Journal of Quantitative Analysis in Sports_ 

#### **2.3 Team Rosters** 

The roster used for each team is listed below. The rosters were determined by the number of starts each player received in the 2010 regular season in conjunction with the number of starts each player received in the 2010 postseason. The left column of each table contains the batting order, while the right column lists the pitching rotation. The player listed as a DH served as the designated hitter and did not bat in games at National League stadiums. The statistics of the five pitchers listed as RP, or relief pitchers, were averaged together. 

|Texas|Rangers|New Yo|rk Yankees|
|---|---|---|---|
|BattingOrder|PitchingRotation|BattingOrder|PitchingRotation|
|Andrus|Lee|Jeter|Sabathia|
|Young|Wilson|Swisher|Pettitte|
|Hamilton|Lewis|Teixeira|Hughes|
|Guerrero|Hunter|Rodriguez|Burnett|
|Cruz|Feliz(RP)|Cano|Rivera(RP)|
|Kinsler|O’Day (RP)|Thames(DH)|Chamberlain(RP)|
|Smoak|Oliver(RP)|Posada|Robertson(RP)|
|Treanor|Francisco(RP)|Granderson|Gaudin(RP)|
|Borbon(DH)|Ogando(RP)|Gardner|Logan(RP)|
|Tampa|BayRays|Minne|sota Twins|
|BattingOrder|PitchingRotation|BattingOrder|PitchingRotation|
|Jaso|Price|Span|Liriano|
|Zobrist|Shields|Hudson|Pavano|
|Crawford|Garza|Mauer|Baker|
|Longoria|Davis|Young|Blackburn|
|Rodriguez|Soriano(RP)|Thome(DH)|Rauch(RP)|
|Aybar(DH)|Cormier(RP)|Cuddyer|Duensing (RP)|
|Pena|Benoit(RP)|Kubel|Guerrier(RP)|
|Upton|Wheeler(RP)|Valencia|Crain(RP)|
|Bartlett|Choate(RP)|Hardy|Mijares(RP)|



6 

http://www.bepress.com/jqas 

###### Rudelius: Did the Best Team Win? 

|San Fran|cisco Giants|Philadel|phia Phillies|
|---|---|---|---|
|BattingOrder|PitchingRotation|BattingOrder|PitchingRotation|
|Torres|Lincecum|Victorino|Halladay|
|Sanchez|Cain|Utley|Hamels|
|Posey|Sanchez|Polanco|Blanton|
|Burrell|Bumgarner|Howard|Kendrick|
|Huff|Wilson(RP)|Werth|Lidge(RP)|
|Uribe|Romo(RP)|Rollins|Durbin(RP)|
|Schierholtz|Casilla(RP)|Ibanez|Contreras(RP)|
|Sandoval|Mota(RP)|Ruiz|Madson(RP)|
|Renteria(DH)|Affeldt(RP)|Valdez(DH)|Romero(RP)|
|Atlan|ta Braves|Cincin|nati Reds|
|BattingOrder|PitchingRotation|BattingOrder|PitchingRotation|
|Infante|Lowe|Phillips|Arroyo|
|Heyward|Hanson|Cabrera|Cueto|
|Lee|Hudson|Votto|Leake|
|McCann|Jurrjens|Rolen|Harang|
|Gonzalez|Wagner(RP)|Gomes|Cordero(RP)|
|Cabrera|Venters(RP)|Bruce|Masset(RP)|
|Prado|Moylan(RP)|Stubbs|Ondrusek(RP)|
|Ankiel|Saito(RP)|Hernandez|Rhodes(RP)|
|Glaus(DH)|O’Flaherty (RP)|Hanigan(DH)|Smith(RP)|



Figure 4: Team Rosters. 

### **3 Results and Conclusions** 

The key findings of this study are shown in Figure 5 below. The probability that each team would be expected to win its first playoff series (LDS), second playoff series (LCS), and third playoff series (WS) were as follows: 

7 

_Submission to Journal of Quantitative Analysis in Sports_ 

|Team|P(Win LDS)|P(Win LCS)|P(Win WS)|
|---|---|---|---|
|Rangers|.602|.374|.233|
|Yankees|.564|.275|.146|
|Rays|.398|.186|.092|
|Twins|.436|.165|.063|
|Giants|.516|.314|.161|
|Braves|.484|.276|.136|
|Phillies|.554|.245|.104|
|Reds|.446|.165|.064|



Figure 5: Probabilites of Winning LDS, LCS, and WS. 

So, did the best team win? The data in Figure 5 suggest that the Texas Rangers, rather than the San Francisco Giants, had the highest probability of running the table. However, it appears that the Rangers and Giants were the most likely teams to advance to the World Series from their respective leagues. This is not the result that would have been predicted by merely examining the teams’ win-loss records, nor is the result that many baseball fanatics would have predicted. Without a doubt, certain citizens of Las Vegas would have liked to see the results of this study before the actual 2010 postseason took place. 

To what extent can the best team in the postseason be expected to win? If 2010 is any indication, the answer is not very often. Even the favorite Rangers would fail to win the World Series in more than three-fourths of all simulations. The long-shot Minnesota Twins and Cincinnati Reds could still expect to run the table in more than one in twenty. The Twins and Reds, both of whom were easily defeated three games to none in their first series, actually would have won those series more than 43 times out of 100. The fact that the most likely World Series candidates, the Rangers and Giants, actually did live up to their potential is merely a coincidence, which would happen with probability .117. 

More in-depth results are provided below. The following tables list the probabilities that the teams listed in the left column could be expected to defeat the teams listed in the top row in a best-of-seven-series: 

http://www.bepress.com/jqas 

8 

Rudelius: Did the Best Team Win? 

|NL / AL<br>R|angers<br>|Yankees|Rays<br>T|wins|
|---|---|---|---|---|
|Giants|.430|.512|.556|.661|
|Braves|.408|.507|.519|.637|
|Phillies|.330|.424|.477|.581|
|Reds|.293|.379|.447|.545|
|Home / Away|Giants|Braves|Phillies|Reds|
|Giants|X|.498|.578|.647|
|Braves|.502|X|.537|.613|
|Phillies|.422|.463|X|.555|
|Reds|.353|.387|.445|X|
|Home / Away|Rangers|Yankee|s<br>Rays|Twins|
|Rangers|X|.579|.609|.674|
|Yankees|.421|X|.589|.592|
|Rays|.391|.411|X|.543|
|Twins|.326|.408|.457|X|



Figure 6: Best-of-Seven Series Matchups. 

One notable result is that the Giants would only be expected to defeat the Braves in a best-of-seven series with probability .498. However, the Giants gain the edge in a best-of-five series, defeating with Braves with probability .516. In reality, the Giants did defeat the Braves in a best-of-five series, by a score of three games to one. Perhaps if Major League Baseball were to expand the first round of its postseason to a best-of-seven, the Braves would have gained the advantage. 

### **4 Sources of Error** 

As in any experiment, these results are affected by two types of error: random and systematic. 

#### **4.1 Random Error** 

Treating the proportion of series wins as a binomial random variable with 2,000,000 trials, an upper bound is placed on the standard deviation via the well-known formula: 



9 

_Submission to Journal of Quantitative Analysis in Sports_ 

Using the normal approximation to the binomial, one can be more than 99.5% confident that a given probability in the series simulation tables above is correct to within .001. 

#### **4.2 Systematic Error** 

Systematic error presents greater challenges to the model than does random error. Sources of systematic error include: 

- Discrepancies between baserunning in the simulation and baserunning in real life, as discussed in section 2.1. 

- Differences in regular season schedules of each team, which may inflate or 

- Choice of pitchers and batters to be used for each team. 

- Failure to adjust for advantage gained by a left-handed batter against a righthanded pitcher, or by a right-handed batter against a left-handed pitcher. 

- Failure to adjust for differences in ballpark dimensions, which produce different run-scoring environments. 

- Failure to adjust for discrepancies in hitting abilities of different pitchers. 

- Failure to explicitly incorporate defense and fielding into the model. 

The list of potential sources of error is long, but the contribution of each should be small. Further testing of the model is recommended to ensure accuracy. 

### **References** 

- [1] _Baseball-Reference.com - Major League Baseball Statistics and History._ 2010. Sports Reference LLC. November 22, 2011 _<_ http://www.baseballreference.com _>_ . 

- [2] Silver, Nate and Dayn Perry. “Why Doesn’t Billy Beane’s Shit Work in the Playoffs?”. _Baseball Between the Numbers_ . New York: Basic Books, 2006. 

- [3] Perry, Dayn. “When does a Pitcher Earn an Earned Run?”. _Baseball Between the Numbers_ . New York: Basic Books, 2006. 

http://www.bepress.com/jqas 

10 

Rudelius: Did the Best Team Win? 

- [4] Click, James. “What if Rickey Henderson had Pete Incaviglia’s Legs”. _Baseball Between the Numbers_ . New York: Basic Books, 2006. 

- [5] Click, James. “When Is One Run Worth More than Two?”. _Baseball Between the Numbers_ . New York: Basic Books, 2006. 

- [6] _Baseball Prospectus_ . 2010. Prospectus Entertainment Ventures, LLC. November 22, 2011 _<_ http://www.baseballprospectus.com _>_ . 

- [7] Fox, Dan. “A Short Digression into Log5.” _The Hardball Times_ . November 23, 2005. November 22, 2011 _<_ http://www.hardballtimes.com/main/article/ashort-digression-into-log5/ _>_ . 

11 


