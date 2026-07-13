<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2023/2023 - Identifying Key Players and Playing Styles of 10 English Premier League Teams During Offensive Sequences in 2021-2022 Season - Unknown Authors.pdf -->



# **Identifying Key players & playing styles of 10 English Premier League Teams during offensive sequences in 2021/2022 season** 

### Praful Upadhyay & Janik Backhaus 

praful.upadhyay1@gmail.com 

## **Introduction** 

In the realm of soccer, the essence of player interactions, particularly through passes, lies at the core of creating scoring opportunities. These interactions, encapsulating a team's strategies, form the bedrock of playing styles, which manifest as characteristic patterns exhibited by teams in various situational contexts [1]. While several works have attempted to define team playing styles, there remains a critical need to comprehensively understand these styles within the broader context of team tactics, especially during offensive sequences [2]. 

#### **1.1. Research Gap** 

Existing frameworks, such as the REOFUT playing styles framework [2, 7, 8, 17], have offered insights into team playing styles. However, they often overlook the roles and connectivity of individual players, which are pivotal during goal-critical offensive sequences and provide valuable insights into attacking set-pieces. Many of these frameworks analyze team attacks primarily from locational and temporal perspectives, without considering the distinct roles and performances of individual players separately [2]. This gap underscores the necessity for further research to bridge this divide. 

**1** 



#### **1.2. Study Objectives** 

This study seeks to broaden the comprehensive understanding of team tactics through an exploration of playing styles and player connectivity during offensive sequences. Specifically, the study aims to identify key players with substantial involvement and importance in possession sequences. The outcomes of this research will illuminate the key positions within a team, reflecting the distinct players and their interactions during offensive maneuvers. The central hypothesis posits that analyzing player interactions within the possession framework will reveal essential connections and interaction patterns among players, leading to a deeper understanding of key attacking positions and team playing styles, in contrast to existing frameworks [8, 17], which predominantly focus on ball and player parameters. 

## **Methodology** 

The primary objective of this study is to establish a possession framework capable of categorizing possession sequences into three distinct groups, as exemplified in Table 1. By classifying sequences into different categories, we aim to gain specific insights into team strategies during both unsuccessful and shot and goal sequences. Some of the previous work in a similar direction also included a possession sequence framework based on time duration [18]. 



<!-- Start of picture text -->
Possession Definition<br>Shot & Goal sequences Team attempts a shot or scores a goal.<br>Partially Successful sequences Team retains the possession<br>Unsuccessful sequences Team loses possession<br><!-- End of picture text -->

Table 1. Possession sequence framework 

The design of the possession sequence categories serves several key purposes. It seeks to identify players who are more involved in shot and goal sequences than in unsuccessful 

**2** 



attempts. Additionally, it examines whether team connectivity and cohesion change across these two categories. Furthermore, the framework allows for comparisons with other teams, shedding light on different playing styles and approaches. Consequently, the possession sequences are instrumental in dissecting the components that contribute to team attacks. 

To classify possession sequences, the procedure commences with identifying the team in possession. This categorization extends until the opponent's team name appears in the possession variable for two consecutive events, accompanied by the detection of either a "Pass" or "Carry Ball" event by the opposing team. For example, figure 1. Shows one possession sequence in which the possession starts with Riyad and ends at Joao. The entire possession sequence consists of 51 passes. 



Figure 1: Manchester City 51 passes possession sequence. 

**3** 



Following the categorization of possession sequences, each sequence is converted into an adjacency matrix, denoted as X. Within this matrix, each entry, represented as Xi,j, signifies the count of passes from player i to player j during the respective possession sequence. Notably, our approach treats both inbound and outbound passes equally, without incorporating centrality measures based on the direction of passes. For example, figure 2. 



Figure 2: The network of the possession sequence mentioned in figure 1. 

**4** 



#### **2.3. Study Parameters** 

In this study, the main study parameters to understand the team playing style and players' interactions are closeness centrality, betweenness centrality, and On Ball Value. 

##### 2.3.1. Closeness Centrality 

According to the work done by Penz [20] defines closeness score explains how easy it is to reach a particular player within the team. A higher centrality score of a player signifies a small average, which means a well-connected player within the team. This is crucial information to understand which players with positional roles were more connected in unsuccessful and shot & goal sequences. Furthermore, the team where the connectivity between players or certain positions is higher reflects the importance of the players, strategies of the team to initiate attacks in different situations, and other information. 





where d(I,j) represents the distance between player I and all other players j. 

##### 2.3.2. Betweenness Centrality 

The second study parameter of centrality measures analyzed is betweenness. Penz [20] explains betweenness how different players contribute to ball flow. Betweenness centrality measures how different players contribute to the flow of the ball within the team's network [20]. Players with high betweenness centrality act as crucial bridges or intermediaries in passing sequences. The formula for betweenness centrality is defined as follows: 





By examining betweenness centrality, we can discern which players play pivotal roles in facilitating ball movement between different parts of the team. This parameter highlights players 

**5** 



who have a significant impact on shaping the team's offensive patterns and the distribution of possession. Understanding the contributions of various players in ball flow is instrumental in comprehending team dynamics and strategies. 

In this study, we employ primary study parameters to comprehend team playing styles and player interactions. In this study, we also aimed to analyze the Average Betweenness ratio (eq.4) and Average Closeness Ratio (eq. 4) to understand player involvement in shot & goal sequences compared to unsuccessful sequences. This information can be used in several ways, for instance, the average closeness ratio of all the players in the team shows the wellconnected players between lines of attacks during shot & goal sequences rather than unsuccessful sequences. Furthermore,  the average betweenness ratio of all the players in the team can clearly show the interaction between players for ball flow between lines of attacks . 

##### 2.3.3. On Ball Value (OBV) 

OBV assesses a player's effectiveness, impact, and decision-making ability when in possession of the ball during a match. It encompasses skills in dribbling, passing, creating goal-scoring opportunities, maintaining possession under pressure, and strategic decision-making to advance team objectives. In this study, we aim to evaluate the correlation between OBV values, Average Betweenness Ratio, and Average Closeness Ratio for players in shot & successful sequences. 

<mark>In the present study centrality measures and OBV average values are calculated and normalized by the equations mentioned below.</mark> 

<mark>1. 𝐶𝑒𝑛𝑡𝑟𝑎𝑙𝑖𝑡𝑦 𝑆𝑐𝑜𝑟𝑒 𝑝, 𝑖, 𝑗 𝑖𝑠 𝑡ℎ𝑒 𝑐𝑒𝑛𝑡𝑟𝑎𝑙𝑖𝑡𝑦 𝑠𝑐𝑜𝑟𝑒 𝑜𝑓 𝑡ℎ𝑒 𝑝𝑙𝑎𝑦𝑒𝑟 𝑝 𝑖𝑛 𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒, 𝑗 𝑖𝑛 𝑚𝑎𝑡𝑐ℎ 𝑖.</mark> 

<mark>2. 𝑘 𝑖𝑠 𝑡ℎ𝑒 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒 𝑎 𝑝𝑙𝑎𝑦𝑒𝑟 𝑝 𝑖𝑛𝑣𝑜𝑙𝑣𝑒 𝑎𝑛𝑑 𝑛 𝑖𝑠 𝑡ℎ𝑒 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑔𝑎𝑚𝑒𝑠 𝑝 𝑝𝑙𝑎𝑦𝑒𝑟 𝑖𝑛𝑣𝑜𝑣𝑙𝑒</mark> ~~<mark>.</mark>~~ <mark>Parameter Value of a player =</mark> ∑∑𝐶𝑒𝑛𝑡𝑟𝑎𝑙𝑖𝑡𝑦 𝑆𝑐𝑜𝑟𝑒 𝑝, 𝑖, 𝑗𝑛𝑖 𝑘𝑗 (equation(eq.) number 1.) 

Weighted CM value of a player in single match  = CM  of a player <mark>*</mark> 𝑃𝑙𝑎𝑦𝑒𝑟 𝑚𝑖𝑛𝑢𝑡𝑒𝑠 𝑝𝑙𝑎𝑦𝑒𝑑 𝑖𝑛 𝑡ℎ𝑒 𝑚𝑎𝑡𝑐ℎ (eq. 2.) 𝑃𝑙𝑎𝑦𝑒𝑟 𝑡𝑜𝑡𝑎𝑙 𝑀𝑖𝑛𝑢𝑡𝑒𝑠 𝑝𝑙𝑎𝑦𝑒𝑑 𝑖𝑛 𝑠𝑒𝑎𝑠𝑜𝑛 

<mark>Average Parameter values of a player =   X  All weighted Parameter values of a player in all matches   (eq. 3.)</mark> 

> Player Centrality Parameter Ratio = 𝑃𝑙𝑎𝑦𝑒𝑟 𝐴𝑣𝑒𝑟𝑎𝑔𝑒 𝐶𝑒𝑛𝑡𝑟𝑎𝑙𝑖𝑡𝑦 𝑃𝑎𝑟𝑎𝑚𝑒𝑡𝑒𝑟 𝑣𝑎𝑙𝑢𝑒 𝑖𝑛 𝑈𝑛𝑠𝑢𝑐𝑐𝑒𝑠𝑠𝑓𝑢𝑙 𝑆𝑒𝑞𝑢𝑒𝑛𝑐𝑒𝑠 (eq.4.) 𝑃𝑙𝑎𝑦𝑒𝑟 𝐴𝑣𝑒𝑟𝑎𝑔𝑒 𝐶𝑒𝑛𝑡𝑟𝑎𝑙𝑖𝑡𝑦 𝑃𝑎𝑟𝑎𝑚𝑒𝑡𝑒𝑟  𝑣𝑎𝑙𝑢𝑒 𝑖𝑛 𝑆ℎ𝑜𝑡 & 𝐺𝑜𝑎𝑙 𝑆𝑒𝑞𝑢𝑒𝑛𝑐𝑒𝑠 

**6** 



#### **2.1. Sample size** 

<mark>The study aims to analyze 10 teams of the English Premier League from season 2021/2022. For each team, 38 matches were analyzed.</mark> 

#### **<mark>2.2 Inclusion Criteria</mark>** 

<mark>The study only includes the players in the analysis who played a minimum of 1000 minutes. The total minute played threshold for inclusion aims to reduce the stochasticity in results. Furthermore, the threshold is also widely used in several Xg matrices.</mark> 

**7** 



## **Results** 

This section explains the results of the study. The results of each study parameters are defined in each subsection. 

#### **3.1 Possession Framework** 

Figure 2. explains the detailed results of the possession framework of each analyzed team. The possession Framework suggested the number of shots & goal sequence are higher for higherranking teams in comparison to lower-rank teams. On the other hand, a higher-ranked team has a lower number of unsuccessful sequences in comparison to a lower-ranked team which has a higher number of unsuccessful sequences. 



Figure 2. Possession Framework results of 10 team 

**8** 



#### **3.2 Betweenness Centrality Measures** 

<mark>This section briefly explains the results of Betweenness Centrality measures.</mark> 

- 3.2.1. Average Betweenness Values in Shot & goal sequences and Unsuccessful Sequences 



Figure 3. Average Betweenness values of Team players in Shot & goal sequences and Unsuccessful sequences. 

Figure 3 illustrates the results of players' average betweenness values in both shot & goal sequences and unsuccessful sequences, as calculated using equations 1, 2, and 3. These values are segmented by player positions (backs, midfielders, and forwards) and team rankings. 

The analysis reveals that players in different positions exhibit varying betweenness values. Higher-ranked teams tend to consist of players with higher betweenness values in both 

**9** 



unsuccessful and successful sequences. This indicates a hierarchal connectivity among players for ball flow in top-ranking teams compared to lower-ranking teams. Players in higher-ranked teams significantly interact with each other, primarily due to these teams having lower unsuccessful sequences and more shot & goal possession sequences. 

- 3.2.2. Average Betweenness Values in Shot & goal sequences and Unsuccessful Sequences of MC and Liverpool. 



Figure 4. Average Betweenness values of Manchester City and Liverpool players in shot & goal sequences and Unsuccessful sequences. 

Figure 4 offers a comparative view of players' average betweenness values between Manchester City and Liverpool teams. Notably, Manchester City's back players, who form the first line of attack, exhibit the highest betweenness values, indicating strong coordination and availability of players for building attacks. A similar trend is observed among Liverpool's back 

**10** 



players, but their midfielders also display significant connectivity with each other. In contrast, Manchester City's center midfielders have a higher involvement in shot & goal sequences compared to Liverpool. Additionally, Liverpool's forward players exhibit strong connections with both midfield and back players, unlike Manchester City's forward players. 



Figure 5. Average Betweenness Values of Teams 

This section explains the detailed results of the Betweenness centrality ratio (eq. 4) of all teams. Figure 5. suggested average Betweenness ratio is higher of higher rank teams in shot & goal sequences than in unsuccessful sequences in comparison to rank teams. 

**11** 



3.2.3. Average Betweenness Values in Shot & Goal Sequences and Unsuccessful Sequences 



Figure 6. Players Betweenness Ratio in Unsuccessful vs. Shot & Goal Sequences with Total Minutes Played. 

Figure 6. explains the Players Betweenness Ratio calculated by eq. 4 and the Total Minutes played in a season. There is a weak /no correlation between players with high ratio value and higher total minutes played. 

**12** 



#### **3.3. Closeness Centrality Measures** 

This section explains the detailed results of the Closeness centrality measures of each analyzed team. 

- 3.3.1. Average Closeness Values in Shot & Goal Sequences and Unsuccessful Sequences 



Figure 7. Average Closeness values of Team players in Shot & goal sequences and Unsuccessful sequences. 

Figure 7 presents the results of players' average Closeness values in both shot & goal sequences and unsuccessful sequences, as calculated using equations 1, 2, and 3. It's 

**13** 



noteworthy that there appears to be a weak or no correlation between higher Closeness values of players and their respective team rankings. Across different teams, players exhibit higher Closeness values in both shot & goal sequences and unsuccessful sequences. 

- 3.3.2. Average Closeness Values in Shot & goal sequences and Unsuccessful Sequences in MC and Liverpool. 



Figure 8. Average Closeness values of Manchester City and Liverpool players in Unsuccessful sequences. 

Figure 8 offers a detailed comparison of average Closeness values between Manchester City and Liverpool players specifically in unsuccessful sequences. Interestingly, it shows that Manchester City's center and forward players exhibit higher connectivity during shot & goal sequences compared to Liverpool. In contrast, Liverpool demonstrates strong connections between forward and back players. Notable players like Arnold display the highest connectivity in both unsuccessful and shot & goal sequences, while Salah is more connected in the shot & goal sequences. Moreover, Liverpool's midfielders and defenders show greater involvement in shot & goal sequences compared to unsuccessful sequences. 

**14** 



##### 3.3.3. Average Closeness Ratio of Teams 



Figure 9. Average Closeness Values of Teams 

This section (Figure 9) provides an overview of the average closeness ratios of players between teams. Figure 9. highlights that players in higher-ranked teams tend to have higher closeness ratios than those in lower-ranked teams. However, it's important to note that many players in lower-ranked teams also perform above the team average. 

**15** 



3.3.4. Players' Closeness Ratio with Total Minutes Played 



Figure 10. Players Closeness Ratio in Unsuccessful vs Shot & Goal Sequences with Total Minutes Played. 

Figure 10 explains the Players' Closeness Ratio (eq.) in relation to Total Minutes played in the season. It reveals a weak or no correlation between players with high ratio values and higher total minutes played. Notably, Manchester City players exhibit the highest closeness values, indicating their higher involvement in shot & goal sequences than in unsuccessful sequences. Conversely, Liverpool's Salah and Arnold show greater performance in shot & goal sequences compared to unsuccessful sequences. 

**16** 



#### **3.4. On Ball Value (OBV)** 

This section consists of a discussion on the correlation between the OBV values of players in shot & goal sequences with players' closeness and betweenness ratio. The aim is to find out if centrality measures are aligned with the action performance of players signified by OBV. Figure 9. shows a moderate correlation with an R-square value of 0.34 between the OBV values of players in shot & goal sequences and the Player Betweenness ratio. Figure 10. shows a moderate correlation with an R-square value of 0.34 between the OBV values of players in shot & goal sequences and the Player Closeness ratio. The results of both the correlation figures signify players from all the teams. 



Figure 9. Average Ball value of players in shot & goal Sequences and Players Betweenness Ratio. 

**17** 





Figure 10. Average On Ball value of players in shot & goal Sequences and Players Betweenness Ratio. 

## **Discussion** 

The development of the possession sequence framework has allowed us to delve into how team strategies and playing styles can be understood through the analysis of players' positional roles and interactions within the team, moving beyond solely temporal and locational parameters of team play. In the following subsections, we present interpretations of the study results, focusing initially on Manchester City and Liverpool, while recognizing that similar interpretations apply to all teams in the league. The last part of the discussion focuses on the correlation result of betweenness and closeness ratio. In addition, presents the top 20 players in each ratio scale that resulted in this study. 

**18** 



#### **4.1. Possession Sequence Framework** 

The aim of developing a possession sequence framework is to find out how team players interact within shot & goal sequences and unsuccessful sequences. The team interaction between different categories helped in finding patterns in the roles of each player during several successful attacks. The results are in Figure 2. Clearly showed the high-rank teams have a higher number of shot & goal sequences. Furthermore, some teams have a higher number of shots & partially successful sequences but don’t have more goals, placing them in ranking below the teams with a greater number of goals. 

#### **4.2. Manchester City** 

The results of the Average Betweenness values shed light on Manchester City's playing style, particularly emphasizing the involvement of their back players as the first line of attack. Manchester City's players can be categorized into three groups: backs, midfielders, and forwards, each playing a distinctive role in the team's offensive strategies (see Figure 11). The availability of midfielders is evident through their high average betweenness values in shot & goal sequences, indicating their central role in the team's second line of attack. The team's playing style emphasizes frequent passing, equal player availability for advancing the attack, and a possession-based approach. The results of average closeness values (Figure 13) further support this interpretation, demonstrating that all Manchester City players are equally connected without relying on one or two key connections. However, the high closeness ratio values of players like De Bruyne suggest that, in the first line of attack, he plays a central role connecting midfielders and forward players. According to Grund, 2012 [21] and Balkundi and Harrison, 2006 [22] teams with much denser networks have a tendency to perform better and remain more viable. In the case of Manchester City, the high team betweenness values signify intact and dense plays. Furthermore, the Betweenness ratio (figure 13) shows 3 players with the highest betweenness values among the top 5 players from all teams. 

**19** 





Figure 11. Average Closeness Value and Betweenness value of Manchester City players in shot & goal sequences and unsuccessful sequences. 

#### **4.3. Liverpool** 

Similarly, the Average Betweenness values for Liverpool reveal the crucial involvement of their back players as the first line of attack. Liverpool's players can be grouped into two categories based on their average betweenness values: backs and midfielders initiating the attack with ball flow, and midfielders connecting with forward players who complete the attack (see Figure 12). Liverpool's midfielders play a bridging role between the back players and wingers by playing intact and high availability during passing the ball [21,22|, facilitating the attack, as indicated by their high average betweenness values in shot & goal sequences. The results of average closeness values for both back and forward players highlight their importance in connecting with other team members during attacks. Liverpool exhibits a mixed playing style, allowing for both possession-based and direct play, as indicated by the centrality measures of players. The high closeness value shows Liverpool's centrality playing style where certain positions connect the team or all the players aim to pass the ball to a certain position. However, the Liverpool centrality nature of play in back and forward and the right balance of betweenness in midfield players show evidence of tactical play. Notably, the high closeness ratio values of Salah and Arnold (Figure 14) suggest their pivotal roles within the team, particularly in shot & goal sequences. 

**20** 





Figure 12. Average Closeness Value and Betweenness value of Liverpool players in shot & goal sequences and unsuccessful sequences. 

#### **4.4. Average Closeness and Average Betweenness Ratio** 

One of the key contributions of this study is the introduction of two matrices: the Average Betweenness ratio and the Closeness ratio. These matrices exhibit a moderate correlation (Rsquared value of 0.34) with the OBV method, which quantifies players' actions. Figure 13 presents the top 20 players with the highest betweenness ratio values, indicating their significant involvement in ball flow during shot & goal sequences compared to unsuccessful sequences. Notably, players from Manchester City, Chelsea, and Arsenal dominate this list, highlighting their teams' possession-based playing styles. Manchester City players excel in direct connectivity. Figure 14 also showcases the top 20 players with the highest closeness ratio values, signifying their importance as key connections within their teams. Players like Salah and Arnold exhibit high closeness ratio values, indicating their significance within their teams and their active involvement in shot & goal sequences compared to unsuccessful sequences. 

Together, these three matrices provide valuable insights for coaches and team management to understand not only key players within their teams but also their team strategies and the contributions of high-performing players. While these matrices offer a comprehensive view of player positions and their roles, it is essential to acknowledge their limitations, such as the inability to account for situational choices, positional role rotation, and other external factors. Nevertheless, this study enhances our understanding of player positional roles and their impact on team success beyond temporal and locational parameters. 

**21** 





Figure 13. Top 20 players with Highest Betweenness Ratio values 

**22** 





Figure 14. Top 20 players with Highest Closeness Ratio values 

## **Conclusion** 

In this study, we embarked on a comprehensive exploration of soccer team strategies and playing styles by delving into players' positional roles and interactions within the team. Our approach moved beyond the traditional focus on temporal and locational parameters to gain a more nuanced understanding of how teams operate on the field. The study employed a novel possession sequence framework to categorize possession sequences into distinct groups, shedding light on the intricacies of team attacks, both successful and unsuccessful. 

Our findings have illuminated the unique playing styles of two prominent teams, Manchester City and Liverpool. Manchester City's approach is characterized by a multi-layered offensive 

**23** 



strategy, with back players serving as the initial line of attack, followed by the pivotal involvement of midfielders in the second line. This approach emphasizes possession-based play, frequent passing, and equal player availability, resulting in a well-connected team. The absence of dominant connections highlights the collective responsibility for initiating attacks, although players like De Bruyne exhibit key connections in the first line of attack. 

Conversely, Liverpool employs a diverse playing style that combines possession-based gameplay with direct attacks. Back players serve as the first line of attack, with midfielders bridging the gap between the backs and forward players who execute the attack. Players like Salah and Arnold play pivotal roles, evident from their high closeness ratio values, indicating their importance in connecting with other team members during attacks. 

The introduction of two matrices, the Average Betweenness ratio and the Closeness ratio, has provided a quantitative assessment of players' contributions to their teams. These matrices have shown a moderate correlation with the established OBV method, offering coaches and team management a valuable tool to understand key players and team strategies. 

Despite the comprehensive insights gained, it is essential to acknowledge the study's limitations. Factors such as the quality of opponents, situational choices, positional role rotations, and external influences like injuries and coaching decisions are not accounted for in the analysis. This limitation highlights the need for more detailed contextual data to enrich our understanding of team dynamics. 

#### **5.2. Critical Limitations and Future Work** 

1. Opponent Quality: The study does not account for variations in opponent quality, which can significantly impact team strategies. Future research should incorporate opponent strength as a variable to provide a more nuanced analysis. 

2. Dynamic Role Changes: Soccer players often adapt their positional roles based on game situations. A more dynamic analysis that captures these role changes during a match could offer deeper insights into team strategies. 

**24** 



3. External Influences: Factors such as injuries, coach influence, and player psychology are external to the scope of this study but can profoundly affect team dynamics. Future research should aim to integrate these external variables into the analysis. 

4. Contextual Data: Access to richer contextual data, including player decision-making and situational awareness, would enhance our understanding of team interactions and playing styles. 

5. Longitudinal Studies: Conducting longitudinal studies over multiple seasons can reveal how team strategies evolve over time and adapt to changing circumstances. 

In conclusion, this study has extended our understanding of soccer team dynamics by emphasizing the significance of players' roles and interactions in shaping team strategies. The possession sequence framework, combined with centrality measures and the OBV method, provides a holistic view of player performance and its impact on team success. Coaches and team managers can use these insights to refine their strategies, identify key players, and enhance overall team performance. Nevertheless, future research endeavors should address the critical limitations outlined here to further advance our knowledge of soccer team dynamics. 

#### **5.3. Acknowledgements** 

With this work, we wanted to extend our gratitude to the Technical University of Munich, Germany, Chair of Sports Performance Analysis and Sport Informatics, especially to Prof. Martin Lames and Dr. Daniel Link for guiding and assisting us in developing the necessary skills to accomplish the successful completion of this project. 

**25** 



## **References** 

[1] Hewitt, A.; Greenham, G., Norton, K. Game style in Soccer. What is it and can we quantify it? Int. J. Performance Anal. Sport 2016, 16, 355-372 

[2] Mackenzie R, Cushion C. Performance analysis in football: a critical review and implications for future research. J Sports Sci. 2013;31(6):639-76. doi: 10.1080/02640414.2012.746720. Epub 2012 Dec 19. PMID: 23249092. 

[3] Sarmento H., Clemente F. M., Araújo D., Davids K., McRobert A., Figueiredo A. (2018a). What performance analysts need to know about research trends in association football (2012– 2016): a systematic review. Sports 

Med. 48 799–836. 10.1007/s40279-017-0836-6 [4] Low, B., Coutinho, D., Gonçalves, B., et al. A Systematic Review of Collective Tactical Behaviours in Football Using Positional Data. Sports Med 50, 343–385 

(2020).  https://doi.org/10.1007/s40279-019-01194-7 Plakias, S.; 

[5] Moustakidis, S.; Kokkotis, C.; Tsatalas, T.; Papalexi, M.; Plakias, D.; Giakas, G.; Tsaopoulos, D. Identifying Soccer Teams’ Styles of Play: A Scoping and Critical Review. J. Funct. Morphol. Kinesiol. 2023, 8,39.  https://doi.org/10.3390/jfmk80200393 

[6] Hughes, Mike &amp; Hughes, Michael &amp; Behan, Hannah. (2007). The evolution of computerized notational analysis through the example of racket sports. International Journal of Sports Science and Engineering. 1. 1750-9823. 10.21797/ksme.2008.10.3.001. 

[7] Hughes M, Franks I. Analysis of passing sequences, shots and goals in soccer. J Sports Sci. 2005 May;23(5):509- 14. doi 10.1080/02640410410001716779. PMID: 16194998. 

[8] Sarmento, Hugo1; Figueiredo, António1; Lago-Peñas, Carlos2; Milanovic, Zoran3; Barbosa, António4; Tadeu, Pedro5; Bradley, Paul S.6. Influence of Tactical and Situational Variables on Offensive Sequences During Elite Football Matches. Journal of Strength and Conditioning Research 32(8):p 2331-2339, August 2018. | DOI: 10.1519/JSC.0000000000002147 

[9] Kempe, Matthias &amp; Memmert, Daniel &amp; Nopp, Stephan &amp; Vogelbein, Matrin. (2014). Possession vs. Direct Play: Evaluating Tactical Behavior in Elite Soccer. International Journal of Sport Science. 4. 35-41. 10.5923/s.sports.201401.05. 

[10] Fernandez-Navarro, J.; Fradua, L.; Zubillaga, A.; McRobert, A.P. Evaluating the effectiveness of styles of play in elite soccer. Int. J. Sport. Sci. Coach. 2019, 14, 514–527. 

[11] Matthias Kempe, Andreas Grunz &amp; Daniel Memmert (2014): Detecting tactical patterns in basketball: Comparison of merge self-organizing maps and dynamically controlled neural networks, European Journal of Sport Science, DOI: 10.1080/17461391.2014.933882. 

**26** 



[12] Pena, J.L., Touchette, H.: A network theory analysis of football strategies. (2012).arXiv preprint arXiv:1206.6904. 

[13] Clemente, F.M., Couceiro, M.S., Martins, F.M.L., Mendes, R.S.: Using network metrics in soccer: a macro-analysis. J. Hum. Kinet. 45(1), 123–134 (2015) 

[14] Clemente, F.M., Martins, F.M.L., Mendes, R.S., et al.: Social Network Analysis Applied to Team Sports Analysis. Springer, New York (2016). 

[15] Mclean, S., Salmon, P.M., Gorman, A.D., Stevens, N.J., Solomon, C.: A social network analysis of the goal scoring passing networks of the 2016 European football championships. Hum. Mon. Sci. 57, 400–408 (2018). 

[16] Korte F, Link D, Groll J and Lames M (2019) Play-by-Play Network Analysis in Football. Front. Psychol. 10:1738. doi 10.3389/fpsyg.2019.01738. 

[17] Aranda R, González-Ródenas J, López-Bondia I, Aranda-Malavés R, Tudela-Desantes A, Anguera MT. &quot; REOFUT&quot; as an Observation Tool for Tactical Analysis on Offensive Performance in Soccer: Mixed Method Perspective. Front Psychol. 2019 Jun 28;10:1476. doi 10.3389/fpsyg.2019.01476. PMID: 31316433; PMCID: PMC6610999. 

[18] Clustering ball possession duration according to players’ role in football small-sided games Coutinho D, Goncalves B. Laakso T, Travassos B (2022) Clustering ball possession duration according to players’ role in football small-sided games. PLOS ONE 17(8): e0273460. 

[19] https://www.setzeus.com/public-blog-post/measuring-network-centrality. 

[20] Peña, Javier & Touchette, Hugo. (2012). A network theory analysis of football strategies. [21] Grund TU. Network structure and team performance: The case of English Premier League soccer teams. _Soc Networks._ 2012;34:682–690. 

[22] <mark>Balkundi P, Harrison D. Ties, leaders, and time in teams: strong inference about network structure’s effects on team viability and performance.</mark> _<mark>Acad Manage J.</mark>_ <mark>2006;49:49–68.</mark> 

## **Appendix** 

**27** 



#### **1.1. Closeness centrality measures** 

This section consists of Figure 1 which shows the Average closeness values of all teams in Shot & goal sequences and Unsuccessful sequences. Players' average closeness values in lower rank teams are much higher in unsuccessful sequences than in shot & goal sequences. Despite this, certain players are more involved in shot & goal sequences than unsuccessful sequences. For instance, Christian Erikson from Brentford, and Pascal Groß from Brighton are some of the players who were major connectors among team players in team score or attempt shots. 



Figure 1: Average Closeness values of Team players in Shot & goal sequences 

and  Unsuccessful sequences of all the teams. 

**28** 



#### **1.2. Betweenness centrality measures** 

This section consists of Figure 2 which shows the Average betweenness values of all teams in Shot & goal sequences and Unsuccessful sequences. Players' average betweenness values in rank teams are much higher in unsuccessful sequences than in shot & goal sequences. Despite this, certain players are more involved in shot & goal sequences than unsuccessful sequences. Furthermore, according to Penz [20] team players who have higher betweenness values show a balanced attack from all the players equally. We can see the difference in the players' average betweenness values is similar for teams with higher rank in comparison to lower rank teams showing the direct connectivity of the players was not equal among lower rank teams. For instance, Everton, and Leeds United players' average betweenness values have the bigger range as the players' positions are scattered in the plot Figure 2. 



Figure 2: Average Betweenness values of Team players above 35 percentiles in Shot & goal sequences and Unsuccessful sequences. 

**29** 


