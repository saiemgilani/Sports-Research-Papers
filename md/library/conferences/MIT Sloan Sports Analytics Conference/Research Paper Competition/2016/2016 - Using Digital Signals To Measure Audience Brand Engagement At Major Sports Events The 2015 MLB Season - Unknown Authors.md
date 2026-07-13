<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2016/2016 - Using Digital Signals To Measure Audience Brand Engagement At Major Sports Events The 2015 MLB Season - Unknown Authors.pdf -->



# **<u>Using Digital Signals To Measure Audience Brand Engagement At Major Sports Events: The 2015 MLB Season</u>** 

Peter Ibarra, Dstillery Peter E. Lenz, Dstillery 

## **1.** 

## **Introduction** 

Each year corporate brands budget huge sums of money for sports team sponsorships, but few methods exist to validate those expenditures. This research analyzes mobile device location data collected from all MLB stadiums during the 2015 season and the online browsing behavior associated with these devices. By marrying real world location data with online behavioral data, we are able to quantify engagement rates of in-stadium audiences and provide a measurement for the value of in-stadium advertising and team sponsorships. 

To achieve this we: 

1. Identify mobile devices for every baseball game by individual stadium. 

2. Use a robust probabilistic matching algorithm to link mobile devices to a visitor's other devices, including desktop computers. 

3. Calculate an affinity index for the users seen at each stadium, based on online engagement with a brand, interest, or market. 

## **2. Data Collection** 

Data for our experiment originated from three primary sources: real-time bid requests from admonetized sites, online clickstream from third party application service providers and location behavior from software development kit (SDK) integrations. This unique combination of data is crucial to our being able to accurately sample online and mobile location behaviors. Using data from only one stream would greatly narrow our view of overall online behaviors and bring potential biases into our results. 

Our native data collection system was originally developed for the collection of desktop only data. With the growth of smartphones, our system was extended to provide a probabilistic network of connections between all digital devices, also known as a device graph. With this we can tell what mobile devices are connected to what desktop devices, thus giving us a more robust view of the user’s online behavior as they switch devices and locations throughout the day. 

### **2.1. Real-Time Behavioral Data** 

We receive real-time online behavioral data from real-time bid requests and from third party desktop and mobile applications.  Real time bid requests (BRQs) occur when a person is on an admonetized website or an app.  A call comes from the site publisher or app publisher to fulfill an 



2016 Research Papers Competition Presented by: 



1 



advertisement slot.  The call contains information such as an advertising device identifier (cookie, IDFA, AAID), a timestamp, an IP address, the publisher, the ad category and location.  Not all fields are available in all instances of a BRQ.  Third party desktop clickstream and mobile app clickstream are those data streams that are licensed from applications where users have opted-in to provide clickstream behavior in return for the functionality of the application. These data sets allow us to have a broader understanding of online behavior beyond ad-monetized sites and apps. [1] For convenience, we use the term “BRQ” to refer to records collected both through the RTB bidstream and through SDK integrations, as the type of information collected in each is similar. 

### **2.2. Geolocation** 

Location, latitude/longitude, is one of the key signals collected from mobile apps either through the BRQs or third party licensing, For each MLB stadium in the study, we chose the center of the pitcher's mount to represent the centroid of the stadium and created a geofence around this centroid, translating a single point into a specifically crafted polygon.  The geofence specifically contains the entirety of the baseball stadium grounds. Figure 1 below displays an example of the polygon methodology used in this experiment.  A list of baseball stadium centroids (latitude and longitude) is included in appendix A. 



_Figure 1. - Data collection geofence for Citifield_ 



2016 Research Papers Competition Presented by: 



2 



For each mobile RTB bid request and third party app clickstream that contained geospatial data during the 2015 MLB season, we matched location to our stadium geofence. If the BRQ location data fell into the geofence polygon dimensions, we qualified that data for inclusion in our experiment. 

### **2.3 Device Graph** 

In order to get a holistic view of a user’s online behavior, it is necessary to connect sample from the mobile data stream to the desktop data stream. We expanded our device location sample using a device graph. A device graph is a network of device IDs that probabilistically connects an individual user’s devices to one another (smartphone, desktop, laptop, etc.). This bi-partite graph is built using a model that takes IP addresses, location data and time as inputs. Only wifi based IP signals are included in the graph.  Devices that are seen on the same IP address within a specific period of time are considered connected. However, if too many devices are seen on one IP address than the system determines that the specified IP address is public access, a coffee shop or library for example, and prevents the IP from being used to expand a device graph. In this way we are able to avoid false positive connections in the device graph. 

### **2.4 User Affinity** 

We quantify the online behavior of users in terms of user affinities. In this work, we deal with three types of user affinities: brand affinity, market affinity, and interest affinity. 

Brand affinity for a given brand is defined simply by site visitation or app visitation to that brand’s website or app, e.g. a user who has visited the brand’s website is said to have a brand affinity for that brand. Market affinity and interest affinity describe whether the user is in-market for a given product or holds a certain interest, respectively, defined by certain online web or app actions. These are found using classification models, which determine whether each user has, or does not have each affinity. [2] 

Our analysis frequently makes use of the index for a user affinity (either brand, market, or interest) for a given group of users with respect to the full population, as described in the results section. 

### **2.5 Filtering Erroneous Data** 

To ensure the integrity of the BRQ and clickstream data collected, we run every BRQ event through a series of programmatic quality checks. An individual BRQ event can be polluted with good or bad faith errors. We applied three broad filters, Spatial, Behavioral, and Associative, to our data to eliminate any inaccurate or fraudulent data. 

### **2.5.1 Spatial Filter** 

Many impressions carry spatial data that originates from a lookup based in IP address as opposed to a more accurate GPS calculated geo-location provided by a device. These IP-lookup based locations are by their very nature much less accurate than device-generated locations and usually locate to the centroid of the neighborhood, city or even state a device is located in. To combat this issue, our system counts the number of devices per unique location and calculates a distribution of these counts to discover and subsequently filter out these high-count IP-lookup locations. [3] 



2016 Research Papers Competition Presented by: 



3 



### **2.5.2 Behavioral Filter** 

The second filter we employed measures the distance and speed between locations of multiple BRQ or clickstream events from the same device. We filter out results that demonstrate impossible travel speeds between impressions. For instance, if an impression was seen in Austin, TX at 10:00 am and five minutes later in Miami, FL, our system detects this anomaly and all impressions from this device are filtered out. 

### **2.5.3 Associative Filter** 

Our last quality check measures the integrity of the ad inventory being collected. Fraudulent ad impressions often occur on clusters of related websites. Theses sites - colloquially known as bot nets - generate revenue by showing ads to fully automated, computer-controlled, fraudulent users. Using machine-learning processes we are able to identify these clusters of fraudulent sites and the browsers and devices that visit them. Once these fraudulent devices are detected, we eliminate them from our dataset. [4] 

### **2.6 Final Data Set** 

After our data has passed through these three filters, we are left with a dataset containing over 16 million unique and accurate location data points across the entire 2015 Major League Baseball season. 

## **3. Experiment** 

### **3.1. Measurement Model** 

Our goal is to measure brand engagement rates for a Major League Baseball team’s audience. To ensure the devices are reflective of attendees, we referenced the Major League Baseball schedule and collected devices only during scheduled baseball games. These measurements were carried out throughout the entire 2015 MLB season. The total set of users observed at each stadium is the “fan base” of the corresponding team. 

For each set of data, we used our device graph technology to match the devices seen within each stadium to their home computers. Once the connection to home devices has been made, we have the ability to study each attendee’s online browsing behavior and thus quantify the average browsing behavior of the “fan base” relative to every other MLB stadium and to the national average. The empirical probability of a website visit is determined by collecting two weeks of online behavior for every unique user seen at an MLB game. Each website visit for every unique URL is counted for the entire two week measurement period. Once the complete website visit count is calculated for the two week period, we determine the total visit count for a particular URL and divide it by the total population for the fan base. That is, the probability _P_ of a visit to URL _j_ for a team fan base _i_ is given by: 



2016 Research Papers Competition Presented by: 



4 





where _Zj,i_ is the sum of visits to URL _j_ by users in fan base _i,_ and _Ni_ is the total number of users in fan base _i_ . This probability can be interpreted as the probability of brand affinity for the brand corresponding to URL _j_ for users in fan base _i_ . 

Similarly, we calculate _P(j)_ for a random sampling of the full population, or the population of all MLB fans. We can then calculate an affinity index for this brand and fan base: 



We use this index to measure brand sponsorship engagement rate in the sections that follow. 

Analogous indexes can be calculated for the market affinity or interest affinity, based on the number of users in each fan base who show a given market or interest affinity according to our classification models. 

### **3.2. Engagement Evaluation** 

To understand the impact of a corporate sponsorship on a team’s fan base, we wanted to find sponsorships that were specific to a MLB team. For our experiment, we wanted to measure as accurately as possible the impact of a sponsorship by choosing sponsorships that were visible to an audience while attending the team’s games. For this, we chose a major airline (sponsoring the Colorado Rockies), a national hotel chain (sponsoring the Chicago Cubs), and a national bank (sponsoring the New York Yankees). Each of these sponsors had in-stadium advertising, in-stadium seating sections and/or ticket promotions in conjunction with the team. Furthermore, these are brands that tend to lead to online browsing visits, enabling our brand engagement index measurement. 

Once the sponsorships were chosen, we measured how each team’s fan base interacted with the brands webpage. We calculated the brand engagement index, as described in section 3.1. This index quantifies how likely the team’s fan base is to visit the brand’s webpage compared to the population as a whole. 

This method was broken out further by measuring the probability by month over the course of the season. That is, we considered the users seen in July, August, and September, as three separate sets, and applied the same methodology to calculate brand engagement index for each set. The general population’s probabilities were also calculated separately for each month to ensure a consistent measurement, and brand engagement indexes were calculated for each month. 





2016 Research Papers Competition Presented by: 

5 



## **4. Results** 

### **4.1 Summary Statistics for MLB Audience** 

The baseball audience observed over the course of a season presented several unique characteristics. The number of devices seen at only one game at any stadium during the course of the season was between 20-30% across the entire MLB audience. Seventy percent of all devices were seen multiples times. The top three stadiums with the most unique audience were Dodger Stadium, Marlins Park and the Oakland Coliseum. The bottom three stadiums are Great American Ballpark, Kauffman Stadium and PNC Park. The five venues with the highest count of unique users were Dodger Stadium, Busch Stadium, Yankee Stadium, Target Field and PNC Park. 

Two groups of fandom emerged within the MLB audience. The casual fan, which were users that were seen 1-2 times, and the avid fan, which were users that showed up at an MLB stadium 3+ times. Measuring the online browsing behaviors of the two groups against one another showed very distinctive characteristics. 

The casual fan base visited college websites (.edu URLs) while also over indexing on entertainment and music content. This suggested an audience that was much younger in their demographics. While they were indeed attending games across the season, the casual fan browsing affinities suggest their stadium visits were more of a one-time entertainment option. On the other side, the avid group had online content suggestive of a much older audience. Their visitation rates over indexed on financial planning, vacation and investment content. 

### **4.2 Singular Brand Affinity Score Over Time** 

For this experiment, we wanted to measure any change in an audience’s brand affinity score over the course of the season. While scores varied over time, a general trend held true across brands that were also team sponsors.  Brand affinity scores were higher among the MLB fan bases exposed to a sponsorship and generally increased as the season went on. A national hotel chain for the Chicago Cubs, a regional airline for the Colorado Rockies and a national bank for the New York Yankees were the three sponsorship brands studied for this experiment. Figure 2 shows the brand affinity scores for a stadium’s audience for the months of July, August and September. 



2016 Research Papers Competition Presented by: 



6 





_Figure 2. – Sponsorship Brand Affinity Score Over Time_ 

The engagement rate was highest with the regional airline brand sponsoring the Colorado Rockies. The other two sponsorships did not see the same levels of affinity as the airline but still experienced growth as the season progressed. This growth in affinity scores could be attributed to prolonged exposure over the course the season. Additionally, the affinity scores suggest these audiences were not only becoming more aware of the brands but the audiences were also acting upon the exposure to the sponsorship as seen through their online behavior. 

### **4.3 Per Stadium Audience Interest Affinity Scores** 

Beyond the measurement of a brand’s affinity score, we were able to determine each audience’s interest affinity, or the interests expressed through their online behavior. As shown in Appendix B, each audience’s browsing interests could be indexed against the general population and a ranking, by venue, could be determined across all MLB stadiums. 

These interests varied by region and team. Some of the affinity interest ranking were intuitive in their representation of the audience. The top five eco-conscious stadiums were Seattle, San Francisco, Oakland, Washington DC and Denver. The audience interests could also be used to measure the activities these groups participated. An example is the “Grill Masters” category that has a top five stadium list of Kansas City, St. Louis, Minneapolis, Houston and Dallas. 

### **4.4 Per Stadium Audience In-Market Affinity Scores** 

Our analyses also extended to MLB stadium audience's differences in in-market or buying likelihood behaviors. . Using the same methodology employed in the previous affinity scoring, we measure each audience in-market to purchase product behavior as compared to the general population. 



2016 Research Papers Competition Presented by: 



7 



As shown in figure 3, these are the top five and bottom five audiences that are “In-Market” for cars. 

|**Top and Bottom 5 Stadiums for “In-Market”**|**Auto Audiences**|
|---|---|
|**Automotive – Top Five**|**Automotive – Bottom Five**|
|Pittsburgh|NY - Queens|
|Detroit|NY - Bronx|
|Tampa|Seattle|
|Atlanta|San Diego|
|Kansas City|Boston|



_Figure 3. – Top Five and Bottom Five In-Market Auto Stadiums_ 

## **5. Conclusion** 

The merging of unique digital and physical datasets gives us invaluable insight into the relationship between teams, their fans, and their fans interests. Using our device graph technology in combination with geo-location data, we can understand where fans are browsing online and quantify how likely individuals are to engage with a particular brand. Additionally, using our affinity scoring methodology, each stadium’s audience can be ranked by the interests of their fan base. 

We built a model that provides a measurement system to be used by brand marketers and by Major League Baseball teams to understand the effectiveness of sponsorships. Measurements of brand affinity allow for analysis of previous sponsorships, as demonstrated here, and can also extend to inform future sponsorships, thus allowing brands to spend their marketing dollars more efficiently. 

This methodology need not be limited to Major League Baseball. While this particular study was restricted to MLB stadiums, it can be expanded to all sporting venues. Similar analysis could be used to challenge or validate assumptions about which sport’s fan base has the best prospective customers for a given brand. Additionally, this approach can be used to provide insight for individual teams or to gain more knowledge about a region (i.e. Los Angeles sports fans) 

Finally, we envision applications beyond studies of brand sponsorship. We’ve shown that this model allows us to measure the interests of sub-groups of Major League Baseball fans, even within one team’s fan base. Insights into the affinities and behavior of casual fans could inform the marketing strategies of the teams themselves in their efforts to increase game attendance. 

We present a unique methodology that contributes to the understanding of how effective brand sponsorships are to a team’s fan base, and can be extended to many more applications related to understanding the interests and behaviors of actual live game attendees. We believe our measurement system is valuable in shedding light into an area of advertising that has previously been difficult to quantify. 



2016 Research Papers Competition Presented by: 



8 



## **6. Acknowledgement** 

We would like to thank Dstillery and, most especially, the Dstillery data science team, for their invaluable feedback and insight. Their constant willingness to assist and answer any questions we had in our project allowed us to ensure the highest quality. We are deeply appreciative of all their contributions. 





2016 Research Papers Competition Presented by: 

9 



## **References** 

[1] Stitelman, Ori, et al. "Estimating the effect of online display advertising on browser conversion." Data Mining and Audience Intelligence for Advertising (ADKDD 2011) 8 (2011). 

[2] Dalessandro, Brian, et al. "Scalable hands-free transfer learning for online advertising." Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2014. 

[3] Provost, Foster J., Tina Eliassi-Rad, and Lauren S. Moores. "Methods, systems, and media for determining location information from real-time bid requests." U.S. Patent No. 9,179,264. 3 Nov. 2015. 

[4] Stitelman, Ori M., et al. "Methods, systems and media for detecting non-intended traffic using covisitation information." U.S. Patent No. 8,719,934. 6 May 2014. 





2016 Research Papers Competition Presented by: 

10 



## **Appendix A: Stadium Centroids** 

|NAME|LATITUDE|LONGITUDE|
|---|---|---|
|Angel Stadium of|||
|Anaheim|33.800107|-117.883602|
|Globe Life Park in|||
|Arlington|32.751269|-97.082612|
|Turner Field|33.735395|-84.389544|
|Oriole Park at Camden|||
|Yards|39.283833|-76.621684|
|Fenway Park|42.346573|-71.097345|
|Wrigley Field|41.948267|-87.655445|
|U.S. Cellular Field|41.829347|-87.633788|
|Great American Ball|||
|Park|39.097239|-84.506537|
|Progressive Field|41.495984|-81.685285|
|Coors Field|39.756158|-104.994154|
|Comerica Park|42.339057|-83.048626|
|Minute Maid Park|29.75712|-95.355505|
|Kauffman Stadium|39.051579|-94.480345|
|Dodger Stadium|34.073849|-118.239951|
|Marlins Park|25.778053|-80.219427|
|Miller Park|43.028135|-87.971108|
|Target Field|44.981712|-93.277631|
|Citi Field|40.757039|-73.84588|
|Yankee Stadium|40.829615|-73.926351|





2016 Research Papers Competition Presented by: 



11 



|O.co Coliseum|37.750891|-122.201576|
|---|---|---|
|Citizens Bank Park|39.906029|-75.166514|
|Chase Field|33.445486|-112.066682|
|PNC Park|40.446874|-80.005607|
|Petco Park|32.707533|-117.157057|
|AT&T Park|37.778397|-122.389341|
|Safeco Field|47.591445|-122.332366|
|Busch Stadium|38.622634|-90.192862|
|Tropicana Field|27.768311|-82.652324|
|Nationals Park|38.872971|-77.007459|
|Rogers Centre|43.641472|-79.389128|







2016 Research Papers Competition Presented by: 

12 







2016 Research Papers Competition Presented by: 



13 


