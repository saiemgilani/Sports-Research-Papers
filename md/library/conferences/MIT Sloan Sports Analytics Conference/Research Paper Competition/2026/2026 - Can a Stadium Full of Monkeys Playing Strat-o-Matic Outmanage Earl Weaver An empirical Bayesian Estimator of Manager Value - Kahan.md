<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2026/2026 - Can a Stadium Full of Monkeys Playing Strat-o-Matic Outmanage Earl Weaver An empirical Bayesian Estimator of Manager Value - Kahan.pdf -->

# **Can a Stadium Full of Monkeys Playing Strat-o-Matic Outmanage Earl Weaver? An empirical Bayesian Estimator of Manager Value** 

Paper Track 121 

**Abstract:** For a sport that is approaching a state of analytic saturation, major league baseball is devoid of one seemingly critical metric: a _manager value_ estimator. Whether managers have ever meaningfully influenced their teams’ performances and still do today are matters of significant dissensus. Without a manager-value estimator, that debate (critical, at a minimum, to informed front-office decisionmaking) cannot be convincingly resolved. This paper examines three candidates for such a measure. These metrics are tested with Bayesian statistical methods: Monte Carlo and bootstrap simulations (the equivalent of over a million Strat-o-Matic monkey managers) are used to form empirical nulls; these are then used to calculate False Discovery Rates and form posterior estimates in relation to Regions of Practical Equivalence. Convergent results suggest that a substantial fraction of managers (including current and recently active ones) have over their careers influenced team “winning percentages” ≥ ± 0.012, the equivalent of ± 2 wins per 162 games. The paper constructs a composite _Hybrid Estimator_ , which can be used for making historical comparisons and for assessing current performances. The Estimator can also be calibrated to reflect the asymmetric-error costs and risk preferences that characterize the tournament structure of MLB economics. 

## **1. Introduction: What difference does the manager make? An analytics lacuna** 

Do managers matter as much today as they did before the baseball analytics revolution? Debate cleaves commentators down the middle (Keating, 2019; Stark, 2019). Moreover, even those who deny that analytics have diluted the significance of managers are not of one mind: about half say that managers have always been important to the fates of their clubs (Miller, 2025), and half that they _never_ were (Bauman, 2019; Paine, 2014). 

Debates over the determinants of team success in major league baseball are no shock; what is, though, is the silence of contemporary analytics itself in this particular dispute. Baseball is suffused with recently developed, data-driven metrics for quantifying the impact that _player_ performances have on team records. But to date, no value estimator akin to WAR has even been developed for gauging the consequence of managers. 

This is not only weird but disconcerting. A central mission of sports analytics is to guide enlightened front-office decisionmaking. If managers _do_ matter, executive management is effectively flying blind when they make the multi-million annual investments now devoted to securing the services of field managers (Elsly, 2025). If managers _don’t_ matter, front offices are squandering resources: they 



1 

might as well pay monkeys daily rations of bananas to manage their clubs and devote the savings to aspects of player performance that have a demonstrable impact on the fate of their teams. 

The aim of this paper is to devise a valid, useable _manager-value estimator_ . To do so, it pits real-life managers against the computer equivalent of hordes of monkeys. The principal means of testing candidate measures consists of simulations that enable the performance of human-managed teams to be assessed in relation to ones that operate without the input of any human-manager signal—ones, in other words, whose on-the-field decision-making is being guided by the equivalent of Strat-o-Matic playing chimpanzees. This “planet of the monkey manager apes” baseline forms a _simulated empirical null_ (Zhang, 2020), against which real-world manager effects can be genuinely tested—and quantified with Bayesian statistical methods. 

By using this process to test a series of candidate manager-value estimators, it becomes possible to form judgments about whether these metrics (or some subset of them) can confidently be accepted as measuring what they purport to be measuring: namely, the difference that individual managers make to the performance of their teams over and above the skill of the teams’ players. The results can then be crafted into a set of tools that help front-office decisionmakers and others make assessments of the value of managers—both in absolute terms and relative to one another. 

## **2. Background: the manager-measurement problem** 

#### **2.1. What are we looking for** 

We can plainly _see_ what determines baseball outcomes: the scoring of runs. The more runs a team scores, and the fewer of them it allows, the more likely it is to win individual games and to finish atop the standings in a season. 

What we _can’t_ see directly is precisely what generates the ratio of runs scored to runs allowed. To be sure, the answer is good hitting, good pitching, and good fielding; but how do we know exactly _how good_ players are at hitting, pitching, and fielding, and how important each is for producing runs and stifling the same? 

From the beginning of baseball, fans, commentators, and front-office decisionmakers have been seeking to quantify these attributes with statistical measures (Schwarz, 2004). These statistics—from batting average to ERA to fielding percentages—are _value estimators_ : metrics for quantifying on the basis of _observable indicators_ the _not directly observable_ player characteristics that create and prevent runs. 

The history of baseball analytics consists in the refinement and perfection of these estimators. Metrics like OPS, wOBA, FIP, and Defensive Efficiency (Blabac, 2010) have relegated the traditional performance statistics to historical curios. The epitome of this process of statistical maturation are systems like WAR (Smith, 2024)—empirically validated measures of “true” player value that enjoy tremendous influence, maybe not uniformly among everyday fans but universally with informed analysts and front-office executives (Castrovince, 2019; Yomtov, 2025). 

There is no equivalent to WAR for _managers_ —no established _value estimator_ that translates observable indicators into a serviceable index of managers’ impact on outcomes. The metrics that exist, like career wins or winning percentage, are the equivalent of the primitive player estimators—batting average, ERA, and fielding percentage—that prevailed before the advance of 



2 

modern analytics. The most blatant flaw in these measures is their conflating of managerial proficiency with the skill of the teams that they managed; a _manager_ value estimator would identify how much a manager is adding to (or subtracting from) the quality of a team’s players. 

But on the basis of successful player estimators, we can identify the criteria that a genuine manager-value estimator would need to satisfy. First, it would need to be _internally valid_ (Brewer & Crano, 2000). That is, it would need to be shown to be based on sound statistical methods that logically support the practical inferences they invite. Measures like ERA and fielding percentage are internally _invalid_ —the former because its estimate of pitching quality is confounded by the proficiency of a team’s fielders in turning batted balls into outs; and the latter because it confines assessment of fielding proficiency to success per play attempted, ignoring that the _number_ of plays a fielder is _able_ to attempt (by virtue of speed and timing) matters much more (Click & Kerry, 2006). 

Second, a manager-value estimator must be _externally valid_ (Brewer & Crano, 2000). That is, such a metric must not only measure something; the thing it measures must be what it _purports to be_ —in this case, the contribution a manager makes to the success of his team. The decline of batting average as a metric is arguably tied to lack of external validity: the percentage of at-bats that result in a hit is in fact a very weak indicator of run-production skill, particularly in comparison to other aspects of performance captured in a measure like OPS (Thorn & Palmer, 1984), for example, a reality the book and later movie _MoneyBall_ (Lewis, 2004) exposed to common knowledge. 

Third, any serviceable value estimator must be _informative._ It must be expressed in or readily translatable into units that figure in the judgments of those who use them. WAR exemplifies an _informative_ evaluator: it purports to tell us how many _wins_ —exactly what, say, a front-office decisionmaker is trying to maximize—a player is worth. FIP also satisfies this criterion: it tells us how many _runs_ a pitcher is responsible for avoiding independently of his supporting fielders. A metric like OPS is not expressed in runs or wins produced but can easily be converted into an internally and externally valid estimate of exactly those quantities. In contrast, a metric like “statistical significance” is generally uninformative—telling us (supposedly) that something matters more than nothing but without indicating how much more or of what (Cohen, 1994). 

#### **2.2. What we’ve seen** 

While no metric of manager proficiency has yet gained currency, it would be a substantial mistake to ignore the work of those who have investigated this topic. Examining previous studies of manager performance not only sharpens understanding of the obstacles that must be overcome to create a workable manager-value estimator; it also distills from the intelligence and hard work of others a range of strategies that can profitably be built upon to reach that objective. 

#### **2.2.1. Pythagorean Expectation** 

Previous investigations of manager effects can be grouped into three classes. The first makes use of the Pythagorean Expectation formula. Devised by Bill James (1983), the formula posits that 





(1) 

3 

where _WP_ stands for winning percentage, _RS_ for runs scored, and _RA_ for runs allowed. An impressive insight that has since been adapted to other team sports (e.g., Cochrane & Blackstock, 2009; Winston, 2012), the Pythagorean Expectation formula explains nearly 90% of the season-by-season variance in MLB team records (Braunstein, 2010). Whether any part of the residual can be attributed to managers is the focus of studies in this group (Hoppes, 1984; Paul et al., 2016). 

Arguably the best measure from this class is _Horowitz’s PH_ . Horowitz (1994) proposes that we evaluate a manager’s career with this regression formula: 





2 A straightforward algebraic transformation shows the second term, ~~(~~ 𝑅𝐴<sup>𝑅𝑆</sup> ) , equals 𝑊𝐿 under the Pythagorean formula. Horowitz thus reasons that β2 should always equal _1_ , and β1—the coefficient 𝑅𝑆 for the gratuitous 𝑅𝐴 term—always equal 0. The sum of β1 and β2, a quantity Horowitz christens _PH_ , indicates how a team fared in relation to its Pythagorean Expectation: a _PH_ greater than 1 means a team won more games, and a _PH_ less than 1 fewer, than what was expected given the ratio of runs scored to those allowed. If a manager finishes his career with a _PH_ ≠ 1, then, according to Horowitz, we can deduce that the manager has exerted either a positive or negative influence on his teams’ winning percentages. Applying this test to a select group of prominent managers, Horowitz concludes (1994, p. 191, Tbl. 1) that Earl Weaver, with a career _PH_ of 1.128, is the best manager of all time. 

Horowitz’s _PH_ has at least one property that makes it extremely attractive as a manager-value estimator: it can be cast as an odds multiplier. By definition, _PH_ = 1 when a team is just as likely to win as lose. This is the predicted outcome when a team scores the same number of runs that it allows, in which case its Pythagorean Expectation winning presentation is .500. If a manager’s _PH_ ≠ 1, that means a team that scores as many runs as it allows would, under his leadership, either exceed or fall short of a .500 record. By how much is denoted by _PH_ , which in that case is equal to the number of wins per loss. So in Weaver’s case, a nominal “.500” team would in fact win 1.128 games for every game it loses—hence odds of 1.128:1 rather than 1:1, equating to a _.530_ winning percentage. That is how much better—.530 vs. .500—an average team would fare under Weaver’s leadership. Like player and team WAR, then, Horowitz’s PH is ideally _informative_ in the sense associated with the third criterion of a manager-value estimator. 

The potential problem for Horowitz’s _PH_ is the second criterion—internal validity. Critics have levelled against this metric a charge that would undermine all systems that use the Pythagorean Expectation as a manager-performance benchmark: namely, that deviations from the Expectation reflect nothing more than random draws from an analytically fixed distribution of outcomes. The formula captures—mathematically—the expected ratio of wins to losses when runs scored and runs allowed vary in a normal way (Miller, 2007; Kaplan & Rich, 2017). If we know the runs-scored/runs-allowed ratio, the Pythagorean Expectation formula does not dictate a unique season record—only one located somewhere in the probability distribution of winning percentages associated with that ratio. On this view, then, any deviation from the Pythagorean Expectation tells us only what the particular random distribution of runs scored by a team happened to look like in a 



4 

given season (Braunstein, 2010). If a team exceeds its expectation, we know that the frequency of run scored was smoother than usual, a pattern that naturally conserves runs for effective use in close games. If a team falls short of its exact Expectation total, then the occurrence of run scoring must have been atypically ragged: blowout wins “wasted” runs that would have had higher marginal value in games lost by one- or two-run margins. The manager has nothing to do with any of this; he is just along for the random-variable ride (Ruggiero _et al_ ., 1997). 

In reply, Horowitz (1997) argued that a surplus of close-scoring wins is exactly what wisely exercised managerial decisionmaking would produce. Better managers, on his account, _cause_ lower-variance run-scoring distributions. The debate continues (Pavitt, 2025 ch. 8, pp. 7-8). 

#### **2.2.2. Value added** 

A second class of empirical assessments evaluates managers’ won-loss records controlling for team quality. The idea is that if teams managed by a particular manager do better or worse than the skill of their players predicts, then the manager can be inferred to be adding—or subtracting—independent value. Some researchers employing this type of analysis have found that managers matter (Jaffe, 2010; Kahn, 1993; Singell, 1993), some not (Smart, Winfree & Wolf, 2018). 

A sound theoretical strategy, the manager-value added method, too, can be challenged on internal validity grounds. Some blindly assign the entire residual of team-performance to managers with no attempt to measure what fraction of it might be reasonably attributed to them as opposed to chance variation or other systematic influences. Others use multivariate methods but rely on weak measures of player performance devised before the advent of modern analytics. The variance explained by these measures tend to be much lower than those associated with state-of-the-art metrics reflected in the prevailing WAR systems. Leaving explainable player-performance variance on the table risks both the creation of spurious manager effects and the inflation of genuine ones. 

A related internal validity defect constrains Data Envelopment Analysis, another prominent approach in this class. DEA measures the “efficiency” with which “decision units” (here, managers) make use of available resources (player talent in this case) (Porter & Scully, 1982). But DEA analyses lack indicia of measurement error. This feature of DEA makes it impossible to partial out chance variation from a manager’s supposed contribution, or to quantify the degree of confidence users of this metric should have in its estimates (Ruggiero, 2010). 

Just as important, analyses in this Value-added class tend not to be _informative_ in the sense specified by the third manager-value estimator criterion. Characteristic of many traditional empirical analyses, work in this area is dominated by null hypothesis testing. Investigators are content to show that a manger effect term had a significant coefficient or added to model _R_<sup>_2_</sup> without either specifying the practical import of that effect or identifying it with particular managers. Investigations that culminate in a bland pronouncement that manager impact generally can be shown to “differ from zero at p < 0.05” are of little help to analysts trying to appraise the performances of past managers or to front-office decisionmakers trying to gauge the expected value of retaining or replacing any particular manager today. DEA analyses helpfully rank managers in relation to the top-scoring one, who is awarded a score of 100 (Hadley & Ruggiero, 1999). But those rankings do not yield a straightforward method for translating those scores into team-performance outcomes. 



5 

#### **2.2.3. Better—or worse—than predicted** 

Whereas the first two classes extract manager value from elements of team performance unexplained at season’s end, the final one seeks it in the gap between team records and _pre_ -season forecasts. Bill James in his book _Guide to Baseball Managers (_ 1997) proposes a formula for forecasting team winning-percentage based on a weighted sum of a club’s records in the past three seasons. The manager is credited with—or blamed for—the difference between predicted and actual wins. Because it thus cashes out the value of managers in exactly the currency that matters, James’ method is _informative_ in the manner specified by the third manager-value estimator criterion. 

But like the Pythagorean Expectation and Value Added approaches, this one, too, faces serious internal validity difficulties. James offers no evidence that his forecasting metric actually predicts team performance; if it doesn’t, the wins and losses this method assigns to managers will be arbitrary. In addition, this system assumes—implausibly—that the full allotment of extra wins or losses is due entirely to the manager. Surely some fraction of the residual between expected and realized team winning percentage—if not the entirety of it—is a product of simple random variation. Whether, and how much of, it is in fact the manager’s contribution can’t be assumed but rather must be measured in a valid way. 

#### **2.2.4. The external validity question** 

All of these tests lack _external validation_ . With greater and lesser success, their developers have attempted to fashion systems that we can be confident are measuring something in a systematic way. But none has taken the further step of demonstrating either that _what’s_ being measured is a durable quality of managerial judgment or that it genuinely accounts for meaningful differences in teams’ overall records. 

## **3. Overview of sample, methods, and analytical strategy** 

The philosophy of this study was _unite_ and conquer. Adapting, synthesizing, and building on existing work, the study tested three candidate manager-value metrics under a protocol guided by the criteria of internal validity, external validity, and informativeness. In the spirit of Horowitz’s _PH_ , the first of these instruments, the _PE Model_ , was designed to assess how managers’ teams fared in relation to the Pythagorean Expectation formula. The second can be called _mWAR Model_ : it assessed whether a manager could be shown to contribute to a team’s record over and above (or under and below) the impact of players as measured by their aggregate player WARs. And the third was the _JF Model_ , which measured manger performance relative to a modified version of James’s pre-season forecast formula. 

The sample for these tests consisted of just over 500 managers. This total included every individual who had been entrusted to manage a team between 1901 and 2025 with the exception of those handling only short-term stints (15 games or fewer), trial periods that added little evidentiary value and complicated model fitting. The records of the sampled managers were compiled at the game level and aggregated as appropriate over seasons and careers. The data were compiled using Retrosheet (which owns the copyright and permits use free of charge). 

Previous empirical studies have limited their consideration to only a select numbers of managers—ones who either managed a substantial number of games over their careers or whose 



6 

tenures spanned a specified set of seasons. Truncating the sample in this fashion not only limits power but also risks bias by extracting model parameters from potentially nonrepresentative classes of managers. These problems are avoided by a sampling method as close as feasible to universal. 

The testing protocol envisioned phases aimed at determining internal and external validity of the candidate measures before using them to form an estimator. The first was in model construction and specification designed to form the best estimate of the manger-independent component of each prospective estimator and the portion of any residual that can systematically be attributed to manager influence. 

Second, for each model simulation methods were used to create an _simulated empirical null_ distribution (Zhang, 2020; Zhang & Sun, 2019; Westfall 2011). These simulations were designed to faithfully reproduce the random processes—such as generation of runs at the game level—responsible for key outcome measures but _without_ manager input. In effect, the simulations generated the result we’d see if a stadiumful of monkeys—indeed, many stadiumsful —had managed the teams in question. Using this Bronx Zoo benchmark (Lyle, 1979), it was then possible to assess whether _human_ managers could plausibly be viewed as the source of the effects attributed to them by the PE, mWAR, and JF Models. 

The next phase of testing was aimed at assuring external validity. Models that survived the internal validity filter were to be assessed for agreement. Again, a manager-value estimator cannot be externally validated by comparing its results to observable outcomes. But we garner a close substitute for that if we observe agreement among multiple internally valid estimators derived from independent data sources. If such measures agree, then one of two conclusions follows: either they _are_ measuring the same unobserved quantity of interest (with greater or lesser amount of fidelity); or they are fortuitously measuring other things (who knows what) that just happen to be correlated with each other despite their diverse origins. The former conclusion is considerably more probable than the latter. This is a _convergent external validation_ strategy (Campbell & Fiske, 1959). 

This _unite and conquer_ approach has another advantage. No indicator of an unobserved trait or characteristic will ever be perfect; any such indicator will inevitably be subject not only to measurement error but also to the risk of confoundment with some influence extraneous to the quantity that is being estimated—here manager value. But when internally valid, reasonably defensible models are combined, they help to offset or dilute these potential defects in one another: so long as they are derived from independent data streams—as PE, mWAR, JF are—they can be expected to cancel out the noise associated with their individual sources of measurement imprecision and association with extraneous influences while amplifying their shared signal. The result is a synthetic latent-variable instrument that is more accurate, more precise, and more worthy of confidence than any of its individual components (Campbell & Fiske, 1959). 

Constructing a _composite estimator_ of this type was to be the aim of the next phase. Any two or three models determined to be measuring a common latent trait of managerial judgment were to be synthesized via an appropriate model, the data output of which could be used to fuel a full-fledged Bayesian estimator (Beasley & Rodgers 2012; Efron, 2024; 2012). 

The estimator would be crafted to meet the information criterion. Every source model was constructed to generate results that could be expressed in terms of a manager’s marginal impact on the winning percentage of a team otherwise expected to achieve a .500 record under the guidance of 



7 

an “average manager.” By extension, these marginal winning-percentage impacts could be translated into an expected number of wins above (or losses below) average over 162 games. The estimator would use the model-generated data to form posterior estimates of the probability that any specified manager—or any particular fraction of all managers—possessed a level of latent ability sufficient to influence team records by a specified consequential margin. 

Finally, the adaptability of the estimator to practical use was to be perfected. Specific tools were to be developed to enable users to form evolving estimates of latent skill season-by-season, and also to conform those estimates to user-defined economic or utility criteria. 

## **4. An ensemble of models** 

_Estimators_ will be distinguished from _models_ . An estimator is the instrument that generates measures of _θ_ , the unobserved latent skill of individual managers. Models assemble observed results into performance estimates, which furnish the _data_ the estimator uses to gauge _θ_ via Bayesian updating. Because the validity of estimator results depend on the validity of the data, the first step in assessing a potential estimator is to assure that the underlying model is in fact valid. 

Three such models are evaluated. The first is the Pythagorean Expectation or _PE Model_ . Like Horowitz’s _PH_ (1994) _, PE_ measures the performance of a manager _relative_ to his team’s Pythagorean Expectation. The second model, _mWAR_ , builds on the work of analysts who have sought to measure the value added by a manager in relation skill of his team’s players. Because WAR is now widely regarded as the best estimator of player value, it was used to form the player-skill baseline. And finally, the JF model is based on James’s forecasting method (1997) for calculating manager wins. 

In model assessment, test statistics—in particular _z_ ’s—will be used to gauge model outcomes in relation to simulated empirical nulls. The test statistics will be computed by a process—including use of the same underlying method of measurement and the calibration of them to the same scale (Templ, 2016; Efron, 2004)—that assures their comparability. The aim of such assessment, however, is not to certify that model outcomes are “statistically significant” per se. Rather it is to supply a practically meaningful assurance that the model as a whole can be viewed as conveying _some_ genuine and discernable signal of manager influence. Bayesian estimation depends on such a signal. Assuming that there is one to detect, Bayesian methods can be relied upon to assign that signal the weight that it deserves in a manner that is more discerning than—and not constrained by the arbitrary characteristics of— _p_ -values (Goodman, 1999a, 1999b). 

#### **4.1. The Pythagorean Expectation (PE) Model** 

#### **4.1.1. Model specification** 

The basic _PE_ Model was structured to try to amplify and refine the signal of manager impact associated with Horowitz’s _PH_ . As discussed, Horowitz fit his model separately to each tested manager. Balkanizing a manager-performance model into as many independent replicates as there are managers in a sample creates numerous difficulties. To begin, it squanders statistical power. Even managers with the longest careers tend to log fewer than 20 seasons, and most substantially fewer; when tested individually, none can borrow strength from the precision with which the effect of the Pythagorean Expectation is estimated when applied to all managers at once. Indeed, when the impact of the Expectation is estimated separately per manager, each measurement is shaped 



8 

entirely by that manager’s own seasons; as a result, this method generates no uniform estimate of the Expectation’s impact that can be used as common benchmark for comparing performances. Finally, when every _manager_ is tested independently of every other, there is no shared covariance matrix—and thus no shared measure of the extent to which any particular manager is out- or under-performing the Expectation to a greater extent than anyone else. 

The _PE_ Model avoids these problems by fitting a single model to all managers: 





_WPit_ is manager _i_ ’s winning percentage in season _t_ . _β1_ measures the impact—estimated sample-wide—of the Pythagorean Expectation on _WPit_ . The fixed effect μ _i_ is manger _i_ ’s career-estimated impact on his team’s season _t_ winning percentage _after the effect of the Pythagorean Expectation is partialed out_ . This is the same information that the β2 parameter in 

Horowitz’s model (2) is intended to extract. However, here it is measured not on the basis of differences in an individual manager’s performance over a handful of seasons but rather via a comparison of his seasons to thousands of seasons generated by hundreds of other managers, all of whose performances can be assessed in relation to a global estimate of the impact of the Pythagorean Expectation. 

Horowitz’s transformation of the Pythagorean formula (1) was cleverly structured to yield an estimate of a manger’s impact when he heads a team expected to produce a .500 winning percentage (2). But the same effect can be achieved in the _PE_ Model by simply setting _RS_ equal to _RA_ when predicting the effect of μ _i_ in the PE Model. 

#### **4.1.2. Simulated empirical null formation** 

As discussed, scholars disagree about whether Horowitz’s _PH_ measures anything other than the dart-board patchwork of the Pythagorean Expectation formula itself as a random variable. Maybe this point can be settled analytically. But it can definitely be resolved by simulation. Properly constructed, a simulation can be used to mark out the Pythagorean Expectation’s random probability perimeter. If Horowitz’s critics are right, then we shouldn’t be able to find a single manager over the course of Major League Baseball history who has succeeded in crossing it. 

That was the idea that guided the formation of the simulated empirical null distribution created to test PE. Typically, empirical testing relies on a _theoretical null_ : the canonical form of a normal distribution presumed to be appropriate for the class of events in question. But what if the true form of the random distribution associated with process of interest is _different_ from what is assumed? That could lead to either overly conservative or overly liberal inferences about the causal mechanisms behind some observed phenomenon (Zhang & Sun, 2019). The goal of empirical null distribution is to avoid those risks by generating a more realistic picture of what the world of outcomes generated by that random process actually looks like (Westfall, 2011; Efron, 2004). 

The empirical null constructed to test PE featured a Monte Carlo simulation (Beaseley & Rodgers, 2012). In it, every major league manager’s entire career was reconstructed _at the game level_ . For every season he managed, his team’s mean runs scored and runs allowed per game were calculated. Then each game of his career was replayed—1,000 times—using random draws of runs scored and 



9 

allowed anchored on those means. The draws were taken from a negative binomial distribution, which was constructed to reproduce the standard deviation of game-level run scoring league wide for the season in question. 

The game-level production of runs is the critical location of the random process associated with the Pythagorean Expectation. The Expectation’s fit with observed outcomes encodes a basic statistical truth about the ratio of runs scored and allowed, on the one hand, and winning parentage on the other (Miller, 2006; Kaplan & Rich, 2017). Because variance in run scoring creates deviations from the Expectation winning percentage, the issue between Horowitz (1997) and his critics (Ruggiero et al. 1997) is whether such variance is attributable to the acumen (or incompetence) of managers or sheer chance. 

The Monte Carlo simulation can go a long way to settling this dispute. The simulation recreates some 500 manager careers 1,000 times from the game level up—but free from the critical strategic decisionmaking of those managers, or at least free from anything they contributed to how many runs their teams scored in close games. The assignment of unusually smooth and unusually ragged run-scoring distributions is indisputably attributable random variation. We can thus learn from the simulation how many, and by what margin, completely skill-free _monkey_ managers would beat (or get beaten by) the Pythagorean Expectation by chance alone. The internal validity of the PE Model, son of Horowitz’s PH _,_ depends on finding that the records of human managers do in fact vary from the Expectation even more decisively. 

To enable detection of such managers, the regression model described above was applied separately to each of the replicated sets of manager careers. Doing so generated a densely populated distribution of 500,000 career-level manager encounters with the force of the Pythagorean Expectation treated as a random variable (which in the simulation, as in the real-world, accounted for 90% of the variance in the team records). Interrogating this distribution could thus be expected to yield a well-grounded and determinate answer to the question of how far “lucky” mangers might travel consistent with the gravitational pull of the Expectation formula. Comparing the simulated empirical null distribution to the _observed_ one would then answer the question whether any real-life, human manager had ever managed to escape Pythagoras’s grasp. 

Additional details on the structure of the simulation can be found in the Appendix (App.) 

#### **4.1.3. Analysis.** 

Of the 507 managers tested, 29 compiled career records that defied their Pythagorean Expectation by |z| _≥_ 1.96 (Table 1). Seven of them _out_ performed the formula by that degree, and 22 _under_ performed it; none of them appears on Horowitz’s list of managers with _PH_ s unequal to 1 (1994, p. 191, Tbl. 1). This surplus of extreme deviations is visible in Figure 1.A, which shows a mild degree of overdispersion of manager scores in the observed sample relative to a normal one. 

There are two reasons, however, not to view this result as informative in itself. First, in a sample of 507, there will be managers who experience deviations of this size by chance. The expected number whose records will deviate by  |z| _≥_ 1.96 is 25; 29 or more observations with |z| _≥_ 1.96 can be expected to occur roughly 25% of the time. 

Second and more importantly, this estimate of expected extreme values itself rests on an untested assumption: namely, that team records are distributed normally in relation to the Pythagorean 



10 

Expectation. If the true distribution is more compact than that, the expected number of managers whose career records would be expected to fall outside the Pythagorean boundary by chance will be lower than 25, and if more dispersed higher. 

The Monte Carlo simulated empirical null distribution is designed to overcome this inferential barrier. Assuming the random process used to generate it was well formulated, the simulated empirical null furnishes a better picture of what a chance distribution of manger records would actually look like. To put them on the same scale and facilitate inspection of their contours, the observed distribution was calibrated by taking the difference between each sample member’s _z_ -statistic and the simulated null mean, and then dividing that quantity by the latter’s standard error (Efron, 2004, 2008). 



**Figure 1. Observed PE Model, theoretical null, and simulated empirical null distributions.** _Z_ -statistic distributions are presented to facilitate assessment of the extremeness of observed sample values relative to a normal distribution and to the simulated empirical null.  Panel (A) superimposes the observed, blue PE Model distribution on the gray theoretical null; and panel (B) superimposes the observed distribution on the red simulated empirical null distribution after calibration. The studentized test statistic for the observed sample was generated by Monte Carlo methods to conform to the empirical null and enable appropriate comparison (Templ, 2016; Wellar & Gotway, 2004). 

When the calibrated sample and simulated empirical null are superimposed, the sample distribution fits almost perfectly atop the latter (Figure 1.B). In other words, the big picture view of the data looks very much like what one would expect were deviations from the Pythagorean Expectation generated by random forces fully divorced from manager skill. 

A formal test of this conclusion is calculation of the False Discovery Rate (FDR). FDR uses the empirical null to determine the probability that observations at any specified point in the sample distribution are a consequence of a systematic, non-chance influence (Efron, 2004, 2024). 

Performed here, FDR supports the conclusion that good or bad luck, and not skill or lack thereof, was most likely responsible for the extreme _z_ ’s in the real-world sample. The analysis found that, under the PE Model, none of the mangers in the sample had a _z-_ statistic more likely to be observed as a result of a systemic manager effect than as a result of chance. The rate of “false” non-nulls at _z_ > 1.96 was identified as 100%, and 75% on average across both extreme tails. Frequentist FDRs generated materially equivalent results (Storey’s _p_ FDR = 0.88, and Benjamin-Hochberg _q-value_ =0.91, for PE deviations at _p_ ≤ 0.05). 



11 

Twenty-five percent is not 0%. On the whole, though, the data suggest that one of two conclusions is likely true. Either human managers can be expected to perform no better than monkeys rolling dice. Or the critics of Horowitz are correct to view the Pythagorean Expectation as an internally invalid benchmark for manager performance: in effect, the formula reflects a speed-of-light constraint on team winning percentage that no manager’s career record can exceed. 



12 

|_Highe_|_st scorin_|_g PE Mod_|_el mana_|_gers_||_High_|_est scorin_|_g PE Mod_|_el mana_|_gers_||
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||**mpr(w**<br>||||||**mpr(w**<br>||
|**manager**|**g**|**W%**|**PE**|**)**|**_z_**|**manager**|**g**|**W %**|**PE**|**)**|**_z_**|
|Harry Lord|109|.550|.474|.074|2.41|Luke Appling|40|.250|.352|-.113|-2.18|
|Del Rice|155|.481|.424|.057|2.20|Bruce Kimm|78|.423|.494|-.072|-1.96|
|Cecil Cooper|341|.506|.466|.040|2.32|Johnny Kling|153|.340|.388|-.056|-2.15|
|Don Wakamatsu|274|.452|.412|.039|1.97|Charles Zimmer|135|.363|.411|-.055|-1.99|
|George Gibson|757|.546|.519|.029|2.51|Bobby Wallace|216|.287|.326|-.051|-2.30|
|Dick Howser|931|.544|.523|.023|2.18|Joe Frazier|207|.488|.536|-.046|-2.01|
|Lum Harris|941|.489|.462|.022|2.14|Matt Quatraro|322|.464|.472|-.038|-2.08|
|||||||Alan Trammell|482|.382|.414|-.036|-2.44|
|||||||Mickey Vernon|362|.371|.399|-.035|-2.03|
|||||||Billy Herman|461|.408|.438|-.033|-2.17|
|||||||Walt Weiss|645|.438|.463|-.028|-2.23|
|||||||Pants Rowland|585|.578|.617|-.028|-2.08|
|||||||Bobby Bragan|921|.481|.509|-.027|-2.61|
|||||||Jimmie Wilson|1217|.402|.418|-.026|-2.77|
|||||||Buddy Bell|1227|.418|.436|-.024|-2.59|
|||||||Doug Rader|803|.482|.504|-.024|-2.01|
|||||||Preston Gómez|887|.404|.421|-.023|-2.18|
|||||||Hugh Duffy|1206|.444|.455|-.019|-2.01|
|||||||Torey Lovullo|1239|.492|.511|-.019|-2.08|
|||||||Eric Wedge|1587|.476|.497|-.018|-2.19|
|||||||Jim Riggleman|1615|.445|.460|-.017|-2.10|
|||||||Jimy Williams|1697|.535|.557|-.017|-2.22|



**Table 1. Tail-end values from PE Model.** “W%” refers to career winning percentage; “PE” to career Pythagorean Expectation; and “mpr(w)” the PE Model estimated marginal winning percentage relative to a .500 team under an “average” manager. Note that the _z-_ statistic characterizes the measurement error of a manager’s Model score—not its value in relation to the sample mean—and thus does not necessarily align with the magnitude of the score. 



13 

#### **4.2. mWAR** 

#### **4.2.1. Model specification** 

Fit to season-level performance observations, this model was used to operationalize mWAR: 









The outcome variable, _wit_ , is the probability that manager _i_ in season _t_ will win a game based on his team’s winning percentage, _pit_ , over the observed number of games, _git_ , he managed it in that season. The first predictor, _β_ 1 _zWPG_ , is the season-standardized team WAR per game of manager _i_ ’s team in season _t_ . Measuring WAR as per-game rather than a per-season metric puts it on a common scale for all managers, including ones who managed during seasons of different lengths or who managed only partial seasons; standardizing it puts team WARs from different eras on the same scale (Schell, 1999, 2005) and makes it more amenable to use for estimation. The second fixed-effect predictor, _μi_ , is again that manager’s _career_ marginal impact on the probability of winning, this time after the sample-wide impact of WAR per game is partialed out. By setting _zWPG_ = 0, the manager’s impact can be estimated when the team is otherwise predicted to experience a .500 winning percentage under an “average manager.” 

#### **4.2.2. Simulated empirical null formation** 

Again, a simulated empirical null distribution was created via simulation. Under PE, the critical random process that generates chance variation is run scoring, a game-level dynamic. Under mWAR, in contrast, the random process of consequence occurs at the season level: the hypothesis that managers make a difference requires identifying them with systematic deviations from the season records predicted by team WAR alone. 



**Figure 2. Observed mWAR Model, theoretical null, and simulated empirical null distributions.** _Z_ -statistic distributions are presented to facilitate assessment of the extremeness of observed sample values relative to a normal distribution and relative to the simulated empirical null.  Observed SEs determined by bootstrap. Panel (A) superimposes the observed, blue mWAR Model distribution on the gray theoretical null; and panel (B) superimposes the observed distribution on the red simulated empirical null distribution after calibration. The studentized test statistic for the observed sample was generated by parametric bootstrap  to conform to the empirical null and enable appropriate comparison (Templ, 2016; Davison & Hinkley, 1997). 



14 

A parametric bootstrap was used to simulate the empirical null used to test for such an effect (Westfall 2011; Efron, 2012). In this simulation, the mWAR model was estimated without the manager fixed-effect term _μi_ ; because whatever influence particular managers exert was deliberately removed, this process effectively estimated the impact that WAR would have were every team piloted by the “average” manager (Hardy, 1993, p. 68). Then 1,000 replicate manager careers were generated by substituting new win totals drawn randomly from a binomial distribution pegged to each team’s Model-estimated winning percentage. At that point, the full mWAR Model, with manager fixed effects restored, was fit to each simulated career set. The Model’s “average” manager effect shares (0 on net) were thus distributed to each sample member’s 1,000 monkey fill-ins in amounts that varied solely on account of the random statistical churning of team wins and the impacts of the _zWPG_ upon the same. 

#### **4.2.3. Analysis** 

Fifty-five of the 512 members of the manager sample—approximately 11%—generated impacts on team winning percentage, controlling for WAR, that met or exceeded | _z_ | = 1.96, 22 above and 33 below (Figure 2.A).<sup>1</sup> Managers with the biggest _z_ ’s, positive and negative, are identified in Table 2. So is the size of their mWAR Model impact, related in terms of their marginal effect on the winning percentage of a team otherwise predicted to achieve a .500 record under an average manager. 

Were the number of managers with | _z_ | ≥ 1.96 evaluated against a conventional theoretical null standard, the likelihood of it occurring by chance would be about 1 in 7.9 million. That calculation assumes, though, that the result should be evaluated against a canonical normal distribution, a presupposition the simulated empirical null is supposed to critically assess. 

In relation to the simulated empirical null too, however, the observed sample exhibited signs of systematic and not merely random influences. This effect is open to visual inspection in (Figure 2.B). On average, the simulated manager careers had 26 values at or above | _z_ | = 1.96. None of the 1,000 career-level replications had 55 exceedances; the largest number, achieved in 1 of the replications, was 49 (a result one would have expected in one percent of the 1,000 sets of 512 trials under a _theoretical_ , N[0,1] null; the simulated empirical null is indeed more diffuse). These results imply that at least some fraction of the particularly strong and particularly weak performances within the real-life sample are more plausibly viewed as a product of genuine individual differences than as haphazard chance landing points within the distribution of team WAR itself as a random variable. 

Formal analyses supports this conclusion but also temper it. Local FDR (Enron, 2004) indicated that all 26 of the managers who recorded scores that exceeded _z_ =1.96 were more likely than not to be “true nulls”; however, only 6 of those who dipped below _z_ = - 1.96 did. The FDR rate for false nulls in the tail regions overall was 32%. 

Again, the point of this analysis is not to identify which observed effects merit being labelled “truly statistically significant.” No arbitrary threshold was set for the minimal “proportion” of “true” versus “false” nulls. The goal was only to assess whether the observed sample exhibited a manager-effect sharp enough to pierce the random-variable perimeter of WAR. In this case, that test seemed to be reasonably satisfied. 

1 Because it included 2025 managers, the sample size slightly exceeded the one used to test the PE Model, the simulated empirical null for which required complete game logs not yet available for 2025 on Retrosheet. 



15 

The mWAR Model thus suggests at least a modest win for the human over the monkey mangers. But that victory is at best provisional; the margin by which meaningful effects are detected will inevitably be whittled down by the shrinkage associated with Bayesian analysis (Efron & Morris, 1973). How much if any it would be left at that point remains to be seen. 

|_Hi_|_ghest mW_|_AR scores_|<br>||_Lo_|_west mW_|_AR score_<br>|_s_||
|---|---|---|---|---|---|---|---|---|---|
|**manager**|**G**|**W%**|**mpr**<br>**w**|**_z_**|**manager**|**G**|**W**<br>**%**|**mprw**|**_z_**|
|Bob Swift|114|.605|.116|2.4<br>5|Malachi Kittridge|17|.059|-.403|-2.16|
|Stephen Vogt|161|.571|.077|2.7<br>5|George Smith|32|.156|-.289|-2.71|
|Cecil Cooper|344|.506|.072|2.6<br>9|Hans Lobert|153|.275|-.137|-3.11|
|Hank O’Day|307|.498|.063|2.2<br>2|Bobby Wallace|216|.287|-.134|-3.64|
|Frank Chance|159<br>3|.594|.061|4.7<br>5|Harry Wolverton|148|.311|-.12|-2.75|
|Fred Clarke|225<br>1|.596|.053|4.9<br>6|Heinie Wagner|154|.338|-.117|-2.81|
|John McGraw|443<br>9|.59|.048|6.2<br>5|Kid Elberfeld|98|.276|-.113|-2.04|
|Pat Moran|133<br>4|.561|.042|3.0<br>1|Joe Cantillon|455|.347|-.099|-4.04|
|Pete Rose|780|.526|.041|2.3<br>1|Harry Davis|126|.429|-.092|-2.07|
|Felipe Alou|205<br>0|.503|.8|3.3<br>8|Doc Prothro|458|.301|-.084|-3.31|
|Al Lopez|241<br>4|.584|.037|3.6<br>2|Shano Collins|207|.353|-.072|-1.99|
|Joe McCarthy|342<br>6|.615|.036|4.0<br>7|Ray Schalk|236|.445|-.065|-1.99|
|Dave Roberts|135<br>4|.625|.032|2.3<br>7|Alan Trammell|498|.382|-.061|-2.62|
|Danny Ozark|116<br>0|.533|.032|2.1<br>5|John McCloskey|457|.333|-.061|-2.47|
|Fredi González|141<br>1|.507|.030|2.2<br>3|F. Fitzsimmons|302|.384|-.060|-2.01|
|Craig Counsell|149<br>1|.529|.028|2.2<br>6|Deacon McGuire|429|.441|-.053|-2.19|
|Steve O'Neill|185<br>9|.558|.025|2.1<br>5|Stan Hack|471|.423|-.048|-2.07|
|W. Robinson|282<br>7|.499|.020|2.1<br>2|Jimmie Wilson|122<br>7|.402|-.045|-3.08|
|Bruce Bochy|435<br>0|.498|.017|2.3<br>2|Bobby Bragan|921|.481|-.044|-2.66|
|Dusty Baker|401<br>6|.539|.016|2.0<br>6|Jimmy McAleer|162<br>3|.452|-.041|-3.26|
|Tony LaRussa|535<br>6|.535|.015|2.1<br>7|Doug Rader|805|.482|-.041|-2.34|
|Bobby Cox|449<br>0|.555|.015|1.9<br>7|Cito Gaston|172<br>6|.516|-.040|-3.33|
||||||Eric Wedge|158<br>7|.476|-.040|-3.20|
||||||Billy Meyer<br>16|764|.412|-.038|-2.08|





|John Gibbons|158<br>0|.501|-.037|-2.91|
|---|---|---|---|---|
|Lee Fohl|150<br>5|.474|-.036|-2.73|
|Tony Muser|763|.421|-.036|-1.99|
|Fred Haney|137<br>6|.456|-.034|-2.49|
|Dan Howley|921|.431|-.034|-2.05|
|Patsy Donovan|130<br>5|.425|-.031|-2.21|
|Jimy Williams|169<br>7|.535|-.027|-2.22|
|Tom Kelly|237<br>5|.478|-.024|-2.27|
|Lou Piniella|352<br>4|.517|-.019|-2.23|



**Table 2. Tail-end values from mWAR Model.** “W%” refers to career winning percentage and “mprw” the manager’s Model-estimated marginal impact on the winning percentage of a team otherwise predicted to finish with a .500 record under an average manager. Note that the _z-_ statistic characterizes the measurement error of a manager’s Model score—not its value in relation to the sample mean—and thus does not necessarily align with the magnitude of the score. Complete mWAR Model results appear in the supporting materials. 

#### **4.3. The Jamesian Forecast (JF) Model** 

#### **4.3.1. Model specification.** 

The JF Model makes two important modifications to James’s “better—or worse—than expected” system for calculating manager impact (1997). First, it refines his forecasting predictor. Upon testing, it was determined that James’s weighted three-season formula performs no better—has an _R_<sup>_2_</sup> no higher and an RMSE no lower—than a simple one-season auto-regression (AR[1]) model. To improve upon it, an AR(3) model was formed using ridge regression that performed modestly better in these respects (out-of-sample _R_<sup>_2_</sup> _=_ 0.38 vs. 0.36 for James’s formula; RMSE 10.08 vs. 10.22 wins per 162 games). 

Second, and more importantly, James’s system was embedded in a genuine statistical model. Rather than assuming that the entire residual between teams’ forecast and realized performances are attributable to the manager, this model was deigned to estimate how much of that residual inheres in the AR(3) predictor as a random variable, and whether team-performance residuals in excess of that are systematically rather than adventitiously connected to particular managers. 

The JF Model parallels the mWAR one: 





Again the outcome variable ( _wit_ ) is the probability that manager _i_ in season _t_ will win a game based on his team’s winning percentage ( _pit_ ) in games ( _git_ ) he managed that season. The predictor β1𝑧𝐸𝑋𝑊𝑃𝑖𝑡 measures the impact of the AR(3) forecast predictor on the per-game winning 

probability of manager _i_ ’s team in season _t_ . Like _zWPG_ , it is standardized for ease of computation, 



17 

particularly in determining the impact of _μi_ : when 𝑧𝐸𝑋𝑊𝑃𝑖𝑡 is set to 0, _μi_ , the predicted value of the manager’s impact, can be estimated in relation to a team that is otherwise forecast to have a .500 winning percentage under an “average manager.” 



**Figure 3. Observed JF Model, theoretical null, and simulated empirical null distributions.** _Z_ -statistic distributions are presented to facilitate assessment of the extremeness of observed sample values relative to a normal distribution and relative to the simulated empirical null. Observed SEs determined by bootstrap. Panel (A) superimposes the observed, blue JF Model distribution on the gray theoretical null; and panel (B) superimposes the observed distribution on the red simulated empirical null distribution after calibration. The studentized test statistic for the observed sample was generated by parametric bootstrap  to conform to the empirical null and enable appropriate comparison (Templ, 2016; Davison & Hinkley, 1997). 

#### **4.3.2. Simulated empirical null formation** 

The same process used to create the mWAR simulated empirical null was used to create a JF Model one. Because the random process of consequence occurs at the season level, that was the level at which the manager-free effect was generated. A parametric bootstrap was again used: first, the JF Model was estimated without the manager fixed-effect term _μi_ ; then, 1,000 replicate manager careers were generated, using the 𝑧𝐸𝑋𝑊𝑃-predicted winning percentage to ground binomial draws of season wins; and finally the full JF Model, including _μi_ , was refit to each of the 1,000 simulated sets of manager careers. Consequently, each manager’s share of the residual once _zEXWP_ was patriated out was totally disconnected from any genuine manager effect. 

#### **4.3.3. Analysis** 

To search for evidence of systematic manager influence, the same analyses run on the PE and mWAR models were run on the JF Model. As can be seen from Figure 3.A, the dispersion of tail values in the observed data relative to the theoretical null is substantial. A total of 133 of the 499 managers in the sample<sup>2</sup> —some 27%—recorded | _z_ | ≥ 1.96. Assuming the theoretical null accurately reflects the random process that generates divergences in the performance of teams relative to _zEXWP_ , the likelihood of this result is atomically low. 

> 2 Because it excluded managers whose tenures began and ended in the first two seasons of a franchise’s existence, the JF sample was smaller than the PE and mWAR ones. 



18 



**Figure 4. Select JF Model scores** . Managers are arrayed on the _x_ -axis by _z_ -statistic. “Mpr(w)” denotes Model-estimated marginal impact on the winning percentage of .500 team under “average manager.” Note that the _z-_ statistic characterizes the measurement error of a manager’s Model score—not its value in relation to the sample mean—and thus does not necessarily align with the magnitude of the score. Complete JF Model results appear in the supporting materials. 

The bootstrap simulated empirical null suggests that the theoretical null is, if anything, too conservative. When the calibrated observed distribution is superimposed on the simulated empirical null, its tail effects are even more pronounced (Figure 1.B). This result supports the inference of genuine non-null results in the JF Model data. 

An FDR analysis reinforces this conclusion. Indeed, none of the managers with | _z_ | ≥ 1.96 was deemed to be a false non-null. The FDR estimated proportion of non-null manager scores in the tail regions was over 80%. 

On the whole, the evidence supports the inference that the JF Model data contain a genuine manager signal. Select extreme performers, strong and weak, are identified in Figure 4. They are again reported as marginal impacts on the winning percentage of a .500 under an average manager. 

#### **4.4. The Hybrid Model** 

#### **4.4.1. Model specification.** 

The _Hybrid Model_ is—a hybrid. It is formed by combining the mWAR and JF Models, the two shown to register a manager signal loud enough to traverse the noisy space of chance that surrounds their respective data-estimation predictors: 





(6) 



19 

Here the outcome variable is again the probability that a particular manager will win a game in a particular season based on his team’s season winning percentage in that season. The fixed-effect predictor _μi_ remains the manager’s _career_ marginal impact on the probability of winning—this time after the sample-wide impact of both _zWPG_ and _zEXWP_ , the standardized team WAR and pre-season forecast variables, are controlled for. When those two team predictors are set to 0, the manager’s impact can again be estimated when the team is otherwise predicted to experience a .500 winning percentage under an “average manager.” 

#### **4.4.2. The convergent validity strategy** 

As mentioned, one goal of testing multiple prospective models was to mine their agreement for convergent validity. Unfortunately, lack of internal validity—its demonstrated inability to capture a manager signal different from what one would expect by chance—excludes the PE Model from contributing to this objective. But the JF and mWAR Models can still be united—generating the Hybrid Model—to achieve it. 

The external validity question is how to gain assurance that _what_ any prospective manager-value estimator is measuring is a latent trait of managerial skill and not something else. Combing the mWAR and JF Models promotes this aim. 

Even after strengthening the predictor for James’s original formula, the JF Model’s pre-season forecast predictor, z _EXWP_ , accounts for only a modest degree of variance in team records ( _R_<sup>_2_</sup> = 0.38). By itself, this degree of explanatory power would be insufficient to quiet anxiety that mangers were being awarded unearned credit for influences—such as team rejuvenation—spuriously correlated with their tenures. But this concern is substantially allayed by the addition of the player _zWPG_ , the mWAR model team predictor, which ramps up total _R_<sup>_2_</sup> to 0.75, a level of explanatory power that can generally be expected to filter out the lurking impact of omitted variables. 

Beyond reducing the scope for other, non-managerial influences to seep in, the Hybrid Model also takes specific aim at the most likely confounds to an inference of manager effect: the performance of players and the decisions of team management. When past performance and observed player achievement are simultaneously controlled for, these manager-independent effects largely cancel out. If a front office acquires better players—or fails to retain ones better than their replacements—this effect will be reflected in team WAR; thus, the inclusion of the WAR predictor offsets the risk that a manager will be credited with this form of front-office contribution to defying the push and pull of an AR(3) predictor. Likewise, nothing the front office does to affect the composition of the team can be expected to influence whether the team exceeds or falls short of the record predicted by the WARs of the players so assembled. Accordingly, there are good grounds to believe that it is neither the front office nor the players but the _manager himself_ who is responsible if one of these patterns _regularly_ occurs on his watch. 

Finally and most important is the level of agreement between the mWAR and JF Models. Already adverted to, the JF Model’s reliance on a relatively weak predictor— _zEXWP_ —risks inflating the impact of managers. This type of imprecision, however, does not necessarily rule out using it as an external validator. Indeed, this situation is a common one in the measure of latent variables: even when the measurement precision of alternative instruments is attenuated by their association with influences unrelated to the latent variable of interest, the _covariance_ of those instruments can support the inference that they are indeed measuring the same latent characteristic, _so long as_ they 



20 

derive from independent data sources. Such instruments can then be synthesized, amplifying one another’s signal and offsetting one another’s noise (Campbell & Fiske, 1959). 

The mWAR and JF Models fit the requirements for this strategy. The two Models overlapped significantly in their assessments of who the best—and worst—managers were. The correlation between the two under Kendall’s _W_ , the measure ordinarily used to assess the concordance of putative latent-variable indicators, was 0.72, a level conventionally regarded as indicating substantial agreement (Landis & Koch, 1977). 

Admittedly not as powerful as it could have been had the PE Model also survived preliminary screening and been able to contribute, the relationship and degree of affinity between the mWAR and JF Models still furnishes the sort of convergent validation that was sought by the testing of diverse models. They reflect independent data sources, supply independent support for an inference of genuine manager influence generally, _and_ they reflect substantial agreement on how that influence is distributed on an individual level. We cannot—and never will be able to—observe managerial influence directly to assure that the Hybrid Model formed by merging the mWAR and PE Models corresponds to it. But practical reason suggests it is much more likely that these independent metrics are measuring _that_ than that they are measuring other things that just happen to display this level of interrelationship with one another. 

#### **4.3.3. Analysis in relation to simulated empirical null** 

Of course, this gain presupposes the Hybrid Model inherits the indicia of systematic manager influence observed in its parent models. Again, an empirical null distribution was created via simulation. The process was the same one as used for both the mWAR and PE Models. That is, a parametric bootstrap was used to simulate 1,000 replicates of the season-level performances of the mangers’ teams had they been managed by an “average” manager; the full Hybrid Model, including manager fixed effects ( _μi_ ), was then fit to those same 1,000 careers’ worth of play; and the impact of the skill-free, “monkey” managers predicted when _zWPG_ and _zEXWP_ were set to zero. The result was an allocation of manager credit devoid of whatever influence the real-life, human managers had on their teams’ records. 

Forty-eight of the 495-member observed sample of managers—approximately 9.6%—generated impacts that met or exceeded that | _z_ | = 1.96 level. Were it evaluated against a conventional theoretical null standard (Figure 5.A), this outcome would be expected to occur by chance is about 1 in 80,500 trials. 

The strong signal of a systematic effect persists when the observed distribution is tested against the simulated empirical null. The average number of | _z_ | ≥ 1.96 was 24 across the 1,000 simulations, and none produced 48; only 4 reached 40 or more, the highest single number being 45. Figure 5.B juxtaposes the densities of the empirical and observed null distributions after calibration of the latter. 

FDR analysis supported the inference that the sample contained genuine non-nulls. All of the 30 managers who had calibrated | _z_ | scores ≥ 1.96 also had non-null probabilities over 50%. Thirteen of them were deemed to have non-null probabilities of over 70%. The Local False Discovery Rate for |z| _≥_ 1.96 was 0.36—indicating a 64% average probability that any sample member with a _z_ -statistic this extreme or more was a genuine rather than a false null. Like the results observed 



21 

under the mWAR and PE Models, the ones generated by the Hybrid Model denote a signal of genuine manager impact that persists after accounting for other material influences on team performance. 



**Figure 5. Observed Hybrid Model, theoretical null, and simulated empirical null distributions.** _Z_ -statistic distributions are presented to facilitate assessment of extremeness of observed sample values to a normal distribution and to the simulated empirical null distribution. Observed SEs determined by bootstrap. Panel (A) superimposes the observed Hybrid Model distribution on the theoretical null. Panel (B) superimposes the observe red distribution on the simulated empirical null distribution after calibration. The studentized test statistic for the observed sample was generated by parametric bootstrap  to conform to the empirical null and enable appropriate comparison (Templ, 2016; Davison & Hinkley, 1997). 

Because the Hybrid Model seeks to extract evidence of manager impact from the gap between expected and realized team performance, the Model presupposes the uniformity and stability of that gap over time. To establish whether this condition was satisfied, team winning percentages were regressed on _zWPG_ and _zEXWP_ alone. This test found that these two predictors consistently explained 80-85% of the variance in team records over the history of the American and National Leagues. The size of the residual left over for detection of manager effects, then, has itself not varied materially over this time. 

## **5. The Hybrid Estimator** 

The analysis so far has been meant only to form a defensible inference that the elements of the Hybrid Model correspond to a genuine signal of manager impact. That conclusion does not furnish any particular—or at least particularly useful—information about how much impact managers supply in general or whether any one of them generates a quantum of value of any practical import. 



22 



**Figure 6. Bayesian mechanics of Hybrid Estimator.** The Hybrid Estimator combines the manager prior, which is uniformly zero with the standard deviation _τ_ based on individual differences in skill, with the data, which is that manager’s own Hybrid Model score and associated measurement uncertainty, to arrive at a ^ posterior estimate of θ _i_<sup>, which is the manager’s personal latent skill estimate. The combining is generated via</sup> the Bayesian likelihood function. Here the values of the prior, the data, and the posterior are rendered in terms of the manager’s impact (positive or negative) on the number of season wins a .500 team, led by an average manger, would be expected to garner ( _w_ 162). 

That is what the _Hybrid Estimator_ is for. It is constructed with empirical Bayesian methods specifically fitted for this task. The same simulated empirical null distribution used to determine what random manager effects look like can anchor a _prior_ assessment and, combined with the calibrated sample distribution, a posterior estimate of a manager’s individual latent skill (Beasley & Rodgers 2012; Efron, 2004, 2012, 2024). The parametric bootstrap simulation makes it possible to disentangle individual-manager differences from measurement imprecision, enabling an estimate of how “true managerial skill,” _θ_ , is distributed within the manager population, as reflected in the variance measure _τ_<sup>_2_</sup> . The manager’s Hybrid Model score, and its standard error, form the _data estimate_ of his individual latent skill. That data estimate is then used to _update_ the empirical-null prior, generating a Bayesian _posterior_ estimate, which itself takes the form of a probability distribution (Figure 6). 

The most likely value of the estimate—the _maximum a posteriori_ or MAP—is the Hybrid Estimator ^ value of the manager’s true skill level, θ _i_<sup>. It can be expressed either in terms of a manager’s marginal</sup> impact on the winning percentage of what would otherwise be a .500 team or, more accessibly, an estimate of the number of additional season wins (positive or negative) that such a team would experience under his direction as opposed to that of an “average manager.” The latter formulation of ^ θ _i_<sup>will be referred to as a manager’s</sup><sup>_w_162.</sup> 

A select list of the managers with the 32 highest and 28 lowest _w_ 162s in AL/NL history appears in Table 3. In addition the table also indicates 0.95 HDIs or Bayesian “Credible Intervals”: these 



23 

identify the densest portion of the manager’s estimated posterior mass containing 95% of its values. The posterior mass encodes uncertainty about _θi_ . It can be viewed as either a degree of “belief” (confidence) in the value of _θi_ , pending any future installment of data, or as the distribution of all ^ the estimated values of θ _i_<sup>and their associated probabilities. Additional</sup><sup>_w_162</sup> summaries—including ones of Hall of Fame Managers and of currently and recently active ones—appear in the Appendix. 

Table 3 also reports the _data_ scores—that is the Hybrid _Model_ estimates for the managers. The discrepancies between these and managers’ _w_ 162s reflect how much the Model scores were “shrunk” or discounted toward the prior estimate of zero effect. Managers who consistently out- or under-performed the mean over relatively long careers retained 65%-70% of their data scores. But many of the Table 3 managers’ raw Model estimates were shrunk by 50% or more. The _w_ 162 scores are uniformly much lower than the ones generated by either the mWAR or JF Models. This feature of the Estimator, and the pervasive re-ranking of managers it entailed relative to the raw Model scores, demonstrate how heavily Bayesian updating penalizes the individual Model estimates as a result of the prior, between-manager variance ( _τ_<sup>_2_</sup> ), and within-manager measurement precision. 

The Table 3 scores include ones at the tails of the overall _θ_ distribution _._ John McGraw’s _w_ 162 of 5.1 (a marginal winning-percentage probability of .031) is _4.9_ SDs from the mean. A | _w_ 162| ≥ 3 is extremely rare—it occurs in less than 2% of the ample. About 72% of the 495 managers in the sample had _w_ 162s between -1.0 and 1.0, and 60% between -0.5 and 0.5. 

Summaries of this sort, and in particular the precision with which they are formed, help to gauge the mechanics and appraisals of the Estimator but leave open the question of whether the differences being detected establish a meaningful impact for managers overall and meaningful differences in their individual levels of skill. To answer that question, a reflective judgment must be made about how large an impact must be before it is viewed as meaningful. Once that judgment has been made, the Estimator can be used to apply it. 

To illustrate, the individual-manager _w_ 162 scores were assessed in relation to a _consequence threshold_ of ± 0.012 marginal-win probability—the equivalent .488 and .512 for a .500 team, or _2_ wins or losses in a conventional 162 game schedule. On this analysis, then, _w_ 162 skill levels between -2 and 2 are lumped together as the effect of an “average manager. 



24 

|**manager**|_H_<br>**G**|_ighest w1_<br>**W%**|_62s_<br>**w162**|**HDI95**|**data**||**manager**|_Lowest w1_<br>**G**|_62s_<br>**W%**|**w162**|**HDI95**|**data**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|<br>1<br>John McGraw|4439|.590|5.1|(3.0, 7.2)|7.1|494|<br>Jimmy McAleer|1623|.452|-3.4|(-6.4, -0.4)|-7.8|
|2<br>Frank Chance|1593|.594|4.4|<br>(1.5, 7.2)|8.8|494|<br>Cito Gaston|1726|.516|-3.4|<br>(-6.2, -0.6)|-6.4|
|3<br>Fred Clarke|2251|.596|3.8|<br>(1.1, 6.5)|6.8|492|Eric Wedge|1587|.476|-3.1|<br>(-5.9, -0.3)|-6.1|
|4<br>Joe McCarthy|3426|.615|3.2|(0.9, 5.5)|4.7|492|Joe Cantillon|455|.347|-3.1|(-6.6, 0.5)|-14.4|
|5<br>Felipe Alou|2050|.503|3.1|(0.5, 5.8)|5.5|491|John Gibbons|1580|.501|-2.9|(-5.7, 0.0)|-5.7|
|5<br>Al Lopez|2414|.584|3.1|(0.5, 5.6)|5.1|490|Patsy Donovan|1305|.425|-2.7|(-5.8, 0.4)|-6.9|
|<br>7<br>Pat Moran|1334|.561|2.8|<br>(-0.2, 5.7)|6.0|488|<br>Jimmie Wilson|1227|.402|-2.6|<br>(-5.6, 0.4)|-6.0|
|8<br>Casey Stengel|3732|.509|2.5|<br>(0.2, 4.8)|3.7|488|Bobby Bragan|921|.481|-2.6|<br>(-5.7, 0.6)|-6.8|
|9<br>Wilbert Robinson|2827|.499|2.4|(0.0, 4.9)|3.8|486|Jimy Williams|1697|.535|-2.5|(-5.3, 0.3)|-4.7|
|10<br>Craig Counsell|1653|.532|2.3|(-0.5, 5.1)|4.4|486|Lee Fohl|1505|.474|-2.5|(-5.3, 0.4)|-5.0|
|11<br>Pete Rose|780|.526|2.2|(-1.1, 5.5)|6.5|485|Ned Hanlon|1018|.450|-2.4|(-5.7, 0.9)|-7.4|
|12<br>Danny Ozark|1160|.533|2.1|<br>(-0.9, 5.2)|5.0|484|Doc Prothro|458|.301|-2.3|<br>(-5.9, 1.3)|-11.6|
|<br>12<br>Bruce Bochy|4350|.498|2.1|<br>(0.1, 4.2)|2.9|483|Doug Rader|805|.482|-2.2|<br>(-5.4, 1.1)|-6.3|
|<br>12<br>Stephen Vogt|323|.557|2.1|<br>(-1.6, 5.7)|11.9|481|<br>Fred Haney|1376|.456|-2.1|<br>(-5.1, 0.8)|-4.6|
|<br>15<br>Fredi González|1411|.507|2.0|<br>(-0.9, 4.9)|4.3|481|<br>Bobby Wallace|216|.287|-2.1|<br>(-5.9, 1.7)|-20.1|
|15<br>Cecil Cooper|344|.506|2.0|<br>(-1.7, 5.6)|10.7|478|<br>Tom Kelly|2375|.478|-2.0|<br>(-4.6, 0.5)|-3.4|
|17<br>Steve O'Neill|1859|.558|1.9|(-0.8, 4.6)|3.5|478|Lou Piniella|3524|.517|-2.0|(-4.2, 0.2)|-2.8|
|17<br>Dave Roberts|1516|.619|1.9|(-1.0, 4.8)|3.9|478|Johnny Oates|1539|.517|-2.0|(-4.8, 0.9)|-3.9|
|19<br>Paul Richards|1819|.506|1.8|<br>(-0.9, 4.5)|3.4|472|<br>Billy Meyer|764|.412|-1.8|<br>(-5.1, 1.5)|-5.7|
|19<br>Dusty Baker|4016|.539|1.8|<br>(-0.4, 3.9)|2.5|472|<br>Bob Geren|714|.475|-1.8|<br>(-5.2, 1.5)|-5.8|
|19<br>Frank Selee|633|.555|1.8|(-1.9, 5.4)|9.5|472|John McCloskey|457|.333|-1.8|(-5.4, 1.8)|-8.6|
|22<br>Buddy Black|2583|.460|1.7|(-0.8, 4.2)|2.7|472|Chuck Tanner|2733|.495|-1.8|(-4.2, 0.6)|-2.8|
|22<br>Jim Tracy|1738|.493|1.7|(-1.1, 4.4)|3.2|472|Mike Hargrove|2343|.504|-1.8|(-4.3, 0.8)|-2.9|
|22<br>Clint Hurdle|2595|.486|1.7|(-0.8, 4.1)|2.7|472|Frank Quilici|567|.494|-1.8|(-5.2, 1.7)|-6.4|
|25<br>Joe Gordon|613|.498|1.6|<br>(-1.9, 5.2)|7.3|468|<br>Tony Muser|763|.421|-1.7|<br>(-5.0, 1.6)|-5.3|
|25<br>Bobby Cox|4490|.555|1.6|<br>(-0.4, 3.7)|2.2|468|<br>Dan Howley|921|.431|-1.7|<br>(-4.9, 1.5)|-4.7|
|<br>25<br>George Stallings|1586|.501|1.6|<br>(-1.3, 4.5)|3.3|468|<br>Alan Trammell|498|.382|-1.7|<br>(-5.2, 1.8)|-7.5|
|<br>25<br>Tony LaRussa|5356|.535|1.6|<br>(-0.3, 3.5)|2.1|468|Deacon McGuire|429|.441|-1.7|<br>(-5.3, 1.9)|-7.8|
|<br>25<br>Chuck Dressen|1992|.509|1.6|<br>(-1.1, 4.3)|2.9||||||||
|25<br>Kirk Gibson|730|.485|1.6|<br>(-1.7, 4.9)|5.0||||||||
|25<br>Red Dooin|762|.514|1.6|<br>(-1.7, 4.9)|4.8||||||||
|25<br>Hank O’Day|307|.498|1.6|<br>(-2.1, 5.2)|9.4||||||||
|<br>25<br>Mike Shildt|775|.561|1.6|<br>(-1.7, 4.9)|4.7||||||||
|25<br>George Gibson|757|.546|1.6|(-1.7, 4.8)|4.7||||||||



^ **Table 3. Best and worst Hybrid Estimator** **_w_ 162s.** List combines top and bottom 25 in _w_ 162 scores, which reflect the MAP estimates of individual ∅ _i_<sup>s,</sup> expressed in these terms. “G” is career games; “W%” career winning percentage; “HDI” the densest (and hence most likely) portion of the manager’s 



25 

posterior mass that includes 95% of the manager’s _w_ 162 distribution; and “data” the manager’s Hybrid Model _w_ 162 score prior to Bayesian updating. Additional compilations, including ones for all Hall of Fame managers and for currently or recently active ones, appear in the Appendix. 



26 

This form of bracketing is conventionally referred to as ROPE—or “region of practical equivalence”—testing (Kruschke, 2018). Using any manager’s posterior mass, it is possible to calculate the probability that his “true managerial value” falls outside the | _w_ 162| > 2 region (Figure 7). Were an analyst of the belief that the consequence threshold should be either higher or lower, he or she could adjust the _w_ 162 ROPE accordingly. All the information necessary to set a threshold of | _w_ 162| > 1.6, | _w_ 162| > 2.5, or any other value, and to determine the probability that a particular manager satisfies it, can be gleaned from the managers’ posterior means and variances (included in the supporting materials). 

Applied to individual managers, the | _w_ 162| > 2 ROPE threshold is a highly selective one. Only 34 of the managers in the 495-member sample—approximately 7%—have career scores that meet it, 16 on the positive side and 18 on the negative. Just 19 of them (4%), moreover, exceed the threshold (in either direction) with a 60% probability, as measured by the fraction of their posterior masses that exceed the outer edge of the ROPE on one side or the other. If one were to treat | _w_ 162| > 2 as the correct threshold for a genuine managerial impact, then one might conclude that such an effect exists but is rare. 



<!-- Start of picture text -->
^<br><!-- End of picture text -->

^ **Figure 7. Individual manager ROPEs** . Densities reflect identified managers Hybrid Estimator θ _i_<sup>s expressed</sup> in terms of wins added per 162 games ( _w_ 162). Fraction of the density outside the shaded region represents the probability that the manager in question exceeds the boundary of the region of practical equivalence in the relevant direction. 



27 

But it is actually not as rare as it might seem. Here the Estimator is being used to estimate _θ_ for individual managers. Only a small fraction of managers might possess posterior masses 51% or more of which lie outside | _w_ 162| > 2 ROPE. But many of the remaining managers still have _some_ non-zero probability of falling outside it (consider Figure 7); accordingly, it is quite likely that there will be additional _unidentified_ managers with _θ_ s outside | _w_ 162| > 2. Thus, rather than flagging individual managers 51% of whose posterior masses fall outside | _w_ 162| > 2, the Estimator can _integrate_ over the sum of every manager’s probability of lying outside that region. The result is the _expected sample-wide number_ with true | _w_ 162| > 2. Here that total is 162: 85 with _w_ 162 ≤ -2 and 75 with _w_ 162 ≥ 2. This is roughly _one-third_ of the sample as a whole (Figure 8). 

The gap between the number of specific individual managers identified as outside the | _w_ 162| > 2 ROPE and the sample-wide incidence of that level of _θ_ creates a practical difficulty for those (GMs, gamblers, professional prognosticators) seeking to use the Estimator to make decisions. Should they be guided only by the Estimator’s ratings of individual managers when making judgments of consequence? If they adopt this stance, they will necessarily be excluding from their consideration a potentially much larger number who genuinely possess the level of skill (or ineptitude) that they regard as consequential. But if in response such users expand the zone of consideration, they must endure a correspondingly higher risk of error in individual cases. What is the optimal balance of these considerations? 



<!-- Start of picture text -->
θ .<br><!-- End of picture text -->

**Figure 8. Sample wide distribution of** **_θ_ .** Derived by integrating over the posterior of the sample as a whole, the curve reflects the sample probability density distribution of _θ_ expressed in _w_ 162. The areas on either side of the gray band constitute the portions of the distribution outside of - 2 ≥ _w_ 162 ≤ 2. Approximately 15% of the sample would be expected to have _w_ 162 ≥ 2, and 17% ≤ -2. 

This dilemma highlights that constructing a valid estimator does not in itself reveal the most effective means of using it. Essential to making this transition is to identify the performance characteristic of the Estimator responsible for this predicament. Once that feature of the Estimator is identified, it will be seen how the information-assessment machinery of the Estimator can itself be used to surmount it.<sup>3</sup> 

3 To test the robustness of these estimates, the Hybrid Estimator scores were also calculated by hierarchical Bayesian regression in which the managers were modeled as random intercepts. The 



28 

## **6. Operationalizing Hybrid** 

#### **6.1. The Hybrid Estimator learning curve** 

The Hybrid Estimator rates managers on their career performances, in toto or to date. A manager’s _score_ is not cumulative; the _scoring_ of it is. That is, each season’s performance is treated as data for updating the model’s prior estimate of _θi_ , which is presumed to correspond to a stable unobserved quality. 



**Figure 9. Select** **_w_ 162 measurement histories.** Gray bands reflect 0.67 HDI estimation of indicated manager’s _w_ 162 at number of games managed. 

This updating can be expected to converge and (in the vast majority of cases) stabilize on a particular value (Figure 9), but the process necessarily takes time. There is variability in how much: in only two seasons, for example, the Guardians’ current manager John Vogt has climbed to a _w_ 162 of 2.1; it took approximately 22 seasons for the model to recognize Casey Stengel possessed a _w_ 162 score equal to that (albeit with a much tighter posterior probability distribution). But reasonable generalizations are possible. The median number of games it took the Estimator to recognize that a 

two versions of the Hybrid Estimator generated _i_ estimates of highly concordant magnitudes (Lin’s CCC = 0.97) and were in near perfect agreement (Kendall’s _W_ =0.99) on the relative skill of different managers. More details appear in the Appendix. 



29 

manger had a | _w_ 162| of ≥ 2 was 810 games, roughly 5 seasons. To determine that he possessed a posterior mass 70% of which included that level of _θ_ or higher, the median number of games was about eight seasons worth—131. The number of games for determining such a manager’s attainment of intermediate benchmark _w_ 162 scores are reported in Figure 10. 



**Figure 10. Hybrid Estimator learning curve for career |** **_w_ 162** | **≥ 2 managers.** Top and bottom panels plot the number of games required for managers with career | _w_ 162s| ≥ 2 to reach MAP _w_ 162 = |1.0|/|1.5|/|2.0| and _w_ 162 with 0.70 posterior masses at those values respectively. For details on how the Estimator’s updating speed was determined, see the Appendix. 

Those studying baseball history are unlikely to find the pace of Hybrid Estimator’s learning curve to be problematic, but users who are making decisions in real time might. They will often want to make assessments within time frames more compact than those likely to yield stable estimates of θ _i_ , particularly for mangers early in their careers. 

Moreover, it turns out that this same characteristic of the Estimator—its learning curve—is the source of the divide between individual and population estimates of θ. For every season’s worth of 



30 

data, the Estimator learns more about the population distribution of θ than it does about individual θ _i_ s. When the day comes in which the Estimator acquires an infinite amount of data, that gap will disappear. But until then (i.e., forever), the number of manages it can identify as having | _w_ 162| > 2 will always fall short of the total number of managers who possess that level of skill. 

By now, the objective for maximizing the practical use of the Estimator should be clear: the development of strategies for effectively accelerating the speed with which the information it generates can profitably be relied on. The information machinery used to run the Hybrid Estimator, it turns out, can be used to devise strategies of exactly that sort. 

#### **6.2 Hybrid Estimator p_** 

The first such strategy adapts the Hybrid Estimator into a season-level estimator: the provisional “Hybrid Estimator p._ ” The Estimator p_ assigns managers the average manager share of the difference between their teams’ actual and expected wins. 

Expected wins are computed using _zEXPWP_ and _zWPG_ , the two non-manager predictors in the Hybrid Model (6). When the Hybrid Estimator scores are then added to this non-manager or base model, it is possible to calculate how much of the difference between actual and expected team wins is due to manager influence. It turns out that the Hybrid Estimator scores increase the _R_<sup>_2_</sup> of the base model from 0.80 to 0.84—a team winning percentage RMSE of .040. The residual between expected and realized team winning percentages is often chalked up to “good” or “bad luck” (Birnbaum, 2005). But the Hybrid Estimator indicates that 20% of what team-performance variables fail to explain is, on average, the team manager’s doing. 

The Hybrid Estimator p_ , then, simply takes this fraction of a team’s residual under the base model in any season and imputes it to the team’s manager. So if a team, for example, won five more games than expected under the _zEXPWP_ and _zWPG_ base model, its manager would be credited with one win; if it won five fewer, he would be charged one loss.<sup>4</sup> 

The season-level scores are meaningful—they are the raw material from which the full Hybrid Estimator scores are constructed—but they differ from the full Estimator scores in two important ways. First, the Estimator p_ scores are innocent of any prior and devoid of any posterior. The same residual between team expected and realized performance is fed into both the provisional and the full Estimators. But because the latter is Bayesian, it combines this information with a prior estimate of a manager’s innate skill to form a posterior one. The season-level Estimator p_ score reflects only the data of a particular season (Figure 6). 

Second, the Estimator __p_ score is ignorant of how any particular season’s data relate to those of others. The Hybrid Model (6) uses information from every season of every individual who has managed an American or National League team. Its _μi_ estimate incorporates the covariances of _both_ a manager’s performance in one season with his performance in every other season _and_ that manager’s season performances with every other manager’s across all of major league history. That covariance information necessarily plays no role in the “raw” residual dividends distributed by Estimator p_ . Indeed, that is exactly why they are based on a uniform rate. 

4 Exact instructions on how to calculate manager scores using the provisional Hybrid Estimator can be found in the Appendix. 



31 

The scores under Estimator __p_ are akin to ones that would be generated by a season-level maximum likelihood variant of the Hybrid Model—but with one important advantage. Like the Estimator p_ , a single-season MLE version of the Hybrid Model would allocate manager credit based on the residuals of the team WAR and AR(3) forecast predictors. But unlike the provisional model, the magnitude of “manager wins” and “losses” under this MLE variant would depend decisively on the estimated aggregate effect of managers on team performances for _that one season_ . The Hybrid Model appropriately recognizes that _μ,_ the aggregate manager effect, is a random variable; it partitions individual manager influence (the full Estimator data signal) in relation to the estimated size of _μ_ over all seasons. The provisional Estimator __p_ is cognizant of this information, too. By assigning managers only 20% of the residual under the base model, the provisional Estimator effectively shrinks what would have been the single-season MLE estimate of manager influence toward its historical mean. 

The estimations of single-season manager effects under the Estimator __p_ are sensible on their face. That is to say, in part, that they are modest—much more so, certainly, than the ones of a system that assigns to managers the _entire_ effect of what’s left over after team performance is accounted for (e.g., Jaffe, 2010; James, 1997, pp. 149-152). Applied over the course of major league history, the largest manager season impacts—wins or losses—are just over four. The number of manager losses at the 10th percentile is - 1.2, and wins at the 90th 1.2. Impacts of -2 and 2 occur at the 2.5 and 97.5 percentiles, respectively. These totals are reasonably in line with those associated generated by the full Hybrid Estimator—although again, they are more akin to the data in Bayesian terms than to posterior estimates, which are shrunk by the full Estimator. 

They are also reliable. That said, user goals will be heterogeneous. Users with a practical stake in shaping or predicting team performance will attach significant value to the greater discernment of the full Estimator. But ordinary fans, and the outlets who serve them, are likely to be more interested in making comparative assessments of manager performance season over season; _this is not what the full Hybrid Estimator produces_ —it is designed to estimate a stable, unobserved skill level, using season performance as data only. For that reason, the Hybrid Estimator __p_ might actually furnish a better fit than the full Estimator for pure entertainment assessments of the sort that figure in on-line and media “leader boards.” 

#### **6.3. Calibration for decision-theory loss functions** 

The second strategy for addressing the Hybrid Estimator’s learning curve speaks directly to the dilemma posed by the disparity between the Estimator’s individual and population-incidence estimates of _θ_ (Figure 7, Figure 8). The strategy involves adjustment of the Estimator loss function. 

The Hybrid Estimator uses Bayesian statistical methods because they dominate alternatives in predictive error reduction. They achieve this result by optimizing the tradeoff between bias and variance, accepting slightly more of the former in order to reduce the latter by an amount that generates more predictive accuracy on net (Efron & Morris, 1973, 1977). Mathematicians often say that Bayesian estimators thus have the lowest “loss function,” meaning that their point-estimate MAPs miss the predictive target by the smallest margin, measured in terms of mean squared error or MSE (James & Stein, 1961). 

presents the Estimator __p_ scores for the last two seasons. The rankings across the seasons display a substantial level of agreement (Kendall’s _W_ = 0.65). Three managers finished in the top six in both seasons; the same one finished last in both. Stephen Vogt topped the list in both 2024 and 2025. 



32 

Tracking Vogt’s unusually rapid acquisition of a _w_ 162 score ≥ 2 (Table 3), this result fortifies the conclusion that the Hybrid Estimator __p_ can reasonably be relied upon pending accumulation of a more robust assessment of a manager’s latent skill via the full Hybrid Estimator. 

|**season**|**Manager**|**Team**|**_w_162****_p_**|**season**|**Manager**|**Team**|**_w_162****_p_**|
|---|---|---|---|---|---|---|---|
|2024|Stephen Vogt|CLE|2.0|2025|Stephen Vogt|CLE|2.6|
|2024|Buddy Black|COL|1.7|2025|Ron Washington|LAA|1.4|
|2024|Oliver Marmol|SLN|1.3|2025|A. J. Hinch<br>Clayton|DET|1.4|
|2024|A. J. Hinch|DET|1.2|2025|McCullough|MIA|1.3|
|2024|Carlos Mendoza|NYN|1.1|2025|Oliver Marmol|SLN|1.0|
|2024|Mike Shildt|SDN|0.9|2025|John Schneider|TOR|1.0|
|2024|Derek Shelton|PIT|0.5|2025|Dave Martinez|WAS|0.7|
|2024|Craig Counsell|CHN|0.3|2025|Miguel Cairo|WAS|0.6|
|2024|Bob Melvin|SFN|0.3|2025|Bob Melvin|SFN|0.3|
|2024|Dave Martinez|WAS|0.3|2025|Mark Kotsay|OAK|0.3|
|2024|Bruce Bochy|TEX|0.2|2025|Dan Wilson|SEA|0.3|
|2024|Torey Lovullo|ARI|0.2|2025|Terry Francona|CIN|0.2|
|2024|Pat Murphy|MIL|0.2|2025|Pat Murphy|MIL|0.2|
|2024|Dave Roberts|LAN|0.2|2025|Dave Roberts|LAN|0.1|
|2024|Scott Servais|SEA|0.1|2025|Brandon Hyde|BAL|0.0|
|2024|David Bell|CIN|0.0|2025|<br>Buddy Black|COL|0.0|
|2024|Matt Quatraro|KCA|0.0|2025|Tony Mansolino|BAL|0.0|
|2024|Dan Wilson|SEA|0.0|2025|Mike Shildt|SDN|0.0|
|2024|John Gibbons|NYN|0.0|2025|Warren Schaeffer|COL|-0.1|
|2024|Rickie Weeks|MIL|0.0|2025|Matt Quatraro|KCA|-0.1|
|2024|Paul Hoover|KCA|0.0|2025|Craig Counsell|CHN|-0.2|
|2024|Rocco Baldelli|MIN|0.0|2025|Derek Shelton|PIT|-0.3|
|2024|Aaron Boone|NYA|0.0|2025|Aaron Boone|NYA|-0.4|
|2024|Brandon Hyde|BAL|0.0|2025|Joe Espada|HOU|-0.5|
|2024|Skip Schumaker|MIA|-0.1|2025|Alex Cora|BOS|-0.7|
|2024|Grady Sizemore|CHA|-0.1|2025|Bruce Bochy|TEX|-0.7|
|2024|Kevin Cash|TBA|-0.2|2025|Torey Lovullo|ARI|-0.8|
|2024|Joe Espada|HOU|-0.5|2025|Will Venable|CHA|-0.8|
|2024|<br>John Schneider|TOR|-0.8|2025|Rob Thomson|PHI|-0.8|
|2024|Mark Kotsay|OAK|-0.9|2025|Don Kelly|PIT|-0.9|
|2024|<br>Rob Thomson|PHI|-0.9|2025|<br>Rocco Baldelli|MIN|-1.0|
|2024|Ron Washington|LAA|-1.0|2025|Kevin Cash|TBA|-1.1|
|2024|Pedro Grifol|CHA|-1.1|2025|Carlos Mendoza|NYN|-1.2|
|2024|Alex Cora|BOS|-1.2|2025|Brian Snitker|ATL|-1.6|
|2024|Brian Snitker|ATL|-1.2|||||



**Table 4. 2024-2025** **_w_ 162** **_p_ scores.** Hybrid Estimator __p_ estimates in wins above average per 162 games ( _w_ 162 _p_ ) for managers in 2024-2025 seasons. For partial seasons, _w_ 162 _p_ score is pro-rated to proportion of team-games managed. 

What makes the Hybrid Estimator __p provisional_ is the expectation that it will be supplanted by the full Hybrid Estimator after a sufficient number of games. The Estimator __p_ ’s rapid, data-based assessment of manager ability makes it a sensible strategy for mitigating the inconvenience of the full Estimator’s deliberate learning curve. But ultimately the full Estimator’s Bayesian machinery is required to connect season-by-season data to a latent quality of managerial acumen. Those 



33 

interested in making accurate appraisals of this deposition will thus want to switch to reliance on the full Hybrid Estimator score for guidance as soon as feasible. 

That said, user goals will be heterogeneous. Users with a practical stake in shaping or predicting team performance will attach significant value to the greater discernment of the full Estimator. But ordinary fans, and the outlets who serve them, are likely to be more interested in making comparative assessments of manager performance season over season; _this is not what the full Hybrid Estimator produces_ —it is designed to estimate a stable, unobserved skill level, using season performance as data only. For that reason, the Hybrid Estimator __p_ might actually furnish a better fit than the full Estimator for pure entertainment assessments of the sort that figure in on-line and media “leader boards.” 

#### **6.3. Calibration for decision-theory loss functions** 

The second strategy for addressing the Hybrid Estimator’s learning curve speaks directly to the dilemma posed by the disparity between the Estimator’s individual and population-incidence estimates of _θ_ (Figure 7, Figure 8). The strategy involves adjustment of the Estimator loss function. 

The Hybrid Estimator uses Bayesian statistical methods because they dominate alternatives in predictive error reduction. They achieve this result by optimizing the tradeoff between bias and variance, accepting slightly more of the former in order to reduce the latter by an amount that generates more predictive accuracy on net (Efron & Morris, 1973, 1977). Mathematicians often say that Bayesian estimators thus have the lowest “loss function,” meaning that their point-estimate MAPs miss the predictive target by the smallest margin, measured in terms of mean squared error or MSE (James & Stein, 1961). 

But this understanding of “loss” reflects an understandably statisi-centric outlook. Conventional Bayesian estimation most effectively reduces loss _if_ what one is trying to maximize is accuracy simpliciter. 

A user of a Bayesian estimator, however, might be trying to maximize something that does not perfectly align with error reduction in this sense (Berger, 1985). This situation is especially likely to be true where the user disvalues certain errors more than others, either because of their asymmetric costs or because of the users risk preferences (Elliott & Timmermann, 2008, 2016; Patton & Timmermann, 2007).Whether to retain a manager might fall into this class. Both good and bad managers can be consequential, the analyses so far confirms. But managers who are _consequentially_ good or bad are rare; they make up a smaller than normal fraction of the overall manager population, whose ranks are bloated by managers of average ability. 

The practical upshot of this distribution of latent managerial ability arguably supports viewing errors in manager retention as asymmetric. On this account, holding on too long to a potentially poor manager is more costly than releasing and replacing him prematurely. The former mistake results in palpable costs for the team. In contrast, the most likely effect (by far) of the latter mistake is the substitution of one average manager for another: allowed more time, the prematurely released manager would most likely have proven himself to be average in ability—which is the most likely value of his replacement as well. 

The opposite is true at the other end of the spectrum. That is, prematurely replacing a potentially good manger is worse than holding on to him too long. The former mistake costs the team the 



34 

services of the rare manager who would have netted them additional wins. The latter mistake, in contrast, is most likely to be costless or nearly so: the manager who fails to rise to the ranks of the elite will most likely be revealed as average; and again, average is the expected value of any replacement. 

This asymmetry can be amplified by the tournament structure of baseball-revenue distribution. Hitting a threshold in wins can result in outsize returns associated with post-season playoff berths; the incremental cost of additional losses when teams fall short of that threshold are close to zero (Gennaro, 2013). Under this “winner,” or select winners, “take all” payout system (Frank & Cook, 1996), teams can be expected to adopt toward manager hiring and retention a stance that is risk-preferring with respect to wins and risk-averse with respect to losses (Becker & Huselid, 1992; Lee & Lee, 2004). That is, they will quickly dispense with the services of a potentially poor manager, but stick it out—take a flier—on the manager they perceive to have a high but as-yet unrealized upside. 

This pattern—risk aversion toward poor performers, risk preference toward relatively neutral ones—is familiar in corporate management retention. Econometricians have long observed that boards do not process information in a purely Bayesian fashion (understood in MSE terms) but instead react more quickly to evidence that a CEO is performing worse than average than they do to evidence that a CEO is not performing _above_ average (Jenter & Lewellyn, 2021). One explanation is that the costs of failing to heed the former class of information exposes firms to greater risks, and denies them smaller opportunities for potential upside gain, than failing to heed the latter. 



**Figure 11. Effect of asymmetric error-cost loss function.** The panels demonstrate the impact of substituting for a uniform MSE-reduction error function a quadratic asymmetric error-cost one. The latter marks out two thresholds— _w_ 162 -2.0 an _w_ 162 2.0—beyond which type II error costs are treated as 100% (2x) more costly than type I. Panel (A) illustrates the changes in estimated _w_ 162s that minimize error costs; red observations are managers whose penalty-adjusted _w_ 162s change from > -2 to ≤ -2 or from < 2 to ≥ 2. Panel (B) illustrates the magnitude of revised _w_ 162 scores; again red observations are managers whose penalty-adjusted _w_ 162s change from > -2 to ≤ -2 or from < 2 to ≥ 2. As can be seen, however, the scores of managers are re-assessed across the entire posterior, generating adjusted _w_ 162s even at points relatively remote from the error-cost thresholds. See the Appendix for details on the formal characteristics of the loss function that generates these effects. 

The distinction between error reduction simpliciter and optimal decision-making generally can be straightforwardly addressed. To handle it, a Bayesian estimator can be calibrated to a _decision theory loss function_ that maximizes utility in terms of the user’s choosing (Berger, 1985). 



35 

The Hybrid Estimator can be adjusted in exactly this way. Figure 11 illustrates how recalibrating the Estimator to reflect the front-office loss function described above would alter the Estimator’s assessments of manger latent skill. In it, the Estimator has been programmed to treat errors asymmetrically. Erroneously under-estimating a manager who _does_ have a true _w_ 162 ≥ 2—that is, short-changing him, and assigning him a _w_ 162 < 2—is _two times more costly_ than erroneously identifying him as a manager who _does_ possess a _w_ 162 ≥ 2 when he does not. The same for a manager who has a true w162 ≤ -2: the penalty is two times more severe for incorrectly scoring him as possessing a _w_ 162 > -2 than vice versa. 

When the Estimator is made to respect this loss function rather than an MSE one, it adjusts the _w_ 162 score of every manager in accord with the resulting expected error cost, as determined by both the size of the penalty and the fraction of his posterior mass that crosses either of the two asymmetric error thresholds. This operation doesn’t just arbitrarily change the w162s of a handful of managers who otherwise would fall just short of the upper threshold or just barely exceed the lower one. Rather it nudges some closer to the critical thresholds; pushes some others across one or the other; and relocates still additional managers, ones with posterior means only marginally higher than |w162| ≥ 2, even father out of harm’s way. It should be noted, though, that the impact is not uniform or monotonic; the degree to which _w_ 162s are recomputed is conscious of the information in variance levels unique to individual managers. The result is a picture of manager skill level comprehensively redrawn to match the user’s own view of utility. More information on the formal properties of this loss function and how the Hybrid Estimator was adjusted to implement it can be found in the Appendix. 

Adjusting the Hybrid Estimator loss function, it can be seen, helps ameliorate the impact of the Estimator’s deliberate learning curve. Where a user identifies particular errors as more costly than others, a responsive adjustment of the Estimator accelerates the _speed_ at which it identifies managers as possessing _w_ 162s of consequence. By the same token, substituting a decision-theory loss function for an MSE-reduction one can reduce the period of time during which it is necessary (or warranted) to rely on the provisional, Estimator p_ alternative to the full Estimator. 

Adoption of this adjusted loss function is also responsive to the dilemma associated with the gap between individual-level estimates and the manager-population estimates of _θ_ (Figure 7, Figure 8). As discussed, the gap is a direct consequence of the difference in the speed at which the Hybrid Estimator acquires information about the population of managers, on the one hand, and the speed about which it acquires information about individual managers, on the other. This disparity implies that there is a rich vein of talent in the vicinity of the _w_ 162 ≥ 2 cutoff. Accordingly, adjusting the Estimator’s MSE-minimization default near that threshold will maximize the probability that those with true w162 ≥ 2.0 are not passed over. 

Necessarily it also tolerates a greater level of risk that managers will be incorrectly identified as harboring that level of skill. But because the most likely cost of that error—the retention of a manager with an average _θ_ –is the most likely outcome if he is replaced by another manager; and because the tournament-structure of payoffs for surplus wins generates a rational preference for risk-taking on managers with an as-yet unrealized potential for higher-than-average latent skill, a utilitarian loss function of this kind dominates the MSE-minimization one that guides the full Hybrid Estimator when run without adjustment (Elliott & Timmermann, 2016). 

Or at least it might. Whether to make such an adjustment, and how much risk of error to tolerate in exchange, are matters of judgment—ones that should be informed by still more empirical analysis. 



36 

_Any_ utility-maximizing loss function identified in this manner can be substituted for the default MSE-minimization one that guides the Estimator’s updating function. The amenability of the Hybrid Estimator to a user-defined decision-theory loss function magnifies what users can learn about manager potential, especially early on in their careers. 

## **7. Conclusion: Not** **_whether_ managers make a difference but** **_how much more_ they could** 

So do mangers matter today? Did they ever? 

The answers are yes, and yes. 

This study systematically investigated the properties of alternative, data-driven manager-value models. One of these—the Pythagorean Expectation Model—was revealed to be invalid because it transmits no genuine signal of manager talent. But two others—the mWAR and Jamesian Forecast Models—did transmit such a signal. They were combined to form the Hybrid Model, which was in turn used as the data source for a Bayesian manager-value estimator. Capable of discerning differences in latent managerial skill, the Hybrid Estimator found that a sizable fraction of the managerial population—in the vicinity of one-third of it (Figure 8)—has over the history of the American and National Leagues generated ± 2 wins per season to their teams’ performances over and above the contribution made by those teams’ players. 

The manager impact that the Hybrid Estimator detected, moreover, was not peculiar to any particular era. Mangers of consequence—positive and negative—are found over all MLB time periods. This includes a cohort of active and recently active managers whose careers started _concurrently with_ or well _after_ with the advent of modern analytics (including Fredi González, Craig Counsel, David Roberts, Bruce Boche, and Craig Vogt). 

Just as important, it was shown that the Hybrid Estimator admits of ready use for practical decisionmaking. It can detect reliable indications of greater- and below-average latent managerial skill within several seasons. Moreover, the information it yields can be fashioned into interim strategies that enable reasonable assessments to be made even more quickly—including after just one or two seasons early on in a manager’s career. Finally, it can be calibrated to yield adjusted estimates tailored to the unique loss functions and risk preferences of those with a stake in hiring and retaining managers. 

The oft-stated claim that analytics has rendered contemporary managers irrelevant essentially gets things backwards. _Analytics_ , this paper suggests, not only show that managers matter but can also be _used_ to make managers an even more consequential aspect of the game. Front offices can employ the measures and protocols developed in this paper to help them more reliably identify the managers most likely to _improve_ their teams’ performances. There is no reason for the effect of analytics on real-time _direction_ of talent resources on the field to fall short of the substantial impact it has had on the _identification_ and _development_ of those resources off the field. 

No doubt, too, more can be done to refine and extend the methods used here. The use of data in baseball science, like any other form of disciplined empirical inquiry, generates the continues enlargement of actionable knowledge through a permanent procession of conjecture and refutation (Popper, 1962). Indeed, the Hybrid Estimator self-consciously builds on earlier efforts to measure 



37 

manage value. Every rung ascended in the ladder of empirical understanding simultaneously enlarges our field of vision and supports ascent to even higher levels. 

So can a stadiumful of monkeys outmanage the managers of today’s professional baseball teams? No—unless we humans make the mistake of excluding manager selection from the process of disciplined observation, measurement, and inference that have so profoundly affected every other aspect of the sport. 



38 

### **References** 

- [1] Aldrich, J.H. and Nelson, F.D., 2011. _Linear Probability, Logit, and Probit Models_ . Quantitative Applications in the Social Sciences. Thousand Oaks, CA: SAGE Publications. 

- [2] Baumann, M. (2019) ‘How the Browns and Paul DePodesta brought Moneyball to the NFL’, _The Ringer_ , 23 August. Available at: <u>https://www.theringer.com/2019/08/23/nfl/paul-depodesta-cleveland-browns-oakland-ath letics-moneyball-analytics-nfl-mlb (Accessed: 5 December 2025).</u> 

- [3] Beasley, W.H. & Rodgers, J.L. (2012) ‘Bootstrapping and Monte Carlo methods’, in APA handbook of research methods in psychology, Vol. 2: Research designs: Quantitative, qualitative, neuropsychological, and biological, American Psychological Association, Washington, DC, pp. 407–425. 

- [4] Becker, B.E. & Huselid, M.A. (1992) ‘The incentive effects of tournament compensation systems’, Administrative Science Quarterly, pp. 336–350. 

- [5] Berger, J.O. (1985) Statistical Decision Theory and Bayesian Analysis, Springer. 

- [6] Birnbaum, P. (2005) ‘Which great teams were just lucky?’, Baseball Research Journal, no. 34, pp. 60–68. 

- [7] Blabac, E. (2010) Encyclopedia of Baseball Statistics: From A to Zr, iUniverse. 

- [8] Braunstein, A. (2010) ‘Consistency and Pythagoras’, _Journal of Quantitative Analysis in Sports_ , vol. 6, no. 1, pp. 1–16. 

- [9] Brewer, M.B. & Crano, W.D. (2014) ‘Research design and issues of validity’, in Reis, H.T. & Judd, C.M. (eds.) _Handbook of Research Methods in Social and Personality Psychology_ , Cambridge: Cambridge University Press, pp. 11–16. 

- [10] Campbell, D.T. & Fiske, D.W. (1959) ‘Convergent and discriminant validation by the multitrait-multimethod matrix’, Psychological Bulletin, vol. 56, p. 81. 

- [11] Castrovince, A. (2019) ‘The influence of WAR on modern front offices’, MLB.com, 3 February. Available at: https://www.mlb.com/news/war-embraced-by-mlb-front-offices-c303484670 (Accessed: 5 December 2025). 

- [12] Click, J. & Keri, J. (2006) Baseball Between the Numbers: Why Everything You Know about the Game is Wrong, Basic Books. 

- [13] Cochran, J.J. & Blackstock, R. (2009) ‘Pythagoras and the national hockey league’, Journal of Quantitative Analysis in Sports, vol. 5. 

- [14] Cohen, J. (1994) ‘The earth is round (p < .05)’, American Psychologist, vol. 49, pp. 997–1003. 

- [15] Davison, A.C. & Hinkley, D.V. (1997) Bootstrap Methods and Their Application, Cambridge University Press. 

- [16] Efron, B. & Morris, C. (1977) ‘Stein’s paradox in statistics’, Scientific American, vol. 236, pp. 119–127. 

- [17] Efron, B. & Morris, C.N. (1973) ‘Stein’s estimation rule and its competitors: an empirical Bayes approach’, Journal of the American Statistical Association, vol. 68, pp. 117–130. 

- [18] Efron, B. (2004) ‘Large-scale simultaneous hypothesis testing: the choice of a null hypothesis’, Journal of the American Statistical Association, vol. 99, pp. 96–104. 

- [19] Efron, B. (2008) ‘Microarrays, empirical Bayes and the two-groups model’, Statistical Science, vol. 23, no. 1, p. 1. 

- [20] Efron, B. (2012) ‘Bayesian inference and the parametric bootstrap’, The Annals of Applied Statistics, vol. 6, p. 1971. 

- [21] Efron, B. (2024) ‘Empirical Bayes: concepts and methods’, in Handbook of Bayesian, Fiducial, and Frequentist Inference, Chapman and Hall/CRC, pp. 8–34. 



39 

- [22] Elliott, G. & Timmermann, A. (2008) ‘Economic forecasting’, Journal of Economic Literature, vol. 46, pp. 3–56. 

- [23] Elliott, G. & Timmermann, A. (2016) ‘Forecasting in economics and finance’, Annual Review of Economics, vol. 8, pp. 81–110. 

- [24] Elsey, J. (2025) ‘Where the Giants’ $3 million manager ranks on MLB’s list of highest paid leaders’, BroBible, 22 October. Available at: <u>https://brobible.com/sports/article/highest-paid-mlb-managers-tony-vitello-contract/</u> (Accessed: 5 December 2025). 

- [25] Frank, R. & Cook, P.J. (1996) The Winner-Take-All Society: Why the Few at the Top Get So Much More Than the Rest of Us, Penguin Publishing Group. 

- [26] Gennaro, V. & Beattie, J. (2013) Diamond Dollars: The Economics of Winning in Baseball, Diamond Analytics. 

- [27] Goodman, S.N. (1999a) ‘Towards evidence-based medical statistics. 1: The P value fallacy’, Annals of Internal Medicine, vol. 130, pp. 995–1004. 

- [28] Goodman, S.N. (1999b) ‘Toward evidence-based medical statistics. 2: The Bayes factor’, Annals of Internal Medicine, vol. 130, pp. 1005–1013. 

- [29] Hadley, L. & Ruggiero, J. (1999) ‘Manager of the Year: an evaluation’, Baseball Research Journal, vol. 28, pp. 51–55. 

- [30] Hardy, M.A. (1993) Regression with Dummy Variables, SAGE Publications. 

- [31] Hoppes, D.F. (1984) ‘The Pythagorean theorem and twenty-two managers’, Baseball Analyst, vol. 12, pp. 11–13. 

- [32] Horowitz, I. (1994) ‘Pythagoras, Tommy Lasorda, and me: on evaluating baseball managers’, Social Science Quarterly, pp. 187–194. 

- [33] Horowitz, I. (1997) ‘Pythagoras’s petulant persecutors’, Managerial and Decision Economics, vol. 18, pp. 343–344. 

- [34] Jaffe, C. (2010) Evaluating Baseball’s Managers: A History and Analysis of Performance in the Major Leagues, 1876–2008, McFarland, Incorporated, Publishers. 

- [35] James, B. (1983) The Bill James Baseball Abstract 1983, Ballantine Books, New York. 

- [36] James, W. & Stein, C. (1961) ‘Estimation with quadratic loss’, in Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability, University of California Press, pp. 361–379. 

- [37] Jenter, D. & Lewellen, K. (2021) ‘Performance-induced CEO turnover’, The Review of Financial Studies, vol. 34, pp. 569–617. 

- [38] Kahn, L.M. (1993) ‘Managerial quality, team success, and individual player performance in Major League Baseball’, ILR Review, vol. 46, pp. 531–547. 

- [39] Kaplan, E.H. & Rich, C. (2017) ‘Decomposing Pythagoras’, Journal of Quantitative Analysis in Sports, vol. 13, pp. 141–149. 

- [40] Keating, P. (2019) ‘The underappreciation of the manager in today’s analytics-driven MLB’, ESPN.com, 4 April. Available at: <u>https://www.espn.com/mlb/story/_/id/26441783/the-underappreciation-manager-today-a nalytics-driven-mlb (Accessed: 5 December 2025).</u> 

- [41] Kruschke, J.K. (2018) ‘Rejecting or accepting parameter values in Bayesian estimation’, Advances in Methods and Practices in Psychological Science, vol. 1, pp. 270–280. 

- [42] Landis, J.R. & Koch, G.G. (1977) ‘The measurement of observer agreement for categorical data’, Biometrics, pp. 159–174. 

- [43] Lee, J. & Lee, J. (2004) ‘Prize and risk-taking strategy in tournaments: evidence from professional poker players’, IZA Discussion Paper no. 1345. Available at: <u>https://ssrn.com/abstract=603525 (Accessed: 5 December 2025).</u> 



40 

- [44] Lewis, M. (2004) Moneyball: The Art of Winning an Unfair Game, W.W. Norton. 

- [45] Lyle, S. & Golenbock, P. (1980) The Bronx Zoo, Dell. 

- [46] Miller, S. (2025) Skipper: Why Baseball Managers Matter and Always Will, Grand Central Publishing. 

- [47] Miller, S.J. (2007) ‘A derivation of the Pythagorean won-loss formula in baseball’, CHANCE, vol. 20, pp. 40–48. 

- [48] Paine, N. (2014) ‘Most managers are headed to the hall of mediocrity’, FiveThirtyEight, 30 March. Available at: <u>https://fivethirtyeight.com/features/most-managers-are-headed-to-the-hall-of-mediocrity/</u> (Accessed: 5 December 2025). 

- [49] Patton, A.J. & Timmermann, A. (2007) ‘Properties of optimal forecasts under asymmetric loss and nonlinearity’, Journal of Econometrics, vol. 140, pp. 884–918. 

- [50] Paul, R.J., Ackerman, G., Filippi, M. & Losak, J. (2016) ‘Managerial decisions and player impact on the difference between actual and expected wins in Major League Baseball’, _Academy of Economics and Finance Journal_ , vol. 7, pp. 57–62. 

- [51] Pavitt, C. (2025) Sabermetric Research Literature Review (unpublished). Available at: <u>https://charliepavitt.home.blog/ (Accessed: 5 December 2025).</u> 

- [52] Popper, K.R. (1962) Conjectures and Refutations: The Growth of Scientific Knowledge, Basic Books, New York. 

- [53] Porter, P.K. & Scully, G.W. (1982) ‘Measuring managerial efficiency: the case of baseball’, Southern Economic Journal, vol. 48, pp. 642–650. 

- [54] Ruggiero, J. (2010) Frontiers in Major League Baseball: Nonparametric Analysis of Performance Using Data Envelopment Analysis, Springer, New York. 

- [55] Ruggiero, J., Hadley, L., Ruggiero, G. & Knowles, S. (1997) ‘A note on the Pythagorean theorem of baseball production’, Managerial and Decision Economics, vol. 18, pp. 335–342. 

- [56] Schell, M.J. (1999) Baseball’s All-Time Best Hitters: How Statistics Can Level the Playing Field, Princeton University Press. 

- [57] Schell, M.J. (2005) Baseball’s All-time Best Sluggers: Adjusted Batting Performance from Strikeouts to Home Runs, Princeton University Press. 

- [58] Schwarz, A. (2004) The Numbers Game: Baseball’s Lifelong Fascination with Statistics, St. Martin’s Press. 

- [59] Singell Jr, L.D. (1993) ‘Managers, specific human capital, and firm productivity in Major League Baseball’, Atlantic Economic Journal, vol. 21, pp. 47–59. 

- [60] Smart, D., Winfree, J. & Wolfe, R. (2008) ‘Major League Baseball managers: do they matter?’, Journal of Sport Management, vol. 22, pp. 303–321. 

- [61] Smith, S. (2024) War in Pieces, Indpnt., North Haven, CT. 

- [62] Stark, J. (2019) ‘Stark: are MLB managers becoming obsolete?’, The Athletic, 10 April. Available at: <u>https://www.nytimes.com/athletic/916577/2019/04/10/stark-are-mlb-managers-becoming</u> - <u>obsolete/ (Accessed: 5 December 2025).</u> 

- [63] Templ, M. (2016) _Simulation for Data Science with R_ , Packt Publishing. 

- [64] Thorn, J., Palmer, P. & Law, K. (1984) The Hidden Game of Baseball, University of Chicago Press. 

- [65] Thorn, J., Palmer, P., Reuther, D. & Law, K. (2015) The Hidden Game of Baseball: A Revolutionary Approach to Baseball and Its Statistics, University of Chicago Press. 

- [66] Waller, L.A. & Gotway, C.A. (2004) _Applied Spatial Statistics for Public Health Data_ , Wiley. 

- [67] Westfall, P.H. (2011) ‘On using the bootstrap for multiple comparisons’, Journal of Biopharmaceutical Statistics, vol. 21, pp. 1187–1205. 



41 

- [68] Winston, W.L., Nestler, S. & Pelechrinis, K. (2022) Mathletics: How Gamblers, Managers, and Fans Use Mathematics in Sports (2nd edn), Princeton University Press. 

- [69] Yomtov, J. (2025) ‘25 best MLB players of the past 25 years, ranked by WAR’, USA Today, 26 November. Available at: <u>https://www.usatoday.com/story/sports/mlb/2025/11/26/best-mlb-players-2025-war-ran kings/87397049007/ (Accessed: 5 December 2025).</u> 

- [70] Zhang, M. (2020) ‘The use and limitations of null-model-based hypothesis testing’, _Biology & Philosophy_ , vol. 35, p. 31. 

- [71] Zhang, T. & Sun, L. (2019) ‘Beyond the traditional simulation design for evaluating type 1 error control: from the “theoretical” null to “empirical” null’, Genetic Epidemiology, vol. 43, pp. 166–179. 



42 

## **Appendix** 

**1. PE Model Monte Carlo empirical null** App. 1 **2. Hybrid Estimator learning curve** App. 2 **3. Additional** **_w_ 162 scores** App. 2 **4. Hybrid Estimator** **__p_** App. 6 **6. Asymmetric loss function** App. 7 

## **1. PE Model Monte Carlo empirical null** 

The simulated empirical null for the PE model involved 1,000 game-level recreations of the careers of each manager in the sample. The simulated null was created at the game level because run-scoring is the random process that determines how closely a team’s record cleaves to the Pythagorean Expectation (Miller, 2007; Kaplan & Rich, 2017) . As explained in the paper, lower-variance run scoring produces excess wins, and higher-variance run scoring excess losses, relative to the Pythagorean formula. The major debate about the validity of using the Pythagorean Expectation as a manager-performance benchmark is whether a manager has any effect on the season-long distribution of a team’s run output (Ruggiero et al., 1997; Horowitz, 1997). 

The aim of the simulation, then, was to create a random run-scoring process—one necessarily uninfluenced by manager input—to determine whether the observed frequency of “smoother than normal” low-variance run-scoring distributions, as well as “more ragged than normal” high variances ones, exceed chance occurrence of such distributions. In the simulation, the mean numbers of runs scored and allowed for each team a sample member managed were calculated. Then each game of that team’s season was replayed by drawing runs scored and allowed randomly from a negative binomial distribution centered on those means: 



(App.1) 

In the event of a “tie,” the outcome of the game was determined randomly based on the mean of team runs scored divided by the sum of the teams’ means of runs scored and runs allowed. 



Importantly, the dispersion of each ( ) was the one that corresponded to _league_ run-scoring standard deviation in the season in question. In this way, runs occurred across games with the appropriately random (manager- _uninfluenced_ ) variation—or distribution of “smoothness” and “raggedness.” This was essential to realistically creating the _random distributional element_ against which the observed manager’s performances—with their own uniquely realized distributions could be observed. 

A robustness check was run using a Weibull distribution of runs scored in line with the finding of Miller (2007) that such a distribution supports an analytic derivation of the Pythagorean Expectation. That simulation generated an outcome that did not meaningfully differ from the one governed by a negative binomial random distribution. The negative binomial was thus chosen for 



App. 1 

greater realism, since a Weibull distribution is continuous, whereas real-word run scoring has so far over the entire course of MLB history been observed to occur in discrete units only. 

## **2. Hybrid Estimator learning curve** 

Section 6.1 of the paper examines the Hybrid Estimator learning curve. As the paper makes clear, the Estimator was formed by fitting the Hybrid Model to manager performance data over a 122-season period—from 1903 (the first season in which the AR(3) _zEXWP_ could be fit) to 2025—and then using empirical Bayesian methods to extract the information necessary to form _w_ 162 posteriors. Accordingly, the Estimator learned everything there was to know in a matter of minutes. 

The “learning curve” is thus a constructive one designed to gauge the pace at which the Estimator _would_ have formed its estimates had it been run in “real time”—as data accumulated season-by-season. The purpose was to form a reasonable understanding of how quickly the Estimator’s measurement of individual manager latent skill levels can be expected to take shape going forward as it is applied to still active and new managers. 

The method for achieving this aim had elements of a historical “what if” simulation. In it, the Hybrid Model was fit 122 times—once after each season _to all the manager data that had accumulated through that season_ . After each successive model was fit, the posteriors of the managers who had served at any time _up to that that point_ were estimated _based on all the information the Estimator used to form posterior estimates of all mangers in 2025_ . 

The latter information reflects nothing in particular about individual managers (if it had, the whole exercise would have been circular). Rather it consists in everything there is to know now—which is a lot—about how _θ_ varies across managers generally. That information is encapsulated in τ<sup>_2_</sup> , the population variance term that defines the spread or scale of the prior. The same information is also used to disentangle measurement precision from individual differences in the updating process that governs the “shrinkage” of individual managers’ data signal—their season-by-season performances as generated by the Hybrid Model. Accordingly, the simulation generated a recreation of the _historical_ trajectory of managers’ _w_ 162 scores using a _timeless_ (really, contemporary) understanding of the distribution of individual differences in latent skill. 

Put differently, the goal of the “what if” simulation was not to discover how quickly the Hybrid Estimator would have learned about the _weight_ to afford season-level data. It was to determine, given what the Estimator _now_ knows about _that_ , how quickly the Estimator would have formed stable estimates of past managers’ innate skill via the Bayesian updating. The answer to that question is the best estimate of how rapidly the Estimator can be expected to form stable estimates of managers’ _w_ 162s today. 

## **3. Additional** **_w_ 162 scores** 

The paper identifies the mangers with the 32 highest and 28 lowest _w_ 162s over the history of the American and National Leagues (Table 3). App. Table 1 and App. Table 2 present the _w_ 162 scores of Hall of Fame managers and of managers active since 2000, respectively. A complete list of all evaluated managers can be downloaded from the supporting materials page. 



App. 2 



App. 3 

|**rank**|**manager **|**g**|**w%**|**_w_162 **|**HDI95**|**dat**<br>**a**|
|---|---|---|---|---|---|---|
|1|John McGraw|4439|.590|5.1|(3.0, 7.2)|7.1|
|4|Joe McCarthy|3426|.615|3.2|(0.9, 5.5)|4.7|
|5|Al Lopez|2414|.584|3.1|(0.5, 5.6)|5.1|
|8|Casey Stengel<br>Wilbert|3732|.509|2.5|(0.2, 4.8)|3.7|
|9|Robinson|2827|.499|2.4|(0.0, 4.9)|3.8|
|25|Bobby Cox|4490|.555|1.6|(-0.4, 3.7)|2.2|
|25|Tony LaRussa|5356|.535|1.6|(-0.3, 3.5)|2.1|
|35|Bill McKechnie|3619|.524|1.5|(-0.8, 3.7)|2.1|
|35|Miller Huggins|2550|.554|1.5|(-1.0, 3.9)|2.4|
|60|Jim Leyland|3489|.507|1.1|(-1.1, 3.4)|1.7|
|60|Whitey Herzog|2406|.532|1.1|(-1.4, 3.6)|1.8|
|77|Dick Williams|3010|.519|0.8|(-1.5, 3.2)|1.3|
|95|Billy Southworth|1748|.597|0.6|(-2.2, 3.3)|1.1|
|121|Leo Durocher|3645|.539|0.4|(-1.8, 2.6)|0.5|
|163|Sparky Anderson|4001|.544|0.2|(-1.9, 2.3)|0.3|
|248|Walter Alston|3632|.559|-0.2|(-2.4, 2.0)|-0.3|
|269|Tom Lasorda|3034|.527|-0.3|(-2.6, 2.1)|-0.4|
|269|Joe Torre|4276|.538|-0.3|(-2.4, 1.8)|-0.4|
|269|Earl Weaver|2518|.582|-0.3|(-2.8, 2.2)|-0.5|
|304|Bucky Harris|4379|.493|-0.4|(-2.5, 1.6)|-0.6|
|444|Connie Mack|7386|.485|-1.3|(-3.1, 0.4)|-1.6|



**App. Table 1. Hall of Fame managers (post 1900** ). “Rank” refers to _w_ 162 rank for all rated managers; “g” career games; “W%” career winning percentage; “HDI” the densest portion of the manager’s posterior mass that include 95% of the manager’s _w_ 162 distribution; and “data” the manager’s Hybrid Model _w_ 162 score prior to Bayesian shrinkage. 



App. 4 

|**ran**<br>|||**w**|**_w_16**|**dat**|**ran**<br>|||**w**|**_w_16**||
|---|---|---|---|---|---|---|---|---|---|---|---|
|**k**|**manager**|**g**|**%**|**2**|**a**|**k**|**manager**|**g**|**%**|**2**|**data**|
|||205|.50||||||.43|||
|1|Felipe Alou|0<br>165|3<br>.53|3.1|5.5|45|Rene Lachemann|995|5<br>.38|0.4|1.4|
|2|Craig Counsell|3<br>451|2<br>.49|2.3|4.4|45|Brad Mills|462<br>179|7<br>.54|0.4|1.6|
|3|Bruce Bochy|2|8<br>.55|2.1|2.9|53|Charlie Manuel|0|7<br>.53|0.3|0.7|
|3|Stephen Vogt|323<br>141|7<br>.50|2.1|11.9|53|Bob Brenly|562|7<br>.50|0.3|1.3|
|5|Fredi González|1|7<br>.50|2.0|4.3<br>10.|53|Tom Trebelhorn|930|5<br>.41|0.3|0.9|
|5|Cecil Cooper|344<br>151|6<br>.61|2.0|7|53|Derek Shelton|747|0<br>.46|0.3|1.0|
|7|Dave Roberts|6<br>401|9<br>.53|1.9|3.9|53|Tony Perez|158|8<br>.49|0.3|3.2|
|8|Dusty Baker|6<br>258|9<br>.46|1.8|2.5|53|Larry Bowa|847|1<br>.54|0.3|0.8|
|9|Buddy Black|3<br>173|0<br>.49|1.7|2.7|59|Ken Macha|972|0<br>.57|0.2|0.6|
|9|Jim Tracy|8<br>259|3<br>.48|1.7|3.2|59|Sandy Alomar|52|7<br>.44|0.2|8.4|
|9|Clint Hurdle|5<br>449|6<br>.55|1.7|2.7|59|Skip Schumaker|324|8<br>.39|0.2|1.3|
|12|Bobby Cox|0<br>535|5<br>.53|1.6|2.2|59|Tony DeFrancesco|41|0<br>.47|0.2|8.7|
|12|Tony LaRussa|6|5<br>.48|1.6|2.1|59|Ray Knight|260|7<br>.42|0.2|1.2|
|12|Kirk Gibson|730|5<br>.56|1.6|5.0|59|Davey Lopes|336|9<br>.29|0.2|0.9|
|12|Mike Shildt|775|1<br>.46|1.6|4.7|59|Warren Schaeffer|122<br>121|5<br>.47|0.2|2.6|
|16|John Boles|432|1<br>.52|1.5|6.9|66|Pat Corrales|2|5<br>.45|0.1|0.3|
|16|Gabe Kapler|867|6<br>.43|1.5|4.2|66|Tom Lawless|24|8<br>.47|0.1|8.7|
|16|Pete Mackanin|525<br>226|6<br>.49|1.5|5.8|66|Edwin Rodríguez|162|5<br>.54|0.1|1.2|
|19|Art Howe|3<br>234|8<br>.50|1.4|2.4|66|John Schneider|562|1<br>.48|0.1|0.4|
|19|Bobby Valentine|7<br>147|4<br>.54|1.4|2.3|66|Robby Thompson|29|3<br>.44|0.1|4.6|
|21|Brian Snitker|8|8<br>.43|1.3|2.7|66|Dan Jennings|124|4<br>.41|0.1|0.9|
|22|Dave Miley|289<br>203|3<br>.51|1.2|7.8|72|Manny Acta|894|7<br>.54|0.0|0.0|
|22|Jack McKeon|7|4<br>.43|1.2|2.1|72|Willie Randolph|556|5<br>.36|0.0|0.0|
|22|Andy Green|650<br>|1<br>|1.2|4.1|72|Bob Schaefer|22|4<br>|0.0|-1.3|
|||348|.50||||||.53|||
|25|Jim Leyland|9|7|1.1|1.7|72|Carlos Mendoza|324|1|0.0|-0.1|





App. 5 

|25|Jim Riggleman|163<br>0|.44<br>5<br>.50|1.1|2.2|72|Don Kelly|124|.47<br>6<br>.47|0.0|-0.3|
|---|---|---|---|---|---|---|---|---|---|---|---|
|25|Ron Roenicke|740|4<br>.38|1.1|3.4|72|David Bell|862<br>144|0<br>.52|0.0|-0.1|
|28|John Russell|488|1<br>.47|1.0|4.5|72|Mike Matheny|9|2<br>.46|0.0|-0.1|
|29|Mike Quade|199<br>119|7<br>.58|0.9|8.1|79|Joel Skinner|77|8<br>.36|-0.1|-1.2|
|29|Aaron Boone|1<br>200|4<br>.49|0.9|2.1|79|Bo Porter|300|7<br>.45|-0.1|-0.5|
|29|Terry Collins|2<br>221|4<br>.47|0.9|1.5|79|Tom Runnells|152|4<br>.45|-0.1|-0.9|
|32|Frank Robinson|9<br>131|6<br>.51|0.8|1.4|79|Don Wakamatsu|301|2<br>.28|-0.1|-0.6|
|32|Scott Servais|3<br>183|4<br>.52|0.8|1.6|79|Grady Sizemore|45|9<br>.41|-0.1|-4.3|
|34|A.J. Hinch|1<br>110|6<br>.45|0.7|1.3|79|Bucky Dent|95|1<br>.40|-0.1|-2.6|
|34|Lloyd McClendon|9|1<br>.50|0.7|1.6|85|Larry Rothschild|494|7<br>.50|-0.2|-19.9|
|36|Oliver Marmol|646|2<br>.48|0.6|2.1|85|Mickey Callaway|324<br>143|3<br>.51|-0.2|-0.9|
|36|Cookie Rojas|158|7<br>.51|0.6|6.7|85|Ozzie Guillén|5<br>111|4<br>.49|-0.2|-0.4|
|36|Jeff Banister|637|2<br>.47|0.6|2.1|85|Gene Lamont|6|6<br>.38|-0.2|-0.6|
|36|Paul Molitor|647|1<br>.50|0.6|2.0|89|Daren Brown|50|0<br>.42|-0.3|-8.3|
|36|Tony Mansolino<br>Clayton|119|4<br>.48|0.6|7.9|89|Bryan Price|665|0<br>.47|-0.3|-0.8|
|41|McCullough|162|8<br>.58|0.5|5.7<br>35.|89|David Ross|536|8<br>.42|-0.3|-1.0|
|41|Tim Bogar|24|3<br>.55|0.5|8|89|Bruce Kimm|78|3<br>.42|-0.3|-5.6|
|41|Pat Murphy|420|2<br>.44|0.5|2.2|89|Trey Hillman|357|9<br>.42|-0.3|-1.5|
|41|Miguel Cairo|107<br>243|9<br>.56|0.5|7.3|89|Mike Redmond|371|6<br>.35|-0.3|-1.5|
|45|Davey Johnson|2<br>132|2<br>.47|0.4|0.7|89|Jerry Royster|150<br>427|3<br>.53|-0.3|-3.4|
|45|Don Baylor|1|7<br>.56|0.4|1.2|89|Joe Torre|6<br>135|8<br>.46|-0.3|-0.4|
|45|Dan Wilson|196|6<br>.55|0.4|3.9|89|Jeff Torborg|1|9<br>.46|-0.3|-0.6|
|45|Larry Dierker|781|6<br>.45|0.4|1.2|89|John McLaren|174|0<br>.45|-0.3|-3.3|
|45|Bob Boone|791|9<br>|0.4|1.2|89|Phil Nevin|257<br>|1<br>|-0.3|-2.2|
||||.42|||||325|.51|||
|45|Ryne Sandberg|278|8|0.4|2.6|89|Bob Melvin|3|3|-0.3|-0.5|





App. 6 

|**ran**<br>|||**w**<br>|**_w_16**<br>||**r**|**an**<br>||**w**<br>|<br>**_w_1**<br>|**6**<br>**dat**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**k**|<br>**manager**|**g**|**%**|**2**|**data**||**k**<br>**manager**|**g**|**%**|<br>**2**|**a**|
|10|||.46|||12|||.41|||
|1|Jerry Narron|633|3|-0.4|-1.3|7|Tony Pena|483|0|-0.7|-3.2|
|10|||.43|||13|||.46|||
|1|Rich Renteria|700|6|-0.4|-1.2|3|Matt Quatraro|485|4|-0.8|-3.3|
|10|||.55|||13||159|.50|||
|1|Grady Little|675|4|-0.4|-1.3|3|Ron Washington|8|0|-0.8|-1.6|
|10||140|.49|||13||260|.53|||
|1|Torey Lovullo|1|2|-0.4|-0.8|5|Joe Maddon|6|3|-0.9|-1.4|
|10||102|.50|||13||182|.48|||
|1|Rocco Baldelli|1|9|-0.4|-1.0|5|Don Mattingly|6|4|-0.9|-1.7|
|10|||.52|||13||167|.53|||
|1|Jayce Tingler|228|2|-0.4|-3.2|5|Kevin Cash|8|3|-0.9|-1.7|
|10|||.49|||13||306|.53|||
|1|Carlos Tosca|384|0|-0.4|-2.0|8|Mike Scioscia|4|4|-1.0|-1.4|
|10|||.45|||13|||.31|||
|1|Chip Hale|328|4|-0.4|-2.4|8|Pedro Grifol|278|7|-1.0|-7.0|
|10|||.35|||13|||.46|||
|1|Luis Pujols|155|5|-0.4|-5.0|8|Buck Martinez|212|7|-1.0|-8.0|
|11|||.35|||14||246|.48|||
|0|Tony Beasley|48|4|-0.5|-16.1|1|Ron Gardenhire|4|4|-1.1|-1.7|
|11|||.57|||14|||.47|||
|0|Rob Thomson|602|8|-0.5|-1.7|1|Brad Ausmus|805|7|-1.1|-3.3|
|11|||.55|||14|||.39|||
|0|Matt Williams|324|2|-0.5|-2.9|1|Mark Kotsay|647|4|-1.1|-4.0|
|11|||.33|||14||364|.53|||
|0|Juan Samuel|51|3|-0.5|-17.2|4|Terry Francona|8|8|-1.2|-1.7|
|11|||.54|||14|||.46|||
|0|Joe Espada|330|2|-0.5|-2.9|4|Brandon Hyde|915|1|-1.2|-3.3|
|11|||.41|||14||111|.44|||
|0|Toby Harrah|80|2|-0.5|-11.5|6|Dave Martinez|7|7|-1.3|-3.0|
|11||194|.51|||14|||.50|||
|6|Bill Virdon|2|9|-0.6|-1.0|6|Charlie Montoyo|471|1|-1.3|-5.5|
|11|||.43|||14|||.45|||
|6|Walt Weiss|646|8|-0.6|-1.9|6|Hal McRae|872|8|-1.3|-3.7|
|11||137|.50|||14||122|.41|||
|6|Jerry Manuel|6|7|-0.6|-1.2|6|Buddy Bell|8|8|-1.3|-3.1|
|11|||.27|||14||205|.54|||
|6|Al Pedrique|84|4|-0.6|-13.8|6|Joe Girardi|0|5|-1.3|-2.3|
|11||201|.48|||15||107|.51|||
|6|Phil Garner|8|3|-0.6|-1.0|1|John Farrell|3|5|-1.4|-3.3|
|11|||.39|||15|||.39|||
|6|Dale Sveum|336|9|-0.6|-3.4|2|Dave Trembley|465|6|-1.5|-6.4|
|11|||.39|||15|||.38|||
|6|Joe Kerrigan|43|5|-0.6|-21.8|3|Alan Trammell|498|2|-1.7|-7.5|
|11||337|.51|||15|||.42|||
|6|Buck Showalter|9|0|-0.6|-0.9|3|Tony Muser|763|1|-1.7|-5.3|
|11|||.36|||15||234|.50|||
|6|Will Venable|168|3|-0.6|-6.7|5|Mike Hargrove|3|4|-1.8|-2.9|
|11|||.46|||15|||.47|||
|6|Robin Ventura|804|6|-0.6|-1.8|5|Bob Geren|714|5|-1.8|-5.8|
|11||112|.54|||15||153|.51|||
|6|Alex Cora|8|0|-0.6|-1.5|7|Johnny Oates|9|7|-2.0|-3.9|
|12<br>7|Sam Perlozzo|300|.42<br>0|-0.7|-4.3|15<br>7|Lou Piniella|352<br>4|.51<br>7|-2.0|-2.8|





App. 7 

|12|||.46|||15||237|.47|||
|---|---|---|---|---|---|---|---|---|---|---|---|
|7|Luis Rojas|220|4|-0.7|-5.3|7|Tom Kelly|5|8|-2.0|-3.4|
|12||254|.47|||16||169|.53|||
|7|Ned Yost|2|3|-0.7|-1.1|0|Jimy Williams|7|5|-2.5|-4.7|
|12|||.42|||16||158|.50|||
|7|Chris Woodward|498|4|-0.7|-2.9|1|John Gibbons|0|1|-2.9|-5.7|
|12|||.48|||16||158|.47|||
|7|Lee Mazzilli|269|3|-0.7|-4.8|2<br>16|Eric Wedge|7<br>172|6<br>.51|-3.1|-6.1|
|||||||3|Cito Gaston|6|6|-3.4|-6.4|



**App. Table 2. Manager** **_w_ 162s since 2000.** List includes every manager who managed since 2000; _w_ 162s reflect career rating regardless of when career started. “Data” refers to raw Hybrid Model score. 



App. 8 

## **4. Hybrid Estimator** **__p_** 

The paper proposes a provisional variant of the Hybrid Estimator, the Hybrid Estimator __p_ , for single-season use. Calculation of the Estimator __p_ scores is straightforward. As indicated in the paper, the scores are formed by awarding 20% of the residuals of the “base model,” that is, the Hybrid Model (6) without the μ _i_ manager fixed-effect term: 





The required data are the wins, the games played, and the standardized season WAR per game and AR(3) expected winning-percentages for all teams in the relevant season. After the model is fit, the residuals for each team (which will consist in win counts over the number of games played in a season) should be predicted or otherwise calculated and then multiplied by 0.2. These are the manager _w_ 162 _p_ s for each team. Where a team used more than one manager in a season, each can be awarded the fraction of the _w_ 162 _p_ total corresponding to the fraction of total games managed. Alternatively, one could split the team into two separate observations if one has access to the WAR per game data corresponding to the portions of the season overseen by each manager. 

The data necessary to generate the season _w_ 162 _p_ s for every season since 1903 (including a file that identifies the manager and number of games managed per team per season) are available for download in the supporting materials page. A file reporting Estimator_p scores—referred to as w162ps—from 1903 to 2025 also can be found there. 

## **5. Alternative hierarchical Bayes Hybrid Estimator scores** 

As a robustness check on the empirical Bayes analysis performed in the paper, a hierarchical Bayes regression model was also fit to the data. The specification tracked the Hybrid Model (6) except that managers were modeled as random intercepts rather than as fixed effects: 





Weakly informed priors centered at no effect were selected: 



For the standardized predictors and for the population-level intercept, N(0,2) creates a heavy mass for plausible coefficient sizes and minimal shrinkage. For the manager-level random intercepts, the half-normal SD is weakly informative, is always positive, is broad on the appropriate scale (a probability effect of roughly 0.50), and permits the data to dominate (Gelman, 2006). 

Ample MCMC draws were made. The model ran 6 chains with 1,500 warmup and 2,500 post-warmup draws each—15,000 posterior draws total. 



App. 9 

The model output summary appears in App. Table 3. The diagnostics confirm a well-performing model. The fixed effect terms are sensible. The value for τ, 0.0441, equates to a standard deviation of 1.8 wins per 162 games—slightly but not substantially tighter than the 2.1 per 162 games observed in the empirical Bayesian analysis. 

|**param**|**mean**|**sd**|**95% HDI**|
|---|---|---|---|
|beta0|-0.0049|0.004|(-0.0129, 0.0033)|
|beta_zwpg|0.2733|0.004|(0.2657, 0.2809)|
|beta_zexwp|0.0468|0.004|(0.0395, 0.0546)|
|τ (SD_u)|0.0441|0.005|(0.0342, 0.0534)|



^ **App. Table 3.** Split-𝑅 < 1.01 for all parameters. Effective sample sizes (bulk and tail) > 5,000). Monte-Carlo SE for posterior means ≤ 0.0001. 

The results were also very similar to the empirical Bayes ones reported in the paper. The rank orderings of managers was near identical (Kendall’s _W_ =0.99). The _w_ 162 estimates highly concordant (Lin’s CCC = 0.97);  the very highest and lowest performers in the hierarchical Bayes analysis score slightly lower than they did under the empirical Bayes analysis, but the impact remains close. This level of agreement helps to reassure that the empirical Bayesian analysis informing the Hybrid Estimator was well formed. Full results are included in the supporting materials. 

|_Highest hierarch_|_ical Bayes_|_w162s_||_Lowest hier_|_archical_|_Bayes_|_w162s_|
|---|---|---|---|---|---|---|---|
||_w_16||HDI95||_w_16|R<||
|manager|2|R>2||manager|2|2|HDI95|
|||||||0.7||
|John McGraw|4.3|0.98|(2.2, 6.5)|Cito Gaston|-2.8|1<br>0.6|(2.2, 6.5)|
|Frank Chance|3.5|0.86|(0.8, 6.4)|Jimmy McAleer|-2.5|4<br>0.6|(0.8, 6.4)|
|Fred Clarke|2.9|0.76|(0.3, 5.6)|Eric Wedge|-2.4|2<br>0.5|(0.3, 5.6)|
|Felipe Alou|2.6|0.68|(0.1, 5.3)|Joe Cantillon|-2.3|5<br>0.5|(0.1, 5.3)|
|Joe McCarthy|2.6|0.68|(0.3, 4.8)|John Gibbons|-2.2|6<br>0.5|(0.3, 4.8)|
|Al Lopez|2.5|0.64|(0.1, 4.9)|Jimy Williams|-2.1|3<br>0.5|(0.1, 4.9)|
|Pat Moran|2.3|0.56|(-0.5, 5.1)|Patsy Donovan|-2.0|0<br>0.4|(-0.5, 5.1)|
|Wilbert Robinson|2.2|0.58|(-0.1, 4.6)|Bobby Bragan|-2.0|8<br>0.4|(-0.1, 4.6)|
|Casey Stengel|2.1|0.53|(-0.2, 4.4)|Ned Hanlon|-1.9|7<br>0.4|(-0.2, 4.4)|
|Bruce Bochy|2.1|0.53|(0.1, 4.1)|Jimmie Wilson|-1.9|7<br>0.4|(0.1, 4.1)|
|Craig Counsell|2.0|0.50|(-0.7, 4.8)|Lee Fohl|-1.8|3<br>0.4|(-0.7, 4.8)|
|Pete Rose|1.8|0.45|(-1.2, 5.0)|Doc Prothro|-1.6|1<br>0.4|(-1.2, 5.0)|
|Danny Ozark|1.8|0.45|(-1.0, 4.7)|Bobby Wallace|-1.6|1|(-1.0, 4.7)|





App. 10 

|||||||0.3||
|---|---|---|---|---|---|---|---|
|Paul Richards|1.8|0.44|(-0.8, 4.4)|Doug Rader|-1.6|9|(-0.8, 4.4)|
|||||||0.3||
|Dusty Baker|1.7|0.37|(-0.4, 3.8)|Lou Piniella|-1.5|4|(-0.4, 3.8)|



**App. Table 4. Scores for hierarchical Bayes variant of Hybrid Estimator.** Top and bottom scores as determined by hierarchical Bayes regression model. “ _w_ 162” refers to estimator MAP; “R>2” and “R<2” probability of _w_ 162 above or below 2 and -2, respectively; HDI95 the densest portion of the posterior mass containing 95% of the _w_ 162 values. 

## **6. Asymmetric loss function** 

Section 6.3 of the paper illustrates how the Hybrid Estimator can be conformed to a user-specific loss function. The default loss function maximizes accuracy by minimizing mean squared error (MSE). It can be represented as 



(App.5) 

Simply put, any discrepancy between the true value of _θ_ (understood as managerial skill level) at ^ any particular point in the distribution at which it is being estimated and the reported value, , is θ the magnitude of the difference squared. 

That default loss function can be adjusted at will: 



(App.6) 

Here _f_ stands for any set of operations performed on the MSE loss function to conform it to an alternative decision theory or utilitarian loss function (Berger, 1985). 

In the paper, _an asymmetric loss function_ was posited. For reasons explored in the paper, it was suggested that a team front office might adopt the position that the mistake of estimating a manager’s _w_ 162 to be < 2 when it is in fact ≥ 2 is _more costly_ than the mistake of erroneously estimating that his _w_ 162 is ≥ 2 when in fact it is < 2. A team front office might similarly deem the mistake of erroneously estimating that a manager’s _w_ 162 is > -2 when in fact it is ≤ -2 to be more costly than the mistake of erroneously estimating that his _w_ 162 is ≤ -2 when in fact it is > -2. 

We could then represent, _f_ , the adjustment being imposed on the MSE default loss function, this way, 





Where _s_ and _t_ are, respectively, _w_ 162 = - 2 and _w_ 162 = 2, the region in between -2 and 2 is governed by the conventional MSE loss function. Errors are penalized by weights _w1_ and _w2_ for the regions of _w_ 162 at or below -2 and at or above 2, respectively. In the paper, the special loss penalties for both 



App. 11 

of the specified type II errors in question was 2x; in that case _w1_ = _w2_ . But the front office could vary _w1_ and _w2_ if it regarded one of the disfavored error types as even more costly than the other. 

The Estimator can be programmed to generate the _w_ 162 estimates that reflect this asymmetric loss function rather than the MSE one (Elliott & Timmerman, 2008, 2016; Patton & Timmerman, 2007). ^ 2 Under _f_ , loss comprises the sum of (θ −θ𝑗) across the three demarcated _w_ 162 regions _weighted_ 𝑗 _by_ the fraction of a manger’s posterior mass within each of those regions: 





Minimizing expected loss thus requires integrating this sum over the posterior of each manager. The resulting collection of estimates—not the MSE MAPs—are now reported as the managers’ _w_ 162s (App. Table 5). 

Two consequences mentioned in the paper bear restating. First, the effects will be felt not only by some small select group of mangers highly proximate to the _s_ and _t_ cutoffs but across the entire _w_ 162 frontier depending on how much of their posterior mass straddles one of the two error thresholds (Figure 11). Second, the effects will not be monotonic: all else equal, managers with relatively low individual variances will be affected less since the precision of their _w_ 162s implies the probability of error associated with their MSE value is small; mangers with higher variances will be affected more, since the uncertainty associated with their MSE _w_ 162 scores will involve higher risks of error. As a result, the re-calculation of the manager _w_ 162 point estimates can result in reordering of managers relative to their MAP baselines (App. Table 5). 

_These are exactly the effects that the front office management’s valuations demand_ . To start, the impact of the re-calculations will always be _unidirectional_ in relation to the stipulated _s_ and _t_ thresholds (Figure 11; App. Table 5). Mangers with MSE MAPs above the _w_ 162 ≤ -2 threshold (to use the paper example) might be moved toward or over it depending on what fraction of their posterior mass lies below that threshold. Those with MSE MAPs _below_ the _w_ < -2 threshold likewise might be pushed even further down depending on how much of their posterior mass straddles the threshold. But managers with MSE MAPs below < -2 will _never_ be moved upward, much less above, the ≤ -2 threshold—for by hypothesis, the readjustment of the manager’s _w_ 162 in that case would be _increasing_ the probability of a _higher_ error costs. Likewise, mangers with MSE MAPs below the _w_ 162 ≥2 threshold (again to use the paper example) might be moved up toward or over it. But those with MSE MAPs _above_ the _w_ 162 ≥ 2 threshold will _never_ be moved downward: such a readjustment can, by hypothesis, _only_ increase the risk of the higher-cost error. 

In addition, any readjustments relative to the MSE MAPs will always be proportional to the front office’s specified risk preference. All else equal, managers closer to _s_ and _t_ will be pushed harder. But importantly and as mentioned, when _θ_ uncertainty for a manger is _low_ , his adjusted _w_ 162 will be adjusted less dramatically relative to his MSE MAP than it will be when his _θ_ uncertainty is _high_ : this is exactly in line with the _risk aversion_ that the front office decisionmakers are posited as experiencing for retaining managers who might have true _w_ 162s ≤ -2 and the risk _preference_ they are posited as experiencing for retaining managers who might have true _w_ 162s ≥ 2. 



App. 12 

It bears re-emphasis, too, that this is just an illustration of this feature of the Hybrid Estimator. Its estimates can be made responsive not only to this non-MSE loss function but to any decision theory loss function a user chooses. 



App. 13 

|_Managers_|_in vicinity of M_|_AE_w_162= 2_|_thresho_|_ld_||_Managers i_|_n vicinity of MAE_w|_162= - 2 thre_|_shold_|||
|---|---|---|---|---|---|---|---|---|---|---|---|
|**manager**|**adj_w162**|**mse_162**|**adj**|**ROP**<br>**E**|**va**<br>**r**|**manager**|**adj_w162**|**mse_w16**<br>**2**|**adj**|**ROPE**|**va**<br>**r**|
|John McGraw|5.1|5.1|0.0|1.00|1.2|Jimmy McAleer|-3.7|-3.4|-0.2|0.83|2.4|
|Frank Chance|4.4|4.4|0.1|0.95|2.1|Cito Gaston|-3.6|-3.4|-0.2|0.84|2.0|
|Fred Clarke|3.9|3.8|0.1|0.90|1.9|Joe Cantillon|-3.4|-3.1|-0.3|0.78|2.1|
|Felipe Alou|3.3|3.1|0.2|0.80|1.4|Eric Wedge|-3.3|-3.1|-0.2|0.73|3.3|
|Joe McCarthy|3.3|3.2|0.2|0.85|1.8|John Gibbons|-3.1|-2.9|-0.3|0.73|2.1|
|Al Lopez|3.3|3.1|0.2|0.79|1.7|Patsy Donovan|-3.1|-2.7|-0.3|0.67|2.6|
|Pat Moran|3.1|2.8|0.3|0.70|2.3|Jimmie Wilson|-3.0|-2.6|-0.3|0.65|2.4|
|Casey Stengel|2.7|2.5|0.3|0.65|1.4|Bobby Bragan|-2.9|-2.6|-0.4|0.64|2.6|
|Wilbert Robinson|2.7|2.4|0.3|0.64|1.5|Jimy Williams|-2.8|-2.5|-0.3|0.64|2.0|
|Craig Counsell|2.6|2.3|0.3|0.58|2.0|Lee Fohl|-2.8|-2.5|-0.3|0.62|2.2|
|Pete Rose|2.6|2.2|0.4|0.55|2.8|Doc Prothro|-2.8|-2.3|-0.4|0.59|2.9|
|Danny Ozark|2.5|2.1|0.4|0.54|2.4|Ned Hanlon|-2.8|-2.4|-0.4|0.58|3.4|
|Stephen Vogt|2.5|2.1|0.4|0.52|1.1|Bobby Wallace|-2.6|-2.1|-0.4|0.54|2.8|
|Fredi González|2.4|2.0|0.4|0.51|3.5|Doug Rader|-2.6|-2.2|-0.4|0.54|2.3|
|Cecil Cooper|2.4|2.0|0.4|0.49|2.2|Fred Haney|-2.5|-2.1|-0.4|0.54|3.8|
|Bruce Bochy<br>Steve O'Neill|2.4|2.1|0.3|0.55|3.4|Tom Kelly|-2.4|-2.0|-0.3|0.52|1.7|





<!-- Start of picture text -->
Steve O'Neill<br>2.3  1.9<br><!-- End of picture text -->

|Dave Roberts|2.3<br>2.2|1.9<br>1.9|0.4<br>0.4|0.48<br>0.46|1.9<br>2.2<br>-|Johnny Oates<br>Lou Piniella<br>App. 14-|-2.3<br>-2.3|-2.0<br>-2.0|-0.4<br>-0.3|0.49<br>0.49|1.3<br>2.1|
|---|---|---|---|---|---|---|---|---|---|---|---|





<!-- Start of picture text -->
-2.3  -2.0<br><!-- End of picture text -->

|Paul Richards|2.2|1.8|0.4|0.45|1.9|Billy Meyer|-2.3|-1.8|-0.4|0.48|2.8|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Frank Selee|2.2|1.8|0.4|0.45|1.2|Bob Geren|-2.3|-1.8|-0.4|0.47|2.9|
|Dusty Baker|2.1|1.8|0.3|0.42|3.4|John McCloskey|-2.2|-1.8|-0.4|0.48|3.3|
|Joe Gordon|2.1|1.6|0.4|0.42|1.6|Frank Quilici|-2.2|-1.8|-0.4|0.44|1.5|
|Jim Tracy|2.1|1.7|0.4|0.41|2.0|Tony Muser|-2.2|-1.7|-0.4|0.43|1.7|
|Buddy Black|2.1|1.7|0.3|0.41|1.6|Alan Trammell|-2.1|-1.7|-0.4|0.46|3.1|
|Kirk Gibson|2.0|1.6|0.4|0.41|3.3|Dan Howley|-2.1|-1.7|-0.4|0.45|2.8|
|Clint Hurdle|2.0|1.7|0.3|0.39|1.1|Chuck Tanner|-2.1|-1.8|-0.3|0.45|2.7|
|George Stallings|2.0|1.6|0.4|0.40|2.2|Deacon McGuire|-2.1|-1.7|-0.4|0.46|3.3|
|Hank O'Day|2.0|1.6|0.4|0.41|0.9|Mike Hargrove|-2.1|-1.8|-0.4|0.46|3.3|
|Red Dooin|2.0|1.6|0.4|0.40|1.9|Harry Wolverton|-2.0|-1.6|-0.4|0.45|3.9|
|Mike Shildt|2.0|1.6|0.4|0.40|2.9|Bill Donovan|-2.0|-1.6|-0.4|0.42|3.1|
|Chuck Dressen|2.0|1.6|0.4|0.39|2.8|Stan Hack|-1.9|-1.5|-0.4|0.42|3.2|
|George Gibson|2.0|1.6|0.4|0.39|3.5|Heinie Wagner|-1.9|-1.5|-0.4|0.43|3.9|
|Nick Leyva|1.9|1.5|0.4|0.40|2.8|Dave Trembley|-1.9|-1.5|-0.4|0.41|3.3|
|John Boles|1.9|1.5|0.4|0.39|2.8|Freddie Fitzsimmons|-1.9|-1.4|-0.4|0.42|3.6|
|Bobby Cox|1.9|1.6|0.3|0.36|3.5|Hans Lobert|-1.9|-1.4|-0.4|0.43|3.9|
|Pinky Higgins|1.9|1.5|0.4|0.38|3.3|Tris Speaker|-1.8|-1.4|-0.4|0.37|2.4|
|Gabe Kapler|1.9|1.5|0.4|0.38|2.4|Jimmy Burke|-1.8|-1.4|-0.4|0.40|3.3|
|Tony LaRussa|1.9|1.6|0.3|0.35|2.7|Solly Hemus|-1.8|-1.4|-0.4|0.40|3.4|
|Pete Mackanin|1.9|1.5|0.4|0.38|1.3|Billy Herman|-1.8|-1.4|-0.4|0.39|3.1|



**App. Table 5. Loss function adjustments.** “Adj_w162” and “mse_162” refer respectively to the _w_ 162 scores with and without the asymmetric-loss-function adjustment; “Adj” the overall degree of adjustment; “ROPE” the proportion of posterior mass outside the relevant border of | _w_ 162| = 2; “Var” _w_ 162 variance. Highlighted cells identify managers whose adjusted _w_ 162s moved from below to above the +2 or from above to below the -2 Threshold, respectively. 

-App. 15- 

### **Appendix references** 

- [1] Berger, J.O. (1985) Statistical Decision Theory and Bayesian Analysis, Springer. 

- [2] Elliott, G. & Timmermann, A. (2008) ‘Economic forecasting’, Journal of Economic Literature, vol. 46, pp. 3–56. 

- [3] Elliott, G. & Timmermann, A. (2016) ‘Forecasting in economics and finance’, Annual Review of Economics, vol. 8, pp. 81–110. 

- [4] Gelman, A. (2006) ‘Prior distributions for variance parameters in hierarchical models’, _Bayesian Analysis_ , vol. 1, pp. 515–534. 

- [5] Horowitz, I. (1997) ‘Pythagoras’s petulant persecutors’, Managerial and Decision Economics, vol. 18, pp. 343–344. 

- [6] Kaplan, E.H. & Rich, C. (2017) ‘Decomposing Pythagoras’, Journal of Quantitative Analysis in Sports, vol. 13, pp. 141–149. 

- [7] Ruggiero, J., Hadley, L., Ruggiero, G. & Knowles, S. A Note on the Pythagorean Theorem of Baseball Production. Managerial and Decision Economics 18, 335-342 (1997). 

- [8] Miller, S.J. (2007) ‘A derivation of the Pythagorean won-loss formula in baseball’, CHANCE, vol. 20, pp. 40–48. 

- [9]Patton, A.J. & Timmermann, A. (2007) ‘Properties of optimal forecasts under asymmetric loss and nonlinearity’, Journal of Econometrics, vol. 140, pp. 884–918. 

-App. 16- 


