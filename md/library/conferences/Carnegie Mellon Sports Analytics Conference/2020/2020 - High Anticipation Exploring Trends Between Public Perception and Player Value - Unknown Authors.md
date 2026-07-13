<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2020/2020 - High Anticipation Exploring Trends Between Public Perception and Player Value - Unknown Authors.pdf -->



# **<mark>High Anticipation</mark>** Exploring Trends Between Public Perception and Player Value 

Alana Willis, Fiona Dunn, and Sahana Rayan October 25, 2020 

player performance? 

- ~ How do we quantify public perception? 

Guiding the Research 

- ~ Do any players or subset of players stand out? 

~ Can we predict public perception using player performance and vise versa? 

2 

#### <mark>Area of Focus</mark> 

- round draft class 

   - All data had to be collected separately 

   - ○ Includes a randomized mix of players 

      - International 

      - ■ Highly anticipated 

      - ■ Underrated 



3 

##### Constructing the Data Set 



<!-- Start of picture text -->
Reddit Game Data<br>Scraped Reddit user<br>Scraped Box score data from<br>comments NBA stats page during the 2018 -<br>using RedditExtractoR  2019 season<br>01 02 03 04<br>Combined<br>Web Hits<br>Rows aligned by weeks a<br>Scraped views from<br>player participated in at<br>YouTube, Wikipedia, and<br>least one game over rookie<br>Google (Images and News)<br>season.<br><!-- End of picture text -->

4 

##### General EDA 

###### Anfernee Simons 



5 

##### Interesting Player Trends 





6 

##### Clustering 



- Hierarchical Clustering was done using positive score, negative score, Wiki views, Google web hits, Google news hits, and Youtube hits 

- ● Cluster 1: Not very popular, low sentiment 

- Cluster 2: A bit more popular, high sentiment 

7 

##### More EDA with the clusters 





8 

##### XGBoost: Predicting Clusters 

- These clusters were used as a response variable for a binary 

- XGboost model was trained using AUC as an evaluation metric and the test predictions has an AUC of 0.887 



9 

##### Partial Dependence Plots 





10 

##### Final Thoughts 

- Data wrangling and cleaning is HARD! 

- There is a relationship between a player’s performance, public sentiment, and overall popularity. 

- Clusters 

- Average minutes played and average points scored are the most important in predicting popularity and sentiment clusters 

11 

##### Continuing the Research 

- Introduce more variables to the models. 

- Reddit: comment score and controversiality 

- ● Expand to more draft classes and to more social media/chat rooms ○ Other subreddits, blogs, Facebook, ect 

- ● 

- Predicting public perception onto future draft classes based on college or international play 

- Principal Component Analysis with sentiment and popularity data 

12 

##### Contacts 

###### **Alana Willis** 

- Winston-Salem State University 

###### **Fiona Dunn** 

   - Kenyon College 

- dunn2@kenyon.edu 

###### **Sahana Rayan** 

   - Purdue University 

   - srayan@purdue.edu 

- awillis117@rams.wssu.edu 

- linkedin.com/in/alana-willi s-7a8014188/ 





- 06035138/ 



- linkedin.com/in/sahana-raya n/ 





13 

### <mark>References</mark> 

Bresler, Alex. “NbastatR v0.1.1503.” NbastatR Package | R Documentation, www.rdocumentation.org/packages/nbastatR/versions/0.1.1503. Game Score, www.nba.com/resources/static/team/v2/thunder/statlab-gamescore-191201.pdf . 

Massicotte, Philippe. “GtrendsR.” Function | R Documentation, www.rdocumentation.org/packages/gtrendsR/versions/1.3.5/topics/gtrends. Meissner, Peter. “Wikipediatrend v2.1.6.” Wikipediatrend Package | R Documentation, www.rdocumentation.org/packages/wikipediatrend/versions/2.1.6. 

Rivera, Ivan. Package ‘RedditExtractoR,’ 1 May 2019, cran.r-project.org/web/packages/RedditExtractoR/RedditExtractoR.pdf. Silge, Julia, and David Robinson. Text Mining with R, 7 Mar. 2020, www.tidytextmining.com/index.html. 

14 

## **Thank You!** 



- Carnegie Mellon University 

- Rebecca Nugent - Ron Yurko - Beomjo Park - Pratik Patil - 2020 Cohort 

- Atlanta Hawks 

- Maksim Horowitz 

15 

##### Variables of Interest 

1. **Week:** Mon-Sun of a week in the regular season of the NBA 

2. **Game Score:** a rough measure of a player’s productivity for a single game 

3. **Popularity** = (wiki_views + avg_web_hits + avg_image_hits + avg_news_hits + avg_yt_hits) / 5 

4. **Social Score** = (sentiment_week + 5 * Popularity) / 6 

16 

##### General EDA 



<!-- Start of picture text -->
Luka Doncic<br>Deandre  Trae Young<br>Ayton<br><!-- End of picture text -->



<!-- Start of picture text -->
Luka Doncic<br><!-- End of picture text -->

17 

##### Interesting Player Trends 





18 

##### General EDA 



19 

##### General EDA 



20 

##### General EDA 



<!-- Start of picture text -->
Luka Doncic<br>Anfernee Simons<br><!-- End of picture text -->

21 

##### Interesting Player Trends 





22 

##### Clustering for Popularity Metrics 



23 

##### Before Modeling 





24 

##### Decision Tree: Predicting Avg Game Score 



25 

##### Decision Tree: Predicting Social Score 





26 

##### In The Beginning 

###### **Initial Research Questions** 

**Packages** 

How do players interact with their fan bases conditioned on the demographic of their home market? Can we quantify "home town bias" among local media outlets for each NBA team? Comparing public perception vs. actual player value (using player stats and social media data) 

TidyCensus 

NBAStatR TwitteR 

27 

##### Stage 1 : Reddit Data 

- Scraped all Reddit posts within subreddit r/nba using RedditExtractoR 

   - Filtered the posts and comments to match the dates of the rookie season (~October 2018 to April 2019) 

- Used bing sentiment analysis on each of the comments to create a sentiment score 



- Resulted in over 2 million rows 

- Grouped comments about each player by week to reduce rows to 296 

28 

##### Stage 4: Final Dataset 

- The game data, Reddit data, and web data were combined to form a data set where each row’s unique identifiers were the player name and the week 



   - 206 observations by 25 variables 

- This data set comprises of 3 types of data; Sentiment data (Reddit), popularity data (Wikipedia and Google trends), and basketball performance data (NBA stat) 







29 

##### Stage 2 : Web Data 

- Used wikipediatrend package to scrape daily Wikipedia page views for each player 

   - Filtered by the dates of the rookie season (~October 2018 to April 2019) 

- Used gtrends package to scrape daily Google image hits, web hits, news hits and YouTube hits for each player 

   - Filtered by the dates of the rookie season 

      - (~October 2018 to April 2019) 

   - Google trends assigns scores from 0 to 100 







30 

##### Stage 3: Game Data 

- Scraped box score data from the NBA stats page 

   - Only looking at 2018-2019 season for players drafted in top 30 

- Each row in this data showed the player’s performance for a game played in the season 

- Game score: a measure of player performance in a given game 



31 

##### Random Forest: Predicting Game Score 



- N_trees  = 40 - 80 with increments of 5 

- M_try = 1 to 6 

- Min_node_size = 3, 5 



32 

##### XGBoost: Predicting Avg Game Score 



Best Tuning Parameters: nrounds = 120, eta = 0.025, max tree depth = 1 



33 

##### Clustering for Sentiment Metrics 





34 


