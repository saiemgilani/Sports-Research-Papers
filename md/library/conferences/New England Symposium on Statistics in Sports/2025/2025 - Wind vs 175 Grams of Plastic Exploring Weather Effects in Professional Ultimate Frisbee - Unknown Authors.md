<!-- source: library/conferences/New England Symposium on Statistics in Sports/2025/2025 - Wind vs 175 Grams of Plastic Exploring Weather Effects in Professional Ultimate Frisbee - Unknown Authors.pdf -->

**Wind vs 175 Grams of Plastic: Exploring Weather Effects in Professional Ultimate Frisbee** Jacob Miller, Braden Eberhard 



# **Motivation** 

# **Impact on Foundation Models** 

The recent growth of analytics in professional ultimate frisbee has significantly advanced our understanding of team and player performance. However, current modeling approaches overlook one of the sport’s most influential contextual factors: weather. Wind can alter gameplay by increasing throw difficulty, lowering completion rates, and reducing scoring probability, which complicates fair evaluation across games. Players and coaches frequently cite weather, particularly wind, as a major factor in poor outcomes, often attributing missed throws and strategic adjustments to environmental conditions rather than executional errors. 

There are two primary models used for evaluation in ultimate frisbee: 

- The **Completion Probability** (CP)  model which estimates the probability of a successful pass, factoring in thrower/receiver positioning, throw features, and game situation. 

- The **Field Value** (FV) model which assigns a value to each position on the field, reflecting the probability of scoring using thrower location and game state. 

Incorporating wind-related covariates to both models significantly improves overall model fit (p << 0.01 in an ANOVA of nested model comparisons). Model selection criteria also support this improvement, as both the Akaike Information Criterion  and the Bayesian Information Criterion decreased, indicating that the gain in explanatory power justifies the added model complexity. Both CP and FV were fit using GAMs. 

## **Data:** 

This study examined a 

comprehensive play-by-play dataset from the Ultimate Frisbee Association (UFA), covering five professional seasons with 400,000+ throws across 755 games combined with historical weather data collected via Open-Meteo. 



# **The Effect of Wind** 

Two primary effects were observed as wind speed increased: 1) players change the way they throw, and 2) players have a harder time completing equivalent throws in low winds. 

Integrating wind covariates into the **CP** model produced distance- and wind-dependent adjustments to the Expected Completion Percentage (xCP) of individual throws. 





Wind speed had little effect on the distribution of long throws. However, in windy games, players keep 6% more of their throws within 10 yards, shifting the balance of short and medium passes as conditions change. 

The data reveals a **10 percentage point swing** in long throw success based on weather. Compared to the average, completion rates for long throws **drop by 7%** in windy conditions but **climb by 3%** on calm days. 

Wind affects long throws much more than short throws. Short throws maintain similar completion rates regardless of wind conditions, but longer throws become increasingly difficult to complete as wind speed increases. Over the course of a game these small changes in risk compound, translating into significantly different outcomes. 



<!-- Start of picture text -->
Leveraging wind data to the  FV<br>model shows that strong wind<br>substantially impacts offensive<br>efficiency.<br>In high winds, the chance of<br>scoring from any given spot on the<br>field  drops by about 5%.  In<br>practical terms, playing in strong<br>wind is comparable to a 10-yard<br>penalty: a team must gain an<br>additional  10 yards  to preserve the<br>same scoring probability they<br>would have under calm<br>conditions.<br><!-- End of picture text -->



# **Contact Info** 



**Website:** shownspace.com **Email:** shownspace.analytics@gmail.com **Substack:** shownspace.substack.com 


