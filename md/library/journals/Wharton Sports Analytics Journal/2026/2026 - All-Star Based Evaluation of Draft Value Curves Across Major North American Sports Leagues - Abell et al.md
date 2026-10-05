<!-- source: library/journals/Wharton Sports Analytics Journal/2026/2026 - All-Star Based Evaluation of Draft Value Curves Across Major North American Sports Leagues - Abell et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/all-star-based-evaluation-of-draft-value-curves-across-major-north-american-sports-leagues/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2026 -->
<!-- authors: Jordan Abell; Felix Soloway-Gilbert; Jonathan Pipping-Gamón; Abraham J. Wyner -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

All-Star Based Evaluation of Draft Value Curves Across Major North American Sports Leagues

Jordan Abell1, Felix Soloway-Gilbert2, Jonathan Pipping-Gamón3, Abraham J. Wyner3 1Latin School of Chicago 2Pilgrim School

3University of Pennsylvania

## Abstract

​

We examine how draft-pick value declines over the course of the draft in the NFL, NBA,

NHL, and MLB, and how the shape of that decline differs across leagues. Using draft and

All-Star data spanning roughly the last 40 years, we fit cubic B-splines to model two outcomes by draft position: the probability that a player is ever selected as an All-Star and the expected number of career All-Star appearances. Draft value declines in all four leagues, but the rate and shape of that decline vary substantially. Within the first round, the NBA and NHL are markedly more top-heavy than the NFL and MLB. Across the full draft, the MLB and NHL exhibit the steepest early decline, whereas the NFL and NBA follow more gradual and broadly similar trajectories. These cross-league differences may help explain variation in incentives around draft position, including the greater prevalence of tanking in the NBA and NHL.

1​ Introduction

In the four major North American sports leagues—the National Football League (NFL), National Basketball Association (NBA), National Hockey League (NHL), and Major League Baseball (MLB)—the draft serves as the primary mechanism by which teams acquire amateur talent. Teams select players in sequence, with the expectation that earlier picks will, on average, produce more value than later ones. A natural question, then, is: how quickly does draft-pick value decline as the draft progresses? A related question is whether that decline follows a similar pattern across leagues.

Comparing draft value across sports is difficult because no single performance metric is used universally. Prior studies have evaluated draft outcomes within individual leagues using league-specific measures. In MLB, Wins Above Replacement is common (Conforti et al., 2022). In the NBA and NHL, studies have often used games played or related outcomes (Miguel et al., 2019; Schuckers, 2011). In the NFL, Pro Bowl appearances and other performance measures are frequently used (Massey & Thaler, 2005). However, these league-specific approaches complicate direct comparison across sports.

To address this problem, we use a common outcome shared across all four leagues: All-Star selection. Although the selection process differs by league, All-Star recognition provides a standardized signal of elite performance that is broadly comparable across sports. Using All-Star outcomes, we estimate and compare draft value curves for the NFL, NBA, NHL, and MLB. Our goal is both descriptive and comparative: to characterize how draft value changes over the course of each draft and to identify how these value curves differ across leagues.

2​ Materials and Methods

For each league, we compiled draft data and career All-Star outcomes for drafted players. For every player, we recorded two variables:

1.​ whether the player was ever selected to an All-Star team, and

2.​ the total number of career All-Star appearances. For the NFL, Pro Bowl selections were used as the league’s All-Star analog.

Data were collected from Sports Reference, Baseball-Reference, and Kaggle. We focus on drafts spanning approximately the 1980s through the 2020s, excluding very recent draft classes whose members have not yet had sufficient time to accumulate All-Star appearances. We then fit cubic B-spline models in R to estimate, as a function of draft position, two outcomes for each league:

1.​ the probability that a drafted player is ever selected as an All-Star, and 2.​ the expected number of career All-Star appearances. These fitted curves allow us to compare both the level and the rate of decline in draft value across leagues.

3​ Results

Figures 1–4 overlay the fitted curves for all four leagues. Additional league-specific plots appear in Appendix A, and the spline equations for each fitted model are reported in Appendix B.

Figure 1 shows the fitted expected number of career All-Star appearances for picks 1–32. Figure 2 extends this comparison to the full draft, with the horizontal axis normalized by percentage of draft completed to facilitate comparison across leagues with different draft lengths.

Figure 3 shows the fitted probability that a player drafted in picks 1–32 is ever selected as an All-Star. Figure 4 presents the same outcome across the full draft, again using draft progress normalized to the total draft length.

Figure 1: All Leagues — Average All-Star Appearances by draft position (picks 1-32)

Figure 2: All Leagues — Average All-Star Appearances by draft position 4

Figure 3: All Leagues — Percent ever named All-Star by draft position (picks 1-32)

Figure 4: All Leagues — Percent ever named All-Star by draft position Across both outcome measures, draft value declines in every league. However, the shape of the decline differs meaningfully across sports. In the first 32 picks, the NBA and NHL exhibit pronounced top-heaviness: the earliest selections carry especially high expected value, followed by a rapid drop-off. By contrast, the MLB and NFL display more gradual declines over the same range.

When the entire draft is considered, the MLB and NHL show the sharpest early declines and approach near-zero value relatively quickly. The NFL and NBA decline more gradually and follow broadly similar trajectories over the full draft.

4​ Discussion

4.1​ Interpretation

The central empirical result is that draft value declines across all four leagues, but not at a common rate. In every league, the decline is steepest at the beginning of the draft and then flattens as the expected value of later picks approaches zero. What differs across leagues is the degree of concentration at the top of the draft.

Across the full draft, the MLB and NHL display the steepest early declines. This suggests that a relatively large share of draft value in those leagues is concentrated in the earliest portion of the draft. The NFL and NBA, by contrast, follow more gradual trajectories overall.

Restricting attention to the first 32 picks reveals a somewhat different pattern. In that range, the MLB and NFL show comparatively steady declines, whereas the NBA and NHL are substantially more top-heavy: the first few selections are especially valuable, after which expected value falls rapidly. This distinction may help explain why draft position is particularly consequential in the NBA and NHL.

4.2​ Limitations and Future Directions

Using All-Star outcomes provides a novel common metric for cross-league comparison, but the approach has several limitations.

First, All-Star selection is not identical across leagues. Voting procedures, roster sizes, positional constraints, and league-specific norms all affect who is selected. As a result, an All-Star appearance may not represent precisely the same level of achievement in each league.

Second, All-Star outcomes capture elite performance rather than overall career value. This makes the measure useful for studying the upside associated with a draft pick, but less informative about differences among non-star players. A player with a long and productive career may still never receive All-Star recognition.

Third, the developmental pathways for drafted players differ substantially across leagues. MLB organizations rely heavily on multiple minor-league levels; NHL teams draw from professional, junior, and college development systems; the NBA has the G League and other pathways; and the NFL has no comparable minor-league structure. These institutional differences likely affect both the distribution of player outcomes and the meaning of later-round selections.

Future work could extend this analysis by incorporating alternative outcome measures, such as career longevity, games played, WAR-based metrics where available, or salary outcomes. Another useful direction would be to quantify uncertainty around the fitted curves and compare leagues using formal inferential procedures rather than relying solely on visual inspection.

5​ Conclusion

Draft-pick value declines in all four major North American sports leagues, but the shape of that decline differs substantially by league. Over the full draft, the MLB and NHL exhibit the steepest early declines, while the NFL and NBA show more gradual overall patterns. Within the first 32 picks, however, the NBA and NHL are the most top-heavy, with especially high value concentrated in the earliest selections.

These differences have practical implications. In leagues where value is concentrated more heavily at the very top of the draft, teams may face stronger incentives to prioritize draft position. Thus, our results are consistent with the greater prevalence of tanking in the NBA and NHL relative to the NFL and MLB. More broadly, the findings illustrate that draft structure and draft incentives vary meaningfully across leagues, even when evaluated using a common performance benchmark.

6​ Acknowledgments

We gratefully acknowledge the support of the Wharton Sports Analytics and Business Initiative and the Moneyball Academy Program. We also thank Tianshu Feng and Noah Sonnenklar for their mentorship and guidance, as well as our teammates Nolan Chong, Jacob Hallas, Jaiden Mehta, and Felix Soloway-Gilbert for their contributions over the summer.

7​ References

Ahmedbendaly. (n.d.). NBA All-Star game data [Data set]. Kaggle. https://www.kaggle.com/datasets/ahmedbendaly/nba-all-star-game-data

Basketball-Reference.com. (n.d.). NBA, ABA, & NCAA awards and honors index. Sports Reference. https://www.basketball-reference.com/awards/

Conforti, C. M., Crotin, R. L., & Oseguera, J. (2022). Major league draft WARs: An analysis of wins above replacement in player selection. Journal of Sports Analytics. https://doi.org/10.3233/JSA-200586

Hockey-Reference.com. (n.d.). NHL & WHA awards and honors. Sports Reference. https://www.hockey-reference.com/awards/

Hrfang. (n.d.). NBA drafts of 1947–2018 [Data set]. Kaggle. https://www.kaggle.com/datasets/hrfang1995/nba-drafts-of-19472018

Massey, C., & Thaler, R. H. (2005). Overconfidence vs. market efficiency in the National Football League draft (NBER Working Paper No. 11270). National Bureau of Economic Research. https://www.nber.org/system/files/working_papers/w11270/w11270.pdf

Mattop. (n.d.). NHL draft hockey player data (1963–2022) [Data set]. Kaggle. https://www.kaggle.com/datasets/mattop/nhl-draft-hockey-player-data-1963-2022

Miguel, C. G., Mílan, F. J., Soares, A. L., Quinauad, R. T., Kós, L. D., Palheta, C. E., Mendes, F. G., & Carvalho, H. M. (2019). Modelling the relationship between NBA draft and the career longevity of players using generalized additive models. Revista de Psicología del Deporte, 28(3), 65–70.

Petti, B., Gilani, S., Baumer, B., Dilday, B., Frey, R., & Kay, C. (2024). baseballr: Acquiring and analyzing baseball data (Version 1.6.0) [R package]. https://billpetti.github.io/baseballr/

Pro-Football-Reference.com. (n.d.). NFL, AFL, & AAFC awards and honors index. Sports Reference. https://www.pro-football-reference.com/awards/

Schuckers, M. E. (2011). What's an NHL draft pick worth? A value pick chart for the National Hockey League. St. Lawrence University. https://myslu.stlawu.edu/~msch/sports/Schuckers_NHL_Draft.pdf

## Appendix A​ Additional Graphs

Figure 5: NHL — Average All-Star Appearances Cubic B-spline, interior knots at picks 38.17, 75.33, 112.50, 149.67, 186.83; boundary knots at 1 and 224.

Figure 6: NHL — Probability of Ever Making an All-Star Game Cubic B-spline, interior knots at picks 38.17, 75.33, 112.50, 149.67, 186.83; boundary knots at 1 and 224

Figure 7: MLB — Average All-Star Appearances Cubic B-spline, interior knots at picks 65, 142, 231, 338, 461; boundary knots at 1 and 600. 11

Figure 8: MLB — Probability of Ever Making an All-Star Game Cubic B-spline, interior knots at picks 101, 231, 396; boundary knots at 1 and 600.

Figure 9: NFL — Average Pro Bowl Appearances Cubic B-spline, interior knots at picks 84 and 167; boundary knots at 1 and 250. 12

Figure 10: NFL — Probability of Ever Making a Pro Bowl Cubic B-spline, interior knots at picks 84 and 167; boundary knots at 1 and 250.

Figure 11: NBA — Average All-Star Appearances Cubic B-spline, interior knots at picks 12.80, 24.60, 36.40, 48.20; boundary knots at 1 and 60. 13

Figure 12: NBA — Probability of Ever Making an All-Star Game Cubic B-spline, interior knots at picks 20.67 and 40.33; boundary knots at 1 and 60.

Figure 13: All Leagues — Average All-Star Appearances by draft position compared to league average (picks 1-32) 14

Figure 14: All Leagues — Average All-Star Appearances by draft position compared to league average

Figure 15: All Leagues — Percent ever named All-Star by draft position compared to league average (picks 1-32) 15

Figure 16: All Leagues — Percent ever named All-Star by draft position compared to league average

B​ Equations

The equations for each league’s models (Figure 5-12) with x being pick number. Figure 5:

Figure 6:.

Figure 7: Figure 8: Figure 9: Figure 10: Figure 11: Figure 12
