<!-- source: library/journals/Journal of Sports Science and Medicine/2026/2026 - A Drone-Based Method to Measure Sprint Force-Velocity Profiles in 30-Meter Sprint Test - A Pilot Study - Wang et al.pdf -->

©Journal of Sports Science and Medicine (2026) **25,** 536-546 http://www.jssm.org DOI: <mark>https://doi.org/10.52082/jssm.2026.536</mark> 

**<mark>`</mark> Research article** 

# **A Drone-Based Method to Measure Sprint Force-Velocity Profiles in 30-Meter Sprint Test - A Pilot Study** 

**Fahui Wang**<sup>**1**</sup> **, Christophe Hautier**<sup>**1**</sup> **, Lin Song**<sup>**2**</sup> **, Yong Zhou**<sup>**2**</sup> **, Brice Guignard**<sup>**1**</sup> **, Paul Glaise**<sup>**1**</sup> **and Qingshan Zhang**<sup>**2,1**</sup> 

> **1** Université Lyon 1, LIBM, UR 7424, Villeurbanne, France 

> **2** School of Athletic Performance, Shanghai University of Sport, Shanghai, China 

### **<mark>Abstract</mark>** 

The objective was to determine the test-retest reliability and concurrent validity of a drone system in comparison to a radar device. Seventeen male collegiate soccer players participated in two maximal 30-meter sprint runs. The test-retest reliability of the drone system was evaluated using intraclass correlation coefficients (ICC3,1), coefficient of variation (CV%), and standard error of measurement (SEM). Subsequently, the systematic bias and consistency of the two devices on various force-velocity (F-V) variables (e.g., maximal velocity [Vmax], theoretical maximal horizontal velocity [V0], theoretical maximal horizontal force [F0], the slope of the F-V relationship [SFV]) were evaluated using linear mixed model (LMM) and Bland-Altman analysis. The drone system demonstrated moderate to excellent test-retest reliability across all variables (0.59 ≤ ICC ≤ 0.95; CV% < 10%). While LMM analysis detected significant systematic differences for Vmax ( _p_ = 0.013) and V0 ( _p_ = 0.012), Bland-Altman analysis confirmed high practical agreement with minimal bias (≤ 1.12%) and narrow limits of agreement (LoA < 10%). Pmax, split times (T5m– T20m) and average accelerations (A10m–A20m) demonstrated greater consistency (%Bias ≤ 1.54%) with no significant systematic bias ( _p_ > 0.05). Conversely, early-acceleration and modelderived metrics ( _Tau_ , Amax, F0, SFV) exhibited significant bias ( _p_ ≤ 0.028) and wide LoA exceeding 10% (e.g., F0: -13.37% to 8.56%; SFV: -11.54% to 18.18%). In conclusion, although the drone system exhibits high monitoring value in the maximum speed phase, early-acceleration metrics (e.g., Amax, F0, and T5m) should be interpreted with caution for individual-level monitoring. The tracking instability during the early acceleration phase necessitates further algorithm optimization. 

**Key words:** Computer vision, acceleration, performance, reliability. 

## **Introduction** 

High intensity actions in soccer encompass a broad spectrum of movements, including curvilinear sprints (Grazioli et al., 2024), change of direction actions (Morgan et al., 2022), and decelerations (Harper et al., 2019; Silva et al., 2023; Morgans et al., 2025); however, linear advancing motion (e.g., sprint) is the most frequently performed action before scoring in soccer games (Faude et al., 2012; Martínez-Hernández et al., 2023). Sprint test is widely used in practice as part of a testing battery (Dobbin et al., 2018; Taylor et al., 2022; Asimakidis et al., 2024). A deep understanding of the mechanics of sprint running is crucial not only for evaluating athletic performance but also as a key 

factor in injury prevention (Morin et al., 2015; Mendiguchia et al., 2016; Edouard et al., 2021). 

Since the development of a simple method for estimating sprint mechanical properties (Samozino et al., 2016), a growing body of research has adopted this approach to assess athletes' sprint force-velocity (F-V) profiles (Zhang et al., 2021; Galantine et al., 2023; AlonsoCallejo et al., 2024). Concurrently, numerous studies have investigated the validity and reliability of different measurement devices—such as radar device (Simperingham et al., 2019), laser gun (Ghigiarelli et al., 2022), mobile phone application (de Barros Sousa et al., 2025), GPS device (Clavel et al., 2022), photocell (Haugen et al., 2020), and linear encoder (Feser et al., 2022)—for determining these F-V variables in athletic populations. Although more affordable than laboratory equipment, radars, photocells, and GPS devices remain financially burdensome for grassroots clubs and face practical limitations. Photocells provide only sparse data, compromising the precision of F-V relationship analysis. While radar accurately measures peak speed (Beato et al., 2018; Ellens et al., 2025), it restricts tracking to a single athlete, whereas vision-based drone systems offer the potential for simultaneous multi-athlete tracking. Similarly, the accuracy of GPS devices is compromised by satellite signal quality and frequency limitations. 

Recent advances in computer vision have led to significant improvements in object detection algorithms. Computer vision technology has been widely adopted in autonomous vehicles (Zablocki et al., 2022) and industrial automation (Haffner et al., 2024), with rapidly growing applications in sports (Host and Ivašić-Kos, 2022). In these sports applications, a critical methodological distinction exists between pose estimation models and bounding boxbased tracking. Pose estimation models focus on the localization of specific anatomical landmarks to track individual body segments for biomechanical analysis (e.g., Della Villa et al., 2022; Straub and Powers, 2022). Conversely, bounding box approaches identify the athlete as a single entity—often utilizing segmentation algorithms to distinguish movement from a static background—to quantify global displacement parameters such as instantaneous velocity (e.g., Saini et al., 2019; Reveret et al., 2020; Tran et al., 2024). Currently, drones have been applied in various sports for performance monitoring and tactical analysis (Reveret et al., 2020; Russomanno et al., 2022; Tran et al., 2024). Compared to traditional fixed cameras, drone-based 

Received: 29 April 2026 / Accepted: 31 May 2026 / Published (online): 01 June 2026 

Wang et al. 

537 

tracking systems can effectively overcome the perspective limitations of fixed cameras (Tran et al., 2024). These applications support the potential of drone technology for velocity assessments in dynamic sports scenarios. 

To expand current testing methodologies, we propose an integrated motion analysis approach (hereafter referred to as the drone system) combining drone-based aerial videography with a computer vision model to track players performing 30-meter maximal sprints. We hypothesized that i) the sprint F-V profile variables derived from the drone method would exhibit acceptable test-retest reliability; ii) the sprint F-V profile variables calculated from the drone would exhibit a high level of agreement compared with the radar system. 

## **Methods** 

### **Participants** 

Seventeen male collegiate soccer players (age: 19.3 ± 1.4 yrs; body mass: 72.1 ± 8.0 kg; height: 177.0 ± 6.4 cm) provided written informed consent prior to participation. The study was approved by the local ethics committee of Shanghai University of Sport, in accordance with the standards of the Declaration of Helsinki (Approval Number: 102772025RT187). 

### **Sample size** 

The sample size for this study was determined a priori based on the primary study hypothesis regarding the testretest reliability of the drone system. According to the reliability sample size calculation method proposed by Walter et al. (1998), the minimum acceptable reliability (null hypothesis) was set at an intraclass correlation coefficient (ICC) of 0.50, corresponding to the threshold for poor reliability (Koo and Li, 2016). Aiming for an excellent level of reliability, the expected ICC (alternative hypothesis) was set at 0.90. With an alpha level of 0.05, a statistical power of 80%, and two repeated testing trials, a minimum of 13 participants was required. 

### **Procedures** 

All participants wore the same soccer boots they wore in daily training on an outdoor artificial turf field during afternoon training hours. After an identical warm-up (jogging, dynamic stretching, and three progressive submaximal sprints), each participant performed two 30-meter maximal sprints. Sprints began from a stationary split stance 50 cm behind the starting line, with no countermovement permitted, and were separated by a 3-minute recovery period. 

A Stalker ATS II radar system (Applied Concepts Inc., Dallas, TX, USA) was positioned on a tripod (0.9 m above the ground) approximately 5 m behind the start line, consistent with the placement protocols used in previous sprint profiling studies (Fornasier-Santos et al., 2022; Vantieghem-Nicolas et al., 2023). The study employed a DJI Air 3s Drone (SZ DJI Technology Co., Ltd.) with a DJI RC controller. Videos were captured at 60 Hz (4K resolution: 3840 × 2160 pixels) using a fixed 24 mm focal length lens without zoom, under clear weather conditions. All flights were conducted in a legally compliant area in accordance 

with local drone regulations, and the drone was operated by an experienced pilot throughout the data collection process. A 30×2 m rectangular runway was marked out using training cones, while the drone maintained stable hovering at 32 m altitude above the central test point (Figure 1). Recording commenced prior to the test, with the flight sequence documented for post-processing. Four backup batteries ensured continuous operation, with tests paused for battery replacement before depletion (approximately 30minute flight time per battery). 



**Figure 1. Experimental setup of the sprint testing sessions. The blue markers (A, B, C, and D) define a 30×2 m rectangular sprinting corridor.** 

### **Data Processing** 

### **Radar data processing** 

Raw radar data were acquired at 46.875 Hz using a customized software (MookyStalker v3.0.21). The raw radar data outliers were manually deleted following established methods from a previous study (Simperingham et al., 2019). 

### **Video data processing** 

All drone-based video processing tasks were executed in a Python 3.12.7 computational environment. The analysis pipeline was implemented using OpenCV (v4.11.0), NumPy (v2.1.2), and PyTorch (v2.7.0). The data processing workflow comprised the following six sequential stages (see the pipeline overview in Figure 2): 

_(1) Video segmentation._ The recorded videos were segmented into 10-second clips based on the test recordings. 

_(2) Video stabilization._ A video stabilization algorithm combining AKAZE feature detection (Accelerated KAZE), FLANN feature matching (Fast Library for Approximate Nearest Neighbors), and the homography matrix was employed to mitigate shake caused by minor movements and rotations, or scale variations (due to altitude fluctuations) during filming for each video segment. 

_(3) Object detection model training._ A single-stage object detection model (YOLOv8s, https://docs.ultralytics.com/models/yolov8/) was then trained to recognize players from a bird’s-eye view. The YOLOv8s model was initialized with pre-trained weights from Ultralytics. To ensure robust athlete detection under various dynamic postures, a total of 3,200 annotated images were utilized for model fine-tuning. These images were randomly extracted 

538 

Drone-based sprint profiling 

from the 30-meter sprint trials as well as supplementary athletic tests conducted concurrently with the same cohort of participants. The dataset was partitioned into training (70%, n = 2,240), validation (20%, n = 640), and testing (10%, n = 320) sets. 

_(4) YOLOv8s-based athlete tracking._ The trained model was utilized to track the geometric center of the bounding box for each athlete. 

_(5) Coordinate transformation._ The positional coordinates in the videos were mapped to real-world coordinates using a perspective transformation algorithm, based on calibration markers placed on the ground. Calibration rectangles, sized at 30×2 m, were manually annotated, and the homography matrix was optimized using the perspective transformation algorithm to ensure robust mapping (Figure 2). 

_(6) Velocity calculation._ The raw time-position data extracted from the video system was subsequently processed into time-velocity data (Figure 3) for calculating sprint F-V profiles. Given that the focus of this study is on 30-meter sprint, which aligns with a single direction (the X-axis), we exclusively utilized X-position data for calculation. To mitigate the impact of measurement error on speed, we adopted the method proposed in Wu and Swartz 

(2023) by adjusting the time increment Δ in Equation 1. 



where 𝑠̂�𝑡� is the estimated velocity (mꞏs<sup>-1</sup> ) at time 𝑡; x��� and x��� are the X-axis positions (m) at times 𝑡�Δ and 𝑡�Δ, respectively; and 2Δ indicates the duration of the time window used for the velocity calculation. In the present study, Δ was set to 0.25 s (15 frames at the 60 Hz sampling rate). By computing velocity over this extended time window (2Δ = 0.5 s), we effectively reduced the impact of data noise on instantaneous speed estimates, thereby obtaining more stable and reliable athlete speed profiles. 

### **Sprinting F-V profile** 

A customized MATLAB script (version R2021a; MathWorks, Inc., Natick, MA, USA) was developed to compute individualized linear F-V profiles by implementing an exponential model fitting protocol based on the methodology of Morin et al. (2019). All data points below 0.5 mꞏs<sup>-1</sup> were discarded (Fornasier-Santos et al., 2022), with the remaining segment, up to the peak velocity, being used for model fitting. The refined mathematical model was subsequently extrapolated  to  estimate  the  movement  onset  across all 



**Figure 2. Overview of the drone video processing procedure. The schematic details the data extraction workflow, encompassing raw video stabilization and subsequent YOLOv8s-based athlete tracking.** 





**Figure 3. Velocity curves comparison over time from the drone system (blue lines) and the radar device (orangered lines).** For each device, raw speed data are shown by solid/dotted lines, and fitted data by dashed/dash-dotted lines, respectively. The data is presented up to the point of maximal velocity achievement. Thus, the endpoint of the curve corresponds to Vmax. 

Wang et al. 

539 

sprint trials through forward prediction algorithms. The F- V parameters were derived based on the following model: 



with Vmax the maximal velocity (mꞏs<sup>-1</sup> ) reached at the end of the acceleration, _Tau_ the acceleration time constant (s). The horizontal force (Fh) and the ratio of force (RF) were calculated using the following equations: 

effects of device (Radar vs. Drone) and trial (Trial 1 vs. Trial 2), and their interaction on all F-V variables, with subject as a random intercept. Non-significant interactions were removed from final models. Post-hoc comparisons utilized Tukey-adjusted estimated marginal means. Effect � sizes were reported as partial eta-squared (η�). Statistical analysis was conducted using R (version 4.5.1, R Core Team, Vienna, Austria) at _p_ < 0.05. 

## **Results** 



Finally, the theoretical maximal horizontal force (F0) and theoretical maximal horizontal velocity (V0) were used to enable the calculation of both maximum power output (Pmax) and the slope of the F-V relationship (SFV): 



The model-predicted cumulative sprint distance was calculated from the fitted velocity curve using cumulative trapezoidal numerical integration. Times to reach 5 m (T5m), 10 m (T10m), 15 m (T15m), and 20 m (T20m) were defined as the time instants at which the cumulative distance first reached the corresponding distance values. Average accelerations (A5m, A10m, A15m, A20m) were then calculated as the ratio between the change in velocity and the time variation between the start and the corresponding reach times (T5m, T10m, T15m, and T20m). 

### **Test-retest reliability** 

Drone system ICC values ranged from 0.59 to 0.95, while radar system values were higher (0.73–0.97). Both systems achieved excellent reliability (ICC > 0.90) for Vmax, V0, and late-phase acceleration kinematics (A15m, A20m), but showed lower stability for early acceleration variables such as Amax, F0, and T5m (Table 1). 

### **Concurrent validity** 

Maximum velocity and kinematic time variables exhibited strong absolute agreement (high R<sup>2</sup> ), whereas early acceleration variables (e.g., F0, Amax) showed greater dispersion and proportional bias (Figure 4). 

Most metrics (Vmax, V0, Pmax, RFmax, T5m, T10m, T15m, T20m, A5m, A10m, A15m, A20m) were classified as Good agreement (%Bias < 5%, LoA < 10%) between systems (Table 2 and Figure 5). 

Significant device main effects (Table 3) showed that the drone overestimated _Tau_ , Vmax, V0, and SFV, while underestimating Amax, F0, RFmax, and A5m. No significant differences were observed for Pmax, T5m, T10m, T15m, T20m, A10m, A15m, or A20m ( _p_ > 0.05). 

## **Discussion** 

### **Statistical analysis** 

Data are presented as mean ± standard deviation (SD). Test-retest reliability for both radar and drone systems was assessed using intraclass correlation coefficients (ICC3,1) with 95% confidence intervals, the coefficient of variation (CV%) and the standard error of measurement (SEM = SD × √(1 - ICC)). The interpretation of ICC values adhered to the guidelines proposed by Koo and Li (2016): values below 0.50 indicated poor reliability, 0.50–0.75 moderate, 0.75–0.90 good, and above 0.90 excellent. The magnitude of change was interpreted using the minimal detectable change (MDC95 = 1.96 × √2 × SEM) and the smallest worthwhile change (SWC = 0.2 × between-subject SD). The MDC95 represents the smallest change exceeding measurement error and is used to determine whether an observed change in an individual is real; the SWC reflects the smallest practically meaningful change. Concurrent validity between the radar and drone systems was assessed using Bland-Altman analysis, reporting mean bias, 95% Limits of Agreement (LoA), and bias percentage (Bias%) (Giavarina, 2015). When compared between different devices, metrics with a bias of less than 5% and a narrow LoA (< 10% of mean) were considered to show good agreement; conversely, metrics with greater bias or a wider LoA were interpreted as having poorer consistency between the devices (Cormier et al., 2023; Dawson et al., 2026). 

The purpose of this study was to evaluate the feasibility of a drone-based vision system for measuring short-sprint performance and F-V profiles. Overall, the drone system demonstrated moderate-to-excellent test-retest reliability and good concurrent validity with the radar system for most F-V variables. However, early-acceleration and model-derived variables showed only moderate reliability (e.g., Amax, F0, T5m) and poor concurrent validity ( _Tau_ , Amax, F0, SFV) between devices. 

Both systems demonstrated moderate-to-excellent test-retest reliability across most F-V variables. However, the drone system returned only moderate ICC values for early-acceleration metrics, including Amax, F0, RFmax, T5m, T10m, and A5m (ICC = 0.61, 0.61, 0.63, 0.59, 0.70, and 0.71, respectively), whereas the radar system achieved moderate-to-good reliability for these same variables (ICC = 0.73, 0.73, 0.73, 0.81, 0.87, and 0.88, respectively). Across all variables, MDC95 values exceeded the SWC, indicating that neither system provides sufficient sensitivity for detecting small individual changes. This limitation was particularly pronounced for early-acceleration metrics such as F0 and T5m, whose lower reliability is not unique to the drone system. This finding is consistent with previous reliability studies on F0 and T5m using radar (Simperingham et al., 2019) and laser (Ghigiarelli et al., 2022). The calculation of F0 relies on the initial phase of sprint acceleration, 

A linear  mixed  model (LMM)  analyzed the fixed 

540 

Drone-based sprint profiling 

where speed data inherently exhibit high noise and variability (Simperingham et al., 2019). This is in line with previous studies that reported only moderate intra-day reliability for laser-derived F0 (CV = 7.8%, ICC = 0.64; Buchheit et al., 2014) and radar-derived F0 (CV = 6.9%, ICC = 0.70; Simperingham et al., 2019). The lower reliability observed in these early-acceleration metrics likely reflects the biomechanical variability inherent to initial acceleration, where unstable velocity data capture contributes to greater 

measurement inconsistency. Specifically, the top-down perspective inherently limits accurate center-of-mass estimation, as the bounding box centroid shifts with rapid postural transitions. Additionally, as the athlete accelerates, rapid postural transitions cause the bounding box dimensions to fluctuate frame-by-frame. This morphological instability introduces high-frequency noise into the positional data, degrading the accuracy of derived horizontal force metrics. 

|**Table 1. Descriptive statistics and test-retest reliability of sprint F-V variables measured by the drone and radar systems.**|
|---|



|**Variables**|**Device**|**Mean ± SD**<br>**(n= 17)**|**ICC (95% CI)**|**CV% (95% CI)**|**SEM**|**SWC**|**MDC95**|**Interpretation**|
|---|---|---|---|---|---|---|---|---|
|**_T_**|Drone|1.14 ± 0.11|0.75 (0.44 to 0.90)|4.69 (3.06 to 6.32)|0.05|0.02|0.15|Good|
|**_au_(s)**|Radar|1.10 ± 0.08|0.77(0.48 to 0.91)|3.37(2.20 to 4.53)|0.04|0.02|0.10|Good|
|**A ꞏ**<sup>**-2**</sup>|Drone|7.59 ± 0.46|0.61 (0.20 to 0.84)|3.84 (2.51 to 5.17)|0.29|0.08|0.81|Moderate|
|**max (ms)**|Radar|7.76 ± 0.40|0.73(0.41 to 0.90)|2.67(1.75 to 3.60)|0.21|0.08|0.58|Moderate|
|**Vmax (mꞏs**<sup>**-1**</sup>**)**|Drone<br>Radar|8.70 ± 0.45<br>8.62 ± 0.41|0.94 (0.85 to 0.98)<br>0.96(0.89 to 0.98)|1.25 (0.95 to 1.46)<br>1.00(0.65 to 1.35)|0.11<br>0.09|0.09<br>0.08|0.30<br>0.24|Excellent<br>Excellent|
|**V ꞏ**<sup>**-1**</sup>|Drone|9.02 ± 0.51|0.94 (0.83 to 0.98)|1.43 (1.09 to 1.66)|0.13|0.10|0.36|Excellent|
|**0 (ms)**|Radar|8.92 ± 0.45|0.95(0.88 to 0.98)|1.12(0.73 to 1.51)|0.10|0.09|0.28|Excellent|
|<sup>**-1**</sup>|Drone|7.57 ± 0.47|0.61 (0.20 to 0.84)|3.91 (2.56 to 5.27)|0.30|0.09|0.82|Moderate|
|**F0 (Nꞏkg)**|Radar|7.76 ± 0.40|0.73(0.40 to 0.89)|2.73(1.79 to 3.68)|0.21|0.08|0.59|Moderate|
|<sup>**-1**</sup>|Drone|17.04 ± 1.17|0.79 (0.51 to 0.92)|3.19 (2.31 to 3.74)|0.54|0.23|1.51|Good|
|**Pmax (Wꞏkg)**|Radar|17.31 ± 1.26|<br>0.91(0.77 to 0.97)|<br>2.23(1.46 to 3.00)|0.39|0.25|1.07|Excellent|
|**RF %**|Drone|61.09 ± 2.37|0.63 (0.23 to 0.85)|2.39 (1.56 to 3.22)|1.46|0.44|4.05|Moderate|
|**max ()**|Radar|61.99 ± 1.94|0.73(0.39 to 0.89)|1.66(1.08 to 2.23)|1.03|0.37|2.85|Moderate|
|**S Nꞏꞏ**<sup>**-1**</sup>**ꞏk**<sup>**-1**</sup>|Drone|-0.84 ± 0.08|0.75 (0.43 to 0.90)|4.88 (3.18 to 6.57)|0.04|0.02|0.11|Good|
|**FV (smg)**|Radar|-0.87 ± 0.06|0.76(0.45 to 0.91)|3.56(2.32 to 4.79)|0.03|0.01|0.09|Good|
|**T5m (s)**|Drone<br>Radar|1.38 ± 0.04<br>1.37 ± 0.03|0.59 (0.17 to 0.83)<br>0.81(0.55 to 0.93)|1.64 (1.20 to 1.89)<br>1.08(0.76 to 1.31)|0.02<br>0.02|0.01<br>0.01|0.06<br>0.04|Moderate<br>Good|
||Drone|2.12 ± 0.05|0.70 (0.34 to 0.88)|1.29 (0.95 to 1.48)|0.03|0.01|0.08|Moderate|
|**T10m (s)**|Radar|2.11 ± 0.05|0.87(0.67 to 0.95)|0.87(0.59 to 1.05)|0.02|0.01|0.05|Good|
||Drone|2.78 ± 0.07|0.84 (0.62 to 0.94)|0.94 (0.62 to 1.27)|0.03|0.01|0.07|Good|
|**T15m (s)**|Radar|2.77 ± 0.07|0.93(0.82 to 0.98)|0.66(0.43 to 0.89)|0.02|0.01|0.05|Excellent|
||Drone|3.40 ± 0.08|0.87 (0.67 to 0.95)|0.92 (0.60 to 1.24)|0.03|0.02|0.09|Good|
|**T20m (s)**|Radar|3.39 ± 0.09|0.94(0.85 to 0.98)|0.64(0.42 to 0.86)|0.02|0.02|0.06|Excellent|
|**A ꞏ**<sup>**-2**</sup>|Drone|4.42 ± 0.21|0.71 (0.37 to 0.89)|2.52 (1.86 to 2.91)|0.11|0.04|0.31|Moderate|
|**5m (ms)**|Radar|4.48 ± 0.22|0.88(0.70 to 0.96)|1.68(1.10 to 2.26)|0.08|0.04|0.21|Good|
|<sup>**-2**</sup>|Drone|3.47 ± 0.17|0.85 (0.63 to 0.94)|1.90 (1.24 to 2.56)|0.07|0.03|0.18|Good|
|**A10m (mꞏs)**|Radar|3.49 ± 0.18|<br>0.94(0.84 to 0.98)|<br>1.29(0.84 to 1.74)|0.05|0.04|0.13|Excellent|
|<sup>**-2**</sup>|Drone|2.86 ± 0.16|0.93 (0.82 to 0.97)|1.47 (0.96 to 1.98)|0.04|0.03|0.12|Excellent|
|**A15m (mꞏs)**|Radar|2.87 ± 0.17|<br>0.97(0.91 to 0.99)|<br>1.09(0.71 to 1.47)|0.03|0.03|0.09|Excellent|
|<sup>**-2**</sup>|Drone|2.44 ± 0.15|0.95 (0.86 to 0.98)|1.39 (0.91 to 1.88)|0.03|0.03|0.09|Excellent|
|**A20m (mꞏs)**|Radar|2.44 ± 0.15|<br>0.97(0.92 to 0.99)|<br>1.11(0.72 to 1.49)|0.03|0.03|0.08|Excellent|



|**A20m (mꞏs)**<br>ICC (95% CI) = intraclass<br>SEM = standard error of<br>**Table 2. Concurrent**|Radar<br>2.44 ± 0.15<br>0.97(0.92 to 0.99)<br>1.11<br>correlation coefficient with 95% confidence interval; CV<br>measurement; SWC = smallest worthwhile change; MDC9<br>**validity and limits of agreement (LoA) between t**|(0.72 to 1.49)<br>0.03<br>0.03<br>% (95% CI) = coefficient of variation<br>5= minimal detectable change at the<br>**he drone and radar systems for**|0.08<br>Excellent<br>with 95% confidence interval;<br>95% confidence level.<br>**sprint F-V variables.**|
|---|---|---|---|
|**Variables**|**Absolute bias (lower-upper LoA)**|**%Bias (lower-upper LoA)**|**Bias interpretation**|
|**_Tau_ (s)**|0.04(-0.14 to 0.22)|3.71(-11.89 to 19.69)|Poor|
|**Amax (mꞏs**<sup>**-2**</sup>**)**|-0.18(-1.02 to 0.67)|-2.29(-12.92 to 8.61)|Poor|
|**Vmax (mꞏs**<sup>**-1**</sup>**)**|0.08(-0.28 to 0.44)|0.96(-3.17 to 5.10)|Good|
|**V0 (mꞏs**<sup>**-1**</sup>**)**|0.10(-0.33 to 0.53)|1.12(-3.66 to 5.91)|Good|
|**F0 (Nꞏkg**<sup>**-1**</sup>**)**|-0.20(-1.06 to 0.67)|-2.55(-13.37 to 8.56)|Poor|
|**Pmax (Wꞏkg**<sup>**-1**</sup>**)**|-0.27(-1.64 to 1.11)|-1.54(-8.96 to 6.12)|Good|
|**RFmax (%)**|-0.90(-5.18 to 3.38)|-1.46(-8.27 to 5.46)|Good|
|**SFV (Nꞏsꞏm**<sup>**-1**</sup>**ꞏkg**<sup>**-1**</sup>**)**|0.03(-0.10 to 0.16)|3.50(-11.54 to 18.18)|Poor|
|**T5m (s)**|0.01(-0.05 to 0.07)|0.76(-3.42 to 5.00)|Good|
|**T10m (s)**|0.01(-0.06 to 0.08)|0.53(-2.62 to 3.71)|Good|
|**T15m (s)**|0.01(-0.06 to 0.08)|0.39(-2.15 to 2.96)|Good|
|**T20m(s)**|0.01(-0.07 to 0.08)|0.16(-2.01 to 2.35)|Good|
|**A5m (mꞏs**<sup>**-2**</sup>**)**|-0.06(-0.35 to 0.23)|-1.32(-7.54 to 5.05)|Good|
|**A10m (mꞏs**<sup>**-2**</sup>**)**|-0.03(-0.18 to 0.13)|-0.73(-4.97 to 3.60)|Good|
|**A15m (mꞏs**<sup>**-2**</sup>**)**|-0.01(-0.10 to 0.08)|-0.34(-3.47 to 2.86)|Good|
|**A20m (mꞏs**<sup>**-2**</sup>**)**|0.00(-0.07 to 0.07)|0.09(-2.78 to 3.01)|Good|



LoA = limits of agreement. 

Wang et al. 

541 

|**Table 3. Linear mixed effec**|**ts model estimate**|**s for sprint F-V**|**variables, assessi**|**ng maineffects **|**of device and trial.**<br>|
|---|---|---|---|---|---|
||||||𝟐|
|**Variables**|**Estimate**|**SE**|**t-statistic**|**_p_**|𝛈𝐩<br>|
|**_Tau_ (s)**|0.042|0.015|2.694|0.010|0.129|
|**Amax (mꞏs**<sup>**-2**</sup>**)**|-0.176|0.078|-2.259|0.028|0.094|
|**Vmax (mꞏs**<sup>**-1**</sup>**)**|0.083|0.032|2.579|0.013|0.120|
|**V0 (mꞏs**<sup>**-1**</sup>**)**|0.100|0.038|2.625|0.012|0.123|
|**F0 (Nꞏkg**<sup>**-1**</sup>**)**|-0.195|0.079|-2.465|0.017|0.110|
|**Pmax (Wꞏkg**<sup>**-1**</sup>**)**|-0.265|0.134|-1.976|0.054|0.074|
|**RFmax (%)**|-0.898|0.391|-2.294|0.026|0.097|
|**SFV (Nꞏsꞏm**<sup>**-1**</sup>**ꞏkg**<sup>**-1**</sup>**)**|0.030|0.012|2.607|0.012|0.122|
|**T5m (s)**|0.011|0.006|1.909|0.062|0.069|
|**T10m (s)**|0.011|0.007|1.712|0.093|0.056|
|**T15m (s)**|0.011|0.007|1.638|0.108|0.052|
|**T20m (s)**|0.005|0.007|0.728|0.470|0.011|
|**A5m (mꞏs**<sup>**-2**</sup>**)**|-0.059|0.028|-2.111|0.040|0.083|
|**A10m (mꞏs**<sup>**-2**</sup>**)**|-0.026|0.016|-1.638|0.108|0.052|
|**A15m (mꞏs**<sup>**-2**</sup>**)**|-0.010|0.010|-0.983|0.330|0.019|
|**A20m (mꞏs**<sup>**-2**</sup>**)**|0.002|0.008|0.272|0.787|0.002|



Interaction effects between device and trial were not statistically significant (all _p_ > 0.05) and were removed from the final models. 



**Figure 4. Scatter plots with lines of identity comparing sprint mechanical variables derived from the drone and radar systems.** The dashed black line represents the line of perfect agreement (y = x), while the solid blue line indicates the linear regression fit along with its 95% confidence intervals. 

542 

Drone-based sprint profiling 





**Figure 5. Bland-Altman plots evaluating the concurrent validity and limits of agreement between the drone and radar measurement systems.** The solid blue line represents the mean systematic bias, and the dashed red lines indicate the upper and lower 95% limits of agreement (LoA). 

The Bland-Altman analysis revealed varying levels of agreement across sprint mechanical variables. While Vmax, V0, Pmax, RFmax, all split-time intervals (T5m–T20m), and all average acceleration metrics (A5m–A20m) showed good agreement with minimal bias (< 5%) and narrow limits of agreement (< 10%), early-acceleration and model-derived metrics ( _Tau_ , SFV, Amax, F0) demonstrated poor agreement, exhibiting wider limits of agreement (> 10%). For initial-acceleration-related metrics (Amax, F0), the observed lower agreements primarily stem from two sources: (i) tracking instability during trunk-angle progression: as the upper body inclines through acceleration (Nagahara et al., 2014), continuous shifts of visual recognition bounding boxes degrade force estimation. The drone system exhibited stronger biases for initial-acceleration-related varia- 

bles, specifically F0 and Amax. This discrepancy likely originates from the kinematic transition of the tracking centroid during the explosive start. During the first 5 m, athletes transition from a deep forward lean to an upright posture. While the radar consistently tracks a reflection point on the lower back, the drone algorithm calculates the centroid of a 2D bounding box. As the athlete’s trunk rotates upward, this geometric center shifts relative to the actual center of mass. This physical reference point drift explains the significant negative estimate for F0 and suggests that tracking stability in the first few strides remains a technical challenge. Critically, Bezodis et al. (2012) demonstrated that posture changes induce substantial measurement error, noting a 0.25 m forward shift of the lumbar tracking point relative to the center of mass (COM) within the first second of sprinting that caused significant velocity discrepancies 

Wang et al. 

543 

(Bias = +0.41 mꞏs<sup>-1</sup> , random error = ±0.18 mꞏs<sup>-1</sup> at 1 m). These extreme postural changes pose a greater challenge for the YOLO model in this study. This is because the geometric center of its detected bounding box may deviate substantially from the athlete's actual biological COM, thereby leading to greater <mark>errors (Figure 6). (</mark> ii) due to the inherent nature of 2D perspective projection, dynamic changes in the athlete's 3D position relative to the camera can distort the perceived 2D displacement. As illustrated in Figure 6, even when the center point of the detection bounding box is identified, its mapped position in realworld coordinates may deviate from the athlete's actual COM location. This error becomes particularly pronounced as the athlete accelerates forward and their distance from the camera's optical axis changes, especially during the initial acceleration phase. Similarly, the acceleration time constant ( _Tau_ ), which quantifies sprint initiation kinetics (Morin et al., 2019), and the slope of the forcevelocity relationship (SFV = -F0/V0) were also influenced by initial acceleration measurement errors. As highlighted in recent visual tracking literature (Yang and Gu, 2023), standard tracking algorithms often struggle to maintain precise localization during significant target appearance changes without advanced bounding box refinement. In this study, these uncorrected fluctuations disrupted the spatial precision required for capturing rapid kinematic transitions. 

Taken together, the Bland-Altman and LMM analyses converged on consistent findings. For parameters dependent on the initial acceleration—specifically _Tau_ , Amax, F0, and SFV—the drone and radar systems should not be used interchangeably. LMM analysis confirmed significant systematic bias ( _p_ ≤ 0.028, η�� = 0.094–0.129, moderate effect; Cohen, 1988). More critically, the Bland-Altman limits of agreement (LoA) exceeded the 10% threshold, which is regarded as the upper limit for acceptable measurement error in athletic performance monitoring (Cormier et al., 2023). This lack of agreement suggests that the drone's vision-based tracking struggles with the high-frequency kinematic changes and extreme trunk lean characteristic of the first few strides. 

In   contrast, a   seemingly   contradictory   finding 

emerged for variables such as Vmax, V0, RFmax, and A5m; while LMM results showed statistically significant differ� ences ( _p_ < 0.05) and moderate effect sizes (e.g., Vmax, η� = 0.120), their consistency was categorized as Good. This reflects a familiar point in sports biostatistics: a significant LMM p-value often indicates the consistency of a bias rather than its magnitude. As noted by Atkinson and Nevill (1998), statistical significance can be achieved with even trivial differences if the measurement precision is high and the bias is systematic. For Vmax, although the bias was statistically stable, its absolute magnitude was negligible (bias = 0.96%, LoA < 10%), falling well within the bounds of practical utility. 

Finally, for the remaining metrics (e.g., Pmax, split times T5m–T20m, and average accelerations A10m–A20m), both statistical methods yielded highly congruent results, although T5m should be interpreted with caution given its moderate test-retest reliability (ICC = 0.59). The LMM found no significant systematic bias ( _p_ > 0.05, η�� ≤ 0.074) and Bland-Altman analysis confirmed extremely low bias (e.g., A20m, bias = 0.09%). This overarching pattern suggests that the drone system reaches its peak evaluative accuracy once the athlete achieves a more stable upright posture and near-maximal velocity. 

### **Limitations** 

Several limitations exist. First, the sample size (n = 17) limits the generalizability of the findings. Second, only two sprint trials were conducted per session, which constrains the robustness of test-retest reliability estimates. Third, the conversion from 2D pixel coordinates to 3D real-world coordinates is susceptible to perspective projection errors, particularly during dynamic postural changes. Future research should implement multi-camera setups for stereoscopic triangulation or integrate human pose estimation to track specific anatomical landmarks (e.g., the hip) rather than bounding box centroids, thereby minimizing errors caused by dynamic postural changes. Additionally, drone deployment requires compliance with local airspace regulations and should be operated by an experienced pilot to ensure the safety of athletes and bystanders, which may limit its feasibility in some training environments. 



**Figure 6. Schematic illustration of 2D perspective projection, highlighting potential sources of error in drone-based velocity measurements. The detection bounding box (green) identifies the tracking point Cj, which is subsequently mapped to the realworld ground position Bj. However, particularly during dynamic sprinting postures, the athlete's actual biological center of mass (Aj) may deviate from this projected point, leading to discrepancies in kinematic parameter estimation.** 

544 

Drone-based sprint profiling 

## **Conclusion** 

sports. _Frontiers in Physiology_ **9** , 1288. 

https://doi.org/10.3389/fphys.2018.01288 

In conclusion, the drone system demonstrates moderate to excellent test-retest reliability for all sprint F-V variables, indicating the potential for repeated assessment of sprint F- V profiles. In addition, the results show that several key F- V variables, particularly those related to the acceleration phase at the start (e.g., _Tau_ , Amax, F0, SFV), exhibit statistically significant and practically meaningful systematic biases, making them unsuitable for interchangeable use. Conversely, variables related to speed (Vmax and V0), split times (T5m–T20m), and average accelerations (A10m, A15m, and A20m) show good practical agreement. However, caution is warranted for individual-level monitoring across all variables, as MDC95 values consistently exceeded the SWC, with this limitation being most pronounced for early-acceleration metrics (e.g., Amax, F0, and T5m). Researchers and practitioners should be mindful of these phase-specific discrepancies and measurement limitations when selecting and interpreting data from these technologies. Further research should explore the potential applications of the drone-based systems in investigating athletes’ turning abilities (e.g., curve sprinting), which has significant practical value for evaluating performance in team sports. 

#### **Acknowledgements** 

We are grateful for the help of all the coaches and the athletes who enthusiastically participated in our measurements. We would particularly like to thank Coach Fei Zhou for his invaluable assistance in organizing the sprint testing. This study was supported by the Shanghai Key Lab of Human Performance (Shanghai University of Sport, NO.11DZ2261100). During the preparation of this work the authors used Gemini to polish the English language and improve readability. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the publication. The datasets generated during the current study are not publicly available but are available from the corresponding author upon reasonable request. <mark>The authors declare that they have no conflict of interest.</mark> All experimental procedures were conducted in compliance with the relevant legal and ethical standards of the country where the study was carried out. 

### **References** 

- Alonso-Callejo, A., García-Unanue, J., Guitart-Trench, M., Majano, C., Gallardo, L. and Felipe, J.L. (2024) Validity and reliability of the acceleration-speed profile for assessing running kinematics’ variables derived from the force-velocity profile in professional soccer players. _Journal of Strength & Conditioning Research_ **38** , 563-570. https://doi.org/10.1519/jsc.0000000000004637 

- Asimakidis, N.D., Bishop, C.J., Beato, M., Mukandi, I.N., Kelly, A.L., Weldon, A., et al. (2024) A survey into the current fitness testing practices of elite male soccer practitioners: From assessment to communicating results. _Frontiers in Physiology_ **15** , 1376047. https://doi.org/10.3389/fphys.2024.1376047 

- Atkinson, G. and Nevill, A.M. (1998) Statistical methods for assessing measurement error (reliability) in variables relevant to sports medicine. _Sports Medicine_ **26** , 217-238. https://doi.org/10.2165/00007256-199826040-00002 

- de Barros Sousa, F. A., Henrique Marinho, A., da Silva Calvalcante, M. D., de Almeida Rodrigues, N., Silva Lima, T., Gilo da Silva, D., Fonseca, F. D. S., Balikian Junior, P. and Gomes de Araujo, G. (2025) Running sprint force-velocity-power profile obtained with a low-cost and low frame rate acquisition video technique: reliability and concurrent validity. _Sports Biomechanics_ **24** , 1957-1973. https://doi.org/10.1080/14763141.2024.2374882 

- Beato, M., Coratella, G., Stiff, A. and Iacono, A.D. (2018) The validity and between-unit variability of GNSS units (STATSports apex 10 and 18 hz)  for  measuring  distance  and  peak speed in team 

Bezodis, N., Salo, A.I. and Trewartha, G. (2012) Measurement error in estimates of sprint velocity from a laser displacement measurement device. _International Journal of Sports Medicine_ **33** , 439444. https://doi.org/10.1055/s-0031-1301313 

- Buchheit, M., Samozino, P., Glynn, J. A., Michael, B. S., Al Haddad, H., Mendez-Villanueva, A. and Morin, J.-B. (2014) Mechanical determinants of acceleration and maximal sprinting speed in highly trained young soccer players. _Journal of Sports Sciences_ **32** , 1906-1913. https://doi.org/10.1080/02640414.2014.965191 

- Clavel, P., Leduc, C., Morin, J.-B., Owen, C., Samozino, P., Peeters, A., Buchheit, M. and Lacome, M. (2022) Concurrent validity and reliability of sprinting force-velocity profile assessed with GPS devices in elite athletes. _International Journal of Sports Physiology & Performance_ **17** , 1527-1531. https://doi.org/10.1123/ijspp.2021-0339 

- Cohen, J. (1988) _Statistical Power Analysis for the Behavioral Sciences_ . 2nd ed. Hillsdale, NJ: Lawrence Erlbaum Associates, Publishers. https://doi.org/10.4324/9780203771587 

- Cormier, P., Tsai, M.-C., Meylan, C., Agar-Newman, D., Epp-Stobbe, A., Kalthoff, Z. and Klimstra, M. (2023) Concurrent validity and reliability of different technologies for sprint-derived horizontal force-velocity-power profiling. _Journal of Strength and Conditioning Research_ **37** , 1298-1305. https://doi.org/10.1519/jsc.0000000000004429 

- Dawson, L., McErlain-Naylor, S.A., Devereux, G. and Beato, M. (2026) Interunit reliability of STATSports APEX global navigation satellite system and accelerometer-derived metrics during shuttle run protocols of varied distances and change of direction frequency. _Journal of Sports Sciences_ **44** , 117-129. https://doi.org/10.1080/02640414.2025.2555554 

- Della Villa, F., Di Paolo, S., Santagati, D., Della Croce, E., Lopomo, N. F., Grassi, A. and Zaffagnini, S. (2022) A 2D video-analysis scoring system of 90° change of direction technique identifies football players with high knee abduction moment. _Knee Surgery, Sports Traumatology, Arthroscopy_ **30** , 3616-3625. https://doi.org/10.1007/s00167-021-06571-2 

- Dobbin, N., Hunwicks, R., Highton, J. and Twist, C. (2018) A reliable testing battery for assessing physical qualities of elite academy rugby league players. _Journal of Strength and Conditioning Research_ **32** , 3232-3238. https://doi.org/10.1519/jsc.0000000000002280 

- Edouard, P., Lahti, J., Nagahara, R., Samozino, P., Navarro, L., Guex, K., Morin, J.-B. and Mendiguchia, J. (2021) Low Horizontal Force Production Capacity during Sprinting as a Potential Risk Factor of Hamstring Injury in Football. _International Journal of Environmental Research and Public Health_ **18** , 7827. https://doi.org/10.3390/ijerph18157827 

- Ellens, S., Moran, C. and Varley, M.C. (2025) Concurrent validity and between-device reliability of the catapult vector S8 GNSS device. _PLOS ONE_ **20** , e0333792. https://doi.org/10.1371/journal.pone.0333792 

- Faude, O., Koch, T. and Meyer, T. (2012) Straight sprinting is the most frequent action in goal situations in professional football. _Journal of Sports Sciences_ **30** , 625-631. https://doi.org/10.1080/02640414.2012.665940 

- Feser, E., Lindley, K., Clark, K., Bezodis, N., Korfist, C. and Cronin, J. (2022) Comparison of two measurement devices for obtaining horizontal force-velocity profile variables during sprint running. _International Journal of Sports Science & Coaching_ **17** , 14551461. https://doi.org/10.1177/17479541211067211 

- Fornasier-Santos, C., Arnould, A., Jusseaume, J., Millot, B., Guilhem, G., Couturier, A., Colson, S., Rabita, G. and Morin, J.B. (2022) Sprint acceleration mechanical outputs derived from position- or velocity-time data: A multi-system comparison study. _Sensors_ **22** , 8610. https://doi.org/10.3390/s22228610 

- Galantine, P., Sudlow, A., Peyrot, N., Vercruyssen, F., Bélard, C., Dalleau, G., Morin, J.-B. and Gimenez, P. (2023) Force-velocity profile in sprinting: sex effect. _European Journal of Applied Physiology_ **123** , 911-921. https://doi.org/10.1007/s00421-02205121-z 

- Ghigiarelli, J.J., Ferrara, K.J., Poblete, K.M., Valle, C.F., Gonzalez, A.M. and Sell, K.M. (2022) Level of agreement, reliability, and minimal detectable change of the MusclelabTM laser speed device on force-velocity-power sprint profiles in Division II collegiate 

Wang et al. 

545 

athletes. _Sports_ **10** , 57. https://doi.org/10.3390/sports10040057 Giavarina, D. (2015) Understanding Bland Altman analysis. _Biochemia Medica_ **25** , 141-151. https://doi.org/10.11613/bm.2015.015 Grazioli, R., Soares, M. L. H. Q., Schons, P., Preissler, A. B., Veeck, F., Benítez-Flores, S., Pereira, L. A., Loturco, I. and Peyré-Tartaruga, L. A. (2024) Curve sprint performance and speed-related capabilities in professional soccer players. _Journal of Bodywork and Movement Therapies_ **40** , 1034-1040. https://doi.org/10.1016/j.jbmt.2024.07.018 

Haffner, O., Kučera, E. and Rosinová, D. (2024) Applications of machine learning and computer vision in Industry 4.0. _Applied Sciences_ **14** , 2431. https://doi.org/10.3390/app14062431 

Harper, D.J., Carling, C. and Kiely, J. (2019) High-intensity acceleration and deceleration demands in elite team sports competitive match play: A systematic review and meta-analysis of observational studies. _Sports Medicine_ **49** , 1923-1947. https://doi.org/10.1007/s40279-019-01170-1 

Haugen, T., Breitschädel, F. and Samozino, P. (2020) Power-force-velocity profiling of sprinting athletes: Methodological and practical considerations when using timing gates. _Journal of Strength and Conditioning Research_ **34** , 1769-1773. https://doi.org/10.1519/jsc.0000000000002890 

|Host, K. and Ivašić-Kos, M. (2022) An overview of Human Action<br>Recognition in sports based on Computer Vision._Heliyon_ **8**,<br>e09633. https://doi.org/10.1016/j.heliyon.2022.e09633|
|---|
|Koo, T.K. and Li, M.Y. (2016) A guideline of selecting and reporting in-<br>traclass correlation coefficients for reliability research._Journal_<br>_of Chiropractic Medicine_ **15**, 155-163.<br>https://doi.org/10.1016/j.jcm.2016.02.012|
|Martínez-Hernández, D., Quinn, M. and Jones, P. (2023) Linear advanc-<br>ing actions followed by deceleration and turn are the most com-<br>mon movements preceding goals in male professional soccer.<br>_Science and Medicine in Football_ **7**, 25-33.<br>https://doi.org/10.1080/24733938.2022.2030064|



|Mendiguchia, J., Edouard, P., Samozino, P., Brughelli, M., Cross, M.,|
|---|
|Ross, A., Gill, N., Morin, J.-B. and Mendez-Villanueva, A.|
|(2016) Field monitoring of sprinting power-force-velocity pro-<br>file before, during and after hamstring injury: Two case reports.|
|_Journal of Sports Sciences_ **34**, 535-541.|
|https://doi.org/10.1080/02640414.2015.1122207|



|Morgan, O.J., Drust, B., Ade, J.D. and Robinson, M.A. (2022) Change of|
|---|
|direction frequency off the ball: new perspectives in elite youth|
|soccer._Science and Medicine in Football_ **6**, 473-482.|
|https://doi.org/10.1080/24733938.2021.1986635|



- Morgans, R., Mandorino, M., Ryan, B., Zmijewski, P., Moreira, A. and Oliveira, R. (2025) Contextualized acceleration and deceleration profiles of elite soccer players during English premier league match-play. The effect of possession, positional demands and opponent ranking. _Biology of Sport_ **42** , 67-75. https://doi.org/10.5114/biolsport.2025.148540 

- Morin, J.-B., Gimenez, P., Edouard, P., Arnal, P., Jiménez-Reyes, P., Samozino, P., Brughelli, M., Mendiguchia, J. and Rabita, G. (2015) Sprint Acceleration Mechanics: The Major Role of Hamstrings in Horizontal Force Production. _Frontiers in Physiology_ **6** , 404. https://doi.org/10.3389/fphys.2015.00404 

- Morin, J.-B., Samozino, P., Murata, M., Cross, M.R. and Nagahara, R. (2019) A simple method for computing sprint acceleration kinetics from running velocity data: Replication study with improved design. _Journal of Biomechanics_ **94** , 82-87. https://doi.org/10.1016/j.jbiomech.2019.07.020 

- Nagahara, R., Matsubayashi, T., Matsuo, A. and Zushi, K. (2014) Kinematics of transition during human accelerated sprinting. _Biology Open_ **3** , 689-699. https://doi.org/10.1242/bio.20148284 

- Reveret, L., Chapelle, S., Quaine, F. and Legreneur, P. (2020) 3D visualization of body motion in speed climbing. _Frontiers in Psychology_ **11** , 2188. https://doi.org/10.3389/fpsyg.2020.02188 

- Russomanno, T.G., Blauberger, P., Kolbinger, O., Lam, H., Schmid, M. and Lames, M. (2022) Drone-based position detection in sports—Validation and applications. _Frontiers in Physiology_ **13** , 850512. https://doi.org/10.3389/fphys.2022.850512 

- Saini, N., Price, E., Tallamraju, R., Enficiaud, R., Ludwig, R., Martinovic, I., Ahmad, A., Hayat, S. and Scaramuzza, D. (2019) Markerless outdoor human motion capture using multiple autonomous micro aerial vehicles. In: _Proceedings of the 2019 IEEE/CVF International Conference on Computer Vision (ICCV)_ . IEEE. 823832. https://doi.org/10.1109/iccv.2019.00091 

- Samozino, P., Rabita, G., Dorel, S., Slawinski, J., Peyrot, N., Saez De Villarreal, E. and Morin, J.B. (2016) A simple method for measuring power, force, velocity properties, and mechanical effectiveness in sprint running. _Scandinavian Journal of Medicine & Science in Sports_ **26** , 648-658. https://doi.org/10.1111/sms.12490 

- Silva, H., Nakamura, F.Y., Beato, M. and Marcelino, R. (2023) Acceleration and deceleration demands during training sessions in football: a systematic review. _Science and Medicine in Football_ **7** , 198-213. https://doi.org/10.1080/24733938.2022.2090600 

- Simperingham, K.D., Cronin, J.B., Pearson, S.N. and Ross, A. (2019) Reliability of horizontal force-velocity-power profiling during short sprint-running accelerations using radar technology. _Sports Biomechanics_ **18** , 88-99. 

https://doi.org/10.1080/14763141.2017.1386707 

- Straub, R.K. and Powers, C.M. (2022) Utility of 2D video analysis for assessing frontal plane trunk and pelvis motion during stepping, landing, and change in direction tasks: A validity study. _International Journal of Sports Physical Therapy_ **17** , 139-147. https://doi.org/10.26603/001c.30994 

- Taylor, J.M., Madden, J.L., Cunningham, L.P. and Wright, M. (2022) Fitness testing in soccer revisited: developing a contemporary testing battery. _Strength & Conditioning Journal_ **44** , 10-21. https://doi.org/10.1519/ssc.0000000000000702 

- Tran, T., Choo, K. T. W., Foong, S., Bhardwaj, H., Win, S. K. H., Ang, W. J., Saini, N., Chakravarthula, P., Ahmad, A. and Scaramuzza, D. (2024) Analyzing swimming performance using drone captured aerial videos. In: _Proceedings of the 10th Workshop on Micro Aerial Vehicle Networks, Systems, and Applications_ . Minatoku Tokyo Japan: ACM. 7-12. 

https://doi.org/10.1145/3661810.3663464 

- Vantieghem-Nicolas, L., Morin, J.-B., Cotte, T., Sangnier, S. and Rossi, J. (2023) Concurrent validity and reliability of the sprint forcevelocity profile assessed with K-AI wearable tech. _Sensors_ **23** , 8189. https://doi.org/10.3390/s23198189 

- Walter, S.D., Eliasziw, M. and Donner, A. (1998) Sample size and optimal designs for reliability studies. _Statistics in Medicine_ **17** , 101-110. https://doi.org/10.1002/(sici)10970258(19980115)17:1<101::aid-sim727>3.0.co;2-e 

- Wu, L.Y. and Swartz, T.B. (2023) The calculation of player speed from tracking data. _International Journal of Sports Science & Coaching_ **18** , 516-522. https://doi.org/10.1177/17479541221124036 

- Yang, Y. and Gu, X. (2023) Accurate and robust visual tracking using bounding box refinement and online sample filtering. _Signal Processing: Image Communication_ **116** , 116981. https://doi.org/10.1016/j.image.2023.116981 

- Zablocki, É., Ben-Younes, H., Pérez, P. and Cord, M. (2022) Explainability of deep vision-based autonomous driving systems: review and challenges. _International Journal of Computer Vision_ **130** , 2425-2452. https://doi.org/10.1007/s11263-022-01657-x 

- Zhang, Q., Pommerell, F., Owen, A., Trama, R., Martin, C. and Hautier, C.A. (2021) Running patterns and force‐velocity sprinting profiles in elite training young soccer players: A cross‐sectional study. _European Journal of Sport Science_ **21** , 1718-1726. https://doi.org/10.1080/17461391.2020.1866078 

### **Key points** 

- The study evaluated a consumer-grade drone system for sprint force-velocity profiling against a radar using multifaceted statistical analyses (ICC, CV%, SEM, LMM, Bland-Altman). 

- The drone system demonstrated moderate-to-excellent reliability (ICC: 0.59–0.95) and high practical agreement in the maximum speed phase (bias ≤ 1.12%; LoA < 10%), but exhibited significant systematic bias during the initial acceleration phase. 

- While suitable for group-level monitoring of maximum velocity metrics, the identified early-phase tracking instability provides clear targets for algorithm optimization in future drone-based sports technology applications. 

546 

Drone-based sprint profiling 

#### **AUTHOR BIOGRAPHY** 



<!-- Start of picture text -->
Fahui WANG<br>Employment<br>Université Lyon 1, LIBM, UR 7424,<br>Villeurbanne, France<br>Degree<br>Ph.D.<br>Research interests<br>Sports Biomechanics<br>E-mail:  fahui.wang@etu.univ-lyon1.frg@etu.univ-lyon1.fretu.univ-lyon1.fryon1.fron1.fr<br><!-- End of picture text -->

Sports Biomechanics **E-mail:** fahui.wang@etu.univ-lyon1.frg@etu.univ-lyon1.fretu.univ-lyon1.fryon1.fron1.fr **Christophe HAUTIER** 



**Employment** Université Lyon 1, LIBM, UR 7424, Villeurbanne, France **Degree** Ph.D. **Research interests** Sports Biomechanics **E-mail:** christophe.hautier@univ-lyon1.fr **Lin SONG Employment** School of Athletic Performance, Shanghai University of Sport, Shanghai, China **Degree** MSc **Research interests** Video Analysis of Athletic Performance **E-mail:** songlinccc@hotmail.com **Yong ZHOU Employment** School of Athletic Performance, Shanghai University of Sport, Shanghai, China **Degree** MSc **Research interests** Football performance **E-mail:** 2421852068@sus.edu.cn 





|**Brice GUIGNARD**|
|---|
|**Employment**|
|Université Lyon 1, LIBM, UR 7424,|
|Villeurbanne, France|
|**Degree**<br>Ph.D.|
|**Research interests**|
|Biomechanics, Human Motion Analy-<br>|
|sis & Sport Performance|
|**E-mail:**brice.guignard@univ-lyon1.fr|
|**Paul GLAISE**|
|**Employment**|
|Université Lyon 1, LIBM, UR 7424,|
|Villeurbanne, France<br>**Degree**<br>Ph.D.|
|**Research interests**|
|Applied physiology of exercise|
|**E-mail:**g-paul@sfr.fr|
|**Qingshan ZHANG**|
|**Employment**|
|School of Athletic Performance,|
|Shanghai University of Sport, Shang-|
|hai, China|
|**Degree**<br>Ph.D.|
|**Research interests**|
|Sports Biomechanics|
|**E-mail:**zhang.qingshan@hotmail.com|











#### **Qingshan Zhang** 

School of Athletic Performance, Shanghai University of Sport, Shanghai, China 


