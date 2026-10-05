<!-- source: library/journals/Wharton Sports Analytics Journal/2022/2022 - Finding the NBA Draft Diamonds in the Rough - Batra et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/finding-the-nba-draft-diamonds-in-the-rough/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2022 -->
<!-- authors: Ayush Batra; Wesley Neidhardt; Pranav Nanda; Daniel Galper -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

The Pascal Siakam Model

Finding Diamonds in the Rough in the NBA Draft

By Ayush Batra, Wesley Neidhardt, Pranav Nanda, and Daniel Galper

Wharton Moneyball Academy 2020, Sports Analytics Student Research Journal

The Problem

● NBA Draft picks performances in the NBA can almost feel random at times

● Why do non-lottery picks like Pascal Siakam and Kawhi Leonard go on to have All-Star careers while top draft picks like Kwame Brown, Derrick Williams, and Anthony Bennett end up as busts?

Our Goal

● Create a model that uses NBA players standard and advanced stats from college to understand why they were successful or unsuccessful in the NBA

● Apply that model to current college players and try to predict their success in the NBA

## Methods

● Gather college and NBA data from Basketball-Reference for every player drafted in the 2007-2016 drafts who played in college and in over 100 games in the NBA

● Use R to fit and build regression models that predict standard stats like 3-point percentage and advanced measurements like Win Shares.

Win Shares

● A metric that attempts to assign an amount of wins a player contributed to their team

● Main measurement we used to calculate a players success in the NBA

● We used Win Shares/40 minutes for college stats and Win Shares/82 games for NBA stats to measure how many wins each player added over a full 82-game NBA season

Initial Models

First steps towards finding which college stats matter the most when predicting NBA stats

Predicting NBA Win Shares

● First we converted win shares in the NBA to win shares per season ● We then used win shares per 40 minutes in college to predict win shares per season in NBA ● Although college win shares was significant in predicting win shares in the

NBA, the r-squared value was fairly low

R-squared = 0.1249 Correlation = 0.3534

Predicting NBA Win Shares

● We then split the players into 2 groups: guards and ‘big-men’

R-squared = 0.08553 Correlation = 0.2925

R-squared = 0.1593 Correlation = 0.3991

Comparing FG%

● We also compared 3 NBA shooting stats to the same college stats: FG%, 3P% and FT%

R-squared = 0.4225 Correlation = 0.650

Comparing 3P%

● We filtered the dataset so only players who attempted more than one 3-pointer per game in college were included

R-squared = 0.07727 Correlation = 0.2780

Comparing FT%

R-squared = 0.5270 Correlation = 0.7259

## Conclusions and Next Steps

● Splitting the players into groups based on their positions will give us a better prediction for NBA win shares

● College FT% and FG% are much more significant in predicting NBA FT% and FG% than college 3P% is in predicting NBA 3P%

● A multiple regression model is likely to be more effective than a univariate regression model

Final Models

Predicting NBA Win Shares and Shooting Stats

Working With Guards

- First, we split the dataset of players into two groups: Guards and Big Men

- Unfortunately, there were an insufficient amount of Centers for their own group

- Then, we looked at the relationship between Draft Pick and Win Shares per 82 games

R-sqrd = 0.078

WS Regression: Guards

- We created a multiple linear regression using college stats as inputs in order to predict the players’ NBA WS/82

## Results of Multiple Linear Regression

Unfortunately, the residuals are not normal Bad Model?

## Model Performance: Guards

- Let’s see how our model performed on past draft prospects

- Players above the line are those who the model expected to outperform their draft position (and vice versa)

V.Oladipo

S.Dinwiddie

WS Regression: Big Men

Residuals = Approx. Normal

- Higher rsqrd than guards model

- All inputs significant

## Model Performance: Big Men

Top performing big men were all at or above the line

No players that were well below the line did exceptionally well

A Final Look

- There looks to be a moderate association for each group - R-sqrd and plots show big men’s careers easier to predict (though neither is very predictable)

Predicting Future Shooting: FG%

Our group also tried to project future NBA shooting splits using players’ college stats

Inputs: - College FG% - College 3P% - College FT% - Height

Predicting Future Shooting: 3P%

College FT% predicts NBA 3P% better than College 3P%

Note: Players had College 3PAr > 0.1

Predicting Future Shooting: 3P%

College 3P% was NOT a significant variable in a multiple linear regression for NBA 3P% Inputs: College FT%, College 3PAr

COMPARISONS

R-sqrd for univariate models: - College 3P%: 0.066 - College FT%: 0.164

Predicting Future Shooting: FT%

Inputs: College FT%, Height

Areas for Improvement

- While our models were adequate for predicting future NBA performance, they could have been improved

- Potential Issues / Methods for Improvement - Larger Sample Size - Potential Overfitting - Non-linear Fits - Non symmetric distribution of residuals - Bias towards Big Men

The Results of Our Model

- The best way to describe how our model did is to showcase some of the predictions that it got right (big hits) and some of the predictions that it got wrong (big misses).

- What makes a prediction a big hit or a big miss? - A big hit is a player that our model predicted to outperform or underperform his predicted win shares per season based on his draft position, and did so. A big miss is a player that our model predicted to outperform or underperform his predicted win shares per season based on draft position, and did not do so.

Which Statistics Did We Use to Determine Big Hits and Big Misses?

- A player would be able to be considered a hit or a miss if our model predicted them to either outperform or underperform their expected win shares based on draft position. - Therefore, we looked at the discrepancy between our model’s predicted win shares per season for a player and the predicted win shares per season based on draft slot (predicted difference). If the difference between these two was large in either the negative or positive direction, then a player could be considered a hit or a miss. - As discussed earlier, if our model predicted a player to overperform or underperform their expected win shares per season based on draft position, and that player did so, that’s a hit. If our model predicted a player to overperform or underperform their expected win shares per season based on draft position and the player did not do so, that’s a miss. - For misses, we also looked at the discrepancy between a player’s predicted win

Big Hits: Frontcourt

● Anthony Davis (predicted difference: 2.93 WS/82) ● Pascal Siakam (predicted difference: 2.81 WS/82, Difference between predicted win shares per season and actual win shares per season: -0.06 WS/82) ● Karl Anthony-Towns (predicted difference: 2.43 WS/82) ● Joel Embiid (predicted difference: 2.34 WS/82) ● Kawhi Leonard (predicted difference: 1.79 WS/82) ● Draymond Green (predicted difference: 1.20 WS/82) ● Anthony Bennett (predicted difference: -1.02 WS/82)

Big Hits: Backcourt

● Spencer Dinwiddie (predicted difference: 3.36 WS/82) ● Kyrie Irving (predicted difference: 2.60 WS/82) ● Delon Wright (predicted difference: 1.36 WS/82) ● Jimmy Butler (predicted difference: 0.95 WS/82) ● Damian Lillard (predicted difference: 0.85 WS/82) ● Isaiah Thomas (predicted difference: 0.84 WS/82)

Big Misses: Frontcourt

● Nerlens Noel (predicted difference: 2.59 WS/82, residual: -2.34 WS/82) ● Andre Drummond (predicted difference: -0.11 WS/82, residual: 3.87 WS/82) ● Otto Porter Jr. (predicted difference: -0.23 WS/82, residual: 1.31 WS/82) ● Harrison Barnes (predicted difference: -1.73 WS/82, residual: 1.70 WS/82) ● Jaylen Brown (predicted difference: -2.19 WS/82, residual: 1.41 WS/82)

Big Misses: Backcourt

● Buddy Hield (predicted difference: -1.44 WS/82, residual: 1.25 WS/82) ● Klay Thompson (predicted difference: -0.97 WS/82, residual: 3.74 WS/82) ● Jamal Murray (predicted difference: -0.77 WS/82, residual: 1.64 WS/82)

Applying Findings to the 2020 NBA Draft

Who are the best players from this year’s draft?

Mock Draft

We had to use a mock draft in order to compare results of our model versus the model using only draft picks

Website: draftsite.com/nba/mockdraft/2020/round1/

Top 10 College Players

Anthony Edwards: 5th highest Predicted NBA WS/82 for Guards in sample

Potential Bust and Sleeper Prospects

Difference: difference between projected NBA WS/82 based on model and projected NBA WS/82 based on draft pick and position

+ Difference = Underrated - Difference = Overrated

Potential Steals: Carey, Azubuike, Bey, Reed, Perry Potential Busts: Nesmith, Vassell, Maxey, Green, Okoro

Best Shooters - Field Goal %

Udoka Azubuike

Best Shooters - 3 Point %

Isaiah Joe’s 41.2% Predicted 3P% is higher than anyone from the sample set

The End
