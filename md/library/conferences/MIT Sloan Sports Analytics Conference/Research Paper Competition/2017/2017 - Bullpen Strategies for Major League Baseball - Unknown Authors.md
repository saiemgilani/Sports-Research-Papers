<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2017/2017 - Bullpen Strategies for Major League Baseball - Unknown Authors.pdf -->



# **Bullpen Strategies for Major League Baseball** 

Paper Track: Baseball Paper ID: 1684 

## **1. Introduction** 

As never before, Major League Baseball (MLB) teams are turning to analytics in an attempt to gain a number of small advantages that, in the composite, may result in signi􀅭icantly altering the odds of winning in their favor. This changing mindset was on full display during the 2016 MLB postseason, where teams showcased several strategies attributed to the 􀅭ield of sabermetrics [3, 6, 8]. One of these was their interesting use of relief pitchers; post-season managers removed starting pitchers from games earlier than in any other postseason to date [2], perhaps to avoid high pitch counts [12] or to prevent opposing lineups from seeing the same pitcher too many times during a single game [10]. The result was, according to popular media, one of the most exciting World Series in recent memory [11]. 

Several issues arise when witnessing paradigm shifts in how baseball is played, and this paper attempts to address two interesting ones surrounding the potential use of relief and starting pitchers. Firstly, we look at the home-􀅭ield advantage and propose a strategy for starters of visiting teams that can be used to remove roughly one half of the 􀅭irst-inning advantage to the home team. A byproduct of this analysis is a set of proper adjustments that must be made to calculate the true home-􀅭ield advantage, which is roughly 0.429 runs/game, rather than the 0.133 runs/game suggested by the scoring data. Secondly, we wish to tackle the age-old question of when to remove a pitcher from a game by proposing a pitcher-by-pitcher analysis that utilizes data that can be easily measured during a game for real-time decision making. 

Since each of these two topics can be addressed independently, they are discussed separately in Sections 2 and 3, respectively. We then conclude the paper in Section 4 with a summary of the pitching strategies of the paper, and a list of potential bullpen tactics for future research. 

## **2. Mitigating the Home Field Advantage** 

In this section, we discuss sources of the home 􀅭ield advantage, and identify the 􀅭irst inning as the most advantageous inning for the home team. We propose a novel strategy for starters when pitching on the road that can remove a signi􀅭icant piece of the 􀅭irst-inning advantage from the home team, and discuss the implications of our 􀅭indings. The data used to form the results of this section are from retrosheet.org [1], and speci􀅭ically include game log data from 1980--2015. These data were selected because it was shown in [16] that the home team’s advantage in scoring has been roughly the same since the 1980s, but experienced a (thus far unexplained) jump in the 1970s. Data selection was, therefore, made to keep our 􀅭indings and strategies applicable to the game in its current state. For simplicity, only games that lasted at least 51 outs in which the home team batted last are included in the analysis of this section, and following the convention in [16], all extra innings were compiled together and are presented as the “10th inning.” 





2017 Research Papers Competition Presented by: 

1 





<!-- Start of picture text -->
0.7 0.1<br>0.6 0.05<br>0.5 0<br>0.4 -0.05<br>0.3 -0.1<br>0.2 Home (sh ) -0.15<br>i<br>0.1 Visitors (svi) -0.2 Actual Difference<br>Home Estimates Estimated Difference<br>0 -0.25<br>2 4 6 8 10 2 4 6 8 10<br>Inning Inning<br>Inning-wise Run Differentials (d) i<br>Average Runs Scored per Game Played<br><!-- End of picture text -->

Figure 1: LEFT: Average number of runs scored by inning for home and visiting teams. RIGHT: Average run differential by inning calculated as home teach score minus visiting team score. Since the home team does not bat in the bottom of the last inning once they have the lead, the true advantage to the home team in the 9th and 10th innings must be estimated using other techniques, and these estimates are also included in the 􀅭igures. 

### **2.1. Background** 

Over 80,000 regular-season baseball games were played in the Major Leagues from 1980--2015, and home teams won 53.93% of those games. Home teams scored a total of 370,331 runs (4.597 runs per game) during that stretch compared to 359,589 runs (4.464 runs per game) produced by visiting teams. The overall scoring differential can then be calculated to be 0.133 runs per game, and could have been higher if the bottom of the last inning were always played to three outs. Much research has been done to attempt to identify the sources of the home-􀅭ield advantage (see [4] and references). Everything from team travel schedules to umpire bias [13] to familiarity with the home ball park has been analyzed, and many of these factors have been shown to be possible sources of the bias toward the home team. When one investigates this advantage by inning, it is surprising to 􀅭ind that a large portion of the scoring differential between home and visiting teams occurs in the 􀅭irst inning [16, 17, 19]. Let _n_ = 80,554 be the number of total games in the data sample, and let _shi_ ( _svi_ ) be the average number of runs scored by the home (visiting) team in inning _i_ for _i_ = 1 _,_ 2 _, . . . ,_ 10; i.e., 



and similarly for _svi_ for _i_ = 1 _,_ 2 _, . . . ,_ 10 _._ Then inning-wise scoring differentials are calculated as 



Figure1showsboth _shi_ and _svi_ intheleft-most􀅭igure, and _di_ intheright-most􀅭igurefor _i_ = 1 _,_ 2 _, . . . ,_ 10. Perhaps the most glaring problem with these calculations is that the data appears to indicate that the visiting team has a scoring advantage in innings 9 and 10, but this is actually not true and will be addressed later on. For now, simply note that the estimates represented with black dotted lines and square markers are likely more accurate when measuring the true advantage to the home team for innings 9 and 10. 

The 􀅭irst inning differential between home and visitor scoring in the regular-season data set from 1980--2015 is _d_ 1 = 0 _._ 09 runs, which seems to indicate that the 􀅭irst inning is responsible for roughly 



2017 Research Papers Competition Presented by: 



2 



67.5% of the overall home team advantage of 0.133 runs per game. This approach is actually taken in [16] by Smith (although his 􀅭igure comes out to be only 58% when he takes data from 1909--2013 into account), where he argues that the biggest reason that a home-􀅭ield advantage exists is because there is a 􀅭irst inning (although we feel this number is actually much too high and will provide more accurate estimates later). Furthermore, in [17] Smith goes on to show that the advantage of a home team in the 􀅭irst inning is highly correlated ( _R_<sup>2</sup> = 0 _._ 86) with the length of the top of the 􀅭irst inning in time (the linear 􀅭it indicates an extra run for the home team in the bottom of the 􀅭irst inning for every 90 seconds beyond 6 minutes for the top of the 􀅭irst). The connection is that it appears the starter on the visiting team is effectively “cooling down” in the dugout during the top of the 􀅭irst, and when he 􀅭inally pitches in the bottom half of the inning, he is less prepared to face the opposing lineup. Similar results were found in [19], where it is shown that pitchers’ velocity in the 􀅭irst inning tends to be much higher when the pitcher is at home verses when he is on the road. Also, strike-out-to-walk ratio (K/BB) in the 􀅭irst inning is affected, tending to be smaller when pitchers are on the road versus at home. 

### **2.2. Methodology** 

### **2.2.1. Estimating the 9th and 10th Inning Differentials** 

We wish to 􀅭irst properly estimate the percentage of the home-􀅭ield advantage that exists in the 􀅭irst inning, and then propose a simple strategy for visiting teams to mitigate much of that 􀅭irst-inning bias. The problem with stating that the 􀅭irst inning is worth 67.5% of the overall home-􀅭ield advantage is that the true baseball data shows advantages in run differentials for visitors in both the 9th and 10th innings, but if this were true we would expect visiting teams to win more extra inning games. For the 7,246 extra inning games in our data set, however, the home team still managed to win 52.43% of them. The negative differentials in Figure 1 for innings 9 and 10 arise because when the home team wins, it doesn’t use all of its outs in the bottom of the last inning; and thus estimates favor the visiting team even though the visitors remain at a disadvantage throughout the game. 

Consider, for example, an extra inning game in which the visitors score six runs in the top of the 10th, and the home team scores zero runs in the bottom of the 10th. In this case, all six runs scored contribute to the statistic _sv_ 10. Consider now the exact opposite, a game wherein the home team would have scored six runs in the bottom of the 10th, and the visiting team scores zero runs in the top of the 10th. Except in the case of a multi-run walk off home run, the home team would be credited with only one run to contribute to _sh_ 10, and the overall statistic is devalued even though the home team wins the game. 

Some strategies for estimating the 9th and 10th inning data points are (a) to consider only a subset of the innings played, or (b) to give estimates based on the number of outs used in the inning; but both of these techniques are 􀅭lawed and will result in biased estimates in favor of the visitors by discounting cases where home teams were likely to score more runs and counting cases where they were unlikely to score more runs. Thus, our approach to making these estimates is to trust the overall home-􀅭ield advantage (since home teams still win a majority of extra-inning games), and apply an average differential to _sv_ 9 and _sv_ 10 to estimate average home team scoring potential in these innings. We de􀅭ine _d_ ave as the average scoring differential using innings three through eight, discounting innings one and two because of irregular behavior in the differential ( _d_ 1 is an in􀅭lated differential and _d_ 2 is a de􀅭lated differential, probably due to the home team being closer to the bottom of the order in the second inning). We must be careful in our calculation of the 10th inning because only a portion of games actually have extra innings, and thus there is an extra weighting parameter required to accurately estimate the 10th 



2017 Research Papers Competition Presented by: 



3 



inning advantage. To be speci􀅭ic, 



and ˆ _shi_ signi􀅭ies the estimate of _shi_ if the bottom of the last inning was always played to three outs. The probability that the 9th inning is played is one for our data set, and the probability that the 10th inning is played is 0.1973, which is the number of extra innings divided by the number of games in the data set. Estimates are given in Figure 1, and _d_ ave = 0 _._ 0419 for our dataset. Using these estimates, we are able to get a better idea of the total advantage to the home team, and likewise the overall percentage of the advantage experienced in the 􀅭irst inning. If we choose to ignore this subtlety, we ignore the fact that the home team has an advantage throughout the bottom of the last inning, whether or not they actually use it in a real game.<sup>1</sup> 

### **2.2.2. First-Batter Starter Strategy** 

Now, we propose a novel strategy for removing a signi􀅭icant chunk of the home-􀅭ield advantage, assuming that the chief reasoning behind the elevated advantage in the 􀅭irst inning is due to suboptimal timing of the warmup for a visiting starter. Our strategy allows the effective “starter” to warmup both before the game and during the top half of the 􀅭irst inning, because he will not actually start the game. Some [5] have advocated for the use of relief pitchers to pitch the 􀅭irst inning in the role of an “opener,” but this strategy would not solve the problem of the opener cooling down in the top of the 􀅭irst. Instead, we propose a “􀅭irst-batter starter.” Although some people will hate this strategy because it means one more relief pitcher in the game, it stands to reason that if a starter is made less effective by sitting in the dugout during the top of the 􀅭irst inning rather than warming up, a visiting team should want to be subject to that disadvantage for as little time as possible. The rules of baseball actually allow for pitching substitutions mid at-bat, but only if the pitcher to be replaced has already pitched to at least one complete batter or is injured [14]. We assume that the 􀅭irst-batter starter will be at the heightened disadvantage of _d_ 1 runs/inning for one batter (probably a high estimate since this pitcher can throw as hard as he likes knowing he only needs to face one batter), and can then be replaced with the effective starter fresh from the bullpen, who will only be subject to the regular differential of _d_ ave runs/inning. Using data from 2015, we calculate the average number of plate appearances per inning as 



where AB: at-bats, BB: walks, IBB: intentional walks, HBP: hit by pitch, SF: sacri􀅭ice 􀅭lies, SH: sacri􀅭ice hits (bunts), CI: 􀅭irst base awarded for catcher interference, and PO: put outs by opposing team, and all these stats are at the per-game level. Notice, this is simply the fraction of all plate appearances that we’d expect to see over the span of three outs in a baseball game. This calculation gives PA<sup>¯</sup> _h_ = 4 _._ 30 

> 1Several works actually make this error by calculating the number of runs they feel a source of the home-􀅭ield advantage is worth, and then simply taking a ratio against actual scoring, like in [13] where the authors claim that umpire bias is worth 2/3 of the home-􀅭ield advantage, but their methods actually give a number close to 1/5 when the total advantage is properly calculated. One sure effect of this miscalculation is the overestimation of the importance of speci􀅭ic items to the home-􀅭ield advantage in baseball. 





2017 Research Papers Competition Presented by: 

4 



(PA<sup>¯</sup> _v_ = 4 _._ 21) plate appearances per inning for home (visiting) teams. Now we have everything we need to estimate a new 􀅭irst inning differential given the 􀅭irst-batter starter strategy as 



### **2.3. Results and Discussion** 

The results of our study indicate that the 􀅭irst run differential of _d_ 1 = 0 _._ 09 is actually only 21% of the total home-􀅭ield advantage, which of course is quite at odds with the 67.5% calculated earlier (or even the 58% reported in [16]), but has a much more intuitive feel. After all, if the 􀅭irst inning differential is around twice the differential for any other inning, it stands to reason that most innings account for about 10% of the advantage, and the 􀅭irst inning should be around twice that number. A full listing by inning of the average advantage to the home team in runs/game and percentage of the whole is given in Table 1. 

Table 1: Run differentials after the adjustment and percentage of total home-􀅭ield advantage in each inning. 

|Inning|1|2|3|4|5|6|7|8|9|10|Total|
|---|---|---|---|---|---|---|---|---|---|---|---|
|_di_(runs/game)|0.09|0.04|0.05|0.03|0.05|0.04|0.04|0.04|0.04|0.01|0.43|
|_di_(%-age of whole)|21.0|8.6|12.2|7.8|11.7|9.1|8.9|9.0|9.8|1.9|100|



We also found that the new value of _d_ 1 that could be possible by having a 􀅭irst-batter starter for away games is _d_<sup>ˆ</sup> 1 = 0 _._ 053 runs/game, which could be a high estimate. This has the potential to remove approximately 0.037 runs/game (about 8.6%) of the total home-􀅭ield advantage. While this may appear to be a small amount, we remind the reader that this shift requires no training, hard work, or discipline of any kind; only a (perhaps uncomfortable) trip to the mound for the manager during the 􀅭irst inning of each and every away game of a season. Over the course of 81 away games per year, this amounts to roughly 3 runs, which could easily result in an extra win (17.8% of the games in our database were lost by the visiting team by exactly one run). 

## **3. ComparisonofStartingtoReliefPitchersusingDataAnalytics** 

We now shift our attention to the second question addressed in this paper: when should a manager remove a pitcher from a baseball game? It is safe to say that this question has yet to be answered in a way that satis􀅭ies managers, players, owners, and fans alike. It was discussed at length in [18] how managers have been in possession of various data sets for years as well as indicators that should apply when deciding whether or not to remove a pitcher; and yet, managers still feel that their “gut instinct” is more valuable at times than all the data in the world. This is likely because good managers are, in fact, internalizing crucial pieces of data that help them to make good clutch decisions, and the analytics has yet to incorporate all of these data into a workable system. This section provides a simple system based on pitch counts and the strike-to-ball (STB) ratio that make up a nice start towards this end. While simple, it is surprising what can be learned through these two observable variables. This section provides evidence that pitchers’ effectiveness can, in fact, be monitored in real time, giving 



2017 Research Papers Competition Presented by: 



5 





<!-- Start of picture text -->
4,000<br>3,500<br>3,000<br>2,500<br>2,000<br>1,500<br>1,000<br>500<br>0<br>Pitcher<br>Starter or Non-Starter NS S<br>Number of Pitches<br>shiej002quinj001salec001 richg002gibsk002lackj001zimmj003lirif001 dankj001bauet001 hestc001 hammj002pelfm001chavj001weavj003gonzm003voger001warra001 mccul002 mortc002 may-t001iwakh001 peraw001coloa001 handb001 norrb001 linct001 delgr001buchd001 wrigs001famij001camia001 worlv001 hoovj002shrec001 osunr001 axfoj001melam001 moorm003 sampk001streh001 badeb001 diazj005rossr002 hughj001dunnm002 milla002 boyeb001torrc001 lambj002madsr001 gregl001stord001 cecib001 lowem002 mottj001petrj001cedex001 eickj001loupa001frees001 cahit001 cingt001araue001 bedrc001 mcgej001cunnb001 rzepm001godlz001webbd001 millj006lopej002adama001 penaa003aardd001 peraj002banum001 givem001rolld002 matzt001 corrk001 gofod001martc007 ohler001 rasmc002 tonkm001 alvah001 gracm003ranaa001 crock001 houst002 kensl001 ramin002 claua001 mendr002 cookr001 bracs001 kellc001 schua001 cothc001 pimes001baila001 belir001 hallc001 tsaoc001 goodn001sorir001 barry001balfg001pazoj001kohnm001 domij002guerj003roacd001 surke001 wilka001 guerj002fujik001cabrc001<br><!-- End of picture text -->

Figure 2: Stacked bar graph of the number of pitches by pitcher in 2015, sorted in descending order. Blue sections of bars indicate starting pitchers, while red sections of bars represent non-starting pitches. A large majority of pitches from a player will be of one of the two types (i.e. Starter or NonStarter). 

managers straightforward techniques for deciding when to replace a pitcher. We use play-by-play 􀅭iles from Retrosheet.org [1] for the 2015 season for the analysis of this section. 

### **3.1. Methodology** 

Almost 700,000 pitches were observed and recorded during the 2015 MLB season. These pitches came from 712 different pitchers for an average number of just under 24 different pitchers per team. Since a team’s active roster is comprised of only 25 players (usually with only 􀅭ive starters), it is evident that franchises are indeed using and seeking to leverage the bullpen in many ways to help relieve, close, and save games. 

Figure 2 shows the sorted distribution in descending order of all pitches across the 712 pitchers. Here we see that 325 different pitchers started at least one of the 2,429 games in 2015 (counting both home and visiting teams there were 4,858 total starts for the season). Collectively, these 325 starters (45% of the 712 pitchers) hurled over 64% of the balls originating from the mound before leaving the game. These 461,317 pitches are colored in blue on Figure 2. The non-starter pitches are colored in red (36% of the total area) on the same 􀅭igure. 

Interestingly, of the 325 “starters” 174 of them (53.5%) also pitched in a non-starting role at least once during the season. Analysis reveals that an additional 48,923 pitches come from these “starters” when they are not starting (10% of their pitches are in relief of other starters). 

Figure 2 suggests that there is indeed mixing of roles in the individual games. Naturally, teams are responding to the season’s game schedules, unforeseen injuries, and experimental contracts with minor league players. We propose that, among other strategies, this “mixing” can be extended such that a franchise employs twice as many starters (10) and uses them in much more varied sequences, specialized match-ups, and different rotations. 





2017 Research Papers Competition Presented by: 

6 





<!-- Start of picture text -->
100 100<br>Y = 3.20 + 1.607*Balls Y = 3.20 + 1.607*Balls<br>80 80<br>60 60<br>40 40<br>20 20<br>0 0<br>0 10 20 30 40 50 60 70 80 90 100 0 10 20 30 40 50 60 70 80 90 100<br>Balls Balls<br>Strikes Strikes<br><!-- End of picture text -->

Figure 3: Plots of strikes versus balls for three games (LEFT) and all games (RIGHT) in which Jake Arrieta started during the 2015 MLB Season (colored by game). 

In order to quantify the validity of this proposition, we look at the pitch-by-pitch performance of the starters versus the non-starters. We track the strikes, balls, and STB ratio with respect to the pitch count to ascertain if indeed closers could start, i.e., perform equal to or better than starters, but for a smaller number of innings. Data is aggregated across different groups and categories with comparisons between teams and individual pitchers. 

### **3.2. Results and Discussion** 

The STB ratio can be a useful metric to evaluate the current state or health of a pitcher. The authors recognize that this ratio is not the only pitching statistic that matters and have even developed derivatives of the popular ERA statistics (see [15]). However, for purposes of initial comparisons between pitchers within the scope of this paper, this statistic provides a wealth of information that should be analyzed prior to complicating the matter. Undoubtedly, similar comparisons and analyses using other measures, including the component ERA statistic, will be explored in the future. 

The left-most plot of Figure 3 displays balls to strikes throughout three games in which Jake Arrieta of the Chicago Cubs started in 2015. The straight grey line, with accompanying equation at the top left ( _Y_ stands for strikes), indicates the linear regression of all of his games in 2015 based on the relationship between balls and strikes. In other words, this line represents an expected strike-to-ball ratio at which Arrieta should be at for different pitch counts. For one of the three games represented, Arrieta followed this line almost exactly the entire game. In the other two games, Arrieta was pitching either above or below his average strike-to-balls ratio for much of the game. When a pitcher pitches signi􀅭icantly below his average trend line, this may be an indicator that he is fatigued or experiencing other issues that may lead to a bad start. On the other hand, when a pitcher pitches above this line, this may be an indicator that he will pitch at levels above his average throughout the night. Of course, at anytime a pitcher may regression back towards his mean, and therefore early signs of superior or 



2017 Research Papers Competition Presented by: 



7 





<!-- Start of picture text -->
Arrieta Chen<br>140<br>100<br>Y = 3.201 + 1.607*Balls Y = 4.689 + 1.843*Balls<br>120<br>100<br>80<br>80<br>60<br>60 40<br>20<br>0<br>40<br>Pitch Count<br>20<br>0<br>0 10 20 30 40 50 0 10 20 30 40 50<br>Balls<br>Strikes<br><!-- End of picture text -->

Figure 4: Plot of strikes versus balls for all pitching sequences for Jake Arrieta (LEFT) and Wei-Yin Chen (RIGHT) during the 2015 MLB Season colored by pitch count. 

inferior pitching should be taken with a grain of salt. 

The right graph in Figure 3 extends this concept to all 33 games in which Arrieta started in the same year with the best 􀅭it line reproduced from the left hand 􀅭igure. Although, each game is represented in a different color, certain strike and ball combinations are reached in multiple games and therefore many “strike-to-ball pro􀅭iles” are observable in his overall dataset. 

The most signi􀅭icant number in the equation for 􀅭it lines is the slope coef􀅭icient, which appears as a multiplier to the “Balls” variable. This slope is a measure of the strike-to-ball ratio (STB), which is generally desired to be as large as possible (although we also note that hits are counted as strikes, so is it theoretically possible to have an excellent STB while still being ineffective as a pitcher). 

By overlaying the pitch count on top of the strike-to-ball region for Arrieta as shown in Figure 4, one can readily see the 􀅭inal ratio with respect to the pitch count in multiple games. In the same 􀅭igure, the analysis is performed for Wei-Yin Chen, who actually has a higher slope for the 􀅭it line but a much wider strikes-to-balls region, with more games signi􀅭icantly deviating from the trend line. In terms of the number of pitches per game, Arrieta averaged 106 pitches per game while Chen averaged 97. Also, Chen’s ERA, 3.34 for 2015, was almost twice that of Arietta’s, 1.77 suggesting that many of Chen’s “strikes” resulted in more hits and runs in comparison. 

Comparisons between pitchers using this method can now be explored. In Figure 5, the strikes-toballs pro􀅭iles for all Chicago Cubs pitchers are presented for the 2015 season. The familiar region and best 􀅭it line for Arrieta is contrasted with 24 other pitchers during 2015. The slopes and best 􀅭it lines are generally the steepest for starting pitchers, with the small regions very rarely composed of more than 40 pitches for relief or closing pitchers. Figure 5 shows that occasionally some non-starting pitchers, such as Richard, Wada, and Wood offer STB ratio 􀅭it lines that are in fact better than the starters. Although the reduced data at higher pitch counts suggests caution for predicting the performance of these pitchers over more innings, the potential to leverage these pitchers in other ways could be an 



2017 Research Papers Competition Presented by: 



8 



advantage without loss of average team performance. 

Combining these strike-to-ball regions for all 30 teams and for all 712 pitchers from the 2015 season results in the left hand side of Figure 6. This aggregate region, with associated 􀅭it line, illustrates the typical range of performance expected by any professional major league pitcher. The coloring is based on frequency quantiles demonstrating that many more pitching states have, as expected, combinations of a low number of balls and strikes. On the other hand, certain strike and ball combinations may occur only once in a season such as the one pitcher’s STB pro􀅭ile extending out to approximately 45 balls and 21 strikes towards the bottom. In fact, this particular pro􀅭ile by pitcher Tyler Matzek is a true outlier. After the 􀅭irst batter in the game was grounded out, Matzek threw 9 straight balls. Amazingly, the Colorado Rockies were able to 􀅭inish the inning without giving up any runs. In the second inning, Matzek threw 8 balls in a row. Again, the Rockies’ defense let no runs. Finally, in the third inning after 6 straight balls Matzek was eventually pulled, producing the lowest strikes-to-balls ratio for the whole season with more than 50 pitches. Arizona never scored against him but eventually went on to win the game. 

The right hand side of Figure 6 shows the distribution of the STB for all 712 pitchers, with an average value of 1.32. This average is lower than the STB coef􀅭icient of 1.603 for the entire league on the left hand side. The main reason this is observed is an artifact of the larger number of events close to the bottom left corner of the strikes versus balls graph driving the slope higher. This effect is also seen in Figure 7 where the league pitchers are divided into starting pitchers (on the right) and pitchers which never start (on the left). The corresponding STB coef􀅭icients are again presented in the equations for the best 􀅭it lines at the top left. As expected, the starters are much more pro􀅭icient overall at delivering more strikes to the plate than balls. In addition, the non-starting pitchers are often replaced more quickly if performance appears to be below average. Therefore, in the left hand side of Figure 7 above average performing relief pitchers are permitted to continue to higher pitch counts (i.e. pro􀅭iles above the best 􀅭it line). However, in both cases the trend line is dominated by a majority of activity at low strike and ball counts. 

Extracting the STB coef􀅭icients for all 712 pitchers and plotting these values with respect to the number of pitches in a season is shown in Figure 8. As before, the data points are colored based on starting (blue _•_ ) or non-starting (red +) pitchers. A distinct difference between the starters and nonstarters is apparent in Figure 8. The categorization of these two groups was seen previously in Figures 2 and 7 where a “bend” in the order of pitchers sorted by number of pitches was observed and the STB coef􀅭icients were different for the two groups, respectively. However, Figure 8 also shows that a signi􀅭icant number of pitchers that never start are able to match or even exceed some starting pitchers with respect to STB over a shorter time frame. This suggests that relief or closing pitchers potentially have the capability to replace starting pitchers much earlier in the game if in fact the starter is showing signs of either fatigue or slumping performance. In addition, there is a distinctive absence of pitchers in the 1,200 to 2,000 pitch count and in a range of STB from 1 to 1.25, or where the sharp cut-off in the distribution is observed. This suggests that the potential to have pitchers train and perform in a type of hybrid role between the two traditional extremes of starters and closers may be untapped. Although this would necessitate alterations to pitching schedules and training regimens, a “three inning” pitcher that plays in every third or fourth game could increase team performance, and potentially be more cost effective as well. 

Extending this STB analysis further can provide an additional metric in judging when to pull a pitcher from the mound. Figure 9 presents 10 pitchers from the Chicago Cubs, 􀅭ive starters on the top row, and 􀅭ive relief pitchers on the bottom row. Each subgraph has two parts. In the bar chart section of each player’s subgraph, the bars represent the frequency with which the player reaches different pitch 



2017 Research Papers Competition Presented by: 



9 





<!-- Start of picture text -->
Arrieta Beeler Coke Edwards 140<br>100<br>80 Y = 3.201 + 1.607*Balls Y = -1.967 + 1.511*Balls Y = 0.9386 + 1.359*Balls Y = 2.169 + 0.9557*Balls 120<br>60<br>40 100<br>20<br>0 80<br>Germen Grimm Hammel Haren<br>100 60<br>80 Y = 1.813 + 1.106*Balls Y = 0.7778 + 1.006*Balls Y = 0.5832 + 1.791*Balls Y = 1.677 + 1.621*Balls<br>60 40<br>40<br>20<br>20<br>0<br>0<br>Hendricks Lester Medina Motte<br>100<br>80 Y = 2.576 + 1.586*Balls Y = 4.23 + 1.523*Balls Y = 0.2807 + 1.293*Balls Y = 1.859 + 1.129*Balls Pitch Count<br>60<br>40<br>20<br>0<br>Ramirez Richard Roach Rodney<br>100<br>80 Y = 2.105 + 0.771*Balls Y = 1.518 + 1.874*Balls Y = -2.605 + 1.48*Balls Y = 1.297 + 1.009*Balls<br>60<br>40<br>20<br>0<br>Rondon Rosscup Russell Schlitter<br>100<br>80 Y = 1.622 + 1.245*Balls Y = 1.61 + 1.031*Balls Y = 0.6618 + 1.364*Balls Y = 1.019 + 0.7777*Balls<br>60<br>40<br>20<br>0<br>Soriano Strop Wada Wood<br>100<br>80 Y = 3.018 + 0.6845*Balls Y = 2.039 + 0.8066*Balls Y = 0.7513 + 1.81*Balls Y = 1.576 + 1.642*Balls<br>60<br>40<br>20<br>0<br>0 10 20 30 40 50 0 10 20 30 40 50 0 10 20 30 40 50 0 10 20 30 40 50<br>Balls<br>Strikes<br><!-- End of picture text -->

Figure 5: Plot of strikes versus balls for all pitching sequences during the 2015 MLB Season for the Chicago Cubs (colored by pitch count). 





2017 Research Papers Competition Presented by: 

10 





<!-- Start of picture text -->
100<br>Y = 1.687 + 1.603*Balls<br>99% (12000)<br>74% (2917)<br>49% (752) N<br>75<br>25% (345)<br>0% (0)<br>50<br>25<br>0<br>0 10 20 30 40 50 60 0 0.5 1 1.5 2 2.5<br>Balls SB Ratio<br>Strikes<br><!-- End of picture text -->

Figure 6: LEFT: Plot of strikes versus balls for all pitching sequences during the 2015 MLB Season. RIGHT: The distribution of strike-to-ball ratios for all 712 pitchers. 

counts. For example, in all 33 starts by Arrieta, he reached at least 70 pitches. However, in fewer and fewer games he reaches 100 or 110 pitches. Below the bar chart is a mean strike-to-ball ratio for the 33 games at a particular pitch count. In other words, this line represents the typical strike-to-ball ratio expected with respect to Arrieta’s pitch count. Interestingly, there seems to be a small strike-to-ball 



<!-- Start of picture text -->
NS S 150<br>100<br>Y = 1.416 + 1.245*Balls Y = 3.824 + 1.534*Balls 125<br>100<br>75<br>75<br>50<br>25<br>0<br>50<br>Pitch Count<br>25<br>0<br>0 10 20 30 40 50 0 10 20 30 40 50<br>Balls<br>Strikes<br><!-- End of picture text -->

Figure 7: Plot of strikes versus balls for all pitching sequences during the 2015 MLB Season. Pitchers who started (S) at least once are shown collectively on the right, and pitchers who never started (NS) are shown collectively on the left. 



2017 Research Papers Competition Presented by: 



11 





<!-- Start of picture text -->
3.0<br>2.5<br>2.0<br>1.5<br>1.0<br>0.5<br>0.0<br>0 500 1,000 1,500 2,000 2,500 3,000 3,500 4,000<br>Number of Pitches<br>Type of Pitcher NS S<br>Strikes-to-Balls Ratio<br><!-- End of picture text -->

Figure 8: Plot of 712 pitchers’ strikes-to-ball ratio versus the total number of pitchers for the entire 2015 MLB season. Pitchers who started (S) at least once are shown in blue, while pitchers who never started (NS) are shown in red. 

ratio peak early in his games before he settles in to his average performance around 1.8. Note that this value is different than the STB coef􀅭icient using the best 􀅭it line described previously. 

In this case, we take the average of the strike-to-ball ratio at each pitch count value (i.e. 33 data points up until 72 total pitches, afterwhich the number of data points decreases). This means that near the end or tail of the distribution, lower con􀅭idence is expected in the results due to less data. However, before that point is reached some interesting observations can be made. At relatively high pitch counts, a local drop in the mean strike-to-ball ratio line is observed. This is most evident in Lester’s STB ratio line around pitch number 100, but can also be seen in Hendricks’s around pitch 80 and twice for Hammel’s near pitch 65 and pitch 90. Arrieta’s drops less so at pitch 100 and Haren’s does too, although with more uncertainty in the latter case, due to less data. 

These changes in performance can be used as trigger points to evaluate if a pitcher is tired or reaching his limit in other ways and perhaps needs to be pulled. Ideally, the signs should be recognized before an undesirable performance makes it obvious and therefore analyzing when and how each pitcher reveals his fatigue in such pro􀅭iles presented here can be fruitful. Since relief pitchers will play in more games than a starter in a give season (e.g., 68 for Rodney), uncertainty should be lower, but over a shorter range of pitch counts. Still, the strike-to-ball ratio line can be used to ascertain when the pitcher is deviating from his expected performance, and modi􀅭ications can be made if needed. 

Lastly, analyzing the non-starting pitchers can also provide insight into when and how they should be used. For example. Rondon’s STB line peak is higher than most starters but he quickly loses steam and falls back to an average starter after 10 or 15 pitches. However, falling “back to average” is still an attractive proposition if he can maintain that rate for more pitches. Although the data is sparse, there seems to be some evidence that he does not continue to fall since the line turns back up around 25 pitches. 

Rosscup and Strop, on the other hand, have a similar peak but continue their burnout phase after only a few pitches. The others offer some indication that they could be used or trained to become more 



2017 Research Papers Competition Presented by: 



12 





<!-- Start of picture text -->
Arrieta Hammel Haren Hendricks Lester<br>60<br>50<br>40<br>20<br>0<br>2.5<br>2<br>1.5<br>1<br>0.5<br>Rodney Rondon Rosscup Russell Strop<br>60<br>50<br>40<br>20<br>0<br>2.5<br>2<br>1.5<br>1<br>0.5<br>0 50 100 0 50 100 0 50 100 0 50 100 0 50 100<br>Number of Pitches<br>Games<br>SB Ratio<br>Games<br>SB Ratio<br><!-- End of picture text -->

Figure 9: Chicago Cubs’ pitchers with the 􀅭ive key starters on the top row and 􀅭ive relievers on the bottom row. The top half of each subgraph shows the number of games during which the pitcher reaches a certain pitch count. The bottom half indicates the mean strike-to-ball ratio for that pitcher at different pitch counts. 

than just 10-or-20-pitch pitchers and 􀅭ill that gap in the bullpen’s collective capability. 

## **4. Conclusion** 

By way of conclusion, we remark that our 􀅭inding regarding the magnitude of the home-􀅭ield advantage (0.429 runs/game rather than 0.133 runs/game) is signi􀅭icant, and is misrepresented in a number of works [13, 16]. It is now known that the 􀅭irst inning makes up approximately 21% of the overall difference in scoring potential between the home and visiting team, rather than 58% as was reported in [16]. A clear understanding of this principle prevents us from overestimating the importance of the 􀅭irst inning (or any other source), although it remains roughly twice as important as any other inning in terms of the home-􀅭ield advantage. 

The remainder of this section is used to succinctly list and summarize starting pitching and bullpen strategies that arise from the 􀅭indings of this paper, and propose additional ones for future study. 

### **4.1. Summary of Strategies in this Work** 

**First-Batter Starters:** Assuming the 􀅭irst inning bias really is largely a function of how long a starting pitcher sits in the dugout between warming up and pitching in a ball game, the strategy of using a relief pitcher to face only the 􀅭irst batter of the game for visiting teams allows the usual starter to enter the game directly from the bullpen, just as fresh as he would likely be when pitching at home. The 



2017 Research Papers Competition Presented by: 



13 



analysis of this paper shows a reduction in the 􀅭irst inning home 􀅭ield advantage of 0.037 runs/game, or approximately 3 less runs scored by home opponents over 81 road games in a season when deploying this strategy. Since roughly 18% of games are won by home teams by only one run, this could easily provide one or more additional road wins to a team in a season. Furthermore, since the strategy does not require any extra skills or work by a team, it is an advantage that comes for free to anyone bold enough to use it. 

**Pitch Until the Trigger Point:** As demonstrated in the 􀅭igures of the previous section, the different pitchers have characteristic triggers and “tells” regarding their state or condition. A pitching management style that reacts to the plethora of data available may be most optimal but also challenging to implement due to the various parameters and factors intrinsic in such a strategy. However, with advances in technology, including the areas of processing capability and computer vision, the potential to evaluate accurately and con􀅭idently process the multi-variable responses to all the signs, trigger points, and tells is closer to reality. Knowing exactly the conditions, both mental and physiological, of one’s player on the mound can only improve decision making in this regard. 

### **4.2. Pitching Strategies for Future Work** 

**Closers as Starters:** An extension of the 􀅭irst-batter starter tactic is to use a relief pitcher for the entire 􀅭irst inning as proposed in [5], and allow the usual starter to begin the game in the second inning. Althoughthis technique does not focus directlyonreducingthe􀅭irst-inning bias towardthe hometeam, it may provide other bene􀅭its to a ball club. Some preliminary analysis of this strategy has indicated that relief pitchers generally pitching the 8th inning would likely be at least as effective as starters in pitching only the 􀅭irst inning. This may allow teams to match up their ace reliever against the top of the opposing lineup, and reduce the overall scoring in the 􀅭irst inning of their opponents, whether at home or on the road. Furthermore, it has been shown [10] that hitters tend to do better the third time facing a pitcher in a game. Since the top of the order is likely to be comprised of an opposing team’s best hitters, this strategy prevents the best hitters from seeing the second-inning starter three times until much later in the game (and maybe not at all). While managers could adopt lineup changes to combat this idea, forcing the best opposing hitters down the lineup is always a good result as they will tend to bat less than those at the top of the lineup. 

**Three-Inning Pitchers:** The data in Section 3 seems to indicate that starting pitchers are likely to be able to deliver a greater number of quality pitches in one outing than relief pitchers. This may be, at least partially, a function of relief pitchers intentionally throwing harder for a shorter number of pitches. In other words, the task of relief pitching is different from that of starting pitching, just as running a marathon is different from running a 100-meter dash. We propose a middle ground of grooming pitchers to pitch exactly three innings in an outing. Overall pitch counts for the starters would be reduced and this may allow for them to start more often. Regrettably, no MLB team has ever adopted such a strategy to our knowledge, but it has been shown recently that relief pitchers are now pitching more innings on average, and have a lower OPS+ for opposing batters compared to starting pitchers [7]. Maybe it’s time to level the playing 􀅭ield between these two groups in the form of three-inning outings. 

**Pitch Once Through the Lineup:** Taking the idea of the three-inning pitcher one step further, and motivated by the results in [9, 10] where we see that opposing batters perform better after seeing a 



2017 Research Papers Competition Presented by: 



14 



pitcher multiple times in one outing, we propose the simple strategy of never allowing a batter on the opposing team to see any pitcher more than once per game. Thus, a pitcher would start with the leadoff batter in the 􀅭irst inning, and come out after facing the 9th batter in the lineup. In 2015, MLB teams had an average of 38 plate appearances in any one game; and therefore, this would necessitate 4--5 pitchers per side for every game. Surprisingly, this number is not all that different from the current trend of roughly 4 pitchers per game [7]. 

## **References** 

- [1] Retrosheet. URL `http://www.retrosheet.org/` . 

- [2] Rob Arthur. In baseball, October is reliever season. _FiveThirtyEight and ESPN_ , Oct. 2016. URL `http://fivethirtyeight.com/features/in-baseball-october-is-reliever-season/` . 

- [3] Phil Birnbaum. A guide to sabermetric research. _Society for American Baseball Research (SABR)_ . URL `http://sabr.org/sabermetrics` . 

- [4] Phil Birnbaum. Examining home-􀅭ield advantage. In _SABR Analytics Conference (SABR 41)_ , Long Beach, CA, Jul. 2011. URL `http://www.philbirnbaum.com/` . 

- [5] Bryan Grosnick. Replacing setup men with “openers”. _Beyond the Box Score_ , Nov. 2013. URL `http://www.beyondtheboxscore.com/2013/11/26/5144934/openers-bullpen-usageclosers-setup-men-weird-baseball-all-the-luke-hochevar` . 

- [6] Bill James. _The Bill James Baseball Abstract_ . Self-published by Bill James, Mar. 1982. 

- [7] Jonah Keri and Neil Paine. How bullpens took over modern baseball. _FiveThirtyEight and ESPN_ , Aug. 2014. URL `http://fivethirtyeight.com/features/how-bullpens-took-overmodern-baseball/` . 

- [8] Michael Lewis. _Moneyball: The Art of Winning an Unfair Game_ . WW Norton & Company, 2004. 

- [9] Mitchel Lichtman. Baseball ProGUESTus: Why having a quick hook helps. _Baseball Prospectus_ , Nov. 2011. URL `http://www.baseballprospectus.com/article.php?articleid=15549` . 

- [10] Mitchel Lichtman. Baseball ProGUESTus: Everything you always wanted to know about the Times Through the Order Penalty. _Baseball Prospectus_ , Nov. 2013. URL `http://www.baseballprospectus.com/article.php?articleid=22156` . 

- [11] Sam Miller. Are statheads responsible for the most exciting postseason in years? _ESPN_ , Oct. 2016. URL `http://www.espn.com/mlb/story/_/id/17870355/are-statheads-responsiblemost-exciting-postseason-years` . 

- [12] MLB.com. Guidelines for youth and adolescent pitchers. URL `http://m.mlb.com/pitchsmart/ pitching-guidelines` . 

- [13] Tobias Moskowitz and L. Jon Wertheim. _Scorecasting: The hidden in􀅲luences behind how sports are played and games are won_ . Three Rivers Press, 2012. 





2017 Research Papers Competition Presented by: 

15 



- [14] Of􀅭icial Playing Rules Committee. _Of􀅲icial Baseball Rules: 2016 Edition_ . Of􀅭ice of the Commissioner of Baseball, 2016. URL `http://mlb.mlb.com/mlb/downloads/y2016/official_baseball_ rules.pdf` . 

- [15] John L. Salmon and Willie K. Harrison. Tracking pitcher performance with instantaneous component ERA and moving averages. In _MIT Sloan Sports Analytics Conference_ , Boston, MA, Mar. 2016. URL `http://www.sloansportsconference.com/` 

   - `wp-content/uploads/2016/02/1564-Tracking-Pitcher-Performance` 

   - `-with-Instantaneous-Component-ERA-and-Moving-Averages.pdf` . 

- [16] David W. Smith. Why do home teams score so much in the 􀅭irst inning? _Retrosheet Research Papers (SABR44)_ , Aug. 2014. URL `http://retrosheet.org/Research/SmithD/WhyDoHome TeamsScoreSoMuchInTheFirstInning.pdf` . 

- [17] David W. Smith. Home team scoring advantage in the 􀅭irst inning largely due to time. _Retrosheet Research Papers (SABR45)_ , June 2015. URL `http://retrosheet.org/Research/SmithD/ HomeTeamScoringAdvantageRelatedToTime.pdf` . 

- [18] Jayson Stark. The book on hooks. _ESPN_ , May 2004. URL `http://www.espn.com/mlb/columns/story?id=1798057columnist=stark_jayson` . 

- [19] Jeff Zimmerman. First inning home 􀅭ield advantage. _FanGraphs_ , Sep. 2013. URL `http://www.fangraphs.com/blogs/first-inning-home-field-advantage/` . 





2017 Research Papers Competition Presented by: 

16 


