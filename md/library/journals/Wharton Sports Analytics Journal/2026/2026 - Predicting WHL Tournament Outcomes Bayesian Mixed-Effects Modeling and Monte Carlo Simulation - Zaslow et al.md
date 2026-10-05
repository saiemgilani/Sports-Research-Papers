<!-- source: library/journals/Wharton Sports Analytics Journal/2026/2026 - Predicting WHL Tournament Outcomes Bayesian Mixed-Effects Modeling and Monte Carlo Simulation - Zaslow et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/predicting-whl-tournament-outcomes-bayesian-mixed-effects-modeling-monte-carlo-simulation/ -->
<!-- authors: Zach Zaslow; Lucas Greenwald; Max Li; Riley Wong; Aaron Wu -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

2026, Fall https://wsb.wharton.upenn.edu/wharton-sports-analytics-journal/

Predicting Hockey Game Outcomes Through Bayesian Mixed-Effects Modeling & Monte Carlo Simulation

Zach Zaslow, ’27

The Pingry School, NJ, USA

Advisor: Bradford Poprik The Pingry School, NJ, USA

2026 Wharton High School Data Science Competition 1st Place Team

## Abstract

Traditional hockey stats such as win-loss record and raw goal differential fail to account for opponent strength, shot quality, and game state context, leading to systematically flawed team evaluations and rankings. We developed an analytical pipeline that used Bayesian mixed-effects modeling and Monte Carlo simulation to identify true team strength and predict tournament outcomes for the World Hockey League. In stage one of our model, we fit a Bayesian mixed-effects model on log expected goals per minute with team and opponent random effects estimated separately for even-strength, power-play, and penalty-kill phases and home/away settings. These estimates were back-transformed and converted into true expected goal differential per 60 for each phase, weighted by the distribution of each team’s actual ice time in each phase and converted to composite zscores.

We also studied how offensive line disparity impacts team performance by isolating the first offensive line's and second offensive line’s performances and creating a ratio. In stage two, we generated win probabilities for each of the first-round tournament matchups. We used individual team penalty data to estimate the time spent in each phase, and then used the geometric mean of offense and defense to estimate scoring rates in each phase. This data was then run through 30,000 Monte Carlo simulations per matchup to produce our win probabilities. The model substantially reorders the standings: Mexico rises from 19th in points to 4th in true strength, while the Netherlands drops from 2nd to 7th. Offensive line disparity showed no relationship with team strength (r ≈ 0, p = 0.955), suggesting top-heavy offenses are not a competitive disadvantage. key words: hockey; win probability; xG; Monte Carlo simulation; Bayesian

Wharton Sports Analytics Journal

## Introduction & Background

For most of hockey’s history, team evaluation has relied largely on base-level statistics like raw goal differential, win-loss record, and plus/minus. However, these metrics fail to capture the whole story as they share a fundamental flaw: they treat every goal equally, regardless of how it was generated, and ignore the strength of the opponents a team faced to accumulate them. A team can score 3 goals on low-danger shots or 3 goals from point-blank range, and goal differential would view them the same. Which is more sustainable? Using traditional stats, 10-5 vs. weak opponents looks better than 9-6 vs. elite ones, but in reality, the 9-6 team is probably stronger. Without opponent adjustment, rankings are systematically misleading. Traditional metrics don’t account for underlying distinctions and have historically driven decisions in player evaluation, awards (the NHL once gave out an annual award for the highest plus-minus), and tournament seeding (Barry, 2024).

The development of expected goals (xG) in the early 2010s addressed the first part of this problem. Building on early work by Ryder (2004), Macdonald (2012) introduced the modern xG framework at the MIT Sloan Sports Analytics Conference, weighting each shot by its true probability of becoming a goal based on its location, type, and game context. Since then, public xG models from Evolving Hockey (2021), MoneyPuck (2026), and others have made shot-qualityadjusted analytics standard in hockey research. xG consistently outperforms raw goal totals as a predictor of future team performance because it captures the underlying process generating goals rather than the noisy outcomes themselves.

While xG addressed shot quality, opponent strength remained a separate issue. A team could rack up high xG against weak defenses without that translating into elite performance against tougher competition. Whole-history rating systems and opponent-adjusted ratings have been used in other sports. For example, (Seung et al., 2024) applied a whole-history rating approach to soccer for last year's Wharton High School Data Science Competition, but these methods typically treat each game as a single observation rather than separating the fundamentally different scoring environments that exist within a hockey game.

Hockey is really played as three games within one. Even-strength play, the power play, and the penalty kill have completely different scoring rates, personnel deployments, and tactical structures. A team that thrives at 5-on-5 might be mediocre on the power play, and vice versa. Collapsing these into a single team-level metric hides which teams are genuinely elite and which are propped up by one strong phase. It also opens the door to Simpson's Paradox, where aggregate numbers can disguise opposite trends within subgroups.

Our work extends the xG framework along two axes simultaneously. First, we used Bayesian mixed-effects modeling to adjust every team's expected goals rate for the specific opponents and venues they faced, with partial pooling stabilizing estimates for teams with limited high-quality matchups. Second, we estimated separate models for even-strength, power-play, and penalty-kill phases, then recombined them using each team's actual time-on-ice distribution. The result was a single composite strength metric that respects both opponent context and game-state structure. We then fed those phase-specific rates into Monte Carlo simulations to generate win probabilities for the WHL's first-round tournament matchups and used the same framework to quantify whether offensive line balance correlates with overall team strength.

## 2 Zaslow

Wharton Sports Analytics Journal

## Methods

The Wharton High School Data Science Competition provided one full season of game-level event data covering 32 teams and 1,312 games from the fictitious World Hockey League (WHL). Each team played exactly 82 games (41 home, 41 away). The raw data was structured at the event level, with each row containing time-on-ice, offensive and defensive line tags (O1/O2 and D1/D2), shot location and type, expected goals values, penalty events, and home/away designations. The data is entirely simulated by the competition organizers, and the underlying simulation was created at the individual player-shift level, with the data set provided being the rolled-up shift game level. The simulation was similar to NHL hockey, but with a wider range of team quality. In a simplification from NHL hockey, in the simulation, teams and players remain constant throughout the season with no injuries, trades, or performance fluctuations.

First, we converted time-on-ice from seconds to minutes and removed all empty-net events, as shots taken with the goalie pulled distort scoring rates and are not representative of true team strength. We then aggregated row-level events into game-level totals, reshaping the data so each game produced one row per team with the opponent, home/away status, goals, shots, expected goals, and penalties. To capture game-state dynamics, we bucketed every event into even-strength, power-play, or penalty-kill splits based on the offensive and defensive line tags. We then created home/away indicators, opponent identifiers, even-strength unit labels (O1/O2 and D1/D2), per-minute and per-60 xG rates, time-on-ice shares for each phase, and O1/O2 disparity ratios. The disparity ratio was constructed by averaging O1 performance across both defensive pairings ((O1/D1 xG/60 + O1/D2 xG/60)/2) and doing the same for O2, then taking the ratio of the two. This isolates offensive line performance from defensive pairing effects.

We used R for all data cleaning, modeling, and simulation, primarily with the brms package for Bayesian regression, tidyverse for data manipulation, and glmnet for supporting analysis. We also used ChatGPT and Claude during development for code writing and debugging, model refinement, and concept clarification. The two AI tools were used to check each other's work, but all final modeling decisions and result interpretations were made by us.

Our pipeline has two stages. In stage one, we fit Bayesian mixed-effects models on log expected goals per minute, with team and opponent as random effects. We modeled this separately for each phase (EV, PP, PK) and each venue (home, away), producing twelve models total. Modeling on the log scale keeps all back-transformed predictions positive and makes team strength act multiplicatively on the rate rather than as a flat offset, which better matches the structure of scoring data. We used exponential priors on variance components to regularize estimates and ran four chains of 6,000 iterations each with adapt_delta = 0.95 to ensure stable sampling. The Bayesian framework's partial pooling was especially important for teams with fewer high-quality opponents or minutes spent in a specific phase, because it pulls those estimates toward the league mean instead of overstating small samples. We backtransformed the posterior means to expected goal differential per 60 minutes for each phase, weighted each phase by the team's actual share of ice time in that phase, and computed home and away weighted totals separately. Each was z-scored against the league to normalize venue baselines, then averaged to produce a single composite z-score per team.

## 3 Zaslow

Wharton Sports Analytics Journal

In stage two, we generated win probabilities for the 16 first-round matchups. We projected phase minutes for each team using their observed penalty draw and take rates, then computed phase-specific scoring rates as the geometric mean of the offensive team's xG-for rate and the defensive team's xG-against rate: 𝜆 = $𝑡𝑒𝑎𝑚_𝑥𝐺_𝑓𝑜𝑟 ∗ 𝑜𝑝𝑝_𝑥𝐺_𝑎𝑔𝑎𝑖𝑛𝑠𝑡 . Goals were drawn from a Poisson distribution with λ as the mean, which fits because goals in a phase are rare, discrete, independent events. Tied games went to sudden-death overtime, repeating until resolved. We ran 30,000 simulations per matchup, which yielded a standard error below 0.3%, tight enough to distinguish close games. We checked R-hat values and effective sample sizes to confirm the Bayesian models converged and sampled stably. We sanity-checked that posterior-mean xG rates aligned with league averages. For the simulations, we verified consistency by confirming that stronger teams generated higher xG and higher win probabilities across repeated matchups.

Results Opponent adjustment and use of xG reorder the standings Our composite z-score reranks the league in ways raw standings miss. Figure 1 shows the top ten teams by composite strength. Brazil leads at 1.844, meaning it sits more than 1.8 standard deviations above the league average, with Thailand close behind at 1.603. The more interesting movement happens in the middle of the table. Mexico finished 19th in traditional points but rose to 4th in true strength (z = 0.967), while the Netherlands fell from 2nd in points to 7th (z = 0.798). These are not small corrections, as Mexico's jump reflects a difficult schedule as well as bad luck that hurt its record without reflecting its underlying play, and the Netherlands' drop reflects the opposite, a softer slate and good luck that inflated its raw results. This is exactly the situation we set out to correct. Without accounting for opponent strength and beneath the surface data, the standings reward teams for unsustainable factors.

Figure 1. Top 10 teams ranked by composite xG z-score, combining opponent-adjusted expected goal differential per 60 across even-strength, power-play, and penalty-kill phases, weighted by each team's actual ice-time distribution.

## 4 Zaslow

Wharton Sports Analytics Journal

Win probabilities and home ice Feeding the phase-specific rates into 30,000 Monte Carlo simulations per matchup produced win probabilities for all 16 first-round games, with Monte Carlo standard error under 0.3%. The spread tracks team strength as expected. Brazil over Kazakhstan was the most lopsided at 67.6%, consistent with Brazil being the clear top team facing a weak opponent. The closest games clustered near a coin flip, including Singapore over New Zealand at 50.6% and Mexico edging the UK at 50.3%. Every home team was favored in our simulations. Part of this is structural, since higher seeds host games, but part is a venue effect, as across the league, moving from away to home swings the expected goal differential by an average of 0.64 per 60. That is a meaningful edge, and it is large enough to flip otherwise even matchups.

Figure 2. Home-team win probabilities for the seven most lopsided first-round matchups, each estimated from 30,000 Monte Carlo simulations with penalty-projected phase minutes and sudden-death overtime resolution. Home team listed first.

Offensive line balance does not predict strength We isolated each team's first and second offensive lines to test whether top-heavy offenses are a competitive liability. Figure 3 shows the ten most top-heavy teams by O1/O2 disparity ratio. Guatemala is the extreme case at 2.014, meaning its first line generates roughly twice the expected goals per 60 as its second. We then plotted disparity against composite strength (Figure 4) to see whether balance matters. It does not. The correlation is essentially zero (r ≈ 0, p = 0.955), and the scatter shows strong and weak teams distributed across the full range of line balance. A top-heavy team is no more or less likely to be elite than a balanced one. The practical takeaway for a league office is that offensive line balance should not be used as a team evaluation metric, as it carries no signal about overall quality.

## 5 Zaslow

Wharton Sports Analytics Journal

Figure 3. Top 10 teams by O1/O2 disparity ratio, computed as the average opponent-adjusted xG/60 of the first offensive line divided by that of the second, isolated from defensive pairing effects.

Figure 4. Composite strength z-score plotted against O1/O2 disparity ratio for all 32 teams. Quadrant labels distinguish balanced versus top-heavy and strong versus weak. The flat relationship (r ≈ 0, p = 0.955) shows line balance carries no information about team strength.

## 6 Zaslow

Wharton Sports Analytics Journal

## Conclusions

We set out to identify true team strength more accurately than traditional standings, and the model accomplishes that. By adjusting expected goals for both opponent quality and venue, then modeling even-strength, power-play, and penalty-kill phases separately before recombining them by actual ice time, we produce rankings that correct the distortions raw points create. Mexico rising from 19th to 4th and the Netherlands falling from 2nd to 7th are the clearest evidence that the standings reward schedule luck as much as quality. We also showed that offensive line balance, despite its intuitive appeal, carries no signal about overall strength (r ≈ 0, p = 0.955), a useful null result for any league office tempted to use it as an evaluation metric.

The data is fully simulated by the competition organizers and modeling team strength this way is still challenging, so performing these methods on real hockey, where rosters and tactics shift across a season, would be an even harder task. Within that difficulty, we found no suitable way to incorporate goaltending efficiency, so we omitted it entirely, despite the clear role it plays in real outcomes.

## Acknowledgments

Thank you to Mr. Bradford Poprik and The Pingry School for supporting this work, and the Wharton High School Data Science Competition organizers for providing the dataset and the opportunity. We also acknowledge the use of ChatGPT and Claude during development for code writing and debugging, model refinement, and concept clarification, but all final modeling decisions and result interpretations were our own.

## References

● Seung, E., Xu, J., Katz, R., Wetzstein, M., & Barr, M. (2024). Calculating Win Probabilities of Any Matchup of Soccer Teams: A Whole-History Rating Approach for the Wharton High School Data Science Competition, Wharton Sports Analytics Journal.

● Macdonald, B. (2012). An expected goals model for evaluating NHL teams and players. Proceedings of the 2012 MIT Sloan Sports Analytics Conference. http://hockeyanalytics.com/Research_files/NHL-Expected-Goals-Brian-Macdonald.pdf

● Ryder, A. (2004). Shot quality. Hockey Analytics. http://hockeyanalytics.com/Research_files/Shot_Quality.pdf

● Barry, S. (2024). Winners of NHL awards that faded into history. The Hockey News. https://thehockeynews.com/news/news/winners-of-nhl-awards-that-faded-into-history

● Evolving Hockey. (2021). A New Expected Goals Model for Predicting Goals in the NHL. https://evolving-hockey.com/blog/a-new-expected-goals-model-for-predicting-goals-inthe-nhl/

● MoneyPuck. MoneyPuck.com: NHL analytics, playoff odds, power rankings, player stats. Retrieved Mar 2026, from https://moneypuck.com/

## 7 Zaslow
