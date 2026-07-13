<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2025/2025 - Analyzing South American soccer team performance using distributional regression models - Rosa et al.pdf -->

J. Quant. Anal. Sports 2026; aop 

### **Research Article** 

Lucas F. Rosa*, Pedro H. R. Cerqueira, Luiz R. Nakamura and Dimitrios M. Stasinopoulos 

# **Analyzing South American soccer team performance using distributional regression models** 

https://doi.org/10.1515/jqas-2025-0055 Received April 2, 2025; accepted June 22, 2026; published online July 6, 2026 

**Keywords:** football; games; sport statistics; statistical modeling 

**Abstract:** South American soccer has distinct characteristics that have a direct impact on team performance and points ratio in competitions. Therefore, this paper analyzes the factors influencing the points ratio of teams in the three major South American soccer leagues in Brazil, Argentina and Chile, during 2022–2024 seasons. We use distributional regression models, also known as generalized additive models for location, scale, and shape, which allow the identification of different factors that affect (both linearly and non-linearly) not only the average (or median) points ratio but also other characteristics such as, for example, the dispersion of the data. The results indicate that the variables goals scored, goals conceded, clean sheets, accurate passes, tackles, saves, fouls, red cards, and the league in question have a significant influence on the median performance of the teams. Additionally, the number of assists, dribbles, saves, yellow cards, and shots against affect the variability in points at the end of the championship. Thus, we can conclude that success in South American soccer is determined by a combination of offensive, defensive, disciplinary, and contextual factors, emphasizing the importance of balanced strategies. Understanding these relationships can assist coaches and analysts in making more informed decisions to improve team performance. 

***Corresponding author: Lucas F. Rosa** , Universidade Federal de Lavras, Programa de Pós-Graduação em Estatística e Experimentação Agropecuária, 37203-202, Lavras, Brazil, E-mail: lucasferreira_77@hotmail.com.br. https://orcid.org/0000-0002-3263-4089 **Pedro H. R. Cerqueira** , Departamento de Estatística, Universidade Estadual de Londrina, Londrina, Brazil 

**Luiz R. Nakamura** , Departamento de Estatística, Universidade Federal de Lavras, Lavras, Brazil. https://orcid.org/0000-0002-7312-2717 **Dimitrios M. Stasinopoulos** , School of Computing and Mathematical Sciences, University of Greenwich, London, UK. https://orcid.org/0000-0003-2407-5704 

## **1 Introduction** 

Soccer is one of the most popular sports in the world and holds particular prominence in South America (Rosales and Tito 2022), where it has a special cultural importance, characterized by the passion and skill of its players, who are wellknown for their creative and technical style. Since its inception in the late 19th century, the sport has been progressively adopted, institutionalized, and popularized across South America, becoming a defining feature of the continent’s global identity (Brown 2014) and substantially contributing to the sport’s history, not only through international titles but also by producing players who have become global icons, or even legends, such as Pelé, Maradona, and Messi (Toledo 2021; Faedo and Corrius 2024). Furthermore, the large-scale export of players from this region has increasingly shifted soccer fanbase and viewership to European leagues (Brown 2018). 

Quantifying the relationships between match data and game results is an efficient method for identifying key performance indicators in soccer competitions (Mao et al. 2016). Determining which match statistics contribute most significantly to victory is critical for performance analysis, and coaches can design more effective strategies to maximize the chances of success based on current trends (Kubayi and Larkin 2022). Additionally, topics such as the outcome of specific matches, the probability of qualifying for major tournaments, the risk of relegation, attacking performance, defensive solidity, among other key aspects, are highly relevant for those involved in the sport (Louzada et al. 2014). 

In this sense, statistics and data science have played an increasingly important role in soccer, altering how the sport is understood and practiced. Various studies have used different approaches to analyze the factors that influence the sport, with the aim of understanding or 

Open Access. © 2026 the author(s), published by De Gruyter. 

This work is licensed under the Creative Commons Attribution 4.0 International License. 

> **2 —** L. F. Rosa et al.: Analyzing South American soccer team performance 

predicting championship results and assessing the quality of matches and teams. For example, traditional regression models were used in Lago-Peñas et al. (2011), generalized linear models were employed in the works of Malcata et al. (2012), Louzada et al. (2014), and Mao et al. (2016), causal inference was used in the study by Cerqueira et al. (2017), discriminant analysis was applied by Lago-Peñas and Lago-Ballesteros (2011) and Castellano et al. (2012), principal component analysis and clustering were utilized by Moura et al. (2014), and machine learning algorithms were used in Hewitt and Karakuş (2023), Markopoulou et al. (2024), Malikov and Kim (2024). 

Despite the extensive literature on predictive studies of soccer matches, most research focuses on major European leagues. In contrast, our paper concentrates on three major South American leagues – the Liga Profesional de Fútbol (Argentina), the Campeonato Brasileiro Série A (Brazil) and the Campeonato Nacional (Chile) – considering data from the years 2022, 2023, and 2024. Furthermore, from a statistical modeling perspective, in this paper, we use the generalized additive models for location, scale, and shape (GAMLSS; Rigby and Stasinopoulos 2005), also referred to as distributional regression models (Heller et al. 2022). While GAMLSS is among the most flexible approaches available in the literature, its application in this context remains limited, with only a few examples, such as Nakamura et al. (2019) and Wang et al. (2024). However, it appears to be highly promising, as it can identify not only the factors influencing the mean (or median) of a response variable (e.g., points ratio in a competition) but also those that directly affect the variability of the outcomes. 

## **2 Dataset overview** 

The dataset used in this study compiles performance statistics from three major South American soccer leagues for the 2022, 2023, and 2024 seasons. The championships in question are the top divisions of Argentina, Brazil, and Chile, which are arranged in a league structure. In this system, all participating teams compete in a single standings table, with each club facing the other at least once per season (Beck et al. 2022). This round-robin format allows for a more consistent evaluation of team performance over time, minimizing the impact of sporadic results and offering a comprehensive and fair assessment of each team’s overall performance. This league model is widely adopted by most national soccer leagues worldwide. In general, points are awarded as follows: three for a win, one for a draw, and zero for a loss. 

The detailed statistics for each league were obtained from the SofaScore website (https://www.sofascore.com) 

using web scraping techniques. This process allowed for the compilation of a collection of explanatory variables that potentially explain team performance, which, in this paper, is based on the standardized points ratio over the three considered seasons, formally defined as. 



where _Ptls_ is the total number of points earned by the team _t_ in league _l_ during season _s_ , and _Pls_<sup>∗isthemaximumpossible</sup> points in that corresponding league and season (i.e., number of matches multiplied by three points per win). This formulation ensures that the points ratio is a standardized measure of team performance that can be applied across leagues and seasons. Hence, the dataset has 191 observations across the three leagues and seasons. The leagues are distinct and do not share teams. Furthermore, it should be noted that many observations correspond to the same team in different seasons within a league. 

The collected variables cover various aspects of the game, such as general information (league, season, and number of matches); goal performance (goals scored and goals conceded); participation in plays (assists); shooting statistics (shots, shots from inside the box, shots from outside the box, shots on target); dribbles and accurate crosses percentage; set-pieces and ball possession (corners, fast breaks, average ball possession, accurate passes percentage, and accurate long balls percentage); defensive performance (clean sheets, tackles, interceptions, and saves); as well as other statistics, such as offsides, fouls, yellow and red cards, and shots against. Consequently, a total of 25 covariates were considered as potential candidates to explain different aspects of the points ratio. 

The number of participating teams in South American soccer leagues varies by league and season. The Argentine League follows a single round-robin system, with each team playing every other team once, for a total of 27 rounds. The team with the most points at the end of the competition is crowned champion. Meanwhile, the Chilean League features 16 teams and a total of 30 matches, organized in a double round-robin system. The Brazilian League follows the same format as the Chilean League, with home and away matches divided into two rounds, but with 20 clubs and a 38-match season. These differences can have an impact on league comparisons, as the total number of games is an important factor in determining team performance. To address issues arising from discrepancies in the number of matches between leagues, all explanatory variables were standardized on a per-match basis, as suggested by Nakamura et al. (2019). It should be noted that the response (points ratio) already considers the number of matches 

L. F. Rosa et al.: Analyzing South American soccer team performance **— 3** 

by definition, as it is defined as the proportion of points obtained relative to the maximum possible points in the league season. This adjustment ensures that analyses This adjustment ensures that analyses are conducted in a fairer and more comparable manner, taking into account differences in the number of teams and matches within each competition. 

## **3 Statistical modeling: the GAMLSS framework** 

GAMLSS are distinguished by their ability to capture highly complex relationships between covariates and multiple aspects of the response variable (not limited to the mean) through different regression structures (Ramires et al. 2021a). Mathematically, they are defined as. 





where _Y_ is the response variable that is explained by a statistical distribution ( _𝜃k_ ) with parameters _𝜃k_ = _⊤_ ( _𝜃_ 1 _,_ … _, 𝜃 p_ ) , _gk_ (⋅) is a known monotonic link function, relating the distribution parameter _𝜃k_ to the predictor _𝜂k_ – for example, the identity link is usually considered when −∞ _< 𝜃k <_ ∞, the logarithm link when _𝜃k >_ 0, and the logit link when 0 _< 𝜃k <_ 1 (De Bastiani et al. 2018) –, _Xk_ is a _⊤_ known design matrix, _𝛽k_ =<sup>(</sup> _𝛽k_ 1 _,_ … _, 𝛽k Jk_ ) is a parameter vector, and _hkj_ (⋅) is a smooth non-parametric function of a covariate _xkj_ , such as a P-spline (Eilers and Marx 1996). 

Since the response in this study refers to the points ratio in soccer leagues, which lies within the unit interval [0,1], the distribution  must account for this characteristic. The beta (Ferrari and Cribari-Neto 2004) and the logit-normal (Atchison and Shen 1980) are two of the most widely used distributions in such cases, both having two parameters ( _𝜃_ 1 _, 𝜃_ 2) = ( _𝜇, 𝜎_ ). These distributions were explored in similar contexts, namely within the GAMLSS framework for soccer applications, in the studies by Nakamura et al. (2019) and Wang et al. (2024). 

Mathematically, if Y follows a beta distribution, then its probability density function (pdf) can be expressed as. 



where _𝛼_ = _𝜇_ (1 − _𝜎_<sup>2</sup> )∕ _𝜎_<sup>2</sup> , _𝛽_ = (1 − _𝜇_ )(1 − _𝜎_<sup>2</sup> )∕ _𝜎_<sup>2</sup> , with _𝛼 >_ 0 and _𝛽 >_ 0, implying 0 _< 𝜇 <_ 1 and 0 _< 𝜎 <_ 1, and _B_ ( _𝛼, 𝛽_ ) = ∫<sup>1</sup> 0<sup>_t𝛼_−1(1−</sup><sup>_t_)</sup><sup>_𝛽_−1 d</sup><sup>_t_isthebetafunction.Notethat</sup> 

this parameterization, presented by Rigby et al. (2019), is not the one commonly used in the literature. However, in this form, the parameter _𝜇_ of the distribution corresponds exactly to the mean, allowing for a straightforward interpretation – a feature of particular interest in GAMLSS (Ramires et al. 2021a) –, and _𝜎_ is a dispersion parameter. Alternatively, the pdf of the logit-normal distribution can be as 



where 0 _< 𝜇 <_ 1 is exactly the median and _𝜎 >_ 0 is a dispersion parameter. 

Within the GAMLSS framework, the selection of covariates to be used in each of the regression structures for the parameters _𝜇_ and _𝜎_ of both beta and logit-normal distributions can be performed using Strategy A (Ramires et al. 2021b). This stepwise-based method employs the generalized Akaike information criterion (Voudouris et al. 2012), expressed as GAIC = −2 × _l_ + _𝜅_ × _d f_ , where _l_ is the fitted log-likelihood function, _𝜅_ is a penalty and _df_ represents the effective degrees of freedom, to select the best model. It is noteworthy that when _𝜅_ = 0 and _𝜅_ = 2 the GAIC reduces to the global deviance (GD) and the Akaike information criterion (AIC; Akaike 1974), respectively. In this paper, we have used the AIC in the Strategy A. 

For two-parameter distributions such as beta or logitnormal, Strategy A is described by Nakamura et al. (2017) as follows: 

- Step 1: The strategy starts with the null model, that is, without considering any covariates; 

- Step 2: Considering _𝜎_ as a constant, a forward selection procedure is performed for the parameter _𝜇_ , that is, covariates are sequentially added to this structure, with each step selecting the one that yields the lowest GAIC value; 

- Step 3: Considering the fitted model for _𝜇_ in Step 2, a stepwise procedure is performed for the parameter _𝜎_ , that is, covariates are included and excluded in this structure according to the GAIC value; 

- Step 4: Considering the fitted model for _𝜎_ in Step 3, a backward procedure is applied to the fitted model in Step 2, that is, covariates are sequentially removed according to the GAIC value. 

At the end of the steps, the final model may have different covariates for each of the fitted regression structures. 

> **4 —** L. F. Rosa et al.: Analyzing South American soccer team performance 

It is worth noting that the inclusion of smooth functions allows for properly capturing complex nonlinear relationships. In practice, within the GAMLSS framework we initially consider smooth functions for all numerical variables, allowing the data to determine the shape of the relationship. However, when the estimated smooth terms indicate an approximately linear behavior, the smoothing functions are removed to simplify the model without loss of explanatory power.Costa et al. (2025) warn that neglecting potential nonlinear effects may lead to incorrect inclusion and/or exclusion of covariates across the different model structures, potentially compromising subsequent interpretations and inferences. 

For diagnostic analysis, we compute normalized quantile residuals (Dunn and Smyth 1996) and graphically depict them in worm plots (van Buuren and Fredriks 2001), which are commonly used in the GAMLSS literature. Their key advantage is that they necessarily follow a standard normal distribution, regardless of the response variable’s distribution, as long as the fitted model is adequate. For a continuous distribution, they can be expressed as _ri_ = Φ<sup>−1[</sup> _F_ ( _y_ | _𝜃_ )<sup>]</sup> , where Φ<sup>−1</sup> (⋅) is the inverse of the cumulative distribution function (cdf) of the standard normal distribution and _F_ ( _y_ | _𝜃_ ) is the model cdf. 

## **4 Results** 

Figure 1 displays the response variable, the points ratio, using a box plot (Panel a) and a histogram (Panel b), along with the marginal fit (i.e., without considering covariates) of the beta and logit-normal distributions. As can be seen, both distributions provide a reasonable fit to the observed symmetric density. Furthermore, only two outliers were in the data. 

Table 1 presents the main descriptive statistics for the response variable. The observed average points ratio is 0.4545, which is close to the median of 0.4444, suggesting an approximately symmetric distribution, as confirmed by the skewness coefficient of 0.2640. The beta and logit-normal distributions appear to be appropriate options for modeling this variable within the unit interval, given that the obseved ratios lies inside the range of 0.1930–0.7531. 

Following the descriptive analysis of the response, we proceeded with the covariate selection procedure for the different regression structures in both GAMLSS based on the beta and logit-normal distributions. A total of 25 covariates, as previously described in Section 3, were initially considered as candidates to explain all regression structures. Table 2 summarizes the best models for each distribution after the covariate selection process, thus reflecting 

the final fitted models, presenting the GD and AIC values. Although the numbers were close, the model based on the logit-normal distribution had the lowest (and consequently the best) values for both criteria: GD (−872.5483) and AIC − ( 790.6954). 

It is worth noting the difference in degrees of freedom between the two models. The inclusion of smoothing functions in the regression structures can increase the effective degrees of freedom. In our case, after the covariate selection procedure, six different smoothing functions were considered in the GAMLSS based on the logit-normal distribution, whereas only four were used in the beta-based model. A detailed discussion of this topic is provided by Hodges and Sargent (2001). 

The worm plot show that the model based on the logitnormal distribution provides a reasonable fit to the data, as all residuals fall within the 95 % confidence bands (Figure 2). Consequently, this model will be considered for the remainder of this paper. 

The final fitted GAMLSS based on the logit-normal distribution is given by. 









> log( _𝜎_ ) = −4 _._ 560 + 0 _._ 761 ⋅ assists + _s_ 21(dribbles) + 0 _._ 782 ⋅ saves + _s_ 22(yellowcards) + _s_ 23(shotsagainst). (4) 

Nine different covariates were selected to explain the median points ratio _𝜇_ : league, goals scored, goals conceded, accurate passes percentage, clean sheets, tackles, saves, fouls, and red cards. Note that the Brazilian league does not appear in this regression structure, as it is considered here as the reference category. Meanwhile, five other variables were used to model dispersion _𝜎_ : assists, dribbles, saves, yellow cards, and shots against. Furthermore, as can be seen, we fitted three smoothing functions in each regression structure to model nonlinear behaviors. The use of 

L. F. Rosa et al.: Analyzing South American soccer team performance **— 5** 



<!-- Start of picture text -->
A B<br>Beta<br>Logit−Normal<br>3<br>0.6<br>2<br>0.4<br>1<br>0.2 0<br>0.00 0.25 0.50 0.75 1.00<br>Points Ratio Points Ratio<br>Density<br><!-- End of picture text -->

**Figure 1:** Distribution of the response points ratio: (A) box plot and (B) histogram. 

**Table 1:** Descriptive statistics for the response points ratio. 

|**Mean**|**Median**|**Standard deviation**|**Skewness**|**Kurtosis**|**Minimum**|**Maximum**|
|---|---|---|---|---|---|---|
|0.4545|0.4444|0.1089|0.2640|−0.0800|0.1930|0.7531|



such functions is critical for capturing the true effect of the covariates included in the model, particularly when this effect is nonlinear. According to Ramires et al. (2019), when such functions are considered, their effects are typically investigated graphically rather than using hypothesis tests. Figure 3 shows the fitted functions in both parameters. All other considered variables are significant at the 5 % level. 

## **5 Discussion** 

### **5.1 Median points ratio** 

The negative coefficients associated with Argentine and Chilean leagues in equation (4) indicate that the median 

**Table 2:** Goodness-of-fit measures for the best-fitted models based on both distributions. 

|**Model**|**df**|**GD**|**AIC**|
|---|---|---|---|
|Logit-normal|40.9264|−872.5483|−790.6954|
|Beta|21.4464|−810.9610|−768.0683|



points ratio is significantly higher in the Brazilian Championship. From a practical perspective, this can be explained by the fact that different leagues have unique characteristics that directly impact on team performance and, as a result, the points ratio. These differences could be attibuted to a variety of factors, including level of competitiveness, predominant style of play, average team quality, home-field factors, and climatic conditions (Aquino et al. 2017; Kubayi and Toriola 2019; Orchard 2002; Watanabe et al. 2017). 

The variable goals scored has a positive effect on the median structure, which means that as the number of goals increases, so does the median points ratio. This behavior can be explained by the fact that outscoring opponents is the central objective of the game (Schulze et al. 2021). In other words, goals scored are the primary determinant of a soccer team’s success (Kubayi 2020), directly influencing the probability of victory and, consequently, the points ratio. Several other studies on goals scored have explored a variety of performance-related factors, including the differences between open-play and set-piece goals (Stafylidis et al. 2022), the impact of first goal (Pratas et al. 2016), and the effects of match time and league ranking on different types of goals 

> **6 —** L. F. Rosa et al.: Analyzing South American soccer team performance 



**Figure 2:** Worm plot for the final fitted GAMLSS model based on the logit-normal distribution. 

(Zhao et al. 2019). These analyses provide a broader understanding of the role of goals in soccer and their implications for team performance. 

Similarly, as the number of goals conceded increases, the median points ratio tends to decrease. This pattern is consistent with the findings of Andrzejewski et al. (2022), who also observed a negative correlation between goals conceded and the points ratio in the German Bundesliga between 2017-2018 and 2018–2019 seasons. Their findings support the hypothesis that conceding more goals has a 

detrimental impact on team performance and results. Analyses of goals conceded can also be found in other studies, such as Clemente et al. (2016) and Aguado-Méndez et al. (2021). 

In contrast to goals conceded, a positive correlation was observed between games without conceding goals and the parameter _𝜇_ in equation (4). In other words, the more games a team goes without conceding goals, the greater the median points ratio. This result supports the findings of Nakamura et al. (2019), who also identified that goals 



<!-- Start of picture text -->
A B C<br>0.10<br>0.00 0.10<br>0.05<br>−0.05<br>0.05<br>−0.10<br>0.00<br>0.00<br>−0.15<br>−0.05<br>−0.05<br>−0.20<br>12.5 15.0 17.5 20.0 22.5 2.0 2.5 3.0 3.5 4.0 0.0 0.1 0.2 0.3 0.4<br>Tackles Saves Red cards<br>D E F<br>1.0 1.0<br>1.0<br>0.5<br>0.5<br>0.5<br>0.0<br>0.0<br>−0.5 0.0 −0.5<br>−1.0 −1.0<br>−0.5<br>10 12 14 16 18 1.5 2.0 2.5 3.0 3.5 5 10 15 20 25<br>Shots against Yellow cards Dribbles<br>)μ )μ )μ<br>Partial effect in logit( Partial effect in logit( Partial effect in logit(<br>)σ )σ )σ<br>Partial effect in log( Partial effect in log( Partial effect in log(<br><!-- End of picture text -->

**Figure 3:** Fitted smoothing functions: (A) Tackles on the median points ratio; (B) saves on the median points ratio; (C) red cards on the median points ratio; (D) shots against on the dispersion parameter; (E) yellow cards on the dispersion parameter; and (F) dribbles on the dispersion parameter. 

L. F. Rosa et al.: Analyzing South American soccer team performance **— 7** 

conceded has a positive relationship with the points ratio in major European soccer leagues during the 2011–2012, 2012–2013, and 2013–2014 seasons. This result highlights a fundamental aspect of soccer, as teams that avoid conceding goals can significantly increase their chances of success. 

Fouls also have a negative relationship with the median points ratio. This negative association is most likely explained by the effect that heavy fouling has on the dynamics of the game. According to Sun et al. (2024), team that commit a high number of fouls may lose control of the match, as players in foul trouble may be substituted by the coach for protection, or their role within the team may be compromised for the remainder of the game affecting overall team performance and changing in-game trends. The authors also point out that a high number of fouls allows opponents to create more scoring opportunities through free kicks or even penalties. Moreover, frequent fouling can result in disciplinary sanctions, including yellow and red cards, which can negatively impact the team by temporarily reducing the number of players on the pitch or suspending them for future matches (Lago-Peñas and Lago-Ballesteros 2011). Further studies in soccer matches can be found in Gümüşdaˇg et al. (2011) and Ryynänen et al. (2013). 

As seen in Figure 3, tackles, saves, and red cards have a nonlinear effect on the median points ratio, meaning that simpler statistical models would fail to capture such behavior. The variable tackles initially has a positive effect on the median, reaching its peak at 17 tackles (Figure 3(a)). Beyond this threshold, the median slightly decreases before stabilizing. In other words, if we assume the effect is approximately constant after 17 tackles, we can conclude that the number of tackles no longer significantly impacts the median of points ratio after this point. Using simpler modeling approaches, Liu et al. (2015) found a positive impact of tackles on winning probability during the 2014 FIFA World Cup group stage. Similarly, Vogelbein et al. (2014) emphasized the importance of quick possession recovery in the 2010–2011 Bundesliga, including tackles, identifying it as essential for defensive performance. Their study also revealed that elite teams had faster reaction times, regaining possession more efficiently after losing it, implying more success in defensive strategies, including tackles. Additionally, Almeida et al. (2014) suggested that stronger teams tend to adopt more proactive defensive strategies, seeking to reclaim possession – potentially through tackles – even when leading. These clubs stood out for their ability to press opponents in more advanced areas of the game, emphasizing the strategic value of defensive recoveries. 

A sinusoidal pattern can be seen in the median points ratio and the number of goalkeeper saves (Figure 3(b)). The 

relationship is nearly constant up to 2.5 saves per match, then becomes positive until 3 saves per game, followed by a decline between 3 and 3.5 saves, before returning to a positive trend from 3.5 to 4 saves per match. Goalkeepers are typically the last line of defense for soccer teams (White et al. 2018), thus the positive correlation between 2.5 and 3 saves may indicate that the goalkeeper is making the right number of interventions, thereby maintaining the team’s competitiveness. However, after this threshold, the median points ratio starts to decline, possibly indicating that a higher number of saves is not necessarily associated with better team performance, but rather shows an increased need for interventions – likely due to defensive weakness. After 3.5 saves, the relationship becomes positive again, implying that a higher number of saves indicates better goalkeeping ability, maybe reflecting greater efficiency in critical moments, which could held secure important points for the team. In Andrzejewski et al. (2022), shots on target saved by goalkeepers showed a positive correlation with the total points earned by team in the German Bundesliga. The study emphasized that goalkeeper saves were crucial in determining league standings. Other studies on saves and goalkeeper performance can be found in Obetko et al. (2022) and Perez-Arroniz et al. (2023). The complex pattern found for this variable emphasizes the importance of considering smoothing functions in the modeling process. Although difficult to interpret, ignoring nonlinear behaviors, as highlighted in Section 3, may lead to the incorrect inclusion or exclusion of covariates in the regression structures and, consequently, to misleading inferences. 

Another fluctuating pattern can be seen in the variable red cards (Figure 3(c)). Up to approximately 0.07 red cards per match, the points ratio remains roughly constant, suggesting that isolated disciplinary events do not significantly compromise overall performance. It then increases until around 0.13, followed by a decline up to around 0.22. After that, the relationship becomes positive again until about 0.34, remaining roughly constant up to 0.40. These changes may reflect complex competitive conditions. Occasional expulsions may be associated with high-intensity defensive play, where tactical fouls prevent goals, whereas higher frequencies of red cards per match may suggest disciplinary instability. From a statistical perspective, capturing these fluctuations is crucial for ensuring that the empirical assumptions of the fitted model are fully met, making all inferences reliable. Studies in the literature often use linear relationships to explain the impact of red cards on points ratio. For example, Liu et al. (2015) conclude that red cards have a clear negative impact on the chance of winning due to the numerical disadvantage resulting from player 

> **8 —** L. F. Rosa et al.: Analyzing South American soccer team performance 

ejections. According to Lago-Peñas et al. (2010), losing teams had a greater average of red cards, which supports the relationship between ejections and unfavorable outcomes. Nevertheless, Caliendo and Radic (2006) found out that the impact of a red card is determined by the timing of the expulsion and has no effect if issued at the end of the first half or later. 

An interesting and possibly unexpected result was the negative effect of accurate passes percentage on the median points ratio, contradicting, for example, the findings of Kubayi (2020), who observed that winning teams performed better in such feature. However, accurate passes percentage associated with ball possession, particularly in defensive areas or regions without direct attacking influence, may not necessarily result in positive outcomes. Teams that are losing can have higher ball possession, raising concerns about its true effectiveness (Jones 2004). 

Some variables, such as shooting statistics and ball possession, were somewhat expected to explain the points ratio but were not selected. This may be attributed to their inherent relationship with other covariates in the model structure that already capture similar effects, or to other aspects that may justify the lack of significant influence of these variables. The absence of shots as a significant variable contradicts the findings of Lago-Peñas et al. (2010) and Lago-Peñas and -Ballesteros (2011), for example. However, Yue et al. (2014) highlight in their analysis that shot quality, represented by goal efficiency, is more important than the number of attempts in influencing match results. Their study reinforces that efficiency outweighs quantity. 

Although ball possession is frequently associated with better performance (Kapsalis et al. 2023), it may not be a decisive factor in the median points ratio. Different playing strategies, such as an offensive or defensive approach based on quick counterattacks, can be equally effective (Harrop and Nevill 2014). Thus, high ball possession does not necessarily reflect a clear advantage, especially in situations where offensive efficiency is more relevant than time spent in possession. Wang et al. (2022) concluded that ball possession alone does not determine a team’s success, but rather the coach’s strategy and the players’ technical and tactical performance. Furthermore, our findings aligns with those of Nakamura et al. (2019), in which the fitted predictive model also did not select this variable to explain the median points ratio. 

### **5.2 Dispersion of the points ratio** 

In this section we discuss the covariates selection in the regression structure related to the dispersion of the points ratio. However, it is vital to highlight that the GAMLSS 

approach has been rarely employed in sports science so far. As a result, there are very few studies in the literature that can be compared to our findings. To the best of our knowledge, as stated in Section 1, only two studies have applied this approach in this field. 

Wang et al. (2024) identified two covariates to explain variability: whether the national team under analysis has won the FIFA World Cup and its current FIFA ranking, both of which are not present in our study. In Nakamura et al. (2019), the chosen statistical distribution for capturing the behavior of the points ratio lacks a well-defined parameter associated to variability. The closest structure linked to dispersion includes only one selected variable, shots on goal per game, which was not selected in our final model. Therefore, the following discussion on variability in our model are pioneering and should be further explored in future studies. 

As the number of assists increases, so does the dispersion of the points ratio. Assists, that represent only passes that lead to score a goal, reflect a team’s offensive capability and tactical organization, which can have a direct impact on performance variability and, consequently, points earned throughout the matches. Studies such as Lago-Peñas et al. (2010) show that winning teams tend to have more assists, while Lago-Peñas and Lago-Ballesteros (2011) highlight that home advantage positively impacts this statistic. Thus, natural variation in the number of assists across different teams and game contexts may contribute to increased variability in the points ratio over the season. 

Shots against presented a negative relationship with the dispersion of points ratio (Figure 3(d)). Nakamura et al. (2019) identified a negative correlation between shots against and the points ratio (not the dispersion) in major European leagues, implying that teams facing more shots have a lower point rate and a higher chance of losing. Variation in the number of shots against during matches may be linked to variability in a team’s point rate, which contributes to reduce variability in South American soccer leagues. This is because teams that face more shots may exhibit more unpredictable performances, resulting in higher variability in their results. 

The impact of yellow cards on the dispersion of points ratio is roughly constant up to approximately 2.5 cards (Figure 3(e)). Beyond this threshold, however, a linear increasing trend emerges. This result suggests that a higher number of cautions directly impacts match instability. This upward trend may be attributed to extreme scenarios in which high aggressiveness causes greater uncertainty in match outcomes – whether due to imminent expulsions, tactical adjustments, or even a loss of emotional control 

L. F. Rosa et al.: Analyzing South American soccer team performance **— 9** 

among players. Kubayi (2020) found that losing teams are more likely to obtain yellow cards than winning teams. 

A positive relationship is also observed between the number of saves and the dispersion of the points ratio, indicating that the greater the average number of saves per game, the more dispersed the outcomes. This behavior appears expected, as teams that rely heavily on their goalkeeper are frequently under attack, making their results more unpredictable. Studies that include this variable in statistical models only consider its effect on the mean. For example, Andrzejewski et al. (2022) state that the number of saved shots is positively related to the final score. 

Finally, the relationship between dribbles and the dispersion of points ratio follows a highly erratic pattern (Figure 3(f)). There is a negative trend up to approximately nine dribbles per game, where variability reaches its lowest observed level. This is followed by an increase in variability up to 14 dribbles, at which point a sinusoidal pattern emerges, with the highest variability happening in matches with 25 dribbles. Liu et al. (2015) observed that dribbles had a clearly negative impact on match outcomes during the group stage of the 2014 FIFA World Cup. Similarly, Lago-Peñas and Lago-Ballesteros (2011) found that home teams performed significantly more dribbles than away teams in Spanish League. On the other hand Harrop and Nevill (2014) suggested that teams should make fewer passes and dribbles in the attacking phase while completing more successful passes and shots in order to succeed. Dribbling does not necessarily result in goal-scoring opportunities. These studies contribute to understanding the influence of dribble and its complex behavior in the dispersion of the points ratio. 

## **6 Conclusions** 

In this paper, we proposed the use of generalized additive models for location, scale, and shape (GAMLSS), also known as distributional regression models, to better understand the elements that influence the points ratio in three major South American soccer leagues over three seasons. This modeling approach is particularly important since nonlinear relationships between the covariates considered in the study and the response were identified. As a result, more conventional models would likely fail to effectively capture these patterns, rendering their inferences unreliable. Furthermore, we not only fitted a regression structure for the median points ratio but also identified factors that have a direct impact on data variability. 

Overall, as expected, the results reinforce that scoring goals and preventing goals – particularly achieving clean 

sheets – are the primary determinants of success in soccer. Additionally, the negative impact of fouls emphasizes the importance of disciplinary control during matches, while passing accuracy proves to be crucial for strong league performance. The nonlinear effect captured in the median structure fitted on the covariates tackles, saves, and red cards indicate the complexity of the relationships under study. 

The identification of variables that directly affect the dispersion of the points ratio highlights the need for more sophisticated models, such as GAMLSS. This is not only important from a statistical perspective – ensuring that the model meets all empirical assumptions – but also from a practical standpoint, as it provides broader understanding of how the variability in points unfolds over the course of a championship. 

Thus, this study contributes to the literature by providing a detailed analysis of the statistics that influence performance in South American soccer as a whole, enabling coaches and analysts to develop more precise strategies to improve team performance. Future research can investigate other variables and broaden the analysis to different competitive contexts, thereby improving our understanding of the factors that determine success in soccer. Although this study focused on three major South American leagues, the patterns observed in points ratio and team success are likely to hold in other leagues as well, suggesting that the findings may have broader applicability. Moreover, even though not considered in this paper, interactions between covariates could be explored to capture even more complex behaviors. However, while this would likely enhance predictive power, it would also reduce model interpretability. 

**Acknowledgement:** The authors are grateful to the Associate Editor and the Reviewers for their helpful comments and suggestions. 

#### **Research ethics:** Not applicable. 

#### **Informed consent:** Not applicable. 

**Author contributions:** All authors have accepted responsibility for the entire content of this manuscript and approved its submission. 

**Use of Large Language Models, AI and Machine Learning Tools:** ChatGPT (OpenAI) was used to improve the English language, grammar, and readability of the manuscript. **Conflict of interest:** The authors state no conflict of interest. **Research funding:** This study was financed in part by the Fundação de Amparo à Pesquisa do Estado de Minas Gerais (FAPEMIG) – Brazil. 

**Data availability:** The data that support the findings of this study are available in SofaScore at https://www.sofascore .com. 

> **10 —** L. F. Rosa et al.: Analyzing South American soccer team performance 

## **References** 

Aguado-Méndez, R.D., González-Jurado, J.A., Callejas-Jerónimo, J.E., and Otero-Saborido, F.M. (2021). Analysis of the goal-scoring opportunities conceded in football: a study case in the Spanish La Liga. _Qual. Quant._ 55: 1477−1496,. 

- Akaike, H. (1974). A new look at the statistical model identification. _IEEE Trans. Automat. Contr._ 19: 716−723. 

Almeida, C.H., Ferreira, A.P., and Volossovitch, A. (2014). Effects of match location, match status and quality of opposition on regaining possession in UEFA champions league. _J. Hum. Kinet._ 41: 203−214,. 

Andrzejewski, M., Oliva-Lozano, J.M., Chmura, P., Czarniecki, S., Kowalczuk, E., Rokita, A., Muyor, J.M., Konefał, M., and Konefał, M. (2022). Analysis of team success based on match technical and running performance in a professional soccer league. _BMC Sports Sci. Med. Rehabil._ 14: 82,. 

- Aquino, R., Munhoz, G.H.M., Vieira, L.H.P., and Menezes, R.P. (2017). Influence of match location, quality of opponents, and match status on movement patterns in Brazilian professional football players. _J. Strength Cond. Res._ 31: 2155−2161. 

Atchison, J. and Shen, S.M. (1980). Logistic-normal distributions: some properties and uses. _Biometrika_ 67: 261−272. 

Beck, H., Prinz, A., and van der Burg, T. (2022). The league system, competitive balance, and the future of European football. _Manag. Sport Leis._ 30: 21−44,. 

- Brown, M. (2014). British informal empire and the origins of association football in South America. _Soccer Soc._ 16: 169−182,. 

Brown, M., Elsey, B., and Wood, D. (2018). Football history in Latin America. _Bull. Lat. Am. Res._ 37: 537−538. 

Caliendo, M. and Radic, D. (2006). _Ten do it better, do they? An empirical analysis of an old football myth. IZA discussion papers, No. 2158_ . Institute for the Study of Labor (IZA), Bonn. 

- Castellano, J., Casamichana, D., and Lago, C. (2012). The use of match statistics that discriminate between successful and unsuccessful soccer teams. _J. Hum. Kinet._ 31: 139−147,. 

- Cerqueira, P.H., Nakamura, L.R., Pescim, R.R., and Leandro, R.A. (2017). Investigating the underlying causal network on European football teams. _J. Data Sci._ 15: 293−312,. 

Clemente, F.M., Martins, F.M.L., and Mendes, R.S. (2016). Analysis of scored and conceded goals by a football team throughout a season: a network analysis. _Kinesiol._ 48: 103−114,. 

Costa, F.J., Pescim, R.R., Nakamura, L.R., Urbano, M.R., Silva, V.C., and Ramires, T.G. (2025). Spatiotemporal analysis of urban land prices: a distributional regression approach. _Spat. Econ. Anal._ 20: 333−345,. De Bastiani, F., Rigby, R.A., Stasinopoulos, D.M., Cysneiros, A.H.M.A., and Uribe-Opazo, M.A. (2018). Gaussian markov random field spatial models in GAMLSS. _J. Appl. Stat._ 45: 168−186. 

Dunn, P.K. and Smyth, G.K. (1996). Randomized quantile residuals. _J._ 

_Comput. Graph. Stat._ 5: 236−244,. 

Eilers, P.H.C. and Marx, B.D. (1996). Flexible smoothing with B-splines 

and penalties. _Statist. Sci._ 11: 89−121,. 

Faedo, N.I. and Corrius, M. (2024). Lionel Messi as a global icon: the player as personal brand in the history of FC Barcelona. In: _FC Barcelona_ . Routledge, London, pp. 207−221. 

Ferrari, S. and Cribari-Neto, F. (2004). Beta regression for modelling rates and proportions. _J. Appl. Stat._ 31: 799−815,. 

Gümüşdaˇg, H., Yildiran, I., Yamaner, F., and Kartal, A. (2011). Aggression and fouls in professional football. _Biomed. Hum. Kinet._ 3: 67−71,. 

Harrop, K. and Nevill, A. (2014). Performance indicators that predict success in an English professional league one soccer team. _Int. J. Perf. Anal. Spor._ 14: 907−920,. 

- Heller, G.Z., Robledo, K.P., and Marschner, I.C. (2022). Distributional regression in clinical trials: treatment effects on parameters other than the mean. _BMC Med. Res. Methodol._ 22: 56,. 

- Hewitt, J.H. and Karakuş, O. (2023). A machine learning approach for player and position adjusted expected goals in football (soccer). _Frankl. Open_ 4: 100034,. 

- Hodges, J.S. and Sargent, D.J. (2001). Counting degrees of freedom in hierarchical and other richly-parameterised models. _Biometrika_ 88: 367−379,. 

- Jones, P.D., James, N., and Mellalieu, S.D. (2004). Possession as a performance indicator in soccer. _Int. J. Perf. Anal. Spor._ 4: 98−102,. 

- Kapsalis, M., Plakias, S., Kyranoudis, A., Zarkadoula, A., Lathoura, A., and Tsatalas, T. (2023). Exploring the impact of possession-based performance indicators on goal scoring in elite football leagues. _J. Phys. Educ. Sport._ 23: 2004−2015. 

- Kubayi, A. (2020). Analysis of goal scoring patterns in the 2018 FIFA world cup. _J. Hum. Kinet._ 71: 205−210,. 

- Kubayi, A. and Toriola, A. (2019). The influence of situational variables on ball possession in the South African premier soccer league. _J. Hum. Kinet._ 66: 175−181,. 

- Lago-Peñas, C., Lago-Ballesteros, J., and Rey, E. (2011). Differences in performance indicators between winning and losing teams in the UEFA champions league. _J. Hum. Kinet._ 27: 135−146,. 

- Lago-Peñas, C. and Lago-Ballesteros, J. (2011). Game location and team quality effects on performance profiles in professional soccer. _J. Sports Sci. Med._ 10: 465−471. 

- Lago-Peñas, C., Lago-Ballesteros, J., Dellal, A., and Gómez, M. (2010). Game-related statistics that discriminated winning, drawing and losing teams from the Spanish soccer league. _J. Sports Sci. Med._ 9: 288−293. 

- Liu, H., Gomez, M.A., Lago-Peñas, C., and Sampaio, J. (2015). Match statistics related to winning in the group stage of 2014 Brazil FIFA world cup. _J. Sports Sci._ 33: 1205−1213,. 

- Louzada, F., Suzuki, A.K., and Salasar, L.E.B. (2014). Predicting match outcomes in the English premier league: which will be the final rank? _J. Data Sci._ 12: 235−254,. 

- Malcata, R.M., Hopkins, W.G., and Richardson, S. (2012). Modelling the progression of competitive performance of an academy’s soccer teams. _J. Sports Sci. Med._ 11: 533−536. 

- Malikov, D. and Kim, J. (2024). Beyond xG: a dual prediction model for analyzing player performance through expected and actual goals in European soccer leagues. _Appl. Sci._ 14: 10390,. 

- Mao, L., Peng, Z., Liu, H., and Gómez, M.A. (2016). Identifying keys to win in the Chinese professional soccer league. _Int. J. Perf. Anal. Spor_ 16: 935−947,. 

- Markopoulou, C., Papageorgiou, G., and Tjortjis, C. (2024). Diverse machine learning for forecasting goal-scoring likelihood in elite football leagues. _Mach. Learn. Knowl. Extr._ 6: 1762−1781,. 

- Moura, F.A., Martins, L.E.B., and Cunha, S.A. (2014). Analysis of football game-related statistics using multivariate techniques. _J. Sports Sci._ 32: 1881−1887,. 

- Nakamura, L.R., Cerqueira, P.H.R., Ramires, T.G., Pescim, R.R., Rigby, R.A., and Stasinopoulos, D.M. (2019). A new continuous distribution on the unit interval applied to modelling the points ratio of football teams. _J. Appl. Stat._ 46: 416−431,. 

L. F. Rosa et al.: Analyzing South American soccer team performance **— 11** 

- Nakamura, L.R., Rigby, R.A., Stasinopoulos, D.M., Leandro, R.A., Villegas, C., and Pescim, R.R. (2017). Modelling location, scale and shape parameters of the birnbaumsaunders generalized t distribution. _J. Data Sci._ 15: 221−237,. 

- Obetko, M., Peráček, P., Mikulič, M., and Babic, M. (2022). Technical−tactical profile of an elite soccer goalkeeper. _J. Phys. Educ. Sport._ 22: 38−46. 

- Orchard, J. (2002). Is there a relationship between ground and climatic conditions and injuries in football? _Sports Med._ 32: 419−432,. 

- Perez-Arroniz, M., Calleja-González, J., Zabala-Lili, J., and Zubillaga, A. (2023). The soccer goalkeeper profile: bibliographic review. _Phys. Sportsmed._ 51: 193−202,. 

- Pratas, J.M., Volossovitch, A., and Carita, A.I. (2016). The effect of performance indicators on the time the first goal is scored in football matches. _Int. J. Perf. Anal. Sport_ 16: 347−354,. 

- Ramires, T.G., Nakamura, L.R., Righetto, A.J., Carvalho, R.J., Vieira, L.A., and Pereira, C.A.B. (2021a). Comparison between highly complex location models and GAMLSS. _Entropy_ 23: 469,. 

- Ramires, T.G., Nakamura, L.R., Righetto, A.J., Pescim, R.R., Mazucheli, J., and Cordeiro, G.M. (2019). A new semiparametric weibull cure rate model: fitting different behaviors within GAMLSS. _J. Appl. Stat._ 46: 2744−2760,. 

- Ramires, T.G., Nakamura, L.R., Righetto, A.J., Pescim, R.R., Mazucheli, J., Rigby, R.A., and Stasinopoulos, D.M. (2021b). Validation of stepwise-based procedure in GAMLSS. _J. Data Sci._ 19: 96−110,. 

- Rigby, R.A. and Stasinopoulos, D.M. (2005). Generalized additive models for location, scale and shape. _J. R. Stat. Soc., C: Appl. Stat._ 54: 507−554,. 

- Rigby, R.A., Stasinopoulos, M.D., Heller, G.Z., and De Bastiani, F. (2019). _Distributions for modeling location, scale, and shape: using GAMLSS in R_ . CRC Press, Boca Raton. 

- Rosales, R.A. and Tito, R.G. (2022). Sports marketing communications in South America. In: _Marketing communications and brand development in emerging economies volume I_ . Palgrave Macmillan, pp. 103−119. 

- Ryynänen, J., Junge, A., Dvorak, J., Peterson, L., Kautiainen, H., Karlsson, J., and Börjesson, M. (2013). Foul play is associated with injury incidence: an epidemiological study of three FIFA world cups (2002−2010). _Br. J. Sports Med._ 47: 986−991,. 

- Schulze, E., Julian, R., and Meyer, T. (2021). Exploring factors related to goal scoring opportunities in professional football. _Sci. Med. Footb._ 6: 181−188,. 

- Stafylidis, A., Michailidis, Y., Mandroukas, A., Gissis, I., and Metaxas, T. (2022). Analysis of goal scoring and performance indicators in the 2020-2021 Greek soccer league. _J. Phys. Educ. Sport._ 22: 91−99. 

- Sun, R., Wang, C., Qin, Z., and Han, C. (2024). Temporal features of goals, substitutions, and fouls in football games in the five major European league from 2018 to 2021. _Heliyon_ 10: e27014,. 

- Toledo, L.H. (2021). Garrincha, Pelé and Maradona: the sporting sacred in times of football icon veneration. In: _Football and social sciences in Brazil_ . Springer, Cham, pp. 243−261. 

- van Buuren, S. and Fredriks, M. (2001). Worm plot: a simple diagnostic device for modelling growth reference curves. _Stat. Med._ 20: 1259−1277,. 

- Vogelbein, M., Nopp, S., and Hökelmann, A. (2014). Defensive transition in soccer − are prompt possession regains a measure of success? A quantitative analysis of German Fußball-Bundesliga 2010/2011. _J. Sports Sci._ 32: 1076−1083,. 

- Voudouris, V., Gilchrist, R., Rigby, R., and Stasinopoulos, D. (2012). Modelling skewness and kurtosis with the BCPE density in GAMLSS. _J. Appl. Stat._ 39: 1279−1293,. 

- Wang, S.H., Qin, Y., Jia, Y., and Igor, K.E. (2022). A systematic review about the performance indicators related to ball possession. _PLoS ONE_ 17: e0265540,. 

- Wang, Z., Su, L.Agudamu, Gong, T., Bu, T., and Zhang, Y. (2024). Factors driving FIFA world cup 2022 viewership ratings in mainland China: marketing outlooks for FIFA World Cup 2026. _Front. Sports Act. Living_ 5: 1282898. 

- Watanabe, N., Wicker, P., and Yan, G. (2017). Weather conditions, travel distance, rest, and running performance: the 2014 FIFA World Cup and implications for the future. _J. Sport Manag._ 

   - 31: 27−43,. 

- White, A., Hills, S.P., Cooke, C.B., Batten, T., Kilduff, L.P., Cook, C.J., Roberts, C., and Russell, M. (2018). Match-play and performance test responses of soccer goalkeepers: a review of current literature. _Sports Med._ 48: 2497−2516,. 

- Yue, Z., Broich, H., and Mester, J. (2014). Statistical analysis for the soccer matches of the first Bundesliga. _Int. J. Sports Sci. Coach._ 9: 553−560,. 

- Zhao, Y.Q. and Zhang, H. (2019). Analysis of goals in the English Premier League. _Int. J. Perf. Anal. Spor._ 19: 820−831,. 


