<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2015/2015 - Who Is Responsible For A Called Strike - Unknown Authors.pdf -->

# **Who Is Responsible For A Called Strike?** 

Joe Rosales, Scott Spratt Baseball Info Solutions Coplay, PA 18037 Emails: joe@baseballinfosolutions.com, <u>scott@baseballinfosolutions.com</u> 

## **Abstract** 

The purpose of this paper is to introduce a new methodology for quantifying what is commonly referred to as “pitch framing,” in which we attempt to divide the credit for whether a pitch is called a ball or strike among the catcher, the pitcher, the batter, and the umpire involved. We call our system Strike Zone Plus/Minus, and it is unique from other pitch framing methodologies in two ways. First, we treat pitchers, batters, and umpires as independent actors in the system rather than treating them as variables to adjust the catcher's performance by. Second, we use Baseball Info Solutions data on where the catcher sets his target for the pitch, allowing us to incorporate the pitcher's command (how close he comes to hitting the target) into our system. Our results show that we are successfully measuring the abilities of each participant independently of each other and that we are reliably measuring a consistent pitch framing skill. Strike Zone Plus/Minus produces results that are more comprehensive and in some cases radically different than publicly available framing methodologies, which will have many implications. The most direct one will be the valuation of catchers in the free agent market. 

## **Introduction** 

We know that the strike zone is not called with 100 percent consistency. Two pitches may be thrown in identical locations, but one may be called a ball and the other called a strike. There is evidence to suggest that some players may have more of a knack than others for getting these borderline pitches called strikes, and we have developed a system for measuring the contribution each player is able to make in getting more or fewer strikes called than average which we call Strike Zone Plus/Minus. 

Most public research on this topic has centered on catcher framing abilities. In many of the methodologies that have been developed, if any consideration is given to the other parties involved—namely the pitcher, the batter, and the umpire—it is usually incorporated as an adjustment to the catcher's numbers. Examples of the most prominent such methodologies include Matthew Carruth's Catcher Report<sup>1</sup> (which considers only the catcher), Mike Fast's measurement of catcher performance at getting extra strikes called<sup>2</sup> , and the Regressed Probabilistic Model devised by Harry Pavlidis and Dan Brooks<sup>3</sup> . However, the catcher, the pitcher, the batter, and the umpire all have their own independent influence on whether the pitch is called a strike or a ball, such as the catcher with his receiving skills, the pitcher with his ability to locate the pitch, the batter with his body language or other mannerisms, and the umpire based on his personal standards. Therefore, the approach that we have taken is to treat all four as meaningful participants and to divide the credit for the outcome of each pitch among the four of them based on their individual tendencies. 

While there are myriad ways that Strike Zone Plus/Minus can illuminate our understanding of the game of baseball, the most direct way relates to how it can inform how the free agent market values catchers. Catchers are involved in many more pitches over the course of a season than pitchers or hitters are, and obviously teams have no choice over who umpires their games. The publicly available framing methodologies value elite framing catchers as being worth upwards of 40 runs in a season, which would correspond to as much as $30 million in today's free agent market. Strike Zone Plus/Minus values the skill more conservatively, but even at more moderate levels, it suggests elite framing catchers should be paid on par with the compensation of many of the elite non-catchers in the game, which is not currently the case. 

## **Methodology** 

### **Determining Significant Variable** 

There are many factors that contribute to a pitch being called a ball or a strike. In addition to the identities of the pitcher, the catcher, the batter, and the umpire, there are many variables related to the context that the pitch was thrown in. In order to determine the individual contributions of each of the active participants on a given pitch, first we have to start by isolating their contribution as a group from the context of the pitch. There are seven contextual variables that we thought would most affect the outcome of a pitch, so we investigated each of the seven to 

determine their significance. Those seven variables, listed in no particular order, are: Pitch Location, Batter Handedness, Pitcher Handedness, Ball/Strike Count, Pitch Type, Command (how close the pitcher was to hitting the catcher's target), Home/Road (whether the pitcher/catcher play for the home team or road team). 

While other methodologies have attempted to account for some of these variables to varying degrees, our approach is unique in that we can incorporate our command data into the methodology. In 2010 we began charting the location of where the catcher sets his target before each pitch. This allows us to measure how close the pitcher came to hitting his target and to determine how much that might affect the umpire's call. 

In calculating the Strike Zone Plus/Minus for a given pitch, the first thing we need to know is the expected strike percentage for that pitch. How we determine that expected strike percentage depends on which of the above variables we choose to consider. Ideally, we would account for them all. However, the more factors that we include in defining the expected strike percentage, the more we increase the likelihood of running into sample size issues – i.e., the more discretely defined our buckets for classifying each pitch become, the fewer pitches we will have in each bucket. For this study, we used all pitch data from 2010-13. 

Since it is the underlying basis for whether a pitch is called a ball or a strike in the first place, we began by bucketing pitches just by their Pitch Location according to a grid that is approximately one inch by one inch. Then we went through the other variables one by one to see how much variation in Plus/Minus there was for each. 

The two variables that showed the most significant variation were Count and Command. For example, pitches were 5.6 percent more likely than average to be called strikes in a 3-0 count, while pitches were 3.2 percent less likely than average to be called strikes in 0-1 counts. See Table 1. 

**Table 1: Plus/Minus Strike Percent Relative to Average based on the Ball-Strike Count** 

|**Count**|||**Ba**|**lls**||
|---|---|---|---|---|---|
|||**0**|**1**|**2**|**3**|
||**0**|1.3%|2.5%|4.2%|5.6%|
|**Strikes**|**1**|-3.2%|-1.5%|0.1%|1.6%|
||**2**|-2.9%|-2.7%|-2.1%|-1.8%|



Because of these significant differences between counts, we decided to include Count as a major variable and to separate each count before calculating the expected strike percentage for every pitch. 

For Command, we found that the difference in horizontal distance between where the catcher set up and where the pitch location ended up mattered more than the vertical difference in terms of the expected strike percentage. Therefore, we grouped pitches by their horizontal distance from the catcher's target. Pitches closest to the glove were called strikes 2.8 percent more often than average, while pitches farthest from the glove were called strikes 8.6 percent less often than average. See Table 2. 

**Table 2: Plus/Minus Strike Percent Relative to Average based on the Pitcher’s Command** 

|**Command (Horizontal Distance from Target)**|**Plus/Minus Strike Pct**|
|---|---|
|Group 1 (less than 3.8 inches)|2.8%|
|Group 2 (3.8 – 7.6 inches)|-0.3%|
|Group 3 (7.6 – 10.4 inches)|-2.9%|
|Group 4 (greater than 10.4 inches)|-8.6%|



Given these significant differences based on command _after_ accounting for pitch location, we added Command as a second significant variable. 

The other variables—Batter Handedness, Pitcher Handedness, Pitch Type, and Home/Road—did not show as much variation. See Tables 3 through 6. 

2 

**Table 4: Pitcher Handedness** 

**Table 3: Batter Handedness** 

|**Bat Side**|**Plus/Minus Strike Pct**|
|---|---|
|LHB|0.1%|
|RHB|-0.1%|



|**Pitch Side**|**Plus/Minus Strike Pct**|
|---|---|
|RHP|0.2%|
|LHP|-0.4%|



**Table 5: Pitch Type** 

**Table 6: Home/Road** 

|**Pitch Type**|**Plus/Minus Strike Pct**|**Home/Road**|**Plus/Minus Strike Pct**|
|---|---|---|---|
|Fastball|0.3%|Home|0.2%|
|Offspeed|-0.4%|Road|-0.2%|
|Breaking Ball|-0.5%|||



However, despite the fact that Batter Handedness and Pitcher Handedness did not show a large variation, we suspected that they might show a larger effect if we focus on specific pitch locations. In other words, if we look at the plate from the pitcher's perspective, we thought that pitches on the left half of the plate might show a large variation in their Plus/Minus depending on the batter's handedness, with a similar but opposite skew on the right half of the plate. Both might show a large variation individually, but taken together they might cancel each other out, thereby masking the significance of Batter Handedness as a variable. And there could be a similar effect for Pitcher Handedness. 

To test this, we calculated the Plus/Minus for pitches on each side of the plate separately. In each case, there was a more significant variation for Batter Handedness and for Pitcher Handedness than those variables showed with all pitches taken together. The results are shown in the Tables 7 and 8 below. 

**Table 7: Batter Handedness (Half the Plate)** 

|**Plate Side (Pitcher's POV)**|**Bat Side**|**Plus/Minus Strike Pct**|
|---|---|---|
|Left Half|RHB|1.7%|
||LHB|-4.0%|
|Right Half|RHB|-2.8%|
||LHB|2.0%|



**Table 8: Pitcher Handedness (Half the Plate)** 

|**Plate Side (Pitcher's POV)**|**Pitch Side **|**Plus/Minus Strike Pct**|
|---|---|---|
|Left Half|RHP|-0.4%|
||LHP|1.1%|
|Right Half|RHP|0.7%|
||LHP|-1.7%|



While the effect was strong for Batter Handedness, the effect was less so for Pitcher Handedness. Therefore, we knew that the next significant variable that we would add to the bucketing criteria would be Batter Handedness. 

After bucketing for Pitch Location, Count, Command, and Batter Handedness, we reached the point where the size of our buckets is about as small as we want them to get given our set of four years worth of pitch data. The remaining variables—Pitcher Handedness, Pitch Type, and Home/Road—still suggest that they might have some effect, but the effect of each has either been reduced or remained small after the addition of these initial variables. See Tables 9 through 11 below. 

3 

**Table 9: Pitcher Handedness (Half the Plate) – After Adjusting for Pitch Location, Count, Command, and Batter Handedness** 

|**Plate Side (Pitcher's POV)**|**Pitch Side **|**Plus/Minus Strike Pct**|
|---|---|---|
|Left Half|RHP|-0.3%|
||LHP|0.9%|
|Right Half|RHP|0.4%|
||LHP|-1.0%|



**Table 10: Pitch Type – After Adjusting for Pitch Location, Count, Command, and Batter Handedness** 

|**Pitch Type**|**Plus/Minus Strike Pct**|
|---|---|
|Breaking Ball|0.2%|
|Offspeed|0.0%|
|Fastball|-0.1%|



**Table 11: Home/Road – After Adjusting for Pitch Location, Count, Command, and Batter Handedness** 

|**Home/Road**|**Plus/Minus Strike Pct**|
|---|---|
|Home|0.2%|
|Road|-0.2%|



Therefore, we are confident that we are adjusting for all of the most significant variables. 

### **The Basis for Determining the Strike Zone Plus/Minus of Each Pitch** 

After we categorize each pitch by its location, the count the pitch was thrown in, the proximity of the pitch to the catcher's target, and the batter's handedness, we can determine the percent likelihood that each pitch is to be called a strike. The full array of these strike percentages represents our Strike Zone Plus/Minus Basis, i.e., the basis by which we assign credit if the pitch is called a strike or debit if the pitch is called a ball. 

Because the baseball environment is constantly in flux, we want to be sure that our basis remains current. As we pointed out in the previous section, we used four years of data to determine how to bucket our pitches, adding levels of complexity to the bucketing up to the point that we were still comfortable that the number of pitches that fit into each bucket was meaningful. In order to balance the need for both recency and for legitimate sample sizes, we will be using a rolling four-year basis moving forward. That means that the strike percentages used to determine Strike Zone Plus/Minus will always be reflective of pitch results going back exactly four years from the current date. 

### **Calculating Strike Zone Plus/Minus** 

The basic idea behind calculating Strike Zone Plus/Minus is pretty straight forward. If a pitch is called a strike, there is positive credit to be awarded (plus) to the players involved. If a pitch is called a ball, there is negative credit to be assigned (minus). The amount of positive or negative credit given depends on how likely that pitch was to be called a strike in the first place, which we know from the Basis that we previously calculated. 

For example, if a pitch is thrown that is one inch off the outside edge of the plate and 10 inches off the ground, to a left handed batter, in a 2-1 count, and misses the catcher's target by 6 inches, we estimate there to be a 43 percent chance that the pitch will be called a strike. Therefore, if the umpire calls the pitch a strike, then there are plus-0.57 Strike Zone Plus/Minus points (or “extra strikes”) to be allotted to the participants on the pitch. However, if the umpire is not so moved and he calls the pitch a ball, then there are minus-0.43 points to be divvied up among the four parties. 

The notion of determining a Plus/Minus for a pitch is fairly common throughout the majority of methodologies that strive to assign credit for getting more or fewer strikes called than average. However, most of these methodologies 

4 

are constrained by the idea of measuring “catcher framing”. They operate under the preconceived assumption that getting extra strikes called is primarily the responsibility of the catcher. The entire Plus/Minus credit for a pitch is assigned to the catcher, and then the the pitcher, the umpire, and the batter get treated as context that needs to be adjusted for. In the batter's case, most don't even give him a thought. And for methodologies that attempt to quantify the pitcher's ability to get extra strikes called, they have to run a separate model where the entire Plus/Minus credit for a pitch is assigned to the pitcher, with adjustments then made for the catcher and others. 

With our methodology, we treat all four of the catcher, the pitcher, the batter, and the umpire as active participants on each pitch. We have divided the Plus/Minus credit for each pitch among all four according to their individual abilities, and we run a single model to be able to evaluate all of the participants individually. 

The approach that we take is an iterative one. To begin, without any initial knowledge about the abilities of any individual to get extra strikes called, we simply start by going through each pitch and dividing the Plus/Minus credit evenly between all four parties. So let's go back to the example pitch that was mentioned earlier, and let's say the pitch was called a strike. Therefore, the overall Plus/Minus for that pitch is plus-0.57. And let's say that James Shields was pitching to Salvador Perez with Oswaldo Arcia batting and Dana DeMuth behind the plate calling balls and strikes. All four would be given plus-0.1425 credit for the pitch. 

Once we have done this for every pitch, we add up all the credits and debits that a player has received to get an initial indication of his Strike Zone Plus/Minus. If a player's Plus/Minus is positive, it suggests that he has the ability to get more strikes called than average. If his Plus/Minus is negative, it suggests that he gets fewer strikes (more balls) called than average. However, we do not really know either of these things for sure at this point. We know better than to think that each party is equally responsible for the outcome of a given pitch. What if, on a particular pitch, there is a pitcher, a catcher, and a batter all prone to getting extra strikes called, but an umpire who is working against them? We don't want that umpire getting the same credit as the other three. So we begin to make iterative adjustments. 

For our second iteration, we want to separate the individual tendencies of the players on each pitch from the portion of the Plus/Minus that is attributable to a neutral environment. We start by dividing each player’s total Strike Zone Plus/Minus from the first iteration by the number of pitches that they were involved in to get their Plus/Minus Per Pitch. This number represents the contribution that each player brings to an individual pitch. 

Returning to our example, let's say that after the first iteration Shields had achieved plus-0.018 Plus/Minus Per Pitch, meaning that there were 1.8 percent more strikes than average called while he was pitching. And let's say Perez was worth plus-0.002, Arcia was worth plus-0.015, and DeMuth was worth minus-0.005—these numbers being entirely hypothetical. Combined, they get 0.030 more strikes than expected per pitch. When we subtract this from the plus0.57 Plus/Minus of the pitch, we are left with plus-0.54. 

This plus-0.54 represents the portion of the Plus/Minus of the pitch attributable to a neutral environment. All four players can lay equal claim to it. Therefore, we can distribute this evenly among the four players, which means assigning plus-0.135 to each. 

We then add each player's share of the neutral portion (the plus-0.135) to his individual contribution (his Plus/Minus Per Pitch). Therefore, instead of the plus-0.1425 that each received after the first iteration, now Shields gets 0.135 + 0.018 = 0.153 credit for this pitch. Likewise, Perez gets 0.137, Arcia gets 0.150, and DeMuth gets 0.130. By doing the same thing for every other pitch and adding up the results, we now have a new Strike Zone Plus/Minus total for each player. 

Having done this second iteration, we are closer to having an accurate reflection of each player's ability to get extra strikes called, but we are still not that far removed from having given everyone equal credit to begin with. There is actually a pretty large change in Strike Zone Plus/Minus for most players from the first iteration to the second. Therefore, to continue refining how accurately our numbers reflect each player's skill, we repeat the process that we did for the second iteration again and again. With each iteration, the change in Strike Zone Plus/Minus for each player gets smaller. We stop iterating once the change has become so small that we know we have converged on a true reflection of each player's abilities. Normally, this takes about 10 iterations. 

5 

The final step we take is to include an adjustment to help smooth out the small pitch samples of some players. We do this by regressing each player's Strike Zone Plus/Minus by a certain number of league average pitches. Based on our research, 250 is the optimal number of league average pitches to add to each player's actual total. 

### **Run Value** 

In order to state each player's impact in terms of the runs that he saves or costs his team (or, in the umpire's case, the runs he saves or costs all teams), we need to know what the run value of converting a ball into a strike is. Therefore, we took our pitch results from the same 2010-13 time period, calculated the run expectancy associated with each ball/strike count (the number of runs scored from that point through the end of the half inning), and then found the difference in the change in run expectancy between the next pitch being called a ball and the next pitch being called a strike. Because we did not find any evidence that any given player is putting more or less effort into getting an extra strike called depending on the count (i.e., “clutch framing”), we felt comfortable averaging all the changes in run expectancy into a single run value. The average difference in run expectancy between a ball and a strike amounts to .1189 runs, which we will apply as the final step. 

### **Independence Test** 

One of the main concerns of trying to assign credit for getting extra strikes called is that the participants involved do not all interact with each other with the same frequency. In particular, pitchers and catchers are likely to have significant overlap in their pitch samples. So if a pitcher has a positive Strike Zone Plus/Minus, is that because he himself is good at getting extra strikes, or is it because he throws the majority of his pitches to a good catcher? 

In order to determine whether our system is adequately accounting for these interaction effects, we performed a couple of variations on a “with or without you” correlation test. To do this, we looked at each pitcher with a specific catcher and with all other catchers. If our system is measuring the performance of each player independently, then the correlation of the pitcher's performance with a specific catcher to the pitcher's performance with all other catchers should be high (i.e., the pitcher's performance is consistent no matter who the catcher is). Conversely, the correlation of the performance of that catcher to the performance of all other catchers with that same pitcher should be low (i.e., each catcher is unique). 

For each pitcher, we calculated his Plus/Minus Per Pitch on the pitches he threw to a specific catcher, and then separately calculated his Plus/Minus Per Pitch on the pitches he threw to all other catchers. For example, between 2010 and 2013, Eric Stults threw 1205 pitches to Nick Hundley that were either a called ball or a called strike, and he threw 1411 such pitches to all other catchers. When paired with Hundley, he managed 0.020 extra strikes per pitch. With all other catchers, he managed 0.019 extra strikes per pitch. We did this for every pitcher/catcher pair, and then calculated the correlation between the two sets of numbers—the values with the specific catcher and the values with all other catchers. 

If we limit our sample to pitcher/catcher pairs where the pitcher had thrown at least 100 pitches to both the catcher in question and to all other catchers so as to eliminate small sample effects, the correlation comes out to 0.80. That's pretty strong. That suggests that our system is measuring very consistent performance for pitchers no matter who the catcher is. If we increase the threshold to 500 pitches thrown with and without the catcher, the correlation improves to 0.91. And as we continue to increase the threshold, the relationship continues to strengthen. Therefore, the first part of our test has us confident that our system is truly measuring the performance of each player independently. 

For the second part of our test, we looked at the same pitcher/catcher pairings, but instead calculated the Plus/Minus Per Pitch that the catcher in question achieved with that pitcher, as well as the Plus/Minus Per Pitch that all those other catchers accumulated with that pitcher. Turning back to our Stults/Hundley example, Hundley had a minus0.007 Plus/Minus Per Pitch when he caught Stults, whereas all the other catchers that caught Stults had a plus-0.016 Plus/Minus Per Pitch when they were paired with him. As before, we did this for all pitcher/catcher pairs, and we calculated the correlation between the two sets of numbers. This time, when the threshold was set to 100 pitches and 500 pitches with and without the catcher, the correlation came out to minus-0.04 and minus-0.03 respectively. This suggests no evidence of a relationship between the performances of the various catchers that caught the same pitcher as measured by our system. This adds to our confidence that our system is truly measuring the performances of each player independently. 

Just to drive the point home, we did the same exercise, but instead of using our iteratively calculated Strike Zone Plus/Minus numbers, we used the numbers that one would get if the Plus/Minus credit for each pitch were simply 

6 

divided evenly between each player. With the threshold set to 100 pitches, both the correlation of the pitchers' numbers and the correlation of the catchers' numbers came out to 0.19. As we expected, the pitchers’ correlation is much stronger than this after our iterative adjustments, and the catchers’ correlation is much weaker. Therefore, we know that we have significantly improved the accuracy of our measurement by using our iterative approach. 

### **Even/Odd Year Correlation Test** 

In order to test that our Strike Zone Plus/Minus metric is measuring something meaningful, we performed an even/odd year correlation. If we are measuring a meaningful ability for a player or umpire to get extra strikes called, then we would expect his numbers to be consistently high or low from year to year. To do this, we added the Strike Zone Runs Saved from 2010 and 2012 together and compared them to the subtotal of 2011 and 2013 taken together for all players that were involved in at least 500 called pitches in both sets of years. Table 12 below shows the correlation for each of the four types of participants. 

**Table 12: Strike Zone Runs Saved Even/Odd Year Correlations** 

|**Player Type**|**Even/Odd Year Correlation**|
|---|---|
|Pitchers|0.46|
|Catchers|0.86|
|Batters|0.50|
|Umpires|0.77|



The even/odd year correlation for catchers is extremely high. The correlation for umpires is quite high as well. It is not very surprising that catchers and umpires would have the highest correlations between even and odd years considering that they are generally involved in many more pitches than pitchers and batters over the course of a season. However, despite showing less consistency between even and odd years, the correlations for pitchers and batters are still strong enough to inspire confidence. Overall, these results demonstrate that Strike Zone Plus/Minus is doing an excellent job of measuring a meaningful skill. 

## **Results** 

Applying our run value to our calculated Strike Zone Plus/Minus totals, Table 13 shows the top five and bottom five catchers, pitchers, batters, and umpires from the 2014 season. 

**Table 13: 2014 Strike Zone Runs Saved Leaders and Trailers** 

|**Catchers**<br>||**Pitcher**<br>|**s**<br>|**Batter**<br>|**s**<br>|**Umpire**<br>|**s**<br>|
|---|---|---|---|---|---|---|---|
|**Name**|**SZRS**|**Name**|**SZRS**|**Name**|**SZRS**|**Name**|**SZRS**|
|M. Zunino|16|H. Iwakuma|4|Me. Cabrera|3|R. Kulpa|12|
|H. Conger|16|F. Hernandez|3|J. Loney|2|B. Miller|12|
|**Top**<br>M. Montero|15|M. Buehrle|2|B. Revere|2|D. Eddings|12|
|J. Lucroy|14|K. Lohse|2|B. Gardner|2|A. Hernandez|11|
|B. Posey|11|J. Weaver|2|X. Bogaerts|2|B. O'Nora|10|
|A. Ellis|-7|T. Wood|-2|M. Joyce|-2|A. Marquez|-8|
|W. Castillo|-9|H. Santiago|-2|C. Santana|-3|G. Gibson|-8|
|**Bottom**<br>K. Suzuki|-15|L. Lynn|-2|A. Gonzalez|-3|S. Buckminster|-9|
|J. Saltalamacchia|-16|A. Harang|-2|M. Montero|-3|T. Hallion|-9|
|D. Navarro|-17|N. Eovaldi|-3|D. Pedroia|-4|P. Schrieber|-16|



An important point to note about these results is that evaluating a participant's performance as “good” or “bad” based on whether their values are positive or negative depends on which participant one is looking at. For catchers 

7 

and pitchers, the results are straight forward. Positive values mean that they are getting more strikes called than average, so that is good for them, and negative numbers are bad. For batters, positive numbers mean that more strikes than average were called while they were at the plate. Therefore, positive numbers are actually undesirable for them, while negative numbers are good. For umpires, positive numbers indicate that they called more strikes than average. That means that umpires with positive Strike Zone Runs Saved can be viewed as pitcher-friendly umpires, while umpires with negative Strike Zone Runs Saved are hitter-friendly umpires. 

These results show why quantifying pitch framing for catchers is so much more important than for anyone else. On a per pitch basis, catchers, pitchers, batters, and umpires all fall within the same range in terms of how much impact they have on getting extra strikes called. However, on aggregate, catchers are involved in so many more pitches than either pitchers or batters that their skills actually have a far more meaningful impact on the overall fortunes of a team. 

## **Conclusion** 

Expanded use of instant replay was a major talking point of the 2014 MLB season, but balls and strikes are notable exclusions to the list of reviewable plays. Despite the increased oversight that video technology has provided in ensuring that umpires call a more consistent strike zone than was once the case, the strike zone will likely remain the final stronghold of the umpire's influence over the game. As a result, the strike zone will always be a bit of a moving target, and the ability of certain players to successfully find ways to exploit that gives us a good reason to quantify that skill, leaving those who can control ball/strike calls with a significant advantage. 

While Strike Zone Plus/Minus is more conservative in its valuation of pitch framing skills than the more prominent publicly available systems—both Matthew Carruth's Catcher Report and Harry Pavlidis' and Dan Brooks' Regressed Probabilistic Model valued the top catcher in 2014 at about 24 runs saved, whereas our model valued the top catcher at 16 Strike Zone Runs Saved—even by our measurements catchers are undervalued in baseball's free agent market. Sixteen runs is worth about $11-12 million in the current market. However, the only catchers in baseball that approach or exceed that kind of annual salary are the ones who are valuable in multiple ways, such as offensively or because they throw out a high percentage of base stealers. 

We have seen some evidence that analytically inclined teams are prioritizing good framing catchers when constructing their rosters. For example, 36-year-old Jose Molina's future was very much in question after the 2011 season with the Toronto Blue Jays. However, the Tampa Bay Rays' forward thinking front office identified Molina's excellent framing abilities and over the next three years gave him more playing time than he had ever gotten before. Similarly, this past November the Houston Astros traded for Hank Conger, who has struggled offensively in his career but was tied for the most Strike Zone Runs Saved in baseball among catchers in 2014. Because pitch framing skills are so undervalued, teams like the Rays and Astros are able to exploit that market inefficiency by acquiring top pitch framers for very small cost outlays much the same way that the Oakland Athletics now so famously did with their Moneyball strategies from a decade and a half ago. 

8 

## **References** 

1. Carruth, Matthew. “StatCorner Catchers & Framing Explainer.” _StatCorner._ <http://www.statcorner.com/exp_PreliminaryCatchingFramework.php> 

2. Fast, Mike. “Spinning Yarn. Removing the Mask Encore Presentation.” _Baseball Prospectus._ 24 September, 2011. <http://www.baseballprospectus.com/article.php?articleid=15093> 

3. Pavlidis, Harry, and Dan Brooks. “Framing and Blocking Pitches: A Regressed, Probabilistic Model. A New Method for Measuring Catcher Defense.” _Baseball Prospectus._ 3 March, 2014. <http://www.baseballprospectus.com/article.php?articleid=22934> 

9 


