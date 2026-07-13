<!-- source: library/conferences/New England Symposium on Statistics in Sports/2025/2025 - Analyzing Movement Dynamics in Elite Female Soccer Athletes - Unknown Authors.pdf -->

Analyzing Movement Dynamics in Elite Female Soccer Athletes Full Kendall Thomas1 and Jan Hannig1 Paper 1Department of Statistics and Operations Research, University of North Carolina at Chapel Hill, Chapel Hill, NC 27599Department of Statistics and Operations Research, University of North Carolina at Chapel Hill, Chapel Hill, NC 27599 





<!-- Start of picture text -->
1Department of Statistics and Operations Research, University of North Carolina at Chapel Hill, Chapel Hill, NC 27599Department of Statistics and Operations Research, University of North Carolina at Chapel Hill, Chapel Hill, NC 27599<br><!-- End of picture text -->





<!-- Start of picture text -->
Methods<br><!-- End of picture text -->

- Methods 

- **Data Object** : **Quantile Cube** • A 3-D summary of athlete movement distributions 

- • <u>Dimensions:</u> velocity, acceleration, angle 

- • Discretized into quantiles: 5 velocity × 5 acceleration × 4 angle • Angle offset: starts from -30º 

Introduction 

**Motivation:** Understanding complex movement dynamics is key to optimizing performance and managing load in elite women’s soccer. Traditional analyses, however, often overlook the multidimensional nature of athlete movement data. 

**Goal** : Develop interpretable statistical models that quantify movement patterns in elite women’s soccer and assess their links to athlete performance and match outcomes. : **Approach** 1. Construct a 3D _quantile cube_ (velocity, acceleration, and angle). 2. Compare movement distributions across match halves. 3. Apply dimensionality reduction to movement patterns in match contexts. 4. Model movement distributions as a function of athlete and match characteristics. 





<!-- Start of picture text -->
Fig 2.  Angle<br>Quantile<br>Representation<br><!-- End of picture text -->

## **Construction:** 

- Quantile cube created for each athletematch-half from full-dataset quantiles → 5 × 5 × 4 = 100-dimensional vector 



<!-- Start of picture text -->
Methods<br><!-- End of picture text -->

   - Represents either deciseconds or proportion of total time spent in each movement category 

   - • : 𝒀 

   - Resulting dataset 𝒏=𝟑𝟗𝟔 × 𝒅=𝟏𝟎𝟎 

- **Data** : • GPS data from 9 elite female soccer athletes across both halves of 23 matches • 1Hz: timestamp, longitude, latitude 

- • Included athletes >25 min/half in ≥5 matches → 396 unique athlete-match-halves 

- • <u>Covariates: Match- and athlete-level features for</u> each athlete-match-half, stored in 𝑿 𝒏 × 𝒓=𝟏𝟑 



## : **Processing & Metrics** 

- 𝑥, 

- Transformed coordinates to into ( 𝑦) coordinates in meters and fit a 3<sup>rd</sup> degree spline 

- • Calculated velocity, acceleration, and angle (180º to 180º) from the spline 

- • Set velocities < 0.01 m/s and accelerations 

- < 0.001 m/s² to 0, then log-transformed values 

**Fig 3.** Quantile Cube for Athlete 5 Match 10 1<sup>st</sup> Half 









<!-- Start of picture text -->
Results<br><!-- End of picture text -->

- Results 

- **1. Quantify Differences Between Match Halves** • Using Hellinger distance, movement distributions differ significantly between the 1<sup>st</sup> and 2<sup>nd</sup> half for each player in every match. (see Fig. 4) 

**2. Reduce Dimensionality of Movement Patterns** • <u>Principal Component Analysis (PCA) reduces</u> the 100-dimensional movement data to 7 components explaining 90% of variance. 

• <u>PC1: Captures a shift toward polarized</u> movement in Match 1’s 2<sup>nd</sup> half, with less time in moderate-intensity movements 



**Fig 5.** Histogram of PC1 Scores • <u>PC4: Highlights Match 23’s unique pattern,</u> with increased low-velocity, highacceleration movements **Fig 6.** Histogram of PC4 Scores **3. Model Movement Distributions** • Relate athlete movement distributions to - contextual factors using <u>Dirichlet</u> multinomial regression (DMR) • For each athlete-match-half 𝑖, the movement distribution is modeled as a 𝒚𝒊 draw from a Dirichlet-multinomial (DM) **.** distribution parameterized by 𝜼𝒊 • Each category 𝑗 has a concentration parameter 𝑟 𝑥 𝜂 = exp 𝛽 + 𝛽 𝑖𝑘 𝑖𝑗 𝑗0 𝑗𝑘 ෍ 𝑘=1 linking covariates to the proportion of time spent in that category. 

# Results 

<u>DMR Model: half, log(playing time), and position group</u> 





**Fig 7.** DMR Coefficients for 2<sup>nd</sup> Half (Baseline Category: 1<sup>st</sup> Half) and log(Playing Time) 





**Fig 8.** DMR Coefficients for Position Groups (Baseline Category: Defender) 

- Conclusions & 

- Future Directions 

- The quantile cube effectively captures multidimensional movement dynamics, providing interpretable workload analytics. • Movement distributions shifted significantly between halves, indicating potential acute fatigue or tactical shifts. 

- PCA and DMR reveal role- and context-specific movement signatures, supporting probability-based monitoring for tailored training and recovery. 

- **Future** : • Integrate longitudinal, multimodal data (IMU, RPE, wellness data) 

- Validate the framework in real-world settings 

# Acknowledgements 

We extend our gratitude to Elena I. Cantú, Sam R. Moore, and Dr. Abbie E. Smith-Ryan from the Applied Physiology Lab in the University of North Carolina at Chapel Hill’s Department of Exercise and Sport Science for their generous contributions in gathering and providing access to the data. 

**Fig 1.** Left: Raw GPS data over 50 sec. Right: Interpolating spline for the same 50 sec. 

**Fig 4.** Quantile Cubes for Athlete 3 in the 1<sup>st</sup> and 2<sup>nd</sup> Halves of Match 12 


