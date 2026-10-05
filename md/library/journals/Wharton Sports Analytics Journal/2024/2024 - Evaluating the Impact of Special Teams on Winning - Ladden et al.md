<!-- source: library/journals/Wharton Sports Analytics Journal/2024/2024 - Evaluating the Impact of Special Teams on Winning - Ladden et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/evaluating-the-impact-of-special-teams-on-winning/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2024 -->
<!-- authors: Matthew Ladden; Ethan Seung -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Evaluating the Impact of Special Teams on Winning

Matthew Ladden — Trinity School ‘25 &

Ethan Seung — Harvard-Westlake School ‘25

January 28, 2024

## Abstract

This paper evaluates the per-play impact of special teams on the winning percentage of NFL

2 teams compared to offense and defense. Employing data from the 1999-2022 NFL seasons in the nflfastR

3 database, we developed a new calculation for Expected Points Added (EPA) to accurately assess the

4 contribution of special teams plays, including punts, kickoffs, and field goals, independent of coaching

5 decisions. This methodology allowed us to create our Special Teams Performance Index (STPI), a

6 composite metric that consolidates the performance of all special teams units on a team. We then used

7 STPI in combination with offensive and defensive ratings from ProFootballReference in a regression

8 model to evaluate the importance of special teams on winning percentage. Finally, since there are fewer

9 plays on special teams than on offense or defense in a game, we adjusted the resulting numbers to find the

10 impact on a per-play basis. We found that an individual play on offense is 3.6 times and that an individual

11 play on defense is 2.6 times more impactful on winning percentage than a play on special teams. Our

12 results can be extrapolated to coaching decisions concerning playing starters on special teams. A special

13 teams play has a significantly lower impact on a game as compared to one on offense or defense, and

14 plays on special teams have a significantly higher per-play injury rate; therefore, starters on offense and

15 defense should generally not be used on special teams.

## 16 Introduction:

Special teams plays, including punts, kickoffs, field goals, and extra points, can significantly

18 influence a football game's outcome. While extra points are limited almost exclusively to a make or a

19 miss, all other special teams plays can affect the score of a game through the resulting field position. For

20 example, a missed field goal can set up the opposing team with a field position that makes scoring points

21 easier. Similarly, pinning a team back at their two-yard line after a punt undoubtedly makes it harder for

22 them to score, but just how impactful is this play in the course of a game? George Allen, a Pro Football

23 Hall of Fame coach, once asserted that: “Football is one-third offense, one-third defense, and one-third

24 special teams,” but his commentary was not grounded in analytics. Research has been published

25 concerning the importance of punting by the 33rd Team, but, according to this model, the top five punting

26 units all had negative expected points added (EPA). Like many others, this EPA model took into account

27 coaching decisions of whether to punt or go for it when calculating the EPA for a given play. Such

28 decisions, when statistically incorrect (i.e. the coach should have elected to go for it), automatically lower

29 the EPA of a punt, regardless of the outcome of the play. Our research aimed to determine the effect that

30 the entirety of a special teams unit can have on a team’s winning percentage relative to its offensive and

31 defensive units on a per-play basis, independent of erroneous coaching decisions.

## 32 Materials and Methods:

An EPA model was used to isolate and measure the performance of special teams units, which

34 measures the actual point value of a given play compared to the expected points derived from historical

35 averages; however, as described earlier, the EPA models that come in datasets like nflfastR, account for

36 incorrect coaching decisions like punting/attempting field goals instead of going for it, rather than directly

37 measuring on-field player performance. Thus, we calculated a new form of EPA by creating an expected

38 points (EP) model to determine the value of a special teams play solely based on the starting field

39 position, eliminating the impact of coaching decisions. This was accomplished by plotting the starting 40 field position of every drive in the dataset along with each drive’s result (in points). Our EP model would 41 serve as the baseline for calculating EPA. Below is our cubic regression model of EP vs. Starting field 42 position from the 1999-2022 seasons, which consisted of 79,389 total possessions:

Kicking it off with kickoffs. We analyzed kickoffs using data from the 2016-2022 NFL seasons, a

45 period chosen because of a rule change that moved the touchback from the 20-yard line to the 25-yard

46 line. To calculate the EPA for kickoffs, we first determined the average resulting field position after a

47 kickoff, which was the 25.52-yard line. Using a version of our EP model with only data from the 2016-

48 2022 seasons, we calculated the expected points a team would score from this average field position. We

49 then calculated the expected points value from the actual starting field position of each kickoff. Taking

50 the difference of these two values gave us the EPA for each kickoff for the kicking team. The EPA for the

51 receiving team is simply the negative of this value. We then calculated the average EPA per kickoff for

52 both kicking and receiving teams for each season and analyzed how these averages correlated to the

53 teams' winning percentages.

To calculate the EPA for each punt, we used the average resulting field position for each yardage

55 where a punt was kicked from. Due to small sample sizes at some of the yardages, we calculated this by

56 averaging the net positions of punts kicked within two yards of each other. For example, to determine the

57 average resulting position for a punt from the 3-yard line, we used data from punts kicked from the 1-yard

58 line to the 5-yard line. We applied our EP model to each average result to estimate expected points for a

59 punt at every yardage. We then calculated the expected points for each punt’s actual resulting field

60 position. The difference between these two expected points values gave us the EPA for the punting team

61 for each punt. By taking the negative value of this EPA, we obtained the EPA for the punt return team.

62 We averaged the EPA of all punts for each team and each season and then analyzed how these averages

63 correlated with the teams' winning percentages.

To calculate the EPA of a field goal attempt, two factors must be evaluated: the expected points

65 for the field goal and the impact of the field position given to the opponent on a miss. The expected points

66 for a field goal is the likelihood of success multiplied by three, making the EPA for any successful FG:

𝐸𝑃𝐴𝑀𝑎𝑑𝑒 𝐹𝐺 = 3 − (3 ∗ 𝑃𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦𝑓𝑖𝑒𝑙𝑑 𝑔𝑜𝑎𝑙 𝑚𝑎𝑘𝑒)

68 To calculate the probability of a successful field goal, we created a regression plane, factoring in kick

69 distance and wind speed for field goal attempts from 1999-2022:

70 71 On a missed field goal, the value of the field position given to the opposing team is calculated by 72 comparing the field position’s expected points value to the expected point value of the average starting 73 field position after a kickoff (the result if the field goal had been made). Thus, the EPA for a missed field

74 goal is the negative value of the expected points for the field goal minus the difference between the

75 expected points of the resulting field position and the average starting position from kickoffs:

𝐸𝑃𝐴𝑀𝑖𝑠𝑠𝑒𝑑 𝐹𝐺 = −(3 ∗ 𝑃𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦𝑓𝑖𝑒𝑙𝑑 𝑔𝑜𝑎𝑙 𝑚𝑎𝑘𝑒 ) − (𝐸𝑃𝑓𝑖𝑒𝑙𝑑 𝑝𝑜𝑠𝑖𝑡𝑖𝑜𝑛

− 𝐸𝑃𝑎𝑣𝑒𝑟𝑎𝑔𝑒 𝑓𝑖𝑒𝑙𝑑 𝑝𝑜𝑠𝑖𝑡𝑖𝑜𝑛 𝑓𝑟𝑜𝑚 𝑘𝑖𝑐𝑘𝑜𝑓𝑓𝑠 )

78 We did not factor in the expected points of the field position given to a team after a field goal miss if all

79 possessions in the same half following the missed field goal have a combined likelihood of less than 5%

80 chance of scoring (as per nflfastR's no_score_prob), such as when there is insufficient time left for the

81 opposing team to score or when a team chooses to kneel. We then calculated the average EPA per field

82 goal for each team in every season between 1999-2022 and analyzed how these averages correlated to the

83 teams' winning percentages.

To compare the impact of special teams units as a whole, we created our own Special Teams

85 Performance Index (STPI). This was created using the sum of the standardized average EPAs for each

86 special teams unit on every team in every season. Using the standardized Offensive and Defensive Simple

87 Rating Systems (OSRS and DSRS) from ProFootballReference and a standardized STPI, we ran a

88 multiple logistic regression model to find the impact of offense, defense, and special teams on winning

89 percentage. We also ran a regression model without the inclusion of our STPI to compare the difference

90 in root mean square error (RMSE) and see if there was an improvement in our rating. By using STPI and

91 thereby including special teams plays that only encompass 15% of all plays in NFL games, we improved

92 the RMSE as compared to the model with only OSRS and DSRS by 1.9%, from 0.107 to 0.105. Taking

93 the ratio of the coefficients from the logistic regression model would allow us to compare the impact of

94 special teams to offensive and defensive units separately as it pertains to winning; however, since special

95 teams units are on the field less than the offense and defense, we divided our results by the ratio of plays

96 each unit is involved in (excluding QB kneels and spikes) to find the difference in per-play impact on

97 winning percentage.

## 98 Results and Conclusion:

## Results from Multi-Regression Model:

Coefficients: Estimate: z_OSRS z_DSRS z_STPI

0.55645 0.40596 0.02877

Number of Occurrences per Play Type:

Play Type: Number of Occurrences:

Percentage:

Pass

463,377

Run

340,589

Kickoff

63,860

Punt

59,644

Field Goal 24,356

Total

951,826

48.68% 35.78% 6.71% 6.27% 2.56%

The top left table contains the results from our multi-regression model, with each coefficient

101 representing their impact on winning percentage. From this, we determined that offense and defense were

102 19.3 times and 14.1 times as impactful over the course of a game as special teams, respectively. To

103 compare the impact on a per-play basis, we divided the results from the regression by the ratio of plays on

104 special teams to offense/defense, given by the top right table. We found that one play on offense and

105 defense is 3.6 times and 2.6 times more impactful on a higher winning percentage than a special teams

106 play, respectively.

Our results can be extrapolated to coaching decisions on deciding if starters should play on

108 special teams. Special teams has a significantly reduced per-play impact on a game compared to offense

109 and defense and a significantly higher per-play injury rate; therefore, starters on offense and defense

110 should generally not be used on special teams.

A further extension of this analysis would be to isolate the kickoff or punt unit from the return

112 unit on each play, using advanced tracking data. This would allow for assessing how much of the

113 resulting EPA stems from the performance of the kicking teams versus the return team, rather than the

114 combination of both units on the field. Finally, the new kickoff rules passed by the NFL have the

7 115 potential to alter how kickoffs are executed and valued. By moving touchbacks up to the 30-yard line, the 116 NFL will encourage more returns on kickoffs, increasing variability in results and the importance of the 117 play to both the return and kicking units. It will be interesting to rerun this analysis next year on the 2024118 2025 NFL season data to determine how this change affects the value of kickoff units and special teams 119 as a whole.

## Acknowledgments:

We would like to thank our partners from Wharton’s Moneyball Academy, Jonathan Dobkin (Mamaroneck High School ‘24), Tyler Frick (Palo Alto High School ‘24), and Xinhang Chen (Renert School ‘24), for their invaluable contributions in conceptualizing, researching, and analyzing the data that formed the basis for this paper. We would also like to extend our gratitude to Professor Wyner, Ryan Brill, Dylan Perlstein, Zeke Kelz, and Elan Roth for their help and instruction throughout the Wharton Moneyball Academy program.

## References:

Ainbinder, R. (2020, September 11). The Future of Special Teams in the NFL. Sports, Tech, Biz. https://www.sportstechbiz.com/p/the-future-of-special-teams-in-the

Horowitz, M., Yurko, R., & Ventura, S. (n.d.). An R package to quickly obtain clean and tidy NFL play by Play Data. Dev status. https://www.nflfastr.com/

NFL team points per game. NFL Football Stats - NFL Team Points per Game | TeamRankings.com. (n.d.). https://www.teamrankings.com/nfl/stat/points-per-game

Nflverse. (n.d.). Nflverse/nflverse-DATA: Automated nflverse Data Repository. GitHub. https://github.com/nflverse/nflverse-data

Simpson, R., & Engler, P. (2023, November 14). Study: Impact of special teams on NFL Success. The 33rd Team. https://www.the33rdteam.com/case-study-impact-of-special-teams-on-nfl-success/

Tokarz, D. (2019, February 18). Beyond Make Percentage: Evaluating NFL Kickers. Yale Undergraduate Sports Analytics Group. https://sports.sites.yale.edu/nfl-kicker-evaluation

Pro Football Stats, history, scores, standings, playoffs, Schedule & Records. https://pro-football-reference.com/
