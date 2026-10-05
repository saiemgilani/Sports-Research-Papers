<!-- source: library/journals/Wharton Sports Analytics Journal/2022/2022 - Optimal Pitch Spin Rate and Velocity to Maximize Whiff Rate - Park et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/optimal-pitch-spin-rate-velocity-to-maximize-whiff-rate/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2022 -->
<!-- authors: Minsoo Park; Richard Yang; Neil Rowe; Wesley Fletcher -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Optimal Pitch: Spin Rate & Velocity to Maximize Whiff Rate

By: Minsoo Park, Richard Yang, Neil Rowe, and Wesley Fletcher

Research Hypothesis: Spin rate and velocity will affect the whiff rate

Null Hypothesis: Spin rate and velocity have no correlation with whiff rate and the data is because of chance

## Background

More Background

- Common Belief: Throwing Harder leads to whiﬀs

- Not much correlation between velocity and whiﬀ rate - r (4 seamers vs. whiﬀ rate)=.273 - r (Sinkers vs. whiﬀ rate)=.323 - r (Sliders vs. whiﬀ rate)=.0079 - r (Changeups vs. whiﬀ rate)=.0766

- Examples - Andres Munoz has on average the fastest fastball in the majors, but a pedestrian whiﬀ rate - Tyler Clippard barely averages 90 mph on his fastball, but has one of the best whiﬀ rates in baseball

If more velocity doesn’t lead to more whiﬀs, then is spin the key factor that aﬀects a pitcher’s ability to miss bats?

Pitcher 1: Mike Minor

- Low Velo, High spin rate

- For all of his pitches, his average velocity clocked in at around 86.93 mph

- However, his average spin rate maintained a high 2502.36 rpm

- Among the players we used in our data, Minor had the 5th highest fastball spin rate, 8th highest changeup spin rate, and 29th highest slider spin rate

Pitcher 2: Nathan Eovaldi

- High velo, Low spin rate

- Four-seam fastball average of 97.5 mph in 2019

- Cutter averaged 93.2 mph - However, his fastball spin rate was below average with 2186 rpm - His curveball spin rate was well below average at 2174 rpm

Inquiry

Q: Any other factors that impact whiﬀ rate? And if any, to what extent? - Velocity - Spin rate - “Combination” of pitch repertoire

Univariate Regression showed not much correlation, but…. We still need to perform multivariate regression!

Basic stat info.

Mean: 𝚺Xi / N (𝜇) Standard deviation: {𝚺(Xi - Mean)2 / N}0.5 (𝜎) Variance: (Standard deviation)2 (𝜎2) RMSE: {𝚺(yi - ŷi)2 / N}0.5 (ŷ = predicted value of y) R-squared: 1 - (SSRegression / SSTotal) where SSRegression = 𝚺(yi - ŷi)2 and SSTotal = 𝚺(yi - ȳi)2 (ȳ = mean of y) Z-score: (X-mean) / S.D.

Univariate Linear Regression Model

Univariate Linear Regression Hypothesis: Parameter: Cost Function: Aim/Goal: to minimize cost

*** h(x) = Ŷ, 𝛉n = Parameters, xn = Features (only 1 feature), y(i) = Actual Output Estimate unknown parameters for given x

Multivariate Regression Model

Exact same process as univariate linear regression, but with multiple features Hypothesis:

Parameter: Cost Function: Aim/Goal: to minimize cost

Step 1: Data crawling process

- Data gathered from statcast

- Crawled data that was in table format by converting it into .csv ﬁles

Step 2: Merging Data Frames

After reading all of the .csv ﬁles for each pitch type, we merged all 7 data frames into 1 master dataframe using the function “rbind”

Step 3: Mean Normalization (Z-Scores)

In regression, it is better to keep the values of all features within certain boundary (ex: between -1 and 1). But since artiﬁcially altering features is not recommended, decided to use feature scaling: Mean normalization method

Mean normalization: xi = Data, 𝜇i = Average (mean) of population, Si = S.D. For our dataset (FullData):

- Velo mean: 89.19 mph / Velo S.D.: 5.47 mph - Spin rate mean: 2262.22 rpm / Spin rate S.D.: 284.83 rpm

Step 4: Filtering

In order to remove outliers from our data that may skew our graph, we constrained our data points to exclude points that we found to be way too extreme.

We repeated this for all the types of pitches by using the ﬁlter() function on our dataframe

Example: Filtering by Changeup Pitches

Step 5: Regression

Since we are dealing with both spin rate and velocity…. Using the linear model “lm()” function, we found the summary of our multivariable regression, which showed that….

Multiple Regression Findings

- The p-value was extremely low, a sign that our ﬁndings were in fact statistically signiﬁcant

- The correlation was pretty high compared to the values we observed earlier with the univariate regression model r = 0.5012

Plotting Data

Using the facet_wrap() function with the ggplot() function, we created graphs for each pitch type comparing spin rate and whiﬀ rate

Plotting Data Cont.

In addition, we added the mean lines for the x-axis (pitch stat) and y-axis (whiﬀ rate) with the geom_vline() and geom_hline() functions

Multivariate Plots For Each Pitch Type (3D)

All Pitches

Trend:

- As Spin Rate goes up, so will the whiﬀ rate

- As Velocity goes up, the whiﬀ rate will go down

Optimization: High Spin, Low Velocity (but probably due to breaking balls having lower velo and higher whiﬀ rates => “Simpson’s Paradox”)

3D Plots

## 4 Seamer

Trend:

- As Spin Rate goes up, the whiﬀ rate increases

- As Velocity goes up, the whiﬀ rate increases

Optimization: (+, +)

3D Plots

Curveball

Trend:

- As Spin Rate goes up, the whiﬀ rate stays constant

- As Velocity goes up, the whiﬀ rate increases

Optimization: (null, +)

3D Plots

Changeup

Trend:

- As Spin Rate goes up, the whiﬀ rate increases

- As Velocity goes up, the whiﬀ rate increases

Optimization: (+, +)

3D Plots

Slider

Trend:

- As Spin Rate goes up, the whiﬀ rate increases

- As Velocity goes up, the whiﬀ rate stays constant

Optimization: (+, null)

3D Plots

Cutter

Trend:

- As Spin Rate goes up, the whiﬀ rate increases

- As Velocity goes up, the whiﬀ rate decreases

Optimization: (+, -)

Mike Minor Z-scores (amongst MLB pitchers)

4-seamer:

● Spin rate: 2.26 ● Velocity: -0.49

Curveball:

● Spin rate: -0.13 ● Velocity: 0.54

Changeup:

● Spin rate: 1.93 ● Velocity: 0.57

Slider:

● Spin rate: 1.28 ● Velocity: 0.46

Practical Optimization: Minor

To maximize Minor’s whiﬀ rate against batters:

## 4 Seamer:

- Already high spin rate - Increase his velocity

Curveball:

- Spin rate has minimal eﬀect - Increase his velocity

To maximize Eovaldi’s whiﬀ rate against pitchers, we had to:

Changeup:

- Already high spin rate - Increase his velocity

Slider:

- Increase his spin rate a bit - Velocity has minimal eﬀect

Nathan Eovaldi Z-scores (amongst MLB pitchers)

4-seamer:

● Spin rate: -0.73 ● Velocity: 1.65

Curveball:

● Spin rate: -1.51 ● Velocity: 0.48

Cutter:

● Spin rate: -0.05 ● Velocity: 1.79

Slider:

● Spin rate: -0.84 ● Velocity: -0.28

Practical Optimization: Eovaldi

To maximize Eovaldi’s whiﬀ rate against batters:

## 4 Seamer:

- Increase his spin rate - Already high velocity

Curveball:

- Spin rate has minimal eﬀect - Increase his velocity

To maximize Eovaldi’s whiﬀ rate against pitchers, we had to:

Cutter:

- Increase his spin rate - Decrease his velocity***

Slider:

- Increase his spin rate - Velocity has minimal eﬀect

## Conclusion

Our Conclusion: The best pitches have both high velocity and spin rate

That’s why Gerrit Cole and Justin Verlander are great while Mike Minor and Nathan Eovaldi are average pitchers

THANKS FOR LISTENING
