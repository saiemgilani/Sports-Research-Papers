<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2013/2013 - The Dwight Effect A New Ensemble of Interior Defense Analytics for the NBA - Unknown Authors.pdf -->



# **The Dwight Effect: A New Ensemble of Interior Defense Analytics for the NBA** 

Kirk Goldsberry<sup>1</sup> and Eric Weiss<sup>2</sup> 1Harvard University, Cambridge, MA, USA, 02138 kgoldsberry@fas.harvard.edu 

2Sports Aptitude, LLC eweiss@sportsaptitude.com 

## **Abstract** 

Basketball is a dualistic sport: all players compete on both offense and defense, and the core strategies of basketball revolve around scoring points on offense and preventing points on defense. However, conventional basketball statistics emphasize offensive performance much more than defensive performance. In the basketball analytics community, we do not have enough metrics and analytical frameworks to effectively characterize defensive play. However, although measuring defense has traditionally been difficult, new player tracking data are presenting new opportunities to understand defensive basketball. This paper introduces new spatial and visual analytics capable of assessing and characterizing the nature of interior defense in the NBA. We present two case studies that each focus on a different component of defensive play. Our results suggest that the integration of spatial approaches and player tracking data promise to improve the status quo of defensive analytics but also reveal some important challenges associated with evaluating defense. 

## **Introduction** 

Basketball is a dualistic sport. Players compete on both offense and defense, and the two core objectives of all basketball stratagems are scoring points and preventing points. Although it is self-evident that the final score of every basketball game depends equally on these two facets, this basic tenet is not properly represented in contemporary basketball statistics. A quick reading of even the most “advanced” basketball statistics would suggest that basketball success hinges more on offensive factors and less on defensive factors. Few of the sport’s most common metrics quantify key defensive aspects. Basketball’s most common statistics are related to events that are most obviously attributable to one individual action at one moment; defensive prowess in basketball fails to meet this basic criterion. 

Contemporary basketball expertise is significantly hindered by the inability to properly assess defensive play; current evaluations of a player or team’s defensive tendencies are constrained by a lack of proper reasoning artifacts. Most defensive analytics remain guided by the simple tallying of disparate event types including “steals,” “blocks,” and “defensive rebounds,” which does little to characterize either the nature or the effectiveness of defensive performance. Effective defensive play requires a cohesive assembly of structured actions converging upon a simple objective: keep your opponent from scoring points. With this in mind, as the NBA enters its “big data” era and new kinds of basketball analytics emerge, advancing defensive understanding presents one of our biggest challenges. 

This paper explores defensive evaluations in the NBA and examines emerging opportunities and challenges associated with measuring defense using optical tracking data. The paper presents a new methodology designed to characterize the interior defensive effectiveness of NBA “big men”. The core objectives of this paper are 1) to improve the characterization and understanding of interior defense in the NBA, and 2) expose key challenges associated with measuring defense as new forms of performance data emerge. We present case studies that 1) use spatial analyses to extract new defensive metrics from optically tracked game data (SportVu data) and 2) use visual analytics to present results. 

The paper also introduces a new ensemble of spatially minded metrics that present a novel and simple means to characterize basketball performance. One key and recurring limitation of many basketball statistics is their relatively limited explanatory abilities. For example, even the most effective “advanced” metrics like “defensive rating” (points allowed per 100 possessions) may provide valuable insight into overall performance ability, but simultaneously they often fail to offer any additional explanatory insight as to _why_ a performance may be good or bad. We introduce “spatial splits”  - a concept inspired by baseball’s “triple-slash” lines - as a means to address this shortcoming; in tandem with other metrics, we contend spatial splits provide additional insight into the nature of how players and teams are performing within court space, therein providing analysts with a more powerful set of reasoning artifacts. 

The paper contains three main sections: a brief background section is followed by an explanation of our 1 2013 Research Paper Competition Presented by: 







methodology, which in turn is followed by a discussion of our results and conclusions. We also append thorough listings of detailed results at the end of the paper. 

## **Background** 



_Figure 1: Overall shooting efficiencies in the NBA. The only shots that go in over half the time occur close to the basket. For this reason, this relatively small area remains the most important tactical space - and the most vigorously defended space in the NBA. Graphic by Kirk Goldsberry._ 

NBA shooters only make about 39% of their field goals from everywhere outside of 7 feet. The only shots that go in more than half the time occur very close to the rim. Despite the rapidly growing importance of the 3-point shot, good shots close to the basket remain the best shots on the floor; not only do they result in points at a higher rate, when missed they have a much greater chance of being rebounded by the shooting team. Over 70% of shots near the rim either result in points, a shooting foul or an offensive rebound. Good shots near the rim are clearly advantageous. For this reason, the league shoots over 1/3rd of its shots from the tiny portion of the court close to the basket, and defenders protect this area with more vigor than any other real estate on the court. Although the vitality of this strategic space is self-evident, few if any contemporary analytics effectively characterize the ability of players or teams to defend basketball’s most sacred real estate.  The problem is obvious: interior defense is critical to basketball success, but our ability to measure or characterize players’ interior defensive abilities remains undeveloped. Consider these two basic questions: 

### 1) Who is the best interior defender in the NBA? 

### 2) What metrics would you use to answer that question? 

The NBA’s most prominent defensive metrics can be misleading, but this is not a problem unique to basketball. Until very recently, the dominant conventional defensive metrics in baseball were “errors” and “fielding percentage,” which do not frequently correlate with a player’s true defensive value. In the NFL, the best cornerbacks never lead the league in any conventional stats because quarterbacks are too afraid to even throw in their direction; they don’t even get chances to defend passes. Basketball exhibits similar issues; our conventional defensive metrics fail to accurately reveal the NBA’s most dominant defenders. 





2013 Research Paper Competition Presented by: 

2 



Last season, Oklahoma City’s Serge Ibaka led the NBA in blocks by averaging an incredible 6.46 blocks per 48 minutes, but what does that really reveal? Does that mean he is an “elite defender,” or even the “best shot blocker” in the NBA? Shot blocks are relatively infrequent events that have an ambiguous relationship with defensive effectiveness. In many cases, for a shot block event to occur a shooter has to believe that his shot will not be blocked. In other words, the shot blocker has to “come out of nowhere” or has to somehow deceive the shooter; at the point of the shot’s release the shooter believes the path is clear, but that turns out not to be the case. 

Dwight Howard, who is commonly referred to as the NBA’s “most dominant” interior defender, only averaged 2.69 blocks per 48 minutes, almost 4 fewer than Ibaka; however, it could be argued that Howard’s mere presence “blocks” shots before they happen. The presence of a truly dominant interior force can augment the spatial behavior of the offense in the same way that a dominant cornerback changes the behavior of a quarterback. While it is easy to tally up things like blocks, rebounds, and steals, it’s much harder to measure the kind of disruption or the strategic augmentations that dominant interior defenders like Dwight Howard create. We define “The Dwight Effect” as the ability of an interior defender to reduce the efficiency of an opponent’s shooting behavior. 

Perhaps the most logical method to evaluate this disruption is to measure the spatial shooting patterns and efficiencies of NBA teams in the presence of different interior defenders. Using emerging data sets from SportVu, it’s now possible – although still not easy – to look at defense in new ways. In the case of interior defense, we can evaluate how NBA offenses behave differently depending on which NBA “bigs” are on the floor; furthermore, we can evaluate how offenses behave when a given NBA interior defender is “protecting the rim” or near a shot event. 

## **Methodology, Data, and Case Studies** 

We conducted two separate case studies of interior defense in the NBA. Using player tracking data provided by STATS (SportVu) we evaluated player positions, shooting tendencies, and shot outcomes for over 75,000 NBA shots during the 2011-2012 and 2012-2013 seasons. We evaluated the spatial structures and efficiencies of NBA shooting in the presence of the 52 NBA interior defenders who faced at least 500 shot attempts during the study period. Each case study monitors a different aspect of defensive effectiveness and introduces new metrics. 

We introduce “spatial splits” as a means to communicate our results. Since NBA scoring efficiency is clearly dependent on spatial factors, we contend spatial splits offer a mechanism to detect, understand, and communicate key aspects of NBA scoring efficiency. Presented in a manner meant to mimic baseball’s “slash line” or “triple-slash line” these sequences of three numbers not only offer a basic quantification of a player or opponent’s shooting, they also present an inherent explanatory characterization as well. Figure 2 depicts the 3 zones represented in the spatial splits. 



_Figure 2: The 3 zones associated with spatial splits: close-range in green, mid-range in blue, and 3-point range in red. Splitting offensive performance data using these zones can help characterize the nature of scoring behaviors in the NBA._ 





2013 Research Paper Competition Presented by: 

3 



We introduce two kinds of spatial splits: frequency splits and efficiency splits. Both reflect percentage values in the following sequence: Close-range value / Mid-range value / 3-point range value. Frequency splits focus on shot distribution; each number corresponds to the percentage of shots that come from the corresponding zone. The three numbers in the frequency splits should sum to 100 (barring any rounding errors). Efficiency splits characterize how well a player or teams shoots from each zone; each value represents the field goal percentage in the corresponding zone.  As an example, consider the spatial splits of the NBA as a whole, and two NBA players from the previous two NBA seasons: Kevin Durant and Josh Smith. 

NBA League Average: Frequency 35/41/24   Efficiency 53/39/36 Kevin Durant: Frequency 27/46/27   Efficiency 65/44/37 Josh Smith: Frequency 45/43/12   Efficiency 61/37/30 

The above examples illustrate the ability of spatial splits to quickly summarize key differences in scoring tendencies. These splits quickly communicate a few facts: 1) In terms of shot distribution, Kevin Durant shot 27% of his shots close to the basket, 46% of his shots in the mid-range, and 27% of his shots from three-point range, 2) In terms of shot efficiency, Durant shot 65% close to the basket, 44% in the mid-range, and 37% from beyond the arc – above league averages in each zone, while Smith is only above average close to the basket. They also enable comparison across players. In this case we can quickly note that Durant is less active close to the basket than Smith, they are both active in the midrange, Durant is more active beyond the arc, and Durant is a more efficient shooter in every area. We contend that this contribution is a valuable new way to characterize NBA scoring behaviors. 

Although spatial splits present an effective way to characterize the nature of an individual player’s offensive tendencies and abilities, in this paper we use them to evaluate defense. More specifically, within the context of spatial splits, effective interior defense should manifest in two ways. The most obvious is perhaps reduced shooting _efficiencies_ close to the basket. The second is less apparent but perhaps more important: reduced shooting _frequencies_ close to the basket, and increased frequency in the mid-range and three-point areas. Taken together, reduced closerange efficiency and reduced close-range frequency translate to fewer easy shots, fewer points, and fewer offensive rebounding opportunities for the offense. 

### Case Study 1: The Basket Proximity Condition 

The objective of the first case study was to examine the ability of interior defenders to “protect the basket.” This case study considered shot attempts that occurred when there was an interior defender within 5 feet of the basket and was designed to measure two aspects of point prevention: the ability to prevent shots near the basket, and the ability to reduce the shooting efficiency of opponents near the basket. We evaluated shooting patterns using spatial splits. As a means to characterize the opponents’ shooting tendencies, we calculated both the frequency and efficiency of shooting in each zone, but placed primary emphasis on close range shooting. 

### Case Study 2: The Shot Proximity Condition 

The second case study evaluates the ability of interior defenders to defend shots in their immediate proximity. This study has two objectives: to determine how frequently an interior defender is proximate to a shot attempt, and to determine how effective an interior defender is when they are proximate to a shot attempt. In this case we place a reduced emphasis on shot locations and instead evaluate two other aspects of defending; each aspect is evaluated via a new metric: 

A) Shots Defended: the relative frequencies in which the defender finds himself within 1, 3, or 5 feet of shot attempts. 

B) Proximal FG%: the relative efficiencies of shooters in the proximity of the defender. 

## **Results** 

### Case Study 1: Basket Proximity 

Overall more than 1/3<sup>rd</sup> of shots in our superset of 76,000 shots occurred with an interior defender within 5 feet of the basket. We assert that “dominant” interior defense can manifest in two ways: reducing the shooting efficiency of opponents, and also reducing the shooting frequency of opponents. In terms of reducing efficiency, we found that Indiana’s Roy Hibbert and Milwaukee’s Larry Sanders (Figure 3) were by far the most effective. We evaluated this by measuring the field goal percentage of close range shots when a qualifying interior defender was within 5 feet of the basket. Overall, NBA shooters make 49.7% of their field goal attempts when qualifying interior defender is within 5 feet of the basket; however, this number drops to 38% when either Hibbert or Sanders are within 5 feet. In contrast, we found that Phoenix’s Luis Scola and Golden State’s David Lee (Figure 3) were the worst defenders in these situations; opponents made 63% of their close-range field goals when Scola was within 5 feet of the basket. See Appendices 1 and 1A for a full list of qualifying defenders. 





2013 Research Paper Competition Presented by: 

4 





_Figure 3: Opponents' field goal percentages vary widely depending on which interior defender is close to the basket. Milwaukee's Larry Sanders is one of the most effective interior defenders in the league; opponents struggle to score when he is near the basket. This is not the case with Golden State’s David Lee; when he is close to the basket, opponents score at very high efficiencies._ 

We also contend that dominant interior defenders often deter shots from even happening. Many NBA players will be reluctant to “challenge” a dominant interior player or be more likely to “settle” for a jump shot further from the basket. We evaluated this effect by examining the percentage of field goal attempts that occur near the basket when a qualifying interior defender is within 5 feet of the rim. We found that the most deterrent interior defender in this sense was Dwight Howard. Overall, when a qualifying defender is within 5 feet of the basket, the NBA shoots 57.2% of its attempts close to the basket; however, when Dwight Howard was the interior defender this number dropped to 48.2% (Appendix 1A). This is what we call the “Dwight Effect” – the most effective way to defend close range shots is to prevent them from even happening. Although Howard does not lead the league in blocks, he does lead the league in “invisible blocks,” which may prove to be markedly more significant. When Howard is protecting the basket, opponents shoot many fewer close range shots than average, and settle for many more midrange shots, which are the least productive shots in the NBA. Furthermore, out of centers who have faced at least 100 total shots in the basket proximity study, Serge Ibaka ranked last; when he is within 5 feet of the basket, opponents shot 74% of their shots in the close range area. This means that Ibaka is likely to be around any shot near the basket and suggests that while Ibaka leads the NBA in blocks per game, part of the reason is that he has many more “potential blocks” than almost any other defender. Full results for Case Study 1 are presented in Appendix 1. We also discuss the challenges and limitations associated with this study in the Discussion section. 

Case Study 2: Shot Proximity 

Overall 27.8% of NBA shots occur within 5 feet of a qualifying interior defender. We evaluated 21,042 shots that met this criterion and examined two separate aspects of defensive tendencies: Shots Defended, and Proximal FG%. The results for each are presented below. 

A) Shots Defended: the relative frequencies in which the defender is located within 1, 3, or 5 feet of shot attempts. We calculated these frequencies for 93 qualifying defenders that faced at least 200 shots while playing defense. Tyler Hansbrough had the lowest frequency of being close to shots; he was within 5 feet of shots only 20.7% of the time. Only 3 defenders were within 5 feet of shots more than 35% of the time: Josh Harrellson, Kosta Koufos, and Jordan Hill. Serge Ibaka was fourth at 34.5%. The full set of results is available in Appendix 2. 

B) Proximal FG%: the relative efficiencies of shooters in the proximity of the defender. Overall, when there is a qualifying interior defender within 5 feet of a shot attempt, the NBA shoots 45.6% from the field; however this value varies considerably depending on which defender that is. The most effective proximate defender in our study was Larry Sanders; opponents shot only 34.9% when he was within 5 feet of their shot. Conversely, Anderson Varejao was found to be the least effective proximate defenders with a proximal FG% value of 54.2%. Table 1 summarizes the best and worst players according to proximal FG%, but a complete list of proximal FG% values can be found in Appendix 2. 





2013 Research Paper Competition Presented by: 

5 



|Top5<br>Proximal FG%<br>Bottom 5<br>Proximal FG%|
|---|
|1. Larry Sanders<br>34.9%<br>48. Kevin Love<br>52.1%|
|2. Andrea Bargnani<br>35.2%<br>49. Jonas Valanciunas<br>52.8%|
|3. Kendrick Perkins<br>37.3%<br>50. David Lee<br>53.0%|
|4. Elton Brand<br>38.0%<br>51. Jordan Hill<br>53.9%|
|5. Roy Hibbert<br>38.7%<br>52. Anderson Varejao<br>54.2%|
|_Table 1: The top and bottom 5 interior defenders according to proximal FG%, which is defined as the opponent’s FG% when the_<br>_qualifying defender is within 5 feet of the shot attempt._|



## **Discussion and Limitations** 

In a league that is both teeming with new data sources as well as desperate for better diagnostics, the application of spatial and visual approaches to optical tracking data represents a vital new corridor to new kinds of basketball expertise. Furthermore, perhaps no aspect of basketball is as important and as under-studied as defense. Our case studies were designed to show how new data and emerging approaches can be integrated to help analysts better characterize defense in the NBA. While we contend it is clear that these studies effectively demonstrated the potential of spatial/visual analytics to expose new insights about defense, we also assert that the paper’s methods only represent a small first step in a multi-step progression towards the core objective of better defensive analytics. 

Evaluating defense in the NBA is very difficult. Despite the new analytical opportunities introduced by player tracking data, our current ability to extract meaningful defensive analytics from these data remains undeveloped. This fundamental notion manifests in multiple ways within our evaluation of interior defense. Perhaps the biggest limitation in our study involves the sample; player-tracking data is only being collected in a subset of NBA arenas. More specifically, as of January 2013, only 15 NBA arenas are equipped with SportVu systems. This obviously biases the sample and is likely to introduce error into our results.  But our goal was not to generate the “be-all end-all” ensemble of defensive analytics; instead our goal was to demonstrate the viability of spatial approaches as they relate to making sense of defensive performance data. 

Another key limitation is the lack of context associated with the data. Optical tracking data enables us to track player movements in fascinating new ways, but it also reduces players to geometric primitives that frequently obscure the nature of an action. In reality we know players are not coordinate pairs, they are athletic human beings. When we reduce Serge Ibaka to a simple x,y pair, we lose key information. In reality, Serge Ibaka is a 3-dimensional creature with arms that stretch and legs that jump. While this is painfully obvious, even our most sophisticated player tracking systems model NBA players as discrete locations on a plane. This dramatic abstraction of reality introduces infinite issues relating to uncertainty and error. Although we contend there is a vast amount of value in optical tracking data, more research is needed to evaluate uncertainty and reliability in these kinds of investigations. 

## **Conclusion** 

This paper has sought two accomplish two main objectives: 1) demonstrate that the combination of spatial analyses, visual analytics, and optical tracking data presents a potent new mechanism to understand defensive effectiveness in the NBA, and 2) expose important challenges associated with measuring defensive performances in the NBA. Despite some relevant limitations, we contend that our results suggest that interior defensive abilities vary considerably across the league; simply stated, some players are more effective interior defenders than others. In terms of affecting shooting, we evaluated interior defense in 2 separate case studies.  Each study focused on important aspects of interior defense, and as a result each study both answers and provokes important questions about defensive analytics. Although we acknowledge that neither study clearly identifies the best and worst interior defenders, we also contend that 1) each study effectively reveals important characteristics of good defensive play, and 2) advancing defensive analytics will be an long-term iterative process that will require several investigations and multiple new approaches. Lastly, due to his outstanding performance in both case studies, we conclude by suggesting Larry Sanders is the best interior defender in the NBA. 

## **Acknowledgements** 

The authors would like to acknowledge the help and support of Brian Kopp, Ryan Warkins, Ryan Shea, and David Sherman of STATS. Thank you! 





2013 Research Paper Competition Presented by: 

6 



## **Appendix 1: Expanded Results from Case Study 1: Basket Proximity Shots faced when defender was within 5 feet of basket.** 

|||Shots<br>|% Close<br>|% Mid-|% 3-<br>point|**Close**<br>|Mid<br>|3-point<br>|
|---|---|---|---|---|---|---|---|---|
|Rank|Defender|Faced|Range|range|range|**FG%**|FG%|FG%|
|1|Roy Hibbert|419|54.4|29.6|14.8|38.2|37.9|30.7|
|**2**|<br>**Larry Sanders**|**622**|**61.9**|**22.2**|**15.4**|**38.4**|**32.6**|**30.2**|
|3|<br>Elton Brand|198|57.1|26.8|14.1|39.8|32.1|46.4|
|**4**|**Serge Ibaka**|**104**|**74.0**|**16.3**|**9.6**|**41.6**|**35.3**|**10.0**|
|5|LaMarcus Aldridge|221|58.8|24.9|14.5|43.9|38.2|46.9|
|6|<br>Jermaine O'Neal|392|56.9|28.1|14.0|44.0|32.7|32.7|
|7|<br>Kosta Koufos|200|60.0|23.5|15.5|45.0|31.9|25.8|
|8|Kendrick Perkins|745|59.3|24.3|16.1|45.5|37.0|36.7|
|9|Joakim Noah|334|56.6|27.8|14.4|45.5|44.1|31.3|
|**10**|**Dwight Howard**|**409**|**48.2**|**32.0**|**19.1**|**45.7**|**38.2**|**43.6**|
|11|<br>JaVale McGee|401|53.6|30.2|16.0|46.1|40.5|40.6|
|12|<br>Amir Johnson|207|56.5|25.1|17.4|46.2|44.2|41.7|
|13|<br>Ekpe Udoh|468|65.2|20.1|14.1|46.2|42.6|34.9|
|14|<br>Andris Biedrins|317|49.8|28.7|20.5|46.8|42.9|36.9|
|15|Tim Duncan|930|57.3|28.6|13.7|47.1|41.4|46.5|
|16|Emeka Okafor|310|52.3|24.5|22.6|47.5|43.4|32.9|
|17|Jeremy Tyler|177|60.5|29.4|10.2|47.7|38.5|50.0|
|18|<br>Nick Collison|273|52.0|27.8|18.7|47.9|35.5|37.3|
|19|Kevin Seraphin|475|55.6|28.4|14.9|48.1|40.7|35.2|
|20|<br>DeMarcus Cousins|279|48.4|29.7|20.1|48.2|38.6|44.6|
|21|Marcus Camby|204|57.8|28.4|13.7|48.3|41.4|39.3|
|22|Kevin Garnett|772|54.4|28.6|16.2|48.3|37.6|41.6|
|23|Tiago Splitter|687|58.8|27.2|13.5|48.5|38.0|35.5|
|24|<br>Samuel Dalembert|777|56.4|30.4|12.9|48.6|38.6|41.0|
|25|Nene Hilario|212|56.1|25.9|17.9|48.7|36.4|29.0|
|26|Aaron Gray|275|54.5|29.5|15.6|49.3|39.5|44.2|
|27|Ed Davis|391|61.6|23.3|14.8|49.4|40.7|34.5|
|28|Nazr Mohammed|260|51.9|28.1|18.8|49.6|41.1|28.6|
|29|Chris Bosh|263|55.9|23.2|19.8|49.7|32.8|40.4|
|30|Marcin Gortat|679|60.2|27.0|12.5|50.4|42.6|37.7|
|31|Al Jefferson|340|52.9|29.7|16.8|50.6|38.6|33.3|
|32|<br>Jonas Valanciunas|239|59.4|26.8|13.4|50.7|43.8|37.5|
|33|<br>Omer Asik|578|58.8|25.8|14.0|51.2|39.6|29.6|
|34|Greg Stiemsma|407|56.0|31.2|12.5|51.3|41.7|33.3|
|35|<br>Tyson Chandler|794|57.6|25.6|16.5|51.4|40.4|34.4|
|36|Nikola Vucevic|421|64.4|24.0|11.6|51.7|37.6|26.5|
|37|Marc Gasol|344|52.6|26.5|19.5|51.9|33.0|32.8|
|38|Spencer Hawes|185|61.1|29.7|8.6|52.2|32.7|25.0|
|39|<br>Nikola Pekovic|669|55.5|27.5|16.9|52.6|46.2|38.1|
|40|Greg Smith|207|65.2|26.1|8.2|52.6|35.2|35.3|
|41|<br>Tristan Thompson|174|67.2|18.4|14.4|53.0|56.3|32.0|
|42|Chris Wilcox|217|65.9|21.2|12.4|53.2|45.7|40.7|
|43|Robin Lopez|201|61.2|22.4|14.9|53.7|31.1|33.3|
|44|Jordan Hill|195|60.5|17.9|20.5|54.2|51.4|27.5|
|45|<br>Tler Zeller|298|534|305|161|547|407|333|
|<br>46|y<br>Chris Kaman|<br>445|.<br>51.2|.<br>25.6|.<br>22.5|.<br>54.8|.<br>42.1|.<br>42.0|
|47|Drew Gooden|562|61.6|23.3|14.9|54.9|37.4|36.9|
|48|Anderson Varejao|224|56.7|23.2|19.2|55.9|42.3|37.2|
|49|<br>Kevin Love|357|55.2|24.6|20.2|57.9|36.4|31.9|
|50|Greg Monroe|302|57.0|25.2|17.5|58.7|55.3|35.9|
|51|David Lee|400|603|233|153|610|333|295|
|<br>52|<br>Luis Scola|<br>199|.<br>62.8|.<br>22.6|.<br>14.6|.<br>62.4|.<br>28.9|.<br>27.6|







2013 Research Paper Competition Presented by: 

7 



## **Appendix 1A: Same data as Appendix 1, but sorted according to % of shots occurring close to the basket** 

|Rank|Defender|Shots<br>|**% Close**<br>|% Mid-|% 3-point|Close<br>|Mid<br>|3-point<br>|
|---|---|---|---|---|---|---|---|---|
|||Faced|**Range **|range|range|FG%|FG%|FG%|
|**1**|**Dwight Howard**|**409**|**48.2**|**32**|**19.1**|**45.7**|**38.2**|**43.6**|
|2|<br>DeMarcus Cousins|279|48.4|29.7|20.1|48.2|38.6|44.6|
|3|Andris Biedrins|317|49.8|28.7|20.5|46.8|42.9|36.9|
|4|Chris Kaman|445|51.2|25.6|22.5|54.8|42.1|42|
|5|Nazr Mohammed|260|51.9|28.1|18.8|49.6|41.1|28.6|
|6|Nick Collison|273|52|27.8|18.7|47.9|35.5|37.3|
|7|Emeka Okafor|310|52.3|24.5|22.6|47.5|43.4|32.9|
|<br>8|<br>Marc Gasol|<br>344|<br>52.6|<br>26.5|<br>19.5|<br>51.9|<br>33|<br>32.8|
|9|Al Jefferson|340|52.9|29.7|16.8|50.6|38.6|33.3|
|10|<br>Tyler Zeller|298|53.4|30.5|16.1|54.7|40.7|33.3|
|11|<br>JaVale McGee|401|53.6|30.2|16|46.1|40.5|40.6|
|**12**|<br>**Roy Hibbert**|**419**|**54.4**|**29.6**|**14.8**|**38.2**|**37.9**|**30.7**|
|13|<br>Kevin Garnett|772|54.4|28.6|16.2|48.3|37.6|41.6|
|14|Aaron Gray|275|54.5|29.5|15.6|49.3|39.5|44.2|
|15|<br>Kevin Love|357|55.2|24.6|20.2|57.9|36.4|31.9|
|16|Nikola Pekovic|669|55.5|27.5|16.9|52.6|46.2|38.1|
|17|Kevin Seraphin|475|55.6|28.4|14.9|48.1|40.7|35.2|
|18|Chris Bosh|263|55.9|23.2|19.8|49.7|32.8|40.4|
|19|Greg Stiemsma|407|56|31.2|12.5|51.3|41.7|33.3|
|20|<br>Nene Hilario|212|56.1|25.9|17.9|48.7|36.4|29|
|21|Samuel Dalembert|777|56.4|30.4|12.9|48.6|38.6|41|
|22|Amir Johnson|207|56.5|25.1|17.4|46.2|44.2|41.7|
|23|Joakim Noah|334|56.6|27.8|14.4|45.5|44.1|31.3|
|24|Anderson Varejao|224|56.7|23.2|19.2|55.9|42.3|37.2|
|25|Jermaine O'Neal|392|56.9|28.1|14|44|32.7|32.7|
|26|Greg Monroe|302|57|25.2|17.5|58.7|55.3|35.9|
|27|Elton Brand|198|57.1|26.8|14.1|39.8|32.1|46.4|
|28|Tim Duncan|930|57.3|28.6|13.7|47.1|41.4|46.5|
|29|Tyson Chandler|794|57.6|25.6|16.5|51.4|40.4|34.4|
|30|<br>Marcus Camby|204|57.8|28.4|13.7|48.3|41.4|39.3|
|31|LaMarcus Aldridge|221|58.8|24.9|14.5|43.9|38.2|46.9|
|32|<br>Tiago Splitter|687|58.8|27.2|13.5|48.5|38|35.5|
|33|Omer Asik|578|58.8|25.8|14|51.2|39.6|29.6|
|34|Kendrick Perkins|745|59.3|24.3|16.1|45.5|37|36.7|
|35|Jonas Valanciunas|239|59.4|26.8|13.4|50.7|43.8|37.5|
|36|<br>Kosta Koufos|200|60|23.5|15.5|45|31.9|25.8|
|37|Marcin Gortat|679|60.2|27|12.5|50.4|42.6|37.7|
|38|David Lee|400|60.3|23.3|15.3|61|33.3|29.5|
|39|Jeremy Tyler|177|60.5|29.4|10.2|47.7|38.5|50|
|40|<br>Jordan Hill|195|60.5|17.9|20.5|54.2|51.4|27.5|
|41|Spencer Hawes|185|61.1|29.7|8.6|52.2|32.7|25|
|42|<br>Robin Lopez|201|61.2|22.4|14.9|53.7|31.1|33.3|
|43|<br>Ed Davis|391|61.6|23.3|14.8|49.4|40.7|34.5|
|44|Drew Gooden|562|61.6|23.3|14.9|54.9|37.4|36.9|
|45|**Larry Sanders**|**622**|**61.9**|**22.2**|**15.4**|**38.4**|**32.6**|**30.2**|
|46|<br>Luis Scola|199|62.8|22.6|14.6|62.4|28.9|27.6|
|47|Nikola Vucevic|421|64.4|24|11.6|51.7|37.6|26.5|
|48|Ekpe Udoh|468|65.2|20.1|14.1|46.2|42.6|34.9|
|49|<br>Greg Smith|207|65.2|26.1|8.2|52.6|35.2|35.3|
|50|<br>Chris Wilcox<br>|217|65.9|21.2|12.4|53.2|45.7|40.7|
|51|Tristan Thompson|174|67.2|18.4|14.4|53|56.3|32|
|**52**|<br>**Serge Ibaka**|**104**|**74**|**16.3**|**9.6**|**41.6**|**35.3**|**10**|







2013 Research Paper Competition Presented by: 

8 



## **Appendix 2: Expanded Results from Case Study 2: Shot Defended: Shots faced when defender was close to shooter.** 

A) **Shots defended:** The results are presented as: 

(% of shots where defenders was within 1 foot) **/** (% within 3-feet) **/** (% within 5-feet) 

|5-ft Rank<br>1|Defender<br>h Hll|Shots Faced<br>206|Within 1ft<br>15|Within 3ft<br>Within 5ft<br>223<br>359|
|---|---|---|---|---|
|<br>2|Jos arreson<br>Kosta Koufos|<br>447|.<br>3.8|.<br>.<br>21.3<br>35.6|
|3|Jordan Hill|519|1.9|22.4<br>35.1|
|**4**|<br>**Serge Ibaka**|<br>**223**|**1.8**|<br>**21.1**<br>**34.5**|
|5|Chris Wilcox|616|1.6|17.9<br>34.4|
|6<br>|Greg Smith<br>'|613<br>|1.6<br>|16.6<br>34.3<br> <br>|
|7<br>8<br>|Jermaine ONeal<br>Cole Aldrich<br>|925<br>364<br>|1.6<br>0.8<br>|17.6<br>34.1<br>14.0<br>33.8<br> <br>|
|9<br>10|Greg Stiemsma<br>Jonas Valanciunas|910<br>536|1.9<br>2.1|18.6<br>33.7<br>18.1<br>33.6|
|11<br>|<br>Ekpe Udoh<br>|1321<br>|2.0<br>|17.6<br>32.6<br> <br>|
|**12**<br>13|**Larry Sanders**<br>Spencer Hawes|**1482**<br>553|**2.4**<br>1.4|**17.3**<br>**32.5**<br>16.3<br>32.2|
|<br>14|<br>Jason Collins|<br>207|<br>1.9|<br> <br>16.9<br>31.9|
|15|Jeremy Tyler|502|2.4|18.1<br>31.7|
|16<br>|<br>Marcin Gortat<br>|1745<br>|1.7<br>|17.3<br>31.4<br> <br>|
|17|Elton Brand|547|1.3|17.0<br>31.3|
|18|Gustavo Ayon|437|0.9|16.5<br>31.1|
|19|<br>Robin Lopez|540|0.7|16.9<br>31.1|
|20|Tim Duncan|2353|1.4|17.5<br>31.1|
|21<br>|Kevin Love<br>|922<br>|1.8<br>|15.2<br>31.0<br> <br>|
|22|Amir Johnson|488|2.9|17.4<br>30.5|
|23|Drew Gooden|1513|1.2|13.4<br>30.3|
|24<br>|Tiago Splitter<br>|2022<br>|1.6<br>|15.4<br>30.1<br> <br>|
|25|Anthony Randolph|284|0.4|15.5<br>29.9|
|26|<br>Andra Blatche|389|15|144<br>298|
|<br>27|y<br>Jon Leuer|<br>239|.<br>1.3|.<br>.<br>15.5<br>29.7|
|28|Lavoy Allen|239|1.7|17.6<br>29.7|
|29<br>|<br>Amar'e Stoudemire<br>|253<br>|2.8<br>|13.0<br>29.6<br> <br>|
|30|Chris Kaman|1095|2.5|17.4<br>29.5|
|31|Kurt Thomas|235|2.1|13.2<br>29.4|
|<br>32|<br>Nikola Vucevic|<br>1352|<br>1.7|<br> <br>14.1<br>29.0|
|33|Tyson Chandler|2186|1.3|15.7<br>29.0|
|34<br>|<br>Kevin Garnett<br>|2067<br>|0.8<br>|13.0<br>28.7<br> <br>|
|35|Andrew Bogut|248|1.2|13.3<br>28.6|
|**36**|**Roy Hibbert**|**1094**|**1.9**|**16.5**<br>**28.6**|
|37|<br>Jason Smith|221|1.8|15.4<br>28.5|
|38|Brandan Wright|435|0.9|13.8<br>28.5|
|39<br>|<br>Andris Biedrins<br>|783<br>|1.9<br>|15.2<br>28.4<br> <br>|
|40<br>41|Al Jefferson<br>Ian Mahinmi|947<br>532|1.6<br>2.1|14.3<br>28.3<br>16.4<br>28.2|
|<br>42|<br>Ed Davis<br>|<br>1171|<br>1.2|<br> <br>14.6<br>28.2|
|43|Tyler Zeller|741|1.1|13.5<br>27.9|
|44<br>|<br>Samuel Dalembert<br>|1765<br>|1.9<br>|15.2<br>27.8<br> <br>|
|45|Anderson Varejao|603|0.7|12.9<br>27.5|
|46|Kevin Seraphin|1141|1.5|16.7<br>27.5|
|47|<br>Tristan Thompson|611|1.3|14.1<br>27.5|
|48|Darko Milicic|420|1.0|13.8<br>27.4|
|49<br>|Patrick Patterson<br>|280<br>|1.8<br>|13.9<br>27.1<br> <br>|
|50|Nick Collison|854|1.4|12.6<br>27.0|
|51|Jared Jeffries|281|1.1|13.5<br>27.0|
|52<br>|<br>Brook Lopez<br>|337<br>|2.4<br>|12.8<br>27.0<br> <br>|
|53|Omer Asik|1571|1.5|15.1<br>27.0|
|54|Joakim Noah|1017|13|130<br>268|
|<br>55|<br>Andre Drummond|<br>210|.<br>1.4|.<br>.<br>10.5<br>26.7|
|56<br>57|Luis Scola<br>Did L|629<br>1269|1.3<br>12|13.8<br>26.6<br>113<br>265|
|<br>58|av ee<br>Kwame Brown|<br>242|.<br>0.8|.<br>.<br>12.8<br>26.4|
|59|Pau Gasol|227|0.0|0.0<br>26.4|
|<br>60|<br>Jamaal Magloire|<br>228|<br>2.6|<br> <br>16.2<br>26.3|
|61|Jason Thompson|289|1.4|11.1<br>26.3|
|62<br>|<br>Chris Bosh<br>|810<br>|0.6<br>|10.5<br>26.0<br> <br>|
|63|Kendrick Perkins|2605|1.3|12.6<br>25.9|
|64|Ryan Hollins|337|1.5|11.9<br>25.5|
|<br>65|<br>Marc Gasol|<br>1071|<br>1.5|<br> <br>13.7<br>25.5|
|66|Nazr Mohammed|699|1.3|13.2<br>25.5|
|67<br>|Hasheem Thabeet<br>|444<br>|0.9<br>|11.7<br>25.5<br> <br>|
|68<br>69|Byron Mullens<br>Festus Ezeli|442<br>487|0.5<br>1.4|13.3<br>25.3<br>12.9<br>25.3|
||||9|2013 Research|



2013 Research Paper Competition Presented by: 







|70|Marcus Camby|674|0.4|11.1|25.2|
|---|---|---|---|---|---|
|71|Nene Hilario|598|2.2|11.2|25.1|
|72|Aaron Gray|836|0.8|11.4|25.0|
|73|Emeka Okafor|818|1.2|13.3|24.9|
|74|Greg Monroe|853|2.2|11.5|24.7|
|75|Meyers Leonard|211|0.9|12.3|24.6|
|76|Zaza Pachulia|492|1.8|13.6|24.6|
|77|Ryan Anderson|387|0.8|11.6|24.5|
|78|DeMarcus Cousins|802|1.5|11.5|24.4|
|79|DeAndre Jordan|566|0.5|10.6|24.4|
|80|DeJuan Blair|353|0.8|9.1|24.4|
|81|JaVale McGee|928|1.6|11.7|24.4|
|82|Nikola Pekovic|1980|1.0|13.4|24.0|
|**83**|**Dwight Howard**|**1071**|**1.2**|**10.0**|**23.6**|
|84|Al Horford|269|1.9|10.8|23.0|
|85|LaMarcus Aldridge|732|0.7|10.9|23.0|
|86|Enes Kanter|318|2.8|12.3|22.6|
|87|Boris Diaw|285|1.1|7.7|22.5|
|88|Andrew Bynum|614|0.5|9.8|22.3|
|89|Blake Griffin|256|0.8|9.0|21.9|
|90|Andrea Bargnani|727|1.0|9.8|21.9|
|91|Brandon Bass|271|1.1|11.8|21.8|
|92|Brendan Haywood|404|1.0|10.4|21.0|
|93|Tyler Hansbrough|381|1.3|9.2|20.7|







2013 Research Paper Competition Presented by: 

10 



## **B) Proximal FG%: The results summarize the FG% of opponents when each defender was within 5 feet.** 

|Rank||Defender|FG%|
|---|---|---|---|
||**1**|**Larry Sanders**|**34.9%**|
||2|<br>Andrea Bargnani|35.2%|
||3|<br>Kendrick Perkins|37.3%|
||4|Elton Brand|38.0%|
||**5**|**Roy Hibbert**|**38.7%**|
||6|Kosta Koufos|39.0%|
||7|Nene Hilario|40.0%|
||8|Andris Biedrins|41.0%|
||9|Greg Stiemsma|41.7%|
||10|Jermaine O'Neal|42.2%|
||11|JaVale McGee|42.5%|
||12|Nazr Mohammed|43.3%|
||13|Ian Mahinmi|43.3%|
||14|Tim Duncan|43.4%|
||**15**|**Dwight Howard**|**43.5%**|
||16|Marc Gasol|43.6%|
||17|Kevin Seraphin|43.6%|
||18|<br>Jeremy Tyler|44.0%|
||19|LaMarcus Aldridge|44.1%|
||20|Aaron Gray|44.5%|
||21|Kevin Garnett|44.9%|
||22|DeMarcus Cousins|44.9%|
||23|Marcus Camby|45.3%|
||24|<br>Ekpe Udoh|45.4%|
||25|<br>Nick Collison|45.5%|
||26|Chris Bosh|45.5%|
||27|Tiago Splitter|45.6%|
||28|Tyson Chandler|45.7%|
||29|Samuel Dalembert|45.7%|
||30|Joakim Noah|45.8%|
||31|Omer Asik|46.0%|
||32|Emeka Okafor|46.6%|
||33|Tyler Zeller|46.9%|
||34|Chris Wilcox|47.2%|
||35|Marcin Gortat|47.5%|
||36|Spencer Hawes|47.8%|
||37|Nikola Pekovic|48.0%|
||38|Al Jefferson|48.5%|
||39|<br>Ed Davis|48.8%|
||40|Nikola Vucevic|49.0%|
||41|Greg Smith|49.1%|
||42|Robin Lopez|49.4%|
||43|<br>Chris Kaman|49.5%|
||44|Greg Monroe|50.2%|
||45|<br>Tristan Thompson|50.6%|
||46|<br>Luis Scola|51.5%|
||47|Drew Gooden|51.8%|
||48|Kevin Love|52.1%|
||49|Jonas Valanciunas|52.8%|
||50|David Lee|53.0%|
||51|Jordan Hill|53.9%|
||52|Anderson Varejao|54.2%|







2013 Research Paper Competition Presented by: 

11 


