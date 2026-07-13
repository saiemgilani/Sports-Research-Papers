<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2024/2024 - Match Phases in Practice - Unknown Authors.pdf -->



# **Match Phases in Practice** 

Edoardo Ghezzi<sup>1</sup> and Hadi Sotudeh<sup>2</sup> 

## **Introduction** 

Match phases are the primary means by which match time is indexed and divided into _valuable_ units for coaches. For each phase, coaches instruct their teams to deploy a set of customized principles and arrangements Pioli 2003, 724. Moreover, these indices can have various applications such as trawling through video footage in match analysis, fan engagement in media, and trend analysis for soccer governing bodies. Last but not least, football analysts have focused for a long time on counting events without phase-related context providing a blurry image of what happened on the pitch. This paper proposes a framework for match phase identification and its possible applications based on StatsBombʼs 360 data (event and partial tracking data), which is also publicly available online StatsBomb 2023. 

## **Related Work** 

While no gold standard is accepted worldwide in defining phases precisely and it is quite subjective, there are still commonalities among previous proposals documented in the literature, coaching textbooks, and match reports High Performance Team of FIFA 2023. To go from top to down, one can look only at offense and defense Garganta and Pinto 1994, 199. The next level is to expand it to 1attack 2defense and 3preparation (transition): where each team reorganizes its structure before moving into the first two phases, as documented in the England Football Association's training and coaching guide Wade 1967, 2,6. The transition phase can be divided into attack to defense and vice versa José Guilherme Oliveira 2012. Additionally, set-pieces are considered a separate phase by some coaches because a significant number of goals are scored from them The Coachesʼ Voice 2021. 

The major difference among these approaches is how the in and out-of-possession phases are segmented into smaller sub-phases based on references such as (attack, midfield, and defense) lines and block heights Sportlogiq 2020; Llana et al. 2020; Gregory et al. 2022; Llana et al. 2022or pitch tactical zones SFV 2017such as the first, middle, and last third Bangsbo and Peitersen 2000, 12; Boomstra 2022, 33, 43, which is also reflected in the training grounds Sumpter 2017, 296. 

> 1 FC Lugano 

> 2 ETH Zürich 

**1** 



## **Data** 

The results of this study are based on StatsBomb 360 and event datasets from the Swiss Super League 20222023 season) and the 2022 Men's World Cup (open data). To align StatsBomb's data with our requirements, the following two issues have been addressed: 

1. **Misclassified possession team** : when analyzing shot events, especially goals scored, we found that StatsBombʼs “possession_teamˮ designation was sometimes incorrect for our use case. Discrepancies arose when comparing the final match score with the goal attributed to the possession team that scored. To address this, we applied a rule: if the "possession_team" at the start of the next possession (triggered by a "From Kick Off" after a goal) was the same team that scored, we corrected the "possession_team". 

2. **Multiple events per timestamp** : we frequently encountered two or three events occurring at the same timestamp, such as in carry-dribble or ball receipt-duel-pass situations. This led to assigning the same phase to multiple events in the same moment. To avoid duplicates, we retained only one event per timestamp by establishing a priority list and keeping the highest-priority event. 

## **Phase Definitions** 

Game phases vary according to coaches, technical staff, and a club's football philosophy. Previous implementations often relied only on event data. For example, Harkins 2017 defined _sequences_ as consecutive on-ball events for one team, starting with a controlled action and ending with a defensive action, stoppage, or shot. Later, _possessions_ were considered multiple sequences for the same team. Decroos et al. 2017proposed a new phase when there's a pause of 10 seconds between events or a possession switch. Worville 2019; STATS LLC 2020further broke sequences into phases based on field location and preceding and following actions, with similar methods used by Seidenschwarz et al. 2020. 

Event data alone is insufficient for accurate match phase identification. Recent work has proposed using synchronized full tracking and event data Bauer, Anzer, and Shaw 2023, applying a trained Convolutional Neural Network CNNto labeled tracking visualizations. In contrast to their and other black-box proposals Juan Camilo Campos 2021; Singh 2020; Fassmeyer et al. 2021, we adopted an explainable approach similar to the one introduced by FIFA FIFA 2022a; High Performance Team of FIFA 2023; Parlak 2023. However, our approach is tailored to StatsBombʼs 360 data and developed in consultation with FC Luganoʼs coaching staff. Our proposal, detailed below, also provides a framework for other teams to implement their own phases: 

**2** 



For each<sup>3</sup> event in the processed data, we use its freeze-frame<sup>4</sup> to assign phases to both teams. The main phases<sup>5</sup> - in possession, out of possession, and set pieces - are further divided into sub-phases, as follows: 

### **<u>In possession</u>** 

If the “play_patternˮ in the event attribute is “From Counterˮ, the phase is identified as **Counterattack** . If the on-ball team is under **Counterpress**<sup>6</sup> , the phase is **Consolidate** . Otherwise, the phase is categorized as **Buildup** , **Progression** , or **Finishing** depending on whether the ball is in the first, second, or third of the pitch, respectively. 

### **<u>Out of possession</u>** 

If the on-ball team is in **Counterattack** , the team without the ball is in **Regroup** . The phase is **Counterpress** if tagged in Statsbombʼs event data **.** Otherwise: 

- If the without-the-ball team has at least four players in their attacking third, it is classified as a **High Block** . 

- Else if the without-the-ball team has at least six players in their first third of the field, it is **Low Press** if the event is under pressure and **Low Block** otherwise. 

- Else if the without-the-ball team has at least four players in their second third of the field, it is **Mid Press** if the event is under pressure and **Mid Block** otherwise. 

- In all other scenarios, it is labeled as **Unidentified** . 

### **<u>Set Piece</u>** 

We defined a set piece phase, either **Set Piece For** or **Set Piece Against** , depending on which team is taking it and for the first five frames with a “play_patternˮ of “From Cornerˮ, “From Free Kickˮ, or “From Thrown inˮ. After the fifth frame, the possession was classified as a normal open-play scenario, and each subsequent frame was labeled according to the rules described earlier. This adjustment was crucial for accurately evaluating more frames as open-play and reducing the number allocated to set piece categories. 

Figure 1 illustrates some examples of the our identified phases. 

> 3 After excluding events not directly related to on-ball actions such as 'Foul Won' and 'Player On'. 4 Any frame that is missing in the StatsBombʼs data is labeled as **MissingSB** . 5 To determine whether a team is in or out of possession, we focus on the team taking the action on the ball—referred to as the "on-ball team"—instead of relying on StatsBomb's definition. This approach is essential because phase assignment occurs independently in each frame. 

> 6 According to <u>StatsBomb's glossary, a counterpress event is defined as a pressing action</u> occurring within five seconds of an open play turnover. 

**3** 





<!-- Start of picture text -->
(a) (b) (c)<br><!-- End of picture text -->



Figure 1. Build-up for the blue team and unidentified for the red team in (a), progression for the blue team and mid press for the red team in (b), and finishing for the blue team and low press for the red team in (c). 

## **Unknown Phases** 

After the initial phase assignment for each frame, approximately 10.5% of frames remained unlabeled due to missing freeze-frames in StatsBomb's 360 data (we call them **missingSB** ). Additionally, around 5% were non-compliant with our pre-specified rules, leading to a total of 16% **unknown** phases. 

To address the **unknown** phases, we implemented the following rule: 

_If the time between two known consecutive phases is 3 seconds or less, label any in-between_ **_unidentified_** _phase or_ **_missingSB_** _frame to one of those known phases._ 

This method reduced the **unknown** phases from 16% to 12%, demonstrating its effectiveness. 

## **Comparison** 

Since phases of play are inherently subjective, conducting a formal validation is not meaningful in this context. However, we can demonstrate our results along with publicly available phases reported by FIFA for the 2022 Men's World Cup in their post-match reports FIFA 2022b). It is important to note that while our analysis is based on StatsBomb's 360 data, FIFA utilized in-stadium full optical tracking data and their FIFA Football Language FIFA 2022c) for event data. Figure 2 shows the percentage<sup>7</sup> of match time spent in each phase for a selected match, as reported by both our analysis and FIFA. 

7 FIFA reported the percentage of each sub-phase not over the entire match duration, but rather in relation to the time spent in and out of possession phases. This difference in reporting makes their findings non-comparable with ours. 

**4** 







<!-- Start of picture text -->
(b)<br><!-- End of picture text -->

Figure 2. Identified phases of play by FIFA in (a) and by our proposal in (b) for one match of the 2022 Men's World Cup. 

**5** 



## **Applications** 

Various applications have been proposed for match phases, such as player and team profiling STATS LLC 2020and contextualizing physical load metrics in sports science SciSports 2021. Based on our assigned phases, we explore three use cases: 1 opposition analysis, 2post-match reports, and 3ad-hoc queries. The value of these use cases is enhanced when integrated with appropriate video footage automatically. 

### **<u>Opposition Analysis</u>** 

Table 1 displays the average percentage of match time a team spent in each phase and sub-phase, including the percentage of pressing-related phases (see **Pressing** ) and the combined percentage of time spent in High Block and CounterPress (see **High Def** ). 

Table 1. Time spent by a team in each phase and sub-phase, with color coding: green for high values, red for low values, and yellow for intermediate values. 





Table 1 indicates that St. Gallen has the lowest percentage of Buildup phases while recording the highest percentage of Finishing phases. Their offensive mindset is evident in their out-of-possession phases, as they exhibit the highest percentage of High Block and the lowest percentage of Low Block/Press. 

Figure 3 illustrates the total time FC Lugano spent in each phase throughout the season, highlighting their strong preference for progression and mid-block phases. 

**6** 



Figure 3. Percentage of time FC Lugano spent in each sub-phase. 



Figure 4. Low Block & Build-up in losing vs winning scenarios. 

**7** 



However, Table 1 and Figure 3 lack context concerning the scoreline. Figure 4 addresses this by illustrating how a teamʼs play varies based on match status (losing vs. winning). For example, FC Winterthur adopts a low block when winning, while Young Boysʼ percentage of Low Block remains nearly unchanged in both scenarios. In contrast, Lugano and Sion increase their percentage of Buildup when winning! 

### **<u>Post-match reports</u>** 

Creating post-match reports that include the percentage of time spent in each phase is a valuable use case. Figure 5 illustrates this for both teams in a match, providing insights into their phase distribution throughout the game. 



Figure 5. Percentage of time each team spent in one specific match. 

**8** 



Figure 5 depicts Luganoʼs match against Servette on April 15, 2023. Lugano recorded the highest percentage of Buildup, while Servette was more active in offensive areas, achieving a higher percentage of Finishing. Defensively, Lugano maintained a higher percentage of Low Block, whereas Servette opted for a more intensive pressing strategy, reflected in their higher percentages of High Block and Counter Press. 

### **<u>Ad-hoc queries</u>** 

The coaching staff can ask several phase-related ad-hoc queries, such as: 

- In which match did FC Lugano achieve the highest percentage of Buildup? ○ Figure 6 provides the answer. 



<!-- Start of picture text -->
○ Figure 6 provides the answer.<br><!-- End of picture text -->

Figure 6. FC Luganoʼs match with the highest percentage of time spent in build-up. 

- In which match did FC Lugano's behavior deviate the most from their average time spent in each sub-phase across the season? 

   - To answer this question, we can use the Euclidean distance to calculate the difference between the average of phase percentages over the season and each individual match. Figure 7 illustrates how much Lugano's performance in each match deviated from their average and Figure 8 showcases the behavior in the match with the highest deviation. 

**9** 





<!-- Start of picture text -->
Figure 7. Difference between matches and the average match-phase behavior for FC<br>Lugano across the season.<br><!-- End of picture text -->

Figure 8. FC Luganoʼs match with the highest difference to the average behavior. 

**10** 



The list of these queries can become extensive when integrated automatically with video footage. For example, it could include requests to return all situations where FC Lugano remained in a low block followed by a counterattack, or instances where FC Lugano did not stay in a low block while their opponents were in the finishing phase! 

## **Conclusion** 

Match phases are segments of a game defined by coaches to analyze specific periods of play. In this work, we presented a framework developed in collaboration with FC Lugano's coaching staff to assist teams in utilizing StatsBomb's 360 data for identifying sub-phases. These sub-phases are buildup, progression, finishing, counterattack, and consolidate for the on-ball team and regroup and low/mid/high press or block for the team without the ball. In addition, set-pieces are divided into for and against categories. Using a frame-by-frame approach, we assigned phases to each team based on a set of rules involving the ball's location on the field, StatsBombʼs event data attributes, and the number of visible players and their locations from TV footage. Due to missing frames or insufficient visible players, 16% of the frames were initially labeled as unknown, but we reduced this to 12% by interpolating from surrounding frames. 

We then demonstrated three match phase applications: opposition analysis, post-match reports, and ad-hoc queries. Clearly, the number of these queries is endless, offering a foundation for coaching staff to explore various questions. The value of these applications is fully realized when automatically integrated with video footage. 

## **Acknowledgement** 

We would like to acknowledge the valuable input of the FC Lugano coaching staff and Scott Johnson from StatsBomb for their helpful and supportive comments, as well as the assistance of ChatGPT, an AI language model by OpenAI, for its role in refining the text for cohesion and conciseness. 

## **References** 

- Bangsbo, Jens, and Birger Peitersen. 2000. _Soccer Systems and Strategies_ . 1st ed. Human Kinetics. 

- Bauer, Pascal, Gabriel Anzer, and Laurie Shaw. 2023. “Putting Team Formations in Association Football into Context.ˮ _Journal of Sports Analytics_ 9 13959. https://doi.org/10.3233/JSA220620. 

- Boomstra, Tom. 2022. “Towards Automatically Classifying Football Formations for Video Analysis.ˮ Master Thesis, Utrecht University. 

   - https://studenttheses.uu.nl/handle/20.500.12932/41653. 

- Decroos, Tom, Jan Van Haaren, Vladimir Dzyuba, and Jesse Davis. 2017. “STARSSA Spatio-Temporal Action Rating System for Soccer.ˮ In _Machine Learning and Data Mining for Sports Analytics ECML/PKDD 2017 Workshop_ , 19711120. Springer. http://ceur-ws.org/Vol-1971. 

- Fassmeyer, Dennis, Gabriel Anzer, Pascal Bauer, and Ulf Brefeld. 2021. “Toward Automatically Labeling Situations in Soccer.ˮ _Frontiers in Sports and Active Living_ 

**11** 



   3. https://doi.org/10.3389/fspor.2021.725431. 

- FIFA, dir. 2022a. _Phases of Play_ . 

   - https://fifatrainingcentre.com/en/fwc2022/efi-metrics/efi-metric--phases-of-play. php. 

- ———. 2022b. “Post Match Summary Reports.ˮ FIFA Training Centre. 2022. https://fifatrainingcentre.com/en/fwc2022/post-match-summaries/post-match-su mmary-reports.php. 

- ———. 2022c. “The FIFA Football Language.ˮ FIFA Training Centre. 2022. https://fifatrainingcentre.com/en/game/performance-analysis/football-language-a nalysis/the-fifa-football-language.php. 

- Garganta, Júlio, and J. Pinto. 1994. “O ensino do futebol.ˮ _O Ensino Dos Jogos Desportivos_ , 95136. 

- Gregory, Sam, Sam Robertson, Robert Aughey, and Grant Duthie. 2022. “The Influence of Tactical and Match Context on Player Movement in Football.ˮ _Journal of Sports Sciences_ . https://doi.org/10.1080/02640414.2022.2046938. 

- Harkins, Johannes. 2017. “Introducing a Possessions Framework.ˮ Stats Perform. 2017. https://statsperform.com/resource/introducing-a-possessions-framework. 

- High Performance Team of FIFA. 2023. “Enhanced Football Intelligence Explanation.ˮ FIFA. https://fifatrainingcentre.com/media/native/tournaments/womens-world-cup/2023 /FIFA%20Enhanced%20Football%20Intelligence%20EFI%20Explainations_EN%2 0v1.1.pdf. 

- José Guilherme Oliveira. 2012. “Periodização Tática.ˮ Presented at the Football Coach Course Level A Lecture, Brazil. 

   - https://pt.slideshare.net/proffernandofarias/periodizao-ttica-jos-guilherme-oliveira -cbf. 

- Juan Camilo Campos, dir. 2021. _StatsBomb Conference: Phases of the Play Using Graph Convolutional Networks_ . https://youtube.com/watch?v=r8fCY71TVDc. 

- Llana, Sergio, Borja Burriel, Pau Madrero, and Javier Fernández. 2022. “Is It Worth the Effort? Understanding and Contextualizing Physical Metrics in Soccer.ˮ https://doi.org/10.48550/arXiv.2204.02313. 

- Llana, Sergio, Pau Madrero, Javier Fernández, and FC Barcelona. 2020. “The Right Place at the Right Time: Advanced off-Ball Metrics for Exploiting an Opponentʼs Spatial Weaknesses in Soccer.ˮ In _Proceedings of the MIT Sloan Sports Analytics Conference_ , 16. Boston, Massachusetts. 

   - https://global-uploads.webflow.com/5f1af76ed86d6771ad48324b/5f6a69841d1ac9 9fa3a71a41_Llana_The-right-place-at-the-right-time.pdf. 

- Parlak, Dogan. 2023. “An Open-Source Implementation of FIFAʼs Enhanced Football Intelligence.ˮ Master Thesis, University of Zurich. 

   - https://www.merlin.uzh.ch/publication/show/24098. 

- Pioli, Stefano. 2003. “Le catene di gioco laterali in un 442.ˮ UEFA Pro License Thesis, Italian Football Federation. 

   - https://figc.it/it/tecnici/aula-multimediale/documenti/le-catene-di-gioco-laterali-inun-442. 

- SciSports. 2021. “Game Phases.ˮ SciSports. 2021. 

   - https://scisports.com/added-game-phases-and-insights-bring-performance-analy sis-to-life. 

- Seidenschwarz, Philipp, Martin Rumo, Lukas Probst, and Heiko Schuldt. 2020. “A Flexible Approach to Football Analytics: Assessment, Modeling and Implementation.ˮ In 

**12** 



_Proceedings of the 12th International Symposium on Computer Science in Sport IACSS 2019_ , edited by Martin Lames, Alexander Danilov, Egor Timme, and Yuri Vassilevski, 10281927. Springer. https://doi.org/10.1007/9783030350482_3. 

- SFV. 2017. “Game Philosophy of the Swiss Football Association.ˮ 2017. 

   - https://football.ch//sfv/spiel-und-ausbildungsphilosophie/unsere-spielphilosophie/ die-spielphasen/schluesselfolien.aspx. 

- Singh, Karun, dir. 2020. _Opta Pro Forum - Learning to Watch Football: Self-Supervised Representations for Tracking Data_ . https://youtube.com/watch?v=H1iho17lnoI. 

- Sportlogiq, dir. 2020. _Sportlogiq Phases of Play_ . 

   - https://youtube.com/watch?v=gRjZ2wyXp18. 

- STATS LLC. 2020. “Stats Perform Playing Styles - an Introduction.ˮ Stats Perform. 2020. https://statsperform.com/resource/stats-playing-styles-introduction. 

- StatsBomb. 2023. “Open Data.ˮ StatsBomb. 

   - https://github.com/statsbomb/open-data/tree/master/doc. 

- Sumpter, David. 2017. _Soccermatics: Mathematical Adventures in the Beautiful Game_ . Bloomsbury Sigma. 

- The Coachesʼ Voice, dir. 2021. _Rangnickʼs Coaching Philosophy, Tactics and Data-Driven Football Strategy_ . https://youtube.com/watch?v=mZskzUKsNwU. 

- Wade, Allen. 1967. _The F.A. Guide to Training and Coaching_ . An official publication of the Football Association. 

- Worville, Tom. 2019. “Phases of Play - an Introduction.ˮ Stats Perform. 2019. https://statsperform.com/resource/phases-of-play-an-introduction. 

**13** 


