<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2025/2025 - Modelling player performance after potential transfers between leagues Richard Mc Intosh Tobias Beckmann.docx - Unknown Authors.pdf -->



# **Modelling player performance after potential transfers** 

# **between leagues** 

How much can be explained by athleticism? 

### Richard McIntosh and Tobias Beckmann 

## **1. Introduction** 

This study investigates the different physical contexts of the top five leagues and how athletic ability is required or leveraged differently in the leagues to lead to player output. This study has led to models being generated that will project player performance when transferring from one league to another based on their physical metrics, the leagues they’re moving from/to and the position they play. 

## **2. Motivation and Aim** 

The motivation and inspiration for this study comes from a series of themes which can loosely be grouped into two categories: football transfers and player aging. The aim is to provide a model that projects inter-league transfers without relying on transfer data between leagues. 

#### **2.1. Transfers** 

Transfers are great. They are crucial to a football club’s competitiveness, but they are also more often than not failures. 

When a player transfers between leagues, it is not possible to apply a “dampening coefficient” to the output to predict the output of a player. In the summer 2025 transfer window, a notable number of transfers between Premier League clubs for players with “modest” output for inflated fees were performed, which can partly be explained by the financial strength of the selling clubs, but the reason the buying clubs did not walk away can partly be explained by the lack of predictability of success when signing players from other leagues into the Premier League. Finally, due to the lack of inter-league transfers, it is not reliable to model transfers between leagues using data from transfers. From this problem, the aim to model transfers between leagues without relying on existing transfer data was born. 

#### **2.2. Physical Correlations to ability** 

In sport generally but also in football there already exists two commonly accepted concepts that highlight physical attributes to player ability. 

**1** 



The age curve is a popular concept in sport, it presents that there is a correlation between a player’s utility to a team and their age. The peak of the curve is a relatively straightforward story of a player becoming more athletic and improving his skills. However, the second part is a far more interesting story of a player attempting to compensate for their lost athletic ability with increased skills. 

## **3. Literature Review** 

#### **League-Specific Physical Demands and Contextual Differences** 

The comparative analysis of physical demands across Europe's elite football leagues has gained substantial research attention in recent years, particularly regarding implications for inter-league player transfers. SkillCorner's (2020) comprehensive broadcast tracking analysis of the Big Five European leagues revealed that the English Premier League demonstrates the highest intensity metrics across multiple physical dimensions, including high-intensity activities, peak sprint velocity, and total sprinting volume. This finding has been empirically validated by Morgans et al. (2024), who specifically compared acceleration and deceleration demands between the Premier League and Ligue 1, demonstrating that Premier League players perform significantly more high-intensity accelerations and decelerations per minute than their French counterparts. 

Importantly, Morgans et al. (2024) identified position-specific variation in these demands, with center forwards showing no significant differences between leagues while other positions demonstrated substantial variance. This position-specific heterogeneity suggests that physical adaptation requirements vary considerably across playing roles, a critical consideration for transfer prediction models. Chainok et al. (2025) further demonstrated that competitive level substantially influences both external load metrics and internal physiological responses, with semi-professional players exhibiting superior cardiorespiratory capacity enabling them to cover greater distances at elevated heart rates during match play. The fundamental challenge of predicting player performance across different competitive contexts has been explicitly acknowledged by industry analysts. Carey (2020) identified inter-league performance translation as "one of the hardest but most important tasks" facing the football analytics community, noting that the scarcity of direct inter-league transfer data makes traditional empirical modeling approaches impossible. FiveThirtyEight's Soccer Power Index methodology addresses this gap through league strength ratings derived from cross-league match results, though this team-level approach does not capture player-specific physical adaptation requirements. 

#### **Position-Specific Physical Demands and Machine Learning (ML) Categorisation** 

Recent research has challenged traditional position-based categorization systems, demonstrating that machine learning approaches may provide superior frameworks for understanding physical demands. De Haan et al. (2025) compared conventional positional groupings with unsupervised 

**2** 



k-means clustering based on match-specific running performance, finding that ML-based categorization yielded significantly lower within-group variance and larger standardized differences between groups for total distance, low-intensity running, high-intensity running, and sprint distance. Their research demonstrated that 20-meter sprint speed differed significantly between ML-derived clusters but not between traditional playing positions, suggesting that conventional positional categories mask important inter-individual variation in physical capacity. 

Jerome et al. (2024) advanced understanding of position-specific demands by contextualizing physical outputs within match phases, demonstrating that physical requirements during transitions substantially exceed 90-minute averages across all positions. Center backs exhibited the lowest absolute metrics but demonstrated the highest frequency of high-intensity accelerations and decelerations during defensive transitions, while fullbacks covered the greatest sprint distances during both defensive transitions and fast attacks. This phase-specific analysis provides crucial insights for understanding the tactical contexts that drive physical demands. 

Ferraz et al.'s (2023) comprehensive framework for tracking devices and physical performance analysis synthesized evidence across team sports, confirming that GPS-based systems provide valid and reliable data for monitoring external training load while emphasizing that interpretation must account for tactical and positional context. Toivonen et al. (2025) demonstrated that small-sided games can effectively replicate official match physical demands when appropriately designed, providing practical guidance for training periodization. 

#### **Age Curves and Physical Performance Decline** 

Understanding age-related performance changes has become increasingly sophisticated through the application of advanced statistical modeling techniques. Guan and Swartz (2024) established strong correlations (0.822-0.908) between maximum acceleration capacity and overall performance measures across playing positions, demonstrating that acceleration-based metrics serve as readily measurable proxies for performance capacity and provide early indicators of performance decline before changes become evident in traditional match statistics. 

Säfvenberg et al. (2024) utilized generalized additive models to demonstrate that peak performance generally occurs by age 27, with substantial position-specific variation. Forwards achieved peak performance earliest (around age 23), followed by midfielders and defenders (26-28 years), while goalkeepers peaked latest but demonstrated extended performance plateaus. Performance decline post-peak was steepest among forwards and midfielders, while defenders and goalkeepers experienced long-lasting, gradual decline patterns. 

Oterhals et al. (2021) analyzed Ballon d'Or nominations as a proxy for elite-level peak performance, finding that individual peak performance occurs around 27-28 years with position-specific variation ranging from 26 to 31 years. Goalkeepers were nominated latest and maintained elite status longest, consistent with the hypothesis that positions less dependent on explosive physical 

**3** 



attributes demonstrate delayed aging curves. Caley (2025) advanced aging curve methodology through the Marcel projection system, implementing regressed weighted averages that account for position-specific patterns while recognizing substantial individual variation in aging trajectories. 

#### **Integration and Synthesis** 

The recent literature establishes three key principles relevant to analyzing physical performance and predicting inter-league transfer outcomes. First, substantial and quantifiable differences exist in physical demands across Europe's top football leagues, with the Premier League consistently demonstrating the highest intensity metrics, particularly in acceleration-based demands (Morgans et al., 2024; SkillCorner, 2020). These differences are not uniform across positions, with center forwards showing minimal inter-league variation while other positions demonstrate substantial physical context differences that may require significant adaptation when players transfer between leagues (Morgans et al., 2024). 

Second, position-specific analysis is essential, as different playing roles demonstrate distinct physical profiles and adaptation requirements (de Haan et al., 2025; Jerome et al., 2024; Morgans et al., 2024). The emergence of machine learning categorization approaches suggests that traditional positional groupings may mask important inter-individual variation in physical capacity, though conventional position-based frameworks remain widely utilized in practice and provide meaningful differentiation in physical demands (de Haan et al., 2025). Understanding physical requirements within specific match phases—particularly transitions—provides additional context for assessing the complete physical demands players face in different competitive environments (Jerome et al., 2024). 

Third, age-related performance changes follow position-specific patterns that must be incorporated into predictive models (Guan & Swartz, 2024; Säfvenberg et al., 2024). The consistent finding that acceleration capacity correlates strongly with performance decline (r > 0.82) provides particular support for including acceleration-based metrics in models assessing physical adaptation across competitive contexts (Guan & Swartz, 2024). Peak performance timing varies substantially by position, from age 23 for forwards to extended plateaus for goalkeepers, suggesting that age effects interact with positional physical demands in complex ways that require flexible, non-linear modeling approaches (Säfvenberg et al., 2024). 

The convergence of these research streams supports integrated methodological frameworks using standardized physical tracking data to quantify league-specific demands, building position-specific models incorporating physical attributes alongside contextual factors such as age, and recognizing that inter-league performance prediction remains a significant gap in football analytics where traditional empirical modeling approaches are constrained by limited transfer data (Carey, 2020). The present research addresses this gap by developing a novel approach that quantifies physical adaptation requirements without relying on historical inter-league transfer outcomes. 

**4** 



## **4. Hypothesis** 

Player performance is a function of various properties: 

- Age 

- Skill / Technique 

- Athletic ability 

- Quality of team they play for 

Physical attributes are one factor that influence players' performance. We predict that by modelling a player’s athletic ability and taking into account age and team quality, we can accurately project player performance from one league to another. 

## **5. Data & Methodology** 

The data used for this study was entirely provided by Hudl Statsbomb, Statsbomb Events and Physical tracking were used to compare physical contexts and outputs for players. Data for the 2024-25 season was provided for the English Premier League, Ligue 1, La Liga, Serie A and the 1. Bundesliga. 

#### **5.1. Data Acquisition and Processing** 

Physical metrics including high-intensity running distance, total distance, and acceleration statistics were collected alongside comprehensive event data for position-specific performance analysis. Event data was leveraged for proxies of athletic attributes, such as aerial duels won for strength. Player features and outputs were flattened into a single table, with players grouped based on their competition and “position group”. If a player played 1,200 minutes as a striker and 1,000 minutes as a winger, they would be represented twice with their output at each position grouped and shown separately according to what was achieved in each role. The outputs and features were normalised onto a per 90 minutes basis where applicable. 

#### **5.2. Position grouping and record filtering** 

To provide larger sample sizes for the statistical analysis of positions, players were grouped into broad categories: 

- Center backs 

- Fullbacks 

- Central Midfielders 

- Wingers 

- Strikers 

**5** 



The mapping of Statsbomb positions to the position groups can be found Table 1. Players who had played fewer than 600 minutes in a specific position group for the 2024/25 season were filtered out for the analysis. 

_Table 1:Position grouping overview._ 

|**Position Group**|**Positions**|
|---|---|
|Fullbacks|RB, LB, RWB, LWB|
|Centre backs|CB, RCB, LCB|
|Central Midfelders|CM, RCM, LCM, CDM, RDM, LDM|
|Wingers|RW, LW, RM, LM, CAM, RAM, LAM|
|Strikers|ST, CF, RCF, LCF, SS|



#### **5.3. League-Based Physical Contexts** 

Initial analysis on the difference in events and physical metrics was performed to highlight differences in the physical demands between the leagues. 

#### **5.4. Position-group league-based contexts** 

From the initial league-based contexts, a more specific league-position pairs focus was taken to describe more precisely what the physical demands for a specific position in each league entails. These results were aggregated to produce a single indicative number for change in physical context for players moving into the Premier League. 

#### **5.5. Feature Engineering and Correlation Analysis** 

After the physical comparisons between leagues for our initial analysis, we used a wide range of features and output variables, with over 90 features and outputs in the flattened table. Various levels of statistical analysis were then applied to this table. 

1. Single variable linear regression 

2. Multi variable linear regression 

3. LASSO regression 

4. Random forest correlation 

5. Gradient boosting 

**6** 



## **6. League-Based Physical Contexts** 

In the following section, we analyse physical features and how they compare across leagues. First, we will introduce the statistical methods employed, focusing on total distance per match, before analysing other physical features at both the per-match and per-player levels. 

#### **6.1. Distribution of physical features per match** 

The intensity of each match varies, and each player has different physical attributes. A density distribution plot shows how values of a continuous variable are distributed. The area under the curve indicates the relative likelihood of different outcomes across the range of possible values. A kernel density estimate (KDE) smooths the density distribution in order to isolate the key characteristics of the distribution when data is limited and/or unreliable. In Figure 1, we see the KDE for total distance by competition. 



_Figure 1: Normalized distributions of the total distance per competition. The leagues are indicated by the different colors._ 

We can observe that there are indeed differences between leagues. In Ligue 1, the total distance covered by both teams in most matches was more than 225 km, whereas in the other leagues it was less than 225 km. 

A box plot illustrates the distribution of a continuous variable by plotting its empirical quantiles. The box covers the 25th to 75th percentile range (i.e. the middle 50% of observations fall within this range). The median is indicated by the division of the box, i.e. the value below which 50% of observations fall and above which 50% of observations fall. The whiskers indicate the maximum and minimum observations in the distribution, with outliers omitted for clarity. For normal distributions, the mean and median are the same due to the symmetry of the distribution. For other 

**7** 



distributions, however, the mean may deviate from the median and is more sensitive to outliers. In Figure 2, we can see the box plot for total distance by competition. 



_Figure 2: Distributions of the total distance as boxplot. Different leagues are indicated by different boxes. The blue area marks the 25_<sup>_th_</sup> _and 75_<sup>_th_</sup> _percentiles. The median is described by the black line, while the yellow line marks the mean._ 

This provides further insight into the quantiles of the distributions. For example, in around 50% of Ligue 1 matches, the total distance covered was at least 225 km, whereas in the other leagues, this figure was no more than around 25%. 

We chose the Kolmogorov–Smirnov test to evaluate whether the distributions of a feature differ significantly between leagues. As it is non-parametric, it can be used to compare distributions where the specific distribution is unknown and cannot be described by a mathematical formula. The test statistic is derived as the maximum distance between two empirical distribution functions (𝐹). The test statistic used to determine whether 𝐹 with 𝑛 observations and 𝐹 with m 1,𝑛 2,𝑚 observations differ significantly is formally defined as follows: 



**8** 



The null hypothesis that there are no significant differences between the two distributions is rejected in favor of the alternative hypothesis that the distributions differ significantly at the confidence level α if: 



Without going into mathematical details, we can observe: 

- The lower / more stringent the confidence level (α), the greater the deviation required for the two distributions to be considered significantly different. The confidence level measures how likely we accept the possibility of falsely rejecting the null hypothesis when it is actually true. Therefore, we require the distributions to deviate more at stricter confidence levels. 

- The more observations we have, the less the two distributions need to differ to be considered significantly different from each other. The greater the number of observations, the more certain we can be that the empirical distribution from the sample matches the true underlying distribution from the population. Consequently, we can reject the null hypothesis even for smaller deviations between the two distributions. 

Figure 3 depicts the differences in means between the leagues in a pairwise comparison, whereby the league mean on the y-axis is subtracted from the league mean on the x-axis. Red indicates that the y-axis league mean is larger than the x-axis league mean. The top value in each field shows the difference in means, while the bottom value shows the p-value of the Kolmogorov–Smirnov test. If the distributions are statistically significant at a 5% confidence level, the p-value is highlighted in bold. If the distributions are not statistically significant, the p-values are in brackets. 



_Figure 3: Pairwise comparison of the total distance between leagues. Red color indicates a larger total distance for the league on the y-axis compared to the league on the x-axis, while blue color indicates a lower total distance. Bold values show a statistically significant difference._ 

**9** 



On average, the total distance covered in Ligue 1 is around 15 km more than in Serie A, and the distributions between most leagues differ significantly, except between the Premier League and Serie A, and the Premier League and the Bundesliga. In conclusion, this suggests that Ligue 1 requires significantly greater endurance than the other leagues. 

Analysing the total sprinting distance, we observe a different pattern (see Figure 4, Figure 5 and Figure 6). The Premier League has the highest total sprinting distance per match, while the Bundesliga has the lowest. Although Ligue 1 has the greatest total distance covered, it is not significantly different from the other leagues in terms of total sprinting distance. In the Premier League, more than 50% of matches involved a total sprinting distance of 5 km or more. By contrast, in all the other leagues, this figure was at most around 25%. 



_Figure 4: Normalized distributions of the total sprinting distance per competition. The leagues are indicated by the different colors._ 

**10** 





_Figure 5: Distributions of the total sprinting distance as boxplot. Different leagues are indicated by different boxes. The blue area marks the 25_<sup>_th_</sup> _and 75_<sup>_th_</sup> _percentiles. The median is described by the black line, while the yellow line marks the mean._ 



_Figure 6: Pairwise comparison of the median total sprinting distance between leagues. Red color indicates a larger total sprinting distance for the league on the y-axis compared to the league on the x-axis, while blue color indicates a lower total sprinting distance. Bold values show a statistically significant difference._ 

On average, the total sprinting distance in the Premier League is 1.2 km greater per match than in the Bundesliga, which has the lowest average sprinting distance. Furthermore, all of the distributions are significantly different from each other, except for La Liga and Serie A. In conclusion, these findings suggest that the Premier League requires significantly more sprints than the other leagues. 

**11** 



Shifting the focus of the analysis to duels reveals the following when it comes to aerial and ground duels, as depicted in Figure 7. The Bundesliga had the most aerial duels, while Ligue 1 had the fewest. 



_Figure 7: Distributions of the total aerial duels per competition as boxplot. Different leagues are indicated by different boxes. The blue area marks the 25_<sup>_th_</sup> _and 75_<sup>_th_</sup> _percentiles. The median is described by the black line, while the yellow line marks the mean._ 

When it comes to ground duels, the statistics are flipped, shown in Figure 8. Ligue 1 has the most ground duels per match, while the Bundesliga has the second fewest. 



_Figure 8: Distributions of the total ground duels per competition as boxplot. Different leagues are indicated by different boxes. The blue area marks the 25_<sup>_th_</sup> _and 75_<sup>_th_</sup> _percentiles. The median is described by the black line, while the yellow line marks the mean._ 

**12** 



#### **6.2. Distribution of physical features on a player basis** 

At player level, there is a significant difference in the percentage of high acceleration between leagues. High acceleration percentages are defined as 

𝐶𝑜𝑢𝑛𝑡 𝐻𝑖𝑔ℎ 𝐴𝑐𝑐𝑒𝑙𝑒𝑟𝑎𝑡𝑖𝑜𝑛𝑠 ℎ𝑖𝑔ℎ 𝑎𝑐𝑐𝑒𝑙𝑒𝑟𝑎𝑡𝑖𝑜𝑛 𝑝𝑒𝑟𝑐𝑒𝑛𝑡𝑎𝑔𝑒= , 𝐶𝑜𝑢𝑛𝑡 𝐻𝑖𝑔ℎ 𝐴𝑐𝑐𝑒𝑙𝑒𝑟𝑎𝑡𝑖𝑜𝑛𝑠+𝐶𝑜𝑢𝑛𝑡 𝑀𝑒𝑑𝑖𝑢𝑚 𝐴𝑐𝑐𝑒𝑙𝑒𝑟𝑎𝑡𝑖𝑜𝑛𝑠 

where a medium acceleration is measured between 1.5 m/s<sup>2</sup> to 3 m/s<sup>2</sup> whilst a high acceleration is 3 m/s<sup>2</sup> or greater. 

We compare the high acceleration percentages between leagues, shown in Figure 9 and Figure 10. Once again, the Premier League is the sportiest, with the highest acceleration percentages and a significantly different distribution to the other leagues. Bundesliga has the lowest percentage of high accelerations and significantly different distributions compared to all the other leagues, except Serie A. Ligue 1 and La Liga also exhibit significant differences in their distributions. 



_Figure 9: Normalized distributions of the high acceleration percentages per competition. The leagues are indicated by the different colors._ 

**13** 





_Figure 10: Pairwise comparison of the mean high acceleration percentages between leagues. Green color indicates a larger high acceleration percentage for the league on the y-axis compared to the league on the x-axis, while red color indicates a lower high acceleration percentage. Bold values show a statistically significant difference._ 

#### **6.3. Physical Demand Index** 

When we look at the physical features required for each position separately, we can also observe the noticeable differences in the physical requirements for each position. Visualisations and distributions of significant features can all be seen in the appendix. To summarise the differences in physical demands of leagues for specific positions, a “Physical Demand Index” (PDI) was calculated based on the following, identified features: 

- high-speed running (HSR) ratio, defined as 

𝐻𝑖𝑔ℎ 𝑆𝑝𝑒𝑒𝑑 𝑅𝑢𝑛𝑛𝑖𝑛𝑔 𝐷𝑖𝑠𝑡𝑎𝑛𝑐𝑒 𝑖𝑛 𝑚𝑒𝑡𝑒𝑟𝑠 𝑅𝑢𝑛𝑛𝑖𝑛𝑔 𝐷𝑖𝑠𝑡𝑎𝑛𝑐𝑒 𝑖𝑛 𝑚𝑒𝑡𝑒𝑟𝑠 

(where a high-speed run is a run between 20 km/h and 25 km/h and a regular run between 15 km/h and 20 km/h) 

- high acceleration percentage (as defined previously) 

- sprinting distance per 90 (where a sprint is any run over 25 km/h) 

- max speed median 

   - (which is the median max speed a player obtain across all matches played that season) 

- total distance per 90 

- aerial duels per 90 

The PDI is a weighted calculation of the difference in distribution of the six features across the league to produce pair-wise comparisons between league A and B for the aggregated six features: 

**14** 





where: 





Kolmogorov-Smirnov test. Distributions that are less similar to each other would have a higher weight. 

The distributions of each league and feature are weighted by play time using: 





The comparison between leagues using the Physical Demand Index yielded the results shown in Figure 11. 

**15** 





_Figure 11: Physical demand index by leagues (y-axis) and positions (x-axis) compared to the Premier League. Green color would indicate a larger value than Premier League, while red color indicates a lower value. Bold values show a statistically significant difference._ 

This concludes that the smallest adaption to physicality for strikers moving to the Premier League are from La Liga and there is a significant change in physical context for strikers from the other three leagues. For wingers, the physical context of the Premier League is substantially different to the other leagues with the Bundesliga providing the largest contrast. For central midfielders Ligue 1 provides the smallest transition but still substantial whilst Bundesliga is still the largest change. Fullbacks have the biggest divergence between the leagues where the physical context for most the leagues is reasonably similar to the Premier League apart from the Bundesliga which is drastically different. There is also a substantial change in physical context for all centre backs moving to the Premier League, while there are no considerable differences between the other leagues. 

This summarisation of the physical contexts of positions supports the previous league-wide findings, indicating that the Premier League provides a significantly different physical context compared to other leagues. With La Liga being the closest match to intensity of accelerations and intensity, Ligue 1 providing the most eventful matches but at a lower intensity than La Liga or the Premier League, and with Serie A and the Bundesliga significantly lacking the number, speed or intensity of sprints and duels. 

**16** 



At this point it is important to challenge why, based on the financial advantage of the Premier League it might be that they can afford more rotation options to replace their players with, keeping the physical intensity of the league high but without that intensity burdening specific players more than players from other leagues. It is investigated in Figure 12. It shows no significant difference between leagues, in particular when accounting for less games in Bundesliga and Ligue 1. Hence, we cannot confirm or reject this hypothesis. 



_Figure 12: Distributions of the total minutes played per competition as boxplot. Different leagues are indicated by different boxes. The blue area marks the 25_<sup>_th_</sup> _and 75_<sup>_th_</sup> _percentiles. The median is described by the black line, while the yellow line marks the mean._ 

Now that it has been established that there are significant differences in the physical context between the leagues, these differences could explain why it is difficult to project transfers between them. 

Another key feature of the physical context is age. Here, we will analyse how age curves differ by position using a simple weighted minutes analysis of the age distribution of players who have played more than 600 minutes in a position. It is depicted in Figure 13. 

**17** 





_Figure 13: Normalized distributions of player’s age. The leagues are indicated by the different colors._ 

The plot shows that only for Wingers the age curves differ significantly, where wingers tend to be younger than players on other positions. This is consistent with Michael Caley’s blog post on aging - - - - - curves <u>https://www.expectinggoals.com/p/building marcel part ii age curves</u> and does not actively contradict Tom Worville’s piece on age curves for positions - - - - - - <u>https://www.nytimes.com/athletic/2935360/2021/11/15/what age do players in different position s-peak/.</u> 

Strikers also show a peak at a slightly younger age but there is no significance in the distribution compared to other positions and since this is only a single season of data across five leagues, we should not draw conclusions about Strikers. 

In conclusion we have evidence that the physical contexts between leagues do vary between the Premier League and the other big five leagues across all positions, and that this is specifically important for Wingers. The focus now moves to whether we can quantify the effects of these changes. 

## **7. Specifications of the analysis** 

#### **7.1. Positional “Output” metrics** 

To help find correlations and focus the scope of the study, two outputs were identified for each position group to define “good” and “bad” players. To find the correct outputs for each positional group, statistical analysis was performed to highlight which outputs were most important for each position. Cohen’s d analysis was performed across all output metrics and positions to see the 

**18** 



outputs most significant for each position. From this analysis the features shown in Table 2 were selected. 

_Table 2: Selected output metrics for the different positions._ 

|**Position Group**|**Output Metrics**|
|---|---|
|Strikers|Expected Goals per 90|
||Progressive passes received|
|Wingers|Passes and dribbles into penalty area|
||Expected goals and assists per 90|
|Central Midfelders|Tackles and interception per 90*<br>Pass on-ball-value per 90*|
|Fullbacks|Pass on-ball-value per 90|
||Tackles and interceptions per 90|
|Centre backs|Progressive passes per 90|
||Defensive actions on ball value per 90|



Central Midfielders had no output metrics that were significant from the analysis, for this reason pass on-ball-value (OBV) as well as tackles and interceptions were selected. The distributions of outputs across player groups, weighted by minutes can be seen in the appendix. 

#### **7.2. Features Set** 

Now that the dependent variable for measuring the output metrics has been selected for analysis, we will now look into the independent variables. The variables shown in Table 3 have been selected because they provide an understandable representation of athletic attributes. Other features have also been included to help separate noise. 

_Table 3: Selected features for the different positions._ 

|**Feature**|**Justifcation**|
|---|---|
|Age|Based on appreciation of age curve, as a player gets older,<br>they develop skills to adapt for losing athletic ability which<br>needs to be accounted for.|



**19** 



|League rank|The quality of the team a player plays for may boost their<br>output, especially in attacking positions. To model physical<br>and output correlations, the league ranking needs to be<br>accounted for.|
|---|---|
|High acceleration percentage|A feature which describes**acceleration**of a player. As<br>defned in 6.2.|
|Median max speed|The median max speed a player has achieved in each game<br>over a season to highlight their**sprint speed**.|
|Aerial duel win percentage|A quantifcation of how often a player wins aerial duels.<br>This is an indicator of**strength/size**.|
|High-speed running (HSR) ratio|The ratio of high-speed running distance and running<br>distance. An indicator of**endurance**.|
|Ground duel win percentage|An indication of**reaction times**.|
|Total distance|An indication of the overall**stamina**.|
|Sprint to total distance ratio|The ratio of sprint distance to total distance. An indicator<br>of the**play style**of the player.|



#### **7.3. Data Sets** 

Based on the 600-minute threshold, we have the sample sizes as depicted in Table 4 for each position group and league. 

_Table 4: Number of data points per league and position._ 

|**Position**|**Premier League**|**Bundesliga**|**Serie A**|**La Liga**|**Ligue 1**|
|---|---|---|---|---|---|
|Strikers|36|43|41|47|38|
|Wingers|91|59|78|92|74|
|Central<br>|82|68|91|84|73|
|Midfelders||||||
|Fullbacks|66|61|76|71|59|
|Centre backs|74|81|87|77|74|



Without the minutes threshold, the number of observations would be increased significantly however it would also increase the noise of the data. 

**20** 



## **8. Linear League-Positional Physical and Output Distributions** 

Initial analysis of the individual features and output variables produce a couple of visually notable results, but no significant correlations. This is expected, given that the relationship between a specific physical trait and output is unlikely to be linear. In fact, physical attributes combine to produce an overall impact. 

However, we find some hints for differences in importance of high acceleration percentage for strikers in the Premier League versus Bundesliga, as shown in Figure 14. 



_Figure 14: Expected goals as a function of the high acceleration percentage for the Premier League (red) and Bundesliga (teal) for strikers. The lines depict linear regression models._ 

In the Premier League, there is a hint at a correlation between high acceleration percentage and xG per 90, which is non-linear or cross-correlated with other features, whilst in the Bundesliga there is no such indication. A further interesting observation is that 50% of strikers in the Bundesliga have a lower high acceleration percentage than any striker in the Premier League aside from Joshua Zirkzee. 

For wingers there is a similar strong hint at a correlation between penalty box entries and acceleration, which does not show for the Bundesliga. This is depicted in Figure 15. 

**21** 





_Figure 15: Passes and dribbles into the penalty area as a function of the high acceleration percentage for the Premier League (red) and Bundesliga (teal) for wingers. The lines depict linear regression models._ 

## **9. LASSO Regression** 

#### **Methodology** 

LASSO (Least Absolute Shrinkage and Selection Operator) regression was employed as a regularized linear modeling approach to examine the relationship between physical features and position-specific performance metrics. Unlike standard linear regression or the gradient boosting models described in Section 8 and 10 respectively, LASSO provides both prediction capability and automatic feature selection through L1 regularization. This makes it particularly valuable for identifying which physical attributes demonstrate genuine linear relationships with player output, while eliminating redundant or weak predictors by shrinking their coefficients to exactly zero. 

#### **Model Specification** 

Separate LASSO models were constructed for strikers with the output variable xG per 90 and wingers for passes and dribbles into the penalty area per 90 across all leagues. The feature set were as described in Section 7, regression analysis was performed excluding and including league rank. The regularization parameter  was optimised using 5-fold cross-validation via the LassoCV λ implementation from scikit-learn. This approach systematically tests multiple  values and selects λ the one that minimizes cross-validated mean squared error, balancing model complexity against prediction accuracy. 

#### **Grouped LASSO without team rank adjustment** 

Table 5 presents LASSO coefficients for features without the league rank. For strikers, HSR ratio is the best predictor whilst for wingers high acceleration percentage was the dominant predicter. 

**22** 



However, these coefficients indicate that the relationship between these features and the outputs, if existent, are not linear. 

_Table 5: LASSO coefficients for the regression without the league rank as input features._ 

|**Feature**|**Striker (xG per 90)**|**Wingers (penalty area entries**<br>**per 90)**|
|---|---|---|
|Age|0.001|-0.024|
|High acceleration percentage|0.006|0.277|
|Median max speed|0.024|**0.000**|
|Aerial duel win %|0.002|-0.030|
|High-speed running (HSR) ratio|0.149|**0.000**|
|Ground duel win percentage|-0.001|0.006|



#### **Grouped LASSO with team rank adjustment** 

To isolate physical effects from team-level confounding, the LASSO models were re-run with league rank. The results are summarised in Table 6. As expected team quality showed strong associations with performance indicating that strikers on last-place teams generate 0.21 fewer xG per 90 than the first placed team while wingers produced 4.3 fewer penalty area entries. Attempting to control for team quality transformed physical feature coefficients notably. For strikers HSR ratio was eliminated entirely. For wingers, max speed became a significant predictor. 

_Table 6: LASSO coefficients for the regression with the league rank as input features._ 

|**Feature**|**Striker (xG per 90)**|**Wingers (penalty area entries**<br>**per 90)**|
|---|---|---|
|Age|**0.000**|-0.013|
|High acceleration percentage|0.006|0.239|
|Median max speed|0.017|0.277|
|Aerial duel win %|0.002|-0.025|
|High-speed running (HSR) ratio|**0.000**|**0.000**|
|Ground duel win percentage|**0.000**|**0.000**|



**23** 

-4.282 League Rank -0.212 



#### **Interpretation and Implications** 

The only feature that has evidence to support of a linear relationship is league rank. For strikers, the elimination of HSR ratio indicates that it’s predictive power initially was caused by it being a proxy for league quality. The fact that max speed became a significant predictor for wingers when introducing league rank indicates that team quality needs to be accounted for when trying to model the effects of athletic ability on physical performance. The contrasting results between models reveal the complex interplay between physical attributes, team context, and performance. Physical features operate through multiple pathways: (1) direct effects on individual capabilities (e.g., faster wingers beat defenders), and (2) indirect effects through team selection (faster wingers join better teams that create more opportunities). 

#### **League Specific LASSO with p-value** 

Given the substantial physical demand differences across leagues identified in Section 6, we estimated separate LASSO models for each league to assess whether physical-to-performance relationships are league-dependent. This addresses a critical limitation of pooled models: the assumption that coefficients are homogeneous across leagues. OLS regression was performed to evaluate the hypothesis that the LASSO coefficient for a feature was in fact 0. These probabilities of the coefficients are displayed in Figure 16 and Figure 17 in each cell. 

Team quality effects varied substantially across leagues. For strikers, coefficients ranged 2-fold from β=-0.144 (Serie A) to β=-0.285 (Ligue 1), while for wingers, the Premier League exhibited a large effect (β=-6.328) in comparison to the next strongest league (Serie A, β=-4.348). This suggests Premier League winger output is particularly team-quality dependent or that a higher level of talent is needed for a player to enter the penalty area in the Premier League than the others. 

Across 60 tests (5 leagues × 2 positions × 6 physical features), only 2 achieved significance at p<0.05: age for La Liga strikers (β=0.037, p=0.036) and aerial win percentage for Premier League strikers (β=0.081, p=0.003). For wingers, no physical features reached significance in any league. However, this likely reflects insufficient statistical power (n≈30-60 per league per position) rather than absence of true effects. Supporting this interpretation, HSR ratio showed uniformly positive coefficients for wingers across all five leagues (β=0.76 to 4.89), with marginal significance in Ligue 1 (p=0.068) and Serie A (p=0.072). This cross-league consistency suggests a genuine positive relationship that individual league samples lack power to detect reliably. 

**24** 





_Figure 16: Results of the LASSO regression for strikers. Red color indicates a positive feature to output correlation, while blue equals a negative correlation._ 



_Figure 17: Results of the LASSO regression for wingers. Red color indicates a positive feature to output correlation, while blue equals a negative correlation._ 

#### **Interpretations and Implications** 

The league-specific heterogeneity has critical implications for transfer prediction. Pooled models produced coefficient estimates (strikers: β=-0.212; wingers: β=-4.282) that represent weighted averages but obscure substantial variation. For instance, the pooled winger model underestimates the Premier League effect by 48% (β=-4.28 vs. -6.33). Furthermore, pooled LASSO eliminated HSR ratio for wingers (β=0.000), yet league-specific models show this feature is consistently positive across all leagues. 

In conclusion, non-linear analysis is required to confidently project player performance based on athletic attributes however there are clearly differences in the relationships between these features and leagues. 

**25** 



## **10.Non-Linear Regression** 

#### **Model** 

As shown before, we find that simple linear relations do not accurately describe the target variables. Hence, we deploy a machine learning algorithm, a boosted regression. The core idea behind boosted regression is to build a sequence of decision trees, where each successive model learns from the mistakes made by the previous ones. A decision tree is a straightforward model that makes predictions by repeatedly splitting the data into groups. This process produces a final, highly accurate model by ‘boosting’ the weak learners into a strong one. The ensemble output is typically a weighted combination of all the individual trees. Boosted regression is known to be robust against overfitting. This is a particular important feature due to dataset size, which becomes quite small when splitting the data by different leagues, positions, and train and test dataset. 

In the following, we will investigate different positions separately. The method is always the same: we input the features previously defined and train against the target variables. The target variables are investigated individually but also combinations of them: 

- The raw sum of both targets 

- The sum of the z-values of the normalized distributions of the targets 

- The logarithmic sum of the z-values of the normalized distributions of the targets 

- The product of the two variables normalized by their minimum and maximum values 

In the following, we will only show the results for original targets. Some of the combined targets lead to small improvements but for clarity we will focus on the raw output. The best parameters for the boosted regression (in particular, decision tree depth and number of trees) are found via a cross-search. The data is always split into training and test set in order to prevent overfitting. The results are always shown for the test set, so that the model did not see this data before. The goodness of our models is evaluated by the reduced Chi-square and the Pearson correlation between true value and predicted value. A Pearson correlation of one, while having a small Chi-square, hints to a perfect prediction power of the model, while zero means no prediction power at all. 

#### **Defenders and central midfielders** 

For fullbacks, centre backs and central midfielders, we did not find significant results, which support drawing relations between input features and target variables. Pearson correlations of true and predicted values mostly close to zero were found, only for few league and position combinations weak prediction power was found with a Pearson correlation coefficient < 0.3. It is up for debate whether the input features and target variables were chosen wrong for these positions, not enough data was available or if the models generally do not perform well for these positions. 

**26** 



#### **Strikers** 

The output variables for strikers (and wingers) are intuitively better defined than for defenders. This also shows for the training of the models. A Pearson correlation of around 0.662 was found for a model describing the xG-value for all leagues at once. This is shown in Figure 18. 



_Figure 18: Predicted output as function of the true value for strikers in the Premier League. The black line marks the 1:1-line. The plot shows test data, which was not used for training the model._ 

However, one observes that the tails of the xG-distribution is not well described by the model. This can have two reasons: either not enough data was available in the tails to accurately predict them or that the leagues are too different for valid extrema predictions. Both arise from the same issue, an overall lack of data points for strikers. Often, clubs play with only one main striker, which is also playing almost all the time. Other positions have more than twice the number of players and therefore this is a natural limitation of the training of the model. Especially, dividing the strikers by league is limiting the freedom of the model. For the results above we had around 180 data points for the training set, which is just enough for good predictions. Dividing this by 5 leagues, this is not enough data for league-wise models. 

As this analysis is centered around the Premier League and on transfers between leagues, it might be nice to see that training a model is overall possible. However, it is not benefiting the analysis, and no transfer predictions are possible with a single model. With more data, it should be possible 

**27** 



to have league-wise models. An improvement of the models compared to the overall model is anticipated, as the models would weigh the features differently according to the league requirements (cf. chapter 6). 

#### **Wingers** 

As above mentioned, wingers have a well-defined output, and the number of players is much larger. We train models for the different targets. The best results are found for the target variable ‘passes and dribbles into penalty per 90’, which is shown in the following. For simplicity, we only speak of the target variable instead of using the full name. 

The target shows strong correlations between predicted and true value for the Premier League model with a Pearson correlation of 0.78, as depicted in Figure 19 (left). It also shows the feature importance of the input (right). As expected, the league rank is the most driving factor with an importance of around 0.3. In particular, attackers depend strongly on the team performance. Second most important factors are the percentage of high accelerations and the ground duel win percentage, which is in agreement with the distributions shown in Chapter 6, indicating the importance of accelerations in the Premier League. 





_Figure 19: (Left) Predicted output as function of the true value for wingers in the Premier League. The black line marks the 1:1-line. The plot shows test data, which was not used for training the model. (Right) Feature importance for the trained model._ 

To clarify the importance of each feature, we check the target value as function of the individual input features, while keeping the other features constant at the median. It is depicted in Figure 20. This look in two dimensions absolutely ignores feature correlations, which are accounted in the boosted regression. Hence, weird looking and not monotonic shapes are produced. Still, it should yield an overview how the output is determined by the single features. It is depicted below. It shows once more the importance of the league rank, which mainly defines the output. The finetuning is then done by the other parameters, which still have significant influence. 

**28** 





_Figure 20: Impact of each feature on the target variable when keeping all other features constant at their median value. This depiction ignores possible cross-correlations, which are accounted for in the model._ 

We can use the model of the Premier League to find implications on transfers from one league to the Premier League. This can be done when assuming two things. First, the output baselines are similar for the different leagues, which was validated. They roughly agree with each other. Second, the league rank remains the same when transferred to the Premier League. We compare the performance in the own league (the true value) with the predicted output in the Premier League. Here, we define a change in output of ±2 as significant, defining if a player improves or worsens his output<sup>1</sup> . The results are shown in Figure 21, depicting the different leagues and the grouping into different classes. It shows Ligue 1 and Bundesliga have the worse changes than the other leagues. They have the largest fractions of players with worse output and the smallest fractions of players with better output. The amount of players remaining the stable is dominating in all leagues, except for the Serie A, where it is approximately equal to the number of players improving. 

> 1 These values are arbitrary set and should only give an indication. 

**29** 





_Figure 21: Prediction of players performance in the Premier League compared to their own league. The columns indicate different leagues. A delta of 2 was defined to group players as improving (green), stable (grey) or worsening (red)._ 

To make predictions on single player level, we need to train the other leagues too. Only if the model for the league is more or less agreeing with the true output of the player, the player can be predicted for transfer in the Premier League. For these players, we know that their output is well-defined by their athletic (and age and league rank), other features like technical skills are not significantly defining their output. For example, players like Lamine Yamal are overperforming their league-models a lot, as their technical skills are not regarded in the model. 

For the Bundesliga and La Liga good models were found, while Ligue 1 and Serie A do not show good prediction power. Hence, we will focus on Bundesliga and La Liga. Their results are shown in Figure 22 with strong prediction power and Pearson correlations of 0.668 (Bundesliga) and 0.562 (La Liga). These models should be good enough for making preliminary predictions. 





_Figure 22: (Left) Predicted output as function of the true value for wingers in the Bundesliga. The black line marks the 1:1-line. The plot shows test data, which was not used for training the model. (Right) Same as left but for La Liga._ 

We select players, where their true and predicted output for their league is differing by maximal 0.2 and input them into the Premier League model under the assumption that their league rank remains constant. We compare the true output and predicted output for the Premier League. The results are shown in Figure 23, showing their change indicated by the arrows from their true value to their predicted value. The players with the largest decrease in outputs are Julian Brandt (-2.88) and Noah Weißhaupt (-1.9), while the largest increase is observed for Daniel Raba Antolin (+4.39) 

**30** 



and Nico Williams (+2.75). The best performance would be seen by Vinicius Jr., which starts at a high output in La Liga (~14) but would gain +1.12 when being transferred to the Premier League. 



_Figure 23: Predicted change in absolute outcome for wingers when being transferred to the Premier League. Only players, which are well predicted in their own league model were selected._ 

The same can be done for transfers in the other directions (plots are shown in the appendix). The largest gains are observed for transfers to the Bundesliga for Bobby Armani De Cordova-Reid (+3.58) and Callum Hudson-Odoi (+2.92). The greatest increase for transfers to La Liga is seen for Omar Marmoush (+2.93) ad Cody Gakpo (+1.5). 

## **11. Conclusions** 

This study has successfully established that physical context significantly varies across Europe's top five football leagues, with the Premier League demonstrating the highest intensity metrics across multiple physical dimensions. Our analysis of over 1,800 player records from the 2024-25 season has revealed several critical insights that challenge traditional approaches to inter-league transfer evaluation. 

#### **Physical Context Differentiation** 

The research conclusively demonstrates that the Premier League operates at a fundamentally different physical intensity compared to other elite European leagues. The Physical Demand Index (PDI) analysis revealed substantial differences across all positions: 

**31** 



- **Strikers** : La Liga provides the closest physical transition to the Premier League, while Bundesliga, Serie A, and Ligue 1 require significant adaptation. 

- **Wingers** : The Premier League's physical context is substantially different from all other leagues, with Bundesliga showing the largest contrast. 

- **Central Midfielders** : Ligue 1 provides the smallest transition gap, though still substantial, while Bundesliga again shows the greatest divergence. 

- **Fullbacks** : Most leagues demonstrate reasonably similar physical contexts to the Premier League, except for Bundesliga which shows dramatic differences. 

- **Centre backs** : All players moving to the Premier League face substantial physical context changes, with minimal differences between origin leagues. 

#### **Athletic Ability as Performance Predictor** 

Our modeling approach has validated that athletic ability serves as a significant predictor of player performance, particularly for attacking positions. The boosted regression models achieved strong predictive power: 

- **Winger models** : Pearson correlations of 0.78 (Premier League), 0.668 (Bundesliga), and 0.562 (La Liga). 

- **Striker models** : Pearson correlation of 0.662 for the combined league model. 

The feature importance analysis confirmed that while team quality (league rank) remains the strongest predictor, physical attributes—particularly high acceleration percentage and ground duel win percentage—contribute substantially to performance prediction. 

#### **Position-Specific Athletic Dependencies** 

The research confirms that athletic ability importance varies significantly by position, aligning with established aging curve research. The age distribution analysis (weighted by minutes played) demonstrated: 

- **Wingers** : Show the youngest age profile, indicating highest athletic dependency. 

- **Centre backs** : Display the oldest age profile, suggesting lowest athletic dependency. 

- **Other positions** : Fall between these extremes with varying degrees of athletic reliance. 

#### **Transfer Prediction Capabilities** 

For wingers, our models enable practical transfer prediction without relying on historical inter-league transfer data or complex ELO calculations. The analysis of potential transfers revealed: 

- **Ligue 1 and Bundesliga** players show the highest risk of performance decline when moving to the Premier League. 

- **La Liga** players demonstrate the most favourable adaption profiles. 

- Individual player predictions achieved accuracy sufficient for preliminary transfer risk assessment. 

**32** 



## **12. Implications** 

#### **Challenge to Traditional Scouting Approaches** 

This research fundamentally challenges traditional scouting methodologies that rely heavily on statistical outputs without accounting for league-specific physical contexts. The finding that 50% of Bundesliga strikers have lower high acceleration percentages than any Premier League striker (except Joshua Zirkzee) illustrates the magnitude of these contextual differences. 

#### **Athletic Threshold Concept** 

The results support the existence of minimum athletic thresholds for effective performance in the Premier League that exceed requirements in other elite leagues. This threshold effect helps explain why some technically proficient players struggle after Premier League transfers despite strong statistical records in their origin leagues. 

#### **Performance Attribution Framework** 

Our findings establish a framework for decomposing player performance into athletic and technical components. Players who significantly outperform our athletic-based models (e.g., Lamine Yamal) demonstrate high technical skill levels that compensate for modest athletic attributes, while players who align closely with model predictions rely more heavily on physical capabilities. 

## **13. Applications** 

#### **Immediate Transfer Applications** 

Football clubs can implement this research for recruitment enhancement: 

- Use winger models to evaluate transfers from Bundesliga and La Liga with quantified performance projections for Premier League adaption: 

   - Input candidate physical metrics 

   - Adjust for expected team league rank (use last seasons to be safe) 

   - Generate projected Premier League performance with confidence intervals 

   - Compare projects against potential squad costs 

- Integrate PDI calculations into existing scouting reports to provide indicate risk of adaption: 

   - Calculate origin league PDI relative to destination league 

   - Flag high-risk transfers requiring additional due diligence 

   - Prioritise target from leagues and positions with favourable physical contexts 

**33** 



#### **Advanced Analytics Applications** 

Football clubs can use this research as a framework for better assessing their existing squad and player talent development: 

- Current performance evaluation – decomposing existing player performance into athletic and technical components to highlight level or inherent skill: 

   - Assess whether over-performance above athletic-based model predictions is consistent across multiple seasons. 

   - Assess whether outstanding talent or athletic ability is more important for future player development. 

   - Use assessment of existing performance compared to athletic ability to better inform training focus, position optimisation, and long-term career planning. 

- Squad planning – gaining insights from athletic demands of position for optimal squad composition: 

   - Prioritise athletic depth for high-intensity positions (wingers, fullbacks) and monitor the age profile of those positions more carefully. 

   - Identify positions where technical skills can compensate for modest athletic profiles. 

## **14.Limitations and Further Research** 

This study presents several limitations that offer opportunities for future investigation. The analysis relies on single-season data with modest sample sizes, particularly for strikers where populations ranged from 36-47 players per league, limiting statistical power and preventing reliable league-specific modeling for all positions. Future research should obtain data from multiple seasons and additional leagues beyond the top five to increase population sizes and represent a wider scouting pool, including Liga NOS and the Eredivisie. 

Key methodological extensions include identifying appropriate performance metrics for fullbacks, centre backs, and central midfielders that accurately capture their contributions, as these positions were excluded from current modeling due to output complexity. Additionally, research should explore whether performance above predicted models remain consistent across multiple seasons, distinguishing players with sustainable technical advantages from those experiencing temporary form. 

Further investigation is needed into deriving better proxies for team strength beyond final league rank, such as predicted points normalized across competitions. Critically, evaluating predictions against actual transfer results will validate model accuracy and enable refinement. Finally, filtering exportable outputs from context-dependent performance indicators and investigating larger sample sizes for player development trajectories after transfers will enhance practical applications for recruitment decision-making. 

**34** 



## **References** 

Caley, M. (2025, August 6). Building Marcel, Part II: Age curves. _Expecting_ 

_Goals_ . **<u>https://www.expectinggoals.com/p/building-marcel-part-ii-age-curves</u>** 

Carey, P. (2020, December 26). Can we better predict player performance between leagues? _Carey Analytics_ . **<u>https://careyanalytics.wordpress.com/2020/12/27/maximising-the-market-can-webetter-predict-player-performance-between-leagues/</u>** 

Chainok, P., Cavichiolli, F. R., Carvalho, H. M., Coutinho, D., Santos, S., & Gonçalves, B. (2025). How do the physical and physiological demands of training and official matches differ between recreational and semi-professional football players? _Frontiers in Sports and Active Living_ , _7_ , 1553694. **<u>https://doi.org/10.3389/fspor.2025.1553694</u>** 

de Haan, M., Doeven, S. H., Hoozemans, M. J. M., Pion, J., & Savelsbergh, G. J. P. (2025). Beyond playing positions: Categorizing soccer players based on match-specific running performance using machine learning. _Journal of Sports Science & Medicine_ , _24_ (4), 565-575. **<u>https://doi.org/10.52082/jssm.2025.565</u>** 

Ferraz, A., Valente-dos-Santos, J., Sarmento, H., Duarte, J. P., & Fernandes da Silva, A. (2023). Tracking devices and physical performance analysis in team sports: A comprehensive framework from technology to interpretation. _Frontiers in Sports and Active Living_ , _5_ , 1216408. **<u>https://doi.org/10.3389/fspor.2023.1216408</u>** 

Guan, T., & Swartz, T. B. (2024). Acceleration and age in soccer. _International Journal of Sports Science & Coaching_ , _19_ (5), 2112-2119. **<u>https://doi.org/10.1177/17479541241232504</u>** 

Jerome, B. W. C., Boyd, L. J., Hogarth, L. W., Haff, G. G., & Climstein, M. (2024). Contextualised physical metrics: The physical demands vary with phase of play during elite soccer match play. _Science and Medicine in Football_ , _8_ (4), 

325-338. **<u>https://doi.org/10.1080/24733938.2023.2293810</u>** 

Morgans, R., Rhodes, D., Di Michele, R., & Drust, B. (2024). The positional demands of explosive actions in elite soccer: Comparison of English Premier League and French Ligue 1. _International Journal of Sports Physiology and Performance_ , _19_ (10), 1087-1094. **<u>https://doi.org/10.1123/ispp.2024-0040</u>** 

Oterhals, G., Sæther, S. A., & Aggerholm, K. (2021). Age at nomination among soccer players nominated to The Ballon d'Or–Exploring the optimal age to perform at the elite level. _Frontiers in Psychology_ , _12_ , 661523. **<u>https://doi.org/10.3389/fpsyg.2021.661523</u>** 

**35** 



Säfvenberg, R., Swartz, T. B., & Laaksoharju, M. (2024). Age of peak performance among soccer players in Sweden. In _Proceedings of the First International Sports Analytics Conference and Exhibition_ (pp. 1-12). Linköping University. 

SkillCorner. (2020, August 22). Which is the most physically demanding league? _Training Ground Guru_ . **<u>https://archive.trainingground.guru/articles/which-is-the-most-physically-demanding-le ague</u>** 

Toivonen, R. M., Datson, N., Raeder, C., & Jakobi, J. (2025). The impact of varying small-sided games' pitch sizes on physical demands compared to official match play in recreational soccer. _Science and Medicine in Football_ , _9_ (3), 

245-256. **<u>https://doi.org/10.1080/24748668.2025.2490867</u>** 

**36** 



## **Appendix** 

#### **Positional Output Metric Comparisons** 





**37** 







**38** 







**39** 







**40** 







**41** 







**42** 







**43** 





#### **Predicted change in absolute outcome for wingers when being transferred to Bundesliga or LaLiga** 



**44** 





**45** 


