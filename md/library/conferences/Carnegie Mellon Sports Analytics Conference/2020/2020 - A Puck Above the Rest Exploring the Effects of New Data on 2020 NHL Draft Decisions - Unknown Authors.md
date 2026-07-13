<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2020/2020 - A Puck Above the Rest Exploring the Effects of New Data on 2020 NHL Draft Decisions - Unknown Authors.pdf -->

A Puck Above the Rest: Exploring the Effects of New Data on 2020 NHL Draft Decisions Ashley Mullan and Lucy Ward October 25, 2020 Advisors: S. Ventura, N. Citrone, R. Yurko 

### Problem Background and Objective 

- The NHL draft usually runs in late June. 

- COVID-19 forced the 2020 draft to run in early October. 

- Multiple European leagues began prior to the draft, so 2020 prospects from these leagues had more data available. 



- _Objective: Model players’ future performance given their amateur performance and assess the impact the of additional data on their value_ 

2 

### Data 

- Season-level data from amateur and professional seasons from 2010 to 2020 

- Player characteristics and statistics 

- Team-level statistics (games played, goals scored, goals against) 

- ● New metrics (relative age, PTPP) 

ID Name DOB Country HT WT Position Shoots GP G A P PM Jake 1994199870 USA 180 82 LW/C L 60 29 44 73 13 Guentzel 10-06 

3 

### Data Modification and Response Metric 

- Player statistics scaled by number of games played 

- ● Response Metric: Professional Total Point Percentage (PTPP) 

𝑃𝑙𝑎𝑦𝑒𝑟𝑃𝑜𝑖𝑛𝑡𝑠𝑝𝑒𝑟𝐺𝑎𝑚𝑒= 

𝑝𝑙𝑎𝑦𝑒𝑟<sup>′</sup> 𝑠𝑡𝑜𝑡𝑎𝑙𝑠𝑒𝑎𝑠𝑜𝑛𝑝𝑜𝑖𝑛𝑡𝑠 𝑝𝑙𝑎𝑦𝑒𝑟<sup>′</sup> 𝑠𝑡𝑜𝑡𝑎𝑙𝑔𝑎𝑚𝑒𝑠𝑖𝑛𝑠𝑒𝑎𝑠𝑜𝑛 

𝑝𝑟𝑜𝑡𝑒𝑎𝑚<sup>′</sup> 𝑠𝑡𝑜𝑡𝑎𝑙𝑠𝑒𝑎𝑠𝑜𝑛𝑝𝑜𝑖𝑛𝑡𝑠 𝑃𝑟𝑜𝑇𝑒𝑎𝑚𝑃𝑜𝑖𝑛𝑡𝑠𝑝𝑒𝑟𝐺𝑎𝑚𝑒= 𝑔𝑎𝑚𝑒𝑠𝑖𝑛𝑠𝑒𝑎𝑠𝑜𝑛 

𝑃𝑇𝑃𝑃= 

𝑃𝑙𝑎𝑦𝑒𝑟𝑃𝑜𝑖𝑛𝑡𝑠𝑝𝑒𝑟𝐺𝑎𝑚𝑒 𝑃𝑟𝑜𝑇𝑒𝑎𝑚𝑃𝑜𝑖𝑛𝑡𝑠𝑝𝑒𝑟𝐺𝑎𝑚𝑒 

4 

### Prior Research 

- Earlier draft choice results in better outcomes, but this effect is muted after 100 decisions. (Tingling et al, 2011) 

- A Poisson GAM successfully models time on ice while including non-linear effects. (Schuckers, 2016) 

- Players born in the first quarter made up the greatest percentage of the draft class. (Deaner et al, 2013) 

- Early birthdays, size advantages, and anaerobic power increase chances of draft selection. (Rocznioc et al, 2013) 

5 



### Approach 

- Identify players from target leagues, both those who were drafted to the NHL and those who were not 

- Model future performance given selection to NHL 

- Scale expected performance by probability of making NHL 

- Observe how predictions change when more data is added to simulate early Fall 2020 games 

6 

### Target Leagues: Early Season Starts 

- Czech Leagues 

   - (Czech, Czech2) 

- Russian Leagues 

   - (KHL, MHL) 

- Swiss Leagues 







   - (NLA) 

- Swedish Leagues 

   - (SHL, Allsvenskan, J18-Allsvenskan, Superelit) 



7 

8 



9 



## Draft Probability Model 

_Goal: Predict a player’s probability of being drafted into the NHL._ 

10 

11 



## NHL Performance Model 

_Goal: Given that a player was drafted into the NHL, model his value to his NHL team based on his amateur statistics._ 

12 



13 

### Joint Metric: Combining Draft Probability with Expected Performance 



14 

### Future Directions 

- Improve accuracy of performance model with a potential different response variable 

- Consider how to correct for lack of independence of draft probability and expected performance 

- Incorporate league strength metric into player assessment to allow for broader application 

15 

# Any questions? 

ashley.mullan@scranton.edu @ashley___mullan lward7@uwyo.edu @_lucyward_ 

16 


