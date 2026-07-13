<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2025/2025 - A smart method of developing football odds using Markov chain process a case study of FC Barcelona against Real Madrid FC - Ohakwe et al.pdf -->

J. Quant. Anal. Sports 2026; aop 

### **Research Article** 

Johnson Ohakwe*, Derrick Ofori, Canice Chimdike Ifeagwu, Bhuphesh Kumar Mishra and Daniel Emeka Ogbajie 

# **A smart method of developing football odds using Markov chain a case of FC process: study Barcelona against Real Madrid FC** 

https://doi.org/10.1515/jqas-2025-0038 Received March 5, 2025; accepted April 17, 2026; published online May 13, 2026 

**Abstract:** This study utilises the Markov Chain process to generate football odds, focusing on historic La Liga matches between FC Barcelona and Real Madrid. Using data from 93 encounters, it categorises matches based on home and away performances. Transition matrices derived from historical results calculate probabilities for match outcomes (win, draw, loss) and over/under goal markets, which are then converted into betting odds. Findings reveal Barcelona’s strong home advantage, with a 55 % probability of winning (odds: 1.82), while Real Madrid has a 59 % probability at home (odds: 1.69). However, both teams experience a significant drop when playing away – Barcelona with 24 % (odds: 4.17) and Real Madrid with 23 % (odds: 4.35). The study also shows a higher likelihood of over 1.5 and 2.5 goals in their matches. This research highlights the Markov Chain process as an effective tool for improving football odds accuracy, offering a data-driven alternative to subjective betting models. 

**Keywords:** football; sports analytics; Markov chain process; long-run probability; stochastic modelling; odds 

***Corresponding author: Johnson Ohakwe** , Data Science, University of Gloucestershire, 47E Lansdown Crescent, Cheltenham, GL50 2NG, UK, E-mail: ohakwejohnson@gmail.com. https://orcid.org/0009-0003-1608-5280 

**Derrick Ofori** , Data Science, University of Gloucestershire, Cheltenham, UK 

**Canice Chimdike Ifeagwu** , Sports Performance Analysis, University of Gloucestershire, Cheltenham, UK 

**Bhuphesh Kumar Mishra** , Center of Excellence for Data Science, Artificial Intelligence and Modelling (DAIM), University of Hull, Hull, UK **Daniel Emeka Ogbajie** , Statistics, Michael Okpara University of Agriculture, Umudike, Abia, Nigeria 

## **1 Introduction** 

Football, with its roots dating back to the mid-19th century, has evolved into a global phenomenon, captivating millions worldwide. Tracing its historical trajectory, Murray and Murray (1998) and Goldblatt (2007) chronicle the transformation of football from a local pastime to a cultural touchstone. The sport’s journey reflects societal shifts and has given rise to iconic moments, shaping the collective consciousness of diverse communities. Football’s historical context provides a foundation for understanding its impact on societies and sets the stage for the nuanced exploration of predictive modeling in the realm of football odds. 

The establishment of La Liga in 1929 stands as a pivotal moment in the history of Spanish football. As detailed by Balagué (2012) and Lowe (2014), La Liga has grown into one of the most prestigious football leagues globally. The league’s narrative is woven with intense rivalries, none more prominent than the clashes between FC Barcelona and Real Madrid FC. These encounters transcend mere sporting events, becoming cultural phenomena that define the Spanish football landscape. Understanding the historical evolution of La Liga is crucial for contextualizing the significance of the matchups between these two football giants. 

In the realm of sports betting, the development of football odds has undergone a continuous evolution, driven by the pursuit of accurate predictive models. Traditional methods, such as historical performance analysis, team statistics, and expert opinions, have long been employed by bookmakers. The works of Tsampazis and Tefas (2018) and Han et al. (2022) underscore the importance of statistical modelling and data analysis in sports betting. While historical performance analysis involves assessing a team’s past record, team statistics consider factors like possession, shots on target, and goals scored. Expert opinions, often based on qualitative assessments, provide additional insights into team dynamics. These methods, though valuable, are limited in 

Open Access. © 2026 the author(s), published by De Gruyter. 

This work is licensed under the Creative Commons Attribution 4.0 International License. 

> **2 —** J. Ohakwe et al.: A smart method of developing football odds using Markov chain 

their ability to capture the dynamic and temporal aspects of football matches. 

This research seeks to navigate the intricate landscape of football odds development, focusing on innovative methodologies beyond conventional approaches. While traditional methods offer valuable insights, they often fall short in predicting the outcomes of football matches with high accuracy. In contrast to machine learning and advanced statistical techniques, the study explores lesser-known methods, such as heuristic models and rule-based systems, to highlight their potential drawbacks and limitations in providing robust football odds predictions. Understanding the limitations of these methods becomes essential in framing the rationale for adopting the Markov Chain process. 

The adoption of the Markov Chain process represents a paradigm shift in our approach to developing football odds. Recent studies by Xu et al. (2019) and Kim and Cha (2022) have demonstrated the efficacy of Markov Chain models in capturing the dynamic nature of sports events. Unlike traditional methods, Markov Chains excel in modelling state transitions and temporal dependencies, offering a more nuanced understanding of the evolving dynamics within a football match. By integrating this process into our study, we aim to harness its capacity to account for the unpredictable nature of football, providing a more comprehensive and accurate method for generating football odds. This research not only contributes to the academic discourse on sports analytics but also offers practical implications for the sports betting industry, particularly in predicting outcomes for high-profile matchups such as those between FC Barcelona and Real Madrid FC (1929–2022). In doing so, it contributes to the ongoing dialogue on the intersection of historical football dynamics and innovative predictive modelling. 

The structure of this paper is organized as follows: Section 2 outlines the data collection and preprocessing methods utilized to analyze historical match outcomes and odds for FC Barcelona and Real Madrid FC in the Spanish LaLiga. This section also provides an overview of the Markov Chain framework, introducing key concepts such as transition probabilities, long-run probabilities (steady state probabilities), and odd methodologies for determining match outcomes and odds. Section 3 presents the results of the analysis, highlighting the long-run probabilities and odds associated with the home and away performances of both FC Barcelona and Real Madrid FC. Finally, Section 4 summarizes the study’s key findings and their implications, discussing practical applications for sports analysts, coaches, and the betting industry. 

## **2 Methodologies** 

### **2.1 Data collection and preprocessing** 

The dataset utilized in this investigation encompasses historical and contemporary match outcomes involving Barcelona and Real Madrid football clubs in the Spanish LaLiga. The primary source of the data is the official LaLiga website (www.laliga.com). To ensure the integrity and reliability of the information, the data collection process adhered to the guidelines and protocols stipulated by LaLiga. 

After data collection, a meticulous preprocessing phase was undertaken to enhance the analytical suitability of the dataset. The match results were systematically encoded to facilitate a standardized representation, wherein outcomes were classified into distinct categories. Specifically, the outcomes were coded as follows: ‘W’ denoting a Win, ‘D’ signifying a Draw, ‘L’ indicating a Loss, ‘O’ representing Over 1.5 goals and Over 2.5 goals (Dixon and Coles 1997), and ‘U’ representing Under 1.5 goals, and Under 2.5 goals (Dixon and Coles 1997). This categorical encoding strategy ensures a coherent and uniform framework for subsequent analytical procedures, affording clarity and precision in the interpretation of match results. The utilization of standardized codes contributes to the establishment of a rigorous foundation for subsequent statistical analyses and modeling processes. 

### **2.2 Markov chain process** 

A Markov chain represents a discrete stochastic process wherein the current random variable _Xi_ is contingent upon the preceding variable _Xi_ −1 and influences solely the subsequent variable _Xi_ +1. The nomenclature “Markov chain” implies an interconnection between random variables within their immediate sequential vicinity. A stochastic process is deemed to possess the Markov property, also recognized as the memoryless property, if _P_<sup>(</sup> _Xi_ +1 = 1| _Xi_ = 1<sup>)</sup> holds true for all pairs of indices _i_ and _j_ . This Markovian property can be demonstrated as equivalent to the assertion that conditional probability regarding any forthcoming events is contingent solely upon the present state and remains independent of the historical sequence. Hence, the Markov property stipulates that the probability distribution governing the system’s evolution in the subsequent step, and potentially all future steps, is contingent exclusively upon the current state of the system, devoid of any reliance on prior history. 

Considering the stochastic and unpredictable nature of system transitions, the precise determination of the system’s 

J. Ohakwe et al.: A smart method of developing football odds using Markov chain **— 3** 

future state becomes inherently unattainable. The alterations in the system’s state are denoted as transitions, and the associated probabilities governing various state changes are recognized as transition probabilities. These transition probabilities encapsulate the likelihoods of moving from one state to another within the Markov chain framework, providing a comprehensive understanding of the system’s dynamic evolution. 

#### **2.2.1 Transition probability** 

A transition probability represents the likelihood of transitioning from one state to another within a given system. Stochastic processes constitute a contemporary focus within the field of statistical time series analysis, involving observations made over time periods influenced by inherent uncertainties. In the context of discrete random processes, the system can exist in multiple states, undergoing random changes in discrete increments. The Markov property dictates that the probability distribution governing the system’s state at the subsequent step, and indeed all ensuing steps, is contingent solely upon the present state of the system during preceding steps. Given the inherently random nature of system transformations, accurate prediction of the system’s precise state in the future becomes a formidable task. The shifts in the system’s states are termed transitions, with the associated probabilities of these state changes designated as transition probabilities. These transition probabilities encapsulate the likelihood of transitioning between different states within the framework of a Markovian process, providing a quantitative understanding of the system’s dynamic evolution. 

A Markov chain denoted by ( _Xn_ , _n >_ 0), defined by _Pij_ ( _n_ − 1, _n_ ) = _Pij_ ( _Xij_ = 1), is referred to as the one-step transitional probability. This transitional probability is considered timehomogeneous if _Pij_ ( _M_ , _m_ + _n_ ) = _Pij_ ( _n_ ), signifying that the _n_ -step transitional probability is contingent solely upon _n_ . The organization of these transitional probabilities is conventionally presented in matrix form. 



where _Pij_ is the probability of movements from state _i_ to state _j_ , and the formula for calculating it is given by: 



where _M_ is the number of movements from state _i_ to state _ij j_ during the period of time under discussion and _n_ is the number of states. 

The transition probability matrix, integral to this study, pertains to the home and away performances of FC Barcelona against Real Madrid FC (1929–2022). The first considered is the transition matrix represented as: 



Then, the transition probability matrix is presented as follows: 



The transition probability matrix concerning the occurrence of over 1.5 (2 goals and above) or under 1.5 (below 2 goals) goals, as well as over 2.5 (3 goals and above) or under 2.5 (below 3 goals) goals, pertaining to the performances of Barcelona and Real Madrid at home and away against Real Madrid and Barcelona, respectively. Its transition matrix is represented as: 



Then its transition probability matrix is presented as below: 



The expressions (2.3)–(2.6) are derived through the systematic enumeration of match results (transitions) characterized by specific sequential outcomes. These outcomes include two consecutive wins ( _WW_ ), two consecutive draws ( _DD_ ), two consecutive losses ( _LL_ ), as well as combinations such as two consecutive win-draw ( _WD_ ), two consecutive draw-win ( _DW_ ), two consecutive win-loss ( _WL_ ), two consecutive loss-win ( _LW_ ), two consecutive draw-loss ( _DL_ ), and two consecutive loss-draw ( _LD_ ). Furthermore, the analysis encompasses scenarios of playing over 1.5 or over 2.5 goals in two consecutive matches ( _OO_ ), playing under 1.5 or under 2.5 goals in two consecutive matches ( _UU_ ), playing overunder 1.5 or over-under 2.5 goals in two consecutive matches ( _OU_ ), and playing under-over 1.5 or under-over 2.5 goals in 

> **4 —** J. Ohakwe et al.: A smart method of developing football odds using Markov chain 

two consecutive matches ( _UO_ ). The next step involves the calculation of the transition probabilities associated with these occurrences, denoted as _PWW_ , _PDD_ , _PLL_ , _PWD_ , _PDW_ , _PWL_ , _PLW_ , _PDL_ , _PLD_ , _POO_ , _PUU_ , _POU_ , and _PUO_ , by employing the formula articulated in (2.2). 

#### **2.2.2 Steady state/long-run probability** 

know what value is attached to their option of play and what return to expect in the case of a successful bet. Odds are calculated mathematically as: 



where: _P_ is the probability of an event. 

The steady-state probability, also known as the stationary distribution, of a Markov chain, refers to the long-term probabilities of the system being in each state after it has run for a sufficiently long time (Heyman 1991). In this study, it is the long-term probabilities of the system being in each state ([win, draw, and loss], [over 1.5 and under 1.5], and [over 2.5 and under 2.5]) after the system has run for a sufficiently long time. This is mathematically represented as: 



where: **_𝝅_** is a row vector and a left eigenvector of the transition probability matrix **P** corresponding to the eigenvalue 1. 

## **3 Results and discussion** 

### **3.1 FC Barcelona at home against Real Madrid FC** 

The results of the matches played by FC Barcelona at home against Real Madrid FC are coded as follows: 

LLWDDLWLDWLDLWWWWWLWWWWDWWLWWLWLL LWWDDWLWWDDWWL WLWWWLWWWWWDWWDWWWWWWWDWDDLWDDL WWWLDWWLDDWDLLW 

With a total of 93 matches, 51 wins, 20 draws, and 22 losses, results to the transition matrix below: 

### **2.3 Odds** 

Odds are values (numbers) that represent the likelihood of a specific event occurring or not, they are often expressed as the reciprocal of its probability (Gujarati 2011). In sports (football), bookmakers use odds to represent events such as win, draw, loss, among others, in the bet markets so bettors 



And the transition probability matrix as seen in (3.2) and Figure 1. 



**Figure 1:** A transition diagram of FC Barcelona at home against Real Madrid FC. 

J. Ohakwe et al.: A smart method of developing football odds using Markov chain **— 5** 

**Table 1:** Long-run probability and odds of FC Barcelona at home against Real Madrid FC. 

||**Long-run probability**|||**Odds**||
|---|---|---|---|---|---|
|**W**|**D**|**L**|**W**|**D**|**L**|
|0.55|0.22|0.23|1.82|4.55|4.35|



less likely outcomes. These findings demonstrate the effectiveness of using the Markov Chain approach for modelling match outcomes and generating fair betting odds. 

### **3.2 Real Madrid FC at home against FC Barcelona** 

|||_W_|_D_|_L_||
|---|---|---|---|---|---|
|_P_ =|_W_<br>_D_<br><br><br><br>|⎡<br>⎢<br>⎢<br><br>28∕50 <br>9∕20|10∕50 <br>6∕20|12∕50<br>5∕20<br>⎤<br>⎥<br>⎥<br>|(3.2)|
||_L_<br>|⎣<br>14∕22|4∕22|4∕22<br>⎥⎦||



The results of the matches played by Real Madrid FC at home against FC Barcelona are coded as follows: 

LWDWWWWWWLWWLWWWDLWWWWWWWWWW WWWWWWLWDWDLDDLWL DWWWWWLWLWDDWWWWDWLWDWLDWDWDLWLW WLLDLWLWLLLLWWLW 

The results presented in Table 1 provide the long-run probabilities and corresponding odds for FC Barcelona’s home matches against Real Madrid FC, derived using the Markov Chain process. The long-run probabilities indicate that FC Barcelona has a 55 % chance of winning ( _W_ = 0.55), a 22 % chance of drawing ( _D_ = 0.22), and a 23 % chance of losing ( _L_ = 0.23). While Real Madrid FC the away team has a 23 % chance of winning ( _W_ = 0.23), 55 % chance of losing ( _W_ = 0.55), and same 22 % chance of drawing ( _D_ = 0.22) as FC Barcelona. These probabilities are reflected in the calculated odds of 1.82 for a win, 4.55 for a draw, and 4.35 for a loss for FC Barcelona at home. For Real Madrid FC at away, 4.35 for a win, 1.82 for a loss, and same 4.55 for a draw. The high probability of a win underscores FC Barcelona’s strong performance at home, while the relatively balanced probabilities of a draw or a loss indicate that matches remain competitive when playing against Ral Madrid FC. The odds align with these probabilities, offering lower values for more likely outcomes and higher values for 

With a total of 93 matches, 55 wins, 15 draws, and 23 losses, results to the transition matrix below: 



And the transition probability matrix as seen in (3.4) and Figure 2. 



Table 2 presents the long-run probabilities and corresponding odds for Real Madrid CF in home matches against FC Barcelona, where Barcelona is the away team. These estimates were obtained using the Markov Chain modelling 



**Figure 2:** A transition diagram of Real Madrid FC at home against FC Barcelona. 

> **6 —** J. Ohakwe et al.: A smart method of developing football odds using Markov chain 

**Table 2:** Long-run probability and odds of Real Madrid FC at home against FC Barcelona. 

||**Long-run probability**|||**Odds**||
|---|---|---|---|---|---|
|**W**|**D**|**L**|**W**|**D**|**L**|
|0.59|0.17|0.24|1.69|5.88|4.17|



### **3.3 FC Barcelona at home against Real Madrid FC (over/under 1.5)** 

The results of total goals (over/under 1.5) scored in the matches played by FC Barcelona at home against Real Madrid FC are coded as follows: 

OOOOOOOOUOOOOOUOOOOOOUOOOUOOOOOOOOOO OOUUUUUUOO 

framework. The results indicate a 59 % probability of a home win for Real Madrid ( _W_ = 0.59), a 17 % probability of a draw ( _D_ = 0.17), and a 24 % probability of a loss ( _L_ = 0.24). Since Barcelona is the away side, the 24 % loss probability for Real Madrid corresponds directly to the probability of an away win for Barcelona. The findings therefore suggest a strong home advantage for Real Madrid, with the likelihood of securing a victory substantially exceeding both the probability of a draw and that of an away win by Barcelona. The associated odds, 1.69 for a home win, 5.88 for a draw, and 4.17 for an away win are consistent with the estimated probabilities. The most likely outcome (a Real Madrid home win) is assigned the lowest odds, while less probable outcomes (draw or Barcelona away win) attract higher odds. Overall, the results highlight Real Madrid’s statistical dominance under home conditions, while still reflecting the competitive nature of the fixture when Barcelona plays away. 

OOOOOOOOOOOOUOOOOOUOUOOOOOUOOOOUOUOO OOOOOOOUOOO 

With a total of 93 matches, 76 over 1.5 (2 goals and above), and 17 under 1.5 (below 2 goals), results to the transition matrix below: 



And the transition probability matrix as seen in (3.6) and Figure 3. 



Table 3 presents the long-run probabilities and odds for the over/under 1.5 goals market in matches where FC Barcelona plays at home against Real Madrid FC, analysed using the Markov Chain process. The results indicate a high probability of over 1.5 goals ( _O_ = 0.82), corresponding to 



**Figure 3:** A transition diagram of FC Barcelona at home against Real Madrid FC (over/under 1.5). 

J. Ohakwe et al.: A smart method of developing football odds using Markov chain **— 7** 

**Table 3:** Long-run probability and odds of FC Barcelona at home against Real Madrid FC (over/under 1.5). 

||**Long-run probability**|||**Odds**|
|---|---|---|---|---|
|**O**||**U**|**O**|**U**|
|0.82||0.18|1.22|5.56|



82 %, while the probability of under 1.5 goals ( _U_ = 0.18) is 18 %. The associated odds are 1.22 for over 1.5 goals (2 goals and above) and 5.56 for under 1.5 goals (below 2 goals). The dominance of the over 1.5 outcome suggests that matches between these two teams under these conditions are likely to feature 2 or more goals, reflecting their offensive tendencies and attacking style of play. The significantly lower probability and higher odd for under 1.5 goals suggest that such low-scoring outcomes are relatively rare. 

### **3.4 Real Madrid FC at home against FC Barcelona (over/under 1.5)** 

The results of total goals (over/under 1.5) scored in the matches played by Real Madrid FC at home against FC Barcelona are coded as follows: 



And the transition probability matrix as seen in (3.8) and Figure 4. 



Table 4 provides the long-run probabilities and odds for the over/under 1.5 goals market in matches where Real Madrid FC plays at home against FC Barcelona, as determined using the Markov Chain process. The probability of over 1.5 goals ( _O_ = 0.86) is 86 %, while the probability of under 1.5 goals ( _U_ = 0.14) is 14 %. The corresponding odds are 1.16 for over 1.5 goals and 7.14 for under 1.5 goals. The high probability and low odds of over 1.5 goals suggest that matches between these teams in this setting are predominantly high scoring, likely influenced by their attacking playstyles and tactical approaches. Conversely, the low probability of under 1.5 goals reflects the rarity of low scoring outcomes, as evidenced by the significantly higher odds for this result. 

UOUOOOOOOOOOUUOOOOOOOOOOOUOUOOOOOOOUOO OUOUOUOO OOOOOOOOOOUOOOUOOUOOOOOOOOOOOOOOOOOOOO OOOOUOOOO 

With a total of 93 matches, 79 over 1.5 (2 goals and above), and 14 under 1.5 (below 2 goals), results to the transition matrix below: 

### **3.5 FC Barcelona at home against Real Madrid FC (over/under 2.5)** 

The results of total goals (over/under 2.5) scored in the matches played by FC Barcelona at home against Real Madrid FC are coded as follows: 



**Figure 4:** A transition diagram of Real Madrid FC at home against FC Barcelona (over/under 1.5). 

> **8 —** J. Ohakwe et al.: A smart method of developing football odds using Markov chain 

**Table 4:** Long-run probability and odds of Real Madrid FC at home against FC Barcelona (over/under 1.5). 

**Table 5:** Long-run probability and odds of FC Barcelona at home against Real Madrid FC (over/under 2.5). 

||**Long-run** **probability**||**Odds**|
|---|---|---|---|
|**O**|**U**|**O**|**U**|
|0.86|0.14|1.16|7.14|



||**Long-run probability**||**Odds**|
|---|---|---|---|
|**O**|**U**|**O**|**U**|
|0.64|0.36|1.56|2.78|



OOOOUOOOUOUOOOUOOOOOOUOOUUUOOOOOOOOO UUUUUUUUOO 

OUUOOOOOUOOUUOOUOOUOUOOOUUUOOUOUUUOO OOOOUOOUOOO 

With a total of 93 matches, 60 over 2.5 (3 goals and above), and 33 under 2.5 (below 3 goals), results to the transition matrix below: 



And the transition probability matrix as seen in (3.10) and Figure 5. 



Table 5 presents the long-run probabilities and corresponding odds for the over/under 2.5 goals market in matches where FC Barcelona plays at home against Real Madrid FC, based on the Markov Chain process. The analysis shows a 64 % probability of over 2.5 goals ( _O_ = 0.64) and a 36 % probability of under 2.5 goals ( _U_ = 0.36). The associated odds are 1.56 for over 2.5 goals and 2.78 for under 2.5 goals. 

These results suggest that matches in this scenario are more likely to feature 3 or more goals, consistent with the attacking capabilities and offensive strategies of both teams. However, the 36 % probability of under 2.5 goals indicates a moderate chance of relatively low scoring encounters, reflecting occasional defensive discipline or strategic conservatism. The calculated odds align with these probabilities, offering lower odds for the more likely outcome (over 2.5 goals) and higher odds for the less likely scenario (under 2.5 goals). 

### **3.6 Real Madrid FC at home against FC Barcelona (over/under 2.5)** 

The results of total goals (over/under 2.5) scored in the matches played by Real Madrid FC at home against FC Barcelona are coded as follows: 

UOUUOOOOOOOOUUOOUOOOOOOOOUOUUOUUOOOUU OOUUUOUUU 

OOOOOUOOOUUOOOUUOUOUUOOOOUUOOOUOOUUOO OOOOOUUOOO 

With a total of 93 matches, 59 over 2.5 (3 goals and above), and 34 under 2.5 (below 3 goals), results to the transition matrix below: 



**Figure 5:** A transition diagram of FC Barcelona at home against Real Madrid FC (over/under 2.5). 

J. Ohakwe et al.: A smart method of developing football odds using Markov chain **— 9** 



**Figure 6:** A transition diagram of Real Madrid FC at home against FC Barcelona (over/under 2.5). 



And the transition probability matrix as seen in (3.12) and Figure 6. 



Table 6 provides the long-run probabilities and odds for the over/under 2.5 goals market in matches where Real Madrid FC plays at home against FC Barcelona, calculated using the Markov Chain process. The probability of over 2.5 goals ( _O_ = 0.64) is 64 %, while the probability of under 2.5 goals ( _U_ = 0.36) is 36 %. The corresponding odds are 1.56 for over 2.5 goals and 2.78 for under 2.5 goals. These results suggest that matches in this scenario are more likely to feature 3 goals and above, reflecting the attacking prowess and high scoring potential of both teams in such fixtures. The 36 % likelihood of under 2.5 goals indicates a reasonable chance of lower scoring matches, possibly influenced by defensive strategies or tactical adjustments. The odds reflect these probabilities, with over 2.5 goals being the more likely 

**Table 6:** Long-run probability and odds of Real Madrid FC at home against FC Barcelona (over/under 2.5). 

||**Long-run probability**||**Odds**|
|---|---|---|---|
|**O**|**U**|**O**|**U**|
|0.64|0.36|1.56|2.78|



outcome, hence receiving lower odds, while under 2.5 goals is assigned higher odd. 

## **4 Conclusions** 

This study demonstrated the utility of the Markov Chain process in accurately developing football odds by modelling match outcomes between FC Barcelona and Real Madrid FC. The study highlights the power of this statistical technique to predict the likelihood of various outcomes such as wins, draws, and losses as well as over/under goal scenarios, offering a data driven and methodical approach to sports odds generation. One of the key components of this study was the use of the Markov Chain model to predict the long-run probabilities of different match outcomes, which were then translated into odds. The odds associated with these probabilities provide a quantitative measure of the likelihood of various match results, directly informing betting markets. In the context of FC Barcelona and Real Madrid FC, the study provided a detailed breakdown of the odds for both the outcome of the match (win, draw, loss) and for specific goal thresholds (over/under 1.5 and 2.5 goals). 

In the case of FC Barcelona’s home matches against Real Madrid FC at away, the study revealed that the probabilities of a win ( _W_ = 0.55), draw ( _D_ = 0.22), and loss ( _L_ = 0.23) were reflected in odds of 1.82, 4.55, and 4.35, respectively. The relatively low odds for a win (1.82) suggest that this outcome is the most probable and therefore attracts the least return. Conversely, the higher odds for a draw (4.55) and loss (4.35) indicate that these results are less likely, with betters receiving higher payouts if they bet on less probable outcomes. The alignment of odds with probabilities is 

> **10 —** J. Ohakwe et al.: A smart method of developing football odds using Markov chain 

key to ensuring that the betting market reflects the actual chances of different outcomes occurring. In the case of FC Barcelona’s away matches (Real Madrid at home), the odds were notably higher, reflecting the team’s lower probability of success on the road. With a 24 % chance of winning, FC Barcelona’s odds were calculated as 4.17 for a win, 5.88 for a draw, and 1.69 for a loss. Here, the odds for a loss (1.69) were the lowest, reflecting Real Madrid’s stronger performance when playing at home. The significant difference in odds between home and away games underscores the importance of home advantage in football, with teams often more successful when playing in familiar surroundings, as shown by both FC Barcelona’s and Real Madrid’s home match odds (1.82 and 1.69 respectively). 

In addition to match outcome odds, this study also considered the goal markets (over/under), which provide additional betting options for the number of goals scored during a match. The results for both FC Barcelona’s and Real Madrid’s home matches against each other indicated a strong trend towards high-scoring encounters. For FC Barcelona’s home games, the probability of over 1.5 goals was 82 % (odds of 1.22), and for over 2.5 goals, it was 64 % (odds of 1.56). These low odds reflect the high probability of these outcomes, suggesting that betters are likely to see 2 or more goals in these fixtures. The significantly higher odds for under 1.5 goals (5.56) and under 2.5 goals (2.78) indicate that these outcomes are much less likely to occur, providing greater potential returns for betters willing to take the risk. For Real Madrid’s home games, the probability of over 1.5 goals was even higher at 86 % (odds of 1.16), while over 2.5 goals had a 64 % probability (odds of 1.56). Again, the odds for under 1.5 goals (7.14) and under 2.5 goals (2.78) reflect the rarity of such low scoring results in this fixture. The consistency in the results for both teams suggests that their encounters are generally high scoring affairs, and the odds calculated using the Markov Chain process reflect this tendency accurately. 

The odds calculated through the Markov Chain process not only provide a clearer understanding of match probabilities but also offer an insight into the dynamics of sports betting. The odds generated in this study provide betters with a more transparent and scientifically driven understanding of what to expect from each match outcome, reducing the influence of external factors that could distort betting predictions, but it’s important to note that these odds could either be decreased or increased by bookmakers or betting companies to suit their narrative. Most times this could be because of a lot of factors like injured players, 

team’s current form, team news, availability of players, media narratives, among others. 

By deriving odds based on historical data and longrun probabilities, this research demonstrates the potential for advanced statistical techniques to improve the betting industry. The findings suggest that such models can be applied to other football teams, leagues, and even other sports to enhance the accuracy of predictions and betting odds. Future research may extend this work by incorporating higher-order Markov models, non-homogeneous transition matrices, covariate-adjusted stochastic processes, or Bayesian updating techniques to improve dynamic responsiveness. 

The odds derived through the Markov Chain process offer a sophisticated and reliable method of assessing football match outcomes. This research has shown that FC Barcelona’s home advantage and Real Madrid’s dominance at home are well-reflected in the odds, with the probabilities of wins, draws, and losses translating into appropriate odds for bookmakers and sports betters. The over/under goal market odds provide additional insight into the nature of matches between these teams, highlighting their tendency for high scoring encounters. 

**Acknowledgments:** The authors would like to express their deep gratitude to a higher power. They would also like to extend their sincere appreciation to the Editor-in-Chief and the anonymous reviewers for their insightful feedback, which greatly improved the quality of this paper. 

**Research ethics:** The local Institutional Review Board deemed the study exempt from review. 

##### **Informed consent:** Not applicable. 

**Author contributions:** All authors have accepted responsibility for the entire content of this manuscript and approved its submission. 

**Use of Large Language Models, AI and Machine Learning Tools:** None declared. 

**Conflict of interest:** The authors state no conflict of interest. **Research funding:** None declared. 

**Data availability:** The data that support the findings of this study are openly available in www.laliga.com. 

## **References** 

Balagué, G. (2012). _Pep Guardiola: another way of winning_ − _the biography_ . Orion, London. 

Dixon, M.J. and Coles, S.G. (1997). Modelling association football scores and inefficiencies in the football betting market. _J. Roy. Stat. Soc. C Appl. Stat._ 46: 265−280,. 

J. Ohakwe et al.: A smart method of developing football odds using Markov chain **— 11** 

- Goldblatt, D. (2007). _The ball is round: a global history of soccer_ . Penguin UK, London. 

- Gujarati, D. (2011). _Econometrics by example_ . Palgrave Macmillan, Basingstoke. 

- Han, R., Shi, S., Hu, T., and Tao, S. (2022). Prediction of future NBA games’ point difference: a statistical modelling approach. _J. Phys.: Conf. Ser._ 2386: 012003,. 

- Heyman, D.P. (1991). Approximating the stationary distribution of an infinite stochastic matrix. _J. Appl. Probab._ 28: 96−103,. 

- Kim, K. and Cha, S. (2022). Soccer analysis based on Markov Chain and PCA. In: _2022 IEEE international conference on big data (big data)_ , pp. 6708−6710. 

- Lowe, S. (2014). _Fear and loathing in La Liga: Barcelona, Real Madrid, and the world’s greatest sports rivalry_ . Bold Type Books, New York. 

- Murray, B. and Murray, W.J. (1998). _The world’s game: a history of soccer_ . University of Illinois Press, Urbana, IL. 

- Tsampazis, K. and Tefas, A. (2018). Deep sparse autoencoders for football match and bet prediction. In: _Proceedings of the 10th Hellenic conference on artificial intelligence_ , pp. 1−8. 

- Xu, Y., Zhang, Q., and Tan, Z.C. (2019). The application of Markov chains in multiplayer online battle arena (MOBA) games. In: _IRC-SET 2018: proceedings of the 4th IRC conference on science_ . Engineering and Technology, pp. 97−110. 


