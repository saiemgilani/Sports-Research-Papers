<!-- source: 2019 Analytics for the Front Office - Valuing Protections on NBA Draft Picks.pdf -->



# **Analytics for the Front Office: Valuing Protections on NBA Draft Picks** 

### Benjamin T. Foster<sup>1</sup> and Michael D. Binns<sup>2</sup> 

Basketball 13521 

## **1. Introduction** 

Like other major sports leagues, the National Basketball Association (NBA) permits teams to trade draft picks. Beginning in 1984 with a trade between the Dallas Mavericks and Indiana Pacers, the NBA officially began allowing teams to place “protections” on traded picks that restrict the conditions under which the picks are ultimately transferred. Protections enable these “pick assets” to take on many possible values<sup>3</sup> , allowing teams to tailor an asset to the trade’s particular circumstances. Both trading draft picks and placing protections on those picks have become increasingly-utilized tools by teams in the NBA marketplace. Figure 1 below plots the distribution of the first-round draft picks included in trades from June 5, 2011, to May 31, 2017. 



<!-- Start of picture text -->
40<br>Distribution of Protections on First-Round Picks<br>35<br>30<br>25<br>20<br>15<br>10<br>5<br>0<br>Ø 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20<br>Protection placed on pick<br>(Top _X_ protected)<br>Number of picks<br><!-- End of picture text -->

**Figure 1:** Distribution of “top-X” pick protections on 2011-2024 first-round draft picks traded from 6/5/11 to 5/31/17 

- 1 Email: benTfoster@gmail.com 

2 Email: binnsmd@gmail.com 

3 There are over one billion possible pick protection combinations for a first-round draft pick protected for a single year. Not all of those combinations will meaningfully alter the value of the asset, but, even if there are just ten positions worth protecting, there are 1023 possible protection schemes. 





2019 Research Papers Competition Presented by: 

1 



Although teams possess the freedom to place protections at _any_ pick position, protections are often placed on numbers that are strong psychological anchors<sup>4</sup> (e.g., 5, 10, and 14<sup>5</sup> ). This suggests that pick protections may be regularly mis-valued and, consequently, improved valuation of pick protections would be beneficial in the NBA marketplace. 

Protections are not assets themselves and, therefore, their value cannot be determined independently from the draft pick. Protections modify the conditions under which the underlying asset – the right to select a player in a given year and draft position – is transferred. As such, protected draft picks function much like financial option contracts: their ultimate value is conditional on the uncertain future value of the underlying financial asset. By conceptualizing draft picks as financial assets, we are able to use economic and financial pricing theories and, using statistical methods, create a non-market valuation model to systematically price draft picks with and without protections. 

## **2. Background** 

Like most professional sports leagues in the United States, the National Basketball Association (NBA) provides teams with multiple avenues for team-building, including free agency, amateur drafts, and trades. The NBA – like the National Football League, National Hockey League, and Major League Soccer – permits teams to trade draft picks<sup>6</sup> . 

#### **2.1. The NBA Marketplace** 

A market is a forum in which buyers and sellers are brought together for the exchange of goods and/or services. By permitting the trade of players and draft picks between teams, the NBA has created a marketplace. This marketplace has particular characteristics that include a limited number of market actors and a limited quantity of a few types of assets with unique levels of quality (i.e., lack of standardization). 

#### **2.1.1. Market Actors** 

The buyers and sellers in the NBA marketplace consist of each of the 30 teams in the league. International basketball teams, though unable to participate in trades, can be thought of as a limited actor in this marketplace for basketball labor [1]. These teams can compete for free agents and may have a peripheral impact on trade decisions because of their presence in the free agent market. NBA teams are generally independently owned, independently operated, and are in competition with one another. 

- 4 In an efficient market, it is likely that there would be less clustering. 

5 This is often referred to as “lottery-protected,” which can be mis-understood to imply some extra value by virtue of aligning with the lottery process. Of course, because protections reference the ultimate pick position (i.e., post-lottery), a top-14 protection should not hold any special value by virtue of the lottery’s existence. 

6 See Glossary for definitions of specialized terms. 





2019 Research Papers Competition Presented by: 

2 



#### **2.1.2. Assets** 

The goods most frequently exchanged in the NBA marketplace are players currently under contract and future draft picks, although other assets types are available to be traded<sup>7</sup> . These two main types of assets share a few characteristics which make the NBA marketplace unique from other markets: there are a limited number of each asset type available for trade<sup>8</sup> , there are a limited number of player assets that one team can hold or trade, and no asset within the entire marketplace is identical to another asset. 

#### **2.1.3. Regulatory Context** 

The regulation which governs the marketplace is agreed upon in the Collective Bargaining Agreement (CBA) between the NBA and the labor union representing the players, the National Basketball Players Association (NBPA). This regulation includes, for example, deadlines by which in-season trades must take place, rules about the timing of traded draft picks, and restrictions on contract size deviations within a trade. Most regulation effectively limits the number of executed transactions, which is likely a desired outcome for a league that values team stability. 

#### **2.2. Characteristics of the NBA Marketplace** 

The NBA marketplace is more like a real estate market than a grocery store. There are not clear market prices for standardized goods like one might find in a store; rather, all assets on the market are unique. The advertised price (i.e., the “asking” price by the seller) is not necessarily the price paid because negotiation between buyer and seller sets the clearing price, much like what occurs in a real estate market. The lack of currency for facilitating transactions further complicates trade. The best analog is not a traditional real estate market, but a fictional real estate market where only other property can be used to make a purchase. Prices, therefore, are expressed in terms of other assets that may be difficult to compare across interested buyers. The result is infrequent transactions and no standardized “pricing” function. As a result, an asset may not be readily exchanged for its true value, an attribute commonly referred to as “low liquidity”. 

#### **2.3. Trading in the NBA Marketplace** 

A team that acquires a player via a trade gains the player and his contract. Players may be under contract with teams for 1-5 years, for varying dollar amounts. Most players’ contracts are guaranteed, although some contracts are partially guaranteed or non-guaranteed. Other rules give certain rights to teams who draft a player (e.g., they can offer an extension that other teams cannot), which add value to a player asset for only one party in the market. 

7 These assets include rights to drafted NBA prospects, the right to swap future draft picks, and cash. 

8 This number of available player and pick assets is limited to (1) the players currently on NBA contracts, and (2) first- and second-round draft picks for each of the 30 teams over each of the next seven years, or 420 total draft picks. 



2019 Research Papers Competition Presented by: 



3 



Draft picks can be categorized into two groups: first-round picks and second-round picks. Each team is granted one first-round pick and one second-round pick in each draft. Teams may trade away their draft picks for the upcoming seven seasons. Also, teams are prohibited from trading their first-round draft picks in consecutive years. Protections may also be added to traded draft picks that alter when, and under what conditions, the pick is ultimately transferred from one team to another<sup>9</sup> . This feature is unique among professional sports leagues and leads to a variety of interesting outcomes, which are, in part, the motivation for this work. These protections serve to increase the effective assets at a team’s disposal: a pick that previously had only a single value can be modified with pick protections to take on a range of values. This, unlike many other features in the NBA market, ought to be a force that increases the likelihood of a trade by allowing buyers and sellers to more closely match asset values. 

As the popularity of trading draft picks has increased, so, too, has the popularity of placing protections on the picks; furthermore, the protections that teams are placing on draft picks are becoming increasingly complex. These complex protection schemes include multi-year protections, high- and low-side protections, and ascending _and_ descending protections. These protections make it difficult to value the traded draft pick, which, in turn, complicates trade assessments. 

## **3. Theory** 

Prices contain a vast amount of information about the costs of production (supply) and the benefits of consumption (demand) that may otherwise be costly for all market actors to acquire [2]. As long as prices fully reflect all relevant market information at a specific point in time and the market is free from other sources of distortion, they will efficiently allocate a scarce asset among actors with varying and sometimes conflicting preferences and values. Simply, prices are the market’s valuation of an asset. Under certain conditions, that definition can be extended: prices are an asset’s “true value” at a particular point in time. This second interpretation of prices has significant advantages for the analyst who is interested in tracking the value of assets. But, if distortions or other market conditions lead prices to deviate from an asset’s true value, discovering that true value becomes a more difficult exercise, requiring either a method for correcting prices or a nonmarket valuation method. 

Whether prices reflect an asset’s true value is, in part, a philosophical question, the discussion of which this paper will avoid, but it is also a technical one. There are identifiable market conditions that are known to strongly indicate that prices may not be a reliable indicator of the true value of an asset. Questions surrounding market and price efficiency have attracted a lot of attention from researchers in economics and finance across a range of markets. We will also avoid an in-depth discussion of market efficiency, but do draw on a few qualities of efficient markets to illustrate that “prices” in the NBA marketplace likely do not reflect the true value of an asset. As such, we develop a non-market valuation method to better understand the value of NBA trade assets, specifically draft picks. 

9 For example, Team A may agree to trade Player X to Team B in return for Team B’s 2019 top-5 protected first-round draft pick; in this situation, Team B’s 2019 first-round draft pick would be conveyed to Team A unless that pick became one of the top-5 picks in the 2019 NBA Draft; it would be “protected”. In the event that the pick is protected, Team B would give Team A a different future asset, agreed upon prior to completing the trade, such as Team B’s unprotected 2020 first-round draft pick. 





2019 Research Papers Competition Presented by: 

4 



#### **3.1. NBA Market Efficiency** 

There are a few market characteristics that are relevant to explaining why NBA trade markets are not likely to have prices that reflect the true value of assets: strict regulatory constraints, high transaction costs, and low liquidity. Regulatory constraints affect market outcomes in part by limiting the pool of tradable assets and the number of prospective buyers and sellers. Both of these reduce market liquidity: the ability to quickly sell an asset for its true value. In a market with low liquidity, prospective sellers may have to sell an asset for less than market value if they want to sell it quickly, and buyers may not be able to find available assets for sale at their true value. 

The NBA marketplace is a barter-based system. Consequently, “price” in the NBA marketplace is another asset, or group of other assets, that can be difficult to value in their own right. In this system, information is asymmetric (e.g., teams possess higher quality information about their own players and lower quality information about other team’s players). Variation in asset quality increases this problem. Each asset that can be exchanged is different, and discovering the quality of any single asset<sup>10</sup> can be costly for some parties and not as costly for others. Beyond variation in quality between assets, each single asset also has internal uncertainty: the future state of that asset can take on many values and the value at any point in the future is unknowable with certainty. 

Competition between teams also distorts prices. Though there are some market forces that might keep teams from using leverage to dramatically “win” a trade (e.g., they may want to trade again, with the same or other teams, who may be not want to negotiate with an actor who has demonstrated a willingness to take advantage of trading partners), there is likely to still be some amount of surplus seeking in trade negotiations. Teams will still use leverage to extract value from competitors. This will result in a price distortion. 

Regulatory constraints, future uncertainty, and information costs combine to result in high transaction costs. Transaction costs are defined as the costs involved in exchange, including the costs of discovering the quality of an asset and the costs of negotiating a transaction. When transaction costs are high, exchange is less likely to occur because one or both parties must be willing to sacrifice value in order to agree on a clearing price: a price for which transaction costs will be paid by one or both parties to complete a transaction. That is, sellers would have to sell low or buyers would have to buy high in order for a deal to be made. High transactions costs also contribute to low liquidity. 

#### **3.2. Non-Market Valuation of Assets** 

10 The quality of an asset describes all of the relevant and knowable information about an asset and its possible future states. This information is likely to be easiest to acquire by the team who owns the asset and has access that other teams do not have. Other teams would have to pay scouts or analysts to just approximate the information the original team holds. 



2019 Research Papers Competition Presented by: 



5 



Ultimately, low liquidity strongly suggests that transactions do not clearly reveal the value of the assets involved. Low market liquidity is generally bad<sup>11</sup> for teams that want to buy or sell assets. A buyer may not be able to buy the asset they want to buy (because, for example, they may not have the “right” combination of assets to exchange), and a seller may not find a buyer willing to pay their “asking price.” So, if teams desire to buy or sell NBA assets in the NBA marketplace, what can they do to improve market liquidity or reduce transaction costs<sup>12</sup> ? 

Changing market rules could improve trading outcomes, but the current ones are likely in place precisely to reduce trade frequency. Efficiency is not necessarily a goal for the parties who set the rules that govern the NBA marketplace. The NBA certainly cares about how resources are allocated, but their primary objective is not to maximize an individual team’s short-term outcomes; rather, they seek to maximize outcomes for the league as a whole, and over a long timeframe. Because team incentives may not always align with this goal, the NBA uses restrictions to achieve their desired market outcomes, such as competitive balance and team stability. 

Within those rules, though, there are some opportunities for the league, or an enterprising team, to improve its evaluation of asset quality. One option is to find a non-market mechanism for establishing the value of an asset. In addition to establishing a standardized unit for “pricing” assets, this would also involve characterizing the uncertainty in the asset’s value. A non-market valuation model would reduce the cost of discovering an asset’s quality, thereby reducing the transaction costs of a trade. From the marketplace’s perspective, lower transaction costs should lead to an increase in trade frequency and improve the probability that assets are ultimately allocated to the highest value owner. That said, a non-market valuation model may also be used by a single actor to increase information asymmetry with trade partners and capture additional value when participating in the market. 

## **4. Methods** 

This work presents a non-market valuation model that will allow NBA stakeholders to better understand how pick protections change the value of traded draft picks. Draft pick assets are like financial assets: their ultimate value at “maturity” is uncertain, but that uncertainty can be characterized. Therefore, they can be valued with methods commonly used to price financial assets. We combine many statistical models/methodologies to create a system that can take any draft pick asset traded at any time and produce its fair-market “basketball price”. 

We first characterize the uncertainty in the asset’s future realized value using game simulations and historical data on player performance to assess the likelihood of a draft pick asset generating a number of on-court basketball outcomes. We pair the output of this model with a financial pricing methodology – that adjusts for league-wide risk preferences – to identify a single value for the asset. The structure of the model is shown in Figure 2. A more detailed model schematic is presented in Appendix 2. 

11 Though some teams may prefer a marketplace with some of the market characteristics that can lead to low liquidity (i.e., information asymmetry may give them an advantage in trade negotiations), in the long run, individual team advantages are probably temporary and a team may not even find an opportunity to use those advantages in a low liquid market. 

12 Or, improve their private information to preserve or develop an information advantage in the market. 





2019 Research Papers Competition Presented by: 

6 





<!-- Start of picture text -->
Module 1:  Team Performance Module 2:  Pick Position Valuation<br>Probability Distributions<br>Probability Distribution of<br>of Player Performance by<br>Team Finishing Position<br>Pick Position<br>Monte Carlo Simulation<br>Probability Distribution of Player Value Generated by Pick Asset<br>Module 3: Financial Asset Pricing Model<br>Risk Adjusted Draft Pick Asset Value<br><!-- End of picture text -->

Output from each process 

**Figure 2:** Basic flow of the Draft Pick Asset Valuation System. Module 1 and 2 output probability distributions that are the foundation of a Monte Carlo Simulation (MCS). The MCS accounts for pick protections and generates a probability distribution of player value by draft pick asset. Module 3 uses the output from the MCS to generate a single value, or price, for the draft pick asset. 

The system has three main modules: 

1. Team Performance – This model simulates the outcomes of scheduled NBA games (i.e., current season) and forecasts team performance in non-scheduled seasons (i.e., future seasons) to capture uncertainty in team standing. Lottery probabilities translate team standing into pick position. Protection schemes are applied to generate a final distribution of pick position for a given draft pick asset. 

2. Pick Position Valuation – This statistical model of historic player performance is used to capture uncertainty in the on-court production of a player picked at any given pick position. 

3. Draft Pick Asset Pricing – This model uses the result from the Pick Position Valuation, along with financial pricing theory (including a market risk adjustment), to calculate the value of a draft pick asset in terms of player-equivalent contribution to team performance (e.g., PER, Win Shares). 

A Monte Carlo simulation assembles the outputs from Module 1 and 2 into the input required for Module 3. 

#### **4.1. Team Performance Simulation** 

To produce a probability distribution of pick position, we use the Elo rating system as the basis for simulating each scheduled NBA game remaining in a given season. We follow the Elo simulation methodology, presented by Silver and Fischer-Baum [3]. The probability of the home team winning a game ( _P(Home)_ ) is represented by: 





2019 Research Papers Competition Presented by: 

7 



_𝑃𝐻𝑜𝑚𝑒= 11+10(−∆𝐺𝑎𝑚𝑒𝐸𝑙𝑜400)_ (1) 

_∆𝐺𝑎𝑚𝑒𝐸𝑙𝑜=(𝐸𝑙𝑜𝐻+𝐻𝑜𝑚𝑒𝐴𝑑)−𝐸𝑙𝑜𝐴_ (2) 

Following Silver and Fischer-Baum (2015), the home team advantage ( _HomeAd_ ) is 100 Elo rating points. A Monte Carlo simulation is used to generate game outcomes. After each simulated game, a team’s change in Elo is calculated as follows: 



The change in _TeamElo_ is added to the home team and subtracted from the away team. Elo ratings are adjusted after each game and used in the next game’s simulation. The model uses a _k_ value of 16. 

After simulating the outcome of every scheduled game, team records are calculated and teams are ranked according to win percentage. This order determines the team position in the league standings. Lottery probabilities then translate the standings position into a pick position. Once protections are applied, the model determines whether a pick will be protected. If protected, the pick rolls over into the following season. Without any scheduled games, the next season’s games cannot be simulated. So, to identify where a rolled-over pick might fall, a conditional probability model, calculated from historic data, is utilized. This model calculates the historical likelihood that a team who finishes in X1 standings position ( _𝑅𝑎𝑛𝑘𝑇_ ) in Year 1 finishes in X2 standings position in Year 2: 



These probabilities, shown in Figure 3, are calculated from historical NBA standings, from 19802017. 





2019 Research Papers Competition Presented by: 

8 





<!-- Start of picture text -->
1<br>Standings Position Year X<br>0.9 1<br>2<br>3<br>0.8 4<br>5<br>6<br>0.7 7<br>8<br>9<br>10<br>0.6 12<br>13<br>14<br>0.5 15<br>16<br>17<br>0.4 18<br>19<br>20<br>0.3 21<br>22<br>23<br>0.2 24<br>25<br>26<br>0.1 27<br>28<br>29<br>30<br>0<br>0 5 10 15 20 25 30 35<br>Standings Position Year X+1<br>Cumulative Probability<br><!-- End of picture text -->

**Figure 3:** Cumulative probability distributions for a team’s final standings position in Year X+1 conditional on their finishing position in Year X 

If a pick is rolled over, a team’s new standings position is calculated using the conditional probability, and lottery probabilities are applied. If the pick asset possesses a multi-year protection scheme, protections are checked again and conditional probabilities are used, if necessary. By the end of the process, a single value of pick position has been simulated accounting for pick protections and the remaining season schedule. Over many draws, a probability distribution across pick positions is generated. 

Elo as implemented does not account for how a team’s strength might change due to the trade itself. There are advanced Elo-based methods that account for individual player’s contributions to a new team. This has not been implemented yet, due to computational limitations, but would not be difficult to replace the basic Elo model used here. Alternatively, a distribution of team standing position could be generated from other methods such as betting odds. 

#### **4.2. Pick Position Valuation** 

To produce a probability distribution of a player value metric for each pick position, we used 36 years of player performance data from Basketball Reference organized by player’s pick position [4]. For the results shown below, we have chosen win shares (WS) generated over 5 years as our player value metric. We use win shares because it is a widely-accepted metric in analysis-driven NBA circles; we use 5 years to capture player contributions over a period during which a team might be able to retain its services due to rookie contracts and extensions. Win shares per five years captures the total contributions a team can expect to obtain (either from actual production or in trade value returned) from a draft pick. This metric also simplifies comparisons with current players, who might be on the other side of a proposed trade and whose team contributions can also be calculated using win shares over time (that is, the player’s value time frame can be adjusted to account for the specifics of a player’s contract or expectations about re-signing). A different advanced metric, or a different time frame, could easily be implemented in our model. 



2019 Research Papers Competition Presented by: 



9 



The raw cumulative distributions of WS/5yrs for each pick position are shown in Figure 4. Although these distributions could be used in the model, they produce idiosyncratic results as a function of outliers in the dataset. To smooth these outcomes, we use linear extrapolation between data points and an algorithm to order the pick distributions, such that a worse pick does not have a larger WS/5yrs at any given cumulative probability. This preserves the expected feature that a higher pick (i.e., closer to 1) is always a better asset than a lower pick, a feature that is not strictly true in the historic data. The filtering algorithm identifies situations where a lower pick has a better outcome and splits the difference in WS at the cumulative probability between the two picks. 

_𝑖𝑓 𝑊𝑆𝐶𝑃,𝐷𝑃+1>𝑊𝑆𝐶𝑃,𝐷𝑃_ (5) 

_𝑡ℎ𝑒𝑛, 𝑊𝑆𝐶𝑃,𝐷𝑃=𝑊𝑆𝐶𝑃,𝐷𝑃+𝑊𝑆𝐶𝑃,𝐷𝑃+1−𝑊𝑆𝐶𝑃,𝐷𝑃2_ 

_𝑊𝑆𝐶𝑃,𝐷𝑃+1=𝑊𝑆𝐶𝑃,𝐷𝑃−𝑊𝑆𝐶𝑃,𝐷𝑃+1−𝑊𝑆𝐶𝑃,𝐷𝑃2_ 

where, 

##### _𝑊𝑆𝐶𝑃,𝐷𝑃=𝑤𝑖𝑛 𝑠ℎ𝑎𝑟𝑒𝑠 𝑎𝑡 𝑎 𝑔𝑖𝑣𝑒𝑛 𝑐𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒 𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦 𝐶𝑃𝑎𝑛𝑑 𝑓𝑜𝑟 𝑎 𝑠𝑝𝑒𝑐𝑖𝑓𝑖𝑐 𝑑𝑟𝑎𝑓𝑡 𝑝𝑜𝑠𝑖𝑡𝑖𝑜𝑛 (𝐷𝑃)_ 

The filtering algorithm is run from pick 1 to 30 at each cumulative probability (1000 discrete steps between 0 and 1) and as many times as is required in order to eliminate all cases where a lower pick generates more win shares at a given cumulative probability than a higher pick. The results of this filtering method are shown in Figure 5. 



<!-- Start of picture text -->
1 Draft Position<br>1<br>2<br>0.9 3<br>4<br>5<br>0.8 6<br>7<br>8<br>0.7 9<br>10<br>11<br>0.6 12<br>13<br>0.5 14<br>15<br>16<br>0.4 17<br>18<br>19<br>0.3 20<br>21<br>22<br>0.2 23<br>24<br>25<br>0.1 26<br>27<br>28<br>0 29<br>-10 0 10 20 30 40 50 60 70 80 30<br>Player Value (WS/5yrs)<br>Cumulative Probability<br><!-- End of picture text -->

**Figure 4:** Raw cumulative probability of win shares in the first five years of a draftee’s career 



2019 Research Papers Competition Presented by: 



10 





<!-- Start of picture text -->
1 Draft Position<br>1<br>2<br>0.9 3<br>4<br>5<br>0.8 6<br>7<br>0.7 8<br>9<br>10<br>0.6 11<br>12<br>13<br>0.5 14<br>15<br>16<br>0.4 17<br>18<br>19<br>0.3 20<br>21<br>22<br>0.2 23<br>24<br>25<br>0.1 26<br>27<br>28<br>0 29<br>-10 0 10 20 30 40 50 60 70 80 30<br>Player Value (WS/5yrs)<br>Cumulative Probability<br><!-- End of picture text -->

**Figure 5:** Filtered cumulative probability of win shares in the first five years of a draftee’s career 

Figure 6 compares the smoothed and raw distributions for each pick. The filtering algorithm is biased towards valuing picks more highly because it reallocates good player outcomes from worse pick positions to better pick positions. In Figure 6, if the red (smoothed) distribution is to the right of the black (raw) distribution, then the model indicates that players picked at that pick position tend to underperform relative to players selected immediately after them; if the red distribution is to the left of the black, it suggests that teams generally get good value from that pick position relative to nearby pick positions. 





2019 Research Papers Competition Presented by: 

11 





<!-- Start of picture text -->
Pick 1 Pick 2 Pick 3 Pick 4 Pick 5 Pick 6<br>1 1 1 1 1 1<br>0.5 0.5 0.5 0.5 0.5 0.5<br>0 0 0 0 0 0<br>0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60<br>Pick 7 Pick 8 Pick 9 Pick 10 Pick 11 Pick 12<br>1 1 1 1 1 1<br>0.5 0.5 0.5 0.5 0.5 0.5<br>0 0 0 0 0 0<br>0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60<br>Pick 13 Pick 14 Pick 15 Pick 16 Pick 17 Pick 18<br>1 1 1 1 1 1<br>0.5 0.5 0.5 0.5 0.5 0.5<br>0 0 0 0 0 0<br>0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60<br>Pick 19 Pick 20 Pick 21 Pick 22 Pick 23 Pick 24<br>1 1 1 1 1 1<br>0.5 0.5 0.5 0.5 0.5 0.5<br>0 0 0 0 0 0<br>0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60<br>Pick 25 Pick 26 Pick 27 Pick 28 Pick 29 Pick 30<br>1 1 1 1 1 1<br>0.5 0.5 0.5 0.5 0.5 0.5<br>0 0 0 0 0 0<br>0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60<br>Player Value (WS/5yrs) Filtered<br>Empirical<br>Cumulative Probability<br><!-- End of picture text -->

**Figure 6:** Comparison between raw and filtered cumulative distributions by pick 

#### **4.3. Monte Carlo Simulation** 

A Monte Carlo simulation generates a probability distribution that describes the probability of the pick asset generating a range of WS/5yrs values. First, a selection is made from the distribution of finishing position. Then, a selection is made from the corresponding distribution of pick positions that could be obtained from that finishing position through the lottery. If the selected pick falls into the protection scheme, a new team finishing position is selected from the conditional future season finishing position distribution. This process is repeated until the pick asset expires or falls into an unprotected level. From this finishing position, a selection is made from the possible pick positions that could be obtained from the lottery. This generates a single WS/5yr value generated from the draft pick asset. After many draws, these values are used to create the final empirical distribution. This distribution is the input to the pricing model. The mechanics of this simulation are further detailed in Appendix 2. 

#### **4.4. Draft Pick Asset Pricing** 

To produce the value of a draft pick asset, we use a method called the Wang transform [5]. The method distorts the cumulative distribution of outcomes. The expectation of the distorted distribution yields the “price.” 



where, = outcomes _ϕy_ = standard cumulative distribution function Q = Student-t distribution with k degrees-of-freedom γ = Sharpe Ratio or “market price of risk” _F*x_ = risk adjusted pdf of outcomes _Fx_ = pdf of outcomes 



2019 Research Papers Competition Presented by: 



12 



_Price(x)_ = _EVi*_ = x*F*x (7) 

In addition to the output from the two models described above, this method requires one fitted parameter, the Sharpe ratio. This value is used to adjust the empirical distribution of outcomes, such that extreme values are more (or less) heavily weighted. For regularly-traded asset classes, the Sharpe ratio is easily calculated as the excess return associated with a measure of an asset’s variation. The Sharpe ratio is a specific calculation that is not possible to calculate for NBA draft picks, but the idea that it represents is valuable. The Sharpe ratio represents the price at which a given class of asset is traded on the market, or the “market price of risk.” This value is difficult to directly calculate for NBA draft picks, but the concept it represents is valuable: how market actors treat risky assets. One way to interpret this value is that it indicates whether market actors are willing to pay more (risk seeking) or less (risk averse) than the expected value of risky assets. To calibrate the market price of risk for NBA draft picks, we use historic trades and extrapolate to the asset classes determined from a clustering method. 

First, we identify a plausible market price of risk using trades that only involved draft picks with known positions. The two trades used to calculate this value are (1) the 2017 Kings-Trail Blazers trade (pick 10 for picks 15 and 20, respectively), and (2) the 2017 Lakers-Jazz trade (pick 28 for picks 30 and 42, respectively). Assuming these trades were perfectly “fair,” the Sharpe ratios that balance the trades are 0.413 (Kings) and 0.436 (Lakers). These suggest that teams are risk averse, that draft pick assets trade for less than their expected values as a result of their variability, particularly the below-average outcomes. We present results using 0.42 (“Risk Averse”), the rounded average between the two trades, 0.00 (“Expected Value” or “Risk Neutral”), and -0.42 (“Risk Seeking”). 

There is reason to think that teams are not always risk averse though. Anecdotally, teams seem happy to “overpay” for a possibility of obtaining the first pick in a draft. The possibility of a franchise-changing player is valuable. In fact, it seems likely that picks in different ranges are all treated differently. Consequently, we treat picks as more than one asset class. Using a K-means clustering method [6], seven asset classes are identified from the filtered pick value distributions: #1, #2-3, #4-5, #6-10, #11-18, #19-24, and #25-30 (“Tiered Asset Risk Preferences”; see Figure 7). 





2019 Research Papers Competition Presented by: 

13 





<!-- Start of picture text -->
Pick 1 Pick 2-3 Pick 4-5 Pick 6-10<br>1 1 1 1<br>0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4<br>0.2 0.2 0.2 0.2<br>0 0 0 0<br>0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60<br>Player Value (WS/5yrs) Player Value (WS/5yrs) Player Value (WS/5yrs) Player Value (WS/5yrs)<br>Pick 11-18 Pick 19-24 Pick 25-30<br>1 1 1<br>0.8 0.8 0.8<br>0.6 0.6 0.6<br>0.4 0.4 0.4<br>0.2 0.2 0.2<br>0 0 0<br>0 20 40 60 0 20 40 60 0 20 40 60<br>Player Value (WS/5yrs) Player Value (WS/5yrs) Player Value (WS/5yrs)<br>Cumulative Probability Cumulative Probability Cumulative Probability Cumulative Probability<br>Cumulative Probability Cumulative Probability Cumulative Probability<br><!-- End of picture text -->

**Figure 7:** Cumulative distributions for each of seven asset classes; each member of each class is highlighted in black, and the colored distributions for all 30 picks are in the background. 

With so few trades involving only draft picks, identifying the market price of risk for each asset class is difficult. We assign ratios assuming a relative level of risk aversion between classes. This could be adjusted for a specific team’s risk preferences, or an alternative method, such as a survey, could be used to find the market’s ratio for each asset class. The ratios used in our study are as follows: 

|**Asset Classes**<br>**(Pick**<br>**Positions)**|**Market Price of**<br>**Risk Ratio (𝛄) **|**Interpretation**|
|---|---|---|
|1|-0.77|Very Risk Seeking|
|2-3|-0.39|Risk Seeking|
|4-5|-0.19|Slightly Risk Seeking|
|6-10|-0.01|Risk Neutral|
|11-18|0.24|Slightly Risk Averse|
|19-24|0.44|Risk Averse|
|25-30|0.54|Very Risk Averse|



**Table 1:** Details of pick asset classes 

There are many ways the model could be adjusted to account for other factors, including different risk preferences, the number of years of future value that a team can expect a player to produce (based on, for example, rookie contracts lengths and re-signings as outlined in the CBA), the 



2019 Research Papers Competition Presented by: 



14 



perceived strength of upcoming draft classes, and expectations about a team’s future performance that are not reflected in the simulation model. Ultimately, this system could be constructed such that a user could toggle various preferences and expectations about the future. 

## **5. Results** 

<mark>All results are from the 2018 trade deadline and valuing 2018 picks for each team. They are colored based on the standing position of each team at the trade deadline with “1” representing the team in last place at the time. Some results only present selected teams that represent the entire range of results: Phoenix (worst Elo, in 5</mark><sup>th</sup> <mark>to last place), New York (10</mark><sup>th</sup> <mark>to last), Detroit (13</mark><sup>th</sup> <mark>to last), and Golden State (30</mark><sup>th</sup> <mark>to last).</mark> 

#### **<mark>5.1. Pick Position Distributions</mark>** 

Protections in this model are for just a single year. If a pick is protected, it rolls over to the following year unprotected. <mark>Figure 8 shows how simulated pick position outcomes change as protections increasingly limit outcomes in year one. Unsurprisingly, the protections do not affect the Warriors (GSW) pick because there is no chance that, as of the 2018 trade deadline, they would end up with a pick better than #25. On the other end of the spectrum are the Suns (PHO), in 5</mark><sup>th</sup> <mark>-to-last place at the trade deadline, but with the worst Elo rating. Without protection, their pick has approximately a 20% chance of ending up #1. With a top-1 protection, that probability drops to almost zero, but it rises as the pick protection horizon extends higher. Consider the top-3 protection. If that protection is utilized, the Suns likely finished close to the bottom of the standings. According to the conditional probability standings position model, they are likely to finish near the bottom of the standings again the following year when the pick is now unprotected. This increases their chance of getting the #1 pick, relative to just the top-1 protection because now the 2</mark><sup>nd</sup> <mark>and 3</mark><sup>rd</sup> <mark>pick, which end up protected in year one, have a chance to become pick #1 in year two.</mark> 





2019 Research Papers Competition Presented by: 

15 



















**Figure 8:** Probability distribution of any team’s draft asset becoming a particular pick position; results are presented for no protection and single year top 1-15 protections 

#### **5.2. Prices by Protection Level** 

Price outcomes, which result from the Wang transform model, are presented for four risk preference scenarios: Risk Neutral (Expected Value), Risk Averse, Risk Seeking, and Tiered Asset Risk Preferences (Figure 9). 





2019 Research Papers Competition Presented by: 

16 





<!-- Start of picture text -->
Expected Value Risk Averse<br>50 50<br>Team-Rank-ELO<br>40 40 ATL-1-1329<br>DAL-2-1364<br>SAC-3-1286<br>30 30 ORL-4-1318<br>PHO-5-1236<br>MEM-6-1330<br>20 20 CHI-7-1356<br>BRK-8-1303<br>LAL-9-1365<br>10 10 NYK-10-1356<br>CHA-11-1442<br>UTA-12-1538<br>0 0 DET-13-1420<br>0 5 10 15 0 5 10 15 PHI-14-1461<br>Pick Protection (Top-XX) Pick Protection (Top-XX) LAC-15-1493<br>NOP-16-1441<br>50 Risk Seeking 50 Tiered Asset Risk Preferences DEN-17-1475POR-18-1475<br>MIA-19-1440<br>IND-20-1457<br>40 40 OKC-21-1534<br>MIL-22-1480<br>CLE-23-1452<br>30 30 WAS-24-1489<br>MIN-25-1518<br>SAS-26-1514<br>20 20 TOR-27-1599<br>BOS-28-1524<br>HOU-29-1639<br>10 10 GSW-30-1625<br>Expected Value<br>0 0<br>0 5 10 15 0 5 10 15<br>Pick Protection (Top-XX) Pick Protection (Top-XX)<br>Expected Value (WS/5yrs)<br>Risk Adjusted Value (WS/5yrs)<br>Risk Adjusted Value (WS/5yrs) Risk Adjusted Value (WS/5yrs)<br><!-- End of picture text -->

**Figure 9:** Prices for each team’s 2018 first round pick under different single year protections schemes (unprotected to top-15 protected) and four risk preference scenarios. The expected value outcomes are grayed out in the background of the other three plots. Each pick is labelled with the team, their standings rank at the trade deadline (1 is last place), and their Elo rating at the trade deadline. 

The move to risk-seeking and risk-averse preferences shifts the prices of all assets up and down, respectively. The most interesting results are when draft picks are broken down into seven asset classes (“Tiered Asset Risk Preferences”). For the worst teams (dark blues), the biggest change in value is moving from unprotected to top-1 protected (nearly 10 WS). For the middle teams (light blues and greens), there is an initial drop in value from unprotected to top-1 protected, but most of that value is recovered as pick protections increase toward the team’s current standings position. Consider the Knicks (NYK) as an example (medium blue line starting in the upper 20s). The unprotected pick is worth approximately the same as a top-8 protected pick, and the minimum value is top-1 protected. The reason for this, is as the protections increase for year one, more outcomes are rolled over into year two where there are no protections. Because teams are risk seeking for low picks, it is extremely valuable to increase the chance of getting picks 1-5. 

#### **<mark>5.3. Pick Value Over Time</mark>** 

<mark>Pick protections do not have to be for one year only. In fact, it is quite common to trade a pick that has multiple years of protections. To investigate how time horizon affects pick value, the four selected team’s picks are valued for a variety of protection levels (1-15) and for 1-3 years of</mark> 





2019 Research Papers Competition Presented by: 

17 



<mark>protection (e.g., two years means that the pick is top-XX protected for this year and the next; if it ends up protected both years, then it becomes unprotected in the final year; see Figure 10).</mark> 



<!-- Start of picture text -->
35<br>30<br>25<br>20<br>15 Team-Rank-ELO (1-last)<br>PHO-5-1236<br>NYK-10-1356<br>DET-13-1420<br>GSW-30-1625<br>2 Years<br>10 3 Years<br>5<br>0 5 10 15<br>Pick Protection (Top-XX)<br>Risk Adjusted Value (WS/5yrs)<br><!-- End of picture text -->

**Figure 10:** Pick value, using tiered risk adjustments, presented for pick protections top 1-15 and for different time horizons (1-3 years) 

First, consider the Suns pick. Increasing the years of protection (solid line to dashed line to dotted line) reduces the value of the pick in all cases. This is because, over time, a team that is at the bottom of the standings is expected to move towards the middle. The longer the “best” pick positions are eliminated by protections, the more likely it is that the team will improve and the pick position will end up worse. Moving up the standings to the Pistons (DET) pick shows that increasing the number of years that a pick is protected actually increases the value of the pick. This is because the Pistons were in the middle of the standings at the time. If they were to finish the season poorly and end up with a pick position that gets protected, they are likely to be on the worse end of the distribution in subsequent years. 

## **6. Case Studies** 

#### **6.1. Lakers 2015 Protected Pick – Carter-Williams Trade** 

On February 19, 2015, a three-team trade took place between the Milwaukee Bucks, Philadelphia 76ers, and Phoenix Suns, in which the 76ers traded away Michael Carter-Williams and received a Los Angeles Lakers protected first-round draft pick that was then-owned by the Suns. In return, the Suns received Brandon Knight and Kendall Marshall. This draft pick was protected for selections 1- 5 in 2015, 1-3 in 2016, 1-3 in 2017, and unprotected in 2018. At the time, the Lakers were the third 



2019 Research Papers Competition Presented by: 



18 



worst team by record in the NBA. Though uncertain, it seemed likely that the pick would end up protected in 2015. 

By simulating the remainder of the 2015 NBA season and using WS as our player value metric, the draft pick asset (Lakers’ 2015 pick with protections) is valued (tiered risk-adjustment) at 20.95 WS over 5 years. An unprotected 2015 Lakers’ First Round Pick is valued at 42.52 WS over the same time period. Thus, the assigned pick protection scheme subtracts 21.57 WS, or 4.31 WS per year. This is the difference between the 25th and 98th ranked player (in WS) in the NBA in the 20162017 season. 

Figure 11 shows how a pick protection scheme impacts the probability of pick outcomes. Figure 11A-B shows the distribution of pick position for both the unprotected 2015 pick (Panel A) and the protected draft pick asset (Panel B). The results show that there is a 78% probability that the pick would fall in the protected range (top 5) in 2015 and therefore roll over into 2016. Over the lifetime of the draft pick asset, the protections remove nearly all instances of the pick becoming #1-3 and slightly increases the probability the pick will be in the #8-12 range. 



<!-- Start of picture text -->
Pick Position Distribution as of 2/19/15: Win Shares Distribution as of 2/19/15:<br>(A) Un-Protected (C) Un-Protected<br>0.25 0.2<br>0.2<br>0.15<br>0.15<br>0.1<br>0.1<br>0.05<br>0.05<br>0 0<br>0 5 10 15 20 25 30 0 10 20 30 40 50 60<br>Pick Position Win Shares/5 Yrs<br>(B) Protected (D) Protected<br>0.25 0.2<br>Distribution<br>0.2 Risk Averse Price<br>0.15<br>Expected Value Price<br>0.15 Risk Seeking Price<br>Tiered Price<br>0.1<br>0.1<br>0.05<br>0.05<br>0 0<br>0 5 10 15 20 25 30 0 10 20 30 40 50 60<br>Pick Position Win Shares/5 Yrs<br>Probability Probability<br>Probability Probability<br><!-- End of picture text -->

**Figure 11:** Pick position and win shares distributions for the unprotected and protected (top-5 in 2015, top-3 in 2016, top-3 in 2017, unprotected in 2018) Lakers pick traded on 2/19/2015. Lines indicated the price as calculated under the four different risk preference paradigms. 

These pick positions are translated into win shares using the Pick Position Valuation model. The distribution of win shares is shown in Figure 11C-D. As expected, the protections reduce the probability of the draft pick asset becoming a player that generates a large number of win shares over their first five years in the league. 



2019 Research Papers Competition Presented by: 



19 



#### **6.2. Bucks 2018 Protected Pick – Bledsoe Trade** 

On 11/7/17, the Bucks traded a first-round draft pick, a second-round draft pick, and Greg Monroe on an expiring contract to the Phoenix Suns for Eric Bledsoe. The first-round pick is protected 1-10 and 17-30 in 2018, 1-3 and 17-30 in 2019, 1-7 in 2020, and unprotected in 2021. The pick protection scheme is quite complicated. The high-end protections (1-10/3/7) move down after year one and back up after year two. There are also low-end protections (17-30) that roll the pick over if it ends up too low. These protections are shown visually in Figure 12. 



**Figure 12:** 2018 traded Bucks pick, green indicates when the pick will transfer 

The modelled pick values, using tiered risk-adjustment, are: 14.80 WS as protected (Figure 13F), 20.61 WS unprotected (Figure 13D),. (See Figure 13.) Interestingly, part of the protection scheme was 17-30 in 2018-19. Removing those low-end protections dropped the value to 12.88 WS, meaning the low-end protections increased the value of the asset (Figure 13E). 



<!-- Start of picture text -->
Pick Position Distribution as of 11/7/17: Win Shares Distribution as of 11/7/17:<br>(A) Un-Protected (D) Un-Protected<br>0.1 0.2<br>0.05 0.1<br>0 0<br>0 5 10 15 20 25 30 0 10 20 30 40 50 60<br>Pick Position Win Shares/5 Yrs<br>(B) High Protections Only (E) High Protections Only<br>0.1 0.2<br>0.05 0.1<br>0 0<br>0 5 10 15 20 25 30 0 10 20 30 40 50 60<br>Pick Position Win Shares/5 Yrs<br>(C) Full Protections (F) Full Protections<br>0.1 0.2 Distribution<br>Risk Averse Price<br>Expected Value Price<br>0.05 0.1 Risk Seeking Price<br>Tiered Price<br>0 0<br>0 5 10 15 20 25 30 0 10 20 30 40 50 60<br>Pick Position Win Shares/5 Yrs<br>Probability Probability<br>Probability Probability<br>Probability Probability<br><!-- End of picture text -->

**Figure 13:** Pick position and win shares distributions for the unprotected and protected (1-10/1730 in 2018, 1-3/17-30 in 2019, 1-7 in 2020, and unprotected in 2021) Bucks pick traded on 11/7/2017. Pick outcomes with only the high-end protections (1-10, 1-3, and 1-10) are also shown. Lines indicated the price as calculated under the four different risk preference paradigms. 



2019 Research Papers Competition Presented by: 



20 



## **7. Discussion** 

Our contribution to the limited scientific and publicly-available basketball literature is twofold, both theoretical and practical. Theoretically, we have conceptualized draft picks as financial assets, whose future value, though uncertain, is characterizable and can be valued using financial asset pricing principles. Practically, we have combined statistical methods and a financial pricing method to create a model that systematically prices draft pick assets with any combination of protections. 

One of the model’s core features is flexibility. It is adjustable for a number of factors, including the user’s preferred player valuation metric (e.g., WS, PER, etc.), risk preferences of the buyers and sellers, and perceived draft strength. The only requirement is the generation of a probability distribution of a player valuation metric generated by a draft pick asset. We have used an Elo rating system to quantify the uncertainty in pick position and a statistical analysis of historic data and a Monte Carlo simulation to quantify the uncertainty in future player contributions. Alternative methods could be used to perform both of these tasks. Risk preferences (i.e., the Sharpe ratio for each of the asset classes) is a large source of uncertainty due to the challenge of deriving those values. One way to address this would be to perform a sensitivity analysis with different risk preferences, or to allow each user to input their own risk preferences. Additional research into market wide risk preferences would be a valuable addition. 

There are two major ways in which a systematic method for valuing draft picks can contribute to the business of sports. First, the model can be used by individual teams to gain a competitive advantage in the NBA marketplace. By having an accurate valuation of protected draft picks, a team can more-precisely match the value of player(s) and draft pick(s) in a trade and extract further value by exploiting a trade partner’s psychological anchors. In addition, teams who have an accurate valuation of protected draft picks can, in conversations with potential trade partners, identify undervalued draft picks owned by said partners and acquire them at a price below their true value. Conversely, the model could be used to establish a “true value of draft picks” that can be referenced by all market actors. By making the model publicly available and, therefore, decreasing information asymmetry in the NBA marketplace, negotiations over pick protections may be made more efficient, perhaps enabling a more liquid trading market<sup>13</sup> . 

The current version of the model is intended to prove the viability of the concept; there are many ways in which additional research could generate improvements to the system. There are two notable shortcomings we have identified with the current model. First, the model does not account for the time-value of assets, as any robust financial model would. We did not address this issue because it is not immediately clear whether time reduces the value of a draft pick as it does for currency. For example, a pick that is protected in year 1 in our model becomes a basketball player in year 2. Since we use five years of win shares as our valuation metric, the five years for the protected pick occur from year 2-6 rather than 1-5. We treat these two situations as the same. In other words, we do not discount the contributions from the player picked for year 2 relative to the player picked for year 1. Further research or input from practitioners could provide insight into how to best address this issue. 

13 Beyond having a common, agreed-upon language with which to discuss the trades of players and draft picks, tools can be developed to assist teams in negotiations. One analog in a parallel industry is the NFL’s _Draft Pick Trade Value Chart,_ developed by Jimmy Johnson. 



2019 Research Papers Competition Presented by: 



21 



Second, the model does not account for the expected salary of a draft pick. The salary allocated to draftees is negotiable within the Rookie Pay Scale assigned for the draftee’s pick position. This is a major component of the cost of a player and is important to any cost-benefit style approach to valuing players. As such, any valuation of a draft pick asset with a pick protection scheme should also account for the conveyed pick’s salary<sup>14</sup> , which varies depending on the pick position. Future iterations of the model should account for the value of time and the value of a draft pick’s contract. 

14 For example, a first-round draft pick that is protected top-10 this year will not have a starting salary above $3.4M if the pick falls outside of the top 10 and, thus conveys; however, if the pick falls within the top 10 this year and conveys without protections the following year, the pick’s starting salary – assuming it became the first overall pick next year – could be as large as $8.1M. 



2019 Research Papers Competition Presented by: 



22 



## **References** 

[1] Mitchell, V. (2009). Will NBA Players go to Europe. _DePaul J. Sports L. & Contemp. Probs._ , _6_ , 221. [2] Friedman, M. (2017). _Price theory_ . Routledge. 

[3] Silver, N., & Fischer-Baum, R. (2015). How We Calculate NBA Elo Ratings. _http://fivethirtyeight. com/features/how-we-calculate-nba-elo-ratings_ . 

[4] Sports Reference LLC (2018). Basketball-Reference.com - Basketball Statistics and History. _https://www.basketball-reference.com/._ 

[5] Wang, S. (2002). A universal framework for pricing financial and insurance risks. Astin Bulletin, 32(2), 213-234. 

[6] Lloyd, S. (1982). Least squares quantization in PCM. _IEEE transactions on information theory_ , _28_ (2), 129-137. 





2019 Research Papers Competition Presented by: 

23 



## **Appendix** 

#### **Appendix 1. Glossary** 

**Draft Pick** - A team’s right to make a first or second round selection in a specified future year’s draft. 

<u>Format: [Team Name][Year][Round] Example: Lakers’ 2015 First Round Pick.</u> 

**Team Standing** - A team’s league rank (as determined by its W-L record) at a specified point in time. At the end of a season, this rank determines the probabilities assigned to the team in the lottery process. 

**Pick Position** - The ultimate numerical position of a _Draft Pick_ , as determined by end-of-season _Team Standing_ and lottery results. 

**Pick Protection** - A conditional restriction on whether a traded _Draft Pick_ will convey. <u>Format: protected [Begin Pick Position]-[End Pick Position] Example: protected 1-5 (or, commonly, “top-5 protected”)</u> 

##### **Draft Pick with a Pick Protection** 

<u>Format: [Draft Pick] [Pick Protection] Example: Lakers’ 2015 First Round Pick protected 1-5</u> 

<u>Interpretation: the Lakers’ 2015 First Round Pick will be conveyed unless its</u> _Pick Position_ is 1-5, in which case the Lakers’ will retain the pick. 

**Draft Picks with a Pick Protection Scheme** - A sequence of _Pick Protections_ for a series of _Draft Picks_ . 

<u>Format:</u> [Pick Protection 1], [Pick Protection 2], [Pick Protection 3], etc. <u>Example: Lakers’ 2015 First Round Pick protected 1-5, Lakers’ 2016 First Round Pick protected 1-3,</u> Lakers’ 2017 First Round Pick protected 1-3, Lakers’ 2018 First Round Pick unprotected. <u>Shorthand Format:</u> [Team][First Year] protected [End Pick Position], [End Pick Position], etc. <u>Shorthand Example:</u> Lakers’ 2015 First protected 5, 3, 3, 0 

<u>Interpretation: the Lakers’ 2015 First Round Pick will be conveyed unless its</u> _Pick Position_ is 1-5, in which case the Lakers’ 2016 First Round Pick will be conveyed unless its _Pick Position_ is 1-3, in which case the Lakers’ 2017 First Round Pick will be conveyed unless its _Pick Position_ is 1-3, in which case the Lakers’ 2018 First Round Pick will be conveyed. 

**Draft Pick Asset** - A traded _Draft Pick, Draft Pick with a Pick Protection,_ or series of _Draft Picks with a Pick Protection Scheme._ A _Draft Pick Asset_ without protections is simply a traded _Draft Pick_ and becomes a “ _Draft Pick_ with a _Pick Position”_ after the draft lottery (note: pick year and round are known at the trade date, but pick position may or may not be known). A _Draft Pick Asset_ with protections becomes a “ _Draft Pick_ with a _Pick Position”_ under the conditions specified by the _Pick Protection_ or _Pick Protection Scheme_ (note: pick year, round, and position are not known at the trade date). 





2019 Research Papers Competition Presented by: 

24 



**Player Value** - A numerical representation of a Player’s basketball value. In the current context, this is a combination of an advanced performance metric and a timeframe (e.g., win shares accumulated over the first 5 years of the Player’s career). 

**Pick Position Value** - The _Player Value_ associated with players drafted at a specific _Pick Position_ . 

**Draft Pick Asset Value** - The _Pick Position Value_ associated with a _Draft Pick Asset_ . 





2019 Research Papers Competition Presented by: 

25 



#### **Appendix 2. Draft Pick Asset Valuation System Schematic** 

This schematic shows how the various models and methods described in the Methods section are assembled to generate a single asset valuation. For the results presented in this paper, both the “Game/Season Simulation” and the “Monte Carlo Simulation” consisted of 10,000 trials (variable _N_ in the figure). 



<!-- Start of picture text -->
Module 2:  Pick Position Valuation<br>Pick Valuation Model Schematic<br>36Years of Historic<br>Player Performance Data<br>Module 1:  Team Performance<br>Distributions of Player<br>Performance by Pick Position<br>Game/Season Simulation<br>Filtering<br>Algorithm<br>Distribution of Team<br>Finishing Position Year 1 Filtered Distributions of Player<br>Performance by Pick Position<br>Lottery  Monte Carlo Simulation<br>Probabilities<br>Draw from Distribution of Team  Draw from  Rank1 ’s<br>Finishing Position Year 1 ( Rank1 )  Lottery Odds ( Pick1 )<br>YES NO<br>Protected? Draw from the  Pick1, Pick2, PickY<br>Lottery  Distribution of Player Performance by<br>Probabilities Pick Position<br>Draw from the Historic Conditional<br>Probability Distribution of Next Season  Draw from  Rank2 ’s  Single Player Value<br>(Year 2) Finishing Position of  Rank1  ( Rank2 )  Lottery Odds ( Pick2 )  Generated from Pick<br>( PVN )<br>Repeat process until Year  Y  YES NO<br>Protected?<br>produces an unprotected<br>Pick Position  Repeat Simulation  N Times<br>Distribution of Player<br>Value Generated by<br>Module 3: Financial Asset Pricing Model Risk Preferences  Pick Asset<br>Calibrated from<br>Pick/Pick Trades<br>Risk Adjusted<br>Draft Pick  Asset Pricing Model<br>Asset Value<br>Asset Classes<br>External Model Intermediate Result Random Draw  External Data/Analysis Contracted Decision Output<br><!-- End of picture text -->

**Figure 14:** System schematic 



2019 Research Papers Competition Presented by: 



26 


