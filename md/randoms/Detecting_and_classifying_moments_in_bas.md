<!-- source: randoms/Detecting_and_classifying_moments_in_bas.pdf -->

Copyright © 2019 

PUBLISHED BY PEARSON 

WWW.PEARSON.COM 

_Giugno 2019 ISBN 9788891915108_ 

# **Detecting and classifying moments in basketball matches using sensor tracked data** 

## **Una procedure per identificare e classificare momenti di gioco in pallacanestro con l’uso di dati sensori.** 

Tullio Facchinetti and Rodolfo Metulini and Paola Zuccolotto 

**Abstract** Data analytics in sports is crucial to evaluate the performance of single players and the whole team. The literature proposes a number of tools for both offence and defence scenarios. Data coming from tracking location of players, in this respect, may be used to enrich the amount of useful information. In basketball, however, actions are interleaved with inactive periods. This paper describes a methodological approach to automatically identify active periods during a game and to classify them as offensive or defensive. The method is based on the application of thresholds to players kinematic parameters, whose values undergo a “tuning” strategy similar to Receiver Operating Characteristic curves, using a “ground truth” extracted from the video of the games. 

**Abstract** La “data analytics” `e cruciale per valutare le prestazioni di singoli giocatori e dei team nello sport. La letteratura accademica ha sviluppato una serie di strumenti per le situazioni di attacco e di difesa. I dati che rilevano la posizione dei giocatori possono essere utilizzati per arricchire la quantita’ di informazioni utili. Nel basket, tuttavia, le azioni sono intervallate da periodi inattivi. In questo lavoro si propone un metodo per identificare i periodi attivi e classificarli come offensivi o difensivi. Il metodo si basa sull’applicazione di soglie sui parametri cinematici dei giocatori, i cui valori vengono sottoposti ad una strategia di “tuning” simile alle curve ROC in cui la “ground truth” viene estratta da un’analisi video. 

**Key words:** Sport Analytics; GPS; Trajectories; Basketball 

#### Tullio Facchinetti 

Department of Industrial, Computer and Biomedical Engineering, University of Pavia, Via Ferrata, 1, 27100 Pavia, e-mail: tullio.facchinetti@unipv.it 

#### Rodolfo Metulini 

Department of Economic and Management, University of Brescia, Contrada Santa Chiara, 50, 25122 Brescia, e-mail: rodolfo.metulini@unibs.it 

Paola Zuccolotto 

Department of Economic and Management, University of Brescia, Contrada Santa Chiara, 50, 25122 Brescia, e-mail: paola.zuccolotto@unibs.it 

1 

297 

Tullio Facchinetti and Rodolfo Metulini and Paola Zuccolotto 

2 

### **1 Introduction** 

Recent years registered the rise of data analytics applied to sports. Experts in data science are nowadays employed by teams to improve strategical decisions. These strategies, related to the objective of winning the games, may regards either single players or the whole team and must consider both offensive and defensive performances. In basketball, Oliver [1] outlines most of the tools used to evaluate performance. Offensive performance can be measured in terms of shots (Zuccolotto et al. [2]) or considering other aspects of playing, such as the number of possessions per game (Kubatko et al. [3]). Sampaio et al. [4] and Paulauskas et al. [5] applied a descriptive discriminant analysis to different competitions to identify which variables best predict differences in the playing style. From a defensive perspective, Franks et al. [6] and Goldsberry and Weiss [7] introduced a new suite of defensive metrics suggesting to integrate spatial approaches and player tracking data. 

The positioning and the velocity of players is an essential aspect to be considered when analysing both offensive and defensive performance. The robust statistical apparatus of National Basketball Association (NBA) supported by private companies made analysis of offensive and defensive moments relatively easy. Wu and Bornn [8] provide a tool for the visual analysis of offensive actions using a sensor data technology. Miller and Bornn [9] use the same data to catalogue NBA league strategies according to players’ movements. Ball circulation during offense actions has been analysed by D’Amour et al. [10] to show that the more open shots opportunities can be generated with more frequent and faster movements of the ball. Less attention was paid to European leagues, mainly depending on the restriction on data collection, which is rarely granted to authorized operators. Metulini et al. [11, 12] and Metulini [13] use tracked data from Italian professional basketball games collected by mean of an accelerometer device and they split games into clusters of homogeneous spatial distances among players, looking for those with better team shooting performance. Metulini et al. [14], using the same data, measured the relation of surface area occupied by players in offence and in defence with the number of scored points by the team. 

However, accelerometer devices track players’ movements along the full game, without distinguishing between active/inactive periods and offensive/defensive possessions. A possible solution is to instruct a person to track these information during the game. However, this option can be unpractical either due to organizational issues and cost impact. For these reasons, we propose a procedure that identifies and removes inactive periods and classifies them as either offensive or defensive. Such a procedure allows a better usage of tracked data from localization systems for the aim of a better team performance analysis at support to game decision in basketball, from professional to amateur and youth leagues. 

In this paper we discuss the procedure proposed by Metulini [15] and we introduce a validation strategy based on the use of a “ground truth” extracted from a video-based annotation of a sample of games. 

298 

Detecting and classifying moments in basketball matches using sensor tracked data 

3 

### **2 Data** 

The tracking system collects the position and the velocity of every player during the full game length, including whose waiting on the bench, along the x-axis (court length) and the y-axis (court width). The measured positions are expressed in centimeters (cm); the estimated accuracy of the tracking system is around 30 cm. Each measurement is marked by its time instant t. The tracking system is able to capture measurements at a sampling frequency of 50 Hz, corresponding to a measurement every 20 milliseconds (ms). We call the ordered set of measurements **X** . The measurement made at the time instant t, denoted with xt , thus contains the following information: 

- The vector of the position for the i-th player along the x− and the y− axis, denoted as posi(t) = {pos<sup>x</sup> i<sup>(t), posy</sup> i<sup>(t)}, measured in cm, where superscript x and</sup> y are used, respectively, for court length and court width; 

- The vector of the velocity for the i-th player along the x− and the y− axis, denoted as veli(t) = {veli<sup>x(t),vel</sup> i<sup>y(t)}, measured in kilometres per hour (km/h);</sup> 

- The velocity for the i-th player in the court at time t, computed as vi(t) = ~~�~~ veli<sup>x(t)2 +vel</sup> i<sup>y(t)2.</sup> 

### **3 The procedure** 

The procedure aims at removing specific measurements from **X** according to three different criteria and to separate the game into offensive and defensive possessions. The filtering and labelling scheme is based on defining kinematic parameters related to players’ positions and velocities on the International Basketball Federation (FIBA) court (Figure 1). The outcome is a reduced set of measurements denoted as **Xr** that includes two features about the type of possession (poss = {offensive, defensive, transition}) and the ordered number of possession (ord = {1,2, ..., n}), respectively. In detail: 

1. According to criterion 1-A, the procedure drops from **X** all the measurements belonging to the time instant t in which the number of players inside the court is different from 5. 

2. Criterion 1-B drops from **X** the measurements when at least one player is on the free throw shooting area (FTSA) for at least a specified interval of time Tft . Player i lies in the FTSA at time t if the vector posi(t) lies in the circle Cr centred on the center of the FTSA of radius r = 1.80m. 

3. The criterion 1-C removes those measurements where the speed of all the five players in the court is below a given threshold Vmin, for an interval of time equal or larger than Tvel. 

4. Criterion 2-A assigns the value of the variable poss to each measurement of **Xr** . The procedure generate the average x coordinate of the five players on the court 

299 

4 

Tullio Facchinetti and Rodolfo Metulini and Paola Zuccolotto 



<!-- Start of picture text -->
� ������<br>�������� ����� �������<br>�<br>�����<br>��������<br><!-- End of picture text -->

**Fig. 1** International Basketball Federation (FIBA) court with relevant measures annotated. 

at time t, avg pos<sup>x</sup> (t) = ∑<sup>5</sup> i=1<sup>posx</sup> i<sup>(t)/5.Themeasurement tcouldlieeitheron</sup> the offensive (avg pos<sup>x</sup> (t) > 4) or on the defensive (avg pos<sup>x</sup> (t) < −4) side of the court. transition is instead assigned to variable poss whereas avg pos<sup>x</sup> (t) lies in the interval {+4,-4}. 

5. Criterion 2-B assigns to the measurement of **Xr** the ord value, for the aim of counting for the total number of possessions in the game. The procedure assign to ord value “1” to measurement x1. Such a value increases by 1 whenever the variable poss takes the value transition at time t − 1 and either o f fensive or defensive at time t. 

### **4 The validation strategy** 

While parameter Tft can easily be determined by looking to the average time required by a player to shot one or two free-throws, the “best” values for the parameters Vmin and Tvel need for a tuning strategy in order to be correctly identified. The tuning strategy has the objective to find those values for Vmin and Tvel such that the accordance of the procedure with the “ground truth” is maximized. 

300 

5 

Detecting and classifying moments in basketball matches using sensor tracked data 

### **4.1 Video-based annotation** 

We extract the “ground truth” by using a specific smartphone application while watching the available video footage of the game. We take note of a number of game events related to i) the moments in which the game is active/inactive; ii) the moments of free-throws, time-outs, quarter- and half-time intervals; iii) the moments when the team was in offence/defence (Table 1). Based on the recorded data, we produce two reports. The first report displays when the action starts to be active 

|**game event**|**description**|
|---|---|
|start free-throws|a player is on the FTSA to shoot a free-throw|
|stop free throws|the game stops due a free-throw|
|start time-out|a time-out starts|
|stop time-out|a time-out ends|
|start half-time interval|an half-time interval starts|
|stop half-time interval|an half-time interval ends|
|<br>start quarter-time interval|a quarter-time interval starts|
|<br>start quarter-time interval|<br> a quarter-time interval ends|
|stop|the game stops for a generic reason|
|start|the game starts / restarts after a generic stop|
|offence|the team starts an offensive action|
|defence|the team starts a defensive action|



**Table 1** Names of the events and description. 

(action = play) or starts to be inactive (action = stop) with reference to a given moment (sec). active is a variable that assumes value equal to 1 if the game starts to be inactive in that moment. timeout, ft, quarter and half are variables assuming value equal to 1 if the reason of the inactivity is, respectively, a time-out, the shooting of a free-throw, a quarter-time interval or an half-time interval. In the excerpt reported in Table 2, the game starts at second 1 (active = 0 & sec = 1 in the first row). From second 1 to second 4 the game is active. At second 5 the game stops (active = 1 at the second row of the table) due to a generic reason. At second 13 the game restarts (third row) and at second 47 the game stops due to a free-throw ( ft = 1 in the fourth row). The second one reports the variable action, which can assumes either value 1 (start a offensive action for the team) or value 0 (start a defensive action for the team). In the excerpt in Table 3 the team starts the game in defence (sec = 1), it starts an offensive play at second 32, it goes back to defence at second 72, an so on. 

|**action **|**sec **|**active **|**timeout **|**ft quarter **|**half**|**action **|**sec **|**off**|
|---|---|---|---|---|---|---|---|---|
|play|1|1|0|0<br>0|0|off|1|1|
|stop|5|0|0|0<br>0|0|def|32|0|
|play|13|1|0|0<br>0|0|off|72|1|
|stop|47|0|0|1<br>0|0|def|138|0|



**Table 2** An excerpt from the first report. 

**Table 3** An excerpt from the second report. 

301 

6 

Tullio Facchinetti and Rodolfo Metulini and Paola Zuccolotto 

### **4.2 The “ROC” method** 

We use the ground truth to check for the robustness of the classification of the procedure in relation to the choice of parameters Vmin and Tvel. Actually, the robustness may be evaluated either in terms of how the procedure classifies active/inactive moments or in terms of how it classifies offence and defence. We borrow the approach of the Receiver Operating Characteristic (ROC) curves. The Area Under the Curve (AUC) is traditionally computed based on sensitivities and specificities to quantify the robustness of a prediction method (Zhou et al. [16], Pepe [17], Krzanowski and Hand [18]). Sensitivity measures the proportion of true positives, while specificity measures the proportion of true negatives. The ROC and AUC help in deciding the optimal threshold value by computing sensitivity and specificity on a series of possible thresholds. In this problem we have no threshold values to set for the underlying probabilities. In our case, the measurements are directly classified by the procedure as positive or negative (i.e. active/inactive; offence/defence). However, the binary classification changes as parameters Vmin and Tvel change. Therefore, we measure the performance of our procedure by evaluating the AUC with respect to different values of Vmin and Tvel used as thresholds. 

The proposed strategy is adopted for identifying the best parameters using active/inactive classification. The same strategy could be applied, making appropriate adaptations, using offence/defence classification. Let **X** ˜ be the set of measurements obtained from **X** by aggregating the observations at a frequency of 1 second. We let Yt˜ be the variable assuming value 1 if, according to the report, the game is inactive ˜ theat secondvariablet, 0 otherwise. Moreover, for a givenassuming value 1 in t˜ if the majority Vminofandthe Tvelobservationscombination, letcorrespond- Yt˜<sup>⋆be</sup> ing to that t˜ was labelled as inactive by the procedure, 0 otherwise. We define true positives (TP), true negatives (TN), false positives (FP) and false negatives (FN) accordingly and we compute sensitivity and 1 - specificity. The method is defined by the following 3 steps: 

1. For a given Vmin we compute the AUC for Tvel varying in a range of values. The AUC is then computed for all the Vmin in a range of values. 

2. Vmin is selected such that AUC is maximized. 

3. Adopting the Youden’s index criteria (Youden’s [19], Fluss et al. [20] and Liu [21]), for the chosen Vmin, the value of Tvel is selected such that the sum of sensitivity and specificity is maximized. 

### **5 Results** 

We apply the method for classifying active/inactive periods to the set of measurements of one game played by a team during the Italian Basketball Cup Final Eight 2017. The game will be indicated as case study 1 (CS1) and the corresponding set, counting for 505, 291 measurements, will be denoted with **X** 1. We first compute the 

302 

Detecting and classifying moments in basketball matches using sensor tracked data 7 



<!-- Start of picture text -->
7<br><!-- End of picture text -->

value of the AUC corresponding to different values of Vmin. Up to a given point, the AUC increases as Vmin increases; beyond such a point, the AUC decreases as Vmin increases (Figure 2). The largest value of AUC is 0.8329. According to the second step, we select the value of Vmin corresponding to the largest AUC, which is equal to to 9.25km/h. Moving to the third step, we search for the value of Tvel that maximize the Youden’s index (Figure 3). The largest Youden’s index is found for Tvel = 2. 



<!-- Start of picture text -->
0.25 3 5 7 9 12 15 18 0.25 3 5 7 9 12 15 18<br>0.80<br>0.5<br>0.70 0.4<br>0.60 0.3<br>0.50 0.2<br><!-- End of picture text -->

**Fig. 2** AUC (y-axis) for Vmin in [0,20] (x-axis). **Fig. 3** Youden (y-axis) for Tvel in [0,20] (x-axis). 

### **6 Conclusions** 

In this work we outline a methodological approach that should be used to automatically select the correct portion of spatial tracking data of a game by just selecting those that correspond to active moments, and to correctly classify them by type of possession. The procedure, along with the identified values for the kinematic parameters may helps experts and analysts who want to analyse tracked data without watching the video of the game. Future work will focus on a more extensive application of this methodological approach and to a larger number of real case studies. First by focusing on finding the parameters that best classify active and inactive moments, then by looking to the best choice with regards to the classification among offensive and defensive possessions. 

**Acknowledgements** Research carried out in collaboration with the Big&Open Data Innovation Laboratory (BODaI-Lab), University of Brescia (project nr. 03-2016, title Big Data Analytics in Sports, https://bdsports.unibs.it/), granted by Fondazione Cariplo and Regione Lombardia. 

303 

Tullio Facchinetti and Rodolfo Metulini and Paola Zuccolotto 

8 

### **References** 

1. Oliver, D. Basketball on paper: rules and tools for performance analysis. Potomac Books, Inc. (2004). 

2. Zuccolotto, P., Manisera, M., & Sandri, M. Big data analytics for modeling scoring probability in basketball: The effect of shooting under high-pressure conditions. International Journal of Sports Science & Coaching, vol. 13(4), pp. 569-589 (2018). 

3. Kubatko, J., Oliver, D., Pelton, K., & Rosenbaum, D. T. A starting point for analyzing basketball statistics. Journal of Quantitative Analysis in Sports, vol. 3(3) (2007) 

4. Sampaio, J., McGarry, T., Calleja-Gonzlez, J., Siz, S. J., i del Alczar, X. S., & Balciunas, M. Exploring game performance in the National Basketball Association using player tracking data. PloS one, 10(7), e0132894. (2015) 

5. Paulauskas, R., Masiulis, N., Vaquera, A., Figueira, B., & Sampaio, J. Basketball gamerelated statistics that discriminate between European players competing in the NBA and in the Euroleague. Journal of human kinetics, vol. 65, pp. 225-233 (2018). 

6. Franks, A., Miller, A., Bornn, L., & Goldsberry, K. Counterpoints: Advanced defensive metrics for nba basketball. In 9th Annual MIT Sloan Sports Analytics Conference, Boston, MA. (2015) 

7. Goldsberry, K., & Weiss, E. The Dwight effect: A new ensemble of interior defense analytics for the NBA. Sports Aptitude, LLC. Web, pp. 1-11 (2013) 

8. Wu, S., & Bornn, L. Modeling offensive player movement in professional basketball. The American Statistician, vol. 72(1), pp. 72-79 (2018). 

9. Miller, A. C., & Bornn, L. Possession sketches: Mapping nba strategies. In MIT Sloan Sports Analytics Conference (2017). 

10. DAmour, A., Cervone, D., Bornn, L., & Goldsberry, K. Move or die: How ball movement creates open shots in the NBA. MIT Sloan Sports Analytics Conference (2015). 

11. Metulini, R., Marisera, M. and Zuccolotto, P. Space-Time Analysis of Movements in Basketball using Sensor Data. Statistics and data science: new challenges, new generations (2017). 

12. Metulini, R., Manisera, M. and Zuccolotto, P.. Sensor Analytics in Basketball. Proceedings of MathSport International 2017 Conference.( 2017). 

13. Metulini, R. Players Movements and Team Shooting Performance: a Data Mining approach for Basketball. Book of short papers SIS2018, ISBN-9788891910233. Publisher: Pearson, Editors: Antonino Abbruzzo, Eugenio Brentari, Marcello Chiodi e Davide Piacentino (2018). 

14. Metulini, R., Manisera, M., Zuccolotto, P. Modelling the dynamic pattern of surface area in basketball and its effects on team performance. Journal of Quantitative Analysis in Sports, vol. 14.3, pp. 117-130 (2018). 

15. Metulini, R. Filtering procedures for sensor data in basketball. Statistics & Applicazions, vol. 15(2), pp. 133-150 (2017). 

16. Zhou, X. H., McClish, D. K., & Obuchowski, N. A. Statistical methods in diagnostic medicine (vol. 569). John Wiley & Sons (2009). 

17. Pepe, M. S. The statistical evaluation of medical tests for classification and prediction. Medicine (2003). 

18. Krzanowski, W. J., & Hand, D. J. ROC curves for continuous data. Chapman and Hall/CRC (2009). 

19. Youden, W. J. Index for rating diagnostic tests. Cancer, vol. 3(1), pp. 32-35 (1950). 

20. Fluss, R., Faraggi, D., & Reiser, B. Estimation of the Youden Index and its associated cutoff point. Biometrical Journal: Journal of Mathematical Methods in Biosciences, vol. 47(4), pp. 458-472 (2005). 

21. Liu, X. Classification accuracy and cut point selection. Statistics in medicine, vol. 31(23), pp. 2676-2686 (2012). 

304 


