<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2019/2019 - The Economic Impact of NBA Superstars Evidence from Missed Games using Ticket Microdata from a Secondary Marketplace - Unknown Authors - b657c647.pdf -->



# **The Economic Impact of NBA Superstars: Evidence from Missed Games using Ticket Microdata from a Secondary Marketplace** 

Scott Kaplan,<sup>*1</sup> Vaibhav Ramamoorthy,<sup>2</sup> Cheenar Gupte,<sup>3</sup> Amit Sagar,<sup>3</sup> Deepak Premkumar,<sup>1</sup> Joshua Wilbur,<sup>4</sup> and David Zilberman<sup>5</sup> 

### Basketball Track Paper ID: 13389 

## **Abstract** 

The NBA is widely regarded as a “superstar-driven league." However, superstars may be forced to miss games due to injury or purposefully “rested” by teams. A superstar's absence has detrimental effects on the quality of games, especially with respect to the fan experience. This paper uses rigorous econometric methods to quantify the per-game value associated with the NBA’s top players by evaluating ticket price changes on a secondary ticket marketplace when such players are announced to miss a game. We collect high temporal frequency microdata from an online secondary ticket marketplace and the exact timing of player absence announcements to determine the reduction in willingness-to-pay associated with a superstar absence for the average NBA game attendee. Our findings suggest that absences of several superstars, including some of the most popular like Stephen Curry, Kyrie Irving, and Anthony Davis, do have a statistically significant and economically meaningful impact ranging from a 7-25% ($9-$25) reduction in the average ticket price for matchups in which they are absent. Over a season, this can lead to millions of dollars in welfare losses. We conduct additional heterogeneity tests, and find that certain players, like Stephen Curry and Kevin Durant, exhibit much larger away game absence effects, while others like Anthony Davis and Kristaps Porzingis experience much larger home game absence effects. Furthermore, the negative impact of a superstar absence is much smaller for games played in larger markets. Our findings have significant ramifications for the NBA and individual franchises, including NBA policies on resting players, the implications of suspensions for welfare of NBA fans, and franchise decision-making about dynamic pricing schemes in the primary marketplace. 

- _Corresponding Author_ . Email: <u>scottkaplan@berkeley.edu</u> 

- 1 PhD Candidate, Department of Agricultural and Resource Economics, UC Berkeley. 

- 2 M.A. Candidate, Department of Statistics, UC Berkeley. 

- 3 Undergraduate Student, Department of Electrical Engineering and Computer Science, UC Berkeley. 

- 4 PhD Candidate, Department of Mechanical Engineering, UC Berkeley. 

- 5 Professor and Robinson Chair, Department of Agricultural and Resource Economics, UC Berkeley. 



2019 Research Papers Competition Presented by: 



1 



## **1. Introduction** 

The National Basketball Association (NBA) has exploded in popularity over the last several years [1][2]. More than other sports, the NBA’s surge in popularity can be largely attributed to the fame and skill of its top players, including LeBron James and Stephen Curry, and has often been labeled a “superstar-driven league”[3][4]. Because of this, fan viewership and the entertainment value associated with the NBA product is strongly tied to fans’ desire to watch superstars play. Therefore, when it is announced that a star player will miss a game (either through an injury sustained, purposeful rest, suspension, etc.), there may be significant reductions in welfare associated with attending that NBA game. This has been an especially relevant point of discussion with respect to the NBA, since player absences are trending upwards as a result of teams choosing to purposefully rest players earlier in the season and more often [5]. This paper leverages recent advances in data availability as well as rigorous econometric methods in an attempt to provide a quantitative measure of the per-game value associated with the NBA’s top players. We aim to do this by evaluating ticket price changes on a secondary ticket marketplace when superstar players are announced to miss a game. 

What is a “superstar” player? Superstars are not necessarily the “best” players from a statistical standpoint – they are defined as much by their skill as they are by their popularity [6]. To encapsulate both of these factors in our analysis, we analyze all players who made the NBA All-Star Team during the 2017-18 season, which is a similar approach taken by other notable studies [7][8]. The list of players making the All-Star Team provides a great comparison of popularity and skill— the starters for the all-star rosters are based on a weighted average between fans (50%), players (25%), and selected media members (25%), while the bench players are selected through a vote by coaches from each respective conference [9]. Of course, there are other metrics that may be useful to rank player popularity and skill, such as the ranking of jersey sales by player for popularity and a player’s ``efficiency rating” (PER) for skill. We use the all-star criteria as a cutoff to determine which players to analyze, as it has been used in previous studies and incorporates notions of both popularity and skill.<sup>6</sup> 

The primary research question this paper attempts to answer is the following: what is the marginal economic loss, as measured by listed price changes on a secondary ticket marketplace, associated with a specific superstar’s absence for a game? This analysis has significant ramifications for NBA policies on resting players and announcement timing of player absences, team decision-making on signing free agents, drafting players, trading players, and scheduling promotional events, as well as implications for whether or not teams choose to engage in dynamic pricing on their primary ticket marketplaces. Our findings suggest that the absences of several superstars, including some of the most popular like Stephen Curry, Kyrie Irving, and Anthony Davis, lead to a statistically significant and economically meaningful impact ranging from a 7-25% ($9-$25) reduction in the average ticket price for those matchups. This implies hundreds of thousands of dollars in welfare lost for each of these matchups, and millions of dollars lost across all superstar absences over the course of a season. On the other hand, there are many slightly less popular, yet highly skilled superstars (e.g. Damian Lillard, Kristaps Porzingis, and James Harden) whose absences do not cause a meaningful 

6 Along with all players selected to the 2017-18 All-Star team, we also include Chris Paul, who did not make the All-Star team because of injury, but played (and missed) a sufficient number of games during the 2017-18 season and has acquired (and maintained) superstar status. 





2019 Research Papers Competition Presented by: 

2 



reduction in listed ticket prices. We conduct additional heterogeneity tests, which suggest that market size of the home team and whether the absence is for a home vs. away game also have meaningful implications for ticket price adjustments. 

The paper will proceed as follows. First, we present a review of relevant fields of literature this paper contributes to. Second, we discuss our data collection strategy and present relevant summary statistics.  The third section overviews our empirical strategy and assumptions for identification, and the fourth section showcases our results. Finally, the paper concludes. 

#### **1.1. Literature Review** 

This work falls into several important strains of literature. First, there has been a large amount of research in hedonic pricing, which attempts to value specific, nonmarket attributes of goods. Second, it contributes to the literature on dynamic pricing and strategic interactions among buyers and sellers in secondary ticket marketplaces. Finally, several academic papers have examined the impact of superstars in different labor contexts, especially sports, suggesting that quality and popularity of players are important factors for spectators. These papers examine superstar athlete impacts on a variety of metrics, including attendance, player salaries, and broadcast audiences. We extend all of this literature by (1) evaluating the marginal value of a superstar to an NBA game attendee by looking at ticket price movements in a secondary ticket marketplace, (2) testing heterogeneous, matchup-specific factors that may impact the marginal loss in value associated with a superstar absence, and (3) leveraging unique, high temporal frequency microdata on ticket prices for all NBA games in the 2017-18 season. 

#### **1.1.1. Hedonic Pricing** 

The literature on hedonic pricing aims to understand and estimate the relative value of each attribute of a good. The theory of hedonic pricing was developed in [10], which was the first paper to describe the total value of a good as a combination of the values of its attributes. There have been numerous empirical papers attempting to price attributes in different settings, from vehicles ([11][12]) to air quality ([13][14]) to real estate [15]. These papers use data on similar products with varying attributes of interest in an attempt to estimate a marginal value of these attributes. Our paper contributes to this literature by being the first to look at a hedonic component of event ticket values, namely the marginal contribution of a superstar player to the value of attending an NBA game. Additionally, compared to hedonic papers written to date, this paper is able to utilize rich microdata with substantial variation in potentially confounding factors (e.g. competitiveness of opponents, market size, etc.). 

#### **1.1.2. Dynamic Pricing in Secondary Ticket Marketplaces** 

The second relevant strand of literature includes work on pricing in secondary ticket marketplaces. Early research on dynamic pricing in these marketplaces borrowed from the literature on airline ticket pricing, suggesting that consumers often learn new information about their demands over time, which may be an important reason for the existence of both primary and secondary ticket marketplaces [16]. Additionally, the dynamic pricing nature of secondary ticket marketplaces allows for real-time updating of preferences of both consumers and producers, which may lead to real-time price changes in response to realized information about an event [17]. Our research 



2019 Research Papers Competition Presented by: 



3 



differs substantially from much of the previous theoretical work on pricing in ticket marketplaces in that it relies on changes in the quality of attributes of an event to determine individuals’ value for those attributes (i.e. their value for watching a specific superstar play). 

While our research builds on many of the theoretical aspects of ticket pricing, it takes a primarily empirical approach. The seminal empirical paper in this field explaining dynamic pricing patterns using secondary ticket marketplace microdata is [18]. [18] develops a game-theoretic framework to discuss the dynamics of buyer-seller interactions on secondary marketplaces as a matchup gets closer. Similar to our research, [18] finds that much of the buying and selling activity in marketplaces, including price adjustments, occurs in the few days before an event. A different paper uses microdata from a secondary ticket marketplace to assess seller dynamics on ticket resale markets, finding that there is a great deal of heterogeneity in seller pricing strategies [19]. Most notably, this work finds that 40% of sellers have a “negative scrap value” (i.e. if their ticket does not sell, they have a zero or negative value associated with attending the game) and 20% of sellers value their tickets above the franchise’s face value. Thus, if we do observe negative price effects associated with the announcement of a superstar absence, it may reflect a lower bound. This is because sellers who do not adjust still have a weakly negative value associated with this announcement, but may face transaction costs that are too high or fall victim to the “sunk cost fallacy.” 

#### **1.1.3. Economics of  “Superstars”** 

Understanding the interest in and impact of superstars began with [20], which developed a model to explain how certain talented individuals in a specific occupation are able to differentiate themselves from the rest of the pool of individuals, and obtain differentially higher salaries as a result. Interestingly, the model suggests that firm revenues have increasing marginal returns to talent, and the attraction of a superstar can have large implications for firm profits. An expansion of this work attempted to differentiate between the “popularity” and “skill” of a star performer; namely there may be a premium for watching a player with average talent, but who is quite popular for other reasons [6]. This effect is confirmed in a later study, which finds a much larger impact on game attendance for “popular players” (those that received All-Star votes) than for “skill players” (those that were ranked the highest in the top statistical performance categories) [8].  Our work synthesizes nicely with these findings, especially in the context of the NBA where “popularity” and “skill” may not be perfectly correlated. 

Other papers have extended and applied this analysis to the NBA. The first empirical paper to analyze the effect of superstar players in the NBA looked at their effects on attendance and television viewership [21]. They find substantial impacts for these players, especially in the case of away games, where fans in those markets were enthusiastic to watch these superstars when they came to town. A different paper conducted a more comprehensive analysis by estimating the marginal effect of one additional All-Star vote on increases in away-game attendance, finding that for top All-Star vote-getters this can lead to thousands of additional tickets sold annually in away arenas [7]. Most recently, researchers conducted a comprehensive analysis examining the effect of superstars on attendance at both home and away games, using attendance data for every NBA game from 1981-2014, finding that there is significantly higher attendance at both home and away games when a superstar player is present [22]. 





2019 Research Papers Competition Presented by: 

4 



## **2. Overview of Data Collection and Characteristics** 

This project leverages unique, high temporal frequency microdata from a secondary ticket marketplace, as well as data on exact timing of injury announcements for different players. This section (i) describes our data collection and organization methodology for both of these sources of data, and (ii) presents high-level summary statistics of this data. 

#### **2.1. Data Collection** 

#### **2.1.1. Secondary Ticket Marketplace** 

An integral component of this project was collecting ticket-listing data from a large, online secondary ticket marketplace that offers tickets for events ranging from concerts to sporting events. Our analysis relies on the use of such a marketplace since sellers and buyers can react instantaneously to announcements about player absences. 

We accessed this data by routinely querying a REST (Representational State Transfer, a protocol built on-top of the standard web protocols) service provided by the secondary ticket marketplace every 30 minutes (or a total of 48 collections per day) for every remaining NBA matchup in the season.<sup>7</sup> For each ticket listing, we collected metadata on the NBA game itself (e.g. home and away teams as well as date and time of matchup), data on the listing characteristics (listing price, quantity available, and a listing identifier), and identifiers for the time of data collection. The data was then fed into an ETL (Extract-Transform-Load) pipeline, which took our raw data and stored it into a set of CSV (Comma-Separated-Value) files. With this data, we had adequate snapshots for observing price changes at relatively fine time granularity before and after superstar absence announcements. 

#### **2.1.2. Absence Announcements** 

We utilize a popular fantasy basketball website to access injury and other reports for all players. This website provides regular updates on announcements from teams regarding player absences. The web page was formatted in a table manner, so we wrote a program that automatically converted the HTML tables into CSV style tables. 

Once we collected all of the announcements (including their date and time) for each player, we did some initial filtering. First, we only collected data for players ranked in ESPN’s “Top 100 NBA Players” rankings as announced prior to the start of the season [23]. This was important since we did not know who would be All-Stars at the start of the season (but could reasonably assume the top 100 rankings would contain all of the eventually selected All-Stars). Next, announcements with keywords that signaled the announcement was recapping a player's performance (e.g. rebound, points, assists) were removed. To determine announcements pertaining to absences, we manually searched for key phrases that are commonly used in announcements when a player misses a game. 

7 A REST service is an HTTP-backed protocol that defines a set of rules for querying, updating, adding, and deleting data on a website. The REST protocol is how a website can securely expose its database without giving everyone unlimited control over the data. 



2019 Research Papers Competition Presented by: 



5 



These include phrases such as “will not play” and “will not suit up.” Such phrases are absolute statements, used only when a player is guaranteed to miss a game. Furthermore, they are future tense, indicating that they occurred before the missed game and were not describing a game the player had already missed. Once an announcement was determined to represent a player absence, our parser classified the reason for the absence as “injury”, “rest”, “personal,” or “other,” again using keywords from the announcement description. 

Once an announcement was classified, we had to determine the game corresponding to an absence announcement. Manually inspecting the announcements, we determined that announcements indicating a single absence or the first absence in a string of absences are never made earlier than a single game in advance. Therefore, the first game a player’s team played after an absence announcement was considered to be the corresponding game missed. Because there were often multiple absence announcements indicating that a player will miss a game, we had to determine which of these announcements occurred first. Once all announcements were cataloged by player, and then by date of the game they referred to, we chose the earliest announcement from each group of announcements that referred to the same game. After this parsing process, these announcements were combined into a dataset where each row included the player the announcement referred to, that player’s team, the text of the announcement, the main reason parsed from the announcement (e.g. “injury”), and the announcement date and time. 

#### **2.1.3. SQL Database Creation** 

To easily search and download relevant ticket data, the ticket data stored in CSV files was put into an SQLite Database using Python. Each observation in this database represented a specific ticket listing from a specific collection time, and included all relevant ticket characteristics (listing price, quantity of tickets available, seat and matchup characteristics). We also included an indicator variable representing whether a star player absence occurred for the game corresponding to the specific observation, a variable indicating the name of the star player (or players) that were absent, and finally a variable indicating whether or not the announcement had occurred for a specific game at the time corresponding to each observation. While we collected data on every future NBA matchup starting from the beginning of the NBA season, we only included data beginning three days prior to each matchup in the SQLite database, since this was the time period over which almost all player absence announcements would be relevant in affecting ticket prices. 

#### **2.2. Summary Statistics** 

#### **2.2.1. Secondary Ticket Marketplace Data** 

A summary of relevant variables collected from the secondary ticket marketplace microdata is presented in Table 1 below. It should be noted that these are the primary summary statistics of the per-game _averages_ for the continuous variables (listing price and quantity per listing), and the pergame _counts_ for the count variables (number of observations, listing IDs, section IDs, and collection IDs). We have data from 1,145 NBA matchups, corresponding to 93% of the total number of games 





2019 Research Papers Competition Presented by: 

6 



played in an NBA season (1,230).<sup>8</sup> The “Listing Price” refers to the price posted by a seller for a specific listing. The “Quantity per Listing” denotes the number of seats available in a specific listing posted by a seller. The “Listing ID” is a unique listing-specific identifier, the “Collection ID” is a unique identifier corresponding to when the data was collected (i.e. each 30 minute collection gets a unique identifier), and “Section ID” corresponds to the section of the arena the listing is located in. Finally, “Number of Observations” corresponds to the number of unique listing-by-collection ID data points for each matchup. 

**Table 1.** Across-Game Summary Statistics (1,145 Total Matchups) 

|**Data Characteristics**|**Mean**|**Standard**<br>**Deviation**|**Minimum**|**Maximum**|
|---|---|---|---|---|
|**Number of**<br>**Observations**|34,569.35|23,767.05|70|216,851|
|**Listing Price**|$152.06|$102.85|$12.74|$988.10|
|**Quantity per Listing**|3.45|0.75|1.97|5.63|
|**Listing IDs**|611.68|398.59|28|3,133|
|**Collection IDs**|116.98|28.68|4|139|
|**Section IDs**|108.97|35.67|18|217|



Table 1 shows that there is an average of 117 collection times for each matchup, which corresponds to approximately 58.5 hours prior to each matchup. We observe an average of 611 unique listings per matchup across an average of 109 different arena sections. The average per-matchup listing price is $152 with a quantity per listing of nearly 3.5. 

Because of the high temporal frequency of our microdata, we can observe the time trends of average listing price and quantity of tickets posted to a secondary marketplace for each matchup. Figure 1 below presents three different quantity time trends in terms of “hours to game”: the top pane presents the average total quantity of tickets available on the secondary marketplace for each matchup, and how this evolves as the matchup approaches. The second pane presents the average number of tickets _added_ (i.e. posted by sellers) to the marketplace per matchup as the game approaches, and the third pane the average number of tickets _sold_ on the marketplace per matchup as the game approaches. It should be noted that we assume the disappearance of a listing on the marketplace implies that this listing was sold, either to a buyer or to the “seller” of the listing who 

8 Reasons for missing data for certain matchups include server restarts and changes of event-names mid-season on the secondary ticket marketplace that were not automatically identified by our data collection program. 





2019 Research Papers Competition Presented by: 

7 



decided to go themselves.<sup>9</sup> One can see that the quantity of tickets available for a given matchup declines as the matchup approaches. This is intuitive, as these tickets represent a “perishable good” and have no value once a matchup is completed. Interestingly, the average number of tickets posted (added) to the marketplace is somewhat uniform in terms of hours to game (with the exception of dips during night-time hours when most sellers and buyers are asleep), but the average number of tickets sold spikes in the 10 or so hours before a game. 



**Figure 1.** Per-Game Average Number of Active, Added, and Sold Listings by Hours to Game<sup>10</sup> 

Additionally, Figure 2 plots the average listing price across all matchups by hours to game. One can see that there is generally a downward trend in prices as a matchup approaches, decreasing from around $145 two days before a matchup to around $110 just before game-time. One can also see that the volatility in prices substantially increases as game-time approaches. This can be attributed to an increase in activity on the marketplace – there are matchups where sellers may be trying to get rid of tickets and continuing to lower prices, and other matchups where buyers are trying to obtain tickets, causing remaining sellers to increase their prices. In both situations, agents are entering and exiting the marketplace at a much higher frequency in the 10 or so hours before a matchup. 

9 In other words, a seller may have their tickets purchased by another buyer, or decide to “purchase” their own tickets (i.e. remove the listing and go to the game themselves). 10 Please note different scale of y-axis for each pane. 





2019 Research Papers Competition Presented by: 

8 





**Figure 2.** Average Listing Price by Hours to Game 

#### **2.2.2. Player Absence Announcement Data** 

The second strain of our collected data is the timing of player absence announcements. Figure 3 presents the distribution of announcements of ESPN’s top 100 players [23] in terms of hours to game. Therefore, each player-announcement combination is presented here, of which there are 677 total. 





2019 Research Papers Competition Presented by: 

9 





**Figure 3.** Distribution of Player Absence Announcements by Hours to Game 

One can see that most of the announcements occur within 10 hours of a game, some coming as close as a few minutes beforehand. This inherently limits our sample size of games that can be analyzed, since we need an adequate timeframe pre- and post-announcement to witness ticket price changes. Many announcements also occur approximately 24 hours prior to a game, which may be the result of a player experiencing an injury during the first game of a back-to-back, or an injury that does not require a “game-time decision.” There are also noticeable dips in announcement counts 12-20 hours prior to a game because these times often fall during the middle of the night. Rarely do announcements for a player absence for a specific matchup occur more than 36 hours prior to a game.<sup>11</sup> 

Once we observed which players were selected to the All-Star team, we narrowed down our list of ESPN’s top 100 players to All-Star players. Table 2 below presents the names of each of these players, how many “qualifying” games they missed (i.e. an explicit announcement within 3 days of a matchup indicating the exogenous nature of a player’s absence) as a result of injury, rest, or “other” reasons, the total number of qualifying games, and the number of qualifying games for each player that was included in our analysis on ticket price changes. 

11 As mentioned previously, our analysis does not consider the effect of a long-term injury announcement on games more than 3 days into the future. 



2019 Research Papers Competition Presented by: 



10 



**Table 2.** Count (by Reason) of “Missed-Game” Announcements for each All-Star Player 

|**Player**|**Injury**|**Rest**|**Other**|**Total**|**Total Analyzed**|
|---|---|---|---|---|---|
|**Al Horford**|7|3|0|10|10|
|**Andre Drummond**|4|0|0|4|3|
|**Anthony Davis**|7|0|0|7|6|
|**Chris Paul**|13|1|0|14|10|
|**Damian Lillard**|7|0|1|8|7|
|**DeMar DeRozan**|0|2|0|2|1|
|**DeMarcus Cousins**|1|0|0|1|0|
|**Draymond Green**|11|1|0|12|10|
|**Giannis Antetokounmpo **|6|0|0|6|5|
|**Goran Dragic**|7|0|0|7|6|
|**James Harden**|2|2|0|4|4|
|**Jimmy Butler**|9|0|0|9|5|
|**Joel Embiid**|6|3|0|9|0<sup>12</sup>|
|**John Wall**|10|2|0|12|9|
|**Kemba Walker**|2|0|0|2|2|
|**Kevin Durant**|11|0|0|11|9|
|**Kevin Love**|3|1|0|4|1|
|**Klay Thompson**|3|1|0|4|4|
|**Kristaps Porzingis**|7|0|0|7|6|
|**Kyle Lowry**|3|1|0|4|4|
|**Kyrie Irving**|11|0|0|11|8|
|**LaMarcus Aldridge **|3|3|0|6|0<sup>13</sup>|
|**Paul George **|3|0|0|3|1|
|**Russell Westbrook**|2|0|0|2|1|
|**Stephen Curry**|11|0|0|11|8|
|**Victor Oladipo **|7|0|0|7|7|



For each All-Star player, we are able to analyze most, if not all, of the qualifying games they were absent for. Reasons for not being able to analyze certain qualifying games include if the announcement occurred “too close” to the matchup, missing ticket price data as a result of server restarts or event-name changes on the secondary marketplace, or if another superstar was announced as out for that qualifying game as well. 

12 We do not examine matchups where Joel Embiid was absent for two primary reasons. First, there are potential confounding issues between the Philadelphia 76ers and the secondary marketplace data we have access to. Secondly, Joel Embiid did not play in the second night of all back-to-back games, and thus those announcements were not plausibly exogenous. 

13 We do not examine matchups where LaMarcus Aldridge was absent because of the season-long uncertainty surrounding Kawhi Leonard’s playing status in San Antonio, likely confounding many if not all of the matchups he was absent for. 





2019 Research Papers Competition Presented by: 

11 



## **3. Empirical Methodology** 

Our primary empirical strategy relies on a modified generalized difference-in-differences (DID) framework, where we aim to identify the causal effect of a specific superstar’s absence on ticket prices. Under important assumptions regarding identification, these estimates represent the marginal value of each superstar’s presence in a game. This framework relies on a plausibly exogenous “announcement” of a player’s absence for an upcoming game, at which point ticket prices for that game should respond according to the missing player’s value. 

#### **3.1. Constructing the Counterfactual Group** 

To obtain a more accurate (and plausibly causal) effect of ticket price responses to a player’s absence, we must construct a counterfactual group that models ticket price movements _without_ a player’s absence, and compare those movements to our “treated” games, where a specific superstar player is announced to be out. This is important because there could be underlying trends in ticket prices for NBA games that may bias our estimate of a player’s absence if not controlled for by selecting an appropriate counterfactual. There are several different ways one may consider doing this—for example, we could use ticket listings from all other games on the same day and compare their price movements to ticket listings for the treated game on that day. We call this the _same day counterfactual_ . There are both pros and cons to this method. On one hand, we are comparing games that occur during the same point in the season. On the other hand, there are a different number of games each day, which could limit the size of the counterfactual group, as well as completely different teams and markets involved each day. 

A second way of constructing a counterfactual is what we call the _same team counterfactual_ . This counterfactual compares games for the team of a specific superstar where that superstar was absent, to other games of that specific team not confounded by _any_ superstar absences. For example, Golden State Warriors guard Stephen Curry missed the game on December 6, 2017 against the Charlotte Hornets in Charlotte. Our counterfactual would consist of a subset of other Golden State Warriors games where Stephen Curry played _and no other superstar players were announced to be absent_ .<sup>14</sup> The game where forward Kevin Durant was announced out due to injury against the Brooklyn Nets in Brooklyn on November 19, 2017 would not be included in this subset of potential counterfactual games. We prefer this counterfactual for our analysis since it allows us to control for “team-specific” trends of ticket prices and their movements that may be common across many of their games, which we believe to be more valuable than the controls allowed by the _same day_ counterfactual. 

#### **3.2. Primary Estimating Equations** 

Our analysis estimates both a simple DID as well as a generalized DID for each superstar player. Using the same-team counterfactual, the simple DID estimating equation is written as follows: 

14 This only includes “qualifying games” for other superstars, as defined in our “Data” section. Namely, we _do_ include games that another superstar may have missed, but that weren’t explicitly announced (for example, if another superstar was known to be out for the rest of the season prior to the treated game being analyzed). 





2019 Research Papers Competition Presented by: 

12 

log (𝑃𝑟𝑖𝑐𝑒!"!) = 𝛽!𝐴𝑏𝑠! + 𝛽!𝑃𝑜𝑠𝑡_𝐴𝑛𝑛! + 𝛽! 𝐴𝑏𝑠∗𝑃𝑜𝑠𝑡_𝐴𝑛𝑛 !!<sup>+ 𝛼</sup> !<sup>+ 𝛼</sup> !<sup>+ 𝜖</sup> !"! (1) 



where 𝑃𝑟𝑖𝑐𝑒!"! represents the average listed price for tickets in section 𝑠 for matchup 𝑖 at hours-togame ℎ. So, an observation for the left-hand side variable would be the average listed price of tickets in section 201 for the Golden State Warriors vs. Houston Rockets matchup on October 17, 2017 listed on October 17, 2017 four hours before the game. 𝐴𝑏𝑠! is a binary variable = 1 if there was a superstar absence for matchup 𝑖, and 𝑃𝑜𝑠𝑡_𝐴𝑛𝑛! is a binary variable = 1 if the announcement had already been made at hours-to-game ℎ. We use hours-to-game as our measure of time since matchups occur at different times during the day (e.g. 7:30pm EST or 10:30pm EST) and across days (e.g. October 16<sup>th</sup> vs. October 17<sup>th</sup> ). Additionally, average ticket price trajectories are heavily dependent on the number of hours before game-time, as quantity of tickets available and prices on the secondary marketplace are very time-dependent (see Figures 1 and 2). Thus, for the Golden State Warriors @ Brooklyn Nets matchup on November 19, 2017, Kevin Durant was announced out of the game at 8:49am EST, which would correspond to 6 hours and 11 minutes to the game (which was at 3:00pm EST). The DID treatment coefficient is represented by 𝛽!, which approximately represents the percentage change in ticket prices associated with a superstar absence, and is our primary coefficient of interest.<sup>15</sup> Finally, 𝛼! represents section fixed-effects (which are matchupspecific as well) and 𝛼! is an hours-to-game fixed effect. We prefer to use a log-level specification since prices cannot fall below zero, and thus the distribution of prices is censored. We also prefer to interpret the effect of a player absence on the percentage change in listed prices. 

Because we are attempting to determine a causal impact on ticket prices associated with a superstar absence, we run a generalized DID model to i) confirm parallel pre-trends in ticket prices for the treatment and counterfactual matchups, and ii) to determine the effect of a superstar absence on ticket prices in each time-period following the announcement (instead of just a postannouncement versus pre-announcement average effect that is obtained by the simple DID). Therefore, still using the same-team counterfactual, our primary empirical specification can be written as follows: 



𝑨𝒃𝒔𝒆𝒏𝒄𝒆!,!! is a vector of binary variables indexed by event-time 𝑡. Event-time 𝑡 is in the hours-togame unit, but is normalized to 𝑡= 0 based on the hours-to-game value when the announcement of a superstar’s absence takes place. As is standard in studies with generalized DID estimations, each variable takes a value  = 1 if the observation in the data refers to a matchup 𝑖 where a superstar was absent and the observation of data corresponds to event-time 𝑡. 𝑫! is a vector of estimated coefficients distinguishing the price differential between the treated game and counterfactual games at event-time 𝑡 compared to an omitted period (which for our analysis will correspond to 

15 In any log-level regression, the coefficients represent a “log-point” change, but for reasonably small coefficient values, these can be approximated as percent changes. 





2019 Research Papers Competition Presented by: 

13 



𝑡= −1). As can also be seen in the estimating equation, we restrict our event-time horizon to 𝑡= [−7, 7], where the left (right) binned endpoint coefficient represents the average treatment effects for all pre- (post-) periods. The dependent variable and fixed-effects remain identical to the simple DID estimating equation. 

In addition to estimating an effect for each individual matchup that experienced a superstar absence, we also sought to estimate an aggregate absence effect for each superstar, which required a slightly more complex method of constructing the same-team counterfactual. Because each “treated” matchup for a specific player has a different announcement time in terms of hours-togame, we cannot simply assign the same announcement time to all matchups in the counterfactual as we did in the individual matchup case. Rather, we randomly assign announcement times for all matchups in the counterfactual sampling from the pool of announcement times observed for the treated matchups. For example, Giannis Antetokounmpo was absent from five matchups (11/22/17, 12/23/17, 1/20/18, 3/23/18, and 4/7/18) and was announced absent for these matchups at 5, 1.5, 29.5, 9, and 2 hours-to-game, respectively. For each of these 5 treated matchups, we randomly pair a proportional number of counterfactual matchups based on the total set of eligible counterfactual matchups for the Milwaukee Bucks, and assign the announcement time (in hours-to-game) of the treated matchup to each counterfactual matchup with which it was paired. In <mark>the case of Antetokounmpo, there are 69 eligible, untreated matchups in the counterfactual group, so 4 treated matchups receive 14 counterfactual matchups each and the remaining treated matchup receives 13 counterfactual matchups.</mark> Once the pairings are assigned, we assign the same announcement time to the group and then normalize the announcement time of each grouping to 0. Finally, we merge groups into a single table for the given player on which we can then perform the estimation. The estimating equations remain the same as in the case of the individual matchup analysis with one key difference – for matchups in the counterfactual, 𝑃𝑜𝑠𝑡_𝐴𝑛𝑛! is determined based on the assigned announcement time within each grouping. To ensure robustness of the random counterfactual matchup-pairing algorithm, we perform the aggregate-matchup analysis for each player 3 times, each with a different random counterfactual pairing. 

Another important consideration in our analysis is that our estimations only look at the effect of an absence announcement on the matchup _immediately following_ this announcement. This is to avoid several complications involved with modeling the effect of an injury announced today on a game 𝑋 weeks out, since many absence timelines are uncertain. For example, if Stephen Curry was announced to be out for 1 week (which may consist of missing several games), we only examine the game immediately following the announcement, since that game had perfect certainty that Steph would be absent, while the following games may have exhibited more complicated ticket price adjustment patterns in response to this announcement. We also narrow our data to injury and rest announcements that occur within 3 days of a game to avoid complications of long-term effects of announcements on future games (i.e., if a player tears their ACL this impacts not just the next game, but all remaining games in the season), to avoid heavy computational burden, and to reduce the number of team-specific confounding factors (like team records in each matchup, changing playoff probability of teams, etc.). It is also the case that most of the action in the secondary ticket marketplace for a specific matchup occurs in the few days before the matchup. 

Finally, it is important to note that we are using _listed_ prices for this analysis. While a listed price does not necessarily indicate a seller’s true willingness-to-sell (i.e. the reservation price of attending the game) since the choice of the listing price is a function of the prices of other listings of 





2019 Research Papers Competition Presented by: 

14 



comparable seats, _changes_ in listed prices due to superstar absences should reflect the combined effect of sellers’ and buyers’ lower value of attending the corresponding matchup. Therefore, the effect we estimate is the net marginal loss associated with the absence of a specific superstar for the average NBA game attendee. 

#### **3.3. Identification Concerns** 

With any empirical estimation, there are concerns over identification of a causal estimate. In our estimation, we are generally worried about omitted variables correlated with announcements that also affect ticket prices, namely: 



where 𝑿𝒊𝒔𝒉𝒕 represents the vector of covariates controlled for. However, because injury announcements are random (the occurrence of an injury is not predictable), and we only look at price movements 3 days prior to a matchup, we are only worried if something else occurs that causes an adjustment of the price trajectory of a treated game differently than counterfactual games. One potential threat to identification is if an absence announcement of a player is correlated with having already made the playoffs and their team’s seeding set. This may occur if the propensity to sit a superstar due to injury is higher once a team’s playoff seeding is already set. In this case, it would be difficult to untangle the price effect associated with a team having already made the playoffs and determined their seeding, and the price effect due to the injury of a superstar player. 

While it is difficult to imagine important identification issues with respect to injury announcements, announcements about superstars resting may face more serious concerns. First, decisions to rest superstar players may be dependent on several factors, for example the second night of back-toback games or fourth game in five nights may exhibit a higher likelihood of superstars resting (e.g. Joel Embiid all of last year), competitiveness of the opponent, home vs. away games, etc. Future work will attempt to more rigorously examine rest announcements once controlling for important factors. A very valuable project may be to develop a predictive model that can explain the likelihood of rests to occur given a vector of meaningful covariates. 

#### **3.4. Future Work: Synthetic Controls** 

Our primary empirical methodology relies on building what we describe above as the _same-team counterfactual_ . However, given that we have incredibly rich temporal data as well as a limited— though useful—set of covariates (e.g. team records, number of superstars playing in each matchup, etc.), a promising future empirical approach is the use of synthetic controls. One drawback from the current analysis is that we cannot explicitly force the treated and counterfactual groups’ pretreatment trends in ticket prices to be parallel. We only observe in the generalized DID framework whether or not the pre-trends do indeed satisfy the parallel condition. However, a synthetic control 





2019 Research Papers Competition Presented by: 

15 



approach would impose a weighting scheme for counterfactual games that _requires_ pre-treatment prices between the two groups to follow the same trends.<sup>16</sup> 

Following [24], we will use the high temporal frequency microdata on ticket prices to create a synthetic control counterfactual, which minimizes the mean squared prediction error of the outcome variable during the pre-announcement period. The synthetic control—by definition, a composite of covariates and pre-intervention outcomes—will largely be created through the weighting of various _same-team_ matchups that most closely align with the treated game before the announcement. Thus, instead of having to choose an appropriate counterfactual for each player’s missed game, the synthetic control approach would generate a counterfactual that similarly resembles the treated game’s pre-announcement ticket price trend. 

## **4. Results** 

In this section, we present our findings for the simple difference-in-differences (DID) estimation, the generalized DID estimation, and tests of heterogeneity of superstar absence impacts in home vs. away games and depending on the market size of the home team. 

#### **4.1. Simple Difference-in-Differences** 

Figure 4 below presents the results of our simple DID estimation as seen in equation (1). This figure measures the average percent change in ticket prices across all games a specific superstar is absent for. There are several important elements to note with these results. First, these results only include players where pre-trends in ticket prices between the counterfactual and treated matchups prior to a superstar’s injury announcement were parallel, satisfying the identifying assumption that the DID estimate is causal. Secondly, each of these estimates represents the results from the _aggregate_ estimation.  Therefore, each estimate reflects the average effect on listed ticket prices from all analyzed games for each of the qualifying superstars. In examining the results, one can see that the reduction in prices due to absence announcements of players like Kemba Walker, Kyrie Irving, and Anthony Davis result in a statistically significant decrease in listed ticket prices.<sup>17</sup> Additionally, Stephen Curry exhibits an economically meaningful effect of approximately an 8% reduction in ticket prices due to his absence that is nearly statistically significant at the 10% level. 

> 16 The _Synth_ package in _R_ conditions on both pre-treatment trends and levels, so we will have to normalize our outcome variable (price) such that the initial binned period imposes that prices are normalized to be equal between the treatment and counterfactual groups. Then in all future periods, the matching of the counterfactual games with treated games occurs exclusively on trends in the pre-period, since we force price levels to be matched initially. 17 90% confidence intervals used here. 





2019 Research Papers Competition Presented by: 

16 





**Figure 4.** Difference-in-Difference Results for Superstar Absences (Percentage Change in Prices) 

Figure 5 exhibits these declines in _level_ price reductions instead of percentage terms. One can see that because the average price of Golden State Warriors tickets is quite high, Stephen Curry’s absences have the largest magnitude decrease on ticket prices. One can also see that many superstar players have statistically insignificant and/or economically small impacts due to their announcements. Most notably, 2017-18 MVP James Harden and 2013-14 MVP Kevin Durant exhibit no statistically significant reduction in prices associated with their absences. 





2019 Research Papers Competition Presented by: 

17 





**Figure 5.** Difference-in-Difference Results for Superstar Absences (Level Change in Prices) 

One can put these estimates into a welfare context with some back-of-the-envelope calculations. For example, Stephen Curry’s average impact on prices for games he is absent for is approximately $25. If each attendee for Golden State Warriors games loses $25 when Stephen Curry is absent, and there are on average 20,000 fans in an NBA arena for these games, and 82 Golden State Warriors games in an NBA season, then the total value of watching Stephen Curry play in person to NBA fans is $25 x 20,000 x 82 = $41,000,000. Interestingly, Stephen Curry’s current contract pays him an average of $40,231,758 per year through the 2021-22 NBA season [25]. It should be noted we are not claiming that the sum of a player’s per-game absence effect is representative of their net worth – there are several other factors that likely make Stephen Curry much more valuable to the NBA and Golden State Warriors than $41,000,000 annually (which is the maximum salary the Golden State Warriors could offer Stephen Curry). However, the sum of these absence effects may indicate these players’ values to the average NBA game attendee – in other words, a player’s combined entertainment and competitiveness value to fans at a game. 

#### **4.2. Generalized Difference-in-Differences** 

The generalized DID results present coefficients for each of the 30-minute intervals before and after an absence announcement takes place. Figure 6 shows the generalized DID results for the top four 



2019 Research Papers Competition Presented by: 



18 



impact players with respect to ticket price declines as a result of their absences, again using the aggregate estimation.<sup>18</sup> One can interpret each of the points on this graph as the differential effect on listed ticket prices of a superstar absence announcement on the treated group vs. the counterfactual group. Coefficients statistically insignificantly different from zero prior to an absence announcement, which is indicated by the vertical red line, suggest that parallel pre-trends in ticket prices hold in each of these players’ cases. The generalized DID estimation allows us to observe when prices change as a result of an announcement. One can see that there is a slight delay in the responsiveness of listed ticket prices to the announcement of a superstar’s absence – typically the effects begin to happen 3-6 hours after an announcement is made. This is intuitive, as many sellers and buyers do not have immediate access to announcement information or the ability to immediately change their listing on the secondary marketplace. We bin our endpoints at -7 and +7 hours in event-time with respect to when the announcement occurs (at t=0). 









**Figure 6.** Generalized Difference-in-Differences Results for Top Impact Superstars 

In Figures 4 and 5, we see that Kevin Durant’s absence announcements on average lead to no statistically significant ticket price adjustments. This is particularly interesting given that we find a meaningful reduction for his teammate Stephen Curry’s absences, especially when considering that the simple DID does not account for the eventual statistically significant effect exhibited for Stephen Curry 6+ hours after his absence announcements. Figure 7 below presents the generalized DID results for Kevin Durant and Stephen Curry. From a skill standpoint (measured by player efficiency rating or value over replacement player), Kevin Durant and Stephen Curry were nearly identical during the 2017-18 season. However, Curry’s popularity effect with NBA fans as “the best shooter 

18 The generalized DID results for the remaining eligible players are presented in the Appendix. 





2019 Research Papers Competition Presented by: 

19 



of all-time,” his unique ability to make impressively difficult three-pointers, and his style of play all may make him a more desirable player to watch from an entertainment standpoint. 





**Figure 7.** Stephen Curry vs. Kevin Durant Absence Impact on Listed Prices 

Finally, we conduct analysis examining only the subset of tickets that are actually _sold_ on the marketplace. There are potential advantages in using just these listings in our estimation of superstar player absence impacts, namely that they represent an actual market-clearing price associated with a ticket. Figure 8 replicates the analysis shown in Figure 6 using only these sold listings. One can see that the results are even more suggestive of price declines associated with absence announcements for these high-impact superstars. 









**Figure 8.** Generalized Difference-in-Differences Results for Top Impact Superstars (Sold Listings) 





2019 Research Papers Competition Presented by: 

20 



#### **4.3. Heterogeneity Tests** 

Our final set of analyses examines heterogeneity with respect to types of games superstars are absent for. We present two sets of analyses here – first we examine the difference in the absence effect on ticket prices differentially for home game absences vs. away game absences for each qualifying player. Next, we examine the impact of market size of the home team on the absence effect of each qualifying superstar player. 

Figure 9 below presents two distinct DID estimators for each player: one for home games missed and another for away games missed. One can see there are some striking differences in effects for certain players. For example, Kevin Durant’s absence effect is statistically significantly different and much more negative for away absences than for home absences. Stephen Curry exhibits a similar result, albeit even larger in away arenas at a greater than 20% reduction in the average price. This suggests that the value of these players in away arenas is higher than in their home arena, likely because a) they only play in opposing arenas at most two times per year, b) Golden State Warriors home fans may be used to seeing them play at home, and c) the Warriors remain an extremely competitive and entertaining team without one of these players on the court. On the other hand, Kristaps Porzingis and Anthony Davis both exhibit the opposite effect, where their absences are much more meaningful for home games than for away games. This is also quite intuitive – both of these players are not just entertaining to watch, but without them their teams become much less competitive and much more likely to lose a game. Home fans value the competitiveness of their team, and thus the absence of one of these players both removes the star element from their team and substantially reduces their team’s chances of winning. 





2019 Research Papers Competition Presented by: 

21 





**Figure 9.** Difference-in-Differences Estimator by Home vs. Away Matchup Absence 

The next heterogeneity test analyzes the additional impact of market size of the home team on a superstar player’s absence effect. This analysis relies on a triple differences estimation, where we interact our DID treatment variable with market size of the home team. The results of this analysis are presented in Figure 10. One can interpret the triple difference estimator as follows: for every $1 million increase in the market size of the home team, the absence effect for superstar player “Y” changes by XX%. To put a $1 million change in perspective, the average market size of teams in the NBA is $1.65 billion [26]. One can see from the figure below that for many superstars, absences in larger markets do not have as large of an impact on prices (i.e. a positive triple-diff coefficient indicates that prices respond less negatively to absence announcements in larger markets). This makes intuitive sense as well – larger markets typically have more established fan-bases, and these markets typically garner fan support no matter the competitiveness or level of star-power of their team (or the opposing team). Anthony Davis exhibits the largest impact (which is also in agreement with Figure 9, since his home market of New Orleans is the smallest in the league and he has a significantly more negative absence effect for home games), and players like Kristaps Porzingis, Kevin Durant, and Stephen Curry also exhibit statistically significant impacts. 



2019 Research Papers Competition Presented by: 



22 





**Figure 10.** Triple Differences Estimator by Market Size of Home Team 

## **5. Conclusions** 

This paper presents an analysis of the entertainment value of NBA superstars to fans attending NBA games. Our findings suggest that absences of several superstars, including some of the most popular like Stephen Curry, Kyrie Irving, and Anthony Davis, do have a statistically significant and economically meaningful impact ranging from a 7-25% ($9-$25) reduction in the average ticket price. This implies hundreds of thousands of dollars in welfare lost for each of these matchups, and millions of dollars lost across all superstar absences over the course of a season. However, there are many slightly less popular, yet highly skilled superstars (e.g. Damian Lillard, Kristaps Porzingis, and James Harden) whose absences do not cause a meaningful reduction in listed ticket prices. We conduct additional heterogeneity tests examining the differential in superstar absence effects for home vs. away absences, as well as the absence effect when games are played in small versus large markets. We find that certain players, like Stephen Curry and Kevin Durant, exhibit much larger away game absence effects, while Anthony Davis and Kristaps Porzingis experience much larger home game absence effects. Games played in larger markets also appear to reduce the magnitude of the absence effect of superstars. 



2019 Research Papers Competition Presented by: 



23 



Our findings have significant ramifications for the NBA and decision-making of franchises. First, this study provides quantitative evidence that there are significant reductions in welfare of NBA fans due to certain superstars missing games. The NBA may want to consider the importance of its policies surrounding timing of injury announcements (and how far in advance they need to be made), purposeful resting of players, and implications of suspensions (versus simply fining players) for welfare of NBA fans. For example, it appears that smaller markets suffer more from absences of NBA superstars, and so policies that penalize teams differentially for resting players in smaller markets versus larger markets may want to be considered. There are also important implications of this study for decision-making by NBA franchises. For instance, franchises may want to set up (at the very least) simple dynamic pricing schemes in the primary marketplace that adjust to absences of the most popular superstars. In addition, when franchises are signing free agents, drafting players, or making trades, and are profit-maximizing, they may not only want to consider the skill level of these players, but also the entertainment value associated with watching them play. 

There are several avenues of future research we would like to expand upon with this work. First, as mentioned in section 3.4, we hope to apply a synthetic controls empirical approach in estimating the superstar absence effect. This will hopefully allow us to obtain causal estimates for superstars in cases where the same-team counterfactual did not produce parallel trends. Second, we hope to look at the effect of long-term injuries on ticket prices. For example, when a player tears their ACL and is guaranteed to be out for the remainder of the season, how does this affect the stream of ticket prices for all future games of this team? We may witness different results since sellers and buyers have more time to adjust and process this information. In a similar vein, we hope to explore the impact of “uncertainty” associated with some players’ timelines in returning from injury or rest on ticket prices for future, potentially impacted games. For example, LeBron James experienced a lingering groin injury during the middle of the 2018-19 season, which led to a highly uncertain timetable for his return. Furthermore, we could apply this methodology to examine ticket price impacts when a superstar player joins a new team. For instance, if there is a midseason blockbuster trade that causes one team to gain a superstar player and another team to lose that player, what happens to ticket prices for future games for these teams? Finally, we plan on conducting a more comprehensive analysis examining the difference between absences due to injury and those due to purposeful rest. 





2019 Research Papers Competition Presented by: 

24 



## **References** 

- [1] <mark>Morris, David Z. “NFL vs. NBA: Which Will Be America’s Biggest Sport 10 Years From Now?”</mark> _<mark>Fortune</mark>_ <mark>.</mark> <u><mark>http://fortune.com/2018/05/26/nfl-vs-nba-americas-biggest-sport/ (accessed</mark></u> <mark>November 21, 2018).</mark> 

- [2] <mark>Adgate, Brad. “Why the 2017-18 Season Was Great For The NBA.”</mark> _<mark>Forbes</mark>_ <mark>.</mark> <u><mark>https://www.forbes.com/sites/bradadgate/2018/04/25/the-2017-18-season-was-great-forthe-nba/#61b9f06d2ecb</mark></u> <mark>(accessed November 21, 2018).</mark> 

- [3] <mark>Knox, Bryant. “B</mark> reaking Down Why the NBA Will Always Be a Star-Driven League.” _Bleacher Report_ <mark>.</mark> <u><mark>https://bleacherreport.com/articles/1329836-breaking-down-why-the-nba-willalways-be-a-star-driven-league (accessed November 21, 2018).</mark></u> 

- [4] <mark>Heindl, Katie. “Free Agency In the New Player Narrative Driven NBA.”</mark> _<mark>RealGM</mark>_ <mark>.</mark> <u><mark>https://basketball.realgm.com/analysis/250427/Free-Agency-In-The-New-Player-NarrativeDriven-NBA (accessed November 21, 2018).</mark></u> 

- [5] Whitehead, Todd. “NBA Teams Are Resting Players Earlier And Earlier.” _FiveThirtyEight_ . <u>https://fivethirtyeight.com/features/nba-teams-are-resting-players-earlier-and-earlier/</u> (accessed November 21, 2018). 

- [6] <mark>Adler, Moshe. "Stardom and talent."</mark> _<mark>The American economic review</mark>_ <mark>75, no. 1 (1985): 208-212.</mark> 

- [7] <mark>Berri, David J., and Martin B. Schmidt. "On the road with the National Basketball Association's superstar externality."</mark> _<mark>Journal of Sports Economics</mark>_ <mark>7, no. 4 (2006): 347-358.</mark> 

- [8] <mark>Jane, Wen-Jhan. "The effect of star quality on attendance demand: The case of the National Basketball Association."</mark> _<mark>Journal of Sports Economics</mark>_ <mark>17, no. 4 (2016): 396-417.</mark> 

- [9] NBA-AllStar.com Voting. “2018 NBA All-Star Ballot – Los Angeles.” _NBA-AllStar.com_ - 

- <u>http://www.nba allstar.com/ballot/</u> (accessed November 21, 2018). 

- [10] <mark>Rosen, Sherwin. "Hedonic prices and implicit markets: product differentiation in pure competition."</mark> _<mark>Journal of political economy</mark>_ <mark>82, no. 1 (1974): 34-55.</mark> 

- [11] <mark>Busse, Meghan R., Christopher R. Knittel, and Florian Zettelmeyer. "Are consumers myopic? Evidence from new and used car purchases."</mark> _<mark>American Economic Review</mark>_ <mark>103, no. 1 (2013): 220-56.</mark> 

- [12] <mark>Sallee, James M., Sarah E. West, and Wei Fan. "Do consumers recognize the value of fuel economy? Evidence from used car prices and gasoline price fluctuations."</mark> _<mark>Journal of Public Economics</mark>_ <mark>135 (2016): 61-73.</mark> 

- [13] <mark>Currie, Janet, and Reed Walker. "Traffic congestion and infant health: Evidence from E- ZPass."</mark> _<mark>American Economic Journal: Applied Economics</mark>_ <mark>3, no. 1 (2011): 65-90.</mark> 

- [14] <mark>Chay, Kenneth Y., and Michael Greenstone. "Does air quality matter? Evidence from the housing market."</mark> _<mark>Journal of political Economy</mark>_ <mark>113, no. 2 (2005): 376-424.</mark> 

- [15] <mark>Luttik, Joke. "The value of trees, water and open space as reflected by house prices in the Netherlands."</mark> _<mark>Landscape and urban planning</mark>_ <mark>48, no. 3-4 (2000): 161-167.</mark> 

- [16] <mark>Courty, Pascal. "Some economics of ticket resale."</mark> _<mark>Journal of Economic Perspectives</mark>_ <mark>17, no. 2 (2003b): 85-97.</mark> 

- [17] <mark>Courty, Pascal. "Ticket pricing under demand uncertainty."</mark> _<mark>The Journal of Law and Economics</mark>_ <mark>46, no. 2 (2003a): 627-652.</mark> 

- [18] <mark>Sweeting, Andrew. "Dynamic pricing behavior in perishable goods markets: Evidence from secondary markets for major league baseball tickets."</mark> _<mark>Journal of Political Economy</mark>_ <mark>120, no. 6 (2012): 1133-1172.</mark> 

- [19] <mark>Clarke, Kailin. “The Gains from Dynamic Pricing for Ticket Resellers.” Chapter 2 of Doctoral Dissertation, University of Minnesota Department of Applied Economics. 2016.</mark> 





2019 Research Papers Competition Presented by: 

25 



- [20] <mark>Rosen, Sherwin. "The economics of superstars."</mark> _<mark>The American economic review</mark>_ <mark>71, no. 5 (1981): 845-858.</mark> 

- [21] <mark>Hausman, Jerry A., and Gregory K. Leonard. "Superstars in the National Basketball Association: Economic value and policy."</mark> _<mark>Journal of Labor Economics</mark>_ <mark>15, no. 4 (1997): 586-624.</mark> 

- [22] <mark>Humphreys, Brad, and Candon Johnson. “The Effect of Superstar Players on Game Attendance: Evidence from the NBA.” Working Paper, West Virginia University (2017).</mark> 

- [23] #NBARank. “#NBA Rank: Players 1-100.” _ESPN_ 

   - <u>http://www.espn.com/nba/story/_/page/nbarank110/nbarank-players-1-10</u> (accessed November 21, 2018). 

- [24] <mark>Abadie, Alberto, Alexis Diamond, and Jens Hainmueller. "Synth: An r package for synthetic control methods in comparative case studies." (2011).</mark> 

- [25] Spotrac. “Stephen Curry Current Contract.” _spotrac.com_ 

   - <u><mark>https://www.spotrac.com/nba/golden-state-warriors/stephen-curry-6287/</mark></u> <mark>(</mark> accessed November 30, 2018). 

- [26] <mark>Badenhausen, Kurt. “NBA Team Values 2018: Every Club Now Worth At Least $1 Billion.”</mark> _<mark>Forbes</mark>_ <mark>. h</mark> <u>ttps://www.forbes.com/sites/kurtbadenhausen/2018/02/07/nba-team-values2018-every-club-now-worth-at-least-1-billion/#51209c487155</u> <mark>(accessed November 30, 2018).</mark> 





2019 Research Papers Competition Presented by: 

26 



## **Appendix** 



**Figure A.1:** Generalized Difference-in-Differences for Al Horford 



**Figure A.2:** Generalized Difference-in-Differences for Andre Drummond 



**Figure A.3:** Generalized Difference-in-Differences for Damian Lillard 



2019 Research Papers Competition Presented by: 



27 





**Figure A.4:** Generalized Difference-in-Differences for Draymond Green 



**Figure A.5:** Generalized Difference-in-Differences for James Harden 



**Figure A.6:** Generalized Difference-in-Differences for John Wall 



2019 Research Papers Competition Presented by: 



28 





**Figure A.7:** Generalized Difference-in-Differences for Klay Thompson 



**Figure A.8:** Generalized Difference-in-Differences for Kyle Lowry 



**Figure A.9:** Generalized Difference-in-Differences for Kristaps Porzingis 



2019 Research Papers Competition Presented by: 



29 


