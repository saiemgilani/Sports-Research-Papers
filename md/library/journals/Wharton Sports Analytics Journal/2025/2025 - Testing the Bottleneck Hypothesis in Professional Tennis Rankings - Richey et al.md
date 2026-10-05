<!-- source: library/journals/Wharton Sports Analytics Journal/2025/2025 - Testing the Bottleneck Hypothesis in Professional Tennis Rankings - Richey et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/testing-the-bottleneck-hypothesis-in-professional-tennis-rankings/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2025 -->
<!-- authors: Seth Richey; Ryan Rodenberg -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Testing the ‘Bottleneck’ Hypothesis in Professional Tennis Rankings

Seth Richey Florida State University

Ryan Rodenberg Florida State University

Abstract: We test whether recent policy changes by the governing body of men’s professional tennis—the ATP Tour—have created a statistical incongruence in the ordinal ranking of players worldwide. Using a quartet of parsimonious methods, we find prima facie evidence of a so-called ‘bottleneck’ in the ATP Tour men’s singles rankings consistent with publicly acknowledged criticism of the player evaluation system following alteration of the ranking point distribution schedule between the 2023 season and the 2024 season. Specifically, we pinpoint that #100 in the men’s singles rankings exhibits characteristics consistent with a bottleneck that would seemingly impact meritorious promotion and relegation within the sport. Our findings highlight the importance of using sports analytics when designing sport governance models and evaluating the impact of major policy revisions.

April 2025

I. Introduction Tennis rankings—an ordinal measurement of player ability based on aggregate ‘points’ earned during sanctioned tournaments—are the lifeblood of professional tennis. Calculated on an almost weekly basis year-round by the tennis governing body for women (WTA Tour) and men (ATP Tour), such rankings determine whether individual players make the cut for lucrative tournaments like the four Grand Slams or are relegated to lesser professional events with markedly lower prize money. Such rankings are also used for seeding at tournaments and for year-end bonus payments under commercial contracts. After the end of the 2023 tennis season, the ATP Tour opted to alter the ranking determination for male professional players. As detailed in Appendix A, the ATP Tour increased the rankings points available in high-level events while simultaneously decreasing the ranking points allocated to lower-level ‘Challenger’ tournaments.

The change resulted in critical comments by Karue Sell, a prominent professional tennis player from Brazil who also operates a successful YouTube channel entitled ‘Turning Pro at 30.’ (Sheets, 2024). In a series of April 2024 posts on X (formerly Twitter), Sell pointedly expressed his frustration with the augmented ranking points: “Thoughts after playing [C]hallengers again: Tennis is so deep, there’s so much talent. But the ATP once again has f***** it up. Challengers now give fewer points and [ATP T]our events more points. Result? Harder to leave and break into top 100. A losing record will be enough to stay.” (Sell, 2024). Sell continued: “Tennis is not a ‘top 100’ sport anymore. Guys [ranked] 600 are beating [players ranked] 100 (twice this week alone.) Moving up and down should be simpler. A guy can stay top 100 going 15-25 in the year and another can’t break top 100 going 4525. Even more so now with the points difference.” (Sell, 2024).

In tennis, movement into (and out of) the top 100 in the singles rankings is pivotal for career duration and success. Players who are ranked among the top 100 by the ATP Tour are virtually guaranteed entry into the main draw of all four Grand Slam tournaments and the ATP Tour events above the minor league ‘Challenger’ tour. The ATP Tour rankings help form the league structure and determine how players are promoted and relegated between tiers in men’s professional tennis. Indeed, promotion and relegation issues speak to the broader narrative of how sports leagues are constituted and administered by governing bodies, which are prime topics of interest for sports analytics scholars.

In a seminal paper, Stanford professor Roger Noll “explore[d] how promotion and relegation affect the economics of a sports team and league.” (Noll, 2002). Within the context of a sports league like the ATP Tour utilizing a tournament format, three researchers surveyed the tournament design literature and pinpointed three criteria: efficacy, fairness, and attractiveness (Devrissere, et al., 2024). The authors found ranking-related concerns to be one of the main components of tournament design. (Id.). Medcalfe (2024) surveyed over two decades of research and found that “[w]ell-designed [sports] contests have beneficial behavioral responses of competitors such as increased effort which results in higher quality of competition.” Finally, two professors modeled sports leagues with ‘open’ promotion and relegation policies and found that such league structure increased fan welfare. (Jasina & Rotthoff, 2012).

The ATP Tour’s ranking point allocation changes between 2023 and 2024 were not a case of first impression. According to former professional player and author Conor Niland:

In 2009, the ATP Tour changed its ranking points system. The number of points on offer to the winner of a Grand Slam doubles, from 1,000 to 2,000. The top sub-Slam tournaments…were rebranded as ATP 1000 events, as there were now 1,000 ranking points on offer to the winner: again, twice as many as previously. But the points inflation was not applied across the board: the number of points available for lesser levels of achievement at the top tournaments increased by smaller percentages…But at lower levels of the game, the rankings points on offer had not doubled—not even close. This meant that, overnight, the distance between the players making the cut for ATP Tour events and the players trying to win their way out of the Futures and Challenger tours became harder to bridge. The change had its most dramatic effect on the players in the age cohort slightly below me and playing on the lower tours, who now had to win more matches and spend longer building points than previously. I’d like to say there was a collective outcry at the change to ranking points, but there wasn’t. Challengers and Futures players didn’t have a union and didn’t have the time or money to hire lawyers to fight their corner. (Niland, 2024). There was no public explanation for the rationale underpinning the ranking point change between 2023 and 2024. Such absence resulted in speculation by Sell and others. Several months after his initial posts, Sell posited: “I’ve had so many conversations with players/coaches this year regarding the drop in points in the [C]hallenger tour and nobody seems to understand the reasoning behind it. There’s a general feeling of protection of players already top 100.” (Sell, 2024). Sell continued: “I’m just not sure why this decision was made and we’ve had no transparency from the [ATP Tour] in the matter. It was already hard to break into the top 100. But now [it] is nearly impossible to drop out.” (Id.). Sell concluded: “BTW, I complain not because of my situation. But I’m in a unique position where I have some sort of a voice compared to my peers so it would be interesting to get answers. The point structure needs to be fixed.” (Id.).

Regardless of whether the reason behind the change was to somehow protect established players for commercial reasons or otherwise, the allegation of a possible top 100 ranking ‘bottleneck’ motivates this paper. To test for the presence or absence of such a bottleneck, this paper is organized as follows. In the second section, we describe our data set culled from secondary sources and explain our multipronged methodological approach. In section three, we present our results and discuss the implications of our findings. Section four concludes.

II. Materials and Methods Men’s professional tennis operates on a tiered tournament structure, with each level offering different amounts of ATP Tour ranking points. Players earn points based on how far they advance in a tournament, and there are two main ways to calculate a player’s ATP Tour ranking. For ‘commitment’ players, or those ranked in the top 30 at the end of the previous season, their ranking must include points from four Grand Slams, eight mandatory Masters 1000 events, and seven of their best results from other tournaments. For ‘noncommitment’ players, their ATP Tour ranking is based on the 19 best tournament results. Notably, players who receive main draw entrance into any of the four Grand Slams or eight mandatory Masters 1000 events must count the points from those tournaments regardless of result. Additionally, players who qualify for the year-end ATP Tour Finals—specifically, the top eight players who earn the most singles points in a calendar year—can earn additional points not available to others. At the pinnacle of professional tennis, Grand Slams award 2,000 ranking points to the winner, while ATP Tour Masters 1000s, ATP Tour 500s, and ATP Tour 250s offer 1,000, 500, and 250 points, respectively, to their champions. The ATP Tour also organizes Challenger tournaments, providing an intermediate level for professional players where players can earn 175, 125, 100, 75, or 50 ranking points for winning. At the base of this system overseen by the ATP Tour, another organization—the International Tennis Federation (“ITF”)—offers bottom-tier tournaments called M15s and M25s that the ATP Tour has approved for ranking points. Such ITF tournaments offer emerging players a chance to break into the professional rankings, with winners earning 15 ranking points at M15 events and 25 ranking points at M25 events. At all levels of professional tennis, non-winners also receive ranking points based on progression through the tournament. Appendix A outlines the comprehensive point tables before and after the rule change that revised ranking point allocation.

Year-end ATP Tour rankings data were collected directly from the ATP Tour website. For this study, we define year-end rankings as the final release of rankings in a calendar year, differing from the ATP Tour’s definition, which considers year-end rankings as those immediately following the ATP Tour Finals. This distinction is important because lower-level tournaments, which occur after the ATP Tour Finals, can still significantly affect the rankings of ‘non-commitment’ players. The data collected include each player’s ranking and total rankings points earned. We consider data from 2024, 2023, 2022, and 2019-2011. We exclude 2020 and 2021 due to the ATP Tour’s introduction of truncated

‘protected’ rankings during the COVID-19 pandemic, which essentially froze rankings during that time.

We then test the bottleneck hypothesis, with the null hypothesis being that such a bottleneck does not exist at or immediately around #100 in the rankings. Four methods will be used to test this hypothesis using a multi-pronged pilot study-type of approach. All data analyses are done through the Python programming language.

The first metric is a ‘sticky’ calculation, which quantifies the number of players that stay within the top 100 from one year to the next. Players who are in the top 100 year-end rankings for any given year and the following year are coded ‘sticky.’ Using a one-tailed t-test, we then evaluate the significance of the ranking point changes for stickiness.

Next, we analyze the total number of points offered at the ATP Tour and Challenger levels from 2023 and 2024. We analyze the breakdown of potential ATP Tour and Challenger points offered. Using the point table and tournament schedule, we provide an estimate of these points. Exact point values will be unknown because the ATP Tour does not award points for players who advance through byes. Additionally, players often compete in more than 19 events, and points garnered in non-countable events are not considered in the final ATP Tour rankings.

Third, we then compare ATP Tour rankings with Elo ratings to identify where players have similar ratings but different rankings. Elo is a widely-accepted rating system in chess, tennis, and otherwise that assigns players a score based on their performance against opponents, adjusting their rating up or down depending on the match outcome and the relative strength of the opponents (Elo, 1978). Sackmann (2019) found that, in terms of predicting winners of tennis matches, “Elo trounced the official rankings [and] Elo is also considerably better over the course of the entire season.” The 2023 and 2024 year-end Elo ratings were obtained from Sackmann’s open-source repository. Importantly,

Elo ratings allow us to account for the quality of a win, which is not fully captured in the ATP Tour ranking system. Analyzing ATP Tour rankings vis-à-vis Elo ratings allow us to identify potential bottlenecks where rankings differ but player rating remains relatively similar.

Finally, we consider theories proposed by different professional tennis players in response to Sell’s social media post and determine whether players may have an advantage to play lower-level tournaments to increase their ranking. Hypothetical—and extreme—schedules and results with points coming from different levels of tournaments and the resulting rankings are outlined. Additionally, we provide examples of players who, counterintuitively, may benefit from playing lower-level ITF M25 and M15 tournaments (instead of Challengers) to increase their ATP Tour ranking.

The purpose of these analyses is not to definitively conclude whether a bottleneck exists around the top 100 ranking. This is a parsimonious, pilot study approach designed to reveal initial evidence, if any. We have not controlled for other rule changes and have not implemented any rigorous regression models. With this limited scope, we can only offer preliminary insights into whether a bottleneck may or may not exist. More robust analyses would need to account for additional factors, such as the 2018 rule change that increased the number of countable events from 18 to 19. With access to more extensive data, a full-blown longitudinal study could be conducted to evaluate the impact of ranking rule changes over time. Such an analysis could also be undertaken to investigate whether any ranking bottlenecks exist on the women’s WTA Tour.

III. Results and Discussion Our results provide prima facie evidence in support of the Top 100 ‘bottleneck’ hypothesis suggested by Sell and others. Table 1 presents the stickiness calculations, which indicate a notable increase in the number of players remaining in the top 100 from one year to the next following the 2024 rule change. The p-value from the one-tailed t-test (p = 0.01498) suggests greater stability in the top 100 rankings compared to previous years. In contrast, when the same method is applied to players ranked in the top 200, we find a decline in the stickiness of player rankings, suggesting greater volatility outside of the top 100 players.

Table 1

Top 100 Top 200

2011-2023* 2024 p-value

(Mean)

(Actual) (two-tailed)

72.83333 74

0.01498

152.0833 144

0.0002389

*2020 and 2021 removed p-value (right-tailed) 0.007491 0.9999

We then provide estimates of rankings points that are available in ATP Tour events and Challenger events in Table 2. As previously noted, these values are estimates, as the total points available are not equivalent to the total number of points that are eventually used in final ATP rankings. The data reveal a notable increase in total ATP Tour points, rising by approximately 9.35% after the 2024 rule change.

In contrast, Challenger points decreased by roughly 13.02%.

Table 2

ATP events Challengers

## 2023 Points 161,600 76,071

## 2024 Points 176,762 66,170

Raw Change 15,102 -9,901

% Change 9.3453% -13.015%

We then compare Elo ratings with ATP Tour rankings to test the idea that players just outside of the top 100 in the ATP rankings are of similar—or better—quality to players just inside the top 100. We provide scatterplots and densities of Elo ratings and ATP Tour rankings. Figures 2 and 4 show a scatterplot with a local regression line that helps to indicate where a bottleneck occurs. Any plateau of this line indicates where a potential bottleneck exists. There is some evidence that a slight plateau occurs just outside of the top 100 players in 2024. The density plots in Figure 1 and Figure 3 give the distribution of ATP Tour ranking based on Elo ratings. Two densities with large overlap show that quality overlaps, while the rankings differ. The peak of each density plot is the most common Elo rating for players in each given ranking group. Figure 1

Figure 2

Figure 3 Figure 4

We now consider hypothetical schedules of ATP Tour players, assuming they are not limited by time, other resources, or injuries. The first hypothetical player exclusively plays and wins ITF M25 tournaments and has 19 countable wins, with each awarding 25 point for a total of 475 points. By the end of 2024, this player achieves and ATP Tour ranking of #125. The same strategy in 2023 earns the player a year-end ranking of #136.

The next player only competes in and wins ITF M15 events and has 19 countable wins at the lowest level of ITF tournaments, awarding him 15 points for each event and 285 points for the year. This player ends 2024 with an ATP Tour ranking of #201. In 2023, the same strategy gives the player an ATP Tour ranking of #224.

We also consider a hypothetical player who exclusively competes at the Challenger 75 level and consistently reaches the quarterfinal round. In 2023, this player would have accumulated 304 ranking points for a year-end ranking of #201. However, in 2024, the same player only amasses 228 ranking points to achieve #250 in the year-end rankings. If this same player advances one round further, consistently reaching the semifinal round of each Challenger 75 event, he finishes 2023 with 570 ranking points and a world ranking of #117. In 2024, the same performance yields the player 418 ranking points and an ATP ranking of #143.

Finally, we examine a player who exclusively competes in ATP Tour events, with two potential scenarios to consider. In the first scenario, the player wins one round at each ATP Tour event and one round at each Grand Slam. In the second scenario, the player loses every first round in mandatory Grand Slam and Masters 1000 events but wins his first rounds at ATP 500 and ATP 250 events. Because points are still awarded for first round losses to players who receive direct entry into the main draw of Grand Slams and Masters 1000s, the second scenario still awards the player 120 ranking points for his losses. At the end of 2024, a player who wins first round matches at the best seven ATP Tour events and loses first round at the twelve mandatory events will be ranked #130 in the world having won only seven matches in a season. If the player wins the first round at each event, he will be ranked #64 in the world.

This four-pronged parsimonious analysis suggests that there is enough evidence of a ranking bottleneck to merit future research, with a focus on whether such a bottleneck is resulting from the rule change involving ATP Tour ranking point allocation or some other exogenous factor. Further, our analysis reveals that the recent changes to the ranking point allocation schedule could incentive players to strategically target lower-tier ITF events instead of Challenger tournaments organized by the aspirational ATP Tour. Indeed, semifinal finishes at Challenger 100 tournaments now earn the same amount of ranking points (25) as winning ITF M25 tournaments.

Our findings raise important policy considerations within the sport of tennis. If the bottleneck is indeed a result of the 2024 rule change, the result could have implications for the fairness, transparency, and accessibility of the sport. Tennis is foundationally built on meritocratic principles established at the formation of the ATP Tour in 1972 and the adoption of the computer rankings in 1975. These principles ensured that players are rewarded based solely on objective performance, not external factor subjective in nature. Any shift towards policies that favor higher-ranked players or policies that create barriers for emerging talent could undermine these foundational promotionrelegation values.

## IV. Conclusion

We conclude that there is evidence of a Top 100 bottleneck as suggested by Karue Sell. However, our methods do not control for the fact that this bottleneck may have existed before the 2024 ATP Tour point reallocation. Regardless, this research is timely and important as a new federal lawsuit brings the ATP Tour ranking system under the scrutiny of antitrust law. According to the 163-page court filing:

“[The ATP] further restricts players’ mobility through a draconian system of ‘Ranking Points,’ the anticompetitive currency used by [the ATP] to dictate which tournaments players can compete in, how much compensation they earn, and whether they receive certain sponsorship opportunities” (Pospisil et al. v. ATP Tour et al., 2025). Additionally, the 2024 ATP Tour point revisions remain as a topic of public discourse and informal speculation beyond the big-picture implications for promotion and relegation as tools of sport governance. Liam Broady, who was ranked as high as #93 in 2023, articulated his displeasure with the 2024 rule change over a year after its implementation: “21 players got 15 ATP points or more from [F]utures events last week, that’s more than a [C]hallenger QF and there were only 4 [C]hallengers. Who’s bright idea at the ATP was it to lower [C]hallenger points and not ITF points[?]” (Broady, 2025). Sell responded: “Not a lot of point playing [C]hallengers tbh if you are just trying to get to like 220 for [Grand S]lams. The [C]hallenger points are stupid now unless you take title” (Sell, 2025). Acknowledgements: The authors would like to thank Chase Cerejo and Daniel Berenblit for excellent research assistance. The authors would also like to thank the following individuals for invaluable feedback regarding this paper during weekly research sessions at Florida State University’s Multipurpose Educational Facility: Young Ho Shin, Richard Victor, Charlie Cowan, Nico Rebedello, Francisco Davila, Reid Kanemasu, Youcef Rihane, Shravan Kambahm, Ella Pogue, Alex Ionescu, Lillian Zhang, Rieke Gillar, Sebastian Roane, Bernardo Peralta, Alex Bulte, Gabriel Roane, and Vito Tonejc.

## REFERENCES

ATP (2024). The 2024 ATP official rulebook. https://www.itftennis.com/media/11553/2024rulebook-atp.pdf

Broady, L. [@Liambroady]. (2025, March 31). 21 players got 15 ATP points or more from futures events last week, that’s more than a challenger QF and [Post]. X. https://x.com/liambroady/status/1906593995582509506?s=46&t=JYfugU7GFQrN5DoE UBi-vQ

Devriesere, K., Csató, L., & Goossens, D. (2024). Tournament design: A review from an operational research perspective. European Journal of Operational Research. doi:10.1016/j.ejor.2024.10.044

Elo, A. (1978). The Raiting of Chessplayers: Past and Present. Ishi Press International

Jasina, J., Rotthoff, K. (2012). A model of promotion and relegation in league sports. Journal of Economics and Finance 36, 303–318 (2012). https://doi.org/10.1007/s12197-009-9120-4

Medcalfe, S. (2024). Behavioral responses to sporting contest design: A review of the literature. American Behavioral Scientist, 0(0). https://doi.org/10.1177/00027642241235814

Niland, C. (2024). The Racket: On tour with tennis’s golden generation—and the other 99%. Penguin Random House UK.

Noll, R. G. (2002). The economics of promotion and relegation in sports leagues: The case of English football.

Journal of

Sports

Economics,

3(2),

169–203. https://doi.org/10.1177/152700250200300205

Pospisil, et al. v. ATP Tour, et al., Complaint, Case 1:25-cv-02207, United State District Court—Southern District of New York (March 18, 2025)

Sackmann, J. (2019, December 3). An introduction to Tennis Elo – Heavy Topspin. https://www.tennisabstract.com/blog/2019/12/03/an-introduction-to-tennis-elo/

Sheets, C. (2024, October 30). An L.A. tennis star revived his pro career — as a YouTube influencer. Los Angeles Times. https://www.latimes.com/california/story/2024-10-30/former-ucla-starkarue-sell-rejoins-pro-tennis-tour-at-30-with-a-youtube-channel

Sell, K. [@KarueSell]. (2024, April 16). Thoughts after playing challengers again: Tennis is so deep, there’s so much talent. But the ATP once again has f***** [Post]. X. https://x.com/karuesell/status/1780435886489940104?s=46&t=JYfugU7GFQrN5DoEUB i-vQ

Sell, K. [@KarueSell]. (2024, April 16). Tennis is not a “top 100 sport anymore”. Guys 600 are beating 100

(twice this week alone).

Moving up and

[Post].

X. https://x.com/karuesell/status/1780436733659598863?s=46&t=JYfugU7GFQrN5DoEUB i-vQ

Sell, K. [@KarueSell]. (2024, November 14). I’ve had so many conversations with players/coaches this year regarding the drop in points in the challenger tour and [Post]. X. https://x.com/karuesell/status/1857100617988145164?s=46&t=JYfugU7GFQrN5DoEUB i-vQ

Sell, K. [@KarueSell]. (2024, November 14). I’m just not sure why this decision was made and we’ve had no transparency from the @atptour in the matter [Post]. X. https://x.com/karuesell/status/1857101841332613514?s=46&t=JYfugU7GFQrN5DoEUB i-vQ

Sell, K. [@KarueSell]. (2024, November 14). BTW, I complain not because of my situation. But I’m in a unique position where

I have some sort of

[Post].

X. https://x.com/karuesell/status/1857102248771301454?s=46&t=JYfugU7GFQrN5DoEUB i-vQ

Sell, K. [@KarueSell]. (2025, March 31). Not a lot of point playing challengers tbh if you are just trying to get to like for slams

[Post].

X. https://x.com/karuesell/status/1906722674564530448?s=46&t=JYfugU7GFQrN5DoEUB i-vQ

W

F

SF

2000 1200 720

2000 1300 800

% Change 0% 8% 11%

## Appendix A

Grand Slams

QF

R16

R32

11%

11%

11%

R64 R128 Q Q3 Q2

25 16

30 16

11% 0% 20% 0% 0%

ATP Masters 1000 (Draw of 96)

W

F

SF

QF

R16

R32 R64 R128 Q Q3 Q2

1000 600 360

-

1000 650 400

-

% Change 0% 8% 11% 11%

11%

11% 20% 0% 25% - 25%

ATP Masters 1000 (Draw of 56)

W

F

SF

QF

R16

R32 R64 R128 Q Q3 Q2

1000 600 360

-

-

1000 650 400

-

-

% Change 0% 8% 11%

11%

11%

11%

0%

-

20% -

0%

W

F

SF

500 300 180

500 330 200

% Change 0% 10% 11%

ATP 500 (Draw of 48)

QF

R16

R32

11%

11%

25%

R64 R128 Q Q3 Q2

-

-

-

-

-

-

-

-

60%

100%

W

F

SF

500 300 180

500 330 200

% Change 0% 10% 11%

ATP 500 (Draw of 32)

QF

R16

R32

-

-

11%

11%

25%

R64 R128 Q Q3 Q2

-

-

-

-

-

-

-

-

25%

30%

W

F

SF

250 150

250 165

% Change 0% 10% 11%

ATP 250 (Draw of 48)

QF

R16

R32

11%

25%

30%

R64 R128 Q Q3 Q2

-

-

-

-

-

-

-

-

60% - 33%

W

F

SF

250 150

250 165

% Change 0% 10% 11%

ATP 250 (Draw of 32)

QF

R16

R32

-

-

11%

25%

-

R64 R128 Q Q3 Q2

-

-

-

-

-

-

-

-

8% - 17%

Challenger 175

W

F

SF

QF

R16

R32

175 100

-

-

% Change 0% -10% -17% -22% -13%

-

R64 R128 Q Q3 Q2

-

-

-

-

-

-

-

-

0%

-

0%

W

% Change 0%

F 75 64 -15%

SF 45 35 -22%

Challenger 125

QF

R16

R32

-

-

-36% -27%

-

R64 R128

-

-

-

-

-

-

Q Q3 Q2

-

-

0% - 50%

W

% Change 0%

F 60 50 -17%

SF 36 25 -31%

Challenger 100

QF

R16

R32

-

-

-30% -22%

-

R64 R128 Q Q3 Q2

-

-

-

-

-

-

-

-

-20% - 50%

Challenger 75

W

F

SF

QF

R16

R32 R64 R128 Q Q3 Q2

-

-

-

-

-

-

-

-

% Change 0% -12% -27% -25% -14%

-

-

-

0% -

0%

Challenger 50

W

F

SF

QF

R16

R32 R64 R128 Q Q3 Q2

-

-

-

-

-

-

-

-

% Change 0% -17% -18% -11%

0%

-

-

-

0% -

0%

W

F

SF

% Change 0% 0% 0%

ITF M25

QF

R16

R32

-

-

0%

0%

-

R64 R128 Q

-

-

-

-

-

-

-

-

-

Q3 Q2

-

-

-

-

-

-

W

F

SF

% Change 0% 0% 0%

ITF M15

QF

R16

R32

-

-

0%

0%

-

R64 R128 Q

-

-

-

-

-

-

-

-

-

Q3 Q2

-

-

-

-

-

-
