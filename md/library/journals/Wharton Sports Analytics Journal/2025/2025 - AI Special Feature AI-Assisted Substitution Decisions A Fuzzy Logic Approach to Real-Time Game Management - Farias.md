<!-- source: library/journals/Wharton Sports Analytics Journal/2025/2025 - AI Special Feature AI-Assisted Substitution Decisions A Fuzzy Logic Approach to Real-Time Game Management - Farias.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/ai-special-feature-ai-assisted-substitution-decisions-a-fuzzy-logic-approach-to-real-time-game-management/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2025 -->
<!-- authors: Pedro Passos Farias -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

## 1 AI-Assisted Substitution Decisions: A Fuzzy Logic

Approach to Real-Time Game Management

Pedro Passos Farias1

1Institute of Computing – Universidade Federal Fluminense (UFF)

Av. Gal. Milton Tavares de Souza – 24210-346 – Nitero´i – RJ – Brazil pedropassos@id.uff.br

October 2025

## Abstract

With millions on the line every match, top soccer clubs still make critical substitution decisions based largely on intuition. This paper introduces an AI-powered Decision Support

System (DSS) that brings data-driven rigor to one of the game’s most crucial tactical moments. Using fuzzy logic to model expert coaching knowledge, our system provides real-time substitution priorities by integrating validated performance metrics (playerankScore), fatigue (minutesPlayed), age, and disciplinary risk (TemCartaoAmarelo). A key innovation is its contextual logic, which modulates disciplinary risk based on a player’s tactical position (roleCluster), reflecting deeper tactical awareness. Validation through case studies confirms the system’s ability to balance conflicting factors and escalate priority in high-risk scenarios, providing a tangible competitive advantage for real-time game management when every decision counts.

1 17 Introduction

18 The financial stakes in modern soccer have never been higher, creating a vast economic 19 disparity between clubs. In the 2023/24 season, Manchester City earned £175.9 million 20 in prize money for winning the Premier League title ge (2025). In contrast, Fluminense, 21 a Brazilian club with more modest economic power, received a total of US$50.71 million 22 for reaching the semifinals of the 2025 Club World Cup—a sum that could have escalated 23 to US$40 million for winning the finalESPN.com.br (s.d.). 24 Despite these immense financial consequences, one of the most impactful in-game 25 decisions: player substitutions, often remains guided by intuition and limited visible cues. 26 As top coaches like Guardiola acknowledge, the timing and choice of a substitution can 27 be the difference between winning titles and missing crucial opportunities. 28 This gap is particularly evident because tactical decision-making during a soccer match 29 is one of the most complex and high-impact processes in team management. Substitu30 tions, changes in tactical posture, or defensive adjustments are frequently made by coaches 31 based on a combination of empirical knowledge and a multifactorial assessment of inher32 ently imprecise variables. Factors like ”the player looks tired,” ”performance has recently 33 dropped,” or ”the risk of expulsion is high” are not binary, but rather gradual. Perfor34 mance evaluation is, in itself, a notable challenge. Although the availability of large-scale 35 event data has grown, there is no single, universally accepted metric that captures all 36 facets of a player’s performance Pappalardo et al. (2019). 37 This work addresses the problem of tactical decision-making under uncertainty through 38 the implementation of a fuzzy logic control system. Fuzzy logic is an artificial intelligence 39 tool particularly suited for this domain, as it allows for modeling ”expert knowledge” (a 40 coach’s rules) and handling vague linguistic concepts, such as ”high age,” ”low perfor41 mance,” or ”medium fatigue” (Marliere, 2017). The objective of this paper is to design, 42 implement, and validate a decision support system (DSS) focused specifically on player 43 substitution priority. The system uses four inputs (performance, fatigue, age, and disci44 plinary risk) to generate a fuzzy output (Substitution Priority), providing a quantitative 45 tool to assist the coaching staff with one of their most critical real-time decisions.”

2 46 Literature Review

47 The academic literature on data analysis in soccer provides the theoretical foundation 48 for this work, which lies at the intersection of performance evaluation and tactical deci49 sion modeling. The first methodological challenge is to quantify a player’s performance. 50 The PlayeRank framework, proposed by Pappalardo Pappalardo et al. (2019), addresses 51 this problem by defining a multidimensional and role-aware evaluation metric, academi52 cally validated against professional scout assessments. Given its robustness, we adopt the 53 playerankScore as the basis for our main performance input, avoiding the subjectivity 54 of creating a new metric. The second challenge is how to interpret imprecise data for 55 decision-making. The literature justifies the use of fuzzy logic as the central methodolog56 ical tool for this purpose. Works such as that by Huarachi-Macuri et al. LACCEI (2023) 57 demonstrate the effectiveness of fuzzy systems for evaluating player performance by mod58 eling imprecise linguistic concepts like ”Stamina” and ”Agility”. This approach validates 59 the ”what” of our system: the transformation of quantitative metrics (like minutesPlayed 60 and IdadeDoJogador) into the fuzzy concept of Fatigue. Similarly, the tactical decision 61 support literature, such as Marliere’s work Marliere (2017) in the context of robot soccer, 62 uses fuzzy control systems to arbitrate between tactical actions (e.g., ”heavy defense,” 63 ”light attack”). This approach validates the ”why” of our system: the generation of a 64 decision output, in our case, the Substitution Priority. Despite these foundations, a gap 65 was identified in the existing literature. While previous works focus on evaluating player 66 performancePappalardo et al. (2019); LACCEI (2023), or modeling general tactical as67 pects Marliere (2017), there is still no decision support system that integrates validated 68 performance metrics (like PlayeRank ) with other critical game factors, such as fatigue 69 and disciplinary risk, to assist in the specific tactical decision of player substitution. This 70 work proposes to fill this gap by uniting performance evaluation approaches with a deci71 sion engine based on fuzzy logic, with the goal of developing a system aimed at supporting 72 substitutions. .

3 73 Dataset

74 The database selected for this project is the ”Soccer match event dataset”, a detailed 75 public repository of soccer match events (Pappalardo, 2020). The choice of this dataset 76 is based on its high granularity. The dataset details player-level actions and aggregated 77 performance metrics, allowing for the modeling of in-game situations, which is an es78 sential requirement for our system. We used the complete dataset available on Kaggle 79 (Pappalardo, 2020), which comprises 27 interrelated CSV tables. They cover seven main 80 competitions and can be grouped into five logical categories:

81 • Match Data (matches *.csv): Contains information about the games, such as dates, lineups, substitutions, results, and tactical formations.

83 • Event Data (events *.csv): The core of the dataset, recording millions of individual actions on the field.

85 • Entity Data (players.csv, teams.csv, etc.): Dimensional tables with demographic and static data.

87 • Performance Metrics (playerank.csv): A pre-processed file that provides the playerankScore, a multidimensional and role-aware performance evaluation metric.

89 • Dictionaries (tags2name.csv, eventid2name.csv): Metadata that translate event and tag IDs into readable descriptions (e.g., Tag 1702 = ’yellow card’).

91 The choice of playerankScore as our main ”Performance” input is a central method92 ological decision. As proposed by PappalardoPappalardo et al. (2019), the PlayeRank 93 framework was developed to solve the absence of a consolidated and universally accepted 94 metric for evaluating player performance. The playerankScore is a metric derived from 95 millions of game events that, according to the authors, surpasses other metrics when com96 pared with assessments from professional scouts. Therefore, instead of trying to model 97 performance from raw events, we adopted the playerankScore as an already validated 98 and academically robust representation of a player’s performance in a match.

100 Dataset available at: 101 https://www.kaggle.com/datasets/aleespinosa/soccer-match-event-dataset/data? 102 select=playerank.csv

4 103 Data Integration and Pre-processing

104 The goal of pre-processing was to consolidate this ecosystem of 16 relevant files (7 from 105 matches, 7 from events, players.csv, and playerank.csv) into a single structured 106 dataset. Each row of the final dataset represents a single ”player-match” instance. The 107 integration process followed three main steps:

108 1. Base and Main Variables: We used playerank.csv as the main table, providing the inputs for playerankScore (Performance) and minutesPlayed (Fatigue), in addition to roleCluster (Player position).

111 2. Creation of the Age Feature: To create the IdadeDoJogador variable, we performed a data join. The date of birth (birthDate) was obtained from players.csv and the match date (date) was extracted from the concatenation of the seven matches *.csv files. The age was then calculated in fractional years at the exact moment of the match.

116 3. Creation of the Risk Feature: For the TemCartaoAmarelo variable, we processed the concatenation of the seven events *.csv files (totaling millions of events). We filtered all events that contained the tag 1702 (identified via tags2name.csv as

’yellow card’) and created a boolean indicator for each (matchId, playerId) pair that received a card.

121 Rows where crucial information (like birthDate or date) was missing were removed. 122 This process resulted in a final clean and validated dataset of 46,897 instances. Table 123 1 summarizes the final attributes used as inputs for the fuzzy system.

Table 1: Attributes of the Consolidated Dataset for the Fuzzy System

Attribute

Description

## Data type

Identifiers Context (Rules) Fuzzy Input 1 Fuzzy Input 2 Fuzzy Input 3 Fuzzy Input 4 matchId, playerId roleCluster playerankScore minutesPlayed IdadeDoJogador TemCartaoAmarelo

Identification keys. Player’s tactical position. Performance metric. Total minutes played. Player’s age on the match day. (1) if received card, (0) otherwise.

Integer Categorical Real Integer Real Integer

5 124 Exploratory Data Analysis

125 The exploratory analysis was conducted on the final dataset of 46,897 instances. The ob126 jective was to define the universes of discourse (ranges of values) and to quantitatively 127 substantiate the design of the membership functions for the control system.

128 5.1 Univariate Analysis: Defining the Universes

129 The analysis of the four input variables (Figure ??) revealed their limits:

130 • Input 1: playerankScore (Performance). As justified in Section 3, this metric is a multidimensional performance evaluation Pappalardo et al. (2019). Although the theoretical framework might describe the score on a normalized scale (e.g., 0 to

1) for presentation purposes, the raw dataset used contains the scores standardized around zero. Our exploratory analysis confirmed this: the observed universe of discourse ranges from -0.119 (very low performance) to 0.173 (elite performance), with the mean (0.007) and median (0.004) very close to zero. This characteristic is ideal for fuzzy logic, as zero represents an ”average performance,” allowing for the creation of Low (negative), Medium (near zero), and High (positive) sets.

139 • Input 2: minutesPlayed (Fatigue). The fatigue universe ranges from 1 to 120 minutes (extra time). The distribution shows strong negative skewness (skewness of -1.40), with the median at 90 minutes. In fact, 59.3% of the instances (n=27,828) represent players who played the full 90 minutes.

143 • Input 3: IdadeDoJogador (Age). Age presents a normal distribution, with the mean (26.68 years) and median (26.51 years) being almost identical. The universe is defined between 15.89 and 41.37 years (oldest age recorded in the dataset). This symmetrical distribution supports the creation of three balanced fuzzy sets: Young,

Peak (centered on the mean), and Veteran.

148 • Input 4: TemCartaoAmarelo (Risk). This is a binary input. The analysis revealed that 15.34% of all player-match instances (n=7,194) involve a yellow card, confirming its importance as a risk factor.

151 5.2 Bivariate and Multivariate Analysis: Validating the Rules

152 This analysis validates the common-sense soccer assumptions that we will use to build 153 the system’s rules. 154 5.2.1 Validation of the Context Rule: Risk vs. Position 155 The central premise is that the risk of a yellow card is position-dependent . The Figure 156 below validates this hypothesis. Defensive positions (right CB 19.1%; left CB 18.5%) 157 and central midfielders (central MF 17.3%) show a statistically higher risk. In contrast, 158 attacking positions (central FW 11.1%; right FW 10.3%) show a significantly lower risk. 159 This finding justifies the creation of contextual rules, where the roleCluster variable will modulate the importance of the TemCartaoAmarelo input.

161 5.2.2 Independence and Relationships of Inputs 162 The Spearman correlation matrix (Figure 5.2.2) reveals that the four input variables are, 163 for the most part, independent. All correlations are weak (below |0.2|). The strongest 164 negative correlation is between TemCartaoAmarelo and playerankScore (-0.179). This 165 suggests that receiving a card is associated with a drop in performance. Table 2 reinforces 166 this: for the most common positions, the average playerankScore is consistently lower 167 for players with a card.

Table 2: Average Performance (playerankScore) by Position and Risk.

Position (roleCluster) Score (No Card) Score (With Card) left CB right CB central MF right MF left MF central FW

0.0112 0.0108 0.0070 0.0030 0.0018 0.0119

0.0055 0.0046 -0.0007 -0.0039 -0.0050 0.0063

168 5.3 Analysis Conclusion

169 The exploratory data analysis allowed for a detailed characterization of the final dataset 170 of 46,897 instances, establishing a solid foundation for understanding the variables before 171 modeling. The univariate analysis (Section 5.1) defined the practical limits (universes of 172 discourse) for the numerical inputs: playerankScore [-0.119, 0.173], minutesPlayed [1, 173 120], and IdadeDoJogador [15.9, 41.37]. It also quantified their distributional charac174 teristics, notably the normality of age (mean 26.7), the strong concentration of minutes 175 played at 90 (median 90), and the peaked, right-skewed distribution of performance (me176 dian 0.004). The prevalence of the binary variable TemCartaoAmarelo was established at 177 15.34% . Subsequently, the bivariate and multivariate analysis (Section 5.2) confirmed 178 two central hypotheses: the statistical dependence of disciplinary risk on tactical position 179 (roleCluster), with defenders showing a higher propensity for cards, and the low mu180 tual correlation among the four input variables (all < |0.18| in the correlation matrix),

181 indicating their informational independence. With these characteristics quantified and 182 relationships validated, the data exploration is complete.

6 183 Fuzzy Control System Design

184 Based on the theoretical foundation (Section 2) and the quantitative data analysis (Sec185 tion 5), we designed the Fuzzy Control System (FCS) to evaluate Substitution Priority. 186 The system was implemented using the scikit-fuzzy library in Python, following the 187 standard Mamdani architecture for fuzzy inference and the Centroid method for defuzzi188 fication.

189 6.1 Definition of Fuzzy Variables

190 The system comprises four input variables (antecedents) and one output variable (conse191 quent). The universes of discourse were defined from the minimum and maximum values 192 observed in the Exploratory Analysis (Section 5.1), with a 5% margin to ensure the model 193 can accommodate values more extraordinary than those recorded in the dataset.

194 6.1.1 Antecedents (Inputs) 195 1. Performance (desempenho): Based on playerankScore.

• Universe of Discourse: [-0.134, 0.188].

• Fuzzy Sets: Low, Medium, High.

198 2. Fatigue (fadiga): Based on minutesPlayed.

• Universe of Discourse: [0, 126] minutes.

• Fuzzy Sets: Low, Medium, High.

201 3. Age (idade): Based on IdadeDoJogador.

• Universe of Discourse: [14.6, 42.7] years.

• Fuzzy Sets: Young, Peak, Veteran.

204 4. Risk (risco): Based on TemCartaoAmarelo.

• Universe of Discourse: [0, 1].

• Fuzzy Sets: NoRisk, WithRisk.

207 6.1.2 Consequent (Output) 208 • Substitution Priority (prioridade): Indicates the calculated urgency .

– Universe of Discourse: [0, 10].

– Fuzzy Sets: Low, Medium, High.

211 6.2 Membership Functions

212 The membership functions were designed using triangular (trimf) and trapezoidal (trapmf) 213 functions for the continuous variables, and narrow Gaussian functions (gaussmf) for the 214 binary variable Risk, aiming for interpretability and reflecting the distributions observed 215 in the EDA (Section 5.1). The exact parameters used in the Python implementation are:

216 • Performance: Low = trapmf([-0.134, -0.134, -0.03, 0.004]); Medium = trimf([-

0.03, 0.004, 0.04]); High = trapmf([0.004, 0.04, 0.188, 0.188]). The narrow Medium set reflects the high kurtosis of the distribution.

219 • Fatigue: Low = trapmf([0, 0, 40, 70]); Medium = trimf([40, 70, 95]); High = trapmf([70, 95, 126, 126]). The High set is concentrated after 70 minutes, reflecting the median at 90.

222 • Age: Young = trapmf([14.6, 14.6, 22, 27]); Peak = trimf([22, 27, 32]); Veteran

= trapmf([27, 32, 42.7, 42.7]). The sets are approximately symmetrical around the mean of 26.7 years.

225 • Risk: NoRisk = gaussmf(mean=0, sigma=0.1); WithRisk = gaussmf(mean=1, sigma=0.1). Narrow Gaussians provide a smooth transition and robustness if the input is not exactly 0 or 1.

228 • Priority (Output): Low = trimf([0, 0, 5]); Medium = trimf([0, 5, 10]); High = trimf([5, 10, 10]). Overlapping triangular functions to allow interpolation in the output.

231 6.3 Rule Base and Contextual Logic

232 The knowledge base was built by combining domain knowledge inspired mainly by the 233 statements of coach Josep Guardiola (ESPN Brasil, s.d.; Terra Esportes, s.d.; CNN Brasil 234 Esportes, s.d.), with the validations from the EDA. A set of 17 base rules was defined (see

Table 3 for examples), using the AND (minimum) operator to combine antecedents.

ID Rule

Table 3: Complete Set of Base Fuzzy Rules.

A1 IF (Performance is Low AND Fatigue is High) THEN (Priority is High) A2 IF (Performance is Low AND Age is Veteran AND Fatigue is Medium)

THEN (Priority is High) A3 IF (Fatigue is High AND Age is Veteran) THEN (Priority is High) A4 IF (Risk is WithRisk AND Fatigue is High) THEN (Priority is High) A5 IF (Risk is WithRisk AND Performance is Low) THEN (Priority is High)

B1 IF (Performance is High AND Fatigue is Low AND Risk is NoRisk) THEN (Priority is Low)

B2 IF (Performance is High AND Age is Young AND Risk is NoRisk) THEN (Priority is Low)

B3 IF (Performance is Medium AND Fatigue is Medium AND Age is Peak AND Risk is NoRisk) THEN (Priority is Low)

B4 IF (Performance is High AND Fatigue is Medium AND Risk is NoRisk) THEN (Priority is Low)

M1 IF (Performance is Low AND Fatigue is Medium) THEN (Priority is Medium)

M2 IF (Performance is Medium AND Fatigue is High AND Risk is NoRisk) THEN (Priority is Medium)

M3 IF (Age is Veteran AND Fatigue is Medium AND Risk is NoRisk) THEN (Priority is Medium)

M4 IF (Performance is High AND Fatigue is High AND Risk is NoRisk) THEN (Priority is Medium)

R1 IF (Risk is WithRisk AND (Fatigue is Medium OR Fatigue is High)) THEN (Priority is High)

R2 IF (Risk is WithRisk AND Fatigue is Low) THEN (Priority is Medium) R3 IF (Risk is WithRisk AND Age is Veteran) THEN (Priority is Medium) R4 IF (Risk is WithRisk AND Performance is Medium) THEN (Priority is

Medium)

236 However, the EDA (Section 5.2) demonstrated the crucial importance of the cate237 gorical variable roleCluster (Position) in modulating Risk. As this variable is not 238 fuzzy, a post-inference contextual logic was implemented. The system first calcu239 lates a base priority using the 17 fuzzy rules. Then, an external function (‘calcu240 lar prioridade contextual‘ in the Python code) evaluates the player’s position and risk 241 level:

242 • If the player is a Defender (’CB’) and the risk is high, the final priority is adjusted to a high minimum value (e.g., 8.0).

244 • If the player is a Midfielder (’MF’), has high risk, and is tired (Medium or High

Fatigue), the final priority is adjusted to a medium-high minimum value (e.g., 7.5)

.

247 • If the player is a Forward (’FW’) with high risk, the base priority is generally maintained (considered Medium), but may be limited if the performance is high.

249 This hybrid approach allows combining the flexibility of fuzzy inference with ”crisp” 250 contextual rules essential for the domain.

251 6.4 Inference and Defuzzification

252 The system uses the Mamdani inference method, where the result of each rule’s activa253 tion is aggregated (using the ‘OR‘ = maximum operator) to form a resulting membership 254 function for the output variable Priority. The conversion of this aggregated fuzzy func255 tion into a final numerical (crisp) value is performed by the Centroid method, which 256 calculates the center of mass of the area under the curve of the resulting membership 257 function. This value, on a scale of 0 to 10, represents the Substitution Priority calculated 258 by the system. 259 Codes available at https://github.com/Pedro-Passos77/Sistema-de-Apoio-a-Decisao260 Baseado-em-Logica-Nebulosa

7 261 Results

262 In this section, we evaluate the behavior of the Fuzzy Control System (FCS). The goal 263 of the validation is not to measure predictive accuracy against actual substitutions (as 264 we do not have a ground truth for ”ideal priority”), but rather to verify if the system 265 produces outputs that are logically consistent with the inputs, the fuzzy rules, and the 266 implemented contextual logic. To do this, we applied the FCS to four representative 267 scenarios, covering different combinations of performance, fatigue, age, risk, and tactical 268 position. The system’s output, Substitution Priority, is a numerical value on a [0, 10] 269 scale, interpreted as Low (approx. 0-3.5), Medium (approx. 3.5-6.5), and High (approx. 270 6.5-10).

271 7.1 Analysis of Typical Scenarios

272 The following four scenarios were simulated using the calcular prioridade contextual 273 function, which integrates the base fuzzy inference with contextual position adjustments.

274 7.1.1 Scenario 1: Solid Performance, Low Risk 275 In this scenario, we evaluate a young player (21 years old, Age = Young/Peak), play276 ing as a midfielder (’central MF’), with good performance (playerankScore = 0.05, 277 Performance = High), low time on field (30 min, Fatigue = Low), and no yellow card 278 (TemCartaoAmarelo = 0, Risk = NoRisk). 279 Result: The system calculated a Priority = 1.67. Discussion: This value, clearly in 280 the Low range, is aligned with expectations. The low priority rules (like B1 and B2) were 281 activated by the combination of favorable performance, low fatigue, and absence of risk. 282 The system correctly identifies that there is no urgency to substitute a player in these 283 conditions, reflecting the philosophy of keeping players who are contributing positively 284 and without restrictions.

285 7.1.2 Scenario 2: Veteran Defender Under Risk

286 We evaluate a defender (’right CB’), veteran (34 years old, Age = Veteran), with consid287 erable time on field (85 min, Fatigue = High), average performance (playerankScore = 288 0.001, Performance = Medium), and with a yellow card (TemCartaoAmarelo = 1, Risk 289 = WithRisk). 290 Result: The system calculated a Priority = 8.00. Discussion: This High Priority re291 sult demonstrates the effectiveness of the contextual logic. Although the base rules (like 292 A3, A4, R1, R3) were already activated by the combination of high fatigue, advanced age, 293 and risk, the contextual function, by identifying that the player is a defender (’CB’) with 294 risk, applied a minimum adjustment, raising the final priority to 8.00. This correctly re295 flects the high tactical risk associated with a yellow-carded and potentially tired defender 296 at the end of the game, a scenario where substitution is often considered a priority.

297 7.1.3 Scenario 3: Yellow-carded and Exhausted Midfielder

298 We consider a midfielder (’left MF’) at peak age (29 years old, Age = Peak), with aver299 age performance (playerankScore = 0.0, Performance = Medium), but with very high 300 playing time (95 min, Fatigue = High) and with a yellow card (TemCartaoAmarelo = 1, 301 Risk = WithRisk). 302 Result: The system calculated a Priority = 7.50. Discussion: Again, a High Priority 303 value. The base rules A4 and R1 (Risk + High/Medium Fatigue) were strongly acti304 vated. The contextual logic for midfielders (’MF’) with risk and fatigue also contributed, 305 ensuring a minimum priority of 7.50. Although slightly lower than the defender scenario 306 (perhaps reflecting a marginally lower tactical risk), the system correctly identifies this as 307 a high-urgency situation for substitution, due to the combination of physical exhaustion 308 and disciplinary risk in a central field position.

309 7.1.4 Scenario 4: Yellow-carded, Tired, but Decisive Forward

310 This scenario explores the trade-off between risk/fatigue and high performance. We eval311 uate a forward (’central FW’) at peak age (25 years old, Age = Peak), with excellent

312 performance (playerankScore = 0.08, Performance = High), high playing time (80 min, 313 Fatigue = Medium/High), and with a yellow card (TemCartaoAmarelo = 1, Risk = With314 Risk). 315 Result: The system calculated a Priority = 6.00. Discussion: The result (in the 316 Medium-High range) captures the complexity of the decision. The rules related to risk 317 (R1, R3, R4) and fatigue push the priority up. However, rules B4 (High Performance + 318 Medium Fatigue) and M4 (High Performance + High Fatigue) exert an opposing force, 319 reflecting the principle of keeping a decisive player on the field. The contextual logic for 320 forwards (’FW’) with risk and good performance limited the final priority to 6.00, sug321 gesting that substitution should be considered, but is not as critical as in scenarios 2 and 322 3, given the player’s positive impact on the game. The system demonstrates the ability 323 to balance conflicting factors.

324 7.2 Aggregated Analysis of Results

325 To evaluate the overall behavior of the system, the SCN was applied to all 46,897 instances 326 of the dataset, generating a benchmark dataset with the CalculatedPriority. The dis327 tribution of this variable provides an initial view of the model’s recommendation profile. 328 The histogram shows that most results fall within the range of 4 to 6, indicating a predom329 inance of priorities classified as Medium. This pattern is partially influenced by the high 330 incidence of players who played 90 minutes or more (59.3%, see Section 5.1), frequently 331 activating rules associated with High Fatigue (e.g., A1, A3, A4, M2, M4, and R1), which 332 naturally increase the priority score. However, the distribution does not concentrate in the 333 High range, suggesting that other factors moderate the priority in most instances, such 334 as median performance (playerankScore median of 0.004), peak-age players (median age 335 26.5 years), and low disciplinary risk (only 15.34% with a card). 336 A more detailed analysis compares the distribution of CalculatedPriority between 337 players who were substituted (‘FoiSubstituido = 1‘, n=10,977) and those who remained on 338 the field (‘FoiSubstituido = 0‘, n=35,920). Descriptive statistics are presented in Table 4. 339 Contrary to initial expectations, both the mean (4.48 vs 4.68) and median (4.74 vs 5.00)

340 are slightly lower for substituted players. This result reflects the influence of fatigue, the 341 contextual nature of the metric, and the complexity of substitution decisions, which are 342 often driven by tactical factors (strategy changes, opponent response, score management) 343 not captured by the SCN’s individual-condition variables. 344 It is important to note that this analysis considers the players’ final state, rather than 345 an in-game state. The ’Not Substituted’ group mainly consists of players who completed 346 90 minutes or more, maximizing the minutesPlayed input and thus receiving high fatigue 347 scores. In contrast, the ’Substituted’ group often left the game earlier (e.g., at 70 minutes). 348 Therefore, a direct comparison of final scores may be distorted by differences in minutes 349 played. An in-game analysis, performed at the exact moment of substitution, would be 350 necessary to evaluate predictive accuracy, but this is outside the scope of the current 351 validation.

Table 4: Comparative Statistics of Calculated Priority by Substitution Status.

Statistic

Not Substituted (0) Substituted (1)

Count (n) Mean Standard Deviation (std) Minimum 25th Percentile Median (50th Percentile) 75th Percentile Maximum

35,920 4.6805 2.1235

0.0 4.7174 5.0035 5.7324 8.2778

10,977 4.4765 1.4758

0.0 3.8105 4.7426 5.1170 8.3333

352 Analyzing data dispersion reveals an important insight. The standard deviation of 353 CalculatedPriority is lower for substituted players (1.48) compared to non-substituted 354 players (2.12). This lower variability suggests that when substitutions are driven by 355 individual conditions, the SCN identifies these situations consistently, producing scores 356 concentrated around the medium range. In contrast, the higher dispersion among non357 substituted players, including some with relatively high priority scores who remained on 358 the field, indicates that other contextual and tactical factors may have influenced the 359 coach’s final decision, even when the model signaled an individual condition justifying a 360 substitution. 361 In summary, the lower variability in substituted players’ scores and the higher disper-

362 sion in non-substituted players reinforce the interpretation that coaches prioritize tactical 363 schemes and game-context factors over isolated individual metrics. This pattern highlights 364 the importance of analyzing SCN results within the game context, rather than solely as 365 absolute priority values.

Figure 1: Distribution of Calculated Substitution Priority for all 46,897 instances in the dataset.

8 366 Conclusion

367 This work demonstrated the feasibility of applying fuzzy logic to create a Decision Sup368 port System (DSS) focused on the substitution priority of soccer players. The designed 369 Fuzzy Control System (FCS) successfully integrated academically validated performance 370 metrics (playerankScore Pappalardo et al. (2019)) with indicators of physical condition 371 (minutesPlayed, IdadeDoJogador) and disciplinary risk (TemCartaoAmarelo), using a 372 rule base inspired by expert knowledge (”Pep” Guardiola) and validated by Exploratory 373 Data Analysis. The validation results indicate that the system behaves in a logically con374 sistent manner. The aggregate analysis and case studies demonstrated the system’s ability 375 to differentiate urgency levels, identify and reflect a conservative tactical philosophy of

376 coaches, and, crucially, implement the contextual logic that adjusts the impact of risk

377 based on the player’s position. The FCS thus provides a quantitative and interpretable

378 index of the player’s individual condition, offering a valuable starting point to assist coach-

379 ing staff in the complex task of managing fatigue and risk during the match. The scope of

380 this project focused on evaluating the player’s condition using aggregated data common in

381 event datasets. Promising future extensions could refine and expand this base. The

382 integration of more granular data, such as Global Positioning System metrics for a more di-

383 rect assessment of fatigue instead of the minutesPlayed proxy, could increase the accuracy

384 of the physical assessment. Similarly, incorporating game context variables (score, remain-

385 ing time, current strategy) would allow the system to provide recommendations even more

386 aligned with immediate tactical needs. The calibration of the membership functions and,

387 especially, the rule base through iterative feedback with coaches and analysts represents a

388 fundamental step to maximize practical applicability and trust in this tool in the pro-

389 fessional environment. The complete source code of the FCS implementation in Python

390 with scikit-fuzzy, including the pre-processing, exploratory analysis, and validation

391 scripts, is publicly available in the following repository: https://github.com/Pedro-

392 Passos77/Sistema-de-Apoio-a-Decisao-Baseado-em-Logica-Nebulosa . The gener-

393 ated benchmark dataset can also be found in the same location, promoting the repro-

394 ducibility of the research. We thank Luca Pappalardo and collaborators for making the

395 Soccer match event dataset publicly available on Figshare (Pappalardo, 2020), which was

396 essential for conducting this study. I highlight that generative artificial intelligence tools

397 were used as an assistant in the writing and revision of parts of this article, always under

398 full human supervision to ensure the accuracy and appropriateness of the final content.

“‘

## 400 References

401 CNN Brasil Esportes. Guardiola ´e o t´ecnico que menos faz substituic¸˜oes na premier league; 402 veja ranking [guardiola is the coach who makes the fewest substitutions in the premier 403 league; see ranking]. https://www.cnnbrasil.com.br/esportes/futebol/futebol-

404 internacional/guardiola-e-o-tecnico-que-menos-faz-substituicoes-na405 premier-league-veja-ranking/, s.d. Accessed on: 24 Oct. 2025.

406 ESPN Brasil. Por que guardiola na˜o fez nenhuma substitui¸c˜ao no city contra o rb leipzig? 407 ele mesmo responde [why didn’t guardiola make any substitutions for city against 408 rb leipzig? he answers]. https://www.espn.com.br/futebol/manchester-city/ 409 artigo/_/id/11661194/por-que-guardiola-nao-fez-nenhuma-substituicao-no410 city-contra-o-rb-leipzig-ele-mesmo-responde, s.d. Accessed on: 24 Oct. 2025.

411 ESPN.com.br. Quanto o fluminense ganhou em premia¸c˜ao no mundial de clubes 412 apo´s elimina¸c˜ao para o chelsea na semifinal. https://www.espn.com.br/futebol/ 413 fluminense/artigo/_/id/15405687/quanto-fluminense-ganhou-premiacao414 mundial-de-clubes-apos-eliminacao-para-o-chelsea-semifinal, s.d. Acesso 415 em: 26 out. 2025.

416 ge. Premia¸ca˜o da premier league: veja quanto cada clube recebeu em 2023/24. 417 https://ge.globo.com/futebol/futebol-internacional/noticia/2025/02/ 418 07/premiacao-da-premier-league-veja-quanto-cada-clube-recebeu-em419 202324.ghtml, 2025. Acesso em: 26 out. 2025.

420 LACCEI. A system for the control of the performance of high level soccer players ap421 plying fuzzy logic. In 2023 LACCEI International Multi-Conference for Engineering, 422 Education, and Technology, 2023.

423 F. T. Marliere. Sistema de apoio `a decisa˜o baseado na lo´gica fuzzy e aplicado ao 424 futebol de roboˆs [decision support system based on fuzzy logic and applied to robot 425 soccer]. https://www2.ufjf.br/eletrica_automacao/wp-content/uploads/sites/ 426 647/2017/02/TCC_Frederick-Tavares-Marliere.pdf, 2017.

427 L. Pappalardo. Soccer match event dataset. https://doi.org/10.6084/m9.figshare. 428 c.4415000.v5, 2020. [Data set].

429 L. Pappalardo, P. Cintia, A. Rossi, E. Massucco, P. Ferragina, D. Pedreschi, and F. Gian430 notti. Playerank: Data-driven performance evaluation and player ranking in soccer via

431 a machine learning approach. ACM Transactions on Intelligent Systems and Technology 432 (TIST), 10(5):1–24, 2019. 433 Terra Esportes. Guardiola explica n˜ao ter feito substitui¸c˜oes no duelo contra o 434 real madrid [guardiola explains not making substitutions in the match against 435 real madrid]. https://www.terra.com.br/esportes/futebol/internacional/ 436 guardiola-explica-nao-ter-feito-substituicoes-no-duelo-contra-o-real437 madrid,e3fd37046389eb17727c7e0d1ef1230ahuy6brqn.html, s.d. Accessed on: 24 438 Oct. 2025.
