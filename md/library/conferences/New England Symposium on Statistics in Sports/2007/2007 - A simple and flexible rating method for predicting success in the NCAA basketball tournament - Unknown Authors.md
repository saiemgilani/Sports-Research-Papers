<!-- source: library/conferences/New England Symposium on Statistics in Sports/2007/2007 - A simple and flexible rating method for predicting success in the NCAA basketball tournament - Unknown Authors.pdf -->

**A Simple and Flexible Rating Method for Predicting Success in the NCAA Basketball Tournament** 

**Brady T. West**<sup>**1**</sup> **, M.A.** 

1University of Michigan Center for Statistical Consultation and Research (CSCAR), Ann Arbor, MI 

# **_Background_** 

- Each year, a small NCAA-appointed committee is responsible for selecting 34 Division I basketball teams (31 conference champions receive automatic bids) for the wildly popular NCAA Basketball Tournament, and then assigning regions and seeds to the 65 teams 

- The seeds represent relative strengths of the teams, and higher seeded teams have a better chance of being assigned to a region close to home 

- Numerical ratings used by the committee to seed the teams and assign them to regions need to be strong indicators of expected success in the tournament, resulting in a balanced and competitive tournament 

# **_Objective_** 

- The primary objective of this work was to highlight the simplicity, flexibility, and effectiveness of a proposed rating method (the OLRE method) for the selected teams, which is based on ordinal logistic regression and the expected value of a discrete random variable 

# **_Methods_** 

- Historical data representing team-level variables at the **_ends of the regular seasons_** for the cohorts of teams selected for the tournament were collected from the 2002-2003 season to the 2005-2006 season, using free internet resources (see **_Conclusions_** for the variables) 

- The number of wins achieved by each team in the 2003, 2004, and 2005 tournaments were also recorded and used as a dependent variable in an ordinal logistic regression model, where the predictor variables were the team-level regular season variables 

- Predicted probabilities of winning 0 through 6 games were then calculated based on the fitted model for the 2006 tournament teams, and adjusted to satisfy known marginal constraints for the expected tournament outcomes (e.g., exactly 32 teams will win 0 games) 

- The adjusted predicted probabilities for each team allowed for the calculation of an expected number of wins in the tournament (a rating) 







# **_Results_** 

# **_Conclusions_** 

- The results of one million NCAA tournaments for the 2006 teams were � The ordinal logistic regression model was re-fitted in � A major limitation of this method is the apparent lack simulated in R using the Bradley-Terry model for paired comparisons, 2007, where the 2005-2006 results were considered of freely available information on team-level variables where the strength parameters for the teams were the **_ranks_** of the as additional historical data to strengthen the model, at the **_end of the regular season_** ; additional teams based on Jeff Sagarin’s regular season-end computer ratings and the simulation was also repeated predictors aside from winning percentage, point 

- � The resulting predicted probabilities of winning 0 through 6 games for � The simulation-based expectations had the lower <u>differential, strength of schedule, and number of wins</u> each team based on the simulation were used to calculate a modelsum of squared errors (43.92, versus 54.33 for the <u>against Top 30 opponents</u> would undoubtedly improve the predictive power of the model 

- based expected number of wins, for comparison with the OLRE method OLRE ratings) 

- The sums of squared errors between the OLRE and model-based � The OLRE ratings once again had a higher � Additional historical data prior to 2002 could also be collected to improve the fit of the model (there were 

- expectations and the actual numbers of wins achieved by the teams in correlation with actual success in 2007 (0.72) than only four outcomes of five and six wins available 

- 2006 were calculated and compared to assess predictive power the final regular season RPI ratings (0.68) and when fitting the 2007 model) 

- Sagarin ratings (0.67) 

- The OLRE ratings had the smaller sum of squared errors (63.92, versus 70.02 for the simulation-based expectations), suggesting stronger predictive power 

   - Applications in other tournaments are also possible 

- _For additional information, please visit http://www.umich.edu/~bwest_ 

- � In addition, the Pearson correlation of the OLRE ratings with the actual number of wins was higher (0.67) than both the final regular season RPI _Comments are welcome! Please email me at bwest@umich.edu_ ratings (0.52) and Sagarin ratings (0.55); see the plots above 


