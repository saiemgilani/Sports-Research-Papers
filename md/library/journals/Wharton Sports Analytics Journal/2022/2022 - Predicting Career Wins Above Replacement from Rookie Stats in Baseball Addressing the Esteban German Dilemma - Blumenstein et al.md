<!-- source: library/journals/Wharton Sports Analytics Journal/2022/2022 - Predicting Career Wins Above Replacement from Rookie Stats in Baseball Addressing the Esteban German Dilemma - Blumenstein et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/predicting-career-wins-above-replacement-from-rookie-stats-in-baseball-addressing-the-esteban-german-dilemma/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2022 -->
<!-- authors: Jack Blumenstein; Josh Braverman; Lekh Murthy; Wilson Wendt -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Predicting Career Wins Above Replacement from Rookie Stats in

Baseball

By: Jack Blumenstein, Josh Braverman, Lekh Murthy and Wilson Wendt

Wharton Moneyball Academy 2022, Sports Analytics Student Research Journal

## Background: The Esteban German Dilemma

Esteban German had a good rookie season, which would seem to lead to later success.

However, over the rest of his career he compiled a lower WAR (1.3) in 5 seasons then he did in his rookie year (1.6). Why??

Why did he play so poorly after a good first season? What causes this to happen throughout the MLB?

Rookie WAR vs. Career WAR

● There is no clear trend between Rookie and Career WAR

● Many points are clustered near the origin with random outliers.

● Only 25% of players in the dataset get more than 10 WAR after their rookie season

Rookie WAR is not a good predictor for Rest of Career WAR, so…

Multivariate Linear Regression

We found specific stats that helped us understand what commonalities rookies with future success shared:

We found:

● Power (ISO) ● Strikeouts (K%) ● Stolen Bases (SB) ● Quality of Contact

(HH%/SH%) ● Defensive Ability (Def/PA) ● Age (Years) ● Team Value (PA/G)

Notable Exclusions:

● Walks ● Position

Logarithmic variables:

● Log(Quality of Contact) ● Log(Age)

## Data Scraping/Cleaning

● We obtained our data from FanGraphs

Filters ● Rookies vs. Rest of Career ● 2003-2015 vs. 2016-2022 ● Rookie Status/Rookie of the Year Voting ● Added the variables that we used in the regression ● Logarithmic Relationships ● Changed variables into rates

Correlation Table

0.72111+0.34493∗(125.5398−(40.4491∗log(AgeRookie))+(0.2039∗SBRookie)+(86.1499∗defensepa)+(26.3500∗ISORookie)−(31.2288∗KRookie)+(5.6711∗log(HS))+(2.9340∗PAG ))+0.04214∗(125.5398−(40.4491∗log(AgeRookie))+(0.2039∗SBRookie)+(86.1499∗defensepa)+(26.3500∗ISORookie)−(31.2288∗KRookie)+(5.6711∗log(HS))+(2.9340∗PAG))^2

## Results

Final Model Correlation: r=0.596, RMSE=9.55 WAR, R.E.=0.197

Predictions

Validation

● Dataset is trained on 2003-2015 but still works great on 20162018 data even with their careers not being over yet

● 2016 ○ 0.621 r ○ 0.216 R.E.

● 2017 ○ 0.696 r ○ 0.282 R.E.

● 2018 ○ 0.581 r ○ 0.185 R.E.

Randy Arozarena vs. Alejandro Kirk

● In the 2021 ROTY voting, Arozarena won while Kirk didn’t receive a vote.

● This year, Kirk has had a breakout season, while Arozarena has regressed.

● Awards based off of one season can be misleading.

## Limitations

● A few of the players in the training dataset have not yet finished their careers

● Minor league success isn’t taken into account

● Steroid era limits data ● No Statcast data ● Injuries

## Conclusion

● Career WAR can be projected well from rookie metrics using our model

● Some players that have a strong start to their careers usually regress because of unsustainable measures in their underlying statistics.

● Our Model actually predicted Esteban German well because of poor underlying statistics in his rookie season

## References

FanGraphs.com https://www.remove.bg/upload https://slidesgo.com https://www.mlb.com/news/2021-mlb-rookie-of-the-year-voting-results https://stats.blue/

Questions?
