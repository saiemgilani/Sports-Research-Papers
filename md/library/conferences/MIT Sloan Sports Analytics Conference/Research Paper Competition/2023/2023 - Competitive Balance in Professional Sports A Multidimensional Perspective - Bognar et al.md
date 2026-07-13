<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2023/2023 - Competitive Balance in Professional Sports A Multidimensional Perspective - Bognar et al.pdf -->

# **Competitive Balance in Professional Sports A Multi-dimensional Perspective** 

Business of Sports ID 272478 

## **1. Introduction** 

Professional sports leagues implement a broad range of competition policies – e.g., salary caps, revenue-sharing, and reverse order drafts – with the aim of promoting _competitive balance_ . Their optimal design hinges importantly on what constitutes a _competitive_ league (Fort & Maxcy, 2003). The conventional view focuses on _within_ - _season_ variation, with a heavy concentration of wins amongst a few teams seen as lacking _balance_ (Butler, 1995). Others have focused instead on _across_ - _season_ variation, e.g., (Schmidt & Berri, 2004) and (Vrooman, 2009). Proponents of this view cite teams frequently moving up and down in the standings from one season to the next as a sign of balance. 

Ultimately, however, competitive balance is a by-product of the distribution of talent. Since we only observe its outcomes, it is not surprising that there exists a lack of consensus on how to measure it and that the methods used to do so vary, e.g., (Lee & Fort, 2005) and (Brave & Roberts, 2019). In fact, the lack of consensus itself strongly suggests that competitive balance is multi-dimensional. What has been left unanswered is the extent to which these competing notions are linked. We propose a simple framework that encapsulates both viewpoints on competitive balance and argue that this unified perspective is essential for understanding how league policies shape competitive landscapes. 

Drawing on insights from game theory, we first show how the degree of competition within sports leagues can be captured along two interrelated dimensions: (i) the _disparity_ across teams within a season (measured by the standard deviation of winning percentages), and (ii) the _immobility_ of teams across seasons (measured by the pooled first-order autocorrelation of winning percentages).  Our model suggests that professional sports leagues often face a trade-off in these two dimensions– e.g., efforts to increase parity can come at the expense of mobility. It also highlights, however, instances where both aspects of competition can improve in sync with each other. 

Using this novel framework, we demonstrate how important structural shifts in the ability of teams to capture talent at below-market wages have influenced competitive balance over the longer run. For instance, we document the positive impact that the introduction of collective bargaining had on the competitive balance of all four major North American professional sports leagues. More recently, however, _both_ disparity and immobility in MLB have increased. We relate this fact to an important structural change in the economics of baseball, namely the rise in importance of non-gate revenue sources and how they are distributed in MLB versus the other leagues. 

We argue based on our framework that substantial increases in non-gate revenues that are largely untied to a team’s performance can adversely reinforce the trade-off between parity and mobility depending on how those revenues are distributed. Team-level two-way fixed effects analysis reveals significant disparities both within and across the North American leagues that help inform how teams’ revenue and payroll growth interact to promote or hinder competitive balance.  Finally, we provide examples of rules that counterbalance the adverse incentives that can arise in these situations. 

1 

## **2. Bargaining over Competitive Balance** 

To illustrate the trade-off between disparity and immobility, we propose a model in which the winning percentage of any team _i_ in season _t_ evolves according to the ARMA(1,1) process, 





where µ ≡ 0.5 to be consistent with the average winning percentage.<sup>1</sup> The parameters θ∊ (0, 1) and φ ∊ (-1, 0) are reflective of league rules governing roster construction. Consistent with the MLB example of (Ferguson, Jones, & Stewart, 2000), we view collective bargaining over these rules between owners and players as a Nash equilibrium outcome over φ and θ, producing a desired wedge between player salaries and their value to the team (i.e. their marginal revenue product). 

The performance shocks η in this framework, thus, reflect teams’ win-share deviations from what they would be expected to garner given their payroll constraints and their (ex-ante) roster of players (or, talent). The moving average term θ > 0 has the feature that these shocks are likely to be persistent, or “sticky,” from season-to-season, embodying the fact that teams—perhaps through long-term contracts, service time manipulation, or similar means—can persistently benefit (ex-post) from players who are paid less than their marginal revenue product. 

To understand the role of the autoregressive term φ, it is helpful to reformulate the dynamic process above in terms of deviations from µ: 



Here, it is natural to see that φ plays the role of a correction term, reinforcing team performances to revert to the mean winning percentage over time. We assume that the league restricts φ < 0 through reverse draft order selection and other collectively bargained rules which facilitate weaker teams in the current season to potentially be made better off in the following season. 

Because we view φ and θ as capturing different aspects of the league rules and institutions surrounding the distribution of talent, it is also natural to assume that the league and its players have different preferences over each, hence the adversarial nature of collective bargaining. However, while we allow this conflict in collective bargaining to determine both φ and θ, it is not without limit. The parameter ω represents a baseline level of variability that is not subject to collective bargaining. This assumption aligns with the underlying uncertainty of the game and player performance across seasons and teams that limit both the league and its teams’ ability to affect the distribution of talent and how that talent determines teams’ wins and losses. 

To see how collective bargaining may affect competitive balance, recall our definitions of its withinseason ( _disparity_ , _Dt_ ) and across-season ( _immobility_ , _Mt_ ) dimensions: 

1 A subtle modification of this model that would allow for additional persistence in team winning percentages without changing the results that follow is to have µ� = 0.5 + 𝛼� with 𝐸(𝛼�) = 0. 

2 

𝐷� ≡𝑆𝑡𝑑[𝑤��] (3) 



We can express them as a function of model parameters that players and owners bargain over, 



where 𝑀�(𝜑, 𝜃) is strictly increasing and 𝐷�(𝜑, 𝜃) is strictly decreasing in _φ_ over its range _._ 

In the case of φ, we show below that, conditional on being negative (i.e., rules that foster support for last year’s weaker performing teams), a change in φ can improve one dimension of competitive balance (e.g., _immobility_ ) only at the cost of deteriorating the other dimension (e.g., _disparity_ ). Moreover, it is natural to assume that owners and players alike view both dimensions of competitive balance as appealing, so to the extent that differences of opinion exist in collective bargaining they are likely to be on the relative weight each side assigns to them. 

In the case of θ, we show in figure 1 that, conditional on φ being negative, increases/decreases in θ lead to unambiguous improvements/deteriorations in competitive balance. However, it is also likely that in terms of league rules that contribute to θ, players’ and owners’ preferences would conflict. Given our interpretation of 𝜂�� as representing the wins attributable to deviations of player performances above market wages, θ serves as a control right afforded to owners to capture the value of ex-post beneficial roster constructions. Thus, we view it as natural that owners would want θ to be as high as possible, whereas players would want θ to be as near zero as possible. 

Figure 1 illustrates these competitive balance functions over the range φ ∊ [−θ , −0.01] for a set of parameter values (σ = 0.3, θ = 0.8) and (σ = 0.3, θ = 0.9). If, as we assume, the league prefers to minimize both disparity and immobility, then it will not choose φ < -θ, as it could reduce both by choosing φ > -θ. However, over the range (−θ, 0) the league faces a trade-off in decreasing immobility at the cost of creating more disparity or decreasing disparity at the cost of creating more immobility. Alternatively, as evidenced by the outward shift of disparity and immobility obtainable when θ varies from 0.8 to 0.9, collectively bargained rules that result in an increase of θalso result in unambiguous decreases in competitive balance on both of its dimensions. 

In summary, while players and owners are likely to have different preferences for both dimensions of competitive balance, those preferences are also more likely to be aligned in terms of the appropriate value of 𝜑, in part because of the trade-off that exists for this feature of the model. However, by the same token, they are also likely to be very different for 𝜃 given its interpretation of control rights over (ex-post) beneficial contractual terms. Changes in the contractual rights of players to switch teams are, thus, a crucial determinant of both parity and mobility in this framework. Moreover, 𝜃 has the feature that increases in it will tend to produce more competitively imbalanced outcomes for both. 

3 



**Figure 1. Illustrating the Competitive Balance Trade-offs** 

Notes: This figure summarizes as competitive balance frontier curves the main implications of our ARMA(1,1) model for team winning percentages on our two measures of competitive balance: _disparity_ and _immobility_ . Movements along the competitive balance frontier reflect the trade-off captured in the model’s AR(1) term, while shifts in the frontier curve reflect the model’s MA(1) term. 

4 

## **3. Competitive Balance & Non-gate Revenues** 

We focus on the types of policies that are more likely to affect θ than φ and the implications of our model for their impact on competitive balance. The top left panel of figure 2 provides an excellent example from MLB. The introduction of collective bargaining directly affected control rights over contractual terms, leading to the end of the reserve clause and the rise of free agency in MLB in the late 60’s/early 70’s. This improved the bargaining position of players such that the _equilibrium_ θ decreased, leading to simultaneous _improvements_ in both parity and mobility and overall competitive balance as more and more players were paid their marginal revenue products. 

A similar pattern can also be seen over time in the remainder of the big four professional North American sports leagues (i.e., the NFL, NBA and NHL) in the other panels of figure 2. To make crossleague comparisons easier, each panel indexes disparity and immobility values relative to the 2019 season, with positive values indicating a higher level than in 2019 and negative values indicating a lower level. Interestingly, the timing of the largest improvements in competitive balance in these other leagues is very much like that of MLB. This is consistent with the observation that these other leagues also implemented collective bargaining around the same time as MLB. 

Where we find the biggest differences across leagues is the magnitude of the improvements in our competitive balance measures. But, here, we must be careful. Disparity is likely to vary substantially across leagues simply because of extreme differences in season lengths (e.g., 16 games in the NFL compared to 81 in the NBA or NHL and 162 in MLB). This is clearly visible in comparing the average values of disparity for each league in figure 2.  That said, each league has seen disparity substantially improve on its own scale over the last 35 years or so. Immobility, on the other hand, is not affected as much by season length, with all four leagues converging to a similar relative value over time. 

We are also interested in situations where both measures of competitive balance have _deteriorated_ simultaneously, e.g., what has happened over the last decade or so in MLB. Below, we argue that the primary driver of this development was a substantial increase in the importance of non-gate revenues and how they were distributed across teams. Given that this revenue source tends to be less sensitive to a team’s winning percentage, owners upon receiving these revenues have a more advantageous bargaining position relative to players. In other words, the _equilibrium_ θ  would increase. An additional prediction of our model is then that the players’ share of league-wide income would consequently decrease, a fact that aligns with the recent experience of all four leagues as seen in figure 3. 

Note, however, that only MLB has experienced a _substantial_ deterioration in _both_ measures of competitive balance consistent with an increase in our model parameter θ . The NBA has instead seen a small increase in disparity over this timeframe but not immobility, whereas the NFL has witnessed the opposite pattern. The NHL, on the other hand, has seen immobility fall with disparity roughly unchanged. These developments are more consistent with a shift along the curve shown in figure 1 as influenced by our model parameter φ. This suggests that how each league and its teams have responded to these new non-gate revenue sources differs substantially and provides some variation that we can use to identify best practices.  Before we dive into the team responses, however, let’s take a closer look at the MLB experience relative to its peer leagues over the last twenty years. 

5 



**Figure 2. Competing Measures of Competitive Balance** 

Notes: This figure reports annual measures of league _disparity_ (red dots) and _immobility_ (blue dots) normalized relative to the 2019 season by subtracting each annual measure by the relevant 2019 value. League disparity measures the standard deviation of winning percentages across teams within a single year. League immobility measures the (pooled across teams) first-order autocorrelation of winning percentages (i.e., from year to year). Data are from Rodney Fort’s Sports Business Data. 

6 



**Figure 3. Non-gate Revenue and Player Salary Shares of League Revenue** 

Notes: Each panel shows estimates of the shares of non-gate revenue and player salaries to total league revenue by year from 2002-2019.  Data are from Rodney Fort’s Sports Business Data 

7 



**Figure 4. League Financials: 2002-2019** 

Notes: This figure shows estimates of total gate revenue, non-gate revenue, payroll, and franchise value by year for each league in billions of 2018 U.S. dollars. Data are from Rodney Fort’s Sports Business Data with the U.S. Consumer Price Index from the Bureau of Labor Statistics used to deflate them. 

8 



Using estimates of teams’ balance sheets, figure 4 demonstrates that non-gate revenue growth has significantly outpaced that of gate revenue since 2009 in all four leagues (Fort, Rodney Fort's Sports Business Data, n.d.). Where did this explosion of revenue come from? For MLB, national TV deals (Brown, 2014) along with the sale of MLB Advanced Media and its assets (Calcaterra, 2017) are prominent examples. MLB owners have significantly benefitted from these developments, with league-wide franchise values increasing 225% over the same period (Forbes, n.d.). Competitive balance, on the other hand, has not. After the national TV deal went into effect during the 2014 season and the proceeds of the sale of MLB Advanced Media to the Disney Corporation were distributed during the 2018 season, both measures of competitive balance deteriorated. 

If MLB teams had tended to pass through this windfall to player salaries in free agency, then competitive balance along either of our two dimensions may reasonably have improved instead by enabling struggling teams to attract and retain more talented players. All else equal, this effect would likely be most pronounced in an environment in which free agency is the primary means by which teams accrue talent. Teams would then use their additional revenue to compete against one another more intensely for the limited number of free agents available each offseason. This increased competition would ultimately benefit players in the form of higher salaries. 

However, panel A of figure 3 demonstrates that this was clearly not the case in MLB: while the share of total revenue attributable to non-gate sources increased after 2009, the players’ share of total revenue experienced steady declines. Rather than benefiting from their teams’ improved balance sheets, players appear to have received an increasingly diminished share of their teams’ income. This is true in terms of the general level of salaries as well, irrespective of team revenue sources. The average MLB player salary declined by 6% from 2017-2021 (Statista, n.d.) and has fallen in three out of the last four years. Before the 2017-18 decline, it had not fallen since 2004. 

But if you stare long enough at both figures 3 and 4, it is hard to see how the rise of non-gate revenue alone would have contributed to MLB’s decline in competitive balance. The other leagues also experienced similar increases in the importance of non-gate revenue sources and declines in their players’ share of income over this period without the kind of widespread deterioration in competitive balance that we find for MLB. So, what is it about MLB that makes it different from the others? Our hypothesis is that the difference is institutional and related to the way that both talent is developed and paid at the team level and how non-gate revenues are shared within each league. 

Our model suggests two ways in which rising non-gate revenues may contribute to lower competitive balance. First, team owners may not be incentivized to attract better talent by passing the revenue gains through to higher player salaries. Historically, in MLB non-gate revenue has been viewed as the least sensitive revenue source to on-field performance (Blass, 1992). Thus, as teams became less dependent on gate revenue, they may have also become more willing to endure periods of low gate receipts brought on by paying rock-bottom player salaries. Such behavior is also consistent with teams employing an “all-or-nothing” type strategy that has become commonplace in MLB, where periods of limited on-field success are viewed as the necessary price to pay to develop younger, cheaper talent that maximizes the likelihood of future success. 

Second, league rules dictating free agency and the cost and availability of player talent are largely a function of collective bargaining in professional sports. If the rise in non-gate revenue indeed diminishes the importance of on-field performance for profits, then the owners’ bargaining power 



9 



in CBA negotiations is likely to have increased. Standard non-cooperative theories of bargaining predict that resulting CBAs would in equilibrium be more (less) favorable to owners (players). One need not look far for recent examples in MLB which confirm this conjecture, with the slotting of draft picks and rules governing international signings as prominent examples which lowered the cost of pre-free agent talent considerably and reinforced team owners’ existing preferences. 

In the context of our model, such rules would lead to higher values of 𝜃 and the subsequent deterioration in competitive balance that we observe in figure 2. However, this framework is largely silent on the mechanisms underlying these changes at the team level. As hypothesized above, increases in non-gate revenue could theoretically improve competitive balance if they primarily accrued to small-market teams that would otherwise struggle to offer competitive contract offers to players, (even pre-free agent talent that they may be forced to trade if arbitration salaries were too high). This suggests that we can further test our hypothesis by examining how non-gate revenue and payroll at the team level evolved over this time in each of the four leagues and look for distinct differences in MLB versus the other leagues. 

## **4. Team Behavior & Revenue Sharing** 

To quantity differences in team behavior across the four North American professional sports leagues, we estimate team-level two-way fixed effect regressions of the following form: 



where log 𝑌�� denotes the natural log of either non-gate revenue or payroll in 2018 U.S. dollars<sup>2</sup> for team _i_ in year _t_ . We normalize 𝛽���� = 0 such that 100*𝛽� represents the average percent change in 𝑌�� for team _i_ in year _t_ relative to its value for team _i_ in 2009. 

Figure 5 plots our estimates of 𝛽� along with 95% confidence intervals, demonstrating how team non-gate revenue and payroll have evolved over time across each of the four North American sports leagues. For example, these estimates show that the average MLB team’s non-gate revenue (top left panel) increased by 49% from 2009 to 2018 with a 95% confidence interval of [45%, 54%]. Contrast this with the evolution of total payroll in MLB (see figure 6; top left panel), where total payroll increased by 17% from 2009 to 2018 with a 95% confidence interval of [3%, 30%]. 

> 2 We deflate all team finance data using the U.S. Consumer Price Index (CPI). 



10 







**Figure 5. 2002-2019 Team-Level Non-Gate Revenue and Payroll Growth** 

Notes: This figure plots the coefficient estimates (and confidence intervals) for each of the year fixed effects estimated in equation (5) with log of non-gate revenue and log of payroll, respectively, as the dependent variables. The 2011 coefficients in the NBA panels correspond to the 2011-2012 lockout-shortened season. The 2012 coefficients in the NHL panels correspond to the 2012-2013 lockout-shortened season. 



11 



There are three important insights that we can glean from figures 5 and 6. First, the non-gate revenue shares displayed in figure 4 are not driven by just a handful of teams. Rather, on average teams in each league experienced significant increases in non-gate revenue. Second, while the average payroll increased across all four leagues during this time (in contrast to a declining share of payroll with respect to total revenue), this growth was driven almost exclusively by the 20142019 period. Payroll growth in MLB, the NBA, and the NFL was roughly zero over the 2006-2014 period and was only slightly positive in the NHL. Third, while we cannot rule out that some teams used their non-gate revenue gains to fund payroll growth, any such investments were far smaller than average non-gate revenue growth – an empirical pattern that holds across all four leagues. 

As in figures 3 and 4, these trends across leagues suggest some commonality in how the explosion in non-gate revenue growth affected each league. How, then, do we reconcile these consistent cross-league patterns with the different trends in competitive balance between MLB and the other leagues shown in figure 2? As seen in figure 6, decomposing these team-level effects according to the average franchise value of teams in the 2002-2009 period reveals important differences across leagues. Specifically, we categorize teams in each league into three categories: “Low Franchise Value” (the bottom quartile of franchise values), “Middle Franchise Value” (the middle two quartiles), and “High Franchise Value” (the top quartile). We then separately estimate the coefficients for equation (5) for each of these categories across both non-gate revenue and payroll. 

These categories represent the relative financial heft of franchises within leagues and capture traditional small-vs-large market distinctions in how non-gate revenues are distributed across leagues. The top panel of figure 6 demonstrates that MLB is a distinct outlier in this regard. On average, non-gate revenue growth for the highest value franchises was nearly twice as large as that for the lowest value franchises. This pattern disappears in the other leagues: non-gate revenue increases were shared evenly across teams in the NFL and NHL, while the lowest value NBA franchises gained more than the highest value franchises. These patterns are highly consistent with the salient features of revenue sharing differences across these leagues. 

As noted, MLB has experienced dramatic changes in the sources of non-gate revenue, with largemarket franchises benefiting tremendously from lucrative local TV deals. Coupled with relatively less generous revenue-sharing, it is unsurprising that the highest value franchises have experienced the greatest increase in non-gate revenue. Conversely, the NBA institutes aggressive revenue-sharing policies that ensure that the least valuable franchises benefit from league-wide revenue growth, perhaps accounting for its distinction as the only league for which these franchises gained the most from the broad-based increase in non-gate revenue. While the NFL institutes less generous revenue-sharing than the NBA, it is also much more reliant on shared national TV deals to drive non-gate revenue than MLB franchises are. 



12 







**Figure 6. 2002-2019 Team-Level Financial Growth by Franchise Values** 

Notes: This figure plots the coefficient estimates (and confidence intervals) for each of the year fixed effects estimated in equation (5) separately for low, middle and high value franchises with log of non-gate revenue and log of payroll, respectively, as the dependent variable. 



13 



The bottom panel of figure 6 demonstrates within-league differences in payroll growth that are also informative of differences in competition policy across the four leagues. The NFL again demonstrates little cross-franchise variation in payroll growth, a likely consequence of the strict “hard cap” on annual payroll. Similarly, the NHL experienced some variation across teams during this time, but growth was tightly clustered again across franchises due to a hard salary cap. In contrast, MLB and the NBA tell a more nuanced story, likely because they institute “soft caps” that allow teams to exceed a fixed level of payroll while incurring a “luxury tax” for such expenses. 

Payroll growth in MLB over the 2014-2019 period was _entirely explained_ by franchises outside of the top quartile of franchise values in the 2002-2009 period. Despite receiving the smallest share of non-gate revenue gains, these franchises still were the most likely to pass on non-gate revenue growth to payroll. Given the patterns that we document in figure 2, it seems these gains still were not enough to halt the overall decline in competitive balance in MLB. However, it does suggest that the teams with the most to gain competitively from spending more– low value franchises – were also the most likely to respond to non-gate revenue increases via player expenditures. 

Mirroring cross-team patterns in non-gate revenue growth for MLB, the lowest value franchises in the NBA also increased payroll the most after 2014. Given the encouraging trends in our competitive balance measures for the NBA, this league perhaps represents a model for MLB on how non-gate revenue sharing can promote competitive balance: non-gate revenue-sharing in the NBA predominantly places money in the hands of the teams that are most likely to spend it competitively. This enables teams to compete in free agency when combined with a luxury tax that prevents the wealthiest franchises from effectively pricing others out in free agency. 

## **5. Conclusion** 

Overall, our regression results demonstrate that the substantial increase in non-gate revenue over the last 10 years in MLB primarily benefited the most valuable teams (which, for the most part, happened to be the more successful large-market franchises). As these trends relate to competitive balance, they support the idea that non-gate revenue windfalls created a source of revenue less reliant on team performance, which allowed the wealthiest teams to reduce their payroll relative to overall revenue. Moreover, it is reasonable to think that the CBAs that were signed in 2012 and 2017 reflected this shift due to an improved bargaining position for owners. 

The heterogeneity across teams in MLB also suggests an additional mechanism through which competitive balance may have declined: because the wealthiest teams benefited the most from increases in non-gate revenue, they may have also gained bargaining power over their fellow, less wealthy, owners. Consistent with this, much of the discussion around competitive balance in MLB has been focused on the luxury tax system. Our results provide strong evidence that the luxury tax system operates as a soft salary cap for large-market teams. In terms of our model, however, it is not clear that this is the reason for the decline in competitive balance. 

For example, imagine if the league-wide gains in non-gate revenue had been distributed according to on-field performance in MLB instead. The bargaining position of large-market vs. small-market owners may not have changed as much with these revenues again tied to winning percentage, and the bargaining position of players not declined as much either. In our model, this would enhance competitive balance. Moreover, in that case an expansion of the playoff field—a recent CBA 



14 



change that increases non-gate revenue for eligible teams—would reinforce these effects. 

Viewed in this light, while the changing economics of MLB are likely the source of its newfound competitive imbalance, teams have simply been responding as expected given the collectively bargained rules that govern them. Changing team behavior requires different rules. It is interesting to note then that small-market teams in MLB did still increase their payrolls on average over this period, suggesting they may in fact have used their non-gate revenue windfalls to field more competitive teams. Recent CBA discussions that focused on a salary floor are, therefore, likely to have been misguided if the aim was to enhance competitive balance. 

Even if MLB is not capable of replicating the NBA model for revenue sharing that seems to have worked well in handling the explosion of non-gate revenues, there are other alternatives. From the player’s perspective, another prominent concern is the time to reach free agency. Clearly, the sooner that occurs the quicker the player can capture his full marginal revenue product in our framework and the more likely that payrolls are to increase. Small-market owners are understandably wary of the upward pressure on payroll that would result. Because the luxury tax system would continue to limit payroll growth for large-market teams, the increases in payrolls would likely have to come from enhanced competition for talent among them instead. 

It is hard to argue, however, that shortening the time to free agency would not improve competitive balance in MLB. With players free to change teams more often, talent levels across teams should be less sticky from year-to-year. The evidence we presented in figure 1 on the introduction of collective bargaining and free agency in baseball is a good example of this. The bigger question, however, is how best to structure league rules to allow for this to happen without overburdening the small-market teams. Our results suggest that anything that more closely aligns non-gate revenues with on-field performance would be a step in the right direction. 



15 



## **References** 

- [1] Blass, A. (1992). Does the baseball labor market contradict the human capital model of investment? _Review of Economics and Statistics, 74_ , 261-268. 

- [2] Brave, S. A., & Roberts, K. A. (2019). The Competitive Effects of Performance-Enhancing Drugs: MLB in the Posttesting Era. _Journal of Sports Economics, 20_ (6), 747-781. 

- [3] Brown, M. (2014, December 10). Retrieved from Forbes: https://www.forbes.com/sites/maurybrown/2014/12/10/major-league-baseball-seesrecord- 

   - 9-billion-in-revenues-for-2014/?sh=85fcb729c103 

- [4] Butler, M. R. (1995). Competitive Balance in Major League Baseball. _The American Economist, 39_ (2), 46-52. 

- [5] Calcaterra, C. (2017, December 15). Retrieved from NBCSports: https://mlb.nbcsports.com/2017/12/15/each-owner-will-get-at-least-50-million-inearly-2018-from-he-sale-of-bamtech/ 

- [6] Ferguson, D., Jones, J. C., & Stewart, K. (2000). 2000. _Review of Economics and Statistics, 82_ , 422-430. 

- [6] Forbes. (n.d.). _The Business of Baseball_ . Retrieved from https://www.forbes.com/mlbvaluations/list/ 

- [7] Fort, R. (n.d.). Retrieved from Rodney Fort's Sports Business Data: https://sites.google.com/site/rodswebpages/codes 

- [8] Fort, R., & Maxcy, J. (2003). Competitive balance in sports leagues: An introduction. _Journal of Sports Economics, 4_ (2), 154-160. 

- [9]Lee, Y. H., & Fort, R. (2005). Structural change in MLB competitive balance: The depression, team location, and integration. _Economic Inquiry, 43_ (1), 158-169. 

- [10] Schmidt, M., & Berri, D. (2004). Another look at competitive balance: a regime switching approach. _Applied Economics, 36_ , 2453-2460. 

- [11] Statista. (n.d.). Retrieved from https://www.statista.com/statistics/236213/mean-salarayof-players-in-majpr-league-baseball/ 

- [12] Vrooman, J. (2009). Theory of the Perfect Game: Competitive Balance in Monopoly Sports Leagues. _Review of Industrial Organization, 34_ , 5-44. 



16 


