<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2020/2020 - Quantifying Passing Using NBA Tracking Data to Create an Expected Assist Model - Unknown Authors.pdf -->



<!-- Start of picture text -->
Quantifying Passing:<br>Using NBA Tracking Data to Create<br>an Expected Assist Model<br>Alex Lagarde, James Hyman, Caleb Peña, Raj Dasani<br><!-- End of picture text -->



<!-- Start of picture text -->
Inspiration / Direction<br>⬥<br>What is a quality pass in the<br>NBA?<br>⬥<br>Adding the value of a pass<br>to a shot<br>⬥<br>Identifying passers who<br>create opportunities for<br>teammates<br>⬥<br>Isolating team success<br>from playmaking skill<br>2<br>2<br><!-- End of picture text -->



<!-- Start of picture text -->
Research Question<br>⬥<br>How can tracking data be used<br>to generate metrics that can<br>predict expected points scored<br>a�er a given pass?<br>3<br>3<br><!-- End of picture text -->

4 



<mark>Focus Data</mark> 



Los Angeles Clippers, December 2015 (total 15 games) 









<!-- Start of picture text -->
Identifying Passes<br>Directional Ball Tracking<br><!-- End of picture text -->



<!-- Start of picture text -->
1<br><!-- End of picture text -->



<!-- Start of picture text -->
Strategy<br>Endin g Node<br>Starting Node<br>6<br><!-- End of picture text -->



<!-- Start of picture text -->
6<br><!-- End of picture text -->

- 

- - 

- 



<!-- Start of picture text -->
Refning + Evaluating the Algorithm<br>We visually inspected film for a<br>sample game (LAC v LAL, 12/25/15)<br>546 passes occurred in the game<br>Our algorithm identified 393<br>( 72% ) of them.<br>-<br>Most of the missing passes<br>were inbounds<br>Additionally, of those plays<br> 85.8%  were in<br>flagged as passes,<br>fact passes.<br>-<br>Most trouble misidentifying<br>dribbles through traffic<br>7<br><!-- End of picture text -->



<!-- Start of picture text -->
7<br><!-- End of picture text -->







<!-- Start of picture text -->
2<br><!-- End of picture text -->



<!-- Start of picture text -->
Analyzing Pass Patterns<br>Passes Received vs Passes Made<br>Pass Starting/Ending Location Distribution<br><!-- End of picture text -->

<mark>Passes Received vs Passes Made</mark> Pass Starting/Ending Location Distribution Nearest Defender 



<!-- Start of picture text -->
9<br><!-- End of picture text -->



<!-- Start of picture text -->
Analyzing Team Pass Locations:<br>Clippers Nodes vs Lakers, Christmas 2015<br>10<br><!-- End of picture text -->



<!-- Start of picture text -->
Analyzing Team Pass Locations:<br>Clippers Nodes December 2015<br>11<br><!-- End of picture text -->



<!-- Start of picture text -->
11<br><!-- End of picture text -->



<!-- Start of picture text -->
Analyzing Team Pass Locations:<br>Clippers Nodes December 2015<br>Gray Hexagon in<br>Paint: Over 1000<br>data points,<br>purposefully not<br>included to not<br>diffuse the data<br>12<br><!-- End of picture text -->



<!-- Start of picture text -->
12<br><!-- End of picture text -->



<!-- Start of picture text -->
13<br><!-- End of picture text -->



From our sample game, we found guards to be more often in the passing lane, with wings coming next 







<!-- Start of picture text -->
3<br><!-- End of picture text -->



<!-- Start of picture text -->
Initial Model<br>Expected Points Added from a Pass<br><!-- End of picture text -->



<!-- Start of picture text -->
Finding Assist Opportunities<br>⬥<br>Identify all shots<br><!-- End of picture text -->

⬥ ⬥ 

⬦ 





<!-- Start of picture text -->
15<br><!-- End of picture text -->



<!-- Start of picture text -->
15<br><!-- End of picture text -->



<!-- Start of picture text -->
Variable Selection<br>⬥ ⬥<br>Shot-specific metrics Pass-specific metrics<br><!-- End of picture text -->

⬦ ⬦ 

⬦ ⬦ ⬩ ⬩ 





<!-- Start of picture text -->
Distance to nearest<br>Number of defenders<br>16<br><!-- End of picture text -->



<!-- Start of picture text -->
16<br><!-- End of picture text -->



<!-- Start of picture text -->
Results - GAM<br><!-- End of picture text -->



<!-- Start of picture text -->
⬥<br>⬩<br>17<br><!-- End of picture text -->



<!-- Start of picture text -->
⬥<br><!-- End of picture text -->

⬥ ⬥ 





<!-- Start of picture text -->
17<br><!-- End of picture text -->



<!-- Start of picture text -->
Results - Evaluating Performance<br>⬥<br><!-- End of picture text -->





<!-- Start of picture text -->
18<br><!-- End of picture text -->



<!-- Start of picture text -->
18<br><!-- End of picture text -->







<!-- Start of picture text -->
Moving Forward<br><!-- End of picture text -->



<!-- Start of picture text -->
4<br><!-- End of picture text -->

## <mark>Moving Forward</mark> **4** 



<!-- Start of picture text -->
Calculating Pass Metrics<br>How is a successful pass defined? Pass Metrics to create/analyze<br>⬥ ⬥<br>Spacing - does it open up  Overall passer rating of a<br>the floor player<br><!-- End of picture text -->

⬥ ⬥ 

⬥ ⬥ ⬥ ⬥ 



<!-- Start of picture text -->
Smart decision?<br> Quantifying  after a pass<br>⬥<br>the decision by evaluating  Look at previously created<br>passing lanes and  passing evaluation metrics<br>percentage of shot created  (Ben Taylor)<br><!-- End of picture text -->

⬥ 



<!-- Start of picture text -->
20<br><!-- End of picture text -->



<!-- Start of picture text -->
Priority: Translating our Data to the Playbook<br>-<br>Replicating our methods across multiple<br>teams<br>-<br>Possible translatable Ideas to investigate<br>with Passing and Tracking data:<br>-<br>Ability to identify Time of<br>Possession per player<br>-<br>Compare with our passing metrics<br>and advanced passing stats to<br>measure playmaking effectiveness<br>-<br>Model most efficient offensive<br>lineup possible for each team<br>- 21<br>Identify paint touches<br><!-- End of picture text -->



<!-- Start of picture text -->
21<br><!-- End of picture text -->



# <mark>THANKS!</mark> 

<u><mark>Special Thanks:</mark></u> _Advisors:_ Maksim Horowitz, Atlanta Hawks Kostas Pelechrinis, Pitt School of Computing _Members of the CMSA Camp:_ Ron Yurko Nick Citrone Pratik Patil, Beomjo Park Professor Rebecca Nugent 



22 



<!-- Start of picture text -->
4 quarters, 12 minutes<br>each (720 seconds)<br>Back and forth game of<br>possessions<br>94 by 50 feet<br><!-- End of picture text -->



<!-- Start of picture text -->
Appendix: The Basics of the NBA<br><!-- End of picture text -->

⬥ Game: 

⬦ 4 quarters, 12 minutes 

⬦ Back and forth game of 

⬥ Court : 

⬦ 94 by 50 feet 

23 23 



<!-- Start of picture text -->
Appendix: Where We Found Data<br><!-- End of picture text -->

⬥ SportVU Data 

⬥ Sealneaward 

⬦ ⬦ 

⬥ Rajshah4 

⬦ ⬦ ⬦ 







24 24 



<!-- Start of picture text -->
Appendix: Data Structure<br>Movement Data Play by Play Events Data<br><!-- End of picture text -->



<!-- Start of picture text -->
Score and Score Margin<br>“Event Type”: Stat associated with play<br>made shot, miss shot, rebound<br>“Event Action Type” (specific version of<br>If event type was a made shot, the<br>types of actions would be a layup,<br>dunk, 3pt, etc<br>Home, Away, and Neutral Description,<br>the play by play<br>25<br><!-- End of picture text -->

⬥ ⬥ ⬦ ⬦ ⬦ ⬥ 

⬥ ⬥ ⬦ ⬦ ⬩ ⬦ ⬩ 

⬦ ⬦ ⬦ ⬦ ⬦ 

⬦ 





<!-- Start of picture text -->
25<br><!-- End of picture text -->



<!-- Start of picture text -->
Appendix: Advanced Stats<br>NBA.com Player Passing Data Application with Tracking Data<br>⬥<br>Data provided by Second  ⬥<br>Verifying pass<br>Spectrum  identification<br>⬥<br>Nine pass related variables<br>⬥<br>Investigating why some<br>for each player per game<br><!-- End of picture text -->



<!-- Start of picture text -->
identification<br>Investigating why some<br>players have a higher<br>Assist to Potential Assist<br>ratio<br>26<br><!-- End of picture text -->

⬥ 

⬥ 





<!-- Start of picture text -->
26<br><!-- End of picture text -->



<!-- Start of picture text -->
Appendix: Identifying Starting Nodes<br>-<br>IF the direction of travel changes rapidly OR the ball begins to<br>accelerate rapidly<br>-<br>AND the next node is a different ball handler  (to exclude dribbles)<br>-<br>AND the ball is released at a height lower than 9 feet  (to exclude<br><!-- End of picture text -->

- - - - - 



<!-- Start of picture text -->
(to exclude<br>27<br><!-- End of picture text -->



<!-- Start of picture text -->
27<br><!-- End of picture text -->



<!-- Start of picture text -->
Appendix: Identifying End Nodes<br>Choose the next camera frame where:<br>-<br>The ball suddenly decelerates OR the distance between frames is<br>below a threshold<br>-<br>AND the height of the ball is greater than 1 foot (to exclude<br>bounce passes)<br><!-- End of picture text -->



<!-- Start of picture text -->
28<br><!-- End of picture text -->





<!-- Start of picture text -->
28<br><!-- End of picture text -->



<!-- Start of picture text -->
Appendix: Refning the Algorithm<br>Problem plays<br>-<br>Shot attempts<br>-<br>Remove IF end node is within two feet of the basket<br>-<br>Dribbling through traffic<br>-<br>Remove IF the ball handler and the receiver are from<br><!-- End of picture text -->



<!-- Start of picture text -->
-<br>-<br>Remove IF the ball handler and the receiver are from<br>opposite teams<br>Note:<br>This will make it difficult to identify lobs and steals.<br>29<br><!-- End of picture text -->



<!-- Start of picture text -->
29<br><!-- End of picture text -->



<!-- Start of picture text -->
Appendix: Possession Overlap: Event ID<br>Inconsistency<br><!-- End of picture text -->



30 



<!-- Start of picture text -->
31<br><!-- End of picture text -->



<mark>Appendix: Confrming the Inbound</mark> Discrepancy 





<!-- Start of picture text -->
32<br><!-- End of picture text -->



<!-- Start of picture text -->
32<br><!-- End of picture text -->



<!-- Start of picture text -->
Appendix: Analyzing Team Pass Locations: Lakers<br>33<br><!-- End of picture text -->



<!-- Start of picture text -->
Floor Spacing: Convex Hulls<br>⬥<br>Smtg concise about how<br>we will use it / any results<br>we can produce<br>34<br><!-- End of picture text -->



<!-- Start of picture text -->
34<br><!-- End of picture text -->



<!-- Start of picture text -->
Floor Spacing: Convex Hulls<br><!-- End of picture text -->



⬥ “A set of points defined as 



<!-- Start of picture text -->
35<br><!-- End of picture text -->

⬦ “Convex”: polygon has 



<!-- Start of picture text -->
inwards<br><!-- End of picture text -->



<!-- Start of picture text -->
35<br><!-- End of picture text -->



<!-- Start of picture text -->
36<br><!-- End of picture text -->

### <mark>Importance of Spacing</mark> 



<u>Generally accepted rule: Spacing,</u> specifically on offense, leads to more opportunity and therefore production 

Defender’s Dilemma 

● Stay closer to the paint, help guard dribble-penetration, give your defensive assignment more space ● Stay close to defender, take away their perimeter opportunities 



<!-- Start of picture text -->
Example Analysis: First Basket<br>Areas:<br>Areas:<br>Clippers: 452..51<br>Clippers: 515.79 ft^2<br>ft^2<br>Lakers: 203 ft^2<br>Lakers: 178.95<br>ft^2<br>Centroids:<br>Clippers:<br>Centroids:<br>85 by 32.3 ft<br>Clippers:<br>Lakers:<br>83.4 by 21.85 ft<br>81.2 by 24.6 ft<br>Lakers:<br>83.16 by 23.68 ft<br>37<br><!-- End of picture text -->


