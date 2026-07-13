<!-- source: randoms/Modelling_the_dynamic_pattern_of_surface.pdf -->

J. Quant. Anal. Sports 2018; 14(3): 117–130 

### Rodolfo Metulini*, Marica Manisera and Paola Zuccolotto 

# **Modelling the dynamic pattern of surface area in basketball and its effects on team performance** 

https://doi.org/10.1515/jqas-2018-0041 

**Abstract:** Because of the advent of GPS techniques, a wide range of scientific literature on Sport Science is nowadays devoted to the analysis of players’ movement in relation to team performance in the context of big data analytics. A specific research question regards whether certain patterns of space among players affect team performance, from both an offensive and a defensive perspective. Using a time series of basketball players’ coordinates, we focus on the dynamics of the surface area of the five players on the court with a two-fold purpose: (i) to give tools allowing a detailed description and analysis of a game with respect to surface areas dynamics and (ii) to investigate its influence on the points made by both the team and the opponent. We propose a three-step procedure integrating different statistical modelling approaches. Specifically, we first employ a Markov Switching Model (MSM) to detect structural changes in the surface area. Then, we perform descriptive analyses in order to highlight associations between regimes and relevant game variables. Finally, we assess the relation between the regime probabilities and the scored points by means of Vector Auto Regressive (VAR) models. We carry out the proposed procedure using real data and, in the analyzed case studies, we find that structural changes are strongly associated to offensive and defensive game phases and that there is some association between the surface area dynamics and the points scored by the team and the opponent. 

**Keywords:** convex hulls; Markov Switching models; sensor data; team sports; Vector Auto Regressive models. 

## **1 Introduction** 

Research in team sports science has gained relevance in the last few years, also because of the advent of new technologies and big data. Several methods borrowed 

***Corresponding author: Rodolfo Metulini,** University of Brescia, Big & Open Data Innovation (BODaI) Laboratory, C.da S. Chiara, 50, Brescia IT 25122, Italy, e-mail: rodolfo.metulini@unibs.it **Marica Manisera and Paola Zuccolotto:** University of Brescia, Big & Open Data Innovation (BODaI) Laboratory, C.da S. Chiara, 50, Brescia IT 25122, Italy 

from machine learning, network and complex systems, geographic information system (GIS), computer vision and statistics have been proposed to solve many different research questions meeting requirements of experts, coaches and analysts. Massive literature on this topic has been well summarized by some review papers (among others, Gudmundsson and Horton, 2016 and Stein et al., 2017). 

One important line of research deals with players’ spatial dynamics analysis, which is possible by means of data coming from video analysis technologies and global positioning systems (GPS). Teammates highly interact each other and this continuous interaction takes on the features of a complex system. Network theory has been first proposed by Wasserman and Faust (1994) in the context of team sports, to analyse the network of ball passings. Passos et al. (2011) used centrality measures with the aim of identifying the key interactions and the cooperation between team members in water polo. Besides network theory, a promising niche of literature intertwined with psychology, called ecological dynamics, expresses players on the court as agents who face external factors (Turvey and Shaw 1995; Araújo, Davids, and Hristovski 2006; Araújo et al. 2009; Travassos et al. 2012; Duarte et al. 2013; Araújo and Davids 2016). Multivariate data analysis tools can also be used (see for example Metulini, Manisera, and Zuccolotto 2017a; Metulini, Manisera, and Zuccolotto 2017b), where patterns of movements in basketball are identified by means of an integration of multidimensional scaling and cluster analysis). The complex system of the interactions among players is also studied by Richardson et al. (2012) using cluster phase analysis, and by Greihaine, Godbout, and Zerai (2011) from a psychological perspective. 

The positioning of each single player in relation to teammates (and/or opponents) can play a crucial role in determining team performance. Coaching experience suggests that the team in possession of the ball should increase distance between players, while the opponent should defend by reducing distance between players (Araújo and Davids 2016). The overall spatial scattering of players on the court can be measured by several quantities (Araújo and Davids 2016): for example, the stretch index (or radius), the team spread and the effective playing space, known in the sport literature with the term 

**118** | R. Metulini et al.: Dynamic pattern of surface area in basketball 

surface area, whose influence on team performance has been investigated by several authors, in the context of different team sports (see, for example, Frencken et al., 2011; Moura et al., 2012; Fonseca et al., 2012; Travassos et al., 2012; Goldfarb, 2014). Visual analysis is frequently used to find preliminary evidence of surface area patterns (Therón and Casares 2010; Kowshik, Chang, and Maheswaran 2012; Metulini 2016). 

This paper is concerned with basketball. Scientific literature on basketball covers several aspects of research, ranging from simply outlining the main features of a game by means of descriptive statistics (Kubatko et al. 2007) to investigating more complex problems, such as forecasting the outcome of a game or a tournament (West 2008; Loeffelholz, Bednar, and Bauer 2009; Brown et al. 2010; Gupta 2015; Lopez and Matthews 2015; Ruiz and Perez-Cruz 2015; Yuan et al. 2015; Manner 2016), analysing players’ performance (Page, Fellingham, and Reese 2007; Cooper, Ruiz, and Sirvent 2009; Piette, Anand, and Zhang 2010; Fearnhead and Taylor 2011; Ozmen 2012; Page, Barney, and McGuire 2013; Deshpande and Jensen 2016), identifying optimal game strategies (Annis 2006) and describing the players’ reactions to stressful moments (Crocker and Graham 1995; Zuccolotto, Manisera, and Sandri 2017). 

Spatial dynamics analysis can be effectively applied in basketball; the most interesting issue is to determine how players’ dynamics and team performance are related each other and if the presence of a specific player or a specific lineup on the court has an effect on performance. Indeed, to measure a player’s performance is very different from assessing the impact of the player on the teammates’ behavior and, ultimately, on the team’s performance. While there are a lot of contributions in the literature about the former point, the latter is still little explored. Lamas et al. (2011), for example, define a set of “space creation dynamics” (states for the offense that produce a rupture of the defense, creating empty spaces for scoring opportunities) and show how they can be used for game analysis. In the discussion the authors point out that some players’ profile may arguably influence the increase in the recurrence of some specific dynamic in a team game strategy. Fewell et al. (2012) describe basketball team offensive strategies by their network properties, in order to capture the interactions among individuals and determine whether these interactions could be associated with team advancement in play-offs. Although this is not the basic aim of their paper, the tool they propose is well suited to assess how single players or lineups affect team performance, as it is always possible to characterize the specific network occurring when they are on the court. 

Additional investigations can be made by merging video and GPS data to play-by-play datasets. The practical possibility to do that depends of course on the availability of such data, that are usually collected by authorized operators within the activities of the basketball associations. For major competitions (NBA, FIBA) play-by-play data are largely available and characterized by an acceptable quality level. But there are other championships whose playby-play data are not easily available, or affected by missing data and recording errors. 

Limiting the focus to the analysis of players’ positions, probabilistic models of players’ coordinates have been used to split the match in phases (Perše et al. 2009; Perica, Trninić, and Jelaska 2011) according to the way players move on the court. Following this line of research, Metulini et al. (2017a,b) analyse some specific case studies focusing on surface areas and confirm the coaching knowledge that offensive and defensive phases exhibit different patterns. In this paper we investigate the association between surface area and team performance, starting from the idea of Frencken et al. (2011), who aim to define a collective variable able to measure the dynamics of team sports. In the cited paper, focused on soccer, the authors use the collective variable to identify an overall game pattern and then assume that deviations from these patterns are present in the build-up of goals. They find that surface area and centroid position may provide a sound basis for a collective variable that captures the dynamics of attacking and defending in soccer at team level. In a similar way, we translate this idea into basketball and examine surface area as a candidate for describing some basic game pattern, which remains valid whatever the game strategy. In this paper, according to Passos, Araújo, and Volossovitch (2016), we measure the surface area by the area within the convex hull of the players on the court. The centroid position is used to label the game phase (offense, defense, transition). 

To this aim, we propose a structured three-step procedure, with a two-fold purpose: (i) to give tools allowing a detailed description and analysis of a game with respect to surface area dynamics and (ii) to investigate its influence on the points made by both the team and the opponent. In detail, using a time series of surface areas from a whole match as a dependent variable, we firstly fit data with a Markov Switching Model (MSM) in order to find two regimes that account for structural changes in the space among players. Secondly, we characterize each regime in terms of its association to game phases (offense, defense, transition) and to certain game situations (i.e. presence of a given player or a combination of players on the court, 

R. Metulini et al.: Dynamic pattern of surface area in basketball | **119** 

implementation of a given playbook, ...), also defining some graphical tools able to describe the match dynamics. Finally, we resort to a Vector AutoRegressive model (VAR) in order to investigate whether changes in the regimes’ probabilities affect the performance, in terms of points made during offense and points made by the opponents when the team is in defense. We check the functioning of the proposed procedure on three real datasets collected during games played by Italian professional basketball teams in a tournament which was held in February 2017. 

The paper is structured as follows. Section 2 introduces the basketball case studies, describes the data source and the datasets manipulation, while Section 3 is devoted to the proposed three-step procedure. For each step, once described the method, we immediately show its application to the data introduced in Section 2. The obtained results are discussed in Section 4, while concluding remarks and future research developments are in Section 5. 

## **2 Case study** 

In this paper we deal with basketball sensor data. Basketball is a sport played by two teams of five players each on a rectangular court (28 m _×_ 15 m). The match, according to International Basketball Federation (FIBA) rules, lasts 40 min, and is divided in four periods of 10 min each. The objective is to shoot a ball through a hoop 46 cm in diameter and mounted at a height of 3.05 m to backboards at each end of the court. 

### **2.1 Data source** 

Data refer to players’ coordinates collected during three matches played in February 2017 by Italian professional basketball teams, at the Italian Basketball Cup Final Eight. In the following, we will refer to the three case studies with CS1, CS2 and CS3. MYagonism (https://www.myagonism. com/) was in charge to set up a system to record the players’ positioning on the court during the games. Each player worn a microchip that, having been connected with machines built around the court, collected the player’s position (in pixels of 1 m<sup>2</sup> ) in both the _x_ -axis and the _y_ -axis, as well as in the _z_ -axis (i.e. how high the player jumps). The positioning of the players has been detected with an average frequency of about 80 Hz. During the match, a total of 10 (for CS1 and CS3) and 11 (for CS2) players rotated on the court. The system recorded series of 4, 733, 124 observations for CS1, 4, 072, 227 for CS2 and 4, 906, 254 for 

CS3, each one referring to one among positioning, velocity or acceleration in one among _x_ -, _y_ - or _z_ -axis, for a specific player in a specific time instant. 

Play-by-play data are not available for this tournament, so, in order to recover at least one game variable, we collected the scores of the match at the end of every minute, by watching the video of the game. When merging these data to sensor data, the problem of time misalignment arises. The procedure we propose is also able to deal with this occurrence, as will be explained later. 

### **2.2 The dataset** 

For each case study, we start from a data matrix **X** where each row corresponds to a sensor record, described by the variables time (in milliseconds), player, team, positioning, velocity and acceleration along the court length ( _x_ ), the court width ( _y_ ) and height ( _z_ ). **X** needs several transformations in order to be ready for the analysis. 

First, it is important to clarify that data are detected with a non-constant frequency; in addition, data of different players are recorded at different time instants. As a consequence, we let the dataset contain any detected time instant _τ_ ˜, and we attribute the last datum available to players not detected in _τ_ ˜. The times _τ_ ˜ are not regularly spaced, so an adjustment procedure is needed to obtain the time series of observations drawn from regularly spaced processes. 

Second, the players’ positions are detected also during the moments when the game is off: these time instants have to be removed from the dataset. However, there is no variable labelling time instants when the game is off, so we needed rules to identify moments to be filtered out. We filter the rows of **X** in three consecutive steps, according to the following criteria: 

- instants in which the game is off due to game intervals, time-outs, pre-game and post-game: delete periods when more than or less than exactly five players exhibit both _x_ - and _y_ -axes coordinates inside the court; 

- moments when free throws are being shot: delete periods when at least one player remains inside the circle of the free throw line for at least _h_ 1 consecutive seconds. 

- other (fouls, violations, ball out, ...): delete periods in which all the five players’ velocity is smaller than _h_ 2 km/h for at least _h_ 3 consecutive seconds. 

Thresholds _h_ 1, _h_ 2 and _h_ 3 are fixed according to reasonable criteria, and then tuned by checking the sensitivity 

**120** | R. Metulini et al.: Dynamic pattern of surface area in basketball 

of results to different choices, by means of graphical representations. Some minor adjustments are made on _h_ 2 and _h_ 3 in order to obtain a total of 40 min (2,400,000 ms, subject to a certain margin of tolerance) for the final dataset. We set _h_ 1 = 10, _h_ 2 = 10 and _h_ 3 = 2.5 in CS1, _h_ 1 = 10, _h_ 2 = 9.4 and _h_ 3 = 2.5 in CS2 and _h_ 1 = 10, _h_ 2 = 9 and _h_ 3 = 2.5 in CS3. Further details about this procedure can be found in Metulini (2017). 

Finally, for CS1 the filtered matrix **X** _F_ counts for a total of effective 2,415,336 ms (40 min and 15.336 s), and contains 206,332 observations at not-regularly spaced times _τ_ ˜ (average frequency of 85.426 Hz). For CS2, **X** _F_ counts for a total of effective 2,425,346 ms (40 min and 25.346 s), and contains 232,544 observations at not-regularly spaced times _τ_ ˜ (average frequency of 95.881 Hz). For CS3, **X** _F_ counts for a total of effective 2,402,458 ms (40 min and 2.458 s), and contains 201,651 observations at not-regularly spaced times _τ_ ˜ (average frequency of 83.935 Hz). Considering CS1, apart from one player ( _p_ 9), who remained most time on the bench, the effective time (minutes:seconds) on the court of the other nine players ranges from 12:21 (player _p_ 2) to 32:17 (player _p_ 1). Only two lineups played for more than 5 min: _p_ 1, _p_ 3, _p_ 4, _p_ 6 and _p_ 10 (8:21) and _p_ 2, _p_ 3, _p_ 5, _p_ 6 and _p_ 8 (5:09). 

With regard to CS2, players _p_ 1, _p_ 2, _p_ 5 and _p_ 6 remained on the court for a large amount of time (respectively, 37:44, 27:14, 34:55 and 30:16 minutes:seconds). Totally, seven players remained in the court for at least 18 min, while other four players remained most of the time on the bench. Only two lineups played for more than 5 min: _p_ 1, _p_ 2, _p_ 4, _p_ 5 and _p_ 6 (8:59) and _p_ 1, _p_ 2, _p_ 5, _p_ 6 and _p_ 8 (5:16). 

Finally, in CS3 nine players remained on the court for a considerable amount of time, ranging from 12:57 (player _p_ 3) to 29:49 (player _p_ 5). Only one lineup played for more than 5 min: _p_ 2, _p_ 5, _p_ 6, _p_ 9 and _p_ 10 (6:23). 

We also computed new variables useful for our analysis. We first defined whether each time instant corresponds to an offensive, defensive or transition moment, depending on whether the centroid position (average coordinates of the five players on the court) on the _x_ -axis lies on the back court (defense – _D_ ), in the front court (offense – _O_ ) or in between (transition – _Tr_ , in detail, in within [ _−_ 4,+4] meters from the half court).¹ This generates the categorical variable _Pτ_ ˜, denoting the game phase, with categories _p_ = _O_ , _D_ , _Tr_ (offense, defense and transition, respectively). 

> **1** We obviously considered that teams change court side after the half-time interval. 

The instant classified as transition moments ( _Pτ_ ˜ = _Tr_ ) were 441,068 effective milliseconds (7 min and 21 s) in CS1, 433,005 (7 min and 10 s) in CS2 and 403,334 (6 min and 44 s) in CS3. Offensive phases ( _Pτ_ ˜ = _O_ ) were detected for 1,019,255 ms (16 min and 56 s) in CS1, 962,883 (15 min and 52 s) in CS2 and 951,171 (15 min and 48 s) in CS3. Lastly, defensive phases ( _Pτ_ ˜ = _D_ ) accounted for 955,013 ms (15 min and 54 s) in CS1, 1,029,458 (16 min and 58 s) in CS2 and 1,047,953 (17 min and 28 s) in CS3. 

Finally, we regularized the space between consecutive observations by selecting a row every 100 effective milliseconds. We denote with **X**<sup>**˜**</sup> _F_ the final data matrix, completed with the new variables and composed of the observations recorded at regularly spaced times<sup>˜</sup> _t_ = 1, 2, · · · , _T_<sup>˜</sup> , with a constant frequency of 10 Hz. 

## **3 Methods and analysis** 

Let C˜ _t_ be the convex hull of the five players on the court at time<sup>˜</sup> _t_ , and _A_ ˜ _t_ the corresponding area, measuring what in the sport literature is usually called surface area, as explained in the Introduction section. Basic summary statistics give a rough support to the idea (common in the coaching experience) that the surface area switches from narrow to large when moving from defense to offense phases [e.g. the median areas (in m<sup>2</sup> ) of _A_ ˜ _t|P_ ˜ _t_ = _D_ and _A_ ˜ _t|P_ ˜ _t_ = _O_ are respectively 22.6 and 52.3 in CS1, 25.8 and 44.7 in CS2, 24.4 and 44.2 in CS3]. 

We propose a three-step procedure to analyse the dynamic of _{A_ ˜ _t}_ ˜ _t_ =1,2,··· ,˜ _T_ and assess its influence on the points made by the team and the opponent. 

- Step 1: we assume a regime-switching model for the process _{A_ ˜ _t}_ , in order to detect structural changes in the surface areas; 

- Step 2: for offense and defense separately, we analyse the identified regimes dynamics and we relate them to other game variables such as, for example, the presence of a specific player on the court or the whole lineup, the implementation of a specific playbook, etc., by means of contingency tables and visual tools; 

- Step 3: we assume a multivariate model able to assess the relation between the regimes and the points scored in offense and defense phases. 

In the next subsections, for each step we will describe in detail the proposed procedure and the results obtained with the analysed data. 

R. Metulini et al.: Dynamic pattern of surface area in basketball | **121** 

### **3.1 Step 1: regime-switching surface areas** 

#### **3.1.1 Method** 

The first step assumes that the surface areas’ stochastic process is affected by recurrent structural changes involving its mean. In order to investigate this issue, we borrow models and terminology from the fairly different context of econometrics, where time series with structural changes are often analysed with regime-switching models. In that context, regimes are defined as states involving different parameters for the stochastic process under study, and they are often found to correspond to specific economic situations (e.g. expansion or recession). Translating the idea into our case study, we assume that surface area dynamics are characterized by different regimes involving different mean levels of the process, and we fit a Markov Switching Model (MSM; see Hamilton 2010) to the data coming from the process _{A_ ˜ _t}_ , observed at the equally-spaced times ˜ _t_ = 1, 2, · · · , ˜ _T_ . The model is able to detect if a regimeswitching dynamic is present, estimate the parameters of the process in the different regimes and, for each observation time, the probability of being in one regime or the other. The rationale behind this first step is built upon team sports technical considerations: it is an established fact that the space among players tends to switch from narrow to large when moving from defense to offense phases. Nevertheless, we cannot assume a strict matching between the area _A_ ˜ _t_ and the game phase. Quite the opposite, we are just interested to the moments when the surface area is different from what we would expect on the basis of the game phase, because the most intriguing game situations are hidden right there. So, the idea is to separate, in this step, regimes of narrow and large surface areas using a model not considering the game phase and, in step 2, investigate the regimes’ dynamics for offense and defense phases separately, highlighting when the regime deviates from what expected. 

Let us assume that the surface area switches between two regimes characterized by different mean levels. We call the two regimes _N_ and _L_ , standing for “narrow” and “large”, respectively ( _N_ is the regime characterized by the lower mean level, and _L_ the other one). Let _R_ ˜ _t_ be the (unobserved) random variable denoting the regime at time<sup>˜</sup> _t_ : 

(Baum et al. 1970; Lindgren 1978; Hamilton 1989), 



and we denote with _πNN_ = Pr( _R_ ˜ _t_ = _N|R_ ˜ _t−_ 1 = _N_ ) and _πLL_ = Pr( _R_ ˜ _t_ = _L|R_ ˜ _t−_ 1 = _L_ ) the two-state transition probabilities, recalling that _πNL_ = Pr( _R_ ˜ _t_ = _N|R_ ˜ _t−_ 1 = _L_ ) = 1 _− πLL_ and _πLN_ = Pr( _R_ ˜ _t_ = _L|R_ ˜ _t−_ 1 = _N_ ) = 1 _− πNN_ . Formulation (1) is perhaps the simplest assumption in the family of regime-switching models, which often assume also the presence of autoregressive components or the effect of some exogenous variables. 

After specifying Gaussian densities N( _α_<sup>(</sup><sup>_N_)</sup> , _σ_<sup>2</sup> _N_<sup>)and</sup> N( _α_<sup>(</sup><sup>_L_)</sup> , _σ_<sup>2</sup> _L_<sup>) under the two regimes, the parameter vector</sup> 



is estimated via EM algorithm, as the regime is unobserved. The estimation algorithm also returns the so-called “filtered” probabilities 



where I˜ _t_ denotes the information available up to time<sup>˜</sup> _t_ , and the corresponding “smoothed” probabilities 



obtained using all the set of information I up to time _T_<sup>˜</sup> , by means of the algorithm developed by Kim (1994). 

If the Markov chain is presumed to be ergodic, we can compute the unconditional probabilities _πr_ of the two regimes 



and their average persistence _δ_<sup>(</sup><sup>_r_)</sup> 



#### **3.1.2 Data analysis** 

We fit the MSM of equation (1) to data from the process _{A_ ˜ _t}_ , in order to detect structural changes in the expected value of the surface area.² We used the R package MSwM (Sanchez-Espigares and Lopez-Moreno 2014). 



The probabilistic model describing the regimes’ dynamics is assumed to be a two-state Markov chain 

**2** We preliminarily performed an Augmented Dickey-Fuller (ADF) test for unit roots, in order to guarantee the stationary condition. ADF test reports values equal to _−_ 6.88 for CS1, _−_ 6.52 for CS2 and _−_ 6.39 for CS3, exceeding the threshold _−_ 3.43, corresponding to _α_ = 0.01. 

**122** | R. Metulini et al.: Dynamic pattern of surface area in basketball 

**Table 1:** Markov Switching Model results (A), 95% confidence intervals for the estimated intercepts (B) and transition probabilities (C). 

||**CS1**|**CS2**|**CS3**|
|---|---|---|---|
||**Coef (S.e.)**|**Coef (S.e.)**|**Coef (S.e.)**|
|(A) Markov Switching Model results||||
|Regime N||||
|Intercept|22.060***|24.448***|21.940***|
||(0.114)|(0.123)|(0.112)|
|Residual standard error|9.156|9.328|8.760|
|Regime L||||
|Intercept|62.897***|60.857***|56.114***|
||(0.221)|(0.265)|(0.220)|
|Residual standard error|21.087|20.256|18.133|
|(B) 95% Confdence intervals for the esti|mated intercepts<br><br>|||
|Regime N|[<br>21.835; 22.284<br>]|[<br>24.207; 24.689<br>]|[<br>21.721; 22.160<br>]|
|Regime L|[<br>62.465; 63.329<br>]|[<br>60.337; 61.376<br>]|[<br>55.683; 56.545<br>]|
|(C) Transition probabilities||||
||[<br>0.986 0.013<br>]|[<br>0.987 0.018<br>]|[<br>0.986 0.013<br>]|
||0.014 0.987<br>|0.013 0.982<br>|0.014 0.987<br>|



Signif. codes: · _p <_ 0.1, * _p <_ 0.05, ** _p <_ 0.01, *** _p <_ 0.001. 

Considering CS1, and consistently with the notation used in SubSection 3.1.1, we find that the estimated intercept of regime _r_ = _L_ is larger than that of regime _r_ = _N_ (Table 1, box A), with _α_<sup>_L_</sup> = 62.897 and _α_<sup>_N_</sup> = 22.060. These estimated parameters are highly statistically significant, with _p_ -values in the order of 10<sup>_−_16</sup> . Furthermore, the 95% confidence intervals of the two parameters do not overlap (Table 1, box B). The transition probabilities (Table 1, box C) denote low probability of regime switching ( _πNN_ = 0.986 and _πLL_ = 0.987), with corresponding persistence indexes (6) given by _δ_<sup>(</sup><sup>_N_)</sup> = 71.43 and _δ_<sup>(</sup><sup>_L_)</sup> = 76.92, meaning that each regime lasts, on average, between 7 and 8 s. The unconditional probabilities (5) result _πN_ = 0.481 and _πL_ = 0.519. Results for CS2 and CS3, as shown in columns 2 and 3 of Table 1, are very similar to those of CS1. 

The filtered and smoothed probabilities _ξ_ ˜ _t_<sup>(</sup> _|_<sup>_r_</sup> ˜ _t_<sup>)and</sup><sup>_ξ_</sup> ˜ _t_<sup>(</sup><sup>_r_),</sup> defined respectively in (3) and (4), are often close to 0 or 1, suggesting a good model fit. 

### **3.2 Step 2: analysis of the regimes’ dynamics** 

#### **3.2.1 Method** 

and _P_ ˜ _t_ using some descriptive statistics (see SubSection 3.2.2) and a graphical tool that will be described in the following. As mentioned above, we expect a prevalence of regime _r_ = _N_ in defense phases and a corresponding prevalence of _r_ = _L_ in offense phases. This conjecture can be easily verified by means of contingency tables, but we are not interested in this almost obvious result. We aim to identify departures from this evidence by plotting some kernel functions Φ<sup>(</sup> _p_<sup>_r_)(</sup><sup>_t_) and comparing their pattern to the</sup> presence of a specific player or a lineup on the court. These kernel functions are defined as 



where _ϕ_ (·) is a Nadaraya-Watson kernel regression (Nadaraya 1964; Watson 1964), estimated with a Gaussian kernel and a bandwidth allowing to take into account a proper time lag (e.g. the average duration of a game phase), computed using only the times<sup>˜</sup> _t_ when the selected game phase _p_ was occurring. By construction, Φ<sup>(</sup> _p_<sup>_r_)(</sup><sup>_t_) is a</sup> function of time _t_ , _t ∈_ R _∩_ [0, _T_<sup>˜</sup> ], so its values can be computed also for time instants when observations are not available. This makes it possible³ to plot the functions Φ<sup>(</sup> _O_<sup>_r_)(</sup><sup>_t_)andΦ(</sup> _D_<sup>_r_)(</sup><sup>_t_)inthesameframe.Foragiven</sup> regime _r_ , the plot of Φ<sup>(</sup> _O_<sup>_r_)(</sup><sup>_t_)andΦ(</sup> _D_<sup>_r_)(</sup><sup>_t_)singlesoutgame</sup> 

Let _P_ ˜ _t_ be the categorical variable denoting the game phase, with categories _p_ = _O_ , _D_ , _Tr_ (offense, defense and transition, respectively), described in SubSection 2.2. In step 2 we investigate the connections between the regimes 

> **3** In step 3, it will also allows to perform a realignment of times to those of the variables denoting the scored points process (<sup>¯</sup> _t_ = 1, 2, .., _T_<sup>¯</sup> , see SubSection 2.2). 

R. Metulini et al.: Dynamic pattern of surface area in basketball | **123** 

tranches with different ways of playing with respect to the surface area. At this stage, a comparison analysis can be performed in order to inspect the relations among regimes and some specific player or a whole lineup, by highlighting, using visual tools, the portions of time when the player or the lineup was on the court. 

#### **3.2.2 Data analysis** 

To study the pattern of the estimated regimes conditionally to the categorical variable _P_ ˜ _t_ , we first compute some descriptive statistics for the three case studies CS1, CS2 and CS3. We assign each observation at time<sup>˜</sup> _t_ to regime _r_ if _ξ_ ˜ _t_<sup>(</sup><sup>_r_)</sup> _>_ 0.5. In doing so, we generate the dichotomous variable _R_<sup>^</sup> ˜ _t_ that is the estimate of the latent state _R_ ˜ _t_ . 

In CS1, we have _R_<sup>^</sup> ˜ _t_ = _N_ for 52.1% of observations (and, of course, _R_<sup>^</sup> ˜ _t_ = _L_ for the remaining 47.9%). In addition, we find that 82.4% of observations in defensive game phases correspond to regime _r_ = _N_ , while 77.3% of observations in offensive game phases correspond to regime _r_ = _L_ . 

In CS2, _R_<sup>^</sup> ˜ _t_ = _N_ for 56.8% of observations, 83.0% of observations in defensive game phases correspond to regime _r_ = _N_ , while 63.7% of observations in offensive game phases correspond to regime _r_ = _L_ . 

In CS3, _R_<sup>^</sup> ˜ _t_ = _N_ for 54.2% of observations, 79.1% of observations in defensive game phases correspond to regime _r_ = _N_ , while 66.2% of observations in offensive game phases correspond to regime _r_ = _L_ . 

We measure the association between _R_<sup>^</sup> ˜ _t_ and _P_ ˜ _t_ by means of the normalized association index 



where _X_<sup>2</sup> is the usual Pearson index, _n_ is the number of observations and _k_ the minimum between the number of rows and columns in the bivariate table. 

The existence of a fairly strong association ( _C_ = 56.22% for CS1, _C_ = 45.47% for CS2 and _C_ = 43.95% for CS3) between regimes and game phases is expected from both (coaching) technical considerations and the above cited summary statistics of _A_ ˜ _t|P_ ˜ _t_ = _D_ and _A_ ˜ _t|P_ ˜ _t_ = _O_ . 

More interestingly, we may extend the focus to players. Tables 2–4 report the contingency tables between estimated regimes and players on the court, separately for defensive and offensive phases, for CS1, CS2 and CS3. Tables 2–4 consider only players who played for at least 5 min. 

**Table 2:** Frequency distributions of _R_<sup>^</sup> ˜ _t_ conditional to _P_ ˜ _t_ and player, for offensive (A) and defensive (B) phases. Case study CS1. 

||**A Ofensiv**|**e phases**|**B Defensiv**|**e phases**|
|---|---|---|---|---|
|**Estimated regime **<sup>**^**</sup>**_R_˜****_t_**|**Bench**|**Court**|**Bench**|**Court**|
|Player 1 (_p_1)|||||
|_N_|0.303|0.207|0.884|0.809|
|_L_|0.697|0.793|0.116|0.191|
|Player 2 (_p_2)|||||
|_N_|0.194|0.285|0.817|0.833|
|_L_|0.806|0.715|0.183|0.167|
|Player 3 (_p_3)|||||
|_N_|0.273|0.220|0.799|0.832|
|_L_|0.727|0.780|0.201|0.168|
|Player 4 (_p_4)|||||
|_N_|0.291|0.190|0.847|0.804|
|_L_|0.709|0.810|0.153|0.196|
|Player 5 (_p_5)|||||
|_N_|0.195|0.287|0.801|0.852|
|_L_|0.805|0.713|0.199|0.148|
|Player 6 (_p_6)|||||
|_N_|0.283|0.208|0.844|0.814|
|_L_|0.717|0.792|0.155|0.186|
|Player 7 (_p_7)|||||
|_N_|0.200|0.292|0.818|0.837|
|_L_|0.800|0.708|0.182|0.163|
|Player 8 (_p_8)|||||
|_N_|0.199|0.260|0.793|0.847|
|_L_|0.801|0.740|0.207|0.153|
|Player 10 (_p_10)|||||
|_N_|0.251|0.192|0.819|0.833|
|_L_|0.749|0.808|0.181|0.167|



As suggested in SubSection 3.2.1, the dependence among regimes and lineups/players on the court can also be inspected by means of a graphical analysis. For the 2 most frequent lineups and the 9 selected players of CS1, Figures 1 and 2 show the functions Φ<sup>(</sup> _D_<sup>_L_)(</sup><sup>_t_)(blue)and</sup> Φ<sup>(</sup> _O_<sup>_L_)(</sup><sup>_t_) (red), defined in formula (7). Grey areas identify the</sup> moments where the lineup or the player was on the court. For the sake of brevity, we do not report the corresponding graphs plotted for CS2 and CS3. 

### **3.3 Step 3: relationship between the regimes and the points scored** 

#### **3.3.1 Methods** 

Let _SP_ ¯<sup>team</sup> _t_ and _SP_ ¯<sup>opp</sup> _t_ be the points scored (0, 1, 2, 3, · · · ) by the team and the opponent, respectively, in the time interval (<sup>¯</sup> _t −_ 1,<sup>¯</sup> _t_ ], where, in general, the times<sup>¯</sup> _t_ = 1, 2, · · · , _T_<sup>¯</sup> 

**124** | R. Metulini et al.: Dynamic pattern of surface area in basketball 

**Table 3:** Frequency distributions of _R_<sup>^</sup> ˜ _t_ conditional to _P_ ˜ _t_ and player, for offensive (A) and defensive (B) phases. 

**Table 4:** Frequency distributions of _R_<sup>^</sup> ˜ _t_ conditional to _P_ ˜ _t_ and player, for offensive (A) and defensive (B) phases. 

||**A Ofensiv**|**e phases**|**B Defensiv**|**e phases**||**A Ofensiv**|**e phases**|**B Defensiv**|**e phases**|
|---|---|---|---|---|---|---|---|---|---|
|**Estimated regime **<sup>**^**</sup>**_R_˜****_t_**|**Bench**|**Court**|**Bench**|**Court**|**Estimated regime **<sup>**^**</sup>**_R_˜****_t_**|**Bench**|**Court**|**Bench**|**Court**|
|Player 1 (_p_1)|||||Player 1 (_p_1)|||||
|_N_|0.438|0.360|0.917|0.824|_N_|0.378|0.312|0.806|0.782|
|_L_|0.562|0.640|0.083|0.176|_L_|0.622|0.688|0.194|0.218|
|Player 2 (_p_2)|||||Player 2 (_p_2)|||||
|_N_|0.328|0.379|0.854|0.819|_N_|0.311|0.366|0.820|0.760|
|_L_|0.672|0.621|0.146|0.181|_L_|0.689|0.634|0.180|0.240|
|Player 4 (_p_4)|||||Player 3 (_p_3)|||||
|_N_|0.414|0.312|0.810|0.856|_N_|0.311|0.389|0.770|0.838|
|_L_|0.586|0.688|0.190|0.144|_L_|0.689|0.611|0.230|0.162|
|Player 5 (_p_5)|||||Player 5 (_p_5)|||||
|_N_|0.283|0.373|0.865|0.825|_N_|0.406|0.312|0.801|0.788|
|_L_|0.717|0.627|0.135|0.175|_L_|0.594|0.688|0.199|0.212|
|Player 6 (_p_6)|||||Player 6 (_p_6)|||||
|_N_|0.434|0.339|0.804|0.838|_N_|0.341|0.334|0.779|0.807|
|_L_|0.566|0.661|0.196|0.162|_L_|0.659|0.666|0.221|0.194|
|Player 7 (_p_7)|||||Player 7 (_p_7)|||||
|_N_|0.360|0.383|0.830|0.830|_N_|0.315|0.386|0.779|0.812|
|_L_|0.640|0.617|0.170|0.170|_L_|0.685|0.614|0.221|0.188|
|Player 8 (_p_8)|||||Player 8 (_p_8)|||||
|_N_|0.313|0.416|0.849|0.813|_N_|0.379|0.313|0.786|0.793|
|_L_|0.687|0.584|0.151|0.187|_L_|0.621|0.687|0.214|0.207|
|Player 9 (_p_9)|||||Player 9 (_p_9)|||||
|_N_|0.375|0.289|0.822|0.882|_N_|0.334|0.340|0.825|0.764|
|_L_|0.625|0.711|0.178|0.118|_L_|0.666|0.660|0.175|0.236|
|Player 10 (_p_10)|||||Player 10 (_p_10)|||||
|_N_|0.351|0.378|0.824|0.837|_N_|0.339|0.337|0.769|0.801|
|_L_|0.649|0.622|0.176|0.163|_L_|0.661|0.663|0.231|0.199|
|Case study CS2.|||||Case study CS3.|||||



are different from the observation times<sup>˜</sup> _t_ = 1, 2, · · · , _T_<sup>˜</sup> of the process _{A_ ˜ _t}_ . In fact, in order to obtain meaningful values for the variables _SP_ ¯<sup>team</sup> _t_ and _SP_ ¯<sup>opp</sup> _t_ , the interval between two consecutive times<sup>¯</sup> _t −_ 1 and<sup>¯</sup> _t_ has to be in the order of at least 1 min. So, we here need to solve the problem of time misalignment. For a given regime _r_ , we denote with **Y** ¯<sup>team,</sup><sup>_r_</sup> and **Y** ¯<sup>opp,</sup><sup>_r_</sup> the vectors _t t_ 



where _∇_ denotes the first-difference operator, _∇_ Φ<sup>(</sup> *<sup>_r_)(¯</sup><sup>_t_) =</sup> Φ<sup>(</sup> *<sup>_r_)(¯</sup><sup>_t_)</sup><sup>_−_Φ(</sup> *<sup>_r_)(¯</sup><sup>_t−_1),necessarytofilterouttheone-lag</sup> dependence induced by construction by the Markov property assumed in step 1 to regulate the regime switching. Note that the realignment of the times related to the regime dynamics (<sup>˜</sup> _t_ ) and those related to the recording of scored 



<!-- Start of picture text -->
Lineup 1<br>0.8<br>0.4<br>0.0<br>0 10 20 30 40<br>Lineup 2<br>0.8<br>0.4<br>0.0<br>0 10 20 30 40<br><!-- End of picture text -->

**Figure 1:** Lineups on the court (grey) against Nadaraya-Watson kernel functions. The charts display, in y-axis, functions Φ<sup>(</sup> _D_<sup>_L_)(</sup><sup>_t_) (in blue) and Φ(</sup> _O_<sup>_L_)(</sup><sup>_t_) (in</sup> red), in x-axis, Time (in min). 

R. Metulini et al.: Dynamic pattern of surface area in basketball | **125** 



<!-- Start of picture text -->
Player 1 Player 2 Player 3<br>0 10 20 30 40 0 10 20 30 40 0 10 20 30 40<br>Player 4 Player 5 Player 6<br>0 10 20 30 40 0 10 20 30 40 0 10 20 30 40<br>Player 7 Player 8 Player 10<br>0 10 20 30 40 0 10 20 30 40 0 10 20 30 40<br>0.6 0.6 0.6<br>0.0 0.0 0.0<br>0.6 0.6 0.6<br>0.0 0.0 0.0<br>0.6 0.6 0.6<br>0.0 0.0 0.0<br><!-- End of picture text -->

**Figure 2:** Players on the court (grey) against Nadaraya-Watson kernel functions. The charts display, in y-axis, functions Φ<sup>(</sup> _D_<sup>_L_)(</sup><sup>_t_) (in blue) and Φ(</sup> _O_<sup>_L_)(</sup><sup>_t_) (in red), in-axis, Time (in min).</sup> 

points (<sup>¯</sup> _t_ ) is solved by using the functions Φ<sup>(</sup> _p_<sup>_r_)(</sup><sup>_t_) defined</sup> in (7), that can be computed for all _t ∈_ R _∩_ [0, _T_<sup>˜</sup> ] and, in this case, are evaluated at the times<sup>¯</sup> _t_ = 1, 2, · · · , _T_<sup>¯</sup> . In order to investigate the relationship between regimes and scored points, we assume a VAR model (Sims 1980) for the processes _{_ **Y** ¯<sup>team,</sup> _t_<sup>_r_</sup> _}_ and _{_ **Y** ¯<sup>opp,</sup> _t_<sup>_r_</sup> _}_ : 



and 



where **_η_** 0 and **_ω_** 0 are 2 _×_ 1 vectors of the intercepts to be estimated, **_η_** 1′ ... **_η_** _q_ ′ and **_ω_** 1′ ... **_ω_** _q_ ′ are 2 _×_ 2 matrices of the coefficients to be estimated, while **_ε_** ¯<sup>team,</sup> _t_<sup>_r_</sup> and **_ε_** ¯<sup>opp,</sup> _t_<sup>_r_</sup> are the usual innovation processes.⁴ 

From here onwards, we will consider time series observed at the end of each minute of the game, i.e. at times<sup>¯</sup> _t_ = 1, 2, · · · , 40. 

To choose the orders of the VAR models, we resort to the Bayesian Information Criterion (BIC), that suggests to set _q_ = 1 and _s_ = 1 in both CS1 and CS3. For CS2, instead, we should opt for _q_ = 3 and _s_ = 2. However, the differences between the BIC values corresponding to the two models of order 1 and the optimal ones are less than 0.13 and 0.45, respectively. According to Kass and Raftery (1995), this denotes a negligible evidence against the models with higher BIC values. For this reason, in order to ensure comparability of results, we set _q_ = 1 and _s_ = 1 also for CS2. 

So, we fit models (9) and (10) in the form 



#### **3.3.2 Data analysis** 

and 

As described in SubSection 3.3.1, we estimate the two VAR models of equations (9) and (10). 

**4** The use of count data (the scored points) within a VAR model could be criticized from a formal point of view. Brandt and Sandler (2012) propose a bayesian Poisson VAR model (see the same reference for a literature review on this topic) to treat count data in a multivariate autoregressive context. Nevertheless, we point out that this is a case of mixed data: count data and numerical variables. In addition, in the theory behind VAR model there are not strict requirements about the nature of the variables to be used. 



where, as defined in (8), the vectors **Y** ¯<sup>team,</sup> _t_<sup>_L_</sup> and **Y** ¯<sup>opp,</sup> _t_<sup>_N_</sup> contain the scored points and the first differences of the corresponding functions Φ. From a methodological point of view, this choice is justified by the necessity to filter out the one-lag dependence induced by the Markov property in the MSM, as mentioned before. In practice, this necessity is confirmed by the Augmented Dickey Fuller (ADF) test for unit roots, that results, for CS1, _−_ 1.468 and 

**126** | R. Metulini et al.: Dynamic pattern of surface area in basketball 

_−_ 0.558 for Φ<sup>(</sup> _O_<sup>_L_)(</sup><sup>_t_) and Φ(</sup> _D_<sup>_N_)(</sup><sup>_t_), respectively (the threshold</sup> for _α_ = 0.05 is _−_ 1.95, so the null hypothesis of the presence of a unit root cannot be rejected). Analogous results hold for CS2 ( _−_ 1.936 and _−_ 1.770 for Φ<sup>(</sup> _O_<sup>_L_)(</sup><sup>_t_)andΦ(</sup> _D_<sup>_N_)(</sup><sup>_t_),</sup> respectively) and CS3 ( _−_ 1.624 and _−_ 1.662 for Φ<sup>(</sup> _O_<sup>_L_)(</sup><sup>_t_)and</sup> Φ<sup>(</sup><sup>_N_)</sup> _D_<sup>(</sup><sup>_t_), respectively).</sup> 

Estimation results of the three case studies are summarized in Table 5 and 6 for models (11) and (12) respectively. 

**Table 5:** VAR model **Y**<sup>team,</sup> ¯ _t_<sup>_L_</sup> = **_η_** 0 + **_η_** 1′ **Y**<sup>team,</sup> ¯ _t−_ 1<sup>_L_</sup> + **_ε_**<sup>team,</sup> ¯ _t_<sup>_L_</sup> . 

|**CS1**|**CS2**|**CS3**|
|---|---|---|
|**Coef (S.e.)**|**Coef (S.e.)**|**Coef (S.e.)**|
|Results for equation_SP_<sup>team</sup><br>¯_t_<br>:|||
|_SP_<sup>team</sup><br>¯_t−_1<br>_−_0.032|_−_0.281|0.043|
|(0.159)<br>|(0.157)|(0.169)|
|_∇_Φ<sup>(</sup><sup>_L_)</sup><br>_O_ <sup>(¯</sup><sup>_t −_1)</sup><br>7.951|4.323|7.394|
|(4.570)|(3.230)|(3.649)|
|Intercept<br>2.194***|2.252***|1.649***|
|(0.433)|(0.416)|(0.402)|
|Results for equation_∇_Φ<sup>(</sup><sup>_L_)</sup><br>_O_ <sup>(¯</sup><sup>_t_):</sup>|||
|_SP_<sup>team</sup><br>¯_t−_1<br>_−_0.005|0.004|_−_0.008|
|(0.006)<br>|(0.008)|(0.008)|
|_∇_Φ<sup>(</sup><sup>_r_)</sup><br>_O_ <sup>(¯</sup><sup>_t −_1)</sup><br>0.258|0.235|0.073|
|(0.162)|(0.164)|(0.177)|
|Intercept<br>0.012|_−_0.012|0.019|
|(0.015)|(0.021)|(0.020)|



Signif. codes: · _p <_ 0.1, * _p <_ 0.05, ** _p <_ 0.01, *** _p <_ 0.001. 

**Table 6:** VAR model **Y**<sup>opp,</sup> ¯ _t_<sup>_N_</sup> = **_ω_** 0 + **_ω_** 1′ **Y**<sup>opp,</sup> ¯ _t−_ 1<sup>_N_</sup> + **_ε_**<sup>opp,</sup> ¯ _t_<sup>_N_</sup> . 

|**CS1**|**CS2**|**CS3**|
|---|---|---|
|**Coef (S.e.)**|**Coef (S.e.)**|**Coef (S.e.)**|
|Results for equation_SP_<sup>opp</sup><br>¯_t_<br>:|||
|_SP_<sup>opp</sup><br>¯_t−_1<br>_−_0.119|0.054|0.029|
|(0.170)<br>|(0.159)|(0.162)|
|_∇_Φ<sup>(</sup><sup>_N_)</sup><br>_D_ <sup>(¯</sup><sup>_t −_1)</sup><br>1.610|7.934|_−_3.590|
|(4.322)|(5.285)|(3.688)|
|Intercept<br>2.436***|1.740***|1.586***|
|(0.448)|(0.400)|(0.357)|
|Results for equation_∇_Φ<sup>(</sup><sup>_N_)</sup><br>_D_ <sup>(¯</sup><sup>_t_):</sup>|||
|_SP_<sup>opp</sup><br>¯_t−_1<br>_−_0.016*|_−_0.012*|_−_0.011|
|(0.006)<br>|(0.005)|(0.007)|
|_∇_Φ<sup>(</sup><sup>_N_)</sup><br>_D_ <sup>(¯</sup><sup>_t −_1)</sup><br>0.247|0.180|_−_0.038|
|(0.156)|(0.169)|(0.161)|
|Intercept<br>0.012|_−_0.012|0.019|
|(0.016)|(0.013)|(0.016)|



Signif. codes: · _p <_ 0.1, * _p <_ 0.05, ** _p <_ 0.01, *** _p <_ 0.001. 

## **4 Discussion** 

The idea that the surface area switches from narrow to large when moving from defense to offense is supported both by team sports coaching experience and statistical evidence. In fact, the median values of the surface areas are found to be appreciably different in defensive and offensive phases in all the analysed case studies (in the range of m<sup>2</sup> 22–25 and 44–52, for defense and offense, respectively). The three-step procedure proposed in this paper is designed to detect departures from this basic evidence and to relate these departures to some game variables, such as the players on the court or the points scored by the team and the opponent. 

In the first step we described the dynamics of narrow and large surface areas in terms of a stochastic process switching between two regimes according to a latent Markov process. In all the tree case studies, a significant presence of two regimes has been detected, characterized by average surface areas in the range of about m<sup>2</sup> 21.7–24.7 and 55.7–63.3 for regime _r_ = _N_ (narrow) and _r_ = _L_ (large), respectively (Table 1). In all the cases, the regimes have a fast switching: they last on average between 7 and 8 s, which suggests that the association of the narrow (large) regime to defense (offense) phases cannot be considered as a perfect matching and stimulates a deeper investigation on the occurrence of regime _N_ and _L_ during offense and defense phases, respectively. 

In the second step, we carried out a deeper investigation on the dynamics of the two regimes detected in the first step. To start, we inspected contingency tables of regimes and game phases (offense or defense) and of regimes and players, separately for offense and defense. In all the case studies, the association between regimes and game phase is quite strong (normalized association index between 43.95% and 56.22%), but not huge. This confirms both the initial evidence of an association between narrow (large) surface areas and defense (offense) and, at the same time, the necessity of understanding the dynamics and the effects of departures from it, as the matching is not perfect. With reference to players (Tables 2–4), interesting remarks can be drawn with respect to some selected ones. For example, in CS1, during offensive phases (box A), when player _p_ 1 is on the bench, the relative frequency of regime _N_ is 0.303. When the same player is on the court, the same relative frequency decreases to 0.207. 

This means that, on average, the team tends to play more spread in offense when player _p_ 1 is on the court. The opposite holds with player _p_ 2: on average the team tends to narrow its offensive surface area when he is on the court, with the relative frequency of regime _N_ moving 

R. Metulini et al.: Dynamic pattern of surface area in basketball | **127** 

from 0.194 to 0.285 when he is on the bench or on the court, respectively. 

Similar remarks can be made with reference to other players and/or defensive phases (box B). This allows to describe the effect of each player on the game played by the team. We are not allowed to know whether a specific effect due to the presence of a player positively or negatively affects the team performance, but this can anyway be useful for the coach, who can (for example) measure the extent to which his guidelines with reference to surface areas are complied with. 

After the inspection of contingency tables, we defined the smoothed functions Φ<sup>(</sup> _D_<sup>_L_)(</sup><sup>_t_)andΦ(</sup> _O_<sup>_L_)(</sup><sup>_t_),thatallowa</sup> useful graphical inspection of the regimes patterns during offense and defense. Also this tool can help coaches in analysing the game played by the team. In fact, fluctuations in the functions Φ<sup>(</sup> _D_<sup>_L_)(</sup><sup>_t_)andΦ(</sup> _O_<sup>_L_)(</sup><sup>_t_)shedlighton</sup> game portions with different features from the point of view of the surface area. As an example of their possible use, consider the two functions computed for CS1 and plotted in Figures 1 and 2, with superimposed grey areas corresponding to the presence on the court of a specific lineup or player. Φ<sup>(</sup> _D_<sup>_L_)(</sup><sup>_t_)isrepresentedwithablueline</sup> and Φ<sup>(</sup> _O_<sup>_L_)(</sup><sup>_t_) with a red one. We may notice that the offen-</sup> sive play until the first half of the second quarter (around minute 15) seems to be appreciably different from what follows, as the kernel smoothed probabilities Φ<sup>(</sup> _O_<sup>_L_)(</sup><sup>_t_)of</sup> regime _L_ are considerably lower in the first 15 min than in the rest of the match. In addition, something happened in the offensive play around minute 30, as the function Φ<sup>(</sup> _O_<sup>_L_)(</sup><sup>_t_) clearly falls. Similar remarks can be done with ref-</sup> erence to defensive phases: a peak is evident in the function Φ<sup>(</sup> _D_<sup>_L_)(</sup><sup>_t_)inthemiddleofthematch,aroundminute</sup> 20. These observed fluctuations can be related to the presence of a specific lineup on the court (Figure 1) or a certain player (Figure 2). 

As regards the lineups, for example, we notice that the fall of Φ<sup>(</sup> _O_<sup>_L_)(</sup><sup>_t_) around minute 30 occurred when the lineup</sup> 2 was on the court, and the same lineup is also related to another game period with low values of Φ<sup>(</sup> _O_<sup>_L_)(</sup><sup>_t_), at the end</sup> of the first quarter, and periods with increased values of Φ<sup>(</sup><sup>_L_)</sup> _D_<sup>(</sup><sup>_t_). Analogous remarks can be done with reference to</sup> single players. Again, at this step, we are not able to assess whether the observed fluctuations have a positive or negative impact on the overall team performance, that was the aim of step 3. Anyway the proposed charts allow a deeper knowledge of the surface area dynamics during the match and with reference to the lineups and players. In addition further relevant game variables (e.g. the implementation of playbooks, the coach’s judgments on the technical performance during the match, ...) could be added to 

**Table 7:** Number of attempted and made shots. 

|**2-point**|**3-point**|**Free throws**|
|---|---|---|
|Shots of the team (made/attem|pted)||
|CS1<br>14/31|13/23|17/19|
|CS2<br>12/28|11/34|11/11|
|CS3<br>15/34|8/21|15/20|
|Shots of the opponent (made/a|ttempted)||
|CS1<br>24/37|7/23|18/22|
|CS2<br>27/46|3/16|13/14|
|CS3<br>16/37|11/22|3/7|



the graphs and compared to the observed fluctuations of functions Φ<sup>(</sup> _D_<sup>_L_)(</sup><sup>_t_) and Φ(</sup> _O_<sup>_L_)(</sup><sup>_t_).</sup> 

Finally, the third step aimed at finding evidence about the effect of regimes’ dynamics on the points scored by the team and the opponent. While the evidence found in the first two steps was basically common to all the three analysed case studies, the features that emerged at this point seem to be genuinely match-specific. On some level, this can be justified in view of the different tactics decided by coaches or the different ways of playing determined by the interaction of the two specific teams involved in the match. One important information that will allow to give some insights for a possible interpretation of these matchspecific results is given by the number of attempted and made shots (Table 7) in the three case studies. 

Besides intercepts, the parameters of both models (11) and (12) tend to have low significance (Tables 5 and 6, respectively). With regard to model (11), we found a (weakly significant, _α_ = 0.1) evidence for an effect of variable _∇_ Φ<sup>(</sup> _O_<sup>_L_)(¯</sup><sup>_t−_1)on</sup><sup>_SP_</sup> ¯<sup>team</sup> _t_ in CS1 and CS3. The coefficients’ estimates (7.951 and 7.394) suggest that an increased probability of _r_ = _L_ in offense has a high positive effect on the points made by the team. In CS2, such influence of the surface area on the scored points was not detected. Instead, we found a negative correlation between the points scored during 1 min on the points scored in the following one, which highlights a certain variability in the game under this point of view. Looking at Table 7, we notice that the team of CS2 has resorted to 3-point shots more often that the other two (and with a lower scoring percentage). This could explain the variability of the scored points in successive times, as points gained with 3-point shots are more volatile. This variability may have masked the possible relationship between surface area and scored points, or the absence of this relationship may be due right to the different tactic, more based on 3-point shots. 

In model (12) we found a significant ( _α_ = 0.05) effect of variable _SP_ ¯<sup>opp</sup> _t−_ 1<sup>on</sup><sup>_∇_Φ(</sup> _D_<sup>_N_)(¯</sup><sup>_t_)forCS1andCS2.The</sup> 

**128** | R. Metulini et al.: Dynamic pattern of surface area in basketball 

coefficients’ estimates ( _−_ 0.016 and _−_ 0.012) suggest a weak negative effect of the points made by the opponent on the variation of probability to be in regime _r_ = _N_ in defense. So, when _SP_ ¯<sup>opp</sup> _t−_ 1<sup>ishigh,theprobabilitytobeinregime</sup> _r_ = _N_ at time<sup>¯</sup> _t_ decreases: a more efficient game of the opponent (in terms of scored points) seems to force the team to keep the defense spread. Such relationship was not detected in CS3. Looking at Table 7 we observe a substantial difference between cases CS1/CS2 and case CS3 from the point of view of the points scored by the opponent: the teams of CS1 and CS2 have faced opponents with high scoring percentages in 2-point shots (65% and 59%) and low scoring percentages in 3-point shots (30% and 19%), while the opposite has happened to the team of CS3 (43% in 2-point shots and 50% in 3-point shots). This may explain the reason for a different tactical reaction to the points scored by the opponent. 

## **5 Concluding remarks** 

The analysis of players’ trajectories in team sports, which nowadays is made possible by the increasing Information Technology potentialities, could bring important information to analysts, experts and coaches, offering both interpretable analysis tools and concrete suggestions about the way to improve performance. We contribute to this growing area of research by adopting a statistical modelling approach to study relationships among surface areas and team performance in basketball. To the best of our knowledge, Markov Switching models are used here for the first time in basketball studies. 

Using sensor data concerned with players’ movements on the court, we analysed the surface areas (measured by the area of convex hulls), since the area covered by the team on the court is often considered, by experts, an important perspective on the game. We proposed a threestep procedure. In the first step we detected structural changes in the space among players by means of a Markov Switching model. After a deep analysis of these structural changes with respect to game phases, players and lineups on the court (step 2), in step 3 we studied, by means of Vector Autoregressive models, the causal relation between surface area and team performance. 

The main findings of the presented case study can be summarized as follows: we found (i) robust evidences of the presence of structural changes, by estimating two well-separated regimes that relate, respectively, to large and narrow convex hull areas; (ii) some players and some combination of players on the court that show 

different probabilities to be in the two regimes; (iii) some match-specific causal relationships, which have to be interpreted with reference to the specific characteristics of each match. 

These results could be used by basketball coaches and experts as they relate with tactics, specifically with the choice of game strategies, players and lineups. Further developments could be carried out following three directions: (i) to jointly analyse the trajectories of the players of both the team and the opponent; (ii) to introduce the ball trajectory and measure its role on the relationship between surface area and performance; (iii) to include the dimension of game schemes and coaches’ tactics in the context of a three-dimensional analysis covering game strategy, players’ movements and team performance. 

**Acknowledgments:** The authors are grateful to the anonymous reviewers for their valuable comments, which greatly improved the paper, and also thank MYagonism ( `www.myagonism.com` ) for having supplied the data. A special thanks goes to Raffaele Imbrogno (“Foro Italico” University, Roma IV), Paolo Raineri (MYagonism) for fruitful discussions, and to Tullio Facchinetti (University of Pavia) for the help with data manipulation. We also thank Giuseppe Arbia (Catholic University of the Sacred Heart) and Marcello Chiodi (University of Palermo) for useful comments at the SIS 2017 conference. Research carried out in collaboration with the Big & Open Data Innovation Laboratory (BODaI-Lab), University of Brescia (project nr. 03-2016, title “Big Data Analytics in Sports”, bodai.unibs.it/bdsports), granted by Fondazione Cariplo and Regione Lombardia. 

## **References** 

- Annis, D. H. 2006. “Optimal End-Game Strategy in Basketball.” _Journal of Quantitative Analysis in Sports_ 2(2):1. 

- Araújo, D. and K. Davids. 2016. “Team Synergies in Sport: Theory and Measures.” _Frontiers in Psychology_ 7:1449. 

- Araújo, D., K. Davids, and R. Hristovski. 2006. “The Ecological Dynamics of Decision Making in Sport.” _Psychology of Sport and Exercise_ 7(6):653–676. 

- Araújo, D., K. W. Davids, J. Y. Chow, P. Passos, and M. Raab. 2009. “The Development of Decision Making Skill in Sport: An Ecological Dynamics Perspective.” in _Perspectives on Cognition and Action in Sport_ . Suffolk, USA: Nova Science Publishers, Inc., pp. 157–169. 

- Baum, L. E., T. Petrie, G. Soules, and N. Weiss. 1970. “A Maximization Technique Occurring in the Statistical Analysis of Probabilistic Functions of Markov Chains.” _The Annals of Mathematical Statistics_ 41(1):164–171. 

R. Metulini et al.: Dynamic pattern of surface area in basketball | **129** 

- Brandt, P. T. and T. Sandler. 2012. “A Bayesian Poisson Vector Autoregression Model.” _Political Analysis_ 20(3):292–315. 

- Brown, M. and J. Sokol. 2010. “An Improved LRMC Method for NCAA Basketball Prediction.” _Journal of Quantitative Analysis in Sports_ 6(3):1–23. 

- Cooper, W. W., J. L. Ruiz, and I. Sirvent. 2009. “Selecting NonZero Weights to Evaluate Effectiveness of Basketball Players with DEA.” _European Journal of Operational Research_ 195(2):563–574. 

- Crocker, P. R. and T. R. Graham. 1995. “Coping by Competitive Athletes with Performance Stress: Gender Differences and Relationships with Affect.” _The Sport Psychologist_ 9(3):325–338. 

- Deshpande, S. K. and S. T. Jensen. 2016. “Estimating an NBA Player’s Impact on his Team’s Chances of Winning.” _Journal of Quantitative Analysis in Sports_ 12(2):51–72. 

- Duarte, R., D. Araújo, V. Correia, K. Davids, P. Marques, and M. J. Richardson. 2013. “Competing Together: Assessing the Dynamics of Team–Team and Player–Team Synchrony in Professional Association Football.” _Human Movement Science_ 32(4):555–566. 

- Fearnhead, P. and B. M. Taylor. 2011. “On Estimating the Ability of NBA Players.” _Journal of Quantitative Analysis in Sports_ 7(3):1–18. 

- Fewell, J. H., D. Armbruster, J. Ingraham, A. Petersen, and J. S. Waters. 2012. “Basketball Teams as Strategic Networks.” _PLoS One_ 7(11): e47445. 

- Fonseca, S., J. Milho, B. Travassos, and D. Araújo. 2012. “Spatial Dynamics of Team Sports Exposed by Voronoi Diagrams.” _Human Movement Science_ 31(6):1652–1659. 

- Frencken, W., K. Lemmink, N. Delleman, and C. Visscher. 2011. “Oscillations of Centroid Position and Surface Area of Soccer Teams in Small-Sided Games.” _European Journal of Sport Science_ 11(4):215–223. 

- Goldfarb, D. 2014. 1‘An Application of Topological Data Analysis to Hockey Analytics.” _arXiv preprint arXiv:1409.7635_ . 

- Greihaine, J.-F., P. Godbout, and Z. Zerai. 2011. “How the “Rapport de Forces” Evolves in a Soccer Match: The Dynamics of Collective Decisions in a Complex System.” _Revista de Psicología del Deporte_ 20(2):747–764. 

- Gudmundsson, J. and M. Horton. 2016. “Spatio-Temporal Analysis of Team Sports–A Survey.” _arXiv preprint arXiv:1602.06994_ . 

- Gupta, A. A. 2015. “A New Approach to Bracket Prediction in the NCAA Men’s Basketball Tournament Based on a DualProportion Likelihood.” _Journal of Quantitative Analysis in Sports_ 11(1):53–67. 

- Hamilton, J. D. 1989. “A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle.” _Econometrica: Journal of the Econometric Society_ 57(2):357–384. 

- Hamilton, J. D. 2010. “Regime Switching Models.” Pp. 202–209 in _Macroeconometrics and Time Series Analysis_ . London: Palgrave Macmillan. 

- Kass, R. E. and A. E. Raftery. 1995. “Bayes Factors.” _Journal of the American Statistical Association_ 90(430):773–795. 

- Kim, C.-J. 1994. “Dynamic Linear Models with Markov-Switching.” _Journal of Econometrics_ 60(1–2):1–22. 

- Kowshik, G., Y.-H. Chang, and R. Maheswaran. 2012. _Visualization of Event-Based Motion-Tracking Sports Data_ . Technical report, Technical report, University of Southern California. 

- Kubatko, J., D. Oliver, K. Pelton, and D. T. Rosenbaum. 2007. “A Starting Point for Analyzing Basketball Statistics.” _Journal of Quantitative Analysis in Sports_ 3(3):1–22. 

- Lamas, L., D. D. R. Junior, F. Santana, E. Rostaiser, L. Negretti, and C. Ugrinowitsch. 2011. “Space Creation Dynamics in Basketball Offence: Validation and Evaluation of Elite Teams.” _International Journal of Performance Analysis in Sport_ 11(1):71–84. 

- Lindgren, G. 1978. “Markov Regime Models for Mixed Distributions and Switching Regressions.” _Scandinavian Journal of Statistics_ 5(2):81–91. 

- Loeffelholz, B., E. Bednar, and K. W. Bauer. 2009. “Predicting NBA Games using Neural Networks.” _Journal of Quantitative Analysis in Sports_ 5(1):1–15. 

- Lopez, M. J. and G. J. Matthews. 2015. “Building an NCAA Men’s Basketball Predictive Model and Quantifying its Success.” _Journal of Quantitative Analysis in Sports_ 11(1):5–12. 

- Manner, H. 2016. “Modeling and Forecasting the Outcomes of NBA Basketball Games.” _Journal of Quantitative Analysis in Sports_ 12(1):31–41. 

- Metulini, R. 2016. “Spatio-Temporal Movements in Team Sports: A Visualization Approach Using Motion Charts.” _arXiv preprint arXiv:1611.09158_ . 

- Metulini, R. 2017. “Filtering Procedures for Sensor Data in Basketball.” _Statistica & Applicazioni_ 15(2). 

- Metulini, R., M. Manisera, and P. Zuccolotto. 2017a. “Sensor Analytics in Basketball.” _Proceedings of the 6th International Conference on Mathematics in Sport. ISBN 978-88-6938-058-7_ . 

- Metulini, R., M. Manisera, and P. Zuccolotto. 2017b. “Space-Time Analysis of Movements in Basketball Using Sensor Data.” _Statistics and Data Science: New Challenges, New Generations” SIS2017 proceeding. Firenze Uiversity Press. eISBN: 978-88-6453-521-0_ . 

- Moura, F. A., L. E. B. Martins, R. D. O. Anido, R. M. L. De Barros, and S. A. Cunha. 2012. “Quantitative Analysis of Brazilian Football Players’ Organisation on the Pitch.” _Sports Biomechanics_ 11(1):85–96. 

- Nadaraya, E. A. 1964. “On Estimating Regression.” _Theory of Probability & Its Applications_ 9(1):141–142. 

- Ozmen, M. U. 2012. “Foreign Player Quota, Experience and Eflciency of Basketball Players.” _Journal of Quantitative Analysis in Sports_ 8(1):1–18. 

- Page, G. L., G. W. Fellingham, and C. S. Reese. 2007. “Using BoxScores to Determine a Position’s Contribution to Winning Basketball Games.” _Journal of Quantitative Analysis in Sports_ 3(4):1–18. 

- Page, G. L., B. J. Barney, and A. T. McGuire. 2013. “Effect of Position, Usage Rate, and Per Game Minutes Played on NBA Player Production Curves.” _Journal of Quantitative Analysis in Sports_ 9(4):337–345. 

- Passos, P., D. Araújo, and A. Volossovitch. 2016. _Performance Analysis in Team Sports_ . London: Routledge. 

- Passos, P., K. Davids, D. Araújo, N. Paz, J. Minguéns, andJ. Mendes. 2011. “Networks as a Novel Tool for Studying Team Ball Sports as Complex Social Systems.” _Journal of Science and Medicine in Sport_ 14(2):170–176. 

- Perica, A., S. Trninić, and I. Jelaska. 2011. “Introduction into the Game States Analysis System in Basketball.” _Fizička kultura_ 65(2):51–78. 

**130** | R. Metulini et al.: Dynamic pattern of surface area in basketball 

- Perše, M., M. Kristan, S. Kovačič, G. Vučkovič, and J. Perš. 2009. “A Trajectory-Based Analysis of Coordinated Team Activity in a Basketball Game.” _Computer Vision and Image Understanding_ 113(5):612–621. 

- Piette, J., S. Anand, and K. Zhang. 2010. “Scoring and Shooting Abilities of NBA Players.” _Journal of Quantitative Analysis in Sports_ 6(1):1–23. 

- Richardson, M. J., R. L. Garcia, T. D. Frank, M. Gergor, and K. L. Marsh. 2012. “Measuring Group Synchrony: A Cluster-Phase Method for Analyzing Multivariate Movement Time-Series.” _Frontiers in physiology_ 3(405):1–10. 

- Ruiz, F. J. and F. Perez-Cruz. 2015. “A Generative Model for Predicting Outcomes in College Basketball.” _Journal of Quantitative Analysis in Sports_ 11(1):39–52. 

- Sanchez-Espigares, J. A. and A. Lopez-Moreno. 2014. _MSwM: Fitting Markov Switching Models_ . R package version 1.2. URL:https://CRAN.R-project.org/package=MSwM. 

- Sims, C. A. 1980. “Macroeconomics and reality.” _Econometrica: Journal of the Econometric Society_ 48(1):1–48. 

- Stein, M., H. Janetzko, D. Seebacher, A. Jäger, M. Nagel, J. Hölsch, S. Kosub, T. Schreck, D. A. Keim, and M. Grossniklaus. 2017. “How to Make Sense of Team Sport Data: From Acquisition to Data Modeling and Research Aspects.” _Data_ 2(1):2. 

- Therón, R. and L. Casares. 2010. “Visual Analysis of Time-Motion in Basketball Games.” in _International Symposium on Smart Graphics_ . Berlin, Heidelberg: Springer, pp. 196–207. 

- Travassos, B., D. Araújo, K. Davids, P. T. Esteves, and O. Fernandes. 2012. “Improving Passing Actions in Team Sports 

   - by Developing Interpersonal Interactions between Players.” _International Journal of Sports Science & Coaching_ 7(4):677–688. 

- Travassos, B., D. Araújo, R. Duarte, and T. McGarry. 2012. “Spatiotemporal Coordination Behaviors in Futsal (Indoor Football) are Guided by Informational Game Constraints.” _Human Movement Science_ 31(4):932–945. 

- Turvey, M. and R. E. Shaw. 1995. “Toward an Ecological Physics and a Physical Psychology.” _The Science of the Mind: 2001 and Beyond_ , Chapter 11, pp. 144–169. 

- Wasserman, S. and K. Faust. 1994. _Social Network Analysis: Methods and Applications_ , Vol. 8. Cambridge, United Kingdom: Cambridge University Press. 

- Watson, G. S. 1964. “Smooth Regression Analysis.” _Sankhy¯a: The Indian Journal of Statistics, Series A_ 26(4):359–372. 

- West, B. T. 2008. “A Simple and Flexible Rating Method for Predicting Success in the NCAA Basketball Tournament: Updated Results from 2007.” _Journal of Quantitative Analysis in Sports_ 4(2):8. 

- Yuan, L.-H., A. Liu, A. Yeh, A. Kaufman, A. Reece, P. Bull, A. Franks, S. Wang, D. Illushin, and L. Bornn. 2015. “A Mixtureof-Modelers Approach to Forecasting NCAA Tournament Outcomes.” _Journal of Quantitative Analysis in Sports_ 11(1):13–27. 

- Zuccolotto, P., M. Manisera, and M. Sandri. 2017. “Big Data Analytics for Modeling Scoring Probability in Basketball: The Effect of Shooting under High-Pressure Conditions.” _International Journal of Sports Science & Coaching_ (OnLine First). 


