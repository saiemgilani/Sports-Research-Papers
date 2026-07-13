<!-- source: 2020 The Hot Hand and Its Effect on the NBA - Brian McNair,Eric Margolin, Michael Law, Ya'acov Ritov.pdf -->

# The Hot Hand and Its on the NBA 

McNair, Brian bmcnair@umich.edu 

Margolin, Eric Law, Michael Ritov, Ya’acov emargo@umich.edu mmylaw@umich.edu yritov@umich.edu 

November 2, 2020 

Department of Statistics University of Michigan Ann Arbor MI, USA 

##### **Abstract** 

This paper aims to revisit and expand upon previous work on the “hot hand” phenomenon in basketball, specifically in the NBA. Using larger, modern data sets, we test streakiness of shooting patterns and the presence of hot hand behavior in free throw shooting, while going further by examining league-wide hot hand trends and the changes in individual player behavior. Additionally, we perform simulations in order to assess their power. While we find no evidence of the hot hand in game-play and only weak evidence in free throw trials, we find that some NBA players exhibit behavioral changes based on the outcome of their previous shot. 

**Keywords:** Basketball, Hot Hand Effect/Fallacy, Small Sample Bias, Stochastic Simulation, Randomness of Streaks, Law of Small Numbers, Gambler’s Fallacy 

1 

## **1 Introduction** 

The “hot hand” phenomenon is at the center of a decades-long debate between basketball fans and social scientists. Many players, fans, coaches, and executives believe that a player who is “hot” — that is, they have made multiple consecutive successful shots — is more likely to make their next shot attempt. As an example, on January 21st, 2019, Golden State Warriors guard Klay Thompson hit all 10 of his three-point attempts in a game against the Los Angeles Lakers, tying an NBA record for the most three pointers in a game without a miss. When asked about the feat afterwards in a post-game interview, Warriors head coach Steve Kerr said, “Klay does that five or six times a season. You guys have seen it. He just got red hot, white hot” (Friedell 2019). 

In Gilovich, Vallone & Tversky (1985) (henceforth referred to as GVT), the first academic research to test the widely accepted notion of the hot hand, the authors found no evidence supporting the phenomenon in basketball. Through the examination of NBA field goal data, NBA free throw data, and controlled shooting experiments with college players, the authors concluded that streaky shooting behavior, or “hotness”, was nothing more than a belief in the fallacious law of small numbers (Tversky & Kahneman 1971), and that there lacked evidence to support the idea that players were truly more likely to make a shot after a make than after a miss. These findings led GVT to label the phenomenon a “widely shared cognitive illusion.” 

Their ideas did not go published without criticism. Larkey et al. (1989) compiled their own data set and sought to undermine GVT’s conclusions by analyzing streaks of high shooting percentages (instead of solely shooting streaks) and deriving their own statistics to conclude that total disregard of the hot hand in basketball was unreasonable. Tversky & Gilovich (1989) responded by suggesting potential flaws in the Larkey et al. (1989) methods and logic, asserting that the paper’s authors were misunderstanding the scope of their argument. Even today, as evident in Kerr’s quote about Thompson, there is still a divide between those who accept the hot hand hypothesis, and those who side with GVT in denying it. Very recently, Miller & Sanjurjo (2018) showed that the statistic used to estimate hot hand behavior (the empirical conditional probability of making a shot given the previous _k_ outcomes) is biased, and correcting for this bias in controlled shooting experiments, as they did with GVT’s data, suggests plausibility in the hot hand after all. Miller & Sanjurjo (2015) also showed support for the hot hand in three-point competitions, which is often thought of 

1 

as a nice balance between a controlled shooting experiment and a competitive environment. The free throw line, a similar setting, might show some signs of hot hand shooting (Arkes (2010), Lantis & Nesson (2019)). 

The original debate, however, is rooted in whether shooting patterns observed in a live game can accurately be labeled as hot shooting behavior, which is difficult to detect. Multiple studies have tried to account for the external factors that get in the way of observing hot hand behavior, such as increased defensive pressure and varying shot difficulty, but there is still no consensus as to whether or not the phenomenon witnessed on the court can truly be described as hot shooting (Aharoni & Sarig (2012), Csapo et al. (2015), Lantis & Nesson (2019), Miller & Sanjurjo (2014), Rao (2009)). Consistent with surveys conducted in GVT, various papers have shown that shot difficulty tends to change in response to detecting hot shooting behavior through increased defensive pressure or different shot selection, which likely accounts for the difficulty in confirming or denying the presence of hot shooting in game situations (Aharoni & Sarig (2012), Bocskocsky et al. (2014), Csapo et al. (2015), Rao (2009)) Aharoni & Sarig (2012) and Csapo et al. (2015) argue that since shot difficulty increases during hot streaks while shooting percentage does not significantly change, the hot hand does exist in game settings, but this conclusion is inconsistent with the idea that a player exhibiting hot hand shooting is more likely to make their next shot, the central premise behind GVT’s original paper. However, as it is difficult to detect the hot hand using massive data sets and precise statistical methods, one should question the ability of any observer of a basketball game to detect a phenomena. 

Our paper aims to revisit, expand upon, and analyze the methods put forward in previous papers, namely GVT. Using modern datasets, we attempt to replicate the results of prior studies, as well as further expand upon analyses of changes in players behavior of the attacker as well as the defenders in response to perceived hot hand behavior. Additionally, due to the difficulties in detecting the hot hand in game action, we also run simulations of some of our methods to determine how frequently we would expect to detect the hot hand in order to assess the statistical power of the procedure. 

In the end, there is no evidence of a hot hand phenomenon in the field of play, and only weak evidence of a hot hand in free throw shooting. However, we detected changes in player behavior in response to their previous shot outcomes, leading us to question GVT’s initial shot independence assumption. This combination leads us to conclude that GVT’s outright rejection of the hot hand is based on limited information and can thus only reject the hot hand in an equally limited capacity. The second section of our paper provides an 

2 

overview of our main data sources, and the third section contains our analysis, followed by our conclusions, tables, and figures. 

## **2 Data** 

Two datasets were utilized in this study: a dataset of shots from the 2014–15 NBA season from the NBA API (which can be found publicly at: https://www.kaggle.com/dansbecker/nba-shot-logs), as well as a dataset of free throws from the 2018–19 NBA season, scraped from Basketball-Reference.com. The NBA API dataset (as it will be referred to henceforth) contains 205,539 shots with many features, including shooter, shot distance, number of dribbles before shot attempt, distance to nearest defender, and type of shot, among many other variables. For this paper, we make use of the aforementioned variables. 

The free throw data from Basketball-Reference consists of 59,345 free throw attempts from 582 players, with free throw trips from flagrant (or technical) fouls filtered out. Each row consists of a game identification code, the free throw shooter, the result of the attempt, the number of attempts the shooter had in their trip, and the score of the game. This dataset was filtered to only include trips to the free throw line with at least two attempts, which lowered the number of free throws considered to 52,979. 

## **3 Analysis** 

### **3.1 Analysis of Runs** 

The core idea to the hot hand phenomenon is the belief that a player has periods during games in which he is shooting more accurately, and is thus more likely to hit their next shot after hitting multiple shots in a row. If this idea were true, then each shot would not be independent with one another. GVT tested this hypothesis with a Wald-Wolfowitz runs test (Wald & Wolfowitz 1943). Using the NBA API dataset, a Wald-Wolfowitz test was conducted on the shooting sequences of 443 players to see if streaky behavior was present. Streaks were limited to within games, thus the streak at the end of one game was not concatenated with the streak at the beginning of the next game. 

With this dataset, 25 out of 443 players (5.6%) had significant p-values at the 5% level, which is within 

3 

the range of expected significant p-values of (3.2%, 7.1%) under the null hypothesis. These results do not lend themselves to the existence of an observed hot hand phenomenon, which is consistent with the findings in GVT. However, the Wald-Wolfowitz tests look for the hot hand in each individual player. Our next section examines global hot hand behavior, in order to present a clearer league-wide picture. 

### **3.2 Global test statistic** 

Before continuing any further, it is important for us to provide a slightly more elaborate quantification of the “hot hand.” Let _pMi_ represent the probability of a player _i_ making a shot after a miss, and _pHi_ represent the probability of that same player making a shot after a make. Then, the effect size of the hot hand for ˆ ˆ player _i_ can be estimated by _pHi − pMi_ . Further, if the hot hand phenomenon was real, it would be expected that _pHi − pMi >_ 0, as this would signal a player is more likely to make a shot after a make than after a miss. Each player’s shots in the NBA API dataset were separated into disjoint pairs of consecutive shots to avoid the criteria of MLS within each game and categorized as one of the following: a “hit-hit” pair when the player made both shots, a “hit-miss” when they made the first shot and missed the second, “miss-miss,” and “miss-hit” for the corresponding outcomes. Each player’s _p_ ˆ _Hi_ , the proportion of made shots after the first shot was made, and _p_ ˆ _Mi_ , the proportion of made shots after the first shot was missed, were calculated. Under the null hypothesis, this estimator has a variance of 1 _/ni_ , where _ni_ is the total number of disjoint pairs for player _i_ . 

Then, to globally test if a player’s shooting percentage was independent of their preceding shot attempt, the following test statistic was utilized, aggregating the data for each player _i_ ( _N_ = 443 players): 



which has an asynptotic, non-standard normal distribution. 

A global test statistic of -4.4396 was computed from the disjoint pairs. The mean _p_ ˆ _Hi_ value was 0.4477, ˆ while the mean _pMi_ value was 0.4554. As we were testing the one-sided hypothesis that _pHi − pMi >_ 0, this negative test statistic is highly insignificant. While hot hand characteristics may occasionally be found in some players on an individual level, these results do not indicate a trend of a general hot hand throughout 

4 

the entire NBA. There are other parts of the game, however, where the hot hand could exist as a global phenomenon. 

### **3.3 Free Throws** 

To remove the possible influences that defensive behavior and shot selection might have on the shot outcome, GVT examined the serial correlation of free throw data from nine players on the 1981–82 Boston Celtics. They aimed to check if the hot hand effect was present in a fixed competitive environment. By examining each player’s correlation between the outcomes of their first free throw attempts and the outcomes of their second attempts, GVT concluded there was no evidence of hot hand behavior within free throw shooting. Using our recent free throw data, the same procedure was conducted. The correlations between the outcome of the first shot versus the outcome of the second shot were recorded for 480 players who had more than one trip to the free throw line, and each value was tested to see if it was significantly greater than zero. Table 1 shows the test results for players with the highest amount of free throw trips among significant correlation values. 

Overall, a total of 37 out of 480 players had serial correlation values that were significantly greater than zero at a 5% significance level, and therefore exhibited some hot hand behavior, which is slightly above the range of expected significant p-values of (14.64, 33.36) under the null, suggesting weak support of the hot hand effect. These results are slightly different than GVT, but are similar to findings from Arkes (2010) and Lantis & Nesson (2019). It is worth noting that there may be debate as to whether free throw shooting (as well as other controlled shooting environments) are truly relevant to the hot hand discussion, since free throws are exact mechanical repetitions, and observers normally do not acknowledge or care whether a free throw shooter is “hot,” with the exception of incredibly long streaks. Nonetheless, hot hand shooting is only weakly found in free throw shooting, and these results are not very relevant in the more popular conversation of whether the hot hand exists in the field of play. 

### **3.4 Player Behavior in Relation to the Hot Hand** 

Many defenders of the hot hand phenomenon point to differences “in both teams’ behavior after the detection of the hot hand” as a challenge in observing the hot hand’s existence (Aharoni & Sarig (2012), 

5 

Csapo et al. (2015)). They argue that defensive players focus more attention on hot players while offensive players focus more on getting hot players the ball. Both of these changes directly impact the probability a hot player makes their next shot and thus need to be considered in any analysis of the hot hand phenomenon. Using the NBA API data set, we attempt to quantify the aforementioned behavioral changes. 

#### **3.4.1 Shot Distance** 

The phrase “heat check” is thrown around by NBA analysts very frequently. It describes the instance where a hot player takes a “low percentage” shot (most frequently a long three-pointer), which for most players, ends their streak of makes. More generally, if shooters take shots from further away after a make than after a miss (a shot which they are more likely to miss), it could partially explain why the hot hand phenomenon would not be seen in tests that did not factor shot difficulty into account. For every player in our data set, we calculated the mean distance of their shot after a make and the mean distance of their shot after a miss. In order to eliminate the “carry over effect” from game to game we re-coded each player’s first shot of the game as an unknown value, allowing us to better quantify the hot hand. Contrary to widespread intuition, our analysis showed that 170 players took longer shots after a make and 171 players took longer shots after a miss. Among the 341 players analyzed, 19 (5 _._ 5% CI: 2 _._ 83% _,_ 8 _._ 17%) had a significant difference between the two means, with six (1 _._ 7% CI: 0 _._ 33% _,_ 3 _._ 07%) taking shots from further after a make and 13 (3 _._ 8% CI: 1 _._ 56% _,_ 6 _._ 04%) taking shots from further after a miss. Those players with significant differences are included in Table 2. Using the Benjamini-Hochberg Procedure (Benjamini & Hochberg 1995) to control False Discovery Rate (FDR) with a significance level of 0.05, we cannot confidently declare any discoveries for any of the p-values. 

These results go against the common hot hand intuition that players tend to be eager to attempt longer shots when they are on a hot streak. They instead show an insignificant mixed bag, with some players even attempting longer shots after miss. It is important to note that certain positions have different shooting behaviors, and it might be insightful to look into how these results vary by position. Again, even if the phenomenon exists, it is impossible to detect without sophisticated tools. In general, however, the outcome of previous shots doesn’t seem to significantly alter player shot attempts throughout the league as a whole. 

6 

#### **3.4.2 Shot Frequency** 

Another way to quantify an increase in “risky behavior” due to increased confidence is the frequency with which a player shoots. One would expect a player who just made a shot would take their next shot sooner than one who just missed. The time between shot attempts (measured in “game time“) for each player was used to examine whether players tended to take shots more frequently after a make than after a miss. 

In order to quantify this phenomenon, we used a similar methodology as in 3.4.1, calculating the mean time before attempting another shot after a make and after a miss. Among the 341 players analyzed, 148 (43%) players took shots later after a make, and 193 (57%) players took shots earlier after a make. 25 (7 _._ 3% CI: 4 _._ 54% _,_ 10 _._ 06%) had a significant difference between the two means, with nine (2 _._ 6% CI: 0 _._ 91% _,_ 4 _._ 29%) taking shots sooner after a make and 16 (4 _._ 6% CI: 2 _._ 38% _,_ 6 _._ 82%) taking shots sooner after a miss. Those players with significant differences are included in Table 3. Using the Benjamini-Hochberg Procedure to control FDR, for an _α_ of 0.05, we can confidently reject only one of the null hypotheses tested. 

These results, combined with the findings of 3.4.1 seem to counter the “heat-check” concept associated with the hot hand phenomenon. Players seem to not be influenced by the success of their previous shots in any systematic way. If anything, specific players seem to be more judicious after a make than a miss as seen in the generally closer shots taken after longer intervals. 

#### **3.4.3 Dribbles Before A Shot** 

Ball movement is often regarded as a crucial skill of a winning team (D’Amour et al. 2015). While the datasets used in this study did not include data on the number of passes a player makes, we can use their number of dribbles as a proxy to arrive at a similar measure of ball movement within an NBA offense. Using the NBA API data, we use a similar methodology as 3.4.1 and 3.4.2, calculating the mean number of dribbles a player takes after a made shot versus a missed shot. Out of 281 players with a significant number of shots, 102 (36 _._ 3%) players take fewer dribbles after a make and 179 (63 _._ 7%) take fewer dribbles after a miss. Forty (14 _._ 2% CI: 10 _._ 12% _,_ 18 _._ 28%) of these players had significant differences between their average number of dribbles, with six (2 _._ 1% CI: 0 _._ 42% _,_ 3 _._ 78%) taking more dribbles after a miss and 34 (12 _._ 1% CI: 10 _._ 12% _,_ 18 _._ 28%) taking more dribbles after a make. Those players with significant differences are included in Table 4. Using the Benjamini-Hochberg Procedure to control FDR, for an _α_ of 0.05, we can confidently 

7 

reject one of the null hypotheses tested. 

From the discussions in 3.4.1 and 3.4.2 we can see that, generally, NBA players do not tend to take “riskier” shots after a make. This, however, does not mean that there aren’t changes in an offensive player’s behavior based on the outcome of a previous shot. Our analysis of dribbles, shows that a minority of offensive players do behave differently, taking more dribbles, on average, after a make than after a miss. 

#### **3.4.4 Defender Distance** 

Thus far we have solely focused on changes in offensive behavior as a result of a made shot. Yet, the five players on the other team have an obvious impact on the game and should thus be considered when analyzing player behavior in regards to the hot hand. In essence, we hope to answer the question “Is a player guarded more closely after a make than a miss?” 

Using the same 281 players from sections 3.4.1–3.4.3, we calculated the mean distance from the closest defender for each shot taken after a miss and after a make. 175 (62 _._ 3%) players had defenders closer after a make and 106 (37 _._ 7%) had defenders closer after a miss. Of these players, 34 (12 _._ 1% CI: 8 _._ 37% _,_ 16 _._ 03%) had significant differences in their mean defender distance. Seven (2 _._ 5% CI: 0 _._ 67% _,_ 4 _._ 33%) of these significant players had defenders closer after a miss and 27 (9 _._ 6% CI: 6 _._ 16% _,_ 13 _._ 04%) had defenders closer after a make. Those players with significant differences are included in Table 5. 

Using the Benjamini-Hochberg Procedure (Benjamini & Hochberg 1995) to control FDR, for an alpha of 0.05, we can confidently reject six of the null hypotheses tested. These results suggest that globally, defenders do not appear to play significantly “tighter” or “looser” defense on an opponent depending on the result of the previous shot. 

#### **3.4.5 Discussion on Player Behavior and the Hot Hand** 

This section is intended to investigate the claim that basketball players change their behavior based on the result of their previous shot. From our analysis we see that, despite a few exceptions, NBA players do not tend to change their behavior based on the previous performance. This macro-observation debunks a crucial tenant of the pro-hot-hand argument, increasing confidence in GVT’s initial claim that the hot hand is mainly an observed psychological phenomenon. 

8 

While no players have significant differences in all three of the offensive metrics tested, three players (Dwayne Wade, Jarret Jack, and John Wall) had significant differences in both the number of dribbles taken before a shot and shot frequency after a miss versus after a make, and two players (James Jones and AlFarouq Aminu) have significant differences in both their shot frequency and shot distance after a miss versus a make. Thus, there appears to be some support for further examination of the idea that a few offensive players do change their behavior significantly in response to perceiving the hot hand, which is consistent with the findings in GVT’s survey of basketball players, but not factored in to their in-game testing methodology. 

### **3.5 Impact of Game Breaks on Hot Hand** 

If the hot hand does exist in the field of play, then it is in the best interest of the opposition to devise strategies aimed to “cool” off a player perceived to be hot. Coaches and players might like to know how quickly a player can slip out of hot behavior, or how easily a player can “cool” down when starting a hot streak. Aside from readjusting defensive pressure, a common strategy utilized by coaches trying to stop players from continuing their apparent hot streaks is to influence the flow of the game. This idea can be focused in offensive play, as some teams believe that changing the speed of their offense (and how deep into a possession they attempt a shot) will help them control the tempo of the game, which is believed to influence the performance of the opposition. Whether or not there is viability to this belief, a more direct way of influencing game flow is through play stoppage, via a timeout or end of a period. One form of this strategy, often referred to as “icing a player”, occurs when a time-out is called in-between an opposing player’s free throw attempts. Icing is practiced in similar ways throughout different sports, such as with field goal kicking in American football. The idea is that by increasing the time between attempts, it not only gives the shooter more time to think about their shot and get “psyched out”, but it removes them from their supposed rhythm that underlies their shooting performance. Regardless of whether or not the hot hand does exist, it is still useful for a team to know how they can instigate cold shooting behavior in an opponent, especially in critical game situations where the outcome of a game rests on one specific shot. Thus, there is value in studying the impact of these strategies. 

To test how breaks in game action impact a player’s shooting performance, field goal percentages before and after halftime were analyzed. Although these situations do not mirror free throw attempts and do not 

9 

illustrate the effect of “icing a shooter”, they do offer a glimpse as to how a substantial break from action affects shooting. In the NBA, halftime is fifteen minutes long, and is the longest pause from play throughout the entire game. Filtering the NBA API dataset to just performances by players who attempted at least three shots in the second and third quarters, player shooting probabilities between the second and third quarters were analyzed. The correlation results between field goal percentage just before the half and field goal percentages just after the half with different subsets of data are found in Table 6. There does not appear to be strong evidence that shooting performance changes significantly after the halftime break. There was one significant p-value at the 5% level with the subset of shots consisting of the last five attempts in quarter two and the first five shots in quarter three, but the global field goal percentages in those two subsets were nearly identical, but every other subset had a highly insignificant p-value. There does not appear to be strong evidence in favor of the halftime break instigating cold shooting behavior in players. Further research into the effects of timeouts on shooting behavior, especially in icing situations, would be beneficial to expand upon this analysis. 

### **3.6 Simulations** 

In order to evaluate power, simulations were performed to assess when hot hand behavior would be detected with the procedures used in this study. Using the NBA API dataset, for all _kit_ shots attempted by player _i_ in quarter _t_ (if player _i_ attempted a shot that quarter), _kit_ Bernoulli random variables were generated, where the probability of player _i_ making a shot in quarter _t_ was generated by the following: 



where _pi_ is player _i_ ’s seasonal field goal percentage. A new probability was generated for every quarter player _i_ recorded a shot. The value of _δ_ was changed for each set of simulations, with the objective of identifying which value of _δ_ was necessary to start detecting hot hand behavior, where a _δ_ value of 0 theoretically emulates the actual data. As _δ_ increases, we expected it to have an increasing effect on our simulated 

10 

results, as the gap between the higher shooting probability and the lower shooting probability widen. For each value of _δ_ , which ranged from values of zero to 0.6 (inclusive) with values differing by 0.03, 10 simulations were conducted, resulting in a total of 210 simulations generated. 

#### **3.6.1 Analysis of Runs** 

The results of running the Wald-Wolfowitz procedure on each player with Benjamini-Hochberg on the simulated data can be found in Figure 1. With the discoveries being declared at a 5% significance level, there is a strong positive relationship between the number of declared discoveries and the associated _δ_ value. A significant number of discoveries (more than 22 declared discoveries) is first found at _δ_ = 0 _._ 39, and 38 percent of the simulations found strong evidence of the hot hand using the Wald-Wolfowitz procedure. 

#### **3.6.2 Global Test Statistic** 

Figure 2 shows the results of finding the global test statistic in the simulations. As the value of _δ_ increases, the value of _T_ constantly increases, which would correspond to moving in the direction of more significance ( _H_ 0 : _T_ = 0 versus _H_ 1 : _T >_ 0). The first simulation results with a strong indication of simulated hot hand behavior was found at a _δ_ around 0 _._ 18. Overall, both simulations suggest that a _δ_ value between 0 _._ 18 and 0 _._ 39 was necessary to start finding strong evidence of the hot hand using our methods. 

## **4 Conclusion** 

Overall, we did not find any strong evidence in defense of the hot hand phenomenon. While we found a slight association between a player’s first free throw attempt and their second free throw attempt, similar to findings in Arkes (2010) and Lantis & Nesson (2019), there was not much evidence in favor of a hot hand effect in the field of play, the setting in which the debate is primarily rooted. And while it is becoming more evident that controlled shooting environments, like free throw attempts and the NBA’s three-point contest, do foster hot hand shooting (Miller & Sanjurjo (2015), Miller & Sanjurjo (2018)), it is difficult to find the existence of hot shooting in real game scenarios. If the debate is about whether the shooting patterns observed on the court show traces of the hot hand, then our analysis would add on to existing studies in 

11 

dissenting, though the more common question in modern statistical literature on the subject is whether there is hotness when controlling for shot difficulty and other external factors. Our study of game breaks suggests that pauses in game play may not have a significant effect on shooting percentage, though this finding does not necessarily apply to instances of “icing” a shooter, such as in crucial free throw shooting situations. 

Additionally, our analysis confirmed that there appears to be some changes in playing behavior as a result of a player’s previous shot, namely in the number of dribbles a player take before attempting another shot, though some players did appear to significantly change their general offensive behavior in response to their previous shot. This is consistent with findings in Aharoni & Sarig (2012), Bocskocsky et al. (2014), Csapo et al. (2015), and Rao (2009), as well as survey results from GVT. Our simulations indicate that hot hand shooting is unlikely to be found with our methods, as adding a large effect size was necessary in order to detect hot shooting behavior in our simulations. 

Three and a half decades after GVT’s original paper, the hot hand debate is still ongoing. Initially, statisticians and psychologists rejected the phenomenon, while the basketball community continued to believe in it. However, recent literature in econometrics has since seen some changed academic perspectives, with some researchers arguing for the hot hand’s existence in game settings, though this belief is not yet met with a consensus in the statistical community. With the many difficulties associated with controlling for shot difficulty, and the questionable relevance of these controls in answering the original question posed in GVT’s paper, it is unclear if or when this debate will ultimately be settled. 

## **5 Acknowledgements** 

This paper was supported in part by NSF grants DMS 1646108 and 1712962. We would also like to offer special thanks to the Statistics Department at the University of Michigan for providing us the rare opportunity to work on a meaningful research project as undergraduates. Finally, we wish to thank our friends and families for their support and encouragement throughout this process. 

12 

## **References** 

- Aharoni, G. & Sarig, O. H. (2012), ‘Hot hands and equilibrium’, _Applied Economics_ **44** (18), 2309–2320. **URL:** _http://www.tandfonline.com/doi/abs/10.1080/00036846.2011.564141_ 

- Arkes, J. (2010), ‘Revisiting the hot hand theory with free throw data in a multivariate framework’. **URL:** _https://calhoun.nps.edu/handle/10945/43641_ 

- Benjamini, Y. & Hochberg, Y. (1995), ‘Controlling the false discovery rate: a practical and powerful approach to multiple testing’, _Journal of the Royal Statistical Society: Series B (Methodological)_ **57** (1), 289–300. **URL:** _http://doi.wiley.com/10.1111/j.2517-6161.1995.tb02031.x_ 

- Bocskocsky, A., Ezekowitz, J. & Stein, C. (2014), Heat check: new evidence on the hot hand in basketball, SSRN Scholarly Paper ID 2481494, Social Science Research Network, Rochester, NY. **URL:** _https://papers.ssrn.com/abstract=2481494_ 

- Csapo, P., Avugos, S., Raab, M. & Bar-Eli, M. (2015), ‘The effect of perceived streakiness on the shot-taking behaviour of basketball players’, _European Journal of Sport Science_ **15** (7), 647–654. **URL:** _http://www.tandfonline.com/doi/full/10.1080/17461391.2014.982205_ 

- D’Amour, A., Cervone, D., Bornn, L. & Goldsberry, K. (2015), Move or die: How ball movement creates open shots in the nba, _in_ ‘Sloan Sports Analytics Conference’. 

- Friedell, N. (2019), ‘Klay ties NBA mark with 10 straight 3-pointers’. 

- **URL:** _https://www.espn.com/nba/story/_ _~~/~~ id/25821022/klay-thompson-golden-state-warriors-ties-nbarecord-10-straight-3-pointers_ 

- Gilovich, T., Vallone, R. & Tversky, A. (1985), ‘The hot hand in basketball: On the misperception of random sequences’, _Cognitive Psychology_ **17** (3), 295–314. 

**URL:** _https://linkinghub.elsevier.com/retrieve/pii/0010028585900106_ 

- Lantis, R. & Nesson, E. (2019), ‘Hot shots: an analysis of the ‘hot hand’ in nba field goal and free throw shooting’, (w26510), w26510. 

**URL:** _http://www.nber.org/papers/w26510.pdf_ 

13 

- Larkey, P. D., Smith, R. A. & Kadane, J. B. (1989), ‘It’s okay to believe in the “hot hand”’, _CHANCE_ **2** (4), 22–30. 

**URL:** _http://www.tandfonline.com/doi/full/10.1080/09332480.1989.10554950_ 

- Miller, J. B. & Sanjurjo, A. (2014), ‘A cold shower for the hot hand fallacy’, _SSRN Electronic Journal_ . **URL:** _http://www.ssrn.com/abstract=2450479_ 

- Miller, J. B. & Sanjurjo, A. (2015), ‘Is it a fallacy to believe in the hot hand in the nba three-point contest?’, _SSRN Electronic Journal_ . 

**URL:** _http://www.ssrn.com/abstract=2611987_ 

- Miller, J. B. & Sanjurjo, A. (2018), ‘Surprised by the hot hand fallacy? A truth in the law of small numbers’, _Econometrica_ **86** (6), 2019–2047. 

**URL:** _https://www.econometricsociety.org/doi/10.3982/ECTA14943_ 

- Rao, J. (2009), ‘Experts’ Perceptions of Autocorrelation: The Hot Hand Fallacy Among Professional Basketball Players’, _Working Paper_ . 

- Tversky, A. & Gilovich, T. (1989), ‘The “hot hand”: statistical reality or cognitive illusion?’, _CHANCE_ **2** (4), 31–34. 

**URL:** _http://www.tandfonline.com/doi/full/10.1080/09332480.1989.10554951_ 

- Tversky, A. & Kahneman, D. (1971), ‘Belief in the law of small numbers.’, _Psychological Bulletin_ **76** (2), 105– 110. 

**URL:** _http://doi.apa.org/getdoi.cfm?doi=10.1037/h0031322_ 

- Wald, A. & Wolfowitz, J. (1943), ‘An exact test for randomness in the non-parametric case based on serial correlation’, _The Annals of Mathematical Statistics_ **14** (4), 378–388. 

**URL:** _http://projecteuclid.org/euclid.aoms/1177731358_ 

14 

## **6 Tables** 

#### **Sample of Players Exhibiting Hot Hand Behavior in Free Throws** 

|Player<br>_P_(_H_|2_|H_1)|_P_(_H_2|_|M_1)|_r_|P-value<br>|
|---|---|---|---|---|---|
|Kevin Durant<br>0.86|(234)|0.76|(37)|0.10|4_._7_×_10<sup>_−_2</sup><br>|
|Julius Randle<br>0.82|(152)|0.61|(59)|0.22|5_._3_×_10<sup>_−_4</sup><br>|
|Andre Drummond<br>0.73|(108)|0.49|(89)|0.24|2_._9_×_10<sup>_−_4</sup><br>|
|Montrezl Harrell<br>0.76|(107)|0.64|(75)|0.14|3_._2_×_10<sup>_−_2</sup><br>|
|LeBron James<br>0.79|(111)|0.57|(67)|0.24|6_._1_×_10<sup>_−_4</sup><br>|
|Jimmy Butler<br>0.86|(141)|0.67|(21)|0.17|5_._3_×_10<sup>_−_2</sup>|



Table 1: (3.3) The player’s conditional probabilities of (H) hitting their second free throw attempt given making and missing their first attempts are listen in columns 2 and 3, respectively. The number of attempts are listed in parentheses. The serial correlation between the first and second attempts are listed in column four. The p-value of the hypothesis test _H_ 0 : _r_ = 0 versus _H_ 1 : _r >_ 0 is listed in column 5. The players listed had the five highest numbers of free throw trips (sorted in descending order) with significant serial correlations ( _α_ = 0 _._ 05) 

. 

15 

**Mean Shot Distance After a Make vs. After a Miss** 

|Player|Avg. Shot Distance After Make|Avg. Shot Distance After Miss|Z|P-value|
|---|---|---|---|---|
|Thabo Sefolosha|8.43(70)|13.09(67)|-2.72|0.0065|
|Mike Muscala|8.84(19)|16.08(26)|-2.69|0.007|
|Chris Johnson|11.40(20)|18.25(28)|-2.59|0.0096|
|Lance Thomas|11.37(108)|14.48(112)|-2.50|0.0124|
|Rajon Rondo|9.42(134)|11.86(155)|-2.31|0.0209|
|Rodney Hood|14.51|16.81|-2.28|0.0228|
|JaMychal Green|6.27(62)|9.86(59)|-2.26|0.0238|
|Dirk Nowitzki|15.67(177)|17.24(220)|-2.18|0.0289|
|Dewayne Dedmon|2.84(19)|6.00(21)|-2.15|0.0312|
|Rudy Gay|9.82(190)|11.67(231)|-2.13|0.0328|
|Al Jeferson|7.54(61)|9.73(67)|-2.09|0.0363|
|Wesley Matthews|16.88(113)|19.03(175)|-2.08|0.0372|
|James Jones|18.96(28)|22.58(38)|-2.06|0.039|
|Langston Galloway|16.61(87)|13.83(127)|1.99|0.0463|
|Brian Roberts|18.30(20)|13.70(23)|2.02|0.0435|
|Al-Farouq Aminu|15.43(129)|13.01(184)|2.08|0.0376|
|Tayshaun Prince|15.53(45)|12.13(38)|2.10|0.0355|
|Stanley Johnson|14.01(97)|11.01(168)|2.18|0.029|
|Solomon Hill|13.32(19)|4.89(19)|2.78|0.0054|



Table 2: (3.4.1) The entire NBA API dataset was used in this analysis (Number of Players = 341). The second and third columns show the mean distance (in feet) of a player’s next shot after a miss versus after a hit, with the number attempts in parenthesis. The fourth and fifth columns show Z-scores found comparing these two means and the associated p-values using the hypothesis test _H_ 0 : _µhit_ = _µmiss_ vs. _H_ 1 : _µhit_ = _µmiss_ . The table above displays those players with significant p-values ( _α_ = 0 _._ 05). 

16 

**Shot Frequency After a Make vs. After a Miss** 

|Player Name|Avg. Time After Make|Avg. Time After Miss|Z|P-value|
|---|---|---|---|---|
|Ronnie Price|175.13(31)|486.82(50)|-3.81|0.0001|
|Dwyane Wade|141.84 (209)|192.50(251)|-2.76|0.0058|
|Larry Nance Jr.|246.09(67)|462.45(53)|-2.72|0.0065|
|Trevor Ariza|221.52(140)|297.69(201)|-2.61|0.0091|
|Ryan Kelly|115.30(20)|365.57(23)|-2.53|0.0113|
|Paul Millsap|180.7(212)|233.06(214)|-2.49|0.0129|
|James Jones|213.43(28)|482.53(38)|-2.41|0.0158|
|Emmanuel Mudiay|156.89(95)|224.53(179)|-2.37|0.0176|
|Darrell Arthur|246.76(76)|394.48(94)|-2.32|0.0202|
|CJ Miles|186.81(113)|259.75(194)|-2.25|0.0246|
|Klay Thompson|144.16(257)|179.24(309)|-2.21|0.0273|
|Ersan Ilyasova|214.65(127)|290.19(179)|-2.18|0.0292|
|Andrew Wiggins|155.06(244)|189.17(303)|-2.09|0.0367|
|Sasha Vujacic|177.33(18)|320.89(47)|-2.03|0.0427|
|Al-Farouq Aminu|212.10(129)|279.88(184)|-2.00|0.0457|
|Brandon Knight|142.19(229)|167.12(332)|-2.00|0.0458|
|Bismack Biyombo|617.16(45)|395.44(39)|2.01|0.0447|
|Tony Allen|435.00(63)|296.14(84)|2.07|0.0382|
|Jarrett Jack|325.45(76)|236.49(130)|2.17|0.0299|
|Cameron Payne|385.38(37)|191.09(57)|2.18|0.0291|
|John Wall|194.63(205)|152.61(290)|2.32|0.0202|
|Patrick Beverley|348.02(83)|221.66(103)|2.40|0.0163|
|JaVale McGee|383.65(46)|164.92(25)|2.48|0.0131|
|Willie Reed|676.29(21)|157.92(12)|2.86|0.0042|
|Jef Withey|618.25(36)|247.17(35)|3.56|0.0004|



Table 3: (3.4.2) The entire NBA API dataset was used for the following analysis (Number of Players = 341). The second and third columns show the mean time difference (in ”basketball seconds”) between a player’s shots after a miss and after a hit, respectively, with the number of attempts in parenthesis. The fourth and fifth columns show Z-scores found comparing these two means and the associated p-values using the hypothesis test _H_ 0 : _µhit_ = _µmiss_ vs. _H_ 1 : _µhit_ = _µmiss_ . The table above displays those players with significant p-values ( _α_ = 0 _._ 05). 

17 

**Mean Number of Dribbles Taken Before Next Shot After a Make vs. After a Miss** 

|Player Name|Avg. # of Dribbles After Make|Average # of Dribbles After Miss|Z|P-value|
|---|---|---|---|---|
|James Ennis|0.57|1.24|-2.85|0.0043|
|Chase Budinger|0.25|0.60|-2.53|0.0115|
|Dante Cunningham|0.07|0.36|-2.50|0.0123|
|Anthony Bennett|0.28|0.50|-2.17|0.0304|
|Jeremy Lamb|1.58|2.46|-2.08|0.0376|
|Alan Anderson|0.98|1.50|-1.98|0.0477|
|Kyle Lowry|5.63|4.81|1.97|0.0485|
|Kelly Olynyk|0.78|0.52|2.04|0.0418|
|Kris Humphries|0.38|0.23|2.04|0.0414|
|Ty Lawson|5.75|4.95|2.07|0.0388|
|Ben Gordon|3.27|2.37|2.07|0.0385|
|Chris Kaman|0.96|0.68|2.10|0.0357|
|Aron Baynes|0.25|0.10|2.11|0.0352|
|Tim Duncan|0.92|0.68|2.15|0.0315|
|Trevor Booker|0.82|0.52|2.16|0.0308|
|Chris Paul|6.52|5.67|2.21|0.0270|
|Kyrie Irving|5.58|4.84|2.23|0.0260|
|Tyreke Evans|5.11|4.33|2.23|0.0259|
|Jonas Valanciunas|0.76|0.52|2.29|0.0222|
|Jarrett Jack|6.08|5.09|2.29|0.0217|
|Kemba Walker|5.69|4.73|2.34|0.0195|
|Mo Williams|5.99|4.81|2.34|0.0195|
|Donatas Motiejunas|0.88|0.62|2.36|0.0185|
|John Wall|6.22|5.34|2.37|0.0178|
|Ryan Anderson|0.89|0.66|2.39|0.0169|
|Marcin Gortat|0.58|0.35|2.39|0.0168|
|Matt Barnes|0.68|0.41|2.48|0.0133|
|Eric Bledsoe|5.16|4.20|2.52|0.0119|
|Tony Parker|6.36|5.16|2.54|0.0110|
|Lance Stephenson|3.51|2.64|2.65|0.0080|
|Lebron James|5.25|4.30|2.66|0.0079|
|Tobias Harris|1.63|1.18|2.68|0.0074|
|Isaiah Thomas|4.69|3.44|2.88|0.0039|
|Dwayne Wade|3.90|3.06|2.89|0.0038|
|Caron Butler|0.99|0.55|3.00|0.0027|
|Greg Monroe|1.37|1.04|3.00|0.0027|
|Jef Teague|6.55|5.24|3.11|0.0018|
|Boris Diaw|1.97|1.27|3.16|0.0016|
|Trey Burke|3.88|2.70|3.36|0.0008|
|Russell Westbrook|5.86|4.53|4.08|0.0000|



Table 4: (3.4.3) The NBA API dataset was filtered so each player tested had at least 15 misses and 15 hits (Number of Players = 281). The second and third columns show the mean number of dribbles a player takes before their next shot after a miss versus after a hit. The fourth and fifth columns show the Z-scores found comparing these two means and the associated p-values using they hypothesis test _H_ 0 : _µhit_ = _µmiss_ vs. _H_ 1 : _µhit_ = _µmiss_ . The table above displays those players with significant p-values ( _α_ = 0 _._ 05). 

18 

**Mean Closest Defender Distance After a Make vs. After a Miss** 

|Player Name|Avg. Distance After Make|Avg. Distance After Miss|Z|P-value|
|---|---|---|---|---|
|Joe Harris|4.37(27)|6.47(39)|-3.04|0.0024|
|Jason Terry|4.46(120)<br>|5.31(162)<br>|-2.80|0.0051|
|Arron Afalo|3.70(284)|4.14(346)|-2.49|0.0127|
|Nicolas Batum|5.31(156)|6.13(240)|-2.28|0.0229|
|Boris Diaw|4.40(170)|5.21(208)|-2.25|0.0247|
|Robert Sacre|3.33(83)|4.05(108)|-2.11|0.0351|
|Brian Roberts|4.30(124)|4.87(189)|-2.03|0.0422|
|Jared Dudley|6.04(148)|5.36(153)|2.01|0.0447|
|James Ennis|5.24(47)|4.05(70)|2.05|0.0406|
|Udonis Haslem|4.25(43)|3.11(54)|2.05|0.0401|
|Nerles Noel|3.49(169)|3.07(218)|2.10|0.0356|
|Chase Budinger|4.79 (60)|3.87(95)|2.12|0.0337|
|Blake Grifn|4.85(421)|4.36(421)|2.17|0.0301|
|Andrew Wiggins|3.67(327)<br>|3.25(411)<br>|2.17|0.0298|
|Chandler Parsons|4.57(283)|4.03(337)|2.27|0.0234|
|Brook Lopez|4.03(291)|3.51(291)|2.27|0.0230|
|Tony Allen|4.03(151)|3.07(156)|2.33|0.0198|
|Brandon Bass|3.81(196)|3.32(223)|2.39|0.0168|
|Anthony Bennett|4.97(103)|4.03(122)|2.46|0.0140|
|Carlos Boozer|3.64(292)|3.22(270)|2.49|0.0127|
|Derrick Williams|4.57(116)|3.76(124)|2.53|0.0114|
|Taj Gibson|2.92(185)|2.43(184)|2.60|0.0092|
|Zach Randolph|3.10(305)|2.67(316)|2.72|0.0065|
|Tyson Chandler|3.42(186)|2.72(97)|2.73|0.0064|
|Jeremy Lamb|5.03(77)|3.78(110)|2.90|0.0038|
|Charlie Villanueva|5.77(87)|4.68(112)|3.00|0.0027|
|Pau Gasol|4.08(369)|3.49(392)|3.09|0.0020|
|Lamarcus Aldridge|4.27(454)|3.80(544)|3.10|0.0019|
|Evan Turner|4.33(180)|3.64(260)|3.32|0.0009|
|Derrick Favors|3.30(335)|2.75(286)|3.42|0.0006|
|Kawhi Leonard|4.84(211)|3.87(263)|4.01|0.0001|
|Marc Gasol|4.55(377)|3.72(377)|4.69|0.0000|
|Quincy Acy|5.66(86)|3.79(101)|4.74|0.0000|
|Marreese Speights|4.66(231)|3.48(213)|4.94|0.0000|



Table 5: (3.4.4) The NBA API dataset was filtered so each player tested had at least 15 misses and 15 hits (Number of Players = 281). The second and third columns show the mean distance (in feet) from the closest defender on their next shot after a miss versus after a hit, respectively. The fourth and fifth columns show the test statistic and its corresponding p-value for the test _H_ 0 : _D_ hit _− D_ miss = 0 versus _H_ 1 : _D_ hit _− D_ miss = 0, where _D_ is the mean closest defender distance. The table above displays those players with significant p-values ( _α_ = 0 _._ 05). 

19 

**Shooting Performance Before Halftime versus Shooting Performance After Halftime** 

|Pre-Half Shots|Post-Half Shots|Shots/Half (Pla|yers)|_FGPpre_|_FGPpost_|r|P-value|
|---|---|---|---|---|---|---|---|
|Last 3|First 3|12486|(331)|0.4640|0.4646|-0.0067|0.3322|
|Last 4|First 4|6992|(236)|0.4723|0.4715|-5.22 _×_10<sup>_−_5</sup>|0.4991|
|Last 5|First 5|3020|(129)|0.4682|0.4645|-0.0682|0.04707|
|Last 6|First 6|1032|(78)|0.4767|0.4922|0.04969|0.7413|
|All in Q2|All in Q3|17585, 18886|(331)|0.4672|0.4647|0.0108|0.7567|



Table 6: (3.5) The NBA API dataset was filtered to include only data from quarters where players attempted at least three shots in quarters two and three before conducting each analysis. Columns 1 and 2 show the subset of shots from each half analyzed for each player in games where the player attempted a sufficient number of shots. Column three shows the total number of shots considered for each half (these values were the same for each half except in the last row, where there were 17,585 shots from before halftime, and 18,886 from after halftime). Columns four and five show the global field goal percentages from the subsets of shots pre-halftime and post-halftime, respectively. Column six shows the correlation between a player’s individual pre-half field goal percentage and their corresponding post-half field goal percentage, and column six reports the accompanying p-value for the test ( _H_ 0 : _r_ = 0 vs _H_ 1 : _r <_ 0) 

20 

## **7 Figure Captions** 

Figure 1: (3.6.1) The output of an FDR (Benjamini & Hochberg 1995) analysis for values of _δ_ ranging from 0 to 0.6. For 21 different values of _δ_ , 10 simulations were generated, for a total of 210 simulations. The Benjamini-Hochberg output (for _α_ = 0 _._ 05) comes from analyzing the p-values of the Wald-Wolfowitz test of each player’s simulated shot results (Number of Players = 438), with the simulations generated using equation (2). A significant number of discoveries (more than 22) is first seen at at _δ_ = 0 _._ 39. The red line marks the threshold for a significant number of declared discoveries. 

Figure 2: (3.6.2) The global test statistics (using equation (1)) from each of the 210 simulations also used in Section 3.6.1 (Number of Players = 438). This analysis was used in Section 3.2 to globally test if _ph −pm >_ 0. As _δ_ increased, the global test statistic increased, gradually growing more significant. Clear evidence of a global hot hand ( _T >_ 0) is seen around _δ_ = 0 _._ 18 and beyond. 

21 

**8 Figures** 

**Fig. 1: Simulation of Wald-Wolfowitz Test** 



22 

**Fig. 2: Simulation of Global t-test** 



23 


