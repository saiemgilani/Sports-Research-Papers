<!-- source: 2016 Stochastic Process Model Basketball.pdf -->

# A Multiresolution Stochastic Process Model for Predicting Basketball Possession Outcomes 

Daniel Cervone<sup>1</sup> , Alex D’Amour<sup>2</sup> , Luke Bornn<sup>3</sup> , and Kirk Goldsberry<sup>4</sup> 

> 1Center for Data Science, New York University, New York, NY 10003 

> 2Department of Statistics, Harvard University, Cambridge, MA 02138 

> 3Department of Statistics and Actuarial Science, Simon Fraser University, Burnaby, BC, Canada 

> 4Institute for Quantitative Social Science, Harvard University, Cambridge, MA 02138 

## **Author’s Footnote:** 

Daniel Cervone (email: `dcervone@nyu.edu` ) is Moore-Sloan Data Science Fellow at New York University. Alex D’Amour ( `damour@fas.harvard.edu` ) is PhD candidate, Statistics Department, Harvard University. Luke Bornn ( `lbornn@sfu.ca` ) is Assistant Professor, Department of Statistics and Actuarial Science, Simon Fraser University. Kirk Goldsberry ( `kgoldsberry@fas.harvard.edu` ) is Visiting Scholar, Center for Geographic Analysis, Harvard University. Daniel Cervone is funded by a fellowship from the Alfred P. Sloan and Betty Moore foundations. Luke Bornn is funded by DARPA Award FA8750-14-2-0117, ARO Award W911NF-15-1-0172, an Amazon AWS Research Grant, and the Natural Sciences and Engineering Research Council of Canada. 

The authors would like to thank Alex Franks, Andrew Miller, Carl Morris, Natesh Pillai, and Edoardo Airoldi for helpful comments, as well as STATS LLC in partnership with the NBA for providing the optical tracking data. The computations in this paper were run on the Odyssey cluster supported by the FAS Division of Science, Research Computing Group at Harvard University. 

## **Abstract** 

Basketball games evolve continuously in space and time as players constantly interact with their teammates, the opposing team, and the ball. However, current analyses of basketball outcomes rely on discretized summaries of the game that reduce such interactions to tallies of points, assists, and similar events. In this paper, we propose a framework for using optical player tracking data to estimate, in real time, the expected number of points obtained by the end of a possession. This quantity, called _expected possession value_ (EPV), derives from a stochastic process model for the evolution of a basketball possession. We model this process at multiple levels of resolution, differentiating between continuous, infinitesimal movements of players, and discrete events such as shot attempts and turnovers. Transition kernels are estimated using hierarchical spatiotemporal models that share information across players while remaining computationally tractable on very large data sets. In addition to estimating EPV, these models reveal novel insights on players’ decision-making tendencies as a function of their spatial strategy. A data sample and R code for further exploration of our model/results are available in the repository `https://github.com/dcervone/EPVDemo` . 

Keywords: Optical tracking data, spatiotemporal model, competing risks, Gaussian process. 

## 1. INTRODUCTION 

Basketball is a fast-paced sport, free-flowing in both space and time, in which players’ actions and decisions continuously impact their teams’ prospective game outcomes. Team owners, general managers, coaches, and fans all seek to quantify and evaluate players’ contributions to their team’s success. However, current statistical models for player evaluation such as “Player Efficiency Rating” (Hollinger 2005) and “Adjusted Plus/Minus” (Omidiran 2011) rely on highly reductive summary statistics of basketball games such as points scored, rebounds, steals, assists—the so-called “box score” summary of the game. Such models reflect the fact that up until very recently, data on basketball games were only available in this low level of resolution. Thus previous statistical analyses of basketball performance have overlooked many of the high-resolution motifs—events not measurable by such aggregate statistics— that characterize basketball strategy. For instance, traditional analyses cannot estimate the value of a clever move that fools the defender, or the regret of skipping an open shot in favor of passing to a heavily defended teammate. The advent of player tracking data in the NBA has provided an opportunity to fill this gap. 

## 1.1 Player-Tracking Data 

In 2013 the National Basketball Association (NBA), in partnership with data provider STATS LLC, installed optical tracking systems in the arenas of all 30 teams in the league. The systems track the exact two-dimensional locations of every player on the court (as well as the three-dimensional location of the ball) at a resolution of 25Hz, yielding over 1 billion space-time observations over the course of a full season. 

Consider, for example, the following possession recorded using this player tracking system. This is a specific Miami Heat possession against the Brooklyn Nets from the second quarter of a game on November 1, 2013, chosen arbitrarily among those during which LeBron James (widely considered the best NBA player as of 2014) handles the ball. In this particular 

1 



<!-- Start of picture text -->
2 2 3 3 4 A 4 2 2 3 3 4 4 B 22 151 3 34 4 C 22 5 11 3 43 4 D 12 Norris ColeRay AllenOFFENSE<br>1 3 Rashard Lewis<br>5 5 15 5 4 LeBron James<br>1 5 5<br>1 5 Chris Bosh<br>22 1 1 3 3 E 22 113 3 F 22 1 1 3 G 22 1 1 3 H 1 Deron WilliamsDEFENSE<br>5 4 4 4 4 44 3 4 4 3 23 Jason TerryJoe Johnson<br>5 5 5<br>5 4 Andray Blatche<br>5 5 5<br>5 Brook Lopez<br><!-- End of picture text -->

_Figure 1: Miami Heat possession against Brooklyn Nets. Norris Cole wanders into the perimeter (A) before driving toward the basket (B). Instead of taking the shot, he runs underneath the basket (C) and eventually passes to Rashard Lewis(D), who promptly passes to LeBron James (E). After entering the perimeter (F), James slips behind the defense (G) and scores an easy layup (H)._ 

possession, diagrammed in Figure 1, point guard Norris Cole begins with possession of the ball crossing the halfcourt line (panel A). After waiting for his teammates to arrive in the offensive half of the court, Cole wanders gradually into the perimeter (inside the three point line), before attacking the basket through the left post. He draws two defenders, and while he appears to beat them to the basket (B), instead of attempting a layup he runs underneath the basket through to the right post (C). He is still being double teamed and at this point passes to Rashard Lewis (D), who is standing in the right wing three position. As defender Joe Johnson closes, Lewis passes to LeBron James, who is standing about 6 feet beyond the three point line and drawing the attention of Andray Blatche (E). James wanders slowly into the perimeter (F), until just behind the free throw line, at which point he breaks towards the basket. His rapid acceleration (G) splits the defense and gains him a clear lane to the basket. He successfully finishes with a layup (H), providing the Heat two points. 

## 1.2 Expected Possession Value 

Such detailed data hold both limitless analytical potential for basketball spectators and new methodological challenges to statisticians. Of the dizzying array of questions that could be asked of such data, we choose to focus this paper on one particularly compelling quantity of interest, which we call _expected possession value_ (EPV), defined as the expected number of points the offense will score on a particular possession conditional on that possession’s evolution up to time _t_ . 

For illustration, we plot the EPV curve corresponding to the example Heat possession in Figure 2, with EPV estimated using the methodology in this paper. We see several moments when the expected point yield of the possession, given its history, changes dramatically. For the first 2 seconds of the possession, EPV remains around 1. When Cole drives toward the basket, EPV rises until peaking at around 1.34 when Cole is right in front of the basket. As Cole dribbles past the basket (and his defenders continue pursuit), however, EPV falls rapidly, bottoming out at 0.77 before “resetting” to 1.00 with the pass to Rashard Lewis. 

2 

The EPV increases slightly to 1.03 when the ball is then passed to James. As EPV is sensitive to small changes in players’ exact locations, we see EPV rise slightly as James approaches the three point line and then dip slightly as he crosses it. Shortly afterwards, EPV rises suddenly as James breaks towards the basket, eluding the defense, and continues rising until he is beneath the basket, when an attempted layup boosts the EPV from 1.52 to 1.62. 



<!-- Start of picture text -->
RASHARD<br>James<br>NORRIS COLE POSSESSION LEWIS LEBRON JAMES POSSESSION shot<br>POSS.<br>Splits the defense;<br>clear path to<br>basket<br>Accelerates<br>towards basket<br>Accelerates<br>into the<br>Pass paint<br>Runs behind Pass<br>basket and<br>Slight dip in EPV after defenders close Slight dip in EPV aftercrossing 3 point line<br>crossing 3 point line EPV constant while<br>pass is en route<br>0  1.2  2.4  3.6  4.8  6.0  7.2<br>time (sec)<br>1.6<br>1.4<br>EPV 1.2<br>1.0 {<br>{<br>0.8<br><!-- End of picture text -->

_Figure 2: Estimated EPV over time for the possession shown in Figure 1. Changes in EPV are induced by changes in players’ locations and dynamics of motion; macrotransitions such as passes and shot attempts produce immediate, sometimes rapid changes in EPV. The black line slightly smooths EPV evaluations at each time point (gray dots), which are subject to Monte Carlo error._ 

In this way, EPV corresponds naturally to a coach’s or spectator’s sense of how the actions that basketball players take in continuous time help or hurt their team’s cause to score in the current possession, and quantifies this in units of expected points. EPV acts like a stock ticker, providing an instantaneous summary of the possession’s eventual point value given all available information, much like a stock price values an asset based on speculation of future expectations. 

## 1.3 Related Work and Contributions 

Concepts similar to EPV, where final outcomes are modeled conditional on observed progress, have had statistical treatment in other sports, such as in-game win probability in baseball (Bukiet, Harold & Palacios 1997; Yang & Swartz 2004) and football (Lock & Nettleton 2014), as well as in-possession point totals in football (Burke 2010; Goldner 2012). These previous efforts can be categorized into either marginal regression/classification approaches, where features of the current game state are mapped directly to expected outcomes, or processbased models that use a homogeneous Markov chain representation of the game to derive outcome distributions. Neither of these approaches is ideal for application to basketball. Marginal regression methodologies ignore the natural martingale structure of EPV, which is essential to its “stock ticker” interpretation. On the other hand, while Markov chain methodologies do maintain this “stock ticker” structure, applying them to basketball requires discretizing the data, introducing an onerous bias-variance-computation tradeoff that is not present for sports like baseball that are naturally discrete in time. 

3 

To estimate EPV effectively, we introduce a novel multiresolution approach in which we model basketball possessions at two separate levels of resolution, one fully continuous and one highly coarsened. By coherently combining these models we are able to obtain EPV estimates that are reliable, sensitive, stochastically consistent, and computationally feasible (albeit intensive). While our methodology is motivated by basketball, we believe that this research can serve as an informative case study for analysts working in other application areas where continuous monitoring data are becoming widespread, including traffic monitoring (Ihler, Hutchins & Smyth 2006), surveillance, and digital marketing (Shao & Li 2011), as well as other sports such as soccer and hockey (Thomas, Ventura, Jensen & Ma 2013). 

Section 2 formally defines EPV within the context of a stochastic process for basketball, introducing the multiresolution modeling approach that make EPV calculations tractable as averages over future paths of a stochastic process. Parameters for these models, which represent players’ decision-making tendencies in various spatial and situational circumstances, are discussed in Section 3. Section 4 discusses inference for these parameters using hierchical models that share information between players and across space. We highlight results from actual NBA possessions in Section 5, and show how EPV provides useful new quantifications of player ability and skill. Section 6 concludes with directions for further work. 

## 2. MULTIRESOLUTION MODELING 

To present our process model for a basketball possession, we require some formalism. Let Ω represent the space of all possible basketball possessions in full detail, with _ω ∈_ Ωdescribing the full path of a particular possession. For simplicity, we restrict our focus to possessions that do not include fouls<sup>1</sup> , so that each possession we consider results in 0, 2, or 3 points scored for the offense, denoted _X_ ( _ω_ ) _∈{_ 0 _,_ 2 _,_ 3 _}_ . For any possession path _ω_ , we denote by _Z_ ( _ω_ ) the optical tracking time series generated by this possession so that _Zt_ ( _ω_ ) _∈Z_ , _t >_ 0, is a “snapshot” of the tracking data exactly _t_ seconds from the start of the possession ( _t_ = 0). _Z_ is a high dimensional space that includes ( _x, y_ ) coordinates for all 10 players on the court, ( _x, y, z_ ) coordinates for the ball, summary information such as which players are on the court and what the game situation is (game location, score, time remaining, etc.), and event annotations that are observable in real time, such as a turnover occurring, a pass, or a shot being attempted and the result of that attempt. 

Taking the intuitive view of Ωas a sample space of possession paths, we model _Z_ ( _ω_ ) as a stochastic process, and likewise, define _Zt_ ( _ω_ ) for each _t >_ 0 as a random variable in _Z_ . _Z_ ( _ω_ ) provides the natural filtration _Ft_<sup>(</sup><sup>_Z_)</sup> = _σ_ ( _{Zs_<sup>_−_1</sup> : 0 _≤ s ≤ t}_ ), which represents all information available from the optical tracking data for the first _t_ seconds of a possession. EPV is the expected value of the number of points scored for the possession ( _X_ ) given all available data up to time _t_ ( _Ft_<sup>(</sup><sup>_Z_)</sup> ): 

**Definition** The _expected possession value_ , or EPV, at time _t ≥_ 0 during a possession is _νt_ = E[ _X|Ft_<sup>(</sup><sup>_Z_)</sup> ]. 

> 1Our data include foul events, but do not specify the type or circumstances of the foul. There are several types of fouls and game situations for which fouls lead to free throws—for instance, shooting fouls, technical/flagrant fouls, clear path fouls, and fouls during the fouling team’s “bonus” period; thus, modeling fouls presents additional complications relative to the other events we model in our EPV model. While drawing fouls can be a valuable and important part of team strategy, we omit modeling such behavior in this paper. 

4 

The expectation E[ _X|Ft_<sup>(</sup><sup>_Z_)</sup> ] is an integral over the distribution of future paths the current possession can take. Letting _T_ ( _ω_ ) denote the time at which a possession following path _ω_ ends<sup>2</sup> , the possession’s point total is a deterministic function of the full resolution data at this time, _X_ ( _ω_ ) = _h_ ( _ZT_ ( _ω_ )( _ω_ )). Thus, evaluating EPV amounts to integrating over the joint distribution of ( _T, ZT_ ): 



Note that we use probability notation P( _·_ ) somewhat heuristically, as P( _T_ = _s|Ft_<sup>(</sup><sup>_Z_)</sup> ) is a density with respect to Lebesgue measure, while _Zs_ mixes both discrete (annotations) and continuous (locations) components. We will also generally omit the dependence on _ω_ when writing random variables, e.g., _Zt_ instead of _Zt_ ( _ω_ ). 

## 2.1 Estimator Criteria 

We have defined EPV in (1) as an unobserved, theoretical quantity; one could thus imagine many different EPV estimators based on different models and/or information in the data. However, we believe that in order for EPV to achieve its full potential as a basis for highresolution player and strategy evaluation, an EPV estimator should meet several criteria. 

First, we require that the EPV estimator be stochastically consistent. Recognizing that EPV is simply a conditional expectation, it is tempting to estimate EPV using a regression or classification approach that maps features from _Ft_<sup>(</sup><sup>_Z_)</sup> to an outcome space, [0 _,_ 3] or _{_ 0 _,_ 2 _,_ 3 _}_ . Setting aside the fact that our data associate each possession outcome _X_ with process-valued inputs _Z_ , and thus do not conform naturally to input/output structure of such models, such an approach cannot guarantee the estimator will have the (Kolmogorov) stochastic consistency inherent to theoretical EPV, which is essential to its “stock ticker” interpretation. Using a stochastically consistent EPV estimator guarantees that changes in the resulting EPV curve derive from players’ on-court actions, rather than artifacts or inefficiencies of the data analysis. A stochastic process model for the evolution of a basketball possession guarantees such consistency. 

The second criterion that we require is that the estimator be sensitive to the fine-grained details of the data without incurring undue variance or computatonal complexity. Applying a Markov chain-based estimation approach would require discretizing the data by mapping the observed spatial configuration _Zt_ into a simplified summary _Ct_ , violating this criterion by trading potentially useful information in the player tracking data for computational tractability. 

To develop methodology that meet both criteria, we note the information-computation tradeoff in current process modeling strategies results from choosing a single level of resolution at which to model the possession and compute all expectations. In contrast, our method for estimating EPV combines models for the possession at two distinct levels of resolution, namely, a fully continuous model of player movement and actions, and a Markov chain model for a highly coarsened view of the possession. This multiresolution approach 

> 2The time of a possession is bounded, even for pathological examples, by the 12-minute length of a quarter; yet we do not leverage this fact and simply assume that possession lenghts are almost surely finite. 

5 

leverages the computational simplicity of a discrete Markov chain model while conditioning on exact spatial locations and high-resolution data features. 

2.2 A Coarsened Process The Markov chain portion of our method requires a coarsened view of the data. For all time 0 _< t ≤ T_ during a possession, let _C_ ( _·_ ) be a coarsening that maps _Z_ to a finite set _C_ , and call _Ct_ = _C_ ( _Zt_ ) the “state” of the possession. To make the Markovian assumption plausible, we populate the coarsened state space _C_ with summaries of the full resolution data so that transitions between these states represent meaningful events in a basketball possession—see Figure 3 for an illustration. 



<!-- Start of picture text -->
Player 1 Player 2 Player 3 Player 4 Player 5<br>C<br>poss<br>C trans Turnover Shot Rebound<br>C end Made 2pt Made 3pt End of possession<br>P2 P3 P4 P5<br>to to to to<br>Pass Pass Pass Pass<br><!-- End of picture text -->

_Figure 3: Schematic of the coarsened possession process C, with states (rectangles) and possible state transitions (arrows) shown. The unshaded states in the first row compose Cposs. Here, states corresponding to distinct ballhandlers are grouped together (Player 1 through 5), and the discretized court in each group represents the player’s coarsened position and defended state. The gray shaded rectangles are transition states, Ctrans, while the rectangles in the third row represent the end states, Cend. Blue arrows represent possible macrotransition entrances (and red arrows, macrotransition exits) when Player 1 has the ball; these terms are introduced in Section 3._ 

First, there are 3 “bookkeeping” states, denoted _C_ end, that categorize the end of the possession, so that _CT ∈C_ end and for all _t < T, Ct ∈C_ end (shown in the bottom row of Figure 3). These are _C_ end = _{_ made 2 pt, made 3 pt, end of possession _}_ . These three states have associated point values of 2, 3, and 0, respectively (the generic possession end state can be reached by turnovers and defensive rebounds, which yield no points). This makes the possession point value _X_ a function of the final coarsened state _CT_ . 

Next, whenever a player possesses the ball at time _t_ , we assume _Ct_ = (ballcarrier ID at _t_ ) _×_ (court region at _t_ ) _×_ (defended at _t_ ), having defined seven disjoint regions of the court and classifying a player as defended at time _t_ by whether there is a defender within 5 feet of him. The possible values of _Ct_ , if a player possesses the ball at time _t_ , thus live in _C_ poss = _{_ player ID _} × {_ region ID _} × {_ **1** [defended] _}_ . These states are represented by the unshaded portion of the top row of Figure 3, where the differently colored regions of the court 

6 

diagrams reveal the court space discretization. 

Finally, we define a set of states to indicate that an annotated basketball action from the full resolution data _Z_ is currently in progress. These “transition” states encapsulate constrained motifs in a possession, for example, when the ball is in the air traveling between players in a pass attempt. Explicitly, denote _C_ trans = _{_ shot attempt from _c ∈C_ poss, pass to _c_<sup>_′_</sup> _∈C_ poss from _c ∈C_ poss, turnover in progress, rebound in progress _}_ (listed in the gray shaded portions of Figure 3). These transition states carry information about the possession path, such as the most recent ballcarrier, and the target of the pass, while the ball is in the air during shot attempts and passes<sup>3</sup> . Note that, by design, a possession must pass through a state in _C_ trans in order to reach a state in _C_ end. For simplicity and due to limitations of the data, this construction of _C_ = _C_ poss _∪C_ trans _∪C_ end excludes several notable basketball events (such as fouls, violations, and other stoppages in play) and aggregates others (the data, for example, does not discriminate among steals, intercepted passes, or lost balls out of bounds). 

## 2.3 Combining Resolutions 

We make several modeling assumptions about the processes _Z_ and _C_ , which allow them to be combined into a coherent EPV estimator. 

(A1) _C_ is marginally semi-Markov. 

The semi-Markov assumption (A1) guarantees that the embedded sequence of disjoint possession states _C_<sup>(0)</sup> _, C_<sup>(1)</sup> _, . . . , C_<sup>(</sup><sup>_K_)</sup> is a Markov chain, which ensures that it is straightforward to compute E[ _X|Ct_ ] using the associated transition probability matrix (Kemeny & Snell 1976). Next, we specify the relationship between coarsened and full-resolution conditioning. This first requires defining two additional time points which mark changes in the future evolution of the possession: 





Thus, assuming a player possesses the ball at time _t_ , _τt_ is the first time after _t_ he attempts a shot/pass or turns the ball over (entering a state in _C_ trans), and _δt_ is the endpoint of this shot/pass/turnover (leaving a state in _C_ trans). We assume that passing through these transition states, _C_ trans, _decouples_ the future of the possession after time _δt_ with its history up to time _t_ : 



Intuitively, assumption (A2) states that for predicting coarsened states beyond some point in the future _δt_ , all information in the possession history up to time _t_ is summarized by the distribution of _Cδt_ . The dynamics of basketball make this assumption reasonable; when a player passes the ball or attempts a shot, this represents a structural transition in the basketball possession to which all players react. Their actions prior to this transition are 

> 3The reason we index transition states by the origin of the pass/shot attempt (and destination of the pass) is to preserve this information under a Markov assumption, where generic “pass” or “shot” states would inappropriately allow future states to be independent of the players involved in the shot or pass. 

7 

not likely to influence their actions after this transition. Given _Cδt_ —which, for a pass at _τt_ includes the pass recipient, his court region, and defensive pressure, and for a shot attempt at _τt_ includes the shot outcome—data prior to the pass/shot attempt are not informative of the possession’s future evolution. 

Together, these assumptions yield a simplified expression for (1), which combines contributions from full-resolution and coarsened views of the process. 

**Theorem 2.1** _Under assumptions (A1)–(A2), the full-resolution EPV νt can be rewritten:_ 



**Remark** Although we have specified this result in terms of the specific coarsening defined in Section 2.2, we could substitute any coarsening for which (A1)–(A2) are well-defined and reasonably hold. We briefly discuss potential alternative coarsenings in Section 6. 

The proof of Theorem 2.1, follows immediately from (A1)–(A2), and is therefore omitted. Heuristically, (4) expresses _νt_ as the expectation given by a homogeneous Markov chain on _C_ with a random starting point _Cδt_ , where only the starting point depends on the fullresolution information _Ft_<sup>(</sup><sup>_Z_)</sup> . This result illustrates the multiresolution conditioning scheme that makes our EPV approach computationally feasible: the term E[ _X|Cδt_ = _c_ ] is easy to calculate using properties of Markov chains, and P( _Cδt|Ft_<sup>(</sup><sup>_Z_)</sup> ) only requires forecasting the full-resolution data for a short period of time relative to (1), as _δt ≤ T_ . 

## 3. TRANSITION MODEL SPECIFICATION 

The representation in Theorem (2.1) shows that estimating EPV does not require a full-blown model for entire basketball possessions at high resolution. Instead, the priority is to accurately predict the next major “decoupling” action in the possession, which we have denoted _Cδt_ . At this point, Equation (4) switches resolutions: _Cδt_ depends on the full-resolution possession history _Ft_<sup>(</sup><sup>_Z_)</sup> , after which our EPV estimate only depends on the coarsened state _Cδt_ . This section presents models that operate on these two distinct levels of resolution, using parameterizations that reflect players’ reactions to the situational, spatiotemporal predicaments they face on the basketball court. 

First, using the full-resolution data, we need to predict _Cδt_ . We achieve this using three models; heuristically speaking, one predicts player movement in space while the ballcarrier remains constant, one predicts the occurrence of events (passes/shots/turnovers) that change the ballcarrier, and one predicts the outcome state ( _Cδt_ ) of such events. 

Writing these models requires some additional notation. Fix _ϵ >_ 0, and for any _t ≥_ 0 during the possession (here, we use 1/25 second since this is the temporal resolution of our data), and let _M_ ( _t_ ) be the event _{τt ≤ t_ + _ϵ}_ ; for this, we say that a _macrotransition_ occurs during ( _t, t_ + _ϵ_ ]. Recalling the definition of _τt_ (2), _M_ ( _t_ ) is realized when the possession moves from _C_ poss to _C_ trans, which represents the start of a pass, shot attempt, or turnover (and _M_ ( _t_ ) is continuously realized throughout the duration of this action). We now define: 

- (M1) The _microtransition model_ , P( _Zt_ + _ϵ|M_ ( _t_ )<sup>_c_</sup> _, Ft_<sup>(</sup><sup>_Z_)</sup> ), which describes infinitesimal player movement assuming that a major ball movement does _not_ occur. 

8 

- (M2) The _macrotransition entry model_ , P( _M_ ( _t_ ) _|Ft_<sup>(</sup><sup>_Z_)</sup> ), which describes the occurrence of a macrotransition (pass/shot/turnover) within the next _ϵ_ time. 

- (M3) The _macrotransition exit model_ P( _Cδt|M_ ( _t_ ) _, Ft_<sup>(</sup><sup>_Z_)</sup> ), which gives the outcome of this macrotransition in _C_ . 

(M1)–(M3) together allow us to sample from P( _Cδt|Ft_<sup>(</sup><sup>_Z_)</sup> ), as we alternate draws from (M1) and (M2) until a macrotransition occurs, and then use (M3) to sample the outcome state of this macrotransition. Thus, while models (M1)–(M3) condition on the full-resolution possession history _Ft_<sup>(</sup><sup>_Z_)</sup> in order to predict _Cδt_ , calculating EPV given _Cδt_ only requires a model for transitions between coarsened states _C_ . Due to the Markov assumption (A1), this is easily summarized by a transition probability matrix: 

- (M4) The _Markov transition probability matrix_ **P** , with _Pqr_ = P( _C_<sup>(</sup><sup>_n_+1)</sup> = _cr|C_<sup>(</sup><sup>_n_)</sup> = _cq_ ). 

Thus, (M1)–(M4) are sufficient to compute EPV using our multiresolution framework of Theorem 2.1. In the following subsections, we discuss each of these models in greater detail. 

3.1 Microtransition Model 

The microtransition model describes player movement with the ballcarrier held constant. In the periods between transfers of ball possession (including passes, shots, and turnovers), all players on the court move in order to influence the character of the next ball movement (macrotransition). For instance, the ballcarrier might drive toward the basket to attempt a shot, or move laterally to gain separation from a defender, while his teammates move to position themselves for passes or rebounds, or to set screens and picks. The defense moves correspondingly, attempting to deter easy shot attempts or passes to certain players while simultaneously anticipating a possible turnover. Separate models are assumed for offensive and defensive players, as we shall describe. 

Predicting the motion of offensive players over a short time window is driven by the players’ dynamics (velocity, acceleration, etc.). Let the location of offensive player _ℓ_ ( _ℓ ∈ {_ 1 _, . . . , L_ = 461 _}_ ) at time _t_ be **z**<sup>_ℓ_</sup> ( _t_ ) = ( _x_<sup>_ℓ_</sup> ( _t_ ) _, y_<sup>_ℓ_</sup> ( _t_ )). We then model movement in each of the _x_ and _y_ coordinates using 



(and analogously for _y_<sup>_ℓ_</sup> ( _t_ )). This expression derives from a Taylor series expansion to the ballcarrier’s position for each coordinate, such that _αx_<sup>_ℓ_[</sup><sup>_xℓ_(</sup><sup>_t_)</sup><sup>_−xℓ_(</sup><sup>_t −ϵ_)]</sup><sup>_≈ϵxℓ′_(</sup><sup>_t_),and</sup><sup>_η_</sup> _x_<sup>_ℓ_(</sup><sup>_t_)</sup> provides stochastic innovations representing the contribution of higher-order derivatives (acceleration, jerk, etc.). Because they are driven to score, players’ dynamics on offense are nonstationary. When possessing the ball, most players accelerate toward the basket when beyond the three-point line, and decelerate when very close to the basket in order to attempt a shot. Also, players will accelerate away from the edges of the court as they approach these, in order to stay in bounds. To capture such behavior, we assume spatial structure for the innovations, _ηx_<sup>_ℓ_(</sup><sup>_t_)</sup><sup>_∼N_(</sup><sup>_µℓ_</sup> _x_<sup>(</sup><sup>**z**</sup><sup>_ℓ_(</sup><sup>_t_))</sup><sup>_,_(</sup><sup>_σ_</sup> _x_<sup>_ℓ_)2),where</sup><sup>_µℓ_</sup> _x_<sup>mapsplayer</sup><sup>_ℓ_’slocationonthecourtto</sup> an additive effect in (5), which has the interpretation of an acceleration effect; see Figure 4 for an example. 

The defensive components of P( _Zt_ + _ϵ|M_ ( _t_ )<sup>_c_</sup> _, Ft_<sup>(</sup><sup>_Z_)</sup> ), corresponding to the positions of the five defenders, are easier to model conditional on the evolution of the offense’s positions. 

9 



<!-- Start of picture text -->
TONY PARKER WITH BALL TONY PARKER WITHOUT BALL DWIGHT HOWARD WITH BALL DWIGHT HOWARD WITHOUT BALL<br>(a) (b) (c) (d)<br><!-- End of picture text -->

_Figure 4: Acceleration fields_ ( _µx_ ( **z** ( _t_ )) _, µy_ ( **z** ( _t_ ))) _for Tony Paker (a)–(b) and Dwight Howard (c)–(d) with and without ball possession. The arrows point in the direction of the acceleration at each point on the court’s surface, and the size and color of the arrows are proportional to the magnitude of the acceleration. Comparing (a) and (c) for instance, we see that when both players possess the ball, Parker more frequently attacks the basket from outside the perimeter. Howard does not accelerate to the basket from beyond the perimeter, and only tends to attack the basket inside the paint._ 

Following Franks, Miller, Bornn & Goldsberry (2015), we assume each defender’s position is centered on a linear combination of the basket’s location, the ball’s location, and the location of the offensive player he is guarding. Franks et al. (2015) use a hidden Markov model (HMM) based on this assumption to learn which offensive players each defender is guarding, such that conditional on defender _ℓ_ guarding offender _k_ his location **z**<sup>_ℓ_</sup> ( _t_ ) = ( _x_<sup>_ℓ_</sup> ( _t_ ) _, y_<sup>_ℓ_</sup> ( _t_ )) should be normally distributed with mean **m**<sup>_k_</sup> opt<sup>(</sup><sup>_t_) = 0</sup><sup>_._62</sup><sup>**z**</sup><sup>_k_(</sup><sup>_t_) + 0</sup><sup>_._11</sup><sup>**z**bask+ 0</sup><sup>_._27</sup><sup>**z**ball(</sup><sup>_t_).</sup> 

Of course, the dynamics (velocity, etc.) of defensive players’ are still hugely informative for predicting their locations within a small time window. Thus our microtransition model for defender _ℓ_ balances these dynamics with the mean path induced by the player he is guarding: 



and symmetrically in _y_ . Rather than implement the HMM procedure used in Franks et al. (2015), we simply assume each defender is guarding at time _t_ whichever offensive player _j_ yields the smallest residual _||_ **z**<sup>_ℓ_</sup> ( _t_ ) _−_ **m**<sup>_j_</sup> opt<sup>(</sup><sup>_t_)</sup><sup>_||_,notingthatmorethanonedefendermaybe</sup> guarding the same offender (as in a “double team”). Thus, conditional on the locations of the offense at time _t_ + _ϵ_ , (6) provides a distribution over the locations of the defense at _t_ + _ϵ_ . 

## 3.2 Macrotransition Entry Model 

The macrotransition entry model P( _M_ ( _t_ ) _|Ft_<sup>(</sup><sup>_Z_)</sup> ) predicts ball movements that instantaneously shift the course of the possession—passes, shot attempts, and turnovers. As such, we consider a family of macrotransition entry models P( _Mj_ ( _t_ ) _|Ft_<sup>(</sup><sup>_Z_)</sup> ), where _j_ indexes the type of macrotransition corresponding to _M_ ( _t_ ). There are six such types: four pass options (indexed, without loss of generality, _j ≤_ 4), a shot attempt ( _j_ = 5), or a turnover ( _j_ = 6). Thus, _Mj_ ( _t_ ) is the event that a macrotransition of type _j_ begins in the time window 

10 

( _t, t_ + _ϵ_ ], and _M_ ( _t_ ) =<sup>�6</sup> _j_ =1<sup>_Mj_(</sup><sup>_t_).Sincemacrotransitiontypesaredisjoint,wealsoknow</sup> P( _M_ ( _t_ ) _|Ft_<sup>(</sup><sup>_Z_)</sup> ) =<sup>�6</sup> _j_ =1<sup>P(</sup><sup>_Mj_(</sup><sup>_t_)</sup><sup>_|F_</sup> _t_<sup>(</sup><sup>_Z_)</sup> ). 

We parameterize the macrotransition entry models as competing risks (Prentice, Kalbfleisch, Peterson Jr, Flournoy, Farewell & Breslow 1978): assuming player _ℓ_ possesses the ball at time _t >_ 0 during a possession, denote 



as the hazard for macrotransition _j_ at time _t_ . We assume these are log-linear, 



where **W** _j_<sup>_ℓ_(</sup><sup>_t_)isa</sup><sup>_pj×_1vectoroftime-varyingcovariates,</sup><sup>**_β_**</sup><sup>_ℓ_</sup> _j_<sup>a</sup><sup>_pj×_1vectorofcoefficients,</sup> **z**<sup>_ℓ_</sup> ( _t_ ) is the ballcarrier’s 2D location on the court (denote the court space S) at time _t_ , and _ξj_<sup>_ℓ_: S</sup><sup>_→_R is a mapping of the player’s court location to an additive effect on the log-hazard,</sup> providing spatial variation. The last term in (8) only appears for pass events ( _j ≤_ 4) to incorporate the location of the receiving player for the corresponding pass: **z** _j_ ( _t_ ) (which slightly abuses notation) provides his location on the court at time _t_ , and _ξ_<sup>˜</sup> _j_<sup>_ℓ_,analogously</sup> to _ξj_<sup>_ℓ_,mapsthislocationtoanadditiveeffectonthelog-hazard.Thefourdifferentpassing</sup> options are identified by the (basketball) position of the potential pass recipient: point guard (PG), shooting guard (SG), small forward (SF), power forward (PF), and center (C). 

The macrotransition model (7)–(8) represents the ballcarrier’s decision-making process as an interpretable function of the unique basketball predicaments he faces. For example, in considering the hazard of a shot attempt, the time-varying covariates ( **W** _j_<sup>_ℓ_(</sup><sup>_t_))weuse</sup> are the distance between the ballcarrier and his nearest defender (transformed as log(1 + _d_ ) to moderate the influence of extremely large or small observed distances), an indicator for whether the ballcarrier has dribbled since gaining possession, and a constant representing a baseline shooting rate (this is not time-varying)<sup>4</sup> . The spatial effects _ξj_<sup>_ℓ_reveallocations</sup> where player _ℓ_ is more/less likely to attempt a shot in a small time window, holding fixed the time-varying covariates **W** _j_<sup>_ℓ_(</sup><sup>_t_).Suchspatialeffects(illustratedinFigure5)arewell-known</sup> to be nonlinear in distance from the basket and asymmetric about the angle to the basket (Miller, Bornn, Adams & Goldsberry 2013). 

All model components—the time-varying covariates, their coefficients, and the spatial effects _ξ, ξ_<sup>˜</sup> differ across macrotransition types _j_ for the same ballcarrier _ℓ_ , as well as across all _L_ = 461 ballcarriers in the league during the 2013-14 season. This reflects the fact that players’ decision-making tendencies and skills are unique; a player such as Dwight Howard will very rarely attempt a three point shot even if he is completely undefended, while someone like Stephen Curry will attempt a three point shot even when closely defended. 

> 4Full details on all covariates used for all macrotransition types are included in Appendix A.1 

11 













_Figure 5: Plots of estimated spatial effects ξ for LeBron James as the ballcarrier. For instance, plot (c) reveals the largest effect on James’ shot-taking hazard occurs near the basket, with noticeable positive effects also around the three point line (particularly in the “corner 3” shot areas). Plot (a) shows that he is more likely (per unit time) to pass to the point guard when at the top of the arc—more so when the point guard is positioned in the post area._ 

## 3.3 Macrotransition Exit Model 

Using the six macrotransition types introduced in the previous subsection, we can express the macrotransition exit model (M3) when player _ℓ_ has possession as 



using the competing risks model for _Mj_ ( _t_ ) given by (7)–(8). As terms _λ_<sup>_ℓ_</sup> _j_<sup>(</sup><sup>_t_)aresuppliedby</sup> (8), we focus on the macrotransition exit model conditional on the macrotransition type, P( _Cδt|Mj_ ( _t_ ) _, Ft_<sup>(</sup><sup>_Z_)</sup> ). 

For each _j_ = 1 _, . . . ,_ 4, _Mj_ ( _t_ ) represents a pass-type macrotransition, therefore _Cδt_ is a possession state _c_<sup>_′_</sup> _∈C_ poss for the player corresponding to pass option _j_ . Thus, a model for P( _Cδt|Mj_ ( _t_ ) _, Ft_<sup>(</sup><sup>_Z_)</sup> ) requires us to predict the state _c_<sup>_′_</sup> _∈C_ poss the _j_ th pass target will occupy upon receiving the ball. Our approach is to simply assume _c_<sup>_′_</sup> is given by the pass target’s location at the time the pass begins. While this is naive and could be improved by further modeling, it is a reasonable approximation in practice, because with only seven court regions and two defensive spacings comprising _C_ poss, the pass recipient’s position in this space is unlikely to change during the time the pass is traveling en route, _δt − t_ (a noteable exception is the alley-oop pass, which leads the pass recipient from well outside the basket to a dunk or layup within the restricted area). Our approach thus collapses P( _Cδt|Mj_ ( _t_ ) _, Ft_<sup>(</sup><sup>_Z_)</sup> ) to a single state in _C_ poss, which corresponds to pass target _j_ ’s location at time _t_ . 

When _j_ = 5, and a shot attempt occurs in ( _t, t_ + _ϵ_ ], _Cδt_ is either a made/missed 2 point shot, or made/missed three point shot. For sufficiently small _ϵ_ , we observe at _Zt_ whether the shot attempt in ( _t, t_ + _ϵ_ ] is a two- or three-point shot, therefore our task in providing 

12 

P( _Cδt|Mj_ ( _t_ ) _, Ft_<sup>(</sup><sup>_Z_)</sup> ) is modeling the shot’s probability of success. We provide a parametric shot probability model, which shares the same form as the macrotransition entry model (7)– (8), though we use a logit link function as we are modeling a probability instead of a hazard. Specifically, for player _ℓ_ attempting a shot at time _t_ , let _p_<sup>_ℓ_</sup> ( _t_ ) represent the probability of the shot attempt being successful (resulting in a basket). We assume 



with components in (10) having the same interpretation as their _j_ -indexed counterparts in the competing risks model (8); that is, **W** s<sup>_ℓ_isavectoroftime-varyingcovariates(we</sup> use distance to the nearest defender—transformed as log(1 + _d_ )—an indicator for whether the player has dribbled, and a constant to capture baseline shooting efficiency) with **_β_**<sup>_ℓ_</sup> s<sup>a</sup> corresponding vector of coefficients, and _ξ_ s<sup>_ℓ_asmoothspatialeffect,asin(8).</sup> 

Lastly, when _j_ = 6 and _Mj_ ( _t_ ) represents a turnover, _Cδt_ is equal to the turnover state in _C_ end with probability 1. 

Note that the macrotransition exit model is mostly trivial when no player has ball possession at time _t_ , since this implies _Ct ∈C_ trans _∪C_ end and _τt_ = _t_ . If _Ct ∈C_ end, then the possession is over and _Cδt_ = _Ct_ . Otherwise, if _Ct ∈C_ trans represents a pass attempt or turnover in progress, the following state _Cδt_ is deterministic given _Ct_ (recall that the pass recipient and his location are encoded in the definition of pass attempt states in _C_ trans). When _Ct_ represents a shot attempt in progress, the macrotransition exit model reduces to the shot probability model (10). Finally, when _Ct_ is a rebound in progress, we ignore full-resolution information and simply use the Markov transition probabilities from **P**<sup>5</sup> . 

## 3.4 Transition Probability Matrix for Coarsened Process 

The last model necessary for calculating EPV is (M4), the transition probability matrix for the embedded Markov chain corresponding to the coarsened process _C_<sup>(0)</sup> _, C_<sup>(2)</sup> _, . . . , C_<sup>(</sup><sup>_K_)</sup> . This transition probability matrix is used to compute the term E[ _X|Cδt_ = _c_ ] that appears in Theorem 2.1. Recall that we denote the transition probability matrix as **P** , where _Pqr_ = P( _C_<sup>(</sup><sup>_i_+1)</sup> = _cr|C_<sup>(</sup><sup>_i_)</sup> = _cq_ ) for any _cq, cr ∈C_ . 

Without any other probabilistic structure assumed for _C_<sup>(</sup><sup>_i_)</sup> other than Markov, for all _q, r_ , the maximum likelihood estimator of _Pqr_ is the observed transition frequency, _P_<sup>ˆ</sup> _qr_ = <u>�</u> _rN_<sup>_′_</sup> _<u>q</u>_<sup>_N_</sup> _rqr_<sup>_′_,</sup> where _Nqr_ counts the number of transitions _cq → cr_ . Of course, this estimator has undesirable performance if the number of visits to any particular state _cq_ is small (for instance, Dwight Howard closely defended in the corner 3 region), as the estimated transition probabilities from that state may be degenerate. 

Under our multiresolution model for basketball possessions, however, expected transition counts between many coarsened states _C_<sup>(</sup><sup>_i_)</sup> can be computed as summaries of our macrotransition models (M2)–(M3). To show this, for any arbitrary _t >_ 0 let _Mj_<sup>_r_(</sup><sup>_t_)betheevent</sup> 



Thus _Mj_<sup>_r_(</sup><sup>_t_)occursifitispossibleforamacrotransitionoftype</sup><sup>_j_intostate</sup><sup>_cr_tooccurin</sup> 

5Our rebounding model could be improved by using full-resolution spatiotemporal information, as players’ reactions to the missed shot event are informative of who obtains the rebound. 

13 

( _t, t_ + _ϵ_ ]. When applicable, we can use this to get the expected number of _cq → cr_ transitions: 



When _cq_ is a shot attempt state from˜ _cq′ ∈C_ poss, (11) is adjusted using the shot probability model (10): _Nqr_ = _ϵ_<sup>�</sup> _t_ : _Ct_ = _cq′_<sup>_λℓ_</sup> _j_<sup>(</sup><sup>_t_)</sup><sup>_p_(</sup><sup>_t_)</sup><sup>**1**[</sup><sup>_M r_</sup> _j_<sup>(</sup><sup>_t_)]when</sup><sup>_cr_representsaneventualmadeshot</sup> and _N_<sup>˜</sup> _qr_ = _ϵ_<sup>�</sup> _t_ : _Ct_ = _cq′_<sup>_λℓ_</sup> _j_<sup>(</sup><sup>_t_)(1</sup><sup>_−p_(</sup><sup>_t_))</sup><sup>**1**[</sup><sup>_M r_</sup> _j_<sup>(</sup><sup>_t_)]when</sup><sup>_cr_representsaneventualmiss.</sup> By replacing raw counts with their expectations conditional on higher-resolution data, leveraging the hazards (11) provides a Rao-Blackwellized (unbiased, lower variance) alternative to counting observed transitions. Furthermore, due to the hierarchical parameterization of hazards _λ_<sup>_ℓ_information is shared across space and player com-</sup> _j_<sup>(</sup><sup>_t_) (discussed in Section 4),</sup> binations so that estimated hazards are well-behaved even in situations without significant observed data. Thus, when _cq → cr_ represents a macrotransition, we use _N_<sup>˜</sup> _qr_ in place of _Nqr_ when calculating _P_<sup>ˆ</sup> _qr_ . 

## 4. HIERARCHICAL MODELING AND INFERENCE 

A critical aspect of the micro- and macrotransition models defined in the previous section is that they are parameterized to capture the variations between actions, players, and court space that play a central role in basketball strategy. This section outlines the procedure for reliably estimating this rich set of model parameters using likelihood-based methods. 

Hierarchical models are essential for our problem because by implicitly averaging over all possible future possession paths, calculating EPV requires transition probabilities for situations for which there is no data. For instance, DeAndre Jordan did not attempt a three-point shot in the 2013-14 season, yet any EPV estimate for a possession with him on the court requires an estimate of his shooting ability from everywhere on the court, even though for some of these regions it is unlikely he would attempt a shot. Hierarchical models combine information both across space and across different players to estimate such probabilities. 

4.1 Conditional Autoregressive Prior for Player-Specific Coefficients Sharing information between players is critical for our estimation problem, but standard hierarchical models encode an assumption of exchangeability between units that is too strong for NBA players, even between those who are classified by the league as playing the same position. For instance, LeBron James is listed at the same position (small forward) as Steve Novak, despite the fact that James is one of the NBA’s most prolific short-range scorers whereas Novak has not scored a layup since 2012. To model between-player variation more realistically, our hierarchical model shares information across players based on a localized notion of player similarity that we represent as an _L×L_ binary adjacency matrix **H** : _Hℓk_ = 1 if players _ℓ_ and _k_ are similar to each other and _Hℓk_ = 0 otherwise. We determine similarity in a pre-processing step that compares the spatial distribution of where players spend time on the offensive half-court; see Appendix A.2 for exact details on specifying **H** . 

Now let _βji_<sup>_ℓ_bethe</sup><sup>_i_thcomponentof</sup><sup>**_β_**</sup><sup>_ℓ_</sup> _j_<sup>,thevectorofcoefficientsforthetime-referenced</sup> covariates for player _ℓ_ ’s hazard _j_ (8). Also let **_β_** _ji_ be the vector representing this component across all _L_ = 461 players, ( _βji_<sup>1</sup><sup>_β_</sup> _ji_<sup>2</sup><sup>_. . . β_</sup> _ji_<sup>_L_)</sup><sup>_′_.We assume independent conditional autogressive</sup> 

14 

(CAR) priors (Besag 1974) for **_β_** _ji_ : 



where _nℓ_ =<sup>�</sup> _k_<sup>_Hℓk_.Similarly,let</sup><sup>**_β_**</sup> s _i_<sup>= (</sup><sup>_β_</sup> s<sup>1</sup> _i_<sup>_β_</sup> s<sup>2</sup> _i_<sup>_. . .β_</sup> s<sup>_L_</sup> _i_<sup>)bethevectorofthe</sup><sup>_i_thcomponent</sup> of the shot probability model (10) across players 1 _, . . . , L_ . We assume the same CAR prior (12) independently for each component _i_ . While the inverse gamma prior for _τ∗_<sup>2terms seems</sup> very informative, we want to avoid very large or small values of _τ∗_<sup>2,correspondingto0or</sup> full shrinkage (respectively), which we know are inappropriate for our model. Predictive performance for the 0 shrinkage model ( _τ∗_<sup>2verylarge)isshowninTable1,whereasthe</sup> full shrinkage model ( _τ∗_<sup>2=0)doesn’tallowparameterstodifferbyplayeridentity,which</sup> precludes many of the inferences EPV was designed for. 

## 4.2 Spatial Effects _ξ_ 

Player-tracking data is a breakthrough because it allows us to model the fundamental spatial component of basketball. In our models, we incorporate the properties of court space in spatial effects _ξj_<sup>_ℓ,_˜</sup><sup>_ξ_</sup> _j_<sup>_ℓ, ξ_</sup> s<sup>_ℓ_,whichareunknownreal-valuedfunctionsonS,andthereforeinfinite</sup> dimensional. We represent such spatial effects using Gaussian processes (see Rasmussen (2006) for an overview of modeling aspects of Gaussian processes). Gaussian processes are usually specified by a mean function and covariance function; this approach is computationally intractable for large data sets, as the computation cost of inference and interpolating the surface at unobserved locations is _O_ ( _n_<sup>3</sup> ), where _n_ is the number of different points at which _ξj_<sup>_ℓ_isobserved(formanyspatialeffects</sup><sup>_ξ_</sup> _j_<sup>_ℓ_,thecorresponding</sup><sup>_n_wouldbeinthehundreds</sup> of thousands). We instead provide _ξ_ with a low-dimensional representation using functional bases (Higdon 2002; Qui˜nonero-Candela & Rasmussen 2005), which offers three important advantages. First, this representation is more computationally efficient for large data sets such as ours. Second, functional bases allow for a non-stationary covariance structure that reflects unique spatial dependence patterns on the basketball court. Finally, the finite basis representation allows us to apply the same between-player CAR prior to estimate each player’s spatial effects. 

Our functional basis representation of a Gaussian process _ξj_<sup>_ℓ_relieson</sup><sup>_d_deterministic</sup> basis functions _φj_ 1 _, . . . , φjd_ : S _→_ R such that for any **z** _∈_ S, 



where **w** _j_<sup>_ℓ_= (</sup><sup>_w_</sup> _j_<sup>_ℓ_</sup> 1<sup>_. . .w_</sup> _jd_<sup>_ℓ_)</sup><sup>_′_isarandomvectorofloadings,</sup><sup>**w**</sup> _j_<sup>_ℓ∼N_(</sup><sup>**_ω_**</sup><sup>_ℓ_</sup> _j_<sup>_,_</sup><sup>**Σ**</sup><sup>_ℓ_</sup> _j_<sup>).LettingΦ</sup><sup>_j_(</sup><sup>**z**) =</sup> ( _φj_ 1( **z** ) _. . . φjd_ ( **z** ))<sup>_′_</sup> , we can see that _ξj_<sup>_ℓ_givenby(13)isaGaussianprocesswithmean</sup> function Φ _j_ ( **z** )<sup>_′_</sup> **_ω_**<sup>_ℓ_</sup> _j_<sup>andcovariancefunctionCov[</sup><sup>_ξ_</sup> _j_<sup>_ℓ_(</sup><sup>**z**1)</sup><sup>_, ξ_</sup> _j_<sup>_ℓ_(</sup><sup>**z**2)]=Φ</sup><sup>_j_(</sup><sup>**z**1)</sup><sup>_′_</sup><sup>**Σ**</sup><sup>_ℓ_</sup> _j_<sup>Φ</sup><sup>_j_(</sup><sup>**z**2).However,</sup> since bases _φji_ are deterministic, each _ξj_<sup>_ℓ_isrepresentedasa</sup><sup>_d_-dimensionalparameter.Note</sup> that we also use (13) for pass receiver spatial effects and the spatial effect term in the shot˜ probability model, _ξ_<sup>˜</sup> _j_<sup>_ℓ_and</sup><sup>_ξ_</sup> s<sup>_ℓ_,respectively.Forthesetermswehaveassociatedbases</sup> _φji, φ_ s _i_ and weights, _w_ ˜ _ji_<sup>_ℓ, w_</sup> s<sup>_ℓ_</sup> _i_<sup>.Asournotationindicates,basesfunctionsΦ</sup><sup>_j_(</sup><sup>**z**)differforeach</sup> 

15 



_Figure 6: The functional bases φji for i_ = 1 _, . . . ,_ 10 _and j corresponding to the shot-taking macrotransition, j_ = 5 _. There is no statistical interpretation of the ordering of the bases; we have displayed them in rough order of the shot types represented, from close-range to long-range._ 

macrotransition type but are constant across players; whereas weight vectors **w** _j_<sup>_ℓ_vary across</sup> both macrotransition types and players. 

Using _d_ = 10, we determine the functional bases in a pre-processing step, discussed in Appendix A.3. These basis functions are interpretable as patterns/motifs that constitute players’ decision-making tendencies as a function of space; please see Figure 6 for an example, or Miller et al. (2013) for related work in a basketball context. Furthermore, we use a CAR model (12) to supply the prior mean and covariance matrix ( **_ω_**<sup>_ℓ_</sup> _j_<sup>_,_</sup><sup>**Σ**</sup><sup>_ℓ_</sup> _j_<sup>)fortheweights:</sup> 



˜ As with (12), we also use (14) for terms **w** _j_ and **w** s. Combining the functional basis representation (13) with the between-player CAR prior (14) for the weights, we get a prior representation for spatial effects _ξj_<sup>_ℓ,_˜</sup><sup>_ξ_</sup> _j_<sup>_ℓ,_˜</sup><sup>_ξℓ_thatislow-dimensionalandsharesinformation</sup> both across space and between different players. 

## 4.3 Parameter Estimation 

As discussed in Section 3, calculating EPV requires the parameters that define the multiresolution transition models (M1)–(M4)—specifically, the hazards _λ_<sup>_ℓ_</sup> _j_<sup>, shot probabilities</sup><sup>_pℓ_,</sup> and all parameters of the microtransition model (M1). We estimate these parameters in a Bayesian fashion, combining the likelihood of the observed optical tracking data with the prior structure discussed earlier in this section. Using our multiresolution models, we can 

16 

write the likelihood for the full optical tracking data, indexed arbitrarily by _t_ : 



The factorization used in (15) highlights data features that inform different parameter groups: _L_ mic is the likelihood term corresponding to the microtransition model (M1), _L_ entry the macrotransition entry model (M2), and _L_ exit the macrotransition exit model (M3). The remaining term _L_ rem is left unspecified, and ignored during inference. Thus, _L_ mic _, L_ entry _,_ and _L_ exit can be though of as partial likelihoods (Cox 1975 _b_ ), which under mild conditions leads to consistent and asymptotically well-behaved estimators (Wong 1986). When parameters in these partial likelihood terms are given prior distributions, as is the case for those comprising the hazards in the macrotransition entry model, as well as those in the shot probability model, the resulting inference is partially Bayesian (Cox 1975 _a_ ). 

The microtransition partial likelihood term _L_ mic factors by player: 



Depending on whether or not player _ℓ_ is on offense (handling the ball or not) or defense, P( **z** _ℓ_ ( _t_ + _ϵ_ ) _|M_ ( _t_ )<sup>_c_</sup> _, Ft_<sup>(</sup><sup>_Z_)</sup> ) is supplied by the offensive (5) or defensive(6) microtransition models. Parameters for these models (5)–(6) are estimated using R-INLA, where spatial acceleration effects _µ_<sup>_ℓ_</sup> _x_<sup>_, µℓ_</sup> _y_<sup>arerepresentedusingaGaussianMarkovrandomfieldapproximationtoa</sup> Gaussian process with Mat´ern covariance (Lindgren, Rue & Lindstr¨om 2011). Appendix A.3 provides the details on this approximation. We do perform any hierarchical modeling for the parameters of the microtransition model—because this model only describes movement (not decision-making), the data for every player is informative enough to provide precise inference. Thus, microtransition models are fit in parallel using each player’s data separately; this requires _L_ = 461 processors, each taking at most 18 hours at 2.50Ghz clock speed, using 32GB of RAM. 

For the macrotransition entry term, we can write 



17 

recognizing that (for small _ϵ_ ), 



and _T_<sup>_ℓ_</sup> is the set of time _t_ for which player _ℓ_ possesses the ball. Expression (18) is the likelihood for a Poisson regression; combined with prior distributions (12)–(14), inference for **_β_**<sup>_ℓ_</sup> _j_<sup>_,_</sup><sup>**w**</sup> _j_<sup>_ℓ,_</sup><sup>**w**˜</sup> _j_<sup>_ℓ_isthusgivenbyahierarchicalPoissonregression.However,thesizeofourdata</sup> makes implementing such a regression model computationally difficult as the design matrix would have 30.4 million rows and a minimum of _L_ ( _pj_ + _d_ ) _≥_ 5993 columns, depending on macrotransition type. We perform this regression through the use of integrated nested Laplace approximations (INLA) (Rue, Martino & Chopin 2009). Each macrotransition type can be fit separately, and requires approximately 24 hours using a single 2.50GHz processor with 120GB of RAM. 

Recalling Section 3.3, the macrotransition exit model (M3) is deterministic for all macrotransitions except shot attempts ( _j_ = 5). Thus, _L_ exit only provides information on the parameters of our shot probability model (10). Analogous to the Poisson model in (18), _L_ exit is the likelihood of a logistic regression, which factors by player. We also use INLA to fit this hierarchical logistic regression model, though fewer computational resources are required as this likelihood only depends on time points where a shot is attempted, which is a much smaller subset of our data. 

## 5. RESULTS 

After obtaining parameter estimates for the multresolution transition models, we can calculate EPV using Theorem 2.1 and plot _νt_ throughout the course of any possession in our data. We view such (estimated) EPV curves as the main contribution of our work, and their behavior and potential inferential value has been introduced in Section 1. We illustrate this value by revisiting the possession highlighted in Figure 1 through the lens of EPV. Analysts may also find meaningful aggregations of EPV curves that summarize players’ behavior over a possession, game, or season in terms of EPV. We offer two such aggregations in this section. 

## 5.1 Predictive Performance of EPV 

Before analyzing EPV estimates, it is essential to check that such estimates are properly calibrated (Gneiting, Balabdaoui & Raftery 2007) and accurate enough to be useful to basketball analysts. Our paper introduces EPV, and as such there are no existing results to benchmark the predictive performance of our estimates. We can, however, compare the proposed implementation for estimating EPV with simpler models, based on lower resolution information, to verify whether our multiresolution model captures meaningful features of our data. Assessing the predictive performance of an EPV estimator is difficult because the estimand is a curve whose length varies by possession. Moreover, we never observe any portion of this curve; we only know its endpoint. Therefore, rather than comparing estimated EPV curves between our method and alternative methods, we compare estimated transition prob- 

18 

abilities. For any EPV estimator method that is stochastically consistent, if the predicted transitions are properly calibrated, then the derived EPV estimates should be as well. 

For the inference procedure in Section 4, we use only 90% of our data set for parameter inference, with the remaining 10% used to evaluate the out-of-sample performance of our model. We also evaluated out-of-sample performance of simpler macrotransition entry/exit models, which use varying amounts of information from the data. Table 1 provides the out-ofsample log-likelihood for the macrotransition models applied to the 10% of the data not used in model fitting for various simplified models. In particular, we start with the simple model employing constant hazards for each player/event type, then successively add situational covariates, spatial information, then full hierarchical priors. Without any shrinkage, our full model performs in some cases worse than a model with no spatial effects included, but with shrinkage, it consistently performs the best (highest log-likelihood) of the configurations compared. This behavior justifies the prior structure introduced in Section 4. 

|||M|odel|Terms|||
|---|---|---|---|---|---|---|
|Macro. type|Player|Covariates|Co|variates|+ Spatial|Full|
|Pass1|-29.4|-27.7|||-27.2|-26.4|
|Pass2|-24.5|-23.7|||-23.2|-22.2|
|Pass3|-26.3|-25.2|||-25.3|-23.9|
|Pass4|-20.4|-20.4|||-24.5|-18.9|
|Shot Attempt|-48.9|-46.4|||-40.9|-40.7|
|Made Basket|-6.6|-6.6|||-5.6|-5.2|
|Turnover|-9.3|-9.1|||-9.0|-8.4|



_Table 1: Out of sample log-likelihood (in thousands) for macrotransition entry/exit models under various model specifications. “Player” assumes constant hazards for each player/event type combination. “Covariates” augments this model with situational covariates,_ **W** _j_<sup>_ℓ_(</sup><sup>_t_)</sup><sup>_asgivenin_(8)</sup><sup>_._</sup> _“Covariates + Spatial” adds a spatial effect, yielding_ (8) _in its entirety. Lastly, “Full” implements this model with the full hierchical model discussed in Section 4._ 

## 5.2 Possession Inference from Multiresolution Transitions 

Understanding the calculation of EPV in terms of multiresolution transitions is a valuable exercise for a basketball analyst, as these model components reveal precisely how the EPV estimate derives from the spatiotemporal circumstances of the time point considered. Figure 7 diagrams four moments during our example possession (introduced originally in Figures 1 and 2) in terms of multiresolution transition probabilities. These diagrams illustrate Theorem 2.1 by showing EPV as a weighted average of the value of the next macrotransition. Potential ball movements representing macrotransitions are shown as arrows, with their respective values and probabilities graphically illustrated by color and line thickness (this information is also annotated explicitly). Microtransition distributions are also shown, indicating distributions of players’ movement over the next two seconds. Note that the possession diagrammed here was omitted from the data used for parameter estimation. 

Analyzing Figure 7, we see that our model estimates largely agree with basketball intuition. For example, players are quite likely to take a shot when they are near to and/or moving towards the basket, as shown in panels A and D. Additionally, because LeBron James 

19 



<!-- Start of picture text -->
LEGEND<br>2 V 1.09P 0.00 3 V 0.98P 0.04 A Macro MOVEMENTHistory Micro<br>D<br>2<br>A 4 V 1.01 MACROTRANSITION VALUE (V)<br>P 0.06<br>3 High Medium Low<br>4<br>V 1.42P 0.83 MACROTRANSITION PROBABILITY (P)<br>C 1 High Medium Low<br>15<br>B<br>OFFENSE DEFENSE<br>TURNOVER<br>V 0.00 1 Norris Cole Deron Williams 1<br>5 V 1.03 P 0.02 2 Ray Allen Jason Terry 2<br>P 0.04 OTHER 3 Rashard Lewis Joe Johnson 3<br>0 1.2 2.4 3.6 4.8 6.0 7.2 V 0.99P 0.02 4 LeBron James Andray Blatche 4<br>time (sec) 5 Chris Bosh Brook Lopez 5<br>V 1.02 V 1.01<br>P 0.03 V 0.98 P 0.04<br>2 3 P 0.04 B 2 3 C V 1.09 2 V 1.01 1 D<br>2 2 V 1.00 1 P 0.01 P 0.01 V 0.98<br>P 0.13 3 2 3 P 0.04<br>4 1<br>V 1.01<br>3 P 0.23 4 V 1.01P 0.61<br>5 1<br>1 4 4 3<br>V 1.17 15 V 1.01 V 1.50 4 4<br>P 0.27 P 0.05 P 0.83<br>5<br>5 V 1.05<br>TURNOVER P 0.04 TURNOVER TURNOVER<br>5 V 0.00 V 0.00 V 0.00<br>V 1.03P 0.12 OTHERP 0.16 OTHERP 0.01 V 1.03 5 OTHERP 0.04<br>V 1.00 V 0.97 P 0.00 V 1.06<br>P 0.16 P 0.13 P 0.06<br>1.6<br>1.4<br>EPV 1.2<br>1.0<br>0.8<br><!-- End of picture text -->

_Figure 7: Detailed diagram of EPV as a function of multiresolution transition probabilities for four time points (labeled A,B,C,D) of the possession featured in Figures 1–2. Two seconds of microtransitions are shaded (with forecasted positions for short time horizons darker) while macrotransitions are represented by arrows, using color and line thickness to encode the value (V) and probability (P) of such macrotransitions. The value and probability of the “other” category represents the case that no macrotransition occurs during the next two seconds._ 

is a better shooter than Norris Cole, the value of his shot attempt is higher, even though in the snapshot in panel D he is much farther from the basket than Cole is in panel A. While the value of the shot attempt averages over future microtransitions, which may move the player closer to the basket, when macrotransition hazards are high this average is dominated by microtransitions on very short time scales. 

We also see Ray Allen, in the right corner 3, as consistently one of the most valuable pass options during this possession, particularly when he is being less closely defended as in panels A and D. In these panels, though, we never see an estimated probability of him receiving a pass above 0.05, most likely because he is being fairly closely defended for someone so far from the ball, and because there are always closer passing options for the ballcarrier. Similarly, while Chris Bosh does not move much during this possession, he is most valuable 

20 

as a passing option in panel C where he is closest to the basket and without any defenders in his lane. From this, we see that the estimated probabilities and values of the macrotransitions highlighted in Figure 7 match well with basketball intuition. 

The analysis presented here could be repeated on any of hundreds of thousands of possessions available in a season of optical tracking data. EPV plots as in Figure 2 and diagrams as in Figure 7 provide powerful insight as to how players’ movements and decisions contribute value to their team’s offense. With this insight, coaches and analysts can formulate strategies and offensive schemes that make optimal use of their players’ ability—or, defensive strategies that best suppress the motifs and situations that generate value for the opposing offense. 

5.3 EPV-Added 

Aggregations of EPV estimates across possessions can yield useful summaries for player evaluation. For example, _EPV-Added_ (EPVA) quantifies a player’s overall offensive value through his movements and decisions while handling the ball, relative to the estimated value contributed by a league-average player receiving ball possession in the same situations. The notion of _relative_ value is important because the martingale structure of EPV ( _νt_ ) prevents any meaningful aggregation of EPV across a specific player’s possessions. E[ _νt − νt_ + _ϵ_ ] = 0 for all _t_ , meaning that _on average_ EPV does not change during any specific player’s ball handling. Thus, while we see the EPV skyrocket after LeBron James receives the ball and eventually attack the basket in Figure 2, the definition of EPV prevents such increases being observed on average. 

If player _ℓ_ has possession of the ball starting at time _ts_ and ending at _te_ , the quantity _νte − νt_<sup>_r_</sup> _s_<sup>(</sup><sup>_ℓ_)</sup> estimates the value contributed player by _ℓ_ relative to the hypothetical leagueaverage player during his ball possession (represented by _νt_<sup>_r_</sup> _s_<sup>(</sup><sup>_ℓ_)).</sup> We calculate EPVA for player _ℓ_ (EPVA( _ℓ_ )) by summing such differences over all a player’s touches (and dividing by the number of games played by player _ℓ_ to provide standardization): 



where _T_<sup>_ℓ_</sup> contains all intervals of form [ _ts, te_ ] that span player _ℓ_ ’s ball possession. Specific details on calculating _νt_<sup>_r_(</sup><sup>_ℓ_)</sup> are included in Appendix A.4. 

Averaging over games implicitly rewards players who have high usage, even if their value added per touch might be low. Often, one-dimensional offensive players accrue the most EPVA per touch since they only handle the ball when they are uniquely suited to scoring; for instance, some centers (such as the Clippers’ DeAndre Jordan) only receive the ball right next to the basket, where their height offers a considerable advantage for scoring over other players in the league. Thus, averaging by game—not touch—balances players’ efficiency per touch with their usage and importance in the offense. Depending on the context of the analysis, EPVA can also be adjusted to account for team pace (by normalizing by 100 possession) or individual usage (by normalizing by player-touches). 

Table 2 provides a list of the top and bottom 10 ranked players by EPVA using our 201314 data. Generally, players with high EPVA effectively adapt their decision-making process to the spatiotemporal circumstances they inherit when gaining possession. They receive the ball in situations that are uniquely suited to their abilities, so that on average the rest of the league is less successful in these circumstances. Players with lower EPVA are not necessarily 

21 

“bad” players in any conventional sense; their actions simply tend to lead to fewer points than other players given the same options. Of course, EPVA provides a limited view of a player’s overall contributions since it does not quantify players’ actions on defense, or other ways that a player may impact EPV while not possessing the ball (though EPVA could be extended to include these aspects). 

|Rank|Player|EPVA|Rank|Player|EPVA|
|---|---|---|---|---|---|
|1|Kevin Durant|3.26|277|Zaza Pachulia|-1.55|
|2|LeBron James|2.96|278|DeMarcus Cousins|-1.59|
|3|Jose Calderon|2.79|279|Gordon Hayward|-1.61|
|4|Dirk Nowitzki|2.69|280|Jimmy Butler|-1.61|
|5|Stephen Curry|2.50|281|Rodney Stuckey|-1.63|
|6|Kyle Korver|2.01|282|Ersan Ilyasova|-1.89|
|7|Serge Ibaka|1.70|283|DeMar DeRozan|-2.03|
|8|Channing Frye|1.65|284|Rajon Rondo|-2.27|
|9|Al Horford|1.55|285|Ricky Rubio|-2.36|
|10|Goran Dragic|1.54|286|Rudy Gay|-2.59|



_Table 2: Top/bottom 10 players by EPVA per game in 2013-14, minimum 500 touches in season._ 

As such, we stress the idea that EPVA is not a best/worst players in the NBA ranking. Analysts should also be aware that the league-average player being used as a baseline is completely hypothetical, and we heavily extrapolate our model output by considering value calculations assuming this nonexistant player possessing the ball in all the situations encountered by an actual NBA player. The extent to which such an extrapolation is valid is a judgment a basketball expert can make. Alternatively, one can consider EPV-added over _specific_ players (assuming player _ℓ_ 2 receives the ball in the same situations as player _ℓ_ 1), using the same framework developed for EPVA. Such a quantity may actually be more useful, particularly if the players being compared play similar roles on their teams and face similar situations and the degree of extrapolation is minimized. 

## 5.4 Shot Satisfaction 

Aggregations of the individual components of our multiresolution transition models can also provide useful insights. For example, another player metric we consider is called _shot satisfaction_ . For each shot attempt a player takes, we wonder how satisfied the player is with his decision to shoot—what was the expected point value of his most reasonable passing option at the time of the shot? If for a particular player, the EPV measured at his shot attempts is higher than the EPV conditioned on his possible passes at the same time points, then by shooting the player is usually making the best decision for his team. On the other hand, players with pass options at least as valuable as shots should regret their shot attempts (we term “satisfaction” as the opposite of regret) as passes in these situations have higher expected value. 

Specifically, we calculate 



22 

|Rank|Player|Shot Satis.|Rank|Player|Shot Satis.|
|---|---|---|---|---|---|
|1|Mason Plumlee|0.35|277|Garrett Temple|-0.02|
|2|Pablo Prigioni|0.31|278|Kevin Garnett|-0.02|
|3|Mike Miller|0.27|279|Shane Larkin|-0.02|
|4|Andre Drummond|0.26|280|Tayshaun Prince|-0.03|
|5|Brandan Wright|0.24|281|Dennis Schroder|-0.04|
|6|DeAndre Jordan|0.24|282|LaMarcus Aldridge|-0.04|
|7|Kyle Korver|0.24|283|Ricky Rubio|-0.04|
|8|Jose Calderon|0.22|284|Roy Hibbert|-0.05|
|9|Jodie Meeks|0.22|285|Will Bynum|-0.05|
|10|Anthony Tolliver|0.22|286|Darrell Arthur|-0.05|



_Table 3: Top/bottom 10 players by shot satisfaction in 2013-14, minimum 500 touches in season._ 

where _T_ shot<sup>_ℓ_indexestimesashotattemptoccurs,</sup><sup>_{t_:</sup><sup>_M_5(</sup><sup>_t_)</sup><sup>_}_,forplayer</sup><sup>_ℓ_.</sup> Recalling that macrotransitions _j_ = 1 _, . . . ,_ 4 correspond to pass events (and _j_ = 5 a shot attempt), 4 � _j_ =1<sup>_Mj_(</sup><sup>_t_)isequivalenttoapasshappeningin(</sup><sup>_t, t_+</sup><sup>_ϵ_].UnlikeEPVA,shotsatisfaction</sup> SATIS( _ℓ_ ) is expressed as an average per shot (not per game), which favors player such as three point specialists, who often take fewer shots than their teammates, but do so in situations where their shot attempt is extremely valuable. Table 3 provides the top/bottom 10 players in shot satisfaction for our 2013-14 data. While players who mainly attempt threepointers (e.g. Miller, Korver) and/or shots near the basket (e.g. Plumlee, Jordan) have the most shot satisfaction, players who primarily take mid-range or long-range two-pointers (e.g. Aldridge, Garnett) or poor shooters (e.g. Rubio, Prince) have the least. However, because shot satisfaction numbers are mostly positive league-wide, players still shoot relatively efficiently—almost every player generally helps his team by shooting rather than passing in the same situations, though some players do so more than others. 

We stress that the two derived metrics given in this paper, EPVA and shot satisfaction, are simply examples of the kinds of analyses enabled by EPV. Convential metrics currently used in basketball analysis do measure shot selection and efficiency, as well as passing rates and assists, yet EPVA and shot satisfaction are novel in analyzing these events in their spatiotemporal contexts. 

6. DISCUSSION 

This paper introduces a new quantity, EPV, which represents a paradigm shift in the possibilities for statistical inferences about basketball. Using high resolution, optical tracking data, EPV reveals the value in many of the schemes and motifs that characterize basketball offenses but are omitted in the box score. For instance, as diagrammed in Figures 2 and 7, we see that EPV may rise as a player attacks the basket (more so for a strong scorer like LeBron James than for a bench player like Norris Cole), passes to a well-positioned teammate, or gains separation from the defense. Aside from simply tracking changes in EPV, analysts can understand why EPV changes by expressing its value as a weighted average of transition values (as done in Figure 7). Doing so reveals that the source of a high (or low) EPV estimate may come from alternate paths of the possession that were never realized, but were probable enough to have influenced the EPV estimate—an open teammate in a good 

23 

shooting location, for instance. These insights, which can be reproduced for any valid NBA possession in our data set, have the potential to reshape the way we quantify players’ actions and decisions. 

We make a number of assumptions—mostly to streamline and simplify our modeling and analysis pipeline—that could be relaxed and yield a more precise model. The largest assumption is that the particular coarsened view of a basketball possession that we propose here is marginally semi-Markov. While this serves as a workable first-order approximation, there are cases that clearly violate this assumption, for example, pre-set plays that string together sequences of runs and passes. Future refinements of the model could define a wider set of macrotransitions and coarsened states to encapsulate these motifs, effectively encoding this additional possession structure from the coach’s playbook. 

A number of smaller details could also be addressed. For instance, it seems desirable to model rebound outcomes conditional on high resolution information, such as the identities and motion dynamics of potential rebounders; we do not do this, however, and use a constant probability for each team of a rebound going to either the offense or defense. We also do not distinguish between different types of turnovers (steals, bad passes, ball out of bounds, etc.), though this is due to a technical feature of our data set. Indeed, regardless of the complexity and refinement of an EPV model, we stress that the full resolution data still omits key information, such as the positioning of players’ hands and feet, their heights when jumping, and other variables that impact basketball outcomes. As such, analyses based on EPV are best accompanied by actual game film and the insight of a basketball expert. 

The computational requirements of estimating EPV curves (and the parameters that generate them) likely limit EPV discussions to academic circles and professional basketball teams with access to the appropriate resources. Our model nevertheless offers a case study whose influence extends beyond basketball. High resolution spatiotemporal data sets are an emerging inferential topic in a number of scientific or business areas, such as climate, security and surveillance, advertising, and gesture recognition. Many of the core methodological approaches in our work, such as using multiresolution transitions and hierarchical spatial models, provide insight beyond the scope of basketball to other spatiotemporal domains. 

24 

APPENDIX A. ADDITIONAL TECHNICAL DETAILS 

In this appendix we provide additional details on steps used in fitting multiresolution models and deriving basketball metrics from EPV estimates. 

A.1 Time-Varying Covariates in Macrotransition Entry Model As revealed in (8), the hazards _λ_<sup>_ℓ_</sup> _j_<sup>(</sup><sup>_t_)areparameterizedbyspatialeffects(</sup><sup>_ξ_</sup> _j_<sup>_ℓ_and</sup><sup>_ξ_˜</sup> _j_<sup>_ℓ_for</sup> pass events), as well as coefficients for situation covariates, **_β_**<sup>_ℓ_</sup> _j_<sup>.Thecovariatesusedmaybe</sup> different for each macrotransition _j_ , but we assume for each macrotransition type the same covariates are used across players _ℓ_ . 

Among the covariates we consider, `dribble` is an indicator of whether the ballcarrier has started dribbling after receiving possession. `ndef` is the distance between the ballcarrier and his nearest defender (transformed to log(1+ _d_ )). `ball` ~~`l`~~ `astsec` records the distance traveled by the ball in the previous one second. `closeness` is a categorical variable giving the rank of the ballcarrier’s teammates’ distance to the ballcarrier. Lastly, `open` is a measure of how open a potential pass receiver is using a simple formula relating the positions of the defensive players to the vector connecting the ballcarrier with the potential pass recipient. 

For _j ≤_ 4, the pass event macrotransitions, we use `dribble` , `ndef` , `closeness` , and `open` . For shot-taking and turnover events, `dribble` , `ndef` , and `ball` ~~`l`~~ `astsec` are included. Lastly, the shot probability model (which, from (10) has the same parameterization as the macrotransition model) uses `dribble` and `ndef` only. All models also include an intercept term. As discussed in Section 4.1, independent CAR priors are assumed for each coefficient in each macrotransition hazard model. 

## A.2 Player Similarity Matrix **H** for CAR Prior 

The hierarchical models used for parameters of the macrotransition entry model, discussed in Section 4.1, are based on the idea that players who share similar roles for their respective teams should behave similarly in the situations they face. Indeed, players’ positions (point guard, power forward, etc.) encode their offensive responsibilities: point guards move and distribute the ball, small forwards penetrate and attack the basket, and shooting guards get open for three-point shots. Such responsibilities reflect spatiotemporal decision-making tendencies, and therefore informative for our macrotransition entry model (7)–(8). 

Rather than use the labeled positions in our data, we define position as a distribution of a player’s location during his time on the court. Specifically, we divide the offensive half of the court into 4-square-foot bins (575 total) and count, for each player, the number of data points for which he appears in each bin. Then we stack these counts together into a _L ×_ 575 matrix (there are _L_ = 461 players in our data), denoted **G** , and take the square root of all entries in **G** for normalization. We then perform non-negative matrix factorization (NMF) on **G** in order to obtain a low-dimensional representation of players’ court occupancy that still reflects variation across players (Miller et al. 2013). Specifically, this involves solving: 



where _r_ is the rank of the approximation **G**<sup>ˆ</sup> to **G** (we use _r_ = 5), and _D_ is some distance 

25 

function; we use a Kullback-Liebler type 



The rows of **V** are non-negative basis vectors for players’ court occupancy distributions (plotted in Figure 8) and the rows of **U** give the loadings for each player. With this factorization, **U** _i_ (the _i_ th row of **U** ) provides player _i_ ’s “position”—a _r_ -dimensional summary of where he spends his time on the court. Moreover, the smaller the difference between two players’ positions, _||_ **U** _i −_ **U** _j||_ , the more alike are their roles on their respective teams, and the more similar we expect the parameters of their macrotransition models to be a priori. 



_Figure 8: The rows of_ **V** _(plotted above for r_ = 5 _) are bases for the players’ court occupancy distribution. There is no interpretation to the ordering._ 

Formalizing this, we take the _L×L_ matrix **H** to consist of 0s, then set _Hij_ = 1 if player _j_ is one of the eight closest players in our data to player _i_ using the distance _||_ **U** _i−_ **U** _j||_ (the cutoff of choosing the closest eight players is arbitrary). This construction of **H** does not guarantee symmetry, which is required for the CAR prior we use, thus we set _Hji_ = 1 if _Hij_ = 1. For instance, LeBron James’ “neighbors” are (in no order): Andre Iguodala, Harrison Barnes, Paul George, Kobe Bryant, Evan Turner, Carmelo Anthony, Rodney Stuckey, Will Barton, and Rudy Gay. 

## A.3 Basis Functions for Spatial Effects _ξ_ 

Recalling (13), for each player _ℓ_ and macrotransition type _j_ , we have _ξj_<sup>_ℓ_(</sup><sup>**z**) = �</sup> _i_<sup>_d_</sup> =1<sup>_w_</sup> _ji_<sup>_ℓφji_(</sup><sup>**z**),</sup> where _{φji, i_ = 1 _, . . . , d}_ are the basis functions for macrotransition _j_ . During the inference discussed in Section 4, these basis functions are assumed known. They are derived from a pre-processing step. Heuristically, they are constructed by approximately fitting a simplified macrotransition entry model with stationary spatial effect for each player, then performing NMF to find a low-dimensional subspace (in this function space of spatial effects) that accurately captures the spatial dependence of players’ macrotransition behavior. We now describe this process in greater detail. 

Each basis function _φji_ is itself represented as a linear combination of basis functions, 



where _{ψk, k_ = 1 _, . . . , d_ 0 _}_ are basis functions (as the notation suggests, the same basis is used for all _j_ , _i_ ). The basis functions _{ψk, k_ = 1 _, . . . , d_ 0 _}_ are induced by a triangular mesh of _d_ 0 vertices (we use _d_ 0 = 383) on the court space S. In practice, the triangulation is defined on 

26 

a larger region that includes S, due to boundary effects. The mesh is formed by partitioning S into triangles, where any two triangles share at most one edge or corner; see Figure 9 for an illustration. With some arbitrary ordering of the vertices of this mesh, _ψk_ : S _→_ R is the unique function taking value 0 at all vertices _k_<sup>˜</sup> = _k_ , 1 at vertex _k_ , and linearly interpolating between any two points within the same triangle used in the mesh construction. Thus, with this basis, _φji_ (and consequently, _ξj_<sup>_ℓ_)arepiecewiselinearwithinthetrianglesofthemesh.</sup> 



_Figure 9: Triangulation of_ S _used to build the functional basis {ψk, k_ = 1 _, . . . , d_ 0 _}. Here, d_ 0 = 383 _._ 

This functional basis _{ψk, k_ = 1 _, . . . , d_ 0 _}_ is used by Lindgren et al. (2011), who show that it can approximate a Gaussian random field with Mat´ern covariance. Specifically, let _x_ ( **z** ) =<sup>�</sup> _k_<sup>_d_0</sup> =1<sup>_vkψk_(</sup><sup>**z**)andassume(</sup><sup>_v_1</sup><sup>_. . .vk_)</sup><sup>_′_=</sup><sup>**v**</sup><sup>_∼N_(0</sup><sup>_,_</sup><sup>**Σ**</sup><sup>_ν,κ,σ_2).Theformof</sup><sup>**Σ**</sup><sup>_ν,κ,σ_2is</sup> such that the covariance function of _x_ approximates a Mat´ern covariance: 



where **_ψ_** ( **z** ) = ( _ψ_ 1( **z** ) _. . . ψd_ 0( **z** ))<sup>_′_</sup> . As discussed in Section 4.2, the functional basis representation of a Gaussian process offers computational advantages in that the infinite dimensional field _x_ is given a _d_ 0-dimensional representation, as _x_ is completely determined by **v** . Furthermore, as discussed in Lindgren et al. (2011), **Σ**<sup>_−_</sup> _ν,κ,σ_<sup>12issparse((A.3)isactuallyaGaussian</sup> Markov random field (GMRF) approximation to _x_ ), offering additional computational savings (Rue 2001). 

The GMRF approximation given by (A.2)–(A.3) is actually used in fitting the microtransition models for offensive players (5). We give the spatial innovation terms _µ_<sup>_ℓ_</sup> _x_<sup>_, µℓ_</sup> _y_ representations using the _ψ_ basis. Then, as mentioned in Section 4.3, (5) is fit independently for each player in our data set using the software R-INLA. 

We also fit simplified versions of the macrotransition entry model, using the _ψ_ basis, in order to determine _{vjik, k_ = 1 _, . . . , d_ 0 _}_ , the loadings of the basis representation for _φ_ , (A.2). This simplified model replaces the macrotransition hazards (8) with 



thus omitting situational covariates ( **_β_**<sup>_ℓ_</sup> _j_<sup>in (8)) and using the</sup><sup>_ψ_basis representation in place</sup> 

27 

of _ξj_<sup>_ℓ_.Notethatforpassevents,like(8),wehaveanadditionaltermbasedonthepass</sup> ˜ recipient’s location, parameterized by _{u_<sup>_ℓ_</sup> _jk_<sup>_, k_=1</sup><sup>_, . . . , d_0</sup><sup>_}_.</sup> As discussed in Section 4.3, parameters in (A.4) can be estimated by running a Poisson regression. We perform this independently for all players _ℓ_ and macrotransition types _j_ using the R-INLA software. Like the microtransition model, we fit (A.4) separately for each player across _L_ = 461 processors (each hazard type _j_ is run in serial), each requiring at most 32GB RAM and taking no more than 16 hours. 

ˆ For each macrotransition type _j_ , point estimates _u_<sup>_ℓ_</sup> _jk_<sup>are exponentiated6, so that [</sup><sup>**U**</sup><sup>_j_]</sup><sup>_ℓk_=</sup> exp(ˆ _u_<sup>_ℓ_</sup> _jk_<sup>).WethenperformNMF(A.1)on</sup><sup>**U**</sup><sup>_j_:</sup> 



Following the NMF example in Section A.2, the rows of **V** _j_ are bases for the variation in coefficients _{u_<sup>_ℓ_</sup> _jk_<sup>_, k_= 1</sup><sup>_, . . . , d_0</sup><sup>_}_acrossplayers</sup><sup>_ℓ_.As1</sup><sup>_≤k≤d_0indexespointsonourcourt</sup> triangulation (Figure 9), such bases reflect structured variation across space. We furthermore use these terms as the coefficients for (A.2), the functional basis representation of _φji_ , setting _vjik_ = [ **V** _j_ ] _ik_ . Equivalently, we can summarize our spatial basis model as: _ξj_<sup>_ℓ_(</sup><sup>**z**) = [</sup><sup>**w**</sup> _j_<sup>_ℓ_]</sup><sup>_′_</sup><sup>**_φ_**</sup> _j_<sup>(</sup><sup>**z**) = [</sup><sup>**w**</sup> _j_<sup>_ℓ_]</sup><sup>_′_</sup><sup>**V**</sup><sup>_j_</sup><sup>**_ψ_**(</sup><sup>**z**)</sup><sup>_._</sup> (A.6) The preprocessing steps described in this section—fitting a simplified macrotransition entry model (A.4) and performing NMF on the coefficient estimates (A.5)—provide us with basis functions _φji_ ( **z** ) that we treat as fixed and known during the modeling and inference discussed in Section 4. 

Note that an analogous expression for (A.6) is used for _ξ_<sup>˜</sup> _j_<sup>_ℓ_intermsof</sup><sup>**w**˜</sup> _j_<sup>_ℓ_and</sup><sup>**V**˜</sup><sup>_j_for</sup> pass events; however, for the spatial effect _ξ_ s<sup>_ℓ_intheshotprobabilitymodel,wesimplyuse</sup> **V** 5. Thus, the basis functions for the shot probability model are the same as those for the shot-taking hazard model. 

A.4 Calculating EPVA: Baseline EPV for League-Average Player To calculate the baseline EPV for a league-average player possessing the ball in player _ℓ_ ’s shoes, denoted _νt_<sup>_r_(</sup><sup>_ℓ_)</sup> in (19), we start by considering an alternate version of the transition probability matrix between coarsened states **P** . For each player _ℓ_ 1 _, . . . , ℓ_ 5 on offense, there is a disjoint subset of rows of **P** , denoted **P** _ℓi_ , that correspond to possession states for player _ℓi_ . Each row of **P** _ℓi_ is a probability distribution over transitions in _C_ given possession in a particular state. Technically, since states in _C_ poss encode player identities, players on different teams do not share all states which they have a nonzero probability of transitioning to individually. To get around this, we remove the columns from each **P** _ℓi_ corresponding to passes to players not on player _ℓi_ ’s team, and reorder the remaining columns according to the position (guard, center, etc.) of the associated pass recipient. Thus, the interpretation of transition distributions **P** _ℓi_ across players _ℓi_ is as consistent as possible. 

> 6 ˆ _ℓ_ The reason for exponentiation is because estimates _ujk_<sup>inform the log hazard, so exponentiation converts</sup> these estimates to a more natural scale of interest. Strong negative signals among the _u_ ˆ<sup>_ℓ_</sup> _jk_<sup>willmoveto0</sup> in the entries of **U** _j_ and not be very influential in the matrix factorization (A.5), which is desirable for our purposes. 

28 

We create a baseline transition profile of a hypothetical league-average player by averaging these transition probabilities across all players: (with slight abuse of notation) let **P** _r_ = _L_ � _ℓ_ =1<sup>**P**</sup><sup>_ℓ/L_.Usingthis,wecreateanewtransitionprobabilitymatrix</sup><sup>**P**</sup><sup>_r_(</sup><sup>_ℓ_)byreplacing</sup> player _ℓ_ ’s transition probabilities ( **P** _ℓ_ ) with the league-average player’s ( **P** _r_ ). The baseline (league-average) EPV at time _t_ is then found by evaluating _νt_<sup>_r_(</sup><sup>_ℓ_)</sup> = E **P** _r_ ( _ℓ_ )[ _X|Ct_ ]. Note that _νt_<sup>_r_(</sup><sup>_ℓ_)</sup> depends only on the coarsened state _Ct_ at time _t_ , rather than the full history of the possession, _Ft_<sup>(</sup><sup>_Z_)</sup> , as in _νt_ (4). This “coarsened” baseline _νt_<sup>_r_(</sup><sup>_ℓ_)</sup> exploits the fact that, when averaging possessions over the entire season, the results are (in expectation) identical to using a full-resolution baseline EPV that assumes the corresponding multiresolution transition probability models for this hypothetical league-average player. 

## APPENDIX B. DATA AND CODE 

The Git repository `https://github.com/dcervone/EPVDemo` contains a one game sample of optical tracking data (csv), along with R code for visualizing model results and reproducing EPV calculations. Pre-computed results of computationally-intensive steps are also included as Rdata files, and can be loaded to save time and resources. A reproducible knitr tutorial, `EPV` ~~`d`~~ `emo.Rnw` , introduces the data and demonstrates core code functionality. 

## REFERENCES 

- Besag, J. (1974), “Spatial Interaction and the Statistical Analysis of Lattice Systems,” _Journal of the Royal Statistical Society: Series B (Methodological)_ , 36(2), 192–236. 

- Bukiet, B., Harold, E. R., & Palacios, J. L. (1997), “A Markov Chain Approach to Baseball,” _Operations Research_ , 45(1), 14–23. 

- Burke, B. (2010), “Win Probability Added (WPA) Explained,” _www.advancedfootballanalytics.com_ , (website). 

- Cox, D. R. (1975 _a_ ), “A Note on Partially Bayes Inference and the Linear Model,” _Biometrika_ , 62(3), 651–654. 

- Cox, D. R. (1975 _b_ ), “Partial Likelihood,” _Biometrika_ , 62(2), 269–276. 

- Franks, A., Miller, A., Bornn, L., & Goldsberry, K. (2015), “Characterizing the Spatial Structure of Defensive Skill in Professional Basketball,” _Annals of Applied Statistics_ , . 

- Gneiting, T., Balabdaoui, F., & Raftery, A. E. (2007), “Probabilistic forecasts, calibration and sharpness,” _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 69(2), 243–268. 

- Goldner, K. (2012), “A Markov Model of Football: Using Stochastic Processes to Model a Football Drive,” _Journal of Quantitative Analysis in Sports [online]_ , 8(1). 

- Higdon, D. (2002), “Space and Space-Time Modeling Using Process Convolutions,” in _Quantitative Methods for Current Environmental Issues_ , New York, NY: Springer, pp. 37–56. 

- Hollinger, J. (2005), _Pro Basketball Forecast, 2005-06_ , Washington, D.C: Potomac Books. 

29 

- Ihler, A., Hutchins, J., & Smyth, P. (2006), “Adaptive Event Detection with Time-Varying Poisson Processes,” in _Proceedings of the 12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , New York, NY: ACM, pp. 207–216. 

- Kemeny, J. G., & Snell, J. L. (1976), _Finite Markov chains: with a new appendix” Generalization of a fundamental matrix”_ Springer. 

- Lindgren, F., Rue, H., & Lindstr¨om, J. (2011), “An Explicit Link Between Gaussian Fields and Gaussian Markov Random Fields: the Stochastic Partial Differential Equation Approach,” _Journal of the Royal Statistical Society: Series B (Methodological)_ , 73(4), 423– 498. 

- Lock, D., & Nettleton, D. (2014), “Using random forests to estimate win probability before each play of an NFL game,” _Journal of Quantitative Analysis in Sports_ , 10(2), 197–205. 

- Miller, A., Bornn, L., Adams, R., & Goldsberry, K. (2013), “Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball,” in _Proceedings of the 31st International Conference on Machine Learning_ , pp. 235–243. 

- Omidiran, D. (2011), “A New Look at Adjusted Plus/Minus for Basketball Analysis,” _MIT Sloan Sports Analytics Conference [online]_ , 2011. 

- Prentice, R. L., Kalbfleisch, J. D., Peterson Jr, A. V., Flournoy, N., Farewell, V., & Breslow, N. (1978), “The Analysis of Failure Times in the Presence of Competing Risks,” _Biometrics_ , pp. 541–554. 

- Qui˜nonero-Candela, J., & Rasmussen, C. E. (2005), “A Unifying View of Sparse Approximate Gaussian Process Regression,” _The Journal of Machine Learning Research_ , 6, 1939– 1959. 

- Rasmussen, C. E. (2006), _Gaussian Processes for Machine Learning_ , Cambridge, MA: MIT Press. 

- Rue, H. (2001), “Fast sampling of Gaussian Markov random fields,” _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 63(2), 325–338. 

- Rue, H., Martino, S., & Chopin, N. (2009), “Approximate Bayesian Inference for Latent Gaussian Models by Using Integrated Nested Laplace Approximations,” _Journal of the Royal Statistical Society: Series B (Methodological)_ , 71(2), 319–392. 

- Shao, X., & Li, L. (2011), “Data-Driven Multi-Touch Attribution Models,” in _Proceedings of the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , New York, NY: ACM, pp. 258–264. 

- Thomas, A., Ventura, S. L., Jensen, S. T., & Ma, S. (2013), “Competing Process Hazard Function Models for Player Ratings in Ice Hockey,” _The Annals of Applied Statistics_ , 7(3), 1497–1524. 

- Wong, W. H. (1986), “Theory of Partial Likelihood,” _The Annals of Statistics_ , pp. 88–123. 

- Yang, T. Y., & Swartz, T. (2004), “A Two-Stage Bayesian Model for Predicting Winners in Major League Baseball,” _Journal of Data Science_ , 2(1), 61–73. 

30 


