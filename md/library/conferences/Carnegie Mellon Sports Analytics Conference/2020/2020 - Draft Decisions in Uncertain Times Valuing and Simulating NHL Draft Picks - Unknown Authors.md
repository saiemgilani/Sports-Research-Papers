<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2020/2020 - Draft Decisions in Uncertain Times Valuing and Simulating NHL Draft Picks - Unknown Authors.pdf -->

CMSAC 2020 

## **Draft Decisions in Uncertain Times: Valuing and Simulating NHL Draft Picks** 

Meg Ellingwood, Jill Reiner 

Advised by Dr. Sam Ventura, Nick Citrone, Ron Yurko 



<!-- Start of picture text -->
*Zoom<br><!-- End of picture text -->



1 



<!-- Start of picture text -->
2<br><!-- End of picture text -->



### **“Conditional 2020 1st Round Pick”** 

● Condition: **_If Pittsburgh misses the 2019-20 playoffs, they have the option to send their 2021 1st round pick instead_** 



3 



### **What is the Draft Lottery?** 

- Draft lottery format in a normal year 

   - **Worst 15** teams that did not qualify for the playoffs are entered into a weighted lottery to determine the draft order 

- This year’s lottery is different! 

   - Pittsburgh has a **⅛ chance** of picking **1st overall** and a **⅞ chance** of picking **15th overall** 

4 



### **Question/Goals** 

- **_What should the Penguins do with their 1st round pick in the 2020 NHL Draft?_** 

   - Main options: either keep this year’s or defer and send next year’s 

   - **1st goal** : figure out the value of each 1st round draft slot 

   - **2nd goal** : predict where the Penguins will finish in the 2020-2021 season to figure out where they will most likely select in next year’s draft 

5 



### **Our Data** 

- Multiple different data sources, all publicly available 

   - Player career statistics from **Hockey Reference** 

   - Team level standard and advanced statistics from **Hockey Reference, NHL.com, MoneyPuck.com** 

   - ○ Historical draft data from **Wikipedia and Hockey Reference** 

6 



### **Draft Slot Value Curve** 

- Goal: create a **curve** valuing each 1st round draft slot 

- _How do you measure a player’s value to a team?_ 

   - Response variable of choice: **Average Point Shares per Season** 

      - Estimates a player’s contribution to his team in terms of standings points 

      - Based on marginal goals for and marginal goals against 

- To create the curve, we used a linear regression model 

7 



<!-- Start of picture text -->
8<br><!-- End of picture text -->



### **Predicting next season performance** 

- _n_ 

- Using stats in season to predict performance in season _n_ +1 

- Standings point percentage as a response variable 

- Per-game and percentage statistics as predictors ○ xG %, Corsi %, shot attempts per game, etc. 

9 



### **Simulating Season Outcomes** 



<!-- Start of picture text -->
Random Forest model of<br>next year’s points %<br>Randomly select a tree to generate<br>a prediction for teams 1-31 PIT CGY WSH SJS<br>Team PIT CGY WSH SJS<br>Generate predicted points % for all<br>31 teams, and rank them Points % 0.655 0.476 0.573 0.612<br>Rank 3 25 20 11<br><!-- End of picture text -->

Repeat 10,000 times to get distribution of possible outcomes 

10 



<!-- Start of picture text -->
11<br><!-- End of picture text -->



### **Simulating draft orders** 



<!-- Start of picture text -->
Simulated<br>Simulated  Simulated<br>Ranking<br>Ranking Lottery  Draft Order<br>Inverted<br>for Top 3<br>Picks<br>Middle<br>Worst 15<br>Best 16 12 Picks<br>Worst 15<br>Best 16 Best 16 Last 16<br>Worst 15<br>Draft Picks<br><!-- End of picture text -->

12 



<!-- Start of picture text -->
13<br><!-- End of picture text -->



### **How do the two year’s picks compare?** 

- One-number summary of the value of a first-round pick this year versus next year 

   - 2020 = ⅛ * value of 1st overall + ⅞ * value of 15th overall 

   - **2.968304** 

   - ○ 2021 = sum of (probability of getting that pick * value) **■ 2.212194** 

- **Based on this, we believe that the Penguins should keep their 2020 1st round selection** 

14 



### **Future Work** 

- Incorporate a more precise playoff performance simulation into model 

- Consider assessing the strength of each year’s draft class we are interested in 

15 



# Thank you! 

ellingwood1@kenyon.edu reiner_j1@denison.edu,       @jillhreiner 





16 



### **Appendix** 

Data Sources: 

Sports Reference LLC. (2020). NHL Stats and History [Hockey Reference page]. Retrieved from <u><mark>https://www.hockey-reference.com/</mark></u> 

Moneypuck. (2020). NHL Team Season Level Data [Moneypuck page]. Retrieved from <u><mark>http://moneypuck.com/data.htm</mark></u> Wikipedia. (2020). NHL Entry Draft [Wikipedia page]. Retrieved from <u><mark>https://en.wikipedia.org/wiki/NHL_Entry_Draft</mark></u> National Hockey League. (2020). NHL Team Statistics [NHL page]. Retrieved from <u><mark>http://www.nhl.com/stats/teams</mark></u> 

GitHub: 

<u>https://github.com/mellingwood/CMSACdraftProject</u> - <u>https://github.com/jillreiner/cmsac penguins</u> 

17 



### **Appendix** 

References: 

CTS Co. (2020). 2008 NHL Entry Draft Transactions [Pro Sports Transactions page]. Retrieved from <u><mark>https://www.prosportstransactions.com/hockey/DraftTrades/Years/2008.htm</mark></u> McCurdy, M. B. (2020). Probabilities for the 2020 draft lotteries [Tweet]. Retrieved from <u><mark>https://twitter.com/IneffectiveMath/status/1276231524648660994</mark></u> McCurdy, M. B. (2019). Draft lottery probabilities  [Tweet]. Retrieved from <u><mark>https://twitter.com/IneffectiveMath/status/1115586301674258432?s=20</mark></u> Pittsburgh Penguins. (2020). Trade description image [Tweeted image]. Retrieved from <u><mark>https://twitter.com/penguins/status/1227046474497822721?s=20</mark></u> 

Rosen, D. (2015). Flames acquire Hamilton from Bruins for draft picks [NHL.com article]. Retrieved from <u><mark>https://www.nhl.com/news/flames-acquire-hamilton-from-bruins-for-draft-picks/c-772332</mark></u> Wyshynski, G. (2020). The NHL's 2020 draft lottery explained: Everything you need to know [ESPN article]. Retrieved from <u><mark>https://www.espn.com/nhl/story/_/id/29225536/the-nhl-2020-draft-lottery-explained-everything-need-know</mark></u> Kubatko, J. (2010). Calculating Point Shares [HockeyReference page]. Retrieved from <mark>-</mark> <u><mark>https://www.hockey reference.com/about/point_shares.html</mark></u> 

18 

Appendix: Normal year draft lottery odds 



19 

Appendix: 2020 draft lottery odds 



<!-- Start of picture text -->
Team E =<br>Team ?5<br><!-- End of picture text -->

20 

Appendix: Explanation of this year’s lottery 

### **2020 NHL Draft Lottery** 

- This year’s lottery is different! (took place June 26th) ○ 24 team playoff instead of 16 team playoff 



- Still 15 teams in the lottery ■ 7 teams that did not qualify for the playoffs 

- ■ 8 teams eliminated in the “qualifying round” ● These are “placeholder” spots in the lottery 

- Placeholder Team E won the lottery (!) 

- This means that the Penguins could get the **1st pick** (⅛) or the **15th pick** (⅞), since they have the highest point percentage of all of the teams in the qualifying round 

21 

Appendix: Variables in Next-Year Model 



22 

Appendix: Categorized 2021 pick probabilities 



23 

Appendix: Examples of what the Penguins could do with the pick 

### **What can the Penguins do from here?** 

- What’s a fair trade if the Penguins want to **trade down** ? ○ e.g. based on the value curve, pick 17 + a pick in the 2nd round = pick 15 

- **Trade up** to have a higher position in the draft 

- ● Trade for a player who can help the Penguins win now ○ Comparable: Dougie Hamilton trade ■ Boston traded defenseman Dougie Hamilton to Calgary for **pick 15** and two picks in the 2nd round 

24 


