<!-- source: library/preprints/arXiv/2026/2026 - A market-initialised accelerated failure time model for in-play football forecasting - Clegg et al.pdf -->
<!-- item: https://arxiv.org/abs/2605.16066 -->
<!-- authors: Lawrence Clegg, Zixing Song, John Cartlidge -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-18; equations, tables and figures are NOT preserved - consult the PDF for those -->

# A market-initialised accelerated failure time model for in-play football forecasting

                                            A market-initialised accelerated failure time model for
                                                                            in-play football forecasting

                                                                      Lawrence Clegg* , Zixing Song , John Cartlidge
                                                              School of Engineering Mathematics and Technology, University of Bristol, UK

                                                                  {lawrence.clegg, zixing.song, john.cartlidge}@bristol.ac.uk
                                                                                               *
                                                                                                   Corresponding author
arXiv:2605.16066v2 [stat.AP] 11 Nov 2026




                                                 Abstract—In-play football forecasting models are rarely compared with betting exchange prices, which aggregate

                                                 information from many market participants. We make this comparison for several goal-arrival models, focusing

                                                 on a Weibull accelerated failure time model with two extensions: initialising team strength parameters from

                                                 Betfair Exchange prices at kick-off to capture pre-match market information, and including cumulative shots as

                                                 a time-varying covariate to capture in-play information. The initialisation, which fits team-strength parameters

                                                 to 1X2 and over/under prices by squared-error minimisation, applies to any intensity-based goal arrival model.

                                                 Evaluated across 280 English Premier League matches at minute intervals, the market-initialised model remains

                                                 measurably weaker than Betfair in-play prices (classification accuracy 68.5% versus 69.5%, ranked probability score

                                                 0.1325 versus 0.1281), but retains interpretable team-level parameters and covariate effects. A comparison with a

                                                 market-implied Poisson model, a Cox process and a Bayesian birth process, all initialised from the same pre-match

                                                 odds, confirms that market initialisation is the dominant driver of predictive accuracy. A betting simulation against

                                                 Betfair in-play odds yields a 1.0% return on investment over 37,467 bets (95% interval −3.8% to 5.9%), which we

                                                 regard as preliminary given the limited sample of matches and prices that may not have been executable.


                                                 Keywords: betting markets; market calibration; goal arrival models; soccer; survival analysis; Weibull distribution




                                           1 Introduction

                                           The prediction of association football match outcomes attracts considerable interest from the sports analytics

                                           and betting communities. In-play betting, where bettors use observed match events to update their forecasts

                                           during a match, now commands around 60% of the sports betting market.1 Betting exchanges such as Betfair

                                           Exchange (and prediction markets) have substantial in-play liquidity for elite-level football matches, with some

                                           bettors placing thousands of bets per match as they react to match events and market dynamics. Live data feeds

                                           from providers such as Stats Perform—whose Opta brand collects over 1 billion unique data points annually across


                                           1 https://www.mordorintelligence.com/industry-reports/online-sports-betting-market

                                           Preprint: Clegg, Song and Cartlidge (2026)                                                                          Page 1 of 27
In-play football forecasting                                                   Preprint: Clegg, Song and Cartlidge (2026)


more than 20 sports and 3,900 competitions2 —enable fully automated betting strategies in these markets. While

association football is the most widely played and watched sport globally, forecasting match outcomes in-play

presents clear challenges: the sport is inherently low-scoring, with around three goals per match on average, and

matches can result in draws, creating a three-way outcome classification problem.

    Pre-match forecasting has a long history, from early Poisson models (Maher, 1982) to bivariate extensions

(Boshnakov et al., 2017; Dixon and Coles, 1997; Karlis and Ntzoufras, 2003) and machine learning approaches

(Bunker et al., 2024). However, these methods do not address in-play updating. In higher-scoring sports, within-

match updating is more straightforward: tennis models update win probabilities point-by-point (Klaassen and

Magnus, 2003; Kovalchik and Reid, 2019) and basketball models simulate possession-by-possession (Štrumbelj and

Vračar, 2012). In football, goals are sufficiently rare that models must extract signal from non-scoring events to

update forecasts meaningfully between goals.

    A growing body of in-play work addresses this challenge. Robberechts et al. (2021) model scoring intensity

as a Poisson process conditioned on many match-event covariates, including expected threat, attacking passes,

and duel success rates. Their pre-match baseline, however, rests on a single Elo rating differential, which captures

relative strength but offers no team-specific attack or defence decomposition: two fixtures with the same Elo gap

are assigned identical pre-match expected goals, regardless of the teams’ scoring rates. Other notable point-process

approaches (Dixon and Robinson, 1998; Maia et al., 2026; Volf, 2009; Zou et al., 2020) model arrivals directly, but

condition on score state, red cards, and time effects alone, drawing little signal from shot-level or event-derived

data between goals.

    Leriou and Ntzoufras (2025) model goal inter-arrival times directly, via a Weibull accelerated failure time

model. The usage of an accelerated failure time model comes from survival analysis, where covariates accelerate or

decelerate the waiting time to the event (goal). A gap-time formulation provides a natural basis for simulating

match progressions. Their model achieves precise in-sample league reconstruction and its structure admits a

straightforward extension to in-play covariates, which they leave as future work.

    A further limitation shared by the above models is their inferior pre-match forecasting compared with betting

markets, which have been consistently shown to be the best forecasters before kick-off (Hvattum and Arntzen,

2010; Maia et al., 2026; Wunderlich, 2025). This likely constrains the in-play performance of these models from the

outset, although in-play models have rarely been compared with in-play odds. For instance, both Zou et al. (2020)

and Titman et al. (2015) bet against live market prices, but neither compares forecast accuracy to the market.


2 https://www.statsperform.com/resource/opta-by-stats-perform-global-leader-ai-sports-data-analytics/

                                                     Page 2 of 27
In-play football forecasting                                                   Preprint: Clegg, Song and Cartlidge (2026)


    Betting odds can be incorporated into goal models to close this gap. Titman et al. (2015) replace team attack

and defence parameters with covariates derived from pre-match bookmaker odds, which informs scoring rates

but leaves no team-level parameters to interpret. Goal intensities have also been fitted to market prices by least

squares, but to value bets rather than to forecast outcomes (Divos, 2020; Jottreau, 2009). With forecasting as

the aim, Egidi et al. (2018) combine odds-implied and historical Poisson scoring rates with a per-match convex

combination, achieving accuracy close to bookmaker odds and positive expected returns in the top four European

leagues. However, the model forecasts only final scores, with no in-play updating.

    Two limitations motivate the work we present. First, the Weibull gap-time framework of Leriou and Ntzoufras

(2025) has not been applied in-play, despite the authors explicitly proposing this as future work and the structure

admitting in-play covariates by design. Second, pre-match baselines estimated from historical data alone are

substantially less accurate than market prices, yet no in-play forecasting model fits its team-strength parameters

directly to them.

    We address both limitations by extending the Weibull accelerated failure time model with in-play covariates

and pre-match market initialisation. We incorporate cumulative shots as a time-varying covariate, capturing

attacking volume beyond what the score alone reflects. Rather than estimating team strength independently of the

market, we initialise the model’s scoring-rate parameters from Betfair Exchange prices at kick-off and use the

model’s structure for in-play updating. Although this step resembles model calibration in finance, where model

parameters are fitted to observed prices, we call it market initialisation to distinguish it from probability calibration

(the agreement between forecast probabilities and observed frequencies).

    We evaluate all models against Betfair Exchange in-play prices across 280 matches from gameweek 11 onwards

of the 2024/25 season, using log-loss, Ranked Probability Score, and classification accuracy at minute intervals.

We compare the Weibull model against the Bayesian birth process of Zou et al. (2020), the Cox process of

Maia et al. (2026), and three market-implied benchmarks. The market-initialised Weibull and Maia models are

indistinguishable from a Poisson benchmark fitted to the same prices, while the Zou model lags, which indicates

that initialisation is the dominant driver of forecasting performance. Market initialisation raises accuracy from

67.7% to 68.5%, against 69.5% for Betfair, while the Weibull model retains interpretable team-level parameters

and covariate effects. A betting simulation with the market-initialised Weibull model against Betfair in-play odds

yields 1.0% ROI with Kelly staking over 37,467 bets, which we regard as preliminary.




                                                      Page 3 of 27
In-play football forecasting                                                Preprint: Clegg, Song and Cartlidge (2026)


1.1 Related work

Considering pre-match forecasting, Maher (1982) demonstrated that a Poisson regression model with team-specific

attack and defence parameters could adequately describe match scores, establishing a framework for subsequent

forecasting models. Notable extensions to this framework include incorporating time-varying team strengths

with a low-score dependence correction (Dixon and Coles, 1997), using a bivariate Poisson model with diagonal

inflation to better capture draws (Karlis and Ntzoufras, 2003), and implementing a Weibull count process with

copula-induced dependence (Boshnakov et al., 2017). Player data has been used to forecast match outcomes, with

Holmes and McHale (2024) introducing a Skellam regression approach that uses player ratings with positional

interactions. Machine learning methods have also been applied to predict outcomes, with gradient-boosted tree

models demonstrating competitive performance (Bunker et al., 2024).

    Scoring rates are known to rise through the course of a match (Ayana et al., 2025), and trailing teams have

an elevated scoring rate in the second half (Silva and Swartz, 2016). Dixon and Robinson (1998) first introduced

a bivariate non-homogeneous Poisson birth process in which home and away goal rates depend on the current

scoreline. Volf (2009) extended this to a semi-parametric Cox model with a non-parametric baseline intensity for

each team, estimated directly from observed goal times, allowing scoring rates to vary freely over match time

rather than following a parametric trend. Titman et al. (2015) took a different approach and jointly modelled

goals and bookings as an eight-dimensional counting process under Weibull proportional hazards, finding that red

cards sharply alter scoring rates but yellow cards do not, and that home scoring rates fall once the home team

leads. Each of these models accounts for the evolving match state, yet assumes team-ability parameters remain

fixed throughout.

    Building on the birth process framework of Dixon and Robinson (1998), Zou et al. (2020) update team scoring

intensities in-play via conjugate Gamma posteriors as goals are observed, without consideration of the information

contained in shots, cards, and other match events that might foreshadow goals.

    Robberechts et al. (2021) address this limitation by treating scoring intensity as a temporal stochastic process

with regression weights that evolve throughout the match. Beyond score and time, they incorporate expected

threat (Singh, 2019), attacking passes, duel success rates, and cards, enabling win probability to respond to shifts

in momentum before goals are scored. However, their use of Elo ratings as the pre-match baseline captures only

relative team strength, precluding the matchup-specific attack–defence decomposition needed for informative

scoreline forecasts.



                                                   Page 4 of 27
In-play football forecasting                                                   Preprint: Clegg, Song and Cartlidge (2026)


    Following the shift towards greater use of in-play covariates, Klemp et al. (2021) evaluated the incremental

value of 18 performance indicators—including shots, passes, space control, and running distance—for match

outcome prediction. Using an ordered logistic regression to forecast second-half results, they found that first-half

goals added no significant predictive value for second-half outcomes once pre-match bookmaker odds were included.

    More recently, Maia et al. (2026) treat goal arrivals as Cox processes with dynamic regressors for score

differential, red-card difference, a half-time indicator, and the log-ratio of pre-match market values. They find that

a team’s scoring intensity drops by over 30% upon receiving a red card, and trailing teams exhibit 10–20% higher

intensity. Although they provide a general structure for incorporating in-play covariates into goal intensity models,

they do not consider shot-based covariates.




2 Data and evaluation

We collect data from several sources for the four English Premier League seasons 2021/22–2024/25 inclusive.

WhoScored.com records a variety of timestamped match events, from which we extract goal arrival times, red card

events, and injury time added. For shot-level detail, we use FBref.com, which records every shot together with its

expected goals (xG) and post-shot expected goals (PSxG) values.

    Betfair Exchange freely provides minute-by-minute historical data for football markets, recording the last

traded price for each outcome. Betfair suspends in-play markets after goals, penalties and red cards, clearing

the order book (Croxson and Reade, 2014), so trades just before or after a suspension, or late in matches when

liquidity is thin, can record unrepresentative prices. We treat prices that are at least 0.05 in implied probability

away from both neighbouring minutes this way, and replace 110 such prices in 2024/25 with the preceding price.3

    Of the 1,520 scheduled fixtures, four with missing or incomplete data are excluded. The remaining 1,516 are

split at gameweek 11 of the 2024/25 season, with the 1,236 earlier matches used for training and the 280 from

gameweek 11 onwards for evaluation. We start at gameweek 11 so that every club, including the promoted sides,

has at least ten league matches in the season. We cross-checked that all but three of the 39,590 shots are noted at

the same minute in both the FBref and the WhoScored data. For the three disputed shots, we use the FBref time.

Appendix A lists all consistency checks.




3 Lower cutoffs than 0.05 worsen Betfair’s RPS, suggesting they remove genuine price movements.

                                                      Page 5 of 27
In-play football forecasting                                                 Preprint: Clegg, Song and Cartlidge (2026)


2.1 Evaluation metrics

We evaluate each model’s performance using three complementary metrics over the predicted probability distribution

p = (𝑝𝐻 , 𝑝𝐷 , 𝑝𝐴 ). The Ranked Probability Score (RPS) measures the accuracy of cumulative probability forecasts

(Epstein, 1969):
                                                    ⎛              ⎞2
                                                  2   𝑖       𝑖
                                               1 ∑︁ ⎝∑︁      ∑︁
                                         RPS =          𝑝𝑗 −    𝑎𝑗 ⎠ ,                                             (1)
                                               2
                                                   𝑖=1   𝑗=1        𝑗=1


where outcomes are ordered as home win, draw, away win, and 𝑎𝑗 = 1 if outcome 𝑗 occurred, 0 otherwise. RPS

is standard in football forecasting (see Constantinou and Fenton, 2012) because it penalises predictions further

from the true outcome more heavily than those nearby. However, Wheatcroft (2021) argues this “sensitivity to

distance” provides no practical benefit, finding that log-loss identifies superior forecasters more efficiently. Hence,

we also report log-loss, − log 𝑝𝑦 where 𝑦 ∈ {𝐻, 𝐷, 𝐴} denotes the realised outcome. Unlike RPS, log-loss considers

only the probability assigned to the outcome and penalises confident incorrect predictions severely. We also report

classification accuracy, though this discards probabilistic information.

    We evaluate forecasts at every minute throughout each match, from minute 0 (pre-match) to the final whistle

as determined by the last recorded event. We report aggregate metrics across all evaluation points; we also plot

log-loss by minute, revealing how forecast accuracy evolves as match information accumulates and match-time

remaining decreases. Since minutes within a match are correlated, we report match-clustered confidence intervals

from a bootstrap that resamples whole matches with replacement (10,000 resamples).




3 A Weibull model for in-play prediction



3.1 Accelerated failure time model

Leriou and Ntzoufras (2025) introduce a Weibull accelerated failure time (AFT) model (Kalbfleisch and Prentice,

2011) for goal inter-arrival times using match data from the English Premier League 2018/19 season. Rather than

addressing “How many goals will a team score?”, they use the time between successive goals to answer “When will




                                                     Page 6 of 27
In-play football forecasting                                                    Preprint: Clegg, Song and Cartlidge (2026)


a goal be scored?” such that in a match between home team 𝐻 and away team 𝐴, goal arrival times follow:


                                                 𝑇𝐻 ∼ Weibull(𝛾, 𝜆𝐻 ),                                                (2)

                                                 𝑇𝐴 ∼ Weibull(𝛾, 𝜆𝐴 ).                                                (3)


For 𝛾 > 1, the conditional scoring hazard increases with time since the last goal. Leriou and Ntzoufras (2025)

estimate 𝛾 = 1.13 with a 95% posterior interval of [1.078, 1.186]. They also fit a model with a score-state-dependent

shape parameter, 0.94 for the leading team, 1.04 when tied and 1.73 for the trailing team, which achieved a superior

fit as measured by the Deviance Information Criterion (DIC = 10,870 vs. 11,010).

    We could not replicate this score-state pattern.4 Labelling each interval by the score that was held during it,

we obtain shape parameters of 1.18, 1.17 and 1.15 for the leading, tied and trailing team. Labelling each interval

instead by the score after the goal that ends it reproduces the pattern (0.94, 1.10 and 1.86) in the original study,

but this label is set by the very goal whose timing is being modelled. To test whether the labelling alone creates

the pattern, we simulated the 1,236 training fixtures from our fitted single-shape model, in which scoring does

not depend on the score. Labels by the score after the goal again give 0.95, 1.07 and 1.84, while labels by the

score during the interval give no effect (1.16, 1.21 and 1.14). The score-state effect of Leriou and Ntzoufras (2025)

therefore appears to arise from labelling intervals by their outcome, and with intervals labelled by the score during

them, a score-state shape fits worse than a single shape (ΔBIC = 16.1). A separate shape for each half is also not

preferred by BIC (ΔBIC = 2.0).

    Heuer and Rubner (2012) examine the same questions in over four decades of Bundesliga matches. They find

that the conceding team’s scoring rate dips by about 10% after a goal and recovers within roughly ten minutes.

Our shape of 1.17 implies a larger dip for both teams, with the hazard over the ten minutes after a goal averaging

29% below its level at thirty minutes. They also find that the score has little effect on which team scores next,

which supports a single shape over separate shapes for the leading, tied and trailing team.

    To determine 𝜆𝐻 and 𝜆𝐴 , the “standard vanilla formulation” of Karlis and Ntzoufras (2003) is used:


                                          log E[𝑇𝐻 ] = 𝜇 + 𝛽home + 𝑎𝐻 + 𝑑𝐴 ,                                          (4)

                                          log E[𝑇𝐴 ] = 𝜇 + 𝑎𝐴 + 𝑑𝐻 ,                                                  (5)




4 This is the only discrepancy we found. The intercept, home advantage and common shape of Leriou and Ntzoufras (2025) all
replicate closely on our data, as reported at the end of this section.

                                                      Page 7 of 27
In-play football forecasting                                                Preprint: Clegg, Song and Cartlidge (2026)


where 𝜇 is the intercept, 𝛽home captures home advantage, and each team 𝑘 has attacking ability 𝑎𝑘 and defensive

ability 𝑑𝑘 . Lower attacking parameters indicate a stronger attack (shorter expected time to score); higher defensive

parameters indicate a stronger defence (longer expected time for opponent to score). For identifiability, sum-to-zero
                          ∑︀       ∑︀
constraints are imposed: 𝑘 𝑎𝑘 = 𝑘 𝑑𝑘 = 0.

    For the half-time interval, Leriou and Ntzoufras (2025) found that treating time as continuous rather than

censoring and resetting at the 45th minute yielded a better fit (DIC 11,010 vs. 11,070). They also investigated

dependence between goal arrival times using a Marshall–Olkin bivariate Weibull distribution and random effects

models, but found no improvement over the independent Weibull model.

    We estimate all parameters by maximum likelihood on the observed goal times, right-censored at the final

whistle, in contrast to the Bayesian approach of Leriou and Ntzoufras (2025), and use BIC for model comparison.

We fit this model on 1,236 in-sample matches from four EPL seasons (2021/22–2024/25). The intercept 𝜇 = 4.21

closely matches Leriou and Ntzoufras’s estimate of 4.03, we obtain 𝛽home = −0.18 compared to their −0.19, and the

common shape is 𝛾 = 1.17 (SE 0.015) against their 1.13. We now describe our adaptations for in-play prediction.




3.2 In-play simulation

We generate in-play forecasts by Monte Carlo simulation: at each prediction point, we sample 10,000 match

completions from the current minute to full time, conditioning on the observed score and elapsed time. Outcome

probabilities are obtained from the proportions of home wins, draws, and away wins across simulations. We

also apply several adaptations to the base model: time-decaying team strengths that evolve across gameweeks, a

conditional sampling mechanism for the Weibull distribution, and in-play covariates that update the scoring rate

as events occur.




3.3 Time decay

The performance of a football team notoriously varies throughout a season due to tactical adjustments, managerial

changes, injuries and transfers. While Leriou and Ntzoufras (2025)’s choice of static team strength parameters is

appropriate for validation of the accelerated failure time approach within a single season, we use a larger dataset

and hence re-estimate team parameters after each gameweek using all previous matches.




                                                    Page 8 of 27
In-play football forecasting                                                             Preprint: Clegg, Song and Cartlidge (2026)


    We implement exponential time decay to capture the evolution of team strengths. Specifically, at each gameweek,

all previous matches are weighted by
                                                               (︂             )︂
                                                                     𝑑𝑘
                                                       𝑤𝑘 = exp −𝜉 ·               ,                                           (6)
                                                                     3.5

where 𝑑𝑘 is the number of days elapsed since match 𝑘, and division by 3.5 converts to half-weeks.

    We use 𝜉 = 0.0065 per half-week following Dixon and Coles (1997), who optimised this value by maximising

predictive log-likelihood on match outcomes. This yields a half-life of approximately one year.




3.4 Conditional Weibull

To adapt the framework for in-play prediction, we first consider that the Weibull distribution is not memoryless:

the probability of a goal in the next minute depends on how long the current scoreline has persisted. We must

therefore condition on the playing time 𝑠 elapsed since the last goal (or kick-off), which runs on across half-time.

Following Kleinbaum and Klein (2012), we sample 𝑇 − 𝑠 | 𝑇 > 𝑠 via inverse transform:

                                              (︂                   )︂1/𝛾
                                                   𝛾   − log(𝑈 )
                               𝑇remaining =        𝑠 +                     − 𝑠,    𝑈 ∼ Uniform(0, 1).                          (7)
                                                           𝜆


    Since we simulate from the current minute to full time, we must estimate the match endpoint, which depends

on stoppage time added by the referee at the end of each half. While Leriou and Ntzoufras (2025) sample total

stoppage uniformly from [3, 7] minutes, we use half-specific means computed exclusively from the 100 training

matches preceding the evaluation period: 3.1 minutes for the first half and 6.4 for the second. We restrict this

computation to the current season because the rules for added time changed twice. From 2023/24, referees added

the exact time lost to goals, substitutions and other stoppages, following guidance from the International Football

Association Board, and from 2024/25 the first 30 seconds after each goal are no longer added.5 Second-half added

time averaged 5.2 minutes in 2022/23 and 7.1 in 2023/24. Although stoppage time can be modelled from match

incidents such as goals, substitutions and cards (Watanabe et al., 2015), the simple mean performs comparably to

an oracle that knows the true match duration on our evaluation set (for the base Weibull model evaluated every

five minutes, log-loss 0.749 vs. 0.747 and accuracy 66.2% for both).




5 https://www.premierleague.com/news/3617054 and https://www.premierleague.com/news/4076251

                                                           Page 9 of 27
In-play football forecasting                                                  Preprint: Clegg, Song and Cartlidge (2026)


3.5 Shot volume

Goals are rare, so the scoreline is a coarse record of attacking output, whereas shots accumulate throughout a

match. Let 𝑡𝑘,𝑗 denote the minute of team 𝑘’s 𝑗-th shot, whether on or off target. Hence,

                                                               ∑︁
                                                  𝑆𝑘 (𝑡) =                1                                         (8)
                                                             𝑗: 𝑡𝑘,𝑗 ≤𝑡


                                                                                                                 ¯
is the running total of shots from kick-off. Since 𝑆𝑘 (𝑡) grows with 𝑡, we subtract an estimated linear baseline 𝑆(𝑡),

obtained by regressing 𝑆𝑘 (𝑡) on 𝑡 across all team-matches in the 1,236 training matches. The shots deviation

covariate is

                                                                 ¯
                                               𝜓𝑘 (𝑡) = 𝑆𝑘 (𝑡) − 𝑆(𝑡).                                              (9)


Positive values indicate above-typical shot volume for the match stage. At prediction minute 𝑀 , 𝜓𝑘 (𝑀 ) is held

fixed across all Monte Carlo paths, so future shots are not simulated. Shots vary widely in scoring potential, and

each can instead be weighted by its estimated scoring probability. This idea dates back to Pollard and Reep

(1997), who modelled the probability of a goal by logistic regression on shot location and context, and the resulting

measure is now termed expected goals (xG). Post-shot expected goals (PSxG) refines xG using where the shot

ends up in the goal. It is defined only for shots on target, so off-target shots contribute zero. FBref records both

measures for every shot (Section 2). We define analogous deviation covariates for cumulative goals, xG and PSxG,

and compare all four in Section 3.6.




3.6 Covariates

We add in-play covariates through the linear predictor and compare five candidates in Table 1: the red card

difference and the deviation covariates for goals, PSxG, xG and shots defined in Section 3.5.

    The log-expected time equations become


                                    log E[𝑇𝐻 ] = 𝜇 + 𝛽home + 𝑎𝐻 + 𝑑𝐴 + 𝛽 ⊤ x𝐻                                      (10)

                                    log E[𝑇𝐴 ] = 𝜇 + 𝑎𝐴 + 𝑑𝐻 + 𝛽 ⊤ x𝐴                                              (11)


where x𝑘 is the vector of covariate values for team 𝑘 at the current prediction time, which in the final model holds

the red card difference and the shots deviation 𝜓𝑘 .


                                                    Page 10 of 27
In-play football forecasting                                                               Preprint: Clegg, Song and Cartlidge (2026)


                                Table 1: Nested comparison of in-play covariates, 1,236 training matches.

                                                 M0        M1           M2         M3          M4       M5
                        Added covariate         None     Red cards     Goals      PSxG         xG      Shots

                        𝛾
                        ^                       1.17         1.17      1.18       1.17         1.17      1.17
                                               (0.012)     (0.012)    (0.013)    (0.013)     (0.012)   (0.012)
                        𝛽^red                    —         −0.442     −0.430     −0.424      −0.405    −0.395
                                                           (0.060)    (0.060)    (0.060)     (0.060)   (0.061)
                        𝛽^cov                    —            —       −0.027     −0.037      −0.082    −0.016
                                                                      (0.015)    (0.020)     (0.023)   (0.004)

                        𝑘                         1          2           3         3           3         3
                        ΔBIC                     0.0       −40.8       −35.5     −35.8        −45.0    −51.5
                        LRT                      —          49.3        3.2       3.4         12.7      19.2
Notes: M2–M5 each add one deviation covariate to M1. Standard errors in parentheses, conditional on team parameters fixed
from the first estimation stage. 𝛽red is the coefficient of the red card difference and 𝛽cov that of the added covariate. 𝑘 counts
estimated parameters and ΔBIC is relative to M0 (BIC 37,352.6). LRT is the likelihood ratio test statistic of M1 against M0
                     and of M2–M5 against M1, each with one degree of freedom (5% critical value 3.84).


    Red cards, though rare, substantially affect match dynamics. Maia et al. (2026), with 3,039 matches containing

715 red cards, report a 30% reduction in goal intensity for a team at a player disadvantage. Leriou and Ntzoufras

(2025) found only weak evidence given their smaller sample of 380 matches with 47 red cards. Our training set of

1,236 matches contains 157 red cards. We encode the red card difference as the opponent’s red cards minus the

team’s own, so that positive values indicate a player advantage.

    Table 1 reports a nested model comparison. Red cards yield a large improvement (M1), with the negative

coefficient indicating that a team with a player advantage scores sooner on average. In the final model (M5), a

one-player advantage shortens the expected time to the next goal by about a third. Among the deviation covariates,

shots fit best (M5), ahead of xG (M4), while goals and PSxG do not improve on M1 once the extra parameter

is penalised. PSxG averages 0.56 on scored shots against 0.20 on saved ones, so it partly restates the scoreline.

Conditional on shots, xG adds nothing (LRT = 0.5), so we adopt the shots deviation. The shape parameters shift

negligibly across specifications.

    At each prediction minute 𝑀 , we draw 𝑁 = 10,000 Monte Carlo paths and take the win, draw, and loss

proportions as the forecast. Algorithm 1 describes the exact process, using remaining playing times calculated

from the observed half and the stoppage-time estimates above.




3.7 Market-initialised team strengths

Leriou and Ntzoufras (2025) achieve an out-of-sample agreement rate of 70.5% for binary outcomes (win-or-loss

versus draw) when predicting the second half of the 2018/19 EPL season from the first, and reconstruct the same

                                                             Page 11 of 27
In-play football forecasting                                                        Preprint: Clegg, Song and Cartlidge (2026)


Algorithm 1 In-play Monte Carlo forecast at minute 𝑀 with 𝑁 = 10,000 paths.
Require: prediction minute 𝑀 ; number of paths 𝑁 ; score (𝑔𝐻 , 𝑔𝐴 ); playing time 𝑠 since the last goal (or kick-off if none);
    log-expected goal-arrival times 𝜂𝑘 = log E[𝑇𝑘 ], 𝑘 ∈ {𝐻, 𝐴}, from Equations (10)–(11); shape 𝛾; remaining playing time 𝑅 to
    the final whistle
                                 𝛾
 1: 𝜆𝑘 ← (Γ(1 + 1/𝛾) e−𝜂𝑘 ) , 𝑘 ∈ {𝐻, 𝐴}
 2: for 𝑖 = 1, . . . , 𝑁 do
          (𝑖)   (𝑖)
 3:     (𝑔𝐻 , 𝑔𝐴 , 𝑠˜, 𝑡rem ) ← (𝑔𝐻 , 𝑔𝐴 , 𝑠, 𝑅)
 4:     while 𝑡rem > 0 do
 5:         Independently sample 𝜏𝑘 from 𝑇𝑘 − 𝑠˜ | 𝑇𝑘 > 𝑠˜ via Equation (7), for 𝑘 ∈ {𝐻, 𝐴}
 6:         𝜏 * ← min(𝜏𝐻 , 𝜏𝐴 )
 7:         if 𝜏 * > 𝑡rem then break
 8:         end if
               (𝑖)    (𝑖)      (𝑖)    (𝑖)
 9:         (𝑔𝐻 , 𝑔𝐴 ) ← (𝑔𝐻 , 𝑔𝐴 ) + (1[𝜏𝐻 ≤ 𝜏𝐴 ], 1[𝜏𝐴 < 𝜏𝐻 ])
10:         𝑠˜ ← 0; 𝑡rem ← 𝑡rem − 𝜏 *                                                              ◁ only a goal resets the clock
11:     end while
12: end for
                                  (𝑖)     (𝑖)              (𝑖)  (𝑖)
                        1
                          ∑︀                     1
                                                   ∑︀
13: return 𝑝𝐻 = 𝑁           𝑖
                              1[𝑔𝐻 > 𝑔𝐴 ], 𝑝𝐷 = 𝑁     𝑖
                                                        1[𝑔𝐻 = 𝑔𝐴 ], 𝑝𝐴 = 1 − 𝑝𝐻 − 𝑝𝐷



season’s final league table in-sample with a root mean squared error of 1.4 positions. However, the betting market

is widely recognised as the most accurate pre-match forecaster (Forrest et al., 2005; Štrumbelj and Robnik-Šikonja,

2010; Wunderlich, 2025): on our evaluation set, the uninitialised Weibull achieves 52.9% pre-match accuracy versus

56.8% for Betfair (Table 2). To analyse the model’s effectiveness at forecasting in-play, we initialise the team

strength parameters from market prices so that pre-match forecasts are approximately the same as those from

Betfair.

    To do this, we utilise the over/under markets where bettors wager on whether the total number of goals

in a match exceeds a given threshold. For example, ‘over 2.5 goals’ pays out if three or more goals are scored.

These markets provide direct estimates of the goals distribution: prices at thresholds 𝑔 ∈ {0.5, 1.5, 2.5, 3.5, 4.5}

give the market-implied probability 𝑃 (𝐺 > 𝑔) for total goals 𝐺, and collectively these five values help determine

the probability of each scoreline when combined with the 1X2 market prices and the goal-arrival model.

    These additional probabilities resolve an identifiability issue: match outcome probabilities alone are consistent

with many combinations of (𝜆𝐻 , 𝜆𝐴 ) at different absolute scoring levels. Over/under thresholds fix the total

scoring rate, yielding a unique solution. Denoting the log-expected scoring times 𝜂𝐻 = 𝜇 + 𝛽home + 𝑎𝐻 + 𝑑𝐴 and
                                                                              𝜅 , 𝜂 𝜅 ) that minimise
𝜂𝐴 = 𝜇 + 𝑎𝐴 + 𝑑𝐻 , we find for each match the market-initialised parameters (𝜂𝐻    𝐴


                                            ∑︁                   )︀2 ∑︁ (︀            )︀2
                                                      𝑝^𝑜 − 𝑝mkt          𝑝^>𝑔 − 𝑝mkt
                                                    (︀
                                   ℒ=                        𝑜      +             >𝑔      ,                                 (12)
                                        𝑜∈{𝐻,𝐷,𝐴}                     𝑔∈𝒢


where 𝑝^𝑜 and 𝑝^>𝑔 are the Weibull model’s minute 0 probabilities at (𝜂𝐻 , 𝜂𝐴 ) for match outcome 𝑜 and the over-𝑔

goals market, and 𝒢 = {0.5, 1.5, 2.5, 3.5, 4.5}. The targets 𝑝mkt
                                                              𝑜   and 𝑝mkt
                                                                       >𝑔 are the corresponding Betfair-implied

probabilities, taken from the last prices traded before kick-off. Each evaluation of ℒ estimates the model probabilities

                                                         Page 12 of 27
In-play football forecasting                                              Preprint: Clegg, Song and Cartlidge (2026)


from 10,000 simulated paths, with common random numbers across evaluations. We minimise ℒ with Powell’s

method (Powell, 1964) initialised at the (𝜂𝐻 , 𝜂𝐴 ) estimated by the model. Appendix C illustrates the resulting

shifts for the first evaluation gameweek.




4 Predictive performance

4.1 Comparison models

We compare the Weibull model with two recent in-play models, three market-implied benchmarks and Betfair’s

in-play prices. The in-play models are the Bayesian birth process of Zou et al. (2020) and the Cox process of Maia

et al. (2026), which we refer to as the Zou and Maia models. We initialise both from Betfair Exchange prices at

kick-off using the same objective as the Weibull model (Equation (12)), computing outcome probabilities by a

recursive algorithm for the birth process and by Monte Carlo simulation for the Cox process. The market-implied

benchmarks use the same prices with minimal structure, which separates the contribution of the prices from that

of the model.




4.1.1 Birth process with Bayesian updating


Zou et al. (2020) build on the non-homogeneous Poisson birth process of Dixon and Robinson (1998), where home

and away goal intensities depend on team-specific attack (𝛼) and defence (𝛽) parameters, score-state multipliers,

and a home advantage factor. Their contribution is a Bayesian update of the composite scoring parameters

𝜃1 = 𝛼𝐻 𝛽𝐴 and 𝜃2 = 𝛼𝐴 𝛽𝐻 as goals are observed. Using Gamma priors conjugate to the Poisson likelihood, the

posterior mean after observing 𝑋(𝑇 ) home goals by minute 𝑇 is


                                                    𝑟1 + 𝑋(𝑇 ) ^
                                             𝜃^1 =              𝜃01 ,                                          (13)
                                                   𝑟1 + 𝐸𝐻 (𝑇 )


where 𝜃^01 is the prior estimate from historical matches, 𝐸𝐻 (𝑇 ) is the expected home goals by minute 𝑇 , and

𝑟1 = 𝐸𝐻 (45) balances prior and in-match information: updating lightly in the first half and more aggressively in

the second. Outcome probabilities are computed exactly via a recursive algorithm. Their update uses goal times

alone.




                                                  Page 13 of 27
In-play football forecasting                                                   Preprint: Clegg, Song and Cartlidge (2026)


       Stoppage time is handled with injury-time multipliers that inflate the scoring rate at minutes 45 and 90, rather

than simulating additional match time. To control for the addition of shots in our Weibull model, we multiply

both intensities by exp(𝜉𝜓 𝜓𝑘 (𝑡)), with 𝜉𝜓 estimated jointly with the other parameters. The shots observed up to

minute 𝑇 then enter 𝐸𝐻 (𝑇 ) as a known multiplier, like the score-state and stoppage multipliers, so the update

keeps its closed form. Both ‘Zou’ variants reported below include this covariate.




4.1.2 Cox process with dynamic regressors


Maia et al. (2026) model goal arrivals as Cox processes with time-varying regressors. Home goal intensity at minute

𝑡 is
                                                 (︀                                       )︀
                               𝜆𝐻 (𝑡) = 𝛼𝐻 𝛽𝐴 exp 𝛿 + 𝜉half ℎ(𝑡) + 𝜉gd Δ𝐻 (𝑡) + 𝜉rc 𝑅𝐻 (𝑡) ,                        (14)


where 𝛿 captures home advantage, ℎ(𝑡) = 1 if 𝑡 is in the second half and 0 otherwise, Δ𝐻 (𝑡) and 𝑅𝐻 (𝑡) are the goal

and red-card differences from team 𝐻’s perspective. The model jointly estimates goal, red card, and stoppage time

processes. Red card arrivals follow a non-homogeneous Poisson process with power-law intensity, and stoppage

times for each half are Poisson-distributed with log-linear regressors for red cards and goals scored, with the

second half additionally including a close-match indicator. Outcome probabilities are computed via Monte Carlo

simulation.

       In place of their market-value regressor, for which we lack comparable data, we initialise from pre-match odds.

This modification was proposed by Maia et al. (2026). Their model with the regressor trails bookmaker odds before

kick-off (RPS 0.2090 against 0.2006, their Table 9), whereas the initialised version is level with Betfair at minute 0

(Table 2). To control for the addition of shots in our Weibull model, we extend the Cox process intensity with

the per-team shots deviation covariate 𝜓𝑘 (𝑡) defined in Equation (9), applied to home and away intensities with

a shared coefficient 𝜉𝜓 . This coefficient is estimated jointly with the other parameters and held constant during

forward simulation from the current prediction minute. Both ‘Maia’ variants reported below include this covariate.




4.1.3 Betfair Exchange


The market benchmark uses Betfair Exchange 1X2 last-traded prices, normalised to implied probabilities. Since

event times and exchange prices are recorded at one-minute resolution on separate clocks, prices at minute 𝑀

may not yet reflect a goal at minute 𝑀 . Additionally, Betfair suspends in-play markets after goals (Section 2),


                                                      Page 14 of 27
In-play football forecasting                                                  Preprint: Clegg, Song and Cartlidge (2026)


which can lead to an unfair representation in the last traded price. We therefore use prices from minute 𝑀 + 2,

by which time the market has reacted to 99% of goals in the 100 training matches of 2024/25 (97% by 𝑀 + 1).

The shift favours the market: without it, Betfair’s aggregate RPS would be 0.1320 rather than 0.1281. The prices

used are also recent, 96% having been traded within a minute of the evaluation minute. Forecasts at minute 0 are

the one exception: we instead take the last price traded before kick-off, so that the market benchmark and the

market-initialised models hold the same information.




4.1.4 Market-implied benchmarks


We use three benchmarks that take their team strengths from the same pre-match prices and add minimal in-play

structure. First, Poisson𝜅 is an independent Poisson model fitted by Equation (12), whose expected remaining

goals scale with the fraction of match time left (Dixon and Robinson, 1998). Second, Poisson𝜅,𝑡 replaces this

fraction with the empirical share of goals still to come in the training matches, which captures the rising scoring

rate and stoppage-time excess reported by Dixon and Robinson (1998). Third, Naive𝜅 is a multinomial logistic

regression on pre-match log-odds, goal difference and minutes remaining, with no goal process.




4.2 Results

We denote the base survival model as Weibull, and use Weibull𝜓 when extended with the shots covariate 𝜓. A

subscript 𝜅 indicates team strengths initialised from the last Betfair Exchange prices before kick-off; thus Weibull𝜅,𝜓

denotes the full model. The same convention applies to the comparison models: Zou𝜓 , Zou𝜅,𝜓 , Maia𝜓 and Maia𝜅,𝜓 .

The market-implied benchmarks are Poisson𝜅 , Poisson𝜅,𝑡 (where the subscript 𝑡 marks a time-varying scoring rate)

and Naive𝜅 . Betfair denotes odds-implied probabilities from the 1X2 market.

    At minute 0, all three market-initialised models (Weibull𝜅,𝜓 , Zou𝜅,𝜓 , Maia𝜅,𝜓 ) closely resemble Betfair (Table 2,

pre-match columns), confirming that market initialisation successfully incorporates market information into team-

strength parameters across structurally different model classes, while retaining each model’s structure for in-play

updating. The Poisson benchmarks sit in the same range, while Naive𝜅 is weaker at 0.990. We do not interpret

these small RPS and log-loss advantages over Betfair as a real edge: sampling variation easily covers the differences

at 𝑁 = 280, and Betfair would likely outperform market-initialised models at scale.

    Across all minutes, Weibull𝜅,𝜓 achieves a classification accuracy of 68.5% against 69.5% for Betfair, and Betfair

retains the best RPS and log-loss. Betfair’s advantage over Weibull𝜅,𝜓 is 1.0 percentage points in accuracy [0.3, 1.8],

                                                    Page 15 of 27
In-play football forecasting                                                         Preprint: Clegg, Song and Cartlidge (2026)


                        Table 2: Predictive performance before kick-off and across all evaluation minutes.

                                                   Pre-match                      All minutes
                          Model        Accuracy        RPS     Log-loss   Accuracy      RPS     Log-loss

                          Weibull          0.529     0.2102     0.9985       0.677    0.1365     0.7213
                          Weibull𝜓         0.529     0.2102     0.9987       0.677    0.1358     0.7184
                          Weibull𝜅,𝜓       0.554     0.2008     0.9747       0.685    0.1325     0.7063
                          Zou𝜓             0.507     0.2168     1.0185       0.670    0.1444     0.7675
                          Zou𝜅,𝜓           0.568     0.2011     0.9740       0.680    0.1395     0.7492
                          Maia𝜓            0.504     0.2168     1.0187       0.678    0.1377     0.7239
                          Maia𝜅,𝜓          0.557     0.2017     0.9753       0.685    0.1329     0.7068
                          Poisson𝜅         0.568     0.2011     0.9744       0.685    0.1332     0.7084
                          Poisson𝜅,𝑡       0.568     0.2011     0.9744       0.685    0.1332     0.7084
                          Naive𝜅           0.561     0.2044     0.9901       0.677    0.1381     0.7401
                          Betfair          0.568     0.2012     0.9755       0.695    0.1281     0.6831

Notes: 280 matches with 27,710 evaluated minutes. Subscript 𝜅 indicates market-initialised variants and 𝜓 the shots covariate of
Equation (9). Bold marks the best value in each column excluding Betfair, including ties. Note that, by construction, Poisson𝜅
and Poisson𝜅,𝑡 have identical pre-match predictive scores, since the time-dependent adjustment is not applied before kick-off.


0.0044 in RPS [0.0026, 0.0062] and 0.023 in log-loss [0.013, 0.034], with match-clustered 95% intervals in brackets,

so the market remains better on every metric. When both models incorporate shots and market initialisation,

Maia𝜅,𝜓 slightly trails Weibull𝜅,𝜓 on RPS (0.1329 vs. 0.1325) and log-loss (0.7068 vs. 0.7063), while Zou𝜅,𝜓 lags

substantially despite market initialisation. Naive𝜅 is clearly worse (log-loss 0.7401), but the Poisson benchmarks

Poisson𝜅 and Poisson𝜅,𝑡 are close to both (0.7084), so most of the accuracy comes from the pre-match prices rather

than the goal-arrival structure. The two Poisson benchmarks also achieve identical all-minutes predictive scores

to the reported precision, suggesting that accounting for empirical time variation in scoring rates provides little

additional predictive benefit.

    Figure 1 traces performance by match minute. Both Weibull𝜅,𝜓 and Maia𝜅,𝜓 perform close to Betfair. Betfair

holds general dominance throughout the match as the market incorporates information beyond goals and shots

that our covariates do not capture. Betfair’s relative performance improves against all models at minute 45 (the

second-half restart), as the half-time interval allows the market to fully absorb first-half information. Weibull𝜓

remains consistently above the market-initialised version, confirming the importance of market-initialised team

strength estimates. The log-loss of Zou𝜅,𝜓 rises sharply around minute 20, as its Bayesian updating overrides the

market-initialised pre-match strengths based on sparse goal evidence. In a 0–0 match, the update reduces scoring

rates by 30% at minute 20 and 50% at half-time, pushing predictions heavily toward draws.




                                                         Page 16 of 27
In-play football forecasting                                                                                                                          Preprint: Clegg, Song and Cartlidge (2026)


                                                                                           Betfair           Naiveκ         Weibullψ       Zouψ
                                                                                           Maiaψ             Poissonκ       Weibullκ, ψ    Zouκ, ψ
                                                                                           Maiaκ, ψ          Poissonκ, t    Weibull




                                          1.00

                                          0.75




                      Log-loss
                                          0.50

                                          0.25



                                          0.25



                                          0.20
                  Δ Log-loss vs Betfair




                                          0.15



                                          0.10



                                          0.05



                                          0.00

                                                 0   10           20                         30               40             50           60             70        80   90
                                                                 First half                                                                          Second half




Figure 1: Log-loss by match minute. Left: first half (minutes 0–44). Right: second half (minutes 45–95). Top: log-loss at each
evaluation minute. Bottom: log-loss minus that of Betfair.


                                                                               1.0
                                                                                                      Weibullκ, ψ (ECE 0.022)
                                                                                                      Betfair (ECE 0.013)
                                                                               0.8
                                                          Observed frequency




                                                                               0.6



                                                                               0.4



                                                                               0.2



                                                                               0.0
                                                                                     0.0              0.2             0.4     0.6         0.8          1.0
                                                                                                             Forecast probability



Figure 2: Reliability diagram for Weibull𝜅,𝜓 and Betfair over the 1X2 probabilities at all 27,710 prediction points, ten equal-width
bins. Legend values are the expected calibration error (ECE). The dashed line marks perfect calibration.



    Table 2 separates the sources of these differences. In the Weibull model the shots covariate lowers aggregate

RPS by 0.0007, while market initialisation lowers it by 0.003–0.005 in every architecture. Once initialised, the

Weibull and Cox models are indistinguishable (difference 0.0004), but both improve on Zou𝜅,𝜓 by about 0.007.

    Figure 2 compares calibration. Both forecasts lie close to the diagonal below a probability of 0.4, but for

Weibull𝜅,𝜓 forecasts between 0.4 and 0.6 and between 0.8 and 0.9, outcomes occur less often than predicted, so its

expected calibration error (ECE), the bin-weighted mean absolute gap between forecast probability and observed

frequency over all three outcomes, is higher than the market’s (0.022 against 0.013). Appendix B shows the same

diagram for every model.



                                                                                                            Page 17 of 27
In-play football forecasting                                                           Preprint: Clegg, Song and Cartlidge (2026)


                                    Table 3: Betting simulation against Betfair in-play odds.

                       Model        Strategy         Bets    Win (%)      Net Profit     ROI (%)      Sharpe

                       Weibull𝜓     Fixed payout    36,969          39       144.59           1.0      0.38
                                    Kelly           36,969          39       −93.14          −1.9     −0.57
                       Weibull𝜅,𝜓   Fixed payout    37,467          44        227.97            1.4     0.64
                                    Kelly           37,467          44         45.26            1.0     0.46
                       Maia𝜅,𝜓      Fixed payout    35,408          44       −45.51          −0.3     −0.13
                                    Kelly           35,408          44       −23.04          −0.5     −0.25
                       Zou𝜅,𝜓       Fixed payout    34,922          45        483.47            3.2     1.51
                                    Kelly           34,922          45        234.86            2.5     0.92
                       Poisson𝜅     Fixed payout    36,805          44        119.59            0.7    0.35
                                    Kelly           36,804          44        −0.67             0.0   −0.01

  Notes: 280 matches, with bets placed at every evaluation minute. Net profit is in units after 2% commission on net match
winnings, and ROI is net profit over total stake. Sharpe is the mean net profit per match over its standard deviation, annualised
                                                     √
                                                  by 380 (matches per season).



5 Betting simulation

As a secondary check, each model trades against Betfair in-play 1X2 odds at every evaluation minute (Table 3).

We compare two staking strategies, the Kelly criterion (Kelly, 1956) and the fixed-payout staking of Wilkens

(2021). For model probability 𝑝 and Betfair decimal odds 𝑜, both back every outcome with positive expected value

(𝑝𝑜 − 1 > 0) and differ only in the stake. Fixed-payout staking stakes 1/𝑜, so every winning bet returns one unit,

while Kelly staking stakes the fraction 𝑓 = (𝑝𝑜 − 1)/(𝑜 − 1) of a one-unit bankroll. Following Boshnakov et al.

(2017), the “bankroll” is reset before each bet, so stakes do not compound. A fractional Kelly stake therefore

scales every bet equally and leaves ROI and the Sharpe ratio unchanged. We also deduct a 2% commission on net

winnings in each match, matching Betfair’s “BASIC” plan.

    Weibull𝜅,𝜓 returns 1.4% under fixed-payout staking and 1.0% under Kelly staking (Figure 3A). Bets within

a match are strongly dependent, and the match-clustered 95% intervals, [−3.6%, 6.2%] and [−3.8%, 5.9%], both

include zero. The returns are also concentrated. The model profits in 68% of matches under fixed-payout staking

and 59% under Kelly staking (Figure 3C and D), but removing the six most profitable of the 280 matches (fixed

payout) or the two most profitable (Kelly) makes the return negative (Figure 3B). Neither return reflects better

calibration, as Weibull𝜅,𝜓 has a higher expected calibration error than the market (0.022 against 0.013, Figure 2),

and the market-implied Poisson𝜅 earns 0.7% under fixed-payout staking. Moreover, Zou𝜅,𝜓 , among the least

accurate models (Table 2), earns the highest returns (3.2% fixed payout, 2.5% Kelly). Last-traded prices may also

not be executable, particularly around goals when the market is suspended. We therefore regard these results



                                                         Page 18 of 27
In-play football forecasting                                                                                                                         Preprint: Clegg, Song and Cartlidge (2026)


                                    A                                                                              B
                                              300         Fixed payout                                                               1


             Cumulative net profit (units)
                                              200         Kelly
                                                                                                                                     0
                                              100                                                                                   −1




                                                                                                             Net ROI (%)
                                                0                                                                                   −2
                                             −100                                                                                   −3
                                             −200                                                                                   −4
                                             −300                                                                                   −5
                                             −400                                                                                   −6
                                                     0       10000       20000        30000                                               0          5         10      15            20
                                                                     Bet number                                                               Most profitable matches removed
                                    C                                                                              D
                                              100
                                                                                                                                     40




                                                                                                     Net profit per match (units)
                                               80
                                                                                                                                     20
                                               60
                        Matches




                                                                                                                                      0
                                               40                                                                                   −20
                                               20                                                                                   −40

                                                0                                                                                   −60
                                                    −60   −40    −20     0       20     40      60                                        0     50       100   150   200       250
                                                            Net profit per match (units)                                                        Match (ranked by net profit)

Figure 3: Betting returns of Weibull𝜅,𝜓 against Betfair in-play odds, 280 matches, under fixed-payout and Kelly staking. (A)
Cumulative net profit by bet. (B) Net ROI after removing the 𝑘 most profitable matches. (C) Distribution of net profit per match.
(D) Net profit per match, matches ranked from most to least profitable. Commission of 2% applied to net match winnings.



as preliminary: returns and forecast accuracy measure different things (Wunderlich and Memmert, 2020), and a

profitability claim would need executable order-book prices and a larger sample.

    Figure 4 shows where the returns arise. Most bets carry an edge below 0.05, with a thin tail up to 1 (Figure 4A).

Half of the bets (19,075) are placed at level scores, where both strategies lose, and the returns come from states in

which the home side trails (Figure 4B). In those states the stake is mostly on the away side, and 2024/25 had the

second-highest number of away wins in Premier League history (Bateman, 2025). By odds, both strategies lose on

outcomes priced between 6 and 15 (Figure 4C). By minute, both profit throughout the first half and lose between

minutes 45 and 59 (Figure 4D).




6 Conclusion

We have extended the Weibull accelerated failure time model of Leriou and Ntzoufras (2025) to in-play football

forecasting, and examined the effect of initialising team strengths from Betfair Exchange prices at kick-off. The



                                                                                             Page 19 of 27
In-play football forecasting                                                                                               Preprint: Clegg, Song and Cartlidge (2026)


                  A                                                                              B
                           104                                                                               10                                    Fixed payout
                                                                                                              8                                    Kelly
                           103                                                                                6




                                                                                               Net ROI (%)
              Bets                                                                                            4
                           102                                                                                2
                                                                                                              0
                           101                                                                               −2
                                                                                                             −4
                           100                                                                               −6
                                 0.0      0.2       0.4         0.6          0.8         1.0                      ≤−2      −1        0         1         ≥2
                                   Edge (model minus market probability)                                                   Home goal difference
                  C                                                                              D
                            15                                                                                8
                            10                                                                                6
                             5                                                                                4
             Net ROI (%)




                                                                                               Net ROI (%)
                             0
                                                                                                              2
                            −5
                           −10                                                                                0
                           −15                                                                               −2
                           −20                                                                               −4
                                   <1.5     1.5–3         3–6         6–15         >15                            0–14 15–29 30–44 45–59 60–74 75–89 90+
                                                Decimal odds                                                                    Match minute

Figure 4: Bets placed by Weibull𝜅,𝜓 against Betfair in-play odds, 280 matches. (A) Edge (model minus market probability) of the
37,467 bets placed, log scale. (B)–(D) Net ROI by home goal difference, decimal odds and match minute at the time of the bet,
under fixed-payout (purple) and Kelly (orange) staking.



model remains less accurate than Betfair in-play prices on every metric, and a market-implied Poisson model

initialised from the same prices performs similarly, so the accuracy of the model is mostly attributable to the

imported market information. However, its interpretable team-level parameters and covariate effects remain

valuable, as does an initialisation method that applies to any intensity-based goal arrival model. Our findings

support the view of Forrest et al. (2005) and Wunderlich (2025) that betting odds encode information difficult

to replicate from historical match data, and suggest that integrating market prices into goal arrival models is

a productive direction for in-play forecasting. The betting simulation yielded small positive returns under both

staking strategies, but given the limited sample of matches and the assumed fulfilment of orders, no conclusion can

be drawn on in-play market efficiency.

    These results carry limitations. First, the betting returns rest on Betfair’s last-traded prices, which may

differ from the prices executable at the time of prediction. Second, the 280 matches come from a single season.

Winkelmann et al. (2024) show by simulation that samples of this length can produce apparent inefficiency in

fully efficient markets by chance alone, and Wunderlich and Memmert (2020) show that positive returns can arise



                                                                                   Page 20 of 27
In-play football forecasting                                                  Preprint: Clegg, Song and Cartlidge (2026)


without a superior forecasting model. We therefore regard the accuracy results as more robust than the betting

returns. Finally, FBref has since lost access to the Opta statistics underlying our shot records.6

    Future research could extend the model in several directions. The market’s consistent advantage from minute

30 onwards, and particularly at the second-half restart, suggests the model would benefit from stronger in-play

covariates. Substitutions are a natural candidate: managers use them to alter team shape and attacking intent, and

they are easily observed. Expected threat from passing sequences (Singh, 2019) could capture sustained momentum

more effectively than shot-level statistics, which are sparse.

    Extending the evaluation to multiple leagues and seasons would test the generalisability of both the underlying

Weibull model and the initialisation approach, particularly in leagues where second-half scoring patterns or market

liquidity may differ. Access to Betfair’s Pro tier historical data (or a similar feed from a prediction market), which

records limit order book depth at 50 ms intervals, would allow executable rather than last-traded prices to be used,

supporting a more rigorous test of betting profitability.

    A final direction is to optimise the model directly for profitability rather than for likelihood. Wunderlich

et al. (2026) show theoretically that the equivalence of accuracy- and profitability-optimal model selection rests on

restrictive assumptions, and Hubáček and Šír (2023) demonstrate in NBA betting that an accuracy-inferior model

can produce systematic profits when decorrelating predictions from market prices is included in the optimisation

function. While our initialisation step targets pre-match market consistency, team-strength estimation could instead

target profit, fitting parameters that maximise expected returns against historical in-play prices rather than market

fit at kick-off.



Funding: LC’s PhD is supported by a studentship from the Engineering and Physical Sciences Research Council

(EPSRC) Doctoral Training Partnership (DTP), grant number EP/W524414/1. JC is supported by the UK

Research and Innovation (UKRI) Engineering and Physical Sciences Research Council (EPSRC), grant number

EP/Y028392/1: AI for Collective Intelligence (AI4CI). ZS received research funding from the School of Engineering

Mathematics and Technology, University of Bristol, which supported his research activities during the period in

which this work was undertaken.




6 https://www.sports-reference.com/blog/2026/01/fbref-stathead-data-update/

                                                    Page 21 of 27
In-play football forecasting                                                            Preprint: Clegg, Song and Cartlidge (2026)



References

G. Ayana, A. Ehlert, J. Ehlert, L. Santagata, M. Torricelli, and B. Klein. Temporal dynamics of goal scoring in soccer, 2025. arXiv

    preprint arXiv:2501.18606. https://arxiv.org/abs/2501.18606.

R. Bateman. Arsenal need to rediscover home comforts to succeed in 2025-26. Opta Analyst, https://theanalyst.com/articles/arsenal-

    home-form-concern-ahead-of-2025-26, 2025. Accessed: 2026-10-08.

G. Boshnakov, T. Kharrat, and I. G. McHale. A bivariate Weibull count model for forecasting association football scores. Interna-

    tional Journal of Forecasting, 33:458–466, 2017. doi: 10.1016/j.ijforecast.2016.11.006.

R. Bunker, C. Yeung, and K. Fujii. Machine learning for soccer match result prediction. In Artificial Intelligence, Optimization, and

    Data Sciences in Sports, pages 7–49. Springer, 2024. doi: 10.1007/978-3-031-76047-1_2.

A. C. Constantinou and N. E. Fenton. Solving the problem of inadequate scoring rules for assessing probabilistic football forecast

    models. Journal of Quantitative Analysis in Sports, 8:1–14, 2012. doi: 10.1515/1559-0410.1418.

K. Croxson and J. J. Reade. Information and efficiency: Goal arrival in soccer betting. The Economic Journal, 124(575):62–91, 2014.

P. Divos. Modelling of the In-Play Football Betting Market. PhD thesis, University College London, 2020. URL https://discovery.ucl.

    ac.uk/id/eprint/10115386/.

M. Dixon and M. Robinson. A birth process model for association football matches. Journal of the Royal Statistical Society: Series

    D (The Statistician), 47:523–538, 1998. URL http://www.jstor.org/stable/2988632.

M. J. Dixon and S. G. Coles. Modelling association football scores and inefficiencies in the football betting market. Journal of the

    Royal Statistical Society: Series C (Applied Statistics), 46:265–280, 1997. doi: 10.1111/1467-9876.00065.

L. Egidi, F. Pauli, and N. Torelli. Combining historical data and bookmakers’ odds in modelling football scores. Statistical Modelling,

    18:436–459, 2018. doi: 10.1177/1471082X18798414.

E. S. Epstein. A scoring system for probability forecasts of ranked categories. Journal of Applied Meteorology (1962-1982), 8:

    985–987, 1969. doi: 10.1175/1520-0450(1969)008<0985:ASSFPF>2.0.CO;2.

D. Forrest, J. Goddard, and R. Simmons. Odds-setters as forecasters: The case of English football. International Journal of

    Forecasting, 21:551–564, 2005. doi: 10.1016/j.ijforecast.2005.03.003.

A. Heuer and O. Rubner. How does the past of a soccer match influence its future? Concepts and statistical analysis. PLoS ONE, 7

    (11):e47678, 2012. doi: 10.1371/journal.pone.0047678.

B. Holmes and I. G. McHale. Forecasting football match results using a player rating based model. International Journal of

    Forecasting, 40:302–312, 2024. doi: 10.1016/j.ijforecast.2023.03.002.

O. Hubáček and G. Šír. Beating the market with a bad predictive model. International Journal of Forecasting, 39:691–719, 2023. doi:

    10.1016/j.ijforecast.2022.02.001.

L. M. Hvattum and H. Arntzen. Using ELO ratings for match result prediction in association football. International Journal of

    Forecasting, 26(3):460–470, 2010. doi: 10.1016/j.ijforecast.2009.10.002.

B. Jottreau. How do markets play soccer? Working paper, Université Paris-Est, 2009.

J. D. Kalbfleisch and R. L. Prentice. The Statistical Analysis of Failure Time Data. John Wiley & Sons, Hoboken, NJ, 2nd edition,

    2011.

                                                           Page 22 of 27
In-play football forecasting                                                            Preprint: Clegg, Song and Cartlidge (2026)


D. Karlis and I. Ntzoufras. Analysis of sports data by using bivariate Poisson models. Journal of the Royal Statistical Society: Series

    D (The Statistician), 52:381–393, 2003. doi: 10.1111/1467-9884.00366.

J. L. Kelly. A new interpretation of information rate. The Bell System Technical Journal, 35:917–926, 1956. doi: 10.1002/j.1538-

    7305.1956.tb03809.x.

F. J. Klaassen and J. R. Magnus. Forecasting the winner of a tennis match. European Journal of Operational Research, 148:257–267,

    2003. doi: 10.1016/S0377-2217(02)00682-3.

D. G. Kleinbaum and M. Klein. Survival Analysis: A Self-Learning Text. Springer, 3rd edition, 2012. doi: 10.1007/978-1-4419-6646-9.

M. Klemp, F. Wunderlich, and D. Memmert. In-play forecasting in football using event and positional data. Scientific Reports, 11:

    24139, 2021. doi: 10.1038/s41598-021-03157-3.

S. Kovalchik and M. Reid. A calibration method with dynamic updates for within-match forecasting of wins in tennis. International

    Journal of Forecasting, 35:756–766, 2019. doi: 10.1016/j.ijforecast.2017.11.008.

I. Leriou and I. Ntzoufras. Survival modeling of goal arrival times in English Premier League. Computational Statistics, 40:2109–2133,

    2025. doi: 10.1007/s00180-024-01589-9.

M. J. Maher.    Modelling association football scores.   Statistica Neerlandica, 36:109–118, 1982.     doi: 10.1111/j.1467-

    9574.1982.tb00782.x.

L. F. G. Maia, T. Pennanen, M. A. da Silva, and R. S. Targino. Stochastic modelling of football matches using dynamic regressors.

    International Journal of Forecasting, 42:181–202, 2026. doi: 10.1016/j.ijforecast.2025.10.006.

A. H. Murphy. A new vector partition of the probability score. Journal of Applied Meteorology, 12(4):595–600, 1973. doi:

    10.1175/1520-0450(1973)012<0595:ANVPOT>2.0.CO;2.

R. Pollard and C. Reep. Measuring the effectiveness of playing strategies at soccer. Journal of the Royal Statistical Society Series

    D: The Statistician, 46:541–550, 1997. doi: 10.1111/1467-9884.00108.

M. J. Powell. An efficient method for finding the minimum of a function of several variables without calculating derivatives. The

    Computer Journal, 7:155–162, 1964. doi: 10.1093/comjnl/7.2.155.

P. Robberechts, J. Van Haaren, and J. Davis. A Bayesian approach to in-game win probability in soccer. In Proceedings of the 27th

    ACM SIGKDD Conference on Knowledge Discovery & Data Mining, pages 3512–3521, 2021. doi: 10.1145/3447548.3467194.

R. M. Silva and T. B. Swartz. Analysis of substitution times in soccer. Journal of Quantitative Analysis in Sports, 12:113–122, 2016.

    doi: 10.1515/jqas-2015-0114.

K. Singh. Introducing Expected Threat (xT), 2019. URL https://karun.in/blog/expected-threat.html. Accessed: 2026-05-15.

E. Štrumbelj and M. Robnik-Šikonja. Online bookmakers’ odds as forecasts: The case of European soccer leagues. International

    Journal of Forecasting, 26:482–488, 2010. doi: 10.1016/j.ijforecast.2009.10.005.

E. Štrumbelj and P. Vračar. Simulating a basketball match with a homogeneous Markov model and forecasting the outcome.

    International Journal of Forecasting, 28:532–542, 2012. doi: 10.1016/j.ijforecast.2011.01.004.

A. Titman, D. Costain, P. Ridall, and K. Gregory. Joint modelling of goals and bookings in association football. Journal of the Royal

    Statistical Society Series A: Statistics in Society, 178:659–683, 2015. doi: 10.1111/rssa.12075.

P. Volf. A random point process model for the score in sport matches. IMA Journal of Management Mathematics, 20:121–131, 2009.

    doi: 10.1093/imaman/dpn027.

                                                           Page 23 of 27
In-play football forecasting                                                          Preprint: Clegg, Song and Cartlidge (2026)


N. M. Watanabe, P. Wicker, and J. C. Reuter. Determinants of stoppage time awarded to teams in the English Premier League.

    International Journal of Sport Finance, 10:310–327, 2015. doi: 10.1177/155862351501000402.

E. Wheatcroft. Evaluating probabilistic forecasts of football matches: the case against the ranked probability score. Journal of

    Quantitative Analysis in Sports, 17:273–287, 2021. doi: 10.1515/jqas-2019-0089.

S. Wilkens. Sports prediction and betting models in the machine learning age: The case of tennis. Journal of Sports Analytics, 7

    (2):99–117, 2021. doi: 10.3233/JSA-200463.

D. Winkelmann, M. Ötting, C. Deutscher, and T. Makarewicz. Are betting markets inefficient? Evidence from simulations and real

    data. Journal of Sports Economics, 25(1):54–97, 2024. doi: 10.1177/15270025231204997.

F. Wunderlich.   Using the wisdom of crowds in sports: how performance analysis in football can benefit from the infor-

    mation enclosed in betting odds.    International Journal of Performance Analysis in Sport, 25:687–706, 2025.     doi:

    10.1080/24748668.2024.2439034.

F. Wunderlich and D. Memmert. Are betting returns a useful measure of accuracy in (sports) forecasting? International Journal of

    Forecasting, 36:713–722, 2020. doi: 10.1016/j.ijforecast.2019.08.009.

F. Wunderlich, M. G. Caparrós, and D. Memmert. Does the consideration of market prices in model selection increase model

    profitability? Evidence from theory, artificial data and real-world data. International Journal of Forecasting, 2026. doi:

    10.1016/j.ijforecast.2025.11.006. In press, corrected proof.

Q. Zou, K. Song, and J. Shi. A Bayesian in-play prediction model for association football outcomes. Applied Sciences, 10:2904, 2020.

    doi: 10.3390/app10082904.




A Data consistency checks

Table 4 lists the data checks applied before model estimation. Three fixtures lack a WhoScored event feed altogether,

and the feed for Newcastle United v Tottenham (17 October 2021) stops in the first half. These four fixtures are

excluded. FBref and WhoScored agree on every team’s shot count in the remaining matches. WhoScored counts

minutes from 0 and FBref from 1, and after allowing for this offset only three shots are timed differently, each by

one minute. In the Betfair data, rows that do not quote all three outcomes are dropped, and one-minute price

spikes are replaced with the preceding price (Section 2). Apart from these price spikes, no check finds an error in

the evaluation matches.




                                                          Page 24 of 27
In-play football forecasting                                                             Preprint: Clegg, Song and Cartlidge (2026)


                               Table 4: Data consistency checks across the 2021/22–2024/25 seasons.


         Check                                           Checked                      Flagged    Action

         WhoScored event feed exists                     1,520 fixtures                    3     Excluded
         Event feed reaches the final whistle            1,517 fixtures                    1     Excluded
         Final score agrees with FBref                   1,517 fixtures                    1     Same fixture as above
         Shot count agrees for both teams                1,516 fixtures                    0     –
         Shot minute agrees                              39,590 shots                      3     FBref minute used
         Shot has an xG value                            39,590 shots                      0     –
         Added time at most 15 minutes per half          1,516 fixtures                    6     Retained, timestamps agree
         Goal event not duplicated                       4,501 goals                       0     –
         Betfair quotes all three outcomes (2024/25)     42,877 in-play minutes            3     Dropped
         No one-minute price spike (2024/25)             42,874 in-play prices           110     Preceding price used
         Kick-off 1X2 and over/under prices exist        280 evaluation                    0     –

Notes: Checked is the number of items examined and Flagged the number failing the check. Betfair checks cover 2024/25, the
                                     season whose in-play prices enter the evaluation.

                                                Table 5: Calibration of all models.


                                  Model         Brier   Reliability   Resolution       ECE      Slope

                                  Weibull      0.1401      0.00046        0.0820      0.014      0.90
                                  Weibull𝜓     0.1397      0.00062        0.0826      0.018      0.89
                                  Weibull𝜅,𝜓   0.1374      0.00095        0.0848      0.022      0.90
                                  Maia𝜓        0.1407      0.00041        0.0814      0.014      0.90
                                  Maia𝜅,𝜓      0.1375      0.00086        0.0847      0.021      0.90
                                  Zou𝜓         0.1464      0.00332        0.0776      0.045      0.68
                                  Zou𝜅,𝜓       0.1429      0.00302        0.0812      0.044      0.69
                                  Poisson𝜅     0.1375      0.00092        0.0847      0.020      0.89
                                  Poisson𝜅,𝑡   0.1375      0.00088        0.0846      0.020      0.90
                                  Naive𝜅       0.1433      0.00070        0.0788      0.020      0.91
                                  Betfair      0.1330      0.00047        0.0886      0.013      1.01

 Notes: 1X2 probabilities at all 27,710 prediction points, ten equal-width bins. Brier is the mean squared error of the pooled
outcome probabilities and approximately equals reliability − resolution + uncertainty (0.2222 for every model). Lower reliability
and higher resolution are better. Slope is the coefficient on the forecast log-odds in a logistic recalibration, and a slope below 1
                                                     indicates overconfidence.



B Calibration of all models

Figure 5 extends Figure 2 to every model in Table 2. The uninitialised Weibull and Cox models are close to Betfair

(ECE 0.014 for Weibull, 0.018 for Weibull𝜓 and 0.014 for Maia𝜓 , against 0.013). Market initialisation raises the

ECE to 0.022 for Weibull𝜅,𝜓 and 0.021 for Maia𝜅,𝜓 , close to the market-implied benchmarks (0.020). Table 5 shows

why initialisation still improves accuracy. In the decomposition of the Brier score of Murphy (1973), initialisation

leads to a large gain in the resolution of Weibull𝜓 from 0.0826 to 0.0848, a larger gain than its loss in reliability

(0.00062 to 0.00095). Apart from the birth process, the model-based forecasts are slightly overconfident (calibration

slope about 0.9, against 1.01 for Betfair). The birth-process models are the worst calibrated, with slopes of 0.68



                                                          Page 25 of 27
In-play football forecasting                                                                                  Preprint: Clegg, Song and Cartlidge (2026)


                 A                                                                         B
                            1.0
                                        Betfair (0.013)                                              Betfair (0.013)
                                        Weibull (0.014)                                              Maiaψ (0.014)
                                        Weibullψ (0.018)                                             Maiaκ, ψ (0.021)
                            0.8         Weibullκ, ψ (0.022)
       Observed frequency


                            0.6


                            0.4


                            0.2

                                                                              Weibull                                                 Cox process
                            0.0
                 C                                                                         D
                            1.0
                                        Betfair (0.013)                                              Betfair (0.013)
                                        Zouψ (0.045)                                                 Poissonκ (0.020)
                                        Zouκ, ψ (0.044)                                              Poissonκ, (0.020)
                            0.8
                                                                                                              t

                                                                                                     Naiveκ (0.020)
       Observed frequency




                            0.6


                            0.4


                            0.2

                                                                         Birth process                                            Market-implied
                            0.0
                                  0.0     0.2          0.4     0.6         0.8       1.0       0.0     0.2          0.4     0.6        0.8      1.0
                                                  Forecast probability                                         Forecast probability

Figure 5: Reliability diagrams for all models over the 1X2 probabilities at all 27,710 prediction points, ten equal-width bins. (A)
Weibull, (B) Cox process, (C) birth process, (D) market-implied benchmarks. The thick grey line is Betfair in every panel and the
dotted line marks perfect calibration. Legend values are the expected calibration error (ECE).



and 0.69 and ECE of 0.045 and 0.044: they overstate outcomes forecast between 0.6 and 0.8 and understate those

forecast below 0.2.




C Market initialisation shifts

Figure 6 illustrates the initialisation shifts for gameweek 11 of the 2024/25 season. Shifts range from near zero

to 0.30 (a 26-minute increase in Leicester’s expected time to score against Manchester United), reflecting the

information gap between the model’s scoreline-derived parameters and the market’s richer assessment of team



                                                                                 Page 26 of 27
In-play football forecasting                                                                                        Preprint: Clegg, Song and Cartlidge (2026)


                                                                                   Home
                                                                                   Away

                                                                       -0.02              Tottenham
                                                                       Ipswich                +0.02

                                                                     Liverpool                 +0.04
                                                                    Aston Villa                 +0.05

                                                                     West Ham                   +0.05
                                                                   -0.05                  Everton

                                                                     -0.03                Chelsea
                                                                       Arsenal                                +0.15

                                                                     -0.02                Nottingham Forest
                                                                    Newcastle                                       +0.17

                                      -0.22                                               Brighton
                                                                           -0.01          Manchester City

                                                                   -0.05                  Wolves
                                       -0.22                                              Southampton

                                                                     Brentford                          +0.11
                                               -0.18                                      Bournemouth

                                                                 Crystal Palace                                      +0.18
                                                       -0.13                              Fulham

                                   -0.25                                                  Manchester United
                                                                     Leicester                                                     +0.30

                           −0.4     −0.3           −0.2             −0.1            0.0        0.1            0.2            0.3       0.4
                                                               Shift in η (log-expected scoring time)

Figure 6: Market initialisation shifts to team scoring parameters for gameweek 11 (first evaluation gameweek, 10 matches). Each
paired row shows the shift from uninitialised to market-initialised 𝜂 for the home (purple) and away (orange) team. Positive values
indicate the market assigns a slower scoring rate than the model. Rows ordered by total absolute shift.



quality. The shifts are positive and negative in roughly equal number (9 of 20 positive), so the market reallocates

scoring strength between teams more than it changes the overall scoring rate.




                                                                           Page 27 of 27
