<!-- source: library/conferences/New England Symposium on Statistics in Sports/2019/2019 - How Do Typical Runners' Performances Vary with Age and Gender - Unknown Authors.pdf -->

## **_HOW DO TYPICAL RUNNERS’ PERFORMANCES VARY WITH AGE AND GENDER?_** 

**Richard L Smith and Spencer Siegel (University of North Carolina); Dorit Hammerling (Colorado School of Mines) New England Symposium on Statistics in Sports September 28, 2019** 







<!-- Start of picture text -->
1<br><!-- End of picture text -->

## **_Acknowledgements_** 

- The staff of the Boston Athletic Association – Jack Fleming (COO), Tom Grilk (CEO), Michael Pieroni, Chris Menard 

- Scott Powers and Jessi Cisewski-Kehe were collaborators in the original project (see paper in _Chance_ , 2014) 

- The work I’m presenting here uses data originally collected for a different study of Boston Marathon performances (Hammerling et al., _PLoS ONE_ , 2014) 

- • Additional work by Spencer (senior thesis, in progress) 

- • Laura Albrecht, Ross Ring-Jarvi  and Dorit Hammerling have a poster on a related topic. They are focusing on a different aspect of the same set of questions. 

2 



3 

###### **2020 Boston Marathon qualifying** 

**Qualifying standard and actual qualification time by age group and gender** 

|**Age group**|men's standard|men's qualification|women's standard|women's qualification|
|---|---|---|---|---|
|**18-34**|3:00:00|2:58:21|3:30:00|3:28:21|
|**35-39**|3:05:00|3:03:21|3:35:00|3:33:21|
|**40-44**|3:10:00|3:08:21|3:40:00|3:38:21|
|**45-49**|3:20:00|3:18:21|3:50:00|3:48:21|
|**50-54**|3:25:00|3:23:21|3:55:00|3:53:21|
|**55-59**|3:35:00|3:33:21|4:05:00|4:03:21|
|**60-64**|3:50:00|3:48:21|4:20:00|4:18:21|
|**65-69**|4:05:00|4:03:21|4:35:00|4:33:21|
|**70-74**|4:20:00|4:18:21|4:50:00|4:48:21|
|**75-79**|4:35:00|4:33:21|5:05:00|5:03:21|
|**80 and older**|4:50:00|4:48:21|5:20:00|5:18:21|



Source: BAA (reprinted by the Boston Globe) 

4 

|**YEAR**|**FIELD SIZE**|**"CUT-OFF TIME"***|**QUALIFIERS NOT ACCEPTED**|
|---|---|---|---|
|**2012**|27,000|1:14|3,228|
|**2014**|36,000|1:38|2,976|
|**2015**|30,000|1:02|1,947|
|**2016**|30,000|2:28|4,562|
|**2017**|30,000|2:09|2,957|
|**2018**|30,000|3:23|5,062|
|**2019**|30,000|4:52|7,248|
|**2020**|31,500|1:39|3,161|



#### Source: BAA 

5 

## **_BACKGROUND_** 

- The Boston Marathon is the only major marathon to require qualifying standards of the majority of participants 

- Qualifying standards were first introduced in the 1970s and have been revised several times since 

- I first got involved in 2010, after entries for the 2011 race closed out in one day. 

- With Scott and Jessi, I wrote a report that provided some background for the 2012 revision of the standards 

- Since 2012, the race has continued to grow and this year the standards were revised again 

6 



7 

## **_CHANGES SINCE 2012_** 

- In 2012, the standards were uniformly tightened by five minutes (e.g. 3 hours, 5 minutes for men 18-34) 

- Beginning in 2020, the standards have been further tightened by five minutes (e.g. 3 hours, 0 minutes for men 18-34) 

- On both occasions, I have made recommendations about how these changes are likely to affect the size of the field 

- • However, the basis of the standards themselves has not been changed (e.g. 30-minute gap between qualifying standards for men and women in the same age group) 

- • The current work is motivated by broader questions of equity across different age and gender categories 

8 

### **_IDEA MOTIVATING THE PRESENT TALK_** 

- All runners slow down as they get older, but there is a lot of individual variability 

- Try to use statistical methods to characterize the agegraded performance of a “typical” runner 

- The standard method used for age-graded performances is nominally based on world records in different age groups, but this may not reflect typical runners’ performances 

- The approach I am presenting here does not directly address the gender-equity issue (see poster by Albrecht et al.) though the two questions are closely related 

9 

### **_Longitudinal Approach to the Performance v. Age Problem_** 

- About 500 runners have run the Boston marathon at least 10 years in succession (BAA) 

10 

### **_Longitudinal Approach to the Performance v. Age Problem_** 

- About 500 runners have run the Boston marathon at least 10 years in succession (BAA) 

- No easy way to reconstruct the list 

11 

### **_Longitudinal Approach to the Performance v. Age Problem_** 

- About 500 runners have run the Boston marathon at least 10 years in succession (BAA) 

- No easy way to reconstruct the list 

- I used the datasets I had available to find 1,272 runners who had run each of 2010, 2011, 2013 

12 

### **_Longitudinal Approach to the Performance v. Age Problem_** 

- About 500 runners have run the Boston marathon at least 10 years in succession (BAA) 

- • No easy way to reconstruct the list 

- I used the datasets I had available to find 1,272 runners who had run each of 2010, 2011, 2013 

- • I then used the BAA archive to find all of those runners who had run at least 6 times (men) or 5 times (women) during 2001-2013 

13 

### **_Longitudinal Approach to the Performance v. Age Problem_** 

- About 500 runners have run the Boston marathon at least 10 years in succession (BAA) 

- • No easy way to reconstruct the list 

- I used the datasets I had available to find 1,272 runners who had run each of 2010, 2011, 2013 

- • I then used the BAA archive to find all of those runners who had run at least 6 times (men) or 5 times (women) during 2001-2013 

- • Runners who did not finish in 2013 were estimated using Hammerling et al. (2014) 

14 

### **_Longitudinal Approach to the Performance v. Age Problem_** 

- About 500 runners have run the Boston marathon at least 10 years in succession (BAA) 

- • No easy way to reconstruct the list 

- I used the datasets I had available to find 1,272 runners who had run each of 2010, 2011, 2013 

- • I then used the BAA archive to find all of those runners who had run at least 6 times (men) or 5 times (women) during 2001-2013 

- Runners who did not finish in 2013 were estimated using Hammerling et al. (2014) 

- Result: 547 men and 249 women identified (806 runners; 7,219 individual race results) 

15 

## **_Idea of the Approach_** 

- Each individual runner defines their own age v. race time plot 

- Color code to distinguish men (red) from women (blue) 

- How best to combine information across runners? 

16 



17 



18 



19 



20 



21 



22 



23 



24 



25 



26 



27 



28 



29 



30 



31 



32 



33 



34 



35 



36 



37 

## **_The Idea_** 

- Each individual runner record is a part-trace of the performance v. age curve for that runner 

- Allow for a random “runner effect” 

- Also allow for a random “calendar year” effect (2004 and 2012 were very hot) 

- Separate men’s and women’s performance 

- A refinement (later): also distinguish runners of different ability levels 

38 



39 

# **_Results_** 

- Men’s curve 

(red, with confidence limit) 

- Women’s 

curve (blue, with confidence limits) 

- Crossover 

above age 70 almost certainly an artifact 



- Other 

anomalies need to be explained 

40 

### **_Recent Results (Spencer and Dorit)_** 



Results from the Chicago Marathon (all runners, 2010-2018), analyzed by the same method 

41 

### **_Recent Results (Spencer and Dorit)_** 



Restricted to runners who have run at least one Boston qualifier time 

42 

### **_Recent Results (Spencer and Dorit)_** 



<!-- Start of picture text -->
Restricted to runners who have run at least one<br><!-- End of picture text -->

Restricted to runners who have run at least one Quartiles for male runners 

43 

### **_Recent Results (Spencer and Dorit)_** 



<!-- Start of picture text -->
Restricted to runners who have run at least one<br><!-- End of picture text -->

Restricted to runners who have run at least one Quartiles for female runners 

44 





45 





46 

## **_Also look at the year effect_** 

47 

##### **_We can also consider the implications of these results for Boston Marathon qualifying times (Warning: These results are quite sensitive to which curve is used and how it is processed)_** 



48 

## **_Conclusions_** 

- The problem is difficult 

49 

## **_Conclusions_** 

- The problem is difficult 

- Current Boston Marathon standards have evolved over the years, but no real “science” behind them 

50 

## **_Conclusions_** 

- The problem is difficult 

- Current Boston Marathon standards have evolved over the years, but no real “science” behind them 

- Age-graded standards are popular in the running community, but they have problems 

51 

## **_Conclusions_** 

- The problem is difficult 

- Current Boston Marathon standards have evolved over the years, but no real “science” behind them 

- Age-graded standards are popular in the running community, but they have problems 

- The longitudinal method proposed here is the only method based on how individual runners’ performances change with age 

52 

## **_Conclusions_** 

- The problem is difficult 

- Current Boston Marathon standards have evolved over the years, but no real “science” behind them 

- Age-graded standards are popular in the running community, but they have problems 

- The longitudinal method proposed here is the only method based on how individual runners’ performances change with age 

- Intention for future work: we plan to look at other marathons and alternative statistical methods 

53 

## **_Conclusions_** 

- The problem is difficult 

- Current Boston Marathon standards have evolved over the years, but no real “science” behind them 

- Age-graded standards are popular in the running community, but they have problems 

- The longitudinal method proposed here is the only method based on how individual runners’ performances change with age 

- Intention for future work: we plan to look at other marathons and alternative statistical methods 

- Thank you for your attention! 

54 


