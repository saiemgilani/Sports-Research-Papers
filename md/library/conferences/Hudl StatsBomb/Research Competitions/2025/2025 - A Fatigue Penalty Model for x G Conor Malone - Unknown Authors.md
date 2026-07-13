<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2025/2025 - A Fatigue Penalty Model for x G Conor Malone - Unknown Authors.pdf -->



# **A Fatigue Penalty Model for xG** 

Quantifying the Impact of Workload on Shot Performance in Elite Football Conor Malone 

## **Abstract** 

The relentless pace of modern elite football has pushed players and teams to their physical and tactical limits. As fixture schedules grow ever more congested, the question of how accumulated fatigue shapes on-field performance has become impossible to ignore. While the physiological consequences of fatigue are well documented, its influence on the moments that decide matches—particularly the volume and quality of shot creation—remains surprisingly unclear. This study addresses that gap by quantifying the relationship between player workload and shot performance, leveraging integrated event and tracking data from roughly 61,000 non-penalty shots across 1,752 men’s matches in the English Premier League, German Bundesliga, and Spanish La Liga during the 2023/24 and 2024/25 seasons. 

Player fatigue was measured via an Acute:Chronic Workload Ratio (ACWR), defined as the ratio between short-term (1-week) and long-term (4-week) distance-weighted running metrics that account for movement intensity. Shot-level analyses were conducted at both the individual and team levels to examine associations between fatigue and (i) shot volume, (ii) shot quality measured by expected goals (xG), and (iii) shot conversion efficiency. 

Results reveal a statistically significant but modest negative association between team-level fatigue and shot volume (p < 0.001, R² = 0.12), corresponding to an estimated decrease of approximately one shot per game for each unit increase in ACWR. A weaker, non-significant relationship (p = 0.1, R² = 0.007) was observed between team fatigue and average shot expected goals (xG), suggesting a limited reduction in the creation of high-quality shooting opportunities under conditions of elevated workload. No significant associations were identified when analyses were restricted to the fatigue levels of the shooting player alone or with the conversion of shots into goals. 

These findings indicate that fatigue exerts only a minor influence on shot-related performance at the elite level, potentially reflecting effective workload management and recovery practices in contemporary professional football. Despite the modest findings, this study provides a valuable framework for integrating physical tracking data with performance outcomes, paving the way for future research into the contextual and cumulative effects of fatigue on match performance. 

**1** 



## **Introduction** 

In contemporary elite football, player workloads have reached unprecedented levels due to increasingly congested competition schedules across domestic, continental, and international tournaments. The modern professional season now extends almost year-round, leaving limited opportunity for physical or psychological recovery. For example, Chelsea’s 2024/25 campaign began on **18 August 2024** and concluded at the FIFA Club World Cup Final on **13 July 2025** , encompassing nearly twelve consecutive months of competitive activity. They then had their first 25/26 preseason game 3 weeks later on **August 8**<sup>**th**</sup> . 

Simultaneously, the methods available to monitor player performance have evolved significantly. For over a decade, **global positioning system (GPS)** tracking has been routinely employed to quantify individual physical output, including distance covered, high-intensity runs, and positional load. Recent advances in **computer vision and multi-camera tracking systems** now enable comparable data collection without the need for wearable sensors, facilitating player-level workload assessment across all competitive fixtures. These advancements have substantially increased the availability and granularity of longitudinal fatigue data in professional football. 

### **2.1 Context and Motivation** 

Figure 1 below illustrates the **weekly fatigue levels** for **FC Bayern Munich (red)** and **Bayer 04 Leverkusen (black)** throughout the 2023/24 Bundesliga season, in which Leverkusen completed an unbeaten campaign to secure the league title. Bayern Munich exhibited pronounced spikes in fatigue preceding critical fixtures against Leverkusen, driven by early-season congestion (including the German Super Cup) and rescheduled matches in December. Notably, these elevated fatigue levels preceded Bayern’s **3–0 defeat in February** , suggesting a potential association between accumulated fatigue and reduced competitive performance. 

**Figure 1: Weekly Fatigue 23/24 Bayern Munich & Bayer 04** 



**2** 



Although considerable research has investigated the **physiological manifestations** of fatigue— such as diminished sprint capacity, reduced total distance, and impaired recovery kinetics— empirical evidence linking fatigue to **football-specific performance outcomes** remains limited. This gap arises primarily from historical constraints in data availability. Only recently have comprehensive tracking and event-level datasets enabled the systematic quantification of fatigue effects on technical and tactical execution at the match level. 

### **2.2 Research Objective** 

The present study aims to **quantify the influence of player fatigue on shooting performance in elite football** , contributing to a growing body of research at the intersection of performance analytics and applied sport science. Specifically, the analysis examines three dimensions of shooting behaviour: 

1. **Shot quality** , represented in the **Expected Goals (xG)** metric; 

2. **Shot conversion** , defined as the probability of converting a shot into a goal; and 

3. **Shot frequency** , representing the total number of attempts generated by a player or team. 

These relationships are evaluated both at the **individual level** (the shooting player) and the **team level** (aggregate for all players on the field for a shot), providing insights into how accumulated fatigue influences offensive performance. By integrating physical workload indicators with match event data, this work seeks to advance the empirical understanding of how fatigue modulates footballing effectiveness, offering potential implications for fixture scheduling, player rotation strategies, and load management practices. 

## **Related Work** 

The relationship between athletic fatigue and performance is a cornerstone of sports science. Foundational to this field is the concept of "load," defined by the International Olympic Committee (IOC) as the total "sport and non-sport burden" applied to an athlete, with its management being critical for optimizing performance and preventing injury (Soligard et al., 2016). A key advancement in load monitoring is the Acute:Chronic Workload Ratio (ACWR), which posits that an athlete's risk of negative outcomes; including performance decrements, spikes when short-term load rapidly exceeds their preparedness (i.e. chronic load), particularly when the ACWR surpasses 1.5. This model establishes that it is not merely high load, but the _rate of change_ relative to an athlete's fitness that heightens risk. While the IOC consensus broadly links load to injury, it provides the theoretical premise that maladaptation impairs an athlete's "capacity to accept load" a principle that logically extends to technical and tactical performance. 

Building on this physiological framework, controlled experimental studies have demonstrated that fatigue directly impairs soccer-specific skills. Research employing match simulations has consistently shown that exercise-induced fatigue leads to measurable declines in technical 

**3** 



proficiency. For instance, Russell et al. (2011) found that soccer-specific fatigue significantly reduced shooting precision and passing speed, especially in the latter stages of a match. Similarly, Teoldo et al. (2024) observed that acute physical fatigue altered tactical behaviour, reducing the number of high-intensity actions performed near the ball. These findings provide crucial evidence that the physiological state of fatigue has a tangible, negative effect on the execution of fundamental skills and in-game decision-making. 

Beyond physical and technical metrics, the psychological dimension of fatigue is also critical. Brink et al. (2010) demonstrated that psychosocial stress and poor recovery states were significant predictors of illness in elite youth players, highlighting the multifaceted nature of "load" and the importance of holistic, prospective monitoring to understand an athlete's readiness. 

A central challenge, however, lies in bridging the gap between measuring internal states and isolated skills, and quantifying the tangible performance cost of fatigue in a competitive setting. While many studies track workload and fitness in isolation, few establish a direct link to in-match output. A benchmark for this type of analysis is provided by Hart et al. (2022) in rugby, who quantified how a decline in physical traits (e.g., an ~11.5% reduction in sprint velocity) translated to a predictable decrease in match effectiveness (one fewer tackle break per game). This approach is foundational for workload monitoring, as it contextualizes a drop in physical capacity with a predicted degradation in competitive performance. 

Despite these advances, a significant gap persists in football, particularly concerning its most decisive action: shooting. While we know fatigue impairs passing and dribbling (Russell et al., 2011) and alters tactical behaviour (Teoldo et al., 2024), its direct impact on the **quality and quantity of shots taken** in real-world, elite competition remains underexplored. Previous research has been limited by small sample sizes, controlled laboratory settings, or a focus on skill execution in isolation rather than its integration into the complex, emergent process of chance creation. This study seeks to bridge this gap. Building on the foundational concepts of load management (Soligard et al., 2016) and the documented effects of fatigue on technical skills, we employ the ACWR framework to operationalize fatigue and move the analysis into the competitive arena. By leveraging large-scale event and tracking data from top European leagues, this research quantitatively investigates the proposed link between accumulated workload and the degradation of shot production and quality, thereby testing a critical, yet unverified, assumption in the chain from fatigue to match outcome. 

### **3.1 Conceptual Framework and Hypotheses** 

Building upon the established literature linking fatigue to diminished technical proficiency and tactical execution, we propose a conceptual model where accumulated workload impairs offensive output through two primary channels: (1) a cognitive-physical channel, where fatigue reduces the precision and power of shooting technique and impairs decision-making in the final third, and (2) a tactical-channel, where fatigue limits a team's capacity to execute high-intensity pressing and overlapping runs, thereby reducing the number of high-quality chances created. 

**4** 



This framework leads to the following testable hypotheses: 

- **H1** : Increased player fatigue, as measured by the ACWR, is associated with a reduction in shot volume (number of shots per game) at both the individual and team levels. 

- **H2** : Increased player fatigue is associated with a reduction in average shot quality (mean xG per shot), as fatigued players take shots from less advantageous positions. 

- **H3** : The negative effects of fatigue on shot volume and quality will be more pronounced at the team level than the individual level, as collective tactical execution breaks down. 

## **Data** 

This study draws on a large-scale dataset combining event and physical tracking data across toptier European men’s football. The final dataset contains approximately **61,000 non-penalty shots** from **1,752 matches** spanning three major domestic leagues over two seasons (2023/24–2024/25): **Table 1:** Match and Shot Data Coverage by League and Season. 

|Competition|Country|23/24|24/25|
|---|---|---|---|
|Bundesliga|Germany|✔|✔|
|Premier League|England|✔|✔|
|La Liga|Spain||✔|



### **4.1 Event Data and Physical Metrics** 

For each shot, event-level data were linked with a set of **in-game physical metrics** derived from match footage using computer vision to track players between frames. These metrics capture player workload through counts and distances associated with different movement intensities. The following variables were available: 

### **High Intensity Running** 

- Count and Distance for High-Intensity (HI) actions 

- Count and Distance for High-Speed Running (HSR) 

- Count and Distance for Sprinting actions 

- Running Distance (15–20 km/h) 

- HSR Distance (20–25 km/h) 

- Sprinting Distance (>25 km/h) 

- Maximum Speed (km/h) 

**5** 



### **Accelerations/Decelerations** 

- Count for Medium-Intensity Accelerations and Decelerations 

- Count for High-Intensity Accelerations and Decelerations 

### **Overall Load** 

- Total Distance covered 

- Distance per minute (m/min) 

Physical metrics were aggregated at multiple temporal resolutions: by **half** , by **full match** , and in **15-minute segments** (e.g., 0–15, 15–30, etc.), enabling analysis of both acute and accumulated workload within games. 

### **Shot-Level Data Construction** 

For each non-penalty shot, physical workload metrics were compiled for both the **shooting player** and all **teammates on the field** at the time of the shot. Metrics were aggregated over three withinmatch windows: 

1. The 15 minutes preceding the shot, 

2. The current half up to the shot time, and 

3. The full match up to the shot time. 

In addition, rolling workload measures were computed over historical time windows of **1 week** , **2 weeks** , and **4 weeks** , allowing the derivation of acute and chronic workload ratios used to quantify fatigue. 

### **4.2 Data Augmentation and Imputation** 

Because complete tracking coverage is not available for all competitions, additional workload estimates were generated to fill gaps: 

- For **European and domestic cup matches** , workload was estimated proportionally to minutes played. For example, a player averaging 10 km of total distance per 90 minutes and playing 45 minutes in a match was allocated 5 km of workload for that fixture. 

- For **international fixtures** , where detailed lineup and time-of-play data are unavailable, each player was assigned an estimated 45 minutes of “regular intensity” match activity for each fixture during an international window. Although this assumption simplifies real-world variability, it ensures that the international workload typical of elite players is captured in cumulative fatigue measures. 

### **4.3 Fatigue Quantification** 

To quantify player workload, a composite metric was constructed, informed by the High Metabolic Load Distance (HMLD) concept, designed to approximate the physiological load associated with varying running intensities. This approach was necessitated as the available data provided acceleration counts but not associated distances. 

**6** 



## **Methodology** 

### **5.1 Nature of Workload in Association Football** 

Association Football (soccer) is a predominantly **running-based intermittent team sport** , characterized by frequent bouts of acceleration, deceleration, and directional change, interspersed with periods of low-intensity movement. Unlike contact-dominant sports, collisions are relatively infrequent, and upper-body load is minimal; consequently, **locomotor activity** represents the principal component of player workload. At the elite level, outfield players typically cover **approximately 10 kilometres per match** [1], with performance output distributed across varying intensity zones. 

### **5.2 Workload Measurement** 

To quantify player workload a **composite workload metric** was constructed, informed by the **High Metabolic Load Distance (HMLD)** concept used by the commercial GPS provider **STATSports** . HMLD is defined as “The distance travelled by a player when their Metabolic Power (Energy Consumption per Kilogram per Second) is above the value of 25.542 W/Kg[2] studies have shown a link between HMLD and fatigue [3] 

In the STATSports framework, HMLD combines distances covered at high speed with distances accumulated during rapid accelerations and decelerations, representing moments of elevated metabolic demand. 

However, the present dataset—derived from **Wyscout computer-vision tracking data** —includes acceleration and deceleration **counts** but not their associated distances. Accordingly, the available variables were combined on a standardized scale to construct a comparable workload indicator. Distance-based and count-based variables were first normalized independently to a **0–1 scale** , after which they were aggregated, using an unweighted average, to form the final composite workload score. The contributing components are summarized in **Table 2** . 

**Table 2: Fatigue Components** 

|Basis|Speed (kmph)|Wyscout Metric|Basis|
|---|---|---|---|
|Distance in<br>Kilometres|20 – 25|HSR Distance|Distance in<br>Kilometres|
|Distance in<br>Kilometres|25<|Sprinting Distance|Distance in<br>Kilometres|
|Count||High Speed<br>Accelerations|Count|
|Count||High Speed<br>Decelerations|Count|



**7** 



### **5.3 Fatigue Estimation: Acute–Chronic Workload Ratio (ACWR)** 

To model the accumulation of fatigue, I applied the **Acute–Chronic Workload Ratio (ACWR)** , a measure widely adopted in sports performance research and endorsed by the **International Olympic Committee (IOC)** for monitoring training load and injury risk [4]. 

Formally, ACWR is defined as the ratio of an athlete’s **short-term workload** (acute load) to their **long-term workload** (chronic load): 



This ratio captures deviations from typical workload patterns, where values above 1.0 indicate an acute workload exceeding the recent baseline (suggesting potential fatigue or overload), and values below 1.0 indicate a relative reduction in recent exertion. 

For each player, ACWR values were computed for every match using individual workload histories. To capture collective team fatigue, player-specific ACWR values were **averaged across all starting outfield players** to produce a **team-level fatigue index** for each fixture. 

### **5.4 Linking Fatigue to Shooting Behaviour** 

The resulting ACWR-derived fatigue measure was then linked to event-level shot data. Specifically, the proportion of shots taken within different **ACWR intervals (“buckets”)** was analyzed to examine how variations in recent workload relate to shot generation and shot quality. The corresponding distribution is presented in **Figure 2** , illustrating the percentage of shots occurring across the observed workload ratio ranges. **Figure 2** 



**8** 



## **Results** 

The primary finding of note concerns team-based metrics: 

A significant negative relationship was identified between team-level fatigue and shot volume (the number of shots at goal taken in a match) however a low correlation value indicates that this explains very little of the variation (p<0.001, R<sup>2</sup> =0.12) indicating reduction of 1 shots per game per unit of ACWR added. 

**Figure 3: Boxplot of Shot Volume per team, grouped by fatigue** 



A secondary, albeit statistically non-significant relationship was observed (p= 0.1, R<sup>2</sup> =0.007), linking fatigue to shot quality when measured at a one week delay, which although statistically insignificant would appear worth further investigation. 

Collectively, these results indicate that the relationship between fatigue and shooting performance at the elite level is minimal 

**9** 



## **Discussion** 

This study set out to quantify the impact of accumulated fatigue on the most decisive action in football: shooting. Contrary to our initial hypotheses and much of the literature on fatigue and technical skills, the results reveal a strikingly modest relationship at the elite level. The most robust finding was a statistically significant but practically small decrease in shot volume with increased team-level fatigue (H1 supported at team level). The absence of a significant relationship at the individual player level for either volume or quality (H1 & H2 not supported) is particularly noteworthy. This suggests that the primary "fatigue penalty" is not borne by the shooter's technique, but rather by the team's collective ability to generate shot opportunities in the first place. A fatigued team may be less effective at winning the ball back in advanced areas or sustaining possession to create shooting angles, indirectly reducing volume. 

The very weak relationship with shot quality (H2 not supported) challenges the notion that fatigued players consistently take worse shots out of desperation or impaired judgment. Several factors, inherent to the modern game, may explain these muted effects. The widespread adoption of **fivesubstitution rules** allows managers to strategically offset acute fatigue within matches. Furthermore, sophisticated **load management and squad rotation policies** likely prevent players from entering matches in a state of extreme fatigue, creating a selection bias in our data where the most fatigued players are simply not selected to play. As such, this study may be measuring the effect of fatigue in a system specifically designed to mitigate it. 

Our findings align with the concept of **maintained performance under fatigue** , where elite athletes exhibit a remarkable capacity to preserve technical skills and decision-making accuracy even under physiological duress, a skill that may be honed through repeated exposure in training and competition. 

## **Limitations and Future Direction** 

While this study identifies some limited relationships between fatigue and shot-related 

performance, several caveats should be noted regarding the data, assumptions, and scope of analysis. 

A primary limitation is the omission of training load data, which constitutes a substantial portion of overall player workload. Professional clubs typically monitor and adjust training intensity in response to fixture congestion, so the absence of training data likely reduces the observable variation in fatigue. In effect, teams with higher match loads may compensate through modified training regimens, masking stronger underlying relationships. 

Second, all data were collected in the era of five substitutions per match. The expanded substitution rule has been shown to mitigate the impact of acute fatigue by allowing coaches to manage workloads dynamically within matches. Similarly, rolling squad rotation and load management strategies mean that players with extreme fatigue levels are less likely to be fielded, further diminishing measurable effects. 

Third, the study assumes that physical metrics derived from match tracking data accurately represent exertion. However, factors such as tactical role, opposition style, and match context 

**10** 



(e.g., game state or scoreline) influence running profiles independently of fatigue. For example, players in possession-dominant teams or those defending deep may record lower high-intensity distances without being less fatigued. The model does not explicitly control for these contextual tactical variables. 

Fourth, estimation methods were necessary for matches without full physical tracking coverage— especially for international fixtures and domestic cup competitions. Although reasonable assumptions were made (e.g. assigning typical running loads for partial minutes or international play), these imputations inevitably introduce noise and potential bias into the workload calculations. 

Finally, the analysis focuses exclusively on 90 minute regular season league matches. Knockout fixtures and games involving extra time likely generate more extreme fatigue conditions, which may reveal stronger effects on shot creation or quality. Similarly, this work does not distinguish between positional groups or playing styles, both of which may moderate the relationship between fatigue and performance. 

Collectively, these limitations suggest that the observed relationships between fatigue and shot outcomes are likely conservative estimates. The findings should therefore be interpreted as evidence of a minimal _net_ effect in a context where elite teams actively manage fatigue. Future work incorporating training data, tactical context, and positional differences, as well as extending to competitions with higher physical demands, may yield a more complete understanding of how cumulative workload influences football performance. 

## **Conclusion** 

This investigation leveraged large-scale event data and physical metrics to test the direct link between accumulated workload and shooting performance in elite football. While a small "fatigue penalty" on team shot volume was identified, the overall findings indicate that the relationship between fatigue and shot-related outcomes is minimal in contemporary elite football. The primary contribution of this work is twofold. First, it provides a replicable framework for integrating physical tracking data with performance outcomes to address sport science questions. Second, and perhaps more importantly, it challenges the assumed direct link between workload and degradation in key performance indicators, suggesting that the advanced load management strategies employed by top clubs are effectively insulating on-pitch performance from the effects of fixture congestion. 

For practitioners, the results suggest that concerns over fatigue may be better directed towards its impact on injury risk and defensive structure rather than a direct degradation of attacking output. For researchers, future work should seek to incorporate training load data, explore positional differences, and extend this analysis to more extreme fatigue environments, such as knockout tournaments with extra time or periods of severe fixture congestion, where stronger effects may yet be uncovered. 

**11** 



## **References** 

[1] Osgnach, C., Poser, S., Bernardini, R., Rinaldo, R., & Di Prampero, P. E. (2010). _Energy cost and metabolic power in elite soccer: A new match analysis approach. Medicine & Science in Sports & Exercise_ , **42** (1), 170–178. <u>https://doi.org/10.1249/MSS.0b013e3181ae5cfd</u> 

[2] STATSports. (n.d.). _High Metabolic Load Distance._ Retrieved from - - - - - <u>https://elitesupport.statsports.com/hc/en us/articles/18374670690205 High Metabolic Load Distance</u> 

[3] Young, D., Malone, S., Collins, K., Mourot, L., Beato, M., & Coratella, G. (2019). _Metabolic power in hurling with respect to position and halves of match-play. PLoS ONE_ , **14** (12), e0225947. <u>https://doi.org/10.1371/journal.pone.0225947</u> 

[4] Soligard, T., Schwellnus, M., Alonso, J.-M., et al. (2016). _How much is too much? (Part 1): International Olympic Committee consensus statement on load in sport and risk of injury. British Journal of Sports Medicine_ , **50** , 1030–1041. 

**12** 


