<!-- source: library/journals/Wharton Sports Analytics Journal/2024/2024 - The Sharpe Ratio and Hitter Evaluation A New Application of Modern Portfolio Theory - Knight.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/the-sharpe-ratio-and-hitter-evaluation-a-new-application-of-modern-portfolio-theory/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2024 -->
<!-- authors: Chad Knight -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Chad Knight

The Sharpe Ratio and Hitter Evaluation A New Application of Modern Portfolio Theory

Thesis When evaluating hitters, it may be very challenging or nearly impossible to consistently predict the future returns (total bases accumulated) of individual hitters due to a variety of uncontrollable random variables. For this reason, I suggest we should shift our focus towards trying to identify hitters with minimal volatility associated with their skillset in an effort to find hitters with the highest Sharpe Ratio.

Abstract Modern Portfolio Theory aims to optimize risk-adjusted returns by identifying assets and creating portfolios with the highest Sharpe Ratio. Generally, there are two strategic approaches to optimizing risk-adjusted returns: maximizing returns or minimizing volatility. In traditional financial literature, it is generally understood that forecasting the future returns of an asset by using its historical returns as a proxy yields low correlation and limited accuracy. However, forecasting the future volatility of an asset is a much more precise science due to the autocorrelation of its squared returns resulting in volatility clusters. In this paper, I will draw comparisons between the ways returns and volatility are measured in financial markets and the ways they can be applied in baseball analytics. Furthermore, I will provide a framework for hitter evaluation by contextualizing the historical difficulty of predicting financial returns accurately, while capitalizing on the predictive nature of volatility.

Introduction In today's world of hitter evaluation there are two archetypes of people: scouts, with playing and/or coaching backgrounds and analysts, with experience in data science, quantitative studies, or finance. The goal of both parties is the same: to identify the best talent and put the best team on the field. However, at times there is a dislocation in the understanding between the methods used by the ‘baseball guys’ and the ‘math guys.’ Traditional baseball thinking relies on physical observations and experienced intuition to find professional talent. Mathematical thinking leverages statistical methods in an attempt to uncover value inobservable to the naked eye. In this paper, I will attempt to marry the two schools of thought in a manner that provides a framework for hitter evaluation based on financial risk management theories translated into digestible baseball language.

Part 1: Financial Perspective The role of a team’s general manager is complicated. The job includes negotiating contracts, evaluating talent, and fielding the best team to meet the goals of ownership. However, in its simplest form, the role can be simplified to the following: given a set of financial constraints, aggregate the optimal team of players constructed to win the most number of games in a 162 game season and compete for a World Series. A fan may view this role as a real-life fantasy baseball manager, but a financier would view this as the same role as a portfolio manager at any large investment fund. However, instead of being evaluated based on the portfolio’s accrual of returns in the terms of return-on-investment, the general manager is evaluated based on the team’s accumulation of runs, wins and losses. Viewing the role of a general manager through the lens of a portfolio manager, the objective remains the same, but the assets being used change form. Instead of valuing the risk and return of financial securities, the language changes to valuing the risk and return of players.

Part 2: Applying Financial Theory to Baseball In finance, asset performance is often spoken about in terms of returns and risk, or returns and “volatility.” Returns, or expected returns are referred to an asset’s gains (or losses) over a period of time. Volatility (risk) refers to the standard deviation of the asset’s return distribution, or in other words, the fluctuation of its value during the same timeframe.

In an ideal world, the perfect asset is one with high returns and low volatility. Think of this as an asset that consistently provides high gains with a low probability of generating losses. In practice, it's rare to find these types of assets in the market as these variables are generally inversely related. Instead, it is much more common to come across assets with high expected returns accompanied with high volatilties and assets with low expected returns accompanied by low volatilities.

Take cryptocurrency for example. In 2021, Bitcoin nearly saw roughly 100% returns. However the asset could see nearly 30% price fluctuations in any trading day. High risk, high return. On the other hand, an investment grade corporate bond may yield 5% annually, but only see a 1% fluctuation in its price on any given day. Lower risk, lower returns. Using measurements of returns and volatility to evaluate financial assets leads us to the idea of risk-adjusted returns. In finance, this concept can be illustrated using the Sharpe Ratio.

In technical terms, the Sharpe Ratio can be defined as an asset's expected return over the risk-free rate for a given level of volatility. However, risk-adjusted returns is a serviceable definition of the metric. This theoretical framework serves as the basis for Modern Portfolio Theory, originally developed by Harry Markowitz and further expanded upon by William F. Sharpe, both of whom received the 1990 Nobel Prize in Economics for their contributions. The theory suggests that the optimal pool of assets an investor should hold is the portfolio that provides the highest risk-adjusted returns – i.e. the portfolio with the highest Sharpe Ratio. The existence of the Sharpe Ratio highlights the tradeoff matrix facing a rational investor. Applying this framework to baseball, we can interpret this theory as “create the team that accumulates the most risk-adjusted wins, or produces the most risk-adjusted runs.”

Part 3: Defining Terms At the individual player level, specifically pertaining to offense, returns have a very malleable definition. However, we should seek to define returns and risk in the context of run creation. Ultimately, since total runs can be defined as a function of total bases, we can loosely define returns by using a hitter's slugging percentage. [I understand that walks and stolen bases should also contribute to a hitter’s net total bases, so I provided an adjusted version of the sharpe ratio in the appendix, see Exhibit A] Similarly, a hitter's risk, or volatility can be defined by a number of different variables such as contact percentage and chase percentage. However, for the purpose of this section, I will use a hitter’s strikeout to walk ratio (K/BB) to quantify risk, as it generally is indicative of a hitter’s ability to make contact and demonstrate plate discipline. [I understand that returns and volatility can be measured by using more advanced statistics. Please see Exhibit B for more advanced iterations of the Sharpe Ratio]

Volatility in the original financial Sharpe Ratio measures the fluctuation of an asset’s returns over a given period of time. A truly identical translation of the metric into baseball would then also measure the fluctuation of one’s [power, total bases, SLG%, etc] over a given period of time as well. However, this is where I would like to slightly alter the metric. As a baseball player, I recognize that the ability to hit for power in games is partially dependent on the ability of a hitter to first make good swing decisions and additionally make contact. By changing the volatility measurement from a historical standard deviation of a hitter’s [power, total bases, SLG, etc] I seek to articulate a more contemporary measurement of a hitter’s ‘risk’ to implement an aspect of his fundamental ability. This can help explain how efficient hitters produce returns relative to their skillsets.

For the purpose of simplicity, substituting SLG% for returns and K/BB for volatility provides us with the simplest way to illustrate the tradeoff matrix between a hitter’s power and contact and plate discipline. This also serves as a framework to answer the question “How much power output is required to make up for high levels of chase and whiff?” or “How low does one’s chase% and whiff% levels need to be to make up for a lack of power?” Using the Sharpe Ratio helps us understand how efficient hitters are at producing power and accumulating bases relative to the fundamental tendencies that are associated with limiting these outputs. Additionally, it helps us evaluate if hitters provide adequate compensation for the risk levels they carry.

Part 4: Sharpe Ratio Applications I want to be clear, I am not suggesting that the Sharpe Ratio is interchangeable with or should be substituted for other mainstream statistics such as WAR, OBP, SLG, or xwOBA. I think these are all similar statistics that measure value in different ways. Perhaps the best way to illustrate the kind of information each statistic provides is by comparing them to financial metrics used to evaluate a company's performance.

WAR is like a company's earnings. It is a holistic statistic that measures the sum of a hitter’s total offensive contributions. On-Base Percentage (OBP), Slugging Percentage (SLG), and On-Base Plus Slugging (OPS) are like a company’s earnings per share (EPS). It measures a hitter’s returns on a per plate appearance or per at-bat basis. xwOBA is like a company’s pro-forma EPS. It measures a hitter’s returns by using expected outcomes rather than actual outcomes to define performance on a per plate appearance or per at-bat basis. The Sharpe Ratio is like a company’s Return on Equity (ROE) or Return on Assets (ROA). It measures how efficiently a hitter generates returns (accumulates bases). [An alternative definition for the Sharpe Ratio in terms of baseball may be a hitter’s return on ability (ROA*). However, I will address this later.]

You wouldn’t necessarily look for the company with the highest EPS or ROE to find the most valuable company in the world. If you wanted to find the most valuable companies, a good place to start would generally be to look at the companies with the highest annual earnings (you would find Apple, Microsoft, Saudi Aramco, etc). Similarly, if you wanted to find the most valuable hitters, you would probably look at the hitters with the highest WAR (historically, you would find Bonds, Ruth and Mays, in 2023, you would find Ohtani, Acuña, and Betts) . This isn’t to say that the most valuable companies cannot have a good EPS or ROE, or the most valuable hitters cannot have good [OBP, SLG, OPS, xwOBA, or Sharpe Ratio] as in many cases they do. However, using these metrics help us perform a more concentrated analysis of player production to better understand where value can be created at an empirical level.

In searching to maximize the Sharpe Ratio, we must either look to find high returns or minimal volatility. In terms of baseball, this means, we must either look for hitters that accumulate lots of bases (hit for power) or look for hitters that exhibit extraordinarily well developed contact and plate discipline skills.

Part 5: Projecting Future Value Now that we’ve built a framework for understanding the definition of and applications for returns and volatility in the language of baseball, we can now face the challenge of finding ways to predict such variables. These are the same types of challenges economists have been studying for decades and are continuing to search for solutions. In this section I’ll provide a historical lens on how economists have attempted to predict future returns and volatility, commenting on the successes and failures in both sciences.

1. Returns In finance, the foundation for predicting the expected returns of assets can be traced back in its simplest form to the Capital Asset Pricing Model (CAPM). The model was founded by the economists William F. Sharpe, Jack Treynor, John Lintner and Jan Mossin in the 1960’s, as they expanded on the earlier work of Markowitz’s Portfolio Theory. Technically, the model suggests that an asset's excess return over the risk-free rate is proportional to its beta (a measurement of an asset's sensitivity to market movements) and market risk premium (the market, or S&P 500, return over the risk free rate). The model was innovative for its time. However, CAPM has many limitations. CAPM suggests that the only systematic risk that influences an asset’s return is the market risk itself, which is encapsulated in the beta value. This would be like predicting a hitter’s success by solely estimating his future performance based on his historical performance relative to league average. The model does not explicitly consider other factors that may influence asset returns such as a company’s size, book value, or previous returns history (momentum).

Later acclaimed models build off the fundamental framework of CAPM. Perhaps most notably, the Fama-French Three Factor Model and its many iterations (Carhart Four Factor Model) are multi-factor models that extend beyond CAPM effort to better predict future stock returns. The Fama-French Three Factor Model accounts for other risk factors such as the size and value premiums of certain companies. A historical analysis of stock returns revealed that typically small market-cap stocks outperform large market cap stocks (SMB) and value stocks typically outperform growth stocks (HML). In terms of baseball, I like to think of the SMB premium as controlling for hitters’ ages and the HML premium as controlling for a hitter's expected statistics. Younger hitters typically outperform older hitters and hitters with a higher xwOBA than wOBA theoretically performed better than their statistics indicated. While this model is more advanced than the original CAPM, its typical criticism is it leaves out other potentially relevant information such as investment, profitability, previous trading history, and time-varying risk premiums that may influence future stock prices. In baseball language, this basically means that the model ignores other factors such as a hitter’s historical statistics and tendencies (in zone swings, out of zone swings, contact percentages etc).

In baseball, a few models used to forecast player performance include the Player Empirical Comparison and Optimization Test Algorithm (PECOTA) developed by Nate Silver, the Zymborski Projection System (ZiPS) developed by Dan Szymborski, Marcel developed by Tom Tango, Oliver developed by Brian Cartwright, and Steamer developed by Jared Cross. Many of these models were developed in the last 25 years and I’d like to believe that some of them were conceived out of a framework similar to CAPM and the Fama-French financial models. Each model differs based on the variables used to make projections, and some are more advanced than others. However, each of them at their core use previous seasons’ data, along with historical player trends to forecast probable player production.

Many investment funds today develop their own proprietary trading models to evaluate assets and project future performance. However, common financial literature generally concludes that accurately predicting the future returns of stock prices consistently remains a very challenging and nearly impossible task. These findings are consistent with the (semi-strong) Efficient Market Hypothesis, which posits that all publicly available information is already reflected in asset prices and it is not possible to consistently achieve higher-than-average returns by using past information or analyzing market data. Applying this framework to baseball, when evaluating hitters, it may be very challenging or nearly impossible to consistently predict the future returns (total bases accumulated) of individual hitters due to a variety of uncontrollable random variables. For this reason, we should shift our focus towards trying to identify hitters with minimal volatility associated with their skillset in an effort to find hitters with the highest Sharpe Ratio.

2. Volatility While the research concludes that predicting individual stock returns is very difficult, the research about predicting their volatilities has shown to be more successful. The history of volatility modeling only dates back to the 1970’s. In 1973, Robert Merton, Fischer Black, Myron Scholes published their work on options pricing in the model famously known as the Black-Scholes model. However one of the limitations of the model is its assumption that the volatility of the underlying asset remains constant throughout the life of the option. This would be the baseball equivalent assuming that a hitter’s bat to ball and plate discipline skills remain constant throughout their career. Of course, variables such as age, experience, and approach among other factors contribute to the changing abilities and tendencies of hitters over the course of their careers. Similarly, the volatility of an asset's returns changes over time as a result of a variety of factors. Volatility is in fact observed to be time-varying in financial markets.

Models that address the observation of time-varying volatility were significantly advanced in 1980’s with development of the Autoregressive Conditional Heteroskedasticity (ARCH) Model in 1982 by Robert Engle, and the Generally Autoregressive Conditional Heteroskedasticity (GARCH) Model by Tim Bollerslev in 1986 [I actually took Dr. Bollerslev’s class, Financial Markets and Investments, in the Fall of 2022]. Without being too technical, the models proposed that the volatility of an asset could be measured by allowing the conditional variance of a time series to be a function of past squared observations.

The study revealed that volatility of stocks exhibited positive autocorrelation. In other words, in the same way that cold weather can be indicative of more future cold weather, and hot weather can be indicative of more future hot weather, periods of low volatility in a financial time series tend to be accompanied by further periods of low volatility, and periods of high-volatility tend to be accompanied by further periods of high-volatility. This pattern is known as the property of volatility clustering, which refers to the empirical observation that volatility tends to persist and cluster in certain time periods rather than be randomly distributed.

Following this logic, I think we can apply the same framework of using historical data to predict volatility when evaluating the risk-profile of hitters. I think a hitters' volatility (contact and plate discipline tendencies) will tend to exhibit higher levels of consistency than their returns (total base accumulation) therefore making it more predictable as well. By taking advantage of the sticky nature of volatility, we can adjust our risk-adjusted return optimization strategy to first focus on minimizing risk, rather than achieving abnormal returns. This strategy would also allow us to take advantage of the malleable nature of power, as many hitters in the past have developed their power production through the avenues of swing re-engineering and strength programs.

Part 6: Testing the Forecasting Ability of Hitters’ Returns and Volatility Using Time Series Data Once we’ve developed the hypothesis that the predictive value of hitters’ historical returns and volatility will mimic the predictive value of historical asset returns and volatility in financial markets, we need to test our hypothesis by conducting numerous time series regressions. In this section, I will analyze the findings of these regressions and compare them with the conclusions found in traditional financial market research.

Technicals There is a low correlation when using hitters’ historical technical returns to forecast their future technical returns, just as there is in financial markets. Using data from hitters with consecutive seasons of at least 300 plate appearances from 2015-2023, the statistic with the most year-over-year predictive value is OBP, and xOBP with an R-squared of 0.29. On the other hand, using historical technical volatility to forecast future technical volatility yields a significantly higher predictive value. Using a hitter’s previous season K% to predict their K% in the following year yields a 0.69 R-Squared, almost three times better than the R-squared of OBP.

Fundamentals The correlation when using hitters’ historical fundamental returns to forecast their future fundamental returns is significantly higher than when using historical technical returns to forecast future technical returns. The year-over-year predictive value of a hitter’s Barrel% yields an R-squared of 0.64. While this is more than double the predictive value OBP (0.29 R-squared), an interesting observation is that the year-over-year predictive value of a hitter’s Barrel% on his SLG only yields an R-squared of 0.17. This implies that the relationship between a hitter’s Barrel% and his SLG in the same year is not that strong (the R-squared is only 0.45). This observation is consistent with the findings of financial markets research: predicting the future returns of an asset yields low correlation and limited accuracy.

The correlation when using hitters’ historical fundamental volatility to forecast their future fundamental volatility is similarly higher than when using historical technical volatility to forecast future technical volatility. Additionally, the year-over-year predictive value of hitters’ fundamental volatility is stronger than the year-over-year predictive value of hitters’ fundamental returns. These findings are also consistent with the findings of financial market research: the predictive value of an asset’s volatility in a time series is stronger than the predictive value of its returns in a time series.

Part 7: Investment Strategy/Hitter Selection Strategy There are typically two types of analyses that are conducted before making an investment decision in finance: fundamental and technical analysis. Fundamental analysis includes the process of dissecting a company’s earnings quality. This may consist of identifying value drivers, sources of revenue, impacts of costs, the burdens of liabilities, and projecting tailwinds and headwinds. Technical analysis involves understanding how a company’s stock has performed in the market. This includes considering where the asset has been priced in the past, where it's currently trading, and where it has the potential to go. In baseball, fundamental analysis may involve understanding a hitter’s swing tendencies, swing geometry, batted ball data, age, and injury history, while technical analysis may involve understanding how a player has performed statistically in games in previous seasons.

The fundamental framework in finance for making an investment decision in a company’s stock involves comparing its intrinsic value (based on fundamentals) to its actual value (technicals). If a company’s intrinsic value exceeds its market value, then it is generally considered that the company is undervalued and its stock should be performing better than the market has indicated. Conversely, if the intrinsic value is beneath the actual value, then the company would be considered overvalued in the market relative to its fundamental value and its stock should be performing worse than the market has indicated.

This is a framework that is consistent with modern hitter evaluation. The essence of the Moneyball strategy is to leverage an understanding of implicit, player-controllable fundamentals (tendencies) to contextualize realized statistics. We should use fundamental analysis to establish a hitter’s intrinsic value, and compare this value with their realized value in terms of their counting-based statistics. If a hitter's fundamental value exceeds their actual value, we should consider this hitter to be trading at a discount, whereas if a hitter’s intrinsic value is beneath their actual value, they should be considered to be trading at a premium.

Relating this back to Modern Portfolio Theory, we should use a hitter’s fundamentals to formulate an understanding of their risk-adjusted returns. Fundamentals are typically indicative of the performance level a hitter should be experiencing by removing random occurrences of luck. Using technicals (counting-based statistics) to evaluate hitters would be the equivalent of analyzing a company by solely considering their previous returns. Just because a stock returned 5% last year isn’t sufficient enough evidence to support the conjecture that it is capable of returning 5% this year. Similarly, just because a hitter accumulated 300 bases last year doesn't necessarily indicate he is going to accumulate 300 bases this year. However at the fundamental level, it is a much safer conjecture to say that a hitter’s contact percentage or plate discipline tendencies may be close to the same level year-over-year, similar to how volatility exhibits the property of clustering in financial markets.

Part 8: Hitter Evaluation Framework

1. Identify the Proper Risk Tolerance The structure of a Major League Team and their farm system is analogous to a large investment fund diversified in equities across different stages of a company’s lifecycle. In each stage, varying levels of risk may be tolerated to satisfy each stage’s risk appetite.

Amateur players are like venture capital investments. In venture capital, many of the risky start up businesses held in the fund’s portfolio may fail. However the returns generated by one company reaching maturity far exceeds the losses incurred by the rest of the companies becoming defunct. Similarly, when teams acquire young talent through the draft or through international signings, a small percentage of the talent may actually reach the major leagues. However, the return on investment through the amateur talent pool has the highest potential by far relative to other player investment strategies. For this reason, teams may accept higher levels of risk (volatility) when considering investing in amateur players if they are accompanied by tremendous upside. A great example of this may be the Cardinals 2021 2nd round draft pick, Josh Baez, a toolsy high school position player with above average 60 grade power and an elite 70 grade arm, but high swing and miss, and chase tendencies–High risk, high returns.

Minor league players are like growth equity investments (somewhere in between mature venture capital and private equity). At this stage, management (player development) is more concerned with implementing the right systems and processes to improve revenue and cost efficiency (player performance). The risk appetite for player evaluation at this level is ultimately lower than at the amateur level merely due to a more uniform distribution of the level of competition. On the amateur side, competition varies from low level public school leagues to higher level collegiate conferences, adding another variable to account for in our risk analysis. At the minor league level, competition has been filtered to have a more comparable talent pool to the major leagues. Players exhibiting consistently higher levels of risk at minor league levels may be unfit for a team’s pre-MLB portfolio. At this stage, players are closer to maturity and weaknesses tend to be further exposed against better competition.

A team's Major League roster is ultimately like a fund's flagship long/short equity investments. At this stage, players (assets) are more mature and competition is uniform. As the majority of a team’s capital is allocated to this portfolio, their risk tolerance at this level may be the lowest relative to the rest of their holdings.

2. Identify and Evaluate the Fundamentals Although we could measure realized risk-adjusted returns by using historical returns (statistics), historical returns don’t explain why a certain asset yielded the returns they did. Similarly, historical performance doesn’t explain how a certain hitter performed the way he did. Therefore, instead of using hitter outputs to project performance, we must instead evaluate fundamentals that are conducive to maximizing returns and minimizing volatility. Begin by considering the following questions:

● What are the tendencies that are allowing for success or failure in the batters box? ● How rigid or malleable are these tendencies? ● How sustainable are the value drivers of this hitter?

Contact ● When they swing, how often do they make contact?

Plate Discipline ● When they swing, do they swing at balls or strikes? ● When they take, do they take balls or strikes? ● Do they take strikes in two-strike counts ● Do they swing at balls in three-ball counts

Power ● When they make contact, what type of contact quality and ball flight do they produce?

3. Select a Forecasting Model Ultimately, when it comes to making player projections, we need to choose a way to model our production forecasts. The purpose of having a model is to create an objective way to measure performance and project value. We can then use these objective measurements as an additional tool to supplement the physical observations made through traditional scouting.

I imagine many teams have their own proprietary models and even I have attempted to develop one myself. However, for similar reasons similar to why many hedge funds may never publicly reveal their own trading strategies or algorithms, many professional teams may never disclose their own proprietary projection systems.

As I mentioned earlier, there are many publicly available player projection systems (PECOTA, ZiPS, Steamer, etc) that can be used to create a frame of reference for anticipated player production. However, these models are predominantly aimed at forecasting the performance of major league players, and exclude amateur and minor league projections.

4. Contextualize Performance in terms of the Sharpe Ratio Many of the publicly available player projection systems are quite effective. They have a history of making some very solid predictions. However, as I mention in the thesis of this paper, forecasting future returns remains a difficult task as it is ultimately a function of a hitter's contact, plate discipline and power. Predicting power is perhaps the most challenging variable to project as it is conditional on a hitter's ability to first make advantageous swing decisions and additionally make contact. For this reason, I assert that understanding volatility is the most crucial aspect to evaluating the professional aptitudes of amateur hitters and forecasting the future values of professional hitters.

If we are to use these player projection models, I reiterate that evaluators should contextualize hitter forecasts using the framework of the Sharpe Ratio [see Exhibit C]. We should reward hitters with the propensity to display power and amplify their returns. However, in the search for hitters that offer the highest risk-adjusted returns, we should leverage the more predictable nature of hitters’ contact skills and plate discipline tendencies the same way we can leverage the property of volatility clustering in financial markets.

Authors Note I majored in Economics with a Finance Concentration at Duke partly due to the famous scene in Moneyball when Peter Brand (Jonah Hill, playing the role of Paul Depodesta) tells Billy Beane (Brad Pitt) that he majored in Economics at Yale. At 10 years old, I had no clue what the world of economics had to offer except a tangential pathway into the realm of baseball. When I started studying finance, there were times that I found myself mystified trying to comprehend the new nomenclature. However, I quickly realized that many of the terms and concepts could be understood when contextualized in baseball. As I mentioned earlier, I took a class titled “Financial Markets and Investments” taught by Tim Bollerslev, founder of the GARCH Model, when I was a senior at Duke University in the fall of 2022. Full disclosure, I probably spent 80% of my time in class trying to create baseball related analogies out of the course content in an effort to better digest the material. However, it was during this process when I discovered the inspiration behind this hitter evaluation framework. My hope in this paper is that maybe some baseball fans or finance students like myself can begin to realize that finance is comprehensible when put in terms of baseball, or baseball is comprehensible when put in terms of finance. I hope that this paper both helps baseball fans understand financial concepts often made intimidating by the presence of greek letters, and finance students understand that much of the complexity of baseball can be simplified by the language of finance.

Appendix Case Study 1: Valuing Collegiate Hitters Let’s evaluate and rank some amateur hitters in terms of risk-adjusted returns using the framework outlined above. Before I begin, I acknowledge that there are many more variables used to evaluate the professional aptitudes of position players such as size, speed, swing geometry, and defense. However, the purpose of this exercise is to help us understand how we can use the applications of modern portfolio theory to specifically measure the value being created by hitters in the batters box. Let’s use some of the best hitters from the Atlantic Coast Conference in the 2023 season in this case study. We begin with our technical analysis:

I. Technicals 1. OPS To provide context, let’s first look at a traditional statistic like OPS to see how each of the hitters performed relative to one another.

Each of the hitters finished with an elite level OPS. Kurtz and Wilken performed at a rate that mirrors the production of Barry Bonds 2001-2004 seasons. Next, let's check out the Sharpe 1 Ratio to better understand how hitters performed on a risk-adjusted basis. 2. Sharpe 1

At the top of the group, not much changes in terms of how the hitters are ranked. Kurtz and Wilken still remain significantly ahead of the field, followed by Gelof and Teel. The two biggest movers are Caden Grice, dropping two spots from 7 to 9, and Honeycutt advancing two spots from 10 to 8. However, in order to understand how hitters are creating value, we need to dig into their fundamentals. Let’s start with returns, or ‘power.’ II. Fundamentals 1. Power (Returns) My definition of power in baseball is interchangeable with ‘in-game impact.’ I like to think of Fundamental Power as a measurement of a hitter's ability to generate solid contact on the barrel. The statistic uses a variety of in-game exit data, similar to Statcast measurements used in the major leagues. Specifically, it is representative of a hitter's average contact quality. For reference anything above a 2.000 is considered elite, and in between 1.850-2.000 is considered above average.

Morales is the leader among the group, followed by Wilken and Kurtz. Using the interpretation of power as returns, we can use the ranking of this fundamental category to rank the hitters in terms of unadjusted returns potential. Let's now take a look at the fundamentals that compose a hitter’s volatility. 2. Contact (Volatility1)

Teel ‘takes the cake’ for bat to ball skills. I use my own variation of a hitter’s contact percentage to evaluate bat to ball skills, so the numbers don't necessarily represent the equation [# of contact] / [# of swings]. An interesting observation is how far Wilken falls. While he was 2nd in OPS and Sharpe 1, he is 9th in Fundamental Contact. I’ll comment more on this later. I also want to provide some context for how each fundamental measurement of volatility helps us understand its impact on a hitter’s risk profile. Below is a table displaying the results of a regression between Fundamental Contact and K%, BB%, and K/BB. I think it is important to dissect our measurement of risk in Sharpe 1, K/BB, by analyzing its two variables K% and BB%.

It is evident that a hitter’s Fundamental Contact is the strongest at explaining a hitter's K% with an R-Squared of 0.610. Let’s next take a look at the another contributing factor to volatility, plate discipline. 3. Plate Discipline (Volatility2) Measuring plate discipline is a highly debated topic, as there are a variety of contributing factors such as the strike zone, the count, and the situation. However, for the purpose of simplicity, I like to think about plate discipline as a weighted average of a hitter’s swing and take decisions. For every pitch, four things can happen: the pitch can be a ball or a strike, and the hitter can choose to swing or take. The value of taking a pitch out of the zone in a three ball count or swinging at a pitch in the zone in a two strike count outweighs the value of these decisions in an 0-0 count. Similarly, the consequences of swinging at a pitch out of the zone in a three-ball count or taking a pitch in the zone in a two-strike count outweigh the consequences of these decisions in a 0-0 count. Using this intuition to measure plate discipline yields the following results.

Wilken and Teel trade rankings in fundamental plate discipline. Similar to Wilken’s contact, Teel’s plate discipline is lower than the majority of the group. This is an interesting observation. Both hitters had incredible seasons. Teel won ACC Player of the Year and had a .400 batting average over the course of the season. Wilken had the second most home runs in division 1 college baseball, and had more walks than strikeouts. What this tells me is that there are multiple combinations of a hitter’s fundamentals that can create value in the batters box.

When analyzing the strengths of Fundamental Plate Discipline, it is evident that it is the strongest at predicting BB%. This makes intuitive sense, as hitters with better plate discipline generally have better pitch recognition and make smarter swing decisions, ultimately leading to more walks. Specifically pertaining to measuring a hitter’s volatility, it is challenging to decipher which fundamental, contact or plate discipline is more valuable, as there are different hitting styles that may leverage one ability over the other. However, perhaps we can better understand the risk profile a hitter has when measuring the sum of the two fundamentals. 4. Contact and Plate Discipline (Volatility12) The intuition of measuring contact and plate discipline together is similar to the idea of taking the sum of a hitter’s on-base percentage (OBP) and slugging percentage (SLG) to create on-base plus slugging (OPS). A hitter who has elite contact skills may be able to afford having poorer plate discipline, as they may be able to make contact with pitches out of the zone (Kyle Teel). Similarly, a hitter with elite plate discipline may be able to afford having poorer contact skills (Brock Wilken). The ideal hitter may have both, and that is what the sum of the two fundamental measurements of volatility attempts to calculate.

In actuality, the hitter who ranks first when combining the two fundamentals is Nick Kurtz. Kurtz ranked fourth in contact and second in plate discipline. Wiken and Teel both follow, each ranking first in one risk measurement and second to last in the other.

Additionally, we can see how the combination of both Fundamental Contact and Plate Discipline offers the most value in explaining a hitter’s volatility, K/BB. This further emphasizes the importance of comprehending how both variables, contact and discipline are equally crucial to understanding a hitter’s risk profile. One final observation is how Yohandy Morales ranks second to last. Morales ranked first out of the group in Fundamental Power. This makes sense in theory, as hitters that display high levels of power are known to also display higher levels of swing and miss and chase, similar to how assets with high potential for returns also are accompanied by higher levels of risk. To understand the value of the fundamentals on a risk-adjusted basis, we now must look at the interaction between Fundamental Power and Volatility12. 5. Fundamental Sharpe Ratio Even though Morales led the group in Fundamental Power, his returns did not provide enough compensation for his associated risk levels relative to the five hitters ahead of him. Nick Kurtz ranks just slightly ahead of Brock Wilken, as the two were ranked in the top 3 in returns, and top 2 in volatility12. In the final rankings, Horvath finished ahead of Teel. Although Teel had a better Volatility12 ranking, Horvath provided a high enough level of return to compensate for his slight additional risk.

Two interesting hitters to pay closer attention to are Jake Gelof and Vance Honeycutt. Gelof originally ranked third amongst the group in overall OPS and Sharpe 1. However he ranked 7th in power, 7th in contact, and 6th in plate discipline, yielding a composite 8th ranking. On the other hand, Honeycutt ranked dead last in OPS and 8th in Sharpe 1. However, he ranked 9th in power, 6th in contact, and 4th in plate discipline yielding a composite 7th ranking. In the discussion of Gelof vs. Honeycutt in terms of 2023 output, it's undeniable that Gelof had the more productive year (he quite literally beats Honeycutt in almost every statistical category). However, such a significant difference in both of their composite risk-adjusted fundamentals ranking begs the questions, “Did Gelof experience a disproportionate amount of good luck? And “Did Honeycutt experience a disproportionate amount of bad luck?”

Many of these players have been drafted and will no longer be playing in the ACC in the 2024 season. However, if we use the strategy I proposed earlier in this paper– leverage the predictable nature of volatility – I would be willing to forecast a more formidable offensive year out of Honeycutt given he remains healthy. Honeycutt ranked 6th in Volatility12, and was less than 1% behind the 5th ranked Lujames Groover and the 4th ranked Mac Horvath. At such an elite volatility level, I’m confident that the malleable nature of power provides him with the opportunity to offer tremendous upside in hitters returning to the ACC.

III. Conclusions Oftentimes, technical analysis and fundamental analysis arrive at similar conclusions. However, there are certain instances when differences between the two create opportunities to capitalize on undervalued fundamentals or recognize risk unobservable in technicals. For example, Nick Kurtz and Brock Wilken ranked in the top 2 during the technical analysis (OPS, Sharpe 1), and finished in the top 2 at the conclusion of our fundamental analysis. However, hitters like Vance Honeycutt and Jake Gelof experienced significant variation between their technicals and fundamentals. Expanding this framework of analysis to include all hitters across the amateur and professional levels can help identify undervalued and overlooked hitters unrecognizable when using traditional eye-test based intuition. Further applications of this framework for hitter evaluation may include, but are not limited to optimizing recruits in the transfer portal in the NCAA, identifying draft candidates or hitters to be targeted via trade, and projecting the future performance of major league hitters.

Case Study 2: Using Comparables to Identify Professional Aptitudes In Amateur Hitters Another application of our hitter evaluation framework can be used to identify professional hitters in an amateur talent pool. We can go back and look at how major league hitters performed fundamentally in their college careers to create a reference point for identifying professional fundamental value. For the purpose of this study, I will compare the ten ACC hitters I referenced in Case Study 1 to nine current major league hitters and a former Duke teammate of mine, Graham Pauley. Graham was a 13th round draft pick by the San Diego Padres in 2022, and recently was named the Padres 2023 Minor League Player of the Year. He was an overlooked prospect who flew under the radar relative to many of the other collegiate hitters selected before him in the 2022 draft. However, in this case study I will demonstrate how using our hitter evaluation framework can help explain the success he has been able to achieve thus far in the minor leagues. Fundamental Sharpe Ratio Before dissecting each tool individually, we should first develop an understanding of how each of the major league hitters' tools work together in the context of their risk-adjusted value. One observation here is each of the major leaguers scored above 2.000. This doesn’t mean that all major league hitters scored above 2.000, or that any hitter that scores above this threshold is going to be a major league hitter. However, the observation is valuable in understanding how some of the most promising young hitters in the major league performed holistically when they were in college.

We can see that only Kurtz, Wilken and Horvath surpass this threshold out of the group of amateur hitters. Pauley in fact is well beneath this level and has several other hitters ranked in front of him. Let’s dig into each tool specifically to see where he loses relative value. Contact (Volatility1) Beginning with contact, we can see that Pauley’s draft season in terms of contact ranks higher than all of the major league hitters in each of their respective draft seasons. He only falls behind recent 1st round draft pick, Kyle Teel.

Additionally, it is evident that the major league hitters are not nearly as clustered together as they were with their risk-adjusted fundamentals. Contact scores amongst the major leaguers ranges from Zack Gelof’s leading score of 0.838 to Spencer Torkelson’s 0.693. An interesting observation is how Adley Rustchman, the highest ranked major league hitter of the group in terms of risk-adjusted fundamentals, actually ranks third to last out of all 20 players in this chart. This is a similar observation to how far Brock Wilken fell in terms of his fundamental contact ranking, but still maintained a very high overall ranking in the previous case study. This tells us that fundamental contact alone is not necessarily the greatest indicator of professional aptitude, and it is perhaps better understood when coupled with hitters’ fundamental plate discipline.

Plate Discipline (Volatility2) In terms of fundamental plate discipline, Pauley doesn’t rank higher than eight out of the nine major leaguers. However, his 0.232 score is 31% higher than his close fundamental contact comparable, Kyle Teel, who scored a 0.177. This will be important when analyzing the sum of the two fundamentals later.

Similar to fundamental contact, there isn’t a noticeable fundamental plate discipline threshold where the major league hitters begin to cluster. However, I think it's interesting that Nolan Schanuel, who was promoted to the major leagues after only playing in 22 minor league games, led the group in plate discipline with a score of 0.344. Contact and Plate Discipline (Volatility12) When we look at the combination of contact and plate discipline, we see a similar clustering pattern of the major league hitters observed in the risk-adjusted fundamentals rankings. Eight out of nine of them score above a 1.000. I reiterate that just because a hitter does not cross this threshold does not mean that they do not possess major league aptitude, as in many cases players have the ability to improve. However, I feel confident making the conjecture that the higher the combined value of contact and discipline scores a player has, the more likely they are to have major league aptitude.

Pauley ranked third out of the group of hitters with a score of 1.074, falling only behind Nolan Schanuel and Zack Gelof. His significantly better plate discipline than Teel helps him rank eight spots higher than him in the Volatility12 rankings. This is an extraordinarily low level of volatility, meaning that a lower level of power (returns) are required of him to provide adequate risk-adjusted returns relative to each of the other players. Power Finally, understanding hitters’ volatility should be done within the context of their potential for returns. I emphasize that the power score does not necessarily indicate who hits the most home runs, but rather who consistently makes hard contact and finds the barrel of the bat. Power scores amongst the major league hitters also do not cluster around a certain threshold, similar to their contact scores. Rustchman’s power score of 2.209 from his draft season ranks significantly higher than the rest of the major league hitters on this list. Nolan Schanuel’s score of 1.816 is the lowest amongst the major leaguers. From a first glance, this makes intuitive sense as in Schanuel’s brief stint in major league baseball, he collected only 4 extra base hits in 109 at-bats.

Pauley finished dead last among the group in power, ultimately causing him to lose a significant amount of value under this risk-adjusted evaluation framework. However, as I mentioned earlier, the range of power scores each major league hitter earned in their draft years has a very large range, and the metric is not necessarily indicative of major league aptitude when viewed alone.

Conclusion The challenge of identifying major league talent varies in difficulty. Of course, there are some players that possess undeniably advanced tools observable to the naked eye. However, there are also some cases of players whose talent requires deeper analysis to identify.

Specifically pertaining to Pauley, his risk-adjusted fundamentals score is significantly altered by a lackluster power score. But this is where it is important to supplement our fundamental analysis with traditional scouting and experienced baseball intuition. Using analytics, we can identify Pauley’s elite level of Volatility12 relative to the rest of the major leaguers, making him a hitter with a very low risk profile. Under the framework of contextualizing player performance using the Sharpe Ratio, this means fewer returns (power) are required of him to provide us with an equally valuable risk-return tradeoff. Using traditional scouting to help forecast his potential to create future value, we can ask ourselves what the likelihood of improving Pauley’s returns (power) is through [swing changes, strength programs or approach changes].

In 2023, Pauley finally unlocked previously unseen power while still maintaining a relatively low risk-profile. He slugged 23 home runs and had a 0.539 slugging percentage, while accumulating 60 walks and 93 strikeouts in

127 games across the A, A+, and AA minor league levels. It will be interesting to see how Pauley progresses in 2024. However, after a solid 2023 minor league campaign, he remains a prime example of a traditionally overlooked amateur hitter who could have been identified as a more valuable asset out of college if evaluated using a risk-adjusted fundamentals framework. The same volatility-minimizing investment thesis used for Pauley could be applied when forecasting the value of Nolan Schanuel. Schanuel led the entire group of 20 hitters in Volatility12, effectively making him the hitter with the lowest risk-profile. In 2023, Schanuel reached base safely in all 29 games he played, finished with a 0.402 on base percentage, and had more walks (20) than strikeouts (19). However, he only had a slugging percentage of 0.330. I reiterate, we should reward hitters with the propensity to display power and amplify their returns. However, in the search for hitters that offer the highest risk-adjusted returns, we should leverage the more predictable nature of hitters’ contact skills and plate discipline tendencies as they are more conducive to enabling the future development of one’s power.

Exhibit A: Adjusted Sharpe Ratio for Stolen Bases I understand that walks and stolen bases are left out of the total bases statistic in the first iteration of the Sharpe Ratio. However, depending on what we are choosing to evaluate, we can either choose to adjust the total bases equation by adding them in or leave them out to completely isolate the value created in the batters box.

Think about the question “Why did Rickey Henderson steal so many bases?” Was it because he was the fastest player that ever played baseball? Or was he just the best baserunner in history? It is possible that the answer to the previous two questions is in fact, yes. However, Henderson also had a career .401 OBP, led the league in walks four separate times, and had more walks than strikeouts over the course of his career. His ability to steal bases was enabled by his elite ability to get on base. Nonetheless, we can create an adjusted Sharpe Ratio to help visualize how a player's speed may enhance their risk-adjusted returns.

Financial Term Returns Volatility

Sharpe Ratio V2 Baseball Translation Total Bases + Stolen Bases Contact + Plate Discipline

Baseball Statistic (TB+SB-CS)/(AB)

(K/BB)X

Name Ronald Acuna Jr.

Shohei Ohtani Mookie Betts Aaron Judge Yordan Alvarez Kyle Tucker Corey Seager

Matt Olson Juan Soto Freddie Freeman

Highest Sharpe 2 Ratios 2023 (300 PA minimum)

Sharpe 1 Sharpe 2 %∆ Sharpe SLG

K/BB

0.589

0.679

15%

0.596

1.05

0.584

0.609

4%

0.654

1.57

0.564

0.582

3%

0.579

1.11

0.556

0.561

1%

0.613

1.48

0.543

0.542

0%

0.583

1.33

0.499

0.542

9%

0.517

1.15

0.538

0.540

0%

0.623

1.80

0.537

0.538

0%

0.604

1.61

0.522

0.535

2%

0.519

0.98

0.498

0.528

6%

0.567

1.68

Net SB 59 14 11 2 0 25 1 1 7 22

Largest Benefits From Speed Adjustments 2023 (300 PA minimum)

Name

Sharpe 1 Sharpe 2 %∆ Sharpe SLG

K/BB

Esteury Ruiz

0.231

0.312

35%

0.345

4.950

Jorge Mateo

0.245

0.306

25%

0.34

3.727

Jake McCarthy

0.262

0.327

24%

0.326

2.385

Taylor Walls

0.277

0.335

21%

0.333

2.091

Starling Marte

0.225

0.269

20%

0.324

4.313

Willi Castro

0.315

0.374

19%

0.411

2.912

CJ Abrams

0.297

0.352

19%

0.412

3.688

Brice Turang

0.239

0.282

18%

0.3

2.474

Corbin Carroll

0.416

0.487

17%

0.506

2.193

Elly De La Cruz

0.288

0.337

17%

0.41

4.115

Net SB 54 27 22 21 20 28 43 22 49 27

Exhibit B: Sharpe Ratio Variations

While in this paper I almost exclusively reference Sharpe 1 to illustrate a hitter’s risk-adjusted returns, I recognize that there are other statistics we can use to define a hitter’s returns and volatility. The following chart shows a few different ways the theory of the Sharpe Ratio can be used to measure the tradeoff matrix of a hitter’s power, contact, and plate discipline.

Iteration Sharpe 1 Sharpe 2 Sharpe 3 Sharpe 4 Sharpe 5 Sharpe 6 Sharpe 7 Sharpe 8 Sharpe 9 Sharpe 10 Sharpe 11

Financial Term

Baseball Translation

Baseball Statistic

Returns

Total Bases

Slugging%

Volatility

Contact & Plate Discipline

(K/BB)X

Returns

Total Bases + Stolen Bases (TB+SB-CS)/(AB)

Volatility

Contact & Plate Discipline

(K/BB)X

Returns

Contact Quality

Barrel%

Volatility

Contact%

Whiff%

Returns

Contact Quality

Barrel%

Volatility

Plate Discipline

Chase%

Returns

Contact Quality

Hard Hit%

Volatility

Contact

Whiff%

Returns

Contact Quality

Hard Hit%

Volatility

Plate Discipline

Chase%

Returns

Contact Quality

Barrel% + Hard Hit%

Volatility

Contact

Whiff%

Returns

Contact Quality

Barrel%+Hard Hit%

Volatility

Contact & Plate Discipline

Chase%

Returns

Contact Quality

Barrel%

Volatility

Contact & Plate Discipline

Whiff%+Chase%

Returns

Contact Quality

Hard Hit%

Volatility

Contact & Plate Discipline

Whiff%+Chase%

Returns

Contact Quality

Barrel%+Hard Hit%

Volatility

Contact & Plate Discipline

Whiff%+Chase%

Exhibit C: Using Steamer Projections to Forecast Risk-Adjusted Returns

Rank 1 2 3 4 5 6 7 8 9 10

## 2024 Steamer Sharpe 1 Projections (300 PA Min)

Name

Team Steamer Sharpe 1

SLG

Juan Soto

NYY

0.583

0.558

Ronald Acuña Jr.

ATL

0.535

0.578

Yordan Alvarez

HOU

0.530

0.591

Aaron Judge

NYY

0.491

0.563

Kyle Tucker

HOU

0.491

0.530

José Ramírez

CLE

0.486

0.501

Vladimir Guerrero Jr. TOR

0.483

0.528

Matt Olson

ATL

0.476

0.543

Mookie Betts

LAD

0.475

0.513

Shohei Ohtani

LAD

0.472

0.549

K/BB 0.835 1.361 1.538 1.729 1.361 1.129 1.428 1.691 1.353 1.827

Rank 1 2 3 4 5 6 7 8 9 10

## 2024 Steamer Sharpe 2 Projections (300 PA Min)

Name

Team Steamer Sharpe 2 SLG

Ronald Acuña Jr.

ATL

0.599

0.578

Juan Soto

NYY

0.593

0.558

Yordan Alvarez

HOU

0.529

0.591

Kyle Tucker

HOU

0.518

0.530

José Ramírez

CLE

0.508

0.501

Aaron Judge

NYY

0.500

0.563

Mookie Betts

LAD

0.494

0.513

Vladimir Guerrero Jr. TOR

0.491

0.528

Shohei Ohtani

LAD

0.487

0.549

Bryce Harper

PHI

0.480

0.518

K/BB Net SB

1.361 41

0.835

1.538

1.361 18

1.129 16

1.729

1.353 11

1.428

1.827 13

1.542
