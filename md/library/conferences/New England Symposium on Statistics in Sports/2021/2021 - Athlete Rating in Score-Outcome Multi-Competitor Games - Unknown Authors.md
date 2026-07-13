<!-- source: library/conferences/New England Symposium on Statistics in Sports/2021/2021 - Athlete Rating in Score-Outcome Multi-Competitor Games - Unknown Authors.pdf -->



# Athlete rating in score-outcome multi-competitor games 



<!-- Start of picture text -->
JONATHAN CHE & MARK GLICKMAN<br>SUPPORTED BY US OLYMPIC & PARALYMPIC COMMITTEE<br><!-- End of picture text -->

JONATHAN CHE & MARK GLICKMAN SUPPORTED BY US OLYMPIC & PARALYMPIC COMMITTEE 



# Athlete rating 



### Athlete ratin <u>g</u> 



<!-- Start of picture text -->
weak strong<br><!-- End of picture text -->

NESSIS 2021 

3 

### Athlete ratin <u>g</u> 





<!-- Start of picture text -->
W<br>weak strong<br>L<br><!-- End of picture text -->



NESSIS 2021 

4 

### Athlete ratin <u>g</u> 



<!-- Start of picture text -->
W<br><!-- End of picture text -->



<!-- Start of picture text -->
weak strong<br>L<br><!-- End of picture text -->

NESSIS 2021 

5 

### Wrinkle 1: “multi-com etitor” <u>p</u> 







NESSIS 2021 

6 

### Wrinkle 1: “multi-com etitor” <u>p</u> 





















- "A stochastic rank ordered logit model for rating multi-competitor games and sports“ (Glickman & Hennessy 2015) 

NESSIS 2021 

7 

### Wrinkle 2: “score-outcome” 



<!-- Start of picture text -->
65<br>7<br><!-- End of picture text -->



<!-- Start of picture text -->
60<br>8<br><!-- End of picture text -->



<!-- Start of picture text -->
43<br>9<br><!-- End of picture text -->



<!-- Start of picture text -->
42<br>10<br><!-- End of picture text -->



<!-- Start of picture text -->
97<br>1<br><!-- End of picture text -->



<!-- Start of picture text -->
82<br>2<br><!-- End of picture text -->



<!-- Start of picture text -->
81<br>3<br><!-- End of picture text -->



<!-- Start of picture text -->
80<br>4<br><!-- End of picture text -->



<!-- Start of picture text -->
74<br>5<br><!-- End of picture text -->



<!-- Start of picture text -->
71<br>6<br><!-- End of picture text -->

8 

NESSIS 2021 

# A model for athlete rating 



D namic linear model DLM : visual idea <u>y ( )</u> Harville (1977); Glickman & Stern (1998) 



<!-- Start of picture text -->
Observed scores<br>Athlete<br>latent<br>ability<br>time<br><!-- End of picture text -->

NESSIS 2021 

10 

### DLM: standard e uations <u>q</u> 

#### 𝑡 : For each athlete in game 𝑔 within time period 



<!-- Start of picture text -->
observation<br>observed score latent ability<br>variance<br>𝜃<br>𝑝 𝑦 𝑡, 𝜎 2 = 𝑁(𝜃𝑡, 𝜎 2 )<br>𝑔𝑡<br>𝜃 𝜃<br>𝑝 𝑡+1 𝑡, 𝜎 2 = 𝑁(𝜃𝑡, 𝜎 2 𝑊)<br>innovation<br>variance ratio<br>initial ability<br>𝜎 2 = 𝐼𝐺 𝑎<br>𝑝 0, 𝑏0 variance ratio<br>𝜃 𝜎 2 𝑉 We can fit this model using<br>𝑝 1 = 𝑁(0, 𝜎 2 0)<br>Kalman Filter equations<br><!-- End of picture text -->

NESSIS 2021 

11 

Modification 1: game-specific effects 𝑡 : For each athlete in game 𝑔 within time period 

𝜃 = 𝑁 𝜃 𝑝 𝑦 𝑡, 𝜎<sup>2</sup> 𝑡, 𝜎<sup>2</sup> 𝑔𝑡 𝜃 𝜃 𝑝 𝑡+1 𝑡, 𝜎<sup>2</sup> = 𝑁(𝜃𝑡, 𝜎<sup>2</sup> 𝑊) 

NESSIS 2021 

12 

### Modification 1: game-specific effects 

𝑡 : For each athlete in game 𝑔 within time period 

− 𝜃 𝜃 𝜃 𝑝 𝑦 −ത𝑦 𝑡, 𝜎<sup>2</sup> = 𝑁( 𝑡 , 𝜎<sup>2</sup> ) 𝑔𝑡 𝑔𝑡 𝑔𝑡 𝜃 𝜃 𝑝 𝑡+1 𝑡, 𝜎<sup>2</sup> = 𝑁(𝜃𝑡, 𝜎<sup>2</sup> 𝑊) 

NESSIS 2021 

13 

### Modification 2: data transformations 

𝑡 : For each athlete in game 𝑔 within time period 

− 𝜃 𝜃 𝜃 𝑝 𝑦 −ത𝑦 𝑡, 𝜎<sup>2</sup> = 𝑁( 𝑡 , 𝜎<sup>2</sup> ) 𝑔𝑡 𝑔𝑡 𝑔𝑡 𝜃 𝜃 𝑝 𝑡+1 𝑡, 𝜎<sup>2</sup> = 𝑁(𝜃𝑡, 𝜎<sup>2</sup> 𝑊) 



NESSIS 2021 

14 

### Modification 2: data transformations 

𝑡 : For each athlete in game 𝑔 within time period 

− 𝑡 𝜃 𝜃 𝜃 𝑝 𝜆(𝑦 −ത𝑦 ) 𝑡, 𝜎<sup>2</sup> = 𝑁( 𝑡 , 𝜎<sup>2</sup> ) 𝑔𝑡 𝑔𝑡 𝑔𝑡 𝜃 𝜃 𝑝 𝑡+1 𝑡, 𝜎<sup>2</sup> = 𝑁(𝜃𝑡, 𝜎<sup>2</sup> 𝑊) 

NESSIS 2021 

15 

### Transformations: Yeo-Johnson 

(Yeo & Johnson 2000) 

> <sup>𝜆</sup> 𝑌𝐽 ( 𝑦+ 1 −1)/𝜆 𝑦≥0 𝑡𝜆 𝑦<sup>2−𝜆</sup> 𝑦< 0 −( −𝑦+ 1 −1)/(2 −𝜆) = ൝ 𝜆= 0.8 𝜆= 1.2 



<!-- Start of picture text -->
𝜆= 0.8<br><!-- End of picture text -->



<!-- Start of picture text -->
𝜆= 1.2<br><!-- End of picture text -->

NESSIS 2021 

16 

### Transformations: monotone s line <u>p</u> 

(Ramsay 1988) 

𝐵 𝑀𝑆 𝑡 𝜆 ⋅𝐼 𝝀 𝑏 𝑏(𝑦) 𝑦= ෍ 𝑏=1 









NESSIS 2021 

17 

# Fitting the model 



### DLM with transformation: full model 

𝑡 : For each athlete in game 𝑔 within time period 

− 𝑡 𝜃 𝜃 𝜃 𝑝 𝜆(𝑦 −ത𝑦 ) 𝑡, 𝜎<sup>2</sup> = 𝑁( 𝑡 , 𝜎<sup>2</sup> ) 𝑔𝑡 𝑔𝑡 𝑔𝑡 𝜃 𝜃 𝑝 𝑡+1 𝑡, 𝜎<sup>2</sup> = 𝑁(𝜃𝑡, 𝜎<sup>2</sup> 𝑊) 

NESSIS 2021 

19 

### DLM with transformation: full model 

𝑡 : For each athlete in game 𝑔 within time period 

𝝀 − 𝜃 𝜃 𝜃 𝑝 𝝍𝑡 𝑡, 𝜎<sup>2</sup> = 𝑁( 𝑡 𝑔𝑡, 𝜎<sup>2</sup> ) 𝜃 𝜃 𝑝 𝑡+1 𝑡, 𝜎<sup>2</sup> = 𝑁(𝜃𝑡, 𝜎<sup>2</sup> 𝑊) 

NESSIS 2021 

20 

### DLM with transformation: full model 



<!-- Start of picture text -->
𝑝 𝑦1:𝑇, 𝜃1:𝑇, 𝜎 2 , 𝑊, 𝜆=<br>priors for  𝜎 2 , 𝑊, 𝜆<br>𝜆<br>transformation<br>𝐽 𝜓1:𝑇 →𝑦1:𝑇 × 𝑝 𝜎 2 𝑝 𝑊𝑝 𝜆<br>Jacobian<br>𝑇 𝑇<br>𝜆 2<br>𝑝(𝜓𝑡 ∣𝜃𝑡, 𝜎 𝑝(𝜃𝑡 ∣𝜃𝑡−1, 𝜎 2 , 𝑊)<br>× ෑ , 𝜆) × ෑ<br>𝑡=1 𝑡=1<br>likelihood innovation<br><!-- End of picture text -->

NESSIS 2021 

21 

### DLM with transformation: model fittin <u>g</u> 



<!-- Start of picture text -->
Goal:<br>𝜎 2 𝑊<br>𝜃<br>𝑝 1:𝑇, 𝜎 2 , 𝑊, 𝜆∣𝑦1:𝑇<br>𝜽1 𝜽2 … 𝜽𝑇<br>𝝍1 𝝍2 … 𝝍𝑇<br>𝝀<br><!-- End of picture text -->

NESSIS 2021 

22 

### DLM with transformation: model fittin <u>g</u> 



<!-- Start of picture text -->
Goal:<br>𝜎 2 𝑊<br>𝑝 𝑊, 𝜆∣𝑦1:𝑇<br>𝜽1 𝜽2 … 𝜽𝑇<br>𝝍1 𝝍2 … 𝝍𝑇<br>𝝀<br><!-- End of picture text -->

NESSIS 2021 

23 

### DLM with transformation: model fittin <u>g</u> 

𝑝 𝑊, 𝜆∣𝑦1:𝑇 

𝜃 𝑑𝜃 𝑑𝜎<sup>2</sup> = ∫𝑝 1:𝑇, 𝜎<sup>2</sup> , 𝑊, 𝜆∣𝑦1:𝑇 1:𝑇 

NESSIS 2021 

24 

### DLM with transformation: model fittin <u>g</u> 

Given 𝑊 and 𝝀 : 

𝑝 𝑊, 𝜆∣𝑦1:𝑇 

1. Use Kalman Filter to help evaluate 𝑝(𝜓𝑡𝜆 ∣𝜓1:𝑡−1𝜆 , 𝑊, 𝜆) for 𝑡= 1, … , 𝑇 2. Compute 𝑝 𝑊, 𝜆∣𝑦1:𝑇 

𝜃 𝑑𝜃 𝑑𝜎<sup>2</sup> = ∫𝑝 1:𝑇, 𝜎<sup>2</sup> , 𝑊, 𝜆∣𝑦1:𝑇 1:𝑇 



<!-- Start of picture text -->
𝜆 𝑇 𝜆 𝜆<br>= 𝐽 𝜓1:𝑇 →𝑦1:𝑇 × 𝑝 𝑊𝑝 𝜆× ς𝑡=1 𝑝(𝜓𝑡 ∣𝜓1:𝑡−1, 𝑊, 𝜆)<br>transformation  priors for  𝑊, 𝜆 posterior predictive<br>Jacobian t-distributions<br><!-- End of picture text -->

NESSIS 2021 

25 

DLM with transformation: model fittin <u>g</u> Goal: find posterior mode of 𝑝(𝑊, 𝝀∣𝒚1:𝑇) 

max 𝑊,𝝀<sup>𝑝(𝑊, 𝝀∣𝒚1:𝑇)</sup> ≥0 ∀𝑖 subject to 𝑊, 𝜆𝑖 

NESSIS 2021 

26 

# Results 



### Recoverin the true transformation <u>g</u> 



<!-- Start of picture text -->
𝑌𝐽<br>𝑡0.8(𝑥)<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑥 𝑥<br>𝑌𝐽<br>𝑡1.2(𝑥) 50 ⋅atan ( 50 ⋅tan (<br>50 ) 50 )<br><!-- End of picture text -->









28 

NESSIS 2021 

### Model com arison: other models <u>p</u> 





Rank-order logit model (ROL) 

Vanilla DLM (VLM) 

NESSIS 2021 

29 

### Model comparison: train/test split 

Training set Test set 

Find 𝑊<sup>෡</sup> & 𝜆<sup>መ</sup> Make predictions 

NESSIS 2021 

30 

### Data 

Multicompetitor: 







Head-to-head: 





NESSIS 2021 

31 

### Model com arison: multi-com etitor data <u>p p</u> 

Games 𝑔 , time periods 𝑡 , correlations 𝜌 , competition sizes 𝑛 : 𝑔𝑡 𝑔𝑡 

|||𝜌=|σ𝑡=𝑠+<br>𝑇<br>σ𝑡=𝑠<br>𝑇|1<br>σ𝑔=1<br>𝑁𝑔𝑡<br>𝑛<br>+1<br>σ𝑔=1<br>𝑁𝑔𝑡|𝑔𝑡−1 𝜌𝑔𝑡<br>𝑛𝑔𝑡−1|||||
|---|---|---|---|---|---|---|---|---|---|
|||Diving|||Biathlon||Bia|thlon re|lay|
|Metric|VLM|LMT|ROL|VLM|LMT|ROL|VLM|LMT|ROL|
|Spearman|**0.62**|0.58|0.61|0.61|0.60|**0.61**|0.75|**0.77**|0.75|
|Kendall|**0.48**|0.45|0.47|0.44|0.44|**0.44**|0.59|**0.60**|0.58|



NESSIS 2021 

32 

### Model com arison: head-to-head data <u>p</u> 



<!-- Start of picture text -->
Ru b Fencin 15  ts<br>g y g ( p )<br>Metric VLM LMT GLO VLM LMT GLO<br>Accuracy .72 .73 .70 .66 .70 0.68<br><!-- End of picture text -->

NESSIS 2021 

33 

### Initial conclusions 

1. Difficult to improve on ROL predictions for given datasets 

2. Scores may help more in low-data settings 

Does the LMT have any other nice features? 

NESSIS 2021 

34 

Ex lorin results: ost. redictive intervals <u>p g p p</u> 



NESSIS 2021 

35 

### Ex lorin results: residuals <u>p g</u> 



<!-- Start of picture text -->
Biathlon<br><!-- End of picture text -->



<!-- Start of picture text -->
VLM LMT<br><!-- End of picture text -->

NESSIS 2021 

36 

### Ex lorin results: residuals <u>p g</u> 



<!-- Start of picture text -->
Diving<br><!-- End of picture text -->



<!-- Start of picture text -->
VLM LMT<br><!-- End of picture text -->

NESSIS 2021 

37 

### Ex lorin results: transformations <u>p g</u> 



<!-- Start of picture text -->
Biathlon<br><!-- End of picture text -->



<!-- Start of picture text -->
Diving<br><!-- End of picture text -->



<!-- Start of picture text -->
Biathlon relay<br><!-- End of picture text -->



<!-- Start of picture text -->
Fencing Rugby<br><!-- End of picture text -->

38 

NESSIS 2021 

### Ex lorin results: athlete stren ths <u>p g g</u> 



NESSIS 2021 

39 

### Conclusion 





<!-- Start of picture text -->
𝜌<br><!-- End of picture text -->



NESSIS 2021 

40 

### References 

Glickman, Mark E., and Jonathan Hennessy. "A stochastic rank ordered logit model for rating multi-competitor games and sports." Journal of Quantitative Analysis in Sports 11.3 (2015): 131-144. 

Glickman, Mark E., and Hal S. Stern. "A state-space model for National Football League scores." Journal of the American Statistical Association 93.441 (1998): 25-35. 

Harville, David. "The use of linear-model methodology to rate high school or college football teams." Journal of the American Statistical Association 72.358 (1977): 278-289. Ramsay, James O. "Monotone regression splines in action." Statistical science 3.4 (1988): 425-441. 

Yeo, In‐Kwon, and Richard A. Johnson. "A new family of power transformations to improve normality or symmetry." Biometrika 87.4 (2000): 954-959. 

NESSIS 2021 

41 

## Thank you! 



### DLM: model matrix notation 

𝑁 𝑁 𝑡 : total athletes, athletes playing in game 𝑔 within time period 𝑔𝑡 

𝜃 𝜽 ⋅𝐼 𝑝 𝒚 𝑡, 𝜎<sup>2</sup> = 𝑁(𝑋 𝑡, 𝜎<sup>2</sup> 𝑁 ) 𝑔𝑡 𝑔𝑡 𝑔𝑡 𝜽 𝜽 𝑊⋅𝐼 𝑝 𝑡+1 𝑡, 𝜎<sup>2</sup> = 𝑁(𝜽𝑡, 𝜎<sup>2</sup> 𝑁) 

⋯ 1 0 0 0 ⋯ 0 0 1 0 𝑋𝑔𝑡 = ⋯ ⋯ ⋯ ⋯ (multicompetitor game) ⋮ ⋯ 0 0 0 1 𝑁 × 𝑁 𝑔𝑡 𝑋𝑔𝑡 = 1 −1 0 ⋯ 0 (head-to-head game) 

NESSIS 2021 

43 

### DLM: full model 

𝑇 𝑇 𝑝 𝑦1:𝑇, 𝜃1:𝑇, 𝜎<sup>2</sup> = ς𝑡=1 𝑝(𝑦𝑡 ∣𝜃𝑡, 𝜎<sup>2</sup> ) × ς𝑡=1 𝑝(𝜃𝑡 ∣𝜃𝑡−1, 𝜎<sup>2</sup> ) × 𝑝(𝜎<sup>2</sup> ) 



<!-- Start of picture text -->
𝜎 2<br>𝜽1 𝜽2 … 𝜽𝑇<br>𝒚1 𝒚2 … 𝒚𝑇<br><!-- End of picture text -->

NESSIS 2021 

44 

### DLM: osterior u dates <u>p p</u> 

𝜽 Target: 𝑝 1:𝑇, 𝜎<sup>2</sup> ∣𝒚1:𝑇 



<!-- Start of picture text -->
Prior: Posterior:<br>Likelihood:<br>𝜽𝑡|𝜎𝜎 22 ∼𝑁(𝒎∼𝐼𝐺(𝑎𝑡−1𝑡−1, 𝜎, 𝑏 2 𝑡−1⋅𝑉)𝑡−1) & 𝒚𝑡 ∼𝑁(𝑋𝑡 ⋅𝜽𝑡, 𝜎 2 ⋅𝐼𝑁𝑡) = 𝜽𝑡|𝒚𝜎𝑡 2 , 𝜎|𝒚 2 𝑡∼𝑁(𝒎∼𝐼𝐺(𝑎𝑡𝑡, 𝜎, 𝑏 2 𝑡)⋅𝑉𝑡)<br>Innovation period:<br>𝜽𝑡+1 ∣𝜽𝑡∼𝑁(𝜽𝑡, 𝜎 2 𝑊)<br><!-- End of picture text -->

NESSIS 2021 

45 

### Exploring results: optim() convergence 

Monotone spline for biathlon dataset 



NESSIS 2021 

46 

### Transformations: monotone s line <u>p</u> 

(Ramsay 1988) 

𝐵 𝑀𝑆 𝑡 𝜆 ⋅𝐼 𝝀 𝑖 𝑖(𝑦) 𝑦= ෍ 𝑖=1 



NESSIS 2021 

47 

### DLM with transformation: model fittin <u>g</u> 

𝑝 𝑊, 𝜆∣𝑦1:𝑇 

𝜃 𝑑𝜃 𝑑𝜎<sup>2</sup> = ∫𝑝 1:𝑇, 𝜎<sup>2</sup> , 𝑊, 𝜆∣𝑦1:𝑇 1:𝑇 

𝜆 𝑇 𝜆 𝜆 = 𝐽 𝜓1:𝑇 →𝑦1:𝑇 × 𝑝 𝑊𝑝 𝜆× ς𝑡=1 𝑝(𝜓𝑡 ∣𝜓1:𝑡−1, 𝑊, 𝜆) 𝑏 𝑡−1 𝑇 𝑡2𝑎𝑡−1 ( 𝑋<sup>ത</sup> 𝑡𝑚𝑡−1, [𝐼+ 𝑋<sup>ത</sup> 𝑡 𝑉𝑡−1 + 𝑊𝐼 𝑋<sup>ത</sup> 𝑡 ]) 𝑎 𝑡−1 

48 

NESSIS 2021 

### DLM with transformation: model fittin <u>g</u> 

Goal: find the values of 𝑊 and 𝝀 that maximize 𝑝(𝑊, 𝜆∣𝑦1:𝑇) 

1. Initialize: set initial (𝑊, 𝝀) 

2. Optimize: use numerical optimization to find optimal value of (𝑊, 𝝀) 

Fit model using Pick 𝑊 and 𝝀 W and 𝑡 𝝀(⋅) 



Evaluate log 𝑝(𝑊, 𝝀∣𝑦1:𝑇) 

3. Return: optimal (MAP) value of 𝑊, 𝝀 

NESSIS 2021 

49 

### Ex lorin results: 95% covera e <u>p g g</u> 

||Diving|Biathlon|Biathlon Relay|Rugby|Fencing|
|---|---|---|---|---|---|
|LMNT|0.998|0.979|0.998|0.958|0.949|
|LM|0.987|0.949|0.985|0.954|0.945|



NESSIS 2021 

50 

### Ex lorin results: covera e <u>p g g</u> 



NESSIS 2021 

51 


