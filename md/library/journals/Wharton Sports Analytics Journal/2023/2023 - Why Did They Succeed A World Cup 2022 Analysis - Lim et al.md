<!-- source: library/journals/Wharton Sports Analytics Journal/2023/2023 - Why Did They Succeed A World Cup 2022 Analysis - Lim et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/why-did-they-succeed-a-world-cup-2022-analysis/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2023 -->
<!-- authors: Aaron Lim; Harrison Goetz; Fangzhou Dai; Kelly Zhang; Neil Varwandkar -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Why Did They Succeed? A World Cup 2022 Analysis

By: Aaron Lim, Harrison Goetz, Fangzhou Dai, Kelly Zhang, Neil Varwandkar

Advisor: Naomi Korn

Wharton Moneyball Academy Flex 2023 Sports Analytics Student Research Journal

## Introduction

● The World Cup is considered the premier competition in soccer, with the winner claiming the honor of the title of the sport’s best.

● Diﬀerent factors contribute to teams making it all the way to the ﬁnal and doing well in the competition

Hypothesis

The factors salary and goals per 90 are most predictive of a team’s World Cup ﬁnal rank in 2022

Procedure

● We took a whole host of data from the 2022 Qatar World Cup, and gave each team a ﬁnal rank as well as statistics for each team.

● From the data, we compared the rank to many diﬀerent data categories like salary, goals_per90, xa_per90, defensive actions and more, to ﬁgure out which data category had the closest correlation to the ﬁnal standings.

● The data was obtained from Kaggle: Performance Attributes and joined with Fifa World Cup 2022 Rankings.

● Analysis of data and code run in R

## Results: Eﬀect of Salary on Rank and Stage Reached

cor(tb5$salaryupdated, tb5$Rank)= -0.532

The graph show that teams with lower salaries did worse than teams with higher salary.

## Results: Correlation between Goals Per 90, and Rank

cor(tb5$goals_per90, tb5$Rank)= 0.5657

As goals increase, a team’s rank gets better. This makes sense as a team’s rank is dependent on winning games and in order to win games the team needs to score more goals.

## Results: Further Impact of Salary on Team Rank

This graph shows a moderately strong correlation between team rank and expected assists. Teams with more expected assists had a better rank. This is conﬁrmed by the linear regression model with a correlation of -0.55 and r^2 of 0.44.

The graph above displays a strong positive correlation between expected assists and team salary. Teams with a higher salary typically have better expected assists. This is conﬁrmed by a linear regression model with a satisfactory r^2 of 0.78.

Salary impacts additional team rank factors, making it a signiﬁcant indicator of team rank.

Results: Correlation between Team Rank and Goal Creating Actions per 90

This graph shows a moderately strong correlation between team rank and goal creating actions per 90. Teams with more goal creating actions typically have a better rank. This is conﬁrmed by the linear regression model with a correlation of -0.55 and a r^2 of 0.31.

Results: Correlation between Team Rank and Expected Goals Plus Minus Per 90

This graph displays that the best teams in this competition ended up having a higher overall expected goals per 90 over their counterparts. This is established by the negative linear regression correlation of -0.4534295.

Results: Predictor variable correlations with rank Compared

Variable Compared Correlation with Rank

Salary

-0.53

Goals per 90

-0.57

Expected Assists

-0.55

Goal Creating Actions

-0.55

Expected Goals +/- per 90

-0.45

Note, lower rank is better. So a correlation with a negative value is a variable with a positive correlation to a world cup success.

## Conclusion

● While “goals per 90” and “expected assists” showed the highest correlation, all of the other variables showed a strong correlation with rank

● Since all of these stats (bar salary) measure ‘attacking stats’, the strong correlation showed that more of a attacking style of soccer is favored.

● External factors like injuries, team chemistry, and strength of opposition were all components that skewed certain data points, hence the anomalies.
