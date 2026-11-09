# Pre-game paired-comparison modeling of professional League of Legends map outcomes

- arXiv: https://arxiv.org/abs/2609.08060
- Authors: Min-Ren Guan, Shen-Ning Tung

---

                                                       Pre-game paired-comparison modeling of professional
                                                               League of Legends map outcomes
                                                                          Min-Ren Guan∗                Shen-Ning Tung†

                                                                                       September 8, 2026
arXiv:2609.08060v1 [stat.AP] 7 Sep 2026




                                                                                             Abstract
                                                      We build and evaluate a pre-game win-probability forecaster for individual maps (“games”)
                                                  in professional League of Legends (LoL). The proposed model is a one-stage logistic regression
                                                  fit end-to-end on the win/loss log-loss: each team’s exponentially-weighted moving average of
                                                  past same-side results, a ridge-shrunk stable strength that is the maximum-a-posteriori estimate
                                                  of a logistic mixed model, and a first-pick draft covariate, natively calibrated out of sample
                                                  (walk-forward slope 0.995). It augments a purely dynamic Bradley–Terry specification with stable
                                                  team strengths. A second, independently built two-stage composite mixed model under restricted
                                                  maximum likelihood (REML) and best linear unbiased prediction (BLUP) shrinkage, with Platt
                                                  calibration, serves as the strongest rival the authors could build. On 5,135 games across six
                                                  regional leagues and three international events (2024–2026), under paired per-game Diebold–
                                                  Mariano inference, the two architectures are statistically indistinguishable on every protocol and
                                                  window (global holdout 0.2230 vs. 0.2257; walk-forward 0.2207 vs. 0.2215), so the simpler model is
                                                  preferred on parsimony, not accuracy; both improve on the classical dynamic benchmark (0.2351)
                                                  by a clear margin and on the static fits (0.2301/0.2268) more modestly. Against Polymarket
                                                  on 928 matched maps, the forecasts are statistically indistinguishable from the market on its
                                                  own per-game contracts, with a modest market edge concentrated on cross-region Worlds and
                                                  series-decider maps.

                                          Keywords: Bradley–Terry model; Gaussian linear mixed model; ranked probability score; esports
                                          forecasting; prediction markets; exponentially weighted moving average.



                                          1       Introduction
                                          Competitive esports has, over the past decade, matured into a data-rich analogue of the professional
                                          sports leagues that have long been the primary subject matter of quantitative sports analysis.
                                          Matches are scheduled, officiated, and broadcast under standardized formats; outcomes are recorded
                                          unambiguously; and, increasingly, liquid prediction markets price the same contests, offering a
                                          natural external forecasting benchmark against which a statistical forecaster can be judged rather
                                          than merely described. League of Legends (LoL) is among the most heavily professionalized and
                                          extensively documented of these titles, contested in regional leagues across China (LPL), Korea
                                          (LCK), Europe (LEC), North America (LCS), the Asia-Pacific (LCP), and Brazil (CBLOL), together
                                          with recurring international championships (Worlds, the Mid-Season Invitational, and the First
                                              ∗
                                              Teahouse Finance, Taipei 105803, Taiwan. E-mail: john@teahouse.finance.
                                              †
                                              Corresponding author. Department of Mathematics, National Tsing Hua University, No. 101, Sec. 2, Guangfu
                                          Rd., Hsinchu 300044, Taiwan. E-mail: tung@math.nthu.edu.tw. ORCID: 0000-0002-4646-3575.


                                                                                                  1
Stand event). A professional match consists of one or more maps—individual games, each ending
in a clean win or loss—most commonly contested as a best-of-three (Bo3), the series awarded
to the first team to win two maps. Before each map begins, the two teams alternate selecting
and banning playable characters in a structured draft; the team granted the first selection in that
phase holds first-pick rights, a schedule-assigned draft-order covariate rather than a fixed property
of either team. This combination—a well-defined binary outcome at the map level, a large and
continually refreshed multi-league corpus, and a liquid prediction market pricing many of the same
contests—makes professional LoL an unusually tractable domain for dynamic paired-comparison
forecasting, and one on which the present paper’s results can be checked against an external
forecasting benchmark rather than against in-sample fit statistics alone.
    Quantitative work specific to esports win prediction remains comparatively young next to the
century-old paired-comparison literature it draws on, and has so far concentrated on two distinct
problems: forecasting from rich in-game or player-level features, and forecasting from the pre-
game information available before a single character is played. Maymin (2021) develops kill- and
death-level analytics for LoL that connect individual in-game events to win probability, establishing
that the game’s telemetry carries exploitable predictive signal well beyond the final score. Hodge
et al. (2021) build a live, in-game win-prediction system evaluated on professional Dota 2 and
Counter-Strike matches, demonstrating that continuously updated in-play features substantially
outperform static pre-match priors as a contest unfolds—a live-model problem the present paper
deliberately does not address, restricting itself throughout to information available before the map
begins. Closest in spirit to the present exercise, Jadowski and Cunningham (2022) fit statistical
classifiers to metrics gathered from professional LoL’s 2020 international competitions, their best
specification correctly calling 67% of the 306 games evaluated; their study, however, neither adopts
a dynamic paired-comparison architecture nor benchmarks against a prediction market, leaving
both as open contributions this paper takes up directly. Read together, this literature motivates
evaluating pre-game forecasts as a question worth answering in its own right, distinct from the
in-game prediction problem, while leaving unresolved how much modeling complexity that pre-game
forecasting task actually requires and how the resulting forecasts compare with the market’s own
pricing—the two questions this paper is built to answer.
    Three research questions organize the analysis. First, does a deliberately minimal one-stage
logistic model—four fixed coefficients plus a ridge-shrunk team-strength block, fit end-to-end on the
forecasting loss it is judged by—concede anything in held-out accuracy to the most competitive two-
stage composite mixed model that can reasonably be built for this domain, one given every design
advantage precisely so that a tie against it is a meaningful result rather than a beaten straw man?
Second, do either of these two architectures improve on the classical paired-comparison benchmarks
against which any new dynamic model should be measured—Cattelan, Varin, and Firth’s purely
dynamic Bradley–Terry model and a static, Stefani-style least-squares fit? Third, does the resulting
pre-game forecaster price individual maps as accurately as Polymarket, a liquid prediction market
pricing contracts on the same games? The answers organize the paper’s contribution around parity
and parsimony: the two architectures prove statistically indistinguishable on every protocol and
window examined, so the case for the simpler model rests on its needing no composite response and
no post-hoc calibration step.
    The paper’s models sit in a direct methodological lineage. Stefani (1977) and Harville (1977b)
established static paired-comparison rating from margins of victory, assigning each competitor
a fixed strength recovered by least squares; such models cannot represent within-season form, a
limitation acute in a domain where rosters change between splits and the underlying game itself is
periodically rebalanced by a patch, a scheduled software update to character and item statistics.
Cattelan, Varin, and Firth (2013) resolved the static model’s chief limitation with a purely dynamic

                                                 2
Bradley–Terry model in which team ability follows an autoregressive, exponentially-weighted process
driven entirely by past results and carries no stable per-team component of its own, continuing a
state-space paired-comparison tradition developed by Barry and Hartigan (1993), Glickman (1999),
and Fahrmeir and Tutz (1994) that this paper does not otherwise draw on directly. A separate
line, following the same dynamic idea but replacing the binary outcome with a continuous score or
margin composite under a linear mixed model, was developed by Guan (2020) in an unpublished
master’s thesis, worked there on professional basketball; the present paper is, to our knowledge,
the first peer-reviewed application of that continuous-response, two-stage paired-comparison design
to esports—a domain the line had not previously reached—and carries it forward as the second
candidate model of §2.3. Against this lineage, the paper’s own contributions are four: a one-stage
model that completes Cattelan, Varin, and Firth’s purely dynamic Bradley–Terry with the stable
team strength it structurally lacks, in a single estimation pass rather than two, established here
as exactly the maximum-a-posteriori solution of a logistic mixed model under a ridge penalty—an
equivalence that is this paper’s own construction rather than one carried from either source; a
first-pick covariate specific to LoL’s draft structure; a benchmark against Polymarket under a leakage-
proof, id-keyed backtest design (§5.5); and, as a smaller, secondary finding rather than a headline
result, a demonstration that the one-stage model’s ridge-shrunk strengths remain identifiable on
thin single-league schedules where the classical random-effect fits become singular.
     The remainder of the paper proceeds in the order the model itself motivates. Section 2 specifies
the paired-comparison lineage, the proposed one-stage model, and the second candidate two-stage
model, establishing the target quantity—the pre-game win probability pbi —before any data are
described. Section 3 describes the three data sources feeding the corpus, the resulting scope and
the source properties that shape the ingestion rules, and the two complementary holdout protocols
used throughout. Section 4 defines the ranked probability score and its exact reduction to the Brier
score for a two-outcome per-map market, together with the paired standard error appropriate to
every reported comparison. Section 5 reports the results, moving from the classical benchmarks
through the one-stage/two-stage architecture comparison and its ablations to the market benchmark.
Section 6 concludes.


2     Model
The quantity this paper delivers and scores throughout is the pre-game win probability pbi for map
i’s per-map market: every specification decision below is judged by held-out forecast loss (§4) and,
ultimately, against the market itself (§5.5). Two models are proposed. The proposed model
(§2.2) is a one-stage outcome logistic—the minimal paired-comparison forecaster, fit end-to-end on
the deliverable it is judged by. The second candidate model (§2.3) instantiates the classical
two-stage rating tradition in full, for the reasons set out there. Both are validated against each other
and against two classical external benchmarks, dynamic and static (§5.2). Cross-region pooling is
used throughout, and no patch fixed effect is fit, for reasons given below and in §3. Throughout,
map i is played between blue-side team b(i) and red-side team r(i) on patch p(i) at calendar time
ti ; Oi ∈ {0, 1} is the blue-side win indicator, and Yi denotes a blue-perspective margin response
wherever a layer of the road map below uses one.

2.1    Road map: the paired-comparison lineage
The modeling landscape is best read as a short lineage, each step adding one piece of structure and
answering one question that the previous step left open. The two layers this paper builds on most
directly are stated in full below rather than merely cited; the two-stage line that historically follows

                                                   3
is summarized at the end of the road map, and its strongest instantiation is carried forward as the
second candidate model (§2.3).
    Layer 1: static paired comparison. The base layer treats the score difference of a contest as
a difference of latent, time-invariant team strengths. Stefani (1977) assigns one least-squares rating
per team, fit to win margins with the average rating fixed at a reference value as his identification
constraint—leaving T − 1 free ratings for T teams—and with no home-advantage term at all, an
omission he reports cost accuracy, the next margin predicted from the rating difference. The
blue/red asymmetry of the present domain makes a side-specific pair the natural adaptation of
that design: writing aB                                           R
                        b(i) for the blue team’s strength and ar(i) for the red team’s, the least-squares
model fitted here is                                                         
                                Yi = aB b(i) − a R
                                                 r(i) + ε i , εi ∼ N   0, σ 2
                                                                                .                     (1)
This side-specific design carries exactly one redundancy—shifting both blocks of strengths by a
common constant leaves every prediction unchanged—so that 2(T − 1) relative strengths together
with a single blue−red level remain identifiable, that level playing precisely the side-advantage
role Stefani’s original omits. Equation (1) is otherwise the long-established standard for paired-
comparison sports rating on a continuous margin: abilities fit by least squares, with the next margin
predicted from the strength gap. Harville (1977b) gives the same idea its mixed-model form, with
teams entering as random effects fitted to score margins and the strengths permitted to drift between
seasons through a first-order autoregression—an early formal treatment of time-varying strength
that predates the state-space paired-comparison line discussed below. What a static layer of this
kind buys is a coherent, transitive strength ranking, and, as §5.2 shows on this corpus, more held-out
accuracy than the purely dynamic Layer 2 that follows it; what it cannot answer is anything about
within-season form, since a team’s strength is a single number for the whole sample—Harville’s
autoregression moves it between seasons, not within them—so a mid-season hot or cold streak is
invisible to it.
    Layer 2: canonical dynamic Bradley–Terry. The second layer makes ability move within
the season but discards stable strength entirely. The Bradley–Terry model of Bradley and Terry
(1952) predicts a pairwise win from the difference of two latent team strengths, the same difference-
of-strengths logic that Elo (1978) put to practical use in chess rating by updating each player’s
strength after every result, and the state-space treatments of time-varying ability cited in §1 filter
those strengths from observed results. Cattelan, Varin, and Firth (2013) replace this state-space
machinery with a designed covariate: they model the binary outcome Oi ∈ {0, 1} with a logistic
link and let each team’s ability be purely dynamic—a running form score updated after every game
by an exponentially-weighted moving average (EWMA) of its own past results, with no underlying
                                             B (t ) for the blue team’s purely dynamic same-side win
time-invariant component at all. Writing Sb(i)   i
form entering map i, and t− for the time of team b(i)’s previous blue-side game, the form evolves
by the EWMA recursion, with blue-side smoothing parameter λ1 ∈ [0, 1],
                              B
                             Sb(i)                    B
                                   (ti ) = (1 − λ1 ) Sb(i) (t− ) + λ1 O(t− ),                        (2)

where O(t− ) ∈ {0, 1} is the blue-perspective outcome of that previous blue-side game—team b(i)
played blue there, so it is exactly its own win indicator—and the sequence is initialized at the
league-wide mean blue-side win rate of the previous season, common to all teams. The red-side
form updates symmetrically from team r(i)’s previous red-side game at t′− , whose win indicator for
the red team is 1 − O(t′− ), with its own smoothing parameter λ2 :
                           R                       R
                                                        (t′− ) + λ2 1 − O(t′− ) .
                                                                                
                          Sr(i) (ti ) = (1 − λ2 ) Sr(i)                                              (3)


                                                    4
There is no stable component in this layer; the form is the ability. The win probability is the logistic
transform of the contemporaneous form gap,
                                                       B (t ) − γ S R (t )
                                                   
                                               exp γ1 Sb(i) i    2 r(i) i
                           Pr(Oi = 1) =                 B (t ) − γ S R (t )
                                                                                  .                       (4)
                                             1 + exp γ1 Sb(i) i    2 r(i) i

In words, the probability that blue wins map i rises with blue’s own recent same-side form and falls
with red’s, on a logistic scale, and with no additive contribution from either team’s identity beyond
that recent record. The side-specific scales γ1 , γ2 are estimated by conditional likelihood rather
than fixed a priori, and teams are initialized at a common prior-season average. One estimation
convention, however, belongs to this paper and not to its source: Cattelan, Varin, and Firth (2013)
treat the decays as estimated parameters—per-side nuisance smoothing parameters (λ1 , λ2 ), fit by
two-step maximum profile likelihood, with λ   b 1 = 0.043 and λ
                                                              b 2 = 0.025 in their National Basketball
Association application, four free parameters in all—whereas throughout the present paper every
decay is a designed, grid-selected covariate, never estimated by the likelihood (§2.4). What this layer
buys is responsiveness to recent form, the headline strength of the dynamic Bradley–Terry family;
what it gives up is a persistent identity for each team, since two clubs with identical recent records
are statistically indistinguishable to it even if one has been the stronger roster all year. Whether
that omission costs anything in forecast accuracy is an empirical question, answered in §5.2.
    One point is worth stating explicitly: Layers 1 and 2 are not boundary cases of one another.
Freezing the decays at λ1 = λ2 = 0 in (2)–(3) does not recover per-team static strengths—it yields an
intercept-only model, since Cattelan, Varin, and Firth’s EWMA has no per-team stable component
at any decay. Both layers are instead boundary cases of the second candidate model developed
in §2.3. The two-stage tradition that historically follows Layer 2 (§1) survives here as the second
candidate model of §2.3.

2.2   The one-stage family and the proposed model
The model this paper proposes is the minimal member of a one-stage family, fit end-to-end on the
deliverable, that completes the road map’s Layer 2 with the stable strength it lacks. A member
of the family is indexed by the dimension d of the game summary its latent update consumes.
Summarize each finished game, from the perspective of the side that played it, by a feature vector
x ∈ Rd —directional own-minus-opponent quantities, sign-flipped for red, with game duration (the
one undirected feature in the pool) entering unsigned—and let each team carry side-specific form
states E B , E R ∈ Rd , the coordinate-wise vector analogue of the Layer-2 recursion (2): with t− the
time of team b(i)’s previous blue-side game and x(t− ) that game’s summary from its perspective,
                       B
                      Eb(i)                  B
                            (ti ) = (1 − λ) Eb(i) (t− ) + λ x(t− ),        B
                                                                          Eb(i) (0) = 0,                  (5)

zero-initialized at a team’s competitive debut, with decay λ selected on a grid; the red-side analogue
            R from team r(i)’s previous red-side game in the same way. In words, (5) tracks each
updates Er(i)
team’s recent form separately for the side it played on, weighting its most recent games most heavily
and discounting older ones geometrically, exactly as (2) does for the scalar win indicator but now
for a general d-dimensional game summary. The win probability is a single logistic expression,
                                                       ⊤ B              ⊤ R                          
        pi = expit β0 + γFP 1[blue is first-picki ] + βB Eb(i) (ti ) − βR Er(i) (ti ) + θb(i) − θr(i) ,   (6)

where expit(x) = ex /(1 + ex ), with side slope vectors βB , βR ∈ Rd and one stable strength θt per
team. Three glosses on (6) matter for what follows. First pick is professional LoL’s draft-order

                                                       5
covariate: one team is assigned the first selection in the pre-game pick/ban phase, in which teams
choose the champions—the playable characters—each of their players will use, an assignment made
by the schedule rather than a property of the team, which is why it enters as its own game-level
covariate rather than being folded into θ. And each side’s form state consumes only that side’s own
games—a team’s red-side results never update its blue-side form; the split is inherited from Layer 2,
where it carries a real asymmetry that the model’s intercepts absorb, and is kept throughout for
comparability across every model in the road map. Pooling both sides into a single state was not
tried; the variants for which it would matter most, d = 4, 10, are the ones §5.3 rejects on accuracy
grounds regardless. Finally, the features entering (5) are normalized on training rows alone (§3.4),
with the directional margins scaled by their training-window standard deviations but deliberately
not centered—centering would destroy the within-game antisymmetry xteam = −xopponent that
the sign-flipped construction guarantees—while game duration, having no direction to preserve,
is fully standardized to zero mean and unit variance, and the win indicator is already coded on
the symmetric ±1 scale. Because the slope vectors βB , βR are left unpenalized, the fitted model is
invariant to any per-feature rescaling of this kind: the normalization conditions the optimization
and renders the learned weights comparable across features, which is what the coefficient diagnostics
of §5.3 rely on, and it settles directly whether the feature-count ablation reported there depends on
the scaling choice, since provably it cannot.
    The proposed model is the minimal member of the family, d = 1: the game summary is the
signed result x = 2O(t− ) − 1 ∈ {±1} alone, so Eb(i)
                                                   B (t ) is simply team b(i)’s EWMA of its own past
                                                        i
blue-side results, and (6) specializes to the scalar-slope expression
                                                          B                R                            
        pi = expit β0 + γFP 1[blue is first-picki ] + βB Eb(i) (ti ) − βR Er(i) (ti ) + θb(i) − θr(i)       (7)

—four coefficients plus the shrunk team block. Put plainly, (7) is a logistic regression that prevents
over-fitting by shrinking each team’s rating toward the league average, using a team’s recent
momentum—weighted toward its most recent games on the same side—and a schedule-assigned
first-pick indicator. The larger members of the family (d = 4: the signed result plus the second
candidate model’s three margins; d = 10: every end-of-game feature considered) are fit under an
identical protocol in §5.3, and the resulting d-ablation there is what fixes the proposal at d = 1
rather than at a richer specification.
    Every member of the family is estimated in a single pass by minimizing the penalized log-loss
                               X                                                τ
                                                                                   ∥θ∥2 ,
                                                                         
                           −        Oi log pi + (1 − Oi ) log(1 − pi )       +                              (8)
                               i
                                                                                 2

where θ stacks the stable per-team strengths of (6) into one vector and ∥θ∥2 = t θt2 is its squared
                                                                                            P

Euclidean norm, so the penalty is simply the sum of squared team strengths, one term per team;
the regression coefficients (β0 , γFP , βB , βR )—2 + 2d numbers, four for the proposed member—are
left unpenalized. The ridge term in (8) is not a tuning afterthought but the source of the model’s
principal methodological claim: (8) is exactly the maximum-a-posteriori           (MAP) estimate of
                                                                  2
                                                                    
a logistic generalized linear mixed model with θt ∼ N 0, σθ , since the negative log-posterior
is the Bernoulli log-loss plus the prior’s t θt2 /(2σθ2 ) term, which coincides with (8) under the
                                                P

correspondence τ ↔ 1/σθ2 (the Bernoulli dispersion being fixed at one, the strength-variance ratio
of the Gaussian case reduces to 1/σθ2 alone). This equivalence is this paper’s own construction
rather than one carried from Cattelan, Varin, and Firth (2013) or Guan (2020), and it means τ
plays exactly the role the strength-variance ratio plays in the second candidate model’s best linear
unbiased prediction (BLUP) shrinkage (§2.3); a team unseen in training receives θb = 0, the prior
mean, under both models. The two tuning constants entering (5) and (8) are different kinds of

                                                       6
knob: λ is a covariate-construction parameter that never enters the loss directly, with each grid
value rebuilding the columns E B , E R from scratch, while τ is the penalty weight inside the loss
itself. Both are selected jointly by a grid search on training data alone (§3.4); at fixed λ the fit is
convex and converges within seconds under L-BFGS, so the outer grid is inexpensive to run in full.
The result proves insensitive to the selection along both dimensions: the criterion surface is flat in
both λ and τ (§5.4).
    Two statements place the proposed model within the road map. In mixed-model terms it is the
logistic analogue of the second candidate model of (9), estimated at its maximum a posteriori rather
than by REML and BLUP; §5.2 prices the completion of Layer 2 at 0.0112 walk-forward Brier
over the purely dynamic benchmark. In design terms it is deliberately minimal, because the latent
update consumes only the binary result: adding richer end-game features degrades held-out accuracy
monotonically in feature count (the d-ablation of §5.3), because those features are near-collinear
measurements of one underlying dominance that the binary result already carries.

2.3   The two-stage candidate model
The paper’s second model is also original to this study: the strongest instantiation the authors could
build of the classical two-stage paradigm, in which score-difference models regress a continuous
margin on team strengths and the win probability is recovered only afterward (Guan, 2020; Harville,
1977b; Stefani, 1977). It enters the analysis as the second candidate model: “benchmark” is reserved
throughout for the external references—the classical fits of §5.2 and the market (§5.5)—since this
model was built by the same authors under the same design choices as the proposal. The distinction
is not merely terminological, because the parity claim of §5.3 is credible only if the system compared
against is the strongest the paradigm offers; it was therefore matched to the one-stage model at
every point where a design choice could favor either—the same EWMA form design and decay grid,
the same data, the same evaluation protocols.
    The second candidate model’s response is a z-standardized composite of the game outcome and
three end-of-game margins,

                                                   ∆gi        ∆ki        ∆Ti
                            Yi = 0.50 Oi + 0.25        + 0.15     + 0.10     ,
                                                   σg         σk         σT

built from the blue-minus-red differences in gold, kills, and towers at the end of the map, with
weights fixed a priori rather than estimated; §5.4 shows that held-out accuracy is identical to four
decimal places across every dense re-weighting tried, a consequence of the three margins being
near-collinear measurements of the same underlying dominance. Put plainly, this composite is a
standard sports rating system that scores winning margins and adjusts each team’s rating by how
much data that team has accumulated. The model itself is a Gaussian linear mixed model with one
stable random strength per team and side-specific form terms of the same design as the proposed
model’s,
                                                                      B                R
           Yi = α + γFP 1[blue is first-picki ] + θb(i) − θr(i) + γ1 Sb(i) (ti ) − γ2 Sr(i) (ti ) + εi   (9)

In words, the composite margin of map i is the sum of a global intercept, a first-pick adjustment,
the difference between the two teams’ stable strengths, and a contribution from each side’s recent
same-side form, about   which the observed margin varies with Gaussian noise. Here θt ∼ N 0, σθ2
and εi ∼ N 0, σ 2 , and S B , S R follow the same-side win-indicator recursion of (2)–(3), with per-side
                 

decays fixed a priori at λ1 = λ2 = 0.3, drawn from the same grid the proposed model selects over
and justified in §5.4 by a flat criterion surface. The candidate’s S B , S R differ from the Layer-2


                                                       7
restatement of §2.1 in one respect: rather than being initialized at the league-wide prior-season mean,
they are zero-initialized at each team’s debut, matching the convention adopted for the one-stage
family’s E B , E R in (5) and kept here for comparability between the two candidate architectures. The
variance components are estimated by restricted maximum likelihood (Harville, 1977a; Patterson
and Thompson, 1971); the team strengths are predicted by their best linear unbiased predictors
(Henderson, 1975), shrunk by the reliability weight κt = σ bθ2 /(σ
                                                                 bθ2 + σ
                                                                       b 2 /nt ) toward zero, so that a team
unseen in training receives θb = 0—the same fallback the proposed model’s ridge penalty supplies, its
correspondence τ ↔ 1/σθ2 making it this machinery’s one-stage analogue. The win probability itself
is recovered only in a second step, by a Platt map pbi = expit(c0 + c1 Ybi ) (Platt, 1999) fit on the
training predictions—a calibration step the proposed model, being fit end-to-end on the win/loss
log-loss directly, requires nowhere in its own pipeline (§3.4).
    The specification of (9) nests the road map’s first two layers as boundary cases rather than as
separate competitors. Setting the form coefficients to zero (γ1 = γ2 = 0, equivalently the decays
λ1 = λ2 = 0, which pin the candidate’s zero-initialized S B , S R at zero) collapses (9) to the static
strength-difference model of Layer 1—(1) on the composite response, in the random-effects form of
Harville (1977b), with the intercept and first-pick terms retained. Setting the strength variance to
zero instead (σθ2 = 0, so every BLUP shrinks entirely to the prior mean of zero) yields the Layer-2
dynamic form structure, carrying the linear predictor of (4) on the margin response rather than
the binary outcome, but with the candidate’s zero-initialization convention for S B , S R in place of
Layer 2’s league-mean initialization, so the boundary is exact in structure rather than in every
estimated value. Both boundaries are priced on the holdout in §5.2: the static one exactly, at
0.2268 (BLUP-shrunk) against 0.2301 for the least-squares Stefani fit; the dynamic one in its own
logistic form, at 0.2351. The proposed model nests the same two boundaries on the logistic side,
with τ → ∞ forcing θ ≡ 0 and recovering (4) up to the first-pick term, and βB = βR = 0 leaving
the static ridge-shrunk strength model alone.
    Fixed-strength and random-form-coefficient variants of (9)—the cross-classified cases of Guan
(2020)—were also fit; none outperformed the single-strength model above, so (9) serves as the
family’s representative throughout. Put simply, the two shrinkage devices are the same prior, as
§2.2 establishes, so neither can be unstable where the other is stable; what separates them on
sparse, single-league schedules is how the prior’s variance is chosen and what else each pipeline
carries. Estimating σθ2 inside the likelihood, as the classical machinery does, is fragile at these
sample sizes—the variance-component surface is flat and boundary-prone, yielding singular fits in
the cross-classified variants and strength estimates sensitive to which basin a refit lands in—and the
separate calibration map inherits a small-sample instability of its own, whereas fixing the penalty τ
by grid selection keeps every fit strictly convex and identifiable on any slice, with no calibration
step to destabilize. The expansion league LCP is the running illustration in §5.1. This robustness
point is secondary to the paper’s central argument for the design. The second candidate model is
compared against the proposed model in §5.3 and against the market in §5.5.

2.4    Model summary
Table 1 collects, for every model in the road map, the response modeled, the parameters estimated,
and the tuning constants set on training data—whether swept over a grid or fixed a priori—rather
than estimated by the likelihood, so that shrunk team blocks are never mistaken for free parameters.




                                                     8
Table 1: Model summary across the paired-comparison road map: response actually modeled,
parameters actually estimated, and hyperparameters that are “grid-designed,” meaning selected
or fixed on training data and never estimated by the likelihood. T is the number of teams (≈ 80,
cross-region pooled). Best linear unbiased predictions and ridge-MAP team blocks are predictions
under a prior, not free parameters. The Layer-1 row counts the side-specific adaptation fitted here
(§2.1); Stefani’s (1977) original assigns one rating per team, T − 1 of them free with the average
fixed. The Layer-2 row counts Cattelan, Varin, and Firth’s (2013) own specification, in which the
per-side decays are estimated by profile likelihood rather than designed; the re-implementation of
§5.2 instead sweeps a single shared λ on this paper’s grid.
 Model                                        Response                     Estimated parameters                          Grid-designed
                                                                                                                 2
 Layer 1 (Stefani, 1977)                      margin Yi                    2(T −1) strengths + side level + σ            —
 Layer 2 (Cattelan, Varin, and Firth, 2013)   binary Oi (logistic)         γ1 , γ2 , λ1 , λ2 (4; decays by profile ML)   —
 Two-stage candidate (9)                      score composite (Gaussian)   6 (REML) + Platt (c0 , c1 )                   λ1 , λ2
 Cattelan re-implementation (§5.2)            binary Oi (logistic)         β0 , γ1 , γ2 (3)                              λ
 Proposed (7), d=1                            binary Oi (logistic)         β0 , γFP , βB , βR (4); ridge θ               (λ, τ )
 One-stage family (6), general d              binary Oi (logistic)         2 + 2d slopes; ridge θ block                  (λ, τ )



3     Data
3.1      Sources
The modeling corpus is assembled from three providers that share no common join key and must
therefore be reconciled by team, date, and patch rather than by a single identifier. lolesports
broadcast telemetry supplies the match schedule, per-game metadata, and team state recorded
at a ten-second cadence—gold, kills, and the map’s contested objectives: dragons and barons,
neutral monsters whose defeat confers team-wide combat bonuses, and towers and inhibitors, the
defensive structures whose destruction opens a path into the opposing base—and is the source of
both the binary outcome Oi and the end-of-game margins entering the second candidate model’s
composite response (§2.3); its endpoints are unofficial, and this paper follows the community API
documentation at github.com/jpteixeira99/lol-esports-api (last accessed 24 August 2026).
Leaguepedia, a MediaWiki Cargo database, supplies patch identifiers, rosters, and the first-pick
assignment recorded for each draft, and is the sole source of the first-pick covariate used throughout;
games without a populated first-pick assignment are excluded from every analysis in this paper
rather than imputed, for reasons given in §3.2 below. Polymarket, a prediction-market API,
supplies per-map binary “Game N winner” contract prices and is used only as an external forecasting
benchmark in §5.5; it plays no role in fitting any model reported elsewhere in this paper.

3.2      Volumes and scope
The corpus comprises 5,893 collected games, of which 5,135 join a populated first-pick assignment and
form the modeling corpus used throughout the remainder of the paper: six regional leagues—LCK,
LPL, LEC, LCS, LCP, and CBLOL—together with three international events—First Stand, the
Mid-Season Invitational, and Worlds—spanning roughly 80 teams and 80 patches over 2024–2026
(counts as of July 2026). Table 2 gives the per-league composition of the modeling corpus. The
758 collected games that do not join a first-pick assignment—mostly 2026 schedule slots recorded
ahead of their leagues’ season starts—are excluded outright rather than imputed: no imputation
scheme for a missing draft-order assignment was judged reliable enough to substitute for the genuine
covariate, and excluding these rows costs under 13% of the collected corpus while leaving every
retained game’s first-pick indicator exact rather than estimated.

                                                                 9
Table 2: Modeling-corpus game counts by league bucket (first-pick-complete games, n = 5,135; July
2026).
                               League   Games     League        Games
                               LPL        1,822   CBLOL           277
                               LCK        1,276   LCS             216
                               LEC          697   Worlds          190
                               LCP          432   MSI             157
                                                  First Stand      68


    Two properties of the sources shape the ingestion rules this corpus is built under, and both
are stated here because a replicator needs them. The lolesports schedule endpoint is paginated,
returning results in pages of roughly eighty events, and must therefore be paged exhaustively:
an unpaginated pull silently truncates the corpus rather than failing visibly, and the truncation
falls unevenly across leagues, since the affected query windows differ from one league to another,
leaving a matchup graph sparser than the true schedule and team-strength estimates correspondingly
poorly conditioned—so the defect first presents as an apparently statistical problem rather than
as an ingestion error. And for some leagues the recorded game timestamp marks the game’s end
rather than its start, a provider-side convention that varies by league and is documented nowhere
in the community API reference, so every pre-game quantity in this study—most critically the
market quotes of §5.5—is anchored instead to the first telemetry frame’s own timestamp, which
is unambiguous about when a game actually began; anchoring to the recorded timestamp would
sample settled prices and produce spuriously perfect market scores. Both rules are load-bearing for
every result reported in §5.

3.3   Evaluation protocol
Two complementary holdout protocols are reported for every model in this paper, rather than a
single design contrasted against an alternative. The global time-based split trains on the oldest
80% of games by calendar time and tests on the most recent 20%—a single, conservative split whose
test window sits entirely after the roster turnover and patch drift the training window predates, so
that every static quantity a model estimates is fixed before the test window begins and applied only
after it. The per-game walk-forward instead refits at every scored game on all games strictly
prior to it in calendar time, subject to a minimum training size of 500 games, and scores 4,605
games in total; this is both the cadence a production deployment of either model would actually
run under and the protocol the market comparison of §5.5 inherits, since a market price is itself set
before each map is played. Ordinary random cross-validation is invalid in this setting and is used
nowhere in this paper: the exponentially-weighted form covariates central to every dynamic model
here (§2) depend on a team’s strictly prior games, so a random fold would let future games leak into
the very training window used to construct a test game’s own features. This subsection specifies
what is compared under each protocol; the sequence of operations a fit actually executes—feature
construction, hyper-parameter selection, refit cadence, and calibration timing—is the workflow
specified next.

3.4   Training and estimation workflow
The proposed and second candidate models are specified in §2.2 and §2.3; this subsection specifies
the sequence of operations a fit of either model runs under either protocol of §3.3, kept here as a


                                                  10
data-processing and estimation question distinct from the mathematical model definitions themselves.
One asymmetry between the two models is a design choice stated here up front rather than left
for the reader to discover in the results: the proposed model carries a grid-selection step and no
calibration step, while the second candidate model carries the reverse.
     Feature construction. Given a training window and a decay (λ for the proposed family;
per-side λ1 , λ2 for the second candidate model), the window is walked chronologically and the form
states of §2.2 and §2.3—the signed-input E states and the win-indicator S states, respectively—are
accumulated from each team’s debut, zero-initialized as specified in §2; every game’s covariate value
is its team’s form state strictly before that game is played, so no game’s own outcome ever enters
its own feature. Feature-scaling constants—the second candidate model’s margin z-scales—are
likewise computed from training rows only; the residual and strength variance components are not
precomputed here but estimated within the REML fit itself, as described next.
     Hyper-parameter selection (proposed model only). The pair (λ, τ ) is selected once per
protocol by an inner chronological split of the training data alone: at each grid pair, the model is
fit on the first 75% of the training window and scored by log-loss on the remaining 25%, and the
argmin over the grid is kept. On the global split this inner window is the full training set; under
the walk-forward it is the first 500 games, and the winning pair—together with the feature-scaling
constants computed from that same window in the previous step—is then frozen for the remainder
of the pass, so that no game the walk-forward ultimately scores ever enters its own hyper-parameter
selection. §5.4 shows the result is insensitive to this choice across a wide grid. The second candidate
model carries no analogous selection step: its decays are fixed a priori at λ1 = λ2 = 0.3, a choice
justified in §5.4 by a flat criterion surface rather than by a grid search, and its strength-variance
shrinkage self-tunes within each fit by restricted maximum likelihood.
     Fit. The proposed family is estimated by a single convex L-BFGS minimization of the penalized
log-loss (8) on the training window. The second candidate model is estimated by a restricted-
maximum-likelihood fit of (9), with team strengths recovered as best linear unbiased predictors.
     Calibration (second candidate model only). A Platt map is fit on the training window’s
own predictions—in-sample by design, with no out-of-fold split—and applied to the held-out games
that follow. The proposed family requires no analogous step: its probabilities are the direct output
of the logistic fit itself, having been fit end-to-end on the win/loss log-loss it is ultimately judged by.
     Refit cadence. Under the global split, feature construction, the fit, and calibration each run
once. Under the walk-forward, all three rerun at every scored game on all games strictly prior
to it (subject to the 500-game minimum), while hyper-parameter selection does not rerun. The
calibration asymmetry between the two models is therefore a matter of in-sample versus out-of-fold
estimation, not of once-versus-per-step timing: the second candidate model’s Platt map is in fact
refit at every walk-forward step, just always on the same rows the mixed model itself was fit on at
that step. §5.3 quantifies the out-of-fold alternative directly, recovering most though not all of the
resulting gap (0.2257 → 0.2248).
     Computational tools. The data-ingestion, estimation, backtesting, and figure-generating code
supporting this study was written with the assistance of a large language model (Anthropic’s
Claude), used to draft and refactor implementation code that the authors then reviewed, tested
against the protocols specified above, and take full responsibility for; the same tool was used to
polish the manuscript’s prose. No modeling decision, no reported result, and no interpretation in
this paper was delegated to it, and every number reported below was regenerated from the authors’
own pipeline runs.
     Research ethics and informed consent. This study analyzes only publicly available
professional match records and publicly quoted market prices; it involves no human or animal
subjects and no personally identifying data, so no ethical approval was required. Research ethics:

                                                    11
Not applicable. Informed consent: Not applicable.


4     Scoring: the ranked probability score and its reduction to the
      Brier score
JQAS forecasting papers are conventionally scored by the ranked probability score (RPS),
introduced by Epstein (1969) and established as the standard metric for sports-forecast evaluation
in this journal by Constantinou and Fenton (2012). The RPS is a strictly proper scoring rule for
ordered-categorical outcomes (Gneiting and Raftery, 2007), meaning a forecaster minimizes its
expected value only by reporting its true beliefs, with no incentive to hedge toward or away from
any particular category. For a single forecast over r ordered categories with predicted probabilities
p1 , . . . , pr and one-hot outcome indicators e1 , . . . , er ,

                                            1 r−1
                                                X P
                                                    i        Pi     2
                                RPS =               j=1 pj −  j=1 ej .                                    (10)
                                          r − 1 i=1

In words, (10) accumulates the predicted and realized probability mass up to each ordinal cutoff and
penalizes the squared gap between them, so that a forecast placing most of its mass one category
away from the true outcome is penalized less than one placing its mass on the opposite end of the
ordering—a distinction that matters for genuinely ordered outcomes but collapses, as shown next,
for the two-outcome market this paper models throughout.

4.1    Reduction to the Brier score for the per-map market
The per-map “Game N winner” contract has r = 2 outcomes—blue win or red win—with no ordinal
structure to distinguish beyond the two categories themselves. Setting category 1 = “blue win” with
p1 = pb and e1 = O ∈ {0, 1}, (10) collapses to a single term,
                                         1
                             RPS =          (p1 − e1 )2 = (pb − O)2 = BS,                                 (11)
                                        2−1
the ordinary (single-component) Brier score. Averaged over a holdout set, RPS = BS = N1 i (pbi −
                                                                                                     P

Oi )2 , with 0 the optimal score and 0.25 the uninformative baseline achieved by a constant forecast
pb ≡ 0.5. Every score reported in §5 is therefore simultaneously an RPS and a Brier score, the two
being numerically identical for this market; this paper writes RPS throughout to match journal
convention, reserving the fully general multi-category form (10) for the forward-looking remark that
closes this section.

4.2    Standard errors: two conventions, not one
Every score reported below is a mean of per-game losses si = (pbi − Oi )2 , so its sampling error is
governed by the central limit theorem; two distinct standard errors nonetheless appear throughout
§5, and conflating them would understate the precision of every paired comparison this paper
reports. The first is the marginal plug-in standard error appropriate to a single forecaster’s mean
                            √
score, estimated by sd(si )/ n; conditional on the realized sequence of forecast probabilities pbi and
assuming calibration (qi = pbi ), Var(si | pbi ) = pbi (1 − pbi )(1 − 2pbi )2 ≤ 1/16, so, averaging independent
                                                                                            √
games, the conditional sampling p   standard error of the mean is at most 1/(4 n). This is only a
conditional scale reference—the 0.06/n figure quoted beside single-model scores—rather than
either an equality for the realized plug-in estimator or an unconditional bound when forecasts

                                                      12
themselves vary across maps. The second, and the one that governs every ∆ reported in this
paper, is the paired standard error appropriate to a comparison between two forecasters A and B
scored on identical games: writing di = sA        B
                                            i − si , the estimand is E[di ] and the correct standard
                               √               ¯
error is the empirical sd(di )/ n, with t = d/SE     referred to a standard normal distribution—a
Diebold–Mariano test under squared-error loss and independent games, no forecast horizon here
                                                         A         B            A     B
overlapping between games. Because  p Var(d) = Var(s ) + Var(s ) − 2ρ sd(s ) sd(s ), the paired
standard error scales roughly as 2(1 − ρ) times a single marginal standard error, and at the
per-game score correlations actually observed in this paper—ρ = 0.944 between the paper’s own two
candidate models, ρ ≈ 0.7 between model and market, ρ = 0.59 between model and the Cattelan
benchmark—the paired standard error runs from about the marginal size (ρ = 0.59) to roughly
three times smaller (ρ = 0.944) than the marginal plug-in bound. The marginal plug-in figure is
therefore a conservative scale reference for a single score and never the correct standard error of a
difference; every comparative claim in §5, including the headline parity result between the proposed
and second candidate models, uses the paired convention throughout, and per-league rows use
the same paired estimator restricted to each league’s games, read against a Bonferroni-corrected
threshold across the eight league-level comparisons.

4.3   Scope for the full ranked probability score
Because the per-map market reduces exactly to the Brier score, reporting RPS throughout this
paper is a matter of nomenclature rather than a distinct analysis. The genuinely multi-category use
of (10) would arise at the level of the series market rather than the map market: a best-of-three
(Bo3)—the format in which a match ends as soon as one team wins two maps—has an outcome
that can be ordered by net game margin, for instance the four-category ordering {team A wins 2–0,
A wins 2–1, B wins 1–2, B wins 0–2}, and (10) would then reward forecasts that place their mass
“close” to the true outcome on that ordinal scale rather than merely on the correct side of it. This
paper does not model the series-level market, leaving it as the natural setting in future work where
the full ranked probability score does work the Brier score cannot.


5     Results
All scores reported below are held-out RPS, equal to the Brier score for this two-outcome market
by (11), with lower values indicating better forecasts throughout. The subsections that follow run
in increasing strength of opponent, from league coverage (§5.1) through the classical benchmarks
(§5.2) and the second candidate model (§5.3) to the market itself (§5.5), with the ablations (§5.4)
placed after the architecture comparison they support. Every result in §5.1–§5.3 comes from the two
protocols of §3.3, which fit each game strictly before its own position, so no game can enter its own
training set; the separate market backtest of §5.5 enforces the same guarantee by a different route,
set out there, and its agreement with the independent walk-forward on the same window is reported
there as a coherence check. The second candidate model is fit throughout with λ1 = λ2 = 0.3, a
choice justified in §5.4 by a flat criterion surface, and in-sample Platt calibration; the proposed
model selects (λ, τ ) on training data alone, following the full sequence specified in §3.4.
    One protocol detail applies to every holdout table below: a test game is scored only if each team
has already appeared on the side it now plays, so that every model can produce a prediction and
the paired tests run on identical games (115 of 1,027 cross-region test rows are removed). The filter
isolates the unseen-team fallback, θb = 0 under both architectures; scored without it the second
candidate model lands at 0.2312, near 0.27 on the 115 fallback games against near 0.23 elsewhere,
so the fallback is usable rather than free.

                                                 13
5.1   League coverage across the analyses
One clarification is worth stating before any comparison, since the market comparison’s window is
easy to misread as evidence that only a small amount of data was fit. In the primary cross-region
analyses of §5.2–§5.3, every model is fit on the full corpus of §3.2 and evaluated on up to roughly
900 held-out games under the global split and on 4,605 games under the per-game walk-forward, in
both cases spanning every league in the corpus. The per-league fits reported immediately below are
the deliberate exception to this: Table 3 restricts both training and test data to one league at a time,
precisely in order to diagnose how each architecture behaves when it cannot draw on cross-region
pooling, and its results should be read as that diagnostic rather than folded into the full-corpus
picture. The matched-market comparison of §5.5, by contrast, is bounded by data availability rather
than by any modeling choice: Polymarket began listing per-game LoL markets only in October 2025,
so that comparison runs on the 928 matched maps found among the 973 corpus games inside that
window, approximately 95% coverage, with the per-league counts given alongside that comparison in
§5.5. The remaining roughly 4,200 corpus games predate market coverage and feed only the models’
own held-out evaluation, so the scores reported against the market in §5.5 and those reported on
the models’ own held-out sets are computed on different samples and are not directly comparable to
one another.
     The proposed model is unusual in fitting and predicting on every one of these slices without
exception: its ridge-shrunk strengths remain identifiable even on thin single-league designs where
classical random-effect fits can become outright singular (§2.3). Table 3 substantiates this claim
league by league. Refit within each league alone, the proposed model converges everywhere—no
slice produces a singular fit—and tracks the second candidate model within sampling noise on the
deeper leagues, identical on LCK and within roughly one marginal standard error on LPL, LEC,
and LCS, while being dramatically more accurate on the thin expansion league LCP, 0.2648 against
0.3055, precisely where the classical machinery is least stable. What destabilizes it there is not
its shrinkage—which is the same Gaussian prior the ridge applies (§2.2)—but the two steps the
proposed model does without: estimating the prior’s variance inside the likelihood, on a surface that
is flat and boundary-prone at these sample sizes, and fitting a separate calibration map on a training
window this thin. The per-league (λ, τ ) selections vary somewhat across leagues, as small training
tails select these hyperparameters noisily, consistent with the flat criterion surfaces documented in
§5.4; the cross-region results reported throughout the remainder of this section are insensitive to
this per-league variation.

Table 3: Per-league robustness of the proposed model: within-league fits, with training and test
restricted to one league under the global 0.2 time-based split and (λ, τ ) selected on each league’s
own training tail. The two-stage column repeats the second candidate model’s Brier on the identical
slices. Lower RPS is better.
                           League      ntr   nte   RPSproposed   RPStwo-stage
                           LCK      1,021    255        0.2137        0.2137
                           LPL      1,458    364        0.2281        0.2216
                           LEC        558    139        0.2529        0.2593
                           LCS        173     31        0.2383        0.2366
                           LCP        346     86        0.2648        0.3055




                                                   14
5.2   Benchmarks against the classical models
To isolate what a stable team strength buys over a purely dynamic specification, both architectures
are benchmarked against the dynamic Bradley–Terry model of Cattelan, Varin, and Firth (2013) fit
on the same data—the Layer-2 model of the road map, in exactly the notation of (2)–(4)—and,
from the opposite boundary, against the static Stefani line. The re-implementation places a logistic
link directly on the binary outcome,
                                                         B                R         
                      P (Oi = 1 | Fi− ) = expit β0 + γ1 Sb(i) (ti ) − γ2 Sr(i) (ti ) ,             (12)

                                                                          B , S R the same-side win-form
conditioning on the history Fi− of all results strictly before ti , with Sb(i) r(i)
EWMAs of (2) under a single shared decay λ. In words, (12) predicts blue’s win probability from
the two teams’ recent same-side records alone, on the same logistic scale the proposed model uses,
with a free intercept carrying the average blue-side advantage and nothing at all carrying either
team’s persistent quality. Three deliberate departures from Cattelan, Varin, and Firth’s (2013) own
specification only strengthen this baseline: the re-implementation initializes at zero rather than at
the league-wide prior-season mean, matching this paper’s own models’ convention so that it shares
the second candidate model’s form covariate exactly, an influence that decays geometrically and
is in any case covered by the fast-decay end of the λ grid; it adds a free intercept β0 , absorbing
the mean blue-side advantage in the role this paper’s own global intercepts play elsewhere; and,
where the original estimates its per-side smoothing parameters (λ1 , λ2 ) by two-step maximum profile
likelihood, the re-implementation sweeps a single shared λ across this paper’s grid and reports
the best configuration it attains—an oracle selection made on the evaluation set itself, which no
train-side estimate can beat. The re-implemented abilities remain purely dynamic—no separately
estimated stable level, so the form term alone carries the team signal—and the fit is an ordinary
logistic regression of Oi on the two side-form EWMAs, the decay profiled on a grid as for this
paper’s own form terms. At fixed λ it estimates three parameters against the proposed model’s four
plus ridge block and the candidate’s six (Table 1).
    Equation (12) is the proposed model (7) stripped of its stable team-strength block and first-pick
covariate—identical link, response, and λ-grid discipline—so the gap between them measures what a
shrunk team strength buys over pure dynamics. The candidate’s own gap against (12) bundles the
stable strength with its composite response and Platt map; the monotone pattern across λ below is
the diagnostic that the missing stable level, not the response choice, is the operative difference.

Table 4: Held-out RPS: the proposed model and the second candidate model against the classical
benchmarks—the canonical dynamic Bradley–Terry of Cattelan, Varin, and Firth (2013), swept
over λ, and the static Stefani line ((1) on the composite response, least-squares and BLUP-shrunk;
no form terms, so λ is inert)—cross-region, all years, global time-based 0.2 holdout (nte = 912).
Lower RPS is better.
                    Model                                                   λ      RPS
                    Cattelan dynamic BT                                    0.1   0.2351
                    Cattelan dynamic BT                                    0.3   0.2391
                    Cattelan dynamic BT                                    0.9   0.2462
                    Stefani static (1), least squares                      —     0.2301
                    Static boundary of (9) (γ1 =γ2 =0, BLUP-shrunk)        —     0.2268
                    Two-stage candidate (9)                                0.3   0.2257
                    Proposed (7)                                           0.1   0.2230



                                                    15
    The proposed model beats Cattelan, Varin, and Firth’s best configuration (λ = 0.1) by 0.0121
RPS, and the second candidate model beats it by 0.0094 (Table 4). The preferred decay is itself
diagnostic of what is happening: the re-implemented Cattelan model wants the slowest decay
on the grid, λ = 0.1, because its EWMA alone must carry the entire team signal and worsens
monotonically as memory shortens, whereas both of this paper’s own models tolerate substantially
faster decays because the stable block already holds each team’s long-run level, leaving the form term
to capture only recent form. This gap is the value of a stable, shrunk team strength over a purely
dynamic specification, demonstrated here empirically rather than only argued for on structural
grounds. Paired per-game inference on the holdout, second candidate model against Cattelan,
gives ∆ = −0.0094 with paired standard error 0.0052 (t = −1.82, p = 0.07)—the underlying score
correlation here is only 0.59, so the paired standard error sits close to the marginal one in this
particular comparison—and the larger-sample 4,605-game walk-forward corroborates the same
ordering with gaps of 0.0112 (proposed) and 0.0104 (second candidate), reinforced further by the
monotone λ pattern noted above.

5.2.1    The static classical benchmark
The classical picture is completed from the opposite boundary. Stefani’s static model (1)—time-
invariant per-side strengths, fit by least squares on the same composite response, the same Platt
map, and no form terms at all—scores 0.2301 on the identical holdout; the second candidate model’s
own static boundary, obtained by setting γ1 = γ2 = 0 in (9), the same architecture but with
REML/BLUP-shrunk strengths in place of a least-squares fit, improves this to 0.2268, so BLUP
shrinkage alone is worth 0.0033 (Table 4). Two readings follow from this pair of numbers. First, on
this corpus the static classical benchmark actually beats the dynamic one, 0.2301 against 0.2351: a
stable team identity carries more of the recoverable signal here than pure recent form does. Second,
the two blocks of (9) are far from symmetric in what they contribute: dropping the form terms
costs the second candidate model only 0.0011 (0.2257 → 0.2268), while the dynamic-only classical
model, in its logistic form (12), sits a full 0.0083 further back at 0.2351. With both boundaries now
priced, the holdout progression reads cleanly: dynamic-only at 0.2351, static-only at 0.2268, both
blocks together at 0.2257, and the proposed one-stage completion at 0.2230.

5.2.2    Per-game walk-forward corroboration
The same comparison under the per-game cadence—refitting at every match on all strictly prior
games, the protocol §5.5’s market comparison itself inherits—gives the same verdict on a substantially
larger scored set. On an identical 4,605-game set, scored once at least 500 prior games exist and
both teams have been seen on their respective sides under an identically implemented rule for both
models, the proposed model attains RPS = 0.2207 against the best Cattelan configuration’s 0.2319
at λ = 0.1—a 0.0112 gap under an identical link and response—while the second candidate model
attains 0.2215, a 0.0104 gap. The stable-strength advantage therefore holds across both architectures
and both validation protocols this paper reports.

5.3     Architecture head-to-head: the proposed model versus the second candidate
        model
This subsection carries the evidence that selects the proposed model (7) from the general one-stage
family (6): the head-to-head comparison against the second candidate model, and the d-ablation that
ultimately fixes the latent update’s input at the binary result alone. The full feature pool considered,
d = 10, is every directional summary of the previous same-side game available in the telemetry—the

                                                  16
win indicator, the three composite margins, inhibitors, barons, dragons, the fifteen-minute gold
and kill differentials, and game duration—each an own-minus-opponent quantity within that game
and sign-flipped for red, except duration, which has no direction and enters z-standardized instead.
The family’s motivating construction folds these features directly into the latent state: replace the
proposed model’s binary recursion input with a learned linear combination w⊤ x(t− ) of all such
features, and estimate feature weights, side scales, and team strengths jointly against the log-loss
of Oi . Because the EWMA operator is linear, EWMAλ (w⊤ x) = w⊤ EWMAλ (x), so that model is
exactly (6)—a logistic regression on per-feature form EWMAs plus the ridge-penalized signed team
block of (8), an exact reduction rather than an approximation, which is what makes the comparison
clean. Three nested variants are fit, with (λ, τ ) selected on training data only and the holdout, test
filter, and paired protocol identical throughout, on the global 0.2 time-based holdout of §3: d = 1
(outcome, exactly the proposed model of (7)), d = 4 (core4, adding the second candidate model’s
own three margins, but now learned rather than fixed), and d = 10 (all, every feature in the pool).

Table 5: One-stage family versus the second candidate model, cross-region all-years holdout
(nte = 912). ∆ is the paired per-game Brier difference Briertwo-stage − Briervariant (positive means
the variant is nominally ahead), with the Diebold–Mariano standard error of §4.2. Calibration
slopes are held-out (ideal value 1.0); the one-stage probabilities are native, while the candidate
carries its in-sample Platt map. The Cattelan row is the external benchmark’s best configuration
on the same holdout and enters no paired test. Lower RPS is better.
   Model                                     d     RPS      LogLoss   ∆ vs. two-stage        p   Calib. slope
   One-stage outcome (proposed)              1   0.2230      0.6371           +0.0027     0.22          0.88
   One-stage core4                           4   0.2242      0.6413           +0.0015     0.44          0.77
   One-stage all                            10   0.2258      0.6454           −0.0001     0.97          0.74
   Two-stage candidate (9)                  —    0.2257      0.6492                —        —           0.67
   Cattelan dynamic BT (λ=0.1; §5.2)        —    0.2351          —                 —        —             —



Table 6: Association between the binary outcome Oi and the directional (blue−red) end-of-game
and at-15-minute features, full corpus (n = 5,135): Pearson correlation with Oi , single-feature
ROC AUC, and the share of blue-win games with a positive value. The three composite margins
(gold, kills, towers; starred) are mutually correlated 0.89–0.96; §5.4 draws the consequence for the
composite response.
                       Feature (blue − red)      Corr. with Oi   AUC      % blue-win, +
                                   a
                       Gold (final)                 +0.919       0.997         97.3
                       Kills (final)a               +0.869       0.989         95.1
                       Towers (final)a              +0.939       1.000         99.0
                       Inhibitors (final)           +0.878       1.000         98.0
                       Barons (final)               +0.714       0.907         75.8
                       Dragons (final)              +0.644       0.875         64.3
                       Gold @15                     +0.483       0.784         72.8
                       Kills @15                    +0.404       0.731         59.1
                 a
                     the three margins entering the second candidate model’s composite (§2.3).

    Five findings organize the evidence in Tables 5 and 6. First, on the full corpus the two
architectures are equivalent on the declared forecasting target: the full one-stage model dead-ties the
second candidate model on the holdout (∆ = −0.0001, p = 0.97) and trails it by roughly one standard


                                                       17
error on the 4,605-game per-game walk-forward (0.2227 against 0.2215), while the proposed model
itself walk-forwards to 0.2207 against the candidate’s 0.2215, a paired ∆ = +0.0008 in the proposed
model’s favor (p = 0.40, score correlation 0.944); no variant of the one-stage family separates from
the second candidate model in either direction on the whole corpus. Second, adding features to the
latent update only hurts: held-out RPS is numerically monotone in d (0.2230 < 0.2242 < 0.2258;
∆ = −0.0012, p = 0.32 for d=1 against d=4; ∆ = −0.0016, p = 0.25 for d=4 against d=10;
∆ = −0.0028, SE 0.0020, p = 0.16 end to end—consistent in ordering, with the mechanism rather
than the p-values carrying the finding), and that mechanism is that the end-game features are
mutually correlated 0.89–0.96 (Table 6), so the learned weights fit noise visibly: the win indicator
itself receives a large negative weight (−0.81 at d = 4, −0.88 at d = 10) and signs flip between
variants. The a-priori composite the candidate fixes instead is therefore not a cost inherent to the
two-stage design; learning it from data is a cost specific to the one-stage design at this corpus’s
size. Third, the one-stage design’s genuine advantage is native calibration: held-out slopes of 0.88,
0.77, and 0.74 for d = 1, 4, 10 respectively, against the second candidate model’s in-sample-Platt
slope of 0.67 on the same holdout, and on the full walk-forward the proposed outcome variant is
essentially perfectly calibrated, with intercept −0.009 and slope 0.995; an out-of-fold refit of the
candidate’s Platt map (Niculescu-Mizil and Caruana, 2005) recovers most though not all of this
gap (0.2257 → 0.2248; the protocol and its bounded implication are given in Appendix A). Fourth,
the ranking axis is unaffected: predictive rank validity—the Spearman correlation between a
model’s end-of-training team ranking and those teams’ realized test-window win rates, over the
50 teams with at least five test games—is 0.438 for the proposed model’s θ block against 0.436
for the candidate’s BLUPs. Fifth, the equivalence holds on every time window examined: sliced
by quarter across the walk-forward the paired difference never leaves ±0.004, and on the market
window itself (October 2025 onward, n = 963 walk-forward-scored games; ten of the 973 corpus
games in the window are seen-on-side exclusions and so receive no forecast) it is ∆ = +0.0003
(paired SE 0.0019, 95% CI −0.003 to +0.004)—a dead tie in exactly the window where deployment
happens—and the result is insensitive to the proposed model’s own (λ, τ ) selection within the grid,
with the walk-forward scoring 0.2207 at both λ = 0.1 and λ = 0.9. The proposed model is therefore
adopted on simplicity, since the accuracy of the two architectures is indistinguishable: no composite
response, no calibration step, four coefficients plus a shrunk team block, against the second candidate
model’s REML shrinkage, which self-tunes inside its own likelihood with no (λ, τ ) schedule of its own
to select. The comparison was specified before it was run, with the prediction that the one-stage
family would tie the second candidate model or trail it within paired noise; that held, with the
monotone degradation in d the surprise beyond it.

5.4   Ablations
Four design choices are settled by ablation rather than by construction, and all four are stable
enough that no conclusion elsewhere in this paper depends sensitively on any of them. The EWMA
decay λ leaves the proposed model essentially unaffected, as the full six-point sweep of Appendix B
confirms: the per-game walk-forward scores an identical 0.2207 at both ends of the grid, λ = 0.1
and λ = 0.9, and the holdout selection procedure of §3.4 picks λ = 0.1 on a criterion surface that is
shallow near its optimum; the second candidate model’s own decay, fixed a priori at λ1 = λ2 = 0.3,
rests on the same flatness, observed across the same [0.1, 0.9] grid in earlier scans of the two-stage
family, so that no conclusion in this paper moves for any decay in that range. The ridge strength
τ is selected on training data alone over a grid spanning 0.25 to 16; the cross-region walk-forward
selects (λ, τ ) = (0.9, 4) on its first 500-game window, with training-window log-loss moving by
less than 0.005 across τ ∈ {2, 4, 8}—the decay sitting at the opposite end of the grid from the


                                                  18
holdout’s selection, at identical cost on the flat walk-forward surface documented above; under the
correspondence of §2.2 the selected τ = 4 corresponds to σ bθ = 0.5 on the log-odds scale. The feature
dimension d is the central ablation, treated in full in §5.3. Finally, response construction on
the second candidate model’s side proves similarly inert: every dense re-weighting of the composite
response tried is identical to four decimal places (0.2257), dropping the outcome term entirely
changes nothing (0.2257 → 0.2257, with every individual league within 0.0016 of its baseline), and
single-margin responses stay within 0.0010 of the reference composite, all a consequence of the
margins’ near-collinearity (Table 6). The candidate’s reported number is therefore not an artifact of
its response construction, and by the same logic its composite carries no information the binary
result lacks.

5.5     External benchmark: model versus market
5.5.1    Backtest construction: the self-training guard
The market backtest refits the model for each predicted game on strictly prior games, and it defines
“prior” by game identifier rather than by a timestamp cutoff: the predicted game is excluded from its
own training window explicitly. The rule matters because scheduled and actual start times differ in
resolution—the former recorded to the minute, the latter to the second from the raw telemetry, and
typically under a minute apart—so a training set built from a timestamp cutoff can silently admit
the predicted game’s own row, carrying its own outcome in the response, into the very window used
to fit the model that predicts it. The resulting self-training is easy to mistake for genuine forecasting
performance, since its signatures are a calibration slope sharper than a well-calibrated forecast
should ever produce and an implausibly precise paired advantage over an independent walk-forward
evaluation of the identical model on the identical maps. Two safeguards verify the guarantee here.
By construction, the holdout and walk-forward protocols of §3.3 order games positionally and fit
strictly before each predicted position, so no game can enter its own training set under either. And
as a coherence check on the backtest itself, its model Brier on the market window, 0.2260, agrees
closely with the independent walk-forward evaluated on the identical window, 0.2263—two pipelines
sharing no code path arriving at the same score on the same maps.

5.5.2    The result
Table 7 reports both architectures against the market on this backtest: the second candidate model
directly from the backtest’s own exact matching (n = 928, including the 136 decider maps whose
price is derived from the series-winner contract, a fallback that applies market-side only, since
the model side remains an ordinary per-game prediction throughout), and the proposed model
by joining its walk-forward predictions to the same maps by exact game id (924 of the 928, the
remaining four falling outside the walk-forward’s own scored set). Three facts follow. First, on
per-game contracts the forecasts are statistically indistinguishable from the market: excluding the
fallback-priced deciders, ∆ = +0.005 (95% CI −0.004 to +0.014) for the second candidate model
and ∆ = +0.006 (−0.002 to +0.015) for the proposed model, intervals that both span zero and
bound any market edge below 0.015 Brier and any model edge below 0.004. Second, including
the deciders, the market is modestly ahead overall (∆ = +0.0093, t = +2.24, proposed model;
∆ = +0.0097, t = +2.24, second candidate model; p = 0.025 for both), consistent with deciders
being maximal-uncertainty games between closely matched teams, exactly where the market’s day-of
information is worth the most; this deficit is concentrated at the cross-region Worlds slice, the only
one to survive a Bonferroni ×8 correction for either architecture, while the dense domestic leagues
sit at parity—LPL nominally model-ahead, LCK a dead heat, First Stand nominally model-ahead.

                                                   19
Third, the two architectures tie on the market subset exactly as they do everywhere else in this
paper (∆ = −0.0004 paired on the identical 924 maps, p = 0.84), and both are sanely calibrated on
this window, with slopes of 0.72 for the second candidate model and 0.87 for the proposed model,
the latter from the walk-forward predictions’ own window calibration.

Table 7: Market comparison from the backtest of 2026-07-21: paired per-game Brier difference
∆ = RPSmodel − RPSmarket (negative means the model is ahead) with paired t. The second candidate
model (9) is evaluated on the backtest’s 928 exactly-matched maps; the proposed model (7) on
the 924 it joins by exact game id. The “per-game only” row excludes the 136 maps whose price
is the series-winner fallback. League-level rows are read against a Bonferroni ×8 threshold (§5.5).
CBLOL’s n = 14 is too sparse to support a league-level reading on its own, and its row is reported
for completeness rather than as an interpretable per-league result.
                                           Proposed (7)           Two-stage candidate
                     League            n         ∆            t    n        ∆        t
                     LPL             316    −0.003        −0.45   316   −0.008   −1.15
                     First Stand      33    −0.008        −0.22    33   −0.031   −1.50
                     LCK             244    +0.002        +0.25   244   +0.001   +0.13
                     LCP             149    +0.015        +1.38   151   +0.032   +2.48
                     LEC              96    +0.020        +1.41    96   +0.032   +1.84
                     LCS              22    +0.037        +2.28    24   +0.026   +1.05
                     Worlds           50    +0.069        +4.61    50   +0.050   +3.52
                     CBLOL            14    +0.077        +1.26    14   +0.094   +1.50
                     Overall         924    +0.009        +2.24   928   +0.010   +2.24
                     Per-game only   788    +0.006        +1.41   792   +0.005   +1.08

   The honest headline is therefore parity on the market’s own per-game contracts—in the bounded
sense given above, not merely a failure to reject a null hypothesis—together with a modest market
edge concentrated on series deciders: a transparent paired-comparison forecaster matches a real
prediction market across the dense domestic leagues, sits nominally ahead on the deepest one of
them (LPL), and pays a real cost only where cross-region strength transfer is hardest (Worlds) and
on decider maps—exactly the games where day-of information the model does not consume is worth
the most.
   Figure 1 traces the ridge-MAP strengths behind these forecasts over time, in the spirit of the
smoothed-ability plots of Cattelan, Varin, and Firth (2013): the stable block θ the proposed model
adds to Layer 2 moves slowly and separates teams persistently, which is the qualitative behavior the
parity result above is built on.
   Figure 2 gives the distribution behind Table 7’s league-level means, and reading the two together
sharpens the verdict: the dense domestic leagues overlap the market almost completely, while the
Worlds panel separates visibly, so the aggregate deficit is a property of one cross-region slice rather
than of the forecaster everywhere. The CBLOL panel, at n = 14, is too sparse to read on its own.

5.5.3   How the market sample is constructed
A map enters the comparison when a Polymarket per-map “Game N winner” contract is matched
to it by tournament slug and team codes and carries a usable quote strictly before the game’s start,
anchored to the first telemetry frame: the last pre-start price is used, and quotes more than six
hours older than the start are rejected as stale (47 games; one further market was unsettled, giving
48 exclusions in total). Deciding games of a series frequently carry no per-map contract of their

                                                     20
                                                     LCK                                                           LPL
    ridge-MAP team strength θ̂ t (log-odds)   1.75
                                                                                                           GEN
                                              1.50
                                                                                                           HLE
                                              1.25                                                                                                                    BLG
                                                                                                           T1
                                              1.00                                                                                                                    TES
                                              0.75
                                                                                                           DK                                                         JDG
                                              0.50

                                              0.25                                                                                                                    WBG

                                              0.00

                                                      Apr Jul Oct Jan Apr Jul Oct Jan Apr Jul                       Apr Jul Oct Jan Apr Jul Oct Jan Apr Jul
                                                     2024 2024 2024 20252025 2025 2025 20262026 2026               2024 2024 2024 20252025 2025 2025 20262026 2026

                                                                    DK       T1        HLE     GEN                            TES        WBG       JDG       BLG




Figure 1: Smoothed team-strength trajectories from the proposed model. Each line is the ridge-MAP
stable strength θbt of one team (log-odds scale; zero is the league average, dashed) re-estimated at
monthly checkpoints by refitting (7) on all games strictly before the checkpoint, at the walk-forward’s
frozen pair (§5.4), for the four most-played teams in two leagues: on the left the LCK, with DK
(Dplus KIA), T1, HLE (Hanwha Life Esports), and GEN (Gen.G); on the right the LPL, with TES
(Top Esports), WBG (Weibo Gaming), JDG (JD Gaming), and BLG (Bilibili Gaming). A line
begins at the team’s first game in the corpus. Fits use the corpus as of August 2026 (5,233 games)
rather than the frozen corpus behind the tables, so the trajectories are illustrative rather than a
reported result; markers distinguish teams in print.


                                                           Market           Proposed (7)           Two-stage candidate (9)          0.25 = uninformative forecast
    per-map Brier score (lower is better)




                                              0.8



                                              0.6



                                              0.4



                                              0.2



                                              0.0
                                                           LPL           First Stand      LCK           LCP          LEC          LCS           Worlds      CBLOL
                                                        (n = 316)         (n = 33)     (n = 244)     (n = 151)     (n = 96)     (n = 24)       (n = 50)    (n = 14)



Figure 2: Per-map Brier score by league for the market price, the proposed model (7), and the
second candidate model (9) on the matched maps of Table 7 (proposed model on the 924 maps
joined by game id, the others on all 928; decider-fallback prices included, as in Table 7’s rows).
Boxes span the interquartile range (IQR) with the median marked, whiskers extend to the most
extreme observations within 1.5 IQR of the quartiles, and points beyond are shown individually;
the dashed line at 0.25 is the score of an uninformative constant forecast. Lower is better.


                                                                                                           21
own; for 136 of the 928 maps (15%; 138 recovered, two subsequently rejected by the price filters) the
price is instead taken from the series-winner contract at the decider point, where the two contracts
necessarily coincide. These fallback-priced maps are included in the “Overall” rows of Table 7 and
excluded from its “per-game only” sensitivity row; accepted quotes have a median staleness of 0.5
minutes (maximum 106), so the six-hour cutoff is not binding near its own boundary.

5.5.4   Scope
The market comparison reported here is a forecasting-quality result only, model RPS against
market-implied RPS: Polymarket functions throughout this paper strictly as an external forecasting
benchmark, and nothing built on top of these probabilities is discussed further here.


6    Conclusion
This paper set out to establish how much modeling machinery a pre-game win-probability forecaster
for professional League of Legends actually requires, and whether the resulting forecasts stand up
against a liquid prediction-market forecasting benchmark. The answer to the first question is a
deliberately minimal one-stage logistic model—a same-side exponentially-weighted form covariate for
each team, a schedule-assigned first-pick indicator, and a ridge-shrunk team strength that is exactly
the maximum-a-posteriori solution of a logistic mixed model—which prices professional LoL maps
as accurately as the strongest two-stage composite mixed model the authors could build, across six
regional leagues and three international events spanning 2024–2026. That the two architectures
tie is itself the finding, since the second candidate model was built as the strongest two-stage rival
available (§2.3) and the tie therefore measures a ceiling rather than a weak opponent.
    A methodological point carries weight beyond this paper’s own results. The holdout discipline
used throughout is a global time-based split paired with an independent per-game walk-forward, not
a contrast between within-season and global protocols, because ordinary random cross-validation is
invalid whenever a model’s covariates are themselves path-dependent: the exponentially-weighted
form terms central to every dynamic model in this paper depend on each team’s strictly prior
games, so a random fold would let future results leak into the very features used to predict the past.
Reporting both protocols together, rather than either alone, is what lets the paper’s central parity
claim stand on more than a single arbitrary split.
    The practical recommendation that follows is the proposed one-stage model, and it is a recom-
mendation made on parsimony rather than on superior accuracy. It carries no composite response
variable, requires no post-hoc calibration step, and is natively almost perfectly calibrated out of
sample, with a walk-forward slope of 0.995, while remaining statistically indistinguishable from the
second candidate model on every protocol and time window this paper examines. External validity
follows a similar pattern: the forecasts are statistically indistinguishable from Polymarket on the
market’s own per-game contracts, and the market retains only a modest edge, concentrated on the
cross-region Worlds slice and on series-decider maps—exactly the settings where day-of information
the model does not consume, roster news, patch-day adjustments, and the like, is worth the most.
    Three limitations qualify these results. The absolute RPS reported for the second candidate
model, and for the classical re-fits built on the same composite response, is mildly inflated by in-
sample Platt calibration, though relative comparisons throughout the paper remain approximately
unbiased under this scheme; an out-of-fold refit recovers most though not all of the resulting gap,
by a margin small enough to leave every comparison in the paper intact (Appendix A). Classical
random-effect fits, independent of this paper’s own architecture, become singular on thin single-
league designs, the expansion league LCP being the running illustration, a limitation the proposed

                                                 22
model’s ridge shrinkage does not share. Finally, the underlying data pipeline depends on three data
sources that share no common join key, and on two source properties documented in §3.2, neither of
which the providers enforce or announce; a corpus assembled this way carries a standing exposure
to silent, provider-side convention changes that future extensions of this work should anticipate.
    Three directions are left for future work. A series-level ranked probability score for Bo3 market
modeling is the one setting in this paper’s own scope where the fully general, multi-category form
of (10) would do work the Brier score cannot, since a series outcome carries a genuine ordinal
structure that a single map’s binary result does not. An out-of-fold Platt scheme could be adopted
as the second candidate model’s default calibration procedure rather than retained only as the
robustness check reported in §5.3, closing the one respect in which that model’s absolute scores
are not directly comparable to the proposed model’s own native calibration. And a live, in-game
model consuming per-frame telemetry as a match unfolds is a natural downstream consumer of the
pre-game forecaster developed here, though building one is explicitly outside this paper’s scope,
which is confined throughout to information available before a map begins.


Acknowledgements
M.-R. G. thanks Teahouse Finance for providing the Claude credits and the computing resources
used for this project.


Funding
S.-N. T. is grateful for the financial support from the National Science and Technology Council of
Taiwan under grant 114-2115-M-007-012-MY3, “Mathematical Foundation of Automated Market
Makers.”


A     Calibration: in-sample versus out-of-fold Platt scaling
The second candidate model’s Platt map is fit in-sample throughout §5, on the same training-window
predictions the mixed model of (9) was itself fit to (§3.4); §5.3 reports an out-of-fold refit recovering
most though not all of the resulting gap, 0.2257 to 0.2248 on the global holdout. The two schemes
differ only in where the Platt map’s own two parameters are fit: the out-of-fold variant holds an
inner slice of the training window back from the mixed-model fit, computes that model’s predictions
on the held-back slice, and fits the map there before applying it to the outer test set—avoiding
the over-separation that training-window predictions carry by construction (Niculescu-Mizil and
Caruana, 2005). The 0.0009 correction bounds the calibration scheme’s contribution without erasing
it: every paired difference in §5 applies the same in-sample scheme uniformly to that model, so
a shared inflation of its absolute score favors it in no comparison, and at 0.0009 the correction is
smaller than the 0.2257-against-0.2230 gap it might be thought to explain and smaller still than the
paired standard errors governing the parity claim of §5.3.


B     EWMA decay grid search
The proposed model’s decay λ is selected on training data alone from the grid specified in §3.4,
{0.1, 0.2, 0.3, 0.5, 0.7, 0.9}. Section 5.4 reports that the per-game walk-forward score is identical to
four decimal places, 0.2207, at both ends of this grid, λ = 0.1 and λ = 0.9. This appendix confirms


                                                   23
that the flatness extends across the interior of the grid rather than being an artifact of the two
endpoints alone. Table B.1 reports a full six-point diagnostic sweep of the per-game walk-forward
with τ held at its selected value of 4, run on the corpus as it stood in August 2026 (n = 4,703 scored
games): the Brier score varies by 0.0002 in total across the whole grid, and the log-loss by 0.0006,
with no interior point distinguishable from either endpoint. Two features of the table need stating
explicitly. Its level sits about 0.0005 above the 0.2207 reported in §5.4 because the corpus had
grown by 98 games between the frozen-corpus runs behind the main results and this later sweep;
the two are therefore not directly comparable as levels, and it is the flatness across λ, not the level,
that this appendix establishes. And the sweep is a diagnostic measurement of the criterion surface
rather than a selection procedure: λ is selected on training data alone under §3.4’s protocol, never
on the walk-forward scores tabulated here.

Table B.1: Diagnostic sweep of the EWMA decay λ for the proposed model, per-game walk-forward
with τ = 4 fixed, August 2026 corpus (n = 4,703 scored games); lower is better for both scores. The
total Brier spread across the grid is 0.0002. Levels sit above §5.4’s 0.2207 because the corpus had
grown by 98 games between the two runs; the flatness, not the level, is this table’s claim.
                     λ             0.1      0.2      0.3      0.5      0.7      0.9
                     Brier      0.2212   0.2210   0.2210   0.2210   0.2211   0.2212
                     LogLoss    0.6323   0.6318   0.6317   0.6318   0.6320   0.6323


    No conclusion reported anywhere in this paper depends on the specific decay selected within
this range.


References
Daniel Barry and J. A. Hartigan. Choice models for predicting divisional winners in major league
 baseball. Journal of the American Statistical Association, 88:766–774, 1993. doi: 10.2307/2290761.
 URL https://doi.org/10.2307/2290761.

Ralph Allan Bradley and Milton E. Terry. Rank analysis of incomplete block designs: I. The
 method of paired comparisons. Biometrika, 39:324–345, 1952. doi: 10.2307/2334029. URL
 https://doi.org/10.2307/2334029.

Manuela Cattelan, Cristiano Varin, and David Firth. Dynamic Bradley–Terry modelling of sports
 tournaments. Journal of the Royal Statistical Society: Series C (Applied Statistics), 62:135–150,
 2013. doi: 10.1111/j.1467-9876.2012.01046.x. URL https://doi.org/10.1111/j.1467-9876.
 2012.01046.x.

Anthony Costa Constantinou and Norman Elliott Fenton. Solving the problem of inadequate scoring
  rules for assessing probabilistic football forecast models. Journal of Quantitative Analysis in Sports,
  8:1–14, 2012. doi: 10.1515/1559-0410.1418. URL https://doi.org/10.1515/1559-0410.1418.

Arpad E. Elo. The Rating of Chessplayers, Past and Present. Arco Publishing, New York, NY,
  USA, 1978. ISBN 978-0668047210.

Edward S. Epstein. A scoring system for probability forecasts of ranked categories. Journal of
 Applied Meteorology, 8:985–987, 1969. doi: 10.1175/1520-0450(1969)008<0985:ASSFPF>2.0.CO;2.
  URL https://doi.org/10.1175/1520-0450(1969)008<0985:ASSFPF>2.0.CO;2.


                                                   24
Ludwig Fahrmeir and Gerhard Tutz. Dynamic stochastic models for time-dependent ordered paired
  comparison systems. Journal of the American Statistical Association, 89:1438–1449, 1994. doi:
  10.1080/01621459.1994.10476882. URL https://doi.org/10.1080/01621459.1994.10476882.

Mark E. Glickman. Parameter estimation in large dynamic paired comparison experiments. Journal
 of the Royal Statistical Society: Series C (Applied Statistics), 48:377–394, 1999. doi: 10.1111/
 1467-9876.00159. URL https://doi.org/10.1111/1467-9876.00159.

Tilmann Gneiting and Adrian E. Raftery. Strictly proper scoring rules, prediction, and esti-
  mation. Journal of the American Statistical Association, 102:359–378, 2007. doi: 10.1198/
  016214506000001437. URL https://doi.org/10.1198/016214506000001437.

Min-Ren Guan. Analyzing dynamic abilities of teams in sports events. Master’s thesis, Institute of
 Applied Mathematical Sciences, National Taiwan University, Taipei, Taiwan, 2020.

David A. Harville. Maximum likelihood approaches to variance component estimation and to
 related problems. Journal of the American Statistical Association, 72:320–338, 1977a. doi:
 10.1080/01621459.1977.10480998. URL https://doi.org/10.1080/01621459.1977.10480998.

David A. Harville. The use of linear-model methodology to rate high school or college football
 teams. Journal of the American Statistical Association, 72:278–289, 1977b. doi: 10.2307/2286789.
 URL https://doi.org/10.2307/2286789.

Charles R. Henderson. Best linear unbiased estimation and prediction under a selection model.
 Biometrics, 31:423–447, 1975. doi: 10.2307/2529430. URL https://doi.org/10.2307/2529430.

Victoria J. Hodge, Sam Devlin, Nick Sephton, Florian Block, Peter I. Cowling, and Anders Drachen.
  Win prediction in multiplayer esports: Live professional match prediction. IEEE Transactions on
  Games, 13:368–379, 2021. doi: 10.1109/TG.2019.2948469. URL https://doi.org/10.1109/TG.
  2019.2948469.

Robbie Jadowski and Stuart Cunningham. Statistical models for predicting results in profes-
 sional League of Legends. In Matthias Wölfel, Johannes Bernhardt, and Sonja Thiel, editors,
 ArtsIT, Interactivity and Game Creation, pages 138–152, Cham, Switzerland, 2022. Springer
 International Publishing. doi: 10.1007/978-3-030-95531-1_10. URL https://doi.org/10.1007/
 978-3-030-95531-1_10.

Philip Z. Maymin. Smart kills and worthless deaths: eSports analytics for League of Legends.
 Journal of Quantitative Analysis in Sports, 17:11–27, 2021. doi: 10.1515/jqas-2019-0096. URL
  https://doi.org/10.1515/jqas-2019-0096.

Alexandru Niculescu-Mizil and Rich Caruana. Predicting good probabilities with supervised learning.
  In Proceedings of the 22nd International Conference on Machine Learning (ICML 2005), volume
  119 of ACM International Conference Proceeding Series, pages 625–632, New York, NY, USA,
  2005. ACM. doi: 10.1145/1102351.1102430. URL https://doi.org/10.1145/1102351.1102430.

H. D. Patterson and R. Thompson. Recovery of inter-block information when block sizes are unequal.
  Biometrika, 58:545–554, 1971. doi: 10.1093/biomet/58.3.545. URL https://doi.org/10.1093/
  biomet/58.3.545.

John C. Platt. Probabilistic outputs for support vector machines and comparisons to regularized
  likelihood methods. In Alexander J. Smola, Peter J. Bartlett, Bernhard Schölkopf, and Dale

                                                25
  Schuurmans, editors, Advances in Large Margin Classifiers, pages 61–74. MIT Press, Cambridge,
  MA, USA, 1999.

Raymond T. Stefani. Football and basketball predictions using least squares. IEEE Transactions
 on Systems, Man, and Cybernetics, 7:117–121, 1977. doi: 10.1109/TSMC.1977.4309666. URL
  https://doi.org/10.1109/TSMC.1977.4309666.




                                              26
