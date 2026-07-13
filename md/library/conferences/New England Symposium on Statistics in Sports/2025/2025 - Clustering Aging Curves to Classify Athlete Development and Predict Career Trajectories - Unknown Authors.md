<!-- source: library/conferences/New England Symposium on Statistics in Sports/2025/2025 - Clustering Aging Curves to Classify Athlete Development and Predict Career Trajectories - Unknown Authors.pdf -->

The predicted aging curve of Usain Bolt in the 100m. 

**Clustering Aging Curves to Classify Athlete Development and Predict Career Trajectories** 

David Awosoga, Yushi Liu, and Samuel WK Wong Department of Statistics & Actuarial Science, Faculty of Mathematics 

# **Introduction** 

Athletes achieve peak performance at highly variable rates: some progress rapidly, while others improve gradually over longer careers. Unlike team sports, track and field results are objectively measured and comparable across events through the World Athletics scoring system<sup>1</sup> . By modeling aging curves using functional data analysis, we aim to classify athlete development patterns and provide predictive insights into career trajectories. 

# **Objective** 

We apply Functional Principal Components Analysis (FPCA)<sup>2</sup> and informatively missing FPCA (imFunPCA)<sup>3</sup> to model athlete aging curves, correct for right tail selection bias, and extract dominant progression patterns. Athletes are clustered at both the population level and by event type using the percent change of World Athletics points to capture different rates of progression. These clusters provide predictive insights into when athletes are likely to reach elite standards based on early career performance. 



Career Progression for 800m Olympic Champions, highlighting the sparse and uneven distribution of observations. 







**Methodology** We modeled athlete aging curves using functional data analysis. FPCA was applied to smooth uneven competition results and identify dominant progression patterns. To address right tail selection bias, we used imFunPCA, which assumes athletes cannot surpass their last observed performance after exiting competition. Clustering was then performed on the percent change of World Athletics points, at both the population and event level, to group athletes with similar developmental trajectories. **Predictive Modeling Results** 



Histogram of performance ages across all athletes. 

**Data** performed on the percent change of World We use **seasons-best performances** of Athletics points, at both the population and Olympic track and field Athletes from event level, to group athletes with similar World Athletics<sup>4</sup> . Results are standardized developmental trajectories. into **World Athletics points** using the **Predictive Modeling** World Athletics scoring system<sup>4</sup> , enabling **Results** comparisons across disciplines such as FPCA and imFunPCA produced smoothed sprints, jumps, and throws. Analyses cover aging curves that captured both dominant performance ages 11 to 58. Each athlete’s progression patterns and realistic late career competition history forms an aging curve, declines. Clustering on the percent change of and athletes competing in multiple events World Athletics points, validated through contribute separate trajectories for eventscree plots and cross validation, identified specific clustering. seven optimal clusters. These clusters **Exploratory Data Analysis** revealed distinct developmental profiles such Athlete performance results show as early risers, steady performers, and late considerable irregularity. Some athletes bloomers, providing insight into how athletes compete frequently while others have progress toward elite standards at different sparse participation, leading to uneven data rates. across ages. Career lengths also vary, with less successful athletes dropping out earlier, creating a right tail selection bias. We computed average Tokyo 2025 World Championships standards across events for men and women, allowing us to examine when athletes typically reach elite benchmarks. These patterns motivate the need for advanced modeling methods. Middle Distance Clustering using FPCA **References:** _40_ (3), 712–724. https://doi.org/10.1002/sim.8798. 1. Awosoga, D. (2024). Peaks and primes: Do athletes get one shot at glory? 4. World Athletics. (n.d.). _World Athletics_ . https://worldathletics.org _Significance, 21_ (3), 6–9. https://doi.org/10.1093/jrssig/qmae038. 5. Crainiceanu, C. M., Goldsmith, J., Leroux, A., & Cui, E. (2024). _Functional Data_ 2. Ramsay, J. O., & Silverman, B. W. (2005). _Functional data analysis_ (2nd ed.). _Analysis with R_ (1st ed.). Chapman & Hall/CRC. . Springer. https://doi.org/10.1201/9781003278726 3. Shi, H., Dong, J., Wang, L., & Cao, J. (2021). Functional principal component analysis for longitudinal data with informative dropout. _Statistics in Medicine,_ 



**Case Study: Usain Bolt** Usain Bolt’s aging curve highlights the importance of censor aware modeling. The imFunPCA trajectory captures his sharp late career decline, while sparse FPCA smooths results but unrealistically sustains performance by ignoring censoring. This example demonstrates how imFunPCA provides a more accurate representation of athlete progression and underscores the value of accounting for selection bias in predictive modeling. **Future Extensions** Future work could extend this analysis using **Multilevel Functional Data Analysis**<sup>5</sup> to model multiple observations per athlete, capturing both between athlete and within athlete variability. Incorporating **training history, injury data, and external factors** may improve predictive accuracy. We are also developing an **interactive Shiny application** that visualizes FPCA based predictions of aging curves and athlete comparisons. A future goal is to integrate censor aware models such as imFunPCA, making the tool more robust for coaches and analysts. 

**Acknowledgements:** This work was made possible via collaboration within the University of Waterloo Analytics Group for Games and Sports (UWAGGS). A special thank you to Rithika Silva for his extensive support acquiring the data. 

**Check out the Shiny app here!** 


