<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2024/2024 - KabaddiPy A package to enable access to Professional Kabaddi Data - Unknown Authors.pdf -->

CMSAC REPRODUCIBLE RESEARCH 

1 

# **KabaddiPy: A package to enable access to Professional Kabaddi Data** 

### **Bhaskar Lalwani**<sup>†</sup> 

**Aniruddha Mukherjee**<sup>†*</sup> 

School of Computer Engineering School of Computer Engineering Kalinga Institute of Industrial Technology Kalinga Institute of Industrial Technology 2205460@kiit.ac.in 2205533@kiit.ac.in 

**Abstract** Kabaddi, a contact team sport of Indian origin, has seen a dramatic rise in global popularity, highlighted by the upcoming Kabaddi World Cup in 2025 with over sixteen international teams participating, alongside flourishing national leagues such as the Indian Pro Kabaddi League (230 million viewers) and the British Kabaddi League. We present the first open-source Python module to make Kabaddi statistical data easily accessible from multiple scattered sources across the internet. The module was developed by systematically web-scraping and collecting team-wise, player-wise and match-by-match data. The data has been cleaned, organized, and categorized into team overviews and player metrics, each filterable by season. The players are classified as raiders and defenders, with their best strategies for attacking, counter-attacking, and defending against different teams highlighted. Our module enables continuous monitoring of exponentially growing data streams, aiding researchers to quickly start building upon the data to answer critical questions, such as the impact of player inclusion/exclusion on team performance, scoring patterns against specific teams, and break down opponent gameplay. The data generated from Kabaddi tournaments has been sparsely used, and coaches and players rely heavily on intuition to make decisions and craft strategies. Our module can be utilized to build predictive models, craft uniquely strategic gameplays to target opponents and identify hidden correlations in the data. This open source module has the potential to increase time-efficiency, encourage analytical studies of Kabaddi gameplay and player dynamics and foster reproducible research. The data and code are publicly available: https://github.com/kabaddiPy/kabaddiPy 

## **Introduction** 

Kabaddi is a fast-paced team-contact sport, that has been rapidly gaining international recognition and popularity. In a game that can be loosely described as a combination of rugby, American football and tag (1) two teams take turns sending a player, called the “raider” into the opponent’s half with the goal of tagging as many defenders as possible and returning to their own side without being tackled. The raider must accomplish this in a single breath for an offense lasting 30 seconds, all the while chanting “kabaddi” (pronounced kuh-bud-DEE). 

Similar to American football, where the offense aims to evade the opponent’s defense to score touchdowns, the raider in Kabaddi must dodge the defender’s tackles, tag them and return to their own half to score points. Meanwhile the defense must work in coordination, aiming to tackle and immobilize the raider before they can return. Unlike football, Kabaddi requires no ball or protective gear; it’s a minimalist sport that focuses purely on strategy and physical strength. 

Originally a traditional Indian sport, Kabaddi was first exhibited at the 1936 Berlin Olympics (2). Since becoming a regular feature in the Asian Games in 1990 (3), the sport has gained international recognition, as witnessed by the launch of the Kabaddi World Cup in 2004, with England set to host the 2025 edition (4; 5). The sport’s popularity skyrocketed with the inception of the Indian Pro Kabaddi League (PKL) in 2014, now attracting 230 million viewers, second only to cricket’s Indian Premier League (IPL). 

With success of the PKL, several regional leagues, like the European Kabaddi Championship and the British Kabaddi League, have emerged and over 30 nations have established dedicated national Kabaddi teams including the United States (6), Japan, South Korea and Iran. 

For a game rooted in strategy, which has witnessed growing viewership across the board, and its highly commercial nature - Star Sports bought the media rights for PKL for $120 million for five years (7), Kabaddi is an overlooked sport. It still lacks the analytical infrastructure seen in other sports such as hockey, basketball or football (8). Existing sports analytics research in Kabaddi has been hampered by easy access of publicly available data. The limited studies conducted have had high barriers of research, manually web scraping data from the official Pro Kabaddi League (PKL) website. (9; 10; 11). 

In this paper, we introduce the first open source module for aggregating Kabaddi data from the PKL website and other disparate sources. Through this module, we aim to improve access to Kabaddi data, standardize it into a single source, and contribute to the formation of a community of researchers and analysts around Kabaddi, increasing the potential for development of sophisticated strategies and detailed insights to improve team and player performance. 

## **Overview of Kabaddi Play** 

Kabaddi is set on a rectangular court, measuring 10 by 13 metres (33 feet by 43 feet) for men and 8 by 12 metres (26 feet by 39 feet) for women, divided into two halves by a _midline_ . Two teams of seven players compete on opposite ends of the court. The game consists of two 20-minute halves separated by a 5-minute halftime break during which the teams switch sides. 

> † Both of the authors contributed equally. 

- Corresponding author: Aniruddha Mukherjee (23f1003186@ds.study.iitm.ac.in) 

CMSAC REPRODUCIBLE RESEARCH 

2 

The offense operates as a unique “tag and return” system (12), distinct from the ball-focused scoring of American football. The offensive player, the raider, sprints into the opponent’s half, seeking to tag one or more defenders, and return to their own half without being tackled, all in a single breath. A tag can be made using either a hand or a foot and each successful tag earns a point, with bonus points awarded for tagging multiple defenders or clearing the opponent’s court. This is known as a “ _raid_ ”, and an entire raid must be completed in no more than 30 seconds. It is crucial that this be done in one breath, hence the necessity to continuously chant “kabaddi”. 

While Kabaddi’s defense shares similarities with that of rugby, the defenders focus on preventing the raider from returning to their own half, rather than keeping them out. If the defenders successfully tackle and hold the raider before they can return, the defending team earns a point. Additionally, the defense scores if the raider goes out of bounds or fails to return to their half before exhaling (when they stop chanting “kabaddi”). 

If the defenders attempt a tackle but fail to prevent the raider from returning to their own half, all defenders involved in the tackle are considered tagged, resulting in points being conceded to the raiding team. This creates a unique, high-stakes dynamic where every raid becomes a time-critical scoring opportunity for both the offense and defense. Players who are tagged or tackled are taken out of the game but can be “ _revived_ ” when their team scores from a successful tag or tackle. 



**Figure 1:** Standard Style Kabaddi Mat. (13) 

On the court, key lines play a crucial role in the point system. The _baulk line_ , which is 3.75 meters (12.3 feet) from the midline, acts as a marker that the raider must cross to make the raid legal; if they fail to cross it without making a tag, no points are scored, and the raid is considered unsuccessful. The _bonus line_ , located 1 meter (3.2 feet) beyond the baulk line, offers the raider an opportunity to score an additional point, if they cross it while keeping at least one foot in the air and manage to return without being tackled. This is only possible when there are six or more players on the mat. 

In addition to standard gameplay, special situations such as _do-or-die raids_ and _all-outs_ significantly impact scoring dynamics. A team can further increase their score by achieving an all-out, which involves eliminating all the opposing players on the court. This forces the opposition to reset their players on the court, and concede two points. A do-or-die raid occurs, after two consecutive empty raids, and the team must score points in it or face a penalty of one point. The green, yellow, and red cards in Kabaddi are analogous to soccer’s warning, temporary suspension, and ejection penalties. A green card is like a verbal warning, a yellow card mirrors a player being temporarily sidelined (e.g., a 2-minute suspension), and a red card resembles a player being ejected from the game. Receiving a yellow or red card awards one technical point to the opposing team. 

The strategic depth of Kabaddi lies in how teams deploy their raiders and defenders, utilizing formations, timing, and coordination to gain an advantage. Defensive tactics, such as chain tackles and “super tackles”, where a shorthanded team successfully tackles a raider, add another layer of complexity to the game. 

Various defensive and offensive strategies for scoring points are described briefly, in Table 1 and Table 2 (14). 

## **Methodology/Data Collection** 

KabaddiPy has been developed as a comprehensive Python package that has aggregated historical data over 10 previous Pro Kabaddi League (PKL) seasons, through web scraping multiple sources: the official PKL website, ProKabaddi.com (15), Tableau Dashboard prepared by SportsKPI (16), kabaddiadda.com (17) and Global Sports Data Archive (18). Play-by-play and player statistics were primarily sourced from ProKabaddi.com, while team-level data was gathered from the Tableau Dashboard. Partial auction data was scraped from kabaddiadda. Additional metrics for raider performance were scraped from the Tableau Dashboard. The data was cross-verified with information from the official PKL website to ensure its validity. 

The scraper populated a central repository with the historical data (github-kabaddi-data) for ease of access. The repository will be constantly updated with live data when the PKL season is going on. 

CMSAC REPRODUCIBLE RESEARCH 

3 

|**Defensive Move**|**Description**|**Offensive Move**|**Description**|
|---|---|---|---|
|Waist/Back Hold|When the defender attempts to grab the raider<br>mid-air by the waist to pin them down on<br>|Toe Touch|The raider attempts to score by touching<br>just the defenders’ toe.|
||the mat.<br>||Raider attempts to score by touching|
|Ankle Hold|The defenders attempt to stop the raider<br>bbbith kl|Hand Touch|<br>the defenders’ with their arm.|
||y grange ane.||The raider attemts to score b kickin|
|Thigh Hold|The defenders attempt to hold the thigh of<br>id ith bth hd|Front and Side Kick|p   y g<br>in front or sideways.|
||raer w o ans.||Rid  t thi bk td th|
|Block|The defenders physically try to stop the raider<br>from crossing the mid-line and go back to their<br>court.|Reverse/Back Kick|aer can urn er ac owars e<br>defender and kick backwards to score a<br>touchpoint.|
|Chain Tackle|When two or more defenders attempt a<br>co-ordinated tackle to prevent the raider<br>from crossingthe midline|Leg Thrust|The raider uses their leg strength to<br>push through the defenders; used<br>when trapped in a hold or tackle.<br>|
|Dash|When the defender pushes the raider out<br>of the court by "dashing". Earns a point<br>for the defense.|Dubki (duck)|The raider ducks below the defenders<br>to reach the half line. Used to avoid chain<br>tackle|



**Table 1:** Table describing various defending strategies **Table 2:** Table with diverse raider strategies used in used in Kabaddi Kabaddi 

In addition to these core functions, the package offers several helper functions specifically designed to process, parse and clean the raw data into structured formats. While these processing functions were developed as part of the Kabaddi package, they are not expected to be used by anyone for Kabaddi analytics. However, to ensure full reproducibility and transparency, we provide both the web scraping functions and the collated data. This allows researchers to not only access pre-processed data (by function calls) but also to replicate the data collection process. 

## **Installing KabaddiPy** 

KabaddiPy, (v1.0.0) is available on the Python Package Index (PyPI) and can be downloaded using pip. 

pip install kabaddiPy 

The class can be initialized with the below. All the functions belong to this class and can be accessed accordingly. 

import kabaddiPy # Initialize the aggregator pkl = kabaddiPy.PKL() 

## **Module Usage** 

kabaddiPy enables an analyst to start from very basic data, such as the season standings, and move to advanced statistics such as, the effectiveness of raiders against a given number of defenders for a given team or zone-wise strength of players. 

The module makes understanding the sport for those new to it (a large portion of our audience) easy, while still allowing for experts to conduct an in-depth analysis of strategies at the team, match or player level. 

To demonstrate the functionality of kabaddiPy, we identify a pivotal match from last season (season 10): the game that secured Puneri Paltan’s place in the final, ultimately leading to their championship victory. 

matches = pkl.get_season_matches(season=10) 

result = matches[(matches['League_Stage'] == 'Semi Final') & ((matches['team_name_1'] == 'Puneri Paltan') | (matches['team_name_2'] == 'Puneri Paltan'))] 

# selecting specific columns to display print(result[['Season','Match_ID','League_Stage','Match_Outcome', 'team_score_1','team_score_2','team_name_1','team_id_1','team_name_2','team_id_2', 'Winning Margin']]) 

<mark>Season Match_ID League_Stage Match_Outcome team_ team_ team_ team_ team_ team_ Winning score_1 score_2 name_1 id_1 name_2 id_2 Margin --------------------------------------------------------------------------------------------------------------10 3163 Semi Final Puneri Paltan 37 21 Puneri 7 Patna 6 16 won by 16 Pts Paltan Pirates # #...with 6 additional columns 'Match_Name', 'Year', 'Venue','Start_Date', 'End_Date' and 'Result',</mark> 

Crucially, we are able to get the unique Match_ID here. We can use this ID to query functions to know exactly why Puneri Paltan won the match by a huge margin. 

CMSAC REPRODUCIBLE RESEARCH 

4 

We plot the point progression for this 40 minute match with the Match_ID in Fig 2. 

pkl.plot_point_progression(season=10, match_id = 3163) 



**Figure 2** 

We can clearly see that after an initial period of stagnation between events 20 and 35, Patna Pirates could never recover. This could have been due to several factors, such as a player receiving a red/yellow card, missing a bonus point or the team suffering an all-out. To pinpoint the exact cause we retrieve play-by-play details for the match. 

events = pkl.load_pbp(season=10, match_id='3163') 

print(events[['event_no', 'event','event_text', 'clock', 'raider_id', 'defender_id', 'score']].iloc[20:35]) 

# using iloc to select a subset of the match events 

|event_no<br>--------|event<br>-------------------|event_text<br>clock<br>---------------------------------------------------|raider_id<br>------------|defender_id<br>-------------|score<br>-------|
|---|---|---|---|---|---|
|21|Unsuccessful Raid|Sudhakar M unsuccessful raid<br>10:15|4193.0|NaN|[9, 8]|
|22|Timeout|None<br>09:48|NaN|NaN|None|
|23|Empty Raid|Aslam Inamdar empty raid<br>09:48|4960.0|NaN|[9, 8]|
|24|Empty Raid|Sachin empty raid<br>09:20|757.0|NaN|[9, 8]|
|25|Successful Raid|Akash Shinde raids successfully<br>09:02|4959.0|NaN|[10, 8]|
|26|Substitution|Abinesh Nadarajan comes in for Akash Shinde 08:19|NaN|NaN|None|
|27|Empty Raid|Sachin empty raid<br>08:15|757.0|NaN|[10, 8]|
|28|Empty Raid|Mohit Goyat empty raid<br>07:56|4022.0|NaN|[10, 8]|
|29|Unsuccessful Raid|Sachin unsuccessful raid<br>07:40|757.0|4925.0|[11, 8]|
|30|Empty Raid|Aslam Inamdar empty raid<br>07:07|4960.0|NaN|[11, 8]|
|31|Empty Raid|Babu M empty raid<br>06:39|726.0|NaN|[11, 8]|
|32|Successful Raid|Mohit Goyat raids successfully<br>06:24|4022.0|NaN|[12, 8]|
|33|Substitution|Sandeep Kumar comes in for Babu M<br>05:46|NaN|NaN|None|
|34|Successful Raid|Sandeep Kumar raids successfully<br>05:38|5282.0|NaN|[12, 9]|
|35|Successful Raid|Aslam Inamdar raids successfully<br>05:19|4960.0|NaN|[13, 9]|
|#...Note<br>#<br>#....wit<br>#<br><br>#<br>|: Events are sequen<br>h 28 more columns '<br>'raid_touch_points'<br>'defending_capture_|tial, but the clock counts down from 20 minutes for <br>event_half', 'event_id', 'raiding_team_id', 'defend<br>, 'raid_bonus_points', 'raid_technical_points', 'ra<br>points', 'defending_bonus_points', 'defending_techn|each half o<br>ing_team_id'<br>id_all_out_p<br>ical_points'|f the game<br>, 'raid_point<br>oints',<br>,|s',|
|#<br><br>#<br>|'defending_all_out_<br>'review', 'defendin|points', 'super_raid', 'super_tackle', 'do_or_die', <br>g_points', 'clock', 'status_id', 'score', 'seq_no',|'super_ten'<br>'defenders|, 'high_five'<br>',|,|
|#<br>|'created_date', 'pl|ayer_id', 'substituted_by', 'team_id' and 'substitu|te_time'|||



A quick data query and we have a clear picture of the critical five minute interval where the Patna Pirates were inefficient. They were unable to tackle the offense, while their two consecutive empty raids led to a do-or-die raid, which was unsuccessful and resulted in the concession of an additional point. This resulted in Paltan gaining a lead of 4 points and ultimately winning. 

A notable return of this data is the raider_id and defender_id’s for each event, which can be used to analyze team dynamics. For example, a raider’s performance can be assessed by their success rate against varying numbers of defenders (Fig. 6) and how their inclusion in the team impacts its overall performance. KabaddiPy enables analysts to easily explore these questions by utilizing a combination of pbp data, player-ids and performance metrics. 

CMSAC REPRODUCIBLE RESEARCH 

5 

For analysts looking to understand the game and the data, season standings can serve as the starting point in their analyses. To demonstrate, we begin by retrieving the season standings for Season 5. 

print(pkl.get_standings(season=5).head(10)) 

|Group<br>------<br>B|Season<br>--------<br>5|Team_Id<br>Team_Name<br>---------------------------<br>4<br>Bengal Warriorz|League_position<br>-----------------<br>1|Matc<br>-----<br>22|hes_played<br>Win<br>---------------<br>11|s<br>Lost<br>--------<br>5|Tied<br>------<br>6|
|---|---|---|---|---|---|---|---|
|B|5|6<br>Patna Pirates|2|22|10|7|5|
|B|5|30<br>UP Yoddhas|3|22|8|10|4|
|B|5|1<br>Bengaluru Bulls|4|22|8|11|3|
|B|5|8<br>Telugu Titans|5|22|7|12|3|
|B|5|29<br>Tamil Thalaivas|6|22|6|14|2|
|A|5|31<br>Gujarat Giants|1|22|15|4|3|
|A|5|7<br>Puneri Paltan|2|22|15|7|0|
|A|5|28<br>Haryana Steelers|3|22|13|5|4|
|A|5|5<br>U Mumba|4|22|10|12|0|
|#.....|with 5 m|ore columns 'Draws', 'No Re|sult','League_poi|nts',|'Score_diff',|'Qualifi|ed'|



Using the Team_Id obtained, the team level stats can be returned from get_team_info() function to see a detailed breakdown of the team stats. We will now examine the stats for the top ranked team in Group B, “Bengal Warriorz”, with Team_Id = 4 

df_rank, df_value, df_per_match, team_raider_skills, team_defender_skills = pkl.get_team_info(season=5, team_id=4) print(df_value) 

|season<br>5.0<br>-----------------------------------------------------------|
|---|
|team_id<br>4|
|team_name<br>Bengal Warriorz|
|matches_played<br>24|
|team-all-outs-conceded_value<br>29|
|team-successful-tackle-percent_value<br>34.81|
|team-super-raid_value<br>11|
|...<br>...|
|# with 64 more rows across three dataframes each for rank, value, and per match score of team raid,|
|# successful-raid-percent, dod-raid-points, super-tackles, total_touch_points, total_bonus_points,<br># raid-points, successful-raids, total-points-conceded, tackle-points, total-points, successful-tackles,|
|# successful-tackles-per-match, all-outs-inflicted, average-raid-points, avg-points-scored and<br># average-tackle-points|
|# and two more dataframes for raider, defender skills with season, skill type, skill name and value.|



To analyze the gameplay of the Warriorz, we plot the points they scored on the Kabaddi mat (see Fig. 3 and Fig. 4). This data is crucial for opponents, as it highlights key areas of the court where the Warriorz performed well or struggled. By identifying these zones and the top performers within the team, opponents can develop targeted strategies to counter the Warriorz more effectively in future matches. 

pkl.plot_team_zones(team_id=4, season=5, zone_type='strong') pkl.plot_team_zones(team_id=4, season=5, zone_type='weak') 



**Figure 3:** Strong Zones of Bengal Warriorz, Season 5 



**Figure 4:** Weak Zones of Bengal Warriorz, Season 5 

CMSAC REPRODUCIBLE RESEARCH 

6 

KabaddiPy provides an even deeper and more granular view of player-level data. To demonstrate, we call and filter the get_team_roster() function to get top five scoring players of Warriorz for Season 5. We plot their strong zones to assess their individual contributions to the team’s overall strength. 

df = pkl.get_team_roster(team_id=4, season=5) 

print(df[['Player ID', 'Name','Played Count','Total Points','Team Name', 'Team ID', 'Matches']].sort_values(by='Total Points', ascending=False).head(5)) # using .head() to select 5 players 

We get a list of the top 5 Warriorz players by the total number of points scored in the season. 

|Player ID<br>---------|Player Name<br>Jersey Number Played Count<br>----------------------------------------------|Total Points<br>Team Name<br>------------------------------------|Team ID<br>--------|Matches<br>----------|
|---|---|---|---|---|
|143|Maninder Singh<br>9<br>21|192<br>Bengal Warriors|4|24|
|12|Jang Kun Lee<br>4<br>22|89<br>Bengal Warriors|4|24|
|211|Deepak Narwal<br>7<br>17|87<br>Bengal Warriors|4|24|
|322|Surjeet Singh<br>6<br>24|79<br>Bengal Warriors|4|24|
|160|Ran Singh<br>13<br>23|64<br>Bengal Warriors|4|24|
|#....with|the full team roster having 12 more rows and|8 more columns for 'Captain Count',|||
|#<br>'Green|Card Count', 'Yellow Card Count', 'Red Card C|ount', 'Starter Count', 'Top Raider|Count',||
|#<br>'Top D|efender Count' and 'Total Matches in Season'||||



We use the PlayerID obtained to plot the strong zones for those Warriorz players. (see Fig. 5) 

plot_player_zones_grid(player_ids=[143, 12, 211, 160], season=5, zone_type='strong', max_cols=2) 



**Figure 5:** Top Warriorz players strong zones 

It can be observed that player 211 (Deepak Narwal) has just played 17 matches as compared to 22 matches played by player 12 (Jang Kun Lee) but has scored a comparable number of points. But their strong zones are very different, the 

CMSAC REPRODUCIBLE RESEARCH 

7 

former’s being the midline and bonus right, while the latter’s being the bonus left and the baulk line. 

This facilitates detailed positional analysis and informed team lineup construction while enabling coaches and analysts to optimize player rotations, develop targeted training regimens, and craft opposition-specific strategies to enhance team performance. 

A core Kabaddi dynamic is the performance of a raider against varying numbers of defenders. This metric is critical, as an excellent raid performance against a high number of defenders directly improves a team’s winning chances. The function get_player_rvd() can be used to analyze this aspect. By providing access to this data across historical seasons, KabaddiPy enables coaches and teams to to identify trends, assess raider efficiency under different defensive pressures and make strategic decisions, such as optimizing substitutions to improve team performance. 

We use this function to retrieve and then plot the historical career data for a raider (Maninder Singh, ID 4947) to identify patterns to identify strengths and weaknesses, and develop training strategies accordingly. 

rvd_data = pkl.get_player_rvd(player_id = 4947) 

print(rvd_data[['season', 'player-id', 'Raider Name', 'Team ID','Number of Defenders', 'Total Raids', 'Percentage of Raids', 'Empty Raids Percentage','Successful Raids Percentage']] 

|season<br>-------|player-id<br>-----------|Raider Name<br>-----------------|Team_ID<br>---------|Number_of_Defenders<br>---------------------|Total_Raids<br>-------------|Percentage<br>of Raids<br>------------|Successful<br>Raids Percentage<br>-------------------|
|---|---|---|---|---|---|---|---|
|5|143|Maninder Singh|4|7|148|40.00%|46.60%|
|5|143|Maninder Singh|4|5|51|14.00%|15.70%|
|5|143|Maninder Singh|4|4|29|8.00%|34.50%|
|5|143|Maninder Singh|4|3|20|5.00%|45.00%|
|5|143|Maninder Singh|4|2|26|7.00%|80.80%|
|...|...|...|...|...|...|...|...|
|9|143|Maninder Singh|4|6|86|24.00%|66.30%|
|9|143|Maninder Singh|4|7|138|38.00%|52.20%|
|9|143|Maninder Singh|4|1|1|0%|100.00%|
|9|143|Maninder Singh|4|2|28|8%|89.30%|
|#....wi|th an addit|ional 13 rows and|three co|lumns including<br>'Tea|m Name', 'Emp|ty Raids Per|centage'.|





**Figure 6:** Successful Raid Percentage vs Number of Defenders by Season for Maninder Singh (PlayerID: 143) (Labels show Percentage of that type of Raid) 

All the KabaddiPy functions, both demonstrated and not, are directly reproducible from the repository. The code demonstrated in the paper can be found here as a Jupyter Notebook. 

## **Limitations** 

This module has certain data limitations beyond our control. Specifically, zonal data for seasons 8, 9, and 10 and match breakdown data for season 4 cannot be accessed publicly, potentially affecting the depth of positional and strategic analyses for these metrics. 

CMSAC REPRODUCIBLE RESEARCH 

8 

Additionally, crucial statistics such as successful raider skills and defender skills as well as raider success rate against particular number of defenders were unavailable for seasons 1 through 4, limiting historical comparisons and trend analyses. To address and avoid these data gaps for future seasons, we propose implementing more robust tracking technologies, and establishing open data-sharing initiatives. 

## **Conclusion** 

KabaddiPy was developed as an answer to the lack of consistent and publicly available data for the Pro Kabaddi League (PKL). Both the league and the sport have been rapidly growing in popularity. As the league gains momentum, so does the demand for comprehensive statistics and insights. KabaddiPy delivers reliable data and also promotes reproducible research by ensuring that every dataset and analysis can be consistently replicated. 

## **What’s Next** 

Further steps for KabaddiPy will be to expand its scope to include more rapidly growing international leagues, such as the Kabaddi World Cup and the British Kabaddi League. This will enable cross-league studies and comparisons and offer more insights into the global Kabaddi landscape. 

Although some auction data has been collected, the module’s dataset will be expanded, by web scraping, to provide for analysis with respect to this. 

## **Acknowledgements** 

We thank Alok Pattani, Dean Oliver and Rakshit Naidu for their invaluable feedback on early drafts of this paper. We also thank the owners of the websites for the data. 

## **Bibliography** 

- [1] P. Garfinkel, “Rugby Meets Red Rover: Kabaddi Has Captured the Heart of India,” _N.Y. Times_ , Oct. 2018. [p1] 

- [2] U. Nag, “How kabaddi went from local to global on the sidelines of the Olympics,” _Olympics_ , Apr. 2021. [p1] 

- [3] R. Venkat, “Kabaddi at Asian Games: Indian men and women rule the roost - winners list,” _Olympics_ , Oct. 2023. [p1] 

- [4] “World Cup 2025 - Kabaddi World Cup,” Apr. 2024. [Online; accessed 7. Sep. 2024]. [p1] 

- [5] O. Flash, “Wolverhampton first city outside Asia to host Kabaddi World Cup,” _BBC News_ , Jan. 2024. [p1] 

- [6] “US Kabaddi,” Sept. 2024. [Online; accessed 7. Sep. 2024]. [p1] 

- [7] J. Farooqui, “Pro Kabaddi League franchises valued at over Rs 100 cr each: Mashal Sports official,” _Economic Times_ , Oct. 2023. [p1] 

- [8] B. Howell and S. Gilani, “fastrhockey: The sportsdataverse’s r package for hockey data.,” 2021. [p1] 

- [9] P. Singh, B. Parashar, S. Agrawal, K. Mudgal, and P. Singh, “Kabaddi: a quantitative approach to machine learning model in pro kabaddi,” in _Proceedings of Second International Conference on Computational Electronics for Wireless Communications: ICCWC 2022_ , pp. 243–260, Springer, 2023. [p1] 

- [10] M. Parmar, “Kabaddi: From an intuitive to an quantitative approach for analysis, predictions and strategy,” 07 2018. [p1] 

- [11] V. Khullar, “K Means clustering and descriptive analytics based performance recommending system for Kabaddi team and player,” _Multimed. Tools Appl._ , vol. 83, pp. 29897–29914, Mar. 2024. [p1] 

- [12] H. Sidhu, “Kabaddi,” _Journal of Physical Education, Recreation & Dance_ , vol. 57, no. 5, pp. 75–77, 1986. [p2] 

- [13] “How to Play Kabaddi,” June 2020. [Online; accessed 6. Sep. 2024]. [p2] 

- [14] S. Singh, D. P. Srivastava, and C. Patvardhan, “Game theoretic analysis of kabaddi,” _J Stat Appl Prob_ , vol. 12, no. 1, pp. 313–319, 2023. [p2] 

- [15] “Pro Kabaddi League _|_ Official Website,” Aug. 2024. [Online; accessed 21. Aug. 2024]. [p2] 

- [16] “DEMO_PKL_S9,” Jan. 2023. [Online; accessed 21. Aug. 2024]. [p2] 

- [17] “Kabaddi Adda - Live Kabaddi Action, Score & News,” Aug. 2024. [Online; accessed 21. Aug. 2024]. [p2] 

- [18] “Global Sports Archive,” Sept. 2024. [Online; accessed 7. Sep. 2024]. [p2] 


