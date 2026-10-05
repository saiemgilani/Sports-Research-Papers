<!-- source: library/journals/Wharton Sports Analytics Journal/2022/2022 - Stolen Bases are Disappearing as Baseball Become More Analytical - Yellin et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/hstolen-bases-are-disappearing-as-baseball-become-more-analytical/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2022 -->
<!-- authors: Nathaniel Yellin; Trevor Chen; Tobias Coker; Zeyad Shariff -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Stolen Bases are a Bad Value Proposition, a 2019 Update

By Nathaniel Yellin, Trevor Chen, Tobias Coker, and Zeyad Shariff

Wharton Moneyball Academy: Training Camp 2020, Sports Analytics Student Research Journal

Overview

● Why are we posing this question? - in order to understand the decline of steals in the MLB

● We also wanted to see the risk of stealing bases using data from the 2019 season

Statistics we used:

● Weighted stolen bases (wSB) - estimates # of runs a player contributes to his team by stealing bases

● Speed score (Spd)- rates MLB players’ speeds from 0-10 - league average is 4.5

● Steal success percentage - SB/SB attempts ● In our models we are comparing each of these three variables in order to find their correlation with one another ● Correlation - on a linear scale from 1 to -1: if the number is negative then the two variables are inversely related, if the number is positive then the numbers are related. The larger the number, the more related or less related the variables are.

Our Models and Visuals Sources: Fangraphs.com, BaseballSavant.com, and the Lahman Database

This is a scatterplot between successful stealing percentage and wSB (weighted Stolen bases which tells us how much a player contributes by stealing bases)

The correlation between these two variables is 0.5816242 which means they are pretty decently correlated. There is a clear trendline in the plot above.

This is a scatterplot between successful stealing percentage and Spd (speed score which rates a player on their speed and base-running ability.)

The correlation between these two variables is 0.37617 which means they have a very light correlation.

Note: We filtered our dataset for players who had >100 PA

This is a scatterplot between successful stealing percentage and R (runs scored)

The correlation between these two variables is 0. 0.1553179 which means how successful a player is at stealing and how many runs they score are almost not correlated at all

This is surprising because you would expect players who steal very efficiently to score more, on average, but this is clearly not the case. The graph has no trends whatsoever and helps make a case for why stealing bases is not worth it. Since the point of stealing bases is to move players over and generate runs, I did not expect this correlation to be so low.

## Analysis and Conclusions from our Models

● Our analysis showed a positive, somewhat strong correlation of ~0.58 between successful stealing percentage and weighted stolen bases. This means that players who are caught stealing at a low rate contribute positively to their teams.

● We found a relatively low correlation of ~0.38 between successful stealing percentage and speed. This alludes to the fact that a lot more goes into successfully stealing a base than pure speed (pitcher’s delivery, runner’s jump, catcher’s arm, etc.)

● We found a very low correlation (~0.16) between successful stealing percentage and runs scored. This means that even players who mostly stole successfully did not make a significant contribution to a team’s run total, and therefore, its ability to win ball games. Since the main objective of stealing bases is to advance bases (and ultimately score more runs), we were very surprised to see such a low correlation between the two measures.

Online Sources

● The data shows that stealing bases is only worth the risk if the base stealer is safe ~70% of the time (called the required success rate)

● The exact percentage that makes a steal worth the risk depends on what base and how many outs are in the inning, and where the team is in the batting order (don’t steal if Trout’s batting)

● Over time stolen base attempts have gone down, but the success rates have skyrocketed

● In 2015 the actual success rate(67) was higher than the the required success rate(65)

● The required rate lowers to about 60% late in the game (home team down by 1 with a speedster on first and a decent, but not spectacular hitter up and of course less than 2 outs)

Final Conclusion

● While some successful base stealers may contribute a decent amount to their teams, the majority of them make a relatively low contribution.

● Furthermore, while speed may seem like an important part of stealing a base, the two are not nearly as correlated as one might think. Stealing a base depends on a host of other factors, some of which are out of the runner’s control.

● Overall, Billy Beane and Paul DePodesta were right: outs are precious, and stealing bases jeopardizes them. It takes a prolific base stealer (think Henderson) to make a significant contribution to wins. Station to station baseball is the safe option-and usually the smart one.
