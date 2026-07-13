<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2019/2019 - Chuckers Measuring Lineup Shot Distribution Optimality Using Spatial Allocative Efficiency Models - Unknown Authors.pdf -->



# **Chuckers: Measuring Lineup Shot Distribution Optimality Using Spatial Allocative Efficiency Models** 

Nathan Sandholtz<sup>1</sup> Jacob Mortensen<sup>1</sup> Luke Bornn<sup>1,2</sup> `nsandhol@sfu.ca        jmortens@sfu.ca     lbornn@kings.com` 

## **1. Introduction** 

In the 2017-18 NBA playoffs, Russell Westbrook scored 46 points on 43 shot attempts in a 96-91 loss to the Utah Jazz, ending the Oklahoma City Thunder's season.  At the time, many popular media figures conjectured that having one player dominate field goal attempts in this way would limit the Thunder's success.  While scoring 46 points in a playoff basketball game is an impressive feat for any one player, its impact on the win column is moderated by the fact that it required 43 attempts.  At its core, this critique is about efficiency. 

Modern discussion around efficiency in the NBA typically focuses on either individual player efficiency or shot selection.  Conceptually, the foundation for shot selection efficiency is simple: shots at the rim and 3-point shots have the highest expected points per shot, so teams should prioritize these high-value shots.  The idea underlying individual player efficiency is also straightforward; scoring more points on the same number of shot attempts increases a team’s chances of winning. However, implicit in any discussion of player efficiency is the idea that inefficient players have a negative impact because basketball is a team sport.  We are concerned with efficiency not just because a given player is inefficient, but because inefficient players take shot opportunities away from teammates that may have higher value.  In other words, if Westbrook was surrounded by dismal shooters his 43 shot attempts might appear more defensible, but if his inordinate number of attempts prevented highly efficient shots from other players, then he has caused shots to be inefficiently distributed among the players on the team and decreased their winning potential.  This aspect of efficiency—the allocation of shots within a lineup—is the primary focus of our paper. 

Allocative efficiency is fundamentally a spatial problem.  The distribution of shots within a lineup is highly dependent on court location.  For example, while the Thunder might want to allocate more shots to Steven Adams near the rim, they probably wouldn't want him taking more shots beyond the 3-point line.  Despite the importance of spatial context, there are very few allocative efficiency analyses which have explicitly accounted for this critical factor.  Our unique contribution with this work is a method to explore allocative efficiency _spatially_ .  We use a novel method to measure a lineup's shot distribution optimality over the court.  Then, using these metrics, we quantify how many points are being lost through inefficient spatial lineup shot allocation, visualize where they are being lost, and identify which players are responsible. 

### **1.1. Related Work** 

> 1 Simon Fraser University - Dept. of Statistics and Actuarial Sciences 

> 2 Sacramento Kings 





2019 Research Papers Competition Presented by: 

1 



In recent years, the emphasis on shot selection (i.e. the quality of shots as determined by the shooter, shot location, and defensive pressure at the time of the shot) has led to the development of many metrics which aim to measure this aspect of a shooting decision, such as true shooting percentage [1], qSQ, and qSI [2].  Additionally, metrics have been developed to quantify player efficiency, such as Hollinger's player efficiency rating [3] or Oliver's usage curves [4].  While these metrics implicitly account for team context, there have been relatively few studies which have looked at shooting decisions explicitly in context of lineup, and none spatially.  An example of a non-spatial allocative efficiency analysis of shot attempts in the NBA is the work of Goldman and Rao in [5].  They model the decision to shoot as a dynamic mixed-strategy equilibrium weighing both the continuation value of a possession and the outside option of a teammate shooting.  Cervone et. al.'s ‘shot satisfaction’ metric [6] is another example of analyzing shooting decisions in context of lineup.  However, since shot satisfaction is marginalized over the allocative and spatial components, these factors can't be explored using this metric alone.  Essentially, we are interested in disaggregating the allocative efficiency component of shot satisfaction smoothly in space. 

### **1.2. Publicly Available Data** 

All of our data is publicly available through the NBA stats API (stats.nba.com).  Shot _x, y_ locations are available through the ‘shotchartdetail' API endpoint whereas lineup data can be gathered from the ‘playbyplayv2' endpoint.  Using the play-by-play data, we can determine the lineup on the court at any point in the game and merge this with the shot data to determine which players were on the court for each shot.  Additionally, shots are tagged in the API with various labels (e.g. dunk, layup, etc.).  Since tip-ins and put-backs are shots that the offense cannot allocate or control in the same way they do for half court sets, we removed shots with these labels from our analysis.  Code used to collect the data and perform an empirical version of the analysis presented in this paper can be found on the author’s GitHub page: https://github.com/nsandholtz/lpl. 

## **2. Models** 

### **2.1. Estimating FG% and FGA Rate Surfaces** 

The foundation of our project rests on spatial estimates of both player field goal percentages (FG%) and field goal attempt (FGA) rates.  Following the methodology in [6], we build a Bayesian hierarchical model to estimate the probability, !, that a shot is made by player _j_ at location **_z_** with the model 



where -<sup>(/)</sup> is a player-specific Gaussian process.  To make estimation of -<sup>(/)</sup> computationally tractable, we use a low-dimensional basis function representation [7] that sets -<sup>(/)</sup> (1) = 6 (/) (/) ∑578 45 95(1), where 95(⋅) represents basis function _d_ , 45 is a player-specific weight, and _D_ is (/) the total number of basis functions.  We define the basis function as 95(⋅) = ;5 <(1), where <(⋅) is a =+ length vector containing the output of the piecewise linear function used by Lindgren in [8], and (/) ;5 is a 1 × =+ vector of weights for player _j_ from the non-negative matrix factorization [9] of coefficients from independent Poisson regressions for their shot counts.   Next, by clustering player shot profiles and creating a player adjacency matrix, we apply conditionally autoregressive (CAR) (/) priors [10] to the basis function weights 45 .  The end result of this process is a model that varies 

2019 Research Papers Competition Presented by: 





2 



spatially and allows us to predict field goal percentages for all players from any location in the offensive half court. 

FGA surfaces are estimated by smoothing a player's empirical shot attempts using a Poisson point process [11].  We then normalize the surfaces to FGA per 100 possessions, allowing us to make meaningful comparisons between players who differ in the number of minutes played.  The FG% and FGA prediction surfaces used in the rest of this paper utilize projections onto a spatial grid of 1 ft by 1 ft cells, producing surfaces like those shown in Figure 1 for Stephen Curry of the Golden State Warriors. 





<!-- Start of picture text -->
FG%<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br><!-- End of picture text -->





<!-- Start of picture text -->
FGA<br>0.15<br>0.1<br>0.05<br>0<br><!-- End of picture text -->

**_Figure 1._** Estimated FG% surface (left) and FGA per 100 possessions (right) in the starting GSW lineup for Stephen Curry in the NBA 2016-2017 regular season. 

In order to have sufficient data to reliably estimate the FG% surfaces, we assume that these surfaces are lineup independent.  We recognize this assumption may be violated in some cases, as players who draw a lot of defensive attention can improve the FG% of their teammates by providing them with more unguarded shot opportunities.  In future work, our analysis could be augmented with proprietary data (e.g. nearest defender distance) to account for defensive pressure when estimating FG%. 

In contrast to the FG% surfaces, FGA rate varies wildly depending on the lineup.  Consider the Oklahoma City Thunder example in the introduction—Westbrook's teammates' attempt rates will change drastically based on whether Westbrook is on or off the court.  Fortunately, because we are focused on smoothing empirical attempts rather than modeling unobserved parameters, obtaining lineup-specific FGA surfaces is comparatively simple.  The reasons for this empirical smoothing will become clear in the following section. 

### **2.2. Spatial Rankings Within Lineup** 

With estimates of FG% and FGA rate surfaces for every player, we can rank players on these metrics A relative to their four teammates in a given lineup spatially over the court. For a given lineup, let ?@/ be the rank (ranging from 1 to 5) of player B′s FG% relative to his four teammates in court location D, K where D ∈{1, … , I}. Let ?@/ be equivalently defined for FGA rate.  We estimate  these rank surfaces LMA⋅/ = (?̂8/A , … , ?̂O/A ) and LM⋅/K = P?̂8/K , … , ?̂O/K Q by ranking the posterior means of our models for FG% and FGA within each cell. Figure 2 shows these rank surfaces for the starting lineup of the 2016-17 Golden State Warriors; the top row shows the FG% rank surfaces while the bottom row shows the rank surfaces for FGA rate. 





2019 Research Papers Competition Presented by: 

3 























**_Figure 2._** GSW 2016-17 starting lineup FG% rank surfaces (top row) and FGA rank surfaces (bottom row). 

As expected, Kevin Durant, Klay Thompson, and Stephen Curry consistently rank as the top three shooters over the entire court, with a surprising exception from the left mid-range region where Pachulia surpasses Curry. We can also see that the top three shooters for Golden State tend to take the most shot attempts across the court, with the exception of the restricted area and a small area at the top of the arc where Green takes the most shots. 

In the following section we propose a metric based on redistributing the observed shots according to a proposed optimum.  In doing so, we require each player's FGA surface to strongly adhere to his observed data while still being smooth enough to yield a plausible surface of ranks.  An example may help make this concept clearer.  Imagine that Zaza Pachulia only took one 3-point shot the entire 2016-17 season (in reality he took two) and that none of his teammates happened to take any shots in the exact same 1 ft square.  If we simply aggregated shot attempts to the nearest 1 ft by 1 ft grid cell, we would conclude that Pachulia is a more prolific shooter in this area than every other player on the Warriors.  We know that this is not true; Pachulia attempted just a single 3-point shot the entire season.  By smoothing the FGA surfaces, small anomalies like this are prevented from muddling the FGA rankings while still allowing us to utilize these surfaces as a pseudo-empirical distribution of a player's observed shots. 

## **3. Measuring Spatial Allocative Efficiency** 

The strong correspondence between the FG% and FGA rank surfaces shown in Figure 2 is no surprise; all other factors being equal, teams would naturally want their most skilled shooters taking the most shots and the worst shooters taking the fewest shots in any given location.  It is the _strength_ of this relationship that we are interested in measuring, for which we now propose a metric. 

2019 Research Papers Competition Presented by: 





4 



### **3.1. Rank Correspondence** 

Using the ranks estimated in Section 2.2 we can difference each player's FG% rank surface from their FGA rank surface, LM⋅/K −LMA⋅/, to obtain a surface which measures how strongly each player's FG% rank matches their FGA rank.  Figure 3 shows these surfaces for the Warriors 2016-17 starting lineup. 











**_Figure 3._** GSW 2016-17 starting lineup rank correspondence surfaces, which are determined by differencing the FGA rank surfaces (per 100 possessions) from the FG% rank surfaces _._ 

Notice in the legend of Figure 3 that we label deviations from 0 as sub-optimal; positive values of rank correspondence are labeled as ‘under-use’ and negative values are labeled as ‘over-use’.  We are assuming that any deviation from perfect correlation in the FG% and FGA ranks is indicative of suboptimal lineup performance.  Due to confounding variables (e.g. defensive pressure) this assumption may not hold in some situations, which we discuss in detail in Section 3.3.  However, under this interpretation, Green appears to be nearly universally overshooting, especially at the top of 3-point line and to the immediate right and left of the basket.  We also see that Curry, Thompson, Durant, and Pachulia all appear to be underutilized over large sections of the court. 

### **3.2. Lineup Points Lost** 

By reducing the FG% and FGA estimates to ranks we compromise the magnitude of player-to-player differences within lineups.  In other words, focusing solely on ordering renders the distance between player FG%'s irrelevant.  For example, if Curry, Thompson, and Pachulia are ranked one, two, and three, respectively, then the ranked distance between Curry and Thompson is equivalent to the ranked distance between Thompson and Pachulia, despite the fact that FG%'s for Thompson and Curry are probably closer in value than the FG%'s for Thompson and Pachulia. In this section we introduce lineup points lost (LPL) and player LPL contribution (PLC), which measure deviation from the optimal shot allocation (i.e. perfect rank correspondence) while retaining the magnitudes of player differences in FG% and FGA. 

LPL is defined as the difference in expected points between the actual distribution of shot attempts from a given lineup and the expected points had those same shots been taken according to the optimal redistribution.  Formally, we calculate LPL in the Dth cell as 



where OEP@/ and AEP@/ are the optimal and actual expected points for player B in grid cell D, respectively.  We set OEP@/ = Y@ × FG%] @/ × ^@(_`ab) and AEP@/ = Y@ × FG%] @/ × ^@/ , where Y@ is the ] point value of a made shot from cell D.  FG%@/ is the model-based FG% for player B and ^@/ is player B's smoothed FGA per 100 possessions in cell D.  Importantly, B is sorted so that B = 1 corresponds to 





2019 Research Papers Competition Presented by: 

5 



the player with the highest FGA rate in location B for a given lineup. The term ^@(_`ab) is the ?̂@/Ath order statistic of the shot attempt vector cd⋅ = (^@8, … , ^@X), which functions as an index to redistribute the shot attempt vector according to the optimum.  Note that by our definition of the optimum, LPL@ ≥0 and if ?̂@/A = ?̂@/K for all B then LPL@ = 0.  Lastly, LPL@ is scaled to a per 100 possessions basis. 

If we divide LPL@ by the sum of the shot attempts in cell D (LPL@/ ∑X/78 ^@/) this yields LPL per shot. The interpretation of this metric is a bit more abstract—it is the lineup points lost per average `lineup shot' from region D.  LPL per 100 and LPL per shot surfaces for the starting lineups of the 2016-17 Golden State Warriors and Denver Nuggets are shown in Figure 4. 





<!-- Start of picture text -->
LPL per 100<br>0.05<br>0.04<br>0.03<br>0.02<br>0.01<br>0.00<br><!-- End of picture text -->





<!-- Start of picture text -->
LPL per shot<br>0.06<br>0.04<br>0.02<br>0.00<br><!-- End of picture text -->





<!-- Start of picture text -->
LPL per 100<br>0.04<br>0.03<br>0.02<br>0.01<br>0.00<br><!-- End of picture text -->





<!-- Start of picture text -->
LPL per shot<br>0.20<br>0.15<br>0.10<br>0.05<br>0.00<br><!-- End of picture text -->

**_Figure 4._** LPL per shot and LPL per 100 possessions for the Golden State Warrior's and Denver Nugget's 2016-17 starting lineups.  Note that the scales are not equal between the teams. 

Both the Golden State and Denver lineups appear to have their greatest inefficiencies directly around the basket, but there are noticeable differences.  LPL per shot is highest for Denver in the left (relative to the basket) corner-3 region, which is the result of a large quantity of shots taken by Emmanuel Mudiay, who had a poor FG% from this area. Golden State has the highest LPL per shot in regions where Draymond Green and Zaza Pachulia tended to take the most shots. 

### **3.3. Player LPL Contribution** 

While LPL summarizes information from all five players into a single surface, we can parse out each player's contribution to LPL and distinguish between points lost due to undershooting and points lost due to overshooting.  We define player B's LPL@ contribution (PLC) as 







2019 Research Papers Competition Presented by: 

6 



The second term in the right-hand side of the equation apportions LPL@ among the 5 players in the lineup proportional to the size of their individual contributions to LPL@. Players whose expected points under the optimum is larger than their actual expected points in cell D will have PLC@/ > 0, hence positive PLC values indicate that a player is undershooting.  On the other hand, PLC values less than 0 indicate overshooting.  As in the case of LPL, if we divide PLC@/ by the sum of all lineup shot attempts in cell D (PLC@// ∑X/78 ^@/) this yields PLC per average lineup shot. The PLC per shot surfaces for the Warriors 2016-17 starting lineup are shown in Figure 5. 



<!-- Start of picture text -->
Stephen Curry Kevin Durant Draymond Green Zaza Pachulia Klay Thompson<br><!-- End of picture text -->







<!-- Start of picture text -->
PLC per Shot<br>0.02 (Under−Use)<br>0.01<br>0<br>−0.01<br>−0.02 (Over−Use)<br><!-- End of picture text -->

**_Figure 5._** PLC per shot surfaces for the GSW 2016-17 starting lineup. 

Notice that for every red region (under-usage) there are corresponding blue regions (over-usage) among the other players.  This highlights the fact that LPL is made up of balancing player contributions from undershooting and overshooting; for every player who overshoots another player, (or combination of players), undershoots.  For example, Figure 5 shows that Thompson and Curry are both undershooting in a region at the top of the 3-point line where Green is overshooting, suggesting this lineup would be more efficient if some of Green's shots were reallocated.  Note that by the nature of how LPL is constructed, there _cannot_ be any areas where the entire lineup overshoots or undershoots.  For this reason, our method does not shed light on shot selection.  LPL and PLC say nothing about whether shots from a given region are efficient or not, rather they measure how efficiently a lineup adheres to optimal allocative efficiency for that given region. 

### **3.4. Potential Confounding** 

Any conclusions about a player's allocative efficiency based on these metrics must be made carefully. LPL and PLC are influenced by a number of contextual variables which we cannot account for in our analysis, including defensive pressure, time remaining on the shot clock, play calls, and instructions from coaches.  These confounding factors introduce situations where interpreting high or low PLC values directly to sub-optimal usage may be incorrect.  For example, consider the starting lineup PLC surfaces for the Oklahoma City Thunder shown in Figure 6. 





2019 Research Papers Competition Presented by: 

7 





<!-- Start of picture text -->
Steven Adams Victor Oladipo Andre Roberson Domantis Sabonis Russell Westbrook<br><!-- End of picture text -->





<!-- Start of picture text -->
PLC per Shot<br>0.05 (Under−Use)<br>0.025<br>0<br>−0.025<br>−0.05 (Over−Use)<br><!-- End of picture text -->

**_Figure 6._** PLC per shot surfaces for the GSW 2016-17 starting lineup. 

Notice that Westbrook has a positive contribution in both the right and left corner 3-point locations. Interpreting these as areas of under-utilization would be erroneous because many of these corner 3- point opportunities were created by his own initial drive to the basket and subsequently kicking the ball out to a teammate in the corner.  Obviously, Westbrook can't both drive down the lane and simultaneously pass to himself in the corner. 

Figure 6 also shows a number of ways in which LPL correctly indicates areas of sub-optimal shot allocation.  Russell Westbrook generally appears to overshoot whereas Victor Oladipo is shown to undershoot over large areas of the court.  Perhaps the Thunder could have gained more utility from Oladipo prior to his trade had they been more aware of these insights.  Additionally, the Thunder may have benefited by having someone other than Roberson fill the role as the primary corner 3-point shooter in drive-and-kick plays. 

## **4. League Results** 

We now report LPL results for the entire league.  In order to avoid low-minute abnormalities, we restricted our analysis in these sections to lineups that played at least 50 minutes over the course of the 2016-17 regular season.  Table 1 shows the players with the lowest and highest PLC per 100 values in the 2016-17 NBA regular season, aggregated over three court regions: rim, mid-range, and three. 

|||Under-u|sage||||Over-us|age|||
|---|---|---|---|---|---|---|---|---|---|---|
|an|||||||||||
||Rim|Mid-|range|Three||Rim|Mid|-range||Three|
|1|Al Horford (0.95)|O. Porter|(0.25)|G. Harris (0.10)|I. Thomas|(-1.23)|D. Cousins|(-0.27)|K. Oubre|(-0.17)|
|2|K. Korver (0.72)|K. Korver|(0.22)|G. Hayward (0.08)|D. Cousins|(-0.89)|A. Harrison|(-0.23)|B. Rush|(-0.09)|
|3|O. Porter (0.65)|A. A✏alo|(0.17)|R. Anderson (0.08)|B. Grifn|(-0.66)|A. Wiggins|(-0.18)|W. Johnson|(-0.08)|
|4|C. Paul (0.61)|A. Crabbe|(0.16)|D. Booker (0.07)|T. Allen|(-0.57)|I. Thomas|(-0.18)|C. Brewer|(-0.08)|
|5|T. Ross (0.59)|N. Bjelica|(0.16)|D. Lillard (0.06)|J. Randle|(-0.55)|B. Grifn|(-0.15)|M. Chriss|(-0.07)|



**_Table 1._** Players with the lowest and highest PLC per 100 possession values in the 2016-17 NBA regular season, aggregated across three court regions (rim, mid-range, and three).  Each player’s aggregated PLC value is shown in parentheses beside their name. 

Notice that pairs of teammates tend to show up on opposite sides of the table, such as Horford/Thomas, Cousins/Afflalo, and Paul/Griffin.  Other pairs that didn't quite make the top five for both players are Porter/Wall and Harris/Mudiay.  This is in part because of the feature we described previously—under-shooting and over-shooting are by construction balanced within each lineup—but our method suggests that some of these pairs could've been more efficient had their collective pool of shots been allocated differently. 





2019 Research Papers Competition Presented by: 

8 



Another interesting feature in Table 1 is the appearance of specialist players like Kyle Korver and Ryan Anderson on the under-usage side of the table.  These players benefit from incredible shot creators (LeBron James and James Harden) that draw defenders toward them on offense and create open shots for their teammates.  Reallocating more shots to these specialist players may lead to significant decreases in their FG%. 

Table 2 shows LPL per 100 values for each team's maximum minute lineup in the 2016-17 season, partitioned into the same regions described above.  Interestingly, the teams with the highest LPL values at the rim (Sacramento), mid-range (Washington), and 3-point (Oklahoma City) regions have been written about in the media regarding related phenomena.  In 2016-17 The Sacramento Kings had the highest LPL around the rim and Demarcus Cousins posted one of the all-time highest usage rates recorded for a big man in the NBA [12].  In the mid-range region, the Washington Wizards had the highest LPL value with John Wall as the largest over-use PLC contributor to that figure.  A season later, Washington beat writers reproved John Wall for taking bad jump shots early in the shot clock [13].  Finally, Oklahoma City star Russell Westbrook has long been one of the NBA's top shot creators. His drives often lead to open corner 3's for his teammates [14], but unfortunately in 2016-17 Andre Roberson was the most frequent recipient, who has an extremely low 3-point percentage. 

## **5. Conclusion** 

A player's decision to take a shot is heavily influenced by which teammates he is playing with, yet to our knowledge this factor hasn't been explored in a spatial context.  Our research fills this gap by introducing novel methods to evaluate allocative efficiency spatially.  The approach we take uses publicly available data and our code base is available online, allowing our methods to be immediately utilized by teams and analysts.  The examples we have shown here provide only a taste of the intelligence we can derive from LPL and PLC, which in turn can help teams identify areas where they could improve shot allocation among their players. 

We do not advocate for strict adherence to the optimal shot distribution we propose in this paper; as mentioned previously, LPL and PLC are influenced by a number of contextual variables which we cannot account for with only publicly available data.  However, this highlights the flexibility and value that could be gained by franchises with access to proprietary data.  Our methods could be sharpened by accounting for defensive pressure and by omitting play types that don't follow the underlying assumptions for allocative efficiency, such as fast breaks, drive-and-kick plays, and double teams. Additionally, by pairing LPL with play call data coaches could gain specific insight into how plays led to lost points.  Even without this additional contextual information, we believe that LPL has the potential to serve as a valuable diagnostic tool to help coaches and front office staff identify inefficiencies. 

There are many promising directions for future work.  We do not account for usage curves in our analysis, which would be a powerful addition.  LPL could also be adapted to account for usage by considering it as a constrained optimization problem, in which not all of a player’s shots are reallocated to other shooters, but rather just a portion of them.  Finally, by using LPL to inform playerspecific shot policy changes, entire seasons could be simulated using the method in [15] to better quantify the impact of shot reallocation on point production.  Our methods are also simple enough that they could easily be implemented at G-league, NCAA, and international levels.  We hope that 





2019 Research Papers Competition Presented by: 

9 



teams and analysts not only utilize but build upon the methods presented here.  We are confident that doing so will lead to more intelligent offenses and progress in the quest for greater efficiency. 

|Team|Max. minutes lineup|Rim LPL|Mid. LPL|Three LPL|Tot LPL|
|---|---|---|---|---|---|
||Teague, Ellis, George, Young, Turner|0.15|0.07|0.04|0.26|
||Hill, Hood, Hayward, Favors, Gobert|0.25|0.04|0.01|0.30|
||Rondo, Wade, Butler, Gibson, Lopez|0.11|0.33|0.03|0.47|
||Irving, Smith, James, Love, Thompson|0.22|0.18|0.14|0.53|
||Parker, Green, Leonard, Gasol, Aldridge|0.25|0.20|0.07|0.53|
||Lowry, Derozan, Carroll, Siakam, Valanciunas|0.29|0.25|0.09|0.62|
||Holiday, Hield, Hill, Cunningham, Davis|0.34|0.24|0.06|0.64|
||Dellavadova, Snell, Parker, Antetokounmpo, Henson|0.42|0.23|0.07|0.72|
||Rubio, Lavine, Wiggins, Dieng, Towns|0.28|0.43|0.10|0.81|
||Bazemore, Schroeder, Sefalosha, Millsap, Howard|0.56|0.21|0.04|0.82|
||Lillard, McCollum, Harkless, Aminu, Plumlee|0.37|0.31|0.22|0.89|
||Lin, Foye, Lavert, Hollis-Je↵erson, Lopez|0.66|0.24|0.09|0.99|
||Curry, Thompson, Durant, Green, Pachulia|0.89|0.11|0.07|1.08|
||Russell, Young, Deng, Randle, Mozgov|0.75|0.33|0.02|1.10|
||Curry, Ferrell, Matthews, Barnes, Nowitzki|0.92|0.14|0.07|1.13|
||Smith, Caldwell-Pope, Harris, Morris, Drummond|0.81|0.32|0.02|1.15|
||Westbrook, Oladipo, Roberson, Sabonis, Adams|0.43|0.43|0.32|1.18|
||Dragic, McGruder, Waiters, Babbitt, Whiteside|0.87|0.30|0.04|1.21|
||Conley, Allen, Parsons, Green, Gasol|0.86|0.26|0.11|1.24|
||Walker, Batum, Kidd-Gilchrist, Williams, Zeller|0.87|0.28|0.11|1.27|
||Beverly, Harden, Ariza, Anderson, Capela|0.56|0.55|0.24|1.35|
||McConnell, Stauskas, Covington, Ilyasova, Embiid|0.90|0.46|0.04|1.40|
||Thomas, Bradley, Crowder, Horford, Johnson|1.08|0.30|0.08|1.45|
||Mudiay, Harris, Chandler, Gallinari, Jokic|0.79|0.45|0.23|1.47|
||Rose, Lee, Anthony, Porzingas, Noah|1.29|0.19|0.02|1.50|
||Bledsoe, Booker, Warren, Chriss, Chandler|1.02|0.27|0.23|1.52|
||Payton, Fournier, Ross, Gordon, Vucevic|1.24|0.27|0.09|1.59|
||Wall, Beal, Porter, Morris, Gortat|1.37|0.70|0.11|2.17|
||Paul, Reddick, Mbah a Moute, Grifn, Jordan|1.77|0.46|0.12|2.35|
||Lawson, A✏alo, Gay, Cousins, Koufos|1.97|0.50|0.03|2.50|





**_Table 2._** LPL per 100 possession values for each team's maximum minute lineup in the 2016-17 regular season, partitioned into three court regions (rim, mid-range, and three). 

2019 Research Papers Competition 

Presented by: 





10 



## **References** 

- [1]  J. Kubatko, D. Oliver, K. Pelton and D. Rosenbaum, "A starting point for analyzing basketball statistics," _Journal of Quantitative Analysis in Sports,_ vol. 3, no. 3, 2007. 

- [2]  Y.-H. Chang, R. Maheswaran, J. Su, S. Kwok, T. Levy, A. Wexler and K. Squire, "Quantifying shot quality in the NBA," _In The 8th Annual MIT Sloan Sports Analytics Conference,_ 2014. 

- [3]  S. R. LLC, "Calculating PER," [Online]. Available: https://www.basketballreference.com/ about/per.html. 

- [4]  D. Oliver, Basketball on Paper: Rules and Tools for Performance Analysis, Brassey’s Incorporated, 2004. 

- [5]  M. Goldman and J. Rao, "Allocative and dynamic efficiency in nba decision making," _In The 5th Annual MIT Sloan Sports Analytics Conference,_ 2011. 

- [6]  D. Cervone, A. D’Amour, L. Bornn and K. Goldsberry, "A Multiresolution Stochastic Process Model for Predicting Basketball Possession Outcomes," _Journal of the American Statistical Association,_ p. 1–37, 2016. 

- [7]  D. Higdon, "Space and space-time modeling using process convolutions," _Quantitative methods for current environmental issues,_ p. 37–54, 2002. 

- [8]  F. Lindgren, H. Rue and J. Lindström, "An explicit link between Gaussian fields and Gaussian Markov random fields: the stochastic partial differential equation approach," _Journal of the Royal Statistical Society, Series B,_ vol. 73, no. 4, p. 423–498, 2011. 

- [9]  D. Lee and H. Seung, "Learning the parts of objects by non-negative matrix factorization," _Nature,_ vol. 401, pp. 788-791, 1999. 

- [10] J. Besag, "Spatial interaction and the statistical analysis of lattice systems," _Journal of the Royal Statistical Society. Series B,_ vol. 36, no. 2, p. 192–236, 1974. 

- [11] S. Banerjee, B. Carlin and A. Gelfand, Hierarchical Modeling and Analysis for Spatial Data, vol. 2, Boca Raton, FL: CRC Press, 2015. 

- [12] N. Paine, "Demarcus cousins is a usage monster," Jan 2016. [Online]. Available: https://fivethirtyeight. com/features/demarcus-cousins-is-a-usage-monster/. 

- [13] J. Whitacre, "Daily digits: Trimming the bad jumpers out of John Wall’s game," Oct 2018. [Online]. Available: https://www.bulletsforever.com/2018/10/6/17939166/ john-wall-midrange-jumpshots-analysis-washington-wizards.. 

- [14] K. Goldsberry, "Russell, the Creator," 2015. [Online]. Available: http://grantland.com/features/russell-the-creator-westbrook-nba-oklahoma-citythunder-western-conference-kevin-durant-serge-ibaka-kevin-love/. 

- [15] N. Sandholtz and L. Bornn, "Replaying the NBA," _In The 12th Annual MIT Sloan Sports Analytics Conference,_ 2018. 





2019 Research Papers Competition Presented by: 

11 



## **Appendix** 

BOS Starting Lineup LPL per 100 







<!-- Start of picture text -->
LPL per 100<br>0.03<br>0.02<br>0.01<br>0.00<br><!-- End of picture text -->



<!-- Start of picture text -->
LPL per shot<br>0.075<br>0.050<br>0.025<br>0.000<br><!-- End of picture text -->



<!-- Start of picture text -->
Avery Bradley Jae Crowder Al Horford Amir Johnson Isaiah Thomas<br><!-- End of picture text -->







<!-- Start of picture text -->
PLC per Shot<br>0.03 (Under−Use)<br>0.015<br>0<br>−0.015<br>−0.03 (Over−Use)<br><!-- End of picture text -->

**_Figure 7._** Boston Celtics highest minute lineup LPL values with corresponding PLC per shot. 







<!-- Start of picture text -->
LPL per 100<br>0.0125<br>0.0100<br>0.0075<br>0.0050<br>0.0025<br>0.0000<br><!-- End of picture text -->



<!-- Start of picture text -->
LPL per shot<br>0.04<br>0.03<br>0.02<br>0.01<br>0.00<br><!-- End of picture text -->



<!-- Start of picture text -->
Kyrie Irving Lebron James Kevin Love JR Smith Tristan Thompson<br><!-- End of picture text -->





<!-- Start of picture text -->
PLC per Shot<br>0.02 (Under−Use)<br>0.01<br>0<br>−0.01<br>−0.02 (Over−Use)<br><!-- End of picture text -->

**_Figure 8._** Cleveland Cavaliers highest minute lineup LPL values with corresponding PLC per shot. 





2019 Research Papers Competition Presented by: 

12 









<!-- Start of picture text -->
LPL per 100<br>0.020<br>0.015<br>0.010<br>0.005<br>0.000<br><!-- End of picture text -->



<!-- Start of picture text -->
LPL per shot<br>0.12<br>0.08<br>0.04<br>0.00<br><!-- End of picture text -->



<!-- Start of picture text -->
Ryan Anderson Trevor Ariza Patrick Beverly Clint Capela James Harden<br><!-- End of picture text -->







<!-- Start of picture text -->
PLC per Shot<br>0.05 (Under−Use)<br>0<br>−0.05 (Over−Use)<br><!-- End of picture text -->

**_Figure 9._** Houston Rockets highest minute lineup LPL values with corresponding PLC per shot. 

WAS Starting Lineup LPL per 100 







<!-- Start of picture text -->
LPL per 100<br>0.04<br>0.03<br>0.02<br>0.01<br>0.00<br><!-- End of picture text -->



<!-- Start of picture text -->
LPL per shot<br>0.06<br>0.04<br>0.02<br>0.00<br><!-- End of picture text -->



<!-- Start of picture text -->
Bradley Beal Marcin Gortat Markieff Morris Otto Porter John Wall<br><!-- End of picture text -->







<!-- Start of picture text -->
PLC per Shot<br>0.04 (Under−Use)<br>0.02<br>0<br>−0.02 (Over−Use)<br><!-- End of picture text -->

**_Figure 10._** Washington Wizards highest minute lineup LPL values with corresponding PLC per shot. 





2019 Research Papers Competition Presented by: 

13 


