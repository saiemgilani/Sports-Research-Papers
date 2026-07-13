<!-- source: library/conferences/New England Symposium on Statistics in Sports/2009/2009 - Using New Iterative Methods and Fine Grain Data to Rank College Football Teams - Unknown Authors.pdf -->

# Using New Iterative Methods and Fine Grain Data to Rank College Football Teams Maggie Wigness Michael Rowell & Chadd Williams Pacific University 

# History of BCS 

## • Bowl Championship Series 

### – Ranking since 1998 

– Undergone reconstruction 

## • Computer Rankings – No longer use scores 

- Common Data 

   - Location, Date, Strength of Schedule, Outcome of a Game 

# Importance of BCS Rankings 

- Determines who plays in the National Championship Bowl 

- Breaks conference ties 

- Influences selections of many bowl games 

BCS Bowl Game Accuracy Using the BCS computer rankings, we determined how often the rankings were able to predict the outcome of a bowl game. - Assuming the higher ranked team should win the game 

||1998|1999|2000|2001|2002|2003|2004|2005|2006|2007|2008|Totals|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Correct|5|7|6|7|6|11|8|7|12|8|5|82|
|Incorrect|5|3|4|3|5|5|6|8|5|9|10|63|
|Accuracy|50.0|70.0|60.0|70.0|54.5|68.8|57.1|46.7|70.6|47.1|33.3|56.6|



• 56.6% is not statistically significant 

• -value = 0.0673 _p_ 

# Preliminary Results 

||**1998**|**1999**|**2000**|**2001**|**2002**|**2003**|**2004**|**2005**|**2006**|**2007**|**2008**|**Totals**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Correct**|**6**|**6**|**6**|**6**|**7**|**12**|**9**|**7**|**11**|**10**|**7**|**87**|
|**Incorrect**|**4**|**4**|**4**|**4**|**4**|**4**|**5**|**8**|**6**|**7**|**8**|**58**|
|**Accuracy**|**60.0**|**60.0**|**60.0**|**60.0**|**63.6**|**75.0**|**64.3**|**46.7**|**64.7**|**58.8**|**46.7**|**60.0**|



- Difference of Scores 

- -value < .01 

- _p_ 

- Indication that scores can help rank teams – What about even finer grain data? 

# Play-by-Play Method 

## • Finer grain data comes from play-byplay statistics 

- Stats should reflect team success 

– Help predict the outcome of a game – Indicate the magnitude of a win or loss 

# Getting the Statistics 

- Designed a web-crawler to download the web pages that contained play-byplay stats 

- Wrote a parser that extracted the data we needed so it could be imported into a database 



<!-- Start of picture text -->
http://web1.ncaa.org/d1mfb/driveSummary.jsp?expand=A&acadyr=2006&h=472&v=655&date=31-AUG-06&game=null<br><!-- End of picture text -->

http://web1.ncaa.org/d1mfb/driveSummary.jsp?expand=A&acadyr=2006&h=472&v=655&date=31-AUG-06&game=null 

# Play-by-Play Statistics 

- Only retrieved full sets of play-by-play data for the past 3 seasons 

- Ran over 40 different statistics on data from the 2007-2008 season 

- Results seen indicate a percentage of accuracy based on the 32 bowl games played that year 

|3rd Down Conversions|65.6|3rd Down Conversions Given Up|65.6|
|---|---|---|---|
|Yards Per Play*|59.4|Yards Given Up Per Play|59.4|
|Yards Per Play Not Including Punts*|62.5|Yards Given Up Per Play Not Including<br>Punts*|59.4|
|1st Down Per Set of Downs*|68.8|1st Down Per Set of Downs - 1st Half*|65.6|
|% of Total Yards Gained on 1st<br>Down|50.0|% of Total Yards Gained on 2nd Down*|40.6|
|% of Total Yards Gained on 3rd<br>Down*|62.5|% Yards Gained Toward 1st Down|59.4|
|% Yards Gained Toward 1st Down -<br>Rushing for Short Yards|53.1|% Yards Gained Toward 1st Down -<br>Rushing in 1st Half*|62.5|
|% Yards Gained Toward 1st Down -<br>Rushing in the 2nd Half*|40.6|% Yards Given Up Toward 1st Down -<br>Rushing in the 1st Half*|62.5|
|% Yards Gained Toward 1st Down -<br>Variable Point Gap|62.5|Defensive Big Plays*|53.1|
|Maroon Zone Scores Per Attempt*|50.0|Maroon Zone 1st Downs Per Attempt*|46.9|
|Red Zone Scores Per Attempt*|53.1|Defensive Big Plays on 3rd Down*|53.1|



* Game Within 14 Points 

|3rd Down Conversions|65.6|3rd Down Conversions Given Up|65.6|
|---|---|---|---|
|Yards Per Play*|59.4|Yards Given Up Per Play|59.4|
|Yards Per Play Not Including Punts*|62.5|Yards Given Up Per Play Not Including<br>Punts*|59.4|
|1st Down Per Set of Downs*|68.8|1st Down Per Set of Downs - 1st Half*|65.6|
|% of Total Yards Gained on 1st<br>Down|50.0|% of Total Yards Gained on 2nd Down*|40.6|
|% of Total Yards Gained on 3rd<br>Down*|62.5|% Yards Gained Toward 1st Down|59.4|
|% Yards Gained Toward 1st Down -<br>Rushing for Short Yards|53.1|% Yards Gained Toward 1st Down -<br>Rushing in 1st Half*|62.5|
|% Yards Gained Toward 1st Down -<br>Rushing in the 2nd Half*|40.6|% Yards Given Up Toward 1st Down -<br>Rushing in the 1st Half*|62.5|
|% Yards Gained Toward 1st Down -<br>Variable Point Gap|62.5|Defensive Big Plays*|53.1|
|Maroon Zone Scores Per Attempt*|50.0|Maroon Zone 1st Downs Per Attempt*|46.9|
|Red Zone Scores Per Attempt*|53.1|Defensive Big Plays on 3rd Down*|53.1|



* Game Within 14 Points 

# BCS Comparison 

#### • Percentages indicate the accuracy when predicting games that include at least 1 team ranked by the BCS 

#### • 2007 - 2008 season 

|**Play-by-Play Statistics**|**%**|
|---|---|
|3rd Down Conversions|64.7|
|3rd Down Conversions Given Up|64.7|
|1st Down Per Set of Downs*|70.6|
|1st Down Per Set of Downs, 1st Half*|58.8|
|BCS Method|47.1|
|*Game withi|n 14 points|



# Combination of Statistics 

- We had 4 play-by-play statistics that did well in 2007-2008 

- Combined 3 statistics and each statistic is given a weight 

   - Ran all possible weight combinations on our 3 years of data 

# Combination of Statistics 

- Looked for combinations that hit a peak percentages when predicting the outcome of bowl games 

- Best combinations for 2008-2009 

||1st Down Per<br>Set of Downs*|1st Down Per Set of<br>Downs in 1st Half*|3rd Down<br>Conversions|Overall<br>Accuracy|
|---|---|---|---|---|
||30|20|50|82.4|
|Weights<br>for each<br>|20|0|80|82.4|
|Statistic (%)|10|10|80|85.3|
||0|20|80|82.4|
||0|10|90|76.5|
||0|0|100|73.5|



*Game within 14 points 

# Combination of Statistics 

- Looked for combinations that hit a peak percentages when predicting the outcome of bowl games 

- Best combinations for 2008-2009 

|1st Down Per<br>Set of Downs*|1st Down Per Set of<br>Downs in 1st Half*|3rd Down<br>Conversions|Overall<br>Accuracy|
|---|---|---|---|
|30<br>|20|50|82.4|
|20<br>Weights<br>for each<br>|0|80|82.4|
|10<br>statistic|10|80|85.3|
|0|20|80|82.4|
|0|10|90|76.5|
|0|0|100|73.5|
|Combinations<br>73.|3%<br>•Combina|*Gam<br>tions do well o|e within 14 point<br>verall, and|
|BCS<br>33.|3%<br>significantl|y better than t|he BCS Met|



*Game within 14 points 

• Combinations do well overall, and are significantly better than the BCS Method 

# Combination of Statistics 

- No combination of statistics worked consistently from year to year 

- • Look for another method to find appropriate combinations 

# Week-By-Week Learning 

- Ran combinations week-by-week, keeping track of the best weights 

- • Average those weights and use the averages to calculate the overall ranks 

# Week-by-Week Results 

#### **Overall Accuracy of Statistics Individually** 

# Week-by-Week Results 

#### **Individual Statistics Compared to Combination of Statistics** 



<!-- Start of picture text -->
 Combination of Statistics<br><!-- End of picture text -->

# Week-by-Week Results 

#### **Individual Statistics Compared to Combination of Statistics** 



<!-- Start of picture text -->
 Combination of Statistics<br><!-- End of picture text -->

# Comparison to BCS 

• Accuracy is based only on games that include at least one team ranked by the BCS computer rankings 

||**2006**|**2007**|**2008**|
|---|---|---|---|
|Combination of Week-<br>by-Week Learning|58.8|64.7|53.3|
|Peak Combination|70.6|70.6|73.3|
|BCS Method|70.6|47.1|33.3|



# Play-by-Play Conclusions 

- Evidence of accuracy when using playby-play statistics to develop rankings 

- • Combinations of statistics can be more accurate than a single play-by-play statistic 

# Future Work 

• Many other play-by-play statistics that can be combined 

- Find a more effective method of determining which weights to use for the combinations of play-by-play statistics 

- http://www.math.pacificu.edu/~rowell/football/index.html 

# Questions? 

# Statistics to Pursue 

||2006|2007|2008|
|---|---|---|---|
|1st Down Per Set of Downs*|62.5|68.8|58.8|
|1st Down Per Set of Downs, 1st Half*|50.0|65.6|67.6|
|3rd Down Conversions|43.8|65.6|70.6|
|3rd Down Conversions Given Up|40.6|65.6|70.6|
|3rd Down Conversions Given Up*|43.8|62.5|58.8|
|Percent of Total Yards Gained on 3rd<br>Down*|59.4|62.5|55.9|
|Percent Yards Gained Toward 1st Down,<br>Rushing, 1st Half*|65.6|62.5|58.8|
|Percent Yards Gained Toward 1st Down,<br>Variable Point Gap|59.4|62.5|58.8|
|Percent Yards Given Up Toward 1st Down,<br>Rushing, 1st Half*|53.1|62.5|58.8|
|Yards Per Play, No Punts*|56.3|62.5|50.0|



*Game within 14 points 

# Overview 

Generate Game Values 

Team Value 

Develop Rankings 

Generate Game Values with Strength of Schedule 

# Similar Methods 

• Started by developing some iterative methods that use statistics similar to the BCS 

- Development of Game Values 

   - Difference of scores 







# Combinations of Two 

- Began combining two statistics together 

- Each of the statistics will be given a weight 

   - Weight of Stat 1 * Game Value using Statistic 1 

   - – (100 - Weight of Stat 1) * Game Value using Statistic 2 

- Add the two parts together to get a final game value 

# Combination Outcome 



* Close Game Statistic 

# Combination Outcome 



- Combining statistics can create greater accuracy 

* Close Game Statistic 


