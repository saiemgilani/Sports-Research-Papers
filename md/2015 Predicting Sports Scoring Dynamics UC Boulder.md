<!-- source: 2015 Predicting Sports Scoring Dynamics UC Boulder.pdf -->

# **Predicting sports scoring dynamics with restoration and anti-persistence** 

Leto Peel<sup>1,</sup><sup>_∗_</sup> and Aaron Clauset<sup>1, 2, 3,</sup><sup>_†_</sup> 

> 1 _Department of Computer Science, University of Colorado, Boulder, CO 80309_ 

> 2 _BioFrontiers Institute, University of Colorado, Boulder, CO 80303_ 

> 3 _Santa Fe Institute, 1399 Hyde Park Rd., Santa Fe, NM 87501_ 

Professional team sports provide an excellent domain for studying the dynamics of social competitions. These games are constructed with simple, well-defined rules and payoffs that admit a high-dimensional set of possible actions and nontrivial scoring dynamics. The resulting gameplay and efforts to predict its evolution are the object of great interest to both sports professionals and enthusiasts. In this paper, we consider two online prediction problems for team sports: given a partially observed game _Who will score next?_ and ultimately _Who will win?_ We present novel interpretable generative models of within-game scoring that allow for dependence on lead size ( _restoration_ ) and on the last team to score ( _anti-persistence_ ). We then apply these models to comprehensive withingame scoring data for four sports leagues over a ten year period. By assessing these models’ relative goodness-of-fit we shed new light on the underlying mechanisms driving the observed scoring dynamics of each sport. Furthermore, in both predictive tasks, the performance of our models consistently outperforms baselines models, and our models make quantitative assessments of the latent team skill, over time. 

## **I. INTRODUCTION** 

Competition in social systems is a natural and pervasive mechanism for improving performance and distributing limited resources. The quantitative study of such competitions can improve our ability to predict the outcomes associated with specific strategies and the strategic choices that competitors may make. However, most real competitions take place in complex and evolving environments [15, 26], which makes them difficult to study. Professional team sports, with their well defined and consistently enforced rules, provide a controlled setting for the study of competition dynamics [14, 27, 29] and have previously been used as model systems for studying business decision making and human behavioral biases [28, 34]. The recent trend toward recording comprehensive and detailed data on the events within particular games provides us with new opportunities to study, model, and predict the dynamics of these games. The results of these studies promise to shed new light on a wide variety of existing competitive social systems, and enhance work on designing new ones, both offline and online. 

Here, we examine the time series of scoring events in all league games across four different team sports over a period of ten years. We construct and test probabilistic models for two online predictive tasks: given a partially observed game _Who will score next?_ and ultimately _Who will win?_ We then use these models to investigate the predictiveness of the dynamical phenomena of _restoration_ and _anti-persistence_ , which are defined below. 

The events within a particular game can be effectively modeled as the interaction of skill and chance. Inferring skill from a series of competitions has a long history of 

> _∗_ leto.peel@colorado.edu 

> _†_ aaron.clauset@colorado.edu 

study, both for individuals [11, 17] and for teams [20, 35]. However, this past work has typically only considered the final outcome of games, in terms of either a win or loss, or the final point difference. Here, we focus on modeling the specific pattern of scoring events within an individual game. 

The role of chance also has a long history of study, typically focusing on the question of whether one success increases the likelihood of subsequent success. This idea can be formalized at different levels, e.g., success by individual players within a game [2, 16, 39], or a team’s success across multiple games [1, 32, 37]. Here, for the first time, we focus on a different level: success by a whole team within a game. 

A simple starting point for such models is the basic idea of many skill ranking systems [6, 11], which model game outcomes as random variables dependent on the competing teams’ skills. We extend this idea to consider the point-scoring events within a game to be a sequence of independent contests. Past work supports this approach, as some studies have found a lack of dependence between an individual scoring and their ability to score subsequent points [16, 39], or between a team winning and their chance to win future games [32, 37]. On the other hand, there is also evidence of non-independence, e.g., the probability of scoring itself can vary with the clock time within a game or with the size of the lead [14, 26, 27]. To investigate the degree to which non-independence governs scoring probabilities, we construct a sequence of more complex models that allow specific aspects of a game’s current state to influence scoring rates, e.g., the team that scored last and the lead size. 

In many sports, including American football and basketball, a simple source of non-independence is a forced change in ball possession after each scoring event, putting the scoring team at a disadvantage. This can result in a phenomenon called _anti-persistence_ , in which a score by one team is more likely to be followed by a score by their 

2 

opponent [14]. 

Another potential source of non-independence is the size of the lead itself. Past work has shown that the observed probability of scoring next can vary with lead size [14, 27]. A negative dependence may be the result of strategy, e.g., a team using its best players when it falls behind and substituting them out when they are ahead. Such strategies have a _restorative_ effect on the lead size, serving to pull the size of the lead back toward zero. Conversely, anti-restoration or momentum occurs when the leading team has a higher chance of scoring again, perhaps by improving their control over the playing field or by learning from gameplay how to better exploit the weaknesses of the opposing team. 

In this paper, we develop probabilistic generative models around these ideas to explore and predict the evolution of point scoring over the course of a game. We use these models to deduce the impact of chance, strategy, and the rules of the game itself, and to test two simple hypotheses: 

1. the probability of scoring _does not_ depend on the current state of the game (team skill alone matters). 

2. the probability of scoring _does_ depend on the current game state (as well as team skill). 

Our probabilistic models encode specific instances of these assumptions and we assess their accuracy under two online predictive tasks. We present novel predictive models that can not only predict the outcome of a game, but also provide better predictions over baseline models about the sequence of scoring events. 

## **II. RELATED WORK** 

Our work addresses two novel prediction problems for predicting _Who will score next?_ and _Who will win?_ , using only the sequence of scoring events that have already occured during the game. In the following we outline related work to each of these questions in turn. 

Essential to answering the question _Who will score next?_ is understanding the underlying mechanisms of scoring dynamics. The study of competitive team sports has a rich history spanning a broad selection of features including the timing of scoring events [7, 12, 14, 21, 27, 36, 39], long-range correlations in scoring [30], the role of timeouts [31], the identification of safe leads [8], and the impact of spatial positioning and playing field design [5, 26, 40]. The most relevant of these studies focuses on the analysis of individual player “momentum” or “hot-hands” [2, 16, 39] and on team winning streaks [1, 16, 32, 37, 39]. Here, we bring together these two ideas by considering the notion of momentum, or its reverse “restoration”, at the team level. Although some analysis has previously been undertaken in this direction [14], we go further to provide the first predictive models that answer the question: _Who will score next?_ 

The foundations of our approach lie in the field of skill modeling and team ranking [6, 11], which originated in the mid-20th century. Work in this area includes the ranking of individuals [9, 11, 17], teams [18, 32, 35], or both [20, 22]. These models have been applied to a wide range of competitive events, including baseball [32], chess [9, 11, 17], American football [18, 35], association football (soccer) [23], and tennis [17]. More recently, they have been adapted to matchmaking problems in online games [20] and to calibrating reviewer scores in computer science conferences [13]. 

Our work is the first to use skill ranking models to predict _Who will win?_ by predicting the sequence of scoring events within a game. Skill ranking models have previously been applied to predicting game outcomes but only based on the final outcome of the game, either in terms of the win/loss result or the final point difference. These past approaches thus cannot update their prediction as the game unfolds, while our models can. We train on a history of scoring event sequences so that we may predict _Who will win?_ in an online fashion. Some commercial online sports betting systems exist that make similar online predictions, but these systems are proprietary and closed, which precludes a scientific evaluation or comparison with our models. They are not considered hereafter. 

## **III. SPORTS DATASETS** 

We use scoring event data<sup>1</sup> from four team sports: college-level American football (CFB, 10 seasons; 20002009), professional American football (NFL, 10 seasons; 2000-2009), hockey (NHL, 9 seasons; 2000-2003, 20052009)<sup>2</sup> and basketball (NBA, 9 seasons; 2002-2010). Each dataset consists of the set of scoring events for each game played in the season. It includes the time the event was scored, the team and player that scored, and its point value. Table I gives a summary of these data including the number of teams, games, and individual scoring events. In our analysis and modeling, we discard the timestamps of the events and instead consider only the order in which events appear within a game. 

## **A. Preprocessing** 

We extract from the raw event data two sequences to represent each game: a _point sequence φ_ , where _φi_ is the point value of scoring event _i_ in the game, and a _team sequence ψ_ , where _ψi ∈{r, b}_ is the identity of the team that won those points. If there are _Nt_ events in game 

- 1 Data provided by STATS LLC, copyright 2015 

- 2 The entire 2004 NHL season was canceled due to an extensive lockout over a dispute about player salary caps [33]. 

3 

TABLE I. Summary of our sports data for multiple seasons across four team competitive sports. 

|sport|abbrv.|seasons|teams|numb<br>total|er of games<br>preprocessed|number of <br>total|scoring events<br>preprocessed|mean events<br>(preprocessed)|
|---|---|---|---|---|---|---|---|---|
|Football (college)|CFB|10, 2000–2009|461|14,588|13,689|190,337|117,752|8.60|
|Football (pro)|NFL|10, 2000–2009|32|2,645|2,561|32,800|20,115|7.85|
|Basketball (pro)|NBA|9, 2002–2010|30|11,744|11,744|1,301,408|1,096,179|93.34|
|Hockey (pro)|NHL|9, 2000–2009|30|11,813|10,259|65,085|59,227|5.77|



_t_ , then the corresponding _φ_ and _ψ_ each contain _Nt_ elements, and the lead size at event _i_ is 



for team labels _r_ and _b_ (arbitrarily chosen), where _δ_ ( _., ._ ) is the Kronecker delta function and by convention we compute _L_ from team _r_ ’s perspective. 

We begin by removing some games and scoring events. We remove any events that occur during regulation overtime (0.88% of all events), because these events follow different scoring processes than events in regular game time [27]. Additionally, any games in which only one team scored are removed (6.24% of all games), as the raw data do not indicate the identity of the non-scoring team. 

Under certain game conditions, multiple scoring events, potentially by different teams, can occur at the same game clock time. For example, in American football, the clock is stopped after a touchdown is scored but the scoring team gets a chance to score a conversion. If the conversion is unsuccessful, occasionally the opposing team gains control and scores points before the clock is restarted. Similarly, in basketball, the clock is stopped during free throws after a foul, after which the ball is inbounded (thrown in). If the ball is inbounded close to the other basket, it is possible to score before a second has elapsed on the clock. In these cases, the ordering of these events is ambiguous. 

Removing these events would alter the running lead size, which is one of the game states of interest. Instead, we merge simultaneous events into a single scoring play that removes the ordering ambiguity while preserving the correct score. If one team scores two simultaneous events _i_ and _i_ +1, we merge their values, setting _φi_ = _φi_ + _φi_ +1, and removing event _i_ + 1 from both sequences. If two teams score simultaneously, we merge their values with that of the immediately preceding event in a way that preserves the running lead. Specifically, we set _φi−_ 1 = _φi−_ 1 _± |φi − φi_ +1 _|_ , where the sign is consistent with the previous assignment of _r_ and _b_ labels to teams, and then remove events _i_ and _i_ + 1 from both sequences. 

## **B. Scoring and lead size** 

We use these point and team sequences to make an initial investigation of our hypotheses. If the scoring dy- 



<!-- Start of picture text -->
CFB NBA<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>−50 0 50 −100 −50 0 50 100<br>NFL NHL<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>−60−40−20 0 20 40 60 −10 −5 0 5 10<br>lead size lead size<br>p(score | lead)<br>p(score | lead)<br><!-- End of picture text -->

FIG. 1. Probability that a team scores next as a function of its lead size, for the observed ( _yellow_ ) and simulated ( _black_ ) patterns, each with a linear least squares fit line. The simulated scoring sequence assumes that the probability of scoring is independent of the game’s state. 

namics are truly independent of the game’s state, these dynamics will be indistinguishable from an independent Bernoulli process, in which each Bernoulli trial represents a scoring event. We evaluate this model by calculating the empirical probability that a team will score the next event as a function of the current lead size _L_ . Recall that we compute _L_ from the perspective of team _r_ ; thus, if _r_ is leading, then _L_ is positive, while if _r_ is trailing, then _L_ is negative (and vice versa for _b_ ). This function is thus rotationally symmetric about a lead of _L_ = 0, where neither team leads, and has the mathematical form of _P_ ( _ψi_ = _r | Li−_ 1) = 1 _− P_ ( _ψi_ = _b | −Li−_ 1). 

We compare the empirical scoring function to one calculated from synthetic team sequences generated according to an independent Bernoulli process, in which we flip a biased coin to determine which team wins each scoring event. The coin’s bias is determined by the proportion of scoring events each team wins in that particular game, _N_ <u>1</u> � _Ni_ =1<sup>_δ_(</sup><sup>_ψi, r_)(orfor</sup><sup>_b_).Inthissimulation,eventsare</sup> thus independent of the game state (hypothesis 1). We also compute a least-squares regression line for the empirical and for the synthetic data, in which each point is given weight proportional to the number of times the corresponding lead size was observed. 

All of the resulting gradients relating scoring probabil- 

4 

ity to lead size are nonzero (Fig. 1), and each Bernoulli process produces a positive gradient. This pattern simply reflects the empirical distribution of biases used to simulate the ensemble of games, with a more positive slope reflecting broader variance in these biases. The variance in the estimated scoring probability increases with lead size simply because progressively fewer games produce leads of that magnitude. 

Comparing the observed and simulated scoring functions (Fig. 1), we observe a clear contradiction. The gradient and, in particular for NBA, the range of lead sizes generated by the Bernoulli process disagree strongly with those properties observed in the empirical data. These results suggest that the probability of scoring does indeed depend, somehow, on the game state (hypothesis 2). In subsequent sections, we investigate this dependence using sophisticated probabilistic models to determine how the probability of scoring depends on game state. 

## **IV. WHERE STANDARD TESTS FAIL** 

To determine whether scoring events are independent, we now apply a suite of statistical randomization tests, which compare observed sequences to random sequences with similar properties. Specifically, we employ the 

- serial test ( _non-uniformity_ ), 

- Wald-Wolfowitz runs test ( _anti-restoration_ ), and 

- autocorrelation test ( _persistence/anti-persistence_ ), 

where for each the null hypothesis is that the team sequence _ψ_ is simply a random sequence. 

The serial test [25] examines bigram frequencies in a sequence and compares them to their expected frequencies under a uniformly random sequence. For a team sequence with _N_ elements, the observed fractions of bigrams _{rr, rb, br, bb}_ are compared to their expectations of _N/_ 4. This test can identify the existence of a bias within each game, i.e., if one team is systematically more likely to score than another. 

The Wald-Wolfowitz runs test [38] examines the observed number of runs in a sequence, i.e., substrings of _ψ_ for which each element is the same (either _r_ or _b_ ), which allows us to identify either positive momentum or antirestorative effects in within-game scoring. We reject the null hypothesis that _ψ_ is random if the observed number of runs is significantly below its expected value. Previously, this test has been used to detect winning streaks in sequences of games [37]. 

The autocorrelation test measures the correlation of a sequence with itself, shifted by one element, which allows us to identify periodic dynamics that occur as a result of anti-persistence. Here, we reject the null hypothesis that _ψ_ contains no dependence between values if the autocorrelation is significantly higher or lower than zero. 

We apply each of these three tests to each of our four data sets, and compare the results against a false positive 



<!-- Start of picture text -->
0.2 0<br>0.1 5 CFB<br>NBA<br>0.1 0<br>NFL<br>0.0 5 NHL<br>0.0 0<br>0 20 40 60 80 100 120 140<br>number of scoring events<br>1.00. 2 CFB 1. 0 NBA<br>0. 1<br>0.80.'00 0 '01 '02 '03 '04 '05 '06 '07 '08 '09 0. 8<br>0.60. 2 NFL 0. 6<br>0. 1<br>0.40. 0 0. 4 Serial Test<br>'00 '01 '02 '03 '04 '05 '06 '07 '08 '09 Wald-Wolfowitz<br>0.20. 2 NHL 0. 2 Auto-correlation<br>0. 1<br>0.00.'00 0 '01 '02 '03 '05 '06 '07 '08 '09 0.'02 0 '03 '04 '05 '06 '07 '08 '09 '10<br>season season<br>probability<br>proportion of games<br><!-- End of picture text -->

FIG. 2. ( _top_ ) Probability distributions for the number of scoring events in a game, and ( _bottom_ ) the randomization test results for each sport, by season, versus a false positive rate of _α_ = 0 _._ 05 (dashed line). The team sequences of each game are tested independently and we plot the proportion of games that reject the null hypothesis that the sequences are random. Because CFB, NFL and NHL typically have a small number of events per game (upper panel), the null hypothesis is difficult to reject. 

rate of _α_ = 0 _._ 05 (Fig. 2). We also consider each season separately so as to reveal non-stationarities. Basketball, unlike the other sports, produces a large proportion of rejections for the serial and autocorrelation tests, which reflects the known anti-persistence pattern in basketball scoring [14]. 

On the other hand, for all sports except basketball, each of these tests rejects the null hypothesis at close to or below the chosen false positive rate, a finding consistent with each of these sequences being random. However, this interpretation is problematic. The serial test makes the very strict assumption that each sequence is drawn from a uniform random distribution, i.e., each is generated by flipping a fair coin several times. A facevalue interpretation thus implies that all teams have an equal chance of winning each game—a highly unlikely situation—and it predicts that the scoring function from Section III B should be independent of lead size, which contradicts the observed pattern (Fig. 1). 

In fact, however, there is no contradiction: the _ψ_ sequences are simply too short (Fig. 1) for these tests to reliably distinguish random from non-random sequences when we assume they are generated independently, i.e., the tests have low statistical power. The one exception is basketball, whose sequences typically contain 90 or so events, while those for American football or hockey typically contain less than 10. 

In the following sections, we show how to circumvent the low statistical power of these tests by exploiting the fact that team sequences are not, in fact, independent of each other. Instead, each season’s sequences are generated by repeatedly selecting pairs from a finite and 

5 

fixed population of teams. This process induces substantial correlations across games that we can capture by modeling the latent skills of each team within a given season. 

## **V. SKILL-BASED SCORING DYNAMICS** 

Toward this end, we develop a series of models of increasing complexity based on specific underlying mechanisms for sports scoring dynamics, including independence, restoration, and anti-persistence. Each of these models represents team skill as a latent variable. We assume that team skill is fixed over the course of any particular season [18], which reflects the relatively stable team rosters and coaching staffs, and low injuries rates in these sports. Furthermore, modeling each season separately allows us to run multiple tests for each sport—one for each season—and allows our models to capture real changes in team skill across seasons [18]. 

Each of our models generates a team sequence _ψ_ by extending the popular Bradley-Terry (BT) model [6] to generate individual scoring events within a game. Traditionally, the BT model is used to estimate unobserved (latent) team skills from the observed outcomes of many games among pairs of teams. The probability that team _r_ wins in a match against team _b_ is given by the skill of _r_ relative to _b_ : 



where _πr, πb ∈_ [0 _,_ 1] is the latent skill for team _r_ . 

## **A. Independent model** 

When scoring events within a game are independent, their generation is equivalent to a simple Bernoulli process with a game-specific bias. This is equivalent to an “independent model” that applies the game-level BT model of Eq. (2) to each of the individual scoring events within a game, yielding 



This represents our first model, which can capture variability in a team sequence caused by differences in team skill parameters, but not other sources of variability. 

## **B. Restorative models** 

Real scoring functions (Fig. 1) produce a range of gradients. However, the independent model can only produce positive slopes. To capture a wider variety of scoring function shapes, and in particular a negative slope or “restorative” pattern, we extend the independent model by allowing each team’s skill to explicitly covary with 

its lead. Such a relationship could arise for psychological reasons, e.g., a winning team “loses steam” or a losing team gains motivation [4], or for strategic reasons, e.g., substituting out or in the more skilled players while in the lead in order to conserve their energy, avoid injury, or create momentum [27]. 

Our restorative model augments the independent model with an explicit per-team “restorative force” parameter _γr_ , which modifies team _r_ ’s strength in response to the current lead size from its perspective _ℓr_ and captures the fact that different teams may have different behaviors in response to how far ahead or behind they are. When _γr <_ 0, team _r_ exhibits a restorative pattern, with skill being proportional to _−ℓr_ . When _γr >_ 0, team _r_ exhibits an anti-restorative or momentum pattern, with skill being proportional to _ℓr_ . 

The probability that team _r_ scores against _b_ is given by 



where _ℓir_ is _r_ ’s lead size just before event _i_ and 



A game as a whole exhibits a restorative pattern whenever _crb <_ 0. This occurs either when both teams exhibit a restorative pattern themselves ( _γr <_ 0 and _γb <_ 0) or when one team’s restorative force is stronger than the other team’s anti-restorative force ( _γr <_ 0, _γb >_ 0, and _|γr| > |γb|_ ). 

The additional term in Eq. (4) relative to the independent model means this model’s scoring function is no longer bounded on the [0 _,_ 1] interval. We correct this behavior by using a sigmoid function of the form _σ_ ( _x_ ) = (1 + e<sup>_−x_</sup> )<sup>_−_1</sup> to provide a smooth and continuous approximation of the misspecified linear function. 

To make this approximation, we change variables so that a logistic curve most closely approximates the linear equation, which occurs when we match the gradients at the point of symmetry at _P_ ( _ψi_ = _r_ ) = 1 _/_ 2. Setting the derivative _σ_<sup>_′_</sup> equal to _crb_ , we find 





Finally, in solving Eqs. (6) and (7) we obtain the following transformation of variables: 





where _mrb_ and _vrb_ are the variables used in the logistic function such that _crb_ and _drb_ retain their linear interpretation and are thus comparable to the skill variables in 

6 



<!-- Start of picture text -->
1. 0<br>y =¡0:02x +0:6<br>0.8 y =¾(¡0:08x +0:4)<br>0.6 y =¡0:01x +0:8<br>y =¾(¡0:04x +1:2)<br>0.4<br>0. 2<br>0.0<br>−40 −20 0 20 40 60 80<br>lead size<br>p(score|lead)<br><!-- End of picture text -->

FIG. 3. Two examples of linear functions matched to logistic functions using the change of variables in Eqs. (8) and (9). 

the independent scoring model. Figure 3 shows examples of two linear functions and their corresponding logistic approximations. 

## **C. Anti-persistence models** 

In many sports, we observe an _anti-persistent_ pattern in the team sequences, in which the probability that _r_ scores next depends on which team scored last, i.e., _P_ ( _ψi_ +1 = _r | ψi_ ). For example, for NBA team sequences, the rate of _rr_ and _bb_ bigrams is only 0.35, indicating strong anti-persistence. (The rates for CFB, NFL, and NHL are 0.45, 0.44, and 0.49, respectively.) Such an antipersistence pattern can occur when teams have different degrees of skill at defensive and offensive play, e.g., when both teams have offenses that are relatively stronger than the opposing team’s defense. 

To capture these effects, we extend the independent model so that each team has an offensive skill parameter _π_<sup>off</sup> and a defensive parameter _π_<sup>def</sup> . For sports like American football and basketball, ball possession (offensive play) typically alternates after a scoring event. We model this game rule by applying a team’s defensive skill immediately after it scores and its offensive skill after the other team scores. Under this independent anti-persistent model, the probability of scoring event _i_ is 



Finally, we obtain a fourth model by combining the restorative model with the anti-persistent model. 

## **VI. MODELING SCORING DYNAMICS** 

We fit the (i) independent, (ii) restorative, (iii) independent anti-persistent, and (iv) restorative antipersistent models to the team sequences within a given season of each sport, using Markov chain Monte Carlo to estimate each model’s parameters. For each, we assess 

model goodness-of-fit by calculating the held out likelihood for each model under a 10-fold cross validation. Furthermore, we follow this procedure for each season of each sport separately, the results of which are given in Tables II–V. By treating seasons independently, we obtain multiple model assessments within each sport while controlling for within season variability. For each season, we highlight the two highest scores in blue and the highest score in bold. 

In basketball (NBA), we find that the restorative antipersistent model consistently provides the best fit across all seasons (Table II), with the second best model being the independent anti-persistent model. These results indicate a strong role for both restoration and antipersistence in driving basketball scoring dynamics. Previous analysis of basketball scoring using random walk theory came to similar conclusions [14]. 

American football (NFL and CFB) shows a different result, with both types of independent model being heavily favored over both types of restorative model (Tables III and IV). The poor fit here of the restorative models indicates that the competitive processes that produce a restorative force in basketball are largely absent in American football. This difference may be related to the much greater scoring rate in basketball relative to American football (Fig. 2): an increased scoring rate lowers the marginal value of each scoring event relative to the game outcome (who wins), and low value interactions in other systems are associated with restorative forces [10, 19]. 

Furthermore, the anti-persistent model for NFL is favored in 8 of 10 seasons over the independent model, while in CFB, it is favored in only 2 of 10 seasons. That is, anti-persistence appears to play a stronger role in NFL games than in CFB games. In fact, CFB is the only sport to strongly favor the independent model, a result that agrees with the our previous simulation results (Fig. 1), which showed that the trivial independent model produced the smallest disagreement for CFB between real and simulated scoring function gradients among the four sports. 

The results for hockey (NHL) are less clear cut (Table V). In 8 out of 9 seasons, the independent antipersistent model is either the best or second best model, and the independent model is best or second best in 7 out of 9. On the other hand, the simple restorative model wins for 2 seasons, and is second best for one. (The restorative anti-persistent model is a poor fit for all hockey seasons.) We note, however, that the loglikelihoods among these three models are all very close, indicating that each performs about as well as the others for these data. Given that NHL is also the one sport among the four that is not anti-persistent by design (possession is determined by a “faceoff” after each goal) and that its scoring function has a negative gradient, we tentatively conclude that the restorative model is better. 

Across seasons, the best overall models appear to be CFB: independent; NFL: independent anti-persistent; NBA: restorative anti-persistent; and NHL: restorative. 

7 

TABLE II. Log-likelihoods on held-out data for NBA games. 

||2002|2003|2004|20|05<br>2|006|2007|2008|2009|2010|
|---|---|---|---|---|---|---|---|---|---|---|
|Independent|-80849|-78814|-84698|-847|44<br>-84|795<br>-|86070|-85727|-86314|-85114|
|Restorative|-80573|-78506|-84361|-844|04<br>-84|469<br>-|85777|-85444|-86005|-84704|
|Independent anti-persistent|-75655|-73823|-79151|-788|41<br>-79|088<br>-|80174|-79841|-80513|-79386|
|Restorative anti-persistent|**-75627**|**-73777**|**-79097**|**-787**|**96**<br>**-79**|**040**<br>**-**|**80141**<br>**-**|**79812**|**-80465**|**-79297**|
||TABLE <br>2000|III. Log-li<br>2001|kelihoods <br>2002|on held-<br>2003|out data f<br>2004|or NFL <br>2005|games.<br>2006|2007|2008|2009|
|Independent|-1286|-1307|-1408|-1372|-1403|**-1373**|**-1369**|-1433|-1484|-1395|
|Restorative|-1324|-1347|-1450|-1402|-1451|-1422|-1424|-1466|-1530|-1432|
|Independent anti-persistent|**-1278**|**-1290**|**-1401**|**-1361**|**-1392**|-1378|-1372|**-1425**|**-1473**|**-1387**|
|Restorative anti-persistent|-1322<br>TABLE|-1337<br> IV. Log-li|-1450<br>kelihoods|-1496<br> on held-|-1448<br>out data f|-1427<br>or CFB|-1434<br>games.|-1470|-1520|-1426|
||2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|
|Independent|-7487|**-7575**|**-8098**|**-8105**|**-7675**|**-7708**|**-7265**|**-8673**|**-8435**|-8097|
|Restorative|-8114|-8182|-8689|-8656|-8268|-8176|-7884|-9334|-9065|-8777|
|Independent anti-persistent|**-7486**|-7643|-8142|-8201|-7741|-7759|-7328|-8678|-8458|**-8078**|
|Restorative anti-persistent|-8011|-8113|-8625|-8586|-8198|-8110|-7781|-9214|-8880|-8630|



TABLE V. Log-likelihoods on held-out data for NHL games. 

||2000|2001|2002|2003|2005|2006|2007|2008|2009|
|---|---|---|---|---|---|---|---|---|---|
|Independent|-4432|-4238|-4300|-4078|-5026|-4712|-4504|**-4755**|**-4655**|
|Restorative|-4432|-4238|-4313|**-4056**|-5031|**-4695**|-4511|-4761|-4663|
|Independent anti-persistent|**-4420**|**-4237**|**-4287**|-4068|**-5020**|-4706|**-4497**|-4761|-4668|
|Restorative anti-persistent|-4449|-4254|-4318|-4090|-5045|-4721|-4521|-4787|-4687|





<!-- Start of picture text -->
CFB NBA<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>−50 0 50 −100 −50 0 50 100<br>NFL NHL<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>−60−40−20 0 20 40 60 −10 −5 0 5 10<br>lead size lead size<br>p(score | lead)<br>p(score | lead)<br><!-- End of picture text -->

FIG. 4. Probability that a team scores next as a function of its lead size, for the observed ( _yellow_ ) and simulated ( _black_ ) patterns, each with a linear least squares fit line. Each simulation uses the best overall skill model for that sport to generate synthetic point and team sequences. 

We check these models by performing a semi-parametric bootstrap, generating synthetic _φ_ and _ψ_ sequences of the same number and lengths as observed empirically in each 

season, and comparing the simulated and empirical scoring functions. That is, we repeat the assessment of Figure 1, but now using models that can capture dependence across sequences. The results show that our skillbased models are a dramatic improvement over simulating each game independently (Fig. 4), agreeing closely with the empirical scoring patterns in both the gradient and range of lead sizes. 

## **VII. PREDICTING OUTCOMES** 

We now apply our models to two online prediction tasks in each of the sports: _Who will score next?_ and _Who will win?_ For both tasks, we let our models observe the point and team sequences of the first _T_ games in a particular season. We then use these models to predict for each unobserved game in that season (i) the team sequence values _ψi_ for 1 _≤ i ≤ N_ , and (ii) the identity of the winning team, when each model is allowed to observe the game states ( _ψj, φj_ ) for 1 _≤ j < i_ . In the second task, all models predict point values _φi_ as the mean value _⟨φ⟩_ averaged over all events in the season. We compare our predictions to those of three baseline models. 

The first baseline is a na¨ıve _leading_ model, which assumes that the team currently in the lead is the stronger 

8 



<!-- Start of picture text -->
CFB NBA<br>0.62 0.68<br>0.66<br>0.60<br>0.64 independent<br>0.58 0.62 restorative<br>0.60 independent anti-pers<br>0.56 restorative anti-pers<br>0.58 Bradley-Terry<br>0.54 0.56 first order Markov<br>0.54 leading<br>0.52<br>0.52<br>0.50 0.50<br>NFL NHL<br>0.59<br>0.58 0.55<br>0.57<br>0.54<br>0.56<br>0.55<br>0.53<br>0.54<br>0.5 3 0.52<br>0.52<br>0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.1 0.2 0.3 0.4 0.5 0.6 0.7<br>proportion of season observed proportion of season observed<br>AUC<br>AUC<br><!-- End of picture text -->

FIG. 5. Probability of accurately predicting which team will score next (AUC), when models observe different fractions of a season. Based on 95% confidence intervals, our best model performs significantly better than the baseline models for CFB and NBA, and after observing at least half of the season for NFL and NHL. 

team and thus more likely to both score next and win the game. Specifically, it predicts that team holding the lead at event _i_ will win the next event, i.e., it predicts _ψi_ +1 = _r_ if _L >_ 0 and _ψi_ +1 = _b_ if _L <_ 0, and will also win the game. If _L_ = 0, the model flips a fair coin for _r_ and _b_ . 

The second baseline is the standard _Bradley-Terry_ model in which we infer latent team skills _π_ from the winloss records among teams in the observed games. This model is simpler than our independent model, which infers team skills using team sequences _{ψ}_ of the observed games. 

The third baseline is a simple _first order Markov_ model. It predicts that the next team to score will either be the same or different than the team that scored last according to the empirical bigram frequencies _{rr, bb, rb, br}_ observed in the first _T_ games of the season. Formally, it predicts that a team will score again given it scored last time as 



For both prediction tasks, we assess prediction accuracy via AUC statistic, which gives the probability that a randomly selected true positive is ranked above a randomly selected false positive. The AUC is a statistically principled measure for binary classification tasks like ours where the cost of an error is the same in either direction (since team labels, _r_ or _b_ , are arbitrary). 

## **A. Who will score next?** 

In the first task, we aim to predict which team will score event _i_ , for each 1 _≤ i ≤ N_ , given the sequence of preceding game states ( _φj, ψj_ ) for 1 _≤ j < i_ . For this online prediction task, we learn each model’s parameters from the first _T_ games in a season and then make predictions across all unobserved games within a season and calculate the AUC for all predictions across all seasons to obtain a single score. Each model observes at least 10% of a season, which ensures that every team has played at least a few times. 

The results show that the overall best models identified in the previous section also tend to be the best predictors at who will score next (Fig. 5), although some alternative models also perform well. For instance, the best model for NFL games early in the season is the first order Markov model; however, the best NFL model beats this baseline after about 30% of a season is observed. Similarly, the first order Markov model performs almost as well as the best skill model in predicting who will score next in NBA games, by capturing the known anti-persistence pattern in that sport. One of the worst models across all four sports is the leading baseline, which often performs only slightly better than chance. 

## **B. Who will win?** 

Predicting who will win a game requires extrapolating the point and team sequences to determine the game’s final outcome. We simplify this task slightly by assuming that the number of scoring events _N_ in each game is known. We then allow the models to learn their parameters from the first 30% of each season (other choices lead to qualitatively similar results as those reported here). For each game in the remainder of a season, the models predict the identity of the winning team when they are allowed to observe a progressively greater fraction of game states ( _φi, ψi_ ) for 0 _._ 1 _≤ i/N ≤_ 0 _._ 9—as if each model were watching the game unfold in real time. 

The results show that the overall best model for each sport both consistently outperforms the baselines and also correctly predicts the winner with at least 80% accuracy at a game’s halftime (Fig. 6). 

The relatively poorer performance of the “leading” baseline model illustrates that this prediction task is non-trivial—who is leading at a given moment is not as predictive of who wins as knowing something about team skills and scoring dynamics. On the other hand, the Bradley-Terry baseline performs comparably well very early in the game, but is quickly beaten because it cannot learn from the real-time evolution of a game. 

For this task, most of our skill-based models make very similar predictions and the first order Markov model also performs well. Although the distributions of final lead sizes may be different, the means are very close, and the individual predictions across models correlate strongly. 

9 



<!-- Start of picture text -->
CFB NBA<br>'0 9 0.96 '1 0 0.90<br>'0 8 0.88 '0 9 0.75<br>'0 7 0.80 '0 8 0.60<br>'0'0 65 0.72 '0 7 0.45<br>'0 4 0.64 '0 6 0.30<br>'0 3 0.56 '0 5 0.15<br>'0 2 0.48 '0 4 0.00<br>'0 1 0.40 '0 3 −0.15<br>'0 0 0.32 '0 2 −0.30<br>'00'01'02'03'04'05'06'07'08'09 '02'03'04'05'06'07'08'09'10<br>NFL NHL<br>'0 9 0.90 '0 9 0.90<br>'0 8 0.75 '0 8 0.75<br>'0 7 0.60 '0 7 0.60<br>'0'0 65 0.45 '0 6 0.45<br>'0 4 0.30 '0 5 0.30<br>'0 3 0.15 '0 3 0.15<br>'0 2 0.00 '0 2 0.00<br>'0 1 −0.15 '0 1 −0.15<br>'0 0 '0 0<br>−0.30 −0.30<br>'00'01'02'03'04'05'06'07'08'09 '00'01'02'03'05'06'07'08'09<br><!-- End of picture text -->



FIG. 6. AUC scores for predicting which team will win given the current state of the game. 

FIG. 7. Correlation of inferred skills over years for each sport. We see that the highest correlations occur along the block diagonal indicating that adjacent years are more similar. Note that the scale is different for CFB due to a much higher correlation across all years. 

The greatest difference occurs at the start of the game. In particular, the first order Markov model performs much worse than the skill-based models at the beginning because it has no information about the heterogeneity of team scoring abilities. As the game progresses the predictions tend to converge. This occurs because these models all make predictions based on random walks on a binary sequence _{r, b}_ , the difference being in how they model the transition probabilities. Later in the game we extrapolate less and so the differences between models become less pronounced. 

few years are likely to be very different, with concomitant in team skill. 

The exception to this pattern is CFB, which shows a larger long-term correlation, i.e., a slower rate of change in relative team skills, than in professional sports. We speculate that this difference is caused by the difference in player mobility between college and professional-level sports: professional teams operate in a national player market, and players can move relatively freely among teams, while colleges operate as rough regional monopolies over the sources of their players. 

## **VIII. TEAM SKILL EVOLVES OVER TIME** 

The inferred season-by-season skill orderings themselves are also of interest, as they reveal the particular trajectories of individual teams over time. We show visualizations of these trajectories for NBA and NFL in Figures 8 and 9. We omit CFB because there are too many teams (461) to meaningfully visualize and NHL for space reasons. 

A useful feature of our probabilistic models is the interpretability of their parameters, which are meaningful measures of team skill here. By learning these parameters independently for each season in each sport, we can investigate how team skills have evolved over time. 

Using the best overall model for each sport, we learn its parameters using all data in each particular season and calculate the Spearman rank correlation across team skills for each pair of seasons (Fig. 7). We find that the relative ordering of teams by their inferred skills exhibits strong serial correlation over time, which appears as a strong diagonal component in the pairwise correlation matrices. The low or inverse correlation in the far off-diagonal elements, as well as the block-like patterns observed in CFB and NFL, implies an underlying nonstationarity in team skills for each of the leagues over the roughly 10-year span of data. 

For each plot we highlight the two teams that won the league championship (NFL Super Bowl and NBA Finals) more than once during the period covered by the dataset. It is notable that these teams are not necessarily the most skilled teams under our model. This is unsurprising, as tournaments by bracket are the highest variance method of identifying the most skilled team [3]. Interestingly, in both NFL and NBA games, the highlighted teams tend to have strong offensive skills, while their defensive skills are more variable. This pattern suggests that offensive skills are more important for winning games, which seems reasonable given that a strong defense alone cannot win a game. 

The manner in which team rosters change over time is a likely source of such long-term dynamics in relative team skill. At short time scales, team rosters are fairly stable, with only a few players changing from season to season. However, over longer time scales, these changes accumulate, and rosters separated in time by more than a 

Looking at individual teams, we can see how their skills change with respect to the total ordering. For instance, the Cleveland Cavaliers drafted LeBron James in 2003 and went from being ranked the third worst (of- 

10 



<!-- Start of picture text -->
Cle veland Cavaliers Cleveland Caval iers<br>To ronto Raptors Minnesota Timberw olves<br>Ne w York Knicks Washington Wi zards<br>Mil waukee Bucks New Jersey N ets<br>Ch arlotte Bobcats Toronto Rapt ors<br>Los  Angeles Clippers New York Kn icks<br>De nver Nuggets Golden State War riors<br>Mi ami Heat Charlotte Bobc ats<br>Atl anta Hawks Sacramento K ings<br>C hicago Bulls Indiana Pace rs<br>Orl ando Magic Detroit Piston s<br>B oston Celtics Utah Jaz z<br>Me mphis Grizzlies Phoenix Su ns<br>Gol den State Warriors Milwaukee B ucks<br>Ho uston Rockets Los Angeles Clipp ers<br>New  Orleans Hornets Houston Roc kets<br>Ph oenix Suns Atlanta Haw ks<br>Detroit Pistons Orlando Ma gic<br>Los  Angeles Lakers Denver Nug gets<br>Was hington Wizards Philadelphia 76 ers<br>In diana Pacers Seattle SuperSo nics<br>Se attle SuperSonics Portland Trail Blaze rs<br>Ph iladelphia 76ers Dallas Maveri cks<br>Minn esota Timberwolves New Orleans Ho rnets<br>Utah Jazz Memphis Grizz lies<br>Da llas Mavericks San Antonio Sp urs<br>P ortland Trail Blazers Los Angeles La kers<br>Sac ramento Kings Boston Celt ics<br>Ne w Jersey Nets Chicago Bu lls<br>Sa n Antonio Spurs Miami He at<br>2002 2003 2004 2005 2006 2007 2008 2009 2010<br>De nver Nuggets Cleveland Caval iers<br>Mi ami Heat New Jersey N ets<br>Cle veland Cavaliers Washington Wi zards<br>C hicago Bulls Sacramento K ings<br>To ronto Raptors Golden State War riors<br>Atl anta Hawks Toronto Rapt ors<br>Ch arlotte Bobcats Detroit Piston s<br>Los  Angeles Clippers Minnesota Timberw olves<br>B oston Celtics Charlotte Bobc ats<br>Me mphis Grizzlies Los Angeles Clipp ers<br>Ne w York Knicks Atlanta Haw ks<br>Detroit Pistons Milwaukee B ucks<br>Se attle SuperSonics Indiana Pace rs<br>Orl ando Magic Utah Jaz z<br>Mil waukee Bucks New York Kn icks<br>Was hington Wizards Philadelphia 76 ers<br>New  Orleans Hornets Phoenix Su ns<br>Los  Angeles Lakers Houston Roc kets<br>In diana Pacers New Orleans Ho rnets<br>Gol den State Warriors Portland Trail Blaze rs<br>Ph iladelphia 76ers Dallas Maveri cks<br>Ph oenix Suns Orlando Ma gic<br>Ho uston Rockets Chicago Bu lls<br>Sac ramento Kings Seattle SuperSo nics<br>Minn esota Timberwolves San Antonio Sp urs<br>P ortland Trail Blazers Memphis Grizz lies<br>Ne w Jersey Nets Boston Celt ics<br>Da llas Mavericks Miami He at<br>Utah Jazz Denver Nug gets<br>Sa n Antonio Spurs Los Angeles La kers<br>0 - 0.2 0 - 0.2 0 - 0.2 0 - 0.2 0 - 0.2 0 - 0.2 0 - 0.2 0 - 0.2 0 - 0.2<br>0.2 - 0.4 0.2 - 0.4 0.2 - 0.4 0.2 - 0.4 0.2 - 0.4 0.2 - 0.4 0.2 - 0.4 0.2 - 0.4 0.2 - 0.4<br>Defensive<br>Increasing Skill<br>Offensive 0.4 - 0.6 0.4 - 0.6 0.4 - 0.6 0.4 - 0.6 0.4 - 0.6 0.4 - 0.6 0.4 - 0.6 0.4 - 0.6 0.4 - 0.6<br>0.6 - 0.8 0.6 - 0.8 0.6 - 0.8 0.6 - 0.8 0.6 - 0.8 0.6 - 0.8 0.6 - 0.8 0.6 - 0.8 0.6 - 0.8<br>Increasing Skill<br>0.8 - 1 0.8 - 1 0.8 - 1 0.8 - 1 0.8 - 1 0.8 - 1 0.8 - 1 0.8 - 1 0.8 - 1<br><!-- End of picture text -->

FIG. 8. NBA defensive ( _top_ ) and offensive ( _bottom_ ) skill rankings. Teams that won more than one NBA finals game in the data are highlighted, i.e., Lakers ( _orange_ ) 2002, 2009 and 2010, Spurs ( _black_ ) 2003, 2005 and 2007. 

|0 - 0.25<br>0.25 - 0.5<br>0.75 - 1<br>0.5 - 0.75<br>0.25 - 0.5<br>0.75 - 1<br>0 - 0.25<br>0.5 - 0.75<br>0.25 - 0.5<br>0.5 - 0.75<br>0.75 - 1<br>0 - 0.25<br>0 - 0.25<br>0.5 - 0.75<br>0.75 - 1<br>0.25 - 0.5<br>0 - 0.25<br>0.25 - 0.5<br>0.5 - 0.75<br>0.75 - 1<br>0 - 0.25<br>0.25 - 0.5<br>0.5 - 0.75<br>0.75 - 1<br>0 - 0.25<br>0.5 - 0.75<br>0.75 - 1<br>0.25 - 0.5<br>0 - 0.25<br>0.25 - 0.5<br>0.5 - 0.75<br>0.75 - 1<br>0 - 0.25<br>0.25 - 0.5<br>0.5 - 0.75<br>0.75 - 1<br>0 - 0.25<br>0.25 - 0.5<br>0.5 - 0.75<br>0.75 - 1<br>San Francisco 49ers<br>Atlanta Falcons<br>Seattle Seahawks<br>Cincinnati Bengals<br>SanDiego Chargers<br>Bufalo Bills<br>St. Louis Rams<br>New England Patriots<br>Cleveland Browns<br>Arizona Cardinals<br>Minnesota Vikings<br>Washington Redskins<br>New Orleans Saints<br>Green Bay Packers<br>Jacksonville Jaguars<br>Denver Broncos<br>Dallas Cowboys<br>Tennessee Titans<br>Pittsburgh Steelers<br>Detroit Lions<br>Tampa Bay Buccaneers<br>Chicago Bears<br>Philadelphia Eagles<br>Kansas City Chiefs<br>Carolina Panthers<br>New York Giants<br>Houston Texans<br>New York Jets<br>Indianapolis Colts<br>Oakland Raiders<br>Baltimore Ravens<br>Miami Dolphins<br>St. Louis Rams<br>Detroit Lions<br>Oakland Raiders<br>Jacksonville Jaguars<br>Tampa Bay Buccaneers<br>Carolina Panthers<br>Kansas City Chiefs<br>Miami Dolphins<br>Pittsburgh Steelers<br>San Francisco 49ers<br>Cleveland Browns<br>Seattle Seahawks<br>Bufalo Bills<br>Atlanta Falcons<br>Chicago Bears<br>Baltimore Ravens<br>Washington Redskins<br>New York Giants<br>Indianapolis Colts<br>San Diego Chargers<br>Arizona Cardinals<br>New Orleans Saints<br>Denver Broncos<br>Houston Texans<br>Dallas Cowboys<br>Cincinnati Bengals<br>New England Patriots<br>Philadelphia Eagles<br>New York Jets<br>Green Bay Packers<br>Minnesota Vikings<br>Tennessee Titans<br>0 -<br>0 -<br>0 -<br>0 -<br>0 -<br>0 -<br>0 -<br>0 -<br>0 -<br>0 -<br>Arizona Cardinals<br>Cleveland Browns<br>SanDiego Chargers<br>Atlanta Falcons<br>Cincinnati Bengals<br>Tampa Bay Buccaneers<br>Cleveland Browns<br>Seattle Seahawks<br>Detroit Lions<br>Kansas Cit Chiefs<br>2000<br>2001<br>2002<br>2003<br>2004<br>2005<br>2006<br>2007<br>2008<br>2009<br>Defensive|Increasing Skill|
|---|---|
|0.25<br>0<br>0<br>0.25<br>0<br>0.25<br>0.25<br>0<br>0.25<br>0<br>0.25<br>0<br>0.25<br>0<br>0.25<br>0<br>0.25<br>0<br>0.25<br>0<br> <br>Chicago Bears<br>Dallas Cowboys<br>New York Jets<br>Oakland Raiders<br>San Francisco 49ers<br>Miami Dolphins<br>Washington Redskins<br>y<br>Washington Redskins<br>St. Louis Rams<br>Chicago Bears<br>Denver Broncos<br>Oakland Raiders<br>Arizona Cardinals<br>Tennessee Titans<br>|Inc|
|.25 - 0.5<br>.25 - 0.5<br>.25 - 0.5<br>.25 - 0.5<br>.25 - 0.5<br>.25 - 0.5<br>.25 - 0.5<br>.25 - 0.5<br>.25 - 0.5<br>.25 - 0.5<br>Philadelphia Eagles<br>Pittsburgh Steelers<br>Kansas City Chiefs<br>Indianapolis Colts<br>Detroit Lions<br>Jacksonville Jaguars<br>New York Giants<br> <br>Cincinnati Bengals<br>New York Giants<br>San Francisco 49ers<br>Bufalo Bills<br>Houston Texans<br>Dallas Cowboys<br>New York Jets<br> <br>Offensiv|reasing|
|0.75 -<br>0.5 - 0.75<br>0.75 -<br>0.5 - 0.75<br>0.5 - 0.75<br>0.75 -<br>0.5 - 0.75<br>0.75 -<br>0.5 - 0.75<br>0.75 -<br>0.5 - 0.75<br>0.75 -<br>0.5 - 0.75<br>0.75 -<br>0.5 - 0.75<br>0.75 -<br>0.5 - 0.75<br>0.75 -<br>0.5 - 0.75<br>0.75 -<br>New England Patriots<br>Carolina Panthers<br>Houston Texans<br>New Orleans Saints<br>Bufalo Bills<br>Seattle Seahawks<br>Baltimore Ravens<br>Green Bay Packers<br>Denver Broncos<br>St. Louis Rams<br>Tampa Bay Buccaneers<br>Jacksonville Jaguars<br>Miami Dolphins<br>Atlanta Falcons<br>Carolina Panthers<br>Green Bay Packers<br>New England Patriots<br>Indianapolis Colts<br>Philadelphia Eagles<br>San Diego Chargers<br>Baltimore Ravens<br>Pittsburgh Steelers<br>e|Skill|
|1<br>1<br>1<br>1<br>1<br>1<br>1<br>1<br>1<br>1<br>Minnesota Vikings<br>Tennessee Titans<br>New Orleans Saints<br>Minnesota Vikings||



FIG. 9. NFL defensive ( _top_ ) and offensive ( _bottom_ ) skill rankings. Teams that won more than one NFL super bowl games in the data are highlighted, i.e., Patriots ( _black_ ) 2002, 2004 and 2005, Steelers ( _orange_ ) 2006 and 2009. 

11 

fensive) team to a mid-range one. When James left for Miami Heat at the start of the 2010–11 season, we see the Cavaliers’ offensive skill drop to the bottom ranked team, while Miami Heat’s offensive and defensive skills increased to be ranked third and first respectively. We also see that the Los Angeles Lakers’ skills (both offensive and defensive) drop for the 2004–05 season. After facing a difficult 2003-04 season [24], they disbanded the team, lost their coach and faced a number of injuries, resulting in a poorer performance in 2004–05. 

Finally, the range of values occupied by offensive and defensive skills is different between NFL and NBA teams: in the latter, these two skills occupy non-overlapping ranges (large and small respectively), while in the former, they fall in similar ranges. That is, NBA teams are less likely to score when playing defensively than when they have possession of the ball, which serves to create a stronger anti-persistence scoring pattern (0.36) than for NFL (0.44), where skills are more evenly matched. 

## **IX. CONCLUSION** 

In this work we considered the online prediction tasks of _Who will score next?_ and _Who will win?_ based on the sequence of scoring events in the game so far. Our probabilistic models based on latent team skills perform well at both predictive tasks and can predict with a high degree of certainty ( _>_ 80%) who will win a game in each of the four leagues we studied, after only half of the game has elapsed. Furthermore, by using gameplay, i.e., the particular sequence of events within each game, to model team skill rather than just game outcomes, we can infer different types of latent team skills e.g., offensive vs. defensive skills. 

Our statistical models provide a quantitative and principled means of capturing and testing hypotheses about the variability induced by chance, the biases produced by real differences in team skill, and the structural impact of game-specific rules. In applying these models to comprehensive data from four different sports, we found that each of the leagues is best fit by a different model. This 

- [1] J. Arkes and J. Martinez. Finally, evidence for a momentum effect in the NBA. _J. of Quantitative Analysis in Sports_ , 7(3):article 13, 2011. 

- [2] M. Bar-Eli, S. Avugos, and M. Raab. Twenty years of “hot hand” research: Review and critique. _Psychology of Sport and Exercise_ , 7(6):525–553, 2006. 

- [3] E. Ben-Naim and N. W. Hengartner. How to choose a champion. _Phys. Rev. E_ , 76:026106, 2007. 

- [4] J. Berger and D. Pope. Can losing lead to winning? _Management Sci._ , 57(5):817–827, 2011. 

- [5] J. Bourbousson, C. S`eve, and T. McGarry. Space-time coordination dynamics in basketball: Part 2. The interaction between the two teams. _J. of Sports Sci._ , 28(3):349– 

indicates that skill, luck, strategy, and the rules of the game serve different roles in the scoring dynamics across sports. The exception was professional hockey (NHL), where the very low scoring rate resulted in no clear predictive winner among our models. 

Our models and results open up many new directions for future work. For instance, we could incorporate other data such as player or ball positioning [5, 40], or the timing of events [27] to improve our models and allow us to apply them to low scoring sports such as soccer. These models could also be used to make other predictions, e.g., the number of scoring events in a game, the final score, and when a lead is safe [8], and to produce more rigorous team rankings (Figs. 8 and 9). 

In addition to data on gameplay, data on individual player attributes and performance in competitive settings are also often available, e.g., height, strength, speed, accuracy when scoring, defensive skill, passing skill, etc. However, there are no good models that connect these characteristics to team skills and to gameplay as a means of predicting game outcomes. The models we formulated here solve part of this problem by connecting team skill to gameplay. An interesting direction for future work would be to predict outcomes from player statistics via team skills as an intermediary. Such a model would allow teams to make more data-driven choices about how they build team rosters and train their players. This extension of our work would also open up new avenues in designing realistic simulations of competitive play, e.g., for better AI in video games. 

## **X. ACKNOWLEDGEMENTS** 

We thank Ruben Coen Cagli, Ramsey Faragher, Theofanis Karaletsos, Marina Kogan, David Edward LloydJones and Sam Way for helpful conversations, and acknowledge support from Grant #FA9550-12-1-0432 from the U.S. Air Force Office of Scientific Research (AFOSR) and the Defense Advanced Research Projects Agency (DARPA). 

358, 2012. 

- [6] R. A. Bradley and M. E. Terry. Rank analysis of incomplete block designs: I. the method of paired comparisons. _Biometrika_ , 39(3-4):324–345, 1952. 

- [7] S. E. Buttrey, A. R. Washburn, and W. L. Price. Estimating NHL scoring rates. _J. of Quantitative Analysis in Sports_ , 7(3):article 24, 2011. 

- [8] A. Clauset, M. Kogan, and S. Redner. Safe leads and lead changes in competitive team sports. _Preprint, arXiv:1503.03509_ , 2015. 

- [9] P. Dangauthier, R. Herbrich, T. Minka, and T. Graepel. TrueSkill through time: Revisiting the history of chess. In _Neural Information Processing Systems 20_ , pages 337– 

12 

344, 2007. 

- [10] Y. Durham, J. Hirshleifer, and V. L. Smith. Do the rich get richer and the poor poorer? Experimental tests of a model of power. _American Economic Rev._ , 88(4):970– 983, 1998. 

- [11] A. E. Elo. _The rating of chessplayers, past and present_ , volume 3. Batsford, 1978. 

- [12] P. Everson and P. S. Goldsmith-Pinkham. Composite Poisson models for goal scoring. _J. of Quantitative Analysis in Sports_ , 4(2):article 13, 2008. 

- [13] P. A. Flach, S. Spiegler, B. Gol´enia, S. Price, J. Guiver, R. Herbrich, T. Graepel, and M. J. Zaki. Novel tools to streamline the conference review process: experiences from SIGKDD’09. _ACM SIGKDD Explorations Newsletter_ , 11(2):63–67, 2010. 

- [14] A. Gabel and S. Redner. Random walk picture of basketball scoring. _J. of Quantitative Analysis in Sports_ , 8(1):manuscript 1416, 2012. 

- [15] T. Galla and J. D. Farmer. Complex dynamics in learning complicated games. _Proc. Natl. Acad. Sci._ , 110(4):1232– 1236, 2013. 

- [16] T. Gilovich, R. Vallone, and A. Tversky. The hot hand in basketball: On the misperception of random sequences. _Cognitive Psychology_ , 17(3):295–314, 1985. 

- [17] M. E. Glickman. Parameter estimation in large dynamic paired comparison experiments. _J. of the Royal Statistical Society: Series C (Applied Statistics)_ , 48(3):377–394, 1999. 

- [18] M. E. Glickman and H. S. Stern. A state-space model for National Football League scores. _J. of the American Statistical Association_ , 93(441):25–35, 1998. 

- [19] K. Hartley and T. Sandler. _Handbook of defense economics_ , volume 2. Elsevier, 2007. 

- [20] R. Herbrich, T. Minka, and T. Graepel. Trueskill(TM): A Bayesian skill rating system. In _Neural Information Processing Systems 20_ , pages 569–576, 2007. 

- [21] A. Heuer, C. M¨uller, and O. Rubner. Soccer: Is scoring goals a predictable Poissonian process? _Eur. Phys. Lett._ , 89(3):38007, 2010. 

- [22] T.-K. Huang, R. C. Weng, and C.-J. Lin. Generalized Bradley-Terry models and multi-class probability estimates. _J. Machine Learning Research_ , 7:85–115, 2006. 

- [23] L. M. Hvattum and H. Arntzen. Using ELO ratings for match result prediction in association football. _Int. J. of Forecasting_ , 26(3):460–470, 2010. 

- [24] P. Jackson and M. Arkush. _The last season: a team in search of its soul_ . Penguin Press, 2004. 

- [25] D. E. Knuth. _The art of computer programming 2: seminumerical algorithms_ . Addision Wesley, 1998. 

- [26] S. Merritt and A. Clauset. Environmental structure and competitive scoring advantages in team competitions. _Sci. Reports_ , 3:3067, 2013. 

- [27] S. Merritt and A. Clauset. Scoring dynamics across professional team sports: tempo, balance and predictability. _Eur. Phys. J. Data Sci._ , 3(1):article 4, 2014. 

- [28] M. Rabin and D. Vayanos. The gambler’s and hot-hand fallacies: Theory and applications. _The Rev. of Economic Studies_ , 77(2):730–778, 2010. 

- [29] D. Reed and M. Hughes. An exploration of team sport as a dynamical system. _Int. J. of Performance Analysis in Sport_ , 6(2):114–125, 2006. 

- [30] H. V. Ribeiro, S. Mukherjee, and X. H. T. Zeng. Anomalous diffusion and long-range correlations in the score evolution of the game of cricket. _Phys. Rev. E_ , 86(2):022102, 2012. 

- [31] S. Saavedra, S. Mukherjee, and J. P. Bagrow. Is coaching experience associated with effective use of timeouts in basketball? _Sci. Reports_ , 2:676, 2012. 

- [32] C. Sire and S. Redner. Understanding baseball team standings and streaks. _Eur. Phys. J. B_ , 67(3):473–481, 2009. 

- [33] P. D. Staudohar. The hockey lockout of 2004-05. _Monthly Lab. Rev._ , 128:23–29, 2005. 

- [34] T. St¨ockl, J. Huber, M. Kirchler, and F. Lindner. Hot hand belief and gambler’s fallacy in teams: Evidence from investment experiments. Technical report, University of Innsbruck, 2013. 

- [35] D. Tarlow, T. Graepel, and T. Minka. Knowing what we don’t know in NCAA football ratings: Understanding and using structured uncertainty. MIT Sloan Sports Analytics Conf., 2014. 

- [36] A. Thomas. Inter-arrival times of goals in ice hockey. _J. of Quantitative Analysis in Sports_ , 3(3):article 5, 2007. 

- [37] R. C. Vergin. Winning streaks in sports and the misperception of momentum. _J. of Sport Behavior_ , 23(2):181– 197, 2000. 

- [38] A. Wald and J. Wolfowitz. On a test whether two samples are from the same population. _The Annals of Mathematical Statistics_ , 11(2):147–162, 1940. 

- [39] G. Yaari and S. Eisenmann. The hot (invisible?) hand: can time sequence patterns of success/failure in sports be modeled as repeated random independent trials? _PLOS ONE_ , 6(10):e24532, 2011. 

- [40] Y. Yue, P. Lucey, P. Carr, A. Bialkowski, and I. Matthews. Learning fine-grained spatial models for dynamic sports play prediction. In _Int. Conf. on Data Mining_ , pages 670–679, 2014. 


