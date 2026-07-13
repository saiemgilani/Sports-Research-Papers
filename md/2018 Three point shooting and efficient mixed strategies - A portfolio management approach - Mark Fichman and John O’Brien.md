<!-- source: 2018 Three point shooting and efficient mixed strategies - A portfolio management approach - Mark Fichman and John O’Brien.pdf -->

107 

Journal of Sports Analytics 4 (2018) 107–120 DOI 10.3233/JSA-160154 IOS Press 

# Three point shooting and efficient mixed strategies: A portfolio management approach 

## Mark Fichman<sup>∗</sup> and John O’Brien 

_Tepper School of Business, Carnegie Mellon University, Pittsburgh, PA, USA_ 

**Abstract** . Using mean/variance investment theory, we identify the efficient mixed shot type strategy for National Basketball Association (NBA) teams. The proportion of 3-point shots in this mixed strategy closely tracks risk and the change in expected points from 1979–2014. We then extend this approach to an individual team level for both offense and defense. This measures both the risk associated with implementing a mixed strategy (for and against an individual team) and the implied shot type efficiency for offense and defense. It is the latter, shot type efficiency, which predicts winning and winning point differential. 

Keywords: Sports, Professional Basketball, mixed strategies, sports strategy 

### **1. Introduction** 

In any competitive sport, rules are put in place that are intended to control and influence the way players or teams compete. In basketball, rule changes are often made to influence how the game is played. For example, adding the shot clock in the National Basketball Association (NBA) in 1954 quickly changed the pace of the game, increasing scoring and ending stalling tactics. Basketball changed almost immediately as scoring went from 79.5 points per game in the 1954 season to 93.1 points per game in the 1955 season. Within 5 seasons, every team was averaging over 100 points per game. The rules changed and within 5 years, teams had all adapted and created a different, faster style of play. The change was not instantaneous because time is required to adjust tactics, personnel and training of basketball players to the shot clock. At that time, no basketball player would have been training with a shot clock in high school, college or in 

> ∗Corresponding author: Mark Fichman, Tepper School of Business, Carnegie Mellon University, Schenley Park, Pittsburgh, PA 15213, USA. Tel.: +1 412 268 3699; E-mail: mf4f@cmu.edu. 

industrial leagues. The most profound change to the rules of American NBA basketball in recent decades has been the introduction of the 3-point shot. Again, the impact of the change was not immediate and the change is still affecting game strategy. Evidence of this is the fact that there has been an increasing trend for the percentage of 3-point shots used by teams in the NBA, increasing from virtually none (3.05 % to be precise) in the 1979-80 season when the shot was introduced in the NBA to 28.4 % in the 2015-16 season (see Fig. 1 below)<sup>1</sup> . Furthermore, the NBA Most 

1Readers might assume that the change in frequency of 3-point shooting is due to increased skill at 3-point shooting, but that is not a sufficient explanation. In the 1980 season, the Boston Celtics had a team 3-point shooting percentage of .384, which would have been second best in the 2016 NBA season. The leading 3-point shooter, Fred Brown of Seattle (‘Downtown Freddie Brown’) had a shooting percentage of .443. The second and third best 3-point shooters were Chris Ford (Boston) at .427 and Larry Bird (Boston) at .406. These players were known as excellent jump shooters, but still Boston only attempted 422 3-point shots. 422 attempts were the second most in the NBA, but still only 5.7% of Boston’s field goal attempts. So there was skill and there was recognition of that skill. But only Chris Ford was among the top 5 players in number of 3 point shots attempted. 

2215-020X/18/$35.00 © 2018 – IOS Press and the authors. All rights reserved 

This article is published online with Open Access and distributed under the terms of the Creative Commons Attribution Non-Commercial License (CC BY-NC 4.0). 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

108 



<!-- Start of picture text -->
1.2<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>1979 1984 1989 1994 1999 2004 2009 2014<br><!-- End of picture text -->

Fig. 1. Expected points from 2- and 3-point shots for the NBA as a whole. 

Valuable Player award for both the 2015 and 2016 seasons was won by Stephen Curry, a skilled 3-point shooter. In this paper we analyze the adaptation of the game to the 3-point shot which in turn allows game outcome predictions to be made including where the game is headed in terms of aggregate two and 3-point shooting strategies. 

When analyzing 3-point shots, we first observe that both the mean and variance of the probability of a successful 2-point shot for the NBA have remained relatively stable over this time, whereas the probability of a successful 3-point shot has exhibited an increasing trend for its mean and a decreasing trend for its variance (See Fig. 2 below). Until 1987 the expected points from 2-point shots (2 points*probability of a successful 2-point shot) was higher than the expected points from 3-point shots. This reversed after 1987 up until current time (see Fig. 3). For the case of the variance of the probability of a successful 3-point shot, this has remained higher than the variance of the probability of a successful 2-point shot for the NBA each year, over the entire time period. This happens even though the variance of a successful 3-point shot has decreased over this same time period. Combined these observations suggest that not only the expected points from a shot 



<!-- Start of picture text -->
0.00006<br>0.00005<br>0.00004<br>0.00003<br>0.00002<br>0.00001<br>0<br>1979 1984 1989 1994 1999 2004 2009 2014<br><!-- End of picture text -->

Fig. 2. Risk Characteristics of 2 and 3-point shots for the NBA as a whole. 



<!-- Start of picture text -->
Correlations between shot types over time<br>0.4<br>0.2<br>0<br>-0.2<br>-0.4<br>-0.6<br>-0.8<br>Correlations<br><!-- End of picture text -->

Fig. 3. Correlations between Shot Types Made. 

type matters but also the variance or risk associated with a successful shot type matters. The latter follows because if only expected points from a shot type matter then we would observe 100% 3-point shots since 1987, which obviously did not happen. As a result, when making predictions about outcomes from NBA games, as well as describing shot type strategy, requires considering both risk and expected points from each shot type. 

To formally analyze this problem, we adopt the finance approach of considering the mean, variance and covariance of expected payoffs from successful 2- and 3-point shots. That is, a team can treat their game strategy as a portfolio of shot types that have an associated risk and return. Our analysis draws heavily upon modern portfolio theory (MPT) and the Capital Asset Pricing Model (CAPM) to analyze NBA basketball strategy. Modern portfolio theory allows us to first explain and predict 3-point trends for the NBA as a whole and we find that the proportion of 3-point shots in this mixed strategy closely tracks risk and expected points changes for 3-point shots in the NBA from 1979–2014. We then shift attention to the individual team level by applying the CAPM to describe both the offensive and defensive strategies at a team level. This provides us with a pricing model for shot types at a team level for both offense and defense. The advantage of this approach is that the slope of the defensive and/or offensive shot type pricing models reveal whether a team can more easily (i.e., at lower cost) defend against and/or make 3-point shots. In turn these results can be applied to problems ranging from predicting post season success to developing a strategy when playing against a team as well as engineering an NBA team. In the current paper we focus upon the prediction issue. In all ouranalyses,weareasking,overthecourseofagame, what mixture of 2 and 3-point shots should a team try to achieve _. We are not asking, on any particular possession, what type of shot a team should attempt._ 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

109 

_Rather, over a series of possessions such as a game or a season, what percentage of shots should be of each type?_ 

This investment theory approach to identifying optimal mixed strategies also highlights the importance of risk aversion in the NBA. For example, professional golfers, playing for large prizes in golf tournaments, show evidence of loss aversion (Pope & Schweitzer, 2011). Professional football coaches, when making decisions about whether to ‘go for it’ on fourthdown,showsimilarbehavior(Romer,2006).In both cases, golfers (who seem more sensitive to going over par (bogey) than to being under par (birdie)) and football coaches (who avoid the risk of failing to get a first down even when that is, in expectation, the more attractive option), players with high stakes reveal the influence of risk aversion upon their choice behavior. The NBA added a 3-point shooting line to the game in 1979, introducing a new and risky choice for coaches and players. The farther one is from the basket the greater the risk of not scoring. Prior to 1979, the NBA only had 2-point field goals. In 1979, after the NBA introduced the 3-point shot, only 3 percent of shots attempted were 3-pointers and the expected points from a 3-point shot was lower than the expected points from a 2-point shot. This reversed in 1986 such that expected points from 3-point shots exceeded the expected points from 2-point shots up to today. However, since 1986 the use of the 3-point shot has increased but does not dominate 2-point shooting as expected in a risk neutral world. This raises the several questions, such as: 

“Currently in Europe it is quite customary to watch games where teams shoot more three-pointers than two-pointers. It will happen in the NBA, and soon.”<sup>2</sup> Will it happen? While we do not answer this question, our framework provides a basis for suggesting whether it should happen. 

In section 2 of this paper we motivate and apply mean/variance investment theory to basketball. That is, we analyze the relationship between the changes in the underlying statistical distributions generated from 2- and 3-point shot types over time with the observed proportions of 2- and 3-point shots taken over the same time periods. This relationship is used to both evaluate and predict performance. Finally, to make this evaluation concrete in terms of modern basketball terminology, we relate our economic variables to 

> 2N.B.A. Landscape Altered by Barrage of 3-Point Shots. April 29, 2013 http://www.apbr.org/forum/viewtopic.php?f=6 &t=4662&p=19464&hilit=three+pointer 

traditional basketball performance measures. From the perspective of existing sports analytical research in basketball our emphasis is on providing a game theoretic analysis of realized shot distributions, as opposed to studying within game behavior, as others have done (Goldman & Rao, 2012; Oliver, 2004; Skinner, 2012; Lucey et al., 2014). This work can be used to analyze shot distributions within a game, but we do not do that here and leave that task for future research. 

### **2. Efficient mixed basketball strategies** 

The game of basketball has two simple objectives for any team. The team wants to score points (offense) and prevent their opponent from scoring points (defense). The team that scores the most points wins the game. Associated with each shot type are expected points from making a successful shot and risk, because shots will either succeed or fail. The coach in any game has a strategic choice to make. How to play the game and what players to put on the floor to execute the coach’s strategy is the problem the coach needs to solve. Suppose the coach chooses to only shoot 2-pointers and puts players suited to that strategy on the floor and always plays to shoot near the basket. Then the other team’s defense would collapse near the basket and make success very difficult (i.e., ‘protecting the paint’). Suppose the coach chooses just to shoot 3-point shots? Then the defense adapts to that by crowding the 3-point line and making those shots as difficult as possible. The coach realizes the team needs a mixed strategy where the team shoots some 3-point shots and some 2-point shots. Now the coach has to ask, how many shots of each type should my team shoot? The choice the coach makes we define as the mixed strategy in this paper. 

NBA coaches and players understand this. 

The analogous problem exists and has been solved in finance by analyzing the tradeoff between risk and return to identify the right combination of risky assets in an investment portfolio. The risks and returns are studied by first representing the returns from each risky asset in a mean/variance framework and then solving for the optimal portfolio weights relative to the investment objective. If return distributions change then so do the predicted portfolio weights. This is referred to as “modern portfolio 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

110 

theory” or MPT analysis. The same analysis is relevant and applicable to basketball by representing shot types in a mean/variance world. Here is an example. In 1994, the NBA moved the 3-point line closer to the basket (uniformly 22 ft. instead of 23 ft. 9 in.). As a result, the risk (i.e., variance) from taking 3-point shots was reduced, and expected points increased. Teams _immediately_ started shooting significantly more 3-point shots, showing that the coaches were prepared to tradeoff risk and return. As the risk went down and the return increased, 3- point shooting took off. Three years later, the NBA moved the line back to 23 ft. 9 in. Coaches immediately responded to the increased risk created by this change, reducing the number of 3-point shots attempted. Modern portfolio theorists recognize this behavior as a rational, correct response to the changes in the mean and variance of returns from 2 and 3-point shots. 

- _2.1. An economic analysis of basketball: An overview_ 

In this paper we identify the efficient mixed strategy for the NBA in aggregate by maximizing the Sharpe Ratio (SR), which is defined here as the expected points divided by the volatility of points. The optimal proportion of 3-point shots for the NBA is then identified from the efficient mixed strategy. 

We then extend this aggregate analysis to the individual team level. In this extension we identify the efficient mixed offensive and defensive strategies by maximizing the SR for each team in each year. The efficient mixed strategies are computed from the offensive (shots made) and defensive (shots given up) distributions. For offense a larger SR is preferred to smaller because this implies that the expected points per unit of risk is higher. The opposite applies to the defensive SR, because a smaller SR implies that the expected points per unit of risk is lower for the team playing against the defense. Finally from the efficient mixed strategy a shot type pricing model is derived for both offense and defense. This provides measures of the risk adjusted price of each shot type by team. An immediate advantage of applying this theory to basketball is that these results are scalable to any number of shot types. A team could analyze different shot types such as corner 3-pointers as compared to other 3-point locations as well as the relative return on midrange jump shots (from 15 feet where they are possibly riskier while only yielding 2 points as a return). 

In summary, adopting the above economic analysis of basketball results in the following parameters: 

- (i) At an aggregate level the NBA’s efficient allocation of aggregate 2- and 3-point shots is estimated from 1979 to 2014. 

- (ii) At an individual team level an offensive 4- tuple: (Sharpe Ratio, 2-point beta, 3-point beta, and slope of Shot Market Line) for each team. 

- (iii) At an individual team level the defensive 4- tuple: (Sharpe Ratio, 2-point beta, 3-point beta, and slope of Shot Market Line) for each team. 

From (i) above, the unique mixed strategy is compared to the NBA actual aggregate statistics for 2- and 3-point shots. For (ii) and (iii) the 4-tuples are estimated using within season data and then applied to predict post season performance. Finally, to better understand our measures and their relation to basketball performance, we correlate our parameters to the factors identified by Oliver (2004) as capturing offensive and defensive performance. This will identify the empirical relationships between these theoretical parameters with modern basketball performance measures. 

We first consider some simple statistics that describe the phenomena being analyzed. 

- _2.2. Offensive investments: Allocation of shot attempts to 2 and 3-pointers_ 

Expected points is points per shot times the probabilityofsuccessfulshotattemptsforeachshottype.In Fig. 1 this is plotted over time for 2- and 3-point offensive shots. If coaches employ a risk neutral strategy, this would imply that only 2-point or 3-point shots are taken. The graph in Fig. 1 suggests that, for risk neutral teams, only 2-pointers would be used up to 1987 (expected points are higher from 2-point shots up to 1987), followed by only shooting 3-pointers from1988on.ActualNBAshotdatadonotreflectthis extreme risk neutral prediction with all 2-point shots crossing over to all 3-point shots. Figure 2 depicts the interesting behavior for the variance of successful 2- and 3-point shots each year. This reveals that 2-point shot variance has been relatively stable over time until recently whereas 3-point shot variance has been declining. If risk is important and we equate variance to risk, as the riskiness of a 3-point shot declines the 3-point shot should be taken more frequently. In fact, this has happened. This is further 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

111 

reinforced from the observation that both the mean and variance of points are also responsive to the rule adjustments made during the 1994–95, 1995–96 and 1996–97seasons.Asnotedabove,theNBAshortened the distance of the line from 23 feet 9 inches and 22 feet at corners to a uniform 22 feet from the basket. In 1997–98, the NBA then reverted back to the original distance of 23 feet 9 inches and 22 feet at the corners. Figures 1 and 2 indicate that both the mean and the variance are sensitive to these rule changes between 1994 and 1997. 

One advantage of invoking the predictions from the optimal mixed strategy is that the NBA can predict the impact from changing rules upon shot taking behavior, which is especially important if maintaining a particular 2- and 3-point shot ratio for fans is an important objective. However, before being able to make such predictions there is a third input that influences predictions from the optimal mixed strategy. This is the covariance (or correlation) between 2- and 3-point offensive shot investments. By using each team as an observation within each year the 2- and 3-point shot expected points correlations can also be computed each year. Figure 3 plots the results from this analysis of the 2- and 3-point data across teams, computing a Pearson product-moment corre- 

Combined, Figs. 1, 2 and 3 provide the basic building blocks for identifying the efficient mixed strategy for basketball as formally described next. 

### _2.3. Identifying the Efficient Mixed Strategy_ 

The set of efficient 2- and 3-point shot strategies is identified by maximizing the Sharpe Ratio, where _j_ = 1 (2-point shots) and 2 (3-point shots) and the maximization problem is defined as follows: 



Subject to: 



### Where 

_ω_ = a vector of shot type weights ( _α_ 2 _, α_ 3) the proportion of 2- and 3-point shots in the mixed strategy and _s_<sup>_T_</sup> the shot type points. Expected points from the mixed strategy is defined as: _μ_ = _s_<sup>_T_</sup> _ω_<sup>_T_</sup> _p_ ¯ . This expands as _μ_ = 2 ∗ _α_ 2 ∗ _p_ 2 + 3 ∗ _α_ 3 ∗ 

_p_ 3 where _p_ 2 _, p_ 3 are the probability of 2 and 3-point successful shots. 

_σ_ = � _ω_<sup>_T_</sup><sup>~~�~~</sup> _ω_ ,<sup>�</sup> =variance covariance matrix of shot type points 

For 2- and 3-point shots, the portfolio volatility (i.e., standard deviation) is: _σ_ = �4 _α_<sup>2</sup> 2<sup>_σ_</sup> 2<sup>2</sup> 0 _._ 5 +9 _α_<sup>2</sup> 3<sup>_σ_</sup> 3<sup>2+ 12</sup><sup>_α_2</sup><sup>_α_3</sup><sup>_rσ_2</sup><sup>_σ_3</sup> � where 4 equals 2 points squared, 9 equals 3-points squared and 12 is 2*2*3 to cover the off diagonal terms. 

For the problem defined above in equation (1), _p_ , the probability of a successful shot computed from _n_ shots is a random variable estimated from the data (dropping shot type subscript for expositional ease). The distribution for _p_ is estimated by applying the central limit theorem to the large number of both 2 and 3-points shots each season, and the variance of _p_ is normally distributed and equal to _p*(1-p)/n_ . As a technical aside, we do not define variance in terms of being a random variable from the Bernoulli distribution, which assumes it is the outcome from a sequence of shot realizations generated from the Binomial ( _n, p_ ) distribution. This is because invoking the Bernoulli distribution assumes that _p_ is a parameter, i.e., a fixed real number, as opposed to being itself a random variable which must be estimated from the data. Finally, we compute the Pearson correlation coefficient, _r_ , between 2- and 3-point shots from each team’s total shot statistics per regular season year. By assuming each team makes a tradeoff between using 2 and 3- point shots in their offensive strategy, we calculate the Pearson correlation coefficient using each team as an observation. The number of teams used to estimate _r_ , range from 22 NBA teams in 1979 to 30 NBA teams currently, and finally covariance is then defined as _rσ_ 2 _σ_ 3. 

The solution to the above maximization problem, when applied to NBA aggregate data, identifies the efficient mixed strategy of 2- and 3-point shots for the NBAasawhole.Herewedefineefficiencyforoffense as the mixed strategy that maximizes expected points per unit of risk. For the NBA as a whole this is also equivalent to finding the minimum expected points given up per unit of risk. That is, the offensive and defensive problems are symmetrical. However, this symmetry does not extend to individual teams and both offensive and defensive performances are measured and analyzed separately for individual teams as discussed next. 

### _1. Individual Team Level of Analysis_ 

The game of basketball consists of both offense and defense and therefore to analyze basketball at 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

112 

the individual team level we first apply equation (1) to identify the two efficient mixed strategies, offensive and defensive for each team. In this paper, we solve for the mixed strategy that maximizes the Sharpe ratio (e.g., Elton and Gruber (1995)), and refer to this strategy as the “Efficient Mixed Strategy” (EMS). Central to this theory of investment returns is the idea that higher risk is associated with higher expected returnsinaworldwhereriskaversionisimportant.By applying investment theory to basketball, we relate the expected points from the 2- and 3-point shot types to the risk associated with each shot type for each team. The steepness of this relationship provides insight into the cost associated with a team’s tradeoff between risk and expected points. Formally the CAPM theory predicts the following general form for this relationship, referred to as the Security Market Line (SML) which is positively sloped and defined as follows (e.g., Bodie, Kane and Marcus (2013)): 



where E ( _ρ_ j) is the expected points from shot type j, �j is shot type j’s beta, and E ( _ρ_ M) is the expected points from the optimal mixed strategy M. This is analogous to the Security Market Line (SML) in investment theory, and in this paper we refer to this as the “Shot Market Line” (SML). The SML describes the tradeoff between risk and expected points for each type of shot. 

Shot type betas are estimated in two equivalent ways, relative to each team’s efficient mixed strategy. First, beta is defined as the covariance between the average shot type payoff and the optimal mixed strategy payoff, scaled by the variance of the optimal mixed strategy payoff. The efficient mixed strategy is computed from the variance/covariance matrix, where covariance is estimated by computing the correlation between shot types estimated from the 30 teams, multiplied by the product of the shot type standard deviations. Equivalently, and simpler, shot type betas can be computed directly from the ratio of the averagepayoffsrelativetotheefficientmixedstrategy as described by Equation (2). 

To make the above theoretical concepts concrete it is instructive to first illustrate some of the important statistics that this analysis produces by applying it to the first and last place teams in the regular 2013 season.Thiswillhelptofocusonsomeoftheintuition behind the empirical results that follow. 

### _2.4. Example: Miami compared to Orlando 2013_ 

During the regular 2013 season Miami attained the highest win percentage of 80.48 percent and Orlando the lowest, 24.39 percent. Based upon regular season team results, the SR, shot type betas and SML slope, for Miami and Orlando is as follows: 

### **Miami 2013 Regular Season Offensive Performance** 

Sharpe Ratio = 16.33 Beta (2-point) = 0.96 Beta (3-point) = 1.15 Slope of the Shot Market Line (SML)=1.03 

### **Miami 2013 Regular Season Defensive Performance** 

Sharpe Ratio = 13.79 Beta (2-point) = 0.96 Beta (3-point) = 1.14 Slope of the Shot Market Line (SML) = 0.91 

### **Orlando 2013 Regular Season Offensive Performance** 

Sharpe Ratio = 13.34 Beta (2-point) = 0.98 Beta (3-point) = 1.08 Slope of the Shot Market Line (SML) = 0.91 

### **Orlando 2013 Regular Season Defensive Performance** 

Sharpe Ratio = 13.54 Beta (2-point) = 0.97 Beta (3-point) = 1.12 Slope of the Shot Market Line (SML) = 0.96 

Major differences immediately appear between these two teams both offensively and defensively which can be interpreted as follows. 

Consider first the Sharpe Ratio (SR) which imposes a price of risk constraint upon the efficient mixed strategy. A high offensive (low defensive) SR is preferred to a low offensive (high defensive) SR because the offensive SR measures the expected points per unit of risk and the defensive SR measures the expected points given up per unit of risk. For the case of Miami versus Orlando, Miami has a higher price of risk for its offensive mixed strategies. As a result, Miami will have a higher expected points per unit of risk than Orlando in its efficient mixed strategy. 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

113 

Additional insight into the drivers of the above differences is provided by considering both the offensive and defensive SML’s. The analogy to the Security Market Line for basketball can be interpreted as follows. In regular CAPM all risky assets are predicted to lie on the Security Market Line in equilibrium. For basketball each risky shot type is predicted to lie on the Shot Market Line (SML). In the above example the slope of the SML is constructed for both offense and defense. For the case of offense a steeper SML implies that the expected points per unit of risk is higher for the 3-point shot compared to the 2-point shot. In addition, the steeper the SML the stronger the offense. Recall from Fig. 2 that the variance of 2-point shots has remained relatively stable for about three decades whereas the variance of the 3-point shot has been declining. The CAPM theory predicts the shot type beta is a function of shot type volatility (e.g., Bodie, Kane and Marcus (2013)) and as a result, the steeper the SML the better is the offensive 3-point shooting from an expected points perspective relative to the 2-point shot type. This difference between CAPM applied to financial securities as opposed to shot types, is that for financial securities the expected return pricing model includes a risk free rate, typically non-zero, whereas for the basketball shot types, the offensive shot pricing model originates at the origin(i.e.,riskfreerateequalszero).Inbothcases,however, steeper rays dominate flatter rays. The opposite applies to the defensive SML as it is defined in terms of points given up. In the above example, Miami compared to Orlando reinforces these insights. 

### **3. Data** 

Data for team level analyses for the years 1979–2014 was extracted from data provided by databasebasketball.com<sup>3</sup> . In particular, we used the file team ~~s~~ eason.csv which provides data on shots taken, shots made, and winning percentage at the team season level. For analyzing individual team performance and performance in the playoffs, we used game level data provided by nbastuffer.com for 2007–2014. We analyze team level NBA data starting in 1979. That is the year the NBA introduced the 3-point shot. The line is 23<sup>′</sup> 9<sup>′′</sup> away from the basket excepting in the corners of the basketball court, where the distance is shorter (22 feet), again, excepting the 1994-95, 1995–96 and 1996–97 seasons, as discussed above. 

> 3 http://www.databasebasketball.com/index.htm. 

### **4. Application of the efficient mixed strategy theory to NBA basketball** 

The first problem we address at the aggregate level is to provide a theoretical explanation of the observed trends in the percentage of 3-point shot taking from 1979 to 2014 in terms of mean/variance efficient mixed 2- and 3-point strategies. This theoretical explanation provides a prediction for the NBA regarding what the future trend for percentage of 3-point shots is likely to be given current skill levels. 

### _4.1. Results for NBA as a whole_ 

In this section we present the results from solving each year for the aggregate offensive efficient mixed strategy for the NBA as a whole. The analysis proceeds by constructing the distribution of points from each shot type for the NBA as a whole by year. Figures 1–3 above depict the evolution of the 3-point shot and its use in the mixed strategy, over time. The negative correlation between 2- and 3-point shot successes is pronounced and reinforces this evolving use of the 3-point shot in NBA strategies. For example, as noted by players such as power forward David Lee of the Golden State Warriors: “The game is changing,” Lee said, “and I think one of the things is not telling ‘4s’ (power forwards) they’re going to be in the post all the time. Instead, teams are giving them the option to shoot mid-range shots and threes. Then the defense has to make the adjustment.”<sup>4</sup> 

As a result, as the mixed 2- and 3-point strategy becomes more prevalent, the negative correlation in Fig. 3 is becoming more pronounced. The efficient mixed 2- and 3-point strategies allow for a consistency relationship to be tested between the predicted efficient strategies each year and the actual observed outcomes. These results are depicted graphically in Fig. 4. 

Figure 4 reveals that, in the aggregate, NBA coaches have exhibited highly efficient 2- and 3- point shot selection strategies. That is, there is a high level of consistency between aggregate mixed strategy behavior and player abilities when reduced to means, variances and covariances. It can also be observed that both actual and predicted behavior is sensitive to the rule changes that took place over the 

> 4Source: http://www.sfgate.com/sports/kroichick/article/Stret ch-4s-changing-NBA-dynamic-5011347.php Monday, November 25, 2013 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

114 



<!-- Start of picture text -->
Actual versus optimal 3-point proportions<br>0.3<br>0.25<br>0.2<br>0.15<br>0.1<br>0.05<br>0<br>1979 1984 1989 1994 1999 2004 2009 2014<br>% 3-Pointers  3-Ptr Optimal<br><!-- End of picture text -->

Fig. 4. Actual versus Optimal 3-Pointers (Actual Correlations). 

1990’s. As a result, analytical modeling combined with empirical analysis of basketball can provide predictions for likely outcomes of future potential rule changes. 

Theaboveanalysisalsoprovidesinsightintowhere the NBA is headed in terms of predicted proportions of 3-point shots. Clearly, from a fan perspective, the NBAprobablywantstomaintainanattractivebalance between the proportions of 2-point and 3-point shots in the game. In investment theory the variance and covariance of shot types are the major drivers of the predicted proportion of shots for a risk averse world. Although Fig. 2 reveals that the NBA has gone down a steep learning curve associated with the _accuracy_ of the 3-point shot from 1979 to 1995, this learning curve settles down post 1995. Between 1995 and 1997 rule changes largely accounted for observed changes in 3-point accuracy and post 1997 the evidence suggests that team strategy became a major driver of this behavior. This is implied from the observation that the correlation between top shooters (in terms of accuracy) and top 3-point shooters (in terms of attempts) in 2014–2015 is substantially higher ( _r_ = 0.417) than it was in 1998–1999 ( _r_ = 0.329). One of the leading 3-point shooters today is Stephen Curry (accuracy = 0.443, third in the NBA in 2014–15). Coincidently,hisfatherDellCurrywasthemostaccurate 3-point shooter in 1998-1999 (accuracy = 0.476). While Stephen Curry led the NBA in 3-point shot attempts, Dell Curry was not even among the top 20 players in 3-point attempts. Although overall league shooting accuracy has not changed very much, the significant overlap between high frequency 3-point shooters and the most successful 3-point shooters today implies that mixed strategies have taken time to evolve differently from just accuracy alone. This is also reflected in the greater stability of correlation trends between 2-point and 3-point shots over time. In order to tease out the relative impact of each of these two important inputs we can systematically intro- 



<!-- Start of picture text -->
Actual versus optimal 3-point proportions<br>(independence condition)<br>0.3<br>0.25<br>0.2<br>0.15<br>0.1<br>0.05<br>0<br>1979 1984 1989 1994 1999 2004 2009 2014<br>% 3-Pointers  3-Ptr Optimal<br><!-- End of picture text -->

Fig. 5. Optimal Number of 3-point shots versus actual under independence condition. 

duce the correlation results into the analysis. In the next section we compare the actual versus predicted behavior in Fig. 4 when using estimated correlations versus a baseline case of zero correlation (i.e., independence). 

First we consider the baseline case under the assumption of zero correlation between shot types. For this analysis we estimate the optimal mixed strategies under the imposed condition that the two shot type distributions are independent. This will allow the effects of shot accuracy (shot expected points variance) versus mixed strategy (shot expected points correlations) to be teased out by comparing Figures 4 and 5. 

The results from Fig. 5 reveal that in aggregate for the NBA trends in the predicted efficient strategies are consistent with trends in Fig. 4 but the gap between actual and predicted is widening which demonstrates the increasing importance of mixed strategies in the game. The increasing widening of the two series is likely to be a result of the strategy learning curve that coaches and players in the NBA have been ‘going down’ over time that was alluded to by David Lee’s comments above. Figures 2 and 3 reveal that both variance and correlations have substantially stabilized in the last few years. This implies that it is unlikely that the proportion of 3-point shooting is about to dominate the proportion of 2-point shots as some have speculated will happen<sup>5</sup> . 

Next, we extend the aggregate analysis of the NBA to the analysis of individual team performances during the regular season. The objective of this section is to provide a _descriptive_ analysis of the basketball performance in terms of the team level performance measures identified from the theory. We analyze the dependent variable, win percentage, as a fractional response variable. For this fractional response, the 

5Source: http://grantland.com/features/the-reliance-3-pointerwhether-not-hurting-nba/, Sunday, July 19, 2015 

115 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

Table 1 

|Frac|tional regres|sion models p|redicting re|gular season|winning perc|entage using|CAPM mea|sures||
|---|---|---|---|---|---|---|---|---|---|
||2007|2008|2009|2010|2011|2012|2013|2014|2007–2014|
|Constant|29.724|18.495|29.887|66.69<sup>∗∗∗</sup>|–54.419|25.147|11.761|2.609|22.364<sup>∗∗</sup>|
||(18.986)|(22.549)|(19.990)|(20.275)|(30.201)|(22.493)|(16.497)|(8.427)|(9.419)|
|Offense||||||||||
|SML|6.307<sup>∗∗</sup>|8.849<sup>∗∗∗</sup>|8.54<sup>∗∗∗</sup>|8.03<sup>∗∗∗</sup>|10.36<sup>∗∗∗</sup>|10.8<sup>∗∗∗</sup>|10.06<sup>∗∗∗</sup>|9.769<sup>∗∗∗</sup>|9.81<sup>∗∗∗</sup>|
||(2.238)|(1.718)|(2.311)|(1.296)|(1.799)|(2.621)|(1.659)|(1.117)|(0.792)|
|Sharpe Ratio|0.045|0.056|0.091<sup>∗∗</sup>|0.015|0.139<sup>∗∗∗</sup>|–0.007|0.072|0.024|.048<sup>∗∗</sup>|
||(0.048)|(0.067)|(0.037)|(0.059)|(0.038)|(0.064)|(0.050)|(0.035)|(0.019)|
|�2|–18.36 <sup>∗</sup>|8.985|–10.972|–24.689|3.384|–5.303|4.378|6.041|–9.359 <sup>∗</sup>|
||(9.003)|(10.583)|(5.856)|(13.095)|(9.790)|(10.145)|(7.688)|(3.983)|(4.198)|
|�3|–5.494<sup>∗</sup>|–0.195|–6.77 <sup>∗∗∗</sup>|–7.592|–0.098|–2.090|omitted|omitted|–4.16 <sup>∗∗∗</sup>|
||(2.428)|(2.689)|(1.812)|(4.295)|(3.710)|(4.276)|omitted|omitted|(1.239)|
|Defense||||||||||
|SML|–13.98<sup>∗∗∗</sup>|–19.66 <sup>∗∗∗</sup>|–18.440|–16.13 <sup>∗∗∗</sup>|–9.26 <sup>∗∗∗</sup>|–10.33 <sup>∗∗∗</sup>|–9.94 <sup>∗∗∗</sup>|–16.84 <sup>∗∗∗</sup>|–14.27 <sup>∗∗∗</sup>|
||(2.015)|(3.114)|(1.935)|(1.968)|(2.746)|(3.027)|(2.195)|(1.874)|(1.239)|
|Sharpe Ratio|0.075|0.0989|–0.035|0.090|–0.098|0.084|–0.058|0.078|0.020|
||(0.073)|(0.069)|(0.053)|(0.069)|(0.087)|(0.092)|(0.068)|(0.051)|(0.025)|
|�2|0.771|–17.606|–3.868|–18.687|36.950|–19.72 <sup>∗∗</sup>|–14.272|–3.280|–5.931|
||(10.575)|(13.978)|(11.957)|(10.390)|(19.089)|(8.389)|(11.398)|(7.089)|(5.330)|
|�3|–0.726|–1.512|0.720|–8.756 <sup>∗∗∗</sup>|12.301<sup>∗</sup>|omitted|–2.211|omitted|0.324|
||(2.691)|(3.663)|(2.378)|(3.018)|(5.720)|omitted|(3.039)|omitted|(1.338)|
|N|30|30|30|30|30|30|30|30|240|
|Fixed effects Year|No|No|No|No|No|No|No|No|Yes|
|Fixed effects Team|No|No|No|No|No|No|No|No|Yes|
|Log pseudo likelihood|–13.223|–12.936|–12.726|–12.944|–12.972|–13.0113|–13.137|–12.961|–103.852|
|<br>AIC|1.482|1.462|1.448|1.463|1.464|1.408|1.409|1.331|1.24|
|Pseudo-R<sup>2</sup>|0.777|0.821|0.913|0.837|0.834|0.745|0.741|0.856|0.833|



> ∗ _p_ < 0.05, ∗∗ _p_ < 0.01, ∗∗∗ _p_ < 0.001. The regressions are all predicting team winning percentage using the fractional regression method discussed in the text. 

values lie in the closed unit interval [0,1]. The linear probability model applied to such a dependent variable cannot guarantee predicted values will not fall outside the unit interval (Wooldridge, 2002). For this reason, other methods such as a log-odds transformation of the dependent variable and NLS estimation are often proposed. It has been shown that such estimators, while estimable with OLS, are problematic. In particular, they do not deal with values at the boundary, 0 and 1, and the regression estimators � are not easily interpreted (Wooldridge, 2002). Papke and Wooldridge (1996) propose a method to address this problem. They show that using a generalized linear model with a Bernoulli log-likelihood function and robust estimates of the standard errors provides estimates that are efficient, allow for values at the unit interval boundaries of 0 and 1, and are directly interpretable. For these reasons, we apply the method proposed by Papke and Wooldridge (1996). In our estimates, we use the logit cumulative density function. 

The results from Table 1 reveal that each year’s descriptive model fits the data well. Furthermore, from inspection of the individual coefficients the pair 

of offensive and defensive SML slopes each had significant _t_ statistics at or around the 0.001 level with signs in the predicted directions. When we aggregate the data from 2007–2014, and estimate the model with fixed effects for year and team, we find all 4 offensive measures are likely to have an effect, while only the defensive SML has an effect over the 8 seasons, comprising 240 team seasons. In all these cases the models fit the data reasonably well, but the models are only descriptive, given they are estimated on the same within season data used to estimate the predictors themselves. Later even more insight is provided when we relate the set of economic variables identified by the theory to traditional basketball factors. 

- _4.2. Out of Sample Analysis using the Post Season Championships_ 

For the out of sample tests, the post season results from 2007 to 2014 were pooled to increase the sample sizeattheteamlevel.Ineachyear,theNBAchampion is determined by a 16-team single-elimination tournament. The winner in each round in the tournament 

116 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

is the winner of a best-of-seven series. The tournament starts a few days after the end of the regular season. No adjustments to personnel occur between the regular season and post season. The loser of each best of 7 series exits the tournament. Given 16 teams, there are 15 series per year in each of the 7 years. The average series length is 5.6 games. The average annual tournament, composed of 15 series, has 83.8 games. Our analysis is at the game level. We use two dependent variables, (1) whether the home team won and (2) the point difference between the home team and road team. The predictor variables are offensive and defensive SML slopes, 2 and 3-point betas, and Sharpe ratios for the home team and the road team. In addition, year of the playoff and series (since games are nested under each 7 game series) are treated as random effects. We choose to use random effects for several reasons. We do not expect year to year variation to be systematically correlated with the effects of the predictors, so year to year variation is treated as random. Each series involves a set of games between the same teams. The observations within a series may be correlated. For this reason, observations within a series are modeled as random effects (Wooldridge, 2002; Angrist & Pischke, 2009). 

These prediction models are multilevel models because you have games nested in series and series nested in year. We used the Stata command ME (multilevel <u>estimation)</u> to estimate the models. The first model, predicting the winner of a game in a series was estimated as a logit model using maximum likelihood. The logistic regression results for home game won are presented in Table 2. The fit is significant (Wald _χ_ 2 = 50.35, _p_ < 0.001). The results again reinforce the descriptive within season analysis, and it is the offensive and defensive SML slopes that drive the results. 

Next a more sensitive dependent variable, point differential, was analyzed to take into account the closenessofthegameresult.Thepredictionmodelfor point differential is a multilevel mixed (having some fixed and some random effects) linear regression model that requires restricted maximum likelihood estimation. Restricted maximum likelihood first estimates the fixed effects and then estimates the random effects. The random effects are estimated with maximum likelihood without the fixed effects (Harville, 1977). The results are provided in Table 2. The linear regressionofthepointdifferentialissignificant(Wald _χ_ 2 = 77.92, _p_ < 0.001). Again this analysis reinforced the same SML slope results where the four SML slope coefficients (offensive, defensive, home and away) 

areallhighlysignificant( _p_ < 0.01).Themajorconclusion from the individual team performance analysis is that SML slopes (offensive and defensive) are useful predictors of performance. 

- _4.3. Linking the Economic Variables to Basketball_ 

In a popular and influential book, Oliver (2004) identifies four factors that determine success in the NBA. These are ranked as follows in terms of assessed order of importance for winning a game. The ranking is, Shooting, Turnovers, Rebounding and Free Throws per shot. In addition, the factors can be applied to both offense and defense. The variables for both offense and defense are: 

- EFG% – Effective Field Goal Percentage which is adjusted for the fact that a 3-point field goal is worth one more point than a 2-point field goal. 

- TOV% – Turnover Percentage which is an estimate of turnovers committed per one hundred plays. 

- ORB% – Offensive Rebound Percentage which is an estimate of the percentage of available offensive rebounds a player or team grabbed. 

- FT/FGA – Free Throws Per Field Goal Attempt. 

It is useful to know how these four factors relate to the 4-tuple of economic variables identified in section 2 and we explore these relationships in a correlational analysis. It is noted however, that the four variables identified in our current paper’s economic analysis are derived from a coarse data set containing only 2- and 3-point shot distributions for both offensive and defensive performance. Refining the set of shot types as improved datasets become available in the future is likely to improve this type of analysis. 

The results are provided in Table 3 and three estimates immediately draw our attention. First, offensive SML slope is extremely highly correlated (0.891) with the EFG% which is considered to be the major driver of success. However, recall from our analysis it was both offensive and defensive SML slopes that are the critical success drivers. As a result it is interesting to observe the defensive correlations. The EFG% of the opponent team is highly correlated (0.817) with the defensive SML slope. This is consistent with the fact that the higher the defensive SML slope the higher the expected points from the opposing team playing against the defense. Similarly, the EFG% correlation with the defensive SR is 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

117 

Table 2 

Playoff performance predicted by CAPM measures 

||Home Team winning|Home Teampoint differential|
|---|---|---|
|Constant|36.379|–82.623|
||(55.969)|(312.067)|
|Road Team offense|||
|Sharpe ratio|0.044<br>|0.075<br>|
||(0.088)|(0.489)|
|SML|–7.972<sup>∗∗</sup><br>|–68.998<sup>∗∗∗</sup><br>|
||(3.147)|(17.6)|
|�2|–14.628|57.49|
||(17.649)|(126.182)|
|�3|–4.16|–19.989|
||(4.968)|(27.711)|
|Road Team defense|||
|Sharpe ratio|–0.256<sup>∗∗</sup>|–1.58<sup>∗∗</sup>|
||(0.1)|(0.56)|
|SML|14.616<sup>∗∗∗</sup>|95.61<sup>∗∗∗</sup>|
||(4.343)|(23.99)|
|�2|–24.433|57.49|
||(22.754)|(126.182)|
|�3|–4.435|22.513|
||(6.175)|(33.939)|
|Home Team offense|||
|Sharpe ratio|0.005|–0.119|
||(0.087)|(0.49)|
|SML|11.268<sup>∗∗∗</sup>|70.816<sup>∗∗∗</sup>|
||(3.147)|(17.485)|
|�2|–8.168|–55.964|
||(18.141)|(100.385)|
|�3|–2.954|–15.49|
||(5.109)|(28.285)|
|Home Team defense|||
|Sharpe ratio|–0.065|–0.389|
||(0.1)|(0.559)|
|SML|–11.167<sup>∗∗</sup>|–60.347<sup>∗∗</sup>|
||(4.365)|(23.964)|
|�2|19.804|123.33|
||(22.116)|(124.803)|
|�3|0.995|39.261|
||(5.92)|(34.072)|
|Year of Playoff Game (_df_=_8)_|–17.76|7.38E-08|
||(5.88E05)|(7.46E-07)|
|Series (_df_=_120_)|–19.47|2.16E-08|
||(4.55E07)|(4.83E-09)|
|_N_|670|670|
|Log Likelihood|–400.338|–346.895|
|Wald _χ_2|50.35<sup>∗∗∗</sup>|77.92<sup>∗∗∗</sup>|



> ∗ _p_ < 0.05, ∗∗ _p_ < 0.01, ∗∗∗ _p_ < 0.001. For the point differential estimates, we estimate a restricted maximum likelihood. 

0.374.HigherdefensiveSRisconsistentwithahigher expected proportion of 2-point shots being played against the defense. The other pair of interesting correlations are in relation to defensive team’s offensive rebound percentages. The correlation between defensive rebound percentages and the defensive SR is –0.25 and the defensive SML slope is –0.404. Again from a strategic defensive perspective this is reinforcing the fact that the opposing team is taking a higher proportion of 2-point shots against weaker defenses 

that in particular are weaker at defending against the opposing team’s rebounding successes. The above analysis also illustrates the advantage of the economic analysis that is decomposing expectations into both strategic and expected points components. For example, if a team tightens up its defensive rebounding this is likely to have _both_ strategic and expected points implications. Strategic in the sense that the opposing offenses are likely to reduce the proportion of 2-point shots played against the defense 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

118 

|rom 2006–2007 to 2013–2014<br>D-SML<br>D-beta2 D-beta3 Win %|1.000<br>–0.124<br>1.000<br>0.060<br>–0.867<br>1.000<br>–0.637<br>–0.025<br>0.065<br>1.000<br>ive Rebound %(ORB%) and 4 = Free<br>SML is the offensive SML slope and<br>n the text. Ordinary signifcance tests<br>s and our statistics) are in bold.|
|---|---|
|8 seasons f<br>D-S|1.000<br>0.342<br>–0.056<br>0.124<br>–0.134<br>3 = Offens<br>T/FGA. O-<br>discussed i<br>actor score|
|os for the<br> O-beta3|1.000<br>–0.011<br>–0.080<br>–0.085<br>0.110<br>0.105<br>(TOV%),<br>and 4 = F<br>ented and<br>Oliver 4 f|
|sharpe rati<br>O-beta2|1.000<br>–0.903<br>0.029<br>0.104<br>0.110<br>–0.150<br>–0.182<br>urn Over%<br>= ORB%<br>es are pres<br>ons of the|
|lues and<br>O-SML|1.000<br>–0.276<br>0.204<br>0.082<br>–0.266<br>–0.079<br>0.080<br>0.670<br>%), 2 = T<br>TOV%, 3<br>se variabl<br>(correlati|
|, alpha va<br>O-S|1.000<br>0.393<br>–0.155<br>0.164<br>0.171<br>–0.080<br>–0.024<br>0.039<br>0.287<br>l % (EFG<br>FG%, 2 =<br>o. All the<br>of interest|
|nsive SML<br>D4|1.000<br>–0.085<br>–0.001<br>0.052<br>–0.023<br>–**0.025**<br>**0.172**<br>–**0.026**<br>**0.076**<br>–**0.210**<br>Field Goa<br>with 1 = E<br>harpe rati<br>rrelations|
|and defe<br>D3|1.000<br>–0.216<br>0.049<br>0.120<br>–0.139<br>0.142<br>–**0.250**<br>–**0.404**<br>–**0.048**<br>**0.056**<br>**0.374**<br>Effective<br>e factors<br>efensive S<br>s. The co|
|nd offensive<br>D2|1.000<br>–0.301<br>0.300<br>–0.098<br>–0.014<br>0.172<br>–0.145<br>–**0.021**<br>–**0.071**<br>**0.033**<br>–**0.002**<br>**0.073**<br>ors with 1 =<br>ur defensiv<br>D-S is the d<br>over 8 year|
|r scores a<br>D1|1.000<br>0.006<br>–0.452<br>0.161<br>–0.050<br>–0.260<br>0.184<br>–0.152<br>**0.374**<br>**0.817**<br>–**0.034**<br>–**0.029**<br>–**0.673**<br>nsive fact<br>(2004) fo<br>lope and<br>30 teams|
|four facto<br>O4|1.000<br>–0.010<br>0.045<br>–0.112<br>0.359<br>–**0.048**<br>**0.233**<br>**0.155**<br>–**0.195**<br>0.041<br>–0.010<br>–0.088<br>0.100<br>0.196<br>four offe<br>the Oliver<br>ive SML s<br>the same|
|defensive<br>O3|1.000<br>0.176<br>0.043<br>0.084<br>–0.111<br>0.153<br>–**0.125**<br>–**0.261**<br>**0.279**<br>–**0.230**<br>–0.034<br>0.045<br>0.009<br>–0.001<br>0.008<br>ver (2004)<br>1-D4 are<br>the defens<br>data from|
|nsive and<br>O2|1.000<br>0.111<br>0.263<br>0.015<br>0.188<br>–0.140<br>0.172<br>–**0.191**<br>–**0.102**<br>**0.202**<br>–**0.186**<br>–0.056<br>0.039<br>–0.062<br>0.067<br>–0.296<br>re the Oli<br>/FGA). D<br>-SML is<br>re pooling|
|ns of offe<br>O1|1.000<br> –0.010<br> –0.295<br>0.187<br> –0.263<br> –0.021<br>0.130<br> –0.110<br>**0.439**<br>**0.891**<br> –**0.249**<br>**0.150**<br>0.116<br> –0.268<br> –0.098<br>0.096<br>0.638<br>O1-O4 a<br>mpted(FT<br>pe ratio. D<br>ince we a|
|rrelatio<br>SD|0.019<br> 0.954 <br> 2.452 <br>0.028<br>0.016 <br> 1.021 <br> 1.817<br>0.027 <br> 1.140<br>0.033<br>0.012 <br>0.041<br> 1.003<br>0.030 <br>0.008 <br>0.031<br>0.156<br>ariables<br>als Atte<br>ve Shar<br>e here s|
|co<br>n|7<br>8 <br>6 <br>4<br>6<br>7 <br>8 <br>4<br>0 <br>4<br>7<br>4<br>4 <br>4<br>6<br>8<br>0<br>V<br>o<br>si<br>iat|
|earson<br>Mea|0.49<br>13.52<br>26.45<br>0.22<br>0.49<br>13.52<br>73.52<br>0.22<br>13.41<br><br>0.94<br><br>0.96<br><br>1.13<br>13.31<br><br>0.94<br><br>0.96<br><br>1.13<br>0.50<br>_N_= 240.<br>/Field G<br>he offen<br>appropr|
|P|1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>-S<br>-SML<br>-beta2<br>-beta3<br>-S<br>-SML<br>-beta2<br>-beta3<br>in %<br>otes: <br>hrows<br>-S is t<br>e not|
||O<br>O<br>O<br>O<br>D<br>D<br>D<br>D<br>O<br>O<br>O<br>O<br>D<br>D<br>D<br>D<br>W<br>N<br>T<br>O<br>ar|



_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

119 

and goals made against the defense are expected to decline. 

The remaining two factors, TOV% and FT/FGA are not really captured (and probably should not be captured) in the data set analyzed in this paper. 

### **5. Discussion and conclusions** 

In this paper we provide an economic analysis of the game of basketball. In particular we focused on how professional basketball in the United States (the NBA) adapted to the addition of the 3-point shot in 1979. The 3-point shot presented coaches and players with a higher risk, potentially higher return alternative to the 2-point shot. We treated the problem as an investment problem where the team takes a limited resource, shots to be attempted, and allocates them to one of the investment alternatives, the less risky 2- point shot or the more risky 3-point shot. We identify the efficient mixed 2- and 3-point shot type strategy by adopting a modern portfolio theory approach and maximizing the Sharpe Ratio (SR). We further extend this analysis to identifying pricing models for both offense and defense referred to as the Shot Market Line (SML). This results in estimating the SR, SML slope and betas for each shot type. We find that the NBA as a league of 30 teams exhibits near optimal risk allocation from 1979 to 2013. In particular, as the variability in 3-point shooting performance has declined, the proportion of 3-point shots taken has increased, closely tracking 3-point shooting performance variability. We then estimated team level parameters for each season of competition, and found that offensive and defensive SML slopes account for much of the variation in winning percentage. To test if these parameters are robust, we then used them to predict out of sample team performance in the post season championship tournament. We find that the offensive and defensive SML slopes account for variation in post season tournament likelihood of winning and point differential (how many more points the winner scores in a game). Sharpe ratios generally do not predict winning or point differential, suggesting most teams are managing risk efficiently using a mixed strategy, but it is individual team differences in the implied shot market lines from these mixed strategiesthatdeterminesoutcomes.Whenwecompareour theoretical variables to basketball ‘accounting’ measures such as offensive efficiency, turnover ratios and so on, we find that the SML slope measures are very strong correlates of measures of offensive efficiency. 

There are several interesting implications suggested by these results. First, financial modeling of risk estimation and management can be applied in a sports setting. In sports, management has to make a set of decisions that impact the risk and return properties of a team. For example, a simultaneity problem can exist among the acquisition of players with different abilities, the hiring of coaches and the design of play systems. Each of these factors has a direct impact upon a team’s risk and return tradeoffs. In this context the decomposition of basketball into ‘strategic’ and ‘expected points related’ economic variables can provide interesting insights into predicted outcomes and thus can support rational decision making. Analogous problems exist in other sports. For example, in American football, coaches are frequently encountering alternatives with different levels of risk. The most well-known and frequently discussed is whether to punt the ball on fourth down or ‘go for it.’ Romer (2006) suggested football coaches were too conservative and risk averse in their choices. So there are opportunities in such settings to measure risk and better manage it. Application of investment theory such as we have done for basketball might be useful in such contexts. Unlike Romer’s results in professional American football, we have found NBA teams seem to manage risk very efficiently relative to the objective function used in this paper. Of course, they have many more trials to learn from than a football team. College and professional football coaches may encounter such risky punting decisions 2–3 times per game over 12–18 games so there are only a few occasions where these decisions may present themselves, often under close scrutiny by fans and the press and owners. NBA coaches have 82 games and over 6000 shot attempts in the course of a season which must help to shape observed optimal outcomes. 

In conclusion, the major advantage of the analysis provided in this paper, has been to condense a large amount of basketball statistics down to a small set of underlying primary performance measures. These measures are relevant for both the NBA when considering rule changes, and each team when analyzing strategy and performance. Underlying these measures is some powerful theory that has had a major impact upon managing risk and return in competitive financial markets, because it is practical and reduces the complex investment problem to assessing mean, variance and covariance of returns. In this paper, we demonstrate that the same strengths carry over to NBA basketball, to provide a very general framework relevant for analyzing 

_M. Fichman and J. O’Brien / Efficient 3-point shooting strategies_ 

120 

strategy, performance and execution. Furthermore, this approach is completely scalable and is able to accommodate finer and finer data as it becomes available without changing the underlying set of performance measures. 

### **Acknowledgments** 

We gratefully acknowledge the comments from an anonymous referee, plus Charles Friedman, the participants at seminars at Tepper School of Business, Carnegie Mellon University (CMU), participants at a seminar at CMU Qatar, MathSport International Conference 2015 Loughborough University (UK), and the 21st SIGKDD International Conference on Knowledge Discovery and Data Mining August 2015, Sydney. 

### **References** 

- Angrist, J.D. and Pischke, J., 2009, _Mostly Harmless Econometrics: An Empiricist’s Companion_ , Princeton, NJ: Princeton University Press. 

- Bodie, Z., Kane, A. and Marcus, A., 2013, _Investments_ , 10th ed. New York: McGraw-Hill Irwin. 

- Elton, E.J. and Martin, G., 1995, _Modern Portfolio Theory and Investment Analysis_ , 5th ed. New York: Wiley. 

- Goldman, M. and Rao, J.M., 2014, Misperception of Risk and Incentives by Experienced Agents. Available at: http://ssrn. com/abstract=2435551 or http://dx.doi.org/10.2139/ssrn.243 5551 

- Harville, D.A., 1977, Maximum likelihood approaches to variance component estimation and to related problems, _Journal of the American Statistical Association_ , _72_ (358), 320-338. 

- Lucey, P., Bialkowski, A., Carr, P., Yue, Y. and Matthews, I., 2014, How to get an Open Shot: Analyzing Team Movement in Basketball using Tracking Data. In: _MIT Sloan Sports Analytics Conference_ , Boston, MA. 

- Markowitz, H., 1952, Portfolio selection. _Journal of Finance_ , _7_ , 77-91. 

- Oliver, D., 2004, _Basketball on Paper: Rules and Tools for Performance Analysis_ , Washington, DC: Potomac Books. 

- Papke, L.E. and Woolridge, J.M., 1996, Econometric methods for fractional response variables with an application to 401(K) plan participation rates, _Journal of Applied Econometrics_ , _11_ , 619-632. 

- Pope, D.G. and Schweitzer, M.E., 2011, Is tiger woods loss averse? Persistent bias in the face of experience, competition, and high stakes, _The American Economic Review_ , _101_ (1), 129-157. 

- Romer, D., 2006, Do firms maximize? Evidence from professional football, _Journal of Political Economy_ , _114_ (2), 340-365. 

- Sharpe, W., 1964, Capital asset prices: A theory of market equilibrium under conditions of risk, _Journal of Finance_ , _19_ , 425442. 

- Skinner, B., 2012, The problem of shot selection in basketball, _PLoS ONE_ [e-journal], _7_ (1). https://doi.org/10.1371/ journal.pone.0030776 

- StataCorp., 2009, _Stata Statistical Software: Release 11_ , College Station, TX: StataCorp LP. 

- Walker, M. and Wooders, J., 2001, Minimax play at wimbledon, _The American Economic Review_ , _91_ (5), 1521-1538. 

- Wasserman, L., 2004, _All of Statistics: A Concise Course in Statistical Inference_ , New York: Springer Texts in Statistics. 

- Wooldridge, J.M., 2002, _Econometric Analysis of Cross Section and Panel Data_ , Cambridge: MIT Press. 


