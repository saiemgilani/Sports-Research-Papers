<!-- source: library/conferences/New England Symposium on Statistics in Sports/2011/2011 - Seed distributions for NCAA men's basketball tournament Why it may not matter who plays whom - Unknown Authors.pdf -->

###### Seed Distributions for the NCAA Men’s Basketball Tournament: Why it May Not Matter Who Plays Whom* 

**Sheldon H. Jacobson** Department of Computer Science University of Illinois at Urbana-Champaign <u>shj@illinois.edu https://netfiles.uiuc.edu/shj/www/shj.html</u> 



* Joint work with, Alexander G. Nikolaev, Adrian, J. Lee, Douglas M. King 

(C)2011 Jacobson 

NCAA BB March Madness 

1 

#### NCAA Men’s Basketball Tournament 

- National Collegiate Athletic Association (NCAA) Men’s DI College Basketball Tournament (aka March Madness) 

– First held in 1939 with 8 teams 

   - Since 1985, 64 teams participate annually 

      - Increased to 68 teams with four play-in games (2011) 

- Popularity of gambling on tournament games – Estimated $2.25B (US) wagered on 2007 Final Four through illegal channels alone 

   - Common types of gambling: traditional (single game) and office pool (entire tournament bracket) 

   - Goal: Forecast the winners of one or more tournament games 

NCAA BB March Madness 

(C)2011 Jacobson 

2 

### Predicting Game Winners 

Models have been proposed to forecast game winners (e.g., binary win/lose, final score difference) 

###### •Predictors: 

– Outcomes of season games (winner, score) – Las Vegas odds 

   - Other rankings (RPI, Sagarin, Massey, Pomeroy) 

- •Useful to the general public? 

– Difficult to gather relevant predictor data and implement the model – Simple alternatives are attractive 

(C)2011 Jacobson 

NCAA BB March Madness 

3 

### Tournament Structure 

- Selection committee 

   - Chooses 37 “at large” participants (31 conference champions) 

– Creates 4 regions of 16 teams each (plus 4 play-in game teams) – Assigns an integer seed to each team in each region, with values from 1 (best) to 16 (worst) 

   - Several issues unrelated to team skill are considered (geography, conference affiliation) when placing teams in regions 

- Format of the bracket in each region 

   - Single elimination 

   - First round: seed _k_ plays seed 17- _k_ 

   - – Later rounds: opponents determined by results of earlier rounds 

(C)2011 Jacobson 

NCAA BB March Madness 

4 

###### **ROUND 1 ROUND 2 ROUND 3** 

###### **ROUND 4 REGIONAL WINNER** 

Seed 1 <u>{1, 16}</u> List of possible seeds in Seed 16 each game of the <u>{1, 8, 9, 16}</u> Seed 8 regional tournaments <u>{8, 9}</u> {1, 4, 5, 8, 9, Seed 9 12, 13, 16} Seed 5 <u>{5, 12}</u> Seed 12 <u>{4, 5, 12, 13}</u> Seed 4 <u>{4, 13}</u> Seed 13 {1, 2, …, 16} Seed 6 <u>{6, 11}</u> Seed 11 <u>{3, 6, 11, 14}</u> Seed 3 <u>{3, 14}</u> {2, 3, 6, 7, 10, Seed 14 11, 14, 15} Seed 7 <u>{7, 10}</u> Seed 10 <u>{2, 7, 10, 15}</u> Seed 2 (C)2011 Jacob ~~son~~ <u>{2, 15}</u> NCAA BB March Madness 5 Seed 15 

###### **ROUND 1** 

###### **ROUND 2 ROUND 3** 

###### **ROUND 4 REGIONAL WINNER** 

<u>Seed 1 Seed 1</u> ~~Seed 16~~ <u>Seed 8 Seed 8</u> ~~Seed 9~~ <u>Seed 5 Seed 5</u> ~~Seed 12~~ <u>Seed 4 Seed 4</u> ~~Seed 13~~ <u>Seed 6 Seed 6</u> ~~Seed 11~~ <u>Seed 3 Seed 3</u> ~~Seed 14~~ <u>Seed 7 Seed 7</u> ~~Seed 10~~ <u>Seed 2</u> (C)2011 Jacobson <u>Seed 2</u> NCAA BB March Madness ~~Seed 15~~ 

If “best” teams win in the first round, seed _k_ plays seed 9- _k_ in the second round 

6 

###### **ROUND 1** 

###### **ROUND 2** 

###### **ROUND 3** 

###### **ROUND 4 REGIONAL WINNER** 

<u>Seed 1</u> ~~Seed 16~~ 

<u>Seed 1</u> ~~Seed 16~~ <u>Seed 1 Seed 8</u> ~~<u>Seed 8</u> Seed 9~~ <u>Seed 5</u> ~~<u>Seed 5</u> Seed 12~~ <u>Seed 4 Seed 4 Seed 4</u> ~~Seed 13~~ <u>Seed 6</u> ~~<u>Seed 6</u> Seed 11~~ <u>Seed 3 Seed 3 Seed 3</u> ~~Seed 14~~ <u>Seed 7</u> ~~<u>Seed 7</u> Seed 10~~ <u>Seed 2 Seed 2</u> (C)2011 Jacobson <u>Seed 2</u> NCAA BB March Madness ~~Seed 15~~ 

If “best” teams win in the second round, seed _k_ plays seed 5- _k_ in the third round 

7 

###### **ROUND 1** 

###### **ROUND 2** 

###### **ROUND 3** 

###### **ROUND 4 REGIONAL WINNER** 

<u>Seed 1 Seed 1</u> ~~Seed 16~~ <u>Seed 1 Seed 8</u> ~~<u>Seed 8</u> Seed 9~~ <u>Seed 1 Seed 5</u> ~~<u>Seed 5</u> Seed 12~~ ~~<u>Seed 4</u>~~ <u>Seed 4 Seed 4</u> ~~Seed 13~~ <u>Seed 1 Seed 6</u> ~~<u>Seed 6</u> Seed 11~~ ~~<u>Seed 3</u>~~ <u>Seed 3 Seed 3</u> ~~Seed 14~~ ~~<u>Seed 2</u>~~ <u>Seed 7</u> ~~<u>Seed 7</u> Seed 10~~ <u>Seed 2 Seed 2</u> (C)2011 Jacobson <u>Seed 2</u> NCAA BB March Madness ~~Seed 15~~ 

8 

### The Final Four 

- Four regional winners meet in two more rounds 

- Two identical seeds can play in a single game 

**TOURNAMENT ROUND 5 ROUND 6 CHAMPION** <u>Reg1 Winner Reg2 Winner</u> 

- Any seed can play against any seed (in theory) 

<u>Reg3 Winner</u> 

<u>Reg4 Winner</u> 

NCAA BB March Madness 

(C)2011 Jacobson 

9 

#### Is It Best To Pick the Better Seed? 

- One way to forecast winners **: Pick the better seed** – Simplicity of this method makes it attractive 

- – Does it provide good predictions? 

- Selection committee tends to assign better seeds to better teams 

- When seed differences are large, games tend to be more predictable (and hence, fewer upsets) 

(C)2011 Jacobson 

NCAA BB March Madness 

10 

### Predictions by Round 

• As the tournament progresses, seed differences tend to be smaller – 70% in round 4 (Elite Eight) have been seeded No. 3 or better – 76% in round 5 (National Semi-final) have been seeded No. 3 or better – 83% in round 6 (National Final) have been seeded No. 3 or better – 89% of tournament champions have been seeded No. 3 or better 

- Other indicators of success? 

   - _r_<sup>th</sup> _r_ 

   - To appear in the round, a team must have won its preceding -1 games 

   - – Teams with worse seeds tend to face more skilled competition earlier in the tournament 

- Are seed less informative as tournament progresses? – Jacobson and King (2009) focus on the top three seeds. 

(C)2011 Jacobson 

NCAA BB March Madness 

11 

### Goals of the Study 

- Compare historical performance of the seed distributions in each round. 

- Model the seed distributions in each round 

- Comparisons model with statistical hypothesis testing – __<sup>2</sup> Goodness-of-fit 

- Data Sources 

– NCAA: Historical tournament results (1985 – 2010) 

(C)2011 Jacobson 

NCAA BB March Madness 

12 

#### Statistical Hypothesis Testing Requirements 

- A sufficient number of samples 

   - 1,638 total games (63 games over 26 years) 

      - Play-in and First Four games not included 

   - When subsets are taken based on seeds and rounds, sample sizes drop dramatically 

- A random sample. To this effect, assume: 

   - Historical data are a representative sample of each seed’s performance 

   - – Each seed has a constant probability of winning against any other seed in a specified round 

(C)2011 Jacobson 

NCAA BB March Madness 

13 

## The Math Behind The Numbers 

(C)2011 Jacobson 

NCAA BB March Madness 

14 

### Geometric Distribution 

- Common (nonnegative) discrete random variable. 

- Defined as the number of independent and identically distributed Bernoulli random variables (with probability p) until the first success occurs. 

- If Y is distributed geometric with probability p, then P{Y=k} = (1-p)<sup>k-1</sup> p, k=1,2,…. 

(C)2011 Jacobson 

NCAA BB March Madness 

15 

#### Key Theorem* 

Let X1, X2, … be an arbitrary sequence of  Bernoulli trials.  Let Z be the number of these Bernoulli trials until the first success. Then Z is a geometric random variable with probability p iff P{Xi = 1 | h=1,2,…,i-1 Xh = 0} = p for all i = 1,2,…. 

**Implication:** Provides a N&S condition for a geometric RV. 

**Intuition** : If the first i-1 seed positions have not advanced to the next round (i.e., won), then the probability that the ith seed position advances is p, the same value for all seed positions i. 

- Shishebor and Towhidi (2004) 

(C)2011 Jacobson 

NCAA BB March Madness 

16 

### Sets of Seeds in Each Round 

- Possible seeds defined by _sets of seeds_ in each round 

   - First round: Seed No. n plays Seed No. 17-n, n = 1,2,…,8 

- Rounds r = 1,2,3: 

   - 2<sup>4-r</sup> non-overlapping sets of 2<sup>r</sup> possible winners • r = 1: {1,16} {2,15}, {3,14}, {4,13}, {5,12}, {6,11}, {7,10}, {8,9} 

   - • r = 2: {1,8,9,16}, {2,7,10,15}, {3,6,11,14}, {4,5,12,13} 

   - • r = 3: {1, 4,5, 8,9, 12,13,16}, {2,3,6,7,10,11,14,15} 

- Rounds r = 4,5,6: 

   - One set of 16 possible winners 

Define Z as the j<sup>th</sup> set in the r<sup>th</sup> round j,r Define t as the i<sup>th</sup> element in set Z i,j,r j,r 

(C)2011 Jacobson 

NCAA BB March Madness 

17 

Truncated Geometric Distribution Truncate the geometric distribution (finite number of seeds) 

– Ensure that discrete probabilities sum to one 

For set j in round r,       P{Z = t } =  p (1-p )<sup>i-1</sup> j,r i,j,r j,r j,r j,r 

• i = 1,2,….,min{2<sup>r</sup> ,16} 

• j = 1,2,…,max{2<sup>4-r</sup> ,1} 

• r = 1,2,…,6 

(position in set) (set in round) (round in tournament) 

– Coefficients: 

- j,r = 1/(1-(1-pj,r)<sup>2^r</sup> )  for set j = 1,2,…, 2<sup>4-r</sup> in round r = 1,2,3 

-  r = 1/(1-(1-pr,1)<sup>16</sup> )  for round r = 4,5,6 (only one set j = 1). 

Important Note: 

must be estimated for _in each set in each_ p _each position_ j,r _round_ 

(C)2011 Jacobson 

NCAA BB March Madness 

18 

##### Geometric Distribution Validation: Values for p r <u>j,</u> 

|**Round r**<br>**Set j**|**Position i**<br>**pj,r**||
|---|---|---|
|1<br>1,2,3,4,5,6,7,8|1<br>(1.00, .961, .846, .788, .663, .683, .596|, .461)|
|2<br>1,2,3,4|1<br>2<br>(.875, .644, .510, .423)<br>(.692, .486, .725, .633)||
|3<br>1,2|1<br>2<br>(.721, .462)<br>(.483, .464)||
||3<br><br> <br>(.467, .433)<br>||
||||
||(., .)||
|4<br>1<br><br>|1<br>2<br>3<br>4<br>5<br>6<br>(.433)<br>(.390)<br>(.361)<br>(.391)<br>(.429)<br>(.375)<br><br>||
|5<br>1|1<br><br>(.481)<br>||
||2<br>(407)||
||3<br>.<br>(.500)||
|6<br>1|1<br>2<br>3<br>(.615)<br>(.400)<br>(.500)||
|(C)2011 Jacobson|NCAA BB March Madness|19|





### Probability of Seed Combinations 

R(r) = 2<sup>6-r</sup> = number of teams that win in round r = 1,2,…,6. – Teams that advance to the next round 

Given that there are four nonoverlapping regions, there are 

- four independent geometric rv’s for each set in round r = 1,2,3,4, 

- two independent geometric rv’s for r = 5, 

- one geometric rv’s for r = 6 

Probability of seed combinations in a round are computed by taking the product of 

– Probabilities of each seed appearing in that round 

- Number of distinct permutations that the four seeds can assume in set j in round r across the four regions 

(C)2011 Jacobson 

NCAA BB March Madness 

20 

### Estimates for p j,r 

- Estimates for p computed by method of moments j,r 

- Y(n,p) truncated geometric with parameter p and n E(Y(n,p)) = (1/p) – n(1-p)<sup>n</sup> /(1-(1-p)<sup>n</sup> ) 

- Iterative bisection algorithm used to solve for an estimate of p using the average seed position over the past 26 j,r 

- tournaments in each set (j) within each round (r) 

|**Round r**|**Set j**|**pj,r**|
|---|---|---|
|3 (Elite Eight)<br>4 (Final Four)|1,2<br>1|(.684, .455)<br>(.400)|
|5 (National Finals)<br>6(National Champion)|1<br>1|(.456)<br>(.510)|



|(C)2011 Jacobson|NCAA BB March Madness|21|
|---|---|---|





# The Final Four 

(C)2011 Jacobson NCAA BB March Madness 

22 

### Seed Fre uenc in Final Four <u>q y</u> 

|**Seed n**<br>**No. Times Actually Appeared**<br>**Expected No. Times Should Appear**<br>**n**||
|---|---|
|1<br>45<br>41.6<br>0.28||
|2<br>23<br>25.0<br>0.15||
|3<br>13<br>15.0<br>0.26<br><br><br><br><br>6.<br>41<br>45<br>2<br><br><br><br>||
|28<br>.0<br><br><br>1<br><br><br>__||
|4<br>9<br>9.0<br>0.00<br>5<br>6<br>54<br>007<br>**Stddid M**<br>6.<br>41<br>||
|.<br>.<br>6<br>3<br>3.2<br>0.02<br>7<br>0<br>1.9<br>1.94<br>**anarze easure**||
|8<br>3<br>1.2<br>2.89<br>9<br>0<br>07<br>070||
|.<br>.<br>10<br>0<br>0.4<br>0.42<br>11<br>2<br>03<br>1215||
|.<br>.<br>12<br>0<br>0.2<br>0.15<br>13<br>0<br>02<br>009||
|.<br>.<br>14<br>0<br>0.1<br>0.05<br>15<br>0<br>0.0<br>0.03||
|16<br>0<br>0.0<br>0.02||
|(C)2011 Jacobson<br>NCAA BB March Madness|23|





### Final Four Seed Combinations 

- Compute probability of Final Four seed combinations 

- Reciprocal is expected frequency between occurrences 

**Scenario Probabilty Expected # # Actual Expected Frequency Occurrences Occurrences** **<u>(years)</u>** Zero No. 1 0.130 3.4 1 7.70 Seeds One No. 1 0.346 9.0 10 2.89 Seed Two No. 1 0.346 9.0 11 2.89 Seeds Three No. 1 0.154 4.0 3 6.49 Seeds Four No. 1 0.026 0.7 1 38.46 Seeds (C)2011 Jacobson NCAA BB March Madness 24 



||Most Likely Final Four|
|---|---|
||Seed Combinations|
|**Seeds**|**Actual Occurrences**<br>**(Tournament Year)**<br>**Probability**<br>**Expected Frequency**<br>**(in Years)**|
|1,1,2,3|1991,  2001, 2009<br>0.066<br>15|
|1,1,1,2|1993<br>0.062<br>16|
|1,1,2,2|2007<br>0.055<br>18|
|1,2,2,3|1994, 2004<br>0.040<br>25|
|1,1,1,1|2008<br>0.026<br>39|
|1,2,3,3|1989, 1998, 2003<br>0.024<br>42|
|…<br>1,5,8,8|…<br>…<br>2000<br>0.0000312<br>32015|
|* Compil|ed based on data from 1985-2010 tournaments|
|(C)2011 Jac|obson<br>NCAA BB March Madness<br>25|





### Final Four Seed Combination Odds 

|**Seed Description**|**Probability**|**Expected Frequency**<br>**(years)**|
|---|---|---|
|One or More 16|0.000756|1307|
|One or More 15 or 16|0.002037|491|
|One or More 14, 15, or 16|0.004152|241|
|One or More 13, 14, 15, or 16|0.007665|130|
|One or More 12, 13, 14, 15, or 16|0.013493|74|
|One or More 11, 12, 13, 14, 15, or 16|0.023137|43|
|All 16’s|1.34 E-15|747 Trillion|
|No teams 1, 2, or 3|0.00220|454|
|No teams  1 or 2|0.016927|59|
|* Compiled based on data from 198|5-2010 tourna|ments|
|(C)2011 Jacobson<br>NCAA BB Ma|rch Madness|26|





### 2011 Final Four 

Odds against any 3,4,8,11 seeds in the Final Four: 121,000 to 1 Odds against UConn, UKentucky, Butler, VCU in the FF: 2.9 Million to 1 

Probability of UConn (#3) winning the NC: .0306 Number of ESPN Brackets: 5.9 Million Number who chose UConn: 279,308 Expected number picking UConn, assuming all No. 3 seeds are equally likely: 181,000 

(C)2011 Jacobson 

NCAA BB March Madness 

27 

### 2011 Final Four 

Probability of UKentucky (#4) winning the NC: .0150 Number of ESPN Brackets that chose UKentucky: 107,249 Expected number picking UKentucky, assuming all No. 4 seeds are equally likely: 89,000 

Probability of Butler (#8) winning the NC: .00347 Number of ESPN brackets that chose Butler: 4,325 Expected number picking Butler, assuming all No. 8 seeds are equally likely: 5,100 

Probability of VCU (#8) winning the NC: .000102 Number of ESPN brackets that chose VCU: 1,023 Expected number picking VCU, assuming all No. 11 seeds are equally likely: 600 

(C)2011 Jacobson 

NCAA BB March Madness 

28 

### Conclusions and Limitations 

- Truncated geometric distribution used to compute probability of seed combinations in each round – Distribution fits closest (via _X_<sup>2</sup> goodness of fit test) in later rounds of tournament (Elite Eight and onwards) 

- Rule changes may impact seed winning probabilities over time 

– Introduction of 35 second clock 

- Expansion of three point arc 

– Selection committee criteria changes 

- Distribution parameters, p , must be updated j,r 

- annually following each year’s tournament 

(C)2011 Jacobson 

NCAA BB March Madness 

29 

### **March Madness Let the games begin!** 











###### **http://bracketodds.cs.illinois.edu** 

**Website Developers: Ammar Rizwan and Emon Dai (Students, Department of Computer Science, University of Illinois at Urbana-Champaign)** 

(C)2011 Jacobson NCAA BB March Madness 

30 

### **Website Functionality** 

###### **Uses model to odds against seed combinations in** 

- **Elite Eight** 

- **Final Four** 

- **National Finals** 

- **National Championship** 

###### **Allows one to** 

- **Compare the relative likelihood of seed combinations** 

- **Compute conditional probabilities of seed combinations in the final two rounds.** 

**Note: Model can do much more than the web site functionality.** 

(C)2011 Jacobson 

NCAA BB March Madness 

31 

### **Thank you** 









**http://bracketodds.cs.illinois.edu** 

**Sheldon H. Jacobson, Ph.D. https://netfiles.uiuc.edu/shj/www/shj.html (217) 244-7275 Skype: sheldon.jacobson1 shj@illinois.edu** 

(C)2011 Jacobson 

NCAA BB March Madness 

32 


