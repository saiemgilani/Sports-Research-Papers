<!-- source: library/journals/Wharton Sports Analytics Journal/2023/2023 - Effect of Increased Three-point Shot Attempts on Probability of Winning in High School Basketball - Kostacos.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/effect-of-increased-three-point-shot-attempts-on-probability-of-winning-in-high-school-basketball/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2023 -->
<!-- authors: Samantha Kostacos -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

2023, Spring Edition wsb.wharton.upenn.edu/student-research-journal

Effect of Increased Three-point Shot Attempts on Probability of Winning in High School Basketball

Samantha Kostacos

Germantown Academy, PA, USA

Abstract Data analytics are used regularly in professional sports today. In particular, NBA basketball has used data science to determine that a strategy of taking more three-point shots has been shown to be effective. However, similar studies have not been done at the high school level. I interpreted data taken from a men’s high school basketball team over the course of one year. Specifically, I recorded the two and three-point shots attempted, the made field goals, field goal percentages and the outcomes of the games. The hypothesis was that increasing the number of three-point shot attempts would lead to a higher offensive rating and wins. After the data was recorded, a series of regression graphs were created to analyze the data. Field goal percentages were calculated from two and threepoint ranges. Graphs compared the field goal percentage vs offensive rating. Three-point shots made and field goal percentage were compared to effective field goal percentage. A comparison of the number of shot attempts with offensive rating and effective field goal percentage were also performed. Finally, the R2 values were compared to determine whether more two-point or three-point shot attempts correlated with victories. The data showed that higher shooting percentages correlated with better offensive rating and higher effective field goal percentages. However, more shot attempts and a higher percentage of threepoint shot attempts did not correlate with victories. The data suggested that a strategy of more three-point shooting was not beneficial in men’s high school basketball. key words: basketball, shot selection, high-school, game strategy

Wharton Sports Analytics Student Research Journal

Introduction Data analytics are used in sports to determine new game plans, ways to score more points, and obtain more victories. This strategy has been used in sports such as baseball, football, and basketball. In particular, data analytics have been increasingly important in the National Basketball Association. Studies have been conducted by teams in the NBA and college basketball to determine how different shots affect scoring. Duke University, a strong school for data science, has researched this topic of shooting, specifically where shots are taken from. Statisticians have used mathematics to determine which locations on the court give more “offball gravity” which can lead to more made baskets (Basketball analytics pipeline).

Studies have shown that NBA teams that shoot a higher percentage of three-point shots lead to more points and victories (Schuhmann). This question has not been studied in high school basketball. Shots made between the basket and the arc are worth two points, while shots from beyond the arc are worth three points. Although the three-point shots are worth more, they are further away from the basket and more difficult to make. High school basketball players are not as skilled as those in the NBA and so have lower shooting percentages.

This study will determine if the strategy of more three-point shooting will affect the offensive performance and the probability of winning at the high school level. The results will help high school teams alter their methods and strategy to win more games. Data from every game in a men’s high school team’s single season will be studied; the two and three-point attempts, makes, and percentages will be studied; additionally, the outcome of winning or losing will be taken into account. The research hypothesis is that if the percentage of three-point shots increases, then the team will have a higher probability of winning a game. This is hypothesized due to the greater point value earned with a three-point shot. The null hypothesis, however, is that if the percentage of three-point shots increases, then the probability of winning the game will not change.

Methods Choose one year to study for a Men’s high school basketball team. Collect data from each game in that season: two-point and three-point attempts, two-point and three-point made. For each game calculate the two-point and three-point FG % using the formula:

Kostacos

Wharton Sports Analytics Student Research Journal eFG % = (FGM + 0.5 * 3PM) / FGA

(Fromal)

Use the data to calculate for the offensive rating per game with the formula:

100*PP/(FGA+0.44*FTA+TO)

(Fromal)

Finally, to create graphs comparing the data.

Results Figures 1a and 1b show the offensive rating for 2-point attempt and 3-point attempts per game. As the field goal percentage increases, the offensive rating also increases for twos and threes; the R2 value is 0.5647 for twos and 0.5091 for threes. Games that they won (red dots) do not correlate with field goal percentage.

Figures 2a and 2b show the effective field goal percentage for 3-point attempts made and 3-point field goal percentage. As three-point makes and field goal percentages increase, the effective field goal percentage increases. The wins (red dots) do not correlate with makes or field goal percentage.

Kostacos

Wharton Sports Analytics Student Research Journal

Figures 3a and 3b show the offensive rating for 3-point attempts and 2-point attempts. As the two-point and 3-point attempts increase, the offensive rating does not increase for both. The slope line for two-pointers is positive with an R2 value of 0.0199. The slope line for threepointers is negative with an R2 value of 0.0001. The wins (red dots) do not correlate with two-point or three-point attempts.

Figures 4a show how the 2-point effective field goal percentage per game varies with the 2-point shot attempt percentage. Figures 4b show how the 3-point effective field goal percentage per game varies with the 3-point shot attempt percentage. As the two-point and three-point attempt percentages increase, the effective field goal percentage does not increase for both. The R2 values are the same for both graphs, but the slope for two-pointers is positive and negative for three-pointers. The wins (red dots) do not correlate with two-point or three-point attempt percentages.

Figure 5 shows the 3-point field goal percentage over a selection of games, both wins and loses. In games that the studied team won or lost by at least twenty points, the three-point field goal percentage affected the outcome. The field goal percentage was much higher than the opponent

Kostacos

Wharton Sports Analytics Student Research Journal in games that they won and much lower in games that they lost.

## Discussion

The null hypothesis of this study that if the percentage of three-point attempts increases, then the probability of winning the game will not change was accepted. As shown in the graphs that compare the shot attempt percentages and the effective field goal percentage, increasing three-point shots does not correlate with the wins (red dots). Additionally, the slope of the graphs for three-point shots is negative, which demonstrates that shooting more two-point shots has a better effect on the effective field goal percentage (how well the team is doing on offense taking into account that three-point shots are worth one more point than two-point shots). The results of this study, which are different from the NBA findings, are likely due to the overall low field goal percentage for three-point shots in high school basketball. When comparing field-goal percentages for shot types, high school three-point shots had a low percentage (30%) compared to the NBA which averages at 36%. Additionally, the final graph compares the study team and the opponents for four games in which they won or lost by at least twenty points; as shown in the graph, the three-point percentage was much higher in games that they won and lower when they lost. This suggests that the three-point shooting percentage does affect the number of points produced and the outcome of the game. When compared to previous studies, these results are novel; in studies in the NBA, it was concluded that increasing three-point attempts leads to more wins.

Kostacos

Wharton Sports Analytics Student Research Journal

## Conclusion

The strategy of taking more three-point shots in high school basketball does not appear to be a successful model. Instead, taking more two-point shots, which tend to be of higher percentage, may be more beneficial for the high school basketball team. As a result, coaches can spend more practice time on focusing on a two-point shooting strategy or emphasizing higher quality threepoint attempts which could lead to a higher three-point percentage. There are limitations of the study which may have affected the results. Only one year and one team was reviewed, so there were only 23 data points for each graph. Additional studies could be done to further explore this topic. Studying a team over multiple years or comparing multiple teams in a single year could provide more insight. Furthermore, one could compare women vs men’s high school teams.

References: Basketball analytics pipeline—from raw video to dynamic visualization. (2019). Rhodes Information Initiative. https://bigdata.duke.edu/projects/basketball-analytics-pipeline-from-rawvideo-to-dynamic-visu alization/

Fromal, A. (2012, January 26). Understanding the NBA: Explaining Advanced Offensive Stats and Metrics. Bleacher Report. https://bleacherreport.com/articles/1039116-understanding-thenba-explaining-advanced-offensi ve-stats-and-metrics

Meng, A. (2018, November 5). Data Analysis on NBA & The 3-Point Shot. Data Science Blog. https://nycdatascience.com/blog/r/data-analysis-on-nba-and-the-3-point-shot/

NBA league average field goal percentage 2021-2022. (n.d.). Statmuse. https://www.statmuse.com/nba/ask?q=nba+league+average+field+goal+percentage+2021-2022 Possession. (n.d.). NBAstuffer. https://www.nbastuffer.com/analytics101/possession/

Schuhmann, J. (2021, October 14). NBA's 3-point revolution: How 1 shot is changing the game. NBA. https://www.nba.com/news/3-point-era-nba-75

Kostacos

Wharton Sports Analytics Student Research Journal

Shin, D. (Ed.). (2022, February 18). A deep dive: how the three-point revolution is changing high school basketball. Tiger Times Online. https://ttonl.org/14310/sports/a-deep-dive-how-the-threepoint-revolution-is-changing-high-sch ool-basketball/

SVG Staff. (2015, April 20). Duke Basketball Deploys Big-Data Analytics. SVG News. https://www.sportsvideo.org/2015/04/20/duke-basketball-deploys-big-data-analytics/ The Truth

About Shooting More Threes. (2018, April 29). Hoopgrind. https://hoopgrind.com/news/the-truthabout-shooting-morethrees/#:~:text=Shooting%20more%20three%20pointers%2C%20at,only%2067%25%20of%20t heir%20games

Kostacos
