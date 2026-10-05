<!-- source: library/journals/Wharton Sports Analytics Journal/2022/2022 - Predicting the Quarterback-MVP in the NFL - Brill et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/predicting-the-quarterback-mvp-in-the-nfl/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2022 -->
<!-- authors: Ryan S. Brill; Ryan Weisman -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Predicting the Quarterback­MVP

Ryan Brill and Ryan Weisman

July 2021

## Abstract

The NFL MVP award is chosen each year by a panel of 50 sportswriters who are selected by the Associated Press. As the MVP is chosen by humans who do not necessarily base their decision on statistics, but on watching all the games and talking to coaches and players, it is natural to wonder whether there is a mathematical rule that can describe the MVP selec­ tion process. Hence in this paper, we create a logistic regression model to predict the NFL Quarterback­MVP. Our algorithm predicts the correct Quarterback MVP in each year since 2003 except 2009 and 2015. In 2009, our model chooses Brees over Manning, and in 2015, our model chooses Palmer over Newton. Perusing articles from 2009 and 2015 reveals that many people in the media agreed with our model that Brees and Palmer were snubbed.

Keywords: NFL MVP, logistic regression, media bias

## 1 Introduction

The NFL MVP award is chosen each year by a panel of 50 sportswriters who are selected by the Associated Press. As the MVP is chosen by humans who do not necessarily base their decision on statistics, but on watching all the games and talking to coaches and players, it is natural to wonder whether there is a mathematical rule that can describe the MVP selection process. So, our task is to create a statistical model that can predict the NFL MVP.

Since 1987, only quarterbacks (QBs) and running backs (RBs) have won the MVP [1], with QBs taking the majority of the MVPs (79% = 27/34). Hence we restrict our analysis to QBs.

## 2 The Features

Our first task is to create a model that selects the QB­MVP. We begin by assembling a dataset of QB statistics from nflfastR [2], which contains play­by­play data. We aggregate the play­by­play data into season­level statistics, so each row of the dataset includes the statistics of a given QB in a given year. We add an indicator column MVP which is a 1 if a given QB won the MVP in a given year, based on the datatable from [1]. Because we want to predict the QB­MVP, and we have a binary output column MVP, it is natural to use logistic regression. Note that we restrict ourselves to data since 2003 to keep our dataset relatively modern, and we remove 2005, 2006, and 2012 because RBs won the MVP that year. We also restrict ourselves to QBs with over 150 pass attempts.

After toying with many different combinations of features, we found the feature combination that works the best. These features are given by the following table.

Wharton Sports Analytics Student Research Journal feature name tot_td_rank tot_yard_rank win_rank epa_rank tot_ints feature description given the year, rank this QB’s total touchdowns (TDs) given the year, rank this QB’s total yards given the year, rank this QB’s team’s number of wins given the year, rank this QB’s EPA (expected points added) given the year, the number of interceptions thrown by this QB

Note that to rank a statistic such as total TDs in a given year is to take the vector of total TDs scored by all the QBs in a given season, order this vector from largest to smallest, and then assign the positive integers 1, 2, 3, ... to this ordered vector. Ties in the ranking are settled by averaging. We get such a ranking with the base­R function rank. For example, the ranking of the vector (40, 43, 37, 40) is (2.5, 1, 4, 2.5). For the majority of the features, we decided to use rankings instead of absolute numbers (i.e., a QB’s total TDs rank instead of his number of total TDs) because the MVP is a comparative award ­ if you perform better than all the other QBs, then you win the MVP ­ there is no absolute threshold in the number of yards or touchdowns needed in order to win MVP. Another reason we used rankings is that rankings prevent statistical inflation from ruining our model. For example, in 2003 Peyton Manning threw for a league­high 4267 yards, whereas in 2016 Drew Brees threw for a league­high 5208 yards. Over the last 20 years, the average number of passing yards has experienced inflation, but we don’t want our model to think less of Manning in 2003.

## 3 Training the Model

We train our logistic regression model on data from 2003 to 2016, excluding the years that RBs won MVP (2005, 2006, and 2012), and we use the data from 2017 to 2020 as hold­out data for testing. This yields 11 years of training data. Since we restrict to QBs with at least 150 pass attempts in a given season, we are left with 432 player­seasons worth of data. 12 of these correspond to MVP player­seasons (12, not 11, because in 2003 both Steve McNair and Peyton Manning won the MVP). The coefficients of the trained model are given in the following table. feature name intercept tot_td_rank tot_yard_rank win_rank epa_rank tot_ints coefficient 7.749 ­0.685 ­0.0401 ­0.492 ­0.572 ­0.263 coefficient symbol β0 βtd βyd βwin βepa βint

Note βtd is negative, which indicates that having a low total touchdown rank­value (i.e. 1, 2, 3), which corresponds to scoring more touchdowns than ones peers, is associated with a higher probability of being MVP according to the logistic regression model. This makes sense, because touchdowns are the most important scoring play in football, and so MVPs should score more touchdowns than their peers. By similar logic, it makes sense that βyd, βwin, and βepa are negative. Moreover, it makes sense that βint is negative, because it indicates that throwing more interceptions is associated with a lower probability of being MVP.

## 4 The Classification Algorithm

We now describe the algorithm used to classify a given player­season as a Quarterback­MVP. Given the season s, define for each quarterback q the MVP­score Ms(q) by the logistic regression model applied

Brill, Weisman

Wharton Sports Analytics Student Research Journal to that quarterback’s season statistics:

(

)

Ms(q) := L β0 + βtdx(tdq,s) + βydxy(qd,s) + βwinxw(qi,ns) + βepaxe(qp,as) + βintxi(nq,ts) , where L is the logistic function

## 1 L(z) = 1 + e−z ,

xt(dq,s), xy(qd,s), x(wqi,ns), x(eqp,as), and xi(nq,ts) are quarterback q’s total touchdown rank, total yards rank, win rank, epa rank, and total number of interceptions during season s, and β0, βtd, βyd, βwin, βepa, and βint are the associated coefficients given by the previous table.

Then, we normalize the MVP­scores during season s so that they sum to 1, in order to interpret Ms(q) as the probability that quarterback q wins MVP during season s, and to put each season on the same scale so as to allow comparison between seasons:

Ms(q)

←

∑Ms(q) . r Ms(r)

Finally, we classify the QB­MVP of season s as the quarterback q(s)∗ with the highest predicted prob­ ability of winning MVP during that season: q(s)∗ := arg max Ms(q). q

## 5 Testing the Model

Recall that we trained the logistic regression model, and hence the classification algorithm, on data from 2003 to 2016 (excluding 2005, 2006, and 2012). Our algorithm picks the wrong MVP in 2009 and 2015, picks one of the two MVPs in 2003 (recall that both Steve McNair and Peyton Manning won the MVP in 2003 [1]), and picks the correct MVP during the other 8 seasons of training data. Counting 2003 as half­correct, this yields a training accuracy of 8.5/11 = 77%. Furthermore, we used the data from 2017­2020 as hold­out data. Our algorithm picks the correct MVP in each of these four seasons, yielding a testing accuracy of 100%.

Note that adding two extra features, tot_games_played (total number of games played) and cpoe_rank (rank each QB’s average CPOE (completion percentage over expected)), increases the training accuracy to 9.5/11 = 86% by correctly picking the 2015 MVP Cam Newton, while retaining the 100% testing accu­ racy. However, adding these features causes some of the other coefficients, including βyd, to be positive instead of negative, which is problematic. If βyd were positive, then gaining more yards, which leads to a lower rank­value for total yards, would be associated with a lower probability of being MVP, which makes no sense. This is a sign of over­fitting, and so we decide to stick with the simpler model without these extra features, despite the lower training accuracy.

## 6 Example Seasons

The following table shows the data for the top 5 QB­MVP candidates from the most recent NFL sea­ son (2020), ranked by the probability of winning MVP according to our logistic regression model. Aaron Rodgers edges out Patrick Mahomes by having more touchdowns, a higher EPA, and fewer interceptions. Even though Mahomes has significantly more total yards than Rodgers, we recall that βyd is much smaller in magnitude than the other coefficients, so total yards rank matters less than the other features.

Brill, Weisman

Wharton Sports Analytics Student Research Journal

One of the most dominant MVP seasons in NFL history is given by Peyton Manning’s record 5th MVP season in 2013. As a Bronco, Manning threw for a single­season record 5477 yards, and a single­season record 55 touchdowns. He was rewarded with 49 of 50 MVP votes (one arrogant Patriots homer voted for Tom Brady) [3]. Our model gives Manning a .978 probability of winning MVP, which matches his nearly unanimous winning of the award. The following table shows the data for the top 5 QB­MVP candidates from 2013, as ranked by our model.

The most recent NFL season involving a tie in the MVP race is 2003, when both Peyton Manning and Steve McNair won co­MVP by each receiving 16 votes [4]. Our model gives a slight edge to Manning, which makes sense because he had more touchdowns, more yards, and the same amount of team wins. So, why did McNair and Manning share the award? Reddit seems to be the only source where we found a decent discussion on why they shared the award despite Manning’s statistical dominance [5]. One user mentions a “you had to be there” quality, where McNair battled through injuries and put an inferior team on his back, to end up with the same record as Manning’s Colts, in the same division. It’s tough to quantify such narratives and put them in a model, so we’re not too upset that our model only picked Manning as the rightful MVP. Note that the following table shows the data for the top 5 QB­MVP candidates from 2003, as ranked by our model.

Brill, Weisman

Wharton Sports Analytics Student Research Journal

Now, we examine the two seasons in which our model chooses the wrong QB: 2009 and 2015. In 2009, our model chooses Drew Brees as the MVP over the actual winner Peyton Manning. Similarly, many sources on the internet claim that Drew Brees was massively snubbed in 2009. For instance, at the end of the 2009 season, Joe Gerrity of Bleacher Report wrote a piece entitle “Drew Brees Snubbed: Manning’s MVP Selection Shows Prejudice Amongst Voters” [6]. He argues that Brees was statistically superior in 2009, as he had more touchdowns, more yards per pass, fewer interceptions, a higher passer rating, and a higher completion percentage than Manning, and Brees only had a worse team record (by one game) because the Saints clinched the number one seed early. Gerrity thinks Manning edged out Brees simply because he is the “darling of the NFL”. Note that the following table shows the data for the top 5 QB­MVP candidates from 2009, as ranked by our model.

Lastly, we examine 2015. Our model chooses Carson Palmer as the MVP, picks Tom Brady as the second best, and puts the actual MVP Cam Newton in third place, as indicated in the table below. 2015 seems to be the greatest shortcoming of our model. However, according to Chase Stuart of the Wash­ ington Post, and Panther’s Coach Ron Rivera, Newton won for a similar reason as McNair in 2003: he had similar production to his competitors (Palmer and Brady) despite having a worse supporting cast [7]. Stuart writes “”On paper, Palmer has the better case, but then there’s the issue of supporting cast. Palmer certainly benefits from a great one, while Newton’s is... more complicated to evaluate. His top two wide receivers are Ted Ginn and Jerricho Cotchery, two players who would struggle to make some NFL rosters, much less starting lineups.” Rivera echoed these sentiments, saying “You’ve got to be willing to look be­ yond the numbers – quarterback rating, the completion percentage, stuff like that – and say, OK, what else is it? Is it about scoring touchdowns? Is it about throwing touchdown passes? Is it about completions? Or is it about winning too?” So, at least anecdotally, it appears that statistics didn’t completely determine the MVP in 2015, which makes us feel a bit better that our model failed to correctly predict the 2015 MVP. However, it is possible that adding a feature to quantify the quality of one’s supporting cast may help our model pick Newton in 2015. Alternatively, it is possible that in some years, statistics don’t account for the full MVP selection process.

Brill, Weisman

Wharton Sports Analytics Student Research Journal

## 7 Future Work

In this article, we used logistic regression to create a classifier to predict the QB­MVP. However, we know that not all MVPs are QBs. Specifically, since 1987, only quarterbacks and running backs (RBs) have won the MVP [1], with QBs taking the majority of the MVPs (79% = 27/34). So, the next step in creating an MVP classifier is to account for RBs. To do so, we suggest devising a logistic regression model to select the RB­MVP. Then, we suggest creating a third model to select the NFL MVP by choosing between the QB­MVP and RB­MVP given by the two logistic regression models.

## 8 Code

Our code is available on github at https://github.com/snoopryan123/QBMVP.

Brill, Weisman

Wharton Sports Analytics Student Research Journal

## References

[1] Associated press nfl most valuable player award. https://en.wikipedia.org/wiki/Associated_ Press_NFL_Most_Valuable_Player_Award.

[2] nflfastr. https://www.nflfastr.com.

[3] Peyton manning wins 2013 nfl most valuable player award. https://www.usatoday.com/story/ sports/nfl/broncos/2014/02/01/peyton-manning-2013-nfl-mvp-denver-broncos-super-bowl/ 5124453/.

[4] Manning, mcnair in rare mvp tie. https://www.espn.com/nfl/news/story?id=1698744.

[5] Anyone who remembers vividly the 2003 season, why was mcnair co­mvp with peyton man­ ning? https://www.reddit.com/r/nfl/comments/5lxhoq/anyone_who_remembers_vividly_the_ 2003_season_why/.

[6] Drew brees snubbed:

Manning’s mvp selection shows preju­ dice amongst voters. https://bleacherreport.com/articles/

322892-drew-brees-snubbed-mannings-mvp-selection-shows-prejudice-among-voters.

[7] 2015­16 nfl mvp: Winner prediction and complete odds for top candidates. https://bleacherreport. com/articles/2605348-2015-16-nfl-mvp-winner-prediction-and-complete-odds-for-top-candidates.

Brill, Weisman
