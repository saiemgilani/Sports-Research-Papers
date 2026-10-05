<!-- source: library/journals/Wharton Sports Analytics Journal/2022/2022 - Whether Weather, Wind Speed and Temperature, Impacts Offensive Success in the NFL - Parks et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/whether-weather-wind-speed-and-temperature-impacts-offensive-success-in-the-nfl/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2022 -->
<!-- authors: Hudson Parks; Cole Ceklosky; Jake Roseman; Jonah Awad; Jimmy Yan -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Whether Weather, Wind Speed and Temperature, Impacts Offensive Success in the NFL

By Hudson Parks, Cole Ceklosky, Jake Roseman, Jonah Awad, and Jimmy Yan

Wharton Moneyball Academy Training Camp 2022, Sports Analytics Student Research Journal

## Introduction & Background

In the NFL, when playing in poor weather conditions, it’s very common for teams to opt for more run-heavy gameplans than they typically would. In theory, this makes sense as the atmospheric conditions of factors such as temperature and wind speed would naturally seem to have a much bigger impact on passing ability than they would on rushing, and therefore rushing may be a more efficient option in these conditions. However, the birth of football analytics and statistics such as expected points added (EPA) have displayed how drastically more efficient passing the ball is than rushing. Our project focused on analyzing different temperatures and wind speeds to see how big of an impact each of these respective weather conditions can have on offensive efficiency in an attempt to answer the question: How do temperature and wind speed affect NFL rushing and passing efficiency?

Goal

Question: How do temperature and wind speed affect NFL rushing and passing efficiency?

● Our x variable for each study was various weather conditions as recorded by nflfastR

● It is important to note that our study does not take into account the possibility of weather changing throughout the game, as nflfastR only displays the weather at the start of the game,, so the weather information is not 100% accurate to the play (instead, since the weather information is only recorded once at the beginning of the game, it is accurate within ~3 hours which is the approximate duration of a game)

Process

● Our data set is play by play information obtained from nflfastR, which tracks information from every NFL play going back to 1999

● We filtered the data to remove

○ All plays that have no weather information (nflfastR began tracking weather information in 2014).

○ All plays that were not runs and passes (takes out all special teams plays and plays resulting in penalties so we can just study runs and passes)

Process Continued

● We measured our data by EPA or Expected Points Added. On every down and distance from everywhere on the field there is an EP, or Expected Points from the offense. EPA is calculated by taking the Expected Points at the beginning of the play and subtracting it from the Expected Points of the situation resulting from the play, hence the phrase Expected Points Added.

● nflfastR tracks 4 different weather conditions in 1 single column as shown below:

● The way nflfastR records this data makes it impossible to graph it without manipulation

Process Continued

● We had to derive the temperature and wind speed numbers out of the column ● We used a multitude of string splitting functions (str_split_fixed), as.numeric functions, and string to integer (stroi) functions to work our way in to derive numbers ● Once we had our new columns with numbers in them, we had to clean up the data so that each indoor temperature and wind speed (which was recorded as N/A) became 72 degrees and 0 wind speed (we did this using is.na functions) ● One other cleaning up method we had to use was to only analyze wind speeds <50 MPH because subjectively we realized that 51-100 MPH wind games were probably a mix of a tiny sample size and bugs with the data ● After that, we sorted all of the numeric data of wind speeds and temperatures into classifications/groups of different intervals to have buckets of these respective measures ● We created 5 buckets in each measure based on a scale of extremity (1-5 scale)

○ Wind: 1-6 MPH = Little to no Wind, 7-14 MPH = Minimal, 15-25 MPH = Significant, 26-34 MPH = Extreme, 35-50 MPH = Insane

○ Temperature: 0-25 degrees = Freezing, 26-50 = Cold, 51-75 = Warm, 76-100 = Hot, 101+ = Extreme Heat

● We created boxplots to represent our data ● The last step was to manipulate the data one step further to find mean ● We ended up needing 32 total datasets to transfer and manipulate all of this data

Disclaimers

● We encountered some trouble working to display our data in a graphically appealing way, so in the end we had to settle on box plots that are scaled in a way that struggles to illustrate the actual differences in EPA. To combat this, we calculated the means for each bucket and displayed them below

● Small numerical differences in EPA actually represent large physical differences because it’s on a per-play basis; for example, the Green Bay Packers led the NFL in passing EPA per play last year at 0.220, and the Carolina Panthers ranked last at -0.158, obviously meaning 30 other teams fall within that seemingly narrow range. However, due to box plots’ property of extending out to capture all the extreme and irregular points, the plots don’t do a great job of illustrating the seemingly small but actually impactful difference, which is why we display the means. Obviously because this is a league-wide average, the numbers are very close to 0

● We found the nflfastR weather data slightly suspicious in general; for example, there were some indoor games listed at a temperature of 0 that we had to manually adjust to 72 degrees, there were the supposedly 51-100 MPH wind speed games we removed, and there were certain temperatures listed for tons of games and then for the next degree there were none listed; the latter could possibly have just been a sorting issue caused by the massive sample size of total plays though. However, by and large the data looks accurate

Wind Speed Study

Mean EPA of each bucket (Ordered left to right, little to insane wind):

0.037 || 0.012 || -0.028 || -0.048 || -0.034

Mean EPA of each bucket (Ordered left to right, little to insane wind):

-0.051 || -0.043 || -0.049 || -0.011 || -0.081

Wind Speed Observations

● There is a significant linear drop off in the Pass EPA/play going from Little to no Wind to Extreme Wind. Interestingly, it bounces back up at Insane Wind, but that’s probably just because of statistical variance in a small sample size, as Insane Wind level games are pretty rare (think the Patriots vs. Bills Monday Night Football game last year, during which Mac Jones threw a grand total of 3 passes in 50 MPH winds).

● The passing variance also decreases in Extreme and Insane level winds, and while you could chalk this up to sample size, it could also be that when teams pass in heavy winds, they elect for much safer throws, hence the lack of super high and super low EPAs. For example, teams would likely be much more hesitant to dial up a 40-yard post route in heavy wind not knowing where the ball may even land.

Wind Speed Observations Continued

● Rushing EPAs remain very constant throughout the lower wind speeds and experience some fluctuation at Insane Wind likely due to sample size

● The Pass EPA box is much bigger between the median and upper quartile than between the median and lower quartile, suggesting that even though passing invokes more risk both ways, the positive outcomes are more impactful than the negatives regardless of the wind

● These are based on the league average, so other team differences such as a quarterback’s arm strength could further bring out the differences

● Rushing has a higher EPA in Extreme Winds, suggesting that in wind speeds of 35+ miles per hour a run-heavy attack is more efficient

Temperature Study

Mean EPA (Ordered left to right, freezing to extreme heat):

-0.035 || 0.002 || 0.023 || 0.026 || 0.216

Mean EPA (Ordered left to right, freezing to extreme heat):

-0.013 || -0.024 || -0.051 || -0.072 || -0.139

Temperature Observations

● Pass EPA sees a very steady increase as temperature increases ○ Likely because hands are colder in cold weather making it harder to throw and catch

● Interestingly, rushing EPA means are at their highest in freezing weather and steadily decline after that. This could be explained by the effect heat has on the fatigue of the linemen and running backs executing these plays. Also, it is harder to tackle in cold weather which makes rushing very effective

## Conclusions!

● Passing generally becomes less effective as the wind increases, while rushing remains roughly the same regardless of the wind

● Passing also becomes more effective as temperature increases, while rushing actually gets worse with heat

● Although, as analytics show, passing is more efficient than rushing in nearly every situation, teams playing in games under 25 degrees in temperature and over 35 miles per hour in wind speed should operate with a more run-focused attack
