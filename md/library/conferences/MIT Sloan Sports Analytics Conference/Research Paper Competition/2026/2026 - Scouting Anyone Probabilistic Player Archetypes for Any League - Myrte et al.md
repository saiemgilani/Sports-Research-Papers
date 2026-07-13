<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2026/2026 - Scouting Anyone Probabilistic Player Archetypes for Any League - Myrte et al.pdf -->

# **Scouting Anyone: Probabilistic Player Archetypes for Any League** 

Paper Track: Basketball Paper ID: 57 

## **1. Introduction** 

Classifying player roles is a central challenge in basketball analytics. While the sport is often described in terms of traditional positions (guard, forward, center), modern basketball has evolved into a continuum of playing styles shaped by spacing, pace, and tactical diversity. Players increasingly occupy hybrid roles, and their responsibilities change across teams, coaches, and developmental stages. As a result, role classification requires models that capture nuance, flexibility, and evolution over time, rather than rigid or subjective labels. 

Elite organizations in leagues such as the NBA have adopted advanced scouting infrastructure and player-tracking technologies to support role identification and recruitment. However, most professional and semi-professional teams globally operate with limited budgets, limited staff, and minimal proprietary data. These teams often rely on qualitative scouting reports or simple statistical comparisons, which can be inconsistent across contexts and fail to identify players who could excel in new roles. 

Another problem is that existing clustering approaches in basketball analytics, such as k-means or hierarchical clustering, typically assign each player to a single group. This is problematic: a stretch big who posts up occasionally and plays pick-and-roll defense does not strictly belong to one role. Such methods also gravitate toward “average” player types, producing centroids that do not align with real basketball archetypes. They cluster around the middle, while basketball roles are more meaningfully described at the extremes. 

In this work, we apply Archetypal Analysis (AA) and Archetypoid Analysis (ADA) to classify player roles in a way that (a) reflects real extremes of playing style, (b) allows each player to belong probabilistically to multiple archetypes, and (c) can be built using data that is easily accessible. AA identifies extreme statistical profiles, or archetypes, while ADA ensures these archetypes correspond to actual players, improving interpretability for coaches and scouting staff. Each player-season-team profile is then modeled as a convex combination of archetypes, producing a role distribution rather than a single assignment. We showcase 2 examples, one using AA on European basketball data and the other using ADA on NBA data. 

Our results demonstrate that this approach consistently produces coherent, interpretable role archetypes across both European and NBA datasets. Moreover, the framework is scalable, it works with simple statistical data, yet improves further as richer datasets (such as play-type distributions or shooting location profiles) are added. The models can be effectively applied to any league or level of competition, provided they are trained on data from leagues of comparable quality. The methodology therefore provides a practical and cost-effective decision-support tool for teams across leagues and resource environments. 



1 

Beyond methodological contributions, the probabilistic archetype framework also generates direct, operational value for basketball organizations. By quantifying stylistic similarity and lineup context, the model supports several practical applications: diagnosing role mismatches within lineups or rotations, identifying stylistically comparable players for scouting across leagues, and informing balanced roster construction. These applications connect the analytical foundations of the method to real decision-making processes in coaching, recruitment, and front-office strategy. 

To demonstrate this in practice, the paper includes a detailed case study using 2024-25 EuroLeague data, where the framework is used to diagnose a structural mismatch involving a high-usage perimeter shooter and his surrounding lineup ecosystem. Additional examples illustrate how archetype analysis can guide roster design and support cross-league player identification. Together, these applications show how archetype-based modeling can serve as an accessible, interpretable, and actionable decision-support tool for teams across varied competitive and resource environments. 

## **2. Related Work & Background** 

Classifying basketball players into meaningful roles has long been of interest to both researchers and practitioners. Traditional methods in basketball analytics have relied heavily on manual scouting taxonomies, where players are labeled using position-based heuristics (e.g., guard, forward, center) or role descriptions crafted by coaching staff and scouts. As the modern game evolved toward pace-and-space offense and switching defenses, these positional labels became less adequate, motivating research into role-based rather than position-based classification. While these taxonomies are useful, they tend to be subjective, vary significantly across leagues and organizations, and struggle to capture the evolving and multi-dimensional nature of modern basketball. 

To formalize role identification, analysts have commonly used clustering techniques such as k-means, hierarchical clustering, and Gaussian Mixture Models (GMMs) to group players based on statistical similarity. These approaches have been applied to box score statistics, lineup impact metrics, and tracking data. However, each comes with limitations in representing how roles function in practice. K-means, for example, assigns each player to exactly one cluster, implying a single, fixed role, an assumption that rarely reflects reality. GMM-based approaches, including prior work such as the work from Kalman & Bosch (1), do allow for probabilistic or “soft” role memberships, but the resulting assignments typically remain highly peaked (e.g., a player is ~90% associated with one cluster and only marginally with others). This is problematic because player roles are inherently fluid: responsibilities shift depending on teammates, coaching schemes, lineup context, and league style. A player may be a secondary creator in one environment and primarily a floor spacer in another. Traditional clustering methods tend to compress these nuanced role overlaps into overly rigid labels. 

Archetypal Analysis (AA), introduced by Cutler and Breiman (1994) (2), offers a different approach. Instead of finding average or central clusters, AA identifies extreme points in the dataset, theoretical endpoints of playing styles, and represents each observation as a convex combination of these extremes. In basketball, this aligns with how coaches and analysts often describe players relative to prototypes (e.g., “a smaller Jokic-type facilitator,” “a more mobile rim protector”). This convex 



2 

combination property enables probabilistic role representation, acknowledging that players rarely fit neatly into single categories. 



_Figure 1: How Archetypal analysis approximates the convex hull of the dataset (3)_ 

Archetypal analysis has been applied extensively in psychology (personality profiles), sociology (group identity modeling), economics (consumer behavior segmentation), and environmental science (extreme climate pattern identification). In these areas, AA is valued because it reveals interpretable prototype behaviors while allowing individuals to exist between extremes. However, its use in sports analytics has been minimal. Basketball is a domain where stylistic blending is the norm, making AA particularly well-suited since roles are fluid, lineup constructions are flexible, and the same player may have different responsibilities across teams, leagues, or seasons. 

A related development is Archetypoid Analysis (ADA) (Vinué, Epifanio & Alemany 2015) (4), which constrains archetypes to be actual observed players instead of synthetic combinations. ADA enhances interpretability, particularly for practitioners who benefit from being able to say, for example, “Player X is stylistically 40% similar to Player Y and 35% to Player Z”, rather than referencing abstract archetype centroids. This distinction is crucial for scouting departments and front offices, where interpretability is often valued as highly as statistical accuracy. 

Recent work in basketball analytics has explored the use of tracking data, play-type frequencies, and spatial shot profiles to refine player style classification, particularly in the NBA where advanced data infrastructure is widely available. However, such data is not accessible to most international leagues. This creates a resource accessibility gap, where elite teams benefit from rich analytics, while the majority of professional teams must rely on limited box score statistics. The challenges associated with cross-league comparisons further complicate scouting markets and player movement. 



3 

The present research builds on this foundation by integrating AA and ADA into a unified, probabilistic framework for player role classification that works across leagues regardless of data richness. By structuring observations at the player-season-team level and drawing upon predictors that are consistently available worldwide, this methodology enables scalable, reproducible, and interpretable role profiles. Furthermore, by allowing players to hold probabilities across multiple archetypes, the approach captures stylistic fluidity and evolution over time, a central limitation of previous hard-clustering approaches. 

## **3. Data & Preprocessing** 

### **3.1 Observation Structure: Player–Season–Team Units** 

Because a player’s role can change depending on roster context, coaching philosophy, age, or league environment, our unit of analysis is a player–season–team combination, rather than a player in aggregate. For example, the same player may appear as a high-usage primary scorer in one season and as a spot-up complementary shooter in another. This structure allows the model to capture role evolution, making the archetypes reflect how players actually functioned in a given context, rather than how they are perceived in general. 

### **3.2 European Dataset (2014-15 season – 2024-25 season)** 

We compiled box-score and advanced game-level statistics from seven major European professional leagues using publicly available data from RealGM.com. These leagues included the Spanish (ACB), French (LNB), Italian (LBA), German (BBL), Turkish (BSL), Greek (GBL) and Adriatic League (ABA) as they represent the highest competitive tier within their respective countries and feature comparable levels of play. This ensures consistency in player role distributions and statistical comparability across contexts. We deliberately excluded pan-European competitions such as the EuroLeague, EuroCup, and FIBA Basketball Champions League from training the model, as their substantially higher level of competitiveness and talent concentration could bias the archetype formation process. After aggregating to season averages and normalizing per-possession where appropriate, the following features were included: 

#### **List of features included in the European Dataset** 

|**Category**|**Variables**|
|---|---|
|**Physical**|Height|
|**Rebounding**|Offensive Reb%, Defensive Reb%|
|**Playmaking**|Assist%, Turnover%|
|**Defensive**|Steal%, Block%|
|**Usage & Efficiency**|Usage%, Free Throw Rate, FT%, 2P%, 3P%|
|**Scoring Profile**|Points per 100 poss., FGA per 100 poss., Share of 3PA|



These features were selected to capture how players impact possessions (creation vs. finishing), where they operate on the floor, and how efficiently they convert opportunities. 

### **3.3 NBA Dataset (2017-18 season – 2024-25 season)** 



4 

For the NBA dataset, we extended the feature space to include shot distribution and play-type behavior, using data from NBA.com and Basketball-Reference.com. In addition to the features included in the European model, the following features were also included: 

**List of additional features included in the NBA Dataset** 

|**Category**|**Variables**|
|---|---|
|**Shot Distribution**|%FGA at 0-3 ft, 3-10 ft, 10-16 ft, 16 ft-3P, above-the-break 3s, corner 3s,<br>average shot distance|
|**Assisted vs**<br>**Unassisted Shots**|%AST-2P, %AST-3P|
|**Play Types**|% of possessions via pick-and-roll (handler/roller), isolation, handoffs,<br>post-ups, cuts, off-screen, putbacks, spot-ups|



These features provide insight into role execution, distinguishing, for instance, a pick-and-roll creator from a movement shooter or interior finisher. 

### **3.4 Normalization and Scaling** 

Because the variables in our dataset span different numerical scales (e.g., percentages, counts, centimeters), we apply z-score normalization prior to modeling. This step ensures that no single feature disproportionately influences the analysis solely due to its magnitude. Standardizing places all variables on a comparable scale, allowing the archetypes to meaningfully reflect underlying playing styles rather than measurement differences. 

### **3.5 Filtering for Stability** 

We apply a minimum playing-time threshold of 300 minutes played per player-season-team in both the European and NBA datasets to ensure statistical stability. This reduces noise and prevents role patterns from being driven by players with very limited sample sizes, where performance tends to exhibit high variance. By filtering out short-minute or injury-shortened seasons, we ensure that the archetype representations reflect sustained playing tendencies rather than small-sample fluctuations. 

## **4. Methodology** 

The objective of this study is to identify interpretable, probabilistic player role profiles derived directly from observed performance data. To achieve this, we applied Archetypal Analysis (AA) and Archetypoid Analysis (ADA) to our standardized player–season–team datasets. Both approaches model players not as members of a single cluster, but as convex combinations of stylistic extremes, enabling more realistic representation of hybrid and evolving playing styles. 

### **4.1 Archetypal Analysis (AA)** 

Archetypal Analysis seeks to represent each observation 𝑥 in the dataset as a weighted mixture of a 𝑖 small set of archetypes Ζ = 𝑧 , 𝑧 , …, 𝑧 , where each archetype itself is a convex combination of { 1 2 𝐾} 



5 

data points. Formally, AA starts with a dataset _X_ of _n_ observations (players) and _m_ variables (performance metrics). The method searches for _k_ archetypes, represented by the matrix _Z_ , that best approximate all data points. Each archetype is a convex combination of real players, and each player is in turn a convex combination of these archetypes. Mathematically: 



subject to: 



where: 

- α represents the mixing weights (how much player  belongs to archetype )𝑖 𝑗 𝑖𝑗 

- β the coefficients used to define each archetype as a combination of actual data points 𝑗𝑖 

- The constraints ensure that all players and archetypes are weighted averages (no negative weights, total weight = 1). 

The archetypes represent extreme, interpretable stylistic endpoints rather than centroids. Player memberships α form probabilities (e.g., 0.60 3P Specialist, 0.25 Playmaker, 0.15 Defensive Wing) 𝑖𝑗 

and every player can express a blend of roles, reflecting real-world basketball dynamics. This differs fundamentally from clustering methods like k-means, where players are forced into a single category, even when their style is hybrid. 

### **4.2 Archetypoid Analysis (ADA)** 

Archetypoid Analysis modifies AA by constraining archetypes to be actual players rather than theoretical convex combinations. This enhances interpretability and practical usefulness. Mathematically, we still have the same minimizing function: 



but the constraints are slightly different: 



The key difference from AA lies in the binary constraint on : β 

- Each archetypoid ΖΚ is a _single actual data point_ (a real player), because β𝑗𝑖 = 1 only for one observation , and 0 otherwise𝑖 

- Each player  is still a convex combination of these archetypoids via Χ α 𝑖 𝑖𝑗 

ADA is particularly effective for scouting and communication, as archetypes can be described with statements such as “This player is 40 % stylistically similar to Player Y and 35% to Player Z.” 



6 

### **4.3 Determining the Number of Archetypes (K)** 

Using the standard elbow method on reconstruction error (RSS) provided an initial guideline for selecting the number of archetypes. However, in both datasets the elbow appeared very early, around four archetypes, which is clearly insufficient to capture the diversity of modern basketball roles. While four archetypes minimize RSS efficiently, they collapse multiple distinct functional player types into overly broad categories (e.g., combining creators, shooters, and hybrid forwards), limiting interpretability and practical value. 



_Figure 2: Scree Plot, European Dataset, Archetypal Analysis (AA)_ 

To address this, we introduced an additional diagnostic: intra-archetype variance. Instead of focusing on global reconstruction error, this metric evaluates how similar the players assigned to each archetype are to one another. Lower intra-archetype variance indicates that archetypes capture more coherent, internally consistent roles. By examining how this variance changes as the number of archetypes increases, we can detect when additional archetypes meaningfully refine role structure, and when they simply overfit noise. 

Applying intra-archetype variance analysis to the European dataset and the AA methodology revealed a clear optimum at 8 archetypes. Variance steadily decreased as we increased the number of archetypes from 4 to 8, reflecting that each additional archetype helped isolate more precise on-court behaviors. Importantly, after k = 8, variance increased considerably, and further archetypes mostly subdivided already coherent roles rather than uncovering new, meaningful distinctions. In other words, eight archetypes represented the point where the model captured the essential diversity of player types without fragmenting them into unnecessarily fine-grained categories. This aligns with qualitative evaluation: each of the eight roles corresponded to recognizable, interpretable basketball archetypes with minimal redundancy. 



7 



_Figure 3: Intra-archetype Variance per number of Archetypes, European Dataset, Archetypal Analysis (AA)_ 

For the NBA dataset and the ADA methodology, intra-archetypoid variance followed a similar pattern, reaching its minimum at 9 archetypoids. However, the improvement from 8 to 9 archetypoids was marginal, the reduction in variance was noticeably smaller than in earlier steps, decreasing from 0.538 to 0.525, and the ninth archetypoid often appeared as a subtle variation of an existing one rather than a distinct, stable role thus leading us to adhere to 8 archetypoids. We refrained from testing much larger numbers of archetypes or archetypoids, as both basketball domain knowledge and prior literature suggest that the ecosystem of meaningful player roles is not dramatically larger. Pushing the model further would produce increasingly niche, fragmented groups with limited interpretability. 



_Figure 4: Intra-archetypoid Variance per number of Archetypoids, NBA Dataset, Archetypoid Analysis (ADA)_ 



8 

## **5. Results** 

### **5.1 European Archetypes (AA Model)** 

Since the labels of the 8 clusters do not correspond to predefined roles, we carried out a detailed exploratory analysis to interpret the player types represented by each group. This included reviewing descriptive statistics, examining mean z-scores for players most strongly associated with each archetype, and using boxplots to identify which variables separated one group from another. The table below highlights the eight archetypes derived from the European dataset, summarizing their characteristics and the features that most clearly distinguish them. 

|**Archetype**|**Explanation**|**Distinguishing Features**|**Top Players**|
|---|---|---|---|
|**High Usage**<br>**Guard**|Primary creator<br>and scorer|High Usage%, High Points per 100,<br>High AST%|N. Hilliard (GER 2020-21)<br>D. Russell (GER 2022-23)<br>M. Huertas (ESP 2021-22)|
|**3PT**<br>**Specialist**|Off-ball shooter<br>with limited<br>on-ball creation|High 3FGA%, High 3P%, Low Free<br>Throw Rate|M. Mahmutoglu (TUR<br>2022-23)<br>B. Heslip (TUR 2018-19)<br>A. Corbacho (ESP<br>2018-19)|
|**Traditional**<br>**Center**|Interior finisher<br>+ rim<br>protection|Taller, High Reb%, High BLK%, High<br>FTr, Low 3PA%|E. Arar (TUR 2023-24)<br>S. Spencer (ITA 2023-24)<br>D. Naymick (GRC 2014-15)|
|**Backup Big**|Low-usage<br>interior role<br>player|Similar to Traditional Center but<br>with lower efficiency and usage|O. Mackeldanz (DEU<br>2018-19)<br>S. Erden (TUR 2019-20)<br>M. Lessort (Adriatic<br>2022-23)|
|**Defensive**<br>**Specialist**|Disruptive<br>defender with<br>low offensive<br>burden|High STL% and/or BLK%, Low<br>Usage%|B. Cerella (ITA 2017-18)<br>K. Tadda (DEU 2014-15)<br>K. Tadda (DEU 2020-21)|
|**High Usage**<br>**Forward**|Multi-level<br>scoring forward|Taller than the average, High<br>Usage%, High Points per 100, High<br>FGA per 100, Low 3FGA%|F. Petrusev (Adriatic<br>2020-21)<br>J. Tillman (GRC 2023-24)<br>B. Dubljevic (ESP 2015-16)|
||||D. Karamfilov (Adriatic|
|**Traditional**<br>**Playmaker**|Pass-first<br>facilitator|Shorter, High AST%, High TOV%,<br>Low scoring production|2014-15)<br>A. Kerckhof (FRA 2017-18)<br>L. Dercole (ITA 2016-17)|





9 

D. Ozdemiroglu (TUR 2019-20) Complementary Shorter, Average in most areas, **Role Guard** O. Williams (DEU backcourt piece slightly elevated usage 2022-23) J. Morgan (FRA 2023-24) 

_Leagues References: GER: German BBL; TUR: Turkish BSL; ESP: Spanish ACB; ITA: Italian Serie A; Adriatic: Adriatic League; FRA: French LNB Elite_ 

The figure below illustrates the average z-scores across all variables for two example archetypes, Traditional Centers and Traditional Playmakers. 



_Figure 5: Traditional Center vs Traditional Playmaker Normalized performance - Average Z-scores per variable_ 



10 

Below we have the results for Dylan Osetkowski from the 2023-24 season with Unicaja Malaga as an example. 



_Figure 6: Dylan Osetkowski’s Archetype Analysis results - 2023-24 Liga Endesa season, Unicaja Malaga_ 

As discussed above, instead of assigning a single label, each player-season receives a vector of membership weights. For instance, Dylan Osetkowski’s playing style in 2023-24 can be described as: 

- 57.0% High Usage Forward 

- 23.2% Role Guard 

- 15.2% 3PT Specialist and 

- 4.5% Defensive Specialist 

### **5.2 NBA Archetypes (ADA Model)** 

Similarly, for our Archetypoid Analysis model, trained on NBA data with an enriched dataset, we performed the same EDA and we identified the following 8 archetypoids: 



11 

|**Archetypoid**|**Explanation**|**Distinguishing Features**|**Top Players**|
|---|---|---|---|
|**Inside Scoring**<br>**Big**|Interior<br>finisher and<br>offensive<br>rebounder|Tallest, Highest %Post-Up, High<br>%Roll Man and Putback, High USG%<br>and scoring production|N. Vucevic (2020-21)<br>L. Aldridge (2017-18)<br>N. Vucevic (2020-21)|
|**Shooting**<br>**Specialist**|Movement or<br>spot-up<br>shooter|High Off-Screen & Spot-up, Low<br>self-creation, Low 2FGA%|T. Daniels (2017-18)<br>W. Ellington (2019-20)<br>W. Ellington (2017-18)|
|**Combo Guard**|Scoring guard<br>with creation<br>ability|Shorter, High PnR Handler% &<br>Isolation%, moderate AST%|T. Burke (2021-22)<br>J. Crawford (2017-18)<br>T. Burke (2018-19)|
|**Offensive**<br>**Engine**|Primary<br>initiator and<br>focal scorer|Very high Usage%, High scoring<br>production, Low % of assisted shots,<br>isolation % PnR-heavy|J. Harden (2018-19)<br>L. Doncic (2022-23)<br>J. Harden (2019-20)|
|**Traditional**<br>**Playmaker**|Pass-first<br>facilitator|High AST%, Higher TOV%, Low shot<br>volume, High PnR Handler%|E. Payton (2024-25)<br>I. Smith (2023-24)<br>R. Rondo (2020-21)|
|**3&D Wing**|Perimeter<br>defender &<br>floor spacer|Average Size, High 3PA%, Moderate,<br>STL% and BLK%, Minimal creation<br>or Rim presence|D. Wade (2024-25)<br>D. Wade (2022-23)<br>K. Edwards (2022-23)|
|**Rim Protector /**<br>**Roll Man**|Interior<br>defender +<br>PnR finisher|Elite BLK% & OREB%, High Roll<br>Man and Putback frequency|M. Robinson (2022-23)<br>M. Robinson (2021-22)<br>M. Robinson (2023-24)|
|**Mobile Big**|Stretch-capabl<br>e or<br>perimeter-mob<br>ile big|Slightly Shorter and other Bigs, High<br>Corner 3FGA%, High % of Assisted<br>FGA, High% on Cuts|J. Poeltl (2017-18)<br>O. Okongwu (2022-23)<br>J. Allen (2017-18)|



Below we have the results for Giannis Antetokounmpo from the 2024-25 season with the Milwaukee Bucks. 



12 



_Figure 7: Giannis Antetokounmpo’s Archetypoid Analysis Results - 2024-25 NBA Regular Season, Milwaukee Bucks_ 

Giannis Antetokounmpo’s playing style in 2024-25 can be described as: 

- 53.5% similar to 2019 James Harden and 2023 Luka Doncic (Offensive Engine) 

- 22.6% similar to 2022, 2023 Mitchel Robinson and 2022 DeAndre Jordan (Rim Protector/Roll Man) 

- 17.1% similar to 2021 Nikola Vucevic (Inside Scoring Big) and 

- 6.8% similar to 2018 Jakob Poeltl and Jarrett Allen and 2023 Onyeka Okongwu (Mobile Big) 

## **6. Application for Teams** 

The probabilistic archetype framework developed in this research enables several practical applications that address real operational challenges faced by basketball organizations. In this section, we demonstrate three key use cases: 

1. Diagnostic analysis: Identifying player combination mismatches in existing rosters 

2. League-wide or cross-league scouting: Finding stylistically similar players within the league/competition or across different leagues/competitions 



13 

3. Roster construction: Balancing archetype distributions for tactical coherence Each application leverages the core methodological advantages established in Section 4: probabilistic role representation, interpretability through real player archetypes (ADA) or extremal profiles (AA), and scalability across data richness levels. 

We present a detailed case study of the first application (player combination mismatch detection) using 2024-25 EuroLeague data to demonstrate how archetype analysis can diagnose performance issues and guide tactical adjustments. This is followed by brief illustrations of roster construction applications. 

### **6.1 Case Study: Diagnosing Player Combination Mismatch in High-Usage Lineups** 

### **6.1.1 Context and Methodology** 

For this application, we retrained our Archetypal Analysis model on EuroLeague-specific data from the 2024-25 season (N=249 player-season observations, minimum 300 minutes played through Regular Season). While our European dataset (Section 3.2) was trained on domestic leagues, EuroLeague represents a higher competitive tier featuring many of the same players and tactical systems. The resulting eight archetypes closely mirror those identified in the NBA (Section 5.2) 

**EuroLeague Archetype Definitions** : The retrained model identified the following eight archetypes, which we use throughout this case study: 

|**Archetype**<br>**Name**|**Explanation**|**Distinguishing Features**|
|---|---|---|
|**Shooter**<br>**Specialist**|Elite perimeter shooter,<br>off-ball oriented|High 3FGA%, high spot-up frequency, minimal<br>self-creation|
|**3&D Wing**|Two-way perimeter<br>player|Moderate 3PA%, high STL%, low creation rate,<br>defensive versatility|
|**Lead Guard**|Pass-first facilitator|Very high AST%, high TOV%, low scoring volume,<br>high pick-and-roll handler usage|
|**Mid-Range**<br>**Specialist**|Interior slasher with<br>midrange game|High 2P% from 10-16ft, low 3PA%, moderate<br>USG%, pull-up oriented|
|**Traditional**<br>**Center**|Interior finisher and rim<br>protector|Tallest, high BLK%, high OREB%, low 3PA%,<br>post-up and putback frequency|
|**High Volume**<br>**Scorer**|Multi-level scoring threat|High USG%, high points per 100, balanced shooting<br>from multiple areas|
|**Stretch 4**|Stretch big with<br>perimeter shooting|High corner 3PA%, high pick-and-pop frequency,<br>moderate height, floor spacing|
|**Rolling Big**|Vertical spacer and<br>dunker|High roll-man%, high putback%, high FG% at rim,<br>lob threat, minimal perimeter shooting|





14 

### **6.1.2 Player Profile: Markus Howard's Extreme Archetype Concentration** 

Baskonia is a high-caliber basketball team in Spain which competes in the Spanish National League (Liga ACB) as well as in the EuroLeague. Baskonia features a high-usage perimeter scorer whose stylistic identity is exceptionally well-defined. Markus Howard, a former NCAA scoring leader at Marquette (leading scorer with 27.8 PPG in 2019-20) and former Denver Nuggets guard, was classified by our EuroLeague model as 72% Shooter Specialist, one of the highest single-archetype concentrations observed in the league. 



<!-- Start of picture text -->
classified by our EuroLeague model as 72% Shooter Specialist, one of the highest single-archetype<br>concentrations observed in the league.<br><!-- End of picture text -->

_Figure 8: Shooter Specialist Archetype Probability Distribution in 2024-25 EuroLeague_ 

Statistically, Howard embodies the modern high-volume shooter profile: 

- 12.1 points per game (89th percentile among 2024-25 EuroLeague players with ≥ 100 minutes) 

- 7.4 three-point attempts per game (99th percentile) 

- 2.5 made threes per game (97th percentile) 

- 33.9% from three (44th percentile overall; 26th-30th percentile among high-volume shooters with ≥ 3 3PA/game) 

This combination of extreme volume with league-average efficiency is characteristic of shooters whose primary value derives from gravity (defensive attention commanded) rather than raw shooting percentages. Players with such extreme perimeter profiles typically require specific structural environments to maximize efficiency: secondary ball-handlers capable of generating advantages, stretch forwards or mobile bigs who preserve spacing, and wings who provide both shooting and defensive coverage. 

When these complementary roles are absent or misaligned, teams often struggle to convert the shooter's gravity into collective efficiency, leading to diminished offensive performance and negative lineup outcomes. 

### **6.1.3 Problem Identification: Performance Split Signals Structural Issue** 



15 

Despite Howard's individual offensive contributions, Baskonia's team performance exhibits a stark contrast based on his court presence: 

- **Net Rating**<sup>1</sup> **with Howard on court** : –7.0 

- **Net Rating with Howard off court** : +3.0 

This represents a 10-point swing per 100 possessions, a substantial margin at the EuroLeague level. Importantly, this does not suggest Howard is a negative-impact player in isolation. Rather, it indicates a deeper structural issue: the lineups surrounding him are not aligned with the requirements of his archetype. 

### **6.1.4 Ecosystem Analysis: Who Plays Alongside Howard?** 

To understand why Baskonia underperforms with Howard on the floor, we examine the archetype distribution of his most frequent teammates at two levels: macro (archetype exposure patterns) and micro (individual player profiles). 

### **6.1.4.1 Macro View: Archetype Distribution in Howard's Minutes** 

We calculated the percentage of Howard's total court time (715 minutes in 2024-25 EuroLeague Regular Season) shared with each of the eight EuroLeague archetypes. The distribution reveals a clear structural imbalance: 

**High-Exposure Archetypes** (collectively 57.3% of shared time): 

- **Traditional Center** : 25.8% of Howard's minutes 

- **Mid-Range Specialist** : 16.9% 

- **High Volume Scorer** : 14.6% 

**Low-Exposure Archetypes** (collectively 21.7% of shared time): 

- **3&D Wing** : 9.5% 

- **Stretch 4** : 7.2% 

- **Rolling Big** : 3.0% 

> 1 Net Rating is calculated as the difference between Points scored per 100 possessions minus Points conceded per 100 possessions. 



16 



_Figure 9: Markus Howard’s Archetype Exposure Patterns Across 2024-25 EuroLeague Season_ This pattern is problematic for a 72% Shooter Specialist. More than half of Howard's shared playing time comes with archetypes that compress offensive spacing (Traditional Centers operate almost exclusively in the paint, Mid-Range Specialists pull defenders inside the arc) or provide limited perimeter gravity (Lead Guards with minimal shooting threat). In contrast, the archetypes that typically amplify high-volume shooters, 3&D wings, stretch bigs, and fellow shooters, represent less than 30% of his ecosystem. 

This macro-level view suggests Howard consistently operates in lineups that do not match the structural requirements of his role, placing him in environments with multiple non-shooters that diminish the value of his gravity and increase defensive pressure on his actions. 

### **6.1.4.2 Micro View: Howard's Three Primary Teammates** 

Across the season, Howard played 91.5% of his on-court minutes with at least one of the three teammates profiled below. 

#### **Chima Moneke (470 shared minutes, 65% of Howard's time):** 

- 43.4% Mid-Range Specialist 

- 25.7% High Volume Scorer 

#### **Donta Hall (443 shared minutes, 62% of Howard's time):** 

- 82.4% Traditional Center 

- 10.0% Stretch 4 

#### **Trent Forrest (403 shared minutes, 56% of Howard's time)** 

- 45.7% Lead Guard 

- 27.0% High Volume Scorer 



17 



_Figure 10: Role Composition of Howard’s Most Frequent On-Court Teammates in the EuroLeague (2024-25)_ 

While each player can be individually productive, their stylistic overlap creates the least compatible offensive environment for a high-volume Shooter Specialist. This archetype-level analysis reveals why traditional scouting, which might label Forrest as a "Point Guard" and Hall as a "Center", fails to capture the nuanced spacing incompatibility that affects lineup performance. 

### **6.1.5 Lineup Performance: Quantifying the Mismatch** 

Using possession-adjusted net ratings across all 2024-25 EuroLeague Regular Season games, we analyzed Howard's most common lineup combinations with his three highest-minute teammates: Forrest, Hall, and Moneke. The results reveal a striking pattern: every major pairing yields a negative net rating. 

#### **Two Players Combinations** 

|**Combination**|**Minutes**|**% Minutes**<br>**w/ Howard**|**ORtg**|**DRtg**|**NRtg**|
|---|---|---|---|---|---|
|Howard + Moneke|470.0|65.8%|110.3|124.7|**-14.4**|
|Howard + Hall|443.0|62.0%|111.3|123.1|**-11.8**|
|Howard + Forrest|403.0|56.4%|115.9|124.3|**-8.4**|



#### **Three Players Combinations** 

|**Combination**|**Minutes**|**% Minutes**<br>**w/ Howard**|**ORtg**|**DRtg**|**NRtg**|
|---|---|---|---|---|---|
|Howard + Hall + Moneke|304.4|42.6%|105.9|125.0|**-19.1**|





18 

|Howard + Forrest +<br>Moneke|290.8|40.7%|109.6|124.9|**-15.3**|
|---|---|---|---|---|---|
|Howard + Forrest + Hall|257.3|36.0%|114.6|120.5|**-5.9**|



This concentration indicates a highly stable rotation pattern, with nearly half of all team minutes (48%) involving at least one member of the Howard-Forrest-Hall-Moneke cohort. 

The consistency across all configurations, regardless of which specific players are combined, suggests the issue transcends individual matchups. The archetype model provides the explanation: when Howard (72% Shooter Specialist) is surrounded by Forrest (45.7% Lead Guard, minimal shooting), Moneke (43.4% Mid-Range Specialist, interior-focused), and Hall (82.4% Traditional Center, paint-bound), the collective effect compresses spacing, reduces catch-and-shoot opportunities, and forces Howard into self-creation, outside his optimal role. These lineups systematically neutralize his primary value (gravity from volume shooting) without providing the structural support to convert that gravity into efficient offense. 

### **6.1.6 League-Wide Comparison: Optimal Ecosystems for Shooter Specialists** 

To identify how Baskonia should construct lineups around Howard, we perform a league-wide analysis of players with similar archetypes and evaluate which environmental factors correlate with positive on-court performance. 

### **6.1.6.1 Identifying High-Impact Comparables** 

We begin with the Top-20 guards and wings classified as Shooter Specialists (ranked by archetype probability ≥ 55%) who played ≥ 300 minutes in the 2024-25 EuroLeague Regular Season. We then filter this group to identify players who drive positive team impact, defined as meeting one or both criteria: 

- Positive Net Rating when on court 

- Higher team Net Rating on-court than off-court (positive on/off differential) 

Among the top 20 Shooter Specialists, only eight players meet these performance criteria: 

|**Player**|**Team**|**Shooter**<br>**Specialist**|**Minutes**|**NRtg On**|**NRtg Off**|**NRtg**<br>**Delta**|
|---|---|---|---|---|---|---|
|Sebastian<br>Herrera|Paris|64.6%|154|**+21.8**|**-2.4**|**+24.2**|
|Rodrigue<br>Beaubois|Anadolu Efes|62.9%|623|**+6.4**|**+7.9**|**-1.5**|
|Alex Abrines|Barcelona|55.0%|563|**+9.9**|**+1.9**|**+8.0**|
|Tarik Biberovic|Fenerbahce|53.0%|718|**+8.5**|**-3.3**|**+11.8**|
|Nikos<br>Rogkavopoulos|<sup>Baskonia</sup>|52.2%|618|**+6.8**|**-9.5**|**+16.4**|
|Vanja<br>Marinkovic|Partizan|51.1%|481|**+6.7**|**-1.0**|**+7.7**|





19 

|Isaiah Canaan|Crvena<br>Zvezda|50.6%|711|**+3.2**|**+1.2**|**+2.0**|
|---|---|---|---|---|---|---|
|Errick<br>McCollum|Fenerbahce|45.4%|238|**+3.5**|**+2.7**|**+0.8**|



These eight players represent the benchmark for successful Shooter Specialist deployment in EuroLeague competition. Notably, Howard (72% Shooter Specialist, –7.0 on-court NRtg, –10.0 on/off differential) exhibits higher archetype concentration than any player in this successful cohort, yet dramatically underperforms them in team impact metrics. 

### **6.1.6.2 Measuring Ecosystem Patterns** 

For each of the eight high-impact Shooter Specialists, we calculated the percentage of minutes shared with each archetype, weighted by shared court time. We then computed the unweighted mean across the cohort to produce a league baseline representing optimal Shooter Specialist environments. 

The table below compares Howard's archetype exposure (playing time) against this baseline: 

|**Archetype**|**League**<br>**Baseline**|**Howard**<br>**Actual**|**Difference**<br>**(pp)**|**Interpretation**|
|---|---|---|---|---|
|Traditional<br>Center|12.9%|25.8%|**+12.9↑**|Howard plays far more minutes with<br>interior-oriented bigs, reducing spacing|
|Mid-Range<br>Specialist|14.7%|16.9%|**+2.2↑**|Slight overexposure to non-shooting<br>scorers|
|High Volume<br>Scorer|16.9%|14.6%|**-2.3↓**|Mild underexposure to secondary<br>creators|
|Lead Guard|12.0%|13.3%|**+1.3↑**|Slightly increased exposure to<br>non-shooting facilitators|
|Shooter<br>Specialist|13.4%|9.8%|**-3.7↓**|Underexposure to spot-up shooters and<br>spacing threats|
|3&D Wing|13.7%|9.5%|**-4.1↓**|Notable shortage of two-way perimeter<br>defenders/spacers|
|Stretch 4|11.1%|7.2%|**-3.9↓**|Lack of stretch bigs limits pick-and-pop<br>spacing|
|Rolling Big|5.4%|3.0%|**-2.4↓**|Underuse of vertical threats, reducing<br>rim-pressure synergy|



#### **Key Findings** : 

#### **1. Howard plays far more with spacing-negative archetypes:** 

● +12.9pp exposure to Traditional Centers (Hall's 82.4% archetype) 



20 

- +2.2pp exposure to Mid-Range Specialists (Moneke's 43.4% archetype) 

These archetypes compress offensive spacing, place additional defenders near the basket, and reduce the effectiveness of Howard's perimeter gravity. 

#### **2. Howard plays far less with spacing-positive archetypes:** 

- -4.1pp less exposure to 3&D Wings (should be 13.7% of minutes, currently only 9.8%) 

- -3.9pp less exposure to Stretch 4s (should be 11.1%, currently only 7.2%) 

- -3.7pp less exposure to fellow Shooter Specialists (should be 13.4%, currently only 9.8%) 



21 

### **6.1.6.3 Validating Predictions with Howard's Actual Teammates** 

To confirm that the model's predictions translate into real outcomes, we tested three archetype pairings using Howard's existing roster and their actual on/off performance data: 

|**Pairing**|**Primary**<br>**Archetype**|**Howard +**<br>**Player**<br>**NRtg**|**Howard**<br>**+ Player**<br>**Minutes**|**Only**<br>**Howard**<br>**NRtg**|**Only**<br>**Player**<br>**NRtg**|**Interpretation**|
|---|---|---|---|---|---|---|
|Donta Hall|82.4%<br>Traditional<br>Center|**-11.8**|443|**+0.7**|**+6.1**|Negative interaction:<br>both perform better<br>apart, validating<br>spacing compression<br>prediction|
|Chima Moneke|43.4%<br>Mid-Range<br>Specialist|**-14.4**|470|**+7.2**|**+7.2**|Strong negative fit<br>despite positive solo<br>performance for both|
|Nikos<br>Rogkavopoulos|52.2%<br>Shooter<br>Specialist|0.0|283|**-11.6**|**+12.3**|Howard improves<br>+11.6 pts/100 with<br>fellow shooter; best<br>available partnership<br>on roster|
|Sander Raieste|<sup>52.0% 3&D</sup><br>Wing|**+22.5**|19|**-7.8**|**-25.6**|+30.3 pt swing<br>suggests strong<br>synergy; limited<br>sample requires<br>validation over<br>150-200 minutes|



**Key Findings** : The analysis confirms the model’s expectations: Howard’s performance declines sharply with Traditional Centers and Mid-Range Specialists, even though each player performs well independently. In contrast, lineups featuring shooting- and spacing-positive archetypes show strong improvements, with Shooter Specialists stabilizing Howard’s impact and 3&D Wings generating the highest projected gains. The Raieste-Howard pairing, currently with only 19 minutes, should be expanded to validate the predicted synergy. 

### **6.1.7 Roster Construction Gaps and Recruitment Priorities** 

Comparing Howard's archetype exposure patterns with the league baseline for successful Shooter Specialists reveals two critical roster deficiencies that limit Baskonia's ability to optimize their primary perimeter scorer. 

#### **Gap 1: No Rotation-Level Stretch 4** 

- **League average exposure** : 11.1% of Shooter Specialist minutes 



22 

- **Baskonia current exposure** : 7.2% 

- **Deficit** : -3.9pp below optimal 

Howard's successful peers (Beaubois, Abrines, Herrera, etc.) rely heavily on stretch bigs who can space the floor from the dunker spot, pop to the perimeter after screening, or provide corner three-point gravity. These players create vertical spacing that prevents defenders from collapsing on perimeter actions. 

Baskonia's only player classified in this archetype is Ousmane Ndiaye (53% Stretch 4), who has played only 12 games with 115 total minutes in the 2024-25 season, insufficient for rotation-level impact. The lack of a consistent Stretch 4 forces Howard into lineups dominated by Traditional Centers (Hall: 82.4%) who compress spacing. 

**Recruitment Priority** : This represents the highest-priority addition for optimizing Howard's ecosystem. Target profile: 

- ≥ 50% Pick-and-Pop Big archetype concentration 

- Roll-man capability for pick-and-roll versatility 

- Defensive mobility to switch on perimeter actions 

#### **Gap 2: Limited 3&D Wing Depth** 

- **League average exposure** : 13.7% of Shooter Specialist minutes 

- **Baskonia current exposure** : 9.5% 

- **Deficit** : -4.2pp below optimal 

Successful Shooter Specialists spend approximately one-seventh of their court time alongside true 3&D wings who provide both perimeter shooting and defensive coverage. This archetype is critical because it: 

1. Maintains spacing without defensive liabilities 

2. Allows defensive switching schemes that protect the Shooter Specialist 

3. Provides secondary ball-handling without compressing perimeter space 

Baskonia's roster includes only Sander Raieste (52.0% 3&D Wing) who fits this profile, yet he plays sparingly (19 shared minutes with Howard, 2% of total) despite strong on/off data (+22.5 NRtg together). 

#### **Recruitment Priority** : 

- Increase Raieste's role and minutes (internal solution) 

- Target external addition with clear 3&D profile: 

   - ≥ 40% 3&D Wing archetype concentration 

   - ≥ 35% three-point percentage on moderate volume 

   - Positive defensive metrics (STL%, on-ball defense rating) 

## **7. Conclusion** 

This research demonstrates that Archetypal Analysis and Archetypoid Analysis provide a scalable, interpretable, and probabilistic framework for describing basketball player roles. Unlike traditional clustering models, which force players into single categories, this approach captures role blending and role evolution, reflecting how modern basketball is actually played. 



23 

By requiring only minimal data, the method is accessible to teams across the global basketball ecosystem, from elite organizations to resource-limited clubs. 

At the same time, incorporating more advanced contextual features (such as shot distribution and play-type involvement) further enhances precision, demonstrating the scalability and extensibility of the framework. 

The practical applications demonstrated in this work underscore the usefulness of archetype modeling for real basketball decision-making. The framework helps teams identify undervalued or context-dependent players across leagues, diagnose stylistic redundancies or mismatches within lineups, and guide roster construction toward more coherent tactical structures. Because the model is both reproducible and interpretable, particularly through ADA’s use of real player examples, it integrates naturally into coaching, scouting, and front-office workflows. 

In a sport defined by fluidity rather than fixed positions, this methodology provides a modern, practical, and reproducible tool for understanding how players actually play. 



24 

## **References** 

[1] “NBA Lineup Analysis on Clustered Player Tendencies: A new approach to the positions of basketball & modeling lineup efficiency of soft lineup aggregates”, S. Kalman, J. Bosch, MIT Sloan Sports Analytics Conference, 2020 

[2] Cutler, Adele, and Leo Breiman. “Archetypal Analysis.” _Technometrics_ , vol. 36, no. 4, 1994, pp. 338–47. _JSTOR_ , https://doi.org/10.2307/1269949. Accessed 15 Nov. 2025. 

[3] Canhasi, Ercan & Kononenko, Igor. (2015). Weighted Hierarchical Archetypal Analysis for Multi-document summarization. Computer Speech & Language. 37. 10.1016/j.csl.2015.11.004. 

[4] G. Vinué, I. Epifanio. Archetypoid analysis for sports analytics. Data Mining and Knowledge Discovery, 31 (6), 1643-1677, 2017. 



25 


