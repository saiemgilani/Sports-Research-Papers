<!-- source: library/conferences/New England Symposium on Statistics in Sports/2009/2009 - Evaluating Risk in NFL Play Calling - Unknown Authors.pdf -->

# Risk & NFL Pla Callin <mark>y g</mark> 

By Benjamin Alamar, PhD Menlo College 

New England Symposium on Statistics in Sports September 26, 2009 



## Play Calling 

- Previous work examining play calling behavior in the NFL has noted to possibility of irrational behavior (Alamar 2006, Romer 2002, Winston 2009, Rockerbie 2008). 

- Most analysis suggests, based on various measures of payoff, that teams run too much. 

- • The increased payoff could in theory be attributed to higher risk, therefore, given the risk reward tradeoff, teams may be rational by not passing more. 

## But what is risk? 

• Rockerbie defines risk as the variance in yards gained/lost on a play of a given type (run or pass). • But as the distribution of yards is not normal, higher variance is actually desirable. • Given two plays of equal mean payoff, a coach should choose the play with a higher variance 





## Play Context 

- To understand risk, we first have to put the outcome in the proper context: ▫5 yards on 2 and 5 is great, and but on 3 and 6 it likely results in punt. 

- Down, distance, yardline all effect how “good” the outcome of a play is. 

- Expected points (known as expected runs in baseball work) provides context and a way to measure the value of each play. 



## The Expected Points Framework 

- Issue of context addressed by utilizing an expected points framework. 

- Expected points are the points a team scores on average given their current situation. 

- • Net expected points is the change in expected points that a play generates. 

- • Utilized in football previously (Winston 2009, Carroll et al 1989, Romer 2002) 



## Expected Points Formula 

 Points _F Down YardsToGo Yardline_ Expected t ( _t_ , _t_ , _t_ ) 

  _NEPt_ Expected Points t  1 Expected Points t  Points Scored t 

- Could easily be expanded to include effects of “next drive” or rest of game or half 

- For this work, the post play EP on turnovers is the negative of the expected points given the new game context. 



## Data 

- Data used to estimate the equations is NFL play by play data from the 2005 to 2008 regular seasons (as provided my Football Outsiders) 

- • There are 220,326 plays in the data set 

- • Each play includes a variable for play type (run or pass) as well as the down, yards to go for a first, distance from the end zone, team on offense, team on defense and several other play descriptors. 



## Data (cont) 

- From the play by play data a points on drive variable was created that calculates the total points scored on the drive 

- • An additional variable was calculated for the number of plays on the drive. 



## Estimation 

- The expected points equation is estimated using a weighted least squares approach (weighted by # of plays on a drive). 

- Fixed effects for each team year were included (ie: 49ers2005, 49ers2006, 49ers2007 & 49ers2008). 

- Statistically significant results were obtained for all control variables with a weighted R<sup>2</sup> of 0.37. 



## Results of Estimation 

|Results of Expected Points Weighted Least<br>Regression|Squares|
|---|---|
|Variable<br>Estimate<br>Std Error|t-value|
|Constant<br>6.38<br>0.09|73.38|
|Down<br>-0.49<br>0.01|-41.57|
|Yards to Go<br>-0.07<br>0.00|-26.83|
|Q1<br>-0.29<br>0.03|-8.71|
|Q2<br>0.07<br>0.03|2.31|
|Q3<br>-0.37<br>0.03|-11.22|
|Distance to Goal<br>-1.18<br>0.01|-90.31|
|Note: All estimates are significant at the 99% c<br>level expect Q2 which is significant at the 95%<br>Distance to goal is entered in natural log form.|onfidence<br>level.|





## Expected Points By Distance 



## Net Expected Points 

- Using the estimated expected points for each play, Net Expected Points (NEP) were calculated for each play. 

- As a “reality” check, the average NEP for each team for each season, for both offense and defense, were calculated. 

- The top offenses and defenses, based on average NEP, were ranked. 



## Top Offenses and Defenses 

|Year|Offense|Average NEP|Year|Defense|Average NEP|
|---|---|---|---|---|---|
|2007|Patriots|0.27|2008|Steelers|-0.04|
|2006|Colts|0.26|2006|Ravens|-0.03|
|2007|Colts|0.24|2008|Eagles|-0.02|
|2008|Saints|0.23|2006|Bears|-0.02|
|2005|Bengals|0.22|2008|Ravens|0.00|
|2005|Colts|0.22|2008|Titans|0.00|
|2008|Chargers|0.22|2006|Jaguars|0.02|
|2007|Cowboys|0.22|2006|Patriots|0.02|
|2005|Seahawks|0.21|2005|Bears|0.03|
|2008|Broncos|0.20|2007|Buccaneers|0.03|



Note: For all teams and all seasons, Offense NEP has a correlation with winning of 0.55 and Defense NEP has a correlation with winning of -0.54. 



### Expected Points and the Passing Premium 

- Using plays only through the 3<sup>rd</sup> quarter in which the score difference was less than 11 points, the average NEP for passing plays and running plays was calculated 

- • The 0.06 difference between running and passing is statistically significant at the 99% confidence level 

- • Normal mean difference between running and passing results 

Pla T e Mean NEP <u>y yp</u> Run 0.07 <u>Pass 0.13</u> 



## Measuring Risk 

- Risk can now be thought of as the probability that a play will produce negative NEP (risk factor – rf) 

- • Comparing run plays and pass plays demonstrates that passing (rf = 0.57) is less risky than running (rf=0.62) for all plays. 

- Looking at specific situations, the risk profile changes. On 1<sup>st</sup> and 10 running (rf=0.66) has a much higher risk than passing (rf=0.53), while on 2<sup>nd</sup> and 3 running (rf=0.35) has a lower risk factor than passing (rf=0.44). 



## Risk Variation by Play Type 





## Conclusion 

- The existence of the passing premium is further confirmed by the use of the expected points framework. 

- If team’s passed more, they would increase their probability of winning by both achieving a higher mean NEP and a lower probability of negative NEP plays. 

- Coach’s insistence on balancing the run and pass seems to be irrational, as running creates a lower expected outcome with increased risk. 


