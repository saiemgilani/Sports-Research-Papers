<!-- source: library/conferences/New England Symposium on Statistics in Sports/2019/2019 - A SHINY Markov Machine for Decision-Making in MLB - Unknown Authors.pdf -->

## Attempt a Steal? 

# **A SHINY Markov Machine for decision-making in MLB** 



Whether or not to steal is a 2018 success question. Marginal league rate was 0.72 (app default). Announcers sometimes give .7 or .75 as the threshold beyond which it makes sense to steal. Main Point: threshold for **P** ( **SB** ) where marginal run expectancy after a stolen base attempt exceeds that when not attempting a stolen base depends on many things . . . 

**2019 New England Symposium on Statistics in Sports, Sept, 2019 Jason A. Osborne (NCSU), Melody Wen (NC School of Sci & Math), Daniel Dulaney (Pittsburgh Pirates)** Introduction 

URL : http://shiny.stat.ncsu.edu/jaosborn/MLBdecideR 



_•_ who’s up, who’s on deck, and the entire lineup! 



<!-- Start of picture text -->
Agreement between observed and Markov<br>= = •<br>means not bad, r 2018 0 . 85 , r 2019  how many outs, what inning!<br>0 . 84:<br>The same is true for consideration of  P ( R >  0).<br>Comparison of Observed Mean vs. Markov Mean<br>2018 Consider 2019 Braves’ Ronald Acu˜na.<br>6<br>SB attempts as leadoff hitter in 65 games: 24<br>G<br>BOS<br>G 2<br>NYY SB attempts as cleanup hitter in 36 games:<br>CLE<br>5 G OAK G G LAD G<br>HOU COL<br>CHC ATL G G The table below uses P � SB  21 25  =  . 84<br>CHW SEA G NYMTEX GG TOR GG PHISTLLAA GG ARI G MIN G PIT G TBR G GG G MILCIN G WSN E ( R ) in remainder of game for( ) = 1 st inning and /  and gives  P ( R  >  0 )<br>4 G DET SFG G KCR G BAL G G SDP G for 9 th inning and corresponding thresholds for  P ( SB )<br>G<br>MIA<br>that increase the marginal measures:<br>Lineu Innin  1 Innin  9<br>p g g<br>3<br>Leadoff Current mean 4.659 P R >  0 no att  =  . 441<br>Markov Estimated Mean ( | )<br>Batting Order Chosen by wOBA<br>Comparison of Observed Mean vs. Markov Mean Marginal mean  4.637 P ( R >  0 | att ) =  . 491<br>2019 Mean if SB  4.761 P R >  0 SB  . 546<br>6 ( | ) =<br>NYY<br>MIN G G BOS G Mean if CS  3.987 P R >  0 CS  . 206<br>( | ) =<br>COL<br>GG<br>LAD<br>TEX G OAK G LAA G G ARI G ATL HOU G threshold P ( SB )  > . 87 P ( SB )  > . 69<br>5 G SFG G KCR G STLCIN G CHW GG CLE G TORTBR GG NYM G PIT G SEA G SDP G G PHIWSN G CHC G MIL G Cleanup Marginal MeanCurrent mean 4.82  4.834 P ( R >P ( R >  0 | no att 0 | att )) = =  . . 358432<br>4 BAL Mean if SB  4.945 P ( R >  0 |SB ) =  . 484<br>DET G G MIA Mean if CS  4.255 P R >  0 CS  . 156<br>( | ) =<br>threshold P SB  > . 82 P SB  > . 617<br>( ) ( )<br>3<br>Markov Estimated Mean<br>. 42). Batting Order Chosen by wOBA Conclusions: despite Acuna’s high success rate, this<br>).<br>3 4 5 6<br>3 4 5 6<br>Observed Runs Per Game<br>Observed Runs Per Game<br><!-- End of picture text -->

Some important decisions in baseball: 

(a) batting order 

- (b) whether to attempt to steal a base 

- (c) whether to sacrifice a runner. 

Good answers to (b) & (c) depend on answer to (a) 

A SHINY a Markov model and allows app implements users to select teams from 2014-2019 and order lineups and specify game situations to obtain estimates of **P** ( **R** = **r** ) for _r_ = 0 _,_ 1 _,_ 2 _, . . . ,_ 20. These distributions, includmeans and _P R >_ can be across out- ing ( 0) compared comes to assist in decision-making. 

## Methodology 

A _Markov Chain_ model for one half-inning of a baseball has 24 _transient states_ or combos of baserunners game , and outs (Diagram from (Sokol, 2004)): 



- 2019 Marlins opening day lineup was terrible ( _E_<sup>�</sup> ( _R_ ) = 2 _._ 42). 

Conclusions: despite Acuna’s high success rate, this analysis does not support running when reaching first base as the leadoff batter in the but it does game, support running if he bats cleanup. There is also an app to consider sacrificing. 

- So far in 2019, **RS** = **3** _._ **57** _,_ **RA** = **4** _._ **57** . Rearranging according to wOBA (Tango et al., 2006) = 

- leads to .09 more runs or 162 _× ._ 09 **14** _._ **6** more runs from per game, per season, or, 

- Pythagorean calculus, 2 more season wins. Lineup from July 24 even better ( **E**<sup>�</sup> ( **R** ) = **3** _._ **131** ). 



### **References** 



As game progress, it _transitions_ between states. 3,1 For example, suppose a runner’s on 3<sup>_rd_</sup> with 1 out . A 

Bukiet, B., Harold, E. R. and Palacios, J. L. (1997), ‘A markov chain approach to baseball’, _Operations Research_ **45** , 14–23. 

13,1 BB transitions to a HR to 0,1 scores 2 game , (and runs) and so on. **P** ( **R** = **r** ) governed by _Transition Probability Matrix_ estimated by substitution of empirical frequencies from MLB data selected by user. This SHINY app an et that en- implements algorithm by (Bukiet al., 1997) ables user to consider full nine-inning games. 

Sokol, J. S. (2004), ‘An intuitive markov chain lesson from baseball’, _INFORMS Transactions on Education_ **5** , 47–55. 

Tango, T., Lichtman, M. and Dolphin, A. E. (2006), _The Book: Playing the Percentages in Baseball_ , TMA Press. 


