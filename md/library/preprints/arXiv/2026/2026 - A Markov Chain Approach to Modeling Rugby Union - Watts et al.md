<!-- source: library/preprints/arXiv/2026/2026 - A Markov Chain Approach to Modeling Rugby Union - Watts & Pipping-Gamón (arXiv 2610.04813).pdf -->
<!-- item: https://arxiv.org/abs/2610.04813 -->
<!-- arXiv: 2610.04813, submitted 2026-10-03 -->
<!-- authors: Kenny Watts; Jonathan Pipping-Gamón -->
<!-- machine conversion from the stored PDF via pdftotext -layout, 2026-10-28; equations, tables and figures are NOT preserved - consult the PDF for those -->

                                           A Markov Chain Approach to Modeling Rugby Union

                                                          Kenny Watts                           Jonathan Pipping-Gamón
                                                      University of Virginia                    University of Pennsylvania
                                                     xen5ek@virginia.edu                      jpipping@wharton.upenn.edu
arXiv:2610.04813v1 [stat.AP] 3 Oct 2026

                                                                                  October 2026

                                                                                      Abstract

                                                   Rugby Union’s continuous play, variable-length possessions, and multiple scoring
                                               outcomes make it difficult to model with standard approaches. We present a Markov
                                               Chain framework that represents Rugby Union as a finite state space over score differ-
                                               ential, remaining time, and pitch location, with transition probabilities estimated from
                                               historical match data.
                                                   The resulting model supports simulation and analysis of in-game trajectories, includ-
                                               ing win probability and expected point estimates from any given state. We validate the
                                               model through calibration analysis and comparison to models that predict only final
                                               outcomes. Our state-space approach produces well-calibrated, competitive estimates
                                               while additionally enabling analysis of how games evolve between states.

                                          1    Introduction
                                          Markov models have been applied extensively in various sports including American Football
                                          (Goldner, 2012), Baseball (Bukiet et al., 1997), and Tennis (Newton and Aslam, 2009).
                                          Rugby Union shares structural features with American Football: variable field position,
                                          alternating possessions, and scoring plays with differing point totals. However, Rugby Union
                                          differs in that there aren’t cleanly defined plays or drives, with continuous possessions that
                                          can vary greatly in length. This motivates a state-space model specifically built for Rugby’s
                                          unique structure.
                                          We build a first order-markov chain built from a state space based on time, field position, and
                                          the current score. This approach has two practical advantages for our setting. First, because
                                          the chain is generative rather than purely predictive, it produces full match trajectories
                                          rather than isolated point estimates, meaning we can simulate forward from any given state
                                          to recover not just a win probability but a distribution over final margins, time-to-next-
                                          score, and momentum shifts, which supports richer post-hoc interpretation of trajectories.
                                          Second, and more importantly given our data constraints, the model is substantially more
                                          data-efficient. Our dataset covers a single season, which yields a comparatively small number
                                          of complete match outcomes, the unit that a feature-to-outcome classifier such as logistic

                                                                                          1
regression, XGBoost, or a random forest would need in volume to fit a robust decision
boundary and avoid overfitting to season-specific noise. A Markov chain instead estimates
transition probabilities from the much larger pool of in-game state transitions (scoring events,
phase changes, territorial shifts) that occur many times within and across matches, meaning
each game contributes dozens of independent transition observations rather than a single
outcome label. This makes the transition-probability estimates considerably more stable
given a one-season sample than a model that must learn its structure from final match
outcomes alone.
In American football, win probability models are now well established and inform coaching
decisions and the evaluation of play-level outcomes (Lock and Nettleton, 2014; Yurko et al.,
2019). Early implementations relied on random forests and generalized additive models
(Lock and Nettleton, 2014; Yurko et al., 2019), while more recent work has moved toward
gradient-boosted methods capable of capturing nonlinear interactions between game-state
variables (Baldwin, 2021). These models have also proven useful beyond in-game forecasting:
game-state-based expected-value frameworks have been used to evaluate the rationality of
coaching decisions, such as fourth-down strategy (Romer, 2006).
Within Rugby Union itself, quantitative work has begun to adopt expected-points frame-
works adapted from American football. Martinez-Arastey et al. (2025) lay methodological
foundations for expected points in rugby union, with their phase-level data making it pos-
sible to construct the state space underlying our model. Watts and Pipping-Gamón (2026)
applied an expected-points approach to a more specific in-game decision problem, evaluating
whether kicking for goal or for touch is the better choice following a penalty. Both works
demonstrate the value of state-based, points-oriented modeling in rugby, but neither devel-
ops a full generative state-space model capable of simulating complete match trajectories or
producing dynamic, in-game win probability estimates alongside expected points.

2    First-order Markov Chain
The name “Markov chain” derives from the first-order Markov property, which states that
the probability of transitioning to the next state depends only on the current state, not on
the sequence of states that preceded it. Let Sn ∈ S denote the state at time n, where S is
the state space. Formally, for any timestep n, the next state Sn is conditionally independent
of all previous states Sn−2 , Sn−3 , . . . , S1 given the current state Sn−1 :

           P (Sn = snew | Sn−1 = sn−1 , . . . , S1 = s1 ) = P (Sn = snew | Sn−1 = sn−1 )    (1)

This property is often described as “memoryless”: the system has no memory of how it
arrived at its current state, only where it is now. In the context of our model, this means we
assume that predicting what happens next requires only the current game situation (score
differential, remaining time, and pitch location) rather than the entire history of prior plays.
While we admit that certain path-dependent effects may exist, this assumption is both
computationally efficient and reasonable given the difficulty of reliably inferring how specific
play sequences influence future outcomes.

                                                2
3    Defining States
A state s ∈ S is a tuple s = (t, f, g) representing the game context at a given possession,
where the full state space decomposes as a Cartesian product:

                                       S = T × F × G.

Time bucket T
We divide each half into three segments based on seconds remaining, yielding |T | = 6 buckets:

          T = {1h_start, 1h_middle, 1h_end, 2h_start, 2h_middle, 2h_end},

where start and end correspond to the first and last two minutes of each half, respectively,
and middle covers the remainder.

Field position F
Field position is expressed as the possession team’s distance, in meters, from the opposition’s
try line. From our phase-level data these are discretized into |F| = 8 ordinal zones centered
on the following meter lines:

                        F = {2.5, 13.5, 31, 45, 55, 69, 86.5, 97.5}.

Score bucket G
The score margin is expressed from the perspective of the possession team—that is, the
signed difference δ = scoreposs − scoreopp —and coarsened into |G| = 7 ordinal buckets:
                                  
                                  
                                  
                                   down_14p if δ ≤ −14,
                                    down_7_13 if − 13 ≤ δ ≤ −7,
                                  
                                  
                                  
                                  
                                  
                                  down_1_6 if − 6 ≤ δ ≤ −1,
                                  
                                  
                                  
                          g(δ) = tied            if δ = 0,
                                                 if 1 ≤ δ ≤ 6,
                                  
                                    up_1_6
                                  
                                  
                                  
                                  
                                                 if 7 ≤ δ ≤ 13,
                                  
                                  
                                  
                                  
                                   up_7_13
                                                 if δ ≥ 14.
                                  
                                  up_14p

By conditioning on the possession team rather than a fixed home or away side, the transition
dynamics are symmetric across teams by construction.

State encoding
In practice, a state is encoded as a concatenated string key, for example 2h_end_22_up_1_6,
denoting the second half’s final two minutes, field position at the 22 m line, with the posses-
sion team leading by one to six points. The total number of states is |S| = 6 × 8 × 7 = 336.

                                              3
4     Transition Matrix
A first-order Markov chain is characterised by its transition probability matrix P, where
each entry psn ,sn+1 represents the probability of transitioning from state sn to state sn+1 :

                   P (Sn+1 = sn+1 | Sn = sn ) = psn , sn+1 ,      sn , sn+1 ∈ S.

In our rugby model, each row of P corresponds to a current game state sn ∈ S (defined
by time bucket, field position, and score bucket), and each column represents a possible
successor state sn+1 . The matrix has the following general structure:
                                                                                  
                            ps1 ,s1 ps1 ,s2 · · · ps1 , PC ps1 , S3 ps1 , S5 · · ·
                           ps ,s ps ,s · · · ps , PC ps , S3 ps , S5 · · ·
                                                                                     (2)
                           2 1       2 2           2        2        2
                     P =  ..         ..    .        ..       ..       ..    .
                                                                                   
                           .          .      . .     .        .        .      . .
                                                                                   
                           psn ,s1 psn ,s2 · · · psn , PC psn , S3 psn , S5 · · ·

where each row sums to unity,
                                  X
                                           psn , sn+1 = 1 ∀ sn ∈ S,
                                 sn+1 ∈S

ensuring that from any state sn the probabilities of all possible transitions sum to certainty.
The columns represent transitions to different field-position states, possession changes (PC),
and scoring events (S3, S5, S7 for 3, 5, and 7 points respectively). All transition probabilities
are estimated empirically from historical match data, with each entry psn ,sn+1 representing
the observed frequency of transitioning from sn to sn+1 in the dataset.

5     Simulation and Win Probability Estimation
To estimate win probabilities, we employ Monte Carlo simulation, running the Markov chain
forward from a given game state many times to generate a distribution of possible outcomes.
Each simulation represents one possible sequence of events that could unfold from the current
state until the end of the match.

5.1    Event Sequences
A single simulation consists of a sequence of state transitions, where at each step the model
samples the next event according to the transition probabilities in P. Consider the following
example sequence starting from kickoff:
Each state can transition in several ways: movement to a new field position, persistence in
the current position, a change of possession, or a scoring event (awarding 3, 5, or 7 points). In
this sequence, possession changes hands twice before the away team scores 7 points, updating
both the score and the game state. Each transition is sampled according to the empirical
probabilities observed in our training data for the corresponding state.

                                                   4
              Table 1: Example Play-by-Play Sequence from a Single Simulation
      Play   State Before           Event             Poss.   Home Away         State After
       1     1h_start_69_tied       1h_middle_69_tied Home      0   0       1h_middle_69_tied
       2     1h_middle_69_tied      Possession_Change Away      0   0        1h_middle_69_tied
       3     1h_middle_69_tied      Possession_Change Home      0   0        1h_middle_69_tied
       4     1h_middle_69_tied      Score_7           Away      0   7      1h_middle_69_up_7_13
       5     1h_middle_69_up_7_13   Possession_Change Home      0   7     1h_middle_13.5_up_7_13

5.2     Aggregating Simulations
By running this process N times we obtain a distribution of final outcomes. Win probability
is then calculated as the proportion of simulations in which each team wins:

                                             Number of simulations where Home wins
               P (Home Win | State) =                                                              (3)
                                                               N
Consider a match state in the middle of the second half where the home team holds a 21-14
lead with possession at the 45-meter line. Given this combination of a 7-point advantage,
possession, and favorable field position, we would expect the home team to have a strong
likelihood of victory. Running 1000 simulations from this state confirms this intuition:

                              Table 2: Aggregated Simulation Results

 Home Wins          Away Wins         Ties    Home Win Prob         Away Win Prob           Tie Prob
    832                129             39         0.832                  0.129                0.039

This approach allows us to estimate win probabilities for any game state, accounting for the
stochastic nature of Rugby and the multiple pathways through which a match can unfold.

6     Win Probability: Performance and Error Reduction
We evaluated the performance of our Markov chain model where the first 80% of the season
was used as training data and the last 20% as the test set. Comparing predictive accuracy
against two baseline models: a naive model that assigns 0.5 win probability to each team
regardless of game state, and a proportion-based model that assigns win probabilities based
solely on the overall proportion of home wins in the dataset.

6.1     Performance Metrics
Model accuracy is assessed using Root Mean Squared Error (RMSE) and Mean Squared
Error (MSE), which measure the average deviation between predicted win probabilities and
actual outcomes. Lower values indicate better predictive performance. We also calculate
error reduction relative to the baseline models:

                                               MSEbaseline − MSEmodel
                       Error Reduction =                              × 100%                       (4)
                                                   MSEbaseline

                                                    5
6.2    Results
      Table 3: Model Performance and Error Reduction vs. Baselines (Out-of-Sample)

                      Model                 MSE     Error Reduction
                      XGBoost               0.182        23.6%
                      Logistic Regression   0.183        23.3%
                      Markov Model          0.188        21.4%
                      Random Forest         0.206        13.7%
                      Naive Baseline        0.239          –

The Markov chain model achieves a 21.4% reduction in MSE relative to the naive baseline
(predicting 50% win probability for each team), performing competitively with machine
learning alternatives such as XGBoost (23.6%) and logistic regression (23.3%) while retaining
full interpretability and the ability to simulate complete game trajectories.

7     Model Calibration
Beyond predictive accuracy, a well-calibrated model ensures that predicted probabilities align
with observed outcomes. For instance, among all predictions where the model assigns a 70%
win probability, we would expect the team to win approximately 70% of the time. We assess
calibration by binning predictions into deciles and comparing the mean predicted probability
within each bin to the observed win rate.
Figures 1 shows calibration plots for the in-sample and out-of-sample datasets, respectively.
The diagonal line represents perfect calibration, where predicted probabilities exactly match
observed frequencies. Points close to this line indicate good calibration.

       (a) In-sample calibration                             (b) Out-of-sample calibration

Figure 1: Calibration plots showing alignment between predicted probabilities and observed
outcomes. (1) In-sample predictions demonstrate good calibration across all probability
bins. (1) Out-of-sample predictions maintain good calibration on unseen data despite the
relatively small dataset.

                                              6
The calibration plots demonstrate that our Markov chain model is well-calibrated on the
training set. We quantify this with the R² of the binned points against the diagonal, which
is 0.974 in sample and 0.915 out of sample. The test set exhibits slight curvature, likely
attributable to its small sample size (only 26 games). The lower out-of-sample R² is also
partly a product of our binning choice: we used 10 bins for both train and test sets, for the
test it spreads its fewer observations thinly across bins and makes each bin’s observed win
rate noisier, deflating the R². Overall, the general adherence to the diagonal suggests that
the empirically derived transition probabilities are reliable estimates of the true underlying
probabilities, and that the Monte Carlo simulation propagates this uncertainty effectively
into the final win probability estimates.

8     Non-win probability analysis
8.1    Next Score and Expected Points
The model can be used to simulate from current game states in order to value the current
state and show the distribution of future events. Figure 2a shows given a team has possession
how changing the distance from the opponents goal line changes the likelihood of different
scoring events (simulated from 1,000 samples). Figure 2b shows the weighted sum of these
outcomes, leading to an expected points graph which matches Watts and Pipping-Gamón
(2026)’s expected points model well, with an asymmetric increase in expected points close
to the opposition goal line.

               (a) Next Score                                (b) Expected Points

                                          Figure 2

8.2    Final Score Margin
We can also analyze final scoring margins given a certain state, allowing you to answer
questions like "if my team is down by X points, what is the probability we win the game by
Y points". Figure 3a shows the final home score minus the final away score in a game given
that the home team is losing by 3 points in the middle of the first half. Figure 3b, shows
the exact same state except starting the simulation in the middle of the second half.

                                              7
(a) Final score margin given down 3 points in       (b) Final score margin given down 3 points in
the middle of the first half                        the middle of the second half

                                          Figure 3

The distribution of final margins is much wider when more time remains in the game. Con-
versely, as time runs out, the current score difference increasingly dominates, becoming the
most likely final margin.

9     Conclusion
We developed a Markov Chain model that constructs a transition matrix to estimate the
likelihood of moving between game states. Beyond simply modeling these transitions, this
approach allows teams to benchmark actual performance against expected outcomes, forecast
final results, and trace how a game’s trajectory unfolds over time.
More broadly, this framework offers a flexible, data-driven tool for in-game analysis that can
be extended and refined with more data. Similar NFL win probability models are constructed
using decades of previous games, where 32 teams each play at least 16 games in a season. Our
data set consists of one singular season with a total of 132 games. This changed the design of
our model with fewer time and scoring states; ideally, we would have many samples in very
granular buckets. It also increases the variability of estimates for transition or absorption
probabilities, with each observation potentially having a large amount of weight. Simply,
with more data the model would perform better. That being said, our model is reasonably
well calibrated and performs similarly to other win probability models.
In terms of future work, team strength is currently only implicit in the transition matrix,
since scoring probabilities are conditioned on the current score differential bucket. With
multiple seasons of data, researchers could stratify matrices by team strength or adjust
scoring transitions more explicitly using offensive/defensive parameters for each team. We
anticipate even better calibration once this has been accounted for.

9.1    Data
The dataset was obtained from a previously published study (Martinez-Arastey et al., 2025).

                                                8
References
Baldwin, B. (2021). Nfl win probability from scratch using xgboost in r. Open Source
  Football Blog.
Bukiet, B., Harold, E. R., and Palacios, J. L. (1997). A markov chain approach to baseball.
  Oper. Res., 45:14–23.
Goldner, K. (2012). A markov model of football: Using stochastic processes to model a
 football drive. Journal of Quantitative Analysis in Sports, 8(1):1–18.
Lock, D. and Nettleton, D. (2014). Using random forests to estimate win probability before
  each play of an nfl game. Journal of Quantitative Analysis in Sports, 10(2):197–205.
Martinez-Arastey, G., Datson, N., Smith, N., and Robins, M. (2025). Foundations of ex-
 pected points in rugby union: A methodological approach. Journal of Sports Analytics,
 11:1–14. Creative Commons Attribution 4.0 License.
Newton, P. K. and Aslam, K. (2009). Monte Carlo tennis: A stochastic Markov chain model.
  Journal of Quantitative Analysis in Sports, 5(3):1–44.
Romer, D. (2006). Do firms maximize? evidence from professional football. Journal of
  Political Economy, 114(2):340–365.
Watts, K. and Pipping-Gamón, J. (2026). Kicking for goal or touch? An expected points
 framework for penalty decisions in rugby union. Journal of Quantitative Analysis in Sports.
Yurko, R., Ventura, S., and Horowitz, M. (2019). nflWAR: a reproducible method for offen-
  sive player evaluation in football. Journal of Quantitative Analysis in Sports, 15(3):163–
  183.

                                             9
