<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2018/2018 - How to Play Strategically in Fantasy Sports (and Win) - Unknown Authors.pdf -->



# **How to Play Strategically in Fantasy Sports (and Win)** 

Paper Track: Other Sports Paper ID: 5558 

## **1. Introduction** 

Daily Fantasy Sports (DFS) has become a multi-billion dollar industry [24, 20, 28, 1, 30] with millions of annual users [14, 28]. The pervasiveness of fantasy sports in modern popular culture is reflected by the regular appearance of articles discussing fantasy sports issues in the mainstream media. Moreover, major industry developments and scandals are now capable of making headline news as evidenced in Figures 1(a) and 1(b) below. The two major DFS websites are FanDuel and DraftKings and together they control approximately 95% of the U.S. market [24, 20]. Approximately 80% of DFS players have been classified as _minnows_ [25] as they are not believed to use sophisticated techniques for decision-making and portfolio construction. Accordingly, these users provide financial opportunities to the so-called _sharks_ who do use sophisticated techniques [25, 29, 22, 17] when constructing their fantasy sports portfolios. The goal of this paper is to provide a coherent framework for constructing fantasy sports portfolios where we explicitly model the behavior of other players. Our approach is therefore strategic and to the best of our knowledge, we are the first academic work to develop such an approach in the context of fantasy sports. 

The number of competitors in a typical DFS contest might range from thousands to hundreds of thousands with each competitor constructing a fantasy team of real world players, e.g. National Football League (NFL) players in a fantasy football contest, with each portfolio being subject to budget and possibly other constraints. The performance of each portfolio is determined by the performances of the real world players in a series of actual games, e.g. the series of NFL games in a given week. The competitors with the best performing portfolios then earn a monetary reward, which depends on the specific payoff structure, e.g. _double-up_ or _top-heavy_ , of the DFS contest. 

Several papers have already been written on the topic of fantasy sports. For example, Fry, Lundberg, and Ohlmann [13] and Becker and Sun [4] develop models for season-long fantasy contests while Bergman and Imbrogno [5] propose strategies for the survivor pool contest, which is also a season long event. Several papers have been written of course on so-called office pools (which pre-date fantasy sports contests), where the goal is to predict the maximum number of game winners in an upcoming elimination tournament such as the _March Madness_ college basketball tournament. Examples of this work include Kaplan and Garstka [19] and Clair and Letscher [6]. There has been relatively little work, however, on the problem of constructing portfolios for daily fantasy sports. One notable exception is the recent work of Hunter et al. [18], which is closest to the work we present in this paper. They consider a winner-takes-all payoff structure and aim to maximize the probability that one of their portfolios (out of a total of 𝑁) wins. Their approach is a greedy heuristic that maximizes their portfolio means, i.e. expected number of fantasy points, subject to constraints that lower bound their portfolio variances and upper bound 



1 

2018 Research Papers Competition Presented by: 



their inter-portfolio correlations. Technically, their framework requires the solution of linear integer programs and they apply their methodology to fantasy sports contests, which are top-heavy in their payoff structure as opposed to winner-takes-all. Their work has received considerable attention, e.g. [8], and the authors report earning<sup>1</sup> significant sums in real fantasy sports contests based on the National Hockey League (NHL) and baseball. 

There are several directions for potential improvement, however, and they are the focus of the work in this paper. First, Hunter et al. [18] do not consider their opponents’ behavior. In particular, they do not account for the fact that the payoff thresholds are stochastic and depend on both the performances of the real-world players as well as the unknown team selections of their fellow fantasy sports competitors. Second, their framework is only suitable for contests with the top-heavy payoff structure and is in general not suitable for the double-up payoff structure. Third, their approach is based on (approximately) optimizing for the winner-takes-all payoff, which is only a rough approximation to the top-heavy contests they ultimately target. In contrast, we directly model the true payoff structure (top-heavy or double-up) and seek to optimize our portfolios with this objective in mind. 





(a) New York Times headline, 5 October 2015        (b) NBC News headline, 3 August 2016 

Figure 1: Fantasy Sports in the News. 

Our work makes several contributions to the DFS literature. First, we formulate an optimization problem that accurately describes the DFS problem for a risk-neutral decision-maker in both double-up and top-heavy settings. Our formulation seeks to maximize the expected reward subject to portfolio feasibility constraints and we explicitly account for our opponents’ unknown portfolio choices in our formulation. Second, we connect our problem formulation to the finance literature on 

> 1 They donated all earnings to charity and we intend to do the same at the end of the 2017-18 NFL season, which is the basis for the real-world contests that we are currently playing using our methodology. Further details are available in Section 6. 

2 



2018 Research Papers Competition Presented by: 



mean-variance optimization and in particular, the mean-variance literature on outperforming stochastic benchmarks. Using this connection, we show how our problem can be reduced (via some simple assumptions and approximations) to the problem of solving binary quadratic programs. Third, we can use our model to estimate the value of “insider trading” where an insider, i.e. an employee of the DFS contest organizers, gets to see information on opponents’ portfolio choices before making his own team selections. This has been a topic of considerable recent media interest [9, 10]; see also Figure 1(a), which refers to the case of a DraftKings employee using data from DraftKings contests to enter a FanDuel DFS contest in the same week and win $350,000. This problem of insider trading is of course also related to the well-known value-of-information concept from decision tree analysis. A further contribution of our work is the introduction of a Dirichletmultinomial data generating process for modeling opponents’ team selections. We estimate the parameters of this model via Dirichlet regressions and we demonstrate its value in predicting opponents’ portfolio choices. Finally, we demonstrate the value of our framework by applying it to both double-up and top-heavy DFS contests in the 2017-2018 NFL season. While the season is still ongoing (as of writing), our results to date are positive particularly in the top-heavy contests, which are our main focus. 

The remainder of this paper is organized as follows. In Section 2, we formulate both the double-up and top-heavy versions of the problem while we outline our Dirichlet regression approach to modeling our opponents’ team selections in Section 3. In Section 4, we use results from meanvariance optimization (that relate to maximizing the probability of outperforming a stochastic benchmark) to solve the double-up problem. We then extend this approach to solve the top-heavy problem in Section 5 and we present numerical results based on the 2017-18 NFL season for both problem formulations in Section 6. In Section 7, we briefly discuss the value of information and in particular, how much an insider can profit from having advance knowledge of his opponents’ team selections. We conclude in Section 8, where we also discuss some directions for ongoing and future research. Some technical details and results are deferred to the appendix. 

## **2. Problem Formulation** 

We assume there are a total of 𝑃 players whose performance, 𝜹∈ℝ<sup>𝑃</sup> , in a given round of games is random. We will assume<sup>2</sup> that 



so that 𝜹 is multivariate normally distributed with mean vector 𝝁𝜹 and variance-covariance matrix 𝜮𝜹. Our goal in the fantasy sports competition is to choose a portfolio 𝒘∈{0,1}<sup>𝑃</sup> of athletes. Typically, there are many constraints on 𝒘. For example, in a typical NFL fantasy sports contest, we will only be allowed to select 𝐶= 9 players out of a total of 𝑃≈100 to 300 NFL players. Each 

> 2 While the formal results of Sections 4 and 5 require a normality assumption, we note that the mean-variance framework we develop can still be used even if normality is not justified. Moreover, we are free in lines 10 and 4 of Algorithms 2 and 3, respectively, to use a more accurate probability distribution if we so desire. 



3 

2018 Research Papers Competition Presented by: 



player also has a certain “cost” and our portfolio cannot exceed a given budget 𝐵. These constraints on 𝒘 can then be formulated as 





where 𝑐𝑝 denotes the cost of the 𝑝<sup>𝑡ℎ</sup> player. Other constraints are also typically imposed by the context organizers. These constraints include positional constraints, e.g. exactly one quarterback can be chosen, diversity constraints, e.g. you can not select more than 4 players from any single NFL team, etc. These constraints can generally be modeled as linear constraints and we use 𝕎 to denote the set of binary vectors 𝒘∈{0,1}<sup>𝑃</sup> that satisfy these constraints. 

A key aspect of our approach to constructing fantasy sports portfolios is in modeling our opponents, i.e. other players who also enter the same fantasy sports competition. We assume there are 𝑂 such opponents and we use 𝑾op ≔{𝒘𝑜}𝑂𝑜=1 to denote their portfolios with each 𝒘𝑜 ∈𝕎. Once the round of NFL games has taken place, we get to observe the realized performances 𝜹 of the 𝑃 NFL players. Our portfolio then realizes a points total of 𝐹≔𝒘<sup>T</sup> 𝜹 whereas our opponents’ realized point totals are 𝐺𝑜 = 𝒘𝑜<sup>T</sup> 𝜹 for 𝑜= 1, … , 𝑂. All portfolios are then ranked according to their points total and the cash payoffs are determined. These payoffs take difference forms, depending on the structure of the contest. There are two contest structures that dominate in practice and we consider both of them. They are the so-called double-up and top-heavy structures. 

### **2.1. The Double-Up Problem Formulation** 

Under the double-up payoff structure, the top 𝑟 portfolios (according to the ranking based on realized points total) each earn a payoff of 𝑅 dollars. Suppose now that we enter 𝑁≪𝑂 portfolios<sup>3</sup> to the contest. Then, typical values of 𝑟 are 𝑟= (𝑂+ 𝑁)/2 and 𝑟= (𝑂+ 𝑁)/5 with corresponding payoffs of 𝑅= 2 and 𝑅= 5 assuming an entry fee of 1 per portfolio. The (𝑟= (𝑂+ 𝑁)/2, 𝑅= 2) case is then a double-up competition whereas the (𝑟= (𝑂+ 𝑁)/5, 𝑅= 5) is a _quintuple-up_ contest. We will refer to all such contests as “double-up” contests except when we wish to draw a distinction between different types of double-up contests, e.g. (true) double-up versus quintuple-up. In practice of course, the contest organizers take a cut and keep approximately 15% of the entry fees for themselves. This is reflected by reducing 𝑟 appropriately and we note that this is easily accounted for in our problem formulation below. We also note that this means the average DFS player loses approximately 15% of her initial entry. In contrast to financial investments then, DFS 

> 3 There is usually a cap imposed by the contest organizer, however. Typical cap sizes we have observed can range from 𝑁= 1 to 𝑁= 150. 



4 

2018 Research Papers Competition Presented by: 



investments are on average NPV-negative and so some skill is required in portfolio construction to overcome this handicap. 

While it is possible and quite common for a fantasy sports player to submit multiple entries, i.e. multiple portfolios, to a given contest, we will consider initially the case where we submit just 𝑁= 1 entry. Given the double-up payoff structure, our fantasy-sports portfolio optimization problem is to solve 



𝑂 where we use 𝐺<sup>(𝑟)</sup> to denote the 𝑟<sup>𝑡ℎ</sup> order statistic of {𝐺𝑜}𝑜=1 and we define 𝑟<sup>′</sup> ≔𝑂+ 1 −𝑟. Note that we explicitly recognize the dependence of 𝐺<sup>(𝑟)</sup> on the portfolio selections 𝑾op of our 𝑂 opponents and the performance vector 𝜹 of the NFL players. 

### **2.2. The Top-Heavy Problem Formulation** 

The top-heavy payoff structure is more complicated than the double-up structure as the size of the cash payoff generally increases with the portfolio ranking. In particular, we first define payoffs 



and corresponding percentiles 



Then a portfolio whose rank lies in (𝑟𝑑−1, 𝑟𝑑] × 𝑂 wins 𝑅𝑑 for 𝑑= 1, … , 𝐷. In contrast to the double-up structure, we now account<sup>4</sup> for the possibility of submitting 𝑁> 1 entries to the contest. We use 𝑾≔{𝒘𝑖}𝑁𝑖=1 to denote these entries and 𝐹𝑖 ≔𝒘T𝑖 𝜹 to denote the realized fantasy points total of our 𝑖<sup>𝑡ℎ</sup> entry. 

It is then easy to see that our fantasy-sports portfolio optimization problem is to solve 



′ (𝑟) 𝑡ℎ 𝑂 𝑁 where 𝑟𝑑 = 𝑂+ 𝑁−𝑟𝑑𝑂, 𝐺−𝑖 is the 𝑟 order statistic of {𝐺𝑜}𝑜=1 ∪ {𝐹𝑗}𝑗=1 ∖𝐹𝑖 and 𝑾−𝑖 ≔𝑾∖𝒘𝑖. We note again that the top-heavy payoff structure is our main concern in this paper. That said, it should be clear that the double-up formulation of (1) is a special case of the top-heavy formulation in (2). We will therefore address the double-up problem before taking on the top-heavy problem. Before doing this, however, we must discuss the modeling of our opponents’ portfolios 𝑾op. 





5 

2018 Research Papers Competition Presented by: 



## **3. Modeling Opponents’ Team Selections** 

A key aspect of our modeling approach is that there is value to modeling our opponents’ portfolio choices, 𝑾op. This is in direct contrast to the work of Hunter et al. [18], who ignore this aspect of the problem and focus instead on constructing portfolios that maximize the expected number of fantasy points, subject to possible constraints<sup>5</sup> that encourage high-variance portfolios. In numerical simulations, we obtained significant gains in expected dollar payoffs by explicitly modeling 𝑾op. This followed because of the well-known fact that some players are (often considerably) more popular than other players and because there is some predictability in the team selections of players who may be responding to weekly developments that contain more noise than genuine information. To the best of our knowledge, we are the first to explicitly model 𝑾op and embed it in our portfolio construction process. That said, we certainly acknowledge that some members of the fantasy sports community also attempt to be strategic in their attempted selection of less popular players and avoidance of more popular players, other things being equal; see for example Gibbs [15]. 

If we are to exploit out opponents’ team selections, then we must be able to _predict_ 𝑾op reasonable accurately. Indeed it is worth emphasizing that 𝑾op is _not observed_ before the contest and so we must make do with predicting it. In most fantasy sports contests, however, it is possible to learn about 𝑾 after the contest is over and the winners have been announced. We therefore assume we op have access to partial data on 𝑾op from previous contests. In particular, we make the reasonable assumption that we have access to sufficient data to estimate the 1-dimensional marginal distributions<sup>6</sup> of 𝒘𝑜 ∈{0,1}<sup>𝑃</sup> , a random opponent’s portfolio. We will also assume we have access to other observable features, e.g. expected NFL player performance 𝝁𝜹, home or away indicators, quality of opposing teams etc. from these previous contests. We will use this information to build a Dirichlet regression model for estimating the marginal distributions of 𝒘𝑜. Towards this end, we must first describe our regression model and then in Section 3.2, we put everything together to (implicitly) define the distribution of 𝑾op. 

### **3.1. Dirichlet Regression** 

To make things clear, we will focus on the specific case of DFS in the NFL setting. Specifically, consider for example the following NFL contest organized by FanDuel [11]. Each fantasy team has 𝐶= 9 positions which must consist of 1 quarterback (QB), 2 running backs (RB), 3 wide receivers (WR), 1 tight end (TE), 1 kicker (K) and 1 defense (D). Consider now the marginal distribution of 

> 5 They included constraints that encouraged high-variance portfolios because they too were focused on top-heavy contests where very few contestants earn substantial payoffs. It is intuitively clear that high-variance portfolios are desirable for such contests. We discuss this property in further detail in Sections 4 and 5 in light of the results from mean-variance optimization that we bring to bear on the problem. 

> 6 Sometimes we can only get to observe 𝑾op after a contest via web-scraping, something that is not very desirable and that is frowned upon by some sites. 



6 

2018 Research Papers Competition Presented by: 



the QB selections<sup>7</sup> in 𝒘𝑜. To begin, we assume there is a total of 𝑁QB QB’s available for selection and we number them from 𝑘= 1 to 𝑘= 𝑁QB. We assume a Dirichlet-multinomial data generating process for QB selection. Specifically, we assume: 

- 𝒑QB~Dir(𝜶QB) where Dir(𝜶QB) denotes the Dirichlet distribution with parameter vector 𝜶QB. 

Note 𝒑QB ≔{𝑝𝑄𝐵𝑘 }𝑁𝑘=1QB lies on the unit simplex in ℝ𝑁QB and therefore defines a probability distribution over the available quarterbacks. We can therefore 

- 𝑘 

- • Select QB 𝑘 with probability 𝑝𝑄𝐵 for 𝑘= 1, … , 𝑁QB. 

It is important to note that the selection probabilities 𝒑QB are not known in advance of the DFS contest. Moreover, they do not appear to be perfectly predictable and so we have to explicitly model<sup>8</sup> their randomness. We do this by assuming instead that the parameter vector 𝜶QB in ℝ<sup>𝑁QB</sup> is predictable. In particular, we assume 



where 𝜷QB is a vector of parameters that we must estimate and 𝑿QB is a matrix (containing 𝑁QB rows) of observable independent variables that are related to the specific features of the NFL games and QB's underlying the DFS contest. To be clear, the exponential function in the r.h.s. of (3) is actually an 𝑁QB × 1 vector of exponentials. 

For example, in a DFS contest for week 𝑡, we might assume 



where 𝒇𝑡QB is an estimate of 𝒑QB that we can obtain from the FantasyPros website [12], 𝒄𝑡QB are the 𝑡 (appropriately scaled) costs of the QB’s in the contest, and 𝝁QB is an (appropriately scaled) subvector of 𝝁𝜹 whose components correspond to the QB positions in 𝝁𝜹 **.** Other features are of course 𝑡 𝑡 also possible. For example, we might also want to include expected returns 𝝁QB/𝒄QB (where 

> 7 Recall that 𝒘𝑜 ∈{0,1}<sup>𝑃</sup> where 𝑃 is the total number of NFL players available for selection. We can assume then that the first 𝑁QB < 𝑃 components of 𝒘𝑜 correspond to the 𝑁QB QB's and so a feasible portfolio will set exactly one of these components to 1 with the remaining 𝑁QB −1 components set to 0. The QB component set to 1 corresponds of course to the QB that is selected in the portfolio. 

> 8 In initial unreported experiments we assumed 𝒑QB was fixed and known but this led to overcertainty and poor performance of the resulting portfolios. 



7 

2018 Research Papers Competition Presented by: 



division is understood to be component-wise), home-away indicators, quality of opponents etc. as features. That said, these latter features should already be accounted for by the features included in (4). 

We can estimate the 𝜷QB vector by fitting a Bayesian Dirichlet regression. Assuming we have data from weeks 𝑡= 1 to 𝑡= 𝑇−1 and a flat prior on 𝜷QB, then the posterior satisfies 



where B(𝜶𝑡QB) is the normalization factor for the Dirichlet distribution. We fit this model using Bayesian software package `STAN` [27]. 

### **3.2. Generating Random Opponents’ Portfolio** 

Suppose now that the Dirichlet regression model has been fit for each position, i.e. the 𝜶QB, 𝜶RB, 𝜶TE etc. vectors have all been estimated. The question arises as to how we can use them to define a random opponent's portfolio 𝒘𝑜. We note that the fitted Dirichlet regression models provide a QB straightforward mechanism for defining the _positional marginals_ of 𝒘𝑜. For example, let 𝒘𝑜 denote the 𝑁QB × 1 sub-vector of 𝒘𝑜 corresponding to the QB's available for selection. We can easily generate a sample of this vector by: 

1. First drawing a sample 𝒑QB from the Dir(𝜶QB) distribution. 

2. Then drawing a single sample from the Mult(𝒑QB) distribution, i.e. multinomial distribution with parameter vector 𝒑QB. 

- QB 

- 3. This draw then defines our chosen QB, i.e. it sets one component of 𝒘𝑜 to 1 with the others being set to 0. 

The obvious approach to defining the distribution of 𝒘𝑜 is to assume that each positional marginal vector is independent and therefore drawn according to the 3 steps outlined above with the obvious understanding that 𝜶RBwould be used for the RB positions, 𝜶TE for the TE position etc. This marginal independence assumption then defines the distribution of a _potential_ 𝒘𝑜. There is no guarantee, however, that the resulting portfolio is feasible, i.e. that 𝒘𝑜 ∈𝕎. We therefore use an accept-reject approach whereby potential portfolios 𝒘𝑜 are generated according to the steps outlined above and are only accepted if they are feasible. In fact, we impose one further condition: we insist that an accepted 𝒘𝑜 uses up most of the available budget. We impose this condition because it is very unlikely in practice that a player in a DFS contest would leave much of his budget unspent. This is purely a behavioral requirement and so we insist the cost of an accepted 𝒘𝑜 satisfy 𝒄<sup>T</sup> 𝒘𝑜 ≥𝐵lb for some lower bound 𝐵lb ≤𝐵 that we get to choose. Algorithm 1 below describes how 



8 

2018 Research Papers Competition Presented by: 



a random opponent's 𝒘𝑜 can be generated and therefore, it (implicitly) defines the distribution of 𝒘𝑜. (We use Mult(∙, 1) to denote a single draw from the multinomial distribution.) 

Algorithm 1 describes the case where the positional marginals are independent. It is well known, however, that some sophisticated DFS players intentionally select their portfolios so that the positional marginals of 𝒘𝑜 are _not_ independent. We are referring here to the phenomenon of socalled _stacking_ , where a portfolio is chosen with a view to maximizing its points variance (as well as its points mean). For example, if a DFS player chooses a QB from a particular team, then it is quite common for the DFS player to also choose the WR from the same team [2]. This is because the realized points of a QB and WR from the same team tend to be strongly correlated and picking the two together will result in a fantasy portfolio with a higher variance (than would otherwise be the case if the chosen QB and WR were from different NFL teams). 

We mention here that it is easy to adapt Algorithm 1 to model this stacking behavior and indeed we do this in the numerical experiments of Section 6. For example, once the QB has been chosen we could assume that the WR from the same team is then chosen with some known probability 𝑞. Otherwise the WR is chosen as before, i.e. as a draw from the relevant multinomial distribution. Note that in this latter case, stacking might still occur by chance since the positional marginals are assumed to be independent. 

**Algorithm 1** Sampling 𝑂 Opponent Portfolios 

**Require:** (𝜷QB, … , 𝜷D), (𝑿QB, … , 𝑿D), 𝒄, 𝐵lb 1: (𝜶QB, … , 𝜶D) = (exp(𝑿QB𝜷QB), … , exp(𝑿D𝜷D)) 2:  (𝒑QB, … , 𝒑D) ∼(Dir(𝜶QB), … , Dir(𝜶D)) 3: **for** 𝑜 = 1: 𝑂 **do** 4:      reject = true 5: **while** reject **do** 6:           (𝑘QB, … , 𝑘D) ∼(Mult(𝒑QB, 1), … , Mult(𝒑D, 1)) 7:           𝒘𝑜 denotes the portfolio corresponding to (𝑘QB, … , 𝑘D) 8: **if** 𝒘𝑜 ∈𝕎 and 𝒄<sup>T</sup> 𝒘𝑜 ≥𝐵lb **then** 9: reject = false 10: **end if** 11: **end while** 12: **return** 𝑾op = {𝒘𝑜}𝑂𝑜=1 

## **4. Solving the Double-Up Problem** 

As mentioned earlier, we first tackle the double-up problem since our solution to this problem will help inform how we approach the top-heavy problem. We begin first by recalling some results from mean-variance optimization and in particular, the problem of maximizing the probability of exceeding a stochastic benchmark. 



9 

2018 Research Papers Competition Presented by: 



### **4.1. Mean Variance Optimization and Outperforming Stochastic Benchmarks** 

We consider<sup>9</sup> a one-period problem where at time 𝑡= 0, there are 𝑃 financial securities available to invest in. At time 𝑡= 1, the corresponding random return vector 𝝃= (𝜉1, … , 𝜉𝑃) is realized. Let 𝝁𝝃 and 𝜮𝝃 denote the mean return vector and variance-covariance matrix, respectively, of 𝝃. The goal is then to construct a portfolio 𝒘= (𝑤1, … , 𝑤𝑃) with random return 𝑅𝒘 = 𝒘<sup>T</sup> 𝝃 that maximizes the probability of exceeding a random benchmark 𝑟0. Mathematically, we wish to solve 



where 𝕎 includes the budget constraint 𝒘<sup>T</sup> 𝟏= 1 as well as any other linear constraints we wish to impose. We assume that 𝝃−𝑟0 has a multivariate normal distribution so that 



for some<sup>10</sup> 𝜇𝒘 and 𝜎𝒘<sup>2</sup> that depend on the portfolio 𝒘. Let 𝒘<sup>∗</sup> be the optimal solution to (5). Then, the problem in (5) amounts to solving 



where 𝛷(∙) denotes the standard normal CDF. The following result is adapted from Morton et al. [21] and follows from the representation in (6). 

**Proposition 4.1.** (i) _Suppose_ 𝜇𝒘 < 0 _for all_ 𝒘∈𝕎 _. Then,_ 



_(ii) Suppose_ 𝜇𝒘 ≥0 _for some_ 𝒘∈𝕎 _. Then,_ 



_so that_ 𝒘<sup>∗</sup> _is mean-variance efficient._ 

> 9 The material and results in this subsection follow Morton et al. [21] and they should be consulted for further details and related results. In this subsection, we will sometimes use the same notation from earlier sections to make the connections between the financial problem of this subsection and the DFS problem more apparent. 

> 10 If the benchmark 𝑟0 is deterministic, then 𝜇𝒘 ≔𝒘T𝝁𝝃 −𝑟0 and 𝜎𝒘2 ≔𝒘T𝜮𝝃𝒘. 



10 

2018 Research Papers Competition Presented by: 



Proposition 4.1 is useful because it allows us to solve the problem in (5) (or equivalently in (6)). In particular, we determine which of the two cases from the proposition applies. This can be done when 𝕎 is polyhedral by simply solving a linear program that maximizes 𝜇𝒘 over 𝒘∈𝕎. If the optimal is negative then we are in case (i); otherwise we are in case (ii). We then form a grid 𝛬 of possible 𝜆 values and for each 𝜆∈𝛬, we solve the appropriate quadratic optimization problem (defining 𝒘(𝜆)) from (7) or (8) and then choose the value of 𝜆 that yields the largest objective in (5) or (6). See Algorithm 2 in Section 4.2 below for when we apply these results to our double-up problem. 

### **4.2. The Double-Up Problem** 

Recall now the double-up problem as formulated in (1). We define 𝑌𝒘 ≔ 𝒘<sup>T</sup> 𝜹−𝐺<sup>(𝑟′)</sup> and assume<sup>11</sup> that 𝑌𝒘 ∼N(𝜇𝑌𝒘, 𝜎𝑌2𝒘) where 



where 𝜇𝐺(𝑟′) = E[𝐺<sup>(𝑟′)</sup> ], 𝜎𝐺2(𝑟′) = Var(𝐺<sup>(𝑟′)</sup> ) and 𝝈𝜹,𝐺(𝑟′) is a 𝑃 × 1 vector with 𝑝<sup>𝑡ℎ</sup> component equal to Cov(𝛿𝑝, 𝐺<sup>(𝑟′)</sup> ). The solution of our double-up problem now follows immediately from Proposition 4.1 and the following discussion. Our procedure is stated formally in Algorithm 2. Note that 𝒘<sup>∗</sup> in line 10 can be computed using the Monte-Carlo samples 𝜹 and 𝒘𝑜 that are inputs to the algorithm. Alternatively, 𝒘<sup>∗</sup> could also be computed using the normal approximation assumption. 

#### **Generating Monte-Carlo Samples** 

2 In order to execute Algorithm 2, we must first compute the inputs 𝜇𝐺(𝑟′), 𝜎𝐺(𝑟′), 𝝈𝜹,𝐺(𝑟′) as defined above. These quantities can be estimated off-line via Monte-Carlo simulation as they do not depend on our portfolio choice 𝒘. We simply note here that the Monte-Carlo can be performed efficiently<sup>12</sup> using results (see [7]) from the theory of order statistics. These results rely on letting 𝑂→∞ and so our Monte-Carlo algorithm is most suited for large DFS contests (which happen to be the contests of most interest anyway). Nonetheless, we can still use the Monte-Carlo algorithm as an approximation for medium-sized contests, and if 𝑂 is small, then we can simply simulate directly without relying on these results. 

#### **Solving the Binary Quadratic Program** 

The optimization problems in lines 3 and 7 of Algorithm 2 require the solution of binary quadratic programs (BQP’s). We solve them using Gurobi's [16] default BQP solver. In our experiments, all such problem instances were successfully solved to optimality with required computation time 

> 11 We justified the normal approximation for 𝑌𝒘 via Monte-Carlo simulation. Specifically, we generated many samples of 𝑌𝒘 corresponding to various portfolios 𝒘. These portfolios included 𝒘<sup>∗</sup> as well as highly ranked portfolios from DFS contests in the current NFL season. In each case, we found the distribution of 𝑌𝒘 to be unimodal and approximately symmetric about its mean. 

> 12 The specific details are described in Appendix A. 



11 

2018 Research Papers Competition Presented by: 



varying with 𝑃 (number of real-world players), 𝜆 and the contest structure (double-up, quintupleup or top-heavy). A typical BQP problem instance took anywhere from a fraction of a second to a few hundred seconds to solve on a shared high-performance computing (HPC) cluster. 

**Algorithm 2** Optimization Algorithm for the Double-Up Problem with a Single Entry 

**Require:** 𝕎, 𝛬, 𝝁𝜹, 𝜮𝜹, 𝜇𝐺(𝑟′), 𝜎𝐺2(𝑟′), 𝝈𝜹,𝐺(𝑟′) and Monte-Carlo samples of 𝜹 and 𝒘𝑜 

1: **if** ∃𝒘∈ 𝕎 with 𝜇𝑌𝒘 ≥0 **then** 

2: **for all** 𝜆∈𝛬 **do** 2 3: 𝒘𝜆 = argmax (𝜇𝑌𝒘 −𝜆𝜎𝑌𝒘) 𝒘∈𝕎,𝜇𝑌𝒘≥0 4: **end for** 5: **else** 6: **for all** 𝜆∈𝛬 **do** 7: 𝒘𝜆 = argmax𝒘∈𝕎 (𝜇𝑌𝒘 + 𝜆𝜎𝑌2𝒘) 8: **end for** 9: **end if** 10:  𝜆<sup>∗</sup> = argmax ℙ{𝑌𝒘𝜆 > 0} 𝜆∈𝛬 

11: **return** 𝒘𝜆<sup>∗</sup> 

### **4.3. The Double-Up Problem with Multiple Entries** 

We briefly consider now the case where we can submit a fixed but finite number of 𝑁> 1 entries to the double-up contest. In the case of a risk-neutral DFS player, it should be intuitively clear<sup>13</sup> that if 𝑂→∞ so that 𝑁/𝑂 →0, then the optimal strategy is a _replication_ strategy. In particular, the DFS player should solve for the 𝑁= 1 optimal portfolio and then submit 𝑁 copies of this portfolio to the contest. Even when 𝑂 is not large then we suspect the replication strategy may still be close to optimal. The key issue would be the probability of having a portfolio exactly at the cutoff 𝐺<sup>(𝑟′)</sup> between receiving and not receiving the cash payoff. 

Finally, we note that a risk-averse DFS player would never (ignoring certain pathological cases) want to use a replication strategy and would prefer instead a more diversified portfolio of entries. Such a diversified portfolio can easily be constructed using the heuristics we outline in Section 5.1 for the case of top-heavy contests. 

## **5. Solving the Top-Heavy Problem** 

> 13 Certainly we would need to impose some technical conditions on {𝒘𝑜}𝑂𝑜=1 to make this claim rigorous. We will not discuss such technical conditions, however, since top-heavy contests are our main focus in this paper and such a replication result does not hold for these contests. See Section 5 for further discussion on this issue. 



12 

2018 Research Papers Competition Presented by: 



We can now extend the analysis we developed for the double-up problem in Section 4 to tackle the more interesting top-heavy problem. We consider first the single-entry case where N = 1. In that case, the problem in (2) simplifies to solving 



′ T where 𝑟𝑑 = 𝑂+ 1 −𝑟𝑑𝑂. Following the development in Section 4.2, we can define 𝑌𝒘𝑑 ≔ 𝒘 𝜹− 𝐺<sup>(𝑟𝑑</sup> ′ ) and assume 𝑌𝒘𝑑 ∼N(𝜇𝑌𝒘𝑑, 𝜎𝑌2𝒘𝑑) with 





where 𝜇𝐺(𝑟𝑑′ ) = E [𝐺<sup>(𝑟𝑑</sup> ′ )], 𝜎𝐺2<sup>(𝑟𝑑</sup> ′ ) = Var (𝐺<sup>(𝑟𝑑</sup> ′ )) and 𝝈𝜹,𝐺(𝑟𝑑′ )is a 𝑃 × 1 vector with 𝑝<sup>𝑡ℎ</sup> component equal to Cov (𝛿𝑝, 𝐺<sup>(𝑟𝑑</sup> ′ )). We can now write (9) as 



Before proceeding, we need to make two additional assumptions, which we will state formally. 

**Assumption 5.1.** 𝜇𝑌𝒘𝒅 < 0 _for_ 𝑑= 1, … , 𝐷 _and for all_ 𝒘∈𝕎 _._ 

Assumption 5.1 can be interpreted as stating that, in expectation, the points total of our optimal portfolio will not be sufficient to achieve the minimum payout 𝑅𝐷. In option-pricing terminology, we are therefore assuming our optimal portfolio is “out-of-the-money”. This is a very reasonable assumption to make for top-heavy contests where it is often the case that only the top 20% or so of entries earn a cash payout. In numerical experiments, our model often predicts that our optimal portfolio will (in expectation) be at or around the 20<sup>𝑡ℎ</sup> percentile. The assumption therefore may break down if payoffs extend beyond the top 20% of entries. Nonetheless, the payoff sizes around the 20<sup>𝑡ℎ</sup> percentile are very small and almost negligible. Indeed within our model most of the expected P&L comes from the top few percentiles and 𝜇𝑌𝒘𝒅 < 0 is certainly true for these values of 𝑑. Finally, we note the well-known general tendency of models to over-estimate the performance of an optimally chosen quantity (in this case our portfolio). We therefore anticipate that our optimal portfolio will not quite achieve (in expectation) the 20<sup>𝑡ℎ</sup> percentile and may well be out of the money for all payoff percentiles as assumed in Assumption 5.1. 

Given Assumption 5.1, it follows that each of the arguments −𝜇𝑌𝒘𝒅/𝜎𝑌𝒘𝒅 to the normal CDF terms in (12) are _positive_ . Given the objective in (12) is to maximize, it is also clear that for a fixed value of 



13 

2018 Research Papers Competition Presented by: 



𝒘<sup>T</sup> 𝝁𝜹 in (10), we would like the standard deviation 𝜎𝑌𝒘𝒅 to be as large as possible. Unfortunately, the third term, 2𝒘<sup>T</sup> 𝝈𝜹,𝐺(𝑟𝑑′ ), on the r.h.s. of (11) suggests that 𝒘 impacts the variance by a quantity that depends on 𝑑. The following assumption enables us to circumvent this problem. 

′ ′ **Assumption 5.2.** 𝐶𝑜𝑣(𝛿𝑝, 𝐺<sup>(𝑟𝑑</sup> )) = 𝐶𝑜𝑣(𝛿𝑝, 𝐺(𝑟𝑑′)) _for all_ 𝑑, 𝑑′ = 1, … , 𝐷. 

Assumption 5.2 seems very reasonable based on our numerical experiments with real-world DFS top-heavy contests. In these contests, we found these covariance terms to be very close to each other for values of 𝑑 corresponding to the top 20 percentiles and in particular for the top few percentiles. We therefore proceed to take Assumption 5.2 as given. It is then clear from (11) that 2 the impact of 𝒘 on 𝜎𝑌𝒘𝑑 does not depend on 𝑑. 

Given the preceding arguments, it should be clear that for any fixed value of 𝒘<sup>T</sup> 𝝁𝜹, we would like to make 𝒘<sup>T</sup> 𝜮𝜹𝒘−2𝒘<sup>T</sup> 𝝈𝜹,𝐺(𝑟𝑑′ ) (the terms from (11) that depend on 𝒘) as large as possible. We are 

therefore in the situation of part (i) of Proposition 4.1 and we have a simple algorithm for solving the top-heavy problem. This is given in Algorithm 3 below where we omit the dependence on 𝑑 of those terms that are assumed (by Assumption 5.2) to not vary with 𝑑. 

**Algorithm 3** Optimization Algorithm for the Top-Heavy Problem with a Single Entry 

**Require:** 𝕎, 𝛬, 𝝁𝜹, 𝜮𝜹, 𝝈𝜹,𝐺(𝑟′) and Monte-Carlo samples of 𝜹 and 𝒘𝑜 

- 1: **for all** 𝜆∈𝛬 **do** 

2: 𝒘𝜆 = argmax𝒘∈𝕎 (𝒘<sup>T</sup> 𝝁𝜹 + 𝜆(𝒘<sup>T</sup> 𝜮𝜹𝒘−2𝒘<sup>T</sup> 𝝈𝜹,𝐺(𝑟′))) 

- 3: **end for** 

′ 𝐷 ) 4:  𝜆<sup>∗</sup> = argmax ∑𝑑=1(𝑅𝑑 −𝑅𝑑+1)ℙ {𝒘<sup>T</sup> 𝜹> 𝐺<sup>(𝑟𝑑</sup> (𝑾op, 𝜹)} 𝜆∈𝛬 

- 5: **return** 𝒘𝜆<sup>∗</sup> 

As with Algorithm 2, the 𝒘𝜆’s are computed by solving BQP’s and the optimal 𝒘<sup>∗</sup> from line 4 can then be determined via the Monte-Carlo samples. 

### **5.1. The Top-Heavy Problem with Multiple Entries** 

Consider now the more general top-heavy problem where we must submit 𝑁 entries or portfolios. We repeat again the problem formulation from Section 2.2: 



′ (𝑟) 𝑡ℎ 𝑂 𝑁 where 𝑟𝑑 = 𝑂+ 𝑁−𝑟𝑑𝑂, 𝐺−𝑖 is the 𝑟 order statistic of {𝐺𝑜}𝑜=1 ∪ {𝐹𝑗}𝑗=1 ∖𝐹𝑖 and 𝑾−𝑖 ≔𝑾∖𝒘𝑖. The first thing to note is that, unlike the double-up format, there is no reason to believe that a 



14 

2018 Research Papers Competition Presented by: 



portfolio replication strategy should ever be optimal here. To see this, consider the winner-takes-all contest where only the entry with the most fantasy points wins. This is clearly a special-case<sup>14</sup> of the top-heavy format. Under some mild assumptions, e.g. the probability of a winning tie being very small, it is clear that the goal is to maximize the probability of having a winning entry. This probability can only be increased by diversifying and so replication is (in general) strictly suboptimal. 

For more general top-heavy contests that are not winner-takes-all contests, it is not clear whether or not some form of replication should take place. For example, consider the case where 𝑁= 2 and we are extremely skilled relative to all of our opponents. If the contest pays out to the top 20% of entries say, and 𝑂 is very large, then it may well be the case that submitting the same optimal entry twice is the best strategy. In general, solving the multiple entry top-heavy problem is difficult and so we propose using a greedy approach to tackle it. In particular, we will follow<sup>15</sup> the greedy approach of Hunter et al. [18] and also impose constraints on our entries that ensure a diversified portfolio of entries. In particular, we: 

1. Solve for the optimal 𝑁= 1 entry. Call this entry 𝒘1∗. 

2. For 𝑖= 2, … , 𝑁, we again solve for the 𝑁= 1 problem but with  a new constraint set 𝕎𝑖 defined as 

   - 𝕎𝑖 ≔ 𝕎∪{𝒘T𝑖 𝒘∗𝑗 ≤𝛾  ∀𝑗= 1, … , 𝑖−1} 

where 𝛾 is a pre-specified parameter satisfying 𝛾≤𝐶. Let 𝒘∗𝑖 denote the optimal solution. 

Note that the effect of 𝛾 is to ensure that portfolio 𝑖 can not have more than 𝛾 players in common with each of the previous 𝑖−1 portfolios. We mention in passing that in our numerical results of Section 6, we found this diversification heuristic for top-heavy contests to have a higher expected P&L than the replication strategy, which simply submits 𝑁 copies of the optimal portfolio for the single-entry problem. (This, not surprisingly, was not the case for our double-up contests.) 

**Remark 5.1.** _While we have taken_ 𝑁 _as given up to this point, it is perhaps worth mentioning that one can always use this heuristic to determine an “optimal” value of_ 𝑁 _. Specifically, we can continue to increase_ 𝑁 _until the expected P&L contribution from the next entry (determined by our heuristic above) goes negative. We note that it is easy to estimate the P&L of any portfolio of entries via MonteCarlo simulation._ 

## **6. Numerical Experiments** 

> 14 The winner-takes-all contest can also be viewed as a pathological case of the double-up format where replication is definitely not an optimal strategy for the reasons outlined in this subsection. 

> 15 Hunter et al. [18] provide some performance guarantees in their setting for the greedy approach in the winner-takes all setting. Those guarantees would also apply here. 



15 

2018 Research Papers Competition Presented by: 



We participated in real-world DFS contests on FanDuel during the 2017-18 NFL season. As of writing, the season is still ongoing and so we present results for the first twelve weeks. Each week, we participated in three contests: top-heavy, quintuple-up and double-up. The cost per entry was $1 in top-heavy and $2 in both quintuple-up and double-up contests. The number of opponents 𝑂 was approximately 200,000, 10,000 and 30,000 for the three contests, respectively, with these numbers varying by around 10% from week-to-week. In the top-heavy contest, the payoff<sup>16</sup> for rank 1 was around $5,000, for rank 2 was around $2,500, declining quickly to around $100 for rank 30. The lowest winning rank was around 50,000, with a payoff of $2. 

We used two different models for each contest. The first model (which we used across all contests) is the _strategic_ model that we introduced in Section 4 for double-up / quintuple-up contests and in Section 5 for top-heavy contests. For all contests, we used the diversification heuristic<sup>17</sup> instead of the replication strategy for 𝑁> 1. The second model is a _benchmark_ model that does not model opponents and hence, is not strategic. For each model, we submitted 𝑁= 50, 25 and 10 entries to top-heavy, quintuple-up and double-up contests, respectively each week. 

### **6.1. Benchmark Models** 

Our two benchmark models do not model opponents and in fact, they (implicitly) assume the benchmarks 𝐺<sup>(𝑟′)</sup> or 𝐺<sup>(𝑟𝑑</sup> ′ ) are deterministic and simply maximize the expected points total in the objective. First, we describe the benchmark model for double-up and then, the benchmark model for top-heavy. 

#### **Benchmark Model 1** 

To optimize in the 𝑁= 1 case, our first benchmark model simply maximizes the expected points total subject to the feasibility constraints on the portfolio. The resulting optimization model is a binary program (BP): 



For 𝑁> 1 (which is the case in our numerical experiments), we employ the greedy heuristic discussed in Section 5.1 but suitably adapted for the case where we do not model opponents. We use this benchmark model for the double-up contest because, according to our calibrated model, we 

> 16 We note that there are other top-heavy contests with even more competitors and payoff structures that are even more ``top-heavy''. For example, a regular contest on FanDuel often has approximately 400,000 entries with a top payoff of $250,000 to $1,000,000, which declines quickly to a payoff of ≈$500 for the 50<sup>_th_</sup> rank. Top-heavy contests are therefore extremely popular and hence are our principal focus in this paper. 

> 17 This makes sense as previously discussed for top-heavy contests. The reason for doing so in the double-up / quintuple-up contests was simply to reduce the variance of P&L. This is discussed further in Section 6.3. 



16 

2018 Research Papers Competition Presented by: 



are comfortably in the case (ii) scenario of Proposition 4.1 where, other things being equal, we prefer less variance to more variance. 

#### **Benchmark Model 2** 

The second benchmark model is similar to the first and indeed the objective functions are identical. The only difference is that we add a stacking constraint to force the model to pick the QB and main WR<sup>18</sup> from the same team. We denote this constraint as “QB-WR”. Mathematically, the resulting BP for 𝑁= 1 is: 



Again for 𝑁> 1, we employ a suitably adapted version of the greedy heuristic from Section 5.1. As discussed in Section 3.2, the purpose of the stacking constraint is to increase the portfolio's variance. This is because we are invariably “out-of-the-money” in these contests as we noted in Section 5 and so variance is preferred all other things, i.e. expected number of points, being equal. We note this model is very similar to the model proposed by Hunter et al. [18] for hockey contests. They presented several variations of their model typically along the lines of including more stacking (or anti-stacking<sup>19</sup> ) constraints, e.g. choosing players from exactly 3 teams to increase portfolio variance. We note that we could easily construct and back-test other similar benchmark strategies as well but for the purposes of our experiments, the two benchmarks above seemed reasonable points of comparison. 

### **6.2. Parameters** 

Our models rely on the following four input parameters<sup>20</sup> : the expected fantasy points of the realworld players 𝝁𝜹, the corresponding variance-covariance matrix 𝜮𝜹, the stacking probability 𝑞 from Section 3.2 and the diversification parameter 𝛾 from Section 5.1. 

18 By “main” WR of a team, we refer to the WR with the highest 𝝁𝜹 value among all the WRs in the same team. 

> 19 An example of an anti-stacking constraint in hockey is that the goalie of team A cannot be selected if the attacker of team B was selected and teams A and B are playing each other in the series of games underlying the DFS contest in question. Such an anti-stacking constraint is also designed to increase variance by avoiding players whose fantasy points would naturally be negatively correlated. 

> 20 In addition to these four input parameters, we need the input features 𝑿 and the realized 𝒑 values for the Dirichlet regression. Such data is available on the internet. For example, the 𝒇 feature (point estimate of 𝒑) is available at the FantasyPros website and FanDuel contains the cost vector 𝒄 (before a contest starts) and the realized positional marginals 𝒑 (after a contest is over). We note that accessing the positional marginals data at FantasyPros required us to create an account and pay for a six-month subscription costing $65.94. 



17 

2018 Research Papers Competition Presented by: 



We obtain the estimate of 𝝁𝜹 from FantasyPros [12]. This estimate is specific to each week’s games and we normally obtained it a day before the NFL games were played. We decompose the variancecovariance matrix 𝜮𝜹 into the correlation matrix 𝝆𝜹 and the standard deviations of the individual players 𝝈𝜹 ∈ℝ<sup>𝑃</sup> . The estimate of 𝝆𝜹 is obtained from RotoViz [26] and 𝝈𝜹 is estimated using the realized 𝜹 values from the 2016-17 and the ongoing 2017-18 seasons. Note that 𝝆𝜹 does not change from week to week whereas 𝝈𝜹 is updated weekly using the realized 𝜹 from the previous week. 

For the stacking probability 𝑞, we first note that we expect it to be contest-specific as we anticipate more stacking to occur in top-heavy style contests where variance is relatively more important than in double-up contests. Accordingly, we empirically checked the proportion of opponents who stacked using data from the 2016-17 season for each contest-type. We then calibrated 𝑞 to ensure that our Dirichlet-multinomial model for generating opponents implied the same proportion (on average). We estimated 𝑞 to be 0.35, 0.25 and 0.20 for top-heavy, quintuple-up and double-up contests, respectively. Finally, we set<sup>21</sup> 𝛾= 6 for the strategic and benchmark models across all contests. 

### **6.3. Main Results** 

We now discuss the P&L-related results for the strategic and benchmark models across the three contest structures for the first twelve weeks of the FanDuel DFS contests in the ongoing 2017-18 NFL season. Figure 2 and Table 1 display the cumulative realized P&L for both models across the three contest structures during the season. The strategic portfolio has out-performed the benchmark portfolio since inception in the top-heavy series of contests. The strategic portfolio has earned a cumulative profit of $384.74, which is ≈2.5 times the realized P&L of the benchmark portfolio. Moreover, the maximum cumulative loss, i.e. the max shortfall, for the strategic portfolio is just $18.5. In addition, the small initial investment of $50 has been sufficient to fund the strategic portfolio throughout the twelve weeks. This suggests a profit of $384.74 on an initial investment of $50, i.e. a return of over 750% in just 12 weeks. In contrast, the benchmark portfolio needed more capital than the initial investment of $50. If we account for this additional required capital, then the benchmark portfolio has earned a return of less than 100% in 12 weeks. Note that given the socalled house-edge of approximately 15%, both models have performed considerably better than the average portfolio which would have lost ≈12 × 15% × 50 = $90 across the 12 weeks. 

With regards to the quintuple-up series, the strategic model was better until the end of week 6 but since then the benchmark portfolio has out-performed it. We note, however, that the current difference in the cumulative P&L between the two models is almost the same as the difference at the end of week 6, implying that one week is enough to flip the story. A similar situation applies to the double-up series. 

We believe the realized P&L to-date for each contest series is actually conservative and that superior performance (in expectation) could easily be attained. There are at least three reasons for this belief. First, we used off-the-shelf estimates of the input parameters 𝝁𝜹 and 𝜮𝜹, which are clearly vital to the optimization model. Moreover, we obtained the 𝝁𝜹 estimate a day before the 

> 21 We found this value of 𝛾 to produce a near maximum within-model expected P&L. 



18 

2018 Research Papers Competition Presented by: 



actual NFL games started and mostly ignored the developments in the last few hours preceding the games, which can be very important in football. For example, in week 7, the main RB of the Jacksonville Jaguars (Leonard Fournette) was questionable to play.  Accordingly, their second main RB (Chris Ivory) was expected to play more time on the field. However, our 𝝁𝜹 estimate did not reflect this information. Our estimate projected 17.27 and 6.78 fantasy points for Fournette and Ivory, respectively. Moreover, since FanDuel sets the price of the players a few days before the games take place, Fournette was priced at 9000 and Ivory at 5900. There was a clear benefit of leveraging this information as Fournette was over-priced and Ivory was under-priced. In fact, our opponents exploited this opportunity as around 60% of them (in double-up) picked Ivory. A proactive user would have updated his 𝝁𝜹 estimate following such news. In fact, the sharks do react to such last-minute information [23], meaning that we were at a disadvantage by not doing so. 







Figure 2: Cumulative realized dollar P&L for the strategic and benchmark models across the three contest structures for the first twelve weeks of the FanDuel DFS contests in the 2017-18 NFL season. 

Table 1: **Cumulative realized dollar P&L** for the strategic and benchmark models across the three contest structures for the first twelve weeks of the FanDuel DFS contests in the 2017-18 NFL season. We invested $50 per week per model in top-heavy series with each entry costing $1. In quintuple-up the numbers were $50 per week per model with each entry costing $2 and in double-up we invested $20 per week per model with each entry costing $2. (We did not participate in <u>the quintuple-up contest in week 1 due to logistical reasons.)</u> 

|**Week**|**Top- **|**heavy**|**Quintu**|**ple-up**|**Doub**|**le-up**|
|---|---|---|---|---|---|---|
||Strategic|Benchmark|Strategic|Benchmark|Strategic|Benchmark|
|1|25.5|−39.5|-|-|3.13|15.13|
|2|−18.5|−77|−50|−50|−16.87|−4.87|
|3|85.24|−97|30|−60|−8.87|3.13|
|4|61.74|12.5|80|20|11.13|15.13|
|5|15.74|−34.5|30|−30|−8.87|−4.87|
|6|−7.26|−52.5|30|−70|−16.87|−8.87|
|7|92.74|−6.5|−10|20|−36.87|−24.87|
|8|170.74|0.5|−10|20|−28.87|−24.87|
|9|290.74|32.5|40|110|−8.87|−4.87|
|10|437.74|−17.5|0|60|−8.87|−4.87|
|11|406.74|189.5|20|130|−8.87|7.13|
|12|384.74|154.5|−30|80|−20.87|−8.87|





19 

2018 Research Papers Competition Presented by: 



The second reason is simply a variance issue in that a large number of DFS contests (and certainly much greater than 12) will be required to fully establish the out-performance of the strategic model in general. In fact, we believe the variance of the cumulative P&L is particularly high for NFL DFS contests. There are several reasons for this. Certainly the individual performance of an NFL player in a given week will have quite a high variance due to the large roster size<sup>22</sup> as well as the relatively high probability of injury. This is in contrast to other DFS sports where there is considerably more certainty over the playing time of each athlete. To give but one example, in week 5 we witnessed a series of injuries that impacted many of our submitted portfolios (both strategic and benchmark). Devante Parker (Miami Dolphins) was injured in the first quarter but was picked by 56 of our entries. Charles Clay (Buffalo Bills) and Sterling Shepard (NY Giants) were injured before halftime, affecting 70 and 4 entries, respectively. Bilal Powell (NY Jets) and Travis Kelce (Kansas City Chiefs) left the field close to the halftime, impacting 44 and 25 entries, respectively. Furthermore, the NFL season consists of just 16 games per team whereas teams in sports such as basketball, ice hockey and baseball play 82, 82 and 162 games, respectively, per season. As a result, we believe the cumulative P&L from playing DFS contests over the course of an NFL season will have a very high variance relative to these other sports. 

The third reason applies specifically to the quintuple up contests and is quite an interesting case. In our strategic model for quintuple-up, there is a possibility of incorrectly minimizing portfolio variance when we should in fact be maximizing it (along with expected number of points of course). Proposition 4.1 leads us to try and increase variance if 𝜇𝒘 < 0 for all 𝒘∈𝕎 and to try and decrease variance otherwise. But 𝜇𝒘 must be estimated via Monte-Carlo and is of course also modeldependent. As such, if we estimate a value of 𝜇𝒘 ≈0, it is quite possible we will err and increase variance when we should decrease it and vice versa. We suspect this occurred on regular basis with the quintuple-up contests, where we often obtained an estimate of 𝜇𝒘 that was close to zero. We note that the benchmark portfolio is always long expected points and variance of points. This problem should be easy to fix by introducing a threshold value of 𝜇𝒘 (presumably greater than 0) below which we are led to increase variance. One could back-test to find a good choice of this threshold. 

Figure 3 displays the P&L distribution for the diversification strategy from Section 5.1 for both strategic and benchmark portfolios in week 10<sup>23</sup> contests. We note this P&L distribution is as determined by our model and therefore assumes the Gaussian model for NFL players and the Dirichlet-multinomial model for opponents portfolios. The strategic model dominates the benchmark model in terms of expected profit. In top-heavy, the expected profit of the strategic portfolio is over 5 times that of the benchmark portfolio. The gain is not as drastic in quintuple-up and double-up contests. The substantial gain in top-heavy seems to come from the fact that the 

> 22 There are more than 45 players on a roster but only 11 on the field at any one time. 

> 23 Other weeks have similar results as shown in Figure 5. 



20 

2018 Research Papers Competition Presented by: 



strategic portfolio has a considerably more mass in the right-tail. Note this leads to the higher standard deviation of the top-heavy strategic portfolio<sup>24</sup> . 







Figure 3: P&L distribution for the diversification strategy for the strategic and benchmark portfolios for week 10 contests of the 2017-18 NFL season. Recall 𝑵= 𝟓𝟎, 𝟐𝟓 and 𝟏𝟎 for top-heavy, quintuple-up and double-up, respectively. The three metrics at the top of each image are the expected P&L, the standard deviation of the P&L and the probability of loss, i.e. ℙ(P&L < 0). 







Figure 4: P&L distribution for the replication strategy for the strategic and benchmark portfolios for week 10 contests of the 2017-18 NFL season. Recall 𝑵= 𝟓𝟎, 𝟐𝟓 and 𝟏𝟎 for top-heavy, quintuple-up and double-up, respectively. The three metrics at the top of each image are the expected P&L, the standard deviation of the P&L and the probability of loss, i.e. ℙ(P&L < 0). 

Figure 4 is similar to Figure 3 except it is based upon using the replication strategy from Section 4.3 instead of the diversification strategy. We note the strategic model continues to have a higher 

> 24 The high standard deviation in the top-heavy strategic portfolio should be seen as a pro instead of a con, since it is mostly coming from the right-tail of the P&L distribution. 

21 



2018 Research Papers Competition Presented by: 



expected P&L than the benchmark model. The main observation here is that the expected P&L drops considerably when we go from the diversification heuristic to the replication strategy for topheavy. This is consistent with the winner-takes-all story we discussed in Section 5.1, where we argued that replication was in general clearly suboptimal. In contrast, the P&L increases for both quintuple-up and double-up when we employ the replication strategy. Again, this is consistent with our earlier argument in favor of replication for double-up style contests. In our numerical experiments, however, we used the diversification strategy for both double-up and quintuple-up contests. This was only because of the variance issue highlighted earlier and our desire to use a strategy, which had a considerably smaller standard deviation (while ceding only a small amount of expected P&L). As can be seen from Figures 3 and 4, the diversification strategy has (as expected) a smaller expected P&L as well as a smaller probability of loss. 

Figure 5 displays the realized and expected P&L’s.  For both strategic and benchmark models and all three contests, the expected profit is greater than the realized profit. This is perhaps not too surprising given the bias that results from optimizing within a model. In top-heavy, however, the realized P&L is within one standard deviation of the expected P&L although this is not the case for the quintuple- and double-up contests. As discussed above, we believe our realized results are conservative and that a more proactive user of these strategies who makes a more determined effort to estimate 𝝁𝜹 and 𝜮𝜹 and responds to relevant news breaking just before the games can do even better. Despite this potential for improvement, the strategic model has performed very well overall. The small loses from the double-up and quintuple-up contests have been comfortably offset by the gains in the top-heavy contests. As we noted earlier, the return on investment in top-heavy is over 750% for a twelve week period although we do acknowledge there is considerable variance in this number as evidenced by Figure 5(a). 







Figure 5: Predicted and realized cumulative P&L for the strategic and benchmark models across the three contest structures for the first twelve weeks of the FanDuel DFS contests in the 2017-18 NFL season. The realized cumulative P&L's are displayed as points 

## **7. The Value of Modeling Opponents and Insider Trading** 



22 

2018 Research Papers Competition Presented by: 



In unreported numerical simulations as well as the numerical results of Section 6, we found that modeling opponents' behavior can significantly increase the expected P&L from participating in DFS contests. But many interesting questions remain open and we briefly describe some of them here. 

1. How much value is there in modeling opponents? Clearly this is contest-dependent and we have seen in Section 6 that our framework, which explicitly models opponents, clearly does much better (in terms of expected P&L) than the benchmark models that do not consider opponents. But the value in modeling opponents also depends on how _accurately_ we model their behavior. On this latter point it would be of interest to consider: 

   - a. How much do we gain if we use a deterministic (𝒑QB, … , 𝒑D)? For example, in the NFL contests, we could set 𝒑 equal to the values predicted by the FantasyPros website. 

   - b. How much additional value is there if instead we assume (𝒑QB, … , 𝒑D) ∼ (Dir(𝜶QB), … , Dir(𝜶D)) as in Algorithm 1 but now 𝜶QB, … , 𝜶D are constant vectors and do not vary with the features 𝑿QB, … , 𝑿D as assumed in line 1 of the algorithm? 

   - c. Finally, how much additional value is there to be gained by assuming the model of Algorithm 1 where 𝜶QB, … , 𝜶D depend on the features 𝑿QB, … , 𝑿D? And just how well can we do if we could find a set of ``optimal'' features? 

2. A question that is somewhat dual to the first question concerns the issue of insider trading and the value of information. This question received considerable attention in 2015 [9, 10] when a DraftKings employee used data from DraftKings contests to enter a FanDuel DFS contest in the same week and win $350,000. Without addressing the specific nature of insider trading in that case, we can pose several questions: 

   - a. How much does the insider gain if he knows the entries of all contestants, i.e. 𝑾op? In that case, the only uncertainty in the system is the performance vector 𝜹 of the real-world players. (Note that the problem of computing an optimal portfolio given full knowledge of 𝑾op is straightforward in our framework.) 

   - b. How much does the insider gain if he only knows the true positional marginals 𝒑= (𝒑QB, … , 𝒑D) as opposed to knowing 𝑾op? 

We note the answers to the second question depend on how well the non-insider can predict opponents' behavior. For example, the more sophisticated the non-insider is, then the less value there is to having inside information. We are currently investigating these issues and will present our results in an extended version of this paper. 

## **8. Conclusions and Further Research** 

In this paper, we have developed a new framework for constructing portfolios for both double-up and top-heavy DFS contests. Our methodology explicitly accounts for the behavior of DFS opponents and leverages mean-variance theory (for the out-performance of stochastic benchmarks) to develop a tractable algorithm that requires solving a series of binary quadratic 



23 

2018 Research Papers Competition Presented by: 



programs. Following Hunter et al. [18], we also provide a tractable greedy heuristic for handling the multiple entry, i.e. 𝑁 > 1, case for top-heavy style contests. This is in contrast to the replication approach we advocate for double-up style contests. 

There are many potential directions for future research. First, the numerical results of Section 6 are preliminary as they are based on the ongoing 2017-18 NFL season. They must therefore be updated at the end of the season. The data we are currently gathering for these numerical experiments can be used to back-test other benchmark strategies as well as refining our own preferred strategies. For example, in Section 6.3, we discussed the possibility our strategic model might be incorrectly minimizing portfolio variance in quintuple-up. A more robust approach is therefore called for and it would be interesting to optimize over the threshold value of 𝜇𝒘 below which we are led to increase variance. 

While NFL contests are among the most popular DFS contests, the season is quite short with only 17 rounds of games. Moreover, as mentioned in Section 6.3, the individual performance of an NFL player in a given week has quite a high variance, potentially causing the cumulative P&L in football DFS contests to be high relative to other sports such as basketball, ice hockey and baseball. For these reasons and others, it would be interesting to apply our modeling framework to DFS contests in these other sports. It would also be interesting to use domain knowledge of these other sports to actively update estimates of 𝝁𝜹 and 𝜮𝜹 as the round of games approaches. This is something we did not do in the current NFL season. Indeed we recorded many instances when it would have been possible to avoid certain players in our DFS entries had we used up-to-date information that was available before the games in question and before our entries needed to be submitted. As a result, we believe the net positive P&L achieved by our models is very encouraging and can easily be improved (in expectation) by more active monitoring of the players. 

It would also be interesting to further develop our modeling and estimation approach for a random opponent's portfolio 𝒘𝑜. We assumed in Section 3 that we had sufficient data to estimate the positional marginals of 𝒘𝑜. We would like to explore other features that might be useful in the Dirichlet regression to better estimate these marginals. We would also like to explore other approaches to splicing these marginals together to construct 𝒘𝑜. (We only discussed splicing them together independently or using a somewhat ad-hoc stacking approach but to do so more systematically we would need to estimate the relevant _copula_ . It is not clear, however, whether we could ever obtain a rich enough data-set to estimate such a copula accurately.) 

Other directions for future research include a more systematic study to estimate the value of insider information. We have already done some (unreported) work on this problem and intend to develop it further. For example, how much gain in expected P&L is there if we have full access to all the positional marginals in 𝑾op. How much if we know 𝑾op entirely? And to what extent can these gains be offset by superior modeling and estimation of 𝑾op? Certainly our Dirichlet regression approach has reduced the value of this information but interesting questions still remain. 

Finally, we briefly mention the area of mean-field games. In our modeling of opponents, we did not assume they were strategic although we did note how some strategic modeling along the lines of 



24 

2018 Research Papers Competition Presented by: 



stacking to increase portfolio variance could be accommodated. If we allowed some opponents to be fully strategic, then we are in a game-theoretic setting. Such games would most likely be impossible to solve. Even refinements such as mean-field games (where we let 𝑂→∞ in some appropriate fashion) would still likely be intractable, especially given the discreteness of the problem (binary decision variables) and portfolio constraints. But it may be possible to solve very stylized versions of these DFS games where it is possible to purchase or sell short fractional amounts of players. There has been some success in solving mean-field games in the literature on parimutuel betting [3] in horse racing and it may be possible to do likewise here for very stylized versions of DFS contests. 

We are pursuing some of these directions in current research. 



25 

2018 Research Papers Competition Presented by: 



## **References** 

1. Anderton, K. 2016. FanDuel And DraftKings Are Dominating The Daily Fantasy Sports Market. https://www.forbes.com/sites/kevinanderton/2016/11/30/fanduel-anddraftkings-are-dominating-the-daily-fantasy-sports-market-infographic/#2979acb87c4f. [Accessed: 26-Feb-2017]. 

2. Bales, J. 2016. Pairing a QB with his Receiver(s). https://rotogrinders.com/articles/pairing-a-qb-with-his-receiver-s-481544. [Accessed: 26Feb-2017]. 

3. Bayraktar, E. and A. Munk. 2017. High-Roller Impact: A Large Generalized Game Model of Parimutuel Wagering. _Market Microstructure and Liquidity_ . 3(01) 1750006. 

4. Becker, A. and X.A. Sun. 2016. An analytical approach for fantasy football draft and lineup management. _Journal of Quantitative Analysis in Sports_ . 12(1) 17-30. 

5. Bergman, D. and J. Imbrogno. 2017. Surviving a National Football League Survivor Pool. _Operations Research_ . 65(5) 1343-1354. 

6. Clair, B. and D. Letscher. 2007. Optimal strategies for sports betting pools. _Operations Research_ . 55(6) 1163-1177. 

7. David, H.A. and H.N. Nagaraja. 1981. _Order statistics_ . Wiley Online Library. 

8. Davis, A. 2017. Data-Driven Portfolios Power ‘Home-Run’ Exits in MIT Study. https://www.wsj.com/articles/data-driven-portfolios-power-home-run-exits-in-mit-study1502105402. [Accessed: 1-Dec-2017]. 

9. Drape, J. and J. Williams. 2015. In Fantasy Sports, Signs of Insiders Edge. https://www.nytimes.com/2015/10/12/sports/fantasy-sports-draftkings-fanduel-insidersedge-football.html. [Accessed: 26-Feb-2017]. 

10. Drape, J. and J. Williams. 2015. Scandal Erupts in Unregulated World of Fantasy Sports. https://www.nytimes.com/2015/10/06/sports/fanduel-draftkings-fantasy-employees-betrivals.html. [Accessed: 26-Feb-2017]. 

11. FanDuel. 2016. Rules & Scoring. https://www.fanduel.com/rules. [Accessed: 26-Feb-2017]. 

12. FantasyPros. 2017. https://www.fantasypros.com. [Accessed: 30-Aug-2017]. 

13. Fry, M.J., A.W. Lundberg, and J.W. Ohlmann. 2007. A player selection heuristic for a sports league draft. _Journal of Quantitative Analysis in Sports_ . 3(2). 



26 

2018 Research Papers Competition Presented by: 



14. FSTA. 2015. Industry demographics. http://fsta.org/research/industry-demographics/. [Accessed: 26-Feb-2017]. 

15. Gibbs, J. 2017. Week 1 FanDuel NFL Tournament Pivots. https://www.numberfire.com/nfl/lists/16195/week-1-fanduel-nfl-tournament-pivots. [Accessed: 1-Dec-2017]. 

16. Gurobi Optimization, Inc. 2016. Gurobi Optimizer Reference Manual. http://www.gurobi.com. 

17. Harwell, D. 2015. Why you (probably) won’t win money playing DraftKings, FanDuel. http://www.dailyherald.com/article/20151012/business/151019683/. [Accessed: 26-July2016]. 

18. Hunter, D.S., J.P. Vielma, and T. Zaman. 2016. Picking winners using integer programming. _arXiv preprint arXiv:1604.01455_ . 

19. Kaplan, E.H. and S.J. Garstka. 2001. March madness and the office pool. _Management Science_ . 47(3) 369-382. 

20. Kolodny, L. 2015. Fantasy Sports Create Billion-Dollar Startups. https://www.wsj.com/articles/fantasy-sports-create-billion-dollar-startups-1436846402. [Accessed: 26-Feb-2017]. 

21. Morton, D.P., E. Popova, I. Popova, M. Zhong. 2003. Optimizing benchmark-based utility functions. _Bulletin of the Czech Econometric Society_ . 10(18). 

22. Mulshine, M. 2015. How one man made hundreds of thousands of dollars playing daily fantasy sports. http://www.businessinsider.com/draft-kings-jonathan-bales-a-day-in-thelife-2015-10. [Accessed: 26-Feb-2017]. 

23. Nickish, K. 2015. Meet A Bostonian Who's Made $3 Million This Year Playing Daily Fantasy Sports. http://www.wbur.org/news/2015/11/23/dfs-power-player-profile. [Accessed: 26-Feb-2017]. 

24. O’Keeffe, K. 2015. Daily Fantasy-Sports Operators Await Reality Check. https://www.wsj.com/articles/daily-fantasy-sports-operators-await-reality-check1441835630. [Accessed: 26-Feb-2017]. 

25. Pramuk, J. 2015. Former pro poker player makes a living on fantasy sports. https://www.cnbc.com/2015/10/06/former-pro-poker-player-makes-a-living-on-fantasysports.html. [Accessed: 26-Feb-2017]. 

26. RotoViz. 2017. http://rotoviz.com. [Accessed: 30-Aug-2017]. 

27. Stan Development Team. 2017. _RStan: the R interface to Stan_ . R package version 2.16.2. http://mc-stan.org. 



27 

2018 Research Papers Competition Presented by: 



28. Wong, K. 2015. The Fantasy Sports Industry, by the Numbers. http://www.nbcnews.com/business/business-news/fantasy-sports-industry-numbersn439536. [Accessed: 26-Feb-2017]. 

29. Woodward, C. 2015. Top fantasy sports player uses software, analytics to reap millions. https://www.bostonglobe.com/business/2015/12/23/from-boston-penthouse-world-bestfantasy-player-plunges-into-startup-world/QHNpLh0O3QMyUDqTd4t27N/story.html. [Accessed: 26-Feb-2017]. 

30. Woodward, C. 2016. DraftKings, FanDuel collected $3b in entry fees last year, analyst says. https://www.bostonglobe.com/business/2016/02/29/fantasy-sports-industry-hitsamid-legal-questions-analyst-says/NKw364kiLjv8XcD54vRr4H/story.html. [Accessed: 26Feb-2017]. 



28 

2018 Research Papers Competition Presented by: 



## **A. Appendix: Efficient Sampling of Order Statistic Moments** 

2 In order to execute Algorithms 2 and 3, we must first estimate the inputs 𝜇𝐺(𝑟′), 𝜎𝐺(𝑟′) and 𝝈𝜹,𝐺(𝑟′) . These quantities can be estimated off-line via Monte-Carlo simulation as they do not depend on our portfolio choice 𝒘. Here, we describe how the Monte-Carlo can be performed efficiently using results from the theory of order statistics assuming 𝑂 is large. Recalling 𝐺𝑜 = 𝒘𝑜<sup>T</sup> 𝜹 is the fantasy points score of the 𝑜<sup>𝑡ℎ</sup> opponent, we first note the 𝐺𝑜's for 𝑜= 1, … , 𝑂 are IID given (𝜹, 𝒑), where 𝒑 denotes the multinomial probability vectors (for the positional marginals) from Section 3. This suggests the following algorithm for obtaining independent samples of 𝜹 and 𝐺<sup>(𝑟′)</sup> : 

1. Generate 𝜹 ~ N(𝝁𝜹, 𝜮𝜹) and (𝒑, 𝑾op) using Algorithm 1 (or the stacking variant of it) where 𝑂 

𝒑≔(𝒑QB, … , 𝒑D) and 𝑾op = {𝒘𝑜}𝑜=1. 

2. Compute 𝐺𝑜 = 𝒘𝑜<sup>T</sup> 𝜹 for 𝑜= 1, … , 𝑂. 

3. Order the 𝐺𝑜's. 

4. Return (𝜹, 𝐺<sup>(𝑟′)</sup> ). 

We note other algorithms are also available. For example, a standard result on order statistics yields 



where 𝐹𝐺(𝑟′)|(𝜹,𝒑) and 𝐹𝐺|(𝜹,𝒑) denote the CDFs of 𝐺<sup>(𝑟′)</sup> and a random opponent 𝐺𝑜, respectively, given (𝜹, 𝒑). Instead of generating 𝑾op and the 𝐺𝑜's, we could use the inverse transform approach and (16) to generate 𝐺<sup>(𝑟′)</sup> directly. Unfortunately, both algorithms are quite computationally 2 expensive since we will need many samples of (𝜹, 𝐺<sup>(𝑟′)</sup> ) to estimate 𝜇𝐺(𝑟′), 𝜎𝐺(𝑟′) and 𝝈𝜹,𝐺(𝑟′) . Moreover, we would also need to estimate 𝐹𝐺|(𝜹,𝒑) and so to do this, many samples from 𝐺|(𝜹, 𝒑) would be required for each value of (𝜹, 𝒑). 

We can circumvent these problems when 𝑂 is large (the typical case of interest) by noting<sup>25</sup> that (see [7]) 



𝑝 where → denotes convergence in probability. Therefore in the limit of large 𝑂, there is no uncertainty given (𝜹, 𝒑) and so we can simply set 𝐺<sup>(𝑟′)</sup> = 𝐹𝐺|(𝜹,𝒑)−1 ~~(~~ 𝑟𝑂<sup>′</sup> ). Of course, we still need to estimate 𝐹𝐺|(𝜹,𝒑) and so, many samples of 𝐺|(𝜹, 𝒑) would be required. The algorithm therefore proceeds as: 

> 25 In fact the result states that 𝐺<sup>(𝑟′)</sup> |(𝜹, 𝒑) is normal with mean 𝐹𝐺|(𝜹,𝒑)−1 ~~(~~ 𝑟𝑂<sup>′</sup> ) and a variance that vanishes as 𝑂→∞. 



2018 Research Papers Competition Presented by: 

29 



1. Generate 𝜹 ~ N(𝝁𝜹, 𝜮𝜹) and (𝒑, 𝑾op) using Algorithm 1 (or the stacking variant of it) where 𝑂 

𝒑≔(𝒑QB, … , 𝒑D) and 𝑾op = {𝒘𝑜}𝑜=1. 

2. Compute 𝐺𝑜 = 𝒘𝑜<sup>T</sup> 𝜹 for 𝑜= 1, … , 𝑂. 

3. Use the 𝐺’s to construct 𝐹̂𝐺|(𝜹,𝒑)(∙). 

4. Set 𝐺<sup>(𝑟′)</sup> = 𝐹̂−1 𝑟<sup>′</sup> . 𝐺|(𝜹,𝒑) ~~(~~ 𝑂 ) 

5. Return (𝜹, 𝐺<sup>(𝑟′)</sup> ). 

We note that the value of 𝑂 is no longer assumed to be the number of DFS competitors (which is assumed to be infinite here) but instead is simply set large enough so that we can estimate 𝐹𝐺|(𝜹,𝒑) sufficiently accurately. 



2018 Research Papers Competition Presented by: 

30 


