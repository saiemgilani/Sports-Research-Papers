<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2024/2024 - Leveraging minute-by-minute soccer match event data to adjust Team s offensive production for game context - Skripnikov et al.pdf -->

J. Quant. Anal. Sports 2025; aop 

### **Research Article** 

### Andrey V. Skripnikov*, Ahmet Cemek and David Gillman 

# **Leveraging minute-by-minute soccer match event data to adjust Team’s offensive production for game context** 

https://doi.org/10.1515/jqas-2024-0162 Received November 14, 2024; accepted July 28, 2025; published online August 25, 2025 

**Abstract:** In soccer, game context can result in skewing offensive statistics in ways that might misrepresent how well a team has played. For instance, in England’s 1–2 loss to France in the 2022 FIFA World Cup quarterfinal, England attempted considerably more shots (16 to France’s 8) and more corners (5–2), potentially suggesting they played better despite the loss. However, these statistics were largely accumulated when France was ahead and more willing to concede offensive initiative to England. To explore how game context influences offensive performance, we analyze minute-by-minute event-sequenced match data from 15 seasons across five major European leagues. Using countresponse Generalized Additive Modeling, we consider features such as score and red card differential, home/away status, pre-match win probabilities, and game minute. Moreover, we leverage interaction terms to test several intuitive hypotheses about how these features might cooperate in explaining offensive production. The selected model is then applied to project offensive statistics onto a standardized “common denominator” scenario: a tied home game with even men on both sides. The adjusted numbers – in contrast to regular game totals that disregard game context – offer a more contextualized comparison, reducing the likelihood of misrepresenting the relative quality of play. 

**Keywords:** generalized additive models; model selection; Negative Binomial; sports analytics 

***Corresponding author: Andrey V. Skripnikov** , Department of Natural Science, New College of Florida, Sarasota, FL, USA, E-mail: askripnikov@ncf.edu 

**Ahmet Cemek and David Gillman** , Department of Natural Science, New College of Florida, Sarasota, FL, USA 

## **1 Introduction** 

In soccer, commonly referred to as football, statistics play an important role in analyzing various aspects of the game – from assessing individual player and team performances to providing valuable strategic insights. For instance, metrics such as shot attempts and corner kicks can indicate how offensively dominant a player or team was during a match. However, relying solely on aggregate statistics without considering the broader context of game events may lead to misleading conclusions. 

Consider the 2022 FIFA World Cup quarterfinal between England and France (where “FIFA” stands for Fédération Internationale de Football Association). England recorded 16 shot attempts compared to France’s 8, and earned 5 corner kicks to France’s 2, yet still lost 1–2 ( _ESPN: France 2-1 England Commentary_ 2024). Based on these numbers alone, one might conclude that England played a more dominant offensive match despite the loss. However, these raw totals ignore the context of the scoreline: during the 40 min when the match was tied, France led in the aforementioned categories – 7 to 5 in shot attempts and 2 to 0 in corner kicks. In the remaining 66 min, with France in the lead, they purposefully ceded possession and initiative to England as a tactical decision, focusing their efforts on defense and protecting the lead. 

The goal of this study is to develop a statistical adjustment that accounts for crucial contextual factors – such as score differential – when interpreting offensive metrics like shot attempts and corner kicks. In particular, we explore how various contextual variables affect offensive production, and subsequently project those effects onto a standardized “common denominator” scenario: a home game where the score is tied and both teams are at even strength throughout. By doing so, we aim for the statistical outputs to more accurately reflect teams’ relative offensive performances, accounting for the likelihood of specific tactical adjustments under different game scenarios and reducing the risk of misleading conclusions. Additionally, leveraging 

Open Access. © 2025 the author(s), published by De Gruyter. 

This work is licensed under the Creative Commons Attribution 4.0 International License. 

> **2 —** A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data 

minute-by-minute data allows us to test several hypotheses regarding how the impacts of various contextual factors may vary depending on the game minute – particularly when comparing early-game versus late-game situations. 

In this section, we will first review existing metrics in soccer analytics, along with related research in other sports. We will then outline our research question and emphasize its contributions to the 

### **1.1 Background and literature review** 

The field of soccer analytics has been growing over the recent years, including the strong increase in scientific publications associated with it over the past decade (Cefis 2022). Various metrics and methods are well established in soccer performance analysis, designed to capture the complexities of game dynamics. One of the most widely adopted models in modern soccer analytics is Expected Goals, commonly referred to as _xG_ (Cefis and Carpita 2025; FBref 2024). This model estimates the probability that a given shot will result in a goal by considering factors such as shot distance, location, angle, whether it is a header, and the number of defenders between the attacker and the goalkeeper, among others. By quantifying the quality of scoring chances with numerical values, _xG_ provides a method for assessing how effectively teams create goal-scoring opportunities. Beyond shot characteristics, some models also incorporate variables that serve as proxies for psychological influences, such as match attendance, game importance (based on tournament stakes), and goal differential (Mead et al. 2023). 

With regard to similar metrics in other sports, Macdonald (2012) introduced a model to calculate expected goals in hockey based on statistics such as faceoffs, hits, and shots, facilitating performance evaluation at both the team and player levels (using adjusted plus-minus for expected goals). In rugby, Kempton et al. (2016) derived an expected point value for a possession by considering contextual factors such as field location and the outcome of the preceding possession. In American football, Yurko et al. (2019) developed a model to calculate added expected points – and even _added win probability_ – for each play, accounting for game context such as down and distance, field position, and remaining game time, among other factors. 

Although extensive research exists on Expected Goals and analogous models – such as Expected Pass ( _xPass_ ) (StatsBomb 2024b), Expected Threat ( _xT_ ) (Van Roy et al. 2020), and other possession value models (StatsBomb 2024a) – the soccer analytics literature remains relatively sparse when it comes to statistical adjustments of existing metrics for game context. The closest example to this work is [X], where offensive statistics accumulated over time intervals 

during specific game contexts were similarly projected onto a baseline scenario. While the core underlying idea is the very similar, our approach employs a far more granular, minute-by-minute game event dataset, allowing us to capture potential shifts in game dynamics between earlier and later stages of a match – something [X] does not address, as it omits the timing of events. Our modeling framework is also considerably more robust and flexible, leveraging Generalized Additive Models instead of basic dummy-variable encoding for scoring and red card contexts. Among other works involving statistical adjustments in soccer, a notable example is the use of bivariate Weibull distributions to model the relationship between goals scored and conceded, as seen in Boshnakov et al. (2017). Although these models are applied to soccer, they still often draw from frameworks developed in other sports – such as the “offensedefense” model introduced by Harville (1977) in American football, where a team’s scoring output is modeled based on both its offensive ability and the opponent’s defensive strength. Additionally, acknowledging the impact of homefield advantage (Edwards and Archambault 1979), these models typically include adjustments for whether a team is playing at home. 

### **1.2 Current research question** 

This paper aims to address the limitations of traditional soccer statistics such as total shot attempts and corner kicks. Although not as pivotal as goals or goal-related metrics – the primary focus of most soccer analytics research (e.g., _xG_ , _xPass_ , _xThreat_ ) – these complementary statistics can still help construct a narrative about which team was more in control of the match flow. When game context is ignored, total shots and corner kicks can be misinterpreted, leading to conclusions that a team won (or lost) primarily due to luck, despite generating fewer (or more, respectively) scoring opportunities. The primary objective of this work is to develop a statistical adjustment that normalizes team performances in these complementary categories to a common baseline scenario, i.e., a tied home game with an equal number of players. This adjustment enables fairer comparative analysis and reduces the likelihood of such misinterpretations. 

Beyond the adjustment itself, a key contribution of this work is a comprehensive investigation into how game context affects statistical categories such as shots and corners across five major European leagues over the past 15 years. Specifically, we hypothesize that certain tactical decisions are influenced by factors including score differential, red card differential, home versus away status, relative team strength (derived from prematch betting odds), and game 

A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data **— 3** 

minute. As noted earlier, a similar analysis was conducted in [X], but it employed a much simpler model – using dummyvariable encoding rather than Generalized Additive Models (GAMs) – and focused solely on cumulative statistics over time spent in various game states. Notably, [X] did not account for the game minute at which events occurred, thereby failing to distinguish between actions taken early in the match and those occurring toward the end. 

By leveraging detailed minute-by-minute match event data, our analysis accounts for both the half of play and the precise game minute. In addition to capturing broad trends in how offensive output evolves over the course of a match, this framework allows us to test specific hypotheses about interactions between contextual factors. For instance, it is intuitive to assume that trailing teams become increasingly aggressive in order to catch up in score, while leading teams would potentially grow more conservative in order to protect their lead. With our data and modeling approach, we can formally test whether such interaction effects are supported by empirical evidence. Given that the task of modeling minute-by-minute offensive output is more complex than analyzing aggregate counts over broader time intervals, we made sure to evaluate several candidate models before selecting our final modeling approach. That included Poisson, Negative Binomial, Zero-Inflated Poisson – potentially relevant due to the high frequency of single minutes with zero shot attempts or corner kicks – Gaussian, and Log-Link Gaussian. 

Lastly, whereas much of soccer analytics relies on complex and less interpretable machine learning algorithms, we prioritize clarity by explicitly explaining _how_ various contextual factors affect offensive statistics, ensuring a full understanding of their effects and testing for their statistical significance. The additivity assumption in Generalized Additive Models (GAMs) allows us to interpret the partial effect of each covariate consistently, with statistical inference methods applying naturally due to GAMs being grounded in the linear modeling framework. Moreover, GAMs offer a clear mechanism for conducting significance testing and visualizing interaction effects, which is particularly valuable in evaluating the plausibility of several key hypotheses. 

## **2 Methods** 

### **2.1 Data collection and cleaning** 

We compiled a large dataset by web scraping minute-byminute event commentary from _ESPN.com_ , covering 15 seasons (2008–2023) in five major European football leagues: England’s Premier League, Spain’s La Liga, Germany’s 

Bundesliga, France’s Ligue 1, and Italy’s Serie A. The events captured included various game statistics such as goals, shot attempts, corner kicks, and disciplinary actions (e.g., yellow and red cards), along with the half of play and the exact game minute in which each event occurred. In parallel, betting coefficients for the same leagues and period were collected from _Oddsportal.com_ . These coefficients serve as a reliable indicator of team strength, reflecting a combination of historical performance, recent form, injuries, expert assessments, and market trends, often being highly predictive of the game outcome (Lopez et al. 2018). To handle the dynamic nature of _Oddsportal.com_ , we employed the _Selenium_ browser automation tool ( _The Selenium Browser Automation Documentation_ 2024). This additional data was instrumental in accounting for potential confounding effects related to team-level characteristics. 

Given the unstructured nature of the web-scraped text data, we undertook an extensive data wrangling and preprocessing pipeline. This included using regular expressions to identify and link game events to their corresponding teams, synchronizing the text commentary from _ESPN.com_ with the betting data from _Oddsportal.com_ , and addressing data inconsistencies. For instance, some games contained commentary from a different match or had inconsistent data formats (e.g., variations in parentheses usage and nomenclature). These issues affected only about 70 games out of over 25,000, and we opted to exclude them from the analysis. Additionally, we encountered occasional instances of out-of-order game minutes (e.g., minute 50 followed by minute 47 or a “Game ends” entry at the start of a half), which were resolved without removing the affected observations. 

For statistical modeling, we structured the final dataset as shown in Figure 1 by aggregating the total events of each type (e.g., shot attempts, corner kicks) per minute per game, while also capturing relevant contextual factors such as homefield indicator, score and red card differentials at each minute. Additionally, we converted prematch betting coefficients into win probabilities and calculated the win probability differential between the teams to measure their relative strengths. The game minute resets to 1 at the start of the second half, with both the half indicator and the minute value used to represent the current game minute during modeling. 

In total, we ended up with: 868,150 min-by-minute observations (4,540 games) from German Bundesliga, 1,080,842 (5,593 games) observations for Italian Serie A, 1,066,160 observations for Spanish La Liga (5,534 games), 1,042,564 observations (5,409 games) in French Ligue 1 

> **4 —** A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data 



**Figure 1:** Minute-by-minute event data format for statistical modeling, with shot attempts as the response variable. 

and 918,658 observations (4,676 games) in English Premier League. 

### **2.2 Modeling setup** 

To model count-based statistics such as shot attempts and corner kicks, we primarily considered the Poisson distribution as the foundational approach. Specifically, in addition to regular Poisson regression, we explored the following alternatives: Negative Binomial distribution, which handles overdispersion (when the variance of the response variable exceeds its mean, violating one of the key assumptions of the Poisson distribution); and the Zero-Inflated Poisson approach, due to the high prevalence of zero counts in our response variables (over 85 %) (McCullagh 2019). We also considered Gaussian and Log-Link Gaussian regression models as a sanity check, to compare against the countbased models. For more details on model selection, see Section 3.1. 

In our regression analysis, we included a baseline set of predictors to explain the response variable (e.g., shot attempts). These predictors were: score differential ( _Diff.S_ ), red card differential ( _Diff.RC_ ), home-field indicator ( _Home_ ), win probability differential ( _Diff.WP_ ), half indicator ( _Half_ ), and game minute ( _GM_ ). To model the dependence between observations for the same team and season, we incorporated team- and season-level random intercept effects. Additionally, to capture potential non-linear relationships, we used smoothing spline Generalized Additive Models (GAMs) (Wood 2017). The model formula for shot attempts ( _Shot.Att_ ), which incorporates the baseline predictors along with the team- and season-level random effects, is as follows: 



where the _s_ () notation represents smoothing splines used to model the non-linear effects of all predictors except the binary home-field indicator, which is represented by a dummy variable. To account for differences in game 

dynamics between the two halves, we model the game minute effect for each half separately using _s_ ( _GM_ | _Half_ = 1) and _s_ ( _GM_ | _Half_ = 2) terms. Additionally, the team- and season-level random effects are modeled via smooth terms that allow varying intercept values across different levels of the respective categorical variables (for more details, see (ibid.)). This combination of techniques enabled us to effectively model offensive production rates per minute while accounting for various contextual factors, as well as teamand season-level dependence in the data. 

Note that we also conducted significance testing for within-game dependence by introducing a game-level random effect (based on the _gameId_ variable from Figure 1) instead of the season-level effect in (1). We performed these tests for each individual season, swapping the _s_ ( _season_ ) term for _s_ ( _gameId_ ), but found that the game-level random effects were not statistically significant<sup>1</sup> for the vast majority of the 5 × 15 = 75 tests (five leagues, 15 seasons each). Therefore, we proceeded with only team- and season-level random effects to account for observation dependence. 

### **2.3 Model selection** 

For goodness-of-fit tests and model diagnostics, we used the simulation-based residuals approach _DHARMa_ (F. Hartig and M. F. Hartig 2017), which emulates the residualsvs-fitted and quantile-quantile diagnostics from classic regression, but for a broader set of response variable distributions, including count-based models. In addition to diagnostic plots, _DHARMa_ provides significance tests for residual uniformity (Kolmogorov-Smirnov), overdispersion, and outliers. For Poisson-based models, it also includes an explicit test for zero-inflation. We used all of these tools to assess the appropriateness of the distributional classes considered for the data. 

Among other model comparison tools, we used both the Akaike Information Criterion (AIC) and Bayesian 

> **1** Here, and throughout the manuscript (unless explicitly specified otherwise), the significance level is set to 0.05. 

A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data **— 5** 

Information Criterion (BIC) to prioritize simplicity and interpretability while maintaining a good fit (Akaike 1998; Schwarz 1978). Additionally, to explicitly evaluate out-of-sample performance, we adopted a leave-oneseason-out cross-validation (LOSOCV) approach, inspired by Yurko et al. (2019). The evaluation metrics included mean absolute error (MAE) and root mean squared error (RMSE) on the response scale, which represent the average errors when predicting shot attempts and corner kicks for each game minute. 

To select the degrees of freedom for the smoothing spline estimates, we used generalized cross-validation (GCV), the default method in the _mgcv_ package. This method efficiently calculates a leave-one-out cross-validation smoothing spline estimate with the same computational cost as obtaining a single fit (Wood 2017). After observing instability in the smoothing spline fits at the extreme ends of certain predictor variable ranges, we considered several ad-hoc approaches to address this issue. First, similar to [X], we “binned” extreme values of predictors into a single value, in order to treat them the same during modeling. For example, score differentials of 3 and higher (3 _,_ 4 _,_ 5 _,_ …) were treated as 3, while score differentials of −3 and lower (−3 _,_ −4 _,_ −5 _,_ …) were treated as −3. Score differentials of −2, −1, 0, 1, and 2 remained unchanged. For red card differentials, the “+2” and “−2” categories were binned, and for game minutes, extra time (i.e., minutes past the 45-mark) was treated the same as minute 45. The intuition was to alleviate fitting issues primarily caused by lower and/or inconsistent sample sizes at the extreme ends of the ranges. 

Additionally, as a lower-complexity alternative to the smoothing spline fit, we considered an ad-hoc natural cubic spline approach (ibid.). Specifically, we manually set the knots to the most prevalent discrete values of score differential (−2 _,_ −1 _,_ 0 _,_ 1 _,_ 2) and red card differential (−1 _,_ 0 _,_ 1). For the effect of game minute, we chose a slightly lower degree of freedom compared to the smoothing spline estimate (e.g., 5 as opposed to 8), and we made the effect of win probability differential fully linear, as it appeared linear in the smoothing spline estimates. Finally, we compared all models (smoothing splines GAM with/without binned extremes, natural cubic splines with/without binned extremes) using AIC, BIC, and LOSOCV. 

Lastly, to compare and illustrate how well-calibrated our models were in predicting event rates across the five soccer leagues, we adapted the “leave-one-season-out” approach presented by Yurko et al. (2019). The main difference is that we applied this approach to count data, whereas Yurko et al. used it for ordinal regression modeling 

to predict rates of various ordinal outcomes. Specifically, we bucketed the predicted event rates into intervals of size 0.01 (i.e., [0, 0.01], (0.01, 0.02], etc.) and plotted the midpoints of these intervals against the actual event rates observed for corresponding data points. For a well-calibrated model, the predicted and actual event rates should form an _x_ = _y_ diagonal line. 

### **2.4 Variable selection and hypothesis testing** 

To evaluate the importance of all variables under consideration, we conducted significance testing for each factor in the baseline set: score differential, red card differential, home advantage, win probability differential, and game minute. Given the large sample sizes for each league (∼1,000,000 observations), even small effects are more likely to be statistically significant. To address this, we fit the models separately for each season, removing the season-level random effect from (1) for this task, resulting in approximately 50,000–75,000 observations per fit. We also applied Holm’s multiple-testing correction (Holm 1979) to control the Type I error rate across all 5 × 15 = 75 tests (five leagues, 15 seasons) for each respective effect. 

Additionally, we tested the significance of pairwise factor interactions by including each interaction as a separate term alongside the baseline set of five key factors for each season, and then evaluating the improvement achieved. This approach allowed us, among other research questions, to investigate hypotheses about how the effects of score and/or red card differential on offensive output change during different stages of the game. We then compared and contrasted the effect displays for cases where interactions were statistically significant versus those where they were not. 

### **2.5 Statistical adjustment approach** 

After fitting the final model and obtaining estimates for the effects of score differential, red card differential, and home advantage, we proceeded to develop an adjustment that projects offensive outputs onto the shared scenario of a tied home game played at even strength throughout. Suppose the offensive output, such as shot counts, is accumulated during a period when the score differential is _s_ , with _s_ ≠ 0. In this case, we adjust the shot count for a tied game scenario via multiplying it by _e_<sup>−(</sup> _𝜂s_ − _𝜂_ 0 ), where _𝜂s_ − _𝜂_ 0 represents the difference in the estimated linear predictor values ( _𝜂_ = log(Shots)) between a score differential of _s_ and 0. This adjustment captures the inverse effect of transitioning from a tied game to a differential of _s_ . 

> **6 —** A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data 

Similarly, if the shot count is recorded during a period with a red card differential _rc_ , _rc_ ≠ 0, we project it onto a scenario where the red card differential is zero by applying the same type of reciprocal adjustment. Notably, since the final model ends up not including interaction terms (see discussion and reasoning later), the linear predictor estimate differences for various score and red card differentials remain consistent as long as all other predictors are held at the same values for both scenarios. Lastly, to adjust an away team’s performance to a hypothetical home game, we multiply their shot counts by _e_<sup>−</sup> _𝛾_ , where _𝛾_ is the estimated coefficient for the home dummy variable, with home serving as the baseline category. If a team’s offensive output was accumulated in a tied home game with no red card differential, no statistical adjustment is required. 

In addition to the point estimates for projected values, we also provide 95 % confidence intervals (CIs). These intervals are initially calculated for the difference in linear predictor values, such as _𝜂s_ − _𝜂_ 0 for the score differential _d_ , where _d_ ≠ 0. We utilize the Bayesian posterior covariance matrix for the GAM model parameters to estimate the standard error (Wood 2017). Subsequently, we apply the appropriate quantiles from the standard normal distribution to obtain the 95 % confidence interval for the difference, which is then transformed to the scale of the response. 

Note that no explicit statistical adjustment is made for win probability differential, half of play, or game minute. We believe it would be unfair to penalize a team for being inherently stronger (or reward a team for being inherently weaker), and it does not make practical sense to adjust statistics solely based on when they were accumulated during the match. The primary purpose of including these variables in the model was twofold: first, to control for them when estimating the effects of other factors, such as score differential, red card differential, and home advantage; and second, to test for potential interactions with these factors, which could affect how score or red card differential impacts offensive output at different values of win probability differential or game minute. 

To illustrate the intuition behind the adjustment mechanism, we showcased the strongest value shifts in shots and corner kicks resulting from our adjustment – both within individual games and across an entire season. We accompany these shifts with relevant contextual information, such as statistics accumulated while a team was ahead or behind in score, up or down in men, and whether they played at home or away. In addition to highlighting the strongest individual shifts, we conducted a correlation analysis to demonstrate that the adjusted values align more closely with intuitive statistical categories, including final 

league standings in terms of points earned (a team earns 3 points for a win, 1 for a draw, and 0 for a loss). For each season, we calculated the correlation between each team’s actual values (shots or corner kicks) and the points earned, repeating the same calculation for the adjusted values. We then averaged these correlations across all 15 seasons and all five leagues under consideration, reporting the overall mean correlation (mean(Err)) along with the standard error estimate (<sup>sd(Err)where</sup><sup>_n_=15×5=75).</sup> ~~√~~ _n_<sup>,</sup> 

Lastly, as another way to demonstrate that our adjustments improve upon the raw statistics, we evaluated their performance in forecasting score differentials using a basic multiple linear regression model. Specifically, the model included the home team’s and away team’s statistic values (e.g., shots per game up to that point in the season) as explanatory variables, with the response variable being the final score differential of the game from the home team’s perspective. For each season, we used the first 50 % of the games (approximately 190 games total, or about 19 games per team) to train the model, and the remaining 50 % to test forecasting performance. The per-game averages used for prediction were calculated solely from the training data to prevent data leakage. We used root mean squared error (RMSE) as the performance metric, comparing it between regression model that used adjusted statistic values versus the one using actual values. For each league, we conducted a paired _t_ -test on the differences in RMSE between the adjusted and actual statistics for each year, testing whether the mean difference was significantly different from zero. To verify the normality assumption, we applied the ShapiroWilk normality test (Shapiro and Wilk 1965), and we report the corresponding _p_ -values and 95 % confidence intervals. 

## **3 Results and discussion** 

### **3.1 Model selection** 

Using the modeling formula (1) outlined in Section 2.2, we fitted Poisson, Negative Binomial, Gaussian, and Log-link Gaussian GAMs to each season from 2008 to 2023 for the five major European soccer leagues under consideration, and conducted DHARMa quality-of-fit tests and diagnostics. We found the count-based models to be more appropriate than their Gaussian counterparts, as the latter consistently showed statistically significant deviations in the Kolmogorov-Smirnov test and displayed inadequate patterns in both residuals-vs-fitted and quantile-quantile plots. In comparing the Poisson and Negative Binomial fits, both models consistently satisfied the Kolmogorov-Smirnov 

A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data **— 7** 

test. However, the Poisson model exhibited statistically significant violations in both overdispersion and zeroinflation tests, which the Negative Binomial model did not. See the Supplementary materials for Holm-corrected _p_ - values of all the aforementioned goodness-of-fit tests, along with several examples of DHARMa diagnostic plots and their comparisons across the models. 

In comparing the Negative Binomial and Zero-Inflated Poisson (ZIP) regression models, due to lack of DHARMa diagnostic tools for Zero-Inflated Poisson GAM model, we resorted to AIC, BIC and LOSO calibration approach described in Section 2.2. As shown in Tables 6 and 7 in the Appendix, AIC indicated a slight advantage for ZIP, while BIC favored the Negative Binomial, mostly due to the significantly lower complexity of the Negative Binomial model (ZIP has twice as many parameters due to its two components). The LOSO calibration approach, illustrated in Figure 2, demonstrated that, except for a few cases with a really low number of observations, the Negative Binomial’s out-of-sample event rate predictions closely aligned with the actual observed rates, in contrast to the ZIP model (the plot is for shot attempts, but the same pattern holds for 

corner kicks). This discrepancy largely results from ZIP overly emphasizing individual zero counts through its zeroinflation component, while underestimating actual event rates by multiplying the Poisson count probability by the probability of not having a structural zero. Since one of the main priorities of our statistical adjustment mechanism is to accurately reflect the _rates_ at which events occur in various game contexts, also combined with the fact that BIC clearly favored the Negative Binomial model for its lower complexity while maintaining a good fit, we chose Negative Binomial as the response distribution moving forward. 

After fitting a single Negative Binomial smoothing spline GAM to all 15 seasons for each respective league, we observed that effect estimates were quite unstable at the extreme ends of the predictor range (see Figure 8 in the Appendix). For example, the effect of score differential exhibited an inconsistent pattern starting at ±4, while the effect of game minute beyond 45 appeared completely unpredictable. These irregularities were likely a byproduct of the leave-one-out cross-validation estimates used by default when fitting smoothing spline GAMs. While computationally efficient, these estimates tend to be more 



**Figure 2:** Leave-one-season-out cross-validation calibration results for the final Negative Binomial regression model when predicting shot attempts across five major European soccer leagues and 15 seasons under consideration. Zero-Inflated Poisson regression model is provided as well for comparison. 

> **8 —** A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data 

prone to overfitting. To address this, we considered adhoc approaches such as binning extreme categories and creating a simpler natural cubic spline model (for more details, see Section 3.1). After evaluating both approaches using AIC, BIC, and LOSOCV, the binning approach with smoothing spline GAMs performed best, and we selected it as our primary model moving forward. For more details on the comparison between the considered models and the potential impact on the nature of the effects, see the Supplementary materials. 

For the final Negative Binomial GAM with binned extreme categories, the leave-one-season-out predictive performance of the model was as follows. When predicting per-game shot counts (the sum of single-minute predictions across the entire game), the average errors across leagues ranged from 3.24 to 3.53 shots per game, which corresponds to about 27–28 % of the actual per-game shot attempt averages. For corner kick predictions, the average errors across leagues were between 1.9 and 2.1 corners per game, about 40 % of the actual per-game corner kick averages. The outof-sample _R_<sup>2</sup> values for shot attempts ranged from 21 % to 31 %, while for corner kicks, they ranged from 17 % to 22 %, depending on the league. Overall, these performance metrics are not necessarily impressive, but it’s important to note that the set of features used in our model is relatively limited (lacking fine-grained data such as player rosters, injuries, weather factors, etc.), and the additive modeling framework is simpler than some other existing alternatives. This simplicity was intentional, as we prioritized interpretability and intuitiveness in the adjustment mechanism. While pure out-of-sample predictive performance could likely have been improved by considering other model types (e.g., random forests, neural networks), these “black box” models would have made the effects harder to interpret, and the adjustment mechanism would have been less intuitive (compared to the straightforward multiplication by a coefficient used in our case). Lastly, it’s evident that corner kicks appear to be more challenging to predict than shot attempts. 

### **3.2 Nature of estimated effects** 

Figure 3 illustrates the effects of the four baseline factors modeled with smoothing splines (all except the home-field indicator, which was modeled using a dummy variable), with separate smooths for two halves of play in case of game minute. 

After binning the extreme categories, score differential exhibits a clear negative pattern, where offensive production tends to decrease as the score difference becomes more positive. The red card differential shows a strong negative effect on offensive production, while the win probability 

differential has a strong positive effect, with both relationships appearing mostly linear. The effect of game minute shows offensive output gradually increasing over the first 5 min of each half, with lower activity at the start of the 1st half compared to the 2nd. This makes sense, as teams may use the first few minutes of the game to assess each other, while in the 2nd half, they are more calibrated for the opponent. After the first 5 min, there is a relatively stable, flat pattern with the same level of activity for the remainder of either half. 

One curious observation is that the Italian Serie A appears to have the steepest impact of score differential on offensive production. Leading teams seem to play even more defensively than in other leagues, limiting their own offensive production while also allowing their opponents to accumulate even more offensive output (this is also reflected in their multiplicative coefficients in Figure 6 later). Historically, Italian soccer has been strongly associated with defensively-minded tactics, the most famous being “catenaccio” – a system that has been embraced by the Italian league and national team throughout their history (Sosa 2015). While catenaccio in its original form is less prevalent in recent decades (Trequattrini et al. 2016), modified versions of it, with an overall emphasis on defensive responsibility, have likely remained in Italian soccer. We suspect that these plots may be reflecting this tendency. 

### **3.3 Studying interaction effect hypotheses** 

After performing season-by-season hypothesis testing to assess the statistical significance of each of the five key factors, along with their pairwise interactions, the results are shown in Figure 4. Accounting for Holm’s correction, every individual key factor under consideration (score differential, red card differential, game minute, win probability differential, home/away factor) was always statistically significant when modeling shot attempts, and significant in the vast majority of cases for corner kicks. This confirms our intuition to retain all of these factors in our baseline model. 

As for the pairwise interaction terms, there were very few cases (virtually none for corner kicks) where adding an interaction term resulted in a statistically significant improvement over the baseline model. In particular, the only interaction term with at least a handful of significant tests was the one between score differential and game minute when predicting shot attempts, which partially confirms one of our primary intuitive hypotheses. To investigate the nature of the effect and confirm that it aligns with our intuition, Figure 5 illustrates the effects of score differential on shot attempts at different points in the game, for a couple of leagues and years where the interaction 

A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data **— 9** 



**Figure 3:** Nature of effects for score differential, red card differential, win probability differential and game minute in 1st/2nd halves on shot attempts (left) and corner kicks (right) in the baseline Negative Binomial Generalized Additive smoothing splines model fitted to 15 seasons (2008–2023) across five major European soccer leagues. The _y_ -axis is on the scale of linear predictor (log-response). The extreme predictor values (±3 for score differential, ±2 for red card differential, 45+ for minute) were binned. 

was found insignificant (top row) and significant (bottom row), respectively. For the cases where it was significant, it indeed confirms our intuition: the trailing team becomes more active toward the latter stages of the second half (end of the game), while the leading team becomes more 

conservative. This is particularly true for smaller score differentials, like ±1, where the game is still within reach. However, for the leagues and years where the interaction between score differential and game minute was not significant – which is the vast majority – it is clear that the data did 

> **10 —** A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data 



**Figure 4:** The _p_ -values from season-by-season fits of Negative Binomial smoothing splines GAM model with binned extreme values. Each effect’s p-value was Holm-adjusted for the fact that there were 15 × 5 = 75 tests being conducted. Five key factors were tested in a model without the interactions included. Each interaction was tested as an additional term to the baseline model of five key factors. 

not support the effect, indicating that a simpler model with additive effects was sufficient. Therefore, for consistency in our adjustment mechanism, we proceeded with the baseline model of the five key factors moving forward. 

Meanwhile, for corner kicks, there were even fewer cases where any of the interactions were found significant after Holm’s correction. More notably, in some cases, even the additive effects of red card differential and game minute had _p_ -values above the typical thresholds of 0.01/0.05, which was never the case for shot attempts. This indicates that while corner kicks mostly exhibit similar patterns to shot attempts, they are not as straightforward to model as a function of those game context variables. This manifests in lower quality-of-fit and out-of-sample performance metrics, as discussed at the end of Section 3.1. 

### **3.4 Statistical adjustment** 

Figure 6 shows the multiplicative coefficients for shot attempts and corner kicks, derived by converting the effect estimates from Figure 3 as described in Section 2.5. Shots 

and corner kicks attempted while trailing receive less credit, with multiplication coefficients ranging from 0.70 to 0.90 (a reduction of 10–30 %). In contrast, offensive output produced when in the lead is weighted more heavily, with coefficients ranging from 1.10 to 1.75 (an increase of 10–75 %), depending on the league and size of the lead. Offensive output generated with a numerical advantage (negative red card differential) is significantly downgraded, with a 25 % reduction when up by one player (multiplication coefficient of 0.75), and a 30–60 % reduction when up by at least two players (coefficients of 0.40–0.70). Conversely, shots and corner kicks attempted with fewer players on the field receive substantial extra credit, with coefficients of 1.7–1.9 when down by one player, and 2–3 when down by at least two players. 

These patterns are generally consistent across leagues, though the magnitudes vary, with Serie A showing steeper coefficients for score differential adjustments (see Section 3.2 for the ‘catenaccio’ discussion). The wider intervals for teams with at least a 2-man 

A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data **— 11** 



**Figure 5:** Investigating the nature of the potential interaction effect between score differential and game minute. 

disadvantage likely result from smaller sample sizes and more inconsistent offensive activity among these teams, compared to those with a 2+ man advantage. In the following subsections, we examine the impact of these adjustments at both the single-game and season-long levels, highlighting the most significant shifts in values and the underlying intuition behind the adjustment mechanism. 

#### **3.4.1 Single-game adjustments** 

Tables 1 and 2 present the individual games where a team experienced the most significant positive and negative adjustments to shot production and corner kicks, respectively, across the five European soccer leagues from 2008 to 2023. To clarify the adjustment mechanism, the tables also include a contextual breakdown of the game situations during which the respective offensive outputs were generated. 

The strongest positive adjustment in each respective league (top five rows) corresponds to the team that generated most of their offensive output while leading by at least one goal and having at least a one-man disadvantage. As shown previously in Figure 3, such game contexts (playing with a lead and with fewer men) typically hinder shot 

production, thus benefiting from an adjustment that projects them onto a more favorable scenario – a tied game at even strength. For example, in the German Bundesliga, the most significant increase in shot attempts occurred for Bayern Munich in their 4-0 win at home against Stuttgart during the 2020/21 season, where their shot count rose from 15 to 31.9 (95 % CI: [30.1 _,_ 33.7]) due to the adjustment. The majority of their shots (14) were attempted after losing a player to a red card in the 12th minute, with 12 of those attempts coming after they took the lead, which they maintained. Both factors created unfavorable conditions for offensive production, making Bayern’s performance even more remarkable. Regarding corner kicks, the largest increase in the Bundesliga occurred for VfL Wolfsburg in their 2-2 draw on the road against Eintracht. Wolfsburg led for the majority of the game while also receiving a red card in the first half. They generated 7 of their 9 corner kicks while playing both shorthanded and in the lead, doubling their count due to the adjustment, which acknowledged their impressive effort given the circumstances. 

One commonality among the largest positive shifts is that the majority of these teams generated most of their offensive output after going up by at least two goals, which increases their weight in our adjustment approach. For 

> **12 —** A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data 



**Figure 6:** Multiplicative coefficients for shot attempts and corner kicks generated during respective score and red card differentials to project those on the scenario of a tied game with equal number of men, along with 95 % confidence intervals. 

example, in Table 1, both Bayern Munich and Caen had 11 of their 15 shots occur when leading by at least two goals, while for Inter Milan it was 26 of their 40 shots, and for Real Madrid – 31 out of 40. In Table 2, AS Roma had 13 out of their 

15 corner kicks when leading by at least two goals, while Barcelona had 6 out of 8. These projections suggest that the actual offensive outputs of these teams may underrepresent their performance level due to tactical considerations. They 

**Table 1:** Individual games across 2008–2023 seasons for each of the five European soccer leagues under consideration where a team experienced strongest positive (first five rows) and strongest negative (last five rows) absolute adjustments in their shot production. An “@” symbol indicates that the team played away, at the opponent’s home field. An asterisk “<sup>∗</sup> ” denotes games where the score or red card differential exceeded ±1 (e.g., ahead by at least 2 goals or down by at least 2 men). 

|**League**|**Team**|**Opponent**|**Season**||**Total** **shots**|**Actual**|**shots** **(&** **m**|**inutes** **playe**|**d)** **when**|
|---|---|---|---|---|---|---|---|---|---|
|||||||**Up**|**Down**|**Up**|**Down**|
|||||**Actual**|**Adjusted,** **[95** **%** **CI]**|**1** **+** **goal**|**1** **+** **goal**|**1** **+** **man**|**1** **+** **man**|
|**Stronges**|**t** **positive** **shifts** **in** **e**|**ach** **league:**||||||||
|ENG <sup>a</sup>|Manchester City|@ West Brom|2012/13|24|41.7, [39.7, 43.9]|1 (2)|2 (13)|0 (0)|20 (78)|
|FRA|Caen|@ Troyes|2015/16|15|31.7, [30.4, 33.1]|13 (78) <sup>∗</sup>|0 (0)|0 (0)|9 (38)|
|GER|Bayern Mun|Stuttgart|2020/21|15|31.9, [30.1, 33.7]|12 (76) <sup>∗</sup>|0 (0)|0 (0)|14 (82)|
|ITA|Inter Milan|Chievo V|2017/18|40|54.6, [53.6, 55.7]|28 (71) <sup>∗</sup>|0 (0)|0 (0)|0 (0)|
|SPA|Real Madrid|@ Real Zaragoza|2011/12|40|60.7, [59.1, 62.4]|33 (67) <sup>∗</sup>|0 (0)|0 (0)|0 (0)|
|**Stronges**|**t negative** **shifts** **in**|**each** **league:**||||||||
|ENG|Blackpool|W Brom|2010/11|26|13.0, [11.1, 15.2]|25 (79) <sup>∗</sup>|0 (0)|26 (81) <sup>∗</sup>|0 (0)|
|FRA|Bordeaux|Montpellier|2021/22|31|13.8, [12.5, 15.1]|0 (0)|31 (94) <sup>∗</sup>|31 (66) <sup>∗</sup>|0 (0)|
|GER|Eintracht|Stuttgart|2010/11|30|22.1, [21.5, 22.8]|0 (0)|12 <sup>∗ </sup>(26)|26 (76)|0 (0)|
|ITA|AS Roma|Venezia|2021/22|43|28.7, [28.0, 29.4]|0 (0)|29 (79)|38 (70)|0 (0)|
|SPA|Getafe|Deportivo|2009/10|22|12.8, [12.1, 13.6]|0 (0)|22 (79) <sup>∗</sup>|19 (66) <sup>∗</sup>|0 (0)|



> aENG, English Premier League; FRA, French Ligue 1; GER, German Bundesliga; ITA, Italian Serie A; SPA, Spanish La Liga. 

A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data **— 13** 

**Table 2:** Individual games across 2008–2023 seasons for each of the five European soccer leagues under consideration where a team experienced strongest positive (first five rows) and strongest negative (last five rows) absolute adjustments in their corner kick production. An “@” symbol indicates that the team played away, at the opponent’s home field. An asterisk “<sup>∗</sup> ” denotes games where the score or red card differential exceeded ±1 (e.g., ahead by at least 2 goals or down by at least 2 men). 

|**League**|**Team**|**Opponent**|**Season**|**T**|**otal** **corners**|**Actual**|**corners** **(&** **m**|**inutes** **played**|**)** **when**|
|---|---|---|---|---|---|---|---|---|---|
|||||**Actual**|**Adjusted**|**Up**<br>**1** **+** **goal**|**Down**<br>**1** **+** **goal**|**Up**<br>**1** **+** **man**|**Down**<br>**1** **+** **man**|
|**Strongest**|**positive** **shifts** **in**|**each** **league:**||||||||
|ENG|Man City|@ Norwich|2012/13|9|17.2, [16.1, 18.4]|9 (101) <sup>∗</sup>|0 (0)|0 (0)|4 (59)|
|FRA|Marseille|@ Guingamp|2017/18|11|18.9, [17.9, 20.0]|2 (53) <sup>∗</sup>|0 (11)|0 (0)|8 (31)|
|GER|VfL Wolfsburg|@ Eintracht|2012/13|9|17.9, [16.5, 19.4]|8 (87) <sup>∗</sup>|0 (0)|0 (0)|7 (62)|
|ITA|AS Roma|Palermo|2012/13|15|25.6, [24.3, 26.9]|13 (85) <sup>∗</sup>|0 (0)|0 (0)|2 (14)|
|SPA|Barcelona|@ Celta|2020/21|8|22.3, [20.7, 24.0]|8 (91) <sup>∗</sup>|0 (0)|0 (0)|7 (60)|
|**Strongest**|**negative** **shifts** **in**|**each** **league:**||||||||
|ENG|Bournemouth|Tottenham|2018/19|10|6.0, [5.2, 6.9]|0 (5)|0 (0)|9 (58) <sup>∗</sup>|0 (0)|
|FRA|Paris St-Ger|St Rennais|2012/13|18|9.5, [8.6, 10.5]|0 (0)|17 (71)|16 (72) <sup>∗</sup>|0 (0)|
|GER|Eintracht|Stuttgart|2010/11|13|9.1, [8.5, 9.6]|0 (0)|5 (26) <sup>∗</sup>|13 (76)|0 (0)|
|ITA|AS Roma|Venezia|2021/22|20|13.1, [12.6, 13.8]|0 (0)|14 (79)|18 (70)|0 (0)|
|SPA|Getafe|Deportivo|2009/10|14|8.7, [7.8, 9.6]|0 (0)|13 (79) <sup>∗</sup>|11 (66) <sup>∗</sup>|0 (0)|



likely would have generated even more shot attempts if the game circumstances were more conducive to it, such as a tied game played at even strength. 

For the strongest negative adjustment in each respective league (last five rows of Tables 1 and 2), the team accumulated most of their offensive output while trailing by at least one goal and playing with at least a one-man advantage. As shown earlier in Figure 3, both of these settings typically associate with increased shot production. Consequently, our adjustment lowered these shot counts by projecting them onto a less favorable scenario – a tied game at even strength. The most significant reduction in shots occurred for Bordeaux in their 0–2 loss at home against Montpellier during the 2021/22 Ligue 1 season. Their actual shot count of 31 was adjusted down to 13.8 (95 % CI: [12.5 _,_ 15.1]). This was due to Bordeaux’s 31 shots all occurring after they gained a two-man advantage (11 vs. 9, with Montpellier receiving a second red card by the 45th minute) while already trailing 0–2. In such a setting, high shot production is expected, even more so than with a one-man advantage or a one-goal lead. Thus, when projecting onto a tied game with equal men, our adjustment led to a substantial reduction in shots for Bordeaux. As for the biggest negative adjustment in corner kicks, it occurred for Paris Saint-Germain (PSG) in their 1–2 loss to Stade Rennais. PSG trailed for most of the game and failed to capitalize on their opponent’s two red cards in the early stages of the second half. Sixteen of their corner kicks came while leading by at least one man but trailing by at least one goal, including 11 corners when up by at least two men. 

A notable feature for the negative shifts is that all 10 teams (five for shot attempts and five for corner kicks) spent at least half of the game with a manpower advantage, and six of these teams even had a two-man advantage at certain points. This led to our adjustment imposing an even heavier penalty on offensive outputs accumulated during such favorable conditions. In addition to the previously mentioned cases of Bordeaux and PSG attempting most of their shots when up by two men, we also have: Blackpool with 25 of their 26 shots when up by two men, Bournemouth with 7 out of 9 corner kicks, and Getafe with 9 out of 22 shots and 7 out of 10 corner kicks in their home game against Deportivo during the 2009/10 season. 

Please note that, despite the multiplicative nature of the projection mechanism, the strength of the adjustment in Tables 1 and 2 was measured by the absolute difference between actual and adjusted values, rather than by percentage change. As a result, the tables primarily highlight teams that both faced some extenuating circumstances _and_ had high actual outputs (e.g., 40+ shots for Real Madrid, Inter Milan, and AS Roma, or 15+ corner kicks for AS Roma and PSG). There may have been other teams that experienced higher percentage adjustments but smaller absolute shifts due to lower actual outputs. 

Finally, although the home-field factor had a smaller impact on offensive production compared to score and red card differentials, it still influenced the adjustments by awarding extra credit to away teams and applying downward adjustments to home teams. This is partially reflected in the fact that all 10 of the strongest negative adjustments 

> **14 —** A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data 

occurred for teams playing at home, and seven out of 10 strongest positive adjustments happened for teams playing away (for three other teams, the home-field effect was likely overshadowed by the more dominant influences of score and red card differential). 

#### **3.4.2 Season-long adjustment** 

Beyond the most drastic adjustments observed within individual games, in Tables 3 and 4 we present some of the strongest positive and negative shifts in season-long average offensive production – measured by shot attempts and 

corner kicks, respectively – across the 2008–2023 period for each league under consideration. 

One may notice that the strongest positive adjustments generally apply to the top-performing teams. Besides passing a domain knowledge sanity check – seeing worldrenowned dominant franchises such as Manchester City, Borussia Dortmund, Barcelona, Paris Saint-Germain, Juventus, and Inter Milan – several other key observations reinforce this pattern. First, these teams consistently generate high offensive output while in the lead, i.e., up by at least one goal. Tables 3 and 4 show all of them ranking #1 or #2 

**Table 3:** Individual seasons across 2008–2023 time span for each of the five European soccer leagues under consideration where a team experienced one of the strongest positive (first five rows) and strongest negative (last five rows) absolute shifts in their shot production per game due to our adjustment. Statistics and league rankings in several important contextual scenarios (leading/trailing, up/down in men) are also provided. 

|**League**|**Team**|**Season**|**Shot**|**s per** **game** **(rank)**|**Actu**|**al** **shots** **per** **g**|**ame** **(&** **rank)** **w**|**hen**|
|---|---|---|---|---|---|---|---|---|
||||**Actual**|**Adjusted,** **[95 % CI]**|**Up**<br>**1** **+** **goal**|**Down**<br>**1** **+** **goal**|**Up**<br>**1** **+** **man**|**Down**<br>**1** **+** **man**|
|**Strongest**|**positive** **shifts** **in** **ea**|**ch** **league:**|||||||
|ENG|Man City|2022/23|15.7 (#3)|17.9, [17.6, 18.1] (#1)|7.1 (#1)|1.5 (#20)|0.3 (#8)|0.3 (#3)|
|GER|Dortmund|2012/13|15.9 (#3)|18.0, [17.7, 18.3] (#2)|7.7 (#2)|2.8 (#13)|0.4 (#10)|0.9 (#1)|
|FRA|Paris St-Germ|2017/18|16.1 (#2)|19.3, [18.9, 19.6] (#1)|8.2 (#1)|1.7 (#20)|0.5 (#10)|0.8 (#1)|
|ITA|Inter Milan|2008/09|14.7 (#7)|16.7, [16.5, 16.9] (#3)|6.1 (#1)|0.6 (#20)|0.5 (#13)|0.5 (#8)|
|SPA|Barcelona|2009/10|15.9 (#3)|19.5, [19.1, 19.8] (#2)|8.6 (#2)|0.7 (#20)|0.4 (#17)|0.6 (#3)|
|**Strongest**|**negative** **shifts** **in** **e**|**ach** **league:**|||||||
|ENG|Bournemouth|2018/19|11.7 (#12)|11.3, [11.2, 11.5] (#16)|2.3 (#13)|4.5 (#5)|1.2 (#2)|0.0 (#18)|
|GER|Hannover 96|2015/16|11.2 (#13)|10.9, [10.8, 11.1] (#16)|0.9 (#18)|6.0 (#1)|0.4 (#6)|0.0 (#15)|
|FRA|Lorient|2021/22|11.7 (#10)|11.1, [10.9, 11.2] (#15)|1.1 (#20)|4.3 (#5)|1.6 (#1)|0.2 (#16)|
|ITA|US Pescara|2016/17|11.5 (#12)|10.3, [10.2, 10.5] (#17)|0.9 (#20)|6.4 (#1)|1.2 (#1)|0.2 (#10)|
|SPA|Las Palmas|2017/18|10.7 (#15)|10.4, [10.3, 10.5] (#20)|1.1 (#17)|4.6 (#3)|0.7 (#6)|0.1 (#17)|



**Table 4:** Individual seasons across 2008–2023 time span for each of the five European soccer leagues under consideration where a team experienced one of the strongest positive (first five rows) and strongest negative (last five rows) absolute shifts in their corner kicks per game due to our adjustment. Statistics and league rankings in several important contextual scenarios (leading/trailing, up/down in men) are also provided. 

|**League**|**Team**|**Season**|**Corne**|**rs per** **game** **(rank)**|**Actu**|**al** **corners** **per** **g**|**ame** **(&** **rank)**|**when**|
|---|---|---|---|---|---|---|---|---|
||||||**Up**|**Down**|**Up**|**Down**|
||||**Actual**|**Adjusted,** **[95** **% CI]**|**1** **+** **goal**|**1** **+** **goal**|**1** **+** **man**|**1** **+** **man**|
|**Strongest**|**positive** **shifts** **in** **ea**|**ch** **league:**|||||||
|ENG|Man City|2020/21|6.4 (#2)|7.6, [7.4, 7.9] (#1)|2.9 (#1)|0.8 (#20)|0.2 (#10)|0.1 (#6)|
|GER|Dortmund|2012/13|5.5 (#4)|6.3, [6.1, 6.5] (#3)|2.4 (#2)|1.0 (#17)|0.1 (#8)|0.3 (#1)|
|FRA|Paris St-Germ|2014/15|4.5 (#12)|5.6, [5.4, 5.7] (#4)|2.1 (#1)|0.4 (#20)|0.0 (#19)|0.0 (#19)|
|ITA|Juventus|2013/14|5.7 (#4)|7.1, [6.9, 7.3] (#1)|2.5 (#1)|0.4 (#19)|0.2 (#12)|0.1 (#10)|
|SPA|Barcelona|2012/13|5.9 (#7)|7.8, [7.5, 8.1] (#3)|3.3 (#1)|0.5 (#19)|0.3 (#9)|0.0 (#18)|
|**Strongest**|**negative shifts in ea**|**ch** **league:**|||||||
|ENG|Aston Villa|2015/16|4.4 (#15)|4.2, [4.1, 4.3] (#19)|0.3 (#20)|2.3 (#2)|0 (#16)|0.1 (#12)|
|GER|FC Cologne|2017/18|5.1 (#6)|4.8, [4.7, 5.0] (#11)|0.5 (#18)|2.7 (#1)|0.0 (#15)|0.2 (#8)|
|FRA|Valenciennes|2013/14|6.2 (#1)|6.0, [5.9, 6.2] (#5)|0.9 (#9)|2.9 (#1)|0.4 (#3)|0.0 (#11)|
|ITA|Siena|2009/10|5.7 (#6)|5.3, [5.2, 5.4] (#14)|0.3 (#20)|2.8 (#1)|0.4 (#2)|0.1 (#14)|
|SPA|Recreativo H|2008/09|5.3 (#9)|5.1, [5.0, 5.2] (#16)|0.4 (#20)|2.3 (#1)|0.6 (#3)|0.0 (#19)|



A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data **— 15** 

in that metric within their respective leagues for the given season. This reflects both the significant time they spend in the lead and their ability to maintain high offensive production while ahead – common traits of dominant teams. Second, these teams typically rank near the bottom in terms of shots taken while trailing (often #18–#20 out of 20 teams in most leagues, or #17–#18 out of 18 teams in the German Bundesliga), indicating how infrequently they fall behind – another hallmark of strong performance. Although not shown in the tables, we verified that teams with the largest positive adjustments also spent the least amount of time per game trailing (or, at worst, the third lowest), and the most time in the lead (or, at worst, the third highest). Conversely, the largest negative adjustments correspond to teams that consistently rank low in output generated while in the lead, instead producing the majority of their offensive output while trailing – when the game context is most favorable for such production. 

On the other hand, identifying consistent season-long patterns related to playing with a numerical advantage or disadvantage is more challenging. One could argue that, for shot attempts in particular (Table 3), there is a tendency for teams with the strongest positive adjustments to rank highly in shots generated while at a man disadvantage (most appear in the top three). Conversely, teams with negative adjustments tend to rank low in that same metric (typically #15 or lower out of 20 teams), while consistently ranking high in shots produced when up at least one man. That said, these patterns are less pronounced than in the case of score differentials, and there is no clear trend among positively adjusted teams when it comes to generating shots while holding a 1-man advantage. As for corner kicks (Table 4), there are no discernible patterns in teams’ season-long tendencies related to playing with a numerical advantage or disadvantage. 

This contrast between the impact of score differential and red card differential (i.e., playing with a 1-man advantage or disadvantage) is not surprising for one main reason: red card situations are generally much rarer than leading or trailing, as goals occur more frequently than player dismissals. Consequently, unlike scoring contexts, it is harder for red card situations to have a sustained impact over the course of an entire season. This contrasts with individual games where, as seen in Tables 1 and 2, red cards were present in nearly all matches most affected by our contextual adjustment. 

It is also noteworthy to examine changes in league rankings for the offensive output under consideration (shots in Table 3, corners in Table 4) before and after the adjustment. Note that, for these season-long tables, we specifically selected the strongest positive and negative 

adjustments that resulted in at least some movement up or down the rankings within that season (there were teams experiencing larger absolute adjustments, but with their ranking being unaffected). In eight out of 10 positive seasonlong adjustments across both tables, the team went on to win the league that season, with Dortmund’s 2012/13 campaign being the only second-place finish, albeit reflected twice (for both shots and corner kicks). These leaguewinners include teams like PSG, who originally ranked only #12 in corner kicks per game and rose to #4 post-adjustment, and Inter Milan, who moved from #7 to #3 in shot attempts per game. Conversely, eight out of 10 negative season-long adjustments involved teams that finished in the bottom two of their respective league, and therefore got relegated to a lower-level league. For example, Serie A’s US Pescara initially ranked #12 (out of 20) with 11.5 shot attempts per game, but their adjusted rate dropped to 10.3 (95 % CI: [10.2, 10.5]), lowering them to #17 – more accurately reflecting their frequent trailing game states and aligning better with their final standing. Even more notably, teams like Valenciennes, FC Cologne, and Siena, despite finishing in the bottom two of their league, initially ranked very highly in corner kicks per game; our adjustments substantially lowered their respective rankings in that statistic. 

Tables 5a and 5b provide a more formal summary of the season-long patterns discussed above. For both shots and corner kicks, one can observe a much stronger positive correlation between the adjusted statistics and the points earned, indicating better alignment with the final standings. Moreover, consistent with the intuition behind our adjustment mechanism, there is a stronger positive relationship between total shots/corners per game and shots/corners taken while leading in score (a setting more conducive to offensive production), and a stronger negative association with shots/corners taken while trailing (a less conducive setting, respectively). In contrast, the correlation patterns between offensive outputs and situations involving a manpower advantage or disadvantage are less clear. First, these correlations are much weaker than those related to scoring context – typically ranging from 0.05 to 0.20 in magnitude, compared to 0.25 to 0.90 for when a team is up or down by one or more goals. Second, the higher standard errors associated with these manpower-related correlations indicate a lack of consistency, resulting in inconclusive comparisons between actual and adjusted statistics. These findings support our earlier takeaways regarding season-long adjustment patterns: scoring context drives most of the observed shifts, as it reflects a more sustainable dynamic over the course of a season (i.e., stronger teams tend to lead more often, while weaker teams tend to trail). In contrast, manpower advantages or disadvantages play a less promi- 

> **16 —** A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data 

**Table 5:** Correlation of several statistical categories with the actual and adjusted shots (5a) and corners (5b), respectively. Averaged across five leagues and 15 seasons under consideration, with the standard error provided in parentheses. 

||**(a)** **For** **shots**||
|---|---|---|
|||**Correlation (SE) with**|
|**Statistic (per game)**|**Actual shots**|**Adjusted shots**|
|Points earned|0.718 (0.01)|0.787 (0.01)|
|Shots up 1+ goal|0.829 (0.01)|0.894 (0.01)|
|Shots down 1+ goal|−0.254 (0.02)|−0.370 (0.02)|
|Shots up 1+ men|0.190 (0.03)|0.129 (0.03)|
|Shots down 1+ men|0.051 (0.02)|0.089 (0.02)|
||**(b)** **For** **corners**||
|||**Correlation (SE) with**|
|**Statistic (per game)**|**Actual corners**|**Adjusted corners**|
|Points earned|0.603 (0.02)|0.737 (0.01)|
|Corners up 1+ goal|0.714 (0.02)|0.849 (0.01)|
|Corners down 1+ goal|−0.057 (0.03)|−0.252 (0.03)|
|Corners up 1+ men|0.151 (0.03)|0.093 (0.03)|
|Corners down 1+ men|0.059 (0.03)|0.090 (0.03)|



nent role, due to the irregular and less predictable nature of red card occurrences. 

All in all, we observe a pattern where the adjusted numbers align more closely with the actual final standings. 

This results from accounting for the game context in which offensive outputs are accumulated, thereby reducing the skew in statistics that may arise purely from tactical choices rather than from genuinely outperforming the opponent. As 



**Figure 7:** Paired _t_ -test _p_ -values and 95 % confidence intervals for the difference in root mean squared error (RMSE) when predicting final score differentials of future games within each season (individual points) and each league ( _y_ -axis) under consideration. Forecasts were generated using linear regression with two explanatory variables: the home and away teams’ statistics (shots or corners) up to the midpoint of the season, either left unchanged (“actual”) or adjusted using our proposed mechanism (“adjusted”). 

A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data **— 17** 

illustrated, certain teams may at times display misleadingly high or low values in metrics such as shot attempts and corner kicks, potentially resulting in misinterpretation. 

#### **3.4.3 Forecasting performance comparison** 

Figure 7 presents the results of the paired _t_ -test comparing forecasting performance when using adjusted statistics versus actual values in predicting score differentials. 

One may notice that forecasts based on actual statistic values consistently result in higher RMSE compared to those based on adjusted values, with all Holm-adjusted _p_ - values significant at the 0.01 level – and some even at the 0.001 level. That said, the confidence intervals for the true RMSE difference range from as low as 0.004 goals per game (English Premier League, shots) to only as high as 0.04 goals per game (Spanish La Liga, corners). When projected over a 380-game schedule – which corresponds to a single season in a 20-team league – this translates to a difference of just 1.52 to 15.2 total goals over a season, which may not be substantial from a practical standpoint. Furthermore, the absolute RMSE values for each season typically ranged between 1.3 and 1.9 goals per game – unsurprisingly high, given the simplicity of the linear regression model used for forecasting – suggesting that the observed per-game RMSE reductions of 0.004–0.04 are of marginal practical magnitude. Nonetheless, when considered alongside the statistically significant results discussed above, these findings still provide evidence of a stable discernible improvement that our adjustment provides. 

## **4 Conclusion & future work** 

We modeled teams’ offensive production – such as shot attempts and corner kicks – as a function of various factors that influence the likelihood of employing certain tactics. The model that achieved the best balance between goodness-of-fit and out-of-sample predictive performance was Negative Binomial Generalized Additive Model (GAM) with smoothing splines, in which we binned extreme values for score differential (treating all differentials beyond +2 the same, and beyond −2, respectively), red card differential (beyond +1 and −1, respectively), and game minute (beyond 45, i.e., extra time). We also confirmed via hypothesis testing procedures that each variable in the baseline set of five factors – score differential, red card differential, home indicator, win probability differential, and game minute (including a half indicator) – was statistically significant and should be retained. 

The nature of the effects observed in our analysis was largely intuitive. Notably, the impact of score differential on offensive output exhibited a predictable decreasing pattern as the differential gradually shifted from −3 to 3. The influence of red card differential was even more pronounced in terms of practical significance, revealing a strong negative trend as the differential increased. These effects align with the understanding that teams in the lead tend to adopt a more conservative approach to protect their advantage and secure the valuable three points for a win, whereas teams down by at least one player are often forced to play defensively due to their numerical disadvantage. The pre-match win probability differential showed a strong positive association with offensive output, reinforcing the notion that stronger teams tend to outperform their opponents. Additionally, the home factor consistently had a positive, albeit relatively modest, effect on a team’s offensive production. All of these findings are consistent with existing literature, including [X, (Lopez et al. 2018; Harville 1977)]. 

Incorporating the game minute variable directly into the model allowed us to explore several research questions that would not have been possible with aggregate data alone. First, it helped illustrate trends in offensive output as the half progresses. Specifically, it showed a steady increase in offensive activity during the first 5 min of a half, with the starting level of activity being higher in the second half. This could be attributed to both teams calibrating their respective offenses for the opponent early in the first half, and getting back into the flow of the game early in the second half, albeit already having calibrated their offense (hence the higher baseline activity level). Afterward, the offensive activity level remained relatively stable. Secondly, we used the game minute variable to test several hypotheses driven by domain knowledge and intuition. For example, one might expect that as time expires, the trailing team becomes more desperate to try and score, while the leading team becomes more conservative in order to hold on to the lead. This would be captured by an interaction between score differential and game minute. When testing the significance of this interaction, we found that there is very limited evidence to support this hypothesis. In the few cases where the interaction was found statistically significant, the results did align with the intuition, but such cases were rare (out of 75 tests). We also tested interactions between other key factor variables, as several plausible hypotheses could be explored that way. However, we found even less evidence for these effects than for the interaction between game minute and score differential. 

In our statistical adjustment process, we projected each team’s offensive performance in a selected statistical 

> **18 —** A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data 

category onto a baseline scenario of a tied home game at even strength, aiming to provide a fairer representation of offensive production given the game context. This adjustment involved giving greater weight to statistics accumulated during periods when a team was leading and/or playing with fewer men, as these situations are generally less favorable for offensive output. Conversely, statistics were adjusted downward for periods when a team was trailing or had a numerical advantage. When examining the largest adjustments to team performances – both in individual games and season-long per-game averages – we observed a clear tendency for teams to be rewarded for generating significant offensive output while leading by at least one goal. In contrast, uneven player distributions (e.g., 9 or 10 players vs. 11) played a more prominent role at the singlegame level, as it is uncommon for teams to experience such scenarios consistently over an entire season. Nonetheless, some season-long patterns of offensive outputs generated while up/down in men were still identifiable, just not as consistently as when it came to the score differential scenarios. 

Note that our statistical adjustment aimed to make team performance comparisons in categories like shot attempts and corner kicks more reflective of relative levels of play. For example, in season-long adjustments, it helped align team rankings in shot attempts and corner kicks more closely with their final standings by points – benefiting stronger teams and downgrading weaker ones. This adjustment accounted for game context, where top teams tend to lead and bottom teams tend to trail for most of the time, thus correcting for potential skew in raw game totals. Notably, it addressed cases where bottom-two teams by points ranked near the top of the league in corner kicks per game, which could otherwise be misleading. Moreover, as a more objective way to quantify the improvement gained from our adjustment, we demonstrated that team per-game averages based on adjusted statistics outperform those based on actual statistics when used to forecast final score differentials of future games. Although not overly large from a practical standpoint, the improvement was consistent enough to be deemed statistically significant, with the findings replicated across all five leagues under consideration. 

As for the single-game adjustments, they also tended to align well with the final game outcome – teams with positive adjustments generally won, while those with negative adjustments tended to lose. Beyond merely reflecting the tendency to play with a lead or deficit, these cases often involved more extreme circumstances, such as teams gaining a 1- or 2-man advantage (or suffering a corresponding disadvantage). For example, Getafe lost 0–2 at home to Deportivo in their 2009/10 match despite outshooting 

them 22–8 and earning 14 corner kicks to the opponent’s 3. However, Getafe played with at least a 1-man advantage for most of the game, and a 2-man advantage for the final 30+ minutes, skewing the raw numbers. Our adjustment reduced their shot count to 12.8 and corners to 8.7, while Deportivo’s adjusted figures rose to 14.6 and 7.8, respectively – offering a more context-aware comparison that accounts for Deportivo’s shorthanded status while also holding a lead for most of the game. Similar adjustments occurred in other matches: 

- Stade Rennais’ 2–1 win over Paris Saint-Germain in 2012/13, where PSG led 23–8 in shots and 18–3 in corners, but the adjustment reversed shots to 12.3–16.2, while shrinking the corner difference (9.5–5.9). 

- Montpellier’s 2–0 win over Bordeaux in 2021/22, despite trailing 32–7 in shots and 11–4 in corners; adjustments brought the numbers to 13.8–11.5 and 5.0–6.1, respectively. 

- Bayern Munich’s 4–0 win against Stuttgart in 2020/21, which initially showed just a slight 15–12 edge in shots and a 1–3 deficit in corners. After adjustment, shots became 31.8–9.6 and corners – 1.7–2.5. 

These examples highlight the main goal of our adjustment, which is to make raw match statistics like shot attempts and corner kicks less misleading and more reflective of the relative quality of play. Without such context, one might incorrectly attribute a match outcome solely to luck, ignoring the fact that such statistical imbalance is often due to tactical dynamics driven by game state. 

Returning to the main motivating example of the 2022 FIFA World Cup Quarterfinal between France and England: even when accounting for France having spent a significant portion of the game with a 1-goal lead and adopting a more defensive style, the extent to which England numerically outperformed France during that period – 11 to 1 in shots, 5 to 0 in corner kicks – cannot be fully explained by contextual factors alone. Applying even the most extreme adjustment for leading or trailing by one goal (see Figure 6), would project England to have 14.35 shots (5 + 11 × 0.85) instead of their actual 16, and France to have 8.15 shots (7 + 1 × 1.15) instead of their actual 8. This reduces England’s statistical lead by only about two shots. The fact that England’s lead in shots remains substantial even after adjustment, in our view, actually strengthens the argument that, despite having lost the game, they might have played more dominantly and might have gotten unlucky. This illustrates that even when our adjustment does not drastically alter the relative performance of the teams, it still provides 

A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data **— 19** 

a fairer baseline for comparison – enabling more confident conclusions about which team truly controlled the game. 

For future work, a promising direction would be to model the actual quality of shot attempts generated in various game contexts, as not all shots are equally likely to pose a significant threat to the opponent. To this end, we plan to use expected goal values ( _xG_ ) (Whitmore 2023) as our measure of offensive output. This would allow us to analyze how the quality of scoring opportunities is influenced by game context, with the potential for subsequent statistical adjustments. Whether a similar adjustment approach is appropriate in this setting will depend heavily on the presence of a consistent monotonic relationship between game context and _xG_ output, ensuring that the adjustment is meaningful. For example, projecting performance onto a neutral context (e.g., tied score or even strength) is only valid if shorthanded teams with a lead consistently generate lower _xG_ values, and vice versa for teams that trail and/or have manpower advantage. 

Lastly, it is important to clarify that, although we referenced a World Cup elimination game as an example, this study primarily focuses on national club leagues, where elimination games – at least in the same sense as the World 

Cup’s knockout stages – do not exist. In these leagues, points are awarded based on match outcomes: 3 points for a win, 1 point for a draw, and 0 points for a loss. The league winner is determined by the total number of points accumulated over the course of the season. With this context in mind, examining competitions that rely on binary outcomes (win/loss) or score differentials to determine advancement would be a logical extension of this research. Such competitions include not only the World Cup knockout rounds, but also the elimination stages of the Champions League, Europa League, and tournaments like the Football Association Challenge Cup (FA Cup). 

## **5 Appendix** 

### **5.1 Model comparison: Poisson, Negative Binomial, Zero-Inflated Poisson** 

Besides the DHARMa diagnostics and leave-one-season-out calibration plots, we also carried out an AIC/BIC comparison of count-response models under consideration (Tables 6 and 7). 

**Table 6:** AIC values (with model complexity in parentheses) comparing all count-based models under consideration across all five leagues. Best-performing models marked in **bold** . 

|||**Shot** **attempts**|||**Corner** **kicks**||
|---|---|---|---|---|---|---|
|**Leagues**|**Poisson**|**Negative** **Binomial**|**Zero-Inflated Poisson**|**Poisson**|**Negative** **Binomial**|**Zero-Inflated Poisson**|
|Bundesliga|695,012.5 (74)|693,432.3 (71)|**,.()**|344,286.1 (69)|343,844.3 (68)|**,.()**|
|La Liga|703,460.4 (81)|702,608.5 (78)|**,.()**|373,223.2 (71)|372,732.8 (73)|**,.()**|
|Ligue 1|790,313.9 (81)|788,846.0 (78)|**,.()**|406,397.3 (66)|405,661.2 (66)|**,.()**|
|Premier league|722,807.5 (87)|720,360.4 (82)|**,.()**|380,695.0 (74)|380,089.1 (75)|**,.()**|
|Serie A|813,704.8 (80)|812,576.1 (76)|**,.()**|414,359.2 (70)|413,629.8 (68)|**,.()**|



**Table 7:** BIC values (with model complexity in parentheses) comparing all count-based models under consideration across all five leagues. Best-performing models marked in **bold** . 

|||**Shot** **attempt**|**s**||**Corner** **kicks**||
|---|---|---|---|---|---|---|
|**Leagues**|**Poisson**|**Negative** **Binomial**|**Zero-Inflated Poisson**|**Poisson**|**Negative** **Binomial**|**Zero-Inflated Poisson**|
|Bundesliga|695,873.0 (79)|**,.()**|694,352.4 (106)|345,090.0 (69)|**,.()**|345,006.2 (104)|
|La Liga|704,414.3 (81)|**,.()**|703,623.9 (126)|374,053.6 (71)|**,.()**|373,868.1 (99)|
|Ligue 1|791,269.0 (81)|**,.()**|789,915.3 (124)|407,178.0 (66)|**,.()**|406,737.4 (94)|
|Premier league|723,826.5 (87)|721,320.0 (82)|**,.()**|381,562.0 (74)|**,.()**|381,258.4 (98)|
|Serie A|814,655.2 (80)|813,475.3 (76)|**,.()**|415,189.4 (70)|**,.()**|414,665.8 (98)|



> **20 —** A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data 

### **5.2 Nature of effects: initial smoothing splines GAM fit** 

##### See Figure 8. 



**Figure 8:** Nature of effects for score differential, red card differential, win probability differential and game minute in 1st/2nd halves on shot attempts (left) and corner kicks (right) in the baseline Negative Binomial Generalized Additive **smoothing splines** model fitted to 15 seasons (2008–2023) across five major European soccer leagues. The _y_ -axis is on the scale of linear predictor (log-response). 

A. V. Skripnikov et al.: Adjusting soccer team production for game context via minute-by-minute data **— 21** 

**Acknowledgments:** The authors are grateful to the host institution for providing summer research funding. **Research ethics:** Not applicable. 

**Informed consent:** Not applicable. 

**Author contributions:** All authors have accepted responsibility for the entire content of this manuscript and approved its submission. 

**Use of Large Language Models, AI and Machine Learning Tools:** The authors used ChatGPT to edit the text for clarity, grammar, syntax and flow, but made sure to subsequently review the text themselves and confirm the actual meaning was preserved. 

**Conflict of interest:** Authors of this work confirm that there are no known of interest to disclose. 

**Research funding:** None declared. 

**Data availability:** Will be made publicly available via Github. 

## **References** 

Akaike, H. (1998). Information theory and an extension of the maximum likelihood principle. In: _Selected papers of hirotugu akaike_ . Springer, New York, pp. 199−213. 

Boshnakov, G., Kharrat, T., and McHale, I. G. (2017). A bivariate Weibull count model for forecasting association football scores. _Int. J. Forecast._ 33: 458−466,. 

Cefis, M. and Carpita, M. (2025). A new xG model for football analytics. _J. Oper. Res. Soc._ 76: 1−13,. 

Cefis, M. (2022). Football analytics: a bibliometric study about the last 

decade contributions. _Electron. J. Appl. Stat. Anal._ 15: 232−248. 

Edwards, J. and Archambault, D. (1979). The home field advantage. In: 

_Sports, games, and play: Social and psychological viewpoints_ . Lawrence Erlbaum Associates, Hillsdale, NJ, pp. 409−438. 

_ESPN: France 2-1 England Commentary_ . (2024). ESPN. https://www.espn .com/soccer/commentary/_/gameId/633846 (Accessed 29 April 2024). 

FBref. (2024). _Expected Goals (xG) Model Explained_ . https://fbref.com/en/ expected-goals-model-explained/ (Accessed 10 October 2024). Hartig, F. and Hartig, M. F. (2017). Package ‘dharma’. _R Package_ 531: 532. 

Kempton, T., Kennedy, N., and Coutts, A. J. (2016). The expected value of possession in professional rugby league match-play. _J. Sports Sci._ 34: 645−650,. 

Lopez, M. J., Matthews, G. J., and Baumer, B. S. (2018). How often does the best team win? A unified approach to understanding randomness in North American sport. _Ann. Appl. Stat._ 12: 2483−2516,. 

Macdonald, B. (2012). An expected goals model for evaluating NHL teams and players. In: _Proceedings of the 2012 mit sloan sports analytics conference_ . 

McCullagh, P. (2019). _Generalized linear models_ . Routledge, New York. Mead, J., O’Hare, A., and Paul, M. (2023). Expected goals in football: Improving model performance and demonstrating value. In: _PLOS ONE 18.4_ . Public Library of Science, pp. e0282295, https://journals. plos.org/plosone/article?id=10.1371/journal.pone.0282295 (Accessed 29 April 2024). 

Schwarz, G. (1978). Estimating the dimension of a model. _Ann. Stat._ : 461−464, https://doi.org/10.1214/aos/1176344136. 

Shapiro, S. S. and Wilk, M. B. (1965). An analysis of variance test for 

normality (complete samples). _Biometrika_ 52: 591−611,. 

Sosa, F. G. R. (2015). La identidad del italiano en la evolución del catenaccio. _Impetus_ 9: 135−142,. 

StatsBomb. (2024a). _Examples of Possession Value Models_ . https:// statsbomb.com/soccer-metrics/possession-value-modelsexplained/ (Accessed 10 October 2024). 

StatsBomb. (2024b). _xPass 360: Upgrading Expected Pass Models_ . https:// statsbomb.com/articles/soccer/xpass-360-upgrading-expectedpass-xpass-models/ (Accessed 10 October 2024). 

_The Selenium Browser Automation Documentation_ . (2024). Selenium. https://www.selenium.dev/documentation/ (Accessed 21 June 2024). 

- Trequattrini, R., Del Giudice, M., Cuozzo, B., and Palmaccio, M. (2016). Does sport innovation create value? The case of professional football clubs. _Technol., Innovat. Educ._ 2: 1−15,. 

- Van Roy, M., Robberechts, P., Decroos, T., and Davis, J. (2020). Valuing on-the-ball actions in soccer: a critical comparison of XT and VAEP. In: _Proceedings of the 2020 AAAI Workshop on AI in Team Sports_ . AAAI (Association for the Advancement of Artificial Intelligence), pp. 1−8. 

- Whitmore, J. (2023). _What is Expected Goals?_ The Analyst. Available at: https://theanalyst.com/2023/08/what-is-expected-goals-xg/. 

Wood, S. N. (2017). _Generalized additive models: an introduction with R_ . Chapman and Hall/CRC, Boca Raton, FL. 

Yurko, R., Ventura, S., and Horowitz, M. (2019). nflWAR: a reproducible method for offensive player evaluation in football. _J. Quant. Anal. Sports_ 15: 163−183,. 

Harville, D. (1977). The use of linear-model methodology to rate high 

school or college football teams. _J. Am. Stat. Assoc._ 72: 278−289,. 

Holm, S. (1979). A simple sequentially rejective multiple test procedure. _Scand. J. Stat._ : 65−70. 

**Supplementary Material:** This article contains supplementary material (https://doi.org/10.1515/jqas-2024-0162). 


