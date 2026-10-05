<!-- source: library/journals/Wharton Sports Analytics Journal/2023/2023 - Optimal Rest Days for Pitchers Maximizing Performance and Wins - Zilberman et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/optimal-rest-days-for-pitchers-maximizing-performance-and-wins/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2023 -->
<!-- authors: Blake Zilberman; Philip Sherr; Lyev Pitram; Marc Sutton -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Wharton Moneyball Academy 2023

Optimal Rest Days for Pitchers: Maximizing

Performance and Wins

Blake Zilberman Philip Sherr Lyev Pitram Marc Sutton

Opening Case: Max Scherzer’s short rest playoff woes

During the 2017 NLDS, the Washington Nationals used Max Scherzer as a starter in game 3. However, two days later in game 5, Scherzer was brought in from the bullpen in the 5th inning of a 4-3 game...

Scherzer proved to be a disaster, allowing 4 runs and costing his team the elimination game, as well as their season.

The Nationals overlooked Scherzer’s need for rest days to return to peak performance.

As a result, the Nationals lost the game and were forced to live with the results of their glaring mistake.

Five-ma n rota tions ha ve been the regula r s ea s on norm for deca des . This long-s ta nding s ta nda rd ma y lea d to a menta l bia s , s imila r to the a vers ion to underha nded free throws in ba s ketba ll.

Are teams following the norm becaus e it is the norm, or becaus e it is correct?

Research Question:

What is the ideal number of res t days between s tarts for pitchers in order to maximize their performance and win the mos t games ?

Why use FIP instead of ERA? r = 0.51 r = 0.33

The correlation between FIP performances at different rest day intervals is 0.51, which is higher than the correlation for ERA, which is 0.33.

FIP focuses on what the pitcher can control, and removes confounding factors like defensive plays by fielders and ballpark dimensions, providing a better estimate of pitcher performance.

Either way, the general ERAs and FIPs scale the same way, allowing us to use them interchangeably.

Too many or too little days of rest are home to largely negative outliers

-17.88% worse than average -7.46% worse than average -6.56% worse than average

-3.51% worse than average

Days of Rest 1 2 3 4 5 6 7+

Combined FIP FIP % diff. from average

5.18

-17.88%

4.59

-7.46%

4.55

-6.56%

4.24

0.27%

4.19

1.32%

4.22

0.72%

4.40

-3.51%

Giving a starting pitcher 1,2,3 or 7 days of rest between starts diminishes their performance.

ERA versus Days of Rest

0.48%

0.59%

3.30%

29.34%

28.62%

12.54%

% of total data

There is not enough data to make proper assumptions about pitcher starts with less than 4 days of rest.

This creates higher variability, making it unreliable to use as a predictor.

The research will focus on pitching with 4, 5, or 6 days of rest between starts

Additional day of rest graphed

Predicted FIP5 = 1.7274 + 0.6083 * FIP4 Benchmark of 4.36

Predicted FIP6 = 1.9094 + 0.5474 * FIP5 Benchmark of 4.23

Break the graphs down into numbers

Days of

Rest

Median FIP 4.46

4.35

4.35

- Better FIP = Lower FIP

- Without adjustments, pitcher performance with 4, 5, and 6 days of rest appear fairly similar

Adjusting FIP

## 1. Subtract FIPDoR from career average FIP

a. Derive the excess FIP produced at each level of rest

1. Ca tegorize pla yers into three groups ba s ed on percentiles a nd a djus t for ca reer perform a nce. a . Given tha t tea m s tend to provide m ore res t to poorer pla yers a nd pla y better pla yers m ore fre q u e n t ly.

## 1 Now let’s adjust FIP for the career average performance

Days of

Rest

Median

Excess FIP

0.01

0.04

- Better FIP = lower FIP

- Once adjusted for career average performance, 4 days of rest stands out as the lowest

Career average FIP - FIPDoR4,5,6 = Excess FIP vs career

= Multiply the beta (regres s ion coefficients ) for each value of res t days by the corres ponding s ubs et (num ber of days of res t and quality of pitcher).

After adjusting for the quality of pitcher, we can see that 5 days of rest produces the best results….

Subtract for the specific DoR and quality categories by the average for each quality category…

Days of Rest

Finds the excess FIP after adjusting for pitcher quality

Good 4 5 6

Average 0.00 -0.03 0.03

Bad 0.05 0.01 -0.06 avg. excess FIP adjusted for pitcher quality

0.19

0.077

-0.11

-0.042

-0.08

-0.036

After adjusting for quality, 5 DoR is strongest

Total Adjusted FIP

Days of Rest Career Avg. Excess FIP Quality Adjusted Excess FIP Total Adjusted Excess FIP

4 0

0.077

0.077

5 0.01

-0.042

-0.032

6 0.04

-0.036

0.004

Earned runs MLB Average Adjustment * 5/9 Runs scored Runs against Win Days of rest innings pitched (2015-2022) after adjusted Percentage

Multiplied by 162 Games

0.042778

4.5

4.560

0.4934

79.9292

-0.017778

4.5

4.475

0.5028

81.4492

0.002222

4.5

4.503

0.4997

80.9440

Excess FIP x average MLB starter innings pitched

Teams that have their pitchers pitch with 5 days of rest between starts should gain an average of….

- 1.52 more wins per season than teams playing their pitchers with 4 days of rest.

- 0.51 more wins per season than teams playing their pitchers with 6 days of rest between starts.

Derived using Bill James’ Pythagorean Win Formula

What was the process?

- Examined the FIP of 6,000 starting pitching performances and grouped them by days of rest.

- Created Adjusted Excess FIP by adjusting for the pitchers’ individual averages and for grouped pitcher quality. - The Adjusted Excess FIP value showed that five days is the optimal rest period between starts.

- Adjus ted Exces s FIP va lue wa s us ed to ca lcula te the number of wins a bove/ below a vera ge tea ms could a chieve by a djus ting the da ys of res t for their pitchers . - Used Bill James’ Pythagorean Win Formula to calculate wins.

A solution which MLB teams can implement to increase their average wins per season.

Final Conclusion

- The four day rest rotation (five man) and the six day rest rotation (seven man) produce an inferior number of wins compared to a five day rest rotation (six man).

By switching from the traditional four to a five day rest rotation, teams can add an average of 1.52 wins per season.

The potential limitation of injuries

JC Bradbury, a sabermetrician, wrote, “there exists little evidence to show that the days of rest affect future injury among adults [athletes].”

Therefore, for the purposes of this experiment, we viewed injuries as a null factor.

However, there may be slight differences in injuries by DoR that haven't been discovered yet….

We are not barring the potential for there to be varying injury levels as a result of differing numbers of rest days.

As a result, this may influence how teams may apply the data discovered.

Further Limitations

● Data only includes the Statcast era (using 2015 -2022)

● Does not consider the possible decrease in pitcher quality when adding additional pitchers to the rotation.

Questions for Further Research

● How do pitchers’ pitch counts vary when they are on different amounts of rest and does it affect their performance?

● Should different strategies be employed in the playoffs?

Sources

● “Player Pitching Game Stats Finder.” Edited by Stathead, Stathead.Com, stathead.com/baseball/player-pitching-game-finder.cgi Accessed 26 July 2023.

● Rymer, Zachary D. “Do Innings Limits, Pitch Counts Actually Prevent Serious Injuries in MLB?” Bleacher Report, 2 Oct. 2017, bleacherreport.com/articles/1622573-do-innings-limits-pitch-counts-actuallyprevent-serious-injuries.

Questions?
