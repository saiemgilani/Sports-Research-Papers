<!-- source: library/journals/Wharton Sports Analytics Journal/2024/2024 - To Go for Two or Not to Go for Two A Statistical Analysis of the Biggest Prisoner s Dilemma in the National Football League - Venkatesh et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/to-go-for-two-or-not-to-go-for-two-a-statistical-analysis-of-the-biggest-prisoners-dilemma-in-the-national-football-league/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2024 -->
<!-- authors: Atul Venkatesh; Gavin Bulthuis -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

To Go for Two or Not to Go for Two? A Statistical Analysis of the Biggest Prisoner’s Dilemma in the

National Football League

Atul Venkatesh1 and Gavin Bulthuis2

1Dartmouth College 2University of Minnesota

May 25, 2024

Abstract In the National Football League, after a team scores a touchdown, they can kick an extra point or attempt a two-point conversion. Historically, teams have opted for the former, as it had a much higher likelihood of success. In 2015, however, the NFL instituted a rule to move the extra point distance back 13 yards, making it a more difficult kick. This paper will analyze the effect of this rule on the extra point rate, statistically analyzing both strategies and offering recommendations to both NFL teams and the league itself.

## 1 Introduction

In the National Football League (NFL), the ultimate goal of every offensive possession is to score a touchdown. Upon this result, a team is awarded six points and is faced with a decision: attempt a one-point extra point kick or go for a two-point conversion from the two-yard line (Goodell, 2023). Historically, teams often opted for the extra point kick unless they urgently required the additional two points because the extra point attempt was more likely to succeed. Before the 2015 season, however, the NFL decided to move the extra point distance back 13 yards from a 20-yard attempt to a 33yard attempt (Patra, 2015). Despite this decision, it seems like teams are still favoring the one-point strategy. Is this the correct choice? The motivation behind this study is to analyze the impact of this rule change on the league. However, with the rule change making extra point attempts more difficult, it is essential to reevaluate the value of both options.

This study has several objectives. First, the paper examines the extra point and two-point conversion rates from before and after the rule change. Theoretically, the expected payoff for kicking an extra point and going for two should be equal. Did the rule change make the expected payoff of both strategies equal? Or did it increase the disparity? With the help of Monte Carlo simulations, this paper will determine the proper extra point distance that results in a balance between the two strategies. Lastly, by looking at kicking and two-point conversion data, it is possible to determine the number of points a team could have scored by simply attempting the two-point conversion in each instance. This information can allow the calculation of the number of potential points a team could have scored by only opting for the two-point conversion.

The ultimate goal of this paper is to use empirics and statistical analysis to present the NFL with a challenging decision. Should the league maintain the current extra point distance or consider further adjustments to ensure that the decision to kick the extra point becomes more difficult?

## 2 Materials and Methods

To address the above question, we conducted two separate studies—one focused on analyzing two-point conversions, while the other examined extra points. We utilized NFL play-by-play data from the R package nflfastR that spanned from 2006 to 2023, dividing it into two distinct periods: before and after the change in extra point distance regulations (Carl and Baldwin, 2024). The pre-change dataset covers 2006 to 2014, while the post-change dataset spans from 2015 to 2023.

First, we filtered the data to isolate instances of two-point conversions and extra points. For extra points, we subsetted the data to 20 yards (standard extra point distance pre-2015) and 33 yards (standard extra point distance post-2015) for the corresponding dataset. Subsequently, we determined the success or failure of each two-point conversion and extra point attempt, assigning a binary outcome for each attempt. With the data cleaned and filtered, we calculated the success rate of both strategies for each time period, assessing the significance of our findings using a t-test. This statistical test will determine whether there is a notable difference in conversion rates for extra points and two-point conversions between the two timeframes.

Utilizing the ratios from the previous calculations, we created two outcome matrices. The first matrix uses the success rate of extra point attempts and two-point conversions before the rule change to come up with the expected payoff for each strategy. The second matrix examines the same thing, except in the timeframe after the rule change. If one specific strategy has a higher expected payoff, it would be considered the dominant strategy.

Next, we needed to figure out how to find the ideal extra point distance: where the payoff of an extra point and two-point conversion were equal. Using the above proportions as well as their standard deviation, a random sample following a normal distribution was generated for each distance (20 and 33 yards). The two generated proportions were used to create a linear model, with the slope representing the change in extra point percentage with a one-yard increase in distance. Using this model, we were able to approximate the probability of making an extra point at every distance. This was repeated 10,000 times through a Monte Carlo simulation and averaged to account for uncertainty. We then compared the expected payout at all distances with the expected payout of the two-point conversion, which was held constant between timeframes. If the expected payouts were the same, this would indicate that the two strategies are equitable.

How could these findings be applied to a specific NFL team? Kicker skill and offensive prowess might influence how teams view the after-touchdown strategies. To prevent a broad generalization of the results, we decided to see if individual teams would benefit from going for two points. To calculate this, we found the total points a team scored off of extra points and two-point conversions from 2015 to 2023 as well as the number of attempts a team had for each strategy. This made it possible to find a team’s success rate for both two-point conversions and extra points. To get the expected points from attempting a two-point conversion each play, we multiplied the total after-touchdown attempts by two. Then we multiplied the above result by the team’s two-point success rate, thus giving us the expected output. Now to compare the two distributions, let

∆n = 2µi+1 × (xi + xi+1) − (xiµi + 2xi+1µi+1) be the difference between the expected points from a team only attempting two-point conversions and the team’s observed after-touchdown points. xi and xi+1 represent the team’s total extra point and two-point conversion attempts respectively and µi and µi+1 denote the team’s success rate for extra point and two-point conversion attempts respectively. The two-point conversion variables are multiplied by two since it is worth two points.

## 3 Results

The results of our study provide valuable insights into figuring out if the NFL made the correct decision in moving the extra point distance back. Through a rigorous analysis of two-point and extra point data, we have uncovered several noteworthy findings that shed light on teams potentially missing points by opting to kick. Figure 1 compares the extra point success rate before and after the rule change. Before 2015, 11,356 extra points were attempted, with over 99 percent of these kicks resulting in a conversion. After the thirteen-yard pushback, while extra point attempts remained relatively constant at 11,447, the success rate decreased by five percentage points. According to Figure 1, the difference in success rates was statistically significant. In other words, the rule change caused a statistically significant decrease in the extra point conversion rate.

Figure 1: Extra point success rates before and after the 2015 rule change The NFL certainly got the results they wanted, but they may have made two-point conversions much more valuable in exchange. Before the rule change, 529 two-point conversions were attempted from 2006 to 2014. In the same timeframe after the rule change, the league has seen the attempts more than double to a total of 1,126 tries. Despite this increase in attempts, Figure 2 highlights no significant difference in two-point conversion rates, as both proportions were around 49 percent. The observations make sense, as two-point conversions have a smaller sample size, hence accounting for variation, and the extra point rule did not structurally change the process of two-point attempts.

Figure 2: Two-point conversion success rates before and after the 2015 rule change The proportions from Figure 1 and Figure 2 are represented in an outcome matrix. When analyzing the matrices, it is worth noting that extra point conversion rates were multiplied by one, and the two-point conversion rates were multiplied by two to get the expected payout of each strategy.

Figure 3a details the outcome matrix of extra points and two-point conversions before the rule change. Due to the high extra point success rate, extra points had a higher expected payout than two-point conversions. On average, if a team kicked only extra points, they would score more points in the long run. Figure 3b details the outcome matrix of the two strategies after the rule change. The lower success rate of extra points resulted in the two-point conversion having the higher payout and being the dominant strategy. On average, if a team only went for two points, they would score more points in the long run. Moving the extra point distance has made the two-point conversion the dominant strategy, seemingly making it a preferable option.

(a) Before rule change

(b) After rule change

Figure 3: Outcome matrices before and after the 2015 rule change

Figure 4 displays the results of the Monte Carlo simulation for every extra point distance, from 18 yards to 35 yards. The bar plots represent the difference between the expected payout of kicking an extra point at that distance and the expected payout of the two-point conversion. Since the two-point conversion success rate did not change significantly before and after the extra point rule change, the same expected payout for two-point conversions from Figure 3B was used for every distance. To achieve the goal of both strategies having an equal payout, the distance corresponding to the bar closest to zero would be the ideal distance. According to the graph, a 22-yard extra point had the most similar expected payout to a two-point conversion. All extra points over 22 yards received lower payouts than the two-point conversion. Extra points shorter than 22 yards received higher payouts than the two-point conversion.

Figure 4: Finding the extra point distance that achieves equilibrium between the two choices

Two-point conversions seem to be the better strategy. But is this true for every team? Figure 5 displays a team-specific analysis using their extra point and two-point success rates. Shockingly enough, 19 of the 32 NFL teams would have scored more points between 2015 and 2023 if they had only gone for two instead of settling for the extra point. The Kansas City Chiefs would have benefited the most, scoring 177 more points, if they simply attempted a two-point conversion after every touchdown. These findings truly show that perhaps teams should be taking advantage of the two-point conversion.

Figure 5: Team-specific analysis based on team extra point and two-point conversion rates

## 4 Discussion

The NFL’s rule change has undoubtedly impacted the success of extra points, allowing the two-point conversion to become a viable strategy. Based on our analysis, NFL teams should consider going for two points more often as they may be leaving points on the table. Being elite at two-point conversions can provide an advantage that could differentiate between a win and a loss.

However, the team-specific analysis should be taken with a grain of salt. Just because the two-point conversion strategy has a higher expected payoff does not mean that it is appropriate to go for two in every situation. In many cases, kicking an extra point would be more than enough to give a team an advantage and it might not be worth the risk to go for two. For example, imagine if a team tied the game up late in the fourth quarter after scoring a touchdown. The after-touchdown play is likely the last snap in the game. This team can either kick the extra point, putting them up one or go for two, putting them up by two. If the team picks the first strategy, they have around a 93 percent chance to win the game (the probability of converting the extra point). If the team picks the second strategy, they have around a 49 percent chance to win the game. In this situation, it makes a lot more sense to kick the extra point as the reward of converting the two-point attempt is simply not worth the risk of keeping the game tied and potentially losing in overtime. This example tells an important truth. While two-point conversions could be a better strategy, situational factors may make it appropriate for the offensive team to kick the extra point. Figure 6 looks at the distribution of two-point and extra point conversions across a large interval of score differentials from 2015 to 2023. Each bar represents the ratio of two-point attempts to extra point attempts for that specific score differential. This is an accurate reflection of the league-wide consensus on the suitable circumstances to go for two. The taller the bar, the more appropriate it would be for a team to go for two. Anything above the dotted red line indicates that two-point conversions were more prevalent than extra points at that score differential.

Figure 6: Two-point and extra point attempt distributions across an interval of score differentials

Figure 7 details the specific score differentials where it would be appropriate to go for two. In this case, ”appropriate” is defined as a ratio above one. Each one of these score differentials makes sense, as a two-point conversion success could significantly change the course of the game.

Figure 7: Appropriate score differentials to go for two

There are limitations with this analysis, however. First, the figures would vary significantly based on the team. For example, a team with a good offense and an aggressive head coach may go for two in seemingly “inappropriate” situations. Second, measuring the ratios using attempts has its drawbacks. The frequency of two-point and extra point attempts is psychologically based, as teams may prefer the safer option and be more sensitive to larger losses. As a result, just because teams go for two less often in a specific situation does not mean statistical logic supports that strategy. With that being said, this still gives useful information. For example, the data suggests that teams who are up by many points should not go for two. This makes sense, as the reward of a two-point conversion success is minimal and would not change the trajectory of the game.

## 5 Conclusion

While there has been a noticeable increase in two-point conversion attempts across the league since the extra point distance rule change, teams still opt to go for the extra point over 90 percent of the time. However, our thorough analysis has revealed that this option might not be as safe as previously thought. Was the rule change a good idea? The analytics say yes. Moving the extra point distance has revitalized the two-point strategy. Going for two points has historically been classified as an end-ofgame tactic when teams are desperate. The results of this study prove that the two-point conversion strategy needs to be utilized more. Does this mean that teams should go for two points every play? Probably not. However, teams should reconsider how they view the role of the two-point conversion in today’s NFL.

## References

[1] Goodell, R. (2023). Article 3 Section 41. 2023 Official Playing Rules of the National Football League. Retrieved from https://operations.nfl.com/media/tvglh0mx/2023-rulebook_ final.pdf.

[2] Patra, K. (2015, May 19). NFL moves extra point to 15-yard line for 2015 season. nfl.com. Retrieved from https://www.nfl.com/news/ nfl-moves-extra-point-to-15-yard-line-for-2015-season-0ap3000000493347#:~: text=NFL%20owners%20approved%20the%20Competition,at%20the%202%2Dyard%20line.

[3] Carl, S., & Baldwin, B. (2024). nflfastR: Functions to Efficiently Access NFL Play by Play Data. R package version 4.6.1.9008. Retrieved from https://www.nflfastr.com/.
