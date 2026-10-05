<!-- source: library/journals/Wharton Sports Analytics Journal/2023/2023 - Calculating NBA MVPs Using Advanced Sports Analytics - Shen et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/calculating-nba-mvps-using-advanced-sports-analytics/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2023 -->
<!-- authors: Max Shen; Gergo Nagy -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Calculating NBA MVPs Using Advanced Sports Analytics

By Max Shen and Gergő Nagy

Wharton Moneyball Academy Training Camp 2023, Sports Analytics Student Research Journal

Image from https://www.skysports.com/nba/news/12028/12843612/will-it-be-jokic-giannis-or-embiid-who-claim-the-nbas-mvp-award-ahead-of-the-post-season

## Background

• The NBA MVP, given since the 1955–56 season, is the most prestigious individual award in professional basketball. It is an annual National Basketball Association (NBA) award received by the best performing player of the regular season. While the criteria for the award is subjective, advanced sports analytics can provide a more objective method to measure player performance and identify the most deserving MVP candidate each season.

• In this project, we will use advanced sports analytics to create a model for calculating the 2023 NBA MVP. We will collect data on player statistics, team performance, and other relevant factors to create a comprehensive model that takes into account all aspects of a player's performance.

## Methodology

• Data Collection: We will gather data on player statistics, team performance, and other relevant factors from various sources such as NBA.com, basketball-reference.com, and other sports analytics websites.

• Model Building: We will create new features based on the existing data, such as player efficiency rating (PER), true shooting percentage (TS%), Offensive/Defensive rating, usage rate, and win shares to create our model via R Studios. With those features, we will implement our own created statistics—ShenNagy MVP value—which will be used to calculate and form our predictions for the 2022-2023 season MVP.

• MVP Prediction: Finally, we will use the model to predict the MVP winners from 20062022 and compare it with the actual MVP winner to evaluate the model's effectiveness and accuracy. We will place a focus on the 2016-2017 season, as it was deemed one of the most competitive MVP race. Then evaluate the 2022-2023 season and predict the MVP winner.

## Data Collection:

• First, we analyzed NBA MVPs and winners from 2006 to present, with a focus on the highly competitive 2016-2017 season. We scrutinized the top 10 players who performed exceptionally and compared their base statistics. Next, we then also evaluated the top 10 players who are currently performing strongly in the 2022-2023 season.

NBA MVPs from 2006-2022 Top 10 Players 2016-2017 Top 10 Players 2022-2023 4

## Model Building

• From the base statistics we have collected, we have calculated the advanced statistics for all 36 players.

• We have identified Player Efficiency Rating (PER) as the most accurate correlation with MVP winners. Almost all MVPs from 2006-2022 have had the highest PER among other players over the season, with the exceptions of Kobe Bryant and Dirk Nowitzki.

• Now, we are creating our own statistical model using advanced statistics, known as the ShenNagy MVP value. The model will focus on PER, True Shooting Percentage, Offensive and Defensive Rating, and use Usage Rates and Winshares as prerequisites. The formula for the ShenNagy MVP value will be:

## Model Building

PERR (PER / highest PER in top 10) + Cor(WS, PER) * WSR(Win Shares / highest Win Shares) + Cor(USG, PER) * USGR + …PERR (PER / highest PER in top 10) + Cor(WS, PER) * WSR(Win Shares / highest Win Shares) + Cor(USG, PER) * USGR + …

We calculated the correlation between each of the advanced statistics mentioned. Next, we created a rate for each variable by dividing its value with the highest value among the ten observations. We then multiplied each variable rate with its corresponding correlation factor. Finally, we added up all the products to obtain a balanced sum based on Player Efficiency Rating (PER). It's worth noting that PER is highly offensive-biased, which aligns well with the MVP selection process.

Applying ShenNagy Model to 2016-2017:

Correlation Factors • PERR -> 1 • WSR -> 0.655 • USGR -> 0.500 • TSPR -> 0.207 • ORR -> -0.162 • DRR -> -0.240

Applying Model to 2006-2022:

After applying the ShenNagy Model to all 16 seasons, we have successfully predicted 15/16 seasons, which put us at a 93.75% accuracy rate. The only misprediction was the 2007-2008 season, while Kobe still ranked top 5 for ShenNagy MVP value, the ShenNagy model places Chris Paul first instead. We later on researched this year, and found many fans, critics, and sources claiming Chris Paul was "snubbed" or "robbed" of an MVP and instead preferred ShenNagy MVP winner instead. Articles about the snub: Bleacher Report: Why Kobe Bryant Should Give the MVP to Chris Paul, Sports Keeda: 5 Biggest Snubs of the 21th Century

Applying ShenNagy Model to 2022-2023:

Correlation factors • PER -> 1 • WSR -> 0.4647094 • USGR -> 0.3567048 • TSPR -> 0.5258898 • ORR -> 0.05929663 • DRR -> -0.3659621

ShenNagy Model's Standard Deviation

Z-scores of leaders: Chris Paul – 1.38 Russell Westbrook – 1.68 Nikola Jokic – 1.56

The MVPs are usually around 1.5 SD from the mean, about the top 10%

## Conclusion

The ShenNagy MVP model is effective, but it performs best in determining the first few ranks, which typically have significant performance differences compared to the rest. The model accurately predicted 15 out of 16 seasons, resulting in a 93.75% accuracy rate. However, despite its slight inaccuraccy, critics, fans, and other sources actually favored the ShenNagy model's predicted winner, Chris Paul. This indicates that the ShenNagy MVP model is reliable and credible. Additionally, our model has predicted that Nikola Jokić will be the MVP of the 2022-23 season.

## References

basketball-reference.com. "2016-2017 NBA Awards Voting." basketball-reference.com, https://www.basketballreference.com/awards/awards_2017.html . basketball-reference.com. "About the Statistical Measures." basketball-reference.com, https://www.basketball-reference.com/about/ratings.html. basketball-reference.com. "Most Valuable Player Award Winners." basketball-reference.com, https://www.basketballreference.com/friv/mvp.html. basketball-reference.com. "Win Shares." basketball-reference.com, https://www.basketballreference.com/about/ws.html#:~:text=to%20the%20players.,Offensive%20Win%20Shares%20are%20credited%20using%20the%20following%20formula%3A%20(marginal,36.176%20%3D%2014.27 %20Offensive%20Win%20Shares. ESPN.com. "NBA Awards: Most Valuable Player." ESPN.com, http://www.espn.com/nba/history/awards/_/id/33. NBA.com. "Kia Race to the MVP Ladder." NBA.com, https://www.nba.com/news/category/kia-race-to-the-mvp-ladder. Wikipedia. "NBA Most Valuable Player Award." Wikipedia, https://en.wikipedia.org/wiki/NBA_Most_Valuable_Player_Award#:~:text=The%20National%20Basketball%20Association%20Most,player %20of%20the%20regular%20season. Wikipedia. "Player Efficiency Rating." Wikipedia, https://en.wikipedia.org/wiki/Player_efficiency_rating. Wolfram Cloud. "Basketball True Shooting Percentage." Wolfram Cloud, https://resources.wolframcloud.com/FormulaRepository/resources/Basketball-True-ShootingPercentage#:~:text=The%20true%20shooting%20percentage%20is,times%20the%20free%20throws%20attempted. Wolfram Cloud. "Basketball Usage Rate." Wolfram Cloud, https://resources.wolframcloud.com/FormulaRepository/resources/Basketball-UsageRate#:~:text=Usage%20rate%20estimates%20the%20percentage,all%20divided%20by%20the%20possessions.
