<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2012/2012 - The Individual Factors of Successful Free Throw Shooting - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1414 

## The Individual Factors of Successful Free Throw Shooting 

**Allan Z. Maymin,** _AllianceBernstein_ **Philip Z. Maymin,** _NYU-Polytechnic Institute_ **Eugene Shen,** _AllianceBernstein_ 

©2012 American Statistical Association. All rights reserved. DOI: 10.1515/1559-0410.1414 

## The Individual Factors of Successful Free Throw Shooting 

Allan Z. Maymin, Philip Z. Maymin, and Eugene Shen 

#### **Abstract** 

We use three-dimensional optical tracking data on the 25-frames-per-second positional data of 2,400 free throw shots by the twenty players with at least twelve tracked makes and twelve tracked misses over the course of the 2010-2011 NBA season, fit each trajectory to a comprehensive physics model to find the implied backspin, initial launch height, velocity, angle, and left-right deviation, and examine the differences of those five factors between makes and misses for each player with sufficient attempts in our sample. We find that usually one or two factors are most responsible for a given player’s misses, but the particular factors at fault differ across players. Thus, the causes of successes and failures in free throw shooting are idiosyncratic. This framework may also be useful in analyzing jump shots taken during the game. 

**KEYWORDS:** free throws, physics, trajectories, shooting, success, NBA 

**Author Notes:** The authors thank STATS LLC for the data and Jeffrey Chuang, editor Jim Albert, and the anonymous referees for comments and suggestions. 

Maymin et al.: The Individual Factors of Successful Free Throw Shooting 

### **1. Introduction** 

Why do professional basketball players not make more of their free throws? Malcolm Gladwell raised this question at the 5<sup>th</sup> Annual Sloan Sports Analytics Conference in a panel on player development (Gladwell 2011). When the margin of victory in many games can be overcome by more precisely shooting free throws, and numerous examples exist of regular people able to achieve high percentages, it is a mystery why professional basketball players do not devote enough time to master this task. Since Gladwell raised the question, no single answer has emerged. 

Pelton (2011) cast doubt on several myths commonly proffered as answers by showing that Europeans and other foreign-born players do not shoot better than American-born players; that free throw shooting has not improved over time, since both the NBA and the NCAA seem to have reached rough equilibriums of free throw shooting at 75 and 69 percent respectively; and that the reason big men are poorer shooters may be partially biophysical and not necessarily the result of a rational economic trade-off of more marginally prized skills in a small talent pool. 

Pelton noted that the question of whether players can improve their free throw shooting, “by far the most important of these questions,” nevertheless happened to be “the most difficult to answer with any sort of certainty from the data.” Indeed, since there are a large number of parameters impacting the free throw, it is currently time consuming and difficult to improve one’s free throw shot. 

This paper investigates the influence of the different trajectory parameters on an individual’s success in shooting free throws. We find that trajectory parameters can be correlated with success, thereby making it possible to identify the few key areas that a player can focus on, thus making it easier and faster for him to improve his free throw shooting. 

We identity those factors by using a novel three-dimensional optical tracking dataset provided by STATS LLC, fitting the trajectories of the tracked free throws to coupled differential equations derived from physical considerations by Fontanella (2006), and evaluating the difference of the implied parameters to the trajectories between makes and misses. 

We find that the reason players miss free throws vary from player to player. Thus, the reason there has not been one explanation is that there is not just one explanation. We find that five factors largely determine the efficiency of free throw shooting: the height of release, the launch velocity, the vertical launch angle, the left-right deviation, and the backspin. 

Other literature has examined theoretically optimal shooting trajectories. Hamilton and Reinschmidt (1997) provide recommendations as a function of launch height, finding generally that the ball ought to be sent closer towards the 

1 

_Submission to Journal of Quantitative Analysis in Sports_ 

far rim than the near rim. Hay (1993) determined the release angle with the greatest margin for error. Tran and Silverberg (2008) used simulations to calculate the optimal five factors, showing that for a release at seven feet above the court, the optimal angle is 52 degrees and the optimal back spin about 3 revolutions per second. In other words, there do exist optimal theoretical combinations of the five factors that produce excellent free throw results; our focus here is instead to document what top professional basketball players actually do and explore which factor deviations are most responsible for the misses. 

### **2. Data** 

The three-dimensional optical tracking data from STATS LLC assigns to each player on the court an ordered pair representing the position of their center of mass on a regulation 94 feet by 50 feet NBA court, and assigns to the ball an additional _z_ coordinate specifying its height above the ground. These coordinates are recorded 25 times per second. In addition, event identification information is automatically assigned to frames satisfying certain criteria; for example, free throw makes or misses are tagged as such. 

The data set covers 158 games during the 2010-2011 season. Due to differential adoption, these games are skewed towards the teams that installed the required technology, namely Houston, Dallas, San Antonio, and Golden State. (Though the technology was also installed in Boston and Oklahoma City, the data for those games were unavailable for analysis.) 

The free throw attempts in this data set are extracted as those consecutive sequences of frames in which only the ball and the shooter appear for which a made or missed free throw event is recorded. 

There were 6,366 such free throws shot by 337 distinct players in our sample. Figure 1 shows the distribution of estimated backspins, which was constrained in our numerical fit to be positive but below ten. The backspin or � is expressed as a positive number when the ball has proper backspin. For example, a reasonable value of � is around two, meaning the ball completes two backwards revolutions per second. One second also happens to be the typical duration of the ball’s trajectory to the rim so the backspin may also be interpreted as the number of backwards revolutions during its trajectory. 

2 

Maymin et al.: The Individual Factors of Successful Free Throw Shooting 



**Figure 1.** This figure plots the histogram of estimated backspin parameter values. The backspin values on the _x_ -axis are expressed in the number of backwards revolutions per second. The counts on the _y_ -axis are on a log scale. 

### **3. Methodology** 

For each free throw, we fit the trajectory of the ball to the comprehensive fourfactor Fontanella (2006) two-dimensional coupled ordinary differential equations (DiffEq) derived from the combined physics of gravity, the Magnus force, the drag force, and the buoyant force, reproduced below with all physical parameters such as the acceleration of gravity replaced by their numerical values: 



where _x_ represents the horizontal distance from the center of the ball to the center of the rim and _z_ represents the height of the ball above the floor, with all distances in this DiffEq expressed in meters. The boundary conditions for the DiffEq are the initial launch velocity, expressed as a vector with a component in each of the _x_ - and _z_ -directions (or, equivalently, as the initial launch magnitude and angle from the floor), and the initial launch height. The parameter � represents the backspin. 

To isolate as much of the trajectory as possible where the ball is not in contact with the player or the rim, a two-stage approach is used. First, the data points closest to where the ball attains its maximum height are used to obtain the best‐fit parameter estimates to the DiffEq. Second, the data points are extended 

3 

_Submission to Journal of Quantitative Analysis in Sports_ 

further so long as the error from the first-stage fit are smaller than twice the maximum error of the first-stage points, where the error is defined as the absolute difference between the observed values and the fitted values. This procedure ensures that as many data points from the ball’s free flight trajectory are used as possible. 

The four input parameters to estimate from the DiffEq are the backspin, launch height, launch velocity, and launch angle. The least-squares fit is computed using a constrained numerical evaluation of the solution to the DiffEq for each given set of input parameters, with the constraints corresponding to reasonableness restrictions like prohibiting topspin rather than backspin, prohibiting more than ten revolutions per second of backspin, requiring a minimum launch velocity, and requiring initial launch height greater than zero. These constraints do not bind in the cases examined here and merely serve to remove trajectories with insufficiently accurate data from consideration (see earlier discussion in the Data section). Output parameters and other calculated values include the maximum height achieved by the ball, its airtime, the maximum deviation of the actual trajectory from the best-fit trajectory, and two novel measures of “goodness-of-shot” that we introduce in the next paragraph to evaluate shots on a more continuous basis than the binary in-or-out measure. 

The goodness-of-shot numbers are determined based on where the ball would have been relative to the center of the rim had its downward trajectory continued unobstructed to a height of exactly ten feet, the height of the basketball rim. From this point, we estimated both the left-right deviation and the overall distance from the rim to the closest part of the basketball. The left-right deviation is the fifth factor, in addition to the launch parameters, that we will see explain successful free throw shooting; the distance from the rim is the “buffer,” measuring how much room for error the shot allowed, and has a maximum value of 4.3 inches; this maximum value is obtained when the ball is exactly in the center of the rim. This novel metric allows a continuous alternative to the traditionally binary measures of whether the shot was successful or not, thus enabling greater precision. An alternative definition for the buffer excludes the left-right deviation; we call this the “fitted buffer” to distinguish from the “actual buffer.” 

4 

Maymin et al.: The Individual Factors of Successful Free Throw Shooting 



<!-- Start of picture text -->
Heig<br>h<br>Fram<br><!-- End of picture text -->

**Figure 2.** This figure shows the height of the ball as a function of time, with time measured in frames at the rate of 25 frames per second, and various estimated values as described in the text reported at the top of the chart. 

Figure 2 displays a typical example of the trajectory of the ball, the best-fit input parameters, and the other output values. It represents a free throw attempt by Dirk Nowitzki with 2:32 left in the second quarter of a game between the Dallas Mavericks and the Charlotte Bobcats on October 27, 2010. The blue dots represent the height of the center of mass for the basketball as a function of the time, with time expressed in frames. 

At first, Nowitzki holds the ball, then dribbles it three times, raises, and shoots. The orange dots represent the trajectory used for fitting the parameters. The brown curve represents the best-fit trajectory from the DiffEq. 

Nowitzki’s initial launch height �� was 9.36 feet, the initial velocity �� was 24.95 feet per second, the initial angle to the floor � was 37.6 degrees, and the backspin � was 1.395 backwards revolutions per second. Nowitzki’s left-right deviation �� was -3.65, indicating the shot ended up 3.65 inches to the left of the center of the hoop. The maximum absolute error ��� between the actual data (orange dots) and the best-fit values (brown curve) was 1.25 inches. The basketball reached a maximum height ����� of 12.95 feet on its trajectory, and it was airborne, between the time it left Nowitzki’s fingertips to the time it passed through the hoop, for just under a second (��������. The fitted buffer value 

5 

_Submission to Journal of Quantitative Analysis in Sports_ 

���������, ignoring left-right deviation, was 0.28 inches, meaning that if Nowitzki’s shot had been perfectly centered, the ball would have had a buffer of more than a quarter inch; a very clean make. The actual buffer value ���������, including left-right deviation, was -1.12 inches, meaning a little more than an inch of the ball landed on or past the rim. Nevertheless, the shot was a success (indicated by a “1” in the last value of the second row following Nowitzki’s name). 

We generated a similar plot and analysis for every free throw trajectory in the data. 

Next, for each player, we compared the average of each of the input and output variables for missed free throws and made free throws, and reported those where the two-sample �-test rejects equality. This allows us to quantify the differences one might observe on visual inspection of free throw trajectories. However, some of the observed differences may be a result of other differences. 

To examine the core factor differences, we ran player-specific logistic regressions. For each player, we standardize each of the predictor variables, run a logistic regression, and select those variables that are significant at the 10% level, i.e., exhibiting a difference in deviance statistic in excess of 2.7. Of those significant variables, we further explore all possible interactions, and again keep only those that significantly reduce the deviance statistic. 

Finally, we graph the implied probability of making a free throw as a function of each of the significant variables or interaction terms. 

### **4. Results** 

Table 1 displays the average values of all five factors for the makes and misses of each player, sorted by the smaller of the number of free throw attempts the player made or missed. Statistically significant differences at the five and ten percent significance levels of the relevant �-test are separately highlighted. 

Overall, players have all sorts of problems with their shots. Players could naturally conclude they need work on all aspects of their free throws. However, we find that the reasons for a missed free throw vary from player to player, but are consistent within a player. For example, Dirk Nowitzki’s backspin, launch angle, velocity, and height are virtually identical for his makes and his misses; the only statistically significant difference in his shot is the left-right deviation. In other words, each particular player has his own unique factors that give him trouble. 

Figure 3 shows the probability histograms on a density scale for each of the parameters. The distributions for Nowitzki’s left-right deviation shows a substantial positive spike, whereas the other parameters do not differ materially in their distribution between makes and misses. 

6 

Maymin et al.: The Individual Factors of Successful Free Throw Shooting 



**Figure 3.** This figure shows the probability distributions on a density scale of parameter estimates (backspin, launch height, launch velocity, launch angle, and left-right deviation) for Dirk Nowitzki’s made and missed free throws, as well as all attempts combined. 

Note that each player usually has only one or two areas where their makes and misses differ, suggesting that it is indeed possible for them to improve by focusing on consistency in the relevant factor(s). 

Like Nowitzki, Brendan Haywood, Luis Scola, Shawn Marion, and Richard Jefferson also have a problem with left-right deviation, though Jefferson’s missed shots tend to drift left, whereas the others all drift right. (Each of the twenty players under consideration are right-handed shooters except for Manu Ginobili.) 

Tony Parker, Chuck Hayes, and Ginobili’s misses are all too flat and have too much backspin. Tim Duncan’s misses occur because he shoots too flat and too strong. Jason Terry’s and George Hill’s misses are released too high. Nobody seems to shoot at too high an angle or with too little backspin on their misses. 

A few players exhibited no statistically significant difference in any single area, suggesting either that more shots are needed, or that their misses result from a combination of factors. One player, Tyson Chandler, nearly had three statistically significant differences. 

7 

##### _Submission to Journal of Quantitative Analysis in Sports_ 

**Table 1.** The table below shows the estimated parameters for the five factors of free throw shooting for each player having at least 12 makes and 12 misses, broken down by their makes and their misses, and sorted in descending order by the smaller of their number of makes and misses. Squares highlighted in pink are significant in a two-sided _t_ -test at the 5 percent level; squares highlighted in blue are only significant at the 10 percent level. Comments represent practical interpretations of factors whose expected values shifted from makes to misses; comments in parentheses correspond to differences significant only at the 10 percent level. 



8 

Maymin et al.: The Individual Factors of Successful Free Throw Shooting 

Most importantly, the particular parameters with which players have errors differ across the players. 

In cases with multiple significant factors, it would be beneficial to know how fixing one factor may help or hinder other factors. For example, there appears to be a relation between releasing too flat and employing too much backspin. Perhaps fixing one would fix the other as a natural byproduct. 

To address this issue, and to incorporate the possible cross-correlations of other factors within individual players, we perform a binomial logistic regression of the estimated parameter values for each shot’s trajectory onto the outcome of that shot, made or missed, for each player individually. 

Let us consider Dirk Nowitzki, who had the highest number of both makes and attempts in our sample. Figure 4 shows the pairwise scatterplots and correlations of the five factors with makes in blue and misses in red. Nowitzki’s launch velocity and launch angle are highly negatively correlated: the stronger Nowitzki’s shot, the flatter. 



**Figure 4.** This figure shows the pairwise scatterplots of parameter estimates (backspin, launch height, launch velocity, launch angle, and left-right deviation) for Dirk Nowitzki’s free throws as well as correlations for makes and misses. Blue dots and text represent made free throws and red dots and text represent missed free throws. 

9 

_Submission to Journal of Quantitative Analysis in Sports_ 

**Table 2.** The entries in the table below represent the percentage of free throws made by Dirk Nowitzki for values of the five factors independently sorted by deciles. For example, when his launch angle was in the second decile of his overall range of observed launch angles, in other words, a relatively flat shot, then he made only 86 percent of his free throw attempts. The text size of the correlation numbers are also proportionally scaled to aid in visual comparison. 



**Table 3.** The entries in the table below represent the percentage of free throws made by Dirk Nowitzki for values of five different specifications of left-right deviation independently sorted by deciles. For example, when the absolute value of his left-right deviation was in its highest decile, he made only 86 percent of his free throw attempts. The text size of the correlation numbers are also proportionally scaled to aid in visual comparison. 



Table 2 lists Nowitzki’s shooting percentage in each of the ten deciles of each of the five factors. Most of them show little variability, suggesting that they do not explain much of his performance. Left-right deviation, however, is the lone exception, particularly the highest decile. 

Is the appropriate predictor the simple left-right deviation number, or perhaps its absolute value or squared value? We can examine which predictor specification explains Nowitzki’s free throw performance better. Table 3 lists Nowitzki’s performance for deciles of plain left-right deviation, the absolute value, the squared value, the negative part only, and the positive part only. The best explaining variable specification appears to be pure left-right deviation itself, rather than its absolute or squared value. It, and the essentially equivalent positive-part-only specification, exhibit the greatest variability in Nowitzki’s performance. 

From a statistical perspective, this finding may appear surprising, if one assumes failed shots are equally likely to be missed left or right, and that therefore some specification commensurate with volatility such as the absolute or squared value would be more informative. However, from a basketball perspective, this finding is perfectly reasonable. Ed Palubinskas, a free throw shooting coach who holds multiple Guinness world records for free throws, notes that shots drift right usually because the last three fingers are doing the shooting and they drift left 

10 

Maymin et al.: The Individual Factors of Successful Free Throw Shooting 

because the elbow is too far out (Palubinskas, 2009). Indeed, our analysis confirms Palubinskas’s insight that missing left and missing right are different kinds of misses. Thus the model specification is: 

Pr��� ������1⁄�1 ��<sup>��������������������������������</sup> � 

where the superscript �<sup>�</sup> denotes the standardized values of variable �. We standardize each predictor by subtracting its mean and dividing by the standard deviation so that all of the regression coefficients will be on the same scale. 

However, it may not be the case that each of the five factors is necessary. We can compare the marginal contribution of each factor using a difference-indeviance approach in the logistic regression to select the important predictors. This is done on a player-by-player basis because different factors could be more or less important for different players. 

For example, in the case of Dirk Nowitzki, the difference in the deviance from accounting only for the backspin factor � is 0.16. This difference in deviance is approximately �<sup>�</sup> distributed with one degree of freedom. The associated one-sided right-tailed _p_ -value is 68.6 percent, meaning we cannot reject the hypothesis that the decrease was due to random chance. 

The same analysis applies to all the other factors with a single exception: the difference in the deviance from the left-right factor for Nowitzki is 4.34, with a _p_ -value of 3.7 percent. The critical value for our variate selection strategy is 2.7, corresponding to a _p_ -value of 10 percent. Thus, for Nowitzki, only his left-right factor is important. 

In general, if more than one factor is significant by the above method, all possible interaction terms are added as well, and again only the significant variates are kept. 

Figure 5 shows the results. The fitted probability of a made free throw is shown as a function of the relevant variate. 

Half of the players have only one significant factor, though the particular factor depends on the player. 

Four of the players have no significant factors, with the best estimate of their probability of making a shot being a simple constant. 

Five of the players have two significant factors; for them, a contour plot of the make probability as a function of both variates is plotted. 

One player (Tyson Chandler) has three significant variates; for him, individual plots of changes in his make probability as a function of each separate variate are overlaid. 

In all plots, the standardized variates vary from -2 to 2, meaning we look at the change from 2 standard deviations below the mean to 2 standard deviations above the mean. 

11 

_Submission to Journal of Quantitative Analysis in Sports_ 



**Figure 5.** The figure above displays the graphs of the fitted probability of a made free throw based on player-specific logistic regressions. The formula � displayed in each graph corresponds to the best-fit logit Pr�make��1/�1 ��<sup>��</sup> � and shows the estimated beta coefficients of significant variables and interaction terms. For example, the probability that Blake Griffin makes a free throw as a function of his backspin � is 1/�1 ��<sup>��.����.���</sup> � . The graphs in the middle two columns 

12 

##### Maymin et al.: The Individual Factors of Successful Free Throw Shooting 

have one significant variate; the plot shows the change in make probability for changes in that variate. The graphs in the rightmost column display results with two significant variates with an associated contour plot. The graphs in the leftmost column have four results with no significant variates and one (Tyson Chandler) with three; Chandler’s plot overlays three single plots changing each variate individually while leaving others unchanged. 

A note of caution about interpreting these variables: extreme extrapolation may result in absurd conclusions. For example, Nowitzki’s probability chart appears to suggest that if he were only able to shoot his shots five standard deviations more to the left than his usual average, he would make more than 100 percent of his free throws, even though the ball would obviously not even hit the rim. 

Overall, for individuals, the story remains the same: only a few factors, in many cases even fewer than before, tend to explain each player’s particular problems. 

In more than half of the cases, the factors responsible for the difference between makes and misses for a particular individual remain the same. For example, George Hill’s misses are still too far high and too strong, and the misses of Nowitzki, Luis Scola, and Shawn Marion are still simply too far right. Tiago Splitter, DeJuan Blair, Marc Gasol, and Kyle Lowry still have no significant differences between their misses and makes. Jason Terry still releases too high. Ian Mahinmi still releases too strong and Blake Griffin still has too much backspin. 

However, in six cases, the individualized logistic regression was able to eliminate a factor or two that previously seemed significant. The misses of Tony Parker, Chuck Hayes, and Manu Ginobili seemed to be both too flat and have too much backspin, but in the individualized logistic regression, we find that the only significant factor for each player is the backspin; in other words, if they correct their backspin, the arcs of their shots will likely improve as well. Ginobili was actually able to drop two factors in this way, as his misses also seemed to have been released too high. J.J Barea also seemed to have too flat a shot with too much backspin, but unlike Parker, Hayes, and Ginobili, in Barea’s case, it is his angle that needs to be adjusted, not the backspin. Brendan Haywood still shoots too far right and with too much backspin, but the flatness of his shot is not significant any more. In Haywood’s case, it was the least significant original factor that dropped out in the individualized regression, but that is not necessarily always the case. Tim Duncan, for example, dropped his angle factor: his only remaining issues are shooting too strong and with too much backspin. Correcting those will likely correct his angle as well. 

The remaining three cases are each unique. 

Tyson Chandler continues to have three factors responsible for his misses, but they are not the same as before. He still misses because he shoots too strong 

13 

_Submission to Journal of Quantitative Analysis in Sports_ 

and too far left, but the individualized regression shows that his third factor is not shooting too flat, but rather shooting with too much backspin. 

Kevin Martin has a new factor: in addition to shooting with too much backspin, he also has a significant interaction term, the product of the angle of his shot and the backspin. As his contour graph shows, his angle of release can compensate for his backspin: when he shoots with too much backspin but with a high arc, or too little backspin but with a low arc, he can still make free throws at a high rate, but in other circumstances, he starts to miss more frequently. 

Richard Jefferson falls from having four factors to just two plus their interaction. His misses still drift left and have too much backspin, but they are no longer too strong and too flat, and his excess backspin seems to matter most when he misses to the left. 

### **5. Conclusion** 

Using three-dimensional optical tracking data on the trajectories of thousands of free throw shots over the course of the 2010-2011 NBA season, we fit each trajectory to a comprehensive physics model to find the implied backspin, initial launch height, velocity, angle, and left-right deviation, and examine the differences of those five factors between makes and misses for each player with sufficient attempts in our sample. 

We find that the reason for errant free throws differs across players. To paraphrase Tolstoy (1878), perfect free throw shooters are all alike; every imperfect free throw shooter is imperfect in his own way. 

Each player usually has only one or two factors exhibiting a substantial difference between his makes and his misses, even though an examination of all free throw trajectories across all players would suggest virtually all factors are significant. 

Because improving a player’s free throw shot can be time consuming, particularly because of the large number of parameters, our approach can help by narrowing down the parameters that need to be prescribed with greater consistency. This has the potential of leading to methods of training for the free throw that are less time consuming and therefore more practical. 

As future work, more targeted training methods could be developed for the free throw and, more broadly, the results here taken together with other information that can be gained from monitoring ball movement could lead future trainers and teams to find it useful to monitor ball movement throughout the basketball season, not just for training. 

More specifically, further statistical analysis can be done on the computed trajectory fits to potentially extract further information, with the possibilities suggested in Table 3 being one example. 

14 

Maymin et al.: The Individual Factors of Successful Free Throw Shooting 

Additionally, as more data for players are collected, further refinements to the logistic specification can be made with statistical confidence, such as bifurcating the left-right deviation into two variables, one for left-only and one for right-only. 

Further, this framework may be naturally extended to analyze jump shots made or missed throughout the course of the game. 

### **Appendix** 

#### **The Data** 

The dataset freethrows.csv contains the values of the best-fitting parameters (found using the methodology described in the paper) and the result of each free throw (1 for make and 0 for miss) for the twenty players in the study. 

There are 2,400 rows after the header where a row corresponds to a particular shot of a player.  The column names are: Player Name, Backspin (w), Launch Height (z), Launch Velocity (v0), Launch Angle (a), Left-Right Deviation (lr), and Made/Missed (result; 1=make, 0=miss). 

### **References** 

#### Fontanella, John J. (2006). The Physics of Basketball. Johns Hopkins University 

Press. 

- Gladwell, Malcolm (2011). “Birth to Stardom: Developing the Modern Athlete in 10,000 Hours?” Moderator, player development panel at the 5<sup>th</sup> Annual MIT Sloan Sports Conference, video available at http://www. sloansportsconference.com/?p=559. 

- Hamilton, G.R., & Reinschmidt, C. (1997). “Optimal trajectory for the basketball free throw.” _Journal of Sports Sciences_ 15, 491-504. 

- Hay, J.G. (1993). <u>The biomechanics of sports techniques</u> (4th ed.). Englewood Cliffs, NJ: Prentice Hall. 

- Palubinskas, Ed (2009). “Basketball - Potential Problems That Can Lead to Poor Free Throw Shooting.” _EzineArticles_ , available online at http://ezinearticles.com/?Basketball---Potential-Problems-That-Can-Leadto-Poor-Free-Throw-Shooting. 

- Pelton, Kevin (2011). “Free Throws: Truth and Rumors.” _Basketball Prospectus_ March 30, 2011, available online at http://basketballprospectus.com/ article.php?articleid=1611. 

- Tolstoy, Leo (1878). Anna Karenina. Moscow: T. Ris. See also 2002 translation by Richard Pevear and Larissa Volokhonsky for Pengiun Books. 

- Tran, C.M. and Silverberg, L.M. (2008). “Optimal release conditions for the free throw in men's basketball.” _Journal of Sports Science_ 26, 1147-1155. 

15 


