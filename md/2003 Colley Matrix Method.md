<!-- source: 2003 Colley Matrix Method.pdf -->

# **Colley’s Bias Free College Football Ranking Method:** The Colley Matrix Explained 

Wesley N. Colley 

## _Ph.D., Princeton University_ 

## **ABSTRACT** 

Colley’s matrix method for ranking college football teams is explained in detail, with many examples and explicit derivations. The method is based on very simple statistical principles, and uses only Div. I-A wins and losses as input — margin of victory does not matter. The scheme adjusts effectively for strength of schedule, in a way that is free of bias toward conference, tradition, or region. Comparison of rankings produced by this method to those produced by the press polls shows that despite its simplicity, the scheme produces common sense results. 

_Subject headings:_ methods: mathematical 

## **1. Introduction** 

The problem of ranking college football teams has a long and intriguing history. For decades, the national championship in college football, and/or the opportunity to play for that championship, has been determined not by playoff, but by rankings. Until recently, those rankings had been strictly the accumulated wisdom of opining press-writers and coaches. Embarrassment occurred when, as in 1990, the principal polls disagreed, and selected different national champions. 

A large part of the problem was the conference alignments of the bowl games, where championships were determined. Michigan, for instance, won a national championship in 1997 by playing a team in the Rose Bowl that was not even in the top 5, because the Big 10 champ always played the Pac-10 champ in the Rose Bowl, regardless of national ramifications. 

In reaction to a growing demand for a more reliable national championship, the NCAA set up in 1998 the _Bowl Championship Series_ (BCS), consisting of an alliance among the Sugar Bowl, the Orange Bowl and the Fiesta Bowl, one of which would _always_ pit the #1 and #2 teams in the country against each other to play for the national title (unless one or more were a Big 10 or Pac-10 participant). The question was, how to guarantee best that the true #1 and #2 teams were selected... 

– 2 – 

By the time of the formation of the BCS (and even long before) many had begun to ask the question, can a machine rank the teams more correctly than the pollsters, with less bias than the humans might have? With the advent of easily accessible computer power in the 1990’s, many “computer polls” had emerged, and some even appeared in publications as esteemed as the _New York Times_ , _USA Today_ , and the _Seattle Times_ . In fact, by 1998, many of these computer rankings had matured to the point of some reliability and trustworthiness in the eyes of the public. 

As such, the BCS included computer rankings as a part of the ranking that would ultimately determine who played for the title each year. Several computer rankings would be averaged together, and that average would be averaged with the “human” polls (with some other factors) to form the best possible ranking of the teams, and hence determine their eligibility to play in the three BCS bowl games. The somewhat controversial method, despite some implausible circumstances, has worked brilliantly in producing 4 undisputed national champions. With the addition of the Rose Bowl (and its Big 10/Pac-10 alliances) in 2000, the likelihood of a split title seems very small. 

Given the importance of the computer rankings in determining the national title game, one must consider the simple question, “Are the computers getting it right?” Fans have doubted occasionally when the computer rankings have seemed to favor local teams, disagreed with one another, or simply disagreed with the party line bandied about by pundits. 

Making matters worse is that many of the computer ranking systems have appeared to be byzantine “black boxes,” with elaborate details and machinery, but insufficient description to be reproduced. For instance, many of the computer methods have claimed to include a home/away bonus, or “conference strength,” or a particular weight to opponent’s winning percentage, etc., but without a complete, detailed description, we’re left just to trust that all that information is being distilled in some correct way. 

With no means of thoroughly understanding or verifying the computer rankings, fans have had little reason to reconsider their doubts. A critical feature, therefore, of the Colley Matrix method is that this paper formally defines _exactly_ how the rankings are formed, and shows them to be explicitly bias-free. Fans may check the results during the season to verify that the method is truly without bias. 

With luck, I will persuade the reader that the Colley Matrix method: 

– 3 – 

1. has no bias toward conference, tradition, history, etc., (and, hence, has no pre-season poll), 

2. is reproducible, 

3. uses a minimum of assumptions, 

4. uses no _ad hoc_ adjustments, 

5. nonetheless adjusts for strength of schedule, 

6. ignores runaway scores, and 

7. produces common sense results. 

## **2. Wins and Losses Only—Keep it Simple** 

The most important and most fundamental question when designing a computer ranking system is simply where to start. Usually, in science, one poses a hypothesis and checks it against observation to determine its validity, but in the case of ranking college football teams, there really is no observation—there is no ranking that is an absolute truth, against which to check. 

As such, one must form the hypothesis (ranking method), and check it against other rankings systems, such as the press polls, other computer rankings, and, perhaps even common sense, and make sure it seems to be doing something right. 

Despite the treachery of checking a method against opinion, we proceed, by contemplating a methodology. The immediate question becomes what input data to use. 

Scores are a good start. One may use score differentials, or score ratios, for instance. One may even invent ways of collapsing runaway scores with mathematical functions like taking the arc-tangent of score ratios, or subtracting the square roots of scores. I even experimented with a histogram equalization method for collapsing runaway scores (which, by the way, produced fairly sensible results). 

However, even with considerable mathematical skulduggery, reliance on scores generates some dependence on score margin that surfaces in the rankings at some level. Rightly or wrongly, this dependence has induced teams to curry favor in computer rankings by running up the score against lesser opponents. The situation had degraded to the point in 2001 that the BCS committee instructed its computer rankers either to eliminate score dependence altogether or limit score margins to 21 in their codes. 

This is a philosophy I applaud, because using wins and losses only 

– 4 – 

1. eliminates any bias toward conference, history or tradition, 

2. eliminates the need to invoke some _ad hoc_ 

3. eliminates any other _ad hoc_ adjustments, such as home/away tweaks. 

By focusing on wins and losses only, we’re nearly halfway to accomplishing our goals set out in the Introduction. 

A very reasonable question may then be, why can’t one just use winning percentages, as do the NFL, NBA, NHL and Major League, to determine standings? The answer is simply that in all those cases, each team plays a very representative fraction of the entire league (more games, fewer teams). In college football, with 117 teams and only 11 games each, there is no way for all teams to play a remotely representative sample. The situation demands some attention to “strength of schedule,” and it is herein that lies most of the complication and controversy with the college football computer rankings. 

The motivation of the Colley Matrix Method, is, therefore, to use something as closely akin to winning percentage as possible, but that nonetheless corrects efficiently for strength of schedule. The following sections describe exactly how this is accomplished. 

## **3. The Basic Statistic — Laplace’s Method** 

_Note to the reader:_ In the sections to follow, many mathematical equations will be presented. Many derivations and examples will be based upon principles of probability, integral calculus, and linear algebra. Readers comfortable with those subjects should have no problem with the level of the material. 

In forming a rating method based only on wins and losses, the most obvious thing to do is to start with simple winning percentages, the choice of the NFL, NBA, NHL and Major League. But simple winning percentages have some incumbent mathematical nuisances. If nothing else, the fact that a team that hasn’t played yet has an undefined winning percentage is unsavory; also a 1-0 team has 100% vs. 0% for an 0-1 team: is the 1-0 team really infinitely better than the 0-1 team? 

Therefore, instead of using simple winning percentage ( _nw/ntot_ , with obvious notation), I use a method attributable to the famed mathematician Pierre-Simon Laplace, a method introduced to me by my thesis advisor, Professor J. Richard Gott, III. 

The adjustment to simple winning percentage is to add 1 in the numerator and 2 in the de- 



nominator to form a new statistic, 



All teams at the beginning of the season, when no games have been played, have an equal rating of 1 _/_ 2. After winning one game, a team has a 2 _/_ 3 rating, while a losing team has a 1 _/_ 3 rating, i.e., “twice as good,” much more sensible than 100% and 0%, or “infinitely better.” 

The addition of the 1 and the 2 may seem arbitrary, but there is a precise reason for these numbers; namely, we are equating the win/loss rating problem to the problem of locating a marker on a craps table by trial and error shots of dice. What? 

This craps table problem is precisely the one Laplace considered. Imagine a craps table (of unit width) with a marker somewhere on it. We cannot see the marker, but when we cast a die, we are told if our die landed to the left or right of the marker. Our task is to make a good guess as to where that marker is, based on the results of our throws. The analogy to football is that we must make a good guess as to a team’s true rating based on wins and losses. 

_r_ = 1 _/_ 2. Mathematically, we are assuming a “flat” distribution, meaning that there is equal probability that the marker is anywhere on the table, since we have no information otherwise—that is to say, a uniform Bayesian prior. The average value within such a flat distribution (shown in Fig. 1 at top left) is 1 _/_ 2. Computing If the that explicitly is called finding the expectation value (or weighted mean, or center of mass). ˆ probability distribution function of rating _r_ is _f_ (ˆ _r_ ), then in the case of no games played (no dice thrown), _f_ (ˆ _r_ ) = 1, and the expectation value of ˆ _r_ is 



ˆ at the left wall ( _r_ = 0) has to be zero — you can’t throw a die to the left of the left wall. From zero at the left wall, the the probability density must increase to the right. That increase is just linear, because the probability density is just the available space to the left of the marker where your die could have landed; the farther you go to the right, the proportionally more available space there is to the left (see Fig. 1, top right). 

The analogy with football here is clear. If you’ve beaten one team, you cannot be the worst team after one game, and the number of available teams to be worse than yours increases proportionally to your goodness, your rating ˆ _r_ . 

The statistical expectation value of the location of the marker (rating of your team) for the one 

– 6 – 

left throw (one win) case is therefore 



If we throw another die to the left, we have not a linear behavior in probability, but parabolic, since the probability densities simply multiply, 



as shown at the bottom left in Fig. 1. 

However, when a die is thrown to the right, we know that the probability at the right wall has ˆ to go to zero, and a term growing linearly from right to left is introduced, (1 _− r_ ) (in exact analogy to the left-thrown die). Therefore, if we have thrown one die to the left and one to the right, we have 



as shown at the bottom right in Fig. 1. 

In general, for _nw_ wins (left throws of the die) and _nℓ_ losses (right throws of the die), the formula is 



which recovers equation (1). It is an interesting exercise to check a few more examples. 

## **4. Strength of Schedule** 

The simple statistic developed in the last section would to produce a ranking if we were confident that all teams had played a schedule of similar strength, or for instance a roundrobin tournament. While a round-robin with 117 teams would require 6786 games, Division I-A teams play typically a tenth that, so there is absolutely no assurance that the quality of opponents from team to team is close to the same. Contrast this with the NFL, or especially the Major League, where each team plays a very healthy sample of the entire league during the regular season. 

This problem is complicated by the addition of still more teams in the form of non-I-A opponents. If one were to use those games as input, he would have to form ratings of all the I-AA teams, which would require ratings of teams in still lesser divisions, since many I-AA teams play 

– 7 – 

such opponents. Forming sensible ratings which relate Florida State to Emory & Henry is extremely difficult and is frankly beyond the scope of this method. The reason is that my method, in its simplicity, relies on some interconnectedness between opponents, which simply does not exist between a given NAIA squad and a given Division I-A squad—there’s barely enough interconnectedness among the I-A teams themselves! Most other computer rankings within the BCS system do endeavor to compute such ratings, and in my opinion, do nearly as good a job as is possible at making sense of such disparate and competitively disconnected teams. To preserve simplicity and total objectivity (no _ad hoc_ division adjustment, etc.), my rating system must ignore all games against non-I-A opponents. Therefore, _padding the schedule with I-AA teams contributes absolutely nothing to a team’s rating._ 

We may then proceed with mathematical adjustments for strength of schedule within Division I-A itself. 

The number of wins in equation (1) may be divided into _nw,i_ = ( _nw,i − nℓ,i_ ) _/_ 2 + _ntot,i/_ 2 (which the reader can check). Recognizing that the second term may be written as<sup>�</sup><sup>_ntot,i_</sup> 1 _/_ 2 allows one to identify the sum as that of the ratings of team _i_ ’s opponents, if those opponents are all random ( _r_ = 1 _/_ 2) teams. Instead, then, of using _r_ = 1 _/_ 2 for all opponents, we now use their actual ratings, which gives an obvious correction to _nw,i_ . 



where _rj_<sup>_i_is the rating of the</sup><sup>_j_thopponent of team</sup><sup>_i_.</sup><sup>_The second term (the summation) in equation_</sup> _(7) is the adjustment for strength of schedule._ 

Now, the rub. When the teams are not random, but ones which have played other teams, which may or may not have played some teams in common with the first team, etc., how does one possibly figure out simultaneously all the _rj_<sup>_i_’swhichareinputstothe</sup><sup>_ri_’s,whicharethemselves</sup> _r_<sup>_i_</sup> _j_<sup>’s for other</sup><sup>_ri_’s, etc.?</sup> 

## **5. The Iterative Scheme** 

The most obvious way to solve such a problem is a technique called “iteration,” which is employed by several of the other computer ranking methods. The way it works is one first computes the ratings, as if all the opponents were random ( _r_ = 1 _/_ 2) teams, using equation (1). Next, each team’s strength of schedule is computed according to its opponents’ ratings, using equation (7). The ratings are re-computed with the new schedule strengths, and then strengths of schedule are re-computed from the new ratings. With luck, the changes to the ratings get smaller and smaller 

– 8 – 

with each step of these calculations, and after a time, when the changes are negligibly small for any team’s rating (a part in a million, say), one calls the list of ratings, at that point, final. 

Here is a very simple example of the iterative technique, after only one week of play, where a team that has played is either 0-1 against a 1-0 team, or vice versa. Before any iterations, the basic Laplace statistic from equation (1) is computed for each team. Letting _rW,_ 0 be the initial rating of a winning team, and _rL,_ 0 be the initial rating of the losing team, one finds that equation (1) initially gives 



is just the rating of the one opponent) is made by computing _n_<sup>_eff_</sup> _w_ for each team, using equation (7): 



Because the 1-0 team beat a 0-1 team, worse than an average team, the 1-0 team is punished, and given only 5 _/_ 6 of a win, whereas the losing team lost to a 1-0 team, better than an average team, and is rewarded by suffering only 5 _/_ 6 of a loss. One can see how the method explicitly gives to one team only by taking from another. 

The next step is to re-compute the ratings, given the new _n_<sup>_eff_</sup> _w_ values. Plugging back into equation (1) yields: 



Let’s look at just one more iteration. 



Ratings After Second Iteration 



If one examines the ratings of the winning team after the zeroth, and second iterations, one finds that the values _rW,{_ 0 _,_ 1 _,_ 2 _} ≈{_ 0 _._ 6667 _,_ 0 _._ 6111 _,_ 0 _._ 6296 _}_ , show first a correction down, then 

– 9 – 

a correction up, by a lesser amount. Corrections that alternate in sign, and shrink in magnitude are hallmarks of _convergence_ , meaning that with each iteration, the scheme is closer to finding a final, consistent value. Table 1 shows how these numbers converge to a part in a million after 11 iterations. 

converging series (compare to Table 1), 



where the last line is the standard formula for the sum of a geometric series. In this simple case, the iterative method converges rapidly and stably, as a classic alternating geometric series. 

Also note that the results converge to an average rating of 1/2, which is the same average as if there had been no game played at all; average rating has been conserved. 

The ratings may converge nicely, but how can one know that these are the _right_ answers? Furthermore, is the method extensible to the prodigiously more complicated case of 117 teams having played 11 or 12 games each? 

## **6. The Colley Matrix Method** 

The previous section showed how an iterative correction for strength of schedule could provide consistent results that make intuitive sense for the simple one game case, but left us with the question of how do we know that the result is really right? 

Referring to equations (1) and (7), we have 



A simple rearrangement gives 



a simple two-variable linear system. Plugging in the results from the iterative technique (Table 1), one discovers that indeed _rW_ = 5 _/_ 8 and _rL_ = 3 _/_ 8 work exactly. 

– 10 – 

This exercise illustrates that linear methods can be used for two teams, but begs the question, can the ratings of many teams, after many games, be computed by simple linear methods? 

## **6.1. The Matrix Solution** 

Returning to equations (1) and (7), using the same definitions for _ri_ and _rj_<sup>_i_,onefindsthat</sup> equations (1) and (7) can be rearranged in the form: 



which is a system of _N_ linear equations with _N_ variables. 

It is convenient at this point to switch to matrix form by rewriting equation (16) as follows, 



where _⃗r_ is a column-vector of all the ratings _ri_ , and _⃗b_ is a column-vector of the right-hand-side of equation (16): 



The matrix _C_ is just slightly more complicated. The _i_<sup>th</sup> row of matrix _C_ has as its _i_<sup>th</sup> entry 2+ _ntot,i_ , and a negative entry of the number of games played against each opponent _j_ . In other words, 



where _nj,i_ is the number of times team _i_ has played team _j_ . 

_The matrix C is as the_ **Colley Matrix** _. Solving equations (17)–(19) is the method for rating the teams._ In practice, the matrix equation is solved in double precision by Cholesky decomposition and back-substitution (faster and more stable than Gauss-Jordan inversion, for instance [e.g., Press et al. 1992]). The Cholesky method is available, because the matrices are not only (obviously) symmetric and real, but are also positive definite, which will be discussed in the next section. 

## **6.2. Equivalence of the Matrix and Iterative Methods** 

The matrix method has been shown to agree with the iterative method in the simple one game case. The question is whether the agreement extends to more complex situations. In a word, “yes,” but why? 

– 11 – 

There is no dazzingly elegant answer here. If the iterative scheme converges, then equations (1) and (7) are more nearly mutually satisfied with every iteration; otherwise the ratings would have to diverge at some point. When the ratings have converged, and iterating no longer introduces any changes to the ratings, the equations themselves have become simultaneously satisfied—the convergent ratings values have solved equations (1) and (7). Because those equations are identically the same ones solved by the matrix method, the matrix and iterative solutions must be identical as long as the iterative method remains convergent. 

The question then becomes shifted to one of the convergence itself, which has been discussed only by example to this point. The convergence is due principally to _n_ +2 denominator in equation (1). I shall not give a rigorous proof as to _exactly_ why this is so, but rather motivate the idea in a less rigorous way. 



where _⃗ρ ⃗δ_ the vector of errors. Let us consider the simple case where _⃗δ_ has only one non-zero component, say _δ_ 1 = 0. Assuming a round-robin schedule (the slowest to converge), the iterations would proceed as in Table 2. The convergence in Table 2 is slow, with the errors decreasing by _∼ n/_ ( _n_ + 2) in each iteration. In practice, the college football schedule is not round-robin outside of each conference, so the convergence factor is more like _∼_ ( _n −_ 2) _/_ ( _n_ + 2) _≈_ 10 _/_ 14 _≈_ 0 _._ 71, so convergence to a part in 10<sup>7</sup> occurs in about 48 iterations. In the 2000 season, for instance, the number of iterations required before median ratings correction fell below 10<sup>7</sup> was 60, so this very simple estimate is correct to 20% for a typical case. 

Of course, in reality there are errors in more than one of the ratings, but, because the equations are linear, the principle of superposition applies, and the above calculation changes very little. 

While the preceding is no proof that the scheme is always convergent, the round-robin case is the slowest to converge, and even in that case, we have shown that any error in a single rating does vanish over time, and superposition extends that to errors in multiple ratings. In the sparser case of an actual college football season the convergence can be slightly faster for some teams. 

It should be noted that if it weren’t for the +2 in the denominator of equation (1), the convergence would not occur, since, in the round-robin case, the error decrement would be by a factor of _∼ n/n_ = 1, so if this method were based strictly on winning percentages, rather than Laplace’s formula, it would fail. 

The iterative scheme produces convergent ratings, which upon convergence simultaneously satisfy equations (1) and (7), which are exactly those that the matrix method solves; therefore, the iterative and matrix solutions must be equivalent (and, in practice, are equivalent). 

– 12 – 

## **6.3. Examples of the Colley Matrix Method** 

We now consider two examples to illustrate the matrix method in action. First, let us return to our friend, the simple two team, one game case. There, we discovered that the ratings could be determined from the linear system 



Rewriting this in matrix form, 



we recognize that _rW_ and _rL_ can be determined by simply inverting the matrix and multiplying by the solution vector on the right hand side. 



verifying the iterative and linear solutions. 

_a–e_ . Their records against each other are shown thus (the initial and final ratings are listed for reference, the latter of which will be solved for forthwith): 



The matrix equation, according to equations (17)–(19) is written 



– 13 – 

Solving the matrix equation yields sensible results: 



As with the two team case, the ratings average to exactly 1/2 (23/46). Notice that team _b_ , having played a 2-1 team and a 2-2 team, is rated higher than team _d_ , having played a 1-2 team and a 2-2 team, despite identical 1-1 records: an example of how strength of schedule comes into play. Finally, there is consistency in that team _c_ has a rating of exactly 1/2, because that team is 2-2 against teams whose ratings average to exactly 1/2. 

## **7. Comments on the Colley Matrix Method** 

There has been discussion of the fact that the matrix method (and the iterative method) conserves an average ranking of 1/2. The reason I emphasize that point is that, as such, the ratings herein require no renormalization. All teams started out with a rating of 1/2, and only by exchange of rating points with other teams does one team’s rating change. The first subsection below shows why the rating scheme explicitly conserves total ratings points. The subsection which follows establishes that the matrix in equation (17) is indeed positive definite, which allows for quick and stable solution of the matrix equation. The last subsection shows that the matrix _C_ is singular if winning percentages are used in place of Laplace’s formula, and thus, the method cannot be used with straight winning percentages. 

## **7.1. Conservation of Average Rating** 

Why does the matrix solution always preserve the average rating of 1/2? We can tackle this problem by examining the construction of the matrix _C_ . From the definition of the matrix _C_ in equation (19), it follows that the matrix can be represented as: 



– 14 – 

where _I_ is the identity matrix, and _G_<sup>_k_</sup> is a matrix operator added for each game _k_ . _G_<sup>_k_</sup> always has the form that _G_<sup>_k_</sup> _ii_<sup>=</sup><sup>_Gk_</sup> _jj_<sup>= 1, and</sup><sup>_Gk_</sup> _ij_<sup>=</sup><sup>_Gk_</sup> _ji_<sup>=</sup><sup>_−_1, with all other entries 0, like this:</sup> 



Carrying out the multiplication _⃗r_<sup>_′_</sup> = _G_<sup>_k_</sup> _r_ , we find that the _i_<sup>th</sup> and _j_<sup>th</sup> entries in _⃗r_<sup>_′_</sup> are _ri − rj_ , and _rj − ri_ , respectively, while all other entries in _⃗r_<sup>_′_</sup> are obviously zeroes. The sum of all the _⃗r_<sup>_′_</sup> values, is, therefore, zero, no matter what the values of _⃗r_ . Hence, 



What about the other side of equation (17), _⃗b_ ? The of _bi_ from equation (18) is _bi_ = 1 + ( _nw,i − nℓ,i_ ) _/_ 2. It is easy to see that the total of the _bi_ ’s must be _N_ , since each win by one team must be offset by a loss by that team’s opponent, so that the total number of wins must equal the total number of losses, and therefore,<sup>�</sup> _bi_ = _N_ . 

So, summing both sides of equation (17), we have 





i.e., the average value of _r_ is exactly one-half. 

## **7.2.** 

In order to use Cholesky decomposition and back substitution to solve the matrix equation (17), the matrix _C_ must be positive definite, such that, for any non-trivial vector _⃗v_ , this inequality holds 



Recalling our separation of _C_ into 2 _I_ +<sup>�</sup> _k_<sup>_Gk_, and noting that matrix multiplication is distribu-</sup> tive, ( _A_ + _B_ ) _⃗v_ = _A⃗v_ + _B⃗v_ , we can examine the inequality piece-wise. Obviously the matrix 2 _I_ is 



positive definite, which leaves the _G_<sup>_k_</sup> ’s. In the subsection above, we discovered that the multiplication _G⃗r_ yielded zeroes in all entries, except the _i_<sup>th</sup> and _j_<sup>th</sup> which contained _ri − rj_ and _rj − ri_ , respectively. The product _⃗r_<sup>_T_</sup> ( _C⃗r_ ) is thus computed as 



Since ( _ri − rj_ )<sup>2</sup> _≥_ 0, and _⃗r_<sup>_T_</sup> (2 _I⃗r_ ) _>_ 0, the matrix _C_ must be positive definite. 

## **7.3. Singularity of** _C_ **for Straight Winning Percentages** 

We have seen that the iterative method would fail if straight winning percentages were used (i.e. if one removed the +1 and +2 from the numerator and denominator in equation [1]). In performing the same exercise with the matrix method, equation (19) would change _C_ into a singular matrix! 

For the one game case, the result is obvious. 



obviously singular. In the general case, it’s easy to see from equation (19) that if one removes the addend of 2 from _cii_ , the total of the _cij_ ’s for any row or any column is zero. Therefore, in performing the legal row operation of adding all the rows, one has produced a row of all zeros; hence the matrix is singular. The matrix method, like the iterative method, cannot work with simple winning percentages. 

## **8. Performance** 

the next question is how well does the method perform. Answering that question is difficult because we do not actually know the “truth.” We simply do not know in any precise way how good Western Michigan is relative to Hawaii; therefore there is really nothing to check our results against. 

The best we can do is compare our results to the venerable press polls, just as a mutual sanity check. Before I even begin, I should caution that the press polls are artificially correlated simply because the coaches are well aware of the AP poll, and the press writers are well aware of the Coaches’ poll. Nonetheless we shall proceed. 

against the Coaches’ Poll rankings for 1999–2002. The first thing to notice is that the national 

– 16 – 

champion is agreed upon every year in all three ranking systems, which is ultimately the most important test for our purposes. Just scanning down the lists, the rankings are usually quite consistent within a few places, with an occasional outlier. 

To quantify the agreement, I have found it more useful to think in terms of ranking ratios, or percentage differences, rather than simple arithmetic ranking differences. I have previously used the median absolute difference as a figure of merit, but have concluded this statistic poorly describes the behavior of the ranking comparisons. To show that, I have plotted in Fig. 2 the arithmetic differences _(top)_ and ratios _(bottom)_ of my rankings vs. the press rankings for 1999– 2002 (all lumped together). In the plots, the histograms for the AP and Coaches’ rankings are over-plotted (they’re very similar). 

Throwing all six groups together (three years, AP, Coaches), one can compute the direct average and variance of the distributions, which are listed as “avg” and “s” on the plots (yes, _s_ is the square-root of the variance, and has a � _n/_ ( _n −_ 1) factor). The corresponding normal curve is plotted as a dotted line. Another way of finding the mean and variance of a distribution is to fit the integral of the normal curve—that’s _P_ ( _x_ ) for you calculator statisticians, or the error function with _√_ 2’s in the right places for you math pedants—to the cumulative distribution. I have plotted those resulting normal curves as solid lines at top and bottom. If a distribution is normal, these two methods should be nearly identical. Obviously at top, the two curves are not so identical, but at bottom things seem much better. 

Of course there are dozens of formal ways to check “Gaussianity” of a distribution, but I don’t want to belabor the point. I just want to illustrate that the ratios are much better behaved than the arithmetic differences. What does this mean? It means that it’s much more accurate to say my rankings disagree with the press rankings by a typical percentage, rather than by a typical number. 

To compute that typical percentage, one may average the absolute differences of the logs of the rankings, as such, 



where _i_ is the press ranking (either AP or coaches), and _jC_ (team _i_ ) is the Colley ranking of that team. It’s hard to come up with a good name for this statistic, _η_ ; perhaps “mean absolute ratio.” Anyway, I list that statistic at the bottom of Table 3 for each of the 4 years of the BCS. The values are typically about 1.25, which means that my rankings agree with the press rankings within about 25% in either direction, so you might have an error of 1 ranking place at around #5, but about 5 places by #20. Inspecting the columns of Table 3 shows this to be quite a good description of the relative rankings. 

Is that a _good_ agreement? 

– 17 – 

Who knows, really? But to me (at least) the agreement is surprisingly good: 

- The press polls started with a pre-season poll, with all the pre-conceived notions of history and tradition such an endeavor demands, then week by week allowed their opinions and judgments to migrate, being duly impressed or disappointed in the styles of winning and losing by certain teams, being more concerned about recent games than earlier ones, perhaps mentally weighting games seen on television as more important, perhaps having biases (good or bad) toward local schools one sees more often... _ad nauseam_ . 

- My computer rankings started with nothing, literally no information, but then, given only wins and losses, generated a ranking with pure algebra. 

That two such processes produce even remotely consistent results is, frankly, remarkable to me. 

I hope in this section we can agree to have learned, despite a lack of “truth” data, comparison of the press polls and my rankings shows both that the press and coaches must not be too loony, and that the Colley Matrix system yields common sense results. 

## **9. Conclusions** 

Colley’s Bias Free College Football Ranking Method, based on solution of the Colley Matrix, has been developed with several salient features, desirable in any computer poll that claims to be unbiased. 

1. It has no bias toward conference, tradition, history, or prognostication. 

2. It is reproducible; one can check the results. 

3. It uses a minimum of assumptions. 

4. It uses no _ad hoc_ adjustments. 

5. It nonetheless adjusts for strength of schedule. 

6. It ignores runaway scores. 

7. It produces common sense results that compare well to the press polls. 

This information, the weekly poll updates, as well as useful college football links may be found on the Internet home for Colley’s Rankings: 

`http://www.colleyrankings.com/` . 

WNC would like to thank A. Peimbert and J. R. Gott for their contributions in many lively 

– 18 – 

discussions on the subject of rankings. All programming for this method was done by WNC in IDL, FORTRAN, C, C++, Perl and shell script in the Solaris Unix and Linux environments. 

## **REFERENCES** 

Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P., 1992, _Numerical Recipes in FORTRAN_ , Cambridge University Press, Cambridge, UK, pp. 89-91 

This preprint was prepared with the AAS L<sup>A</sup> TEX macros v5.0. 

– 19 – 

## **Convergence of Ratings via Iteration** 

|**Iteration**|**Winning Team’s Rating**|**Losing Team’s Rating**|
|---|---|---|
|0|0.666667|0.333333|
|1|0.611111|0.388889|
|2|0.629630|0.370370|
|3|0.623457|0.376543|
|4|0.625514|0.374486|
|5|0.624829|0.375171|
|6|0.625057|0.374943|
|7|0.624981|0.375019|
|8|0.625006|0.374994|
|9|0.624998|0.375002|
|10|0.625001|0.374999|
|11|0.625000|0.375000|



one game case. The initial ratings are 2/3 for the winner and 1/3 for the loser, before any adjustment for schedule strength. Moving down the table are successive adjustments for strength of schedule. Because the winning team beat a below average (0-1) team, while the losing team lost to an above average (1-0) team, the final ratings are lower for the winning team, and greater for the losing team than were the initial ratings. 

– 20 – 

## **Iterative Convergence of Ratings in a Round-Robin** 

|iter.<br>team 1|other teams|
|---|---|
|1.<br>_r →ρ_+_δ_1<br>_n_<sup>_eff_</sup><br>_w_<br>=_ν_<sup>_eff_</sup><br>_w_|_r_ =_ρ_<br>_n_<sup>_eff_</sup><br>_w_<br>_→ν_<sup>_eff_</sup><br>_w_<br>+_δ_1|
|2.<br>_r_ =_ρ_<br>_n_<sup>_eff_</sup><br>_w_<br>=_ν_<sup>_eff_</sup><br>_w_<br>+_nδ_1_/_(2 +_n_)|_r_ =_ρ_+_δ_1_/_(2 +_n_)<br>_n_<sup>_eff_</sup><br>_w_<br>=_ν_<sup>_eff_</sup><br>_w_<br>+ (_n −_1)_δ_1_/_(2 +_n_)|
|3.<br>_r_ =_ρ_+_nδ_1_/_(2 +_n_)<sup>2</sup><br>_n_<sup>_eff_</sup><br>_w_<br>=_ν_<sup>_eff_</sup><br>_w_<br>+_n_(_n −_1)_δ_1_/_(2 +_n_)<sup>2</sup>|_r_ =_ρ_+ (_n −_1)_δ_1_/_(2 +_n_)<sup>2</sup><br>_n_<sup>_eff_</sup><br>_w_<br>=_ν_<sup>_eff_</sup><br>_w_<br>+ [(_n −_1)<sup>2 </sup>+_n_]_δ_1_/_(2 +_n_)<sup>2</sup>|
|4.<br>_r_ =_ρ_+_n_(_n −_1)_δ_1_/_(2 +_n_)<sup>3</sup><br>...|_r_ =_ρ_+ [(_n −_1)<sup>2 </sup>+_n_]_δ_1_/_(2 +_n_)<sup>3</sup><br>...|



Table 2: Iterative convergence in a round-robin. Ratings _r_ and effective wins _n_<sup>_eff_</sup> _w_ are computed from equations (1) and (7) in each iteration. Starting with the correct (final) values, _ρ_ and _νw_<sup>_eff_, an</sup> error _δ_ 1 is added to team 1’s rating. Column 1 gives the propagation of that error in team 1 through 4 iterations; Column 2 does the same for all other teams (whose errors will be equivalent). As one moves down the table, the errors shrink (slowly). 

– 21 – 

## **Comparison of Final Rankings with Press Polls** 

||||ColleyR<br>|anking|for Teams wi<br>|th Give<br>|n Press Rank<br>|<br>||
|---|---|---|---|---|---|---|---|---|---|
|**press**|**1998**||**1999**||**2000**||**2001**||**2002**|
|**rank**|**AP**|**AP**|**Coaches**|**AP**|**Coaches**|**AP**|**Coaches**|**AP**|**Coaches**|
|1|1|1|1|1|1|1|1|1|1|
|2|2|5|2|3|3|3|3|3|3|
|3|3|2|5|2|2|4|4|2|2|
|4|6|11|11|5|6|2|2|4|4|
|5|8|3|3|6|5|6|6|5|5|
|6|4|7|7|4|4|10|10|6|11|
|7|10|4|4|7|8|8|5|11|6|
|8|5|6|6|8|11|5|8|8|8|
|9|11|10|10|11|7|7|7|7|7|
|10|9|8|8|9|13|11|13|12|12|
|11|7|9|9|13|9|13|11|10|14|
|12|13|13|12|22|22|9|9|14|17|
|13|12|12|15|19|19|15|15|13|13|
|14|17|15|13|17|12|12|12|19|20|
|15|16|14|14|10|17|16|16|17|18|
|16|22|24|24|12|10|14|17|18|19|
|17|14|28|23|15|30|17|14|9|9|
|18|19|23|17|20|23|31|31|20|24|
|19|20|17|28|29|15|18|18|24|32|
|20|23|18|22|30|20|20|20|21|23|
|21|24|21|18|23|29|30|21|15|21|
|22|15|27|27|28|27|24|28|25|28|
|23|27|22|21|14|18|28|30|28|15|
|24|21|16|29|27|14|33|19|32|26|
|25|26|26|16|18|32|19|24|23|25|
|_η_<br>Colleyvs. poll|1_._224|1_._309|1_._281|1_._287|1_._331|1_._262|1_._232|1_._200|1_._253|
|AP vs. Coaches|n/a|1|_._071||1_._098|1|_._037||1_._082|



Table 3: Comparison of rankings to AP Poll for 1998–2002, and to the Coaches’ Poll for 1999–2002. At bottom is a statistic _η_ , described in the text. Essentially, it is the typical ratio of the Colley ranking to the poll ranking, or vice versa, so that the larger of the two always in the numerator, (specifically _η_ is the exponent of the mean of the absolute values of the logs of the ratios), so _η_ = 1 _._ 25 means the rankings would differ by typically one place at #4, and 5 places at #20. 

– 22 – 









Fig. 1.— Probability distribution functions for the Laplace dice problem, analogous to rating by wins and losses. At top left is the initial condition _{_ no dies thrown; no games played _}_ . At top right is _{_ one die left; one game won _}_ : the probability density must be zero at the left. At bottom left is _{_ two dies left; two games won _}_ : the probability densities multiply. At bottom right is _{_ one die left, one die right; one game won, one game lost _}_ : the probability density must be zero at the left and at the right. The functions here have been normalized to have an integral of one, which is irrelevant in section 3 of the text, because the normalizations explicitly divide out. 

– 23 – 





Fig. 2.— Two different ways for comparing the Colley Rankings with the Press Polls. _(at top)_ Arithmetic differences, (Colley _−_ press), between the final rankings for 1999–2002 for both the AP and Coaches’ polls. Over-plotted are the normal curves from direct measurement of mean (= _avg_ ) and standard deviation (= _s_ ), and from fitting for the mean (= _µ_ ) and standard deviation (= _σ_ ). _(at bottom)_ Same plots, but for ratios (Colley _÷_ press) in logarithmic space. 


