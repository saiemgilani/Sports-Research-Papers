<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2021/2021 - Increasing the shot at a quality draft-decision A Bayesian approach to improve predicting three-point accuracy translation in the NBA Draft - Unknown Authors.pdf -->



# **Increasing the shot at a quality draft-decision – A Bayesian approach to improve predicting three-pointaccuracy translation in the NBA Draft** 

Tobias Berger | Friedrich-Schiller-Universität Jena | tobias.berger@gmx.net Frank Daumann | Friedrich-Schiller-Universität Jena 

## **1. Introduction** 

The NBA Draft is a mechanism to regulate competitive balance of a sports league. Its ambition - to give the worst franchises a chance to acquire young prospects, improve longterm and close the on-field talent gap to better teams - is clear and noble. In theory the policy strengthens the NBA’s product in many ways. It is supposed to distribute league-entering player capital equally, and by this dynamic improve the quality of play [14, 32] while increasing the competitive balance among all competitors by raising the uncertainty of outcome on a game and season-level . This has been deemed an important goal for sports leagues for a long time [63]. The potential benefits of the mechanism should lead to increasing attractiveness of the entertainment product the NBA offers. 

The crux of these theoretical outcomes is the nature of the mechanism itself. For the described dynamics to work, all NBA managers need to constantly seize the opportunity the NBA Draft provides them with. Unfortunately, this is an incredibly complex expectation to have for the acting decision-makers. In the draft environment, choices are not made within a known variance, but among widely unknown outcomes. The policy can therefore be treated as a proxy for decisions under uncertainty [51]. Within this complex process decisionmakers ultimately do not only have to judge who the best prospect is at the moment of the draft, but also who will develop into the most valuable player in the future, while additionally (among considering other external factors) forecasting the direction in which the sport itself is moving in the long-term. This provides much room for individual failures due to personal misjudgments or misconceptions by the managers, and leaves the door open for systematic errors on a leaguewide level caused by collective decision-making biases [64]. 

Over the past few decades many efforts have been made to improve draft-decision-makingquality and reach the goals the draft mechanism intends to fulfill. Still, the mechanism does not produce such positive outcomes constantly, even though it would be beneficial for the entire league. Research has shown that it does not pay off to solely build up a franchise through the draft [11, 54]. Meanwhile, the NBA historically has performed as the most 



1 



imbalanced of all the North American sports leagues [70]. At least to some extend this state of the association can be based on the rather poor draft-decision-making-quality next to salary cap-induced factors [74]. 

We identified the increase of managerial decision-making-quality within the dynamics as a crucial component to fulfill the aims of the fundamental policy proposal. Initial judgements in talent evaluation and future predictions of performance for the potential draftees and the environment they will play in need to be improved in their accuracy and reliability to reduce uncertainty inside the complex choice mechanism and thus, provoke better overall results. 

This paper aspires to reach this goal by examining one of the key components of the sport more closely – shooting the basketball from distance. We will explore league-wide threepoint scoring tendencies and investigate in which direction the sport has developed and will progress. Afterwards we strive for improving the prediction of shooting-translation from the college to the professional level by implementing a Bayesian approach to pre-draft metrics and including a play-by-play-based metric into modeling. Being able to project an important basketball skill more accurately should improve the individual managers player evaluations and, in the end, increase the draft-decision-making-quality on a leaguewide level. The results will provide a new baseline for the judgement of draft prospects within one of the most important performance facets of the sport. 

## **2. Background and related literature** 

### **2.1. The NBA Draft policy and its shortcomings** 

The draft as a regulating sports mechanism has been an integral part of all North American major leagues and is investigated in many environments. Researchers mostly analyzed the structure as well as the decision-making within the process or look for inefficiencies from an economic standpoint. Papers on the draft, can be found for hockey [e.g. 24, 73], baseball [e.g. 20, 69], football [e.g. 34, 49] and basketball in the WNBA [e.g. 31, 33]. 

The draft policy of the NBA was firstly discussed from a strictly legal perspective. Over half a century ago, the mechanism was debated focusing on antitrust laws, labor rights and its general validity [e.g. 2, 18, 21]. It took a while until early structural criticism was raised, because it failed to deliver the intended league-wide outcomes concerning competitive balance through equal talent distribution. As Burkow and Slaughter (1981) pointed out team success was more dependent on the managerial decision-making qualities in other areas such as personnel hiring and player trading [19]. Drafting did not seem to level the playing field as much as it was supposed to, since most of the deciding organizations seem to lack proper talent evaluation abilities [12]. Stronger teams tend to profit more from the policy than bad ones, which is completely contrary to its intentions [11]. Consequently, research even advices against the draft policy as league-wide tool to strengthen competitive balance. Historical results show, there are not enough competent decision-makers to implement the 



2 



mechanism well enough to produce those favorable outcomes for the entire association constantly [55]. 

### **2.2. The NBA Draft dynamic as a proxy for decisions under uncertainty** 

The reasons for these policy shortcomings of the NBA Draft are manifold but can be mostly be attributed to the ‘human judgement-factor’ in many parts of this particular decisionmaking equation. The decision problem of the entire mechanism is clear. Every franchise strives to optimize the opportunity its current draft position provides them with by selecting the best talent available. Talent in this environment can be seen as a mixture of mostly oncourt but also off-court benefits the prospect will generate for his new employer. This value allows the drafting organization to maximize financial and sportive utility following classical economic theory [25, 41]. The process towards solving this problem is immensely complex due to the hurdles the decision-makers must master. Within this straight-forward setup a draft choice requires NBA front offices to give their judgement in two main areas which both present huge levels of uncertainty, as probabilities of decision outcomes in this framework can only be roughly estimated and are mostly unknowable [78]. 

One the one hand, a manager needs to evaluate the talent level of all the players at the moment of the draft, while factoring their potential development in the future. On the other hand, the direction of the entire sports, as an underlying environment the athlete needs to perform in, must be correctly anticipated as well. The NBA has come a long way over the past two decades by installing more sophisticated processes around these interwoven dynamics. Especially with the recent emergence of sports analytics huge steps have been taken towards a more scientific approach of the sport to better understand the entire discipline and reduce uncertainties [1, 46]. The evaluation of player talent along the triangulation of eyes (e.g. scouting, personal workouts), ears (e.g. personal interviews, medical records exploration, further background research) and numbers (e.g. anthropometric measurements, high school and college performance metrics) has become much more sophisticated [8], while leaguewide playing trends can be discovered and followed more closely than ever before ([68]. 

However, judging individuals is extremely difficult because basketball as a sport has not been ‘solved’ yet. It is hard to isolate the personal impact of one player in a dynamic team discipline [48]. And even if managers knew what exact data to look at, how to weigh all the information correctly to anticipate career arcs of players perfectly, there would probably still be discussions about career values of prospects arguing about peak versus average performance-level, relative value or longevity as potentially driving utility dimensions [e.g. 7, 72]. 

At some point the analysis of those factors simply comes down to taste, preferences, and the decision-maker’s philosophy on how the sports of basketball should be played. These clear aspects of judgement, which are defined as ‘the set of evaluative and inferential processes 



3 



that people have at their disposal and can draw on in the process of making decisions’ [43, p. XV] open up the entire process to the realm of classical decision-making-quality-lowering fallacies and biases. Many of those have been investigated in the NBA Draft environment to either reduce uncertainty or uncover hidden systematic errors. Basketball draft research has covered nationality bias [54] as well as recency and availability bias [12, 17, 38]. Additionally, it was shown that age and favorable positional length as proxies for potential [4, 13, 29] get misjudged constantly, while certain boxscore statistics do not translate as smoothly from the amateur to the professional level as one would expect [e.g. 22, 31, 65]. 

### **2.3. The NBA three-point revolution** 

Arguably the most influential rule change in the history of basketball was the implementation of the three point-line. After much experimentation in other basketball environments the three-point line was introduced to the NBA in 1979. This rule change was a clear reaction to the dominance of the bigmen in early decades of the sport. It was intentionally designed to give smaller players better opportunities to score, while making the game more enjoyable to watch for the fans [30]. 





Figure 1. Leaguewide Average of 3PApG over time in NBA and NCAA. 

At first the league was slow to react to this change. Only a few players possessed the shooting skills to use this new offensive weapon constantly, while managers and coaches had not fully grasped the advantages the additional way of scoring does provide. But as more athletes were brought up with the three-point line being present for their entire basketball upbringing shooting-competence and the acceptance of the three-pointer rose in the NBA [27]. In a trickle-down fashion this change affected college basketball as well, which introduced the line in 1986. 



4 





Figure 2. Leaguewide Average 3P% over time in NBA. 

With the general skill level of the players catching up, the era of sports analytics led to shooting from distance becoming even more fashionable. Building on the ‘Moneyball’-ideas early introduced by the Oakland As in baseball [45], which center around the use of data to find exploitable inefficiencies within the sport [e.g. 1, 46], the three-pointer as a strategic option was finally recognized as an excellent driver for efficient basketball offenses [57]. Backed up by numbers, managers and players not only started to realize the huge benefit the potential extra-point the shot grants. They also recognized the positive effect the threat of such attempts alone produced, forcing opposing defenses to space out, opening up room for other basketball actions as well. The entire geometry of the sport changed [e.g. 27, 67]. 



Figure 3. Leaguewide Average Offensive Rating over time in NBA. 



5 



The strategic and stylistic innovation the extensive use of the three-pointer has caused within sport is enormous. The increased application of sports analytics only fuels this development to this day. Currently, some of the arguably most influential players of the sport make more three-pointers over a season than entire teams did over a year just three decades ago [6]. This trend should last, since it has led to a vast increase in offensive efficiency, which is one key factor in winning basketball games [57]. With the 2010s Golden State Warriors and Cleveland Cavaliers disproving the old NBA sentiment, that teams relying on the jump shot will never win championships [76] and no diminishing rule-changes on the horizon, the three-point-movement is here to stay. Thus, the league-wide demand for competent threepoint shooters is increasing. 



Figure 4. Leaguewide 3PA trends by player height in NBA [23]. 

This development becomes especially obvious by looking at functional demands for different positions. The tallest of players of the NBA used to have the simple job of converting scoring opportunities close to the basket. Since the start of the analytics era, most teams want all their players to be able to shoot the three, making the ability to hit open triples one of the most valuable individual basketball traits no matter the height or position [23]. As we can see everybody is supposed to shoot more. Curiously, NBA front offices seem to be slow to react to this trend. They arguably still draft more non-shooting bigmen in higher spots than they should [58], which potentially illustrates rigid underlying management structures and a potential status-quo-bias. 

### **2.4. Three-point shooting as an NBA Draft trait** 

Due to the current league environment and general playstyle, we have identified three-point shooting as a valuable skillset-element for every NBA player. Experts forecast this association-wide shooting-trend to last since an increasing number of athletes and teams is 



6 



adapting [e.g. 16, 27, ] (e.g. Nasru, 2017). Consequently, this trait becomes an increasingly interesting pre-draft ability to evaluate. Especially at the moment, it is often deemed the swing skill for players that can make or break successful careers [35]. Identified and correctly projected, the accurate judgement of a prospects three-point shooting skills can result in better draft decision-making. On the one hand, drafting underrated elite long-range shooters can setup a team for a decade of success [e.g. 52, 53]. On the other hand, simply avoiding players who fail to meet their shooting projection and turn out to be less of a talent as anticipated for that matter indirectly helps a franchise as well [e.g. 44, 47]. Either way, the projection of this ability is key to be able to seize the opportunities the NBA draft provides for the franchises. 

However, predicting the translation of pre-draft three-point shooting towards NBA performance in this category is rather complex and difficult because many factors need to be considered. From a player’s internal perspective, managers need to judge the shooting technique [e.g. 37, 42] while considering the prospect’s mental and physical capabilities [e.g. 3, 59]. External variables like adaption to the greater NBA shooting distance<sup>1</sup> , differing level of play around the player, varying role within the team system, change of player position as well as potentially shifting degrees of difficulty of the types of three-point attempts a prospect is taking, complicate a clean projection. Due to differing circumstances and the uncertainty such external factors produce, even smart forecasts for NBA performance based on pre-draft indictors can never be fully accurate [56]. 

Additionally, within these pre-draft components several biases can cloud judgement. Recency, availability, or small sample size-biases can negatively influence evaluators, if a prospect has a hot shooting streak in the march madness tournament [12]. Overconfidence might also lead to inaccurate projections on three-point ability, as managers falsely believe that they will teach a non-shooting player how to hit more threes, or on the contrary, irrationally disregard a solid shooter because of their unorthodox throwing motion [64]. To avoid some of these biases, analytics would suggest blocking out as much subjective noise as possible by projecting shooting and its potential development using a model based on tangible, historic data. 

## **3. Methodology** 

### **3.1. Data** 

The website ‘Hoop-Math’ was used as a primary data resource [36]. Their data base allowed us to capture the shooting statistics of every NCAA athlete and their respective schools from 2012 to 2020 (N = 47408). We isolated the drafted players from this sample and were able 

> 1 The NBA line (7.24m) is farther back than the one in college and FIBA basketball (both 6.75m) [77]. 



7 



to match further, missing shooting data from the stats-portal ‘Barttorvik’ as well as scraping and adding the NBA performance data of all draftees from ‘Basketball-Reference’ [5, 6]. 

Consequently, the constructed data set includes pre-draft information (e.g. name, college, position, age, years of pre-draft-experience), detailed pre-draft shooting data (e.g. shot attempts and makes from several distances) based on play-by-play information and detailed post-draft performance data (e.g. shot attempts and makes from several distances) of all college players who were drafted between 2012 and 2020 (N = 386). 2012 became the natural starting point for our records since college basketball play-by-play data and resulting deeper statistics for full draft classes were only available to us from this point on. 

The ongoing nature of the dataset is an important limitation we want to point out. While the players pre-draft statistics cannot change anymore, their post-draft numbers are still developing as most of the players are currently active in the league. The data was scraped in June 2020 and does not include the most recent continuation of the NBA season after an intermission of the 2019/20 season, induced by the COVID-19 pandemic. 

We used the ‘R’-software to prepare and analyze the data. For empirical Bayes binominal estimations, we relied on the “ebbr”-package within this program [62]. 

### **3.2. Modeling three-point accuracy translation by using different shooting measures** 

Predicting the translation of three-point accuracy from the college to the NBA level is difficult. There are many context variables (e.g. pre-draft team tactical system, teammates, competition) that would need to be included into a more holistic approach. We chose to disregard these factors completely to simplify our approach as much as possible and reduce the amount of potential statistical noise around the two introduced metrics. Consequently, we approached shooting-ability simply as a measure of how many of the three-pointers a player attempted (3PA) he converted (3PM). 

Introducing shooting as this basic measure of volume and efficiency already poses some difficulties. Research has shown that three-point percentage (3P%) as a metric stabilizes at around 750 attempts. Hence, it needs a certain kind of volume until this statistic becomes a reliable measure for a player’s shooting competence [15]. This creates a draft projection dilemma, because almost no potential draftee plays enough official games to be able to offer such a dependable pre-draft sample-size. Especially since drafted players have been getting a lot younger over the past few decades [79]. 

Current publicly available models try to account for this complication by factoring in other potentially useful dimensions that contribute to measuring shooting ability. Regular threepoint metrics in these models are usually considered with raw percentages and a shooting volume estimate based on three-point makes or attempts on a ‘per-40-minutes-basis’ to be able to compare talents with different playing times. Pre-draft free-throw-percentage (FT%) is a popular addition in such designs as well. It has been shown that including free-throw percentage in models significantly improves projections of NBA three-point accuracy, even 



8 



though the shots seem to differ a lot in terms of distance or game circumstance [e.g. 28, 39, 40, 71]. Despite the differences, it seems logical, that free-throw percentage contributes to the projection of three-point skills. In its core it is only capturing another throwing-activity on the court and is therefore just an additional, interesting measure of ‘shooting touch’, while increasing the data basis the system can gather meaningful information from. 

In our later modeling we will add two-point-jumper accuracy (2PJ%) as another shooting metric to our prediction attempt with the same logic. We assume two-point jumpers require a draftee to apply many of the same biomechanical capabilities that are needed to hit a threepointer or a free-throw. Even though the game context differs a lot in the given situations, all scoring attempts are usually executed with a similar shooting technique or style and require a level of ‘shooting touch’ to successfully put the ball into the basket [80].  Hence, two-pointjump shooting could also be a reliable measure of overall shooting-ability and should therefore contribute to the prediction of three-point competence in the NBA. This hypothesis will be tested. 

### **3.3. Adding a Bayesian approach to identify true pre-draft shooting competence more accurately** 

To ‘apply a Bayesian approach’ usually means to use statistical techniques relying on ‘Bayes theorem’, which assigns a rather subjective treatment to probabilities and handles unknown information probabilistically [10]. Taking a Bayesian perspective when dealing with statistical problems has become popular in many fields because it provides several advantages. For the discipline of sports science and analytics particularly - facing a data influx rapidly growing in volume and complexity - it proves to be beneficial especially because it allows to: “ 

- _incorporate expert information or prior believes, […]_ 

- _use Bayesian learning where the current posterior distribution becomes the prior for future data, […]_ 

- _model complex problems, […]_ 

- _deal more effectively with small dataset using prior information to improve the parameter estimates, […]_ 

- _make predictions taking into consideration uncertainty”_ [66, p. 2] 

among other listed benefits. Various applications of Bayesian methods for basketball shooting problems and modeling can be found [9, 26, 60, 75]. In our opinion, such an approach should be favorable for pre-draft three-point shooting as well because it allows to add more context and potentially assign more meaning to this measure by using an empirical Bayesian shrinkage towards a Beta prior based on historical data. This technique has been applied successfully to produce a more well-informed assessment of baseball’s batting average, an estimate of a player’s hitting ability [61]. Statistically speaking, the logic of batting average is very similar to three-point-shooting in many ways. This approach has therefore already been applied to pre-draft three-point percentage and provided interesting 



9 



results in the basketball realm as well [50]. With our analysis, we will build on this first modeling attempt and hope for even more accurate results by adding more informed data, factoring in two-point-jumper accuracy. 

## **4. Analysis** 

### **4.1. Empirical Bayes estimation of pre-draft three-point percentage** 

Three-point-percentage is a straight-forward statistic. It is calculated by dividing the number of three-point-makes by the number of attempts: 



As the term shows, three-point-percentage measures shooting accuracy and will always be a value somewhere between 0 and 1. Carelessly just going by 3P% a manager looking for a good shooting prospect would have to draft a talent that went 1/2 over a player who converted 40/100 of his triples as .5 is a lot greater than .4. But when evaluating and projecting shooting ability and not only accuracy this approach seems silly. We intuitively know that the number of attempts a player needed for his results should be factored in since even though they present the same accuracy on the surface neither 1/2 and 50/100 nor 0/1 and 0/100 should be treated equally. 

Hence, to produce a more useful or even ‘true’ estimate of shooting abilities, more context needs to be added to the simple percentage. Often basic filtering is sufficient. As described earlier, after crossing a certain threshold in sample-size plain percentages become reliable statistics. For three-point shooting this point has proven to be around 750 attempts [15], meaning we can use simple 3P% as a tool to compare shooting capabilities of talents somewhat confidently if all of the evaluated players have hit this mark. 

However, this excludes a lot of prospects. As we want to be able to project all potential NBA players in their shooting translation, we chose empirical Bayes estimation as our method to work with pre-draft three-point-percentage - a good example for a binominal distribution. With this technique, context is added by fitting a beta distribution to all available data, gaining a prior that adds information based on the investigated environment. Later, this prior is individually updated with the evidence each observation gave and converted to a posterior distribution [61]. 

To produce our prior, we first need to fit a regular beta distribution to the histogram of all the three-point-percentages of our data base, using this model: 





10 



This estimation gives us α ≈ 114 and β ≈ 201 for all players who attempted at least one threepointer, using the most data points from our data set possible. 



Figure 5. Density plot of Pre-Draft-3P% with beta distribution fit curve. 

The density plot of the beta distribution fit with maximum likelihood over a histogram of three-point percentage seems to match our data satisfyingly well. Hence, we can apply Bayesian inference, adapt the found values as our priors and update each case based on this foundation using the following formula: 

𝐵𝑒𝑡𝑎 (𝛼! + 𝑚𝑎𝑘𝑒𝑠, 𝛽! + 𝑚𝑖𝑠𝑠𝑒𝑠) 

This means that the expected mean value of the beta distribution is 



The found prior is the head start basically every player gets assigned with before evaluating their actual performance. Depending on the three-point makes and misses a talent showed the found prior is updated. The greater the sample size a prospect produced, the greater the chance to shift the prior in one direction or the other. Simply applying the examples from earlier, we can see that this approach would estimate that an athlete hitting 40/100 is more likely to be a better shooter than a competitor making 1/2 despite having a lower three-point percentage: 



11 





Applying this method, we updated each observation using our found prior. Or as this figure shows, we basically shrunk each value towards the expected mean value. The smaller the sample-size a player put up the more reason the model has to move the three-pointpercentage towards the general expectation of average based on the investigated environment. 



Figure 6. Raw Pre-Draft-3P% versus Shrunken-3P% 

In our first step, we updated all three-point-percentages of our database this way and got a little closer to a more insightful metric to use for our shooting translation projection. Extreme cases of either extremely high or low accuracy got corrected if they were based on little evidence. 

### **4.2. Beta binomial regression for pre-draft three-point percentage** 

Shrinking three-point percentages towards an expected mean seems to have improved the metric already. All players getting lucky by hitting most attempts of a very low number of tries from behind the three-point line are not listed as the players potentially possessing the most shooting accuracy anymore. But our method did not account for one important dynamic within the sport of basketball: Weak shooters generally tend to shoot less than better long-range threats due to e.g. a lack of self-confidence or coaching staffs restricting prospects from taking triples. On the flipside strong shooters usually get the green light in their team’s offense, even if they hit a cold-streak that could already influence a small college- 



12 



sample immensely, because they showed their talents in practices. As we can see, we did not account for this complication in our first estimation. Players shooting very little tend to get overrated by only using a one-fit-all-prior. 



Figure 7. Comparison Raw 3P% versus Shrunken 3P% by CBB 3PA. 

Factoring in this complication, forces us to adjust our found estimates again, since we can see that our Empirical Bayes estimate towards our prior (indicated by the red dotted line) systematically overvalues shooters that took very little shots. The blue line, showing the median average for every attempt range, bears out that sentiment. 

Removing this bias within our estimates, we need to adjust our model. We want our priors to be influenced by the number of threes a prospect has taken/was allowed to take. Robinson (2017) suggests using beta-binomial regression and update the model in a generative process to the following, with pi being defined as the true shooting percentage of player i and letting 3PAi be known and fixed per player [61]: 





The “ebbr”-package in R lets us calculate individual priors for our shooting estimation, based on the number of attempts. Their distributions look like this: 



13 





Figure 8. Overview over new priors based on beta-binomial regression. 

Our newfound priors still state a fairly great amount of uncertainty. Attempting 750 threes in college still leaves open a broad corridor of a ‘true’ shooting-percentage of .31 to .46 for a prospect as the range of probable results. But with the range depending on 3PA, it can be assumed that a talent that only attempted 10 threes is almost certainly a worse shooter than a player taking 750 triples, assumed they had equal playing opportunities. 



Figure 9. Shrunken-3P% versus 3P% estimate with regression. 



14 



With the new priors most of the percentage estimates for players with little attempts drop quite a bit and correct for our former systematic overvaluation of shooting. 



Figure 10. Overview of Raw 3P%, Shrunken 3P% and 3P% estimate with regression by CBB 3PA. 

Investigating the effects of our last step, we reached our intended results. Our new basic shooting-estimates look more context driven and therefore more accurate than our raw percentages. We eliminated unreasonably high or low percentages produced by (bad) shooting luck in small sample-size circumstances, using a data educated prior. Afterwards we corrected our shrinkage values by introducing individual priors for every player based on their number of three-point attempts as basketball logic suggests that this factor should play a role in the estimation of shooting ability. 

The newfound statistic is still problematic as various external factors (e.g. tactical system, injury, suspensions, competition) can influence the number of three-point attempts a player is taking despite his assumed shooting ability as our simple approach puts to the forefront here. However, our values now better line up with the median average a certain attempt threshold dictates, which is promising. Additionally, the found estimates are only one piece of the three-point-translation-model presented later. 

### **4.3. Modeling three-point-percentage translation adding two-point-jumper accuracy** 

Finally, we can put together all the prepared components and combine them into a modeling approach. Based on our theoretical work we assume the pre-draft factors free-throw percentage, two-point-jumper percentage and our estimation of three-point-percentage (after an empirical Bayes estimation while according for three-point-attempts in our priors) to be a fruitful foundation for the projected translation of NBA three-point-shooting based 



15 



on pre-draft-data. Hence, the formula of our multiple regression model (M1) with postshooting-accuracy as our dependent variable shall be: 

𝑀1: 𝑃𝑜𝑠𝑡𝐷𝑟𝑎𝑓𝑡3𝑃% = 𝛽! + 𝛽" 𝑃𝑟𝑒𝐷𝑟𝑎𝑓𝑡𝐹𝑇% + 𝛽# 𝑃𝑟𝑒𝐷𝑟𝑎𝑓𝑡2𝑃𝐽% + 𝛽$ 𝑃𝑟𝑒𝐷𝑟𝑎𝑓𝑡3𝑃%𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 

We will compare the results of this approach with two other popular methods we found [39, 40], using pre-draft three-point-accuracy-data without a shrinkage concept. While the second model (M2) adds simple pre-draft three-point-percentage and three-point attemptrate per 40 minutes, the third model (M3) factors in a combination of the two variables by calling on three-pointers made per 40 minutes: 

𝑀2: 𝑃𝑜𝑠𝑡𝐷𝑟𝑎𝑓𝑡3𝑃% = 𝛽! + 𝛽" 𝑃𝑟𝑒𝐷𝑟𝑎𝑓𝑡𝐹𝑇% + 𝛽# 𝑃𝑟𝑒𝐷𝑟𝑎𝑓𝑡3𝑃% + 𝛽$ 𝑃𝑟𝑒𝐷𝑟𝑎𝑓𝑡3𝑃𝐴𝑝40 

𝑀3: 𝑃𝑜𝑠𝑡𝐷𝑟𝑎𝑓𝑡3𝑃% = 𝛽! + 𝛽" 𝑃𝑟𝑒𝐷𝑟𝑎𝑓𝑡𝐹𝑇% + 𝛽# 𝑃𝑟𝑒𝐷𝑟𝑎𝑓𝑡3𝑃𝑀𝑝40 

We tested all modeling ideas on our data set for all athletes who attempted at least one three in college (to be able to calculate a pre-draft three-point-percentage estimate) and played at least 50 games in the NBA already (N = 255). We chose this threshold to be able to include as many players as possible, while working with a reasonable sample-size of games. Even rookies from the 2019/20 season had the chance to qualify if they played enough until the COVID-19 intermission. 

M1 proved to be a highly significant general model with an overall explanatory power of an adjusted R² of 0.231. We can reject the H0 of these factors not having an influence on the dependent variable. All individual components were highly significant as well and having an effect in the expected direction. Good pre-draft performance translates into a projection of higher post-draft skills: 

**Table 1** 

<u>Coefficient Overview Model 1</u> 

|||Unstanda|rdized Coefficients|Standardized Coefficients|t|Sig.|
|---|---|---|---|---|---|---|
|Model 1||B|Std. Error|Beta|||
|1|(Constant)|-.134|.052||-2.576|.011|
||Pre-Draft-FT%|.153|.062|.169|2.456|.015|
||Pre-Draft-2PJ%|.202|.081|.145|2.502|.013|
||Pre-Draft-3P%-Estimate|.756|.146|.343|5.177|.000|



a. Dependent Variable: Post-Draft-3P% 

M2 also presents a highly significant model with and an adjusted R² of 0.213. Contrary to M1, it does not only consist of significant parts. Curiously, Pre-Draft-3P% does not improve the prediction of the design. Though, removing the variable only improves the explained variance by 0.002. 



16 



**Table 2** 

<u>Coefficient Overview Model 2</u> 

|||Unstand|ardized Coefficients|Standardized Coefficients|t|Sig.|
|---|---|---|---|---|---|---|
|Model 2||B|Std. Error|Beta|||
|1|(Constant)|.126|.040||3.137|.002|
||Pre-Draft-FT%|.215|.059|.238|3.645|.000|
||Pre-Draft-3P%|-.020|.042|-.028|-.468|.640|
||Pre-Draft-3PAp40|.009|.002|.316|4.722|.000|



a. Dependent Variable: Post-Draft-3P% 

M3 is similar to M2 in its results. Presenting a highly significant modeling concept again, M3 has an adjusted R² of 0.216. Its individual variables are all highly significant and have an effect in the expected direction: 

**Table 3** 

<u>Coefficient Overview Model 3</u> 

||Unstand|ardized Coefficients|Standardized Coefficients|t|Sig.|
|---|---|---|---|---|---|
|Model 3|B|Std. Error|Beta|||
|1<br>(Constant)|.123|.040||3.106|.002|
|Pre-Draft-FT%|.212|.058|.233|3.621|.000|
|Pre-Draft-3PMp40|.009|.002|.308|4.771|.000|



a. Dependent Variable: Post-Draft-3P% 

Comparing the explained variance of all the designs, M1 fares the best. Its prediction of postdraft three-point-percentage based on pre-draft-statistics is superior to the explored publicly available methods. Examining the standardized beta coefficients, the Pre-Draft3P%-Estimate has the most influence on the projection of the dependent variable. But taking two-point-jump shoot-accuracy into account also contributes to the overall model performance. Without posing a huge increase in explained variance, our design still delivers a slight improvement over the known technique. 

To further evaluate the models, we calculated the mean absolute deviation for all designs. M1 performed best again with a general error size of 0.0447 compared to M2 (0.0466) and M3 (0.0463). Once more, the differences are marginal, but still relevant. 



17 





Figure 11. Absolute Errors of Model 1 by NBA Games. 



Figure 12. Absolute Errors of Model 1 by NBA 3PA. 

Finally, we used absolute error terms to evaluate M1 individually. With an increasing number of NBA games and three-point attempts the size of the errors made decreases rapidly and seems to stabilize. Curiously, we can also show that predicting the shooting 



18 



accuracy of bigmen offers the most problems to our design and can clearly be picked out as an area of improvement, even though position variables did not prove to be significant in our initial modeling. 

### **4.4. Predicting post-draft three-point-attempt rate** 

Shooting ability in the NBA is surely about how accurate players are at hitting the basket when taking shots from distance. Therefore, we investigated Post-Draft-3P% as a metric, managers should be eager to project accurately in a draftee. However, prospects also need to be willing to take these kinds of shots at a reasonable rate to make enough use of their own competence and keep defenses honest. Only a combination of accuracy and volume represents shooting-ability correctly. That is why we incorporated three-point-attempts into our estimations of ‘true’ pre-draft-three-point-percentage. 

Consequently, in our quest of predicting shooting-translation from the NCAA to the NBA, we also need to look at the three-point-attempt-rate at the professional level and suggest a model that allows to project this metric as accurate as possible to aid draft decision-making even further. 

Thus, we chose a rather exploratory approach since we could not derive a regression design solely from theory. We selected NBA three-point-attempt rate per 40 minutes as our dependent variable. For the independent components of the model, we took all six available factors from the three already explored ideas for three-point-percentage as all of these can be argued as measures for shooting ability (all pre-draft measures: 3P%, 3PAp40, 3PMp40, FT%, 2PJ%, 3P%-estimate). Afterwards, we applied a stepwise multiple regression method to check if a significant approach was there and which combination of the individual parts would offer the most explanatory power. Again, we used the entire data set, filtering for one college three attempt and 50 played NBA games. 

**Table 4** 

<u>Model Summaries of Viable Designs with Stepwise Addition of Variables</u> 

|||||Std. Error of the|C|hange Stati|stics||Sig. F|
|---|---|---|---|---|---|---|---|---|---|
|Model|R|R Square|Adjusted R Square|Estimate|R Square Change|F Change|df1|df2|Change|
|1|.750<sup>a</sup>|.562|.560|1.531|.562|324.692|1|253|.000|
|2|.759<sup>b</sup>|.575|.572|1.511|.013|7.962|1|252|.005|
|3|.767<sup>c</sup>|.588|.583|1.491|.012|7.547|1|251|.006|



a. Predictors: (Constant), Pre-Draft-3PMp40 

b. Predictors: (Constant), Pre-Draft-3PMp40, Pre-Draft-2PJ% 

c. Predictors: (Constant), Pre-Draft-3PMp40, Pre-Draft-2PJ%, Pre-Draft-3P%-Estimate 

d. Dependent Variable: Post-Draft-3PAp40 



19 



#### **Table 5** 

<u>Coefficient Overview Stepwise Model</u> 

|||Unst<br>Co|andardized<br>efficients|Standardized<br>Coefficients|t|Sig.|Collinearity|Statistics|
|---|---|---|---|---|---|---|---|---|
|Mo|del|B|Std. Error|Beta|||Tolerance|VIF|
|1|(Constant)|1.696|.181||9.396|.000|||
||Pre-Draft-3PMp40|.685|.038|.750|18.019|.000|1.000|1.000|
|2|(Constant)|-.203|.696||-.292|.770|||
||Pre-Draft-3PMp40|.687|.038|.752|18.320|.000|1.000|1.000|
||Pre-Draft-2PJ%|4.977|1.764|.116|2.822|.005|1.000|1.000|
|3|(Constant)|-3.830|1.488||-2.573|.011|||
||Pre-Draft-3PMp40|.563|.058|.616|9.642|.000|.402|2.488|
||Pre-Draft-2PJ%|4.990|1.741|.116|2.865|.005|1.000|1.000|
||Pre-Draft-3P%-|11.955|4.352|.176|2.747|.006|.402|2.488|
||Estimate||||||||



a. Dependent Variable: Post-Draft-3PAp40 

The best model appears to include pre-draft three-pointer-make rate per 40 minutes, predraft-two-point-jumper-percentage, and our newly introduced estimate of pre-draft-threepoint-percentage. The model itself is highly significant as well as all its individual components. The adjusted R² of 0.588 is fairly strong, while all component coefficients have an effect in the anticipated direction. 

This gives us reason to believe, that the found model (M4) 

𝑀4: 𝑃𝑜𝑠𝑡𝐷𝑟𝑎𝑓𝑡3𝑃𝐴𝑝40 = 𝛽! + 𝛽" 𝑃𝑟𝑒𝐷𝑟𝑎𝑓𝑡3𝑃𝑀𝑝40 + 𝛽# 𝑃𝑟𝑒𝐷𝑟𝑎𝑓𝑡2𝑃𝐽% + 𝛽$ 𝑃𝑟𝑒𝐷𝑟𝑎𝑓𝑡3𝑃%𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 

should be useful in the projection of shooting competence translation, while our newly introduced components contribute to this prediction. 

Again, we evaluated the model by investigating its error terms. The mean absolute deviation of the design is 1.2, which seems reasonable, when projecting 3PAp40. 



20 





Figure 13. Average Errors of Model 4 by NBA Games. 



Figure 14. Average Errors of Model 4 by NBA 3PA. 

Again, it can be observed that the model’s projections become more accurate with increasing NBA games played as well as threes taken, and then stabilize. The distinction between 



21 



bigmen and non-bigs appears to be important again, even though bigmen-attempt-rates seem to be more predictable by the variables used than three-point accuracy. 

## **5. Conclusion and Outlook** 

In this paper we investigated whether an empirical Bayesian derived ‘true’ pre-draft threepoint percentage and pre-draft two-point-jumper-percentage could contribute positively to the quest of projecting the shooting translation of NBA draft prospects. Our analysis showed that in addition to pre-draft free-throw-shooting both statistics provide value as a basis for predictive modeling. The newfound three-point-percentage estimate based on dataintroduced Bayesian priors, factoring in the number of attempts as an indicator for basic shooting-quality lends more context to the former simple percentages. The two-point jumper-percentage also behaves as expected. Our notion of this metric being another indicator of general ‘shooting touch’, just like free-throw percentage, turned out to be right and should be considered for shooting translation ideas from now on. 

Interestingly, this statistic also contributes positively to the projection of three-pointattempt-rate, which should draw some attention. The showed connection indicates that the popular basketball narrative, implying that hitting midrange-shots effectively could be an indicator for a player having shooting-range which might be expandable to behind the threepoint line, could be true. 

The general model we found, including the components in question, presents an improvement to other publicly available designs of shooting-translation. We were able to show that compared to systems based on simpler metrics, our model was able to project three-point accuracy with less errors than former approaches. Additionally, we were pleased to see that our introduced variables offer an even more promising basis for the projection of post-draft three-point shooting-volume, adding even more information to the evaluation of a prospects shooting-competence. Such contributions could ultimately improve draft decision-making league-wide and therefore move the results of the policy towards the intended outcomes. 

However, the simple modeling presented here, cannot be used reliably on its own. As we can see with the shares of variance that both models for shooting translation fail to explain, many important dynamics are not captured by the simple metrics including the Bayesian informed three-point percentage and two-point jump-shooting. The design has difficulties picking up on e.g. conservative college schemes suppressing shooting aspirations of talented bigmen or possible non-linear future development of players due to improved coaching or shooting mechanic change. Hence, it should rather be used as a valuable decision-informing tool during the draft process, triggering conversation and possibly closer investigations of prospects, rather than being the main argument for a choice. 



22 



To produce a model powerful enough to be used in this way, more research, time, and data is needed. Our approach regarding two-point-jumpers was based on pre-draft play-by-play data that has been available for NCAA prospects for a decade only. Such a sample-size is not satisfying, but will automatically expand in the coming years, maybe even with the addition of information on international prospects, to allow more accurate results. 

Besides this natural progression, more sophisticated future approaches should consider capturing more of the external factors that potentially go into the projection of shooting progression. Having data on system-based shooting suppression/enhancement of a former team or a more detailed overview of the types of threes a player took, would further inform estimations of a ‘true’ pre-draft three-point percentage. Analysis of biomechanical or psychological attributes could educate estimates of development curves as well, by e.g. showing an obvious, but easy to fix flaw in the shooting motion, a lack of throwing consistency due to weak conditioning or a lack of confidence in the own abilities and then indicating a high likelihood of improvement in these areas by showing a good work-ethic and high coachability with psychological profiling. Picking up on such signals, which should inform shooting translation even further, would allow to improve draft decision-makingquality even more. 

## **References** 

- [1] Alamar, B. C. (2013). Sports Analytics. Columbia University Press. https://doi.org/10.7312/alam16292 

- [2] Allison, J. R. (1973). Professional Sports and the Antitrust Laws: Status of the Reserve System. Baylor L. Rev., 25, 1. 

- [3] Ardigò, L. P., Kuvacic, G., Iacono, A. D., Dascanio, G., & Padulo, J. (2018). Effect of Heart rate on Basketball Three-Point Shot Accuracy. Frontiers in Physiology, 9, 75. https://doi.org/10.3389/fphys.2018.00075 

- [4] Ashley, C. (2017). Explaining NBA Success for Players with Varied College Experience. Sport Management Undergraduate., Article Paper 128. 

- [5] Barttorvik. (2020). Customizable College Basketball Tempo Free Stats - T-Rank. https://barttorvik.com/ 

- [6] Basketball-Reference.com. (2020a). Basketball Statistics and History | BasketballReference.com. https://www.basketball-reference.com/ 

- [7] Basketball-Reference.com. (2020b). NBA & ABA Career Leaders and Records for Value Over Replacement Player | Basketball-Reference.com. https://www.basketballreference.com/leaders/vorp_career.html 

- [8] Beene, A. (2019). NBA Draft Decision-Making using Play-by-Play Data. MIT Sloan Sports Analytics Conference. MIT Sloan Sports Analytics Conference Research Paper Competition. 

- [9] Berg, A. (2020). Bayesian statistics in the classroom: Introducing shrinkage with basketball statistics and the internet movie database. Teaching Statistics, 42(2), 47–53. https://doi.org/10.1111/test.12220 

- [10] Bernardo, J. M., & Smith, A. F. M. (2009). Bayesian theory. John Wiley & Sons. 

- [11] Berri, D. J. (2013). Losing Is Not a Winning Strategy in the NBA - Freakonomics. http://freakonomics.com/2013/10/29/losing-is-not-a-winning-strategy-in-the-nba/ 



23 



- [12] Berri, D. J., Brook, S. L., & Fenn, A. J. (2011). From college to the pros: Predicting the NBA amateur player draft. Journal of Productivity Analysis, 35(1), 25–35. 

- [13] Berri, D. J., & Schmidt, M. B. (2010). Stumbling on wins: Two economists expose the pitfalls on the road to victory in professional sports. FT Press. 

- [14] Berri, D. J., Schmidt, M. B., & Brook, S. L. (2004). Stars at the Gate: The Impact of Star Power on NBA Gate Revenues. Journal of Sports Economics, 5(1), 33–50. https://doi.org/10.1177/1527002503254051 

- [15] Blackport, D. (2014). How Long Does It Take For Three Point Shooting To Stabilize? Nylon Calculus. 

- [16] Brahme, A. (2017). Nylon Calculus: Navigating the NBA’s changing landscape. Nylon Calculus. 

- [17] Burdekin, R. C. K., & Van, C. (2019). NBA Player Outcomes Following the Implementation of the ‘One-and-Done’Rule: Do Top Players Really Benefit from Attending College First? Journal of Sports Economics and Management. 

- [18] Burger, J. E. (1972). The NBA's Four Year Rule: A Technical Foul. Law & Soc. Order, 489. 

- [19] Burkow, S. H., & Slaughter, F. L. (1981). Should Amateur Athletes Resist the Draft. Black LJ, 7, 314. 

- [20] Caporale, T., & Collier, T. C. (2013). Scouts versus Stats: the impact of Moneyball on the Major League Baseball draft. Applied Economics, 45(15), 1983–1990. 

- [21] Carlson, R. S. (1972). The Business of Professional Sports: A Reexamination in Progress. NYLF, 18, 915. 

- [22] Coates, D., & Oguntimein, B. (2010). The length and success of NBA careers: Does college production predict professional outcomes. International Journal of Sport Finance, 5(1), 4–26. 

- [23] Curcic, D. (2020). 69 Years of Height Evolution in the NBA [4,379 players analyzed]. RunRepeat. 

- [24] Deaner, R. O., Lowen, A., & Cobley, S. (2013). Born at the wrong time: selection bias in the NHL draft. PloS One, 8(2). 

- [25] Friedman, M., & Savage, L. J. (1948). The utility analysis of choices involving risk. Journal of Political Economy, 56(4), 279–304. 

- [26] Goldsberry, K. (2012). CourtVision : New Visual and Spatial Analytics for the NBA. 

- [27] Goldsberry, K. (2019). SPRAWLBALL: A visual tour of the new era of the nba. MARINER Books. 

- [28] Goldblatt, B. (2008). Adjusting (and projecting) Three Point Shooting Statistics. Stanford.edu. 

- [29] Groothuis, P. A., Hill, J. R., & Perri, T. J. (2007). Early entry in the NBA draft: The influence of unraveling, human capital, and option value. Journal of Sports Economics, 8(3), 223–243. 

- [30] Harper, Z. (2013). The Quest for 900: How slingers have replaced Goliath in the NBA. CBS SPORTS. https://www.cbssports.com/nba/news/the-quest-for-900-how-slingers-havereplaced-goliath-in-the-nba/ 

- [31] Harris, J., & Berri, D. J. (2015). Predicting the WNBA draft: What matters most from college performance? International Journal of Sport Finance, 10(4), 299. 

- [32] Hausman, J. A., & Leonard, G. K. (1997). Superstars in the National Basketball Association: Economic Value and Policy. Journal of Labor Economics, 15(4), 586–624. https://doi.org/10.1086/209839 

- [33] Hendrick, J. L. (2016). The Waiting Game: Examining Labor Law and Reasons Why the WNBA Needs to Change Its Age/Education Policy. Marq. Sports L. Rev., 27, 521. 



24 



- [34] Hendricks, W., DeBrock, L., & Koenker, R. (2003). Uncertainty, hiring, and subsequent performance: The NFL draft. Journal of Labor Economics, 21(4), 857–886. 

- [35] Hofmann, R. (2013). Michael Carter-Williams and The Swing Skill. Liberty Ballers. 

- [36] Hoop-Math. (2020). College basketball play-by-play statistics. https://hoop-math.com/ 

- [37] Hudson, J. L. (1985). Prediction of Basketball Skill Using Biomechanical Variables. Research Quarterly for Exercise and Sport, 56(2), 115–121. https://doi.org/10.1080/02701367.1985.10608445 

- [38] Ichniowski, C., & Preston, A. E. (2012). Does march madness lead to irrational exuberance in the NBA draft? High-value employee selection decisions and decision-making bias. National Bureau of Economic Research. 

- [39] Johnson, A. (2014). Predictions are Hard, Especially about Three Point Shooting. Counting the Baskets. 

- [40] Johnson, A. (2015). Projecting Draft Prospects Three-Point Percentages. Nylon Calculus. 

- [41] Kahneman, D., & Tversky, A. (1979). Prospect Theory: An Analysis of Decision under Risk. Econometrica, 47(2), 263. https://doi.org/10.2307/1914185 

- [42] Knudson, D. (1993). Biomechanics of the Basketball Jump Shot—Six Key Teaching Points. Journal of Physical Education, Recreation & Dance, 64(2), 67–73. https://doi.org/10.1080/07303084.1993.10606710 

- [43] Koehler, D. J., & Harvey, N. E. (Eds.). (2004). Blackwell handbook of judgment and decision making. 

- [44] Levick, N. (2019). What if the Sixers had never traded up to draft Markelle Fultz? NBC Sports Philadelphia. 

- [45] Lewis, M. (2004). Moneyball: The art of winning an unfair game ; [with a new afterword (1. pbk. ed.). Norton. 

- [46] Lewis, M. (2017). The undoing project: A friendship that changed our minds (First edition). W.W. Norton & Company. 

- [47] Marcin, T. (2018). Markelle Fultz's Jump Shot, the Yips and Explaining the Sports Phenomenon Through Past Cases. Newsweek. 

- [48] Martínez, J. A. (2012). Factors determining production (FDP) in basketball. Economics and Business Letters, 1(1), 21–29. 

- [49] Massey, C., & Thaler, R. H. (2013). The loser's curse: Decision making and market efficiency in the National Football League draft. Management Science, 59(7), 1479–1495. 

- [50] Miller, P. (2018). Predicting 3-point efficiency for incoming rookies. Nylon Calculus. 

- [51] Mishra, S., Barclay, P., & Sparks, A. (2017). The relative state model: Integrating need-based and ability-based pathways to risk-taking. Personality and Social Psychology Review, 21(2), 176–198. 

- [52] Monroe, M. (2016). How an NBA 'Shot Whisperer' Transformed Kawhi Leonard into a 3- Point Fire Hazard. Bleacher Report. 

- [53] Morris, B. (2015). Stephen Curry Is The Revolution. FiveThirtyEight. 

- [54] Motomura, A. (2016). MoneyRoundball? The Drafting of International Players by National Basketball Association Teams. Journal of Sports Economics, 17(2), 175–206. https://doi.org/10.1177/1527002514526411 

- [55] Motomura, A., Roberts, K. V., Leeds, D. M., & Leeds, M. A. (2016). Does It Pay to Build Through the Draft in the National Basketball Association? Journal of Sports Economics, 17(5), 501–516. https://doi.org/10.1177/1527002516641169 



25 



- [56] Moxley, J. H., & Towne, T. J. (2015). Predicting success in the National Basketball Association: Stability & potential. Psychology of Sport and Exercise, 16, 128–136. https://doi.org/10.1016/j.psychsport.2014.07.003 

- [57] Oliver, D. (2004). Basketball on paper: Rules and tools for performance analysis (1. ed.). Potomac Books, Inc. 

- [58] Paine, N., & Herring, C. (2018). If The NBA Is Going Small, Why Are This Year’s Prospects Tall? FiveThirtyEight. 

- [59] Pates, J., Cummings, A., & Maynard, I. (2002). The Effects of Hypnosis on Flow States and Three-Point Shooting Performance in Bastketball Players. The Sport Psychologist, 16(1), 34–47. https://doi.org/10.1123/tsp.16.1.34 

- [60] Richey, M., & Zorn, P. (2005). Basketball, Beta, and Bayes. Mathematics Magazine, 78(5), 354. https://doi.org/10.2307/30044191 

- [61] Robinson, D. (2017). Introduction to empirical bayes: Examples from baseball statistics. ASIN: B06WP26J8Q. 

- [62] Robinson, D. (2020). dgrtwo/ebbr. https://github.com/dgrtwo/ebbr 

- [63] Rottenberg, S. (1956). The Baseball Players' Labor Market. Journal of Political Economy, 64(3), 242–258. https://doi.org/10.1086/257790 

- [64] Sailofsky, D. (2018). Drafting Errors and Decisionmaking Bias in the NBA Draft. MIT Sloan Sports Analytics Conference Research Paper Competition. 

- [65] Salador, K. (2011). Forecasting Performance of International Players in the NBA. MIT Sloan Sports Analytics Conference. 

- [66] Santos-Fernandez, E., Wu, P., & Mengersen, K. L. (2019). BAYESIAN STATISTICS MEETS SPORTS: Acomprehensive. JOURNAL of QUANTITATIVE ANALYSIS in SPORTS (JQAS). 

- [67] Shea, S. M. (2014). Basketball analytics: Spatial tracking. 

- [68] Shields, B. (2017). Integrating Analytics in Your Organization: Lessons From the Sports Industry. https://sloanreview.mit.edu/article/integrating-analytics-in-your-organizationlessons-from-the-sports-industry/ 

- [69] Sims, J., & Addona, V. (2016). Hurdle Models and Age Effects in the Major League Baseball Draft. Journal of Sports Economics, 17(7), 672–687. 

- [70] Soebbing, B. P., & Mason, D. S. (2009). Managing legitimacy and uncertainty in professional team sport: the NBA's draft lottery. Team Performance Management: An International Journal, 15(3/4), 141–157. https://doi.org/10.1108/13527590910964928 

- [71] Sun, H., Yu, J., & Centeno, R. (2017). Projecting Three-Point Percentages for the NBA Draft. 

- [72] Taylor, B. (2017). The Backpicks GOAT: The 40 Best Careers in NBA History. https://backpicks.com/2017/12/11/the-backpicks-goat-the-40-best-careers-in-nba-history/ 

- [73] Tingling, P., Masri, K., & Martell, M. (2011). Does order matter? An empirical analysis of NHL draft decisions. Sport, Business and Management: An International Journal, 1(2), 155–171. https://doi.org/10.1108/20426781111146754 

- [74] Totty, E. S., & Owens, M. F. (2011). Salary caps and competitive balance in professional sports leagues. Journal for Economic Educators, 11(2), 45–56. 

- [75] Wetzels, R., Tutschkow, D., Dolan, C., van der Sluis, S., Dutilh, G., & Wagenmakers, E.-J. (2016). A Bayesian test for the hot hand phenomenon. Journal of Mathematical Psychology, 72, 200–209. 

- [76] Whitehead, T. (2016). Why Charles Barkley hates jump-shooting teams. Nylon Calculus. 

- [77] Wilco, D. (2019). College and NBA basketball's biggest rule differences. NCAA.com. 

- [78] Volz, K. G., & Gigerenzer, G. (2012). Cognitive processes in decisions under risk are not the same as in decisions under uncertainty. Frontiers in Neuroscience, 6, Article 105, 1–6. 



26 



- [79] Phillips, O. (2017). The NBA’s Age Limit Is Broken. FiveThirtyEight. 

- [80] Oudejans, R. R.D., van de Langenberg, Rolf W, & Hutter, R.I. (2002). Aiming at a far target under different viewing conditions: Visual control in basketball jump shooting. Human Movement Science, 21(4), 457–480. https://doi.org/10.1016/S0167-9457(02)00116-1 



27 


